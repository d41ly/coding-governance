# memory-recall — ask your decision corpus a question, get the records that answer it

<!-- gov:kit memory-recall@1.3 -->

A project-agnostic kit that turns a memory-tree corpus into two derived FTS5 indexes — one document
per anchored record, one per heading-bounded chunk — fuses them with reciprocal rank fusion, and
emits a byte-budgeted ranked list. Standard library only, offline, no model files, no network.

It declares **no config of its own**. It reads the memory-tree kit's `.memory-tree.conf` — two keys,
`MEMORY_ROOT` and `FAMILIES` — so the corpus root and the id grammar are declared once, in the file
another kit's gate already enforces. A second declaration would be the hand-kept-second-copy defect
this port exists to remove, which is why there is no `--memory-root` and no `--families` flag: the
conf is required, and its absence is a refusal that prints a two-key stub rather than scaffolding one.

Ported from the inCMS `scripts/recall/` implementation at `5318064`.

## What's here

| File | Role |
|---|---|
| `recall_conf.py` | the project layer — reads `.memory-tree.conf`, exposes `MEMORY_ROOT`, `FAMILIES`, the node-tag class, and `Conf.digest()`; carries `KIT_MEMORY_RECALL_VERSION`. Run it directly to print the resolved values (or the refusal). |
| `query.py` | the CLI. **Forked** from upstream — see Maintenance. |
| `extract.py` | record + chunk extraction and the alias join. **Forked**. |
| `bench.py` | the FTS5 index builder and the retrieval-substrate harness. **Verbatim** upstream. |
| `union.py` | the two-source ensemble scorer. **Verbatim** upstream. |
| `selftest.py` | the kit's contract gate — 18 checks, every arm inside a throwaway repo. |
| `adopt-memory-recall.sh` | renders the Skill from the conf (`--scaffold`), and reds when it drifts (`--check`). |
| `SKILL.template.md` | the agent-facing Skill, with the project values as placeholders. Rendered, never copied. |
| `recall-opened.js` | **optional** PostToolUse hook that infers which hit was read. **Forked**. |
| `recall-opened.fragment.json` | the settings block that wires that hook: event, matcher, dedup marker, hook path. |
| `recall-opened.test.sh` | the hook's own check — 8 cases, including a non-`memory` corpus root and a sibling worktree. |
| `verbatim.json` | LF-normalised digests of the two verbatim files, so a silent edit to one reds the selftest. |

## Configure

Nothing to configure. Adopt the **memory-tree** kit first; this kit reads its `.memory-tree.conf`:

| Key | Used for |
|---|---|
| `MEMORY_ROOT` | the corpus root passed to `git ls-files`, and folded into the durable-home regex |
| `FAMILIES` | the `discipline:FAMILY` pairs; the uppercase FAMILY tokens are the id allowlist |

The node-tag character class is **not** a conf key: it is `a-z`, matching the memory-tree gate's own
`node [a-z]`. Non-letter node tags are unsupported.

## Use

```bash
python3 tools/memory-recall/query.py "why did the gate start refusing my push" \
    --terms "pre-push dirty tree porcelain untracked submodule refusal predicate gatepost"
python3 tools/memory-recall/query.py --opened <rank> --qid <N>  # record which hit answered it
python3 tools/memory-recall/query.py "<question>" --rebuild     # force a cache rebuild
python3 tools/memory-recall/query.py --export --tag a           # aggregate the log, outside the tree
```

`--terms` is **required**. Rewriting is the measured half of the retrieval gain upstream (records
recall@20 0.71 → 0.84 on its hard slice) and the CLI cannot produce the terms itself — it is offline
and stdlib-only. The caller is a model, so supplying them costs nothing. `--no-terms` runs the
un-rewritten baseline deliberately and is logged as such.

## What it writes — nothing inside your worktree

The cache (`records.db`, `chunks.db`, `manifest.json`) and the append-only query log
(`queries.jsonl`) live under `<common-git-dir>/recall/`, keyed by a digest of the worktree path.
`--export`'s aggregate is written beside the log, not into the tree, so no free-text question ever
reaches a tracked file.

That property is asserted **by path**, not by a clean `git status`: a status is also clean when a
write was merely hidden by an ignore rule. `sys.dont_write_bytecode = True` sits above the
`sys.path` insert in `query.py`, `selftest.py` and `recall_conf.py` for exactly this reason — without
it, importing the sibling modules drops `__pycache__` next to the source, inside the adopter's tree.
An adopter therefore needs **no** `.gitignore` entry from this kit.

The cache is not small: upstream measures ~115 MiB per live worktree against a 40 MB corpus, and only
37.9% of a 552.6 MB tree was evictable by liveness alone — which is why the budget is a size, not an
age. Two passes run after a successful build, never before (a cache is replaceable only once its
replacement exists):

1. **dead-worktree eviction**, unconditional and free: a sibling whose recorded `worktree` no longer
   exists goes. A cache with **no readable manifest** is never evicted — that is the shape of a
   sibling mid-first-build.
2. **the byte budget**, `RECALL_CACHE_BUDGET_MB` in `.memory-tree.conf`. **Absent** = the kit's

`RECALL_EXTRA_SOURCES` — space-separated, repo-RELATIVE files whose `KEY=value` declarations join
the corpus as chunks, each carrying the comment block above it. Blank or absent is the pre-widening
corpus exactly; a declared file that does not exist is skipped with one line. **Declared, never
globbed** — corpus membership is a decision about what counts as an answer. Note for adopters: a
file you name here is INDEXED, so do not name one holding secrets.
   default, 512 MB; **blank** = uncapped. Eviction is least-recently-built first by `built_at`, and
   it stops the moment the tree is under budget. Three directories are never candidates: the current
   worktree's cache (evicting it makes the budget a rebuild loop), one that is **mid-build** — a
   database newer than its manifest, which is true during a *re*build too, when the previous manifest
   is still readable — and one whose manifest has no `built_at`. When the budget cannot be met
   without reaching past them, the shortfall is reported and **nothing** is deleted.

Every eviction prints one line naming the worktree and its `built_at`. A cache that vanishes silently
is indistinguishable from one that was never built.

## Adopt (per project)

1. Copy this directory to your repo root as `memory-recall/` and make sure `.memory-tree.conf`
   exists (the memory-tree kit owns it — this one refuses rather than creating it).
2. `bash tools/memory-recall/adopt-memory-recall.sh --scaffold` renders the Skill from the conf into
   `.claude/skills/memory-recall/SKILL.md`. Add `--with-hook` only if you want the `recall-opened`
   PostToolUse hook; skipping it is a supported end state, not a gap. With `--with-hook`, finish
   the wiring:
   `python3 settings-merge.py --fragment tools/memory-recall/recall-opened.fragment.json`.
3. **Wire both legs into your local gate runner AND your CI config**, grep-guarded so a re-run does
   not duplicate them. Without this the skill-drift check silently never runs:
   `python3 tools/memory-recall/selftest.py` and `bash tools/memory-recall/adopt-memory-recall.sh --check`.
   The `--check` leg resolves its own interpreter by RUNNING each candidate — `RECALL_PY` first if
   set, then `GOV_PYTHON`, then `python3`, `python`, `py` — so a `python3`-only adopter needs no
   extra step, and a Windows box where the Store `python3` stub answers `command -v` and exits 9009
   still resolves. A gate runner's argv rewrite cannot reach a `bash` leg.
4. Re-run `--scaffold` after any `FAMILIES` or `MEMORY_ROOT` edit. `--check` reds until you do.

## The Skill, and the optional hook

The Skill is **rendered from the conf, not copied**. Its `description` is the entire trigger
mechanism and it names project values — the id families, the query-script path, the corpus root —
and a description is matched *before* the skill runs, so those values have to be in the file. That
is also why it is project-local rather than a per-machine junction: one machine working on two
projects needs two descriptions. `--check` re-renders and diffs, so a `FAMILIES` edit nobody
re-rendered is a red leg instead of a silently stale trigger.

Three things about that description are pinned by `selftest.py`, because breaking any of them is
silent. It **augments** Grep and Glob rather than replacing them, so ordinary code search still
goes where it already worked. Every flag it prints is one `query.py` actually parses (the flag set
is imported from `query.py`, not restated). And it claims nothing about a numbered `/session-kickoff`
step — upstream's clause named a step that issues this query in *its* repo, which ported verbatim
would suppress the tool at the exact moment it exists for.

The `recall-opened` hook is **opt-in**. It appends one `opened` row per query saying which rank the
caller actually read, stamped `inferred: true`, and it is the only instrument that can answer
"did the answer get shown". It ships dark: no `--with-hook`, no file — so `check-wiring.sh` reports
three honest states (kit not adopted · opt-in not taken · present but unmerged = UNWIRED) instead of
a permanent false alarm. Membership is decided by the log's `shown_paths` array rather than a
`memory/` literal, so it works on any `MEMORY_ROOT`.

## The recall floor (gov-only)

`check-recall.py` grades a committed question set and exits non-zero when retrieval falls below a
declared pin. It exists because `bench.py` computes every metric and ALWAYS returns 0 — its flag set
is closed and `verbatim.json` pins it byte-for-byte — so the exit code has to live beside it. This
program imports its scoring functions and edits nothing.

```bash
python check-recall.py                  # the merge-bar leg
python check-recall.py --audit-fixture  # per-question homes, hits and overlap, plus the derivation
python check-recall.py --data-dir DIR   # grade an already-extracted dir (what the arms use)
```

**The pin names a CELL, as one token**, because `bench.py` emits a matrix that spans 0.17 to 0.83 in
a single run and a bare scalar names none of it:

```
RECALL_FLOOR="records:fts5:r@5>=0.81"
```

`fts5` because `query.py` ranks with `bm25(d, 1.0, 1.0, ALIAS_WEIGHT)` and bench's `fts5` is that
same unweighted expression — the reason is the source, not a score. The value is compared against the
CEILING-NORMALISED figure, which reduces exactly to `h/R`: `h` questions that hit, `R` whose targets
resolve at all.

**0.81 is DERIVED, not observed.** Measured `h=10`, `R=12`, normalised 0.8333. The one-retirement
worst case is `(h-1)/(R-1) = 0.8182`, so the pin sits just below it and the property it buys is that
retiring one hitting record costs nothing. Retiring a NON-hitting one raises the score. A regression
with no retirement (`9/12 = 0.75`) reds. Re-measure with `--audit-fixture`, which prints `h`, `R` and
`(h-1)/(R-1)` beside the declared value. It reds in ONE direction — when the pin has become LOOSER
than the worst case, i.e. unsafe. A pin left merely conservative is caught by the arms, which assert
the literal `h=10 R=12`.

**Two predicates, and each can red ALONE** — two checks that only ever fail together are one check
wearing two names. `test_recall_floor.py` proves both directions on this corpus:

| degradation | per-id | floor |
|---|---|---|
| drop one home of a multi-homed HITTING target | ok | RED (0.7500) |
| retire a NON-hitting target entirely | RED, names the id | ok (0.9091) |
| retire a HITTING target entirely | RED, names the id | ok (0.8182 — the derived headroom) |
| drop the whole record file | RED | RED (0.2000) |

**The fixture must not be a tautology.** Every question carries a `from` naming the record a person
wrote that states its answer, and `--audit-fixture` measures content-term overlap against the union
of the target's homes, redding above `OVERLAP_MAX`. A question copied from its own record scores
~1.0 there; this set measures max 0.500.

**None of this ships.** `kit.toml` withholds `recall-fixture.json`, `check-recall.py` and
`test_recall_floor.py` through a `project-owned` rule claiming their destinations. A question set
keyed on one repo's record ids grades nothing in another, and a floor copied from a foreign corpus is
the same defect as a pin copied from one. An adopter who wants a floor authors their own fixture and
measures their own value.

## Maintenance — three categories, three different stories

- **Verbatim** — `bench.py`, `union.py`. Zero coupling on the query path, so they are re-pulled
  **wholesale** from upstream on any fix and never merged. Two caveats, stated rather than patched
  out, because patching them would end the wholesale re-pull: their usage strings name the *upstream*
  script path (`scripts/recall/bench.py`), and `bench.main()` / `union.main()` are the upstream
  benchmark harnesses, which are **inert here** — they need a graded `fixture.json` that this kit
  deliberately does not ship. `selftest.py` pins both files' digests, so an edit reds.
- **Forked** — `extract.py`, `query.py`, `recall-opened.js`. Each carries a header naming the
  upstream path and the sha it was taken from, and enumerates its edits, so a re-pull is a
  three-way merge rather than archaeology.
- **New** — `recall_conf.py`, `selftest.py`, `adopt-memory-recall.sh`, `SKILL.template.md`,
  `recall-opened.fragment.json`, `recall-opened.test.sh`, this README.

## Notes

- **No alias data ships.** The alias *mechanism* does: `extract.load_aliases` treats an absent
  default as a legal alias-free corpus, and `bench.build_index` writes an empty third FTS5 column.
  Upstream's `aliases.json` is 915,515 bytes of questions authored against *its* corpus and joined by
  id, so none of it transfers. Drop your own `aliases.json` in this directory and it is picked up
  with no config edit — the cache rebuilds on the digest change.
- **Zero records is diagnosed, never reported as success.** The chunk arm is family-blind and works
  with no configuration; the record arm is the only consumer of the id grammar. Point `FAMILIES` at a
  corpus it does not describe and the un-forked upstream prints `index 0 records + N chunks` and
  exits 0. This kit prints a `ZERO RECORDS` diagnosis naming the resolved families, the conf path and
  `--rebuild`, on the query path and on `extract.py`'s own.
- **On a small corpus, retrieval buys precision, not speed.** Measured on this repo — 66 tracked
  corpus files, 496,153 bytes, 9 anchored records, 1,033 chunks — a full-corpus
  `grep -rIl "adopt" memory/` takes 0.077 s / 0.092 s / 0.447 s across three warm runs and returns
  31 of 66 files. The kit's index build is 0.18 s and a warm query is 1.58–2.27 s wall, dominated by
  interpreter start-up and `git` calls, so it is **slower** than the grep at this size. What it
  returns is a ranked handful instead of half the tree. Adopt it for the ranking, not the clock;
  upstream's 40 MB corpus is where the 6 s cold build starts paying for itself.
