---
name: shipped-checker-edit-is-an-adopter-contract-change
description: the manifest checker in this repo is the copy every adopter installs, so an edit made for this repo's own kickoff changes what every adopter's gate demands on their next pull
kind: class
---

# Editing the shipped `manifest-check.sh` is an adopter contract change

## Symptom

An edit to `skills/session-kickoff/manifest-check.sh` is made to fix this repo's own kickoff — a
check loosened, a message reworded, a number moved. It lands, this repo's ratchet is green, and the
file is now different from the copy every adopter runs as `tools/manifest-check.sh`. They re-pull
on kit update, at which point their manifests are graded by rules they never saw change. The
divergence in between is invisible from here.

## Where it bit

The kickoff manifest carried this as a standing trap: the file is copied in by
`WIRE-INTO-PROJECT.md`'s recipe, a `cp` from `skills/session-kickoff/` into the adopter's tool
root, so the source here IS the product, and this repo is one adopter among several that happens
to share a checkout with it.

## The fix

Treat any edit to that file as a kit change, which the manifest's own tier rule already says is
Tier 2 — spec, review, then the edit — and never as a local repair. Check numbers and their
messages are a public surface: `check-arms` signatures and the adopters' pre-commit lines quote
them. A change this repo needs and adopters do not is a conf key or a flag, not a rewrite.

Gated by the `manifest-check self-test` leg (`skills/session-kickoff/manifest-check.test.sh`) for
the checker's own behaviour; the divergence between this file and an adopter's installed copy has
no machine gate, because the adopter's tree is not here. The documented check is the tier rule.
