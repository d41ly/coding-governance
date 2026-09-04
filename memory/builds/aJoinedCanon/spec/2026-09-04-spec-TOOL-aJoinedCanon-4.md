# TOOL-aJoinedCanon-4 — a criterion names the break that would turn it red

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 750ca0ca · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `## 6. Acceptance criteria` ask each criterion what break would turn it red, because authors are
already answering that question in a section that never asked it. Finding A3 measured 93 of 479 specs
mentioning a staged break or a red-first run, clustering in §6 with 79 lines and in §5 with 30. The
format is collecting the answer by accident, in whichever section the author reached for, and can
therefore neither find it nor check it.

## 2. Scope (IN)

- **S1** — a per-criterion failure-mode clause, marked `Red when:`, stated in the acceptance-criteria
  body of `tools/memory-tree/SPEC-TEMPLATE.template.md`. The clause may sit on the bullet's opening
  line or on any continuation line beneath it, which is the same latitude the acceptance-witness rule
  already grants and matches this corpus's wrap style at 100 columns.
- **S2** — `SPEC_FAILURE_MODE_CUTOFF` declared in `tools/memory-tree/check-memory-hygiene.sh` beside
  the sibling cutoff constants at `:36-46`, blank-defaulting to off, and read from
  `.memory-tree.conf` by the same loader. Blank means OFF, taking `STREAMS_CUTOFF` semantics and not
  `SPEC10_CUTOFF`'s forward resolution, because this key switches one rule on rather than selecting
  between two canons.
- **S3** — the arm itself, inside the acceptance-witness walk that already exists at
  `tools/memory-tree/check-memory-hygiene.sh:1020-1048`. That walk already accumulates each AC
  bullet's opening line plus its continuation lines into `acc` and tests `acc` for a backtick pair.
  This adds a second test on the same accumulated string and a second entry in the same finding list.
  No new walk, no new section, no new `fail` branch.
- **S4** — the rule binds BOTH tiers, like the streams and witness ratchets and unlike the section
  canon. A Tier-1 spec is exempt from the ceremony, not from meaning what it writes.
- **S5** — both halves of the template move together. `tools/memory-tree/SPEC-TEMPLATE.template.md`
  is edited and `memory/TEMPLATE-SPEC.md` is REGENERATED from it by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited, because the two
  are byte-compared after placeholder substitution.
- **S6** — five fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, numbered 90 through 94
  in the free range above the current high of `tFixture-86`. They are the coverage: the live cutoff
  will sit ahead of every dated spec on every branch, so the real corpus cannot exercise the arm.
- **S7** — the documentation carriers. Item 12 of `tools/memory-tree/HYGIENE.template.md` gains one
  sentence beside its existing acceptance-witness sentence at `memory/HYGIENE.md:183-185`, and
  `KIT_MEMORY_TREE_VERSION` moves from `2.59` to `2.60` in the engine constant and in the
  `gov:kit memory-tree@` marker on every tracked `tools/memory-tree/*.template.md` and its rendered
  live copy.

## 3. Non-goals (OUT)

- **Grading whether the named break would actually fail.** The arm reads SHAPE only. It asserts that
  a criterion NAMES a break; it cannot assert that the break exists, that staging it would red
  anything, or that anyone ran it. A criterion whose failure mode restates its own negation satisfies
  this arm. That liveness lives with whoever observes the staged red, which is the charter's §7 rule
  and the journal record, not this gate. Said here because a structural check reads as a semantic one
  to everybody who did not write it.
- **Retrofitting the corpus.** 479 specs and 414 CLOSED ones stay untouched; the cutoff grandfathers
  them by filename date.
- **A `### Failure modes` table or any other second list.** Follow-up: none — it is rejected in §4,
  not deferred.
- **Anything about the acceptance ledger or check 23.** Joining a ledger answer to its criterion's
  tokens is `TOOL-aJoinedCanon-6`. This unit writes only inside check 12.
- **Widening the marker to the phrasings the corpus already uses in prose.** Follow-up: reopen only
  if the fixtures or a later measurement show the single spelling rejecting honest criteria.
- **A new gate leg.** The arm rides check 12, which the `memory hygiene` leg already runs.

## 4. Design

### Data model

One marker, one spelling: `Red when:`. It is matched case-insensitively as the nine-byte string
`red when:` by `index()` over a `tolower()`ed accumulator, which is the dialect-free idiom the §10
evidence arm already uses at `tools/memory-tree/check-memory-hygiene.sh:1226-1240`. The file's own
header records that interval expressions are spelled out character by character to survive an awk
build that does not honour `{8}`; a substring test has no dialect surface at all.

A conforming bullet therefore looks like this, with the clause on a continuation line:

```markdown
- **AC1** — When `check-memory-hygiene.sh` runs over the fixture tree, it names `tFixture-90`.
  Red when: the fixture's only criterion carries no clause and the arm stays silent.
```

There is no `N/A` escape and no second form. That is the acceptance ledger's own ruling applied one
level up: `memory/HYGIENE.md:303-306` says TWO forms and no third, and no `N/A`, on the stated ground
that a third form is how an evidence field becomes a checkbox exercise. A criterion whose break is
merely its own negation costs one clause to write, and the author discovering that the negation is
all there is IS the finding — that is the "criteria that could not fail reached close" case A3 names.

### Inventory

| carrier | change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | one paragraph in the §6 body, beside the witness rule at `:210-214` |
| `memory/TEMPLATE-SPEC.md` | regenerated by `kit-dogfood-parity.test.sh --render`, never hand-edited |
| `tools/memory-tree/check-memory-hygiene.sh` | the cutoff constant, one `-v` on the awk at `:956`, one test and one message inside the walk at `:1020-1048` |
| `.memory-tree.conf` | `SPEC_FAILURE_MODE_CUTOFF` with its date and the reason for that date |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixtures 90-94 and their `hit`/`miss` assertions |
| `tools/memory-tree/HYGIENE.template.md` | one sentence in item 12; `memory/HYGIENE.md` regenerated |
| kit version | `2.59` → `2.60` in the constant and in six `gov:kit memory-tree@` markers |

### Migration

None. The cutoff is a date compared against a filename, and blanking the key in `.memory-tree.conf`
turns the arm inert. There is no state and no data to move.

### Rollout

Dark by construction. The arm is doubly gated: `SPEC_FAILURE_MODE_CUTOFF` must be non-blank, and
check 12's outer guard `[ -n "$SPEC_FORMAT_CUTOFF" ]` at `:913` must hold, so an adopting repo with
no spec-format ratchet receives no failure-mode ratchet either.

### Files touched (estimate)

Seven files, four of them one-line or one-paragraph edits. The engine change is roughly six lines
inside a loop that already exists; the fixture file is the bulk of the diff.

### Alternatives rejected

- **A `### Failure modes` sub-head under §6, one row per AC.** It duplicates the AC numbering into a
  second list that goes stale the moment a criterion is renumbered, which is exactly the unjoined
  seam this build exists to remove. Rejected on the build's own premise.
- **A section-level minimum — §6 mentions one break somewhere.** One line would satisfy ten criteria.
  That is the vacuous-selector class the charter names, and BUILD-METHOD M3's counter-rule refuses an
  observation that passes by matching nothing.
- **Widening the marker to `reds when`, `would red` or `fails when`.** Measured over the tracked spec
  corpus with `git grep -ci`: `would red` appears in 92 specs, `staged break` in 43, `reds when` in
  33, `red-first` in 18. All four are prose, and admitting them would let an incidental sentence
  satisfy the arm. The §10 terms arm took this exact decision and recorded the reason at
  `check-memory-hygiene.sh:1219-1225`: a false red names its own remedy, a false pass is silent.
- **A `Red when: n/a — <why>` escape.** Rejected on the ledger precedent above.

## 5. Production-readiness checklist

- security — N/A. The change reads tracked markdown and writes nothing.
- perf / scale — one `index()` per accumulated AC bullet inside a loop that already walks them. The
  batched awk at `:956` is the shape that took check 12 from ~13 forks per spec down to one pass, and
  this adds no pass.
- a11y — N/A. No user interface.
- i18n — N/A, and deliberately: the marker is an ASCII literal, which is what makes it safe under a
  mojibake-prone toolchain. The corpus is English-only by construction.
- error / empty / loading states — an empty §6 is already refused by the empty-body walk at
  `:1183-1197`; a §6 with a heading and no AC bullet is outside this arm and stays so.
- observability — the finding names the offending bullet's label and the cutoff key, matching the
  witness message at `:1046-1047`.
- risks — one, and it is a false-red risk rather than a data risk: a cutoff set behind a live spec's
  filename date reds landed work. Rollback is blanking the key. There is no concurrency and no data
  loss surface.
- testing + left-shift gates — five fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`.
  That harness is the ONLY arm available: `tools/memory-tree/check-arms.py` cannot see a branch
  inside an awk body, which is why the fixtures are scope and not a nicety.
- migration / rollback — see §4. Blank the key.
- user docs — the §6 body of `memory/TEMPLATE-SPEC.md` and item 12 of `memory/HYGIENE.md`, both
  rendered from their kit templates.

## 6. Acceptance criteria

- **AC1** — When a Tier-2 spec dated on or after the cutoff carries an AC bullet with no `Red when:`
  clause, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 and its output names that bullet's
  label and `SPEC_FAILURE_MODE_CUTOFF`.
  Red when: the branch never fires and the run is silent about `tFixture-90`.
- **AC2** — When that same bullet gains the clause, `bash tools/memory-tree/check-memory-hygiene.sh`
  is silent about `tFixture-91`, with no other fixture change.
  Red when: the marker test matches the wrong string and reds a conforming bullet.
- **AC3** — When the identical clauseless bullet sits in a fixture dated strictly inside
  `[SPEC_FORMAT_CUTOFF, SPEC_FAILURE_MODE_CUTOFF)` in the harness's scratch tree,
  `bash tools/memory-tree/check-memory-hygiene.sh` is silent about `tFixture-92`.
  Red when: the date comparison is dropped and the arm grades the grandfathered era too.
- **AC4** — When the clause sits on a CONTINUATION line rather than the bullet's opening line,
  `bash tools/memory-tree/check-memory-hygiene.sh` is silent about `tFixture-93`.
  Red when: the test is applied to the opening line instead of to the accumulated `acc` string.
- **AC5** — When the clauseless bullet sits in a `Tier-1` spec dated after the cutoff,
  `bash tools/memory-tree/check-memory-hygiene.sh` still reports `tFixture-94`.
  Red when: the branch is placed below the `if (hdr ~ /Tier-1/) next` cut at
  `check-memory-hygiene.sh:1170`, which silently narrows S4 to Tier-2 and leaves the harness
  byte-identical.
- **AC6** — When `SPEC_FAILURE_MODE_CUTOFF` is blank in `.memory-tree.conf`, the AC1 fixture passes
  and `bash tools/memory-tree/check-memory-hygiene.sh` prints no failure-mode finding at all.
  Red when: the blank string compares earlier than every date and arms the rule over the whole corpus,
  which is the `ecut != ""` conjunct the §10 arm records at `:1211-1213`.
- **AC7** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs after the edit, it
  reports no drift between `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`.
  Red when: one half was edited and the other was not, which is the build's fifth rule.
- **AC8** — When each of the five fixtures is staged as a break and the suite is run,
  `bash tools/memory-tree/check-memory-hygiene.test.sh` is observed RED for that fixture before the
  fixture is unstaged, and the observation is recorded per item in this unit's journal record.
  Red when: an arm passes by finding nothing, which is the class this whole unit is about.

## 7. Gates

- `memory hygiene` — the leg that runs check 12 over this tree.
- `memory-hygiene self-test` — the leg that runs `tools/memory-tree/check-memory-hygiene.test.sh`
  and therefore the five new fixtures.
- `kit/dogfood doc parity` — the byte-compare that binds the two template halves together.
- `verdict epoch (kit version dates the engine)` — a new arm changes the engine's verdicts, so
  `KIT_MEMORY_TREE_VERSION` must move in the same landing. Verified at
  `tools/memory-tree/check-verdict-epoch.sh:2-18`.
- `spec tokens (a spec's own names resolve)` — this spec's own backticked names must resolve.
- No new leg. The arm adds no `fail` branch either: check 12 has exactly one `fail 12` site, at
  `tools/memory-tree/check-memory-hygiene.sh:1291`, so the per-gate `ARMS_FLOORS` pair that
  `tools/memory-tree/check-arms.py` reads does not move.

## 8. Open questions

- **F1 — where `SPEC_FAILURE_MODE_CUTOFF` lands, and whether this build's own specs are its first
  subjects.** Two in-corpus precedents pull opposite ways. `STREAMS_CUTOFF` and `SPEC_WITNESS_CUTOFF`
  were both set strictly ahead of every committed spec so nothing landed went retroactively red,
  which left the required arm with no live data and made the fixtures the only coverage —
  `.memory-tree.conf:24-27` records that trade in as many words. `SPEC10_EVIDENCE_CUTOFF` went the
  other way at `2026-09-01`, and 79 tracked specs are dated at or after it. Setting this one at
  `2026-09-04` would make the twenty specs dated that day its first live subjects, eleven of them
  this build's own, and every one of them would need its criteria amended before the arm could go
  green. **Recommendation: land it at the arm's landing date, strictly ahead of every dated spec on
  every live branch.** The build's third rule says every template change is a dated cutoff and never
  a retrofit, and redding twenty live spec files to buy a live example is the one outcome that makes
  this unit a net loss. The counter is real and is why this is a fork rather than a decision: the
  witness ratchet deliberately made its own spec the first subject, and that bought an example the
  fixtures cannot. Owner's call.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grading each acceptance criterion bullet for a required
clause behind a dated cutoff"` returned no seam that fits. Its top candidates were
`require_adopted_root` in `tools/codebase-map/map_lib.py` and a set of affordance-seam prose hits in
unrelated dossiers, all matched on name stems rather than on behaviour. That is expected and is not a
gap in the map: the seam this unit extends is an awk block inside a shell script, and the map indexes
symbols, inventory keys and dossiers, none of which reach inside `check-memory-hygiene.sh`'s single
batched awk. The seam is named directly instead, verified by reading it: the per-bullet acceptance
accumulator at `tools/memory-tree/check-memory-hygiene.sh:1020-1048`, which already folds each AC
bullet's continuation lines into `acc` and tests that string. The retrieval probe found the record
that built it — `memory/builds/cTracedPromise/spec/2026-08-15-spec-cTracedPromise-2.md`, whose S1
through S7 are the shape this spec deliberately mirrors, down to the doubly-gated cutoff, the
both-tiers claim and the grandfathered fixture whose date must sit strictly inside the pre-cutoff
window. Recall terms used: acceptance witness backticked token SPEC_WITNESS_CUTOFF check 12
per-bullet accumulator continuation line ratchet grandfathered fixture staged red.
