# TOOL-aOrientedCast-20 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-20

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: the §6 fixture T,
a `git init` repository under a short `%TEMP%` path holding a copy of the kit at tools/roles, gov's
`AGENTS.md`, `.claude/roles.json` and `.claude/agents/`, and a conf declaring `MEMORY_ROOT=memory`
and `CHARTER=AGENTS.md`. Its build folder and session S under the run's scratch path were written by
arm 9's own fixture writer, cut out of `adopt-roles.test.sh` and run with python. In it ran the verb
for each criterion, one staged break at a time, the fixture rebuilt before each, and the adopter's
`--scaffold`, whose render of the Skill differs from gov's committed one by the marker and the new
bullet alone. Also: a read-only `--run` probe against this session's live transcript from inside T,
so nothing was written into gov's tree; the AC9, AC10 and AC11 greps and the scanner probe from the
worktree root; `bash -n` over the suite; arm 9's two comparisons replayed by hand in T; and
`lexicon.py --suggest` for every new function name, nested helpers included, each answering OK
after two of them were renamed. Owed to the main loop at the close (M8): every leg §7 lists, and
§7's `New arm:`, arm 9 of `tools/roles/adopt-roles.test.sh`, RED on its staged break and GREEN once
restored. The break was already replayed in T: with the per-message-id maximum staged to a
per-record sum, the returned line read `1.9k out` and the arm's comparison answered 0. Also owed:
the second pass's re-render of `.claude/skills/build/SKILL.md` with `adopt-roles.sh --scaffold`,
which AC8 and AC9's third grep observe, and AC7 on the live session.

**Evidences:** TOOL-aOrientedCast-20
- AC1 — `1.6k out` — `agents --handoff <H> --session <S>` exited 0 and printed exactly the two lines §6 states, `effort medium` from the transcript, `wrote 2 files` and `7m47s`.
- AC2 — `committed abc123def` — `agents --run wf_00000001-aaa` exited 0 and printed three lines: a0000000000000002's `agent` line with `effort xhigh`, `model claude-test-2`, `TOOL-tFix-1` and H's link; its `returned` line `committed abc123def · 45s · 1.5k out`; and a0000000000000003's `agent` line with `commit:specs:tFix` and `writes none · gates none`, with no `returned` line.
- AC3 — `model unknown` — with the transcript cut to its user record and the notification deleted it printed one `agent` line with `effort high` and `model claude-test-1`, and no `returned` line; with `resolvedModel` deleted too the line read `model unknown`, stderr named `model`, and the ledger gained no line.
- AC4 — `colour` — with the `agent` definition deleted from T's `AGENTS.md` it exited 1 naming `agent`; restored and given `<colour>` it exited 1 with `the governing doc's agent shape names colour, a field handoff.py agents does not derive`.
- AC5 — `-build-TOOL-tFix-1-agent-ledger.md` — after AC1 the build folder held `2026-10-13-build-TOOL-tFix-1-agent-ledger.md`, third line `**Serves:** journal TOOL-tFix-1`, the two lines once each with the link `../prompts/2026-10-13-prompt-TOOL-tFix-1-1-builder.md`; a second AC1 run left `git hash-object` unchanged, and AC2's run then added three lines, five in all.
- AC6 — `a second *-agent-ledger.md` — H without its marker exited 1; no `Agent` call carrying it exited 1 naming H; `--run wf_00000009-zzz` exited 1 naming its journal; no `--session` with `CLAUDE_CODE_SESSION_ID` unset exited 2; `.claude/roles.json` removed exited 2; a second `*-agent-ledger.md` exited 1 naming both, printing no line; the spec removed exited 0, printed both lines, wrote no ledger and said why.
- AC7 — `--run <this unit's own unit-harness run id>` — owed to the main loop at the close, on the live session. The read-only probe ran from T against this session's transcript, where gov's build folder is absent, so nothing was written into gov's tree. It printed the PLAY-aOrientedCast-3 builder's `agent` and `returned` lines with no `unknown` field, and this unit's own `agent` line.
- AC8 — `handoff.py agents` — the grep over `tools/roles/SKILL.template.md` printed 1; the `--scaffold` re-render of the committed Skill is the second pass's, owed.
- AC9 — `^KIT_ROLES_VERSION = "1.3"` — the grep printed 1, the README and the template each carry `gov:kit roles@1.3`, and `kit.toml` reads the constant, so it needed no edit; `.claude/skills/build/SKILL.md` still reads 1.2 until the second pass's re-render, owed.
- AC10 — `## What each agent line tells you` — the grep showed the section, both verb spellings, the ledger's `-agent-ledger.md` name and the meaning of `unknown`.
- AC11 — `--show-prefix` — the scanner probe printed `0 ['-C "$HERE" --show-prefix', '-C "$HERE" --show-toplevel']` and the grep printed 2.
