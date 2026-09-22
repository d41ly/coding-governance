# Design research — how an unattended run's action and decision sequence gets recorded

**Serves:** research TOOL-dLoggedFlight-1..13

Node `d`, 2026-09-12 to 2026-09-13, at base `09a22d2b`. Five read-only readers mapped the kit, the
Claude Code transcripts, the run corpus, the repo's existing telemetry and the platform's hooks. Five
cold reviewers then tried to refute the first draft. This record keeps what survived, in the shape the
build method's M12 asks for: the candidates, the test that decided each, and the loss as well as the
win. Figures are node `d` measurements unless a line says otherwise. No transcript text is reproduced.

## What a run leaves behind today

- **The run-state file is a snapshot plus a row log of verbs that SUCCEEDED.** Facts are rewritten in
  place with no timestamp, so repeated phase moves collapse and none carries a time. One sampled run
  made 29 `--phase` calls, 28 of them re-setting the same phase.
- **Refusals leave nothing tracked.** In that run, 15 of 88 state-changing driver calls were refused.
- **Gate verdicts leave nothing structured.** Its session ran the bar 17 times, 3 of them inside the
  run's window, and no structured per-run verdict exists. The gate ledger keeps one row per leg and the
  run records keep the last five.
- **Also untracked:** the close checklist's per-item results, landing attempts, compactions, resumes,
  keepalive fires and owner messages.
- **No run record names the session that ran it.** That is 0 of 56.
- **Six of 56 records sit at LANDING or BUILDING although their builds merged.** Three of the four
  LANDING ones are wedged on the landing verb's lander-marker check.
- **Decisions taken without a park mostly vanish.** Of 21 substantive mid-run choices sampled from one
  run's narration, 1 sits in a run-state row, 12 sit in commit bodies, acceptance ledgers, briefs or
  backlog rows, and 8 are recorded nowhere. The 21 are a curated lower bound.
- **Cost is unmeasured.** In one sampled session the main loop carried 84% of all tokens and 97% of
  output tokens, and no tool extracts either figure.

## Candidates, and what decided each

**A. Mine the Claude Code transcripts after the fact, as the whole record.** Rejected as the backbone,
kept as enrichment.
- Locality: 30 of the 50 run slugs have no transcript on the node holding this corpus, because they
  ran elsewhere.
- Reasoning: thinking blocks carry a signature and no text from engine 2.1.237 onward, with a few
  exceptions at 2.1.266.
- Exit status: about 96% of driver refusals reached the agent's harness as exit code 0, because the
  call was piped or the status was folded into later output.
- Background jobs: their output files are gone, and a background bar's notification reports the exit
  code of the compound command, which read 0 on bars later found RED.
- It works as enrichment for runs whose transcript is local. A prototype recovered 449 events from one
  multi-run session, including every workflow and agent spawn with its token totals.

**B. A recorder hook on every tool call.** Rejected, and kept as a fallback.
- Redundancy: the sampled transcript already carries every tool call, 2,633 of 2,633, and the sidechain
  files carry every workflow agent's calls.
- Cost: node startup alone is about 0.1 s per hook call here.
- It adds only allow decisions and hook latency.
- It stays available: a PROJECT-level PreToolUse hook was observed firing inside a Workflow sidechain,
  where its denial was recorded with `isSidechain:true`.

**C. OpenTelemetry.** Rejected.
- It is not configured on this node and covers only runs started after it is.
- A desktop session's console exporter is the SDK pipe, so it needs a local collector.

**D. Journals written by each PRODUCER at the moment of the act, joined by one renderer.** Chosen.
- The exit code comes from the producer itself, so no caller's pipe can mask it.
- The line is keyed to the run when it is written, so nothing attributes it by heuristic later.
- The run-to-session join is free: `CLAUDE_CODE_SESSION_ID` is present in the Bash environment of both
  the main loop and a sidechain agent, carrying the parent session's id in both.
- The agent authors nothing new.

**E. An agent-authored decision verb.** Rejected in favour of harvesting what agents already write,
plus a `Decided:` commit trailer for a choice with no commit of its own.
- The harvest test: in the sample above, reading commit bodies, ledgers, briefs and backlog rows moves
  coverage from 1 of 21 to 13 of 21 with no new authoring.
- A new row kind would grow run-state files. 12 of 56 already exceed the protocol's 8 KB budget, and
  that spill rule has no writer.

**F. A hash chain across log lines, for tamper evidence.** Rejected.
- With two concurrent writers and no `flock` on this platform, 39 of 59 links broke with nothing
  tampered. Twelve writers broke 714 of 719.
- Real runs do overlap: seven same-slug driver calls overlapped in the local sessions.
- What replaces it: the committed record carries the journal's hash, line count and first and last
  timestamps. That commitment reaches the remote.

**G. The record as a Definition-of-Done item.** Rejected.
- Circular: the item would be evaluated inside `--close`, before the record could hold the close.
- Overridable, because only two items refuse an override.
- It raises the core-set floor on every adopter.
- What replaces it: a schema leg over committed records, and a drift signal.

## Mechanics the cold review corrected

- **One line on exit is not enough.** A killed verb leaves no line, and a TERM trap sees `$?` 0 while
  the process exits 143. So each call writes a START line and an END line with a shared nonce, and a
  start with no end is itself the finding.
- **The trap has to sit before the argument loop,** because `--phase` and `--plan` exit inside it. It
  also has to be protected from the sourced project conf.
- **The bar calls the driver's multi-slug `--plan` on every run.** That call is read-only and must not
  be journaled as run activity.
- **Durations of background and async calls end at the first record carrying their tool-use id,** not
  at the launch acknowledgement, which returns in about 0.1 s.
- **An owner turn has three sources:** human- or null-origin typed records, messages absorbed
  mid-turn, and interrupts.
- **A session id read from the environment becomes a path component,** so it is validated as a UUID
  and every constructed path is contained. In a replica, a traversal value overwrote a sibling log.
- **A committed record needs a `Serves:` line naming unit ids,** or the record-binding check reds at
  the push boundary. Its render re-renders every spec it serves, so the render step runs the index
  generator.
- **The record is rendered at `--abort` and after `--landed`,** riding the record commit the Skill
  already requires. A commit between the push and `--landed` wedges the landing check.
- **The first draft's evidence overstated six figures** by counting one multi-run session's totals as
  one run's. The figures above are per run. One refutation matters for the owner: three runs did reach
  LANDED with no owner message after launch, so "no run was unattended end to end" was false.
