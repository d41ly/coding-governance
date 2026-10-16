# TOOL-dRedressedBar-7 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-7

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 7 rev-4 in the one
pass commit `671f25c71`. Spec 7's rev-5 rewords AC4 to name every unit ordered before this one and
says "this unit's ledger still answers it", because the kit set AC4 derives from its own `epoch`
run is unchanged; the reading below is that run's. The readings are the builder's, from that
commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
under the heading `2026-10-14T17:30:21 · gov-builder · wf_7000bf13-341/a41438c689c4a68eb` at line
5035. No merge bar, no self-test suite and no gate leg ran in the build pass. Every reading is a
direct probe, and the section 7 legs were owed to the close.

**Evidences:** TOOL-dRedressedBar-7
- AC1 — `memory/gotchas/INDEX.md` — its diff from the base adds exactly the two class rows S1
  names, with the count line. Its freshness was read through `regen.py --check`, which declares
  the index and read `12 declared · 12 fresh · 0 stale`. The record names no separate run of
  `gotchas.py --check`.
- AC2 — `0 stale` — `regen.py --check` read `12 declared · 12 fresh · 0 stale` and exited 0. The
  baseline before the pass read `12 declared · 11 fresh · 1 stale`, naming the gotchas index.
- AC3 — `memory/project/method-carriers.txt` — after the mint, the files that mention the method
  and the registry differed by one path, `.claude/agents/gov-reuse-scout.md`. Its row now sits
  between the gov-researcher and gov-skeptic rows, the two lists match, and the agent file holds no
  `## M<n>` heading.
- AC4 — `FAILED` — before any write, `govkit.py epoch --base ebce889c7` exited 1 with `FAILED` for
  exactly five kits, agent-cap (1.38), branch-reconcile (1.4), playbook-render (1.28), roles (1.5)
  and unattended (1.106), and read run-gates `clean`. At the tip the same command printed no
  `FAILED` line and exited 0.
- AC5 — `git grep -nF "gov:kit <kit>@<old>"` — partly met, as the builder reported it. The mint
  printed `agent-cap · 1.38 -> 1.39`, `branch-reconcile · 1.4 -> 1.5`,
  `playbook-render · 1.28 -> 1.29`, `roles · 1.5 -> 1.6` and `unattended · 1.106 -> 1.107`, each
  value moving by its last component. Over the whole tree at the tip, the literal probe printed two
  lines, both in `memory/builds/aOrientedCast/`: line 35 of the TOOL-aOrientedCast-27 acceptance
  ledger and line 11 of the TOOL-aOrientedCast-25 fold brief. Both quote old markers in prose and
  were already tracked at `ebce889c7`, so neither is a carrier. Outside `memory/builds/` it printed
  nothing for all five kits.
- AC6 — `memory/guides/SESSION-KICKOFF.md` — the probe over its watch list printed nothing: no
  watched path moved in `ebce889c7..HEAD` or in the pass commit, so no stamp was written.
- AC7 — `render_playbook.py` — `git diff -U0 HEAD~1 HEAD` over it changed line 1839 only, and lines
  1397 and 1646 both read `v3.5`. The commit's changed files fall only in the categories AC7 allows.
