# Synthesis — the adversarial pass's own report

**Serves:** journal TOOL-aProbedToolkit-1

Written by the synthesis agent from 45 graded findings. Kept verbatim, because it is the pass's own
reasoning and because two of its conclusions were checked against the tree here and one of them
changed: its refutation of the retired-conf-key finding is CORRECT, and what replaces that finding
is recorded in the measurements journal under the nicocares fork. Its '81 renames' figure was not
re-derived here; the pin-history table in the measurements journal is the verified version of the
same argument.

# Toolkit adversarial review — synthesis

Four kits (`memory-tree`, `memory-recall`, `lexicon`, `codebase-map`) measured across four repos
(gov, incms, nc, swydee). 45 findings graded by a skeptic pass: 44 CONFIRMED, 1 REFUTED, 11 with
material corrections. Nine defects (F1–F9) were already on the record before this pass and are
referenced, not re-argued.

---

## 0. Top line

Every one of these kits works in the tree that wrote it and does measurably less everywhere else.
That is not four independent bugs; it is one shape repeated four times, and it has three legs:

1. **The gate grades the population that was easy to enumerate, not the one the tool exists to
   serve.** memory-recall's floor grades a records-only index at k=5 while the CLI ships a fused
   list at k=20. codebase-map's ratchet grades inventory KEYS in both directions while file coverage
   runs entirely through ungated globs. lexicon grades every `ast.walk` FunctionDef including
   closures and pytest hooks. memory-tree grades 21 of 88 build READMEs.
2. **A disarmed rule is byte-identical to a satisfied one.** The shipped memory-tree conf turns off
   six checks including the largest one, silently. codebase-map prints five greens over a dossier
   set that selects zero files. memory-recall's two diagnostics are zero-predicates, so a 90%-dead
   index and a 99%-dead alias layer are both silent. Every kit's own header preaches "a skip must
   announce itself"; every kit breaks it.
3. **The install prefix is `tools/` in the source and nowhere else.** One gate leg is dead at every
   adopter (blocker #1), one selftest arm skips with a false reason (F3), and the one mechanism
   designed to catch a forked engine is the one that cannot run where the fork lives.

The distribution story is the amplifier: four repos, four prefixes, three forks, no version
verification, no upgrade path, no adopter feedback loop. Two adopter-filed kit defects (swydee's
EXTR-aPatientHarvest-3 and -4) have sat OPEN for weeks; one was fixed upstream as a default and
never as a check, the other is still live at the shipped configuration.

---

## 1. Per-kit verdict

### memory-tree — **KEEP-WITH-FIXES**

Serving its purpose, in gov. The full gate runs in 17.6 s, exits 0 with 386 bytes, and fourteen
staged synthetic breaks lit checks 2, 3, 4, 6, 9, 12, 20 and 21 — it is a working gate, not a
decorative one. The corpus-facing verbs earn their keep: `gotchas.py --for-diff` returns a bounded
1.3 KB bug-class checklist, `--print-bindings` is the migration path check 21's remedy actually
names, and the pop_guard/precondition split is a real answer to the empty-selector class.

Still relevant: yes, and it is the load-bearing kit — the other three depend on the tree it enforces.

The caveats are all one caveat: **the adopter does not get the same bar.** `check-verdict-epoch.sh`
cannot run at any prefix but gov's, which is why nc runs a 116-line local fork of the 2.49 engine
while its version marker reads a pristine `2.49`. The shipped `.memory-tree.conf.example` hands a
fresh adopter check 12 (378 lines, the largest in the file) plus five other rules disarmed with no
runtime announcement. And the shipped `FORK_MARK_CUTOFF=""` reds 72 of gov's own correctly-resolved
specs — the adopter's first experience of check 12 is 72 false positives on a corpus that conforms.

### memory-recall — **KEEP-WITH-FIXES**, and **NARROW on small corpora**

The retrieval half is a real instrument. 33 graded questions across four repos, ground truth read
first: the answering record landed in the top 5 for 32 of 33 (gov 10/10 mean rank 2.3, nc 9/10 mean
2.7, swydee 10/10 mean 1.8, incms 3/3), ~430 ms warm, ~15 KB out, against a naive grep's median 33
files. Keep it on gov, nc and incms.

Narrow it on swydee-scale trees: 8 of 10 answers there were rows in a 7,812-byte `DECISIONS.md` that
costs less to read whole than one 10,153-byte query. The kit is clearly positive for the 1.2 MB of
build records behind that file and marginal for the ratified index itself. Its README says as much,
honestly; its 20,000-byte default budget does not, being inCMS's number for a corpus 16x larger.

The measurement half is aimed at the wrong target and is the fix list: the floor grades a
configuration the CLI does not ship, its fixture is one family out of four, and both of its "this is
broken" diagnostics fire only on total failure.

One claim needs softening rather than fixing. The head-to-head study that would justify
"retrieval beats grep" came back `verdict: UNDERPOWERED` upstream — population B realized n=5
against a pre-registered threshold of 53 — and the harness that would run it was dropped in the gov
fork. The rendered SKILL discloses this. AGENTS.md §5 and the shipped charter template do not.

### lexicon — **NARROW** (and RETIRE P1 as a merge-bar leg)

Not serving the purpose it was built for. The gate does one thing reliably: it counts function
definitions whose leading token is outside a 23-row table and refuses to let the count rise. That
count does not measure naming quality. Of gov's 461 offenders, 123 (27%) are test arms or nested
closures no caller can name, 5 are pytest hooks and protocol dunders whose spelling is not the
author's to choose, and the set spans 281 distinct leading tokens — a long tail of domain nouns, not
a small set of wrong-verb spellings. Grading fifteen offenders by hand: 4 point at something a
reviewer would also flag, 3 report a missing table row, 8 are noise, and **zero** surfaced the
unclear responsibility or misplaced seam that LEXICON.md claims is the instrument's entire value.

The pin's own history says the same thing quantitatively: 8 raises totalling +130, two drains
totalling −81, net +49, one raise logged verbatim as "to unblock a landing the owner asked for", and
the only substantial drain was 52 mechanical `t_*`→`test_*` renames plus 27 sites absorbed by adding
a table row. Three weeks, 81 renames, zero responsibilities changed. The kit's own author cannot
pass it: 10 of the 45 definitions in `tools/lexicon/` are offenders, including both public functions
of `subtokens.py`.

Adoption confirms it: deployed into two repos, adopted by neither, live adoption = 1 (the author).

**What to keep, and it is real:** the engine is unusually well-defended (unselective-rule refusal,
DEAD PROBE, DEAD SNIFFER, STALE WAIVERS, the CRLF-inverts-the-refusal fix — all with observed
failing cases); the canon is genuinely prescriptive rather than a corpus mirror; `--brief`'s
object-level "spelled more than one way" output is the one thing here a reviewer would not get for
free; and the whole thing costs 1.3 s on the bar. Narrow P1 to public module-level definitions in
non-test files, wire canon into `--suggest`, add `ts`/`tsx`, gate the coverage floor — then
re-measure the pin. Shipping it unchanged to a second adopter hands them a fabricated architecture
rule, an inherited pin, and a refusal that cannot tell them what to type instead.

### codebase-map — **KEEP-WITH-FIXES** in gov and incms; **RETIRE at nc**

The kit verifies an inventory of NAMES and is being read as an inventory of the system. The key
ratchet is genuinely both-directional and worth keeping. File coverage is not gated at all — it runs
through dossier `paths.globs`, which the gate never reads and the scaffolded README openly calls
"digest-only, never gated". Derived over tracked source (excluding memory/ records and vendored
trees): **incms 971/2509 (38%), gov 98/144 (68%), nc 0/180 (0%)** — and nc's five gate legs all
print `ok`, because six of its seven dossiers declare `globs = []` and all 198 of its keys are
content, not code.

gov, the repo that ships the kit, cannot attribute `tools/push-main.sh`,
`tools/drift-audit/drift_report.py` or `tools/memory-tree/gotchas.py` — the three commands its own
AGENTS.md tells every session to run.

nc is the retire case: 0 source files attributable, 81% of keys still parked in the baseline after
seven weeks, a symbol tier declined on a count that was 17x low when it was written, and a
`reuse_lookup` that answers "normalise a path for windows" with three `.webp` filenames. Either grow
source dossiers there or stop running it — five greens over an empty population is worse than no
gate.

The engine's portability holds (root resolution is prefix-free and cwd-independent; the hardcoded
`tools/` rot is confined to `selftest.py`), and the kit is one assert away from honesty in three
places: baseline growth, the symbols.json compare, and a source-coverage number the gate reports
itself.

---

## 2. Confirmed defects, ranked by severity

Severity = blast radius × silence. Everything here reproduced under skeptic verification.

### Blockers

**B1 — the version-marker gate is dead at every non-gov install prefix**
`tools/memory-tree/check-verdict-epoch.sh:68` — `ENGINE=tools/memory-tree/check-memory-hygiene.sh`,
a literal, with `exit 2` on a miss (line 70). Both adopters ship the same byte at their own line 68.
*Repro:* `cd nc && bash scripts/check-verdict-epoch.sh; echo $?` → prints a path that exists at
neither install, exit 2. *Consequence:* nc runs a 116-line fork of the 2.49 engine (loosened
build-slug regex, four extra registries, a whole local `RECORD_SERVES_CUTOFF` feature) while
`KIT_MEMORY_TREE_VERSION=2.49` claims pristine. The one mechanism designed to catch exactly that is
the one that cannot run there. `kit.toml:108` already parametrizes the leg as `{kit}/…`, so the
descriptor is prefix-free and the script is not. Neither adopter has wired it yet, so today this is
dead-on-arrival rather than a red bar — the next adopter who wires it from `kit.toml` gets the red.
*Fix:* derive `ENGINE` from `$0` using the `HERE=` idiom already at `check-method-carriers.sh:26`,
and add a selftest arm at a non-`tools/` prefix.

**B2 — the recall floor's fixture is one family of four; three can be mis-declared and the gate
stays green**
`tools/memory-recall/recall-fixture.json` — all 12 `expected_ids` are `TOOL-`. gov declares four
families and anchors 860 records (TOOL 780, DEPL 67, PLAY 12, KICK 1). *Repro:* rewrite FAMILIES to
`playbook:PLAZ kickoff:KICZ tooling:TOOL deployer:DEPZ`, `rm -rf .git/recall`, run
`check-recall.py` → `per-id ok — every expected id resolves (12/12)`, `RECALL_FLOOR ok — 0.8333 >=
0.81`, rc=0, while the index silently drops 860 → 780 records and the probe question's correct
answer leaves the record arm entirely. All 20 arms of `test_recall_floor.py` build their scratch
conf as `FAMILIES="tooling:TOOL"` (lines 121, 422) — a single-family world where the hole cannot
exist. *Fix:* one assert — `{id.split('-')[0] for id in expected_ids} == set(CONF.families)` — plus
at least one non-TOOL question.

**B3 — lexicon P1 grades a population it was never designed for**
`tools/lexicon/lexicon.py:219` — `_python_defs` uses `ast.walk`, so nested closures, methods and
dunders are all graded. 123 of gov's 461 offenders (27%) are test-file arms or nested closures no
external caller can name; the union of {test file} ∪ {nested} ∪ {leading underscore} is 208 (45%).
On incms the same predicate yields 6,539 offenders of 14,835 defs, 2,593 of them in test files.
Waivers key on identifier TEXT, not path, so there is no existing escape hatch. *Repro:*
`python tools/lexicon/lexicon.py --list | grep -c 'selftest.py\|bench.py\|test_'` → 99 of 461.
*Fix:* track enclosing scope in `_python_defs`, skip nested defs and dunders, add a conf key for
test-harness paths — then re-measure the pin.

### Majors

**M1 — the shipped memory-tree conf disarms six rules, silently**
`tools/memory-tree/.memory-tree.conf.example` — blank `SPEC_FORMAT_CUTOFF` (check 12, 378 lines,
`check-memory-hygiene.sh:767–1145`), `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF`,
`SPEC10_EVIDENCE_CUTOFF`, `FORK_MARK_CUTOFF`, `REVIEW_VERDICT_CUTOFF`, `ACCEPTANCE_LEDGER_CUTOFF`,
`ORPHAN_ID_PIN`/`DEAD_PATH_PIN`. *Repro:* stage the same break (every `## ` section deleted from a
post-cutoff Tier-2 spec) under gov's conf → `check 12 FAILED`; under the shipped example →
`check 6 FAILED`, byte-identical to the example-conf CLEAN run. Check 12 neither fires nor says it
is off. Check 23's own two announce lines are themselves gated on its key being set. The example's
comments and the scaffolder's `Next:` list mention three of the six once, outside the gate.
*Fix:* one `announce_off <n> <key>` helper printing `check <n> NOT ARMED — <key> is blank` on every
run, called from each blank-means-off site.

**M2 — the shipped `FORK_MARK_CUTOFF=""` reds 72 conforming specs**
`tools/memory-tree/check-memory-hygiene.sh:1022` — the loose branch counts a `RESOLVED` mark only on
an item's OPENING line, while the kit's own comment at :967 records that "246 of 339 items carry a
conforming mark and nearly all of them carry it on a continuation line". The tightened `bmark`
reader at :1013–1020 is reachable only behind the opt-in date. *Repro:* blank `FORK_MARK_CUTOFF` in
gov's conf → 72 × `terminal Status with unresolved §8 Open questions`, all post-cutoff specs that
pass the tightened reader. swydee declares the key not at all, so **EXTR-aPatientHarvest-4 is still
live**, not fixed. *Fix:* delete the :1022 branch, make `bmark` unconditional, keep the key for the
hollow-section arm only.

**M3 — deleting codebase-map's whole symbol tier leaves every leg green**
`gen_map.py:141–144` and `test_codebase_map.py:140–144` both read `symbols = getattr(ext,
"all_symbols", list)()` then guard the artifact behind `if symbols:`. *Repro:* replace
`map_extractors.SYMBOL_EXTRACTORS` with `{}` on a copy of gov → coverage gate 5× ok exit 0,
`gen_map.py --check` exit 0, kit selftest PASS, `symbols.json` still committed at 84,124 bytes, and
`reuse_lookup.py` still prints `corpus: 609 symbols` with no staleness notice, because its
`has_symbols` test is file presence (`reuse_lookup.py:153`), not freshness. Fan-in is then computed
live over paths listed in a frozen JSON. *Fix:* compare `symbols.json` unconditionally; an empty
tier with a committed artifact is a hard failure, not a skipped compare.

**M4 — codebase-map's file layer has no liveness assertion**
`map_lib.py:1340–1369` (four asserts, all over inventory keys) and `map_lib.py:1503` (`attribute_
paths`, globs asserted by nothing). *Repro:* `cd nc && python scripts/codebase-map/
test_codebase_map.py` → five `ok`, exit 0, with 0 of 180 tracked source files attributable and six
of seven dossiers declaring `globs = []`. `map_diff <root>..HEAD` independently reports nc at
28/1953 files (1%), all markdown. gov: 46 of 144 source files unmapped, including `push-main.sh`,
`drift_report.py`, `gotchas.py`, `check-wiring.sh`, `corpus_ids.py`, `resolve-python.sh`, both
pytest-guardrails sources and every `*.test.sh`. The map's convergence forcing function cannot fire
for a file no dossier and no key names. The README does disclose that globs are never gated — the
defect is the missing DEAD-PROBE line, not a false claim. *Fix:* red (or print DEAD PROBE) when a
dossier's glob set selects zero tracked files, and report source coverage from the gate.

**M5 — the recall floor grades a configuration the CLI does not ship**
`check-recall.py:69` — `SETS = ("spine","records","chunks")` has no ensemble token, and
`check-recall.py:199` feeds `bench.rank_with` the raw un-rewritten question. The CLI
(`query.py:1177`) serves `rrf([search(records), search(chunks)])` at default `--k 20` and requires
`--terms`. *Measured on the kit's own 12-question fixture:* gate 0.8333; shipped CLI at defaults
9/12 = 0.7500; CLI at `--k 5` = 0.8333. The README names `9/12 = 0.75` as the value a regression
produces. Fixture question 8 scores `hits: yes` while sitting at CLI rank 6 with five chunks above
it — and the chunk arm scores r@5 0.08 alone, yet takes rank 1 in 8 of 12 fixture runs.
*Fix:* add an ensemble token to `PIN_RE`/`SETS` and grade the fused list at the CLI's own k, or
state in the gate's header what it does not check. `union.py` already scores ensembles and runs.

**M6 — the ZERO RECORDS diagnosis is a zero-predicate**
`extract.py:390` — `if n_records: return None`, with a docstring naming the exact case it misses.
*Repro:* in swydee change `orchestration:ORCH` → `ORCK`, clear the cache → `index 23 records` (was
31), no diagnosis, rc=0, and the answering record for a graded question is replaced at rank 1 by an
unrelated one. A one-character typo in one family of four is invisible; only total failure speaks.
*Fix:* `for fam in CONF.families: if not counts[fam]: warn(fam)` — the counts are already computed.

**M7 — two kits state the backlog row shape and disagree; the one that obeys the template indexes
zero backlog rows**
`extract.py:115` — all four anchors require the id immediately after the list marker.
`adopt-memory-tree.sh:238` writes each backlog with "Each row leads with one status token". A repo
that obeys writes `- OPEN · ORCH-… ·` and matches no anchor. *Measured:* swydee 31 anchored records,
all 31 from `DECISIONS.md`, **0 from `memory/backlog/`**, 5 orphan ids all of them backlog rows;
moving the status token after the id on ONE row takes anchored 31 → 32 and orphans 5 → 4. gov and nc
index 349 backlog records only because they violate their own stated convention. *Fix:* one source
for the row shape — either a fifth anchor accepting a leading status token, or change line 238.

**M8 — the lexicon pin is a one-way ledger**
`lexicon.py:697` — `if len(unwaived) > pin`, strictly greater, so a stale pin can never red, while
`.lexicon.conf:29` declares in its own words "Shrink-only: the count may fall, never rise".
*Repro:* set `VERB_OFFENDER_PIN="900"` → `lexicon OK`, rc=0, printed one line under
`offenders=461`, with nothing comparing the two. drift-audit's `signal_shrink_only`
(`drift_signals.py:78`) names five `memory/project/*.txt` registries and neither `.lexicon.conf`'s
three pins nor the kit's three waiver files. *Fix:* red on `<` too, naming the new value.

**M9 — the lexicon gate is legally green at 8% coverage**
`lexicon.py:729` (coverage printed, decides nothing) and `:604` (`if mode == "dark": continue`,
skipping DEAD PROBE). *Repro on gov:* declare `py::dark`, invent a LAYERS rule between two
directories that never import each other, drop the pin to 45 → both legs exit 0
(`lexicon OK — 1393 tracked file(s)`, `lexicon-adopt OK`) with coverage down from 42.0% to 8.0% and
graded from 1047 to 122. `scan_unselective_rules` (`:447`) refuses a rule whose globs match nothing
and cannot refuse one whose direction no import ever takes — its own docstring says "This does NOT
prove a rule is reachable. It cannot." gov's single real rule is that shape by construction.
*Fix:* declare a coverage floor and red below it; drop P3 or require a crossing somewhere in
history.

**M10 — `--suggest`, the kit's whole remedy, answers 1.5% of its own findings**
`lexicon.py:850` — `run_suggest` resolves only through `build_banned_index` (23 tokens). The 461
offenders carry 281 distinct leading tokens; the intersection is 5 tokens over 7 sites. For the
other 454 it prints the refusal plus a dump of the table — literally "read a copy of the table",
which §12 exists to replace. `canon.build_form_index()` ships 120 forms mapping `is→check`,
`list→read`, `make→build`, `ensure→check`, `find→scan`; `lexicon.py` **already imports canon at
line 84**. *Fix:* one lookup in the else branch — answerability 7 → 43 of 461.

**M11 — `RECALL_DARK_LAYERS` is a hand-typed second answer to what `SYMBOL_EXTRACTORS` covers**
`reuse_lookup.py:172` parses it; `:320–329` fires the partial-recall notice only on that string;
nothing anywhere compares it to what `symbols.json` holds. incms declares `""` ("Empty once Python +
TS/JS are both covered") while its symbol corpus covers `.sh` 0/77, `.js` 0/23, `.cjs` 0/1, `.py`
394/1164, `.ts` 279/637 — so neither notice branch fires and the run ends on a confident
"or reply 'no seam fits'". nc declares the key not at all. *Fix:* derive the covered set from
`symbols.json` and notice on any tracked source extension outside it.

**M12 — `reuse_lookup` returns image filenames as reusable seams**
`reuse_lookup.py:153–179` folds inventory keys and dossier prose into the same ranked list as
symbols; `:327–329` prints "symbol recall tier not adopted" BELOW the shortlist. *Repro:*
`cd nc && python scripts/codebase-map/reuse_lookup.py "normalise a path for windows"` →
`hero-window-mug-inkwash.webp`, `hero-window-tea-inkwash.webp`, `ink-window.webp` [media], and the
closing line still says "wire the behaviour through one seam above". Precision across six realistic
queries: incms 60/60 symbol rows, gov 34/50, nc 0/12. *Fix:* with 0 symbols, refuse — or at minimum
print the notice above the list.

**M13 — nc's decision to skip the symbol tier rests on a count that was 17x low when written**
`nc/scripts/codebase-map/map_extractors.py:6–9` — "run against this repo it found 26 symbols".
Re-measured with the kit's own parser: 719 python symbols today (scripts 596, tests 109, brand 5,
backend 9), and 435 at the commit that added the docstring. The premise "ships no runtime code" is
true of `package/` and false of the repo, which is what the map inventories. *Fix:* re-measure and
re-decide; a whole recall capability was declined on a number off by 17x.

**M14 — lexicon is dark over the entire frontend of its only large adopter**
`lexicon.py:102` — `KNOWN_EXTS = {"py": …, "js": …}`. incms scaffolds 43 of 45 extensions dark;
running the **shipped** js-regex over its tracked `.ts/.tsx` finds 915 files and 3,711 definitions —
identical syntax, no new extractor needed. *Fix:* two lines adding `ts` and `tsx` to `KNOWN_EXTS`.
Do NOT arm `sh` until B3 lands: it adds 485 offenders to gov, 61% of them in test harnesses.

**M15 — `spine` extracts to zero docs in every flat memory tree, and it is a fork regression**
`extract.py:131` — `DURABLE` requires a directory segment between `MEMORY_ROOT` and the index file.
gov 860 records / spine 0; nc 609 / 0; swydee 31 / 0. Upstream's regex is flat-correct
(`memory/DECISIONS\.md$|memory/backlog/[^/]+\.md$|…`) and yields `durable home: 2348` on incms — the
gov fork's "generalisation" inserted a segment upstream never had. swydee's ORCH-aFlattenedLedger-4
filed this against kit 1.0; gov is at 1.4 and it is still 0. *Fix:* port upstream's three
alternatives verbatim; the proposed optional-segment patch still misses the backlog shards.

### Minors (grouped, one line each)

- `subtokens.py:29` strips leading underscores, so `__repr__`, `__call__` and `pytest_configure` are
  graded as bad names the author is forbidden to change (gov 5, incms 67) — skip dunders, ship
  seeded hook waivers.
- `map_lib.py:1340` has no fifth assert on baseline growth: "shrink-only" is stated in five places
  and enforced nowhere; one demonstrated violation fleet-wide (incms `flags:
  plugin_css_allow_positioning`, added with zero removals).
- `map_lib.py:858` returns `SEAM_FANIN_THRESHOLD_DEFAULT` on an absent key with no notice; nc
  declares neither recall knob, gov's comment admits the pin is unmeasured. At threshold 3, gov
  marks 11/50 candidates SEAM and incms 57/60 — the same pin means "rare" and "almost everything".
- `attribute_paths` globs rot silently: incms carries 4 dead globs of 609, each naming a deleted
  test. Live harm is a rename, not a delete.
- `map_diff.py:12–15` promises the affordance grace shrinks mechanically; `--drop-affordance-exempt`
  has no automated caller in any of the three repos (only a runbook step in WIRE-INTO-PROJECT.md:319).
  incms: 72 of 84 dossiers still graced after six weeks.
- `tools/memory-recall/README.md:197` calls `bench.py`/`union.py` "inert here"; both run against the
  shipped fixture in one command, and `union.py` is the only instrument that can score the ensemble
  M5 needs.
- `query.py:1` states `recall@20 0.71 → 0.84` with no provenance while README and SKILL both say
  "upstream"; the figure is inCMS's, on a 184-query fixture and 1,613-record alias layer that do not
  ship, and the A/B harness was dropped in the fork.
- `query.py:132` — `DEFAULT_BUDGET = 20_000` carried unchanged into a 1.2 MB tree where one query
  costs 1.3× the entire `DECISIONS.md` it usually answers from; a budget sweep shows everything
  above 12,000 is pure slack there.
- `check-memory-hygiene.sh:292` leaves `memory/guides/` and `memory/archive/` opaque: any filename,
  any file kind. Two of five staged strays are caught incidentally by codebase-map; a non-`.md` file
  under `guides/` and anything under `archive/` escapes every check (and swydee ships no map).
- `adopt-memory-tree.sh:46` claims it never scaffolds demo disciplines; the second run does exactly
  that, and the kit carries two demo taxonomies that disagree (`ARCH/DEPLOY/BLOCK/DES/PERF` vs
  `ARCH/DEPL/DES`). One `cmp -s` against the example closes it.
- `gotchas.py:125–144` raises `Problem` from the front-matter parser, caught by main() and printed
  without a check number, aborting checks 17–19 before they run; a red bar where
  `grep 'HYGIENE check [0-9]* FAILED'` returns nothing.
- `REVIEW_DIR` is answered by the renderer and refused by `check-memory-hygiene.sh:384`
  (`k=="D:reviews"`, string equality) with nothing validating the pair — swydee hand-edited its
  rendered AGENTS.md, which the placeholder's own comment says is the repair that gets reverted.
  EXTR-aPatientHarvest-3 fixed upstream as a DEFAULT, never as a CHECK.
- `HYGIENE.template.md` numbers checks 1–22 under a heading claiming to be the complete catalog;
  check 23 has a contract section but no catalog entry, and `README.md:18` writes the literal
  "23 checks" — a derived count in prose. The parity harness compares template to rendered copy, so
  it structurally cannot see a gate/doc divergence.
- `build-readme-slot-highwater.txt` is a seeded median, not a high-water: 39 of 105 slot
  measurements breach it every run, 76% on one slot, and two of five ceilings sit within 5 bytes of
  the corpus max. `--bump` fixes it in one command. Both that file's header and
  `build-readme-slot-limits.txt:18` still describe themselves as empty/non-binding.
- `.lexicon.conf` was curated nine days before `canon.py` landed, in the same tree, so canon's
  "reproduces a curated table it never saw" cannot be independence evidence. The vocabulary
  converged anyway (canon's 20 ⊂ gov's 23), so the harm is provenance, not spelling.
- Both non-gov lexicon deployments are incomplete: incms is missing `kit.toml` entirely (govkit
  cannot see the kit), nc is missing `SKILL.template.md` (the adopter gets a green wiring leg with
  the entire author-facing surface absent). Neither has a `.lexicon.conf`, neither wires a gate leg.

### Observations worth carrying

- 67 of 88 build READMEs are exempt from the slot canon (`readme-contract.txt`), the pin is an
  equality with per-row drain conditions and a named converter — honest, owned, and still 76% of the
  corpus. `--survey` prints 87 KB nobody can act on in one sitting.
- `TERM_BAND = (8, 14)`: the upper element is never a predicate. Over-supply is the likelier failure
  and the unwarned side; measured, it is harmless today.
- The DEAD ALIAS diagnosis is also a zero-predicate (1 live + 99 dead is silent). Disclosed in the
  docstring. No alias data ships anywhere, so half of the published retrieval gain is structurally
  absent from every install.
- `.claude/hooks/agent-cap.js` and `tools/hooks/agent-cap.js` are byte-identical at 93,786 bytes;
  `scratch-guard.js` at 17,235; `recall-opened.js` at 9,447. The JS extractor walks `ROOT/"tools"`
  only, so one side of each pair is invisible to `--converge`'s reinvention detector — 120 KB of
  one-sided duplication the kit is structurally unable to flag.
- No codebase-map command reports whole-tree coverage without being handed a range, and the one
  percentage it does print is dominated by `memory/` records (F4).
- 10 of the 45 definitions in `tools/lexicon/` are P1 offenders (22%), including both public
  functions of the module the predicate rests on. Cleanest available evidence that the leading-token
  predicate does not discriminate good names from bad.

---

## 3. Invisible / omitted / malformed / duplicated

### memory-tree

**INVISIBLE.** Anything installed at a prefix other than `tools/memory-tree/` (B1) — including a
116-line forked engine wearing a pristine version marker. With the shipped conf: checks 11, 12 and
its four sub-ratchets, 13–15, 22 and 23. The contents of `memory/guides/` and `memory/archive/` —
any filename, any file kind, arbitrary nesting. Any `.memory-tree.conf` key the gate does not read:
the conf is sourced wholesale and validated only for the ten size caps, so a misspelled, invented or
genuinely retired key is a bound the adopter believes they still have. 67 of 88 build READMEs.

**OMITTED.** The "NOT ARMED" line for every blank-cutoff rule, on every run — the single largest
gap, and the kit's own header preaches it. The check number on a gotchas front-matter abort. Check
23's entry in a catalog that claims completeness. A refusal when the scaffolder is handed the
unedited example conf.

**MALFORMED.** `build-readme-slot-highwater.txt` (a seeded median presented as a high-water, 37% of
measurements breaching). Two file headers describing themselves as empty/non-binding while carrying
rows and binding. `README.md`'s "23 checks" literal. The two disagreeing demo taxonomies. The loose
§8 `RESOLVED` reader left standing beside the tightened one that replaced it.

**DUPLICATED.** `HYGIENE.template.md` ↔ `memory/HYGIENE.md`, compared to each other by the parity
harness and to the gate by nothing. The demo taxonomy, in the adopt script and in the example conf.
The reviews-directory name, owned by the renderer's default and by check 4's string literal, with
nothing joining them.

### memory-recall

**INVISIBLE.** Every backlog row written the way memory-tree's own template prescribes (M7) —
swydee indexes zero of them. The `spine` document set, in every flat tree (M15). Any family whose
FAMILIES entry is mistyped (M6) — 9.3% of gov's index, silently. The fused RRF list the user
actually reads (M5). A 99%-dead alias layer. And every adopter: the floor, the fixture and its test
are withheld as project-owned, so nc and swydee have no retrieval check at all.

**OMITTED.** Seven upstream instruments dropped in the fork — `grep_study.py` (the recall-vs-grep
head-to-head), `rewrite_bench.py` (the A/B for the figure `--help` quotes), `ceiling.py`,
`redundancy.py`, `alias_bench.py`, `alias_distinct.py`, `session_stats.py` — plus upstream's
behavioural selftest arm asserting `union.SUBS` and `bench.rank_with` agree. Per-family record
counts. The upper `TERM_BAND` arm. Any alias data at all, in any repo.

**MALFORMED.** The README's "inert here" (both harnesses run against the shipped fixture).
`query.py --help`'s unqualified `0.71 → 0.84`. `DEFAULT_BUDGET`'s comment presenting inCMS's
measurement as "the MEASURED cost of the shipped configuration". AGENTS.md §5 **and the shipped
charter template** asserting "retrieval beats grepping it" against an upstream verdict of
UNDERPOWERED.

**DUPLICATED.** The recall-gain figure, in three carriers, two of which qualify it and the one the
CLI prints does not. The backlog row shape, stated by two kits that declare a dependency. The
`DURABLE` regex, forked from a correct upstream into a broken one.

### lexicon

**INVISIBLE.** `.ts`/`.tsx` — 980 definition-carrying files and 3,711 definitions on the flagship
adopter, with a working extractor already in the box. `.sh` — 89 files and ~581 definitions in gov,
whose definition regex is already in the file, used only to count what it refuses to grade. 43 of 45
extensions at incms. Any language an adopter declares `dark` (DEAD PROBE is skipped outright). Any
LAYERS violation that no import ever takes. A pin that has fallen below the true count.

**OMITTED.** A coverage floor (the number is computed, printed, and decides nothing). The `<` arm of
the ratchet. Seeded waivers for protocol slots and plugin hooks. A canon fallback in `--suggest`.
`kit.toml` at incms; `SKILL.template.md` at nc; `.lexicon.conf` at both.

**MALFORMED.** The offender population itself (B3) — closures, test arms, dunders, pytest hooks.
`.lexicon.conf`'s "Shrink-only: the count may fall, never rise" sitting above a `>`-only predicate
that has been raised eight times. `canon.py`'s independence claim. `--brief`'s
"SPELLED MORE THAN ONE WAY" firing on `read_set`/`write_set`.

**DUPLICATED.** The verb table: declared in `.lexicon.conf`, rendered into a byte-compared Skill
(correct), and printed a third time by `--suggest` as its refusal — the exact copy §12 says to
replace with "ask it per name".

### codebase-map

**INVISIBLE.** Every source file no dossier glob and no key names: gov 46/144, incms 1,538/2,509,
nc 180/180. `.claude/hooks/*` — the JS extractor walks `ROOT/"tools"` only, so 120 KB of
byte-identical duplicated hooks is structurally unreachable by the reinvention detector. Every shell
script and two thirds of the Python at incms. An emptied symbol tier (M3). A baseline that grew.
A dossier whose globs select nothing.

**OMITTED.** A whole-tree coverage number from any command. A DEAD-PROBE line for an empty glob set.
The fifth `compute_coverage` assert. An unconditional `symbols.json` compare. A duplicate-claim
count (the rows are rendered in MAP.md; only the aggregate is missing). A mechanical affordance
drain — the flag exists, no automation calls it.

**MALFORMED.** nc's opt-out docstring, justified on a 17x-low count. `map_diff`'s coverage
percentage, counting `memory/` records (F4). `reuse_lookup`'s confident shortlist over zero symbols,
with the disclaimer below it. Four dead globs at incms. `selftest.py`'s hardcoded lexicon path and
`tools/` prefix (F3).

**DUPLICATED.** `RECALL_DARK_LAYERS` vs what `SYMBOL_EXTRACTORS` actually covers — two answers, one
hand-typed, cross-checked by nothing, and incms's is demonstrably false. `.claude/hooks/*` vs
`tools/hooks/*`, three byte-identical pairs. `ROOT/"tools"` in gov's project-owned
`map_extractors.py`, which every adopter template copy inherits.

---

## 4. Cross-cutting recommendations, by value over effort

**1. Make every kit prefix-free, and prove it with a fixture.** (hours; fixes B1, F3, and the class)
Derive paths from `$0`, never a literal; add one selftest arm per kit that runs from a non-`tools/`
install. Twenty-plus versions shipped with B1 because no selftest ever left the gov shape.

**2. One announce-off helper per kit.** (hours; fixes M1, M4, M6, M11, half of M3)
Blank cutoff → `NOT ARMED`. Empty glob set → `DEAD PROBE`. Empty symbol tier → red. Zero records in
a declared family → warn. Four kits carry §7's "a skip must announce itself" in their own headers
and four kits break it. This is the single highest-value change in the report.

**3. Close every ratchet in both directions.** (three one-line edits)
lexicon `<` arm (M8); codebase-map baseline-growth assert; memory-tree `--bump` on the slot
high-water. A ratchet that only ever loosens is a changelog.

**4. Grade the artifact the user reads, not the one that is easy to enumerate.** (days)
Recall floor over the fused list at the CLI's own k (M5). codebase-map coverage over source files,
reported by the gate (M4). lexicon P1 over callable, non-test definitions (B3). Each of these is the
difference between a gate and a ritual.

**5. Derive every declared population from the machine.** (days)
Fixture families from the conf (B2). Dark layers from `symbols.json` (M11). Kit file manifests
asserted at the target in both directions — that alone catches incms's missing `kit.toml` and nc's
missing `SKILL.template.md`. Enforce the kit's own existing rule: *every PIN, FLOOR, CEILING and
CUTOFF is MEASURED at adoption and written by the adopt script, never inherited* — and where a pin
cannot be measured (nc has zero symbols), the adopter must refuse and say so rather than default.

**6. Fix the distribution model.** (a week, and the only structural fix here)
Four repos, four prefixes, three forks, no version verification, no upgrade path, no feedback loop.
Three pieces, in order of value:
   - **`verify-install`.** One command per kit — or one in `govkit` — that, run in an adopter,
     prints: kit version installed vs upstream, files declared by `kit.toml` and missing at the
     target, files present and byte-divergent from upstream (nc's 116-line fork would have shown up
     the day it was made), and conf keys the engine no longer reads. This is B1's real fix, one
     level up: stop relying on a single leg to notice a fork.
   - **A conf-key contract.** The shell gate sources `.memory-tree.conf` wholesale and validates
     nothing outside the size caps. Declare the key set; report once per run any key that is
     neither known nor explicitly retired. `corpus_ids.py:52` already has the `RETIRED_KEYS`
     channel — extend it, and give the shell half the same treatment.
   - **An adopter feedback path.** swydee filed two kit defects in its own backlog. One was fixed
     upstream as a default with no check behind it; the other is still live at the shipped
     configuration; both rows are still OPEN downstream. incms filed ABL-bCandidLoupe-4 against
     codebase-map's affordance sentence and gov still ships the sentence. Tag such rows
     `kit:<name>` and give upstream one command that collects them across the fleet. Without this,
     every adopter re-discovers the same defects privately.

**7. Narrow or retire what is not earning.** (a day, mostly deletions)
   - lexicon P1 off the merge bar until B3 lands; keep the engine, `--brief` and canon.
   - codebase-map at nc: grow source dossiers or stop running it. Five greens over zero attributable
     files is worse than no gate.
   - memory-recall on swydee-scale corpora: keep it for build records, tell the operator to read
     `DECISIONS.md` whole.
   - `--survey`'s 87 KB: either bound it or make it emit a work list.

**8. Soften the two overclaims.** (two edits, one of which ships)
`AGENTS.md:204` **and `coding-governance-agents.template.md:132`** — "Retrieval over the decision
corpus beats grepping it" is unproven at the source (`verdict: UNDERPOWERED`, n=5 against a
threshold of 53) and the template is what every adopter inherits. `query.py --help` — add the word
"upstream". Neither costs anything; both are the "two answers to one question" class in the
documents that name it.

---

## 5. What the skeptics refuted or materially corrected

Calibration matters, so here is what did not survive.

- **REFUTED outright — the RECORD_SERVES_CUTOFF retirement (finding 6).** The finder claimed the key
  was retired from the engine without a retired-key notice. It was never in the upstream engine at
  all: it is an nc-local fork feature with an OPEN upstream adoption spec. Adding it to
  `RETIRED_KEYS` would announce the retirement of something that never shipped. The finding's second
  half — the shell gate silently ignores any conf key it does not read — survives as an independent
  gap and is folded into recommendation 6.
- **The codebase-map baseline erosion (finding 35) was a measurement artifact.** "11 new keys entered
  gov's baseline across 6 commits" came from `git log --follow`, which diffs non-adjacent snapshots
  across a branchy history. Re-measured against real parents: 3 additions, all in-place renames
  paired with a same-commit removal — including the one swap AGENTS.md documents. The flagship
  example (`22f3e12c` parking an entire new kit) is flatly wrong: that commit added nothing and
  removed seven keys. What survives: the shrink-only rule is stated in five places and enforced by
  none, with exactly one demonstrated violation fleet-wide.
- **Check 23 is not undocumented (finding 5).** The finder's own grep was case-sensitive and missed
  the `## Acceptance ledger` contract section present in both copies. The real gap is a missing
  catalog entry and a prose count. Severity dropped major → minor.
- **The unnumbered hygiene failure is not "checks 17–19" (finding 9).** Those three do number
  themselves; the unnumbered line comes from the front-matter parser's `Problem` abort, which runs
  before any of them. Different fix, same symptom. The claimed knock-on to the per-leg log
  convention was unsupported.
- **codebase-map does not misreport its own contract (findings 33/34).** The README states outright
  that path globs are digest-only and never gated. Both dropped blocker → major, and they share one
  mechanism rather than being independent defects. The residual defect — no liveness assertion on
  the path layer — is real and unchanged.
- **`reuse_lookup` does say which regime it is in (finding 38).** Line 2 of every run prints
  `corpus: 0 symbols`. The defect narrows to the plain-English notice sitting below the shortlist,
  and to the tool assembling a confident list from image filenames at all. nc's six queries return
  12 candidates, not 21 — three honestly return "no seam fits".
- **Duplicate map claims are visible (finding 44).** MAP.md renders every claimant on the key's own
  row. Only the aggregate count is missing.
- **`--drop-affordance-exempt` is not callerless (finding 42).** WIRE-INTO-PROJECT.md:319 prescribes
  it as a DoD step, and gov's own reviewers already found and graded this. What survives: no gate,
  hook or script invokes it, so the drain is human-remembered rather than the mechanical one the
  header promises.
- **`memory/guides/` strays are not entirely unwatched (finding 7).** Two of five are caught
  incidentally by codebase-map's inventory walk — in any repo that carries that kit, which swydee
  does not. And the gate's own header does declare the three opaque subtrees.
- **The build-README exemption is honest (finding 11).** `exempt-pin` is an equality in both
  directions, not a ceiling; every exempt row carries a drain condition; a named converter owns it;
  21 of 88 are already converted. And AGENTS.md does not point sessions at that leg. What survives
  is the ratio and the 87 KB survey.
- **Counting corrections that did not change a verdict:** 72 specs red under the shipped
  `FORK_MARK_CUTOFF`, not 73. Six disarmed rules, not seven (`TOMBSTONE_ROOTS` blank is a legitimate
  empty population). 24% of lexicon offenders carry a leading underscore, not 45% — 208 is the union
  of three predicates, and the title said so correctly. gov's dark-language demo lands at 8.0%
  coverage, not the 5.2% quoted from a different fixture. nc's symbol count was 17x low when
  written, 28x low today. swydee's scaffolded lexicon pin is 185/261, not 195/306 — the quoted
  figures had git-added the kit itself.
- **One finding got stronger under scrutiny (finding 21).** `spine` extracting to zero is not a
  layout mismatch — upstream's regex is flat-correct and yields 2,348 durable-home ids on its own
  tree. The gov fork's "generalisation" inserted a directory segment that never existed, and the
  proposed fix would still have missed the backlog shards.
- **Two claims remain unverified rather than confirmed.** codebase-map's linked-worktree portability
  arm rests on the kit's own selftest — neither the finder nor the skeptic could exercise it on
  Windows. And several of memory-recall's supporting A/B measurements (the 10-question terms-vs-
  no-terms runs, the 11,750 B mean) use question sets that were not supplied; the reproducible
  single-query figure is 1.3× `DECISIONS.md`, not 1.5×.
