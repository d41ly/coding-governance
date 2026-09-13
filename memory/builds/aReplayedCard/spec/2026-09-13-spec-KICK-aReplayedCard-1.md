# KICK-aReplayedCard-1 — `manifest-check.sh --card` writes and replays the session's orientation card

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams kickoff · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Give every session one on-disk orientation artifact, written once at session start from facts a
script can derive and replayed verbatim after a compaction or a resume. The writer is a verb on the
checker the kickoff engine already resolves, so the card costs no new file, no new hook process and
no manifest bytes.

## 2. Scope (IN)

- **S1** A `--card` verb on `skills/session-kickoff/manifest-check.sh`, dispatched BEFORE the
  catch-all that reads any other argument as a manifest path, and AFTER the repo probe, because the
  card needs a repository. It writes `<git-common-dir>/orientation/<session_id>.md` and prints the
  same bytes to stdout. Observed by AC1 and AC2.
- **S2** The `session_id` is read from the JSON the SessionStart hook hands on stdin, else from
  `--session <sid>`. Neither present is a refusal naming both channels, never a card under a guessed
  id. Observed by AC3.
- **S3** The card's startup fields are DERIVED, never authored, and are exactly: the header line
  naming the session id, the ISO time and this script; `node —` from the registry; `tree —` with the
  toplevel, whether it is the primary tree or a worktree, the branch, HEAD as `BASE`, and clean or
  dirty with the dirty count; `ff —` for the default-branch fast-forward the engine's Step 1 makes,
  or `skipped:` with why; `worktrees —` with the count; `live —` with the non-terminal build count
  read from the generated `LIVE.md` at the memory root the conf declares; `recent —` with five
  one-line subjects; and the closing `READY — none yet`. Observed by AC2.
- **S4** The `node —` cell is resolved by matching `$USERNAME` against the Machine/user cell of the
  registry table in the file `--registry <path>` names, never row-wide. No unique cell match prints
  `node — UNKNOWN` with the user name, and the card still writes. Observed by AC4.
- **S5** `--card --replay` prints the stored card unchanged and appends one `now —` line carrying
  HEAD, the branch and clean or dirty, computed at replay and never stored. A missing card under
  replay writes a fresh one and says so on the first line. Observed by AC5.
- **S6** `--card --path` prints the card's path and exits 0 before any other work, the print-only
  shape `--locations` already has. Observed by AC6.
- **S7** The card is LF, capped at 8192 bytes by one constant in the verb, and the constant is the
  same one `KICK-aReplayedCard-2`'s append refuses against. A startup card over the cap is a
  refusal, because every startup field is bounded and an overflow means a derivation went wrong.
  Observed by AC7.
- **S8** The verb runs NO manifest audit. The audit stays in the engine's Step 2b, where it costs a
  kickoff and not every session start. NOT OBSERVED by a criterion here: the absence of a call is
  read from the source, and the design record's verdict 35 carries the measurement that decided it.
- **S9** Every `fail` call site the verb adds is armed in `manifest-check.test.sh` and the
  `ARMS_FLOORS` entry for this script moves in the same commit. Observed by AC8.

## 3. Non-goals (OUT)

- No `--append`, `--check` or citation logic; that is `KICK-aReplayedCard-2`.
- No `--waive` verb and no waiver line. Owner decision 2, prompt record.
- No hook wiring and no settings edit; `TOOL-aReplayedCard-2` wires the verb.
- No reading of the card by the engine; `KICK-aReplayedCard-3` teaches Step 1 to consume it.
- No manifest audit at session start, per S8.
- No signed or hashed artifact and no TTL sweep. The design record's section 6 rejects both.

### Edges

- **hands-off** `KICK-aReplayedCard-2` — the file, the cap constant and the `READY — none yet`
  sentinel it appends against and replaces.
- **hands-off** `TOOL-aReplayedCard-1` — the `READY —` line grammar and the `tree —` cell the deny
  compares to the payload's toplevel.
- **hands-off** `TOOL-aReplayedCard-2` — the two SessionStart invocations that call this verb.
- **hands-off** `KICK-aReplayedCard-3` — the card header line Step 1 recognises in context.
- **consumes-from** external — `git rev-parse --git-common-dir`, which resolves the primary tree's
  `.git` from any worktree; without it the card has no home shared across worktrees.

## 4. Design

### Data model

One file per session under the git common dir, so every worktree of one repository shares the
directory and a card names the tree it was written in. The `tree —` cell is what tells a card from
a sibling worktree apart, and the deny compares it rather than the path.

```
orientation — <session_id> · written <iso> · by manifest-check.sh --card
node — <tag> · <machine/user>
tree — <toplevel> · primary|worktree · branch <b> · BASE <sha> · clean|dirty <n>
ff — moved <old>..<new> | unchanged | skipped: <why>
worktrees — <n>
live — LIVE.md · <n> non-terminal builds
recent — <five subjects, one per line beneath>
READY — none yet
```

Every line is a factual statement. Imperative text injected by a hook reads to the model as an
instruction from nobody, which is a class the harness area of the design record names.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `CARD_CAP_BYTES` | shell constant | `manifest-check.sh` | screaming snake, like `MAX_MANIFEST_BYTES` |
| `render_card` | shell function | `manifest-check.sh` | leads with `render`, structure to text |
| `derive_node_tag` | shell function | `manifest-check.sh` | leads with `derive`, computed from the registry |
| `write_card` | shell function | `manifest-check.sh` | leads with `write`, persists the file |
| `print_replay` | shell function | `manifest-check.sh` | leads with `print`, stdout for a human |

### Migration

None. A repository with no card directory gains one on the first `--card`; nothing reads the
directory before it exists, and the common dir is untracked.

### Rollout

Dark until `TOOL-aReplayedCard-2` wires the invocations. The verb is callable by hand from the
commit that lands it, which is how AC1 through AC7 are observed before any hook exists.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | the verb dispatch, four functions, one constant |
| `skills/session-kickoff/manifest-check.test.sh` | arms for S2, S4, S5, S7; the assertion floor |
| `.memory-tree.conf` | `ARMS_FLOORS` for this script |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped; the script is in `watch:` |
| `memory/map/features/session-kickoff.md` | dossier refresh on touch |

### Alternatives rejected

**A separate `orientation-card.sh` beside the checker.** It needs a new `watch:` literal in a
manifest with 5 B of headroom, a new install-prefix row, and a second place the engine resolves a
script from. The checker already ships beside the engine and is already watched.

**Writing the card under the worktree's `.git` file.** A linked worktree's `.git` is a file, not a
directory, and `<git-common-dir>/recall/` and `<git-common-dir>/agent-cap/` already established the
common dir as this repo's per-session scratch home.

**Running the manifest audit in the card.** Measured 41–44 s on the loaded host in the design study;
the `--staged` and full checker runs already catch the drift at the commit and push boundaries.

## 5. Production-readiness checklist

- security — the card is written under the git common dir only, from a session id the harness
  supplied; a path segment in the id is refused rather than joined.
- perf / scale — one git batch, budgeted at ~1.6 s quiet and 5–6 s loaded per the design record's
  verdict 35; no manifest audit. AC2 records the wall.
- error / empty / loading states — no session id refuses; no registry match prints UNKNOWN; a
  missing card under replay is rewritten and announced.
- observability — the card IS the report; `--path` locates it.
- risks — a stale card from a previous session under the same id is overwritten at startup, which
  is the SessionStart `startup` matcher's job in `TOOL-aReplayedCard-2`.
- testing — arms in `manifest-check.test.sh`, staged RED before wiring.
- migration — none.
- user docs — the kit README states the verb family; `WIRE-INTO-PROJECT.md` is `TOOL-aReplayedCard-2`'s.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --card --session t1` runs from this
  worktree, a file exists under the directory `git rev-parse --git-common-dir` names, in an
  `orientation` subdirectory, named `t1.md`, and stdout equals its bytes.
  Red when: the verb falls into the manifest-path catch-all and the script reports the argument as
  a manifest that does not exist.
- **AC2** — When that card is read, it carries the `tree —` line with this worktree's toplevel and
  the word `worktree`, a `BASE` equal to `git rev-parse HEAD`, and ends with `READY — none yet`; the
  run's wall is recorded beside the observation.
  Red when: the BASE is read from a moving ref, or the cell says `primary` in a linked worktree.
  figure: DERIVED at observation from `git rev-parse HEAD` and `--show-toplevel`.
- **AC3** — When `--card` runs with neither stdin JSON nor `--session`, it exits non-zero naming
  both channels and writes nothing under `orientation/`.
  Red when: a card named after an empty string or a literal `null` appears.
- **AC4** — When `--card --registry` is pointed at a fixture registry whose Remote column repeats
  one user name on every row and whose Machine/user cell matches on exactly one, the card names that
  one row's tag; pointed at a fixture with no matching cell, it prints `node — UNKNOWN`.
  Red when: a row-wide match hits every row and the card names the first.
  fixture: two registry tables the self-test writes.
- **AC5** — When `--card --replay --session t1` runs after AC1, stdout is AC1's bytes followed by
  exactly one `now —` line, and the file on disk is byte-identical to before.
  Red when: the `now —` line is stored, so a second replay prints two.
- **AC6** — When `--card --path --session t1` runs, it prints one path and exits 0 without touching
  the file.
  Red when: the path verb writes a card as a side effect.
- **AC7** — When the self-test forces `CARD_CAP_BYTES` below the startup card's size, `--card`
  exits non-zero naming the cap and the overage, and leaves no file.
  Red when: a truncated card is written.
- **AC8** — When `python tools/memory-tree/check-arms.py --check` runs, this script's
  `ARMS_FLOORS` entry has moved by the number of `fail` sites added and the new arms are absent from
  `unarmed-branches.txt`.
  Red when: a `fail` site is added without its self-test assertion.

## 7. Gates

`manifest-check self-test` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `skills/session-kickoff/manifest-check.test.sh` · no session id on either channel · this script's `ARMS_FLOORS` entry and `FLOOR_ASSERTIONS`
New arm: `skills/session-kickoff/manifest-check.test.sh` · a registry whose Remote column repeats the user on every row · same floors
New arm: `skills/session-kickoff/manifest-check.test.sh` · `CARD_CAP_BYTES` forced under the startup size · same floors

The full bar is owed with `GATE_SELFTESTS=1`: kit work, and the manifest-check self-test is held.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is `skills/session-kickoff/manifest-check.sh` itself, which the design record's reader
and this run's `python tools/codebase-map/reuse_lookup.py "session orientation card written at
session start, replayed after compaction, commit denied until READY"` both returned as the
session-kickoff affordance seam, and whose `--locations` verb the dossier
`memory/map/features/session-kickoff.md` names as the shape to reuse whenever a script and a
document need one list. The card home reuses the common-dir convention `<git-common-dir>/recall/`
and `<git-common-dir>/agent-cap/` already established. The probe reported the shell layer unscanned,
so the seam was confirmed by reading the script's verb dispatch at lines 60–67 and 74–79.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
