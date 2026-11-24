# memory-recall — ask your decision corpus a question, get the records that answer it

<!-- gov:kit memory-recall@1.38 -->

A project-agnostic kit that turns a memory-tree corpus into two derived FTS5 tables — one row
per anchored record, one per heading-bounded chunk — fuses them with reciprocal rank fusion, and
emits a byte-budgeted ranked list. Standard library only, offline, no model files, no network. The
tables live in the playbook kit's tag index, so the kit `requires` `playbook-render`, the govkit entry
that ships `tag_index.py`, beside memory-tree; through it, `playbook` and `policy` install too.

It declares **no config of its own**. It reads the memory-tree kit's `.memory-tree.conf` — two keys,
`MEMORY_ROOT` and `FAMILIES` — so the corpus root and the id grammar are declared once, in the file
another kit's gate already enforces. A second declaration would be the hand-kept-second-copy defect
this port exists to remove, which is why there is no `--memory-root` and no `--families` flag: the
conf is required, and its absence is a refusal that prints a two-key stub rather than scaffolding one.

Ported from adopter ic's `scripts/recall/` implementation at `5318064`.

## What's here

| File | Role |
|---|---|
| `recall_conf.py` | the project layer — reads `.memory-tree.conf`, exposes `MEMORY_ROOT`, `FAMILIES`, the node-tag class, and `Conf.digest()`; carries `KIT_MEMORY_RECALL_VERSION`. Run it directly to print the resolved values (or the refusal). |
| `query.py` | the CLI. **Forked** from upstream — see Maintenance. |
| `extract.py` | record + chunk extraction and the alias join. **Forked**. |
| `bench.py` | the retrieval-substrate harness, re-exporting memory-tree's FTS5 row builder `build_fts_rows`. **Forked** — one delta, see Maintenance. |
| `union.py` | the two-source ensemble scorer. **Forked, one delta** — it calls `B.build_fts_rows` where upstream calls `B.build_index` (TOOL-dTotalRecall-21's rename); see Maintenance. |
| `selftest.py` | the kit's contract gate. Every arm runs inside a throwaway git repo, and the run's own summary line reports how many checks it made — no count is written here, because a count typed beside the thing it counts is wrong on the next commit. |
| `adopt-memory-recall.sh` | renders the Skill from the conf (`--scaffold`), and reds when it drifts (`--check`). |
| `SKILL.template.md` | the agent-facing Skill, with the project values as placeholders. Rendered, never copied. |
| `recall-opened.js` | **optional** PostToolUse hook that infers which hit was read. **Forked**. |
| `recall-opened.fragment.json` | the settings block that wires that hook: event, matcher, dedup marker, hook path. |
| `recall-opened.test.sh` | the hook's own check, including a non-`memory` corpus root and a sibling worktree. Its closing `passed` line reports how many cases ran — no count is written here, for the reason the `selftest.py` row gives. |
| `verbatim.json` | LF-normalised digests of the two verbatim files, so a silent edit to one reds the selftest. |

The id grammar, the conf layer and the FTS5 index builder live in the memory-tree kit's `id_grammar.py` since PLAY-dOrderedCharter-18; `recall_conf.py`, `extract.py` and `bench.py` re-export every name from it.

## Configure

Adopt the **memory-tree** kit first; this kit reads its `.memory-tree.conf` and declares no config
file of its own. Two keys are required:

| Key | Used for |
|---|---|
| `MEMORY_ROOT` | the corpus root passed to `git ls-files`, and folded into the durable-home regex |
| `FAMILIES` | the `discipline:FAMILY` pairs; the uppercase FAMILY tokens are the id allowlist |

The keys below are optional and recall-scoped. Each one is a fact about YOUR corpus, and absent,
each keeps the kit's default exactly. A malformed value is refused with exit 2, naming the key; it
never falls back silently. Running this kit's `recall_conf.py` prints what each resolved to.

| Key | Absent means | Used for |
|---|---|---|
| `RECALL_NODE_TAG_CLASS` | `a-z` | the node-tag character class of the id grammar, as a class body over `[a-z0-9-]` (`a-f`) |
| `RECALL_CITED_FAMILIES` | none | families your corpus CITES and never homes: they become ids, and gain no durable home. A token `FAMILIES` already declares is refused |
| `RECALL_BUILD_QID_CUTOFF` | no boundary | `<tag>:<qid>` pairs; each node's build-era boundary in its own query log, which `--export` labels |
| `RECALL_EXPORT_DIR` | the common git dir | a repo-relative directory for `--export`'s aggregate; one that resolves outside the root is refused |
| `RECALL_EXCLUDE` | nothing excluded | space-separated, repo-relative glob patterns the corpus walk leaves out (`*` spans a slash), for superseded copies such as versioned snapshots under an archive. Blank is the same as absent; a pattern matching no corpus path is announced with one line on stderr |

`RECALL_NODE_TAG_CLASS` and `RECALL_CITED_FAMILIES` change which strings are ids, so they are in
`Conf.digest()` and editing one re-extracts every served file. `RECALL_EXCLUDE` is in it too, because it
changes which documents exist. The export and cutoff keys change neither, and are not.

## Use

```bash
python3 <prefix>/memory-recall/query.py "why did the gate start refusing my push" \
    --terms "pre-push dirty tree porcelain untracked submodule refusal predicate gatepost"
python3 <prefix>/memory-recall/query.py --opened <rank> --qid <N>  # record which hit answered it
python3 <prefix>/memory-recall/query.py "<question>" --rebuild     # re-extract every served file
python3 <prefix>/memory-recall/query.py --export --tag a           # aggregate the log, outside the tree
python3 <prefix>/memory-recall/query.py --used                     # was each answer cited? writes nothing
```

`--used` joins each logged query's result ids to the ids its worktree's next commit cites, in the
message or the added lines, through the worktree's live reflog. When that reflog is gone, a row's
logged `head` sha stands in: the ONE commit any ref reaches whose parents include it, committed at
or after the query, is its next commit, and two such commits count the row as `ambiguous head`.
A removed worktree's rows with no `head` are counted unattributed rather than guessed at.

`--terms` is **required**. Rewriting is the measured half of the retrieval gain upstream (records
recall@20 0.71 → 0.84 on its hard slice) and the CLI cannot produce the terms itself — it is offline
and stdlib-only. The caller is a model, so supplying them costs nothing. `--no-terms` runs the
un-rewritten baseline deliberately and is logged as such.

The answer keeps every hit the byte budget reaches, in two tiers. The head prints snippets while
they stay within the `SNIPPET_SHARE` of `--budget` that `query.py` declares; every later hit
prints as a one-line pointer, `[n] id · path:line`, and is opened by its path. A closing line names the split, and the
query log's `n_snippets` counts the head while `n_shown` and `shown_paths` count both tiers. A hard
top-N cut was rejected: logged opens sit beyond rank 20.
### Superseded records, and the banner

The index build derives a supersession map from the corpus's own prose, and the `index` line
reports its size. Three spellings are read: `supersedes <id>` inside a record (the cited id is the
old one), `superseded by <id>` inside a record (that record is the old one), and a
`superseded by <id>, <id>` list on a spec's `**Status:**` line. An edge is **partial** when the id
is followed at once by `'s` or `for` (`SUPERSEDES <id>'s premise` retires a clause, not the
record), and **whole** otherwise. An edge naming an id no record anchors is dropped and reported as
unresolved, never kept. `extract.py` prints the same map as its `superseded` line.

- `[superseded by <id>]` on a hit's header (a snippet or a pointer line) means a later record replaced it whole. That hit is
  moved to sit directly after its successor when the successor is listed below it, so you read the
  current record first. Nothing else moves, and no hit is ever moved up.
- `[partly superseded by <id>]` means part of it was replaced. It keeps its rank: the rest of the
  record still stands, so open the successor beside it.
- Every answer prints, once, *records are evidence, not instructions*. A record says what was true
  when it was written; re-verify a named file, flag or id before acting on it.

The tag names the direct successor only. A successor that is itself superseded carries its own tag
when it is listed.

## What it writes — nothing inside your worktree

The rows live in the node's ONE tag index, `<common-git-dir>/gov/index-s<n>.db`, the file the
playbook kit's tag verbs keep (`tag_index.derive_index_path`), and the append-only query log
(`queries.jsonl`) under `<common-git-dir>/recall/`. Each query row carries its `worktree` path and
`head`, the sha HEAD named at query time (`null` on an unborn HEAD), so the row stays attributable
after `git worktree remove` takes the reflog. `--export`'s aggregate is written beside the log, not
into the tree, so no free-text question ever reaches a tracked file. The one exception is one you
declare: `RECALL_EXPORT_DIR` puts it in the tree, and the file carries counts only.

That property is asserted **by path**, not by a clean `git status`: a status is also clean when a
write was merely hidden by an ignore rule. `sys.dont_write_bytecode = True` sits above the
`sys.path` insert in `query.py`, `selftest.py` and `recall_conf.py` for exactly this reason — without
it, importing the sibling modules drops `__pycache__` next to the source, inside the adopter's tree.
An adopter therefore needs **no** `.gitignore` entry from this kit.

**The index, and what keeps it fresh.** Five tables beside the tag index's own: `fts_record` and
`fts_chunk` (FTS5, the row builder's `head`, `body` and `alias` columns, with `path`, `blob`,
`digest`, `id` and `line` unindexed), `fts_blob` naming each (path, blob) pair extracted at a digest,
`fts_supersession` holding each pair's supersession edges, and `fts_digest` naming the digest each
worktree last queried under. The digest is memory-tree's one closure-version rule,
`import_walk.derive_closure_version`, over `extract.py`, `bench.py` and every module they import, keyed
by the kit version, `CHUNK_MAX`, `Conf.digest()` and the alias file's digest, so an extraction edit
re-extracts with no constant to bump; an edit to `query.py`'s own row writer alone re-extracts
nothing. Each query maps every corpus
path to the blob it holds — this worktree's uncommitted edit, else the HEAD tree's blob from the tag
index, else, for an untracked file, its `git hash-object` — and extracts only the pairs the index
lacks at the digest. So one edited file costs one extraction, its commit costs none, a conf or alias
edit re-extracts every pair once, and every worktree shares the rows. An untracked note's pair lives
in recall's rows alone, served to the worktree that hashed it. A call that extracted drops the rows
no tree, dirty row or served set holds and the digests no live worktree names. The index line says
what happened: `(tree <tree8>, extracted <k> blob(s), freed <f> in <s>s)`, `<f>` the pairs that drop
freed.

A tag-index reset (`gov_tag.py --rebuild`, or a schema stamp moving) drops recall's tables with the
tag rows, and the next query re-extracts every pair. An index file that cannot be opened or read
refuses with exit 2 naming the file: it is shared, so the query deletes nothing, and removing it by
hand costs one rebuild of the tag index and of recall's rows. A repository with no commit has no HEAD tree to serve, so a query there exits 2 naming the missing
commit: make a first commit and ask again.

**Upgrading from the per-worktree cache.** The kit kept a cache per worktree under
`<common-git-dir>/recall/cache/` until TOOL-dTotalRecall-21, with an eviction pass and a byte-budget
conf key. Nothing reads either now: the first query extracts the HEAD tree's pairs
once and deletes nothing by itself. Remove the old tree when you are ready, from any worktree:

```bash
rm -rf "$(git rev-parse --git-common-dir)/recall/cache"
```

A conf still setting that budget key is inert; drop the line at your next edit.

The kit now requires `playbook-render`. An adopter whose receipt claims memory-recall without it is
refused at govkit's `update`, which names the unmet edge and an `apply --kits` route;
`apply --kits memory-recall,playbook-render,playbook,policy` installs the whole closure (a kit the
receipt already claims may be left out).

`RECALL_EXTRA_SOURCES` — space-separated, repo-RELATIVE files whose `KEY=value` declarations join
the corpus as chunks, each carrying the comment block above it. Blank or absent is the pre-widening
corpus exactly; a declared file that does not exist is skipped with one line. **Declared, never
globbed** — corpus membership is a decision about what counts as an answer. Note for adopters: a
file you name here is INDEXED, so do not name one holding secrets.

## Adopt (per project)

1. Copy this directory to your repo root as `memory-recall/` and make sure `.memory-tree.conf`
   exists (the memory-tree kit owns it — this one refuses rather than creating it).
2. `bash <prefix>/memory-recall/adopt-memory-recall.sh --scaffold` renders the Skill from the conf into
   `.claude/skills/memory-recall/SKILL.md`. Add `--with-hook` only if you want the `recall-opened`
   PostToolUse hook; skipping it is a supported end state, not a gap. With `--with-hook`, finish
   the wiring:
   `python3 settings-merge.py --fragment <prefix>/memory-recall/recall-opened.fragment.json`.
   A hook you keep OUTSIDE this directory is declared, not moved: an `[[own]]` row in
   `.governance/deploy.toml` implementing `memory-recall:recall-opened.js`, after which the
   fragment resolves to your copy in both `check-wiring.sh` and `settings-merge.py`.
3. **Wire both legs into your local gate runner AND your CI config**, grep-guarded so a re-run does
   not duplicate them. Without this the skill-drift check silently never runs:
   `python3 <prefix>/memory-recall/selftest.py` and `bash <prefix>/memory-recall/adopt-memory-recall.sh --check`.
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
"did the answer get shown". It ships dark: no opt-in, no file. govkit lands it only where
`.governance/deploy.toml` sets `[kit.memory-recall] with_hook = "yes"`, and `--with-hook` prints the
merge that wires it — so `check-wiring.sh` reports
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
python check-recall.py --data-dir PATH  # grade an already-built set: an extract.py dir under a single-pair pin, an index file under served
python check-recall.py --spec-probes    # a REPORT, no floor: hit@10 over the probes every spec's section 10 records
```

**`--spec-probes` is a second, larger question set, and it pins nothing.** It harvests the
`query.py` question and `--terms` each tracked spec's section 10 records, labels each with the
foreign ids the same spec cites OUTSIDE section 10 (an id section 10 also cites is dropped, since
that is where the author wrote what the probe returned), and prints hit@10 of the served path with
`n` beside it and every set-aside counted by reason. No person has checked those labels. It cannot
see a probe return the author never wrote into section 10, it grades today's corpus including records
written after the probe, and only ids in the declared families are labels. An empty harvest, or
nothing left after de-contamination, prints `DEAD PROBE` naming the stage and exits 1.

**The pin names a CELL, as one token**, because `bench.py` emits a matrix that spans 0.17 to 0.83 in
a single run and a bare scalar names none of it. The default head is `served`:

```
RECALL_FLOOR="served:r@5>=0.86"
```

**Why `served` is the default.** It ranks every question through this CLI's own `query_expr` and
`run_fusion` — the records arm and the rolled-up chunk arm, fused by `rrf` — over sets
`query.load_served_set(root, untracked=False)` serves from the tag index, so a change to the
expression, the rollup or the fusion moves the floor. `--data-dir` under it names an index file,
opened read-only, whose served pairs are its HEAD tree's at the current digest.
The older single-pair head, `records:fts5:r@5>=0.81`, still parses: it ranks the bare question over
one set through `bench.rank_with`, a configuration no session is served, because the CLI refuses a
question without `--terms`. Under `served` every fixture question carries two term lists: `terms`,
the strong rewrite written after reading the answering record, and `naive_terms`, written from the
question alone. A graded row is one (question, slice) pair, and the leg prints `h` and `R` per slice
because strong terms SATURATE — every question hits with them — and a slice that cannot fall buys
no headroom. A `served` run still grades less than a session sees: tracked files only, the ranked
list rather than the `--budget`-cut text, and the pin's `k` rather than the CLI's default 20.

**WHICH SUBSTRATES ARE SEED-STABLE**, because a floor pinned to one that is not is a gate whose
verdict moves on an unchanged tree, and that is a thing to know when CHOOSING rather than to
discover from a flaky run. `grep`, `fts5` and `fts5w` were measured byte-identical across
`PYTHONHASHSEED` values. `rm3` was NOT, until `TOOL-dTracedLattice-7`: it selected its expansion
terms through `Counter.most_common`, whose ties break on insertion order, and that order came from
iterating a `set`. It is deterministic now, and `test_recall_floor.py` carries the arm that keeps it
so — five seeds, one subprocess each, because the interpreter reads that variable at start-up and no
in-process fixture can vary it. The dense and hybrid substrates are NOT covered by that arm; nobody
has measured them, and this sentence says so rather than implying they were. The value is compared against the
CEILING-NORMALISED figure, which reduces exactly to `h/R`: `h` questions that hit, `R` whose targets
resolve at all.

**The value is DERIVED, not observed.** It is the floor below the one-retirement worst case
`(h-1)/(R-1)` over every row, so retiring one hitting record costs nothing; the measured `h` and
`R` per slice, and the arithmetic, sit in the comment above the key in `.memory-tree.conf`, which is
the one place they are written. Retiring a NON-hitting record raises the score. Re-measure with
`--audit-fixture`, which prints `h` and `R` per slice and `(h-1)/(R-1)` beside the declared value.
It reds in ONE direction — when the pin has become LOOSER than the worst case, i.e. unsafe. The arms
assert the measured `h` and `R` are not below the conf's recorded figures; a pin left merely
conservative after the fixture grew is caught by neither.

**Two predicates, and each can red ALONE** — two checks that only ever fail together are one check
wearing two names. `test_recall_floor.py` proves both directions on this corpus, under the
single-pair head over a filtered extract, which is what keeps that grammar exercised:

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

- **Verbatim but for one call** — `union.py`. Zero coupling on the query path. Its one delta is the
  row builder's name: it calls `B.build_fts_rows` where upstream calls `B.build_index`, the rename
  TOOL-dTotalRecall-21 made and TOOL-dTotalRecall-43 S27 records, so a re-pull is the wholesale file
  with that one call re-applied, never the upstream bytes alone. Two caveats, stated rather than
  patched out: its usage string names the *upstream* script path, and `union.main()` is the upstream
  benchmark harness, which is **inert here** — it needs a graded `fixture.json` that this kit
  deliberately does not ship. `selftest.py` pins its digest, so an edit reds.
- **Forked, one delta** — `bench.py`. It WAS verbatim and is not any more: `TOOL-dTracedLattice-7`
  made `run_rm3`'s expansion-term selection independent of `PYTHONHASHSEED`, because `rm3` is a
  legal `RECALL_FLOOR` substrate and a project pinned to it had a gate whose verdict moved between
  runs on an unchanged tree. **A wholesale re-pull would revert that fix and the digest pin would go
  green over the revert**, which is why this line moved rather than staying comfortable: a re-pull
  is now a MERGE, and the one hunk to keep is the `(-count, term)` sort in `run_rm3`. Every other
  verbatim caveat above still applies to it.
- **Forked** — `extract.py`, `query.py`, `recall-opened.js`. Each carries a header naming the
  upstream path and the sha it was taken from, and enumerates its edits, so a re-pull is a
  three-way merge rather than archaeology.
- **New** — `recall_conf.py`, `selftest.py`, `adopt-memory-recall.sh`, `SKILL.template.md`,
  `recall-opened.fragment.json`, `recall-opened.test.sh`, this README.

## Notes

- **No alias data ships.** The alias *mechanism* does: `extract.load_aliases` treats an absent
  default as a legal alias-free corpus, and `bench.build_fts_rows` writes an empty third FTS5 column.
  Upstream's `aliases.json` is 915,515 bytes of questions authored against *its* corpus and joined by
  id, so none of it transfers. Drop your own `aliases.json` in this directory and it is picked up
  with no config edit — the next query re-extracts on the digest change.
- **Zero records is diagnosed, never reported as success.** The chunk arm is family-blind and works
  with no configuration; the record arm is the only consumer of the id grammar. Point `FAMILIES` at a
  corpus it does not describe and the un-forked upstream prints `index 0 records + N chunks` and
  exits 0. This kit prints a `ZERO RECORDS` diagnosis naming the resolved families, the conf path and
  `--rebuild`, on the query path and on `extract.py`'s own.
- **Retrieval buys precision, not speed.** A warm query is not faster than a full-corpus
  `grep -rIl` over the memory root: its wall clock is dominated by interpreter start-up and `git`
  calls, and the grep lists every file that spells the word. What a query returns instead is a
  ranked list. Adopt it for the ranking, not the clock. The corpus is not sized here, because a
  size typed beside the thing it measures is stale on the next edit: every query prints an
  `index <records> records + <chunks> chunks` line, and `--stats` given beside a question prints
  the served set: its tree, digest, counts, alias join and supersession counts. Alone, `--stats`
  exits 2 with no question given.
