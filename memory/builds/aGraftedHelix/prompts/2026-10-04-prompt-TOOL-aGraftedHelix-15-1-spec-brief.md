**Serves:** journal TOOL-aGraftedHelix-15

# Spec brief — TOOL-aGraftedHelix-15, adopted mid-run

Read the shared brief beside this file first
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`): its twelve shared invariants bind this
unit too. Tier-1, streams tooling, `order 10` — it touches no file another unit of this build writes.

## What was observed

This run drove `tools/workflows/unattended-build.js` on a build whose nine specs were all MISSING,
with `specAudit` declared. Run `wf_7b67cf1d-995`:

1. **First call.** The SPEC stage authored nine specs and, as its prompt orders, committed nothing.
   The AUDIT stage's resolver ran `git rev-parse HEAD:<specPath>` for each, every one failed because
   no spec was committed, so it returned no subjects, and the stage threw
   `no spec subjects could be pinned at round 1`. This is not an edge: it is the outcome of EVERY
   first call on a build with a MISSING spec and a declared audit.
2. **The remedy the dirty-tree refusal names** is "commit the fold, then re-invoke with the same
   arguments". After committing, the run re-invoked with `resumeFromRunId`, the natural way to keep
   the nine spec writers' work. The resolver's prompt was unchanged, so its EMPTY answer replayed from
   cache and the stage threw the same refusal again in 20 ms.
3. **What completed the route**: re-invoking with caller-pinned `subjects` (`{path, blob}` from
   `git ls-tree HEAD`), which skips the resolver. Nothing in the harness or its refusal names that.

The empty-subject refusal itself (the `if (specAudit && !subjects.length)` throw in
`tools/workflows/unattended-build.template.js`) names neither cause nor remedy.

## What to decide (M12: candidates, plural, and the test that loses each)

At least these, and any better one you find:

- **(a)** A single agent, after every spec writer has returned and before the resolver, regenerates
  the build index and commits the authored specs with a spec-subject commit. Nothing else is writing
  then, so the contention the writers avoid does not arise. One call completes SPEC and AUDIT.
- **(b)** The resolver also reports specs that exist on disk but not at HEAD, and the harness refuses
  naming them, the cause, and the two remedies that work: pass `subjects` pinned, or re-invoke
  WITHOUT `resumeFromRunId`.
- **(c)** The SPEC stage returns early whenever it authored a spec and an audit is declared, with
  the authored list and the commit instruction — and say what stops a resumed call from returning
  early forever, since the spec writers' cached results still say they authored.

Test what discriminates: which candidate survives a resume, which survives a fresh call, and which
keeps `pass-order history` satisfied (the spec commit must precede any build commit). Record the
loser's test.

## Bounds

- Edit the template and re-render the `.js`; `tools/workflows/unattended-build.test.sh` is the kit's
  suite and is NOT run inside the pass (shared invariant 11). Its arms that this changes are named
  under §7 `New arm:`.
- The harness's header comment states what the change does NOT buy, in the same register as the
  rest of that header.
- Bump the workflows kit version once (shared invariant 4).
