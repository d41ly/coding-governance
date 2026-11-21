# TOOL-dWitnessedBar-21 — a fix pass that keeps its check: its allowance less the red leg's own files and the acceptance commands' own files

**Status:** CLOSED · rev-4 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 27 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0359@5c408077 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md](../build/2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-11-05-build-TOOL-dWitnessedBar-1-crosscheck-returns.md](../build/2026-11-05-build-TOOL-dWitnessedBar-1-crosscheck-returns.md) | research | TOOL-dWitnessedBar-1 |
| [2026-11-05-build-TOOL-dWitnessedBar-1-parents-crosscheck.md](../build/2026-11-05-build-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 |
| [2026-11-19-build-TOOL-dWitnessedBar-21-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-21-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-21-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-21-1-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-115.md](../build/2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-115.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-116.md](../build/2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-116.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-117.md](../build/2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-117.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-118.md](../build/2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-118.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-119.md](../build/2026-11-20-build-TOOL-dWitnessedBar-21-red-fix-119.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 |
| [2026-11-05-prompt-TOOL-dWitnessedBar-21-1-spec-reviewer.md](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-21-1-spec-reviewer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-21-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-21-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-21-reground3-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-21-reground3-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-21-reground3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-21-reground3-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

A fix pass may edit the check that reds it: nothing keeps a red leg's own test files or gate script
out of the pass's write set (gap-test-19). A re-dispatch is an ordinary `--dispatch`
(`tools/unattended/unattended.sh#verb_dispatch`), which draws the rework budget as a `fix-pass` or
`re-dispatch` cause and then records its row. Its `--writes` loops refuse only shape, the run-state
file, shared records, a sibling's overlap and the generator pairing. This unit declares a fix pass against the red it fixes, subtracts the
red check's own files from its allowance at `--dispatch --writes` and at `--check-commit`, and routes a
change to those files through the tester's `spec-wrong` judgment to Design as a new unit; a fix pass
after a failed acceptance leaves the acceptance commands' own files alone (night pass, point 6; M16).

## 2. Scope (IN)

- **S1** — The red leg's own files (shared interface I15), `read_leg_files(rows, name, tool_root,
  tracked)` in `tools/unattended/fix_keeps.py`: the words of the leg's `argv` in
  `tools/gate-legs.json`, `{prefix}` resolved to the tool root, that carry a `/`, no whitespace, and
  name a tracked file, the census shape of `tools/run-gates/run-gates.sh@e044bc9fce2f:3313-3314`
  without its extension filter; the gate script is the first such word. An unknown leg name is a
  refusal naming it. Observed by AC1.
- **S2** — The acceptance commands' own files, `read_acceptance_files(spec_text, tracked)` in the same
  module: every word of a backticked token in the spec's acceptance-criteria section that names a
  tracked file, by path or by a basename unique among tracked files, and that is a check file:
  `*.test.sh`, a name ending `selftest.py`, `test_*.py`, or a path under a `fixtures/` directory
  (§8 F2). Observed by AC2.
- **S3** — The declaration: `--dispatch <slug> --pass <id> --writes <path>… --fix-of <red>`, `<red>`
  one of `leg:<leg name>` or `acceptance`. The driver computes the keeps by running
  `fix_keeps.py --keeps <red> [--spec <path>]` under the launcher `resolve_python` answers, the way
  `tools/unattended/unattended.sh#check_commit_message` runs `commit_trailers.py`. It refuses, with
  code 49, every `--writes` path that covers or is covered by a kept file, naming the path, the red
  and the route of S5. The refusal sits after the per-path shape loop and before the rework budget's
  draw and the `dispatch` row, so a refused declaration draws nothing and records nothing. On success
  it records one run-state row `<ts> fix-of · item <grp> <unit> · reason <red>` through
  `tools/unattended/unattended.sh#park`, at a call site spelled `park "$rel" fix-of `, the literal
  check 27 of `tools/unattended/check-unattended.sh` joins to the kind set both ways. `fix-of` joins
  `tools/unattended/unattended.sh#PARK_KINDS`. Observed by AC3 and AC4.
- **S4** — The commit check: `tools/unattended/unattended.sh#check_commit_message`, for an open pass
  whose key holds a `fix-of` row, re-derives the keeps and refuses a staged path among them, code 49,
  with S5's route. It refuses before the walk's undeclared-path refusal, so a staged kept file meets
  the route and never a widening command the keeps would refuse. A later `--dispatch` of that key
  without `--fix-of` is held to the same keeps. A `--no-verify` commit that writes a kept file falls
  outside the declared set, so check 23 refuses it at the close as code 49 does today. Observed by
  AC5.
- **S5** — The route, one sentence both refusals print: a red check's own files change only through
  the tester, `gov-tester`, judging the red `spec-wrong`, which routes to Design as a new unit, whose
  own `--dispatch` is no fix pass and holds no keeps. For a `leg:` red the sentence also names the
  targets of the leg's `tests` edge, the `feature.<f>` tags TOOL-dWitnessedBar-22's row key carries
  in `tools/gate-legs.json`, each the feature whose dossier names the code a `code-miss` fix belongs
  in. A leg whose row carries no `tests` key, `run-gates canary` among them, is said to declare none.
  Observed by AC3 and AC5.
- **S6** — `python fix_keeps.py --fixture --plant <case>` builds a throwaway repository in the system
  temp directory with a manifest, a leg, its suite file, a preflighted run, and the build README and
  unit spec that `tools/unattended/unattended.sh#check_unit_spec` reads before a dispatch is admitted.
  It drives `unattended.sh` through the case: `writes-test-file`, `writes-product`,
  `commit-test-file`, `acceptance-fixture` and `unknown-leg` (§4). Observed by AC3, AC4, AC5 and AC6.
- **S7** — The flag's statement: `[--fix-of <red>]` on the `--dispatch` line of `unattended.sh`'s
  header, which `usage` renders, and the flag parsed between the `gov:argv-begin` and `gov:argv-end`
  sentinels. Check 26's flag arm joins the header and the parser both ways, and its suite half wants
  the token on a non-comment line of `tools/unattended/unattended.test.sh`. One paragraph states it
  in the verbs carrier, `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`. Observed by AC7.
- **S8** — The kind's held copies (§8 F5): `fix-of` joins
  `tools/drift-audit/drift_report.py#_RUN_PARK_KINDS` and `tools/runlog/model.py#PARK_KINDS`, each
  compared with the driver's set both ways by its kit's self-test. `tools/runlog/record.py` gains
  `EXCLUDED_KINDS_BEFORE_FIX_OF`, `EXCLUDED_KINDS` less `fix-of`, and `EXCLUDED_KINDS_BEFORE_REFUSAL`
  derives from it, so a committed record keeps reading against the set it was rendered under. The
  `excluded rows` fact's shapes gain the `EXCLUDED_KINDS_BEFORE_FIX_OF` shape, the set a record
  rendered before this unit carries. Observed by AC8.

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
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 12, 28 and 64: no `tests` target kept, the acceptance reader by heading text, and the red leg's fixtures kept, each a scope item of that unit; id 38, `fix-of` in the two park-kind copies, is this unit's S8 (§8 F5)

## 4. Design

### The keeps

```
fix_keeps.py --keeps leg:<name>                 -> read_leg_files(<name>)
fix_keeps.py --keeps acceptance --spec <path>   -> read_acceptance_files(<the unit's spec>)
```

One path per line on stdout, exit 0; a refusal on stderr with exit 2. The unit's spec is the file
under `<memory root>/builds/*/spec/` whose heading carries the id, handed to the module as
`--spec <path>`. At `--dispatch` it is the path `tools/unattended/unattended.sh#check_unit_spec`
already set, which `verb_dispatch` holds as `_d_spec`. At `--check-commit` it is the `SPEC_PATH`
entry `tools/unattended/unattended.sh#load_spec_facts` fills, read only for a key holding a
`fix-of acceptance` row. The manifest is `gate-legs.json` in the run-gates kit's parent directory,
`resolve_kit_dir("run-gates", "run-gates.sh", here).parent / "gate-legs.json"`, the reading
`tools/memory-tree/routed_commits.py#resolve_leg_manifest` makes, never a literal. That parent is
the tool root, against which `{prefix}` resolves through `resolve_prefix_token`. The module carries
`resolve_kit_dir` and `resolve_prefix_token` inline between their `# >>>` markers, byte-identical
to `tools/lib/resolve_kit_dir.py#resolve_kit_dir` and
`tools/lib/resolve_prefix_token.py#resolve_prefix_token`, because the unattended kit is
copy-installed. The parity arm of `python resolver (behaviour + inline parity + idiom ban)` finds
every carrier by its marker, so the module joins that population.

### The driver's one helper

`check_fix_keeps`, called by `verb_dispatch` and `check_commit_message`, holds every refusal site
this unit adds to `tools/unattended/unattended.sh`: the red's shape refused, the module's refusal
relayed, and a kept path refused. The driver's census is 340 branches, PINNED 2026-11-20 by
`python tools/memory-tree/check-arms.py --emit-floors`. Its ceiling is 343 (PINNED 2026-11-20), the
`tools/unattended/unattended.sh` entry of `.memory-tree.conf`'s `REFUSAL_CEILINGS`, so these
three sites reach the ceiling and pass it nowhere. A fourth would be a ceiling raise under the
retirement review that file's growth-budget comment names, which this unit does not take. Each
site is armed in `tools/unattended/unattended.test.sh`, the class
`harness arms (fail branches armed or pinned)` grades. The shape refusal's arm calls
`--dispatch … --fix-of` directly, which also puts the flag on the suite line check 26 wants.

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
`--keeps`, `--spec`, `--fixture`, `--plant`; the driver function `check_fix_keeps`; the `--dispatch`
flag `--fix-of`; the run-state row kind `fix-of`; the red forms `leg:<name>` and `acceptance`; the
constant `EXCLUDED_KINDS_BEFORE_FIX_OF` in `tools/runlog/record.py`. Naming cells:
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answers OK for
`read_leg_files` and `read_acceptance_files`, and `--as sh.function` answers OK for
`check_fix_keeps`, each asked 2026-11-20. The lexicon declares no constant cell.

### Migration

Additive. A dispatch without `--fix-of` behaves as today.

### Rollout

Live at landing. The unattended, drift-audit and runlog kits' versions are minted at the landing by
the lander's `tools/push-main.sh#run_minter`, never by the pass. The unattended kit's `[[files]]`
`include = "**"` row (`tools/unattended/kit.toml@3ef0246e7453:25-27`) already ships the new module
as an engine file.

### Files touched (estimate)

- `tools/unattended/fix_keeps.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/drift-audit/drift_report.py` (`_RUN_PARK_KINDS`, S8)
- `tools/runlog/model.py` (`PARK_KINDS`, S8)
- `tools/runlog/record.py` (`EXCLUDED_KINDS_BEFORE_FIX_OF`, S8)
- `memory/map/generated/symbols.json` (re-rendered by the codebase-map kit's `gen_map.py --write`,
  which the unguarded `codebase-map coverage + freshness` leg reads)

Shared with sibling units: `tools/unattended/unattended.sh` with `TOOL-dWitnessedBar-30` (order 24)
and `tools/drift-audit/drift_report.py` with `TOOL-dWitnessedBar-1` (order 23), both landed, neither
of whose landed changes touches a seam this unit extends. `memory/map/generated/symbols.json` is
shared with `TOOL-dWitnessedBar-7` (order 26), which lands before this unit, and
`tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh` with
`TOOL-dWitnessedBar-6` (order 28), which lands after it. Nothing is shared with
`TOOL-dWitnessedBar-29`.

### Alternatives rejected

- **The keeps typed into the spec's Files touched.** They are derived from the manifest and the spec
  at dispatch, so a moved suite cannot leave a stale list.
- **Refusing at the harness's write gate.** It sees Edit and Write calls only, so a shell write passes
  it; the commit check sees every staged path.
- **The red carried on the `fix-pass` row.** `--fix-pass` (TOOL-dDeclaredLoop-32) records a pass
  after it ran, with its count of reds, so its row comes after the writes the keeps must bound; the
  keeps bind at `--dispatch`, before any write.

## 5. Production-readiness checklist

- security — narrows a write surface: a fix pass may write less than it declared. The leg name and
  the spec path reach `fix_keeps.py` as argv words, never through a shell string; a leg name spelling
  `BYPASS_BAN` is refused as every recorded field is. The fixture's planted kit `fx` is no directory
  of the tool root, so its literal paths spell no kit path `install-prefix (shipped surface)` bans.
- perf / scale — one python spawn per `--dispatch --fix-of` and per `--check-commit` on a key holding
  a `fix-of` row; no spawn on any other commit.
- error / empty / loading states — an unknown leg, an absent manifest or a spec the id names nowhere
  refuses the dispatch, exit 2 from the module, check 49 from the driver; an empty keep set is printed
  as `fix-of: no kept file` and admits every declared path.
- observability — the `fix-of` row in `RUN.md`, and each refusal naming the path, the red and the route.
- risks — a leg whose gate script is also product code (`govkit selfcheck` runs `govkit.py`) keeps
  that file out of a fix pass, so a code miss there goes to a new unit; this follows the clause's
  "gate script" and is stated in the verbs carrier.
- testing — AC1 to AC8 by fixture and probe; the arm in §7; each of `check_fix_keeps`'s refusal
  sites armed in the driver's suite (§4 "The driver's one helper").
- migration — none, per §4.
- user docs — none owed under `help/`; the verbs carrier states the flag (S7). The usage row
  `verb:unattended.sh:--dispatch` is listed in `memory/project/docs-undocumented.txt`, so the
  fingerprint the new flag moves anchors on no page.

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
  runs, the verbs carrier states the flag and the driver's `--dispatch` header line carries it.
  Red when: the flag is parsed and documented nowhere, the class check 26 reads.
- **AC8** — When `grep -c '"fix-of"' tools/drift-audit/drift_report.py tools/runlog/model.py` runs,
  it prints 1 for each file; and when this probe runs, it prints `True False`:
  `python -B -c "import sys; sys.path.insert(0, 'tools/runlog'); import record; print('fix-of' in record.EXCLUDED_KINDS, 'fix-of' in record.EXCLUDED_KINDS_BEFORE_FIX_OF)"`
  Red when: a copy lacks `fix-of`, so its both-ways comparison with the driver's set reds, or the
  record reader keeps no set a record rendered before this unit carries.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `drift-audit selftest` · `runlog selftest` · `runlog record schema` · `policy fixtures` · `run-gates run-log line` · `pre-push run-log line` · `harness arms (fail branches armed or pinned)` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 AC5 AC6 · each plant of §4 run through `fix_keeps.py --fixture`, staged red by deleting the `check_fix_keeps` calls from `verb_dispatch` and `check_commit_message` · none

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
  As landed, TOOL-dWitnessedBar-22's targets are `feature.<f>` tags and no file path, so (a) would
  keep no file either; the pick stands and S5 names the tags.
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
- **F5 — Who writes `fix-of` into the two held copies of the park-kind set?** The round-1 audit's
  minor id 38 handed it to TOOL-dWitnessedBar-51 S23, at order 31. At HEAD the copies,
  `tools/drift-audit/drift_report.py#_RUN_PARK_KINDS` and `tools/runlog/model.py#PARK_KINDS`, are
  each held to `tools/unattended/unattended.sh#PARK_KINDS` both ways by `drift-audit selftest` and
  `runlog selftest`. The runlog record reader also reds a committed record whose excluded set it no
  longer knows, the defect `f035f1169` repaired a day after `fix-pass` joined in `29d86011b`.
  Options: (a) this unit writes `fix-of` into both copies and `tools/runlog/record.py`'s derivations
  in its own commit, as S8; (b) keep the hand-off to unit 51. (b) leaves both comparisons red from
  this unit's landing at order 27 until order 31. Neither leg's guard names the driver, so the red
  is latent at this landing and surfaces under `GATE_FULL=1` or in the next pass touching either
  kit, a red that pass did not cause. RESOLVED (agent, 2026-11-20, delegated): (a), veto 1
  discarding (b), which fails two legs this unit's change reds; it is also the shape
  TOOL-dDeclaredLoop-32 took for `fix-pass`. Unit 51's S23 and AC19 then hold at its build.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 21, the brief's shared interfaces I14
  and I15, scout A's row for cl-0359 and flow-steps' `build.fix-pass` row and "A fix pass keeps its
  check" (`:291`, `:382`), at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; the `**Carries:**` line re-pinned to `5c408077`, deviation 211's amended text, with §8 F4; nothing else moved.
- rev-3 · 2026-11-19 · §7 · the leg line gains the legs `scratch-guard self-test` and
  `tier2-review self-test`, whose guards §4's `tools/unattended/unattended.sh` trips, as the
  spec-token checker's guards join named them at `c6df3e901`, by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief`; §4 is unchanged, as the unit writes
  that path; nothing else moved.
- rev-4 · 2026-11-20 · §1 · S1 S3 S4 S5 S6 S7 S8 · §3 · §4 · §5 · AC7 AC8 · §7 · §8 F1 F5 · §10 ·
  re-grounded on the tree at `174f9d9e5`, every unit through order 24 landed, by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-21-reground3-brief`: line citations become `path#symbol` or
  blob-pinned; the re-dispatch's rework-budget draw and the landed `--fix-pass` kind are named; the
  keeps run under `resolve_python`, refuse before the budget draw, and sit in one helper
  `check_fix_keeps` held to the driver's refusal ceiling; the spec path is `check_unit_spec`'s, the
  manifest `resolve_leg_manifest`'s reading, `{prefix}` resolved by an inline
  `resolve_prefix_token`; S5 names the landed `feature.<f>` tags; S7 names the header line, the
  argv sentinels and check 26's suite half; S8 and AC8 take id 38 from unit 51 (F5), the hands-off
  bullet dropping it; Files touched gains the two copies, `record.py` and `symbols.json`, and the
  leg line `drift-audit selftest`, `runlog selftest`, `runlog record schema`, `policy fixtures`,
  `run-gates run-log line`, `pre-push run-log line`, `harness arms (fail branches armed or pinned)`,
  `python resolver (behaviour + inline parity + idiom ban)` and
  `codebase-map coverage + freshness`; the version bump is the lander's.

## 10. Reuse audit

The seams extended: `tools/unattended/unattended.sh#verb_dispatch`'s per-path `--writes` refusals,
`tools/unattended/unattended.sh#check_commit_message`'s staged-path walk and its launcher call, the
run-state row writer `tools/unattended/unattended.sh#park` and the kind set
`tools/unattended/unattended.sh#PARK_KINDS` with its two held copies, and the runner's argv-word
census shape (`tools/run-gates/run-gates.sh@e044bc9fce2f:3313-3314`). S1 reads that predicate
without the extension filter, because the census selects shipped sources and this unit selects the
files a check reads. The manifest and `{prefix}` are read through the landed readers
`tools/memory-tree/routed_commits.py#resolve_leg_manifest` and
`tools/lib/resolve_prefix_token.py#resolve_prefix_token`. The `fix-pass` row and `--fix-pass` verb
(TOOL-dDeclaredLoop-32) count passes after they run and carry no red, so they are no seam for a
declaration made before the writes (§4 Alternatives rejected). Re-run 2026-11-20,
`python tools/codebase-map/reuse_lookup.py "exclude a red gate leg's own test files from a fix pass
write set"` ranked generic stems (`write`, `legs`, `owners_of`) and no seam that subtracts a path set
from a declaration: no existing seam fits the keeps derivation, so it is a new module beside the
driver. Scout A's line citations were made against an older tree; each seam is cited by symbol
above.

Recall terms used: `python tools/memory-recall/query.py "how does a fix pass keep the check that reds it out of its declared write set" --terms "fix pass allowance red leg test files gate script dispatch writes check-commit spec-wrong tester"`
