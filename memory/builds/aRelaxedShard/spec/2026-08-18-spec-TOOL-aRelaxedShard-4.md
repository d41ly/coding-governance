# TOOL-aRelaxedShard-4 — the backlog's slope, not its ceiling

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 86eefd8f · streams tooling

## 1. Goal

`TOOL-aRelaxedShard-1` raised the row byte cap and bought about 24 days. This unit is the one the owner
sequenced after it: change the rate at which the tooling backlog grows, rather than the bound it grows
into. The measurement below says both mechanisms that unit named are the wrong shape, so this unit's
first job is to establish what the lever actually is.

## 2. Scope (IN)

- **S1** — The measurement of record: mint rate, closure rate and net live growth for the tooling
  backlog, derived from git rather than estimated, committed so a later session can re-run the
  derivation instead of re-inventing it. §4 carries today's numbers.
- **S2** — `TOOL-aRelaxedShard-1` fork F4 BUILT, because this unit cannot evaluate a spill tier without
  it. Two arms: rotating a backlog shard to `archive/` does not orphan the ids the moved rows defined,
  and a sibling fixture proving that arm can fail. The claim that it DOES orphan them is recorded in
  `memory/builds/cSteadyMetronome/README.md`, was the reason a rotation was once reverted, and reading
  `corpus_ids.py` contradicts it — a reading is not a fixture.
- **S3** — A drain signal in `tools/drift-audit/drift_signals.py`: live non-terminal rows PER backlog
  shard, against a shrink-only pin, so the live set cannot grow indefinitely without a recorded
  decision. This is the repo's native idiom and it keys on the variable that actually moves.
- **S4** — That signal's arms in `tools/drift-audit/selftest.py`, both directions: silent on a fixture
  under its pin, firing on a minimal one over it.
- **S5** — `memory/HYGIENE.md` and its kit template gain one paragraph under "Index budgets, caps,
  rotation": rotation carries forward every non-terminal row, so a shard's floor is its live set, and
  the bound that matters is therefore the live-row count rather than the byte cap. Both carriers stay in
  lockstep.

## 3. Non-goals (OUT)

- **Sharding the tooling backlog below `FAMILY`.** Measurement-rejected in §4, not deferred.
- **A spill tier.** Blocked on S2, and per §4 it relocates bytes without touching the slope. If S2 comes
  back clean it becomes a candidate for a LATER unit with its own spec, never a fold into this one.
- **Re-opening `ROW_DOC_CAP_BYTES` or `DOSSIER_CAP_BYTES`.** `TOOL-aRelaxedShard-1` set both and this
  unit does not touch check 6 at all.
- **Curating the existing 82 rows.** A sweep is work, not mechanism, and mixing the two makes the diff
  unreviewable. If the pin S3 sets is below today's count, that sweep is its own commit.
- **The other three families.** `PLAY`, `KICK` and `DEPL` hold 9, 4 and 11 rows and have no growth
  problem. The signal covers them because it is per-shard; nothing here curates them.

## 4. Design

### The measurement that decides this unit

Derived over the tooling shard and its three archives, across the nine active days the corpus covers:

| quantity | measured |
|---|---|
| ids minted | 17.3 / day |
| rows reaching a terminal status | 10.6 / day |
| **net live growth** | **+6.7 rows / day, about 1,700 B / day** |
| mean row length | 253.7 B by `wc -c` |
| shard today | 20,940 B · 82 rows · 34.1% of 61,440 |
| runway to the declared cap | about 24 days |

**Closure trails minting by roughly 40%, so the live set grows monotonically.** That one fact is what
makes both candidate mechanisms the wrong shape: a shard relocates the growth, a spill hides it, and a
larger cap postpones it. Only minting less or closing more changes the slope, and neither of those is a
file layout.

### Why sharding below FAMILY is rejected

A sub-shard needs a partition the rows actually fall into, and they do not. Measured over all 82 rows, by
which kit or area each row names:

| area | rows |
|---|---|
| `unattended` | 9 |
| `memory-tree` | 4 |
| `drift-audit` | 4 |
| `run-gates`, `playbook`, `memory-recall` | 3 each |
| `lexicon`, `hooks`, `govkit` | 2 each |
| `codebase-map` | 1 |
| **names no kit at all** | **53** |

**65% of rows would land in a catch-all shard** and the largest real cluster is 11%. Sharding here
produces one file with the same problem plus nine small ones, and splits the id space across carriers
for no gain. The measurement lives in this spec so the option cannot be re-proposed without new data.

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
| `tools/drift-audit/drift_signals.py` | the live-row signal and its per-shard pin | S3 |
| `tools/drift-audit/selftest.py` | both arms | S4 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | F4's rotation arms | S2 |
| `memory/HYGIENE.md` · `tools/memory-tree/HYGIENE.template.md` | the floor paragraph | S5 |
| `memory/builds/aRelaxedShard/` · `memory/DECISIONS.md` | records, and F4 marked resolved | S2 |

### Alternatives rejected

- **A second byte raise.** 61,440 is already 250 rows at measured width; past that a shard stops being
  scannable, which is the constraint `TOOL-aWidenedGuide-1` protected and `-1` already spent once.
- **A hard cap on live rows that REFUSES a new row.** It would block filing work in order to keep a
  record tidy, which is the failure this build hit twice from the other direction.
- **Doing nothing.** Defensible on 24 days of runway, and it is F1 below. The cost is that the next
  session rediscovers the slope by hitting it, exactly as this one did.

## 5. Production-readiness checklist

- **security** — N/A. A reporting signal over tracked text; no new input and no write path.
- **perf / scale** — One pass over the backlog shards, which drift-audit already reads. Seconds.
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
- **migration / rollback** — None. The signal is additive and reverting is one commit.
- **user docs** — S5 only. No end-user surface.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --check` runs, it prints live non-terminal row
  counts PER backlog shard against a pin, and the tooling shard's figure agrees with
  `grep -cE '^- TOOL-' memory/backlog/TOOL.md` less its terminal rows.
- **AC2** — When a fixture shard exceeds its pin, `drift_report.py --check` exits non-zero naming that
  shard, and when it sits under, the signal is silent. Both arms live in
  `python tools/drift-audit/selftest.py`.
- **AC3** — When a fixture backlog shard is rotated to `archive/` with its terminal rows moved,
  `bash tools/memory-tree/check-memory-hygiene.sh` reports NO orphaned ids, and a sibling fixture proves
  that arm can fail — so F4 is settled by observation rather than by reading `corpus_ids.py`.
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

### F1 — build this at all, on 24 days of runway?

The case FOR building now is that the slope is the actual defect, and it took a two-round audit and a
blocked landing to see it. The case for waiting is that 24 days is real and the backlog may drain on its
own as open units close.

**Recommendation: build S2 and S3 only.** S2 is owed regardless — it settles a claim two units now
depend on, and it is two arms. S3 is small and makes the slope visible. Defer any layout change until
the signal has produced data, which is the opposite of the order this build has been forced to work in.

### F2 — where the live-row pin lives, and what it is set to

Either a `drift_signals.py` constant beside the other pins, or a `.memory-tree.conf` key, which would
make it an adopter-facing declaration like the two caps `-1` added.

**Recommendation: a `drift_signals.py` constant.** Those two caps are adopter-facing because they gate a
merge; this is a drift REPORT about gov's own records, and drift-audit's pins already live there. Set it
at today's count plus about one week of measured growth — roughly 129 rows — so it fires on a trend
rather than on the next row filed.

### F3 — one pin for all families, or one per shard?

The signal is per-shard by construction, but the PIN could be a single number. `PLAY`, `KICK` and `DEPL`
hold 9, 4 and 11 rows.

**Recommendation: one pin per shard, three of them generous.** A single pin lets tooling's growth hide
inside a total, which is the aggregation mistake this repo has already fixed once in `ARMS_FLOORS`.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, authored this run and therefore unreviewed by definition. Written
  AFTER measuring rather than before: the mint-versus-closure gap and the 53-of-82 unclustered rows both
  arrived during §4, and both changed the unit's shape — they turned the two mechanisms this unit was
  sequenced for into §3 non-goals. `base` is this branch's tip rather than a default-branch sha, because
  unit 1 is built and NOT landed (the primary tree is mid-merge with unresolved conflicts) and this
  unit's design assumes unit 1's mechanism is in place.

## 10. Reuse audit

**The seam this unit extends** is `tools/drift-audit/drift_signals.py`, which already holds shrink-only
pins with their movements recorded beside them, already walks the memory tree, and already reports
per-item detail under `--json`. S3 is one more signal in that file, not a new tool. The status
vocabulary it counts against is `.memory-tree.conf`'s, read the way `row_grammar.py` reads it, so the
terminal-status set is not spelled a second time.

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
