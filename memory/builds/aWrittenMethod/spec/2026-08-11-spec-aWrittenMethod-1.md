# TOOL-aWrittenMethod-1 — the build method, rendered and delivered

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling+playbook+kickoff

## 1. Goal

The build method — how to spec, how to review, how to build — is retyped into chat at the start of
every run, which is the state `aUnmannedHelm` found the mandate in before it became a kit. Turn it
into one authored template that renders into this repo's guides, is pointed at from the four places a
run actually reads, and survives a compaction the agent cannot observe.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/BUILD-METHOD.template.md`, the authored source. Eleven sections M1
  through M11: what the method is, the spec set, forks, the spec audit, recall and reuse, passes and
  parallelism, regrounding, closing, the wrap-up, the unattended delta, and a pointer table. Budget
  **≤15,000 B and ≤220 lines**, measured on the RENDERED copy.
- **S2** — the render pair. One row appended to `PAIRS` in
  `tools/memory-tree/kit-dogfood-parity.test.sh`, producing `memory/guides/BUILD-METHOD.md`. The
  direction is TEMPLATE to LIVE, per that script's own DIRECTION note at `:30`. No new gate leg.
- **S3** — `tools/memory-tree/adopt-memory-tree.sh` gains one `render_doc` call, so an adopter of the
  memory-tree kit receives the method with the spec format and the hygiene rules it belongs beside.
- **S4** — `KIT_MEMORY_TREE_VERSION` `2.4` to `2.5` in `tools/memory-tree/check-memory-hygiene.sh`,
  because the kit's shipped set changed and `check-verdict-epoch.sh` dates verdicts by that constant.
- **S5** — delivery, four sites, each a PATH and never a summary: one line under Conventions in
  `AGENTS.md`; one sentence in `skills/session-kickoff/SKILL.md` Step 5b; a step 0 in
  `tools/unattended/SKILL.template.md` naming `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md`; and one
  `printf` in `verb_resume` at `tools/unattended/unattended.sh:374`.
- **S6** — the removals, which are the reason this build is spelling-negative. The §1 unattended
  block in `parallel-coding-governance.domain-rules.md` collapses from thirteen bullets to one
  pointer. The duplicate landing clause at `parallel-coding-governance.template.md:158` shortens.
  Three stale `AGENTS.md` claims go: the `CODEBASE_MAP_ROOT` requirement, "eleven checks", and "two
  dossiers".
- **S7** — `KEEPALIVE_INTERVAL` in `.unattended.conf`, rendered into the Skill beside the two
  keepalive tool names. Optional, and deliberately NOT added to the gate's required-key loop.
- **S8** — `memory/map/features/build-method.md`, or the equivalent `baseline.toml` entry, so the
  codebase-map coverage gate does not red on a guide no dossier claims.
- **S9** — `memory/TEMPLATE-SPEC.md` §8 gains the delegated-resolver grammar
  `RESOLVED (agent, <date>, delegated): <pick>`, with `tools/memory-tree/SPEC-TEMPLATE.template.md`
  re-rendered in lockstep. The corpus has one fork-resolution form and it hardcodes the owner.
- **S10** — read-path funding. `AGENTS.md:7` cites `memory/map/` rather than one dossier by path, and
  `:123` keeps its adopter warning while dropping the dossier path. Both citations are false or
  half-true today, so this is a repair that happens to free bytes.
- **S11** — backlog rows for what this build declines: the never-landed playbook cross-reference
  gate, and the risk that the method is later summarized into a sixth carrier.

## 3. Non-goals (OUT)

No enforcement. No provenance, blob pinning, evidence ledger, DoD obligation or gate check grading
whether the method was followed. Pass 1 designed that and it is rejected; the record is in
`../build/2026-08-11-build-aWrittenMethod-1-enforcement-pass.md`.

No new gate leg. `tools/gate-legs.json` stays at 47 entries, because the drift-audit probe
`_charter_mentions_every_leg` pins 7 of 47 at tolerance 0.

No `METHOD_DOC` or `BUILD_METHOD` conf key. The path derives from `MEMORY_ROOT`, which is already
required, so `render()` cannot substitute an empty value for a key that does not exist.

No `method:` fact in `RUN.md`. The protocol's §2 says the authored region carries exactly five facts
and never restates a derivable one, and this path is derivable.

Not the BASE forgery. That is `TOOL-aWrittenMethod-2` and it is a defect in the mandate check, not in
the method. Not the unattended kit's unreachable terminal phases either.

No document-review harness. `tier2-review.js` reviews diffs and cannot be pointed at a document; M4
states that outright rather than pretending otherwise. Whether to build one is a separate unit.

## 4. Design

The method is generic. Six of the owner's rules bind attended builds too, so it belongs to the
memory-tree kit, which already owns the spec format and the record rules, and NOT to the unattended
kit, which points at it the way it points at `LANDER` and `GATE_CMD`.

### Data model

| Artifact | Authored? | Governed by |
|---|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | yes, by hand | the parity leg's placeholder arm |
| `memory/guides/BUILD-METHOD.md` | no, rendered | the parity leg's diff arm, hygiene check 6 |

Hygiene check 6 caps a file in `memory/guides/` at 20,480 B and 250 lines. The S1 budget of 15,000 B
and 220 lines sits deliberately inside that, because a method at 240 lines has ten lines of headroom
and the first fold-in makes it red.

### Migration

Seven blockers from the pass-2 review are folded here rather than left in the method text.

**B1 — the roster is not `ids:`.** Measured: `memory/builds/aBatchedTribunal/README.md` reads
`ids: TOOL-aBatchedTribunal-1..-8` while its `spec/` holds three specs and the build closed with
three units. M2 derives the roster from the README's authored Units table, one row per unit, and
names `ids:` a reservation range that is explicitly not a roster.

**B2 — the hard floor contradicted Step 5b exit 5.** Two lenses raised it. The reconciliation is that
exit 5 governs the run's authority to LAND, not its authority to work: a unit whose ACCEPTANCE or
GATES cannot be derived is parked and set BLOCKED, the run continues with the remaining units, and
the run **may not merge or push**. That is forced by the owner's own rule that the push happens only
when the entire build is done, and a BLOCKED unit means it is not. The run closes surfacing the park.

**B3 — the pre-commit checklist was blind.** `gotchas.py --for-diff HEAD..HEAD` resolves to an empty
range and prints "touches no file". M6 invokes it after staging, in the form the tool supports, and
gives the literal `<pass-base>` recipe.

**B4 — the closing review's report reds check 5.** `tier2-review.js` writes a free-named file into
the review directory. M8 says to rename it to `<date>-review-<slug>-<seq>.md` before the next gate
run.

**B5 — the direct-Agent budget does not reset unattended.** It is keyed per prompt turn and an
unattended run has no next user prompt. M4 routes the spec audit through a `Workflow` script, whose
sidechain agents are uncounted, and states the budget so the reader knows why.

**B6 — "sub-spec major build passes" had vanished.** M2 gains a decomposition step ahead of Detect:
one mechanism per spec, a separate document or gate is a separate unit.

**B7 — the read path had negative margin.** S10 funds it by repairing two citations that are already
wrong, rather than by deleting a true statement.

### Files touched (estimate)

Sixteen files. Three are new: the template, its render, and the dossier. Six are removals or
repairs of existing text. The rest are one-line pointers.

### Alternatives rejected

The domain-rules companion, because it is an un-rendered product template carrying thirteen live
placeholders nothing substitutes, so a method written there tells an agent to run `{{REUSE_CMD}}`.

A hand-authored guide, because prose in two places with nothing holding them together is the fifth
carrier and this repo already has four.

A fifth rendered Skill, because it costs a gate leg at tolerance 0 and a Skill body loads only on
invocation, so nothing forces the first read.

## 5. Production-readiness checklist

- security — N/A. No new execution path, no new input, no credential surface.
- perf / scale — N/A. One render at adopt time and one diff per gate run.
- a11y — N/A. Not a user interface.
- i18n — N/A.
- error / empty / loading states — the parity leg's two arms already cover a missing live copy, a
  missing shipped copy, a drifted render and a surviving placeholder.
- observability — the gate prints the pair count; the render prints what it wrote.
- risks — the line cap is the live hazard, at 220 of 250 after this build. The displacement rule in
  M1 is the brake, and the named spill target is `tools/memory-tree/README.md`, outside the index set.
- testing + left-shift gates — no new leg. `kit-dogfood-parity.test.sh`, `check-kit-versions.sh`,
  `check-verdict-epoch.sh`, hygiene check 6 and the codebase-map coverage gate all grow to cover this
  automatically once S2, S4 and S8 land.
- migration / rollback — the method is additive; reverting is deleting two files and four pointers.
  The S6 removals are the only destructive part and each is a duplicate of surviving text.
- user docs — the method IS the doc. `WIRE-INTO-PROJECT.md` gains nothing: the adopter path is S3.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs, it reports three
  pairs and exits 0.
- **AC2** — When the template is edited and the render is not re-run, that leg reds naming
  `memory/guides/BUILD-METHOD.md`, and its printed remedy regenerates the live copy.
- **AC3** — When a `{{PLACEHOLDER}}` is left unsubstituted in the template, the leg's second arm
  fails naming the shipped file, independently of the diff arm.
- **AC4** — When `wc -c -l memory/guides/BUILD-METHOD.md` runs, it reports at most 15,000 bytes and
  at most 220 lines.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tree carrying the new
  guide, it exits 0.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, the new guide is claimed by a
  dossier and the leg exits 0.
- **AC7** — When `bash tools/check-kit-versions.sh` runs after S4, the memory-tree marker and
  constant agree at 2.5.
- **AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs after S5 and S7, it reports
  in sync and the rendered Skill carries no `{{`-shaped placeholder.
- **AC9** — When `grep -c 'BUILD-METHOD' AGENTS.md skills/session-kickoff/SKILL.md
  tools/unattended/SKILL.template.md tools/unattended/unattended.sh` runs, each reports at least one.
- **AC10** — When the domain-rules §1 unattended block is read after S6, it carries one pointer and
  no restatement of a rule that `memory/guides/UNATTENDED-PROTOCOL.md` already states.
- **AC11** — When `python tools/memory-tree/corpus_ids.py --measure` runs after S10, the charter read
  path is at most `READ_PATH_CEILING` with a positive margin, and the reported figure is recorded.
- **AC12** — When `bash tools/run-gates.sh` runs on a quiescent tree at the push boundary, all 47
  legs are green.

## 7. Gates

`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/check-verdict-epoch.sh` · `tools/check-kit-versions.sh` ·
`tools/check-template-size.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/adopt-unattended.sh --check` · `python tools/codebase-map/test_codebase_map.py` ·
`skills/session-kickoff/manifest-check.sh` · `tools/check-install-prefix.sh` · and the full
`bash tools/run-gates.sh` at the push boundary. No new leg is added.

## 8. Open questions

### F1 — does the method ship to adopters, or dogfood only

S3 puts a `render_doc` call in the memory-tree adopter, so every adopter receives the method. The
alternative is to render it here and leave adopters to write their own. **Recommendation: ship it.**
A kit that ships a spec format and hygiene rules but not the method for using them is the same
half-delivery this build exists to fix.

### F2 — the size budget, 15,000 B and 220 lines, against a 20,480 B and 250-line cap

The tighter budget costs content now and buys fold-in room later. **Recommendation: take the tighter
budget.** The pass-2 draft measured 17,282 B at 240 lines, which is ten lines from red, and every
review this method survives will want to add to it.

### F3 — `RESOLVED (agent, <date>, delegated)` in TEMPLATE-SPEC §8

The corpus's one fork form hardcodes the owner. An agent resolving a fork under delegation has no
honest way to record it and currently signs as the owner. **Recommendation: add the grammar.** The
alternative is that every delegated resolution is indistinguishable from an owner's, which is a
record-integrity problem this build is in a position to fix cheaply.

### F4 — the sixth-carrier risk has no mechanism

Nothing stops the method being summarized into a new carrier later, which is exactly how the four
unattended spellings accumulated. **Recommendation: a backlog row, not a gate.** Enforcement is out
of scope for this build and a check here would be the pass-1 mistake in miniature.

### F5 — `KEEPALIVE_INTERVAL` has no consumer but the Skill's prose

It is a value nothing reads except a rendered sentence. **Recommendation: declare it anyway, optional
and outside the required-key loop.** The cadence currently lives only in chat, and a declared value
that renders is strictly better than an undeclared one that does not. If it ever becomes checkable it
belongs in the protocol's §5, not here.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Converges two design passes: pass 1 (enforcement, rejected for
  scope, recorded under `build/`) and pass 2 (method and delivery). Folds seven blockers from pass
  2's adversarial stage into §4 Migration as B1 through B7.

## 10. Reuse audit

Two probes were run before any design was fixed, and one of them changed the build.

`python tools/codebase-map/reuse_lookup.py "render a shipped template document into the repo and gate
it against drift"` returned the codebase-map render family and `install-prefix`'s shipped-surface
seam. It confirmed the render-plus-parity shape is the repo's established idiom and that no new
mechanism is needed: the seam this unit wires through is
`tools/memory-tree/kit-dogfood-parity.test.sh`'s `PAIRS` string, which already carries two document
pairs and grows by one row.

`python tools/memory-recall/query.py` on why shipped kit documents are rendered rather than
hand-authored returned eleven relevant hits, four of which state the render direction is LIVE to
SHIPPED and that the template must never be hand-edited. **Those records are stale and were not
followed.** `tools/memory-tree/kit-dogfood-parity.test.sh:30` carries a DIRECTION note stating the
opposite — `--render` writes TEMPLATE to LIVE, the template is the authored source, and the live copy
is never hand-edited — and `:66` implements it as `render "$ship" > "$live"`. The direction was
reversed at some point and the records describing the old behaviour were never corrected. The design
follows source. This is the reason S1 names the template as the authored artifact and S2 names the
guide as generated, and it is recorded here because a future reader running the same probe will get
the same four misleading hits.

No existing seam covers the method's CONTENT, because none exists yet; that is the build.
