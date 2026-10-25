# TOOL-dPlacedRequest-13 — the change feed: every governance ref write appended once on its node, replayable and rebuilt equal from git

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 2 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0131@3532cbe6 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-13-deviation-131.md](../build/2026-10-25-build-TOOL-dPlacedRequest-13-deviation-131.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

Each node keeps an ordered, append-only feed of every `refs/gov/*` write it makes or sees, keyed by
ref, blob and commit, so a real-time mirror can follow memory without a change to the core (the
owner's NT-14) and the observer clock (`TOOL-dPlacedRequest-17`) can read when this node first saw a
lease's tip. Nothing records a governance ref write today: the run claim (`tools/unattended/
unattended.sh:2423`) and the bar-red marker (`tools/run-gates/post-merge.sh:280`) push and keep no
trace on the node beyond the claim cache `refs/gov/remote/runs` (`unattended.sh:2088`). The feed
hooks `TOOL-dPlacedRequest-11`'s one writer, so every later writer joins it by construction.

## 2. Scope (IN)

- **S1** — The file (I4): `<git-common-dir>/gov-feed.log`, one LF-terminated line per event, six TAB
  fields: `seq` (a positive integer, node-local, rising across refs), `ref` (the remote ref name),
  `kind` (the segment after `refs/gov/`), `blob` (the commit's tree, or `-` on a deletion), `commit` (40
  hex, or 40 zeros on a deletion), `seen-utc` (an ISO-8601 UTC second, shaped `2026-10-25T14:03:07Z`, this node's clock at the append).
  The key is (`ref`, `blob`, `commit`). Observed by AC1 and AC2.
- **S2** — The appender, `add_feed_event <ref> <commit or empty>`, canonical in the new
  `tools/lib/gov-feed.sh` between `# >>> gov_feed_sh` and `# <<< gov_feed_sh`, inline byte-identical
  in `tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh` beside `gov_ref_sh`. Under
  the node-local lock `gov-feed.lock` it appends only when no line carries the key, so a retried
  write appends nothing, and takes `seq` from the counter `gov-feed.seq`. Observed by AC1 and AC2.
- **S3** — The join: `write_gov_ref`'s one success exit sets this node's cache ref
  `refs/gov/remote/<tail>` to what it wrote (or clears it when the write was a deletion), then calls
  `add_feed_event`.
  A lost or uncompleted write appends nothing. Observed by AC1.
- **S4** — The sightings, `add_feed_sightings <cache prefix>`: after a fetch of governance refs into
  the cache, every cached ref whose tip the feed does not hold has its unseen first-parent chain
  appended oldest first, the walk stopping at the newest commit the feed holds for that ref or at the
  first commit not authored `gov-claim`, which is appended as a lone event. `read_claims`
  (`unattended.sh:2118`) calls it after its fetch (`:2136`). Observed by AC3.
- **S5** — The derivation, `derive_feed_events <cache prefix>`: for every ref git holds under the
  cache, the events the same walk yields from its tip with no feed to stop at, mapped to the remote
  name, in per-ref order. Observed by AC4 and AC5.
- **S6** — The check, `check_feed <cache prefix> <file>` and the verb `unattended.sh --feed check
  [<file>]`: per ref git holds, the file's events whose commit is in the derived chain must equal that
  chain in order; a duplicate key anywhere, a derived event the file lacks (`missing`), and on a chain
  ref an event whose commit is outside the chain (`extra`) each print one line and exit 1. Events of a
  ref the cache no longer holds stay in the feed and out of the comparison. Observed by AC4 and AC5.
- **S7** — The rebuild, `write_feed <cache prefix>` and `unattended.sh --feed rebuild`: with no feed
  file present, it writes the derived events with fresh `seq` from 1 and `seen-utc` the rebuild's
  time, and the counter; with one present it exits 2 naming it. Observed by AC4.
- **S8** — The replay, `print_feed [<seq>]` and `unattended.sh --feed print [--from <seq>]`: every
  event at or after `seq`, in file order. Observed by AC6.
- **S9** — The census, `scan_feed_writers <file>…`: every line of a shipped shell file that pushes
  with `--force-with-lease` must sit in a function whose body calls `add_feed_event` or
  `write_gov_ref`; each other one prints `<file>:<line>`. The lib test runs it over every shipped
  shell file and hook, and the parity row `gov_feed_sh` holds the copies. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- No mirror and no relay: the memory-mirror point is dWellOiledMachine's; the feed is its source.
- No record writes: "every commit that touches a record" (memory-plan:97) joins when dTotalRecall's
  `record` command lands; this unit's population is every `refs/gov/*` write.
- No observer clock: `TOOL-dPlacedRequest-17` reads `seen-utc` through `read_first_seen`.
- No Python writer census: no Python file pushes a `refs/gov/*` ref today
  (`branch_reconcile.py:1100` leases `refs/heads/*`), and S9 reads shell only.
- No trim or rotation: the feed is append-only, unlike the health log it borrows its path rule from.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, whose one success exit is where every write joins the feed
- **hands-off** `TOOL-dPlacedRequest-17` — `gov-feed.log`, whose first `seen-utc` per tip is the observer clock
- **hands-off** `TOOL-dPlacedRequest-15` — `gov-feed.log`, the `gov_feed_sh` block and `add_feed_event`, which the lander's fenced beat joins so the census finds it
- **hands-off** `TOOL-dPlacedRequest-2` — `gov-feed.log` and the `gov_feed_sh` block, which the kickoff engine carries inline beside `gov_ref_sh` so the card ref's write joins the feed
- **hands-off** external — dTotalRecall's record writes and dKeptSession's mail writes join through `add_feed_event` or `write_gov_ref`, and the census reds a writer that skips both
- **hands-off** `TOOL-dPlacedRequest-24` — the `gov_feed_sh` block and `add_feed_event`'s `gov-feed.lock`, which that unit's guarded node lock factory joins and replaces
- **hands-off** `TOOL-dPlacedRequest-27` — `add_feed_event`'s append-once test, `add_feed_sightings` and `check_feed`, which that unit narrows to the ref's newest event
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-39` — `add_feed_event`, whose lock and append that unit runs in a subshell so an abort never ends its carrier

## 4. Design

### The line

```
17	refs/gov/runs/dExample	runs	4b825dc642cb6eb9a060e54bf8d69288fbee4904	3f9c2a71…	2026-10-25T09:14:03Z
```

`kind` is derived from `ref`, so a rebuild agrees with it. `blob` is the commit's tree: the empty tree
for every claim and lease commit, the main commit's tree for `refs/gov/bar-red`, which points at a
main commit rather than a gov commit (`post-merge.sh:383`). A delete has no object, so its `blob` is
`-` and its `commit` 40 zeros. `seen-utc` is written with bash's `printf '%(…)T'` under `TZ=UTC`,
so an append forks nothing for the stamp.

### Appending once, in order

`add_feed_event` resolves the common dir once per process (`git rev-parse --path-format=absolute
--git-common-dir`, the call `resolve_health_log` makes at `tools/lib/health-log.sh:28-33`) unless the
caller set `GOVFEED_DIR`, reads the tree with one `git rev-parse <commit>^{tree}`, and then:

1. Takes `gov-feed.lock` by `mkdir`, retrying every 50 ms for up to 5 s; a lock whose directory is
   older than one minute was left by a crash and is removed and retaken.
2. Looks for the key with one `grep -qF` over the file; found, it releases and returns 0.
3. Reads `gov-feed.seq` with the `read` builtin, appends the line with `seq` one higher, writes the
   counter, and releases the lock.

A failure to lock or write prints one `feed: NOTE -` line on stderr and returns 0, as the health log's
appender never fails its caller (`health-log.sh:21-23`): the governance write already landed, and the
next `--feed check` names the missing event. The lock guards only these microseconds on one node; it
is no lock the lander holds.

### Sightings and the cache

The cache namespace `refs/gov/remote/` mirrors `refs/gov/` on the remote: `refs/gov/remote/runs/x` is
`refs/gov/runs/x`. It holds what this node fetched, through `read_claims`' `--prune` fetch, and from
S3 also what it wrote, so the cache is everything this node knows and the feed is everything it
recorded. The walk for one ref is `git rev-list --first-parent --format='%H %T %an' <tip>`, stopped
at the stop commit; one `for-each-ref` lists the refs, and one `awk` pass reads the feed's newest
commit per ref. A ref whose tip the feed already holds costs nothing past that pass.

### The comparison

`derive_feed_events` and the feed agree exactly when every write and every sighting appended once.
A dropped event is `missing`; a retried write appending twice is a duplicate key; a writer that
pushes around `write_gov_ref` leaves its commit in the chain after the next fetch, where the sighting
records it, so it is the census (S9), not the comparison, that reds a writer skipping the append.
`seq` and `seen-utc` are node-local and never compared. `bar-red`'s earlier values are not in any
chain git holds, so only its current tip compares; its past events stay replayable.

### The census

`scan_feed_writers` reads each file with one `awk`: it tracks the enclosing `name() {` and its closing
`}` at column 0, and flags a line carrying both `push` and `--force-with-lease` whose function body
calls neither `add_feed_event` nor `write_gov_ref`. A comment line is skipped. Its population today
is two lines, both inside `write_gov_ref` once `TOOL-dPlacedRequest-11` lands; an empty population
reds the arm, never passes it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/lib/gov-feed.sh` | file | none declared for files |
| `gov_feed_sh` | parity block stem | none |
| `add_feed_event`, `add_feed_sightings` | shell functions | `add`, OK |
| `derive_feed_events` | shell function | `derive`, OK |
| `check_feed` | shell function | `check`, OK |
| `write_feed` | shell function | `write`, OK |
| `print_feed` | shell function | `print`, OK |
| `scan_feed_writers` | shell function | `scan`, OK |
| `gov-feed.log`, `gov-feed.seq`, `gov-feed.lock` | node-local files | none |
| `--feed check`, `--feed rebuild`, `--feed print` | driver verbs | none |
| `GOVFEED_DIR` | shell variable | none |

### Migration

None. A node starts with no feed; its first `--feed check` reports every cached ref's chain
`missing`, and `--feed rebuild` writes them, each `seen-utc` the rebuild's time, which only ever makes
a lease read younger to the observer clock and never expires one early.

### Rollout

Live on landing wherever a governance ref is written; dark where `RUN_CLAIMS` is off, since no claim
is then written or fetched, while post-merge's bar-red write joins under any setting.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: the canonical block, new
- `tools/lib/gov-ref.sh`: `write_gov_ref`'s success exit sets the cache ref and appends
- `tools/lib/resolve-python.test.sh`: the `gov_feed_sh` parity row and the census arm over every
  shipped shell file and hook
- `tools/unattended/unattended.sh`: the inline blocks, the sighting call in `read_claims`, the `--feed`
  verbs in the dispatch table beside `--claims` (`:14489`), `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the feed arms
- `tools/run-gates/post-merge.sh`: the inline blocks
- `tools/run-gates/run-gates.sh`: `KIT_RUN_GATES_VERSION` moved
- `tools/unattended/STOPS.template.md`: section 7 names the feed and its three verbs
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **The health log's writer.** It trims at a cap and does not serialise writers
  (`tools/lib/health_log.py:16-21`); the feed must keep every event and give each a sequence.
- **`seq` as the line number, unstored.** The interface fixes `seq` as a field a mirror resumes from,
  and a reader cannot learn a line number without counting the file.
- **Rebuilding from a fresh fetch of the remote.** The remote holds writes this node never saw, so a
  rebuild from it differs from any node's feed by design; the cache is what this node knows.

## 5. Production-readiness checklist

- security — the feed holds ref names, object ids and stamps, never a message body, so no request
  text or secret reaches it; it lives in the common dir and is never pushed.
- perf / scale — one `rev-parse` and one `grep` per write, and one `awk` plus one `rev-list` per changed
  ref per fetch; the file grows by under 150 bytes an event.
- error / empty / loading states — a failed append is a NOTE and a `missing` line at the next check;
  an empty feed under a non-empty cache is all `missing`, never green; rebuild over a live feed exits 2.
- observability — every check finding names the kind, the ref and the commit.
- risks — two waiters breaking one crashed lock at once can both append, which gives two events one
  `seq` and never loses one; a writer in Python is outside the census.
- testing — the probes of §6, and the suite arms of §7.
- migration — none; `--feed rebuild` seeds a node's feed.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7 names the feed and its verbs; no `help/`
  page covers the unattended kit.

## 6. Acceptance criteria

- **AC1** — When a scratch clone sources `gov-ref.sh` and `gov-feed.sh` and writes `refs/gov/runs/tFix`
  twice through `write_gov_ref`, `gov-feed.log` in its common dir holds two lines, `seq` 1 and 2, kind
  `runs`, blob `4b825dc642cb6eb9a060e54bf8d69288fbee4904`, each naming its commit, and
  `git rev-parse refs/gov/remote/runs/tFix` prints the second; a third write that loses its
  compare-and-swap leaves the file at two lines.
  Red when: the success exit skips the append, or a lost write appends.
  fixture: a scratch clone and bare origin under the run's short temp path, built by the probe.
- **AC2** — When the probe calls `add_feed_event refs/gov/runs/tFix <second commit>` again, the file
  still holds two lines; with the key check cut from a scratch copy of the block, it holds three.
  Red when: a retried write appends twice.
- **AC3** — When a second clone writes `refs/gov/runs/tFix` twice more and the first clone fetches
  `+refs/gov/runs/*:refs/gov/remote/runs/*` and calls `add_feed_sightings refs/gov/remote/`, the
  feed gains exactly those two commits, oldest first, and a second call adds nothing.
  Red when: a sighting records only the tip, or re-records a known commit.
- **AC4** — When the AC3 feed is copied aside, deleted, and `write_feed refs/gov/remote/` rebuilds it,
  `check_feed refs/gov/remote/ <copy>` exits 0; with one line deleted from the copy it exits 1
  printing `missing` and that commit, and with one line duplicated it exits 1 printing `duplicate`.
  Red when: the rebuild differs from the live feed, or a dropped event reads green.
- **AC5** — When the probe deletes `refs/gov/remote/runs/tFix` as a pruning fetch would,
  `check_feed refs/gov/remote/ gov-feed.log` exits 0 and the file still holds every `tFix` line.
  Red when: a pruned ref's events are dropped from the feed or counted as `extra`.
- **AC6** — When `print_feed 3` runs over the AC3 feed, it prints the lines whose `seq` is 3 or more,
  in file order, and nothing else.
  Red when: a replay from a point skips or repeats an event.
- **AC7** — When `scan_feed_writers` runs over `unattended.sh`, `post-merge.sh`, `push-main.sh` and
  `pre-push`, it prints nothing; over a scratch copy of `unattended.sh` with a planted function that
  pushes with `--force-with-lease` and never appends, it prints that copy's line.
  Red when: a writer that skips the append passes the census.
- **AC8** — When `awk` cuts each block from its `# >>> gov_feed_sh` line to its `# <<< gov_feed_sh`
  line in `gov-feed.sh`, `unattended.sh` and `post-merge.sh`, `cmp` finds the three cuts equal, and
  `grep -c '^gov_feed_sh|' resolve-python.test.sh` prints 1.
  Red when: the row is absent, so a drifted copy passes.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `unattended kit gate` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/lib/resolve-python.test.sh · covers AC7 AC8 · the `gov_feed_sh` parity row and the census over every shipped shell file, staged by a planted pushing function with no append · none
New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the feed arms over the suite's bare origin, staged by cutting the key check and by deleting one feed line · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — What does "rebuilt equal from git over the refs git still holds" read?** (a) This node's cache
  namespace, which S3 keeps equal to what it wrote and S4 to what it fetched; (b) a fresh fetch of the
  remote; (c) both. (b) and (c) compare a node's feed with writes it never saw, so no feed on a
  multi-node fleet could pass, which fails the clause's equality. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Does the feed record other nodes' writes, which the clause's "every lease, claim and register
  write joins" leaves open?** (a) Yes, as sightings after each fetch; (b) this node's writes only.
  `TOOL-dPlacedRequest-17`'s observer clock needs the first sighting of another node's tip, and the
  equality of F2 needs the cache and the feed to cover one population. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — What is `blob` for a ref write, which carries no file?** (a) The commit's tree; (b) `-` always;
  (c) a hash of the commit message. (b) leaves the key `ref` and `commit` only, and (c) costs a process
  and names no object git holds. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the record
  writes dTotalRecall joins naming their file's blob in the same field. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 13, scout A row 4 and Shared interface 5,
  memory-plan:97, night-pass-two:261-262 and research-cloud-headless S6.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: S1's time shape written as an example rather
  than a skeleton placeholder; S1 and S3 say deletion where they retire nothing; §3 gains the hands-off to
  TOOL-dPlacedRequest-15 and TOOL-dPlacedRequest-2.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-24,
  hands-off TOOL-dPlacedRequest-27, hands-off TOOL-dPlacedRequest-34, each the mirror of that
  promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-39.

## 10. Reuse audit

No existing seam fits the feed itself. `python tools/codebase-map/reuse_lookup.py "append an event line
to a node-local log under the git common dir"` ranked `add_health_event` and `resolve_health_log`
(`tools/lib/health-log.sh`, the health log), `run_git`, `GIT` and `check_line`; the health log is the
only node-local append under the common dir, and its header says it trims at a cap and "does not
serialize concurrent writers" (`tools/lib/health_log.py:18-21`), so this unit reuses its common-dir
derivation and its never-fail-the-caller rule, not its writer. The writers the feed joins are reached
through `TOOL-dPlacedRequest-11`'s `write_gov_ref`, which merges the only two `refs/gov/*` pushes at
base (`unattended.sh:2423`, `post-merge.sh:280`; `git grep -- --force-with-lease` finds no third in
shell). The copy discipline is the `PARITY_ROWS` loop (`tools/lib/resolve-python.test.sh:168-233`).
Scout A's row 4 holds against source; its "path derivation of `derive_health_log` (health-log.sh:27)"
is the function at that line. `python tools/memory-recall/query.py "where does a node record governance
ref writes for a mirror"` returned scout A's row 4, the brief's I4 and the memory plan's feed row as the
night-pass instruments quote it; none disagrees with the clause or with source.

Recall terms used: change feed gov-feed.log refs/gov append idempotent rebuild mirror health log common dir sighting
