# TOOL-dSafePassage-103 — the census tree reads gov's source-mode receipt as gov's own tree, by the registry search it makes with no receipt

**Status:** CLOSED · rev-2 · 2026-11-01 · node a · Tier-2 · base f25d719e4 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-97 TOOL-dSafePassage-98 TOOL-dSafePassage-99 TOOL-dSafePassage-100 TOOL-dSafePassage-101 TOOL-dSafePassage-102 |
| [2026-11-01-build-TOOL-dSafePassage-103-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-103-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-103-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-103-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-103-2-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-103-2-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-103-audit-fold-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-103-audit-fold-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dSafePassage-103-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-103-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-103-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-103-spec-brief.md) | research | — |
| [2026-11-01-review-TOOL-dSafePassage-103-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-103-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-8 makes every landing write gov's source-mode receipt, a `.governance/install.json`
whose top-level `"mode"` is `"source"`. `derive_census_tree` in `tools/policy/policy.py` reads any
receipt as an adopter's. So on gov's own tree the cap census grades four rows at installed paths gov
does not hold, and the legacy-homes arm stops grading. This unit makes a source-mode receipt answer
the registry search the function already makes when no receipt exists. An adopter's receipt reads
exactly as before.

## 2. Scope (IN)

- **S1 — the source branch.** In `derive_census_tree`, a receipt that parses as a JSON object and
  whose `"mode"` equals `"source"` answers the registry search, per §4 "The change". The search
  moves out of the no-receipt branch, policy.py lines 1054-1061, into one new function,
  `derive_registry_tree`. Both branches call it. The new branch sits after the object check, lines
  1068-1069, and before the `kits` and `prefix` checks, lines 1070-1074. Observed by AC1, AC2, AC3
  and AC4.
- **S2 — a source-mode receipt with no registry is refused.** Where the receipt says source mode and
  the search finds no registry, the function raises a Refusal naming the receipt. It never answers
  `unadopted`. Two or more registries raise the search's existing Refusal, as they do with no
  receipt. Observed by AC5.
- **S3 — the regression case.** `tools/policy/check_policy.py` gains one outcome case,
  `census-source-receipt`, in `CASES` after `census-window-edge` (line 4411), run by a new
  `run_census_source_receipt`. It runs the four checks §4 "The regression case" lists. Observed by
  AC3, AC4 and AC5.
- **S4 — the docs that state the old rule.** The class is every line in `tools/policy/README.md`,
  `tools/policy/policy.py` and `tools/policy/check_policy.py` that ties an install receipt to the
  adopter reading or to `not graded`, that lists the derivation's Refusal causes, or that places the
  registry search in `derive_census_tree`. Ten sites hold it, per the table below. Each gains the
  source-mode exception, the S2 refusal or the new function's name, as its row says. Observed by AC6.

  | Site | What it says today | It gains |
  |---|---|---|
  | `derive_census_tree` docstring, policy.py lines 1044-1050 | any receipt answers `adopter` | the source-mode exception and the S2 refusal |
  | WHERE IT INSTALLS paragraph, check_policy.py lines 146-150 | a tree with a receipt is read as an adopter | the source-mode exception |
  | `arm_legacy_homes` docstring, check_policy.py lines 394-402 | the one finding is "a receipt that does not read, or two registries" (lines 401-402) | the source-mode exception, and S2's refusal among the causes |
  | `arm_cap_census` docstring, check_policy.py lines 659-672 | the same cause list (line 672) | S2's refusal among the causes |
  | `seed_ambiguous_registry` docstring, check_policy.py line 3621 | the window `derive_census_tree` searches | `derive_registry_tree` as the function holding the search |
  | README line 23, the `policy.py` row of the module table | lists `derive_census_tree` alone | `derive_registry_tree` beside it |
  | README lines 170-178 | the arm says `not graded` wherever the tree holds a receipt (line 174) | the source-mode exception |
  | README line 650, the `arm_legacy_homes` row | `not graded` "in any tree holding an install receipt" | the source-mode exception, written in place of that phrase |
  | README line 653, the `arm_cap_census` row | the receipt makes the target an adopter | the source-mode exception and the S2 refusal |
  | README census-case paragraphs, lines 539-550 | no paragraph for the new case | one paragraph for `census-source-receipt` |

  Each site that gains the exception or S2's refusal spells it with the word `source-mode`, which
  AC6 greps. No site spells it so today.

  The predicate `git grep -n -i 'install receipt\|install.json' -- tools/policy/`, run at
  `bacc82c20`, also returns lines that stay unchanged. They are the inlined `resolve_kit_dir` blocks
  (`tools/policy/adopt-policy.sh` 122 and 134, `tools/policy/policy-shim.sh` 140 and 152, policy.py
  1136 and 1148), which follow a receipt row's `path` and never read the tree as an adopter. They
  are also the `kits` comment at `tools/policy/caps.toml` line 25, the receipt's read, parse and
  object Refusal strings (policy.py 1063, 1067 and 1069), the `invalid` finding string
  (check_policy.py 683) and the fixture reader's docstring (check_policy.py 1193). None of these
  states the adopter rule.
- **S5 — no other reader changes.** §4 "The class" lists every reader of the receipt the predicate
  returns. Only `derive_census_tree` is shown misreading it, so only `tools/policy/policy.py`,
  `tools/policy/check_policy.py` and `tools/policy/README.md` change under the tool root. Observed by
  AC7.

## 3. Non-goals (OUT)

- Any change to govkit's source-mode update (`tools/govkit/govkit.py` lines 9414-9455) or to the
  receipt's shape. The brief rules both out.
- Any change to `arm_cap_census`, `arm_legacy_homes`, `check_legacy_graded` or `cmd_lists`. All four
  read the tree through `derive_census_tree`, so S1 corrects them without an edit.
- Any change to another reader of the receipt, including the memory-tree selftest that copies gov's
  receipt into its fixtures (§4 "What it does not cover").
- A version bump of the policy kit. The lander mints it into the prepared merge, so a branch owes
  none (`tools/govkit/govkit.py` lines 13845-13850).
- A help page. No page under `help/` describes the source tree's reading. `help/size-caps.md` lines
  88-95 describe the adopter's reading, which does not change.
- Any edit to a CLOSED spec, including TOOL-dSafePassage-8's, and a `RUN.md` row.

### Edges

- **consumes-from** `TOOL-dSafePassage-8` — the source-mode receipt its `govkit update` writes on
  gov's tree (govkit.py lines 9445-9447), whose top-level `"mode"` S1 reads. Without that key this
  unit could not tell gov's receipt from an adopter's.
- **consumes-from** external — the main loop's runs of the `policy check` leg's checker on the AC1
  fixture, and of the `policy fixtures` case. Scratch-guard row G1 refuses a leg's argv to a role
  whose allowlist does not name that leg (`tools/hooks/README.md` line 518). Without those runs, AC1
  to AC5 have no observation.
- **hands-off** external — observing the 73 selftest legs the close held on a tree carrying gov's
  receipt, per §4 "What it does not cover". That needs a selftest run on such a tree, which no unit
  of this build owns.

## 4. Design

Every line cited here was read at `f25d719e4`, the HEAD this spec was written at, on 2026-11-01 on
node a. rev-2 re-read every cited line at `bacc82c20`. `git diff --stat f25d719e4 bacc82c20 -- tools/
.githooks/` prints nothing, so the line numbers hold there too. The bar log is the close's run on the prepared landing merge `f14f0f72c`, saved at
`C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/close-f14f0f72c.log`. That merge was local-only
and has been reset. Its policy-check output reproduces at HEAD on the fixture AC1 names, by the probe
§4 "The finding, reproduced" records.

### Where the red comes from

The close's bar reds `policy check` on `arm_cap_census` (log lines 150-175). The arm prints 8
announced rows and four findings: `manifest-bytes`, `manifest-line`, `manifest-trap` and
`orientation-card`. Each finding reads "its enforcer is not a file at tools/manifest-check.sh, where
kit kickoff-manifest installs it". On main at `f4597719e` the same arm prints `0 finding(s)` with
`0 announced`, and `arm_legacy_homes` prints `115 row(s) derived from the legacy homes`. Both are read
from the saved run `C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/policy-main.txt`, lines 9 and
13.

The chain runs as follows:

1. The lander's `run_gov_first` runs `govkit.py update --target "$top" --write`
   (`tools/push-main.sh` line 1009). On gov's own tree that is source mode (govkit.py line 9414).
2. Source mode writes a receipt with `"mode": "source"`, `"prefix"` from gov's deploy file, and
   `"kits"` from that file's list (govkit.py lines 9445-9447). Gov's `.governance/deploy.toml` lists
   `kickoff-manifest` among its kits.
3. `derive_census_tree` finds a receipt, so it never reaches the registry search at lines
   1053-1061. It checks the receipt's `kits` and `prefix` and returns `("adopter", receipt)` at line
   1075.
4. `arm_cap_census` therefore takes its adopter branch (`tools/policy/check_policy.py` lines
   689-697). It announces the seven `ships = false` rows and `line-length`, whose kit gov's deploy
   file does not list. It grades each other row at its `installed` path under prefix `tools`. The
   kickoff-manifest kit's four rows install at a path gov does not hold, because gov keeps that
   enforcer under `skills/session-kickoff/`.
5. `check_legacy_graded` answers false wherever the tree is `adopter` (policy.py line 1093). So
   `arm_legacy_homes` prints `not graded` (log line 159) and grades none of the 115 rows it grades
   on main. That loss does not red the bar, because the arm announces it.

The no-receipt rule was designed when gov's tree held no receipt. TOOL-dGroundRules-22 S2 records
"`source` when the tree under test holds no `.governance/install.json`"
(`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-22.md` line 41).
TOOL-dSafePassage-8 removed that premise, and no unit carried the census forward.

### The finding, reproduced

On 2026-11-01 this spec's author cloned `f25d719e4` into a scratch directory with `core.longpaths`
on. From the clone's root, `python tools/govkit/govkit.py update --target . --write` printed
`231 file row(s) recorded, never graded` and exited 0. It left `.governance/install.json` untracked with
`"mode": "source"` and the 22 kits of gov's deploy file. Over that clone, `derive_census_tree`
answered `adopter`, and `check_legacy_graded(clone, "tools/policy")` answered `False`. The registry
search over the same clone finds exactly `tools/govkit/registry.toml`, so after S1 the function
answers `("source", "tools")`. A receiptless tree holding the same registry answered `source` and
`True` in the same probe. The author did not run the `policy check` leg's checker, because the role
may run no gate. AC1 is that run.

### The class: every reader of the receipt

The brief's predicate is `git grep -n install.json -- 'tools/*.py'`. At `f25d719e4` it returns 34
files. 23 of them carry the inlined `resolve_kit_dir` block. The other 11 read the receipt
directly. `policy.py` also reads the receipt through `RECEIPT_REL` (line 1038), so the census tree's
three callers join the population.

| Reader | Branches adopter against source? | Handles `"mode": "source"`? | Evidence | Verdict |
|---|---|---|---|---|
| `derive_census_tree` (policy.py 1043-1075) | yes, on whether a receipt exists | no | log line 171 and the probe above | fixed by S1 |
| `check_legacy_graded` (policy.py 1087-1093), and through it `arm_legacy_homes` (check_policy.py 404) and `cmd_lists` (policy.py 1444) | yes, via the census tree | no | log line 159 against `policy-main.txt` line 9 | fixed by S1, no edit |
| `arm_cap_census` (check_policy.py 679) | yes, via the census tree | no | log lines 163-175 | fixed by S1, no edit |
| `derive_source_rows` (`tools/run-gates/check-receipt.py` 162-171) | yes, on the mode | yes, line 170 | TOOL-dSafePassage-8 S6 | none |
| govkit's `_cmd_update` (govkit.py 9414-9427) | yes, on path identity | yes, it refuses a non-source receipt on gov's tree (line 9425) | read | none |
| `read_down_population` (`tools/lib/python_floor.py` 313-319) | yes, on path identity (`target == gov`) | not read on gov's tree | read | none |
| `resolve_kit_dir` (`tools/lib/resolve_kit_dir.py` 15-50) and its 22 inlined copies the predicate returns | no | not needed | it follows a row only where the row's `path` is a file inside the tree (line 43), else it probes | none |
| the adopter-owned join (`tools/settings-merge.py` 360-385) | no | not needed | gov's deploy file declares no owned row, so no join forms and the hook path returns unchanged (line 374) | none |
| `receipt_schema_4.py` `main` (`tools/govkit/steps/receipt_schema_4.py` 87) | no | not needed | the walk on the fixture clone skipped it as `witness holds` | none |
| `map_from_receipt` (`tools/govkit/census.py` 122) | no | not needed | it reads an adopter checkout the operator names | none |
| the upgrade-step readers in `tools/govkit/upgrade_steps.py` (`derive_pending_steps` 1886, `check_gov_first` 2121) | consume source mode by design | yes | TOOL-dSafePassage-8 S1, S2 | none |
| `step_gate.py` 626-634 | writes a source receipt into its own fixture clone | yes | read | none |
| fixture and suite readers: `check_policy.py` 1194, 1249, 1409, 1438; `tools/govkit/selftest.py`, `matrix.py`, `fixtures/retired_edits.py`, `refusal_join.py`, `upgrade_walk.py`; `tools/roles/render_agents.py` 582 | no, each reads a scratch target it builds | not needed | read | none |

The bar is the empirical half of the predicate. At `f14f0f72c`, 75 legs ran and 3 failed (log line
191). `kickoff-manifest ratchet` names watched files with no re-stamp (log lines 52-62).
`spec tokens` names the packet's byte compare (log line 148). Neither message names the receipt.
`policy check` is the only red that does. Shell and JavaScript readers fall outside the brief's
`.py` predicate. Every leg that ran their checkers on the same tree passed.

### The change

`receipt.get("mode") == "source"` is the exact test govkit's writer uses (govkit.py line 9425) and
check-receipt uses (line 170). An adopter receipt carries no top-level `mode`. The `mode` keys at
govkit.py lines 7574 and 7656 are fields of file rows, not of the receipt.

```python
def derive_registry_tree(repo):
    """-> ("source", <d>) where exactly one REGISTRY_REL sits under a <d> 0 to 2 deep,
    ("unadopted", None) where none does; two or more is a Refusal naming each candidate.
    Lines 1054-1061 today, moved verbatim, `from None` kept on the Refusal."""

def derive_census_tree(repo):
    try:
        text = Path(repo, RECEIPT_REL).read_text(encoding="utf-8")
    except FileNotFoundError:
        return derive_registry_tree(repo)
    ...                                    # the read, parse and object checks, unchanged
    if receipt.get("mode") == "source":    # TOOL-dSafePassage-103 S1: gov's own receipt
        tree = derive_registry_tree(repo)
        if tree[0] == "unadopted":         # S2
            raise Refusal(RECEIPT_REL, 0, f"a source-mode receipt in a tree holding no {REGISTRY_REL} "
                          "0 to 2 deep, so it is neither gov's tree nor an adopter's")
        return tree
    ...                                    # the kits and prefix checks and the adopter answer, unchanged
```

The source branch sits before the `kits` and `prefix` checks because a source answer reads neither
field. A source receipt's `prefix` is gov's tool root and its `kits` is gov's list, so neither
field is the one the census needs. The registry search derives the tool root, as it does with no
receipt.

### The regression case

`run_census_source_receipt(name)` follows `run_census_window_edge` (check_policy.py line 4193). It
builds one scratch repository with `run_fixture_git(t, "init", "-q")`. It writes a copy of the
source's registry at this kit's tool root, the path `derive_window_edge_paths` writes first. It
writes a receipt at `RECEIPT_REL` carrying `"schema": 4`, `"mode": "source"`, `"gov_source": "."`,
this kit's tool root as `"prefix"`, `ADOPTER_KITS` as `"kits"` and an empty `"files"`. Those are the
keys govkit's writer sets (govkit.py lines 9445-9447). It then prints one `policy-fixture:` line per
check through `print_checks`. The scenarios run in this order over the one repository:

| Scenario label | Tree | Expected |
|---|---|---|
| `source-mode receipt` | registry and source receipt | `derive_census_tree` answers `("source", budgets.derive_tool_root())`, and `check_legacy_graded(t, KIT)` answers `True` |
| `adopter receipt` | the same receipt with its `"mode"` key removed | the first element answers `adopter`, and `check_legacy_graded(t, KIT)` answers `False` |
| `no registry` | the source receipt with the registry deleted | a Refusal whose path is `RECEIPT_REL` |
| `source-mode receipt, two registries` | the source receipt, the registry rewritten at `written[0]`, and a copy at `planted`, both from `derive_window_edge_paths` (check_policy.py lines 4183-4190) | a Refusal whose path is `", ".join(sorted((written[0], planted)))`, not `RECEIPT_REL` |

The fourth scenario observes S2's promise that two or more registries raise the search's existing
Refusal. `planted` is a registry two deep, inside the search window, as in `run_census_window_edge`.
A build that re-raised S2's message, or answered from the receipt's `prefix`, reds that line.

Every scenario calls `derive_census_tree` and `check_legacy_graded` through one wrapper, as
`run_census_window_edge`'s `ask()` does (check_policy.py lines 4203-4207). The wrapper turns a
`policy.Refusal` into the value `refused <path>`. The scenario compares that value with its expected
result and prints `WRONG` on a mismatch. Without it, a Refusal in the first two scenarios would
propagate: `check_legacy_graded` leaves a Refusal to its caller (policy.py lines 1087-1093), and
`run_fixture`'s outcome-case loop (check_policy.py lines 4483-4487) catches nothing, so the run
would end in a traceback before the remaining checks. The case also catches
`subprocess.CalledProcessError` and `OSError` as its sibling does, and it removes the repository in
a `finally`. Its source reads are the registry and this kit's `legacy-homes.txt`.
Both sit inside the `policy fixtures` guard, so the guard trace stays green.

### What it does not cover

- **The selftest legs the close held.** 73 legs did not run at `f14f0f72c`, because
  `GATE_SELFTESTS` was unset (log line 191). One of them reads gov's receipt: the memory-tree
  selftest copies the source tree's receipt into each fixture it builds, where one exists
  (`tools/memory-tree/row_grammar.py` lines 2569-2580). Whether a source-mode receipt changes that
  suite's verdict is unobserved. The brief fixes only readers the bar or a probe shows misreading the
  receipt, and neither shows this one, so it is handed off.
- **Readers outside the predicate.** Shell and JavaScript readers of the receipt are not in the
  table. The legs that ran them at `f14f0f72c` passed, which is the only evidence about them.
- **A forged source-mode receipt in an adopter that also plants a registry.** It reads as source, and
  each row is graded at its `enforcer` path. It turns nothing green that the plant does not already
  hold, but S2 does not refuse it.

### Inventory

Minted: one function `derive_registry_tree` in `tools/policy/policy.py`. One function
`run_census_source_receipt` and one case name `census-source-receipt` in
`tools/policy/check_policy.py`. One Refusal message. Both functions sit in the lexicon's
`py.function snake` cell (`.lexicon.conf` line 581). Their verbs, `derive` and `run`, are declared
at lines 644 and 647. No file, flag, conf key, gate leg or receipt field is minted.

Both new functions enter the codebase map's symbol tier. That tier is rendered into
`memory/map/generated/symbols.json`, which today holds `derive_census_tree` and
`run_census_window_edge`. The builder regenerates it with `python tools/codebase-map/gen_map.py
--write`, the command `map_lib.regen_cmd` spells (`tools/codebase-map/map_lib.py` lines 149-153). The
`codebase-map coverage + freshness` leg compares that file byte for byte with a fresh render. So does
the pre-commit hook on any staged `.py` change (`.githooks/pre-commit` lines 264-293).

### Migration

None. The receipt's shape is unchanged, and no adopter receipt carries a top-level `mode`.

### Rollout

Live at landing, at order 16. It must land in the same merge as the first gov-first receipt, or the
landing's own bar reds `policy check` as `f14f0f72c` did.

### Files touched (estimate)

- `tools/policy/policy.py` — S1 and S2, and the `derive_census_tree` docstring of S4.
- `tools/policy/check_policy.py` — S3, and the four docstrings of S4: WHERE IT INSTALLS,
  `arm_legacy_homes`, `arm_cap_census` and `seed_ambiguous_registry`.
- `tools/policy/README.md` — the five README sites of S4.
- `memory/map/generated/symbols.json` — regenerated for the two new functions, per §4 "Inventory".
- The unit's acceptance ledger, under the build's own build-records folder.

### Alternatives rejected

- **Answering `unadopted` for a source-mode receipt with no registry.** That is the search's own
  zero answer. It would announce every row and grade none on a tree whose receipt claims to be gov's,
  a silent pass. The function already refuses a receipt that is not an object rather than guess a
  `source` answer (policy.py line 1049), and the charter's security rule denies by default. So S2
  refuses.
- **Reading `gov_source == "."` or the `prefix` instead of `mode`.** govkit's writer and
  check-receipt both key on `mode` (govkit.py line 9425, check-receipt.py line 170). A second key
  would be a second spelling of one fact.
- **Removing the receipt before the bar, or ignoring the file in the lander.** It changes govkit's
  source-mode flow, which §3 rules out, and it leaves the census wrong on any tree that carries the
  receipt.
- **Branching on mode inside `arm_cap_census` and `check_legacy_graded`.** That is two guards where
  one in the shared function covers every caller, `cmd_lists` included.
- **Copying the search into the new branch.** That is a second copy of seven lines. One function
  both branches call is the extraction the charter's reuse rule asks for at a second instance.

## 5. Production-readiness checklist

- security: S2 refuses a source-mode receipt that no registry backs, rather than reading it as
  unadopted. No write path or surface is added.
- perf / scale: N/A — one dictionary lookup per call. The search is the one the receiptless branch
  already makes.
- error / empty / loading states: a source-mode receipt with no registry is a Refusal naming the
  receipt (S2). Two registries are the search's existing Refusal. Both callers report a Refusal as
  their one finding (check_policy.py lines 405-406 and 680-681).
- observability: on gov's tree the census reads 0 announced again, and `arm_legacy_homes` prints its
  derived row count instead of `not graded`.
- risks: the 73 held selftest legs are unobserved on a receipt-carrying tree (§4 "What it does not
  cover").
- testing: AC1 to AC7, and the new case under the `policy fixtures` leg.
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` describes the source tree's census, checked with `git grep`
  on 2026-11-01. `help/size-caps.md` describes the adopter's reading, which is unchanged.

## 6. Acceptance criteria

- **AC1** — When `python tools/policy/check_policy.py` runs from the root of the fixture clone at the
  build commit, the line opening `policy-check: arm_cap_census ·` reads `0 finding(s)` and
  `0 announced`, as on main at `f4597719e`. It prints no `cap census:` line.
  Red when: the census reads gov's receipt as an adopter's. At `f14f0f72c` the leg printed (log lines
  163-175):
  ```
  cap census: line-length · kit check-line-length not installed
  policy-check: arm_cap_census · 4 finding(s) · 33 census row(s) joined to their enforcers and cases, 8 announced · 12 request(s) in 192 tracked code file(s) · 7 row(s) of tools/template-size-limits.txt
    manifest-bytes: its enforcer is not a file at tools/manifest-check.sh, where kit kickoff-manifest installs it
    manifest-line: its enforcer is not a file at tools/manifest-check.sh, where kit kickoff-manifest installs it
    manifest-trap: its enforcer is not a file at tools/manifest-check.sh, where kit kickoff-manifest installs it
    orientation-card: its enforcer is not a file at tools/manifest-check.sh, where kit kickoff-manifest installs it
  ```
  The same leg printed seven `enforcer not shipped` lines above those.
  fixture: a clone of the build commit, with `core.longpaths` on under Windows. From its root,
  `python tools/govkit/govkit.py update --target . --write` writes gov's receipt as the lander does.
  On 2026-11-01 at `f25d719e4` that wrote the receipt untracked and exited 0.
  figure: `0 finding(s)` and `0 announced` are PINNED from main's run at `f4597719e`.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name the
  `policy check` leg.
- **AC2** — When the AC1 run is made, its line opening `policy-check: arm_legacy_homes ·` names
  `row(s) derived from the legacy homes` and does not read `not graded`.
  Red when: `check_legacy_graded` still reads the tree as an adopter's. At `f14f0f72c` the same run
  printed
  `policy-check: arm_legacy_homes · not graded · the list is gov's own and is withheld from installs; …`,
  beside the `arm_cap_census` line AC1 quotes. Main at `f4597719e` printed `115 row(s)`
  there.
  fixture: the AC1 clone.
  permission: as AC1.
- **AC3** — When `python tools/policy/check_policy.py --fixture census-source-receipt` runs from the
  repository root at the build commit, its `source-mode receipt` line carries no `WRONG`.
  Red when: S1's branch is absent. On 2026-11-01 at `f25d719e4`, without S1, a probe built this
  check's tree, a registry beside a source-mode receipt, and called both functions on it.
  `derive_census_tree` answered `adopter` and `check_legacy_graded` answered `False`, the reading
  behind the `arm_cap_census` line AC1 quotes. The main loop observes the case RED with S1 reverted
  and GREEN at the build commit.
  permission: G1 refuses the `policy fixtures` leg's argv to a role. This one-case argv is not that
  leg's argv, so it is UNVERIFIED whether G1 refuses it.
- **AC4** — When the AC3 run is made, its `adopter receipt` line carries no `WRONG`.
  Red when: S1 keys on something every receipt carries, such as `prefix`. The adopter receipt then
  reads as source, and an adopter's census grades each row at its `enforcer` path. That is the
  converse of the `arm_cap_census` line AC1 quotes.
- **AC5** — When the AC3 run is made, its `no registry` line and its
  `source-mode receipt, two registries` line carry no `WRONG`, and the run's last line reads
  `policy-fixture: <n> assertion(s) executed · 0 wrong`. The run exits 0.
  Red when: S2 is absent. A source-mode receipt with no registry then answers `unadopted`, and every
  census row is announced and none graded. That is a silent version of the `arm_cap_census` line AC1
  quotes, with no finding at all. The second line reds when the two-registry tree ends anywhere but
  the search's own Refusal, such as S2's message naming `RECEIPT_REL` or a `source` answer read from
  the receipt's `prefix`.
  figure: `<n>` is DERIVED by the run, the case's four checks plus the guard trace's.
- **AC6** — When these five probes run at the build commit, each prints what its clause names. At
  `bacc82c20` the second, third and fifth probes print nothing, and the fourth prints README line 650,
  so each clause can fail.
  1. `git grep -c census-source-receipt -- tools/policy/README.md tools/policy/check_policy.py`
     prints both files, each with a count of 1 or more.
  2. `git grep -n -e "source-mode" -- tools/policy/README.md` prints the lines that replace README
     lines 174, 650 and 653.
  3. `git grep -n -e "source-mode" -- tools/policy/policy.py tools/policy/check_policy.py` prints one
     line inside the `derive_census_tree` docstring. It also prints one line inside each of three
     check_policy.py docstring passages: the WHERE IT INSTALLS paragraph, the `arm_legacy_homes`
     docstring and the `arm_cap_census` docstring.
  4. `git grep -n "any tree holding an install receipt" -- tools/policy/README.md` prints nothing.
  5. `git grep -n derive_registry_tree -- tools/policy/README.md tools/policy/check_policy.py` prints
     the README's `policy.py` module-table row and a line inside the `seed_ambiguous_registry`
     docstring.
  Red when: a doc still says any receipt makes the tree an adopter, a Refusal-cause list leaves out
  S2's refusal, or the module table or the window docstring leaves out the function that now holds
  the search. The `arm_cap_census` line AC1 quotes is the old rule's output on gov's tree.
- **AC7** — When `git show --name-only --format= HEAD -- tools/` runs at the build commit, it prints
  exactly these three lines:
  ```
  tools/policy/README.md
  tools/policy/check_policy.py
  tools/policy/policy.py
  ```
  Red when: another receipt reader is edited, such as check-receipt or a resolver copy. The bar names
  only the `arm_cap_census` line AC1 quotes, and no other reader is shown misreading.
  fixture: the build lands as one commit under the tool root.

## 7. Gates

`policy check` · `policy fixtures` · `memory hygiene` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py --fixture · covers AC3 AC4 AC5 · `census-source-receipt` plants a source-mode receipt beside one registry, removes its mode key, deletes the registry, then plants two registries, in one scratch repository · none

The branch's `policy check` leg cannot observe S1 or S2. The branch tracks no
`.governance/install.json` (`git ls-files .governance` lists `deploy.toml`, `policy.json` and
`policy.toml`), so `derive_census_tree` takes the receiptless path to the registry search
(policy.py lines 1054-1061) with or without S1, and the leg prints the same either way. Only two
observations of that checker can go red for this change. One is AC1's run on the fixture clone,
where `govkit update --target . --write` writes the receipt. The other is the prepare's bar on the
landing merge, which carries the receipt as `f14f0f72c` did. On the branch, `policy fixtures` is
the gate that observes the change, because it runs the new `census-source-receipt` case.

The legs the estimate trips were derived by matching each backticked Files-touched path against the
guards in `tools/gate-legs.json`. `policy fixtures` is tripped by the narrow `tools/policy/` guard,
carried by one leg. `recall floor` and `recall floor arms` are tripped by the `memory/` guard,
carried by those two legs, through `memory/map/generated/symbols.json`, the acceptance ledger and
this spec. Every other leg the estimate trips is reached only through the broad `tools/` guard,
carried by 12 legs. `codebase-map coverage + freshness` and `memory hygiene` carry no guard and run
on every bar. The first compares the regenerated `symbols.json` with a fresh render. The second
grades this spec and its ledger. The fixture suite pins no assertion count, so no floor moves.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-103-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-103-spec-brief.md`.
  The brief's finding: the close's bar on the prepared landing merge `f14f0f72c` reds `policy check`
  on `arm_cap_census`, with four findings and 8 rows announced. `manifest-bytes`, `manifest-line`,
  `manifest-trap` and `orientation-card` each read "its enforcer is not a file at
  tools/manifest-check.sh, where kit kickoff-manifest installs it". The same leg reads 0 findings and
  0 announced at main `f4597719e`. TOOL-dSafePassage-8 makes the landing's govkit update write gov's
  source-mode receipt, and the prepare's merge carries it. It is the first landing that does, and the
  receipt is absent at `60d90cb71`, `f4597719e` and `37b3bf328`. `policy.derive_census_tree`
  (`tools/policy/policy.py` line 1043) answers `("adopter", receipt)` for any receipt. Adopted under
  UNATTENDED-PROTOCOL §11: a measured red at the landing, with nothing this repo measures getting
  worse. This draft adds the second misreading the same log shows, `arm_legacy_homes` reading
  `not graded` (log line 159), which S1 corrects with no further edit. S2's refusal is derived from the
  function's own refusal of a non-object receipt and from the charter's deny-by-default rule, as §4
  "Alternatives rejected" states. Every cited line was read at `f25d719e4`.
- rev-2 · 2026-11-01 · S3 · S4 · §4 · AC5 · AC6 · §7 · folded the round-1 spec audit
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-103-spec-audit-round1.md`
  (CLEAN WITH FIXES, 2 medium and 7 low) under its brief
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-103-audit-fold-brief.md`.
  M1, M2, L1 and L5 widened S4 to a named class of ten doc sites and AC6 to five probes that each fail
  at `bacc82c20`. L2 and L4 rewrote §7 to declare the branch's `policy check` leg blind to S1 and to
  add `recall floor` and `recall floor arms`. L3 added `memory/map/generated/symbols.json` to Files
  touched, its regen to §4 "Inventory" and `codebase-map coverage + freshness` to §7. L6 added the
  `source-mode receipt, two registries` scenario at the skeptic's corrected fix, bound to AC5. L7
  routed every scenario through a Refusal-to-value wrapper. Every line cited was re-read at
  `bacc82c20`.

## 10. Reuse audit

The seam this unit extends is `derive_census_tree` in `tools/policy/policy.py`, the one function
the census arm, the legacy-homes arm and `lists` all read the tree through. Its registry search,
lines 1054-1061, is the second-instance extraction S1 makes. The task names `tools/govkit/`,
`tools/lib/` and `tools/push-main.sh` as seams. None of them changes: govkit's writer already marks
the receipt, `tools/lib/resolve_kit_dir.py` does not branch on adopter against source, and the
lander only runs the writer.

`python tools/codebase-map/reuse_lookup.py "read a source-mode install receipt as gov's own tree by the registry search, not as an adopter"`
ranked name-stem neighbours only: `read_text`, `read`, `tree` and `search` as SEAMs with fan-in 149,
140, 129 and 69, and `load_registry` and `read_descriptors` in `tools/govkit/govkit.py` with fan-in
3. None fits. Each reads bytes or govkit's registry for the deployer, and none answers which tree the
policy kit grades. The recall probe ranked TOOL-dSafePassage-8 first, the unit that introduced the receipt. It
ranked TOOL-dGroundRules-29 and TOOL-dGroundRules-22 next, the units that wrote the census tree and
its "no receipt means source" premise, and TOOL-dGroundRules-22's ledger, whose AC2 observed
`0 announced` on gov's tree when gov held no receipt.

Recall terms used: `python tools/memory-recall/query.py "the census tree reads gov's source-mode receipt as an adopter, so the cap census grades installed paths on gov's own tree" --terms "derive_census_tree source-mode receipt mode source adopter registry census check_legacy_graded arm_cap_census installed enforcer"`
