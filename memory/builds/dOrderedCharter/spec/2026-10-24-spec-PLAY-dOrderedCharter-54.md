# PLAY-dOrderedCharter-54 — the card file's owner is live only while its transcript moves, and a dead owner's card is taken over

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 40 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-55 |
| [2026-10-24-build-PLAY-dOrderedCharter-54-deviation-541.md](../build/2026-10-24-build-PLAY-dOrderedCharter-54-deviation-541.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-54-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-54-promoted-fix-return.md) | research | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 39 at HIGH**, its item **H5**. `PLAY-dOrderedCharter-49` S54 makes
`write_card_file` refuse to overwrite a card file that "another live session" owns, but never defines
a live session, and no session-liveness predicate exists in the spec set or in `skills/`. Every session
ends, so the simplest build treats any other session id in the header as live, and a crashed session,
one that ended without cleanup, or a `/clear` successor then owns the tree's card file forever: every
later session skips the write and loads a dead session's build, unit and route at level 1, behind
one skip line. This unit defines liveness by the one signal every live session moves, its transcript,
records that transcript beside the owner's session id, and takes over a dead owner's card with a
printed line. It repairs unit 49 and is built right after it.

## 2. Scope (IN)

- **S1** — The owner line. `write_card_file` in `skills/session-kickoff/manifest-check.sh` writes,
  as the card file's second line, `card-owner — <session id> · <transcript path>`. The transcript path
  is the SessionStart payload's `transcript_path`, read by `read_session_id` (`:292`) from the same
  stdin JSON as `session_id`, with JSON's `\\` unescaped. A caller that passed `--session` and no
  payload records the literal `absent`. This supersedes unit 49 S54's unstated header shape.
  Observed by AC1.
- **S2** — Liveness. The owner named by an existing card file is live when its session id differs from
  the writer's, its transcript path is not `absent`, the file exists, and its modification time is
  within `CARD_OWNER_BOUND` seconds of now, a constant of the script set to 1800. Any other case is a
  dead owner: no owner line, an owner line of another shape, `absent`, a missing transcript, a stale
  one, or a modification time the script cannot read. This defines unit 49 S54's "another live
  session". Observed by AC2 and AC3.
- **S3** — The verdicts. A live owner keeps unit 49 S54's skip and its line. A dead owner's card file
  is overwritten, printing `card-file — took over: session <old id> (transcript <age>s old, or
  absent)`. The writer's own session id overwrites silently, as today. Observed by AC2 to AC4.
- **S4** — The fixtures, in `skills/session-kickoff/manifest-check.test.sh`: a live owner (a
  transcript touched now), a stale owner (a transcript dated two bounds back), an owner whose
  transcript is missing, an owner line of unit 49's id-only shape, and the writer's own id. Observed
  by AC2 to AC4.

## 3. Non-goals (OUT)

- The card file's content, envelope and import: units 8 and 43.
- A lock or lease file beside the card: the transcript is the signal, and a second record of
  liveness would be a fact twice.
- The unattended kit's lease, `check_pid_alive` (`tools/unattended/lib-unattended.sh:660`): an
  optional kit the kickoff engine may not depend on.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-49` — `write_card_file`'s owner refusal and its skip line (S54), which S1 to S3 give a liveness rule; without it there is no ownership to expire

## 4. Design

### Evidence

Read at `ce13efbe`. `read_session_id` (`skills/session-kickoff/manifest-check.sh:292`) reads the
SessionStart JSON once from stdin and takes `session_id` by `sed`; `--session` suppresses the read.
The payload's `transcript_path` is already read by `tools/hooks/format-guard.js:496` for the same
session's agents. The unattended kit grades a run's liveness by the newest of several clocks, the
session transcript among them (`resolve_transcript_path`, `tools/unattended/unattended.sh:8625`), and
treats a holder whose clocks stopped as stale; this unit takes the transcript term alone, since it is
the one signal both kits read and the only one the kickoff engine holds.

### Why the transcript

The CLI appends to a session's transcript on every turn, so its modification time moves exactly while
the session works and stops when it ends, crashes or is cleared. A process id would need the unattended
kit's image probe and is recycled; the orientation card under `<git-common-dir>/orientation/` moves
only on card writes, which a working session may not make for hours.

### Inventory

Minted: the owner line `card-owner —`, the constant `CARD_OWNER_BOUND`, and the line prefix
`card-file — took over:`. Naming cells: `lexicon naming predicates` grades the shell names.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`

### Rollout

Live at landing, order 40, after unit 49 at order 39. A card file written before this unit carries no
owner line and is taken over once, printing its line.

### Alternatives rejected

- **Any other session id is live**, the simplest reading of unit 49 S54: the finding.
- **The unattended kit's pid probe**: an optional kit, and a pid says nothing about a session that
  was cleared inside one process.
- **No ownership at all**: two live sessions in one tree overwrite each other's card, the case unit 49
  S54 exists for.

## 5. Production-readiness checklist

- security: the transcript path is stat'ed, never read or executed; the path is the harness's own
  payload field, and the owner line lives in a git-ignored file.
- perf / scale: one `stat` per card write.
- error / empty / loading states: an unreadable modification time reads as a dead owner, never as
  live; the takeover always prints.
- observability: the takeover line names the old owner and the transcript's age.
- risks: a live session idle past the bound loses its card to a new session in the same tree; its next
  card write sees the new owner live and skips, which is unit 49 S54's two-session outcome.
- testing: AC1 to AC4 in the kickoff engine's suite.
- migration: an owner line of the old shape is a dead owner, taken over once.
- user docs: the card file paragraph of `skills/session-kickoff/SKILL.md`, which unit 8 writes, gains
  one sentence on takeover.

## 6. Acceptance criteria

- **AC1** — When `write_card_file` runs from a SessionStart payload carrying `transcript_path`, the card
  file's second line is `card-owner —` with the session id and that path.
  Red when: the owner line omits the transcript, or a `--session` caller records a guessed path.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh --card --write < payload-s2.json`, session
  `s2`'s SessionStart payload, runs in a fixture worktree whose `orientation-card.md` is owned by session `s1`, its transcript touched
  now, `grep -c "card-owner — s1" orientation-card.md` still prints 1 and the output carries unit 49's
  `card-file — skipped:` line.
  Red when: a live owner's card is overwritten.
- **AC3** — When the owner's transcript is dated two bounds back, missing, or the owner line has the
  id-only shape, the second session's write overwrites the card and prints `card-file — took over:`.
  Red when: a dead owner's card is kept.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh --card --write < payload-s1.json`, session
  `s1`'s SessionStart payload, runs in a fixture worktree whose `orientation-card.md` `s1` owns, the file is rewritten, its
  `orientation —` line's `written` stamp moved, and the output carries neither `card-file — skipped:`
  nor `card-file — took over:`.
  Red when: a session is refused its own card.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 · the five owner fixtures, each failing case staged by treating any other session id as live · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 8's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What signal says a session is live, and for how long.** Options: (a) the transcript's
  modification time within 1800 seconds; (b) a recorded pid through the unattended kit's probe; (c)
  the stored orientation card's modification time. (b) adds a dependency on an optional kit and (c)
  moves only on card writes. 1800 seconds is the shorter of the two horizons a working session leaves
  between turns and a crashed one is mistaken for live. RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 39 (HIGH, item H5).

## 10. Reuse audit

The seam extended is `write_card_file` and `read_session_id` in `skills/session-kickoff/manifest-check.sh`,
the payload parse widened by one field; the liveness signal is the session transcript, the term
`resolve_transcript_path` (`tools/unattended/unattended.sh:8625`) already grades for a run, read here
from the payload rather than derived. `python tools/codebase-map/reuse_lookup.py "decide whether
another session that owns a file is still alive"` ranked `corpus_files`, `extract_session`,
`owners_of` and `resolve_session_tree` by name stem, none a liveness predicate the kickoff engine may
import, so no existing seam fits the predicate itself. The recall query returned
TOOL-dDerivedDocket-61, the run clock whose transcript term this unit takes, and TOOL-aWokenSentinel-1.

Recall terms used: `python tools/memory-recall/query.py "how is a stale lease or dead session owner detected and taken over" --terms "lease liveness pid alive transcript stale bound takeover session owner card dead"`
