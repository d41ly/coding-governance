**Serves:** journal TOOL-dWitnessedBar-29

# TOOL-dWitnessedBar-29 — builder return 1 (run `wf_4f3b1452-30d`), committed b0ad989581b307fcb739a7b8f548509171a897c8

## Why

TOOL-dWitnessedBar-29 is built from spec rev-5 and committed as one pass commit with the trailer `Pass: TOOL-dWitnessedBar-29`. The spec header is now CLOSED, dated 2026-11-20. The spec could be built as written. The census, citations, runner symbols and runner blob e044bc9f all matched the tree.

## Summary

Built and committed TOOL-dWitnessedBar-29 as b0ad989581b3 on base 60f08d3db831. No gate, suite, bar or `--selftest` ran. The only check of that kind was the naming lexicon's `--suggest`, which passed for `render_warn_marker`, `scan_leg_warnings` and `run_warn_slice`.

**What changed**
- **The marker:** `tools/policy/budgets.py` gains `render_warn_marker`, and its `check` verb prints the marker after a warned verdict. All 13 emitter files in the census now print the `gate-warn` marker. The four shell sites use one printf each; the Python sites call the factory.
- **Attribution:** `tools/memory-tree/routed_commits.py` takes `--newest-unit <range> [<path>]`; the path is passed to git as a literal pathspec.
- **The runner:** `tools/run-gates/run-gates.sh` gains `scan_leg_warnings`. It runs after the same-tree re-run and inside the wall. It prints `GATE warn` lines before `----` and in the summary file, adds `(<n> warned)` to the closing line, and writes `warned` and `warn.<k>` to the verdict.
- **Profile reader:** `tools/run-gates/profile_bar.py` pins `warn` and reads it as an annotation.
- **Docs:** the run-gates README, the size gate's header, `help/size-caps.md` and the policy README's `budgets.py` row.
- **Records:** `memory/guides/SESSION-KICKOFF.md` last-audit re-stamped; codebase map and build index regenerated; acceptance ledger and deviations 291 and 292 written.

**What each check stood in for (all scratch fixtures, slices or probes)**
- AC1 (template-size selftest): the real gate over a scratch fixture and planted high-water file printed the marker on the line after the warning; at the high-water it printed neither.
- AC2 (census): both §4 queries named the 13 files, and each matches `git grep -c 'gate-warn'`. For the 7 Python sites that build the marker through the factory, that match is a comment word beside the call. So AC2 is only a presence check there; the AC9, load_sets and render_playbook probes are what show the marker is actually printed.
- AC3 and AC6 (run-gates canary): the sliced `scan_leg_warnings` over planted work dirs showed:
  - one line for a passing leg, none for a red leg, none for a re-run copy;
  - a held leg read from its passing first attempt only, never its retry copy;
  - a missing memory-tree kit, a non-path subject or an outside-tree path each giving `grown by -` with the reason.
- AC4: the sliced verdict-write block wrote `verdict GREEN`, `warned 1` and `warn.1` with the subject as the line's fourth TAB field.
- AC5 (routed-commits selftest): `--newest-unit HEAD memory/guides/BUILD-METHOD.md` printed TOOL-aTrimmedWait-19. With two arguments it printed the same as the base copy. A scratch repository built with the module's own fixture helper told the two cases apart.
- AC7: both section-6 greps hit.
- AC8 (profile-bar selftest): printed `[] True`.
- AC9 (policy fixtures): printed the exact repr; `budgets.py check` in a scratch repo printed the marker under `warn` and none under `refuse`.
- Every edited file passes `bash -n` or `ast.parse`.

**Owed at the close**
- Three new arms, written but not run; each needs its RED-first observation:
  - `run-gates.test.sh` arm 9e3, 12 assertions, with `FLOOR_ASSERTIONS` raised from 468 to 480. Staged red by dropping the `scan_leg_warnings` call.
  - `check-template-size.test.sh` A6m/A7m. Staged red by deleting the marker line.
  - `routed_commits.py --selftest`, the pair labelled `dWB29 AC5`. Staged red by dropping the path argument.
- The legs of §7, plus the bar halves of AC3, AC4 and AC6, which only a fixture bar can show.

**Decisions and deviations**
- **Deviation 291:** no kit version was moved. Read from source, `govkit.py epoch` off the push boundary reports moved kits as `owed at the lander`, and `mint` writes the bump.
- **Deviation 292:** where a list of warnings is printed somewhere else (`load_sets`, `render_playbook`, `check_roles`, `handoff`), the marker rides inside the warning's own item after a newline. A Python site with no policy kit loaded prints no marker. `gen_build_index` and `gotchas` print the marker beside the line. The `-` reason comes before `grown by -`.
- **AC4 reading:** "value's fourth TAB field" is read as the line's fourth field, which is where S7 puts the subject.

**Other things to know**
- **Dispatch:** my first `--dispatch` replaced the main loop's declaration instead of widening it, and `--check-commit` refused the commit. A second declaration that also named `memory/LIVE.md` was refused for pairing a generated index with its generator. I then re-declared the full set without the generated outputs, and the commit passed every hook.
- **Unbounded spawn:** the per-subject attribution python call has no bound of its own; only the runner's wall bounds it.
- **Line endings:** the CRLF working copies of several edited Python files (gotchas, load_sets, render_playbook, check_roles, handoff, query) were rewritten as LF. Git normalizes these to LF on commit, so the committed bytes are unaffected.
- **`gotchas.py --for-diff HEAD~1..HEAD`:** ran and printed 70 classes. Acted on:
  - The heredoc-escape class: caught during the build and fixed in the four affected files.
  - Floor raised to match the 12 new assertions.
  - No `read`-with-TAB parsing.
  - No pipe added inside a table cell.
  - No literal tab or CR added in the diff.
- The pre-existing unstaged edits to `help/reference/drive.md` and `help/reference/units.md` are not mine and were left alone.

Paths: C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-29-1-acceptance-ledger.md, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-29-deviation-291.md, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-29-deviation-292.md
