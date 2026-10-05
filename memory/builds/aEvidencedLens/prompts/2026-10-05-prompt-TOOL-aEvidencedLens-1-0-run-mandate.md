# Run mandate — aEvidencedLens

**Serves:** journal TOOL-aEvidencedLens-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-05. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Bring all 5 improvement points into the build and execute it per the protocol. Test your
> improvement points on this very build, opt-in into spec reviews for this build.
> Decisions:
>
> 1. Spec audits are not worth running on the small units at all and should be aimed at multi-unit
> builds and vague briefs. However, per the rules, spec reviews are now OWNER OPT-IN ONLY and they
> are off by default. The should be RECOMMENDED to the owner for the multi-unit builds but it will
> remain up to the owner whether to opt-in. The scope of this build is to ensure that IF the owner
> opts-in they get a good quality review.
> 2. Spec lenses SHOULD run read-only commands.
> 3. Prior-art is important to this product's philosophy - functionality must be reused and extended
> , not rebuilt or duplicated. How to implement and improve prior-art with this in mind is up to you
> in this build.
> 4. By default, each unreviewed spec gets only ONE audit review but this is operator adjustable
> (human owner, agents should never decide this for themselves and only follow the default rule). A
> recent build has changed how review items are treated - they are all promoted to build units
> (MEDIUM and LOW get batched into 1 or 2 specs/units).

## The five improvement points the prompt names

The points were stated in the same session, immediately before the prompt, from a read-only study of
243 spec-audit records, a 91-escape analysis over 13 audited builds, and the `aBlindedTrial` report:

1. Fix the harness's own defects. The only automated caller passes no context, siblings, checklist or
   prior findings. A round-2 brief contradicts itself. The spec skeptic's test cannot confirm a LOW
   and has no duplicate or by-design refutation. A moved subject is hard-coded BLOCKER. The prior-art
   brief drifted from the method's catalogue.
2. Let lenses gather evidence: lift "nothing outside the spec set" and require read-only probes. Run
   each acceptance criterion's command at BASE, grep consumers, time stated goals, and probe every §4
   claim about existing code.
3. Reshape the lens set inside the five slots the fan-out hook admits. Name the classes no brief
   named: fallout on the repo's own machinery, degenerate inputs and failure modes, a criterion that
   cannot pass, ordering across units, and an instance named where the class was meant.
4. Make a fold round see what changed, by handing the lens the diff from the previous blob.
5. Make the lens shape measurable: the lens on every finding, refuted ones included, and each lens
   scored on unique defects rather than raw counts.

## The one question asked, and its answer

Asked once, before the build folder was written: should batched promotion, which `aBatchedMinors`
built for the closing diff review only, extend to spec-audit exits, superseding the fold half of the
`TOOL-aProbedUnit-9` ruling? **Answer: promote, batched.** A spec-audit MEDIUM or LOW becomes one of
one or two batched units, as at a closing review, and is no longer folded into the spec.

## How the run reads it

- Decision 1 is already the driver's behaviour: the audit is opt-in, and the not-owed line
  recommends it for two or more units or a forked spec. This build does not move that default. It
  improves the review an owner gets after opting in.
- Decision 2 is improvement point 2. "Read-only" means no write to the repository tree. Scratch files
  under the session scratchpad are allowed, and every command is bounded. No suite and no bar run
  inside a lens, which the gate guard refuses anyway.
- Decision 3 keeps prior art as a lens of its own, renamed `reuse`. Its brief targets duplicated or
  rebuilt functionality, as well as decisions a record already made. It probes with the reuse lookup,
  the recall CLI and grep, and a finding must name the seam or record it rests on.
- Decision 4: `REVIEW_ROUNDS` stays at its kit default of 1. Because the owner said agents never decide
  it, unit 9 makes the merge bar refuse a run commit that changes it.
- "Test your improvement points on this very build": this build's own specs are audited by the
  harness as it stands at BASE. The harness units build first. The specs that audit promotes are then
  audited by the improved harness. That second audit, together with a replay of the improved harness
  over the round-1 subjects that `TOOL-aEvidencedLens-10` scores, is the test.
