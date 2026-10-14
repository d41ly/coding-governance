# Research: orientation cost — tool calls, tokens and time per entry kind, measured from this node's transcripts

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md`
(dispatch 12), verbatim. The harness escaped `<`, `>` and `&` in the returned text as HTML entities;
they are restored here, and nothing else is changed.

---

## 1. Inventory

- **Startup card hook.** Writes and prints the `orientation —` card on startup or clear: `.claude/settings.json` SessionStart, `skills/session-kickoff/manifest-check.sh:706`.
- **Card cells.** node, cli, tree (branch, BASE, dirty count), worktree count, drift, overlaps, `live —`, claims, health, `git log -5`, then `READY — none yet`. The `live —` cell is only a count of LIVE.md rows (`manifest-check.sh:517-545`, `:529`).
- **Replay hook.** On resume or compact it prints the stored card plus one `now —` line (`manifest-check.sh:721-725`).
- **Kickoff engine Step 1.** It tells the agent to re-run branch, status, fetch and rev-parse, and to trust the card for "never its branch or BASE" (`skills/session-kickoff/SKILL.md:49-56`).
- **Kickoff Steps 2–5.** Read the manifest, audit it, derive the scope, run the M5 probes and recall, then append READY with `--card --append` (`SKILL.md:67-210`).
- **Charter auto-load.** `CLAUDE.md` holds only `@AGENTS.md` (16,732 B); `.claude/rules/product.md` loads when a product file is opened.
- **Wiring and process hooks.** `tools/check-wiring.sh --session` and `procmon-hook.js` run at SessionStart.
- **Unattended tick.** `tools/unattended/resume-tick.sh:367` launches `claude -p --resume` with a CONTINUE payload of three steps: reap, `--resume`, then continue from the phase.
- **Run status.** `tools/unattended/unattended.sh:8038` (`verb_status`) gives the phase and first non-terminal unit for one run.
- **Subagent context.** The SubagentStart hook `tools/hooks/scratch-guard.js` (comment at :128-145) injects the card's `## route`.
- **Subagent brief.** `tools/roles/handoff.py render` builds the brief. Its Protocols and Facts sections are carried as pointers and facts (`tools/roles/roles_lib.py:67`).
- **`next` verb: absent.** I grepped `--next`, `verb_next` and `'next')` over `tools` and `skills` and found nothing.

## 2. Sequence

- **New session** (64 sessions; 53 invoked the kickoff). The card is injected (about 1.1 KB, about 1.3 s). Pre-productive calls (2,282 in total) split as:
  - 58% content reads: sed, grep and cat over records and code.
  - 14% method docs: `memory/guides`, the charter, SKILL.
  - 13% locating the work: LIVE.md, build READMEs, `ls memory/builds`.
  - 7% git state the card already printed.
  - The rest: TaskCreate, ToolSearch, AskUserQuestion.
  - By returned chars, sed, grep and cat lead (2.1M, 1.6M, 1.5M), then Reads of `memory/guides` (0.7M) and `memory/builds` (0.5M).
- **Resume.** Few calls (median 4), but the median fresh input is 467k tokens: the whole context is cache-written again. Calls are 48% content, 15% locate, 13% state.
- **Compact.** The median is 15 calls, 80% of them content reads that rebuild working memory. Locate and state medians are 0.
- **Run tick.** No `claude -p` resume-tick launch exists in the population: all 87,590 records have entrypoint `claude-desktop`, and `.git/unattended/` holds no attempt sidecar. There were 109 scheduled wakes, all in 2 sessions; 106 produced no model turn and 3 ran.
- **Subagent.** Of 88,375 calls before the first output, 80.6% are content, 8.6% locate, 7.4% method and 1.7% state. Content is 87.8% of the returned chars.

## 3. Measurements

The probes were inline python3 heredocs, run read-only and printed, never saved. Each one streamed `C--projects-coding-governance*/*.jsonl` line by line, with `json.loads` per line.

**Shared predicates, verbatim:**
- productive = `n in {Edit,Write,MultiEdit,NotebookEdit} and '.git/orientation/' not in path` or `re.search(r'\bgit\b[^;&|\n]*\bcommit\b',cmd)`
- READY = assistant text matching `r'READY —(?! none yet)'`
- resume marker = attachment `hookName=='SessionStart:resume'`; compact marker = `system/compact_boundary`
- tick = user record with `turnOrigin=='scheduled'`
- tokens: deduped by `message.id`; fresh = `input+cache_creation`; cache-read reported separately
- percentiles: nearest rank on the sorted list

The full script text runs past this return's word cap; the predicates above fix every number below.

**P1b — sessions, resume, compact, tick** (64 top-level files, 383 MB)

| entry | n (reached productive) | calls | fresh-in tok | cache-read tok | out tok | secs |
|---|---|---|---|---|---|---|
| new | 64 (58) | 35 / 67 / 82 | 146k / 293k / 444k | 3.5M / 10.2M / 15.8M | 29k / 65k / 85k | 684 / 9,272 / 87,812 |
| new → READY | 20 | 26 / 55 / 57 | | | | 406 / 4,893 / 87,455 |
| resume | 35 (33) | 4 / 12 / 24 | 467k / 827k / 1.50M | 1.8M / 5.6M / 20.1M | 6.3k / 14k / 54k | 163 / 622 / 10,254 |
| compact | 23 (23) | 15 / 42 / 80 | 93k / 143k / 177k | 1.3M / 5.8M / 10.2M | 15k / 49k / 73k | 207 / 1,636 / 10,058 |
| tick | 109 (3) | 6 / 6 / 6 | 796k / 910k / 910k | | 2.7k / 6k / 6k | 51 / 3,428 / 3,428 |

Cells read median / p90 / max. Wall times include owner waits.

**P1b — re-reads and re-runs**
- Same-path re-reads per session: median 1, p90 9, max 29 (188 in total). Identical path+offset+limit re-reads: median 0, p90 1, max 4 (12 in total).
- Ten most re-read paths:
  - `tools/memory-tree/gen_build_index.py` 10
  - `tools/memory-tree/check-memory-hygiene.sh` 9
  - `memory/builds/dRedressedBar/README.md` 8
  - `tools/govkit/selftest.py` 8
  - `tools/govkit/govkit.py` 7
  - `tools/hooks/agent-cap.js` 5
  - `tools/memory-tree/check-memory-hygiene.test.sh` 5
  - `tools/workflows/unattended-build.js` 5
  - `tools/memory-recall/selftest.py` 5
  - `tools/unattended/unattended.sh` 5
- Most re-run exact-duplicate commands, by first word: bash 69, for 41, python 21, grep 15, python3 14, git add 11, git rev-parse 9, cat 9, sed 9, git status 6.

**P3 — card- or charter-answerable calls before the first productive write** (64 sessions)
- Per session: median 6, p90 16, max 25; 475 in total.
- By command: git log 151, git status 111, git rev-parse 81, git worktree 51, git branch 42, git fetch 32, Read `SESSION-KICKOFF.md` 6, Read `AGENTS.md` 1.
- `--card --append` was called in 19 sessions; only 2 of them did so before their first productive write.

**P2 — ticks**
- 109 scheduled turns in 2 sessions. The next prompt was another scheduled wake 106 times and a task notification 3 times.
- 106 ticks made 0 calls and spent 0 tokens; 3 made a productive act.

**P4 — subagents** (3,170 transcripts, about 2.1 GB, under `*/subagents/**`; type from `.meta.json`)

| type | n | calls before first write | read-only total calls | paths named in prompt | re-reads of named paths |
|---|---|---|---|---|---|
| workflow-subagent | 2,582 | 23 / 63 / 159 (1,209 wrote) | 30 / 58 | 6 / 19 | 1 / 8 (7,219 in total) |
| general-purpose | 77 | 24 / 61 | 36 / 49 | 5 / 11 | 2 / 6 |
| gov-spec-writer | 45 | 28 / 60 | | 7 / 19 | 1 / 9 |
| gov-researcher | 14 | | 34 / 46 | 21 | 4 / 11 |
| gov-spec-reviewer | 20 | | 55 / 111 | 23 | 4 / 8 |
| gov-builder | 13 | 18 / 28 | | 4 | 3 / 3 |

- Reads of content the prompt already carried: `AGENTS.md` 123, the agent's own handoff prompt 10, `CLAUDE.md` 3.
- Most re-read named paths: `tools/unattended/unattended.sh` 464, `tools/govkit/govkit.py` 328, `memory/guides/BUILD-METHOD.md` 303, `check-memory-hygiene.sh` 185, `memory/TEMPLATE-SPEC.md` 174, `gen_build_index.py` 172, `check-unattended.sh` 144, `run-gates.sh` 118, `unattended.test.sh` 103, `corpus_ids.py` 94.

**P5 — tests A and B.** Its outputs are under section 5. The call classes are:
- state: a git status, log, branch, worktree, rev-parse or fetch command that names no repository path.
- locate: LIVE.md, `memory/builds/*/README.md`, `ls memory/builds`, `gen_build_index`, `--status`, `memory/plan`, BACKLOG or ASKS.
- method: `memory/guides/`, TEMPLATE-SPEC, HYGIENE, AGENTS, CLAUDE, the charter template, SKILL or DECISIONS.
- content: everything else.

**P6 — test C.** Same classes, over subagent calls before the first output.

## 4. Gaps

- **HIGH.** Kickoff Step 1 makes the agent re-derive what the card already printed (`SKILL.md:51-56`). Sessions where the card was recorded ran a median of 8 state calls before writing, against 3 for sessions without it; 18 of 19 ran at least one.
- **HIGH.** No `next` verb exists (absent: grep of `--next`, `verb_next` and `'next')` over `tools` and `skills`). Locating the work costs a median of 4 calls per new session, 307 in total, 13%.
- **HIGH.** A resume rebuilds the whole cache: median fresh input is 467k tokens against 146k for a new session, though it needs only 4 calls.
- **MED.** The card does not name the build, step, unit or next action. Its `live —` cell is only a count (`manifest-check.sh:529`).
- **MED.** The READY card is rarely appended: 19 of 64 sessions, and only 2 before their first write. A replay or a subagent therefore inherits no scope (P3).
- **MED.** Handoff briefs carry Protocols as pointers (`roles_lib.py:67`). Briefed agents spend 15.1% of their calls on method docs, against 7.3% for unbriefed ones (P6, n=34 briefed).
- **MED.** Subagents re-read content they already carry: `AGENTS.md` 123 times, their own prompt file 10 times (P4).
- **LOW.** The resume-tick path was never exercised on this node: 0 `claude -p` launches and no sidecar, so tick cost cannot be measured (P2).
- **LOW.** 106 of 109 scheduled wakes did nothing and spent 0 tokens; the cost there is noise in the transcript, not tokens (P2).

## 5. Candidates

**A — Richer pushed card.** Add the build, step, unit, LIVE rows and next action to the startup and replay cards.
- **Seam:** `skills/session-kickoff/manifest-check.sh` `render_card` and `print_replay`.
- **Losing test:** sessions that had the card in context should run no fewer card-answerable calls than those without. If so, pushed content is not consumed and A loses.
- **Result: LOSES.** With the card the median was 8 calls (p90 23); without it, 3 (p90 10).
- **Caveat:** this is confounded by Step 1 ordering the re-derivation. A only helps if Step 1 is rewritten too.

**B — A `next` verb, pulled in one call.** It returns build, step, unit, next action, the read set, and HEAD/BASE fresh at call time. Commands end with a `next —` line.
- **Seam:** `unattended.sh` `verb_status` (it already derives the first non-terminal unit) together with the card's `--replay` `now —` line.
- **Losing test:** B loses if the locate-plus-state calls it would replace are at most 1 per new session, or under 10% of pre-productive calls.
- **Result: PASSES.**
  - New sessions: locate median 4 (p90 11) plus state median 1 (p90 6), 20% of 2,282 calls.
  - Resume: 28%, but a median of 0.
  - Compact: 11%, median 0.
- **Estimated saving:** about 4 calls per new session. At about 100k cache-read tokens per call (3.5M ÷ 35), that is about 400k cache-read tokens. In total it is up to 461 calls (20%); the saving on resume and compact is small.

**C — A brief that carries its facts.** The handoff inlines the protocol and record excerpts the role needs, instead of trigger pointers, and stops listing auto-loaded files.
- **Seam:** `tools/roles/handoff.py` render and `roles_lib.py:67` `CARRIED_SECTIONS`.
- **Losing test:** C loses if method plus carried-file reads are under 10% of subagent calls before output.
- **Result: LOSES on the whole population, wins for briefed roles.** Overall it is 7.4% of calls and 6.6% of returned chars. For handoff-briefed roles it is 15.1% method plus 14.9% locate (n=34).
- **Estimated saving:** about 136 carried re-reads, plus about 15% of a briefed agent's calls (about 4 of a median 28).

## 6. Pick

My pick is B: the `next` verb with a `next —` line, plus a Step 1 that consumes its answer. It is the only candidate whose losing test passed on the full population. It answers the locate and state calls that cost new sessions 20% of their pre-productive calls (median 5 per session, about 400k cache-read tokens).

A failed its test: the card already in context did not stop re-derivation, so pushing more content into it is not consumed while Step 1 mandates recomputing. C is worth pairing with B only for handoff-briefed roles, where it passed. Neither candidate addresses the largest per-entry cost I measured, the 467k-token cache rebuild on resume. I hand that to the step-resolution researcher, who covers how a resumed session re-enters the flow.
