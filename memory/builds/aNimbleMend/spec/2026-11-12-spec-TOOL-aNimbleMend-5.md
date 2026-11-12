# TOOL-aNimbleMend-5 — the pass-leg runner: the declared legs run over one pass's diff through the bar runner, with a run record and an overrun printed as a finding

**Status:** OPEN · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-5-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-5-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A red a unit pass causes is seen one full bar later, because nothing runs between passes. This unit
ships the one command that runs the declared pass legs over a pass's diff, records what ran, and
says when the run cost more than its budget.

## 2. Scope (IN)

- **S1** — A new adapter, `tools/run-gates/pass-legs.sh`, invoked as
  `bash <prefix>/run-gates/pass-legs.sh --base <rev>`. It holds no leg command and no verdict logic
  of its own: it starts the bar runner beside it once and passes its output through unbuffered.
  `--base` is required and must resolve to a commit; otherwise the adapter exits 2 naming the value
  and starts nothing. Observed by AC1 and AC2.
- **S2** — The list is derived at each run: every row of the leg manifest whose `pass_leg` field,
  the one TOOL-aNimbleMend-2 declares, is true, in manifest order, each row copied whole. The
  adapter writes that list as a JSON array under the git dir and hands it to the runner through
  the existing `GATE_LEGS` seam. No leg name is typed in the adapter. Observed by AC1.
- **S3** — The run is scoped to the pass. The adapter sets `GATE_BASE` to the resolved base, so each
  leg's own `guard` decides against the pass's diff, and it empties `GATE_FULL` and
  `GATE_SELFTESTS`, so a flag exported by the calling session cannot widen the run. Observed by AC3.
- **S4** — The switch. Before it starts anything the adapter asks the key `pass.fast-legs` once,
  under the ask contract TOOL-aNimbleMend-1 states, and follows that contract's five rows. On `off`
  it prints nothing, starts no runner, writes no file and exits 0. A refused read and a value
  outside the pair end the run the same way, each with the one line the contract names. Where no
  policy kit resolves it runs, with the contract's one NOTE line on stderr. Observed by AC4.
- **S5** — The run record, `<git-dir>/gate-pass-legs.txt`, written atomically at mode 600 after the
  runner returns, in the shape of §4, "The run record". Observed by AC5.
- **S6** — Two findings, each one line on stdout opening `pass-legs: FINDING` and each also a key of
  the record: the run's wall time exceeded the limit, and a declared leg did not run because the
  runner held it. A wall time above the budget and at or under the limit prints one
  `pass-legs: NOTE` line instead. The budget is `PASS_BUDGET_SECONDS` of TOOL-aNimbleMend-2's
  module, and the limit is read from where TOOL-aNimbleMend-3 declares its tolerance. Neither
  figure is typed in the adapter. A finding moves no exit code. Observed by AC6
  and AC7.
- **S7** — The exit code is the runner's, unchanged. An empty list starts no runner, prints
  `pass-legs: 0 legs declared, nothing ran`, writes a record whose verdict reads `EMPTY`, and
  exits 0. Observed by AC1, AC5 and AC8.
- **S8** — `tools/run-gates/README.md` gains a section naming the command, the record path, the two
  findings and the costs §4 states under "What a pass-leg run costs the bar's records". Observed by
  AC9.

## 3. Non-goals (OUT)

- Which legs carry the field, and the rule that derives them. That is TOOL-aNimbleMend-2.
- The budget gate over the declared ceilings, the per-leg cap and the excluded classes. That is
  TOOL-aNimbleMend-3. This unit reports a held leg; it refuses no manifest.
- The scoped legs themselves. That is TOOL-aNimbleMend-4.
- Who calls the adapter and what a red or a finding does to the run. That is TOOL-aNimbleMend-7.
- Any change to the bar runner. The adapter uses four of its existing environment seams and adds
  no knob, so the class `a-runner-knob-owes-a-push-class` has nothing to select.
- A test seam for the switch, a `--dry-run`, a `--legs` filter, or a default base. None is needed by
  a caller this build names.
- The page under `help/`. That is TOOL-aNimbleMend-11.
- The kit version bump, which the lander's `mint` moves once.

### Edges

- **consumes-from** `TOOL-aNimbleMend-1` — the key `pass.fast-legs` and the ask contract. Without
  it S4 has nothing to ask and the adapter cannot be switched off.
- **consumes-from** `TOOL-aNimbleMend-2` — the `pass_leg` field on a manifest row, and the budget
  constant of `tools/run-gates/pass_legs.py`. Without it S2 selects nothing and every run is the
  empty list of S7.
- **consumes-from** `TOOL-aNimbleMend-3` — the declared limit above the budget. Without it S6
  cannot tell a run inside the tolerance from an overrun.
- **hands-off** `TOOL-aNimbleMend-6` — the adapter is a new gate runner by file name, which the
  role-gate arm must refuse to a role agent and the gate guard must leave admitted.
- **hands-off** `TOOL-aNimbleMend-7` — calling the adapter after each unit pass's commit with that
  pass's base, and acting on its exit code and findings.
- **hands-off** `TOOL-aNimbleMend-8` — a red pass leg reaches the gate ledger because the adapter
  runs through the bar runner, and the lane reads it there.

## 4. Design

### Evidence

Read at 97e0841d. Line numbers are of `tools/run-gates/run-gates.sh` unless another file is named.

| Fact | Where |
|---|---|
| The manifest path is overridable: `LEGS_FILE="${GATE_LEGS:-...}"`. | `:372` |
| An explicit `GATE_BASE` outranks the derived guard base. | `:515-518` |
| A guard is decided by `changed()`, which diffs the base against the working tree, and runs every leg when `GATE_FULL` is set or the base is empty. | `:539` |
| A leg of `subject = kit` or `chunk = selftests` is held unless `GATE_SELFTESTS` is set. | `:3259-3262` |
| The run id is pinned by `GATE_RUN_ID`, and the run record opens at `<git-dir>/gate-run/<id>`. | `:1585`, `:2720-2722` |
| Each leg that ran leaves one `<i>.leg` row of eight tab-separated fields: name, status, rc, seconds, start, end, key, foreign. Status is `ok`, `fail` or `timeout`. | `:4073-4086` |
| The `verdict` file carries `verdict`, `ran`, `failed`, `skipped` and `held`. | `:5684-5690` |
| A red run writes `<git-dir>/gate-last-failure.txt`. | `:5890-5893` |
| The ledger merge keeps every row this run did not measure. | `:5396-5404` |
| The turnstile queues one bar per host and `GATE_TURNSTILE=0` turns it off. | `:1586-1640` |
| `GATE_BASE` is not among the variables the runner removes before a leg starts, so a leg inherits it. | the `unset` lines `:377`, `:387`, `:556`, `:2743`, `:2753`, `:3876` |
| A shell caller in this kit resolves the policy reader with `resolve_kit_dir` and asks it with `policy.py get <key>`. | `tools/run-gates/run-gates.gov.test.sh@17d30d22:165-170` |
| The push hook trusts a full-green stamp only when its `manifest` is the kit's own. | `.githooks/pre-push#check_green_manifest` |

### The flow

1. Parse `--base <rev>`. Any other argument, or none, exits 2 with a usage line.
2. Resolve the git dir and the base with `git rev-parse --verify -q "<rev>^{commit}"`.
3. Ask the key (S4). Off ends the run here.
4. Derive the list (S2) and read the two figures (S6) with one python call that imports
   `pass_legs.py` from beside the adapter, under the launcher `tools/lib/resolve-python.sh`
   resolves, carried inline as every copy-installed kit carries it. The filtered array goes to
   `<git-dir>/gate-pass-legs.json`, replaced by rename.
5. An empty list ends the run here (S7).
6. Start the runner beside the adapter with `GATE_LEGS`, `GATE_BASE`, a pinned `GATE_RUN_ID` of the
   form `pass-<UTC stamp>-<pid>`, and `GATE_FULL` and `GATE_SELFTESTS` empty. Its stdout and stderr
   are not captured: a captured runner is the class `bounded-through-a-pipe-is-unbounded`.
7. Time the call with the shell's own `SECONDS`, whole seconds, around step 6 only.
8. Read `<git-dir>/gate-run/<id>/verdict` and each `.leg` row, write the record (S5), print the
   findings (S6), and exit with the runner's code.

### The run record

One file, `key<TAB>value` per line, the grammar the runner's own `header` and `verdict` use, so
`read_record_keys` reads it. It is replaced on every run that reaches step 5.

| Key | Value |
|---|---|
| `run_id` | the pinned id, which names the directory under `gate-run/` |
| `base` | the resolved base, full sha |
| `head` | `HEAD` when the run started, full sha |
| `started` | UTC, ISO 8601 to the second with a `Z` suffix |
| `exit` | the runner's exit code, or `-` for the empty list |
| `verdict` | the `verdict` value of the runner's own record, `EMPTY`, or `NO-VERDICT` when the runner wrote none |
| `declared` | how many rows carried the field |
| `wall_s` | whole seconds around the runner call |
| `budget_s` | the declared budget |
| `limit_s` | the declared limit |
| `over` | `none`, `tolerance` or `limit` |
| `held` | the runner's `held` count |
| `leg` | one line per declared leg, in manifest order: name, status, seconds |

A `leg` line's status is `ok`, `fail` or `timeout`, taken from that leg's `.leg` row, or from its
`.retry.leg` row where one exists. A declared leg with no row reads `not-run` with `-` for seconds:
its guard skipped it, or the runner held it. The record carries `head`, so a reader can tell a
record earned at another commit from one earned at this one.

### The findings

| Condition | Line |
|---|---|
| `wall_s` above `limit_s` | `pass-legs: FINDING overrun: the run took <wall>s, over the <limit>s limit (budget <budget>s)` |
| `wall_s` above `budget_s`, at or under `limit_s` | `pass-legs: NOTE the run took <wall>s, inside the tolerance above the <budget>s budget` |
| the runner's `held` above 0 | `pass-legs: FINDING held: <n> declared leg(s) did not run, held as a self-test or a kit-subject leg` |

### What a pass-leg run costs the bar's records

These follow from running through the bar runner, and the kit README states them (S8).

- A red pass-leg run replaces `gate-last-failure.txt`, exactly as the next red bar would.
- A green run with no skipped leg and a clean tree replaces the `gate-full-green` stamp with one
  naming the filtered manifest. The push hook does not trust that stamp, so the next push runs its
  bar in full. The close's bar re-earns the stamp.
- The run adds its legs' rows to the ledger and leaves every other row standing.
- `GATE_LEGS` is inherited by every leg. A declared leg that starts a runner of its own would read
  the filtered list, the defect the ask TOOL-dPolishedVitrine-10 records. The builder greps each
  declared row's script for `GATE_LEGS` and names any hit in the ledger.

### Inventory

| Minted | Kind |
|---|---|
| `tools/run-gates/pass-legs.sh` | shipped kit file, role `engine` by the descriptor's `**` rule |
| `gate-pass-legs.txt` | untracked record under the git dir |
| `gate-pass-legs.json` | untracked filtered manifest under the git dir |
| the `pass-legs:` output prefix | stdout lines; `pass_legs.py --check` of TOOL-aNimbleMend-2 prints under the same prefix |
| the `pass-` run id prefix | a `gate-run/` directory name |

No function name, conf key, policy key or manifest field is minted here. No naming cell grades
these: `lexicon.py --suggest pass-legs.sh --as sh.file` answers that the cell is undeclared, and
the kebab spelling follows `run-gates.sh` and `gate-last-failure.txt` beside it.

### Rollout

The adapter ships with the kit and does nothing until TOOL-aNimbleMend-7 calls it. The key is the
default-off switch in reverse: on by default, one key turns it off.

### Files touched (estimate)

- `tools/run-gates/pass-legs.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **A runner of its own that reads the manifest and spawns each leg.** It would restate the
  `{prefix}` resolution, the guard rule, the ceiling kill, the hold and the per-leg record, each of
  which the bar runner owns. Rejected on reading `:2879-2979` and `:3259-3276`: a second
  implementation of five rules is the copy `[core]` forbids.
- **A `--pass-legs` flag inside the bar runner.** The runner exits from eight sites after its
  legs return (`:5504-5898`), so the record and the findings would be written at each. The adapter
  needs none of the runner's internals, only its record, and the runner's header says an edit
  there can move every leg's verdict.
- **No record, the runner's own `gate-run/<id>` only.** `GATE_RUN_KEEP` keeps five runs (`:2692`),
  and that directory holds no base, no budget and no wall time for the pass.

## 5. Production-readiness checklist

- security — the adapter runs only rows of the tracked manifest, through the runner; `--base` is
  passed to `git rev-parse` as one quoted argument and never evaluated; the record is mode 600 under
  the git dir and holds names, shas and seconds.
- perf / scale — one python call and one runner start per pass; the runner's own start cost is
  inside `wall_s` and is reported by S6.
- error / empty / loading states — an absent or unresolvable base exits 2; an empty list is S7; a
  runner that wrote no verdict reads `NO-VERDICT`; a refused run, exit 2, is passed through.
- observability — the record of S5 and the two findings of S6.
- risks — the four costs under §4, "What a pass-leg run costs the bar's records", and the queue
  wait F1 decides.
- testing — AC1 to AC9 in a scratch repository, and the arm of §7.
- migration — N/A: a new file; an adopter takes it at its next `govkit update`.
- user docs — the kit README, S8; the `help/` page is TOOL-aNimbleMend-11.

## 6. Acceptance criteria

Every criterion but AC9 runs in a scratch repository under `%TEMP%/<short-name>` that holds a copy
of the kit directory, the policy kit, and a manifest of three rows: `alpha`
unguarded and carrying the field, `beta` carrying the field with a `guard` of `watched/`, and
`gamma` unguarded and not carrying it. Each row's `argv` writes its own name to a marker file.
The fixture points `GATE_TURNSTILE_DIR` at a directory of its own, so no probe waits behind a real
bar on the host.

- **AC1** — When `bash <kit>/pass-legs.sh --base HEAD~1` runs after a commit that changed a file
  under `watched/`, the marker files of `alpha` and `beta` exist, the marker of `gamma` does not,
  and the exit code is 0.
  Red when: the adapter runs a row that does not carry the field, or filters by a typed name.
- **AC2** — When `bash <kit>/pass-legs.sh` runs with no argument, and again with
  `--base no-such-rev`, each exits 2, names the missing or unresolvable base, and writes no marker.
  Red when: an unresolvable base reaches the runner, which reads it as empty and runs every leg.
- **AC3** — When the same command runs after a commit that changed no file under `watched/`, with
  `GATE_SELFTESTS` exported non-empty in the calling shell, `alpha` has a marker and `beta` has
  none, and the record's `leg` line for `beta` reads `not-run`.
  Red when: the base is not handed to the runner, or an inherited flag bypasses the guard.
- **AC4** — When `pass.fast-legs` is `off` in the fixture's policy file at its landed revision and
  the command runs, it prints nothing, exits 0, writes no marker, and `gate-pass-legs.txt` is
  absent. With the key line deleted, the same command writes the `alpha` marker. With the policy
  kit moved out of the fixture, it writes the marker and prints one NOTE line on stderr naming the
  key.
  Red when: the adapter runs without asking the key, reads an absent key as off, or stops where no
  policy kit resolves.
  fixture: needs the policy kit copied into the scratch repository; the tree holds no such fixture
  today.
- **AC5** — When the record `gate-pass-legs.txt` under the fixture's git dir is read after AC1, it
  holds every key of §4, "The run record", `declared` reads 2, and the `leg` lines for `alpha` and
  `beta` read `ok`. After a run whose `alpha` row exits 1, the `alpha` line reads `fail`, `exit`
  reads 1, and the adapter's own exit code was 1.
  Red when: a key is missing, a failed leg reads `ok`, or the adapter exits 0 over a red runner.
  figure: 2 is DERIVED from the fixture manifest.
- **AC6** — When the fixture's copy of `pass_legs.py` and of the limit's declaration state a budget
  of 1 second and a limit of 2, and `alpha` sleeps 4 seconds, the command prints one line opening
  `pass-legs: FINDING overrun`, the record's `over` reads `limit`, and the exit code is still 0. With a limit of 600 the same run prints no
  `FINDING overrun` line and one `pass-legs: NOTE` line.
  Red when: the wall time is not compared, or a finding changes the exit code.
  figure: the fixture's three figures are PINNED in the fixture; the adapter reads them from the
  declaration and types none.
- **AC7** — When a fourth row carrying the field and `"subject": "kit"` is added and the command
  runs, it prints one line opening `pass-legs: FINDING held`, the row writes no marker, and its
  `leg` line reads `not-run`.
  Red when: a held declared leg is reported as nothing, and the run reads as full coverage.
- **AC8** — When no row carries the field and the command runs, it prints
  `pass-legs: 0 legs declared, nothing ran`, exits 0, and the record's `verdict` reads `EMPTY`.
  Red when: the adapter hands the runner an empty manifest, or prints a green over no leg.
- **AC9** — When `grep -c 'pass-legs.sh' tools/run-gates/README.md` runs, it prints at least 1, and
  `grep -c 'gate-full-green' tools/run-gates/README.md` prints one more than it did before the
  pass.
  Red when: the README does not name the command, or omits the stamp cost.
  figure: both counts are DERIVED against the pass's starting tip, recorded in the ledger.

## 7. Gates

`run-gates canary` · `docs` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates`

The kit epoch leg expects the lander's `mint`. The canary is in the held tier, and the close runs
it only if it asks for that tier.

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 AC5 AC6 AC7 AC8 · the fixture of §6 with the field stripped from `alpha`, then with the comparison of S6 removed · none

The arm for AC4 is TOOL-aNimbleMend-12's, whose scratch adopter holds the policy kit.

## 8. Open questions

- **F1 — Does a pass-leg run take the host turnstile?** The turnstile admits one bar per host at a
  time, and this run's record states a gate backstop that allows 7200 s of queue. A pass-leg run
  that queues behind another worktree's bar cannot meet 690 s by any design of its legs.
  - **Queue as a bar does.** No runner knob is set. Two gate runs never overlap on the host. The
    wall time of S6 then includes the wait, so nearly every run on a busy node prints the overrun
    finding, and the build's 690 s acceptance is not observable there.
  - **Run beside the bar.** The adapter sets `GATE_TURNSTILE=0`. The run starts at once and its
    wall time is its legs' time. It overlaps a queued bar's legs, the contention the turnstile's
    own comment measured for whole bars, here for at most the budget's ten minutes.
  - **Queue, and time the legs only.** No knob is set, and `wall_s` is read from the runner's
    record rather than the adapter's clock. The finding is true to the legs, and the pass still
    waits for however long the queue is.
  Recommendation: run beside the bar. It is the only option under which the 690 s criterion can be
  observed on a shared node, and it needs one existing knob.
  RESOLVED (agent, 2026-11-12, delegated): run beside the bar. It is the one option under which the build's 690 s criterion can be observed on a shared node, and it uses a knob the runner already has.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is the bar runner, `tools/run-gates/run-gates.sh`, driven through four environment seams
it already reads: `GATE_LEGS`, `GATE_BASE`, `GATE_RUN_ID` and the empty forms of `GATE_FULL` and
`GATE_SELFTESTS`. The adapter extends it from outside and changes no line of it.
`python tools/codebase-map/reuse_lookup.py "run a declared subset of gate legs over a diff and
record the run"` returned name-stem neighbours only, `run`, `legs`, `leg` and `records` among them,
and none runs a subset of the manifest, so the seam was read from the runner's source as §4,
"Evidence", cites it. Recall returned the ask TOOL-dPolishedVitrine-10, on a suite that fails when
it inherits `GATE_LEGS`, which is the fourth cost §4 states, and the aFrugalTurnstile closing
review's note that a subset run under `GATE_LEGS` earns a stamp, which is the second.
`gotchas.py --for-paths` over the estimate selected `a-runner-knob-owes-a-push-class`,
`bounded-through-a-pipe-is-unbounded` and `fixture-passes-by-finding-nothing`; §3, the flow's
step 6 and AC1's `gamma` row answer them in that order.

Recall terms used: `python tools/memory-recall/query.py "how does a run execute a subset of gate
legs scoped to a diff and which hook admits or refuses a gate runner during a pass" --terms "pass
leg GATE_LEGS GATE_BASE manifest guard run record gate-guard scratch-guard role-gate GATE_RUNNERS
turnstile ceiling"`
