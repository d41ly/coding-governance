**Serves:** research TOOL-dDeclaredLoop-57

# Brief: revise spec TOOL-dDeclaredLoop-57 after its builder's divergence

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The dispatch of TOOL-dDeclaredLoop-57 returned a divergence before any write: the claim its section 5 marks
unverified is false. The return is `memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-57.md` in place, as a rev bump with one revision-log
line naming that return, so a builder can build it with every existing govkit selftest arm still green.

### Items

1. The `rq11b` fixture B block of the dRB-11 arms in `tools/govkit/selftest.py` claims `agent-cap` without its dependency
   `kickoff-manifest`, which no update of that fixture gains, so the refusal this unit adds would red the arm that expects one
   settings-merge problem line. Read that block and its arms yourself, then settle it in section 4, Files touched, section 6 and
   section 7. Weigh claiming `kickoff-manifest` in that fixture, as the `rq9p` fixture beside it does, against recording that
   the arm now observes the new refusal; write it as a section 8 fork with your recommendation and the body on it.
2. Read every other hand-written receipt and update call in `tools/govkit/selftest.py` and `tools/govkit/matrix.py` again
   against the new refusal, and replace section 5's unverified claim with what you found.
3. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the revised spec and fix every hit. Do not run
   the whole-tree memory hygiene gate, and do not ask any checker for its help text.

### Acceptance

- The revised spec names every fixture the new refusal reaches, each with what keeps its arm green.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
