# PLAY-aRoutedQuill-1 — acceptance ledger

**Serves:** journal PLAY-aRoutedQuill-1

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a
in the run's worktree, and AC3 in two scratch fixture repositories under a short `%TEMP%` root. A
staged break was observed red once: with the write-gate bullet deleted from `AGENTS.md`,
`adopt-playbook.sh --target . --check` printed `DRIFT — the charter region differs from a fresh
render`, and restoring the file returned it to OK. The close still owes the legs §7 names inside the
bar, and AC7's second half, which only the run's mint commit and the landing can observe.

**Evidences:** PLAY-aRoutedQuill-1
- AC1 — `grep -n "Spec before code"` — it hit `coding-governance-agents.template.md:37` and `AGENTS.md:95`, each followed by the `Tier-2:` bullet; the menu from `+ a bounded production-readiness menu (` to `docs)`, extracted from both files at base and at the tip, compared byte-identical with `cmp`, 276 bytes.
- AC2 — `adopt-playbook.sh --target . --check` — after the render it printed `region matches a fresh render, no placeholder survived`; `grep -c "A write gate refuses" AGENTS.md` returned 1 and `grep -c "<!-- kit:agent-cap" AGENTS.md` returned 0.
- AC3 — `adopt-playbook.sh --target` — a fixture whose `deploy.toml` kits omit `agent-cap` rendered the `Spec before code`, `Tier-2:` and scope-approval bullets once each and the write-gate bullet 0 times; the control fixture, the same file with `agent-cap` kept, rendered the write-gate bullet once.
- AC4 — `check-template-size.sh` — after `--bump` on both subjects it printed `48800 / 49152 bytes (352 under, 99.3%)` for the template and `54628 / 64512 bytes (9884 under, 84.7%)` for `AGENTS.md`, with no high-water warning; the figures equal the spec's §4 measurement, and the `AGENTS.md` bump absorbs the 95 bytes it grew before this unit.
- AC5 — `check-line-length.sh` — it printed `0 over 450 characters` for both files, and `check-playbook-parity.sh` printed `playbook-parity OK — 17 kit(s) documented or waived · pairs in agreement`.
- AC6 — `manifest-check.sh` — run on the unit's commit, whose `last-audit` and `last-body-change` name its parent `60aa85982`; `grep -n "micro-spec" memory/guides/SESSION-KICKOFF.md` shows the Tier rule at line 211.
- AC7 — amended rev-4 — the marker and banner move rides the run's mint commit, not this unit's; `govkit.py epoch` on the unit's commit is the observation this pass owns, and the main loop owns the `clean` row and the landed `--check`.
