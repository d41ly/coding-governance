# TOOL-dDerivedDocket-2 — in-place landing merge

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/push-main.sh` lands only from the primary tree with the default branch checked out
(`tools/push-main.sh:63-67`), and it pushes the node's whole local default branch
(`tools/push-main.sh:95`), which every build on the node shares. A run may never be on the default
branch, so every mandated landing has to leave the run's own tree, and a landing can publish another
build's unpushed commits. Give the lander flags that make the landing merge IN PLACE, in the run's
own worktree, onto the tip the remote advertises, push exactly that merge, and refuse to publish
another build's commits. The attended no-flag path is unchanged, by the brief's binding note on
D12-i1.

## 2. Scope (IN)

- **S1** `--prepare --slug <slug>`, run in the run's worktree on branch B. It observes the remote's
  advertised tip R, makes a `--no-ff` merge of B onto R whose subject names the slug and no unit
  id, and moves B to that merge T. Observed by AC3 and AC5.
- **S2** On a merge conflict, `--prepare` restores B to its old tip, leaves HEAD on B with a clean
  tree, and refuses naming the manual reconcile. Observed by AC8.
- **S3** `--land --slug <slug>` refuses unless HEAD carries a prepared merge T: T is HEAD, or T is
  reached from HEAD through single-parent commits only, and T's FIRST parent is the tip the remote
  advertises now. The single-parent tail is where the landing path commits its close records.
  Observed by AC3 and AC10.
- **S4** `--land` computes the carry set — the commits the push would publish that rode in through
  local `<def>` — and refuses when any of them belongs to another build, naming each sha, its
  subject and its derived build. Observed by AC2.
- **S9** `--carry --slug <slug>` prints the same carry set and exits 1 when it holds a foreign
  commit, 0 when it does not, and never writes, fetches beyond one observation, or pushes. It is the
  one spelling of the predicate, so the driver's close can ask it rather than re-implement it.
  Observed by AC10.
- **S5** Otherwise `--land` writes the lander marker in THIS worktree's git dir and pushes
  `HEAD:refs/heads/<def>`, never local `<def>`. The LANDER_MARKER record is written exactly as the
  attended path writes it. Observed by AC1 and AC4.
- **S6** On a push rejected as a race, `--land` re-prepares onto the newly advertised tip and
  retries, bounded by `GOV_PUSH_MAIN_MAX_RETRIES`. Observed by AC7.
- **S7** An unrecognised argument refuses with exit 2 and pushes nothing. The no-argument invocation
  behaves exactly as at BASE. Observed by AC6.
- **S8** `tools/push-main.test.sh` gains one arm per criterion, over a scratch repository with a
  local bare remote and a linked worktree. NOT OBSERVED during the unit pass: the suite is a gate
  leg, and unit passes run no gate legs by owner rule; the one post-build bar grades it (AC9).

## 3. Non-goals (OUT)

- The unattended driver's use of these flags: `LANDER_MODE`, the three-step Land section, the
  prepared-merge bar and `--close` committing on T are the landing-path unit's.
- Any change to `.githooks/pre-push`. The in-place shape was chosen so the hook that adopters
  receive verbatim stays untouched, and the lab showed it already accepts this push shape.
- Deriving LANDED from the advertised tip, and `--landed`'s refusal of the local arm in in-place
  mode. Both belong to the derived-terminal unit.
- Offering the carry-set check to the attended path as an opt-in flag. D12-i3's consequences name
  it as a possible follow-up; the brief binds the attended path unchanged, so it is not built here.
- Pull-request landing, and any GitHub setting. The build's non-goals exclude both.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — the "no NEW FAIL" reading of the held push-main
  suite at the post-build bar, so a red there is attributed against BASE before it is called this
  unit's.
- **hands-off** `TOOL-dDerivedDocket-3` — the three flags, their refusal texts and the
  prepared-merge shape, which the run's landing path calls from the Skill, grades at `gates-green`
  and asks through `--carry` at `--close`.

## 4. Design

### Data model

The prepared merge T is defined by three facts, and `--land` re-derives all three rather than
trusting a file:

| Fact | Derivation |
|---|---|
| T is the prepared merge | walking HEAD's first-parent chain, the first commit with two parents; every commit passed on the way has one |
| T^1 is the advertised tip | `git ls-remote <remote> refs/heads/<def>` equals T^1 at the moment `--land` runs |
| T carries B | T^2 is the branch tip that `--prepare` merged, and B contains T |

The merge subject is `merge: <slug> — land onto <remote>/<def> at <R8>`. It names the slug so a
reader can place it, and no unit id, because `build_commit` in `tools/unattended/lib-unattended.sh`
joins a commit to a unit by the unit id as a whole token in the subject. A unit id there would make
the pass-order history leg grade the landing merge as that unit's build commit.

### `--prepare --slug <slug>`

1. Resolve `def` and `remote` exactly as the attended path does, including `GOV_DEFAULT_BRANCH` and
   `GOV_REMOTE`. Refuse on the default branch, on a detached HEAD and on a dirty tree, reusing the
   attended path's dirty-tree message.
2. Observe R by advertisement, `git ls-remote`, then `git fetch <remote> <def>` so R's object is
   present. Refuse when the fetched ref and the advertisement disagree, which is a race between two
   reads, and say so.
3. Idempotent: when HEAD is already a merge whose first parent is R and whose second is the previous
   B tip, print T and exit 0.
4. `git checkout --detach R`, then `git merge --no-ff <B> -m <subject>`.
5. On success, move B with `git update-ref refs/heads/<B> <T> <old-B>`. The compare-and-swap form
   refuses if B moved underneath, which a plain `branch -f` would not notice. Then check B out.
6. On conflict, `git merge --abort`, check B out at its old tip, and refuse naming
   `git merge <remote>/<def>` as the reconcile to do on B before preparing again. Exit 1.
7. Print `push-main: prepared <T8> — first parent <R8> (the advertised tip) · second parent <old8>`.

Neither flag reads or writes local `<def>`, except that `--land` READS it for the carry set.

### `--land --slug <slug>`

1. Precondition S3. A plain `git merge <remote>/<def>` on B produces a merge whose first parent is
   the old branch tip, so it fails this test and the refusal names `--prepare`. A second merge on
   the tail between T and HEAD also fails it, because the tail may hold only single-parent commits.
2. The carry set. C is the set of commits reachable from HEAD and from local `<def>`, and not from R:

   ```
   C = rev-list HEAD --not R   ∩   rev-list refs/heads/<def> --not R
   ```

   `--carry` runs exactly this step and stops, printing the members and exiting 1 on a foreign one.

   These are the commits that entered B through a merge of local `<def>` and that the push would
   publish. Each is attributed to a build by the first unit id in its subject, else by the
   `<memory-root>/builds/<slug>/` folders it touches, else `unknown`. A member whose build is not
   `<slug>` refuses the landing, naming the sha, the subject and the build; `unknown` counts as
   foreign. A commit of this build that reached local `<def>` by some attended act is not foreign.
3. `touch "$(git rev-parse --git-dir)/push-main-active"`. In a linked worktree that is the
   worktree's own git dir, which is the one the pre-push hook reads; the lab arm Q showed the hook
   refuses the same push without it.
4. `git push <remote> HEAD:refs/heads/<def>`, classified as `race`, `unreachable` or `red` by the
   attended path's own classifier, unchanged.
5. On success, write LANDER_MARKER exactly as the attended path does: resolved against the git
   common dir, carrying the pushed commit, and reported when the write fails.
6. On `race`, go back to `--prepare`'s steps 2 to 6 against the newly advertised tip, then repeat
   the carry set and the push, bounded by `GOV_PUSH_MAIN_MAX_RETRIES`.

### Why re-prepare on a race, and not merge the new tip into B

The design record's race text says to merge the new tip INTO B, the attended reconcile shape. That
produces a merge whose first parent is T and whose second is the new tip, which step 1 of `--land`
then refuses, and which demotes the commits the remote gained to a second parent on the default
branch's first-parent line. Re-preparing keeps the invariant on every attempt. The already graded
merge T stays an ancestor of what is pushed, which is the property the lab arm measured, and the
pre-push hook's own lag bound decides whether a fresh full bar is owed. This is a divergence from
the design record's wording and is recorded in §9.

### Argument parsing

The script accepts no arguments at BASE and ignores any it is given. A mistyped `--land` would
therefore run the attended path, which pushes local `<def>` — the exact hazard this unit exists to
remove. So any argument other than the three flags and their `--slug` refuses with exit 2. That is
the one observable change to the no-flag contract, and it only affects an invocation that passed
something.

### Files touched (estimate)

`tools/push-main.sh` · `tools/push-main.test.sh` · the push-main entry's runbook wording if it
quotes the usage line.

### Alternatives rejected

- A lander-owned lane worktree with the full-green stamp moved to the common dir (D12-i1 option b).
  The owner ruled for (a); it also splits the graded merge and the stamp into two git dirs, which is
  what makes the push reuse the run's green.
- The primary-tree lander only (D12-i1 option c). It keeps local `<def>` as a staging ref, which is
  the root cause of the foreign-commit landings.
- Computing the carry set as T minus local `<def>`. It excludes exactly the commits that rode in
  through local `<def>`, so it can never name one.

## 5. Production-readiness checklist

- security — the push surface is unchanged: one ref, the default branch, through the existing hook.
  The new refusal narrows what a landing may publish. No input beyond a flag and a slug token,
  which is validated against the slug grammar before it reaches a commit message.
- perf / scale — one `ls-remote` and one fetch per attempt, plus two bounded `rev-list` calls over
  the landing range.
- error / empty / loading states — dirty tree, detached HEAD, default branch, a conflict, a stale
  advertisement, a foreign carry and exhausted retries each refuse with a distinct message.
- observability — every flag prints the shas it acted on, and the carry refusal lists every
  member with its build.
- risks — `update-ref` with an old value refuses a concurrent move of B; the lock a sibling session
  may hold on the index is not this unit's to break, and a refusal says which ref.
- testing — `tools/push-main.test.sh` arms over a scratch repository, a bare remote and a linked
  worktree, with `GOV_GATE_CMD=true` so no real bar runs. Each arm observed RED before it lands.
- migration — none. Adopters receive the flags through their own deployer builds.
- user docs — the usage block at the head of the script.

## 6. Acceptance criteria

- **AC1** — When local `<def>` carries an unpushed foreign commit and the fixture worktree runs
  `bash tools/push-main.sh --land --slug tFix`, the bare remote's default branch afterwards equals T
  and the foreign sha is not reachable from it.
  Red when: the push names local `<def>` as the attended path does, so the foreign sha lands.
  fixture: a scratch repository with a bare remote and a linked worktree, built by the test.
- **AC2** — When B has merged local `<def>` carrying a commit whose subject names another build's
  unit id, `--land` exits 1, names that sha and that build, and the remote is unchanged.
  Red when: the set is computed as T minus local `<def>`, which excludes exactly that commit.
- **AC3** — When `--prepare` has run, T's first parent is the advertised tip and its second is the
  old branch tip; when B was instead reconciled with a plain `git merge`, `--land` refuses and names
  `--prepare`.
  Red when: `--land` accepts any two-parent HEAD.
- **AC4** — When the fixture pushes `HEAD:refs/heads/<def>` from the worktree without the marker,
  `.githooks/pre-push` refuses; when `--land` pushes the same commit, the hook accepts it.
  Red when: `--land` writes the marker in the git common dir, so the worktree's hook refuses the
  lander's own push.
- **AC5** — When `build_commit` from `tools/unattended/lib-unattended.sh` is asked for each unit of
  a fixture build before and after `--prepare`, it returns the same commit per unit.
  Red when: the merge subject names a unit id, so the landing merge becomes a unit's build commit.
  permission: observed by hand in the scratch fixture, because the unattended suites are not this
  unit's to run.
- **AC6** — When `bash tools/push-main.sh --lnad` runs, it exits 2 and pushes nothing; when the
  fixture's primary tree runs it with no argument, the push and its messages match the BASE script.
  Red when: an unrecognised argument falls through to the attended path, which pushes local `<def>`.
- **AC7** — When the remote advances between `--prepare` and the push, `--land` re-prepares onto the
  new tip, lands within `GOV_PUSH_MAIN_MAX_RETRIES`, and T remains an ancestor of the pushed commit.
  Red when: the retry merges the new tip into B, which the precondition then refuses.
- **AC8** — When `--prepare` meets a conflict, B's sha is unchanged, HEAD is on B, the tree is
  clean, and the message names `git merge <remote>/<def>`.
  Red when: the abort path leaves HEAD detached at R or B pointing at a half merge.
- **AC9** — When the post-build bar runs `tools/push-main.test.sh` with the self-tests included, the
  arms for AC1 to AC8 and AC10 are present and pass, and `run-selftests.sh --attribute` against BASE
  reports no NEW failure for that suite.
  Red when: an arm was wired without its failing case having been observed.
  permission: the suite is a gate leg, so only the one post-build bar runs it.
- **AC10** — When a single-parent records commit sits on top of T, `--land` accepts it and pushes
  HEAD; when a second merge sits there, `--land` refuses; and `--carry --slug tFix` over AC2's
  fixture exits 1 naming the same sha that `--land` names, while writing nothing.
  Red when: `--carry` re-derives the set by a different expression than `--land` uses, so the two
  can disagree about one landing.

## 7. Gates

`push-main self-test` · `pre-push self-test` · `pass-order history` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/push-main.test.sh` · a scratch repository with a bare remote, a linked worktree and a foreign commit on local main · none

## 8. Open questions

- **F1 — on a race, re-prepare, or merge the new tip into B as the design record says?** Merging
  into B yields a merge whose first parent is not the advertised tip, which `--land`'s own
  precondition refuses, and it demotes the remote's new commits on the first-parent line.
  Re-preparing keeps the invariant and keeps T an ancestor of the push.
  RESOLVED (agent, 2026-09-14, delegated): re-prepare; recorded as a divergence in §9.
- **F2 — is `--slug` required, or derived from the branch name?** A branch name is free text in
  this repository and deriving a slug from it is a guess; both the subject and the carry set's
  own-build exemption need the real value.
  RESOLVED (agent, 2026-09-14, delegated): required on every flag, validated against the slug
  grammar.
- **F3 — the D12-i1 landing shape.** RESOLVED (owner, 2026-09-13): in place on the run's branch,
  D12-i1 option (a).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Diverges from the design record's U18 race wording under F1:
  a race re-prepares onto the new tip instead of merging it into B. Adds `--carry`, which the
  record does not name, because its U19 runs the carry refusal at `--close` as well and one
  predicate must have one spelling. Admits a single-parent tail on T, because U19 commits the close
  records on T before `--land` runs.

## 10. Reuse audit

- The seam is `tools/push-main.sh` itself: its default-branch resolution, dirty-tree refusal, push
  classifier, retry bound and LANDER_MARKER write are all reused unchanged, and the three flags are a
  second entry into the same file. The pre-push hook is reused without an edit. The probe
  `reuse_lookup.py "land a merge onto the remote default branch tip and push it"` returned only
  name-stem candidates, and its coverage line reads `unscanned layers: .sh`, so the lookup is blind
  to the shell lander and its hook; that blindness is recorded rather than retried. Recall returned
  TOOL-aPacedTurnstile-15, the row this unit and the landing-path unit answer together, and the
  aHoistedPass landing record where local main had diverged by another build's thirteen commits.
  Where the design record and the source disagree: the hook's marker and head checks sit a line or
  two from the record's citations at BASE; the behaviour is as described.
- M12 was not reached: the design record tested this shape in a lab (arms P, Q, R, S and F) and the
  owner ratified it.
- Recall terms used: `push-main lander in-place landing merge remote-tip carry-set foreign-commit
  pre-push marker full-green-stamp reconcile local-main`
