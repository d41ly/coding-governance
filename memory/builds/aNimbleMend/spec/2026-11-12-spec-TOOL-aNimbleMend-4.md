# TOOL-aNimbleMend-4 — the scoped legs: three manifest rows a pass can afford, for memory hygiene's pass checks, the positional check alone and the spec tokens of the pass's own spec

**Status:** INPROGRESS · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-4-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-4-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Three legs that red mid-build cost too much to run after a pass: `memory hygiene`,
`tags (the resolver's checks)` and `spec tokens (a spec's own names resolve)`. Each has a cheap
form that grades what a pass can break. This unit makes each form a leg of its own, gives it a
cost and a red count the derivation can read, and re-derives the declared list over them.

## 2. Scope (IN)

- **S1** — Three rows in `tools/gate-legs.json`, as §4, "The rows", spells them. Each carries a new
  key, `scope_of`, naming the leg it is a form of. Observed by AC1.
- **S2** — A flag on `tools/check-spec-tokens.py`, `--pass-spec [<range>]`, that grades the spec of
  the newest unit the range's commits name, as `--spec` grades a named one. Observed by AC2, AC3,
  AC4 and AC5.
- **S3** — In `tools/run-gates/pass_legs.py`, which TOOL-aNimbleMend-2 ships, `--write` credits a
  row carrying `scope_of` with the reds of the leg it names, added to its own. That is how each new
  leg enters `pass-leg-evidence.txt`. A `scope_of` naming no manifest row refuses. Observed by AC6.
- **S4** — The rows gov's own registries owe a new leg, for each of the three: an `[[exempt_leg]]`
  row in `tools/govkit/registry.toml`, a row in `tools/govkit/subject-pins.tsv`, the leg's name in
  the `gate-legs` list of its feature dossier's front matter, a `leg` row in
  `tools/playbook/core-pending.txt`, and `scope_of` in both pinned key sets of the manifest canary.
  Observed by AC7.
- **S5** — A row in `tools/run-gates/ceiling-evidence.txt` for each new leg and for
  `writing practice (records and units)`, the leg that holds the pinned-facts arm. Each is written
  by `derive-ceilings.py --write --observed` from a reading of the leg alone. Observed by AC8.
- **S6** — The declaration re-derived over the manifest that holds the new rows, by
  `pass_legs.py --write` on node `a`, and committed as whatever the rule yields. Observed by AC9.

## 3. Non-goals (OUT)

- A leg for pinned facts. `writing practice (records and units)` already runs that arm with three
  others, and its last run cost `12.7 s` (PINNED, the dOrderedCharter worktree's ledger, 2026-11-12).
  It lacks only a cost row, which S5 gives it.
- Typing `pass_leg` onto any row. The rule of TOOL-aNimbleMend-2 selects, and S6 runs it.
- Holding the new rows off the bar. They run on every bar as any unguarded row does (§4, "What the
  rows cost the bar").
- A `[[gate_leg]]` descriptor row. The selection of S1 is sized against gov's corpus, so an adopter
  receives none of the three, by the class `memory/gotchas/pin-copied-from-another-corpus.md` names.
- A scoped form of `govkit acceptance matrix`, `routed commits name a specced unit`,
  `pass-order history`, `straggler-guard arms`, `brief-recorded` or `unattended kit gate`. §4,
  "The slow legs", states each exclusion.
- Any change to `tools/memory-tree/check-memory-hygiene.sh`, `tools/playbook/positional.py` or the
  bar runner. Each scoped form but one is an argv that exists today.
- The help page, which is TOOL-aNimbleMend-11's, and the kit version, which the lander's `mint`
  moves.

### Edges

- **consumes-from** `TOOL-aNimbleMend-2` — `pass_legs.py`, its `--write` verb and
  `pass-leg-evidence.txt`. Without them S3 has no reader to extend and S6 has no rule to run.
- **consumes-from** external — a bar run log on node `a`, which `--write` distils; the linked
  worktree reaches it through the common directory.

## 4. Design

### Evidence

Read at 97e0841d. The readings are this writer's, taken on node `a` on 2026-11-12 while sibling
writers ran gates beside them. They decide the selection and are no evidence rows: S5's are.

| Command | Wall | Note |
|---|---|---|
| `check-memory-hygiene.sh --only 9,12,21,23,25` | `393 s` | PINNED; the prompt's five checks |
| `check-memory-hygiene.sh --only 12,25` | `351 s` | PINNED; spec format and retirement readers |
| `check-memory-hygiene.sh --only 9,21,23` | `78 s` | PINNED; index drift, record bindings, closed-unit evidence |
| `check-spec-tokens.py --spec <one spec>` | `2 s` | PINNED; a sibling spec of this build |

- **`--staged` grades nothing after a commit.** It takes its set from `git diff --cached`, which is
  empty once the pass has committed, and the pre-commit hook already ran it on that commit's
  content (`.githooks/pre-commit`, the three `--staged` calls). So the pass form is `--only`.
- **`--only` runs alone.** `tools/memory-tree/check-memory-hygiene.sh#check_selected` selects the
  blocks, and the script refuses `--only` beside any other argument. Checks 12 and 25 share one
  block.
- **Positional runs alone today.** `tools/playbook/positional.py#run_check` is the `positional` arm
  of the tags leg, reached by `positional.py check`. No row runs it alone, and the tags leg's cost
  row is `210.0 s` (PINNED, `tools/run-gates/ceiling-evidence.txt`, dated 2026-11-10).
- **The pass's unit is already derivable.** `tools/memory-tree/routed_commits.py#read_newest_unit`
  returns the newest unit id a range's commits name that a spec at HEAD defines, reading the
  subject and the `Pass:` trailer. `tools/memory-tree/routed_commits.py#load_spec_paths` maps an id
  to its spec by the H1.
- **A leg inherits `GATE_BASE`.** TOOL-aNimbleMend-5's adapter sets it to the pass's base and the
  runner does not clear it before a leg starts (that spec's §4, "Evidence").
- **A new leg with no `enforces` needs a pending row.** `tools/playbook/core-pending.txt` holds one
  `leg` row per such leg, arming build `dWitnessedBar`. The hygiene and spec-token parents each
  have one; the tags parent carries `enforces` in its place.

### The rows

| `name` | `argv` | `chunk` | `scope_of` | `reads` |
|---|---|---|---|---|
| `memory hygiene (the pass checks)` | `bash {prefix}/memory-tree/check-memory-hygiene.sh --only 9,21,23` | `records` | `memory hygiene` | `base`, `clock`, `history` |
| `positional (the citation check alone)` | `python {prefix}/playbook/positional.py check` | `declarations` | `tags (the resolver's checks)` | `history` |
| `spec tokens (the pass's own spec)` | `python {prefix}/check-spec-tokens.py --pass-spec` | `declarations` | `spec tokens (a spec's own names resolve)` | `history` |

Each row has `subject` `repo`, `ceiling` 300 and no `guard`. Each `reads` class carries a one-line
reason, as the parent rows' do: the hygiene row copies its parent's three, the positional check
reads `git blame`, and `--pass-spec` reads `git log`. A ceiling of 300 clears any reading up to
`150 s` under `tools/run-gates/ceiling-margin.txt` (DERIVED, reading plus the larger of the floor
and the reading).

### The flag (S2)

```
python <prefix>/check-spec-tokens.py --pass-spec [<range>]
```

The range is the operand when one is given, else `$GATE_BASE..HEAD` when `GATE_BASE` is set and not
empty, else `HEAD~1..HEAD`. The new function `read_pass_spec` resolves both ends, asks
`read_newest_unit` for the unit and `load_spec_paths` for its spec, loading the memory-tree kit's
module by path as the checker already loads `design_lib.py`. It prints one line, naming the range
as asked and not as resolved, then grades:

```
spec-tokens: --pass-spec · <range> · <unit id> · <spec path>
spec-tokens: --pass-spec · <range> · names no specced unit · 0 spec(s) graded
```

On the first form the spec is handed to the `--spec` path, `tools/check-spec-tokens.py#read_named_specs`
onward, so every join `--spec` runs is run and the exit is its exit. On the second the exit is 0. A
range that does not resolve, or `--pass-spec` beside `--spec` or `--legs-for`, prints a
`spec-tokens: REFUSING` line and exits 2.

### The credit (S3)

`--write` counts reds per leg name from the bar run log. After that count, each manifest row
carrying `scope_of` gains the count of the leg it names. A row with a credited count above zero
gets an evidence row like any other, with `-` for its last seconds until it has a ledger row. The
new function is `read_scope_reds`. The tracked verbs read the evidence file and change nowhere.

This is the answer TOOL-aNimbleMend-2 leaves to this unit. The owner asks for each form because its
parent redded, so the parent's count is the form's reason to run.

### What the rows cost the bar

The three rows run on every bar, beside their parents, for their own seconds. No hold exists for a
row that is neither a kit self-test nor a suite, and adding one edits the runner's hold predicate,
its three spellings and every reader of a held leg. On a bar, `--pass-spec` grades the newest unit
of the last commit, or prints the zero line.

### What it does not check

- A form's credited reds overstate it. The hygiene parent's count includes reds of checks 12 and
  25, which the form does not run.
- The pass form of memory hygiene never runs checks 12 and 25. A spec-format red a pass causes is
  seen at its own pre-commit hook for the staged files, and otherwise at the close's bar.
- `--pass-spec` grades one spec. A pass that breaks a sibling's token is seen at the close's bar.
- `--pass-spec` grades a spec at any status, as `--spec` does. A frozen spec named by the last
  commit can red on a path a later unit moved.
- The rule may still leave a form out when the budget is full. That is its verdict.

### The slow legs

| Leg | Why no pass | Scoped form |
|---|---|---|
| `memory hygiene` | last run `632.7 s` (PINNED, the primary checkout's ledger, 2026-11-12) | S1's first row |
| `tags (the resolver's checks)` | cost row `210.0 s` (PINNED, the ceiling evidence) | S1's second row |
| `spec tokens (a spec's own names resolve)` | cost row `465.2 s` (PINNED, the ceiling evidence) | S1's third row |
| `govkit acceptance matrix` | cost row `218.8 s` (PINNED, the ceiling evidence) | none: it drives the deployer against whole repository shapes |
| `routed commits name a specced unit` | cost row `378.7 s` (PINNED, the ceiling evidence) | none here: its range form reads `GATE_PUSH_BASE`, a push hook's variable |
| `pass-order history` | cost row `1053.6 s` (PINNED, the ceiling evidence) | none: it is a check of the commit graph |
| `brief-recorded` | cost row `403.5 s` (PINNED, the ceiling evidence) | none found |
| `straggler-guard arms` | `184 s` in the owner's prompt (PINNED there), no cost row | none: a suite of arms |
| `unattended kit gate` | held, and excluded by the owner's rule | none |

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the manifest key `scope_of` | `tools/gate-legs.json`, the canary's two `KNOWN` literals | the snake spelling of `doc_reads` |
| the flag `--pass-spec` | `tools/check-spec-tokens.py` | no cell grades a flag |
| `read_pass_spec`, `read_scope_reds` | the checker, `pass_legs.py` | `py.function`; `lexicon.py --suggest` answered OK for both on 2026-11-12 |
| the three leg names of "The rows" | the manifest and the five registries of S4 | no cell grades a leg name |

### Migration

Additive. A manifest row without `scope_of` reads as before.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/run-gates/pass_legs.py`
- `tools/run-gates/pass-leg-evidence.txt`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/playbook/core-pending.txt`
- `memory/map/features/memory-tree-hygiene.md`
- `memory/map/features/playbook.md`
- `memory/map/features/spec-tokens.md`
- `memory/map/generated/`

### Alternatives rejected

- **A pass argv on the parent's row.** One leg would then carry two costs, and the ceiling evidence
  keys one figure per leg name; `tools/run-gates/derive-ceilings.py#parse_observed` refuses a name
  the manifest lacks. TOOL-aNimbleMend-6 also reads a scoped leg as a manifest row.
- **`--only 9,12,21,23,25`.** `393 s` (PINNED, §4 "Evidence") is over any cap F1 of
  TOOL-aNimbleMend-2 offers.
- **A range form of `--staged`.** It re-grades what the pre-commit hook graded on the same commit.
- **The pass's spec handed in by the runner.** The adapter would need a per-leg argument, and the
  commit subject already names the unit.
- **The new legs wait for a red of their own.** They are undeclared until a bar reds one, which is
  the delay the owner asks to remove.

## 5. Production-readiness checklist

- security — no write path beyond tracked tool files. The range reaches `git rev-parse` as one
  argument and is never evaluated; a leg name from `scope_of` is compared with manifest names only.
- perf / scale — the three forms' readings are in §4, "Evidence"; S5 records each as a cost row.
- error / empty / loading states — a range naming no specced unit prints the zero line and exits 0;
  an unresolvable range and an unknown `scope_of` refuse with exit 2.
- observability — the `--pass-spec` line names the range, the unit and the spec on every run.
- risks — a reading in S5 above the cap leaves that row undeclarable, which F1 and F2 decide before
  code. A reading above `60 s` (DERIVED from its 180 ceiling and the margin's floor) for the
  writing-practice leg reds its ceiling unless the ceiling rises in the same commit.
- testing — AC1 to AC7 are probes and fixtures a pass runs. AC8 and AC9 are the main loop's.
- migration — additive; see §4, "Migration".
- user docs — the pass-leg help page is TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

`<kit>` is the run-gates kit directory: `tools/run-gates` in this repository, and its copy in a
fixture.

- **AC1** — When `python -c "import json,sys;[print(l['name'],'|',' '.join(l['argv']),'|',l['chunk'],l['subject'],l['ceiling'],'|',l['scope_of'],'|',','.join(sorted(l['reads']))) for l in json.load(sys.stdin.buffer) if 'scope_of' in l]" < tools/gate-legs.json`
  runs, it prints three lines whose fields equal the table of §4, "The rows", with `repo` and 300.
  Red when: a row is absent, or its argv is not the form the table names. At base it prints nothing.
- **AC2** — When `python tools/check-spec-tokens.py --pass-spec 6fbf4a9b7~1..6fbf4a9b7` runs, its
  output holds one line opening `spec-tokens: --pass-spec ·` that names `PLAY-dOrderedCharter-88` and
  that unit's spec path, and one line opening `spec-tokens: --spec · 1 named spec(s) graded`.
  Red when: the flag grades the whole corpus, or names no unit for a commit whose subject names one.
- **AC3** — When `python tools/check-spec-tokens.py --pass-spec 1265772cc~1..1265772cc` runs, it
  prints a line ending `names no specced unit · 0 spec(s) graded` and exits 0.
  Red when: a commit naming no unit refuses, or grades a spec the range never named.
- **AC4** — When `python tools/check-spec-tokens.py --pass-spec no-such-rev..HEAD` runs, and again
  with `--pass-spec` beside `--spec`, each prints a `spec-tokens: REFUSING` line and exits 2.
  Red when: an unresolvable range falls back to another range and grades something.
- **AC5** — When `GATE_BASE=6fbf4a9b7 python tools/check-spec-tokens.py --pass-spec` runs, its
  `--pass-spec` line names the range `6fbf4a9b7..HEAD`.
  Red when: the inherited base is not read, which prints `HEAD~1..HEAD`.
- **AC6** — When `GOV_NODE=f python <kit>/pass_legs.py --write` runs in fixture F of
  TOOL-aNimbleMend-2's §6 with one added row, `s-form`, that carries `"scope_of": "b-mid"`, has a
  cost row of 10.0 and is named by no run-log line, the evidence file holds `s-form` with 5 reds
  and `--report` reads it `selected`. With `scope_of` set to a name no row carries, `--write`
  exits 2 and `git status --porcelain` is unmoved.
  Red when: the credit is absent, which leaves `s-form` with no evidence row and reads it `no-red`.
  figure: 5 is PINNED in that fixture's table, the reds of `b-mid`.
  fixture: a scratch repository under `%TEMP%`; the tree holds no such fixture today.
- **AC7** — When `python tools/run-gates/owed_rows.py --base <the pass's starting tip>` runs, it
  prints no line opening `owed —`, and
  `grep -cE "^leg.(memory hygiene \(the pass checks\)|positional \(the citation check alone\)|spec tokens \(the pass's own spec\))." tools/playbook/core-pending.txt`
  prints 3.
  Red when: a pin, an exempt row, a dossier name, a key of `KNOWN` or a pending row is missing.
- **AC8** — When `grep -cE "^(memory hygiene \(the pass checks\)|positional \(the citation check alone\)|spec tokens \(the pass's own spec\)|writing practice \(records and units\))" tools/run-gates/ceiling-evidence.txt`
  runs after S5, it prints 4, and no such row's sixth field reads `runner`.
  Red when: a cost row was typed, or a form was declared with no reading behind it.
  permission: the main loop takes the four readings; a role agent's hook refuses a leg's command.
  cost: the four legs run once each, alone.
- **AC9** — When `python <kit>/pass_legs.py --report` runs after S6, the line of each of
  the three new legs carries a verdict other than `no-red` and `unevidenced`, and
  `python <kit>/pass_legs.py --check` exits 0.
  Red when: S6 did not run, so the manifest's fields predate the new rows.
  fixture: needs node `a`'s bar run log; the tree holds it today.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `memory-hygiene self-test` · `build-index selftest` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `govkit selfcheck` · `core meta-check` · `spec-tokens self-test` · `leg ceilings clear their evidenced maximum` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first twelve are what the guards join owes the paths of §4's estimate, by the checker's
`--legs-for` at 97e0841d with broad guards set aside. `govkit selfcheck` and `core meta-check`
grade the rows of S4, the ceilings leg grades the rows of S5, and the map leg grades the dossier
names. The close's bar also runs the three new legs themselves, which is their first run there.

New arm: tools/check-spec-tokens.test.sh · covers AC2 AC3 AC4 AC5 · a fixture repository whose last commit names a specced unit, staged with the unit lookup removed so the flag grades the corpus · `FLOOR_ASSERTIONS`, raised by the arms added

New arm: tools/run-gates/run-gates.test.sh · covers AC1 · a control manifest whose row carries `scope_of` must pass, staged with `scope_of` taken back out of one `KNOWN` literal · none

## 8. Open questions

- **FACT-QUESTION · F1 — Does `--only 9,21,23` fit the per-leg cap?** The cap is
  `PASS_LEG_CAP_SECONDS`, which F1 of TOOL-aNimbleMend-2 decides. Probe: the main loop times
  `bash tools/memory-tree/check-memory-hygiene.sh --only 9,21,23` alone on node `a`. Observation:
  the wall time at or under the cap keeps the row as written; above it, check 9 leaves the
  selection and the probe repeats on `--only 21,23`. Liveness: the probe can answer no, as
  `--only 12,25` did at `351 s` (PINNED, §4 "Evidence"). This writer's reading is `78 s` (PINNED,
  the same table), so the recommendation is the row as written at a cap of 120 or more.
  RESOLVED (agent, 2026-11-12, delegated): the row stands as written. The main loop timed `--only 9,21,23` alone on node a at 66 s on 2026-11-12, under the cap of 120.
- **FACT-QUESTION · F2 — Does the positional check alone fit the per-leg cap?** No reading of it
  alone exists, and a role agent's hook refuses the command. Probe: the main loop times
  `python tools/playbook/positional.py check` alone on node `a`. Observation: at or under the cap,
  the second row of S1 stands; above it, that row and its registry rows leave this spec by a
  revision, and "The slow legs" states the exclusion. Liveness: the whole tags leg reads `210.0 s`
  (PINNED, the ceiling evidence), so a reading above the cap is possible. Recommendation: keep the
  row if the reading fits.
  RESOLVED (agent, 2026-11-12, delegated): the positional row stands. The main loop timed the positional check alone on node a at 29 s on 2026-11-12, under the cap of 120.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

Every form but one is an argv that exists: `--only` in `check-memory-hygiene.sh`, the `check` verb
of `positional.py`, and the `--spec` path of `check-spec-tokens.py`, which `--pass-spec` reaches
after one lookup. That lookup is `read_newest_unit` and `load_spec_paths` in
`tools/memory-tree/routed_commits.py`, the seam the lander's mint already uses to name a range's
unit. `python tools/codebase-map/reuse_lookup.py "a cheap scoped form of a slow gate leg that grades
only selected checks or one named spec"` ranked name-stem neighbours, `read_spec_revisions` and
`parse_spec_h1` among them, and none selects a leg's form, so the seams were read from the four
sources. For crediting a new leg with another leg's reds, no existing seam fits: the red count is
first built by TOOL-aNimbleMend-2, and S3 extends that reader. Recall returned
`TOOL-dWitnessedBar-10`, a deferred design for a per-row commit-time argv with no built seam, which
"Alternatives rejected" answers. `gotchas.py --for-paths` over the estimate selected
`a-new-leg-trips-a-growing-set-of-meta-gates`, which S4 answers row by row, and
`criterion-asserts-what-its-own-command-cannot-show`, which is why AC1 prints each field it grades.

Where the records and the source disagreed: the prompt offers `--staged` as a pass form, and after
a commit that form grades an empty set.

Recall terms used: `python tools/memory-recall/query.py "which gate legs are cheap enough to run
after every pass, and how is a leg's evidenced wall time budgeted" --terms "pass leg budget ceiling
evidence evidenced maximum derive-ceilings scoped --only --staged spec tokens --spec hygiene"`
