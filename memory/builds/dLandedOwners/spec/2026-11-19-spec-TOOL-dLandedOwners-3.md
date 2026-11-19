# TOOL-dLandedOwners-3 — a key read only outside the scanned code takes a declared, reasoned disposition in reader coverage

**Status:** SPECCED · rev-1 · 2026-11-19 · node d · Tier-2 · base 51971579 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md) | research | TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 |

<!-- /gen:spec-records -->

## 1. Goal

Reader coverage gains one declared channel for a catalogue key whose only consumer sits outside the
code its scan reads. A declared key is printed with its reason on every run and is never counted as
read. A declaration the tree no longer supports is a finding. The gov tree declares one such key,
`deviation.approval`, so that key stops reading as a false finding once its owner reads landed.

## 2. Scope (IN)

- **S1** — An authored list, `tools/policy/unscanned-readers.txt`: comment lines open `#`, blank
  lines are skipped, and each other line is one row `<key> <path> <reason>`, split on the first two
  runs of whitespace. Gov's list holds one row, for `deviation.approval`, as §4 "The one row" gives.
  Observed by AC3.
- **S2** — `read_unscanned_readers(kit, names)` in `tools/policy/check_policy.py` reads the list from
  `kit`'s directory. An absent list is no rows and no finding. A line that is not a row, a key no
  catalogue row names, and a key on a second row are each one finding naming the list's line.
  Observed by AC2.
- **S3** — `check_reader_coverage` disposes each graded key it finds no reader for and the list
  declares: it prints the disposition line of §4 "The grading" and records no finding. A graded key
  the list declares is a finding instead when the scan reads it, when its path is not a tracked file,
  or when its path is a file the scan reads. Observed by AC1, AC2 and AC3.
- **S4** — `derive_scanned_files(repo, kit)`, the file selection `scan_reader_keys` makes, extracted
  so the scan and S3 read one set. Observed by AC2 and AC4.
- **S5** — The fixture case `reader-coverage-declared`, one planted repository per case of
  `RD_CASES`, as §4 "The fixture case" gives. Observed by AC1 and AC2.
- **S6** — `tools/policy/kit.toml` withholds the list from installs by naming it in the existing
  `project-owned` rule beside `legacy-homes.txt`. Observed by AC5.
- **S7** — The user's page `help/policy.md`, the kit's `tools/policy/README.md` and the module
  docstring of `tools/policy/check_policy.py` state the list, its row, the disposition line and the
  five findings. Observed by AC6.

## 3. Non-goals (OUT)

- The landed-owner predicate, which `TOOL-dLandedOwners-1` changes, and the module-constant reader
  shape, which `TOOL-dLandedOwners-2` adds. The seven other dDeclaredLoop keys are that shape's.
- Any edit to a dClosedLoop record or instrument, the deviations instrument included.
- Making `deviation.approval` take effect: no code passes the key to a policy reader today, as §4
  "The one row" records. A reader for it is a follow-up the main loop may file as an ask at the close.
- Any disposition other than "outside the scan": a row names one path and one reason, and nothing
  else.
- Checking the row of a key whose owner has not landed beyond its shape: §4 "What it does not check".
- A change to the summary line `reader coverage: graded <n> of <m> catalogue key(s)` or to the arm's
  population text, which other units and fixtures read.
- The policy kit's own self-test arms, the owner's flagged bar, waived for this build by its brief.

### Edges

none

## 4. Design

### What the tree holds today

- `check_reader_coverage` grades each catalogue key whose owner is landed and finds a reader for it
  through `scan_reader_keys` and `check_key_read`; a graded key with no reader is one finding
  (`tools/policy/check_policy.py#check_reader_coverage`).
- `scan_reader_keys` reads tracked code by `git ls-files` over `CODE_PATHSPECS`, skipping the memory
  root, `help/`, its own module and `READER_SKIPPED`, and opens a file only where a `READER_SHAPES`
  row matches its suffix or directory (`tools/policy/check_policy.py#scan_reader_keys`).
- Run on 2026-11-19 at this spec's base with the owner set forced, the probe of AC3 printed
  `graded 32 of 273` and eight findings, `deviation.approval` among them (PINNED).
- `deviation.approval` is a catalogue row owned by dDeclaredLoop, allowed `by-risk`, `owner-all` and
  `author-recorded` (`tools/policy/catalogue.toml@9d43738cca727d03cb43c81c40e059ef74c8cd50:1032`).
- No tracked `.py`, `.sh` or `.js` file spells `deviation.approval`, by `git grep` on 2026-11-19
  (PINNED). The dClosedLoop deviations instrument applies the chain's value `author-recorded` in its
  approver check (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#check_approver`),
  the value decision `PLAY-dClosedLoop-4` fixed (`memory/DECISIONS.md@2d3629f32ac1a63220226aa285090ec0cfa76700:236`).
  The instrument reads no policy key. The brief's question called it the key's reader; the code shows
  a consumer of the chain's fixed value, and the row's reason says so.
- The kit already withholds a gov-only list from installs: `legacy-homes.txt`, named in a
  `project-owned` rule (`tools/policy/kit.toml@374659e4a413097df883f0f3da76bbc19c5e462e:33`), whose
  rows name gov's own tree.

### The list

`tools/policy/unscanned-readers.txt`, authored and never generated. Its header, verbatim:

```
# unscanned-readers.txt - AUTHORED. One row per catalogue key whose consumer sits outside the code
# reader coverage scans: `<key> <tracked path> <reason>`, the reason the rest of the line. Read by
# check_policy.py's reader coverage, which prints each row of a landed owner's key and never counts
# it as read. A row the scan now reads, a path not tracked, a path the scan reads, a key no catalogue
# row names and a key on two rows are each a finding. Withheld from installs by this kit's kit.toml.
```

A path cannot hold whitespace, since whitespace ends the field. A reason is at least one character.

### The one row

```
deviation.approval memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py the chain applies the approval route in this instrument at the value PLAY-dClosedLoop-4 fixed, author-recorded; no tracked code passes the key to a policy reader
```

### The grading

`check_reader_coverage(repo, landed=None, kit=KIT)` keeps its signature and its return,
`(the count graded, the findings)`. It calls `read_unscanned_readers(kit, names)` on every run, and
`derive_scanned_files(repo, kit)` and one `git ls-files -z -- <the declared paths>` only when a graded
key is declared. For each graded key, in catalogue order:

| Read by the scan | Declared | Path | Outcome |
|---|---|---|---|
| yes | no | any | read, as today |
| no | no | any | the finding of today, `has no reader` |
| yes | yes | any | finding: the row is stale |
| no | yes | not a tracked file | finding: the declared path is not tracked |
| no | yes | a file the scan reads | finding: the scan reads that file |
| no | yes | tracked, outside the scan | the disposition line, no finding |

A tracked file is exact membership of the `ls-files` output, so a directory path reads as untracked.
The disposition line is printed after the summary line, one per disposed key:

```
reader coverage: <key> (owner <owner>) declared outside the scan at <path>: <reason>
```

Every finding opens `reader coverage: `, as today's does, so `arm_reader_coverage` splits it on its
first `: ` unchanged. The texts:

```
reader coverage: unscanned-readers.txt:<n> is not a row: a row is <key> <path> <reason>
reader coverage: unscanned-readers.txt:<n> names <key>, which no catalogue row names
reader coverage: unscanned-readers.txt:<n> declares <key> a second time, first at line <m>
reader coverage: <key> (owner <o>, landed at <rev8>) is declared outside the scan, and the scan reads it: drop its row
reader coverage: <key> (owner <o>, landed at <rev8>) is declared read at <path>, which is not a tracked file
reader coverage: <key> (owner <o>, landed at <rev8>) is declared read at <path>, which the scan reads: give the scan its shape instead
```

The first three are the list's shape and are found whether or not any key is graded. With nothing
graded and a shape finding, `run_arm` adds its zero-population finding as well, so a malformed list
reds before any owner lands. The first row of a duplicated key is the one that disposes it.

### The scanned files

`derive_scanned_files(repo, kit)` returns the tracked paths `scan_reader_keys` opens: the `ls-files`
walk, the skips and the suffix or directory test of the scan as `TOOL-dLandedOwners-2` leaves it.
`scan_reader_keys` iterates that list in place of its own walk. Nothing about which file is read
changes.

### The fixture case

`reader-coverage-declared` runs `run_reader_declared(name)`, entered in the fixture table beside
`reader-coverage-relocated`. Each case builds its repository with `build_reader_coverage_repo(t,
case, spec=...)`, writes the case's list text to `UNSCANNED_LIST` in the returned kit copy, and runs
`check_reader_coverage` capturing stdout. The planted instrument is `RD_INSTRUMENT`,
`memory/builds/bPlanted/build/instrument.py`, holding `APPROVAL = "author-recorded"`. `RC_KEY`,
`RC_OWNER` and `RC_CALL` are the reader-coverage cases' own.

| Case | Landed token | Planted files | List rows | Findings, each holding | Graded |
|---|---|---|---|---|---|
| `declared-outside` | `CLOSED` | the instrument | a `#` line, a blank line, `RC_KEY` at the instrument | none; stdout holds `declared outside the scan at memory/builds/bPlanted/build/instrument.py: ` and the reason | 1 |
| `declared-unlanded` | `OPEN` | none | `RC_KEY` at the instrument | none; stdout holds the announce line | 0 |
| `declared-and-read` | `CLOSED` | the instrument, `consumer.py` holding `RC_CALL` | `RC_KEY` at the instrument | `and the scan reads it` | 1 |
| `declared-untracked` | `CLOSED` | none | `RC_KEY` at the instrument | `which is not a tracked file` | 1 |
| `declared-scanned` | `CLOSED` | `consumer.py` holding `value = 1` | `RC_KEY` at `consumer.py` | `which the scan reads` | 1 |
| `declared-malformed` | `CLOSED` | the instrument | `RC_KEY` and the instrument path, no reason | `is not a row`, `has no reader` | 1 |
| `declared-unknown` | `CLOSED` | the instrument, `consumer.py` holding `RC_CALL` | `fixture.absent` at the instrument | `which no catalogue row names` | 1 |
| `declared-twice` | `CLOSED` | the instrument | `RC_KEY` at the instrument, twice | `a second time, first at line` | 1 |

A case passes when its finding count equals its column's count of texts, every text is found in
one finding, its graded count matches, and its stdout text is present. It prints
`case <name>: red|green`, as `run_reader_coverage` does.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `tools/policy/unscanned-readers.txt` | file | the list of §4 "The list" |
| `UNSCANNED_LIST` | constant | `"unscanned-readers.txt"` |
| `read_unscanned_readers(kit, names)` | function | `({key: (line, path, reason)}, [finding])` |
| `derive_scanned_files(repo, kit)` | function | `[path]`, the tracked files the scan opens |
| `RD_INSTRUMENT` | constant | `"memory/builds/bPlanted/build/instrument.py"` |
| `RD_CASES` | constant | the eight cases of §4 "The fixture case" |
| `run_reader_declared(name)` | function | the fixture runner; `(assertions, wrong)` |
| `reader-coverage-declared` | fixture case | its row in the fixture table |

### What it does not check

- That the declared file consumes the key or its value: the row is the author's claim, printed on
  every run so a reader sees it.
- A row whose key's owner has not landed, beyond the list's shape: its path and staleness are graded
  from the landing on.
- That the list is withheld from installs: S6 is observed by AC5 once, and nothing re-checks it.
- A path holding whitespace, which the row cannot spell.

### Files touched (estimate)

`tools/policy/check_policy.py`
`tools/policy/unscanned-readers.txt`
`tools/policy/kit.toml`
`tools/policy/README.md`
`help/policy.md`
`memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-3-ledger.md`

### Alternatives rejected

- Widening the scan into the memory root: the deviations instrument spells no key, so no scan sees
  it, and every record's code would then count as a reader.
- A catalogue field naming the reader: the catalogue ships to every adopter as engine, so gov's paths
  would ship with it, and its schema, `OPTIONAL` in `tools/policy/policy.py`, is a shared contract.
- A constant in `check_policy.py`: it ships too, and an adopter could not declare its own rows.
- The consumer registry `TOOL-dGroundRules-8` rejected, a list of reads beside the code
  (`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md@3266bce7794fd19aa478b878bbd19215b803c93f:152`).
  It counted a declared read as read; this list never does, prints each row, and reds a row the tree
  no longer supports.

## 5. Production-readiness checklist

- security — Read-only: one file read, one `git ls-files` call, and nothing executed from the list.
- perf / scale — One `git ls-files` call and one list read per run, beside a scan that already walks
  every tracked code file.
- error / empty / loading states — An absent list is no rows; a malformed row, an unknown key and a
  duplicate are named findings; the five-row grading table covers every graded key.
- observability — One printed disposition line per disposed key, on every run.
- risks — A row hides a key with no effective reader, which `deviation.approval` is; the printed
  reason is what keeps that visible, and §3 names the follow-up.
- testing — The eight cases of `reader-coverage-declared`, and the existing `reader-coverage` cases
  held unchanged.
- migration — N/A — a new authored file and a new optional read; an absent list reproduces today.
- user docs — `help/policy.md`, section "Every key whose build has landed has a reader", gains the
  third way to clear a finding, the row, the disposition line and the findings.

## 6. Acceptance criteria

Commands run from the worktree root after `. tools/lib/resolve-python.sh && PY=$(resolve_python)`.

- **AC1** — When `"$PY" -B tools/policy/check_policy.py --fixture reader-coverage-declared` runs, it
  prints `case declared-outside: green` and `case declared-unlanded: green` with no `WRONG`, and the
  first's line carries the disposition text of §4 "The fixture case".
  Red when: `read_unscanned_readers` returns no rows, where `declared-outside` finds
  `fixture.planted (owner bPlanted, landed at` and `has no reader` and prints `WRONG`.
- **AC2** — When the same command runs, it prints `case <name>: red` for each of `declared-and-read`,
  `declared-untracked`, `declared-scanned`, `declared-malformed`, `declared-unknown` and
  `declared-twice`, no `WRONG`, and closes `policy-fixture: <n> assertion(s) executed · 0 wrong`,
  exit 0.
  Red when: the scanned-path test is dropped from S3, where `declared-scanned` finds nothing and
  prints `WRONG`.
- **AC3** — When `"$PY" -B -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; n, f = c.check_reader_coverage('.', landed={'dDeclaredLoop'}); print([x for x in f if 'deviation.approval' in x])"`
  runs, its stdout holds one line opening
  `reader coverage: deviation.approval (owner dDeclaredLoop) declared outside the scan at`, then
  naming `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` and the
  reason of §4 "The one row", and its last line is `[]`.
  Red when: the row is deleted from S1's list, where the last line names
  `deviation.approval (owner dDeclaredLoop, landed at` and `has no reader`.
- **AC4** — When `"$PY" -B tools/policy/check_policy.py --fixture reader-coverage` runs, every one of
  its eleven cases prints the verdict it printed at this spec's base, with no `WRONG`.
  Red when: `derive_scanned_files` stops skipping `READER_SKIPPED`, where `not-a-reader` reads its
  planted test script as a reader and prints `WRONG`.
  figure: eleven is PINNED, the count of `RC_CASES` at this spec's base.
- **AC5** — When `"$PY" -B -c "import sys, tomllib; r = tomllib.load(open(sys.argv[1], 'rb'))['files']; print([x['include'] for x in r if x['role'] == 'project-owned'])" tools/policy/kit.toml`
  runs, it prints one list holding both `legacy-homes.txt` and `unscanned-readers.txt`.
  Red when: the rule is left as it stands at this spec's base, where the list holds
  `legacy-homes.txt` alone.
- **AC6** — When `grep -c "unscanned-readers.txt" help/policy.md tools/policy/README.md` runs, each
  file counts at least one, and `grep -F "declared outside the scan at" help/policy.md` prints the
  disposition line's form.
  Red when: the page is left as at this spec's base, where `help/policy.md` counts 0.

## 7. Gates

The close runs the merge bar once. The legs below are those the files touched keep green; the
`policy fixtures` leg runs the new case, and the `policy check` leg grades the gov tree's own list.
`scratch-guard self-test` and `routed-commits selftest` guard the whole kit directory, and the two
recall legs guard the build's records, the unit's ledger among them.

`policy fixtures` · `policy check` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py --fixture reader-coverage-declared · covers AC1 AC2 · a list with no rows read, or the scanned-path test dropped, stages its failing case · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

## 10. Reuse audit

The seams extended: `tools/policy/check_policy.py#check_reader_coverage`, whose grading gains the
declared outcome; `tools/policy/check_policy.py#scan_reader_keys`, whose file walk becomes
`derive_scanned_files`; the fixture's `tools/policy/check_policy.py#build_reader_coverage_repo` and
the case shape of `tools/policy/check_policy.py#run_reader_coverage`; and the withheld-list rule of
`tools/policy/kit.toml`, with its reason, from `TOOL-dGroundRules-17`.
`python tools/codebase-map/reuse_lookup.py "a declared list of exempt keys with a reason checked for staleness"`
ranked name-stem helpers, among them `tools/codebase-map/map_lib.py#load_affordance_exempt`, a
shrink-only grace list of names with no reason and no path, so no existing seam fits the row itself.
The recall probe returned `TOOL-dGroundRules-8`, whose §4 rejected a consumer registry, read and
answered in §4 "Alternatives rejected", and `TOOL-dTrackedAtlas-5`, the ask this build serves.

Recall terms used: `python tools/memory-recall/query.py "how does reader coverage dispose a policy key whose reader sits outside the scanned code" --terms "reader coverage policy key catalogue owner landed scan declared disposition exemption stale withheld list"`
