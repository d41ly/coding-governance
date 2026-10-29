**Serves:** research TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-29

# Promoted-fix brief — dMindYourWords, the round-1 promotions' mechanical reds

The round-1 spec audit's disposal authored eight promoted units, TOOL-dMindYourWords-22 to -29, under
`memory/builds/dMindYourWords/spec/`, staged and NOT committed. The main loop ran `tools/check-spec-tokens.py` over them
and every red below is a finding in exactly one spec. Fix each in place, in the spec it names, and nothing else: no
design change, no new scope, no edit to a spec this list does not name. These specs have never been committed, so a
fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit; its paths rule is the one these break.

## Paths the check reads as citations of tracked files

Each is a file a unit of this build or a parent will CREATE, so it is not tracked at HEAD. Keep its full path in §2,
§4 and Files touched, and cite it by its basename in any section the check reads as a citation, §6 above all.

- TOOL-dMindYourWords-24: `.governance/install.json`.
- TOOL-dMindYourWords-27: `memory/project/lexicon-debt.txt`, `tools/govkit/steps/lexicon_pin_ledger.py`.
- TOOL-dMindYourWords-29: `tools/lexicon/legacy_ledger.py`, `tools/lexicon/lexicon_signals.py`,
  `tools/lib/extract_code.py`, `tools/govkit/upgrade_steps.py`, `tools/lexicon/coverage_join.py`.

## A suite named as an acceptance observation

- TOOL-dMindYourWords-29: an acceptance criterion names `tools/lexicon/selftest.py`. Observe the checker on its staged
  break or a fixture of the unit's own code instead, and put the suite arm on a `New arm:` line in §7.

## How to verify

Stage your edits under `memory/builds/dMindYourWords/` (`git add`, never commit), then run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25`, the one gate your role admits, and repeat until it
prints no finding on a dMindYourWords spec. The main loop re-runs `check-spec-tokens.py` after you return; its hits
above are stated whole, so fix them by reading. Return each finding with what you changed, and any you could not fix
with the reason.
