# TOOL-aRelaxedShard-4 — the backlog's slope, not its ceiling

**Status:** CLOSED · rev-4 · 2026-08-18 · node a · Tier-2 · base 86eefd8e · streams tooling

## 1. Goal

`TOOL-aRelaxedShard-1` raised the row byte cap and bought about 18 days. This unit is the one the owner
sequenced after it: change the rate at which the tooling backlog grows, rather than the bound it grows
into. The measurement below says both mechanisms that unit named are the wrong shape, so this unit's
first job is to establish what the lever actually is.

## 2. Scope (IN)

- **S1** — The measurement of record: mint rate, closure rate and net live growth for the tooling
  backlog, derived from git rather than estimated, committed so a later session can re-run the
  derivation instead of re-inventing it. §4 carries today's numbers.
- **S2** — `TOOL-aRelaxedShard-1` fork F4 BUILT, along the axis that can actually fail. Rotating between
  two TRACKED paths under the memory root cannot orphan an id by construction, so the arm varies CORPUS
  MEMBERSHIP instead: archive staged (no orphans) against archive present-but-unstaged (the moved ids ARE
  orphans). That second state is the one under which `cSteadyMetronome`'s report reproduces, which makes
  this a settlement of F4 rather than a restatement of it.
- **S3** — A drain signal for live non-terminal rows per backlog shard. **It spans TWO files, and
  rev-2 named the wrong one.** The implementation goes in the shipped ENGINE,
  `tools/drift-audit/drift_report.py`: signal functions live there and the set is a hardcoded
  module-level `SIGNALS` list at `:697`. The project layer `tools/drift-audit/drift_signals.py` cannot
  host one — `load_project_layer()` validates it for exactly four attributes (`PRODUCT_GLOBS`,
  `SHRINK_ONLY`, `HANDKEPT`, `PINS`) and there is no registration hook. So the engine gets the function
  and the project layer gets only its pin entries.
- **S4** — That signal's arms in `tools/drift-audit/selftest.py`, both directions: silent on a fixture
  under its pin, firing on a minimal one over it.
- **S5** — `memory/HYGIENE.md` and its kit template gain ONE SENTENCE that points rather than restates:
  the section already says rotation carries forward every non-terminal row, so the addition is only that
  this makes the live-row count the bound that matters and that drift-audit reports it per shard. Both
  carriers stay in lockstep. rev-2 specified a paragraph that re-stated the carry-forward rule the same
  section already carries and defined the terminal set a second time.

## 3. Non-goals (OUT)

- **Sharding the tooling backlog below `FAMILY`.** Measurement-rejected in §4, not deferred.
- **A spill tier.** Blocked on S2, and per §4 it relocates bytes without touching the slope. If S2 comes
  back clean it becomes a candidate for a LATER unit with its own spec, never a fold into this one.
- **Re-opening `ROW_DOC_CAP_BYTES` or `DOSSIER_CAP_BYTES`.** `TOOL-aRelaxedShard-1` set both and this
  unit does not touch check 6 at all.
- **Curating the existing 82 rows.** A sweep is work, not mechanism, and mixing the two makes the diff
  unreviewable. If the pin S3 sets is below today's count, that sweep is its own commit.
- **The other three families.** `PLAY`, `KICK` and `DEPL` hold **6, 1 and 6 rows** and have no growth
  problem. The signal covers them because it is per-shard; nothing here curates them. rev-2 said 9, 4
  and 11, which were `wc -l` LINE counts read off the files and mislabelled as rows — the same
  convenient-proxy error that put a character count in unit 1's §4, one measurement later.

## 4. Design

### The measurement that decides this unit

Derived over the tooling shard and its three archives, across the nine active days the corpus covers.
**Two methods were run and they disagree, so the weaker one is named rather than dropped.** A CENSUS of
distinct ids is the figure of record. A per-commit diff scan gave 17.3 and 10.6 for a net of +6.7, and it
is the one to distrust: it double-counts rows a merge re-adds and misses rows closed by an in-place edit,
which is most of them.

| quantity | measured (census) |
|---|---|
| distinct ids ever minted | 170 |
| now terminal | 89 (88 CLOSED, 1 WONTDO) |
| still live | 81 |
| ids minted | 18.9 / day |
| rows reaching a terminal status | 9.9 / day |
| **net live growth** | **+9.0 rows / day, about 2,228 B / day** |
| mean row length | **247.6 B** by `wc -c`, measured on today's 82 rows |
| shard today | 20,940 B · 82 rows · 34.1% of 61,440 |
| runway to the declared cap | **11 to 26 days — see below** |

Two of the 170 are this build's own rows. rev-2 reported 91 terminal and 79 live, which did not
reproduce, and carried 253.7 B/row over from unit 1's 73-row measurement instead of re-measuring on the
82 rows this table describes.

**The runway is a RANGE, not a point, and rev-2 was wrong to state one.** Four methods over the same
corpus give +6.2, +6.7, +9.0 and a trailing-three-day figure that implies about 11 days. Daily net runs
from +1 to +25 and arrives in merge STEPS rather than as a slope: one day of this window consumed 15.8%
of the remaining headroom by itself. So the honest statement is 11 days at the recent rate, 26 at the
gentlest method, and the spread is itself an argument for measuring continuously rather than
re-deriving by hand — which is what S3 is for.

**Closure trails minting by about half, so the live set grows monotonically.** That one fact is what
makes both candidate mechanisms the wrong shape: a shard relocates the growth, a spill hides it, and a
larger cap postpones it. Only minting less or closing more changes the slope, and neither of those is a
file layout.

### Why sharding below FAMILY is rejected

**rev-2 rejected sharding on two grounds and only one of them was sound. This is the sound one, and it
is sufficient: a sub-shard does not change the slope.** Splitting 82 rows across ten files leaves the
same +9.0 rows/day arriving, now spread over ten carriers, plus an id space split across them and ten
files to read instead of one. Nothing about the partition changes that arithmetic.

The unsound ground is recorded here rather than deleted, because it is a measurement trap worth naming.
rev-2 counted, per row, whether the row's text SPELLED a kit's directory name:

| area | rows |
|---|---|
| `unattended` | 9 |
| `memory-tree` | 4 |
| `drift-audit` | 4 |
| `run-gates`, `playbook`, `memory-recall` | 3 each |
| `lexicon`, `hooks`, `govkit` | 2 each |
| `codebase-map` | 1 |
| **names no kit at all** | **53** |

That yields 53 rows in a catch-all and an 11% largest cluster — and it measures whether an AUTHOR HAPPENED
TO SPELL A PATH, not which area a row concerns. Re-measured by topic keywords instead, only **13 rows
(16%) match nothing** and the largest cluster is `memory-tree` at **44 rows (54%)**. A natural partition
therefore DOES exist, and the buckets overlap, so the table above is a per-kit tally and not a partition:
its rows sum to 86 over 82 because four rows name two kits.

So sharding is rejected on the slope alone. If a later unit wants to shard for READABILITY rather than
for growth, this measurement supports it and this spec does not stand in the way — what it forecloses is
sharding as a remedy for the budget.

### Why a spill tier is not this unit's answer either

The run-state file spills because its content is append-only and its oldest entries are genuinely cold.
A backlog row is neither: a two-week-old `OPEN` row is exactly as live as a new one, and the thing that
makes it spillable is closing it. Spilling live rows to a dated recording moves bytes out of the shard
and moves the reader's problem with them — the next session still has to read them to know what is open.

It is also blocked on a claim nobody has tested. `cSteadyMetronome` recorded that rotating a backlog
orphans every id the moved rows defined, which is why a rotation was once reverted; `corpus_ids.py`'s
walk has no `archive/` exclusion, and three rotations have since landed green. S2 turns that into a
fixture, because a mechanism resting on it must not rest on a reading.

### What the lever is

The variable is the gap between minting and closing, and this repo already has an idiom for a number
that must not drift upward: a shrink-only pin with its movements recorded beside it. S3 applies that to
live non-terminal rows per shard. It does not close rows — nothing mechanical can — but it makes the
growth a decision rather than a discovery, which is exactly the difference between what happened to the
byte cap in `TOOL-aRelaxedShard-1` and what should have happened.

### Files touched (estimate)

| path | change | forced by |
|---|---|---|
| `tools/drift-audit/drift_report.py` | the signal function and its `SIGNALS` entry | S3 |
| `tools/drift-audit/drift_signals.py` | the per-shard entries only — it cannot host a signal | S3 |
| `tools/drift-audit/selftest.py` | both arms | S4 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | F4's rotation arms | S2 |
| `memory/HYGIENE.md` · `tools/memory-tree/HYGIENE.template.md` | the floor paragraph | S5 |
| `memory/builds/aRelaxedShard/` · `memory/DECISIONS.md` | records, and F4 marked resolved | S2 |

### Alternatives rejected

- **A second byte raise.** 61,440 is already 250 rows at measured width; past that a shard stops being
  scannable, which is the constraint `TOOL-aWidenedGuide-1` protected and `-1` already spent once.
- **A hard cap on live rows that REFUSES a new row.** It would block filing work in order to keep a
  record tidy, which is the failure this build hit twice from the other direction.
- **Doing nothing.** Defensible on 18 days of runway, and it is F1 below. The cost is that the next
  session rediscovers the slope by hitting it, exactly as this one did.

## 5. Production-readiness checklist

- **security** — N/A. A reporting signal over tracked text; no new input and no write path.
- **perf / scale** — One new pass over the backlog shards. drift-audit does NOT read them today, so this
  is added work rather than reused work; it is a `git ls-files` slice and a line scan, still seconds.
- **a11y** — N/A. A CLI signal with no user interface.
- **i18n** — N/A, and it must stay that way: the row count is a line count over a status vocabulary, so
  nothing here may acquire a locale-sensitive comparison.
- **error / empty / loading states** — A shard with zero rows reports 0 rather than DEAD PROBE, and a
  MISSING shard must be distinguishable from an empty one.
- **observability** — The signal IS the observability, and it must print per-shard counts rather than a
  total. A total lets one shard's growth hide inside another's drain, which is the aggregation mistake
  `ARMS_FLOORS` was already split per-gate to avoid.
- **risks** — One that matters. A shrink-only pin set at today's count freezes the backlog at its
  current size, so filing a row would require closing one. The pin needs headroom and a stated movement
  rule, or S3 becomes the refusal §4's alternatives already rejected.
- **testing + left-shift gates** — S4, plus S2, which left-shifts a claim carried on reading alone since
  2026-08-14.
- **migration / rollback** — None for gov; NOT none for adopters, which rev-2 got wrong. A signal absent
  from an adopter's `PINS` falls back to a tolerance of 0, and the shipped template declares no pins, so a
  GATEABLE backlog-row signal would red every adopter's first `--check` the moment they have one open row.
  `gateable: False` per F2 removes that hazard; if a later unit gates it, the shipped template must
  declare a pin in the same change.
- **user docs** — S5 only. No end-user surface.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --check` runs, it prints live non-terminal row
  counts PER backlog shard, and the tooling shard's figure agrees with
  `grep -cE '^- TOOL-' memory/backlog/TOOL.md` less its terminal rows. Report-only per F2, so the exit
  code does not move on it.
- **AC1b** — S1's measurement is committed as a runnable derivation rather than prose: the command that
  produced §4's census lives at `build/2026-08-18-build-TOOL-aRelaxedShard-4-census.md` and re-running it
  reproduces the table at the stated base. rev-2 left S1 with no criterion and no carrier, and its figures
  have already moved twice.
- **AC2** — When a fixture shard's live count is high, `drift_report.py` REPORTS the figure and the exit
  code does not move; when the shard is empty it reports 0 rather than DEAD PROBE; and when a family has
  no shard file at all that is distinguishable from an empty one. All three arms live in
  `python tools/drift-audit/selftest.py`.
- **AC3** — F4 is settled along the axis that can actually fail: CORPUS MEMBERSHIP, not rotation. In one
  fixture the rotated archive is STAGED and `bash tools/memory-tree/check-memory-hygiene.sh` reports no
  orphaned ids; in a second the archive file exists on disk but is NOT staged, and the same command
  reports the moved ids as orphans. Rotating between two TRACKED paths under the memory root cannot
  orphan anything — check 14 is `cites` minus `defs`, a backlog row defines and cites its own id on one
  line, and 83 ids in this corpus are defined only inside `archive/` with zero orphans today. So the
  green-only arm rev-2 specified is green by arithmetic and proves nothing.
- **AC4** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, `memory/HYGIENE.md` and its
  template carry S5's floor paragraph identically.
- **AC5** — When `GATE_FULL=1 bash tools/run-gates.sh` runs at the push boundary it is green apart from
  legs already red on the default branch, and `TOOL-aRelaxedShard-1` §8 F4 reads RESOLVED with S2 as its
  witness.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `memory/` hygiene and its self-test · kit/dogfood doc
parity · testsuite counts · codebase-map coverage and freshness · the kickoff-manifest ratchet, because
S3's pin lives in a file that may join its `watch:` list.

Bug classes for these paths: `fixture-passes-by-finding-nothing` (S4 and AC3 exist for it) ·
`pin-copied-from-another-corpus` (the pin is measured here, per shard) ·
`vacuous-selector-empty-population` (a shard glob matching nothing must report, not pass) ·
`two-answers-to-one-question`.

## 8. Open questions

### F1 — build this at all · RESOLVED (owner, 2026-08-18): build it

The case FOR building now is that the slope is the actual defect, and it took a two-round audit and a
blocked landing to see it. The case for waiting is that 18 days is still real and the backlog may drain on
its own as open units close. Note that re-deriving the rate moved it from 24 days to 18 INSIDE this
unit's own authoring pass, which is itself an argument for a signal that tracks it.

**Recommendation: build S2 and S3 only.** S2 is owed regardless — it settles a claim two units now
depend on, and it is two arms. S3 is small and makes the slope visible. Defer any layout change until
the signal has produced data, which is the opposite of the order this build has been forced to work in.

### F2 — gateable or report-only · RESOLVED (agent, 2026-08-18): report-only

rev-2 asked where the pin lives and answered `drift_signals.py`, which is right for a PIN but ducked the
real question. `drift-audit records` is an UNGUARDED merge-bar leg, so a gateable signal pinned N days
ahead of today's count becomes a scheduled refusal: the day the count crosses it, every merge reds until
someone raises the pin or closes rows. That is the refusal §4's alternatives already rejected, arriving
on a timer.

The file's own precedent for a population that legitimately grows is `gateable: False` — report the
number, never block on it — and `shrink_only_lists_not_shrinking` already runs that way at
"out of tolerance (report only)".

**Recommendation: `gateable: False`, and NO forecast pin.** Report live rows per shard every run, and let
the trend be visible without arming a refusal nobody scheduled. If a later unit wants it gated, it can
pin a MEASURED value with a movement rule, which is the thing §5 says is mandatory and no rev-2 scope
item built.

### F3 — per-shard or aggregate · RESOLVED (agent, 2026-08-18): per shard, one scalar pin

The signal is per-shard by construction, but the PIN could be a single number. `PLAY`, `KICK` and `DEPL`
hold 9, 4 and 11 rows.

**Recommendation: report per shard, and if a pin is ever added make it one SCALAR key per shard.** The
ratchet guard covers SCALARS ONLY and says so: the compound floors `ARMS_FLOORS` and `CORE_FLOOR` are
excluded because they need a per-member diff. A compound per-shard pin would therefore sit OUTSIDE the
shrink-only guard and could be weakened silently — the exact failure the signal exists to prevent.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, authored this run and therefore unreviewed by definition. Written
  AFTER measuring rather than before: the mint-versus-closure gap and the 53-of-82 unclustered rows both
  arrived during §4, and both changed the unit's shape — they turned the two mechanisms this unit was
  sequenced for into §3 non-goals. `base` is this branch's tip rather than a default-branch sha, because
  unit 1 is built and NOT landed (the primary tree is mid-merge with unresolved conflicts) and this
  unit's design assumes unit 1's mechanism is in place.

- rev-2 · 2026-08-18 · re-derived the load-bearing rate by a SECOND method before handing the spec back,
  and the two disagreed. A census of distinct ids (170 ever, 91 terminal, 79 live) gives net +8.8 live
  rows/day against the diff scan's +6.7, so the runway is about 18 days rather than 24 and F2's suggested
  pin moves from 129 to 141. The diff scan is NAMED in §4 as the method to distrust rather than deleted,
  because it is the one a later session reaches for first. Nothing else moved: both §3 rejections rest on
  the GAP between the rates, which both methods agree on.

- rev-3 · 2026-08-18 · folded the M4 audit at `reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md` —
  verdict BLOCKED, 47 raw, 37 confirmed, 10 refuted, precision 0.79, 3 of 3 lenses, 19 distinct defects
  including two blockers. **B1: the signal cannot live where rev-2 put it.** Signals are functions in the
  shipped engine `drift_report.py` with a hardcoded `SIGNALS` list; the project layer is validated for four
  attributes and has no registration hook, so S3 now spans both files and names each. **B2: the
  sibling-family counts were `wc -l` output mislabelled as rows** — 6, 1 and 6, not 9, 4 and 11, the same
  convenient-proxy error as unit 1's character count one measurement earlier. The census did not reproduce
  either: 89 terminal and 81 live, closure 9.9/day, net +9.0/day, and row length re-measured on today's 82
  rows at 247.6 B rather than carried from unit 1's 73. The runway became a RANGE, 11 to 26 days across
  four methods, because daily net runs +1 to +25 in merge steps and a point estimate over that is fiction.
  §4's sharding rejection NARROWED to the ground that survives — a shard does not change the slope — after
  the audit showed the 65%-catch-all figure measured whether an author spelled a directory name: by topic,
  13 rows match nothing and the largest cluster is 54%. F2 was re-asked as the question it actually is,
  gateable or report-only, and answers report-only, because a forecast pin on an unguarded merge-bar leg is
  a scheduled refusal and this file's precedent for a growing population is `gateable: False`. AC3 moved
  onto corpus membership, the only axis where F4 can fail: 83 ids here are defined only under `archive/`
  with zero orphans, so rev-2's rotation arm was green by arithmetic. Also: base sha corrected to a
  resolvable one, §10's borrowed-vocabulary claim retracted, the adopter migration hazard stated, S1 given
  a criterion, S5 reduced from a paragraph to a pointer, and AC2 re-pointed at report-only behaviour.

- rev-4 · 2026-08-18 · BUILT and CLOSED. S1 committed the derivation as commands at
  `build/2026-08-18-build-TOOL-aRelaxedShard-4-census.md`; S2 armed F4 on corpus membership and is
  red-proved, because staging the archive fails the second arm; S3 added `signal_live_backlog_rows` to the
  ENGINE with its pin and ratchet row in the project layer, reporting 81 across 4 shards at `ok`; S4 added
  eight arms, red-proved by making the signal count entries instead of live rows; S5 added one pointing
  sentence to both HYGIENE carriers. The hygiene suite floor moved 153 to 155. F1 is the owner's; F2 and
  F3 name the AGENT as resolver, because the owner said "build unit 2" without itemising them.

## 10. Reuse audit

**The seam this unit extends** is `tools/drift-audit/drift_signals.py`, which already holds shrink-only
pins with their movements recorded beside them, already walks the memory tree, and already reports
per-item detail under `--json`. S3 is one more signal in that file, not a new tool. **The terminal-status set has to be spelled here**, and rev-2 was wrong
to say otherwise: `.memory-tree.conf` declares no status vocabulary and `row_grammar.py` reads none, so
there is nothing to borrow. The engine already hardcodes the same seven tokens for check 8; this is a
second spelling, it is unavoidable, and naming it beats the false claim that it was reused.

`python tools/codebase-map/reuse_lookup.py "count live backlog rows per shard against a pin"` and the
recall probe were both run before authoring. The recall terms, recorded so M7 can re-run them: `backlog
shard live rows terminal status rotation carry-forward shrink-only pin drift signal mint closure rate
curation sweep`. The records that bind are `TOOL-aRelaxedShard-1` (the cap it replaced and the F4 it left
open), `TOOL-cSettledDocket-16` (closed by that unit, and the row that first said new rows were being
paid for by shortening old ones), `memory/builds/cSteadyMetronome/README.md` (the rotation-orphans-ids
claim S2 settles) and `TOOL-cTracedPromise-6` (check 10's blindness to shard rotations, which any spill
tier would have to face).

**Where a hit and the source disagreed.** `cSteadyMetronome`'s claim is contradicted by `corpus_ids.py`,
whose one walk enumerates `git ls-files` with no `archive/` exclusion. This spec does not resolve that by
preferring the source: S2 builds the fixture, because two units now depend on the answer.
