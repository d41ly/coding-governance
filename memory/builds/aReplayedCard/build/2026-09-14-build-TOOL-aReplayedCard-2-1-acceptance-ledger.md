# Acceptance ledger — TOOL-aReplayedCard-2, the SessionStart wiring

**Serves:** journal TOOL-aReplayedCard-2

Every observation below was made at the dispatched base tree (`72ff919e`, the branch tip the unit
was handed) with the unit's working-tree changes applied, by running each suite whole and by running
partial suites against staged mutants of the engine under test. No figure is copied from the brief or
the spec; where the spec's wording was changed before the code, the rev-4 line in its section 9 says
what and why.

## What was built

- `skills/session-kickoff/orientation-card.fragment.json` and `orientation-replay.fragment.json`:
  SessionStart, `interpreter: bash`, `hook_path: {here}/manifest-check.sh`, matchers `startup|clear`
  and `resume|compact`, args `--card --write` and `--card --replay`, markers `--write` and
  `--replay`. `tools/check-wiring.fragment.json` (`startup|resume|clear`, `{here}/check-wiring.sh`,
  `--session`, marker `check-wiring.sh`) and `tools/process-monitor/procmon-session.fragment.json`
  (`startup|resume|clear`, `{kit}/process-monitor/procmon-hook.js`, marker `procmon-hook.js`).
- `tools/settings-merge.py` 1.3 → 1.4: the optional `interpreter` (closed pair) and `args` (closed
  character class) keys, `render_command` replacing `_command`, `{here}` in `resolve_hook_path`
  (refused with no fragment file), `set_group` — the re-match, scoped to marker and event, dropping
  only a group the move emptied — the whole-command rewrite, `--resolve-fragment`, the schema
  docstring, and self-test arms 13–17. Arm 17 lifts `check-wiring.sh`'s real `matchers_of` into a
  file and runs it under the bash `resolve_bash` finds — the bare name resolves to System32's WSL
  launcher from a Windows python, the class `subprocess-resolves-a-different-shell` records.
- `tools/check-wiring.sh` 1.2 → 1.3: `resolve_fragment_hook` (one resolver for `{kit}` and
  `{here}`, replacing the two inline copies), `--resolve-fragment`, `-e` in `matchers_of`, the
  `card` arm (`check_card`), one `SMERGE` resolution instead of four.
- `tools/check-wiring.test.sh`: AC14, ten arms — six card states and three `--resolve-fragment`
  arms plus the writer-alone negative.
- `tools/check-hook-destinations.sh`: the flat-home set and canonical prefix read from the deployer,
  the parity arm (both readers asked per fragment, refused on disagreement or refusal), the `{here}`
  branch judging at `{prefix}/<relative>` with both spellings printed, the header.
  `tools/check-hook-destinations.test.sh`: arms 6–8; `FLOOR_ASSERTIONS` 8 → 16.
- `tools/govkit/entries/kickoff-manifest.kit.toml`: the rule shipping the two card fragments to
  `{prefix}/{relpath}`. `check-wiring.kit.toml`: the fragment in the include list and in `claims`.
- `tools/process-monitor/adopt-process-monitor.sh`: `measure_hook_entries`, a per-event count;
  `--check` refuses a file wired on one event alone, naming the missing event's fragment. Its
  self-test's fixture carries both events; a post-only arm and two message arms.
- `.claude/settings.json`: produced by the merger, four fragments applied — three SessionStart
  groups, every one with a matcher, exactly one carrying `compact` and that one the replay.
- `WIRE-INTO-PROJECT.md`: the by-hand SessionStart instruction replaced by the fragment step.
  `tools/hooks/README.md`: the fragment schema paragraph beside the deny section.
  `memory/map/features/agent-cap.md`: the fragment paragraph refreshed; `symbols.json` regenerated.
- `tools/install-prefix-waivers.txt`: four `check-wiring.sh` rows re-keyed for the lines that moved.
  `tools/install-prefix-carried.txt`: `check-wiring.sh` 5 → 3, lowered by `--write-ratchet`.
  `.lexicon.conf`: `VERB_OFFENDER_PIN` 984 → 983 (`_command` left; every addition leads with a
  declared verb; two nested helpers first measured as offenders were renamed).

## The wall, measured

On node `a`, 2026-09-14: `settings-merge.py --selftest` 3 s. `check-wiring.test.sh` 9m22s for 103
passed, run concurrently with the destinations suite (its ceiling is 2320 s). `check-hook-destinations.test.sh`
5m21s for 16 assertions — each arm archives the tree and runs the gate, and the gate now spawns the
two readers per fragment (about 2 s of its 17 s). `adopt-process-monitor.test.sh` 2m17s. The
partial card suite (harness plus AC14) about 35 s per run, five runs in 2m54s; the partial
destinations suite (harness plus arms 6–8) between one and five minutes per run, six runs in about
25 minutes with the build's other work sharing the host — four `git archive` scratch trees and a
gate that spawns two readers per fragment, per arm. `govkit selfcheck` 5 s.

## The bar at the pass boundary

Run standalone, each green: `python tools/settings-merge.py --selftest` (PASS); `bash
tools/check-wiring.test.sh` (103 passed, 0 failed); `bash tools/check-hook-destinations.sh` (7
fragments, clean); `bash tools/check-hook-destinations.test.sh` (PASS, 16 assertions); `python
tools/govkit/govkit.py selfcheck` (exit 0, 68 tracked paths, 0 unclaimed); `bash
tools/process-monitor/adopt-process-monitor.sh --check` (exit 0, `hook entries PostToolUse 1,
SessionStart 1`); `bash tools/check-install-prefix.sh` (clean after the re-key and the ratchet
write); `bash tools/check-kit-versions.sh` (exit 0); `python tools/lexicon/lexicon.py` (983
offenders against the re-pinned 983, every `conv` cell unchanged); `bash
tools/lexicon/adopt-lexicon.sh --check` (Skill in sync); `python
tools/codebase-map/test_codebase_map.py` (fresh); `python tools/check-spec-tokens.py` (exit 0).
`bash tools/check-wiring.sh --check` at the tip prints `ok card` and exits 1 for ONE pre-existing
line outside this unit: `UNWIRED skill — the installed engine differs from tracked`, the
machine-global junction pointing at the primary tree while this branch edits the engine
(`KICK-aReplayedCard-1` and `-2` changed `manifest-check.sh` and `MANIFEST-TEMPLATE.md`); it clears
when the branch lands and the junction's target moves. `bash
tools/process-monitor/adopt-process-monitor.test.sh` reports 29 passed and ONE failing arm outside
this unit, `test_hook_reports_a_flagged_row (got: <silence>)`: it feeds the live hook a 1-second
ceiling over this machine's real roots and needs a process attributable to them at that instant; the
base-revision suite passed it once and failed it once in the same hour, and
`reap.py --sweep --dry-run` in that fixture printed `0 flagged of 0 scoped of 309` with empty
command columns — host state, not this change. The scoped bar and the full bar with
`GATE_SELFTESTS=1` are the orchestrator's at the push boundary; none was run here.

## RED before it landed — how each arm was staged

Mutants were staged into the WORKING COPY one at a time, the suite (or a partial suite carrying the
new arms only) run, and the pristine bytes restored and byte-compared. The runner scripts live in
the session's scratchpad, not in the tree.

`settings-merge.py --selftest`, whole, eight mutations, each red at the line named:

- **M1 — `matchers_of` without `-e` (in `check-wiring.sh`):** arm 17 red at the matcher read-back —
  `matchers_of('--write') returned '', not 'startup|clear'`.
- **M2 — args rendered QUOTED:** arm 13 red at the render pin.
- **M3 — `set_group` never called:** arm 15 red — the matcher-less seeded group survived beside the
  fragment's.
- **M4 — the whole-command rewrite disabled:** arm 14 red — `old/manifest-check.sh --write --card
  --stale` survived.
- **M5 — `{here}` left unexpanded:** arm 13 red at `main([... --fragment card])`, the merge refusing
  a hook path spelled with the token.
- **M6 — `interpreter` outside the pair accepted:** arm 9 red, `accepted a bad fragment: … 'perl'`.
- **M7 — the `args` character class ignored:** arm 9 red, `accepted a bad fragment: … ['a b']`.
- **M8 — a group the move emptied survives:** arm 16 red — `[{'hooks': []}, …]`.

`check-wiring.test.sh`, the AC14 block on the harness (11 arms, green pristine), four mutations of
the checker:

- **W1 — `matchers_of` without `-e`:** 2 red — `both merged -> ok` and `a replay matcher lacking
  compact -> UNWIRED naming compact` (grep read `--write` as an option; the writer read as unwired
  before the replay was judged).
- **W2 — the card arm tests marker presence only:** 2 red — the narrowed-replay arm and `the
  correctly wired writer does not print ok on its own`.
- **W3 — `{here}` resolved to a wrong directory:** 5 red — the `--resolve-fragment` `{here}` arm and
  every engine-present state (the engine read as absent, so `skip` where UNWIRED or ok was due).
- **W4 — the writer alone prints ok:** 1 red — the writer-alone negative.

`check-hook-destinations.test.sh`, arms 6–8 on the harness (8 assertions, green pristine), five
mutations of the gate:

- **D1 — the flat-home refusal removed:** 1 red — `the refusal does not name the directory`: the
  orphan still redded, but for the wrong reason (`tools/agent-cap.js` unshipped), and the arm that
  reads the reason is the one that discriminates.
- **D2a — a shared flat home treated as undecidable:** 3 red — the shared-home pass, and both
  both-spellings arms, every `{here}` fragment under `tools/` refused as `the home of NO kind=flat`.
- **D2b — the adopter path compared as a constant shipped file:** 2 red — `a {here} fragment naming
  an unshipped file was accepted` and its spellings arm (`tools/nobody.sh … ships as
  tools/manifest-check.sh`).
- **D3 — the parity refusal removed:** 1 red — `the refusal does not name the disagreement`: the
  card fragment redded on the wrong path the broken reader produced, never on the readers
  disagreeing.
- **D4 — the ok line prints one spelling:** 1 red — `the ok line does not print both spellings`.

`adopt-process-monitor.test.sh`: the base-revision suite run against the new adopter reds
`test_valid_conf_is_accepted (got '1', wanted '0')`, because its fixture wires PostToolUse alone and
the adopter now refuses that — the post-only refusal observed from the other side, before the
fixture was widened.

Found red by the FIRST full run and fixed in the suite, not the engine: arm 17 passed the lifted
function through `bash -c`, which the Windows loader hands to System32's WSL bash and which the
MSYS layer re-parses as one line; it is a file now, run under the bash `resolve_bash` proves runs,
with forward-slashed paths, because a backslashed `C:\…` handed to MSYS bash loses its separators.

**Evidences:** TOOL-aReplayedCard-2

- AC1 — `settings-merge.py --selftest` — arm 13: on a scratch file the two fragments produce
  SessionStart groups `startup|clear` and `resume|compact`, one entry each, commands `bash
  "${CLAUDE_PROJECT_DIR}/skills/session-kickoff/manifest-check.sh" --card --write` and `… --card
  --replay` pinned as literals, `{here}` absent from the file. Red under M2 (quoted args) and M5
  (the token surviving).
- AC2 — `python tools/settings-merge.py --fragment` — `settings-merge.py --selftest` arm 14: an
  entry under the right matcher naming `old/manifest-check.sh` with `--write --card --stale` is
  rewritten whole by one run of the merger with the card fragment; arm 14b: the
  three shipped fragments render as `node "${CLAUDE_PROJECT_DIR}/<resolved>"` with nothing after.
  Red under M4.
- AC3 — `settings-merge.py --selftest` — arm 15: the four fragments in file order, reverse, and file
  order again each yield three groups, `startup|clear` and `resume|compact` one entry each and
  `startup|resume|clear` two, entry sets equal across the three, no group empty; arm 16: a
  matcher-less group holding the check-wiring entry moves under `startup|resume|clear` and the old
  group is gone, and a group the move does not empty keeps its foreign command. Red under M3 and
  M8.
- AC4 — `.claude/settings.json` — read at the tip: three SessionStart groups, matchers
  `startup|clear`, `resume|compact`, `startup|resume|clear`; exactly one carries `compact` and its
  one entry is `… manifest-check.sh" --card --replay`; the check-wiring and procmon entries sit
  under `startup|resume|clear`. `adopt-process-monitor.sh --check` reads `PostToolUse 1,
  SessionStart 1`.
- AC5 — `check-hook-destinations.sh` — at the tip: exit 0 over 7 fragments; the two card fragments
  print `-> skills/session-kickoff/manifest-check.sh in the tree, ships as tools/manifest-check.sh`;
  every fragment passed the parity arm, `check-wiring.sh --resolve-fragment` and `settings-merge.py
  --resolve-fragment` printing one value each. Red under D3 with the readers made to disagree.
- AC6 — `check-hook-destinations.test.sh` — arm 6: a `{here}` fragment under `tools/hooks/` exits 1
  naming `'tools/hooks' is the home of NO kind=flat`; arm 7: one under `tools/` naming
  `settings-merge.py` exits 0 printing both spellings, and one naming `nobody.sh` exits 1 printing
  both. Red under D1, D2a and D2b.
- AC7 — `check-wiring.sh --check` — at the tip over the merger-produced file: `ok card —
  SessionStart card entries wired in .claude/settings.json (--write at 'startup|clear', --replay at
  'resume|compact')`; `check-wiring.test.sh` AC14 state 4: a hand-written replay entry under
  `resume` alone prints `UNWIRED card — the orientation-replay entry (--replay) is wired under
  matcher 'resume', not 'resume|compact'`; `settings-merge.py --selftest` arm 17: every one of the 7
  tracked fragments applied and read back through the checker's own `matchers_of` returns its
  matcher. Red under W1, W2 and M1.
- AC8 — `govkit selfcheck` — exit 0 at the tip, `68 tracked path(s) · 26 entr(y|ies) · 23
  exemption(s) · 0 unclaimed`; `govkit plan --target <scratch> --kits
  kickoff-manifest,check-wiring,process-monitor` against a git-initialised scratch with a declared
  `deploy.toml` lists `tools/check-wiring.fragment.json`, `tools/orientation-card.fragment.json`,
  `tools/orientation-replay.fragment.json` and
  `tools/process-monitor/procmon-session.fragment.json` among its writes. Red as staged, each
  restored after: with the fragment dropped from the check-wiring rule's `claims` (kept in its
  include), selfcheck exits 1 — `entry 'check-wiring' declares a rule whose destination
  'tools/check-wiring.fragment.json' is not among its own claims`, rule 4b, the brief's reason for
  the double entry; with the kickoff rule removed, selfcheck exits 1 naming both
  `skills/session-kickoff/orientation-*.fragment.json` as `in the declared surface but neither an
  entry member nor an exemption`, `2 unclaimed`. Selfcheck is 5 s, so both were run whole.
- AC9 — `--card --replay` — OWED TO THE ORCHESTRATOR, NOT OBSERVED HERE: a sidechain cannot compact
  a session. In a session started after this unit lands, force one compaction and read the
  transcript after the boundary: the card's bytes re-injected verbatim, then one `now —` line, and
  no `check-wiring` output. The orchestrator appends beneath this line the session id, the date and
  what the transcript showed. Red as written: the replay entry never fires, the writer fires instead
  (a fresh card, not the stored one), or `check-wiring` output appears after the boundary.
