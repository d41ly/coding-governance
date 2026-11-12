# TOOL-aNimbleMend-13 — the first pass-leg run's findings repaired: a pass leg grades the whole manifest, the rule selects no leg the runner holds, and three texts say what the code does

**Status:** INPROGRESS · rev-1 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-13-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-13-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-13-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-13-brief.md) | research | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-13-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-13-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The first pass-leg run of this build, over `bde79f210`, went red on eight legs, and six of those
reds are defects of this build and no finding about the pass. This unit repairs the five defects
behind them, so that a pass-leg run in this repository reds only on a real red of the pass it
grades.

## 2. Scope (IN)

- **S1** — `tools/run-gates/pass-legs.sh` writes each selected row with its `argv` behind the leg
  shim the held tier already uses, `bash <kit>/run-held-wsl.sh --leg`, so every pass leg starts
  with `GATE_LEGS` unset and reads the manifest beside its kit. The runner still receives the
  filtered list and starts only its rows. Observed by AC1 and AC2.
- **S2** — `tools/run-gates/pass_legs.py#check_pass_eligible` answers a new reason, `kit-subject`,
  for a row whose `subject` is `kit`, placed second in `EXCLUSIONS`, after `selftest`.
  `tools/run-gates/pass_legs.py#check_pass_budget` reads that reason for its held finding and
  keeps the finding's sentence. Observed by AC3 and AC4.
- **S3** — The `pass_leg` field of `tools/gate-legs.json` is written again by
  `python tools/run-gates/pass_legs.py --apply`, on node `a`, from the tracked files. No hand
  types a field. Observed by AC5.
- **S4** — The `why_no_regenerate` sentence of `tools/run-gates/kit.toml` names `GOVKIT_RERENDER`
  and says what stays true of the adopter whatever the flag reads. Observed by AC6 and AC7.
- **S5** — The nested function `strip` of `tools/run-gates/pass_legs.py#render_pass_field` takes
  the name `remove_pass_field`, at its definition and its two calls. The lexicon's pin stays where
  it is. Observed by AC8 and AC9.
  **Readers:** by name: `tools/run-gates/pass_legs.py`, the only file that spells the function.
  by value: NO VALUE READERS — the name is local to one function and nothing compares it.
- **S6** — The docstring of `tools/run-gates/derive-ceilings.py#cmd_check` names every tracked
  file the check reads, the pass-leg evidence of the budget arm included. Observed by AC10.
- **S7** — `tools/run-gates/README.md` and the header comment of `tools/run-gates/pass-legs.sh`
  say what S1 and S2 make true: the exclusion table holds `kit-subject`, and the runner's section
  says a pass leg reads the manifest beside its kit. The two comment lines that call the shim the
  held tier's alone, in `tools/run-gates/run-held-wsl.sh` and `tools/run-gates/held_halves.py`,
  name the pass-leg adapter as its second caller. Observed by AC11.

## 3. Non-goals (OUT)

- The `docs` leg's red, two undocumented policy keys. TOOL-aNimbleMend-11 documents them.
- The red of `writing practice (records and units)`. It names an unpinned figure in the acceptance
  ledger of unit 3, a record under `memory/`, and this unit's files are product files. The main
  loop repairs that record; the brief's items do not list it.
- Any change to what the three list-reading legs do under the full bar. There `GATE_LEGS` is unset
  already, and this unit gives a pass leg the same environment.
- A new knob on the bar runner. `tools/run-gates/run-gates.sh` is not edited (§4, "Alternatives
  rejected").
- A second shim. The adapter calls the one that exists.
- Handing a pass leg the caller's own `GATE_LEGS`. A leg under a pass-leg run reads the manifest
  beside its kit, whatever the caller exported (§4, "What it does not check").
- A fresh `--write` of `tools/run-gates/pass-leg-evidence.txt`. The red counts did not move; the
  rule did.
- The help page, which is TOOL-aNimbleMend-11's, and any kit version, which the lander's `mint`
  moves.
- Any edit to a CLOSED spec of this build. Each correction is stated here.

### Edges

- **consumes-from** external — the held tier's leg shim, the `--leg` mode of `run-held-wsl.sh`, and
  the constant naming it in `held_halves.py`, both landed by TOOL-aSparedSpawn-5. Without them
  there is no shim to call and S1 would write one.
- **consumes-from** external — the code of this build's CLOSED units 2, 3 and 5: the predicate,
  the budget gate and the pass-leg adapter this unit corrects.
- **hands-off** external — the unpinned figure in unit 3's acceptance ledger, which the main loop
  pins or lists, and the `docs` leg's two keys, which unit 11 of this build documents.

## 4. Design

### Evidence

Read at `b386848f`, the branch tip, where units 1 to 7 of this build are built. The run's record is
`gate-pass-legs.txt` in this worktree's git directory, and its red lines are in `gate-logs/` beside
it.

- **The adapter hands the runner a filtered file, and every leg inherits it.**
  `tools/run-gates/pass-legs.sh@320c81f30b81:322` sets `GATE_LEGS` to the filtered file for the
  runner's process, and `tools/run-gates/run-gates.sh@970e3e89a3e9:372` reads its list from that
  variable and never clears it, so each leg it starts sees the same value.
- **Three declared legs read that variable as their subject.**
  `tools/check-testsuite-counts.sh@d4bad437a217:32`, `tools/run-gates/derive-ceilings.py#read_legs`
  and `tools/run-gates/run-selftests.sh@25d3174e1eab:49` each take `GATE_LEGS` ahead of the manifest
  beside them. A fourth reader, `tools/run-gates/profile_bar.py@39b313f7cff9:338`, is no leg today.
- **Two of the three went red on the filtered list.** The testsuite-count leg printed one failure
  per waiver whose suite the filtered list does not run. The budget-row leg printed one failure per
  budget row whose leg the filtered list does not hold.
- **The third went red on the budget gate alone.** The ceiling check prints a row the manifest
  lacks as a report and does not fail on it, by its own comment in
  `tools/run-gates/derive-ceilings.py#cmd_check`. Its one failing line was
  `PASS-BUDGET FAILED — python resolver (behaviour + inline parity + idiom ban): the pass-leg runner would hold it`.
  Under the filtered list it also graded only the declared rows' ceilings, which is a narrower
  check than the bar's and was silent.
- **The rule selects a leg the runner holds.** `python tools/run-gates/pass_legs.py --report` at
  this tip prints `selected` for `python resolver (behaviour + inline parity + idiom ban)`, a row
  with `chunk` `wiring` and `subject` `kit`. The runner holds a row whose `subject` is `kit` or
  whose `chunk` is `selftests`, at `tools/run-gates/run-gates.sh@970e3e89a3e9:3259`. The predicate
  has a reason for the chunk and none for the subject. The run's record reads `held` 1 and
  `not-run` for that leg.
- **Every ranked leg is selected today.** The same report prints no `over-budget` line, so taking
  one leg out of the list lets no other in. The list was 30 legs at this tip (PINNED, 2026-11-12).
- **A shim that clears the variable exists.** `tools/run-gates/run-held-wsl.sh@3ff0069b601f:191`
  unsets `GATE_LEGS` and then runs the words after `--leg`, mapping a python launcher at the head
  to the resolved one. `tools/run-gates/held_halves.py@a994e1fce362:129` writes every partition row
  through it, from the constant at `tools/run-gates/held_halves.py@a994e1fce362:54`. Its comment
  states this unit's defect: the runner exports the variable to every leg, and a leg of a partition
  must not inherit the partition.
- **A runner knob owes the push boundary a class.**
  `memory/gotchas/a-runner-knob-owes-a-push-class.md` records it, and three lists scrub
  `GATE_LEGS` today: `.githooks/pre-push@2714fe14bf6e:1965`,
  `tools/unattended/unattended.sh@21fe403ca809:11343` and
  `tools/run-gates/post-merge.sh@a0462621d566:36`.
- **The selfcheck grades sentences.** `tools/govkit/govkit.py@37f075e4e93e:3506` refuses, in every
  tracked file under the home of a kit that declares `[[regenerate]]`, a sentence holding the word
  `update` and a re-render claim without `GOVKIT_RERENDER`. The key name `why_no_regenerate` is
  itself a claim by that pattern, and its value at `tools/run-gates/kit.toml@0e4a5ed195a7:150` ends
  `on apply and on update`. The same arm never asks for the reason once `[[regenerate]]` is
  declared, so the sentence is graded and the key is not required.
- **The lexicon names the offender.** `tools/run-gates/pass_legs.py@b503ecdc8f81:342` defines
  `strip`. `python tools/lexicon/lexicon.py --suggest strip --as py.function` answers `extract`,
  and `--suggest remove_pass_field --as py.function` answers `OK`, both on 2026-11-12.
- **The ceiling check reads four tracked files.** `cmd_check` reads the manifest, the ceiling
  evidence and the margin file, and its budget arm reads the pass-leg evidence through
  `tools/run-gates/pass_legs.py#read_pass_evidence`. Its docstring says two files and nothing else.

### The mechanism for S1, and why this one

The python call of `pass-legs.sh` that filters the manifest imports `held_halves` beside
`pass_legs` and writes each selected row as a copy whose `argv` is
`["bash", held_halves.SHIM, "--leg"]` followed by the row's own words. Nothing else of the row
moves, and nothing else of the adapter moves: the runner still gets the filtered file as
`GATE_LEGS`, so which legs start, the run's record and what the run costs the bar's records are
what TOOL-aNimbleMend-5 built.

Each leg then starts through the shim, with `GATE_LEGS` unset. A leg that reads the variable falls
back to the manifest beside its kit, which is the whole manifest and the environment the full bar
gives it. That is the brief's preferred direction: the whole manifest is every leg's subject, and
only the list the runner starts is narrow.

It closes the class and not the three instances. The fix sits where the variable is inherited, so
`profile_bar.py` and any reader written later are covered without an edit of their own.

An import that fails ends the adapter with exit 2 and nothing run, through the guard that call
already has. A shim file that is absent fails every leg loudly, each with the shell's exit 127.

### The mechanism for S2

`check_pass_eligible` gains one clause after the `selftest` clause:

```python
if leg.get("subject") == "kit":
    return "kit-subject"
```

`EXCLUSIONS` lists the reason second. The order matters twice. The two reasons the runner's hold
is made of sit together, and `kit-subject` is answered ahead of `no-red`, so a declared kit row
with no red row still reaches the budget gate's held finding.

`check_pass_budget` keeps its three excluded classes as they are. Its held clause tests
`reason == "kit-subject"` in place of the row's `subject`, and the `ponytail:` comment above that
clause goes, since the condition it waits for is now met. The sentence the finding prints is
unchanged, so the arm TOOL-aNimbleMend-3 left for its AC6 stays green.

The hold itself is stated twice, in the runner's shell and in this predicate. The pass-leg
adapter's `FINDING held` line is the live comparison of the two: a row the predicate lets through
and the runner holds prints it on the next run.

### The texts (S4, S6, S7)

S4. The value of `why_no_regenerate` becomes this, or a sentence of the same content:

```
the adopter writes nothing, so `update` re-runs no adopter here whatever GOVKIT_RERENDER reads; the [gate_runner] declaration its check joins against is emitted by govkit itself from [gate_runner_seed], on apply and on update
```

The key stays. Its reason is still true of the adopter, and the comment above the `[[regenerate]]`
row cites it. The sentence must not call a flag-off run silent, which the same arm refuses.

S6. The docstring of `cmd_check` says the gate reads tracked files and nothing else, and names
them: the manifest, `ceiling-evidence.txt` and `ceiling-margin.txt` for the ceiling arm, and
`pass-leg-evidence.txt` for the budget arm, where `pass_legs.py` is beside the script.

S7. In the README, the exclusion table of "The pass legs" gains the `kit-subject` row second, and
the budget table's held row says the predicate answers `kit-subject`. In "The pass-leg runner",
the opening paragraph says each row is copied with its `argv` behind the shim, and the bullet
saying a declared leg grades the filtered list is rewritten to say every leg starts with
`GATE_LEGS` unset. No sentence added under `tools/run-gates/` may hold `update` beside a re-render
claim without the flag's name, for the reason S4 exists.

### What it does not check

- A pass-leg run started with `GATE_LEGS` naming another manifest filters that manifest, and its
  legs grade the one beside the kit. No caller does this today outside a suite's fixture.
- A leg that finds the manifest by any means other than the variable is untouched.
- The runner's own reads still name the filtered file: the manifest blob in the run record, and
  the full-green stamp. Those are the costs TOOL-aNimbleMend-5 wrote down, unchanged.
- Each row's `argv` differs from the manifest's, so a ledger row a pass-leg run writes is keyed on
  the wrapped command. UNVERIFIED: whether any later bar reused such a row before this unit; the
  filtered manifest's blob already differed from the tracked one.
- Each leg costs one more shell start.
- The predicate and the runner state the hold separately. Nothing compares them before a run; the
  held finding compares them at each run.
- `GATE_BASE` is inherited as before.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the reason `kit-subject` | `EXCLUSIONS` in `pass_legs.py` | no cell grades a reason string; the spelling of the five beside it |
| `remove_pass_field` | nested in `render_pass_field` | `py.function`; `lexicon.py --suggest` answered OK on 2026-11-12 |

### Migration

Additive for an adopter. A manifest whose rule selected a kit-subject row loses that row's field at
the next `--apply`, which the `[[regenerate]]` row of the kit runs at every landing.

### Rollout

No switch. `pass.fast-legs` already gates the adapter, and the shim is inert for a leg that does
not read the variable.

### Files touched (estimate)

- `tools/run-gates/pass-legs.sh`
- `tools/run-gates/pass_legs.py`
- `tools/gate-legs.json`
- `tools/run-gates/kit.toml`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/run-held-wsl.sh`
- `tools/run-gates/held_halves.py`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

### Alternatives rejected

- **A runner knob naming the list to start, with `GATE_LEGS` left whole.** It is the same
  direction by a larger road. The knob narrows a bar, so it owes a class at the push boundary and
  a place in the three scrub lists the evidence names, and it edits the bar runner. The shim
  reaches the same environment for every leg with none of that.
- **A second variable the three scripts prefer.** It repairs the instances. `profile_bar.py` and
  the next reader inherit the filtered list again.
- **Leaving the three legs out of the declared list**, the brief's fallback. The budget gate would
  stop running on a pass, and the rule would carry one clause per reader, found one false red at a
  time.
- **A `--leg` mode of the adapter's own.** It would be a copy of the shim, the second of its kind.
- **The shim moved to a file of its own.** The constant in `held_halves.py` and the arm that pins
  its value would move for no change in behaviour.
- **Teaching the shim to restore the caller's `GATE_LEGS`.** It changes the held tier's contract
  for a case no caller has.
- **Taking the `why_no_regenerate` key out of the descriptor.** The selfcheck allows it, but the
  reason is still true and still read by whoever reviews the descriptor.
- **Moving the lexicon's pin.** The brief forbids it, and the offender has a declared verb.

## 5. Production-readiness checklist

- security — no new write path, knob or input. The shim runs words that come from the tracked
  manifest, as the runner does. No runner knob is added, so the push boundary's classes stand.
- perf / scale — one more shell start per pass leg. The declared list loses one leg's cost row.
- error / empty / loading states — a failed import ends the adapter with exit 2 and nothing run;
  an absent shim file fails every leg with exit 127; a list with no declared row starts no runner,
  as before.
- observability — the filtered file in the git directory shows each wrapped `argv`; `--report`
  prints the new reason beside its leg; the held finding stays as the runtime check of the rule.
- risks — the arms of TOOL-aNimbleMend-5 in `run-gates.test.sh` build a fixture kit of five files,
  and the adapter now needs three more beside it: the shim, `held_halves.py` and `profile_bar.py`,
  which that module imports. The builder widens that copy in the same change, or every arm of that
  section reds on the import.
- testing — AC3 to AC6, AC8, AC10 and AC11 are probes a pass runs. AC1, AC2, AC7 and AC9 are the
  main loop's. The two arms of §7 keep S1 and S2.
- migration — additive; see §4, "Migration".
- user docs — the kit README, S7. The help page is TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

`<gd>` is the git directory of the worktree the unit is built in.

- **AC1** — When `bash tools/run-gates/pass-legs.sh --base HEAD~1` runs at the unit's pass commit,
  the record `gate-pass-legs.txt` in `<gd>` reads `ok` on the `leg` line of each of
  `testsuite counts (every bar self-test prints one)`, `leg ceilings clear their evidenced maximum`
  and `every held leg is budgeted, every budget row resolves`, its `held` key reads 0, and the
  output holds no line opening `pass-legs: FINDING held`.
  Red when: the wrap is absent, which reads `fail` on the first and third, or the rule still
  selects the held leg, which reads `fail` on the second and `held` 1.
  permission: the main loop's; a role agent's hook refuses the pass-leg runner.
  cost: one pass-leg run, 209 s of wall at `bde79f210` (PINNED, 2026-11-12).
- **AC2** — When `python -c "import json,sys; r=json.load(open(sys.argv[1],encoding='utf-8')); print(len(r), sum(l['argv'][0]=='bash' and l['argv'][2]=='--leg' for l in r))" <gd>/gate-pass-legs.json`
  runs after AC1's run, it prints two equal numbers above zero.
  Red when: a row is copied whole, so the second number is 0.
  permission: the main loop's, since only a pass-leg run writes the file.
  figure: both numbers are DERIVED from the file.
- **AC3** — When `python -c "import sys; sys.path.insert(0,'tools/run-gates'); import pass_legs as p; print(p.check_pass_eligible({'name':'k','subject':'kit','chunk':'product','argv':['true']},{'k':(1,None)},{'k':1.0}), p.EXCLUSIONS[1])"`
  runs, it prints `kit-subject kit-subject`.
  Red when: the clause is absent, which prints an empty first field, or the reason is listed
  elsewhere than second.
- **AC4** — When `python -c "import sys; sys.path.insert(0,'tools/run-gates'); import pass_legs as p; print(p.check_pass_budget([{'name':'k','pass_leg':True,'subject':'kit','chunk':'product','argv':['true']}],{'k':1.0})[0])"`
  runs, it prints a list of one string that holds `would hold it`.
  Red when: the reason is answered after `no-red`, which gives a declared kit row with no red row
  no finding, or the held sentence went with the comparison it replaced.
- **AC5** — When `python tools/run-gates/pass_legs.py --report` runs, the line of
  `python resolver (behaviour + inline parity + idiom ban)` opens `kit-subject`; then
  `python tools/run-gates/pass_legs.py --check` exits 0, and
  `python tools/run-gates/pass_legs.py --budget` exits 0 with a last line opening `pass-budget:`
  that names the budget.
  Red when: `--apply` did not run, so `--check` names a field the rule does not give.
  figure: the declared count and its sum are DERIVED, printed by `--check` and `--budget`.
- **AC6** — When `grep -c 'GOVKIT_RERENDER' tools/run-gates/kit.toml` runs, it prints 1 or more.
  Red when: the sentence is unchanged. At base it prints 0.
- **AC7** — When `python tools/govkit/govkit.py selfcheck` runs, no line of its output names
  `tools/run-gates/kit.toml`.
  Red when: the new sentence holds `update` beside a re-render claim without the flag, or calls a
  flag-off run silent.
  permission: the main loop's; the command is a leg's own, which a role agent's hook refuses.
- **AC8** — When `grep -c 'def strip' tools/run-gates/pass_legs.py` runs it prints 0,
  `grep -c 'remove_pass_field' tools/run-gates/pass_legs.py` prints 2, and
  `git diff --stat HEAD -- .lexicon.conf` prints nothing before the pass commits.
  Red when: a call still spells the old name, or the pin moved to admit it.
  figure: 2 is PINNED at `b386848f`, the definition's line and the one line holding both calls.
- **AC9** — When `python tools/lexicon/lexicon.py` runs, it exits 0 and prints no line holding
  `over pin`.
  Red when: the new name leads with no declared verb, or another offender entered with this unit.
  permission: the main loop's; the command is a leg's own.
- **AC10** — When `grep -c 'TWO TRACKED FILES and nothing else' tools/run-gates/derive-ceilings.py`
  runs it prints 0, and `grep -c 'pass-leg-evidence.txt' tools/run-gates/derive-ceilings.py` prints
  1 or more.
  Red when: the docstring still counts two, or names the evidence nowhere. At base the second
  prints 0.
- **AC11** — When `grep -c 'filtered list and not the manifest' tools/run-gates/README.md` runs it
  prints 0, `grep -c 'kit-subject. |' tools/run-gates/README.md` prints 1 or more, and
  `grep -c 'pass-legs.sh' tools/run-gates/run-held-wsl.sh` prints 1 or more.
  Red when: the README still says a declared leg grades the filtered list, the exclusion table
  lacks the reason, or the shim's header still names one caller. At base they print 1, 0 and 0.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `leg ceilings clear their evidenced maximum` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `lexicon naming predicates` · `lexicon wiring` · `python reads (a name never bound, an import outside its guard)` · `harness arms (fail branches armed or pinned)` · `docs` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures`

The last three are owed by the manifest's guard, which S3's re-applied field trips. The first two hold the new arms and are in the held tier, so the close runs them only where it asks
for that tier. The brief's close is the full bar once, without the self-tests and without the
unattended kit gate leg, so the main loop observes each arm below RED and then GREEN by itself.
The `docs` leg stays red on its two keys until TOOL-aNimbleMend-11 lands, and the kit epoch leg
expects the lander's `mint`.

New arm: tools/run-gates/run-gates.test.sh · covers AC1 · section 14's fixture with a declared row whose script records whether `GATE_LEGS` is set when it starts, staged with the wrap taken out of the fixture's copy of the adapter · `FLOOR_ASSERTIONS`, raised by the assertions added

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC3 AC4 · fixture G of TOOL-aNimbleMend-3 with a planted pass-leg evidence file and a kit-subject row holding a red row and a cost row, which `--report` must read `kit-subject` and `--apply` must leave undeclared, staged with the clause taken out of the fixture's copy of the module · `FLOOR_ASSERTIONS`, raised by the assertions added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.

## 10. Reuse audit

The seam for S1 is the held tier's leg shim, the `--leg` mode of `tools/run-gates/run-held-wsl.sh`,
with the constant `SHIM` of `tools/run-gates/held_halves.py` naming it: a shim that already clears
`GATE_LEGS` for a leg of a narrowed manifest, for the reason this unit has. The seam for S2 is the
predicate `tools/run-gates/pass_legs.py#check_pass_eligible`, whose order of reasons the budget
gate already reads. `python tools/codebase-map/reuse_lookup.py "wrap each filtered gate leg argv
through a shim that unsets the leg manifest variable so a leg grades the whole manifest"` ranked
name-stem neighbours only, `load_manifest` in `tools/run-gates/held_halves.py` among them, and
named no shim; the shim was found by reading every reader of the variable under `tools/`. For a
runner knob that narrows the started legs, no existing seam fits, and the evidence is that the
runner reads one list for both its dispatch and its records. `gotchas.py --for-paths` over the
estimate selected `fixture-passes-by-finding-nothing`, which is why the first arm's row records
the variable's state and does not merely run. `a-runner-knob-owes-a-push-class`, found by reading
the push hook's scrub list, decided against the knob.

Where the brief and the source disagreed: the brief says the ceiling leg false-reds on evidence
rows naming legs the manifest lacks. Those lines are reports and fail nothing; the leg's one
failure was the budget gate's held finding, which S2 and S3 repair. S1 still matters to that leg,
because under the filtered list it graded the declared rows' ceilings alone.

Recall terms used: `python tools/memory-recall/query.py "a gate leg inherits the filtered leg
manifest from the pass-leg runner and grades it as its subject" --terms "pass leg GATE_LEGS
filtered manifest subject shim --leg partition held kit-subject runner knob push class"`
