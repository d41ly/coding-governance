# KICK-dKeptSession-24 — a mail deadline judged by the observer clock: `flow.wait-ceiling` declared on each message, the asker's default past it

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 19 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0162@6ce67958 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

Every mail message carries the deadline its asker declared, `flow.wait-ceiling` in hours, and a
default answer; a node judges that deadline by the time it first saw the message on its own clock,
the declared clock dPlacedRequest's leases use, never by its clock minus the sender's stamp. Past the
deadline the message reads `expired`, the asker's default answers it, and the recipient build's
transitions go on (P39, the whole-design audit's A2-F6). Without this, a question nobody answers
blocks the recipient for ever, and a reader whose clock runs a day ahead expires every message a day
early (gap-conc-14's class, `tools/unattended/unattended.sh:2180`).

## 2. Scope (IN)

- **S1** — The declared deadline. `unattended.sh --mail post` (I19, `KICK-dKeptSession-5`) writes the
  I17 field `deadline` as the integer hours `flow.wait-ceiling` reads at the post, through I8's shell
  form `python <prefix>/policy/policy.py get flow.wait-ceiling`; a refusal of that read writes the
  catalogue default `72` (TOOL-dDeclaredLoop-33 S5) and prints one NOTE naming the key. Every message
  carries one, whatever its kind (§8 F2). Observed by AC1 and AC5.
- **S2** — The declared default. `--mail post` takes `--default <text>` into the I17 field `default`.
  A `question` or a `confirm-request` posted without `--default` is refused with exit 2 naming the
  flag, before any commit is built; every other kind writes `default: ack`. The text passes the same
  body check I17's builder applies (4096 bytes, no control byte but tab and newline). Observed by AC1.
- **S3** — The judgment, `check_mail_deadline <ref> <commit> <hours>` (I23), in
  `tools/unattended/unattended.sh`: it calls TOOL-dPlacedRequest-17 S4's
  `check_deadline_passed <ref> <commit> <hours × 3600>` with the message's remote mail ref and its own
  commit, and returns that call's code: 0 passed, 1 not yet, 2 not sighted. An `<hours>` that is not a
  non-negative integer returns 2. Observed by AC2, AC3 and AC4.
- **S4** — The sightings, consumed. `KICK-dKeptSession-5`'s `read_mailbox` runs TOOL-dPlacedRequest-13
  S4's `add_feed_sightings refs/gov/remote/mail/` after its fetch (unit 5 S6), and its writer builds
  every message commit by `build_gov_commit` under the fixed `gov-claim` identity (unit 5 S2), which
  the sightings walk requires (scout B's disagreement 5); so every fetched message has a first
  sighting in `gov-feed.log` before a row is judged. This unit adds no call, and AC6 observes the pair
  its clock rests on. Observed by AC6.
- **S5** — The `expired` state. In `read_mailbox`'s rows, a message whose state would be `open` and
  whose `check_mail_deadline` returns 0 reads `expired`; a return of 1 or 2 keeps it `open`, so an
  unsighted message never expires (§8 F4). The row gains the columns `deadline` and `default`, after
  the columns `KICK-dKeptSession-27` appends, so `--mail read` prints an `expired` row beside the
  asker's declared answer. The transition guard of
  `KICK-dKeptSession-5` refuses on `open` rows only, so an expired message lets the recipient's
  transitions go on. Observed by AC2, AC3 and AC4.
- **S6** — The verbs guide: the `--mail` section unit 5 adds to `tools/unattended/VERBS.template.md`
  (rendered to `memory/guides/UNATTENDED-VERBS.md`) states `--default`, the `deadline` field, the
  observer rule and the `expired` state. Observed by AC7.

## 3. Non-goals (OUT)

- No mailbox, record, kind list or transition guard: `KICK-dKeptSession-5`'s. This unit fills two of
  I17's fields and adds one state to I20's rows.
- No observer clock of its own: `read_first_seen` and `check_deadline_passed` are TOOL-dPlacedRequest-17's,
  and the feed and its sightings walk are TOOL-dPlacedRequest-13's. This unit calls them.
- No answering: who answers a `question`, the `mailbox.answer` item and the lease renewal while a
  build waits are `KICK-dKeptSession-25`'s.
- No written answer on expiry. The default is derived from the message, never posted (§8 F5).
- No clock offset correction: v2:1160's second rule is dWellOiledMachine's supervisor's.
- No `flow.wait-ceiling` row or reader: dGroundRules-1 S3 writes the catalogue row, owner dDeclaredLoop,
  and dGroundRules-2 S6 the reader.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its rows and states, the `--mail post` writer and I17's `deadline` and `default` fields; without them there is no message to judge
- **hands-off** `KICK-dKeptSession-25` — `check_mail_deadline` and the `expired` state, through which an unattended build's question is answered by the asker's default
- **consumes-from** external — TOOL-dPlacedRequest-17's `check_deadline_passed` and `read_first_seen`, TOOL-dPlacedRequest-13's `add_feed_sightings` and `gov-feed.log`, TOOL-dPlacedRequest-11's `build_gov_commit`, and the `flow.wait-ceiling` row and reader of dGroundRules

## 4. Design

### Evidence

- Today's only age in the coordination code is the reader's clock minus the holder's stamp:
  `a = age[1] - age[$11 + 1]` in `read_claims`' age pass (`tools/unattended/unattended.sh:2180`),
  which TOOL-dPlacedRequest-17 S3 moves onto the first sighting. No mail code exists:
  `grep -rn mailbox tools` finds nothing at base.
- The feed keys a sighting by (`ref`, `blob`, `commit`) and stamps `seen-utc` on this node's clock
  (TOOL-dPlacedRequest-13 S1); a write this node makes is sighted at its own write (S3), and a
  fetched one by the walk (S4), which stops at the first commit not authored `gov-claim`.
- The deadline gov's own waits declare is `flow.wait-ceiling`, 72 hours, v2:1263; strict sets 168
  (v2:1582). A wait declares `deadline` and `on-deadline` (TOOL-dDeclaredLoop-33 S5).

### The rule

```
deadline(message) = the asker's flow.wait-ceiling, in hours, written at the post
age(message)      = now(this node) - seen-utc(this node's first sighting of the message commit)
expired           = state would be open  and  age > deadline × 3600
```

The asker's node sights its own question at the write and the recipient's node at its first fetch,
so each side judges the same declared deadline on its own clock, and a constant skew cancels on each.
A message no answer and no acknowledgement disposes stays `open` until then and reads `expired`
after; an answered or acknowledged one keeps the state unit 5's reader gives it.

### The post's two fields

```
deadline: 72
default: no
```

`deadline` is the integer the policy read returned; `default` is `--default`'s text, or `ack` for a
kind that only needs acknowledging (`changed`, `landed`, `overlap`, `takeover`, `intake`, `withdrawn`,
`superseded`, `answer`, `ack`, `confirmed`). The two kinds that ask for content, `question` and
`confirm-request`, must declare theirs.

### The read

1. `read_mailbox`'s bounded fetch, then unit 5's `add_feed_sightings refs/gov/remote/mail/`.
2. Its parse yields each message's `ref`, `commit`, `state` and `first-seen`, as unit 5 S6 defines them.
3. For each `open` row, `check_mail_deadline <remote ref> <commit> <deadline>`; rc 0 sets `expired`.
   The rows are judged in one feed read: `check_deadline_passed` is called per row, and each call is
   one `awk` over the feed, so the cost is linear in open messages, which the guard keeps few.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_mail_deadline` | shell function | `check`, OK |
| `--default` | flag of `--mail post` | none |
| `expired` | a state of I20's rows | none |

### Migration

None. No message exists before unit 5 lands, and unit 5 lands before this unit (order 16 before 19).

### Rollout

Behind `RUN_CLAIMS`, as every mail write and read is (I16). A build with no open message sees no
change.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `check_mail_deadline`, the post's two fields, the `expired`
  state and its two columns, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: the `--mail` section's flag, field and state
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **The deadline as the tag `policy.flow.wait-ceiling`, resolved by each reader.** Two nodes with two
  values would judge one message two ways (§8 F1).
- **The sender's commit time as the clock.** It is the holder's stamp, the clause's red case.
- **An `answer` message posted at expiry.** A second record of what the deadline already derives,
  written once per reading node (§8 F5).

## 5. Production-readiness checklist

- security — `--default` text passes I17's body check before any commit; no new outbound call.
- perf / scale — one feed `awk` per open message per read; the sightings walk is the feed's own.
- error / empty / loading states — an unsighted message reads `open`, never `expired`; a policy read
  refused writes 72 with a NOTE; a malformed `deadline` judges rc 2 and stays `open`.
- observability — `--mail read` prints each expired row's state and its `default` column.
- risks — a feed deleted and rebuilt restamps every sighting, which delays expiry by up to one
  deadline and never advances it.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`; no `help/` page covers the unattended kit.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --mail post` posts a `question` with
  `--default no` in a fixture whose policy file plants `flow.wait-ceiling = 30`, the new mail commit's
  message carries `deadline: 30` and `default: no`; the same post without `--default` exits 2 naming
  `--default` and builds no commit; a `landed` post carries `default: ack`.
  Red when: a message is written with no deadline, or a question with no declared default.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, a fleet tag and
  `CLAUDE_CODE_SESSION_ID` set.
- **AC2** — When a question addressed to `build:<slug>` with `deadline: 30` has its feed line planted
  with `seen-utc` 31 hours ago, `--mail read <slug>` prints its row with the state `expired` and the
  `default` column `no`, and
  `python loop_transition.py record` for that build is not refused by the mail guard; with the line
  planted one hour ago it prints `open`, and the record is refused naming the message id. This is the
  clause's planted question nobody answers.
  Red when: an unanswered question blocks the transition past its deadline.
- **AC3** — When the question's commit carries a committer date 25 hours before now, as a holder a
  day behind the reader stamps it, its `deadline` is 24 and this node's feed sights it 60 seconds ago,
  `--mail read` prints it `open`; a scratch copy of the driver whose `check_mail_deadline` ages
  `now - %ct` prints it `expired`. This is the clause's reader whose clock runs a day ahead.
  Red when: the sender's stamp decides the deadline.
- **AC4** — When `check_mail_deadline <ref> <sha> 1` runs in a shell that has sourced
  `tools/unattended/unattended.sh`, over a commit sighted 7200 seconds ago it returns 0, over one sighted 60 seconds ago 1,
  over an unsighted sha 2, and over `<hours>` planted `x` 2; the unsighted message's row reads `open`.
  Red when: an unsighted or malformed deadline reads `expired`.
- **AC5** — When the policy read of `flow.wait-ceiling` is refused, `--mail post` writes
  `deadline: 72` and prints one NOTE naming `flow.wait-ceiling`.
  Red when: a refused read writes no deadline or a value other than the catalogue default.
- **AC6** — When clone A posts a message and clone B runs `--mail read <slug>`, B's `gov-feed.log`
  holds a line for A's mail ref and commit, and `git log -1 --format=%an <commit>` prints `gov-claim`.
  Red when: the read path sights nothing, so every fetched message stays `open` for ever.
- **AC7** — When `grep -n -- '--default\|deadline\|expired\|first saw'` runs over
  `tools/unattended/VERBS.template.md`, each is found in its `--mail` section.
  Red when: the guide states no deadline rule.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the deadline arms over planted feed lines and mail commits, staged by a scratch copy whose judgment reads the commit's own date · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

## 8. Open questions

- **F1 — What does a message's `deadline` hold: the asker's hours, or the key each reader resolves?**
  Options: (a) the integer hours `flow.wait-ceiling` read at the post, so every reader judges the one
  deadline the asker declared; (b) the tag `policy.flow.wait-ceiling`, TOOL-dDeclaredLoop-33 S5's
  grammar for a row, resolved by each reader, so two nodes with two values judge one message two
  ways. The clause says the message declares the deadline, and P40 forbids two nodes deciding one
  verdict differently. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Which messages carry a deadline?** Options: (a) every message, since cl-dClosedLoop-0143 refuses
  a transition while any message addressed to the build is neither answered nor acknowledged until
  `flow.wait-ceiling` passes; (b) only `question` and `confirm-request`, which leaves a `changed` nobody
  acknowledges blocking for ever. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, cl-dClosedLoop-0143.
  widens: none · relaxes: none
- **F3 — What does a `question` posted with no declared default do?** Options: (a) refused at the
  post, exit 2; (b) written with `default: none`, so it expires into an answer nobody chose. The
  clause names "the asker's declared default". RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  the clause's text. widens: none · relaxes: none
- **F4 — What does a reader do with a message its feed has not sighted?** Options: (a) `open`, never
  `expired`, the rule TOOL-dPlacedRequest-17 §8 F3 settled for leases; (b) sighted now, which restarts
  the clock whenever a feed line is lost. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F5 — Is the default answer written when the deadline passes?** Options: (a) derived, read as
  `expired` with its `default`; (b) an `answer` message posted by the first reader past the deadline,
  a second record of a derived fact that each reading node would post. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the charter's `[derive]` rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 24, scout B row 7 and its disagreement
  5, Shared interfaces I17, I20 and I23, v2:1263, v2:1582 and TOOL-dPlacedRequest-17 S1, S4.

## 10. Reuse audit

The seam extended is TOOL-dPlacedRequest-17 S4's `check_deadline_passed <ref> <sha> <seconds>`, the one
judgment of a deadline by first sighting, which this unit calls with a mail ref, a message commit and
the declared hours; its first sighting is S1's `read_first_seen` over TOOL-dPlacedRequest-13's feed,
and the walk that sights a fetched commit is that unit's S4. None of them exists at base: every one is
a parent's spec section, and `tools/lib/gov-feed.sh` is absent. Today's code is the holder-stamp age at
`tools/unattended/unattended.sh:2180`, verified at this writing, and the parent's S3 moves it. `python
tools/codebase-map/reuse_lookup.py "a deadline judged by the time this node first saw a record"`
ranked `records`, `extract_records`, `read_records` and `render_record`, name stems only; no existing
function judges a deadline by sighting, so no code seam fits beyond the parent's. `python
tools/memory-recall/query.py "how does a mailbox message expire by the observer clock"` returned scout
B's row 7, scout A's row 7 of dPlacedRequest and TOOL-dPlacedRequest-20's edge to
`check_deadline_passed`; none disagrees with source, and scout B's note that gap-conc-14 cites a stale
range (`:2152-2185`, now `:2172-2186`) holds.

Recall terms used: mailbox question deadline flow.wait-ceiling observer clock first sighting check_deadline_passed expired default answer read_first_seen
