# TOOL-aRoutedQuill-12 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-12

No merge bar and no held suite ran in this pass. Each criterion was observed directly on node a,
against fixtures under `%TEMP%/rq12` that the pass built and removed: a primary repository with a
linked worktree and a junction for the gate, a `git clone --local` of parent 3a150ac1 for the
checker and the card, and a fresh target for the deployer. Every staged break below was observed
red against the parent's copy of the file, or with the named line staged out, and restored. The
arms added to `manifest-check.test.sh`, `scratch-guard.test.sh`, `check-wiring.test.sh`,
`push-main.test.sh`, `tools/govkit/selftest.py` and `routed_commits.py --selftest` were not run as
suites here, except `routed_commits.py --selftest`; the close owes the rest of §7 inside the bar.
`matrix.py`'s new shape ran alone, cut out of the file with its helpers; the whole matrix did not.

**Evidences:** TOOL-aRoutedQuill-12
- AC1 — `manifest-check.sh` — `read_memory_root`, cut out and run with `ROOT` at a fixture, printed `memory` for the exported, commented, quoted and twice-assigned confs and returned 1 with no conf; the parent's copy printed empty, `memory  # note` and `other`.
- AC2 — `routed_commits.py --selftest` — the two new `--newest-unit` arms printed `ok`, reporting `TOOL-tFix-1`; with the id check and `--no-merges` staged out they reported `TOOL-tFix-9` and `TOOL-tFix-2`.
- AC3 — `check-wiring.sh` — with the marker only on `Bash|PowerShell` and on SubagentStart, no conf and an empty `HOME`, the routed and skill lines read `skip`; the parent's printed `UNWIRED  routed` and `UNWIRED  skill`.
- AC4 — `check-wiring.sh` — a write-tool matcher and no conf printed the routed line saying the write gate admits every write here; the parent's said every product write refuses.
- AC5 — `scratch-guard.js` — `checkRouted` returned a `deny` for an Edit through the junction and through the repository spelling; the parent's returned `null` for the junction.
- AC6 — `govkit.py apply` — a fresh target with run-gates and a declared runner received the routed-commits row carrying `impure`; with the row builder's `impure` line staged out the row carried only `argv`, `name` and `subject`.
- AC7 — `govkit.py selfcheck` — exit 0 over the tree; with the `impure` line staged out of `tools/memory-tree/kit.toml` it exited 1 naming the leg and the field.
- AC8 — `scratch-guard.js` — `checkUnarmed('memory', 'src/ memory/builds/')` returned the reason naming `memory/builds/` as covering MEMORY_ROOT and `checkUnarmed('memory', 'src/')` returned `''`; the parent's returned `''` for both.
- AC9 — `routed_commits.py --selftest` — the refusal table printed `ok` for the entry under MEMORY_ROOT; with the two-way clause staged out that arm printed FAIL.
- AC10 — `check-wiring.sh` — `ROUTED_PATHS="tools/ memory/builds/"` printed `UNWIRED  routed` naming `memory/builds/` as covering MEMORY_ROOT; the parent's printed `ok       routed`.
- AC11 — `matrix.py` — shape 7 alone printed 15 passing checks in 128 s; with `add_deploy_kits` staged out of the aged copy's `update --write`, the declared-kits check failed.
- AC12 — `grep -n 'New arm'` — the TOOL-aRoutedQuill-5 spec's `matrix.py` line covers AC3 and AC4 and its `selftest.py` line covers AC1 and AC2.
- AC13 — `scratch-guard.js` — `checkBuildable` returned `''` for the colon, bold and fenced H1 spellings and the H1 reason for a spec naming TOOL-x-2; the parent's refused all three spellings.
- AC14 — `grep -n 'shell write'` — the one hit says a shell write passes the gate and the routed-commits leg grades the commit.
- AC15 — `scratch-guard.js` — `checkBuildable` returned `''` for a spec in a `units` sub-folder; the parent's returned the `is outside` reason.
- AC16 — `push-main.sh` — `read_mint_unit`, cut out with its resolvers stubbed, printed nothing for a refusing stub and `TOOL-x-1` for an answering one; the parent's printed the refusal text.
- AC17 — `scratch-guard.js` — `checkBuildable` returned `''` for Tier-1 INPROGRESS and the five named reasons for no Tier cell, an absolute path, no build and no spec.
- AC18 — `scratch-guard.js` — under `node -r` with a stub throwing on every `.git` read, the hook exited 2 printing `fails closed`; with the catch staged to admit it exited 0.
- AC19 — `manifest-check.sh --card --append` — a `## route ` body onto a routed fixture card left one route heading; the parent's left two.
- AC20 — `grep -n 'PLAY-aRoutedQuill-1'` — the `roster:units` row reads CLOSED.
- AC21 — `check-arms.py --check` — exit 0 with 18 sites armed; with the R1 needle staged back to a prefix it named the R1 site unarmed.
- AC22 — `check-install-prefix.sh` — clean, 0 spellings; before the pass it named `tools/check-wiring.sh` and the kickoff suite's reader line.
- AC23 — `lexicon.py` — `lexicon OK` with no `over pin` line, and `--offenders` listed none of the six old names.
- AC24 — `check-template-size.sh` — `template-size OK` for the protocol at 65842 bytes, after `--bump` recorded the high-water.
