**Serves:** research TOOL-dPavedRoad-4

# Brief: TOOL-dPavedRoad-4's three bar reds

## The brief

### Goal
The merge bar at `d08106d4d` reds on four legs that TOOL-dPavedRoad-4's commit `166c1fef7` moved, each over a pin the base `14320c985` meets exactly. Fix all three causes in one pass of this unit, without changing what the unit grades:

1. **`lexicon naming predicates` and `lexicon wiring`**: verb offenders 1215 against the pin 1211. The four new offenders are this unit's new shell functions, `_al_sbuild` in `tools/memory-tree/check-memory-hygiene.sh` and `pr4_spec`, `pr4_ledger` and `pr4_run` in `tools/memory-tree/check-memory-hygiene.test.sh`. Rename each to a name `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` accepts, and every caller with it; do not raise the pin.
2. **`shell hygiene (a loop fed by a command substitution)`**: the registry `memory/project/substitution-fed-loops.txt` declares 8 here-string sites in `tools/memory-tree/check-memory-hygiene.sh` and the scan measures 9; the count may fall and may not rise. The new site is this unit's `done <<<"$c12_all"`. Feed that loop without a here-string or heredoc over a command-substitution variable, and without a fork (see 3); do not raise the registry count.
3. **`spawn budget (forks per hot entrypoint)`**: `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only memory-hygiene` measures 192 against the ceiling 190, and 190 at base. The main loop's site diff against base puts the two extra forks at the `alspecs=$(git ls-files "$M/builds/*/spec/*.md" ... | _al_sbuild ...)` pipeline, where the function in a pipe costs a subshell the full-mode path did not pay, and at one awk listing in the same check-23 block. Bring the run back to 190 or below, in full mode too; do not raise the ceiling.

`tools/memory-tree/check-memory-hygiene.sh` is on the kickoff manifest's watch list, so the commit bundles the `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` exactly as `e719dff11` and `166c1fef7` did. While in the suite, also restore the space the review found dropped at `tools/memory-tree/check-memory-hygiene.test.sh:4425` (`UNEXERCISEDhere`) and the stale comment at `:919` that still calls the shape arm the only one run under `--staged`.

### Items
1. **TOOL-dPavedRoad-1 — writers self-check spec tokens.** `tools/check-spec-tokens.py --spec <path>` grades that one spec as if it were live, whatever its status, and `tools/roles/house/policy.toml` adds the spec-tokens leg to `gov-spec-writer`'s gates.
2. **TOOL-dPavedRoad-2 — format-guard prints the lines it wants.**
3. **TOOL-dPavedRoad-3 — the handoff carries the brief's prompt.**
4. **TOOL-dPavedRoad-4 — `--staged` grades the staged joins.** `tools/memory-tree/check-memory-hygiene.sh --staged` grades check 12's edge reciprocity and check 23's ledger joins for the staged specs and ledgers only.

### Acceptance
The unit's AC1 to AC6 still hold, observed by the same fixture probes the pass used; `python tools/lexicon/lexicon.py` exits 0; no function this unit added leads with a token outside the VERBS table; the here-string count of `tools/memory-tree/check-memory-hygiene.sh` is 8 or fewer; and the main loop's `fork-count.sh --only memory-hygiene` measures 190 or fewer.

### Gates
`bash tools/run-gates/run-gates.sh`, legs from `tools/gate-legs.json`.

### Non-goals
No change to what any check grades on the full run; no change to the spec-audit policy, the dispatch order gate, the packet regen or the manifest ratchet; no new role; no pin, registry count or ceiling raised.
