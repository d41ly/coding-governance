# TOOL-dScopedBuild-12 — `build.reuse-check`: the reuse scout over the units a unit's commits add, before the closing review

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 13 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0410@869f06dd whole
**Carries:** node:item.build.reuse-check
**Carries:** node:policy-key.build.reuse-check.second-pass

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md](../build/2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md) | research | TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 |
| [2026-11-01-build-TOOL-dScopedBuild-12-deviation-121.md](../build/2026-11-01-build-TOOL-dScopedBuild-12-deviation-121.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

No diff-time reuse check runs in the flow (gap-build-06,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:367`): the measured
two-stage shape's second stage, which took aScoutedSeam's system to 33 of 35, has no item, the diff
preset has no reuse lens (`DIFF_LENSES`, `tools/workflows/tier2-review.template.js:774`), and the diff
reviewer reads only the diff and the spec. This unit builds `build.reuse-check`: per unit, before the
closing review, the reuse scout at medium answers one closed-vocabulary row for each unit the unit's
commits add, listed from the code record and capped at sixty with an overflow line, plus added rows,
a no-stop line and one row per MUST seam the unit's spec carried; a `duplicate` or `bypassed` row
routes to a fix pass, a disputed row goes to the closing review, re-entries stop at
`flow.route-backs`, a second independent pass runs as `build.reuse-check.second-pass` says, and the
whole is accepted by reproducing aScoutedSeam's measured figures through gov's own route.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced at HEAD and each a build
this one descends from: the code record `tools/memory-tree/code_record.py` and its `--dump --tree
<rev>` rows (TOOL-dTotalRecall-8 S2, S7; dTotalRecall is a parent of dIndexedDesign, README
`parents:` line); `join_upstream(rows, answers, gate)` and the answer grammar
`used|bypassed|not-applicable` (TOOL-dDeclaredLoop-29 S5, S6); `count_returns` and
`promotion_target` with the draw rows `verb_dispatch` writes (TOOL-dDeclaredLoop-30 S3, S4, S6); the
`--fix-of reuse-check` value (TOOL-dScopedBuild-15, I17, over TOOL-dWitnessedBar-21 S3); the ask
route `derive_ask_seq` and `write_ask_rows` as TOOL-dScopedBuild-11 makes `--propose` their third
caller (I20); the `scouted-seam` grader instance (TOOL-dFairHearing-12 S4) and the experiment
method (TOOL-dFairHearing-14) for S11. Where the code record is absent the lister says so (S1).

- **S1** — The lister. `map_diff.py --added-units <base>..<head>` in
  `tools/codebase-map/map_diff.py`, spelled and ruled exactly as TOOL-aScoutedSeam-3 S8 specs it,
  so one lister serves both builds: `extract_units` and `render_units` ported from
  `memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py:44-91`, the
  header `# added-units <base>..<head> · <n> found`, one `U<i>. <name>  [<kind> · <path>]` line per
  unit up to `UNIT_CAP = 60`, then the overflow sentence of `d1v2.py:88-89`. This unit adds the code
  record to it: where `code_record.py` is installed, each definition its `--dump` rows hold at
  `<head>` and not at `<base>` that the diff patterns missed is appended as a `def` unit, and a listed
  unit the record holds carries the record's kind; where it is not, one line
  `# code record: not-installed — <why>` follows the header. Observed by AC1 and AC2.
- **S2** — The unit's own commits. `reuse_check.py` in `tools/codebase-map/` lists over the union of
  each non-merge commit whose subject or `Pass:` trailer names the unit, read through
  `routed_commits.extract_unit_ids` (`tools/memory-tree/routed_commits.py:119`, I8's union rule), each
  diffed against its parent and fed to `extract_units` in commit order, deduplicated by path and
  name. A unit id is unique in the tree, so no base bounds the walk. Observed by AC3.
- **S3** — The MUST rows (I15). `read_spec_musts(spec_text)` in `tools/memory-tree/design_lib.py`,
  beside `read_spec_writes` (`:528`), returns `[(row id, path, symbol)]` for each line of the spec's
  `## 10. Reuse audit` reading `- seam-<n> · seam · <path> :: <symbol> · MUST`, in order; a `SHOULD`
  line is not returned, so a bypassed SHOULD opens no fix pass (scout D disagreement 4). The line is
  TOOL-dDeclaredLoop-29 S3's row with the binding the seams record's match carries
  (TOOL-dIndexedDesign-13 S3) as its last field. `memory/TEMPLATE-SPEC.md`'s §10 section gains one
  paragraph stating the line, edited in its kit template. Observed by AC4.
- **S4** — The question. `python reuse_check.py question <slug> <unit id> [--from <k>]` prints the
  task the scout answers, its sentences ported from `render_question` (`d1v2.py:94-126`) with gov's
  tree in place of the case trees: a header `# reuse-check <unit id> · pass <p> of <n> · from U<k>`,
  `<n>` being 2 under `build.reuse-check.second-pass: on` and 1 under `off`, read as
  `policy.py get build.reuse-check.second-pass` (I4); the lister's output from `U<k>`; the row
  vocabulary `duplicate`, `should-extend`, `new`, `not-a-unit`, each row with its nearest existing
  `path::symbol` or `none` with what was searched; the added-rows instruction; the no-stop sentence
  of `d1v2.py:120`; one `- seam-<n> · seam · <path> :: <symbol>` row per S3 MUST under a row
  contract answering each exactly once `used`, `bypassed` or `not-applicable`; and the return
  contract, a JSON block of `rows`, `seams`, `verdict` and `upstream`. The form `question --diff
  <file> --spec <file>` renders the same task over a foreign diff and spec, the route S11 measures.
  Observed by AC5 and AC6.
- **S5** — The join. `check_reuse_rows(units, musts, replies, disputes)` in `reuse_check.py`, the
  computed join of `flow-steps.md:294`: every listed unit from `U<k>` to the cap has exactly one row
  per reply, each verdict one of the four; every MUST is joined through `join_upstream` at gate
  `record`; a `bypassed` MUST is also a `duplicate` row whose nearest names that seam, else the finding
  `bypassed-without-duplicate`. Its verdict is `fix` on any `duplicate` or `bypassed` row not disputed,
  `incomplete` on a listed unit with no row or a bad verdict, `overflow` when units remain past the
  cap, else `clean`. Observed by AC6, AC7 and AC8.
- **S6** — The record (I16). `python reuse_check.py join <slug> <unit id> --reply <file>
  [--reply <file>] [--from <k>] --write` writes
  `memory/builds/<slug>/build/<date>-build-<unit id>-reuse-check-<n>.md`, opening
  `**Serves:** journal <unit id>`, then `**Head:** <sha>`, `**Pass:** <p> of <n> · from U<k> · listed
  <m> · cap 60`, `## Verdict: <verdict>`, and the sections `## Rows`, `## MUST` and `## Disputed`, a
  row line `- U<i> · <verdict> · <path>::<symbol> or none — <searched> · <why>`, an added row's id
  `A<i>`. It exits 0 on `clean`, 1 on any other verdict, 2 on a reply it cannot parse. Observed by
  AC6 and AC7.
- **S7** — The second pass. Under `build.reuse-check.second-pass: on`, `join` refuses one reply,
  naming the key and the value, and unions two: a unit's row set is every distinct verdict either pass
  gave it, so a `duplicate` either pass found routes to the fix pass. Under `off` it refuses a second
  reply the same way. Observed by AC9.
- **S8** — The routes. A `fix` verdict routes the unit to `build.fix-pass` through `--dispatch <slug>
  --pass <unit id> --fix-of reuse-check` (I17). The fix pass may dispute a row by a trailer line
  `Disputed: <path>::<name> — <reason>` in its commit; the next `join` reads every such trailer of the
  unit's commits, records the row under `## Disputed` with its reason, and no longer counts it toward
  `fix`, so the row goes to the closing review (TOOL-dScopedBuild-13 reads it through
  `read_reuse_records(root, slug, unit)`). `python reuse_check.py bound <slug> <unit id>` exits 1,
  printing the newest record's open rows, once `count_returns(build, "item.build.reuse-check")`
  exceeds `flow.route-backs`, read as `policy.py get flow.route-backs` (I4); `--dispatch --fix-of
  reuse-check` calls it first, and on exit 1 refuses, the loop ending non-converging, and files the
  open rows as one ask through `derive_ask_seq` and `write_ask_rows`
  (`tools/unattended/unattended.sh:9780`, `:9984`), as `promotion_target` answers `ask` for this
  non-blocking item. Observed by AC10 and AC11.
- **S9** — The overflow. An `overflow` record is never `clean`. `python reuse_check.py status <slug>`
  prints one line per roster unit, `reuse-check · <unit id> · clean|fix|overflow|incomplete|none`,
  reading the unit's records at its newest `**Head:**`: clean only when those records cover U1 to
  `listed` contiguously and each is `clean`, an `overflow` record's remainder taken by a further pass
  `--from <k + 60>`. It exits 1 when any unit is not clean. Observed by AC7 and AC12.
- **S10** — Where it runs. `tools/workflows/unattended-unit.js` takes the optional argument
  `reuseCheck: { question: <command> }`; after a committed build pass it spawns `gov-reuse-scout`
  (its effort the type's own, `medium` from `tools/roles/house/policy.toml:6`), told to run the
  command and answer the task it prints, and returns `reuse: [<reply>]`, spawning a second
  independent scout when the first reply's header said `of 2`. The build harness's dispatch row
  (`tools/workflows/unattended-build.template.js:2471-2491`) passes the command and tells the main
  loop to run `join --write` and commit the record after each unit's call. `verb_review`, on a round
  whose subject is the build slug, refuses while `reuse_check.py status` names a unit not clean, found
  beside `MAP_CLI` as `unattended.sh:10551-10559` finds `map_diff.py`, and prints `reuse-check
  not-installed` where it is absent. The attended Skill's closing-review stage
  (`tools/roles/SKILL.template.md:74`) runs `status` first. Observed by AC12 and AC13.
- **S11** — The acceptance measurement. The reproduction of aScoutedSeam's figures through gov's own
  route, on its 23 tuning and 12 held-out cases: the orientation arm is gov's reuse scout under
  TOOL-dIndexedDesign-13's contract, its MUSTs written as S3 lines into a scratch spec per case, and the
  check is `question --diff --spec`, the scout at medium, the replies parsed and counted first, then
  joined by S5 and graded blind by the `scouted-seam` instance. Bars: at least 29 of 35 for the check
  with the card and at least 31 of 35 for the system, the measured 31 and 33 less the stated noise of
  2 (`memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-3-1-system-and-held-out.md:82-83`,
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-scoutedseam-apply.md:177`).
  The record is `memory/builds/dScopedBuild/build/2026-11-01-build-TOOL-dScopedBuild-12-reproduction.md`.
  Observed by AC14.
- **S12** — The key's catalogue row. `build.reuse-check.second-pass` at `tools/policy/catalogue.toml:986`
  gains `summary` and `usage`, its allowed values `off`, `on` and default `off` unchanged, and
  `policy.py lists --write` re-renders `tools/policy/unsummarised-keys.txt` without it. The literal
  reader is S4's call. Observed by AC15.
- **S13** — The docs: `tools/codebase-map/README.md` documents `--added-units` and `reuse_check.py`,
  and `help/roles.md`'s "How to use it" names the reuse check between a unit's build and the closing
  review. Observed by AC16.

## 3. Non-goals (OUT)

- No second lister and no edit of TOOL-aScoutedSeam-3: its S8 spelling is the one this unit builds,
  and its harness `reuse-scout.js` diff mode is that build's, met here by an ask (§8 F2).
- No reuse lens in `DIFF_LENSES`: NT-11 placed the check as a Build item before the closing review,
  not as a lens of it (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:609`).
- No effort pin and no effort floor: the scout runs at its type's resolved effort, `medium` at base;
  the floor below medium is NT-12's, another build's.
- No arming of the reuse edge at `measured` in `tools/loop/loop.toml`: the measurement record S11
  writes is what an owner or a later unit cites as `measured-by` (TOOL-dDeclaredLoop-29 §3).
- No `build.fix-pass` item, keeps or red value: TOOL-dScopedBuild-15 carries the node and I17.
- No `item.build.unit-lease` wait on a dependency's clean check (`flow-steps.md:288`): TOOL-dScopedBuild-5
  carries the lease.
- The closing review's rows: TOOL-dScopedBuild-13 hands the disputed rows and the MUST rows on.

### Edges

- **consumes-from** `TOOL-dScopedBuild-15` — `--fix-of` with its `reuse-check` value, the dispatch a `duplicate` or `bypassed` row routes to; without it a `fix` verdict has no pass to open
- **consumes-from** `TOOL-dScopedBuild-11` — `write_ask_rows`, as `--propose`'s third caller makes it the shared ask filer; without it the open rows past `flow.route-backs` have no ask route but a second writer
- **hands-off** `TOOL-dScopedBuild-13` — `read_spec_musts`, the one MUST-seam reader, and `read_reuse_records`, whose `## Disputed` rows the closing review is handed
- **consumes-from** external — TOOL-dTotalRecall-8 (the code record), TOOL-dDeclaredLoop-29 S5, S6 (`join_upstream`), TOOL-dDeclaredLoop-30 S3, S4, S6 (`count_returns`, `promotion_target`), TOOL-dFairHearing-12 S4 and -14 (the grader and the method), all specced and DEFERRED at base
- **hands-off** external — the arming of the reuse edge at `measured`, citing S11's record, and the reconciliation of TOOL-aScoutedSeam-3 with this unit (§8 F2)
- **hands-off** `TOOL-dScopedBuild-26` — S4's, S7's and S8's two policy reads in `reuse_check.py`, and AC11's and AC15's grep clauses, which that unit reads through the memory-tree adapter and supersedes (id 2)
- **hands-off** `TOOL-dScopedBuild-35` — the new leg's map claim, S15, and S9's status for a stale head and a never-built unit, S29 (ids 31, 47)

## 4. Design

### The flow

```
unit's last pass committed
  -> unattended-unit.js reuse stage: gov-reuse-scout runs `reuse_check.py question <slug> <unit>`
     and replies (twice under second-pass: on)
  -> main loop: `reuse_check.py join <slug> <unit> --reply r1 [--reply r2] --write`, commits the record
       clean       -> the unit is checked
       fix         -> --dispatch --fix-of reuse-check; the fix pass may write `Disputed:` trailers;
                      then the check again (a re-entry, drawn by verb_dispatch)
       overflow    -> question --from <k+60>, a further pass over the remainder
       incomplete  -> the check again, the same pass
  -> past flow.route-backs: the dispatch refuses and files the open rows as one ask
  -> closing review: verb_review on the slug subject refuses while `status` names a unit not clean
```

### The reply

The scout's reply ends with one fenced JSON object, the measured return contract
(`d1v2.py:121-125`) plus the MUST answers:

```json
{"rows": [{"unit": "U1", "nearest": "tools/a.py::f", "verdict": "duplicate", "why": "...", "added": false}],
 "seams": [{"path": "tools/a.py", "symbol": "f", "binding": "MUST", "how": "...", "evidence": "tools/a.py:12"}],
 "verdict": "duplicates-found",
 "upstream": [{"id": "seam-1", "answer": "used", "reason": "calls it at b.py:40"}]}
```

`read_reuse_replies(path)` takes the last fenced `json` block; a reply with none, or with `rows` not a
list, is unparseable and exits 2, and S11 counts it as unparsed before scoring.

### The record

```
# TOOL-dScopedBuild-3 reuse check 2

**Serves:** journal TOOL-dScopedBuild-3
**Head:** 5f0b11f12
**Pass:** 1 of 1 · from U1 · listed 61 · cap 60

## Verdict: overflow

## Rows
- U1 · new · none — searched "scope report", "write set match" · a new grader
- U2 · duplicate · tools/memory-tree/design_lib.py::check_guard_trips · the same path match
- A1 · duplicate · tools/lib/compare_base.py::read_compare_base · a copied base reader (added)

## MUST
- seam-1 · used · check_writes_intersect called at routed_commits.py:410

## Disputed
- tools/memory-tree/routed_commits.py::check_scope · the nearest grades a pass, not a push (fix pass 1a2b3c4)
```

`read_reuse_records(root, slug, unit)` returns each record's head, pass fields, verdict and the three
sections parsed, newest last; `status` and TOOL-dScopedBuild-13 read records only through it.

### The spec's MUST lines

The seams record's `## Matches` carries the binding, MUST or SHOULD, and its `## Establishes` rows do
not (TOOL-dIndexedDesign-13 S3, S6). A spec carries a MUST by copying the row with its binding into
§10, the line `- seam-<n> · seam · <path> :: <symbol> · MUST`. The TEMPLATE-SPEC paragraph states
that line and that the reuse check answers every MUST line, nothing else. A spec carrying no line
hands no MUST rows, and the question says `0 MUST rows: the spec's §10 carries no seam line`, so the
absence is printed, never silent.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `extract_units`, `render_units` (ported) | functions, `map_diff.py` | `py.function`, `--suggest` OK |
| `--added-units` | `map_diff.py` CLI mode | none |
| `read_spec_musts` | function, `design_lib.py` | `py.function`, `--suggest` OK |
| `render_question`, `read_reuse_replies`, `check_reuse_rows`, `write_reuse_record`, `read_reuse_records` | functions, `reuse_check.py` | `py.function`, `--suggest` OK |
| `question`, `join`, `status`, `bound`, `--fixture` | `reuse_check.py` CLI modes | none |
| `UNIT_CAP` | constant, 60, PINNED from `d1v2.py:37` | none declared |
| `reuseCheck`, `reuse` | `unattended-unit.js` argument and return field | none |
| `Disputed:` | commit trailer | none |
| `reuse-check` | journal record tail | none |
| `codebase-map reuse-check fixtures` | gate leg, `tools/codebase-map/kit.toml` | none |

### Migration

None. A build whose harness passes no `reuseCheck` runs as before; `verb_review` refuses only where
`reuse_check.py` is found beside `MAP_CLI`.

### Rollout

Live at landing for every build whose closing round is recorded after it. An open build at landing
whose units have no record is refused at its closing round until each unit is checked, which is the
clause's intent.

### Files touched (estimate)

- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/reuse_check.py` (new)
- `tools/codebase-map/kit.toml`: the module and the leg `codebase-map reuse-check fixtures`
- `tools/gate-legs.json`: rendered from the kits' declarations
- `tools/codebase-map/README.md`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, rendered to `memory/TEMPLATE-SPEC.md`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.template.js`, rendered to `tools/workflows/unattended-build.js`
- `tools/unattended/unattended.sh`: the `verb_review` guard and the `--fix-of reuse-check` bound
- `tools/unattended/unattended.test.sh`
- `tools/policy/catalogue.toml`, and `tools/policy/unsummarised-keys.txt` by `lists --write`
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `help/roles.md`

S11's instruments and record are build records under `memory/builds/dScopedBuild/build/`, named in
§6, never product paths.

### Alternatives rejected

- **Listing from `memory/map/generated/symbols.json` as the code record's stand-in.** Rejected by
  reading it: its rows are `{id, kind, file}` only, in four kinds (`tools/codebase-map/map_lib.py:313`,
  `:1599-1616`), with no line, so it holds none of the `hunk`, `css-prop`, `css-rule`, `json-key` and
  `constant` units the measured lister found, and the 35 host trees carry no map at all (scout D
  disagreements 1, 2). The code record itself is a precondition, not a stand-in.
- **Listing from the code record alone.** Rejected by the same reading of `extract_units`
  (`d1v2.py:44-82`): the measured figures were made by a diff lister, and a record of definitions
  cannot list logic added inside an existing function. Recorded as deviation 121.
- **A reuse lens in the closing review's panel.** NT-11's second option; the owner chose the Build
  item (`night-pass-two.md:609`).
- **Counting re-entries from the record count.** It would hold a second count beside the draw rows
  TOOL-dDeclaredLoop-30 S4 already writes at `verb_dispatch`; `count_returns` reads those.

## 5. Production-readiness checklist

- security: the scout writes nothing (`tools/roles/agents/gov-reuse-scout.agent.md`, `writes: none`);
  the reply is parsed as JSON and its strings are written into a markdown record only after each
  field is checked against its closed set or path shape, so a reply cannot forge a `## Verdict` line.
- perf / scale: one scout per unit at medium, two under `on`; the lister is one `git show` per unit
  commit. A unit of sixty-one units costs one further pass.
- error / empty / loading states: an unparseable reply exits 2; zero listed units prints the lister's
  sentence and the scout enumerates; no code record prints `not-installed`; no MUST lines prints the
  zero line.
- observability: every pass leaves a record; `status` prints one line per unit; the guard's refusal
  names each unit not clean.
- risks: the reproduction runs on the host holding the case trees only (§6 AC14); a scout reply that
  drifts from the vocabulary is `incomplete`, never `clean`.
- testing: `reuse_check.py --fixture` plants each case of §6; the driver arms in
  `tools/unattended/unattended.test.sh`; the reproduction is S11.
- migration: none (§4).
- user docs: `help/roles.md` and the map kit's README (S13).

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/map_diff.py --added-units <base>..<head>` runs over a
  fixture range adding a function, a CSS custom property in a `.css` file and a five-line hunk inside an
  existing function, it prints the header and three `U<i>.` lines with kinds `def`, `css-prop` and
  `hunk`; over a range git cannot read it exits 1 and prints no header.
  Red when: the hunk is not listed, or an unreadable range prints an empty list.
  fixture: `reuse_check.py --fixture` builds the repository under `%TEMP%`.
- **AC2** — When `python reuse_check.py --fixture --plant code-record` runs with a planted code record
  holding a definition the diff patterns miss, the list carries it as a `def` unit; with the record
  absent it prints `# code record: not-installed` and the diff units alone.
  Red when: the record is silently ignored, or its absence lists nothing.
- **AC3** — When `python reuse_check.py --fixture --plant own-commits` lists a unit whose two commits
  are separated by another unit's commit, it lists the two commits' units and none of the other's.
  Red when: the lister reads `<base>..<head>` and lists the other unit's code.
- **AC4** — When `read_spec_musts` reads a §10 holding one `MUST` line, one `SHOULD` line and one
  `seam-<n>` line with no binding, it returns the MUST alone.
  Red when: the SHOULD is returned, so a bypassed SHOULD opens a fix pass.
- **AC5** — When `python reuse_check.py question <slug> <unit>` runs in the fixture with no policy
  file, the header reads `pass 1 of 1`; after a committed `.governance/policy.toml` sets
  `build.reuse-check.second-pass` to `on`, it reads `pass 1 of 2`; the task names the four verdicts,
  the no-stop sentence and one row per MUST.
  Red when: the header ignores the key, or the no-stop sentence is absent.
- **AC6** — When `python reuse_check.py --fixture --plant false-duplicate` runs, a first reply marking
  a `new` unit `duplicate` writes a record whose verdict is `fix`; after a fix-pass commit carrying
  `Disputed: <path>::<name> — <reason>`, the next `join` writes `## Verdict: clean` with the row under
  `## Disputed` and its reason.
  Red when: the disputed row opens a second fix pass, or is dropped from the record.
- **AC7** — When `python reuse_check.py --fixture --plant overflow-61` lists sixty-one added units
  whose last duplicates an existing function, and the first reply answers U1 to U60 `new`, the record's
  verdict is `overflow` and `status` prints the unit not clean; the further pass `--from 61` lists U61,
  its `duplicate` row writes `fix`.
  Red when: the first pass reads `clean` with U61 unread.
- **AC8** — When `--plant dropped-unit`, `--plant bad-verdict` and `--plant bypassed-alone` each run
  through `reuse_check.py --fixture`, the first writes `incomplete` naming the U-number with no row, the
  second `incomplete` naming the verdict outside the four, and the third, a `bypassed` MUST with no
  `duplicate` row on its seam, prints `bypassed-without-duplicate` and writes `fix`.
  Red when: a missing row or a fifth verdict reads `clean`.
- **AC9** — When `python reuse_check.py --fixture --plant second-pass` joins one reply under a committed
  policy value `on`, it exits 2 naming `build.reuse-check.second-pass` and `on`; two replies, only the
  second finding a `duplicate`, write `fix`; under `off`, two replies exit 2 naming `off`.
  Red when: `on` accepts one pass, or the union keeps only the first reply's row.
- **AC10** — When `bash unattended.sh --dispatch tRun --pass TOOL-tRun-1 --writes a.py --fix-of
  reuse-check` runs in a preflighted fixture whose draw rows count four returns of
  `item.build.reuse-check` under the default `flow.route-backs` of 3, it refuses and files one ask
  naming the open rows through `write_ask_rows`; at two returns it admits the pass.
  Red when: the dispatch admits a fifth lap, or files the ask through a second writer.
  fixture: the driver suite's preflighted slug fixture with the policy kit beside it.
- **AC11** — When `python reuse_check.py join` reads a reply answering one `duplicate` row, the record
  is written and the exit is 1; `python reuse_check.py bound` over the fixture's four drawn returns
  exits 1 printing the open row, and `git grep -c 'get flow.route-backs' -- tools/codebase-map/`
  prints at least 1.
  Red when: a `duplicate` exits 0, or the bound has no literal reader.
- **AC12** — When `bash unattended.sh --review tRun --subject tRun --verdict CLEAN --blockers 0`
  runs in the fixture while one roster unit's newest record is `overflow`, it refuses naming that unit
  and `reuse-check`; once every unit reads clean it records the round; with `MAP_CLI` blank it prints
  `reuse-check not-installed` and records.
  Red when: a closing round is recorded over a unit whose check never read clean.
  fixture: as AC10.
- **AC13** — When a `node -e` probe evaluates `unattended-unit.js` with a stub `agent` that records
  each spawn and `reuseCheck` set, the stub sees one `gov-reuse-scout` spawn after the builder, and a
  second when the first reply's header says `of 2`; without `reuseCheck` it sees the builder alone.
  Red when: the stage runs with no `reuseCheck`, or `on` spawns once.
- **AC14** — When `2026-11-01-build-TOOL-dScopedBuild-12-reproduction.md` is read, it counts parsed
  replies per arm before any score, and reports the check with the card at 29 or more of 35 and the
  system at 31 or more of 35 over the 23 tuning and 12 held-out cases, each case's judge blind with
  labels rotated.
  Red when: either figure falls below its bar, or a score is read before the parsed count.
  cost: about 105 agents, 35 orientation scouts, 35 checks and 35 judges, five at once.
  permission: the measurement spawns agents through a `Workflow` script, which a pass's role may not.
  fixture: the case trees under `C:/Users/daily-agent/AppData/Local/Temp/rsd`, `rsb` and `rsh`,
  untracked, present on this host on 2026-11-01; the case files are tracked under
  `memory/builds/aScoutedSeam/build/`.
  figure: PINNED bars, 29 and 31, from the measured 31 and 33 less 2; the reached figures DERIVED at
  the run.
- **AC15** — When `python tools/policy/policy.py get build.reuse-check.second-pass` runs with no policy
  file, it prints `off`; after `policy.py lists --write`, `grep -c build.reuse-check.second-pass
  tools/policy/unsummarised-keys.txt` prints 0; `git grep -c 'get build.reuse-check.second-pass'
  -- tools/codebase-map/` prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.
- **AC16** — When `grep -n "added-units" tools/codebase-map/README.md` and `grep -n "reuse check"
  help/roles.md` run, each prints the sentence S13 names.
  Red when: the mode ships undocumented.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit selftest` · `kit/dogfood doc parity` · `measure-legs selftest` · `policy fixtures` · `policy check` · `recall floor` · `recall floor arms` · `review-join self-test` · `run-gates canary` · `run-gates gov canary` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `check-wiring self-test` · `lexicon naming predicates` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/codebase-map/reuse_check.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC11 · the leg `codebase-map reuse-check fixtures`, `reuse_check.py --fixture` over every plant of §6, staged by deleting the overflow test in `check_reuse_rows` · none

New arm: tools/unattended/unattended.test.sh · covers AC10 AC12 · the fixture dispatch past `flow.route-backs` and the closing round over an overflow record, staged by removing the `verb_review` guard · none

New arm: tools/workflows/unattended-build.test.sh · covers AC13 · the stubbed `agent` run of `unattended-unit.js` with `reuseCheck`, staged by spawning the second scout unconditionally · none

## 8. Open questions

- **F1 — What does the lister read: the code record, the diff, or both?** Options: (a) the code record
  alone, as the clause words it; (b) the ported diff lister alone, the measured instrument; (c) the diff
  lister with the code record's added definitions joined to it. (a) loses the measured `hunk`, CSS and
  JSON units and cannot run over the 35 host trees, so AC14 cannot pass; (b) reads no code record, so
  it fails the clause's text. RESOLVED (agent, 2026-11-01, delegated): (c), rung 3, the most
  feature-rich option, the code record listing what it holds and the diff the rest the clause's "added rows for what the lister cannot see" would otherwise leave to the scout; recorded as deviation 121 (additive). widens: none · relaxes: none
- **F2 — How does this unit meet TOOL-aScoutedSeam-3, a ratified, unbuilt spec of the same diff check?**
  Options: (a) build its lister under its S8 spelling and ask aScoutedSeam to retire its unit 3 as
  carried here, or rebase it on this unit's join; (b) build a second lister under a new name; (c) wait
  for aScoutedSeam to build first. (b) is two copies of one mechanism and (c) parks on a build outside
  the chain. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, tie-broken by reuse of the seam M5
  found, with an ask for the main loop to file once, target aScoutedSeam's `BACKLOG.md`: "THE CHAIN'S
  BUILD.REUSE-CHECK AND TOOL-aScoutedSeam-3 ARE ONE DIFF CHECK. TOOL-dScopedBuild-12 builds `map_diff.py
  --added-units` under TOOL-aScoutedSeam-3 S8's spelling and its own question, join and record in
  `reuse_check.py`, and TOOL-aScoutedSeam-3 specs `reuse-scout.js` diff mode over the same lister", accept
  "TOOL-aScoutedSeam-3 is retired as carried by TOOL-dScopedBuild-12, or revised to call its lister and
  `check_reuse_rows` rather than a second join, seen as one diff-check route in the tree". widens: none · relaxes: none
- **F3 — Where does a spec carry its MUST seams?** Options: (a) a §10 line with the binding as its last
  field, read by `read_spec_musts`, stated in TEMPLATE-SPEC; (b) the same line, its grammar only in the
  reader's docstring; (c) no spec line, the seams record serving the unit read directly. (b) leaves a
  spec writer to learn the line from an empty row set, the defect ask PLAY-dClosedLoop-22 names for the
  binding lines; (c) fails the clause's "the MUST seams the unit's spec carried", and no parent spec
  defines the carrying (scout C disagreement 6). RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  the template edit a governance-carrier change the clause names. grants: PLAY-dClosedLoop-3 TEMPLATE-SPEC §10 states the MUST seam line. widens: none · relaxes: none
- **F4 — Where is the fix pass's dispute written?** Options: (a) a `Disputed:` trailer on the fix-pass
  commit, read by the next `join`; (b) a verb rewriting the previous record; (c) a field in the next
  scout's reply. (b) rewrites a committed record and (c) lets the checker dispute itself, when
  `flow-steps.md:294` gives the dispute to the fix pass. RESOLVED (agent, 2026-11-01, delegated): (a),
  rung 1, the flow row's own route, written where this repo already writes a pass's choices, a commit
  trailer. widens: none · relaxes: none
- **F5 — Is the per-unit guard placed at the closing round or earlier?** Options: (a) `verb_review`
  refusing a closing round while a unit is not clean, with the attended Skill's stage running `status`
  first; (b) a new DoD term at `--close`. (b) lets a closing review run and land its findings over
  unchecked units, which the clause's "before the closing review" forbids. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 12, v2:1298 and :1984, flow-steps:288-294,
  night-pass-two:189-193 and :609-611, research-scoutedseam-apply:166-192, gap-register:367, scout D's
  row 12 and its disagreements 1, 2, 4 to 7, and the spec brief's I15, I16, I17 and I20.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-26, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are `map_diff.py` (`tools/codebase-map/map_diff.py`, its CLI at `:230-247` gaining
the `--added-units` mode TOOL-aScoutedSeam-3 S8 specs), `design_lib.read_spec_writes`
(`tools/memory-tree/design_lib.py:528`), beside which `read_spec_musts` sits, `routed_commits.extract_unit_ids`
(`tools/memory-tree/routed_commits.py:119`), the ask filer `derive_ask_seq` and `write_ask_rows`
(`tools/unattended/unattended.sh:9780`, `:9984`), the derived map-kit reader beside `MAP_CLI`
(`:10551-10559`), the unit harness's single `agent` call (`tools/workflows/unattended-unit.js:333`) and
the `gov-reuse-scout` role as it stands, whose task block may override its pointer
(`tools/roles/agents/gov-reuse-scout.agent.md`). `python tools/codebase-map/reuse_lookup.py "list the
units a diff adds and ask a reviewer for one closed verdict row per unit"` scanned every layer and
ranked name-token helpers (`rows`, `units`, `extract_row`, `parse_verdicts`); none lists added units or
joins verdict rows, so the join is new and its lister is ported. The recall probe surfaced
TOOL-aScoutedSeam-3, a ratified spec of the same diff check, which §8 F2 reconciles; scout D's rows
hold against source at `5f0b11f12`, and its symbols.json path is corrected in §4.

Recall terms used: `python tools/memory-recall/query.py "how is a diff-time reuse check of a unit's added code run and graded before the closing review" --terms "reuse scout diff check duplicate should-extend MUST seam card rows overflow aScoutedSeam"`
