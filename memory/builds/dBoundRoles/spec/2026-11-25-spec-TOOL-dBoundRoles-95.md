# TOOL-dBoundRoles-95 — under `policy-file.guard = owner-only` the policy guard admits no live run's own write of the policy file

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-2 · base 735060358 · streams tooling · order 48

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 |
| [2026-11-25-build-TOOL-dBoundRoles-95-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dBoundRoles-95-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-build-TOOL-dBoundRoles-95-deviation-951.md](../build/2026-11-25-build-TOOL-dBoundRoles-95-deviation-951.md) | deviation | — |
| [2026-11-25-build-TOOL-dBoundRoles-95-widen-21.md](../build/2026-11-25-build-TOOL-dBoundRoles-95-widen-21.md) | widen | — |
| [2026-11-25-build-TOOL-dBoundRoles-95-widen-22.md](../build/2026-11-25-build-TOOL-dBoundRoles-95-widen-22.md) | widen | — |
| [2026-11-25-prompt-TOOL-dBoundRoles-95-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dBoundRoles-95-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dBoundRoles-95-spec-brief.md](../prompts/2026-11-25-prompt-TOOL-dBoundRoles-95-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`check_run_mandate` (`tools/policy/guard.py#check_run_mandate`) admits every guarded path on a live run's
branch, the policy file among them, whatever `policy-file.guard` reads. So a run can commit a
`roles.effort.*` level below the floor on its own branch, and it lands as the owner's write
(`TOOL-dBoundRoles-23` F6). The owner answered on 2026-11-25: "Close it before landing". This unit makes
a live run's own change to the policy file refuse under `owner-only`.

## 2. Scope (IN)

The property, which every item below serves. Where the landed policy file leaves `policy-file.guard` at
`owner-only`, an agent's commit on a live run's branch changes `.governance/policy.toml` only as the
raised cap `check_raise_shape` admits, or as a merge taking a parent's blob whole, which
`check_parent_sides` leaves out of the judged set. Every other guarded path keeps the run admission of
PLAY-dOrderedCharter-84, the owner's 2026-11-12 ruling. The 2026-11-25 answer narrows that ruling for the
policy file alone.

- **S1** — `check_run_mandate(paths)` takes the guarded paths the caller would write, a required argument,
  and refuses a live run's branch where `paths` holds the policy file and the guard value does not open the
  file to a run (section "The admission"). `main` passes its touched set, so the refusal holds for the policy
  file changed alone, beside other guarded paths, deleted, retyped, renamed away, added, or written anew by a
  merge. Observed by AC1 and AC2.
  **Readers:** by name: `tools/policy/guard.py` (`main`), `tools/loop/guard.py` (`check_staged`, its
  guard-self and owner-only steps), `tools/loop/policy_edit.py` (`run_set`) and `tools/policy/README.md` ·
  by value: `main` refuses a touched set holding the policy file under `owner-only`, and admits a set without it
  as at base; the guard-self step admits the list file as at base and refuses a leaf of the policy file;
  the owner-only step refuses a leaf of `OWNER_ONLY_KEYS`; `run_set` prints its proposal and writes nothing.
  The upgrade steps that write the policy file, `tools/govkit/steps/fanout_cap.py`,
  `tools/govkit/steps/inherited_red.py` and `tools/govkit/steps/reviewer_merge.py`, write the working tree
  and call no guard; a live run's commit of what they wrote is refused, so the owner commits it.
  `tools/govkit/steps/review_rounds.py` reads the file and proposes, and
  `tools/govkit/steps/kickoff_facts_to_overlay.py` writes it in a fixture alone, so neither sees a change.
- **S2** — `read_guard_value(key)` in `tools/policy/guard.py` is the one read of the key for an admission: it
  runs `policy.py get <key> --json` from its own kit as a subprocess, and answers a value only where the
  landed policy file sets one. An unset key answers `owner-only`, whatever the catalogue's default says, and
  a reader that refuses answers no value (section "The value"). So a switch of the key in the commit, or in an
  earlier commit of the run, and a moved catalogue default, open nothing. Observed by AC3.
- **S3** — `agents-with-reason` and `agents-within-mandate` keep admitting, on a live run's branch, what they
  admit at base, their records owed as at base. The cap raise, the parent's side of a merge, the mirror's
  render and the role renders keep their shapes under every value. Observed by AC4 and AC6.
- **S4** — `tools/loop/guard.py` hands `check_run_mandate` the path each step judges, and step 4 takes the
  value from `read_guard_value` in place of its own `policy.resolve` call. Its refusal text names a live run's
  branch only where that branch would be admitted. Observed by AC5, AC6 and AC8.
- **S5** — `tools/loop/policy_edit.py set` hands `check_run_mandate` the policy file. Under `owner-only` on a
  live run's branch, off a terminal, it prints the proposal and the not-proven line and writes nothing. Under
  an opened value it writes with `none — run mandate <run-state path>` as at base. `raise` is untouched.
  Observed by AC7.
- **S6** — Every refusal names the owner's terminal commit as the remedy: the guards' `REMEDY` lines, the
  door's not-proven line, and the write hook's deny text (section "Texts"). Observed by AC1, AC5 and AC7; the
  deny text is NOT OBSERVED by a criterion, being prose the standing write row reads by its door's name.
- **S7** — The push arm and the merge bar are unchanged (section "The push arm and the bar"). Observed by AC9.
- **S8** — The pages and headers that state the old admission state the new one (section "Texts"), the fixture
  cases and their budget rows move (section "Fixtures"), and one deviation record of this unit restates the gap
  `TOOL-dBoundRoles-23` names, whose text stays frozen. Observed by AC10 and AC11.

## 3. Non-goals (OUT)

- The other guarded paths. The mirror, the instruction manifest, the deployer's answers and the role renders
  keep the run admission on a live run's branch.
- What `agents-with-reason` and `agents-within-mandate` admit, on a live run's branch and off it.
- The list file. A list line dropped in one commit and the policy file changed in the next stays a named gap of
  the guard, for every agent, as does the guard's own code edited in the working tree.
- Authorship at the push. The push arm grades records and trailers, never who committed.
- The code of `check_effort_floor` (`tools/roles/roles_lib.py#check_effort_floor`). Its docstring alone moves.
- The landing's own commits, which the pre-commit hook never judges, and any edit of `tools/push-main.sh`.
- Any other build's spec, any CLOSED spec, `tools/memory-tree/routed_commits.py` and `tools/loop/position.py`.

`TOOL-dBoundRoles-21`, `TOOL-dBoundRoles-23` and `TOOL-dBoundRoles-43` built the effort keys and the floor. Each
is CLOSED, so this unit takes nothing from them and leaves them nothing.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-84's admission and its run-state grammar, and
  TOOL-dDeclaredLoop-2's verdict and door, each landed at the base
- **hands-off** external — the owner's edit of the unit `repo.kickoff.f31` in `.governance/instructions.toml`,
  whose last clause says the guard admits a live run's change; its write door takes the owner's terminal
  proof, so the main loop proposes the sentence to the owner at the close (F6)

## 4. Design

### Evidence

Probed at HEAD `18ba9d383`, whose `tools/` tree equals the base's, in scratch repositories under `%TEMP%` built by
the loop guard's own `write_guard_plant` and `write_live_run`, the change named staged on `run/t`.

| staged on the live run's branch, key unset | reading |
|---|---|
| `roles.effort.default = "low"` alone, no change record | minimal guard exit 0; loop guard exit 1 for the missing record alone |
| the same with its change record | each exit 0; the loop guard prints `policy-file.guard = owner-only · the minimal guard admits it` |
| the file deleted; renamed away; changed beside `.governance/deploy.toml` | minimal guard exit 0 each |
| a third text concluding a conflicted merge | minimal guard exit 0 |
| the parent's side of the same merge | each exit 0, printing nothing |
| `policy_edit.py set roles.effort.default low` | exit 0, written, `Proof: none — run mandate memory/builds/tRun/RUN.md` |
| the file changed after the run committed `policy-file.guard = "agents-within-mandate"` | `policy.py get` still answers `owner-only`, read at local `main`; minimal guard exit 0 |
| `policy.py get policy-file.guard` with a remote and no tracking ref | exit 2, naming the missing ref |
| the same with `GOV_DEFAULT_BRANCH=run/t` in the environment and no remote | `agents-within-mandate`, the run's own value |

So the gap holds in each shape. The loop guard refuses the first row only because no record was staged, and its record
is the run's own to write. The reader already answers from the landed revision, but its catalogue is the working
tree's (`tools/policy/policy.py#read_revision` calls `load_catalogue(KIT)`), so an unset key answers whatever default
the run's own branch carries. gov's landed policy file sets no `policy-file.guard`.

### The admission

`check_run_mandate(paths)` keeps its reads in order: the branch, the candidates, the terminal set, the phase. Where
they find no live run it returns what it returns at base. Where a live run names the branch:

1. `POLICY` not in `paths`: the admission, as at base.
2. Else `value, why = read_guard_value("policy-file.guard")`. `value` in `RUN_WRITABLE`, the tuple
   `("agents-with-reason", "agents-within-mandate")`: the admission.
3. Else no admission, and the one reason below, reading `policy-file.guard does not read` where the reader gave no value.

```text
<run-state path>, phase <PHASE>, names this branch, and policy-file.guard = <value> leaves
.governance/policy.toml to the owner, who commits it from a terminal (<why>)
```

It is a single line. `main` prints each reason as `policy-guard: no run admits it · <why>`, in place of
`policy-guard: not a live run's branch · <why>`, since a live run's branch can now be refused. No code compares the
old prefix; `help/policy.md` and `tools/policy/README.md` spell it and move with it.

A refused set holding the policy file beside other guarded paths refuses whole (F4). Its remedy line says to commit the
other paths apart, which the run admission then takes.

### The value

`read_guard_value(key)`, under `functools.cache`, runs `[sys.executable, "-B", <this kit>/policy.py, "get", key,
"--json"]` from the working directory with no standard input, and returns `(value, why)`:

| the reader | answer |
|---|---|
| exit 0, `source` `file` or `last-valid`, the value a string | its `value`, its `reason` |
| exit 0, any other `source` | `owner-only`, its `reason` |
| another exit, no start, or output that is no such object | `None`, the reader's first standard error line, or the exit |

A `last-valid` answer whose own reason is the catalogue default carries that source too, so the function also answers
`owner-only` where the `reason` holds `the catalogue default`. `tools/policy/policy.py#read_last_valid_value` joins the
inner reason onto its own, and `read_default_value` is the only writer of those words.

Each caller passes the key as a literal first argument, so `scan_reader_keys` counts the read. The read costs an
interpreter start per process, and in the minimal guard only where a live run names the branch and the policy file is
judged. The minimal guard still imports no reader: the mirror shape already runs `policy.py` this way
(`tools/policy/guard.py#check_mirror_render`). Where the loop kit is absent the minimal guard reads the key itself,
so each kind of install gives the same answer.

`tools/loop/guard.py` step 4 calls `mguard.read_guard_value("policy-file.guard")`. A `None` answer is
`loop-guard: cannot judge · <why>`, exit 2, as a refused resolve is at base. Its `agents-with-reason` branch
therefore also reads the landed file's own value and never a moved default, for an agent off a run as well.

### The wrappers

- Guard-self (`tools/loop/guard.py#check_staged`): each entry is judged by `check_run_mandate` over its own path, the
  list file or the policy file, so a staged change of each admits the list and refuses the leaf. A refused leaf of the
  policy file prints the reason the admission gave, beside the line it prints at base.
- Owner-only, the leaves of `OWNER_ONLY_KEYS`: judged over the policy file's path. Under an opened value a live run's
  branch admits them as at base.
- Step 4's refusal sentence offers a live run's branch for the policy file only where the value is in `RUN_WRITABLE`.
  `floor.guard-self` and `floor.record-changes` at `off` change nothing here, since step 4 runs the minimal guard
  whatever they read.
- `run_set` (`tools/loop/policy_edit.py#run_set`): `check_run_mandate([plan["rel"]])`. Its not-proven line already joins
  the reasons, and then names the terminal.

### The landing steps

`run_gov_first` in `tools/push-main.sh` walks the upgrade steps, and the lander folds their output by `commit-tree`
(`tools/push-main.sh@3a5bf825:1669-1673`) or commits it with `--no-verify`, so no pre-commit hook judges it. The push
arm then grades that merge or commit, and a policy key it sets with no `Gov-Policy:` trailer and no change record is
refused as `policy-unrecorded`. So a run whose landing step writes the policy file cannot land that write, nor commit
it first on its own branch: the owner commits it from a terminal, and the step's next run finds nothing to write. A run
driving an adopter's `govkit update` hands the same commit to the owner. `help/policy.md` states each.

gov's own policy file holds no key the steps of this build write. `reviewer_merge.py` is the one of them that writes
it, and `git grep -nE 'gov-(spec|diff)-reviewer|roles' -- .governance/policy.toml` prints nothing, exit 1, at HEAD.
`house_overlays_to_instructions.py` and `spawn_guard_pack.py` write other files.

### The push arm and the bar

`check_push_range` (`tools/loop/guard.py#check_push_range`) grades a trailer and a change record per changed key, read
from the commit alone. It asks no authorship, so it certifies no write as the owner's, and a commit that skipped the
hook passes it on its records. The merge bar's readers of the policy file, the `policy check` leg and check 19 of
`tools/unattended/check-unattended.sh` over a run's own commits, certify none either. Each stays as it is.

### What it does not check

The minimal guard's header keeps its standing list: `--no-verify`, a pty wrapper, a commit made with no hook, a list
line dropped a commit earlier, the guard deleted from the working tree, another clone, and a run-state file naming the
agent's own branch. This unit adds to it, and to `help/policy.md`:

- the guard's or the reader's code edited in the working tree;
- the landed revision moved by hand, by `GOV_REMOTE` or `GOV_DEFAULT_BRANCH` in the agent's environment or by
  `git update-ref` on the tracking ref;
- a merge taking an old parent's blob whole, which brings back a value the owner once wrote;
- a level an agent wrote while the key read another value, which stays after the owner sets `owner-only` again;
- where the landed value opens the file, a run that sets `policy-file.guard` back to `owner-only` beside a low level (F5).

### Texts

Each of these says today that `owner-only` and `agents-within-mandate` admit the same, or that a live run's branch is
admitted whatever the value, and is corrected:

- `tools/policy/guard.py`: the header, `REMEDY`, the docstring of `check_run_mandate`. The header's claim that neither
  key is read becomes that `policy-file.guard` is read at the landed revision through a subprocess, for the run
  admission alone, and `policy-file.proof` not at all.
- `tools/loop/guard.py`: the header's steps, the comment over `OWNER_ONLY_KEYS`, `REMEDY`, the plant descriptions.
- `tools/loop/policy_edit.py` and `tools/loop/floor.py`: their headers.
- `tools/roles/roles_lib.py`: the last paragraph of `check_effort_floor`'s docstring; `tools/roles/README.md`, the
  paragraph that closes the floor.
- `tools/policy/README.md`, sections "The guard" and "The arms"; `tools/policy/check_policy.py`, the header's account of
  the live run's cases; `tools/loop/README.md`, the `guard.py` bullet and the sentence on a live run's switch of the
  floor; `tools/run-gates/README.md`, the peer signer paragraph.
- `tools/policy/catalogue.toml`: the summaries of `verdict.remote.pin` and `verdict.peer.signers`, which say a live run
  may set them, and from them `help/reference/policy.md` and the mirror `.governance/policy.json`. The mirror is a
  commit of its own, since it renders the committed catalogue.
- `help/policy.md`, section "Who may change the policy file" and the floor table's `guard-self` row: the ruling and its
  narrowing, the verdict's steps, the door, the refusal line, what the guard does not catch, and the landing steps.
  `help/roles.md`, the floor bullet: under `owner-only` a live run's change to the policy file is refused.
  `help/verdict-backends.md`, the signer and pin paragraphs.
- `.githooks/pre-commit`: the clause of the block's comment that lists a live run's branch among the admitted shapes.
- `tools/hooks/scratch-guard.js`: the deny text that offers `set <key> <value>` on a live run's branch.

The fixtures that assert it are the plants `owner-only-live`, `floor-off-run` and `set-run-live` of
`tools/loop/guard.py`. `guard-run-live` of `tools/policy/check_policy.py` stages no policy file and stays.

The deviation record is numbered `951`, departs from `TOOL-dBoundRoles-23` at rev-7, its S6 and F6, and restates that
the guard now refuses a live run's change under `owner-only`, with the limits above.

### Fixtures

`tools/policy/check_policy.py`, beside `GUARD_RUN`, each over `build_guard_repo` on `run/t` with the driver and the
run-state record committed, and with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` empty for the guard:

- `guard-run-policy`, exit 1 each and naming `policy-file.guard = owner-only`: the policy file alone under either
  `run-branch` spelling; beside `.governance/deploy.toml`; deleted; retyped to mode `120000`; renamed away; added
  over a HEAD lacking it; with `policy-file.guard` switched in the same commit; after a commit of the run that
  switched it; and after a commit of the run that moved the catalogue row's default, the landed file valid, then
  invalid over a last valid revision that sets no key. Then, with the tracking ref deleted, exit 1 naming the
  reader's line.
- `guard-run-policy-open`, exit 0 each: the policy file alone with the tracking ref at a commit setting each value of
  `RUN_WRITABLE`, and, under `owner-only`, the argued raise with its decision row, printing the raise's own line.
- `guard-run-policy-merge`: a conflicted merge concluded with the branch's side, exit 0, then with a third text, exit 1.

`guard-run-live` keeps its bytes and is the split's other half.

`tools/loop/guard.py`, the plants:

- `owner-only-live`: `review.max-rounds` with its record, exit 1; a `floor` member with its record, exit 1 naming
  `floor`; `verdict.remote.pin` with its record, exit 1; the list line dropped beside a change of
  `.governance/deploy.toml` with the list's record, exit 0; `policy_edit.py raise` and its decision row, exit 0; a
  conflicted merge concluded with main's side, exit 0, and with a third text and its record, exit 1.
- `run-switched-guard`: a commit of the run sets `policy-file.guard` to `agents-within-mandate`, then
  `review.max-rounds` with its record and decision row, exit 1.
- `mandate-live` unchanged; `with-reason-live`, new: the same change under `agents-with-reason` with its record and no
  decision row, exit 0.
- `floor-off-run`: its scratch lands `agents-within-mandate`, so its scenarios read as at base.
- `set-run-live`: exit 1 for a key, naming `policy-file.guard` and `nothing written`, the file's bytes unchanged, then
  `raise`, exit 0. `set-run-open`, new: the scenarios of `set-run-live` at base, under `agents-within-mandate`.

The `owed` map of `run_selftest` gains each plant whose last scenario exits 1. The `loop guard fixtures` and
`policy fixtures` rows of `tools/run-gates/selftest-budgets.txt` rise by the worst of repeated direct-CLI readings of
the added cases times the row's own factor, the reading named on the row.

### Inventory

Minted: `read_guard_value` (cell `py.function`, `read` a declared lead) and the module constant `RUN_WRITABLE`, which no
cell grades; the cases `guard-run-policy`, `guard-run-policy-open` and `guard-run-policy-merge`; the plants
`run-switched-guard`, `with-reason-live` and `set-run-open`.

### Migration

Nothing stored changes shape, so no upgrade step is owed. A run in flight on another branch meets the refusal at its
first policy write after it merges this unit. A policy change already committed on its branch is a parent's blob, and
a later merge that writes a new one is the owner's.

### Rollout

Live at landing, and on this branch from the pass's own commit, since the hook resolves the guard in the worktree.
No switch: the owner's `policy-file.guard` is the switch. This run writes no policy key after it.

### Files touched (estimate)

- `tools/policy/guard.py`
- `tools/policy/check_policy.py`
- `tools/policy/catalogue.toml`
- `tools/policy/README.md`
- `tools/loop/guard.py`
- `tools/loop/policy_edit.py`
- `tools/loop/floor.py`
- `tools/loop/README.md`
- `tools/roles/roles_lib.py`
- `tools/roles/README.md`
- `tools/hooks/scratch-guard.js`
- `tools/run-gates/README.md`
- `tools/run-gates/selftest-budgets.txt`
- `.githooks/pre-commit`
- `.governance/policy.json`
- `help/policy.md`
- `help/roles.md`
- `help/verdict-backends.md`
- `help/reference/policy.md`

The deviation record and the acceptance ledger go under this build's `build/` folder.

### Alternatives rejected

- **A further check beside `check_run_mandate`, called by each caller.** A caller that forgets it admits; a required
  argument errors instead.
- **The value passed to the minimal guard as a flag.** The install with no loop kit has nobody to pass it.
- **The policy file off `guarded-paths.txt`, under a rule of its own.** The hook reads that list to decide whether to
  run the guard at all.

## 5. Production-readiness checklist

- security — narrows what a live run may write; denies by default on an unread key, an unset key and an unknown value;
  widens nothing. What it cannot see is listed in "What it does not check".
- perf / scale — an interpreter start per guard process, for a judged policy file alone.
- error / empty / loading states — a reader that refuses, does not start or prints another shape reads as no value.
- observability — the refusal names the run, the key, its value and why it read so, and the owner's terminal.
- risks — an adopter whose runs write the policy file under `owner-only` is refused until the owner commits or opens
  the key; a clone with no resolvable landed revision refuses a run's write.
- testing — the criteria and the new arms below.
- migration — as "Migration" says.
- user docs — `help/policy.md`, `help/roles.md`, `help/verdict-backends.md` and `help/reference/policy.md` (S8).

## 6. Acceptance criteria

A staged break is a scratch copy of the kits with the named code changed, and each case runs over it by the same
command. No criterion runs a whole self-test.

### The minimal guard

- **AC1** — When `python tools/policy/check_policy.py --fixture guard-run-policy` runs, its scenarios of the policy
  file alone under either `run-branch` spelling exit 1 naming the run, `policy-file.guard = owner-only` and the
  owner's terminal; and `python tools/policy/check_policy.py --fixture guard-run-live` still exits 0.
  Red when: `check_run_mandate` ignores `paths`, so the policy file is admitted; or refuses every path, so
  `guard-run-live` reds.
- **AC2** — When `python tools/policy/check_policy.py --fixture guard-run-policy` runs, the scenarios beside another
  guarded path, deleted, retyped, renamed, added and switched in the same commit each exit 1; and
  `--fixture guard-run-policy-merge` exits 1 for the third text and 0 for the branch's side.
  Red when: the test asks for the policy file touched alone, or for a modified file alone, or a merge in progress
  admits a live run's third text.
- **AC3** — When `python tools/policy/check_policy.py --fixture guard-run-policy` runs, the scenarios after the run's own
  switch, after the run's moved catalogue default over a valid and over an invalid landed file, and with no landed
  revision each exit 1.
  Red when: `read_guard_value` passes `--rev HEAD` or reads the index; or takes a `default` source's value, or a
  `last-valid` one whose reason is the default; or an exit other than 0 admits.
- **AC4** — When `python tools/policy/check_policy.py --fixture guard-run-policy-open` runs, each value of
  `RUN_WRITABLE` at the landed revision admits the policy file, and the argued raise admits under `owner-only` by its
  own line.
  Red when: either value is cut from `RUN_WRITABLE`, or the run refusal is placed before the raise's verdict.

### The wrapper and the door

- **AC5** — When `python tools/loop/guard.py --fixture --plant owner-only-live` and the same with `run-switched-guard`
  run, each scenario holds as "Fixtures" states, the command exits 1 and the refusal names the owner's terminal.
  Red when: the guard-self or the owner-only step hands over the list's path for a policy leaf; the list's own entry
  is judged over the policy file; or the key is read at HEAD.
- **AC6** — When `python tools/loop/guard.py --fixture --plant mandate-live` and the same with `with-reason-live` run,
  each exits 0 printing `loop-guard: admitted`; and `floor-off-run` exits 1 for its missing records alone, its
  recorded scenario admitted.
  Red when: the run admission is refused under every value.
- **AC7** — When `python tools/loop/guard.py --fixture --plant set-run-live` runs, `policy_edit.py set` exits 1 printing
  `policy-file.guard` and `nothing written`, the policy file's bytes unchanged, and `raise` writes; and under
  `set-run-open` it writes with `Proof: none — run mandate`.
  Red when: `run_set` hands `check_run_mandate` an empty set, and the door writes as at base.
- **AC8** — When `git grep -n -F "check_run_mandate(" -- tools` and
  `git grep -n -F 'resolve("policy-file.guard")' -- tools` run, every call of the first passes an argument and the
  second prints nothing.
  Red when: step 4 keeps its own read, so a verdict rests on a pair of readings.
- **AC9** — When a probe compares the source of `check_push_range` in `tools/loop/guard.py` with that of its blob
  `be997d5a`, by `inspect.getsource` over a scratch file written by `git cat-file blob`, they are equal, and
  `python tools/loop/guard.py --fixture --plant push-no-trailer` exits 1 as at base.
  Red when: the push arm moves.

### Documents

- **AC10** — When `git grep -n -F "policy-guard: not a live run's branch" -- tools help .githooks` runs it prints
  nothing, and `grep -n "2026-11-25" help/policy.md`, `grep -n -F "RUN_WRITABLE" tools/policy/README.md` and
  `grep -n "owner-only" tools/loop/README.md help/roles.md help/verdict-backends.md` each print the corrected line.
  Red when: a page states the run admission of the policy file as at base.
- **AC11** — When `python tools/policy/policy.py mirror --check` runs after the mirror's commit it prints
  `policy: mirror fresh`; `git diff -U0` of the pass shows the `loop guard fixtures` and `policy fixtures` rows of
  `tools/run-gates/selftest-budgets.txt` moved; and the deviation record names `TOOL-dBoundRoles-23`.
  Red when: the catalogue's summaries move and the mirror or a row does not.

## 7. Gates

`policy fixtures` · `policy check` · `loop guard fixtures` · `routed-commits selftest` · `govkit selftest` · `scratch-guard self-test` · `spawn-guard self-test` · `format-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended-build self-test` · `help reference pages` · `help page commands` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the `paths` test cut, then narrowed to the policy file touched alone, then to a modified file · none; the `policy fixtures` budget row moves
New arm: tools/policy/check_policy.py · covers AC3 · the read moved to HEAD, then a `default` source's value taken, then a `last-valid` one resting on the default, then a refused reader admitted · none, the same row
New arm: tools/policy/check_policy.py · covers AC4 · each member of `RUN_WRITABLE` cut, then the refusal placed before the raise · none, the same row
New arm: tools/policy/check_policy.py · covers AC2 · the third text of a merge admitted on a live run's branch, then the parent's side refused · none, the same row
New arm: tools/loop/guard.py · covers AC5 · each step's path swapped, then the key read at HEAD · none; the `loop guard fixtures` budget row moves
New arm: tools/loop/guard.py · covers AC6 · the run admission refused under every value · none, the same row
New arm: tools/loop/guard.py · covers AC7 · `run_set` handing over an empty set · none, the same row

## 8. Open questions

- **F1 — Where is `policy-file.guard` read for the run admission?** Options: (a) in the minimal guard, by its own kit's
  `policy.py get` as a subprocess, the wrapper and the door taking its answer; (b) the minimal guard refuses a run's
  write of the file always, and the wrapper admits it again under the other values; (c) the minimal guard parses the
  landed file itself. (b) changes what those values admit where no loop kit is installed, against S3, and gives the
  admission another home; (c) is another reader of the landed revision. RESOLVED (agent, 2026-11-25, delegated): (a).
  options: (a) > (b) > (c) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F2 — What does an unset key read as?** Options: (a) `owner-only`, whatever the catalogue's default says; (b) the
  catalogue default the reader prints; (c) the default of the catalogue's blob at the landed revision. Under (b) a run
  that moves the default in the working tree's catalogue, which no guarded path names, opens the file to itself; (c)
  needs a catalogue reader the policy kit does not have. RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) >
  (c) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — What does a reader that does not answer admit?** Options: (a) nothing, the run's write of the policy file is
  refused naming the reader's line; (b) what it admits at base. (b) lets a missing tracking ref open the file, and the
  kit's default-on contract says an unread switch loosens nothing. RESOLVED (agent, 2026-11-25, delegated): (a).
  options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F4 — Does a change of the policy file beside other guarded paths refuse whole?** Options: (a) whole, the remedy
  naming the split; (b) the verdict sets the policy file aside and admits the rest. (b) admits a commit that carries the
  refused file, since a hook judges a commit and not a path. RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) >
  (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F5 — Where the landed value opens the file, may a run set the key back to `owner-only` beside a low level?** Options:
  (a) yes, as at base, the limit named in the guard's header and `help/policy.md`; (b) refuse a run's change of
  `policy-file.guard` under an opened value. (b) narrows values the owner was not asked about, against S3 and the
  Non-goal above, veto 1. RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none
- **F6 — Who corrects the unit `repo.kickoff.f31` of `.governance/instructions.toml`?** Options: (a) the owner, through
  the write door, which asks the owner's terminal proof, the main loop proposing the sentence; (b) a hand edit on the
  run's branch, which the policy guard admits. (b) goes round the one write path of an instruction manifest, veto 2.
  RESOLVED (agent, 2026-11-25, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the brief `2026-11-25-prompt-TOOL-dBoundRoles-95-spec-brief` and the owner's
  answer on `TOOL-dBoundRoles-23` F6.

## 10. Reuse audit

The seams extended are `tools/policy/guard.py#check_run_mandate`, its callers, and the subprocess form
`tools/policy/guard.py#check_mirror_render` already uses for `policy.py`; `check_parent_sides` and `check_raise_shape`
are kept as they are; the fixtures extend `GUARD_RUN` of `tools/policy/check_policy.py` and the plants of
`tools/loop/guard.py`. `python tools/codebase-map/reuse_lookup.py "admit a live run's commit to a guarded policy file"`
ranked name neighbours and no other admission. `tools/roles/roles_lib.py#read_policy_setting` reads a key by the same
subprocess and the same `source` test; the guard spells its own since a kit imports no sibling kit. The recall probe
returned PLAY-dOrderedCharter-84, TOOL-dDeclaredLoop-2, TOOL-dWitnessedBar-6 F7, which extended the 2026-11-12 ruling to
`OWNER_ONLY_KEYS`, and TOOL-dGroundRules-13, an ask for a step's write that this unit leaves as it is.

Rejected candidates and the test that rejected each: the wrapper's re-admission, by the install with no loop kit, whose
verdict is the minimal guard's alone; the reader's default, by the source line of `read_revision`, which loads the
working tree's catalogue.

Recall terms used: `python tools/memory-recall/query.py "does the policy guard admit a live run's change to the policy file under owner-only" --terms "check_run_mandate policy-file.guard owner-only run-branch guarded-paths agents-within-mandate landed-revision minimal-guard policy_edit guard-self effort-floor PLAY-dOrderedCharter-84"`
