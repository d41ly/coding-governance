# Brief — TOOL-aReplayedCard-2, the SessionStart wiring

**Serves:** journal TOOL-aReplayedCard-2

What this pass is handed: the unit's spec at rev-3 (two audit rounds, CLEAN WITH FIXES at the
second, folded), the build README, `tools/settings-merge.py` (455 lines; `merge()` at 199–232,
`resolve_hook_path` at 174–198, `_FRAGMENT_KEYS` at 146, `_command` at 168), `tools/check-wiring.sh`
(860 lines; `matchers_of` at 157–166, the scratch arm's inline `{kit}` resolver near 403, the recall
arm at 434–488), `tools/check-hook-destinations.sh` (its `{kit}` resolver at 71–77), the three
shipped fragments, and the writer as units 2 and 4 left it: `skills/session-kickoff/manifest-check.sh
--card --write` and `--card --replay`, reading `registry:` from the manifest.

What it builds: four fragments, the merger's two optional keys and its re-match, a `{here}` token
in three readers with a parity arm and one shared resolver in `check-wiring.sh`, the `card` arm,
the descriptors' claims, the settings edits the merger produces, the adopter's remediation line,
and one replaced step in the runbook.

What is not obvious, each verified at the base:

- **Markers are `--write` and `--replay`, space-free and dash-leading**, and `matchers_of` strips
  whitespace before `grep -F "$1"` with no `-e`, so a dash-leading marker is parsed as an option
  today: add `-e` before the marker. The check-wiring fragment's marker is `check-wiring.sh`, the
  procmon SessionStart sibling's is `procmon-hook.js`; the re-match is scoped to marker AND event,
  so sharing a basename across events is safe.
- **Arguments render as unquoted argv tokens joined by single spaces**, the shape the live
  `bash "${CLAUDE_PROJECT_DIR}/tools/check-wiring.sh" --session` entry already has, so a marker is a
  substring under the merger's plain view and under the stripped one. The repath compares the
  whole rendered command.
- **`merge()` finds a group by exact matcher and appends into it**: the two entries sharing
  `startup|resume|clear` share ONE group, so the four fragments yield THREE SessionStart groups;
  AC3 asserts entry-set equality per group across the three application orders, never
  byte-identity of the file.
- **`{here}` is the fragment's own directory in all three readers.** The destinations leg judges a
  `{here}` fragment at its adopter path: the directory must be the `home` of at least one
  `kind = "flat"` descriptor — ten declare `home = "tools"`, one declares
  `home = "skills/session-kickoff"` — and `{prefix}/<basename>` is compared against the whole
  declared set, both spellings printed. `check-wiring.sh` gets ONE `resolve_fragment_hook` helper
  replacing its two inline resolvers, plus `--resolve-fragment <path>`, twinned on
  `settings-merge.py`; the parity arm compares the two verbs' output over every tracked fragment.
- **The descriptors**: `tools/govkit/entries/kickoff-manifest.kit.toml` gains a rule shipping the
  two card fragments to `{prefix}/{relpath}`; `check-wiring.kit.toml` adds
  `check-wiring.fragment.json` to its include list AND to that rule's `claims`, because
  `govkit.py`'s rule 4b reds a rule whose resolved destination is not among its claims;
  process-monitor's `**` rule covers its sibling. `python tools/govkit/govkit.py selfcheck` is the
  gate and `plan --target <scratch> --kits kickoff-manifest,check-wiring,process-monitor` the
  observation; there is no `--dry-run`.
- **The procmon SessionStart fragment is aReapedSpinner's R8 residue**
  (`memory/builds/aReapedSpinner/reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round2.md`
  lines 236–248): `tools/process-monitor/adopt-process-monitor.sh:203`'s remediation names both
  fragments and its wiring count at line 193 becomes per event.
- **`.claude/settings.json` is produced by the merger, never by hand**, and its edits are picked
  up live: every SessionStart group carries a matcher afterwards and exactly one carries
  `compact`, the replay's. Your own session is unaffected until its next compaction, which then
  writes a replay-origin card the deny allows. The file is `eol=lf`-pinned; `check-wiring.sh`'s
  `eol` arm grades it.
- **`WIRE-INTO-PROJECT.md` lines 610–612** ("`settings-merge.py` handles only the agent-cap block —
  add SessionStart by hand") are REPLACED by the fragment step, not appended to.
- **AC9 — one forced compaction replaying the card — is the ORCHESTRATOR's to observe** in a
  session started after this unit lands; a sidechain cannot compact a session. Write the ledger
  line naming what the orchestrator observes, and say so in your return.
- **Names are graded**: the shell helper leads with `resolve`; the python `render_command`
  replaces `_command`; `set_group` if the re-match is extracted. Function definitions in
  `check-wiring.sh` are parsed by the lexicon leg.
- **The manifest owes nothing here** unless you touch a watched path; `tools/gate-legs.json` is
  watched and this unit does not edit it.
- **The acceptance ledger** is `2026-09-14-build-TOOL-aReplayedCard-2-1-acceptance-ledger.md` under
  `build/`, `**Serves:** journal TOOL-aReplayedCard-2`, AC1–AC9 with every backticked token on the
  bullet's first physical line; every new arm observed RED first and the ledger says how.
- **Author with the Write tool, LF.** Finish with the records: spec status CLOSED with today's
  date, `gen_build_index.py --write`, `git add -A`, the hygiene gate (minutes, never through
  `tail`), `python tools/check-spec-tokens.py`, `python tools/settings-merge.py --selftest` or its
  self-test entry, `bash tools/check-wiring.test.sh`, `bash tools/check-hook-destinations.sh`,
  `python tools/govkit/govkit.py selfcheck`, `bash tools/check-wiring.sh --check`, and commit with
  the unit id in the subject. No push, no merge.
