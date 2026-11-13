# TOOL-aClearedLedger-7 — the policy fixtures leg prints no wrong assertion: fourteen guard paths, the recall plant's grammar file, and check 8 saying the reader's refusal

**Status:** INPROGRESS · rev-1 · 2026-11-13 · node a · Tier-1 · base 8db6f4be · streams tooling · order 7 · closes TOOL-aNimbleMend-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The `policy fixtures` leg prints wrong assertions that predate this build, so a new one hides among
them. This unit fixes each of the three causes where it sits, so the leg reads `0 wrong`.

## 2. Scope (IN)

- **S1** — The `policy fixtures` row of `tools/gate-legs.json` gains fourteen guard paths, one per
  file its cases import or read and its guard does not name, and the `pass_leg` field is re-applied.
  Observed by AC1, AC2 and AC3.
- **S2** — `tools/policy/check_policy.py#derive_recall_export_plant` plants the memory-tree kit's
  `id_grammar.py` beside the recall kit copy, so the recall enforcer's kit lookup resolves in the
  case repository. Observed by AC4.
- **S3** — Check 8 of `tools/check-template-size.sh` prints the policy reader's refusal, once, when
  the cap it grades is the handed-in default of a reader that refused. Its exit and its remedy
  sentence are unchanged. Observed by AC5 and AC6.
- **S4** — The whole leg prints `0 wrong`. Observed by AC7, which is the main loop's.

## 3. Non-goals (OUT)

- No case of `tools/policy/check_policy.py` is removed, re-pointed at another subject or given a
  looser expectation, and no assertion is waived.
- No directory guard for `tools/playbook/` (section 4, "Alternatives rejected").
- No skip of check 8 for an undeclared cap (section 4, "Alternatives rejected").
- No arm is added to `tools/check-template-size.test.sh`. The case `budgets-reader-refused` is the
  arm that observes S3, and it is red today.
- The `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` that a moved manifest owes. The
  main loop makes it after the pass, as it did after TOOL-aNimbleMend-27.
- Any kit version, which the lander's `mint` moves.
- Any edit to a CLOSED spec. Each correction is stated here.

## 4. Design

### Evidence

The leg's own command, run by the main loop on a frozen clone of `8db6f4bef`, printed
`908 assertion(s) executed · 31 wrong` (PINNED, 2026-11-13). The output is
`C:/Users/daily-agent/AppData/Local/Temp/nm16out/a20.out` on node a. The ask counted 33 at
aNimbleMend's tip: TOOL-aNimbleMend-27 has since guarded `id_grammar.py`, which cured two rows.

| Rows | Count at `8db6f4bef` | Cause, verified in source |
|---|---|---|
| `fixtures-guard-census` | 13 | thirteen playbook modules the census enforcers import, outside the guard |
| `guard-trace` | 14 | the same thirteen, and `tools/govkit/upgrade_steps.py`, which this process reads |
| `budgets-cap-recall-export` | 3 | the plant copies no memory-tree kit, and the recall kit now looks one up |
| `budgets-reader-refused` | 1 | check 8 exits before the reader's refusal is printed |

### S1 — fourteen guard paths

`tools/policy/check_policy.py#run_fixtures_guard_census` owes the guard every file
`derive_enforcer_imports` finds a census enforcer reaching, transitively and inside the enforcer's
own directory. `check_guard_trace` owes it every source file the fixture process opens. The judge of
both is `python tools/check-spec-tokens.py --legs-for -`. The guard names four playbook modules
today. PLAY-dOrderedCharter split the renderer into more, and nothing added them.

Append to the row's `guard`, last, in this order, each spelled `{prefix}/<rest>`:

| Path | Owed by |
|---|---|
| `tools/govkit/upgrade_steps.py` | the trace: `tools/govkit/govkit.py#load_upgrade_steps` opens it |
| `tools/playbook/check_layers.py` | the census and the trace |
| `tools/playbook/core.py` | the census and the trace |
| `tools/playbook/edge_grammar.py` | the census and the trace |
| `tools/playbook/gov_tag.py` | the census and the trace |
| `tools/playbook/instructions_edit.py` | the census and the trace |
| `tools/playbook/memory_index.py` | the census and the trace |
| `tools/playbook/overlay.py` | the census and the trace |
| `tools/playbook/overlay_rows.py` | the census and the trace |
| `tools/playbook/pins.py` | the census and the trace |
| `tools/playbook/positional.py` | the census and the trace |
| `tools/playbook/row_checks.py` | the census and the trace |
| `tools/playbook/tag_bundle.py` | the census and the trace |
| `tools/playbook/tag_index.py` | the census and the trace |

Each is tracked, which `check_guard_lines` requires. Then `python tools/run-gates/pass_legs.py --apply`
runs. The seam is the one TOOL-dGroundRules-25 S24 and TOOL-dGroundRules-67 used: one line per file.

### S2 — the recall plant

`tools/memory-recall/recall_conf.py@8db6f4bef:75` resolves the memory-tree kit by its anchor
`id_grammar.py`, through the install receipt and then two sibling probes. The recall kit's
descriptor declares `requires = ["memory-tree"]`. `derive_recall_export_plant` copies the recall kit
and the policy kit only, so each of the three modes dies on a `LookupError` before the export runs.

The plant's `files` gains one entry: the memory-tree kit's `id_grammar.py` at its own path under the
tool root, its bytes read from the source tree. The path is joined from `budgets.derive_tool_root()`,
never typed with the tool root in it. `id_grammar.py` imports the standard library only, so the one
file satisfies the sibling probe. `derive_zero_plant` copies `files`, so the third mode follows.

UNVERIFIED: that the export, past the lookup, reaches its cap check in all three modes. No probe of
this spec ran the case. AC4 observes it, and a further missing file is this scope item's to plant.

### S3 — check 8 and a reader that refused

`budgets.py resolve` answers a refused reader with a row and prints the refusal on its stderr
(`tools/policy/budgets.py#main`). The enforcer captures both and reads the first line, so the
refusal is dropped (`tools/check-template-size.sh@8db6f4bef:322` and `:330`). For `AGENTS.md` the
row then holds the handed-in default, source `constant`. Check 8, landed by PLAY-dOrderedCharter-6
on 2026-11-08, compares that default with `CODEX_MAX` and exits at `:347`. Check 2, whose verdict
would have carried the refusal, never runs. The case wants a non-zero exit, no `BUDGET WARN`, and
the ladder's refusal said once (TOOL-dGroundRules-21 S31).

The fix keeps check 8's red and makes it say why the cap is a default. The lines of the captured
answer after the first are the reader's refusal. When they are non-empty, check 8's message carries
them after its remedy sentence, on their own line, introduced by a clause saying the cap is the
handed-in default because the policy reader refused. The `fail 8` call stays one call, so
`check-arms.py` sees no new branch. The exit code logic is untouched.

Two landed criteria bind here, and this is the one form that holds both. PLAY-dOrderedCharter-6 S6
holds the charter's cap inside `CODEX_MAX` under either value of the switch. TOOL-dGroundRules-21
S31 has a refusing reader's refusal printed once. Before the edit the builder runs
`git grep -n "not held inside the smallest harness"` and keeps every substring a reader pins.

### What it does not check

- A file a child process reads. The trace sees this process alone, by its own docstring.
- A playbook module added after this unit. The census reds on it, which is its job.
- Check 8's wording under a refusal. AC5 counts the ladder's sentence and nothing else.
- A refusing reader over a charter inside the default. Check 8 reds there too, now with the reason.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/policy/check_policy.py`
- `tools/check-template-size.sh`

### Alternatives rejected

- **One directory guard, `{prefix}/playbook/`.** It never goes stale. It also starts this leg, at
  a ceiling of 2420 s (PINNED, 2026-11-13), on an edit of the practice catalogue or a template,
  which no case reads. The census exists to name the next missing module.
- **Copying the whole memory-tree kit into the recall plant.** The copy opens every file of the kit
  in the fixture process on a platform whose copy opens files, and the trace would then owe each one
  a guard line. One file is what the lookup needs.
- **Guarding check 8 on a declared cap.** One token. A charter between `CODEX_MAX` and the default
  would then pass in silence under a refusing reader, which loosens a gate to pass a case.
- **Pointing the case at another subject.** The case would pass and `AGENTS.md` under a refusing
  reader would keep printing a remedy with no reason. That is the arm moved off the defect.

## 5. Acceptance criteria

Each of AC1 to AC6 is a probe a builder runs. A one-case fixture run is the direct check the
spec-token checker admits. Where a hook refuses one, that criterion is the main loop's.

- **AC1** — When the fourteen paths of section 4's table, one per line, are piped to
  `python tools/check-spec-tokens.py --legs-for -` and its output to
  `grep -c '^  policy fixtures <- '`, it prints 14.
  Red when: a path is missing from the guard or misspelled. It prints 0 at `8db6f4bef`.
  figure: the list is PINNED, 2026-11-13, from the leg's output at `8db6f4bef`.
- **AC2** — When `python tools/run-gates/pass_legs.py --check` runs, it exits 0.
  Red when: `--apply` did not run after the manifest moved.
- **AC3** — When `python tools/policy/check_policy.py --fixture fixtures-guard-census` runs, no line
  holds `WRONG` and the last line ends `· 0 wrong`.
  Red when: a census enforcer reaches a module outside the guard, or the case's own reads do.
- **AC4** — When `python tools/policy/check_policy.py --fixture budgets-cap-recall-export` runs, it
  prints one line each for `warn`, `refuse` and `zero`, none holding `WRONG` or `LookupError`, and
  the last line ends `· 0 wrong`.
  Red when: the plant holds no `id_grammar.py`, or the export needs a file the plant still lacks.
- **AC5** — When `python tools/policy/check_policy.py --fixture budgets-reader-refused` runs, the
  line naming `two remotes, no GOV_REMOTE, under warn` holds `said 1 time(s)` and no `WRONG`, and
  the last line ends `· 0 wrong`.
  Red when: check 8 exits without the reader's refusal, or prints it twice.
- **AC6** — When `grep -c 'Lower the cap to CODEX_MAX or under; a harness reading less than the charter drops its tail.' tools/check-template-size.sh`
  runs it prints 1, and `grep -c 'fail 8 ' tools/check-template-size.sh` prints 1.
  Red when: the remedy sentence an arm of the enforcer's suite pins was reworded, or a second
  `fail 8` branch was added.
- **AC7** — When the main loop runs the leg `policy fixtures` of `tools/gate-legs.json` on a frozen
  clone of the built tip, the last line of its output ends `· 0 wrong`.
  Red when: any assertion is wrong, one outside the three causes included.
  permission: the main loop's; the command is a leg's own.
  cost: the leg's ceiling is 2420 s (PINNED, 2026-11-13).

## 6. Gates

`policy fixtures` · `template size gate selftest` · `charter size` · `scratch-guard self-test` · `routed-commits selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

The first is the leg this unit repairs. The next two run the enforcer S3 edits. The last five are
owed by a guard the estimate trips: two by the policy checker, three by the manifest.

The close is the brief's: the plain bar once after the last unit. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 9. Reuse audit

The seam is the leg's own `guard` list, extended one line per file as TOOL-dGroundRules-25 S24 and
TOOL-dGroundRules-67 extended it, and the plant's own `files` map. `python
tools/codebase-map/reuse_lookup.py "a gate leg's guard list covering every file its fixture cases
import or read"` ranked name-stem neighbours only, so for a helper that derives a guard list no
existing seam fits, and fourteen lines of data do not earn one. Recall named TOOL-aNimbleMend-20 and
the two units above.

Recall terms used: `policy fixtures guard census guard-trace leg guard gate-legs enforcer imports
budgets-reader-refused recall-export check 8 CODEX_MAX`
