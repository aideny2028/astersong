# AsterSong

AsterSong is a Python toolkit that converts real astronomical data into sound
through fixed, documented, deterministic mappings: no randomness, no learned
parameters, no generative audio. It embodies a thesis: technology should
interpret real data and human meaning, never manufacture content. Its inputs,
over time: light curves (the astronify and lightkurve ecosystems), events from
the Xuanji guest-star dataset, and eventually spectra from the radio telescope
Aiden works on.

**Status: one mapping implemented; gallery and further mappings planned.**
The `docs-mockup/` folder is an internal design mockup of the target
documentation site (written under the project's earlier working name) and is
not deployed; see its README.

## Install and run

```
python -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest
.venv/bin/python examples/render_sn1054.py
```

Python 3.10+; dependencies are numpy and scipy only.

## The brightness-decline-to-pitch mapping, end to end

The one mapping implemented today renders a linear brightness decline as a
pitch glide:

```python
from astersong import render_brightness_decline

pcm = render_brightness_decline(
    duration_days=642.0,       # real span of the decline
    start_magnitude=-6.0,      # brighter = numerically smaller
    end_magnitude=6.0,
    compression_seconds=22.0,  # playback length
    out_path="sn1054.wav",
)
```

**The formula.**

```
f(m) = f_hi * (f_lo / f_hi) ** ((m - m_bright) / (m_dim - m_bright))
```

**The reasoning.** Apparent magnitude is already a logarithm of flux (the
Pogson scale), and pitch perception is a logarithm of frequency, so a mapping
linear in magnitude and logarithmic in frequency makes equal magnitude steps
equal musical intervals. Magnitudes are inverted: smaller is brighter, and
brighter reads higher. The endpoints are exact: the brightest sample maps to
`f_hi`, the dimmest to `f_lo`. With the defaults (220 Hz to 1760 Hz, three
octaves) a 12-magnitude decline moves exactly 3 semitones per magnitude.
Record time is carried to playback time by one linear factor
(`duration_days * 86400 / compression_seconds`). One honest consequence of
the endpoint rule, stated rather than hidden: for a strictly linear decline
the rendered waveform is always the full `f_hi` to `f_lo` glide, so
`duration_days` and the magnitude endpoints set the documented compression
factor and the semitones-per-magnitude scale, not the sound itself; they
start mattering audibly with real, non-linear light curves, which is what
the signature is ready for. The test suite locks this behavior in place.

**Parameters.**

| parameter | default | meaning |
|---|---|---|
| `duration_days` | required | real span of the decline; defines the compression factor |
| `start_magnitude` | required | apparent magnitude at the start |
| `end_magnitude` | required | apparent magnitude at the end |
| `compression_seconds` | required | playback length |
| `out_path` | `None` | write a mono 16-bit PCM WAV here if given |
| `f_lo`, `f_hi` | 220.0, 1760.0 | pitch range, dimmest to brightest |
| `sample_rate` | 44100 | output sample rate |
| `amplitude` | 0.8 | constant; loudness carries no data |
| `fade_seconds` | 0.05 | raised-cosine fade at each end (click suppression) |

**Synthesis.** The tone is phase-continuous: the instantaneous frequency is
integrated (a cumulative sum) rather than evaluated as `sin(2*pi*f(t)*t)`,
which would click. Raised-cosine fades remove the start and end
discontinuities. Amplitude is constant by policy: loudness and timbre carry
no data.

**Determinism.** Every output sample is a pure function of the arguments:
no randomness, no clock, no environment reads, no learned parameters; all
arithmetic is float64 elementwise work (no BLAS, no FFT). The test suite
asserts byte-identical output for identical inputs and holds the canonical
SN 1054 render to a golden SHA-256, so the mapping cannot change silently.
The honest scope: transcendental functions follow the platform's libm, so
byte-identity is guaranteed per platform and NumPy build, and checked, not
promised, across them.

## The worked example: SN 1054

`examples/render_sn1054.py` renders the founding record of the Xuanji
dataset: the guest star of 4 July 1054 (the Crab supernova), visible to the
naked eye for 642 days (to 6 April 1056), from roughly magnitude -6 at peak
(bright enough to be logged in daylight) down to the naked-eye limit near +6,
compressed to 22 seconds: a three-octave descent from 1760 Hz to 220 Hz. The
constants and their sources are documented in the script.

## Not yet implemented

`TimeToTempo`, `PositionToStereo`, and the Xuanji `from_record` interface are
stubs that raise `NotImplementedError`; their docstrings point at the design
pages in `docs-mockup/` they will follow. No gallery audio exists yet and
none is claimed.

## License

BSD-3-Clause. Author: Aiden Yeoh.
