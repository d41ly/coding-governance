# TOOL-dPlacedRequest-32 — an absent session is no identity: no consent, and no lease held on session alone

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 11 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-32-deviation-321.md](../build/2026-10-25-build-TOOL-dPlacedRequest-32-deviation-321.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 55 at HIGH**, its item **H8**. Neither `TOOL-dPlacedRequest-19` nor
`TOOL-dPlacedRequest-1` names where the session comes from or what happens when the harness exposes
none. The driver records `absent` then (`tools/unattended/unattended.sh:8884`), and `absent` passes
`TOOL-dPlacedRequest-19` S3's "letters, digits and dashes" shape. Any id-less session on the node then
passes `check_request_consent` for a request another id-less session typed, and two id-less sessions
on one node each read the other's lease as `mine` under `TOOL-dPlacedRequest-1` S6, which compares
fleet tag and session alone; today's claim test tolerates `absent` only because it also compares the
keepalive (`:2260`). The finder's fix, refusing every lease verb with no session, was judged unsound:
it breaks run claims the driver supports today. This unit builds the skeptic's corrected fix. It
repairs `TOOL-dPlacedRequest-19` and `TOOL-dPlacedRequest-1`, and is ordered after the later of them.

## 2. Scope (IN)

- **S1** — The source. The session is `CLAUDE_CODE_SESSION_ID`, read where both units read it; unset,
  empty and the literal `absent` are one value, no session. Observed by AC1 to AC4.
- **S2** — No session, no consent. `--request` with no session writes the record with `session:
  absent` as provenance and appends no `.typed` line; `check_request_consent` with no session returns 1
  printing `request — <key> · no session: the harness exposed none, so nothing here is consent`.
  Observed by AC1 and AC2.
- **S3** — No lease on session alone. In `TOOL-dPlacedRequest-1` S6's `lease` mode, a record is `mine`
  by fleet tag and session only when both sessions are present and equal; with either absent it is
  `mine` only through today's keepalive comparison, a keepalive present on both and equal, which a run
  claim carries and a step-checklist lease does not. Observed by AC4 and AC5.
- **S4** — A lease verb with no identity. `--lease <act>` run with no session and no keepalive prints
  `lease not written — no session: CLAUDE_CODE_SESSION_ID is unset and no keepalive identifies this
  holder` and exits 2, with nothing read or written. The driver's run claim, which carries the run's
  keepalive, keeps today's rules. Observed by AC3 and AC5.
- **S5** — The stops guide's section 7 (`tools/unattended/STOPS.template.md`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states S1, S3 and S4. Observed by AC6.

## 3. Non-goals (OUT)

- No refusal of a run claim for want of a session: the keepalive identifies a run's holder, as
  `check_claim_writable` does today (`:2260-2261`).
- No consent bound to bytes: `TOOL-dPlacedRequest-31`'s.
- No new identity source: a node with no session id and no keepalive takes no lease.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `--request`, its `.typed` file and `check_request_consent`, which this unit closes to an absent session; without them there is no consent to guard
- **consumes-from** `TOOL-dPlacedRequest-1` — the `lease` mode's `mine` test and the `--lease` verbs, which this unit keeps from matching on an absent session; without them there is no lease identity to guard
- **hands-off** `TOOL-dPlacedRequest-40` — S4's id-less refusal, which that unit scopes to the holder acts by name
- **hands-off** `TOOL-dPlacedRequest-43` — the identity rule and the refusal's order, which that unit's items for findings 16, 40 and 41 restate against the code and place after `RUN_CLAIMS`

## 4. Design

### Evidence

- `check_claim_writable` reads `me="${CLAUDE_CODE_SESSION_ID:-}"`; its `mine` row needs the keepalive
  and the session both equal (`tools/unattended/unattended.sh:2260`), and its `same session` row refuses
  `absent` (`:2262`).
- The record writes `absent` for an empty session (`:8884`), and the reap check reads an `absent`
  session as "the harness exposed none" (`:6267-6268`).

### The identity rule

```
session = CLAUDE_CODE_SESSION_ID; "" or "absent" -> none
mine(lease) = (session != none and record session != none and equal, and fleet tags equal)
              or (keepalive != absent and record keepalive != absent and equal)
--lease <act>, session none and keepalive absent -> exit 2, "no session"
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the `lease` mode's `mine` test, the `--lease` identity refusal,
  `--request`'s `.typed` append and `check_request_consent`
- `tools/unattended/unattended.test.sh`: the unset-session arms
- `tools/unattended/STOPS.template.md`: section 7
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Refuse every lease verb with no session.** It breaks run claims the driver supports under a
  harness that exposes no session (the skeptic's reading of finding 55).
- **Mint a node-local session id.** It would be a second identity a run-state file does not record.

## 5. Production-readiness checklist

- security — closes forged consent and shared holdership for id-less sessions; deny by default.
- perf / scale — none.
- error / empty / loading states — an id-less `--lease` is exit 2 naming the variable.
- observability — the two refusal lines name the cause.
- risks — a step checklist under a harness with no session id cannot take a lease; it names why.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-19`'s bare remote and clone, with a fixture `fleet.toml`.

- **AC1** — When `env -u CLAUDE_CODE_SESSION_ID bash unattended.sh --request req.md` runs, the remote
  record reads `session: absent`, `<git-common-dir>/requests/<key>.typed` gains no line, and a probe calling
  `check_request_consent <key>` in that environment returns 1 printing `no session`.
  Red when: an id-less session records or reads consent.
- **AC2** — When the same runs with `CLAUDE_CODE_SESSION_ID=absent`, the outcome is AC1's.
  Red when: the literal `absent` is read as a session.
- **AC3** — When `env -u CLAUDE_CODE_SESSION_ID bash unattended.sh --lease acquire build tFix` runs, it
  exits 2 printing `no session` and the origin is unchanged.
  Red when: an id-less, keepalive-less verb writes a lease.
- **AC4** — When a lease record carrying `session: absent`, `keepalive: absent` and this node's fleet
  tag is planted and a probe derives its class with the session unset, the class is a `foreign-`
  class, never `mine`.
  Red when: two id-less sessions share a lease.
- **AC5** — When `--preflight tFix` runs with the session unset and the run-state file's keepalive
  equal to the planted claim's, the claim is renewed as `mine`, as today.
  Red when: a run claim with a keepalive is refused for want of a session.
- **AC6** — When `grep -n 'CLAUDE_CODE_SESSION_ID' tools/unattended/STOPS.template.md` runs, section 7
  names it as the session source and states the absent rule.
  Red when: the guide omits the source.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the unset and `absent` session arms, staged against the session-only `mine` test and `.typed` append · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What is an id-less session allowed?** (a) A request record as provenance, no consent, no
  lease on session alone, a run claim through its keepalive; (b) nothing, every verb refused; (c) the
  same as a session, `absent` compared literally. (b) breaks run claims supported today; (c) is the
  defect. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 55 (HIGH, item H8).
- rev-2 · 2026-10-25 · promoted fix brief: AC1 writes the node-local `.typed` file with its
  `<git-common-dir>/` prefix, so it does not read as a repository path.
- rev-3 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-40, hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is the claim table's identity rows in `check_claim_writable`
(`tools/unattended/unattended.sh:2260-2262`), whose keepalive comparison this unit keeps as the
id-less path, plus the two units' new `lease` mode and consent predicate. `python
tools/codebase-map/reuse_lookup.py "session id absent when the harness exposes none"` ranked `absent`,
`extract_session`, `read_id_list` and `resolve_session_tree`, name stems only; the identity rows above
are the seam. `python tools/memory-recall/query.py "how is the session id recorded when the harness
exposes none"` returned TOOL-aGraftedHelix-20 and -18, whose specs set today's `absent` and
prior-session rules, and the audit's H8; none disagrees with source.

Recall terms used: CLAUDE_CODE_SESSION_ID absent session keepalive mine lease consent identity
