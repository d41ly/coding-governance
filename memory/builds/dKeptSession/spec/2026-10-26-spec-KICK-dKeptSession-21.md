# KICK-dKeptSession-21 — news shown as `mailbox.notice` says: one bounded fetch at each item boundary, a tool-call hook reading the local copy, and the live ring's payload

**Status:** DEFERRED · rev-4 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 22 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0159@ad40c608 whole
**Carries:** node:policy-key.mailbox.notice
**Carries:** node:policy-key.mailbox.fetch-seconds
**Carries:** node:policy-key.deps.messaging

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-21-deviation-211.md](../build/2026-10-26-build-KICK-dKeptSession-21-deviation-211.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A session is shown the unread message ids addressed to its build or item as `mailbox.notice` says:
at every item boundary by default, after one fetch of the mail refs bounded by a timeout, falling
back to the node's local copy and naming its age when the fetch fails; and at every tool call where
the owner's policy sets `every-tool-call`, listed by a hook from the local copy with no network call,
a detached fetch started when the copy is older than `mailbox.fetch-seconds`. The live channel
`deps.messaging` picks carries only a message's ref and id, so a lost ring costs only latency, and the
disposal stays at items and transitions (the night pass two, point 3, the owner's NT-17). News today
waits for the reader's read points, not the transport: a fetch takes 0.6 s and the median gap between
pass commits is 7.5 minutes, gap-conc-05's figures (PINNED,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b44c7:241`).

## 2. Scope (IN)

- **S1** — The notice verb, `unattended.sh --mail notice <slug> [--item <instance key>] [--local]`, a
  member of `KICK-dKeptSession-5`'s `--mail` family (its S8) with its own `#   unattended.sh --mail
  notice …` usage-header row. It first reads `mailbox.notice` and `mailbox.fetch-seconds` (S8). Under
  `off` it fetches nothing, rewrites S3's stamp with its first line alone, prints `mail — notice off
  for <slug> (mailbox.notice: off)` and exits 0. Otherwise it calls `read_mailbox <slug> soft` (unit 5
  S6), whose one bounded fetch of `+refs/gov/mail/*:refs/gov/remote/mail/*` runs through
  `observe_remote` under `REMOTE_BOUND` (`tools/unattended/unattended.sh#observe_remote`). It keeps the
  rows in state `open`, which that reader admits by `check_mail_addressed <to> build:<slug>`
  (`KICK-dKeptSession-28`), and prints one line: `mail — <n> unread for <slug> · <id> <id> … ·
  fetched`, or `mail — none for <slug> · fetched`. `--item` appends ` · item <instance key>`.
  Observed by AC1.
- **S2** — The fallback, and `--local`. When that fetch fails or its bound fires, the `soft` reader
  reads the node's cache `refs/gov/remote/mail/…` and names its cause (unit 5 S6); the notice ends its
  line ` · local copy <age>s old (<why>)`, the age read from S3's stamp, or ` · local copy age unknown
  (<why>)` with no stamp, leaves the stamp untouched and exits 0. This unit adds `local`, a third mode
  of `read_mailbox <who> soft|strict|local` that reads the cache with no fetch, and the flag `--local`
  on `--mail read` and `--mail notice`, which selects it. `--mail notice --local` ends its line
  ` · local copy <age>s old (--local)`. `KICK-dKeptSession-10`'s read at a boundary the notice already
  fetched for uses `--mail read --local`. Observed by AC2.
- **S3** — The notice stamp (I24, refined here, §8 F2): the sidecar
  `<git-dir>/unattended/mail-notice.<slug>.log`, the path `deriveSidecarPath(gitDir, 'mail-notice',
  slug)` (`tools/unattended/run-lease.js#deriveSidecarPath`) and `resolve_sidecar_dir`
  (`tools/unattended/lib-unattended.sh#resolve_sidecar_dir`) both derive. `write_mail_notice`
  rewrites it whole after every notice that fetched, and after an `off` notice, through a unique temp
  file renamed into place. Its first line is `{"notice": <value>, "fetch-seconds": <n>, "bash":
  <path>}` (§8 F5, F6), then one JSON line per unread row, `{"id": …, "kind": …, "to": …}`. Its mtime
  is the age of the local copy this build's notice last fetched. A failed or `--local` notice leaves
  it untouched. Observed by AC2 and AC4.
- **S4** — The item boundary. `run_mail_notice <slug> <key> <out file>` in
  `skills/session-kickoff/manifest-check.sh` runs inside `KICK-dKeptSession-13`'s boundary verb,
  `manifest-check.sh --card --boundary --build <slug> --session <sid>` (its S6), once that verb's
  `run_item_boundary` answers a crossing. It runs `run_driver_bounded "$CARD_CLAIMS_BOUND" <out>
  <err> --mail notice <slug> --item <key>` (`skills/session-kickoff/manifest-check.sh#run_driver_bounded`),
  as unit 5 S13 runs its card read, and prints `notice — <the verb's line>`, nothing for an `off`
  line, or `notice — skipped: <why>` for an unresolved driver, a non-zero exit or a fired bound. It
  runs before unit 10's step and hands it `--local` when the line ends ` · fetched`, so a boundary
  costs one fetch; after an `off` line or a skip, unit 10's read fetches as it says. The verb's lines
  reach the session through unit 13's S7, at the session's next Bash or PowerShell call after the
  detached verb finishes, never on the call that noticed the boundary. Observed by AC1, AC3 and AC6.
- **S5** — The tool-call hook, `tools/unattended/mail-notice.js`, a `PostToolUse` hook on every tool
  (§8 F1), and its fragment `tools/unattended/mail-notice.fragment.json`, both first written by the
  hook kind's factory, `python tools/playbook/core.py new hook mail-notice --kit unattended --event
  PostToolUse` (`tools/loop/factories.py#write_hook`), whose matcher defaults to `*`; the kit's
  `include = "**"` files row already ships both. Per call it reads the payload's `session_id`, the
  repository and its per-worktree git dir through `resolveRepo`
  (`tools/unattended/run-lease.js#resolveRepo`), the build through `resolveLease(root,
  readMemoryRoot(root), sessionId)` (`tools/unattended/run-lease.js#resolveLease`), the first lease
  where two match, and S3's stamp, with one `statSync` and one read. It acts only when the stamp's
  first line reads `"notice": "every-tool-call"`. Then, where the stamp holds a row, it prints
  `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "mail — <n> unread for
  <slug> · <ids> · local copy <age>s old"}}`. It calls no `readPolicy`, spawns no `git` and makes no
  network call; a subagent's call (`agent_id` set), a session bound to no build, no stamp, any other
  value and any throw exit 0 in silence. Observed by AC4 and AC5.
- **S6** — The detached fetch. Under `every-tool-call`, when the stamp is older than its own
  `fetch-seconds`, the hook creates `<stamp>.fetching` with the exclusive flag and, only when it
  created it, spawns the stamp's `bash` with `<this hook's directory>/unattended.sh --mail notice
  <slug>`, detached, its streams ignored and the child unreferenced, so the call never waits. The verb
  clears the marker when it ends, and a marker older than twice `fetch-seconds` is overwritten.
  Observed by AC4.
- **S7** — The live ring's payload (I25): a ring carries exactly `<mail ref> <message id>` and never a
  fact, and its receiver's one act is the notice fetch. `--mail notice <slug> --ring <ref> <id>` is
  that receiver's entry. It refuses with exit 2 a ref outside I16's grammar,
  `refs/gov/mail/<build>/<tag>/<segment>`, each segment held to the grammar `derive_mail_ref` writes,
  the build the sender's (unit 5 §8 F1), or an id that is not twelve hex digits, then runs S1. A ring
  that never arrives costs the latency until the next boundary or detached fetch, since S1 and S6 read
  the mailbox, never the ring. The sender's side and the `deps.messaging` read are
  `KICK-dKeptSession-6`'s. Observed by AC7.
- **S8** — `mailbox.notice` (`every-tool-call`, `every-item`, `off`; default `every-item`) and
  `mailbox.fetch-seconds` (seconds, at least 10; default 60), both rows landed in
  `tools/policy/catalogue.toml`, owner dKeptSession. `--mail notice` is their one reader, through two
  new arms of `read_lease_policy` (`tools/unattended/unattended.sh#read_lease_policy`), the driver's
  one shell reader of policy keys, to which `KICK-dKeptSession-24` S1 adds `flow.wait-ceiling`: each a
  literal `policy.py get` line, the closed set or the lease bounds' number check, and the catalogue
  default under the reader's one NOTE where no policy kit resolves. A refused `get` reads the
  catalogue default and prints one `unattended: NOTE -` line naming the key and the refusal. The
  boundary verb and the hook read neither key. Both rows gain `summary` and `usage`; `python
  tools/policy/policy.py lists --write` drains them from `tools/policy/unsummarised-keys.txt`, and
  `help/reference/policy.md` is re-rendered by `python tools/playbook/render_playbook.py
  --reference`. Every preset keeps both defaults
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1556`).
  Observed by AC6 and AC9.
- **S9** — The docs: the `--mail` section unit 5 adds to `tools/unattended/VERBS.template.md`
  (rendered to `memory/guides/UNATTENDED-VERBS.md`) gains `--mail notice`, `--local`, `--ring`, the
  stamp and the hook; `help/loop.md` gains the `notice —` line beside unit 10's mailbox interrupt,
  under "Where a build is, and what runs next". Observed by AC8.

## 3. Non-goals (OUT)

- No disposal: answering, acknowledging and the transition guard are `KICK-dKeptSession-5`'s and
  `-25`'s, and the item-boundary interrupt is `KICK-dKeptSession-10`'s.
- No ring transport and no doorbell: the sender's ring is `KICK-dKeptSession-6`'s, and a registered
  doorbell attaches at the point dWellOiledMachine declares in Runtime's `[extend]`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1167`).
- No mail record, ref or kind: unit 5's.
- No catalogue row: the three rows stand, owner dKeptSession, and this unit writes the two mailbox
  rows' `summary` and `usage`; `deps.messaging`'s reader is unit 6's.
- No notice for a `node:<tag>` or `project` recipient: the notice lists what unit 5's guard holds the
  build for, `build:` and `unit:` recipients.
- No item boundary and no boundary verb: `KICK-dKeptSession-13`'s; this unit adds one step inside it.
- No lock on the boundary fetch: two sessions of one build fetching at once each run one bounded
  fetch, which git's ref locks serialise.
- No kit version: the lander mints it (`tools/push-main.sh@78f40c3c2475:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, `run_item_boundary` and the `--card --boundary` verb, the one item-boundary point the notice fetches inside
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its bounded fetch, its rows and states, and the `--mail` verb family this unit adds `notice` and `--local` to
- **hands-off** `KICK-dKeptSession-6` — `deps.messaging`, the channel key the post's ring reads, and I25's payload `<mail ref> <message id>` whose receiver is `--mail notice --ring`
- **consumes-from** external — `tools/unattended/run-lease.js`' `resolveRepo`, `readMemoryRoot`, `resolveLease` and `deriveSidecarPath`, the driver's `resolve_sidecar_dir`, `observe_remote` and `read_lease_policy`, the boundary verb's `run_driver_bounded` and `CARD_CLAIMS_BOUND`, the hook kind's factory, and the landed catalogue rows
- **hands-off** `KICK-dKeptSession-44` — `mail-notice.js`, its binding, reads and spawn, and `--local`, the batch's S3, S6 to S9, S18 and S31 (ids 6, 8, 37, 9, 10, 27, 61), S18's stamp-borne values met by this unit's S3

## 4. Design

### Evidence

- The night pass two, point 3: a fetch takes 0.6 s, tool calls are a median 10.5 s apart, and the
  read point, not the transport, sets how late news arrives (PINNED, its figures,
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b44c7:241`).
- `procmon-hook.js` is the hot-path precedent: it finds its stamp by reading the `.git` pointer files,
  never spawning git (`tools/process-monitor/procmon-hook.js#resolveStamp`), gates its work on one
  `statSync` of the stamp's mtime (`tools/process-monitor/procmon-hook.js#checkThrottled`), and writes
  the stamp after the work (`tools/process-monitor/procmon-hook.js#writeStamp`).
- `run-lease.js` binds a session to its build and derives a sidecar path under the per-worktree git
  dir with no spawn: `resolveRepo` reads the `.git` pointer, `resolveLease` scans the run records, and
  `deriveSidecarPath` joins `<git-dir>/unattended/<kind>.<slug>.log`
  (`tools/unattended/run-lease.js#resolveLease`).
- The JS policy reader spawns: `readPolicy` runs `git rev-parse`, `git cat-file` and the policy shim's
  `landed` on every call (`tools/policy/policy-mirror.js#readPolicy`). Five reads of `mailbox.notice`
  on this node took 269 ms each (PINNED, 2026-11-21), under the default value too.
- `observe_remote` is the driver's one bounded remote call, and `read_claims` makes its fetch through
  it (`tools/unattended/unattended.sh#read_claims`).
- The only `additionalContext` writer in the kits today is scratch-guard's `SubagentStart` arm
  (`tools/hooks/scratch-guard.js#main`); `KICK-dKeptSession-13` S7 adds a PreToolUse one for Bash and
  PowerShell calls, which emits the boundary verb's lines.
- The hook kind's factory writes `<name>.js` and `<name>.fragment.json` beside the kit's descriptor
  and adds a `[[files]]` row only where no `include` matches (`tools/loop/factories.py#write_hook`).

### The boundary, in order

1. The boundary verb answers a crossing (unit 13 S6).
2. `run_mail_notice` runs `--mail notice <slug> --item <key>`. The driver reads both keys: under `off`
   it rewrites the stamp's first line and prints its `off` line; otherwise its bounded fetch, on
   success the stamp rewritten from the fresh rows, on failure the cache rows listed with the stamp's
   age.
3. The verb prints `notice — mail — …`, then runs unit 10's step, with `--local` after a fetch.
4. The verb's lines reach the session at its next shell call after the verb finishes.

### The tool call, in order

1. Parse stdin; leave on `agent_id`, on no `session_id`, on no repository, on no lease for the session.
2. `statSync(stamp)`; no file, leave. Read it; a first line not `every-tool-call`, leave.
3. An mtime older than the first line's `fetch-seconds` starts S6's fetch.
4. No row, leave; else print the `additionalContext` object.

The hook's whole cost is two file reads; its one spawn is the detached fetch, at most once per
`mailbox.fetch-seconds` per build and worktree.

### Why twice the fetch interval

A message posted just after a fetch is fetched by the first tool call past `mailbox.fetch-seconds`,
whose detached fetch rewrites the stamp in about one fetch time; the next call lists it. With tool
calls closer than the interval, that is within twice `mailbox.fetch-seconds` of the post, the bound
the clause states.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/unattended/mail-notice.js`, `tools/unattended/mail-notice.fragment.json` | hook and fragment, first written by the hook kind's factory | none declared for files |
| `readMailNotice`, `checkFetchDue`, `runDetachedFetch`, `renderMailNotice` | JS functions | `js.function`, OK by `lexicon.py --suggest` |
| `write_mail_notice`, `print_mail_notice` | shell functions, the driver | `sh.function`, OK by `lexicon.py --suggest` |
| `run_mail_notice` | shell function, `manifest-check.sh` | `sh.function`, OK by `lexicon.py --suggest` |
| `--mail notice`, `--local`, `--ring`, `--item` | verb and flags of `tools/unattended/unattended.sh` | none |
| `local` | third mode of `read_mailbox` | none |
| `mail-notice.<slug>.log`, `<stamp>.fetching` | sidecar and marker | none |
| `notice —` | boundary verb output line | none |
| `mail-notice-boundary` | plant of `skills/session-kickoff/card-store.fixture.sh` | none |

The stamp's `bash` is `cygpath -m "$BASH"` where `cygpath` resolves and `$BASH` elsewhere, the bash
that ran the driver that wrote it (§8 F6).

### Migration

None: no stamp exists before this unit, and the first notice writes it.

### Rollout

Live with `RUN_CLAIMS`. The hook is wired by its fragment through `settings-merge`. Under the default
`every-item` the hook reads one stamp per call and leaves, and under every value it stays silent until
a first notice writes the stamp.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `--mail notice` and its usage row, `--local`, `--ring`,
  `read_mailbox`'s `local` mode, `write_mail_notice`, `print_mail_notice`, two `read_lease_policy` arms
- `tools/unattended/mail-notice.js`: the hook, over the factory's file
- `tools/unattended/mail-notice.fragment.json`: its fragment, the factory's
- `.claude/settings.json`: the `PostToolUse` entry, merged from the fragment by `settings-merge.py`
- `skills/session-kickoff/manifest-check.sh`: `run_mail_notice` inside `--card --boundary`
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: the `mail-notice-boundary` plant
- `skills/session-kickoff/manifest-check.test.sh`: its arm
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: the `--mail` section's notice rows
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/policy/catalogue.toml`: the two mailbox rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `help/reference/policy.md`: re-rendered by `render_playbook.py --reference`
- `help/loop.md`: the `notice —` line

### Alternatives rejected

- **The hook running `--mail read` per call.** A driver process per tool call, where the stamp costs
  one file read; and the driver's fetch would put the network back on the call path.
- **A JS parser of the mail refs in the hook.** A second reader of unit 5's record beside
  `read_mailbox`.
- **A node-wide stamp in the git common dir.** Two builds' notices would rewrite one list; the
  per-worktree sidecar keys the list by build, as the stop and stall sidecars already are.
- **The policy read in the hook through `readPolicy`**, or the values in a second sidecar the
  boundary verb writes (§8 F5).

## 5. Production-readiness checklist

- security — the hook writes only its marker and spawns one fixed argv, the bash the stamp records
  and the driver beside the hook; `--ring` validates both fields before any read; the
  `additionalContext` carries ids and a slug, never a message body.
- perf / scale — at a boundary one bounded fetch; at a tool call one `statSync` and one small file
  read, and at most one detached fetch per interval, with no git and no policy spawn.
- error / empty / loading states — a failed fetch prints the local copy with its age; no stamp reads
  as age unknown at the verb and as silence in the hook; a hook throw is silent.
- observability — `notice —` at each boundary, the hook's line at each call that has news.
- risks — a hook on every tool adds a node start per call; a value changed in the policy file reaches
  the hook at the next notice, a boundary's or its own detached fetch's, within `mailbox.fetch-seconds`
  under `every-tool-call`.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`, `help/loop.md` and `help/reference/policy.md`.

## 6. Acceptance criteria

- **AC1** — When clone A posts a `question` to `build:<slug>` and clone B, at its next item boundary,
  runs `bash tools/unattended/unattended.sh --mail notice <slug> --item <key>`, B prints
  `mail — 1 unread for <slug> · <id> · fetched · item <key>`; a scratch copy of the driver whose
  notice skips its fetch prints `mail — none`. This is the clause's message posted on one node shown
  on another at its next item boundary, red where the boundary's fetch misses it.
  Red when: the boundary lists only what the node already held.
  fixture: two scratch clones of one bare origin under `%TEMP%`, `RUN_CLAIMS=on`, two fleet tags.
- **AC2** — When B's origin is pointed at a missing path after one successful notice, and A's message
  is already in B's cache, `bash tools/unattended/unattended.sh --mail notice <slug>` exits 0 and prints
  the id with ` · local copy <n>s old (` and the fetch's cause, `<n>` within two seconds of the
  stamp's age by `stat`, and the stamp's mtime is unchanged; `--mail notice <slug> --local` prints
  the id with ` · local copy <n>s old (--local)` and no `mail — local copy:` cause line, since it
  attempts no fetch. This is the clause's fetch planted to fail.
  Red when: a failed fetch prints nothing or names no age, or `--local` fetches.
- **AC3** — When `bash skills/session-kickoff/card-store.fixture.sh --plant mail-notice-boundary` runs
  `--card --boundary` across a crossing with one message in B's mailbox, the output holds
  `notice — mail — 1 unread` before unit 10's `interrupt — mailbox` line and the stub engine records
  `--mail-interrupts --local`; with `mailbox.notice = "off"` planted it holds no `notice —` line, unit
  10's line still lists the message and the stub records no `--local`; with no crossing it runs no
  notice.
  Red when: a crossing shows no notice, `off` silences the disposal, or a boundary fetches twice.
- **AC4** — When `mailbox.notice = "every-tool-call"` and `mailbox.fetch-seconds = 10` are planted on
  B, one `--mail notice <slug>` on B writes the stamp, A posts, and B's hook is fed one `PostToolUse`
  payload for B's session every two seconds through `node mail-notice.js` in the unattended kit, a
  payload within 20 seconds of the post (PINNED, twice the planted interval) prints an `additionalContext`
  naming the id, and `<stamp>.fetching` was created once per interval; with S6 stubbed to spawn
  nothing, no payload names it. This is the clause's next tool call within twice the fetch interval.
  Red when: the hook never fetches, or fetches on every call.
  figure: the interval, the cadence and the window are PINNED fixture literals.
- **AC5** — When B's origin is unreachable and the stamp is fresh, `node mail-notice.js` in the
  unattended kit fed one payload returns in under 500 ms (PINNED) with the stamp's ids, and a payload with `agent_id`
  set, or for a session bound to no build, prints nothing;
  `grep -c 'execFileSync\|spawnSync\|readPolicy' mail-notice.js` prints 0 there.
  Red when: the tool call waits on the network, spawns `git`, or reads the policy kit.
- **AC6** — When the policy reads of `mailbox.notice` and `mailbox.fetch-seconds` are refused,
  `--mail notice <slug>` prints the notice as `every-item` and one `unattended: NOTE -` line naming
  each key, and the stamp's first line reads `"notice": "every-item"`, so the hook fed a payload
  prints nothing.
  Red when: a refused read changes the behaviour from the default.
- **AC7** — When `--mail notice <slug> --ring <ref> <id>` runs with a ref outside
  `refs/gov/mail/<build>/<tag>/<segment>` or an id of eleven hex digits, it exits 2 and fetches
  nothing; with a valid pair it prints S1's line. With `deps.messaging = "live-and-mailbox"` and no
  ring ever delivered, AC1's boundary still shows the message.
  Red when: a ring carries a fact the receiver acts on, or a lost ring loses the message.
- **AC8** — When `grep -n -- '--mail notice\|--local\|--ring\|mail-notice'` runs over
  `tools/unattended/VERBS.template.md`, and `grep -n 'notice —' help/loop.md`, each is found.
  Red when: the notice is undocumented.
- **AC9** — When `python tools/policy/policy.py get mailbox.notice` and `get mailbox.fetch-seconds`
  run in a repository whose policy file sets neither, they print `every-item` and `60`, and after
  `policy.py lists --write` `tools/policy/unsummarised-keys.txt` names neither key.
  Red when: either row is still unsummarised.

## 7. Gates

`unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `routed-commits selftest` · `policy check` · `help reference pages` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `docs` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC4 AC5 AC6 AC7 · the notice arms over two clones and one bare origin, AC1 staged by a scratch copy that skips the fetch and AC4 by a stubbed spawn · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 · the `mail-notice-boundary` plant, red with the notice step left out of the boundary verb · none

## 8. Open questions

- **FACT-QUESTION · F1 — Which hook event's output reaches the model at a tool call?** Probe: the
  installed CLI's bundled source, read with `grep -a -o '.\{0,160\}hook_additional_context.\{0,160\}'
  <CLI binary>`. Observation, 2026-10-26, on Claude Code 2.1.308: the output schema admits
  `additionalContext` under both `PreToolUse` and `PostToolUse`, and the CLI builds a
  `hook_additional_context` attachment message with `hookEvent:"PostToolUse"` from a `PostToolUse`
  hook's `additionalContext`, the message type the model reads. Re-probed 2026-11-21 on the binary
  PATH names, 2.1.319, this run's `RUN.md` recording 2.1.326: 42 lines (PINNED) name the
  attachment type, their builders naming `PostToolUse` five times and `PreToolUse` once, so the 2026-10-26
  line that no `PreToolUse` builder was seen is superseded; PreToolUse's channel is
  `KICK-dKeptSession-13` S7's, for Bash and PowerShell calls only. Liveness: the grep would return no
  `PostToolUse` builder if that event's context were dropped. RESOLVED (agent, 2026-10-26,
  delegated): a `PostToolUse` hook printing `hookSpecificOutput.additionalContext`, rung 2; the build
  run re-observes it in a live session. widens: none · relaxes: none
- **F2 — Where does the notice stamp live, and what does it hold?** I24 proposed
  `<git-common-dir>/gov-mail-fetch.stamp`, its mtime the local copy's age. Options: (a) the per-worktree
  sidecar `<git-dir>/unattended/mail-notice.<slug>.log`, holding the build's unread rows, its mtime the
  age, so the hook reads both with no `git` and no second reader; (b) I24's node-wide stamp, which the
  hook cannot find without spawning `git rev-parse --git-common-dir` and which holds no rows, so the
  hook must read the refs itself. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the shared
  interface refined as its owner may, said in this unit's return. widens: none · relaxes: none
- **F3 — Which recipients count as addressed to the session's build or item?** Options: (a) the rows
  `check_mail_addressed <to> build:<slug>` admits, `build:<slug>` and a `unit:` of the build, the set
  `KICK-dKeptSession-10` §8 F1 settled and unit 5's guard holds; (b) only those naming the item in
  flight, which I14 cannot address, since its grammar names a unit and no item. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, cl-dClosedLoop-0143's "a message addressed to the build".
  widens: none · relaxes: none
- **F4 — Does the boundary fetch twice when both the notice and unit 10's interrupt read?** Options:
  (a) the notice fetches and the interrupt reads `--local` at the same boundary; (b) each fetches, two
  network round trips per item. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's
  "one fetch of the mail refs". widens: none · relaxes: none
- **F5 — How does the hook learn `mailbox.notice` and `mailbox.fetch-seconds` without the git spawns
  `readPolicy` makes?** Options: (a) `readPolicy` per call, through `policy-mirror.js`, which spawns
  git and the policy shim on every call under every value, the default included, against AC5; (b)
  `--mail notice`, the one reader of both keys, writes them as S3's stamp's first line, and the hook
  reads them with the stamp's read, a changed value reaching it at the next notice; (c)
  `KICK-dKeptSession-44` S18's form, the boundary verb writing them into a second sidecar beside the
  stamp, a second writer in a second kit spelling the sidecar root that `resolve_sidecar_dir` keeps to
  one line, and two reads per call. RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; veto 1
  discards (a) through AC5, and (b) keeps one file, one writer and the sidecar root's one spelling.
  widens: none · relaxes: none
- **F6 — Which bash does the hook's detached fetch run?** Options: (a) the bash that ran the driver
  that wrote the stamp, recorded in its first line as a native path, proven to see the driver; (b)
  scratch-guard's `resolveCardBash` carried inline, which probes each candidate with `spawnSync`,
  against AC5; (c) the bare name `bash`, which on a Windows PATH can resolve the WSL launcher that
  cannot open a `C:/` path, so the fetch would never run and nothing would say so. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3; veto 1 discards (b) through AC5, and (c) fails in silence.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 21, scout B row 4 and its
  disagreement 7, Shared interfaces I8, I12, I14, I16, I19, I20, I24 and I25, the night pass two,
  point 3, and v2's three mailbox rows and their preset rows.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-11-21 · §7 · the leg line names `tier2-review self-test`, the leg whose manifest
  guard §4's `tools/unattended/unattended.sh` trips, as the spec-tokens guards join named at the
  build run's spec stage under the brief `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`; no
  other section moved.
- rev-4 · 2026-11-21 · §1 · S1 to S9 · §3 · §4 · §5 · AC1 to AC9 · §7 · §8 F1 F5 F6 · §10 ·
  re-grounded on the landed tree at `c2a407b0` by
  `2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief`: the JS `readPolicy` spawns git,
  so the driver's notice is the one reader of both keys, through `read_lease_policy`, and writes them
  with the bash it ran under into the stamp's first line, which the hook reads (F5, F6); S4 runs the
  notice through `run_driver_bounded` and its lines reach the session at the next shell call after
  unit 13's detached verb ends; S2 adds `--local` as a third `read_mailbox` mode; S5 takes the hook
  from the hook kind's factory; S7's ring ref is the sender's, per unit 5 §8 F1; F1 re-probed;
  unit 10's line reads `interrupt — mailbox`. Narrowed: the boundary verb and the hook read no policy;
  the catalogue rows stand, given their summaries by S8 and AC9; the kit version and the
  `subject-pins.tsv` regeneration left §4, and `kit epoch` and the five govkit legs left §7, which
  gained `policy fixtures`, `routed-commits selftest`, `policy check`, `help reference pages` and
  `docs`. Every line-number citation became a `path#symbol` or blob pin.

## 10. Reuse audit

The seams extended are `read_mailbox`'s bounded fetch (unit 5's, made through
`tools/unattended/unattended.sh#observe_remote`, as `tools/unattended/unattended.sh#read_claims`
makes its own), gaining a `local` mode; the driver's one shell policy reader,
`tools/unattended/unattended.sh#read_lease_policy`; the hot-path stamp throttle of
`tools/process-monitor/procmon-hook.js#checkThrottled`; `run-lease.js`' git-free `resolveRepo`,
`resolveLease` and `deriveSidecarPath` (`tools/unattended/run-lease.js#deriveSidecarPath`); the
kickoff engine's bounded driver call, `skills/session-kickoff/manifest-check.sh#run_driver_bounded`;
and the hook kind's factory, `tools/loop/factories.py#write_hook`. The sidecar path and the
session-to-build binding are reused, not copied. The detached spawn is new, as scout B found: `grep
-rn 'detached' tools --include=*.js` finds only detached-HEAD mentions, no detached child. `python
tools/codebase-map/reuse_lookup.py "show unread message ids at every tool call from a local copy"`,
re-run at this writing, ranked `ids`, `derive_tool_root`, `inventory_ids`, `derive_tool_rel`,
`resolve_tool_path` and `read_session_ids` by name stem, none a notice. Scout B's disagreement 7,
that a `PreToolUse` hook's `additionalContext` was unprobed, is §8 F1, re-probed; its suggested
common-dir stamp is refined by §8 F2.

Recall terms used: mailbox.notice every-tool-call fetch-seconds hook additionalContext local copy detached fetch stamp unread ids read_lease_policy run_driver_bounded
