# TOOL-dWellOiledMachine-44 — the memory-mirror point: a stand-in adapter fed from the change feed, four reads that consult it, and every verdict computed locally

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 57 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0322@a00b6c23 whole
**Carries:** node:point.memory-mirrors
**Carries:** node:policy-key.memory.mirror

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

Multi-node concurrent builds have no real-time shared memory: a node sees another's records only
after a fetch at its read points, and nothing gives a real-time store a place to plug in
(gap-mem-46, gap-register:229). The owner's NT-14 asks for that place now, git staying the store of
record and every verdict computed locally (v2:1372). This unit declares the memory-mirror point, its
adapter protocol and `memory.mirror`'s registered names; ships a stand-in adapter that receives the
change feed as it is written; extends four reads, `record show`, `record find`, the mail notice and
the card's pointers, to consult it where the local git lacks what it holds and to fall back to git
and the local index when it is absent; and holds every verdict, `next` answer, gate and transition
output byte-equal with the mirror on and off.

## 2. Scope (IN)

- **S1** — The point (I4): the `[[point]]` row `name = "point.memory-mirrors"` in
  `tools/runtime/points.toml`, `purpose` "a backend that receives the change feed in real time and
  answers other nodes' reads, git staying the store of record" (layer-runtime `[extend]` :871),
  `contract` the adapter protocol: an `[[adapter]]` row's `run` argv reads one JSON request per line
  on stdin and writes one JSON answer per line, for five verbs: `put` (one change-feed event, its six
  fields, TOOL-dPlacedRequest-13 S1, and `files`, the path and base64 bytes of each file of the
  event's commit tree), `get` (a ref prefix: the newest event held per ref under it), `scan` (a path
  prefix: the newest event per ref holding a file under it), `dump` (every held event in `seq` order)
  and `reset`. Observed by AC1.
- **S2** — `memory.mirror` (`policy-key.memory.mirror`, catalogue `tools/policy/catalogue.toml:1438-1442`,
  default `none`): the row keeps its values, default and owner, and its `registry` text becomes the
  point tag `point.memory-mirrors`, so `check_value`'s registry arm (TOOL-dWellOiledMachine-55 S7)
  admits a name an `[[adapter]]` row at this point names and refuses any other. Read through
  `resolve` (I31). Under `none` no read consults a mirror and nothing is relayed. Observed by AC1.
- **S3** — The stand-in adapter, `tools/runtime/mirror_standin.py`, registered as `name = "stand-in"`
  with `run = ["python", "mirror_standin.py"]`, `tenancy = "shared"`, `retention = "forever"`,
  `region = "local"` and `grant = { service = "local", scopes = [], secret = "anonymous" }`. It keeps
  its store in the directory `GOV_MIRROR_DIR` names, else `<git-common-dir>/gov/mirror-standin/`,
  one file per ref holding the newest event and an `events.jsonl` in `seq` order, so two clones
  pointed at one directory share it as two nodes share a hosted database. `--lose-every <n>` loses
  every n-th `put`, the lossy adapter AC2 plants. Observed by AC2, AC3.
- **S4** — The relay, `run_mirror_relay(repo)` in `tools/runtime/mirror.py`, run as `python mirror.py
  relay`. It reads `memory.mirror`; under `none` it clears the relay file `<git-common-dir>/gov/mirror.relay` and
  exits 0. Under a registered name it writes that file, holding this command's argv, and sends every
  feed event after the last one relayed, read through `unattended.sh --feed print --from <n>`
  (TOOL-dPlacedRequest-13 S8), `n` kept in `<git-common-dir>/gov/mirror.seq`. Each event's files pass
  `secret_scan.py payload mirror <file>` (TOOL-dWellOiledMachine-57 S3) before the `put`; an event
  the scan refuses is withheld, printing `mirror — withheld · <ref> · token-shape`, and never sent.
  `n` moves past an event only once it is sent or withheld. Observed by AC2, AC6.
- **S5** — Real time. `add_feed_event`'s one success exit (TOOL-dPlacedRequest-13 S2), in the
  `gov_feed_sh` block and each of its inline copies, gains one guarded line: when
  `<git-common-dir>/gov/mirror.relay` exists it starts the argv the file holds detached, so a ref
  written on one node reaches the mirror without waiting for a beat; no relay file, no start, so a
  node under `none` pays one file test per append. The node tick runs `python mirror.py relay` once
  per tick as the catch-up after a crash. Observed by AC3.
- **S6** — The reads, through `read_mirrored(kind, key, repo)` in `mirror.py` and its CLI `python
  mirror.py get <ref-prefix>` and `python mirror.py scan <path-prefix>`, each answer used only where
  the local git lacks the answer's commit (`git cat-file -e`), so a mirror never overrides what the
  node holds. Under `none`, or when the adapter cannot start, exits non-zero or outlasts
  `MIRROR_BOUND_SECONDS`, it answers nothing and the reader prints ` · mirror absent (<why>)`. The four
  readers:
  - `record show <id>` (TOOL-dTotalRecall-9 S5) on its unknown-key exit asks `scan memory/` for a file
    whose stem is the id, printing the record with a last line `· via mirror <ref>@<commit8>`;
  - `record find --build <slug>` (its S3) appends, after its local rows, a row per mirror record under
    `memory/builds/<slug>/` the local index lacks, marked `via mirror`;
  - the mail notice, `unattended.sh --mail notice <slug>` (KICK-dKeptSession-21 S1), adds the mail
    events `get refs/gov/mail/<slug>/` holds that the local git lacks, each id marked `via mirror`;
  - the card's pointers, `manifest-check.sh --card --lookup --build <slug>` (TOOL-dPlacedRequest-2
    S6), reads the card event `get refs/gov/builds/<slug>/card` holds when the local copy lacks it.
  Observed by AC3, AC4.
- **S7** — Rebuild and check. `python mirror.py rebuild` sends `reset` and then every feed event from
  `seq` 1; `python mirror.py check` compares the adapter's `dump`, reduced to the newest event per ref,
  with the same reduction of the feed, printing `missing <ref>` or `extra <ref>` per difference and
  exiting 1 on any. Observed by AC2.
- **S8** — No verdict reads the mirror. `check_mirror_readers(root)` in `mirror.py`, run as `python
  mirror.py --check-readers`, finds every call of `read_mirrored` or of `mirror.py get` or `scan` in
  tracked code and reds each outside `MIRROR_READERS`, the four readers' files, naming its path and
  line; it prints `<n> mirror read(s) in <m> file(s)`, and zero reads print `unarmed`. Beside it, the
  fixture's verdict probe runs each command of `MIRROR_VERDICTS`, the position, plan, status and lease
  reads, under `none` and under a registered mirror holding what the local git lacks, and compares the
  outputs byte for byte. Observed by AC5.
- **S9** — The page `help/runtime.md` gains a section on the mirror: `memory.mirror`, the adapter
  protocol, the stand-in, the four reads and what never reads it. Observed by AC7.

## 3. Non-goals (OUT)

- The cloud relational database adapter. v2 plans it as an integration that "counts in no build's
  planned units", run against this unit's stand-in fixture (v2:1892-1896); this unit ships the point,
  the protocol and the stand-in it conforms to.
- The change feed, its appender, its replay and its census: TOOL-dPlacedRequest-13. S5 adds one line to
  its success exit and nothing else.
- Record writes joining the feed: dTotalRecall's `record` command joins through `add_feed_event` when it
  lands (TOOL-dPlacedRequest-13 §3); until then a record reaches the mirror only on a `refs/gov/*`
  write, and the two record reads find nothing there.
- The secret scan of a mirror payload: TOOL-dWellOiledMachine-57, whose `mirror` population S4 calls.
- The adapter's credential for a hosted store: `runtime.secret-home` and the grant, units 17 and 37.
- A mirror answer in any verdict: S8 refuses it by construction.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-20` — `points.toml`, where `point.memory-mirrors` and its stand-in adapter register
- **consumes-from** `TOOL-dWellOiledMachine-57` — `scan_payload`, which the relay runs under `mirror` before it sends an event
- **consumes-from** `TOOL-dWellOiledMachine-55` — `check_value`'s registry arm, which admits `memory.mirror`'s registered names once S2 names the point
- **consumes-from** external — TOOL-dPlacedRequest-13's `add_feed_event` and `--feed print`, TOOL-dTotalRecall-9's `record show` and `record find`, KICK-dKeptSession-21's `--mail notice` and TOOL-dPlacedRequest-2's `--card --lookup`, each specced and unbuilt at base `0689e7fa`
- **hands-off** `TOOL-dWellOiledMachine-79` — its catalogue edit (finding 56), which the spec audit's minors batch repairs

## 4. Design

### Evidence

- layer-runtime's `[extend]` table declares the point and its contract (:871); its `[current]` row
  says integrations fill the memory-mirror adapters and nothing uses the point yet (:940-941).
- `memory.mirror` is a one-member enum whose `registry` text names "a registered memory-mirror adapter"
  (`tools/policy/catalogue.toml:1440`), and `check_value` refuses every name outside `of` until a
  registry arm admits it (`tools/policy/policy.py:143-159`).
- The feed is node-local and append-only, keyed by ref, blob and commit, with a replay from any `seq`
  (TOOL-dPlacedRequest-13 S1, S8): the one event source a mirror needs, and a rebuild source.

### The flow

```
node A: write_gov_ref ─▶ add_feed_event ─▶ (mirror.relay exists) ─▶ mirror.py relay ─▶ scan ─▶ adapter put
node B: --mail notice / --card --lookup / record show / record find
          local git ──hit──▶ answer
             └─miss or older──▶ mirror.py get|scan ─▶ adapter ─▶ commit local lacks ─▶ answer · via mirror
                                       └─ none, failed, slow ─▶ local answer · mirror absent (<why>)
next / --plan / --status / gates / transitions ─▶ local git only (S8)
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `point.memory-mirrors` | `[[point]]` row | none |
| `put`, `get`, `scan`, `dump`, `reset` | adapter protocol verbs | none |
| `mirror.py` with `relay`, `get`, `scan`, `rebuild`, `check`, `--check-readers`, `--fixture` | runtime kit file | none |
| `mirror_standin.py` | stand-in adapter | none |
| `run_mirror_relay`, `read_mirrored`, `check_mirror_readers` | Python functions | `py.function`, OK |
| `MIRROR_READERS`, `MIRROR_VERDICTS`, `MIRROR_BOUND_SECONDS` | constants, `mirror.py` | none |
| `<git-common-dir>/gov/mirror.relay`, `mirror.seq` | node-local files | none |

`MIRROR_BOUND_SECONDS` is PINNED at 5, the bound a read waits before it answers from git alone, so a
slow store never slows a read past a fetch.

### Files touched (estimate)

- `tools/runtime/mirror.py`
- `tools/runtime/mirror_standin.py`
- `tools/runtime/points.toml`: the point row and the stand-in's adapter row
- `tools/policy/catalogue.toml`: `memory.mirror`'s `registry` text
- `tools/lib/gov-feed.sh`, and its inline copies in `tools/unattended/unattended.sh`,
  `tools/run-gates/post-merge.sh` and `skills/session-kickoff/manifest-check.sh`: S5's line
- `tools/unattended/unattended.sh`: the mail notice's mirror read; the node tick's relay call in
  `tools/unattended/resume-tick.sh`
- `skills/session-kickoff/manifest-check.sh`: the card lookup's mirror read
- `tools/memory-tree/record_find.py`: the two record reads
- `help/runtime.md`

### Alternatives rejected

- **A relay on the supervisor's beat alone.** It bounds the delay at a minute on a node running a
  supervisor and ten on any other, which is not the clause's real time; the beat survives as S5's
  catch-up.
- **The mirror answering first, git second.** A store that lost an event would hide a record the node
  holds; S6 uses an answer only where the local git lacks its commit.
- **One verdict check per command.** S8 grades the class, every call site of the mirror read, so a new
  verdict command cannot start reading it unseen.

## 5. Production-readiness checklist

- security — every relayed payload passes the `mirror` scan first and a refused one is withheld; the
  stand-in's grant is anonymous and local; a hosted adapter's credential is read by reference only
  (unit 17); `mirror.relay` holds an argv gov wrote under the git common dir, never a secret.
- perf / scale — one file test per feed append under `none`; one detached relay per append under a
  name; a read waits at most `MIRROR_BOUND_SECONDS` on the adapter.
- error / empty / loading states — an absent, failing or slow adapter degrades every read to git and
  the local index, named on the read's line; an empty store answers misses.
- observability — `mirror.py check` names every ref the store lacks or holds extra; each withheld event
  prints one line.
- risks — relays from two appends can overlap; the adapter keeps the newest event per ref by `seq`, so
  a late duplicate `put` changes nothing, and `check` names any gap.
- testing — the fixture plants under §6 and the arm in §7.
- migration — none: `none` is the default, under which nothing changes.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python mirror.py --fixture --plant <case>`: a bare remote and two clones, A and B,
under `%TEMP%` with short names, both pointed at one stand-in directory, `memory.mirror` set to
`stand-in` unless the case says `none`, and the feed, mailbox and card verbs of their parents.

- **AC1** — When `python policy.py get memory.mirror` reads `stand-in` with the stand-in's row
  registered it prints `stand-in`, and with the row removed it refuses naming `point.memory-mirrors`;
  `python points.py check` over the registry is clean.
  Red when: an unregistered name is admitted.
- **AC2** — When `--plant lossy` relays ten mail events through the stand-in with `--lose-every 2`,
  `python mirror.py check` exits 1 naming the five dropped refs `missing`; after `python mirror.py
  rebuild` it exits 0 and the store's `dump` equals the feed's newest event per ref.
  Red when: the rebuild leaves a ref missing, or `check` passes a store that dropped events.
- **AC3** — When `--plant cross-node` posts a mail message on A, B's `unattended.sh --mail notice fx
  --local`, run before any fetch on B, names the message's id marked `via mirror`; a card published on
  A is printed by B's `--card --lookup --build fx` before B fetches.
  Red when: B names nothing until it fetches, or the relay waits for a tick.
- **AC4** — When `--plant absent` sets `memory.mirror` to `none`, and when `--plant broken` makes the
  adapter exit 1, B's notice and lookup print what B's git holds with ` · mirror absent (<why>)` and
  exit as they do with no mirror; with B fetched, every read prints the local answer and no `via
  mirror` mark.
  Red when: a read fails, hangs past `MIRROR_BOUND_SECONDS`, or prefers the mirror over a commit B
  holds.
- **AC5** — When `--plant verdicts` plants in the stand-in a record and a mail event B's git lacks and
  runs each of `MIRROR_VERDICTS`, `next.py fx`, `unattended.sh --plan fx`, `unattended.sh --status fx`
  and `unattended.sh --claims`, on B under `none` and under `stand-in`, the two outputs of each are
  byte-equal; `python mirror.py --check-readers` reds a planted `read_mirrored` call in a copy of
  `next.py` and passes the tree.
  Red when: any output differs with the mirror on and off, or the census misses the planted call.
- **AC6** — When `--plant token` relays a mail event whose body carries a planted token, the relay
  prints `withheld` with the ref, the stand-in's `dump` lacks the event, and the next relay does not
  send it.
  Red when: the planted token reaches the store.
- **AC7** — When `grep -n "memory.mirror\|point.memory-mirrors" runtime.md` runs over the help page,
  both are named.
  Red when: the page omits the key or the point.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `policy fixtures` · `manifest-check self-test` · `scratch-guard self-test` · `unattended kit gate`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/mirror.py · covers AC2 AC3 AC4 AC5 AC6 · each plant run by `--fixture`, staged against a `read_mirrored` that prefers the mirror over local git and a `check_mirror_readers` that admits every file · none

## 8. Open questions

- **F1 — How does a feed event reach the mirror in real time?** (a) A guarded line at
  `add_feed_event`'s success exit starting the relay recorded in `mirror.relay`, with the node tick as
  catch-up; (b) a relay on the supervisor's beat and the tick only; (c) the readers pulling from the
  writer's node. (b) delays an event by up to a beat or a tick, short of "in real time"; (c) needs a
  node-to-node channel no clause builds. (a) touches a parity-held block by one guarded line and runs
  nothing under `none`. Rung 3, the most capable option. RESOLVED (agent, 2026-10-26, delegated): (a).
  widens: none · relaxes: none
- **F2 — When does a read take the mirror's answer?** (a) Only where the local git lacks the answer's
  commit; (b) whenever the mirror's event is newer by `seq`. `seq` is node-local
  (TOOL-dPlacedRequest-13 S1), so (b) compares two nodes' counters. Rung 1, git the store of record
  (v2:1372). RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — Is "a cloud relational database first" this unit's adapter?** (a) No: the point, its protocol
  and a stand-in it conforms to, the hosted adapter being the integration v2:1892 plans in no build's
  units; (b) this unit ships a hosted adapter. (b) is a new external dependency and a credentialed
  outbound surface, veto 2 and veto 3. Rung 1, v2:1892-1896. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-79.

## 10. Reuse audit

The seams extended are TOOL-dPlacedRequest-13's change feed, whose replay is the relay's source and
the rebuild's, and whose one append exit is where a write starts the relay; the point registry
`points.toml` and unit 55's registry arm, which together arm `memory.mirror`'s names; unit 57's
`mirror` scan population; and the four parent reads named in S6, each extended at its miss and never
copied. `python tools/codebase-map/reuse_lookup.py "mirror the change feed to a store other nodes
read"` ranked `read`, `read_text`, `changed`, `read_journal` and `read_host_name` by name stem; none
is a mirror or a feed relay, and no existing seam fits the adapter protocol, which the point's own
contract declares. Scout B's row names `record_find.py` as unbuilt at this base, which holds: it is
TOOL-dTotalRecall-9's file.

Recall terms used: `python tools/memory-recall/query.py "how does the memory mirror answer reads while every verdict stays local" --terms "memory mirror memory.mirror change feed record show record find stand-in adapter git store of record verdict"`
