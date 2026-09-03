# Measurements — the four kits in four scratch clones

**Serves:** journal TOOL-aProbedToolkit-1

Node `a`, 2026-09-03. BASE `51444cc1`. Every number below names the command that produced it. The
scratch clones are `git clone --local` copies under `/tmp/kite`; nothing here was run inside a real
checkout. The captured stdout of every run is under `/tmp/kite/out/`, which is scratch and is not
committed — the numbers are, and each is re-derivable from the command beside it.

## Subjects, and one corrected premise

`C:/projects/nicocares` is not a repository. It is an asset directory whose `main` entry is a
symlink to `C:/projects/incms/main/vendor/nicocares-package`, which IS its own git repository, nested
inside incms/main's working tree. Command: `git -C C:/projects/nicocares/main rev-parse --show-toplevel`.

| subject | clone | tracked files |
|---|---|---|
| coding-governance | `/tmp/kite/gov` | 1393 |
| incms/main | `/tmp/kite/incms` | 6347 |
| nicocares-package | `/tmp/kite/nc` | 1879 |
| swydee | `/tmp/kite/swydee` | 133 |

`git clone --local` into the session scratchpad failed on all four with `Filename too long`: the
scratchpad path plus a pack filename exceeds the Windows path limit. `/tmp/kite` is short enough and
is still inside the `TEMP` root the scratch guard derives, so it is allowed. Worth knowing before the
next session tries to clone a repository into the scratchpad.

## Kit presence and version, as installed

Command: read each kit's declared version marker (`version_from` in its `kit.toml`) in every clone.

| repo | memory-tree | memory-recall | lexicon | codebase-map | prefix |
|---|---|---|---|---|---|
| gov | 2.55 | 1.4 | 1.1 | 1.3 | `tools/` |
| incms | forked to `scripts/check-docs-hygiene.sh`, no version marker | forked to `scripts/recall/`, no `recall_conf.py` | 1.1 | 1.3 | `scripts/` |
| nc | 2.49 | 1.4 | 1.1 | 1.3 | `scripts/` |
| swydee | 2.2 | 1.0 | absent | absent | repo root |

`swydee` is 53 minor versions behind on memory-tree. Its gate defines `fail` branches 1 through 12;
gov 2.55 defines 1 through 12 plus 21, 22 and 23.

## Corpus sizes, derived before any kit was asked

Command: `git -C <clone> ls-files | grep -E '^memory/'` piped through `awk -F/` and `uniq -c`, plus
`wc -l` on each `DECISIONS.md`.

| repo | builds | DECISIONS.md lines | gotcha records | map dossiers | backlog shards |
|---|---|---|---|---|---|
| gov | 88 | 127 | 38 | 19 | 4 |
| incms | 312 | 326 | 232 | 84 | 5 |
| nc | 78 | 429 | 41 | 7 | 2 |
| swydee | 10 | 47 | 0 | 0 | 4 |

## Conf coverage — a kit deployed is not a kit adopted

Command: test for each conf file at each clone's root.

| repo | `.memory-tree.conf` | `.codebase-map.conf` | `.lexicon.conf` | `.unattended.conf` |
|---|---|---|---|---|
| gov | present | present | present | present |
| incms | present, 2 live keys | present | ABSENT | present |
| nc | present | present | ABSENT | present |
| swydee | present | ABSENT | ABSENT | ABSENT |

incms's `.memory-tree.conf` carries exactly two non-comment keys, `MEMORY_ROOT` and `ARMS_FLOORS`;
gov's carries thirty. Every conf key whose blank value means "skip" is therefore skipped there.

`nc/.governance/install.json` lists `lexicon` among fifteen installed kits, and `nc/scripts/lexicon/`
holds the whole engine — with no `.lexicon.conf` and no lexicon row in `nc/scripts/gate-legs.json`.
The same is true of incms. The kit is deployed and inert in both, which makes its live adoption count
one: this repo.

## What each kit reported

Full index at `/tmp/kite/out/mech.txt`; one file per run beside it. Exit codes as measured.

### lexicon

`python tools/lexicon/lexicon.py --check` in gov:

```
lexicon: P1 verb   graded=1047 offenders=461 waived=0
lexicon: P2 suffix graded=39 offenders=0 waived=0
lexicon: P3 layer  graded=548 offenders=0 waived=0
lexicon: coverage — armed 58 of 138 definition-carrying file(s) (42.0%)
lexicon OK — 1393 tracked file(s); coverage: .js=probe, .py=parser, everything else dark
```

Exit 0, with 44 % of graded names offending, because `VERB_OFFENDER_PIN="461"` in `.lexicon.conf`
equals the measured count. The dark half is not small: `git ls-files "*.sh" | wc -l` is 89 files, and
those hold 573 shell function definitions against 928 python `def`s. Roughly a third of the
definition population is invisible by declaration.

In incms and nc the same command prints `lexicon: NOT ADOPTED — no .lexicon.conf at the repo root;
the kit is opt-in and inert without it` and exits **0**. `tools/lexicon/kit.toml` declares three
`[[hole]]` rows, all `blocks_gate = true` — the table's ratification stamp, the empty `LAYERS`
declaration, and the three measured pins. Adoption stalls because it is designed to stall until an
adopter discharges all three, and nothing surfaces the holes after `govkit apply` copies the engine.

### codebase-map

`python <kit>/selftest.py`, run in all four clones. The interesting rows are the last two:

| repo | the js-probe arm | the corpus-recall arm | summary |
|---|---|---|---|
| gov | `ok` (it really ran) | `ok` (it really ran) | `PASS` |
| nc | prints `SKIP … NOT a pass`, then `ok` | prints `SKIP … NOT a pass`, then `ok` | `PASS` |
| incms | prints `SKIP …`, then `SKIP … the arm declined to run; NOT a pass` | same | `PASS` |

`tools/codebase-map/selftest.py:51` is a `check()` that prints `ok <name>` whenever the arm returns
without raising, and four arms `return` early after printing an indented `SKIP … NOT a pass` line.
gov's copy and nc's are byte-identical (`git hash-object` gives `82acb99d` for both); incms's differs
(`21f3c8d1`) and carries a comment naming the delta: *"INCMS DELTA D2 (ARCH-aFerriedToolkit-1) — the
SKIP sentinel. An arm that returns this instead of asserting is reported as SKIP, not ok."* All three
files declare `KIT_CODEBASE_MAP_VERSION = "1.3"`.

So the two arms that measure the map's actual quality — recall against ground-truth identifiers, and
the JS definition probe against an independent implementation — are inert in every adopter, and the
row above them says `ok`. The fix exists in an adopter's fork and was never carried back. The arm's
own docstring at line 1239 claims the opposite: that an adopter is "TOLD the arm did not run, rather
than shown a green it did not earn".

The js-probe arm also resolves the lexicon at `m.repo_root() / "tools" / "lexicon"`
(`selftest.py:1243`), and lines 1287 and 1290 hardcode the same prefix. incms installs the lexicon at
`scripts/lexicon/`, so the skip reason it prints there — "tools/lexicon/ is not installed here" — is
false. `map_lib.kit_dir()` exists and was not used.

`python scripts/codebase-map/gen_map.py --check` in incms crashes:
`ModuleNotFoundError: No module named 'pydantic'`, raised from `map_extractors.py:75`'s
`from app.services import feature_flags`. `.codebase-map.conf` declares `MAP_DIFF_CMD` so `map_diff`
can be launched under `uv run`; there is no equivalent declared launcher for `gen_map`, so the
documented invocation is the one that fails.

`python scripts/codebase-map/reuse_lookup.py "resize and optimise an image asset"` in nc:

```
# corpus: 0 symbols | 197 inventory keys | 6 affordance seams | 7 dossiers
no seam fits - nothing in the corpus shares a token stem with the query.
note: symbol recall tier not adopted (inventory + affordance corpus only).
```

Zero symbols in a 1879-file repository. The note is printed, which is the right behaviour; the
freshness gate `gen_map.py --check` is nonetheless green in that state, at exit 0 with no output.

The same CLI in incms returns 35 334 bytes over 365 lines for one query, against 5 367 bytes in gov.
`query.py` bounds its output by a byte budget and explains at length why bytes are the right
quantity for a model consumer; `reuse_lookup.py` bounds nothing.

`map_diff.py:266-270` computes `mapped_count / len(files)` over every changed file with no exclusion
for `MEMORY_ROOT`. Over the last thirty commits: gov reports 21 % mapped, and 182 of its 199 unmapped
files are under `memory/`; nc reports 8 %, with 185 of 262 under `memory/`. Excluding records, gov's
real source attribution over that range is 54 of about 71. The help text calls this line "the map's
convergence-visibility metric".

Duplicate claims exist and are not gated: `map_lib.py:1030` raises on duplicate feature NAMES, and
nothing rejects one inventory key claimed by two dossiers. Measured over `memory/map/features/*.md`,
`gotcha-classes: bounded-through-a-pipe-is-unbounded.md` is claimed by both `run-gates.md` and
`unattended.md`.

### memory-tree

`bash scripts/check-memory-hygiene.sh` in nc produced 178 bytes and exit 0:

```
HYGIENE check 21: NOTE branch A reports 0 unbound record(s) in reach; out of reach are 490 dated
before RECORD_SERVES_CUTOFF=2026-08-28 and 122 whose name carries no date at all
```

Zero records in reach out of 612. The same gate in swydee produced zero bytes and exit 0.

`python scripts/gen_build_index.py --check-format` in nc exits 1:
`memory/project/readme-contract.txt is absent; the heading canon and the slot budgets would then bind
nothing and report clean, which is coverage of nothing`. Correct refusal, and it means that leg has
never been runnable there.

The same verb in gov exits 0 after printing 8 789 bytes of `ADVISORY — a slot passed its recorded
high-water`. An advisory that fires across most of its population is read by nobody.

`python tools/memory-tree/corpus_ids.py --check` in gov reports one finding under check 16 and says
it is "REPORTED, not gated — this tree never declared the retired read-path ceiling, so these rules
have never run here".

swydee's own `memory/backlog/EXTR.md` carries two OPEN rows filed against this kit:
`EXTR-aPatientHarvest-3` (the playbook prescribes a singular `review/` folder while hygiene check 4
sanctions only `reviews/`) and `-4` (TEMPLATE-SPEC says a terminal §8 may be "none or fully
RESOLVED" while check 12 accepts only a first line starting `none`). Checked against gov 2.55: the
first is fixed — §8 of the current template names `memory/builds/<slug>/reviews/`, plural — and the
second is fixed too, at `check-memory-hygiene.sh:1022`, which now admits `items > 0 && items ==
resolved`. Both rows are still OPEN in swydee, and swydee still runs 2.2. Nothing carried either fix
down or closed either row.

### memory-recall

`python tools/memory-recall/selftest.py` passes 38/38 in gov and in nc; incms's forked
`scripts/recall/selftest.py` passes 106/106 over a much larger surface. The selftests are hermetic,
so they pass in a repo where the kit retrieves nothing.

`python tools/memory-recall/check-recall.py` in gov:

```
check-recall: per-id ok -- every expected id resolves in records (12/12 questions)
check-recall: cell records:fts5:r@5  raw 0.8333  ceiling 1.0000
check-recall: RECALL_FLOOR ok -- normalised 0.8333 >= 0.81
```

This is the only measured quality floor any of the four kits carries, and `tools/memory-recall/kit.toml`
withholds it from adopters by role: `recall-fixture.json`, `check-recall.py` and
`test_recall_floor.py` are `project-owned`, so `govkit apply` never writes them. The reasoning in the
descriptor is sound — a floor measured on this corpus is vacuous or permanently red on another — but
the consequence is that no adopter has any retrieval-quality signal at all.

## Provenance recorded by the deployer

`nc/.governance/install.json` records `gov_commit`, and per file the `gov_oid`, the `carry` mode and
an `evidence` verdict. So the machinery to detect a stale adopter exists. nc is nonetheless at
memory-tree 2.49 against gov's 2.55, and carries the codebase-map selftest defect byte-for-byte.

## What an upgrade would cost, measured

The question behind every version gap above is what happens if an adopter takes the current kit. So
each adopter's clone was copied, the current `tools/memory-tree/*.py` and `*.sh` were overlaid on its
install prefix, and the gate was run. Command:
`cp -r nc up/nc && cp gov/tools/memory-tree/*.py gov/tools/memory-tree/*.sh up/nc/scripts/ && (cd up/nc && bash scripts/check-memory-hygiene.sh)`.

| adopter | from | to | checks that go RED | offending lines listed |
|---|---|---|---|---|
| swydee | 2.2 | 2.55 | 9, 12, 21 | 7 |
| nicocares-package | 2.49 | 2.55 | 3, 4, 5, 9, 21 | 612 |

Both trees are green on the version they run. The reds are not defects in those trees; they are
requirements the kit added after the adopter installed it. Check 21 wants a `**Serves:**` line on
every record under `build/`, `prompts/` and `reviews/`. Check 4 rejects the `memory/builds/*/STATUS.md`
file that was the sanctioned shape until kit 2.17. Check 5 rejects free-named recording files.
Check 3 rejects four `memory/project/*.txt` registries the current structure lint does not know.
Check 21 additionally refuses outright because `RECORD_UNBOUND_PIN` is undeclared — a conf key that
did not exist when either adopter installed, which must be MEASURED against their corpus.

There is no migration verb. `adopt-memory-tree.sh` scaffolds a fresh tree; nothing converts a tree
that conformed to an earlier version. That is the mechanical reason both adopters are behind, and it
is why a fix landing in gov does not reach them: taking the fix means taking the corpus migration
with it.

For contrast, this repo's own gate on the records this unit adds:
`bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with 386 bytes, both of them the standing
check-16 note that those rules "have never run here".

## How much of each system the map actually holds

`map_diff`'s coverage line is computed over a git range, so it answers a different question from "how
much of this repository is in the inventory". That one was derived directly: load each repo's map
tree through its own `map_lib`, attribute every tracked path, and split the result.

| repo | all tracked | mapped | non-record source | mapped | code only | mapped |
|---|---|---|---|---|---|---|
| gov | 1393 | 14 % | 248 | 67 % | 179 | 72 % |
| incms | 6347 | 73 % | 2930 | 42 % | — | — |
| nc | 1879 | 1 % | 713 | **3 %** | — | — |

The two columns disagree in opposite directions and for the same reason: gov's dossiers claim almost
no records, so its all-tracked figure is dragged down by 1145 record files; incms's dossiers glob the
memory tree, so 3417 of its 4670 "mapped" files are records rather than source. Neither number is
wrong, and the one the tool prints is neither of them.

nicocares is the case that matters. 28 of 713 non-record source files are claimed, 685 are not, and
`python scripts/codebase-map/gen_map.py --check` exits 0 with no output in that state. Its
`reuse_lookup` corpus holds 0 symbols. The kit's guarantee is real but narrower than its name: the
ratchet reds on an unclaimed INVENTORY KEY, never on an unclaimed file, so a map describing 3 % of a
system is a passing map.

Command, per repo:
`python -c "import sys,subprocess; sys.path.insert(0,'<kit>'); import map_lib as m, map_extractors as ext; ..."`
— load the map tree, `m.attribute_paths` over `git ls-files`, then split `UNMAPPED` on the
`memory/` prefix. Full script in the session transcript.

One correction to the crash recorded above: incms's `map_extractors` imports fine and
`inventory_ids()` works. The `pydantic` failure is raised by `all_inventories()` through
`inv_flags()`, which only `gen_map.py` calls. So the freshness gate is the broken path, not the
attribution one.

## Two smaller measurements

`tools/memory-tree/gotchas.py` selects a checklist per path, and the UNIVERSAL half is uncapped. For
one file: gov selects 5 classes of which 4 are universal, out of 38; incms selects 3 anchored plus
**46 universal** out of 223. The universal set grows with the corpus, so the instrument gets less
usable exactly as the corpus it depends on gets richer. Nothing caps or decays it.

`selectable()` at `gotchas.py:196` matches an anchor to a path by bidirectional substring
(`anchor in p or p in anchor`) plus tree-wide basename equality. The looseness is deliberate and its
rationale is written above it; it is also why a large tree produces long checklists.

Fourteen files across the four kits independently enumerate the tracked file set
(`git ls-files` / `os.walk` / `rglob`). Each answers a different question, so this is not duplication
to collapse, but it is fourteen places that must agree about what this repository contains.

`swydee`'s memory-tree 2.2 has no `--for-paths` verb at all; the usage line offers `--for-diff` only.
`AGENTS.md` and the kickoff skill both instruct a session to run `--for-paths`, so in that adopter
the instruction names a flag the installed kit does not have. Unknown flags exit 2 in every copy
checked, so this fails loudly rather than silently.

## Is any of this actually used? The two instruments that log

`memory-recall` writes a query log under the common git dir, so live use is measurable rather than
assumed. Command: read `$(git rev-parse --git-common-dir)/recall/queries.jsonl` on the real checkout.

- 187 events since the kit landed: 124 queries, 62 `opened` records, 1 refusal.
- Of the 62 opened records, 17 carry a RANK. Median rank 6; 8 of 17 in the top 5, 12 of 17 in the top
  10, worst 37. All 17 are `inferred`, meaning the hook attributed them — no session called
  `--opened` explicitly.

So the kit is genuinely used, and the record a reader actually opened sat at median rank 6 against a
fixture floor stated as `records:fts5:r@5>=0.81`. The floor's twelve questions are curated and the
live queries are not, and n is 17, so this is a signal rather than a verdict — but the two numbers
measure different things and only one of them is on the bar.

`codebase-map`'s reuse probe is measurable a different way, through the specs that are supposed to
cite it. Over 457 tracked specs: 418 carry a section 10, 217 cite `reuse_lookup`, 182 carry a
`Recall terms used` line — and **3** say "no existing seam fits". A probe that almost never returns
"nothing fits" is either finding a real seam every time or is being cited rather than run. The
check grades presence, and its own template says so: "What the check still cannot see is whether
either fact is TRUE: a citation naming the wrong seam satisfies it."

## The one quality floor, and who gets it

Each kit ships a pin mechanism, and they are not the same kind of thing. `memory-tree`'s
`DEAD_PATH_PIN`, `ORPHAN_ID_PIN` and `RECORD_UNBOUND_PIN`, the lexicon's three offender pins, and
codebase-map's shrink-only baseline are all DEBT RATCHETS: they bound how much known-bad exists and
say nothing about whether the instrument works. `memory-recall`'s `RECALL_FLOOR` is the only one that
measures OUTPUT QUALITY — and `tools/memory-recall/kit.toml` withholds it from adopters by role, for
a stated and correct reason. The consequence is that the only kit with a quality floor is the only
kit whose adopters have none.

## Retrieval graded exactly, on the corpus small enough to hold whole

swydee's decision surface is 47 rows and ten builds, so its answers can be established by reading
rather than by trusting the instrument. Six questions were chosen from `memory/DECISIONS.md` and the
answering id recorded BEFORE any query ran. Then `python memory-recall/query.py "<q>" --terms "<12
words of swydee's jargon>"` was run for each, on that repo's own memory-recall 1.0. Script kept at
`/tmp/kite/recall_grade.sh`, output at `/tmp/kite/out/recall-swydee.txt`.

| expected id | rank of the answering record |
|---|---|
| EXTR-aPatientHarvest-1 | 2 |
| EXTR-aUniformLattice-1 | 1 |
| ANLZ-aUniformLattice-8 | 2 |
| ANLZ-aUniformLattice-7 | 1 |
| ORCH-aFlattenedLedger-1 | 2 |
| ORCH-aFlattenedLedger-3 | 1 |

Six of six in the top two, on a two-versions-old copy, over an index of 31 records and 2320 chunks.
The retrieval works.

What it costs is the other half. One query's output there is 8663 bytes; swydee's entire
`DECISIONS.md` is 7812. Reading the whole decision log is cheaper than asking one question about it.

| repo | `DECISIONS.md` | whole `memory/` | one query | query ÷ DECISIONS.md |
|---|---|---|---|---|
| gov | 27 213 B | 20 136 177 B (1145 files) | 16 036 B | 0.59x |
| incms | 66 605 B | 56 838 701 B (3417 files) | 15 569 B | 0.23x |
| nc | 107 936 B | 21 827 070 B (1166 files) | 15 803 B | 0.15x |
| swydee | 7 812 B | 1 211 619 B (53 files) | 8 663 B | **1.11x** |

The kit's value scales with the corpus, and there is a crossover below which reading beats querying.
swydee is under it. Nothing in the kit says so, and `adopt-memory-recall.sh` has no floor on corpus
size — a fresh adopter is told to install an index over a decision log they could paste.

## The ratio nobody measures

| repo | source bytes | record bytes | records / source |
|---|---|---|---|
| gov | 6 538 738 | 20 136 177 | **3.1x** |
| incms | 35 318 639 | 56 838 701 | 1.6x |
| nc | 79 501 514 | 21 827 070 | 0.3x |
| swydee | 1 636 305 | 1 211 619 | 0.7x |

In the repository that ships the memory tree, the tree is three times the size of the source it
describes, over 1145 record files against 248 non-record ones. The charter's rule is that memory
carries only the non-derivable. No check anywhere measures this ratio, and none of the kit's caps
bound the tree as a whole — `INDEX_CAP_BYTES`, `GUIDE_CAP_BYTES` and `DOSSIER_CAP_BYTES` each bound
one file class, and `TOOL-dFoldedVerdict-7` already records three carriers sitting exactly on their
ceiling.

## What the 461 lexicon offenders actually are

The declared table is 23 verbs: `build load read write parse render resolve check scan extract
measure derive seed init run arm add remove set print main cmd test`. `python
tools/lexicon/lexicon.py --list` in `/tmp/kite/gov` prints all 461 P1 offenders; 83 of them are in
`selftest`/`test_` files. The most frequent offending leading tokens are `a` (18), `git` (13),
`demand` (10), `signal` (8), `kit` (7), `is` (7), `bounded` (7).

Named offenders, taken verbatim from the kit's own source: `map_lib.py:113 repo_root`,
`map_lib.py:122 kit_dir`, `map_extractors.py:55 _git_hooks`, `map_extractors.py:71 _gate_legs`,
`map_extractors.py:249 inventory_ids`, `map_diff.py:62 _changed_files`, `agent-cap.js:1123 why`,
`agent-cap.js:358 key`, `agent-cap.js:1272 slug`.

None of those is a naming defect. `repo_root()` returns the repo root; it does one thing and has the
clearest available name. The table has no row for a noun accessor, none for an `is_`-shaped boolean
predicate — the single most standard convention in the language it grades — and none for a test arm.
So the offender count is dominated by a mismatch between the predicate's population and the table's
scope, not by naming debt, and `VERB_OFFENDER_PIN="461"` freezes that mismatch as the baseline.

This also falsifies the kit's own stated justification, which the charter carries: "a name that will
not fit is reporting an unclear responsibility". `repo_root` and `kit_dir` do not fit and report
nothing of the sort. The claim is testable and it fails on the kit's own code.

## The minimal repro for the skip-reads-as-pass defect

It does not need an adopter. In a clone of THIS repository:

```bash
git clone --local C:/projects/coding-governance /tmp/repro
cd /tmp/repro && mv tools/lexicon tools/_moved
python tools/codebase-map/selftest.py
```

Output, verbatim and adjacent:

```
     SKIP js-probe cross-check: tools/lexicon/ is not installed here, so the independent
     definition set this arm compares against does not exist. NOT a pass.
ok   js definition probe ⊇ the lexicon's own set (TOOL-dClosedLexicon-12)
...
ok   identifier tokens: corpus recall + precision floors
PASS
```

Exit 0. `check()` at `selftest.py:51` prints `ok` for any arm that returns without raising, and four
arms return after printing their own `NOT a pass` line. The summary is a bare `PASS` with no skip
count. `tools/gate-legs.json` runs exactly this argv as the `codebase-map kit selftest` leg.

The fix is eleven lines and already written, in incms's copy: a `SKIP` sentinel object that the four
guarded arms return and `check()` reports separately. It is labelled `INCMS DELTA D2
(ARCH-aFerriedToolkit-1)` in `incms/scripts/codebase-map/selftest.py`.

## One more, from the conf

`ARMS_FLOORS` is `<gate>:<branches>:<armed>`, per `check-arms.py:207`. gov declares
`tools/memory-tree/check-memory-hygiene.sh:20:20` — every failure branch has been observed firing.
incms declares `scripts/check-docs-hygiene.sh:46:16` for its fork of that gate: 46 failure branches,
16 of them ever armed. Thirty branches of the largest hygiene gate in the largest adopter have never
been seen to fire, and the floor pins that state as the baseline.

## Does the mandatory `--terms` earn its cost on a small corpus?

`query.py` REFUSES to run without `--terms`, and its help justifies the requirement by measurement:
"Rewriting is the measured half of the retrieval gain (records recall@20 0.71 -> 0.84, MRR 0.389 ->
0.530)". That measurement was taken on this corpus. The same six swydee questions were re-run with
`--no-terms`, which the CLI supports as the logged baseline:

| expected id | with `--terms` | with `--no-terms` |
|---|---|---|
| EXTR-aPatientHarvest-1 | 2 | 1 |
| EXTR-aUniformLattice-1 | 1 | 1 |
| ANLZ-aUniformLattice-8 | 2 | 4 |
| ANLZ-aUniformLattice-7 | 1 | 1 |
| ORCH-aFlattenedLedger-1 | 2 | 2 |
| ORCH-aFlattenedLedger-3 | 1 | 1 |

Mean rank 1.50 with terms, 1.67 without. Two questions ranked BETTER without them, three tied, one
worse. n is 6 and the terms were written carefully, so this is a signal rather than a verdict — but
on that corpus the expensive half of the probe bought nothing measurable, while the refusal that
enforces it is unconditional. The gain is real where it was measured and is assumed everywhere else,
which is `pin-copied-from-another-corpus` applied to a mandatory INPUT rather than to a threshold.

## Cost, since cost is a verdict

`bash <kit>/check-memory-hygiene.sh` timed in the scratch clones, quiet and uncontended:

| repo | seconds | record files |
|---|---|---|
| gov | 17 | 1145 |
| nc | 16 | 1166 |
| swydee | 3 | 53 |

The gate is cheap. Its declared ceiling in `tools/gate-legs.json` is 12720 s and the largest run in
`<git-dir>/gate-ledger.tsv` is 98.6 s, so the ceiling sits 129x above the worst observed cost. Across
the 85 legs that have a ledger row, the MEDIAN ceiling headroom is **21x**, and the widest is 315x
(`settings-merge selftest`, 300 s declared against 1.0 s measured).

The charter's rule is that a suite declares a ceiling and "a runner REDS on breach", framed as making
slowness fail rather than merely annoy. At 21x median headroom a ceiling reds on a hang, not on a
regression — a leg can get twenty times slower and stay green. That is a defensible design for a
hang guard and it is not what the rule says it buys. This one is outside the four kits under test and
is recorded because the memory-hygiene leg is the biggest instance of it.

## Numbers stated beside the thing that owns them

The owner asked about duplication. Two instances, both in a kit's own README, both of the class this
repo catalogues as `two-answers-to-one-question`:

- `tools/memory-recall/README.md:26` — "`selftest.py` | the kit's contract gate — **18 checks**".
  `python tools/memory-recall/selftest.py` ends with `---- memory-recall selftest: 38/38 checks
  passed`. `AGENTS.md` §5 deliberately does NOT restate a kit's check count, on the stated ground
  that the README owns it. The delegated owner is wrong by twenty.
- `tools/lexicon/README.md:71` — a pasted sample output reading
  `lexicon: coverage — armed 54 of 128 definition-carrying file(s) (42.2%)`. The live run prints
  `armed 58 of 138 definition-carrying file(s) (42.0%)`. A pasted sample is a copy of a derived
  number, and this one drifted.

Checked and CORRECT, so the class is not universal here: `tools/memory-tree/README.md:18` claims 23
checks split 1-12/21-23 in the shell with 13-16, 17-19 and 20 delegated, and that reconciles with the
gate's actual `fail` branches; `tools/memory-recall/README.md:31` claims 8 cases for
`recall-opened.test.sh` and the run reports 8 passed.

The same sweep found no stale numbers in `tools/codebase-map/README.md`, which states no derived
counts at all — the only one of the four that avoids the class by construction rather than by
being current.

## Two of the readings above are CORRECTED by the kit's own documentation

Recorded here rather than edited out, because the correction is the finding.

**The duplicate inventory claim is BY DESIGN, not a defect.** `gen_map.py:119` states it: "Path globs
are digest-only, never gated; overlap is legal (multi-claim >= 1 owner)." So
`gotcha-classes: bounded-through-a-pipe-is-unbounded.md` being claimed by two dossiers is sanctioned.
Withdrawn as a finding.

**The 3 % file coverage in nicocares is outside the gate's guarantee, and the guarantee is narrower
than its name.** `tools/codebase-map/README.md:62` — "Claims are exact keys, gated BOTH directions;
path globs are digest-only and never gated" — and `test_codebase_map.py` contains no reference to
`globs` at all. The ratchet is honest and it binds inventory KEYS.

What does not survive that correction is the framing around it. `AGENTS.md` §5 calls for "a system
inventory that CANNOT rot into fiction" whose "coverage and freshness checks are merge-bar legs", and
`memory/map/features/codebase-map.md` titles the feature "CI-verified inventory claims". A reader
takes "system inventory" to mean the system. In nicocares it means 28 of 713 source files, with a
green gate, and nothing in the gate's output says which of the two it just verified. §7's own rule
covers this exactly: "A gate's OWN header states what it does NOT check. A structural check reads as
a semantic one to everybody who did not write it."

## Which kits check their own wiring

`bash <kit>/adopt-<kit>.sh --check`, run in every clone that carries the script:

| repo | memory-tree | memory-recall | lexicon | codebase-map |
|---|---|---|---|---|
| gov | exit 2 — no `--check` verb | exit 0, verified | exit 0, verified | exit 2 — no `--check` verb |
| nc | exit 2 — no `--check` verb | exit 0, verified | exit 0, **NOT ADOPTED** | exit 2 — no `--check` verb |
| incms | script absent (forked away) | script absent (forked away) | exit 0, **NOT ADOPTED** | exit 2 — no `--check` verb |
| swydee | exit 2 — no `--check` verb | exit 0, verified | absent | absent |

Two of the four kits have no wiring verb at all: `adopt-memory-tree.sh` and
`adopt-codebase-map.sh` both print `usage: … --scaffold` and exit 2. `tools/gate-legs.json` carries a
`wiring` leg for memory-recall and for lexicon and none for the other two. The two kits without a
wiring check are the two whose adopters were found mis-wired here — nicocares missing
`memory/project/readme-contract.txt`, and incms's `map_extractors` failing at `all_inventories()`.

The `lexicon wiring` leg is declared with `guard: []`, so it runs on every bar, and
`adopt-lexicon.sh --check` exits 0 while printing `NOT ADOPTED`. `tools/run-gates/run-gates.sh`
reports one row per leg and sends a green leg's stdout to `<git-dir>/gate-logs/`, so in an adopter
that leg is a green row whose only content is the sentence saying it graded nothing.

## CORRECTION: there IS an upgrade path, and it is good

The earlier claim "there is no migration verb" is wrong about the engine and right about the corpus.
`python tools/govkit/govkit.py update --target /tmp/kite/nc` is read-only and reports the whole plan.
It resolved nicocares's prefix remapping on its own, dropped seven ambiguous gov directories from the
carry map with a reason each, and graded every file:

| disposition | files |
|---|---|
| current | 87 |
| stale | 34 |
| unattributed (no gov vintage matches; locally edited) | 19 |
| reseed-available | 4 |

Per kit: `memory-tree` DIFFERS (receipt stores 2.50, gov has 2.55), `drift-audit` DIFFERS (1.7 -> 1.8),
`unattended` DIFFERS (1.12 -> 1.15); ten kits level. `scripts/check-memory-hygiene.sh` is one of the
19 unattributed rows, which is consistent with its file marker reading 2.49 against the receipt's
stored 2.50 — the receipt records what gov shipped and the file was edited after.

So the deployer does the hard part: three-way merge through a local edit, rename carrying, withdrawal
orders under `.governance/outbox/`, and read-only by default because "that verb's failure mode is
silent data loss in a repository the operator owns".

What it does not do, and what nothing does, is the CORPUS migration. `update --write` would land
memory-tree 2.55 in nicocares and the next gate run reds on checks 3, 4, 5, 9 and 21 across 612
listed lines, because those checks want `**Serves:**` headers on 612 records, the retirement of ten
`STATUS.md` files, seven recording-file renames, four `memory/project/*.txt` registries reconciled,
and a `RECORD_UNBOUND_PIN` measured against that corpus. The engine upgrade is one command; the
records upgrade is a build nobody has scoped. That asymmetry, not a missing verb, is why both
adopters sit behind.
