# Research: the lexicon kit, the offender population and the pin's history

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 28's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`.

---

## Researcher B: the offender population and the pin's history (PLAY-dClosedLoop-1)

Everything below was measured read-only at HEAD `f02d8e228` on 2026-10-15. Probe scripts went to the scratchpad; nothing in the tree was changed. The three classifier scripts in that scratchpad (`dump.py`, `pyctx.py`, `classify.py`) are throwaway probes. They call the kit's own `measure_pass` and `ast`.

### 1. Inventory

| Item | Where | Fact |
|---|---|---|
| P1 grader | `tools/lexicon/lexicon.py:2941-2965` | Each extracted function's `leading_verb` that is not in VERBS becomes an offender. It is marked `debt` if `canon.build_form_index` holds the token, otherwise `unruled`. Nothing checks enclosing class, base class, decorator or host. |
| Leading token | `tools/lexicon/subtokens.py:39-48` | Underscores are stripped, so `__str__` grades on `str` and `__exit__` on `exit`. |
| Python extractor | `lexicon.py:425-456` | `ast.walk` collects methods, nested functions and properties alike. |
| Canon | `tools/lexicon/canon.py:55-81` | 20 clusters. `has`/`is`→check, `handle`/`do`→run, `emit`/`log`→print, `configure`/`setup`→init. These are exactly the stems that host frameworks fix. |
| Waivers | `tools/lexicon/lexicon-verb-waivers.txt`, `lexicon-suffix-waivers.txt` | Both files are header-only, and no version in history ever held a row (probe below). |
| Records already naming the forced class | `.lexicon.conf:173-181`, `:207-215` | `boundedParallel`/`chunk` "cannot be renamed: agent-cap.js recognises both BY NAME". A text-keyed waiver was refused because it "would waive every copy corpus-wide". |
| HEAD is red | `--measure` reads 1088 against `VERB_OFFENDER_PIN="1087"` (`.lexicon.conf:268`) | The extra offender is `tools/unattended/gate-guard.js:689 clean`. `8ddc0a482` (aOrientedCast-22, 2026-10-13) added it without moving the pin. |

### 2. Sequence

1. List every offender with the kit's own verbs (`--offenders`, `--list`, `--measure`). Pull line numbers and the debt/unruled split from `measure_pass`.
2. Add Python context with `ast` (enclosing class, bases, decorators), then classify by the rubric below.
3. Walk the pin with `git log -G` over `.lexicon.conf`, plus a first-parent value walk to catch merges. Read each stated reason from the commit body and the in-conf note.
4. Measure the drift proxies over the 5,428 non-`memory/` definitions.
5. Run each candidate's losing test against the real tree.

**Rubric, stated before classifying:**

| Class | Operational test |
|---|---|
| (a) forced by a third party | The name must equal a hook, protocol or data-model name of something outside the repo: a pytest hook, a Python dunder, or a shell function shadowing an external command. |
| (b) forced by own contract | Code outside the defining file reads the name **by name**, and that reader ships. |
| (d) false positive | The definition is not a callable the author named as an action: an IIFE-valued constant, or a `@property`. |
| (e) records/fixtures | The path is under `memory/`. No `tools/**/fixtures/` path carries an offender. |
| (c) real debt | Everything else. |

### 3. Measurements

**M1. The kit's own count**

```
$ python tools/lexicon/lexicon.py --offenders > off.tsv ; cut -f2 off.tsv | sort | uniq -c
      1 problem          # UNDECLARED EXTENSIONS: html, svg
      6 sh.function.conv
   1088 verb
$ python tools/lexicon/lexicon.py --measure
VERB_OFFENDER_PIN="1088"
$ python tools/lexicon/lexicon.py --list | tail
lexicon: verb offenders 1088 over pin 1087:   … and 1048 more
lexicon: P1 verb   graded=5710 offenders=1088 (debt=87 + unruled=1001) waived=0
```

`--list` caps at 40 rows (`lexicon.py:3284-3287`), so it cannot serve as a full census. The rows came from `measure_pass` directly.

**M2. Population by origin**

| Class | py | sh | js | Total | Examples |
|---|---|---|---|---|---|
| (a) third party | 5 | 1 | 0 | **6** | `crashprobe.py:147 pytest_configure`, `:160`, `:166`, `:172` (pytest hooks) · `lexicon.py:256 __str__` · `unattended.test.sh:9054 mktemp` (shadows the command) |
| (b) own contract | 6 | 0 | 16 | **22** | `boundedParallel`/`chunk` in 8 `tools/workflows/*.js` files (template and rendered), read by name at `agent-cap.js:1286,1413` · `all_symbols`/`inventory_ids`/`all_inventories` in `map_extractors.py:390,408,417` and `.template.py:104,123,132`, called on the adopter's module at `gen_map.py:38,138,149` |
| (c) real debt | 421 | 572 | 20 | **1013** | `.lexicon.conf` names e.g. `ts_*`, `demand_*` · `verb_plan` (`unattended.sh:5785`, one of 18 `verb_*` that the reserved `cmd` row already covers) · `ok`/`bad`/`say` suite helpers |
| (d) false positive | 3 | 0 | 1 | **4** | `agent-cap.js:1471 holder` (IIFE value, closes at `:1477`) · `@property` `map_lib.py:1281 has_block`, `:1398 clean`, `reuse_lookup.py:165 empty` |
| (e) records | 4 | 38 | 1 | **43** | `memory/builds/aSparedSpawn/build/*-direct-checks.sh` · `aMendedFleet-73-trial.js:38 boundedParallel` |
| **Total** | 439 | 611 | 38 | **1088** | |

Inside (c): 83 are debt and 930 unruled. 443 sit in test or selftest files and 95 are nested Python functions. There are 515 distinct unruled tokens, and 362 of them occur once. The 31 tokens with 5 or more sites account for 261 offenders.

Only 11 offenders are methods at all. On this tree, forced names (a+b) are **28 of 1,088 (2.6%)**.

**M3. The mechanism would turn forced names into debt.** This probe matters more than the count.

```
$ for n in do_GET emit handle setUp log_message visit_Name __exit__; do python tools/lexicon/lexicon.py --suggest $n --as py.function; done
use `cmd_get` — ... NOT `do`                         # http.server override broken
use `print` — the shipped canon says `print`, NOT `emit`   # logging.Handler.emit broken
use `run` — ... NOT `handle`                         # socketserver handler broken
use `set_up` — cell py.function declares snake       # unittest silently stops calling it
use `print_message` — ... NOT `log`                  # BaseHTTPRequestHandler.log_message broken
`visit` is not in the declared table ... SCOPING question
`exit` is not in the declared table ... SCOPING question
```

A work order that hands builders `--suggest` answers (a settled fact) would hand them renames that break overrides. Any adopter with stdlib or framework subclasses gets these. That population is not measurable here, because adopter reads are out of scope.

**M4. Pin history**, from first-parent value changes on `.lexicon.conf`, merges included, read out of each commit's diff.

| Commit | Date | Δ | Build/session | Stated reason | Names absorbed, by class |
|---|---|---|---|---|---|
| b06261529 | 08-16 | →412 | dClosedLexicon-1 | arm; "not a backlog" | scope |
| d54f0caf9 | 08-16 | +3 | dClosedLexicon | drift-audit growth, "deliberately NOT waived" | c ×3 |
| be0ee6a7c | 08-16 | +2 | dClosedLexicon-2 | `signal_*` house prefix | c ×2 |
| 667826019 | 08-18 | +46 | reconcile | 45 named, 1 moved | c |
| a8d1c1be4 | 08-18 | +33 | fix legs | govkit growth | c |
| 95737bc85 | 08-25 | −79 | dScaffoldedMirror-14 | `t_*`→`test_*`, `do_*`→`cmd_*` | drain |
| e16de5fe2 | 08-26 | +68 | dCarriedReceipt review | 70 named, all govkit | c |
| 267b598f0 / 3dee7112f / d8bbb16ca | 08-26 | +3/+3/+2 | dCarriedReceipt rounds | selftest helpers, `demand_*` family | c |
| 3b2d89c8a | 08-27 | +3 | aBoundedCeiling | inherited: dTieredTribunal landed without moving it | c |
| aa852df40 | 09-01 | −2 | dMispairedQuote-3 | dispatchers replaced | drain |
| e13436462 | 09-05 | +6 | aStagedLane | named and attributed | e ×4, b ×2 |
| 2d4870199 | 09-05 | +507 | aSurfacedLexicon-14 | shell armed | scope |
| 9a4da6b42 | 09-06 | +9 | aHoistedPass | 10 in, 1 out; `has`→check deferred | c |
| 4699cce60 / 4540897ee | 09-06/07 | +2 / −5 | aQuenchedHarness | `ts_tick_*` prefix / `mk_*`→`build_*` | c / drain |
| 78eb7488e | 09-12 | +2 | dPolishedVitrine-1 | "two forced names" | **b ×2** |
| cb2ab5418, d4509c29a, 39df2b1a8 | 09-13/14 | −1 each | cWidenedNet, aRatifiedRulings, aReplayedCard | renames | drain |
| 53a7a067f | 09-21 | −2 | dDerivedDocket-23 | moved and renamed | drain |
| 774bfecff | 09-24 | +6 | aRepatriatedFork-7 | "agent-cap.js keys on both names" | **b ×6** |
| e7d99c03c / e3d2cda9b | 09-24/30 | −7 / −7 | aRepatriatedFork-18/-30 | renamed, deleted | drain |
| 2d54cc085 | 09-28 | +89 | dDerivedDocket verify | helpers written "before ... `--suggest` first"; drain filed TOOL-dDerivedDocket-67 | c |
| e83b29b66 | 10-06 | −1 | aMendedFleet-53 | 7 out, 6 in | c ×5, e ×1 |
| 38e594a6f | 10-12 | +5 | aPrimedIndex-16 | inherited `pm_*` | c |
| 301a36664 | 10-13 | +24 | aSweptBar-6 | 30 in, all aSparedSpawn records, "frozen records, so the pin absorbs them" | **e ×30** |
| 8ddc0a482 | 10-13 | (+1 unrecorded) | aOrientedCast-22 | none; the pin was not moved, so the leg reads 1088/1087 | c |

Merges re-measured the value 21 times without adding names (for example `78c4bf7d1` 982→1071 and `106bf6e92` 1063→1087).

```
$ for h in $(git log --all --format=%h -- tools/lexicon/lexicon-verb-waivers.txt); do git show $h:tools/lexicon/lexicon-verb-waivers.txt | grep -v '^\s*#' | grep -v '^\s*$'; done | wc -l
0
```

**How sessions responded**, over the 30 non-merge moves:

| Response | Moves | Names |
|---|---|---|
| Raised the pin | 19 | +814, of which 507 is shell arming |
| Drained the pin | 11 | −107 |
| Added a waiver | **0** | 0, never once |
| Renamed before landing (stated in the record) | about 8 sessions | `cWidenedNet` 4, `aReplayedCard` 2, `aRepatriatedFork-7` 4, `-18` 7, `aTrimmedHook` 5, `aQuenchedHarness` 8 |

Across the history, the forced names absorbed are 10, all class (b) and none class (a). Records account for 35, and real debt for the rest.

**M5. Drift beyond verbs**, measured by `drift.py` over 5,428 non-memory definitions.

```
objects with >=2 acquire-family verbs: 57 defs: 165
  conf {'load': 11, 'read': 3, 'parse': 2}  map_lib.py:181 load_conf · scratch-guard.test.sh:946 read_conf · tree_lib.py:132 parse_conf
  registry {'read': 3, 'load': 1, 'parse': 1, 'resolve': 1}  encoding_posture.py:165 · govkit.py:244 · corpus_ids.py:809
  rows {'read': 4, 'parse': 1, 'resolve': 1}   line {'read': 2,'scan':1,'resolve':1,'parse':1}
objects carrying two spellings of one canon cluster: 6  repo[init,setup] repo[build,make,new] target[build,make] gate_runner[check,validate] coverage[compute,derive] ancestor[check,is]
noun variants: sha 13/oid 4/hash 4/digest 10 · dir 101/directory 1/folder 2 · rel 57/relpath 2/relative 2 · tmp 1/temp 1/scratch 24 · wt 2/worktree 27 · msg 1/message 8 · fixture 95/fix 5/fx 2
```

| Drift kind | Caught today? | Evidence |
|---|---|---|
| Synonym of a declared verb (`get` for read) | Yes, as DEBT (87) | `lexicon.py:2950-2965` |
| Two **declared** verbs over one object (`load_conf` and `read_conf` and `parse_conf`) | **No.** All 57 objects and 165 definitions pass. | P1 grades only the leading token |
| One noun spelled several ways (sha/oid/hash/digest) | **No.** The kit has no noun model; `grep -i noun` finds none. | `lexicon.py` |
| Type suffixes | Yes, P2 (`BANNED_SUFFIXES`) | `.lexicon.conf:17` |
| Case convention | Yes, conv cells (`sh.function.conv` 6) | `--list` |
| The rate itself | Drift signal `build_lexicon_marginal_offense_rate` | `drift_report.py:1434` |

### 4. Gaps

1. **G1.** The canon converts host-fixed names into DEBT with a rename (M3). Default policy and `--suggest` both point agents at breaking an override.
2. **G2.** There is no forced-name class at all. The only exits are a raise or a corpus-wide text waiver, which was refused for that reason (`.lexicon.conf:178`). Zero waivers in history; 19 raises.
3. **G3.** Records (e) drove the latest raise (+24 of the +30 arrivals in `301a36664`) and still sit in the count: 43 offenders. The path selector is `TOOL-aSurfacedLexicon-23`.
4. **G4.** Landings do not hold the equality: HEAD is red at 1088/1087 via `8ddc0a482`, the same shape as `3b2d89c8a`'s inherited red.
5. **G5.** Small false-positive surface (4): IIFE values and `@property` are graded as verbs.
6. **G6.** No measure of object-level verb drift or noun variants (M5).
7. **G7.** The premise can only be measured here for (b). This tree has almost no third-party subclasses, so the owner's "built-in verbs from 3rd-party kits" population lives in adopters, and it is unmeasured.

### 5. Candidates

Each candidate keeps forced names out of the debt count by default. Each losing test was written before running it.

| # | Mechanism | Losing test | Result |
|---|---|---|---|
| **K1** Inheritance oracle | A Python method whose enclosing class has a base not defined in the repo, and whose name that base defines, is classed as forced. | On this tree it must reclassify all 6 (a). | **LOSES as a sole mechanism.** It reaches 0 of 6: the 4 pytest hooks are module-level (`pyrows`: kind=top) and `Offender` has no base. It also cannot see JS or shell (b). |
| **K2a** Shipped per-host name tables, keyed by import | Rows like `pytest: pytest_*`, `logging.Handler: emit handle`, `http.server: do_*`, applied only in files importing the host. | `crashprobe.py`'s hooks must be exempted. | **LOSES.** `crashprobe.py:38-42` imports only faulthandler, os, sys, time and traceback; pytest loads the plugin without an import. |
| **K2b** Shipped per-host tables with a per-row scope kind | Each row carries a scope: **exact closed set** (pytest hookspec names, the data-model dunders, a command list for shell shims) needs no scope; a **generic name** (`emit`, `handle`, `default`, `run`) needs K1's base evidence. | (i) `query.py:968 emit` (module-level, free) and `govkit.py:1581 emit` (method of the base-less `Report`) must stay debt. (ii) All 6 (a) must leave the count. | **Passes both on paper.** (i) neither has a host base (pyrows: no bases); (ii) the 4 hooks are exact hookspec names, plus `__str__` and `mktemp`. It is unbuilt, so the build must run (i)/(ii) as fixtures. |
| **K3** Repo-declared contract names | The defining kit declares the names a shipped reader keys on (for example `boundedParallel chunk` read by `agent-cap.js`), next to that reader. A declared name the reader no longer matches reds as stale. | The pin must fall by exactly 22 (M2 b). Deleting `boundedParallel` from `agent-cap.js:1286` while leaving the declaration must red. | The 22 are identified; the stale arm is unbuilt and owed. It loses if keyed by text alone: the record copy `aMendedFleet-73-trial.js:38` (e) would be exempted with it. |
| **K4** Site annotation (`gov:note forced=<host>`) | The author marks the definition line, and the extractor moves it to a separate *forced* tally. | An annotation on a free name, for example `# gov:note forced=logging` on `query.py:968 emit`, must red. | **LOSES unless verified by K1/K2b.** Nothing in the annotation proves the host defines the name. Otherwise it is the corpus-wide waiver again, made per-site. |
| **K5** Existing text-keyed waivers, unchanged | Add rows to `lexicon-verb-waivers.txt`. | Adoption: in 30 pin moves sessions must have used it at least once. | **LOST: 0 rows ever** (probe above). The record says why: "a waiver asserts deliberate exception" (`d54f0caf9`), and it waives every copy (`.lexicon.conf:178`). |
| **K6** Exclude all methods from P1 | Grade only module-level functions. | Real method debt must survive: `drift_report.py:467 is_commit` and `:470 is_ancestor` (DEBT `is`→check) on the base-less `Git` class. | **LOSES.** It drops 11 offenders, including at least those 2 real debts, and misses the 4 module-level pytest hooks. |

Records (e) and false positives (d) fall outside the forced question. `TOOL-aSurfacedLexicon-23`'s path selector would move 43 (the source of 35 historic absorptions); an IIFE/property extractor fix would move 4.

### 6. Pick

**K2b scoped by K1, with K3 for own-contract names. Forced names go into a reported `forced=` tally, never into the pin.**

- K2b is the only candidate that passes both losing tests on this tree:
  - It takes the 6 (a), where K1 and K2a fail.
  - It keeps `emit` at `query.py:968` and `govkit.py:1581` as debt, where a bare name table fails.
- K3 takes the 22 (b) from a declaration kept next to the reader that forces them, with a stale arm. That is the place `.lexicon.conf:176-178` already says the constraint lives.
- K4 is acceptable only as a fallback whose claim K1/K2b re-verify.
- K5 and K6 are rejected by their measured tests.

The build must show:

1. The 6+22 reclassify, and the pin falls by 28 under a `shrink-only` default.
2. M3's seven `--suggest` calls stop proposing renames, so the work order's `--suggest` answers are safe.
3. Both `emit` fixtures stay debt.
4. An adopter-side census of class (a) before shipping any table beyond pytest, unittest, http.server, ast, logging, json and the dunders. G7: this tree cannot size it.

The re-architecture should also count the M5 gap, one concept under three declared verbs (`conf`: load 11 / read 3 / parse 2), as a separate enforcement gap. The verb pin cannot see it.
