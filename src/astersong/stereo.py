"""Position-to-stereo mapping. TODO: not yet implemented.

Design (docs-mockup, Mapping page, rule 3 "Position to stereo"): where the
object stood in the sky sets the stereo image; ``mode="azimuth"`` pans by
horizontal angle, ``mode="hemisphere"`` carries declination, and a moving
object's pan follows the recorded motion. Positions will be placed through
Astropy in the coordinate frame of the record's own date, with precession
applied (Astropy is a future dependency of this module only; it is not
imported by the package today).
"""

from __future__ import annotations


class PositionToStereo:
    """TODO stub: see the design notes in this module's docstring."""

    def __init__(self, coords=None, mode="azimuth", width=0.9):
        raise NotImplementedError(
            "PositionToStereo is not implemented yet; see docs-mockup mapping "
            "rule 3 for the design it will follow."
        )
