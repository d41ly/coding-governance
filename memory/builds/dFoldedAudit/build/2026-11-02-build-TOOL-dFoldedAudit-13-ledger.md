# TOOL-dFoldedAudit-13 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-13

The acceptance criteria were observed by this unit's builder over the tree of this commit, on fixtures U and P of section 6, by a scratch probe of the driver as a CLI. No gate, suite or bar ran. Each new arm's RED-first observation is the close's, and it is not recorded here.

**Evidences:** TOOL-dFoldedAudit-13

- AC1 — `spec-disposal: absent` — `$P` over a blank cutoff printed this directly after its `roster:` line with `next:` following, exited 0, and its stderr held no `no policy kit resolves`.
- AC2 — `spec-disposal: by-nature` — `$P` printed this with no `RUN.md`, its stderr holding `no policy kit resolves`, and again with a `RUN.md` first committed 2026-11-02, where the `--review` call with `--folded 3` exited 0.
- AC3 — `spec-disposal: promote-all` — `$P` printed this over fixture P, the `--folded 1` call refused with `which folds nothing`, and the `--promoted 1` call exited 0.
- AC4 — `--folded and --promoted are counted only` — with a `RUN.md` first committed 2026-10-30, `$P` printed `spec-disposal: absent` and the `--folded 0` call refused with this.
- AC5 — `spec-disposal: absent` — with no `RUN.md`, `$P` printed this under a 2099-01-01 cutoff and `spec-disposal: by-nature` under 2000-01-01.
- AC6 — `TOOL-tFix-1` — with `disposal = "fold-all"` committed first, `$P` exited 0, printed `spec-disposal: refused - policy: refused · .governance/policy.toml:2 ...` and still printed this row.
- AC7 — `spec-disposal:` — `grep -c` over `--plan tFix` and `--plan tFix --framed` printed 0 under a blank and a dated cutoff, and under `--paths` the line held no TAB and `next:` was the last line.
- AC8 — `-chain-rounds.md` — each refused call exited 1 with the check 118 sentence and none of these existed, under a blank cutoff and under `promote-all` with a dated one, for a `local` row and for `--sibling`. The `new-mechanism` row exited 0 under `promote-all`, and the `local` row exited 0 under a dated cutoff with no policy kit. Neither case held a run-state file.
- AC9 — `policy.py get review.spec-audit.disposal` — `grep -c` printed 0 for this in each of the six files, and at least 1 for `spec-disposal:` in each.
- AC10 — `wc -l tools/roles/SKILL.template.md .claude/skills/build/SKILL.md` — each printed 102.
- AC11 — `grep -c 'fail 118' tools/unattended/unattended.sh` — it printed 1, and the raw `fail` census printed 318.

Beyond the criteria. A second scratch probe ran every call the new arms make over the fixture's other shape, the driver and library alone under `u/` with the policy kit at a sibling, and every one answered as the first did. The `local` row under a refused policy read also refused, and its sentence carried the read's text.

Owed at the close: the bar, and the five `New arm:` lines of section 7, each RED on its staged break and GREEN once restored. `FLOOR_ASSERTIONS` moved 2983 to 3022 and `FLOOR_SHARD_1` 466 to 505, counted off the block's own lines, 25 unconditional and 14 over a policy kit.
