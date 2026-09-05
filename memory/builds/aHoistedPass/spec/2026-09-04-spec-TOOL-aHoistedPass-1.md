# TOOL-aHoistedPass-1 — the record catches up with the verdicts that superseded it

**Status:** CLOSED · rev-4 · 2026-09-05 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-05-prompt-TOOL-aHoistedPass-1-brief.md](../prompts/2026-09-05-prompt-TOOL-aHoistedPass-1-brief.md) | journal | — |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md) | spec-audit | TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md) | spec-audit | TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

This repo's decision index still names `parallelism route: none` as the standing verdict and a live
backlog row still says the two experiments that would re-open it were never run; both were superseded
on 2026-08-21 and neither record knows it. Correct the record, and give every residual this build
knowingly leaves open a durable, greppable home instead of a paragraph in a design document.

## 2. Scope (IN)

- **S1** — Append ONE row to `memory/DECISIONS.md` superseding `TOOL-cBriefedPilot-21` (the file's line
  65 at this base) for route R2+R5, citing `TOOL-dUnstalledConvoy-7` and the record that carries the
  cleared verdict. The superseded row is not touched: the log is append-only.
- **S2** — Amend `TOOL-cBriefedPilot-28` in `memory/backlog/TOOL.md` so it no longer states that E3 and
  E4 "never were" run. The id and the `OPEN` token stay: two of its three clauses are still true.
- **S3** — File one backlog row per residual bullet of the design record's §10, each carrying the token
  `aHoistedPass-residual` plus that bullet's ordinal, routed to `TOOL.md` or `DEPL.md` by the carrier it
  names.
- **S4** — File one further backlog row for the tracked non-memory carriers that state the superseded
  verdict in the present tense, naming every one and what each owes. **The population is DERIVED, never
  typed:** `git grep -ln "parallelism route: none" -- tools/` returns FIVE at BASE `e828f778`. This unit
  does not edit them (§3).
- **S5** — Regenerate the memory tree's derived artifacts in the SAME commit as S1–S4, because the ids
  minted by those rows change this build's generated roster (§4).

## 3. Non-goals (OUT)

- **The live carriers are not edited here, and there are FIVE of them, not four.** Re-derived at BASE
  `e828f778` with `git grep -n "parallelism route: none" -- tools/`, which is the command S4 runs rather
  than a count carried in prose: `tools/hooks/README.md:63`, `tools/hooks/agent-cap.js:444`,
  `tools/hooks/agent-cap.test.sh:328`, `tools/workflows/unattended-build.js:64` and `:333`, and
  `tools/workflows/unattended-build.test.sh:187`, `:194` and `:421` — eight sites across five files.
  rev-1 through rev-3 said four, and cited `agent-cap.js:412`, `agent-cap.test.sh:177` and
  `unattended-build.js:34-37`, which were exact at `c4fcf5ad` and name unrelated prose at BASE. The
  fifth file is the one the count missed rather than the one the addresses moved: its `:194` asserts in
  the present tense that E3 and E4 "failed", the exact claim `TOOL-dUnstalledConvoy-7` overturned by
  RUNNING them. Correcting the set makes a records unit edit three files of the `agent-cap` kit and two
  of `review-harness`; `tools/hooks/agent-cap.js` is a governance carrier, so M3 veto 2
  (`memory/guides/BUILD-METHOD.md:84`) makes the unit an owner turn, and each edited kit owes a version
  bump. **S4's row carries all five, and NO unit of this build takes any of them — including the
  `unattended-build.js` one.**

  That last clause is a correction, not a restatement. rev-1 said "the design's U5 already opens
  `unattended-build.js` and is the cheapest home for that one", U5 in the design's section 7 table is
  `TOOL-aHoistedPass-6`, and that spec's own section 3 disclaims the same edit on the ground that
  "`TOOL-aHoistedPass-1` at `order 1` owns that correction by name" — which is false against this
  text. The two specs disclaimed to each other and the edit fell between them, which nothing on the
  bar would have caught: no leg grades whether a decision row's quotation is still true. **The
  residual is now FILED rather than assumed handled**, which is the whole point of S4 and is the
  weaker but honest half of this unit's goal.
- **`memory/DECISIONS.md:65` is not rewritten, softened or annotated.** Supersession is a new id and a
  note (§6 of the charter).
- **`TOOL-cBriefedPilot-28` is not CLOSED.** Its R3 and R1 clauses are unmeasured, and closing the row
  would discard them along with the false one.
- **`memory/backlog/TOOL.md` is not rotated or split**, though this unit adds rows to a shard already
  over cap. Its `memory/project/curation-debt.txt` entry already records that the drain is rotation and
  that nobody has performed it; a second record of the same fact is not an improvement.
- **Nothing about parallelism is re-decided or built.** The cleared verdict is recorded, not acted on.
- **Recipe mode is not decided** — that is the design's U8, a measurement.

## 4. Design

### Inventory

Everything below was re-opened at `c4fcf5ad` in this worktree. `<the design record>` below is **the
path in this spec's own `gen:spec-records` table at the top of this file** — today
`memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md`.

**It is defined by pointing at that generated row rather than by retyping the filename, and rev-2
learned why the hard way.** rev-1 bound the token to
`…/2026-09-04-build-aHoistedPass-1-design-pass.md`, a name that has never been tracked in this
repository — the record was added under its real name in `fa273fc7`. The token is the operand of a
derivation this spec runs twice (the residual count in the table below, and AC3 at landing), so a
missing operand makes the `awk` emit nothing, `grep -c` print `0`, and AC3 compare a real backlog
count against zero. The generated table cannot go stale and a hand-typed second copy can; that is the
charter's derive-over-author rule applied to a spec. **Re-derived at BASE `e828f778` against the real
record: the count is 28, unchanged, so only the path was wrong and every figure below stands.**

| fact | where | state at this base |
|---|---|---|
| the standing verdict | `memory/DECISIONS.md:65` | `TOOL-cBriefedPilot-21 · parallelism route: none` |
| any trace of the clearance in the index | `git grep dUnstalledConvoy -- memory/DECISIONS.md` | zero hits, and zero in the rotated archive |
| what actually cleared it | `memory/builds/dUnstalledConvoy/build/2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md:5` | `parallelism route: cleared` |
| the two specs behind it | `.../spec/2026-08-20-spec-TOOL-dUnstalledConvoy-7.md`, `...-8.md` | both `CLOSED`, `ratified 2026-08-20` |
| the shipped consequence | `memory/guides/BUILD-METHOD.md:184` | "Parallelism is REQUIRED where disjointness is PROVEN" |
| the stale backlog row | `TOOL-cBriefedPilot-28` in `memory/backlog/TOOL.md` — by id, because rows move and ids do not | `OPEN`, 199 chars, says E3 and E4 "never were" run |
| residual bullets to file | `awk '/^## §10/{f=1} /^## Appendix/{f=0} f' <the design record> \| grep -c '^- '` | 28 — 21 above the adopter-block paragraph, 7 below it |

The clearance is not a re-argument of the same evidence. `TOOL-cBriefedPilot-21` rejected R2 because E3
and E4 FAILED; its own record marked them NOT OBSERVED, which is unmeasured evidence rather than adverse
evidence. `TOOL-dUnstalledConvoy-7` ran both, with the losing conditions committed before the tests and
a control that reproduced the row-driver conflict when M6's condition 3 is violated. R1, R3 and R4 stay
rejected on the prior hunt's own adverse tests, so the supersession is scoped to R2+R5 and says so.

### Data model

Three row shapes. All three obey `- <id> · <STATUS> · <text>`, the status vocabulary of seven tokens,
and `ENTRY_CAP_CHARS` = 300 (`tools/memory-tree/check-memory-hygiene.sh:73`).

```
- TOOL-aHoistedPass-<n> · supersedes TOOL-cBriefedPilot-21 for R2+R5: E3 and E4 were UNMEASURED, not
  adverse. TOOL-dUnstalledConvoy-7 ran both, losing conditions written first, and recorded
  `parallelism route: cleared`; M6 now reads parallel-on-proof. R1/R3/R4 stay rejected
```

That is the DECISIONS row, and it is one physical line when written. The backlog residual rows take:

```
- TOOL-aHoistedPass-<n> · OPEN · <the residual, in one sentence, with what holds it today> —
  aHoistedPass-residual <k>
```

`<k>` is the bullet's ordinal in the design record's §10, in document order, so a reader can map a row
back to the paragraph it came from and a missing or duplicated ordinal is visible. The count is derived
at build time from that record, never typed into a row.

A residual that names no remedy anyone intends to take takes `WONTDO` rather than `OPEN` — the design
says of several of them that the run holds it and nothing else does, and a row that can never close is
not an open item. The token is the disposition; the sentence carries the reason either way.

### The two couplings this unit must not trip

**Minting ids changes this build's generated roster.** `gen_build_index.py`'s `rosters()` scans every
tracked file under the memory root except `LIVE.md`, `ledger/` and the build's own README, and derives
each build's `ids:` field from the ids it finds; the module's own header states that `ids` is an OUTPUT
and that `--write` overwrites whatever was authored there. So a new `TOOL-aHoistedPass-<n>` in a backlog
shard changes `memory/builds/aHoistedPass/README.md`, and hygiene check 9 runs `--check` on every bar.
S5 exists for this and nothing else.

**A rooted `path:line` citation inside backticks is a dead-path finding in these two files.** Check 15
grades backticked tokens in the present-tense corpus, which includes `DECISIONS.md` and `backlog/`, and
`tools/workflows/unattended-build.js:37` resolves to nothing. The corpus already writes it the other
way: `memory/backlog/DEPL.md` cites `govkit.py:2011` and `check-kit-versions.sh:84` — basenames, no
slash, and a token with no `/` is skipped before the resolution test. New rows cite a line as a bare
basename, or a path with no line suffix. This spec is under `builds/`, which the present-tense selector
excludes, so its own citations are unconstrained.

### What holds each half of this, honestly

- The row SHAPES are held by `memory hygiene` — checks 7 and 8 — on `memory/backlog/DEPL.md` and
  `memory/DECISIONS.md` only. `memory/backlog/TOOL.md` is listed in `memory/project/curation-debt.txt`,
  which its own header says silences checks 6, 7 AND 8 on that file. Twenty-one of these rows therefore
  land where the gate is off, and their cap and status token are held by the run and by AC4.
- The ID set is held by check 14: a backlog row's `- <id> ·` is an anchor that DEFINES its id, stated in
  the checker's own fixture comment at `tools/memory-tree/corpus_ids.py:744-746`, so these rows cannot
  orphan themselves. The reverse is why this spec names no id it has not minted: an id cited in a spec
  and defined nowhere is exactly check 14's finding.
- The REGENERATION is held by check 9 and by the `build README slot contract` leg.
- **Nothing anywhere grades that a residual has a row, that a decision row's text is true, or that a
  superseded row is reachable from the row that superseded it.** There is no such reader in this tree
  and this unit does not add one. The run holds all three, and AC3 is an observation made once, at
  landing, not a standing check.

### Files touched (estimate)

`memory/DECISIONS.md` (+1 line) · `memory/backlog/TOOL.md` (1 line rewritten, ~22 added) ·
`memory/backlog/DEPL.md` (~7 added) · `memory/builds/aHoistedPass/README.md`, `memory/LIVE.md` and
`memory/ledger/2026-09.md` (regenerated, not authored). No file outside `memory/`.

### Alternatives rejected

- **Annotating `TOOL-cBriefedPilot-28` instead of rewriting its text.** `TOOL-dUnstalledConvoy-17` is
  the recorded precedent and it went the other way, in its own words: a corrected row that still carries
  its false sentence is a second copy of the claim it was corrected to remove, and git holds the
  original. The backlog is the mutable record; only `DECISIONS.md` is append-only.
- **Grouping the 28 residuals into a handful of themed rows.** A grouped row cannot be closed when one
  of its members is, and the ordinal-to-row map is the only thing that makes coverage observable.
- **Leaving the residuals in the design record alone.** The build folder is UNTRACKED at this base
  (`git ls-files memory/builds/aHoistedPass/` is empty), so today they live in a working tree; once it
  is committed they live in a build record, which goes terminal with the build and which nobody sweeping
  for open work reads.
- **Citing `TOOL-cBriefedPilot-28` by line number.** `dBriefedPass`'s round-1 spec audit cites it at
  `memory/backlog/TOOL.md:131` and it is at 137 today. Rows move; ids do not.

## 5. Production-readiness checklist

- security — N/A. No code, no write path, no surface. No credential or instance-specific content enters
  these rows.
- perf / scale — N/A for the rows themselves; the regeneration in S5 is the same `--write` every records
  commit already runs.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — N/A. No runtime.
- observability — the shared `aHoistedPass-residual` token IS the observability: it makes the row set
  countable and mappable back to the design record by one grep.
- risks — one, and it is bounded: every row routed to `memory/backlog/TOOL.md` lands in a shard whose
  cap checks are silenced by `curation-debt.txt`, so a malformed row there is invisible to the bar,
  and the rows also widen a debt whose drain is rotation. Mitigated by AC4, which makes
  the observation by hand. A second, smaller one: forgetting S5 reds the next bar rather than corrupting
  anything, and AC5 stages that red deliberately.
- testing + left-shift gates — no new gate. This unit's whole product is state that existing legs
  already grade for shape; the class it left-shifts is a stale record, which nothing static can detect.
- migration / rollback — a single revert of one commit restores every file, including the regenerated
  artifacts. No schema, no cutoff, no flag.
- user docs — N/A. `help/` covers user-facing features; this is an internal record.

## 6. Acceptance criteria

- **AC1** — When the supersession lands, `git grep -c dUnstalledConvoy -- memory/DECISIONS.md` returns a
  non-zero count and the new row names both `TOOL-cBriefedPilot-21` and `TOOL-dUnstalledConvoy-7`.
- **AC2** — When `git diff --numstat <base> -- memory/DECISIONS.md` is read, the deletion column is `0`:
  the append-only log gained a row and lost none, and line 65 is byte-identical.
- **AC3** — When the residual rows land, `git grep -h "aHoistedPass-residual" -- memory/backlog/ | wc -l`
  equals the bullet count derived by `grep -c '^- '` over the design record's §10 slice, and the ordinals
  those rows carry are that range with no gap and no repeat.
- **AC4** — When `awk 'length > 300' memory/backlog/TOOL.md memory/backlog/DEPL.md` is run over the added
  rows, it prints none of them, and each new row's second field is one token of the seven-token status
  vocabulary. Stated as a hand observation because `curation-debt.txt` silences check 7 and check 8 on
  `TOOL.md`, so a green bar does not make it.
- **AC5** — When the rows are committed WITHOUT rerunning the generator,
  `python tools/memory-tree/gen_build_index.py --check` exits non-zero naming
  `memory/builds/aHoistedPass/README.md`; when `--write` is rerun and the regenerated files are included,
  it exits 0. The failing half is staged and observed before landing — it is what proves the roster
  coupling in §4 is real rather than argued.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the landed tree, it exits 0,
  with check 14 clean: no id this unit cites is left undefined, and no id it mints is cited before its
  row exists.
- **AC7** — When the S4 row is read, it names every file
  `git grep -ln "parallelism route: none" -- tools/` returns — `agent-cap.js`, the hooks `README.md`,
  `agent-cap.test.sh`, `unattended-build.js` and `unattended-build.test.sh`, five at BASE — and says
  which owes a version bump and which is governance-carrier work under veto 2. The criterion asserts
  the row equals the command's output, so a later carrier cannot fall silently outside the population.
- **AC8** — When `grep -c "they never were" memory/backlog/TOOL.md` is run after S2, it returns `0`, and
  `grep -n "TOOL-cBriefedPilot-28" memory/backlog/TOOL.md` still returns exactly one row, still `OPEN`.

## 7. Gates

- **`memory hygiene`** (chunk `records`, subject `repo`, no guard) — runs on every bar. It carries the
  checks that grade this unit's output: 7 and 8 for the row shapes where they are not silenced, 9 for the
  regenerated artifacts, 13 and 14 for the ids, 15 for the path citations.
- **`build README slot contract`** (`gen_build_index.py --check-format`, chunk `records`, subject `repo`,
  no guard) — the README is **already tracked and already contract-BOUND at BASE `e828f778`**, with a
  bare-path row at `memory/project/readme-contract.txt:123` and `--survey` reporting it conforms, so
  this leg simply stays green and this unit mints no registry row. rev-1 said this commit would be the
  first to track that README and routed the question to §8's F1; rev-2 resolved F1 as MOOT on exactly
  this evidence and left this bullet standing — the amendment class, in this spec, one section away
  from where it was fixed. The leg's chunk, subject and guard are unchanged and the obligation was
  never in doubt; what was stale was the reason given for it.
- No new gate leg, and no existing leg is moved, scoped or waived.

## 8. Open questions

- **F1 — `memory/project/readme-contract.txt` has no row for `aHoistedPass`, and this unit's commit is
  the first that tracks the build folder.** The registry is asserted in both directions by
  `gen_build_index.py --check-format`: a tracked build README named by no row is a refusal. A BOUND row
  (bare path) binds the five-heading canon and the slot budgets and leaves `exempt-pin: 67` untouched; an
  EXEMPT row (`!` prefix, reason on the line) needs the pin raised to 68 in the same commit.
  **Recommendation:** run `python tools/memory-tree/gen_build_index.py --survey`, which grades the canon
  over every README and never fails, and take the BOUND row if this README passes it — the exemption
  block in that registry is for terminal builds, and this one is opening. If the survey objects, take the
  exempt row with the objection as its reason and raise the pin, rather than editing a README this unit
  does not own. Either way it is one line, and it belongs to whichever commit first tracks the folder,
  which at `order 1` is this one.

RESOLVED (agent, 2026-09-05, delegated): **F1 is MOOT — the BOUND row already exists.** Re-derived at the run's BASE
`e828f778`, 66 commits after the base this spec was written against:
`memory/project/readme-contract.txt:123` already carries the bare path
`memory/builds/aHoistedPass/README.md`, and `python tools/memory-tree/gen_build_index.py --survey`
reports `BOUND memory/builds/aHoistedPass/README.md - conforms`. So the fork's premise — that the
registry has no row for this build — is false at BASE. **No row is minted and `exempt-pin: 67` is
untouched**, which is the BOUND branch the recommendation asked for, reached by observation rather
than by a pick.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against the design record at `c4fcf5ad` with four
  corrections to it. **(1)** Its U1 acceptance demands that `git grep -n "parallelism route: none"`
  outside `memory/{builds,archive}` return only citations naming the supersession; four tracked carriers
  under `tools/` state it, three of them in the `agent-cap` kit, so meeting that condition makes U1 an
  owner turn under M3 veto 2 and contradicts the same table's "owner-gated: no". Cut to §3 and routed to
  an S4 row. **(2)** Its U1 line and edit-set omit the roster coupling: minting ids in a backlog shard
  rewrites this build's generated `ids:` field, so the regeneration is in scope as S5 and its red is
  staged as AC5. **(3)** They also omit the citation grammar — a rooted `path:line` in backticks is a
  check 15 finding inside `DECISIONS.md` and `backlog/`, which is where every row this unit writes goes.
  **(4)** Counts re-derived here rather than carried: the §10 residual bullets are 28, split 21 and 7
  across the adopter-block paragraph; `memory/backlog/TOOL.md:137` and `memory/DECISIONS.md:65` both
  verified at this base, against `dBriefedPass`'s round-1 audit which cites the backlog row at `:131`.
- rev-2 - 2026-09-05 - M3 fork sweep under the standing mandate. F1 marked RESOLVED as MOOT:
  the readme-contract row this fork was to mint landed between `c4fcf5ad` and the run's BASE
  `e828f778`. S1 and S2's premises were re-verified at BASE and both HOLD — `memory/DECISIONS.md:65`
  still states `parallelism route: none` and `memory/backlog/TOOL.md:138` still says E3 and E4 "never
  were" run, so the line numbers this spec cites are exact at BASE for S1 and one line off for S2
  (`:138`, not `:137`).
- rev-3 - 2026-09-05 - folded round-1 spec-audit findings 35, 23, 17 and 27. **35 and 23** are one
  defect seen by two lenses: section 4 bound `<the design record>` to a filename that has never been
  tracked, and that token is the operand of the residual derivation AND of AC3. The token is now
  defined by POINTING at this spec's generated `gen:spec-records` row instead of retyping a path, and
  the derivation was re-run at BASE against the real record - 28 bullets, 21 above the adopter-block
  paragraph and 7 below, all unchanged. Only the path was wrong. **17** - section 3 routed the
  `unattended-build.js:34-37` correction to the design's U5, which is `TOOL-aHoistedPass-6`, whose own
  section 3 routes it back here by name. Two specs disclaiming to each other left the cheapest of the
  four carriers owned by nobody, and nothing on the bar grades a decision row's truth, so it would
  have closed green. Section 3 now states that S4's row carries all four and that no unit of this
  build takes any of them - the residual is FILED rather than assumed handled. **27** - section 7's
  build-README bullet still argued from "this unit's commit is the first to track the README", which
  rev-2's own F1-is-MOOT resolution had already disproved one section away. Rewritten to the BASE
  fact: tracked, contract-BOUND at `readme-contract.txt:123`, leg stays green, no registry row minted.
  Section 4's rejected alternative keeps its "UNTRACKED at this base" clause, which is explicitly
  qualified to `c4fcf5ad` and is true there; the review refuted that half of the finding and it is
  left standing as the model for how the other half should have been written.

- rev-4 - 2026-09-05 - **built-pass correction, folding round-2 findings M7, M6 and L1**, all three in
  S4's neighbourhood and all three surfaced again by the `amendment-leaves-its-other-half-standing`
  class the post-commit checklist selected over this unit's own diff. **M7 is the substantive one and
  it is a MEASUREMENT error, not staleness:** `git grep -ln "parallelism route: none" -- tools/`
  returns FIVE files at BASE and returned five at `c4fcf5ad` too, so "the four tracked non-memory
  carriers" was wrong when it was written. The missed file is
  `tools/workflows/unattended-build.test.sh`, whose `:194` asserts in the present tense that E3 and E4
  failed - the exact claim this unit's S1 records as overturned - and which carries three sites, with
  `unattended-build.js` carrying two, for eight sites across five files. S4 and AC7 now DERIVE the
  population by command instead of naming a count, which is section 7's "no count of a derived
  population is written in prose" applied to a spec. **M6** - three of section 3's four addresses were
  `c4fcf5ad` addresses naming unrelated prose at BASE; all are re-derived and the two extra sites
  added. **L1** - section 4's inventory cited the amended backlog row at `:137` while this spec's own
  rev-2 log and its own rejected-alternative both say to cite it by id; it now does. The S4 backlog row
  was rewritten in the same commit to match, so the spec and the artifact do not disagree.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "append a superseding decision row and amend a backlog
row"`, run in this worktree at this base. It reports a corpus of 645 symbols, 188 inventory keys, 19
affordance seams and 20 dossiers, and its ranked shortlist returns only READERS of these two row
documents — `append_backlog` in `tools/codebase-map/map_lib.py` at fan-in 2, `row_docs` in
`tools/memory-tree/row_grammar.py`, `resolve_rows` and `no_row_loss` in `tools/memory-tree/merge-rows.py`,
`read_contract_rows` in `tools/memory-tree/gen_build_index.py`, and the `row-grammar selftest` and
`row-keyed merge driver replay` legs. **No existing seam fits, and none should:** this unit adds no code
and extends nothing. It writes three rows by hand into two documents whose grammar those readers already
grade, and the only seam it must respect is that grammar — which is why §4 states the entry cap, the
status vocabulary, the anchor form and the citation shape rather than a call site.

Recall terms used: parallelism route cleared verdict supersede decision-index backlog residual
append-only ratified dUnstalledConvoy cBriefedPilot roster
