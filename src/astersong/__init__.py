"""AsterSong: deterministic sonification of real astronomical data.

Fixed, documented, deterministic mappings; no randomness, no learned
parameters, no generative audio. One mapping is implemented today
(brightness-decline-to-pitch); the rest of the documented surface exists as
stubs that raise NotImplementedError.
"""

from .brightness import (
    AMPLITUDE,
    F_HI,
    F_LO,
    FADE_SECONDS,
    SAMPLE_RATE,
    magnitude_to_frequency,
    render_brightness_decline,
)
from .records import from_record
from .stereo import PositionToStereo
from .tempo import TimeToTempo

__version__ = "0.1.0"

__all__ = [
    "AMPLITUDE",
    "F_HI",
    "F_LO",
    "FADE_SECONDS",
    "SAMPLE_RATE",
    "PositionToStereo",
    "TimeToTempo",
    "from_record",
    "magnitude_to_frequency",
    "render_brightness_decline",
    "__version__",
]
