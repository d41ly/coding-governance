# TOOL-aMendedFleet-31 — recall output keeps every hit and prints snippets only for the head

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 31

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every recall query prints every fused hit with a snippet until the 20,000-byte budget runs out, so a
typical answer is about 17 KB of 40 snippets, while the hits a caller actually opens cluster near the
top. This unit prints snippets for the head of the ranked list only, sized by a share of the byte
budget, and prints every later hit as a one-line pointer, so the answer costs well under half its
bytes and no hit leaves the list. A hard top-5 cut is not an option: logged opens sit at ranks
beyond 20, and weak-term answers sat at ranks 9, 19 and 35 in the report.

## 2. Scope (IN)

- **S1** — `emit` in `tools/memory-recall/query.py` renders in two tiers over the same ranked pool.
  The SNIPPET tier renders each hit exactly as `render` does today, while the bytes spent stay
  within `SNIPPET_SHARE` of the budget; the first hit is always in that tier. The POINTER tier
  renders each later hit as one line, `[<n>] <id> · <path>:<line>`, or `[<n>] <path>:<line>` for a
  hit with no id, the shape of today's header line, until the whole budget is spent. Observed by
  AC1 and AC2.
- **S2** — `SNIPPET_SHARE = 0.25` is a module constant beside `DEFAULT_BUDGET`, so the snippet tier is
  sized by `--budget` and no new flag exists. At the default budget the tier holds about 5,000 B.
  Observed by AC2 and AC4.
- **S3** — After the hits, one byte-stable line names the split:
  `snippets for ranks 1-<s> · pointers for <s+1>-<shown> of <n> hits · raise --budget for more snippets`,
  printed only when the pointer tier is non-empty. Today's `shown <k> of <n> within <b> B` line
  stays for hits the whole budget could not reach. Observed by AC1 and AC4.
- **S4** — The query's log row keeps `n_shown` and `shown_paths` counting BOTH tiers, because a
  pointer line shows the path and `tools/memory-recall/recall-opened.js` maps a read to a rank through
  `shown_paths`, and gains `n_snippets`, the snippet-tier count. Observed by AC3.
- **S5** — `emit` returns `(text, shown, spent, overflow, snippets)`; the existing call sites in
  `query.py` and `tools/memory-recall/selftest.py` take the fifth value. The selftest arm
  `test_budget_bounds_emission_and_beats_full_documents` moves its truncation probe to a budget
  small enough that the pointer tier cannot hold all 20 fixture hits, and a new arm pins S1 to S3.
  Observed by AC5.
- **S6** — The Skill's "Reading the answer" paragraph, edited in
  `tools/memory-recall/SKILL.template.md` and re-rendered into `.claude/skills/memory-recall/SKILL.md`,
  and the README's `Use` section say the head prints snippets, the rest prints pointers, and a pointer
  is opened by its path. The paragraph stops typing the default budget and names `--budget` instead.
  Observed by AC6.

## 3. Non-goals (OUT)

- Changing `--k`, `DEFAULT_BUDGET`, the fusion or the rollup. The ranked pool is the pool today.
- A count-based cut of any size. §8 F1 records why.
- Re-tuning `SNIPPET_SHARE` against a graded set. The gold set has n=12 to 16 and cannot price a
  share; unit 29 of this build harvests a larger one, and a re-tune follows it.
- The miss advice in the Skill and the README's stale scale figures. Those are unit 33, which edits
  the paragraph after the one S6 edits.
- The memory-recall kit version bump, owed once at this build's close after the last move.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `tools/memory-recall/` is byte-identical at `580dc980e`, re-verified
2026-10-04 with `git diff --stat`.

- `emit` prints snippets in rank order until the next one would pass the budget, and nothing else.
  The live query log at `<git-common-dir>/recall/queries.jsonl`, 432 query rows on 2026-10-04,
  PINNED: `bytes_emitted` median 16,594 B and p90 17,749 B; `n_hits` and `n_shown` median 40. The
  report's "37 hits per answer" is now 40.
- The same log holds 36 `opened` rows carrying a rank, hand and inferred: median rank 6, 12 beyond
  rank 10, 5 beyond rank 20, the deepest 37. PINNED, measured 2026-10-04. A cut at any rank below
  the pool depth drops answers callers opened.
- One real answer, the §10 probe below, split by line kind with a scratch reader over its stdout:
  40 header lines averaging 84 B, 40 snippet lines averaging 347 B, 17,273 B in all. Printing every
  header and the first 10 snippets costs 6,801 B; the first 12, 7,636 B. PINNED, measured
  2026-10-04 on one query; AC2 re-derives the figure on the tree it runs on.
- `rrf` sums `1/(RRF_K + rank)` per arm and discards every `bm25` value, and the selftest arm
  `test_rrf_is_rank_based_not_score_based` pins that. The fused list carries no score magnitude
  that could call a top hit "strong".

### Output shape

```
index <r> records + <c> chunks (cached <built_at>)
<n> hits for: <question>

[1] <id> · <path>:<line>
    <snippet>

[2] <path>:<line>
    <snippet>

[7] <id> · <path>:<line>
[8] <path>:<line>
snippets for ranks 1-6 · pointers for 7-40 of 40 hits · raise --budget for more snippets
```

### Inventory

- `SNIPPET_SHARE = 0.25`, a module constant of `query.py`.
- `render_pointer(hit, n)`, the pointer line; the lexicon's `--suggest` answered it OK for cell
  `py.function`. A name the lexicon leg refuses at build time is replaced with its `--suggest`
  answer and this list amended with a rev bump.
- `n_snippets`, a new key of the `query` log row.

### Files touched (estimate)

- `tools/memory-recall/query.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md`

### Rollout

Units 31, 32 and 33 all write `tools/memory-recall/README.md` and two of them write the Skill, so
they build in order and never concurrently. The rendered Skill is regenerated with
`adopt-memory-recall.sh --scaffold`, never hand-edited.

### Alternatives rejected

- **`--k 10` per source.** The pool shrinks to at most 20 hits, and 5 of the 36 ranked opens sat
  beyond rank 20 of today's pool.
- **A hard 5 plus 3 cut.** 22 of the 36 ranked opens sit beyond rank 5.
- **Cut adaptively when the top score is strong.** `rrf` keeps no score magnitude, so "strong" has
  no signal to read without a new scoring path.
- **Cut every snippet to its decisive line.** It keeps 40 pointers at a similar byte count, about
  40 lines of 84 B plus about 100 B each, UNVERIFIED, but thins the context on the head ranks where
  most opens fall, which is what the snippet tier keeps whole.

## 5. Production-readiness checklist

- security — N/A — read-only over the local index; the log gains one integer.
- perf / scale — one more branch per hit; the output shrinks.
- error / empty / loading states — zero hits prints today's lines; a budget below the first hit
  keeps today's overflow note; a pool that fits the snippet tier whole prints no split line.
- observability — the split line says where snippets stop, so a short answer never reads as a
  short pool; `n_snippets` lets the log tell the two tiers apart.
- risks — a caller that only reads snippets skips the pointer tier. The Skill paragraph says a
  pointer is opened by its path.
- testing — a new arm in `tools/memory-recall/selftest.py`, and direct runs on this tree.
- migration — N/A — no stored data; old log rows simply lack `n_snippets`.
- user docs — the Skill paragraph and the README `Use` section, S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/query.py "how is the recall query output sized and trimmed" --terms "query.py emit byte budget DEFAULT_BUDGET snippet render rank weak terms trim pointer"`
  runs on this tree, the number of lines starting `[<n>] ` equals the `<n> hits for:` count, every
  snippet line sits above the first pointer line, and the split line names ranks that agree with
  the line kinds above it.
  Red when: a hit is missing, a snippet follows a pointer, or the split line disagrees.
  figure: every count DERIVED from that run's stdout.
- **AC2** — When the AC1 command runs, its stdout is at most half the bytes the same command prints
  in a throwaway clone checked out at the pass's parent commit, against the same corpus.
  Red when: the output did not shrink by half, or the clone's run lists a path this run does not.
  fixture: a `git clone --local` under a short `%TEMP%` root; the tree holds none today.
  figure: both byte counts DERIVED at observation time.
- **AC3** — When the AC1 command has run, the last `query` row of the log under
  `git rev-parse --git-common-dir` carries `n_snippets` equal to the split line's `<s>`, and
  `shown_paths` holds `n_shown` entries, pointer hits included.
  Red when: `n_snippets` is absent or wrong, or `shown_paths` stops at the snippet tier.
- **AC4** — When the AC1 command runs again with `--budget 3000`, the snippet tier holds at least the
  first hit, pointers follow it, and the split line is printed.
  Red when: a small budget prints snippets only, or prints no hit in full.
- **AC5** — When a scratch script under the session scratchpad, run from the repo root, puts the
  kit directory on `sys.path`, imports `query` and calls `emit` on 20 synthetic hits of equal size
  at a budget whose `SNIPPET_SHARE` holds 3 of them, it gets 3 snippets, 17 pointers and a fifth
  return value of 3; at a budget too small for every pointer, `shown` is below 20.
  Red when: the tier boundary moves, a hit is dropped while budget remains, or the truncation path
  becomes unreachable.
  fixture: built by the script itself; the kit's own arm for the same shape is the §7 `New arm:`.
- **AC6** — When `bash tools/memory-recall/adopt-memory-recall.sh --check` runs after the render, it
  exits 0, and `grep -n "pointer" .claude/skills/memory-recall/SKILL.md tools/memory-recall/README.md`
  hits the Skill's "Reading the answer" paragraph and the README `Use` section.
  Red when: the rendered Skill drifts from its template, or either text still says every hit prints
  a snippet.

## 7. Gates

`memory-recall skill wiring` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-recall/selftest.py · a 20-hit fixture at a budget whose snippet share holds 3 hits, against today's all-snippet emission · none

`memory-recall kit selftest`, `recall floor` and `recall floor arms` run at the close: their guard,
`tools/memory-recall/`, is excluded as broad. `check-wiring self-test` and
`lexicon naming predicates` are owed by the rendered Skill under `.claude/`.

## 8. Open questions

- **F1 — What decides where snippets stop?**
  Options: a fixed count of 10; a share of `--budget`; a score threshold on the fused list. The
  score threshold has no signal, §4. A fixed count ignores snippet length and makes `--budget` a
  knob over pointers only. A share keeps `--budget` the one knob and adapts to how long the head
  snippets are.
  RESOLVED (agent, 2026-10-04, delegated): a share of `--budget`, S2.
- **F2 — Does a pointer-tier hit count as shown?**
  Options: count it, so `shown_paths` maps its read to a rank; or count snippets only. The hook's
  `in_shown` asks whether the caller was shown the path, and a pointer shows it.
  RESOLVED (agent, 2026-10-04, delegated): both tiers count, and `n_snippets` separates them, S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `emit`, `render`, `rrf` and the live query log at base.

## 10. Reuse audit

The seam extended is `emit` in `tools/memory-recall/query.py`, which already owns the byte budget
and the overflow rule; the pointer line reuses the header half of `render`. `python
tools/codebase-map/reuse_lookup.py "print a ranked list of hits within a byte budget, full text for
the top and one-line pointers for the rest"` returned name-stem neighbours only, `read_text`,
`rank_with` and `export_text` among them, none of which emits a ranked list, so no existing seam
fits beyond `emit`. Recall named `TOOL-aWeighedCompass-18`, which measured the chunk half costing
116% more snippet bytes for no recall at k=20, and `TOOL-aProbedToolkit-9`, the reuse-lookup byte
budget that cites this CLI's budget as its model. Where the report and the tree disagree: hits per
answer are 40, not 37, and `--stats` exists but only beside a question; alone it exits 2.

Recall terms used: `python tools/memory-recall/query.py "how is the recall query output sized and
trimmed, and why is there no hard top-5 cut" --terms "query.py emit byte budget DEFAULT_BUDGET
snippet render rank weak terms top-5 trim --k per source"`
