# TOOL-aLevelledCopy-9 — receipt fixtures are hermetic, a renamed row keeps its bit, the records agree

**Status:** CLOSED · rev-3 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 3 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aLevelledCopy-9-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aLevelledCopy-9-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md) | journal | TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review of this build confirmed five minor findings outside the ssh arm, and the build
method promotes every one. Two are product defects: the receipt-sync leg's git fixtures read the
host's gitattributes and object format, so a host with a global `text=auto` rule or a SHA-256 default
reds the leg on every run (M2, finding ids 4 and 12); and `govkit update` drops an adopter's exec bit
on an engine row gov renames, which `DEPL-aLevelledCopy-1`'s never-down rule forbids (M6, id 8). One
is a coverage gap: the no-`.git` guard in `resolve_clean_oids` has no arm (L3, id 15). Two are records
out of step: the README roster's hand-kept Status column (L4, id 18), already dropped by the main loop
and owed a left-shift, and spec 3's AC6 naming a filesystem its run did not use (L5, id 19). This unit
closes all five, in one batch, because their write set is disjoint from the ssh arm's.

## 2. Scope (IN)

- **S1 — the git fixtures pin what they read (M2).** In `tools/run-gates/check-receipt.py`,
  `check_git_arms`:
  1. each fixture's `[core]` block gains `attributesFile = <that fixture>/.git/no-such-attributes`,
     a path that does not exist, which replaces both a host `core.attributesFile` and the XDG
     default;
  2. its whole body, the fixture build and the graded `hash-object --stdin-paths` spawns, runs inside
     an environment window that sets `GIT_ATTR_NOSYSTEM=1`, `GIT_CONFIG_NOSYSTEM=1` and
     `GIT_DEFAULT_HASH=sha1` (§8 F1), restored in a `finally` so `main`'s grade of the real tree never
     sees it;
  3. the docstring states exactly what is pinned and what is not.

  Observed by AC1, AC2.
- **S2 — the class guard is the fixtures' own environment (M2's left-shift).** The same window points
  `HOME`, `XDG_CONFIG_HOME` and `GIT_CONFIG_GLOBAL` at a scratch directory, written by a new
  `seed_hostile_env`, whose `git/attributes` under both homes holds `* text=auto eol=lf` and whose
  global config sets `init.defaultObjectFormat = sha256`. So every run of the leg runs its four git
  arms against hostile ambient state, and a pin that regresses reds on every host rather than on the
  rare one (§8 F2). A LIVENESS arm proves the hostile state is live: an unpinned probe repository in
  the window, built with `GIT_DEFAULT_HASH` unset for that one spawn, reports `eol: lf` from `git
  check-attr eol`, and reports `sha256` from `git rev-parse --show-object-format`; a git that cannot
  report an object format prints an announced skip for that half instead of a pass. This is the
  fixture-inherits-ambient-machine-state class (C14). Observed by AC1, AC2.
- **S3 — the no-`.git` guard has an arm (L3).** A built-in arm in `check_fixtures` writes a tree with
  NO `.git` and one engine row whose bytes are CRLF while its `sha256` and `oid` are the LF bytes'. It
  asserts one graded row, eol-only 0, exactly one `DRIFTED` finding and exactly one finding opening
  `GIT       hash-object --stdin-paths not consulted`. It spawns nothing. Observed by AC3.
- **S4 — a renamed engine row resolves its mode from its OLD index entry (M6).** In
  `tools/govkit/govkit.py`, `land_through_index` gains a keyword parameter `entry_path`, default the
  row's own path, naming the index key the mode is resolved from. The renamed arm of `update` passes
  the path it moved FROM, because `index0` was read before `git mv` and holds no entry at the new
  path. The other two callers are unchanged. The docstring's MODE paragraph names the parameter and
  why. Observed by AC4.
- **S5 — never-down is gated per touching verdict (M6's left-shift).** `tools/govkit/selftest.py`
  gains a module-level `check_mode_never_down(tmp)` that `main` calls. It runs `measure_mode_carry`
  over this tree's `govkit.py` with a new arm key, `ND`, whose fixture is a third scratch gov beside
  `cm` and `rb`. In it the adopter makes four engine rows 100755 that gov ships 100644, and gov's next
  commit gives each a different verdict that lands through `land_through_index`: `renamed` (gov moves
  the source), `diverged` merged cleanly (the adopter edits one line and gov another), `missing` (the
  adopter's deletion is committed) and `stale`. One `update --write` must leave the three rows that
  carry an index entry at 100755 with gov's new bytes, the renamed row at its new path, and land the
  `missing` row at gov's 100644. That row is the control, not a fourth never-down case: the
  classifier reads `missing` only where the index holds NO entry, and a worktree-only deletion with
  the entry kept is dirty and refused before any verdict, so a `missing` row has no adopter bit to
  keep and takes the rule's no-entry half. Observed by AC4, AC5.
- **S6 — the hand-kept status column is a recorded class (L4).** A new section, the roster form, is
  appended to `memory/gotchas/two-answers-to-one-question.md`: the authored `roster:units` table of
  this build's README carried a Status column that read OPEN while the generated units table beside it
  read CLOSED rev-2, and 31 of the 144 authored rosters in the tree carry one. The record names the
  check (write no status into an authored roster; the generated `build-units` region is the status),
  and why it is not gated (§8 F3). The index is re-rendered with `gotchas.py --write`. Observed by AC6.
- **S7 — spec 3's AC6 names the filesystem its run used (L5).** `TOOL-aLevelledCopy-3`'s spec takes a
  rev-3: AC6's `fixture:` line names WSL's own `/tmp`, which `df -T` reported as tmpfs and which
  honours the exec bit, in place of `WSL ext4`; the header moves to rev-3 with the date; §9 gains a
  rev-3 line naming §6 and AC6. Status stays CLOSED (§8 F4). Observed by AC7.

## 3. Non-goals (OUT)

- **The receipt's own portability.** A receipt written on a CRLF box and graded on an LF clone still
  reds; that is `TOOL-aLevelledCopy-1`'s stated non-goal and unchanged.
- **Production `hash-object` environment.** `resolve_clean_oids` keeps the target's system
  gitattributes when it grades a real tree, because a target's commit would apply them too. Only the
  fixture window cuts them off.
- **Other ambient state the fixtures do not read today.** The git version, the filesystem's CRLF and
  exec-bit semantics, and inherited `GIT_DIR`-family variables (the closing review refuted that hazard
  as handled at the hook boundary, id 2) are named in the docstring as not pinned.
- **A hygiene refusal of a Status column.** §8 F3 measures why; the memory-tree kit is not touched.
- **`govkit apply`'s mode on a new row.** That is the open deployer ask in this build's `BACKLOG.md`.
- **The ssh arm.** `TOOL-aLevelledCopy-7` and `TOOL-aLevelledCopy-8` hold `tools/check-wiring.sh`.

### Edges

none

## 4. Design

### The fixture window (S1, S2)

```python
saved = {k: os.environ.get(k) for k in WINDOW_KEYS}
try:
    os.environ.update(seed_hostile_env(base) | {"GIT_ATTR_NOSYSTEM": "1",
                      "GIT_CONFIG_NOSYSTEM": "1", "GIT_DEFAULT_HASH": "sha1"})
    ...  # the liveness probe, the four fixtures, the four grades
finally:
    for k, v in saved.items():  # restore exactly, deleting what was absent
        ...
```

The window is set in `os.environ` rather than passed as `env=` because the graded spawn is
`resolve_clean_oids`, production code that takes no environment, and the fixtures must grade through
it unchanged. `check-receipt.py` is single-threaded, and `check_fixtures` returns before `main` grades
a real tree. The existing idiom this follows is the suites' `GIT_CONFIG_GLOBAL` plus
`GIT_CONFIG_NOSYSTEM` pair, which `tools/check-wiring.test.sh` and the unattended suites already use;
pointing `GIT_CONFIG_GLOBAL` at a HOSTILE file rather than `/dev/null` is what turns the pin into a
guard.

**Probe, run 2026-10-09 on node a, git 2.54.0.windows.1**, in scratch repositories under `%TEMP%`
with `HOME`, `XDG_CONFIG_HOME` and `GIT_CONFIG_GLOBAL` at hostile files: an unpinned `git init`
reported `sha256`; `GIT_DEFAULT_HASH=sha1 git init` reported `sha1`; `git init --object-format=sha1`
reported `sha1`, and still did with `GIT_DEFAULT_HASH=sha256` exported; `git check-attr text eol`
reported `auto` and `lf` until the local `core.attributesFile` named a missing file, then
`unspecified` for both. The unpinned reads are the negatives that show the probe could fail. The
system gitattributes half cannot be observed red on node a, whose system file holds only
`diff=astextplain` rules (the closing review read it); S1 pins it, and the docstring says it is pinned
and not observed.

### The renamed arm (S4)

At the renamed call, `index0.get(new_dest)` is None, so `resolve_landed_mode(None, gov)` returns
gov's mode and a 100755 adopter row lands at gov's 100644. The S3 mode-carry block already resolves
this row correctly from the old entry, so the line it prints and the mode that lands disagree today.
Passing `entry_path=old_path` makes both read the same entry: one rule, one input. The acted entry's
`mode_to` was the other candidate (§4 Alternatives rejected).

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `seed_hostile_env` | function in `check-receipt.py` | `py.function` |
| `check_mode_never_down` | function in `selftest.py` | `py.function` |
| `entry_path` | keyword parameter of `land_through_index` | none: parameters are not a declared surface |
| `ND` | arm key of `measure_mode_carry` | none |

`python tools/lexicon/lexicon.py --suggest seed_hostile_env --as py.function` and `--suggest
check_mode_never_down --as py.function` both answered OK on 2026-10-09.

### Files touched (estimate)

- `tools/run-gates/check-receipt.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/gotchas/two-answers-to-one-question.md`
- `memory/gotchas/INDEX.md` — re-rendered by `gotchas.py --write`.
- `memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md` — rev-3, S7.
- `memory/map/generated/symbols.json` — regenerated with `gen_map.py --write`, because two new
  functions stale it.
- This build's acceptance ledger under `memory/builds/aLevelledCopy/build/`.

The gotcha record widens the brief's write set by two files under `memory/gotchas/`. Neither sibling
in this order group writes there: `TOOL-aLevelledCopy-7` writes the wiring checker and its
suite. `TOOL-aLevelledCopy-8` sits at `order 4`, so even a `tools/govkit/govkit.py` write its M5 pick
might need is sequenced after this unit rather than concurrent with it.

### Rollout

The run-gates and govkit kits ship with a normal `govkit update`; the one kit-version bump per touched
kit happens once, after the last unit of this build. An adopter on a hostile host stops seeing a false
receipt-sync red on its first update.

### Alternatives rejected

- **A second, separate run of `check_git_arms` under the hostile environment.** Rejected by §8 F2: it
  doubles the leg's spawns, about 8 s a run on node a, to prove what one hostile run proves.
- **`git init --object-format=sha1` as the object-format pin.** Rejected by §8 F1: `git init` older
  than 2.29 refuses the flag, so every arm would fail on such a host, while the environment pin is
  ignored there and wins over the config key everywhere else.
- **The acted entry's `mode_to` at the renamed call.** Rejected: it is set only when the mode
  changes, so the call would still need the old entry for every other renamed row.
- **Passing `env=` through `resolve_clean_oids`.** Rejected: it adds a fixture-only parameter to
  production code for something a scoped window does without one.

## 5. Production-readiness checklist

- security — no new write surface. S4 narrows what `update` writes: a renamed engine row keeps an
  adopter's bit instead of taking gov's lower mode.
- perf / scale — S2 adds three spawns per receipt-sync run, about 2.3 s on node a at 0.75 s a spawn
  (PINNED, measured 2026-10-02); S3 spawns nothing; S5 adds one scratch gov to the govkit suite, about
  60 s, PINNED by analogy to `check_mode_carry`'s 137 s for eight verbs.
- error / empty / loading states — a git without sha256 announces its liveness skip; a git that cannot
  start fails every git arm with the cause named, as today.
- observability — the liveness arm prints its own `ARM` line, so a run where the hostile state did not
  apply is visible as a failure, not a pass.
- risks — the window mutates `os.environ`; an exception inside it is caught by the existing handler,
  and the `finally` restores the values in every case.
- testing — S2, S3 and S5's arms, each failing case observed per §6.
- migration — none. No receipt field and no index entry outside a renamed engine row changes.
- user docs — the `check-receipt.py` docstring (S1) and the `land_through_index` docstring (S4); the
  gotcha record (S6).

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/check-receipt.py --selftest` runs, it prints an `ARM ok`
  line for the liveness arm and for each of the four git arms, and exits 0. Red when: the liveness
  arm fails, which means the hostile state never reached the fixtures and the four arms proved
  nothing about it.
  figure: the four arms and one liveness arm are counted from the `fixtures:` line at observation
  time, not pinned here.
- **AC2** — When a scratch copy of `check-receipt.py` has the three S1 pins removed, keeping the
  hostile environment of S2, and `python <scratch copy> --selftest` runs, at least arm (c) and arm (a)
  print `ARM FAIL` and the copy exits 1. Red when: the copy still exits 0, which means the hostile
  environment cannot see an unpinned fixture.
- **AC3** — When `python tools/run-gates/check-receipt.py --selftest` runs, the no-`.git` arm prints
  `ARM ok`; and when a scratch copy with the `.git` guard of `resolve_clean_oids` deleted runs with
  `--selftest`, that arm prints `ARM FAIL`. Red when: the arm passes against the deleted guard.
- **AC4** — When the `ND` fixture runs alone, through
  `python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_mode_never_down(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`,
  it prints an empty list, and `git ls-files -s` in the fixture target reports 100755 for the renamed
  row at its new path. Red when: the renamed row lands 100644, which is the behaviour of the
  `govkit.py` read with `git show` at this unit's pre-build commit and handed to `measure_mode_carry`
  as its `source`.
  cost: about 60 s on node a, run under the default `%TEMP%` because a scratchpad temp root false-reds
  on path length; the whole suite is not run in this pass.
- **AC5** — When the same `ND` run executes, its read-only `update` prints the verdicts `renamed`,
  `diverged`, `missing` and `stale` once each for the four rows, the `renamed`, `diverged` and
  `stale` rows read 100755 after `--write`, and the `missing` row reads 100644; when the scratch
  gov's `govkit.py` copy has `resolve_landed_mode` changed to return gov's mode for every existing
  entry, the three entry-bearing arms fail and the `missing` arm still passes. Red when: a row takes
  a verdict other than its intended one, so its arm passes without the path it names being
  exercised.
- **AC6** — When `python tools/memory-tree/gotchas.py --check` runs after `--write`, it exits 0;
  `grep -n roster memory/gotchas/two-answers-to-one-question.md` hits the new section; and
  `python tools/memory-tree/gotchas.py --for-paths memory/builds/aLevelledCopy/README.md` lists
  `two-answers-to-one-question`. Red when: the record is not selected for a build README, which is the
  file the class bites.
- **AC7** — When `grep -n ext4 memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md`
  runs, its only hit is the rev-3 line of §9; the AC6 bullet names `tmpfs`; and the header reads
  `CLOSED · rev-3`. Red when: AC6 still names ext4, or the header rev has no §9 line.

## 7. Gates

`receipt sync (installed files match the receipt)` · `run-gates adopter e2e` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The close runs these once, in the bar. `tools/govkit/` trips the four govkit legs and the recall arms
leg, and `memory/` trips the two recall legs, as `check-spec-tokens.py --legs-for` prints; the rest
are named by judgment from `TOOL-aLevelledCopy-1` and `DEPL-aLevelledCopy-1`'s sets.

New arm: tools/run-gates/check-receipt.py · covers AC1 AC2 · the three S1 pins removed in a scratch copy · none
New arm: tools/run-gates/check-receipt.py · covers AC3 · the .git guard deleted in a scratch copy · none
New arm: tools/govkit/selftest.py · covers AC4 AC5 · the pre-build govkit.py, then a mirrored mode rule, handed to measure_mode_carry as its source · none

## 8. Open questions

- **FACT-QUESTION · F1 — which object-format pin?** Options: (a) `git init --object-format=sha1`, the
  brief's spelling; (b) `GIT_DEFAULT_HASH=sha1` in the fixture window. The probe is the §4 run of
  2026-10-09: with `init.defaultObjectFormat=sha256` in the global file, both pins produced `sha1`
  and the unpinned init produced `sha256`, which is the liveness negative. Both therefore satisfy
  AC1. They differ on a git older than 2.29, where (a) is an unknown option and fails every arm while
  (b) is ignored by a git that has only SHA-1. RESOLVED (agent, 2026-10-09, delegated): (b), the
  option with no failure mode the observation left open.
- **F2 — a separate hostile run, or a hostile environment for the one run?** Options: (a) keep the
  arms as they are and add a second run of `check_git_arms` under the hostile environment; (b) run the
  arms once, always under it. Both satisfy every criterion. (a) also shows the arms pass under the
  host's real global config, which (b) replaces; but with S1's pins that config cannot reach a
  fixture, so the extra run proves nothing (b) does not, at about 8 s more per leg run. Neither trips
  an M3 veto. RESOLVED (agent, 2026-10-09, delegated): (b), tie-broken on cost with the same criteria
  met and the class guarded on every run.
- **F3 — a hygiene refusal of a Status column, or a gotcha record?** Options: (a) refuse a Status
  column in an authored `roster:units` table, in `tools/memory-tree/gen_build_index.py`; (b) record
  the class in `memory/gotchas/`. The probe, run 2026-10-09: an awk walk of every
  `memory/builds/*/README.md` printed 31 authored roster header rows carrying `Status` out of 144
  rosters, so the probe can find positives. (a) would red 31 landed READMEs or need a new cutoff key,
  a memory-tree kit change and its version bump, which is a carrier change outside this unit's tier
  (M3 veto 2). RESOLVED (agent, 2026-10-09, delegated): (b), appended to the existing
  `two-answers-to-one-question` class, which is universal so every diff selects it and which needs no
  new map key, rather than a new record.
- **F4 — rev-3 on spec 3, or an AMENDED line in this unit's ledger?** Options: (a) a rev-3 bump of
  `TOOL-aLevelledCopy-3`'s spec with its §9 line; (b) leave spec 3 and record the correction in this
  unit's acceptance ledger as an AMENDED form against it. The probe read `build_commit` in
  `tools/unattended/lib-unattended.sh`, the predicate the pass-order and brief-recorded legs share: it
  walks oldest first and takes the first commit whose subject or `Pass:` trailer names the unit AND
  that touches a path outside the build folder, the generated indexes and the shared records. A
  spec-only commit touches only the build folder, so it can never become TOOL-3's build commit, and
  that build commit (788a74b79) is earlier than anything this unit writes. (a) puts the true fact in
  the one place a reader of spec 3 looks; (b) leaves the spec stating a filesystem the run did not use.
  Neither trips a veto. RESOLVED (agent, 2026-10-09, delegated): (a), with no subject naming the
  TOOL-3 id.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the closing review's M2, L3, M6, L4 and L5 and the
  promotion brief.
- rev-2 · 2026-10-09 · §4 Files touched: the sibling's write is named in prose rather than as a
  backticked path, because the spec-token guards join read it as this unit's own write and owed two
  legs this unit does not move. No design change.
- rev-3 · 2026-10-09 · §2 S5 and §6 AC5: the `missing` row is a control landing at gov's 100644,
  not a fourth 100755 row. Read at build time: `classify_row` takes `o_state` from the index, so
  `missing` means no index entry, and `dirty_claimed_paths` refuses the worktree-only deletion rev-2
  described before any verdict; `resolve_landed_mode(None, gov)` is gov's mode by the unchanged rule.

## 10. Reuse audit

Five seams, each extended rather than duplicated: `check_git_arms` and `check_fixtures` in
`tools/run-gates/check-receipt.py` for S1 to S3; `land_through_index` and `resolve_landed_mode` in
`tools/govkit/govkit.py` for S4; `measure_mode_carry` in `tools/govkit/selftest.py`, whose nested
`build_gov`, `build_target` and `read_entry` the `ND` fixture reuses by being one more arm key, for S5;
the `two-answers-to-one-question` gotcha for S6; and the suites' `GIT_CONFIG_GLOBAL` plus
`GIT_CONFIG_NOSYSTEM` idiom, which the fixture-inherits-ambient-machine-state record names, for the
window. `python tools/codebase-map/reuse_lookup.py "isolate a git fixture from the host's global
config and attributes"` ranked generic `git` and `fixture` stems and no hermetic-fixture helper, and
`python tools/codebase-map/reuse_lookup.py "keep an adopter's executable mode when a renamed row lands
through the index"` ranked no mode seam beyond the two functions S4 names, which the recall probe
returned through `DEPL-aLevelledCopy-1`'s spec.

Recall terms used: fixture hermetic ambient GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM attributesFile autocrlf object-format sha256 check-receipt C14 · renamed land_through_index resolve_landed_mode mode_to index0 never-down engine exec bit govkit update git mv
