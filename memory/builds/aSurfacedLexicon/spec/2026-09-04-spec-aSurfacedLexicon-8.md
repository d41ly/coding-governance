# TOOL-aSurfacedLexicon-8 — `--suggest` becomes surface-aware and answers in the declared convention

**Status:** SPECCED · rev-3 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

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
- **S2** — `<cell>` resolves against the `CELLS:` block. An undeclared cell, a `dark` cell and a
  malformed cell are each a distinct named refusal. `TOOL-aSurfacedLexicon-4` owns the block grammar;
  this unit is a reader of it.
- **S3** — On a cell carrying `notail`, the name's TAIL is checked against `BANNED_SUFFIXES` before the
  leading token is looked at, and a hit is reported with the banned suffix named. `--suggest FooManager
  --as py.type` answers about `Manager`.
- **S4** — On a cell carrying `vocab`, the leading-token path runs as
  `TOOL-aSurfacedLexicon-7` leaves it, and its result is re-cased to the cell's declared convention
  before printing.
- **S5** — A name that violates the cell's convention but breaks no other predicate still gets an
  answer: the re-cased spelling of the same name, with the convention it currently satisfies named,
  matching the message shape the convention-predicate probe already observed.
- **S6** — The renderer that turns subtokens back into a declared convention lands in
  `tools/lexicon/subtokens.py`, beside `TOOL-aSurfacedLexicon-5`'s classifier. It is the inverse of
  that classifier and shares its affix rule, so the two live in one file or they drift.
- **S7** — `tools/lexicon/SKILL.template.md:19` and its description line gain `--as <cell>`, and
  `tools/lexicon/kit.toml:38`'s placeholder list follows.

## 3. Non-goals (OUT)

The convention classifier itself, which is `TOOL-aSurfacedLexicon-5` — this unit consumes
`classify()` and adds only the inverse direction. The `CELLS:` and `PINS:` grammar, which is
`TOOL-aSurfacedLexicon-4`. The canon graft into the verb path, which is `TOOL-aSurfacedLexicon-7` and
must land first or S4 has nothing to re-case. The prefix and decorator selector, which is
`TOOL-aSurfacedLexicon-13` and is the mechanism that would let one cell answer differently for
`cmd_*` handlers and `test_*` arms. That unit puts the selector ON the `<ext>.<surface>` row key, so
cell keys grow a THIRD component after this unit ships, and any reading of `--as` that is ambiguous
today gets more ambiguous then, not less.

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

There is no `CELLS:` block in the tree at this rev — `grep -rn "CELLS" .lexicon.conf tools/lexicon/`
returns nothing — so every statement here about cell keys is measured against the block
`TOOL-aSurfacedLexicon-4` proposes. If that unit lands a different key shape, F2's tie-break moves
with it and must be re-run rather than inherited.

Verified today by direct run on this worktree:

| Invocation | What it prints today |
|---|---|
| `--suggest FooManager` | `` `foo` is not in the declared table, and no row bans it by name `` |
| `--suggest fetchUserData` | `` use `loadUserData` — the declaration says `load`, NOT `fetch` `` |

The first answers about the wrong end of the name. The second answers with a name that the convention
predicate `TOOL-aSurfacedLexicon-5` builds reds on a `py.function` cell, because `loadUserData`
satisfies camel and the cell declares snake.

### Inventory

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
ORIGINAL surface wherever that surface already satisfies the target convention, and never regenerates
a byte outside a span. That is binding rather than a preference. Running `_SUBTOKEN_RE.finditer` over
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

### Files touched (estimate)

`tools/lexicon/lexicon.py`, `tools/lexicon/subtokens.py`, `tools/lexicon/SKILL.template.md`,
`tools/lexicon/kit.toml`, the rendered Skill, and `tools/lexicon/selftest.py`. ESTIMATE on the size —
no case-rendering code exists anywhere in the kit to measure against, which the research record names
as one of the things it could not determine.

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
  re-cases on a truncated core and a fully non-ASCII one has no subtokens at all. It is filed as an
  unfiled review finding in the research record and needs its backlog row before this unit builds; this
  unit must refuse such a name rather than re-spell it. That refusal is AC7.
- error / empty / loading states — three distinct refusals (missing `--as`, undeclared cell, dark
  cell), plus F1's NARROWED refusal: an unseen character the target convention does not itself
  re-supply. A separator is re-supplied and never refuses. `$` and `é` do. The wide form of that
  predicate — any unseen character — is the one this rev rejected, because it refuses a plain snake
  name asked for in a camel cell.
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

- **AC1** — When `python tools/lexicon/lexicon.py --suggest FooManager --as py.type` runs, it names the
  banned suffix `Manager`. Today `--suggest FooManager` answers about `foo`, verified by direct run at
  writing time.
- **AC2** — When `python tools/lexicon/lexicon.py --suggest fetchUserData --as py.function` runs, it
  returns `load_user_data`. Today `--suggest fetchUserData` returns `loadUserData`, verified by direct
  run, and that name reds the `py.function` snake cell.
- **AC3** — When `python tools/lexicon/lexicon.py --suggest fetchUserData` runs with no `--as`, it
  exits 2 and the message names `--as`. The refusal is asserted on the exit code and on the text, so a
  future default cannot slip in past a test that only reads stdout.
- **AC4** — When the round-2 regression names `getUserURLs`, `fetch_v2_data` and `create$data` are run
  through `--suggest ... --as js.function`, each answer is asserted by VALUE: `create$data` refuses on
  the `$` and falls back to today's already-lossless slice `build$data`, `fetch_v2_data` re-cases to
  `loadV2Data`, and `getUserURLs` keeps every token surface and swaps only the verb. "Preserves the
  characters the splitter cannot see" was this criterion's first wording and it is NOT sufficient —
  `getUserURLs` has no such characters, 11 of its 11 covered by `_SUBTOKEN_RE.finditer` spans, and it is
  the name that broke — so the criterion is the three answers themselves. Staging a re-caser that
  rebuilds the tail from `subtokens()` reds all three arms in `tools/lexicon/selftest.py`; unstaging
  returns them to green. The RED is observed before this unit is called done.
- **AC5** — When `--as py.file` is passed, the answer is a snake stem and no leading-token check runs,
  because `py.file` carries neither `vocab` nor `notail` in the declaration.
- **AC6** — When `--as md.file` is passed, the run refuses naming the cell as `dark` rather than
  answering, and exits non-zero.
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

## 7. Gates

`lexicon wiring` (guard `[]`, ceiling 330) is the leg that catches the template and Skill drift, and it
runs on every bar. `lexicon naming predicates` (chunk `declarations`, ceiling 300) must stay green:
this unit adds no offender and moves no pin. `lexicon selftest` (chunk `selftests`, ceiling 880)
carries the arms, and it is invisible to the push boundary unless `GATE_SELFTESTS=1` is set, which no
boundary sets. `memory-tree hygiene` grades this spec. No new leg, so no ceiling and no
`testsuite-count-waivers.txt` row is owed.

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
