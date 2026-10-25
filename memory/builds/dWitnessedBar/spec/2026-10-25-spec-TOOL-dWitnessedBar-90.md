# TOOL-dWitnessedBar-90 — the round-1 audit of unit 89, 15 minors batched: a canary verdict on every code, the built match on quoted arms, selectors keyed on their unit, criteria that can red and a derivation that names each failure

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 47 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-90-deviation-901.md](../build/2026-10-25-build-TOOL-dWitnessedBar-90-deviation-901.md) | deviation | — |
| [2026-10-25-review-TOOL-dWitnessedBar-90-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-90-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 89
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-89-spec-audit-round1.md`)
exited CONVERGED with 15 confirmed findings, none at BLOCKER or HIGH. BUILD-METHOD M4 batches every
MEDIUM and LOW into one unit, or two only where they split into disjoint write sets by M6's clauses.
§4 "Why one unit" says why these stay one. Each finding is named by report id and is its own scope
item, including where the report merged two ids into one item. Every minor lands on
`TOOL-dWitnessedBar-89`, so this unit repairs unit 89 and builds one step after it (order 47).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 17 | unit 89 S4, AC4 | S1 |
| M2 | MEDIUM | 4 | unit 89 S6, AC6 | S2 |
| M3 | MEDIUM | 18 | unit 89 AC6 | S3 |
| M4 | MEDIUM | 19 | unit 89 S11, AC11 | S4 |
| L1 | LOW | 2 | unit 89 S11, AC11 | S5 |
| L2 | LOW | 1 | unit 89 S11, AC11; unit 87 AC2 | S6 |
| L3 | LOW | 6 | unit 89 AC3 | S7 |
| L3 | LOW | 12 | unit 89 AC3 | S8 |
| L4 | LOW | 7 | unit 89 S1, S4, AC1, AC4 | S9 |
| L5 | LOW | 9 | unit 89 §4 Rollout, §5, AC12 | S10 |
| L6 | LOW | 13 | unit 89 S10 | S11 |
| L7 | LOW | 14 | unit 89 S13, §4 Evidence, AC13, §10 | S12 |
| L8 | LOW | 16 | unit 89 S13, §4 Files touched, AC13 | S13 |
| L9 | LOW | 20 | unit 89 AC7 | S14 |
| L10 | LOW | 21 | unit 89 §4 owner derivation, S12 | S15 |

That is 4 MEDIUM and 11 LOW findings by raw id. Ids 6 and 12 share item L3. Ids 19 and 2 describe one
defect at two binding grades and stand as items M4 and L1.

## 2. Scope (IN)

- **S1** — id 17. The canary's verdict on every code. At the canary's single top-level call of
  `check_canary_keys`, a return of 3 sets `fail=1`. The call site then prints nothing beyond the
  visited line `check_canary_keys` already printed on stderr, and no `TOOL-dWitnessedBar-75` S1 line.
  A return outside 0 to 3 sets `fail=1` and prints
  `gov-canary: check_canary_keys returned <rc>, a code it does not define`. Returns 0, 1 and 2 keep the
  actions units 70, 75 and 84 S13 give them. The liveness loop already requires exactly 1 on each
  variant's mutant (84 S13), so it fails on every other code. Unit 89's ledger beside AC4 records that
  the canary's verdict on 3 is observed by this unit's AC1, and names this unit. Observed by AC1.
- **S2** — id 4. The built match, graded on the quoted spellings. At the close the main loop runs the
  arm in two scratch clones of the built tree. One clone's `.githooks/pre-push` spells the `sha)` arm
  `rec_sha="$_rg_v"`, and the other spells it `rec_sha="${_rg_v}"`. The built liveness loop edits
  each in one line, so neither clone prints `variant changed 0 lines`. With 89 AC6's modifier-arm
  clone and 88 AC10's braced and aligned clones, every spelling 88 S10 lists is then observed through
  the built loop. Unit 89's ledger beside AC6 names this unit. Observed by AC2.
- **S3** — id 18. The probe's arms spelled whole. 89 AC6's first half is graded through this unit's
  AC3, whose seven scratch lines each carry the `sha)` label: `sha) rec_sha=$_rg_v ;;`,
  `sha) rec_sha="$_rg_v" ;;`, `sha) rec_sha=${_rg_v} ;;`, `sha) rec_sha="${_rg_v}" ;;`,
  `sha)   rec_sha=$_rg_v`, and the modifier arms `sha) rec_sha=${_rg_v%$'\r'} ;;` and
  `sha) rec_sha=${_rg_v:-} ;;`. That probe grades 89 S6's match text. S2 grades the built loop.
  Unit 89's ledger beside AC6 records the seven lines' counts. Observed by AC3.
- **S4** — id 19. 89 AC11's selector keyed on the line's own unit. 89 AC11 is graded through this
  unit's AC4. Its selection for the length reason is
  `grep -n 'AC2' <76 ledger> | grep 'TOOL-dWitnessedBar-87' | grep 'rec_fp' | grep 'one byte short'`,
  and it holds exactly one line. The tail reason's selection is the same with `last byte is not CR`.
  The break records `TOOL-dWitnessedBar-81` S4 writes beside the same AC2 carry 81, not 87, and fall
  outside both. Unit 89's ledger beside AC11 names this unit. Observed by AC4.
- **S5** — id 2. Unit 87's statement line outside the selection. The statement `TOOL-dWitnessedBar-87`
  S2 records beside 76 AC2, that 79 S3's length reason and 80 S3's tail reason are what 76 AC2's break
  reaches, cites both reasons by section label and quotes the text of neither. So unit 87's lines
  beside 76 AC2 that quote a reason's text are exactly the two `rec_fp` lines S4 selects. Observed by
  AC5.
- **S6** — id 1. Each reason credited to its own unit alone. The length line S4 selects holds
  `TOOL-dWitnessedBar-79` and not `TOOL-dWitnessedBar-80`. The tail line holds
  `TOOL-dWitnessedBar-80` and not `TOOL-dWitnessedBar-79`. 87 AC2's requirement that both lines hold
  `TOOL-dWitnessedBar-80` is superseded for the length line. Unit 87's ledger beside AC2 records the
  supersession and names this unit. Observed by AC6.
- **S7** — id 6. 89 AC3's fixture clause struck. Its first sentence runs grep over a file the
  criterion itself writes, so no 89 S3 artefact takes part and it cannot red. 89 AC3 is graded by its
  at-close clause alone, which this unit's AC8 runs. Unit 89's ledger beside AC3 records the fixture
  clause as struck and names this unit. Observed by AC7.
- **S8** — id 12. The at-close clause cannot pass on nothing. The glob
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger*` matches exactly
  two ledgers, one each for units 74 and 76. 89 AC3's pipeline runs over each ledger on its own and
  prints at least 2 for each. Every line it selects holds a `uname -s` value beginning `MINGW` or
  `MSYS`, or `owed` with the id of an ask row in `memory/builds/dWitnessedBar/BACKLOG.md`. Observed
  by AC8.
- **S9** — id 7. The must-not-print tokens observed. 89 AC1's clone whose skip sits before the count
  is graded with no line holding `lost its CR`, beside `rec_sha byte check`. 89 AC4's clone whose two
  loops stop after the first pair is graded with no line holding `for unread`, beside
  `could not be sourced or read (rc 2)`. Unit 89's ledger records both readings, each naming this
  unit. Observed by AC9.
- **S10** — id 9. Unit 89's close-time acts, listed whole. 89 S1 to S3 and S5 to S13 write ledger
  lines at the close, and 89 S4 writes none. 89 AC2, AC3, AC5, AC7 to AC9, AC11 and AC13 are graded at
  the close. 89 AC1, AC4, AC6 and AC10 have a probe half at the pass and an arm half at the close. 89
  AC9 is the owner derivation and a ledger grep, both at the close. 89 AC12's ledger half is read at
  the close, as if it carried `permission: the ledger is written at the close.` So at the close
  unit 89's ledger answers every one of its thirteen criteria. Observed by AC10.
- **S11** — id 13. One owner line, its claim stated true. This unit declares a gov-canary arm (§7),
  so `TOOL-dWitnessedBar-88` S6's derivation names it the floor's owner at the close (§8 F2). Its
  builder restates `FLOOR_ASSERTIONS` absolutely, at the count the suite executes on a passing run at
  this pass, by `TOOL-dWitnessedBar-82` S1's counting rule. The one comment line directly above
  `FLOOR_ASSERTIONS=<n>` reads
  `# Raised to <n> by TOOL-dWitnessedBar-90, counting every arm through order 47; stated ABSOLUTELY.`
  That line is the only `Raised` comment the built suite keeps. The two `TOOL-aShardedFloor-2` lines
  at `:92-93` and the `TOOL-dDerivedDocket-23` line at `:95` are not carried into the built file. The
  other floor comments stay: the trailing comment on `:91`, the verdict block at `:377-378` and the
  shard contract's note at `:408`. The assignment carries nothing after the number. Unit 89's ledger
  beside AC10 records that this unit restates the floor after it, and that 89 AC10's owner-line
  clauses were read at 89's pass commit as `build_commit` finds it. It names this unit. Observed by
  AC11.
- **S12** — id 14. The render-freshness seam, named. The renders an ask row moves are held fresh by
  the seam the kits already ship, and this build adds no rule beside it. Hygiene check 9 runs
  `gen_build_index.py --check`, with `--staged` from `.githooks/pre-commit` on any commit touching
  `memory/`. `regen.py --check` runs before the bar's first leg, and its remedy is
  `bash tools/run-gates/run-gates.sh --regen`. The `[[generated]]` rows of
  `tools/memory-tree/kit.toml` declare `memory/LIVE.md` and `memory/backlog`. `GENERATED_INDEXES`
  only adds pairs to those rows, so no `GENERATED_INDEXES` entry names either render. 89 S13's rule
  that a pass's `--writes` declares the renders stands, and so do 89 AC13's id sweep and its line in
  unit 88's ledger. 89 AC13's porcelain clause is read as an observation of check 9's predicate, which
  S13 widens. Unit 89's ledger beside AC13 names check 9, `regen.py --check` and this unit. Observed
  by AC12.
- **S13** — id 16. The write set holds the spec-records regions. `gen_build_index.py --write` also
  rewrites the `gen:spec-records` region of every unit spec. This unit's pass, and each pass 89 S13
  binds, declares `memory/builds/dWitnessedBar/spec/` in its `--writes` beside the three renders and
  commits the regions the run moves. Unit 89's ledger beside AC13 records the widened path and names
  this unit. Observed by AC13.
- **S14** — id 20. 89 AC7's structural clause, non-empty and spelling-proof. 89 AC7's first clause is
  graded through this unit's AC14. The cut of `check_canary_keys` holds its definition line, it holds
  no increment of `a` in any of the forms `a=$((a`, `a++` or `a+=`, and a call of the function leaves
  `a` where it was. The other side of 89 S7's placement, one visited increment at each call site, is
  held by `TOOL-dWitnessedBar-86` AC1's exact difference. Unit 89's ledger beside AC7 names this
  unit. Observed by AC14.
- **S15** — id 21. The owner derivation names each failure. §4's owner derivation takes the place of
  89 §4's. It checks that the cut defined `region` before calling it, and maps only `region`'s exit 3
  to `MALFORMED REGION`. It resolves its interpreter through `tools/lib/resolve-python.sh`, never a
  bare launcher name. Every run of the owner derivation at the close runs this script: 88 S6, AC6
  and AC18, and 89 S9, AC9 and AC12. Unit 89's ledger beside AC12 names this unit. Observed by AC15.

## 3. Non-goals (OUT)

- Rewording the spec text of units 87 and 89. Each item is closed by what this pass builds or
  observes. A claim or criterion it answers is answered in that unit's acceptance ledger by name, as
  `TOOL-dWitnessedBar-89` §3 does for units 84 to 88.
- The left-shift gates the report names: the spec-lint rules for a return code's callers, a fixture
  copied from the spec, a quoted fixture line, a ledger selector's unit and count, a Red-when's
  negative clause, a must-not-print token, a derived Rollout, an "only X" claim, a freshness rule, a
  generator's write set, a "count is 0" criterion and a bare interpreter name. No clause of this
  build names them. S1's verdict, S11's owner line and S15's derivation are the regressions this
  batch builds.
- New assertions in the suite. S1 changes which code fails the canary, and S11 restates the floor
  over the count the suite already executes.
- The liveness loop's own verdict on a code outside 0 to 3. 84 S13 requires exactly 1 there, and
  89 S4 sets `fail=1` on 3.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-82` — S1's counting rule, by which S11 restates the floor under this unit's owner line (id 13)
- **consumes-from** `TOOL-dWitnessedBar-87` — S2's statement and two `rec_fp` lines beside 76 AC2, and AC2's token list, which S5 keeps outside the selection and S6 supersedes for the length line (ids 1 and 2)
- **consumes-from** `TOOL-dWitnessedBar-88` — S6's owner rule, which names this unit the floor's owner, and the owner derivation that S6, AC6 and AC18 run, which S15 makes name each failure (ids 13 and 21)
- **consumes-from** `TOOL-dWitnessedBar-89` — S4's return code 3, S6's match, S7's placement, S10's owner line, S11's attribution, S12's derivation, S13's render rule, §4 Rollout and §5, and AC1, AC3, AC4, AC6, AC7 and AC10 to AC13, which S1 to S15 complete (ids 1, 2, 4, 6, 7, 9, 12, 13, 14, 16, 17, 18, 19, 20 and 21)
- **hands-off** `TOOL-dWitnessedBar-91` — AC2's `rec_sha="` count over the two quoted-arm clones, which unit 91 supersedes with the count anchored on the `sha)` arm, the reader's only-arm check and the resets held at the unedited count (id 1 of the round-1 spec audit of unit 90, item H1)
- **hands-off** `TOOL-dWitnessedBar-92` — AC1's clones and §7's staged red, S3's probe, S10's schedule, S11's keep list, S12's freshness claim, S13's write set, §4's owner derivation, Rollout and Evidence, and the ledger clauses of AC1 to AC4, AC6, AC7 and AC9 to AC15, which unit 92 supersedes or completes (ids 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14 and 16 of the round-1 spec audit of unit 90)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The suite half, S1 and S11,
writes `tools/run-gates/run-gates.gov.test.sh`. The ledger half, S2 to S10 and S12 to S15, records
arm runs and probes over that built suite in the ledgers of units 87 and 89. It reads the suite half's
output as an acceptance input, M6 clause 2: S2's clones and S9's readings run the arm S1 changes, and
S14 cuts the function S1's call site calls. S13 regenerates indexes beside the ledger records, M6
clause 3. No split leaves two disjoint write sets. Dispatch is strictly sequential, a shared order
included (`tools/workflows/unattended-build.js:76`), so a split would buy no concurrency.

### Evidence

- `tools/run-gates/run-gates.gov.test.sh`, read on 2026-10-25: `:91` is
  `a=0  # executed assertions, printed at the end against the pinned floor`, `:92-93` the two
  `TOOL-aShardedFloor-2` lines, `:94` `FLOOR_ASSERTIONS=16`, `:95` the `TOOL-dDerivedDocket-23` line,
  `:377-378` the verdict block's comment holding `a counter and a floor at BIRTH`, and `:408` the
  shard contract's note holding `per-mode assertion floor`. `grep -n -i floor` prints those lines,
  and `:459` fails only when `a` is below the floor. `grep -c Raised` prints 2.
- `check_canary_keys`, its call sites and the liveness loop are not in the tree yet: units 74, 76,
  79, 80, 84 and 89 specify them, and none is built. 84 S13 (spec-84 lines 115-122) gives the
  canary's actions on 1 and 2, and requires exactly 1 from the liveness loop. 89 S4 (spec-89 lines
  68-76) adds 3 and states the liveness loop's action on it, and no canary verdict.
- `TOOL-dWitnessedBar-75` S1 (spec-75 line 35) spells the canary's line
  `... on <uname -s> for <what>; the CR-strip assertion is not counted`, so `for unread` is the
  read-failure slot's token.
- Probed on this node on 2026-10-25 (GNU sed 4.9): 89 S6's match for `sha` with the replacement
  `${_rg_v:1}` changed one line for each of S3's first five lines and none for its two modifier arms,
  each line written to its own scratch file.
- `region()` (`tools/unattended/unattended.sh:1310-1318`) exits 3 only from its END block. Probed on
  2026-10-25 against a scratch copy of the five paths the derivation reads: §4's script printed 27 and
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-89.md` over the live README, `MALFORMED REGION` with exit 3
  with a second `gen:build-units` pair appended, `REGION READER NOT FOUND` with exit 4 with `region()`
  renamed, and `REGION READ FAILED (rc 2)` with exit 6 with the README absent. Once the index is
  re-rendered with this unit, the length reads 28 and the path names this spec. PINNED on
  2026-10-25; 89 S9 re-derives it at the close.
- `resolve_python` (`tools/lib/resolve-python.sh`) runs each candidate and echoes the first that
  exits 0, returning non-zero and leaving the caller to halt when none does.
- Hygiene check 9 (`tools/memory-tree/check-memory-hygiene.sh:1245-1277`) runs
  `gen_build_index.py --check` and fails with `generated build index differs from a fresh render`.
  `.githooks/pre-commit:179-182` runs that hygiene with `--staged` when `memory/` is touched.
  `tools/run-gates/run-gates.sh:1449` runs `regen.py --check`, and `:224` maps `--regen` to
  `regen.py --write`. `tools/memory-tree/kit.toml:473-478` and `:489-495` declare the `[[generated]]`
  rows for `{memory_root}/LIVE.md` and `{memory_root}/backlog`. `tools/unattended/README.md:34` says
  `GENERATED_INDEXES` only adds pairs to these, and `.unattended.conf:418` names neither render.
- `tools/memory-tree/gen_build_index.py:2709-2733` renders the `gen:spec-records` region of every unit
  spec of every build on `--write`. Commit `29ad48729` touched `spec-TOOL-dWitnessedBar-1.md`,
  `-10.md`, `-11.md` and others at that region alone.
- `build_commit` (`tools/unattended/lib-unattended.sh:1186`) answers which commit is a unit's pass.

### The owner derivation

Run as a script with `bash` from the repository root. It prints the New-arm list's length, then the
owner's spec path. Its failures are `MALFORMED REGION` (exit 3), `REGION READER NOT FOUND` (exit 4),
`resolve_python`'s own refusal (exit 5) and `REGION READ FAILED (rc <n>)` (exit 6).

```bash
eval "$(sed -n '/^region() {/,/^}/p' tools/unattended/unattended.sh)"
declare -F region >/dev/null || { echo 'REGION READER NOT FOUND'; exit 4; }
. tools/lib/resolve-python.sh
py=$(resolve_python) || exit 5
b=memory/builds/dWitnessedBar/
r=$(region "${b}README.md" '<!-- gen:build-units -->' '<!-- /gen:build-units -->'); rc=$?
[ "$rc" = 3 ] && { echo 'MALFORMED REGION'; exit 3; }
[ "$rc" = 0 ] || { echo "REGION READ FAILED (rc $rc)"; exit 6; }
printf '%s\n' "$r" | "$py" -c "import sys, importlib.util as u, re; s = u.spec_from_file_location('cst', 'tools/check-spec-tokens.py'); m = u.module_from_spec(s); s.loader.exec_module(m); b = 'memory/builds/dWitnessedBar/'; o = [p for p in re.findall(r'\]\((spec/[^)]+)\)', sys.stdin.read()) if any(l.startswith('New arm: tools/run-gates/run-gates.gov.test.sh') for l in (m.extract_gates(open(b + p, encoding='utf-8').read()) or '').splitlines())]; print(len(o)); print(o[-1] if o else 'NO OWNER')"
```

### Inventory

Minted: the canary call site's line `gov-canary: check_canary_keys returned <rc>, a code it does not
define`; the owner line naming this unit, with the restated `FLOOR_ASSERTIONS`; the derivation's
`REGION READER NOT FOUND` and `REGION READ FAILED (rc <n>)` lines with exits 4 and 6. No function,
plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 47, after every other unit of the build, the last of them
`TOOL-dWitnessedBar-89` at order 46. S1, S3, S11, S14 and S15's probes run at the pass. S2's clones
and S1 and S9's clone readings run at the close. Every ledger line, from S1 to S15, is written at the
close.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/builds/dWitnessedBar/README.md`
- `memory/backlog/TOOL.md`
- `memory/LIVE.md`
- `memory/builds/dWitnessedBar/build/`
- `memory/builds/dWitnessedBar/spec/`

### Alternatives rejected

- **Two batches, suite half and ledger half.** §4 "Why one unit".
- **Cut the canary's call-site block and run it against a stub, the report's first way for id 17.**
  The block has no name a cut can anchor on, so the probe would need a minted function or marker that
  exists only for the probe. §8 F3.
- **Cut the sed expression out of the built suite, the report's first way for id 4.** The built
  match is composed from `<key>` and `<var>` at run time, so its spelling in the file is not the
  expression sed runs. The clones grade the loop's behaviour instead.
- **Drop 89 AC13's porcelain clause, id 14's option.** Id 16's fix widens the same clause. Read as
  check 9's predicate over `memory/`, it answers both. §8 F4.

## 5. Production-readiness checklist

- security — no new write path. The scratch clones sit under `%TEMP%`.
- perf / scale — none: S1 adds two `case` arms, and the close's clones run once.
- error / empty / loading states — S1 fails the canary on every code but 0; S14 refuses an empty cut;
  S15 gives a missing reader, a malformed region and an unreadable README three distinct lines.
- observability — S1's undefined-code line names the code; S11's owner line names its unit.
- risks — a builder who prints S1's undefined-code line on stdout of `check_canary_keys` rather than
  at the call site puts it into the captured output; AC1's second clone still reds on the exit.
  S14's increment grep reads three spellings, and the call probe reads the value of `a` itself.
- testing — AC3, AC14 and AC15 by probe or fixture at the pass; AC11's file reads at the pass; AC1,
  AC2 and AC9 by scratch clone at the close; AC13 after the pass commit; the rest by ledger at the
  close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone of the built tree whose canary's top-level call of `check_canary_keys`
  runs with `_iso=1` set for that call alone, and whose `check_canary_keys` stops after its first pair
  when `_iso` is set, the arm prints a line holding `the canary visited 1 of 2`, no line holding
  `liveness loop visited` and no line holding `for unread`, and exits non-zero. In a second such clone
  whose `check_canary_keys` returns 7 with empty output when `_iso` is set, the arm prints a line
  holding `check_canary_keys returned 7` and exits non-zero. When
  `grep -n 'AC4' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a canary call site whose `case` handles 0, 1 and 2 alone passes on a visited failure.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: the `2` is the number of words in `${CANARY_KEYS[*]}`, DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — In each of two scratch clones of the built tree, one whose `.githooks/pre-push` spells the
  `sha)` arm `rec_sha="$_rg_v"` and one spelling it `rec_sha="${_rg_v}"`, `grep -c 'rec_sha="'`
  over the clone's hook prints 1, and the arm prints no line holding `variant changed 0 lines` and
  no line holding `visited`. When
  `grep -n 'AC6' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line naming `rec_sha="${_rg_v}"` and `TOOL-dWitnessedBar-90`.
  Red when: a built match that lost its optional quotes stalls the liveness loop on a quoted arm.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When a probe writes each of S3's seven lines to its own scratch file and applies 89 S6's
  match for `sha` with the replacement `${_rg_v:1}` through `sed`, `grep -c 'sha)'` prints 1 for each
  file, and `diff` counts one changed line for each of the first five and none for each modifier arm.
  When `grep -n 'AC6' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*`
  runs at the close, it prints a line holding `sha)` and `TOOL-dWitnessedBar-90`.
  Red when: a match whose quotes or braces are independently optional changes a modifier arm, or a
  fixture line without `sha)` counts 0 where 1 is owed.
  fixture: scratch files under the run's scratch directory.
- **AC4** — When
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger* | grep 'TOOL-dWitnessedBar-87' | grep 'rec_fp' | grep -c 'one byte short'`
  runs at the close it prints 1, and that line holds `TOOL-dWitnessedBar-79`. The same pipeline
  ending `grep -c 'last byte is not CR'` prints 1, and that line holds `TOOL-dWitnessedBar-80`. When
  `grep -n 'AC11' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs,
  it prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a correct build reds because unit 81's records sit in the selection, or a misattributed
  unit-87 line hides behind another.
  permission: the ledgers are written at the close.
- **AC5** — When
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger* | grep 'TOOL-dWitnessedBar-87' | grep -cE 'one byte short|last byte is not CR'`
  runs at the close, it prints 2.
  Red when: unit 87's statement line quotes a reason's text and doubles a selection.
  permission: the ledger is written at the close.
- **AC6** — At the close, the line AC4's length pipeline selects holds no `TOOL-dWitnessedBar-80`, and
  the line its tail pipeline selects holds no `TOOL-dWitnessedBar-79`. When
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-87*acceptance-ledger*` runs, it
  prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a length line naming both 79 and 80, which 87 AC2 and 89 AC11 both pass, credits the
  length reason to unit 80.
  permission: the ledgers are written at the close.
- **AC7** — When
  `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line holding `struck` and `TOOL-dWitnessedBar-90`, and no line answering 89
  AC3 cites the fixture clause's count as an observation.
  Red when: the ledger counts a grep over a hand-written file as an observation of 89 S3.
  permission: the ledger is written at the close.
- **AC8** — At the close,
  `ls memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger* | wc -l` prints 2.
  For each of those files, `grep 'TOOL-dWitnessedBar-81' <file> | grep -c 'break:'` prints at least 2,
  and every line it selects holds a `uname -s` value beginning `MINGW` or `MSYS`, or `owed` with the
  id of an ask row in `memory/builds/dWitnessedBar/BACKLOG.md`.
  Red when: a missing ledger, or one whose selection is empty, passes the at-close clause.
  permission: the ledgers are written at the close.
- **AC9** — In 89 AC1's scratch clone whose skip sits before the count, the arm's output holds no
  line holding `lost its CR` or `rec_sha byte check`. In 89 AC4's scratch clone whose two loops stop
  after the first pair, it holds no line holding `for unread` or `could not be sourced or read (rc 2)`.
  When `grep -n 'lost its CR' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*`
  and the same with `for unread` run at the close, each prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a canary that routes a visited failure to the `unread` slot passes 89 AC4.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC10** — When, at the close, for each `n` from 1 to 13,
  `grep -cE "^- AC${n} " memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*`
  runs, it prints at least 1, and the line answering AC12 names `TOOL-dWitnessedBar-90`.
  Red when: a close-time act 89's Rollout omitted leaves one of its criteria unanswered.
  figure: 13 is PINNED, the criteria 89 §6 numbers at rev-1.
  permission: the ledger is written at the close.
- **AC11** — On the built tree, `grep -c 'Raised' tools/run-gates/run-gates.gov.test.sh` prints 1, and
  the line number `grep -n 'Raised'` prints is one less than the one `grep -n '^FLOOR_ASSERTIONS='`
  prints. `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` names
  `TOOL-dWitnessedBar-90` and no other unit id, and
  `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$' tools/run-gates/run-gates.gov.test.sh` prints 1. Each of
  `grep -c 'printed at the end against the pinned floor'`, `grep -c 'a counter and a floor at BIRTH'`
  and `grep -c 'per-mode assertion floor'` over the suite prints 1. At the close the arm prints
  `PASS (<n> assertions)` with `<n>` equal to the value, and
  `grep -n 'build_commit' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*`
  prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a builder reading "the only floor comment" deletes the verdict block's provenance, or a
  stale owner line survives beside the restated value.
  figure: the floor and `<n>` are DERIVED at observation time; `grep -c 'Raised'` prints 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC12** — At the close, `grep '^GENERATED_INDEXES=' .unattended.conf` holds neither
  `memory/LIVE.md` nor `memory/backlog`, and
  `grep -n 'regen.py --check' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*`
  prints a line holding `check 9` and `TOOL-dWitnessedBar-90`.
  Red when: a builder answers the evidence bullet with a second declaration over renders the kit
  already declares.
  permission: the ledger is written at the close.
- **AC13** — After this unit's pass commit, `python tools/memory-tree/gen_build_index.py --write`
  leaves `git status --porcelain --untracked-files=no -- memory/` empty. When
  `grep -n 'AC13' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line naming `memory/builds/dWitnessedBar/spec/` and `TOOL-dWitnessedBar-90`.
  Red when: a moved spec-records region stays uncommitted while the three-path porcelain reads clean.
  permission: the ledger is written at the close.
- **AC14** — On the built tree,
  `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh | grep -c '^check_canary_keys()'`
  prints 1, and the same cut piped to `grep -cE '\ba(=\$\(\(a|\+\+|\+=)'` prints 0. When a probe
  sources the cut functions as 89 AC4 does, sets `a=0`, and calls
  `check_canary_keys <file> <record> >out 2>err` with no command substitution, once with
  `CANARY_KEYS` emptied and once as defined, `echo "$a"` prints 0 after each call. When
  `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: an empty cut, or an increment spelled `((a++))` or `: $((a+=1))`, passes the count of 0.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC15** — When §4's owner derivation runs on the built tree, it prints a non-zero length and a
  spec path. In a scratch copy holding `tools/unattended/unattended.sh`, `tools/lib/resolve-python.sh`,
  `tools/check-spec-tokens.py` and `memory/builds/dWitnessedBar/`, it prints `MALFORMED REGION` and
  exits 3 with a second `gen:build-units` pair appended to the README, `REGION READER NOT FOUND` and
  exits 4 with `region()` renamed, and `REGION READ FAILED (rc 2)` and exits 6 with the README absent.
  `sed -n '/^### The owner derivation/,/^### Inventory/p'` over this spec piped to
  `grep -cE 'python3? -c'` prints 0. When
  `grep -n 'AC12' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89*acceptance-ledger*` runs at
  the close, it prints a line naming `TOOL-dWitnessedBar-90`.
  Red when: a dead reader or a missing README reads as a malformed index.
  fixture: a scratch copy under the run's scratch directory.

## 7. Gates

`run-gates gov canary` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close, which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf:40`). `testsuite counts (every bar self-test
prints one)` reads the assignment line S11 writes. `recall floor` and `recall floor arms` are owed for
the paths under `memory/`.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 · the canary call site's verdict on a visited failure and on a code it does not define, and the built match on quoted arms, staged red by a scratch suite whose canary call site handles 0, 1 and 2 alone (the isolated clone ends `PASS (`) and by a match whose quotes are not optional (a quoted hook arm reaches `variant changed 0 lines`) · FLOOR_ASSERTIONS restated absolutely by S11, its owner this unit

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Unit 89 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-89` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Does this unit declare a gov-canary arm, and so own the floor (ids 13 and 17)?** Options:
  (a) yes: it declares a `New arm:` line, restates the floor and writes the one owner line under the
  narrowed claim; (b) no: unit 89 stays the owner, and S1's changed call site rides under 89's arm.
  Under (b) S1's failure route lands with no RED-first observation at the close, and id 13's claim
  stays on a line this unit does not write. (a) observes the route and closes id 13 at the line it
  writes. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor, as
  `TOOL-dWitnessedBar-89` §8 F4 ruled for its own arm.
  widens: none · relaxes: none
- **F3 — How is the canary's call site isolated (id 17)?** Options: (a) the report's second way, a
  clone whose `check_canary_keys` stops early only under a variable the canary's call alone sets;
  (b) its first way, the call-site block cut and run against a stub. (b) needs a name a cut can anchor
  on, a function or marker minted only for the probe, which the charter's YAGNI rule refuses. (a)
  needs nothing in the built file. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one
  survivor.
  widens: none · relaxes: none
- **F4 — What becomes of 89 AC13's porcelain clause (ids 14 and 16)?** Options: (a) keep it, widened
  to `memory/` and read as check 9's predicate; (b) strike it, id 14's option. (b) leaves id 16's
  widened write set with no observation. (a) satisfies both fixes. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 89: 4 MEDIUM and
  11 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-91 and TOOL-dWitnessedBar-92, promoted by the round-1 spec audit of
  unit 90; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names. S1 extends the canary's call site and 89 S4's return
code. S2 and S9 reuse the scratch-clone arm runs of 88 AC10 and 89 AC1, AC4 and AC6. S11 follows
`TOOL-dWitnessedBar-82` S1's rule. S12 names the existing render-freshness seam: hygiene check 9
(`tools/memory-tree/check-memory-hygiene.sh:1245`), `regen.py --check` (`tools/run-gates/run-gates.sh:1449`)
and the `[[generated]]` rows of `tools/memory-tree/kit.toml`, so this build adds no freshness rule of
its own. S15 keeps `region` (`tools/unattended/unattended.sh:1310`) and adopts `resolve_python`
(`tools/lib/resolve-python.sh`), the one interpreter resolver.
`python tools/codebase-map/reuse_lookup.py "report a failure distinctly when a sourced shell function is missing or a slice reader exits non-zero"`
ranked `read`, `read_text`, `report` and `slice`, none of them a reader that tells a missing function
from a malformed slice, so no existing seam fits beyond `region`, `resolve_python` and the seams named
above. The ledger items use the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger".

Recall terms used: `python tools/memory-recall/query.py "how does a canary call site fail when a checker function returns a code it does not define" --terms "canary call site return code fail visited count isolate clone stub floor owner"`
