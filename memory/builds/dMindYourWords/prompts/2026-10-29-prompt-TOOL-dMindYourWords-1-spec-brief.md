**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17

# Spec brief — dMindYourWords, the seventeen lexicon units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dMindYourWords/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dMindYourWords/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds ask TOOL-dMindYourWords-18, which the LAST unit in build order (unit 17)
   names in its header's `closes`; every other unit's header says `advances TOOL-dMindYourWords-18`.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each is a new
   or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md` (units 1-6),
   `-7-reuse-scout-b.md` (7-10), `-11-reuse-scout-c.md` (11, 12, 13, 16) and `-14-reuse-scout-d.md` (14, 15, 17). Each holds a seam row per clause with path:line
   at `f27c63819`, and a section on where a record and source disagree. Those disagreements are findings you act on.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below). The PRIMARY one is
the lexicon kit review `B/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`: `[classes]` :210-234, `[forced]` :236-286,
`[packs]` :288-326, `[enforcement]` :328-353, `[drift]` :355-388, `[vocabulary]` :390-419, `[integration]` :421-452,
`[fixes]` :454-467, the forks L-1 to L-6 and their settled table :515-605, and `[debt-fold]` :607-674 (LX-1 to LX-3,
and the class each defect carries). Then architecture v2 `B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
(grep your clause id; `[policies]` :1202-1206; `[owed]` :2000), the four `B/*research-lexicon-*.md` records, the gap
register `B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line),
the night pass `B/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` (unit 17), and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 36-61 and 900-946. You never edit an instrument, v2,
the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-<n>.md`; H1
  `# TOOL-dMindYourWords-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order <k> ·
  advances TOOL-dMindYourWords-18`, with `<k>` your unit's order below (unit 17 writes `closes TOOL-dMindYourWords-18`
  in place of `advances`). `OPEN` is the status token: `DRAFT` is not in `STATUS_TOKENS`
  (`tools/memory-tree/tree_lib.py`). The shape is `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-1.md`
  line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each node the owned-node table gives your unit,
  `**Carries:** node:<node>`. A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part
  is carried by a spec of this build: never split a clause without saying so in your return.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 3, 4, 5, 14, 16, 17) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. A policy key's non-default value is seen by a planted
  `.governance/policy.toml` naming that value, read through I7; each allowed value of a key your unit owns is a
  planted case.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `f27c63819`: verify each line number before citing it. Record each
  candidate you rejected and the test that rejected it (M12), under `### Alternatives rejected`.
- §8 forks: settle each by the README's rungs (the execution plan lines 36-61 and 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`, ON THE SAME LINE as the ruling; a `relaxes:` value joins
  a record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a
  choice the README's `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave
  an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md`, `memory/HYGIENE.md` and
  `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their `.template.js`,
  `tools/gate-legs.json` from the kits' `[[gate_leg]]` declarations, the installed Skills under `.claude/skills/`
  from each kit's `SKILL.template.md`, and the installed kickoff skill from `skills/session-kickoff/`: name the source
  as the edit and the render as its copy.
- A parent's surface is specced and NOT built (next section). Cite the parent's spec by id and section as the
  interface and name the call you make; never re-spec it, never add a copy of it. Where your unit cannot run until it
  lands, say so in §2 as a build-run precondition, and where the clause names a stand-in, spec the stand-in and
  register it as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- Each policy key this build owns already has its catalogue row in `tools/policy/catalogue.toml` (`:387-416`, owner
  dMindYourWords) and its name in `tools/policy/unsummarised-keys.txt` (`:103-107`): the owner unit fills the row's
  missing summary and drains its name from that file, and never adds a second row. Its allowed values and default are
  that row's, verbatim. Once every unit of this build is terminal, the policy kit's reader-coverage arm reds any of the
  five keys no literal call reads, so the owner unit of each key names that literal reader in its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build, its accept line, and your return names it. The main
  loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dMindYourWords/spec/` and `memory/builds/dMindYourWords/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python gen_pack.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare;
  add an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over
  the tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use
  one only where you mean it. Units 1, 11, 14 and 17 retire named things; scout C's disagreement 2 lists `ratified`'s
  by-value readers, which are NOT the ones the clause names.
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it, and `widens:` and `relaxes:` on one
  line.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- **An acceptance criterion's ledger token** is written in backticks before the line first wraps (check 23).
- **Names you introduce** (a function, a module, a CLI mode, a conf block) are asked of the lexicon first:
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`. This build's own names are graded by the kit it
  changes; a spec proposing a name the gate refuses hands the builder a red.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dMindYourWords` after every writer returns.

## The parents are specced, not built

Every parent surface this build calls is specced and DEFERRED at HEAD; the scout records list each by spec id.
dTotalRecall: the `extract_code` block in `tools/lib/extract_code.py` and `read_defs_at(root, state, paths=None, …)`
(TOOL-dTotalRecall-13 S1-S5), `extract_ranges(src, ext)` with qualified name, enclosing class and bases as imported
(TOOL-dTotalRecall-8 S2-S3), `BUILTIN_ARMED` (TOOL-dTotalRecall-43 S15, S36), `record-kinds.toml` and
`record_kinds.py new` (TOOL-dTotalRecall-1 S1, S9). dOrderedCharter: `instructions_edit.py` and the `change` record
kind `<date>-build-<unit id>-change-<n>.md` (PLAY-dOrderedCharter-15 S1, S2, S4, S7, S9), the registered row kinds
`tools/playbook/kinds.toml` (PLAY-dOrderedCharter-7 S4, -35 S1, S10), the name-check point and `lexicon.py --tags`
with `--suggest <name> --as tag.<ns>` (PLAY-dOrderedCharter-10 S6, S7), `TAG_RE`, `parse_tag`, `read_namespaces` over
`tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19 S1, S2), the leg `pack` key (PLAY-dOrderedCharter-19 S12).
dWitnessedBar: the leg factory `tools/run-gates/leg_factory.py` and one `[[gate_leg]]` declaration per leg
(TOOL-dWitnessedBar-11 S1, S2, S8), the `tag` key (TOOL-dWitnessedBar-12 S1), the keyed ledger population factory
(`read_rows`, `compare_counts`, `compare_to_base`, `carry_renames`; TOOL-dWitnessedBar-13 §4, S5, S8), the pack-row
tag pattern (TOOL-dWitnessedBar-14 S2). dWellOiledMachine: the hook-pack fields (TOOL-dWellOiledMachine-10 S1) and the
refusal journal `git:pre-commit/<gate>` (TOOL-dWellOiledMachine-49 S3). dFurnishedOrders: the work order's slot
`render_slot(point, state, body)` (TOOL-dFurnishedOrders-4 S1). dLinkedLibrary: the `gov:note` resolver
`parse_note_line` and `check_resolve` (TOOL-dLinkedLibrary-4 S2, S7), and the `tools/lib` clause
`cl-dClosedLoop-0255`. Not an ancestor: dSafePassage's upgrade-step grammar (TOOL-dSafePassage-1 S1, S3), DEFERRED too.
None of those files exists at HEAD. Where your unit needs one of them and its build is not this build's ancestor, say
so in §8 and route it as the rungs say (a build-run precondition, an ask, or a stand-in), never by assuming it lands
first.

Landed and readable now: dTrueNorth's `tools/memory-tree/design_lib.py` and `tools/check-spec-tokens.py`; dGroundRules'
`tools/policy/` (`policy.py get`, `catalogue.toml`, `policy-mirror.js` `readPolicy`); `tools/lib/compare_base.py`
`resolve_compare_base`; the lexicon kit as it stands (`tools/lexicon/`), the drift audit (`tools/drift-audit/`),
`.githooks/pre-commit` and `tools/run-gates/`.

Where a scout found that a design record, a parent spec or source disagree, v2's clause governs; a parent spec it
contradicts gets an ask (the rule above), never an edit. Where the clause itself names something source shows wrong
(a reader that does not read, a hole of another name), the spec says what source shows, carries the clause's intent,
and writes a deviation record naming the difference.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.lexicon.pin` | 1 |
| `policy-key.lexicon.forced` | 2 |
| `policy-key.lexicon.packs` | 8 |
| `policy-key.lexicon.at-commit` | 9 |
| `policy-key.lexicon.drift` | 10 |
| `record-kind.lexicon-declaration` | 11 |

Every other unit owns no node; each still names the nodes it reads, in prose.

## Shared interfaces — one spelling for every writer

Fixed so seventeen specs by six writers agree on the interface axis (M2). Each row names its owner, the unit whose spec
defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed" has
no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says so in
its return and writes a deviation record rather than a second spelling. Every new name is asked of `--suggest` first.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The definition class | a new field `Offender.grade` taking `conforming`, `forced`, `out-of-scope`, `not-a-name`, `debt`; the existing `Offender.cls` stays the `debt`/`unruled` canon split inside `debt`, so "debt" never takes two meanings; only `grade == debt` counts against the pin (proposed) | 1 | scout A interface 1; lexicon review :212-218 |
| I2 | The forced source | `Offender.source`, one of `pack:<kit>:<row>`, `parent:<path>::<Class>`, `contract:<row tag>`, `suppressed:<path>::<name>`; one tally line after the P1 line, `lexicon: forced=<n> (pack=…, parent=…, contract=…, suppressed=…)` (proposed) | 2 | scout A interface 2; lexicon review :215, :228 |
| I3 | The site key | `<repo-relative path>::<name>`, and for a method `<path>::<Class>.<name>` (proposed) | 5 | TOOL-dScaffoldedMirror-4 S1; scout A interface 3 |
| I4 | The offender key and the debt ledger | the `render_offender_keys` key `<path>\t<rule>\t<identifier>` (`lexicon.py:3482`), rule values gaining `drift` and `noun` beside `verb`, `suffix`, `<cell>.conv`, `problem`; move-aware by mapping the path through `git diff -M`, never by dropping it; registered as the dWitnessedBar-13 population `lexicon-debt`, fields `path`, `rule`, `name`, `key = "site"`, `direction = "shrink-only"`, home `memory/project/lexicon-debt.txt`; `absorb` maps to the factory's widened disposition and `no-gate` to report-only (proposed) | 1 | scout A interface 4; scout B interface 6 |
| I5 | The definition context | an additive accessor beside TOOL-dTotalRecall-8's `extract_ranges(src, ext)`, keyed `(path, lineno, name)`, returning enclosing class, bases resolved through imports, decorators with aliases resolved, and the module's imports; never widening the frozen `(name, lineno)` pair `extract_text` returns (`lexicon.py:2532-2540`); `extract_decorators` becomes its adapter (proposed) | 12 | scout C interface 2; scout A interface 5 |
| I6 | The pack file, its grammar and its loader | `tools/lexicon/packs/<kit>.toml`; header keys `kit`, `versions` (a PEP 440 range), `generator` (the command, or `curated`), `families`; rows `[[member]] base, name` · `[[prefix]] base, prefix` · `[[host]] namespace, pattern` · `[[shim]] command`; one loader and validator `load_pack(path)` for shipped and custom packs, refusing a malformed pack whole and naming its row; the generator `tools/lexicon/gen_pack.py`; a forced-name pack is never tagged `pack.<kit>`, which names a leg pack (proposed) | 7 | scout B interfaces 1-2, disagreement 6 |
| I7 | The policy read | one lexicon helper `read_policy_value(key, root)` over `policy.py get <key>` by subprocess, key a string literal at every call site, because the kit imports no sibling kit (`check_self_containment`, `lexicon.py:2359`); keys and values verbatim from `catalogue.toml` (proposed) | 1 | scout A interface 7; scout B interface 7 |
| I8 | The conf blocks | `PACKS:` (unit 8), `FAMILIES:` and `NOUNS:` (unit 10), `OUT_OF_SCOPE:` (unit 15), each one `BLOCK_KEYS` row plus its row parser (`lexicon_conf.py:37`, `:401`); `PINS:`, `SUFFIX_OFFENDER_PIN` and `VERB_OFFENDER_PIN` fold into the one pin (unit 1); the repeated-header refusal in `load_conf` (unit 14) lands before any new block, its message `"{p}:{lineno}: duplicate block header {key!r}, first seen at line {n}"` mirroring `_parse_rows` (`lexicon_conf.py:198-200`); this repository's own conf carries the defect today (`.lexicon.conf:515` and `:579`), and unit 1's retirement of `PINS:` removes both | 14 | scout B interface 3, finding 4 |
| I9 | The noun canon | `canon.NOUNS`, a second tuple passed as `clusters=` to the existing `build_clusters`, `build_form_index` and `read_gloss`; no new canon function; the map inventory `lexicon-nouns` through one `_read_lexicon_block(block)` serving `lexicon-verbs` too (`map_extractors.py:246-275`) | 10 | scout B interfaces 4, 12 |
| I10 | The import census | a census over `scan_corpus`'s imports, top-level module to count, later fed by I5's imports (proposed) | 8 | scout B interface 5 |
| I11 | The vocabulary record and its reader | PLAY-dOrderedCharter-15 S7's `change` record, tag `unit.lexicon.<convention>` with `<convention>` one of `verbs`, `nouns`, `families`, `packs`, `contracts`, `suppressions`, `pins`, `cells`; one reader in `lexicon_conf.py` returning the latest record's date and path, with a CLI mode beside `--print-verbs` and `--print-rows` (`lexicon_conf.py:501-521`); every by-value reader of `ratified` moves to it (proposed) | 11 | scout C interfaces 3-4 |
| I12 | The forced-aware suggest | `--suggest <name> --as <cell> [--base <dotted.Base>]`, answered from committed pack data only so the no-corpus-pass contract (`lexicon.py:3727-3730`) holds; a generic name with no base gets the conditional answer (proposed) | 6 | scout A interface 8 |
| I13 | The work-order vocabulary slot | `render_slot("vocabulary", state, body)` (TOOL-dFurnishedOrders-4 S1): the verb rows with their negatives, the packs for the write set, and I12's answers for the names the spec declares (proposed) | 9 | scout B interface 10 |
| I14 | The commit arm | one `.githooks/pre-commit` block reading the staged set through `with_hook_index` (`.githooks/pre-commit:9-11`), grading through `read_defs_at(root, "index", paths)` with `read_defs_at_sha` over the index tree as the fallback until TOOL-dTotalRecall-13 lands, within `budget-ms=2000`; journal rule `git:pre-commit/lexicon`; hook-pack fields `owner=dMindYourWords`, `key=lexicon.at-commit` (TOOL-dWellOiledMachine-10 S1) (proposed) | 9 | scout B interfaces 9, 11, findings 1-3 |
| I15 | The lexicon leg pack | `pack = "lexicon"` on each `[[gate_leg]]` in `tools/lexicon/kit.toml`, tags `leg.lexicon.<name>`, registered through TOOL-dWitnessedBar-11's factory; the hand-written `tools/gate-legs.json` row is the fallback until it lands (proposed) | 16 | scout C interface 8; scout B row 9 |
| I16 | The signal names | keep `lexicon_verbs_declared_but_unused`; `lexicon_ratified_older_than_language_surface` becomes `lexicon_record_older_than_language_surface` (`drift_signals.py:290`, `:309`) (proposed) | 11 | scout C interface 9 |
| I17 | The path selector | a block `OUT_OF_SCOPE:` with rows `<glob>  <reason>`, parsed by `_parse_rows`, matched with stdlib `fnmatchcase` (the kit is copy-installed and imports no `map_lib`); one predicate `check_out_of_scope(rel, rows)` returning the reason or `None`, honoured in `scan_corpus` (`lexicon.py:2262-2321`), whose 4-tuple shape stays, an out-of-scope file yielded with no definitions plus a reason side-table; seed rows `memory/builds/**` and the planted fixture trees; an out-of-scope name takes `Offender.grade` `out-of-scope` and carries its row's reason as its source (proposed) | 15 | scout D interfaces 2-3; TOOL-aSurfacedLexicon-23 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 1 → 14, 15, 2, 3, 5, 9, 11 | `Offender.grade` |
| 14 → 15, 8, 10 | `load_conf` |
| 15 → 12, 9, 16 | `check_out_of_scope` |
| 12 → 2, 4, 8 | `extract_ranges` |
| 1 → 9 | `render_offender_keys` |
| 1 → 2, 5, 8, 9, 10 | `read_policy_value` |
| 11 → 3, 5, 16 | `read_vocabulary_record` |
| 5 → 2 | `load_waivers` |
| 7 → 2, 4, 6, 8, 10 | `load_pack` |
| 2 → 3, 4, 6 | `Offender.source` |
| 6 → 9, 13 | `--base` |
| 10 → 9, 13 | `canon.NOUNS` |

## The units

**Writer groups and build order.** The `order` value is the build order: the classes and the one debt pin first, because every
later unit grades into them and the kit's wording sweep must state the pin they define; the kit's own defects,
because the repeated-header refusal must stand before any unit adds a conf block; the path selector, which takes
records out of the graded population; the extraction primitive's definition context, which every forced-name reader
needs; the vocabulary write path, which the suppressions,
the contract table, the re-baseline and the leg pack all record through; the site suppression, the simplest forced
source; the packs, then base resolution over them, the contract table, the markers and the forced-aware `--suggest`;
pack selection; drift and the noun canon; enforcement, which compares everything above at commit and at the bar; the
leg pack; the tag-name check, which grades against the families and nouns; and the overloaded terms last, the only
unit that changes prose carriers. The harness splits the 17 orders into six writer groups of consecutive orders;
author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 1 (1), 14 (2), 15 (3) |
| 2 | 12 (4), 11 (5), 5 (6) |
| 3 | 7 (7), 2 (8), 3 (9) |
| 4 | 4 (10), 6 (11), 8 (12) |
| 5 | 10 (13), 9 (14), 16 (15) |
| 6 | 13 (16), 17 (17) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dMindYourWords-1** — Items 1 (gap-mem-10). I1, I4, I7. The five classes, only `debt` counted;
  `VERB_OFFENDER_PIN` becomes the debt pin, `SUFFIX_OFFENDER_PIN` folds in and the per-cell `PINS:` block retires
  (`**Readers:**`: `PIN_KEYS` `lexicon.py:121`, `:3054-3059`, `_parse_pins` `lexicon_conf.py:289`, `:462`,
  `scaffold_lexicon.py`, `kit.toml`'s `lexicon-pins` hole, the selftests); the pin moves from today's two-sided
  equality (`lexicon.py:3281-3293`) to `lexicon.pin`'s three values, each seen on a planted case; the pin held as
  dWitnessedBar-13's keyed population of offender names, never a count, with a fallback until that factory lands; the
  adopter upgrade step converting a pin, which needs dSafePassage's upgrade grammar (not an ancestor: route it by the
  rungs). The 11 `py.file` and 62 `py.constant` violations left outside records once unit 15
  re-arms both cells count against this one pin, never new `PINS:` rows (scout D interface 7). Seen red: a branch that fixes one offender and adds another, which today nets to zero.
- **TOOL-dMindYourWords-14** — Items 14 (gap-lex-07; ask TOOL-aProbedToolkit-5). I8, reads I1. Four defects, one
  batch unit: (a) the repeated-header refusal in `load_conf` (`lexicon_conf.py:139-157`), its arm beside the
  conf-refusal arms; (b) `@property` definitions take `Offender.grade` `not-a-name` through the decorator mark in the
  grader, the extractor untouched (TOOL-dTotalRecall-13 §3 makes changing an extractor's output its non-goal), and the
  IIFE fixed in the `js-regex` arrow pattern (`lexicon.py:146`), `parse_ts_defs` the reference rule (scout D, parent
  disagreement); the live population is the three `@property` sites scout D lists and no live IIFE remains, so the
  IIFE case is planted; (c) `--brief` and `--help` answered with exit 0, nothing documents them to remove, and
  `scaffold_lexicon.py`'s refusal of `--help` as a destination stays; (d) the two-sided pin wording retired in every
  carrier, from scout D's list at HEAD and never M17's drifted one, landing with or after unit 1's pin change, with
  the selftest arms AC10 and H2 rewritten once (H2 asserts the literal `"TWO-SIDED EQUALITY"`), and the Skill, conf
  and README reconciled (`SKILL.template.md:10-11` says "or the gate refuses it" while the pin absorbs the name).
  Seen red: a planted conf with a repeated block header, a planted IIFE value and `@property`, and each dead mode.
- **TOOL-dMindYourWords-15** — Items 15 (gap-lex-04; ask TOOL-aSurfacedLexicon-23). I17, reads I1. No `CELLS`
  selector fits (`SELECTOR_KINDS` is name-based, `_SEL_LIT_RE` forbids `/`): the exclusion lives in `scan_corpus`, so
  it also leaves the undeclared-extension census and the scaffold walks; the same decision for `read_defs_at_sha` and
  `--merge-losses`. `py.file` and `py.constant` re-armed once records are out (measured at HEAD: 62 and 251
  violations, 11 and 62 outside records, which join unit 1's pin); the stale `.lexicon.conf:556` claim and the ARMED
  figure the selftest reads corrected; the two legs' `doc_reads` on `memory/builds/` (`tools/gate-legs.json:1476`,
  `:1502`, through their kit declarations) dropped or re-justified; the `html` and `svg` dark rows L-6 added
  re-justified, since they exist only for records. Seen red: a planted record-shaped offender under `memory/builds/`
  graded before and out of scope after, and a planted fixture tree the same.
- **TOOL-dMindYourWords-12** — Items 12 (LX-2). I5. TOOL-dTotalRecall-13 builds the primitive and moves the
  tokenizers out of `lexicon.py`; this unit owns only the definition context its §3 hands to dMindYourWords
  (decorators with aliases resolved, bases resolved through imports, the module's imports for the census), extending
  `extract_ranges` rather than adding a third walk, and the lexicon calling the primitive over the working tree, the
  index or a revision so neither kit requires the other. Precondition: TOOL-dTotalRecall-13 and -8 land first; say what
  the lexicon reads until then. Seen red: a planted `from typing import override as ov` read as `override`, and a
  planted base imported under an alias resolved to its dotted name.
- **TOOL-dMindYourWords-11** — Items 11 (gap-lex-06). I11, I16. Fork in §8: how a vocabulary change reaches
  `.lexicon.conf` at all, since `instructions_edit.py` writes manifest rows and its S4 refuses every write until
  dDeclaredLoop's guard lands (scout C disagreement 6; scout A disagreement 7 offers a registered row kind or the
  files kept plus a check refusing a change with no `change` record). Then: `ratified` replaced by the record, and
  every by-value reader moved, which are `drift_report.py:1215`, `:1334-1338`, `adopt-lexicon.sh:430-431`, the
  `lexicon-ratified` hole `kit.toml:177-183` (the clause says `lexicon-pins`: scout C disagreement 1) and the writer
  `scaffold_lexicon.py:319`, not `lexicon.py` or `lexicon_conf.py` (disagreement 2); the signal widened from LANGS
  alone to VERBS and LANGS edits (disagreement 3); a commit that raises the pin or un-arms a cell with no record refused,
  probed by staging a pin raise in a scratch clone; the re-baseline (lexicon review :404-408), probed by removing the
  `init` row on a fixture and seeing one record carry the delta; the `init` row re-justified or removed with the
  dossier claim `memory/map/features/lexicon.md:36` in the same commit. Seen red: a planted LANGS change newer than
  the record (`tools/drift-audit/selftest.py:1074-1095` is today's fixture).
- **TOOL-dMindYourWords-5** — Items 5. I3, I11. `load_waivers` (`lexicon.py:2324-2337`) re-keyed to I3 with a
  mandatory reason (TOOL-dScaffoldedMirror-4 S1-S3, whose line numbers and "three registries" are stale: scout A
  disagreement 2), changed only through the write path, refused with no provenance record, counted and printed, never
  the default; the owner item's three outcomes for a refused uncovered forced name (suppress, add a custom pack row,
  rename) and the unattended run's rename-or-park under `refuse`. Seen red: a suppression with no reason, and one with
  no provenance record.
- **TOOL-dMindYourWords-7** — Items 7 (`[owed]` v2:2000). I6. The pack store, its header, its load-time validation and
  `gen_pack.py`'s four generators (`inspect` keyed on a declared Python version and per platform tag where a module
  differs, the wheel's syntax tree, pluggy hookspecs, `.d.ts`), shell hosts and shims curated; the first wave shipped,
  the second wave specced as waiting on an adopter census, never built here. Packs are not `[[generated]]` rows
  (scout B row 7). Seen red: each first-wave pack on a planted fixture with one forced site per row kind and one free
  module function of the same name (the arm clears the forced sites and grades the free one), a malformed pack refused
  whole naming its row, and the stdlib pack's 3.12-against-3.14 byte-identity run as a `New arm:` where a second
  interpreter is needed.
- **TOOL-dMindYourWords-2** — Items 2 (gap-lex-01). I2, reads I5, I6. The forced check before the debt split in
  `measure_pass` (`lexicon.py:2941-2965`); member and prefix rows only where the enclosing class resolves statically
  through its imports to that base; host rows by namespace pattern; no live import (lexicon review :275-277); dunders
  graded on their stripped verb today (`subtokens.py:39`). `lexicon.forced`'s three values, each seen; `by-name`
  printing its measured false-exemption rate. Seen red: the three cases, each with its fixture (an unresolved base
  graded debt and reported unresolved; an override of a repository parent forced by that parent and falling with its
  rename; a marker on a repository base or an unpacked base reported, not red).
- **TOOL-dMindYourWords-3** — Items 3 (LX-3). Reads I2, I11. The table, its home (a registered row kind, scout A
  disagreement 7 option a), the `gov:` pointer resolved through TOOL-dLinkedLibrary-4, and the stale arm that runs a
  row's own match rule over its reader's source. The `boundedParallel` reader the records cite in `agent-cap.js` does
  not exist (scout A disagreement 1): name readers whose rule actually matches, and say what forces `boundedParallel`.
  Seen red: a planted row whose reader stopped matching.
- **TOOL-dMindYourWords-4** — Items 4. Reads I2, I5, I6. A marker on a repository base confirmed when that base
  defines the member; on an outside base honoured where a pack confirms it; only a marker with no defining base reds
  (PEP 698); TypeScript's `override` reports until the second wave. The corpus holds 0 `@override` (scout A row 4), so
  planted fixtures are the population, and one must be a marker that fails. Seen red: a planted `@override` on a
  method its base does not define.
- **TOOL-dMindYourWords-6** — Items 6 (gap-lex-02). I12, reads I2, I6. The forced check before the debt lookup in
  `run_suggest` (`lexicon.py:3857-3876`) so no forced name is renamed; `--base` in `main`'s positional parser
  (`:4396-4405`); the conditional answer for a generic name. Seen red: gap-lex-02's five renames (`do_GET`, `emit`,
  `handle`, `get_queryset`, `setUp`), each answered as forced with its base given.
- **TOOL-dMindYourWords-8** — Items 8 (L-5). I8, I10, reads I6. The census over `scan_corpus`, a manifest reader
  (`pyproject.toml`, `requirements.txt`, `package.json`, `composer.json`; none exists in the kit), `PACKS:` for the
  owner's declaration and custom packs, `lexicon.packs`' four values each seen, and the four uncovered-input states
  (lexicon review :322-326), each a planted case.
- **TOOL-dMindYourWords-10** — Items 10 (gap-lex-05, LX-1). I8, I9. Families declared by packs and by `FAMILIES:`,
  never inferred; one verb per declared family per object, the object the subtokens after the verb under the noun
  canon; the established verb the earliest-landed definition's; ties and existing splits reported, not refused; a
  forced name never establishes a verb. The split table (lexicon review :377-381) across `lexicon.at-commit` and
  `lexicon.drift`, each cell a planted case; `lexicon.drift`'s three values each seen. `sha`/`oid`/`hash`/`digest` as
  a noun cluster.
- **TOOL-dMindYourWords-9** — Items 9 (gap-lex-03, L-2). I13, I14, reads I4, I12. Four parts: the work-order slot;
  the commit arm under 2 s (a full `--offenders` pass took 6.25 s, scout B finding 3), moves by `git diff --cached
  -M` and a `git mv` fixture committing clean, merges left to the bar; the bar's by-name comparison as a binding arm
  on every bar from the merge base with the default tip, never the report-only `GATE_ATTRIBUTE` block; the replay of
  the merges since 2026-08-16 with 0 move reds (state which population: 577 reachable, 269 first-parent). No parent
  renders a pack into `.githooks/pre-commit` (scout B finding 1): add the block by hand and file the ask for
  dWellOiledMachine. `lexicon.at-commit`'s three values each seen. Seen red: path-only keys on a planted move.
- **TOOL-dMindYourWords-16** — Items 16 (gap-lex-08). I15, reads I11, I16. The two signals move into the lexicon kit
  as its leg pack, absent from the legs manifest where the lexicon is not installed, and drift-audit stops importing
  the kit for them. Fork in §8: `build_lexicon_marginal_offense_rate` (`drift_report.py:1437`) imports the kit too
  (scout C disagreement 4). Seen red: the planted LANGS change newer than the record, now on the pack's own arm.
- **TOOL-dMindYourWords-13** — Items 13 (gap-lex-10). Reads I9, I12. PLAY-dOrderedCharter-10 S7 already specs
  `--tags`, `--as tag.<ns>`, the first-segment refusal and the registry read (scout C disagreement 5): call them, never
  re-spec them; this unit adds the grading of a tag's verbs against the declared families and its nouns against the
  noun canon, and the refusal of a namespace word declared in `.lexicon.conf`. Its three seen-red cases are the
  clause's.
- **TOOL-dMindYourWords-17** — Items 17 (gap-lex-09; `closes TOOL-dMindYourWords-18`). No lexicon code seam: these
  are prose terms. The settled home is PLAY-dOrderedCharter-20 S2's one-fact check over `definition` units, written
  through PLAY-dOrderedCharter-15; neither is built, so until then the unit edits each carrier's source and its render.
  Attendance is a mode and the session binding says "owner" (`night-pass.md:79-81`, `:88`, `:113-114`); "baseline"
  keeps retrofit's meaning and an experiment's probe record is the "measured reference" (`:181-182`); "playbook" is
  decided by no record (scout D): settle it in §8 by the rungs, never park it, and record the ruling. The carriers are
  scout D's list at HEAD, including the persisted value `landed-by attended` (`unattended.sh:7311` and its readers),
  which a rename migrates by value with a `**Readers:**` clause, and the fourth and fifth senses of "baseline" scout D
  found. Terms other builds own as carried nodes (`policy-key.runtime.attended-judge`, `-allowance`,
  `record-kind.baseline`, `record-kind.attendance-override`) are renamed only by that build's deviation: file the ask.
  Seen red: a planted second definition of one settled term, through the one-fact check where built, else a grep arm
  the unit names.
