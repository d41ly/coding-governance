# TOOL-aMeasuredDrag-11 — the merge bar hands its own resolved python to its legs, so no leg re-probes the launcher

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-11-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-11-red-fix-3.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-11-red-fix-3.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-11-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-11-1-builder.md) | journal | — |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md) | diff-review | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 |

<!-- /gen:spec-records -->

## 1. Goal

Every bash leg of the bar re-resolves the python launcher, and each resolution spawns a probe of a
launcher the runner already resolved (finding spawns-8). The runner hands its resolution to its legs
under a runner-set variable, and the resolver block echoes it without a probe whenever the inputs
that decided it are unchanged, so no verdict, refusal or printed line moves.

## 2. Scope (IN)

- **S1** — The resolver block. `tools/lib/resolve-python.sh#resolve_python` gains one memo rung
  before its candidate loop: it reads `GATE_RESOLVED_PY` and echoes the launcher it carries, with no
  spawn, only when the caller passed no override, the carried `GOV_PYTHON` and `PATH` equal the
  current ones byte for byte, and the carried version is at or above the block's own floor. Any
  other value, malformed or absent included, is ignored and the loop runs exactly as today.
  Observed by AC1, AC2 and AC3.
- **S2** — The copies. Every inline copy of the block is re-synced byte-identically: the population
  is what `git grep -l '^# >>> resolve_python' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md`
  names, the derivation `tools/lib/python_floor.py#read_parity_population` uses, as
  TOOL-dSafePassage-23 S4 re-synced it. Observed by AC4.
- **S3** — The runner. `tools/run-gates/run-gates.sh` unsets an inherited `GATE_RESOLVED_PY` before
  it resolves `PYBIN`, so an inherited value is never admitted, and exports its own after the
  toolchain digest is taken and before any leg runs. Observed by AC5.
- **S4** — The push hook's classification. `.githooks/pre-push` names `GATE_RESOLVED_PY` in
  `ENV_DROPPED_KNOBS`, beside `GOV_PYTHON`, so the hook clears it before `gate-env.sh` runs and the
  knob-class arm of TOOL-aRepatriatedFork-49 S5 finds it classified exactly once. Observed by AC6.
- **S5** — The help page. `help/python-floor.md` says the resolver takes the bar's own resolution
  first, inside a bar, and when it does. Observed by AC7.
- **S6** — The measurement. The changed call is timed before and after beside a spawn baseline, and
  the figures are recorded in the unit's acceptance ledger. Observed by AC8.
- **S7** — Two new suite arms, declared under §7. NOT OBSERVED by a pass criterion: the main loop
  observes each arm RED on its staged break and GREEN once restored, at the close (M8).

## 3. Non-goals (OUT)

- Exporting from any other runner: `tools/run-gates/run-selftests.sh`,
  `tools/unattended/run-unattended-gates.sh` and the hooks keep resolving for themselves.
  `tools/run-gates/pass-legs.sh` starts `run-gates.sh`, so it inherits S3 without an edit.
- Exporting `GOV_PYTHON` itself, or keeping it through `.githooks/pre-push`. The review's table row 32
  proposed the second; the brief rules it out, because TOOL-aRepatriatedFork-49 drops it on purpose.
- Any change to the candidate order, the floor, the probe, the refusal text or `platforms.provision`.
- Caching a resolution across bars, on disk or by content key: that is §5 of the review, out of scope.
- `tools/run-gates/measure_legs.py`: it scrubs every `GATE_*` name, so its measured legs keep probing.
- The adopter repositories. Each receives the new block on its next adopt.
- Any self-test suite or the bar inside the pass.

### Edges

- **hands-off** external — the other runners listed in the first bullet above, which could export
  the same memo; a follow-up ask once this one is measured.

## 4. Design

### Evidence

Read at base `aebbb4a72`; the run branch's HEAD `6d98c39ca` holds the same blobs for every file
cited here, because its commits after the base are records only.

- `tools/run-gates/run-gates.sh@bfc3ad495:338` resolves `PYBIN=$(resolve_python)` and exports
  nothing. The runner substitutes `PYBIN` into a python argv leg, but a bash leg's script carries the
  block and resolves again.
- `tools/lib/resolve-python.sh@9ec71b5b6:36-43` probes each candidate with one spawn of
  `"$_rp_c" -I -c`, in the order `"${1:-}"`, `"${GOV_PYTHON:-}"`, `python3`, `python`, `py`. It has
  no memo. Its floor is the literal `_rp_floor` at `:33`, and `_rp_fv` at `:34` is its integer form.
- `.githooks/pre-push@2714fe14b:535` declares `ENV_DROPPED_KNOBS="GOV_KITROOT GOV_PYTHON"`, and the
  loop at `:538` also unsets every `*_PY` name in the environment.
- `.githooks/pre-push.test.sh@a13521651:1750` derives every `$GATE_*` or `$GOV_*` name the runner
  reads, and the arm reds a name that is not in exactly one of `ENV_DROPPED_KNOBS`,
  `BAR_SCRUBBED_KNOBS` or `BAR_INERT_KNOBS` (`:1737`).
- `tools/run-gates/run-gates.sh@bfc3ad495:3502-3551` computes `REUSE_DIGEST` from `compgen -e` over
  the classes `GATE_*|GOV_*|*_PY|…` (`:3548`) in a direct bar, and from the hook's file of the
  caller's environment under `push`. A name exported before `:3502` would enter a direct bar's key
  and never a push bar's, which is the divergence TOOL-aSparedSpawn-33 closed.
- `tools/gate-lint/fork-count.sh@e97c34c2a:51-53` unsets every `GATE_*` name before it counts, and
  `tools/run-gates/measure_legs.py@57aa3b9bc:410` scrubs every `GATE_*` name. A `GATE_` name keeps
  the fork ceilings and the leg profiles reading what they read today.
- `tools/lib/resolve-python.test.sh@4b2fb1fb8:66-75` arm (b) shadows every launcher on a prepended
  `PATH` and expects a refusal with `GOV_PYTHON` inherited. That arm is why the memo must key on
  `PATH` and `GOV_PYTHON` and why exporting `GOV_PYTHON` was rejected below.
- The resolver's version at the runner is already known: the manifest parse prints `sys.version` of
  `PYBIN` as `PY_ID` (`run-gates.sh@bfc3ad495:2915`, read at `:2995`). No extra spawn is needed.

### Data model

`GATE_RESOLVED_PY` holds four fields joined by a newline, in this order:

| line | field | value |
|---|---|---|
| 1 | version | `<major>.<minor>` of `PYBIN`, taken from the leading digits of `PY_ID` |
| 2 | launcher | `PYBIN`, exactly as `resolve_python` printed it |
| 3 | override | `${GOV_PYTHON:-}` as the runner saw it, empty when unset |
| 4 | path | `$PATH` as the runner saw it; the rest of the value |

The block admits the memo only when all four hold: `"${1:-}"` is empty; lines 3 and 4 equal
`${GOV_PYTHON:-}` and `$PATH` byte for byte; line 2 is non-empty; and line 1 parses as two digit
runs whose integer form, computed as `_rp_fv` is, is at least `_rp_fv`. Then it prints line 2 and
returns 0. Nothing is printed on a miss, and the loop proceeds as today.

Why these keys decide the result: with no caller override, the loop's outcome is a function of
`GOV_PYTHON`, the launchers `PATH` finds and the floor. The runner's resolution ran with the same
three, so a leg under the same `PATH` and `GOV_PYTHON` would print the same launcher. The version
field carries the floor across copies, so a fixture copy raising its own floor is refused the memo.

### Mechanism

- **The block (S1).** The rung sits after `_rp_fv` is computed at `:34` and before the loop. It uses
  bash parameter expansion and `[[ =~ ]]` only, so a hit spawns nothing. The marker lines and the
  rest of the block are unchanged.
- **The copies (S2).** The builder rewrites the text between the two marker lines of every file the
  S2 derivation names with the canonical block, by one scripted pass, and commits the copies in the
  same commit as the canonical.
- **The runner (S3).** `unset GATE_RESOLVED_PY` is added immediately before `:338`, beside the
  pattern `unset GATE_ATTRIBUTE` at `:377` follows. The export is added immediately after the
  `REUSE_DIGEST` assignment at `:3551`, so neither digest mode reads it. Every leg runs after that
  line. A nested bar a leg starts unsets the inherited value on entry, so it resolves and keys
  exactly as it does today.
- **The hook (S4).** `ENV_DROPPED_KNOBS` gains `GATE_RESOLVED_PY`. The loop at `:538` already unsets
  it through the `*_PY` case. The listing makes the drop explicit and classifies the knob for the
  H49 arm.

### Inventory

One name is minted: the environment variable `GATE_RESOLVED_PY`. It is runner-set: no operator
sets it, no document invites one to, and the runner discards an inherited value. The `GATE_` prefix
puts it inside every scrub that already clears bar knobs, and the `_PY` suffix puts it inside the
hook's interpreter drop. `git grep -n GATE_RESOLVED_PY` returns no hit outside this build's records
at base `aebbb4a72`.

### Files touched (estimate)

- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `.githooks/pre-push`
- `help/python-floor.md`

The inline copies of S2, derived by the `git grep` S2 names, are re-synced in the same commit and
added to this unit's `--dispatch --writes`. That population is 80 files, PINNED at `aebbb4a72`, the
six files above among them.

### Rollout

Live at landing, with no switch: a miss runs today's code path, so the only new behaviour is a hit
that prints what the probe would have printed. It builds at order 11, the last of this build. The S2
population includes `tools/unattended/unattended.sh` and
`tools/memory-tree/check-memory-hygiene.sh`, which TOOL-aMeasuredDrag-1 and TOOL-aMeasuredDrag-3
edit, so the write sets intersect and the passes are sequenced. The edits touch different lines:
this unit changes only the lines between the resolver markers. The unlanded branches
`branch/speedups-9c2e63` and `branch/alightenedloop-eb7b8b` change no `_rp_` line, measured with
`git diff main...<branch>` at `6d98c39ca`.

### Migration

None in this repository. At an adopter, a new block beside an old runner never sees the variable and
probes, and an old block beside a new runner ignores it. Both mixes print what they print today.

### Alternatives rejected

- **Export `GOV_PYTHON` from the runner.** No block edit, and a probe of the direct executable rather
  than the alias would still halve the cost. It reds `resolve-python.test.sh` arm (b), which inherits
  `GOV_PYTHON` and expects a shadowed `PATH` to refuse, and it re-opens the planted-interpreter path
  TOOL-aRepatriatedFork-49 closed.
- **A memo keyed on nothing.** Every arm that shadows `PATH` or sets `GOV_PYTHON` would read the
  bar's interpreter and pass where it refuses today.
- **Key on the runner's floor instead of the launcher's version.** The runner resolves inside a
  command substitution, so it cannot read the block's `_rp_floor`. The version is already in `PY_ID`.
- **Export at `:338`.** A direct bar's toolchain digest would carry the name and a push bar's would
  not, so a leg verdict earned by one would never be reused by the other.
- **A name outside the `GATE_` prefix.** `fork-count.sh` would admit the memo while it counts, and its
  recorded fork counts would move.

## 5. Production-readiness checklist

- security: an inherited value is admitted by no bar: the runner unsets it before it resolves, and
  the push hook drops it before `gate-env.sh` runs. Outside a bar, a value a caller plants can name
  only what `GOV_PYTHON` can already name, and it must match the caller's own `PATH` and override.
- perf / scale: a hit spawns nothing. The before figure, PINNED on node a on 2026-11-15 at
  `aebbb4a72`: ten resolutions took 2.342 s, beside 0.578 s for ten `bash -c true` and 0.234 s for
  ten `/usr/bin/true`, so one probe costs about 176 ms (PINNED, same run). The review counts about
  504 resolutions per `check-unattended.test.sh` run (PINNED in the findings record at `aebbb4a72`).
- error / empty / loading states: a malformed, empty or partial memo is a miss, never a refusal; the
  refusal text and its order are unchanged, because a miss prints nothing.
- observability: none added. A hit prints exactly what a probe prints; the timing in AC8 is the
  record of the saving.
- risks: a `PATH` holding a relative entry, or a launcher installed or removed under an unchanged
  `PATH` while a bar runs, could make a probe disagree with the memo; no leg does either at base.
  `PATH` is carried twice in the environment; it is 979 characters on node a (PINNED, 2026-11-15).
- testing: the two new arms under §7, plus AC1 to AC6 as pass probes.
- migration: N/A — no data or format moves; the Migration sub-head above covers adopter mixes.
- user docs: `help/python-floor.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `GATE_RESOLVED_PY=$'3.15\n/no/such/py\n'"${GOV_PYTHON:-}"$'\n'"$PATH" bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs, it prints `/no/such/py`, writes nothing to stderr and exits 0.
  Red when: the block probes the memo's launcher, which does not exist, or ignores a matching memo.
- **AC2** — When the AC1 command runs in each of five variants, its stdout, stderr and exit status
  equal those of the same variant with `GATE_RESOLVED_PY` unset, compared with `cmp`: a fake
  `python3` stub directory prepended to `PATH`; `GOV_PYTHON` set to that stub; a caller override
  passed as `resolve_python "$2"`; the memo's version line `3.14`; and a memo of three lines.
  Red when: any variant admits the memo, so its stdout reads `/no/such/py`.
  fixture: the stub directory and its 9009 fake are built under the run's scratch, as the
  resolver's own suite builds its stubs.
- **AC3** — When `bash -c '. "$1"; resolve_python' _ <file>` runs over the real tree with `<file>`
  first the base block, written to scratch by `git show` of that file at base `aebbb4a72`, and
  then the built `tools/lib/resolve-python.sh`, with `GATE_RESOLVED_PY` unset and then set to a memo
  whose launcher is the base run's output, all four runs print the same stdout, the same stderr and
  the same exit status.
  Red when: the built block prints a launcher, a line or an exit status the base block does not.
- **AC4** — When every file the S2 `git grep` names has the text between its two resolver markers
  compared with the canonical's by `sed -n '/^# >>> resolve_python/,/^# <<< resolve_python/p'` and
  `cmp`, no file differs; and `python tools/lib/python_floor.py check` exits 0.
  Red when: one inline copy was not re-synced, or a copy's floor literal moved.
- **AC5** — When `grep -nE '^unset GATE_RESOLVED_PY|^PYBIN=\$\(resolve_python\)|^\) && REUSE_DIGEST=|^export GATE_RESOLVED_PY' tools/run-gates/run-gates.sh`
  runs, it prints exactly four lines, in the order unset, `PYBIN`, digest, export.
  Red when: the unset follows the resolution, so an inherited memo could choose `PYBIN`, or the
  export precedes the digest, so a direct bar's key would carry the name.
- **AC6** — When the `ENV_DROPPED_KNOBS` line and the loop after it in `.githooks/pre-push` are
  sourced from scratch with `GATE_RESOLVED_PY=x` set, `GATE_RESOLVED_PY` reads unset afterwards and
  `ENV_CLEARED` names it; and `grep -n '^ENV_DROPPED_KNOBS=' .githooks/pre-push` names it.
  Red when: the hook leaves an inherited memo for its own resolver or for the bar.
- **AC7** — When `git grep -n GATE_RESOLVED_PY -- help/python-floor.md` runs, it prints the sentence
  saying that inside a bar the resolver first takes the runner's own resolution, and when.
  Red when: the page still lists the candidate order without the memo rung.
- **AC8** — When ten runs of the AC3 command over the built block are timed with
  `GATE_RESOLVED_PY` unset and then set to a matching memo, beside ten runs of `/usr/bin/true`, the
  set loop costs less than the unset loop by at least the spawn of ten probes.
  Red when: a hit still spawns the probe, so both loops cost the same.
  figure: the before loop is PINNED at 2.342 s on node a on 2026-11-15; the after loop is DERIVED
  at observation time and recorded in the ledger beside its baseline.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `pre-push self-test` · `run-gates canary` · `measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 · a block copy with the memo rung deleted reds the hit arm, and one whose key compare drops `PATH` reds the shadowed-PATH miss arm · the suite's declared assertion count
New arm: tools/run-gates/run-gates.test.sh · covers AC5 · a scratch bar, as at its `:499`, with an inherited sentinel memo and one leg that records the memo it sees and the launcher it resolves; staged by deleting the runner's unset line · the suite's declared assertion count

The close runs the bar once; the pass legs run after the unit's commit. The knob-class arm of
`.githooks/pre-push.test.sh` already reds an unclassified `GATE_RESOLVED_PY`, which is S4's check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seam is `tools/lib/resolve-python.sh#resolve_python`, edited in place: `reuse_lookup.py` ranks
`resolve_python` a SEAM with 81 installs (PINNED at `aebbb4a72`), and the runner's `PYBIN` at
`tools/run-gates/run-gates.sh@bfc3ad49:338` is the value it hands on. The copy re-sync follows TOOL-dSafePassage-23 S4, which
changed the same block across the same population and bumped no kit version. The reuse probe was
`python tools/codebase-map/reuse_lookup.py "hand the resolved python launcher to child legs so they skip the probe"`.
Recall returned TOOL-dSafePassage-75, which keeps `GOV_PYTHON` through the step environment, and
TOOL-aRepatriatedFork-49, which drops it at the push hook; S3 and S4 keep both. The first recall run
failed on a cache file another process held, and the retry answered.

Recall terms used: `python tools/memory-recall/query.py "how does the bar pass its resolved python to legs and why is GOV_PYTHON dropped" --terms "resolve_python GOV_PYTHON pre-push dropped interpreter PYBIN legs runner export probe floor"`
