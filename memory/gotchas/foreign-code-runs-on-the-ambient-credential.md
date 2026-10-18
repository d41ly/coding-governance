---
name: foreign-code-runs-on-the-ambient-credential
description: an unattended item runs code another repository authored, on the node's whole environment and ambient credential, so that repository's committers gain the node's rights
kind: class
universal: false
---

# Another repository's code, on this node's credential

## Symptom

A command that installs into or updates another repository can execute code that repository chose: a
regenerate argv, a hook, an adopter script. Attended, a person sees the prompt and the command line.
Unattended, the code runs with the node's environment and its ambient credential. Anyone who can
commit to that repository can then act with the node's rights, on every remote the credential reaches.
The design reads as a plain update, because the execution happens inside the tool.

## Where it bit

The expansion round, 2026-10-16: `kits.offer` in
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` ran each
adopter's update unattended under `deploy.currency: push-branches`. govkit's update runs the target's
`[[regenerate]]` argvs and gained kits' adopters with the target as its working directory
(`tools/govkit/govkit.py`, near lines 10986 and 11114), and govkit's own warning on its apply path
says the target's committers choose what runs on the operator's machine. The node's push credential is ambient
(`credential.helper=manager`, from the system gitconfig). Run B of the round's review caught it as a
high finding (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md`,
H2), and run A did not.

The fold's closing review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`, H1) caught the fold's own fix overclaiming. It said
`GOVKIT_RERENDER=0` refused target-side execution, but that switch declines only the regenerate, hook-wiring and
adopter steps. Update still runs each touched kit's `[check]` argv in the target, before the write and
again after it (`run_kit_check`, near lines 10015 and 11214). This record once added each `[[hole]]`
discharge probe (`run_hole_probes`, near lines 10953 and 11800), which the same switch declines
(corrected 2026-10-17). The follow-up round
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md`,
H2) found that the fold's fix still left out the hook wiring, which runs the adopter's own
`settings-merge.py`, and the hole probes.

The debt round's two reviews of that fold
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md`
and `-b.md`) found a sixth kind that no switch declines: each `[[contract]]` parity probe, which runs
the adopter's own file in the target (`measure_contract_parity`, near line 6065, reached through
`derive_parity_lines`, near line 9658). The probe below, run then, lists every site.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Upgrade steps run in
an adopter's tree with no execution contract: a step's `git mv` fires the adopter's hooks, and its imports run adopter
code, in the workspace that pushes through the adopter's grant. The step kind now runs every step scrubbed, isolated and
hookless, with no ambient credential.

## The fix

- An unattended item that touches another repository names its sandbox: a throwaway workspace, an
  emptied environment and no credential helper.
- It refuses target-side execution, and hands an update that needs it to that repository's owner as an
  outbox order. A claim that a switch refuses execution cites every execution site in the command,
  not only the ones the switch gates.
- It pushes through a grant scoped to the refs it writes on that one remote, declared on its adapter
  row.
- A fixture plants a payload in each kind of target-side code the command can reach: a regenerate
  argv, a kit's adopt script that its check runs, the adopter's `settings-merge.py`, a hole's
  discharge command, a contract-probed file, a seed argv, a git hook that an index write fires
  (post-index-change) and a workspace hook. Each payload writes a canary when it
  runs, then reads the credential helper and the environment. Under a mode that refuses execution,
  the fixture asserts no canary and one refusal record per kind, so a payload that crashed before its
  canary cannot pass as refused. Under a sandbox that runs it, the fixture asserts the canary and
  finds neither the credential nor the environment.
- Probe: list every subprocess call reachable from the command whose working directory is the
  target, and fail when the design does not name each one. Its first run, on 2026-10-17, listed sites and
  checked nothing. Its revision takes the design's named list and fails when the reached sites differ, and
  it also reads git calls in the target, whose writes fire the target's own hooks: 27 sites in 9 functions
  on update's path (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`,
  `[probes-final]`).

It has no machine gate yet: dShippedRelease owes the sandbox and its fixture (`gap-deploy-13`).
