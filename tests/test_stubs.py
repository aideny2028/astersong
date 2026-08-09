"""The unimplemented surface must say so loudly, and versions must agree."""

import pathlib
import re

import pytest

import astersong


def test_time_to_tempo_is_stub():
    with pytest.raises(NotImplementedError):
        astersong.TimeToTempo(seconds=22)


def test_position_to_stereo_is_stub():
    with pytest.raises(NotImplementedError):
        astersong.PositionToStereo(coords=None)


def test_from_record_is_stub():
    with pytest.raises(NotImplementedError):
        astersong.from_record("XJ-1054")


def test_version_matches_pyproject():
    pyproject = pathlib.Path(__file__).resolve().parents[1] / "pyproject.toml"
    m = re.search(r'^version = "([^"]+)"', pyproject.read_text(), re.M)
    assert m and m.group(1) == astersong.__version__
