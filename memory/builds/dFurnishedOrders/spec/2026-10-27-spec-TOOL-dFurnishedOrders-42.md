# TOOL-dFurnishedOrders-42 — the third spec audit's 19 roles, runlog, hooks, unattended and kickoff minors: criteria that read what they claim, one output for an empty transcript, imports gated as a class, the posture read decoded and bounded, and a runner bound a suite can lower

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 08e30fef · streams tooling · order 25 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 |
| [2026-10-27-build-TOOL-dFurnishedOrders-42-deviation-421.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-42-deviation-421.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 |
| [2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
confirmed 28 MEDIUM and 3 LOW findings. BUILD-METHOD M4 batches them, and they split into two
disjoint write sets by M6 (`TOOL-dFurnishedOrders-41` §4 "Why two units"): `TOOL-dFurnishedOrders-41`
takes the 12 that land on the govkit upgrade step, and this unit the other 19. Each report id is named
once below and closed by its own scope item; ids the report merged into one item still take one
scope item each.

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M1 | 1 | MEDIUM | unit 37 AC3, S4; unit 38 S2 | S1 |
| M2 | 2 | MEDIUM | unit 37 AC11 | S2 |
| M2 | 23 | MEDIUM | unit 37 S17, §4 Clause 1 | S3 |
| L2 | 16 | LOW | unit 37 S17 | S4 |
| M3 | 3 | MEDIUM | unit 37 S1, S10, §4 | S5 |
| M3 | 22 | MEDIUM | unit 37 S10, §1; unit 16 S2, AC2 | S6 |
| M4 | 4 | MEDIUM | unit 37 S2, S3, AC2; unit 29 S6 | S7 |
| M5 | 5 | MEDIUM | unit 37 S32, S33, AC7, AC17 | S8 |
| M6 | 6 | MEDIUM | unit 32 S1, AC2 | S9 |
| M6 | 25 | MEDIUM | unit 32 AC2 | S10 |
| M7 | 7 | MEDIUM | unit 37 S25, §5, AC14 | S11 |
| M9 | 11 | MEDIUM | unit 31 §10, S2, F3 | S12 |
| M22 | 35 | MEDIUM | unit 31 §5, AC1 | S13 |
| M10 | 12 | MEDIUM | unit 34 S1, S2, §4 | S14 |
| M11 | 13 | MEDIUM | unit 37 AC9 | S15 |
| M16 | 21 | MEDIUM | unit 34 S2, AC2; unit 37 AC8 | S16 |
| M17 | 26 | MEDIUM | unit 37 S12, S26, AC8 | S17 |
| M18 | 30 | MEDIUM | unit 37 S22, AC12 | S18 |
| L3 | 20 | LOW | unit 34 S2, §3, §10 | S19 |

## 2. Scope (IN)

- **S1** — id 1. The converted arms counted. Beside `TOOL-dFurnishedOrders-38`'s red pattern, the
  adopt-unattended half of unit 37 AC3 has a floor over content: `git grep -h -e "for-diff HEAD~1" --
  tools/unattended/adopt-unattended.test.sh` piped to `grep -c "^[[:space:]]*miss "` prints at least
  3, so deleting, commenting out or reshaping the arms cannot pass. Unit 37's ledger answers that
  half of AC3 in the AMENDED form, naming this item and unit 38. Observed by AC1.
- **S2** — id 2. Unit 37 AC11 is the ratchet's own predicate. W is `git rev-list -1 <stamp>..HEAD`
  over every path the `watch:` line of `memory/guides/SESSION-KICKOFF.md` lists, read by its key; S is
  the newest commit in `<stamp>..HEAD` whose `last-audit:` value differs from its parent's, as
  `skills/session-kickoff/manifest-check.sh:1525-1534` finds it; and `git merge-base --is-ancestor W
  S` exits 0, or W is empty. Unit 37's ledger answers AC11 in the AMENDED form, naming this item.
  Observed by AC2.
- **S3** — id 23. The re-stamp's place. Unit 37 S17's re-stamp lands bundled with, or after, the last
  commit touching a watched path, as the ratchet's failure text invites; the units that edit watched
  paths are 1 and 13 (`skills/session-kickoff/SKILL.md`, `manifest-check.sh`), 4
  (`memory/guides/BUILD-METHOD.md`), 6 (`tools/gate-legs.json`), 29, 30 and 37, all ordered at or
  before 23; units 38 to 42 edit none. Observed by AC2.
- **S4** — id 16. The `watch:` line found by its key, never a line number: it is line 6 of
  `memory/guides/SESSION-KICKOFF.md` at `08e30fef`, where unit 37 S17 cites `:5`, the `last-audit:`
  line. Observed by AC2.
- **S5** — id 3. One output for an empty transcript. `runlog.py turns` (`TOOL-dFurnishedOrders-16`
  S2, with unit 37 S1 and S10) prints, for a transcript holding no event, the single line `untimed 0`
  and exits 0; a missing transcript keeps unit 37 S1's exit 3. Observed by AC3.
- **S6** — id 22. Unit 16's count amended. Unit 37 S10 lands on unit 16 S2 and AC2 as well: unit 16's
  ledger answers AC2 in the AMENDED form, three event lines then `untimed 0`, naming unit 37 S10 and
  this item, and the `turns` arm of `tools/runlog/selftest.py` expects four lines. Observed by AC3.
- **S7** — id 4. The roles kit's imports gated as a class. `read_cap_answer`
  (`tools/roles/roles_lib.py:140-156`) loads the policy kit's `budgets.py` through
  `load_kit_module("policy", "budgets.py", "gov_policy_budgets")` (`TOOL-dFurnishedOrders-29` S6) and
  keeps its `sys.path` insert of the policy kit's directory, which `budgets.py`'s own `import policy`
  (`tools/policy/budgets.py:49`) reads; no `import` or `from` statement in `tools/roles/*.py` names a
  module other than the roles kit's own modules and the standard library. Unit 37's ledger answers
  AC2's first arm in the AMENDED form, naming this item. Observed by AC4.
- **S8** — id 5. Unit 37's criteria carry S33's branch. Where `grep -n "def validate_return"
  tools/roles/roles_lib.py` prints nothing at unit 37's pass, its ledger answers AC7's last clause in
  the AMENDED form, and `tools/roles/README.md` names no checker TOOL-dBoundRoles-5 S1 or
  TOOL-dBoundRoles-26 S2 has not built; where `FACT_RE` is absent from `roles_lib.py` and
  `tools/hooks/agent-cap.js`, it answers AC17 in the AMENDED form, naming TOOL-dBoundRoles-13 and
  this item. Observed by AC5.
- **S9** — id 6. The duplicate member observed. Unit 32 S1's "member named twice" case is a criterion:
  `subject-reads: input:diff|input:diff` is an `R3` defect naming the role and the entry. Observed by
  AC6.
- **S10** — id 25. Unit 32 AC2's fixture on both rosters. Its group values are planted in
  `gov-skeptic.agent.md`, whose `reads` line, `input:diff?, input:spec?`, exists before and after
  TOOL-dBoundRoles-1's merge; unit 32's ledger answers AC2 in the AMENDED form, naming this item.
  Observed by AC6.
- **S11** — id 7. The broken-index branch scoped to its step. Unit 37 S25 governs unit 29 S3's
  `writes none` step alone: on a broken `.claude/roles.json` that step denies a payload carrying
  `agent_type` and leaves one with none to the later steps, and steps 6a and 9a
  (`tools/hooks/scratch-guard.js:1100-1110`) still deny every spec and product write on a broken
  index, the main loop's included. Unit 37 AC14's main-loop payload is a note x.md under
  `memory/notes/`, neither spec nor product class, and unit 37's ledger answers AC14 in the AMENDED
  form, naming this item. Observed by AC7.
- **S12** — id 11. Unit 31's field render grounded. The return template line unit 31 S2 appends to is
  composed by TOOL-dBoundRoles-43 S13, by way of `TOOL-dFurnishedOrders-15` S1, and `render_role`
  (`tools/roles/roles_lib.py:604-617`) renders none at `08e30fef`. At this pass the rendered
  `gov-builder` role carries `establishes:list` on its template line, or, where TOOL-dBoundRoles-43
  S13 is still unbuilt, unit 31's ledger answers AC2 in the AMENDED form, naming it and this item.
  Observed by AC8.
- **S13** — id 35. Unit 31's arm set observed. The outcomes of `derive_return_arms`'s triples equal
  the set of `[return.<name>]` tables of `tools/roles/role-schema.toml` that declare `outcome`, and
  `render_return_schema`'s `anyOf` holds that many branches plus the template's; a table that
  loses its `outcome` turns the probe red. Observed by AC8.
- **S14** — id 12. The posture read's encoding stated. `derive_attended` runs `breakpoints.py list`
  with `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8` set in the child's environment, and the runner
  decodes its output as UTF-8, so the `attendance —` line matches on a host whose shell exports
  neither. Observed by AC9.
- **S15** — id 13. Unit 37 AC9's verdict relative to its sleeper. The stub `gov_map.py` sleeps 120
  seconds and each append returns in under 100 seconds, the form
  `skills/session-kickoff/manifest-check.test.sh:1741-1751` records; unit 37's ledger answers AC9 in
  the AMENDED form, naming this item. Observed by AC10.
- **S16** — id 21. The posture read observed under a descendant holding stdout. With unit 39's
  file-backed runner, a stub `breakpoints.py` that leaves a sleeper holding stdout and exits 0 is
  answered within the bound plus the kill grace, and unit 34 AC2 and unit 37 AC8 carry that stub.
  Observed by AC9.
- **S17** — id 26. A bound a suite can lower. `roles_lib.py` reads `ROLES_SLOT_BOUND` once, beside
  `CHECKER_BOUND_S`; when it is a positive integer, every `run_slot_reader` call runs under the smaller
  of it and its own bound. Unit 37 AC8's stubs sleep past `ROLES_SLOT_BOUND=2`, so
  `tools/roles/adopt-roles.test.sh` stays inside its 60-second row
  (`tools/run-gates/selftest-budgets.txt:96`). Observed by AC11.
- **S18** — id 30. The no-bypass probe joins lines. Unit 37 AC12's `awk` joins each line ending in `\`
  with the next before matching, and matches `owner-question` alone, outside `read_owner_door`'s body,
  over every `tools/unattended/*.sh` but `*.test.sh`; its planted negative is a call continued across
  two lines. Unit 37's ledger answers AC12 in the AMENDED form, naming this item. Observed by AC12.
- **S19** — id 20. One runner in the roles kit's Python. Every `subprocess` call in
  `tools/roles/*.py` sits inside the `run_bounded_py` block unit 39 inlines, and unit 34's posture
  read reaches it through `run_slot_reader`, not a runner of its own. Observed by AC13.

## 3. Non-goals (OUT)

- The HIGH findings of the same report: `TOOL-dFurnishedOrders-38` to `-40`.
- The 12 govkit upgrade-step minors: `TOOL-dFurnishedOrders-41`.
- Rewording the spec text of units 16, 31, 32, 34 and 37: each item states the built tree's end
  state, and where a landed criterion cannot hold as written, that unit's ledger answers it AMENDED,
  naming the item.
- The report's left-shift gates, the spec-lint rules and checklist entries: no clause of this build
  names them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-16` — the `turns` verb's AC2 and its selftest arm, which S6 amends for the `untimed` line (id 22)
- **consumes-from** `TOOL-dFurnishedOrders-29` — `load_kit_module` and `run_slot_reader`, through which S7 loads `budgets.py` and S17 lowers the bound (ids 4, 26)
- **consumes-from** `TOOL-dFurnishedOrders-31` — S2's template-line render and AC1's arm assertions, which S12 grounds and S13 completes (ids 11, 35)
- **consumes-from** `TOOL-dFurnishedOrders-32` — S1's duplicate-member case and AC2's fixture, which S9 and S10 settle (ids 6, 25)
- **consumes-from** `TOOL-dFurnishedOrders-34` — the posture read, whose encoding, descendant bound and runner S14, S16 and S19 settle (ids 12, 21, 20)
- **consumes-from** `TOOL-dFurnishedOrders-37` — AC2, AC3, AC7, AC8, AC9, AC11, AC12, AC14 and AC17, S1, S10, S17, S22 and S25, which S1 to S8, S11 and S15 to S18 settle (ids 1, 2, 23, 16, 3, 22, 4, 5, 7, 13, 21, 26, 30)
- **consumes-from** `TOOL-dFurnishedOrders-38` — the `miss` helper and the arms written with it, whose floor S1 counts (id 1)
- **consumes-from** `TOOL-dFurnishedOrders-39` — the file-backed `run_slot_reader`, which S16 observes on the posture read, S17 bounds lower and S19 counts as the one runner (ids 21, 26, 20)
- **hands-off** `TOOL-dFurnishedOrders-46` — S2, S3, S7, S14, S17, S19, AC2, AC4 and AC13 and its staged breaks, which unit 46 S1, S2, S4 to S6, S10, S12 and S18 settle (ids 2, 3, 10, 15, 16, 4, 12, 33 of the fourth audit)

## 4. Design

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so, as `TOOL-dFurnishedOrders-37` §4 does. Why this half is disjoint
from unit 41 is `TOOL-dFurnishedOrders-41` §4 "Why two units", stated once there.

### The ratchet's predicate, as S2 reads it

```
LA := the sha after "@" on the last-audit: line
W  := git rev-list -1 LA..HEAD -- <each path on the watch: line, ";"-separated>
S  := first of git log --format=%H -G'^last-audit:' LA..HEAD whose stamp differs from its parent's
W empty, or git merge-base --is-ancestor W S  -> green
```

### The `turns` read after S5

```
no transcript     -> exit 3, stderr "runlog: no transcript for session <sid>"   (unit 37 S1)
no event          -> "untimed 0", exit 0
events            -> "<utc> owner <via>" | "<utc> keepalive" lines, then "untimed <n>", exit 0
```

### The import gate, as S7 reads it

`python -c` parses each `tools/roles/*.py` with `ast`, collects the first segment of every
absolute `import` and `from` module, and prints each one that is neither a stem of `tools/roles/*.py`
nor in `sys.stdlib_module_names`. At `08e30fef` it prints `roles_lib.py 150 budgets` (PINNED,
measured 2026-10-27).

### Inventory

Minted: the environment knob `ROLES_SLOT_BOUND` of S17; the private module name `gov_policy_budgets`
of S7; the stdout line `untimed 0` for an empty transcript, a value of unit 37 S10's grammar. No
function.

### Migration

None: no stored data changes shape.

### Rollout

Live at landing, at order 25, after every unit it lands on. `KIT_ROLES_VERSION` and the runlog kit's
version move for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/runlog/runlog.py`
- `tools/runlog/selftest.py`
- `tools/hooks/scratch-guard.test.sh`
- `tools/unattended/unattended.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`

### Alternatives rejected

- **Admit `budgets` as the one bare sibling import (S7).** A named exception is a list, and the next
  sibling import passes beside it; the class gate fails on any.
- **Re-price the roles adopter row instead of a knob (S17).** Every bar run would still pay a minute
  of sleep for two stubs.
- **Match the posture line on its ASCII prefix (S14).** It changes the matched grammar of
  KICK-dKeptSession-17's line; stating the encoding keeps the line as that unit prints it.

## 5. Production-readiness checklist

- security — S11 keeps steps 6a and 9a denying every spec and product write on a broken index; S7
  loads a sibling kit's module under a private name, from the resolved kit directory only.
- perf / scale — S17 lets the roles suite run its bound arms in seconds; S15 removes an absolute wall
  clock from a criterion.
- error / empty / loading states — S5 gives an empty transcript one output; S8 gives an unbuilt parent
  one answer.
- observability — the `untimed` line, the ledger's AMENDED answers and the import gate's printed
  offenders each name their cause.
- risks — S8 and S12 depend on DEFERRED parent units; each takes the AMENDED route when its parent is
  absent and is observed either way.
- testing — AC1 to AC13 by probes and fixtures; the arms of §7 at the close.
- migration — none.
- user docs — `tools/roles/README.md` by S8.

## 6. Acceptance criteria

- **AC1** — When `git grep -h -e "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh` runs
  piped to `grep -c "^[[:space:]]*miss "`, it prints at least 3.
  Red when: the arms are deleted or reshaped and unit 38's red pattern passes on nothing.
  figure: the floor 3 is PINNED by the three arms at `08e30fef`.
- **AC2** — When the four lines of §4 "The ratchet's predicate" run in `bash` at this unit's pass,
  reading the `last-audit:` and `watch:` lines of `memory/guides/SESSION-KICKOFF.md` by their keys,
  W is empty or `git merge-base --is-ancestor` exits 0.
  Red when: a watched edit lands after the re-stamp, units 38 to 42 included, or the criterion reads
  two of the eleven paths.
- **AC3** — When `python tools/runlog/runlog.py turns --session <sid> --transcripts <dir>` runs over a
  scratch transcript holding no event, it prints exactly `untimed 0` and exits 0; over one holding two
  owner prompts and one keepalive fire, it prints four lines, the last `untimed 0`.
  Red when: an empty transcript is answered two ways, or unit 16's count reds on the added line.
  fixture: scratch transcripts roots under `%TEMP%`.
- **AC4** — When §4 "The import gate" runs over `tools/roles/*.py` it prints nothing; run over a
  scratch copy in which `handoff.py` gains `import gov_map`, it prints that line.
  Red when: a bare sibling import passes because its name is not on a list.
  figure: it prints one line at `08e30fef` (PINNED), so it is red before the unit is built.
- **AC5** — When `grep -n "def validate_return" tools/roles/roles_lib.py` prints nothing,
  `grep -n -E "validate_return|TOOL-dBoundRoles-(5|26)" tools/roles/README.md` prints nothing and unit
  37's ledger answers AC7 AMENDED; when `git grep -n FACT_RE -- tools/roles tools/hooks/agent-cap.js`
  prints nothing, unit 37's ledger answers AC17 AMENDED naming `TOOL-dBoundRoles-13`.
  Red when: a faithful build of unit 37 S33 fails a criterion it cannot meet, or quietly rewrites it.
- **AC6** — When `python tools/roles/check_roles.py` runs over a scratch copy of the kit in which
  `gov-skeptic.agent.md` carries `subject-reads: input:diff|input:claim`, it exits 1 with an `R3`
  defect naming `input:claim`; with `input:diff|input:diff` it names the doubled member; with
  `input:diff|input:spec` it prints no `R3` defect.
  Red when: the fixture names a role file the merged roster no longer holds, or a doubled member
  passes.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`, built by the pass.
- **AC7** — When `node tools/hooks/scratch-guard.js` reads a `Write` payload for a note x.md under
  `memory/notes/` with `.claude/roles.json` invalid, it exits 0 with no `agent_type` and 2 with
  `agent_type` `gov-tester`; and a payload with no `agent_type` for a path under
  `memory/builds/<slug>/spec/` exits 2 naming the broken index.
  Red when: the main loop's spec write passes on a broken index, or its non-spec write is denied.
- **AC8** — When `python -c` compares the outcome of every triple `roles_lib.derive_return_arms`
  yields over the roles kit's `role-schema.toml` (S13) with the `[return.<name>]` tables declaring
  `outcome`, the two sets are equal and `roles_lib.render_return_schema("gov-builder", [])`'s `anyOf`
  holds one branch more than the set; over a scratch schema whose `[return.refused]` loses `outcome`,
  the compare fails; and `grep -c "establishes:list" .claude/agents/gov-builder.md` prints at least 1
  after `python tools/roles/render_agents.py --write`, or unit 31's ledger answers AC2 AMENDED naming
  `TOOL-dBoundRoles-43`.
  Red when: an arm table that forgets `outcome` passes every assertion.
- **AC9** — When `python -c` calls `roles_lib.derive_attended(root, since=T1)` with
  `PYTHONUTF8` and `PYTHONIOENCODING` removed from its environment, over a stub `breakpoints.py` that
  prints `attendance — ask-live`, its source names no `unread` cause; over a stub that starts a 30-second
  sleeper holding stdout and exits 0, the call returns in under 20 seconds.
  Red when: the em-dash decodes to U+FFFD and a declared posture reads unreadable, or a descendant
  holds the owner question.
  fixture: stub loop files under `%TEMP%`.
- **AC10** — When the card append runs with `CARD_MAP_BOUND=2` and a stub `gov_map.py` that sleeps 120
  seconds, it returns in under 100 seconds and the stored card holds `project-map — unavailable:
  gov_map.py timed out`.
  Red when: the append waits for the sleeper.
  figure: the 100-second verdict is RELATIVE to the 120-second sleeper; PINNED.
- **AC11** — When `python -c` sets `ROLES_SLOT_BOUND=2` before importing `roles_lib` and calls
  `run_slot_reader` with its default bound on a stub that sleeps 30 seconds, the call returns in under
  15 seconds with the `timed out after 2s` answer.
  Red when: a suite's bound arm must sleep past 30 seconds.
- **AC12** — When unit 37 AC12's `awk` probe runs over `tools/unattended/*.sh` but `*.test.sh` with a
  call to `handoff.py ... owner-question` planted in `tools/unattended/lib-unattended.sh` across two
  lines joined by `\`, it prints the joined call; without the plant it prints nothing.
  Red when: a wrapped call that skips `read_owner_door` passes the probe.
- **AC13** — When `python -c` walks `tools/roles/*.py` with `ast` and prints every call whose function
  is an attribute of `subprocess` lying outside the `run_bounded_py` block's line range, it prints
  nothing.
  Red when: the posture read, or any roles subprocess, runs through a runner of its own.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `manifest-check self-test` · `kickoff-manifest ratchet` · `unattended kit gate` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC3 · an empty transcript and unit 16's two-owner, one-keepalive transcript, staged by printing nothing for no event · none
New arm: tools/roles/adopt-roles.test.sh · covers AC4 AC6 AC8 AC9 AC11 AC13 · a planted sibling import, a doubled and a foreign group member, an arm table with no `outcome`, a posture stub under no UTF-8 env and one holding stdout, and a lowered slot bound, staged by restoring the bare `budgets` import · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC7 · a broken index with a main-loop spec write and a main-loop note write, staged by admitting every payload with no `agent_type` · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC10 · a 120-second stub renderer under a 2-second bound, staged by capturing the renderer with `$( )` · none
New arm: tools/unattended/unattended.test.sh · covers AC12 · a wrapped sibling call planted in `lib-unattended.sh`, staged by matching unjoined lines; the suite stays WAIVED at landing by the build README's rule, its arm owed with PLAY-dClosedLoop-18 · none

## 8. Open questions

- **F1 — How many units do the minors take?** RESOLVED (agent, 2026-10-27, delegated): two, by
  `TOOL-dFurnishedOrders-41` §8 F1, rung 1, BUILD-METHOD M4's two-unit clause. widens: none ·
  relaxes: none
- **F2 — How does the roles kit read the policy kit's caps module (S7)?** Options: (a)
  `load_kit_module` with the class import gate; (b) `budgets` admitted as a named exception. (b) lets
  any next sibling import pass. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  skeptic-judged first fix of id 4. widens: none · relaxes: none
- **F3 — How does a suite lower the runner's bound (S17)?** Options: (a) an environment knob read
  once, `CARD_MAP_BOUND`'s pattern; (b) a re-priced budget row. (b) keeps a minute of sleep on every
  bar. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of id 26. widens:
  none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F5 — The units this one lands on are unbuilt.** Units 16, 29, 31, 32, 34, 37, 38 and 39 are
  specced and unbuilt at `08e30fef`, and TOOL-dBoundRoles-5, -13, -26 and -43 are DEFERRED. RESOLVED
  (agent, 2026-10-27, delegated): the build run re-grounds on each at the pass and records any item a
  landed unit already closed, and S8 and S12 take their AMENDED route where a parent is absent, rung
  1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-2 promotions' roles, runlog, hooks,
  unattended and kickoff minors batched: 17 MEDIUM and 2 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: the ratchet's own predicate (`skills/session-kickoff/manifest-check.sh:1525-1534`)
for S2; `load_kit_module` (`TOOL-dFurnishedOrders-29` S6) for S7; `run_slot_reader` and unit 39's
`run_bounded_py` block for S16, S17 and S19; `CARD_MAP_BOUND`'s read-once knob (unit 37 S13) as
the pattern for `ROLES_SLOT_BOUND`; the sleeper-relative verdict of
`skills/session-kickoff/manifest-check.test.sh:1741-1751` for S15. `python
tools/codebase-map/reuse_lookup.py "gate every import of a kit's python files against its own modules
and the standard library"` was run for S7, the one item that builds a new check, and ranked
`resolve_kit_dir`, `kit_rel`, `kit_dir` and `resolve_python`, none an import gate, so the `ast` walk of
§4 is written in the criterion. The recall probe returned KICK-dKeptSession-44, -64 and -65, minors
batches closed after the units they land on, the shape §4 "How an item closes" takes, none
disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the third
dFurnishedOrders spec audit land on the roles runlog and kickoff kits" --terms "minors batch untimed
ratchet watch last-audit miss load_kit_module budgets ROLES_SLOT_BOUND posture encoding"`
