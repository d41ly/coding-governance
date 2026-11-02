# TOOL-dTendedCadence-65 — the record push names its remote, reads the pre-push hook's refusal token, and states what the hook runs inside its bound

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-65-deviation-651.md](../build/2026-11-01-build-TOOL-dTendedCadence-65-deviation-651.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 26 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 5 (TOOL-dTendedCadence-64) and 37 (TOOL-dTendedCadence-66). Unit
49 §4 pushes with a bare `git push --porcelain --force` and names neither the push protocol
`write_claim` follows nor what the tracked pre-push hook does with a non-default ref. Given a remote
NAME the hook observes `<name>/HEAD` and exits `skip-nondefault`, or runs the branch bar a repository
declares as `GOV_BRANCH_GATE_CMD` (`.githooks/pre-push:1145-1166`); given a remote with no recorded
HEAD it refuses `default-branch` (`tools/unattended/unattended.sh:2370-2376`). In an adopter declaring a
branch bar, that bar runs inside unit 49's 30 s bound, the push is killed, and the walk exits 1 on
every wake. This unit states the protocol and makes each outcome name itself.

## 2. Scope (IN)

- **S1** — The push. Inside the lock TOOL-dTendedCadence-64 takes, `write_record_landing` clears
  `<git-dir>/pre-push-refusal`, then runs `git push --porcelain --force <name>
  <commit>:refs/gov/maintain-record/<key>` bounded at 30 s, `<name>` the remote NAME
  TOOL-dTendedCadence-68 resolves, never its URL. Its outcome is the porcelain status line for that
  ref, never the exit alone, as `write_claim` reads it (`unattended.sh:2423-2437`). Observed by AC1.
- **S2** — The refusal token. A status line flagged `!`, no status line, or a non-zero exit raises
  `maintain — refused: record push <key>: <git's reason or the exit>`, and where the refusal file
  exists its first TAB field is appended as `· the pre-push hook refused it: <token>`; the token
  `default-branch` appends `· fix once: git remote set-head <name> -a`. Observed by AC1.
- **S3** — The bound and the branch bar. The bound firing raises `maintain — refused: record push
  <key> killed by its 30 s bound`, and where `GOV_BRANCH_GATE_CMD` is set in the environment or in
  `.githooks/gate-env.sh` it appends `· a declared branch bar runs on this push; it receives the ref
  lines on stdin and may pass refs/gov/ lines through`. Observed by AC2.
- **S4** — The docs. The drift-audit README's maintenance record section states that the record push
  is a non-default ref push the tracked hook exits `skip-nondefault` on, that a declared branch bar
  runs on it inside 30 s, and that the remote needs `refs/remotes/<name>/HEAD`. Observed by AC3.

## 3. Non-goals (OUT)

- The lock and the lander's marker: TOOL-dTendedCadence-64.
- Which remote: TOOL-dTendedCadence-68.
- A longer bound or a policy key for it: §8 F1.
- `--force-with-lease`: the ref is content-addressed and moved only by a newer record, the deliberate
  difference from `write_claim` that TOOL-dTendedCadence-74 records in unit 49's citation (item L4).

### Edges

- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`'s push (S2) and its 30 s bound, whose protocol this unit states
- **consumes-from** `TOOL-dTendedCadence-64` — the held lock, inside which the refusal file is cleared and the push runs
- **consumes-from** `TOOL-dTendedCadence-68` — the remote name the push is made to
- **hands-off** `TOOL-dTendedCadence-66` — the refusal-token and default-branch cases, which that unit's fixture observes with the tracked hooks installed

## 4. Design

```
clear <git-dir>/pre-push-refusal
git push --porcelain --force <name> <commit>:refs/gov/maintain-record/<key>    (30 s)
line = the status line whose ref field is refs/gov/maintain-record/<key>
bound fired              -> raise S3
no line, or flag "!"     -> raise S2, + the refusal file's token where present
else                     -> pushed
```

The refusal file is cleared before the push, as `write_claim` clears it (`unattended.sh:2422`), so a
token read after the push came from this push's hook. That holds only inside the lock, which is why S1
runs there. The hook's non-default exit is `[ -z "$main_local" ] && ... exit 0` at
`.githooks/pre-push:1166`, below the branch bar at `:1145-1160`, so with no branch bar declared the
push is ungated and fast.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_push_refusal` | function, `maintenance.py`: the refusal file's first TAB field, or "" | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1 to S3
- `tools/drift-audit/selftest.py`: the cases of §6
- `tools/drift-audit/README.md`: S4

### Alternatives rejected

- **Push with the hook skipped.** The bypass flag is banned by the charter's landing rule, and the hook
  is the publishing boundary for every `refs/gov/` push.
- **Push to the remote's URL.** The hook then observes no default branch and refuses every push
  (`unattended.sh:2370-2376`).

## 5. Production-readiness checklist

- security — the push stays behind the tracked hook; nothing here skips or weakens it.
- perf / scale — one bounded push; with no branch bar the hook exits before any bar runs.
- error / empty / loading states — S2 and S3 each raise with one line naming the cause, and the walk
  exits 1 (unit 49 S4).
- observability — the raise carries the hook's own token, never a paraphrase of its output.
- risks — an adopter whose branch bar takes longer than 30 s and does not pass `refs/gov/` lines
  through fails every wake, named by S3's line; the remedy is in the bar the adopter owns.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no record push exists at base.
- user docs — the kit README, S4.

## 6. Acceptance criteria

The fixture is TOOL-dTendedCadence-66's: unit 49's scratch repository with the tracked `.githooks` as
`core.hooksPath` and `refs/remotes/<name>/HEAD` recorded.

- **AC1** — When `write_record_landing` runs in the fixture, the ref lands on the bare remote; with
  `refs/remotes/<name>/HEAD` deleted it raises a line carrying `default-branch` and `git remote
  set-head`, and no ref is pushed.
  Red when: a hook refusal is reported without its token, or a push to a URL is made.
- **AC2** — When `GOV_BRANCH_GATE_CMD` names a stub that sleeps past the bound, the call raises a line
  naming the 30 s bound and the branch bar; with a stub that exits 0 at once, the ref lands.
  Red when: a killed push raises a line that does not name its cause.
- **AC3** — When `grep -n "skip-nondefault" README.md` runs in `tools/drift-audit/`, it matches inside
  the maintenance record section.
  Red when: the page leaves the hook's behaviour on this push unstated.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · the tracked hook installed, a deleted remote HEAD and a slow and a fast branch-bar stub, staged against a bare push that reads no token · none

## 8. Open questions

- **F1 — A declared branch bar slower than the 30 s bound?** Options: (a) keep 30 s and name the
  cause, the bar receiving the ref lines so it can pass `refs/gov/` lines through; (b) a policy key for
  the bound; (c) a longer fixed bound when a branch bar is declared. (b) adds a public surface, veto 2.
  (c) holds the claim-push lock longer, which the lander waits on, for every adopter declaring a bar.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the survivor that widens nothing; the hook's
  own header says a branch bar receives git's ref lines (`.githooks/pre-push:1141-1142`). widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 26 (HIGH, item H2) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

The seam is `write_claim`'s push protocol (`tools/unattended/unattended.sh:2370-2437`): push by remote
name, clear the hook's refusal file first, decide on the porcelain status line, and append the hook's
token. This unit ports that protocol for one more ref class. `python tools/codebase-map/reuse_lookup.py
"push a ref under refs/gov and read the pre-push refusal token"` ranked name stems only, `read`,
`read_text`, `pre`, `refusal` and `Refusal`, none a pusher; the protocol's one implementation is shell
(`write_claim`, `observe_remote` at `unattended.sh:480`), which the copy-installed kit cannot call, so
no existing seam fits beyond the protocol.

Recall terms used: `python tools/memory-recall/query.py "what does the pre-push hook do with a push of
a non-default ref" --terms "pre-push hook skip-nondefault branch bar GOV_BRANCH_GATE_CMD refusal token
default-branch remote set-head porcelain"`
