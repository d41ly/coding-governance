# TOOL-aGraftedHelix-9 — a newly added decision row or gotcha that ranks as a near match must name its relation

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 5 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 |

<!-- /gen:spec-records -->

## 1. Goal

Prior art is checked today only as a lens of a spec audit, so two nodes can each record what is in
effect the same decision, or a decision that quietly narrows an older one, and every leg stays green.
This unit adds hygiene check 27 to the memory-tree kit: every decision row and every gotcha added
since the mainline merge-base is ranked against the records that existed at that base, with the
recall kit's own index builder, and a top hit that clears a measured similarity floor must be named
by the new record or answered with a relation token. It is helixir's deterministic contradiction
gate (a shared significant token plus a similarity floor, before any judgment) grafted onto the
hygiene gate that already owns the row grammar.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/row_grammar.py` gains `scan_records(root, conf)`, the one enumeration
  of the record population: every row the row grammar keys in the decision index and its rotated
  archives, the members of `row_docs()` whose stem is `DECISIONS`, and every gotcha record under the
  memory root's `gotchas/` folder except its `INDEX.md`.
  Its fields are §4 "Data model". The front-matter pattern moves from `gotchas.py` to `tree_lib.py`
  as `FM_RE`, and `gotchas.py` imports it, so the kit holds one copy. Observed by AC1, AC3 and AC9.
- **S2** — A new mode, `row_grammar.py --check-relations [<base>]`. With no argument the base is the
  merge-base of `origin/<branch>` and `HEAD`, falling back to `<branch>` and `HEAD`, where
  `<branch>` is `GOV_DEFAULT_BRANCH` or `main`. The ADDED set is every record at `HEAD` whose
  identity is absent at that base, and the ELIGIBLE set is every record whose identity is present
  both at it and at `HEAD`, so a gotcha renamed inside the range is added under its new name and
  never eligible under its old one. An armed run with no resolvable base reds naming it, an empty
  added set prints a graded count of 0, and an unarmed run reads no history at all. Observed by AC1,
  AC5, AC7, AC9 and AC14.
- **S3** — The near-match predicate, pinned in §4 "The predicate": an in-memory index over the
  record population built by the recall kit's `bench.build_index`, queried with the record's own
  summary text through `bench.match_expr`; the top eligible hit is a NEAR MATCH when the Jaccard similarity
  of the two `bench.terms` sets reaches the declared floor and the sets share a term of four or more
  characters. A top hit that is a row of the new row's own slug is not graded and is counted.
  Observed by AC1, AC3 and AC8.
- **S4** — A near match is SATISFIED when the new record's full text names the hit's identity, or
  names a successor the superseded-by map of `TOOL-aGraftedHelix-4` holds for the hit, or carries
  one of the relation tokens `supersedes`, `coexists-with`, `disputes`. An unsatisfied near match is
  a finding line, and a hit the map holds is tagged there as that unit's `render()` tags it. The map
  is derived only when some near match is otherwise unsatisfied, §4 "The superseded-by map".
  Observed by AC1, AC2, AC3 and AC12.
- **S5** — `.memory-tree.conf` declares `NEAR_MATCH_GATE`, grammar `red:<floor>` or `warn:<floor>`
  with the floor a decimal in (0, 1], blank meaning NOT ARMED and announced. This repository declares
  `red:0.125`, the value §8 F1 measured. The kit's example conf declares it blank, because a floor
  measured on gov's corpus is not a floor for another corpus. A malformed value, or an armed key
  with the recall kit's index builder absent or too old, is a named refusal and never a traceback.
  Observed by AC1, AC4, AC5, AC6 and AC11.
- **S6** — A second mode, `row_grammar.py --measure-relations [<floor> [<base>]]`, replays every
  row and gotcha the history added against the records older than it, with the S3 predicate, and
  prints the would-flag count per band and the flagged pairs at the floor given, or at the declared
  one. Given a base, the population is the records present both at it and at `HEAD`, read with S2's
  presence test, so a measurement can be repeated exactly after newer records have moved the index's
  term statistics. It is the instrument F1 was decided with, shipped so an adopter can measure their
  own floor before arming the key. Observed by AC8.
- **S7** — Hygiene check 27 is wired: the module constant `RELATION_CHECK = 27`, a full-run dispatch
  block in `tools/memory-tree/check-memory-hygiene.sh` that prints the mode's output on a green run
  too and keys offenders under 27, its catalog entry in `tools/memory-tree/HYGIENE.template.md`
  re-rendered into `memory/HYGIENE.md`, and the kit README's check count moved to 27. Observed by
  AC10 and AC11.
- **S8** — The module header states what check 27 does NOT check, and every new branch has a
  `--selftest` arm whose fixture makes it fire. Observed by AC1 to AC7, AC12 and AC13.
- **S9** — The memory-tree kit version moves once, after the last move, in every carrier
  `tools/check-kit-versions.sh` pairs, and the row-grammar dossier's prose names the two new modes.
  One of those carriers is line 1 of `memory/guides/BUILD-METHOD.md`, which the re-render moves and
  nothing else in that file, under `TOOL-aGraftedHelix-3`'s §8 F1 ruling (§8 F2 here). Observed by
  AC15; the kit-versions, verdict-epoch and codebase-map legs grade the rest at the close (§7).

## 3. Non-goals (OUT)

- Exact duplicates. A normalized content key held twice is `TOOL-aGraftedHelix-6`.
- Deciding whether two records CONTRADICT. A near match obliges the author to name a relation; it
  never judges which record is right, and no model is consulted.
- Any record kind other than decision rows and gotchas: specs, backlog asks, review records and
  journals are out of the population.
- Grading a row edited in place. The decision index is append-only, so a changed row is check 20's
  and the merge driver's business, and the added set is decided by identity alone.
- Comparing a new record with another record added in the same range. Both are the author's own
  session's, and the eligible set is the base's records only.
- The pre-commit `--staged` path. Check 27 reads a range and runs on full runs only, as checks 13 to
  20 and 24 do.
- The served recall CLI and its ranking. Demotion and the `[superseded by <id>]` tag in `query.py`'s
  output are `TOOL-aGraftedHelix-4`'s.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-4` — `extract_supersessions` and `derive_supersession_map`
  in the recall kit's `extract.py`, called directly here to accept a named successor and to tag a
  superseded hit; nothing here reads the cache manifest or a hit's fields. Without them a record
  naming the successor of an old hit still reds. Only a relation spelled `supersedes <id>` reaches
  that map; a bare `supersedes` token satisfies this check and adds no edge, so the finding's
  remedy text suggests the `supersedes <id>` form.
- **hands-off** `TOOL-aGraftedHelix-6` — the record enumeration `scan_records` and the shared
  `FM_RE` in `tree_lib.py`, which that unit extends with a gotcha body field for its content key;
  and `derive_relation_base` with the identity-presence test, which that unit uses to report only
  keys an added record holds.
- **hands-off** `TOOL-aGraftedHelix-14` — the hygiene engine's dispatch block for check 27, which
  calls `--check-relations` and keys offenders under `RELATION_CHECK`. AC10 here proves the block is
  present; that unit observes it red the leg under `NEAR_MATCH_GATE` and print its summary on a
  green run (round-1 audit finding 27).

## 4. Design

### Evidence

- Placement. `row_grammar.py` is the owner of the decision index's row grammar and its walk
  (`row_docs`, `scan`), and check 24 already rides it as a second mode, `--check-rotation`.
  `TOOL-cSpliceWarden-6` is the ruling that a check grading rows delegates to that owner rather than
  spelling a second row predicate. The recall floor leg's `check-recall.py` was the other host with
  an index already built, and the recall kit's `kit.toml` withholds it from every adopter, so a check
  there ships to nobody.
- The cross-kit read has a precedent: `corpus_ids.py` resolves the recall kit's `extract.py` through
  the canonical `resolve_kit_dir` block, refuses by name when a pin is set and the kit is absent, and
  is off when no pin is set. This unit takes the same shape for `bench.py`. It names the sibling by
  its kit home through that resolver, receipt row first, and never by a typed path, which is the
  spec brief's invariant 2 as `corpus_ids.py` already satisfies it.
- The base derivation is `check-verdict-epoch.sh`'s: `origin/<branch>` first, then `<branch>`, with
  `GOV_DEFAULT_BRANCH`, and a missing base while armed is a red, because the bar judges a leg by its
  exit code and a zero-status skip reads as a pass.
- Population at base `5266d22e`, measured 2026-10-04 on node `a`: 260 keyed rows across
  `memory/DECISIONS.md` and its one rotated archive, and 94 gotcha records.

### The graded pairs

Every pair §8 F1's replay flagged at the 0.125 floor, new record first, then its top hit, then the
hand grade. Family prefixes are elided; a gotcha is its file stem.

```
worktree-crlf-outside-the-gated-population > aDrainedSluice-8b T
dHonouredPark-4 > aBoundedVerdict-11 T
aProbedUnit-10 > aTetheredScratch-1 T
aBatchedTribunal-1i > aFoldedQuarry-7 T
cFinalBerth-2 > aUnmannedHelm-5 T
aNamedGesture-1 > aPromptedMandate-4 F
aMendedLedger-1 > aFoldedQuarry-4 T
a-spelling-change-strands-its-readers > two-readers-of-one-config-one-re-derived T
aPooledSweep-1 > aGradedDoorway-8 F
aDrainedSluice-5 > aFoldedQuarry-7 T
aProbedUnit-8 > aLeakedHandle-7 F
aBatchedTribunal-6q > fixture-passes-by-finding-nothing T
aBoundedVerdict-2 > cFinalBerth-1 F
dHonouredPark-1 > dFramedEntrypoint-8 T
aRelaxedShard-4 > aMendedLedger-5 F
aBatchedTribunal-1f > aWireWarden-1 T
line-count-reads-empty-capture-as-one > retirement-inventory-misses-readers-by-value F
msys-grep-counts-cr-on-every-line > aBatchedTribunal-1g T
aCandidStub-1 > aFoldedQuarry-6 T
dRetiredFork-41 > dBriefedPass-4 T
cMendedVintage-13 > aWidenedGuide-1 T
aUnmannedHelm-5 > aBatchedTribunal-6o T
dPolishedVitrine-14 > aLeakedHandle-7 F
dRetiredFork-4 > aWidenedGuide-2 F
format-derived-from-arity > trailing-comma-counted-as-an-element F
dGatedProse-4 > dHonouredPark-2 T
dScaffoldedMirror-17 > aMendedLedger-6 F
aMendedLedger-1c > aDrainedSluice-9 T
anchor-literal-resolves-above-its-target > aBatchedTribunal-6e F
swallowed-delegate-reads-as-clean > aBatchedTribunal-6k T
```

### Data model

`scan_records(root, conf)` returns one dict per record:

| field | a row | a gotcha |
|---|---|---|
| `kind` | `row` | `gotcha` |
| `ident` | the row's id | the file stem |
| `names` | the id | the stem and the front-matter `name` |
| `where` | `<path>:<line>` | `<path>` |
| `summary` | the line after the keyed prefix | the front-matter `description` |
| `full` | the whole line | the whole file, front matter included |
| `slug` | the id's middle segment | none |

`summary` is what similarity is measured on; `full` is what the satisfaction test reads, so an
invariant record of `TOOL-aGraftedHelix-3` whose `decision:` key names its ruling's id satisfies a
near match against that ruling's row. The front-matter `description` is read from the block `FM_RE`
matches, with the column-0 `key: value` rule `gotchas.py` already enforces in check 17-19's parse.

At a base, a row's identity is present when the row grammar keys its id in the row documents as
they stood there, each read with `git show <base>:<path>` after `git ls-tree -r --name-only <base>`
lists them, and a gotcha's when `git ls-tree --name-only <base>` lists its path. Texts are always
read at `HEAD`.

### The predicate

Pinned, because §8 F1's measurement was taken with exactly this and a different construction is a
different floor.

1. One document per record `scan_records` returns, `{"id": <id or empty>, "path": <path>,
   "text": <summary>}`, into `bench.build_index` with its default in-memory database. The index holds
   the whole population in both modes, so its term statistics are the replay's.
2. The query is `bench.match_expr(<the added record's summary>)`, ranked by
   `bm25(d, 1.0, 1.0, bench.ALIAS_WEIGHT)`, `LIMIT 200`. The top hit is the first row returned that
   is ELIGIBLE: under `--check-relations` a record of the eligible set, and under the replay a record
   older than the one being ranked. A record with no eligible row in the 200 has no near match.
3. A top hit that is a row whose slug equals the added row's slug ends that record's grading:
   counted as `own-session`, never advanced to the next hit. The measurement dropped those pairs, and
   advancing was not measured.
4. `A` and `B` are the distinct `bench.terms` sets of the two summaries. The hit is a near match when
   `|A ∩ B| / |A ∪ B|` reaches the floor AND `A ∩ B` holds a term of four or more characters.
5. Satisfied when `full` matches any of: each of the hit's `names`, delimited by
   `(?<![\w-])` and `(?![\w-])`; any successor, whole or partial, the superseded-by map holds for
   the hit's id, delimited the same way; or `\b(supersedes|coexists-with|disputes)\b`,
   case-insensitive.

`bench.py` is imported with `sys.dont_write_bytecode` set first, the line the recall kit itself
carries so that an import writes nothing inside an adopter's tree.

### The superseded-by map

Derived by `TOOL-aGraftedHelix-4`'s two functions and no third: `extract_supersessions` over every
file `extract.corpus_inputs(root)` lists, against that file's `extract_records`, then one
`derive_supersession_map` over the edges with every anchored id as `defined`. Those are the calls
that unit's cache builder makes in `query.py`'s `_docs`, so the map is the one a session is served.
It costs a corpus walk, so it is derived LAZILY: only when at least one near match is unsatisfied by
its names and the relation tokens, and once per run. A finding's tag is that unit's:
`[superseded by <id>, …]` for a whole edge, `[partly superseded by <id>, …]` otherwise.

`extract.py` binds its id grammar to the repository the recall kit is installed in, which is the
audited repository on every real run. An arm that reaches this map therefore runs a copy-install
fixture, the kit directories copied into the fixture repository, so that the fixture IS the kit's
repository. An arm calling it against a foreign root would grade the wrong grammar and pass, which is
`memory/gotchas/grammar-bound-to-the-wrong-root.md`.

### The replay

`--measure-relations` reads the history the way §8 F1's probe did. A row's add commit is the first
commit in `git log --reverse -m -p` over the decision index and its archives whose diff adds a line
the row grammar keys with that id, and a gotcha's is the first `--diff-filter=A` commit naming its
path in the same walk. The `-m` matters: two rows at `5266d22e` entered in a merge's own resolution
and have no other add commit.
OLDER means an add commit with an earlier committer time. Only records present at `HEAD` are ranked
or ranked against, texts are read at `HEAD`, and each record is ranked against the older records
with steps 1 to 5 above. It prints, per band edge 0.10, 0.125, 0.15, 0.175 and 0.20, how many records
would be flagged, then every flagged pair at the floor it was given.

### Output

A finding, one line per unsatisfied near match, with `WARN` in place of `check 27:` under `warn`:

```
check 27: TOOL-x-12 (memory/DECISIONS.md:140) near-matches TOOL-y-3 [superseded by TOOL-y-9] at 0.143, shared `scoping` — name it, or carry supersedes <id>, coexists-with or disputes
```

The remedy names `supersedes <id>` rather than the bare token, because only that form reaches
`TOOL-aGraftedHelix-4`'s map; a bare token still satisfies the check.

On every armed run, red or green, one summary line, and unarmed the NOT ARMED line instead:

```
row-grammar: check 27 graded <n> added record(s) in <base8>..HEAD against <m> at base — <k> near match(es), <s> satisfied, <o> own-session, mode <red|warn> floor <f>
row-grammar: check 27 NOT ARMED — NEAR_MATCH_GATE is blank, so no added record was compared
```

### Inventory

| identifier | kind | cell |
|---|---|---|
| `scan_records` | function | `py.function` |
| `scan_added_records` | function | `py.function` |
| `derive_relation_base` | function | `py.function` |
| `measure_near_match` | function | `py.function` |
| `check_relations` | function | `py.function` |
| `cmd_check_relations` | function | `py.function` |
| `cmd_measure_relations` | function | `py.function` |
| `read_relation_gate` | function | `py.function` |
| `RELATION_CHECK` | module constant | none graded |
| `FM_RE` | module constant, moved | none graded |
| `NEAR_MATCH_GATE` | conf key | none graded |
| `--check-relations`, `--measure-relations` | CLI flags | none graded |

Every function name was answered `OK` by `lexicon.py --suggest <name> --as py.function`. The
constants and the conf key sit in no declared naming cell, which `py.constant` being undeclared
confirms.

### Rollout

The unit lands armed red in this repository, so its own close bar grades every row and gotcha this
build adds. Every unit of this build that appends a decision row or seeds a gotcha is graded by it
at the close, and the remedy is one relation token or one named id in a record that has not landed.

### Files touched (estimate)

- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `memory/HYGIENE.md`
- `.memory-tree.conf`
- `memory/map/features/row-grammar.md`
- `memory/guides/BUILD-METHOD.md`, line 1 only, the kit version marker the re-render moves
- the memory-tree kit's version carriers

### Alternatives rejected

- Hosting the predicate in `check-recall.py`, the recall floor leg's program. It already extracts
  and indexes the corpus, and `tools/memory-recall/kit.toml` withholds it from every adopter, so the
  mechanism would govern only this repository.
- Querying the served CLI cache through `query.py`'s fusion. Its pool ranks every anchored record,
  spec titles and backlog asks among them, and a decision row legitimately resembles its own build's
  records; filtering the pool after a top-k leaves a record with no eligible hit. Argued, not tested.
- Similarity over a gotcha's BODY rather than its description. Tested and lost; F1 records it.
- A floor of 0.10. Tested and lost; F1 records it.
- A bare relation token that must also name a record. The brief pins the three tokens as sufficient
  on their own, and a token is the cheap remedy for a false positive; the header states the gap.
- Reading the map from the query cache's `manifest.json`, where `TOOL-aGraftedHelix-4` stores it.
  `query.ensure_cache` rebuilds that cache whenever the corpus moved, which on a records commit is
  always, so a hygiene leg would write a shared cache under the git common dir as a side effect of
  grading. The two functions it is built from are called directly instead.
- Importing `gotchas.py` for its record reader, which `reuse_lookup.py` ranked as a seam. The row
  grammar's module takes its shared helpers from `tree_lib.py` and never from a sibling engine,
  which its `scan_engine_imports` arm keeps true, so the one piece both need, `FM_RE`, moves there.

## 5. Production-readiness checklist

- security — Read-only over tracked files and git objects; it writes nothing and runs no code from
  the corpus. The FTS5 query is built by `bench.match_expr`, which double-quotes every term.
- perf / scale — The replay in §8 F1 built one index over 354 documents and ranked every one of
  them in 0.7 s wall on node `a`. A check run builds the same index once and ranks only the added records,
  plus the git spawns that read the base: one merge-base, two tree listings and one `git show` per
  row document.
- error / empty / loading states — No base while armed is a red naming it; an empty added set prints
  a graded count of 0; a blank key prints NOT ARMED; a malformed key or an absent index builder is a
  named refusal.
- observability — The summary line prints on every armed run with every count in it, and the
  hygiene dispatch block shows it on a green run.
- risks — Measured precision is 0.63, so about one finding in three is not a true relation; each
  costs one token in a record that has not landed. The precision was hand-graded by this spec's
  author, which the spec audit can re-grade from §4 "The graded pairs".
- testing — `row_grammar.py --selftest` arms for every branch (AC1 to AC7, AC12), the header
  (AC13), and the replay instrument observed against the recorded pairs (AC8).
- migration — None in this tree beyond declaring the key. An adopter's example conf ships it blank.
- user docs — Check 27's catalog entry in `memory/HYGIENE.md`, rendered from the kit template, and
  the kit README's row for the two modes.

## 6. Acceptance criteria

- **AC1** — When a `--selftest` fixture commits a base, then adds a decision row restating a base
  row under a new id, and `row_grammar.py --check-relations <base>` runs under `red:0.125`, it exits
  1 and prints one `check 27:` line naming the new id and the base row's id. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: the restated row is graded as no near match, or the line names a different hit.
- **AC2** — When the same fixture row also carries `coexists-with`, and separately when it instead
  names the base row's id, `--check-relations <base>` exits 0 and its summary line counts the match
  as satisfied. Observed by `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: either form still prints a `check 27:` finding.
- **AC3** — When a fixture adds a gotcha whose `description` restates a base gotcha's, the mode reds
  naming both stems; when the added gotcha's body names the base stem, it exits 0. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: the gotcha pair is never compared, or naming the stem in the body does not satisfy it.
- **AC4** — When the fixture's conf declares `NEAR_MATCH_GATE="warn:0.125"`, the AC1 row prints a
  `WARN` line and the mode exits 0. Observed by `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: warn mode exits 1, or prints nothing.
- **AC5** — When `NEAR_MATCH_GATE` is blank, the mode exits 0 and prints `NOT ARMED`; when it is
  `red:1.5` or `amber:0.1`, it refuses naming the key and prints no traceback. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: a blank key compares anything or stays silent, or a malformed value reaches a traceback.
- **AC6** — When the key is armed and the fixture install holds no recall kit `bench.py`, the mode
  refuses naming the recall kit and the key, and prints no traceback. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: an absent kit reads as a clean range.
- **AC7** — When the key is armed and the fixture has no `origin/main` and no `main`, the mode exits
  1 naming `no mainline base`; when the base equals `HEAD`, it exits 0 with a graded count of 0.
  Observed by `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: a missing base exits 0, or an empty range prints no graded line.
- **AC8** — When `python tools/memory-tree/row_grammar.py --measure-relations 0.125 5266d22e` runs on
  this tree, its flagged list is exactly the 30 pairs §4 "The graded pairs" lists, and its 0.125
  band counts 23 rows and 7 gotchas.
  Red when: a pair is missing or added, which means the shipped predicate is not the one F1 measured.
  figure: PINNED, measured 2026-10-04 on node `a`; the base argument holds the population at the
  one the measurement saw, so later records cannot move it.
- **AC9** — When `python tools/memory-tree/row_grammar.py --check-relations 5266d22e` runs on this
  tree at the unit's build commit, its summary line names a graded count equal to an identity set
  difference derived at observation, whatever its exit. The figure is the gotcha stems
  `git ls-tree --name-only HEAD memory/gotchas/` lists that the same listing at `5266d22e` does not,
  `INDEX.md` excluded, plus the row ids the row grammar keys across the decision index and its
  archives at `HEAD` and not at `5266d22e`.
  Red when: the summary's graded count differs from that figure, whether by dropped rows, a missed
  archive or a rename counted from added diff lines.
  figure: DERIVED at observation, by identity and never by `--diff-filter=A` lines, whose default
  rename detection drops a renamed gotcha.
- **AC10** — When `grep -n 'RELATION_CHECK = 27' tools/memory-tree/row_grammar.py` and
  `grep -n 'check-relations' tools/memory-tree/check-memory-hygiene.sh` run, each prints one line.
  Red when: the constant or the dispatch block is absent.
- **AC11** — When `grep -c '^27\. ' memory/HYGIENE.md` runs, it prints 1, and the kit README's row
  for `check-memory-hygiene.sh` reads `27 checks`. `grep -n '^NEAR_MATCH_GATE=""' tools/memory-tree/.memory-tree.conf.example`
  prints one line, and `grep -n 'NEAR_MATCH_GATE="red:0.125"' .memory-tree.conf` prints one line.
  Red when: the catalog or the README count disagrees with the module constant, or the example conf
  arms check 27 in every new adopter at a floor measured on another corpus.
- **AC12** — When a copy-install `--selftest` fixture holds a base row, a later base row reading
  `SUPERSEDES <the first id>`, and an added row restating the first while naming only the second,
  `--check-relations <base>` counts the match as satisfied; with the naming taken out it reds and
  the finding carries `[superseded by` and the second id. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: naming the successor does not satisfy, or the finding carries no tag.
- **AC13** — When the header of `tools/memory-tree/row_grammar.py` is read, it states that check 27
  does NOT check a near match below the top hit, a paraphrase under the floor, a bare relation token
  that names no record, or a row edited in place.
  Red when: any of the four is unstated.
- **AC14** — When a `--selftest` fixture holds `origin/main` behind a local `main` and a branch
  adding one restated row, `--check-relations` with no argument names the merge-base of
  `origin/main` and `HEAD` as `<base8>` and grades exactly that row. With `GOV_DEFAULT_BRANCH=trunk`
  and only `trunk` present, it resolves `trunk`. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: the derivation takes a branch tip, prefers a stale local `main`, or ignores
  `GOV_DEFAULT_BRANCH`, which the hygiene dispatch, the production caller, would inherit.
- **AC15** — When `git diff <the pass's parent sha> -- memory/guides/BUILD-METHOD.md` runs at the
  pass's commit, it changes line 1 only.
  Red when: the method's content moved, which shared invariant 10 forbids.

## 7. Gates

`memory hygiene` · `row-grammar selftest` · `gotchas selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)`

A pass runs `python tools/memory-tree/row_grammar.py --selftest` as its direct check, each new arm
observed red on a staged break first; the close runs the legs listed above. The four recall,
transition-audit and straggler-guard legs are owed by the guards of the memory root and the conf
this unit's write set reaches, and the last three grade S9's kit version bump.

New arm: `tools/memory-tree/row_grammar.py --selftest` · fixture repos with a base commit, a restated row, a restated gotcha description, warn and blank keys, a malformed key, an absent recall kit and a missing base · the module's arm count rises by the new arms

## 8. Open questions

- **FACT-QUESTION · F1 — does check 27 ship red or warn, and at what floor?** The brief's rule: red
  only when measured precision at the floor reaches the review protocol's floor of 0.5, otherwise
  warn. Probe: replay every decision row and gotcha present at `HEAD`, 354 records, each ranked
  against the records older than it with §4's predicate and §4 "The replay", then hand-grade every
  flagged pair; 27 top hits were own-session rows and were not graded. A pair is TRUE when the new
  record restates, refines, narrows, extends, corrects or contradicts the hit's specific claim, so
  that a reader of one is misled without the other; FALSE when the two share a theme and make
  independent claims. Liveness: the probe reads below the floor as readily as above it. A first cut
  that measured gotchas by their BODY flagged 19 unsatisfied gotcha pairs at 0.175 and graded only 3
  TRUE, and the sub-0.125 band below grades 3 of 14.
  Observation, with the §4 construction (description summaries, satisfaction over the whole record):
  at floor 0.125, 30 flagged pairs, 23 from rows and 7 from gotchas, and 19 TRUE, so precision 0.63.
  Rows grade 15 of 23 and gotchas 4 of 7. At 0.15 the set is 10 pairs, 8 TRUE, precision 0.80.
  Below 0.125, the band down to 0.10 holds 57 more pairs, and a sample of 14 of them graded 3 TRUE,
  which puts the cumulative precision at 0.10 near 0.36; for it to reach 0.5 the band would need
  0.43. That sample was drawn from an earlier cut of the replay whose population differed by a few
  rows and whose gotcha naming read the description alone. Every pair at 0.125 and its grade is §4
  "The graded pairs".
  Options: (a) red at 0.125, the lowest band edge whose cumulative precision clears 0.5; (b) red at
  0.15, fewer and more precise findings; (c) warn at any floor. The observation removes (c) and every
  floor below 0.125, since 0.63 clears 0.5 there and the next band down does not. Between (a) and
  (b) M3's rule takes the more feature-rich, (a), which catches 19 true relations against 8.
  RESOLVED (agent, 2026-10-04, delegated): (a), `NEAR_MATCH_GATE="red:0.125"` in this
  repository, blank in the kit's example conf.
- **F2 — Does the memory-tree bump's re-render of line 1 of `memory/guides/BUILD-METHOD.md` breach
  shared invariant 10, which says no unit edits that file?** `TOOL-aGraftedHelix-3` §8 F1 decided
  this for the kit's version marker: the line is a derived carrier `check-kit-versions.sh` pairs
  with the engine constant, and the invariant protects the method's content, which the render
  leaves byte-identical below line 1. RESOLVED (agent, 2026-10-04, delegated): as unit 3's Option
  A, the file listed under Files touched as line 1 only, and AC15 observes that only line 1 moved.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft from the aGraftedHelix spec brief, with F1 measured by replay
  on node `a` at base `5266d22e`.
- rev-2 · 2026-10-04 · §3 §4 §6 §7 §8 · S2 S5 S9 · AC9 AC11 AC14 AC15 · folded the round-1 spec
  audit's findings on this unit: 28 (AC14, the no-argument base derivation the hygiene dispatch
  uses); 29 (AC11 greps the example conf's blank `NEAR_MATCH_GATE` and this repository's armed
  value); 30 (AC9 derives its equality as an identity set difference); 36 (§7 states that the pass
  runs the module's `--selftest` as its direct check); and 37 (`memory/guides/BUILD-METHOD.md`
  line 1 listed, §8 F2 citing unit 3's ruling, AC15). §3 Edges: the consumes-from
  `TOOL-aGraftedHelix-4` is amended as the mirror of finding 34's correction, and the finding's
  remedy text in §4 now names `supersedes <id>`; the hands-off to `TOOL-aGraftedHelix-6` adds the
  base derivation that unit now uses (finding 48); and a hands-off to the unit promoted from
  finding 27 is added.

## 10. Reuse audit

The seams extended, each verified against source at base `5266d22e`: the row grammar and its walk in
`tools/memory-tree/row_grammar.py` (`row_docs`, `scan`, and `--check-rotation` as the precedent
for a second mode on one module); the recall kit's `bench.build_index`, `bench.match_expr`,
`bench.terms` and `bench.ALIAS_WEIGHT` in `tools/memory-recall/bench.py`, which `query.py`'s own
cache builder calls; the canonical `resolve_kit_dir` block and `corpus_ids.py`'s armed-only
cross-kit refusal; and `check-verdict-epoch.sh`'s base derivation. `reuse_lookup.py` with "flag a
newly added decision row or gotcha that closely resembles an existing record" ranked `records` in
`tools/memory-tree/gotchas.py` first as a seam; it is not imported, for the reason §4 "Alternatives
rejected" gives, and its front-matter pattern moves into `tree_lib.py` instead. The probe's
`unscanned layers: .sh` line means the hygiene engine's shell was read by hand, which is where the
check 24 dispatch block was found. The recall query found no existing check: its hits were this
build's own mandate and brief, `TOOL-cSpliceWarden-6` (a check grading rows delegates to the
grammar's owner, which §4 follows), and records about check 20's per-file id uniqueness, which
grades ids and not content. Where a hit was stale: none of the cited records disagreed with the code.

Recall terms used: `prior art near-duplicate decision row gotcha supersedes contradiction similarity recall index spec-audit lens two-answers-to-one-question`
