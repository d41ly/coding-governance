# TOOL-dSettledStage-2 — acceptance ledger

**Serves:** journal TOOL-dSettledStage-2

No merge bar, no self-test suite, no `--selftest` and no leg argv ran in this pass. The pass started at
d53a82477. `<p2>` is the product commit, the one that adds this ledger and closes the spec; `<p2m>` is
the manifest re-stamp after it, and it writes `<p2>`'s sha below. Each probe ran from the worktree
root: the built `sh_hygiene.py` as a CLI over fixture repositories under `%TEMP%`, its functions
imported by `python -I` scripts under the session scratchpad, and staged-break copies of it under
`%TEMP%`. `<base>` is a local clone of this worktree checked out at 12764ec21 under `%TEMP%`.

**Evidences:** TOOL-dSettledStage-2
- AC1 — `b.sh` — the built mode over the criterion's fixture repository with an empty declaration exited 1, its one finding naming `a.sh` with its line 3, the class lines reading 1 unchecked and 1 admitted, DERIVED at observation; `b.sh` was in no finding. A copy with the staged-test step taken out named `b.sh` as well.
- AC2 — `tools/push-main.sh` — the built mode over `<base>` with that pathspec exited 1, one finding at lines 1065, 1347, 1372 and 1396, PINNED at 12764ec21. A copy that reads no `commit-tree` named 3 sites and omitted line 1065, DERIVED at observation.
- AC3 — `write_staged_change` — the built mode over this tree with pathspec `tools/push-main.sh` exited 0, reading 0 unchecked, 4 admitted and 0 unpaired, DERIVED at observation. A copy with the stager follow taken out read the four commits as unpaired.
- AC4 — `tools/unattended/unattended.sh` — the built mode over this tree with the leg's population and an empty declaration exited 1, 75 sources and 3 sites in 3 files, DERIVED at observation; the unpaired list named `tools/unattended/unattended.sh` twice. The registry, read through `resolve_declaration` and graded by `check_registry` over `scan_stage_tree` of that population, parsed no malformed row and left no problem, 3 sites in 3 rows, DERIVED at observation. The same registry over `<base>` exited 1 with `tools/push-main.sh` undeclared at 4 sites, PINNED at 12764ec21. The `.memory-tree.conf` line carries the member. The leg-argv form of the green run is the close's.
- AC5 — `tools/gate-legs.json` — a python read found one row whose argv carries `--stage-commits`, the registry, `.`, `:!*.test.sh` and `:!memory/`, chunk `product`, subject `repo` and no guard; its name is a `[[gate_leg]]` of `tools/gate-lint/kit.toml` whose argv is the criterion's; the subject-pins body equals the manifest's sorted rows; the dossier and the README section carry the name and the heading.
- AC6 — `STAGE_BOUNDARY` — every fixture row of section 4 and every boundary row read its stated class through `scan_stage_file`; every boundary label is in the docstring and the README section. A `build_blanked` that blanks nothing read the `echo` fixture as a commit, and a `read_stage_helpers` returning nothing read the checked-stager fixture as unpaired. `FLOOR_ASSERTIONS` is 151, counted off the arms, DERIVED at observation; the `--selftest` run and its printed count are the close's.
- AC7 — `scan_temp_file` — the built and the `<base>` module's `scan_temp_file` returned equal results for every tracked `*.sh`, 178 files, DERIVED at observation; the `two prefix assignments` row reads one fixed site. `grep -c 'build_blanked\|read_function_spans'` printed 10, DERIVED at observation. The criterion's `--temp-names` command is a leg argv the role hook refused, so its two-output comparison is the close's.
- AC8 — `memory/guides/SESSION-KICKOFF.md` — `<p2>` bundles a re-stamp at its parent d53a82477 with a `manifest-audit:` line in its body, and `<p2m>` re-stamps at `<p2>`. The pre-commit codebase-map leg passed on `<p2>` after `gen_map.py --write`. This ledger carries `**Serves:** journal TOOL-dSettledStage-2`.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/gate-lint/sh_hygiene.py --selftest`, covering AC6: RED on each of the three staged breaks section 7 names, GREEN once restored, and its printed count against `FLOOR_ASSERTIONS`.
- New arm `tools/gate-lint/sh_hygiene.py --stage-commits`, covering AC2 and AC3: the new leg RED over `<base>`, GREEN on this tree.
- AC4's and AC7's leg-argv runs, and the gates section 7 names.
