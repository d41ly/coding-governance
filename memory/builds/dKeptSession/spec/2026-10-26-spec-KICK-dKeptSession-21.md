# KICK-dKeptSession-21 — news shown as `mailbox.notice` says: one bounded fetch at each item boundary, a tool-call hook reading the local copy, and the live ring's payload

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 22 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0159@ad40c608 whole
**Carries:** node:policy-key.mailbox.notice
**Carries:** node:policy-key.mailbox.fetch-seconds
**Carries:** node:policy-key.deps.messaging

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
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
waits for the reader's read points, not the transport: a fetch takes 0.6 s, the median gap between
pass commits is 7.5 minutes (gap-conc-05).

## 2. Scope (IN)

- **S1** — The notice verb, `unattended.sh --mail notice <slug> [--item <instance key>]` (I19's member
  this unit owns). It calls `KICK-dKeptSession-5`'s `read_mailbox <slug> soft` (its S6), whose one
  bounded fetch of `+refs/gov/mail/*:refs/gov/remote/mail/*` runs through `observe_remote` and
  `REMOTE_BOUND` (`tools/unattended/unattended.sh:480`), keeps the rows in state `open`, which that
  reader admits by `check_mail_addressed <to> build:<slug>` (`KICK-dKeptSession-28`), and prints one
  line: `mail — <n> unread for <slug> · <id> <id> … · fetched`, or `mail — none for <slug> · fetched`.
  `--item` adds ` · item <instance key>` to the line. Observed by AC1.
- **S2** — The fallback. When that fetch fails or its bound fires, the `soft` reader reads the node's
  local copy, the cache `refs/gov/remote/mail/…` (I16), and names its cause (unit 5 S6); the notice
  ends its line ` · local copy <age>s old (<why>)`, the age read from the notice stamp of S3, or
  ` · local copy age unknown (<why>)` with no stamp, and exits 0. This unit adds `--local` to
  `--mail read` and to `--mail notice`: a read of the cache with no fetch, which unit 10's read at a
  boundary the notice already fetched for uses. Observed by AC2.
- **S3** — The notice stamp (I24, refined here, §8 F2): the sidecar
  `<git-dir>/unattended/mail-notice.<slug>.log`, the path `deriveSidecarPath(gitDir, 'mail-notice',
  slug)` in `tools/unattended/run-lease.js:179` and `resolve_sidecar_dir` in the driver already
  derive, rewritten whole by every successful notice fetch with one JSON line per unread row, `{"id":
  …, "kind": …, "to": …}`, through a unique temp file renamed into place. Its mtime is the age of the
  local copy this build's notice last fetched. A failed fetch leaves it untouched. Observed by AC2 and
  AC4.
- **S4** — The item boundary. Inside `KICK-dKeptSession-13`'s boundary verb, `manifest-check.sh
  --card --boundary --build <slug> --session <sid>` (its S6), once `derive_item_boundary` (I12)
  answers a crossing and `mailbox.notice` is `every-item` or `every-tool-call`, one step runs
  `bash <kit>/unattended.sh --mail notice <slug> --item <key>`, resolved as unit 5 S13 runs its read
  from that file (`resolve_kit_file unattended unattended.sh`, bounded by `CARD_CLAIMS_BOUND`,
  `skills/session-kickoff/manifest-check.sh:228`), and prints `notice — <the verb's line>` before
  `KICK-dKeptSession-10`'s step, which it hands `--local` when the line ends ` · fetched`, so a
  boundary costs one fetch. Under `off` it prints no notice and unit 10's read fetches as it says. The
  verb's output reaches the session through unit 13's S7. Observed by AC1, AC3 and AC6.
- **S5** — The tool-call hook, `tools/unattended/mail-notice.js`, a `PostToolUse` hook on every tool
  (§8 F1), its fragment `tools/unattended/mail-notice.fragment.json` in `gate-guard.fragment.json`'s
  shape. Per call it reads the payload's `session_id`, the repository through `run-lease.js`'s
  `resolveRepo`, the build through `resolveLease(root, memoryRoot, sessionId)`
  (`tools/unattended/run-lease.js:173`), and `mailbox.notice` and `mailbox.fetch-seconds` through I8's
  JS reader `readPolicy(key, {repo})` (TOOL-dGroundRules-5 S5), found beside this kit's directory as
  TOOL-dGroundRules-10 S5 finds it. Under `every-tool-call` it reads S3's stamp with one `statSync`
  and one read, and when the stamp holds a row prints
  `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "mail — <n> unread for
  <slug> · <ids> · local copy <age>s old"}}`. It spawns no `git` and makes no network call; a
  subagent's call (`agent_id` set), a session bound to no build, any other value and any throw exit 0
  in silence. Observed by AC4 and AC5.
- **S6** — The detached fetch. When the stamp is absent or older than `mailbox.fetch-seconds`, the hook
  creates `<stamp>.fetching` with the exclusive flag and, only when it created it, spawns
  `bash <kit>/unattended.sh --mail notice <slug>` detached with its streams ignored and unreferenced,
  so the call never waits; the verb clears the marker when it ends, and a marker older than twice
  `mailbox.fetch-seconds` is overwritten. Observed by AC4.
- **S7** — The live ring's payload (I25): a ring carries exactly `<mail ref> <message id>` and never a
  fact, and its receiver's one act is the notice fetch. `--mail notice <slug> --ring <ref> <id>` is
  that receiver's entry: it refuses with exit 2 a ref outside I16's grammar for `<slug>` or an id that
  is not twelve hex digits, then runs S1. A ring that never arrives costs the latency until the next
  boundary or detached fetch, since S1 and S6 read the mailbox, never the ring. The sender's side and
  the `deps.messaging` read are `KICK-dKeptSession-6`'s. Observed by AC7.
- **S8** — `mailbox.notice` (`every-tool-call`, `every-item`, `off`; default `every-item`) and
  `mailbox.fetch-seconds` (seconds, at least 10; default 60), read in the driver and the boundary verb
  through I8's shell form, `python <prefix>/policy/policy.py get <key>`, a refusal reading the
  catalogue default with one NOTE naming the key; the hook reads them silently, a refusal reading the
  default. Every preset sets both to their
  defaults (v2:1556-1557). Observed by AC3 and AC6.
- **S9** — The docs: the `--mail` section of `tools/unattended/VERBS.template.md` (rendered to
  `memory/guides/UNATTENDED-VERBS.md`) gains `--mail notice`, `--local`, `--ring`, the stamp and the
  hook; `help/loop.md` gains the `notice —` line. Observed by AC8.

## 3. Non-goals (OUT)

- No disposal: answering, acknowledging and the transition guard are `KICK-dKeptSession-5`'s and
  `-25`'s, and the item-boundary interrupt is `KICK-dKeptSession-10`'s.
- No ring transport and no doorbell: the sender's ring is `KICK-dKeptSession-6`'s, and a registered
  doorbell attaches at the point dWellOiledMachine declares in Runtime's `[extend]` (v2:1167).
- No mail record, ref or kind: unit 5's.
- No catalogue rows: dGroundRules-1 S3 writes `mailbox.notice`, `mailbox.fetch-seconds` and
  `deps.messaging`, owner dKeptSession (`tools/policy/catalogue.toml` on dGroundRules' branch).
- No notice for a `node:<tag>` or `project` recipient: the notice lists what unit 5's guard holds the
  build for, `build:` and `unit:` recipients.
- No item boundary and no boundary verb: `KICK-dKeptSession-13`'s; this unit adds one step inside it.
- No lock on the boundary fetch: two sessions of one build fetching at once each run one bounded
  fetch, which git's ref locks serialise.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary` and the `--card --boundary` verb, the one item-boundary point the notice fetches inside
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its bounded fetch, its rows and states, and the `--mail` verb family this unit adds `notice` and `--local` to
- **hands-off** `KICK-dKeptSession-6` — `deps.messaging`, the channel key the post's ring reads, and I25's payload `<mail ref> <message id>` whose receiver is `--mail notice --ring`
- **consumes-from** external — `tools/unattended/run-lease.js`' `resolveRepo`, `resolveLease` and `deriveSidecarPath`, the boundary verb's `resolve_kit_file` and `CARD_CLAIMS_BOUND`, and dGroundRules' `readPolicy` and `resolve`
- **hands-off** `KICK-dKeptSession-44` — `mail-notice.js`, its binding, reads and spawn, and `--local`, the batch's S3, S6 to S9, S18 and S31 (ids 6, 8, 37, 9, 10, 27, 61)

## 4. Design

### Evidence

- The night pass two, point 3 (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:241-247`):
  a fetch takes 0.6 s, the median gap between pass commits is 7.5 minutes, tool calls are a median
  10.5 s apart, and the read point, not the transport, sets how late news arrives.
- `procmon-hook.js` is the hot-path precedent: a `PostToolUse` hook that gates its work on one
  `statSync` of a stamp's mtime (`tools/process-monitor/procmon-hook.js:89-96`) and writes the stamp
  after the work, never before (:111-112).
- The only `additionalContext` producer at base is the `SubagentStart` arm of
  `tools/hooks/scratch-guard.js:1545`; plain stdout of a `PostToolUse` hook does not reach the model,
  which is why procmon's report is a transcript line.
- `run-lease.js` already binds a session to its build (`resolveLease`, :173) and derives a sidecar
  path under the per-worktree git dir (`deriveSidecarPath`, :179-181), git-free.
- `observe_remote` (`tools/unattended/unattended.sh:480`) is the driver's one bounded remote call;
  `read_claims` makes its fetch through it at :2136.
- `KICK-dKeptSession-13` S6 makes `--card --boundary` the one item-boundary point and names
  `mailbox.notice` among the readers that run inside it; its S7 prints the verb's output to the
  session.

### The boundary, in order

1. The boundary verb answers a crossing and resolves `mailbox.notice`; `off` skips to unit 10's step.
2. `--mail notice <slug> --item <key>`: the bounded fetch; on success the stamp is rewritten from the
   fresh rows; on failure the `soft` reader's cache rows are listed and the line names the stamp's age.
3. The verb prints `notice — mail — …`, then runs unit 10's step, with `--local` after a fetch.

### The tool call, in order

1. Parse stdin; leave on `agent_id`, on no `session_id`, on no lease for the session.
2. `readPolicy('mailbox.notice')`; leave unless `every-tool-call`.
3. `statSync(stamp)`: no file, or an mtime older than `mailbox.fetch-seconds`, starts S6's fetch.
4. Read the stamp's lines; none, leave; else print the `additionalContext` object.

The hook's whole cost is file reads; its one spawn is the detached fetch, at most once per
`mailbox.fetch-seconds` per build and worktree.

### Why twice the fetch interval

A message posted just after a fetch is fetched by the first tool call past `mailbox.fetch-seconds`,
whose detached fetch rewrites the stamp in about one fetch time; the next call lists it. With tool
calls closer than the interval, that is within twice `mailbox.fetch-seconds` of the post, the bound
the clause states.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/unattended/mail-notice.js` | hook module | none declared for files |
| `readMailNotice`, `checkFetchDue`, `runDetachedFetch`, `renderMailNotice` | JS functions | `js.function`, verb-first |
| `write_mail_notice`, `print_mail_notice` | shell functions | `write`, `print`, OK |
| `--mail notice`, `--local`, `--ring`, `--item` | verb and flags of `tools/unattended/unattended.sh` | none |
| `mail-notice.<slug>.log`, `<stamp>.fetching` | sidecar and marker | none |
| `notice —` | boundary verb output line | none |
| `mail-notice-boundary` | plant of `skills/session-kickoff/card-store.fixture.sh` | none |

### Migration

None: no stamp exists before this unit; the first notice writes it.

### Rollout

Live with `RUN_CLAIMS`. The hook is wired by the kit's fragment through `settings-merge`; under the
default `every-item` it reads one policy value per call and returns.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `--mail notice`, `--local`, `--ring`, `write_mail_notice`,
  `print_mail_notice`, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/mail-notice.js`: the hook
- `tools/unattended/mail-notice.fragment.json`: its fragment
- `.claude/settings.json`: the `PostToolUse` entry, merged from the fragment by `settings-merge.py`
- `skills/session-kickoff/manifest-check.sh`: the notice step inside `--card --boundary`
- `skills/session-kickoff/card-store.fixture.sh`: the `mail-notice-boundary` plant
- `skills/session-kickoff/manifest-check.test.sh`: its arm
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: the `--mail` section's notice rows
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `help/loop.md`: the `notice —` line
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **The hook running `--mail read` per call.** A driver process per tool call, where the stamp costs one
  file read; and the driver's fetch would put the network back on the call path.
- **A JS parser of the mail refs in the hook.** A second reader of I17's record beside I20.
- **A node-wide stamp in the git common dir.** Two builds' notices would rewrite one list; the
  per-worktree sidecar keys the list by build, as the stop and stall sidecars already are.

## 5. Production-readiness checklist

- security — the hook writes only its marker and spawns one fixed argv; `--ring` validates both
  fields before any read; the `additionalContext` carries ids and a slug, never a message body.
- perf / scale — at a boundary one bounded fetch; at a tool call one policy read, one `statSync`, one
  small file read, and at most one detached fetch per interval.
- error / empty / loading states — a failed fetch prints the local copy with its age; no stamp reads as
  age unknown and starts a fetch; a hook throw is silent.
- observability — `notice —` at each boundary, the hook's line at each call that has news.
- risks — a hook on every tool adds a node start per call (`PostToolUse` already runs two hooks here);
  under the default value it returns after one read.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md` and `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When clone A posts a `question` to `build:<slug>` and clone B, at its next item boundary,
  runs `bash tools/unattended/unattended.sh --mail notice <slug> --item <key>`, B prints
  `mail — 1 unread for <slug> · <id> · fetched · item <key>`; a scratch copy of the driver whose notice
  skips its fetch prints `mail — none`. This is the
  clause's message posted on one node shown on another at its next item boundary, red where the
  boundary's fetch misses it.
  Red when: the boundary lists only what the node already held.
  fixture: two scratch clones of one bare origin under `%TEMP%`, `RUN_CLAIMS=on`, two fleet tags.
- **AC2** — When B's origin is pointed at a missing path after one successful notice, and A's message
  is already in B's cache, `bash tools/unattended/unattended.sh --mail notice <slug>` exits 0 and prints
  the id with ` · local copy <n>s old (` and the fetch's cause, `<n>` within two seconds of the
  stamp's age by `stat`, and the stamp's mtime is unchanged. This is the clause's fetch planted to fail.
  Red when: a failed fetch prints nothing, or names no age.
- **AC3** — When `bash card-store.fixture.sh --plant mail-notice-boundary` runs `--card --boundary` across
  a crossing with one message in B's mailbox, the output holds `notice — mail — 1 unread` before unit
  10's `interrupt — mail` line and the stub driver records that read with `--local`; with
  `mailbox.notice = "off"` planted it holds no `notice —` line and unit 10's line still lists the
  message; with no crossing it runs no notice.
  Red when: a crossing shows no notice, `off` silences the disposal, or a boundary fetches twice.
- **AC4** — When `mailbox.notice = "every-tool-call"` and `mailbox.fetch-seconds = 10` are planted on
  B, A posts, and B's hook is fed one `PostToolUse` payload for B's session every two seconds through
  `node mail-notice.js`, a payload within 20 seconds of the post prints an `additionalContext` naming
  the id, and `<stamp>.fetching` was created once per interval; with S6 stubbed to spawn nothing, no
  payload names it. This is the clause's next tool call within twice the fetch interval.
  Red when: the hook never fetches, or fetches on every call.
- **AC5** — When B's origin is unreachable and the stamp is fresh, `node mail-notice.js` fed one
  payload returns in under 500 ms with the stamp's ids, and a payload with `agent_id` set, or for a
  session bound to no build, prints nothing; `grep -c 'execFileSync\|spawnSync' mail-notice.js`
  prints 0.
  Red when: the tool call waits on the network or spawns `git`.
- **AC6** — When the policy reads of `mailbox.notice` and `mailbox.fetch-seconds` are refused, the
  boundary verb prints the notice as `every-item` and one NOTE naming each key, and the hook prints nothing.
  Red when: a refused read changes the behaviour from the default.
- **AC7** — When `--mail notice <slug> --ring <ref> <id>` runs with a ref outside
  `refs/gov/mail/<slug>/` or an id of eleven hex digits, it exits 2 and fetches nothing; with a valid
  pair it prints S1's line. With `deps.messaging = "live-and-mailbox"` and no ring ever delivered, AC1's
  boundary still shows the message.
  Red when: a ring carries a fact the receiver acts on, or a lost ring loses the message.
- **AC8** — When `grep -n -- '--mail notice\|--local\|--ring\|mail-notice'` runs over
  `tools/unattended/VERBS.template.md`, and `grep -n 'notice —'` over `loop.md`, the loop kit's help page, each is found.
  Red when: the notice is undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `manifest-check self-test` · `scratch-guard self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC4 AC5 AC6 AC7 · the notice arms over two clones and one bare origin, AC1 staged by a scratch copy that skips the fetch and AC4 by a stubbed spawn · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 · the `mail-notice-boundary` plant, red with the notice step left out of the boundary verb · none

## 8. Open questions

- **FACT-QUESTION · F1 — Which hook event's output reaches the model at a tool call?** Probe: the
  installed CLI's bundled source, read with `grep -a -o '.\{0,160\}hook_additional_context.\{0,160\}'
  <CLI binary>` (Claude Code 2.1.308, the version this run's `RUN.md` records). Observation,
  2026-10-26: the output schema admits `additionalContext` under both `PreToolUse` and `PostToolUse`,
  and the CLI builds a `hook_additional_context` attachment message with `hookEvent:"PostToolUse"`
  from a `PostToolUse` hook's `additionalContext`, the message type the model reads; no such builder
  was seen naming `PreToolUse`. Liveness: the grep would return no `PostToolUse` builder if that
  event's context were dropped, and returned 23 lines naming the attachment type. RESOLVED (agent,
  2026-10-26, delegated): a `PostToolUse` hook printing `hookSpecificOutput.additionalContext`, rung 2;
  the build run re-observes it in a live session. widens: none · relaxes: none
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
  flight, which I14 cannot address, since its grammar names a unit and no item. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, cl-dClosedLoop-0143's "a
  message addressed to the build". widens: none · relaxes: none
- **F4 — Does the boundary fetch twice when both the notice and unit 10's interrupt read?** Options:
  (a) the notice fetches and the interrupt reads `--local` at the same boundary; (b) each fetches, two
  network round trips per item. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's
  "one fetch of the mail refs". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 21, scout B row 4 and its
  disagreement 7, Shared interfaces I8, I12, I14, I16, I19, I20, I24 and I25, the night pass two,
  point 3, and v2:1234-1235, v2:1556-1557.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.

## 10. Reuse audit

The seams extended are `read_mailbox`'s bounded fetch (I20, unit 5's, made through
`observe_remote`, `tools/unattended/unattended.sh:480`, as `read_claims` makes its own at :2136), the
hot-path stamp throttle of `tools/process-monitor/procmon-hook.js:89-96`, and `run-lease.js`'
`resolveRepo`, `resolveLease` (:173) and `deriveSidecarPath` (:179), each verified at this writing.
The sidecar path derivation is reused, not copied, and so is the session-to-build binding; the
detached spawn is new, as scout B found (`grep -rn 'detached\|unref' tools` finds none). `python
tools/codebase-map/reuse_lookup.py "show unread message ids at every tool call from a local copy"`
ranked `ids`, `inventory_ids`, `read_session_ids` and `derive_tool_class`, name stems only, none a
notice. `python tools/memory-recall/query.py "how is a session shown unread mail at a tool call"`
returned this build's brief, v2's `mailbox.notice` row and scout B's row 4; scout B's disagreement 7,
that a `PreToolUse` hook's `additionalContext` was unprobed, is §8 F1, and its suggested common-dir
stamp is refined by §8 F2.

Recall terms used: mailbox.notice every-tool-call fetch-seconds hook additionalContext local copy detached fetch stamp unread ids
