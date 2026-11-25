# TOOL-dBoundRoles-96 — the policy guard takes the key from the landed file alone, and the security review's other items

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-2 · base a911378eb · streams tooling · order 49

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 TOOL-dBoundRoles-95 |
| [2026-11-25-build-TOOL-dBoundRoles-96-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dBoundRoles-96-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-build-TOOL-dBoundRoles-96-deviation-961.md](../build/2026-11-25-build-TOOL-dBoundRoles-96-deviation-961.md) | deviation | — |
| [2026-11-25-prompt-TOOL-dBoundRoles-96-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dBoundRoles-96-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dBoundRoles-96-spec-brief.md](../prompts/2026-11-25-prompt-TOOL-dBoundRoles-96-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dBoundRoles-95` makes a live run's own change to the policy file refuse while the landed file leaves
`policy-file.guard` at `owner-only`. Its security review found a path on which that is false: a run's edit of the
catalogue or of the cap census makes the landed file read as invalid, and the guard then takes an older landed value
(H1). This unit closes that path and the review's other items, M1, L1 and L2. The owner's answer on 2026-11-25 was
"Close it before landing".

The review is `memory/builds/dBoundRoles/reviews/2026-11-25-review-TOOL-dBoundRoles-95-security-diff-review-round1.md`.
Finding 1 of it is a duplicate of finding 2.

## 2. Scope (IN)

- **S1** — H1, findings 2, 3 and 6. `read_guard_value` (`tools/policy/guard.py#read_guard_value`) answers the reader's
  value only where its `source` is `file`. Every other source answers `owner-only`, its reason returned as at base, and
  the match on the words `the catalogue default` goes (section "The read"). The case `guard-run-policy` of
  `tools/policy/check_policy.py` gains the scenarios that plant a moved census and a moved catalogue row. Observed by
  AC1, AC2 and AC3.
  **Readers:** by name: `tools/policy/guard.py` (`check_run_mandate`), `tools/loop/guard.py` (`check_staged`, its
  value's rule), `tools/policy/README.md` and `tools/loop/README.md` ·
  by value: no caller relies on a `last-valid` opening. `main` of the minimal guard and `run_set` of
  `tools/loop/policy_edit.py`, each through `check_run_mandate`, refuse a run's write of the policy file;
  the guard-self and owner-only steps of `check_staged` refuse a leaf through the same call; its value's rule judges
  under `owner-only`, so the `agents-with-reason` branch is not taken. `read_policy_setting` of
  `tools/roles/roles_lib.py` and `read_floor` of `tools/loop/floor.py` take a `last-valid` value through reads of
  their own and do not call this one (F4).
- **S2** — M1, finding 4. `tools/loop/guard.py` gains the plant `moved-default`: the loop, policy and memory-tree kits
  copied into the scratch repository, the copied catalogue's `policy-file.guard` default at `agents-with-reason`, the
  landed file setting no such key. A recorded key with its decision row exits 1, off a run and on `run/t`. Observed by
  AC4.
- **S3** — L1, finding 5, with the skeptic's class-level fix. `tools/loop/guard.py` gains the plant `landed-unread`,
  which owes exit 2 and the `cannot judge` line. `tools/policy/check_policy.py` gains the case
  `guard-run-policy-reader`: a stub reader over a table of outputs, and a reader that does not start. Observed by AC5
  and AC6.
- **S4** — L2, finding 7, with the skeptic's class-level fix. The guard-self line of a policy leaf and the owner-only
  line of `check_staged` offer a live run's branch only where the value `read_guard_value` answers is in
  `RUN_WRITABLE`; the list path's line keeps its words (section "The refusal lines"). Each remaining statement of what
  `guard-self` covers is corrected, the header of `tools/loop/floor.py` and section "The guard" of
  `tools/policy/README.md`. Observed by AC7 and AC8.
- **S5** — The pages and headers lose the limit S1 closes and keep the rest (section "Texts"). Deviation record `961`
  of this unit restates what `TOOL-dBoundRoles-95` and its deviation record 951 state (section "The deviation
  record"). Observed by AC8 and AC9.
- **S6** — The budget rows move, each in its place in `tools/run-gates/selftest-budgets.txt`, and the plant count the
  `loop guard fixtures` row states moves with its row. Observed by AC9.

## 3. Non-goals (OUT)

- What `agents-with-reason` and `agents-within-mandate` admit while the landed file is valid and sets one of them.
- The reader. `policy.py get` keeps answering `last-valid` to every other asker, and `policy-file.on-invalid` keeps its
  meaning.
- Which revision is landed, and any other limit the guard's header lists.
- The other reads that take a `last-valid` value, the floor's and the roles kit's (F4).
- Putting `tools/policy/catalogue.toml` or `tools/policy/caps.toml` on `guarded-paths.txt`.
- The push arm, `tools/push-main.sh`, `tools/memory-tree/routed_commits.py`, `tools/loop/position.py` and anything on
  `origin/main`.
- The text of any CLOSED spec, and of deviation record 951.

`TOOL-dBoundRoles-95` built what these items correct. It is CLOSED, so this unit takes nothing from it and leaves it
nothing.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-84's admission and its run-state grammar, and TOOL-dDeclaredLoop-2's
  verdict and door, each landed at the base

## 4. Design

### Evidence

Probed at HEAD `7aadde6bf`, whose `tools/` tree equals the base's. H1 ran in scratch repositories under `%TEMP%`, built
by `build_guard_repo` of `tools/policy/check_policy.py`. Landed history sets `agents-within-mandate` in a valid file,
then a valid file setting `owner-only` beside a further leaf. `run/t` is a live run's branch by a committed run-state
record and driver. The change staged is `runtime.agents-in-flight`.

| state | `policy.py get policy-file.guard` | `guard.py --staged` |
|---|---|---|
| before the run's edit | `owner-only`, source `file` | exit 1 |
| after the run commits the census without the row of the cap the landed `[budgets]` sets | `agents-within-mandate`, source `last-valid`, reason holding `names no row of the cap census` | exit 0, admitted on the run-branch |
| after the run commits the catalogue with the `review.max-rounds` row renamed, a leaf only the newest landed file sets | `agents-within-mandate`, source `last-valid` | exit 0, admitted on the run-branch |
| each of the above with `landed = source == "file"` in the scratch guard | unchanged | exit 1, the reason holding `is invalid` |

So H1 holds, by execution, for each input that decides validity: `tools/policy/policy.py#read_revision` loads the
working tree's catalogue and `tools/policy/budgets.py#check_budgets` the working directory's census.

M1: a scratch copy of the kits with the moved default read `agents-with-reason`. `check_staged` at HEAD exits 1 off a
run and on `run/t`; with step 4 put back to `policy.resolve` each exits 0, printing
`loop-guard: admitted · policy-file.guard = agents-with-reason`. No plant of `PLANTS` moves the catalogue.

L1: no plant of `tools/loop/guard.py` spells `cannot judge` as a needle, and no case of
`tools/policy/check_policy.py` hands the guard a stub reader. Over a stub `policy.py`, `read_guard_value` at HEAD
answers no value for each output that section "Fixtures" lists, and dropping any one check or caught exception changes
the answer on one of them.

L2: `python tools/loop/guard.py --fixture --plant owner-only-live` prints, on the live run's own branch, that
`floor.no-actor-witness` is refused `for every agent commit off a live run's branch, whatever policy-file.guard reads`,
then the reason that names the key. `tools/loop/floor.py` and `tools/policy/README.md` hold the statements S4 names.

### The read

In `read_guard_value`, `landed = source == "file"`, and nothing else of the function's code moves. A `file` answer is
the leaf of the valid landed text itself, so no file of the working tree can turn it into another value. The shape
checks and the caught exceptions stay.

What a run sees while the landed file reads invalid, whoever made it so:

- `read_guard_value` answers `owner-only`, whatever an older landed revision set, with the reader's reason, which holds
  `is invalid`, the line and the problem.
- Its own write of the policy file is refused, by the guards and by `policy_edit.py set`, with that reason. An agent off
  a run loses the `agents-with-reason` shape too.
- The argued raise, the mirror's render, the role renders, a merge's parent side and the other guarded paths on a live
  run's branch stay as they are.
- Under `policy-file.on-invalid = refuse`, or with no valid revision before it, the reader refuses, and no value is
  read, as at base.

The way out is the row put back, or the owner's commit of the policy file from a terminal. A run under an opened key
that retires a capped file commits the policy file's row out first and the census row after, since the landed file
reads invalid from the census edit on.

A run that edits the catalogue so that an invalid landed file reads valid gets the value that file's own text sets. The
owner landed that text, so the edit opens nothing the owner did not write there.

### The refusal lines

`check_staged` reads the key above step 2, as `value, value_why = mguard.read_guard_value("policy-file.guard")`, the
memoised read; step 4 keeps its `cannot judge` exit in its place and takes the same names. `why` is rebound by the loop
over the missing records, so the read's reason has a name of its own. With `where` as ` off a live run's branch` where
`value` is in `mguard.RUN_WRITABLE`, else empty:

```text
<leaf>: the guard's own switch, refused under floor.guard-self for every agent commit<where> · <reasons>
<key>: owner-only, refused for every agent commit<where>, whatever floor.guard-self reads · <reasons>
```

The first is the line of each guard-self entry on the policy file, the entry of a file that does not parse among them.
The entry on the list file keeps its line byte for byte, since a live run's branch admits the list under every value.

### Fixtures

In `run_guard_run_policy` of `tools/policy/check_policy.py`:

- `guard-run-policy`, after its invalid-file scenario: `write_landed` a valid file with `agents-within-mandate`, then
  one with `owner-only` and a `[budgets]` cap, the first census row with no family, derived through
  `budgets.read_cap_census`. Read back `owner-only` from `file`. On `run/t` remove that row's table from the kit copy's
  census, commit, read back through `policy.py get policy-file.guard --json` that the value is
  `agents-within-mandate` and the source `last-valid`, and owe exit 1 with the `closed` needles and
  `names no row of the cap census`. Then, over a reset, the newest landed file sets `review.max-rounds` in place of the
  cap, the kit copy's catalogue renames that row, the same reads back, exit 1 with `is invalid`.
- `guard-run-policy-reader`, new in `GUARD_RUN_POLICY`: `policy.py` of the kit copy is overwritten by a stub that prints
  the output and exits 0, and the policy file's change is judged on `run/t`. The outputs are text that is no JSON,
  `[]`, `{}`, then an object whose `value` is a list, whose `source` is a number and whose `reason` is a number, each
  otherwise reading `agents-within-mandate`, `file` and a string. Each owes exit 1 and
  `policy-file.guard does not read`. Then a module loaded from the kit copy's `guard.py`, fresh so no memo answers,
  with `sys.executable` patched to a path that names no file: `read_guard_value("policy-file.guard")` is `None` and a
  reason opening `policy.py did not start: `.

In `tools/loop/guard.py`, each in `PLANTS` and in the `owed` map of `run_selftest`:

- `moved-default`, owed 1. The `.py`, `.toml` and `.txt` files of this kit, of the policy kit and of the memory-tree kit,
  found by `resolve_kit_dir`, go to `fx/loop`, `fx/policy` and `fx/memory-tree` of the scratch, where the copied kits'
  own `resolve_kit_dir` probes. The copied catalogue's default moves by a replacement that must match, and the copies
  are committed on `main`. The scenarios: the copied `policy.py get policy-file.guard` prints `agents-with-reason`;
  `review.max-rounds` with its record and its decision row, judged by the copied `guard.py --staged` on `main`; the
  same after `write_live_run`. Each judged scenario owes exit 1 and
  `policy-file.guard = owner-only admits an agent's write only as`.
- `landed-unread`, owed 2. A remote `origin` with no tracking ref, `review.max-rounds` staged with its record,
  `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` empty, owing `loop-guard: cannot judge · policy: refused`.
- `owner-only-live`: the needles of its floor member and its `verdict.remote.pin` become the lines of section "The
  refusal lines", `<where>` empty. `floor-off-agent`: the needle is the first line per landed value, `<where>` empty
  under `owner-only` alone. `pin-owner-only` and `signers-owner-only`: the second line with `<where>`.

The `loop guard fixtures` and `policy fixtures` rows of `tools/run-gates/selftest-budgets.txt` rise by the worst of
repeated direct-CLI readings of the added scenarios times the row's own factor, the reading named on the row. No other
floor moves: neither leg pins a count but the `plants=` figure the former row ends with.

### Texts

- `tools/policy/guard.py`: the docstring of `read_guard_value`; the header's list, which loses the clause on the
  catalogue whose rows decide whether the landed file is valid, and keeps the clause on this file's or the reader's
  code edited in the working tree; the header's admission sentence, which adds an invalid landed file to the cases
  refused.
- `tools/policy/README.md`: section "The guard", the sentence on a `last-valid` answer, the words `or catalogue` of the
  closing list, and the sentence that the loop kit's verdict refuses a change to the guard's own switch off a live
  run's branch; section "The arms", the account of the live run's cases.
- `tools/policy/check_policy.py`: the docstring of `run_guard_run_policy`, and the header where it names the cases.
- `tools/loop/guard.py`: the header's step 4, where it names what reads as `owner-only`, and one clause added to what it
  does not check: while the landed file reads invalid, the floor is read from the last valid revision (F4).
- `tools/loop/floor.py`: the header's gloss on `guard-self` says the guard protects its own switch off a live run's
  branch, and on one under `owner-only`, as the floor table of `help/policy.md` reads.
- `tools/loop/README.md`: the `guard.py` bullet, that an invalid landed file reads as `owner-only`.
- `help/policy.md`: the same clause of "What the guard does not catch" goes; the opening paragraph of "Who may change
  the policy file" says what a run sees while the landed file reads invalid, and the way out; the `last-valid` bullet
  names this key's exception for an admission.

### The deviation record

The record `2026-11-25-build-TOOL-dBoundRoles-96-deviation-961`, under this build's `build/` folder, is the unit's only
deviation record. It departs from `TOOL-dBoundRoles-95` at rev-1, its S2, S4, "The value", "The wrappers", "What it does not check" and
"Texts". It restates:

- the value table's first row reads source `file` alone, and its second row any other source, `last-valid` among them;
- the sentence on a `last-valid` answer whose reason is the default has no object left;
- the limit that deviation record 951 names in its second item is closed, and it had held for the cap census as for the
  catalogue;
- the guard-self and owner-only lines of a policy leaf name a live run's branch only where it would be admitted, which
  amends the third item of 951;
- the `guard-self` statements S4 names read as the help page's floor table does.

Its risk is stricter.

### Inventory

Minted: the case `guard-run-policy-reader` and the plants `moved-default` and `landed-unread`. No function, no module
constant and no key is minted, so no naming cell grades a new name.

### Migration

Nothing stored changes shape, so no upgrade step is owed. A clone whose landed file reads invalid over an older opened
revision stops admitting a run's write of the policy file until the file is valid.

### Rollout

Live at landing, and on this branch from the pass's own commit, since the hook resolves the guard in the worktree. No
switch: `policy-file.guard` in a valid landed file is the owner's.

### Files touched (estimate)

- `tools/policy/guard.py`
- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `tools/loop/guard.py`
- `tools/loop/floor.py`
- `tools/loop/README.md`
- `tools/run-gates/selftest-budgets.txt`
- `help/policy.md`

The deviation record and the acceptance ledger go under this build's `build/` folder.

### Alternatives rejected

- **Guard the catalogue and the census.** Each is ordinary work of a run, and a clone's own reader code stays a limit.
- **Judge the landed file by the landed catalogue and census.** The reader judges by its own kit's, for every asker.
- **Keep `last-valid` where the older value is `owner-only`.** That answers what `owner-only` already answers.

## 5. Production-readiness checklist

- security — narrows what a live run may write and widens nothing; an invalid landed file denies. What it cannot see
  stays listed in the guard's header.
- perf / scale — none: the memoised read moves up within `check_staged`, and no process is added.
- error / empty / loading states — an invalid, absent or unread landed file opens nothing.
- observability — the refusal carries the reader's reason, which names the invalid line and its problem.
- risks — an adopter whose landed file reads invalid sees a run's policy write refused until it is valid.
- testing — the criteria and the new arms below.
- migration — as "Migration" says.
- user docs — `help/policy.md` (S5).

## 6. Acceptance criteria

A staged break is a scratch copy of the kits with the named code changed, and each case runs over it by the same
command. No criterion runs a whole self-test.

- **AC1** — When `python tools/policy/check_policy.py --fixture guard-run-policy` runs, the moved-census scenario reads
  back `agents-within-mandate` from `last-valid` and the guard exits 1 naming `policy-file.guard = owner-only` and
  `names no row of the cap census`.
  Red when: the line admits `last-valid` beside `file` with the text match, as at base, and the guard exits 0.
- **AC2** — When `python tools/policy/check_policy.py --fixture guard-run-policy` runs, the moved-catalogue scenario
  reads back the same and the guard exits 1 with `is invalid`; and the scenario of the moved default over an invalid
  landed file still exits 1 with `is invalid`.
  Red when: the line is as at base; or the reason is replaced by one that does not name the invalid file.
- **AC3** — When `python tools/policy/check_policy.py --fixture guard-run-policy-open` runs, each value of
  `RUN_WRITABLE` in a valid landed file still admits; and `git grep -n -F "guard.read_guard_value(" -- tools/loop` with
  `grep -n "read_guard_value(" tools/policy/guard.py` prints the definition, the call of `check_run_mandate` and the
  call of `check_staged`, and no other call.
  Red when: `source` is compared with a word the reader never writes, so an opened key refuses; or a further caller
  takes the value another way.
- **AC4** — When `python tools/loop/guard.py --fixture --plant moved-default` runs, the read back prints
  `agents-with-reason`, the judged scenarios hold off a run and on `run/t`, and the command exits 1.
  Red when: step 4 is put back to `policy.resolve("policy-file.guard").value`, and each judged scenario exits 0.
- **AC5** — When `python tools/loop/guard.py --fixture --plant landed-unread` runs, its scenario holds and the command
  exits 2.
  Red when: the branch of `check_staged` on a value of `None` is deleted, and the verdict exits 1.
- **AC6** — When `python tools/policy/check_policy.py --fixture guard-run-policy-reader` runs, each stub output exits 1
  with `policy-file.guard does not read`, and the reader that does not start answers no value and
  `policy.py did not start: `.
  Red when: the `isinstance` check of `value`, of `source` or of `reason` is deleted; `ValueError`, `TypeError` or
  `KeyError` leaves the caught set; or the `OSError` branch is deleted.
- **AC7** — When `python tools/loop/guard.py --fixture --plant owner-only-live` runs, and the same with
  `floor-off-agent`, `pin-owner-only` and `signers-owner-only`, every scenario holds its line of section "The refusal
  lines"; and `git grep -n -F "whatever policy-file.guard reads" -- tools/loop/guard.py` prints the list path's line.
  Red when: either line is as at base; or `where` is empty, or set, under every value.
- **AC8** — When `git grep -n -F "whether an older revision answers" -- tools help`,
  `git grep -n -F "protects its own switch off a live run's branch)" -- tools` and
  `git grep -n -F "switch off a live run's branch, asks" -- tools/policy/README.md` run they print nothing, and
  `grep -n "reads invalid" help/policy.md tools/loop/README.md tools/policy/guard.py tools/policy/README.md` prints a
  line of each file.
  Red when: a header or a page still names the closed limit, or the floor's header keeps its gloss.
- **AC9** — When `git diff -U0` of the pass is read it shows the `loop guard fixtures` and `policy fixtures` rows of
  `tools/run-gates/selftest-budgets.txt` moved, the former's `plants=` figure equal to the length of `PLANTS` a probe
  that imports `tools/loop/guard.py` prints; and
  `grep -rn --include="*-deviation-961.md" "TOOL-dBoundRoles-95" memory/builds/dBoundRoles/build` prints the departure.
  Red when: a row stays, the figure is stale, or the record is absent.
  figure: the plant count is derived at observation time.

## 7. Gates

`policy fixtures` · `policy check` · `loop guard fixtures` · `routed-commits selftest` · `govkit selftest` · `scratch-guard self-test` · `spawn-guard self-test` · `help page commands` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the line of `read_guard_value` put back to its base form, for the moved census and for the moved catalogue row · none; the `policy fixtures` budget row moves
New arm: tools/policy/check_policy.py · covers AC6 · each shape check deleted, then each caught exception dropped · none, the same row
New arm: tools/loop/guard.py · covers AC4 · step 4 put back to the resolver · none; the `loop guard fixtures` budget row moves
New arm: tools/loop/guard.py · covers AC5 · the `None` branch deleted · none, the same row
New arm: tools/loop/guard.py · covers AC7 · each refusal line put back to its base form, then `where` fixed empty and fixed set · none, the same row

## 8. Open questions

- **F1 — What does an invalid landed file read as?** Options: (a) `owner-only`, with the reader's reason; (b) no value,
  as a refused reader. Under (b) the loop guard exits 2 on every guarded change, the raise and the mirror's render among
  them, while a landed file reads invalid. RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) > (b) ·
  pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F2 — How do the policy-leaf lines offer a live run's branch only where it would be admitted?** Options: (a) by the
  value read, as step 4's sentence does; (b) a fixed sentence that states the condition in words. (b) still names a
  run's branch where it would be refused, against `TOOL-dBoundRoles-95` S4. RESOLVED (agent, 2026-11-25, delegated):
  (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — How does M1's plant part step 4's read from the resolver's?** Options: (a) a scratch copy of the kits whose
  catalogue default moved; (b) a landed file made invalid over an older `agents-with-reason`, with this tree's kits. (b)
  is cheaper and leaves the moved default, the consequence the review names, with no arm. RESOLVED (agent, 2026-11-25,
  delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F4 — Do the other reads that take a `last-valid` value change here?** `read_floor` and `read_policy_setting` fall
  back as `policy-file.on-invalid` says. A floor member an older revision switched off can so read `off`. Guard-self and
  the change records are then reported, and step 4 still refuses a run's write of the policy file, so the property
  holds. Options: (a) leave both, the floor's reach named in the loop guard's header; (b) change both. (b) changes what
  other consumers read under a policy value the owner set, veto 1 by the Non-goal above, and `read_floor` has readers no
  item of the review names. RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the brief `2026-11-25-prompt-TOOL-dBoundRoles-96-spec-brief` and the security
  review it names.

## 10. Reuse audit

The seams extended are `tools/policy/guard.py#read_guard_value`, the step sequence of
`tools/loop/guard.py#check_staged`, the fixture `tools/policy/check_policy.py#run_guard_run_policy` over
`build_guard_repo` with its `write_landed`, and the plants of `tools/loop/guard.py` over `write_guard_plant` and
`write_live_run`. `python tools/codebase-map/reuse_lookup.py "answer a policy key only where the landed file sets it, never a fallback revision"`
ranked name neighbours, `read_policy_value` first among the policy readers, and no other admission read; a kit imports
no sibling kit, so none of them serves the guard. The recall probe returned `TOOL-dBoundRoles-95`, its review,
`TOOL-dGroundRules-4` and `TOOL-dGroundRules-6`, and no record that any admission relies on a fallback.

Rejected candidates: those of "Alternatives rejected", by reading; the base line, by the H1 probe of "Evidence".

Recall terms used: `python tools/memory-recall/query.py "may a guard take a last-valid value of policy-file.guard that a run's own catalogue or cap census edit moved" --terms "read_guard_value last-valid policy-file.guard owner-only cap-census catalogue RUN_WRITABLE read_last_valid landed-revision minimal-guard check_run_mandate on-invalid"`
