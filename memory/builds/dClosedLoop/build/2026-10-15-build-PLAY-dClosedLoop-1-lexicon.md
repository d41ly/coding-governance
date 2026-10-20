# Kit review: the lexicon

**Serves:** research PLAY-dClosedLoop-1

The owner asked for a full review of the lexicon kit under the new architecture, with an upgrade and
its own codebase integration. The review follows the memory round
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`), which set `lexicon.pin` to
`shrink-only` and recorded `gap-mem-10` against dTotalRecall.

Three researchers measure the kit in parallel: dispatches 27 to 29. Their returns are saved verbatim
beside this record, and the design is written here once they return.

## [words] The owner's words, 2026-10-15

> Lexicon needs a full review under the new architecture and an upgrade and codebase integration of
> its own: currently, agentic sessions keep raising its offender pin as a default mechanism for verbs
> that are not actually 'debt' - they are built-in verbs from the 3rd party kits and changing them is
> innately impossible. The kit has to account for that by default and provide agents a clear
> mechanism with how to exclude these verbs from debt and perhaps pre-built tables of verbs per
> popular kits. Additionally, the mechanism of enforcing naming conventions should be reviewed and
> improved where possible. The goal of the Lexicon kit is to ensure that conventions and names are
> consistent and don't drift.

## [settled] What the design already fixes

- **Layers.** The lexicon belongs to the Knowledge expansion (layers round one). The core never depends
  on it (P28).
- **The pin** (memory round, F4-8):
  - `lexicon.pin` defaults to `shrink-only`.
  - `absorb` is allowed, and `velocity` uses it.
  - `no-gate` is allowed.
- **dTotalRecall owns the lexicon's work**, with `gap-mem-10`: the gate absorbs debt, its pin rising
  from 412 to 1,087 with one real drain in 60 days.
- **Point-of-use delivery** (P29). A builder's work order hands it what its item needs, keyed. The
  memory round names `--suggest` as the answer handed for new names.
- **The codebase map** reads definitions with the lexicon kit's own tokenizers
  (`map_extractors.py:306`), and the map is planned to grow callers and complete Python definitions.
- **The annotation grammar** (F4-2):
  - `gov:note` is voluntary.
  - `gov:feature` anchors are required wherever a reuse entry points.
  - The `gov:` marker family is already read by four gates.
- **What dispatch 25 measured:**
  - `.lexicon.conf` is 46,577 B. It holds 23 verb rows, 4 cells, 1 pin, the banned suffixes and the
    languages.
  - Two waiver files exist, of 8 lines each.
  - Agents ran the kit 1,305 times bare and 542 times with `--suggest` in 60 days.
  - The drift audit read `lexicon_marginal_offense_rate` at 584 of 4,948.
- **Revised: 2026-10-17, the debt round.** Three lines above were overtaken:
  - L-4 moved the lexicon's work and `gap-mem-10` from dTotalRecall to dMindYourWords. `gap-mem-10`
    keeps its key, and its area becomes Lexicon;
  - KN-1 made the lexicon an optional component of memory's library side, which this record calls the
    Knowledge expansion;
  - the pin's history holds 11 drains (−107) and 19 raises (+814), not one drain (dispatch 28).

## [history] The builds that made the kit

- **dClosedLexicon** opened on 2026-08-16. Its README gives the kit's founding idea: a closed verb
  table, because "a verb you cannot pick is a responsibility you have not scoped". Three design
  choices followed:
  - a scaffold seed derived from the adopter's own corpus and then frozen;
  - vacuity armed twice;
  - the predicates shipped behind one opt-in kit.
- **aSurfacedLexicon** extended the kit. Two of its asks bear on this review:
  - `TOOL-aSurfacedLexicon-23` is the path-scoped selector. Two cells are un-armed for lack of it,
    because they graded `memory/builds/**` records.
  - `TOOL-aSurfacedLexicon-15` is the rename unit the pin was meant to fall with.

Neither build is live. Both are evidence; no chain build counts on them.

Revised: 2026-10-17, the debt round. dMindYourWords absorbs `TOOL-aSurfacedLexicon-23` and
`TOOL-aSurfacedLexicon-15`, and links or closes each row when it opens. This build changes no ask's
status.

## [research] Dispatched, 2026-10-15

| # | Part | Handoff |
|---|---|---|
| 27 | the kit as built and as enforced: mechanics, enforcement points, exceptions, how the vocabulary changes | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md` |
| 28 | the offender population and the pin's history: what is forced, what is debt, who raised the pin and why, naming drift | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md` |
| 29 | prior art and the forced-name mechanism: how naming checkers treat names nobody can change, generated vocabulary tables per kit, override detection prototyped on this tree | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md` |

### Returned, 2026-10-15

| # | Part | Return | Wall | Out |
|---|---|---|---|---|
| 27 | the kit as built and as enforced | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md` | 5m23s | 28.0k |
| 28 | the offender population and the pin's history | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | 7m43s | 38.9k |
| 29 | prior art and the forced-name mechanism | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-prior-art.md` | 8m15s | 38.8k |

Their probe files are kept in `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-instruments.md`.

## [now] Two reds to know about

- **This branch reds the lexicon's wiring leg.** The leg runs on every bar.
  - **Cause:** the three design-overview and layer-model records (`.html`, `.svg`) are the only tracked
    files with those extensions, and the kit refuses an undeclared extension.
  - **Origin:** the main loop committed them earlier in this session.
  - **The gate's own remedy:** declare both `dark` in `LANGS`. Asked as L-6.
- **Main carries a lexicon red of its own.** The count reads 1,088 against `VERB_OFFENDER_PIN="1087"`.
  - **Cause:** `8ddc0a482` (aOrientedCast-22, 2026-10-13) added `clean` at
    `tools/unattended/gate-guard.js:689` without moving the pin.
  - **Not this branch:** no code file changed here since the merge base, and no offender sits in this
    build's folder.
  - **Who meets it:** the next landing that runs the naming leg.
  - **Scope:** renaming the function is product code, outside this build's cut-line, and raising the
    pin is the habit this review exists to end.
- **Revised: 2026-10-17, the debt round.** Both reds are gone. L-6 declared `html` and `svg` dark in
  LANGS (`0ac38b016`), and the undeclared-extension refusal stays armed for every other extension. Main's
  red is gone since `ef9c3fbab`.

## [current] What the kit is and does, measured 2026-10-15

**How a name is judged** (dispatch 27):
- **The test:** a definition offends when its leading subtoken is missing from the 23-verb table. The
  canon then labels it DEBT (a rename exists) or UNRULED.
- **What it ignores:** nothing consults the definition's class, base, decorator or host. Underscores
  are stripped, so `__str__` grades as `str`.
- **The one binding check** is the number of offenders against the pin, at the bar. Nothing judges a
  name at commit or by name.
  - A fixed offender plus a new one nets to zero, and the engine's own docstring says so.
  - The count includes 43 offenders in frozen records under `memory/builds/`.
- **Exemptions:** waivers are keyed on a bare name across the whole corpus. Their reason is optional
  and nothing checks it. Pins and un-armed cells change by plain edit. `ratified` is a stamp checked
  only for being non-empty.
- **Defects:**
  - the conf reader keeps only the last of a repeated block header;
  - `--brief` and `--help` exit 2, though about 130 calls used them;
  - the Skill says the gate refuses a non-fitting name, while the gate absorbs it;
  - the conf and the waiver headers say "two-sided equality", while the README says "shrink-only".

**What the count is made of** (dispatch 28), all 1,088 offenders:

| Class | Count | Examples |
|---|---|---|
| (a) forced by a third party | 6 | four pytest hooks in `crashprobe.py`, `__str__`, a `mktemp` shim that shadows the command |
| (b) forced by gov's own published contract | 22 | `boundedParallel` and `chunk`, which `agent-cap.js` reads by name; the map extractor's entry points, which `gen_map.py` calls on an adopter's module |
| (c) real debt | 1,013 | 83 with a canon rename and 930 unruled. 443 sit in test files. 362 of the 515 distinct unruled tokens occur once |
| (d) false positives | 4 | an IIFE value; three `@property` definitions |
| (e) records | 43 | build records' scripts |

- **On gov's own tree, forced names are 28 of 1,088 (2.6%).** The population the owner describes,
  third-party verbs, lives in the adopters, which this review does not read.
- **Pin history:**
  - 19 raises (+814, of which 507 armed the shell cell);
  - 11 drains (−107);
  - 0 waivers, ever.

  Of the names absorbed over that history, 10 were forced (all gov's own contract), 35 were records,
  and the rest were real debt.
- **`--suggest` advises renames that break the code it is asked about:**
  - `do_GET` to `cmd_get` breaks `http.server` dispatch;
  - `emit` to `print` breaks `logging.Handler`;
  - `handle` to `run` breaks `socketserver`;
  - `setUp` to `set_up` silently stops unittest calling it;
  - `get_queryset` to `read_queryset` breaks a Django view.

  P29 hands `--suggest` answers to builders, so this would break an adopter's code by instruction.
- **Drift beyond verbs goes unseen:**
  - 57 objects carry two or more declared acquire-family verbs; `conf` alone is loaded 11 times, read
    3 times and parsed twice;
  - nouns vary freely: `sha` 13, `oid` 4, `hash` 4, `digest` 10; `dir` 101, `directory` 1,
    `folder` 2.

**How others solve forced names** (dispatch 29):
- **The checkers that never excuse a free choice resolve or verify the base:** pylint's
  overridden-method skip, TypeScript's `noImplicitOverride`, Checkstyle's `@Override`.
- **The ones that ship tables key them on names that are namespaced by convention:** ruff's
  `ignore-names` (in effect a unittest table), and revive's `Test*` and `Example*`.
- **A table keyed by name or by verb fails on this tree:**
  - a whole-stdlib name table exempts 53 sites, of which 1 is forced;
  - keyed by verb, it exempts 99 to 202 offenders, of which about 0 are forced.
- **What passes:** tables keyed by what forces the name (a base class's member, a base's prefix, a
  host's namespace), applied only where the site resolves to that base through its imports. On this
  tree they cover 5 of 5 third-party-forced names, exempt no free choice, and produce byte-identical
  output twice.
- **Table sizes:**

  | Source | Size |
  |---|---|
  | 35 commonly subclassed stdlib bases | 1,270 rows |
  | pytest's hook specifications | 52 |
  | Django | 342 rows over 14 bases |
  | Flask / Starlette / FastAPI | 92 / 24 / 59 |
  | React | 9 lifecycle names and 18 hooks |
  | Node events and Express | none: event names are strings, and handlers are anonymous |

  All were measured from wheels and `.d.ts` files without importing them.
- **Revised: 2026-10-17, the debt round.** Two readings above were overtaken:
  - the packs cover 5 of 6 third-party-forced names, not 5 of 5: the `mktemp` shell shim is in no pack,
    and `[packs]` adds shim rows. The byte-identical result came from a live import on one class site;
  - the README's "shrink-only" (its line 650) describes the waiver registry. Every carrier's pin text
    says two-sided equality, which the settled `shrink-only` retires (`[fixes]`).

## [fit] The owner's points against the design

| The owner's point | Today | This round's answer |
|---|---|---|
| Sessions raise the pin for third-party verbs that are not debt | no forced class: 19 raises, 0 waivers | every definition gets one class, and only debt counts (`[classes]`) |
| Exclude them by default, with a clear mechanism | a text waiver keyed corpus-wide, never used | forced names resolved to the base or host that forces them, with no agent action (`[forced]`) |
| Pre-built tables per popular kit | none | generated packs keyed by base, prefix or host, never by verb (`[packs]`) |
| Review and improve enforcement | a corpus count at the bar | supply in the work order, a check at commit, a name-by-name comparison at the bar, the pin as backstop (`[enforcement]`) |
| Consistent names that do not drift | verbs only | one verb per object family, and a noun canon (`[drift]`) |
| Its own upgrade and codebase integration | the map borrows the lexicon's tokenizers | one extraction in the map, one classification in the lexicon (`[integration]`) |

## [design] The lexicon, as proposed

Revised: 2026-10-17, the debt round's fold. Its subsections are amended in place, and `[debt-fold]` names
where each defect's fix sits.

### [classes] Every definition gets exactly one class

| Class | Means | Counts against the pin? |
|---|---|---|
| conforming | its verb is declared and its case matches its cell; it keeps its object's established verb inside a declared family (`[drift]`), and its nouns are canon | no |
| forced | a name the code cannot choose, with a verified source (`[forced]`) | no; reported in its own tally |
| out of scope | a record under `memory/builds/**`, or a file in a planted fixture tree, found by the path selector (`TOOL-aSurfacedLexicon-23`, which dMindYourWords absorbs). Test files stay graded | no; not graded |
| not a name | an IIFE value or a `@property`, fixed in the extractor | no |
| debt | everything else: a drift or noun-canon split and a banned suffix included | yes |

- **The pin counts debt only.** Under `lexicon.pin: shrink-only`, the default, it only falls. Under
  `absorb`, a raise moves only the backstop count and is recorded with its cause; the bar's by-name
  comparison still refuses what a branch adds. `no-gate` reports both and refuses neither.
- **One pin over today's three seams.** `VERB_OFFENDER_PIN` becomes the debt pin. `SUFFIX_OFFENDER_PIN`
  folds into it, since a banned suffix is debt. The per-cell `PINS:` block retires, its cells counted
  inside the one pin. F4-8's shrink-only supersedes `TOOL-aSurfacedLexicon-18`.
- **A drift or noun split is debt.** A new split is refused as L-3 settled (`[drift]`). The existing
  splits join the pin once, through `[vocabulary]`'s re-baseline, with the delta and its cause recorded.
- **Each forced or out-of-scope name carries its source,** so the lexicon has no reasonless exemption
  left.
- **On this tree the pin falls by 28 forced names,** 22 contract-forced, 5 host-forced and the `mktemp`
  shim through `[packs]`' shim rows, and by 43 out-of-scope names and 4 false positives, once the
  classes land. The splits then raise it once, by the count the re-baseline records.
- **Two cells re-arm.** `py.file` and `py.constant`, declared off for want of the selector, re-arm once
  it excludes `memory/builds/**`.

### [forced] How a forced name is recognised, with no agent action

1. **Host-forced names come from packs** keyed by what forces the name:
   - a base class's member, such as `logging.Handler.emit`;
   - a base's prefix, such as `ast.NodeVisitor` with `visit_*` or `http.server.BaseHTTPRequestHandler`
     with `do_*`;
   - a host's namespace or closed set, such as pytest's hook specifications or Python's data-model
     dunders.

   A generic name (`emit`, `handle`, `run`, `do_*`) is forced only where its enclosing class resolves,
   statically and through its imports, to the base that defines it. A namespaced closed set applies by
   name, and its rows carry a namespace pattern the pack grammar accepts (`pytest_*`, `__*__`). The same
   `emit` stays debt in a module function, or on a class with no outside base. Three cases have their
   own outcome, each with a fixture:
   - **an unresolved base** grades as debt, reported as unresolved;
   - **an override of a parent defined in the repository** is forced by that parent, and falls with the
     parent's rename;
   - **a marker on a base defined in the repository, or on an unpacked base,** reports rather than reds.

   Context comes per language. Python's comes from its syntax tree. JavaScript and TypeScript need a
   parser that yields class membership, `extends` and import resolution, which the shared extraction
   primitive owes in its second wave (`[integration]`). Until it lands, JavaScript and TypeScript
   forced names are out of the first wave, and an `override` there reports rather than reds.
2. **Contract-forced names are declared in a table the instruction write path owns**
   (LX-3). Each row names the reader, the name and the match rule the reader applies, such as
   `agent-cap.js`'s regular expressions over `boundedParallel` and `chunk`. The code carries at most a
   `gov:` pointer to its row, which a check resolves. A stale arm reds a row once the reader stops
   matching: the check runs the row's own match rule over the reader's source.
3. **Markers are a fast path, never a pass.** A marker whose base is defined in the repository is
   confirmed when that base defines the member, and the name takes the base's class. A marker on an
   outside base (`@typing.override`, TypeScript's `override`, `hookimpl`) is honoured where a pack
   confirms the base. Only a marker with no defining base reds, as PEP 698 rules.
4. **A site suppression with a reason is the owner's fallback** for a host no pack covers. It extends
   today's waiver files and `load_waivers` under the `path::name` key that `TOOL-dScaffoldedMirror-4`
   designs, with a mandatory reason (`TOOL-aLoosenedCeiling-5`). It changes only through
   `instructions.edit`, and the check refuses a suppression with no provenance record. It is counted
   and printed, never the default. A commit refused on an uncovered forced name goes to an owner item
   with three outcomes: suppress the site, add a custom pack row, or rename. An unattended run under
   `refuse` renames or parks the unit.
5. **No live import.** Resolution runs against committed pack data, so every node grades the same. A
   live import depends on each node's packages and user site: on this node, pytest imports under one
   interpreter and not the other.

- **`lexicon.forced`'s other values route too.** `by-name` applies the same packs without base
  resolution: a member name is exempted wherever it appears, printed with its measured false-exemption
  rate (53 sites for 1 forced on this tree), and witnessed by the forced tally. `by-annotation` is
  item 4's site suppression, each site annotated with its reason.
- **`--suggest` becomes forced-aware.** It takes the site's base or host (`--base logging.Handler`), or
  reads the site from the extraction. It never proposes renaming a forced name. For a generic name with
  no base given, its answer is conditional: forced if the class derives from the named base, otherwise
  the rename. The work order hands it the base the spec declares.

### [packs] The pre-built tables, as packs

- **One pack per host kit, generated where possible:**
  - `inspect` for the stdlib, keyed on a declared Python version: `requires-python`, or a repository
    declaration changed through `instructions.edit`, never the running interpreter. Failing both, the
    union across the declared minor range. A module that differs by platform is generated per platform
    tag;
  - the wheel's syntax tree for pip kits, never an import;
  - pluggy's hook specifications for pytest;
  - `.d.ts` declarations for JavaScript kits.

  Shell hosts are curated: bats, bash's and zsh's hook functions (about 8 names), and command shims.
  A shim row is a closed set of external commands a shell function may shadow, applied only where the
  function's name equals a command it also invokes, as the `mktemp` shim does.
- **Each pack carries a header:** the kit, its version range, the generator command that rebuilds it,
  and the verb families it declares for its kit (`[drift]`).
- **Every pack is validated at load:** its header, its grammar, duplicate rows, and bare generic tokens
  in a by-name set. A malformed pack is refused whole, with its offending row named, and a custom
  pack the same way.
- **First wave:**
  - the Python data model;
  - the commonly subclassed stdlib bases;
  - unittest, pytest, argparse, `ast`, `http.server`, `logging`, `json` and `cmd`;
  - the shell hosts and shims.
- **Its acceptance.** Each first-wave pack is proven on a planted fixture with one forced site per row
  kind (member, prefix, host set) and one free module function of the same name: the arm clears the
  forced sites and grades the free one. The stdlib pack adds a cross-node byte-identity run, 3.12
  against 3.14. The research's "5 of 5, byte-identical" was a prototype's result, measured with a live
  import on one class site.
- **Second wave:** Django, Flask, Starlette and FastAPI, and React's lifecycle and hooks. Each ships
  after a census in an adopter shows its names actually offend. Node's core events and Express need
  no pack.
- **Selection** is detected and declared, with custom packs (L-5). The stack is detected from the import
  census the extraction makes, with manifests (`pyproject.toml`, `requirements.txt`, `package.json`,
  `composer.json`) supplying versions where they exist. Inputs no pack covers have their own states:
  - a kit with no pack is reported as uncovered, and its names route as `[forced]` item 4;
  - a version outside every pack's range takes the nearest range below and reports the gap;
  - no manifest selects by the import census alone, its versions unknown;
  - several minors take the union across them.

### [enforcement] Where a name is judged

1. **Supply, at the point of naming.** The builder's work order hands it (P29):
   - the verb rows with their negatives;
   - the packs that apply to its write set;
   - forced-aware `--suggest` answers for the names its spec declares.
2. **At commit.** The definitions a commit adds or renames, in its staged files, are graded. The check
   is a Runtime hook pack rendered into `.githooks/pre-commit`'s staged-arm sequence, within 2 s per
   commit. A bypass is journaled, and the bar's comparison catches what it skipped. The check keys
   against HEAD's definitions with rename detection (`git diff --cached -M`): a staged definition whose
   name stands as debt in HEAD, at a path the commit deletes or removes that definition from, is a move,
   not an addition. A fixture in which a `git mv` of a file holding an offender commits clean is its
   acceptance. Merge commits are left to the bar, because their diff carries the other parent's names.
   L-2 settled `refuse`.
3. **At the bar, by name.** The branch's offender set is compared with its base's, and the bar reds on
   any offender the branch adds. This is a new binding arm on every bar, not the report-only
   attribution block, which runs only on a red leg under `GATE_ATTRIBUTE`. Its base is the current
   default tip, read as a three-dot diff from the merge base, never a frozen branch point. Remote CI runs
   the same arm against the remote's default tip. The keys are move-aware. The build first replays the
   merges since 2026-08-16 with the shipped keys, and the replay must show 0 reds attributable to a moved
   or renamed file. It is seen red with path-only keys on a planted move.
4. **The count stays as the backstop:** the debt-only pin, over today's three seams (`[classes]`).
5. **The Loop Review reads the trends:** debt, the forced tally, and drift.
6. **The lexicon's leg pack.** The naming comparison, the pin backstop, the wiring, the selftest and the
   two drift signals form the lexicon's leg pack at Test's leg-pack point (`gap-lex-08`). The pack is
   absent from the legs manifest where the lexicon is not installed.

### [drift] Consistency beyond verbs

- **Verb families are declared, never inferred** (LX-1). The canon's clusters are synonyms, and load,
  read and parse are three clusters with three meanings, so the canon holds no families. Families come
  from two sources:
  - each pack the stack census selects for a kit it discovers in the repository declares that kit's
    families;
  - the owner declares the rest through `instructions.edit`.

  A family groups canon representatives. An acquire family over `load`, `read` and `parse` exists only
  where a pack or the owner declares it.
- **One verb per declared family per object.** The object is the subtokens after the verb, compared
  after the noun canon's normalization. Its established verb is the one its earliest-landed definition
  in the family uses. A new definition over that object must use it. A tie, or an object already split,
  is reported for the owner instead of refused. A forced name never establishes a verb, and is never
  refused for drift.
- **A noun canon.** NOUNS extends canon.py's cluster shape (CLUSTERS and the `build_clusters` overlay)
  with noun clusters, written exogenously, such as `sha` against `oid`, `hash` and `digest`. The corpus
  decides only which clusters are live. Its overlay is a naming convention (`[vocabulary]`).
- **Where a split is judged.** A split is debt (`[classes]`), so the commit check and the bar refuse a
  new split as they refuse a new offender:

  | `lexicon.at-commit` | `lexicon.drift: refuse-new` | `report` | `off` |
  |---|---|---|---|
  | `refuse` | refused at commit and at the bar | counted in the drift signal, refused nowhere | not measured |
  | `warn` | warned at commit, refused at the bar | counted, refused nowhere | not measured |
  | `off` | refused at the bar | counted, refused nowhere | not measured |

  A split outside every declared family is reported, never refused.
- **The map's inventories.** The map ratchets a `lexicon-verbs` inventory from VERBS, and the lexicon's
  dossier claims `init`. The inventory stays, and NOUNS gains a sibling `lexicon-nouns` inventory.
  Removing the `init` row moves the dossier's claim and the coverage and freshness leg in the same
  commit.
- **Existing splits become debt with their rename,** through the re-baseline.

### [vocabulary] How the vocabulary changes

- **These are naming conventions,** and each changes only through the instruction layer's write path
  (`instructions.edit`: the owner's command, agents propose):
  - the verb table;
  - the noun canon and its overlay;
  - the verb families the owner declares;
  - the pack selection and custom packs;
  - the contract-declaration table;
  - site suppressions;
  - the pins and the cells' arming.

  A check refuses a commit that raises a pin or un-arms a cell with no instruction-path record. It is
  probed by staging a pin raise in a scratch clone.
- **The re-baseline.** A change through the write path that widens or reclassifies debt re-grades the
  corpus in the same commit, and sets the pin to the new debt count, with the delta and its cause
  recorded. Such changes are a removed verb row, a frozen noun, a pack upgrade, or the splits joining
  the pin. A pin change in any other commit stays refused. Probe: remove the `init` row on a fixture,
  and see one record carry the delta.
- **No session raises the pin or adds a verb on its own.** A name that will not fit is renamed, shown to
  be forced, or proposed as a vocabulary change. While the proposal is pending, its unit routes as a
  fork under `design.forks`: it is parked, or built under a conforming name. On the owner's no, the
  proposal record routes a rename to the unit that added the name. An unattended run under `refuse`
  picks a conforming name or parks the unit.
- **`ratified` gives way to that path's record, and its readers move with it.** The drift signal that
  compares VERBS and LANGS edits with `ratified` reads the write path's latest record date instead, as
  `gap-lex-08`'s leg pack. `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole and the scaffold
  read that record too. The leg pack's arm is seen red on a planted LANGS change newer than the record.
- **The `init` row** partly exists to clear `__init__`. It is re-justified as vocabulary or removed,
  since the data-model pack clears `__init__`.

### [integration] One extraction, one classification

- **One extraction primitive in `tools/lib`** (LX-2) reads every definition with its context:
  - the enclosing class;
  - its bases, resolved through imports;
  - its decorators, with aliases resolved;
  - the module's imports, which feed the stack census.

  It reads the working tree, the index or any revision. The codebase map and the lexicon each call it,
  and each copy-installed kit carries it inline. So neither kit requires the other, as KN-1 and the
  standing decision `TOOL-dClosedLexicon-12` hold. dTotalRecall builds it with the map's extraction,
  and dMindYourWords calls it.
- **The states the lexicon reads:**
  - the working tree, for `--suggest` and the census;
  - the index, for the commit check;
  - the base revision, for the bar's comparison;
  - both parents of a merge, for `--merge-losses`, which `.githooks/pre-push`'s default-branch
    merge-loss refusal and the lander call.
- **The tokenizers move into the primitive** as its shell and JavaScript parsers, so the map stops
  borrowing them from the lexicon kit. The map's other dependency on the lexicon, its `lexicon-verbs`
  inventory, stays (`[drift]`).
- **A `gov:note` may document a forced name, and never exempts one alone.** Contract declarations live
  in their table (`[forced]` item 2), not in the marker family.
- **The tag vocabulary.** The lexicon registers a tag-name vocabulary check at the instruction layer's
  name-check point, which dOrderedCharter builds: it checks the verbs and nouns in tag leaves. Where the
  lexicon is absent, the core's tag-shape check stands alone. The check grades every tag's name, policy keys
  and the overlay's rows among them, and `--suggest` answers a tag's name as it answers a function's, with
  `--as tag.<namespace>`. The namespace words come from dOrderedCharter's registry, never from `.lexicon.conf`,
  so the core's shape check and the lexicon's answers never disagree on which words may open a name (revised
  2026-10-19, the owner: "shouldn't lexicon integrate with the tag grammar? Will this be accounted for?";
  `gap-lex-10`).
- **The reviewer's lens is handed the debt a diff adds.** The Loop Review gets the trends.

### [fixes] The kit's own defects

- Refuse a repeated block header in the conf.
- Stop grading IIFE values and `@property` definitions as verbs.
- Remove `--brief` and `--help` from the documentation, or answer them.
- Retire the two-sided pin wording in every carrier that holds it: the engine, the README's pin text,
  LEXICON.md, the Skill template, kit.toml's `lexicon-pins` hole, adopt-lexicon.sh, the scaffold, both
  waiver headers, the conf and the selftest arms. Each line is listed in
  `reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-b.md`'s M17. The README's line 650 calls the
  waiver registry shrink-only, which is correct and stays.
- Keep records out of the graded population with the path selector (`[classes]`).
- The legs' `doc_reads` on `memory/builds/` go stale once records leave the graded population.
  dMindYourWords lists both carriers in its touched set, and drops or re-justifies them once the
  selector lands.

## [gaps-proposed] Gaps to register once the forks settle their home

Registered on 2026-10-15, after the forks, as `gap-lex-01` to `gap-lex-07`, in the order below. The
expansion round added `gap-lex-08`: the two drift signals become the lexicon's own leg pack.
They go to dMindYourWords, with `gap-mem-10`.

New area `Lexicon`. `gap-mem-10` (the gate absorbs debt) moves with them.

1. HIGH. No class for forced names:
   - host-forced names (pytest hooks, `__str__`, a command shim) and 22 contract-forced names count
     as debt;
   - the only exits are a pin raise or a corpus-wide text waiver: 19 raises and 0 waivers in history.
2. HIGH. `--suggest` proposes renames that break overrides:
   - `do_GET` to `cmd_get`, `emit` to `print`, `handle` to `run`;
   - `setUp` to `set_up`, which silently stops unittest calling it;
   - `get_queryset` to `read_queryset`, which breaks a Django view;
   - P29 would hand these answers to builders.
3. HIGH. Enforcement is a corpus count at the bar:
   - nothing judges a name at commit or by name;
   - a fixed offender plus a new one nets to zero;
   - landings absorbed raises instead of holding the equality: 19 raises (+814) in the pin's history.
4. MED. Records are graded:
   - 43 offenders sit under `memory/builds/`. The latest raise, +24 net in `301a36664`, came from 30
     arrivals, all aSparedSpawn build records, less 6 departures;
   - undeclared record extensions refuse the wiring leg.
5. MED. No consistency beyond verbs:
   - 57 objects carry two or more declared acquire-family verbs;
   - noun variants go unchecked (`sha`/`oid`/`hash`/`digest`; `dir`/`directory`/`folder`).
6. MED. Exemptions need no reason, and nothing checks one:
   - waivers are keyed corpus-wide, and pins and cells change by plain edit;
   - `ratified` certifies nothing about verb edits;
   - VERBS mixes vocabulary with forced names (`init`).
7. LOW. Kit defects:
   - a repeated block header silently replaces the earlier block;
   - 4 non-names are graded as verbs;
   - two dead modes still draw calls;
   - the Skill, the conf and the README disagree on what the gate does.

- **Revised: 2026-10-17. The live asks these gaps state.** dMindYourWords links or closes each one when it
  opens, and this build changes no ask's status:
  - `gap-lex-01` states TOOL-aWeldedTribunal-12, with L-1, and TOOL-aProbedToolkit-5;
  - `gap-lex-02` and `gap-lex-03` state TOOL-aProbedToolkit-4;
  - `gap-lex-06` states TOOL-aProbedToolkit-6;
  - `gap-lex-07` states TOOL-aProbedToolkit-5 too;
  - `[integration]` states TOOL-aMendedFleet-96 and TOOL-aGradedDialect-6.

## [forks] Asked, 2026-10-15

**L-1. "Third-party kits and gov's own readers force some names. How does the kit keep them out of
debt?"**
- Offered:
  - By what forces them (Recommended): packs keyed by base member, base prefix or host namespace,
    applied only where the code resolves to that base; gov's own forced names declared beside their
    reader; markers verified, never trusted.
  - By name or verb tables: one list per kit, applied everywhere. It exempts free choices: 53 sites
    for 1 forced on this tree.
  - By site annotation: the author marks each forced name, with a reason.

**L-2. "Where is a name judged, and what does an offense do at commit?"**
- Offered:
  - Commit refuses, bar compares (Recommended): staged new and renamed definitions are refused at
    commit; the bar compares the branch's offenders with its base's by name; the debt pin is the
    backstop.
  - Commit warns, bar compares.
  - Bar compares only: nothing at commit.

**L-3. "Should the lexicon catch one concept named several ways: `conf` loaded, read and parsed, and
`sha`, `oid`, `hash` and `digest` for one thing?"**
- Offered:
  - Refuse new splits (Recommended): one verb per family per object and a noun canon, seeded from the
    corpus and frozen; existing splits become debt with their rename.
  - Report only: the drift audit measures the splits and refuses nothing.
  - Verbs only, as today.

**L-4. "The memory round put the lexicon pin in dTotalRecall. Where does the lexicon's upgrade get
built?"**
- Offered:
  - Its own chain build (Recommended): `dMindYourWords`, a child of dTotalRecall, which supplies the
    map's extraction it classifies.
  - Inside dTotalRecall.

**L-5. "Which packs apply to a repository?"**
- Offered:
  - Detected (Recommended): from the import census, with manifests for versions.
  - Declared by the owner.
  - Every shipped pack.

**L-6. "My design-overview records (`.html`, `.svg`) red the lexicon's wiring leg on this branch. How
should that be fixed now?"**
- Offered:
  - Declare `html` and `svg` dark (Recommended): one `LANGS` line in `.lexicon.conf`, the gate's own
    remedy.
  - Move the three files out of the tree: they become published artifacts, with Markdown pointers.
  - Wait for the path selector: the bar stays red until the lexicon build lands it.

### Settled after L-1 to L-6, 2026-10-15

| Fork | Answer | Key | Default | Also allowed |
|---|---|---|---|---|
| L-1 | By what forces them | `lexicon.forced` | `verified` | `by-name`, `by-annotation` |
| L-2 | Commit refuses, bar compares | `lexicon.at-commit` | `refuse` | `warn`, `off` |
| L-3 | Refuse new splits | `lexicon.drift` | `refuse-new` | `report`, `off` |
| L-4 | Its own chain build | none: dMindYourWords, a child of dTotalRecall | — | — |
| L-5 | "Detected + declared by the owner (custom packs?)" | `lexicon.packs` | `detected-and-declared` | `detected`, `declared`, `all` |
| L-6 | Declare `html` and `svg` dark | none: applied the same day in `0ac38b016` | — | — |

- **L-4.** dMindYourWords takes the lexicon pin and `gap-mem-10` from dTotalRecall.
- **L-5, the owner's own answer, is the default.** The three offered options are kept as allowed
  values.
- **The owner's question: can there be custom packs? Yes.** A custom pack has the shipped packs'
  shape:
  - rows keyed by base member, base prefix or host namespace;
  - a header naming its source, and its generator or its curation.

  It is declared by the owner in the repository's lexicon declaration, and it is changed through the
  instruction write path. It is verified like a shipped pack: a row applies only where the code
  resolves to its base or host. An adopter's own framework is covered this way. gov's own
  contract-forced names, declared beside their reader, are the in-repository case of the same idea.
- **L-6** turned the undeclared-extension refusal off. The check still exits 1, on main's inherited
  1,088 against 1,087.
  Revised: 2026-10-17. L-6 declared `html` and `svg` dark; the refusal stays armed for every other
  extension, and the class closes only with the path selector (`[now]`).

**Presets.** `velocity` warns at commit and only reports drift. Every other new key holds its
default in all four presets.

**What changed elsewhere:**
- **v2:**
  - The four keys join the catalogue and every preset.
  - The chain gains dMindYourWords and becomes thirteen builds. Revised: 2026-10-17: fifteen since
    (v2 `[chain]`), after dWellOiledMachine and dFairHearing joined.
  - dTotalRecall gives up the lexicon pin and `gap-mem-10`.
  - `[owed]` gains the adopter census the second-wave packs wait on.
- **The register** gains `gap-lex-01` to `gap-lex-07`.
- **Revised: 2026-10-17.** The expansion round added `gap-lex-08` and made the two drift signals the
  lexicon's leg pack. The runtime round made the commit check a Runtime hook pack. The debt fold owes
  v2's dMindYourWords row two changes (`[debt-fold]`).

## [debt-fold] The debt round's lexicon pair, folded 2026-10-17

Dispatches 61 and 62 audited this record at `424d2a7de`
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md` and `-b.md`). Each of their 52 map rows
(the debt comparison record's `[map-lexicon]`) went here, and LX-1 to LX-3 settled its forks. Each row's
classes are its confirmed findings' own, from the two ledgers.

| Defect | A | B | Disposition | Where the fix sits | Its classes |
|---|---|---|---|---|---|
| `ratified-readers` | 3, 30, 37, 41 | 2, 30, 38 | amend | `[vocabulary]`, `ratified` and its readers | `retirement-inventory-misses-readers-by-value` |
| `acquire-family` | 25 | 14, 29 | fork, amend | `[drift]`, declared families (LX-1) | — |
| `drift-vs-classes` | 1 | — | amend | `[classes]`, the conforming and debt rows | — |
| `drift-object-undefined` | 48 | 54 | amend | `[drift]`, one verb per declared family per object | — |
| `drift-enforcement-site` | — | 9 | amend | `[drift]`, where a split is judged | — |
| `map-extraction-states` | 35 | 40 | fork, amend | `[integration]`, the states the lexicon reads (LX-2) | — |
| `map-dependency-undeclared` | 18, 28, 36, 40 | 5, 25, 28, 42, 52 | fork, amend | `[integration]`, one extraction primitive (LX-2) | — |
| `shim-uncovered` | 4, 17, 43 | 6, 16 | amend | `[packs]`, the shim rows; `[current]`'s dated note | `two-answers-to-one-question` |
| `pin-absorb-dead` | 2 | 12 | amend | `[classes]`, the pin counts debt only | — |
| `pin-rebaseline` | 47 | 49 | amend | `[vocabulary]`, the re-baseline | — |
| `markers-pep698` | 16 | 1 | amend | `[forced]` item 3 | — |
| `unresolved-base` | 49 | 47 | amend | `[forced]` item 1, three cases | — |
| `declaration-home` | 19, 52 | 23, 35, 48 | fork, amend | `[forced]` item 2 (LX-3) | — |
| `suppression-path` | 6 | 31 | amend | `[forced]` item 4 | — |
| `bar-comparison-seam` | 12, 27 | 15 | amend | `[enforcement]` item 3 | `a-merge-of-the-default-branch-read-as-additions` |
| `commit-check-seam` | 29, 45 | 8, 33, 51 | amend | `[enforcement]` item 2 | — |
| `commit-check-moves` | 46 | 24 | amend | `[enforcement]` item 2 | — |
| `replay-threshold` | 8 | 32 | amend | `[enforcement]` item 3 | — |
| `stdlib-pack-platform` | 7, 15 | 17 | amend | `[packs]`, the stdlib pack and its acceptance | — |
| `pack-selection-inputs` | 50 | 50 | amend | `[packs]`, selection states | — |
| `pack-fixture` | 5 | — | amend | `[packs]`, its acceptance | `fixture-passes-by-finding-nothing` |
| `prototype-live-import` | 42 | — | amend | `[packs]`, its acceptance; `[current]`'s dated note | `staged-break-substitutes-a-synthetic-value` |
| `pack-row-validation` | — | 55 | amend | `[packs]`, validated at load; `[forced]` item 1 | — |
| `forced-by-name-route` | 32 | 36 | amend | `[forced]`, the other values | `policy-value-with-no-route` |
| `suggest-forced-aware` | 14 | — | amend | `[forced]`, `--suggest` | — |
| `no-pack-owner-route` | 13 | — | amend | `[forced]` item 4 | `owner-item-without-its-reject-outcome` |
| `vocabulary-proposal-route` | — | 22 | amend | `[vocabulary]`, a proposal pending or refused | `owner-item-without-its-reject-outcome` |
| `nouns-table` | 26 | — | amend | `[drift]`, the noun canon | — |
| `init-row-inventory` | — | 41 | amend | `[drift]`, the map's inventories | — |
| `leg-placement` | — | 4 | amend | `[enforcement]` item 6 | — |
| `later-records` | 9, 20, 51 | 27, 43, 56 | amend | `[enforcement]` item 6; the dated note in What changed elsewhere | — |
| `chain-order` | — | 3 | owed | v2's dMindYourWords row, after review 72 | — |
| `chain-count` | 39 | 45 | amend | the dated note in What changed elsewhere | — |
| `l6-misstated` | 53 | 11 | amend | L-6's bullet; `[now]`'s dated note | — |
| `settled-stale` | 10, 34 | 37 | amend | `[settled]`'s dated note | `amendment-leaves-its-other-half-standing` |
| `drain-count` | 22 | — | amend | `[settled]`'s dated note | — |
| `readme-misread` | 21 | 20, 39 | amend | `[fixes]`; `[current]`'s dated note | — |
| `pytest-installed` | 24 | 18 | amend | `[forced]` item 5 | — |
| `doc-reads-stale` | — | 46 | amend | `[fixes]` | — |
| `three-pins` | — | 34 | amend | `[classes]`, one pin over three seams | — |
| `pins-plain-edit` | 38 | — | amend | `[vocabulary]`, the conventions and their check | — |
| `gaps-cite-asks` | 31 | — | amend | `[gaps-proposed]`'s dated note | — |
| `raise-misread` | 23 | — | amend, owed | `[gaps-proposed]` item 4; the register's row after review 72 | — |
| `gap2-example` | — | 13 | amend, owed | `[gaps-proposed]` item 2; the register's row after review 72 | `two-answers-to-one-question` |
| `foreign-ask` | — | 10, 44 | amend | `[classes]`; `[history]`'s dated note | `two-answers-to-one-question` |
| `main-red-stale` | — | 19 | amend | `[now]`'s dated note | — |
| `fixture-undefined` | 11 | — | amend | `[classes]`, out of scope | — |
| `tokenizers-thin` | 44 | 26 | amend | `[forced]` item 1, context per language | — |
| `tag-check-point` | — | 7 | amend, owed | `[integration]`, the tag vocabulary; v2's roster after review 72 | — |
| `declaration-second-carrier` | 33 | — | none: refuted, the example limits nothing and a stale arm guards the copy | — | — |
| `import-census` | — | 21 | none: refuted, `lexicon.py`'s Python and JS extractors collect imports | — | — |
| `keys-absent` | — | 53 | none: refuted, v2's `policy.on-missing-expansion` covers an absent component | — | — |

- **Owed after review 72.** Two fixes sit in v2's dMindYourWords row, which reviews 71 and 72 read as a
  spec. The parents become dWellOiledMachine and dWitnessedBar (`chain-order`), and the roster gains the
  tag-name vocabulary check (`tag-check-point`). The register's gap-lex rows take the corrected evidence
  (`raise-misread`, `gap2-example`, gap 3's history), and `gap-mem-10` moves to area Lexicon. They land
  with the systems fold. Revised 2026-10-17: they landed once review 72 returned, in v2's chain rows,
  flow-steps and the register.
- **The fold is unreviewed text.** A closing review of the debt fold is owed.
