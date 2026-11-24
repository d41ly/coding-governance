# KICK-dKeptSession-10 — the mailbox read at every item boundary: `mailbox.reads` arming the position engine's mail interrupt, with the `intake` kind

**Status:** CLOSED · rev-6 · 2026-11-23 · node a · Tier-2 · base d06e2a65 · streams kickoff · order 20 · advances KICK-dKeptSession-29

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
| [2026-11-21-build-KICK-dKeptSession-10-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-10-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md](../build/2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 KICK-dKeptSession-79 KICK-dKeptSession-80 KICK-dKeptSession-89 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-10-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-10-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md) | research | KICK-dKeptSession-25 KICK-dKeptSession-21 |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-5 |
| [2026-11-22-prompt-KICK-dKeptSession-10-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-10-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-10-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-10-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The build's mailbox is read at every item boundary, as `mailbox.reads` says, and each open message
addressed to the build is listed as the position engine's mailbox interrupt, so a message that
arrives mid-step, an amendment from another session or a parent's breaking change, waits one item
rather than one step. That is flow-roles FR-8's answer, "Every item, plus an intake kind"
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb3965:232`).
The landed engine prints that interrupt `unarmed` on every call
(`tools/loop/position.py#derive_interrupts`). This unit arms it behind a flag of its own, run at the
one item-boundary point `KICK-dKeptSession-13` landed, through the one mailbox read the loop kit
already makes, and gives the `intake` kind, which `KICK-dKeptSession-5` landed in the `[mail]`
table, the line a lease holder reads as an amendment.

## 2. Scope (IN)

- **S1** — The boundary step. `run_mail_interrupts <slug> [--local]` in
  `skills/session-kickoff/manifest-check.sh` is called by
  `skills/session-kickoff/manifest-check.sh#run_card_boundary` in its crossing branch, after
  `run_context_boundary`, with no `--local`. No crossing, and a `boundary — skipped:` answer, run
  no step. `KICK-dKeptSession-21`, landing after this unit, is the one caller that passes `--local`,
  after a notice line ending ` · fetched` (its S4). The step finds the engine by `resolve_kit_file
  loop position.py` and the python by `resolve_python`, refuses a node with no working `timeout -k`,
  each in `skills/session-kickoff/manifest-check.sh#run_item_boundary`'s words, and runs
  `<python> <engine> <slug> --mail-interrupts [--local]` with stdin closed under `timeout -k 2
  "$CARD_CLAIMS_BOUND"`, the bound `render_mail_line` gives the same driver read (15 s, PINNED at
  `skills/session-kickoff/manifest-check.sh@eb3e33878e89:323`). On exit 0 it prints each output line
  opening `interrupt — mailbox · `, CRs stripped, and no other line. A kill (124 or 137) prints
  `interrupt — mailbox · unarmed · the read passed its <n>s bound`; an unresolved engine, python or
  `timeout -k` prints `interrupt — mailbox · unarmed · <why>`; any other exit prints `interrupt —
  mailbox · unarmed · position.py --mail-interrupts exited <rc>: <its first non-empty line>`, cut
  as `run_item_boundary` cuts, to 160 bytes (PINNED, its figure). It returns 0. The lines reach the
  session as the verb's others do: `tools/hooks/scratch-guard.js#checkItemBoundary` starts the verb
  detached with `--out <git common dir>/orientation/<sid>.boundary` and returns that file, cut to
  `ROUTE_CONTEXT_CAP`, at the session's next Bash or PowerShell call. The `--card --boundary` usage comment at the head of
  the script gains "and the build's open mail as `interrupt — mailbox` lines, as mailbox.reads
  says". Observed by AC2.
- **S2** — The read. `read_mail_interrupts(repo, slug, local=False)` in `tools/loop/position.py`
  returns the flag's lines. `--mail-interrupts` reads the positional `<slug>`; `--local` is legal
  only beside it; `ap.error` refuses the flag without a slug or beside `--json`, `--next-line`,
  `--frontier`, `--boundary`, `--check-refusal`, `--fixture` or `--selftest`
  (`tools/loop/position.py#main`). `main` runs it over `git rev-parse --show-toplevel`'s answer, as
  it runs `derive_position`, prints each line and exits 0. The one read is
  `tools/loop/loop_transition.py#read_mail_rows`, the loop kit's landed launch of the driver's
  `--mail read <slug>`: the driver `resolve_kit_dir` locates, the bash `resolve_bash` answers,
  stdin closed, `read_clean_env()`, and `MAIL_GUARD_SECONDS` (30 s, PINNED at
  `tools/loop/loop_transition.py@2f3a26de0fd2:134`), returning `(rows, unarmed)`, each row a dict of
  `MAIL_COLUMNS`, `id` to `reply`. `read_mail_rows` gains one keyword, `local=False`, appending
  `"--local"` to its argv where true, and its docstring names it and this caller. The transition
  guard's call passes none, so its argv stays the one unit 36's `mail-argv` plant records. The
  kept rows are those whose `state` is `open`, the selection `--open` makes
  (`tools/unattended/unattended.sh#print_mailbox`), so `answered`, `acked`, `reply` and unit 24's
  `expired` rows are not listed; the columns units 27 and 24 append after `reply` are not read.
  Each kept row prints `interrupt — mailbox · <id> <kind> from <from-build>`, ordered by `first-seen` then id, a
  `-` sighting last. Only this flag reads the mailbox: `derive_interrupts` and every other call keep
  their landed `interrupt — mailbox · unarmed` line and read no mail, so `derive_item_boundary`,
  which calls `derive_position`, never reads it (§8 F2). A mailbox line changes no answer; refusing a
  transition over an open message is unit 5's guard. The `script:{prefix}/loop/position.py` row of
  `tools/govkit/usage.toml` gains `--mail-interrupts` and `--local` in its `flags`. Observed by AC1
  and AC9.
- **S3** — `mailbox.reads` (`every-item`, `transitions-only`, `every-item-amendments-at-transitions`;
  default `every-item`), its row landed in `tools/policy/catalogue.toml`, owner dKeptSession. It is
  read as the loop kit reads every policy key: `read_policy_kit()`
  (`tools/loop/loop_parents.py#read_policy_kit`), then `policy.resolve("mailbox.reads",
  str(repo)).value`, the key a string literal at its read, as
  `tools/loop/claim.py#read_claim_policy` writes its reads. A `policy.Refusal` reads the catalogue
  default, `policy.read_catalogue_row(policy.parse_key("mailbox.reads"),
  policy.load_catalogue(policy.KIT))["default"]`, never a typed copy, and prints `interrupt —
  mailbox · mailbox.reads refused, read as <default>: <why>`; a `LookupError`, no policy kit, lists
  every kind and prints `interrupt — mailbox · mailbox.reads unread, every kind listed: <why>`.
  `every-item` lists every kind. `transitions-only` runs no read and prints one line,
  `interrupt — mailbox · read at transitions (mailbox.reads: transitions-only)`.
  `every-item-amendments-at-transitions` lists every kind but `intake` and prints one line counting
  the held ones, `interrupt — mailbox · <n> intake held to the next transition (mailbox.reads:
  every-item-amendments-at-transitions)`, and no such line where none is held. Observed by AC3, AC4
  and AC6.
- **S4** — `--mail-interrupts --local` passes `local=True` to `read_mail_rows`, a read of the node's
  cache with no fetch, the flag `KICK-dKeptSession-21` S2 adds to `--mail read`. Until that unit
  lands the driver refuses it, `mail — not written · --mail takes … not --local`, exit 2
  (`tools/unattended/unattended.sh@a11693ddbd88:19840`), which S6 prints as `unarmed`, and S1
  never passes it. NOT OBSERVED here: the pass-through is observed against the
  driver that parses the flag, by `KICK-dKeptSession-21` AC3 and `KICK-dKeptSession-44` AC3.
- **S5** — The `intake` kind is one of the `[mail]` kinds `KICK-dKeptSession-5` landed in
  `tools/loop/loop.toml`, so this unit adds no kind. Its interrupt line ends ` · amendment`, so the
  session holding the build's lease reads it as a request to amend and disposes it through unit 5's
  verbs. Observed by AC1 and AC4.
- **S6** — The unarmed case. `read_mail_rows`' `unarmed` answer, the driver's locator refusing, a
  repository with no `.unattended.conf` or `mail — off`, prints `interrupt — mailbox · unarmed ·
  <why>`; its `ValueError`, `mail unknown: …`, for a driver no bash sees, a read silent within the
  bound or a non-zero read with no row, prints the same line with that error's words, which name
  the exit and the read's first line. Each exits 0. A list read from the node's cache after a failed
  fetch, which the driver names on stderr as `mail — local copy: <why>`, is listed unmarked. Observed
  by AC5.
- **S7** — The key's row. The `mailbox.reads` row of `tools/policy/catalogue.toml` gains `summary`
  and `usage`, the summary stating the three values as S3 does and that the transition guard reads
  the mailbox under each, the usage `mailbox.reads = "transitions-only"`.
  `python tools/policy/policy.py lists --write` takes it off `tools/policy/unsummarised-keys.txt`;
  `python tools/policy/policy.py mirror --write` re-renders `.governance/policy.json`, whose
  `catalogue_blob` the edit moves; `help/reference/policy.md` is re-rendered by
  `python tools/playbook/render_playbook.py --reference`, as `KICK-dKeptSession-14` did for its two
  keys. Observed by AC8.
- **S8** — The user texts. `help/loop.md`, under "Where a build is, and what runs next", gains one
  bullet: the flag, its read point after a crossing, its lines, the three values of
  `mailbox.reads` with `<!-- usage: policy:mailbox.reads <fp8> -->`, the `intake` line, and that the
  lines appear at the shell call after the boundary verb finishes. Its `script:tools/loop/position.py`
  anchor is re-stamped. Its fixture-cases sentence names every key of `PLANTS` the module holds at
  build time, the five plants and `boundary`, which it omits today, and its driver sentence every
  `FX_DRIVER` member. The `policy:mailbox.reads` row leaves `memory/project/docs-undocumented.txt`,
  by hand, as `KICK-dKeptSession-14` drained its two, since an anchored member still listed is the
  docs leg's `DRAINED` finding. `help/orientation-card.md`'s "When the section is rewritten"
  paragraph gains one sentence after the crossing's `boundary —` line: the verb then lists each open
  message as an `interrupt — mailbox` line, as `mailbox.reads` says, pointing at the loop page's
  section by name. The engine's module docstring gains a usage line, one THE MAILBOX INTERRUPT
  paragraph stating S2 to S6, the five plants in its driver sentence, and its WHAT THIS DOES NOT
  CHECK clause "the mailbox, printed `unarmed`" becomes "the mailbox on every call but
  `--mail-interrupts`, printed `unarmed`; a list read from the cache after a failed fetch, listed
  unmarked". `tools/loop/README.md`'s position-engine section gains one sentence and one usage line
  for the flag, and its "the last two over the unattended driver" becomes "the `FX_DRIVER` plants
  over the unattended driver". Observed by AC7.

## 3. Non-goals (OUT)

- No mailbox, reader, kind list or transition guard: `KICK-dKeptSession-5`'s. The read at a
  transition is that guard's, under every value of `mailbox.reads`.
- No item boundary and no boundary verb: `KICK-dKeptSession-13`'s; this unit adds one step inside it.
- No fetch of its own and no `--local` in the driver: the reader's fetch is unit 5's, and the
  notice's fetch and `--local` are `KICK-dKeptSession-21`'s.
- No edit to `tools/unattended/unattended.sh`: the read is the landed `--mail read`, so no `fail`,
  `exit 1` or `status=1` site is added against its harness-arms ceiling, 347 of 347 by the brief.
- No change to `derive_interrupts`' landed `interrupt — mailbox · unarmed` line on a plain engine
  call: that text is the parent's, and dDeclaredLoop holds the ask for it (§8 F3).
- No dispatch of a message: `next` listing messages as next actions is dWellOiledMachine's, and the
  `question` answer is `KICK-dKeptSession-25`'s.
- No refusal of an `intake` posted by the lease holder: neither FR-8 nor the clause asks for one.
- No `project` or `node:` interrupt: unit 5's guard gates `build:` and `unit:` recipients only, and
  this read lists what that guard holds (§8 F1).
- No catalogue row: the landed `mailbox.reads` row stands, and this unit writes its `summary` and
  `usage` only.
- No kit version: the lander mints it (`tools/push-main.sh@3a5bf825e879:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, `run_item_boundary` and the `--card --boundary` verb, the one item-boundary point the read runs inside
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, reached through `read_mail_rows` and its `MAIL_GUARD_SECONDS`, and the `intake` kind in its `[mail]` table
- **consumes-from** external — the landed position engine's `derive_interrupts` (TOOL-dDeclaredLoop-7), the loop kit's `read_policy_kit`, the policy kit's `resolve`, and the landed `mailbox.reads` row
- **hands-off** external — dDeclaredLoop's next pass amends TOOL-dDeclaredLoop-7 S4's text to name dKeptSession as the build arming the mailbox interrupt, the ask TOOL-dDeclaredLoop-103 in its `BACKLOG.md` (§8 F3)
- **hands-off** `KICK-dKeptSession-44` — `read_mail_interrupts` and its `--local` step, the batch's S3, S16 and S19 (ids 6, 23, 33)

## 4. Design

### Evidence

- The engine's interrupts come in `[position]`'s order; the mailbox entry is `{"kind": "mailbox",
  "subject": "unarmed"}` on every call, printed as `interrupt — <kind> · <subject>`
  (`tools/loop/position.py#derive_interrupts`, `tools/loop/position.py#render_position_lines`).
- FR-8's settled text gives `intake` as an amendment from a session that does not hold the build's
  lease to the session that does
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb3965:248`).
- The catalogue default of `mailbox.reads` is `every-item` (`tools/policy/catalogue.toml`, row
  `mailbox.reads`), and every preset keeps it
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1555`).
- `read_mail_rows` handles every outcome this read needs: a locator refusal, no conf and
  `mail — off` as `unarmed`; no bash, a silent read and a failed read as `mail unknown`; rows of
  eleven or more fields zipped with `MAIL_COLUMNS` (`tools/loop/loop_transition.py#read_mail_rows`).
  `KICK-dKeptSession-27` and `-24` append five columns after `reply`, leaving the first eleven.
- `print_mailbox`'s `--open` keeps rows whose fourth column is `open`; `read_mailbox` prints rows
  oldest sighting first (`tools/unattended/unattended.sh#read_mailbox`).
- The loop kit reads policy keys in process, `read_policy_kit()` then `policy.resolve(<key>,
  root)`, in `claim.py`, `loop_parents.py`, `budget.py` and others
  (`tools/loop/loop_parents.py#derive_parent_route` is one). No loop module prints a `NOTE` line.
- `run_card_boundary`'s crossing branch prints the `boundary —` line, writes the section, publishes
  under `card.pointers` and runs `run_context_boundary`; its comment already names `mailbox.reads`
  among the readers run there (`skills/session-kickoff/manifest-check.sh#run_card_boundary`).

### The boundary step, in order

1. The boundary verb answers a crossing (unit 13 S6).
2. `run_mail_interrupts` runs `position.py <slug> --mail-interrupts`.
3. The flag resolves `mailbox.reads`; `transitions-only` prints its one line and returns.
4. `read_mail_rows` runs `--mail read <slug>`; the flag keeps the open rows, sets `intake` aside
   under the third value, and prints one line per kept row and the held count.
5. The verb's lines, these among them, reach the session at its next shell call after the verb ends.

### The plants

Five `--plant` cases of `position.py --fixture`, each a `FX_DRIVER` member, so its scratch
repository holds the `.unattended.conf` and `.memory-tree.conf` copied from this tree, the conf
gaining the two lines `tools/loop/loop_transition.py#write_transition_plant` appends to its mail
plants, `RUN_CLAIMS="on"` among them, since a conf with it off reads `mail — off`. The driver is this
tree's, beside the loop kit. A planted `.governance/policy.toml` is in the fixture commit, pushed as
`main` with the other cases', since `resolve` reads `refs/remotes/<remote>/main`
(`tools/policy/policy.py#derive_landed_revision`). Each message is one parentless commit on its own
ref, `refs/gov/mail/<sender>/z/s-<n>`, its text `tools/loop/loop_transition.py#render_fixture_mail`'s,
pushed by `tools/loop/placement.py#write_fixture_gov_ref`, which gains `remote=FIXTURE_REMOTE`, the
position plant passing its remote's name read back from git. `check_mail_plant(case, repo,
definition, handover)` runs the read, prints its lines and returns the misses, as
`tools/loop/position.py#check_plan_line` does for its case.

| Case | Planted | Owed |
|---|---|---|
| `mail-open` | to `build:tPos` from `fy`: an open `question`, an open `intake`, and a `question` a `tPos` `answer` names | the two open lines in id order, the `intake` one ending ` · amendment`; the plain call's `interrupt — mailbox · unarmed` and no id |
| `mail-transitions-only` | `mail-open`'s messages; `[mailbox]` `reads = "transitions-only"` | the one `read at transitions` line alone |
| `mail-amendments` | an open `changed` and an open `intake`; `reads = "every-item-amendments-at-transitions"` | the `changed` line and `1 intake held to the next transition` |
| `mail-unarmed` | `mail-open`'s repository; `loop_lib.resolve_kit_dir` rebound for the call to the real locator over an empty scratch directory as `here`, restored after | one `unarmed` line naming the `unattended` kit, no exception |
| `mail-refused` | `mail-open`'s messages; `reads = "sometimes"` in the file's only revision | the `refused, read as every-item` line naming `mailbox.reads`, then `mail-open`'s two lines |

`mail-unarmed` rebinds the name `read_mail_rows` imports inside its function, as unit 36's
`mail-no-driver` does, so the read carries no test hook; `read_policy_kit` keeps the name
`loop_parents` bound at import.

The `mail-boundary` plant of `skills/session-kickoff/card-store.fixture.sh` adds no second stub:
the stub `position.py` gains one branch, `<slug> --mail-interrupts [--local]`, which appends its
arguments to `$CARD_STUB_POSITION.log`, sleeps the planted `mail-delay`, and prints the planted
`mail` line, the keys `set_card_position` writes; its refusal text, the file's header comment and
`set_card_position`'s comment name the branch and the two keys. `PLANTS` gains `mail-boundary`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_mail_interrupts` | Python function, `tools/loop/position.py` | `py.function`, OK by `lexicon.py --suggest` |
| `check_mail_plant` | Python function, `tools/loop/position.py` | `py.function`, OK by `lexicon.py --suggest` |
| `--mail-interrupts`, `--local` | CLI flags of `tools/loop/position.py` | none |
| `local`, `remote` | keyword parameters of `read_mail_rows` and `write_fixture_gov_ref` | none |
| `run_mail_interrupts` | shell function, `skills/session-kickoff/manifest-check.sh` | `sh.function`, OK by `lexicon.py --suggest` |
| `mail-open`, `mail-transitions-only`, `mail-amendments`, `mail-unarmed`, `mail-refused` | `--plant` cases of `position.py --fixture` | none |
| `mail-boundary` | plant of `skills/session-kickoff/card-store.fixture.sh` | none |
| `mail`, `mail-delay` | keys of the card-store stub's plant file | none |

### Migration

None: no position is stored.

### Rollout

Live once built: unit 5's mailbox and unit 13's boundary verb are landed. A build with no open mail
prints no mailbox line at a boundary.

### Files touched (estimate)

- `tools/loop/position.py`: `read_mail_interrupts`, `check_mail_plant`, the two flags, five plants
  with their `FX_DRIVER` members and `run_plant` branch, the docstring (S8)
- `tools/loop/loop_transition.py`: `read_mail_rows`' `local` keyword and its docstring
- `tools/loop/placement.py`: `write_fixture_gov_ref`'s `remote` keyword
- `tools/loop/README.md`: the position-engine sentence, usage line and driver phrase (S8)
- `tools/govkit/usage.toml`: the two flags in the `position.py` row's `flags`
- `tools/run-gates/selftest-budgets.txt`: the `loop position fixtures` row's `plants=32` set to
  `plants=37` (DERIVED: `len(PLANTS)` of `tools/loop/position.py`, 32 at `d06e2a65d`), its reading
  re-priced by direct CLI over the five as `KICK-dKeptSession-13` re-priced its one; and the
  `manifest-check self-test` row re-priced by the `mail-boundary` plant's direct-CLI reading, as
  `KICK-dKeptSession-5` re-priced its three, the row carrying no `plants=` token
- `memory/map/generated/symbols.json`: the three functions, by `python tools/codebase-map/gen_map.py
  --write`, never hand-edited
- `skills/session-kickoff/manifest-check.sh`: `run_mail_interrupts`, its call in
  `run_card_boundary`, the usage comment (S1)
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: the stub's branch, its comments and the
  `mail-boundary` plant
- `skills/session-kickoff/manifest-check.test.sh`: `FLOOR_ASSERTIONS`, 441 at `d06e2a65d` (DERIVED:
  its last assignment, `skills/session-kickoff/manifest-check.test.sh@990a71661936:2542`), raised to
  442 with a `+1: RAISED by KICK-dKeptSession-10` line, the card-store loop's one ok row for the plant
- `tools/policy/catalogue.toml`: the `mailbox.reads` row's `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `.governance/policy.json`: re-rendered by `policy.py mirror --write`
- `help/reference/policy.md`: re-rendered by `render_playbook.py --reference`
- `help/loop.md`: the bullet, both anchors and the two fixture sentences (S8)
- `help/orientation-card.md`: the one sentence (S8)
- `memory/project/docs-undocumented.txt`: the `policy:mailbox.reads` row deleted

The texts that stay as they are: `help/loop.md`'s guard paragraph under "Recording a build's move"
and `tools/loop/README.md`'s mail guard paragraph describe the guard's own unfiltered read, which
keeps its argv; `tools/unattended/VERBS.template.md`'s `--status` entry prints the plain call's
`interrupt —` lines, which keep the `unarmed` mailbox line; the comment above `run_card_boundary`
already names `mailbox.reads` among its readers; `tools/policy/presets.toml` keeps `every-item`.

### Alternatives rejected

- **A second launcher of `--mail read` in `position.py`**, rev-5's, beside `read_mail_rows`, the
  loop kit's landed one: two copies of the driver's location, bash, bound and error words.
- **A mail reader in the loop kit.** A second parser of unit 5's record beside `read_mailbox`.
- **The mail read inside `derive_position`.** `derive_item_boundary` calls the engine, so the read
  would run before the crossing is known, and at every `--status` and `--plan` as well.
- **An `awaiting` answer while a message is open.** It would stop an item the message may not
  concern; the transition guard is where an unanswered message holds the build.
- **A `loop: NOTE -` line for a refused key**, rev-5's: no loop module prints that shape, and the
  boundary step prints only `interrupt — mailbox` lines.

## 5. Production-readiness checklist

- security — read-only: the landed subprocess of the unattended driver with a fixed argv and no
  shell string; the policy read is in process, as the loop kit's other reads are.
- perf / scale — one `--mail read` per crossing, none without one and none under
  `transitions-only`. The step is bounded by `CARD_CLAIMS_BOUND` (15 s, PINNED, S1) inside the
  detached verb, so no tool call waits on it; the engine's own `MAIL_GUARD_SECONDS` (30 s, PINNED,
  S2) bounds a direct CLI call, and under the verb the outer kill comes first.
- error / empty / loading states — a missing driver, a failed read or a fired bound prints `unarmed`
  with its cause and exits 0; an empty mailbox prints nothing.
- observability — each open message is one `interrupt — mailbox` line; a held `intake` is counted.
- risks — a slow remote delays the verb's lines by up to the bound; a mailbox long enough to pass
  `ROUTE_CONTEXT_CAP` is cut there by the hook (`tools/hooks/scratch-guard.js#checkItemBoundary`).
- testing — the plants of §4 and the arms of §7.
- migration — none.
- user docs — `help/loop.md`, `help/orientation-card.md` and `help/reference/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant mail-open` runs, it prints
  `interrupt — mailbox · <id> question from fy` and the `intake` line ending ` · amendment`, no line
  for the answered `question` or its `answer`, and the same plant's plain engine call prints its one
  landed `interrupt — mailbox · unarmed` line and no message id; the case line reads `held`.
  Red when: the flag prints `unarmed` with the driver present, an answered message is listed, or a
  plain engine call reads the mailbox.
  fixture: the plant's scratch repository and bare remote, built by the case (§4 The plants).
- **AC2** — When `bash skills/session-kickoff/card-store.fixture.sh --plant mail-boundary` runs
  `--card --boundary` with the session card at `item — K1`, the stub engine answering `K2` and its
  planted `mail` line `interrupt — mailbox · m1 question from fy`, the output holds `boundary — K1 →
  K2` and then that line; run again with no crossing, it prints no mailbox line and
  `$CARD_STUB_POSITION.log` gains no `--mail-interrupts` row; and with `mail-delay` planted at 5 and
  `CARD_CLAIMS_BOUND=2` (PINNED), a crossing prints `interrupt — mailbox · unarmed · the read passed
  its 2s bound` (PINNED).
  Red when: a crossing reads no mail, a run with no crossing reads it, or a fired bound prints nothing.
  figure: the bound and the delay are PINNED, the plant's own values.
- **AC3** — When `python tools/loop/position.py --fixture --plant mail-transitions-only` runs,
  with `mailbox.reads = "transitions-only"` planted and open messages waiting, its read prints only
  `interrupt — mailbox · read at transitions (mailbox.reads: transitions-only)`.
  Red when: a boundary read runs under `transitions-only`.
- **AC4** — When `python tools/loop/position.py --fixture --plant mail-amendments` runs, with
  `mailbox.reads = "every-item-amendments-at-transitions"` planted, one open `changed` and one open
  `intake`, it lists the `changed` and prints `interrupt — mailbox · 1 intake held to the next
  transition (mailbox.reads: every-item-amendments-at-transitions)`.
  Red when: the `intake` is listed at the boundary, or the `changed` is held.
  figure: the held count is PINNED, the plant's one `intake`.
- **AC5** — When `python tools/loop/position.py --fixture --plant mail-unarmed` runs, with
  `loop_lib.resolve_kit_dir` rebound for the call to the real locator over an empty scratch
  directory, it prints one `interrupt — mailbox · unarmed` line naming the `unattended` kit and
  raises nothing.
  Red when: a missing driver raises, or reads as an empty mailbox.
- **AC6** — When `python tools/loop/position.py --fixture --plant mail-refused` runs, with
  `mailbox.reads = "sometimes"` in the only revision of `.governance/policy.toml`, so `resolve`
  refuses it, since an invalid file over a valid one reads that one, as `read_last_valid_value` in
  `tools/policy/policy.py` rules, it prints `interrupt — mailbox · mailbox.reads
  refused, read as every-item:` and the refusal, then `mail-open`'s two open lines.
  Red when: a refused read silences the interrupt, or the default is typed beside the catalogue.
- **AC7** — When `grep -n 'mail-interrupts\|mailbox.reads\|intake' help/loop.md` runs, each is found
  in the section "Where a build is, and what runs next"; `python tools/govkit/docs_leg.py
  --fingerprints` prints `script:tools/loop/position.py` and `policy:mailbox.reads` each with the
  fingerprint its `help/loop.md` anchor carries; `grep -c 'policy:mailbox.reads'
  memory/project/docs-undocumented.txt` prints `0`; and `grep -n 'interrupt — mailbox'
  help/orientation-card.md` finds the sentence.
  Red when: the page does not state the read point, an anchor keeps a stale fingerprint, or the
  member stays listed as undocumented.
  figure: the `script:` fingerprint read `8d078234` and the `policy:` one `6509cdac` before this unit
  (PINNED, `docs_leg.py --fingerprints` at `d06e2a65d`); the second hashes `allowed` and `default`
  alone, as `read_policy_usage` in `tools/govkit/docs_leg.py` reads it, so the summary moves it not; the builder
  re-reads both at build time.
- **AC8** — When `python tools/policy/policy.py get mailbox.reads` runs in a repository whose policy
  file sets no value, it prints `every-item`; after `policy.py lists --write`
  `tools/policy/unsummarised-keys.txt` no longer names `mailbox.reads`; and `python
  tools/policy/policy.py mirror --check` prints `policy: mirror fresh`.
  Red when: the row is still unsummarised, or the mirror carries the old catalogue blob.
- **AC9** — When `python tools/loop/loop_transition.py --fixture --plant mail-argv` runs, it prints
  `loop: fixture · mail-argv · held`: the guard's call of `read_mail_rows` still records the argv
  `[<bash>, <driver>, "--mail", "read", <slug>]`, with no `--local`.
  Red when: the new keyword leaks `--local` into the guard's read.
  fixture: `mail-argv` is `KICK-dKeptSession-36`'s plant, landed before this unit.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `routed-commits selftest` · `policy check` · `help reference pages` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `docs` · `loop position fixtures` · `loop transition record` · `loop placement fixtures` · `loop claim fixtures` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC3 AC4 AC5 AC6 · the five `--plant` cases, `mail-open` staged red by the interrupt left `unarmed` · the `loop position fixtures` row's `plants=<n>` token rises by five, 32 to 37
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 · the `mail-boundary` plant, read from `--list`, staged red by the step run with no crossing · `FLOOR_ASSERTIONS` rises by one, 441 to 442

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
- rev-6 · 2026-11-23 · §1 · S1 to S8 · §3 · §4 · §5 · AC1 to AC9 · §7 · §10 · re-grounded at
  `d06e2a65d` by `2026-11-22-prompt-KICK-dKeptSession-10-reground-brief`, units 36, 39, 51, 27 and
  24 read as landed: S2 reads through `read_mail_rows`, unit 5's landed launch, which gains a
  `local` keyword, rather than a second launcher, and keeps the `open` rows as `--open` does; S1's
  step takes `[--local]`, which unit 21 passes, prints only `interrupt — mailbox` lines and names
  each failure; S3 and AC6 print a refused key as an interrupt line, no loop module printing a
  `NOTE` line, its default read from the catalogue; S8 adds the `policy:mailbox.reads` anchor and
  drains its undocumented row, a sentence in `help/orientation-card.md`, the engine's docstring and
  the loop README; the plants reuse `render_fixture_mail` and `write_fixture_gov_ref`, which gains
  `remote`, and the card-store stub gains one branch; the plant token is 32 to 37 and the floor 441
  to 442; S7 re-renders the policy mirror; AC9 holds the guard's argv; three loop legs join §7.

## 10. Reuse audit

The seams extended are the landed engine's mailbox interrupt in `tools/loop/position.py#derive_interrupts`,
printed `unarmed`, armed here behind its own flag; the loop kit's one launch of the driver's mail
read, `tools/loop/loop_transition.py#read_mail_rows`, which gains `local`; the loop kit's
in-process policy read, `tools/loop/loop_parents.py#read_policy_kit`; the fixture planters
`tools/loop/loop_transition.py#render_fixture_mail` and `tools/loop/placement.py#write_fixture_gov_ref`,
which gains `remote`; the card-store fixture's one stub engine; and `KICK-dKeptSession-13`'s boundary
verb, `skills/session-kickoff/manifest-check.sh#run_card_boundary`, inside which the step runs,
shaped as its sibling `run_item_boundary`. The one mail reader is unit 5's `read_mailbox`, reached
through the driver's `--mail read`. `python tools/codebase-map/reuse_lookup.py "read the mailbox at
each item boundary of the position engine"`, re-run at `d06e2a65d`, ranked `read_text`, `read`,
`read_bytes`, `read_rows`, `read_git` and `read_memory_tree` by name stem, `read_policy_kit` the one
it names that S3 takes; none reads a mailbox or an item boundary, and `git grep -n 'mail", "read"' -- tools/loop` finds `read_mail_rows` alone, the
seam S2 takes. Scout B's disagreement 1, the parent naming dWellOiledMachine, holds against the
landed parent text and is §8 F3, filed as TOOL-dDeclaredLoop-103.

Recall terms used: mailbox.reads every-item intake interrupt position engine item boundary transitions-only amendments derive_item_boundary unarmed read_mail_rows run_card_boundary
