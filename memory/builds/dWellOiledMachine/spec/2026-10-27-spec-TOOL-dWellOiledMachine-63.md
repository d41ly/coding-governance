# TOOL-dWellOiledMachine-63 — the record door's node writer: a sessionless coordination write admitted for this node's own records

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 27 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-63-deviation-631.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-63-deviation-631.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 1, item B1, at BLOCKER. TOOL-dWellOiledMachine-58 S1 refuses every coordination write that
carries no `CLAUDE_CODE_SESSION_ID`, and the node tick and the supervisor carry none, so from that
unit on every supervisor beat, cadence lease, wait wake, hand-over and pick-and-claim is refused
`no-session`. This unit gives the door one more writer, the node writer, admitted only for records
that name this node's fleet tag and either no session or the session of the run this host holds:
the reach `check_claim_writable`'s `mine` row grants the tick today, and no more.

## 2. Scope (IN)

- **S1** — The door's argv carries the node. `tools/unattended/unattended.sh`, where it sets
  `GOVREF_DOOR` once (TOOL-dWellOiledMachine-58 S2), appends `--node <tag> --memory <root>`: `<tag>`
  from `resolve_fleet_tag` (TOOL-dPlacedRequest-1 S11), the reader the lease mode's `mine` row compares
  with, and `<root>` the memory root the driver already holds as `$M`. A node with no fleet row gets no
  `--node`, and the block inside `write_gov_ref` stays byte-identical in its three carriers, since
  only the array's value changes. Observed by AC1, AC5.
- **S2** — The node writer, `read_node_writer(ref, node, memory)` in
  `tools/memory-tree/gov_record.py`, used by `check_writer_binding` when `CLAUDE_CODE_SESSION_ID` is
  unset or empty. It returns the writer `(sessions, node)`: `node` is the `--node` tag, and
  `sessions` is the literal `absent` plus, where `<ref>` names a slug whose run-state file
  `<memory>/builds/<slug>/RUN.md` exists with a `## Run facts` `host:` equal to this host (the
  lowercased `COMPUTERNAME` or host name, `read_host_name`'s rule, `tools/unattended/lib-unattended.sh:528`),
  that file's `session:` fact. With no `--node` it returns none and the door refuses `no-session`
  as today. Observed by AC1, AC2, AC5.
- **S3** — The rules read the node writer as a writer. TOOL-dWellOiledMachine-58 S3's write rule
  admits a node writer's lease, run or request write when the record's `fleet-tag`, where it carries
  one, is `node`, and its `session` is one of `sessions`; a mail write when the ref's `<fleet tag>` is
  `node`, its `<segment>` is `derive_ref_segment` of one of `sessions`, and the message's `from-tag`
  and `from-session` name the same. S4's tombstone rule (a) admits a node writer when the tip read's
  `fleet-tag` is `node` and its `session` is one of `sessions`; (b) and (c) are unchanged. Any other
  node-writer write is refused `cross-session`. Observed by AC1, AC2, AC3.
- **S4** — What the node writer never does. It never takes S5's owner path, since it has no binding
  and no terminal; a prune it makes is admitted only by S5's holder clause with `sessions` as the
  holder, or as TOOL-dPlacedRequest-16 S7's `lease.prune`. Observed by AC4.
- **S5** — The limit, stated where a reader meets it: the door's docstring, the door section of
  `tools/unattended/VERBS.template.md` (rendered to `memory/guides/UNATTENDED-VERBS.md`) and
  `help/runtime.md` each say that a process on this host that unsets its session id writes as the
  node writer, for this node's records and the hosted run's session only, the reach the `mine` row of
  `check_claim_writable` (`tools/unattended/unattended.sh:2260`) grants today. Observed by AC6.
- **S6** — The fixture cases, added to `tools/memory-tree/door_fixture.py`
  (TOOL-dWellOiledMachine-58 S10): its fleet registry maps the fixture's user and host to tag `a`,
  one clone holds a run-state file for `fx` whose `host:` is this host and whose `session:` is `s1`,
  and each node case runs its verb with `CLAUDE_CODE_SESSION_ID` removed from the environment.
  Observed by AC1 to AC5.

  **Readers:** by name: READER NOT IN TREE — `door_fixture.py` is TOOL-dWellOiledMachine-58's, unbuilt at HEAD, and gains these cases. by value: NO VALUE READERS — the fixture's environment is its own.
## 3. Non-goals (OUT)

- No change to `check_claim_writable`'s table: the door stays a second check in front of the push.
- No signed or token-proved node identity: the door's stated limit, a process outside it that holds
  push rights, already covers a local process that forges its environment.
- No supervisor or tick code: TOOL-dWellOiledMachine-6, -13, -18, -47, -48, -54 and -59 write through
  the verbs as their specs say, and this unit makes those writes admissible.
- No new refusal reason word: a sessionless write with no node keeps `no-session`, and a node
  writer's write naming another node or session is `cross-session`.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-58` — `check_writer_binding`, its verdict table and `door_fixture.py`, which this unit gives the node writer; without them there is no door to admit through
- **hands-off** `TOOL-dWellOiledMachine-6` — the node writer, through which the supervisor's `--beat`, its lease reads and its wakes reach the remote with no session
- **consumes-from** external — TOOL-dPlacedRequest-1 S11's `resolve_fleet_tag` and S2's lease record keys `session` and `fleet-tag`; TOOL-dPlacedRequest-12's `derive_ref_segment`

## 4. Design

### Evidence

- The tick runs with no session: `grep -c CLAUDE_CODE_SESSION_ID tools/unattended/resume-tick.sh`
  prints 0 at this base, and `write_claim_beat` (`tools/unattended/unattended.sh:2462-2500`) renews a
  claim with the session it copies from the run-state file, never the caller's.
- Today's admission of that beat is `check_claim_writable`'s `mine` row, keyed on the run-state
  file's keepalive and session (`tools/unattended/unattended.sh:2260`), and `write_claim` fills
  `session` from the run-state file when one is handed in, else from `CLAUDE_CODE_SESSION_ID` or
  `absent` (`:2405-2409`).
- TOOL-dWellOiledMachine-52 §4 rejected a node ref for exactly this reason, citing 58 S1's refusal of a
  sessionless write (`spec-52.md:128-131`), and its S4 sets `GOV_DOOR_VERB=lease.beat` on the beat.
- The run-state file's facts sit under `## Run facts`, one `key: value` per line
  (`tools/unattended/unattended.sh:1347-1361`), and its path is `$M/builds/<slug>/RUN.md`.

### The node writer's verdict

| Op | Ref | Admitted for the node writer when |
|---|---|---|
| write | `refs/gov/leases/…`, `refs/gov/runs/…`, `refs/gov/requests/…` | `fleet-tag` (where carried) is `node`, `session` is `absent` or the hosted run's |
| write | `refs/gov/mail/<slug>/<tag>/<seg>` | `<tag>` is `node`, `<seg>` and the message's sender name a session of `sessions` |
| tombstone | a build or unit lease | the tip read names `node` and a session of `sessions`; or 58 S4 (b), (c) |
| delete | as 58 S5 | the holder clause with `sessions`, or `lease.prune`; never the owner path |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_node_writer` | Python function | `read`, OK |
| `--node`, `--memory` | `gov_record.py door` options | none |

### Files touched (estimate)

- `tools/memory-tree/gov_record.py`: `read_node_writer`, the node branch of `check_writer_binding`
- `tools/memory-tree/door_fixture.py`: S6's cases
- `tools/unattended/unattended.sh`: `GOVREF_DOOR` gains `--node` and `--memory`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `help/runtime.md`

### Alternatives rejected

- **Admit any sessionless write naming this node's fleet tag.** It would let a sessionless writer
  tombstone a lease another session on this node holds; S2's `sessions` keeps the reach at the
  `mine` row's.
- **Key the node writer on the supervisor's pid file.** The tick writes before any supervisor exists
  (TOOL-dWellOiledMachine-54 S4's pick-and-claim, TOOL-dWellOiledMachine-13 S6's cadence lease), so a
  pid-file key would refuse the writes that create the lease the supervisor later holds.

## 5. Production-readiness checklist

- security — deny by default kept: no `--node` still refuses `no-session`; a node writer writes only
  records naming this node and either no session or the hosted run's; it has no owner path. The
  added reach is stated in three places (S5).
- perf / scale — one run-state file read per sessionless write, beside a push.
- error / empty / loading states — an unreadable run-state file leaves `sessions` as `absent` alone,
  so a beat of a run-session lease is refused `cross-session` and named, never admitted on a guess.
- observability — the refusal line names the ref and the reason, carried in `GOVREF_WHY`.
- risks — a session on this host that unsets its id can act as the hosted run; that is today's
  `mine` reach, stated in S5.
- testing — the fixture cases under AC1 to AC5 and the arm in §7.
- migration — none: an argv option and a rule branch; no record moves.
- user docs — the verbs guide's door section and `help/runtime.md`.

## 6. Acceptance criteria

Each case runs `python door_fixture.py --case <name>` with `CLAUDE_CODE_SESSION_ID` removed from the
verb's environment.

- **AC1** — When `--case node-beat` runs `unattended.sh --beat fx` in the clone whose run-state file
  names session `s1` on this host, the beat prints `beat — fx · renewed` and the remote's build lease
  moves; `--case node-acquire-run` runs `--lease acquire run wake w1` and the lease record lands with
  `session: absent` and `fleet-tag: a`.
  Red when: either write is refused `no-session`, as 58 S1 alone refuses it.
- **AC2** — When `--case node-cross-tag` runs a sessionless `--lease renew` on a build lease whose
  `fleet-tag` is `b`, the verb exits 2 printing `door — refused · refs/gov/leases/fx/build ·
  cross-session` and the lease is unchanged.
  Red when: the node writer writes another node's record.
- **AC3** — When `--case node-foreign-tombstone` runs a sessionless `--lease release unit fx TOOL-fx-1
  --as withdrawn` on a unit lease held by session `s2` on tag `a`, it exits 2 printing
  `forged-tombstone`, and with the lease held by `s1` it writes the tombstone.
  Red when: a sessionless writer tombstones a lease held by a session that is not the hosted run's.
- **AC4** — When `--case node-prune` runs a sessionless prune of `refs/gov/mail/fx/a/s2` while no
  lease of `fx` names `s1` or `absent`, it exits 2 printing `not-holder`.
  Red when: the node writer deletes a mailbox it does not hold, or takes the owner path.
- **AC5** — When `--case node-unregistered` empties the fixture's fleet registry and runs
  `--beat fx`, the beat prints the door's `no-session` refusal.
  Red when: a node with no fleet row is admitted as a node writer.
- **AC6** — When `grep -n "node writer" tools/unattended/VERBS.template.md runtime.md` runs over the
  guide and the help page, each names the node writer and its reach.
  Red when: either page omits the limit.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates`

The unattended kit's self-test suites are waived for this build's landing (README rule 8); the door
fixture is this unit's observation.

New arm: tools/memory-tree/door_fixture.py · covers AC1 AC2 AC3 AC4 AC5 · each node case staged against `check_writer_binding` with the node branch removed, and with the `sessions` check removed · none

## 8. Open questions

- **F1 — Which sessions does the node writer stand for?** (a) `absent` and the hosted run's session,
  read from the run-state file on this host; (b) any session on a record naming this node's tag;
  (c) only `absent`. (b) lets a sessionless writer tombstone another session's lease on this node,
  against 58 S4; (c) refuses the supervisor's `--beat`, which renews a lease carrying the run's
  session (`write_claim`, `:2405-2409`), so AC1 fails. Rung 3, the most capable surviving option,
  reusing the `mine` row's keying. RESOLVED (agent, 2026-10-27, delegated): (a). widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 1 (B1).

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-58's door, `check_writer_binding` in
`tools/memory-tree/gov_record.py`, and its argv `GOVREF_DOOR`; the identity rule reuses the keying of
`check_claim_writable`'s `mine` row (`tools/unattended/unattended.sh:2260`) and the node identity of
`resolve_fleet_tag` (TOOL-dPlacedRequest-1 S11). The probe
`python tools/codebase-map/reuse_lookup.py "admit a coordination write from a process with no session"`
ranked `write`, `write_text`, `extract_session` and `resolve_session_tree` by name stem, none an
identity check, so no existing seam does the admission and the door is extended in place.

Recall terms used: `python tools/memory-recall/query.py "which writer may write a lease when no
session id is set" --terms "record door node tick supervisor sessionless writer fleet tag lease beat
keepalive mine class"`
