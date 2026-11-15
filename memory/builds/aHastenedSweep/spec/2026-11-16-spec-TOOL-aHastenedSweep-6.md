# TOOL-aHastenedSweep-6 — every arm this build added can go red on its regression, and every comment and map line describes the one-process launch

**Status:** INPROGRESS · rev-2 · 2026-11-16 · node a · Tier-1 · base f25308f0 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md](../prompts/2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md) | research | TOOL-aHastenedSweep-5 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 confirmed four MEDIUM and four LOW items on this build's arms, comments
and dossier (`memory/builds/aHastenedSweep/reviews/2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md`,
M1 to M4 and L1 to L4). This unit closes all eight as one batch: the assertion floor counts every arm
the build added, each side of the one-process split and its fallback has an arm that reds on the
regression the review names, the with-ids selftest reaches the stderr and crash paths of the frame,
and every comment and map line names the launch the engine actually makes. No verdict moves.

## 2. Scope (IN)

- **S1** — M1. `FLOOR_ASSERTIONS` in `tools/memory-tree/check-memory-hygiene.test.sh` moves from 710
  to 719: unit 3's five assertions, which its commit never counted, plus the four this unit adds in
  S2 and S3. A `# RAISED 710 -> 719` comment, in the shape of the entries above it, names
  `TOOL-aHastenedSweep-3`, `TOOL-aHastenedSweep-4` and `TOOL-aHastenedSweep-6` and what each counts.
  Observed by AC5.
- **S2** — M2. Two one-red `--offenders` arms after unit 4's block in the hygiene suite, one
  assertion each. The bug-class-only arm reds only the gotchas verb and asserts the `check 17-19`
  key of its check 18 line is present and no `check 13-16` row is. The id-classifier-only arm reds
  only the corpus_ids verb and asserts the `check 13-16` key of its check 14 line is present and no
  `check 17-19` row is. Observed by AC1.
- **S3** — M3. One arm in the hygiene suite, a two-pass loop with one assertion per pass, drives the
  frame-failure fallback through a `GOV_PYTHON` wrapper. The wrapper answers an argument list holding
  `--check-with-ids` with one unframed line and exit 0 on the first pass, exit 2 on the second, logs
  every other argument list, and passes it to the real interpreter. Each pass asserts a non-zero
  exit, the wrapper's line keyed `check 13-16`, and no standalone `gotchas.py --check` in the log.
  Observed by AC2.
- **S4** — M4. The `gotchas.py --selftest` with-ids arms gain one whose loaded `corpus_ids` has a
  `main` writing one stderr line and one stdout line and returning 3. It asserts the first frame is
  exactly the stderr line, then the stdout line, then `\x1d3\n`, and the second frame equals the
  standalone gotchas `--check` frame. Observed by AC3.
- **S5** — L2. A second new selftest arm whose loaded `corpus_ids` has a `main` that raises
  `RuntimeError` inside the per-verb loop. It asserts the first frame opens with `Traceback`, holds
  `in cmd_check_with_ids` and the raised message, holds no `in <module>` line and ends `\x1d1\n`, and
  the second frame equals the standalone gotchas `--check` frame. Observed by AC4.
- **S6** — L1. The docstring of `gotchas.py#cmd_check_with_ids` and the comment on its
  `except Exception:` line say the crash frame holds the in-process traceback, which starts at the
  `cmd_check_with_ids` frame, is written in this process's stream encoding, and sits ahead of all of
  the verb's stdout. Observed by AC4, which shows the claim true, and AC6, which shows the text.
- **S7** — L3. Three texts name the stdin hand-down on both launches. The suite's exemption note for
  `GOV_INDEX_SET_STDIN` names `corpus_ids.py --check` and, on an unscoped run, `gotchas.py
  --check-with-ids`. The `corpus_ids.py` module docstring and the hygiene shell's comment above the
  id-classifier block each say the shell hands `--print-index-set`'s answer down on stdin under
  `GOV_INDEX_SET_STDIN=1` when its checks 1 to 5 ran clean. Observed by AC6.
- **S8** — L4. The `--print-index-set` bullet of `memory/map/features/memory-tree-hygiene.md` places
  the hand-down on the unscoped run's single `gotchas.py --check-with-ids` launch, which runs
  corpus_ids' `--check` in-process, and says a scoped run's `corpus_ids.py --check` always asks the
  print mode. Observed by AC6.
- **S9** — The corrections to the CLOSED spec 4, recorded in §4 of this spec and not in spec 4.
  NOT OBSERVED — a record of what spec 4 claimed wrongly, with no code to observe; AC3 and AC4 are the
  observations spec 4's claims lacked.
- **S10** — On the live tree, the whole hygiene output and its exit code are `cmp`-equal at this
  unit's parent and at this unit. Observed by AC8.

## 3. Non-goals (OUT)

- No change to any line of the hygiene shell outside the comment block above the id-classifier
  block: the split, the fallback and both launches stay byte for byte.
- No change to the code of `cmd_check_with_ids`. The review's optional crash sentinel, which re-runs
  a crashed verb as its own launch, is not built: S6 states the crash bytes instead.
- No edit to spec 4 or spec 3. Both are CLOSED and stay frozen; §4 carries their corrections.
- No `gotchas.py` contract clause in `tools/memory-tree/kit.toml`. That is `TOOL-aHastenedSweep-5`.
- No left-shift gate. The main loop files these as asks, one per class the review names:
  - `assertion-floor-left-below-the-added-arms`, a floor-count check (M1);
  - `both-red-fixture-hides-a-swapped-rc`, a one-red-arm rule (M2);
  - the fallback's assignment block registered with the `harness arms (fail branches armed or
    pinned)` leg (M3);
  - `criterion-asserts-what-its-own-command-cannot-show`, a Red-when staged-break rule (M4);
  - `in-process-fold-claims-standalone-bytes`, a crash-path identity row (L1);
  - `observed-by-claim-no-arm-discharges`, an Observed-by rule (L2);
  - `a-folded-field-leaves-its-row-shape-docs-behind`, a folded-launch grep (L3);
  - `amendment-leaves-its-other-half-standing`, a non-goal map grep (L4).
- No kit version move: the lander mints it.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- No self-test suite and no bar inside the pass, a sliced suite included.

## 4. Design

### Evidence

Read at the build's tip `13863b03e` on 2026-11-16, which the review's pin `cf64f39df` precedes by one
records commit.

- The one-process launch is `tools/memory-tree/check-memory-hygiene.sh@71e199ce1cc2:3226`. The split
  is `:3227-3232`, and the fallback
  `[ "$_onepy" = 1 ] || { ids=$_both; _idsrc=1; got=""; _gotrc=1; _onepy=1; }` is `:3234`. The
  bug-class block launches `gotchas.py --check` alone at `:3257` only when `_onepy` is not `1`.
  The comment saying the shell "PRINTS them on demand" is `:3208`.
- `resolve_python` (`tools/memory-tree/check-memory-hygiene.sh@71e199ce1cc2:465`) RUNS each
  candidate with `-I -c` at `:482`, and `GOV_PYTHON` is candidate 2 at `:476`, echoed as given when it
  runs at or above the floor. With no candidate the run exits 2 at `:615`. A wrapper must therefore
  pass the probe through to a real interpreter.
- `add_offender_keys` (`tools/memory-tree/check-memory-hygiene.sh#add_offender_keys`) drops the first
  line it is handed and every line ending `:`, and prefixes the rest with `check <key>` and a tab.
- Unit 3's arms are `tools/memory-tree/check-memory-hygiene.test.sh@4a13ab303877:3352-3389`: four
  top-level `n=$((n+1))` sites, one of them inside a two-pass loop, so five assertions, none skipped.
  Unit 4's are `:3392-3417`, two assertions. `FLOOR_ASSERTIONS=710` is `:4812`, and its last RAISED
  entry, `:4810-4811`, credits unit 4 alone.
- The `_b1` fixture (`tools/memory-tree/check-memory-hygiene.test.sh@4a13ab303877:3313-3350`) is
  otherwise clean and prints corpus_ids' `READ_PATH_CEILING is declared` notice at exit 0, so a
  green id-classifier block still has lines to key when its rc is misread. It has no
  `memory/gotchas/` directory, and `gotchas.py#cmd_check` prints nothing and returns 0 on a tree with
  no record and no INDEX.
- The suite already ships a `GOV_PYTHON` wrapper that fails one call and execs the real interpreter
  for the rest: `pywrap.sh` at `tools/check-install-prefix.test.sh@f9b2fd1f258c:296-302`.
- The exemption note is `tools/memory-tree/check-memory-hygiene.test.sh@4a13ab303877:3068-3069`. The
  `corpus_ids.py` docstring bullet is `tools/memory-tree/corpus_ids.py@d88903f124ca:17-20`. The
  dossier bullet is `memory/map/features/memory-tree-hygiene.md@02cd1131f952:169-175`.
- `gotchas.py#cmd_check_with_ids` frames each verb as
  `f"{err.getvalue()}{out.getvalue()}\x1d{rc}\n"` at `tools/memory-tree/gotchas.py@776abcc606f2:702`.
  Its except line is `:699`, `traceback.print_exc()` inside the redirect is `:700`, and the docstring
  is `:677-683`. The verb list binds `ids.main` from the module `_load_corpus_ids()` returned, so a
  loader that replaces `main` on the module it returns reaches the per-verb loop.
- The with-ids selftest arm is `tools/memory-tree/gotchas.py@776abcc606f2:1269-1314`: fixture `tw`,
  loader `load_counted`, helper `run_alone`, and the swap of `globals()["_load_corpus_ids"]` with its
  restore. The selftest's `arm` (`:1004`) redirects stdout and reports a raised exception as
  `UNEXPECTED`.

### The suite arms (S2, S3)

Both go after unit 4's block, before the project-key section, and copy `_b1` into a fresh
`mktemp -d` as unit 4's arm does.

The bug-class-only fixture adds `memory/gotchas/x.md` naming no gate, runs `gotchas.py --write`
and commits, with no `ORPHAN_ID_PIN`. The id-classifier-only fixture appends `ORPHAN_ID_PIN="0"`
and an orphan citation to `memory/README.md` and commits, with no gotchas record. Each runs
`check-memory-hygiene.sh --offenders` once and is one `case` assertion. Exchanging `_idsrc` and
`_gotrc` at the end of the split keys corpus_ids' notice under `check 13-16` and drops the check 18
key in the first fixture, and drops the check 14 key in the second, so each arm reds alone.

The wrapper arm writes, under its own `mktemp -d` and outside the fixture tree, a script in the
`pywrap.sh` shape with the suite's `$_PY` substituted:

```bash
#!/usr/bin/env bash
case " $* " in *" --check-with-ids "*) echo "wrapper: an unframed answer"; exit <RC> ;; esac
printf '%s\n' "$*" >> <LOG>
exec <the suite's _PY> "$@"
```

A loop over `<RC>` of 0 and 2 runs `GOV_PYTHON=<wrapper> bash check-memory-hygiene.sh --offenders` in
a clean `_b1` copy. Exit 0 reaches the fallback through the split's failed `[[ ]]`, and exit 2 through
the failed launch, which is the usage exit an older adopter-owned `gotchas.py` gives. Each pass
asserts a non-zero exit, the line `check 13-16<TAB>wrapper: an unframed answer`, and no log line
ending `gotchas.py --check`. The fallback's `_idsrc=1` set to 0 reds both passes on the key only: the
same fallback line sets `_gotrc=1`, and the catalogue block's `status=1` on it keeps the exit at 1, so
the exit assertion moves only when both `_idsrc=1` and `_gotrc=1` are zeroed and checks neither alone.
Its `_onepy=1` dropped reds both on the log.

### The selftest arms (S4, S5)

`check_framed_with_ids` gives up its chdir, loader swap and redirect to a nested
`run_framed(loader)`, which returns the captured text, and `run_alone` moves beside it. The existing
arm calls both and keeps its output line, so its want string is unchanged. A nested
`load_with_main(fn)` returns a loader whose module has `main` replaced by `fn`. Each new arm splits
the capture with `re.findall(r"(.*?)\x1d([0-9]+)\n", text, re.S)` and prints one line:

| Arm | `fn` | Prints when it holds |
|---|---|---|
| S4 | writes `with-ids stderr line` to `sys.stderr`, `with-ids stdout line` to `sys.stdout`, returns 3 | `with-ids err-first 3 · second same` |
| S5 | raises `RuntimeError("staged in the with-ids arm")` | `with-ids raise 1 traceback · second same` |

S4 holds when frame one equals the stderr line, then the stdout line, each newline-terminated, at
rc 3. S5 holds when frame one starts with `Traceback (most recent call last):`, holds
`in cmd_check_with_ids` and `RuntimeError: staged in the with-ids arm`, holds no `in <module>`, and
its rc is 1. Both need the second frame to equal `run_alone(main, ["gotchas.py", "--check"])` in `tw`.

### The texts (S6, S7, S8)

- `cmd_check_with_ids` docstring: the framing sentence ends at the frame shape. Add that neither
  `--check` writes stderr on a clean run. On a crash the frame holds the in-process traceback, which
  starts at this function's frame rather than the standalone `<module>` frame, in this process's
  stream encoding, ahead of all of the verb's stdout, at rc 1.
- The `except Exception:` comment: `noqa: BLE001 — the in-process traceback, from this frame,
  ahead of the verb's stdout`.
- The suite note: `sets it on its own launch of corpus_ids.py --check, or of gotchas.py
  --check-with-ids on an unscoped run, never in a conf`.
- The `corpus_ids.py` bullet and the shell comment at `:3208` each gain one sentence: when the
  shell's own checks 1 to 5 ran clean it hands `--print-index-set`'s answer down on stdin under
  `GOV_INDEX_SET_STDIN=1` (`TOOL-aHastenedSweep-3`).
- The dossier bullet's hand-down sentence: on an unscoped, unstaged run whose checks 1 to 5 recorded
  no failure, the engine hands the index set down on stdin under `GOV_INDEX_SET_STDIN=1` to its
  single `gotchas.py --check-with-ids` launch, which runs corpus_ids' `--check` in-process. A scoped
  run's `corpus_ids.py --check` always asks the print mode, and so does the standalone CLI, so the
  refusal of findings still fires (`TOOL-aHastenedSweep-3`, `TOOL-aHastenedSweep-4`).

### Corrections to spec 4

Spec 4 (`spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md`, CLOSED at rev-2) stays frozen. Where it and
this section disagree, this section holds.

- AC1's Red-when clause "a verb's stderr is dropped", and the §5 risks claim that AC1's arm reds on
  an edit printing before a stderr write, are not shown by spec 4's command: its fixtures reach no
  stderr write. This unit's AC3 and its S4 arm show both.
- S4's "Observed by AC1, AC2 and AC6" does not hold for the per-verb exception route: AC6 stages its
  raise before the per-verb loop. This unit's AC4 and its S5 arm observe it.
- The §4 frames text "stderr first as the two-process `2>&1` capture put it" and "What it does not
  check" on the traceback hold for a clean verb only. A crashed verb's frame is the in-process
  traceback that S6 describes.
- The §3 non-goal "No edit to `memory/map/features/memory-tree-hygiene.md`" is superseded by S8.
- The §7 hygiene-suite arm moved `FLOOR_ASSERTIONS` by its own two assertions and left spec 3's five
  uncounted; spec 3's three New-arm lines read `none` for the floor. S1 counts them.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `run_framed` | nested function in `gotchas.py#cmd_selftest` | `py.function`; the lexicon's `--suggest` is the pass's check |
| `load_with_main` | nested function in `gotchas.py#cmd_selftest` | `py.function`; as above |
| `_ixw`, `_ixl` | suite shell globals: the wrapper's directory and its log | none; underscore-led as the suite's arm-local globals |

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `memory/map/features/memory-tree-hygiene.md`
- `memory/map/generated/symbols.json`, if `gen_map.py --write` moves it
- `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-6-1-acceptance-ledger.md`
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, which the manifest ratchet owes
  whenever the hygiene shell, a watched file, is staged

### Rollout

One pass at order 5, after `TOOL-aHastenedSweep-5` is CLOSED: both units' CLOSED flips re-render the
build README, which `--dispatch` refuses to two open siblings. No contract, file or output passes
between them. The spec lands in a records commit before the code. The pass runs
`python tools/codebase-map/gen_map.py --write`, and the status flip to CLOSED is its last change.

### Alternatives rejected

- **One floor raise per arm or per unit.** The review's fix is one raise naming every unit it counts,
  and one RAISED line is the shape the entries above it take.
- **Dropping AC1's stderr clause from spec 4 instead of adding the S4 arm.** Spec 4 is CLOSED, and the
  drop leaves the frame order unguarded. The brief chooses the arm.
- **A wrapper that answers every call with the bad line.** `resolve_python` runs it first, finds no
  version, and the run exits 2 before the id-classifier block (`:615`).
- **The crash sentinel and a re-launch of the crashed verb (L1's optional fix).** It adds a branch and
  a launch for crash bytes no verdict reads; the rc and the status already match.
- **Asserting the shell's keying of a crash (L2's last clause) in a suite arm.** A crash is a framed
  rc 1 on one side, which the S2 id-classifier-only arm already keys and guards.

## 5. Acceptance criteria

`$SCRATCH` is the run's scratch directory. Fixtures are git repositories the probe builds under
`%TEMP%/hs6f`, a short path, in the `_b1` shape. `$KIT` is the worktree's `tools/memory-tree` as an
absolute path.

- **AC1** — When `bash "$SCRATCH/t6-onered.sh"` runs `check-memory-hygiene.sh --offenders` in the
  bug-class-only fixture and then the id-classifier-only one, it prints
  `bug-class-only 17-19 yes 13-16 no` and `id-classifier-only 13-16 yes 17-19 no`. With `_idsrc` and
  `_gotrc` exchanged at the end of the split as a staged break, both lines change.
  Red when: the fixture reds both verbs, or the split reads one verb's rc for the other.
  fixture: built by the probe; no tree holds one today.
- **AC2** — When `bash "$SCRATCH/t6-wrap.sh"` runs the S3 wrapper over a clean fixture at wrapper
  exits 0 and 2, it prints `wrap 0 rc 1 keyed 13-16 relaunch 0` and `wrap 2 rc 1 keyed 13-16 relaunch 0`.
  With the fallback's `_idsrc=1` set to 0 it prints `rc 1` and no key, and with its `_onepy=1`
  dropped it prints `relaunch 1`.
  Red when: the fallback keys nothing under `check 13-16`, keys under `check 17-19`, or launches
  `gotchas.py --check` again; its exit assertion reds only when both `_idsrc=1` and `_gotrc=1` are zeroed.
  fixture: built by the probe; no tree holds one today.
- **AC3** — When `python "$SCRATCH/t6-frame.py" stderr` runs the S4 case through
  `gotchas.py#cmd_check_with_ids` in-process, it prints `with-ids err-first 3 · second same`. With
  `err.getvalue()` dropped at the frame write, and with stdout put ahead of it, it prints something else.
  Red when: a verb's stderr leaves its frame, the frame puts stdout first, or the rc field is not the verb's.
- **AC4** — When `python "$SCRATCH/t6-frame.py" raise` runs the S5 case, it prints
  `with-ids raise 1 traceback · second same`. With `traceback.print_exc()` moved after the redirect's
  `with` block, it prints something else, and with `except Exception` narrowed to `except OSError` the
  probe ends in `RuntimeError`.
  Red when: the traceback leaves the crashed verb's frame, the exception escapes the per-verb loop,
  or the second verb is skipped after the first crashes.
- **AC5** — When `grep -cx 'FLOOR_ASSERTIONS=719' tools/memory-tree/check-memory-hygiene.test.sh`
  runs it prints 1, and the RAISED line above it names `TOOL-aHastenedSweep-3`,
  `TOOL-aHastenedSweep-4` and `TOOL-aHastenedSweep-6`.
  Red when: the floor stays below the count of the arms it pins.
  figure: DERIVED by reading at the tip, 710 plus unit 3's five plus this unit's four. The close's
  suite run prints the count, and the floor equals it.
  permission: the suite's printed count is the main loop's at the close, not the pass's.
- **AC6** — When `grep -c 'in-process traceback' tools/memory-tree/gotchas.py` runs it prints at
  least 2, and `grep -c 'gotchas.py --check-with-ids'` prints at least 1 over the suite's exemption
  note and the dossier. `grep -c 'GOV_INDEX_SET_STDIN=1'` prints at least 1 over `corpus_ids.py` and
  over the hygiene shell's comment block above the id-classifier block.
  Red when: a text still names only the `corpus_ids.py --check` launch, or a crash claim names
  standalone bytes.
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs it exits 0. `bash -n` on both
  shell files and `python -m py_compile` on `gotchas.py` and `corpus_ids.py` exit 0, and
  `git diff -U0` over the hygiene shell shows comment lines only.
  Red when: the pass rewrites a status line, adds a `status=1` or `fail` site, or edits shell code.
- **AC8** — When the whole `check-memory-hygiene.sh` runs from the worktree root on the live tree,
  once from this unit's parent's `tools/` extracted with `git archive` under `%TEMP%/hs6a` and once
  from the unit's own, `cmp` of the two outputs exits 0 and the exit codes match.
  Red when: any byte of any check's output moves.
  cost: two full hygiene runs, each 805 to 1093 s on node a (PINNED, the 2026-11-15 bar ledgers).
  permission: the main loop's at the close, under a `Pass: none` commit; a unit pass does not run it.
  fixture: the live tree at the close's tip.

## 6. Gates

`memory hygiene` · `memory-hygiene self-test` · `corpus-ids selftest` · `gotchas selftest` · `harness arms (fail branches armed or pinned)` · `spawn budget (forks per hot entrypoint)` · `shell hygiene (a fork spent on builtin work)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `playbook render selftest` · `policy fixtures`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 · `_idsrc` and `_gotrc` exchanged at the end of the split reds both one-red arms · `FLOOR_ASSERTIONS` 710 -> 719, shared with the next two lines
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 · the fallback's `_idsrc=1` set to 0, then its `_onepy=1` dropped, reds both wrapper passes · counted in the line above
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · unit 3's block wrapped in `if false; then … fi` drops five assertions under the floor · the floor itself
New arm: tools/memory-tree/gotchas.py --selftest · covers AC3 AC4 · `err.getvalue()` dropped from the frame write, then `traceback.print_exc()` moved after the redirect · none

A pass checks its own change with `bash -n`, `python -m py_compile`, `check-arms`, the lexicon, the
spec-token checker and the AC1 to AC7 commands over its fixtures. The close runs the bar once,
observes each arm red then green, and runs AC8.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-16 · initial draft from `prompts/2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md` and
  the closing review's round 1, grounded at the build's tip `13863b03e`.
- rev-2 · 2026-11-16 · the fallback's `_idsrc=1` break reds the S3 arm on its key only, since the same
  line sets `_gotrc=1` and the run stays at exit 1; section 4 and AC2 say so, and AC2's Red-when names
  what the exit assertion does not check (the builder's divergence return of 2026-11-16).

## 9. Reuse audit

The seams this unit extends: the suite's `_b1` fixture and unit 4's `--offenders` arm shape in
`tools/memory-tree/check-memory-hygiene.test.sh`; the `pywrap.sh` wrapper of
`tools/check-install-prefix.test.sh`, which fails one call and execs the real interpreter for the
rest; and the with-ids arm's `load_counted`, `run_alone` and loader swap in
`tools/memory-tree/gotchas.py#cmd_selftest`, which `run_framed` and `load_with_main` factor out
rather than copy. `python tools/codebase-map/reuse_lookup.py "a fake python wrapper that fails one
verb and passes every other call through"` ranked `fail` and `resolve_python` first, and the second
is the resolver the wrapper must pass. Recall named the dSafePassage spec audit's `pywrap.sh` reading,
which confirms a wrapper at the floor is echoed as given, and `TOOL-aWokenSentinel-19`, the floor's
origin.

Recall terms used: `python tools/memory-recall/query.py "how does a suite arm drive a delegated
checker failure through a python wrapper" --terms "GOV_PYTHON wrapper pywrap fallback frame
check-with-ids offenders FLOOR_ASSERTIONS one-red arm selftest stderr"`
