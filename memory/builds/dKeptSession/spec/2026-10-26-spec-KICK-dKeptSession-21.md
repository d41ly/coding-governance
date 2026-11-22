# KICK-dKeptSession-21 — news shown as `mailbox.notice` says: one bounded fetch at each item boundary, a tool-call hook reading the local copy, and the live ring's payload

**Status:** DEFERRED · rev-6 · 2026-11-23 · node a · Tier-2 · base b2303b53 · streams kickoff · order 22 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-6 KICK-dKeptSession-5 |
| [2026-11-22-prompt-KICK-dKeptSession-21-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-21-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-21-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-21-1-spec-writer.md) | journal | — |
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

- **S1** — The notice verb, `unattended.sh --mail notice <slug> [--item <instance key>] [--local]
  [--ring <ref> <id>]`, a member of `KICK-dKeptSession-5`'s `--mail` family (its S8) with that
  usage-header row. The `--mail` arm (`tools/unattended/unattended.sh@a11693ddbd88:19829`) parses
  `--local`, and `--ring` with the two words after it, else `mail — not read · --ring takes a ref
  and an id`; its unknown-flag and unknown-verb refusals name the three words beside those units 24,
  25 and 27 add. The `notice` form takes one word and no flag but `--item`, `--local` and `--ring`,
  else `mail — not read · the form is` and the usage; `read` gains `--local`; `post`, `ack` and
  `answer` refuse both. It reads both keys (S8). Under `off` it fetches nothing, rewrites S3's
  stamp with its first line alone, prints `mail — notice off for <slug> (mailbox.notice: off)` and
  exits 0. Otherwise it calls `read_mailbox <slug> soft` (unit 5
  S6), whose one bounded fetch of `+refs/gov/mail/*:refs/gov/remote/mail/*` runs through
  `observe_remote` under `REMOTE_BOUND` (`tools/unattended/unattended.sh#observe_remote`). It keeps the
  rows in state `open`, which that reader admits by `check_mail_addressed <to> build:<slug>`
  (`KICK-dKeptSession-28`), and prints one line: `mail — <n> unread for <slug> · <id> <id> … ·
  fetched`, or `mail — none for <slug> · fetched`. `--item` appends ` · item <instance key>`.
  Observed by AC1.
- **S2** — The fallback, and `--local`. When that fetch fails or its bound fires, the `soft` reader
  reads the node's cache `refs/gov/remote/mail/…` and prints `mail — local copy: <why>` on stderr
  (`tools/unattended/unattended.sh#read_mailbox`), which the notice passes through and whose `<why>`
  ends its line ` · local copy <age>s old (<why>)`, the age read from S3's stamp, or ` · local copy
  age unknown (<why>)` with no stamp, leaves the stamp untouched and exits 0. This unit adds
  `local`, a third mode of `read_mailbox <who> soft|strict|local` that reads the cache with no fetch and prints no cause,
  and the flag `--local` on `--mail read`, `print_mailbox` passing the mode, and on `--mail notice`.
  `--mail notice --local` ends its line ` · local copy <age>s old (--local)`.
  `KICK-dKeptSession-10`'s `read_mail_rows(…, local=True)` appends `--local` to its `--mail read
  <slug>`, so the refusal its S4 prints as `unarmed` until this unit lands stops. Observed by AC2.
- **S3** — The notice stamp (I24, refined here, §8 F2): the sidecar
  `<git-dir>/unattended/mail-notice.<slug>.log`, the path `deriveSidecarPath(gitDir, 'mail-notice',
  slug)` (`tools/unattended/run-lease.js#deriveSidecarPath`) and `resolve_sidecar_dir`
  (`tools/unattended/lib-unattended.sh#resolve_sidecar_dir`) both derive, the root never respelled.
  `write_mail_notice` rewrites it whole after every notice that fetched, and after an `off` notice,
  through a unique temp file renamed into place. Its first line is `{"notice": <value>, "fetch-seconds": <n>, "bash":
  <path>}` (§8 F5, F6), then one JSON line per unread row, `{"id": …, "kind": …, "to": …}`. Its mtime
  is the age of the local copy this build's notice last fetched. A failed or `--local` notice leaves
  it untouched. Observed by AC2 and AC4.
- **S4** — The item boundary. `run_mail_notice <slug> <key>` in
  `skills/session-kickoff/manifest-check.sh` runs in the crossing branch of
  `skills/session-kickoff/manifest-check.sh#run_card_boundary`, `KICK-dKeptSession-13`'s boundary
  verb (its S6), after `run_context_boundary` and before `KICK-dKeptSession-10`'s
  `run_mail_interrupts`; `<key>` is the crossing's target, read off the `boundary —` line as
  `skills/session-kickoff/manifest-check.sh#render_pointers` reads it. It runs
  `run_driver_bounded "$CARD_CLAIMS_BOUND" <out> /dev/null --mail notice <slug> --item <key>`
  (`skills/session-kickoff/manifest-check.sh#run_driver_bounded`), as
  `skills/session-kickoff/manifest-check.sh#render_mail_line` runs its read, and prints `notice —
  <the verb's first line>`, CRs stripped, cut to 160 bytes, nothing for an `off` line, or `notice —
  skipped: <why>` for an unresolved driver, a fired bound or a non-zero exit. It returns 0 when the
  line ends ` · fetched`, else 1, and the branch passes `--local` to `run_mail_interrupts` on 0
  alone, so the notice and unit 10's read share one fetch (§8 F4); after an `off` line or a skip,
  unit 10's read fetches as it says. The section's `mail —` line, which `write_card_pointers` and the
  `stored` publish render through `--mail read --open --ids` (unit 5 S13), keeps its own reads: the
  clause's one fetch is the notice's. The `--card --boundary` usage comment at the script's head
  gains "the notice as a `notice —` line, as mailbox.notice says". The lines reach the session as
  unit 13 S7 returns the verb's others, at the next Bash or PowerShell call after the detached verb
  finishes. Observed by AC1, AC3 and AC6.
- **S5** — The tool-call hook, `tools/unattended/mail-notice.js`, a `PostToolUse` hook on every tool
  (§8 F1), and its fragment `tools/unattended/mail-notice.fragment.json`, both first written by the
  hook kind's factory, `python tools/playbook/core.py new hook mail-notice --kit unattended --event
  PostToolUse` (`tools/loop/factories.py#write_hook`), whose matcher defaults to `*`; the kit's
  `include = "**"` files row already ships both. Per call it reads the payload's `session_id`, the
  repository and its per-worktree git dir through `resolveRepo`
  (`tools/unattended/run-lease.js#resolveRepo`), the build through `resolveLease(root,
  readMemoryRoot(root), sessionId)` (`tools/unattended/run-lease.js#resolveLease`), the first lease
  where two match, and S3's stamp, with one `statSync` and `readSidecarLines`
  (`tools/unattended/run-lease.js#readSidecarLines`). It acts only when the stamp's
  first line reads `"notice": "every-tool-call"`. Then, where the stamp holds a row, it prints
  `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "mail — <n> unread for
  <slug> · <ids> · local copy <age>s old"}}`. It calls no `readPolicy`, spawns no `git` and makes no
  network call; a subagent's call (`agent_id` set), a session bound to no build, no stamp, any other
  value and any throw exit 0 in silence. `tools/settings-merge.py --fragment` over its fragment
  wires it into `.claude/settings.json`, never a hand edit. The wiring adds the codebase map's
  `harness-hooks` key `PostToolUse tools/unattended/mail-notice.js`, so `tools/loop/loop.toml`
  gains its `[[hook]]` row, `key = "PostToolUse {prefix}/unattended/mail-notice.js"` with the five build steps the kit's other hooks
  claim, which `tools/loop/stage_coverage.py` joins both ways, and the `harness-hooks` claim of
  `memory/map/features/unattended.md` gains the key. Observed by AC4, AC5 and AC10.
- **S6** — The detached fetch. Under `every-tool-call`, when the stamp is older than its own
  `fetch-seconds`, the hook creates `<stamp>.fetching` with the exclusive flag and, only when it
  created it, spawns the stamp's `bash` with `<this hook's directory>/unattended.sh --mail notice
  <slug>` as `tools/hooks/scratch-guard.js#checkItemBoundary` spawns its verb, detached, streams
  ignored, an `error` listener and `unref()`, so the call never waits. The verb
  clears the marker when it ends, and a marker older than twice `fetch-seconds` is overwritten.
  Observed by AC4.
- **S7** — The live ring's payload (I25): a ring carries exactly `<mail ref> <message id>` and never a
  fact, and its receiver's one act is the notice fetch. `--mail notice <slug> --ring <ref> <id>` is
  that receiver's entry. It refuses `mail — not read · --ring takes a mail ref and a twelve-hex-digit
  id`, exit 2 before any read, for a ref outside I16's grammar, `refs/gov/mail/<build>/<tag>/<segment>`
  as `tools/unattended/unattended.sh#derive_mail_ref` writes it, the build the sender's (unit 5 §8 F1)
  by `check_slug_shape`, the tag one lower-case letter, the segment `[A-Za-z0-9_-]` bytes and `%HH`
  (`tools/unattended/unattended.sh#derive_ref_segment`), or an id not matching `^[0-9a-f]{12}$`,
  then runs S1. A ring
  that never arrives costs the latency until the next boundary or detached fetch, since S1 and S6 read
  the mailbox, never the ring. The sender's side and the `deps.messaging` read are
  `KICK-dKeptSession-6`'s. Observed by AC7.
- **S8** — `mailbox.notice` (`every-tool-call`, `every-item`, `off`; default `every-item`) and
  `mailbox.fetch-seconds` (seconds, at least 10; default 60), both rows landed in
  `tools/policy/catalogue.toml`, owner dKeptSession. `--mail notice` is their one reader, through two
  new arms of `read_lease_policy` (`tools/unattended/unattended.sh#read_lease_policy`), the driver's
  one shell reader of policy keys, to which `KICK-dKeptSession-24` S1 adds `flow.wait-ceiling`: each a
  literal `policy.py get` line, the closed set or the lease bounds' number check, and the catalogue
  default under the reader's one NOTE where no policy kit resolves, both keys joining its NOTE's,
  refusal's and signature's key lists. The notice calls it with stdout to `/dev/null` and reads
  `LP_VALUE`, as its callers do; where it returns 1, a refused `get` or a value outside the set, the
  notice takes that key's catalogue default and prints one `unattended: NOTE -` line naming the key
  and `LP_VALUE`. The boundary verb and the hook read neither key. Both rows gain `summary` and
  `usage`; `python tools/policy/policy.py lists --write` drains them from
  `tools/policy/unsummarised-keys.txt`, `policy.py mirror --write` re-renders `.governance/policy.json`,
  whose `catalogue_blob` the edit moves, and `python tools/playbook/render_playbook.py --reference`
  re-renders `help/reference/policy.md`. Every preset of `tools/policy/presets.toml` keeps both
  defaults. Observed by AC6 and AC9.
- **S9** — The texts this unit makes false, each rewritten. The `--mail` entry of
  `tools/unattended/VERBS.template.md`, its verb count gaining `notice`, gains `--mail notice`,
  `--local`, `--ring`, the stamp and the hook; `memory/guides/UNATTENDED-VERBS.md`, the kit's
  placeholder-free `rendered` row, is its byte-equal copy, copied whole. `help/loop.md`, under
  "Where a build is, and what runs next", gains one bullet beside unit 10's: the `notice —` line,
  the hook's line, the three values of `mailbox.notice` and `mailbox.fetch-seconds`, with
  `<!-- usage: hook:mail-notice <fp8> -->`, `<!-- usage: policy:mailbox.notice <fp8> -->` and
  `<!-- usage: policy:mailbox.fetch-seconds <fp8> -->` (`tools/govkit/docs_leg.py`). Its `--mail`
  paragraph gains `--local` and a pointer to that bullet, its `verb:unattended.sh:--mail` anchor
  re-stamped, as the usage rows add `--local` and `--ring` to the flags it hashes
  (`tools/govkit/docs_leg.py#read_verb_usage`); each `<fp8>` is what `docs_leg.py --fingerprints`
  prints at build time. The two `policy:` rows leave `memory/project/docs-undocumented.txt` by hand,
  as an anchored member still listed is the leg's `DRAINED` finding. `help/orientation-card.md`'s
  "When the section is rewritten" gains one sentence beside unit 10's: a crossing then prints the
  unread mail as a `notice —` line, as `mailbox.notice` says. `tools/unattended/README.md`'s sidecar
  section reads five kinds, the fifth `mail-notice.<slug>.log`, rewritten whole by `--mail notice`
  and read by the hook. `run-lease.js`'s header names `mail-notice.js` among its requirers and
  `deriveSidecarPath`'s comment its `mail-notice` kind; the `check-unattended.sh` comment "The two
  hooks, `stop-guard.js` and `stall-recorder.js`," names `mail-notice.js` as a third. Observed by AC8.

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
- No change to the pointers section's `mail —` reads, unit 5's, which keep their own fetch.
- No kit version: the lander mints it (`tools/push-main.sh@3a5bf825e879:27`).

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
- `procmon-hook.js` is the hot-path precedent: it finds its stamp from the `.git` pointer files,
  never spawning git, and gates its work on one `statSync` of the stamp's mtime
  (`tools/process-monitor/procmon-hook.js#checkThrottled`).
- The JS policy reader spawns: `readPolicy` runs `git rev-parse`, `git cat-file` and the policy shim's
  `landed` on every call (`tools/policy/policy-mirror.js#readPolicy`). Five reads of `mailbox.notice`
  on this node took 269 ms each (PINNED, 2026-11-21), under the default value too.
- The kits' `additionalContext` writers are scratch-guard's `SubagentStart` arm
  (`tools/hooks/scratch-guard.js#main`) and its `PreToolUse` arm for Bash and PowerShell calls,
  `KICK-dKeptSession-13` S7's, returning the boundary verb's lines and starting that verb as a
  detached child (`tools/hooks/scratch-guard.js#checkItemBoundary`).
- The hook kind's factory writes `<name>.js` and `<name>.fragment.json` beside the kit's descriptor
  and adds a `[[files]]` row only where no `include` matches (`tools/loop/factories.py#write_hook`).
- At a crossing the section's `mail —` line reads the mailbox with a fetch in `write_card_pointers`,
  and again in each try of the `stored` publish
  (`skills/session-kickoff/manifest-check.sh#write_build_card`).

### The boundary, in order

1. The boundary verb answers a crossing, writes the section and runs `run_context_boundary` (unit 13 S6).
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

Live with `RUN_CLAIMS`. The hook is wired by its fragment through `settings-merge.py`, and an
adopter's `govkit update` wires it as it wires every fragment an install lands. Under the default
`every-item` the hook reads one stamp per call and leaves, and under every value it stays silent until
a first notice writes the stamp.

### The refusal ceiling

`tools/unattended/unattended.sh` stands at its harness-arms ceiling, 347 of 347 (PINNED,
`check-arms.py --report` at `b2303b53`, `REFUSAL_CEILINGS` in `.memory-tree.conf`). This unit adds
no `fail`, `exit 1` or `status=1` site: the dispatch refuses through `_rl_rc=2`, each new function
returns its code, and `read_mailbox`'s `status=$_st` restore is untouched, so the ceiling holds.
The new shell adds no site of the classes `tools/gate-lint/sh_hygiene.py` counts in the shrink-only
`memory/project/spawn-idiom-sites.txt`: `printf -v`, `$(<file)` and parameter expansion stand for
`$(printf …)`, `$(cat …)` and `$(basename …)`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `--mail notice`, its usage row and the `read` row's `--local`,
  the arm's flags and refusals, `read_mailbox`'s `local` mode, `print_mailbox`'s mode,
  `write_mail_notice`, `print_mail_notice`, two `read_lease_policy` arms
- `tools/unattended/mail-notice.js`, `tools/unattended/mail-notice.fragment.json`: the hook over the
  factory's file, and its fragment, the factory's
- `.claude/settings.json`: the `PostToolUse` group, by `settings-merge.py --fragment` (S5)
- `tools/loop/loop.toml`: the `[[hook]]` row; `memory/map/features/unattended.md`: the claim (S5)
- `memory/map/generated/`: `symbols.json` and the inventory files, re-rendered by `python
  tools/codebase-map/gen_map.py --write`, never hand-edited
- `skills/session-kickoff/manifest-check.sh`: `run_mail_notice`, its call, the usage comment
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: the `mail-notice-boundary` plant in `PLANTS`
- `skills/session-kickoff/manifest-check.test.sh`: `FLOOR_ASSERTIONS`, 441 at `b2303b53` (DERIVED:
  its last assignment) and 442 after unit 10, raised by one with a `+1: RAISED by
  KICK-dKeptSession-21` line, the card-store loop's one ok row for the plant
- `tools/unattended/unattended.test.sh`: the arms of §7 in region eight, after the mailbox blocks;
  `FLOOR_ASSERTIONS`, 4100, and `FLOOR_SHARD_8`, 1317, at `b2303b53` (DERIVED: their last
  assignments), each raised over its value at build time by the counted assertions, with its line
- `tools/run-gates/selftest-budgets.txt`: `manifest-check self-test` re-priced by the plant's direct
  reading, as unit 5 priced its three; `unattended driver selftest shard 8/8` raised by 1.5 times the
  block's direct reading
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: the entry and its copy
- `tools/policy/catalogue.toml`: the two mailbox rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`, `help/reference/policy.md`: by
  `lists --write`, `mirror --write` and `render_playbook.py --reference`
- `help/loop.md`, `help/orientation-card.md`, `memory/project/docs-undocumented.txt`: S9
- `tools/unattended/README.md`, `tools/unattended/run-lease.js`, `tools/unattended/check-unattended.sh`:
  the sidecar section and the three comments of S9

The texts that stay: the comment above `run_card_boundary` already names `mailbox.notice`;
`resolve_sidecar_dir`'s comment names its readers by example, and the stamp's writer calls it; the
card page's `mail —` bullet and the guard paragraphs of `help/loop.md` and `tools/loop/README.md`
describe reads whose argv is unchanged; the kit README already says `govkit update` wires every
fragment; `.governance/install.json` moves at the landing merge, never in a pass.

### Alternatives rejected

- **The hook running `--mail read` per call.** A driver process per tool call, where the stamp costs
  one file read; and the driver's fetch would put the network back on the call path.
- **A JS parser of the mail refs in the hook.** A second reader of unit 5's record beside
  `read_mailbox`.
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
- user docs — `memory/guides/UNATTENDED-VERBS.md`, `help/loop.md`, `help/orientation-card.md`,
  `help/reference/policy.md` and `tools/unattended/README.md`.

## 6. Acceptance criteria

- **AC1** — When clone A posts a `question` to `build:<slug>`, with the `--default` that
  `KICK-dKeptSession-24` S2 requires, and clone B, at its next item boundary,
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
  `--card --boundary` across a crossing, one message to `build:tFix` set on the bare remote by the
  fixture's `write_card_mail`, the output holds `notice — mail — 1 unread` before unit 10's
  `interrupt — mailbox` line and the stub engine's log records `--mail-interrupts --local`; with
  `mailbox.notice` planted `off` by `set_card_policy`, since the stub policy kit answers only planted
  keys, it holds no `notice —` line and the log records `--mail-interrupts` with no `--local`; with
  no crossing it holds no `notice —` line.
  Red when: a crossing shows no notice, `off` silences the disposal, or unit 10's read fetches after
  a fetched notice.
- **AC4** — When `mailbox.notice = "every-tool-call"` and `mailbox.fetch-seconds = 10` land on the
  origin and are fetched on B, as `write_lease_policy` lands a file, one `--mail notice <slug>` on B
  writes the stamp, A posts, and B's hook is fed one `PostToolUse` payload for B's session every two
  seconds through `node mail-notice.js` in the unattended kit, a
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
- **AC6** — When the policy reads of `mailbox.notice` and `mailbox.fetch-seconds` are refused, staged
  as DPR1 AC17 stages a refusal, an unparsable first policy revision after a fresh
  `write_lease_fixture`, `--mail notice <slug>` prints the notice as `every-item` and one
  `unattended: NOTE -` line per key, naming it, and the stamp's first line reads
  `"notice": "every-item"`, so the hook fed a payload prints nothing.
  Red when: a refused read changes the behaviour from the default.
- **AC7** — When `--mail notice <slug> --ring <ref> <id>` runs with a ref outside
  `refs/gov/mail/<build>/<tag>/<segment>` or an id of eleven hex digits, it exits 2 and fetches
  nothing; with a valid pair it prints S1's line. With `deps.messaging = "live-and-mailbox"` and no
  ring ever delivered, AC1's boundary still shows the message.
  Red when: a ring carries a fact the receiver acts on, or a lost ring loses the message.
- **AC8** — When `grep -n -- '--mail notice\|--local\|--ring\|mail-notice'` runs over
  `tools/unattended/VERBS.template.md`, `grep -n 'notice —' help/loop.md help/orientation-card.md`
  and `grep -n 'mail-notice' tools/unattended/README.md`, each is found; `cmp` of the template and
  `memory/guides/UNATTENDED-VERBS.md` is silent; `grep -c 'mailbox.notice\|mailbox.fetch-seconds'
  memory/project/docs-undocumented.txt` prints 0; and `python tools/govkit/docs_leg.py
  --fingerprints` prints `hook:mail-notice`, `policy:mailbox.notice`, `policy:mailbox.fetch-seconds`
  and `verb:unattended.sh:--mail`, each with `help/loop.md` and the fingerprint its anchor there carries.
  Red when: the notice is undocumented, the hook or a key is anchored nowhere, or the `--mail` anchor
  keeps the fingerprint from before `--mail notice`.
- **AC9** — When `python tools/policy/policy.py get mailbox.notice` and `get mailbox.fetch-seconds`
  run in a repository whose policy file sets neither, they print `every-item` and `60`, and after
  `policy.py lists --write` `tools/policy/unsummarised-keys.txt` names neither key, and the
  `catalogue_blob` of `.governance/policy.json` is the blob `git rev-parse` names for the committed
  `tools/policy/catalogue.toml`.
  Red when: either row is still unsummarised, or the mirror pins the catalogue before the edit.
- **AC10** — When `grep -c 'mail-notice.js' .claude/settings.json`, `grep -c 'PostToolUse
  {prefix}/unattended/mail-notice.js' tools/loop/loop.toml` and `grep -c 'PostToolUse
  tools/unattended/mail-notice.js' memory/map/features/unattended.md` run, each prints 1, and the
  settings file's diff against the base is the one group `settings-merge.py --fragment` writes.
  Red when: the hook is wired by hand off its fragment, or its key has no stage or dossier claim.

## 7. Gates

`unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `routed-commits selftest` · `policy check` · `help reference pages` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `docs` · `loop stage coverage` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC4 AC5 AC6 AC7 · the notice arms in region eight over two clones and one bare origin, as unit 5's mailbox block stands its up, AC1 staged by a scratch copy that skips the fetch and AC4 by a stubbed spawn · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the arms' count, counted off the diff
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 · the `mail-notice-boundary` plant, red with the notice step left out of the boundary verb · `FLOOR_ASSERTIONS` rises by one, the plant's ok row

## 8. Open questions

- **FACT-QUESTION · F1 — Which hook event's output reaches the model at a tool call?** Probe: the
  installed CLI's bundled source, read with `grep -a -o '.\{0,160\}hook_additional_context.\{0,160\}'
  <CLI binary>`. Observation, 2026-10-26, on Claude Code 2.1.308: the output schema admits
  `additionalContext` under both `PreToolUse` and `PostToolUse`, and the CLI builds a
  `hook_additional_context` attachment message with `hookEvent:"PostToolUse"` from a `PostToolUse`
  hook's `additionalContext`, the message type the model reads. Re-probed 2026-11-21 on 2.1.319: 42
  lines (PINNED) name the attachment type, their builders naming `PostToolUse` five times and
  `PreToolUse` once, the channel `KICK-dKeptSession-13` S7 uses for shell calls. Liveness: the grep would return no
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
  "the notice runs one fetch of the mail refs"; the section's `mail —` reads are unit 5's and stay
  (S4). widens: none · relaxes: none
- **F5 — How does the hook learn `mailbox.notice` and `mailbox.fetch-seconds` without the git spawns
  `readPolicy` makes?** Options: (a) `readPolicy` per call, through `policy-mirror.js`, which spawns
  git and the policy shim on every call under every value, the default included, against AC5; (b)
  `--mail notice`, the one reader of both keys, writes them as S3's stamp's first line, and the hook
  reads them with the stamp's read, a changed value reaching it at the next notice; (c)
  `KICK-dKeptSession-44` S18's second sidecar, written by the boundary verb, a second writer spelling
  the root `resolve_sidecar_dir` keeps to one line, and two reads per call. RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; veto 1
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
- rev-5 · 2026-11-21 · S8 · S9 · §4 · AC1 · AC3 · AC4 · AC6 · AC8 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: `get` reads the landed revision, so AC4
  lands its values on the origin and AC6 stages its refusal as DPR1 AC17 does; the card-store
  fixture's stub policy refuses an unplanted key, so AC3 plants `off` by `set_card_policy`; S8 states
  the notice's own default and NOTE on the reader's return 1; AC1's question carries unit 24's
  `--default`; the docs leg needs the new hook anchored and the `--mail` anchor re-stamped (S9, AC8);
  `symbols.json` and the suites' floors joined Files touched and §7.
- rev-6 · 2026-11-23 · S1 to S9 · §3 · §4 · §5 · AC3 · AC8 · AC9 · AC10 · §7 · §8 F4 · §10 ·
  re-grounded at `b2303b53` under `2026-11-22-prompt-KICK-dKeptSession-21-reground-brief`, units 39,
  51, 27, 24, 10 and 25 read as landed: the notice sits in `run_card_boundary`'s crossing branch,
  its one fetch the notice's alone; the hook's stamp read, spawn, wiring and inventory claims
  (AC10); the texts made false joined S9; the ceiling, idiom ledger, floors and budget rows stated.

## 10. Reuse audit

The seams extended are `read_mailbox`'s bounded fetch (unit 5's, made through
`tools/unattended/unattended.sh#observe_remote`, as `tools/unattended/unattended.sh#read_claims`
makes its own), gaining a `local` mode; the driver's one shell policy reader,
`tools/unattended/unattended.sh#read_lease_policy`; the hot-path stamp throttle of
`tools/process-monitor/procmon-hook.js#checkThrottled`; `run-lease.js`' git-free `resolveRepo`,
`resolveLease` and `deriveSidecarPath` (`tools/unattended/run-lease.js#deriveSidecarPath`); the
kickoff engine's bounded driver call, `skills/session-kickoff/manifest-check.sh#run_driver_bounded`;
and the hook kind's factory, `tools/loop/factories.py#write_hook`. The sidecar path, its reader
`tools/unattended/run-lease.js#readSidecarLines` and the session-to-build binding are reused, not
copied. The detached spawn is no longer new: `grep -rn 'detached' tools --include=*.js` at `b2303b53`
finds `tools/hooks/scratch-guard.js#checkItemBoundary`'s, whose spawn options S6 takes; the hooks
kit and the unattended kit ship apart and share no JavaScript module, so the five-line idiom is
spelled in each, the three-line idiom being no kind with a factory. `python tools/codebase-map/reuse_lookup.py "show unread message
ids at every tool call from a local copy"` and `"spawn a detached child from a hook without
waiting"`, re-run at `b2303b53`, ranked names by stem (`ids`, `derive_tool_root`,
`check_child_forwarding`), none a notice or a spawn. Scout B's disagreement 7,
that a `PreToolUse` hook's `additionalContext` was unprobed, is §8 F1, re-probed; its suggested
common-dir stamp is refined by §8 F2.

Recall terms used: mailbox.notice every-tool-call fetch-seconds hook additionalContext local copy detached fetch stamp unread ids read_lease_policy run_driver_bounded detached spawn harness-hooks readSidecarLines
