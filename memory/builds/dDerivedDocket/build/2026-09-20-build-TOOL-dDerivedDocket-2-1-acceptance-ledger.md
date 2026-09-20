# TOOL-dDerivedDocket-2 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-2

Every line below was observed in ONE scratch fixture, built and run in this pass outside the tree: a
bare remote, a primary tree with `main` checked out, a linked worktree on a run branch, a second
clone racing the remote, and `GOV_GATE_CMD` stubbed so no bar ran. It is the fixture route the
build brief sanctions and NOT the suite — `tools/push-main.test.sh` is a gate leg, unit passes run
none, and its own verdict is AC9's, owed to the VERIFYING run.

**Evidences:** TOOL-dDerivedDocket-2
- AC1 — `<def>` — fixture arm 12: with a commit of another build sitting unpushed on local `main`
  and NOT merged into the run branch, `--land` pushed and the bare remote's `main` afterwards equals
  the prepared merge T, while `merge-base --is-ancestor` on the remote shows the foreign sha is not
  reachable from it. Observed RED against break A, the push spelled as the local default branch the
  attended path pushes: arm 12b failed, the hook refusing a push whose ref is not this tree's HEAD.
- AC2 — `--land` — fixture arm 13: the run branch merged local `main` carrying
  `TOOL-zOther-4: another build unit again`; `--land` exited 1, named that sha and the build
  `zOther`, and the remote sha was byte-identical before and after. Observed RED against break B,
  the carry set computed as T minus local `main` (`comm -23` for `comm -12`): the refusal then named
  the merge commit instead of the foreign one and the arm failed.
- AC3 — `--prepare` — fixture arm 9: after `--prepare` the first parent is the sha
  `git ls-remote` advertised and the second is the old branch tip, the branch moved to the merge and
  is checked out. Arm 18: a branch reconciled instead with a plain merge of the fetched tip is
  refused by `--land`, and the refusal names `--prepare`. Observed RED against break C, the
  first-parent test disabled: arms 17 and 18 both passed a landing they must refuse.
- AC4 — `HEAD:refs/heads/<def>` — fixture arm 12: the same push issued by hand from the worktree
  without the marker is refused by the copied `pre-push`, and the one `--land` makes is accepted.
  The marker is written in the worktree's own git dir, which is what that hook reads; arm 12d shows
  it cleared afterwards.
- AC5 — `build_commit` — fixture arm 11, by hand as the criterion's `permission:` line allows:
  sourcing the unattended kit's library in the fixture worktree and asking `build_commit` for a unit
  of the fixture build over the pre-merge and post-merge windows returned the same commit,
  `82ab8a3c`, both times. Arm 9b is the property behind it — the merge subject
  `merge: tFix — land onto origin/main at <R8>` names the slug and no unit id at all.
- AC6 — `bash tools/push-main.sh --lnad` — fixture arm 21, run from the fixture's PRIMARY tree on
  `main`, which is where a fallthrough would actually publish something: it exited 2 and the remote
  sha was unchanged across the call. Arm 21b then ran the no-argument invocation there and it landed
  with BASE's own `landed main on origin`. Observed RED against break E, the unrecognised-argument
  arm shifted instead of exiting: the mistyped flag landed the local default branch at rc 0.
- AC7 — `GOV_PUSH_MAIN_MAX_RETRIES` — fixture arm 20: the stub advanced the remote from the racing
  clone while the gate ran, the push was rejected, `--land` re-prepared onto the newly advertised
  tip and landed on the second attempt, inside the default bound of 3. The merge made before the
  race is still an ancestor of what was finally pushed, checked with `merge-base --is-ancestor`.
- AC8 — `git merge <remote>/<def>` — fixture arm 19: with the racing clone and the run branch
  editing one file differently, `--prepare` exited 1, the branch sha was unchanged, HEAD was on the
  branch, `git status --porcelain` was empty, and the refusal named the reconcile to run first.
- AC10 — `--carry --slug tFix` — fixture arm 16: a single-parent records commit on top of the
  prepared merge is accepted and HEAD, not T, is what reaches the remote. Arm 17: a SECOND merge on
  top of it is refused and the remote does not move. Arm 13: `--carry` over arm 13's fixture exits 1
  naming the same sha `--land` names, because both call one function over one expression.
- AC11 — `--prepared --slug tFix` — fixture arms 10, 16, 17 and 18: its exit agreed with `--land`'s
  precondition verdict on all four shapes — prepared, records-commit-on-top, second-merge-on-top and
  plain reconcile — and arm 10 compared HEAD, the branch ref and `git status --porcelain` on both
  sides of the call to show it wrote nothing.
- AC12 — `memory/builds/tFix/` — fixture arm 14: a carry commit touching that folder and naming no
  unit id attributes to this build, `--carry` exits 0 and `--land` pushes. Arm 15: a carry commit
  naming no unit id and touching no build folder is printed as `unknown` and refuses. Both were RED
  under break B, which computes a set that can never hold either of them.
- AC13 — `GOV_DEFAULT_BRANCH` — fixture arm 22: with `origin/HEAD` deleted and that variable unset,
  `--carry` exits 3 and not 2. Arm 22b, over a HEAD carrying a prepared merge and with the default
  branch pinned, repoints `origin` at a path that does not exist: `--carry` and `--prepared` each
  exit 3 and the remote sha is unchanged across both. Observed RED twice — break F, which gives the
  undeterminable default branch exit 2, failed arm 22; break D, which gives the unreachable remote
  exit 2, failed arm 22b.

## What this ledger does NOT evidence, and why

AC9 is not observed here and no line above answers it. It grades the SUITE — that the arms for the
criteria above are present in `tools/push-main.test.sh` and pass, and that an attributed run of that
suite against BASE reads `verdict clean`. Its own `permission:` line defers both observations to the
VERIFYING run, the first to
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` because `push-main self-test` is a
HELD leg, the second to `bash tools/run-gates/run-selftests.sh --attribute <BASE>` beside it. Both
verbs are denied to a pass by `tools/unattended/gate-guard.js` before VERIFYING, and the owner rule
keeps gate legs out of a pass regardless. The orchestrator writes AC9's line after that run.

## The arms were written from the fixture, and the transcription is the residual risk

The twelve criteria above were observed by a fixture script, not by the suite. The suite's cases 9
to 22 are that script transcribed into `tools/push-main.test.sh` with its `ok`/`bad` helpers, its
`$tmp` layout and its `setup_repo`, which now takes the remote as a second argument so a second
bare remote can be built beside the first. Everything the transcription changed is named here so a
reader is not guessing: the fixture's `src/` files became flat `src-*.txt` files, the seed commit
moved after `setup_repo`, and case 11 LOCATES the kit library with `git ls-files` rather than
spelling a kit path, because this file ships to adopters who install at another prefix or carry no
such kit — where it announces a skip rather than passing quietly. What no pass can rule out is a
typo in that transcription; the run that catches one is AC9's, which is exactly what AC9 is for.
