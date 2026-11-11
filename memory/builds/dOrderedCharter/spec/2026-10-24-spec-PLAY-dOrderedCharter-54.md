# PLAY-dOrderedCharter-54 — the card file's owner is live only while its transcript moves, and a dead owner's card is taken over

**Status:** CLOSED · rev-3 · 2026-11-11 · node d · Tier-2 · base ce13efbe · streams playbook · order 40 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-55 |
| [2026-10-24-build-PLAY-dOrderedCharter-54-deviation-541.md](../build/2026-10-24-build-PLAY-dOrderedCharter-54-deviation-541.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-54-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-54-promoted-fix-return.md) | research | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 |
| [2026-11-02-build-PLAY-dOrderedCharter-54-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-54-ledger.md) | journal | — |
| [2026-11-11-build-PLAY-dOrderedCharter-54-1-builder-return.md](../build/2026-11-11-build-PLAY-dOrderedCharter-54-1-builder-return.md) | journal | — |
| [2026-11-11-build-PLAY-dOrderedCharter-54-deviation-542.md](../build/2026-11-11-build-PLAY-dOrderedCharter-54-deviation-542.md) | deviation | — |
| [2026-11-11-build-PLAY-dOrderedCharter-54-deviation-543.md](../build/2026-11-11-build-PLAY-dOrderedCharter-54-deviation-543.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-55 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-54-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-54-build-brief.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-55 |
| [2026-11-10-prompt-PLAY-dOrderedCharter-54-1-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-54-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-54-precheck-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-54-precheck-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 39 at HIGH**, its item **H5**. `PLAY-dOrderedCharter-49` S54 makes
`write_card_file` skip a card file that "another live session" owns, but never defines a live
session, and no session-liveness predicate exists in the spec set or in `skills/`. Every session
ends, so the simplest build treats any other session id on the owner line as live. A crashed session,
one that ended without cleanup, or a `/clear` successor's predecessor then owns the tree's card file
forever: every later session skips the write and loads a dead session's build, unit and route at
level 1, behind one skip line. This unit defines liveness by the one signal every working session
moves, its transcript, records that transcript on the owner line unit 49 writes, and takes over a dead
owner's card, or a cleared predecessor's, with a printed line. It repairs unit 49 and is built right
after it.

## 2. Scope (IN)

- **S1** — The capture. `skills/session-kickoff/manifest-check.sh#read_session_id` takes two more
  fields from the payload it already holds in its `payload` variable, each by one `[[ =~ ]]` match as
  it takes `session_id` and `cwd`: `transcript_path` into `CARD_TRANSCRIPT`, JSON's escaped
  backslash read as `/` exactly as `CARD_CWD` is, and `source` into `CARD_SOURCE`. Stdin is never read
  a second time. A caller with no payload leaves both empty. Observed by AC1.
- **S2** — The owner line. Unit 49 S54's second line, `card-owner — <session id>`, gains one field and
  reads `card-owner — <session id> · <transcript>`. The transcript is `CARD_TRANSCRIPT` when it is set.
  Otherwise, when the card file's own second line already names the writer's session id with a
  transcript, that transcript is kept. Otherwise the field is the literal `absent`. Observed by AC1
  and AC2.
- **S3** — Liveness. An owner named by an existing card file is live when all of these hold: its
  second line has the S2 shape, its session id differs from the writer's, its transcript is not
  `absent`, the transcript is a file, `stat -c %Y` dates it, and `$EPOCHSECONDS` less that time is at
  most `CARD_OWNER_BOUND`. That constant is set once in the script to 1800 (section 8 F2). Every other
  case is a dead owner: no owner line, unit 49's id-only shape, `absent`, a missing transcript, one
  older than the bound, or a time `stat` cannot read. This defines unit 49 S54's "another live
  session". Observed by AC3 and AC4.
- **S4** — The verdicts, in this order. With no card file, the write is silent, as today. An owner line
  naming the writer's own session id is overwritten silently. A writer whose `CARD_SOURCE` is `clear`
  takes over whatever the owner (section 8 F5). A live owner keeps unit 49 S54's skip and its line
  `card-file — skipped: another live session <sid> owns this tree`. A dead owner's card is
  overwritten. A takeover prints one line, only after the rename lands:
  `card-file — took over: session <old id> · <reason>`. The old id reads `none` when the second line
  is no owner line. The reason is `source clear`, or `transcript <n>s old` for a dated transcript over
  the bound, or `transcript absent` otherwise. A write that fails after the verdict prints
  `write_card_file`'s existing `card-file — skipped:` line in its place. Observed by AC3 to AC6.
- **S5** — The fixtures, in `skills/session-kickoff/manifest-check.test.sh`: one per criterion AC1 to
  AC6, each built as section 6's fixture states. Two arms already in the file move with S2. The card
  file arm's `check_card_file`, which unit 49 extends with the owner line, expects ` · absent` after
  the id, since its payload carries no `transcript_path`. Unit 49's AC45 arm gives its first session a
  transcript touched at the arm's start, when it writes with none, since an owner with no transcript
  is dead from this unit on. Observed by AC1 to AC6, which these fixtures re-observe.
- **S6** — The comment block above `write_card_file` states the owner rule, the bound, and what it
  does not check (section 5). NOT OBSERVED: it is prose for the next reader, which no command grades.

## 3. Non-goals (OUT)

- The card file's content, envelope and import: units 8 and 43, both CLOSED.
- A lock or lease file beside the card: the transcript is the signal, and a second record of
  liveness would be a fact twice.
- The unattended kit's lease and clocks, `tools/unattended/lib-unattended.sh#check_pid_alive` and
  `tools/unattended/unattended.sh#derive_last_move`: an optional kit the kickoff engine may not
  depend on.
- A session's sub-agent transcripts as a liveness term (section 8 F3).
- A help page for the card file. None exists at HEAD, since unit 8 shipped none; a page is a document
  unit of its own (`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`), the follow-up section 8 F6 names.
- `TOOL-dPlacedRequest-2` S7 and `KICK-dKeptSession-15` S3, DEFERRED in other builds, read the
  payload's `transcript_path` and `source`. `CARD_TRANSCRIPT` and `CARD_SOURCE` are the one capture
  for them to read rather than a second, and this unit edits neither spec.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-49` — `write_card_file`'s owner line and its skip line (S54), which S2 to S4 extend with a transcript and a liveness rule; without it there is no ownership to expire

## 4. Design

### Evidence

Re-read at `95a63d8ab`, against unit 49's rev-8.

- `skills/session-kickoff/manifest-check.sh#read_session_id` reads stdin once into `payload`, skipped
  when the verb is `--append`, when `--session` is given, or when stdin is a terminal. It takes
  `session_id` and `cwd` by `[[ =~ ]]` match, never `sed`, and stores `cwd` in `CARD_CWD` with
  `${…//\\\\//}`, the unescape S1 repeats.
- `skills/session-kickoff/manifest-check.sh#write_card_file` is in the tree, built by unit 8. It renders
  the stored card through `skills/session-kickoff/manifest-check.sh#render_envelope_sh` into a temp
  beside the card file and renames it into place, and every failure prints one `card-file — skipped:`
  line and returns 0. `render_envelope_sh` is a byte-identical copy of the gov lib's `envelope.sh`,
  held by a parity gate, so the owner line reaches the file through the body unit 49 hands it, never
  through an edit to that copy.
- Unit 49 rev-8 S54 still builds the owner line `card-owner — <session id>` and the skip line, its
  AC45 observing two session ids in one scratch tree. Its §3 hands this unit "S54's owner liveness and
  takeover". It is order 39 and this unit order 40.
- `.claude/settings.json` runs `--card --write` on the SessionStart matcher `startup|clear` and
  `--card --replay` on `resume|compact`, each with the payload on stdin. The kickoff's
  `--card --append`, which `skills/session-kickoff/SKILL.md` has the session run, passes
  `--session <sid>` and no payload. Under rev-2's S1 that append recorded `absent` and made every
  kicked-off card dead; S2's kept transcript is the repair (section 8 F4).
- The matcher values are the payload's `source` values. No reader in the tree captures the field
  today, so its presence in the payload is UNVERIFIED here. A payload without it leaves
  `CARD_SOURCE` empty, and the transcript rule alone decides.
- `tools/hooks/format-guard.js` reads the payload's `transcript_path` for the same session's agents.
  `tools/unattended/unattended.sh#derive_last_move` dates a session transcript with
  `stat -c %Y -- <path>` and reads an empty or non-numeric answer as a dead probe. S3 takes that
  term's form for one file.
- `skills/session-kickoff/manifest-check.sh#render_health_cell` reads the clock as `$EPOCHSECONDS`, so
  the script's bash floor already admits it.
- `tools/gate-lint/sh_hygiene.py#check_spawn_substitution` classes a `$( )` by its first word; a
  `stat` capture is no class, so the spawn-idioms leg finds no new site.
- `tools/playbook/instruction_units.py#check_envelope` reads only `[…]` envelope lines of the
  untracked card file, so a second line inside the envelope keeps it green.
- A reader of the owner line at HEAD: none outside `memory/`, by `git grep -n "card-owner" -- ':!memory'`
  (DERIVED at `95a63d8ab`).
- The legs the files touched trip: `manifest-check self-test`, `scratch-guard self-test` and
  `lexicon naming predicates` for both, and `policy fixtures` for the script
  (DERIVED by `python tools/check-spec-tokens.py --legs-for` at `95a63d8ab`).
- This repo's unattended bound, `RESUME_STALE_BOUND` in `.unattended.conf`, is 5400 seconds (KEYED).
- The card bound, 1800 seconds (PINNED by section 8 F2, 2026-10-24, re-confirmed 2026-11-10).

### Why the transcript

The CLI appends to a session's transcript on every turn, so its modification time moves while the
session works and stops when it ends, crashes or is cleared. A process id would need the unattended
kit's image probe and is recycled. The stored card under `<git-common-dir>/orientation/` moves only
on card writes, which a working session may not make for hours.

### Inventory

Minted: the owner line's transcript field, the shell variables `CARD_TRANSCRIPT` and `CARD_SOURCE`,
the constant `CARD_OWNER_BOUND`, and the line prefix `card-file — took over:`. No function is minted.
The variables and the constant are graded by no cell, since the naming lexicon declares no
`sh.constant` cell.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`

### Rollout

Live at landing, order 40, after unit 49 at order 39. A card file unit 49 wrote carries the id-only
owner line, and the first write by another session takes it over once, printing its line. A card file
whose owner is the writer is rewritten with the new field silently.

### Alternatives rejected

- **Any other session id is live**, the simplest reading of unit 49 S54: the finding.
- **The unattended kit's pid probe**: an optional kit, and a pid says nothing about a session that
  was cleared inside one process.
- **No ownership at all**: two live sessions in one tree overwrite each other's card, the case unit 49
  S54 exists for.

## 5. Production-readiness checklist

- security: the transcript path is stat'ed, never read or executed; the takeover line prints the old
  id, which matches `[A-Za-z0-9][A-Za-z0-9._-]*` or reads `none`, and never the path; the owner line
  lives in a git-ignored file.
- perf / scale: at most one `stat` fork per card write, and only when the owner line names another
  session with a transcript; the clock is `$EPOCHSECONDS`, no fork.
- error / empty / loading states: an unreadable time reads as a dead owner, never a live one; a
  takeover always prints, after its rename lands.
- observability: the takeover line names the old owner and the reason.
- risks: a live session idle past the bound loses its card file to a new session in the same tree,
  and so does one waiting past the bound on its own agents or on one long tool call: its main
  transcript does not move then, as `TOOL-aSparedHolder-1` measured for two hours. Its next card write
  sees the new owner live and skips, unit 49 S54's two-session outcome. A `/clear` in one of two live
  sessions sharing a tree takes the other's card file the same way.
- testing: AC1 to AC6 in a scratch repository, and S5's arms in the kickoff engine's suite.
- migration: an id-only owner line is a dead owner, taken over once.
- user docs: the comment above `write_card_file` (S6); no help page covers the card file (section 8
  F6).

What the rule does not check: a transcript path the payload spells with a `\uXXXX` escape or an
escaped quote reads as a missing file, so that session's card reads dead; on a host whose `stat`
lacks `-c`, every owner reads dead and every write takes over, printing its line; and a `resume`
payload gets no `clear` treatment, its predecessor's transcript deciding.

## 6. Acceptance criteria

The fixture: a scratch repository made by `git init` with one empty commit, a scratch folder of
transcript files, and one payload file per session holding `session_id`, `cwd` as the scratch
repository, `transcript_path` as its transcript with JSON's doubled backslashes on Windows, and
`source` as `startup` unless a criterion says otherwise. Each command runs from the scratch
repository, the checker named by its absolute path. "The second line" is the second line of the
card file under the scratch repository's `.claude` folder.

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --card --write < s1.json` runs, the
  second line is `card-owner — s1 · <t1>`, with `<t1>` spelled with `/` throughout.
  Red when: the line omits the transcript, or keeps a backslash.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh --card --replay --session s1` runs
  over AC1's card, the second line still ends with `<t1>`; and when
  `bash skills/session-kickoff/manifest-check.sh --card --write --session s3` runs in a fresh scratch
  repository, the second line is `card-owner — s3 · absent`.
  Red when: a session's own payload-less write records `absent` over its transcript, or a first
  payload-less write records a guessed path.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh --card --write < s2.json` runs over a
  card `s1` owns, `<t1>` touched just before, the output carries
  `card-file — skipped: another live session s1 owns this tree` and the second line is still
  `card-owner — s1 · <t1>`.
  Red when: a live owner's card is overwritten.
- **AC4** — When the same `s2` write runs over each of five staged cards, the second line becomes
  `card-owner — s2 · <t2>` and the output carries one `card-file — took over: session` line: for
  `<t1>` dated 3600 seconds back, `s1 · transcript 3600s old` within a second; for `<t1>` missing, an
  owner line of `card-owner — s1 · absent`, or unit 49's `card-owner — s1`, `s1 · transcript absent`;
  for a card with no owner line, `none · transcript absent`.
  Red when: a dead owner's card is kept, or a takeover prints nothing.
- **AC5** — When `bash skills/session-kickoff/manifest-check.sh --card --write < s2-clear.json` runs,
  its payload carrying `"source":"clear"`, over AC3's live card, the second line names `s2` and the
  output carries `card-file — took over: session s1 · source clear`.
  Red when: a `/clear` successor loads its predecessor's card.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh --card --write < s1b.json` runs, `s1`
  with a second transcript `<t1b>`, over a card `s1` owns, the second line is
  `card-owner — s1 · <t1b>` and the output carries neither `card-file — skipped:` nor
  `card-file — took over:`.
  Red when: a session is refused its own card.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `shell hygiene (a fork spent on builtin work)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the owner fixtures, each failing case staged by reading every other owner as live, by ignoring `source`, or by recording `absent` on a session's own payload-less write · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 8's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What signal says a session is live, and for how long.** Options: (a) the transcript's
  modification time within 1800 seconds; (b) a recorded pid through the unattended kit's probe; (c)
  the stored orientation card's modification time. (b) adds a dependency on an optional kit and (c)
  moves only on card writes. 1800 seconds is the shorter of the two horizons a working session leaves
  between turns and a crashed one is mistaken for live. Re-checked 2026-11-10 against this repo's
  unattended bound of 5400 seconds: that bound decides whether a run's process is killed, where a
  false stale costs a session, and this one decides whose card a tree renders, where a false live
  loads a dead build at level 1, so the shorter bound stands. RESOLVED (agent, 2026-10-24,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Does a session's sub-agent transcripts keep it live.** Options: (a) the main transcript
  alone; (b) `derive_last_move`'s sub-agent term copied inline; (c) that term extracted into a gov lib
  primitive with a parity row, inlined in both kits. (b) is a copy the [reuse] rule refuses. (c) edits
  the clock the unattended run kills a holder by, to serve a case that needs two live sessions in one
  tree, which [yagni] refuses. (a) leaves a session waiting on its own agents past the bound read
  dead, stated in section 5 risks. RESOLVED (agent, 2026-11-10, delegated): (a), rung 1. widens:
  none · relaxes: none
- **F4 — What a payload-less write by the owner records.** Options: (a) `absent`, as rev-2 had it;
  (b) the transcript its own owner line already records; (c) a path derived from the session id, as
  `tools/unattended/unattended.sh#resolve_transcript_path` derives one. (a) makes every card dead
  after the kickoff's `--append`, so unit 49 S54 never holds. (c) is a second derivation of a path the
  harness hands, and its own kit marks the `_` encoding UNVERIFIED. RESOLVED (agent, 2026-11-10,
  delegated): (b), rung 2. widens: none · relaxes: none
- **F5 — How a `/clear` successor gets its own card.** Options: (a) the transcript rule alone; (b) a
  payload whose `source` is `clear` takes over whatever the owner; (c) the CLI's process id beside the
  session id. Under (a) the successor finds its predecessor's transcript seconds old, reads it live,
  and loads that card for up to the bound, the goal's third case left open. (c) needs the unattended
  kit's image probe, a section 3 non-goal. (b) costs a second live session in the same tree its
  render until its own next write, which then skips, stated in section 5 risks. RESOLVED (agent,
  2026-11-10, delegated): (b), rung 2. widens: none · relaxes: none
- **F6 — Where the takeover is documented.** Options: (a) a new help page for the card file; (b) the
  comment above `write_card_file` and the printed line; (c) a sentence in
  `skills/session-kickoff/SKILL.md`. No page under `help/` and no paragraph of that Skill names the
  card file at `95a63d8ab`, by `git grep -n -i "orientation-card" -- help/ skills/session-kickoff/SKILL.md`.
  (a) is a document unit of its own (`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`), and (c) a sentence about a file the Skill
  never introduces. RESOLVED (agent, 2026-11-10, delegated): (b), rung 1. widens: none · relaxes:
  none, since no help page covers the card file and none goes stale

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 39 (HIGH, item H5).
- rev-2 · 2026-11-08 · S1 · section 4 Evidence · section 5 · section 7 · from
  `2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md`: re-read at `05aeb20a`. S1 reads
  `transcript_path` from the payload unit 8 S2 already holds, and says the owner line sits inside the
  envelope beside unit 8 AC3's equality; the evidence names the moved unattended anchors and that
  `write_card_file` is still unit 8's to add; the clock takes the no-fork form; the leg line gains
  `policy fixtures`, whose guard the touched script trips, and the spawn-idioms leg.
- rev-3 · 2026-11-10 · sections 1 to 10 · S1 to S6 · AC1 to AC6 · F2, new F3 to F6 · from
  `2026-11-10-prompt-PLAY-dOrderedCharter-54-precheck-brief.md`, pre-checked at `95a63d8ab` against
  unit 49's rev-8: `write_card_file` and the payload read are built, so the evidence cites them by
  symbol and drops every bare line number; S1 captures `transcript_path` and `source` by `[[ =~ ]]`;
  S2 keeps the owner's own transcript on a payload-less write, since the kickoff's `--append` passes
  `--session` alone (F4); S4 takes over on a `clear` payload (F5) and prints after the rename; the clock
  is `$EPOCHSECONDS`; S5 moves unit 8's and unit 49's arms; the takeover line's reasons are fixed; the
  criteria run the checker in a scratch repository and are renumbered AC1 to AC6, rev-2's AC4 becoming
  AC6; the SKILL.md sentence rev-2 named goes, no such paragraph existing (F6); sub-agent transcripts
  stay out (F3); no edge gained.

## 10. Reuse audit

The seam extended is `write_card_file` and `read_session_id` in
`skills/session-kickoff/manifest-check.sh`: the one payload read gains two fields, and the owner line
unit 49 writes gains one. The liveness term takes the form of the transcript term in
`tools/unattended/unattended.sh#derive_last_move`, one `stat -c %Y` of one file read as dead when it
answers nothing, without importing that kit. The probe
`python tools/codebase-map/reuse_lookup.py "decide whether another session that owns a file is still alive"`
ranked `write_file`, `owners_of`, `extract_session`, `resolve_session_tree` and `check_pid_alive`
by name stem, and the second query,
`"the newest modification time of a session transcript and its sub-agent transcripts"`, ranked the
run-log kit's `extract_session` and `resolve_session_tree`. None is a liveness predicate the kickoff
engine may import, so no existing seam fits the predicate itself. The recall query returned
TOOL-dDerivedDocket-61, the run clock whose transcript term this unit takes, TOOL-aSparedHolder-1,
which measured a live session's transcripts still for two hours, and TOOL-aWokenSentinel-1.

Recall terms used: `python tools/memory-recall/query.py "how is a stale lease or dead session owner detected and taken over" --terms "lease liveness pid alive transcript stale bound takeover session owner card dead subagents clear"`
