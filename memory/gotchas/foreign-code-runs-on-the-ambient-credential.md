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
`GOVKIT_RERENDER=0` refused target-side execution, but that switch declines only the regenerate and
adopter steps. Update still runs each touched kit's `[check]` argv in the target, before the write and
again after it (`run_kit_check`, near lines 10015 and 11214).

## The fix

- An unattended item that touches another repository names its sandbox: a throwaway workspace, an
  emptied environment and no credential helper.
- It refuses target-side execution, and hands an update that needs it to that repository's owner as an
  outbox order. A claim that a switch refuses execution cites every execution site in the command,
  not only the ones the switch gates.
- It pushes through a grant scoped to the refs it writes on that one remote, declared on its adapter
  row.
- A fixture plants a payload in each kind of target-side code the command can reach: a regenerate
  argv, a kit's adopt script that its check runs, and a workspace hook. Each reads the credential
  helper and the environment, and expects to find neither.

It has no machine gate yet: dShippedRelease owes the sandbox and its fixture (`gap-deploy-13`).
