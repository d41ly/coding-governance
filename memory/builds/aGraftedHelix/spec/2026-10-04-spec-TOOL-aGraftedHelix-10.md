# TOOL-aGraftedHelix-10 — a claim push names the remote, so the tracked pre-push hook observes its default branch and takes the non-default exit

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 2 · ratified 2026-10-04

<!-- gen:spec-records -->

*No record names this unit.*

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
  check 90, and leaves the tree untouched. The message carries the token the hook left in
  `<git-dir>/pre-push-refusal` and the hook's own remedy, `git remote set-head <name> -a`.
  Observed by AC3.
- **S3** — The header comment of `write_claim` states the invocation and the hook branch it takes:
  by the remote's name, the hook observes `<name>/HEAD`, the pushed ref is not the default branch,
  and the hook exits `skip-nondefault` unless the repository declares `GOV_BRANCH_GATE_CMD`. That
  is the restatement unit 1's §3 "The pre-push hook" lacks. Observed by AC1.
- **S4** — `tools/unattended/unattended.test.sh` gains one claim block whose fixture sets
  `core.hooksPath` to the clone's tracked `.githooks` and runs with `GOV_DEFAULT_BRANCH` unset. It
  observes a create, a CAS update and the unset-`HEAD` refusal through the hook. NOT OBSERVED by a
  criterion here: the suite is the main loop's to run at VERIFYING, and each arm's red on a staged
  break is observed there (§7).
- **S5** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC4.

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
  does not touch. Only the claim block runs hook-wired.

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
`git remote set-head <name> -a`, the one-line fix the hook itself prints. A refusal here is honest:
a run that cannot publish its claim cannot be told from a second driver.

### Inventory

No new function, check, conf key or file. `resolve_claim_remote` changes its output from one field
to two. The new test block's fixture builder is local to that block.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
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
  refusal token names any refusal.
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
  `git remote set-head`, and the fixture holds no run-state file for the slug.
  Red when: the refusal is reported as check 90, the record is created, or the driver supplies
  `GOV_DEFAULT_BRANCH` and the push lands.
- **AC4** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a hook-wired claim block with GOV_DEFAULT_BRANCH unset; stage the push target set back to the URL, and the remote HEAD deleted · the suite's floor rises by its new arm count

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
