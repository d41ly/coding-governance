# TOOL-aFrugalTurnstile-9 — the unattended close runs the boundary's decision where a post-merge bar is declared

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D11. Under `LANDER_MODE=in-place`, where `GATE_POST_MERGE` is declared at R, the
`gates-green` item asks the push boundary what bar the prepared merge owes, `pre-push --decide`, and
runs exactly that bar: full, scoped from the base the boundary picked, or none when a recorded green
already covers the tree. Undeclared, the item is today's `GATE_FULL=1` bar, byte for byte.

## 2. Scope (IN)

- **S1** — `read_gate_policy` in `tools/unattended/unattended.sh` also sets `GP_POST_MERGE`, cleared
  on entry, to `read_policy_key` of `GATE_POST_MERGE` in `.githooks/gate-env.sh` AT R. It reads that
  file whatever `GATE_POLICY_FILE` names, because the hook and the lander read the declaration there
  (F3). Observed by AC5, AC6 and AC7.
- **S2** — In the in-place branch of `gates-green`, on the first try only and after
  `check_inplace_preconditions` passes, a `GP_POST_MERGE` of `local` or `ci` makes the arm resolve the
  hook git will run and call it with `--decide <HEAD> <R>`, bounded, reading its stdout. Observed by
  AC1 and AC8.
- **S3** — The answer selects the bar: `full <why>` runs today's command; `scoped <base>` runs the
  bar with `GATE_FULL` unset and `GATE_BASE=<base>`; `covered <record>` runs no bar and meets the item,
  printing a line that names the record. Observed by AC1, AC2 and AC3.
- **S4** — Anything else falls back to today's `GATE_FULL=1` bar and says so in one line: a non-zero
  exit, no line, two lines, a line outside the three shapes, a scoped base that is not a commit here,
  or no hook file. Observed by AC4.
- **S5** — The green record design D3 defines is written by the TOOL-3 writer with `kind` and `base`
  matching the bar that ran: `full` with an empty base, or `scoped` with the decision's base. A
  `covered` item writes no record and no `gates-run` fact, because no bar ran. Observed by AC1, AC2
  and AC3.
- **S6** — Undeclared, under `LANDER_MODE=primary`, and for a value outside `local ci`, the hook is
  never asked and the bar is today's. Only the last prints a line, naming the value. Observed by AC5,
  AC7 and AC8.

## 3. Non-goals (OUT)

- The unattended protocol's text for this path. The build's protocol-text unit owns it, and F2 names
  a sentence that text must not carry.
- The decision itself, its predicates and its refusals. They are the hook's, and this arm reads one
  line.
- The `primary` landing mode. Its bar grades the branch rather than the merge the push publishes, so
  the boundary's decision for the merge does not describe it.
- Starting the post-merge bar. The lander does that after the push.
- Changing how a red, a TREE MOVED exit or a killed bar is read. The decision table after the bar is
  untouched.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-7` — `pre-push --decide <tip> <remote-sha>`, its one-line answer in three shapes and its promise to write nothing; without it every declared close falls back to the full bar, announced
- **consumes-from** `TOOL-aFrugalTurnstile-3` — the writer of the green record in the gates-green arm, which this unit hands a `kind` and a `base` instead of the fixed `full` it writes for a `GATE_FULL=1` bar
- **hands-off** external — whether the landing push after an in-place close can be covered at all, which F2 leaves to the main loop because the close commits on top of the graded merge

## 4. Design

### The declaration, S1

`read_gate_policy` already spells the hook's file in its `hook` local. Two lines join it, the clear
at the top beside the other three outputs and the read right after the empty-R refusal:

```bash
  GP_POLICY=park; GP_MAX_AGE=""; GP_WHY=""; GP_POST_MERGE=""
  ...
  GP_POST_MERGE=$(read_policy_key "$(GIT show "$r:$hook" 2>/dev/null)" GATE_POST_MERGE)
```

Its header line gains `GP_POST_MERGE` as an output and one sentence saying the key is read from the
hook's file on purpose. Every later early return in the function leaves the value set, which is
right: the policy file's absence says nothing about the hook's.

### The decision, S2 to S4

Inside the loop's in-place branch, after `check_inplace_preconditions` and `run_orphan_reap`, and
before the bar, on `_gtry = 1` only so a TREE MOVED re-run keeps the first decision:

| step | spelling |
|---|---|
| gate | `GP_POST_MERGE` is `local` or `ci`; otherwise skip silently, or print the outside-the-set line |
| HEAD | `_gh0=$(GIT rev-parse HEAD)`, the prepared merge the preconditions just admitted |
| hook | `$(GIT rev-parse --path-format=absolute --git-path hooks)/pre-push`, which honours `core.hooksPath` and resolves a relative value against the top level |
| ask | `RB_BOUND=600 run_bounded "${BASH:-bash}" "$hook" --decide "$_gh0" "$_gr"` |
| read | `RB_STDOUT` must be exactly one non-empty line |
| full | `full ` then text: the bar is today's command |
| scoped | `scoped ` then 40 lowercase hex that `GIT cat-file -e "<b>^{commit}"` accepts |
| covered | `covered ` then text: the record, as the hook names it |

The hook is resolved and not spelled because the hook git runs on the landing push is the one whose
answer matters. On node a a linked worktree's `config.worktree` points `core.hooksPath` at the
primary tree's `.githooks`, and `--git-path hooks` returned exactly that value when probed on
2026-10-09 with git 2.54; a relative `.githooks` came back absolute from a subdirectory.

`600` is a PINNED literal: the decision reads a tree digest and makes one bounded `ls-remote`, and
the bound exists so a hung remote cannot hold the close, not to time the decision.

### The bar, S3

```bash
case "$_gdec" in
  full)    run_bounded env -u GATE_WALL GATE_FULL=1 "${_genv[@]}" $GATE_CMD; _grc=$? ;;
  scoped)  run_bounded env -u GATE_WALL -u GATE_FULL GATE_BASE="$_gbase" "${_genv[@]}" $GATE_CMD; _grc=$? ;;
  covered) _grc=0 ;;
esac
```

`full` is the existing line unchanged, and the undeclared path never reaches this `case`: it keeps
the line it has today. `GATE_SELFTESTS` is neither set nor unset on any arm, as today. On `covered`,
`GG_RUN_FACT` is cleared before the arm returns 0, so the close writes no `gates-run` fact naming a
run id that never ran. The held-suite reader after the loop still runs on every path.

### Messages

Each is one stdout line, prefixed `unattended: gates-green — `:

| case | line |
|---|---|
| asked | `GATE_POST_MERGE=<v> at <R8>, so the push boundary decides this bar: pre-push --decide answered '<line>'` |
| covered | `met without a bar: the boundary reads this tree as covered by <record>` |
| fallback | `pre-push --decide did not answer with one decision line (exit <rc>), so the bar runs with GATE_FULL=1 as it does undeclared: <first line, or nothing>` |
| no hook | `no pre-push hook at <path>, so the boundary cannot be asked and the bar runs with GATE_FULL=1 as it does undeclared` |
| outside the set | `GATE_POST_MERGE at <R8> is '<v>', outside 'local ci', so it reads undeclared and the bar runs with GATE_FULL=1` |

### The record, S5

The TOOL-3 writer runs where it runs for today's bar, after `_grc = 0` with HEAD unmoved and an empty
porcelain listing. This unit makes it take the kind and the base as arguments, `full` and empty for
the full arm, `scoped` and `$_gbase` for the scoped arm, and skips it on `covered`. If the TOOL-3
writer as built already takes them, this unit only passes them.

### Inventory

No new function. `GP_POST_MERGE` is a new global beside `GP_POLICY`, `GP_MAX_AGE` and `GP_WHY`, and
`_gh0`, `_ghk`, `_gdec`, `_gbase` and `_grec` are locals added to the arm's existing `local` line.
The suite arms add no named function; if one is added, `gen_map.py --write` follows in the same commit.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — `read_gate_policy` and the in-place branch of `gates-green`.
- `tools/unattended/unattended.test.sh` — the new arms (run at VERIFYING, not in the pass).

### Alternatives rejected

- **Reading the declaration through `GATE_POLICY_FILE`.** See F3.
- **Asking the decision on every try.** A TREE MOVED re-run grades the same commit, and a second
  decision could pick a different base for it.
- **Spelling `.githooks/pre-push`.** It names the tracked file, not the hook git runs, and the two
  differ on every linked worktree of this repo.
- **Running the decision under `primary` too.** See §3.

## 5. Production-readiness checklist

- security — the arm acts on one line from a hook it resolves the way git does. A scoped base is
  accepted only as a commit present here; anything else is the full bar. No write surface is added.
- perf / scale — one bounded hook call per declared close; the saving is the scoped or skipped bar.
- error / empty / loading states — every malformed answer is the full bar plus one line, S4.
- observability — the asked line carries the hook's answer verbatim, so a reader sees what decided.
- risks — F1: the close commits `records(<slug>): close — LANDING` on top of the merge it graded, so
  the landing push's tree differs from the graded tree and a `covered` landing does not follow by
  construction. A `covered` close writes no `gates-run` fact, so `--handoff --code owner-landing`
  then refuses for want of a bar record, which is the existing refusal for a close with no bar. A hook
  older than TOOL-7 receives `--decide` as a remote name; it prints no decision line, so the arm falls
  back, but it may clear its own verdict files on the way, which push-main clears before every push.
  The decision describes the HOOK's bar and the arm applies it to `GATE_CMD`. In gov both are the
  runner (`.unattended.conf` and the hook's default, read 2026-10-09). An adopter whose `GATE_CMD` is
  another script gets a scoped run only if that script passes `GATE_BASE` on, a whole run otherwise,
  and a record naming `GATE_CMD` as its `bar`, which covers nothing at a push whose vetted bar differs.
- testing — direct fixtures in §6; the arms in §7 at VERIFYING.
- migration — none. Undeclared is today's behaviour, byte for byte.
- user docs — the protocol text is the protocol-text unit's; this unit adds the arm's comment block,
  including the sentence saying what it does NOT check: that the tree it graded is the tree the
  landing push will carry.

## 6. Acceptance criteria

Every criterion is observed in one scratch fixture under `%TEMP%/ft9`, never inside the worktree,
built as the unattended suite's in-place block builds its own: a bare origin, a stub lander whose exit
codes are env-driven, a stub bar `bin/bar.sh` that writes `GATE_FULL` and `GATE_BASE` from its own
environment to a file outside the repo, and `.githooks/gate-env.sh` committed at origin's main with the
case's declaration. `core.hooksPath` points at a `stubhooks` directory whose `pre-push` writes its argv
to a file outside the repo and, given `--decide`, prints `$STUB_DECISION`. The driver under test is
`tools/unattended/unattended.sh` from this worktree, run as `--close tRun` with the fixture as its
working directory. Each case runs first against the driver at base `bef97330`, where the hook is never
asked and the bar always sees `GATE_FULL` as 1.

- **AC1** — When `GATE_POST_MERGE=local` is declared at R and `STUB_DECISION='full stale'`, the hook's
  argv file holds `--decide`, then `git rev-parse HEAD`, then R; the bar's environment file reads
  `GATE_FULL` as 1 and no `GATE_BASE`; `gate-bar-green` in the fixture's git dir carries `kind` `full`; and
  the output carries the `pre-push --decide answered 'full stale'` line. Red when: the argv file is
  absent, which is the base driver's behaviour, or the record's kind is not `full`.
- **AC2** — When `STUB_DECISION` is `scoped ` followed by the full sha of origin's main, the bar's
  environment file reads `GATE_FULL` as `<unset>` and `GATE_BASE=` that sha, and `gate-bar-green` carries
  `kind` `scoped` and `base` that sha. Red when: the bar sees `GATE_FULL` as 1, or the record reads
  `kind full`.
- **AC3** — When `STUB_DECISION='covered gate-bar-green@1234abcd'` and the bar's environment file has
  been removed first, the file is still absent after the close, the item is met, the output carries
  `met without a bar` and `gate-bar-green@1234abcd`, and the run-state file's `gates-run:` line is
  unchanged by the close. Red when: the bar runs, or a `gates-run` fact names a run id with no
  `gate-run/<id>` directory.
- **AC4** — When `STUB_DECISION` is each of `maybe`, two lines, an empty string, `scoped deadbeef`, and
  a stub hook that exits 1, and again with the stub hook removed, the bar sees `GATE_FULL` as 1 and the
  output carries the `did not answer with one decision line` line, or the `no pre-push hook at` line
  for the removed hook. Red when: any of the six runs the bar scoped or skips it.
- **AC5** — When R declares no `GATE_POST_MERGE`, the hook's argv file is absent, the bar sees
  `GATE_FULL` as 1, and the `unattended: gates-green` lines of the output equal the base driver's for the
  same fixture once run ids and timings are masked with `sed -E 's/unattended-[0-9]+-[0-9]+/ID/g'`.
  Red when: the hook is asked, or any new line appears.
- **AC6** — When `GATE_POST_MERGE=local` is committed only on the run branch and not at R, the hook's
  argv file is absent and the bar sees `GATE_FULL` as 1; when `.unattended.conf` names a
  `GATE_POLICY_FILE` that declares `local` while `.githooks/gate-env.sh` at R declares nothing, the same
  holds. Red when: the hook is asked in either case, which would mean the declaration was read from
  HEAD or from the policy file.
- **AC7** — When R declares `GATE_POST_MERGE=yes`, the hook's argv file is absent, the bar sees
  `GATE_FULL` as 1, and the output carries the `outside 'local ci'` line naming `yes`. Red when: the hook
  is asked for a value outside the set.
- **AC8** — When `LANDER_MODE=primary` and R declares `local`, the hook's argv file is absent and the
  bar's environment is what the base driver gives it. Red when: the hook is asked outside `in-place`.

## 7. Gates

`unattended kit gate` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · a stub pre-push printing each decision through core.hooksPath, over the suite's in-place fixture with a gate-env declaration at origin · none

The close runs these. A pass runs only the §6 fixture.

## 8. Open questions

- **FACT-QUESTION · F1 — Does the landing push after an in-place close carry the tree the close
  graded, as design D11's "the landing push that follows is covered by construction" assumes?**
  Probe: read `write_close_commit` and its caller in `tools/unattended/unattended.sh`, then in this
  unit's fixture compare `git rev-parse <graded HEAD>^{tree}` with `git rev-parse HEAD^{tree}` after
  `--close`. Observation that decides it: equal trees in the ordinary close. Liveness: the probe can
  read equal, because `write_close_commit` commits nothing when the close changed no byte of the
  record, its re-close branch.
  Observed on 2026-10-09 by reading: the close writes `phase LANDING`, which always differs from the
  RUNNING or VERIFYING it replaces, stages it, and under `in-place` `write_close_commit` commits
  `records(<slug>): close — LANDING` on top of the graded merge (decision TOOL-dDerivedDocket-3), and
  `--land` pushes that commit. The trees differ in every ordinary close. Design D4 covers by tree
  equality, so D11's sentence is false as written; the scoped record the close writes covers nothing
  at the landing push.
  RESOLVED (agent, 2026-10-09, delegated): the fact is that the trees differ. This spec's criteria
  claim nothing about the landing push, and F2 carries what to do about it.
- **F2 — What makes the landing push after a scoped close cheap, given F1?**
  Under D11 as written, a scoped close writes `kind scoped` at the merge M with base B, stamps no full
  green, and the landing push of the close commit C is then decided again: not covered, because C's
  tree is not M's, and scoped from the older full green B over B..C, which re-grades the whole build.
  Today's close pays a full bar and the push scopes over M..C, the run-state file alone. A declared
  adopter would pay two scoped bars of the build's size instead of a full one and a tiny one.
  Options:
  (a) Build this unit as specced and accept the gap. Survives every veto; delivers little or no saving
  at the landing.
  (b) The boundary's scoped decision, TOOL-7's, adopts a `kind scoped` record as a base at its own sha
  when its `base` is itself a full green the decision would adopt and its sha is an ancestor of the
  tip, with the staleness bound counted from that underlying base so scoped records cannot chain past
  it. The push then scopes over M..C. This unit is unchanged; TOOL-7's spec and design D4 or D9 change.
  It extends the boundary's trust by exactly the evidence a scoped landing already rests on, and
  design D8's post-merge full bar backstops it.
  (c) Grade C instead of M, by writing the close commit before the bar. Changes the protocol's
  in-place order, a governance carrier, so it is an owner turn under the build method's veto 2.
  Recommendation: (b), resolved by the main loop across this unit, TOOL-7 and the text units, before
  any of them is built. Whatever is picked, the protocol and charter text must not say the landing
  push is `covered` after a close; under (b) it is scoped over the record commit.
- **F3 — Which file carries the declaration the driver reads?**
  Options: the policy file `read_gate_policy` resolves for `INHERITED_RED`, which `GATE_POLICY_FILE`
  may point elsewhere; or the hook's own `.githooks/gate-env.sh` at R.
  The brief says to read it "with the same reader the arm uses for the inherited-red policy". The
  reader, `read_policy_key`, is the same either way; the file is the question. The hook binds a
  post-merge red only where its own file declares one (design D8), and the lander starts the post-merge
  bar only where that same file declares it (design D10). A driver reading another file could declare
  a scoped close that no post-merge bar ever follows and no hook ever binds.
  RESOLVED (agent, 2026-10-09, delegated): the hook's file at R, always. Under the build method's rule
  this is the most feature-rich option surviving veto 3, since the other widens what a scoped landing
  may skip with nothing to backstop it.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seams this unit extends are `read_gate_policy` and its parser `read_policy_key`, both in
`tools/unattended/unattended.sh`, and `run_bounded` for the bounded hook call; the bar invocation is
the in-place line already in `gates-green`. `python tools/codebase-map/reuse_lookup.py "run the pre-push boundary decision without pushing"`
returned only generic `run` helpers and no seam that asks a hook for a decision, so for the decision
call itself no existing seam fits and it is a new caller of `run_bounded`. The hook path is resolved
with `git rev-parse --path-format=absolute`, the form `tools/unattended/adopt-unattended.sh` already
uses for the common dir. The recall probe returned decision TOOL-dDerivedDocket-3, which is the record
that the close commits on the graded merge and the source of F1.

Recall terms used: gates-green in-place GATE_FULL prepared merge close commit LANDING landing push scoped full-green stamp boundary decision
