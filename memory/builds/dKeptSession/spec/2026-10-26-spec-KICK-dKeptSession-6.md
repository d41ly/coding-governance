# KICK-dKeptSession-6 — live delivery where the harness has it: the post's tail rings the channels `deps.messaging` picks, with only the ref and the id

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 23 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0144@c41201f3 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

Where the harness can message another session, a sender writes the mailbox first and then delivers
live, citing the message (coordination item 7); `deps.messaging` picks the channels, and the live
message carries only the message's ref and id, so a lost ring costs only latency (FI-6, the owner's
NT-17). This unit gives `--mail post` that tail: one ring point, called only after the mailbox write
has landed, reading `deps.messaging` and ringing each live channel the harness offers. The harness
this repository runs in offers none between sessions (§8 F1), so today the tail rings nothing and says
so, and a registered doorbell joins at the point dWellOiledMachine declares in Runtime's `[extend]`
(v2:1167).

## 2. Scope (IN)

- **S1** — The ring point, `run_mail_ring <ref> <id>` in `tools/unattended/unattended.sh`, called by
  `KICK-dKeptSession-5`'s `--mail post` once its `write_gov_ref` returned 0, with the mail ref the
  message was appended to and the message's id, and with nothing else: it reads no field of the
  record and passes no fact. A post whose write was lost or not completed calls it never. Observed by
  AC2.
- **S2** — `deps.messaging` (`live-and-mailbox`, `live-only`, `mailbox-only`, or a registered doorbell;
  default `live-and-mailbox`), read through I8's shell form, `python <prefix>/policy/policy.py get
  deps.messaging`; a refusal, which is what any doorbell name reads as until Runtime registers one,
  reads the catalogue default and prints one NOTE naming the key. Observed by AC1 and AC4.
- **S3** — The ring, by value. Under `mailbox-only` the point rings nothing and the post prints
  `ring — off (deps.messaging: mailbox-only)`. Under `live-and-mailbox` and `live-only` it rings each
  live channel the harness offers, the empty set today (§8 F1), and prints
  `ring — none · no live channel in this harness (stand-in dWellOiledMachine)`. Under every value the
  mailbox was written first: `live-only` never skips it (§8 F2). Observed by AC1 and AC3.
- **S4** — A ring never fails a post. The post's exit is its write's; the ring point's own outcome is
  the `ring —` line alone. Observed by AC2.
- **S5** — The verbs guide: the `--mail` section of `tools/unattended/VERBS.template.md` (rendered to
  `memory/guides/UNATTENDED-VERBS.md`) states the `ring —` line, its three values and the stand-in.
  Observed by AC5.

## 3. Non-goals (OUT)

- No transport, doorbell or adapter: the doorbell point and its registered names are
  dWellOiledMachine's, in Runtime's `[extend]` (v2:1167, v2:1777). Building one here would build a
  later build's surface.
- No receiver: what a node does on a ring, the notice fetch through `--mail notice --ring`, and I25's
  payload rule are `KICK-dKeptSession-21`'s.
- No mailbox, record or post path: `KICK-dKeptSession-5`'s.
- No `deps.messaging` row: dGroundRules-1 S3 writes it, `registry = "a registered doorbell"`, owner
  dKeptSession; `KICK-dKeptSession-21` carries the key's node.
- No `[[stand-in]]` row (§8 F3).

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox` and the `--mail post` writer whose tail this point is; the id a ring carries is the one `read_mailbox` reports, so a receiver finds the message by it
- **consumes-from** `KICK-dKeptSession-21` — `deps.messaging`, the channel key, and I25's payload `<mail ref> <message id>`
- **hands-off** external — dWellOiledMachine's doorbell point in Runtime's `[extend]` arms the registered doorbell names and the live channels the ring point rings

## 4. Design

### Evidence

- Coordination item 7 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md:122-129`):
  the sender writes the mailbox first, then delivers live citing the message id; any other harness,
  and the owner by hand, use the same verbs; the live message carries only ref and id.
- FI-6 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md:113-115`):
  "Live where possible, mailbox always".
- No code rings anything: `grep -rn 'SendMessage\|doorbell' tools skills` finds 0 lines at base.
- `SendMessage` reaches the agents of the session that spawned them, never another session
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md:103`).

### The tail, in order

1. `--mail post` builds and writes the message (unit 5); on any return but 0 it exits as unit 5 says.
2. On 0 it calls `run_mail_ring <ref> <id>`.
3. The point resolves `deps.messaging` and prints its one `ring —` line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_mail_ring` | shell function | `run`, OK |
| `ring —` | the post's output line | none |

### Migration

None.

### Rollout

Behind `RUN_CLAIMS` with every mail write. The point rings nothing until a live channel exists, so
landing it changes no delivery.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `run_mail_ring` and its call in the post's tail,
  `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: the `ring —` line
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **A same-node ring through a file the other session's hook watches.** The tool-call hook of
  `KICK-dKeptSession-21` already reads the node's local copy, which the post's own write updates, so
  a ring file would be a second copy of what the cache already holds.
- **A ring before the write.** A receiver could fetch before the message exists and find nothing,
  and a lost write would leave a ring for no message.

## 5. Production-readiness checklist

- security — the ring passes two validated strings, a ref of I16's grammar and a 12-hex id; no body,
  sender or subject leaves the mailbox.
- perf / scale — one policy read per post.
- error / empty / loading states — no channel prints `ring — none`; a refused read prints a NOTE and
  rings as the default.
- observability — every post prints its `ring —` line.
- risks — none at landing: nothing is rung.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --mail post` posts a message with no
  `deps.messaging` planted, its output ends `ring — none · no live channel in this harness (stand-in
  dWellOiledMachine)`; with `deps.messaging = "mailbox-only"` planted, it ends
  `ring — off (deps.messaging: mailbox-only)`.
  Red when: the post rings under `mailbox-only`, or prints no ring line.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, a fleet tag and
  `CLAUDE_CODE_SESSION_ID` set.
- **AC2** — When a shell that has sourced `tools/unattended/unattended.sh` replaces `run_mail_ring`
  with a recorder and posts, the recorder holds one call of exactly two arguments, the mail ref and
  the id, and at that call `git ls-remote` already shows the ref at the message commit; with
  `write_gov_ref` planted to return 1, the recorder holds no call and the post exits as a lost write.
  Red when: the ring runs before the mailbox write, after a lost one, or with more than the ref and id.
- **AC3** — When `deps.messaging = "live-only"` is planted, the post still moves the mail ref and
  prints `ring — none`, exit 0.
  Red when: `live-only` skips the mailbox.
- **AC4** — When the policy read of `deps.messaging` is refused, as a doorbell name reads before
  Runtime registers one, the post rings as `live-and-mailbox` and prints one NOTE naming
  `deps.messaging`.
  Red when: a refused read rings nothing silently or fails the post.
- **AC5** — When `grep -n 'ring —\|deps.messaging'` runs over `tools/unattended/VERBS.template.md`,
  both are found in its `--mail` section.
  Red when: the ring line is undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the ring arms over a post, AC2 staged by a recorder in place of `run_mail_ring` and a planted lost write · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

## 8. Open questions

- **FACT-QUESTION · F1 — Does this harness offer a channel by which one session messages another?**
  Probe: `grep -rn 'SendMessage\|doorbell' tools skills`, and the installed CLI's tool text read with
  `grep -a -o '.\{0,100\}SendMessage.\{0,240\}' <CLI binary>` (Claude Code 2.1.308). Observation,
  2026-10-26: no file under `tools` or `skills` rings anything; the CLI's `SendMessage` addresses an
  agent this session spawned or a teammate of "a single implicit team", never another session, as
  research-runtime-spawn.md:103 records. Liveness: a tool addressing another session would print in
  the CLI's tool text the grep reads. RESOLVED (agent, 2026-10-26, delegated): no live channel; the set
  the ring point rings is empty until Runtime's doorbell point, rung 2. widens: none · relaxes: none
- **F2 — Does `live-only` skip the mailbox?** Options: (a) no: the mailbox is written under every
  value, since a ring carries only a ref and an id (cl-dClosedLoop-0159) and the sender writes the
  mailbox first (coordination item 7); (b) yes, which rings an id no mailbox holds. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — Is the stand-in a `[[stand-in]]` row?** The brief asks a stand-in be registered so.
  Options: (a) no row: TOOL-dDeclaredLoop-13 S8's list holds transition-table items whose owning build
  has not landed and reds a row naming no row item, and a ring is no item, so the stand-in is named on
  the `ring —` line and in §3's hand-off; (b) a row, which that unit's check reds. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, TOOL-dDeclaredLoop-13 S8. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 6, scout B row 2, Shared interfaces
  I8, I19 and I25, coordination item 7, FI-6 and v2:1167.

## 10. Reuse audit

No existing seam fits the ring itself: `grep -rn 'SendMessage\|doorbell' tools skills` finds 0 lines,
and scout B's row 2 found the same. The seam extended is the `--mail post` writer of
`KICK-dKeptSession-5`, whose success exit after `write_gov_ref` (TOOL-dPlacedRequest-11 S1) is the one
place a ring may follow a landed write; the policy read is I8's shell form, as
TOOL-dPlacedRequest-1 S12's `read_lease_policy` reads its keys. `python
tools/codebase-map/reuse_lookup.py "ring another session live after writing a message"` ranked
`write`, `live`, `write_text` and `extract_session`, name stems only, none a delivery. `python
tools/memory-recall/query.py "how does a live ring reach another session"` returned scout B's row 2,
the night-pass instrument's `deps.messaging` cell and this build's brief; none disagrees with source.

Recall terms used: deps.messaging live-and-mailbox doorbell live ring SendMessage registered doorbell mailbox-only Runtime extend
