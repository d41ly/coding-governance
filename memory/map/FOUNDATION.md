# foundation — the shared substrate (not a feature)

```toml
feature = "foundation"
title = "Foundation — shared substrate claimed outside any single feature"
status = "shipped"
streams = ["architecture"]
decisions = []

[claims]
gate-legs = ["run-gates evidence"]
kits = []
git-hooks = []
harness-hooks = ["SessionStart tools/check-wiring.sh"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  ".githooks/gate-env.sh",
]
```

## Claim policy

Claim here only what is genuinely shared substrate (sanitization boundaries, shared transport
seams, ops tooling, the registries themselves). Feature-shaped items belong in
`features/<feature>.md` dossiers. Everything else waits in `baseline.toml` (shrink-only).

## What is claimed here, and why it is not a feature

`SessionStart tools/check-wiring.sh` is claimed here because it is no kit's feature: it wires
every kit, auto-setting an unset `core.hooksPath` so a fresh clone runs with live gates.

`.githooks/gate-env.sh` is THIS repository's gate policy, sourced by the shipped push hook and
claimed by no kit, so no adopter inherits a choice it did not make (TOOL-dUnstalledConvoy-28). It
is a helper git never runs, so it is no `git-hooks` key (TOOL-aMendedFleet-39).
