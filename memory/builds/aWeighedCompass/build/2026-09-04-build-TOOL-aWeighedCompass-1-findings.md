**Serves:** journal TOOL-aWeighedCompass-1

# Does the orientation toolchain actually orient? — the measured answer

Every figure below carries the command that produced it. Harness scripts were written to the session
scratchpad and are reproduced inline where they are not one-liners. Each finding is labelled
**MEASURED** (derived from a command run against this tree) or **INFERRED** (rests on a heuristic
that the producing tool itself flags as such).

Base: `c4fcf5ad`, node `a`, 2026-09-04.

**Measurement provenance, because this build perturbed two of its own subjects.** Every figure was
taken BEFORE this build's own records landed, and two will not reproduce as quoted:

- `memory/backlog/TOOL.md` is quoted at 261007 B. This build appended 15 rows totalling 7991 B, so
  `wc -c` now returns 268998. The difference is exactly this build's rows and nothing else.
- `codebase-map/lookups.jsonl` is quoted with other sessions' 33 probes separated out. The harnesses
  here contributed 366 of the file's 399 rows at the time of reading, and more since. Any usage
  figure from that log must exclude this worktree, which section 3 does explicitly.

The recall query log was READ and not written to by the analysis, so its 148/70 split is unperturbed.
No other subject was touched.

## The verdict in four sentences

The retrieval half works and is worth its cost: on the graded fixture `records:fts5` finds an
expected record in the top 5 for 83% of questions against grep's 17%. The other half of the same
ensemble — `chunks` — scores below grep on the identical task while supplying 52.5% of every result
set a session reads, and no gate grades it. The map probe points at a file the unit went on to
change about half the time overall — but only 37% of the time for a unit touching three files or
fewer, and it buries the answer in seventeen candidates at a mean precision of 0.056. And
the single largest orientation cost in this repo is not a tool at all: it is one 261 KB backlog
shard that the session-start reading order asks every tooling session to load. And a feature did get
rebuilt: merge `05b3c68f` records two units on one node independently rewriting the same two hygiene
checks, with one implementation discarded — though the branch was 389 commits behind main, which no
probe defends against.

## 1. What sessions actually asked, and what it cost them

The kit logs every recall query. Nobody had read the log.

```bash
python scratchpad/analyze_log.py "$(git rev-parse --git-common-dir)/recall/queries.jsonl" .
```

**MEASURED.** 219 rows spanning 2026-08-03 to 2026-09-04: 148 queries and 70 attributed opens.

| Signal | Value |
|---|---|
| Bytes emitted per query | mean 14436, median 15649, max 19044 |
| Total emitted across the log | 2.04 MiB |
| Distinct questions | 130 of 148 (12.2% repeat rate) |
| Terms supplied per query | mean 12.8, within the documented 8–14 band |
| Result slots shown | 5140 |
| Distinct paths behind them | 2339 |

**Finding 1 — 54.5% of every result set is a path the same result set already showed. MEASURED.**
2801 of 5140 slots are repeats. The mean query spends 48.4% of its slots on new paths; the worst
(`qid 132`) showed 8 distinct paths across 39 slots. At 14.4 KB per query this is roughly 7.8 KB of
duplicate context per probe. The cause is structural and is finding 3: chunks are 600-character
slices, so one relevant file legitimately produces many hits, and the fusion keys on
`(path, line, text[:60])` rather than on the file.

**Finding 2 — the corpus retains paths that no longer exist. MEASURED.** 52 of the 627 paths the log
ever showed (8.3%) are absent from the tree today. Retrieval is rebuilt per run so this is not a
stale index; it is that the log preserves answers whose files were deleted or moved, which matters
only for this analysis. No session-facing cost is claimed.

**INFERRED, and weakly.** 17 of 70 attributed opens (24.3%) landed on a file the query had shown;
68 of 148 queries (45.9%) had any attributed open. These numbers are *not* precision. Per
`tools/memory-recall/recall-opened.js` (`:25`), an open is the FIRST corpus-file read within a 30-minute
window, one row per query maximum, and every row carries `inferred: true` because "inside the window
is indistinguishable from a deliberate pick". A session that read three shown files and then one
unshown file records a single `in_shown: false`. Treat this as a hint that sessions frequently
navigate away from the result set, not as a measured miss rate.

## 2. The retrieval substrate: one half excellent, one half below grep

`bench.py` must be run at the chunk width `query.py` serves. The extractor defaults to 2400; the live
index is built at 600. The first run of this measurement used the default and produced 18641
documents against the live index's 43270 — an invalid corpus, and the result was discarded.

```bash
python tools/memory-recall/extract.py . <dir> --chunk-max 600
python tools/memory-recall/bench.py <dir> tools/memory-recall/recall-fixture.json \
       --sets records,chunks --subs grep,fts5,fts5w,rm3 --ks 1,5,10,20
```

**MEASURED**, 12-question fixture, both sets at ceiling 1.00:

| set | substrate | r@1 | r@5 | r@20 | MRR |
|---|---|---|---|---|---|
| records | grep | 0.08 | 0.17 | 0.17 | 0.125 |
| records | **fts5** | **0.58** | **0.83** | **0.83** | **0.681** |
| chunks | grep | 0.17 | 0.17 | 0.17 | 0.167 |
| chunks | **fts5** | **0.00** | **0.00** | **0.08** | **0.008** |

**Finding 3 — the ensemble's chunk half scores an order of magnitude below its record half and below
grep, and nothing grades it. MEASURED.** `query.py` merges both sets by reciprocal-rank fusion at k
per source. Measured from the log's own `results` field, the live pool is 52.5% chunks and 47.5%
records:

```bash
python -c "import json;from collections import Counter;rows=[json.loads(l) for l in open(...)];c=Counter(h['set'] for r in rows if r.get('type')=='query' for h in r['results']);print(c)"
# {'chunks': 387, 'records': 350}
```

`check-recall.py` pins `records:fts5:r@5 >= 0.81` and reports 0.8333. That cell is real and it
passes. It is also the only cell anyone grades, and it is the half that works.

**Finding 3b — the published chunk numbers are measured on a query shape no session sends, and
correcting it changes the answer. MEASURED, added after the first draft.** The committed fixture
carries no terms (`any with terms? 0 of 12`), so `bench.py` grades the bare question — while
`query.py` REFUSES without `--terms` and all 148 logged queries supplied them. Re-running with terms
appended to each question, at the live chunk width:

| set | substrate | r@20 bare | r@20 with terms | MRR bare | MRR with terms |
|---|---|---|---|---|---|
| chunks | fts5 | 0.08 | 0.17 | 0.008 | 0.026 |
| chunks | **roll** | 0.08 | **0.33** | 0.010 | **0.044** |
| records | fts5 | 0.83 | **1.00** | 0.681 | 0.646 |

So terms roughly double chunk recall and take `records` to a perfect r@20. `roll` — the small-to-big
rollup already implemented at `bench.py` (`:135`) and dispatchable as `roll` (`:322`) — quadruples
chunk recall and is the only chunk substrate that beats grep decisively. The kit's own docstring
records rollup as worth "+0.04 to +0.05 on CHUNK-ONLY retrieval"; with terms it is +0.25 at r@20.
**That docstring's measurement is stale for the query shape sessions actually use.**

**Finding 3c — in the live ensemble the chunk half adds zero recall and 58% more bytes. MEASURED
with `union.py`**, the ensemble scorer that grades the two-set shape the CLI serves, with terms, k=20:

| ensemble | recall | bytes_full | bytes_snippet |
|---|---|---|---|
| `records:fts5+chunks:fts5` (the live shape) | 1.000 | 32451 | 18424 |
| `records:fts5` alone | **1.000** | **20483** | **8544** |
| `records:fts5+chunks:roll` | 1.000 | 32400 | 18374 |

Identical recall. The chunk half costs 11968 extra bytes read in full, and 9880 extra as snippets —
116% more snippet bytes for nothing measurable.

**The caveat that stops this being a verdict, and it is a big one.** `records` alone already reaches
1.000 at k=20 on this fixture, so the fixture CANNOT show chunks contributing anything — there is no
headroom left to contribute. This is fixture saturation, not proof that chunks are useless. And
`union.py`'s own docstring names the thing recall@k cannot see: whether an agent can still pick the
right record off snippets alone. Chunks may be earning their place by pointing at the right LINE
inside a record, which no metric here measures. Two further honesty notes: n=12, so 0.08 to 0.33 is
one question becoming four; and the terms were written by hand by someone who had just spent a
session in this corpus, which biases them optimistic.

**So the first move is not to tune chunks. It is to build a fixture that can tell the difference.**
Every number above saturates, and tuning against a saturated fixture is how a pin gets set to noise.

**The honest caveat, stated because it changes what the number means.** The fixture's `expected_ids`
are record ids, so an expected "document" in the chunks set is whichever 600-character slice carries
the anchor. Ranking that specific slice is a harder task than ranking a whole record, and part of
the gap is task difficulty rather than substrate failure. What survives the caveat is the
same-task comparison: on identical questions against an identical corpus, grep beats fts5 on chunks
by 2:1. That comparison does not depend on the fixture's design.

**Finding 4 — the `spine` document set is empty in this repo, and has been since the memory tree
flattened. MEASURED.**

```bash
python -c "import importlib.util;spec=importlib.util.spec_from_file_location('ex','tools/memory-recall/extract.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);print(m.DURABLE.pattern)"
```

`DURABLE` requires `memory/<one-dir>/(DECISIONS|BACKLOG).md`, `memory/<one-dir>/decisions/*.md`, or a
matching archive path. This repo's decision log is `memory/DECISIONS.md` and its backlogs are
`memory/backlog/TOOL.md` — a flat layout adopted at the flatten. The pattern matches **none** of
them. `extract.py` reports `spine 0 docs, 0 indexed chars` and `ids anchored 678 (durable home: 0)`.
The kit's own comment at `tools/memory-recall/extract.py` (`:127`) says why nobody noticed: "DURABLE
selects ONLY the `spine` document set … so no gate and no merge-bar floor reads this."

Impact, bounded honestly: the definitions still live in `records`, which is the half that scores
0.83, so no answer is unreachable. What is lost is the highest-precision layer as a tuning option —
`bench.py --sets spine` can never inform a decision here — and the memory tree's central idea of a
"definition home" has no representation in retrieval at all. Any adopter with a flat memory root
inherits the same silent zero.

**Finding 5 — 211 of 889 cited ids (23.7%) have no record of their own. MEASURED.** From the same
extract run, `orphan-ids.txt` holds 211 ids: 171 `TOOL`, 24 `DEPL`, 9 `PLAY`, 7 `KICK`. An orphan is
an id cited somewhere in the corpus that no anchored record defines. `TOOL-dRetiredFork-14` is one,
and it is cited in 47 files including `tools/hooks/README.md`, where it is the stated authority for
the one-copy hook rule. A session asking recall what that decision was gets chunks that mention it
and no definition. The distinction matters: this is a memory-tree hygiene gap, not a retrieval bug —
`TOOL-aProvenReuse-4` by contrast has its own backlog row and anchors correctly.

## 3. The map probe: right about half the time, buried in noise

170 specs record a literal `reuse_lookup.py "<phrase>"`. That is a ground truth nobody had graded.

The first harness reported 0/12 and was wrong — its commit-to-id parse silently resolved 31 of 171
cases where a correct parse resolves 503 ids. Both harnesses now assert liveness first: they probe
`"cap how many agents a fan-out may spawn"` and refuse to report unless `tools/hooks/agent-cap.js`
comes back. It comes back at rank 2 of 8.

```bash
python scratchpad/reuse_gt2.py    # ground truth: files the unit's commits changed
python scratchpad/reuse_gt3.py    # ground truth: the seam the spec's own §10 named
```

**MEASURED**, two independent ground truths:

| Metric | vs. files the unit changed (n=133) | vs. the seam §10 named (n=135) |
|---|---|---|
| Probe returned ≥1 correct path | 63 (47.4%) | 71 (52.6%) |
| hit@1 | 6.0% | 20.0% |
| hit@5 | 22.6% | 39.3% |
| hit@10 | 37.6% | 46.7% |
| Rank of first correct path | mean 6.4, median 6 | mean 4.1, median 2 |
| Product paths returned per probe | mean 17.3 | mean 17.4 |
| Precision | 0.056 | 0.051 |
| Output bytes per probe | mean 10782 | — |

**Finding 6 — the probe is right about half the time and pays ~10.8 KB to say so. MEASURED.** Both
ground truths agree within five points, which is the strongest evidence here that ~50% is the real
figure rather than an artifact of either proxy. The two disagree usefully on rank: graded against the
seam a human actually chose, the median correct hit is at position 2; graded against files eventually
edited, position 6. The probe's *top* is better than its bulk.

**A size bias in the first metric, measured rather than assumed.** Hit rate correlates with how many
files the unit touched, because a larger truth set gives the probe more targets:

| Unit size | Hit rate |
|---|---|
| touched ≤3 product files (n=40) | 15 (37.5%) |
| touched ≥8 product files (n=53) | 35 (66.0%) |
| median truth-set size, hits | 9 |
| median truth-set size, misses | 4 |

So 47.4% is the corpus-weighted figure and it flatters the small, focused unit that the charter's
"keep units small" rule actually asks for. **For a unit touching three files or fewer, the probe hits
about 37%.** The second metric does not carry this bias — it grades against a median of one named
seam and scores higher at 52.6%, which is the better of the two numbers for exactly that reason.

**One miss, in full, because it is the clearest picture of finding 7.** The phrase
`"a wall-clock ceiling per gate leg, enforced by the runner, that turns a hang into a red verdict"`
is recorded verbatim in two specs. Replayed today it returns twelve paths, in this order:

```
 1 tools/govkit/govkit.py              7 tools/memory-recall/selftest.py
 2 tools/playbook/render_playbook.py   8 tools/codebase-map/map_lib.py
 3 tools/run-gates/profile_bar.py      9 tools/codebase-map/map_extractors.py
 4 tools/hooks/agent-cap.js           10 tools/memory-recall/query.py
 5 tools/memory-recall/test_recall_floor.py  11 tools/hooks/scratch-guard.js
 6 tools/codebase-map/selftest.py     12 tools/memory-tree/gen_build_index.py
```

`tools/run-gates/run-gates.sh` — the runner that enforces the ceiling — is absent, and so is
`tools/gate-legs.json`, which holds the `ceiling` field itself. Both units went on to edit them. The
probe instead offered the playbook renderer and two hooks. This is finding 7 made concrete rather
than statistical: the answer is shell, and shell has no symbol extractor.

The first metric is biased DOWN and the bias is worth stating: reusing a seam without editing it
scores as a miss. The second metric is biased UP: a spec's §10 sometimes records what the probe
returned, so the probe is partly being graded against its own past output. Neither bias is large
enough to move a 50% figure to either 20% or 80%.

**Finding 7 — shell is dark to the symbol index. MEASURED.** Every probe output ends with
`recall partial: layers bash have no symbol extractor`. 11 of 133 graded cases (8.3%) have a ground
truth that is *entirely* `.sh` files, so the probe could not have hit them by construction.
Restricting to cases with at least one non-shell truth file moves the hit rate from 47.4% to 51.6%.
This repo's gates are overwhelmingly shell, so the dark layer sits on a large part of the product.

**Finding 8 — ranking is by shared name stem, which is why a conceptual query returns unrelated
symbols. MEASURED, and reproduced during this session's own kickoff.** The probe
`"measuring whether the orientation toolchain surfaces the right context for a session"` returned
twelve `measure_*` functions from six unrelated files, matched on the stem `measur`, plus
`fold-text-is-unreviewed-surface.md` on `surfac`. The relevant answer —
`tools/memory-recall/check-recall.py` — was present, but so was `measure_slot_sizes` in the build
index generator. Precision 0.056 is the general form of this: about one useful path in eighteen.

**Two mechanical causes, both verified at source, both cheap to fix.** First,
`tools/codebase-map/reuse_lookup.py` (`:243`) reads
`for name, reason in sorted(neighbours.items())[:NEIGHBOUR_CAP]` — the neighbour pool is truncated
**alphabetically** before `_rank` computes fan-in, and only the line after does
`ranked.sort(key=lambda r: (not r.is_seed, -r.fanin, ...))` run. A high-fan-in neighbour whose name
sorts late is discarded before it can ever be ranked. Second, `tools/codebase-map/map_lib.py`
(`:342`, `:345`, `:349`) excludes every symbol whose name starts with `_`, so private helpers are
absent from the index entirely — and a private helper is exactly the kind of internal seam a reuse
audit is looking for.

**Finding 9 — the probe DOES log, and the backlog row saying otherwise is stale. MEASURED, and it
corrects a claim this session made at kickoff.** `TOOL-aProvenReuse-4` is OPEN and states that
`reuse_lookup.py` "logs NOTHING, so the map half of the reuse obligation has no liveness evidence at
all". `tools/codebase-map/reuse_lookup.py` (`:442`) writes `<git-common-dir>/codebase-map/lookups.jsonl`,
landed by `TOOL-aClosedDocket-2` in `5a368d98`. The file holds 399 rows.

This is the clearest orientation defect found: the backlog handed a false fact to a session reading
it for orientation, and that session repeated it. Five days elapsed between the code closing the row
and this measurement.

The row is not *entirely* wrong, and the surviving half matters. The map log records only
`{type, at, query, worktree, n_shown}` — no results and no opens. Recall's log records results and
attributed opens, which is the entire reason section 1 of this report exists. So the map probe now
has liveness evidence (it ran) and still has no efficacy evidence (whether it helped). The two are
different claims and the row conflates them.

**Usage, with this session's own probes excluded.** 33 of the 399 rows came from other sessions,
across 4 days since the logger landed, over 32 distinct queries. The remaining 366 are this
research's harnesses. Any usage figure quoted from that log must exclude them.

## 4. Does a feature get rebuilt anyway? Once, documented, in the repo's own merge message

This is the question the reuse audit exists to answer, and the corpus answers it in both directions —
from the same build.

**Finding 9b — a save. MEASURED.** `memory/builds/aCollapsedScan/spec/2026-08-26-spec-TOOL-aCollapsedScan-6.md`
opens `# TOOL-aCollapsedScan-6 — RETIRED: hygiene check 20 already gates per-file id uniqueness`. A
unit was specced, prior art was found, and it was retired before code. That is the mechanism working
exactly as designed.

**Finding 9c — and a rebuild, in the same build. MEASURED.** Merge `05b3c68f` carries its own
verdict in its subject line: `merge: aCollapsedScan followups — its code half had already landed,
twice over`. Its body:

> `TOOL-aCollapsedScan-13`'s builtin rewrite of checks 21/23 is subsumed by `TOOL-aThawedCorpus-1`
> and `-4`, which removed the enclosing shell loops too. Main's bytes kept.

Two units on the same node independently rewrote the same two hygiene checks. One implementation was
discarded at the merge. `git log --all --grep` confirms both sides touched
`tools/memory-tree/check-memory-hygiene.sh`: `836e4e27` for `-13`, `faf5b7fb` and `5e928f5b` for
`aThawedCorpus`.

**The honest attribution, because blaming the wrong instrument fixes nothing.** The same merge
message records that the branch was **389 commits behind main**. No reuse probe protects against
that: the duplicate work did not exist in the corpus when the branch's audit ran. This is a §3
trunk-based-development failure that the orientation tooling was never positioned to catch, and the
correct reading is that the reuse audit is not the control for concurrent work — merging small and
often is. The manifest already carries the lesson as an orientation bullet
("Before starting work inside a kit, check whether another node is already rewriting it"), which is a
`git log origin/main -- tools/<kit>/` away and is cheaper than any probe here.

**Finding 9d — the reuse OBLIGATION earns its keep; the instrument it names does not. MEASURED.**
Three units in this corpus were killed before code by a reuse audit: `TOOL-aCollapsedScan-6`,
`TOOL-dPromptedSeam-1` and `TOOL-aThawedCorpus-2`. In none of them is the save attributable to
`reuse_lookup.py`. The clearest is `aThawedCorpus-2`, whose §10 says in its own words that the seam
was **"Found by reading `run-gates.sh` while pricing a kit-local digest helper"**. The others came
from a map dossier reached through `query.py`, or from the Tier-2 review pass.

That is the sharpest available statement of section 3's numbers. The habit of asking "does this
already exist" before building is paying for itself. The specific tool the habit is required to
invoke is not the one collecting.

## 5. What the orientation protocol actually costs to read

**Finding 10 — the session-start reading order asks a tooling session for 382 KB, and 68.3% of it is
one backlog shard. MEASURED.**

```bash
for f in AGENTS.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/DECISIONS.md memory/backlog/TOOL.md; do wc -c "$f"; done
```

| File | Bytes | Note |
|---|---|---|
| `AGENTS.md` | 64506 | auto-loaded every session |
| `memory/guides/SESSION-KICKOFF.md` | 25571 | the manifest |
| `memory/LIVE.md` | 2332 | generated |
| `memory/DECISIONS.md` | 28749 | §6 reading order |
| `memory/backlog/TOOL.md` | 261007 | §6 reading order |
| **Total** | **382165** | ~95k tokens |

The charter's §6 says "read your stream's decision log + backlog". For the `tooling` stream that
instruction is 261 KB.

**Finding 11 — the shard is 4.25× its own cap, waived, and the remedy its waiver names cannot
work. MEASURED.** `.memory-tree.conf:148` sets `INDEX_CAP_BYTES="61440"`.
`memory/project/curation-debt.txt` waives checks 6, 7 and 8 on this file, and its note says rotation
is now the live remedy: "nineteen rows were terminal. Rotation is the live remedy and this row now
describes a drain nobody has performed rather than one that cannot be."

Re-derived today, by status, over the 334 parsed rows:

| Status | Rows | Bytes | |
|---|---|---|---|
| OPEN | 247 | 191931 | live |
| CLOSED | 64 | 53451 | terminal |
| SPECCED | 10 | 3618 | live |
| DEFERRED | 7 | 5733 | live |
| WONTDO | 3 | 2991 | terminal |
| INPROGRESS | 2 | 1430 | live |
| WITHDRAWN | 1 | 1241 | live |

Rotating **every** terminal row sheds 56442 B and leaves 203953 B — still 142513 B over the cap, a
factor of 3.3. The mass is 247 OPEN rows at a mean of 780 bytes each; the largest is 2752 bytes. A
backlog row has become a short essay. Rotation is not the remedy; splitting the shard or shortening
rows is. The waiver's note should be corrected, and it also admits it currently hides one real
status-token fault.

**Finding 12 — the charter template is at 100.0% of its gated ceiling, with 8 bytes spare.
MEASURED.** `bash tools/check-template-size.sh` reports `49144 / 49152 bytes (8 under, 100.0%)` and
also WARNs that the file has passed its recorded high-water of 48378. The document every session
auto-loads as `AGENTS.md` (64506 B after rendering) is therefore full: any new rule must displace an
old one, which is the design working as intended, but it means "add a line to the charter" has
stopped being an available remedy for anything found in this report. Every recommendation above is
written to need no charter change.

**Finding 12b — the bug-class checklist has two settings, everything and nothing. MEASURED.** The
kickoff engine's Step 4 runs `gotchas.py --for-paths` over the pointer-map row's entrypoints. Run
against each of the manifest's four rows:

| Pointer-map entrypoint | Classes selected | Bytes |
|---|---|---|
| `tools/` | 30 + 4 universal | 8113 |
| `coding-governance-agents.template.md` | 0 + 4 universal | 1034 |
| `skills/session-kickoff/` | 0 + 4 universal | 1034 |
| `WIRE-INTO-PROJECT.md` | 0 + 4 universal | 1034 |

The `tooling` row's entrypoint is the whole `tools/` directory, so it selects essentially the entire
catalogue — a checklist of thirty classes is not a checklist, it is the catalogue with extra steps.
The other three rows anchor nothing at all. Run against four specific kit directories instead, the
same command returned 6 classes plus the 4 universal, which is a usable list. The tool is fine; the
manifest's entrypoint granularity is what makes it useless for the biggest stream.

**Finding 12c — the manifest never mentions the recall kit. MEASURED.**
`grep -c recall memory/guides/SESSION-KICKOFF.md` returns 0, against 5 for `codebase-map` and 5 for
`gotchas`. The engine's Step 4 conditions its recall probe on the kit being present and, finding no
declaration in the project layer, falls through to probing two hard-coded directory spellings — while
both kits support any install prefix. One of the three orientation probes is reached by a filesystem
guess rather than by declaration.

**Finding 13 — cross-carrier prose duplication is near zero. The "not restated here" discipline
measurably works. MEASURED, and this is the strongest positive result in the report.**

```bash
python scratchpad/dup.py   # 10-word shingles, inline code stripped
```

| Pair | Shared shingles | % of the first |
|---|---|---|
| `AGENTS.md` ↔ `SESSION-KICKOFF.md` | 13 | 0.1% |
| `AGENTS.md` ↔ `HYGIENE.md` | 2 | 0.0% |
| `AGENTS.md` ↔ `REVIEW-PROTOCOL.md` | 4 | 0.0% |
| `SESSION-KICKOFF.md` ↔ `BUILD-METHOD.md` | 2 | 0.1% |
| `AGENTS.md` ↔ `coding-governance-agents.template.md` | 7234 | 78.1% |

Eight orientation carriers totalling ~41k words share, between them, six passages of 14 words or
more — and three of those six are the render pair. The repo spends real effort on pointing rather
than copying, and it is working. **De-duplicating the governance prose is not where the wins are**,
and any recommendation to consolidate these documents should be rejected on this evidence.

**What this method cannot see, stated because it bounds the positive result.** Shingle overlap
catches VERBATIM reuse. Two carriers that state the same rule in different words score zero here
and are still two answers to one question. So the finding is precisely "the carriers do not
copy-paste from each other", which is what the pointer discipline was built to prevent, and not
the broader "no fact is stated twice". A paraphrase audit would need a reader, not a shingle.

The single genuine duplicate is structural rather than editorial: `AGENTS.md` *is* the render of
`coding-governance-agents.template.md`. A `playbook`-stream session is pointed at the template by the
manifest's pointer map while already holding the render in context, and pays ~49 KB for a text it
has.

## 6. Corroborating signals

`python tools/drift-audit/drift_report.py` — seconds, no agents:

```
lexicon_marginal_offense_rate                  149  557  out of tolerance (report only)
shrink_only_lists_not_shrinking                  3    5  out of tolerance (report only)
dangling_pointers_in_own_ledger                 -1    0  DEAD PROBE — signal cannot move
live_backlog_rows_per_shard                    268    4  out of tolerance (report only)
readme_mechanism_drift                          24   92  out of tolerance (report only)
```

`live_backlog_rows_per_shard` at 268 independently corroborates finding 11 from a different code
path. `dangling_pointers_in_own_ledger` printing `DEAD PROBE` rather than a reassuring 0 is the
liveness discipline working exactly as the charter specifies, and is worth recording as a positive.

## 7. Recommendations, ranked by cost removed over effort

| # | Change | Cost it removes | Shape | Row |
|---|---|---|---|---|
| 1 | Close the stale `TOOL-aProvenReuse-4` row, keeping its surviving half | A false fact served to every session that reads the backlog at orientation | One-line edit | `-2` |
| 2 | Fix `DURABLE` to match a flat memory root | Restores the `spine` layer here and for every adopter with a flat tree | One regex | `-5` |
| 3 | Correct the `curation-debt.txt` note that names rotation as the remedy | A recorded plan that provably cannot work, plus one hidden status fault | One-line edit | `-3` |
| 4 | Collapse same-file hits in `rrf()`, or cap hits per path | ~7.8 KB of duplicate context per query, on 148 queries so far | Kit change | `-6` |
| 5 | Split or shorten `memory/backlog/TOOL.md` | 261 KB — 68.3% of a tooling session's stated reading order | Curation job | `-3` |
| 6 | Add terms to the recall fixture | Every chunk figure today grades a query shape no session sends | Fixture edit | `-4` |
| 7 | Switch the chunk source to `roll` in `query.py` | 2x chunk recall AND collapses the 54.5% duplicate slots, one change | Kit change, already implemented | `-17` |
| 8 | Wire `union.py` behind a pin | The one quality leg would grade the shape the CLI serves | Kit change | `-16`, `-19` |
| 9 | Build a fixture that discriminates, then re-price the chunk half | The current one saturates at records-alone, so it cannot | **Owner call** | `-18` |
| 10 | Log `shown_paths` in the map log | Makes the map half measurable at all, as recall already is | Small kit change | `-10` |
| 11 | Record every corpus read in the open window, with rank | Turns this report's weakest numbers into real ones | Small hook change | `-11` |
| 12 | Rank the neighbour pool BEFORE truncating it | A high-fan-in neighbour sorting late is discarded unranked | One-line reorder | `-12` |
| 13 | Index private symbols, or index them at lower weight | The internal seams a reuse audit hunts for are absent | Kit change, needs measurement | `-13` |
| 14 | Demote or re-rank the name-stem arm in `reuse_lookup` | Precision 0.056; ~17 paths returned to deliver ~1 | Kit change, needs its own measurement | `-7` |
| 15 | Add a shell definition extractor | The largest structural blind spot in the map | Real work | `-8` |
| 16 | Anchor the 211 orphan ids, or waive them explicitly | Retrieval cannot define 23.7% of the ids the corpus cites | Curation job | `-9` |
| 17 | Narrow the pointer map's `tooling` entrypoint below `tools/` | A 30-class "checklist" that is really the catalogue | Manifest edit | `-14` |
| 18 | Declare the recall kit in the manifest | One of three probes is reached by a filesystem guess | Manifest edit | `-15` |

Rows 1 through 3 are edits, not projects, and between them remove a false fact, a broken plan and a
silently dead retrieval layer. They should go first regardless of what is decided about 6.

**What NOT to do, on this evidence.** Do not consolidate the governance documents. Finding 13
measures verbatim cross-carrier duplication at 13 shared shingles between the two documents every
session loads, out of 12500. The "not restated here" discipline is the most expensive habit in this
repo and it is the one that is demonstrably working.

## 8. What this could not measure

- **The counterfactual.** Nothing here compares a session that followed the orientation protocol
  against one that did not, because no such record exists. Every efficacy claim above is about what
  an instrument RETURNS, never about what a session did afterwards. Building that instrument would
  mean recording, per unit, which probes ran and whether the unit later touched code the probes named
  — the two logs already carry half of it.
- **Whether the map prevents rebuilds, at a RATE.** Section 4 finds one documented save and one
  documented rebuild, which establishes that both happen and refutes the earlier draft of this line
  claiming the question was unmeasurable. What is still unmeasured is frequency: two instances is an
  existence proof, not a rate, and neither save is attributable to `reuse_lookup.py`.
- **Dossier quality at scale.** 20 dossiers were counted and a few read; no systematic grading was
  done of whether a dossier answers an unfamiliar reader's questions.
- **The `opened` signal properly.** One row per query, first read only, 30-minute window. A richer
  attribution — every corpus read in the window, with its rank — would turn section 1's weakest
  numbers into real ones and is a small change to a hook that already exists.

## Acceptance ledger

**Evidences:** TOOL-aWeighedCompass-1

- AC1 — `scratchpad/reuse_gt2.py` — two ground truths recorded in section 3 at 47.4% and 52.6%; both
  harnesses print `liveness OK` naming the rank `agent-cap.js` returned at, and refuse otherwise.
- AC2 — `--chunk-max 600` — section 2 carries both sets at the width `query.CHUNK_MAX` pins, and
  names the fusion as reciprocal-rank over `records` plus `chunks` at k per source.
- AC3 — `wc -c` — every table in sections 1 through 4 is preceded by the command that produced it.
- AC4 — `inferred` — the open-event paragraph in section 1 is the only claim resting on that signal
  and is labelled INFERRED with the hook's own line cited.
- AC5 — `memory/backlog/TOOL.md` — one row per recommendation, landed with this record.
- AC6 — `gen_build_index.py --check-format` — slot contract clean; the build renders into
  `memory/LIVE.md`.
