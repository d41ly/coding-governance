# TOOL-aFrugalTurnstile-2 — pre-push records the green of the bar it ran, and a push whose tree carries one runs nothing

**Status:** OPEN · rev-2 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 2 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D3 (the hook's writer) and D4 (the reader and the `covered` decision). A push whose
tip TREE is the tree a recorded green graded, under the same bar, runs no bar at all. Today the
close's bar grades a tree, the landing push carries the same tree as a merge commit, and the hook
pays a second full bar because nothing records a green by tree and by bar.

## 2. Scope (IN)

- **S1 — the record grammar, written by one function.** A new column-0 function
  `write_bar_green` in `.githooks/pre-push`, signature
  `<git dir> <head before> <rc> <kind> <base> <bar> <run id>`. It writes nothing and returns 0
  unless every one holds: `rc` is 0; `kind` is `full` or `scoped`; `git rev-parse HEAD` equals
  `head before`; `git status --porcelain --ignore-submodules=untracked` succeeds and prints nothing;
  `git rev-parse <head before>^{tree}` is non-empty. It then writes `<git dir>/gate-bar-green.tmp`
  and renames it to `gate-bar-green`, one `key<TAB>value` line per key in exactly this order:
  `sha`, `tree`, `bar`, `bar_paths`, `kind`, `base`, `selftests`, `run_id`, `by`, `stamped`.
  `bar_paths` is every word of `bar` matching `*/*` or `*.sh`, the pattern `check_bar_command`
  uses, in order, space-separated, split with `read -ra` and never with `set -f`. `selftests` is
  `${GATE_SELFTESTS:+1}`; `by` is `pre-push`; `stamped` is `date -u +%Y-%m-%dT%H:%M:%SZ`. When the
  git dir and `git rev-parse --git-common-dir` resolve to different absolute paths, the file is also
  copied to `<common dir>/gate-bar-green.shared` through a `.tmp` rename, exactly as the runner
  shares its stamp at `tools/run-gates/run-gates.sh` ~3896. Observed by AC1, AC12, AC13.
- **S2 — the hook writes on its own green only.** In the `else` branch after the HEAD-moved check
  (~1606-1615), the hook calls `write_bar_green` with `$gd`, `$main_local`, `$_own_rc`,
  `$_bg_kind`, `${GATE_BASE:-}`, `$gate` and `$RUNLOG_GATE_RUN`, where `_own_rc` is `rc` captured after the verdict
  record check (~1588) and BEFORE the inherited-red landing arm (~1594) can change it. `_bg_kind` is
  `full` on a FULL decision and `scoped` on a scoped one. The call is skipped for a STUB bar
  (`bar_class` `stub`) and on a doc-only scoped push (`GATE_DOCS_BASE` exported), and each skip prints
  one line naming why. Observed by AC1, AC4, AC5, AC14, AC15.
- **S3 — the cover pass.** A new column-0 function `check_cover_record` and one pass over the
  candidates, placed after the dirty-tree refusal (~1448) and before the decision line (~1450),
  because it needs the vetted bar (~1354-1381) and the base the scoped decision adopted (~1297-1351).
  Candidates, in order, each read only when it exists: when `bar_record` is `runner`, the three
  runner stamps already in `green_candidates`; then, for any bar that is not a STUB,
  `$gd/gate-bar-green`, the common dir's own `gate-bar-green` when it is a different directory, and
  `<common dir>/gate-bar-green.shared`. The first candidate that covers wins. A record covers only
  when every condition holds:
  - its `sha` is non-empty and `git merge-base --is-ancestor <sha> "$main_local"` succeeds;
  - tree: for a bar record, its `tree` and `git rev-parse "$main_local^{tree}"` are both non-empty
    and equal; for a runner stamp, its `fingerprint` and `bash "$kitfp" "$main_local"` are both
    non-empty and equal, and its `manifest_blob` equals `git rev-parse "$main_local:${KP}gate-legs.json"`;
  - bar: a bar record's `bar` equals `$gate` byte for byte; a runner stamp needs `bar_record`
    `runner` and passes the manifest rule TOOL-aFrugalTurnstile-1 adds to predicate 7, called, not
    re-spelled;
  - selftests: when `GATE_SELFTESTS` is non-empty, the record's `selftests` reads `1`, predicate 8's
    relation;
  - kind: a runner stamp, or a bar record of kind `full`, covers outright; a bar record of kind
    `scoped` covers only when this push's own decision is scoped and its `base` equals the base that
    decision adopted, `inh_sha` when an inherited green was adopted, else `rec_sha`. A FULL decision
    is covered by no scoped record.
  Observed by AC2, AC3, AC6, AC7, AC8, AC9, AC10.
- **S3b — a bar record is a candidate for the scoped path too (rev-2, design §6 rev D4/D11).** After
  the runner-stamp candidates in the loop at ~1301 (and for a non-runner bar, in their place, per
  TOOL-aFrugalTurnstile-1), the same three `gate-bar-green` files are read as candidates for
  `check_green_record`. A `kind full` record passes predicates 2, 3, 5, 6 and 8 unchanged; predicate 4
  reads, for a bar record, "its `tree` equals `git rev-parse <sha>^{tree}`, both non-empty", and predicate 7
  "its `bar` equals `$gate` byte for byte". A `kind scoped` record at sha M is adoptable only when its
  `base` B, read as a sha, itself passes those predicates as a full green would (the runner stamps
  and the `kind full` bar records are searched for one whose `sha` is B), and then predicate 3's lag
  is counted from B, not from M, so a chain of scoped records can never stand further from a full
  green than the bound. An adopted record exports `GATE_BASE=<its sha>` exactly as a runner stamp
  does, and the scoped decision line names the record and, for `kind scoped`, its base. Because the
  bar compare needs the vetted bar, the bar-record candidates are evaluated after the bar vetting
  (~1381), the placement TOOL-aFrugalTurnstile-1 F1 chose for its own rule. Observed by AC17 to AC20.
- **S4 — the `covered` decision.** When a candidate covers, the hook prints one line, writes
  `$PUSH_BAR` in the same `printf` shape as ~1563 so push-main's lander-marker logic is unchanged,
  sets `RUNLOG_DECISION=covered`, starts no bar, exports none of `GATE_FULL`, `GATE_BASE`,
  `GATE_RUN_ID`, and exits with `RUNLOG_DECISION=covered; RUNLOG_CLEAN=1; exit 0` on one line. When
  no candidate covers and at least one `gate-bar-green` candidate exists, it prints one
  `not covered` line naming each existing candidate with the first condition it failed, then decides
  exactly as at base. Observed by AC2, AC3, AC11.
- **S5 — the header says what `covered` does not check.** One paragraph in the hook's opening
  comment block (lines 1-22). Observed by AC16.
- **S6 — the arms.** New arms in `.githooks/pre-push.test.sh` for AC1 to AC15, and in
  `.githooks/pre-push.runlog.test.sh` a new exit-table row for the covered exit plus an arm that
  produces a covered push, so the table's seen-join holds. Observed by AC11; the suites themselves
  run at VERIFYING, NOT OBSERVED inside the pass.

## 3. Non-goals (OUT)

- The unattended close's writer (TOOL-aFrugalTurnstile-3) and lineage reuse
  (TOOL-aFrugalTurnstile-4).
- The `--decide` callable and the post-merge red force (TOOL-aFrugalTurnstile-7).
- Re-grading history-reading legs over a covered push; the header states the gap (S5).

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-1` — the runner stamp's `manifest` key and the rule that
  admits a runner stamp only for a runner bar; without it a runner stamp written by a nested runner
  inside a wrapper bar could cover that wrapper's push.
- **hands-off** `TOOL-aFrugalTurnstile-3` — the record grammar and the function shape the
  unattended close writes and its parity arm compares.
- **hands-off** `TOOL-aFrugalTurnstile-7` — the inline comparison of a scoped record's base moves onto
  the callable decision, and a post-merge red that forces FULL must refuse a covered decision too
  unless the covering record's sha descends from the red.

## 4. Design

The cover pass is a FIFTH way out of the decision block and the only one that makes a push cheaper
than at base. It comes after every refusal the hook makes before a bar, so a dirty tree, a refused
bar command, a raw push and a head mismatch all still refuse first. It comes before the decision
line, so a covered push prints the covered line INSTEAD of a scoped or FULL line, never beside one.

Why tree equality is enough. Every leg the bar ran read the tree at `sha`, and the pushed tip holds
the same tree. The bar string is compared too, because `gate` is the program that decides what is
graded; tracked scripts it names are inside the tree, so `bar_paths` needs no blob check of its own.
The selftests relation is predicate 8's, because a held suite is not graded by a held-suite green.

Why the writer narrows on a doc-only push. A doc-only scoped bar runs fewer legs than a scoped bar
against the same base, and the record cannot say which it was. A later push of the same tree whose
R differs need not be doc-only, so that record would cover more than its bar graded. Writing no
record there costs a saving and never a verdict.

### Messages

| Event | Line, on stdout |
|---|---|
| covered | `pre-push: covered on <def> push (<tip8>) — tree <tree8> already carries a <kind> green: <where> sha <sha8> run <run id> by <by> — bar: <bar label> — no bar runs` |
| not covered | `pre-push: not covered — <where>: <why>[; <where>: <why>]` |
| written | `pre-push: recorded gate-bar-green for <sha8> — kind <kind>[ base <base8>] — bar: <bar>` |
| declined | `pre-push: no gate-bar-green written — <why>` |

`<where>` is `this git dir's gate-bar-green`, `the common dir's gate-bar-green`,
`the common dir's gate-bar-green.shared`, or `green_label`'s existing text for a runner stamp,
whose `by` prints as `run-gates` and whose kind prints as `full`. Each candidate reports its first
failure only.

| Not-covered `<why>` | Declined `<why>` |
|---|---|
| `sha <s8> is not an ancestor of the pushed tip` | `the bar is the declared STUB` |
| `it graded tree <t8> and the pushed tip holds <t8>` | `this push was scoped doc-only` |
| `its tree or the pushed tip's could not be read` | `the bar's own verdict was red, and the push lands under INHERITED_RED=land` |
| `it was earned by bar '<bar>' and this push runs '<gate>'` | `HEAD moved` |
| `it was earned with the kit self-tests HELD and this push runs them` | `the tree is not clean` |
| `it is a scoped green against base <b8> and this push scopes from <b8>`, or `… and this push is FULL` | — |

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `write_bar_green` | function | `sh.function`, `python tools/lexicon/lexicon.py --suggest` answered OK |
| `check_cover_record` | function | `sh.function`, answered OK |
| `gate-bar-green`, `gate-bar-green.shared` | git-dir record | none |
| `covered` | run-log decision value | none |

### Rollout

No migration: an absent `gate-bar-green` is today's state and changes no decision. The hook ships
verbatim to push-main adopters; under an absolute `core.hooksPath` the primary tree's copy runs.
This unit shares `.githooks/pre-push.test.sh` with TOOL-aFrugalTurnstile-5 in order group 2, so the
two passes are not write-disjoint and sequence.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Hashing the manifest a wrapper bar handed the runner**, the prompt's literal fix: rejected in
  design §2, because it lets a nested subset green certify a whole wrapper bar.
- **Keying the cover on the runner's fingerprint for every bar**: a wrapper bar writes no runner
  stamp of its own, so it would never be covered.

## 5. Production-readiness checklist

- security — the record lives in the git dir like `gate-full-green` and is trusted the same way;
  a process that can write the git dir can already plant a runner stamp. The bar string is
  compared byte for byte, and a tree that cannot be read on either side is never agreement
  (`TOOL-aPacedTurnstile-13`).
- perf / scale — at most six candidate files, each two or three `git` spawns; a covered push saves
  the whole bar.
- error / empty / loading states — every failed read is a not-covered reason, never a cover.
- observability — the covered line, the not-covered line, the writer's line and the run log's
  `covered` decision.
- risks — the in-place unattended close commits `records(<slug>): close — LANDING` on top of the
  merge its bar graded (`write_close_commit`, `tools/unattended/unattended.sh` ~9752, called at
  ~10091 after the Definition of Done), so that landing push's tree is NOT the graded tree and is
  not covered (F1). Every existing arm that pushes twice with a non-stub bar now also sees a
  writer line; the suite arms grep by pattern, which the VERIFYING run confirms.
- testing — S6's arms; the pass observes AC1 to AC16 in a scratch fixture.
- migration — none; absent records keep today's decisions.
- user docs — the hook header (S5); the runbook text is DEPL-aFrugalTurnstile-1's.

## 6. Acceptance criteria

Every criterion is observed in ONE scratch fixture under the session scratch, built the way
`build_vr_fixture` in the hook suite builds one: a bare remote, a work clone whose
`core.hooksPath` names a hooks dir holding a copy of the hook, the lander marker the fixture
touches, and a tracked stand-in runner at the kit path that writes `verdict GREEN` into its run
record and appends one line to a marker file outside the repo. The base hook is
`git show bef97330:.githooks/pre-push`, run first on each staged case.

- **AC1** — When branch tip X is pushed to `main` and its bar exits 0, `gate-bar-green` in the git
  dir carries `sha` X, `tree` equal to `git rev-parse X^{tree}`, `kind full`, `by pre-push`, `bar`
  equal to the vetted bar, and the ten keys in S1's order (`cut -f1`). Red when: the file is absent,
  which is the base hook's behaviour.
- **AC2** — When `main` at R then takes `git merge --no-ff X` and that merge is pushed, the output
  carries `pre-push: covered on main push` naming the record, `wc -l` of the marker file is
  unchanged, and the hook exits 0. Red when: the marker gains a line, which the base hook does.
- **AC3** — When the same merge carries one more commit changing one byte, the output carries
  `not covered` with `it graded tree`, and the marker gains a line. Red when: the push is covered.
- **AC4** — When a green push runs with `GOV_GATE_CMD_TEST` set, no `gate-bar-green` is written and
  the output says `the bar is the declared STUB`. Red when: a record is written.
- **AC5** — When the stand-in runner writes `verdict RED` and exits 1, no `gate-bar-green` is
  written. Red when: one is.
- **AC6** — When the record's `bar` value is replaced with another tracked bar's command and the
  merge is pushed, the output carries `it was earned by bar` and the bar runs. Red when: the push is
  covered.
- **AC7** — When the record's `selftests` is empty and the push runs with `GATE_SELFTESTS` set, the
  output carries `self-tests HELD` and the bar runs. Red when: the push is covered.
- **AC8** — When the record's `tree` value is empty, the output carries `could not be read` and the
  bar runs. Red when: an empty tree on the record side reads as agreement.
- **AC9** — When no `gate-bar-green` exists and a `gate-full-green` names X with the fingerprint
  `gate-fingerprint.sh X` prints and the kit manifest's blob, the merge push is covered by
  `this git dir`'s runner stamp. Red when: the push runs a bar.
  fixture: the stand-in runner at the kit path, so `bar_record` reads `runner`.
- **AC10** — When a `kind scoped` record's `base` equals the full green the scoped decision adopts,
  the push is covered; when its `base` names another sha, the output carries
  `a scoped green against base`. Red when: either half inverts.
- **AC11** — When AC2's push is covered, `pre-push-bar` in the git dir holds the vetted bar's three
  fields and `pushes.log` under the common dir's `runlog/` ends with an END line carrying
  `decision=covered` and `exit=clean`. Red when: either is absent.
- **AC12** — When AC1's push runs from a linked worktree made with `git worktree add`, the common
  dir also holds `gate-bar-green.shared` byte-identical to the worktree's record. Red when: it is
  absent.
- **AC13** — When `write_bar_green` is evaluated out of the hook by the `slice_fn` recipe and called
  with HEAD moved past `head before`, or with an untracked file present, it writes nothing. Red when:
  a record appears.
- **AC14** — When the stand-in runner writes a RED verdict whose every failed leg reads INHERITED
  against R and the push lands under the kit-default `land` policy, the output carries
  `red on inherited legs only` and no `gate-bar-green` is written. Red when: one is.
- **AC15** — When a doc-only push under `GATE_DOC_PATHS` is scoped and green, no `gate-bar-green` is
  written and the output says `doc-only`. Red when: one is.
- **AC16** — When `grep -c 'COVERED DOES NOT RE-GRADE HISTORY' .githooks/pre-push` runs, it prints
  `1`. Red when: it prints `0`.

- **AC17** — When a wrapper bar (a tracked script that runs the stand-in runner with `GATE_LEGS` at a
  derived manifest, as inCMS's `scripts/gov-bar.sh` does) earns a `kind full` record at merge M by a
  FULL push, and M plus one record-only commit C is pushed, the output carries `scoped gate` naming
  the `gate-bar-green` record at M, and `GATE_BASE` reaches the bar as M. Red when: the base hook's
  line, `the leg manifest differs`, and a FULL bar.
- **AC18** — When a `kind scoped` record at M carries `base` B and a `kind full` record names B, and
  C on top of M is pushed, the decision is scoped from M with the lag counted from B. Red when: the
  push is FULL, or it scopes from B.
- **AC19** — When the `kind scoped` record's `base` names a sha no full green names, the record is
  refused naming its base, and the decision is what it would be without it. Red when: it is adopted.
- **AC20** — When the `kind scoped` record's base B stands more than `GATE_FULL_MAX_LAG` first-parent
  landings behind C although M is one behind, the record is refused on the lag from B. Red when: it
  is adopted on M's lag.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `testsuite counts (every bar self-test prints one)`

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC12 AC13 AC14 AC15 AC17 AC18 AC19 AC20 · the scratch fixture above, each case run against the base hook first · none
New arm: .githooks/pre-push.runlog.test.sh · covers AC11 · a covered push, plus the exit-table row for the covered exit · `FLOOR_ASSERTIONS` raised by the assertions it adds

The hook header sentence S5 adds, quoted: "COVERED DOES NOT RE-GRADE HISTORY: a push whose tip
tree equals the tree a recorded green graded runs no leg, so a leg that reads history rather than
the tree (one the manifest marks impure) is not graded over the pushed commits; a declared
post-merge bar grades it." `.githooks/pre_push_bar_selftest.py` anchors on `set +f` spelled once in the hook, which is why
S1 splits with `read -ra`.

## 8. Open questions

- **FACT-QUESTION · F1 — Is the tree the unattended in-place close grades the tree its landing push
  carries, as design §1 and D11 state?** Probe: read `verb_close` in `tools/unattended/unattended.sh`
  for the order of the `gates-green` item and `write_close_commit`; and in an in-place close fixture
  compare `git rev-parse HEAD^{tree}` after the close with the graded merge's tree. Observed at
  writing time by the read: `write_close_commit` runs at ~10091, after the Definition of Done, and
  commits the run-state file on top of the graded merge, so the trees differ whenever the close
  changed a byte of its record. Liveness: a re-close over a record already at LANDING commits
  nothing (the `NOTHING STAGED IS NOT A FAILURE` arm), and there the trees are equal, so the probe
  can read the other way. Consequence for this unit: none to its mechanism; a gov landing still
  scopes from the runner stamp at the merge, one first-parent landing back, and a wrapper-bar
  adopter's in-place landing is not covered. Design D4 and D11 overstate the yield.
  RESOLVED (agent, 2026-10-09, delegated): build S1 to S6 as written; the finding is recorded here,
  in TOOL-aFrugalTurnstile-3 F1, and in this run's summary for the main loop to rev design D11.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft from design D3 and D4, insertion points read at base bef97330.
- rev-2 · 2026-10-09 · S3b, AC17 to AC20: a bar record is a candidate for the scoped path, and a
  scoped record is adoptable on its full-green base. What disagreed: rev-1's non-goal kept bar
  records cover-only, which left every wrapper-bar adopter's in-place landing FULL because the close
  commit moves the tree (this spec's F1); resolved by TOOL-aFrugalTurnstile-9 F2 option (b), design
  §6 rev D4/D11.

## 10. Reuse audit

`reuse_lookup.py "record that a bar exited green for a tree so a later push skips it"` (shell layer
scanned, no blind layer) returned no candidate that records a bar verdict by tree; the seams this
unit extends are in the hook itself: `read_green_file`, `green_candidates` and `green_label` for the
candidate walk, predicate 8's relation, `check_bar_command`'s path pattern for `bar_paths`, and the
runner's `.shared` write for the copy. No existing seam records a non-runner bar's green.

Recall terms used: pre-push full green stamp scoped boundary fingerprint candidate shared worktree selftests predicate lander marker
