# TOOL-aQuarriedLantern-1 — memory-recall: the retrieval CLI as a project-agnostic kit

**Status:** INPROGRESS · rev-2 · 2026-08-03 · node a · Tier-2 · base 9368d1e8 · ratified 2026-08-03 · U1-U3 built, closing review folded; NOT CLOSED — §8 Q6 is deliberately open

## 1. Goal

Port the working memory-tree retrieval CLI from the inCMS repo (the scripts/recall folder, records
ARCH-aTemperedLoom-1..-4 and ARCH-aGrittedFlagstone-3/-6) into this repo as a copy-in kit at
`tools/memory-recall/`, so any adopter project gets "ask the decision corpus a question and get the
records that answer it" without re-deriving the index, the ranking, or the caching. The port earns
its keep only if it reads the project layer that already exists — `.memory-tree.conf` — instead of
shipping a second declaration of the corpus root, the disciplines and the id families.

## 2. Scope (IN)

- **S1** — `tools/memory-recall/` kit directory carrying `recall_conf.py`, `extract.py`, `bench.py`,
  `query.py`, `selftest.py`, `SKILL.template.md`, `adopt-memory-recall.sh`, `README.md`, the hook
  `recall-opened.js`, its test `recall-opened.test.sh`, and the settings fragment
  `recall-opened.fragment.json`. The fragment ships inside the kit directory because S11 makes
  `tools/check-wiring.sh` resolve it by path in an adopter, so it cannot live outside what the
  adopter copies.
- **S2** — `recall_conf.py`: reads `.memory-tree.conf` from the repo root and exposes `MEMORY_ROOT`,
  `FAMILIES` (the uppercase family tokens), and the node-tag character class; exposes
  `conf_digest()` over those three RESOLVED values for S6; carries
  `KIT_MEMORY_RECALL_VERSION = "1.0"` as the kit's version constant and the `gov:kit
  memory-recall@1.0` marker.
- **S3** — `extract.py` forked so `FAMILIES`, the node-tag character class inside `ERAS`, the
  `DURABLE` path regex and `corpus_files()` derive from `recall_conf`, with the upstream sha the
  fork was taken from recorded in a header comment.
- **S4** — `bench.py` copied **byte-identical** (measured: zero coupling on the query path), so it
  can be re-pulled wholesale. Its two usage strings name the upstream script path and are left
  as upstream spellings; the README says so.
- **S5** — `query.py` forked with five edits, each named here because the build must not discover
  them at the keyboard:
  1. `corpus_files()` derives from `recall_conf`.
  2. `sys.dont_write_bytecode = True` immediately above the `sys.path` insert, so importing the
     sibling modules writes no `__pycache__` inside the adopter's worktree.
  3. Every printed invocation derives from `__file__` relative to the repo root as one expression,
     reused by the module docstring usage block, the `REFUSAL` text and the qid hand-back line.
  4. `--export` keeps its aggregation but writes beside the query log under the common git dir
     instead of inside the worktree, and its node-registry lookup is removed — `--tag` becomes
     required for `--export` and refuses when absent.
  5. `--rebuild` is documented in `--help`; it exists upstream but is undiscoverable there.
- **S6** — cache manifest and eviction. The manifest gains two fields: `worktree` (the absolute path
  the cache was built for) and `conf_digest` (S2). `conf_digest` joins the `fresh` predicate in
  `ensure_cache`, so an id-grammar or corpus-root change invalidates the cache the way an alias
  change already does. A build deletes sibling cache directories whose recorded `worktree` no longer
  exists. A cache directory with no readable manifest is **never** evicted.
- **S7** — a loud diagnosis for the mis-declared-families failure: when the records document set is
  empty while the chunks set is not, the CLI prints which conf key produced no anchors, the conf
  path, and `--rebuild` as the escape hatch for a cache built before the conf was fixed.
- **S8** — refusal when `.memory-tree.conf` is absent, naming the memory-tree kit as the
  prerequisite, printing a copy-pasteable two-key conf stub, and scaffolding nothing.
- **S9** — `adopt-memory-recall.sh` with `--scaffold`, `--check` and `--with-hook`: renders
  `SKILL.template.md` into `.claude/skills/memory-recall/SKILL.md` from the conf and converges
  idempotently; `--check` exits non-zero when the rendered skill has drifted from the conf. The hook
  file is copied to `.claude/hooks/` **only** under `--with-hook`. The script resolves its
  interpreter by probing `python3` first and falling back to `python`, with a `RECALL_PY` override.
- **S10** — `tools/settings-merge.py` generalised to `--fragment FILE` so it can wire a second hook,
  plus the shipped `recall-opened.fragment.json`; the existing agent-cap behaviour stays the default
  and stays byte-identical on a re-run.
- **S11** — `tools/check-wiring.sh` gains a `recall-opened` arm delegating detection to
  `settings-merge.py --check --fragment`, with a three-state result: kit absent, hook file absent
  (opt-in not taken), hook file present but unmerged (UNWIRED).
- **S12** — `selftest.py`: the kit's own contract gate, fixture-driven, run entirely inside throwaway
  repos, wired as a leg in `tools/gate-legs.json`; plus `recall-opened.test.sh` alongside the hook,
  matching `agent-cap.test.sh`. `selftest.py` also sets `sys.dont_write_bytecode = True`, since it
  imports the same modules.
- **S13** — registrations: `tools/gate-legs.json` legs, a `tools/check-kit-versions.sh` entry, a
  `WIRE-INTO-PROJECT.md` section **including a numbered adopter gate-wiring step**, an optional-kit
  bullet plus a §0 decision row in `parallel-coding-governance.template.md`, a memory-recall probe
  paragraph in `skills/session-kickoff/SKILL.md` Step 4, an `AGENTS.md` kit-list and gate-suite line,
  and this repo's own dogfood adoption (its `.claude/skills/memory-recall/SKILL.md` rendered for
  `PLAY KICK TOOL DEPL`).

## 3. Non-goals (OUT)

- The alias **data**. The upstream `aliases.json` is 915,515 bytes of questions authored against the
  inCMS corpus and joins by id; no id in it exists anywhere else. The alias **mechanism** ships
  (S2–S5) and the empty-alias state is first-class.
- The measurement instruments: `alias_bench.py`, `rewrite_bench.py`, `redundancy.py`, `ceiling.py`,
  `session_stats.py`, `agent_queries.py`, `merge_fixture.py`, `alias_distinct.py`, `ci.py`,
  `union.py`, and `grep_study.py`.
- The upstream `fixture.json` — 184 graded queries whose expected ids are inCMS ids.
- The recall-floor gate (`check_recall.py` and `check-recall.sh` upstream). It grades a fixture no
  adopter has. §7 states what gates this kit instead.
- The corpus-integrity classifier `corpus_ids.py`. It is 1,845 lines that wire six hygiene checks
  upstream, and every one of them is a statement about the memory **tree**, not about retrieval. It
  belongs to the memory-tree kit; a later port would depend on this kit, because it imports
  `extract.py`. Not this unit.
- A per-machine skill junction. §4 explains why this skill is project-local.
- Rewiring the three existing Python-launcher detectors in this repo. §4 takes the launcher decision.
- A per-worktree cache size cap or an LRU eviction policy. §5 states the measured ceiling this leaves
  standing and files it as a backlog row.
- Changing this repo's `.gitignore`. It already carries `__pycache__/` and `*.pyc` on lines 1–2. That
  is not the guarantee, though: S5's `sys.dont_write_bytecode` is, because an adopter without those
  two lines gets a dirty tree from a read-only query. The wiring doc states the dependency.

## 4. Design

### Measured coupling inventory

Every row below was read from source at C:/projects/incms/main, not inferred. Two greps produced it,
because one could not: `grep -c "memory/" scripts/recall/*.py` finds the corpus root, and
`grep -n "scripts/recall" scripts/recall/query.py scripts/recall/bench.py` finds the second baked-in
project literal — the script's own path, which the corpus-root grep is structurally blind to.

| Where | Coupling | Port |
|---|---|---|
| extract.py:37 `FAMILIES` | 11 hardcoded family tokens (`ARCH DEPLOY BLOCK DES PERF ABL DPL BBL DBL PBL PKG`) | from conf `FAMILIES` |
| extract.py:42-46 `ERAS` | three id eras; the node-scoped and session-scoped eras pin the node tag to `[a-f]` | node class from `recall_conf` |
| extract.py:59-64 anchor regexes | built by concatenation from `ID`, so they follow `FAMILIES` | no edit needed |
| extract.py:75-79 `DURABLE` | `memory/` root plus `DECISIONS`/`BACKLOG`/`decisions/`/`archive/` | root from conf `MEMORY_ROOT` |
| extract.py:109,111 `corpus_files` | `git ls-files memory/` | root from conf |
| extract.py:94 `ALIASES_DEFAULT` | resolves beside the script | no edit needed (see below) |
| query.py:174-175 `corpus_files` | `git ls-files memory/` twice | root from conf |
| query.py:13-16 docstring usage | four invocations naming the upstream script path | derived from `__file__` |
| query.py:134 `REFUSAL` | the invocation a caller sees when they forget `--terms` | derived from `__file__` |
| query.py:608 `--export` header | the invocation printed into the generated traffic file | derived from `__file__` |
| query.py:976 qid hand-back | the `--opened` invocation printed after every successful query | derived from `__file__` |
| query.py:740 `--export` output | `repo/memory/project/recall-traffic-<tag>.md`, inside the worktree | retargeted beside the log |
| query.py:820 `--tag` default | `node_tag()` reads CLAUDE.md's node registry | removed; `--tag` required |
| query.py:63-66 `sys.path` insert | sibling import writes `__pycache__` into the worktree | `sys.dont_write_bytecode` |
| query.py:287-296 `fresh` | five inputs, none of them the id grammar | `conf_digest` added |
| recall-opened.js:81,86 path resolver | literal `memory/` prefix and literal `/memory/` boundary | matched via `shown_paths` |
| bench.py:20,223 usage strings | the upstream script path, in a docstring and a `SystemExit` | left verbatim; README says so |
| bench.py | zero occurrences of the corpus root | byte-identical copy |
| union.py | zero occurrences of the corpus root | excluded anyway (instrument) |
| selftest.py | 174 occurrences | replaced, not ported |

The worst instance is query.py:976. That line prints, after every successful query,
`logged as qid N — record which hit answered it:` followed by an invocation naming the upstream
script path. It is the fix that made `--opened` usable at all. Ported unedited, the kit hands every
adopter an instruction to run a file that does not exist in their repo, so the outcome-recording rate
the hook exists to raise stays at zero by a second route. The spec already knew the script path was a
project value — it templates that path into the skill — but that invariant covered the skill file
only.

The measured consequence of *not* fixing the family coupling is not a crash. Running the unmodified
upstream query path over this repo's corpus returns chunks and zero records, and looks healthy. The
chunk arm is family-blind and works with zero configuration; the record arm silently produces
nothing. Re-measured this session against the current corpus, with a scratch copy of extract.py:

```
$ python -c "... ex.corpus_files(repo, None) ... ex.extract_records(...)"
files: 66
records: 9                          # families PLAY KICK TOOL DEPL, node class a-z
records with UPSTREAM families: 0
chunks @600: 989                    # query.py pins CHUNK_MAX = 600, not extract.py's 2400
```

That silent zero is why S7 exists, and why "just copy it" is not an option.

### Data model

**Config.** The kit declares no config file. It reads the memory-tree kit's `.memory-tree.conf`,
using two of its keys and inventing none:

| Key | Used for |
|---|---|
| `MEMORY_ROOT` | the corpus root passed to `git ls-files` and folded into `DURABLE` |
| `FAMILIES` | the discipline-to-family pairs; the kit takes the uppercase family tokens as its allowlist |

The node-tag character class is not a conf key. Upstream pins it to `[a-f]`, which is narrower than
the gate it lives beside: this repo's `tools/memory-tree/check-memory-hygiene.sh:332` already admits
`node [a-z]`. The kit uses `a-z` and adds no key, so nothing about another kit's contract has to
change. Q1 keeps the alternative open.

**Conf parsing.** `recall_conf.load_conf()` parses the restricted shell grammar the conf documents.
`tools/codebase-map/map_lib.py:86-108` already does exactly this, and its docstring says it is "the
same one-conf-both-worlds format the memory-tree kit uses". It is not importable here: kits are
copied into adopters independently, so importing across kit directories would make memory-recall
un-adoptable without codebase-map. The 20 lines are copied, and the drift is gated the only way that
proves anything — the selftest sources the same conf file **with bash** and asserts the Python parse
matches bash's, over the grammar's documented cases (a quoted value with spaces, an unquoted value
with a trailing comment, an `export` prefix, blank and comment lines). Asserting one Python parser
against another Python parser would be an assertion whose two operands share a generator.

**Cache and its manifest.** Shape unchanged from upstream: a per-worktree directory under the
**common** git dir, holding `records.db`, `chunks.db` and `manifest.json`. The common git dir rather
than `--git-dir`, so `git worktree remove` cannot take the log with it; sub-keyed by a digest of the
worktree path, because two worktrees of one repo hold different corpus content.

The manifest schema changes in one place and two consumers read it, so it is stated once here. Today
`build_cache` writes `version chunk_max n_files counts digest alias_digest built_s built_at`, and
`ensure_cache`'s `fresh` predicate reads five of those plus the two `.db` files existing. S6 adds:

| Field | Written from | Read by |
|---|---|---|
| `conf_digest` | `recall_conf.conf_digest()` — a hash of the RESOLVED `MEMORY_ROOT`, the sorted families tuple, and the node-tag class | the `fresh` predicate |
| `worktree` | the absolute path the cache was built for | the eviction step |

`conf_digest` hashes resolved values rather than the conf file's bytes, so editing a comment in the
conf does not force a 6-second rebuild.

The two features share one failure mode, and it resolves to one predicate in two directions. The
builder writes both `.db` files **before** the manifest, deliberately and atomically, so an
interrupted or in-progress build leaves a directory with no readable manifest. That state means:

- **freshness** — treat as stale and rebuild. This is already upstream's behaviour (`man is not None`
  is the first conjunct) and it stays.
- **eviction** — treat as live and **never** delete. A sibling mid-first-build is exactly this state,
  and evicting it destroys a live cache the builder is still writing.

Stated as one rule: *an unreadable manifest means rebuild mine, never delete theirs.* AC7 gates both
directions.

Why the freshness half is a blocker and not a nicety: the port's whole thesis is moving the id
grammar out of source and into `.memory-tree.conf`, which makes an adopter-editable value a **cold**
input to a **hot** cache. The corpus digest is computed over the memory tree's `.md` files, so a
`FAMILIES` edit never enters it. Two consequences, both proven by experiment in a throwaway repo
carrying the three upstream scripts and a decision file with `ARCH-aFoo-1/-2`. Forward:
run 1 `index 2 records + 1 chunks (rebuilt 2.27s)`, then `FAMILIES` mutated `ARCH`→`ZZZZ` with the
mutation asserted applied, run 2 `index 2 records + 1 chunks (cached …)`. Inverse: `--rebuild` with
the wrong grammar gives `index 0 records + 1 chunks (rebuilt 0.97s)`, and repairing `FAMILIES` back
to `ARCH` then querying plainly gives `index 0 records + 1 chunks (cached …)`. So the S7 diagnosis
would fire, the adopter would fix the conf, and the repair would be a silent no-op. `MEMORY_ROOT`
partially self-heals, because a new root changes the file set and therefore the digest, which makes
the failure look intermittent. The precedent is in the code being forked: the alias digest sits in
the manifest for precisely this reason, because an alias edit "would otherwise leave a stale cache
serving un-joined results with no signal at all".

**Log.** `queries.jsonl` beside the cache, append-only JSONL, one row per query. Fields observed on a
live row: `qid at type query terms rewritten k budget bytes_emitted worktree n_hits n_shown results
shown_paths`. It carries the free-text question and the absolute worktree path, and carries no
username or hostname. Re-measured upstream: 2,414,771 bytes over 676 rows.

### The fork boundary

Three categories, because they have three different maintenance stories.

- **Verbatim** — `bench.py`. Zero coupling on the query path, so it is copied byte-identical and
  re-pulled wholesale on any upstream fix, exactly as `WIRE-INTO-PROJECT.md` says of the memory-tree
  scripts. Its two usage strings do name the upstream script path, so the claim is "zero coupling on
  the query path", not "zero project coupling": the README states that its usage spellings are
  upstream's, which is the price of keeping the wholesale re-pull. Its `main()` is the upstream
  benchmark harness and is inert here without a fixture; the README says so rather than the code
  being trimmed, for the same reason.
- **Forked** — `extract.py`, `query.py`. Each carries a header line naming the upstream path and the
  sha it was taken from, so a future re-pull is a three-way merge rather than archaeology. S5
  enumerates query.py's five edits so none of them is rediscovered mid-build.
- **New** — `recall_conf.py`, `selftest.py`, `SKILL.template.md`, `adopt-memory-recall.sh`,
  `README.md`, `recall-opened.fragment.json`.

`recall-opened.js` is forked too, on one construct: its path resolver tests a literal `memory/`
prefix and then scans for the literal `/memory/` boundary, and both return null for a corpus rooted
anywhere else, after which `main()` bails — indistinguishable from "no read matched". A non-`memory`
root is a supported adopter state, since the memory-tree kit's own conf example ships
`MEMORY_ROOT=memory` as a documented per-repo value. The fix is the cheap honest one: the hook
already parses the log's `shown_paths` array and already indexes into it to compute the rank, and
those paths are corpus-relative by construction, so membership is decided by matching that array
rather than by a root literal. No rendering step, no second place for the root to drift.

### The no-conf behaviour

`.memory-tree.conf` is **required**, and its absence is a refusal, not a default. This matches both
existing adopt scripts: `tools/memory-tree/adopt-memory-tree.sh:18-23` refuses because it must "never
silently scaffold the built-in DEMO disciplines into a real repo", and
`tools/codebase-map/adopt-codebase-map.sh:22-26` does the same for its own conf.

The one difference is that this kit does **not** own the conf, so it must not create one. The refusal
therefore names the memory-tree kit as the prerequisite and prints a copy-pasteable two-key stub the
caller can paste into `.memory-tree.conf` themselves:

```
MEMORY_ROOT=memory
FAMILIES="<discipline>:<FAMILY> ..."
```

It adds **no flags**. An earlier draft had the refusal offer `--memory-root` and `--families`
overrides; those are deleted, because a second way to configure the same three values is the
hand-kept-second-copy defect this repo forbids, and a flag that silently overrode the conf would
reintroduce the exact drift the port exists to remove. The conf is the single source. This also keeps
the Inventory's "no new flags" statement true rather than contradicted.

The refusal fires at **query time as well as adopt time**. Upstream's failure mode when the id
grammar does not match the corpus is a healthy-looking run that returns chunks and zero records; a
refusal guarding only the adopt path would let a later `DISCIPLINES` edit reintroduce it silently.
S7 covers the surviving case — conf present, families wrong — as a printed diagnosis rather than a
refusal, because zero records is also the honest state of a tree that has not written a decision yet.
That diagnosis names `--rebuild`, because with `conf_digest` in the manifest the fix is automatic but
a cache built by a pre-S6 kit is not.

### The alias mechanism without alias data

The mechanism and the data are separable, and upstream already treats them so. `load_aliases()`
returns an empty map, an "(absent)" source label and an empty digest when the default file is
missing; its docstring calls that "a legal alias-free corpus". Only an *explicitly requested* source
that cannot be read is a refusal. `build_index()` writes a third FTS5 column from the record's
`alias` key defaulted to the empty string, so with no data every alias cell is empty.

The kit therefore ships the mechanism and no data:

- `bench.ALIAS_WEIGHT = 0.4` and the three-column schema stay, byte-identical.
- No alias file ships. `ALIASES_DEFAULT` resolves beside the script, so an adopter who later authors
  one drops it in the kit directory and it is picked up with no new config.
- The empty-alias path is a first-class supported state, asserted by the selftest, not merely
  tolerated.

Empty-alias ranking was exercised, not assumed: the run quoted above had no matching alias for any
id, so every alias cell was empty, and the top two hits were the two documents that actually discuss
the adopt script's refusal.

**Cost of excluding the data, stated plainly.** Upstream reports the alias layer as worth +0.040
full@20 at weight 0.4 on its 99-query hard slice, over 1,613 aliased records and 8,675 authored
questions. That figure is a source-repo publication and was **not re-derived in this session**. An
adopter gets none of it, and there is no cheap substitute: the questions are per-record English, and
authoring them is the work upstream's own comment says nothing reconstructs.

### Cache, log, and what the kit writes

The property to preserve is that a query writes nothing inside the adopter's worktree, and it is
asserted by **path**, not by a clean `git status` — a clean status is also what a correctly-ignored
write produces, so it cannot distinguish "wrote nothing" from "wrote something we hid".

That distinction is not hypothetical here. As specified in rev-1 the property was **false**:
query.py:63-66 inserts its own directory on `sys.path` and imports its siblings, so CPython writes
their bytecode next to the source — inside the worktree, not under the common git dir. The rev-1
measurement missed it because it ran from the upstream script directory, where the pycache already
existed and upstream's `.gitignore` hid it. Verified in a throwaway git repo with the kit copied to a
`tools/` subdirectory and one query run: `git status --porcelain` empty before, one untracked
`__pycache__/` entry after, and the two files created inside the worktree were sibling `.pyc` files,
neither of which resolves under the common git dir. In this repo the status stays clean anyway, since
`.gitignore` lines 1–2 carry `__pycache__/` and `*.pyc` — which is precisely why a status-based check
is worthless and the path enumeration is the gate. With `sys.dont_write_bytecode = True` added above
the `sys.path` insert (S5, and S12 for the selftest, which imports the same modules), exactly four
files are created and all four sit under the common git dir.

One sub-claim is corrected rather than amplified: nothing in this repo's tooling refuses on the
resulting dirty tree, because `tools/push-main.sh` gates on the untracked-ignoring form. The harm is
the false property, a red AC4, and untracked noise in an adopter's tree — not a blocked push.

`--export` is kept and retargeted (S5). Upstream writes its aggregate to
`memory/project/recall-traffic-<tag>.md`, inside the worktree, which is the one tracked write and the
one path that could carry a free-text question into version control. Writing it beside the log under
the common git dir closes that path and keeps the reader, and keeping the reader matters: the query
log's only purpose is that somebody can eventually read it, and it is the instrument that told
upstream its outcome-recording rate was 3 records against 178 queries. Dropping the reader outright
would have left a write-only log.

`--stats` is not that reader and never was. It dumps the cache manifest — version, chunk max, file
count, record and chunk counts, corpus digest, alias digest, build seconds, build timestamp — and
`read_log` has exactly two references in query.py, its definition and one call inside `export()`. It
is also not a standalone mode: without a question the CLI prints its usage refusal. §5 lists `--stats`
under observability as a cache fact, which is what it is.

### The Skill surface and the kickoff probe

The skill's `description` is the whole trigger mechanism, and upstream's names five inCMS families
and one inCMS script path. Both must become project values, so the skill is **generated, not
shipped**: `SKILL.template.md` carries placeholders for the id families, the query-script path and
the corpus root, and `adopt-memory-recall.sh` renders it into
`.claude/skills/memory-recall/SKILL.md` from the conf.

Project-local, not a per-machine junction like `skills/session-kickoff/`. The contrast is
deliberate: the kickoff engine is junctioned precisely because it holds nothing project-specific and
reads its project layer at run time, whereas a skill description is matched *before* the skill runs,
so its project values have to be in the file. One machine working on two projects needs two
descriptions.

There is a **third** project coupling in that description, and it is the one that would break the
port silently. Upstream's description ends "Skip it while /session-kickoff is running; that skill's
Step 3 issues this query itself" — true in inCMS, whose kickoff Step 3 literally issues the query.
Here, `skills/session-kickoff/SKILL.md` Step 3 is "Derive a CLOSED task scope" and issues nothing;
the probe analogue codebase-map earned lives in Step 4, "Point at the right code + project protocol".
Grepping this repo for "recall" across `skills/`, `AGENTS.md` and `CLAUDE.md` returns zero hits.
Ported verbatim, the clause suppresses the tool during the exact moment this spec's Goal targets.
Dropped silently, the positive wiring is still missing. Both sides are fixed:

- The template's clause is rewritten to claim nothing the engine implements — it defers to whatever
  probe the kickoff skill's Step 4 actually runs, and names no step number that could go stale.
- `skills/session-kickoff/SKILL.md` Step 4 gains a memory-recall probe paragraph beside the
  codebase-map one, conditioned on the kit being present. Step 4 is literally "point at the right
  code", so a retrieval probe belongs there and nowhere else.

Rendering from config means the description can go stale when `FAMILIES` changes, so
`adopt-memory-recall.sh --check` re-renders and diffs, and rides the gate. This is the shape
`tools/agent-instructions/adopt-agent-instructions.sh --check` already has as a leg in
`tools/gate-legs.json`.

Three invariants are carried into the selftest, all of the same class: the description AUGMENTS grep
rather than replacing it (the "do not use for ordinary code search" clause is not editorial), every
invocation the skill prints must be one `query.py` still parses, and the rendered description makes
no claim about a kickoff step the engine does not implement.

### Python launcher

This repo has **no** equivalent of upstream's `pyrun.sh`, and has three divergent detectors instead:
`tools/run-gates.sh:11` (`PYBIN=python3`, else `python`), `tools/check-wiring.sh:69` (the same two
lines), and `tools/codebase-map/adopt-codebase-map.sh:15` (`PY="${MAP_PY:-python}"`). None executes
the candidate, so none catches the Microsoft Store `python3` stub that answers `command -v` and then
exits 9009.

The port does not add a fourth resolver, because the failure upstream's resolver exists to prevent
does not exist here: `tools/run-gates.sh` prints `GATE FAIL <name> (exit N)` for every non-zero exit,
so a wrong interpreter is loud on the one surface that gates a merge. It also does not copy the
weakest of the three. `MAP_PY`'s bare-`python` default guards a MANUAL `--scaffold`, where a missing
interpreter is a one-off loud failure; `adopt-memory-recall.sh --check` is a **merge-bar leg**, and a
stock Debian or Ubuntu adopter without `python-is-python3` would red the whole gate suite on a
working kit. `tools/run-gates.sh:52` cannot rescue it either — it rewrites `argv[0]` only when that
token is `python` or `python3`, and this leg's first token is `bash`. Today not one bash leg in
`tools/gate-legs.json` shells out to python at all, and
`tools/agent-instructions/adopt-agent-instructions.sh:56` says it computes its path in pure shell
specifically to avoid this, so this would be the first.

So `adopt-memory-recall.sh` uses the `tools/check-wiring.sh:69` form — probe `python3`, fall back to
`python` — with a `RECALL_PY` env override, and the gate legs declare `python3` in `gate-legs.json`
as the codebase-map and settings-merge legs already do. A selftest arm runs the adopt script with
`python` removed from `PATH` and asserts exit 0; without that arm, every node with both binaries
keeps the leg green and the defect invisible. Converging the three detectors onto one resolver is a
real improvement and a separate unit; it is filed as a backlog row, not smuggled into this port.

### Wiring inventory

A kit that ships unwired is the defect the source feature spent a session repairing
(ARCH-aGrittedFlagstone-1: two integrity checks built, green, and invoked by nothing). Every surface
below was read, and each row states the exact addition.

| Surface | What this kit adds |
|---|---|
| `WIRE-INTO-PROJECT.md` | a §0 decision row ("adopt memory-recall?"), a new adopt section after the codebase-map one, **a numbered adopter gate-wiring step** (below), the kit's line in the Result tree, and a Maintenance paragraph naming `bench.py` as wholesale-overwritable and `extract.py`/`query.py`/`recall-opened.js` as forked |
| `parallel-coding-governance.template.md` | one "Optional —" bullet in the §5 optional-kits list beside the memory-tree and codebase-map bullets, and the matching §0 row; byte budget below |
| `parallel-coding-governance.domain-rules.md` | receives the prose displaced by that bullet (below) |
| `skills/session-kickoff/SKILL.md` | the memory-recall probe paragraph in Step 4 |
| `tools/gate-legs.json` | two legs — a `python3 tools/memory-recall/selftest.py` kit selftest, and a `bash tools/memory-recall/adopt-memory-recall.sh --check` skill-wiring check |
| `tools/check-kit-versions.sh` | one `need` line for `KIT_MEMORY_RECALL_VERSION` in `recall_conf.py`, plus the constant-versus-marker pair assertion against `SKILL.template.md`, in the style already used for memory-tree and pytest-parallel-guardrails |
| `tools/settings-merge.py` | the `--fragment FILE` generalisation its own note asks for ("lift the matcher-group to a `--fragment FILE` arg when a second consumer appears"); the no-argument behaviour stays agent-cap and stays idempotent |
| `tools/check-wiring.sh` | a three-state `recall-opened` arm, advisory only — no mode may rewrite `settings.json`, the file the SessionStart hook lives in |
| `tools/check-wiring.test.sh` | cases pinning BOTH the opt-in-not-taken state and the present-but-unmerged state |
| `tools/hooks/` | nothing — the hook and its test ship inside the kit directory, so an adopter gets them by copying the kit |
| `tools/run-gates.sh` | nothing — it iterates the manifest, and the canary asserts it hardcodes no leg |
| `skills/` | see the Step 4 row above; no new skill directory here, since the rendered skill lands in `.claude/skills/` |
| `memory/tooling/DECISIONS.md` | one `TOOL-aQuarriedLantern-1` row |
| `memory/tooling/BACKLOG.md` | rows for the deferred items §8 leaves open, the launcher convergence, and the cache size cap |
| `memory/TREE.md` and `memory/tooling/TREE.md` | regenerated by `gen-memory-tree.sh --write`; hygiene check 9 reds otherwise, verified in this session |
| `memory/project/in-flight/a.md` | one ledger row, node `a` only |
| `AGENTS.md` | the kit in the `tools/` list and the two legs in the gate-suite list |
| `.gitignore` | nothing — S5 removes the need rather than hiding the write |
| `.gitattributes` | an LF rule for the kit's shell scripts, matching the repo's existing LF discipline |

**The adopter gate-wiring step is the load-bearing addition, and it was missing.** Both existing kits
carry one: `WIRE-INTO-PROJECT.md` §3 step 3 for memory-tree ("Wire the gate in all three places" — CI
job, local gate runner, pre-commit) and §3b step 5 for codebase-map, which ends "Without this the
freshness/coverage ratchet silently never runs", and §6 re-verifies the codebase-map leg is standing
in CI and the gate runner rather than merely runnable by hand. Rev-1 wired both of this kit's gates
into this repo's own `tools/gate-legs.json` and nowhere else, so an adopter could copy the kit in and
have `--check` silently never run — kit copied plus a skill file never rendered would read as fully
wired, because AC9 exists solely to catch that drift. The new step mirrors §3b step 5:

1. Add `python3 memory-recall/selftest.py` and `bash memory-recall/adopt-memory-recall.sh --check` to
   the project's local gate runner **and** its CI config, grep-guarded so a re-run does not duplicate
   the leg. Without this the skill-drift check silently never runs.
2. The `--check` leg's interpreter is resolved inside the adopt script (`python3` first, `python`
   fallback, `RECALL_PY` override), so a `python3`-only adopter needs no extra step — this is the
   sentence that has to exist, because the gate runner's argv rewrite cannot reach a `bash` leg.
3. The hook is a separate, explicitly optional sub-step: run `--with-hook` only if the project wants
   the `recall-opened` PostToolUse hook, then `python settings-merge.py --fragment
   memory-recall/recall-opened.fragment.json`. Skipping it is a supported end state, not a gap.

**The adopter-side kit directory name is `memory-recall/` at the project root**, fixed, mirroring
`codebase-map/` (`WIRE-INTO-PROJECT.md`:139-140, whose step adds "the fixed name the gate template
resolves — don't rename"). Every path this spec writes as `tools/memory-recall/...` is this repo's
own spelling; the check-wiring arm and the adopt section use the adopter name.

**The settings fragment's schema**, since `tools/settings-merge.py` hardcodes all three of these
today (the event at line 57, the matcher at line 61, the dedup marker at line 42) and its own
docstring says the marker IS the deployer's is-it-wired signal:

| Field | Value |
|---|---|
| event key | `PostToolUse` |
| matcher | `Read` |
| dedup marker | `recall-opened.js` |

S11 delegates detection to that marker, so a fragment without a declared marker would leave the
recall arm nothing to join on.

**Template byte budget.** Measured this session:

```
$ bash tools/check-template-size.sh
template-size OK — parallel-coding-governance.template.md: 32735 / 32768 bytes (33 under, 99.9%)
```

The two existing optional-kit bullets are 419 bytes (line 106, memory-tree) and 435 bytes (line 107,
codebase-map), measured by reading the file's bytes and splitting on the detected newline. A third
comparable bullet does not fit in 33 bytes, and the gate's own text forbids raising the ceiling to
fit new prose. The displaced prose is named rather than left to the build: line 153, the §8
structured-output-schemas bullet, at 470 bytes, moves verbatim into
`parallel-coding-governance.domain-rules.md` under a new `## §8` block, and the template keeps a
pointer in the shape its §4/§9/§10/§11/§12/§13 stubs already use. That frees 471 bytes with the
newline, for 504 available against a bullet budgeted at ≤ 440. The bullet is a Tier-2 review-harness
mechanic, which is exactly the activity-scoped content that companion file exists to hold.

### Inventory

New keys this unit claims: kit `memory-recall`; version constant `KIT_MEMORY_RECALL_VERSION`; marker
`gov:kit memory-recall@1.0`; env override `RECALL_PY`; two gate legs; skill `memory-recall`; hook
`recall-opened`; the settings fragment `recall-opened.fragment.json` with the schema above; two
manifest fields, `conf_digest` and `worktree`; and one adopt-script flag, `--with-hook`.

CLI flags on `query.py` are **unchanged from upstream** — none added, none removed. `--export`'s
output path moves out of the worktree and its node-registry lookup is deleted, so `--tag` becomes
required for `--export`; `--rebuild` gains a `--help` line it lacked. There is no `--memory-root` and
no `--families`: the conf is the single source, and the refusal prints a conf stub instead.

### Migration

None. The kit is additive and no adopter has a prior version. Within this repo the dogfood adoption
creates the rendered skill file; it adds a hook block to `.claude/settings.json` only if `--with-hook`
is passed, which the dogfood adoption does not do. Both are new files or new keys, and
`settings-merge.py` backs the settings file up before writing.

### Rollout

Land the kit dark relative to the corpus it indexes: nothing about the kit changes what any existing
gate reads, and the two new legs test only the kit's own contract. The hook lands darker still — not
copied at all without `--with-hook`, so its absence is a true signal rather than a permanent false
alarm. This repo dogfoods immediately because it *is* the reference adopter, and its corpus (66
files, 468,288 bytes) is small enough that a wrong answer is cheap to notice.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-recall/` (11 files) | new — the nine of S1 plus the hook test and the fragment |
| `tools/settings-merge.py` | the `--fragment` generalisation, lifting the three hardcodes, plus selftest cases |
| `tools/check-wiring.sh` and `tools/check-wiring.test.sh` | one three-state arm plus both of its state cases |
| `tools/check-kit-versions.sh`, `tools/gate-legs.json` | a few lines each |
| `skills/session-kickoff/SKILL.md` | one Step 4 paragraph |
| `parallel-coding-governance.template.md` | one §5 bullet (≤ 440 B) and one §0 row, funded by moving line 153 out |
| `parallel-coding-governance.domain-rules.md` | a new `## §8` block receiving that 470-byte bullet |
| `WIRE-INTO-PROJECT.md`, `AGENTS.md`, `.gitattributes` | doc and registration edits, including the gate-wiring step |
| `memory/` indexes, TREE files, ledger | registrations |
| `.claude/skills/memory-recall/SKILL.md` | this repo's dogfood adoption |

### Alternatives rejected

- **Ship the whole upstream recall folder.** 8,422 lines against roughly 1,900 that the query path
  needs. `grep_study.py` alone is 42,031 bytes of a study whose verdict was `UNDERPOWERED`, and its
  `selftest.py` is 4,419 lines carrying 115 checks, of which 15 grade that study and 10 grade an
  alias file that does not ship. The instruments stay upstream, one copy away, and the constants they
  tuned ship as constants.
- **Invent a second config file.** A second declaration of `MEMORY_ROOT` and the families is the
  hand-kept-second-copy class this repo's own rules forbid, and it would drift from the gate that
  already enforces those names.
- **Scope `--memory-root` and `--families` as escape-hatch flags.** The same objection wearing a
  smaller hat: two flags that override the conf are a second way to declare the three values the port
  exists to centralise, and a silent override is worse than a second file because nothing records it.
  The refusal prints a conf stub instead, which serves the same population — a project with a memory
  tree but no hygiene kit — at zero contract cost.
- **Import `load_conf` from `map_lib.py`.** Correct on duplication, wrong on coupling: kits are
  copied in independently, and this would make memory-recall un-adoptable without codebase-map.
- **Promote `load_conf` to a shared `tools/conf_lib.py`.** The same objection in the other direction,
  and it changes an already-adopted kit's file layout for a 20-line function.
- **Drop `--export` entirely.** It closes the credential-into-git path, but it leaves a log nothing
  reads, and `--stats` does not substitute for it because `--stats` prints the cache manifest.
  Retargeting the write outside the worktree closes the same path and keeps the reader.
- **Hash the conf file's bytes for `conf_digest`.** A comment edit would force a full rebuild —
  6 seconds on the upstream corpus — for no semantic change. Hash the resolved values.
- **Copy the hook file unconditionally and leave it unwired.** Present-but-unmerged is the state
  `tools/check-wiring.sh` already reports as UNWIRED, so the reference adopter would print a
  permanent false alarm at every session start, which is the fastest way to train every node to
  ignore the wiring verifier. Upstream has this hook wired on no node, so "it gets wired later" is
  refuted by evidence rather than merely unproven.
- **A generic, family-free Skill description.** The families are the trigger's discriminating tokens;
  removing them trades the port's usefulness for one avoided template.
- **Port `check_recall.py` with re-derived floors.** A gate that recomputes its threshold from the run
  it is grading can never fail — upstream names this the circular-ceiling class and pins its floors
  against a frozen fixture for exactly that reason. Without a fixture there is no honest floor.

## 5. Production-readiness checklist

- **security** — the query log stores free-text questions and an absolute worktree path under the git
  directory, untracked and never pushed; `--export` writes its aggregate beside that log, outside the
  worktree, so no path in the kit moves query text into a tracked file. The hook reads a bounded
  128 KB tail, never blocks a `Read`, and exits 0 on every path. The kit executes nothing from the
  corpus and makes no network call.
- **perf / scale** — measured cold index 6.006 s on the 40,993,440-byte inCMS corpus; warm query
  0.702 s and 0.865 s on two consecutive upstream runs, 0.685 s here. For scale honesty:
  `grep -rIl "adopt" memory/` over this repo takes 0.048–0.056 s across three warm runs and returns
  31 of 66 files. On a small corpus retrieval buys precision, not latency, and the README must say so
  rather than implying a speed win that is not there.
- **a11y** — N/A — a standard-library CLI with no UI surface.
- **i18n** — N/A — output is the corpus's own text, and the FTS5 `unicode61` tokenizer is unchanged.
- **error / empty / loading states** — no conf (refuse, naming memory-tree, printing the stub); conf
  present but no family produces an anchor (print the diagnosis naming the key, the conf path and
  `--rebuild`, S7); empty corpus; zero hits; a budget smaller than the first hit (emit it alone and
  report the overflow, upstream behaviour kept); a corrupt cache (rebuild); a partially written
  manifest (rebuild mine, never evict theirs — §4).
- **observability** — the JSONL query log, `--export`'s aggregate beside it, and `--stats`, which
  prints the **cache manifest** (version, chunk max, file count, record and chunk counts, corpus
  digest, alias digest, build seconds, build timestamp) and reads no log.
- **risks** — git-directory growth, re-measured upstream this session and stated as its split rather
  than as one headline: five cache directories totalling 552.6 MiB, of which three belong to
  worktrees that exist and survive eviction (343.2 MiB — 114.6, 114.6 and 114.1) and two are orphaned
  (209.4 MiB — 110.2 and 99.2), plus a 2.30 MiB log, for 555 MiB total. S6's eviction therefore
  reclaims **37.9% of the cache**, not the 555 MiB figure. The real driver is ~115 MiB of cache per
  LIVE worktree against a 40 MB corpus, in a repo shape that mandates concurrent worktrees: at the
  seven currently checked out, a perfectly-evicted cache is still ~802 MiB. v1.0 ships no per-worktree
  cap and no LRU on `built_at`; the ceiling is stated here and filed as a backlog row rather than
  designed blind. Log growth is unmitigated at 2,414,771 bytes over 676 rows. `qid` allocation is
  "max plus one" after a re-read, so concurrent writers collide and nothing may join on `qid` or count
  distinct `qid`s as a proxy for queries. A fixed id grammar means a project whose ids do not match
  gets the chunk arm only, which works and is quiet about it (Q4).
- **testing + left-shift gates** — `selftest.py` as a gate leg, plus the hook's test. Three classes
  are gated deliberately rather than assumed. The Python conf parser is asserted against **bash**,
  never against a second Python parser. Every selftest arm runs in a throwaway repo: upstream's own
  selftest appended a synthetic `refused` row to the shared query log on every run — 471 of 489
  refusals in the live log came from the gate that was grading it — so a leg that writes to the
  instrument it measures is a hard rule here. And the interpreter arm runs the adopt script with
  `python` off `PATH`, because a node with both binaries can never see that defect.
- **migration / rollback** — nothing to migrate. Rollback is deleting the kit directory and the
  rendered skill, removing the two legs, removing the hook block if `--with-hook` was taken, and
  deleting the `recall` directory under the common git dir; no tracked project data is touched.
- **user docs** — `tools/memory-recall/README.md` in the shape of the other two kit READMEs (what's
  here, configure, adopt, maintenance, plus the bench.py usage-string caveat and the pycache
  dependency), the `WIRE-INTO-PROJECT.md` section with its gate-wiring step, and the rendered skill
  file, which is itself the agent-facing documentation.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-recall/query.py` runs in this repo with a question and `--terms`, it
  prints ranked hits whose ids carry this repo's families, and the header reports a non-zero record
  count (today's baseline: 9 anchored records and 989 chunks over 66 files).
- **AC2** — When `FAMILIES` in `.memory-tree.conf` is edited to a value matching nothing and the
  query is re-run against an already-warm cache, the header reports `rebuilt` (not `cached`), the
  record count moves to zero, and the S7 diagnosis names `FAMILIES`, the conf path and `--rebuild`.
  When `FAMILIES` is then repaired and the query re-run, the header again reports `rebuilt` and the
  record count returns to its AC1 value. Asserting the diagnosis message alone is insufficient — both
  directions must move the count.
- **AC3** — When `.memory-tree.conf` is absent, the CLI and the adopt script both exit non-zero with
  a message naming the memory-tree kit, neither creates a conf file, and the printed stub, pasted
  verbatim into `.memory-tree.conf` and given real values, makes the next query succeed.
- **AC4** — When a query runs in a clean checkout, `git status --porcelain` is empty **and** every
  file created resolves under the `recall` directory inside the common git dir; the check enumerates
  paths under the worktree root **and** under the kit directory, rather than reading the status, and
  the enumeration is run in a repo whose `.gitignore` does not carry `__pycache__/`.
- **AC5** — When the corpus has no alias source, the index builds, every alias cell is empty, and the
  ranked list is non-empty for a question whose answer is in the corpus.
- **AC6** — When an alias file is placed in the kit directory, the cache rebuilds on the alias digest
  change and the manifest records the new digest, with no config edit.
- **AC7** — Three cases. When a cache directory's recorded `worktree` no longer exists, the next
  build deletes it. When its `worktree` does exist, it survives. When a sibling cache directory holds
  both `.db` files and **no readable manifest**, it survives every build — the mid-first-build state
  is never evicted.
- **AC8** — When `adopt-memory-recall.sh --scaffold` runs twice, the second run changes no file
  (byte-compared), and `--check` then exits 0.
- **AC9** — When `FAMILIES` changes and the skill is not re-rendered,
  `adopt-memory-recall.sh --check` exits non-zero and names the drifted placeholder.
- **AC10** — When `settings-merge.py` runs with no `--fragment`, its output is byte-identical to the
  pre-change version on the same input; when run with `recall-opened.fragment.json`, it adds the
  PostToolUse/Read block carrying the `recall-opened.js` marker, and a re-run changes nothing.
- **AC11** — When the `recall-opened` hook fires on a `Read` of a corpus file within the window, it
  appends one `opened` row carrying `inferred: true`, and appends nothing when a record already
  exists for that `qid`.
- **AC12** — When the same hook runs in a repo whose `MEMORY_ROOT` is not `memory`, it appends the
  same `opened` row — membership is decided by the log's `shown_paths` array, not by a root literal.
- **AC13** — When `adopt-memory-recall.sh --scaffold` runs **without** `--with-hook`, no file appears
  under `.claude/hooks/`, and `tools/check-wiring.sh` reports the recall arm as an opt-in-not-taken
  skip line, not UNWIRED. When it runs **with** `--with-hook` and the settings block is absent,
  the same arm reports UNWIRED. Both states are cases in `tools/check-wiring.test.sh`.
- **AC14** — When `adopt-memory-recall.sh --check` runs with `python` removed from `PATH` and only
  `python3` available, it exits 0.
- **AC15** — When any CLI path prints an invocation — the usage refusal for a missing `--terms`, the
  module docstring, the qid hand-back after a successful query — the script path in that invocation
  resolves to an existing file in the adopter repo. The selftest asserts this in a throwaway repo
  whose kit directory name differs from this repo's.
- **AC16** — When `selftest.py` runs, it reports its check count, every arm operates inside a
  throwaway repo, and the live query log is byte-identical before and after the run.
- **AC17** — When the conf holds a quoted value with spaces, an unquoted value with a trailing
  comment, and an `export`-prefixed key, `recall_conf.load_conf()` returns exactly what `bash`
  sourcing the same file reports for those keys.
- **AC18** — When the rendered `SKILL.md` is read, its description carries the augments-grep clause,
  every invocation it prints parses under `query.py`, and it names no `/session-kickoff` step the
  engine in `skills/session-kickoff/SKILL.md` does not implement. The selftest asserts all three.
- **AC19** — When `bash tools/run-gates.sh` runs, both new legs appear and pass;
  `bash tools/check-kit-versions.sh` reports the kit's constant and its marker pair as consistent;
  and `bash tools/check-template-size.sh` exits 0 with the template still under 32,768 bytes.
- **AC20** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs after the landing, it exits 0
  with no output.

## 7. Gates

Standing legs this unit must keep green, all via `bash tools/run-gates.sh`: memory hygiene (12
checks), kickoff-manifest ratchet, template size, kit version markers, agent-instructions wiring,
settings-merge selftest, check-wiring self-test, run-gates canary, and the remaining kit self-tests.

New legs this unit adds to `tools/gate-legs.json`:

- `memory-recall kit selftest` — `python3 tools/memory-recall/selftest.py`.
- `memory-recall skill wiring` — `bash tools/memory-recall/adopt-memory-recall.sh --check`.

Two existing legs change and must still pass: `settings-merge selftest` gains `--fragment` cases, and
`check-wiring self-test` gains the recall arm's two state cases (AC13).

**What gates this kit in an adopter project — the mechanism, not just the file.** Copying the kit in
wires nothing; the gate exists only once the adopter has run the `WIRE-INTO-PROJECT.md` gate-wiring
step that adds both legs to their local gate runner and their CI config, grep-guarded. That step is
part of this unit precisely because rev-1 omitted it and both existing kits carry one. Without it the
skill-drift check silently never runs, and a kit copied in beside a skill file never rendered reads as
fully wired.

What that gate then asserts is the *kit contract*, not a recall floor — no adopter has a graded
fixture, and a floor re-derived from the run it grades cannot fail. `selftest.py` asserts the
parser-versus-bash parity, the no-conf refusal and its stub, the empty-alias path, the
write-nothing-in-the-worktree property by path, the cache eviction including the never-evict branch,
the interpreter fallback, and that every invocation both the CLI and the skill print still parses and
still resolves. That is the same bargain `tools/codebase-map/selftest.py` and
`settings-merge.py --selftest` already strike here. An adopter who later authors a fixture can pull
`bench.py`'s harness and `check_recall.py` from upstream and pin their own floors; the kit neither
requires nor pretends to that.

## 8. Open questions

- **Q1 — Should the node-tag class be a conf key?** §4 hardcodes `a-z`, matching
  `tools/memory-tree/check-memory-hygiene.sh:332`. Option (a): add an optional `NODE_TAGS` key to
  `.memory-tree.conf`, which is a contract change to a file another kit's gate reads. Option (b):
  keep `a-z` hardcoded and declare non-letter node tags unsupported. Option (c): derive the tags from
  the ledger files present under the corpus root. **Recommendation: (b).** No measured case needs
  narrowing, and (a) spends a cross-kit contract change on a value nobody has asked to set. Flagged
  rather than closed because it is the one place this port touches another kit's declared surface.
- **Q2 — Should `--export` go?** **RESOLVED (owner, 2026-08-03): option (b)** — keep the aggregation
  and write it outside the worktree, beside the query log under the common git dir. Dropping it would
  have closed the credential-into-git path at the cost of leaving a log nothing ever reads, and the
  log's only purpose is that somebody can eventually read it: it is the instrument that told upstream
  its outcome-recording rate was 3 records against 178 queries, and the upstream grep study died at
  n=5 for want of exactly this evidence. `--stats` was named as the substitute in rev-1 and is not
  one; it prints the cache manifest. The node-registry lookup goes with the retarget, so `--tag`
  becomes required for `--export`.
- **Q3 — Does the `recall-opened` hook ship wired in v1.0?** **RESOLVED (owner, 2026-08-03): ship it
  dark, behind an explicit opt-in.** Upstream wired it on **no** node as of 2026-08-03, so its value
  is projected, not observed, and it runs on every `Read` in the session. Rev-1's phrasing of this
  option was unreachable: it claimed `tools/check-wiring.sh` would report "not adopted", but that arm
  keys "not adopted" on the hook file's ABSENCE and rev-1's `--scaffold` copied the file
  unconditionally, so a faithful mirror would have printed UNWIRED forever — in the repo that runs
  that script as its own SessionStart hook. The resolved shape is the honest one: `--scaffold` copies
  no hook without `--with-hook`, so absence is a true signal, and both states are pinned in
  `tools/check-wiring.test.sh` (AC13). Two consequences claimed during review do **not** hold and are
  not designed around: `--session` exits 0 early, so session start never breaks, and
  `WIRE-INTO-PROJECT.md` says not to run the wiring check as a merge-bar leg, so no gate goes red.
  The `--fragment` generalisation (S10) is worth building either way, since it is what makes any
  second hook wirable at all.
- **Q4 — Corpora with no id grammar.** A project whose corpus has no anchored ids gets chunk
  retrieval and zero records, which the measurement above shows works and looks identical to a
  misconfiguration. S7's diagnosis distinguishes them by printing the conf values, but there is no
  positive declaration of "this project has no id grammar". Option (a): leave it as a printed
  diagnosis. Option (b): a conf key that turns the diagnosis off. **Recommendation: (a)** until a
  real adopter hits it; (b) is a config key for a state nobody has.
- **Q5 — The three Python-launcher detectors.** §4 declines to converge them in this unit and files a
  backlog row, while adopting the stronger of the two forms for the merge-bar leg. Open only as to
  whether the owner wants that convergence bundled here instead, since this port is the third
  consumer and the cheapest moment to do it. **Recommendation: keep it out** — it touches
  `tools/run-gates.sh`, `tools/check-wiring.sh` and `tools/codebase-map/adopt-codebase-map.sh`, three
  files this port otherwise does not need to change.
- **Q6 — Is retrieval worth adopting on a small corpus at all?** Re-measured here: 66 files, 468,288
  bytes, 9 anchored records, 989 chunks, and a full-corpus grep in 0.048–0.056 s. Retrieval's honest
  claim at that size is precision (one common word matched 31 of 66 files), not speed or token cost.
  Option (a): ship the kit and let the README state the size at which it starts paying. Option (b):
  add an adoption guideline with a threshold. **Recommendation: (a)** — no measurement in this
  session establishes a threshold, and inventing one would be the kind of number this spec's own
  rules forbid. **This fork stays open on purpose:** the build does not settle whether retrieval
  earns its keep in a 403 KB-class corpus, and no acceptance criterion pretends to.

## 9. Revision log

- rev-1 · 2026-08-03 · initial draft. The coupling inventory, cache and log residency, and every
  timing and size figure were measured in-session against both repos; the alias-layer recall figure
  is carried from the upstream record and labelled as not re-derived.
- rev-2 · 2026-08-03 · folded the pre-code adversarial review
  (`memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/reviews/2026-08-03-review-aQuarriedLantern-1.md`,
  NOT READY, 14 confirmed findings, precision 0.93, zero unverified). All 14 folded; none declined.
  **Blocker F1** — the cache freshness key ignored the conf, so the one value the port moves into
  `.memory-tree.conf` was a cold input to a hot cache and the S7 remediation path was a silent no-op
  in both directions; S6 now adds `conf_digest` over resolved values to the manifest and the `fresh`
  predicate, S7 names `--rebuild`, S5 documents that flag, and AC2 was rewritten from asserting a
  message to asserting `rebuilt` plus a moved record count in both directions.
  **Blocker F2** — both gates were wired only into this repo, so an adopter could copy the kit in and
  have the drift check silently never run; S13 and the wiring inventory now carry a numbered
  adopter gate-wiring step mirroring `WIRE-INTO-PROJECT.md` §3b step 5, and §7 names the mechanism
  rather than the file. That step is also where F9's interpreter form and F10's hook opt-in surface,
  since it is the only place an adopter reads before wiring either.
  The two blockers interact and the resulting shapes are stated in §4 Data model: F1's `conf_digest`
  and F14's `worktree` land in the same manifest, whose absence resolves to one rule in two
  directions — rebuild mine, never delete theirs — gated by AC7's third case.
  Also folded: F3 (escape-hatch flags deleted; the refusal prints a conf stub, so the Inventory's
  no-new-flags statement is now true rather than contradicted), F4 (both sides — the template's
  kickoff clause claims nothing the engine lacks, and `skills/session-kickoff/SKILL.md` Step 4 gains a
  memory-recall probe paragraph), F5 (`sys.dont_write_bytecode` named as a fork edit in S5 and S12;
  AC4 enumerates the kit directory too and runs without a `__pycache__` ignore rule; the Non-goals
  `.gitignore` line corrected), F6 (`--stats` stated correctly as printing the cache manifest
  everywhere it appeared, and Q2 resolved to (b) — the aggregation is kept and written outside the
  worktree), F7 (the script's own path added to the fork list and the coupling table, every printed
  invocation derived from `__file__`, AC15 added, S4's bench.py claim re-scoped to the query path),
  F8 (no separate action — the portability lens reported F5's defect from the adopter angle and F5's
  one-line fix closes it), F9 (`python3`-first probe in the adopt script plus AC14's `python`-off-PATH
  arm), F10 (no hook copy without `--with-hook`; both states pinned in `tools/check-wiring.test.sh`
  via AC13; Q3's stated outcome corrected), F11 (template bullet and §0 row, with the byte budget
  measured — 33 free, existing bullets 419 and 435 B — and line 153's 470-byte bullet named as the
  prose moving to the domain-rules companion), F12 (the fragment's shipped path in S1 and the
  Inventory, its event/matcher/marker schema stated, and the fixed adopter-side kit name
  `memory-recall/` declared), F13 (the hook matches the log's `shown_paths` array instead of a root
  literal, is added to the coupling table, and gets AC12), and F14 (§5 now states the measured split —
  209.4 MiB evictable of 552.6 MiB cache plus a 2.30 MiB log, so eviction reclaims 37.9% of the cache,
  not 555 MB — with the ~802 MiB seven-worktree ceiling stated and no cap shipped in v1.0).
  Declined: nothing. One optional sub-leg of F2 was not taken — a SKILL arm in `tools/check-wiring.sh`
  — because the review itself noted that file has two arms today, neither existing kit has one, and
  the blocker does not rest on it. Every figure in this rev was re-measured this session; the
  corpus moved from 64 files / 403,312 bytes to 66 files / 468,288 bytes, and chunks were recounted at
  query.py's real `CHUNK_MAX = 600` (989, not rev-1's 861 at the old corpus size). The alias-layer
  recall figure remains carried from upstream and labelled as not re-derived.
