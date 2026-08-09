"""Time-to-tempo mapping. TODO: not yet implemented.

Design (docs-mockup, Mapping page, rule 2 "Time to tempo"): record-time is
compressed to playback-time by one linear factor; the caller sets either the
total clip length (``seconds``) or, for periodic data, how many cycles to play
(``cycles``); gaps between observations are preserved exactly, never
interpolated across; ``gap="mark"`` adds a faint tick at each gap edge.

The linear-factor convention is already honoured by
:func:`astersong.brightness.render_brightness_decline`; this class will carry
it for arbitrary (times, values) series.
"""

from __future__ import annotations


class TimeToTempo:
    """TODO stub: see the design notes in this module's docstring."""

    def __init__(self, seconds=None, cycles=None, gap="preserve"):
        raise NotImplementedError(
            "TimeToTempo is not implemented yet; see docs-mockup mapping "
            "rule 2 for the design it will follow."
        )
