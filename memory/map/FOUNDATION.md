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
git-hooks = ["gate-env.sh"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
]
```

## Claim policy

Claim here only what is genuinely shared substrate (sanitization boundaries, shared transport
seams, ops tooling, the registries themselves). Feature-shaped items belong in
`features/<feature>.md` dossiers. Everything else waits in `baseline.toml` (shrink-only).

## What is claimed here, and why it is not a feature

`git-hooks/gate-env.sh` is THIS repository's gate policy: a file the shipped push hook
sources when it is present, and that no kit claims. It belongs here rather than in a
dossier because it is not a feature — it is one repo-local decision about the merge bar,
and the whole point of its location is that it sits outside every kit's payload. A choice
written into a file a kit copies is a choice every adopter inherits without making it;
govkit's selfcheck asserts that separation rather than trusting it.
TOOL-dUnstalledConvoy-28.
