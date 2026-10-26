**Serves:** research TOOL-dGroundRules-34

# Divergence brief 2 — TOOL-dGroundRules-34, the intake route arms the target's gate runner

## The prompt

> Its builder built TOOL-dGroundRules-34 rev-7 at 7106e5abc (saved as a patch), observed every buildable finding green, and handed it back as a DIVERGENCE on S22 (finding 18): `build_install_target` running the snapshot deployer's `intake` writes the descriptor's `[gate_runner]` table from the run-gates seed, whose kind is `manifest`; with it present `apply` runs the target's own gate runner before and after the install, seven legs are new and red after a fresh install, and `apply` exits 1 ("leg '<name>' did not exist before this install and is red after"), so `adopter-fresh-target` prints a WRONG and AC29 cannot hold; `legacy-homes-withheld-install` and `census-default-adopter` are exposed the same way. HEAD's builder on the same tree printed 154 assertions and 0 wrong. AC19's command passes five cases to one `--fixture`, which takes one case.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md` to the run's ruling (a). Author only: no product code, no commit, no gate.

### Items
1. S22 and §4 "The fresh-target builder after S22 and S23": `intake` stays the one source of the target's descriptor, and the builder removes the `[gate_runner]` table intake writes before the target's one commit, because a fixture target has no gate history for `apply`'s before-and-after comparison; the claim that the seed is kept goes. A criterion observes that the committed descriptor carries no `[gate_runner]` table and that `apply` exits 0. Option (b), the builder writing its own descriptor, is refused as a second descriptor source; option (c), a govkit change, is refused as outside this unit's write set and §3.
2. AC19 runs its five cases one `--fixture` invocation each.
3. The status header's rev rises by one, with a §9 line naming the disagreement and the ruling. The spec sits at 48586 bytes with its records region and must end at or under 48600 measured with `wc -c` before the records region grows again: trim prose outside §2 and §6 to pay for every byte added, and shorten older §9 lines if needed; never touch AC11, AC12, AC15, AC16, AC32 or AC36. Every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48600; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's per-finding statuses at 7106e5abc stand; its patch applies with only `build_install_target` to adjust.

### Reuse
The builder's patch `TOOL-dGroundRules-34-dispatch2.patch` in the session scratchpad.
