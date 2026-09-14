# KICK-aReplayedCard-1 — `manifest-check.sh --card` writes and replays the session's orientation card

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams kickoff · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-build-KICK-aReplayedCard-1-1-acceptance-ledger.md](../build/2026-09-14-build-KICK-aReplayedCard-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-KICK-aReplayedCard-1-brief.md](../prompts/2026-09-14-prompt-KICK-aReplayedCard-1-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Give every session one on-disk orientation artifact, written once at session start from facts a
script can derive and replayed verbatim after a compaction or a resume. The writer is a verb on the
checker the kickoff engine already resolves, so the card costs no new file, no new hook process and
no manifest bytes beyond one audit-block key.

## 2. Scope (IN)

- **S1** A `--card --write` verb on `skills/session-kickoff/manifest-check.sh`, dispatched BEFORE the
  catch-all that reads any other argument as a manifest path, and AFTER the repo probe and the
  manifest resolution, because the card needs a repository and reads one key from the manifest. It
  writes `<git-common-dir>/orientation/<session_id>.md` and prints the same bytes to stdout.
  Observed by AC1 and AC2.
- **S2** The `session_id` is read from the JSON the SessionStart hook hands on stdin, else from
  `--session <sid>`. Neither present is a refusal naming both channels, never a card under a guessed
  id. A `session_id` carrying a path separator or `..` is refused, never joined. Observed by AC3.
- **S3** The card's startup fields are DERIVED, never authored, and are exactly: the header line
  naming the session id, the ISO time and this script; `node —` from the registry; `tree —` with the
  toplevel, whether it is the primary tree or a worktree, the branch, HEAD as `BASE`, and clean or
  dirty with the dirty count; `worktrees —` with the count from `git worktree list`; `live —` with
  the non-terminal build count read as the table rows of the generated `LIVE.md` under the memory
  root `.memory-tree.conf` declares, or `live — skipped: <why>` when that conf or that file is
  absent, never a refusal; `recent —` with five subjects from `git log --oneline -5`; and the closing
  `READY — none yet`. The toplevel is written in ONE declared spelling: the bytes
  `git rev-parse --show-toplevel` prints, forward-slash with a drive letter on Windows, before the
  script's own `pwd` normalisation. Observed by AC2 and AC10.
- **S4** The `node —` cell is resolved from the registry file the manifest's audit block names in a
  `registry:` key, which this unit adds to `memory/guides/SESSION-KICKOFF.md` as `registry: AGENTS.md`
  and to the seed `skills/session-kickoff/MANIFEST-TEMPLATE.md` as `registry: {{REGISTRY_PATH}}`,
  bumping `KIT_MANIFEST_VERSION` and the template's `kickoff-manifest:` marker together and
  extending the runbook's retrofit list, the way `check-script:` arrived at v1.1 and
  `last-body-change:` at v1.3; an absent manifest or key prints `node — UNKNOWN: no registry`. The reader takes the FIRST table
  under a `## Node registry` heading, strips backticks from cells, and matches `$USERNAME` against
  the Machine/user cell by equality or by the prefix `$USERNAME @`, never row-wide. No unique match
  prints `node — UNKNOWN` with the user name, and the card still writes. Observed by AC4.
- **S5** `--card --replay` prints the stored card unchanged and appends one `now —` line carrying
  HEAD, the branch and clean or dirty, computed at replay and never stored. A missing card under
  replay writes a fresh one by S3's derivation, node cell included, whose header line names
  `--card --replay` as the writer — the one byte-level fact that tells a session which started
  before the writer was wired from one whose startup ran it, and the fact
  `TOOL-aReplayedCard-1` allows on — and says so on the first line. Observed by AC5.
- **S6** `--card --path` prints the card's path and exits 0 before any other work, the print-only
  shape `--locations` already has. Observed by AC6.
- **S7** The card is LF, capped at 8192 bytes by one constant in the verb, and the constant is the
  same one `KICK-aReplayedCard-2`'s append refuses against. A startup card over the cap is a
  refusal, because every startup field is bounded and an overflow means a derivation went wrong.
  Observed by AC7.
- **S8** The verb runs NO manifest audit and NO fetch: it never contacts a remote and never moves a
  ref. The audit stays in the engine's Step 2b and the fast-forward stays in its Step 1, where each
  costs a kickoff and not every session start. Observed by AC9.
- **S9** Every refusal the verb adds uses the script's existing `MANIFEST env ERROR — …` shape with
  exit 2, not the numbered `fail` recorder, which is reached only after a manifest resolves and
  which `check-arms.py` counts; so `ARMS_FLOORS` does not move. Every refusal is armed in
  `manifest-check.test.sh` and `FLOOR_ASSERTIONS` there moves by the arms added, in the same commit.
  Observed by AC8.

## 3. Non-goals (OUT)

- No `--append`, `--check` or citation logic; that is `KICK-aReplayedCard-2`.
- No `--waive` verb and no waiver line. Owner decision 2, prompt record.
- No hook wiring and no settings edit; `TOOL-aReplayedCard-2` wires the verb.
- No reading of the card by the engine; `KICK-aReplayedCard-3` teaches Step 1 to consume it.
- No manifest audit and no fetch at session start, per S8; the card carries no `ff —` cell.
- No `--registry` flag: the registry is the manifest's to name, so a verbatim fragment can wire the
  verb in any adopter.
- No signed or hashed artifact and no TTL sweep. The design record's section 6 rejects both.
- No dependency on the memory-tree kit: the `live —` cell is conditional on the conf, and its
  absence is a `skipped:` value.

### Edges

- **hands-off** `KICK-aReplayedCard-2` — the file, the cap constant and the `READY — none yet`
  sentinel it appends against and replaces.
- **hands-off** `TOOL-aReplayedCard-1` — the `READY —` line grammar, the sentinel bytes, and the
  `tree —` cell's declared spelling the deny normalises before comparing.
- **hands-off** `TOOL-aReplayedCard-2` — the two SessionStart invocations that call this verb.
- **hands-off** `KICK-aReplayedCard-3` — the card header line Step 1 recognises in context.
- **hands-off** `TOOL-aReplayedCard-5` — the card an Explore-typed arm reads at Step 1, once wired.
- **consumes-from** `TOOL-aReplayedCard-4` — the manifest bytes the eviction frees; the `registry:`
  key this unit adds does not fit the 3 B of headroom at base.
- **consumes-from** external — `git rev-parse --git-common-dir`, which resolves the primary tree's
  `.git` from any worktree; without it the card has no home shared across worktrees.

## 4. Design

### Data model

One file per session under the git common dir, so every worktree of one repository shares the
directory and a card names the tree it was written in. The `tree —` cell is what tells a card from
a sibling worktree apart, and the deny compares it, after normalising both sides, rather than the
path. `KICK-aReplayedCard-2`'s append rewrites the cell to the tree the kickoff ran in; this verb
writes it once.

```
orientation — <session_id> · written <iso> · by manifest-check.sh --card --write | --card --replay
node — <tag> · <machine/user>          | node — UNKNOWN: <why>
tree — <toplevel> · primary|worktree · branch <b> · BASE <sha> · clean|dirty <n>
worktrees — <n>
live — LIVE.md · <n> non-terminal builds | live — skipped: <why>
recent — <five subjects, one per line beneath>
READY — none yet
```

Every line is a factual statement. Imperative text injected by a hook reads to the model as an
instruction from nobody, which is a class the harness area of the design record names. The
sentinel `READY — none yet` is spelled here once; `TOOL-aReplayedCard-1` reads the writer's own
output in its self-test rather than restating the bytes.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `CARD_CAP_BYTES` | shell constant | `manifest-check.sh` | screaming snake, like `MAX_MANIFEST_BYTES` |
| `render_card` | shell function | `manifest-check.sh` | leads with `render`, structure to text |
| `derive_node_tag` | shell function | `manifest-check.sh` | leads with `derive`, computed from the registry |
| `write_card` | shell function | `manifest-check.sh` | leads with `write`, persists the file |
| `print_replay` | shell function | `manifest-check.sh` | leads with `print`, stdout for a human |
| `registry:` | manifest audit-block key | `SESSION-KICKOFF.md` | kebab, beside `check-script:` |

### Migration

A repository with no card directory gains one on the first `--card --write`; nothing reads the
directory before it exists, and the common dir is untracked. The manifest gains one audit-block
key; the checker tolerates keys beyond the four it requires, as `check-script:` already shows.

### Rollout

Dark until `TOOL-aReplayedCard-2` wires the invocations. The verb is callable by hand from the
commit that lands it, which is how AC1 through AC10 are observed before any hook exists — every
one of them in the self-test's scratch clone of this repository, never in this worktree, because
the card home is the common dir every worktree on the node shares and a card left there is a
fixture a sibling session trips on; AC11 asserts the clone left nothing behind.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | the verb dispatch, four functions, one constant, the header's verb table |
| `skills/session-kickoff/manifest-check.test.sh` | arms for S2, S3, S4, S5, S7, S8; `FLOOR_ASSERTIONS` |
| `memory/guides/SESSION-KICKOFF.md` | `registry: AGENTS.md` in the audit block; `last-audit` re-stamped |
| `skills/session-kickoff/MANIFEST-TEMPLATE.md` | `registry: {{REGISTRY_PATH}}` in the seed's audit block; the marker bumped |
| `skills/session-kickoff/manifest-check.sh` | `KIT_MANIFEST_VERSION` bumped with the marker; the seed arm asserts the key |
| `WIRE-INTO-PROJECT.md` | the `registry:` key in the manifest recipe and in the §4 retrofit list |

### Alternatives rejected

**A separate `orientation-card.sh` beside the checker.** It needs a new `watch:` literal in a
manifest with 3 B of headroom, a new install-prefix row, and a second place the engine resolves a
script from. The checker already ships beside the engine and is already watched.

**Writing the card under the worktree's `.git` file.** A linked worktree's `.git` is a file, not a
directory, and `<git-common-dir>/recall/` and `<git-common-dir>/agent-cap/` already established the
common dir as this repo's per-session scratch home.

**Running the manifest audit or a fetch in the card.** The audit measured 41–44 s on the loaded
host in the design study, and the `--staged` and full checker runs already catch the drift at the
commit and push boundaries. A fetch mutates local refs from a hook nobody asked, inside a hook
timeout; the engine's Step 1 owns it.

**A `--registry` flag on the fragment.** A fragment is deployed verbatim, so a per-adopter value on
its command line is a literal the adopter must edit; the manifest is the project layer and already
carries per-project values.

**A `ff —` cell.** Its only honest value at session start was `skipped:`; a cell with one value
carries no information.

## 5. Production-readiness checklist

- security — the card is written under the git common dir only, from a session id the harness
  supplied; a separator or `..` in the id is refused rather than joined.
- perf / scale — one git batch with no network, budgeted at ~1.6 s quiet and 5–6 s loaded per the
  design record's verdict 35; no manifest audit. AC2 records the wall.
- error / empty / loading states — no session id refuses; no registry key or no match prints
  UNKNOWN; no conf or no LIVE.md prints `live — skipped:`; a missing card under replay is rewritten
  and announced.
- observability — the card IS the report; `--path` locates it.
- risks — a stale card from a previous session under the same id is overwritten at startup, which
  is the SessionStart `startup` matcher's job in `TOOL-aReplayedCard-2`.
- testing — arms in `manifest-check.test.sh`, staged RED before wiring.
- migration — one manifest key.
- user docs — the script's own header states the verb family; `WIRE-INTO-PROJECT.md` carries the
  manifest key; the kit ships no README and this unit adds none.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --card --write --session t1` runs
  in the self-test's scratch clone of this repository, a file exists under the directory
  `git rev-parse --git-common-dir` names there, in an `orientation` subdirectory, named `t1.md`,
  and stdout equals its bytes.
  Red when: the verb falls into the manifest-path catch-all and the script reports the argument as
  a manifest that does not exist.
- **AC2** — When that card is read, it carries the `tree —` line with the bytes
  `git rev-parse --show-toplevel` prints and the word `worktree`, a `BASE` equal to
  `git rev-parse HEAD`, a `worktrees —` count equal to the line count of `git worktree list`, a
  `live —` count equal to the table rows of `memory/LIVE.md` minus its header, a `recent —` block
  equal to `git log --oneline -5`, and ends with `READY — none yet`; the run's wall is recorded
  beside the observation.
  Red when: the BASE is read from a moving ref, the cell says `primary` in a linked worktree, or
  the toplevel is written in the `pwd` spelling.
  figure: DERIVED at observation from the four git commands and the `LIVE.md` row count.
- **AC3** — When `--card --write` runs with neither stdin JSON nor `--session`, or with a session id
  containing `/` or `..`, it exits 2 naming the channel or the offending id and writes nothing under
  `orientation/`.
  Red when: a card named after an empty string, a literal `null` or a path appears.
- **AC4** — When `--card --write` runs in the scratch clone with the manifest naming
  `registry: AGENTS.md`, the card reads `node — a · daily-agent` on this node; when the self-test points the key at a
  fixture registry whose Remote column repeats one user name on every row and whose Machine/user
  cell matches on exactly one, the card names that row's tag; pointed at a fixture with no matching
  cell, it prints `node — UNKNOWN`; with the key absent, `node — UNKNOWN: no registry`.
  Red when: a row-wide match hits every row, the charter's second registry-shaped table wins, or a
  backticked cell fails to match.
  fixture: the real `AGENTS.md` at HEAD inside the clone, and two registry tables the self-test
  writes.
- **AC5** — When `--card --replay --session t1` runs after AC1, stdout is AC1's bytes followed by
  exactly one `now —` line, and the file on disk is byte-identical to before; when it runs for a
  session with no card, the card it writes carries a `node —` tag, not `UNKNOWN`, and its header
  line names `--card --replay` as the writer.
  Red when: the `now —` line is stored, so a second replay prints two; the replay-written card
  skips the registry; or it claims `--card --write` as its writer and the deny binds a session
  that started before the wiring.
- **AC6** — When `--card --path --session t1` runs, it prints one path and exits 0 without touching
  the file.
  Red when: the path verb writes a card as a side effect.
- **AC7** — When the self-test forces `CARD_CAP_BYTES` below the startup card's size, `--card --write`
  exits 2 naming the cap and the overage, and leaves no file.
  Red when: a truncated card is written.
- **AC8** — When `bash skills/session-kickoff/manifest-check.test.sh` runs, it prints `PASS` with
  an assertion count at or above the moved `FLOOR_ASSERTIONS`, and `check-arms.py --check` reports
  this script's floor unchanged.
  Red when: an arm is unreachable and the floor did not move, or a refusal was written as `fail`.
- **AC9** — When the self-test runs `--card --write` in a scratch repository whose remote is one
  commit ahead, `git rev-parse HEAD` and `git rev-parse origin/main` are unchanged afterwards and
  no `FETCH_HEAD` was written.
  Red when: the hook fetches or fast-forwards from session start.
- **AC10** — When the self-test runs `--card --write` in a scratch repository with no
  `.memory-tree.conf`, the exit is 0 and the card reads `live — skipped:` with the reason.
  Red when: an absent conf refuses the card, so every commit in that repository is denied.
- **AC11** — When this repository's real common dir is listed after the whole self-test, no
  `orientation/` entry the suite wrote is present, and the seed arm of the self-test asserts the
  template's audit block carries every key the card verb reads.
  Red when: a fixture card is left in the shared common dir, or a fresh adopter's seed lacks the
  key and every card it writes reads `UNKNOWN` with no version WARN.

## 7. Gates

`manifest-check self-test` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `skills/session-kickoff/manifest-check.test.sh` · no session id on either channel, and a path-shaped id · `FLOOR_ASSERTIONS`
New arm: `skills/session-kickoff/manifest-check.test.sh` · the real `AGENTS.md` at HEAD, and two fixture registries · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · `CARD_CAP_BYTES` forced under the startup size · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · a remote one commit ahead, refs unchanged after · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · no `.memory-tree.conf` in the tree · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · the shared common dir after the suite, and the seed's key set · same

The full bar is owed with `GATE_SELFTESTS=1`: kit work, and the manifest-check self-test is held.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §2 · §3 · §4 · §6 · §7 · S1 · S3 · S4 · S5 · S8 · S9 · AC2 · AC3 · AC4
  · AC5 · AC8 · AC9 · AC10 · folded the round-1 spec audit. The writer verb is `--card --write` so
  the two fragments carry distinct markers (H5); the toplevel is written in one declared spelling
  and the deny normalises (B4); the `ff —` cell is gone and the verb never fetches (H2); the
  registry comes from a manifest `registry:` key, first table under `## Node registry`, backticks
  stripped, prefix match (H3, B3, M4); `live —` has a `skipped:` value and the conf read is
  conditional (M2); the three unobserved cells joined AC2 (M2); refusals use the env-error shape
  and `ARMS_FLOORS` is dropped in favour of `FLOOR_ASSERTIONS` (M10); the user-docs row names the
  script header and the runbook (L1); a `consumes-from TOOL-aReplayedCard-4` edge for the manifest
  bytes the key needs.
- rev-3 · 2026-09-14 · §2 · §3 · §4 · §6 · §7 · S4 · AC1 · AC4 · AC11 · folded the round-2 spec
  audit. The `registry:` key rides a manifest format bump — seed template, `KIT_MANIFEST_VERSION`,
  marker and retrofit list together — so a fresh adopter's card resolves a node (M9); every
  criterion observes in a scratch clone and AC11 asserts the shared common dir is left clean, which
  is what lets `TOOL-aReplayedCard-1` allow an absent card without a bootstrap (round-2 B1); the
  headroom figure is the measured 3 B (L2); the append's cell rewrite is named in §4 (H4).
- rev-4 · 2026-09-14 · §2 · §4 · §6 · S5 · AC5 · folded the round-3 spec audit's exit: a card the
  replay writes fresh names `--card --replay` in its header, so the deny can tell a pre-wiring
  session from one that skipped its kickoff (round-3 B1).

## 10. Reuse audit

The seam is `skills/session-kickoff/manifest-check.sh` itself, which the design record's reader
and this run's `python tools/codebase-map/reuse_lookup.py "session orientation card written at
session start, replayed after compaction, commit denied until READY"` both returned as the
session-kickoff affordance seam, and whose `--locations` verb the dossier
`memory/map/features/session-kickoff.md` names as the shape to reuse whenever a script and a
document need one list. The card home reuses the common-dir convention `<git-common-dir>/recall/`
and `<git-common-dir>/agent-cap/` already established; the refusal shape reuses the script's
`MANIFEST env ERROR` form at its lines 72–73 and 112. The probe reported the shell layer
unscanned, so the seam was confirmed by reading the script's verb dispatch at lines 60–67 and
74–79 and its audit-block reader at lines 154 and 210–220.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
