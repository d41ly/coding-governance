# TOOL-dDerivedDocket-18 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-18

The unattended gate leg's second opinions over the ask mandate: `asks:` against the README at BASE
and at HEAD, P5 and `m-base:` re-derived, the folder-wide anchor ban as check 37, the freeze's
presence, the one authorization path, and the pinned grades and freeze re-derived by re-running the
declared producer before publication. No merge bar, no gate leg and no `*.test.sh` suite ran in this
pass. What ran instead, all from a scratch root outside the tree with each call's working directory
inside its own fixture repository:

- the leg itself over a hand-built fixture repository carrying one mandated record, a stub producer
  that reads its grade table AT THE REV it is asked about, and the recall kit's real extractor —
  fifty-two assertions, green;
- twenty-four staged breaks of the leg, each a copy with one arm disarmed or bent the way its
  criterion's `Red when:` says, each run against only the arms it targets — all twenty-four RED, each
  on the assertion it targets;
- the suite block this unit adds, sliced out of `tools/unattended/check-unattended.test.sh` by its
  own markers and executed standalone in a replica of that suite's prologue — sixty assertions,
  green, which is the count both suite floors carry — and RED under five further staged breaks,
  each on only the arm it targets: the introducing-commit resolver narrowed to the archived path
  (the rotated mandated record, which is where `TOOL-dDerivedDocket-52`'s AC1 and AC3 left their
  check-19 half), the ancestry fallback unable to fail, the unreadable-`m-base:` refusal silenced,
  the publication guard removed, and the foreign-slug test disarmed.

One harness trap, recorded because it cost a round: the first parallel run of those five breaks red
thirty arms each, and the cause was the scratch path, not the leg. Its long directory names pushed
the fixture's bare remote past git's length limit, the push failed with `'$GIT_DIR' too big`, and
both pins were written EMPTY. The block now takes its merge-base from the local `main` and asserts
the fixture pinned a 40-hex `m-base:` and that the remote holds the anchor before any arm runs.

AC9 and AC10 carry `permission:` lines and get no line here; the orchestrator writes them after the
post-build bar. AC9 was AMENDED at rev-6 (its line is on the report channel under
`GOV_UNATTENDED_REPORT=1`), and its pass-direct check, the leg over a scratch fixture holding no
mandated record, printed the vacuity line with the count 0.

**Evidences:** TOOL-dDerivedDocket-18
- AC1 — `asks:` — a record whose pinned fact carries one id more than the README line at its recorded
  BASE reds check 19 naming the pinned value, both ids, against the declared one, one id. Staged
  RED: with the BASE comparison disarmed the arm misses it.
- AC2 — `asks:` — a README edited at HEAD reds a RUNNING record; the same committed edit under a
  LANDING record and under a LANDED one does not, and the LANDING run prints that the record is past
  its close. Staged RED two ways: the HEAD comparison disarmed, so the live record passes, and the
  phase guard removed, so both closed records red.
- AC3 — `m-base:` — with the ask row dropped from the home `BACKLOG.md` on the anchor and every pin
  re-recorded against it, check 19 reds naming `EXMP-aFoo-3` and `memory/builds/aFoo/BACKLOG.md` at
  the recorded tree, while the equality arm stays green. Staged RED: with the filing test disarmed.
- AC4 — `m-base:` — `base:` and `m-base:` forged together to an older ancestor of `anchor-sha:`,
  committed, red check 19 naming the forged and the re-derived value; the same `m-base:` left
  uncommitted, so no commit introduced it, prints that the arm FELL BACK TO ANCESTRY. Staged RED
  three ways: the equality disarmed, the merge-base taken from `base:` instead of `anchor-sha:`, and
  the fallback's announcement removed.
- AC5 — `anchor_at` — a table row whose first cell is a backticked foreign id reds check 37 naming
  the fixture file, its line 3 and the id; a link-wrapped first cell in the same file does not.
  Staged RED: with the foreign-slug test disarmed inside the extractor call the arm misses it.
- AC6 — `RECALL_CLI` — blank in the fixture conf, the leg prints `check 37 SKIPPED` naming the key and
  does not red on the same foreign row. Staged RED: with a blank key answered as zero anchors found.
- AC7 — `asks-at-landing:` — a LANDED mandated record with no freeze reds check 15; with the freeze
  present it does not. Staged RED: with the absence refusal disarmed.
- AC8 — `SECOND_ANCHOR_MODES` — one fixture per member, read from the driver's constant, each reds
  check 19; a `slug` record under a blank `ASKS_CMD` reds on the conf half alone. Staged RED three
  ways: the mode refusal disarmed, the refusal keyed on `prompt` alone (the `recipe` arm misses), and
  the conf refusal disarmed.
- AC11 — `asks-ready:` — on an unpublished record, `EXMP-aFoo-3=no` against the stub's `yes` at the
  pinned tree reds check 19 naming both pairs; pushed to the advertised tip it is counted as
  `published, not re-derived`; a stub sleeping past a 2 s bound is reported UNANSWERED and does not
  red; a remote advertising no default tip re-derives and prints why; an uncommitted `m-base:`
  skips the re-derivation by name; and a grade table that moves AFTER the pin does not red. Staged
  RED six ways, including the producer re-run at HEAD and the publication guard removed.
- AC12 — `asks-at-landing:` — `EXMP-aFoo-3=CLOSED` against the stub's `OPEN` at the first parent of
  the commit that introduced the freeze reds check 15 naming both; a REOPEN committed after the
  freeze reds neither a published record nor an unpublished one whose landing tree said CLOSED.
  Staged RED: the comparison disarmed, and the freeze re-derived at HEAD.
- AC13 — `asks-at-landing:` — a freeze omitting one id of a two-id mandate reds check 15 naming
  `EXMP-aFoo-4`. Staged RED: with the per-id test disarmed, so presence alone passes.
