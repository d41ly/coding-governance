# TOOL-dPlacedRequest-23 — a strict claim read stays strict: `leases.offline` never reaches the preflight, a take-over or the close

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 4 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-deviation-231.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-deviation-231.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 21 at HIGH**, its item **H3**. `TOOL-dPlacedRequest-1` §1 says an unreachable
remote "is only announced", but a `strict` claim read refuses: `read_claims` calls `fail 109` on the
`strict` policy and only `soft` announces (`tools/unattended/unattended.sh:2145-2147`), and
`--preflight` reads `strict` (`:7477`). That unit's S4 makes the driver's claim a build lease and its
S10 applies `leases.offline`, default `warn`, which queues the write and prints `queued`, with no
exception for the preflight. Two nodes cut off from the remote could then both preflight one slug
and learn of each other only when the queued pushes yield. This unit repairs `TOOL-dPlacedRequest-1`
by fixing which callers `leases.offline` governs: the `--lease` verbs and the soft and quiet claim
callers, never a strict read.

## 2. Scope (IN)

- **S1** — The strict callers keep check 109. `read_claims strict` refuses an unanswered read with
  `fail 109` and returns 1, as at `:2145-2147`, before any lease policy is read. Its four callers,
  `print_claims` (`:2202`), `--preflight`'s claim (`:7477`), `run_takeover` (`:9037`) and
  `verb_close` (`:10839`), never call `read_lease_policy` for `leases.offline`, never call
  `add_gov_queue`, and never build a lease commit after a failed read. Observed by AC1 and AC3.
- **S2** — `leases.offline` has one population. The value is read only by `run_lease_verb`, the
  `--lease` verb body `TOOL-dPlacedRequest-1` S5 adds, which reads the claims `quiet` and prints its
  own offline outcome, and by the `soft` and `quiet` callers of `read_claims` that write a lease;
  under every value of the key the strict callers behave as S1 states. Observed by AC2 and AC3.
- **S3** — The stops guide states the split. `tools/unattended/STOPS.template.md` section 7, rendered
  to `memory/guides/UNATTENDED-STOPS.md`, says in the `leases.offline` row that the key governs the
  `--lease` verbs and the soft and quiet claim callers, and that `--preflight`, a take-over and
  `--close` refuse with check 109 when the remote does not answer, whatever the key says. Observed by
  AC4.

## 3. Non-goals (OUT)

- No change to `leases.offline`'s three values or to the offline queue: both are
  `TOOL-dPlacedRequest-1`'s S10, and the queue's lock and idempotence are `TOOL-dPlacedRequest-24`'s.
- No change to which callers read `strict`, `soft` or `quiet`: the policy word each caller passes
  today stays.
- No rewrite of `TOOL-dPlacedRequest-1`'s §1 sentence: a spec this audit reviewed is not folded, and
  this spec's §1 records the correct fact.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — `run_lease_verb`, `read_lease_policy`, `add_gov_queue` and the `leases.offline` key, whose population this unit narrows; without them there is no offline branch to keep the strict callers out of
- **hands-off** `TOOL-dPlacedRequest-43` — the strict callers' split, which that unit's items for findings 3 and 37 observe by behaviour through `run_takeover`, `verb_close` and an `add_gov_queue` stub

## 4. Design

### Evidence

- `read_claims` takes `strict|soft|quiet` (`tools/unattended/unattended.sh:2118`); on a failed fetch the
  `strict` branch is `fail 109 "the claims on the remote could not be read …"` and `soft` echoes one
  line (`:2145-2147`).
- The strict callers, by `grep -n "read_claims strict"`: `:2202` (`print_claims`), `:7477`
  (`--preflight`), `:9037` (`run_takeover`) and `:10839` (`verb_close`). Every other caller reads
  `soft` (`:6381`, `:6632`, `:6768`, `:7051`, `:7192`, `:7619`, `:9253`, `:9340`, `:9431`, `:13970`) or
  `quiet` (`:2484`, the beat).

### The rule

```
read failed under strict  -> check 109, return 1; no policy read, no queue, no commit
read failed under soft    -> leases.offline decides: queue (warn), refuse (refuse), follow (follow-leases)
read failed under quiet   -> leases.offline decides, silently, as the beat already skips
--lease <act>, read failed -> leases.offline decides (TOOL-dPlacedRequest-1 S10)
```

The policy read sits in the lease writer's offline branch, which only a caller that passed `soft` or
`quiet`, or `run_lease_verb`, can reach. A strict caller returns at the refusal, so no code after it
needs a guard.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the offline branch's callers
- `tools/unattended/unattended.test.sh`: the strict-read arms
- `tools/unattended/STOPS.template.md`: section 7's `leases.offline` row
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **A `leases.offline` exception named in the preflight alone.** `run_takeover` and `verb_close` read
  strict for the same reason the preflight does; naming one caller leaves two.
- **Reading the key and overriding it for strict callers.** The value would be read only to be
  ignored, and a reader of the code would find a policy read whose answer is never used.

## 5. Production-readiness checklist

- security — the one-driver guarantee holds offline: a node that cannot read the claims starts no run.
- perf / scale — none: no new read or write.
- error / empty / loading states — an unreachable remote at the preflight is check 109, as today.
- observability — the refusal line is today's check 109 line.
- risks — a node with no remote cannot start an unattended run under any `leases.offline` value; that
  was true before this build and is the point of the strict read.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the unattended kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-1` AC7's: a scratch clone with a bare origin, `RUN_CLAIMS=on` and
a fleet user, the origin renamed away to make it unreachable.

- **AC1** — When the origin is renamed away and `bash unattended.sh --preflight tOff` runs under the
  default `leases.offline`, it exits non-zero printing `check 109`, `<git-common-dir>/gov-queue.log`
  is absent or unchanged, and `git for-each-ref refs/gov/` lists no ref the call made.
  Red when: the preflight queues a lease commit or exits 0, the planted case being a driver whose
  preflight claim reaches the `warn` branch.
- **AC2** — When `leases.offline` is planted `warn`, `refuse` and `follow-leases` in turn, the same
  `--preflight` exits non-zero printing `check 109` under each; and `--lease acquire build tOff`
  under planted `warn` still prints `queued`.
  Red when: a planted value changes the preflight's outcome, or the split removes the lease verb's
  queue.
- **AC3** — When an `awk` over `tools/unattended/unattended.sh` prints each function body that spells
  both `read_claims strict` and `add_gov_queue`, it prints nothing.
  Red when: a strict caller can queue a write, the planted case being a scratch copy whose
  `verb_close` calls `add_gov_queue`.
- **AC4** — When `grep -n 'check 109' tools/unattended/STOPS.template.md` runs, a line in section 7
  names `leases.offline` and the three strict callers.
  Red when: the guide still says an unreachable remote is only announced.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the preflight over an unreachable origin under each planted `leases.offline` value, staged by a scratch copy whose preflight claim reaches the `warn` branch · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Which callers does `leases.offline` govern?** (a) The `--lease` verbs and the soft and quiet
  claim callers, every strict read keeping check 109; (b) every lease write, the preflight included,
  as `TOOL-dPlacedRequest-1` S10 reads unqualified; (c) the `--lease` verbs alone. (b) is the defect
  finding 21 names; (c) leaves the run's own holder writes, which read `soft` today, with no offline
  rule at all. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 21 (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is `read_claims`' policy word (`tools/unattended/unattended.sh:2118`, the refusal at
`:2145-2147`) and its existing split of strict, soft and quiet callers; this unit adds no reader and
only keeps `TOOL-dPlacedRequest-1`'s offline branch behind the non-strict words. `python
tools/codebase-map/reuse_lookup.py "refuse a strict claim read when the remote cannot be reached"`
ranked `read`, `read_text`, `claims` and `read_conf`, name stems only; `read_claims` is the seam, read
at source above. `python tools/memory-recall/query.py "what does the preflight do when the claims
cannot be read"` returned scout A's row 1 of this build and the audit's finding table; neither
disagrees with source.

Recall terms used: preflight strict read_claims fail 109 offline queue leases.offline warn refuse claim remote
