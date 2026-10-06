# TOOL-aGraftedHelix-36 — the rotated run's closing review MEDIUM and LOW findings, fixed as one batch

**Status:** CLOSED · rev-2 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 20 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-36-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-36-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-prompt-TOOL-aGraftedHelix-35-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-35-1-spec-brief.md) | journal | TOOL-aGraftedHelix-35 |

<!-- /gen:spec-records -->

## 1. Goal

The rotated run's closing diff review, round 1, confirmed nine items below HIGH that are not the
HIGH's own defect: M2 to M7 and L1 to L3. The owner's promote-every-finding ruling makes them one
unit. This unit fixes each item as its section's Fix line states, taking the skeptic's corrected fix
where the record judged the finder's unsound (ids 6, 10, 11 and 14), and left-shifts each as its
Left-shift line states. It runs after unit 35, which holds M1 with the HIGH, and keeps every
mechanism unit 35 builds.

## 2. Scope (IN)

Every item names the review section it answers. The review record is
`memory/builds/aGraftedHelix/reviews/2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md`.

- **S1** — M2, ids 2, 9 and 17. `cmd_for_diff` in `tools/memory-tree/gotchas.py` reads the range's
  touched set with `git diff --no-renames --name-only -z <rng>`, split on NUL, so a renamed
  invariant's source path joins `changed` and `paths`. The base copy of that record is then filtered
  out of the by-design block and itemised as moved. A `--selftest` arm beside the TAKES OUT arm
  `git mv`s an anchored invariant with a small edit and asserts a block of 0 with both names as
  items. Observed by AC1.
- **S2** — M2's second left-shift. The documented check of
  `memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md` runs over every
  `diff --name-only` read this build added, unit 35's included, and each is classified as a
  prefix-matched touched set, a "did anything change" read, or an equality assertion in a suite. The
  record gains the gotchas instance under its `## Where it bit` section. Observed by AC2.
- **S3** — M3, id 7. `tools/workflows/unattended-build.template.js` refuses a declared `specAudit`
  beside a `base` that is not 7 to 40 lowercase hex, before any agent spawns, naming where the value
  comes from. The working-tree `WARNING` the audit resolver logs when no pinned base was passed is
  deleted, since no call can reach it. The harness header marks `base` as required beside
  `specAudit`. The unattended skill's harness-call paragraph tells every call to carry
  `base: <the run's pinned base fact>` beside `scratch`, audit on or off, and the rendered skill is
  re-adopted. The suite's audit-route fixtures gain a 40-hex `base`, and the GH29 no-base arms
  become refusal arms. Observed by AC3 and AC4.
  **Readers:** by name: `tools/workflows/unattended-build.test.sh` spells the deleted line as
  `GH29_WT`. by value: `tools/workflows/unattended-build.test.sh`, whose GH29 `has` and `hasnt_`
  arms compare the logged text.
- **S4** — M4, ids 8 and 19, adopted as this unit's mechanism rather than parked. The settle's claim
  status write moves into one function, `write_settle_claim`, called by the settle that writes the
  record and by the already-settled exit. On that exit it writes the status only when the slug's
  claim still reads `held` or `live` and is `mine` under the record's own keepalive and session. A
  first write that does not complete prints the remedy, a re-run of `--settle <slug>`. The
  already-settled line says the record was not rewritten, and the verbs and stops guides say the
  re-run retries the claim. Observed by AC5 and AC6.
- **S5** — M4's documented check. The class record
  `memory/gotchas/orchestrator-hand-off-owed-a-disposition.md` is applied to every spec of this
  build. Each line handing work to the orchestrator, to "this run" or to its close resolves to a
  unit in the roster or a parked row. Unit 34's hand-off to the close is the one line resolving to
  neither, so this unit records it with `--park`. Observed by AC7.
- **S6** — M5, id 10, the skeptic's corrected fix. In `check_skill_install` of `tools/check-wiring.sh`
  the linked-worktree `note` also requires every file in `$bad` to differ between HEAD and its merge
  base with the clone's one remote's `HEAD`. Where any file fails that, or no such tip resolves, the
  arm reports UNWIRED as at base. When the install matches the primary checkout, that UNWIRED line's
  remedy is to fast-forward the primary checkout, not to re-link. The header's WHAT THIS DOES NOT
  CHECK line says what the note now proves. Observed by AC8 and AC9.
- **S7** — M6, ids 11 and 14, the skeptics' corrected fix. The commit pass of
  `tools/workflows/check-workflow-syntax.js` skips lines whose trimmed text opens `//` or `*`, and
  grades every other line matching `\bgit(\s+-[cC]\s+\S+)*\s+commit(?![-\w])` anywhere on it. It
  prints `graded <n> git commit line(s)` beside its green line. In discovery mode a zero count while
  the population holds a file named `unattended-build.js` exits 1 as a dead probe, and any other zero
  is printed as an announced count. The header names the forms the pass still does not check, and
  the README's checker-table row names the second pass. Observed by AC10, AC11 and AC12.
- **S8** — M6's left-shift. The build-harness suite gains fixture arms for a comment line, a
  `git -C` line, a mid-literal `set -e; git commit` line and a `git commit-tree` line, and one arm
  running the checker in discovery mode over the real tree with a floor of one graded line.
  Observed by AC10 and AC11.
- **S9** — M7, id 15. The extracted-`run_bounded` harness of the driver suite gains one arm whose
  `write_proc_record` stub records whether the exec marker existed when the record ran, and asserts
  `up`. `FLOOR_SHARD_2` and `FLOOR_ASSERTIONS` rise by one. Observed by AC13.
- **S10** — L1, id 6, the skeptic's corrected fix. `write_claim` in `tools/unattended/unattended.sh`
  takes the lock directory `claim-push.lock` in its git dir BEFORE it tests `push-main-active`,
  writes its deadline into the lock, holds it across the push and releases it on every path. A lock
  whose deadline has passed is cleared and taken once. `tools/push-main.sh` touches its marker, waits
  through `check_claim_push_clear` for no live lock, then clears the verdict files and pushes, and
  clears its marker only after `write_lander_marker` or `derive_push_failure` has read them. The
  "One writer per verdict file" comment and the class record's instance are corrected. Observed by
  AC14, AC15 and AC16.
- **S11** — L2, id 16. Each of the nine re-cut seam lines of the kit-gate suite calls
  `read_topo s<k>` after `anchor_restore`, `s1` to `s9` in file order, and the header says how the
  seams restore refs. A prologue helper, `check_helpers_hoisted`, and one prologue arm calling it,
  fail naming any column-0 function definition between the first `if in_shard` line and the
  `FLOOR_ASSERTIONS` line, and refuse as a dead probe when they read no region. Observed by AC17 and
  AC18.
- **S12** — L3, id 20. The README roster row for unit 34 states the mechanism unit 34 built.
  Observed by AC19.
- **S13** — The bookkeeping the fixes owe. Each of the four kits whose shipped bytes move bumps once,
  after this unit's last move in it: `memory-tree`, `review-harness` with the harness's
  `unattended-build@` engine identity and its suite pin, `unattended` and `check-wiring`. The
  harness and the skill are re-rendered, the unattended guides re-adopted, `gotchas.py --write`
  re-renders the catalogue index, the two dossiers whose prose names a moved mechanism are
  refreshed, and the kickoff manifest is re-stamped. Observed by AC20 and AC21.
- **S14** — Adopted from unit 35's discovery. Two carriers say `gotchas.py --for-diff` always exits
  0, false since unit 29, which made it exit 1 with a `HYGIENE gotchas:` line on a refused range, as
  the memory-tree README states: the build method's M6 sentence in
  `tools/memory-tree/BUILD-METHOD.template.md`, and the per-pass checklist paragraph of
  `tools/unattended/SKILL.template.md`. Each sentence says instead that it exits 0 whenever it
  prints a checklist and 1 with a `HYGIENE gotchas:` line on a refusal. The build method is a
  governance carrier shared invariant 10 closes; this edit takes that invariant's one exception,
  because the shipped contract would otherwise state false behaviour, and it changes the claim about
  an exit status and no rule. Both are re-rendered. Observed by AC22.

## 3. Non-goals (OUT)

- **No HIGH item, and not M1.** Unit 35 closes H1 and M1 at the union and at the spec commit's
  checker. This unit edits neither `renderChecklistUnion` nor `SPEC_COMMIT_CHECKLIST` nor unit 35's
  audit-OFF warning, and keeps every assertion unit 35's GH15 and GH35 arms make.
- **No refusal on the audit-OFF route.** A call with no `specAudit` and no `base` still runs, and
  unit 35's warning says its hand-out was read unpinned.
- **No `--base` option on `--for-diff`.** S1 changes the touched-set read and nothing else.
- **No new gate leg.** S7 rides `workflow script syntax`, and every arm lives in a suite that already
  exists. Shared invariant 5.
- **No change to the claim write table.** No row, mode or class of `CLAIM_READS` or `CLAIM_MODES`
  moves, and S4 calls the `status` column as the settle does today.
- **No change to the pre-push hook.** The verdict files keep their writer and their format. S10
  changes only when a claim push and a landing push may run.
- **No env override for the lander's wait.** Its bound is the deadline the claim writer records, and
  its ceiling is a file constant.
- **`dispatch.args.checklist` and the per-pass `--for-diff HEAD~1..HEAD` keep their form.** Unit 35
  §3 says why, and the touched-set fix of S1 reaches them through `gotchas.py`.
- **No class gate for orchestrator hand-offs.** The class record measured why no predicate separates
  them; S5 runs the documented check instead.
- **The roster-row class stays a documented check.** BUILD-METHOD M8 already owes a re-read of the
  build README against the code at the close. This unit edits the method at M6's exit-status
  sentence alone (S14), under shared invariant 10's false-behaviour exception, and adds no rule.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-35` — the shipped caller passing the run's pinned base, which
  that unit hands here: S3's skill sentence and refusal make its pinned spec-commit checker the
  route every audit takes, and AC3 reads that checker's command off the commit prompt. This unit
  edits the build harness and its suite after that unit's build, so its union, its constant and its
  arms are inputs here.

## 4. Design

### Evidence

Read at `45ce8c76`, the run branch's tip, which carries the review record. The build-harness lines
below move when unit 35 builds; this unit re-derives each at its pass's base.

- `tools/memory-tree/gotchas.py:705` reads `changed` with `git diff --name-only <rng>`, passing it as
  both `paths` and `changed`. The block filter is at `:625`. The TAKES OUT arm is at `:1087`.
- `tools/workflows/unattended-build.template.js:280` reads `base`, `:166` lists it unmarked in the
  header, `:460` derives `auditBase`, `:1242` forwards it to the resolver, and `:1259-1263` logs the
  working-tree `WARNING`. The suite's `GH29_WT` at `:1503` and its arms at `:1506-1522` pin that
  warning. Twenty-three lines of the suite spell the fixture literal `"specAudit":"2026-09-20"`, some
  of them `sed` patterns that strip it, and no fixture carries `base` except through
  `build_gh29_args`.
- `tools/unattended/SKILL.template.md:716` makes `scratch` required and never names `base`.
- `tools/unattended/unattended.sh:5938` is `run_settle`. Its already-settled exit is `:5950`, and the
  status write is `:6047-6051`. `check_claim_writable` is `:1963`, and `write_claim` is `:2060`, with
  the marker test at `:2073` and the comment ending "One writer per verdict file" at `:2053`. The
  `run_bounded` wait is `:263`.
- `tools/unattended/unattended.test.sh:7402` stubs `write_proc_record` in the extracted harness.
  `FLOOR_ASSERTIONS` is `:15679` and `FLOOR_SHARD_2` is `:15828`. The GH31 settle arms end at
  `:9401`, and the GH32 AC6 marker arm is `:14341-14353`, both in region two.
- `tools/check-wiring.sh:1239` opens the `note` branch, with the install-versus-primary loop at
  `:1229-1233`.
- `tools/workflows/check-workflow-syntax.js:39` is `COMMIT_LITERAL`, and the pass is `:94-99`.
  `tools/workflows/README.md:9` is the checker-table row.
- `tools/push-main.sh:515-525` is `--land`'s clear, touch, push and marker clear, and `:616-624` the
  attended path's. The trap at `:142` clears the marker on exit.
- `tools/unattended/check-unattended.test.sh:48` says refs are carried by `read_topo` at every
  boundary. The nine seams sit at `:4181`, `:4544`, `:4700`, `:4864`, `:5081`, `:5395`, `:5513`,
  `:5860` and `:6115`.
- `memory/builds/aGraftedHelix/README.md:99` is unit 34's roster row.

### Probes run while speccing, all on node `a`, 2026-10-06, read-only

- **S2's sweep.** Every `diff ... --name-only` line the build's own commits added, from
  `git log --no-merges --grep=aGraftedHelix 5266d22e..HEAD`: one prefix-matched touched set, the M2
  instance at `gotchas.py:705`; one "did anything change" read, the spec commit block's
  `changed=$(git diff --name-only -- "$root" ...)`, which reads index against work tree and refuses
  on any line, so a rename still surfaces as a change; one walk that already passes `--no-renames`,
  `row_grammar.py`'s gotcha replay; and fifteen equality assertions in suites, which compare a whole
  listing. Unit 35 adds `git diff --no-renames --name-only HEAD~1..HEAD`, which its own header
  declares unsplit on spaces. PINNED, measured at `45ce8c76`; AC2 re-derives it.
- **S5's sweep.** Four lines across the build's specs hand work to the orchestrator, this run or its
  close: unit 27's, parked at `2026-10-05T20:21:42Z`; unit 29's, the M3 this unit builds; unit 31's,
  the M4 this unit builds; and unit 34's hand-off of the pooled calibration and the eight-shard
  identity to the close, which has neither. Unit 35's lone hand-off names this unit.
- **S6 on this worktree.** The installed engine is a link to the primary checkout, and only
  `manifest-check.sh` differs from this worktree's tracked copy. `git diff --quiet` from the merge
  base with `refs/remotes/origin/HEAD` reads it as this branch's own edit, and `SKILL.md` and
  `MANIFEST-TEMPLATE.md` are untouched and equal. So the corrected arm keeps today's `note` here and
  does not wedge this run's own `--check`.
- **S7's predicate over the real tree.** Six scripts declare workflow meta. The corrected predicate
  grades one line, `unattended-build.js:1002`, the spec commit's `git commit --only ... -- <paths>`,
  as the old one did. Near-misses that carry `git` and `commit` and stay ungraded: three
  `rev-parse ...^{commit}` and log prompt lines in `tier2-review.js`, two comment lines and one
  prose line in `unattended-build.js`.
- **S11's predicate.** Over the shipped suite it finds 0 column-0 definitions inside the regions.
  Over the same file at `7dd6b08ec^`, before unit 34's hoist, it finds 31. Its indented near-misses
  number 33, every one a `mutate` or `printf` string, which a column-0 anchor correctly ignores.

### S1 — the touched set names both sides of a rename

```python
out = run("git", "diff", "--no-renames", "--name-only", "-z", rng, cwd=root)
changed = [p for p in out.split("\0") if p]
```

The source path of a rename is now in `paths` too. `normalise_paths` passes it through,
`selectable` excludes the memory root, and `derive_moved_invariants` itemises it from the base's
text through its own-path clause, so the moved invariant is named once per side. The `--selftest`
arm builds on the existing `bd` fixture: a commit `git mv`s `inv-one.md` to `inv-two.md`, edits its
`## Actually`, and edits the anchored gate. It asserts `extract_block` returns the 0 head alone and
that both `inv-one` and `inv-two` print as `NEW/CHANGED invariant` items.

### S3 — a declared audit carries its base

After the `specAudit` derivation, where the other impossible pairings refuse:

```js
if (specAudit && !/^[0-9a-f]{7,40}$/.test(base)) {
  throw new Error('unattended-build: `specAudit` is declared beside no pinned `base` (got ' +
    JSON.stringify(a.base) + '). The audit reads its by-design block at that base, and read at none ' +
    'an invariant this build added stands as by design on its own audit. Pass the run-state file\'s ' +
    '`base` fact under a mandate, else the sha the build branched from.')
}
```

`auditBase` keeps its name and its test, because unit 35's spec commit stage reads it on the
audit-OFF route too. The resolver's `if (!auditBase)` branch can no longer run beside a declared
audit, so it is deleted rather than left dead.

The skill's paragraph gains one sentence after the `scratch` one: every call carries
`base: <the run's pinned base fact>`, which pins the audit's checklist and, through unit 35, the
spec commit's, and the harness refuses a declared audit without it.

Every suite fixture carrying `"specAudit":"2026-09-20"` gains `"base":"<40-hex>"` beside it, one
fixed value. Each arm then re-reads its expected text, since the resolver prompt gains `--base` and
unit 35's step-6 command takes its pinned form. The GH29 no-base and `origin/main` arms assert the
throw and its message, and the pinned GH29 arm keeps its assertions.

### S4 — the settle's claim write, once, with a retry

```sh
write_settle_claim() { # slug · run-state file · status to write · first|retry
  local slug="$1" rel="$2" st="$3" when="$4" _sk
  [ -n "$st" ] && [ "$RUN_CLAIMS" = on ] || return 0
  read_claims soft || return 0
  _sk=$(fact "$rel" keepalive)
  check_claim_writable "$slug" status "$_sk" "$(fact "$rel" session)" "$_sk" "$rel" || return 0
  if [ "$when" = retry ]; then
    [ "$CW_CLS" = mine ] || return 0
    case "$CW_STATUS" in held|live) ;; *) return 0 ;; esac
  fi
  if write_claim "$slug" "$st" "$_sk" soft "$rel"; then
    [ "$when" = first ] || echo "unattended: claim retried — $slug now reads $st on the remote"
  else
    echo "unattended: the settle's claim write did not complete; re-run --settle $slug to retry it"
  fi
}
```

`check_claim_writable` exports two more values beside `CW_ACT`, reset with them: `CW_CLS`, the
claim-read class it derived, and `CW_STATUS`, the claim's own status. The already-settled exit
derives the status from the record as the settle's three branches do: `landed` for a LANDED record
`landed-by: attended`, `aborted` for a working record carrying `abandoned`, and none for an
`ABORTED` record. Its line becomes `unattended: already settled - <rel> reads <phase>...; the record
was not rewritten`, and the driver suite's one `hit` on the old text, `unattended.test.sh:9099`,
reads the new one.

The `mine` and `held`-or-`live` guard is what keeps a retry from moving a claim it does not own. A
claim already `landed` or `aborted` is left, so a second re-run pushes nothing. A newer run's claim
is foreign, so the status column's `*)` branch announces it and nothing moves.

The verbs guide's `--settle` entry says a re-run over a settled record leaves the record and retries
that claim write. The stops guide's status-write sentence says the same. Both templates are edited
because they would otherwise state false behaviour, the edit rule shared invariant 10 gives them.

### S5 — the hand-off sweep's one unresolved line

`bash tools/unattended/unattended.sh --park aGraftedHelix --item unit-34-close-handoff --reason "<question; options; reason>"`.
The question: who runs unit 34's hand-off to the close, the pooled calibration of the five receiving
shards and the eight-shard identity. The options: a unit of this build, or the main loop at
`VERIFYING`. The reason: both are suite runs, which no pass may perform, and the unattended kit's
README already makes the pooled suites the DoD for work touching the kit, so the close owns them.

### S6 — a note the branch's own edit earns

Inside the existing `if [ -z "$pbad" ]` branch, before the `note`:

```sh
r=$(git remote 2>/dev/null); case "$r" in *$'\n'*) r="" ;; esac
tip=""; [ -z "$r" ] || tip=$(git rev-parse -q --verify "refs/remotes/$r/HEAD" 2>/dev/null)
mb=""; [ -z "$tip" ] || mb=$(git merge-base HEAD "$tip" 2>/dev/null)
own=""; [ -z "$mb" ] || own=1
for f in $bad; do [ -n "$own" ] || break; git diff --quiet "$mb" HEAD -- "$rel/$f" && own=""; done
```

With `own` set it prints the note and returns, as today. Otherwise the install matches the primary
and the branch did not make the difference, so the primary lags, and the arm prints
`UNWIRED  skill     — the installed engine differs from tracked in:${bad}; the install matches the primary checkout, which lags this branch's base. Fix: git -C <primary> pull --ff-only`
and counts it. The install-drifts-from-primary path is unchanged.

The wiring suite's linked-worktree block gains a bare origin with its `HEAD` set, so the existing
note arm resolves a tip. A new arm advances the origin's `main` with an engine edit the primary
never fetched into its own `HEAD`, branches a linked worktree from `origin/main` with no engine edit,
and expects that UNWIRED line.

### S7 and S8 — the commit pass, graded and counted

```js
const COMMIT_LITERAL = /\bgit(\s+-[cC]\s+\S+)*\s+commit(?![-\w])/
// in the per-file loop:
const t = line.trim()
if (t.startsWith('//') || t.startsWith('*')) return
if (!COMMIT_LITERAL.test(line)) return
graded++
if (!line.includes(' -- ')) { /* the existing finding line */ pathless++ }
```

The name stays; its comment says the match now runs anywhere on a code line. The `(?![-\w])` tail
keeps `git commit-tree`, which reads no index, out of the population. After the per-file loop, in
discovery mode, `graded === 0` with some discovered path ending `/unattended-build.js` prints
`workflow-syntax: graded 0 git commit lines while the build harness render is present — the pass matched nothing it exists to grade`
and exits 1. Any other run prints `workflow-syntax: graded <n> git commit line(s)` before the green
line. The header's DOES-NOT-CHECK list gains: a `git` reached through a variable or a wrapper
function, a global option other than `-c` or `-C` between `git` and `commit`, a command continued
across lines, and a trailing `//` comment on a code line, which is graded as code.

The suite's GH32 block gains four explicit-file fixtures and one discovery arm: a comment-only line
passes, `'git -C "$r" commit -q -m x'` reds, `'set -e; git commit -q -m y'` reds, and
`'git commit-tree "$t" -m z'` passes. The discovery arm runs the checker from the repo root and
asserts its `graded <n>` line reads at least 1. `FLOOR_ASSERTIONS` rises by the assertions added.

### S9 — the exec wait gets an arm that can fail

In the extracted-`run_bounded` block, after the arm proving a command inside its bound survives:

```sh
write_proc_record() { [ -e "$_d/up" ] && echo up || echo early; } >>"$TMP/rb-up.log"
run_bounded bash -c 'exit 0'
same "GH36 the process record waits for the exec marker" "$(cat "$TMP/rb-up.log")" "up"
write_proc_record() { :; }
```

The stub runs where the wait ends. With the wait loop at `unattended.sh:263` deleted it runs as soon
as `&` returns, before the child shell has started, and reads `early`.

### S10 — one lock between a claim push and a landing push

The lock is `<git-dir>/claim-push.lock`, a directory, beside `push-main-active`, so it is per git dir
for the reason unit 32's guard is.

`write_claim`, where `RUNLOG_GITDIR` is set:

1. `mkdir "$lk"`. When that fails, the lock is stale if its `until` file holds an epoch already
   passed, or carries none and the directory is older than two minutes by `find -mmin +2`; a stale
   lock is cleared and `mkdir` tried once more. A live one returns 2 with
   `WC_WHY="a claim push from this git dir is in flight; retry once it ends: <lk>"`.
2. Write `until`, now plus `REMOTE_BOUND` plus ten seconds, the push's bound and its kill grace with
   a margin.
3. Test `push-main-active` as today. When it exists, release the lock and return 2 with today's
   `WC_WHY`, unchanged, so GH32 AC6's `hit` holds.
4. Build, push and classify as today, then release the lock before `rm -f "$d"`, on every path.

`tools/push-main.sh`, on both paths, becomes: `touch "$marker"`; `check_claim_push_clear`;
`rm -f "$refusal" "$barfile"`; `git push`; then on success `write_lander_marker`, else
`cls=$(derive_push_failure)`; then `rm -f "$marker"`. The marker now precedes the clear, so a claim
push already past its marker test finishes, and its hook's clear lands, before the lander clears and
pushes. `check_claim_push_clear` polls once a second while `claim-push.lock` exists and its `until`
is in the future, up to `CLAIM_WAIT_CEILING=120` seconds for a lock with no readable deadline. It
prints `push-main: waited <n>s for a claim push in flight in this git dir` when it waited, and
`push-main: proceeding past a claim-push lock whose deadline passed: <path>` when it stopped at an
expired one. The EXIT trap still clears the marker.

The header comment at `unattended.sh:2053` says the two writers are serialised by the lock and the
marker, and states what it does not check: on a host with no runnable `timeout -k` the push is
unbounded, so a push can outlive its recorded deadline. The second-instance paragraph of
`memory/gotchas/decision-re-derived-by-a-second-process.md` says the check-then-act window is
closed by the lock, and its gate section names the new arms.

### S11 — the seams carry their instrument, and the hoist rule a standing arm

Each seam line becomes `cd "$TMP" || exit 2; anchor_restore; read_topo s<k>`, keeping its comment.
The header's REFS clause says the nine re-cut seams restore refs by `anchor_restore` and call
`read_topo s1` to `s9` as their instrument.

```sh
check_helpers_hoisted() { # <suite file> -> 0 and nothing printed, or 1 naming each definition
  awk '/^if in_shard/ { r++ } /^FLOOR_ASSERTIONS=/ { f = 1; exit }
       r && /^[A-Za-z_][A-Za-z0-9_]*\(\) *\{/ { print FILENAME ":" NR ": " $0; bad = 1 }
       END { if (!r || !f) { print "DEAD PROBE: no shard region or no floor line read in " FILENAME; exit 1 }
             exit bad }' "$1"
}
```

The arm calls it on `$HERE/check-unattended.test.sh`, counts one assertion, and prints its output on
failure. The prologue now executes one assertion, so `FLOOR_ASSERTIONS` and each of
`FLOOR_SHARD_1` to `FLOOR_SHARD_8` rise by one, and the floor comment's "the prologue alone executes
0" becomes 1.

### S12 — the roster row

`memory/builds/aGraftedHelix/README.md:99`'s Mechanism cell becomes
`ADOPTED: every red arm of the owed unattended suites is fixed, the two pool races are closed, and gate shard 8 is re-cut`,
the title spec 34 carries at rev-3, in a records commit.

### S14 — two carriers stop saying the checklist always exits 0

The build method's M6 line becomes: it takes a COMMITTED range and exits 0 whenever it prints a
checklist, and 1 with a `HYGIENE gotchas:` line when it refuses the range. The skill's sentence
"Its stdout IS the checklist and it always exits 0" becomes "Its stdout IS the checklist and it
exits 0 whenever it prints one, and 1 with a `HYGIENE gotchas:` line when it refuses the range".
The README row already states this, so both point at behaviour one carrier owns. The method stays
under its 30720-byte budget. The method's live copy is re-rendered by the kit's parity render, the
skill by `adopt-unattended.sh`.

### Inventory

| identifier | where | cell |
|---|---|---|
| `write_settle_claim` | `tools/unattended/unattended.sh` | `sh.function` |
| `CW_CLS`, `CW_STATUS` | `check_claim_writable`'s outputs | shell globals beside `CW_ACT` |
| `check_claim_push_clear` | `tools/push-main.sh` | `sh.function` |
| `CLAIM_WAIT_CEILING` | `tools/push-main.sh` | constant |
| `claim-push.lock` | the git dir | lock directory, with an `until` file |
| `check_helpers_hoisted` | `tools/unattended/check-unattended.test.sh` | `sh.function` |
| `unit-34-close-handoff` | `memory/builds/aGraftedHelix/RUN.md` | parked item |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
on 2026-10-06 and answered OK; `wait_` was refused as outside the declared table, which is why the
lander's helper is a `check_`. No check number, leg, conf key or file is minted, and no Python or
JavaScript symbol is added, so the map's symbol index does not move.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js` by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/check-workflow-syntax.js`, `tools/workflows/README.md`
- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js`, the version line
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/STOPS.template.md`, `memory/guides/UNATTENDED-STOPS.md`
- `tools/check-wiring.sh`, `tools/check-wiring.test.sh`
- `tools/push-main.sh`, `tools/push-main.test.sh`
- `memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md`,
  `memory/gotchas/decision-re-derived-by-a-second-process.md`, `memory/gotchas/INDEX.md`
- `memory/map/features/unattended-stops.md`, `memory/map/features/review-harnesses.md`
- `memory/builds/aGraftedHelix/README.md`, `memory/builds/aGraftedHelix/RUN.md` through `--park`
- `memory/guides/SESSION-KICKOFF.md`, the re-stamp
- `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` by the render (S14)
- every version carrier `tools/check-kit-versions.sh` pairs for the four kits

### Rollout

One pass, in these steps, each verified by its own criteria before the next:

1. `tools/memory-tree/gotchas.py`: S1. Then S2's sweep, recorded in the class record.
2. `tools/unattended/unattended.sh` and its driver suite: S4, then S10's driver half, then S9.
3. `tools/push-main.sh` and its suite: S10's lander half.
4. `tools/check-wiring.sh` and its suite: S6.
5. `tools/workflows/`: S3, then S7 and S8. The render, then the fixture `base` edit across the
   suite, re-reading unit 35's arms.
6. The skill, verbs and stops templates, re-adopted: S3's sentence, S4's two and S14's skill
   sentence; then S14's build-method sentence and its render.
7. `tools/unattended/check-unattended.test.sh`: S11.
8. Records: S12, S5's park, the gotcha sections, `gotchas.py --write`, the two dossiers.
9. S13: each kit's version once, the harness engine identity and its suite pin, renders, the
   manifest re-stamp.

### Alternatives rejected

- **M3 by the skill sentence alone.** The skeptic's first option. It binds the one caller that reads
  the skill, and a caller copying arguments from the harness header still reaches an audit that
  reads invariants nowhere. §8 F1.
- **M3 by a refusal on every call.** It would refuse unit 35's audit-OFF route, whose AC4 runs it
  with no `base` and asserts the warning, which undoes that unit.
- **M5 against the primary checkout's HEAD.** Where the primary lags, its HEAD sits before the
  branch's fork, so the diff counts the default branch's own commits as the branch's edits and the
  note stays a lie in exactly the reported case. §8 F2.
- **M6 with the zero floor in the suite alone.** The suite is not on the merge bar, so the floor
  would bind only on demand. The checker's refusal keyed on the render binds on every bar, and an
  adopter tree with no render keeps its announced zero. §8 F3.
- **M4 parked.** The mandate files nothing and adopts every discovery, and the fix is one function
  over the existing status column. §8 F4.
- **L1 by per-push verdict paths.** The finder's fix, judged unsound by the skeptic: the pre-push
  hook names its verdict files, and changing that is a change to the hook every adopter receives.
- **L1 with the lander's bound as a literal copy of `REMOTE_BOUND`.** Two kits would spell one
  number. Reading the unattended kit's constant names another kit's file, shared invariant 2. §8 F5.
- **L1 by the run-gates turnstile.** It is another kit's lock, built for hour-long bars with a
  heartbeat; a push bounded by `REMOTE_BOUND` needs a deadline and nothing else.

## 5. Production-readiness checklist

- security — S3 refuses an audit that would read its exemptions from the working tree. S10 closes a
  window in which one process could erase the verdict another trusts. No credential, endpoint, ref
  namespace or write surface is added; the lock lives in the git dir beside the existing marker.
- perf / scale — S1 changes one git call's flags. S4 adds one claim read on a re-run of an
  already-settled `--settle` where claims are on. S10 adds one `mkdir`, one `date` and one file write
  per claim push, and the lander waits at most one claim push's bound. S7 tests one regex per line
  of six scripts. The new suite arms each cost under a second except the lander's wait arm, about
  three seconds.
- error / empty / loading states — A busy lock is a named not-completed write, a stale lock is
  cleared, and a lock with no deadline is bounded by the lander's ceiling. A settle claim write that
  does not complete names its remedy. A zero graded count is either a named dead probe or an
  announced count, never silent. The hoist arm refuses as a dead probe when it reads no region.
- observability — New lines: `claim retried —`, the settle's re-run remedy, the busy-lock reason,
  the lander's waited and proceeded lines, `graded <n> git commit line(s)`, the primary-lags UNWIRED
  remedy, and `topo boundary=s<k>` under `CHECK_UNATTENDED_TOPO`.
- risks — S3's fixture edit touches every audit-route arm of the build-harness suite after unit 35
  rewrote some of them; each arm's expected text is re-read rather than bulk-replaced. Edits to
  `unattended.sh`, `push-main.sh` and `check-wiring.sh` shift lines under the install-prefix waivers,
  which are line-keyed, so the leg is read and any moved waiver re-keyed. The unattended kit's
  suites are run once at VERIFYING by the main loop. A claim push and a landing in one git dir now
  serialise, so a beat during a landing's push skips as it already does during the bar.
- testing — Every new assertion is observed red on its staged break before it lands; §6 names each.
  The suites they live in run once at VERIFYING, at the main loop.
- migration — None. An adopter's caller passing `specAudit` without `base` now gets a named refusal
  instead of a warning, and the rendered skill tells it what to pass.
- user docs — `tools/unattended/SKILL.template.md`, the verbs and stops guides, the workflows README,
  and the two dossiers.

## 6. Acceptance criteria

Criteria naming a slice run it in the session scratchpad under a name that is not a suite name:
the suite's prologue plus the block the criterion names. Each staged break is made in a scratch copy
or in the working tree, and is restored before the next criterion, which
`git diff --quiet -- <the file>` against the pass's commit confirms.

- **AC1** — When `python tools/memory-tree/gotchas.py --selftest` runs at the pass's commit, it
  prints `PASS — gotchas: all arms held`, and its rename arm's line reads `ok`. With the touched-set
  read in the working tree reverted to `--name-only` alone, the rename arm reads FAIL. In a fixture
  repository whose last commit `git mv`s an anchored invariant and edits its gate,
  `gotchas.py --for-diff HEAD~1..HEAD` prints `# by design — 0` and both names as
  `NEW/CHANGED invariant` items.
  Red when: a renamed record's base ruling stays in the by-design block.
- **AC2** — When the S2 sweep is re-run at the pass's commit as
  `git log --no-merges --grep=aGraftedHelix --format=%h 5266d22e..HEAD`, each commit's added lines
  filtered by `grep -E 'diff[^|]*--name-only'`, every hit outside a suite is classified in the
  acceptance ledger, and `grep -n "gotchas.py" memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md`
  prints a line inside its `## Where it bit` section.
  Red when: a prefix-matched touched-set read without `--no-renames` survives unclassified, or the
  class record does not name this instance.
  figure: the hit count is DERIVED at observation time.
- **AC3** — When a slice of the build-harness suite runs its GH29 and BT3 blocks over the edited
  render, a declared `specAudit` with no `base` and one with `base` `origin/main` each print `THROW`
  and `is declared beside no pinned`, and no `prompt:` line. A 40-hex `base` puts
  `--for-paths --base <that sha>` on the resolver's prompt line and the pinned step-6 command on the
  `prompt:commit:specs:tB:` line, and no `WARNING: the audit's checklist reads invariants from the working tree`
  line prints in any run. Every other arm of the two blocks keeps its verdict with the fixtures'
  `base` in place.
  Red when: a declared audit runs with no pinned base. Staged: the refusal cut from a scratch copy of
  the render, under which the no-base arm prints no `THROW`.
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice.
- **AC4** — When `grep -n "base: <" .claude/skills/unattended/SKILL.md` runs at the pass's commit, it
  prints a line in the harness-call paragraph beside the `scratch` sentence, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: the shipped caller's instruction still names no `base`, or the installed skill differs
  from its template.
- **AC5** — When a slice of the driver suite plants `push-main-active` in the fixture's git dir beside
  a hand-off whose claim reads `held`, `--settle tRun` exits 0, writes `phase: LANDED`, prints the
  re-run remedy, and `--claims` reads `tRun` `held`. With the marker cleared, a second `--settle tRun`
  prints `already settled` and `claim retried`, and `--claims` prints `landed terminal`. A third
  re-run leaves the claim ref's sha unchanged, read by `git ls-remote`.
  Red when: the already-settled exit writes nothing, so the claim stays `held`.
- **AC6** — When the same slice seeds a fresh `live` claim another session holds over a settled
  record, a re-run of `--settle tRun` prints `claim not written` and leaves that ref's sha unchanged.
  The existing `unattended: already settled -` arm reads `the record was not rewritten`.
  Red when: the retry writes over a claim the record's run does not hold.
- **AC7** — When `grep -n "unit-34-close-handoff" memory/builds/aGraftedHelix/RUN.md` runs at the
  pass's commit, it prints one parked row carrying ` · reason `, and every other hand-off line the
  sweep lists resolves to a unit id in the roster of `memory/builds/aGraftedHelix/README.md` or a
  parked row in the same run-state file, which the acceptance ledger lists line by line.
  Red when: a line handing work to the orchestrator or the close resolves to neither.
- **AC8** — When a slice of the wiring suite runs its linked-worktree block over a fixture with a bare
  origin, the worktree whose branch edits `SKILL.md` prints `note     skill`, and the worktree branched
  from an `origin/main` whose engine edit the primary has not taken, with no engine edit of its own,
  prints `UNWIRED  skill` naming `SKILL.md` and `pull --ff-only`. With no remote `HEAD` set, the
  editing worktree prints `UNWIRED  skill`.
  Red when: the branch-change condition is cut from a scratch copy of `tools/check-wiring.sh`, so the
  lagging worktree reads `note`.
- **AC9** — When `bash tools/check-wiring.sh --check` runs in this worktree at the pass's commit, its
  skill line reads `note` and names only the engine files this branch edits.
  Red when: a file the branch did not edit is named in the note.
  fixture: node `a`'s install is a link to the primary checkout, measured 2026-10-06; another node's
  copy install reaches the install-drifts arm instead.
- **AC10** — When `node tools/workflows/check-workflow-syntax.js` is handed four scratchpad files
  explicitly, a comment-only `git commit` line and a `git commit-tree` line each exit 0, while
  `'git -C "$r" commit -q -m x'` and `'set -e; git commit -q -m y'` each exit 1 naming their line.
  Red when: either real form passes, or the comment reds. Staged: the old `COMMIT_LITERAL` restored in
  a scratch copy of the checker, under which both real forms pass and the comment reds.
- **AC11** — When `node tools/workflows/check-workflow-syntax.js` runs at the repo root at the pass's
  commit, it exits 0 and prints `graded 1 git commit line(s)`. In a fixture repository under a short
  temp root holding a marked `unattended-build.js` with no commit line, it exits 1 naming the dead
  probe; holding only a marked `other.js`, it exits 0 printing `graded 0`.
  Red when: a population holding the render and grading nothing exits 0.
  figure: the count 1 is PINNED from the probe in §4 at `45ce8c76`; the suite's arm floors it at 1.
- **AC12** — When `grep -n "second pass\|pathless" tools/workflows/README.md` runs at the pass's
  commit, it prints the checker-table row for `check-workflow-syntax.js`, and
  `grep -c "git -C" tools/workflows/check-workflow-syntax.js` counts at least one line in its header.
  Red when: the README row still says only that every script parses.
- **AC13** — When a slice of the driver suite runs its extracted-`run_bounded` block, the new arm's
  `same` reads `up`. Against a scratch copy of the driver with the wait loop at
  `tools/unattended/unattended.sh:263` deleted, the arm reads `early` and FAILs in each of five runs.
  Red when: the record can run before the exec and the arm stays green.
  figure: five of five is PINNED from the pass's own runs.
- **AC14** — When a slice of the driver suite plants a `claim-push.lock` directory whose `until` lies
  sixty seconds ahead beside a due beat, `--beat tRun` prints one `beat —` line skipped naming
  `claim-push.lock`, and `git ls-remote` shows the claim ref unmoved. With `until` in the past, the
  beat renews the claim and no lock directory remains. With `push-main-active` planted instead, the
  beat skips as GH32 AC6 asserts, and no lock directory remains.
  Red when: a claim push runs while another holds the lock, or a refused write leaves its lock.
- **AC15** — When a slice of the lander suite plants a `claim-push.lock` whose `until` lies three
  seconds ahead in the fixture's git dir, `bash tools/push-main.sh` lands, prints
  `waited` and `claim push in flight`, and takes at least two seconds. With `until` in the past it
  prints `proceeding past a claim-push lock` and lands without waiting.
  Red when: the wait is cut, so the lander pushes at once with the lock held.
- **AC16** — When `sed -n '/^cmd_land()/,/^}/p' tools/push-main.sh` is read at the pass's commit,
  `touch "$marker"`, `check_claim_push_clear`, the verdict-file clear and `git push` appear in that
  order, and `rm -f "$marker"` appears only after `derive_push_failure` and `write_lander_marker`. The
  attended path reads the same order.
  Red when: the marker is cleared before the lander reads the verdict files.
- **AC17** — When `grep -c "anchor_restore; read_topo s" tools/unattended/check-unattended.test.sh`
  runs at the pass's commit, it prints 9, and `sed -n 48p` of that file names `anchor_restore` for the
  re-cut seams.
  Red when: a seam restores refs with no instrument, or the header still says `read_topo` runs at
  every boundary alone.
  figure: 9 is PINNED, the seam count unit 34's re-cut made, measured at `45ce8c76`.
- **AC18** — When `check_helpers_hoisted`, extracted with `sed` from the kit-gate suite, runs over
  that suite at the pass's commit, it exits 0 printing nothing. Over a scratch copy with
  `x_helper() { :; }` inserted at column 0 inside region 8 it exits 1 naming that line. Over the
  suite's blob at `7dd6b08ec^`, unit 34's build commit's parent, read out with `git show` into the
  scratchpad, it names 31 lines. Over a file with no `if in_shard` line it exits 1 with `DEAD PROBE`.
  Red when: a region-defined helper passes, or a file with no region reads clean.
  figure: 31 is PINNED from the probe in §4.
- **AC19** — When `sed -n 99p memory/builds/aGraftedHelix/README.md` runs at the pass's commit, it
  carries `every red arm of the owed unattended suites is fixed` and not `proved inherited`.
  Red when: the roster row still states rev-1's filing mechanism.
- **AC20** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, its `memory-tree`, `review-harness`, `unattended` and `check-wiring` lines read
  `clean` at their bumped versions. `bash tools/check-kit-versions.sh` exits 0, line 3 of
  `tools/workflows/unattended-build.js` carries an engine identity one minor step above the parent's,
  and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a kit's shipped bytes moved and its version did not, or an installed guide differs from
  its template.
  figure: every version is DERIVED from the pass's parent at observation time.
- **AC21** — When `python tools/memory-tree/gotchas.py --check` and
  `python tools/codebase-map/test_codebase_map.py` run at the pass's commit, the first exits 0 and
  every line of the second reads `ok`. `bash skills/session-kickoff/manifest-check.sh` exits 0 over
  the re-stamped manifest.
  Red when: the catalogue index, the map or the manifest's audit stamp is stale.
- **AC22** — When `grep -n "always exits 0" memory/guides/BUILD-METHOD.md .claude/skills/unattended/SKILL.md`
  runs at the pass's commit, it prints nothing, and `grep -c "HYGIENE gotchas:"` counts at least one
  line in each. `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exits 0, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: either carrier still claims the checker cannot exit non-zero, or a render differs from
  its template.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `push-main self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `line length` · `govkit selfcheck` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `build-method size`

New arm: gotchas.py --selftest · a range renaming an anchored invariant; stage the touched-set read reverted to --name-only alone · none
New arm: tools/workflows/unattended-build.test.sh · GH29 refusals and the audit fixtures' base; stage the refusal cut from a render copy · FLOOR_ASSERTIONS, by the assertions added
New arm: tools/workflows/unattended-build.test.sh · the commit pass's four fixture forms and the real-tree graded floor; stage the old predicate restored · FLOOR_ASSERTIONS, by the assertions added
New arm: tools/unattended/unattended.test.sh · the settle retry (S4), the exec-marker record (S9) and the claim-push lock (S10); each break as §6 names it · FLOOR_ASSERTIONS and FLOOR_SHARD_2, by the assertions added
New arm: tools/push-main.test.sh · the lander's wait on a live and an expired claim-push lock; stage the wait cut · none
New arm: tools/check-wiring.test.sh · a lagging primary under a branch that never touched the engine; stage the branch-change condition cut · none
New arm: tools/unattended/check-unattended.test.sh · check_helpers_hoisted over its own file; stage a column-0 helper inside region 8 · FLOOR_ASSERTIONS and every FLOOR_SHARD_k, by one

The kit suites are not on the bar. A pass runs every criterion above directly, through slices where
a criterion lives in a suite, and the main loop runs those suites once at VERIFYING.

## 8. Open questions

- **F1 — M3: tell the shipped caller to pass `base`, refuse a declared audit without one, or both?**
  The skill sentence binds the one caller that reads the skill. The refusal binds every caller,
  including one copying the harness header, and turns a logged warning into a stop; it costs a
  fixture edit across the suite's audit-route arms, after unit 35 rewrote some of them. A refusal on
  every call, audit or not, would refuse unit 35's audit-OFF route and its AC4. Veto 1: neither
  criterion nor non-goal breaks under both. Veto 2: no new dependency or surface, since `base` is
  already a documented argument. Veto 3: the refusal narrows what an audit may read.
  RESOLVED (agent, 2026-10-06, delegated): both, the refusal only beside a declared `specAudit`, and
  the skill telling every call to pass `base`.
- **F2 — M5: what tells a branch's own edit from a lagging install?** The options: the merge base
  with the clone's one remote's `HEAD`, the skeptic's fix; the primary checkout's `HEAD`; or the local
  default branch. The primary's `HEAD` is the lagging thing itself, so measured against it a lagging
  primary counts the default branch's commits as the branch's edits, which is the reported defect.
  The local default branch in this repo's layout is the primary's own branch, the same answer. On
  this worktree the remote tip keeps today's note (§4).
  RESOLVED (agent, 2026-10-06, delegated): the merge base with the one remote's `HEAD`, UNWIRED when
  none resolves, and a primary-lags remedy on the UNWIRED line.
- **F3 — M6: where does the at-least-one floor live?** Id 11's corrected fix puts it in this repo's
  suite and keeps discovery mode from refusing a zero. Id 14's refuses a zero in the checker only when
  the harness render is present. Both agree an adopter tree with no commit line must not red, and
  the render-keyed refusal satisfies that, because every adopter carrying the render carries its
  commit line. The suite is not on the merge bar and the checker's leg is.
  RESOLVED (agent, 2026-10-06, delegated): both, the checker's refusal keyed on the render and the
  suite's real-tree floor.
- **F4 — M4: adopt the retry as this unit's mechanism, or park it?** The mandate adopts every
  discovery and files nothing. The fix reuses the status column and the settle's own write. Parking
  leaves a slug wedged at check 107 on a failed write with no route but a hand-deleted ref.
  RESOLVED (agent, 2026-10-06, delegated): adopt it, as S4.
- **F5 — L1: what bounds the lander's wait for a claim push?** The options: a literal in the lander
  matching `REMOTE_BOUND`; the lander reading the unattended kit's constant; or the deadline the
  claim writer records in the lock. A literal copy is two spellings of one number in two kits, the
  derive-over-author rule broken. Reading the constant names another kit's file by literal, shared
  invariant 2 and veto 2. The recorded deadline is derived by its owner and read by the waiter, with
  a file-constant ceiling only for a lock that carries none.
  RESOLVED (agent, 2026-10-06, delegated): the deadline the writer records, under a 120-second
  ceiling.
- **FACT-QUESTION · F6 — Does any other `diff --name-only` read this build added feed a prefix
  match?** Probe: the sweep in §4, over the added lines of the build's own non-merge commits since
  `5266d22e`. Liveness: the sweep finds the M2 instance at `gotchas.py:705` itself, so it can return
  a positive. Observation: one prefix-matched read, the M2 instance; one change-detection read; one
  read already passing `--no-renames`; the rest are suite equality assertions.
  RESOLVED (agent, 2026-10-06, delegated): no other read needs the fix; S1 is the only code change
  M2 owes, and S2 records the sweep.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 35-36 spec brief and the rotated run's closing
  review round 1, M2 to M7 and L1 to L3, grounded at `45ce8c76` against unit 35's spec as authored,
  with the sweeps, the wiring measurement and the two predicate probes run on node `a`.
- rev-2 · 2026-10-06 · S14 and AC22 added, adopted from unit 35's discovery: the build method and the
  unattended skill both say `--for-diff` always exits 0. §3's method non-goal now names the one
  sentence this unit edits under shared invariant 10's false-behaviour exception, and §7 names the
  method's parity and size legs.

## 10. Reuse audit

The map probes were these two:

```bash
python tools/codebase-map/reuse_lookup.py "retry a remote status write that failed on a re-run of the settle verb"
python tools/codebase-map/reuse_lookup.py "a lock that serialises two processes pushing from one git dir"
```

Both `reuse_lookup.py` probes ranked name-stem neighbours only, `run`, `write` and `git` helpers in
other kits, and both printed `unscanned layers: .sh`, so their miss is no evidence about the driver,
the lander or the wiring check, which are shell, and all three were read by hand. The second surfaced the run-gates
turnstile decisions, `TOOL-aPacedTurnstile-1` onward; that lock is another kit's and heartbeat-driven,
rejected in §4. The seams extended are these. The settle's status-write block in
`tools/unattended/unattended.sh` becomes `write_settle_claim`, and `check_claim_writable` gains two
outputs beside `CW_ACT`. `write_claim`'s own `push-main-active` guard is where the lock goes, and
`tools/push-main.sh`'s marker lifecycle is where the wait goes. `cmd_for_diff` in
`tools/memory-tree/gotchas.py` keeps its delegation to `cmd_for_paths`. `check-workflow-syntax.js`
keeps its discovered population and its constant. The `note` branch of `check_skill_install` gains
one condition. The suites' existing fixtures are extended in place: the `bd` invariant fixture, the
GH29 and GH32 blocks, the GH31 settle fixture, the extracted-`run_bounded` block, the GH32 AC6
marker fixture, the lander's bare-origin fixture and the wiring suite's linked-worktree block.

Recall surfaced unit 31's brief and spec, whose hand-off S4 disposes of; the previous closing
review's H3, the wedge S4 narrows to nothing; unit 29's brief and spec, whose S9 base pin S3 makes
reachable; and `memory/gotchas/decision-re-derived-by-a-second-process.md`, whose verdict-file
instance S10 extends rather than duplicates. Recall and the code disagreed once: the record says
`write_claim` pushes nothing while the marker exists, which the review showed holds only for a claim
that tests after the touch. §4 follows the code.

Recall terms used: claim push-main-active verdict pre-push-bar settle held wedge rename no-renames by-design invariant lock

The question passed with them: "what rules govern a claim push racing a landing's verdict files, a
settle whose claim write failed, and a rename hiding an invariant from the by-design block".
