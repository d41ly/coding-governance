# KICK-dKeptSession-89 — the four names the first reconcile dropped from policy.py defined again at the tip, so the landing's merge-loss check clears

**Status:** INPROGRESS · rev-1 · 2026-11-24 · node d · Tier-1 · base 271522b2 · streams tooling · order 39 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-24-build-KICK-dKeptSession-89-widen-10.md](../build/2026-11-24-build-KICK-dKeptSession-89-widen-10.md) | widen | — |
| [2026-11-24-prompt-KICK-dKeptSession-89-1-spec-writer.md](../prompts/2026-11-24-prompt-KICK-dKeptSession-89-1-spec-writer.md) | journal | — |
| [2026-11-24-prompt-KICK-dKeptSession-89-build-brief.md](../prompts/2026-11-24-prompt-KICK-dKeptSession-89-build-brief.md) | research | — |
| [2026-11-24-prompt-KICK-dKeptSession-89-spec-brief.md](../prompts/2026-11-24-prompt-KICK-dKeptSession-89-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The lander refuses this run's landing. The lexicon kit's `--merge-losses` over the landing range
reads four definitions lost at merge `ad02f1a6a`, parent 1, in `tools/policy/policy.py`. This unit
defines the four names there again, over the code that does their work now, with no change of
behaviour, so the check counts each one `restored`.

## 2. Scope (IN)

- **S1** — In `tools/policy/policy.py`, `check_name_ledger` is renamed `check_shrink_list` and
  `write_name_ledger` is renamed `write_shrink_list`: the two definitions, every call, and every
  citation in that file and in `tools/policy/README.md`. Arguments, returns and refusals are unchanged.
  Observed by AC1, AC3, AC5.
  **Readers:** by name: `tools/policy/policy.py`, `tools/policy/README.md` and
  `memory/map/generated/symbols.json`, each rewritten by this unit; CLOSED specs and records keep the
  old spelling · by value: NO VALUE READERS, since each name is a function's and no code compares,
  counts or derives from it.
- **S2** — The base compare inside `check_shrink_list` is extracted as `read_shrink_base`, and the
  rewrite inside `write_shrink_list` as `write_shrink_file`, per §4 "The four functions".
  `check_legacy_homes` calls `read_shrink_base` in place of its own copy of that compare (§7 F1).
  Observed by AC2, AC3, AC4, AC5.
- **S3** — Each of the four carries a docstring stating what it does now, over a ledger population. None
  describes the plain-name list file main's side of the merge lacked, and the first's clause naming the
  earlier factory goes. Observed by AC2.
- **S4** — `memory/map/generated/symbols.json` is re-rendered by `python tools/codebase-map/gen_map.py
  --write`, with any other file that write moves under `memory/map/generated/`. Observed by AC6.
- **S5** — The lexicon kit's `--merge-losses` over the landing range clears the four losses at
  `ad02f1a6a` as `restored`. Observed by AC7.

## 3. Non-goals (OUT)

- Any change to `tools/memory-tree/legacy_ledger.py`, to what either function grades or writes, to a
  message any verb prints, or to a row of `tools/policy/catalogue.toml`.
- `write_legacy_homes`. Its rewrite keeps rows by whole key, not by name, so it is no second caller of
  `write_shrink_file`.
- The fifth function KICK-dKeptSession-69 S5 names, `read_base_pairs`. `--merge-losses` prints no LOSS
  line for it, so it stays absent.
- The old parameters. The names return; the list-file arguments `name`, `header` and `compare` do not.
- A `superseded:` line, a rewritten commit, or `git replace`.
- An edit to any CLOSED spec or ledger. KICK-dKeptSession-69's AC6 names these four absent, and §4 says
  why it still holds.
- An edit to `tools/policy/check_policy.py`, which spells none of the six names.

### Edges

- **consumes-from** external — the main loop's commit of this spec with the dKeptSession packet re-rendered over it by `python tools/chain-packet.py --write dKeptSession`, as KICK-dKeptSession-80 §3 took it; without it the packet join reds on a spec the packet does not carry

## 4. Design

### Evidence

Read 2026-11-24 at `271522b2`.

- `python tools/lexicon/lexicon.py --merge-losses "origin/main..HEAD"` printed four `LOSS ad02f1a6 parent
  1: tools/policy/policy.py:` lines, `check_shrink_list`, `read_shrink_base`, `write_shrink_file` and
  `write_shrink_list`, then `graded=68 skipped=0 paths=588 losses=4 masked=0 restored=0 superseded=0
  seconds=95.75`, exit 1. <!-- PINNED 2026-11-24 -->
- `tools/lexicon/lexicon.py#check_merge_losses` counts a candidate `restored` where the range tip defines
  its name at the lost path (`if path in at_tip or at_tip - old`,
  `tools/lexicon/lexicon.py@fbc2677e727a:4487`). A definition of each name in `tools/policy/policy.py`
  clears it. The other escape, a `superseded:` line, is read from the merge's own message, and that
  merge is published. TOOL-aTrimmedWait-19 cleared one loss by the same route, a real rename.
- The loss was deliberate (KICK-dKeptSession-69 S5), and the work moved to `check_name_ledger` and
  `write_name_ledger` (`tools/policy/policy.py@45911543ed4d:1485`,
  `tools/policy/policy.py@45911543ed4d:1527`), by that unit's S6.
- Outside `memory/builds/`, those two names are spelled in `tools/policy/policy.py`,
  `tools/policy/README.md` and `memory/map/generated/symbols.json` and nowhere else, by a grep over
  `tools/`, `skills/`, `help/`, `memory/map/`, `memory/project/` and `memory/guides/`.
- The callers are `check_unnamed_list`, `check_unpurposed_list` and `cmd_lists`, all in
  `tools/policy/policy.py`. The fixtures reach the two through those callers.
- `check_legacy_homes` holds the same four-line base compare, byte for byte, at
  `tools/policy/policy.py@45911543ed4d:1719` as the first function does at
  `tools/policy/policy.py@45911543ed4d:1515`.
- The pass and landing merges add no loss of the two old names. `check_merge_losses` skips a definition
  that is in the merge base and absent from the other parent, and neither name is on `origin/main`.
- `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for each of the four,
  and `python tools/codebase-map/gen_map.py --check` exited 0.

### The four functions

| Function | Holds |
|---|---|
| `read_shrink_base(repo, ll, reg)` | `ll.compare_to_base(repo, reg)` under its `ValueError` refusal, the `Refusal` text as it is. Returns the factory's `(findings, why)` unchanged, `findings` None where nothing is compared. Called by `check_shrink_list` and `check_legacy_homes`. |
| `write_shrink_file(repo, ll, reg, declared, keep)` | the one `ll.write_rows` call: the rows of `declared` whose name is in `keep`, sorted by key, each row's value as read. Returns nothing. |
| `check_shrink_list(repo, kit, population, derived, unlisted)` | the body of `check_name_ledger`, its base compare now one `read_shrink_base` call. |
| `write_shrink_list(repo, kit, population, derived)` | the body of `write_name_ledger`, its rewrite now one `write_shrink_file` call. Its registration, read and malformed-row refusals stay before that call. |

`ll` is the factory module and `reg` the registration, the pair `read_legacy_registration` returns, so
neither new function reads the registration again. The render of the findings stays in each caller, and
`write_rows`' own `ValueError` still reaches `cmd_lists` uncaught.

### KICK-dKeptSession-69's AC6

That criterion reads `git grep` over `tools/` and `help/` for these names and expects nothing. The
preamble of its §6, as of its rev-4, says a criterion naming no commit reads the reconcile commit,
`ad02f1a6a`. `git grep -n -e read_shrink_base -e write_shrink_file -e check_shrink_list -e
write_shrink_list -e read_base_pairs ad02f1a6a -- tools/ help/` printed nothing on 2026-11-24. So AC6
holds where it is read, and this unit's tip does not contradict it. What AC6 guards, one list factory,
holds at the tip too: the four names grade and write through `tools/memory-tree/legacy_ledger.py`.

### What it does not check

AC7 reads definitions by name. It would count four empty functions `restored` as readily as these, which
is why AC2 to AC5 read what they do.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_shrink_base`, `check_shrink_list` | function, `policy.py` | `py.function`, `read` and `check` verbs |
| `write_shrink_file`, `write_shrink_list` | function, `policy.py` | `py.function`, `write` verb |

### Migration

None: no stored data, argv or output changes. Reversal is a revert of the pass commit.

### Files touched (estimate)

- `tools/policy/policy.py`: S1 to S3
- `tools/policy/README.md`: S1
- `memory/map/generated/symbols.json`: S4
- `memory/builds/dKeptSession/build/2026-11-24-build-KICK-dKeptSession-89-1-acceptance-ledger.md`

### Alternatives rejected

- **Define the four as unused stubs or aliases.** It satisfies AC7 and leaves dead definitions.
- **Keep the two current names and add the four beside them.** Two names for one function.
- **A `superseded:` line.** The merge's message is published, so it would be a rewritten commit.

## 5. Acceptance criteria

`$S` is the pass's scratch directory, outside the tree.

- **AC1** — `git grep -n name_ledger -- tools/ help/` prints no line, and `grep -cE '^def
  (check_shrink_list|read_shrink_base|write_shrink_file|write_shrink_list)\(' tools/policy/policy.py`
  prints `4`.
  Red when: a call or citation keeps an old name, or one of the four is not defined.
  figure: 4 is PINNED 2026-11-24, one per LOSS line of §4 "Evidence".
- **AC2** — `python -c "import sys; sys.path.insert(0, 'tools/policy'); import policy; print([n for n in
  ('check_shrink_list', 'read_shrink_base', 'write_shrink_file', 'write_shrink_list') if 'population' not
  in (getattr(policy, n).__doc__ or '')])"` prints `[]`. Over `tools/policy/policy.py`, `grep -c 'the
  shrink-list factory made'` prints `0`, `grep -c 'compare_to_base(repo, reg)'` prints `1`, `grep -c '=
  read_shrink_base('` prints `2`, and `grep -c '^ *write_shrink_file('` prints `1`.
  Red when: a docstring is missing or still describes a list file, or the extraction copied a call and
  left the old one in place. At `271522b2` the compare call counts 2.
  figure: each count is PINNED 2026-11-24 by §4 "The four functions".
- **AC3** — Before the edit, `python tools/policy/policy.py lists --check` is written to `$S/before.txt`.
  After it, the same command written to `$S/after.txt` exits 0, and `cmp $S/before.txt $S/after.txt` is
  silent, with `origin/main` unmoved between them.
  Red when: a note, a finding or an exit moves, or a caller was not renamed and raises `NameError`.
- **AC4** — `python -c "import sys, types; sys.path.insert(0, 'tools/policy'); import policy;
  policy.read_shrink_base('.', types.SimpleNamespace(compare_to_base=lambda *a: int('x')),
  types.SimpleNamespace(home='h'))"` exits 1 and its last stderr line opens `policy.Refusal: ` and
  carries `the base compare did not run`.
  Red when: the extraction left the `ValueError` refusal behind, so the traceback ends in `ValueError`.
- **AC5** — `python tools/policy/check_policy.py --fixture reader-join`, then `--fixture purposes-drain`,
  `--fixture purposes-new` and `--fixture legacy-homes`, each exit 0 and print `0 wrong`, and `python
  tools/policy/check_policy.py` exits 0.
  Red when: the stale or grown finding is lost, the drain writes other rows, or an arm raises.
  permission: the main loop runs all five. The check is a leg, which no role agent runs, and the fixture
  leg is held.
- **AC6** — `python tools/codebase-map/gen_map.py --check` exits 0 after S4's write. Over
  `memory/map/generated/symbols.json`, `grep -c name_ledger` prints `0`, and `grep -cE '"id":
  "(check_shrink_list|read_shrink_base|write_shrink_file|write_shrink_list)"'` prints `4`.
  Red when: the map is not re-rendered.
  figure: 4 is PINNED 2026-11-24, AC1's four names.
- **AC7** — At the pass commit, `python tools/lexicon/lexicon.py --merge-losses "origin/main..HEAD"` exits
  0, prints no line opening `merge-losses: LOSS`, and its summary line carries `losses=0` and
  `restored=4`.
  Red when: a name is not defined in `tools/policy/policy.py` at the tip.
  cost: about a minute and a half; it read 95.75 seconds on 2026-11-24.
  figure: `restored=4` is PINNED 2026-11-24 against the four losses that run printed.

## 6. Gates

`policy check` · `policy fixtures` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `memory-recall kit selftest` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The guarded legs are the ones `python tools/check-spec-tokens.py --legs-for` names over §4's files,
beside the broad `tools/` guard it excludes. The merge-loss check is no leg: the lander and the pre-push
hook run it, and AC7 runs its command. No suite and no bar runs in this pass, and no arm is added or
moved.

## 7. Open questions

- **F1 — Does `check_legacy_homes` call the extracted base compare too?** Options: (a) it calls
  `read_shrink_base` in place of its byte-identical copy, the population's own text unchanged; (b) the
  copy stays, and the new function has one caller. The brief extracts from the first function alone and
  names no second caller. (b) leaves a function beside an inline copy of its body, which the charter's
  `[reuse]` refuses. (a) changes no behaviour, and `legacy-homes` observes it under AC5.
  Recommendation: (a). RESOLVED (agent, 2026-11-24, delegated): (a), rung 3; one function, two callers.
  widens: none · relaxes: none

## 8. Revision log

- rev-1 · 2026-11-24 · initial draft from the brief `2026-11-24-prompt-KICK-dKeptSession-89-spec-brief`,
  grounded at `271522b2`.

## 9. Reuse audit

The seam extended is `tools/policy/policy.py#check_name_ledger` and `#write_name_ledger`, renamed in
place, over `tools/memory-tree/legacy_ledger.py`'s `compare_to_base` and `write_rows`. `python
tools/codebase-map/reuse_lookup.py "grade a plain-name shrink-only ledger population against its base and
drain it"`, run at `271522b2`, ranked those factory functions and no second grader. Recall returned
TOOL-aTrimmedWait-19, whose rename route this unit takes.

Recall terms used: `python tools/memory-recall/query.py "merge-loss check cleared as restored by a rename at the range tip" --terms "merge-losses restored superseded LOSS read_shrink_base write_shrink_list check_name_ledger write_name_ledger reconcile merge range tip"`
