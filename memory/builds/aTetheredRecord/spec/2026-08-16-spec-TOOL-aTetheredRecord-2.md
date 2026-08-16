# TOOL-aTetheredRecord-2 — the binding grammar and its read-only parser

**Status:** SPECCED · rev-2 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

## 1. Goal

Define the one authored line that binds a record to the spec it is evidence about, and put its parser
in the module that already reads every record's bytes. The parser raises nothing and writes nothing,
so an unannotated record can never brick the index render.

## 2. Scope (IN)

- **S1** — `read_bindings(root, tracked)` in `tools/memory-tree/gen_build_index.py`: over each
  tracked record, scan the unfenced head for the binding line and the optional inverse line, parse
  the grammar in §4, expand ranges, and return per-path results classified as bound, unbound-with-
  reason, or malformed.
- **S2** — `spec_ids(root, tracked)` in the same module: the first H1 id per file at any depth under
  a build's `spec/` folder. This is the resolution set, carrying a docstring that records why it is
  not the build README roster.
- **S3** — `--print-bindings`, a read-only mode emitting one tab-separated row per finding plus a
  count row, always exiting 0 and writing no file.
- **S4** — The prose home: a new catalog entry in `tools/memory-tree/HYGIENE.template.md` describing
  the rule, and the M4 and M8 paragraphs in `tools/memory-tree/BUILD-METHOD.template.md` naming the
  line a record must carry. Both re-rendered into their installed counterparts so the three document
  pairs stay byte-identical.
- **S5** — `--selftest` arms for every parse classification, the range expansion, the head-window
  boundary, and the read-only property.

## 3. Non-goals (OUT)

- **No enforcement.** This unit adds no `fail` branch and reds nothing. The gate is
  `TOOL-aTetheredRecord-4`, deliberately separate: the parser must exist and be exercised before a
  gate reads it, and a read-only mode is what lets `TOOL-aTetheredRecord-3` use the gate's own
  predicate as its retrofit checklist.
- **No render change.** The generated region is untouched here; that is
  `TOOL-aTetheredRecord-5` and is forked.
- **No id-resolution logic.** Whether a cited id resolves is already check 14's question and this
  unit does not re-answer it. See §10.
- **No coverage CLAIM from the kind token.** The vocabulary lands (Fork E, owner-resolved), but a
  `spec-audit` record still answers coverage-EVER, not coverage-at-rev, because the reviewed rev is
  optional under Fork C. `TOOL-aTetheredRecord-5` states that limit where the derived line renders;
  this unit must not let the token imply a claim the data cannot support.
- **No new module and no new gate leg.** The parse rides a module that is already a delegate, already
  carries a self-test, and already rides a leg.

## 4. Design

### Data model

A record carries, in its unfenced head, one line of either shape:

- the bound form — the key `Serves`, bolded and colon-terminated, followed by one or more space-
  separated ids;
- the unbound form — the same key followed by the single token `none`, an em dash, and a reason in
  prose. The reason is mandatory and unparsed: a bare `none` is malformed. This follows the rule the
  hygiene catalog already applies to bug-class records, where declaring no gate is acceptable and
  silence is not.

The line opens with a KIND token before the ids, from a closed vocabulary of four, DERIVED by
classifying the measured corpus rather than invented:

| Kind | What it is | A record that reads this way today |
|---|---|---|
| `spec-audit` | a pre-code adversarial pass over a spec or spec set (the M4 obligation) | "Tier-2 adversarial pass over TOOL-aNumeralWarden-1 at rev-1" |
| `diff-review` | a pass over BUILT code — a closing or cumulative diff (the M8 obligation) | "Closing Tier-2 review — TOOL-aGuardedTally-1 as BUILT" |
| `journal` | evidence of what was built: a build ledger, an AC transcript, a reproduction | "TOOL-aQuarriedLantern — build ledger" |
| `research` | a report that PRECEDES the specs — a commissioning input, census or design pass | "The playbook audit — the commissioning input" |

The vocabulary is closed and the check rejects an unknown token, because an open kind field is a
free-text column that stops being groupable the first time two authors spell one relation differently.

An optional second line carries the key `Commissions` and the same id list. It expresses the inverse
relation — this record PRODUCED those specs — and exists because the corpus contains records that
precede every spec in their build. It is never a substitute for the first line: a commissioning
record still states what it serves, which is usually `none` with the reason.

An id is the family-qualified form already used everywhere: one of the four family tokens, the build
slug, and the unit ordinal. Two optional extensions:

- **A reviewed rev.** An id may carry a trailing at-sign and rev token. It is recorded and never
  validated — see Fork C in §8.
- **A contiguous run.** A run of ordinals within one family and slug may be written with a range
  separator. It EXPANDS at authoring time to a fixed set, so unlike a wildcard it cannot rot when the
  build gains a unit.

Ids are fully qualified rather than bare ordinals precisely so a record can name a spec in another
build. The corpus needs this: one review filed under `aDrainedSluice` covers a second build's units.

### Inventory

| Element | Value | Why |
|---|---|---|
| head window | the first 12 unfenced lines | The deepest existing metadata line in the corpus sits at line 4; 12 is generous without admitting body prose. Fence-skipping reuses the module's existing helper, which is what keeps a fenced EXAMPLE of the grammar — in a spec like this one — from parsing as a real binding. |
| line prefix | optional leading whitespace and an optional comment marker | The one non-markdown record in the corpus is a shell script, where the line must be a comment. An extension-scoped rule would structurally exclude it. |
| resolution set | ids defined by a spec H1 | Measured 113 today, 118 after `TOOL-aTetheredRecord-1`. |
| NOT the resolution set | a build README `ids:` roster | Measured 179 ids of which 66 have no spec. The roster is a reservation range generated from citations anywhere, and it admits backlog and decision rows as if they were units. |

### Rollout

The parser lands inert. `--print-bindings` over the tree at that moment reports every record as
unbound, which is the true state and is not a failure — nothing consumes the classification until
`TOOL-aTetheredRecord-4`.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py`, `tools/memory-tree/HYGIENE.template.md`,
`tools/memory-tree/BUILD-METHOD.template.md`, their two installed counterparts under `memory/`, and
the kit version constant wherever it is spelled.

### Alternatives rejected

**Reuse the `Subject` key.** Five records already carry it, which reads as a ready-made convention.
Measured: four of the five carry a commit range, not a spec. The key has an established incompatible
meaning, so reusing it merges two relations into one field — the drift class, not reuse. `Serves`
collides with nothing in the tree.

**A new Python module.** It would have to join the delegate list, carry its own self-test, and claim
a codebase-map dossier. The generator already reads these files, is already a delegate, and already
rides a self-test leg, so the parse costs no new file and no new leg.

**Raising an exception on a malformed record.** The generator's collect step is reached by both the
check and the write verbs through one call site, so one bad record would refuse to render every
artifact, and the remedy string would live only on the failing path. A read-only classifier cannot do
that.

## 5. Production-readiness checklist

- security — N/A; the parser reads tracked text and executes nothing.
- perf / scale — the module already reads every record's bytes for the existing scan; this adds a
  bounded head parse per file over a corpus of 76.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a tree with no records prints a zero count and exits 0; a
  malformed line is classified, never raised.
- observability — `--print-bindings` is the observation, and it is what the retrofit consumes.
- risks — the head window and the fence-skip are the two places a wrong boundary silently changes
  the population. Both carry explicit arms. No write path, so no data-loss or rollback hazard.
- testing + left-shift gates — `--selftest`, already a gate leg.
- migration / rollback — inert on landing; revertible as one commit.
- user docs — the catalog entry and the two method paragraphs, in the shipped templates and their
  installed copies.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs on the live
  tree, it exits 0, and its unbound-classification row count equals the record count before the
  retrofit and zero after it.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --print-bindings` has run,
  `git status --porcelain` is empty — the mode wrote nothing.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it covers every parse
  classification, the range expansion, a line one past the head window being ignored, and a fenced
  example of the grammar NOT parsing as a binding.
- **AC4** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, all three document pairs
  are byte-identical after the prose lands in both halves.
- **AC5** — When `bash tools/check-kit-versions.sh` runs after the kit version is bumped at every
  live spelling derived by `git grep -n 'gov:kit memory-tree@'`, it is green.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs, it is green — a non-comment
  change to the hygiene engine and its kit version move together.

## 7. Gates

`memory hygiene (20 checks)` · `build-index selftest` · `kit/dogfood doc parity` · `kit version
markers` · `verdict epoch` · `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — the forks below are RESOLVED and kept for the record.

**Fork C — is the reviewed rev mandatory?** M4 selects specs whose rev moved since their last review,
so a binding without a rev answers coverage-ever rather than coverage-at-rev.

- *Option 1* — optional, recorded, never validated.
- *Option 2* — mandatory on all records. Unsatisfiable against the corpus without invention.
- *Option 3* — mandatory on new records only, which is a cutoff by another name.

RESOLVED (owner, 2026-08-17): option 1, by elimination rather than by preference. The owner's
no-cutoff ruling removes option 3, and option 2 cannot be satisfied for records whose review-time rev
is unrecoverable without fabricating one. The consequence is carried rather than hidden: the M4
coverage claim is STRUCK from this build, and the derived line in `TOOL-aTetheredRecord-5` is
labelled by what it computes.

**Fork E — does a record declare the KIND of relation?** RESOLVED (owner, 2026-08-17): yes, now. The
four-token vocabulary in §4 is derived from the measured corpus. It does not rescue Fork C — a
`spec-audit` token still answers coverage-ever — and §3 forbids letting the token imply otherwise.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.
- rev-2 · 2026-08-17 · folded the owner's fork resolutions. Fork E ratified ADD-NOW, so the grammar
  gains the closed four-token kind vocabulary in §4 and §3 gains the standing limit that the token
  must not imply a coverage claim Fork C cannot support. Fork C resolved by elimination.

## 10. Reuse audit

Three existing seams carry this unit, and the third is what makes it small:

1. **The head-scan pattern** — `gen_build_index.py:200-228` already reads a bounded head for the
   status header and already skips fenced regions. The binding parse is the same shape against a
   different key.
2. **The module's delegate status** — it is already called by hygiene check 9 and already listed in
   the verdict-epoch delegate set, so no new leg and no new dossier.
3. **Id resolution, which this unit deliberately does not build.** `corpus_ids.py:221` collects every
   id token on every corpus line as a citation, and check 14 already reds a citation no spec defines.
   An id written into a binding line is therefore already resolution-checked, for free, including a
   typo. This is why §2 has no resolution scope item.

`python tools/codebase-map/reuse_lookup.py "bind a build artifact to the spec id that warranted it"`
returned `parse_spec` and `build_reference_index` as the ranked seams; `parse_spec` is seam 1 above.
Recall terms: `build slug spec artifact filename header adversarial review closeout journal
bookkeeping convergence naming hygiene`.
