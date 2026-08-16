# The design pass — how the binding carrier was chosen

**Serves:** none — this record PRECEDES the spec set and commissioned it; it is the class-4 case the
design must handle, written here in the grammar it proposes as the first live specimen.
**Commissions:** TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6

*Adversarial design pass run 2026-08-16 against BASE `96141aed`, the tip of `origin/main`. Three
carriers were designed independently, five skeptic angles tried to break all three, and one synthesis
pass composed the survivor. 13 agents, 0 errors, 2.13 M subagent tokens, 55 findings — 11 blockers
and 17 highs. Every number in this record was re-measured against source by the orchestrator before
inclusion; the four places the synthesis was wrong are enumerated below rather than quietly fixed.*

## The commissioning measurement

At BASE `96141aed`, over the tracked tree:

| Fact | Value | Derived by |
|---|---|---|
| records under a build's `build/`, `prompts/`, `reviews/` | 76 | `git ls-files` over the three subfolders, any depth, any extension |
| of those, naming no id in their first six lines | 54 | first-six-line scan for the family-qualified id form |
| non-markdown records | 1 | `aMooredAnchor/build/2026-08-11-build-aMooredAnchor-1-repro.sh` |
| ids defined by a spec H1 | 113 | first H1 id match per file under a build's `spec/` |
| ids appearing in a build README `ids:` roster | 179, of which 66 have no spec | the roster is a reservation range, not a unit list |
| spec files carrying no family-qualified H1 | 5 | exactly the five rows of `memory/project/id-orphan-waiver.txt` |
| review records carrying the literal verdict line M4 requires | 12 of 53 | `^## Verdict:` scan |

The recording-name grammar at `tools/memory-tree/check-memory-hygiene.sh:313` constrains the trailing
ordinal to a run of digits and nothing else. Nothing has ever required it to resolve.

## What each candidate proposed, and what killed two of them

**Candidate 1 — the filename carries the binding.** Dropped on four blockers. Widening the ordinal
slot to admit an id list collapses the CLOSED family alternation for the entire non-spec population,
flipping a live fixture from red to green. Its adopter escape hatch was `legacy-files.txt`, which is
a three-check exemption — pasting a path list there to bound the migration also disables broken-link
detection for those files. The binding would live in the one place the index derivation cannot read,
since that derivation scans file TEXT. And the rename touches 103 cross-referring lines in 62 files.

**Candidate 3 — the generated index carries the binding.** Dropped. A generator cannot invent a
binding it is not told, so the angle needs the authored line regardless. Its enforcement was the
generator's own exception path, which is reached by both the check and the write verbs through one
call site: a single unannotated record would refuse to render all 41 artifacts, and the remedy string
only existed on the failing path. Its render-time wildcard, which expanded a whole-build binding at
render time, is the false-green direction — it rewrites history as the roster changes, and 66 of 179
roster ids have no spec to expand to.

**Candidate 2 — an authored head line carries the binding.** Survives, with corrections. Its proposed
key was `**Subject:**`, reusing a field five records already carry. Refuted and changed: four of
those five carry a COMMIT RANGE, not a spec, so the field has an established incompatible meaning and
reusing it is the drift class rather than reuse. The key is `**Serves:**`, which collides with
nothing tree-wide (verified: zero hits). Its gate placement — a third call site behind check 5 —
was also refuted: the test harness re-arms on each check's failure header, so a second predicate
behind one number destroys attribution between the two. Check 21 gets its own number.

## The mechanism that survived

Every tracked record under a build's `build/`, `prompts/` or `reviews/` carries one authored
`**Serves:**` line in its head, naming the spec ids it is evidence about, or the single token `none`
with a mandatory reason. Ids are fully qualified, so a record can name another build's spec — which
the corpus needs, because one review under `aDrainedSluice` covers a second build's units. An
optional `**Commissions:**` line carries the inverse relation for records that PRODUCED specs.

Resolution costs no new machinery. `tools/memory-tree/corpus_ids.py:221` already collects every id
token on every line of the corpus as a citation, and check 14 already reds a citation that no spec
defines. Writing an id into a record therefore inherits resolution for free; check 21 only has to
enforce PRESENCE and SHAPE.

The five classes the corpus actually contains are all expressible: one spec, many specs, the whole
build (enumerated, never wildcarded), no spec yet (the `none` escape, bounded by a shrink-only
count), and cross-build (an id is an id).

## Where the synthesis was wrong, and what the spec carries instead

Recorded because a design pass that reports only its conclusions cannot be graded.

1. **The check-count rename plan was incomplete.** It named six carriers found by `git grep '20
   checks'`. Two more spell it hyphenated — `README.md:33` and `tools/memory-tree/README.md:6` —
   for eight spellings across seven files. The corpus already learned this: a prior review used a
   `[0-9]+-check` pattern for exactly this reason. The spec carries the wider predicate.
2. **Verdict coverage was reported as 22 of 53.** Measured: 12 of 53 carry the literal line M4
   requires; 27 carry some verdict heading. The recommendation stands and its figure changed.
3. **The record count was reported as 76 against an orchestrator measurement of 75.** The synthesis
   was right and the orchestrator was wrong: the missing file is the one non-markdown record, and it
   is exactly why check 21's population must be extension-agnostic rather than markdown-scoped.
4. **The census's four "unrecoverable" artifacts are recoverable, but not by the route two
   candidates took.** They resolve because the five missing spec H1s can be minted in five one-line
   edits, not because their ids appear in a README roster — that roster route is refuted by the same
   66-of-179 measurement that killed the wildcard.

## Findings deliberately not folded

- **Making the reviewed rev mandatory.** M4 is rev-keyed, so the criticism is correct. The remedy is
  unsatisfiable: the rev at review time is unrecoverable for most of the 76, and requiring it only of
  new records is a cutoff, which the owner ruled out. The rev is optional; instead the M4 coverage
  CLAIM is struck from the spec, and the derived line is labelled by what it actually computes.
- **Widening the harness meta-gate beyond shell.** Correct and out of scope: it would immediately red
  on six already-unarmed exception sites in the generator. The design keeps its own fail branches in
  the shell so it never depends on that widening. It is a recommendation, not a scope item.

## Two live defects found in passing

Both are real today, neither is caused by this build, and both are recorded rather than silently
repaired.

- `memory/project/unarmed-branches.txt` declares itself EMPTY in its own header while carrying one
  row, and `memory/HYGIENE.md:240` repeats the claim — as does the shipped
  `tools/memory-tree/HYGIENE.template.md:240`, so every adopter receives it. `ARMS_FLOORS` confirms
  the row is real: one gate is pinned at 57 branches and 56 armed.
- `AGENTS.md:94` states the hygiene check count as unguarded prose, two clauses after explaining why
  it deliberately does NOT restate the kit version — "a version written in prose rots between bumps,
  and this one rotted twice in a day". The same lesson, not applied to the number beside it. The
  playbook parity gate has a declared-pair mechanism built for exactly this and no pair covers it.

## Method

Four survey lenses mapped the gate surface, the render surface, the adopter surface and the full
artifact census. Three design agents each pushed one carrier as far as it honestly went, each
required to state its own strongest objection. Five skeptic angles — retrofit feasibility, gate
mechanics, adopter blast radius, redundancy and drift, and semantics — attacked all three with a
default of REFUTE. One synthesis pass composed the survivor. Fan-out and concurrency were bounded at
5 throughout, per `memory/guides/REVIEW-PROTOCOL.md`.
