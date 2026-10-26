# KICK-dKeptSession-10 — the mailbox read at every item boundary: `mailbox.reads` arming the position engine's mail interrupt, with the `intake` kind

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 20 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0148@ab3d7b8c whole
**Carries:** node:policy-key.mailbox.reads

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

The build's mailbox is read at every item boundary, as `mailbox.reads` says, and each open message
addressed to the build is listed as the position engine's mail interrupt, so a message that arrives
mid-step, an amendment from another session or a parent's breaking change, waits one item rather than
one step (flow-roles FR-8, "Every item, plus an intake kind"). At base the engine is specced and
unbuilt, and its mail interrupt prints `unarmed` (TOOL-dDeclaredLoop-7 S4); this unit arms it at the
one item-boundary point `KICK-dKeptSession-13` provides, and carries the `intake` kind, the amendment
a session that does not hold the build's lease sends to the session that does.

## 2. Scope (IN)

- **S1** — The read point. Inside `KICK-dKeptSession-13`'s boundary verb, `manifest-check.sh --card
  --boundary --build <slug> --session <sid>` (its S6), once `derive_item_boundary` (I12) answers a
  crossing, one step runs `python <loop kit>/position.py <slug> --mail-interrupts`, the loop kit
  resolved as that verb resolves `position.py`, and prints the lines it returns after the verb's
  `boundary —` line. No crossing runs no read. Observed by AC2.
- **S2** — The interrupt, `read_mail_interrupts(repo, slug, local)` in `tools/loop/position.py`, behind
  the CLI flag `--mail-interrupts`: it runs `bash <kit>/unattended.sh --mail read <slug> --open`
  (`KICK-dKeptSession-5` S8, I19), the unattended kit located by
  `resolve_kit_dir("unattended", "unattended.sh", here)` and run as a subprocess, the sibling-kit
  pattern TOOL-dDeclaredLoop-12 S4 uses, never an import. Each row, the open messages
  `check_mail_addressed <to> build:<slug>` admits (`KICK-dKeptSession-28`), prints one line in
  TOOL-dDeclaredLoop-7's interrupt shape, `interrupt — mail · <id> <kind> from <from-build>`, ordered
  by `first-seen` then id. Only this flag reads the mailbox: `derive_position` and every other engine
  call print no mail line, so `derive_item_boundary`, which calls the engine, never reads it (§8 F2).
  A mail interrupt changes no answer; refusing a transition over an open message is unit 5's guard.
  Observed by AC1.
- **S3** — `mailbox.reads` (`every-item`, `transitions-only`, `every-item-amendments-at-transitions`;
  default `every-item`), read through I8's Python form, `resolve("mailbox.reads")`
  (TOOL-dGroundRules-2 S6); a refusal reads the catalogue default and prints one NOTE naming the key.
  `every-item` lists every kind. `transitions-only` runs no read and prints one line,
  `interrupt — mail · read at transitions (mailbox.reads: transitions-only)`.
  `every-item-amendments-at-transitions` lists every kind but `intake` and prints one line counting the
  held ones, `interrupt — mail · <n> intake held to the next transition (mailbox.reads:
  every-item-amendments-at-transitions)`. Observed by AC3, AC4 and AC6.
- **S4** — `--mail-interrupts --local` passes `--local` to the read, so it reads the node's cache
  without a fetch; `KICK-dKeptSession-21`'s notice sets it when it fetched at the same boundary.
  Observed by AC2.
- **S5** — The `intake` kind, a member of I18's closed list that unit 5 declares in
  `tools/loop/loop.toml`'s `[mail]` table: an amendment from a session that does not hold the build's
  lease, addressed to the build or one of its units. Its interrupt line ends ` · amendment`, so the
  session holding the build reads it as a request to amend and disposes it through unit 5's verbs.
  Observed by AC1 and AC4.
- **S6** — The unarmed case: with the unattended kit absent, or its read exiting non-zero, the flag
  prints `interrupt — mail · unarmed · <cause>` naming the kit, or the exit and its first stderr line,
  and exits 0. Observed by AC5.
- **S7** — The page `help/loop.md`, TOOL-dDeclaredLoop-1's, gains the mail interrupt, the three values
  of `mailbox.reads` and the `intake` kind. Observed by AC7.

## 3. Non-goals (OUT)

- No mailbox, reader, kind list or transition guard: `KICK-dKeptSession-5`'s. The read at a
  transition is that guard's, under every value of `mailbox.reads`.
- No item boundary and no boundary verb: `KICK-dKeptSession-13`'s; this unit adds one step inside it.
- No fetch of the mail refs of its own: the reader's fetch is unit 5's, and the notice's is
  `KICK-dKeptSession-21`'s.
- No dispatch of a message: `next` listing messages as next actions is dWellOiledMachine's, and the
  `question` answer is `KICK-dKeptSession-25`'s.
- No refusal of an `intake` posted by the lease holder: neither FR-8 nor the clause asks for one.
- No `project` or `node:` interrupt: unit 5's guard gates `build:` and `unit:` recipients only, and
  this read lists what that guard holds.
- No catalogue row: dGroundRules-1 S3 writes `mailbox.reads`'s row, owner dKeptSession.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary` and the `--card --boundary` verb, the one item-boundary point the read runs inside
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, read through `--mail read --open`, and the `intake` kind in I18's list
- **consumes-from** external — TOOL-dDeclaredLoop-7's `derive_interrupts` and interrupt shape, TOOL-dDeclaredLoop-12's `resolve_kit_dir` pattern, and TOOL-dGroundRules-2's `resolve`
- **hands-off** external — dDeclaredLoop's next pass amends TOOL-dDeclaredLoop-7 S4's text to name dKeptSession as the build arming the mailbox interrupt (§8 F3, an ask)
- **hands-off** `KICK-dKeptSession-44` — `read_mail_interrupts` and its `--local` step, the batch's S3, S16 and S19 (ids 6, 23, 33)

## 4. Design

### Evidence

- TOOL-dDeclaredLoop-7 S4 orders the interrupts: an owner decision, mailbox messages, invalidated
  witnesses, dependency gates; its line shape is `interrupt — <kind> · <subject>` (§4 Line output).
- FR-8 (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:232-235`)
  answered "Every item, plus an intake kind"; the settled text (:248-251) gives `intake` as an
  amendment from a session that does not hold the lease to the one that does.
- Every preset sets `mailbox.reads` to `every-item` (v2:1555); the catalogue default is the same
  (v2:1233).
- `KICK-dKeptSession-13` S6 makes `--card --boundary` the one item-boundary point and names
  `mailbox.reads` among the readers that run inside it; its S7 hook prints the verb's output to the
  session as `additionalContext`.
- A kit reaches a sibling kit by subprocess through `resolve_kit_dir`, never by import
  (TOOL-dDeclaredLoop-12 S4, TOOL-dGroundRules-1 §4 Evidence).

### The boundary step, in order

1. The boundary verb answers a crossing (unit 13's S1).
2. Unit 21's notice runs where `mailbox.notice` admits it, and reports whether it fetched.
3. This step runs `position.py <slug> --mail-interrupts`, with `--local` when the notice fetched.
4. The flag resolves `mailbox.reads`; `transitions-only` prints its one line and returns.
5. It runs `--mail read <slug> --open [--local]`, keeps the rows, sets `intake` aside under the third
   value, and prints one line per kept row and the held count.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_mail_interrupts` | Python function, `tools/loop/position.py` | `py.function`, verb-first |
| `--mail-interrupts` | CLI flag of `tools/loop/position.py` | none |
| `mail-open`, `mail-transitions-only`, `mail-amendments`, `mail-unarmed` | `--plant` cases of `position.py --fixture` | none |
| `mail-boundary` | plant of `skills/session-kickoff/card-store.fixture.sh` | none |

### Migration

None: no position is stored.

### Rollout

Live when the engine, the boundary verb and the mailbox are built; a build with no open mail prints
no line.

### Files touched (estimate)

- `tools/loop/position.py`: `read_mail_interrupts`, `--mail-interrupts`, four plants
- `skills/session-kickoff/manifest-check.sh`: the step inside `--card --boundary`
- `skills/session-kickoff/card-store.fixture.sh`: the `mail-boundary` plant
- `skills/session-kickoff/manifest-check.test.sh`: its arm
- `help/loop.md`: the mail interrupt section

### Alternatives rejected

- **A mail reader in the loop kit.** A second parser of I17's record; I20 is the one reader.
- **The mail read inside `derive_position`.** `derive_item_boundary` calls the engine, so the read
  would run before the crossing is known, at every `--status` and `--plan` as well.
- **An `awaiting` answer while a message is open.** It would stop the item the message may not
  concern; the transition guard is where an unanswered message holds the build.

## 5. Production-readiness checklist

- security — read-only: one subprocess of the unattended kit with fixed argv; no shell string.
- perf / scale — one `--mail read` per crossing, none without one and none under `transitions-only`;
  with the notice's fetch, the read is local.
- error / empty / loading states — a missing kit or a failed read prints `unarmed` with its cause and
  exits 0; an empty mailbox prints nothing.
- observability — each open message is one `interrupt —` line; a held `intake` is counted.
- risks — a slow remote slows a crossing by the reader's bound when no notice fetched first.
- testing — the plants of §6 and the arms of §7.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant mail-open` runs `--mail-interrupts` over a build
  holding one open `question` and one open `intake` addressed to `build:<slug>` and one `answered`
  message, it prints `interrupt — mail · <id> question from <from-build>` and a line for the `intake`
  ending ` · amendment`, and no line for the answered one; the same plant's plain engine call prints
  no `interrupt — mail` line and the same answer.
  Red when: the interrupt prints `unarmed` with the kit present, an answered message is listed, or a
  plain engine call reads the mailbox.
  fixture: the plant's repository holds a bare remote with one mail ref, `RUN_CLAIMS=on`, and the
  unattended kit at the fixture prefix.
- **AC2** — When `bash card-store.fixture.sh --plant mail-boundary` runs `--card --boundary` with the
  session card at `item — K1`, the stub engine answering `K2` and one open message, the output holds
  `boundary — K1 → K2` and then the message's `interrupt — mail` line; run again with no crossing, it
  prints no mail line and the stub records no `--mail-interrupts` call; with `--local` passed, the
  stub driver records `--mail read` with `--local`.
  Red when: a crossing reads no mail, or a run with no crossing reads it.
- **AC3** — When `python position.py --fixture --plant mail-transitions-only` runs `--mail-interrupts`
  with `mailbox.reads = "transitions-only"` planted and an open message waiting, it prints only
  `interrupt — mail · read at transitions (mailbox.reads: transitions-only)`.
  Red when: a boundary read runs under `transitions-only`.
- **AC4** — When `python position.py --fixture --plant mail-amendments` runs `--mail-interrupts` with
  `mailbox.reads = "every-item-amendments-at-transitions"` planted, one open `changed` and one open
  `intake`, it lists the `changed` and prints `interrupt — mail · 1 intake held to the next transition`
  with the key's value.
  Red when: the `intake` is listed at the boundary, or the `changed` is held.
- **AC5** — When `python position.py --fixture --plant mail-unarmed` runs `--mail-interrupts` with the
  unattended kit removed from the fixture prefix, it prints `interrupt — mail · unarmed` naming the kit
  and exits 0.
  Red when: a missing kit raises, or reads as an empty mailbox.
- **AC6** — When `mail-open` runs with the policy read of `mailbox.reads` refused, it reads
  `every-item`, lists the open messages and prints one NOTE naming `mailbox.reads`.
  Red when: a refused read silences the interrupt.
- **AC7** — When `grep -n 'mailbox.reads\|interrupt — mail\|intake'` runs over `loop.md`, the loop
  kit's help page, each is found in its mail interrupt section.
  Red when: the page does not state the read point.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `python resolver (behaviour + inline parity + idiom ban)` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/loop/position.py · covers AC1 AC3 AC4 AC5 AC6 · the four `--plant` cases, `mail-open` staged red by the interrupt left `unarmed` · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 · the `mail-boundary` plant, staged red by the step run with no crossing · none

## 8. Open questions

- **F1 — Which recipients does the read list as addressed to the build?** Options: (a) the rows
  `check_mail_addressed <to> build:<slug>` admits, `build:<slug>` and a `unit:` of the build, the set
  unit 5's guard holds a transition for; (b) those and `project`, which no guard holds and which
  `KICK-dKeptSession-28` matches only for a reader answering as `project`. cl-dClosedLoop-0143 reads
  "a message addressed to the build". RESOLVED (agent, 2026-10-26, delegated): (a), rung 1.
  widens: none · relaxes: none
- **F2 — Where does the read run, so the boundary is known before it?** Options: (a) behind
  `--mail-interrupts`, called by unit 13's boundary verb after a crossing, every other engine call
  reading no mail; (b) inside `derive_position`, which `derive_item_boundary` calls before it knows the
  crossing, so every `--status` and `--plan` would read the mailbox and the key's `every-item` would
  mean every engine call. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1233 and FR-8 name
  the item boundary. widens: none · relaxes: none
- **F3 — TOOL-dDeclaredLoop-7 S4 says the mail interrupt prints `unarmed` "until dWellOiledMachine
  lands the mailbox", and v2:1771 gives the mailbox to dKeptSession. What does this unit do with the
  parent's text?** Options: (a) arm the interrupt here, as the clause says, and state an ask for
  dDeclaredLoop that the main loop files in `memory/builds/dDeclaredLoop/BACKLOG.md`; (b) edit the
  parent spec, which the brief bars; (c) leave it, so the parent's record names the wrong armer for
  good. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1771. Ask: target dDeclaredLoop ·
  accept TOOL-dDeclaredLoop-7 S4 names dKeptSession's KICK-dKeptSession-10 as the unit that arms the
  mailbox interrupt, at the item boundary KICK-dKeptSession-13's verb provides, its text amended in
  place by a rev bump with its §9 line. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 10, scout B row 3 and its
  disagreement 1, Shared interfaces I8, I12, I14, I18, I19 and I20, KICK-dKeptSession-13 S6, FR-8,
  v2:1233 and v2:1555.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dDeclaredLoop-7 S4's mail interrupt in `tools/loop/position.py`, specced
`unarmed`, and `KICK-dKeptSession-13`'s boundary verb in `skills/session-kickoff/manifest-check.sh`;
this unit arms the first inside the second through the one mail reader, I20's `read_mailbox`, reached
by subprocess through `resolve_kit_dir` as TOOL-dDeclaredLoop-12 S4 reaches the playbook kit. Neither
the engine nor the verb exists at base: `tools/loop/` is absent and `grep -rn mailbox tools` finds
nothing, so every seam is a spec section, dDeclaredLoop's read at `origin/main`. `python
tools/codebase-map/reuse_lookup.py "read the mailbox at each item boundary of the position engine"`
ranked `read`, `read_text`, `engine` and `read_conf`, name stems only; no existing function reads a
mailbox or an item boundary, so no code seam fits beyond the specs'. `python
tools/memory-recall/query.py "when is the build mailbox read at an item boundary"` returned scout B's
row 3, this build's brief and FR-8's settled text; scout B's disagreement 1, the parent naming
dWellOiledMachine, holds against the parent's text at `origin/main` and is §8 F3.

Recall terms used: mailbox.reads every-item intake interrupt position engine item boundary transitions-only amendments derive_item_boundary unarmed
