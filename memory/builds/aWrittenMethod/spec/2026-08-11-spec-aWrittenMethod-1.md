# TOOL-aWrittenMethod-1 — the build method, rendered and delivered

**Status:** INPROGRESS · rev-3 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling+playbook+kickoff · review wf_198d8c01-46e · ratified 2026-08-11

## 1. Goal

The build method — how to spec, how to review, how to build — is retyped into chat at the start of
every run, which is the state `aUnmannedHelm` found the mandate in before it became a kit. Turn it
into one authored template that renders into this repo's guides, is pointed at from the four places a
run actually reads, and survives a compaction the agent cannot observe.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/BUILD-METHOD.template.md`, the authored source. Its content is the
  pass-2 draft at `../build/2026-08-11-build-aWrittenMethod-1-method-pass.md`, trimmed to budget and
  with B1 through B7 applied. Eleven sections M1 through M11, keeping that draft's own numbering.
  Budget: the hygiene check 6 caps on `memory/guides/*.md`, **≤20,480 B and ≤250 lines**, measured on
  the RENDERED copy. See F2 — the tighter self-imposed budget did not survive contact. Paths follow the
  `HYGIENE.template.md` precedent: `{{KIT_DIR}}/…` for own-kit paths, `{{TOOL_ROOT}}<kit>/…` for
  sibling kits, and a literal `memory/` for the memory root with that file's `:13` rename caveat.
  `{{MEMORY_ROOT}}` is NOT a substitution key of this renderer and would red the placeholder arm.
- **S2** — the render pair, **two edits** to `tools/memory-tree/kit-dogfood-parity.test.sh`: append
  the row to `PAIRS` at `:53`, and derive the printed pair count at `:90` from `PAIRS` instead of the
  hardcoded `2 pairs`. Bootstrap: `mkdir -p memory/guides && : > memory/guides/BUILD-METHOD.md`
  before the first `--render`, because `:63` returns early on a missing live copy and `:89` exits 0
  regardless, so the first render is otherwise a silent no-op.
- **S3** — `tools/memory-tree/adopt-memory-tree.sh`: add `"$M/guides"` to the `mkdir -p` at `:59`
  **and** one `render_doc` call. Without the directory the redirect dies mid-scaffold.
- **S4** — the kit version bump, **three sites**: the constant and inline marker at
  `tools/memory-tree/check-memory-hygiene.sh:13`, the marker at
  `tools/memory-tree/HYGIENE.template.md:1`, and a re-render of `memory/HYGIENE.md`. Required because
  `tools/check-kit-versions.sh:48-50` pairs the constant with the shipped marker.
- **S5** — delivery, four sites, each a PATH and never a summary: one line under Conventions in
  `AGENTS.md`; one sentence in `skills/session-kickoff/SKILL.md` Step 5b; a step 0 in
  `tools/unattended/SKILL.template.md`; and one `echo` in `verb_resume` at
  `tools/unattended/unattended.sh:374`. The two unattended-side pointers are phrased conditionally
  — "if the project installs the memory-tree kit's build method, read it first" — because
  `check-unattended.sh` permits the unattended kit to be installed alone. Re-render the Skill with
  `bash tools/unattended/adopt-unattended.sh`.
- **S6** — the removals. The §1 unattended block in `parallel-coding-governance.domain-rules.md`
  collapses to one pointer spelled `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`, with
  `MEMORY_ROOT` added to that file's catalog in `parallel-coding-governance.customize.md` (13 keys to
  14) and its three-deletion recipe at `:59-62` updated. The duplicate landing clause at
  `parallel-coding-governance.template.md:158` shortens. Both `governance-template` markers bump to
  v2.7 with a v2.6 snapshot into `memory/archive/`, and the template's history line describes the
  collapse. Four stale `AGENTS.md` claims go: the `CODEBASE_MAP_ROOT` requirement, "eleven checks",
  "two dossiers", and the "69 inventory keys" on the same line S10 edits.
- **S7** — `KEEPALIVE_INTERVAL` in `.unattended.conf`, plus its two sites in
  `tools/unattended/adopt-unattended.sh`: the initialiser at `:67` and a sixth `sed` arm in
  `render()`. Optional, and deliberately NOT added to the gate's required-key loop.
- **S8** — `memory/map/features/build-method.md`, carrying `## Constraints & why`, `## Shared seams`,
  `## Gaps` and `## Reuse affordance`, and claiming the `guides` key `BUILD-METHOD.md`. Regenerate
  `memory/map/generated/{MAP.md,inventories.json,symbols.json}`. There is no `baseline.toml`
  alternative: that file only shrinks and its own header bans new keys.
- **S9** — the delegated-resolver grammar `RESOLVED (agent, <date>, delegated): <pick>` is authored
  in `tools/memory-tree/SPEC-TEMPLATE.template.md` §8, and `memory/TEMPLATE-SPEC.md` is REGENERATED
  by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The grammar is prose-only:
  `check-memory-hygiene.sh:627-636` tests only that a terminal spec's first non-empty §8 line starts
  with `none` or `N/A`, and parses no `RESOLVED` form.
- **S10** — read-path funding and citation repair. `AGENTS.md:7` cites `memory/map/` rather than one
  dossier by path, and `:123` keeps its adopter warning while dropping the dossier path.
- **S11** — backlog rows for what this build declines: the never-landed playbook cross-reference
  gate, and the risk that the method is later summarized into a sixth carrier.

## 3. Non-goals (OUT)

No enforcement. No provenance, blob pinning, evidence ledger, DoD obligation or gate check grading
whether the method was followed. Pass 1 designed that and it is rejected; the record is in
`../build/2026-08-11-build-aWrittenMethod-1-enforcement-pass.md`.

No new gate leg. Not because a leg count is pinned — `drift_signals.py` pins the charter as naming 7
of 47 legs and counts the ones it FAILS to name, so a new leg would not move it — but because a leg
costs a dossier claim against a shrink-only `baseline.toml` list plus a `run-gates` canary row, and
the existing parity leg already answers this question.

No `METHOD_DOC` conf key. The path derives from `MEMORY_ROOT`, which is already required, so
`render()` cannot substitute an empty value for a key that does not exist.

No `method:` fact in `RUN.md`. The protocol's §2 says the authored region carries exactly five facts
and never restates a derivable one, and this path is derivable.

Not the BASE forgery (`TOOL-aWrittenMethod-2`), and not the unattended kit's unreachable terminal
phases. No document-review harness: `tier2-review.js` reviews diffs and M4 says so rather than
pretending otherwise.

## 4. Design

The method is generic. Six of the owner's rules bind attended builds too, so it belongs to the
memory-tree kit, which already owns the spec format and the record rules, and NOT to the unattended
kit, which points at it the way it points at `LANDER` and `GATE_CMD`.

### Data model

| Artifact | Authored? | Governed by |
|---|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | yes, by hand | the parity leg's placeholder arm |
| `memory/guides/BUILD-METHOD.md` | no, rendered | the parity leg's diff arm, hygiene check 6 |

Hygiene check 6 caps a file in `memory/guides/` at 20,480 B and 250 lines. Measured after the trim:
246 lines and 17,486 B. The byte axis is comfortable; the line axis has four and binds. F2 records
why the tighter self-imposed budget was abandoned rather than met.

### Migration

Seven blockers from the pass-2 review are folded here rather than left in the method text.

**B1 — the roster is not `ids:`.** Measured: `memory/builds/aBatchedTribunal/README.md` reads
`ids: TOOL-aBatchedTribunal-1..-8` while its `spec/` holds three specs and the build closed with
three units. M2 derives the roster from the README's authored Units table where one exists, else from
the conforming specs under `spec/`, and names `ids:` a reservation range that is explicitly not a
roster. Only 3 of 26 READMEs carry a Units table today, so the fallback is the common path.

**B2 — the hard floor defers to the kickoff engine.** `skills/session-kickoff/SKILL.md` Step 5b exit
5 states that an un-derivable ACCEPTANCE or GATES means ABORT, and that an ABORT stops. The method
does NOT restate or invert that: M2 points at exit 5 and adds nothing. Inverting an engine rule from
a document with no authority over it is the two-spellings class, and rev-1's park-and-continue
reading was exactly that. See F6.

**B3 — the pre-commit checklist was blind.** `gotchas.py --for-diff HEAD..HEAD` resolves to an empty
range and prints "touches no file". M6 invokes it after staging, in the form the tool supports, and
gives the literal `<pass-base>` recipe.

**B4 — the closing review's report reds check 5.** `tier2-review.js` writes a free-named file into
the review directory. M8 points at hygiene check 5's recording grammar rather than respelling a
narrower form, because a one-slug two-family build needs the optional FAMILY qualifier.

**B5 — the direct-Agent budget does not reset unattended.** It is keyed per prompt turn and an
unattended run has no next user prompt. M4 routes the spec audit through a `Workflow` script, whose
sidechain agents are uncounted, and states the budget so the reader knows why.

**B6 — "sub-spec major build passes" had vanished.** M2 gains a decomposition step ahead of Detect:
one mechanism per spec, a separate document or gate is a separate unit.

**B7 — the read path.** Measured 32,339 B against `READ_PATH_CEILING` 49,268. A 15,000 B guide leaves
1,929 B of margin before S10, so the build fits without S10 and S10 is reclassified as the
stale-citation repair it is, not as funding.

### Files touched (estimate)

Roughly twenty-five. Three new: the template, its render, the dossier. The rev-1 count of sixteen was
short by about nine — it omitted `HYGIENE.template.md`, `memory/HYGIENE.md`, the rendered
`.claude/skills/unattended/SKILL.md`, `adopt-unattended.sh`, `parallel-coding-governance.customize.md`,
the v2.6 archive snapshot, and the three `memory/map/generated/` artifacts.

### Alternatives rejected

The domain-rules companion, because it is an un-rendered product template, so a method written there
cannot carry a literal command line.

A hand-authored guide, because prose in two places with nothing holding them together is the fifth
carrier and this repo already has four.

A fifth rendered Skill, because it costs a gate leg and a Skill body loads only on invocation, so
nothing forces the first read.

## 5. Production-readiness checklist

- security — N/A. No new execution path, no new input, no credential surface.
- perf / scale — N/A. One render at adopt time and one diff per gate run.
- a11y — N/A. Not a user interface.
- i18n — N/A.
- error / empty / loading states — the parity leg's two arms cover a drifted render and a surviving
  placeholder; S2's bootstrap covers the missing-live-copy no-op the leg does not.
- observability — the leg prints a pair count derived from `PAIRS` after S2, not a literal.
- risks — the line cap is the live hazard. The displacement rule in M1 is the brake and the named
  spill target is `tools/memory-tree/README.md`, outside the index set.
- testing + left-shift gates — no new leg. The parity leg, `check-kit-versions.sh`, hygiene check 6,
  the codebase-map coverage gate and `drift_report.py --check` all grow to cover this once S2, S4 and
  S8 land.
- migration / rollback — additive; reverting is deleting two files and four pointers. The S6 removals
  are the destructive part and each duplicates surviving text.
- user docs — the method IS the doc. The adopter path is S3.

## 6. Acceptance criteria

- **AC0** — When `memory/guides/BUILD-METHOD.md` is read against
  `../build/2026-08-11-build-aWrittenMethod-1-method-pass.md`, every rule in that draft appears in the
  M section S1 assigns it, and each of B1 through B7 is applied.
- **AC1** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs, it reports three
  pairs from a count derived from `PAIRS` and exits 0.
- **AC2** — When the template is edited and the render is not re-run, that leg reds naming
  `memory/guides/BUILD-METHOD.md`, and its printed remedy regenerates the live copy.
- **AC3** — When a `{{PLACEHOLDER}}` is left unsubstituted in the template, the leg's second arm
  fails naming the shipped file, independently of the diff arm.
- **AC4** — When `wc -c -l memory/guides/BUILD-METHOD.md` runs, it reports at most 20,480 bytes and
  at most 250 lines. Separately, `grep -c 'tools/' tools/memory-tree/BUILD-METHOD.template.md`
  reports 0: the no-literal-prefix rule binds the TEMPLATE, because `{{TOOL_ROOT}}` renders precisely
  to `tools/` in this install and a rendered copy without it would be wrong, not clean.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tree carrying the new
  guide, it exits 0.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, the new guide is claimed by
  `memory/map/features/build-method.md` and the leg exits 0.
- **AC7** — When `bash tools/check-kit-versions.sh` runs after S4, the constant at
  `check-memory-hygiene.sh:13` and the shipped marker at `HYGIENE.template.md:1` both read 2.5 and it
  exits 0.
- **AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs after S5 and S7, it reports
  in sync and the rendered Skill carries no `{{`-shaped placeholder.
- **AC9** — When each of the four delivery sites is greped for its full path token
  (`memory/guides/BUILD-METHOD.md`, or `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` in the unattended
  template), every one matches; a bare-stem mention does not satisfy it.
- **AC10** — When the §1 unattended block is read after S6, it is at most three lines and holds
  exactly one path token.
- **AC11** — When `python tools/memory-tree/corpus_ids.py --report` runs after S1 and S10, the
  charter read path is at most `READ_PATH_CEILING` with a positive margin, and the measured figure is
  recorded in §9.
- **AC12** — When `bash tools/memory-tree/adopt-memory-tree.sh` scaffolds into a scratch tree, it
  produces `<MEMORY_ROOT>/guides/BUILD-METHOD.md` with no surviving placeholder. No gate leg covers
  this adopter, so this AC is the only thing that does.
- **AC13** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs after S9, the
  spec-template pair is green and `memory/TEMPLATE-SPEC.md` §8 carries the delegated grammar.
- **AC14** — When `python tools/drift-audit/drift_report.py --check` runs after S6 and S10, every
  signal is at or under its pin.

## 7. Gates

`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/check-verdict-epoch.sh` · `tools/check-kit-versions.sh` ·
`tools/check-template-size.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/adopt-unattended.sh --check` · `python tools/codebase-map/test_codebase_map.py` ·
`python tools/drift-audit/drift_report.py --check` · `skills/session-kickoff/manifest-check.sh` ·
`tools/check-install-prefix.sh` · and the full `bash tools/run-gates.sh` at the push boundary. No new
leg is added.

## 8. Open questions

### F1 — does the method ship to adopters, or dogfood only

**RESOLVED (agent, 2026-08-11, delegated): ship it.** S3 puts a `render_doc` call in the memory-tree
adopter. A kit that ships a spec format and hygiene rules but not the method for using them is the
same half-delivery this build exists to fix.

### F2 — the size budget

**RESOLVED (agent, 2026-08-11, delegated): take the tighter budget** — and it did not survive the
build, which is recorded here rather than quietly widened. Measured after trimming every rationale
clause that was not load-bearing: **246 lines and 17,486 B**. The byte axis has 2,994 B of headroom
and is comfortable; the LINE axis has four, and it binds. Cutting the further 26 lines to reach 220
would have cost rules the audit's coverage lens requires, so the budget is the hygiene cap and the
displacement rule in M1 is now load-bearing rather than decorative: the next addition must remove
something or spill to `tools/memory-tree/README.md`, which is outside the index set. S11 carries a
backlog row for the spill, because a four-line margin on a document designed to grow is a defect
waiting for its first fold-in.

### F3 — `RESOLVED (agent, <date>, delegated)` in the spec template

**RESOLVED (agent, 2026-08-11, delegated): add the grammar**, authored in the template per S9. The
corpus's one fork form hardcodes the owner, so a delegated resolution currently signs as the owner,
which is a record-integrity problem this build can fix cheaply. This spec's own §8 uses it.

### F4 — the sixth-carrier risk has no mechanism

**RESOLVED (agent, 2026-08-11, delegated): a backlog row, not a gate.** Enforcement is out of scope
and a check here would be the pass-1 mistake in miniature.

### F5 — `KEEPALIVE_INTERVAL` has no consumer but the Skill's prose

**RESOLVED (agent, 2026-08-11, delegated): declare it anyway**, optional and outside the required-key
loop. The cadence currently lives only in chat. If it becomes checkable it belongs in the protocol's
§5, not here.

### F6 — the hard floor versus kickoff Step 5b exit 5

The pass-2 draft's M2 said an un-derivable ACCEPTANCE or GATES parks the unit and the run continues;
exit 5 says ABORT and stop. Rev-1 called this a reconciliation, which the audit correctly identified
as inverting the engine's rule from a document with no authority over it. Two options: edit exit 5 to
park-and-continue, or have the method defer to exit 5 by pointer.
**RESOLVED (agent, 2026-08-11, delegated): defer by pointer.** It is one line, adds no spelling,
preserves the single source, and is the conservative reading. Editing a kickoff engine that reaches
sessions through a per-machine junction is a change whose blast radius exceeds this build.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Converges pass 1 (enforcement, rejected for scope) and pass 2
  (method and delivery). Folds seven pass-2 blockers into §4 Migration as B1 through B7.
- rev-3 · 2026-08-11 · built S1 and S2. Two corrections the build forced. AC4 asserted the RENDERED
  guide holds no `tools/`, which is backwards: `{{TOOL_ROOT}}` renders to exactly that, so the rule
  binds the template and the AC now says so. F2's 15,000 B / 220-line budget did not survive contact
  at 246 lines / 17,486 B; the budget is now the hygiene cap and the reasoning is in F2. Also caught
  by the gate while building: M2's example roster used a real family prefix with a placeholder slug,
  which hygiene check 14 correctly read as a live id citation with no definition. The example now
  spells the family as a placeholder too. This §9 line is worded to avoid the same trap.
- rev-2 · 2026-08-11 · folded review `wf_198d8c01-46e`, 53 raw findings, 20 confirmed, 13 rejected.
  Two blockers: S1 had no content source in the tree (the pass-2 draft is now committed under
  `build/` and AC0 grades against it), and S9 stated the render direction backwards — the same error
  §10 documents, made two sections later. Eight highs: the pair count at `:90` is a literal, the
  first `--render` is a no-op on a missing live copy, S4 is a three-site edit with the wrong stated
  cause, S3 needs the `guides` mkdir, S7 needs two `adopt-unattended.sh` edits, S5 needs the Skill
  re-render, and B2 inverted the kickoff engine's exit 5. F6 added and resolved. §4 file estimate
  raised from sixteen to about twenty-five. AC0 and AC12 through AC14 added; AC9 and AC10 made
  mechanical; the old AC12 whole-bar green deleted as banned by the format.

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
follows source. It is recorded here because a future reader running the same probe will get the same
four misleading hits, and because rev-1's S9 reproduced the error anyway: reading the correct fact
and writing the wrong one two sections later is the failure this note exists to prevent.

No existing seam covers the method's CONTENT, because none exists yet; that is the build.
