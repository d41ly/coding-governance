# aTunedCompass — the acceptance ledger for unit 4

**Serves:** journal TOOL-aTunedCompass-4

*Node `a`, 2026-09-05, written by the unattended run that built the unit.*

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form.

## Two criteria are DEFERRED and neither is claimed

`AC4` waits on `TOOL-aTunedCompass-2`'s terms-carrying fixture and `AC5` on
`TOOL-aTunedCompass-9`'s discriminating set. Both carry a `DEFERRED` marker in §6, added at rev-3
when the round-1 audit found the unit deferring a measurement in a resolved fork while still
listing it as a criterion. This unit's order-1 Definition of Done is the other eight, and every one
of them is observed below. Nothing here claims anything about ensemble RECALL.

## Evidences

**Evidences:** TOOL-aTunedCompass-4

- AC1 — `python tools/memory-recall/query.py`, the same question served before and after, reading
  the `shown_paths` field of its own logged row: duplicate slots fall from **24 of 39** to **16 of
  40**. The claim is a total duplicate count, per S8: `shown_paths` carries no `set` label, so "at
  most once FROM THE CHUNK SOURCE" is not observable from it, and rev-2's wording could only have
  been satisfied by reading a field that does not exist.
- AC3 — `python tools/memory-recall/query.py` over **four** questions, before and after: the duplicate-path rate falls
  **0.467 → 0.369** (70 duplicate slots of 150, against 59 of 160). Recorded with the unit rather
  than quoted from the parent build's 54.5%, which is what this criterion asks for. n=4, stated
  beside the figure per the build README's rule.
- AC4 — amended rev-3 — NOT observed, and DEFERRED to `TOOL-aTunedCompass-2`. It grades the
  terms-carrying fixture that unit creates, which is order 2 and BLOCKED, so at this unit's
  declared order-1 there is nothing to run it against. rev-2 carried it as a live criterion while
  the header read `order 1`, which is the disagreement the round-1 audit found.
- AC5 — amended rev-4 — NOT observed, and DEFERRED to `TOOL-aTunedCompass-9`. The owner's F1
  resolution defers the ensemble-recall comparison until a discriminating fixture exists; rev-3
  still pointed this criterion at `recall-fixture.json`, whose lack of headroom is the very reason
  for the deferral, so it stayed unsatisfiable even after its named unblocker would land. It now
  names unit 9's set.
- AC2 — `python tools/memory-recall/selftest.py` — **44/44 checks passed**, including S7's new arm.
  Observed RED first against a `run_rollup` staged to a pass-through, and the failure prints the
  un-collapsed list.
- AC6 — the module docstring of `tools/memory-recall/query.py` carries a ranking-rationale bullet
  for the rollup, naming what it costs and what it buys, and stating that `bench.run_rollup`'s own
  advice against expecting an ensemble gain was measured on the BARE question. The FORKED header now
  reads **seven** constructs and names the seventh.
- AC7 — same suite — `tools/memory-recall/verbatim.json` still matches `bench.py` and `union.py`
  byte for byte. Neither was edited: F2's resolution stands.
- AC8 — `python tools/memory-recall/check-recall.py` — exit 0, `records:fts5:r@5 raw 0.8333 ceiling
  1.0000`, `RECALL_FLOOR ok`. A no-regression observation, not evidence the served shape improved:
  the floor grades ranking over one set and not the CLI's fusion, which is exactly why unit 3 exists.
- AC9 — observed as the true three-part sequence rev-2 could not have got: `CACHE_VERSION` is
  unmoved at `3`; the FIRST run after the kit-version bump prints
  `index 946 records + 46818 chunks (rebuilt 2.92s, cause conf_digest)`; the SECOND prints
  `(cached 2026-09-05T11:36:26+00:00)`. rev-2 required that first run to report `cached`, which the
  unit's own `KIT_MEMORY_RECALL_VERSION` bump forbids — that constant is inside the blob
  `Conf.digest()` hashes, and `ensure_cache` keys freshness on it.
- AC10 — `tools/memory-recall/query.py` holds ONE fused call site, `fuse()`, where it held two
  identical `rrf([search(...), search(...)])` expressions — the first attempt and the rebuild after
  a `sqlite3.DatabaseError`. A rollup applied to one and not the other would have made the served
  shape depend on whether the cache happened to be healthy, and every arm in the suite runs the
  healthy path, so the defect was unobservable by construction. Deleting the duplication is smaller
  than gating it.

## What the rollup actually keys on, because the spec's own name for it was wrong

§4 called the path branch a FALLBACK. Measured over the tracked corpus by running `extract_chunks`
across every `memory/**/*.md`: **129 of 20056** chunk documents carry a `rec`, so the parent key is
the PATH for **99.4%** of the served arm and the per-record behaviour is the 0.6% case. A chunk gets
`rec` only when a heading line itself defines a record id and the heading pattern requires `#{2,6}`,
so an H1, a bold-list anchor and a table anchor all leave it unset.

The unit survives that correction — a per-path cap at most one hit per file is precisely what the
duplicate-slot problem needs — but the description did not, and S7 gained a SECOND arm over the
unanchored branch because an arm on the 0.6% certifies nothing about the other 99.4%.

## One thing this unit added that no criterion asked for

`ensure_cache` now derives WHY it rebuilt and the report line names it. AC9 as folded requires the
cause to be observable, and it was not: the line said `rebuilt Ns` and nothing else, so a criterion
about caching could only assert THAT a rebuild happened. That is how rev-2 came to assert the
opposite of what its own kit bump forces. The cause is one of `no manifest`, `forced`,
`CACHE_VERSION`, `chunk_max`, `conf_digest`, `alias_digest`, `corpus digest` or `a missing database`
— each a separate reason, and `conf_digest` moving costs exactly one rebuild per node while a corpus
digest moving is routine.

## Suites, in full

- `python tools/memory-recall/selftest.py` — **44/44 passed**.
- `python tools/memory-recall/check-recall.py` — exit 0.
- `bash tools/check-kit-versions.sh` — exit 0 with `KIT_MEMORY_RECALL_VERSION` at `1.8` across its
  three carriers.

The kit's suite is `subject = kit` and held off an ordinary bar, so it was run ON DEMAND, directly.
