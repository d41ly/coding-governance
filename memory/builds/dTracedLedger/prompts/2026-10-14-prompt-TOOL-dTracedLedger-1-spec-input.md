# Spec input — TOOL-dTracedLedger-1, from the main loop

**Serves:** research TOOL-dTracedLedger-1

Fill every `<fill: …>` slot of the Tier-1 scaffold
`memory/builds/dTracedLedger/spec/2026-10-14-spec-TOOL-dTracedLedger-1.md`, written by
`gen_build_index.py --new-spec`; keep its headings, Status line and revision log. Work only in the
worktree `C:/projects/coding-governance/.claude/worktrees/dTracedLedger` (branch
`branch/dTracedLedger`, base `ebce889c7d7104fe4811707d6f17b2a486bf0fd6`), with forward-slash git
paths, and do not commit.

The unit is records only and its records are already written:
`memory/builds/dTracedLedger/README.md`, `BACKLOG.md`,
`build/2026-10-14-build-TOOL-dTracedLedger-1-research-check-23-reds.md`,
`build/2026-10-14-build-TOOL-dTracedLedger-1-pairs.py` and
`prompts/2026-10-14-prompt-TOOL-dTracedLedger-1-brief.md`. The spec describes exactly those, so the
research record's `**Serves:** research TOOL-dTracedLedger-1` resolves; hygiene check 21 needs a
spec H1 defining the id. Invent no scope beyond them.

The asks TOOL-dTracedLedger-2 and TOOL-dTracedLedger-3 live in this build's `BACKLOG.md`, because
the backlog grammar admits an ask only in its own slug's folder (`tools/memory-tree/README.md`,
"Row kinds"; verdict V1); the owner's request to file in aSparedSpawn's `BACKLOG.md` had no legal
form for this session, and the spec says so. They are not spec ids.

Files touched: the five build-folder files above, the spec, the spec-writer prompt,
`memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp committed at 1a172f139),
`memory/project/readme-contract.txt`, and the generated `memory/LIVE.md`,
`memory/ledger/2026-10.md` and `memory/backlog/TOOL.md`. Take section 6's leg line from `python
tools/check-spec-tokens.py --list`, not a guess.

Acceptance criteria are observable now, each with a "Red when:" line and every backticked token on
its first physical line: `git diff --stat ebce889c7..HEAD` lists no path under
`memory/builds/aSparedSpawn/` or `memory/builds/aOrientedCast/`; `bash
tools/memory-tree/check-memory-hygiene.sh` names no TOOL-dTracedLedger id and the same 37 check-23
rows as at the base; `python tools/memory-tree/gen_build_index.py --check` reports 0 verdicts. Wrap
prose at 100 columns. Return the spec path, the leg line used, and any slot left unfilled.
