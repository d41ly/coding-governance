# dCountedConsumers — unit 1's builder return, the self-review and the leg reads

**Serves:** journal TOOL-dCountedConsumers-1

Run wf_3ef53294-c95, summarized from its result.

- Built as `871f3c975`, with `Pass: TOOL-dCountedConsumers-1` and the spec flipped to CLOSED in the same commit. The consumer paragraph names all eight consumed key families, with one link each, and keeps the closing claim and the invalid-file exception.
- Probe A ran verbatim from §4. AC1 holds: `read 14 unlisted none`, and eight `named links 1` lines. AC2 holds: `two-families 0 closing 1`. AC3 holds: the seven anchors are unchanged, with `commands 8` and `links 9`.
- AC4 does not hold as written. It expects the commit to name `help/policy.md` alone, but the commit also carries the required CLOSED flip and the two files the hook re-renders: `memory/LIVE.md` and the build README. The product hunk sits within lines 8-15 as AC4 asks. The criterion was mis-scoped, and it is recorded here because the spec is frozen.
- Self-review by the main loop: the diff matches the spec. One low nit stays: the forwarder line's "hold read" reads awkwardly.
- `docs` exits 0: 45 anchors on 13 pages, 0 stale.
- `policy fixtures` exits 1 with two guard-trace lines, naming `.governance/install.json` and `tools/govkit/upgrade_steps.py`. The same two lines print at BASE `8bec4cefd` in a clean clone, so they are INHERITED and not this build's.
- Follow-up from §3: `tools/policy/README.md:686-688` repeats the stale "No consumer reads the file yet" claim.
