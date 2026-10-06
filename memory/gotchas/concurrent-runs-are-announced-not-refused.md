---
name: concurrent-runs-are-announced-not-refused
description: two live unattended runs of different builds are announced at preflight and never refused, and that is the ruling, not a gap
kind: invariant
decision: TOOL-aUnblockedFleet-1
---

## Looks wrong
`--preflight` lets an unattended run start while another build's run is live, and only prints a line about it.

## Actually
Concurrent runs of DIFFERENT builds are announced and never refused, because nothing is keyed on "the run" tree-wide; the same-slug claim refusal is a separate rule about one build.

The one-live-run rule protected a consumer that does not exist, measured by construction: with the
refusal and its leg check neutered in a scratch copy, two live records for unrelated builds left the
whole leg green and every verb resolved its own build. Every verb that resolves a build takes its
`<slug>`. The refusal unit 1 of the aGraftedHelix build added — a live or held claim on the SAME slug,
held by another session — is not what this ruling retired, and a finding about that refusal is not
covered here.

## Do
Announce each other live run at `--preflight`, as `tools/unattended/unattended.sh` does, and key every verb on its `<slug>`.

## Do not
Reinstate a tree-wide one-live-run refusal; the aDeferredBar build's spec audit caught a spec asserting that retired rule.

## Guarded by
`tools/unattended/unattended.test.sh`

Its concurrent-run arm pins the announcement. No bar leg runs that suite, so the guard names the file.
