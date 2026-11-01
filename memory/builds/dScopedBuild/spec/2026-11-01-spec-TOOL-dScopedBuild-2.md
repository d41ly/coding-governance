# TOOL-dScopedBuild-2 — built specs frozen, and every closing-review finding disposed as new units

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 3 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0400@d5dcbafa whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md) | research | TOOL-dScopedBuild-4 TOOL-dScopedBuild-13 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-2-1-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-2-1-reuse-scout.md) | journal | — |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

A closing review's blockers are folded into an already-built unit as a spec revision, so the trail
of what was built against which spec breaks (gap-flow-05, P19). This unit freezes a landed unit's
spec: a revision of it is refused at the commit, with or without a deviation record, and a
status-only edit passes. And it makes the method and the attended Skill say what the driver already
enforces at a review's exit: every closing-review finding becomes a new unit by `review.findings`,
never a fold.

## 2. Scope (IN)

- **S1** — The I12 landed predicate: `read_landed_units(root, units)` in
  `tools/memory-tree/deviation_join.py`, `units` mapping each unit id to its spec's path, reads every
  path at the ref `read_decision_ref(root)` resolves (`:676`), in one `read_blobs_at` batch, and
  returns `(landed, why)`: `landed` is the set of units whose spec header there matches
  `tree_lib.HDR_RE` (`tools/memory-tree/tree_lib.py:376`) with the token `CLOSED`. A ladder refusal,
  and a ref that names no commit in the clone, return `(None, why)`. HEAD's header is never read for
  this, because the harness writes `CLOSED` in the build commit on the run branch. Observed by AC1.
- **S2** — The frozen arm of `deviation_join.py --staged`, the I11 verb TOOL-dScopedBuild-14 S7 builds.
  Its population is every staged path a spec file name matches (`tree_lib.build_spec_path_re`) that
  has a pre-image at `HEAD`: a modification, a deletion, or a rename from such a path, as `git diff
  --cached --name-status -M` lists them. The unit is the id the `HEAD` blob's H1 defines. A
  modification, or a rename with a change, is a revision when `check_material` (`:436`) reads its
  `HEAD` blob and its index blob as different; a deletion is a revision; a pure rename is not. Each
  revision of a unit S1 reads landed is refused, one line naming the unit, the ref, the path and the
  remedy, a new unit, and the verb exits 1, whatever deviation records are staged or tracked. The arm
  runs whatever the `DESIGN_*` keys say, because the freeze is no chain-build rule. Where S1 returns
  `None` and a revision exists, the arm refuses naming why. Observed by AC2, AC3, AC4, AC5.
- **S3** — The strip: where the unattended kit's `GEN_REGION_AWK` does not resolve
  (`read_gen_region_awk`, `:357`), the frozen arm prints one held line naming the kit and why, and
  grades nothing, §8 F2. Observed by AC5.
- **S4** — Check 32 carries the arm: its name becomes "a staged spec revision answers to
  `deviation.gate`, and a landed unit's spec is not revised", in
  `tools/memory-tree/check-memory-hygiene.sh` and in the check catalogue of
  `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`. The check's exit handling
  is TOOL-dScopedBuild-14 S8's. Observed by AC6.
- **S5** — The disposal, in the method. The in-place blocker fold M8 prescribes, the sentence opening
  `Fix every blocker, and ONLY blockers` at `tools/memory-tree/BUILD-METHOD.template.md:274`, is
  retired: it reads that no finding is folded into a built unit, that each blocker becomes a new unit
  as `review.findings` counts it (TOOL-dDeclaredLoop-20 S4), specced and built as any unit, that
  highs, mediums and lows carry to the exit where M4 promotes them, and that the re-review reads those
  units. Round N's base sentence (`:256-257`) reads the units that round's blockers became, never a
  fold. The render `memory/guides/BUILD-METHOD.md` is the template's copy, and the file stays within
  M1's 30720-byte budget.
  **Readers:** by name: `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md`.
  by value: NO VALUE READERS — `git grep` of the sentence outside `memory/builds/` finds only these two
  carriers and the Skill of S6, and no arm, fixture or leg asserts it. Observed by AC7, AC9.
- **S6** — The disposal, in the attended Skill. Stage 6 of `tools/roles/SKILL.template.md`, whose
  sentence at `:78-80` makes "each blocker's fix … a pass of the unit it lands in", is retired: it
  reads that each finding the review confirms becomes a new unit as `review.findings` counts them,
  specced through Stage 3's harness and built through Stage 5, then re-reviewed (M8). The render
  `.claude/skills/build/SKILL.md` is `adopt-roles.sh`'s copy.
  **Readers:** by name: `tools/roles/SKILL.template.md`, `.claude/skills/build/SKILL.md`. by value:
  NO VALUE READERS — the render's sync check compares the bytes and asserts no sentence. Observed by
  AC8.
- **S7** — What the freeze does not catch, stated here as the scout found it (scout C disagreement 2):
  gap-flow-05's motivating case, dSweptBranches' "blockers folded into unit 3 rev-3", was a fold BEFORE
  landing, which S2's "landed" trigger does not refuse. It is caught by S5 and S6, which stop
  prescribing the fold, and by TOOL-dScopedBuild-14's gate over the first-pass arm, which refuses a
  revision past a unit's first pass with no record under `deviation.gate` `refuse`. NOT OBSERVED by
  this unit: TOOL-dScopedBuild-14 AC8 observes that refusal.

## 3. Non-goals (OUT)

- The promotion count and its three values: TOOL-dDeclaredLoop-20 S4 specs `review.findings`, and
  the driver's `verb_review` (`tools/unattended/unattended.sh:12673`), check 2 and the DISPOSAL stage
  compute from it there. This unit points at that count and never re-derives it.
- The driver's refusal of `--disposition fold` at a terminal exit, which stands (`:12786-12830`).
- A push-time freeze over history: the clause names the commit, and a `--no-verify` commit or a
  hook-less clone is not refused here.
- A spec revision before landing: TOOL-dScopedBuild-14's arm grades it under `deviation.gate` (S7).
- Widening the trigger from "landed" to "built", §8 F1.
- A spec audit's own folds before any code (M4), which revise no built unit.

### Edges

- **consumes-from** `TOOL-dScopedBuild-14` — `--staged`, the I11 verb and hygiene check 32 the frozen
  arm joins; without them the arm has no commit-time host
- **consumes-from** external — TOOL-dDeclaredLoop-20 S4's `review.findings` count, DEFERRED at base,
  which S5 and S6 point at; its default `blocker-high-own` is today's rule, so the text holds before
  it lands
- **hands-off** `TOOL-dScopedBuild-28` — S2's frozen arm, which that unit's widened pre-commit trigger reaches on a deletion-only commit, observed there through the hook (id 14)
- **hands-off** `TOOL-dScopedBuild-35` — AC6's command, restated by that unit's S9, and S1's landed read, whose freshness line its S20 prints (ids 13, 38)

## 4. Design

### Evidence

Read at `5f0b11f12`; no product file differs from base `f4597719`.

- `check_material(before, after)` (`deviation_join.py:436-438`) compares the two texts less their
  `**Status:**` line and every generated region, the strip read from `lib-unattended.sh:1136`.
- `read_decision_ref` (`:676-689`) returns `<remote>/<branch>` from the remote ladder, `main` where
  it names none, with `GIT_ENV_LEAKS` held aside.
- The join's revision arm already finds a revision after a unit's first pass (`:589-602`) and only
  reports it; nothing reads the mainline's status, and nothing refuses at the commit
  (`.githooks/pre-commit` names neither `deviation_join` nor `routed_commits`).
- `verb_review` already promotes at every terminal exit and refuses `fold` there
  (`unattended.sh:12786-12830`), while M8 (`BUILD-METHOD.template.md:274`) and the Skill's Stage 6
  (`SKILL.template.md:78-80`) still prescribe the in-place fix (scout C disagreement 5).
- `memory/guides/BUILD-METHOD.md` is 29354 bytes and 362 lines at `5f0b11f12`, PINNED; M1's budget is
  30720 bytes.

### The frozen arm

```
for each staged spec path P with a HEAD pre-image (M, D, or R from P):
    unit = parse_spec_h1(HEAD:P)
    revised = deleted, or check_material(HEAD:P, :P') is true      # P' the index path
landed, why = read_landed_units(root, {unit: P for each revised})
landed is None and a revision exists -> refuse naming why
each revised unit in landed -> "deviation: frozen — <unit> is CLOSED at <ref>; its spec <P> is
    revised at the commit, and a change to a built unit is a new unit", exit 1
```

### The rewritten sentences

M8 at `:274`, its bytes within 120 of the sentence it rewrites: "Fold no finding into a built unit:
each blocker becomes a new unit as `review.findings` counts it, specced and built as any unit, and
highs, mediums and lows carry to the exit, where M4 promotes them. Then re-review those units, not
the diff again. A blocker unbuildable inside the mandate's scope is a park, not a waiver, and the
build does not close." Round N's base at `:256-257` reads the units "that round's blockers became
instead of re-reading the diff, and passes those blockers as `priorFindings`".

Byte delta, measured against the template at `5f0b11f12`: the M8 sentence grows from 249 to 352
bytes, +103, and the round-N clause shrinks from 115 to 112, −3, so this unit adds 100 bytes to
the render. TOOL-dScopedBuild-13 S9 adds 271 more; the two sum to 371, inside the 1366 bytes M1's
30720-byte budget leaves above the render's 29354.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_landed_units` | python function, `deviation_join.py` | `py.function`, OK |
| `frozen-edit`, `frozen-recorded`, `frozen-status`, `frozen-gen`, `frozen-unlanded`, `frozen-delete` | `deviation_join.py` fixture plants | none |

### Rollout

Live at landing, at every commit that stages a landed unit's spec. Every tracked landed spec is
already frozen by practice (`TEMPLATE-SPEC.md` "a landed record is frozen"), and the index generator's
record regions are stripped, so no routine commit is refused.

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`: S1, S2, S3, the plants and their arms
- `tools/memory-tree/check-memory-hygiene.sh`: S4
- `tools/memory-tree/check-memory-hygiene.test.sh`: S4's arm
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`: S4
- `tools/memory-tree/BUILD-METHOD.template.md` and its render `memory/guides/BUILD-METHOD.md`: S5
- `tools/roles/SKILL.template.md` and its render `.claude/skills/build/SKILL.md`: S6

### Alternatives rejected

- **A freeze in the push-time host over history.** Lost to the clause, which names the commit, and to
  history: a landed spec revised before this unit would red every push.
- **A `deviation.gate`-graded freeze.** Lost to the clause's "with or without a deviation record": a
  record must not admit a revision of a landed unit's spec.
- **The landed test at `HEAD`.** Lost to scout C disagreement 1: the harness writes `CLOSED` before
  landing, so `HEAD` reads unlanded units as landed.

## 5. Production-readiness checklist

- security — deny by default: an unread mainline refuses a revision rather than reading it unlanded.
- perf / scale — one `diff --cached`, one blob batch for the pre- and post-images, one for the
  mainline headers, and one strip per candidate; no history is read.
- error / empty / loading states — no staged spec is check 32's held line; an unresolved strip is one
  held line naming the kit.
- observability — each refusal names the unit, the ref, the path and the remedy.
- risks — an adopter without the unattended kit has the freeze held, announced (§8 F2); a
  `--no-verify` commit is not refused (§3).
- testing — the arms of §7, over the join's own fixture with its remote.
- migration — none.
- user docs — `memory/HYGIENE.md`, `memory/guides/BUILD-METHOD.md` and the `/build` Skill, each
  through its template.

## 6. Acceptance criteria

- **AC1** — When `read_landed_units` runs in a fixture whose remote's `main` holds unit A's spec
  `CLOSED` and unit B's `OPEN` while `HEAD` holds both `CLOSED`, it returns `{A}`; with the remote's
  ref absent it returns `None` and a reason.
  Red when: B reads landed, which is the harness's run-branch case.
  fixture: the join's own fixture, its remote added by `add_fixture_remote`.
- **AC2** — When `python deviation_join.py --fixture --plant frozen-edit --staged` runs, the plant
  staging an in-place body edit of a landed unit's spec, it exits 1 printing `frozen` and the unit.
  Red when: the planted in-place edit of a landed unit's spec passes.
- **AC3** — When `--plant frozen-recorded --staged` runs, the same edit staged beside a deviation
  record departing from that unit's revision, it exits 1; `--plant frozen-delete --staged` exits 1.
  Red when: a record, or a deletion, admits the revision.
- **AC4** — When `--plant frozen-status --staged` runs, a status-only edit of a landed unit's spec,
  it exits 0; `--plant frozen-gen --staged`, an edit inside a generated region, exits 0;
  `--plant frozen-unlanded --staged`, an edit of a spec `CLOSED` at `HEAD` and not at the remote's
  `main`, raises no `frozen` line.
  Red when: the status-only edit is refused, or an unlanded unit reads frozen.
- **AC5** — When the frozen arm runs with `read_gen_region_awk` stubbed to raise, it prints one held
  line naming `GEN_REGION_AWK` and refuses nothing.
  Red when: the arm refuses or passes silently with no strip.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged --only 32` runs in a scratch
  tree staging the AC2 edit, it fails check 32 naming the unit and `frozen`; staging the AC4
  status-only edit, it passes.
  Red when: check 32 passes the planted edit.
  fixture: the hygiene suite's scratch tree with its remote; none exists in this tree.
- **AC7** — When `grep -n "review.findings" tools/memory-tree/BUILD-METHOD.template.md
  memory/guides/BUILD-METHOD.md` runs it prints M8's sentence in both files, and `grep -c "Fix every
  blocker"` over the same two files prints 0 for each.
  Red when: M8 still prescribes fixing a blocker inside its built unit.
- **AC8** — When `grep -n "review.findings" tools/roles/SKILL.template.md .claude/skills/build/SKILL.md`
  runs it prints Stage 6's sentence in both, and `grep -c "pass of the unit it lands in"` prints 0
  for each.
  Red when: Stage 6 still sends a blocker back to the unit it lands in.
- **AC9** — When `wc -c memory/guides/BUILD-METHOD.md` runs after the pass, it prints at most 30720.
  Red when: the rewrite breaches M1's byte budget.
  figure: DERIVED at the pass; 29354 at `5f0b11f12` is the PINNED reading of §4.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `routed-commits selftest` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/deviation_join.py · covers AC1 AC2 AC3 AC4 AC5 · the selftest's six frozen plants over the fixture's remote, its failing case `frozen-edit` exiting 0 · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 · a scratch tree staging a landed unit's body edit and its status-only twin, its failing case check 32 passing the body edit · none

## 8. Open questions

- **F1 — What is "landed"?** Options: (a) `CLOSED` at the mainline ref the remote ladder resolves, I12;
  (b) `CLOSED` at `HEAD`; (c) built, a first pass in history. (b) freezes a unit the harness closed on
  its run branch, which has not landed, and (c) refuses a revision M2 sanctions before landing,
  diverging by a rev bump with its deviation record, both departing from the clause's word.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 1, the clause says "a spec whose unit has landed";
  S7 states the pre-landing case and where it is caught. widens: none · relaxes: none
- **F2 — What does the arm do where the strip does not resolve?** Options: (a) exit 2, failing check
  32 on every staged spec revision; (b) one held line naming the kit, grading nothing; (c) the identity
  strip, the status line alone. (c) reads every records-region render of a landed spec as a revision
  and refuses commits nobody can avoid, failing AC4's generated-region case; (a) fails every adopter
  commit that edits a spec where the memory-tree kit is installed without the unattended kit. RESOLVED
  (agent, 2026-11-01, delegated): (b), rung 3, the held line announcing what is not graded; gov's tree
  resolves the kit, so gov is graded. widens: none · relaxes: none
- **F3 — Which staged changes are revisions?** Options: (a) a material modification, a rename with a
  change, and a deletion, a pure rename passing; (b) a material modification alone. (b) lets a
  deletion and a re-add under a new name bypass the freeze. RESOLVED (agent, 2026-11-01, delegated):
  (a), rung 3. widens: none · relaxes: none
- **F4 — How do M8 and Stage 6 dispose a closing review's findings?** Options: (a) rewrite both
  sentences to mint each finding as a new unit by `review.findings`; (b) leave the text, relying on
  the driver's terminal-exit refusal. (b) leaves standing the fold P19 forbids, failing the clause.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3; grants: PLAY-dClosedLoop-3 M8's fold sentence and the attended Skill's Stage 6 rewritten, a governance-carrier change the clause names. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 2, v2:914-916 (P19), flow-steps:302-306,
  gap-register:110, scout C's row for this unit and its disagreements 1, 2, 3 and 5, and the spec
  brief's I11 and I12.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-28, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are `check_material` (`tools/memory-tree/deviation_join.py:436`), the one
status-only predicate, called and never re-stripped; `read_decision_ref` (`:676`), the one mainline
ref; `read_blobs_at` (`tools/memory-tree/tree_lib.py`) and `HDR_RE` (`:376`) for the headers; and
TOOL-dScopedBuild-14's `--staged` verb and check 32 as the commit-time host. `python
tools/codebase-map/reuse_lookup.py "refuse a commit that revises the spec of a unit already landed on
the default branch, unless only its status line changed"` ranked `read_spec_revisions`
(`tools/memory-tree/design_lib.py`), which reads revisions over history and not the index, then
`parse_spec_h1` and `build_spec_path_re` (`tools/memory-tree/tree_lib.py`), which S2 calls for the
unit and the population, among name-token helpers; none reads a landed status, so
`read_landed_units` is new over existing readers.
Scout C's row holds against source at `5f0b11f12`, its `deviation_join.py:436`, `:676` and
`check-memory-hygiene.sh:1802`, `:1843` reading as it says; its proposed check number 32 is the one
TOOL-dScopedBuild-14 F4 decides.

Recall terms used: `python tools/memory-recall/query.py "how is a built unit's spec frozen against an in-place revision after landing" --terms "frozen spec landed CLOSED check_material status-only revision fold blocker review.findings P19 mainline"`
