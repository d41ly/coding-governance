# TOOL-aHoistedPass-1 — the record catches up with the verdicts that superseded it

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

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
- **S4** — File one further backlog row for the four tracked non-memory carriers that state the
  superseded verdict in the present tense, naming all four and what each owes. This unit does not edit
  them (§3).
- **S5** — Regenerate the memory tree's derived artifacts in the SAME commit as S1–S4, because the ids
  minted by those rows change this build's generated roster (§4).

## 3. Non-goals (OUT)

- **The four live carriers are not edited here.** `tools/hooks/agent-cap.js:412`,
  `tools/hooks/README.md:63`, `tools/hooks/agent-cap.test.sh:177` and
  `tools/workflows/unattended-build.js:34-37` all quote the superseded verdict, the last of them as a
  present-tense description of the very backlog row S2 rewrites. Correcting them makes a records unit
  edit three files of the `agent-cap` kit and one of `review-harness`; `tools/hooks/agent-cap.js` is a
  governance carrier, so M3 veto 2 (`memory/guides/BUILD-METHOD.md:84`) makes the unit an owner turn,
  and each edited kit owes a version bump. S4's row carries the work; the design's U5 already opens
  `unattended-build.js` and is the cheapest home for that one.
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

Everything below was re-opened at `c4fcf5ad` in this worktree. The design record is
`memory/builds/aHoistedPass/build/2026-09-04-build-aHoistedPass-1-design-pass.md`, and `<the design
record>` below is that path.

| fact | where | state at this base |
|---|---|---|
| the standing verdict | `memory/DECISIONS.md:65` | `TOOL-cBriefedPilot-21 · parallelism route: none` |
| any trace of the clearance in the index | `git grep dUnstalledConvoy -- memory/DECISIONS.md` | zero hits, and zero in the rotated archive |
| what actually cleared it | `memory/builds/dUnstalledConvoy/build/2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md:5` | `parallelism route: cleared` |
| the two specs behind it | `.../spec/2026-08-20-spec-TOOL-dUnstalledConvoy-7.md`, `...-8.md` | both `CLOSED`, `ratified 2026-08-20` |
| the shipped consequence | `memory/guides/BUILD-METHOD.md:184` | "Parallelism is REQUIRED where disjointness is PROVEN" |
| the stale backlog row | `memory/backlog/TOOL.md:137` | `OPEN`, 199 chars, says E3 and E4 "never were" run |
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
- **AC7** — When the S4 row is read, it names all four carriers — `agent-cap.js`, the hooks `README.md`,
  `agent-cap.test.sh` and `unattended-build.js` — and says which owes a version bump and which is
  governance-carrier work under veto 2.
- **AC8** — When `grep -c "they never were" memory/backlog/TOOL.md` is run after S2, it returns `0`, and
  `grep -n "TOOL-cBriefedPilot-28" memory/backlog/TOOL.md` still returns exactly one row, still `OPEN`.

## 7. Gates

- **`memory hygiene`** (chunk `records`, subject `repo`, no guard) — runs on every bar. It carries the
  checks that grade this unit's output: 7 and 8 for the row shapes where they are not silenced, 9 for the
  regenerated artifacts, 13 and 14 for the ids, 15 for the path citations.
- **`build README slot contract`** (`gen_build_index.py --check-format`, chunk `records`, subject `repo`,
  no guard) — this unit's commit is the first to track `memory/builds/aHoistedPass/README.md`, which is
  the fork in §8.
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
