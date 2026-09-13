# TOOL-aReplayedCard-2 — SessionStart matchers, two card fragments, a rematching merge, a wiring arm

**Status:** SPECCED · rev-2 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Wire the card verb into the harness: write it at `startup` and `clear`, replay it at `resume` and
`compact`, and stop the two existing SessionStart entries from running on every compaction. Ship
the wiring as fragments `settings-merge.py` applies, which means widening that merger's schema by
two optional fields so a fragment can name an interpreter and arguments, teaching it to re-match an
entry it already owns, adding a `{here}` token the three fragment readers resolve alike, and adding
the `check-wiring.sh` arm that reds when a matcher is missing or misspelled — because a
SessionStart matcher that never fires looks exactly like one that is wired.

## 2. Scope (IN)

- **S1** Two fragment files beside the engine at `skills/session-kickoff/`, each with event
  `SessionStart`, `interpreter: bash`, `hook_path: {here}/manifest-check.sh`, and distinct markers
  equal to their argument strings: `orientation-card.fragment.json` with matcher `startup|clear`,
  args `["--card", "--write"]`, marker `--card --write`; `orientation-replay.fragment.json` with
  matcher `resume|compact`, args `["--card", "--replay"]`, marker `--card --replay`. Neither
  carries a registry: the verb reads it from the manifest (`KICK-aReplayedCard-1` S4). Observed by
  AC1.
- **S2** `tools/settings-merge.py`'s fragment schema gains two OPTIONAL keys, `interpreter`
  (`node` or `bash`, default `node`) and `args` (a list of strings, default empty); `_command`
  renders `<interpreter> "${CLAUDE_PROJECT_DIR}/<hook_path>" <args…>`; the REPATH compare is on the
  whole rendered command, so a stale path or a changed argument is rewritten in place; the schema
  docstring at its lines 34–37 is rewritten to say which fields vary and why. Observed by AC1 and
  AC2.
- **S3** The merger REMATCHES: when an entry carrying the fragment's marker sits under the same
  event in a group whose matcher differs from the fragment's, the entry moves to the fragment's
  group and the emptied group is dropped. The re-match is scoped to marker AND event, and the two
  card fragments have disjoint markers, so applying both in either order twice yields two groups
  of one entry each and byte-identical output. Observed by AC3.
- **S4** The two existing SessionStart entries gain matcher `startup|resume|clear`, so neither
  runs at `compact`, through fragments the merger re-matches: `tools/check-wiring.fragment.json`
  with `interpreter: bash`, args `["--session"]`, `hook_path: {here}/check-wiring.sh`; and
  `tools/process-monitor/procmon-session.fragment.json`, a SessionStart sibling of that kit's
  PostToolUse fragment with `hook_path: {kit}/process-monitor/procmon-hook.js`. Observed by AC4.
- **S5** A `{here}` token, resolved by all three fragment readers — `settings-merge.py`,
  `check-wiring.sh` and `check-hook-destinations.sh` — as the fragment's OWN directory, beside the
  `{kit}` token each already resolves two directories up. The destinations leg checks a `{here}`
  fragment at its ADOPTER destination: it finds the descriptor whose `home` is the fragment's
  directory and, for a `kind = "flat"` kit, compares `{prefix}/<basename>` against the declared
  set, printing both spellings; it states in its header that a flat kit's in-tree path and its
  shipped path differ by design. A parity arm asserts the two wiring readers resolve every tracked
  fragment to the same path. Observed by AC5 and AC6.
- **S6** A `card` arm in `tools/check-wiring.sh` on the recall arm's pattern: fragment absent →
  `skip`; fragment present and either SessionStart entry absent, or present under a matcher that
  is not the fragment's → `UNWIRED` naming the entry and the matcher it expected; both present →
  `ok`. Observed by AC7.
- **S7** The descriptors claim the new files so adopters receive them and `govkit selfcheck` stays
  green: `tools/govkit/entries/kickoff-manifest.kit.toml` gains a rule shipping the two card
  fragments to `{prefix}/{relpath}`, `check-wiring.kit.toml` adds `check-wiring.fragment.json` to
  its include list, and the process-monitor kit's `**` rule already covers its sibling. Observed by
  AC8.
- **S8** `WIRE-INTO-PROJECT.md` gains one step: apply the four fragments with `settings-merge.py
  --fragment`, run `check-wiring.sh --check`, and read the deny's ceiling from the hooks README.
  NOT OBSERVED by a criterion: runbook prose.

## 3. Non-goals (OUT)

- No `UserPromptSubmit` and no `PreCompact` hook; the design record's harness area rejects both.
- No change to any wired command's PATH beyond what the fragment declares; `check-wiring --session`
  keeps its report-never-rewrite rule (`TOOL-aBatchedTribunal-1f`).
- No `SubagentStop` hook; stage 2.
- No CI wiring.
- No inventory key and no dossier claim for fragments: `tools/codebase-map/map_extractors.py`
  enumerates no `*.fragment.json` class, so a claim would name a dead key; the session-kickoff
  dossier is `KICK-aReplayedCard-3`'s to refresh.
- No `--registry` on any command line; the manifest names it.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the verb the two entries call and the manifest key it
  reads; without it both SessionStart entries run a bash script that refuses.
- **hands-off** `KICK-aReplayedCard-3` — the card in context that Step 1 consumes exists only once
  this unit wires the writer.
- **hands-off** `TOOL-aReplayedCard-3` — the fresh session's card a resumed run's kickoff appends to.
- **consumes-from** external — the harness's SessionStart matcher vocabulary `startup`, `resume`,
  `clear`, `compact`, confirmed from the hooks documentation in the design record's appendix
  (verdicts 3 and 16).

## 4. Design

### Data model

The fragment schema becomes `{name, event, matcher, marker, hook_path, interpreter?, args?}`, one
event per file, the two new keys optional so the three shipped fragments are unchanged bytes and
render as before. The card needs two matchers on one event, so two files, and their markers are
their argument strings, which is what makes them disjoint under the merger's substring test at its
line 228.

`{here}` is the fragment's own directory. It exists because the kickoff kit is `kind = "flat"` with
`home = "skills/session-kickoff"` and `to = "{prefix}/manifest-check.sh"`: `{kit}` resolves two
directories up, which for a fragment beside that engine is `skills/`, a path nothing ships. In an
adopter the fragment is copied beside the checker at `{prefix}/`, and `{here}` resolves correctly
there too.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `orientation-card.fragment.json` | fragment | `skills/session-kickoff/` | kebab like the siblings |
| `orientation-replay.fragment.json` | fragment | `skills/session-kickoff/` | kebab |
| `check-wiring.fragment.json` | fragment | `tools/` | kebab |
| `procmon-session.fragment.json` | fragment | `tools/process-monitor/` | kebab |
| `interpreter`, `args` | fragment keys | `settings-merge.py` | lower, like the five existing keys |
| `{here}` | fragment token | three readers | braces, like `{kit}` |
| `render_command` | python function | `settings-merge.py` | leads with `render`, replaces `_command` |
| `set_group` | python function | `settings-merge.py` | leads with `set`, the re-match step if extracted |

### Migration

An installed tree runs `python tools/settings-merge.py --fragment <each>` once for the four
fragments; the re-match moves the two existing entries under their matchers without duplicating
them. `check-wiring.sh --check` reports UNWIRED until then, which is the migration's own signal.
The three shipped fragments carry no new key and render byte-identically.

### Rollout

Live at the commit. The first SessionStart after it writes the card; the first compaction replays.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/orientation-card.fragment.json` | new |
| `skills/session-kickoff/orientation-replay.fragment.json` | new |
| `tools/check-wiring.fragment.json` | new |
| `tools/process-monitor/procmon-session.fragment.json` | new |
| `tools/settings-merge.py` | two optional keys, `render_command`, whole-command repath, the re-match, `{here}`, the docstring; self-test arms |
| `tools/check-wiring.sh` | `{here}` resolution; the `card` arm |
| `tools/check-wiring.test.sh` | arms for S6 |
| `tools/check-hook-destinations.sh` | `{here}` resolution with the flat-kit adopter rule; the parity arm; header |
| `tools/govkit/entries/kickoff-manifest.kit.toml` | the fragments' shipping rule |
| `tools/govkit/entries/check-wiring.kit.toml` | the fragment in the include list |
| `.claude/settings.json` | four matchers, two new entries, produced by the merger |
| `WIRE-INTO-PROJECT.md` | one step |
| `tools/hooks/README.md` | the fragment schema's two new keys beside the deny section |

### Alternatives rejected

**Editing `.claude/settings.json` by hand and shipping no fragment.** An adopter then has no
merge path and the wiring arm has nothing to compare against.

**One fragment carrying a matcher list.** The merger's schema is one matcher per fragment; a
list is a second grammar, where two optional scalar keys extend the existing one.

**Leaving the existing entries matcher-less.** Measured 35–81 s per compaction for the wiring
check; the design record's improvement 3.

**Putting the card fragments under `tools/`.** They would resolve `{kit}` correctly and ship to
the wrong place: the checker they name lives beside the engine, and the deployer copies a kit's
files from its home.

**A `--registry` argument.** A fragment is deployed verbatim; a per-adopter value on it is a
literal the adopter must edit. The manifest is the project layer.

## 5. Production-readiness checklist

- security — N/A. Settings edits through the existing merger; `args` are rendered as separate
  quoted tokens, never joined into a shell string.
- perf / scale — two fewer hook runs per compaction; the card run replaces neither.
- error / empty / loading states — a fragment missing a required field is refused by the merger and
  reported UNWIRED by the arm, as today for scratch-guard; an `interpreter` outside the pair is
  refused by name.
- observability — the `card` arm line on every SessionStart; the destinations leg prints both
  spellings of a `{here}` fragment.
- risks — a misspelled matcher never fires; the arm compares the literal. Three readers of one
  token; the parity arm.
- testing — merger self-test arms for the render, the repath, the re-match and idempotence;
  `check-wiring.test.sh` arms; the destinations leg's own fixture.
- migration — one merger run per installed tree.
- user docs — `WIRE-INTO-PROJECT.md`; the hooks README states the schema.

## 6. Acceptance criteria

- **AC1** — When `python tools/settings-merge.py --fragment` is run on a scratch settings file with
  `orientation-card.fragment.json` and then `orientation-replay.fragment.json`, the result holds
  two SessionStart groups with matchers `startup|clear` and `resume|compact`, each carrying one
  entry whose command is `bash "${CLAUDE_PROJECT_DIR}/skills/session-kickoff/manifest-check.sh"`
  followed by that fragment's arguments, and the `{here}` token is absent from the output.
  Red when: the two fragments collapse into one group, the render drops the arguments, or the
  token survives unresolved.
- **AC2** — When a scratch settings file holds an entry whose command names a stale path or a
  different argument list for the same marker, one `python tools/settings-merge.py --fragment` run
  rewrites the whole command; when the three shipped fragments are applied, the rendered commands
  are byte-identical to today's.
  Red when: the repath compares the path alone and a changed argument survives.
- **AC3** — When the merger's self-test applies the four new fragments in file order, then in
  reverse, then in file order again, the three results are byte-identical, hold four SessionStart
  groups of one entry each, and no group is empty; when it seeds a matcher-less SessionStart group
  holding the check-wiring marker and applies the check-wiring fragment, the entry sits under
  `startup|resume|clear` and the old group is gone.
  Red when: a second entry is appended, a group ping-pongs between two matchers, or an empty group
  survives.
- **AC4** — When `.claude/settings.json` at the landing commit is read, every SessionStart group
  carries a `matcher`, exactly one carries `compact`, and that one's entry is the replay.
  Red when: the wiring check or procmon still fires on compaction.
- **AC5** — When `bash tools/check-hook-destinations.sh` runs at the landing commit, it exits 0,
  prints the two card fragments resolved to `skills/session-kickoff/manifest-check.sh` in the tree
  and to `manifest-check.sh` under the adopter prefix as the shipped destination, and the parity
  arm reports the two
  wiring readers agree on every tracked fragment.
  Red when: a `{here}` fragment is judged at its in-tree path against the adopter set and fails, or
  the three readers disagree.
- **AC6** — When the destinations leg's fixture places a `{here}` fragment in a directory no
  descriptor declares as a home, the leg exits 1 naming the directory.
  Red when: an orphan fragment passes because the flat-kit rule found nothing to compare.
- **AC7** — When `bash tools/check-wiring.sh --check` runs at the landing commit it prints an `ok
  card` line; when the self-test stages a settings file whose replay entry carries matcher
  `resume` alone, the arm prints `UNWIRED card` naming `compact`.
  Red when: a narrowed matcher passes as wired.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs at the landing commit it exits 0,
  and `govkit apply --dry-run` against a scratch target lists all four new fragments among the
  files it would ship.
  Red when: a new fragment is unclaimed by any descriptor rule.
- **AC9** — When one compaction is forced in a session on this branch after landing, the transcript
  shows the card's bytes re-injected after the compaction boundary, verbatim, followed by one
  `now —` line, and no `check-wiring` output.
  Red when: the replay entry never fires or fires the writer instead.
  fixture: one live session; recorded in the acceptance ledger with the session id.
  cost: one manual compaction, minutes.

## 7. Gates

`settings-merge selftest` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `govkit selfcheck` · `process-monitor wiring` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/settings-merge.py` self-test · a bash fragment with arguments, a stale command, a matcher-less group, and the four fragments in both orders twice · none, the self-test asserts inline
New arm: `tools/check-wiring.test.sh` · a replay entry whose matcher lacks `compact` · its own count line
New arm: `tools/check-hook-destinations.sh` · a `{here}` fragment in a directory no descriptor homes · none, the leg refuses inline

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §1 · §2 · §3 · §4 · §6 · §7 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · AC1 · AC2
  · AC3 · AC5 · AC6 · AC8 · folded the round-1 spec audit. The merger schema gains optional
  `interpreter` and `args` and renders them, and the repath compares the whole command (B3); the
  two card fragments carry disjoint markers and the re-match is scoped to marker and event, with
  an idempotence arm over the set (H5); a `{here}` token for flat kits, resolved by all three
  readers, with the destinations leg judging a flat kit at its adopter path and a parity arm (H6);
  the descriptors claim the four fragments and `govkit selfcheck` joins §7 (H7); the fragment
  inventory claim is dropped as a dead key (M1); the dossier is `KICK-aReplayedCard-3`'s alone
  (L2); `--registry` leaves every command line (B3, M4); `hands-off` edges to the two units whose
  criteria need a wired writer (M5).

## 10. Reuse audit

The seams are `tools/settings-merge.py`'s `merge()` at lines 199–232, whose marker-and-path compare
is the two-question shape the re-match extends with a third, and its `resolve_hook_path` at lines
174–198, where `{here}` joins `{kit}`; the recall arm of `tools/check-wiring.sh` at lines 434–488,
the one arm that already distinguishes `skip` from `UNWIRED` on fragment presence; and
`tools/check-hook-destinations.sh` lines 71–77, the third reader of the token. `python
tools/codebase-map/reuse_lookup.py` run for this build returned `agent-cap.topLevelArgs` and
`registry.toml` as seams; the fragment schema was read from `tools/hooks/scratch-guard.fragment.json`
and `tools/process-monitor/procmon-hook.fragment.json`, and the flat-kit destination from
`tools/govkit/entries/kickoff-manifest.kit.toml`.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
