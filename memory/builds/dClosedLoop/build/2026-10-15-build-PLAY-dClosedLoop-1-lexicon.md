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

### [classes] Every definition gets exactly one class

| Class | Means | Counts against the pin? |
|---|---|---|
| conforming | its verb is declared, and its case matches its cell | no |
| forced | a name the code cannot choose, with a verified source (`[forced]`) | no; reported in its own tally |
| out of scope | a record or a fixture, found by a path selector (`TOOL-aSurfacedLexicon-23`) | no; not graded |
| not a name | an IIFE value or a `@property`, fixed in the extractor | no |
| debt | everything else | yes |

- The pin counts debt only, and only falls (`lexicon.pin`).
- Each forced or out-of-scope name carries its source, so the lexicon has no reasonless exemption left.
- On this tree the pin falls by 28 forced and 43 out-of-scope names, and by 4 false positives, once
  the classes land.

### [forced] How a forced name is recognised, with no agent action

1. **Host-forced names come from packs** keyed by what forces the name:
   - a base class's member, such as `logging.Handler.emit`;
   - a base's prefix, such as `ast.NodeVisitor` with `visit_*` or `http.server.BaseHTTPRequestHandler`
     with `do_*`;
   - a host's namespace or closed set, such as pytest's hook specifications or Python's data-model
     dunders.

   A generic name (`emit`, `handle`, `run`, `do_*`) is forced only where its enclosing class resolves,
   statically and through its imports, to the base that defines it. A namespaced closed set applies by
   name. The same `emit` stays debt in a module function, or on a class with no outside base.
2. **Contract-forced names are declared beside the reader that keys on them.** For example,
   `agent-cap.js` declares that it reads `boundedParallel` and `chunk` by name. The declaration lives
   in the `gov:` marker family. A stale arm reds it once the reader stops matching. This is where
   `.lexicon.conf` already says the constraint belongs.
3. **Markers are a fast path, never a pass.** `@typing.override` (PEP 698), TypeScript's `override` and
   `hookimpl` are honoured only where the packs confirm an outside base. An unconfirmed marker reds, as
   PEP 698 rules.
4. **A site suppression with a reason is the owner's fallback** for a host no pack covers. It is
   counted and printed, never the default. Exempting by a stamp anyone can apply is the habit this
   review ends.
5. **No live import.** Resolution runs against committed pack data, so every node grades the same.
   `pytest` is not installed on this node, which is the reason.

`--suggest` becomes forced-aware. It never proposes renaming a forced name; it answers that the name
is forced by its base or host, and to keep it.

### [packs] The pre-built tables, as packs

- **One pack per host kit, generated where possible:**
  - `inspect` per Python minor version for the stdlib;
  - the wheel's AST for pip kits, never an import;
  - pluggy's hook specifications for pytest;
  - `.d.ts` declarations for JavaScript kits.

  Shell hosts (bats, and bash's and zsh's hook functions) are curated, about 8 names.
- **Each pack carries a header:** the kit, its version range, and the generator command that rebuilds
  it.
- **First wave:**
  - the Python data model;
  - the commonly subclassed stdlib bases;
  - unittest, pytest, argparse, `ast`, `http.server`, `logging`, `json` and `cmd`;
  - the shell hosts.
- **Second wave:** Django, Flask, Starlette and FastAPI, and React's lifecycle and hooks. Each ships
  after a census in an adopter shows its names actually offend. Node's core events and Express need
  no pack.
- **Selection:** the adopter's stack is detected from the import census the extractor already makes,
  with manifests (`pyproject.toml`, `requirements.txt`, `package.json`, `composer.json`) supplying
  versions where they exist. Asked as L-5.

### [enforcement] Where a name is judged

1. **Supply, at the point of naming.** The builder's work order hands it (P29):
   - the verb rows with their negatives;
   - the packs that apply to its write set;
   - forced-aware `--suggest` answers for the names its spec declares.
2. **At commit.** The definitions a commit adds or renames, in its staged files, are graded. Merge
   commits are left to the bar, because their diff carries the other parent's names. What an offense
   does is asked as L-2.
3. **At the bar, by name.** The branch's offender set is compared with its base's, and the bar reds on
   any offender the branch adds. Dispatch 27 found the bar already computes this comparison, but only
   to label a red. The keys must be move-aware: the build first replays the merges since 2026-08-16,
   and counts the reds that come from moved files.
4. **The count stays as the backstop.** The debt-only pin, shrink-only.
5. **The Loop Review reads the trends:** debt, the forced tally, and drift.

### [drift] Consistency beyond verbs

- **One verb per family per object.** The canon already groups verbs into families, such as acquire
  (load, read, parse) and create (build, make, new). A new definition over an object that already has
  an established verb in that family must use it.
- **A noun canon.** A NOUNS table, alongside VERBS, holds one spelling per concept (`sha` against
  `oid`, `hash` and `digest`). It is seeded from the corpus census and then frozen, as the verb seed
  was.
- **Existing splits become debt with their rename.** New splits are handled as L-3 says.

### [vocabulary] How the vocabulary changes

- **The verb table, the noun canon, the pack selection and the contract declarations are naming
  conventions.** Each changes only through the instruction layer's write path (`instructions.edit`:
  the owner's command, agents propose).
- **No session raises the pin or adds a verb on its own.** A name that will not fit is renamed, shown to
  be forced, or proposed as a vocabulary change.
- **`ratified` gives way to that path's record.** The `init` verb row, which partly exists to clear
  `__init__`, is re-justified as vocabulary or removed, since the data-model pack clears `__init__`.

### [integration] One extraction, one classification

- **The codebase map extracts every definition with its context:**
  - the enclosing class;
  - its bases, resolved through imports;
  - its decorators, with aliases resolved;
  - the module's imports, which feed the stack census.

  This is dTotalRecall's map work. The lexicon stops walking the corpus itself, and classifies the
  map's definitions.
- **Today's dependency inverts.** The map borrows the lexicon's tokenizers now; the map comes to own
  extraction, with those tokenizers as its shell and JavaScript parsers.
- **A `gov:note` may document a forced name, and never exempts one alone.** Contract declarations use
  the marker family's existing readers.
- **The reviewer's lens is handed the debt a diff adds.** The Loop Review gets the trends.

### [fixes] The kit's own defects

- Refuse a repeated block header in the conf.
- Stop grading IIFE values and `@property` definitions as verbs.
- Remove `--brief` and `--help` from the documentation, or answer them.
- Reconcile the Skill, the conf and the README on what the gate does.
- Keep records out of the graded population with the path selector.

## [gaps-proposed] Gaps to register once the forks settle their home

New area `Lexicon`. `gap-mem-10` (the gate absorbs debt) moves with them.

1. HIGH. No class for forced names:
   - host-forced names (pytest hooks, `__str__`, a command shim) and 22 contract-forced names count
     as debt;
   - the only exits are a pin raise or a corpus-wide text waiver: 19 raises and 0 waivers in history.
2. HIGH. `--suggest` proposes renames that break overrides:
   - `do_GET` to `cmd_get`, `emit` to `print`, `handle` to `run`;
   - `setUp` to `set_up`, which silently stops unittest calling it;
   - P29 would hand these answers to builders.
3. HIGH. Enforcement is a corpus count at the bar:
   - nothing judges a name at commit or by name;
   - a fixed offender plus a new one nets to zero;
   - landings do not hold the equality, and main reads 1,088 against 1,087.
4. MED. Records are graded:
   - 43 offenders sit under `memory/builds/`, and they drove the latest raise (+24 of +30 in
     `301a36664`);
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
