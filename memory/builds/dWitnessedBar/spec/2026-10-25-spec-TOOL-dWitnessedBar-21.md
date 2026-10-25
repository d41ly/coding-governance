# TOOL-dWitnessedBar-21 — a fix pass that keeps its check: its allowance less the red leg's own files and the acceptance commands' own files

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 27 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0359@5c408077 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md](../build/2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

A fix pass may edit the check that reds it: nothing keeps a red leg's own test files or gate script
out of the pass's write set (gap-test-19). A re-dispatch is an ordinary `--dispatch`
(`tools/unattended/unattended.sh:13584`), and `--writes` refuses only shape, the run-state file and
shared records (`:13800-13850`). This unit declares a fix pass against the red it fixes, subtracts the
red check's own files from its allowance at `--dispatch --writes` and at `--check-commit`, and routes a
change to those files through the tester's `spec-wrong` judgment to Design as a new unit; a fix pass
after a failed acceptance leaves the acceptance commands' own files alone (night pass, point 6; M16).

## 2. Scope (IN)

- **S1** — The red leg's own files (shared interface I15), `read_leg_files(rows, name, tool_root,
  tracked)` in `tools/unattended/fix_keeps.py`: the words of the leg's `argv` in
  `tools/gate-legs.json`, `{prefix}` resolved to the tool root, that carry a `/`, no whitespace, and
  name a tracked file, the census shape of `tools/run-gates/run-gates.sh:3026-3027` without its
  extension filter; the gate script is the first such word. An unknown leg name is a refusal naming
  it. Observed by AC1.
- **S2** — The acceptance commands' own files, `read_acceptance_files(spec_text, tracked)` in the same
  module: every word of a backticked token in the spec's acceptance-criteria section that names a
  tracked file, by path or by a basename unique among tracked files, and that is a check file:
  `*.test.sh`, a name ending `selftest.py`, `test_*.py`, or a path under a `fixtures/` directory
  (§8 F2). Observed by AC2.
- **S3** — The declaration: `--dispatch <slug> --pass <id> --writes <path>… --fix-of <red>`, `<red>`
  one of `leg:<leg name>` or `acceptance`. The driver computes the keeps through
  `python fix_keeps.py --keeps <red> [--spec <path>]` and refuses, with code 49, every `--writes` path that
  covers or is covered by a kept file, naming the path, the red and the route of S5. On success it
  records one run-state row `<ts> fix-of · item <grp> <unit> · reason <red>` through `park()`, and
  `fix-of` joins `PARK_KINDS` (`tools/unattended/unattended.sh:875`). Observed by AC3 and AC4.
- **S4** — The commit check: `check_commit_message` (`unattended.sh:13475`), for an open pass whose
  key holds a `fix-of` row, re-derives the keeps and refuses a staged path among them, code 49, with
  S5's route; a later `--dispatch` of that key without `--fix-of` is held to the same keeps. A
  `--no-verify` commit that writes a kept file falls outside the declared set, so check 23 refuses it
  at the close as code 49 does today. Observed by AC5.
- **S5** — The route, one sentence both refusals print: a red check's own files change only through
  the tester, `gov-tester`, judging the red `spec-wrong`, which routes to Design as a new unit, whose
  own `--dispatch` is no fix pass and holds no keeps. For a `leg:` red the sentence also names the
  targets of the leg's `tests` edge (TOOL-dWitnessedBar-22's row key), the code a `code-miss` fix
  belongs in, or says the leg declares none. Observed by AC3 and AC5.
- **S6** — `python fix_keeps.py --fixture --plant <case>` builds a throwaway repository in the system
  temp directory with a manifest, a leg, its suite file and a preflighted run, and drives
  `unattended.sh` through the case: `writes-test-file`, `writes-product`, `commit-test-file`,
  `acceptance-fixture` and `unknown-leg` (§4). Observed by AC3, AC4, AC5 and AC6.
- **S7** — The flag's statement: the `--fix-of` header line in `unattended.sh`'s argv fence (check 26
  joins it), and one paragraph in the verbs carrier, `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`. Observed by AC7.

## 3. Non-goals (OUT)

- `build.fix-pass`, the item that dispatches a fix pass on a red record: dScopedBuild's. The driver's
  flag is the stand-in a main loop or that item calls.
- The tester role, its return schema and its judgment set: TOOL-dWitnessedBar-23's. This unit names
  the role and the judgment in its refusal and reads nothing it writes.
- Counting fix passes against a budget: TOOL-dDeclaredLoop-30's `flow.rework-budget` draw and
  TOOL-dDeclaredLoop-32's `--fix-pass` loop.
- The targets of a leg's `tests` edge as kept files: they are named in the refusal, never kept (§8 F1).
- A refusal at the harness's write gate (`scratch-guard.js`): the driver's declaration and commit
  check are the clause's enforcement points.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-22` — `tests`, the leg's edge whose targets S5's refusal names as where a code fix belongs
- **consumes-from** `TOOL-dWitnessedBar-23` — `gov-tester`, the role S5's route sends a change to a red check's own files through, and its `spec-wrong` judgment
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 12, 28, 38 and 64: no `tests` target kept, the acceptance reader by heading text, `fix-of` in the two park-kind copies, and the red leg's fixtures kept, each a scope item of that unit

## 4. Design

### The keeps

```
fix_keeps.py --keeps leg:<name>                 -> read_leg_files(<name>)
fix_keeps.py --keeps acceptance --spec <path>   -> read_acceptance_files(<the unit's spec>)
```

One path per line on stdout, exit 0; a refusal on stderr with exit 2. The unit's spec is the file
under `<memory root>/builds/*/spec/` whose heading carries the id, the reading the driver's
`spec_facts` (`unattended.sh:4691`) makes, handed to the module as `--spec <path>`. The manifest
is the one beside the run-gates kit, found through `resolve_kit_dir("run-gates", "run-gates.sh",
here)`, never by literal.

| Leg (manifest row) | Kept |
|---|---|
| `memory hygiene` (`bash {prefix}/memory-tree/check-memory-hygiene.sh`) | `tools/memory-tree/check-memory-hygiene.sh` |
| `shell hygiene (a loop fed by a command substitution)` | `tools/gate-lint/sh_hygiene.py`, `memory/project/substitution-fed-loops.txt` |
| `run-gates canary` | `tools/run-gates/run-gates.test.sh` |

### The plants

| Case | Act in the fixture | Expected |
|---|---|---|
| `writes-test-file` | `--dispatch … --fix-of leg:fx canary --writes tools/fx/fx.test.sh` | exit non-zero, check 49, names the path and `spec-wrong` |
| `writes-product` | the same with `--writes tools/fx/fx.sh` | exit 0, a `fix-of` row recorded |
| `commit-test-file` | `writes-product`, then the suite file staged and `--check-commit` run | exit non-zero, check 49 |
| `acceptance-fixture` | `--fix-of acceptance` on a spec whose AC names `tools/fx/fixtures/a.txt` | that path refused, `tools/fx/fx.sh` admitted |
| `unknown-leg` | `--fix-of leg:nope` | exit non-zero naming `nope` |

### Inventory

Minted: `tools/unattended/fix_keeps.py` with `read_leg_files`, `read_acceptance_files` and the verbs
`--keeps`, `--spec`, `--fixture`, `--plant`; the `--dispatch` flag `--fix-of`; the run-state row kind
`fix-of`; the red forms `leg:<name>` and `acceptance`. Naming cells: each function is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive. A dispatch without `--fix-of` behaves as today.

### Rollout

Live at landing. The unattended kit's version moves (`KIT_UNATTENDED_VERSION`, `unattended.sh`), and
the kit's `[[files]]` `include = "**"` row (`tools/unattended/kit.toml:14-16`) already ships the new
module as an engine file.

### Files touched (estimate)

- `tools/unattended/fix_keeps.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **The keeps typed into the spec's Files touched.** They are derived from the manifest and the spec
  at dispatch, so a moved suite cannot leave a stale list.
- **Refusing at the harness's write gate.** It sees Edit and Write calls only, so a shell write passes
  it; the commit check sees every staged path.

## 5. Production-readiness checklist

- security — narrows a write surface: a fix pass may write less than it declared. The leg name and
  the spec path reach `fix_keeps.py` as argv words, never through a shell string; a leg name spelling
  `BYPASS_BAN` is refused as every recorded field is.
- perf / scale — one python spawn per `--dispatch --fix-of` and per `--check-commit` on a key holding
  a `fix-of` row; no spawn on any other commit.
- error / empty / loading states — an unknown leg, an absent manifest or a spec the id names nowhere
  refuses the dispatch, exit 2 from the module, check 49 from the driver; an empty keep set is printed
  as `fix-of: no kept file` and admits every declared path.
- observability — the `fix-of` row in `RUN.md`, and each refusal naming the path, the red and the route.
- risks — a leg whose gate script is also product code (`govkit selfcheck` runs `govkit.py`) keeps
  that file out of a fix pass, so a code miss there goes to a new unit; this follows the clause's
  "gate script" and is stated in the verbs carrier.
- testing — AC1 to AC7 by fixture and probe; the arm in §7.
- migration — none, per §4.
- user docs — none owed under `help/`; the verbs carrier states the flag (S7).

## 6. Acceptance criteria

- **AC1** — When `python fix_keeps.py --keeps 'leg:memory hygiene'`
  runs in `tools/unattended/`, it prints `tools/memory-tree/check-memory-hygiene.sh` and nothing else,
  and with `'leg:nope'` it exits 2 naming `nope`.
  Red when: the manifest's `{prefix}` is not resolved, so no word names a tracked file.
- **AC2** — When `python fix_keeps.py --fixture --plant acceptance-fixture` runs, the fixture path the
  spec's AC names is kept and the product file the same AC probes is not.
  Red when: every tracked file an AC names is kept, so the fix pass cannot touch the code it fixes.
- **AC3** — When `python fix_keeps.py --fixture --plant writes-test-file` runs, the fixture's
  `unattended.sh --dispatch` with `--fix-of` exits non-zero with check 49 naming the leg's suite file,
  `gov-tester` and `spec-wrong`: the clause's planted fix pass writing the red leg's test file.
  Red when: `--dispatch` ignores `--fix-of`, so the declaration is recorded.
- **AC4** — When `python fix_keeps.py --fixture --plant writes-product` runs, the dispatch exits 0 and
  the fixture's `RUN.md` holds one `fix-of` row naming the leg.
  Red when: the keeps refuse a path outside them, so no fix pass can declare its fix.
- **AC5** — When `python fix_keeps.py --fixture --plant commit-test-file` runs, the fixture's
  `unattended.sh --check-commit` exits non-zero with check 49 naming the staged suite file.
  Red when: the commit check reads no `fix-of` row, so a fix pass that never declared the file commits it.
- **AC6** — When `python fix_keeps.py --fixture --plant unknown-leg` runs, the dispatch exits non-zero
  naming the unknown leg and records nothing.
  Red when: an unknown leg reads as an empty keep set and the pass is admitted unrestricted.
- **AC7** — When `grep -n 'fix-of' memory/guides/UNATTENDED-VERBS.md tools/unattended/unattended.sh`
  runs, the verbs carrier states the flag and the argv fence holds its header line.
  Red when: the flag is parsed and documented nowhere, the class check 26 reads.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 AC5 AC6 · each plant of §4 run through `fix_keeps.py --fixture`, staged red by deleting the keeps refusal from `verb_dispatch` and the `fix-of` read from `check_commit_message` · none

## 8. Open questions

- **F1 — Do the targets of the red leg's `tests` edge join its kept files, as shared interface I15
  says?** A `tests` edge names what its source tests (PLAY-dOrderedCharter-24's registry: `tests`, any
  to any), so on a leg row its targets are the code under test. Options: (a) keep them, as I15 reads;
  (b) keep the argv words alone. (a) empties a code-miss fix pass's allowance of the code it must fix,
  so flow-steps' `build.fix-pass` row (`:291`), routed from a `code-miss` judgment, could not act.
  TOOL-dWitnessedBar-22 S1 confirms the reading: "a list of tags, each a thing the leg tests".
  RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the only option under which the clause's two
  routes, fix pass and new unit, both remain; the `tests` targets are read for S5's refusal, which
  names them as where a code fix belongs. widens: none · relaxes: none
- **F2 — Which of the files an acceptance command names are "its own"?** In this repository a command
  usually probes the unit's own module (`python seen_red.py --fixture …`), so the module is both the
  product and the probe. Options: (a) every tracked file a §6 token names; (b) the check files among
  them, by the class S2 states; (c) none until dScopedBuild's executor records which files a command
  read. (a) keeps the product out of its own fix pass; (c) leaves M16's half of the clause unbuilt.
  RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the most capable surviving option, its limit
  stated in §5: a probe whose plants live inside the product keeps nothing; the departure is
  `2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md`. widens: none · relaxes: none
- **F3 — Is a new driver flag and row kind within this build's authority?** The verbs carrier is a
  governance carrier and `--fix-of` a public surface of the unattended kit. RESOLVED (agent,
  2026-10-25, delegated): yes, rung 3 with veto 2 lifted by the README's `may:` grant, because the
  carried clause names the fix pass's allowance and its arm, and the brief names `--dispatch --writes`
  and `--check-commit` as its enforcement points. grants: PLAY-dClosedLoop-3 the --fix-of flag of
  --dispatch, the fix-of run-state row kind and their statement in the unattended verbs carrier.
  widens: none · relaxes: none
- **F4 — Which hash does the `**Carries:**` line pin?** Deviation `2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211` amends
  cl-dClosedLoop-0359's text, so the as-built view hashes it `5c408077` where the baseline hashed `390176b3`.
  RESOLVED (agent, 2026-10-25, delegated): rung 1, the line pins `cl-dClosedLoop-0359@5c408077`, the view's hash,
  moved by deviation 211. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 21, the brief's shared interfaces I14
  and I15, scout A's row for cl-0359 and flow-steps' `build.fix-pass` row and "A fix pass keeps its
  check" (`:291`, `:382`), at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; the `**Carries:**` line re-pinned to `5c408077`, deviation 211's amended text, with §8 F4; nothing else moved.

## 10. Reuse audit

The seams extended: `verb_dispatch`'s per-path `--writes` refusals
(`tools/unattended/unattended.sh:13800-13850`), `check_commit_message`'s staged-path walk
(`:13475-13582`), the run-state row writer `park()` (`:12533`) and `PARK_KINDS` (`:875`), and the
runner's argv-word census shape (`tools/run-gates/run-gates.sh:3026-3027`), whose predicate S1 reads
without the extension filter because the census selects shipped sources and this unit selects the
files a check reads. `python tools/codebase-map/reuse_lookup.py "exclude a red gate leg's own test
files from a fix pass write set"` ranked generic stems (`write`, `legs`, `owners_of`) and no seam that
subtracts a path set from a declaration: no existing seam fits the keeps derivation, so it is a new
module beside the driver. Scout A cited `--dispatch` validation at `:13799-13830` and
`check_commit_message` at `:13474`; at `cdfbd1cf` the per-path loop runs `:13800-13850` and the
function opens at `:13475`.

Recall terms used: `python tools/memory-recall/query.py "how does a fix pass keep the check that reds it out of its declared write set" --terms "fix pass allowance red leg test files gate script dispatch writes check-commit spec-wrong tester"`
