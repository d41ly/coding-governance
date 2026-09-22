# Build brief — TOOL-cMendedVintage-9

**Serves:** journal TOOL-cMendedVintage-9

The pass this brief is handed to builds unit 1 of `cMendedVintage`: the card verbs resolve a session
id without blocking on an open stdin. Read the spec whole before touching code; this brief carries
only what the spec cannot — how the defect was observed, and what the acceptance arm must not become.

## What was observed, live, on this run

`skills/session-kickoff/manifest-check.sh:128`:

```
[ "$CARD_VERB" = append ] || [ -t 0 ] || sid=$(sed -n 's/.*"session_id"...' | head -1)
```

`read_session_id` resolves the id by reading stdin for the SessionStart hook's JSON. The only guard
is `[ -t 0 ]`, "is stdin a terminal". That admits the two cases its author had in mind — the hook,
which writes JSON then closes, and a human at a terminal — and not the third: stdin as an open pipe
that never sends EOF, which is what every tool-invoked shell hands a child. `sed` then waits forever.

Measured on this session: `--card --write --session <sid>` ran **71 minutes** and consumed **4.4 s of
CPU**, with a single bash subshell and no children. The same command with `< /dev/null` returned in
under a second. That pair is the evidence; neither half alone distinguishes a hang from slow work.

Passing `--session` does NOT avoid it. The stdin read runs first and `CARD_SID` is only consulted
afterwards, so the caller answering the question the read exists to ask does not stop it being asked.

## Why this is worth a unit

The kickoff skill's own Step 5 prescribes `--card --write --session <sid>` as the repair verb for a
malformed card. So the documented remedy for a broken card is itself a hang, and it strands exactly
the operator who is already stuck. It also blocked this run: with the sentinel `READY — none yet`
still on the card, `scratch-guard` refused the session's next commit.

## The trap the acceptance arm must avoid

An arm that runs the verb with stdin already closed proves nothing — that is the passing case today.
The arm has to hold stdin OPEN and assert the verb still returns, which means it needs a bound of its
own, or it becomes the hang it is testing for. State the bound and the timeout mechanism explicitly;
a `fixture-passes-by-finding-nothing` arm here is worse than no arm, because it certifies the fix.

`staged-break-substitutes-a-synthetic-value` is the sibling trap: grade the real script, not a copy
with a simplified read.

## Bounds

The spec's §3 is binding. In particular this unit does not touch `--card --append`, which already
skips the stdin read by verb and whose stdin is the body it stores. Do not widen the fix into a
general "never read stdin" change: the SessionStart hook's channel is the reason the read exists and
it must keep working.
