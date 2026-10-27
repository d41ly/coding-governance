# TOOL-dSafePassage-68 — the upgrade-walk child's stand-ins take and pass on every parameter of the functions they rebind, held by an arm that reads the live signature

**Status:** CLOSED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 7 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-68-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-68-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-68-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-68-1-spec-writer.md) | research | — |
| [2026-10-27-prompt-TOOL-dSafePassage-68-2-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-68-2-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-68-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-68-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Every child walk the `upgrade-walk` leg spawns runs `update` to completion again. The child's
stand-in for `upgrade_steps.run_step_isolated` takes and passes on whatever the real function takes,
so a parameter added to the real one later cannot break the leg silently. A cheap selftest arm
reads the real signature live and reds when a stand-in stops passing its parameters on, instead of
the leg failing an hour in.

Every line cited below was read at the run branch's HEAD `6055cdf18`. TOOL-dSafePassage-26's
`to` parameter is not on the default branch yet, so the header's `base` is the run's merge base,
as on TOOL-dSafePassage-62 to -67.

## 2. Scope (IN)

- **S1** — Pass-through. In the child script `CHILD` (`tools/govkit/upgrade_walk.py:337-399`), the
  stand-in `run` (`:353`) becomes `def run(row, phase, target, gov_root, *args, **kwargs)`, and each
  of its three calls to `real_run` (`:359`, `:370`, `:386`) ends `*args, **kwargs`. The stand-in
  `read` (`:389`) becomes `def read(root, rev, landed_ref, *args, **kwargs)`, and its call to
  `real_read` (`:390`) ends the same way. The names the stand-ins read stay positional and keep the
  real functions' spelling. Observed by AC1 and AC3.
- **S2** — The predicate. `check_child_forwarding(us, child=CHILD) -> list[str]` in
  `tools/govkit/upgrade_walk.py`, beside `CHILD`. It parses `child` with `ast` and returns one
  problem per way a stand-in fails to take and pass on its real function's parameters (§4). An
  empty rebind, a stand-in it cannot find, or a stand-in that never calls its real binding is a
  problem too, never an empty pass. Observed by AC1 and AC2.
- **S3** — The arm. `tools/govkit/selftest.py` gains two `[dSP-68]` checks in `main`, at the head
  of the TOOL-dSafePassage-5 block that observes the leg without building release-0
  (`tools/govkit/selftest.py:18516-18530`). One asserts the predicate over the shipped `CHILD` is
  empty. The other feeds it two edits of the shipped `CHILD` and asserts each is named (§4). Both run
  in process, in milliseconds. Observed by AC1 and AC2, which the arm re-observes.

## 3. Non-goals (OUT)

- **The leg's report of a child that dies before its count line.** `check_walk_exit`
  (`tools/govkit/upgrade_walk.py:277-296`) answers `exit <rc>` and nothing else when the output
  carries no `govkit: N problem(s)` line, which is why the measured failure read `the walk to the tip
  did not return: exit 1`. Printing the child's last lines there would have named the `TypeError`.
  It is decided out of this unit: it is a second mechanism in a second function with its own
  contract, and BUILD-METHOD M2 puts one mechanism in one spec. It is handed off below, recommended
  as its own unit, because it would name every crash class the arm of S3 does not gate.
- A fail-fast call of `check_child_forwarding` from the leg's `main`. S3's arm already runs on every
  change under `tools/govkit/`, and §4 says why the leg gains nothing from a second caller.
- Any change to `run_step_isolated`, `read_steps`, `run_step_reread` or the `to` they carry. The real
  functions are the reference this unit reads.
- A declared step using `{to}`. None does today (`git grep "{to}"` over the kit descriptors finds
  none), so the forwarded `to` is held by the predicate, not by a walk.

### Edges

- **consumes-from** `TOOL-dSafePassage-5` — the leg, its child script `CHILD`, `run_child_walk`, and the selftest block observing the leg; without them there is no stand-in to fix and no arm to extend
- **consumes-from** `TOOL-dSafePassage-26` — `run_step_isolated`'s fifth parameter `to` and `run_step_reread`'s positional pass of it; without them the stand-in's four parameters would still fit
- **hands-off** external — the leg's report of a child walk that exits with no `govkit: N problem(s)` line: printing the child's last lines in `check_walk_exit`, recommended as its own unit

## 4. Design

### What was measured

PINNED 2026-10-27 on node `d`, by the brief's probe `probe_up40.py`, which wraps
`check_walk_exit` to print the child's tail and runs `upgrade_walk.main(["--case", "up"])`. The
child's `update` died in `run_step_walk`'s first witness, through `spawn`
(`tools/govkit/upgrade_steps.py:1376-1377`) and `run_step_reread`, whose call
`run_step_isolated(row, phase, target, gov_root, to)` (`:1298`) passes `to` positionally even when
it is `None`. The stand-in takes four, so it raised
`TypeError: run() takes 4 positional arguments but 5 were given`. TOOL-dSafePassage-26 added `to`
in `dfcef45a7` (`:1096`) and changed that call, and did not touch `upgrade_walk.py`. Every case walks
`up` first through `run_up_walk` (`tools/govkit/upgrade_walk.py:540-552`), which raised the `Stop`
`up · the walk to the tip did not return: exit 1`.

### Why pass-through, not an explicit `to`

The goal is that the next parameter cannot break the leg. An explicit `to` fixes this break and
leaves the stand-in one signature edit from the next one. Pass-through follows the real function by
construction. The stand-in names only the four parameters its branches read, and those keep the real
spelling, so a caller passing `target=` by keyword still binds. The forwarding matters on every call,
not only the last: a stand-in that took `to` and swallowed it would run a rollback's `down` with
`{to}` unanswered, which `resolve_step_argv` refuses before any spawn
(`tools/govkit/upgrade_steps.py:962-965`), on the leg alone. `read` gets the same form. Its signature matches today (`:378`), but it is the
second instance of the class, and the arm grades the class.

### The predicate

```
check_child_forwarding(us, child=CHILD) -> list[str]:
  tree   = ast.parse(child)
  stand  = {attr: name} from every top-level tuple assignment `us.<attr>, ... = <name>, ...`   # :396
  real   = {attr: name} from every top-level tuple assignment `<name>, ... = us.<attr>, ...`   # :348
  stand empty                                   -> "the child rebinds nothing on `us`"
  per attr in stand, sorted:
    fn = the top-level def named stand[attr]; rname = real.get(attr)
    fn or rname absent                          -> "<attr>: no stand-in def or real binding found"
    names = list(inspect.signature(getattr(us, attr)).parameters)
    own   = fn's positional parameter names
    own is not names[:len(own)], or fn lacks *args or **kwargs
                                                -> "<attr>: stand-in <name>(<own>) does not take and pass on (<names>)"
    calls = every ast.Call in fn whose func is the Name rname
    no call                                     -> "<attr>: <name> never calls <rname>"
    per call: len(own) positional args, then Starred(fn's *args name), and a `**` keyword of fn's **kwargs name
      else                                      -> "<attr>: CHILD line <n> calls <rname> without passing on *<a>, **<k>"
```

A candidate of this predicate was run over the real `CHILD` at HEAD before this spec was written. It
named both stand-ins' signatures and all four calls, three to `real_run` and one to `real_read`. With
S1's form applied to a copy it returned `[]`, and with one of the three `real_run` calls put back to
four arguments it named that call alone. The population is 2 stand-ins and 4 calls, PINNED at
HEAD `6055cdf18`.

**What it does not check.** It reads the shape of the forwarding, not what a stand-in's branches do
with the values. It reads the working tree's `upgrade_steps`, while the child imports the clone's
copy at the tip. The tip is HEAD's commit plus the `[[gov_plant]]` commits, which edit only
`tools/hooks/kit.toml` and `tools/hooks/README.md` (`tools/govkit/fixtures/release-0/plants.toml`),
so the two are the same file. It does not see a real function the child calls through any name
other than the one bound at `:348`.

### The arm

```
in selftest main, at the head of the TOOL-dSafePassage-5 block (:18516):
  import upgrade_walk as _uw; _us = govkit_module().upgrade_steps
  check("[dSP-68] the upgrade-walk child's stand-ins take and pass on every parameter of what they rebind",
        _uw.check_child_forwarding(_us) == [], detail = the problems joined)
  _a = _uw.CHILD with the stand-in `run`'s def put back to `(row, phase, target, gov_root)`
  _b = _uw.CHILD with the kill branch's `real_run(row, phase, shadow, gov_root, ...)` call put back to four arguments
  check("[dSP-68] the predicate names a stand-in that cannot take `to`, and a call that stops passing on",
        _a != _uw.CHILD and _b != _uw.CHILD
        and any("run_step_isolated" in p and "to" in p for p in _uw.check_child_forwarding(_us, _a))
        and _uw.check_child_forwarding(_us, _b) == [one problem naming run_step_isolated and the kill call's CHILD line],
        detail = both outputs)
```

Both edits are made to the shipped `CHILD` itself, the subject, so the liveness half cannot pass on
a simplified stand-in. The `!=` guards keep an edit that no longer matches from reading as a pass.
`HERE` is on `sys.path` already (`tools/govkit/selftest.py:679`), so the import needs nothing new.

### Inventory

Minted: the function `check_child_forwarding` in `tools/govkit/upgrade_walk.py` (the lexicon's
`--suggest` answers OK for cell `py.function`), and two `[dSP-68]` check labels. No flag, conf key,
gate leg, receipt field or policy key.

### Migration

None. `CHILD` is built into each child process at spawn.

### Rollout

Live at landing, at order 7.

### Files touched (estimate)

- `tools/govkit/upgrade_walk.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **An explicit `to` parameter.** It fixes today's break only (above).
- **Calling the stand-in with the real function's full parameter list.** The stand-in exists only
  inside the child's script, after it has imported the clone and before it runs `govkit.py` as
  `main`. Calling it needs that setup stubbed, and its `kill` branch copies trees and calls
  `os._exit`, so a call reaches the pass-through branch and the witness branch and not the kill
  branch's call. The predicate reads all four calls.
- **A fail-fast check in the leg's `main`.** With pass-through in place, a new parameter on the real
  function no longer breaks the child. What is left is an edit to `CHILD` that stops forwarding, and
  that edit is under `tools/govkit/`, which every `govkit selftest` run covers.

## 5. Production-readiness checklist

- security: N/A — no write path, input or surface; the predicate parses a string constant of its own
  module.
- perf / scale: one `ast.parse` of a 60-line string per selftest run.
- error / empty / loading states: an empty rebind, a missing stand-in or a stand-in with no call to
  its real binding is a named problem, never an empty pass.
- observability: each problem names the rebound attribute and, for a call, its line in `CHILD`.
- risks: an arm that pins the edit strings goes silent when `CHILD` is reworded; the `!=` guards
  turn that into a red.
- testing: S3's two checks, and `--case up` for the walk itself (AC3).
- migration: none.
- user docs: N/A — the leg's internals; `help/upgrade-steps.md` describes the child's rebinding and
  that description does not move.

## 6. Acceptance criteria

- **AC1** — When `python -I -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as uw; print(uw.check_child_forwarding(uw.load_engine()[0]))"`
  runs, it prints `[]`.
  Red when: either stand-in in `CHILD` lacks `*args, **kwargs`, or any of the four calls to
  `real_run` and `real_read` stops passing them on, as at HEAD `6055cdf18`, where it names 2
  signatures and 4 calls.
  figure: 2 stand-ins and 4 calls, PINNED at HEAD `6055cdf18`.
- **AC2** — When the same probe is fed `uw.CHILD` with `run`'s def put back to
  `def run(row, phase, target, gov_root):`, its output names `run_step_isolated` and the real
  parameter `to`. When it is fed `uw.CHILD` with the kill branch's call put back to
  `real_run(row, phase, shadow, gov_root)`, it prints exactly one problem, naming that call's line.
  Red when: the predicate compares against a typed parameter list rather than
  `inspect.signature(us.run_step_isolated)`, or reads only the first call to `real_run`.
- **AC3** — When `python -I tools/govkit/upgrade_walk.py --case up` runs, its output carries no
  `TypeError` line and no `nothing measured: up · the walk to the tip did not return` line, and it
  prints its `upgrade-walk: summary ·` line.
  Red when: the stand-in `run` is back at four parameters, and the child dies at the first witness.
  cost: about a minute, PINNED 2026-10-27 by `probe_up40.py`'s run of the same case on node `d`.
  fixture: release-0, built by the leg from `tools/govkit/fixtures/release-0/pin.txt`; nothing to
  prepare.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · two `[dSP-68]` checks at the head of the TOOL-dSafePassage-5 block, their failing case staged by a working copy whose `CHILD` keeps HEAD's four-parameter `run` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from the main loop's kill probe after TOOL-dSafePassage-40,
  which found every `upgrade-walk` case dying at the first witness on TOOL-dSafePassage-26's `to`,
  by `2026-10-27-prompt-TOOL-dSafePassage-68-2-spec-writer.md`.

## 10. Reuse audit

The seam extended is the leg's child script `CHILD` in `tools/govkit/upgrade_walk.py:337-399`,
whose stand-ins `run` and `read` take the pass-through form, with the predicate written beside it.
The arm extends the TOOL-dSafePassage-5 block of `tools/govkit/selftest.py:18516-18530`, the leg's
observations that build no release-0 tree. `python tools/codebase-map/reuse_lookup.py "a test
stand-in that replaces a module function must accept and forward every parameter of the real
function"` ranked `load_stand_in_waivers` and `scan_stand_in_declarations`
(`tools/roles/roles_lib.py`), which are about role stand-ins and not call signatures, and found no
signature-parity helper in the tree. The recall probe found TOOL-dSafePassage-5's S5 and F6, which
chose the child's rebinding and bind any sibling that imports either rebound name, and
TOOL-dRedressedBar-19's AC19, which reads `inspect.signature` the same way in another kit.

Recall terms used: `python tools/memory-recall/query.py "a monkeypatched stand-in drifts from the real function's signature and breaks the walk" --terms "stand-in rebinds run_step_isolated CHILD signature inspect.signature monkeypatch upgrade-walk child walk TypeError positional forward parameter drift"`
