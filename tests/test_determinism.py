"""Determinism: the tests that matter most. Same inputs, same bytes."""

import hashlib
import io

import numpy as np
import pytest
from scipy.io import wavfile

from astersong import render_brightness_decline

SN1054 = dict(
    duration_days=642.0,
    start_magnitude=-6.0,
    end_magnitude=6.0,
    compression_seconds=22.0,
)

# SHA-256 of the canonical SN 1054 WAV, recorded on the reference platform
# (macOS arm64, CPython 3.x, NumPy 2.x). IEEE-754 basic ops are exactly
# rounded everywhere, but sin/exp2 go through the platform libm, so a
# different platform or NumPy build may legitimately differ. To refresh
# after a *deliberate* mapping change: run examples/render_sn1054.py and
# paste the printed digest here, noting the change in CHANGELOG.md.
GOLDEN_SHA256 = "e1f63084e821c7341506761559c3e70821958a8298727f97f0f668b3ffcf81a1"


def wav_bytes(**kwargs):
    buf = io.BytesIO()
    pcm = render_brightness_decline(**{**SN1054, **kwargs}, out_path=None)
    wavfile.write(buf, 44_100, pcm)
    return buf.getvalue()


def test_byte_identity_files(tmp_path):
    a, b = tmp_path / "a.wav", tmp_path / "b.wav"
    render_brightness_decline(**SN1054, out_path=a)
    render_brightness_decline(**SN1054, out_path=b)
    assert a.read_bytes() == b.read_bytes()


def test_byte_identity_in_memory():
    assert wav_bytes() == wav_bytes()


def test_array_identity():
    x = render_brightness_decline(**SN1054)
    y = render_brightness_decline(**SN1054)
    assert x.dtype == np.int16
    assert np.array_equal(x, y)


def test_golden_checksum():
    digest = hashlib.sha256(wav_bytes()).hexdigest()
    assert digest == GOLDEN_SHA256


@pytest.mark.parametrize(
    "change",
    [
        {"compression_seconds": 21.0},
        {"f_lo": 110.0},
        {"f_hi": 880.0},
        {"amplitude": 0.5},
        {"fade_seconds": 0.2},
    ],
)
def test_sound_shaping_parameters_matter(change):
    assert wav_bytes() != wav_bytes(**change)


def test_linear_decline_is_span_normalized():
    # The documented rule fixes the endpoints: the dimmest sample maps to
    # f_lo and the brightest to f_hi. For a strictly linear decline the
    # magnitude endpoints therefore set the documented scale (semitones per
    # magnitude), not the waveform, which is always the full f_hi -> f_lo
    # glide. This test locks that documented behavior in place.
    assert wav_bytes() == wav_bytes(start_magnitude=-5.9)
    assert wav_bytes() == wav_bytes(end_magnitude=5.9)
