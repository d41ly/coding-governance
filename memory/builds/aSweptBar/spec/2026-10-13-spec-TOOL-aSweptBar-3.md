# TOOL-aSweptBar-3 — the run-gates evidence and pre-push suites' standalone reds, each at its root

**Status:** CLOSED · rev-2 · 2026-10-13 · node a · Tier-1 · base 53b25884 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md) | research | TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |
| [2026-10-13-prompt-TOOL-aSweptBar-3-2-fix-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-3-2-fix-brief.md) | journal | — |
| [2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md) | diff-review | TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

Run alone on node a over `53b25884`, the run-gates evidence suite and the pre-push suite stay red, so
their reds are not contention. Each red is an arm or a helper that drifted from the code it grades,
which the reuse cache, the push cover pass or the reuse probe moved under it. This unit fixes each at
the arm, so both suites read green alone and each arm reds again on its own break.

## 2. Scope (IN)

- **S1** — evidence S2's broken copy: the trailing-newline sed matches the strip loop as it now
  stands on one line, and the redaction-guard sed breaks both alternatives of the guard, so all six
  variants move. Observed by AC1.
- **S2** — evidence S2's log names: the gate-logs directory is cleared after the per-leg reference
  bar and before the broken bar, so `broken.logs` holds only the broken copy's log names. Observed
  by AC2.
- **S3** — evidence AC5 for `REUSE_SCHEMA`: the staged runner copy is committed before the run that
  must miss, so that run writes its entries on a clean tree and the control can reuse them. Observed
  by AC3.
- **S4** — evidence lineage controls: `check_lin_control` compares the refused row's input key with
  the key the lineage run computed, instead of running the cache's env mode. The AC3 lineage arm's
  earning bar becomes a full bar over an untracked file, so its rows carry the lineage key and an
  empty `full`. Observed by AC4.
- **S5** — evidence AC6, the opt-in run: an earning bar without `GATE_FULL` runs on the fixed tree
  before the opt-in bar. Observed by AC5.
- **S6** — evidence AC7: the location probe in `sb_want` takes the scrub the shell-hygiene leg
  prints. Observed by AC6.
- **S7** — pre-push 25b and `run_vr_push`: each push carries a tree that no earlier push in its
  fixture carried, so the cover pass has no record to answer with and the bar runs. Observed by AC7.
- **S8** — pre-push `run_rp_push` pushes to the remote it is handed. Observed by AC8.
- **S9** — pre-push PM AC3 counts only the post-merge red's reads, the shim lines naming
  `refs/gov/bar-red`. Observed by AC9.

## 3. Non-goals (OUT)

- No product change. `tools/run-gates/README.md` lines 362-371 name every exported `GATE_*` variable,
  `GATE_FULL` included, as a key input, and the cover pass is the hook's designed behaviour
  (TOOL-aFrugalTurnstile-2). The arms adapt to both.
- Whether `GATE_FULL` should leave the key, so a boundary's full bar could feed the cache's env mode,
  is a product question for a follow-up, not a fixture repair.
- The ten other pre-push reds in the bar log passed alone. They are contention, and the brief puts
  them out of scope.
- The `merge-loss check did NOT run` line in the fixtures is a note about an absent lexicon kit, not a
  refusal, and nothing here touches it.
- PM AC1 and AC5 keep counting every `ls-remote`. Their decisions are FULL, so the reuse probe never
  runs there, and their count is right as written.
- The fork idioms in both suites belong to `TOOL-aSweptBar-5`.

## 4. Design

**S1.** The runner's strip is now one line, `while [[ $out == *$'\n' ]]; do out=${out%$'\n'}; done`
(`tools/run-gates/run-gates.sh:3870`), and the sed at `tools/run-gates/run-gates.evidence.test.sh:2152`
still anchors on `do` at the end of a line. The guard is now `*://*@*|*$'\r\n'*)`
(`tools/run-gates/run-gates.sh:310`), and the sed still keys on `*://*@*) printf`. Both match nothing,
so the copy carries 4 of 6 variants, and the url leg's CRLF would route its output through `redact`
even if only the first alternative were broken. The strip sed keys on `; do ` with no end anchor and
rewrites the head to `while false; do `, so the loop never runs. The guard sed rewrites both
alternatives to patterns no leg output can match, `*://*@@@*|*$'\r'@@@*)`. Measured at spec time with
those two forms, built from explicit bytes in a scratch copy, the six seds move exactly six lines of
the runner. AC2 to AC4 can then red-detect, because the copy keeps trailing newlines and leaks the
credential.

**S2.** The brief traces AC3 to the same two seds. The code says otherwise. The per-leg reference bar
at line 2166 runs the runner with `local LC_ALL=C` intact and writes `sp____x_y.log` into
`$SB_T/.git/gate-logs`. The broken bar at line 2167 writes `sp___x_y.log` beside it, and line 2168
copies both into `broken.logs`. The arm's existence test then finds the reference bar's file, so AC3
can never see the caller-locale variant. The runner only creates that directory (lines 282-283) and
never clears it. One `rm -rf` of it between lines 2166 and 2167 makes `broken.logs` the broken copy's
alone. If AC3 still reds at the close with S1 and S2 both in, the cause is neither, and it goes back to
the main loop.

**S3.** `ru_repo` commits the runner copy, so the `sed -i` at line 1149 dirties a tracked file. The
cache is written only when the tree was clean at start (`[ "$TREE_CLEAN" = yes ]` at
`tools/run-gates/run-gates.sh:5423`), so the miss run writes nothing and the control reuses nothing.
A commit of the staged copy after the `sed -i` restores the premise the arm's comment states. HEAD is
no input of an undeclared leg's key, as the history arms show by reusing an undeclared guarded leg
across a commit. So the commit cannot be what makes the miss miss.

**S4.** The digest takes every exported `GATE_*` variable less the reuse knobs, the two turnstile
names, the run id and the two bases (`tools/run-gates/run-gates.sh:3386`, README line 369). So a bar with `GATE_FULL` set keys
differently from one without it, which the S2 section of this suite already relies on when it
substitutes an unresolvable base for `GATE_FULL`. TOOL-aSparedSpawn-32 S10 moved the lineage controls
from the ledger opt-in under `GATE_FULL` onto the cache's env mode, which cannot run under it. Every
earning bar in the AC4, AC5 and AC6 scratches sets `GATE_FULL`, so the env mode's key never equals
theirs and the control never reuses `pa`. The control's comment states its purpose: prove the lineage
refusal is the named term's, not a key that never matched. Comparing the two keys observes exactly
that, at the cost of no bar. `check_lin_control` reads field 4 of the `pa` row in the saved ledger,
the input key per README lines 807-808, and `read_ru_key pa` from the lineage run's record. It passes
when both are non-empty, not `-` and equal.

The same reading shows the AC3 lineage arm passes vacuously today. Its earning bar runs without
`GATE_FULL`, so its rows key differently from the lineage run, and the refusal is the key's rather
than the empty `full`. Under the key comparison its control would red, which is right. So the AC3
earning bar becomes a full bar over an untracked file, removed before `write_lin_fix` commits. A dirty
tree leaves `full` empty (`tools/run-gates/run-gates.sh:5200`), which the suite's own AC1 arm at line
1517 observes. The untracked file sits outside `ga/`, so `pa`'s key is the lineage run's.

**S5.** AC6 asserts the opt-in mode reuses `pa` and stamps no full green. Its reuse needs an entry
under the env mode's key, and only a bar without `GATE_FULL` writes one. A plain bar between lines
1510 and 1511 earns it on the fixed, clean tree and stamps nothing, because only a full bar stamps.
The ledger still holds one row per leg, so the AC1 row count that follows is unchanged.

**S6.** The shell-hygiene leg flags line 2248 and prints its remedy:
`$(unset GIT_DIR GIT_WORK_TREE; git -C "$sb_t" rev-parse --show-toplevel)`. The line takes it as
printed.

**S7.** The cover pass (`.githooks/pre-push` lines 2034-2079) answers `covered … no bar runs` when a
`gate-bar-green` record graded the pushed tip's tree under the same bar, and `write_bar_green` at
line 2285 writes one after every green non-stub bar. Arm 25's push and the VR control's push each land
a green and record their tree. Every push after them in the same fixture is an `--allow-empty` commit
on that tree, so it is covered. It prints no `gate on main push` line, runs no bar and exits 0. The
standalone log shows the VR arms' output reading `covered on main push … gate-bar-green … no bar runs`.
25b's own output is not in the log, because the arm keeps one grep line, so its cause is inferred from
the same mechanism. 25b's second commit and the commit in `run_vr_push` each write a file whose content
no earlier commit in the fixture held, such as a counter the helper increments. Arms 26 to 29b are
refused before the cover pass or run under the declared stub, which skips it, so they are unaffected.

**S8.** `run_rp_push` sets `remote` from its first argument and then pushes to `origin`
(`.githooks/pre-push.test.sh:973`), as TOOL-aSparedSpawn-13 wrote it. So AC12's push reaches the
populated origin, and the hook offers reuse at origin's tip, which the standalone log shows. The
probe asks the URL git hands the hook (`.githooks/pre-push:2095`). Pushed to `second`, an empty bare
remote, it finds no default-branch tip and offers nothing.

**S9.** Since TOOL-aSparedSpawn-13 a scoped decision runs one `ls-remote --heads` reuse probe
(`.githooks/pre-push` line 2098). PM AC3's decision is scoped, so its count of every `ls-remote` sees
the probe. The post-merge red reads `refs/gov/bar-red` and nothing else (lines 1927 and 1933), so the
arm counts the shim lines that carry both `ls-remote` and `refs/gov/bar-red`.

### Files touched (estimate)

- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- S4 keeping the env-mode control with a plain earning bar before it: the control then proves the
  env key is stable, never that the lineage key matched, and AC3's refusal stays vacuous.
- S4 planting cache entries with `seed_cache_ok`: the entries would carry the lineage run's own key,
  so the control would pass whatever the key held.
- S7 deleting the `gate-bar-green` records before each push: it leaves the shared copies and any
  later tree-keyed record to catch the next arm, where a fresh tree misses every record by construction.
- S9 counting every `ls-remote` and expecting one: the count then depends on whether the decision is
  scoped, which is not what AC3 asks.

## 5. Acceptance criteria

- **AC1** — When the S2 sed program is applied to `tools/run-gates/run-gates.sh` alone and the result
  compared with `diff`, `grep -c '^>'` reads 6. The strip loop reads `while false; do`, and the guard
  pattern matches neither `https://u:p@host/x` nor a text holding a CRLF. Red when: either sed matches
  nothing again and the count reads 4.
  figure: PINNED at 6, one variant per criterion the arm names.
- **AC2** — When `grep -n 'gate-logs' tools/run-gates/run-gates.evidence.test.sh` runs, a removal of
  `$SB_T/.git/gate-logs` sits between the per-leg bar's line and the broken bar's line. Red when: the
  per-leg bar's `sp____x_y.log` reaches `broken.logs` and AC3's existence test finds it.
- **AC3** — When `grep -n -A3 'REUSE_SCHEMA=staged/' tools/run-gates/run-gates.evidence.test.sh` runs,
  a commit inside `$RU_T` follows the `sed -i` before the first reuse bar. Red when: the miss bar runs
  on a dirty tree, writes no entry, and the control reads no reuse.
- **AC4** — When `awk '/^check_lin_control/,/^}/' tools/run-gates/run-gates.evidence.test.sh` runs,
  the body runs no bar and compares field 4 of the `pa` row in `$tmp/ru.led` with `read_ru_key pa`.
  `grep -n -B5 'AC3 lineage reuses nothing' tools/run-gates/run-gates.evidence.test.sh` shows the AC3
  earning bar run over an untracked file that is removed before `write_lin_fix`. Red when: the control reuses through
  the env mode, whose key lacks the `GATE_FULL` term, so it cannot observe the key lineage refused.
- **AC5** — When `grep -n -B4 'AC6 the opt-in mode' tools/run-gates/run-gates.evidence.test.sh` runs,
  a bar without `GATE_FULL` precedes the opt-in bar. Red when: no earning bar runs and the cache holds
  no entry under the env mode's key.
- **AC6** — When `grep -n 'sb_want=' tools/run-gates/run-gates.evidence.test.sh` runs, the
  `--show-toplevel` probe sits first in a substitution opening `(unset GIT_DIR GIT_WORK_TREE;`.
  Red when: the probe is asked bare and the location-probe leg names the line.
- **AC7** — When `grep -n 'allow-empty' .githooks/pre-push.test.sh` runs, neither 25b's second
  commit nor `run_vr_push` commits an empty tree. Red when: a push carries a tree an earlier green
  push recorded, the hook answers covered, and no bar runs.
- **AC8** — When `awk '/^run_rp_push/,/^}/' .githooks/pre-push.test.sh` runs, the push names
  `"$remote"`. In a scratch directory, `git ls-remote --heads` against a fresh `git init --bare`
  prints nothing, which is the premise of AC12. Red when: the helper pushes to `origin` whatever it is
  handed, and AC12's probe answers with origin's tip.
- **AC9** — When `grep -n 'ls-remote' .githooks/pre-push` runs, both post-merge reads name
  `refs/gov/bar-red` and the reuse probe does not. `grep -n -A4 '^# AC3 — undeclared' .githooks/pre-push.test.sh`
  shows PM AC3 counting only shim lines naming `refs/gov/bar-red`. Red when: the arm counts every
  `ls-remote` and the scoped decision's reuse probe reds it.

## 6. Gates

`run-gates evidence` · `pre-push self-test` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)`

Both suites run alone at the close, serially, so a red there is this unit's and not contention.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 · restore either old sed anchor and S2 reds at 5 of six; remove the gate-logs clear and AC3 reds · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC3 · drop the commit after the schema `sed -i` and the AC5 control reds reusing nothing · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC4 · export one extra `GATE_` variable on the lineage bar alone and each lineage control reds on unequal keys · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC5 · drop the earning bar before the opt-in bar and AC6 reds · none
New arm: .githooks/pre-push.test.sh · covers AC7 AC8 AC9 · make 25b's or `run_vr_push`'s commit empty again and 25b, VR AC15 and VR F8 red on a covered push; push AC12 to origin and it reds with a knob; count every `ls-remote` in PM AC3 and it reds on the reuse probe · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft from the build brief and the standalone logs, every cause re-read
  at `53b25884`.
- rev-2 · 2026-10-13 · AC6 rewrapped so its failure mode reads `Red when:` on one line, which check 12 parses; a main-loop edit by the owner's leave, since no spec-writer role renders until aOrientedCast lands.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "re-arm a suite arm a landing disarmed so its staged break reds
again"` returned name-stem neighbours only, such as `arm`, `armed` and `run_arms`, so no existing seam
fits as a helper and this unit mints none. The seams it extends are already in the two suites:
`read_ru_key` at `tools/run-gates/run-gates.evidence.test.sh:978` answers the lineage run's key, the
ledger's field 4 answers the row's, the shell-hygiene leg's printed remedy answers S6, and `seed_cache_ok`
was weighed and rejected in §4. The recall probe returned the TOOL-aFrugalTurnstile-2 brief that
introduced the cover pass and its candidate order, and the TOOL-aSparedSpawn-32 spec that put the reuse
probe after the cover pass and the post-merge red. Those are the two moves S7 and S9 answer. The brief
and the code disagree in one place: the brief traces evidence AC3 to the two stale seds, and the code
traces it to the per-leg bar's logs, which S2 answers.

Recall terms used: `python tools/memory-recall/query.py "why did suite arms go red after landings
merged without a bar, and which fixture or helper re-arms them" --terms "bar-less landing stale
fixture arm disarmed probe marker WHOLE_RUN cover pass gate-bar-green reuse digest GATE_FULL key"`
