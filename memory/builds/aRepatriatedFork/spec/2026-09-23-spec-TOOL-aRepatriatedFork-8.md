# TOOL-aRepatriatedFork-8 — the lander contracts inCMS carries

**Status:** CLOSED · rev-3 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-TOOL-aRepatriatedFork-8-1-acceptance-ledger.md](../build/2026-09-24-build-TOOL-aRepatriatedFork-8-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-8-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-8-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Take upstream the generic contracts inCMS's own pre-push hook and lander enforce and gov's do not, so
the push boundary works on a node whose remote is not named `origin`, reports why a push was refused
from a verdict the hook wrote rather than from git's prose, and cannot certify a tree the push does
not carry. Then give the one inCMS policy that is not generic, its docs-only fast path and its
branch-push hygiene gate, a declared seam, so inCMS can run gov's bytes.

## 2. Scope (IN)

- **S1** — The hook resolves the default branch from the remote git names in its first argument,
  `refs/remotes/$1/HEAD`, and never from a literal `origin`; `tools/push-main.sh` resolves its remote
  first and reads that remote's HEAD. `GOV_DEFAULT_BRANCH` keeps its cross-check role unchanged.
  Observed by AC1 and AC2.
- **S2** — A refusal channel. The hook clears `$(git rev-parse --git-dir)/pre-push-refusal` on every
  run and writes `<token><TAB><message>` from one function on every refusal and on a red bar; the
  lander clears it before each push, reads it after a failed one, probes `git ls-remote` before
  calling a remote unreachable, and reads no push output at all. Observed by AC3, AC4 and AC5.
- **S3** — One dirty definition, `git status --porcelain --ignore-submodules=untracked`, in the lander
  and in the hook, which refuses a default-branch push from a dirty tree before the bar. Observed by
  AC6 and AC7.
- **S4** — The hook re-reads `HEAD` after a green bar and refuses when it moved. Observed by AC8.
- **S5** — The adopter-policy seam. The bar receives `GATE_PUSH_BASE`, the remote's old sha for the
  default branch, set by the hook from git's ref lines. `.githooks/gate-env.sh` may declare
  `GOV_BRANCH_GATE_CMD`, vetted by `TOOL-aRepatriatedFork-5`'s tracked-script rule and run on a
  non-default push; unset, a non-default push stays ungated. Observed by AC9 and AC10.
- **S6** — `tools/push-main.test.sh` and `tools/check-wiring.test.sh` run at a foreign prefix. Each
  derives its kit path from its own location and resolves python through the inline fallback the
  hooks kit uses, never `tools/lib/resolve-python.sh`, which ships to no adopter. Observed by AC11.
- **S7** — `TOOL-aHonedRuleset-10` closes, since S2 is its fix. Observed by AC4.
- **S8** — ONE channel for the bar's verdict. The hook clears `pre-push-bar` beside
  `pre-push-refusal` on every run and, once the bar is vetted and before it runs, writes
  `<class><TAB><path><TAB><blob>`; the lander clears it before each push and writes its marker only
  when it reads `default` or `tracked`, never re-deriving the class from its own environment. And
  `.githooks/gate-env.sh` is sourced only when tracked at the pushed sha (HEAD on a non-default push)
  with a clean working copy; otherwise the push is refused as `bar-refused`. Observed by AC12.

## 3. Non-goals (OUT)

- A docs-only classifier in gov. Gov's economy for a cheap landing is the scoped decision against a
  recorded full green (`.githooks/pre-push:413-541`). S5 hands the pushed range to an adopter's bar,
  which classifies with its own policy.
- inCMS's environment names `INCMS_REMOTE` and `PUSH_MAIN_MAX_RETRIES`. The adopter documents the
  `GOV_` spellings instead; a dual read keeps two names for one knob.
- A `Co-Authored-By` trailer on the lander's reconcile merge. inCMS's commit-msg hook exempts an
  in-progress merge (`.githooks/commit-msg:42-49` at inCMS), so gov's merge is accepted there.
- inCMS's refusal when `.governance/kits.json` is present and its hygiene engine is not
  (`.githooks/pre-push:55-67` at inCMS). With S5, the branch bar is a tracked script, and a missing
  one is refused by `TOOL-aRepatriatedFork-5`'s rule.
- `tools/check-wiring.sh` itself. Its relocated-layout arms are `TOOL-aRepatriatedFork-19`, which
  owns the checker; S6 takes only the suite's two portability literals, and moves there whole if
  that unit takes the suite.
- The decision to run the full bar. Every forcing predicate stays as it is.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-5` — the tracked-script vetting S5 applies to `GOV_BRANCH_GATE_CMD`, and the bar refusal S2 turns into a token; without it the branch bar is an unvetted environment command
- **hands-off** external — inCMS moving its policy into `.githooks/gate-env.sh` and its bar, and retiring its project-owned hook and lander, in an inCMS session

## 4. Design

### Inventory of the gap

Measured by audit-B on 2026-09-23 against gov a7c78ad2 and inCMS 2bbd7b99b, and re-read at inCMS
1bc57da27 for this spec.

| contract | gov | inCMS | this unit |
|---|---|---|---|
| default branch | `refs/remotes/origin/HEAD`, `.githooks/pre-push:329` and `tools/push-main.sh:20` | literal `main`, `scripts/push-main.sh:32` | S1 |
| refusal verdict | the lander greps its own tee'd push output, `tools/push-main.sh:95`, `:137-144` | token file, `.githooks/pre-push:68-74`, `:103-110`; reader `scripts/push-main.sh:163-190` | S2 |
| dirty tree | `--porcelain -uno`, `tools/push-main.sh:71`; the hook checks nothing | `--ignore-submodules=untracked` in both, `scripts/push-main.sh:89`, `.githooks/pre-push:139` | S3 |
| HEAD moved during the bar | not checked | `.githooks/pre-push:164-165` | S4 |
| docs-only push | not classified | `scripts/gate.sh --docs-only`, `.githooks/pre-push:113-122` | S5, by seam |
| non-default push | ungated, `.githooks/pre-push:366` | hygiene when `memory/` moved, `.githooks/pre-push:85-98`, `:168-176` | S5, by seam |
| SSH keepalive | `tools/push-main.sh:56-61` | the same | already in gov |

Measured by audit-B: gov's lander run under inCMS's `scripts/push-main.test.sh` fails five arms, 4c,
11, 12, 13 and 14, and gov's hook fails 11 of the 13 cases of `scripts/test-pre-push-hook.sh`. On
node `d`, whose remote is `incms`, gov's lander exits 2 before its first fetch and gov's hook refuses
every default-branch push unless each node exports `GOV_DEFAULT_BRANCH`. `.githooks/gate-env.sh` is
sourced at `.githooks/pre-push:445`, after the lookup at `:329`, so a tracked file cannot repair it.

### S1, the remote

git runs a pre-push hook with the remote NAME as `$1` and its URL as `$2`; the hook already records
both (`RUNLOG_ARG1`, `RUNLOG_ARG2` at `.githooks/pre-push:98`). When `$1` names a configured remote,
the observed default is `refs/remotes/$1/HEAD` and the branch-existence probe at `:342-343` reads
`refs/remotes/$1/$def`. When the push names a URL, nothing is observable and the environment is the
only source, which is today's rule for a fresh `git init` at `:337`. Nothing moves `gate-env.sh`.

The lander takes its remote from `GOV_REMOTE`, else `branch.<current>.remote`, else the repository's
only remote, and refuses when none of those resolves. It then reads `refs/remotes/$remote/HEAD`.

### S2, the channel

| token | written by | lander says |
|---|---|---|
| `default-branch` | the three default-branch refusals, `:330-346` | a precondition; no leg ran |
| `manifest` | the misplaced-manifest refusal, `:387-397` | a precondition; no leg ran |
| `raw-push` | the missing lander marker, `:405-408` | a precondition; no leg ran |
| `head-mismatch` | pushed tip is not `HEAD`, `:411-416` | a precondition; no leg ran |
| `dirty-tree` | S3 | a precondition; no leg ran |
| `bar-refused` | `TOOL-aRepatriatedFork-5`'s refusals | a precondition; no leg ran |
| `gate-red` | a bar exiting non-zero, `:549` | the bar RAN and is red; read `gate-last-summary.txt` in the git dir |
| `head-moved` | S4 | the bar ran green and `HEAD` moved |

Tokens keep inCMS's spellings wherever inCMS has one, listed in its `fail_push` header
(`.githooks/pre-push:100-102` at inCMS), so inCMS's reader and gov's read one vocabulary. The run log
keeps its `refuse-*` decisions; the hook's one refusal function writes both, which is the only place
the two words are paired. `gate-last-summary.txt` is the file gov's runner
writes (`tools/run-gates/run-gates.sh:168`) and the one inCMS's `scripts/gate.sh` writes too.

The lander's order of evidence is inCMS's: the hook's token; else an `ls-remote` probe, so
unreachability is observed rather than inferred; else fetch and ancestry, red or race. It greps no
push output, which is what misreported a red bar as a network failure in `TOOL-aHonedRuleset-10`.

### S3 and S4, the tree the bar certifies

`--ignore-submodules=untracked` is the only form that refuses an untracked superproject file, a
submodule pointer change and a tracked edit inside a submodule, and ignores foreign untracked files
inside a submodule (`scripts/push-main.sh:84-89` at inCMS states the four cases). The hook refuses
before the bar because the bar reads the working tree while the push carries the commit. S4 reruns
the `HEAD` comparison `.githooks/pre-push:410-416` already makes, after the bar.

### S5, the seam

The hook sets `GATE_PUSH_BASE` itself from the ref line, overwriting any inherited value, and exports
it to the bar beside `GATE_FULL` or `GATE_BASE`. `GOV_BRANCH_GATE_CMD` requires sourcing
`.githooks/gate-env.sh` before the non-default exit at `:366`, so the sourcing moves up to just after
the ref loop; nothing it may set is read before its old position except by S5.

What inCMS then declares, as an inCMS change: `GOV_GATE_CMD='bash scripts/gate.sh'` and a branch bar
running `scripts/check-docs-hygiene.sh` when the pushed range touches `memory/`, in its tracked
`.githooks/gate-env.sh`; and `scripts/gate.sh` classifying the `GATE_PUSH_BASE` range with its
existing `--docs-only` rules.

### Migration

| adopter | record | disposition |
|---|---|---|
| inCMS | `KIT_PUSH_MAIN_DELTA` on `scripts/push-main.sh` | deleted after the inCMS session in the external edge; gov bytes |
| inCMS | `KIT_PUSH_MAIN_TEST_DELTA` on `scripts/push-main.test.sh` | deleted with it; gov's suite after S6 |
| inCMS | `.githooks/pre-push`, `role_dispositions` project-owned | becomes `engine` once its policy sits in `gate-env.sh`; `scripts/test-pre-push-hook.sh` retargets its stub from `INCMS_PUSH_GATE_CMD` to `GOV_GATE_CMD` with the test escape |
| inCMS | `CLAUDE.md` naming `PUSH_MAIN_MAX_RETRIES` | the `GOV_` spelling |
| inCMS | the `scripts/check-wiring.test.sh` fork | loses its two portability patches; the rest waits on `TOOL-aRepatriatedFork-19` |
| nc | `scripts/check-wiring.test.sh:29-35` at nc, the third `src_of` rung | deleted; S6 derives the prefix |
| gov | `TOOL-aHonedRuleset-10` in `memory/backlog/TOOL.md` | CLOSED by S2 |

### Rollout

One gov commit. The hook is `core.hooksPath`-resolved from the primary tree, so the new contracts bind
a clone once its primary tree checks the commit out. A lander that predates S2 reads no token and
falls back to its prose grep, so an old lander against a new hook is no worse than today.

### As built (rev-2)

- **S2's one function holds the pairing.** `write_refusal <token> <message>` writes the file and maps
  the token to its run-log decision, so no call site spells both words. `gate-red` and `head-moved`
  map to no decision: the bar RAN, and the `full` or `scoped` decision it ran under stands.
- **S3 computes the dirt before the bar is vetted and refuses after it**, so the vetting's own
  working-copy refusal keeps its message. `.githooks/pre_push_bar_selftest.py`'s mutation clears the
  dirt as well, since S3 now catches the rewrite its case M3 needs to see land.
- **S5's branch bar reads git's ref lines on stdin**, the pre-push hook's own input, and runs with
  `GATE_PUSH_BASE` unset: a non-default push can carry several refs, so one base sha cannot describe
  it. It is vetted at `HEAD`, the tree it runs from, and its run is the run-log decision `branch-gated`.
- **S2's lander probes the PUSH URL** with `ls-remote`, since the fetch URL may reach a remote the
  push cannot.
- **S7's backlog flip is the main loop's.** `--dispatch` refused `memory/backlog/TOOL.md` as a shared
  mutable record, so this unit closes the mechanism and the main loop records the row.

### Files touched

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh` (the exit table, and the `refuse-dirty` and `branch-gated` decisions)
- `.githooks/pre_push_bar_selftest.py` (the mutation also clears S3's dirt)
- `.githooks/gate-env.sh` (the documented keys, as comments)
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/check-wiring.test.sh`
- `AGENTS.md` (the push-boundary paragraph)

### Alternatives rejected

- **Export `GOV_DEFAULT_BRANCH` per node.** It works and is the documented stopgap, but it is an
  environment knob per node for a fact git hands the hook as `$1`.
- **Move `gate-env.sh` above the default-branch lookup so a file can set it.** A tracked file then
  selects which branch is gated, the fail-open `TOOL-aStandingWrit-4` closed.
- **Keep the prose grep and widen its patterns.** The grep reads the bar's own output, which the push
  tees, so any leg printing "rejected" fakes a race; inCMS measured that at `ABL-aWeighedAssay-2`.

## 5. Production-readiness checklist

- security — the push boundary. `GATE_PUSH_BASE` is set by the hook from git's stdin and overwrites an
  inherited value; `GOV_BRANCH_GATE_CMD` passes the tracked-script rule. A branch bar can only add a
  refusal to a push that is ungated today.
- perf / scale — one `git status` per default-branch push in the hook, and one `ls-remote` per failed
  push in the lander.
- error / empty / loading states — an absent token file after a failed push is the lander's cue to
  probe, never a pass; a stale file is cleared by both sides before it could be misread.
- observability — each token names its precondition, and the run log carries the same word.
- risks — a hook refusing dirt that an adopter's workflow leaves in the primary tree. The refusal
  names the paths, as inCMS's does.
- testing — each contract is an arm in `.githooks/pre-push.test.sh` or `tools/push-main.test.sh`,
  observed red against a7c78ad2, and both suites run at a `scripts/` prefix.
- migration — none for gov data; inCMS's steps are the external edge.
- user docs — `AGENTS.md`'s push-boundary paragraph and the comments in `.githooks/gate-env.sh`.

## 6. Acceptance criteria

- **AC1** — When a fixture's only remote is named `incms`, with its HEAD set, `tools/push-main.sh`
  lands the default branch with no `GOV_DEFAULT_BRANCH` exported; the a7c78ad2 lander exits 2.
  Red when: either side still reads `refs/remotes/origin/HEAD`.
- **AC2** — When the same fixture pushes a red bar to its default branch, `.githooks/pre-push`
  refuses at the bar; the a7c78ad2 hook refuses earlier with `can't determine the default branch`.
  Red when: the hook classifies the push from a remote it did not push to.
- **AC3** — When a raw default-branch push is refused, the git dir's `pre-push-refusal` holds
  `raw-push` and a message, and a later successful push through `tools/push-main.sh` leaves no such file.
  Red when: the token is missing, or a stale one survives into a later push.
- **AC4** — When the bar exits 1 in a fixture whose remote is reachable, `tools/push-main.sh` prints
  that the bar RAN and is red and names `gate-last-summary.txt`; the a7c78ad2 lander, given a bar that
  prints `connection`, reports the remote unreachable.
  Red when: any wording in the bar's output can still select the lander's verdict.
- **AC5** — When the remote is unreachable and no token was written, `tools/push-main.sh` reports
  unreachability after its `ls-remote` probe fails.
  Red when: the lander calls the remote down without probing it.
- **AC6** — When the primary tree holds an untracked superproject file, `tools/push-main.sh` refuses
  before the push; the a7c78ad2 lander, reading `-uno`, pushes.
  Red when: the bar can certify a file the push does not carry.
- **AC7** — When a submodule holds only its own untracked files, `tools/push-main.sh` and
  `.githooks/pre-push` both proceed, and when its pointer moved both refuse.
  Red when: the two sides disagree about one tree.
- **AC8** — When a stub bar commits during its run and exits 0, `.githooks/pre-push` refuses with
  `head-moved`.
  Red when: a green bar over a moved `HEAD` lands.
- **AC9** — When a stub bar prints `GATE_PUSH_BASE`, it prints the remote's pre-push sha, and an
  inherited value set before `git push` is not what it prints.
  Red when: the bar can be handed a range by the environment.
- **AC10** — When `.githooks/gate-env.sh` in a fixture declares `GOV_BRANCH_GATE_CMD` naming a tracked
  red script, a feature-branch push is refused; naming an untracked script, it is refused as
  `bar-refused`; unset, the push is ungated.
  Red when: the seam runs an unvetted command, or gates a branch push nobody declared.
- **AC11** — When `tools/push-main.sh` and `tools/check-wiring.sh` are installed with their suites
  under `scripts/` in a fixture that has no `tools/` directory, `git grep -n 'tools/lib/resolve-python' -- tools/push-main.test.sh tools/check-wiring.test.sh`
  returns nothing and each suite resolves its subject.
  Red when: a suite still spells `tools/` or needs a gov-internal library.
  fixture: a scratch install at a `scripts/` prefix; none is tracked today.
- **AC12** — When a fixture's `.githooks/gate-env.sh` sets `GOV_GATE_CMD_TEST=1` and
  `GOV_GATE_CMD=true` and `tools/push-main.sh` runs with neither in its environment, a committed copy
  lands with NO lander marker and push-main names the STUB; an untracked copy hidden by
  `.git/info/exclude` is refused before it is sourced, so nothing lands; and an untracked copy on a
  feature push is refused as `bar-refused`.
  Red when: the lander decides "stub" from an input the hook did not act on, or the hook sources a
  policy file nobody reviewed.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `push-main self-test` · `branch-guard self-test` · `lexicon naming predicates` · `check-wiring self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `agent-instructions wiring` · `recall floor` · `recall floor arms`

New arm: `tools/push-main.test.sh` · inCMS's arms 1b, 2c, 4c, 11, 12, 13 and 14, each run first against the a7c78ad2 lander to observe it fail · none
New arm: `.githooks/pre-push.test.sh` · a fixture remote named `incms`, a dirty tree, a HEAD moved by the bar, and a branch bar, each observed first against the a7c78ad2 hook · none
New arm: `tools/push-main.test.sh` · H1 and H1b, gate-env.sh setting the escape committed and then excluded, each observed writing the marker against the c6513db0 lander and hook first · none
New arm: `.githooks/pre-push.test.sh` · H1, an untracked gate-env.sh on a feature push, observed sourced against the c6513db0 hook first · none

## 8. Open questions

- **F1 — should the hook tolerate dirt its adopter classifies as docs, as inCMS's does?** inCMS lets a
  docs-only dirty path through (`.githooks/pre-push:139-156` at inCMS). Recommendation: no; the
  bar certifies a tree, and a dirty tree is not the pushed one. An adopter wanting the tolerance
  declares it in its bar.
  RESOLVED (owner, 2026-09-23): no, as recommended.
- **F2 — does the lander refuse when the repo has several remotes and none is configured for the
  branch?** Guessing picks a remote nobody chose. Recommendation: refuse and name
  `GOV_REMOTE`.
  RESOLVED (owner, 2026-09-23): refuse and name `GOV_REMOTE`, as recommended.
- **F3 — is `GOV_BRANCH_GATE_CMD` worth a key, or should inCMS keep branch-push hygiene in its
  pre-commit?** Without it inCMS cannot run gov's hook verbatim. Recommendation: take the key; it is
  one vetted command and the mechanism `gate-env.sh` exists for.
  RESOLVED (owner, 2026-09-23): take the key, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from audit-B and a re-read of gov a7c78ad2, inCMS 1bc57da27
  and nc f69e2ffb.
- rev-2 · 2026-09-24 · built. §4 gains "As built": S2's refusal function maps token to decision,
  S3 refuses after the bar is vetted, S5's branch bar reads the ref lines on stdin, the lander probes
  the push URL, and S7's backlog row moves to the main loop after `--dispatch` refused it. Files
  touched gains the run-log suite and the bar self-test, and loses `memory/backlog/TOOL.md`.
- rev-3 · 2026-09-24 · closing review round 1 H1 folded. S8 and AC12 added: the hook writes the bar
  it vetted to `pre-push-bar` and push-main reads that instead of its own `GOV_GATE_CMD_TEST`, and
  `gate-env.sh` is vetted before it is sourced, taking the review's "vet it" option over naming it
  an open class in the protocol, which this fold may not edit. The AC10 fixtures now commit their
  `gate-env.sh`, and the run-log suite's exit table counts three `bar-refused` sites. The class is
  recorded as `memory/gotchas/decision-re-derived-by-a-second-process.md`.

## 10. Reuse audit

The seams are inCMS's: the refusal writer `fail_push` at `.githooks/pre-push:100-110` there and its
reader at `scripts/push-main.sh:163-190` there; gov's own run-log decision vocabulary at
`.githooks/pre-push:254-287` supplies the token words. `tools/codebase-map/reuse_lookup.py` scans no
`.sh` and ranked only Python `resolve_*` helpers, so no existing seam in gov fits beyond those.

Recall terms used: `origin/HEAD GOV_DEFAULT_BRANCH remote pre-push-refusal token dirty ignore-submodules head-moved docs-only lander push-main`.
