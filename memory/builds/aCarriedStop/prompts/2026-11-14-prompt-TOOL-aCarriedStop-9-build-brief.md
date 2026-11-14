# Brief — aCarriedStop: build unit 9, the routed-commits leg's ceiling

**Serves:** research TOOL-aCarriedStop-9

## The brief

### Goal
Build `TOOL-aCarriedStop-9` as its spec states it. The design is `memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names.

### Acceptance
1. Each criterion of the spec's §6 that the spec assigns to the builder is observed in the pass and named in the return.
2. Each criterion the spec assigns to the main loop is named in the return as owed.

### Gates
None in the pass. The merge bar runs once, at the close.

### Non-goals
Everything the spec's §3 lists, and any file the spec does not name. Any kit version, which the lander's mint moves. Any path under `memory/builds/dDeclaredLoop/`.

### Limitations
- No gate, suite, self-test or bar runs in the pass, and every command is bounded under two minutes.
- The spec is not edited beyond its status header at the build commit; a divergence is returned, not built.
- The pass commits once, after the spec commit, with a subject naming `TOOL-aCarriedStop-9` and a final trailer block holding `Pass: TOOL-aCarriedStop-9` beside the charter's `Co-Authored-By:` line.
- The pass commit carries `memory/builds/aCarriedStop/RUN.md` as staged, and the acceptance ledger `memory/builds/aCarriedStop/build/2026-11-14-build-TOOL-aCarriedStop-9-1-acceptance-ledger.md` in the grammar `memory/HYGIENE.md` states under "Acceptance ledger".
- The CLOSED flip of the spec header is in the same pass commit.

### Reuse
The seam the spec's §10 names.
