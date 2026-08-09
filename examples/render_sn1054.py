"""SN 1054, the Tianguan guest star: its naked-eye decline as a 22-second
pitch fall.

Documented constants and their sources:

- 642 days: night visibility of the guest star, first daylight sighting
  4 July 1054 (Julian) to last recorded sighting 6 April 1056, per the
  Xuanji archive record XJ-1054 (Song shi, Treatise on Astronomy).
- -6.0: approximate peak apparent magnitude; bright enough to be logged in
  full daylight for about 23 days (XJ-1054, reconstructed sky).
- +6.0: the conventional naked-eye limiting magnitude, taken as the
  brightness at which the record says the star "finally vanished".
- 22 seconds: the project's compression convention for this record
  (docs-mockup tutorial, example 3: roughly two years to 22 s).

Every sample of the output is a pure function of these inputs: rendering
twice produces byte-identical files, and the printed SHA-256 is the receipt.
"""

import hashlib

from astersong import render_brightness_decline

SN1054_DURATION_DAYS = 642.0
SN1054_PEAK_MAG = -6.0
SN1054_END_MAG = 6.0
CLIP_SECONDS = 22.0

OUT = "sn1054.wav"


def main():
    render_brightness_decline(
        SN1054_DURATION_DAYS,
        SN1054_PEAK_MAG,
        SN1054_END_MAG,
        CLIP_SECONDS,
        out_path=OUT,
    )
    factor = SN1054_DURATION_DAYS * 86400.0 / CLIP_SECONDS
    with open(OUT, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"wrote {OUT}: 22 s, three-octave descent (1760 Hz -> 220 Hz),")
    print(f"compression factor {factor:.3g} (642 days -> 22 s)")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
