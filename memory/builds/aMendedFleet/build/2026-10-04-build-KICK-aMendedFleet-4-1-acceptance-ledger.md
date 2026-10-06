# KICK-aMendedFleet-4 — acceptance ledger

**Serves:** journal KICK-aMendedFleet-4

**Evidences:** KICK-aMendedFleet-4
- AC1 — `cli — NOTE: PATH claude 2.1.178 is older than this session's 2.1.286` — under `%TEMP%`/k4a, a clone of the base carrying the unit's `manifest-check.sh` with a stub `claude` first on PATH, the NOTE printed for `AI_AGENT=claude-code_2-1-286_agent` on the line after `node —`, and `cli — PATH claude 2.1.178 is newer than this session's 2.1.99` for `AI_AGENT=claude-code_2-1-99_harness`; with the integer comparison swapped for a string one, a NOTE printed for 2.1.99
- AC2 — `cli — skipped: AI_AGENT names no Claude Code version` — printed for `AI_AGENT` unset and for `AI_AGENT=claude-code_x_agent`; `AI_AGENT=claude-code_2-1-178_agent` read as matching and `AI_AGENT=claude-code_2-1-290_harness` printed the NOTE
- AC3 — `cli — skipped: claude --version did not answer within 1s` — a stub sleeping ten seconds under `CARD_CLI_BOUND=1` was skipped at exit 0 in 3 s wall
- AC4 — `cli — skipped: no claude on PATH` — printed with no `claude` on PATH, and a stub printing no number read `cli — skipped: claude --version printed no version`
- AC5 — `grep -n "cli —" memory/map/features/session-kickoff.md` — hit the dossier's sentence; the same grep over `skills/session-kickoff/manifest-check.sh` hit the comment block and `derive_cli_line`, and `grep -n "tools/unattended" skills/session-kickoff/manifest-check.sh` printed nothing

## Where the observations come from

Each line restates an observation the unit's build commit `f3e9f93d7` records in its message, made
when the unit was built as Tier-1. TOOL-aMendedFleet-112 re-graded the unit Tier-2, which owes this
ledger, and wrote it from that record; no observation was re-made in that pass.
