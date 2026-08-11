# build method — the rendered procedure a multi-pass build runs on

```toml
feature = "build-method"
title = "The build method: how to spec, review and build, rendered from the memory-tree kit"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = []
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = ["BUILD-METHOD.md"]
backlog-shards = []
[paths]
globs = [
  "tools/memory-tree/BUILD-METHOD.template.md",
  "memory/guides/BUILD-METHOD.md",
]
```

## Constraints & why

The unattended-run kit supervises a build but does not instruct one: between `RUNNING` and `--close`
the driver runs no loop, dispatches nothing and carries no prompt. The build method — how to spec,
how to review, how to build — was therefore retyped into chat at the start of every run, which is
precisely the state `aUnmannedHelm` found the *mandate* in before it became a kit.

**The method is generic, so it does not belong to the unattended kit.** Six of the owner's rules bind
attended builds too. It belongs to the memory-tree kit, which already owns the spec format
(`TEMPLATE-SPEC.md`) and the record rules (`HYGIENE.md`); the method is the third member of that
family, and the unattended kit POINTS at it the way it points at `LANDER` and `GATE_CMD`.

**It is a procedure, not an enforcement layer.** An earlier design pass built provenance ledgers,
blob pinning and per-obligation evidence anchors, and was rejected for scope — it answered "did the
run tamper with its instructions" when "how does a run work" had been asked. That record is
`memory/builds/aWrittenMethod/build/2026-08-11-build-aWrittenMethod-1-enforcement-pass.md`. Nothing
here grades a run; the merge bar does that.

**No new gate leg.** `tools/gate-legs.json` stays at 47. The method rides the existing
`kit-dogfood-parity.test.sh` as a third `PAIRS` row, whose two arms already cover the two ways a
rendered document goes wrong: the live copy drifting from a fresh render, and a placeholder surviving
one. A leg would have cost a dossier claim against a shrink-only `baseline.toml` list plus a
`run-gates` canary row, to answer a question an existing leg answers.

**The render direction is TEMPLATE to LIVE.** `kit-dogfood-parity.test.sh:30` states it and `:66`
implements it as `render "$ship" > "$live"`. Four memory-recall hits assert the opposite and are
stale; the spec's §10 records the discrepancy, because the same probe will mislead the next reader.

## Shared seams

- **`kit-dogfood-parity.test.sh`'s `PAIRS` string** — the population every document pair joins. Its
  success line now DERIVES the pair count from `PAIRS`; it was the literal `2 pairs`, a second
  hand-kept spelling of a population sitting in the file whose whole job is catching that class.
- **`adopt-memory-tree.sh`'s `render_doc`** — byte-identical in intent to the parity leg's `render()`.
  The scaffold `mkdir -p` must create `guides/`, because the redirect cannot create its own directory.
- **`{{KIT_DIR}}` / `{{TOOL_ROOT}}`** — the only two substitution keys of this renderer. `{{MEMORY_ROOT}}`
  is NOT one, so the memory root is spelled literally with the rename caveat `HYGIENE.template.md`
  carries. A `{{MEMORY_ROOT}}` in this template would survive the render and red the placeholder arm.
- **The four delivery sites** — `AGENTS.md` (the only zero-invocation carrier, via the `CLAUDE.md`
  import), `skills/session-kickoff/SKILL.md` Step 5b, `tools/unattended/SKILL.template.md` step 0,
  and `verb_resume`'s echo. Each spells a PATH, never a summary, so none can become a sixth carrier.

## Gaps

- **Three lines of headroom.** The rendered guide measures 247 lines against hygiene check 6's
  250-line cap; the byte axis is comfortable at ~17.6 KB of 20,480. The LINE axis binds, which makes
  the displacement rule in M1 load-bearing rather than decorative: the next addition must remove
  something or spill to `tools/memory-tree/README.md`, which is outside the index set.
- **Nothing detects a sixth carrier.** The design starts spelling-negative and every pointer is a
  path, but the repo accumulated four spellings of the unattended rules exactly this way. Enforcement
  was out of scope, so this is a discipline, not a check.
- **The unattended-side pointers are conditional prose.** `check-unattended.sh` permits its kit to be
  installed without memory-tree, so both pointers say "if this project ships one". Nothing verifies
  the conditional is honoured in either direction.
- **`M4` has no harness.** `tier2-review.js` reviews DIFFS and cannot be pointed at a document, so
  the spec audit is hand-run under the review protocol's caps. The most token-expensive obligation
  the method names is its least instrumented step.

## Reuse affordance

seam: kit-dogfood-parity.PAIRS — reuse for shipping any kit-authored document into an adopter's tree
under drift and placeholder gating; extend via one `<live>:<shipped>` row in `PAIRS` at
`tools/memory-tree/kit-dogfood-parity.test.sh:53`, which the derived pair count and both arms pick up
with no further edit.

seam: adopt-memory-tree.render_doc — reuse for delivering a rendered document to every adopter of the
memory-tree kit; extend via one `render_doc` call plus its target directory in the scaffold
`mkdir -p` at `tools/memory-tree/adopt-memory-tree.sh:59`.

seam: BUILD-METHOD.md delivery pointers — reuse for putting a document in front of a run without
adding a carrier; extend via a PATH-only pointer at one of the four sites, never a summary of what
the document says.

Extend the method by editing `tools/memory-tree/BUILD-METHOD.template.md` and re-rendering with
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` — never by hand-editing
`memory/guides/BUILD-METHOD.md`, which the next render overwrites while the parity diff passes over
the loss. Register any further document pair by appending to `PAIRS`; the count and both arms follow
automatically. To ship a new rendered document to adopters, add one `render_doc` call to
`adopt-memory-tree.sh` and make sure its target directory is in the scaffold `mkdir -p`.
