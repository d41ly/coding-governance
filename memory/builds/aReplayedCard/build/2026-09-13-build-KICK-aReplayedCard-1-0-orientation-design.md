# Orientation design — the synthesized study this build implements

**Serves:** research KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

node a · 2026-09-13 · order 0 · streams kickoff+tooling

Produced in the attended session that opened this run by a 13-agent study: five readers, three
independent designers, four batched skeptics, one synthesis. Copied from the scratchpad verbatim
below this header, because the prompt record names a path outside the repository. The owner
decisions recorded in the prompt record resolve section 7 of this document; where the two disagree,
the prompt record wins. Section 2.8 designs the stage-2 subagent this build does NOT ship.

---

# Session orientation — synthesized design

Repo: coding-governance, worktree `session-orientation-tooling-2faa9f` at 5677452c, 2026-09-13.
Inputs: the owner objective, the UNDERSTAND map (five readers), three designs (D1 enforcement, D2
context economy, D3 YAGNI card), and 44 skeptic verdicts (appendix). Every number below names its
source; a number with no source is not here.

## 1. Verdict on the objective as stated

**What makes sense.** Orientation is the weakest-measured stage in the repo: no end-to-end cost of
a kickoff exists, nothing observes compaction, and the only enforced step-0 today is a wiring check
that orients nothing (`tools/check-wiring.sh --session`, 753 B, 35–81 s measured across three
readers). The three concerns in the objective — relevance, compaction retention, between-turn
retention — are real, and two of the three are answerable from the harness docs alone.

**What is wrong or overstated**, with the verdict ids that settle it:

- *"Called FIRST (enforced)"* cannot be literal. SessionStart runs only `command`/`mcp_tool` hooks
  and cannot block (harness facts, appendix "harness" area). In an unattended run the keepalive is
  first by protocol, and that is bound by `--preflight` refusing without `--keepalive-id`, not by any
  check (verdict 43, refuted D3's attribution to checks 18/20). "First" therefore means **before the
  session's first durable act**, which a PreToolUse deny on commit-shaped commands gives — and a
  read-only or conversational session then pays nothing.
- *"Executes memory-recall / reuse audit / lexicon / map"* — lexicon is a measured dead probe for
  orientation (`.lexicon.conf` declares md and sh dark; `--suggest` has no input before a name
  exists; aGroundedOrientation README:39-45). reuse_lookup's measured precision is 0.056 with hit@1
  6 % (aWeighedCompass Finding 6) and shell is dark to it, so it earns a "sources to open" row at
  best. drift_report is task-independent and 32–36 s; it is a bar question, not an orientation one.
- *"Reads all the relevant files and code"* is the wrong target. The charter's session-start reading
  order for a tooling session is 498 982 B today, 74 % of it one backlog shard (`wc -c` on the five
  files, map area 3). An agent that ingests that is the garbage the objective complains about. The
  artifact must **cite** `path:line` and record ids; the reader opens one slice per claim it uses,
  which is what the charter's "recalled memory is background, re-verify before acting" already
  demands (AGENTS.md §5).
- *"Reviews it for accuracy"* as a second reading is a self-grade. What is mechanically checkable is
  that every cited path, line and id **exists**; what no reviewer can check cheaply is that the
  claim is true at that line. The design does the first with one batched git call (verdict 40 sets
  the cost) and leaves the second to verify-before-act.
- *"Feeds it to the main session"* is only half the retention story: hook-added context is
  **summarized** at compaction; the one documented verbatim re-injection point is a SessionStart
  hook with matcher `compact` (verdicts 3, 16, 24, 42). Between compactions nothing is lost; there
  is no per-turn eviction to defend against.
- *The garbage is precision, not location.* Moving low-precision probe output into a subagent hides
  the noise; it cannot raise the precision, which is aTunedCompass's blocked work (unit 9 fixture).
- *The subagent is not free.* A custom or general-purpose subagent loads every CLAUDE.md level —
  AGENTS.md at 64 347 B — before it reads a probe, spends one of the five per-prompt agent-cap slots
  (verdict 39), and cannot ask a question (verdict 20). It buys main-context **occupancy**, not
  total spend. The Explore built-in type skips CLAUDE.md (verdict 38 refuted D3's blanket
  deferral), but then the charter does not bind it — see §7 decision 2.

Refuted claims that shaped the recommendation: 13 (a node hook costs a git spawn on node a, so no
second per-call spawn), 18 (key the subagent allow on `agent_id`, never `agent_type`), 20 (the
engine does not run unchanged inside a subagent), 35 (the card costs 45–50 s on a loaded host if it
runs the manifest audit), 40 (per-token git loops cost 25–50 s), 41 (node tag matches the
Machine/user cell only), 43 (keepalive ordering is driver-enforced), 14 and 27 (checks 18/20 derive
order at run time from first-occurrence literals — a hazard, not a line-number pin).

## 2. Recommended design

**Shape.** D2's shape (a small cited artifact on disk, re-injected verbatim after compaction, a
subagent that absorbs the probe dump, a deny at the first durable act), built in two stages so that
the first stage stands alone and is the lazy thing that solves the measured problems. D3's
deterministic card is stage 1's writer; D1's "the script writes the liveness rows, the model only
curates" is the property both stages keep; D1's sha256 signature and five-verb hook are dropped as
protection against evasion the repo's other hooks do not attempt either (agent-cap's posture:
stops forgetting, not evasion).

- **Stage 1 (build now):** the orientation card, written by a verb on the checker that already
  ships beside the engine, injected at SessionStart, replayed on `compact`/`resume`, appended-to by
  the engine's Step 5 with a batched citation check, and a deny on commit-shaped Bash commands until
  the session's card carries a `READY —` line. No subagent. No new hook process.
- **Stage 2 (build when §7 decision 1 says so):** the `orient` subagent that runs engine Steps 0–4
  in its own context and appends the curated, cited sections to the same card; the main loop then
  holds the card and the READY line and nothing else of orientation.

### 2.1 Mechanism

One artifact, one writer, three readers, one deny.

**The card** (see 2.5) lives under the git common dir, keyed by `session_id`. The **writer** is
`bash <check-script> --card …` — a verb on `skills/session-kickoff/manifest-check.sh`, which the
engine already resolves via `check-script:` and adopters already copy; it is already in the
manifest's `watch:` list, so adding the verb costs zero manifest bytes where a new file would have
cost a `watch:` literal against 5 B of headroom (`tr -d '\r' < memory/guides/SESSION-KICKOFF.md |
wc -c` → 25595 vs `MAX_MANIFEST_BYTES` 25600).

Verbs:

```
--card                       write + print (SessionStart startup|clear)
--card --replay              print the card + one live `now —` line (SessionStart resume|compact)
--card --append              stdin → citation-checked, appended (engine Step 5/5b; stage-2 agent)
--card --check               re-run the citation check over the whole card, exit 1 on a miss (stage-2 SubagentStop)
--card --waive "<reason>"    append a dated waiver line (the visible bypass)
--card --path                print the path
```

`session_id` comes from the hook's stdin JSON on the SessionStart paths; `--append`/`--check` take
`--session <sid>` (the engine copies it from the card header already in context) and fall back to
`$GOV_SESSION_ID`, which `--card` writes to `$CLAUDE_ENV_FILE` at startup. UNVERIFIED: whether
`CLAUDE_ENV_FILE` exports reach a subagent's Bash — settled by printing `$GOV_SESSION_ID` from inside
a spawned agent; the explicit `--session` is the channel that does not depend on it.

**What the card does at startup** is the task-independent, script-shaped part only: the Step 1 git
batch (branch, status, HEAD as BASE, worktree list — 1961 B in 1.6 s quiet, map area 1; ~5–6 s on
the loaded host per verdict 35), the node tag from the registry, the `memory/LIVE.md` non-terminal
count, `git log --oneline -5`. **It does not run the manifest audit.** D3 put the 21 s audit at every
session start; measured on the loaded host it is 41–44 s (verdict 35), the drift it catches is
already caught at the commit and push boundaries by the `--staged` and full checker runs, and a
session that never kicks off should not pay for it. The audit stays in engine Step 2b and its verdict
rides the `--append`.

**Readers:** the main session (hook stdout at startup, ≤ 8192 B inline — verdicts 6, 16, 32); the
engine (Step 1 consumes the card instead of re-running the batch; Step 5 appends); the deny (reads
the file, never the context).

**The deny** is one added check inside `tools/hooks/scratch-guard.js`, which already spawns on every
`Bash|PowerShell` call. Verdict 13 measured a node spawn at 0.8–1.1 s on node a — the same as a git
spawn — so a second hook file on the same matcher would double the per-call cost of every Bash call;
folding the check into the existing spawn costs one `fs.readFileSync` and a regex. The check fires
only when the command matches `\bgit\b.*\b(commit|merge|push)\b` and the payload has no `agent_id`
(verdict 18: `agent_type` is present on a `claude --agent` main loop too). It reads
`<common>/orientation/<session_id>.md`, requires a `READY —` line (or a `waived —` line) and a
`tree —` cell equal to the toplevel derived from the payload's cwd by the same `.git` walk
agent-cap already implements, and otherwise exits 2 with the reason on stderr: the card path, which
condition failed, and the one remedy (`/session-kickoff`, or `--card --waive "<why>"`). The reason
reaches the model and the deny holds under `--dangerously-skip-permissions` (verdicts 7, 19). Fail
open silently when `session_id` or `tool_use_id` is absent, mirroring agent-cap. Declared ceiling in
the file header: a commit made by a script, a redirect, or a non-git tool escapes — the guard stops
forgetting, not evasion.

Why commit-shaped commands and not Edit/Write: Edit and Write pay no hook today, so gating them adds
a ~1 s spawn to every edit (verdict 13); an unoriented edit that is never committed changes nothing
durable; and the charter's landing rules already make the commit the unit of record. This also
leaves a read-only session and the `orient` agent's own probes entirely free.

### 2.2 Attended sequence

1. SessionStart `startup` → existing `check-wiring --session` (now with matcher `startup|resume|clear`)
   and procmon, plus `--card`: ≤ 8192 B lands in context, opening with
   `orientation — <sid> · …` and ending `READY — none yet`.
2. The user works. Read/Grep/Glob/Bash probes are free. The first `git commit` without a READY line
   is denied with the remedy in the reason.
3. `/session-kickoff`: Step 0 unchanged; Step 1 consumes the card (one clause — the engine already
   says "a SessionStart hook may already have reported worktree/branch state. Consume, don't
   recompute", SKILL.md:26-28, which has had no live source until now); Step 2/2b/3/4 as today
   (manifest read once, audit, skeleton, dossier, gotchas `--for-paths`, one recall query, slug mint
   in the main loop per §2); Step 5 emits the READY micro-format and pipes it, with the manifest-audit
   delta, the gotcha class names, the recall ids it judged binding, and the `## open` rows, to
   `--card --append --session <sid>`. The append runs the batched citation check (2.6) and refuses an
   over-cap body with exit 2, printing the overage. Then STOP, as today.
4. Stage 2 replaces step 3's Steps 0–4 with one `Agent(subagent_type: orient)` spawn; the agent
   appends its sections; the main loop resumes at Step 5 (2.7).

### 2.3 Unattended start sequence

The card is the **harness's** act (SessionStart fires in `-p`, verdicts 5, 34; not with `--bare`), so
it precedes the run's first act without moving the step table. The keepalive stays the run's first
act, bound as today by `unattended.sh --preflight` `fail 8` (verdict 43).

- SLUG path: keepalive → BUILD-METHOD whole → roster → waiver ask → `--preflight` → `/session-kickoff`
  after preflight (check 18 holds because the template is untouched in stage 1) → Step 5b emits READY,
  appends it plus the build slug and run-state path to the card, loads BUILD-METHOD, continues. The
  run's first commit now passes the deny.
- PROMPT and PLAYBOOK paths: keepalive → orient from the prose and RUN the probes before the roster
  (unchanged; the check-20 literals stay where they are) → ask once → write the build folder →
  **commit + push** → `--preflight` → kickoff. That commit precedes kickoff, so the deny would refuse
  it. Two resolutions, §7 decision 3: (a) the prompt path's step-1 orientation ends with
  `--card --append` of its own probe summary plus a `READY — <slug> · prompt-path` line, which is
  what "RUN the orientation probes HERE" already produces in prose (TOOL-aGroundedOrientation-1); or
  (b) the deny exempts a commit whose cwd holds a build folder with `authorized-by: prompt` — more
  logic in a hook for one path. (a) is recommended; it changes one sentence inside the prompt section
  and must not add a `/session-kickoff` mention above template line 175 (verdict 14).
- Stage 2 on the prompt/playbook paths: step 1 becomes "spawn `orient` with the prose as its task";
  the literal `RUN the orientation probes` stays inside the prompt section, naming the agent as the
  runner (verdict 27 lists the five section-scoped literals check 20 needs).

### 2.4 Resume-after-compaction sequence

- **Compaction, same process (attended or unattended):** SessionStart `compact` → `--card --replay`
  prints the card plus `now — HEAD <sha> · <branch> · clean|dirty`, ~0.2 s (D3's estimate; the
  file read is trivial, the one git call for `now` is the cost — budget one git spawn, 0.75–1.1 s on
  node a). check-wiring and procmon no longer run here. M7's regrounding list is not extended: the
  card arrives without anyone reading, and RUN.md stays the on-disk truth for a run.
- **`--resume`/`--continue` of a session:** same `session_id` (verdicts 4, 17, 33), same replay. A
  `--fork-session`/`/branch` mints a new id and gets a fresh card with `READY — none yet`.
- **Resume after process death (unattended, new session):** `startup` → fresh card → reap the
  keepalive, schedule the replacement → `unattended.sh --resume <slug>` → today's resume section
  reads RUN.md and works, and its first commit would now be denied. The resume section gains
  `/session-kickoff` after `--resume` (Step 5b fires on the live non-terminal run-state file and
  appends READY); the mention sits in the resume section, far below the first `--preflight`, so
  check 18 is unaffected. This is D1's improvement: a resumed run re-reads the manifest and re-runs
  the probes, which it never did before (map area 2).

### 2.5 The orientation artifact

- **Name / location:** `<git-common-dir>/orientation/<session_id>.md`. Same lifecycle class as
  `<common>/recall/queries.jsonl` and `<common>/agent-cap/` (verdicts 29, 44): untracked, never
  pushed, invisible to every hygiene, coverage and lexicon leg, and the worktree stays clean for
  `check_clean`. The common dir is shared by all worktrees, so the card carries its `tree —` cell and
  the deny compares it (verdict 44 caveat).
- **Byte cap:** 8192 B, LF, one constant in the checker verb. Under the harness's 10 000-character
  inline threshold (verdicts 6, 16 — characters, so bytes ≥ chars is the safe direction) and under
  the 5 000-token per-skill re-attach cap. `--append` refuses a breach with exit 2 and leaves the file
  as it was; the refusal prints, so a skip announces itself.
- **Writer:** the checker verb only. Stage 1: `--card` at startup, `--append` from engine Step 5/5b
  (and the prompt-path step 1). Stage 2: `--append` from the `orient` agent as well. The model never
  writes the file directly (the agent has no Write/Edit; the main loop is asked not to, and a
  hand-written card is the evasion class the deny does not chase).
- **Readers and re-injection points:** the main session at `startup`/`clear` (written and printed),
  at `compact`/`resume` (replayed verbatim + `now`); the engine at Step 1 (consume) and Step 5
  (append); the deny at every commit-shaped Bash call; the stage-2 SubagentStop hook at `--check`.
- **Shape** (every startup field DERIVED; appended sections are cited rows, never paraphrase;
  prose is factual statements because imperative hook text can trip prompt-injection defenses —
  harness area):

```
orientation — <session_id> · written <iso> · by manifest-check.sh --card
node — <tag> · <machine/user>          | node — UNKNOWN: no Machine/user cell matches <user>
tree — <toplevel> · primary|worktree · branch <b> · BASE <sha> · clean|dirty <n>
ff — moved <old>..<new> | unchanged | skipped: <why>
worktrees — <n>
live — memory/LIVE.md · <n> non-terminal builds
recent — <git log --oneline -5>
READY — none yet
## task      the checker's sealed skeleton fields as derived, or "unfillable: <field> — <why>"   (appended)
## manifest  <path> · audit ok|FAIL <files> · watch-commits-since-stamp <n> · unaudited flag when machine-global   (appended)
## read      ≤12 rows `path:lo-hi — why` (pointer-map row docs SLICED, dossier, first entrypoints)   (appended)
## records   ≤8 rows `ID — one clause — path:line` from the recall query; `Recall terms used:` line   (appended)
## classes   gotchas class names from --for-paths over the entrypoints, one line   (appended)
## open      parked fields, questions, the six interactive exits when unattended   (appended)
READY — <slug> · node <tag> · <branch> · base <sha> · Tier-<n> · gates <list>   (appended; replaces "none yet")
waived — <iso> · <reason>   (only after --waive)
now — HEAD <sha> · <branch> · clean|dirty   (stdout only at --replay, never stored)
```

The node tag resolves by matching `$USERNAME` against the **Machine/user cell** of the registry
table named on the hook command line (`--registry AGENTS.md`, project config, not a kit literal);
rows a and d carry no hostname, and a row-wide match on `d41ly` hits every row through the Remote
column (verdict 41). No unique cell match → `UNKNOWN`, printed, never guessed.

Relevance is keyed the way `gotchas.py --for-paths` keys: the pointer-map row the task names gives
the entrypoint paths; a candidate row (recall hit, doc slice, trap bullet) is kept only when it
names one of those path tokens or the row's id family, and the cap forces the residue out.
UNVERIFIED that this keeps the relevant rows (verdict 30): settled by running the append on three
past units with known §10 seams and grading `## records` and `## read` against them.

### 2.6 Enforcement — hook, deny, and the gate that proves it RED

- **Hook:** the added check in `tools/hooks/scratch-guard.js` (PreToolUse, existing matcher
  `Bash|PowerShell`). Header states what it does NOT check: commits by scripts or non-git tools, a
  hand-written card, MCP tools, and that a READY line is *correct*.
- **Deny:** exit 2, reason on stderr, on a commit-shaped command from a payload without `agent_id`
  whose session card lacks `READY —`/`waived —` or whose `tree —` cell is not the payload's toplevel.
  Fail open on a missing `session_id`/`tool_use_id`, silently, like agent-cap.
- **Gate that proves it RED:** two legs.
  1. `tools/hooks/scratch-guard.test.sh` (exists; kit self-test, off the bar by the 2026-08-23
     ruling, run via `GATE_SELFTESTS=1` or on demand) gains arms, each observed RED before landing:
     commit with no card → 2; card without READY → 2; card with READY → 0; `waived —` → 0;
     `tree —` mismatch → 2; payload with `agent_id` → 0; missing `session_id` → 0 (fail-open asserted,
     not assumed); non-commit Bash with no card → 0.
  2. `tools/check-wiring.sh` gains a `card` arm on the recall-arm pattern (R, `tools/check-wiring.sh`
     ~L434): fragment present and the SessionStart entries absent or lacking their matchers →
     UNWIRED. This is a bar leg on the subject repo; RED observed by staging `.claude/settings.json`
     without each entry. A misspelled SessionStart matcher never fires and looks wired, which is
     exactly the case this arm exists for.
  3. `skills/session-kickoff/manifest-check.test.sh` gains: an over-cap `--append` → exit 2 and the
     file byte-identical; an unknown id → an `UNVERIFIED —` line beneath the row; a citation-free
     append → `DEAD PROBE: nothing to check`, exit 1.

### 2.7 The accuracy review

Mechanical existence, batched, then the charter's verify-before-act.

`--append` extracts every path-shaped token and every `[A-Z]+-[A-Za-z]+-[0-9]+` id from stdin and
runs **one** `git ls-files -- <paths>` and **one** `git grep -l -F -f <tokenfile>` — verdict 40
measured the per-token loop at 25–50 s for 30 tokens on node a and the batched pair at ~1.1 s. A
`path:lo-hi` whose `hi` exceeds the file's line count is a miss. A miss is never dropped: the row is
kept and one `UNVERIFIED — <token>` line is added beneath it. Zero tokens → `DEAD PROBE`, exit 1 — a
probe that cannot move says so. The verb header states what it does not check: relevance, scope
correctness, tier, and truth at the cited line.

Stage 2 adds a SubagentStop hook, matcher `orient`, running `--card --check --session <sid>`; on
exit 1 it returns `{"decision":"block","reason":"<miss list>"}` so the agent fixes its own citations
(verdicts 8, 22). It must honor `stop_hook_active`; the harness caps consecutive continuations at 8,
so an unfixable map ends rather than loops. A second LLM pass is rejected in both designs that
considered it: another slot, another ~60 KB of reads, and it cannot see truth either.

### 2.8 Stage 2 — the `orient` subagent (designed here, built on §7 decision 1)

- **Definition:** `.claude/agents/orient.md` (no `.claude/agents/` exists today). Frontmatter:
  `name: orient`, `tools: Read, Grep, Glob, Bash`, no Write/Edit/Agent/Workflow, no
  `isolation: worktree` (verdict 28 — that would orient on a worktree branched from the default
  branch, not the session's HEAD), `maxTurns` bounded, `model: inherit` until measured (D2's sonnet
  choice is a recall-quality risk: r@20 0.614 with terms vs 0.446 without, n=83, dTracedLattice).
- **Body:** invoke the `session-kickoff` Skill and run Steps 0–4 for the task given; every
  `AskUserQuestion` exit becomes an `## open` row (verdict 20: the tool is removed from every
  subagent, so this restated rule is unavoidable and is three lines); never mint the slug (§2);
  select by the pointer-map row's entrypoints; cite, never ingest; end by `--card --append
  --session <sid>` and return the card body as the final message (verdict 21: the Agent tool returns
  the final text intact; a `maxTurns` or rate-limit cut returns PARTIAL text, so the presence of the
  appended sections in the file, not the returned text, is the acceptance test).
- **Deny interplay:** the agent's Bash calls carry `agent_id`, so the deny never touches them
  (verdict 1); probes invoked by the worktree's own relative path log the worktree the reuse-probed
  DoD item joins on (verdict 12 caveat: an absolute path into the primary tree logs the primary).
- **agent-cap:** one of five slots on the spawning prompt, no exemption (verdicts 23, 39), reclaimed
  45 min after the claim; a review that starts within 45 min has four.
- **Engine change:** Step 0 gains one clause — a card without READY and a project that ships
  `orient` → spawn it, wait, continue at Step 5. UNVERIFIED that the clause fits the engine's 207 B
  of headroom (`bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` → 18225/18432,
  verdicts 26, 37); settled by drafting it and running the gate; D1's split of Steps 0–2b/4 into the
  agent definition with its own size leg is the fallback when it does not.
- **memory-recall Skill line** ("while /session-kickoff is running, run the probes that skill asks
  for rather than pre-empting them") is re-rendered to name the agent as the runner; one line, both
  template and rendered copy, so the byte-compare gate stays green.

### 2.9 What the main session holds, before and after (bytes, `wc -c`; tokens unmeasured)

| Event | Today | Stage 1 | Stage 2 |
|---|---|---|---|
| Session start injection | 753 B (check-wiring) | 753 B + card (expected ~2 KB, cap 8192) | same |
| Session start wall | 35–81 s (check-wiring, three readers) + ~6 s procmon | + ~1.6 s quiet / 5–6 s loaded for the git batch (verdict 35) | same |
| Attended kickoff, main context | 69 041 B minimum: SKILL.md 18225 + manifest 25595 + Step 1 batch 1961 + `--locations` 60 + `--task-skeleton` 369 + dossier 4465 + gotchas 1325 + recall 17041 (map areas 1, 3) | 67 080 B (Step 1 batch consumed from the card) | ≈ 18225 (SKILL.md, still invoked in main) + card ≤ 8192; the manifest, dossier, gotchas and recall dump (≈ 48 KB) move to the child |
| Child context | — | — | AGENTS.md 64 347 + the ≈ 48 KB above + its own turns; net total spend UP on turn 1 |
| After compaction | 0 orientation bytes verbatim; check-wiring re-runs, 35–81 s, 753 B | card ≤ 8192 verbatim + `now`; 0 s check-wiring | same |
| Between turns | nothing evicted | nothing evicted | same |
| Agent slots | 0 | 0 | 1 of 5 on the spawning prompt, 45 min |

Stage 2's saving is main-context occupancy of ≈ 48 KB per attended kickoff and the unattended
prompt path's double orientation (probes at step 1, Step 4 again at the hand-back — map area 2).
Whether that occupancy costs anything measurable is the counterfactual nobody has run
(aWeighedCompass §8, dTracedLattice §7); §7 decision 1 asks the owner to buy the measurement or the
build.

## 3. Components

| Name | Kind | File | Change | Reuses |
|---|---|---|---|---|
| card verb | script | `skills/session-kickoff/manifest-check.sh` | `--card [--replay\|--append\|--check\|--waive\|--path] [--session] [--registry]`; 8192 B cap; batched citation check; `UNVERIFIED —` annotation; `DEAD PROBE` on zero tokens; header names what it does not check | the checker's existing `--locations`/`--task-skeleton` verb pattern, its `show-toplevel` anchoring, its place in the manifest `watch:` list |
| card tests | gate (kit self-test) | `skills/session-kickoff/manifest-check.test.sh` | over-cap append RED; unknown id → UNVERIFIED; zero-token → DEAD PROBE | existing test file |
| commit deny | hook | `tools/hooks/scratch-guard.js` | one check on commit-shaped commands from non-`agent_id` payloads: READY/waived line + `tree —` match; exit 2 + reason; fail-open on missing keys; ceiling in header | the already-spawned PreToolUse process; agent-cap's `.git` walk and fail-open shape |
| deny tests | gate (kit self-test) | `tools/hooks/scratch-guard.test.sh` | the eight arms in 2.6, each observed RED then GREEN | existing test file |
| SessionStart wiring | hook | `.claude/settings.json` | matcher `startup\|resume\|clear` on the check-wiring and procmon entries; new `startup\|clear` → `--card --registry AGENTS.md`; new `resume\|compact` → `--card --replay` | existing entries |
| settings fragment | script | `skills/session-kickoff/orientation-card.fragment.json` | the two SessionStart entries in the `recall-opened.fragment.json` shape | `tools/settings-merge.py --fragment` |
| wiring arm | gate (bar leg) | `tools/check-wiring.sh` | `card` row: fragment present + entries/matchers absent → UNWIRED; RED staged | the recall arm R |
| engine consume + append | skill-edit | `skills/session-kickoff/SKILL.md` | Step 1: a card in context satisfies the step; Step 5/5b: pipe READY + audit delta + classes + record ids + open rows to `--card --append` | the existing "consume, don't recompute" hedge at L26-28 (near-zero bytes); must fit 207 B or trim (UNVERIFIED, verdict 37) |
| manifest re-stamp | doc | `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped with the delta line in the commit; no body change | C5 ratchet (SKILL.md and the checker are watched) |
| unattended resume line | skill-edit | `tools/unattended/SKILL.template.md` (+ rendered `.claude/skills/unattended/SKILL.md`) | resume section: `/session-kickoff` after `--resume`; prompt-path step 1: append its probe summary + READY (decision 3a) | check 18/20 literals untouched; nothing above template L175 mentions `/session-kickoff` |
| dossier refresh | doc | `memory/map/features/session-kickoff.md` | claim the new keys; record the card's home, cap, matchers | codebase-map coverage leg |
| runbook | doc | `WIRE-INTO-PROJECT.md` | one step: fragment merge, check-wiring; states the deny's ceiling and the waive verb; without the hook the wrapper is a request | — |
| orient agent (stage 2) | subagent-def | `.claude/agents/orient.md` | as 2.8 | the session-kickoff Skill via the Skill tool; the card verb |
| orient stop hook (stage 2) | hook | `.claude/settings.json` | SubagentStop matcher `orient` → `--card --check`, block with miss list | the card verb |
| recall Skill line (stage 2) | skill-edit | `tools/memory-recall/SKILL.template.md` (+ rendered) | name the agent as the probe runner | the byte-compare render gate |

Bookkeeping found in passing, same unit: backlog rows TOOL-aWeighedCompass-14 and -15 read OPEN
while the manifest carries their fix (`grep -c recall memory/guides/SESSION-KICKOFF.md` → 1; the
tooling entrypoint reworded at L116) — close them.

## 4. Improvement points over the objective, ranked

1. **Enforce at the first durable act, not at session start.** SessionStart cannot run an agent or
   block; a commit-shaped deny with the remedy in its reason binds attended and unattended sessions
   alike, holds under permission bypass, and costs a read-only session nothing.
2. **Solve retention at the seam that re-injects verbatim.** Hook context is summarized; a
   SessionStart `compact` hook is the documented pin. Put the artifact on disk under the inline cap.
3. **Give the two existing SessionStart entries matchers.** check-wiring runs on every compaction
   today for 753 B of wiring rows at 35–81 s; this is the largest measured saving in any of the
   three designs and needs nothing else.
4. **Cite, do not ingest; verify existence, not prose.** The map is identifiers with `path:line`;
   one batched git call checks they exist; the reader opens a slice per claim it uses.
5. **Derive what is script-shaped once per session** (branch, BASE, node tag, worktrees, LIVE count)
   and let the engine consume it — its own rule since cKeyedLaunchpad, with no live source until now.
6. **Keep the manifest audit at kickoff, not at every start.** 41–44 s on the loaded host (verdict
   35); the ratchets at the commit and push boundaries already catch the drift.
7. **Resume-after-death re-orients.** A resumed unattended run never re-read the manifest or re-ran
   a probe; kickoff after `--resume` fixes that at the cost of one kickoff.
8. **The subagent is a second stage with a measurement in front of it**, not the first build: it
   buys occupancy, spends a slot and a 64 KB child load, cannot ask, and does not raise probe
   precision.
9. **Drop lexicon and drift_report from the probe set** on measurement; treat reuse_lookup rows as
   "sources to open".
10. **The largest per-kickoff byte cut needs no mechanism:** the manifest's traps section is
    12 973 B of 25 595 (`sed`/`wc` slices, map area 1), global bullets with no prune-when condition,
    22 of them path-bearing and therefore keyable by `gotchas.py --for-paths`. Evicting those is a
    separate unit (D3's U4).

## 5. Risks and the compensating check for each

| Risk | Compensating check |
|---|---|
| Deny-forever if the READY predicate is wrong for every card | the deny reason prints the failing condition and card path; `--waive` is the visible bypass, replayed after every compaction; the self-test arms observe every predicate branch |
| A doc-only session is denied its commit without a kickoff | `--waive "<reason>"`; §7 decision 4 |
| The prompt path's build-folder commit precedes kickoff | decision 3; the check-20 arm keeps "RUN the orientation probes" ahead of "Write the build folder" |
| Card from a sibling worktree read through the shared common dir | `tree —` cell compared to the payload's toplevel; mismatch denies with "oriented in A, committing in B" |
| `session_id` changes on `--fork-session`/`/branch` | fresh card prints `READY — none yet`; the deny asks for a kickoff |
| An id that exists but is irrelevant passes the existence check and reads as vetted | the verb header states it checks existence only; `UNVERIFIED` is the only annotation, absence of it is not relevance |
| The engine clauses do not fit 207 B | UNVERIFIED (verdicts 26, 37); draft, `wc -c`, run `tools/check-template-size.sh`; fallback is D1's split with its own size leg |
| Hook-injected `READY —`/`now —` lines read as imperative | lines are factual statements; unmeasured; check the transcript after one compaction |
| Card counts against the 25 000-token skill re-attach budget | undocumented (harness gap); an 8 KB card is small against it; observe one compaction with a loaded skill |
| A new `/session-kickoff` mention above template L175 reds check 18 | verdict 14; the only template edits sit in the prompt section and the resume section; run `bash tools/unattended/check-unattended.sh` (it exceeded 100 s for the skeptic — not a cheap check, budget it) |
| CLAUDE_ENV_FILE does not reach a subagent's Bash (stage 2) | explicit `--session <sid>` from the card header is the channel; the env var is a convenience |
| Stage-2 agent returns partial text | the appended sections in the file are the acceptance test, never the returned text |
| Stage-2 slot held for 45 min | a review starting inside 45 min has four slots; declared, not hidden |

## 6. What NOT to build — the cuts, each with its upgrade trigger

- **The orient subagent (stage 2)** — until §7 decision 1: two matched kickoffs, inline vs agent,
  total tokens and wall to READY, show the occupancy saving is worth a slot and a 64 KB child load.
- **A signed artifact and a five-verb hook file (D1)** — the sha256 stamp, the `stale` marker, the
  TTL sweep, the conf-token backstop. Trigger: a session observed hand-writing or editing a card to
  pass the deny, i.e. evasion rather than forgetting.
- **Gating Edit/Write** — trigger: an unoriented edit observed causing a rebuild that a commit-time
  deny would not have caught; cost is a ~1 s node spawn per edit (verdict 13).
- **The manifest audit at every session start (D3)** — trigger: manifest drift observed reaching a
  commit that the `--staged` checker did not catch.
- **A second LLM refuter over the card** — trigger: a resolved-but-false citation observed causing a
  wrong action that verify-before-act did not catch.
- **Adding the card to M7's regrounding list** — the compact hook delivers the same bytes; the list
  is closed by design. Trigger: none foreseeable.
- **A per-worktree fallback card for resumed-after-death sessions** — trigger: the one kickoff a
  resumed run now pays measured as a real cost.
- **Cutting recall `--k`/`--budget`** — the measured value of depth is r@20; it is aTunedCompass's
  fixture question.
- **Any charter, template or manifest-body change** — all three carriers sit at their ceilings
  (267 B, 207 B, 5 B — `check-template-size.sh`, `wc -c`); aWeighedCompass F12 wrote every
  recommendation to need no charter change.
- **`agent`/`initialPrompt` as the always-first mechanism, `context: fork`, a UserPromptSubmit gate,
  a PreCompact hook** — each rejected on documented harness properties (appendix); no trigger.

## 7. Open decisions for the owner

1. **Build stage 2 now, or after the counterfactual?** Stage 1 solves retention, cost and
   enforcement; stage 2 buys ≈ 48 KB of main-context occupancy per kickoff at one slot, a 64 KB child
   load, and no ask capability. Nothing in the repo measures whether occupancy matters.
2. **If stage 2: custom `orient` agent (gets the charter, costs 64 KB, `subagent_type` is
   distinguishable) or Explore-typed (skips CLAUDE.md, charter does not bind it, every Explore spawn
   looks the same to a hook)?** UNVERIFIED whether Explore can run Bash and the Skill tool; settle
   with one spawn.
3. **Prompt-path commit before kickoff:** (a) the step-1 orientation appends its own READY line —
   one sentence in the prompt section; or (b) the deny exempts `authorized-by: prompt` build-folder
   commits — hook logic for one path. Recommended (a).
4. **Doc-only sessions:** pay a kickoff, or `--waive`? The waiver is visible on every replay; the
   alternative is no deny at all (D3's default).
5. **The traps eviction (U4)** as a separate unit: 22 path-bearing bullets out of the manifest into
   `memory/gotchas/`, the largest per-kickoff byte cut available.

## 8. Appendix — every claim, its verdict, its evidence (by id)

| id | design | claim (short) | verdict | evidence / correction |
|---|---|---|---|---|
| 1 | D1 | PreToolUse payload inside a subagent carries `agent_id`/`agent_type` | confirmed | hooks doc L267, L767-768; only `agent_id` is subagent-exclusive |
| 2 | D1 | Agent `tool_input` carries `subagent_type` | confirmed | hooks doc L1722-1728; may be omitted → treat absent as not-orient |
| 3 | D1 | SessionStart `compact` fires after auto-compaction, stdout added | confirmed | hooks doc L1133, L1146, L583, L810; hooks-guide L313-315 |
| 4 | D1 | `session_id` stable across compaction and `--resume` | confirmed | cli-reference `--fork-session`; sessions doc L159, L192; fork/branch mint a new id |
| 5 | D1 | SessionStart stdout visible in `-p` | confirmed | hooks doc L810, L1015, L1184, L1268; headless L37; not with `--bare` |
| 6 | D1 | ≤ 10 000 chars inline, else path + preview | confirmed | hooks doc L941, L1023; characters, not bytes |
| 7 | D1 | PreToolUse deny holds under bypass; stderr reaches the model | confirmed | hooks-guide L967; hooks doc L826, L882, L1784 |
| 8 | D1 | SubagentStop matches agent name; block re-instructs | confirmed | hooks doc L2362, L2384, L887; honor `stop_hook_active` |
| 9 | D1 | Settings hooks fire inside Agent subagents | confirmed | hooks doc L267; frontmatter hooks need trust and skip in `-p` |
| 10 | D1 | agent-cap slots expire after 45 min via O_EXCL re-claim | confirmed | agent-cap.js L1508, L1590, L1599-1608 |
| 11 | D1 | Agent tool and `.claude/agents/` available in `-p` | confirmed | headless L37-39, L58, L69; sub-agents L875, L1171; not with `--bare` |
| 12 | D1 | Probes and checker behave the same from a worktree cwd, write only under the common dir | confirmed | observed by the skeptic from this worktree; caveat: probes are FILE-anchored — invoke the worktree's own copy |
| 13 | D1 | fs-only node hook costs far less than a git spawn | **refuted** | measured node a: node ~0.8–1.1 s ≈ git spawn; fold into scratch-guard.js, no second spawn |
| 14 | D1 | check 18 pins line numbers | **refuted** | check-unattended.sh L2086-2099 derives first-occurrence order at run time; a `/session-kickoff` mention above L175 reds it |
| 15 | D1 | Custom subagents get CLAUDE.md, not auto memory | confirmed | sub-agents L1036, L1041, L1048; the workflow-spawned skeptic did see MEMORY.md — cite gotchas by path regardless |
| 16 | D2 | SessionStart[compact] stdout under 10 000 chars inserted verbatim | confirmed | hooks doc matcher table, exit-0 rule, L941; a bare JSON-looking blob is not added |
| 17 | D2 | `session_id` stable across compaction and resume, present in both payloads | confirmed | common-fields table; a local transcript with one compact_boundary holds one sessionId; fork/branch mint new |
| 18 | D2 | `agent_type` set inside subagents and absent on the main loop | **refuted** | `agent_type` is present on a `claude --agent` main loop; key on `agent_id` |
| 19 | D2 | Deny reason reaches the model; holds under bypass | confirmed | hooks doc decision-control table; hooks-guide L967; `-p --resume` must re-pass the flag |
| 20 | D2 | A subagent can invoke the Skill and run the engine unchanged | **refuted** | Skill access holds; `AskUserQuestion` is removed from every subagent (sub-agents L405-412) — the engine's asks are unreachable; restate them as `## open` rows |
| 21 | D2 | Agent tool returns the final message intact | confirmed | tools-reference L98; context-window walkthrough; partial on rate-limit/maxTurns |
| 22 | D2 | SubagentStop block continues the subagent; matcher is the frontmatter name | confirmed | hooks doc SubagentStop section; 8-continuation cap |
| 23 | D2 | agent-cap counts orient, TTL reclaims | confirmed | agent-cap.js L1737, L1508, L1598-1610; four slots inside 45 min |
| 24 | D2 | Compaction clears tool outputs and summarizes hook context | confirmed | context-window table; ordering language is the claim's own; up to five recent files re-read |
| 25 | D2 | Probe logs key on worktree, so a subagent's probes satisfy the DoD item | confirmed | query.py:406, reuse_lookup.py:752-767, unattended.sh:3602-3712 |
| 26 | D2 | Step 0 consume clause fits 207 B | unverifiable | 18225/18432 exact; clause undrafted; settle by drafting and running the gate |
| 27 | D2 | Checks 18/20 anchor on two literal pairs the edit preserves | **refuted** | check 20 needs five section-scoped literals plus the heading; check 18 takes the first file-wide `/session-kickoff`; the check exceeded 100 s |
| 28 | D2 | Subagent Bash runs in the session's worktree | confirmed | observed; sub-agents doc; not with `isolation: worktree` |
| 29 | D2 | Common-dir artifact is outside every gate and the tree | confirmed | agent-cap.js L1512-1543, query.py L264, reuse_lookup.py; by construction |
| 30 | D2 | Path-keyed selection keeps the relevant rows | unverifiable | the figures live only in the parent session; mechanism unbuilt; settle on three past units |
| 31 | D3 | SessionStart matcher accepts source values and pipe alternation | confirmed | hooks doc matcher tables; hooks-guide |
| 32 | D3 | SessionStart[compact] stdout under 10 000 chars inline | confirmed | hooks doc L941; hooks-guide re-inject example |
| 33 | D3 | Same `session_id` on startup, compact, resume | confirmed | cli-reference; sessions.md; fork is the exception |
| 34 | D3 | SessionStart fires in `-p` | confirmed | hooks doc L1184, L1268; headless L41, L221; not with `--bare` |
| 35 | D3 | Card costs ≈ 23 s (audit 21 s + git 1.6 s) | **refuted** | loaded host: audit 41–44 s, six git calls 4.9–5.8 s; budget ≈ 45–50 s if the audit runs at start — this design does not run it there |
| 36 | D3 | Scoping check-wiring off compaction loses nothing | confirmed | arms read git config, settings bytes, file bytes; `--check` took 80.9 s here; loses only re-detection of mid-session drift |
| 37 | D3 | Four engine clauses fit ≤ 200 B or a trim exists | unverifiable | 207 B exact; existing hedge at L26-28 makes one clause near-zero; draft and run the gate |
| 38 | D3 | A subagent loads AGENTS.md so it costs more than it isolates | **refuted** (partly) | true for general-purpose/custom; Explore skips CLAUDE.md and git status (sub-agents L1036-1041) — but then the charter does not bind it |
| 39 | D3 | agent-cap exempts no agent type | confirmed | grep 0 hits; L1718, L1737, L1564, L438; "never resets" overstated — TTL and new prompt_id reset |
| 40 | D3 | Existence verifier ~1 s for 30 tokens | **refuted** | per-token loop 27.4 s + 23.9 s for 30 tokens; batched `git grep -F -f` + one `git ls-files` ≈ 1.1 s |
| 41 | D3 | Node tag resolves uniquely from `$USERNAME`/hostname against the registry | **refuted** | row-wide match on `d41ly` hits 4 rows via the Remote column; match the Machine/user cell on `$USERNAME` alone; rows a and d have no hostname |
| 42 | D3 | Only the listed sources are re-injected after compaction | confirmed | context-window table L1598-1609; skill-description listing is not re-injected |
| 43 | D3 | Unattended ordering fully gated by checks 18/20 | **refuted** | keepalive-first is `unattended.sh --preflight` `fail 8`; keepalive-before-orient is unenforced; checks 18/20 are document line-order assertions |
| 44 | D3 | Common-dir card leaves the tree clean, not pushed | confirmed | precedent verified; key per session and carry the toplevel — the common dir is shared across worktrees |

Harness facts used without a numbered verdict (map area 4, all from the raw docs): SessionStart
accepts only `command`/`mcp_tool` and cannot block; `initialPrompt` fires only when the session runs
AS that agent; `context: fork` runs in the background by default and does not see the conversation;
UserPromptSubmit's block reason never reaches the model and a 30 s timeout discards its output;
PreCompact cannot shape the summary; `Workflow` is removed from every subagent; injected text should
be factual, not imperative.
