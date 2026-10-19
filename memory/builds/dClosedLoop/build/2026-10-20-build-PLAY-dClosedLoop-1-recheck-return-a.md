# Second look: run A

**Serves:** research PLAY-dClosedLoop-1

Dispatch 190's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-31-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- A1-F7: confirmed high
  The finding holds. In flow-steps [design], line 192 gives `design.ready`'s Needs as only "`design.recommend`, and the spec audit where it ran". Line 302 gives `test.exit` the same shape, waiting on `test.recommend` and not `test.reason`. [rules] lines 26-31 build the frontier from the Needs column alone, and layer-runtime [decide] line 329 has `next` hand out every frontier item to run. So once `design.recommend` is witnessed, `design.ready` (a command) and `design.reason` (an architect agent) are both runnable. Line 208 says the audit sits "after `design.recommend` and `design.reason`, before `design.ready`", but no Needs column enforces that order. v2 :1527 sets `review.recommendation: binding` in a preset, so a review the reason calls for can be skipped (c3).

- A1-F9: confirmed medium
  I rebuilt the [chain] clauses from v2 into the scratch file `clauses.txt`. No clause ties a lens to practice reach. The P14 row (v2 :1698) names `cl-dClosedLoop-0031`, which is only the catalogue. It also names `cl-dClosedLoop-0051`, which hands step-scoped reach to role work orders. The lens clauses (0070, 0080, 0458, 0470) fill the harness's lens slots from catalogue data and never mention reach. The Review-stage reach that foundations :71-76 describe has no step to be scoped under.

- A2-F8: refuted
  The copy already gives a unit holder on another node its own branch. `cl-dClosedLoop-0319` has that holder "driving only that unit's passes on its own branch, pushed the same way … the driver alone running transitions". night-pass-two :329 says the same, and :671 states "a build branch has one writer, a unit branch one each". layer-runtime [isolate] :732-735 merges unit branches into the build branch before release. So node x never pushes X's build branch, and the race the finding describes does not arise. Its proposed fix is already in the design.

- A3-F14: refuted
  The scenario cannot happen. The rule "a retry that finds its own key counts as claimed" only applies when the same slug is retried. That claim instance's witness is the claim ref, so after the build moves on it is never re-run (layer-runtime [decide] :336-343). A replayed intake is a content-keyed write and is a no-op (layer-memory :336-337). A fresh placement mints a new slug, collision-checked by the record command (layer-memory [names]), and since the claim ref is never pruned, "a slug is minted once" (:333). S5's "queued claim replayed" is a lease claim, and `cl-dClosedLoop-0134` refuses it at the terminal tombstone.

- A4-F7: confirmed medium
  `cl-dClosedLoop-0028` makes the floor raise "the step kind's first step". `cl-dClosedLoop-0020` adds the per-step `steps` progress field to receipt schema 4, and that change is itself shipped as an upgrade step. No clause orders the two, or says where progress lands for a step completed on a schema-3 receipt. This collides with `cl-dClosedLoop-0019` ("the receipt advancing per completed step") and with `cl-dClosedLoop-0022` ("the k-th step made to exit 1 and the receipt naming step k-1"). One part of the stated consequence is overstated: a re-run of the floor step after a kill is skipped because its witness holds (0019).

- A5-F5: refuted
  The lease does not stay lost, and Design cannot be entered without one. Under v2 :1103 and `cl-dClosedLoop-0326`, parking releases the lease as a hand-over. `cl-dClosedLoop-0134` and layer-runtime :406 say any node takes a hand-over by design. `run <build>` takes the build lease again (layer-runtime :346). `cl-dClosedLoop-0133` fences every effect push on the holder's lease tip, so a node holding no lease cannot push `plan.exit`'s transition. The build therefore cannot enter Design without a lease.

- **Read outside the list above:** none. My greps ran over the copy's whole build folder, but I filtered the `*-compared.md`, `*-instruments.md` and session-log records out of the output. The only files I wrote are `chain.txt` and `clauses.txt` in `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-a/`.
