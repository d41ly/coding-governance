**Serves:** journal TOOL-dBoundRoles-13

# TOOL-dBoundRoles-13 — the main loop's decision over the second builder's divergence

Run `wf_e5e7a4cb-5ca`, started at `35b19ccc5` on rev-6 under the first decision record, wrote nothing and committed
nothing. Its two items are decided by M3 as delegated resolutions and built under the same deviation record.

1. S6, §4 Migration and AC5 make `facts` required by the unit harness with no exception, while `facts` comes only
   from the roles kit's `handoff.py facts`, which neither the review-harness kit nor the unattended kit requires.
   Route (a) is taken: `facts` is required only where `roles.builder` travels, and AC5's stub arguments name that case;
   a call with no `roles` passes as before. Route (b), a new `requires` edge on the roles kit, adds a dependency and is
   a new public surface (veto 2). widens: none · relaxes: none.
2. `memory/guides/UNATTENDED-VERBS.md`, the install copy that the adopter and memory hygiene check 10 byte-compare with
   `tools/unattended/VERBS.template.md`, joins the write set, so S7's edit lands in both files in one commit.
