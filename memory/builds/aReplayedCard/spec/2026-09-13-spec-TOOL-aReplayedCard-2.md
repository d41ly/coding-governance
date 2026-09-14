# TOOL-aReplayedCard-2 — SessionStart matchers, two card fragments, a rematching merge, a wiring arm

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md](../build/2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 |
| [2026-09-14-build-TOOL-aReplayedCard-2-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aReplayedCard-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-TOOL-aReplayedCard-2-brief.md](../prompts/2026-09-14-prompt-TOOL-aReplayedCard-2-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

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
  `SessionStart`, `interpreter: bash`, `hook_path: {here}/manifest-check.sh`, and distinct
  space-free markers that are substrings of the rendered command under the merger's plain view and
  under `check-wiring.sh`'s whitespace-stripped view alike: `orientation-card.fragment.json` with
  matcher `startup|clear`, args `["--card", "--write"]`, marker `--write`;
  `orientation-replay.fragment.json` with matcher `resume|compact`, args `["--card", "--replay"]`,
  marker `--replay`. Neither marker occurs in any other command `.claude/settings.json` carries.
  Neither fragment carries a registry: the verb reads it from the manifest (`KICK-aReplayedCard-1`
  S4). Observed by AC1 and AC7.
- **S2** `tools/settings-merge.py`'s fragment schema gains two OPTIONAL keys, `interpreter`
  (`node` or `bash`, default `node`) and `args` (a list of strings, default empty);
  `render_command` renders `<interpreter> "${CLAUDE_PROJECT_DIR}/<hook_path>"` followed by the
  arguments as UNQUOTED argv tokens joined by single spaces, the shape the live
  `bash "…/check-wiring.sh" --session` entry already has, so a marker is a substring under both
  readers; the REPATH compare is on the whole rendered command, so a stale path or a changed
  argument is rewritten in place; the schema docstring at its lines 34–37 is rewritten to say
  which fields vary and why. Observed by AC1 and AC2.
- **S3** The merger REMATCHES: when an entry carrying the fragment's marker sits under the same
  event in a group whose matcher differs from the fragment's, the entry moves to the group holding
  the fragment's matcher — created if absent, shared if two fragments declare one matcher, which
  is how `merge()` already groups at its line 210 — and the emptied group is dropped. The re-match
  is scoped to marker AND event, so a basename marker shared across events is safe. Applying the
  four fragments in either order twice yields the same three groups with the same entry SETS.
  Observed by AC3.
- **S4** The two existing SessionStart entries gain matcher `startup|resume|clear`, so neither
  runs at `compact`, through fragments the merger re-matches: `tools/check-wiring.fragment.json`
  with `interpreter: bash`, args `["--session"]`, `hook_path: {here}/check-wiring.sh`, marker
  `check-wiring.sh`; and `tools/process-monitor/procmon-session.fragment.json`, a SessionStart
  sibling of that kit's PostToolUse fragment with `hook_path: {kit}/process-monitor/procmon-hook.js`,
  marker `procmon-hook.js` — the second fragment aReapedSpinner's closing review R8 asked for and
  the fold there left unbuilt. `tools/process-monitor/adopt-process-monitor.sh`'s remediation line
  names both fragments and its wiring count is per event: `--check` DECIDES per event, refusing a
  file wired on one event alone and naming the fragment for the missing one, and its own
  self-test's fixture carries both events, with a post-only arm that must refuse. Observed by AC4.
- **S5** A `{here}` token, resolved by all three fragment readers — `settings-merge.py`,
  `check-wiring.sh` and `check-hook-destinations.sh` — as the fragment's OWN directory, beside the
  `{kit}` token each already resolves two directories up. The destinations leg checks a `{here}`
  fragment at its ADOPTER destination: the fragment's directory must be the `home` of at least one
  `kind = "flat"` descriptor, else the leg refuses naming the directory, and `{prefix}/<basename>`
  is compared against the WHOLE declared destination set, both spellings printed; the header states
  that a flat kit's in-tree path and its shipped path differ by design. `check-wiring.sh` extracts
  ONE `resolve_fragment_hook` helper shared by its scratch, recall and card arms — today two inline
  copies at its lines 403 and 466 — and gains a `--resolve-fragment <path>` print verb, twinned on
  `settings-merge.py`, and the parity arm compares those two verbs' output over every tracked
  fragment, so it reads the value the arms decide on rather than a third derivation beside them.
  `{here}` resolves ONLY against a fragment file: with none there is no "here", and both readers
  refuse rather than guess a prefix. Observed by AC5 and AC6.
- **S6** A `card` arm in `tools/check-wiring.sh` on the recall arm's pattern: fragment absent →
  `skip`; fragment present and either SessionStart entry absent, or present under a matcher that
  is not the fragment's → `UNWIRED` naming the entry and the matcher it expected; both present →
  `ok`. The two engine-absent states the scratch arm has apply too: engine missing and unwired →
  `skip` (not adopted); engine missing and wired → `UNWIRED` (dispatches a missing script).
  `matchers_of` at its line 157 gains `-e` before the marker, because a dash-leading marker
  is otherwise parsed by `grep -F` as an option and every card check would print `UNWIRED`
  forever. Observed by AC7.
- **S7** The descriptors claim the new files so adopters receive them and `govkit selfcheck` stays
  green: `tools/govkit/entries/kickoff-manifest.kit.toml` gains a rule shipping the two card
  fragments to `{prefix}/{relpath}`; `check-wiring.kit.toml` adds `check-wiring.fragment.json` to
  its include list AND to that rule's `claims`, because `govkit.py`'s rule 4b reds a rule whose
  resolved destination is not among its own claims; the process-monitor kit's `**` rule already
  covers its sibling. Observed by AC8.
- **S8** `WIRE-INTO-PROJECT.md`'s instruction that `settings-merge.py` handles only the agent-cap
  block and SessionStart is added by hand — its lines 610–612 at base — is REPLACED by one step:
  apply the four fragments with `settings-merge.py --fragment`, run `check-wiring.sh --check`, and
  read the deny's ceiling from the hooks README. NOT OBSERVED by a criterion: runbook prose.

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
one argument each, `--write` and `--replay`: space-free, so `check-wiring.sh`'s stripped view still
holds them; distinct, so the merger's substring test at its line 228 never confuses them; and
dash-leading, which is why `matchers_of` needs `-e`.

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
| `resolve_fragment_hook` | shell function | `check-wiring.sh` | leads with `resolve`, the one token resolver its three arms share |
| `check_card` | shell function | `check-wiring.sh` | leads with `check`, like every arm |
| `--resolve-fragment` | print verb | `check-wiring.sh` and `settings-merge.py` | the parity arm's two inputs |
| `measure_hook_entries` | shell function | `adopt-process-monitor.sh` | leads with `measure`: counts one event's entries, decides nothing |
| `resolve_bash` | python function | `settings-merge.py` self-test | leads with `resolve`; the bash that shares this filesystem, RUN to prove it |

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
| `tools/settings-merge.py` | two optional keys, `render_command`, whole-command repath, the re-match, `{here}`, `--resolve-fragment`, the docstring; self-test arms |
| `tools/check-wiring.sh` | `resolve_fragment_hook` replacing two inline resolvers; `{here}`; `--resolve-fragment`; `matchers_of -e`; the `card` arm |
| `tools/check-wiring.test.sh` | arms for S6 |
| `tools/check-hook-destinations.sh` | `{here}` resolution with the flat-kit adopter rule; the parity arm through the two print verbs; header |
| `tools/check-hook-destinations.test.sh` | arms 6–8 for AC6 and the parity refusal |
| `tools/govkit/entries/kickoff-manifest.kit.toml` | the fragments' shipping rule |
| `tools/govkit/entries/check-wiring.kit.toml` | the fragment in the include list and the rule's `claims` |
| `tools/process-monitor/adopt-process-monitor.sh` | the remediation line names both fragments; the wiring count is per event |
| `tools/process-monitor/adopt-process-monitor.test.sh` | the fixture carries both events; a post-only arm refuses |
| `.claude/settings.json` | four matchers, two new entries, produced by the merger |
| `WIRE-INTO-PROJECT.md` | lines 610–612 replaced by the fragment step |
| `tools/hooks/README.md` | the fragment schema's two new keys beside the deny section |
| `memory/map/features/agent-cap.md` | the dossier's fragment paragraph, refreshed on touch |
| `tools/install-prefix-waivers.txt`, `tools/install-prefix-carried.txt` | line-keyed waivers re-keyed; the carried count lowered where a remedy path was hoisted |

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

- security — settings edits through the existing merger. `args` render as UNQUOTED tokens (S2), so
  the loader admits each one only from a closed character class — no whitespace, quote or shell
  metacharacter — and `interpreter` only from the closed pair, because both land inside a command
  Claude Code runs. Refused by name, never defaulted over.
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
  followed by that fragment's arguments as unquoted tokens, and the `{here}` token is absent from
  the output.
  Red when: the two fragments collapse into one group, the render drops or quotes the arguments,
  or the token survives unresolved.
- **AC2** — When a scratch settings file holds an entry whose command names a stale path or a
  different argument list for the same marker, one `python tools/settings-merge.py --fragment` run
  rewrites the whole command; when the three shipped fragments are applied, the rendered commands
  are byte-identical to today's.
  Red when: the repath compares the path alone and a changed argument survives.
- **AC3** — When the merger's self-test applies the four new fragments in file order, then in
  reverse, then in file order again, each result holds three SessionStart groups — `startup|clear`
  and `resume|compact` with one entry each, `startup|resume|clear` with the two re-matched entries
  — the entry SET of every group is equal across the three orders, and no group is empty; when it
  seeds a matcher-less SessionStart group holding the check-wiring marker and applies the
  check-wiring fragment, the entry sits under `startup|resume|clear` and the old group is gone.
  Red when: a second entry is appended, a group ping-pongs between two matchers, an empty group
  survives, or the shared-matcher case is not exercised.
- **AC4** — When `.claude/settings.json` at the landing commit is read, every SessionStart group
  carries a `matcher`, exactly one carries `compact`, and that one's entry is the replay.
  Red when: the wiring check or procmon still fires on compaction.
- **AC5** — When `bash tools/check-hook-destinations.sh` runs at the landing commit, it exits 0,
  prints the two card fragments resolved to `skills/session-kickoff/manifest-check.sh` in the tree
  and to `manifest-check.sh` under the adopter prefix as the shipped destination, and the parity
  arm reports that `bash tools/check-wiring.sh --resolve-fragment` and
  `python tools/settings-merge.py --resolve-fragment` print the same path for every tracked
  fragment.
  Red when: a `{here}` fragment is judged at its in-tree path against the adopter set and fails, or
  the two wiring readers disagree.
- **AC6** — When the destinations leg's fixture places a `{here}` fragment in a directory that is
  the home of no `kind = flat` descriptor, the leg exits 1 naming the directory; placed under
  `tools/`, whose home ten flat descriptors share, the leg compares `{prefix}/<basename>` against
  the whole declared set and exits 0.
  Red when: an orphan fragment passes because the flat-kit rule found nothing to compare, or a
  shared home is treated as undecidable.
- **AC7** — When `bash tools/check-wiring.sh --check` runs at the landing commit over the settings
  file the merger itself produced, it prints an `ok card` line; when the self-test stages a
  settings file whose replay entry carries matcher `resume` alone, the arm prints `UNWIRED card`
  naming `compact`; and the merger's self-test, for every tracked fragment, applies it and runs
  `matchers_of` over the result asserting the fragment's matcher comes back.
  Red when: a narrowed matcher passes as wired, or a dash-leading marker makes `grep -F` exit 2 and
  the arm prints `UNWIRED` over a correctly merged file.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs at the landing commit it exits 0,
  and `python tools/govkit/govkit.py plan --target <scratch> --kits
  kickoff-manifest,check-wiring,process-monitor` lists all four new fragments among the files it
  would write.
  Red when: a new fragment is unclaimed by any descriptor rule, or claimed by a rule whose `claims`
  omit it.
- **AC9** — When one compaction is forced in a session on this branch after landing, the transcript
  shows the card's bytes re-injected after the compaction boundary, verbatim, followed by one
  `now —` line, and no `check-wiring` output.
  Red when: the replay entry never fires or fires the writer instead.
  fixture: one live session; recorded in the acceptance ledger with the session id.
  cost: one manual compaction, minutes.

## 7. Gates

`settings-merge selftest` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `govkit selfcheck` · `process-monitor wiring` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/settings-merge.py` self-test · a bash fragment with arguments, a stale command, a matcher-less group, two fragments sharing a matcher, and the four fragments in both orders twice · none, the self-test asserts inline
New arm: `tools/settings-merge.py` self-test · every tracked fragment applied and read back through `matchers_of` · none
New arm: `tools/check-wiring.test.sh` · a replay entry whose matcher lacks `compact` · its own count line
New arm: `tools/check-hook-destinations.sh` · a `{here}` fragment in a directory no flat descriptor homes, and one under a shared home · none, the leg refuses inline

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
- rev-3 · 2026-09-14 · §2 · §4 · §6 · §7 · §10 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · AC1 ·
  AC3 · AC5 · AC6 · AC7 · AC8 · folded the round-2 spec audit. Markers are the space-free
  `--write` and `--replay`, arguments render unquoted, and `matchers_of` gains `-e` so a
  dash-leading marker is not an option (H1); AC3 expects three groups with the shared matcher
  holding two entries and set equality across orders (M6); `govkit plan` is the verb, `--dry-run`
  does not exist (M7); the procmon SessionStart fragment is aReapedSpinner R8's, cited, with the
  adopter's remediation line and per-event count (M10); the flat-kit rule is "at least one flat
  descriptor homes the directory" against the whole set, one shared resolver and two print verbs
  feed the parity arm (M11); the check-wiring rule's `claims` gain the fragment (L5); the runbook's
  by-hand instruction is replaced, not appended to (L6).
- rev-4 · 2026-09-14 · §2 · §4 · §5 · S2 · S4 · S5 · S6 · changed BEFORE the code where the build
  had to diverge. §5's security line said `args` render as QUOTED tokens while S2 and AC1 say
  unquoted; S2 wins, and the loader's closed character class for `args` and closed pair for
  `interpreter` are now stated as the control that makes unquoted safe. S4 states that the
  adopter's per-event count DECIDES (a post-only file is refused naming the missing fragment), so
  its self-test's fixture carries both events. S5 states that `{here}` with no fragment file
  refuses. S6 gains the two engine-absent states the scratch arm has. §4's files table gains the
  two self-tests, the dossier and the two install-prefix registries; the inventory gains
  `check_card`, `measure_hook_entries` and the self-test's `resolve_bash` (the merger's arm 17 runs
  the checker's real `matchers_of` under bash, and the bare name resolves to the WSL launcher on a
  Windows python — the gotcha class `subprocess-resolves-a-different-shell`).

## 10. Reuse audit

The seams are `tools/settings-merge.py`'s `merge()` at lines 199–232, whose marker-and-path compare
is the two-question shape the re-match extends with a third, and its `resolve_hook_path` at lines
174–198, where `{here}` joins `{kit}`; the recall arm of `tools/check-wiring.sh` at lines 434–488,
the one arm that already distinguishes `skip` from `UNWIRED` on fragment presence, and its
`matchers_of` at lines 157–166, the stripped view every marker must survive; and
`tools/check-hook-destinations.sh` lines 71–77, the third reader of the token. The procmon
SessionStart fragment is the residue aReapedSpinner's closing review R8 recorded at
`memory/builds/aReapedSpinner/reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round2.md`
lines 236–248 and no backlog row carried. `python
tools/codebase-map/reuse_lookup.py` run for this build returned `agent-cap.topLevelArgs` and
`registry.toml` as seams; the fragment schema was read from `tools/hooks/scratch-guard.fragment.json`
and `tools/process-monitor/procmon-hook.fragment.json`, and the flat-kit destination from
`tools/govkit/entries/kickoff-manifest.kit.toml`.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
