# Brief — aNimbleMend: unit 27, the three reds of the close's full bar repaired

**Serves:** research TOOL-aNimbleMend-27

## The prompt

> gates = the full bar once at the close with GATE_FULL=1, without self-tests and without the unattended kit gate leg

The owner's prompt is recorded whole in `memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md`; this unit serves the passage above.

## The brief

### Goal
The close ran the full bar once on the prepared landing merge `b61832752`, and three legs went red. Each red is this build's: the same leg is green at `cac14c195`, the default branch's tip before this build merged. This unit repairs the three so the close's bar can read green. Every spec of the build is CLOSED, so the repair is a new unit on top.

### Items
1. `shell hygiene (a fork spent on builtin work)` reports five findings. Three are product code: `tools/run-gates/pass-legs.sh` holds two `date-fmt` sites, the two `$(date -u ...)` substitutions under its section 5 to 7, and one `path-subst` site, the `$(dirname "$0")` of its `KITDIR` line, and no registry row declares them. Convert each to the no-fork form the leg names, `printf -v v '%(FMT)T' -1` and `${p%/*}`, keeping the bytes each variable held.
2. The other two kinds of finding are counts that rose in three suites this build added arms to, against rows of `memory/project/spawn-idiom-sites.txt`: `tools/run-gates/run-gates.evidence.test.sh` at `var-pipe` declares 43 and measures 72, `tools/run-gates/run-gates.test.sh` at `var-pipe` declares 141 and measures 156, and `tools/workflows/unattended-build.test.sh` at `printf-subst` declares 66 and measures 74. (PINNED, 2026-11-13) The main loop decided these: the three rows are re-declared at the measured counts with a reason naming this build, as the row of `run-gates.evidence.test.sh` at `printf-subst` already does for an earlier reconcile, and an ask files the drain. Converting the sites would owe a whole run of each of the three suites, about two hours of suite time on node a. The spec states this as a decision made, and the registry file is in the unit's write set.
3. `python reads (a name never bound, an import outside its guard)` reports five guards: `tools/memory-tree/backlog.py` is imported and outside the guard of `memory-recall kit selftest`, `recall floor`, `recall floor arms` and `drift-audit selftest`, and `tools/memory-tree/id_grammar.py` outside the guard of `policy fixtures`. Find the import this build added that put each module into those legs' reach, then either add the module to each leg's guard in `tools/gate-legs.json` or remove the reach, and say which and why. A change to that manifest owes `python tools/run-gates/pass_legs.py --apply` and `python tools/run-gates/pass_legs.py --check` after it.
4. `spawn budget (forks per hot entrypoint)` reports two rows of `memory/project/fork-ceilings.txt`: `memory-hygiene` measured 192 against a ceiling of 191, and `manifest-check` 82 against 76. (PINNED, 2026-11-13) This build added check 31 to `tools/memory-tree/check-memory-hygiene.sh` and added lines to `memory/guides/SESSION-KICKOFF.md`, which the `manifest-check` row's fixture copies; `skills/session-kickoff/manifest-check.sh` itself is unchanged by this build. For each row, find the sites that grew with `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only <id> --sites`, then either remove the added forks or raise the row's ceiling to the measured count with its reason, and say which and why. A fork that grades a manifest line this build added is a cost of that line, so a raise is acceptable there; the added fork in the hygiene gate is removed when a builtin form exists.
5. Write the spec at `memory/builds/aNimbleMend/spec/2026-11-13-spec-TOOL-aNimbleMend-27.md`, Tier-1 if the spec format admits a micro-spec for a mechanical repair and Tier-2 otherwise, status SPECCED, order 16, with `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md` as the worked example of a repair unit's shape. Units 1 to 15 are CLOSED and frozen, so declare edges only as `external`, and state each correction in this spec itself.
6. The exact red lines are in the failure record `gate-last-failure.txt` of this worktree's git directory, `C:/projects/coding-governance/.git/worktrees/inline-bar-fixes-pass-legs-1a64f7`. Each acceptance criterion names the leg's own command over the tree, which a builder may run because none of the three is a self-test or a gate runner; a criterion that needs a pass-leg run or the bar is the main loop's, and the spec says so in that criterion.
7. Every spec line stating a figure with a unit carries the word PINNED or a commit sha on the same line. The acceptance section cites no path the unit has not built yet. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it and `python tools/playbook/positional.py check`; do not run the whole-tree memory hygiene, and do not commit.

### Acceptance
- `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` exits 0, and the same command without the two exclusions prints no finding for the three suites.
- `python tools/run-gates/py_reads.py` prints no line opening `py-reads: RED`.
- `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` prints `0 red`.
- `bash tools/run-gates/pass-legs.sh --base <rev>` still writes its run record with a `started` stamp and a run id of the same shape as before the conversion.

### Gates
The full bar once more at the close, with `GATE_FULL=1`, without the self-tests and without the unattended kit gate leg.

### Non-goals
- Draining the three suites' fork idioms, which an ask files.
- Any change to `skills/session-kickoff/manifest-check.sh`.
- Any kit version, which the lander's mint moves.

### Limitations
- A CLOSED spec stays frozen; this unit's spec states each correction itself.
- A pass leg never runs inside a role agent's pass.
- Asks TOOL-aNimbleMend-25 and TOOL-aNimbleMend-26, which the close filed as inherited reds, name two of these three legs; the close compared against a default branch that already held this build. This unit is their cure, and the main loop disposes of them.

### Reuse
- Seams: `tools/run-gates/pass-legs.sh`, `tools/gate-legs.json`, `memory/project/spawn-idiom-sites.txt`, `memory/project/fork-ceilings.txt`, `tools/memory-tree/check-memory-hygiene.sh`, `tools/gate-lint/sh_hygiene.py`, `tools/gate-lint/fork-count.sh`, `tools/run-gates/py_reads.py`.
- The crash witness of `aWitnessedCrash` converted a read to a builtin loop for the same leg, at `796deda7a`.

## Drawn from the session

> gates RED — 3/95 legs failed (79 held: subject kit or chunk selftests, GATE_SELFTESTS=1 runs them) (2 retried after timeout)
— agent, the close's bar of 2026-11-13 on `b61832752` (PINNED, 2026-11-13)

## Owner confirmation

not asked — the run is unattended, and the unit is added under the mandate by `--rescope --act add`
