**Serves:** journal TOOL-dBoundRoles-17

# Brief — dBoundRoles: TOOL-dBoundRoles-17 revised over its second builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 17's second builder (run `wf_25370bd3-656`) stopped before its
code on rev-6. Its return and the main loop's decisions are in
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` to its next rev so the next builder can
build it as written.

### Items

1. §5 names the user docs this unit owes: `help/roles.md`, for `--item`, the `**Answers:**` obligation and the R16
   refusal, and `tools/govkit/usage.toml`, the render verb's flag list gaining `--item`, with the page's usage anchor
   moving with it. Add both to §4 Files touched and the docs leg that grades the anchor to §7.
2. S6 states that the pass re-stamps the kickoff manifest `memory/guides/SESSION-KICKOFF.md` in its own commit, since
   `tools/memory-tree/check-memory-hygiene.sh` is on its `watch:` list; add the manifest to Files touched.
3. S6 states that the main loop renders `memory/HYGIENE.md` from the edited template in a follow-up commit naming
   this unit, since the render route is a `.test.sh` file a builder may not run; the pass itself edits only the
   template. Say which criterion observes the render at that follow-up commit.
4. §4's return predicate takes one reading, the one that reproduces the population pin the spec carries; probe both
   against HEAD and state whether the `**Answers:**` line's own path counts as the naming. Record it as a §8 fork
   resolved by M3 as a delegated agent resolution, `widens: none` and `relaxes: none`.
5. S2 names which readers return `item` and in what shape; a reader whose output is lines or edges says what it does
   with `item` instead.
6. Fold the builder's advice if it holds: `--legacy-rows` reads the head itself for the home's header sha.
7. Change nothing else. Keep every criterion's number and keep each passable on a correct build and red on the break
   it names. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Keep the status `INPROGRESS`. One
   revision-log line names this brief and the return by their file stems.
8. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with every item folded and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the items.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` alone.

### Reuse

TOOL-dBoundRoles-21's spec, whose S8 renders a mirror in a follow-up commit naming the unit, the shape item 3 copies.
