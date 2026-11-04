**Serves:** research PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-41

# Split brief — PLAY-dConvergedCharter-11 into the fold and PLAY-dConvergedCharter-41, the re-points

The owner ruled on 2026-11-04 (`memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions.md`)
that PLAY-dConvergedCharter-11, at about 67.5 KB against the 49152-byte spec ceiling, splits in two along the seam
"fold vs re-points". You author that split. It is a spec change after the spec run landed (`923954b61`): every unit is
DEFERRED and no code has started, so the split is a design change of specs only. Read the spec brief
`memory/builds/dConvergedCharter/prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md` ("Every spec, whatever
its unit" and "What the last spec runs had to fix") before the first edit; its rules bind both specs.

## The seam

- **PLAY-dConvergedCharter-11 keeps the fold itself:** S1 (the catalogue rows), S2 (gov's values moved), S3 (the
  both-homes reader `policy.py legacy`), S5 (the red arm `arm_folded_homes`), S6 (`derive_readers`, shared interface I1),
  S7 (the policy README sentence) and S9 (the census re-point), with the acceptance criteria, §4 design text, §8 forks
  and §10 reuse rows that serve them.
- **PLAY-dConvergedCharter-41 takes the re-points:** S4 (the named readers re-pointed: the four `read_policy_key`
  copies in `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh` and
  `tools/unattended/unattended.sh` with their callers, comments and parity tests, `tools/run-gates/held_halves.py`,
  `transition_audit.read_modes`, govkit's conf-key gap checks, kit.toml's `*_keys` and the kit-placeholders leg) and S8
  (the house-file arm `arm_house_readers` and `roles_lib.load_policy`'s house-file fallback), with the acceptance
  criteria, §4 design text, §8 forks and §10 rows that serve them, the scratch-clone `--decide` proof
  (`INHERITED_RED=park` folded, `land` before the re-point and `park` after it) among them.

Where an AC, a design paragraph or a fork serves both halves, keep it in the unit whose S-item it observes and have the
other cite it by id and label; never copy it. Move text; do not rewrite what it decides.

## What each spec carries

- Both carry `cl-dClosedLoop-0485@43490b62` in parts: unit 11 `**Carries:** cl-dClosedLoop-0485@43490b62 part 1/2`,
  unit 41 `**Carries:** cl-dClosedLoop-0485@43490b62 part 2/2`. Every token of the clause (the packet's Items 11)
  appears in backticks in whichever part carries what it names; the carries join needs each token in at least one
  carrier, and none may be lost.
- Unit 41's spec: `memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md`, H1
  `# PLAY-dConvergedCharter-41 — <title>` (an EM DASH), status header
  `**Status:** DEFERRED · rev-1 · 2026-11-04 · node d · Tier-2 · base 923954b6 · streams playbook · order 3 · advances PLAY-dConvergedCharter-24`.
  Order 3 puts it after unit 11 (order 2) and before unit 12 (order 4), which deletes the kit holding one of the four
  copies.
- Unit 11: bump to `rev-5` (status stays DEFERRED, base unchanged) with one revision-log line naming the owner's ruling
  record above and what moved to unit 41. Its §9 history stays as it is.
- Deviation `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111.md` departs
  from the clause on the house-file readers, which move to unit 41: write
  `memory/builds/dConvergedCharter/build/2026-11-04-build-PLAY-dConvergedCharter-41-deviation-412.md` carrying the same
  departure for unit 41 (same grammar, `**Follow-through:** amends cl-dClosedLoop-0485@dde21704`, Serves and Caused-by
  naming unit 41), and leave deviation 111 unedited (a recorded departure is append-only); say in unit 41's §8 that
  411's number is reserved for the main loop's design-to-spec record of the new unit.

## Edges and siblings

- Every §3 edge of unit 11 that concerns what moves goes to unit 41, and the sibling declaring its reverse re-points it:
  the house-file arm's hands-off to PLAY-dConvergedCharter-21 (`arm_house_readers`), the external consumes-from
  TOOL-dBoundRoles-21, and anything naming the four copies or `held_halves.py`.
- New pair: unit 11 `hands-off` unit 41, naming the tokens 41 reads from 11 (at least `policy.py legacy` / the folded
  key names, and `derive_readers` if 41's red arm uses it); unit 41 `consumes-from` unit 11 back.
- New pair: unit 41 `hands-off` PLAY-dConvergedCharter-12, naming the `read_policy_key` copy in
  `tools/unattended/unattended.sh` that 41 re-points before 12 removes the kit; unit 12 `consumes-from` 41 back.
- Every other spec of this build that cites unit 11's S4 or S8 by id and label (`git grep -n 'PLAY-dConvergedCharter-11'`
  over `memory/builds/dConvergedCharter/spec/`, skipping generated record regions) re-points the citation to unit 41's
  new label. A sibling spec you edit takes a rev bump and a revision-log line naming the owner's ruling record and the
  split, as a sibling edit.

## Checks before you return

- Unit 11 and unit 41 each under 49152 bytes (`wc -c`); say each size.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0 with no red on this build's specs.
- No acceptance criterion names the bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run; a suite is a
  `New arm:` line.
- A path a criterion names that does not exist at HEAD is cited by basename there and kept whole in §2, §4 and Files
  touched.

Write nothing outside `memory/builds/dConvergedCharter/spec/` and `memory/builds/dConvergedCharter/build/`. Return:
both sizes, unit 41's S-items and ACs by label, every sibling spec you edited with its new rev, each edge pair you
added or moved, and the hygiene exit.
