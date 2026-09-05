# TOOL-aSurfacedLexicon-8 — `--suggest` becomes surface-aware and answers in the declared convention

**Status:** SPECCED · rev-5 · 2026-09-05 · node a · Tier-2 · base 6c670b02 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 |

<!-- /gen:spec-records -->

## 1. Goal

Make `--suggest` take the surface it is answering for, so it consults `BANNED_SUFFIXES` on a type cell
and returns a name in the cell's declared convention rather than in whatever case the caller typed.
A surface-blind suggestion is how the tool produced a name its own gate rejects, and that is a defect
of the advice half rather than a cosmetic one.

## 2. Scope (IN)

- **S1** — `--as <cell>` is a REQUIRED companion to `--suggest`. Omitting it exits 2 with a usage line
  naming the flag. It is not defaulted, because the surface is the whole question and a default answers
  it silently for a caller who did not think about it.
- **S2** — `<cell>` resolves against the `CELLS:` block. FOUR refusals are distinct and separately
  worded: an undeclared cell, a `dark` cell, a malformed cell, and a BARE SURFACE.
  `TOOL-aSurfacedLexicon-4` owns the block grammar; this unit is a reader of it. The bare-surface
  refusal is §8's ratified F2 ruling reaching scope, which rev-3 left sitting in the ruling and never
  wrote here: the message lists the declared cells that carry the surface, and that list is the clause
  making the refusal a menu rather than a wall. Distinctness is now GRADED rather than asserted, by
  AC9, AC10 and AC11, which compare the messages instead of only observing a non-zero exit.
- **S3** — On a cell carrying `notail`, the name's TAIL is checked against `BANNED_SUFFIXES` before the
  leading token is looked at, and a hit is reported with the banned suffix named. `--suggest FooManager
  --as py.type` answers about `Manager`. **The order is DEFENSIVE over a population no declaration
  populates, and that is stated rather than implied.** No cell anywhere in this build arms both arms at
  once: `sed -n '348,363p'
  memory/builds/aSurfacedLexicon/build/2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md |
  awk '/vocab/ && /notail/' | wc -l` returns 0 over the sixteen proposed rows, where `/vocab/` alone
  returns 2 and `/notail/` alone returns 1; the two cells that land tracked before this unit,
  `TOOL-aSurfacedLexicon-6`'s `py.constant` and `TOOL-aSurfacedLexicon-14`'s `sh.function`, arm neither.
  So no criterion below can distinguish this ordering from its reverse, and none pretends to. If a
  later declaration arms both on one cell, this rule acquires a population and owes a criterion whose
  input hits both arms.
- **S4** — On a cell carrying `vocab`, the leading-token path runs as
  `TOOL-aSurfacedLexicon-7` leaves it, and its result is re-cased to the cell's declared convention
  before printing.
- **S5** — A name that violates the cell's convention but breaks no other predicate still gets an
  answer: the re-cased spelling of the same name, with the convention it currently satisfies named,
  matching the message shape the convention-predicate probe already observed. **This is the tool's
  quiet everyday case and it is the one path rev-3 graded nowhere.** It is also the path with a
  control-flow consequence: a name whose leading token IS declared returns at
  `tools/lexicon/lexicon.py:805-807` today, printing `OK` before any tail or convention check runs, so
  the renderer must be reached from THAT return and not only from the banned-verb branch. AC12 is its
  criterion.
- **S6** — The renderer that turns subtokens back into a declared convention lands in
  `tools/lexicon/subtokens.py` as `render_convention`, beside `TOOL-aSurfacedLexicon-5`'s classifier.
  It is the inverse of that classifier and shares its affix rule, so the two live in one file or they
  drift. The name is not free-chosen: §4's `### Inventory` carries it with its cell, its `--suggest`
  verdict and this unit's pin delta.
- **S7** — `tools/lexicon/SKILL.template.md:19` and its description line gain `--as <cell>`. **The
  `kit.toml` clause rev-3 carried here is STRUCK.** Line 19 is `{{SUGGEST_CLI}} <identifier>` and
  `tools/lexicon/kit.toml:38` is the six-name placeholder list `["VERBS_TABLE", "SUGGEST_CLI",
  "BRIEF_CLI", "GATE_CLI", "CONF", "KIT_VERSION"]`, both read at this rev's base, so appending a
  LITERAL `--as <cell>` introduces no new token and the descriptor does not follow. The hazard the
  clause was reaching for is already covered from the other side:
  `tools/lexicon/adopt-lexicon.sh:144-148` greps the rendered Skill for a leftover `{{...}}` token and
  refuses, on the `lexicon wiring` leg whose
  guard is `[]`, so an unsubstituted token cannot ship silently and needs no scope bullet here.
- **S8** — WHAT A `file` CELL'S ARGUMENT IS, which no spec in the set stated. `--suggest` takes an
  identifier, so on an `<ext>.file` cell it accepts a BASENAME and reduces it to the graded stem with
  `TOOL-aSurfacedLexicon-5`'s `read_stem` — the basename up to its FIRST dot, that unit's S6, landing
  at order 3. A path is reduced to its basename first; the reduction is a reuse of the grader's own
  seam and not a second stemming rule, because a suggester that stems differently from the checker is
  the surface-blindness §1 exists to remove, one level down. `_SUBTOKEN_RE` at
  `tools/lexicon/subtokens.py:20` shreds `.` and `/` into separate tokens and so cannot compute that
  stem on its own, which is why the reuse is named rather than assumed.
- **S9** — HOW A SELECTOR'D ROW PARTICIPATES. `TOOL-aSurfacedLexicon-13` lands at order 5, one order
  BEFORE this unit, and its selector rides on the `CELLS` row key: a key is `<ext>.<surface>`
  optionally followed by one selector clause naming a prefix, or a decorator name in `parser` mode.
  `--as` takes the plain `<ext>.<surface>` cell and never a selector'd key; a selector'd key passed to
  `--as` is malformed. The routing is then applied FROM THE NAME, exactly as the grader applies it: a
  name matching a declared prefix selector on the resolved cell is answered in the SELECTOR's
  convention and arms, because that is the cell the grader will grade it in. A DECORATOR selector
  cannot be resolved from an identifier — `--suggest` sees no decorator — so such a cell answers in the
  parent's convention and says so in the message. That limit is honest and stated rather than silent.
  Unit 13 never mentions `--suggest` or `--as`: `grep -c suggest` over its spec returns 0 at this rev's
  base, so this bullet is the only place the two mechanisms meet and it owes no edit from that unit.

## 3. Non-goals (OUT)

The convention classifier itself, which is `TOOL-aSurfacedLexicon-5` — this unit consumes
`classify()` and adds only the inverse direction. The `CELLS:` and `PINS:` grammar, which is
`TOOL-aSurfacedLexicon-4`. The canon graft into the verb path, which is `TOOL-aSurfacedLexicon-7` and
must land first or S4 has nothing to re-case. The prefix and decorator selector, which is
`TOOL-aSurfacedLexicon-13` and is the mechanism that lets one cell answer differently for
`cmd_*` handlers and `test_*` arms. That unit puts the selector ON the `<ext>.<surface>` row key, so
cell keys carry an optional selector clause. **The tense rev-3 wrote here was backwards and is
corrected:** unit 13 is order 5 and this unit is order 6, so the selector'd key grammar ALREADY EXISTS
when `--as` lands rather than arriving after it. What is out of scope is BUILDING the selector; how a
selector'd row participates in cell resolution is in scope and is S9, because a resolution rule that
went unwritten would have left `cmd_*` unanswerable, which is the exact surface-blindness §1 says this
unit exists to remove.

No corpus pass. `run_suggest`'s docstring at `tools/lexicon/lexicon.py:786-790` states the contract and
it survives: the whole value is that an author can ask before writing, and a verb that walks 900 files
to answer one question is a verb nobody waits for. Adding `--as` must not add a walk.

No new gate leg. This unit changes what an existing verb prints and what an existing wiring leg
byte-compares.

## 4. Design

### Data model

A cell is `<ext>.<surface>` and carries a convention plus optional `vocab` and `notail` arms.
`--suggest <name> --as <cell>` resolves the row, then runs at most three checks in this order: the
banned tail when `notail` is armed, the leading token when `vocab` is armed, and the convention
always. The first hit is the answer; the convention re-casing is applied to whatever name the earlier
checks produced, so the printed name is legal under every armed predicate of that cell at once.

There is no `CELLS:` block in the tree at this rev — `grep -nE '^[A-Z]+:' .lexicon.conf` returns
`VERBS:` and `LAYERS:` and nothing else — so every statement here about cell keys is measured against
the block the REBUILD RESEARCH RECORD proposes, at its lines 348-363. If a unit lands a different key
shape, F2's tie-break moves with it and must be re-run rather than inherited.

### What is armed at this unit's own build order

Read at each owning spec rather than assumed, because five criteria were previously phrased against
cells nothing declares at order 6. `TOOL-aSurfacedLexicon-6` at order 4 lands exactly one tracked
`CELLS` row, `py.constant`, and names `py.function`, `py.type` and `js.function` as the pairs that are
non-empty and carry no row. `TOOL-aSurfacedLexicon-14` at order 4 lands a second, `sh.function snake`,
with its `sh.function.conv` pin row, once its shell parser exists — owner ruling Q5. Those TWO are the
whole tracked population at order 6. `TOOL-aSurfacedLexicon-4` at order 2 ships the grammar and no
rows: its Migration says the conf rewrite that pastes the real `CELLS` and `PINS` bodies is a later
unit. `TOOL-aSurfacedLexicon-5` at order 3 arms nothing. The FULL matrix is
`TOOL-aSurfacedLexicon-12`'s S14 at order 7, one order after this one.

So at this unit's landing order the tracked declaration answers for `py.constant` and `sh.function`
and refuses every other cell as undeclared. That is a DECLARED consequence of S1 keeping `--as`
required, not an oversight, and §4's `### Migration` already states its general form: a repo with no
row for a cell has no cell to name, and the refusal is the notice. It is written down here because the
alternative — defaulting the cell, or deferring the flag to order 7 — would answer the surface question
silently for a caller who did not think about it, which is S1's whole reason for existing. What it
COSTS is one build order in which `--suggest` answers in full only for those two cells, and §6 grades
every other cell against a scratch declaration rather than pretending the tracked one carries it.

Verified today by direct run on this worktree:

| Invocation | What it prints today |
|---|---|
| `--suggest FooManager` | `` `foo` is not in the declared table, and no row bans it by name `` |
| `--suggest fetchUserData` | `` use `loadUserData` — the declaration says `load`, NOT `fetch` `` |

The first answers about the wrong end of the name. The second answers with a name that the convention
predicate `TOOL-aSurfacedLexicon-5` builds reds on a `py.function` cell, because `loadUserData`
satisfies camel and the cell declares snake.

### Inventory

**`run_suggest` has FOUR exits and rev-3's Inventory named one of them.** Read at this rev's base,
`run_suggest` spans `tools/lexicon/lexicon.py:785-852` and returns from exactly these places:

| Exit | Lines | What it prints today | This unit |
|---|---|---|---|
| ungradeable | `:802-804` | `has no word characters, so it is ungradeable rather than wrong` | AC7 keeps it, narrowed to the underscore-only and non-ASCII names |
| declared verb | `:805-807` | `OK — <name> leads with <verb>, which the declaration carries` | REACHED: the convention check and the renderer must run before this returns (S5, AC12) |
| banned verb | `:834-848`, case block `:837-846` | `use <swap> — the declaration says <want>, NOT <verb>` | the case-inheritance block `:837-846` is REPLACED by `render_convention` |
| neither | `:849-851` | `<verb> is not in the declared table, and no row bans it by name` | REACHED: the convention answer replaces the bare "not in the table" line under a cell |

That matters because rev-3 named only the third row and AC1 does not reach it. `FooManager` leads with
`foo`, which is neither declared nor banned, so it exits at `:850` — verified by direct run on this
worktree and recorded in this section's own today-behaviour table. AC12's `buildUserIndex` leads with
`build`, which IS declared, so it exits at `:806`. Two of this unit's criteria therefore land on exits
the previous rev's Inventory did not mention, which is how a renderer wired only into the banned
branch would have passed a read and failed both.

### Identifiers this unit mints

Each was run through `python tools/lexicon/lexicon.py --suggest <name>` on this worktree at this rev's
base, in the shape `TOOL-aSurfacedLexicon-7` established and with the same obligation it states: any
identifier added in this build that is not in a table like this one owes its own `--suggest` run before
the commit lands.

| Identifier | Cell | Role | `--suggest` verdict |
|---|---|---|---|
| `render_convention` | `py.function` | S6's inverse of `TOOL-aSurfacedLexicon-5`'s classifier, in `tools/lexicon/subtokens.py` | OK — leads with `render`, which the declaration carries |
| `resolve_cell` | `py.function` | S2's `<cell>` lookup and its four refusals, in `tools/lexicon/lexicon.py` | OK — leads with `resolve`, which the declaration carries |

**Pin delta: ZERO.** Both lead with a declared verb, so neither is a P1 offender and
`VERB_OFFENDER_PIN`, which reads `461` at `.lexicon.conf:164` and counts per occurrence, passes through
this unit unchanged. The negative is measured rather than assumed, and the obvious alternative would
have cost a raise: `--suggest recase_to_convention` answers that `recase` is not in the declared table.
`TOOL-aSurfacedLexicon-5` raises that same pin by one for `classify` at order 3 and
`TOOL-aSurfacedLexicon-6` lands on top of the raise at order 4, so the scalar this unit inherits at
order 6 is whatever those two leave and is not restated here. Module-body assignments are not graded by
the verb predicate, so this unit budgets no delta for constants and mints none.

The re-casing replaces `tools/lexicon/lexicon.py:837-846`, the block whose comment says the verb
inherits the case of the token it replaces. That rule was correct when the tool had no declared
convention to answer in and is wrong the moment it does. The comment above it, at `:810-823`, records
two review rounds spent on exactly this splice, and it is the reason S6 is not a one-liner: a round-1
fix that rebuilt the tail from `subtokens()` returned `getUserURLs` as `readUserUrLs`, `fetch_v2_data`
as `load_v_2_data` and `create$data` as `build_data` with the `$` silently gone. Three answers that
had been correct before the fix, replayed by re-running the round-1 hunk that `git show 468e8912 --
tools/lexicon/lexicon.py` returns.

That comment's own EXAMPLE does not reproduce, and the next reader should not trust it. It says the
pre-round-1 code made `_fetch_conf` suggest `_load_h_conf`. The body at that point, read with `git
show 468e8912^:tools/lexicon/lexicon.py`, guards the slice with `name.lower().startswith(verb)` and
printed `load` with the whole tail dropped. The two-rounds history is real; the example is not.

`subtokens()` at `tools/lexicon/subtokens.py:23-26` lowercases, breaks acronym runs, splits on digit
boundaries and drops every character its regex cannot see. So the re-caser cannot be built by round-
tripping a name through it, and it cannot be built by rebuilding one from its subtokens either.

**The renderer is SPAN-ANCHORED.** It builds from `_SUBTOKEN_RE.finditer` spans, keeps each token's
ORIGINAL surface wherever that surface already satisfies the target convention, and regenerates no
byte outside a span EXCEPT the separators the target convention itself supplies. That carve-out is not
a softening; the absolute without it is false, and the next paragraph and two criteria already
disprove it. `fetchUserData` spans as (0,5)(5,9)(9,13) with no gaps, so AC2's expected
`load_user_data` emits two underscore bytes that exist in no span, and `fetch_v2_data`'s underscores at
offsets 5 and 8 sit outside every span, so AC4's expected `loadV2Data` deletes them. Separators are the
convention's own alphabet and the renderer owns them; every OTHER byte outside a span is preserved or
the name is refused. Rev-3 stated the absolute and the carve-out as two paragraphs; they are one rule
and are written as one. Running `_SUBTOKEN_RE.finditer` over
`getUserURLs` covers 11 of its 11 characters, so it has NO unseen characters at all, and a renderer
that rebuilds from lowercased subtokens still returns `readUserUrLs` on it — what the round trip loses
there is CASE, not a character.

**The refusal is NARROW.** It fires only on an unseen character the target convention does not itself
re-supply. Separators are re-supplied; `$` and `é` are not. Of the 16 shape-preservation rows read by
`sed -n '883,903p' tools/lexicon/selftest.py`, 11 carry unseen characters and every one of those 11 is
a `_` or a `-`. A refusal firing on any unseen character would therefore refuse `--suggest
fetch_remote --as js.function` and hand back `load_remote`, a name the camel predicate reds — verbatim
the surface-blind suggestion §1 says this unit exists to remove, on every separator-bearing name.

So the risk classes here are THREE, not two. Characters the splitter cannot see that the convention
re-supplies (separators — safe, and the majority). Characters it cannot see that the convention does
not re-supply (`$`, `é` — the refusal's whole population). And case inside `[A-Za-z]`, which every span
covers and a rebuild still destroys; that is the class `getUserURLs` is in, and it is the one that has
actually broken. See F1.

### Migration

None for adopters who have not adopted the block yet, because a repo with no `CELLS:` block has no
cell to name and `--suggest` refuses with the same message an undeclared cell gets. The refusal is the
migration notice.

### Rollout

`--as` becomes required in the same commit that ships the cell reader, so there is no window in which
the flag exists and does nothing. The `lexicon wiring` leg carries `guard: []` in
`tools/gate-legs.json`, so it runs on every bar and byte-compares the rendered Skill: the template edit
in S7 reds the bar until the Skill is re-rendered, which is the transition's own tripwire and needs no
new check.

**THIS UNIT AND `TOOL-aSurfacedLexicon-11` ARE SEQUENTIAL WITHIN ORDER 6, NOT PARALLEL.** Both specs
read `order 6`. Both Files-touched lists name `tools/lexicon/lexicon.py` and
`tools/lexicon/selftest.py`, and the intersection is inside ONE function: that unit's S2 routes its
canon overlay through the `build_form_index` call site `TOOL-aSurfacedLexicon-7` grafts into
`run_suggest`, and this unit rewrites `run_suggest`'s answer path, replacing the case-inheritance block
at `lexicon.py:837-846` and reaching the `:806` and `:850` exits. BUILD-METHOD M6 permits concurrency
only where disjointness is PROVEN, and this pair's write sets intersect, so the two passes are
dispatched one after the other. **`TOOL-aSurfacedLexicon-11` lands FIRST**, because its edit is
additive — one optional parameter on `build_form_index` and one argument at the graft site — where this
unit's is a rewrite of the surrounding answer path; landing the rewrite first would force that
parameter into a function body that had just moved underneath it. Read that unit's spec at this rev's
base to confirm the write set rather than trusting this sentence: it names `canon.py`,
`lexicon_conf.py`, `lexicon.py`, `adopt-lexicon.sh`, `scaffold_lexicon.py`, `selftest.py`,
`.lexicon.conf` and its README. **That spec CARRIES its half**: it names this unit, states the same
sequencing, and gives the same reason. The obligation this rev recorded as outstanding was discharged
in the same batch that recorded it, and the sentence is corrected rather than left asserting a debt
that no longer exists.

The generated build-order table cannot be used as the disjointness proof and must not be read as one.
Its `Parallel` column derives from the step's CARDINALITY alone, which `TOOL-aSurfacedLexicon-17` in
`memory/backlog/TOOL.md:341` records as an over-claim with this build's own step 5 as its worked
example. A `yes` in that column means "more than one unit sits at this order", never "their write sets
are disjoint".

### Files touched (estimate)

`tools/lexicon/lexicon.py`, `tools/lexicon/subtokens.py`, `tools/lexicon/SKILL.template.md`, the
rendered Skill, `tools/lexicon/selftest.py`, and `memory/map/generated/symbols.json`. ESTIMATE on the
size — no case-rendering code exists anywhere in the kit to measure against, which the research record
names as one of the things it could not determine.

`tools/lexicon/kit.toml` is REMOVED from this list at this rev, per the struck clause in S7: appending
a literal `--as <cell>` to the Skill template introduces no placeholder, so the descriptor is not
touched.

`memory/map/generated/symbols.json` is ADDED, and it is the entry rev-3 missed. That artifact already
indexes `tools/lexicon/subtokens.py` by symbol — `leading_verb` and `subtokens` are live rows in it at
this rev's base — so S6's `render_convention` is a public definition whose absence from the regenerated
artifact reds a leg, and §1's claim-edits-regen-in-the-same-commit rule applies. The arm that moves is
FRESHNESS, not coverage: `tools/codebase-map/test_codebase_map.py`'s
`test_generated_artifacts_are_fresh` byte-compares the committed `symbols.json` against a live
re-render. The coverage arm grades INVENTORY keys, and this unit adds none — the ten inventories are
`gate-legs`, `kits`, `git-hooks`, `workflow-scripts`, `skill-engines`, `rendered-skills`,
`gotcha-classes`, `guides`, `backlog-shards` and `lexicon-verbs`, and a Python symbol is in none of
them.

### Alternatives rejected

Defaulting `--as` to the cell implied by the caller's file extension. Rejected because `--suggest`
takes an identifier and not a path, so there is no file to read an extension from, and inventing one
from the cwd would make the answer depend on where the author happened to be standing.

Accepting a bare surface (`--as function`) and resolving the language from the single armed cell when
there is exactly one. Rejected as the same class one step down: it answers correctly on a one-language
repo and silently picks a language on every other. See F2.

## 5. Production-readiness checklist

- security — N/A. One identifier in, one line out, no file written, no network.
- perf / scale — unchanged by construction: the no-corpus-pass contract at `lexicon.py:786-790` is
  preserved and S1 through S6 add only declaration reads.
- a11y — N/A. A stdout line on a CLI has no rendered surface.
- i18n — a non-ASCII identifier is the known gap: `subtokens.py` is ASCII-only, so an accented name
  re-cases on a truncated core and a fully non-ASCII one has no subtokens at all. **It is FILED, as
  `TOOL-aSurfacedLexicon-16` at `memory/backlog/TOOL.md:343`, and rev-3's "needs its backlog row before
  this unit builds" is struck as stale by one commit.** No precondition remains; this unit must refuse
  such a name rather than re-spell it, and that refusal is AC7.
- error / empty / loading states — SIX, reconciled to S1, S2 and F1 rather than to rev-3's shorter and
  differently-drawn list. S1's missing-flag refusal, graded by AC3. S2's four — undeclared cell (AC9),
  `dark` cell (AC6), malformed cell (AC10) and bare surface (AC11) — whose distinctness is the point,
  so those criteria compare the MESSAGES and not only the exit codes. And F1's NARROWED refusal: an
  unseen character the target convention does not itself re-supply. A separator is re-supplied and
  never refuses. `$` and `é` do. The wide form of that predicate — any unseen character — is the one
  rev-3 rejected, because it refuses a plain snake name asked for in a camel cell. Rev-3 listed three
  here, dropped `malformed` and bare surface entirely, and counted S1's refusal among S2's; the spec
  disagreed with itself about the population in three places.
- observability — every refusal names the flag or the cell that caused it, so a caller never has to
  guess which of the three it hit.
- risks — the re-caser is the one place in this build that WRITES a name rather than grading one, so a
  bug here hands an author a wrong name with the tool's authority behind it. The round-2 regression
  corpus in AC4 is the mitigation and it is not optional.
- testing + left-shift gates — arms in `tools/lexicon/selftest.py` covering each cell arm and the three
  historical breakages by name; observed-RED is AC4. A SECOND observed-RED is owed for the narrowed
  refusal itself: stage the wide predicate, watch a separator-bearing name refuse, unstage. Without it
  the narrowing is an assertion about nothing.
- migration / rollback — single-commit revert; the template and the rendered Skill revert together or
  `lexicon wiring` reds, which is the intended coupling.
- user docs — `tools/lexicon/README.md` and the rendered Skill both carry the new invocation. The Skill
  is generated, so its update is the template edit in S7 and not a second authored copy.

## 6. Acceptance criteria

**Every criterion below that names a cell names the DECLARATION it is measured against**, because at
build order 6 the tracked declaration carries `py.constant` and `sh.function` and nothing else — §4's
`### What is armed at this unit's own build order` reads that out of the owning specs. Rev-3 phrased
AC1, AC2, AC4, AC5 and AC6 against `py.type`, `py.function`, `js.function`, `py.file` and `md.file`,
every one of which is undeclared at this order, so each would have hit this unit's OWN S2
undeclared-cell refusal instead of the behaviour it asserts, and AC6 would have observed the wrong
refusal message entirely.

The route is `TOOL-aSurfacedLexicon-5`'s and this unit adopts it unchanged, as units 7 and 13 already
did. A SCRATCH DECLARATION is a `CELLS` block written into the working-tree `.lexicon.conf` and never
committed: `main()` resolves the root with `git rev-parse --show-toplevel` and `run()` opens
`root / CONF_NAME`, so the engine takes no `--conf` flag and no fixture repo is needed. The rows the
scratch block carries are the ones the research record proposes at its lines 348-363, verbatim, so no
criterion below invents a convention. Removing the block returns every run to the tracked declaration's
answer, which is itself worth observing and is AC9's second half.

**What is DEFERRED, named rather than implied.** The STANDING answer for each of these cells against
the TRACKED declaration is not this unit's to observe, because this unit arms nothing:
`TOOL-aSurfacedLexicon-12`'s S14 writes the full `CELLS` matrix at order 7, and every criterion here
that names a cell other than `py.constant` or `sh.function` becomes a tracked-declaration observation
only then. What is NOT deferred is any observed-RED obligation: AC4's staged re-caser and AC12's
staged break are both observed against a scratch declaration before this unit is called done, which is
where "a new predicate is not landed until its failing case has been observed" is actually discharged.

- **AC1** — With a scratch declaration carrying `py.type pascal notail`, `python
  tools/lexicon/lexicon.py --suggest FooManager --as py.type` names the banned suffix `Manager`. Today
  `--suggest FooManager` answers about `foo` — `` `foo` is not in the declared table, and no row bans it
  by name `` — verified by direct run on this worktree at this rev, exiting at `lexicon.py:850` and not
  at the `:837-846` block §4's Inventory used to name alone.
- **AC2** — With a scratch declaration carrying `py.function snake vocab`, `python
  tools/lexicon/lexicon.py --suggest fetchUserData --as py.function` returns `load_user_data`. Today
  `--suggest fetchUserData` returns `loadUserData`, verified by direct run at this rev, and that name
  reds the `py.function` snake cell.
- **AC3** — When `python tools/lexicon/lexicon.py --suggest fetchUserData` runs with no `--as`, it
  exits 2 and the message names `--as`. The refusal is asserted on the exit code and on the text, so a
  future default cannot slip in past a test that only reads stdout.
- **AC4** — With a scratch declaration carrying `js.function camel vocab`, when the round-2 regression
  names `getUserURLs`, `fetch_v2_data` and `create$data` are run
  through `--suggest ... --as js.function`, each answer is asserted by VALUE: `create$data` refuses on
  the `$` and falls back to today's already-lossless slice `build$data`, `fetch_v2_data` re-cases to
  `loadV2Data`, and `getUserURLs` keeps every token surface and swaps only the verb. "Preserves the
  characters the splitter cannot see" was this criterion's first wording and it is NOT sufficient —
  `getUserURLs` has no such characters, 11 of its 11 covered by `_SUBTOKEN_RE.finditer` spans, and it is
  the name that broke — so the criterion is the three answers themselves. Staging a re-caser that
  rebuilds the tail from `subtokens()` reds all three arms in `tools/lexicon/selftest.py`; unstaging
  returns them to green. The RED is observed before this unit is called done.
- **AC5** — With a scratch declaration carrying `py.file snake`, `--suggest checkKitPlaceholders.py
  --as py.file` answers `check_kit_placeholders`, and `--suggest map_extractors.template.py --as
  py.file` answers `map_extractors` unchanged with no verb finding. Both pin an INPUT and an ANSWER by
  value, which rev-3's wording did not: it named neither, asserted a negative about an unnamed name,
  and was satisfied by any already-snake input. The second input is S8's stemming rule doing visible
  work — `read_stem` takes the basename up to its FIRST dot, so the graded stem is `map_extractors` and
  not `map_extractors.template`, and a last-dot rule would answer differently. No leading-token check
  runs on either, because `py.file` carries neither `vocab` nor `notail` in the declaration the answer
  is measured against.
- **AC6** — With a scratch declaration carrying `md.file dark`, `--as md.file` refuses naming the cell
  as `dark` rather than answering, and exits non-zero. The scratch block is what makes this observable
  at all: against the tracked declaration at order 6 the same run refuses as UNDECLARED, a different
  message, so rev-3's criterion would have passed on the wrong refusal. AC9 pins that the two messages
  differ.
- **AC7** — When an identifier carrying no ASCII word characters is passed, the run refuses as
  ungradeable and re-spells nothing, preserving `leading_verb`'s contract. That contract is at
  `tools/lexicon/subtokens.py:29`, where `def leading_verb` sits, and the sentence stating it spans
  `:32-34`; the `:29-38` cited here at rev-2 runs past the docstring into the body. The contract is
  also narrower than its own docstring claims: calling `leading_verb("1")` returns `"1"` and not the
  empty string, because `_SUBTOKEN_RE` includes `[0-9]+`, while `leading_verb("_")` and
  `leading_verb("__")` do return `""`. Measured by direct call on this worktree. So this arm's
  population is the underscore-only and the non-ASCII names, and a digit-leading name is graded rather
  than refused.
- **AC8** — When `tools/lexicon/SKILL.template.md` is edited without re-rendering, `bash
  tools/lexicon/adopt-lexicon.sh --check` reds on the byte-compare; after `--render` it greens. The
  leg's guard is `[]` in `tools/gate-legs.json`, so this fires on every bar.
- **AC9** — With a scratch declaration carrying the research record's sixteen rows, `--as py.type`
  answers; with the scratch block REMOVED, the same run refuses as undeclared against the tracked
  declaration, exits non-zero, and its message names the cell `py.type` and the word UNDECLARED. The
  two message strings are captured and asserted to DIFFER from AC6's `dark` refusal. S2 declares the
  four refusals distinct, and distinctness asserted but never compared is the
  gate-satisfied-by-its-own-prose shape.
- **AC10** — With any declaration, `--as py..function`, `--as pyfunction` and `--as py.function.extra`
  each refuse as MALFORMED, exit non-zero, and produce a message that differs from AC9's undeclared
  refusal. The third input is the S9 boundary: a selector'd key is malformed as an `--as` argument,
  because `--as` addresses the parent cell and the selector is applied from the name instead.
- **AC11** — With a scratch declaration carrying the research record's sixteen rows, `--as file`
  refuses the bare surface, exits non-zero, and its message LISTS the thirteen declared `file` cells.
  This is §8's ratified F2 ruling being observed rather than merely recorded: the cell list is the
  clause that makes the refusal a menu rather than a wall, and rev-3 shipped that ruling with neither a
  scope bullet nor a criterion carrying it. The message is asserted to differ from AC10's malformed
  refusal.
- **AC12** — With a scratch declaration carrying `py.function snake vocab`, `--suggest buildUserIndex
  --as py.function` answers `build_user_index` and names the convention the input currently satisfies.
  Today `--suggest buildUserIndex` prints the OK line naming `build` as a verb the declaration
  carries, and returns at `lexicon.py:806` before any convention check runs, verified by
  direct run on this worktree at this rev. This is the CONVENTION-ONLY path — no banned suffix, no verb
  finding, nothing wrong but the case — which is the tool's quiet everyday case and which no criterion
  in rev-3 exercised: AC1 is a suffix hit, AC2 and AC4 are verb hits, AC5 grades a file stem, and AC6,
  AC7, AC9, AC10 and AC11 are refusals. Staging a renderer wired only into the banned-verb branch
  leaves this criterion RED while every other one greens; that RED is observed and unstaged before this
  unit is called done, and it is the failing case for the `:806` exit specifically.

## 7. Gates

`lexicon wiring` (guard `[]`, ceiling 330) is the leg that catches the template and Skill drift, and it
runs on every bar. `lexicon naming predicates` (guard `tools/`, `skills/session-kickoff/`, `.githooks/`,
`.claude/`, chunk `declarations`, ceiling 300) must stay green, and the claim is now backed rather than
asserted: the two identifiers this unit mints are in §4's `### Identifiers this unit mints` with their
`--suggest` verdicts, both lead with a declared verb, and the pin delta is zero. A commit editing
`tools/lexicon/lexicon.py` selects that leg, so the push bar runs it. `lexicon selftest` (guard
`tools/lexicon/`, chunk `selftests`, ceiling 880) carries the arms, and it is invisible to the push
boundary unless `GATE_SELFTESTS=1` is set, which no boundary sets. `memory-tree hygiene` grades this
spec.

**`codebase-map coverage + freshness` is the leg rev-3 omitted, and it is UNGUARDED.** Read from
`tools/gate-legs.json` at this rev's base: chunk `declarations`, subject `repo`, ceiling 300, and NO
guard key at all, where both of its codebase-map neighbours carry one. So nothing scopes it off any
bar. Its `test_generated_artifacts_are_fresh` arm byte-compares `memory/map/generated/symbols.json`
against a live re-render, and that artifact already carries `leading_verb` and `subtokens` rows for
`tools/lexicon/subtokens.py`, so S6's `render_convention` reds this leg at the push boundary unless the
artifact is regenerated in the same commit. Its coverage arm does not move: the ten inventories hold no
Python-symbol keys. `TOOL-aSurfacedLexicon-2`'s AC9 is the in-build precedent for enumerating the
unguarded legs a unit's populations touch, and it names this same leg.

No new leg, so no ceiling and no `testsuite-count-waivers.txt` row is owed.

## 8. Open questions

- **F1 — What does the re-caser do with characters `subtokens()` cannot see?**
  The splitter drops anything outside `[A-Za-z0-9]`, so `create$data` has no lossless round trip
  through it. Option A refuses to re-case such a name and prints only the verb or suffix finding, which
  keeps the tool from ever inventing a spelling but degrades the answer for a name the author can still
  fix by hand. Option B re-cases the subtokens it can see and splices the unseen characters back at
  their original offsets. That mechanism is not merely riskier, it is UNDEFINED: a re-case changes the
  string's length — `fetch_v2_data` is 13 characters and its camel target `loadV2Data` is 10 — so
  "their original offsets" names positions that do not exist in the output. B therefore fails AC4 as
  written on every one of its three arms, not only on the hard one.
  Recommendation: option A, with the reason printed. The rationale first written here — that B is "a
  second place where an offset can be wrong" — is REFUTED and does not carry the pick: the spans come
  free from `_SUBTOKEN_RE.finditer`, in `tools/lexicon/subtokens.py`, the file S6 already names, so
  there is no second offset computation to get wrong. AC4 is the reason that holds, and the measured
  history at `lexicon.py:810-823` is two review rounds spent on exactly this splice.

- **F2 — Does `--as` accept a bare surface, or require the full `<ext>.<surface>` cell?**
  A bare surface reads better in the Skill's routing line and in a session's prose. The full cell is
  unambiguous on a repo that arms two languages, which is every adopter this rebuild is for.
  "There is no measurement that decides it" was this fork's first wording and it is REFUTED; two bear
  on it. Counting the `CELLS:` block `TOOL-aSurfacedLexicon-4` proposes, by surface, gives `type` 1
  cell, `function` 2 and `file` 13 of which 5 are dark, 16 in all and every full key unique — so a bare
  surface would need an ambiguity policy that VARIES BY SURFACE, silent on `type` and forced on `file`.
  That favours the recommendation harder than this fork claimed. The second measurement cuts the other
  way and is a real cost the pick carries: `--as <none>.file` is a shell redirect, `bash -c 'echo --as
  <none>.file'` printing `bash: line 1: none: No such file or directory`, and `<` is reserved in
  PowerShell, so exactly one of the sixteen declared cells is unquotable by default.
  Recommendation: require the full cell, and reject a bare surface with a message listing the declared
  cells that carry it. The list makes the refusal a menu rather than a wall.

**RESOLVED (agent, 2026-09-04, delegated): F1 — option A, refuse to re-case a name the round trip
cannot carry and print the verb or suffix finding with its reason; with two corrections that are
binding, not optional.**

Option B falls to veto 1, failing AC4 as written. Its mechanism is undefined: a re-case changes the
string's LENGTH, so "their original offsets" names positions that do not exist in the output —
`fetch_v2_data` is 13 characters, its camel target `loadV2Data` is 10, and its unseen characters sit
at input offsets 5 and 8. On all three names AC4 enumerates, B either produces garbage or has no
defined answer, so it fails "each answer preserves the characters the splitter cannot see" on every
arm, where A fails at most one. B also deletes a declared error state — §5 lists "the lossless
round-trip refusal of F1" among them — so taking it forces a §5 edit that REMOVES a refusal. Vetoes
2 and 3 do not reach it: no dependency, no install location, no carrier, and §5 records the security
surface as one identifier in, one line out.

A is the sole survivor and is the richer answer besides, satisfying AC1, AC2, AC3, AC5, AC6, AC7 and
AC8 outright. The two corrections keep it from re-landing the defect §1 says the unit exists to
remove. (1) THE RENDERER IS SPAN-ANCHORED: build from `_SUBTOKEN_RE.finditer` spans, keep each
token's ORIGINAL surface wherever it already satisfies the target convention, and never regenerate a
byte outside a span. Without this, A re-cases `getUserURLs` — which has ZERO unseen characters, 11
of 11 covered — from lowercased subtokens and returns `readUserUrLs`, the exact historical breakage
AC4 pins, reproduced by replaying the round-1 body from 468e8912. (2) THE REFUSAL PREDICATE IS
NARROWED to "an unseen character the target convention does not itself re-supply": separators are
re-supplied, `$` and `é` are not. Of the 16 shape-preservation rows in the self-test, 11 carry
unseen characters and every one is a separator, so the unamended predicate would refuse
`--suggest fetch_remote --as js.function` and hand back `load_remote`, a name the camel predicate
reds — verbatim the surface-blind suggestion §1 names, on every separator-bearing name.

With both corrections all three AC4 names land: `create$data` refuses and falls back to today's
already-lossless slice (`build$data`), `fetch_v2_data` re-cases to `loadV2Data`, `getUserURLs` keeps
its token surfaces and swaps only the verb. A staged subtokens-rebuild re-caser reds all three.

Note for the record: option B's stated hazard, "a second place where an offset can be wrong", is
avoidable by construction — `finditer` already yields the spans, in the file S6 already names — so
the spec's reason for preferring A does not hold, and AC4 is the reason that does.

**RESOLVED (agent, 2026-09-04, delegated): F2 — `--as` requires the full `<ext>.<surface>` cell and
refuses a bare surface with a message listing the declared cells that carry it.**

NO OPTION IS VETOED, and that changes the shape of the ruling. Veto 1: no acceptance criterion names
a bare surface — AC1, AC2, AC4, AC5 and AC6 each pass a full cell — so accepting a bare surface
ADDITIVELY keeps all of them green; only a bare-ONLY reading would break them, and that is not what
the fork proposes. §3's non-goals are untouched: both forms resolve from the declaration alone and
neither adds the corpus walk `run_suggest`'s docstring forbids, the refusal menu included, since a
menu is a read of declared rows. Veto 2: both define the same new public surface, the `--as` flag,
which S1 commits to independently of this fork. Veto 3: no write surface either way. So the pick is
feature-richness and the tie-breaks.

On acceptance criteria the two tie at 8 of 8. Tie-break one — fewer open questions — decides it, and
the surface census is what makes it decisive. Counting the proposed CELLS block by surface: `type` 1
cell, `function` 2, `file` 13 of which 5 are dark, with all 16 full keys unique. A bare surface must
therefore ship an ambiguity policy for a 13-way and a 2-way case while being silently unambiguous
for a 1-way case — behaviour that VARIES BY SURFACE, which is worse than either uniform answer and
is a question the fork does not pose. It gets worse forward: `TOOL-aSurfacedLexicon-13` puts the
prefix/decorator selector ON the cell row key, so keys grow a third component and bare surfaces get
more ambiguous, not less. The full cell is forward-compatible with that; the bare form would have to
be re-decided. Tie-break two agrees — the argument IS the CELLS row key, one lookup against an
existing seam, where the bare form needs a new surface-to-cells index.

The recommendation stands but its stated reason does not. §8 says "There is no measurement that
decides it"; that is false in both directions. The census above is one measurement and favours the
recommendation harder than the spec claims. The other cuts against it and nobody has raised it:
`--as <none>.file` is a shell redirect — `bash -c 'echo --as <none>.file'` prints `bash: line 1:
none: No such file or directory`, and `<` is reserved in PowerShell — so exactly one of sixteen
declared cells is unquotable by default. It does not sink the full-cell form, but it is a real cost
the pick carries rather than a wash. The third stated reason, that a bare surface reads better in
the Skill's routing line, is a judgement and is set aside.

Residual: this entire fork is downstream of a unit that has not landed. There is no `CELLS:` block
in the tree, so every measurement here is against `TOOL-aSurfacedLexicon-4`'s proposal; if that lands
with a different key shape, the tie-break moves with it and this ruling should be re-run rather than
inherited.

**CORRECTION to the ruling above, rev-4. The census is right, its ATTRIBUTION is wrong, and its
re-run trigger is too narrow.** The block counted is not `TOOL-aSurfacedLexicon-4`'s: that spec ships
the grammar and no rows, and its own Migration says the conf rewrite pasting the real `CELLS` and
`PINS` bodies is a later unit. Its S3 also declares FOUR surfaces where the census has three, dropping
`constant`. The block actually counted is the REBUILD RESEARCH RECORD's, at
`memory/builds/aSurfacedLexicon/build/2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md`
lines 348-363. Re-derived at this rev's base rather than carried: 16 rows, all 16 full keys unique,
`type` 1, `function` 2, `file` 13 of which 5 are `dark`. The figures reproduce exactly, so the
tie-break stands as ruled.

The POPULATION the census describes is superseded, and that is the half worth fixing. Two owner
overrides arm cells the proposed block does not carry: Q5 arms `sh.function`, landing tracked with
`TOOL-aSurfacedLexicon-14` at order 4, and Q6 arms `py.constant`, landing with
`TOOL-aSurfacedLexicon-6` at order 4 — both BEFORE this unit. Correcting for them does not move the
ruling: `py.constant` is another one-cell surface and `sh.function` makes `function` a three-way, which
strengthens the varies-by-surface argument rather than weakening it. The Residual's re-run trigger is
therefore WIDENED from "a different key shape" to ANY change in the declared cell set — arming two
cells is not a key-shape change, and under the old trigger a reader would have inherited a stale count
without a signal.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The two today-behaviours in §4 were re-run on this worktree at
  writing time rather than quoted from the research record.
- rev-2 · 2026-09-04 · cross-spec audit: `order` moved from 5 to 6. §3 already states that
  `TOOL-aSurfacedLexicon-7` must land first or S4 has nothing to re-case, and the two units carried the
  same order value, which put a hard dependency inside a parallel group.
- rev-3 · 2026-09-04 · F1 ratified as option A (refuse rather than splice), with two binding
  corrections now written into §4, §5 and §6 rather than left in the mark: the renderer builds from
  `_SUBTOKEN_RE.finditer` spans and never regenerates a byte outside one, and the refusal fires only on
  an unseen character the target convention does not itself re-supply. F1's own test is corrected —
  `getUserURLs` carries no unseen characters yet still breaks under a lowercased-subtoken rebuild, so
  the risk classes are three (re-supplied separators, non-separator bytes, and case inside `[A-Za-z]`),
  not two. Option B's splice mechanism is UNDEFINED rather than merely riskier, because a re-case
  changes length, so it fails AC4 on every arm; §8's stated reason for preferring A, a second offset to
  get wrong, is struck as refuted and AC4 put in its place. §5's error-state row now carries the
  narrowed refusal and its testing row records the second observed-RED it owes. AC4 asserts the three
  answers by value. AC7's cite is corrected from `subtokens.py:29-38` to `:29` with the contract
  sentence at `:32-34`, and the docstring's own `1` example recorded as false — `leading_verb("1")`
  returns `"1"`. F2 ratified as the full `<ext>.<surface>` cell; its "there is no measurement that
  decides it" is struck as false, the proposed block's surface census (`type` 1, `function` 2, `file`
  13, 16 keys) forcing a per-surface ambiguity policy, and `--as <none>.file` recorded as unquotable by
  default in bash and PowerShell. §3 now records that `TOOL-aSurfacedLexicon-13` grows the cell key to
  three components, and §4 that no `CELLS:` block exists yet, so F2 is re-run rather than inherited if
  the key shape lands differently. The in-tree comment's `_load_h_conf` example is flagged in §4 as not
  reproducing. Base re-pinned from `d0a18683` to `6c670b02`, the tree every figure in this rev was
  measured on.
- rev-4 · 2026-09-05 · spec-audit round 1 folded; fifteen findings whose subject is this unit, one of
  them the blocker. THE BLOCKER: AC1, AC2, AC4, AC5 and AC6 each named a cell undeclared at this unit's
  own build order, so every one would have hit this unit's own S2 undeclared-cell refusal instead of
  the behaviour it asserts. §6 now opens with `TOOL-aSurfacedLexicon-5`'s scratch-declaration preamble
  and every criterion naming a cell names the declaration it is measured against; §4 gains
  `### What is armed at this unit's own build order`, read out of the owning specs — `py.constant` from
  `TOOL-aSurfacedLexicon-6` and `sh.function` from `TOOL-aSurfacedLexicon-14`, both at order 4, are the
  whole tracked population at order 6, and the full matrix is `TOOL-aSurfacedLexicon-12`'s S14 at order
  7. Keeping `--as` required at order 6 is recorded as a declared consequence with its cost, and the
  standing tracked-declaration answers are named as DEFERRED to order 7. §4's `### Rollout` now
  sequences this unit AFTER `TOOL-aSurfacedLexicon-11` within order 6 on their write-set intersection
  inside `run_suggest`, per BUILD-METHOD M6, and records that the generated `Parallel` column derives
  from step cardinality alone per `TOOL-aSurfacedLexicon-17`; that sibling owes the mirror sentence and
  does not carry it. Four new criteria: AC9, AC10 and AC11 compare the refusal MESSAGES that S2
  declares distinct — undeclared, malformed and the bare surface, the last being §8's ratified F2
  ruling reaching acceptance for the first time — and AC12 grades the convention-only path, the tool's
  quiet everyday case, which no criterion reached. S2 grows from three refusals to four; §5's
  error-state row is reconciled to six and had listed a different three. AC5 is rewritten with named
  inputs and named answers, and new S8 states what a `file` cell's argument IS and reduces it through
  `TOOL-aSurfacedLexicon-5`'s `read_stem` rather than through `_SUBTOKEN_RE`, which cannot compute that
  stem. New S9 states how a selector'd row participates, and §3's tense is corrected —
  `TOOL-aSurfacedLexicon-13` is order 5 and lands BEFORE this unit, so its key grammar already exists.
  §4's `### Inventory` now lists all four `run_suggest` exits with their line ranges, because rev-3
  named one and AC1 does not reach it, and gains a mint table carrying `render_convention` and
  `resolve_cell` with their cells, their `--suggest` verdicts and a measured pin delta of ZERO against
  `VERB_OFFENDER_PIN` at 461. §7 adds the unguarded `codebase-map coverage + freshness` leg and §4's
  Files touched adds `memory/map/generated/symbols.json`, whose freshness arm S6's new definition reds;
  `tools/lexicon/kit.toml` LEAVES both S7 and that list, since a literal flag introduces no
  placeholder. S3's arm ordering is recorded as defensive over a population no declaration populates,
  0 of 16 proposed rows arming both. §4's SPAN-ANCHORED absolute folds in its separator carve-out
  instead of being contradicted by the paragraph beneath it. §5's i18n row cites
  `TOOL-aSurfacedLexicon-16` and drops a landing precondition that was already filed. §8 gains a
  correction re-attributing F2's census to the research record's lines 348-363, re-derived here, and
  widening its re-run trigger from a changed key shape to any change in the declared cell set.
- rev-5 · 2026-09-05 · the outstanding-obligation sentence about `TOOL-aSurfacedLexicon-11` corrected: that
  spec carries its half, discharged in the same batch that recorded the debt. Cross-spec rev pins
  dropped in favour of the id alone, since a sibling's rev number rots within the hour here.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "re-case an identifier to a declared naming convention for
one surface cell"` returned no seam for the re-casing direction. Its ranked candidates are
`extract_declarations`, `raw_write_cells` and `case_collisions [tools/gate-lint/ps-hygiene.py]`, none
of which renders a name into a convention — `case_collisions` detects case-insensitive identifier
clashes in PowerShell and shares only the word. No existing seam fits, and the evidence is that
`tools/lexicon/subtokens.py` is the kit's only case-aware code and it runs strictly in the lossy
direction, lowercasing at `:26`. The seam this unit DOES extend is `run_suggest` at
`tools/lexicon/lexicon.py:785-852`, whose case-inheritance block at `:837-846` is the code being
replaced rather than a seam being reused, and `TOOL-aSurfacedLexicon-5`'s classifier, whose affix rule
this unit's renderer must share.

Recall terms used: `python tools/memory-recall/query.py "why must a suggestion be surface aware rather
than inheriting the caller's case" --terms "lexicon suggest surface cell convention snake camel pascal
banned suffix re-case declaration refusal"` — 39 hits, the load-bearing one being the
`TOOL-dPromptedSeam-1` round-1 spec audit at minor m1, which records that one identifier's suggestion
proves nothing about the engine because `run_suggest` reads the declaration and nothing else.
