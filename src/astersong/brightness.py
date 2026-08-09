"""The brightness-decline-to-pitch mapping: AsterSong's first, and so far only,
implemented rule.

The rule, as documented in the project's design pages (docs-mockup, Mapping
page, rule 1 "Brightness to pitch"): brightness sets the frequency of the tone;
the mapping is logarithmic in flux, which is linear in magnitude, so equal
steps in magnitude are equal musical intervals; magnitudes are inverted, so a
smaller magnitude is brighter, and brighter reads higher; the dimmest sample
maps to ``f_lo`` and the brightest to ``f_hi``.

Determinism: every output sample is a pure function of the arguments. There is
no randomness, no clock, no environment read, no learned parameter, and all
arithmetic is float64 elementwise work (no BLAS, no FFT). Given the same inputs
on the same platform and NumPy build, the rendered bytes are identical; a
golden checksum in the test suite guards the mapping against silent change.
"""

from __future__ import annotations

import os

import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44_100      # Hz, CD-standard mono
F_LO = 220.0              # Hz, dimmest endpoint (A3)
F_HI = 1760.0             # Hz, brightest endpoint (A6); 220 -> 1760 is 3 octaves
AMPLITUDE = 0.8           # constant; loudness carries no data
FADE_SECONDS = 0.05       # raised-cosine fade at each end, click suppression

INT16_FULL_SCALE = 32767.0


def magnitude_to_frequency(mag, mag_bright, mag_dim, f_lo=F_LO, f_hi=F_HI):
    """Map apparent magnitude(s) to frequency in Hz.

    Linear in magnitude, logarithmic in frequency:

        f(m) = f_hi * (f_lo / f_hi) ** ((m - m_bright) / (m_dim - m_bright))

    so f(mag_bright) == f_hi exactly, f(mag_dim) == f_lo exactly, and one
    magnitude step is always the same musical interval. A degenerate span
    (mag_bright == mag_dim) maps everything to the geometric mean
    sqrt(f_lo * f_hi), a constant tone.
    """
    mag = np.asarray(mag, dtype=np.float64)
    if mag_dim == mag_bright:
        x = np.full(mag.shape, 0.5)
    else:
        x = (mag - mag_bright) / (mag_dim - mag_bright)
    return f_hi * (f_lo / f_hi) ** x


def render_brightness_decline(
    duration_days,
    start_magnitude,
    end_magnitude,
    compression_seconds,
    out_path=None,
    *,
    f_lo=F_LO,
    f_hi=F_HI,
    sample_rate=SAMPLE_RATE,
    amplitude=AMPLITUDE,
    fade_seconds=FADE_SECONDS,
):
    """Render a linear brightness decline as a pitch glide and return int16 PCM.

    Parameters
    ----------
    duration_days : float
        The real span of the decline in days. With a linear decline the
        waveform depends only on the magnitude endpoints; this parameter
        defines the documented compression factor
        (duration_days * 86400 / compression_seconds) and keeps the signature
        ready for non-linear light curves.
    start_magnitude, end_magnitude : float
        Apparent magnitudes at the start and end of the decline. Smaller is
        brighter (astronomical convention); brighter reads higher in pitch.
    compression_seconds : float
        Playback length. The whole record span is fit to this by one linear
        factor (the Time-to-tempo convention).
    out_path : str | os.PathLike | None
        If given, the rendered audio is written there as a mono 16-bit PCM WAV.

    Returns
    -------
    numpy.ndarray of int16, shape (n_samples,)
    """
    if not (duration_days > 0):
        raise ValueError("duration_days must be positive")
    if not (compression_seconds > 0):
        raise ValueError("compression_seconds must be positive")
    if not (0 < f_lo < f_hi):
        raise ValueError("need 0 < f_lo < f_hi")
    if not (0 < amplitude <= 1):
        raise ValueError("amplitude must be in (0, 1]")
    if not (isinstance(sample_rate, int) and sample_rate > 0):
        raise ValueError("sample_rate must be a positive integer")

    n = int(round(compression_seconds * sample_rate))
    if n < 2:
        raise ValueError("compression_seconds too short for this sample_rate")

    # One linear factor carries record time to playback time.
    u = np.linspace(0.0, 1.0, n)
    mag = start_magnitude + (end_magnitude - start_magnitude) * u

    m_bright = min(start_magnitude, end_magnitude)
    m_dim = max(start_magnitude, end_magnitude)
    freq = magnitude_to_frequency(mag, m_bright, m_dim, f_lo=f_lo, f_hi=f_hi)

    # Phase-continuous synthesis: integrate instantaneous frequency rather
    # than evaluating sin(2*pi*f(t)*t), which clicks when f varies.
    phase = (2.0 * np.pi / sample_rate) * np.cumsum(freq)
    y = np.sin(phase)

    # Raised-cosine fades at both ends remove the start/end discontinuity.
    k = min(int(round(fade_seconds * sample_rate)), n // 2)
    env = np.ones(n)
    if k > 0:
        ramp = 0.5 - 0.5 * np.cos(np.pi * np.arange(k, dtype=np.float64) / k)
        env[:k] = ramp
        env[-k:] = ramp[::-1]

    pcm = np.rint(y * env * (amplitude * INT16_FULL_SCALE)).astype(np.int16)

    if out_path is not None:
        wavfile.write(os.fspath(out_path), sample_rate, pcm)
    return pcm
