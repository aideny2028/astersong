"""Interface to the Xuanji guest-star dataset. TODO: not yet implemented.

Design (docs-mockup, Tutorial example 3): ``from_record("XJ-1054")`` will load
a record from the Xuanji archive's per-record JSON (``records/<id>.json``,
schema per the archive's ``docs/schema.md``) and expose ``.source``,
``.cross_id``, ``.confidence``, ``.coords``, and ``.light_curve()`` so a
sonification can carry the record's own uncertainty into the audio.
"""

from __future__ import annotations


def from_record(record_id):
    """TODO stub: see the design notes in this module's docstring."""
    raise NotImplementedError(
        "from_record is not implemented yet; see the docs-mockup tutorial "
        "(example 3) for the interface it will follow."
    )
