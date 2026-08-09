"""The mapping math and the rendered WAV's format."""

import io
import math

import numpy as np
import pytest
from scipy.io import wavfile

from astersong import (
    AMPLITUDE,
    F_HI,
    F_LO,
    magnitude_to_frequency,
    render_brightness_decline,
)


def test_endpoints_exact():
    assert magnitude_to_frequency(-6.0, -6.0, 6.0) == F_HI
    assert magnitude_to_frequency(6.0, -6.0, 6.0) == F_LO


def test_midpoint_is_geometric_mean():
    mid = magnitude_to_frequency(0.0, -6.0, 6.0)
    assert mid == pytest.approx(math.sqrt(F_LO * F_HI), rel=1e-12)


def test_equal_magnitude_steps_are_equal_intervals():
    mags = np.arange(-6.0, 7.0)
    f = magnitude_to_frequency(mags, -6.0, 6.0)
    ratios = f[:-1] / f[1:]
    assert np.allclose(ratios, ratios[0], rtol=1e-12)
    # 12 magnitudes over 3 octaves: 3 semitones per magnitude
    assert ratios[0] == pytest.approx(2 ** (3 / 12), rel=1e-12)


def test_brighter_reads_higher():
    mags = np.linspace(-6.0, 6.0, 100)
    f = magnitude_to_frequency(mags, -6.0, 6.0)
    assert np.all(np.diff(f) < 0)


def test_degenerate_span_constant_tone():
    f = magnitude_to_frequency(np.array([2.0, 2.0]), 2.0, 2.0)
    assert np.all(np.isfinite(f))
    assert np.allclose(f, math.sqrt(F_LO * F_HI))
    pcm = render_brightness_decline(10.0, 2.0, 2.0, 1.0)
    assert np.all(np.isfinite(pcm.astype(np.float64)))


def test_wav_format_round_trip(tmp_path):
    path = tmp_path / "out.wav"
    render_brightness_decline(642.0, -6.0, 6.0, 22.0, out_path=path)
    rate, data = wavfile.read(path)
    assert rate == 44_100
    assert data.dtype == np.int16
    assert data.ndim == 1  # mono
    assert len(data) == round(22.0 * 44_100)


def test_no_clipping_and_faded_ends():
    pcm = render_brightness_decline(642.0, -6.0, 6.0, 22.0)
    assert np.max(np.abs(pcm.astype(np.int32))) <= round(AMPLITUDE * 32767)
    assert pcm[0] == 0
    assert pcm[-1] == 0


def test_phase_continuity_no_clicks():
    pcm = render_brightness_decline(642.0, -6.0, 6.0, 22.0).astype(np.int32)
    # |d/dt sin(phase)| <= 2*pi*f_hi/sr per sample; fades only reduce it.
    bound = AMPLITUDE * 32767 * (2 * math.pi * F_HI / 44_100) * 1.1
    assert np.max(np.abs(np.diff(pcm))) <= bound


@pytest.mark.parametrize(
    "kwargs",
    [
        {"duration_days": 0.0},
        {"duration_days": -1.0},
        {"compression_seconds": 0.0},
        {"compression_seconds": -5.0},
        {"f_lo": 880.0, "f_hi": 220.0},
        {"amplitude": 0.0},
        {"amplitude": 1.5},
    ],
)
def test_validation(kwargs):
    base = dict(
        duration_days=642.0,
        start_magnitude=-6.0,
        end_magnitude=6.0,
        compression_seconds=22.0,
    )
    with pytest.raises(ValueError):
        render_brightness_decline(**{**base, **kwargs})


def test_write_to_filelike_buffer_matches_return():
    buf = io.BytesIO()
    pcm = render_brightness_decline(642.0, -6.0, 6.0, 22.0)
    wavfile.write(buf, 44_100, pcm)
    rate, data = wavfile.read(io.BytesIO(buf.getvalue()))
    assert np.array_equal(data, pcm)
