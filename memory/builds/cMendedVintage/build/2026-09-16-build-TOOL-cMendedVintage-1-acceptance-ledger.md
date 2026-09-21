# cMendedVintage — the acceptance ledger for unit 1

**Serves:** journal TOOL-cMendedVintage-1

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commit, `8a8529b1`, 2026-09-16. FOUR of the six criteria
are answered by what the building pass measured, and the commit is cited AS that record and named as
such each time; TWO are answered by commands replayed at the shell against this worktree at this
tip, with their output given. No merge bar, no `*.test.sh` and no self-test runner ran in this pass,
and no scratch tree was built here.*

## The one thing worth reading twice

**The building pass named four criteria and was silent on two.** Commit `8a8529b1` states that "the
live script passes all of AC1, AC2, AC3 and AC6" and says nothing at all about AC4 or AC5 — the two
that are answered by a gate rather than by the adopter. Those two were replayed here instead of
being assumed from the commit's green tone, and both hold. The distinction is kept per criterion
below rather than flattened, because who observed a thing is half of what a ledger is for.

**Both failing cases were staged before the code existed, and the commit records which was which.** A
copy of the script with the mode test removed replaced an adopted tree's `HYGIENE.md` with the
one-line stub, which is AC6's red; a copy with the marker check removed rendered into an unmarked
tree, which is AC3's red. That is the whole risk this unit was written against.

**The pass's own declared write set was wrong, and nothing refused it.** `RUN.md` records the
decision at 2026-09-16T19:48:13Z: this unit declared two paths at dispatch and committed seventeen,
the version bump rippling to four templates, a README and `check-memory-hygiene.sh`, plus a
pre-commit manifest re-stamp. The builder reported it; no verb, hook or gate raised it. It is the
same pass's self-report that answers four criteria here, which is why it is written down.

**Evidences:** TOOL-cMendedVintage-1

- AC1 — `bash tools/memory-tree/adopt-memory-tree.sh --render` — two halves, two records. The
  `--render` half is the building pass's: commit `8a8529b1` reports it green against a scratch
  adopted tree under that run's scratch root, the fixture AC1 names, a copy of this repo's own
  `memory/` tree rather than a construction. It was NOT replayed here — running that mode against
  this worktree would rewrite the four rendered rows, and this pass writes ledgers and nothing else.
  The usage half WAS replayed here, at this tip: an unknown mode word exits 2 printing
  `usage: tools/memory-tree/adopt-memory-tree.sh --scaffold|--render`, and `git status --porcelain`
  is unchanged afterwards, so the word is refused at the parse with nothing downstream reached.
- AC2 — `--render` — the building pass's record, and its fixture detail is what shows the run was
  made rather than described. Spec rev-3 divergence 3 reports that AC2's fixture truncates the
  SECOND rendered row and not the first, because truncating the first removes the adoption marker
  and S3's guard then refuses — which is AC3's case, not AC2's. That is a measurement, taken at
  build time, that changed the criterion. The render set the criterion calls DERIVED was re-read
  here at this tip and is still four on both sides: `tools/memory-tree/kit.toml` declares four
  `role = "rendered"` rows, and `render_all` in the adopter holds exactly four template-to-
  destination pairs, which is the single set S2 exists to keep the two modes from splitting.
- AC3 — `gov:kit memory-tree@` — the building pass's record, red first: commit `8a8529b1` reports
  that a copy with the marker check removed rendered into an unmarked tree, then that the live
  script passes. The branch was read here at this tip and matches what the criterion asks of it —
  under `--render`, a memory root whose `HYGIENE.md` is absent or carries no marker exits 1 with a
  message naming `--scaffold`, and it returns before `render_all`, so nothing is written. Reading a
  branch is not running it; the RUN is the commit's, not this pass's.
- AC4 — `python tools/govkit/govkit.py selfcheck` — replayed at this tip: exit 0. Its notes read
  `rendered rows: 6 descriptor(s) ship at least one, 6 of those declare [[regenerate]]` and
  `re-render claims: 15 sentence(s) … across 6 kit(s) declaring [[regenerate]]`, the elision
  standing for the note's own flag-off clause. NEITHER NOTE NAMES A KIT, so the criterion's
  wording is answered by a count plus one derivation, stated rather than glossed: reading the
  registry through `read_descriptors` at this tip, `memory-tree` ships four `role = "rendered"` rows
  — the most of the six — and declares one `[[regenerate]]` whose argv is
  `["bash", "{kit}/adopt-memory-tree.sh", "--render"]`. Six of six therefore includes it, and had it
  not, `DEPL-cMendedVintage-8`'s join would exit 1 naming it, which commit `8295fb18` records it
  doing at base `859daa67` against `memory-tree with 4 rendered rows`. The building pass recorded no
  run of selfcheck at all.
- AC5 — `bash tools/check-kit-versions.sh` — replayed at this tip: exit 0 with no output, which is
  this gate's green. Both halves the criterion asks for are in it and were read: a presence-and-
  format assertion for `KIT_MEMORY_TREE_VERSION` against `tools/memory-tree/check-memory-hygiene.sh`,
  and a pair assertion comparing that constant to the `gov:kit memory-tree@` marker in EVERY tracked
  `tools/memory-tree/*.template.md`, which refuses outright if that population comes back empty. The
  constant and the four template markers moved 2.78 to 2.79 in commit `8a8529b1`. The building pass
  recorded no run of this gate either.
- AC6 — `HYGIENE.template.md` — the building pass's record, red first and the red is the point:
  commit `8a8529b1` reports that a copy with the mode test removed replaced the tree's `HYGIENE.md`
  with the stub, then that the live script passes. The refusal was read here at this tip and is
  wider than the criterion's own wording: under `--render`, `render_all` walks all four templates
  first, names every missing one, and returns 1 BEFORE the first write, so a partial set is never
  left on disk. Spec rev-3 divergence 2 records that widening — from `HYGIENE.template.md` alone to
  all four — as a build-time decision, and it is what makes "writes nothing" true of the whole set
  rather than of the first destination.

## What this ledger does NOT claim

That the merge bar is green. §7 names five legs. Two of them — `govkit selfcheck` and
`kit version markers` — ran here and exit 0, and they are exactly the two that answer AC4 and AC5.
`memory hygiene`, `kit/dogfood doc parity` and `kit placeholders (a declared token its adopter
substitutes)` did not run in either pass and are unobserved for this unit. That last one matters
more than usual here: this unit added a rendered-mode branch to a kit whose whole job is substituting
placeholders into an adopter's documents.

That anything ran `--render` in THIS pass. AC1's first half, AC2, AC3 and AC6 are all reports of the
building pass's scratch tree, cited as such. No scratch adopted tree was built here, and this
worktree's own four rendered documents were not re-rendered, compared or touched.

That an adopter took the mode. Nothing in this repo installs it — the spec's third edge says an
adopter picks it up on their next routine pull — and the declared argv stayed unreachable by
`update` until `DEPL-cMendedVintage-7` flipped `GOVKIT_RERENDER` on two units later. Until then it
was reachable by hand only, which is how every observation above that ran it was made.
