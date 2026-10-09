# TOOL-aLevelledCopy-8 — the ssh arm's failure states each get a verdict and an arm

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 4 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aLevelledCopy-8-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aLevelledCopy-8-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md) | journal | TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-9 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 1 (`2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md`)
confirmed six minor findings against the ssh arm of `tools/check-wiring.sh` that TOOL-aLevelledCopy-2
built. Each is a failure state that today either reads as success, carries a misleading cause, or has
no arm that can fail. This unit is the build method's M4 batch for them: M3 with L1 (ids 16, 5 and
10), M4 (id 6), M5 (id 7), M7 (id 13) and L2 (id 14). Every state gets a verdict line and a gate arm
whose failing case is observed.

## 2. Scope (IN)

- **S1 — a config write that fails is `UNWIRED`, on every set-when-unset arm (M3, L1).** The four
  arms that run `git config <key> <value>` when the key is unset gain the branch they lack. A write
  that exits non-zero prints `UNWIRED  <arm> — could not set <key> (local). Fix: git config <key>
  '<value>'`, increments `unwired`, and logs no health event. The four are `check_ssh_keepalive`
  (`core.sshCommand`), `check_hooks` (`core.hooksPath`), `check_merge_rows` (`merge.rows.driver`) and
  `check_merge_ours` (`merge.ours.driver`), which today writes with `&&` and has no if-block at all.
  §8 F2 records why the class and not only the two named arms. Observed by AC1, AC2, AC3.
- **S2 — set or unset is decided by the exit status of a plain read (M4).** `check_ssh_keepalive`
  reads `git config --get core.sshCommand` and keeps its status. Status 0 is set, status 1 is unset,
  and any other status prints `note     ssh       — cannot read core.sshCommand (git config exited
  <n>); NOT setting it` and returns, writing nothing and counting nothing. `--show-scope` is spawned
  only after a status of 0, only to label the line, and a failure there labels it `scope unread`
  instead of changing the branch. Observed by AC4, AC5.
- **S3 — the `n=0` derivation line names kit skew (M5).** When `push-main.sh` carries no
  `GOV_SSH_KEEPALIVE=` line, the existing `UNWIRED  ssh       — cannot derive the keepalive from
  <path>` prefix is kept byte-for-byte, so TOOL-aLevelledCopy-2's AC6 arm still matches, and the
  rest of the line says that this `push-main.sh` predates the definition line or has lost it, and
  that the fix is updating the push-main kit. It stays `UNWIRED`, as TOOL-aLevelledCopy-2 AC6
  requires. The two-or-more case and the malformed one-line case keep today's text. Observed by AC6.
- **S4 — the shipped self-test skips LC2 for kit skew only outside gov (M5).** The LC2 block of
  `tools/check-wiring.test.sh` keeps its `push-main.sh is not installed` skip, and gains one more:
  when the repository carries an install receipt AND the installed `push-main.sh` holds zero
  `GOV_SSH_KEEPALIVE=` lines, it prints `skip LC2 arms — the installed push-main.sh predates
  GOV_SSH_KEEPALIVE (kit skew); check-wiring --check reports it UNWIRED with the remedy` and runs no
  LC2 arm. gov's own tree carries no receipt, so there a missing line still reds the arms. Observed
  by AC7.
- **S5 — the edge is declared where govkit grades it (M5).** `tools/govkit/entries/check-wiring.kit.toml`
  gains `requires_if = [{ kit = "push-main", why = "..." }]`, with no condition key, stating that the
  ssh arm derives `core.sshCommand` from push-main's definition line and degrades to `skip` where
  push-main is absent and to a named `UNWIRED` where it predates the line. It installs nothing and
  orders nothing: `govkit selfcheck` check 7 is its only reader, and it grades the kit name. Observed
  by AC8.
- **S6 — "read with sed, never sourced" gets an arm that can fail (M7).** An LC2 arm seeds the
  fixture's `push-main.sh` definition line with a command substitution that would create a marker
  file if evaluated. Observed by AC9.
- **S7 — the classifier's untested branches get arms (L2).** An LC2 arm for a drive-path remote and
  one for an `ssh://` remote. Observed by AC10.
- **S8 — every new arm's failing case is staged and observed.** Each arm of S1 to S7 in
  `tools/check-wiring.test.sh` reports `ok` against the built checker and `FAIL` against a scratch
  copy carrying its break. Observed by AC11.

## 3. Non-goals (OUT)

- **The operator's choice of SSH program.** `GIT_SSH`, `GIT_SSH_VARIANT` and `ssh.variant` are
  TOOL-aLevelledCopy-7's (H1, M1). This unit edits the branches after that gate and never the gate.
- **govkit holding or widening an update for this pair.** Neither `derive_marker_coupling` nor
  `update`'s hold logic changes here; §8 F1 records why. A general kit-graph check that flags a kit
  file reading a literal out of another kit's file without a declared edge is the review's broader
  left-shift, and it is the §3 Edges hand-off.
- **The other swallowed reads in `check-wiring.sh`.** §4 lists them. Only the ssh arm's read is this
  unit's to change.
- **`push-main.sh`.** No byte of it changes. Its definition line and its precedence are
  TOOL-aLevelledCopy-2's, and that spec's §3 hand-off still stands.
- **Kit-version bumps.** One bump per touched kit happens once, after the last unit.

### Edges

- **consumes-from** `TOOL-aLevelledCopy-7` — the operator-choice gate that sits before the set and
  `UNWIRED` branches this unit edits; every ssh fixture here runs with `GIT_SSH` and `GIT_SSH_VARIANT`
  unset and no `ssh.variant`, so that gate stands aside, and `seed_ssh_fixture` is taken as that
  unit leaves it.
- **hands-off** external — a govkit check that a kit file reading a literal out of another kit's
  file declares an edge to it, and any `update` coupling that makes the two move together; filed as
  an ask at the close, because it changes the update behaviour the runbook describes.

## 4. Design

### The failed-write branch (S1)

Each of the four writes becomes the same if-block. The `FIXED` line and the `add_health_event` call
stay inside the success branch, so a failed write logs nothing. The else branch prints the
`UNWIRED` line and increments `unwired`. Under `--fix` the script then exits 1. Under `--session` it
still exits 0, as its contract says, and the line is the record. The value in the `Fix:` text is the
one the arm tried to write: `$want` for ssh and merge.rows, `.githooks` for hooks, `true` for
merge.ours.

### The read (S2)

```bash
cur=$(git config --get core.sshCommand 2>/dev/null); rc=$?
case $rc in
  0) scope=$(git config --show-scope --get core.sshCommand 2>/dev/null) && scope=${scope%%$'\t'*} \
       || scope="scope unread" ;;
  1) ;;   # unset at every scope: the set / UNWIRED branch
  *) echo "note     ssh       — cannot read core.sshCommand (git config exited $rc); NOT setting it"
     return ;;
esac
```

`git config --get` returns the last value when several scopes set the key, with status 0, so the set
branch keeps today's last-one-wins reading. A trailing CR is trimmed from `cur` as today. The spawn
count is unchanged on the unset path and gains one on the set path, about 0.75 s on node a (PINNED,
the memory note "A git spawn costs 751ms", measured 2026-10-02).

### The swallowed reads in `check-wiring.sh` (M4's grep)

`git grep -n '2>/dev/null || true)' tools/check-wiring.sh` at this unit's authoring found six. Four
feed a write decision. The ssh read is this unit's (S2). The other three are LEFT: each reads with
plain `git config <key>`, whose only failure besides status 1 is an unreadable config file, and a
write to that same file then fails too, which S1 now reports.

| Read | Feeds | Disposition |
|---|---|---|
| `check_hooks`, `core.hooksPath` | set when unset | LEFT; S1 reports its failed write |
| `check_merge_rows`, `merge.rows.driver` | set when unset | LEFT; S1 reports its failed write |
| `check_merge_ours`, `merge.ours.driver` | set when unset | LEFT; S1 reports its failed write |
| `check_ssh_keepalive`, `core.sshCommand` | set when unset | S2 |
| the hook-dir `rev-parse --abbrev-ref HEAD` | a `note` label | no write |
| the straggler arm's per-worktree `core.hooksPath` | a mark in a report | no write |

### The self-test discriminator (S4)

"Outside gov" is read as "this repository carries `.governance/install.json`", the same file
`resolve_receipt_path` treats as the install receipt. gov's own tree carries a `.governance/` folder
with a deploy descriptor and no receipt, which the script header already relies on ("A tree with no
receipt — gov's own — resolves exactly as the probes always did"). The count uses the same
`grep -c '^GOV_SSH_KEEPALIVE='` the checker uses, so the suite and the arm cannot disagree on what
"has the line" means.

### The git shadow (S2's arms)

AC4 and AC5 put a directory first on `PATH` holding an executable named `git`, written by the arm
with `printf`, that exits with the arm's status when its argv matches and otherwise runs the real
git, whose path is captured with `command -v git` before `PATH` changes. A shell function exported
with `export -f` was rejected, because the lexicon leg grades every function definition in the
suite and `git` is not a verb in the declared table.

### Inventory

This unit mints no function, variable, health-event token or file name. If the builder needs a
fixture helper in the suite, it asks `python tools/lexicon/lexicon.py --suggest <name> --as
sh.function` before naming it and records the answer in the revision log.

### Files touched (estimate)

- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `tools/govkit/entries/check-wiring.kit.toml`

### Rollout

TOOL-aLevelledCopy-7 writes `check-wiring.sh` and its suite first, which is why this unit is
`order 4`. TOOL-aLevelledCopy-9 writes `tools/govkit/govkit.py` and `tools/govkit/selftest.py` at
`order 3`; this unit writes neither, and its one govkit-directory file is a descriptor nothing in
TOOL-aLevelledCopy-9's write set reads as a contract. The adopters take all of it with a normal
`govkit update`. inCMS's push-main already carries the definition line, so S3 and S4 change nothing
there unless it updates check-wiring alone.

### Alternatives rejected

- **`requires = ["push-main"]` on check-wiring (the brief's option a).** It cannot close M5:
  `derive_unsatisfied_requires` tests that the dependency is INSTALLED, and the skew case has an
  older push-main installed, so the edge is satisfied and the red stays. It would also make `apply`
  refuse every check-wiring selection without the lander, which the arm does not need because it
  already skips there.
- **govkit holds check-wiring whenever push-main is held or out of scope (option b).** It writes
  `update`'s scope and hold logic and would name two kits inside govkit, which the kit-literal ban
  forbids, or needs a new descriptor field to say it. Either way the runbook's account of how
  `update` widens a scope (`WIRE-INTO-PROJECT.md`, block 1's scope paragraph) goes stale, and that
  runbook is a governance carrier M3 veto 2 keeps from a delegated run.
- **`derive_marker_coupling` as it stands (option c).** It couples two kits when one ships a file
  carrying the other's `gov:kit` version marker. push-main has no version constant
  (`version_from = { none = ... }`), so there is no marker to carry, and declaring one false
  carrier would red selfcheck's marker-parity arm. Extending it to a second edge kind is option b's
  descriptor field.
- **Downgrading `n=0` to `note` (the finder's fix).** The skeptic judged it UNSOUND: a definition
  line lost in gov would then pass.
- **A shell function shadowing `git`.** Graded by the lexicon leg (§4, the git shadow).

## 5. Production-readiness checklist

- security — S6 adds a guard on the trust boundary TOOL-aLevelledCopy-2 §5 states: the definition
  line is read with `sed` and never evaluated. S1 and S2 only narrow when a write happens. No new
  write path.
- perf / scale — one extra `git config` spawn on the ssh arm's set path (§4); none elsewhere.
- error / empty / loading states — a failed write is `UNWIRED`; an unreadable key is `note`; a lost
  definition line is `UNWIRED` naming kit skew; a failed scope read is labelled `scope unread`.
- observability — every state above prints one line naming its arm and key; a failed write logs no
  health event, so the orientation card's counter never counts a write that did not happen.
- risks — an adopter that copied kits by hand carries no receipt, so its self-test runs LC2 against
  a skewed push-main and reds; that red is loud and its `--check` line names the remedy.
- testing — S8's arms, each failing case staged (AC11).
- migration — none; no config key, file or receipt field changes shape.
- user docs — `check-wiring.sh`'s header names no failure states today and gains none; the
  `requires_if` row's `why` is the descriptor's own documentation.

## 6. Acceptance criteria

Every fixture below is a git repository under a short `%TEMP%` directory, built by the suite's
`newrepo` or `seed_ssh_fixture`, with `GIT_CONFIG_GLOBAL` pointed at a file of the fixture's own and
`GIT_CONFIG_NOSYSTEM=1`, so node a's own config cannot decide a criterion. `GIT_SSH`,
`GIT_SSH_VARIANT` and `GIT_SSH_COMMAND` are unset and no `ssh.variant` is set. The ssh remote is
git@example.invalid:o/r.git unless a criterion says otherwise; nothing is contacted. "The lock" is an
empty config.lock file created beside the fixture's own config inside its git dir, which makes every
`git config` write fail with "could not lock config file" on every OS, where `chmod` is unreliable
on MSYS.

- **AC1** — When `bash tools/check-wiring.sh --fix` runs in an ssh fixture with `core.sshCommand`
  unset and the lock held, it prints `UNWIRED  ssh       — could not set core.sshCommand` and exits
  1, the common dir's `health.log` holds no `sshcommand-set` line, and after the lock is released
  `git config core.sshCommand` prints nothing; under `--session` the same line prints and the exit
  is 0. Red when: `--fix` exits 0, or no `ssh` line prints, or an event is logged.
- **AC2** — When `bash tools/check-wiring.sh --fix` runs in a `newrepo` fixture with
  `core.hooksPath` unset and the lock held, it prints `UNWIRED  hooks     — could not set
  core.hooksPath`, exits 1, and logs no `hookspath-set` line. Red when: it exits 0 or prints
  `FIXED    hooks`.
- **AC3** — When `bash tools/check-wiring.sh --fix` runs with the lock held, once in a fixture
  tracking a `.gitattributes` that declares `merge=ours` on one path, and once in the merge.rows
  fixture at the suite's state 4 (declared, driver unset), it prints `UNWIRED  merge     — could not
  set merge.ours.driver` and `UNWIRED  merge     — could not set merge.rows.driver` respectively,
  each run exiting 1, and the merge.rows run logs no `merge-driver-set` line. Red when: either run
  exits 0 with no `merge` line.
  fixture: the merge.rows half needs the suite's `install_driver`, which needs the memory-tree,
  memory-recall and lib kits beside the suite; gov's tree holds all three today.
- **AC4** — When a fixture's global file sets `core.sshCommand` to `ssh -i ~/.ssh/id_test`, a `git`
  shim first on `PATH` exits 129 on any argv carrying `--show-scope`, and `bash
  tools/check-wiring.sh --session` runs, `git config --local core.sshCommand` prints nothing and the
  run prints `note     ssh       — core.sshCommand is the operator's (scope unread)`. Red when: a
  local value appears, which is today's behaviour.
- **AC5** — When the shim instead exits 3 on `config --get core.sshCommand` and `bash
  tools/check-wiring.sh --check` runs on an unset ssh fixture, its `ssh` line is `note     ssh
  — cannot read core.sshCommand` and no `UNWIRED  ssh` line prints, and `--session` then leaves
  `git config core.sshCommand` empty. Red when: the run prints `UNWIRED  ssh` or a value is written.
- **AC6** — When the fixture's `push-main.sh` copy holds no `GOV_SSH_KEEPALIVE=` line and `bash
  tools/check-wiring.sh --check` runs, its `ssh` line begins `UNWIRED  ssh       — cannot derive the
  keepalive from` and names the copy, carries the words `predates` and `update the push-main kit`,
  and the run exits 1. Red when: the line lacks the remedy, or the exit is 0.
- **AC7** — When the suite's prologue, its LC2 guard and the LC2 AC1 block run as a slice from a
  scratch clone of this repository whose `tools/push-main.sh` holds no definition line, the slice
  prints `FAIL LC2 AC1` while the clone carries no install receipt, and prints `skip LC2 arms` naming
  kit skew and no `FAIL` once a receipt holding `{"schema": 3, "files": []}` is written where
  `resolve_receipt_path` looks for one. Red when: gov's
  receipt-less clone skips, or the receipt-carrying one runs the arm.
  fixture: the clone sits under a short `%TEMP%` directory, because a clone under the scratchpad
  hits MAX_PATH; the built checker and suite are copied into it, since a clone carries only HEAD.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs with the new row's `kit` value
  changed to `push-mian` in the working tree, it prints `entry 'check-wiring' requires_if names
  'push-mian', which is not a registry entry`; with the value restored, a second run prints no
  `requires_if` line for `check-wiring`. Red when: the misspelled run is silent, which would mean
  the row is not read.
  cost: up to 310 s a run, the leg's declared ceiling; two runs.
- **AC9** — When the fixture's definition line reads
  `GOV_SSH_KEEPALIVE='ssh'$(touch "$D/ran")` with `$D` expanded at seed time, and `bash
  tools/check-wiring.sh --session` runs, no file named `ran` exists in the fixture, the run prints
  `UNWIRED  ssh       — cannot derive`, and `git config core.sshCommand` prints nothing. Red when:
  the marker file exists, which an `eval` or `source` derivation produces.
- **AC10** — When the fixture's only remote is the drive path C:/x/origin.git and `bash
  tools/check-wiring.sh --session` runs, it prints `skip     ssh       — no remote pushes over ssh`
  and sets nothing; when it is ssh://git@example.invalid/o/r.git, it prints `FIXED    ssh` and
  `git config --local core.sshCommand` equals the derived value. Red when: the drive path is set, or
  the `ssh://` remote skips.
- **AC11** — When each new arm of the kit's own self-test is run ALONE, as that suite's prologue
  plus the one block in a sliced copy inside the kit directory, under `bash <slice>`, it prints `ok`
  against the built checker and `FAIL` against a scratch copy of the checker carrying that arm's
  staged break: the else branch absent (AC1 to AC3); the read restored to `--show-scope ... || true`
  deciding the branch (AC4, AC5); today's `n=0` text (AC6); the `sed` derivation swapped for `eval
  "$(grep '^GOV_SSH_KEEPALIVE=' "$pm")"` (AC9); `${#host} -gt 1` changed to `-gt 0`, and the
  `ssh://` case line absent (AC10). Each break and its `FAIL` line is recorded in the unit's
  acceptance ledger. Red when: an arm prints `ok` against its break.
  cost: about 20 s a slice on node a (the memory note "Slice a suite to debug one arm"); the whole
  suite is not run in this pass.

## 7. Gates

`check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The close runs these once, in the bar. `transition-audit arms` and `straggler-guard arms` are the
legs whose guard names `tools/check-wiring.sh`; the four govkit-directory legs and `recall floor
arms` are owed by the descriptor path. The rest are named by judgment: `tools/` is a broad guard.

New arm: tools/check-wiring.test.sh · covers AC1 AC2 AC3 · the else branch absent in a scratch copy of the checker · none
New arm: tools/check-wiring.test.sh · covers AC4 AC5 · the read restored to the swallowed --show-scope form · none
New arm: tools/check-wiring.test.sh · covers AC6 AC7 · today's n=0 text, and the suite's skew skip run in gov's receipt-less clone · none
New arm: tools/check-wiring.test.sh · covers AC9 · an eval derivation in a scratch copy of the checker · none
New arm: tools/check-wiring.test.sh · covers AC10 · the drive-path rule and the ssh:// case line broken in a scratch copy · none

## 8. Open questions

- **F1 — Which mechanism closes M5, kit skew between check-wiring and push-main?**
  The brief names four. (a) `requires = ["push-main"]`; (b) govkit holds check-wiring with
  push-main; (c) `derive_marker_coupling`; (d) the `n=0` line names kit skew, and the shipped
  self-test skips LC2 only outside gov. A fifth, (e), is (d) plus a `requires_if` row on the
  check-wiring descriptor, the declaration-only edge memory-tree already uses for playbook-render
  (aRepatriatedFork-42's closing review, "why it is not a `requires`"). By M3: (a) fails veto 1,
  because it cannot catch an installed-but-older push-main (§4); (b) and (c) as extended fail veto
  2, because they change `update` behaviour that `WIRE-INTO-PROJECT.md` describes, and (c) as it
  stands cannot express an edge to a kit with no version marker. (d) and (e) survive; (e) states
  more, a graded edge in the kit graph, at the cost of one descriptor line, and leaves fewer
  follow-ups. It writes no file in TOOL-aLevelledCopy-9's write set, so neither unit moves.
  RESOLVED (agent, 2026-10-09, delegated): (e).
- **F2 — Does the failed-write branch cover only the ssh and hookspath arms the review named, or all
  four set-when-unset writes?** (a) The two named; (b) all four, since `check_merge_rows` and
  `check_merge_ours` carry the same no-else shape. (b) is the class the review's own left-shift asks
  for, it stays inside the one file this unit already writes, and no veto applies.
  RESOLVED (agent, 2026-10-09, delegated): (b).

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the closing review's promotion brief.

## 10. Reuse audit

The seams are in `tools/check-wiring.sh` itself. S1's branch copies the read-back-then-`UNWIRED`
shape `check_hook_modes` already prints for a write that did not take. S4 discriminates on the
install receipt the way `resolve_receipt_path` does, and S5 rides the existing `requires_if` row
kind, graded by `govkit selfcheck` check 7, which `tools/memory-tree/kit.toml` already uses for a
declaration-only edge. `python tools/codebase-map/reuse_lookup.py "report a failed git config write
as unwired instead of exiting zero"` ranked only generic name stems (`git`, `write`, `fail`,
`report`) and named no failed-write seam, so no existing seam fits the branch beyond the sibling
arm's shape. The recall probe's hit 5, the aRepatriatedFork-42 closing review, is the precedent F1
takes: a floor govkit cannot express is declared as `requires_if` and enforced by the consumer's own
runtime check.

Recall terms used: check-wiring push-main GOV_SSH_KEEPALIVE marker_carriers requires coupling govkit update kits skew derive
