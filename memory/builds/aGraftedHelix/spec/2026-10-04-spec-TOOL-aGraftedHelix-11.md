# TOOL-aGraftedHelix-11 — a claim write copies its identity from the run's lease record, never from the writer's environment

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 2 · ratified 2026-10-04

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-1` writes `session: <CLAUDE_CODE_SESSION_ID, else absent>` into every claim. The
resume tick that runs `--beat` is launched by the OS scheduler and carries no such variable, so its
first due renewal rewrites a live claim to `session: absent`. The holder's next `--resume`,
`--dispatch` or `--close` then reads its own claim as foreign `live`, refuses with check 90, and must
`--abort claim-lost`. A Workflow child running `--dispatch` under another session id has the same
exposure. This unit makes every claim write after the one that takes the claim copy its identity
from the run's lease record. It closes finding 39 (BLOCKER) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — The identity a claim write carries is the identity the run's lease record holds once the
  call is done. `--preflight` and `run_takeover` take the claim, so they write the values they
  record into the lease, read from their environment as unit 1 has it. Every other writer copies
  `keepalive`, `session`, `host` and `lease-utc` from the record's lease facts in `RUN.md`. That
  covers the holder's renewals, the `--replaces` block, the LANDING re-bind, the status writes and
  `--beat`. `node` is copied from the claim on the `mine` row and read from the environment on the
  others. Observed by AC1 and AC2.
- **S2** — Renewal's "a field the write would set differs" compares the claim with those copied
  values. A writer whose environment names another session therefore makes no write due. Observed
  by AC2.
- **S3** — `write_claim_beat` reads the lease facts itself, on both the `none` row and the `mine`
  row, so the tick's call needs no identity argument. Observed by AC1.
- **S4** — The tick suite runs its `--beat` arm under `env -u CLAUDE_CODE_SESSION_ID`, the
  condition the OS scheduler gives it. The driver suite gains a `--dispatch` arm under another
  session id. NOT OBSERVED by a criterion here: the suites are the main loop's to run at
  VERIFYING, and each arm's red on a staged break is observed there (§7).
- **S5** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **The `mine` test.** It already compares the claim with the record's facts and reads no
  environment. It is unchanged.
- **The `same session` row.** It still reads `CLAUDE_CODE_SESSION_ID`, because recognising the
  holder's own restart is the one question only the environment can answer. It recognises; it
  supplies no identity to the write.
- **Giving the tick a session id.** The tick is not a Claude session, and inventing an id for it
  would be a second identity for one run.
- **A `node` fact in `RUN.md`.** The tick runs as the run's OS user, and the `mine` row copies
  `node` from the claim.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `write_claim`, `write_claim_beat`,
  `check_claim_writable` and the claim record's eight keys; without them there is no identity to
  copy.

## 4. Design

### Evidence

- Unit 1 §4 "The claim record" pins `session: <CLAUDE_CODE_SESSION_ID, else absent>`, and §4
  "Renewal" writes whenever a field it would set differs.
- `tools/unattended/resume-tick.sh` sets no `CLAUDE_CODE_SESSION_ID`; the variable appears nowhere
  in it. The tick only launches `claude -p --resume` itself.
- `tools/workflows/unattended-unit.js:147` has Workflow child agents run `--dispatch`, and nothing
  shows their session id equals the lease's.
- `write_lease` (`tools/unattended/unattended.sh:5557`) records `keepalive`, `session`, `host` and
  `lease-utc`, so every identity value a claim carries except `node` is already a lease fact.

### The rule

| writer | identity source |
|---|---|
| `--preflight`, `run_takeover` | the values the call records into the lease (its environment) |
| holder renewals at `--resume`, `--dispatch`, `--close` | the record's lease facts |
| the `--replaces` block, the LANDING re-bind | the record's lease facts as the call leaves them |
| `--hold`, `--landed`, `--abort` | the record's lease facts |
| `--beat`, on the `none` and `mine` rows | the record's lease facts |

The `--replaces` block decides `mine` against the facts as they stood before it, and writes the
facts it leaves. So the claim follows the record's new keepalive, and the next holder call reads
`mine` again.

### Inventory

No new function, check or file. `write_claim_beat` takes its identity from the record instead of
its caller.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/resume-tick.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **`--beat` alone copies identity.** It closes the tick's exposure and leaves the Workflow child's
  `--dispatch` writing its own session over the lease's.
- **The tick passes `--session-id` read from `RUN.md`.** It is a second reader of the same fact and
  a new argument, and every other writer would still read its environment.

## 5. Production-readiness checklist

- security — No new surface. The claim publishes the lease values the run branch already carries.
- perf / scale — One read of facts `RUN.md` already holds, inside calls that read it anyway.
- error / empty / loading states — A record whose lease facts are absent is the missing-record
  refusal `--beat` already makes.
- observability — `--claims` shows the lease's session for every renewal, whoever wrote it.
- risks — A take-over still takes identity from its environment. That is correct, because a
  take-over is the call that makes the claim this session's.
- testing — S4's arms, each observed RED on a staged break first.
- migration — None: no claim exists before unit 1 lands.
- user docs — N/A: the record's fields are unchanged.

## 6. Acceptance criteria

The fixture is unit 1's tick fixture: a run `--liveness` reads `LIVE` on this host, with its claim
on a bare remote seeded by real `gov-claim` messages.

- **AC1** — When `env -u CLAUDE_CODE_SESSION_ID bash tools/unattended/resume-tick.sh` runs over the
  fixture with the claim's beat older than a quarter of `RESUME_STALE_BOUND`, the claim's `session`
  equals the `session:` fact of the run's `RUN.md`. A following `--resume <slug> --keepalive-id <id>`
  under the lease's session exits 0 and prints no `UNATTENDED check 90 FAILED`. Run again with no
  claim on the remote, the created claim names the lease's `session`, `keepalive`, `host` and
  `lease-utc`.
  Red when: the claim reads `session: absent`, or the holder's resume refuses with check 90.
- **AC2** — When `--dispatch` runs for the fixture run's next pass with `CLAUDE_CODE_SESSION_ID` set
  to another session, as a Workflow child's is, and the claim's beat is due, it exits 0 and the
  claim's `session` still equals the lease's. With the beat not yet due, `git ls-remote <bare>
  refs/gov/runs/<slug>` prints the same sha before and after.
  Red when: the child's session lands in the claim, or a differing environment makes a write due.
- **AC3** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/resume-tick.test.sh · the LIVE row's --beat under env -u CLAUDE_CODE_SESSION_ID, over a seeded claim and over none; stage the session read back from the environment · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · --dispatch under another session id, beat due and not due; stage the identity read back from the environment · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its blocks as a
slice, and the main loop runs the suites once at VERIFYING.

## 8. Open questions

- **F1 — Where does a renewal on the `mine` row take its identity: from the claim it read, or from
  the record's lease facts?** The audit's corrected fix copies from the claim. The two agree on the
  `mine` row except after `--replaces`, where the record has moved and the claim has not. Copying
  from the claim would then write the old keepalive back, and the next holder call would read the
  claim as foreign. RESOLVED (agent, 2026-10-04, delegated): the record's lease facts, for every
  writer that does not take the claim.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's finding 39, grounded
  against unit 1's spec, `resume-tick.sh` and `write_lease` at base `5266d22e`.

## 10. Reuse audit

No existing seam fits beyond the lease record itself. `python tools/codebase-map/reuse_lookup.py
"push a ref to the remote so the pre-push hook can observe the default branch"` was run for this
set and ranked name-stem neighbours only, with `unscanned layers: .sh`. The seam extended is
`write_lease`'s record, read where unit 1 reads its facts for the `mine` test. The recall probe run
for this set returned `TOOL-aStandingWrit-4` and pre-push records, and no record that gives a
scheduled process a session identity.

Recall terms used: pre-push default-branch GOV_DEFAULT_BRANCH remote name URL refusal resolve_remote_name tick session keepalive lease

The question passed with them: "why does the pre-push hook refuse a push to a URL when
GOV_DEFAULT_BRANCH is unset, and how does a scheduled tick get its session identity".
