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
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
[paths]
globs = [
]
```

## Claim policy

Claim here only what is genuinely shared substrate (sanitization boundaries, shared transport
seams, ops tooling, the registries themselves). Feature-shaped items belong in
`features/<feature>.md` dossiers. Everything else waits in `baseline.toml` (shrink-only).
