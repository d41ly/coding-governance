# TOOL-dScaffoldedMirror-14 — the `t_` and `do_` renames, and `cmd` as a reserved row

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling

## 1. Goal

Seventy-nine of the 459 offender keys — 17% of the whole backfill — are two naming habits in seven
files, and neither is a judgment call. All 52 `t_*` are self-test arms in two selftests, and `test`
is already a declared verb meaning exactly that. All 27 subcommand entrypoints split `do_` in
memory-tree against `cmd_` in govkit for no reason anyone recorded. Renaming them and reserving one
row takes the backfill from 459 to 380 before any other decision is taken, and it is the cheapest
17% this build will ever get.

## 2. Scope (IN)

- **S1** — rename all 52 `t_*` definitions to `test_*`: 29 in `tools/memory-recall/selftest.py`,
  23 in `tools/codebase-map/selftest.py`, with every in-file reference moved in the same edit.
- **S2** — delete the deliberate-inconsistency comment at `tools/memory-recall/selftest.py:1193-1196`
  and the state it describes, in the same commit. It names this unit's work in so many words:
  *"Renaming the siblings is that kit's shrink work, not this unit's."*
- **S3** — add `cmd` to the `VERBS` table in `.lexicon.conf` as a STRUCTURAL row beside `main`, with
  a negative definition, so it does not become the twelfth row lacking one.
- **S4** — rename all 22 `do_*` definitions in `tools/memory-tree/` to `cmd_*`, across five modules,
  with every in-file call site and every prose comment naming them.
- **S5** — lower `VERB_OFFENDER_PIN` from 463 to the derived post-rename count in the same commit,
  with the `<old> -> <new>` marker the conf already writes by hand for a movement.
- **S6** — regenerate `memory/map/generated/symbols.json` in the same commit; 22 of its rows name a
  `do_*` symbol today.
- **S7** — state on the record what is NOT renamed and why: govkit's five `cmd_*` are already the
  target spelling, and the frozen records under `memory/` that cite `do_*` are not rewritten.

## 3. Non-goals (OUT)

- **No other rename.** The remaining 380 keys are `-9`'s grandfather set and `-8`'s canon work. A
  unit that starts renaming on judgment does not stop at a defensible line.
- **No new verb beyond `cmd`.** `do` is refused, and refusing it is half the ruling.
- **`.lexicon.conf`'s pin archaeology is not rewritten.** Those ~70 lines are dated notes about past
  raises, three of which name identifiers this unit deletes. They are records of what was true when
  written, and `-9` removes the block entirely; churning it now is work on a file scheduled for
  deletion.
- **No structured `NOT` grammar.** `-8` owns the parsed negative-definition format and the 11
  backfilled clauses. S3 writes its clause in today's prose format so `-8` inherits 23 rows in one
  shape rather than 22 plus an exception.
- **No pin mechanism change.** The pin is still an integer and still raisable; `-9` deletes it. This
  unit only moves it down.

## 4. Design

### The ruling: `cmd`, not `do`, and not carried as debt

`main` is already reserved as a module's CLI entry point. A subcommand handler is that same role one
level down, so `cmd` names the role while `do` names nothing — `do_check` and `do_write` tell a
reader they do something, which every function does. Admitting `do` would also be the table's first
pure synonym row, and the table's whole value is that "which verb is this?" has one answer. `cmd` is
the more expensive rename by 22 definitions against 5, and it is taken anyway, because the cheaper
direction buys a worse table. Agent-defaulted 2026-08-24 with the owner declining to override.

### The call-site inventory, verified rather than assumed

Every reference was counted on this worktree at base `9ddcc5c9`. Renaming a dispatch handler moves
whatever names it, so the question is where the names are read.

| file | defs | refs | how the names are read |
|---|---|---|---|
| `tools/memory-recall/selftest.py` | 29 `t_` | 59 | decorator at import, plus a roster |
| `tools/codebase-map/selftest.py` | 23 `t_` | 47 | explicit `check(name, fn)` arguments |
| `tools/memory-tree/gotchas.py` | 6 `do_` | 36 | argv dispatch, arms, prose |
| `tools/memory-tree/gen_build_index.py` | 5 `do_` | 28 | argv dispatch, arms, prose |
| `tools/memory-tree/check-arms.py` | 4 `do_` | 24 | argv dispatch, arms, prose |
| `tools/memory-tree/row_grammar.py` | 4 `do_` | 12 | argv dispatch, arms, prose |
| `tools/memory-tree/corpus_ids.py` | 3 `do_` | 6 | argv dispatch, arms, prose |

`memory-recall`'s `@check("…")` decorator runs each arm at definition time, so the name is not read
there — but `main` carries an `order` roster listing all 34 arms by name (`:1312-1325`) under a
`len(order) == len(_checks)` arity assert, and that roster is the second call-site class.
`codebase-map` names each arm as an argument to `check(name, fn)`, seven directly and the rest
wrapped in a `lambda:`.

Every reference is in the same file as its definition. There is no dispatch table keyed on the
function name, no `getattr` lookup, and no cross-module import of any of the 74 names. A partial
rename cannot land silently in either selftest: `memory-recall`'s `order` roster and
`codebase-map`'s explicit `check(name, fn)` arguments both raise `NameError` at import if a
definition moved and its reference did not.

**Collisions: none.** After the rename neither selftest defines a duplicate name, and no memory-tree
module already defines the `cmd_*` a `do_*` maps to — verified by comparing the mapped def sets
against the existing ones per file.

**The CLI surface does not move.** Subcommand strings are argv literals compared in each module's
`main`; the handler's name is not derived from them. `bash tools/run-gates/run-gates.sh` invokes
`--selftest`, `--check`, `--report` and friends, none of which change.

**pytest collection does not move.** This repo declares no `python_files` override — there is no
`pytest.ini`, `pyproject.toml`, `setup.cfg` or `tox.ini` in the tree — so pytest's default file
pattern does not match `selftest.py`. Promoting 52 functions to `test_*` does not make them
collectable anywhere.

### The `refusal_join.py` anchors: they do not move, and here is the second reason

`tools/govkit/refusal_join.py` anchors every refusal branch on `(module, enclosing function, ordinal
within that function)`, chosen so an anchor survives an edit above it where a line number would not.
Its population is `git ls-files tools/govkit/*.py` minus a three-file harness (`:53-57`). Two
independent reasons this unit moves no anchor: `tools/memory-tree/` is not in that population at all,
and govkit's five `cmd_*` are not renamed here.

Measured for the next author rather than for this one: 69 of the file's 161 pinned branches sit
inside those five functions — `cmd_check` 24, `cmd_apply` 31, `cmd_update` 10, `cmd_intake` 4. So a
future rename in `govkit.py` would re-key 43% of the anchor set, and it would do it SILENTLY: the
join half has never executed, because nothing in the tree passes a reached-set (the file says so at
`:41-45`, filed as `TOOL-dUnstalledConvoy-36`), and neither count pin moves when a name changes.
That is a real hazard and it is written here because this unit is the one that went looking.

### The arithmetic, and where each number comes from

Measured 2026-08-24 with the shipped checker on this worktree. `python tools/lexicon/lexicon.py
--list` reports **463** verb occurrences over **459** distinct `path::name` keys over **395**
distinct bare names, and `--measure` prints `VERB_OFFENDER_PIN="463"`.

| | occurrences | `path::name` keys |
|---|---|---|
| today | 463 | 459 |
| 52 `t_` renamed to `test_` | −52 | −52 |
| 22 `do_` renamed to `cmd_` | −22 | −22 |
| 5 `cmd_` legalised by S3's row | −5 | −5 |
| after | **384** | **380** |

The 5 govkit `cmd_*` are offenders today (`govkit.py:1429,1463,2208,2918,3170`) and stop being
offenders when the row lands, without being touched. The pin compares occurrences
(`lexicon.py:537`), so S5 moves it 463 → 384; the 459 → 380 figure is the backfill `-9` inherits and
is keyed differently.

### Migration: the frozen records are not rewritten

`do_*` appears in seventeen tracked records under `memory/` — specs, reviews and build READMEs from
`aLoosenedCeiling`, `aDeclaredCeiling`, `aDrainedSluice`, `aCandidStub`, `aFoldedQuarry`,
`cKeyedLaunchpad` and others. None is touched. A record states what was true when it was written,
and editing a landed spec so it agrees with today's tree is precisely the rewrite the append-only
rule forbids. After this unit those records cite names that no longer exist, which is correct and is
said out loud here so a later reader does not "fix" them.

`memory/map/generated/symbols.json` IS regenerated, because it is derived and carries a generator
banner saying so. The two are not the same class: one is a record, the other is an artifact.

### Files touched (estimate)

`tools/memory-recall/selftest.py`, `tools/codebase-map/selftest.py`, five modules under
`tools/memory-tree/`, `.lexicon.conf` (one `VERBS` row, one pin value, one movement note), and the
regenerated `memory/map/generated/symbols.json`. Roughly 210 reference sites, all mechanical.

### Alternatives rejected

- **Reserve `do` instead and rename govkit's five.** Cheaper by 17 renames and it buys a table whose
  first synonym row is a verb that names no role. The cost difference is one edit session; the table
  is permanent.
- **Waive the 79 keys.** Under `-9` the waiver becomes the only remaining dodge, and 79 waivers for
  a mechanical rename is exactly the waiver pile `TOOL-dScaffoldedMirror-19` refuses on the noun-led
  population.
- **Carry them into the grandfather set as debt.** They would be permanently legal and permanently
  wrong, and every one is a one-line rename with no cross-file caller.

## 5. Production-readiness checklist

- **security** — N/A. No input, no write path, no privilege surface; the renamed functions are
  self-test arms and CLI handlers whose argv contract is unchanged.
- **perf / scale** — N/A. Identical code paths under different names; no measurable delta.
- **a11y** — N/A. CLI tooling.
- **i18n** — N/A. Identifiers are ASCII before and after.
- **error / empty / loading states** — N/A for the rename itself. One state does change: five
  offenders disappear from `--list` output because a table row legalised them, which is a legal
  transition and is visible in the count.
- **observability** — the pin movement note in `.lexicon.conf` is the observability. A pin that
  moves without a `<old> -> <new>` line beside it is the class `-5` exists to ratchet.
- **risks** — a partial rename is the only real one, and both selftests are structurally protected:
  `memory-recall`'s `order` roster and its `len(order) == len(_checks)` arity assert, and
  `codebase-map`'s `check(name, fn)` arguments, all raise at import rather than passing quietly. The
  memory-tree modules have no equivalent guard, so their arms are the check — AC3 names them.
- **testing + left-shift gates** — no new arm is written and none is needed: this unit is exercised
  by the suites it renames. The left-shift already exists as the `lexicon naming predicates` leg,
  which reds if a `t_` or `do_` reappears above the lowered pin.
- **migration / rollback** — the frozen-record decision is in §4 and is the only migration question.
  Rollback is a revert of one commit; nothing is persisted outside the tree.
- **user docs** — none. No user-facing behaviour changes; the CLI verbs are byte-identical.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "^def t_" -- '*.py'` runs after this unit, it matches nothing, and
  `git grep -n "^def do_" -- '*.py'` matches nothing.
- **AC2** — When `python tools/memory-recall/selftest.py` and `python tools/codebase-map/selftest.py`
  run, both pass and print the same executed-assertion counts as at base `9ddcc5c9`, so the rename
  moved names and not arms.
- **AC3** — When `python3 tools/memory-tree/gotchas.py --selftest`,
  `python3 tools/memory-tree/gen_build_index.py --selftest`,
  `python3 tools/memory-tree/corpus_ids.py --selftest`,
  `python3 tools/memory-tree/row_grammar.py --selftest` and
  `python3 tools/memory-tree/check-arms.py --selftest` each run, all five pass with unchanged
  counts — these five modules carry the 22 renamed handlers and no import-time roster to catch a
  miss.
- **AC4** — When `python tools/lexicon/lexicon.py --measure` runs after the change, it prints
  `VERB_OFFENDER_PIN="384"`, and `python tools/lexicon/lexicon.py` exits 0 against the lowered pin
  in `.lexicon.conf`.
- **AC5** — When `python tools/lexicon/lexicon.py --list` runs, no line names a `t_`, `do_` or
  `cmd_` identifier, and the `cmd` row in `.lexicon.conf` carries a negative definition rather than
  a bare gloss.
- **AC6** — When `python tools/codebase-map/gen_map.py --write` runs after the commit, it leaves the
  tree clean, and `python3 tools/codebase-map/test_codebase_map.py` is green — the freshness leg
  proves `symbols.json` moved with the code.
- **AC7** — When `python tools/govkit/refusal_join.py` runs after the change, it reports the same
  branch count and module count as at base `9ddcc5c9`, confirming that no anchor moved.
- **AC8** — When `tools/memory-recall/selftest.py` is read, the deliberate-inconsistency comment at
  `:1193-1196` is gone, because the inconsistency it justified is gone. A comment explaining a state
  that no longer exists is the stale-prose class this build keeps finding.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory-recall kit
selftest`, `codebase-map kit selftest`, `codebase-map coverage + freshness`, `govkit refusal join`,
`build-index selftest`, `corpus-ids selftest`, `gotchas selftest`, `row-grammar selftest`,
`check-arms selftest`, `harness arms (fail branches armed or pinned)`, `memory hygiene`. Adds no
leg: this unit's regression protection is the existing `lexicon naming predicates` leg at a lower
pin, which is the correct shape — the leg count is not the coverage.

**What this unit does NOT check.** It does not verify that any renamed arm still tests what its name
claims. The gates prove the arms run and pass, not that they assert the same thing, and a rename
that also mangled a body would show as green. The protection there is that the edit is mechanical
and reviewable as one diff, which is a documented check and not a machine one.

## 8. Open questions

- **F1 — `cmd` or `do` as the reserved row?** Priced in §4. RECOMMENDATION: `cmd`, accepting the
  more expensive rename, because `main` already reserves the module-level CLI entry point and a
  subcommand handler is that role one level down. RESOLVED (agent, 2026-08-24, delegated): `cmd`,
  with govkit's five existing `cmd_*` left untouched and memory-tree's 22 moved to join them.
- **F2 — does the pin drop to 384 in this commit, or wait for `-9` to delete it?** RECOMMENDATION:
  drop it here. `-9` is Phase 4 and may not land; leaving a pin 79 above its population is a ceiling
  that absorbs 79 free offenders in the meantime, which is the exact defect this build was
  commissioned over. RESOLVED (agent, 2026-08-24, delegated): lower to 384 in the same commit, with
  the movement note.
- **F3 — are the seventeen frozen records naming `do_*` left to rot?** RECOMMENDATION: yes, and say
  so in this spec rather than in a commit message, which is what §4 does. They are append-only
  records of past states. RESOLVED (agent, 2026-08-24, delegated): not rewritten; the generated
  `symbols.json` is regenerated because it is derived, and the distinction is stated on the record.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, owner question
  Q4 and its agent default) and on the read-only probe of `incms/main` taken the same day. Call-site
  and collision inventories re-verified against this worktree at writing time.
- rev-1 status 2026-08-24 · KEPT whole. The review rates this the second-most valuable unit in the set: it is the only one that makes this repo's NAMES better rather than making the machinery that judges them bigger, and it drops the offender count 463 -> 384 by doing the work rather than by moving a number.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py rename subcommand dispatch selftest entrypoint` returns
`do_selftest` (`tools/memory-tree/row_grammar.py`, fan-in 4, SEAM) as its only symbol candidate, and
that is a subject of this unit rather than a seam it wires through — the lookup found the population
being renamed, which is the correct answer to a rename and not a reuse opportunity. The remaining
hits are gate-leg inventory keys (`build-index selftest`, `check-arms selftest`, `gotchas selftest`
and eight siblings), which name the legs §7 must keep green and supply no mechanism. **No existing
seam fits, and none should**: a rename introduces no behaviour, so there is nothing to route through
a helper. The lookup's one substantive contribution is negative and worth recording — it surfaced no
consumer of any renamed name outside the module that defines it, which agrees with §4's grep-level
inventory. The inventory is the evidence; the lookup is a second route to the same answer, and the
`do_selftest` fan-in it reports is a name defined independently in five memory-tree modules rather
than a caller graph, so it is not read here as proof of anything.
