**Serves:** journal TOOL-dBoundRoles-43 TOOL-dBoundRoles-50 TOOL-dBoundRoles-56 TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69

# Brief — dBoundRoles: the renamed spawn-guard leg, carried into the open roster specs

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. TOOL-dBoundRoles-25, built at `00a96bb43`, moved the agent-cap hook and
its suite into the roles kit and renamed the bar leg `agent-cap self-test` to `spawn-guard self-test` in
`tools/gate-legs.json`. Every open roster spec that names the leg now reds the spec-token checker on two hits: the leg
name, which no longer resolves, and a guards finding, because the spec's Files touched trip the renamed leg and its
leg line no longer names it. `--dispatch` refuses a unit while its spec reds the checker, so the build stops at the
next unit, TOOL-dBoundRoles-43.

## The brief

### Goal

Revise the one spec your handoff names in place, as a rev bump with one revision-log line, so that it names the leg
by its current name and `python tools/check-spec-tokens.py --spec <that spec>` prints no hit for it.

### Items

1. Replace every occurrence of the leg name `agent-cap self-test` with `spawn-guard self-test`, on the section 7 leg
   line, on every `New arm:` line and in prose that names the leg. Nothing else moves.
2. Leave every path citing `tools/hooks/agent-cap.js` or `tools/hooks/agent-cap.test.sh` as written. Those citations
   are the unit's history and its reasons; the spec-token waiver register waives them, and TOOL-dBoundRoles-43 S28
   owns that register.
3. Bump the status line's `rev-<n>` by one, keep its status, and add one revision-log line in section 9 naming this
   brief, the rename and TOOL-dBoundRoles-25's commit.
4. Run `python tools/check-spec-tokens.py --spec <that spec>` before and after your edit. Your return quotes the hit
   lines from before and states that the run after prints none for the leg; any other hit it prints is reported, not
   fixed.

### Acceptance

The spec names `spawn-guard self-test` wherever it named the retired leg, its rev is one higher with one new revision-log line, and its spec-token run prints no leg or guards hit for the spawn-guard leg.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to the spec, its criteria or its forks, no other spec, no product code, and no gate, suite or bar.

### Limitations

The write grant is the one spec your handoff names.

### Reuse

`tools/gate-legs.json`, whose `spawn-guard self-test` row is the renamed leg, and `tools/check-spec-tokens.py --spec`, the probe.
