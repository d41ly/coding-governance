---
slug: aPrimedKeepalive
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
ids: TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9
authorized-by: prompt
---

# aPrimedKeepalive — an unattended run keeps itself alive from its first act, and adopts a beneficial discovery instead of waiting for the owner who left

## The problem this build exists to solve

A run that cannot be woken and a run that will not decide are one outage: the terminal goes quiet.
The kit knew both — the keepalive exists, `--park` demands a reason — yet the keepalive was step 3 of
the SLUG path and nowhere else, so the two prompt-bearing paths spent their longest unattended
stretch with nothing able to wake them; and nothing told a run what to do with something good it was
not looking for, so it parked and waited for a reader who had left. `aGroundedOrientation` is both:
it stalled in orientation with no keepalive, and it parked a measured sixteen-fold speedup twice.

## Expected improvements

- A run wakes from a stall on ANY start path, including the pre-preflight stretch the prompt and
  playbook paths spend orienting.
- A discovery worth having is built by the run that found it, not filed for a reader who has left.
- A record whose work is provably on the remote stops holding the whole fleet's bar hostage.

## Detriments if this is not built

- The keepalive gap costs a run per stall, silently, on the paths the owner uses most.
- The adoption gap costs every finding a run makes outside its own scope — which are the findings
  nobody else is placed to make.

## Build-level rules

Classification (M2): every unit was MISSING at open, authored, then re-classified.

M3 veto 2 is not tripped by this build's subject. Units 1-3 change governance carriers, and the
carrier edit IS the mandate: the prompt asks for a binding rule, which lives in
`UNATTENDED-PROTOCOL.md` and `BUILD-METHOD.md`. Recorded so no reader mistakes it for a bypass.

`BUILD-METHOD.md` is capped by its own M1 and the TEMPLATE half is 11 B tighter than the render;
price against the template and re-measure with `wc -c`, never from a number in prose. That budget is
a carrier's stated constraint, which M3's delegation does not reach, so this run may not raise it.

THE WORK PRECEDED THE PREFLIGHT. The pre-commit hook cost ten minutes per commit until unit 6 landed,
so the build folder could not be committed first; the pinned BASE is later than the work and the
closing review runs `b4e1d5be..HEAD`. Units 7, 8 and 9 were added mid-build — 7 adopted under the
rule this build writes, 8 and 9 promoted by M4's NON-CONVERGENT exit after rounds of 4, 1 and 2
blockers. Detail lives in the specs, the acceptance ledger and four review records, not here.

## Parked decisions

Three, each with its question, the options seen and the refusal, in `RUN.md`:

- the merge bar is RED for five legs this build did not cause, and fixing them means editing a
  governance carrier the mandate excludes plus two other builds in flight;
- the kickoff-manifest ratchet breached its own 60 s ceiling and nobody separated contention from a
  real regression;
- the kit self-test suite never returned a verdict — started twice, killed twice.

`gates-green` carries a recorded DoD override naming those five legs. It is not a claim the bar
passed.

<!-- roster:units -->
| Unit | Tier | Mechanism |
|---|---|---|
| `TOOL-aPrimedKeepalive-1` | 2 | the keepalive is scheduled as the run's first act, on every start path |
| `TOOL-aPrimedKeepalive-2` | 2 | the adoption rule — a strictly beneficial discovery joins the running build |
| `TOOL-aPrimedKeepalive-3` | 2 | the `discoveries-adopted` directive, so the rule is in the set a run reads at step 0 |
| `TOOL-aPrimedKeepalive-4` | 2 | leg check 7 stops counting a LANDING record whose work is already on the remote |
| `TOOL-aPrimedKeepalive-5` | 1 | `dCarriedReceipt`'s record gains the `landed-anchor` its own verb failed to write |
| `TOOL-aPrimedKeepalive-6` | 1 | hygiene check 23 takes the `--staged` guard its siblings carry, and the block stops calling itself 22 |
| `TOOL-aPrimedKeepalive-7` | 2 | the driver's live-run count takes the same exclusion the leg got |
| `TOOL-aPrimedKeepalive-8` | 1 | the Skill's two halves agree that a resumed keepalive is presumed ALIVE |
| `TOOL-aPrimedKeepalive-9` | 1 | the acceptance ledger evidences every criterion a fold added |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 9 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPrimedKeepalive-6 — hygiene check 23 takes the `--staged` guard its siblings carry, and the block stops calling itself 22](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-6.md) | 1 | 1 | CLOSED | rev-4 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-1 — the keepalive is scheduled as the run's FIRST act, on every start path](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-1.md) | 2 | 2 | CLOSED | rev-4 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-2 — the adoption rule: a strictly beneficial discovery joins the running build, decided at once](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-2.md) | 3 | 2 | CLOSED | rev-3 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-3 — the `discoveries-adopted` directive, so the rule is in the set a run reads at step 0](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-3.md) | 4 | 2 | CLOSED | rev-3 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-4 — leg check 7 stops counting a LANDING record whose work is already on the remote](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-4.md) | 5 | 2 | CLOSED | rev-4 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-5 — `dCarriedReceipt`'s record gains the `landed-anchor` its own verb failed to write](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-5.md) | 6 | 1 | CLOSED | rev-2 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-7 — the DRIVER's live-run count takes the same exclusion the leg just got](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-7.md) | 7 | 2 | CLOSED | rev-3 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-8 — the Skill's two halves agree that a resumed keepalive is presumed ALIVE](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-8.md) | 8 | 1 | CLOSED | rev-1 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-9 — the acceptance ledger evidences every criterion a fold added](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-9.md) | 9 | 1 | CLOSED | rev-1 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPrimedKeepalive-6` | no |
| 2 | `TOOL-aPrimedKeepalive-1` | no |
| 3 | `TOOL-aPrimedKeepalive-2` | no |
| 4 | `TOOL-aPrimedKeepalive-3` | no |
| 5 | `TOOL-aPrimedKeepalive-4` | no |
| 6 | `TOOL-aPrimedKeepalive-5` | no |
| 7 | `TOOL-aPrimedKeepalive-7` | no |
| 8 | `TOOL-aPrimedKeepalive-8` | no |
| 9 | `TOOL-aPrimedKeepalive-9` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
