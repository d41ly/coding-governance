# TOOL-dDeclaredLoop-2 — the guard, the TTY policy command and the default floor

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 15 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0087@5eb8d36a whole

**Carries:** node:policy-key.floor

**Carries:** node:policy-key.policy-file.guard

**Carries:** node:policy-key.policy-file.proof

**Carries:** node:policy-key.policy-file.on-missing-expansion

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

The policy file gets its real guard: a verdict that reads `policy-file.guard` and `policy-file.proof`,
a policy command that writes only after an interactive terminal confirms it and stamps a
`Gov-Policy:` trailer, a push arm that checks the trailer, and the default floor's four invariants,
each switched by `floor` and only under the guard. The guarded command admits one agent write, a
run's raise of one measured-file cap under `budgets.*` on the four conditions
`tools/template-size-limits.txt:16-24` states, and refuses every other agent write as
`policy-file.guard` says (gap-spine-02, gap-spine-07; v2 `[floor]` and `[witnesses]`, v2:1723-1741;
the whole-design audit's C2-F9; the owner's FK-7-1).

## 2. Scope (IN)

- **S1** — The guard verdict, `tools/loop/guard.py --staged`, which wraps dGroundRules-6's minimal
  guard rather than copying it. It reads `policy-file.guard` through
  `python tools/policy/policy.py get policy-file.guard` and, for a staged change to any path
  `tools/policy/guarded-paths.txt` lists at HEAD, applies the value's rule of §4. Under
  `owner-only` its agent arm is the minimal guard itself, run as
  `tools/policy/guard.py --staged`, so the one admitted shape has one implementation.
  Observed by AC1, AC2, AC3, AC5, AC6, AC7.
- **S2** — The floor, `tools/loop/floor.py`: `FLOOR_INVARIANTS`, the four member names
  `verdict-before-move`, `record-changes`, `guard-self` and `no-actor-witness` (I11), and
  `read_floor(repo)`, which reads the `[floor]` table at the landed revision through dGroundRules-2's
  `read_policy_text` and `parse_policy`, every absent member reading `on` (v2:1154's "all on"), an
  unknown member or a value other than `on` and `off` refused. Its CLI `floor.py get <member>`
  prints `on` or `off`. Observed by AC4, AC12.
- **S3** — The guard's own switch (`floor.guard-self`): a staged change that alters
  `policy-file.guard`, `policy-file.proof`, any `floor` member, or `tools/policy/guarded-paths.txt`
  is refused for every agent commit under every value of `policy-file.guard`, so an invariant
  switched off without the owner's terminal is refused. Observed by AC4.
- **S4** — The TTY policy command, `python tools/loop/policy_edit.py <verb>`, with the write verbs
  `set <key> <value>` and `raise <cap> <new>` and the read verb `propose`. A write checks the value
  against its catalogue row with dGroundRules-1's `check_value`, writes `.governance/policy.toml`,
  writes the change record (I13) for the same commit, and prints the `Gov-Policy:` trailer line the
  commit must carry. `set` writes only when the shared terminal proof of S5 holds; without it, it
  prints the proposal and writes nothing. `raise` is the one verb admitted without the proof, and
  only on the four conditions of §4. Observed by AC8, AC9.
- **S5** — The shared guarded-write factory, extracted at its second instance (I12): the terminal
  proof and its confirmation prompt, `check_terminal_proof`, and the write-then-record step,
  `write_guarded`, canonical in `tools/lib/guarded_write.py` and carried inline, between
  `# >>> guarded_write_py` and `# <<< guarded_write_py`, in `tools/loop/policy_edit.py` and
  `tools/playbook/instructions_edit.py`, held by a `guarded_write_py` row of
  `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS`. `instructions_edit.py`'s own terminal check is
  re-pointed to the inline block in the same unit. Observed by AC10.
- **S6** — The push arm, `tools/loop/guard.py --push-range <base>..<tip>`, called from
  `.githooks/pre-push`: every commit in the range whose diff changes `.governance/policy.toml`
  carries a `Gov-Policy:` trailer, read through `commit_trailers.py`'s `read_commits` with that key, naming each changed key with
  its old and new value, and adds a change record; one that does not is refused, naming the commit
  and the key (`floor.record-changes` for policy changes). Observed by AC11.
- **S7** — `policy-file.proof`'s values: `tty-cli` is S5's proof; `signed` and `both` select the
  layered proof v2 places in `[planned]`, which no component implements, and are read as
  `policy-file.on-missing-expansion` says. Observed by AC12.
- **S8** — `policy-file.on-missing-expansion`, its rule as one function,
  `check_expansion_value(key, value)` in `tools/loop/guard.py`, over `[[selects]]` rows of
  `tools/loop/loop.toml`, each naming a key, a value and the extension point that value needs. When
  no core row of `tools/playbook/layers.toml` declares that point, `refuse` (the default) exits 2
  naming the key, the value and the point, and `fallback-reported` reads the catalogue default and
  prints one line naming the substitution. The two rows at landing are `policy-file.proof` `signed`
  and `both`, each needing `point.instructions.signed-proof`. `instructions_edit.py`'s two load
  refusals of an absent component are re-pointed to the same function. Observed by AC12.
- **S9** — The layer point `point.instructions.guard`, appended to the `declares` list of the
  `layer.flow` row of `tools/playbook/layers.toml`, which dOrderedCharter-15 S4 waits for, so the
  instruction command's write verbs stop refusing for the guard's absence. Observed by AC13.
- **S10** — The harness refusal: a policy-path arm in `checkRouted`
  (`tools/hooks/scratch-guard.js:1113`) denies an Edit, Write, MultiEdit or NotebookEdit whose path is
  listed in `tools/policy/guarded-paths.txt`, naming `policy_edit.py` as the door. It sits inside
  the write gate's one evaluation order, which already fails closed
  (`tools/hooks/scratch-guard.js:1549`). Observed by AC14.
- **S11** — The pre-commit block of dGroundRules-6 S4 re-pointed: its staged-path test and terminal
  admission stay, and the verdict it runs becomes `tools/loop/guard.py --staged`. Observed by AC15.
- **S12** — The leg `loop guard fixtures` in `tools/gate-legs.json`, running
  `python tools/loop/guard.py --fixture`, whose cases plant every admitted and refused shape of §4.
  Observed by AC1 to AC12.
- **S13** — The section "Who may change the policy file" of `help/policy.md` rewritten for the guard
  values, the command and the floor. Observed by AC16.
- **S14** — The switch readers: each invariant's enforcing site reads its member through
  `read_floor` and, at `off`, prints `floor: <member> off` and reports instead of refusing. The sites:
  `.githooks/pre-push`'s bar refusal (`verdict-before-move`); unit 3's `check_transition_channels` in
  `tools/loop/loop_transition.py` and S6's push arm (`record-changes`); step 2 of the verdict
  (`guard-self`); and unit 5's `check_witness_classes()` in `tools/loop/loop_lib.py`, which refuses an
  `actor` witness off the shrink-only list (`no-actor-witness`). Those two loop modules land before this
  unit, so this unit adds the read to each. Observed by AC17.

## 3. Non-goals (OUT)

- The policy file, its catalogue, its reader and the minimal guard's admitted shape: dGroundRules'
  (`TOOL-dGroundRules-1`, `-2`, `-6`). This unit reads through them and adds no fourth shell parser
  beside `read_policy_key`. Every key this unit owns already has its catalogue row (I10).
- The change-record kind, its name grammar and its fields: dOrderedCharter's S12/S13 (I13).
- The layered proof behind `signed`. It waits in v2's `[planned]`; until then the key's value reads
  as S8 says. The threat `tty-cli` accepts, a pty wrapper giving an agent a terminal, stays accepted
  (SA-1) and is printed in the command's help.
- Harness refusals of agent writes to hooks and verdict refs, and `hooks.bypass`: no clause of this
  build names them. The arm here covers the guarded paths list alone.
- The enforcement behind `floor.verdict-before-move` and `floor.no-actor-witness`: the pre-push bar
  run and unit 5's class rule enforce them; this unit gives each its switch and the switch's reader.
- Condition 2 of `tools/template-size-limits.txt:16-24`, a comment block's stated rule, is checked
  only for an explicit `reserved: owner` line; any other stated rule is left to the change record's
  argument, as dGroundRules-6 leaves it.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py`, the one trailer reader S6 reads `Gov-Policy:` through; without it the push arm would be a fifth trailer parser
- **consumes-from** `TOOL-dDeclaredLoop-5` — the refused witness class `actor` and `check_witness_classes()`, which `floor.no-actor-witness` switches; without it the invariant names nothing to refuse
- **consumes-from** `TOOL-dDeclaredLoop-3` — the `Gov-Transition` trailer and `check_transition_channels`, which `floor.record-changes` switches for stage transitions as S6 holds `Gov-Policy:` for policy changes
- **consumes-from** external — dGroundRules' policy kit (`tools/policy/policy.py` `get`, `check_value`, `read_policy_text`, `parse_policy`, `tools/policy/guard.py --staged`, `tools/policy/guarded-paths.txt`), dOrderedCharter-15's `instructions_edit.py`, dOrderedCharter-16's `tools/playbook/layers.toml` and dOrderedCharter's `change` record kind, each landed before this build's build run
- **hands-off** external — the layered proof behind `signed`, and harness refusals of agent writes to hooks and verdict refs, to the builds that own them

## 4. Design

### Evidence

- The minimal guard admits one shape and reads neither key: S2 and S3 of
  `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md`; its §3 hands this
  guard the job of reading `policy-file.guard` and `policy-file.proof` and retiring its block.
- v2's `[floor]`: four invariants, "each switchable only under the policy guard (R5.1)"
  (v2:1723-1728). `[witnesses]`: harness refusals of agent writes to the policy file, and "a policy
  CLI that needs an interactive terminal" (v2:1730-1741).
- The walkthrough's guard unit: "a CLI that changes policy only after an interactive terminal
  confirmation and stamps a trailer; a push gate that checks the trailer; the four floor invariants"
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:127-130`).
- R4.2: owner-only by default, switchable to agents with a recorded reason or agents within a
  mandate, and "the guard protects its own switch"
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md:199-209`).
- The four conditions of a run's raise, the one statement of them:
  `tools/template-size-limits.txt:16-24`.
- The catalogue types `floor` as `{ type = "map", of = ["on", "off"] }` (dGroundRules-1 §4, the
  `allowed` grammar), with no member list, so the members are this unit's constant.
- The write gate's one evaluation order is `checkRouted` (`tools/hooks/scratch-guard.js:1113`); a
  throw inside it denies (`tools/hooks/scratch-guard.js:1549`).
- dOrderedCharter-15 S4 refuses every instruction write "while no core row of the layer register
  declares `point.instructions.guard`"; its S5 refuses `signed` and `both` of `instructions.proof` at
  load as an absent component, the rule S8 generalises at its second instance.
- An agent's shell has no terminal: dGroundRules-6 §4 measured `[ -t 0 ]`, `[ -t 1 ]` and `[ -t 2 ]`
  false on 2026-10-23.

### The verdict — `guard.py --staged`

Run by the pre-commit block only when a guarded path is staged and stderr is not a terminal, so
every call is an agent's commit. In order:

1. The guarded touch set, as the minimal guard reads it: the list at HEAD intersected with the
   staged names. Empty: exit 0.
2. Guard-self (S3): when `floor.py get guard-self` prints `on`, a staged change to
   `policy-file.guard`, `policy-file.proof`, any `floor` member or the list file is refused, naming
   the key and `floor.guard-self`. This runs before the value's rule, so no value of
   `policy-file.guard` admits it.
3. The value's rule, `policy-file.guard` read at the landed revision:

| Value | An agent's staged write is admitted when |
|---|---|
| `owner-only` (default) | `tools/policy/guard.py --staged` exits 0: the one `budgets.*` raise, its RAISED argument and decision row; every other write refused |
| `agents-with-reason` | only `.governance/policy.toml` changed, a change record (I13) naming each changed key as `policy.<key>` is staged, and `memory/DECISIONS.md` gains a row |
| `agents-within-mandate` | the `agents-with-reason` conditions hold, and the branch is the `run-branch:` of a run-state file whose derived phase is not terminal |

4. Every refusal prints `loop-guard: refused · <path> · <why>` and the remedy: the owner commits from
   a terminal, or an agent writes through `policy_edit.py`. Admission prints
   `loop-guard: admitted · <rule>`.

The value is read from the landed revision, never the staged file, so a commit cannot loosen the
rule that judges it. An invalid policy file reads as `policy-file.on-invalid` says, through the
reader.

### The command — `policy_edit.py`

| Verb | Proof | Writes |
|---|---|---|
| `set <key> <value> --unit <id>` | `check_terminal_proof`: stdin a terminal and the typed confirmation `yes` | the leaf, the change record, prints the trailer |
| `raise <cap> <new> --unit <id> --argument <text>` | none, the agent door | the cap, its RAISED comment, the change record, the decision row line it prints for the caller |
| `propose <key> <value>` | none | nothing; prints the row diff and the command that would apply it |

`raise` admits only when all hold, checked in this order and each refusal named:

1. The cap is a leaf under `budgets`, neither `budgets.enforce` nor `budgets.pinned`, its last
   segment a file tracked at HEAD, and `<new>` an integer larger than the value at HEAD.
2. Condition 1 of the four: the working tree's file, measured CR-stripped in bytes, exceeds the old
   value.
3. Condition 2: the comment block directly above the cap carries no `reserved: owner` line.
4. Condition 3: the command writes `# RAISED <old> -> <new>, <date>, <unit>, measured <n> bytes,
   <argument>` directly above the cap, the shape the minimal guard checks.
5. Condition 4: the change record names `budgets.<cap>`, and the command prints the decision row
   the caller must add to `memory/DECISIONS.md` in the same commit; the minimal guard refuses the
   commit without it.

The trailer is `Gov-Policy: policy.<key> <old> -> <new>`, one line per changed key, `<old>` `none`
for a key the file did not set. The key is registered with the `commit` kind by unit 23 (I7).

### The factory — `guarded_write.py`

`check_terminal_proof(prompt)` returns the proof `tty-cli` when stdin is a terminal and the line
typed is `yes`, else `None`. `write_guarded(path, new_text, record)` writes the file and the change
record together and removes both when either write fails. `policy_edit.py` and
`instructions_edit.py` carry the block inline because a kit may not import a sibling kit; the
parity row holds each copy to the canonical.

### The floor

| Member | What it keeps | Its reader |
|---|---|---|
| `verdict-before-move` | a binding verdict runs before the default branch moves | `.githooks/pre-push`, before the bar: `off` prints `floor: verdict-before-move off — the bar's red is advisory` and does not refuse on red |
| `record-changes` | every policy change and stage transition recorded | S6's push arm for `Gov-Policy:`; unit 3's `check_transition_channels` for `Gov-Transition` |
| `guard-self` | the guard protects its own switch | S3, step 2 of the verdict |
| `no-actor-witness` | no stage witness reads actor-typed state | unit 5's `check_witness_classes()`, refusing an `actor` witness off its list |

Every member defaults `on`. Switching one `off` is a staged change to a `floor` member, which S3
refuses for every agent; only the owner's terminal commit lands it.

### Data model

```toml
# tools/loop/loop.toml — rows this unit adds
[[selects]]
key = "policy-file.proof"
value = "signed"
point = "point.instructions.signed-proof"

[[selects]]
key = "policy-file.proof"
value = "both"
point = "point.instructions.signed-proof"
```

Each key this unit reads is read through dGroundRules' reader once it lands, with v2's catalogue
default until then: `policy-file.guard` `owner-only`, `policy-file.proof` `tty-cli`, `floor` all
on, `policy-file.on-missing-expansion` `refuse` (v2:1151, 1152, 1154, 1268).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_staged`, `check_push_range`, `check_expansion_value`, `main` | function | `tools/loop/guard.py` |
| `--staged`, `--push-range`, `--fixture` | CLI flags | `tools/loop/guard.py` |
| `FLOOR_INVARIANTS`, `read_floor` | constant, function | `tools/loop/floor.py` |
| `set`, `raise`, `propose` | CLI verbs | `tools/loop/policy_edit.py` |
| `check_terminal_proof`, `write_guarded` | function | `tools/lib/guarded_write.py` |
| `guarded_write_py` | parity row and block marker | `tools/lib/resolve-python.test.sh` |
| `[[selects]]` | table | `tools/loop/loop.toml` |
| `loop guard fixtures` | gate leg | `tools/gate-legs.json` |

Each function leads with a verb `.lexicon.conf` declares, in `py.function`'s snake case.

### The fixture cases

`guard.py --fixture` builds one repository per case under `%TEMP%` with a short prefix, holding the
policy kit, the loop kit, a tracked `big.md` of 118 bytes and a policy file whose `[budgets]` sets
`"big.md" = 100`; `--plant <case>` runs one.

| Case | Plant | Outcome |
|---|---|---|
| `raise-admitted` | `policy_edit.py raise big.md 120` and its decision row | exit 0; a refusal is RED |
| `raise-no-record` | the cap raised by hand, no change record, no row | exit 1 |
| `raise-lowered` | `big.md` set to 90 by hand | exit 1, "a lowering" |
| `floor-off-agent` | `floor.no-actor-witness = "off"` staged, under each guard value | exit 1 naming `floor.guard-self`, three times |
| `other-write-owner-only` | `review.max-rounds` set, with a change record | exit 1 naming `policy-file.guard` |
| `with-reason-admitted`, `with-reason-no-row` | `agents-with-reason`, a key set with and without the decision row | exit 0, then exit 1 |
| `mandate-live`, `mandate-none` | `agents-within-mandate`, inside a live run's branch, then on a branch no run names | exit 0, then exit 1 |
| `push-no-trailer` | a commit changing the policy file with no `Gov-Policy:` line, graded by `--push-range` | exit 1 naming the commit |
| `proof-signed-refuse`, `proof-signed-fallback` | `policy-file.proof = "signed"` under each value | exit 2 naming the point, then exit 0 with the substitution line |
| `floor-readers` | an `actor` witness off the list and a transition with one channel missing, under the floor all `on`, then with `no-actor-witness` and `record-changes` `off` at the landed revision | both refuse, then both report and pass |

### Alternatives rejected

- **Extending `tools/policy/guard.py` in place.** One file, but the floor, the command and the push
  arm are the loop's, and the policy kit would then read the run-state file for
  `agents-within-mandate`, a dependency on the unattended kit's grammar it does not have today.
- **The guard's own copy of the raise shape.** Two implementations of one admitted shape; the
  minimal guard runs as a subprocess instead.
- **The floor members as catalogue rows.** I10 forbids a row; the map type carries their values.

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/floor.py`
- `tools/loop/policy_edit.py`
- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/loop_transition.py`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `tools/lib/guarded_write.py`
- `tools/lib/resolve-python.test.sh`
- `tools/playbook/instructions_edit.py`
- `tools/playbook/layers.toml`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `.githooks/pre-commit`
- `.githooks/pre-push`
- `tools/gate-legs.json`
- `help/policy.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`

## 5. Production-readiness checklist

- security — the change narrows agent writes: the harness arm denies tool writes to the guarded
  paths, the verdict reads its rule from the landed revision, and guard-self runs before every value.
  The accepted residual is SA-1's pty wrapper and `git commit --no-verify`, both printed.
- perf / scale — one Python spawn per commit that stages a guarded path, as today; the push arm
  reads trailers once per pushed range.
- error / empty / loading states — an absent list exits 0 as nothing guarded; an unparsable policy
  file reads as `policy-file.on-invalid` says; a missing launcher refuses, as dGroundRules-6's block
  does.
- observability — one `loop-guard:` line per verdict naming the rule and each failed condition; the
  fallback line under `fallback-reported`.
- risks — a broken verdict blocks the owner's commits too only where stderr is not a terminal; the
  owner's terminal path does not run it.
- testing — the fixture cases above, a parity row, a scratch-guard payload probe.
- migration — none for data; the pre-commit block's verdict path moves in one commit.
- user docs — `help/policy.md`, its section "Who may change the policy file".

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant raise-admitted` runs, the staged single-cap raise
  written by `policy_edit.py raise` exits 0.
  Red when: the verdict refuses it, the arm the clause requires red if the guard refuses.
- **AC2** — When `python guard.py --fixture --plant raise-no-record` runs, it exits 1 naming the
  missing change record.
  Red when: a raise with no change record is admitted.
- **AC3** — When `python guard.py --fixture --plant raise-lowered` runs, it exits 1 with "a
  lowering".
  Red when: a lowered cap is admitted.
- **AC4** — When `python guard.py --fixture --plant floor-off-agent` runs, each of the three guard
  values refuses the staged `floor.no-actor-witness = "off"`, naming `floor.guard-self`.
  Red when: any value admits an invariant switched off without the guard.
- **AC5** — When `python guard.py --fixture --plant other-write-owner-only` runs, it exits 1 naming
  `policy-file.guard`.
  Red when: an agent write other than the raise is admitted under `owner-only`.
- **AC6** — When `python guard.py --fixture --plant with-reason-admitted` and then
  `--plant with-reason-no-row` run, the first exits 0 and the second exits 1.
  Red when: `agents-with-reason` admits a write with no recorded reason, or refuses one that has it.
- **AC7** — When `python guard.py --fixture --plant mandate-live` and then `--plant mandate-none`
  run, the first exits 0 and the second exits 1.
  Red when: `agents-within-mandate` admits a write outside a live run.
- **AC8** — When `python policy_edit.py set review.max-rounds 4 --unit TOOL-x-1 </dev/null` runs in a
  fixture repository, it prints the proposal, writes nothing and exits 1.
  Red when: a non-terminal `set` writes the policy file.
- **AC9** — When `python policy_edit.py raise big.md 120 --unit TOOL-x-1 --argument probe` runs in a
  fixture repository whose `big.md` measures 118 bytes, it writes the RAISED comment, the change
  record and prints one `Gov-Policy:` line; with `big.md` at 90 bytes it refuses naming condition 1.
  Red when: the raise is admitted with the file under its old cap.
- **AC10** — When the two blocks are cut with
  `sed -n '/# >>> guarded_write_py/,/# <<< guarded_write_py/p'` from `instructions_edit.py` and from
  the canonical `guarded_write.py`, `cmp` finds them equal.
  Red when: either copy differs from the canonical.
- **AC11** — When `python guard.py --fixture --plant push-no-trailer` runs, it exits 1 naming the
  commit and the policy file `policy.toml`.
  Red when: a policy change with no `Gov-Policy:` trailer passes the push arm.
- **AC12** — When `python guard.py --fixture --plant proof-signed-refuse` and then
  `--plant proof-signed-fallback` run, the first exits 2 naming `point.instructions.signed-proof`
  and the second exits 0 printing the substitution of `tty-cli`; `floor.py get guard-self` prints
  `on` on a policy file with no `[floor]` table.
  Red when: a value selecting an absent component is read silently, or an absent member reads `off`.
- **AC13** — When `grep -n point.instructions.guard layers.toml` runs in the playbook kit, it prints
  the `layer.flow` row's `declares` line, and `python instructions_edit.py propose` no longer prints
  the guard's refusal.
  Red when: the point is absent and the instruction command still refuses for the guard.
- **AC14** — When `node tools/hooks/scratch-guard.js` is fed a PreToolUse Write payload for the
  policy file `policy.toml`, it prints a deny naming `policy_edit.py`.
  Red when: the write gate admits a tool write to a guarded path.
- **AC15** — When `grep -n 'loop/guard.py' .githooks/pre-commit` runs, it prints the block's verdict
  call, and `grep -c 'policy/guard.py --staged' .githooks/pre-commit` prints 0.
  Red when: the block still runs the minimal guard directly.
- **AC16** — When `grep -n policy_edit.py policy.md` runs under `help/`, it names the command under
  "Who may change the policy file".
  Red when: the page is not current.
- **AC17** — When `python guard.py --fixture --plant floor-readers` runs, `check_witness_classes()` and
  `check_transition_channels` each refuse their planted case under the floor all `on`, and each prints
  `floor: <member> off` and passes once the landed revision sets that member `off`.
  Red when: a switch has no reader, so turning it off changes nothing, or `on` stops refusing.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `govkit acceptance matrix` · `playbook render selftest` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC11 AC12 AC17 · each `--plant` case staged in its fixture repository, and the admitted case red with the verdict forced to refuse · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC14 · a Write payload for each guarded path · the suite's assertion floor raised by the arms added
New arm: tools/lib/resolve-python.test.sh · covers AC10 · the `guarded_write_py` row with one copy edited · none

## 8. Open questions

- **F1 — Where does the guard verdict live?** (a) `tools/loop/guard.py`, wrapping the minimal guard by
  subprocess; (b) `tools/policy/guard.py` extended in place; (c) a loop module importing the policy
  kit's shape check. (c) breaks the rule that a kit never imports a sibling. (b) puts the run-state
  grammar inside the policy kit. (a) keeps one implementation of the admitted shape and follows I1
  and I12. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the pre-commit block's verdict re-pointed to the loop guard ·
  widens: none · relaxes: none
- **F2 — Where does the shared terminal proof live?** (a) `tools/lib/guarded_write.py`, carried
  inline in both commands under a `PARITY_ROWS` row; (b) in the playbook kit, imported by the loop;
  (c) a second copy. (b) is a sibling import and (c) is the copy the [reuse] rule forbids at a second
  instance. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the instruction command's terminal check re-pointed to the inline block
  · widens: none · relaxes: none
- **F3 — The floor members' names.** v2:1723-1728 and R5.1 state the four invariants in prose; I11
  spells them `verdict-before-move`, `record-changes`, `guard-self` and `no-actor-witness`. Rung 1, the
  invariants as v2 states them, spelled as the brief fixes. RESOLVED (agent, 2026-10-24, delegated):
  I11's four. widens: none · relaxes: none
- **F4 — What do `agents-with-reason` and `agents-within-mandate` admit?** R4.2 offers "agents with a
  recorded reason" and "agents within a mandate". (a) A recorded reason is a change record plus a
  decision row in the same commit; a mandate is a live run whose `run-branch:` is the commit's
  branch. (b) A free-text reason in the trailer. (b) is text anyone types and records nothing a gate
  reads. Recommendation (a). Rung 1, R4.2's words. RESOLVED (agent, 2026-10-24, delegated): (a).
  widens: none · relaxes: none
- **F5 — Does the harness arm cover hooks and verdict refs too?** v2's `[witnesses]` lists all three;
  this clause names the policy file's guard. Covering hooks would refuse tool writes to `.githooks/`,
  a write surface no clause of this build prices. Recommendation: the guarded paths list only, the
  rest handed off. Rung 3. RESOLVED (agent, 2026-10-24, delegated): the guarded paths list only.
  grants: PLAY-dClosedLoop-3 the scratch-guard write gate's policy-path arm · widens: none ·
  relaxes: none
- **F6 — Where are the values that select an absent component declared?** (a) `[[selects]]` rows of
  the loop definition, one function reading them; (b) a field on each catalogue row; (c) each
  reader's own refusal, as dOrderedCharter-15 does today. (b) edits rows I10 says this unit leaves
  alone, and (c) is the per-reader copy gap-spine-07 names. Recommendation (a), re-pointing
  dOrderedCharter-15's two refusals. Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the instruction command's two load refusals re-pointed · widens: none ·
  relaxes: none
- **F7 — Which layer row declares `point.instructions.guard`?** dOrderedCharter-15 S4 reads any core
  row; the guard is the flow's, and `layer.flow` is a core row. Rung 1. RESOLVED (agent, 2026-10-24,
  delegated): `layer.flow`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.

## 10. Reuse audit

The seams extended are dGroundRules-6's minimal guard, `tools/policy/guard.py --staged`, which the
verdict runs as its `owner-only` arm and never re-implements; the write gate's evaluation order,
`checkRouted` at `tools/hooks/scratch-guard.js:1113`, which gains one arm; the pre-commit block
dGroundRules-6 S4 places, whose verdict path moves; dOrderedCharter-15's `instructions_edit.py`,
whose terminal check becomes the extracted factory at its second instance; and the `PARITY_ROWS`
table at `tools/lib/resolve-python.test.sh:168`. For the floor, the command, the push arm and the
expansion rule no existing seam fits: `python tools/codebase-map/reuse_lookup.py "refuse an agent
write to the policy file unless an interactive terminal confirms it"` ranked only name-stem hits
(`write`, `load_policy`, `CensusRefused`), and the one terminal probe in the tree,
`skills/session-kickoff/manifest-check.sh:295`, reads a session id, not a proof. The scout's citation
of `checkRouted` at :1113 and the fail-closed catch at :1549 agreed with source; no hit disagreed.

Recall terms used: `python tools/memory-recall/query.py "who may raise a measured file cap and how is
the policy file guarded" --terms "policy guard minimal guard RAISED budgets cap template-size-limits
owner terminal TTY proof floor"`
