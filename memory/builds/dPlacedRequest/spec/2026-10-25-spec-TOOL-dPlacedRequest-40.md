# TOOL-dPlacedRequest-40 — the id-less refusal gates the holder acts by name and lets every other lease act run

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 12 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-40-deviation-401.md](../build/2026-10-25-build-TOOL-dPlacedRequest-40-deviation-401.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 26 at HIGH**, its item **H3**, which holds no other finding.
`TOOL-dPlacedRequest-32` S4 refuses every `--lease <act>` with exit 2 when there is no session and no
keepalive, exempting only the driver's run claim. Acts that need no holder identity fall under it:
`--lease prune`, which dWellOiledMachine's supervisor runs headless (`TOOL-dPlacedRequest-16` S7),
`--lease flush` (`TOOL-dPlacedRequest-1` S10), `--lease fence` on its `fence — none` path
(`TOOL-dPlacedRequest-15` S2), and `TOOL-dPlacedRequest-34` S22's read-only `--lease status`. Run
tombstones are then never pruned, a sessionless flush never drains, and the lander's fence from a
terminal or CI exits 2 where exit 0 is promised. This unit repairs `TOOL-dPlacedRequest-32`, at order
11, so it sits at order 12: the refusal names the acts it gates, and every other act runs as its own
unit states.

## 2. Scope (IN)

- **S1** — The gated set. `TOOL-dPlacedRequest-32` S4's refusal applies to the holder acts `acquire`,
  `take-over`, `renew`, `release` and `offer` and to no other act; each of these writes a record
  naming its holder. Observed by AC4.
- **S2** — The exempt set. `prune`, `flush`, `fence` and `status` run with no session and no keepalive
  exactly as their units specify: `prune` writes no holder, `flush` pushes commits already built,
  `fence` reads the lease and answers `fence — none` or a refusal by its own `lease` mode, and `status`
  reads only. The two lists are one `case` in `run_lease_verb`, and an act on neither list is gated,
  so a new act is denied by default until it is named exempt. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- No order between this refusal and the `RUN_CLAIMS`-off answer: finding 41's, an item of
  `TOOL-dPlacedRequest-43`.
- No change to the refusal's line or exit code, or to the run claim's keepalive identity:
  `TOOL-dPlacedRequest-32`'s.
- No identity for the exempt acts: `fence` with no session holds nothing, so on a held lease it
  answers `TOOL-dPlacedRequest-15` S2's refusal, which is that unit's outcome, not this one's.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-32` — S4's id-less refusal of `--lease`, which this unit scopes to the holder acts; without it there is no refusal to scope
- **consumes-from** `TOOL-dPlacedRequest-16` — `--lease prune`, which AC1 runs with no session; without it there is no prune to exempt
- **consumes-from** `TOOL-dPlacedRequest-1` — `--lease flush` and the offline queue, which AC2 drains with no session; without them there is no flush to exempt
- **consumes-from** `TOOL-dPlacedRequest-15` — `--lease fence` and its `fence — none` path, which AC3 runs with no session; without it there is no fence to exempt
- **hands-off** `TOOL-dPlacedRequest-34` — `--lease status`, which that unit's S22 mints after this order and which joins the exempt set by name
- **hands-off** external — dWellOiledMachine's supervisor, which runs `--lease prune` headless with no session and is not refused
- **hands-off** `TOOL-dPlacedRequest-49` — the exempt `status` act, which that unit's item for finding 12 observes with no session

## 4. Design

### The act split

```
run_lease_verb <act> …
  case act:
    acquire | take-over | renew | release | offer   -> holder act: TOOL-dPlacedRequest-32 S4 applies
    prune | flush | fence | status                  -> no holder: run as its unit states
    *                                               -> holder act (deny by default)
```

### Evidence

- `TOOL-dPlacedRequest-32` S4 and its AC3, which runs `acquire` alone.
- The exempt acts' outcomes: `TOOL-dPlacedRequest-16` S7 (prune, exit 0 or `prune refused`),
  `TOOL-dPlacedRequest-1` S10 (flush), `TOOL-dPlacedRequest-15` S2 and its table (`fence — none`,
  exit 0), `TOOL-dPlacedRequest-34` S22 (status, read-only).
- Today's claim identity needs a keepalive and a session both equal for `mine`
  (`tools/unattended/unattended.sh:2260`); an exempt act never asks it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the act split in `run_lease_verb`
- `tools/unattended/unattended.test.sh`: the id-less act arms
- `tools/unattended/STOPS.template.md`: section 7 names the gated and exempt acts
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **List only the exempt acts and gate by elimination silently.** The same `case`, but a reader of S4
  could not tell which acts it reaches; both lists are written.
- **Exempt every act but `acquire`.** A `release` or `offer` with no identity would write a record
  naming no holder.

## 5. Production-readiness checklist

- security — deny by default: an unnamed act is gated.
- perf / scale — none.
- error / empty / loading states — an exempt act's own outcomes stand, `prune refused` included.
- observability — the gated refusal keeps `TOOL-dPlacedRequest-32` S4's line.
- risks — a future maintenance act is refused id-less until named exempt; the refusal names the act.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-32`'s bare remote and clone with `RUN_CLAIMS=on`, no run-state
file, and every call prefixed `env -u CLAUDE_CODE_SESSION_ID`.

- **AC1** — When a cadence `run` tombstone older than `leases.queued-claim-days` is planted and
  `bash unattended.sh --lease prune` runs, it exits 0 and the ref is gone from the remote.
  Red when: the prune is refused `no session`, the staged case being `TOOL-dPlacedRequest-32` S4's
  blanket refusal.
- **AC2** — When one line is queued in `gov-queue.log` with the origin reachable and
  `bash unattended.sh --lease flush` runs, it exits 0 and the queue is empty.
  Red when: the flush is refused `no session`.
- **AC3** — When no lease ref exists and `bash unattended.sh --lease fence build tFix` runs, it prints
  `fence — none` and exits 0.
  Red when: the fence exits 2.
- **AC4** — When `--lease acquire build tFix`, `take-over`, `renew`, `release --as withdrawn` and
  `offer … --to b` run in turn, each exits 2 printing `no session` and the remote is unchanged.
  Red when: a holder act escapes the gate, the staged case being a scratch copy whose exempt list
  names `release`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the id-less prune, flush, fence and holder acts, staged against the blanket refusal · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Which `--lease` acts does the id-less refusal reach?** (a) The five holder acts by name, the
  four others exempt by name, an unnamed act gated; (b) every act, as S4 reads; (c) `acquire` alone.
  (b) is the defect; (c) lets an id-less release or offer write. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound, with deny by default per the charter's
  `[security]` rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  26 (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-32` S4's refusal inside `run_lease_verb`, the `--lease` body
`TOOL-dPlacedRequest-1` S5 adds; no act dispatch exists at the base. `python
tools/codebase-map/reuse_lookup.py "exempt maintenance acts from an identity guard on a verb"` ranked
`leading_verb`, `load_affordance_exempt` and `check_verb_flag`, name stems only; none splits a verb's
acts. `python tools/memory-recall/query.py "which lease acts need a holder identity"` returned scout
A's row on the lease verbs, this audit's H3 and TOOL-aGraftedHelix-18 on the holder row's `mine`
test; none disagrees with source.

Recall terms used: lease act prune flush fence status acquire release renew take-over offer session keepalive identity refusal
