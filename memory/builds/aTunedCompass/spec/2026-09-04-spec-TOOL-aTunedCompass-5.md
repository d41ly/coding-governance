# TOOL-aTunedCompass-5 — `DURABLE` matches a flat memory root, so `spine` stops being empty

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the recall kit's `spine` document set non-empty in a repo whose memory tree is flat, so the
kit's definition-home layer exists at all. Today `tools/memory-recall/extract.py`'s `DURABLE`
pattern matches nothing here, and it matches nothing in any tree the sibling memory-tree kit's own
adopter creates, so the layer is silently dead for this repo and for every adopter of both kits.

## 2. Scope (IN)

- **S1** — `DURABLE` matches the FLAT layout and keeps matching the nested one. The single
  directory segment between the memory root and the index file becomes optional, and an index file
  named for an id family is admitted alongside `DECISIONS` and `BACKLOG`. Both layouts, one
  pattern; nothing that matches today stops matching.
- **S2** — the family alternation is DERIVED from `CONF.families`, never typed as a literal list.
  The conf already declares `MEMORY_ROOT` and `FAMILIES`, and an adopter's families are its own.
  A literal would be this repo's four prefixes shipped into every adopter's kit.
- **S3** — an empty `spine` beside a non-empty `records` announces itself on stderr, naming
  `DURABLE`, the resolved `MEMORY_ROOT`, and the index paths the pattern looked for. This is the
  state that was silent for a month, and the charter's own rule is that a probe which cannot move
  says so rather than reporting a reassuring zero.
- **S4** — arms in `tools/memory-recall/selftest.py` covering both layouts: a flat fixture and a
  nested fixture each produce at least one `spine` document, and the compiled pattern changes when
  the stub conf's `FAMILIES` changes. Each arm's red is observed before the arm is written.
- **S5** — `tools/memory-recall/test_recall_floor.py`'s empty-graded-set arm stops using `spine` as
  its empty set. That arm currently DEPENDS on this defect, so the fix reds it; the replacement
  empties a set synthetically through `build_filtered` and still exercises the same branch of
  `tools/memory-recall/check-recall.py`.
- **S6** — the two prose claims that go stale in the same commit are corrected in the same commit:
  the document-set gloss in `tools/memory-recall/extract.py`'s module docstring, and the
  parenthetical in `tools/memory-recall/check-recall.py` (`:33`) saying `spine` extracts to zero
  docs in this repo today.
- **S7** — `KIT_MEMORY_RECALL_VERSION` moves. The kit version is the marker `tools/check-kit-versions.sh`
  grades, and it is also in the cache digest blob, so a warm cache built before this change is not
  read after it. The cost is one rebuild, which the digest docstring already priced for exactly this
  class of edit.

## 3. Non-goals (OUT)

- Not changing this repo's memory layout. The memory-tree kit's adopter WRITES the flat layout at
  `tools/memory-tree/adopt-memory-tree.sh` (`:125`, `:259`), so the flat tree is the shipped shape
  and the recall kit's pattern is the side that is wrong.
- Not pinning a floor over `spine`. `RECALL_FLOOR` stays where it is. What the recall floor grades
  is `TOOL-aTunedCompass-3`, and pinning a set that was empty until this unit would be a pin set
  from a number nobody has measured on a fixture.
- Not tuning retrieval with `spine`. This unit makes `python tools/memory-recall/bench.py --sets spine`
  able to run. Whether the layer is worth using is a later question with its own measurement.
- Not touching `records` or `chunks`. `spine` is a filter over `records`, and this unit changes only
  the filter.
- Not the orphan-id gap. That 211-id finding is a memory-tree hygiene question and carries its own
  backlog row.

## 4. Design

### The two layouts, and what the shipped pattern sees

| Index file | Layout | Shipped `DURABLE` |
|---|---|---|
| `<MEMORY_ROOT>/<dir>/DECISIONS.md` | nested, upstream's | matches |
| `<MEMORY_ROOT>/<dir>/decisions/<file>.md` | nested, upstream's | matches |
| `memory/DECISIONS.md` | flat, this repo's | no match |
| `memory/backlog/<FAMILY>.md` | flat, this repo's | no match |
| `memory/archive/<FAMILY>.<date>.md` | flat, this repo's | no match |

Two independent reasons for the miss. The directory segment between the root and the index is
mandatory in all three alternations, and the flat decision log has none. And the flat backlog shard
is named for its id family rather than `BACKLOG`, which no alternation admits.

### The derivation

The pattern is built from the two conf values the kit already resolves, so nothing new is declared
and there is no second place for the answer to be wrong. The index alternation is
`DECISIONS|BACKLOG` joined with `CONF.families`, and the directory segment becomes optional in each
of the three arms. `_ROOT` is already `re.escape(CONF.memory_root)` at
`tools/memory-recall/extract.py` (`:130`), which is the same idea applied to the root a release
earlier.

### The candidate predicate, run over the real tree before it is wired

§7 of the charter asks for this before a predicate is wired, and it changes what the unit claims.
Measured on this worktree at BASE, over the 1240 tracked Markdown files under the memory root:

| Predicate | Files matched | Near-misses |
|---|---|---|
| shipped `DURABLE` | 0 | 0 |
| candidate | 9 | 0 |

The nine are `memory/DECISIONS.md`, the four `memory/backlog/<FAMILY>.md` shards, and the four
rotated indexes under `memory/archive/`. No file with an index-shaped basename is left out, and
nothing else is pulled in. The optional segment admits at most two path components below the root,
so a build folder or a map dossier cannot reach the set.

Running the extractor and applying the candidate to its `records.jsonl` gives what the layer would
actually hold:

| Figure | Shipped | Candidate |
|---|---|---|
| `spine` documents | 0 | 748 |
| `spine` indexed chars | 0 | 368183 |
| anchored ids with a durable home | 0 | 626 of 696 |

The zero is the parent report's finding 4 and is cited, not re-derived. The candidate column is new
and was measured here, because the report priced the defect and never priced the fix.

### What those numbers do to the claim

`spine` would be 748 of 925 records, or 81%. That is not the small high-precision layer the
upstream figures describe, and the reason is this corpus rather than the pattern: 405 of the 748 are
backlog rows, and the tooling shard alone is 261 KB of essay-length rows. So the honest statement of
what this unit buys is that the definition-home concept gains a representation in retrieval and the
layer becomes runnable, NOT that a high-precision layer arrives. Whether backlog rows belong in it
is F1.

### The announcement

`zero_record_diagnosis` at `tools/memory-recall/extract.py` (`:372`) is the existing shape for this
and the new signal follows it rather than inventing a second one. Its reasoning transfers with one
difference worth stating. Zero records can be the honest state of a tree that has written no
decision yet, which is why that function prints rather than refuses. Zero `spine` beside non-zero
`records` has no honest reading at all: records exist, so the corpus and the id grammar both work,
and the only remaining cause is that `DURABLE` describes a layout this tree does not have.

### The collateral, because one arm depends on the defect

`tools/memory-recall/test_recall_floor.py` (`:258`) pins a floor over `spine` and asserts the
refusal, and its return string says spine extracts to zero docs. That arm passes today BECAUSE of
the defect, so this unit reds it. It is a genuine arm over a real branch of `check-recall.py`
(`:185`) and must survive; S5 keeps the branch and drops the dependence on a live bug.

### Files touched (estimate)

`tools/memory-recall/extract.py`, `tools/memory-recall/recall_conf.py` for the version marker,
`tools/memory-recall/selftest.py`, `tools/memory-recall/test_recall_floor.py`, one comment line
in `tools/memory-recall/check-recall.py`, and `memory/map/features/memory-recall.md` for the dossier
refresh §5 owes. Six files.

### Alternatives rejected

A conf-declared list of durable homes, on the model of `RECALL_EXTRA_SOURCES`, was rejected. That
key exists because the corpus root cannot imply which files OUTSIDE it belong to the corpus, which
is a fact no other declaration carries. Durable homes are different: `MEMORY_ROOT` and `FAMILIES`
already determine them, so a third key would be a second place to state a derivable fact and a
second place for an adopter to get it wrong. It would also need a digest-blob entry and a
refusal path of its own.

Fixing this repo's layout instead of the pattern was rejected on the same evidence as §3's first
bullet. The kit that owns memory layout ships the flat one.

## 5. Production-readiness checklist

- security — N/A. The change is a path predicate over already-tracked files, and it widens which
  of them are indexed into a local data dir. No new read surface and no new write path.
- perf / scale — one more filter pass over `records`, already performed. The `spine.jsonl` write
  grows from empty to roughly 368 KB on this corpus, which is a fraction of the chunk dump.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — S3 is exactly this line. The empty state is the one that was
  silent, and it is the state the unit makes loud.
- observability — the extractor already prints per-set doc counts and the durable-home tally, so the
  fix is visible in the output that reported the defect.
- risks — a widened predicate over-matching is the real one, and it is answered by the near-miss
  scan in §4 rather than by argument. Rollback is a one-line revert of the pattern.
- testing + left-shift gates — S4's arms, plus S5's repair of the arm that depended on the defect.
  The class is "a pattern that resolves to nothing reports success", and S3 is the gateable form of
  it.
- migration / rollback — no data migration. A stale warm cache is handled by the version bump in S7.
- user docs — the kit README states what the three document sets are; refresh it on touch. The
  `memory-recall` dossier under `memory/map/features/` is refreshed in the same commit per the DoD.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/extract.py . <dir>` runs on this repo, the `spine` row
  reports a non-zero document count and `ids anchored` reports a non-zero `durable home:` figure.
  The same command at BASE prints `spine 0 docs`, which is the before half of the observation.
- **AC2** — When the candidate predicate is run standalone over `git ls-files -- memory` before it
  is wired, it matches the nine index files and nothing else, and the near-miss list of
  index-shaped basenames it does not match is empty.
- **AC3** — When the arm in `tools/memory-recall/selftest.py` builds a NESTED fixture holding
  `<MEMORY_ROOT>/<dir>/DECISIONS.md`, that fixture still yields at least one `spine` document, so the
  widening does not trade one layout for the other.
- **AC4** — When that arm's stub conf declares a different `FAMILIES` value, the compiled
  `DURABLE.pattern` changes with it, which is the observation that the alternation is derived rather
  than typed.
- **AC5** — When `records` is non-empty and `spine` is empty, `tools/memory-recall/extract.py`
  writes a diagnosis to stderr naming `DURABLE` and the resolved `MEMORY_ROOT`. The arm observes
  that message RED against the shipped extractor before the pattern fix lands, so the signal is
  known to fire.
- **AC6** — When `python tools/memory-recall/test_recall_floor.py` runs after the change, it is
  green, its empty-graded-set arm no longer names `spine`, and it still reaches the `is EMPTY`
  branch of `tools/memory-recall/check-recall.py`.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it is green with
  `KIT_MEMORY_RECALL_VERSION` moved.

## 7. Gates

The legs this unit must keep green when it is built, by their `tools/gate-legs.json` names:
`memory-recall kit selftest`, `recall floor`, `recall floor arms`, `memory-recall skill wiring`,
`kit version markers`, `codebase-map coverage + freshness` because the dossier prose is refreshed on
touch, and `row-keyed merge driver replay`, whose guard names this kit's directory.
The full bar is `bash tools/run-gates/run-gates.sh`. `memory-recall kit selftest`, `recall floor
arms` and `row-keyed merge driver replay` are all `chunk = selftests`, so an ordinary bar does not
run them and this unit's Definition of Done owes them under `GATE_SELFTESTS=1`, which is what the
charter requires of kit work. This unit adds no new leg; it adds arms to two suites that are already
legs.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): admit backlog shards, keeping upstream parity.** The owner took this
fork's recommendation and its stated cost with it. On this corpus `spine` becomes 81% of `records`,
405 of 748 documents, so the layer is not a precision layer today and no session should tune against
it as though it were. Re-pricing it waits until it can be measured at all, which is only possible
once it is non-empty.

**F2 RESOLVED (owner, 2026-09-05): print on stderr and exit 0.** Not a refusal. The reasoning the owner
accepted is this fork's own: the defect was invisible because nothing SAID anything, not because
nothing refused, so a print closes it and a refusal would block an adopter mid-migration whose repo
was working a minute earlier. The print matches `zero_record_diagnosis` exactly.

- **F1 — do backlog shards belong in `spine`?** Upstream's `DURABLE` admits `BACKLOG.md` by design,
  and a backlog row genuinely is a record's definition home. On this corpus that decision is what
  makes `spine` 81% of `records`: 405 of the 748 documents are backlog rows, and the tooling shard
  is 261 KB of rows that the parent report measured at a mean of 780 bytes each.
  Options: admit them, for upstream parity and because the semantics are right; exclude them, so
  `spine` is decisions and rotations only and stays a small layer; make the choice a conf value.
  Recommendation: admit them and keep upstream parity, then re-price the layer once it can be
  measured at all. Excluding them is a semantic claim about what a backlog row IS, and this unit has
  no measurement that settles it. The counter-argument is real and is why this is a fork rather than
  a design note: a layer that holds most of the corpus is not a precision layer, and shipping it as
  one invites the next session to tune against it.

- **F2 — is an empty `spine` beside non-empty `records` a loud print or a refusal?** §4 argues the
  state has no honest reading, which is the case for a refusal. Against it: `extract.py` is run by
  the floor, by the selftest and by any adopter mid-migration, and a refusal turns a silent layer
  into a blocked pipeline for a repo that was working fine a minute earlier.
  Options: print on stderr and exit 0, matching `zero_record_diagnosis`; exit non-zero; print now
  and refuse in a later kit version once adopters have had a release to notice.
  Recommendation: print, matching the existing precedent exactly. The defect this unit fixes was
  invisible because nothing SAID anything, not because nothing refused, and a print closes that.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Candidate predicate and its yield measured at BASE on node a;
  every other figure cited from the parent build's findings record.
- rev-2 · 2026-09-05 · M2 cross-read. Two disagreements, both resolved here. §5 claimed the
  `memory-recall` dossier is refreshed while §4 and §7 carried neither the file nor
  `codebase-map coverage + freshness`, which `TOOL-aTunedCompass-3`, `-4` and `-8` all carry for the
  same obligation. And §7 named three `chunk = selftests` legs without the `GATE_SELFTESTS=1` clause
  that `TOOL-aTunedCompass-2`, `-3`, `-4` and `-8` each state, so a builder could report those legs
  green having never run them. Also reds `spec tokens (a spec's own names resolve)`: §4's layout
  table and AC3 backticked `memory/<dir>/…` as if it were a repo path, and the leg graded it as one.
  Both now carry the `<MEMORY_ROOT>` placeholder `memory/TEMPLATE-SPEC.md` itself uses.
- rev-3 · 2026-09-05 · both forks resolved by the owner. Backlog shards are admitted for upstream parity,
  with the 81%-of-records consequence recorded in scope; an empty `spine` prints on stderr and exits
  0 rather than refusing.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "select which corpus files are a record's durable
definition home"` ranks `corpus_files` and `zero_record_diagnosis`, both in
`tools/memory-recall/extract.py`, inside the top eleven, and both are the seams this unit extends.
`corpus_files` is the one corpus walk and is untouched, which is what confirms the change belongs in
the filter rather than in enumeration; `zero_record_diagnosis` (`:372`) is the existing shape for
S3's announcement and the unit follows it rather than adding a second diagnosis idiom. No candidate
above them is closer, and the probe's own top hit is `tracked_files` in the lexicon kit, which is a
different corpus. The pattern half has no seam beyond `DURABLE` itself, which is correct: there is
one durable-home predicate and this unit edits it.

`python tools/memory-recall/query.py "why does the recall kit treat only a nested memory layout as a
record's durable home" --terms "memory-recall extract DURABLE spine document set flat memory root
decisions backlog archive rotation adopter"` returned 40 hits. The two that bind are the port spec
for this kit, whose measured coupling inventory already lists `DURABLE` with the note that only its
ROOT comes from the conf, and the parent build's own routing line recording that whether the fix
belongs in the pattern or in this repo's layout was left open. §3 answers that routing question with
the sibling kit's adopter script.

Recall terms used: `memory-recall extract DURABLE spine document set flat memory root decisions
backlog archive rotation adopter`.
