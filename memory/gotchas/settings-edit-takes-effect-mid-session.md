---
name: settings-edit-takes-effect-mid-session
description: an edit to the hooks settings file is live on the next tool call, not at the next session, so a throwaway hook fires on the call that checks for it
kind: class
---

# Editing the hooks settings takes effect mid-session

## Symptom

A hook entry is added to `.claude/settings.json` to test something, or a matcher is loosened while
diagnosing a deny. The expectation is that nothing changes until the next session. The next tool
call fires it. Hooks are re-read, not snapshotted at start.

## Where it bit

Measured 2026-08-10 with a throwaway `PreToolUse` hook that fired on the very call which checked
whether it was present. The probe had two halves — does the edit take effect, and can the probe see
it not taking effect — and the second is the one a reader skips: a hook that never fires and a hook
that fires silently are the same observation until the probe proves it can produce a negative.

## The fix

Treat a settings edit as a live change. A hook added to reproduce a problem is armed before the
reproduction starts, so remove it in the same turn or it grades every later call. Any probe of hook
behaviour carries its liveness half: an observation that a hook did NOT fire is evidence only when
the same probe has shown it firing.

No machine gate — this is a property of the harness, measured once and recorded here. The
documented check is the two-halves probe above whenever a claim about hook timing is made.
