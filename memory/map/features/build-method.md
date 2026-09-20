# build method — the rendered procedure a multi-pass build runs on

```toml
feature = "build-method"
title = "The build method: how to spec, review and build, rendered from the memory-tree kit"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aWrittenMethod-1"]

[claims]
gate-legs = ["method carriers (every pointer declared)", "method-carriers self-test", "build-method size"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["fold-text-is-unreviewed-surface.md", "amendment-leaves-its-other-half-standing.md",
  "one-value-field-records-a-mixed-outcome.md", "criterion-asserts-what-its-own-command-cannot-show.md",
  "observation-before-the-last-fold-of-the-same-commit.md",
  "hand-named-gate-list-green-while-the-bar-reds.md"]
guides = ["BUILD-METHOD.md"]
backlog-shards = []
lexicon-verbs = []
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

**The RENDER rides an existing leg; the CARRIERS needed their own.** The method is a third `PAIRS`
row on `kit-dogfood-parity.test.sh`, whose two arms already cover the two ways a rendered document
goes wrong. But nothing enumerated the files POINTING at it, so `check-method-carriers.sh` and its
self-test were added — 47 legs to 49. A self-test is itself a leg here, and both argv paths must
appear in the charter gate suite or drift counts the uncredited one against a pin sitting exactly at
its ceiling.

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

- **There is no local cap to measure headroom against, since `TOOL-aHonedRuleset-6`.** The method
  declared a byte and a line budget in its own opening prose, said in the same breath that no gate
  enforced the pair, and the owner ruled the claim DELETED rather than made enforceable. What is
  left is the hygiene class cap for `guides/`, a different constraint with a different owner. M1's
  displacement discipline survives as a norm with no enforced figure. *(This bullet described the
  pre-deletion state until `aHonedRuleset`'s closing review caught it, and it had also inverted the
  axis: the deleted prose said the BYTE half bound first.)*
- **The carrier check is STRUCTURAL, not semantic.** `check-method-carriers.sh` catches an
  undeclared carrier, a stale row and a copied `## M<n>` section. A fluent paraphrase that invents
  its own headings passes, and the leg says so rather than implying a comprehension it lacks.
- **One unattended-side pointer is still conditional, and it is now the only one.** The Skill's step
  0 is unconditional after `cBriefedPilot` unit 9, and `--preflight` REFUSES a tree with no method
  after unit 4 — so the kit is a run-time dependent rather than an optional reader. What survives is
  `verb_resume`'s echo, still guarded by `[ -f "$M/guides/BUILD-METHOD.md" ]`, and leg check 16's
  arm B, which stays silent when the carrier is absent BY DESIGN: the leg grades the tree, the driver
  grades the run.
- **`M4` HAS a harness now, and the rule states the mechanism rather than a category.**
  `TOOL-dTieredTribunal-12` replaced the ban with a declared-subject rule: `tier2-review.js` audits a
  spec when the call names the spec kind, and undeclared it acquires a diff and primes code-shaped
  lenses, which is why calling a spec reviewed by that run would be false. The wording matters more
  than the verdict. The old rule stated a CONCLUSION — a spec is not code — whose ground was a
  category assertion nothing could falsify, and it reached that state by losing its mechanism clause
  in a deletion no record explains. The replacement is falsifiable: it names the missing input, so a
  reader can check whether the call carries it. The obligation is still the method's least
  instrumented step, because nothing yet asserts that a spec audit HAPPENED.
- **A spec's gate list is authored. The bar's list is derived.** No check compares the two. Five builds
  closed a unit green on the legs their specs named while the unguarded codebase-map leg was red.
  The pre-commit hook now catches that one leg for staged `.py` and `.js` paths. For every other leg
  the defence is still a documented check: `hand-named-gate-list-green-while-the-bar-reds`.

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
