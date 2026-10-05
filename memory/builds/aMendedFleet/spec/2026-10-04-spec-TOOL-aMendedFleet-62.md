# TOOL-aMendedFleet-62 — the two history legs grade the run's own range, reusing node d's bytes

**Status:** CLOSED · rev-4 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 61

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-62-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-62-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`pass-order history` and `brief-recorded` walk every build's whole history on every bar, so a
violation landed by anybody at any time reds every later closing run, and the two legs set a floor
under the bar's wall clock. Node d's `dUnstuckLanding` already built RANGE mode for them, in commits
`d99cd0328` and `f8afa61bc`: each leg asks the remote which tip it advertises and grades only the
commits HEAD carries past it, and falls back to today's whole walk, announced, when it cannot.
The owner ruled that this build builds every report item even where node d has, and that such a
unit REUSES node d's bytes so the later reconcile meets identical hunks. This unit applies the
history-leg half of those commits to this tree byte for byte, plus the two helper renames node d
made afterwards in `83eec3021` so its own lexicon leg stayed green.

## 2. Scope (IN)

- **S1** — THE READER. `read_advertised_head` and `read_history_range` in
  `tools/unattended/lib-unattended.sh`, as node d wrote them, including `f8afa61bc`'s refusal of a
  zero bound. The first runs one bounded `ls-remote --symref --exit-code <remote> HEAD`, with its
  three bounds read from the driver's text as data, and never reads a local ref or an environment
  variable; the second sets `HR_MODE`, `HR_EXCL` and `HR_FIELD` for both legs. Observed by AC1.
- **S2** — `pass-order history` IN RANGE MODE. In `tools/unattended/check-pass-order.sh`, both
  `build_commit` calls take `HR_EXCL` as an extra range token, the summary line gains the range field
  and a `waivers not judged` count, and in RANGE mode a waiver row naming a unit outside the range is
  counted rather than judged stale. Observed by AC2 and AC4.
- **S3** — `brief-recorded` IN RANGE MODE. The same in `tools/unattended/check-brief-recorded.sh`
  for every ranged `build_commit` call; the single-commit probes are unchanged. Observed by AC3.
- **S4** — THE TWO LEGS DECLARE `impure` in `tools/gate-legs.json`, with node d's reason text, so a
  verdict cached before the remote moved is not reused. Observed by AC6.
- **S5** — THE ARMS node d added to `tools/unattended/check-pass-order.test.sh` and
  `tools/unattended/check-brief-recorded.test.sh`, with the helper names `83eec3021` gave them.
  NOT OBSERVED by a criterion here: the suites run once at the close, and the arms are declared
  under `New arm:` in §7. AC5 observes that their bytes are node d's.
- **S6** — BYTE IDENTITY. Every hunk S1 to S5 write is node d's hunk, applied, never retyped. The
  patch is `git diff d99cd0328^ f8afa61bc` limited to the six files above, then `git show 83eec3021`
  limited to the two suites. Observed by AC5.
- **S7** — THE KICKOFF MANIFEST is re-stamped, because `tools/gate-legs.json` is on its `watch:`
  list. Observed by AC7.

## 3. Non-goals (OUT)

- Check 23's half of node d's unit: its RANGE mode in `tools/unattended/check-unattended.sh`, the
  per-build budget key that takes the ceiling key's place, the fleet line, the retired measuring
  flag, and the drift signal that reads the fleet line. §8 F1 splits them out, to
  `TOOL-aMendedFleet-92`, which builds the fleet line and the drift signal and finds the range mode,
  the budget key, the ceiling key and the flag already settled on main by another route. Their
  hunks also do not apply to this tree as they stand, which this unit's probe measured.
- Routing the driver or the kit gate through S1's reader. Node d left that as a known residual of
  three bounded observations of one advertisement, and this unit keeps their decision.
- Node d's later units, whose commits touch `tools/unattended/lib-unattended.sh` after these, and
  the `tools/unattended/unattended.test.sh` half of `83eec3021`, which renames unit 18's helpers.
- Bumping the unattended kit version, owed once at the close; node d's hunks bump nothing.

### Edges

- **hands-off** `TOOL-aMendedFleet-92` — check 23's range mode, its per-build budget, the fleet line and
  the drift signal reading it, which §8 F1 split off.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/` and in `.unattended.conf` equal
base `7af5f564`'s. Node d's branch is `origin/branch/unattended-build-closing-f90fd9`, read at
`a96ae2dfa`; node d's build base `98926870` is not an ancestor of this base, whose merge-base with
`d99cd0328` is `a587e82dc`.

- Node d's spec for its unit 17 at `d99cd0328` names thirteen scope items. S1 to S4 and S11 are the
  history legs; S5 to S10 and S12 are check 23, its keys, its flag and a drift signal. Its title
  says so too: the history legs, AND check 23 a per-build budget.
- `git diff d99cd0328^ f8afa61bc`, without node d's build folder and backlog, applied to this tree
  with `git apply --check`: the six files of S1 to S5 apply cleanly, with offsets; every other file
  fails, namely `tools/unattended/check-unattended.sh`, its suite, `cross-component.test.sh`, the
  kit example conf, `.unattended.conf`, both protocol copies, the kit README, the drift engine, its
  selftest, its README and `memory/guides/SESSION-KICKOFF.md`.
- The six-file patch, then `83eec3021`'s two suite hunks, applied in that order to a scratch index
  read from `7af5f564` with `GIT_INDEX_FILE` and `git apply --cached`: both apply. The resulting
  `tools/unattended/check-pass-order.test.sh` blob equals node d's blob at `83eec3021`; the other
  files differ from node d's whole files only where this tree and node d's diverged before them.
- No tracked file outside the two legs reads either leg's summary line: `git grep` for
  `pass-order: graded`, `brief-recorded: graded` and `waivers not judged` hits only the legs.
- `tools/run-gates/run-gates.sh` already honours an `impure` key; one leg in the manifest carries
  one today.
- The hunks cite node d's unit ids in comments and in the `impure` reason. No record on this tree
  anchors node d's slug, so `source_cited_ids_resolving_to_no_record` in the drift engine reads them
  as fixture-shaped and does not count them; they resolve when node d lands.

### Rollout

1. Build the patch as S6 says and apply it with `git apply --index`.
2. Re-stamp the manifest's `last-audit:` line, and commit once with the unit id in the subject and a
   `Decided:` trailer naming the reuse.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-pass-order.test.sh`
- `tools/unattended/check-brief-recorded.test.sh`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Re-implement RANGE mode here.** The owner's ruling asks for node d's bytes, and a retyped hunk is
  a conflict at the reconcile that an applied one is not.
- **Apply all of node d's unit, resolving the conflicts by hand.** Every hand resolution is a hunk
  that differs from node d's, which is the outcome the ruling exists to avoid, and the conflicting
  half is a second mechanism.
- **Leave the test helpers under their first names.** Node d renamed them because they took the
  lexicon leg's verb-offender count past its pin; carrying the first names would red the same leg
  here, and would differ from node d's final bytes.

## 5. Production-readiness checklist

- security — the range narrows what is graded, so its one input is observed from the remote and
  never read from a ref, a file or the environment the run controls; every failure widens to WHOLE.
- perf / scale — RANGE mode walks only the run's commits; each leg gains one bounded remote call.
  The saving is UNVERIFIED until the close's bar measures it.
- error / empty / loading states — an unreachable remote, an absent object and an empty range each
  select WHOLE with the reason on the summary line.
- observability — the summary lines name the mode, the tip and the waivers not judged.
- risks — remote CI runs with HEAD at the tip, so it reads WHOLE there and still grades all history.
- testing — AC1 to AC7; the arms in S5.
- migration — N/A: no conf key, no stored record.
- user docs — N/A: node d's hunks touch neither README for these two legs.

## 6. Acceptance criteria

- **AC1** — When a scratch script sources `tools/unattended/lib-unattended.sh` inside a fixture
  clone under a short `%TEMP%` root that has a bare origin, and calls `read_advertised_head` with the
  driver's path, it returns 0 and `ADVH_SHA` equals what `git ls-remote origin HEAD` prints; after a
  second clone pushes a commit to that origin, a fresh call returns the new sha; with the remote
  removed it returns 1 and `ADVH_WHY` names the missing remote.
  Red when: the reader is staged to read `refs/remotes/origin/HEAD`, which is stale after the second
  clone's push.
  fixture: under `%TEMP%`, never the scratchpad, whose long path fails a clone.
- **AC2** — When a scratch script built from the pass-order suite's prologue and its range arm runs,
  a fixture whose origin tip carries a unit built before its spec, and whose unpushed run adds one
  conforming unit, makes `check-pass-order.sh` exit 0 with a summary line carrying `range ` and the
  tip's first eight hex; adding a second unpushed built-before-specced unit makes it exit 1 naming
  that unit and not the pushed one.
  Red when: `HR_EXCL` is staged out of the first `build_commit` call, so the pushed unit reds the
  first run.
  cost: about a minute for the slice; the suite whole is never run.
- **AC3** — When the same kind of slice runs the brief-recorded range arm, a fixture whose origin tip
  carries a CLOSED unit with no brief row and whose unpushed run adds a CLOSED unit with one makes
  `check-brief-recorded.sh` exit 0 with `range ` on its summary line; adding an unpushed CLOSED unit
  with no row exits 1 naming that unit only.
  Red when: `HR_EXCL` is staged out of the ranged call.
- **AC4** — When the AC2 fixture's origin HEAD symref is pointed at a branch that does not exist,
  the pass-order summary line reads `range whole` with the unresolved-tip reason and the pushed unit
  reds as at base; with HEAD reset to the tip, it reads `range whole` with the nothing-unpushed
  reason.
  Red when: an unresolved tip is read as an empty range, so the pushed unit is never graded and the
  leg exits 0.
- **AC5** — When a scratch index is read from the unit commit's parent with `GIT_INDEX_FILE` and
  `git read-tree`, and S6's two patches are applied to it with `git apply --cached`, then for each
  of the six files `git rev-parse` of the index entry equals `git rev-parse` of that path at the unit
  commit.
  Red when: any hunk was retyped rather than applied, so one blob differs.
  cost: seconds; nothing outside the scratch index file is written.
- **AC6** — When `git diff HEAD~1 HEAD -- tools/gate-legs.json` runs at the unit commit, it shows
  one `impure` key added to the `pass-order history` entry and one to the `brief-recorded` entry,
  and no other entry changed.
  Red when: either leg lacks the key, or another leg moved.
- **AC7** — When `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` runs at the unit
  commit, the `last-audit:` line moved.
  Red when: `tools/gate-legs.json` moved and the manifest stamp did not.

## 7. Gates

`pass-order history` · `brief-recorded` · `unattended kit gate` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-pass-order.test.sh` · node d's range arms: a pushed built-before-specced unit beside a clean unpushed run, then a second unpushed violation; the unresolved-tip and nothing-unpushed WHOLE arms; a waiver row naming the pushed unit, not judged · none
New arm: `tools/unattended/check-brief-recorded.test.sh` · node d's range arms: a pushed CLOSED unit with no brief row beside a clean unpushed run, then an unpushed one; the unresolved-tip WHOLE arm · none

## 8. Open questions

- **F1** — Node d's unit is two mechanisms. Which half does this unit take?
  Options: all of it, resolving the conflicting files by hand; the history-leg half, splitting
  check 23's budget, the fleet line, the retired ceiling key and measuring flag and the drift signal
  into a unit of their own; the history-leg half alone with the rest dropped. The roster names this
  unit as the history legs, the brief's rule 2 is one mechanism per spec, and the probe in §4 shows
  that only the history-leg half applies as node d's bytes. Dropping the rest would leave a report
  point without a unit.
  RESOLVED (agent, 2026-10-04, delegated): split — check 23's range mode, the per-build budget key
  and the ceiling key it takes the place of, the measuring flag, the fleet line and the drift signal
  reading it move to a new unit the run adds.
- **F2** — Do node d's id citations in comments and in the `impure` reason stay?
  Options: keep them, as node d's bytes; rewrite them to this build's ids. Rewriting breaks S6, and
  the drift engine reads an id whose slug anchors no record here as fixture-shaped, so nothing on
  this tree counts them.
  RESOLVED (agent, 2026-10-04, delegated): keep node d's bytes, per S6.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 62 and report item [B#14], node d's
  spec at `d99cd0328`, and an applicability probe of node d's three commits against base.
- rev-2 · 2026-10-04 · §3 · the split-off half pointed at "a new unit the run adds"; it is
  `TOOL-aMendedFleet-92`, which narrowed it to the fleet line and the drift signal. The Edges bullet
  stays `external` until that unit declares the reciprocal edge.
- rev-3 · 2026-10-04 · §3 names the hands-off to TOOL-aMendedFleet-92, which declares the consumes-from back (check 12 edge join).
- rev-4 · 2026-10-04 · §1 status header order 62 -> 61: built before unit 61, whose insertion could break the byte-identical apply of node d's patch.

## 10. Reuse audit

The seam is node d's unit 17, reused as bytes: `read_advertised_head` and `read_history_range` in
`tools/unattended/lib-unattended.sh`, and the `build_commit` range token both legs already pass, at
`d99cd0328`, `f8afa61bc` and `83eec3021`. `python tools/codebase-map/reuse_lookup.py "grade only the
commits a closing run adds past the advertised default-branch tip"` returned name-stem neighbours,
`build_run_model` and `measure_commitment` in the runlog kit, none of which walks a leg's range, and
printed `unscanned layers: .sh`; node d's own §10 recorded the same blindness and read the shell
seams directly, which this unit's `git apply --check` probe re-verified against this tree. Recall
returned `TOOL-dBriefedPass-3` on why pass order is graded twice, `TOOL-dPolishedVitrine-14` on
brief-recorded grading only units built while a run was live, `TOOL-aRepatriatedFork-48` and `-51`
on the two legs' build-commit selection and waiver registry, and an ask recording `pass-order
history` at 134 s against its ceiling. None records a reason to keep grading landed history. Where
the report and the tree disagree: the report says land node d's unit; this tree cannot take its
check 23 half as node d's bytes, so §8 F1 splits it.

Recall terms used: `python tools/memory-recall/query.py "why do the pass-order and brief-recorded
history legs grade landed history on every closing run" --terms "pass-order history brief-recorded
history leg advertised tip RANGE mode WHOLE build_commit closing run landed"`
