# KICK-dKeptSession-10 — the mailbox read at every item boundary: `mailbox.reads` arming the position engine's mail interrupt, with the `intake` kind

**Status:** DEFERRED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 20 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0148@ab3d7b8c whole
**Carries:** node:policy-key.mailbox.reads

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-10-deviation-101.md](../build/2026-10-26-build-KICK-dKeptSession-10-deviation-101.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-10-deviation-102.md](../build/2026-10-26-build-KICK-dKeptSession-10-deviation-102.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-10-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md) | research | KICK-dKeptSession-25 KICK-dKeptSession-21 |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-5 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

The build's mailbox is read at every item boundary, as `mailbox.reads` says, and each open message
addressed to the build is listed as the position engine's mailbox interrupt, so a message that
arrives mid-step, an amendment from another session or a parent's breaking change, waits one item
rather than one step. That is flow-roles FR-8's answer, "Every item, plus an intake kind"
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb3965:232`).
The landed engine prints that interrupt `unarmed` on every call
(`tools/loop/position.py#derive_interrupts`). This unit arms it behind a flag of its own, read at the
one item-boundary point `KICK-dKeptSession-13` provides, and gives the `intake` kind, which
`KICK-dKeptSession-5` declares, the line a lease holder reads as an amendment.

## 2. Scope (IN)

- **S1** — The boundary step. `run_mail_interrupts <slug> <out file>` in
  `skills/session-kickoff/manifest-check.sh` runs inside `KICK-dKeptSession-13`'s boundary verb,
  `manifest-check.sh --card --boundary --build <slug> --session <sid>` (its S6), only after that
  verb's `run_item_boundary` answers a crossing, and after `KICK-dKeptSession-21`'s notice step where
  that unit has landed. It runs `python <loop kit>/position.py <slug> --mail-interrupts`, with
  `--local` when the notice line ends ` · fetched`. The loop kit is resolved by `resolve_kit_file loop
  position.py` (`skills/session-kickoff/manifest-check.sh#resolve_kit_file`) and the python by
  `resolve_python`. The call runs under `timeout -k 2 "$CARD_CLAIMS_BOUND"`
  (`skills/session-kickoff/manifest-check.sh#CARD_CLAIMS_BOUND`), the bound the card's other mail read
  takes (unit 5 S13). The verb prints the lines it returns after its `boundary —` line. No crossing
  runs no read. A kill at the bound prints `interrupt — mailbox · unarmed · the read passed its
  <n>s bound`, and no loop kit or python resolving prints `interrupt — mailbox · unarmed · <why>`.
  These lines reach the session as unit 13's other lines do: its hook starts the verb detached with
  `--out` and emits that file at the session's next Bash or PowerShell call after the verb finishes
  (its S7), never on the call that noticed the boundary. Observed by AC2.
- **S2** — The interrupt, `read_mail_interrupts(repo, slug, local)` in `tools/loop/position.py`,
  behind the bare CLI flag `--mail-interrupts`, which reads the positional `<slug>`
  (`tools/loop/position.py#main`) and is refused without one and beside `--json`, `--next-line`,
  `--check-refusal` or `--fixture`. The `script:{prefix}/loop/position.py` row of
  `tools/govkit/usage.toml` gains `--mail-interrupts` and `--local` in its `flags`, so the docs leg
  tests the page's commands against them, and the row's anchor in `help/loop.md` is re-stamped with the
  fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints. It runs `[bash, driver, "--mail", "read", slug,
  "--open"]`, `"--local"` appended when `local`, in `repo` with stdin closed, under unit 5's
  `MAIL_GUARD_SECONDS` in `tools/loop/loop_transition.py`, the bound of that unit's read of the same
  verb (its S9). The driver and the bash are found as `read_handover` finds them:
  `resolve_kit_dir("unattended", "unattended.sh", KIT)` and `resolve_bash(driver)`
  (`tools/loop/position.py#read_handover`, `tools/loop/loop_witness.py#resolve_bash`), a subprocess
  and never an import. Each row, unit 5 S6's TAB-separated columns `id`, `kind`, `to`, `state`,
  `first-seen` and `from-build` first, prints one line in the engine's interrupt shape,
  `interrupt — mailbox · <id> <kind> from <from-build>`, ordered by `first-seen` then id, a `-`
  sighting last. Only this flag reads the mailbox: `derive_interrupts` and every other engine call
  keep their landed `interrupt — mailbox · unarmed` line and read no mail, so `derive_item_boundary`,
  which calls `derive_position`, never reads it (§8 F2). A mailbox line changes no answer; refusing a
  transition over an open message is unit 5's guard. The module docstring's WHAT THIS DOES NOT CHECK
  names this flag as the one mailbox read. Exit 0. Each `mail-` plant joins `FX_DRIVER`, so its
  scratch repository holds the `.unattended.conf` copied from this tree, set `RUN_CLAIMS="on"` there,
  since a conf with it off reads `mail — off` and no row; the driver is this tree's, located beside
  the loop kit, never a copy; the messages are commits pushed straight to the plant's bare remote, as
  unit 5 S13's plants push theirs; and a planted policy file is committed before the plant's push of
  `main`, since `resolve` reads `refs/remotes/<remote>/main` and never the working tree
  (`tools/policy/policy.py#derive_landed_revision`). Observed by AC1.
- **S3** — `mailbox.reads` (`every-item`, `transitions-only`, `every-item-amendments-at-transitions`;
  default `every-item`), its row landed in `tools/policy/catalogue.toml`, owner dKeptSession. It is
  read as the loop kit reads every policy key: `read_policy_kit()`
  (`tools/loop/loop_parents.py#read_policy_kit`), then `policy.resolve("mailbox.reads",
  str(repo)).value`, the key a string literal at its read, as
  `tools/loop/claim.py#read_claim_policy` writes its reads. A `policy.Refusal`, or a `LookupError`
  where no policy kit resolves, reads the catalogue default and prints one `loop: NOTE -` line naming
  the key and its cause. `every-item` lists every kind. `transitions-only` runs no read and prints one
  line, `interrupt — mailbox · read at transitions (mailbox.reads: transitions-only)`.
  `every-item-amendments-at-transitions` lists every kind but `intake` and prints one line counting
  the held ones, `interrupt — mailbox · <n> intake held to the next transition (mailbox.reads:
  every-item-amendments-at-transitions)`, and no such line where none is held. Observed by AC3, AC4
  and AC6.
- **S4** — `--mail-interrupts --local` passes `--local` to the read, a read of the node's cache with
  no fetch, the flag `KICK-dKeptSession-21` S2 adds to `--mail read`. Until that unit lands the driver
  refuses the flag and the read prints S6's `unarmed` line naming the refusal, and S1 never passes it,
  since only that unit's notice step prints a line ending ` · fetched`. NOT OBSERVED here: the
  pass-through is observed against the driver that parses the flag, by `KICK-dKeptSession-21` AC3 and
  `KICK-dKeptSession-44` AC3.
- **S5** — The `intake` kind is one of the twelve `KICK-dKeptSession-5` S3 declares in
  `tools/loop/loop.toml`'s `[mail]` table, so this unit adds no kind. Its interrupt line ends
  ` · amendment`, so the session holding the build's lease reads it as a request to amend and
  disposes it through unit 5's verbs. Observed by AC1 and AC4.
- **S6** — The unarmed case. Where the unattended driver does not resolve (`LookupError`), no bash
  can see it (`resolve_bash` answers `None`), the read exits non-zero or its bound fires, the flag
  prints `interrupt — mailbox · unarmed · <cause>`, naming the driver's path, the exit and the first
  stderr line, or the bound, and exits 0. Observed by AC5.
- **S7** — The key's row. The `mailbox.reads` row of `tools/policy/catalogue.toml` gains `summary` and
  `usage`; `python tools/policy/policy.py lists --write` takes it off
  `tools/policy/unsummarised-keys.txt`; and `help/reference/policy.md` is re-rendered by `python
  tools/playbook/render_playbook.py --reference`, as `KICK-dKeptSession-13` S5 does for
  `card.pointers`. Observed by AC8.
- **S8** — The page `help/loop.md` gains, under "Where a build is, and what runs next", the mailbox
  interrupt: the flag, its read point at the item boundary, its lines, the three values of
  `mailbox.reads`, the `intake` line, and that the lines appear at the shell call after the boundary
  verb finishes. Observed by AC7.

## 3. Non-goals (OUT)

- No mailbox, reader, kind list or transition guard: `KICK-dKeptSession-5`'s. The read at a
  transition is that guard's, under every value of `mailbox.reads`.
- No item boundary and no boundary verb: `KICK-dKeptSession-13`'s; this unit adds one step inside it.
- No fetch of the mail refs of its own, and no `--local` in the driver: the reader's fetch is unit
  5's, and the notice's fetch and `--local` are `KICK-dKeptSession-21`'s.
- No change to `derive_interrupts`' landed `interrupt — mailbox · unarmed` line on a plain engine
  call: that text is the parent's, and dDeclaredLoop holds the ask for it (§8 F3).
- No dispatch of a message: `next` listing messages as next actions is dWellOiledMachine's, and the
  `question` answer is `KICK-dKeptSession-25`'s.
- No refusal of an `intake` posted by the lease holder: neither FR-8 nor the clause asks for one.
- No `project` or `node:` interrupt: unit 5's guard gates `build:` and `unit:` recipients only, and
  this read lists what that guard holds (§8 F1).
- No catalogue row: the landed `mailbox.reads` row stands, and this unit writes its `summary` and
  `usage` only.
- No kit version: the lander mints it (`tools/push-main.sh@78f40c3c2475:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, `run_item_boundary` and the `--card --boundary` verb, the one item-boundary point the read runs inside
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, read through `--mail read --open`, its `MAIL_GUARD_SECONDS`, and the `intake` kind in its `[mail]` table
- **consumes-from** external — the landed position engine's `derive_interrupts`, `read_handover` and `resolve_bash` (TOOL-dDeclaredLoop-7), the loop kit's `read_policy_kit` and the policy kit's `resolve`, and the landed `mailbox.reads` row
- **hands-off** external — dDeclaredLoop's next pass amends TOOL-dDeclaredLoop-7 S4's text to name dKeptSession as the build arming the mailbox interrupt, the ask TOOL-dDeclaredLoop-103 in its `BACKLOG.md` (§8 F3)
- **hands-off** `KICK-dKeptSession-44` — `read_mail_interrupts` and its `--local` step, the batch's S3, S16 and S19 (ids 6, 23, 33)

## 4. Design

### Evidence

- The engine's interrupts come in `[position]`'s order: owner decisions, the mailbox, invalidated
  witnesses, an absent remote, dependency gates, the undecided ask. The mailbox entry is
  `{"kind": "mailbox", "subject": "unarmed"}` on every call, and each prints as
  `interrupt — <kind> · <subject>` (`tools/loop/position.py#derive_interrupts`,
  `tools/loop/position.py#render_position_lines`).
- FR-8's settled text gives `intake` as an amendment from a session that does not hold the build's
  lease to the session that does
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb3965:248`).
- The catalogue default of `mailbox.reads` is `every-item` (`tools/policy/catalogue.toml`, row
  `mailbox.reads`), and every preset keeps it
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1555`).
- The engine already runs the unattended driver once, for `--plan`, through `resolve_kit_dir`,
  `resolve_bash` and `subprocess.run` (`tools/loop/position.py#read_handover`), and unit 5 S9 runs
  `--mail read` from the transition writer the same way.
- The loop kit reads policy keys in process, `read_policy_kit()` then `policy.resolve(<key>, root)`,
  in `claim.py`, `loop_parents.py`, `budget.py`, `adapt.py`, `composition.py`, `guard.py` and
  `loop_transition.py` (`tools/loop/loop_parents.py#derive_parent_route` is one).
- Unit 13 S6 makes `--card --boundary` the one item-boundary point and names `mailbox.reads` among the
  readers inside it. Its S7 starts that verb detached with `--out <git common dir>/orientation/<sid>.boundary`
  and emits the file as PreToolUse `additionalContext` at the next Bash or PowerShell call.

### The boundary step, in order

1. The boundary verb answers a crossing (unit 13 S6).
2. Unit 21's notice step runs where `mailbox.notice` admits it, and its line says whether it fetched.
3. `run_mail_interrupts` runs `position.py <slug> --mail-interrupts`, with `--local` after a fetch.
4. The flag resolves `mailbox.reads`; `transitions-only` prints its one line and returns.
5. It runs `--mail read <slug> --open [--local]`, keeps the rows, sets `intake` aside under the third
   value, and prints one line per kept row and the held count.
6. The verb's lines, these among them, reach the session at its next shell call after the verb ends.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_mail_interrupts` | Python function, `tools/loop/position.py` | `py.function`, OK by `lexicon.py --suggest` |
| `--mail-interrupts`, `--local` | CLI flags of `tools/loop/position.py` | none |
| `run_mail_interrupts` | shell function, `skills/session-kickoff/manifest-check.sh` | `sh.function`, OK by `lexicon.py --suggest` |
| `mail-open`, `mail-transitions-only`, `mail-amendments`, `mail-unarmed`, `mail-refused` | `--plant` cases of `position.py --fixture` | none |
| `mail-boundary` | plant of `skills/session-kickoff/card-store.fixture.sh` | none |

The `mail-boundary` plant writes its `--mail-interrupts` answer into the plant file unit 13 S9's
stub `position.py` answers from, and adds no second stub.

### Migration

None: no position is stored.

### Rollout

Live once unit 5's mailbox and unit 13's boundary verb are built, both earlier in build order. A
build with no open mail prints no mailbox line at a boundary.

### Files touched (estimate)

- `tools/loop/position.py`: `read_mail_interrupts`, `--mail-interrupts`, `--local`, five plants with
  their cases and `FX_DRIVER` members, the docstring's mailbox sentence
- `tools/govkit/usage.toml`: `--mail-interrupts` and `--local` in the `position.py` row's `flags`
- `tools/run-gates/selftest-budgets.txt`: the `loop position fixtures` row's `plants=<n>` token five
  above the count the units before it leave, its reading re-priced by direct CLI (DERIVED:
  `len(PLANTS)` of `tools/loop/position.py`, 31 read on 2026-11-21 before unit 13's `boundary`)
- `memory/map/generated/symbols.json`: `read_mail_interrupts` and `run_mail_interrupts`
- `skills/session-kickoff/manifest-check.sh`: `run_mail_interrupts` inside `--card --boundary`
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: the `mail-boundary` plant
- `skills/session-kickoff/manifest-check.test.sh`: its arm
- `tools/policy/catalogue.toml`: the `mailbox.reads` row's `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `help/reference/policy.md`: re-rendered by `render_playbook.py --reference`
- `help/loop.md`: the mailbox interrupt paragraph, and the `script:tools/loop/position.py` anchor
  re-stamped

### Alternatives rejected

- **A mail reader in the loop kit.** A second parser of unit 5's record beside `read_mailbox`, the
  one reader.
- **The mail read inside `derive_position`.** `derive_item_boundary` calls the engine, so the read
  would run before the crossing is known, and at every `--status` and `--plan` as well.
- **An `awaiting` answer while a message is open.** It would stop an item the message may not
  concern; the transition guard is where an unanswered message holds the build.
- **`mailbox.reads` through `policy.py get` as a subprocess**, rev-3's read. The landed loop kit
  resolves every key in process, so one subprocess reader would stand beside seven in-process ones.

## 5. Production-readiness checklist

- security — read-only: one subprocess of the unattended driver with a fixed argv and no shell
  string; the policy read is in process, as the loop kit's other reads are.
- perf / scale — one `--mail read` per crossing, none without one and none under `transitions-only`,
  local after the notice's fetch. The step is bounded by `CARD_CLAIMS_BOUND`, 15 s (PINNED, unit 5's
  figure for the card's mail read), inside the detached verb, so no tool call waits on it.
- error / empty / loading states — a missing driver, a failed read or a fired bound prints `unarmed`
  with its cause and exits 0; an empty mailbox prints nothing.
- observability — each open message is one `interrupt — mailbox` line; a held `intake` is counted.
- risks — without a notice fetch first, a slow remote delays the verb's lines by up to the bound, and
  the session reads them one shell call after the verb ends.
- testing — the plants of §6 and the arms of §7.
- migration — none.
- user docs — `help/loop.md` and `help/reference/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant mail-open` runs `--mail-interrupts`
  over a build holding one open `question` and one open `intake` addressed to `build:<slug>` and one
  `answered` message, it prints `interrupt — mailbox · <id> question from <from-build>` and a line
  for the `intake` ending ` · amendment`, and no line for the answered one; the same plant's plain
  engine call prints its one landed `interrupt — mailbox · unarmed` line, no message id, and the same
  answer.
  Red when: the flag prints `unarmed` with the driver present, an answered message is listed, or a
  plain engine call reads the mailbox.
  fixture: the plant's scratch repository, a `FX_DRIVER` member holding the copied `.unattended.conf`
  set `RUN_CLAIMS="on"`, and its bare remote holding the messages' mail refs, pushed straight; the
  driver is the one beside this tree's loop kit (S2).
- **AC2** — When `bash skills/session-kickoff/card-store.fixture.sh --plant mail-boundary` runs
  `--card --boundary` with the session card at `item — K1`, the stub engine answering `K2` and its
  `--mail-interrupts` answer one line, the output holds `boundary — K1 → K2` and then that
  `interrupt — mailbox` line; run again with no crossing, it prints no mailbox line and the stub
  records no `--mail-interrupts` call.
  Red when: a crossing reads no mail, or a run with no crossing reads it.
- **AC3** — When `python tools/loop/position.py --fixture --plant mail-transitions-only` runs
  `--mail-interrupts` with `mailbox.reads = "transitions-only"` planted and an open message waiting,
  it prints only `interrupt — mailbox · read at transitions (mailbox.reads: transitions-only)`.
  Red when: a boundary read runs under `transitions-only`.
- **AC4** — When `python tools/loop/position.py --fixture --plant mail-amendments` runs
  `--mail-interrupts` with `mailbox.reads = "every-item-amendments-at-transitions"` planted, one open
  `changed` and one open `intake`, it lists the `changed` and prints
  `interrupt — mailbox · 1 intake held to the next transition` with the key's value.
  Red when: the `intake` is listed at the boundary, or the `changed` is held.
  figure: the held count is PINNED, the plant's one `intake`.
- **AC5** — When `python tools/loop/position.py --fixture --plant mail-unarmed` runs
  `--mail-interrupts` with `resolve_kit_dir` rebound for the run to the real locator over an empty
  scratch directory as `here`, as `KICK-dKeptSession-36`'s `mail-no-driver` stages its miss, it prints
  `interrupt — mailbox · unarmed` naming the `unattended` kit and exits 0.
  Red when: a missing driver raises, or reads as an empty mailbox.
- **AC6** — When `python tools/loop/position.py --fixture --plant mail-refused` runs
  `--mail-interrupts` with `mailbox.reads` planted outside its allowed set in the remote's first
  revision of `.governance/policy.toml`, so `resolve` refuses it, since an invalid file over a valid
  one reads that one, as `read_last_valid_value` in `tools/policy/policy.py` rules, it reads `every-item`, lists
  `mail-open`'s open messages and prints one `loop: NOTE -` line naming
  `mailbox.reads`.
  Red when: a refused read silences the interrupt.
- **AC7** — When `grep -n 'mail-interrupts\|mailbox.reads\|intake' help/loop.md` runs, each is found
  in the section "Where a build is, and what runs next"; and `python tools/govkit/docs_leg.py
  --fingerprints` prints `script:tools/loop/position.py` with the fingerprint its `help/loop.md`
  anchor carries.
  Red when: the page does not state the read point, or the anchor keeps the fingerprint from before
  `--mail-interrupts`.
- **AC8** — When `python tools/policy/policy.py get mailbox.reads` runs in a repository whose policy
  file sets no value, it prints `every-item`, and after `policy.py lists --write`
  `tools/policy/unsummarised-keys.txt` no longer names `mailbox.reads`.
  Red when: the row is still unsummarised.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `routed-commits selftest` · `policy check` · `help reference pages` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `docs` · `loop position fixtures` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC3 AC4 AC5 AC6 · the five `--plant` cases, `mail-open` staged red by the interrupt left `unarmed` · the `loop position fixtures` row's `plants=<n>` token rises by five
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 · the `mail-boundary` plant, staged red by the step run with no crossing · `FLOOR_ASSERTIONS` rises by the plant's rows

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
  mean every engine call. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1; the `mailbox.reads`
  row (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1233`)
  and FR-8 name the item boundary. widens: none · relaxes: none
- **F3 — TOOL-dDeclaredLoop-7 S4 says the mail interrupt prints `unarmed` "until dWellOiledMachine
  lands the mailbox", and v2's chain row gives the mailbox to dKeptSession. What does this unit do with
  the parent's text?** Options: (a) arm the interrupt here, as the clause says, and state an ask for
  dDeclaredLoop that the main loop files in `memory/builds/dDeclaredLoop/BACKLOG.md`; (b) edit the
  parent spec, which the brief bars; (c) leave it, so the parent's record names the wrong armer for
  good. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the chain row
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1771`).
  Ask: target dDeclaredLoop · accept TOOL-dDeclaredLoop-7 S4 names dKeptSession's KICK-dKeptSession-10
  as the unit that arms the mailbox interrupt, at the item boundary KICK-dKeptSession-13's verb
  provides, its text amended in place by a rev bump with its §9 line. Filed as TOOL-dDeclaredLoop-103,
  open at this writing; the landed engine's plain call still prints `unarmed`, which this unit leaves.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 10, scout B row 3 and its
  disagreement 1, Shared interfaces I8, I12, I14, I18, I19 and I20, KICK-dKeptSession-13 S6, FR-8,
  and the `mailbox.reads` rows of v2.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-10-26 · §2 S3 · §3 Edges · §5 · re-grounded on dDeclaredLoop at `783f1ad3a` by the
  cross-check record `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, row 39:
  `mailbox.reads` is read by `policy.py get` as a subprocess through `loop_lib.py`'s inline
  `resolve_kit_dir`, never an in-process `resolve`.
- rev-4 · 2026-11-21 · §1 · S1 to S8 · §3 · §4 · §5 · AC1 to AC8 · §7 · §8 F2 F3 · §10 · re-grounded
  on the landed tree at `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief`:
  the engine's interrupt kind is `mailbox`, so every line reads `interrupt — mailbox`, and AC1's plain
  call keeps its landed `unarmed` line; S2 runs the driver as `read_handover` does, through
  `resolve_bash`, bounded by unit 5's `MAIL_GUARD_SECONDS`; S3 reverses rev-3, reading the key in
  process as the landed loop kit reads every key; S1 names `run_mail_interrupts`, its bound and that
  its lines reach the session at the next shell call after unit 13's detached verb ends; S7 and AC8
  give the landed row its summary. Narrowed: the `intake` kind is unit 5's `[mail]` table member and
  S5 keeps only its line; S4's pass-through is observed by units 21 and 44; the catalogue row stands.
  `policy fixtures`, `routed-commits selftest`, `policy check`, `help reference pages`, `loop position
  fixtures` and the recall legs joined the leg line, `kit epoch` left it; every line-number citation
  became a blob pin.
- rev-5 · 2026-11-21 · S1 · S2 · §4 · AC1 · AC5 · AC6 · AC7 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: the `plan-line` plant copies the driver's
  conf, never its kit, so AC1's fixture is a `FX_DRIVER` plant with `RUN_CLAIMS` on and AC5 stages
  the miss by the real locator over an empty `here`; `resolve` reads the landed revision, so a plant
  commits its policy file before pushing `main`, and AC6's invalid file is the first revision, since
  one over a valid file reads that file; `--mail-interrupts` reads the positional slug and joins
  `usage.toml`'s `position.py` row, whose `help/loop.md` anchor AC7 observes; the plants move the
  `loop position fixtures` token; `symbols.json`, `usage.toml` and the budget row joined Files
  touched, the manifest-check arm names its floor, and `docs` and the three govkit legs whose guard
  holds `usage.toml` joined the leg line.

## 10. Reuse audit

The seams extended are the landed engine's mailbox interrupt in `tools/loop/position.py#derive_interrupts`,
printed `unarmed`, armed here behind its own flag; the engine's one driver call,
`tools/loop/position.py#read_handover`, whose `resolve_kit_dir` and `resolve_bash` launch the read
copies; the loop kit's in-process policy read, `tools/loop/loop_parents.py#read_policy_kit`; and
`KICK-dKeptSession-13`'s boundary verb in `skills/session-kickoff/manifest-check.sh`, unbuilt at this
base, inside which the step runs. The one mail reader is unit 5's `read_mailbox`, reached through the
driver's `--mail read`. `python tools/codebase-map/reuse_lookup.py "read the mailbox at each item
boundary of the position engine"`, re-run at this writing, ranked `read_text`, `read`, `read_bytes`,
`read_git`, `read_memory_tree` and `engine` by name stem; none reads a mailbox or an item boundary,
so no code seam fits beyond the engine's own. `grep -rn 'mailbox' tools/loop/position.py` finds only
the `unarmed` entry and the docstring line naming it. Scout B's disagreement 1, the parent naming
dWellOiledMachine, holds against the landed parent text and is §8 F3, filed as TOOL-dDeclaredLoop-103.

Recall terms used: mailbox.reads every-item intake interrupt position engine item boundary transitions-only amendments derive_item_boundary unarmed read_handover
