# Brief — aCarriedStop: build unit 1, the owner-stop row

**Serves:** research TOOL-aCarriedStop-1

## The brief

### Goal
Build `TOOL-aCarriedStop-1` as its spec states it. The design is `memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names under "Files touched".

### Acceptance
1. Each criterion of the spec's §6 that a probe or a fixture of the changed code can observe is observed in the pass and named in the return.
2. Each criterion only a gate, a suite or a new arm's RED-first run can observe is named in the return as owed to the main loop at the close.

### Gates
None in the pass. The legs of the spec's §7 run once, at the close, with the full bar.

### Non-goals
Everything the spec's §3 lists, and any file the spec's §4 does not name. Any kit version, which the lander's mint moves. Any path under `memory/builds/dDeclaredLoop/`.

### Limitations
- No gate, suite, self-test or bar runs in the pass. Every command is bounded under two minutes.
- The spec is not edited beyond its status header at the build commit; a divergence is returned, not built.
- The spec commit is already made, so the pass commits code after it, in one commit whose subject names `TOOL-aCarriedStop-1` and whose final trailer block holds `Pass: TOOL-aCarriedStop-1` beside the charter's `Co-Authored-By:` line.
- The pass commit carries `memory/builds/aCarriedStop/RUN.md` as staged, and the acceptance ledger `memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-1-1-acceptance-ledger.md`, a `journal` record in the grammar `memory/HYGIENE.md` states under "Acceptance ledger", each token one the criterion itself spells in backticks.
- Every edit lands before the header goes CLOSED, and the CLOSED flip is in the same pass commit.
- A new shell function owes `python tools/codebase-map/gen_map.py --write` in the pass commit.
- `tools/unattended/unattended.sh` holds CRLF-sensitive and backslash-heavy text: edit it with the Edit tool, never through a heredoc or a Python text-mode rewrite.
- If the pre-commit hook asks for a `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md`, make it as the hook's message states and name it in the return.

### Reuse
The seams the spec's §10 names, extended in place.
