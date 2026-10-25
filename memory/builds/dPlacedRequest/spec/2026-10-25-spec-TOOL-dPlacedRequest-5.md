# TOOL-dPlacedRequest-5 — the `breakpoint` disposition: an owner's request for a review on a live build, fired through `review.trigger`

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 19 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0503@65f19d46 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

When the owner asks mid-build for a review, "audit the specs" say, the request is placed as a `breakpoint` on
that live build, the review it names is declared on the build and fired through `review.trigger` at its
position, and the build cannot pass that position without it. Today such a request is placed as `continue` and
dropped, and the build passes Design's exit with no spec audit, because no route turns the owner's words into
the trigger's witness (the whole-design audit's A1-F5, settled by the owner's FK-4-4,
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w4.md:109-115`).

## 2. Scope (IN)

- **S1** — The payload. A placement block (TOOL-dPlacedRequest-4 S4) whose `disposition:` is `breakpoint`
  carries `build: <slug>` and one more key, `breakpoint: <name>`, the name one of TOOL-dDeclaredLoop-19 S1's
  review breakpoints, `spec audit`, `gate review`, `closing review` or `landing review`, or `item <tag>` for an
  item boundary in the build's loop definition. `breakpoint` with no name, or a name outside those, is
  refused naming it. Observed by AC2.
- **S2** — The check, `check_breakpoint(block)` in `tools/loop/placement.py`, the function the `breakpoint` row
  of TOOL-dPlacedRequest-4's fact table calls: the build is live (`derive_status`,
  `tools/memory-tree/gen_build_index.py:793`, not in `TERMINAL`, orientation.md:161-162); an `item <tag>` names
  a tag the build's loop definition declares; and the request is the owner's, never relayed (S3). Each failed
  fact refuses as `placement.check` says. Observed by AC2 and AC3.
- **S3** — Provenance. `check_breakpoint` asks TOOL-dPlacedRequest-19's `check_request_consent <content key>`,
  the one consent predicate, through a read-only driver verb this unit adds,
  `bash tools/unattended/unattended.sh --request-consent <content key>`, which runs the predicate and exits its
  answer. A request this session did not type here, one that reached it by its record's id alone, answers 1,
  and `check_breakpoint` refuses it `relayed`: a relayed request is data with provenance and never consent.
  The check runs at placement, in the placing session, never at the later firing, whose session is the
  build's and did not type the request. Observed by AC3.
- **S4** — The declaration. `python tools/loop/placement.py breakpoint --request <content key>` writes, for a
  passed block, the owner's disposition record through TOOL-dDeclaredLoop-16 S4's door, `python
  tools/memory-tree/build_records.py new disposition --build <slug> --unit <first unit id> --item
  item.entry.place --disposition breakpoint --channel prompt`, its `Reason` `<name> · request <content key>`,
  in the build's `build/` folder of the session's own tree, for the session's commit. That record and the
  request record are the witness: the intake record's stand-in, TOOL-dPlacedRequest-19's request record, by
  the content key, and the placement disposition, by the record. The write needs the build's lease free or
  this session's, as `amend` does; a lease another session holds refuses `live-holder`, routed as
  flow-steps.md:56 says, until dKeptSession's mailbox carries the declaration to the holder. Observed by
  AC4.
- **S5** — The listing. TOOL-dDeclaredLoop-19 S1's `derive_breakpoints(policy, definition, build)` in
  `tools/loop/breakpoints.py` reads the build's `disposition` records whose `Item` is `item.entry.place` and
  `Disposition` is `breakpoint` and lists each as a placed breakpoint, cause `placement`, disposer the
  reviewer lens, at the position S2 of that unit gives the name, or at the named item's boundary. `--plan`
  prints it on its `breakpoint:` line (TOOL-dDeclaredLoop-19 S9). Observed by AC5.
- **S6** — The firing. A listed placed breakpoint fires through TOOL-dDeclaredLoop-20's
  `bash tools/unattended/unattended.sh --trigger <slug> --subject <s> --cause placement` (shared interface I22),
  never a new verb: at its position, as TOOL-dDeclaredLoop-19 S6 fires every review breakpoint; and at once,
  by `placement.py breakpoint`, when the build's newest transition record is already past that position. The
  subject is `<slug>-specs` for `spec audit`, the bare `<slug>` for `closing review` (the driver's subject
  rule at `tools/unattended/unattended.sh:11866-11869`), and the item tag otherwise. Observed by AC6.
- **S7** — The hold at Design's exit. A placed `spec audit` makes the pre-code audit owed: the driver's
  derivation in `check_authorization` (`tools/unattended/unattended.sh:3975-4041`, re-pointed by
  TOOL-dDeclaredLoop-19 S8) gains a third source, `placement`, set when the build's folder at the pinned BASE
  holds such a record, beside `readme` and `project` in `AUTH_SPEC_AUDIT_FROM` (`:1964-1968`), and
  `print_spec_audit_line` prints it. The source can only add an owed audit, never cancel one, so check 89's
  rule that a run never opts itself out is untouched. The build harness then holds the roster's hand-out until
  the audit's verdict is terminal, and `--close`'s specs-audited term is owed. Observed by AC1.
- **S8** — The fixture plants of §6, run by `python tools/loop/placement.py --fixture` under
  TOOL-dPlacedRequest-4's leg, the AC1 plant building a scratch repository with the driver copied in.
  Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- The `--trigger` verb, its causes and `review.blocks`: TOOL-dDeclaredLoop-20's, called by name.
- Where every other breakpoint sits, and owner gates: TOOL-dDeclaredLoop-19's `review.<stage>`, `autonomy` and
  `review.breakpoints`.
- The disposition record kind and its door: TOOL-dDeclaredLoop-16's.
- The intake record and the mailbox that would carry a declaration to another session's build:
  dWellOiledMachine's and dKeptSession's; S4 names the stand-in for each.
- The request record and its local text: TOOL-dPlacedRequest-19's; this unit reads where the text is held.
- An owner breakpoint, an owner gate the owner disposes: a review breakpoint is the clause's case, and
  `autonomy` places the owner's gates.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-4` — `disposition`, the placement record and the fact table whose `breakpoint` row calls `check_breakpoint`
- **consumes-from** `TOOL-dPlacedRequest-19` — `check_request_consent`, the predicate that refuses a relayed request, and the request record the witness names by its content key
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The flow

```
owner prompt "audit the specs" ──▶ scout return: disposition breakpoint · build dX · breakpoint spec audit
  place  ──▶ block (check: pending)
  check  ──▶ check_breakpoint: dX live · request held on this node · name known ──▶ check: pass
  placement.py breakpoint
     ├─ build_records.py new disposition … --disposition breakpoint --channel prompt   (dX/build/)
     └─ dX past item.design.reason?  yes ─▶ unattended.sh --trigger dX --subject dX-specs --cause placement
next preflight of dX at a BASE holding that record
     └─ AUTH_SPEC_AUDIT_FROM=placement ─▶ the audit owed: hand-out held, --close owes specs-audited
```

### Data model

The block of TOOL-dPlacedRequest-4 S4 gains one key for this disposition:

```
disposition: breakpoint
build: dLiveBuild
breakpoint: spec audit
reason: the owner asked for the specs to be audited before building
check: pass
```

The declaration's `Reason` field is `spec audit · request 3f9c2a7d01be`, so the record names the request by id
and carries none of its text.

### Inventory

| Minted | Kind |
|---|---|
| `check_breakpoint`, `write_breakpoint_declaration` | functions, `tools/loop/placement.py` |
| `breakpoint` | `placement.py` verb, and placement record key |
| `relayed` | `check` failed-fact word |
| `--request-consent` | read-only driver verb, `tools/unattended/unattended.sh` |
| `placement` | `AUTH_SPEC_AUDIT_FROM` value |
| `read_placed_breakpoints` | function, `tools/loop/breakpoints.py` |

Each function name is put to `python tools/lexicon/lexicon.py --suggest <name> --as py.function` in the build
pass.

### Migration

None. No build carries a `breakpoint` disposition record before this unit, so no build's owed audit moves at
landing.

### Rollout

Live at landing. The owed-audit source reads only records this unit writes, and a build that never receives
such a request derives exactly what it derived before.

### Files touched (estimate)

- `tools/loop/placement.py`: `check_breakpoint`, the `breakpoint` verb, the record key, the fixture plants
- `tools/loop/breakpoints.py`: `read_placed_breakpoints`, called by `derive_breakpoints`
- `tools/unattended/unattended.sh`: the `placement` source in `check_authorization`, its line in
  `print_spec_audit_line`, and the `--request-consent` verb
- `tools/unattended/VERBS.template.md`: the `--request-consent` line
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/unattended/PROTOCOL.template.md`: the spec-audit opt-in sentence names the third source
- `memory/guides/UNATTENDED-PROTOCOL.md`: its render
- `help/loop.md`: the placement section names the `breakpoint` disposition

### Alternatives rejected

- **A `review` verb on the owner's lifecycle command, or an owner-request record kind.** FK-4-4's options (B)
  and (C); the owner chose (A), the disposition, whose witnesses already exist.
- **Fire `--trigger` at once in every case.** A breakpoint before its position would run the review on a
  design not yet written; the clause fires it "at its position".
- **Write the `spec-audit:` README key.** Check 89 refuses a run writing it, and a slug-mode README is the
  owner's file.

## 5. Production-readiness checklist

- security — a relayed request cannot fire a review on another build (S3); the declaration names the request
  by id and holds no text.
- perf / scale — one record and at most one trigger per placement.
- error / empty / loading states — an unnamed breakpoint, an unknown item, a closed build, a relayed request
  and a lease held elsewhere each refuse by name.
- observability — the declaration is a committed record in the build's folder; `--plan` lists it; the
  preflight line names `placement` as the audit's source.
- risks — while dKeptSession's mailbox is unbuilt, an owner request for a build another session holds waits
  as contention and then becomes an owner item; the holder never sees it sooner.
- testing — the fixture plants of AC1 to AC6; the suite arms in §7 at the close.
- migration — none.
- user docs — `help/loop.md` names the disposition; the protocol names the third audit source.

## 6. Acceptance criteria

- **AC1** — When `python placement.py --fixture --plant audit-request` places the planted owner prompt "audit
  the specs" on a build in designing with no `spec-audit:` key and no `SPEC_AUDIT_DEFAULT`, and then runs
  `bash unattended.sh --preflight <slug>` in the scratch repository at the BASE holding the declaration, the
  preflight's spec-audit line names the source `placement` and the audit as owed.
  Red when: the prompt is placed as `continue`, or the record is not read, so the line says no audit is owed
  and the build passes Design's exit with no spec audit.
  fixture: built by the plant, a scratch repository with the driver copied in; the tree holds none today.
- **AC2** — When `python placement.py --fixture --plant breakpoint-unnamed` checks a `breakpoint` block with no
  `breakpoint:` key, and `--plant breakpoint-closed` one naming a CLOSED build, each refuses naming the fact.
  Red when: a breakpoint is declared with no position, or on a terminal build.
- **AC3** — When `python placement.py --fixture --plant relayed` checks a `breakpoint` block whose request has a
  record on the scratch remote and no `.typed` line for this session, it refuses `relayed`, and with the line
  planted it passes.
  Red when: a request known only by its record's id fires a review.
- **AC4** — When `python placement.py --fixture --plant declare` runs `breakpoint` on a passed block, the build's
  `build/` folder holds one `disposition` record whose `Item` is `item.entry.place`, `Disposition` is
  `breakpoint`, `Channel` is `prompt` and `Reason` names `spec audit` and the content key; with
  `--plant declare-held` the lease is another session's and it refuses `live-holder`, writing no record.
  Red when: the declaration is written into a build another session holds.
- **AC5** — When `python breakpoints.py --fixture --plant placed` lists a build carrying that record,
  `derive_breakpoints` returns a `spec audit` entry with cause `placement` after `item.design.reason`.
  Red when: the record exists and the listing omits it, so nothing fires at the position.
- **AC6** — When `python placement.py --fixture --plant past-position` declares a `spec audit` on a build whose
  newest transition record is in building, the stub driver in the fixture records one call
  `--trigger <slug> --subject <slug>-specs --cause placement`, and a build in designing records none.
  Red when: a breakpoint whose position has passed is declared and never fired.

## 7. Gates

`unattended protocol size` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/placement.py · covers AC2 AC3 AC4 AC6 · the `loop placement fixtures` leg's plants, its failing case staged by `relayed` with the provenance read removed · none
New arm: tools/loop/breakpoints.py · covers AC5 · TOOL-dDeclaredLoop-19's fixture plants, its failing case staged by `placed` with `read_placed_breakpoints` unhooked · none
New arm: tools/unattended/unattended.test.sh · covers AC1 · the preflight case whose build folder holds a placed spec-audit record, its failing case staged by dropping the `placement` source · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: `DRAFT` is
  not in the tuple. Liveness: the tuple would list it if the vocabulary admitted it. RESOLVED (agent,
  2026-10-25, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Where is the breakpoint "declared on that live build"?** Options: (a) the owner's disposition record
  of TOOL-dDeclaredLoop-16 S4 in the build's folder, read by `derive_breakpoints`; (b) a `review.breakpoints`
  entry in the policy file; (c) the `spec-audit:` README key. (b) is the owner's file, whose guard refuses an
  agent's write, and it is repository-wide; (c) is refused by check 89 and covers one breakpoint name.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, FK-4-4's "its witness is the intake record plus the
  placement disposition, so no new kind is needed". grants: PLAY-dClosedLoop-3 the placement source of the
  spec-audit opt-in in check_authorization and its sentence in tools/unattended/PROTOCOL.template.md and its
  render memory/guides/UNATTENDED-PROTOCOL.md · widens: none · relaxes: none
- **F3 — What makes a request relayed, and who decides it?** Options: (a) TOOL-dPlacedRequest-19's
  `check_request_consent`, called through a read-only driver verb; (b) a second reading of the node-local
  files in `placement.py`; (c) a provenance field on the request record. (b) is a second copy of one
  predicate; (c) is not in TOOL-dPlacedRequest-19's record, which pushes three fixed keys. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, reuse of the predicate unit 19 hands this unit by name.
  grants: PLAY-dClosedLoop-3 the read-only --request-consent verb and its line in
  tools/unattended/VERBS.template.md and its render memory/guides/UNATTENDED-VERBS.md · widens: none ·
  relaxes: none
- **F4 — A declaration on a build another session holds?** Options: (a) refused `live-holder`, waited for as
  contention, then an owner item, until the mailbox lands; (b) written anyway into this tree. (b) is a
  second writer on a leased build. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, flow-steps.md:56
  routing a live holder. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 5, the brief's shared interface I22, scout B's
  row for TOOL-dPlacedRequest-5, flow-steps.md:124 and :516-560, the fold brief's A1-F5 and the owner's FK-4-4,
  and TOOL-dDeclaredLoop-16, -19 and -20, read at base `c63aabbb`.
- rev-2 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seams are TOOL-dDeclaredLoop-20's `--trigger … --cause placement`, whose closed cause set already holds
`placement`, so this unit is a caller; TOOL-dDeclaredLoop-16 S4's disposition record and door for the
declaration; TOOL-dDeclaredLoop-19 S1's `derive_breakpoints` for the listing; and the driver's spec-audit
derivation in `check_authorization` (`tools/unattended/unattended.sh:3975-4041`) for the hold. `python
tools/codebase-map/reuse_lookup.py "fire a review breakpoint on a live build from an owner request"` ranked
only name stems (`live`, `build`, `build_commit`), and no trigger verb exists at base. Where the scout record
and source disagree: none. Scout B's `check_review_ended` is the predicate grep at
`tools/unattended/unattended.sh:12762`, inside `verb_review` (`:12669`) at base, and the name is the one
TOOL-dDeclaredLoop-20 gives it on extraction. `python tools/memory-recall/query.py "how does an owner request a review on a live
build"` returned scout B's row, the packet's Items 5 and the brief's row.

Recall terms used: breakpoint disposition review.trigger cause placement spec audit owner request live build witness intake
