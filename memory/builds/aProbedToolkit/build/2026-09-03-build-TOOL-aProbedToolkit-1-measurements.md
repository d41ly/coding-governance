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
