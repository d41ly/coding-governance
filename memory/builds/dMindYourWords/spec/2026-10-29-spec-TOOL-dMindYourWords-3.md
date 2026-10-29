# TOOL-dMindYourWords-3 — gov's own contract-forced names in a table, with a stale arm

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 9 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0264@a1b36116 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Some names in gov's own code cannot change because another of gov's files reads them by name.
`tools/hooks/agent-cap.js` matches `chunk(` in a Workflow script, and `gen_map.py` calls
`all_symbols`, `inventory_ids` and `all_inventories` on the adopter-authored `map_extractors`
module. Today `.lexicon.conf:173-178` absorbs them into the pin by hand. This unit declares them in a
table the instruction write path owns (LX-3). Each row names the reader, the name and the match rule
the reader applies. The code carries at most a `gov:note` pointer, which a check resolves. A stale arm
runs each row's own match rule over its reader's source, and reds the row once the reader stops
matching.

## 2. Scope (IN)

- **S1** — The table, a `CONTRACTS:` block in `.lexicon.conf`, added through the conf's one door (I8):
  one `BLOCK_KEYS` row (`tools/lexicon/lexicon_conf.py:37`) plus its row parser `_parse_contracts`
  in `_BLOCK_PARSERS` (`:401-402`), and one `RECORD_TAGS` entry mapping `CONTRACTS` to
  `unit.lexicon.contracts` (TOOL-dMindYourWords-11 §4 "The tags"), so that unit's `--check-record`
  refuses at commit a table change no record carries. A row is `<tag> <name> <defined> <reader> <match>` (§4 "Data
  model"). The parser refuses a malformed tag, a name that is not an identifier, a missing field and a
  `match` that does not compile, each a `ConfError` naming the file and line. Observed by AC5, AC8.
- **S2** — The contract source. TOOL-dMindYourWords-2's forced check (its S1) gains one source: a
  definition whose name equals a row's `name`, in a file whose repo path matches the row's `defined`
  glob under `fnmatchcase`, is forced with `Offender.source` `contract:<tag>` (I2). It applies under
  every `lexicon.forced` value (TOOL-dMindYourWords-2 §8 F3), and to every extension, JavaScript
  included, because no base is resolved. Observed by AC3, AC6.
- **S3** — The stale arm, `check_contract_rows(rows, root, scanned)`, run in `measure_pass` on every
  run. A row is stale, and a problem line `STALE CONTRACT <tag>: <reason>` reds the run, when its
  reader is not a tracked file, when `re.search(match, <reader source>)` finds nothing, or when no
  definition of `name` sits in a file `defined` matches. Each run prints `lexicon: contracts — <n>
  row(s), <k> stale`, a zero included. Observed by AC1, AC2, AC6.
- **S4** — The pointer arm, `check_contract_pointers(rows, root)`. It reads the `gov:note` rows of
  TOOL-dLinkedLibrary-4's `annotations.py index` (its S9) by subprocess, never by import. The kit is
  found at `<kit>/../memory-tree/annotations.py`, the sibling probe `read_policy_value` uses for
  `policy.py` (TOOL-dMindYourWords-1 S5). Every note whose tag opens
  `lexicon.contract.` must name a row's `tag`, in a file that row's `defined` matches. A note that does
  not is a problem line `DANGLING CONTRACT POINTER <path>:<line> <tag>`. A note never exempts on its
  own: a definition carrying one with no row is graded as before. With no memory-tree kit found, the run
  prints `lexicon: contract pointers not graded — <why>` and checks nothing. Observed by AC4, AC7.
- **S5** — The write-path arm at the bar, `check_contract_record(rows, root)`, the backstop for a
  commit that bypassed the hook. It reads the latest record through `read_vocabulary_record(root,
  ("unit.lexicon.contracts",))` (I11, TOOL-dMindYourWords-11 S1), and parses the `CONTRACTS:` rows of
  `.lexicon.conf` at the commit that added that record, with the same parser. The arm reds `CONTRACTS
  changed with no change record` when they differ from the rows now, or when rows exist and no record
  does. Observed by AC5.
- **S6** — gov's rows, four, recorded through the route TOOL-dMindYourWords-11 settles for a
  `.lexicon.conf` vocabulary change, its record tagged `unit.lexicon.contracts` (I11): `chunk`,
  `all_symbols`, `inventory_ids` and `all_inventories` (§4 "gov's rows"). They force 14 definitions.
  Observed by AC6.
- **S7** — The pointers: one `gov:note` line above each of the three definitions in
  `tools/codebase-map/map_extractors.py`, gov's project-owned copy, so S4 grades a live population.
  Observed by AC6.
- **S8** — The docs. A `### Contract-forced names` section of `tools/lexicon/README.md` gives the row
  grammar, the three arms and why `boundedParallel` has no row. `KIT_LEXICON_VERSION`
  (`tools/lexicon/lexicon.py:90`) moves. Observed by AC9.

## 3. Non-goals (OUT)

- A row for `boundedParallel` (§8 F2). No reader keys on it. Its 8 definitions stay debt, and
  whether to rename them stays the owner's question, ask TOOL-aWeldedTribunal-12.
- Pointers in a file gov ships: the four workflow templates, their renders, and
  `tools/codebase-map/map_extractors.template.py`. An adopter's tree would hold the note with no row
  in its own `.lexicon.conf`, and S4 would red there.
- An adopter's own contract rows. The block is the repository's own, so an adopter declares its own
  rows through the same route, and gets no gov rows.
- The routing of a `.lexicon.conf` change through the instruction write path, the record's kind, its
  reader and the commit-time `--check-record`: TOOL-dMindYourWords-11's. This unit adds one
  `RECORD_TAGS` entry, calls `read_vocabulary_record`, and adds no second record reader.
- The forced check, the walk and the tally: TOOL-dMindYourWords-2's. This unit adds one source.
- The repeated-header refusal: TOOL-dMindYourWords-14's, which lands before this block (I8).
- The `gov:note` grammar, its parser and the annotation index: TOOL-dLinkedLibrary-4's.
- The pin's fall at landing is entered in TOOL-dMindYourWords-1's form, never as a `PINS:` row.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, the class a contract-forced definition takes, so it leaves the debt count
- **consumes-from** `TOOL-dMindYourWords-14` — `load_conf` with the repeated-header refusal, the door the `CONTRACTS:` block is added through
- **consumes-from** `TOOL-dMindYourWords-11` — `read_vocabulary_record`, the latest `contracts` record S5 compares the rows against, and `RECORD_TAGS`, which S1 extends so `--check-record` covers the block; without them no change to the table can be tied to the write path
- **consumes-from** `TOOL-dMindYourWords-2` — `Offender.source`, whose `contract:<row tag>` value S2 sets inside that unit's forced check
- **consumes-from** external — TOOL-dLinkedLibrary-4's `annotations.py index` verb, DEFERRED at base, in a parent build that lands before this build run
- **hands-off** external — `boundedParallel`'s 8 definitions, left as debt for the owner's ruling on ask TOOL-aWeldedTribunal-12
- **consumes-from** `TOOL-dMindYourWords-24` — the inline `resolve_kit_dir` in `tools/lexicon/lexicon.py`, through which S4 finds `annotations.py` as `resolve_kit_dir("memory-tree", "annotations.py", KIT_DIR)` in place of the `<kit>/../memory-tree/` probe (review id 23)
- **hands-off** `TOOL-dMindYourWords-29` — its pin falls, `check_contract_record` and `check_contract_pointers`, which the minors batch repairs (review ids 6, 53, 54)

## 4. Design

### Evidence

Read at `ba8b3c8c4`. No product file differs from base `ccd1292e`.

- `tools/hooks/agent-cap.js` matches `chunk` by name, in two regular expressions:
  `/\bchunk\s*\(\s*[^,]+,\s*Math\.ceil…/` at :591 and `/\b(chunk|splitInto)\s*\(/` at :887. A
  Workflow script whose bounded split is not spelled `chunk(` fails `boundedBranch` (:587) and is
  denied.
- `boundedParallel` is matched by no expression in `agent-cap.js`. It appears there only in comments
  (:1088, :1106, :1293, :1307) and in the remedy text the hook prints (:1950). The hook judges a
  fan-out by its structure, the enclosing openers of an `agent(` call (:1080-1112), so a wrapper of
  any name passes. The records that call it read by name (research-lexicon-population:68, lexicon
  review :261, `.lexicon.conf:176-177`) cite :1286 and :1413, which are a parenthesis scanner and a
  comment (scout A, disagreement 1). What names it is prose: `memory/guides/REVIEW-PROTOCOL.md:136`
  and the hook's remedy.
- `gen_map.py` calls `ext.inventory_ids()` (:38), `ext.all_inventories()` (:138, :162, :233) and
  `getattr(ext, "all_symbols", list)()` (:149). `tools/codebase-map/map_extractors.py` is
  `project-owned` and `map_extractors.template.py` is the seed an adopter's copy is made from
  (`tools/codebase-map/kit.toml:35-36`, :61-63). So the engine fixes the three names for every author
  of the module.
- The definitions, off `python tools/lexicon/lexicon.py --offenders` at `ba8b3c8c4` (PINNED): `chunk`
  and `boundedParallel` in the `.js` and `.template.js` copies of `drift-audit-code`,
  `drift-audit-state`, `tier2-review` and `unattended-build` under `tools/workflows/`, 8 each, and the
  three map names in `map_extractors.py` and `.template.py`, 2 each. That is 22 offender keys, 14 of them with a reader keying on the name.
- `load_conf` admits only `BLOCK_KEYS` headers, and a key with no `_BLOCK_PARSERS` entry is a
  `ConfError` (`lexicon_conf.py:37`, :393-411). `_parse_rows` splits `<row-key> <rest>` on the first
  run of whitespace and refuses a duplicate key (:187-200).
- TOOL-dLinkedLibrary-4 specs the note grammar `gov:note <tag>[,<tag>…] — <definition> → <target>`
  (its S2) and the `index` verb, which prints one JSON object per row with `path`, `line`, `word`,
  `tags`, `definition`, `target`, `refs` and `block_end` (its S3, S9). It is DEFERRED at base.
- `lexicon.py` carries no sibling-kit resolver. TOOL-dMindYourWords-1 S5 finds `policy.py` by the
  probe `<kit>/../policy/policy.py`, and S4 here probes the same way, so the kit has one way to find a
  sibling.

### Data model

```text
CONTRACTS:
    lexicon.contract.chunk            chunk            tools/workflows/*.js                     tools/hooks/agent-cap.js       \\bchunk\\s\*\\\(
    lexicon.contract.all-symbols      all_symbols      tools/codebase-map/map_extractors*.py    tools/codebase-map/gen_map.py  "all_symbols"
    lexicon.contract.inventory-ids    inventory_ids    tools/codebase-map/map_extractors*.py    tools/codebase-map/gen_map.py  ext\.inventory_ids\(
    lexicon.contract.all-inventories  all_inventories  tools/codebase-map/map_extractors*.py    tools/codebase-map/gen_map.py  ext\.all_inventories\(
```

- `tag`: `lexicon.contract.<seg>`, `<seg>` matching `[a-z0-9][a-z0-9-]*`. That is TAG_RE's segment
  shape (PLAY-dOrderedCharter-19 S1), checked by a local pattern because the kit imports no playbook
  module. The tag is the row key, so `_parse_rows` refuses a repeat.
- `name`: `[A-Za-z_$][A-Za-z0-9_$]*`.
- `defined`: one `fnmatchcase` glob over repo-relative paths. `*` crosses `/`, which is
  `fnmatchcase`'s rule.
- `reader`: one repo-relative path.
- `match`: the rest of the line, a Python regular expression run over the reader's source text. For
  `chunk` it matches the expression's own text `\bchunk\s*\(` in `agent-cap.js`, so the row goes stale
  when the hook stops spelling it.

A conf row is raw text with no escape processing, so the `match` field is the pattern exactly as
written.

### The pointer

```python
# gov:note lexicon.contract.all-symbols — gen_map.py calls this by name → .lexicon.conf
def all_symbols() -> list[dict[str, str]]:
```

The definition is at most 80 characters, and the target is a repo path (TOOL-dLinkedLibrary-4 S2).

### Where each arm runs

S3, S4 and S5 append to `measure_pass`'s `problems` list, so the default run and `--check` both red
on them, and neither mode can skip one (`lexicon.py:2796-2808`). S2 is one more branch in
TOOL-dMindYourWords-2's walk, tried before the `host` rows. S5's old revision is written to a
`tempfile.NamedTemporaryFile` and read through `load_conf`, so one grammar parses both revisions.

### gov's rows

| Row tag | Definitions forced | Reader and its rule |
|---|---|---|
| `lexicon.contract.chunk` | 8, `tools/workflows/*.js` | `agent-cap.js:591`, `:887` |
| `lexicon.contract.all-symbols` | 2 | `gen_map.py:149` |
| `lexicon.contract.inventory-ids` | 2 | `gen_map.py:38` |
| `lexicon.contract.all-inventories` | 2 | `gen_map.py:138` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `CONTRACTS` | conf block key | none |
| `_parse_contracts` | function, `lexicon_conf.py` | `py.function`, asked: OK |
| `check_contract_rows`, `check_contract_pointers`, `check_contract_record` | functions, `lexicon.py` | `py.function`, asked: OK |
| `lexicon.contract.<seg>` | row tags | none |
| `STALE CONTRACT`, `DANGLING CONTRACT POINTER` | problem lines | none |

### Rollout

The four rows land with their `unit.lexicon.contracts` record in one commit. In that commit
TOOL-dMindYourWords-1's pin falls by the 14 definitions S2 forces. The figure is derived by the
landing run, never typed here.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1
- `tools/lexicon/lexicon.py`: S2 to S5, `KIT_LEXICON_VERSION`
- `.lexicon.conf`: S6's block, and the pin's fall in TOOL-dMindYourWords-1's form
- `tools/codebase-map/map_extractors.py`: S7's three pointer lines
- `tools/lexicon/selftest.py`: the arms of §7
- `tools/lexicon/README.md`: S8

### Alternatives rejected

- **A registered row kind in the overlay, written by `instructions_edit.py`** (scout A, disagreement 7,
  option a). The test: can a copy-installed kit read a registered kind's rows? The one reader,
  `read_overlay_rows` (PLAY-dOrderedCharter-35 S1), is a function in another kit with no specced CLI.
  S1 of that spec forbids a second parser of the overlay, and the lexicon may import no sibling kit
  (`lexicon.py:2359`). So option (a) needs a new public surface in another build (§8 F1).
- **A stale arm that only checks the reader file exists.** It passes on the day agent-cap.js changes
  its rule, which is the defect the clause names.
- **A row for `boundedParallel` whose reader is `REVIEW-PROTOCOL.md`.** The test is the design's own
  row definition, "the match rule the reader applies" (lexicon review :260). A page applies no rule,
  so the row would be a reasonless exemption with a citation attached (§8 F2).
- **Pointers in all 14 definitions.** Ten of them ship, so the note would red every adopter (Non-goals).

## 5. Production-readiness checklist

- security — S4 runs a sibling kit's CLI with fixed arguments, at a path derived from the kit's own
  directory and never from the repository's content. A row's `match` is compiled once and run over one tracked file.
- perf / scale — four regex searches, one annotation index read and one `git show` per run.
- error / empty / loading states — no block gives `contracts — 0 row(s)`, and S5 has nothing to
  compare. No memory-tree kit gives S4's `not graded` line. A malformed row is a `ConfError`.
- observability — the contracts line on every run, and each stale row or dangling pointer by name.
- risks — a broad `defined` glob forces a same-named free definition in another matched file. gov's
  globs are confined to the files the readers read.
- testing — the arms of §7, each a fixture repository with a planted row, reader, pointer or record.
- migration — the pin's fall at landing (Rollout). `.lexicon.conf:173-178`'s hand-absorption notes
  stay as history.
- user docs — `tools/lexicon/README.md` `### Contract-forced names`. `help/` holds no lexicon page.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs in a fixture repository whose `CONTRACTS:` row
  names reader `hook.js` with match `\bchunk\s*\(`, and `hook.js` holds that text, the run prints
  `contracts — 1 row(s), 0 stale`. After `hook.js` is edited to match `splitInto(` only, it exits
  non-zero printing `STALE CONTRACT` and the row's tag.
  Red when: the reader stops matching and the row stays green, which is the clause's planted case.
- **AC2** — When the same fixture's reader still matches but no file under the row's `defined` glob
  defines `chunk`, `lexicon.py` prints `STALE CONTRACT` naming the missing definition. When the reader
  path is deleted, it prints `STALE CONTRACT` naming the reader.
  Red when: a row with no reader or nothing to force stays green.
- **AC3** — When `lexicon.py` runs over a fixture with `chunk` defined in `wf-a.js`, which the row's
  `defined` glob `wf-*.js` matches, and in `lib-b.js`, which it does not, `--offenders` holds
  `lib-b.js` and not `wf-a.js`, and the tally reads `contract=1`.
  Red when: the same name outside the glob is forced, or the one inside is debt.
- **AC4** — When a fixture file carries `# gov:note lexicon.contract.nosuch — x → .lexicon.conf`,
  `lexicon.py` prints `DANGLING CONTRACT POINTER` with its path and line. A note naming a real row in
  a file outside that row's glob does the same. A definition carrying a valid-shaped note and no row
  stays in `--offenders`.
  Red when: a pointer resolves to no row and the run is green, or a note exempts a name.
  fixture: TOOL-dLinkedLibrary-4's `annotations.py` installed beside the lexicon in the fixture.
- **AC5** — When a fixture commits a `CONTRACTS:` row with a `contracts` record, `lexicon.py` is green.
  After a later commit edits the row's `match` with no new record, it prints `CONTRACTS changed with
  no change record`. With a record committed beside the edit, it is green again. A fixture holding rows
  and no record reds the same way. With a row edit staged and no record staged, `python
  tools/lexicon/lexicon.py --check-record` exits 1 naming `unit.lexicon.contracts`.
  Red when: a table change with no record passes, at the bar or at commit.
  fixture: TOOL-dMindYourWords-11's record shape, committed in the fixture's history.
- **AC6** — When `python tools/lexicon/lexicon.py` runs on this tree after the unit lands, it prints
  `contracts — 4 row(s), 0 stale`, its tally's `contract=` reads 14, the 8 `boundedParallel` keys stay
  in `--offenders`, and S4 grades the 3 pointers in `tools/codebase-map/map_extractors.py` with no
  dangling one.
  Red when: a gov row is stale at landing, or a contract name stays debt.
  figure: 14 and 3 are PINNED at `ba8b3c8c4`.
- **AC7** — When `lexicon.py` runs in a fixture holding no memory-tree kit, it prints `contract
  pointers not graded` and its exit code equals the same run with the line's arm removed.
  Red when: the absent kit reds the run, or passes silently.
- **AC8** — When `load_conf` reads fixture confs whose `CONTRACTS:` rows carry four fields, the tag
  `Lexicon.Contract.X`, and the match `chunk(`, each raises `ConfError` naming the file and line.
  Red when: a malformed row is accepted.
- **AC9** — When `grep -n "Contract-forced names" tools/lexicon/README.md` runs, it prints the section
  heading, and the section names `boundedParallel` and why it has no row.
  Red when: the section is missing.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `lexicon naming predicates` · `straggler-guard arms` · `govkit acceptance matrix` · `lexicon wiring` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 · one fixture repository per case, its failing case a `CONTRACTS:` row whose reader stopped matching that stays green · none

## 8. Open questions

- **F1 — Where does the table live?** Options: (a) a registered row kind `lexicon-contract` in the
  overlay `.governance/instructions.toml`, written by `instructions_edit.py` and read through
  `read_overlay_rows`; (b) a `CONTRACTS:` block in `.lexicon.conf`, a convention of I11, changed
  through the route TOOL-dMindYourWords-11 settles, with S5 refusing a change no record carries. (a)
  needs a CLI that prints a kind's composed rows, which no spec of dOrderedCharter states. S1 of
  PLAY-dOrderedCharter-35 forbids a second parser of the overlay, and this kit imports no sibling. So
  (a) needs a new public surface in another build, outside the `may:` grant (veto 2). RESOLVED (agent,
  2026-10-29, delegated): (b), rung 3, the one option that survives the vetoes. It satisfies the
  clause's "a table the instruction write path owns" through that path's record, and I11 already
  lists `contracts` among the lexicon's conventions. widens: none · relaxes: none
- **F2 — Does `boundedParallel` get a row?** Options: (a) no row, 8 definitions stay debt; (b) a row
  whose reader is `REVIEW-PROTOCOL.md`'s template and whose rule matches its fan-out sentence. Source
  shows no code reader keys on the name (§4 Evidence). RESOLVED (agent, 2026-10-29, delegated): (a),
  rung 1: the lexicon review defines a row as "the reader, the name and the match rule the reader
  applies" (:260-261), and a page applies none. The records' claim that `agent-cap.js` reads it is the
  stale citation scout A found. widens: none · relaxes: none
- **F3 — Where do the pointers go?** Options: (a) the three definitions in gov's project-owned
  `map_extractors.py` only; (b) all 14 definitions; (c) none. (b) reds every adopter (Non-goals), and
  (c) leaves S4 grading an empty population, which a gate must never read as coverage. RESOLVED
  (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 3, the lexicon review's `[forced]` item 2
  (:259-263), `[integration]` (:442-443) and `[vocabulary]` (:398), debt-fold rows :628 and :665,
  scout A row 3 and disagreements 1 and 7, and the spec brief's I2, I8 and I11.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-24, TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `load_conf`'s block door, `BLOCK_KEYS` and `_BLOCK_PARSERS`
(`tools/lexicon/lexicon_conf.py:37`, `:401-402`) with `_parse_rows` (`:187`), and `measure_pass`'s
`problems` list (`tools/lexicon/lexicon.py:2796`). The unit reads TOOL-dMindYourWords-2's forced
check, TOOL-dMindYourWords-11's `read_vocabulary_record` and `RECORD_TAGS`, TOOL-dLinkedLibrary-4's
`annotations.py index`, and TOOL-dMindYourWords-1's sibling-kit probe. `python
tools/codebase-map/reuse_lookup.py "run a declared regular expression over a reader file to detect a
stale declaration row"` ranked name-stem hits only: `rows`, `row`, `read`, `run_git` and `read_conf`.
No check in `tools/` runs a declared pattern over another file's source, so the stale arm is new.
That matches scout A's row 3. The source disagrees with the records on `boundedParallel` (§4 Evidence,
§8 F2).

Recall terms used: `python tools/memory-recall/query.py "where are gov's own contract-forced names declared and what keeps them from going stale" --terms "contract-forced boundedParallel chunk agent-cap reader match rule stale arm table pointer gov:note"`
