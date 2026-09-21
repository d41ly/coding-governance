# Run mandate — aWokenSentinel

**Serves:** journal TOOL-aWokenSentinel-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-09-16. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts. The value carried whitespace and named no
readable file, so it is the prompt itself.

## The prompt

> build this through to completion per the protocol

## What "this" is

The prompt answers the assistant's message immediately before it in the same session, which ended
with the question "Want me to spec them as a build, or write this up as a research record under a
build folder first?". The message was the result of a four-agent research workflow (three lenses,
one skeptic) over the owner's question, quoted here because it is the scope the prompt points at:

> In the unattended kit and its sessions, CronCreate keepalive pushes its stalled session ONLY if
> its the only background task running in its session, otherwise its completely useless. What other
> keepalive solutions we can use so stalled sessions can reliably resume? Currently, it's a
> significant problem for unattended build to stall due to API unavailability/session limits and
> never resume.

The assistant's answer ranked the mechanisms by failure-domain separation and proposed a layering,
smallest first. The full derivation, with every measured fact and every rejected candidate, is the
research record `build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md`. The
layering, as stated in the message the owner replied to:

0. No mechanism — record `session:` and `pid:` in the run-state file at `--preflight` and
   `--resume`; define terminal as a predicate rather than `phase:` alone; make the CONTINUE payload
   forbid re-parking and state the absent-owner default.
1. A `Stop` hook, session-bound, with a bounded block count — no scheduler, disk-persisted, and its
   trigger is the decision to stop, the most frequent recorded stall class. Paired with a
   `StopFailure` hook that writes an on-disk stall marker at zero API cost.
2. One idempotent `schtasks` tick: if the recorded pid is dead, or alive with the run's liveness
   signal untouched past the bound, and the run is non-terminal — kill the tree, then
   `claude -p --resume <sid> --max-turns N "CONTINUE"`, exit. Blocked on the owner minting a CLI
   token.
3. Keep `CronCreate` as the free idle-wake; stop calling it a keepalive.

Rejected, with the reason recorded: `ScheduleWakeup`; a watchdog session in the same app; the
desktop-app scheduled task; cross-session `SendMessage` alone; cloud routines. Fallbacks, not
mechanisms: an OS notification after N failed resumes; cross-node takeover for a weekly lockout.

## Owner facts handed mid-run

- 2026-09-16, mid-turn: "also, CLI is now logged in if you need to use it". The research had
  measured node `a`'s standalone CLI as NOT logged in, which left layer 2 untestable; this lifts
  that. It is a fact, not an instruction, and it changes what unit 5 can observe.
