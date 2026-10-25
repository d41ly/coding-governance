# TOOL-dGroundRules-77 — guard plants reach the text-shape, key-scope and not-a-count refusals

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-77-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-77-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-77-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-77-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md](../reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md) | diff-review | TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-78 TOOL-dGroundRules-79 |

<!-- /gen:spec-records -->

## 1. Goal

Three refusals of the minimal guard have no fixture plant that reaches them. They are the text-shape
refusal, the key-scope refusal and the not-a-count refusal in `check_raise_shape`
(`tools/policy/guard.py`). With the text-shape condition switched off, the guard admits an argued
raise beside a rewritten comment line, and every `guard-*` case stays green. That is finding M3
(id 10) of the closing diff review, round 1. This unit adds three `GUARD_PLANTS` rows, one per
refusal, each reaching its refusal alone, and gives the fixture's policy file the runtime row the
key-scope plant needs.

## 2. Scope (IN)

- **S1** — The plants. In `tools/policy/check_policy.py`, `GUARD_POLICY` gains a leading `[runtime]`
  table holding `agents-in-flight = 4`, and a constant `FLIGHT` names that row. `GUARD_PLANTS`
  gains `guard-other-line`, `guard-not-budgets` and `guard-not-a-count`, and the `guard-new-row`
  needle gains the table its added key lands in. The comment above `GUARD_POLICY`, the module
  docstring's `guard-*` paragraph and `build_guard_repo`'s docstring say the fixture's policy file
  now holds the runtime table. §4 "The rows" gives every line. Observed by AC1, AC2, AC3, AC4
  and AC5.
- **S2** — The kit page. In `tools/policy/README.md`, the `guard-*` paragraph counts twenty-one
  cases, says the policy file holds the runtime table, and names the three new cases in its exit-1
  list. Observed by AC5 and AC6.

## 3. Non-goals (OUT)

- `tools/policy/guard.py`. Its three refusals are correct today, and this unit only grades them.
- The `policy fixtures` budget row in `tools/run-gates/selftest-budgets.txt` and the leg's ceiling
  in `tools/gate-legs.json`. Finding M4 owns those, in unit `TOOL-dGroundRules-78`, and its
  re-measure counts the three cases this unit adds.
- The report's left-shift gate, a reason-string coverage check with a mutation pass (§7).
- Every other finding of the report, every other spec, and the inherited reds the close recorded.

### Edges

none

`TOOL-dGroundRules-75` also edits `tools/policy/check_policy.py`, in other symbols. This spec cites
the file by symbol, and its line numbers are those at `fce5603f`.

## 4. Design

### Evidence

All line numbers are at `fce5603f8`. `check_raise_shape` (`tools/policy/guard.py:141-178`) returns
early when the number of changed keys is not one (`:150-151`), or when a key was added or removed
(`:154-155`). Past those, it collects every failed condition. The key-scope refusal sits at
`:157-158`, the measured-file refusal at `:159-160`, the not-a-count refusal at `:161-163` and the
text-shape refusal at `:172-174`.

None of the three reason strings, "only a cap under budgets.*", "is not a count" and "another line
of the policy file changed", appears in `tools/policy/check_policy.py`. A grep for them and for each
other needle confirms this. `guard-two-raised` and `guard-beside-change` stop at the key count.
`guard-new-row` and `guard-removed-row` stop at the added or removed key. `guard-class-row`
reaches the measured-file refusal and not the key-scope one. No plant stages a string value or a
second text block.

The premise was measured in a scratch copy of the policy kit at `fce5603f8` (§8). With the text-shape
condition staged off (`if False and not (ops and one_block`), all eighteen `guard-*` cases and
`on-invalid-bom`, which writes `GUARD_POLICY` with a BOM, stayed green. So the premise holds.

### The rows

`GUARD_POLICY` and the comment above it become the lines below. The three comment lines before them
are unchanged. `FLIGHT` goes directly below the `BIG, SMALL, CLASS` line:

```
# The [runtime] table leads the file: guard-not-budgets raises its count, which sits outside budgets.*,
# and a row appended at the end, as guard-new-row's is, still lands under [budgets] (TOOL-dGroundRules-77).
GUARD_POLICY = f'[runtime]\nagents-in-flight = 4\n\n[budgets]\n"{BIG_FILE}" = 100\n"small.md" = 50\n"memory/builds/*/spec/" = 10\n'
FLIGHT = "agents-in-flight = 4\n"
```

`agents-in-flight` is a real catalogue key, `runtime.agents-in-flight` (`tools/policy/catalogue.toml:478`),
so the mirror cases render a valid file. The guard reads no catalogue.

The `guard-new-row` needle becomes `'a key was added: budgets."new.md"'`, and the three rows below
go after `guard-removed-row`:

```
    "guard-other-line": [("another line", [RAISED, ROW, (POLICY_REL, lambda t: t.replace(CLASS, CLASS + "# planted\n"))],
                          1, ["another line of the policy file changed"], [])],
    "guard-not-budgets": [("not budgets", [(POLICY_REL, lambda t: t.replace(FLIGHT, "# RAISED 4 -> 6\nagents-in-flight = 6\n")), ROW],
                           1, ["only a cap under budgets.*"], [])],
    "guard-not-a-count": [("not a count", [(POLICY_REL, lambda t: t.replace(SMALL, '"small.md" = "60"\n')), ROW],
                           1, ["is not a count"], [])],
```

Each row reaches its refusal and only that one, because every other condition holds. `guard-other-line`
changes one leaf, argued, with a decision row, and adds a comment line under the class row, which is
a second diff block. `guard-not-budgets` changes one count that grew, in one block with its `RAISED`
line. `guard-not-a-count` changes one leaf to a string in one block, and the `RAISED` test is skipped
when the values are not counts (`guard.py:175`). In the scratch copy, each case printed exactly one
`refused` line.

The new cases need no edit to the case table. It runs every `GUARD_PLANTS` key through
`run_guard_case` (`check_policy.py:4353`), and that function stages each scenario
(`check_policy.py:2445-2453`).

### Where the runtime table sits

The report's fix put the table after `[budgets]`. Measured in the scratch copy, that moves
`guard-new-row`'s appended key under `[runtime]`. The guard then prints `a key was added:
runtime."new.md"`, and the old needle stays green, so the case quietly stops planting a budgets row.
A leading table keeps every existing plant's text and its meaning. The respelled needle makes that
placement something the suite grades. With the table trailing, `guard-new-row` prints `WRONG`.

### What the cases do not check

They do not check that every refusal string in `guard.py` has a needle, or that each condition is
the only thing between a mutant and an admit. Those belong to the left-shift gate in §7. They also
do not check the refusals outside `check_raise_shape`, which other cases already reach.

### The docs

The phrase `runtime table setting agents-in-flight to 4` goes on one line in each of three places.
They are the module docstring's `guard-*` paragraph, after "(TOOL-dGroundRules-21 S22)", as
"beside a runtime table setting agents-in-flight to 4,", and `build_guard_repo`'s docstring, after
the class row's value, as "behind a runtime table setting agents-in-flight to 4,". The third is the
README's `guard-*` paragraph (`tools/policy/README.md:486-496`). That paragraph's "The eighteen"
becomes "The twenty-one", and its exit-1 list ends:
"`guard-new-row`, `guard-removed-row`, `guard-other-line` (a comment line added away from the cap
beside an argued raise), `guard-not-budgets` (`runtime.agents-in-flight` raised with its argument)
and `guard-not-a-count` (a cap set to a string)". No page under `help/` names a `guard-*` case or
`GUARD_PLANTS`. A grep of `help/`, `README.md` and `WIRE-INTO-PROJECT.md` confirmed it.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/README.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. Each runs one case of the
module's own single-case runner, `--fixture <case>` (`check_policy.py:4495-4499`). At `fce5603f8`
the three new case names print `policy-fixture: no case named <case>` and exit 2
(`check_policy.py:4425-4427`). The staged breaks below were measured on a scratch copy of the kit at
`fce5603f8` with S1 applied. Each break goes in the worktree's `tools/policy/guard.py`, the file the
case copies into its fixture, and is reverted after. The whole `policy fixtures` leg is a suite this
pass may not run. The main loop runs it at the close.

- **AC1** — When `python tools/policy/check_policy.py --fixture guard-other-line` runs, its case line starts `policy-fixture: guard-other-line · another line · guard.py --staged · exit 1 · ` and holds `another line of the policy file changed`, and its last line ends `· 0 wrong`.
  Red when: the text-shape condition in `check_raise_shape` is staged off, its `if not (ops and one_block` becoming `if False and not (ops and one_block`. The case line then holds `WRONG: exit 0` and `policy-guard: admitted`.
- **AC2** — When `python tools/policy/check_policy.py --fixture guard-not-budgets` runs, its case line holds `exit 1` and `only a cap under budgets.* may be raised, not runtime.agents-in-flight`, and its last line ends `· 0 wrong`.
  Red when: the key-scope condition in `check_raise_shape` is staged as `if False:`. The case line then holds `WRONG` and `runtime.agents-in-flight is not a measured-file cap`, so the measured-file refusal behind it no longer stands in for the key-scope one.
- **AC3** — When `python tools/policy/check_policy.py --fixture guard-not-a-count` runs, its case line holds `exit 1` and `is not a count: 50 -> `, and its last line ends `· 0 wrong`.
  Red when: the `if not counts:` line in `check_raise_shape` is staged as `if False:`. The case line then holds `WRONG` with stdout `(none)` and a `TypeError` traceback on stderr.
- **AC4** — When `python tools/policy/check_policy.py --fixture guard-new-row` runs, its case line holds `a key was added: budgets."new.md"`, and its last line ends `· 0 wrong`.
  Red when: `GUARD_POLICY` carries the runtime table after `[budgets]`, as the report's fix had it. The case line then holds `WRONG` and `a key was added: runtime."new.md"`.
- **AC5** — When `grep -c "runtime table setting agents-in-flight to 4" tools/policy/check_policy.py tools/policy/README.md` runs, it prints `tools/policy/check_policy.py:2` and `tools/policy/README.md:1`.
  At `fce5603f8` it printed `0` for each.
  Red when: either docstring, or the README, still describes a policy file that holds only the budgets table.
- **AC6** — When `grep -o -F -e "The twenty-one" -e "guard-other-line" -e "guard-not-budgets" -e "guard-not-a-count" tools/policy/README.md` runs, it prints each of the four strings at least once.
  At `fce5603f8` it printed none of them.
  Red when: the README still counts eighteen cases, or its exit-1 list leaves out a new case.

## 6. Gates

`policy fixtures` · `policy check` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

Run through `derive_guarded_legs` at `fce5603f8`, `python tools/check-spec-tokens.py --legs-for`
names one non-broad guarded leg for both touched files, `policy fixtures`, through `tools/policy/`.
Every other leg it prints trips only on the broad `tools/`. Two legs named beside it carry no guard
and read what this unit changes. `policy check` runs `tools/policy/check_policy.py` in its live
mode, which no edit here reaches. `kit epoch` reads the policy kit's shipped bytes, both files among
them, and prints `owed at the lander` for this move.

New arm: tools/policy/check_policy.py --fixture guard-other-line · covers AC1 · the text-shape condition staged off in guard.py, which admits the plant: exit 0 · none
New arm: tools/policy/check_policy.py --fixture guard-not-budgets · covers AC2 · the key-scope condition staged as if False, which leaves only the measured-file refusal · none
New arm: tools/policy/check_policy.py --fixture guard-not-a-count · covers AC3 · the not-a-count condition staged as if False, which crashes on a str-int comparison · none

The `guard-new-row` needle is respelled in place, so it is not a new arm. AC4's staged break reds it.
No floor or pinned count moves. The fixture pins no case count. The budget row's evidence text, "the
fixture's 16 cases", is already stale, and `TOOL-dGroundRules-78` re-measures it. Each new case ran in
about two seconds in the scratch copy.

## 7. Open questions

none

Follow-up, not a fork, for the main loop to file as an ask: the report's left-shift gate. It is a
reason-string coverage check, under which every refusal string in `guard.py` must appear as a needle
in at least one `GUARD_PLANTS` row, plus a mutation pass that deletes each condition and must turn at
least one case red. That means parsing the guard's source and driving mutants, which is a separate
gate and more than one arm of this mechanism.

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing diff review's finding M3 (id 10) and this unit's
  spec brief, grounded at `fce5603f8`. The premise was measured, not run as a suite. The kit was
  copied by `git archive` into a scratch repository, the three plants were applied, and each
  condition of `check_raise_shape` was staged off in turn. Under the text-shape mutant, all eighteen
  existing `guard-*` cases stayed green. Each new case went green on the intact guard and red on its
  own mutant. Takes the skeptic's corrected fix with one grounded change: the runtime table leads
  the file rather than trailing it, because a trailing table moved `guard-new-row`'s planted key out
  of `[budgets]` while its needle stayed green. That case's needle is respelled to grade the
  placement. The brief's leg item names §6, which is this Tier-1 shape's Gates section. The brief,
  untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-77-spec-brief.md
```

## 9. Reuse audit

This unit builds no mechanism. It adds rows to the table the guard's outcome cases already read,
`GUARD_PLANTS` in `tools/policy/check_policy.py`, and reuses its `RAISED`, `ROW`, `SMALL` and
`CLASS` edits. `run_guard_case` runs the rows unchanged.
`python tools/codebase-map/reuse_lookup.py "a guard fixture plant that stages a policy edit and expects a refusal reason"`
ranked only name stems (`refusal`, `fixture`, `Refusal`, `build_fixture`, `run_fixture`), and none of
them stages a guard plant. The seam is `GUARD_PLANTS` itself. The recall probe returned the report's
finding, this unit's brief, the guard's own spec `TOOL-dGroundRules-6` and its backlog row, and no
record of a plant that reaches these refusals.

Recall terms used: `python tools/memory-recall/query.py "guard plants text-shape key-scope not-a-count refusal coverage" --terms "GUARD_PLANTS check_raise_shape another line of the policy file changed only a cap under budgets is not a count"`
