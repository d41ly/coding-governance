# TOOL-aGraftedHelix-10 — a claim push names the remote, so the tracked pre-push hook observes its default branch and takes the non-default exit

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 2 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-1` pushes every claim to the push URL. Given a URL, the tracked pre-push hook
resolves no remote name, so it observes no default branch and falls back to `GOV_DEFAULT_BRANCH`.
Node `a` leaves that variable unset, so the hook refuses every claim push, every `--preflight`
refuses with check 91, and no unattended run can start. Unit 1's fixtures cannot see this, because a
`git clone --local` fixture runs no hook and the driver suite exports the variable. This unit pushes
the claim by the remote's NAME and observes the write through the tracked hook. It closes findings
38 (BLOCKER) and 31 (HIGH) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — `resolve_claim_remote` prints two TAB-separated fields: the name of the clone's one
  remote, which check 24 already admits, and that remote's push URL. `write_claim` pushes to the
  NAME. `read_claims` keeps fetching from the URL, which check 25 already proves names the same
  endpoint. Observed by AC1 and AC2.
- **S2** — The driver never supplies `GOV_DEFAULT_BRANCH` to a claim push. Where the remote's
  `HEAD` is not recorded locally and the variable is unset, the hook refuses with its
  `default-branch` token. That is a NOT COMPLETED write, so `--preflight` exits with check 91, never
  check 90, and leaves the tree untouched. Before every claim push the driver clears
  `<git-dir>/pre-push-refusal`, as `tools/push-main.sh` does before its own, and the message cites a
  token only when that file exists after the push. For the `default-branch` token the message also
  carries `git remote set-head <name> -a`, which the driver composes from the name S1 resolved,
  because the hook prints that line only to stderr and `observe_remote` discards stderr. Observed by
  AC3 and AC5.
- **S3** — The header comment of `write_claim` states the invocation and the hook branch it takes:
  by the remote's name, the hook observes `<name>/HEAD`, the pushed ref is not the default branch,
  and the hook exits `skip-nondefault` unless the repository declares `GOV_BRANCH_GATE_CMD`. That
  is the restatement unit 1's §3 "The pre-push hook" lacks. Observed by AC6.
- **S4** — `tools/unattended/unattended.test.sh` gains one claim block whose fixture sets
  `core.hooksPath` to the clone's tracked `.githooks` and runs with `GOV_DEFAULT_BRANCH` unset. It
  observes a create, a CAS update and the unset-`HEAD` refusal through the hook. NOT OBSERVED by a
  criterion here: the suite is the main loop's to run at VERIFYING, and each arm's red on a staged
  break is observed there (§7).
- **S5** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC4.
- **S6** — `memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md` gains this build's instance, so
  the documented check reaches a reviewer of a driver diff. A `git clone --local` fixture carries no
  `core.hooksPath`, and the driver suite exports `GOV_DEFAULT_BRANCH=main` for every arm, so a push a
  spec adds to the driver is observed through the tracked hook with that variable unset, and the
  spec names the invocation its claim about the hook's branch was measured with. The record names
  `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh` as backticked anchors.
  Observed by AC7.

## 3. Non-goals (OUT)

- **The pre-push hook.** It belongs to another kit, and its URL rule is a deliberate refusal to
  guess (`TOOL-aStandingWrit-4`). This unit changes the push, not the hook.
- **Exporting `GOV_DEFAULT_BRANCH` into the push.** That was the other option the audit named. The
  driver would then choose the name the hook classifies the push by, which is the environment
  fail-open `TOOL-aStandingWrit-4` closed (§8 F1).
- **Moving the read to the name.** A fetch runs no pre-push hook, so the URL read is not defective,
  and unit 2 relies on the read moving no remote-tracking ref.
- **The suite's other arms.** `tools/unattended/unattended.test.sh:477` exports
  `GOV_DEFAULT_BRANCH=main` for every arm; changing that default would re-ground arms this build
  does not touch. Only the claim block runs hook-wired. The round-1 audit's class gate for the
  fixture builder is declined for that reason, and S6's gotcha record is the documented check that
  replaces it.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `write_claim`, `read_claims`, `resolve_claim_remote`
  and the NOT COMPLETED class of §4 "The outcome of a write"; without them there is no claim push
  to re-route.

## 4. Design

### Evidence

- `resolve_remote_name` (`.githooks/pre-push:164-169`) treats any `$1` containing `/`, `\`, `:` or
  `@` as no name. A URL push therefore observes no `<name>/HEAD`.
- With nothing observed and `GOV_DEFAULT_BRANCH` unset, the hook writes a `default-branch` refusal
  and exits 1 (`.githooks/pre-push:413-420`), before its `skip-nondefault` exit at
  `.githooks/pre-push:905`.
- The skeptic of finding 38 reproduced both arms in a scratch clone wired to the tracked hooks. The
  URL push was refused with no `!` status line and exit 1. The same push to the remote name, with
  `origin/HEAD` set, landed as a new reference.
- `observe_anchor` (`tools/unattended/unattended.sh:1562`) already holds the remote's name as
  `rem`, and check 25 compares that name's fetch URL with its push URL.

### The invocation

```
git push --porcelain --force-with-lease=refs/gov/runs/<slug>:<observed sha> <name> <sha>:refs/gov/runs/<slug>
```

The hook receives `<name>` as `$1`, resolves it as a name, and reads `refs/remotes/<name>/HEAD`.
A clone made by `git clone` records that ref, so the observed default is set and the cross-check
against an unset environment value never fires. The pushed ref is under `refs/gov/`, so no pushed
line names the default branch, and the hook takes the `skip-nondefault` exit. A repository that
declares `GOV_BRANCH_GATE_CMD` runs its branch bar instead, which is unit 1's §5 residual.

### A clone with no recorded remote HEAD

A remote added by `git remote add` records no `<name>/HEAD`. The hook then refuses, and the write
is NOT COMPLETED by unit 1's rule. Check 91's message names the refusal token and
`git remote set-head <name> -a`. The hook prints that fix only to stderr
(`.githooks/pre-push:413-420`) and writes just `<token><TAB><why>` to the refusal file, so the
driver composes the line from the remote name it holds. A refusal here is honest: a run that cannot
publish its claim cannot be told from a second driver.

### The refusal file belongs to one push

The hook clears `<git-dir>/pre-push-refusal` only when it runs (`.githooks/pre-push:327-334`), and
git starts pre-push only after it has connected and matched refs. A claim push that cannot connect,
or times out first, therefore leaves whatever an earlier push wrote, such as `gate-red` from a
refused landing. `tools/push-main.sh` removes the file before its own push for that reason. The
driver does the same before every claim push, so a file present afterwards was written by this push's
hook, and a network failure is reported as NOT COMPLETED with git's exit and no token.

### Inventory

No new function, check, conf key or file. `resolve_claim_remote` changes its output from one field
to two. The new test block's fixture builder is local to that block. S6 extends an existing gotcha
record and mints none.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Export the anchor's observed default into the push's environment.** It passes the skeptic's
  probe. It loses on `TOOL-aStandingWrit-4`: the hook ruled an environment value a cross-check that
  may only refuse, and a driver that sets it is choosing the classifier's input. It also refuses
  outright where a stale local `<name>/HEAD` disagrees with the anchor's advertisement.
- **Push to the URL with `--no-verify`.** That is the declared bypass, banned in this repository's
  records and refused by the driver's own field checks.

## 5. Production-readiness checklist

- security — No new surface. The push reaches the same endpoint, and the hook keeps every check it
  had; this unit routes the push through the hook's named-remote branch instead of its URL refusal.
- perf / scale — No added spawn: `resolve_claim_remote` already read the remote, and the hook's
  `skip-nondefault` exit is the cost unit 1 §5 priced.
- error / empty / loading states — An unrecorded remote `HEAD` is check 91 with the hook's remedy,
  never check 90.
- observability — The hook's push journal records `skip-nondefault` for every claim push, and the
  refusal token names any refusal this push's hook wrote, never one left by an earlier push.
- risks — A repository that declares `GOV_BRANCH_GATE_CMD` runs that bar on every claim push. The
  hook hands it the `refs/gov/runs/<slug>` line on stdin, so it can skip one.
- testing — S4's hook-wired block, each arm observed RED on a staged break first.
- migration — None: no claim has been pushed before this unit lands.
- user docs — N/A: the invocation is internal, and unit 1's verbs entry is unchanged.

## 6. Acceptance criteria

The fixture is unit 1's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository beside it. Here it also runs `git config core.hooksPath .githooks`,
and every command runs under `env -u GOV_DEFAULT_BRANCH`.

- **AC1** — When `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id k1` runs in
  the hook-wired fixture, it exits 0, `git ls-remote <bare> refs/gov/runs/<slug>` lists the claim,
  no `pre-push-refusal` file exists in the fixture's git dir, and the newest line of the hook's
  `pushes.log` journal names the decision `skip-nondefault`.
  Red when: the push names the URL, so the hook writes a `default-branch` refusal and the preflight
  exits with check 91.
- **AC2** — When the holder then runs `--resume <slug> --keepalive-id k1` with the claim's
  `beat-utc` rewritten older than a quarter of `RESUME_STALE_BOUND`, the claim's `beat-utc` moves
  through the hooked CAS update and no `pre-push-refusal` file exists.
  Red when: the update is refused by the hook.
- **AC3** — When `git remote set-head origin -d` has run in the fixture, `--preflight` of a new slug
  exits with `UNATTENDED check 91 FAILED`, the message names `default-branch` and
  `git remote set-head origin -a`, and the fixture holds no run-state file for the slug.
  Red when: the refusal is reported as check 90, the record is created, or the driver supplies
  `GOV_DEFAULT_BRANCH` and the push lands.
- **AC4** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.
- **AC5** — When the fixture's git dir holds a `pre-push-refusal` file reading `gate-red`, and a
  `git` shim first on `PATH` makes `git push` exit 128 before any hook runs while passing every other
  call to the real git, `--preflight` of a new slug exits with `UNATTENDED check 91 FAILED`. Its
  message names neither `gate-red` nor `set-head`, and no `pre-push-refusal` file exists afterwards.
  Red when: the driver reads a refusal file it did not clear, so a network failure carries a stale
  token.
- **AC6** — When `grep -n -B20 '^write_claim()' tools/unattended/unattended.sh` runs at the pass's
  commit, the comment block that ends at the definition names `skip-nondefault`, `/HEAD` and
  `GOV_BRANCH_GATE_CMD`.
  Red when: the header does not state the hook branch the push takes. At base the driver holds none
  of the three, so the grep can fail.
- **AC7** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh
  tools/unattended/unattended.test.sh` runs at the pass's commit, its output names
  `fixture-lacks-a-gate-the-consumer-has`.
  Red when: the record carries no anchor on the driver's files, so a driver diff never selects it.
  figure: PINNED, measured on node `a` 2026-10-04 at `14e5f265`, where the same command selected 17
  anchored and 6 universal classes and not this one.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a hook-wired claim block with GOV_DEFAULT_BRANCH unset; stage the push target set back to the URL, and the remote HEAD deleted · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · a refusal file seeded with gate-red and a git shim failing the push before any hook runs; stage the driver's removal of the refusal file deleted · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs the block as a
slice, prologue plus that block, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

- **F1 — Does the claim push name the remote, or carry `GOV_DEFAULT_BRANCH` in its environment?**
  Both pass the skeptic's reproduction. The environment option makes the driver choose the branch
  name the hook classifies the push by, which `TOOL-aStandingWrit-4` ruled a fail-open shape. It
  also adds a refusal where a stale local `<name>/HEAD` disagrees with the anchor. Naming the remote
  uses the hook's own observation and adds nothing to it.
  RESOLVED (agent, 2026-10-04, delegated): the remote's name, as S1 states.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's findings 38 and 31,
  grounded against `.githooks/pre-push` and the driver at base `5266d22e`.
- rev-2 · 2026-10-04 · §3 §4 §5 §6 §7 · S2 S3 S6 · AC3 AC5 AC6 AC7 · folded the round-1 spec audit
  of units 10 to 15 on this unit: 25 (the driver removes the refusal file before every claim push
  and cites a token only from this push, §4 "The refusal file belongs to one push", AC5 and its
  arm); 29 (the driver composes `git remote set-head <name> -a`, AC3); 12 (S3's header comment is
  observed by AC6, not AC1); and 34 (S6 extends the fixture gotcha with this build's instance and
  anchors it on the driver's files, AC7).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "push a ref to the remote so the pre-push hook can
observe the default branch"` ranked name-stem neighbours only and printed `unscanned layers: .sh`,
so its miss is no evidence. The seams were read from source: `resolve_claim_remote` and
`write_claim` from unit 1's spec, `observe_anchor`'s remote name and check 25, and the hook's
`resolve_remote_name` and `skip-nondefault` exit. No existing seam fits a hook-wired fixture: the
driver suite exports `GOV_DEFAULT_BRANCH` for every arm. The recall probe returned
`TOOL-aStandingWrit-4`, the ruling that an environment-supplied branch name may only cross-check,
which decided §8 F1, and the round-1 audit record itself.

Recall terms used: pre-push default-branch GOV_DEFAULT_BRANCH remote name URL refusal resolve_remote_name tick session keepalive lease

The question passed with them: "why does the pre-push hook refuse a push to a URL when
GOV_DEFAULT_BRANCH is unset, and how does a scheduled tick get its session identity".
