# TOOL-dRetiredFork-8 — acceptance ledger

**Serves:** journal TOOL-dRetiredFork-8

**Evidences:** TOOL-dRetiredFork-8
- AC1 — `bash tools/check-wiring.sh --check` — in-tree settings resolve and the arm results are byte-identical to the pre-change run, diffed against it; the ok lines print the RELATIVE path, which is what keeps them identical
- AC2 — `bash tools/check-wiring.sh --check` — with `GOV_SETTINGS_JSON` outside the repo, the run REPORTS `OUTSIDE the repo root`, still grades the wiring and exits 0; the pre-change command with the file absent printed 4 ok lines
- AC3 — `bash tools/check-wiring.test.sh` — no settings file resolves: the run names the failed resolution, exits non-zero, and an ADOPTED kit reports UNWIRED rather than passing by absence. Not a whole-run exit 2 — see the correction below
- AC4 — `bash tools/check-wiring.sh --session` — exits 0 and left `core.hooksPath` at its already-set value, verified before and after
- AC5 — `grep -c '.claude/settings.json' tools/check-wiring.sh` — returns 1, the resolver's preference rung. Byte-identity cannot catch a residual literal here because gov's own file sits where the literal pointed
- AC6 — `bash tools/check-install-prefix.sh` — carried count for this file fell 6 to 1, the ratchet was re-baselined in this commit, and the waiver registry shrank 12 to 11
- AC7 — `bash tools/check-kit-versions.sh` — exits 0 after 1.1 to 1.2

## Three of my own cuts were measured wrong before they landed

**The eager resolution killed 45 of 76 arms.** Calling the resolver at startup and exiting 2 on
failure broke every fixture without a settings file — and not one of those arms was about settings.
A repo with no `.claude/settings.json` is a legal state, and refusing there says nothing about the
hooks, skills and eol wiring the run was asked to grade. The refusal belongs to the arms that NEED
the file.

**Collapsing S6 to one derived rung broke six more.** `KIT_REL` is derived from where the SCRIPT
lives, not from the tree it grades, and those differ exactly when it matters — which is what the
self-test reproduces by running the real checker against root-install fixtures. The dual-spelling
probe is load-bearing; only the prefixed rung is derived.

**The tolerant wrapper discarded the resolver's stderr.** "You named a path that is not there" and
"there is no settings file anywhere" are different operator problems with different fixes, and they
printed the same sentence until the resolver's own words were surfaced.

All three were found by running the suite, not by reading it. The baseline had to be measured in
place first: running the original suite from a scratch directory reported 46 failures that were
entirely an artefact of `$HERE` resolving to the wrong directory.
