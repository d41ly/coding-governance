# TOOL-dTotalRecall-114 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-114
**Caused-by:** TOOL-dTotalRecall-114

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`08a895a66feb42430e5d6ec87f1571c34d3a9a59` on node a, 2026-11-25 local, in one commit. Every probe below ran from the
repository root over the working tree the commit holds. `fork-count.sh --only`, `py_reads.py --guards`, `check_layers.py
--list` and the `--measure` forms are the instruments' own reads, as §6 names them. §7's legs and the RED-first
observation of its three new arms are owed to the close. The deviation is `2026-11-25-build-TOOL-dTotalRecall-114-deviation-1015`.

The one criterion clause that does not hold is AC16's `cmp`. `gov-claim.sh` carries the `gov_ref_sh` block of before
`0678a8e7b`, which main's reconcile brought to `tools/lib/gov-ref.sh`, `post-merge.sh` and `unattended.sh`; it differed at
the base too. The block is a non-goal of §3, so it is handed back as a divergence and not edited. The leg that grades it,
`python resolver (behaviour + inline parity + idiom ban)`, is held, so the first bar did not show it.

**Evidences:** TOOL-dTotalRecall-114
- AC1 — `grep -c 'exclude)\*/record-kinds.toml' tools/drift-audit/drift_signals.py` — printed 1, and `git grep -l` of the id listed `check-spec-tokens.test.sh`, `record-kinds.toml`, `unscanned-readers.txt` and `template-size-highwater.txt`, each read past by a row of that list (DERIVED 2026-11-25, these commands).
- AC2 — `grep -cE 'tMark\$(i|_f2|mark_case_n)'` — printed 0, and the two lines over cases 1 to 60 printed 60 distinct slugs, each matching the shape (DERIVED 2026-11-25, these commands).
- AC3 — `git grep -nE '"origin"'` — listed none of the five fixture lines, and `--plant ask-door` printed `PASS ask-door — 15 cases` and `--plant door-header` `PASS door-header — 12 cases` (DERIVED 2026-11-25, those plants).
- AC4 — `grep -rhoE 'gov:kit runlog@[0-9.]+'` — printed `gov:kit runlog@1.19`, the version `KIT_RUNLOG_VERSION` holds (DERIVED 2026-11-25).
- AC5 — `grep -c "PLAY-fxHeld-{n} F1"` — printed 1, and the `HOLD_RE` read printed `True False` (DERIVED 2026-11-25).
- AC6 — `python tools/memory-tree/transition_audit.py` — over the scratch copy with no `id_grammar.py` exited 0 printing `DORMANT` under shards, and exited 1 under `--expect-builds` naming `id_grammar.py` and `reinstall the memory-tree kit`, neither with a `Traceback` (DERIVED 2026-11-25, that fixture).
- AC7 — `python tools/playbook/check_layers.py --list` — every edge of the two kits ended `allowed`, the count line `71 allowed, 0 red; 0 contract red(s)` (DERIVED 2026-11-25).
- AC8 — `grep -c 'principle.p35' tools/playbook/core-pending.txt` — printed 0 (DERIVED 2026-11-25).
- AC9 — `grep -cE 'asks\.acceptance|builds\.slug-(words|style|date)|memory\.map-purpose' help/reference/policy.md` — printed 15 (DERIVED 2026-11-25), and a second render left the page as it stood.
- AC10 — `python tools/run-gates/py_reads.py --guards "<leg>"` — printed closure lines alone for each of the twelve, exit 0, and no gap line; a second `leg_factory.py --write` answered `the manifest already fresh` (DERIVED 2026-11-25).
- AC11 — `python tools/run-gates/py_reads.py --list-params` — printed none of the eight keys, and its 124 keys and the 124 rows of `unread-params.txt` join both ways (DERIVED 2026-11-25).
- AC12 — `grep -c 'RUN.LANDED.bc313f97.md' memory/project/positional-refs.txt` — printed 5, each row counting 1 and ending `widened:2026-11-25-build-TOOL-dTotalRecall-114-widen-16`, whose Keys name all five (DERIVED 2026-11-25).
- AC13 — `python tools/govkit/upgrade_steps.py list --ids` — every id it printed is a first field of `landed-steps.txt`, and the diff shows four added lines and none removed (DERIVED 2026-11-25).
- AC14 — `spawn_sites` — over the hygiene suite printed `date-fmt` 0, `printf-subst` 16 and `var-pipe` 80, and the bare-probe grep printed 0 (DERIVED 2026-11-25).
- AC15 — `spawn_sites` — printed `path-subst` 0 and `var-pipe` 3 for `gov-claim.sh`, `printf-subst` 0 for the push-main suite and `path-subst` 6 for `lib-unattended.sh`, and `spawn-idiom-sites.txt` holds `gov-claim.sh` under `var-pipe` at 3 alone, the three in `remote_ladder_sh` (DERIVED 2026-11-25).
- AC16 — `grep -h 'memory-tree/gov-claim.sh'` — printed one `fixed-temp` row at 1 and one `tab-ifs-read` row at 2, each `widened:` (DERIVED 2026-11-25). The `cmp` half: `remote_ladder_sh`, `health_log_sh` and `gov_feed_sh` equal their canonical files, and `gov_ref_sh` does not, the divergence above.
- AC17 — `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` — its 156 keys equal the rows of `shell-role.txt` at every count, and `2026-11-25-build-TOOL-dTotalRecall-114-widen-22` names 21 keys (DERIVED 2026-11-25).
- AC18 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only <id>` — the guard admitted it, and it printed `ok` for all four ids. Beside the bar's counts: `unattended-status` 57 then 51, `unattended-plan-handover` 221 then 215, `check-unattended` 809 then 809, `memory-hygiene` 193 then 193 (PINNED 2026-11-25, `bar1.log`, then DERIVED 2026-11-25, these runs). The `setup` text of the plan row was re-quoted, its count unmoved, as the deviation says. The 24 over `check-unattended`'s row are one site's, check 28's raw arm, 117 at main `3d6c1702a` and 141 here (DERIVED 2026-11-25, `--sites` at both).
- AC19 — `python tools/gate-lint/encoding_posture.py --cleanup --measure . tools` — printed the two `tools/govkit/steps` keys alone, and `--plant missing-section` ended at its `exit 2` line with no `rf-` directory left (DERIVED 2026-11-25).
- AC20 — `grep -E '^(last-audit|last-body-change):' memory/guides/SESSION-KICKOFF.md` — the first names the base sha, the second `ffa0dcf2da2ba209a820b287660948f7d1a3988a`, and the `rev-list` count printed 0 (DERIVED 2026-11-25). The table below is the re-read.
- AC21 — `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import corpus_ids as c` — printed `[]` over this tree, and over the scratch tree `('memory/README.md', 'tools/gone.py')` alone, the live `tools/live.py#x` beside it unlisted (DERIVED 2026-11-25).
- AC22 — `python tools/memory-tree/row_grammar.py --check-relations 3d6c1702a` — before the commit, over the working tree, printed 1 near match and 1 satisfied and no `check 27:` line (DERIVED 2026-11-25); the same read after the commit is owed to the close. `gotchas.py --write` left `INDEX.md` byte for byte.
- AC23 — `grep -c 'grep -qF -- "$1"' tools/memory-tree/check-memory-hygiene.test.sh` — printed 2; `door-header` printed `PASS door-header — 12 cases`, `legacy` `notes.md findings causes` and `notes.md findings-2 causes`, and `none` neither (DERIVED 2026-11-25, those plants).
- AC24 — `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import row_grammar as r; print(r.scan_engine_imports('tools/memory-tree')[0])"` — printed `[]` (DERIVED 2026-11-25). `row_grammar.py --selftest` is owed to the close: the role runs no `--selftest`.
- AC25 — `tag_index.check_tag_shape` — printed no red over 120162 tags and `check_owned` none; a `practice.` row of 65 bytes, an authored `[section.<seg>]` heading and a mapped section tag of the same length each kept one `shape` red while a derived anchor over the cap kept none; `check_retired` over `section.gone` and `doc.x#gone` red the second alone (DERIVED 2026-11-25, that probe). The plant `memory-records` printed `section 5` and `tags: green · 0 red` (DERIVED 2026-11-25).
- AC26 — `python tools/playbook/edge_grammar.py --fixture --plant leg-unregistered` — printed the `edges: leg rows · 1 tests target(s)` line and no `is not registered`; `--plant leg-unarmed` printed `edges: green` and no `resolves to no row`; `resolve_edge` over this tree answered `unarmed`, `resolved` and `red` for `feature.playbook`, `practice.land` and `practice.nowhere` (DERIVED 2026-11-25).

AC20's re-read. The watched commits the reconcile brought (DERIVED 2026-11-25, `git log --no-merges` from `adb171bb0` over the
watch list), and what §B said of each:

| Commits | Watched file | §B |
|---|---|---|
| `2b84cd488`, `4c347e333` | `coding-governance-agents.template.md` | names the template in the pointer map alone; the preset section and the `progress —` line are the charter's, and no line is stale |
| `dfdcd7284`, `bb95b0dcf`, `d1ca8c5c5`, `41ea551a7`, `6178a65ee`, `2185a389c`, `6d3567df3`, `a20dc8168`, `f0768671b`, `dc8e2b1d8`, `f81b9d4ea`, `6b77340cd`, `914f41751`, `3e7b30623` | `skills/session-kickoff/manifest-check.sh` | says the card prints the orientation units under `## pockets` and names no pointer, mailbox or version line; nothing stale |
| `525d33285` | `.memory-tree.conf`, `gate-legs.json`, `run-gates.sh`, `run-selftests.sh` | its trap on the bar's own scratch already reads `even if its repo is gone` |
| `c81e16bbd` | `run-gates.sh` | says what `GATE_FULL=1` ignores and not how a guard's diff is read; nothing stale |
| `3a1d97e63` | `run-selftests.sh` | its `--serial` and `--pooled` line names modes, refusals and the kept output, none of which moved |
| `dcc7e30f8`, `40607fd2a`, `c5fd95b52`, `33a4e2325`, `360d706f6`, `040e261d1`, `10c54981f`, `4b845d0b7` | `gate-legs.json` | names no leg's guard, and points at `leg_factory.py --write` for the list |

No §B line changed. The two §B edits the merge carried, the slug grammar and the front-matter keys, are this build's own
units 5 and 4, and hold at the base.
