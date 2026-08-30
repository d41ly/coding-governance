# TOOL-aProvenReuse-1 — hygiene check 12 grades §10's CONTENT, behind a declared cutoff

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 3bfc5e87 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aProvenReuse-1.md](../prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md) | research | TOOL-aProvenReuse-2 |

<!-- /gen:spec-records -->

## 1. Goal

Make a spec's §10 Reuse audit carry the two facts `memory/guides/BUILD-METHOD.md` M5 requires of
it — which probe was run and what it found, and the recall terms that were used — so that the
obligation stops being satisfiable by any non-empty prose. The evidence must be a TRACKED file, so
the check works in a clone the run never touched.

## 2. Scope (IN)

- **S1** — a new cutoff key `SPEC10_EVIDENCE_CUTOFF` declared in `.memory-tree.conf`, in the same
  shape and with the same blank-resolves-forward guard as `SPEC10_CUTOFF`, and mirrored in
  `tools/memory-tree/.memory-tree.conf.example`.
- **S2** — an added assertion inside check 12's existing Tier-2 awk block in
  `tools/memory-tree/check-memory-hygiene.sh`: for a spec graded against the ten-section canon whose
  filename date is at or after `SPEC10_EVIDENCE_CUTOFF`, the §10 body must satisfy BOTH arms below.
- **S3** — the arms, matched case-insensitively as plain substrings (`index()`, never a regex, so no
  awk-dialect question arises):
  - **arm T (the recall terms)** — the body contains `recall terms` or `--terms`.
  - **arm P (the probe result)** — the body contains `reuse_lookup`, `reuse-lookup`,
    `no existing seam`, `no seam fits`, or `reuse-first`.
- **S4** — the failure line names WHICH arm is missing and the cutoff that armed it, so the remedy
  is readable without opening the checker.
- **S5** — `memory/TEMPLATE-SPEC.md` §10 states the two required facts and the cutoff, replacing a
  paragraph that describes the obligation without stating what satisfies it.
- **S6** — `tools/memory-tree/README.md` and the kit's `kit.toml` version move per the kit's own
  version discipline, and `bash tools/check-kit-versions.sh` is the authority on which carriers.
- **S7** — a self-test arm in `tools/memory-tree/check-memory-hygiene.test.sh` covering: a
  post-cutoff spec missing arm T reds; one missing arm P reds; one satisfying both passes; a
  PRE-cutoff spec missing both passes.

## 3. Non-goals (OUT)

- **N1** — grading the QUALITY of what §10 records. A citation that is wrong is out of reach of any
  substring test, and pretending otherwise is the false-confidence class §7 of the charter names.
- **N2** — proving the probe actually ran. That is node-local evidence and belongs to
  `TOOL-aProvenReuse-2`; this unit's evidence is tracked and this unit claims only what tracked
  evidence can carry.
- **N3** — repairing the 253 landed specs that would fail the predicate. The cutoff exists precisely
  so no landed spec goes retroactively red; a migration is a separate decision nobody has asked for.
- **N4** — extending the check to Tier-1 specs. `memory/TEMPLATE-SPEC.md` scopes the ten-section
  canon to Tier-2, and the existing awk cut already places the canon and the empty-body test on that
  side. This assertion rides the same cut rather than inventing a second scoping rule.
- **N5** — logging from `tools/codebase-map/reuse_lookup.py`. See the build README's third
  build-level rule.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `.memory-tree.conf` | S1 — the new cutoff declaration and its rationale |
| `tools/memory-tree/.memory-tree.conf.example` | S1 — the adopter-facing mirror |
| `tools/memory-tree/check-memory-hygiene.sh` | S1 shipped default + `-v ecut=`; S2–S4 the assertion |
| `memory/TEMPLATE-SPEC.md` | S5 — §10's body |
| `tools/memory-tree/README.md`, `tools/memory-tree/kit.toml` | S6 — version and check description |
| `tools/memory-tree/check-memory-hygiene.test.sh` | S7 — four arms |

The assertion sits immediately after the empty-body test, inside the block the awk already gates on
`want == canon10`. That placement is not cosmetic: `want` is the canon check 12 CHOSE by filename
date, so reusing it means the evidence arm can never grade a spec the section canon did not, and the
two cannot drift into disagreeing about which specs are ten-section specs.

The §10 body is collected by walking the same `body[]` array the empty-body loop walks, setting a
flag on the `## 10. Reuse audit` heading and clearing it on any later `## ` heading. §10 is canon
LAST, so in practice the flag runs to end of body; the clear-on-heading is written anyway because a
canon that grows a §11 must not silently widen this predicate's reach.

### Alternatives rejected

- **A new checker script.** Rejected: check 12 already reads, unfences and section-splits every
  spec in the tree, in one awk pass that replaced roughly thirteen forks per spec. A second reader
  of the same files would be a second answer to one question and would pay the walk twice.
- **A regex predicate.** Rejected: this file's own header records that interval expressions are
  spelled out character by character because a build that does not honour `{8}` would demand those
  literal bytes. `index()` on a `tolower()`ed body has no dialect surface at all.
- **Requiring a specific line grammar** (`**Reuse:** …`, in the shape of check 21's record
  bindings). Rejected: 156 landed specs already spell arm T as `Recall terms used:` and would have
  to be rewritten to match a new grammar they predate, and the grammar buys nothing a substring does
  not — nothing downstream PARSES §10, it is read by people and by M7's regrounding step.
- **Requiring arm P only.** Rejected: arm T is the arm with a named downstream consumer. M7 step 5
  says to re-run the recall probe with the terms recorded in §10, and that step is inert without it.

### Migration

None. The cutoff is set to this build's own date, so every tracked spec is grandfathered and the
first file the predicate grades is the next one anybody writes — including this spec and its
sibling, which is why both carry a filled §10.

### Rollout

One commit. The check is inert on every existing file by construction, so there is no dark-launch
question and nothing to flip.

## 5. Production-readiness checklist

- **Security** — N/A. No new write path, no new input from outside the repo; the checker reads
  tracked files it already reads.
- **Performance** — one extra pass over an already-loaded `body[]` array per Tier-2 spec, inside an
  awk invocation that already runs. No new process, no new file read. `memory hygiene` is an
  unguarded leg, so the cost lands on every bar and is measured in S7's own run rather than asserted.
- **Error states** — a blank `SPEC10_EVIDENCE_CUTOFF` resolves FORWARD to the shipped literal, never
  off, matching `SPEC10_CUTOFF`'s guard. An empty string compares earlier than every date, so
  resolving blank to blank would arm the predicate over the whole corpus, which is the one outcome
  the cutoff mechanism exists to prevent.
- **Observability** — the failure line names the file, the missing arm and the cutoff.
- **Testing** — S7.
- **Migration/rollback** — revert the commit; nothing is generated and nothing is stored.

## 6. Acceptance criteria

- **AC1** — a spec dated at or after the cutoff whose §10 omits arm T makes
  `bash tools/memory-tree/check-memory-hygiene.sh` exit non-zero, and the failure text names
  `§10` and the missing arm. Observed by staging the break, not asserted.
- **AC2** — the same, for a spec omitting arm P: `bash tools/memory-tree/check-memory-hygiene.sh`
  exits non-zero and its text names the probe-result arm.
- **AC3** — a spec dated BEFORE the cutoff whose §10 omits both arms leaves
  `bash tools/memory-tree/check-memory-hygiene.sh` at exit 0, proving the grandfathering is real
  rather than a comment.
- **AC4** — on the tree as it stands, `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with
  the cutoff at its declared value. This is the predicate-over-the-real-tree run §7 of the charter
  requires before wiring, and it must produce ZERO hits over 346 landed §10 sections.
- **AC5** — with `SPEC10_EVIDENCE_CUTOFF` temporarily set to `2026-08-04`, the same command reds and
  names 253 files. This is the liveness assertion for AC4: a predicate that reds nothing at its
  declared cutoff must be shown capable of redding, or AC4 is indistinguishable from a check that
  matches nothing.
- **AC6** — `bash tools/memory-tree/check-memory-hygiene.test.sh` passes with S7's four arms present,
  and the arm count the suite reports moves by four.
- **AC7** — `bash tools/check-kit-versions.sh` exits 0 after the version move.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the full bar, which carries `memory hygiene` unguarded. The
kit self-test leg (`memory-hygiene self-test`) is guarded on `tools/memory-tree/`, which this unit
touches, so it runs on this diff rather than being held. `bash tools/check-kit-versions.sh` for AC7.
What no gate here checks: whether the two arms are the RIGHT two facts to demand — that is a design
question the spec audit owns, not a predicate.

## 8. Open questions

- **Q1 — should arm P accept `reuse-first` as a satisfying token?** It admits a §10 that names a
  waiver instead of a finding. **RESOLVED (agent, 2026-08-31, delegated):** yes. The kit's own Skill
  asks a waived run to NAME the waiver in §10 and has no way to make it, so accepting the token is
  what converts that request into a record. Rejecting it would instead make `reuse-first` effectively
  unwaivable for any post-cutoff spec, which is a rule change M3 veto 2 puts outside this run's
  authority.
- **Q2 — should the cutoff be this build's date or the date the change lands?** **RESOLVED (agent,
  2026-08-31, delegated):** this build's date, `2026-08-31`. The two are the same day, and pinning
  the later of two identical values buys nothing. `UNITS_REGION_CUTOFF`'s own declaration records why
  a cutoff set after the landing commit re-opens the gap for every commit in between.

## 9. Revision log

- rev-1 · 2026-08-31 · authored by the aProvenReuse run.

## 10. Reuse audit

The seam this unit wires through is `tools/memory-tree/check-memory-hygiene.sh` check 12 — it
already reads, unfences and section-splits every spec in the tree, already grades §10's presence and
emptiness, and already carries the four-cutoff declaration idiom this unit adds a fifth member to.
No new script, no second reader.

`python tools/codebase-map/reuse_lookup.py "checking that a spec records a reuse audit before code
is written"` returned `check-memory-hygiene.sh`'s check family and the `memory-tree-hygiene`
affordance seam, plus `row_grammar.py`'s `cmd_check`. The row-grammar seam was inspected and
REJECTED: it grades table ROWS against a declared grammar, and §10 is free prose with 156 landed
files already spelling arm T their own way.

Recall terms used: `reuse-first reuse audit spec section 10 seam recall probe terms directive waiver
silent unchecked machine-checked prose`. That query surfaced `dFramedEntrypoint`'s round-1 finding
RECALL-1, which reproduced this defect on an eight-spec build, and `TOOL-dPromptedSeam-1`'s
observation that `check-memory-hygiene.sh:744` is already "the forcing function in as many words" —
both of which are evidence that the seam named above is the one the corpus already expects to hold
this rule.

Where a hit was STALE: none. The two claims about check 12's current behaviour above were re-read
against source at `tools/memory-tree/check-memory-hygiene.sh:1015-1047` rather than taken from the
records.
