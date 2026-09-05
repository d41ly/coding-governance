# TOOL-aSurfacedLexicon-8 — `--suggest` becomes surface-aware and answers in the declared convention

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 6

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
`cmd_*` handlers and `test_*` arms.

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
convention to answer in and is wrong the moment it does. The comment above it, at `:810-823`, is the
constraint this unit must not break, and it is the reason S6 is not a one-liner: a round-1 fix that
rebuilt the tail from `subtokens()` returned `getUserURLs` as `readUserUrLs`, `fetch_v2_data` as
`load_v_2_data` and `create$data` as `build_data` with the `$` silently gone. Three answers that had
been correct before the fix.

`subtokens()` at `tools/lexicon/subtokens.py:23-26` lowercases, breaks acronym runs, splits on digit
boundaries and drops every character its regex cannot see. So the re-caser cannot be built by round-
tripping a name through it. What it can do is round-trip only where the round-trip is LOSSLESS, and
refuse otherwise. See F1.

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
  cell), plus the lossless-round-trip refusal of F1.
- observability — every refusal names the flag or the cell that caused it, so a caller never has to
  guess which of the three it hit.
- risks — the re-caser is the one place in this build that WRITES a name rather than grading one, so a
  bug here hands an author a wrong name with the tool's authority behind it. The round-2 regression
  corpus in AC4 is the mitigation and it is not optional.
- testing + left-shift gates — arms in `tools/lexicon/selftest.py` covering each cell arm and the three
  historical breakages by name; observed-RED is AC4.
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
  through `--suggest ... --as js.function`, each answer preserves the characters the splitter cannot
  see. Staging a re-caser that rebuilds the tail from `subtokens()` turns those arms RED in
  `tools/lexicon/selftest.py`; unstaging returns them to green. The RED is observed before this unit is
  called done.
- **AC5** — When `--as py.file` is passed, the answer is a snake stem and no leading-token check runs,
  because `py.file` carries neither `vocab` nor `notail` in the declaration.
- **AC6** — When `--as md.file` is passed, the run refuses naming the cell as `dark` rather than
  answering, and exits non-zero.
- **AC7** — When an identifier carrying no ASCII word characters is passed, the run refuses as
  ungradeable and re-spells nothing, preserving `leading_verb`'s contract at
  `tools/lexicon/subtokens.py:29-38`.
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
  their original offsets, which is more useful and is a second place where an offset can be wrong.
  Recommendation: option A, with the reason printed. The measured history at `lexicon.py:810-823` is two
  review rounds spent on exactly this splice, and a refusal that says why is cheaper than a third.

- **F2 — Does `--as` accept a bare surface, or require the full `<ext>.<surface>` cell?**
  A bare surface reads better in the Skill's routing line and in a session's prose. The full cell is
  unambiguous on a repo that arms two languages, which is every adopter this rebuild is for. There is no
  measurement that decides it: this repo arms `py` and `js`, so both forms are live here.
  Recommendation: require the full cell, and reject a bare surface with a message listing the declared
  cells that carry it. The list makes the refusal a menu rather than a wall.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The two today-behaviours in §4 were re-run on this worktree at
  writing time rather than quoted from the research record.
- rev-2 · 2026-09-04 · cross-spec audit: `order` moved from 5 to 6. §3 already states that
  `TOOL-aSurfacedLexicon-7` must land first or S4 has nothing to re-case, and the two units carried the
  same order value, which put a hard dependency inside a parallel group.

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
