# joss-submission.md

The Journal of Open Source Software (JOSS) is a real, free, peer-reviewed venue
for research software. It reviews the **software**, openly, on GitHub. The goal
site shows a finished JOSS paper; this file is how you actually earn one. Do not
submit early.

## Submit only when all of this is true
- [ ] The package is on PyPI and installs cleanly for someone who is not you.
- [ ] A tagged release is archived with a real Zenodo (or equivalent) DOI.
- [ ] There is a real, meaningful test suite and CI that runs it.
- [ ] The docs teach a new user to get a first result (the launch tutorial does
      this).
- [ ] The software does enough to be worth citing. JOSS expects "substantial
      scholarly effort," not a weekend script. This usually means v0.4 or later,
      after real contributors and real use.

## The paper itself
- `paper.md` is short (about 250 to 1000 words): a summary, a statement of need,
  and how it compares to prior tools (Astronify is the closest sibling; cite it).
- `paper.bib` holds your references.
- Both live in the repo. The review happens as a GitHub issue against your repo.

## Authorship, the honest rule
- Authors are everyone who made a **substantial** contribution to the software or
  paper, and no one who did not.
- The goal site's six-author citation is a **demonstration placeholder** (see
  `../provenance.md`); those co-authors are fictional. Your real paper lists the
  real people who did the work. On day one that may be you alone, and that is a
  perfectly good JOSS paper.
- An advisor who reviewed cross-IDs may be acknowledged, or a co-author if they
  contributed substantially and agree. Ask; do not assume.

## Until then
The launch site correctly says "JOSS paper in preparation." Keep it that way
until the submission is real and accepted. Do not print a DOI, a volume, or an
article number that does not resolve.
