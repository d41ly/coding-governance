**Serves:** research TOOL-dMindYourWords-34 TOOL-dMindYourWords-37

# Promoted-fix brief — dMindYourWords, the round-2 promotions' mechanical reds

The round-2 spec audit's disposal authored eight promoted units, TOOL-dMindYourWords-30 to -37, under
`memory/builds/dMindYourWords/spec/`, staged and NOT committed. The main loop ran `tools/check-spec-tokens.py` over them
and every red below is a finding in exactly one spec. Fix each in place, in the spec it names, and nothing else: no
design change, no new scope, no edit to a spec this list does not name. These specs have never been committed, so a
fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit; its paths rule is the one these break.

## A suite named as an acceptance observation

- TOOL-dMindYourWords-34: an acceptance criterion names `tools/govkit/selftest.py` (§6, near line 122). Observe the
  checker on its staged break or a fixture of the unit's own code instead, and keep the suite arm on a `New arm:`
  line in §7. Its §2 and Files touched may keep naming the file.

## Paths the check reads as citations of tracked files

- TOOL-dMindYourWords-37, AC8: `memory/project/lexicon-debt.txt` is a path the criterion asserts is ABSENT, and the
  check reads it as a citation of a tracked file. Keep the observation, spelled so the check does not read a path:
  a glob pathspec such as `'*lexicon-debt.txt'` was the fix the round-1 pass used for the same case.
- TOOL-dMindYourWords-37, AC20: `requirements/dev.txt` and `../requirements.txt` are planted fixture paths. Spell them
  as the fixture's own relative paths so the check does not read them as repository citations, as the earlier fix
  pass did with a `<fixture>/` prefix.
- TOOL-dMindYourWords-37, AC20: `{prefix}/memory-tree/build_records.py` is an install-prefix placeholder, not a
  tracked path. Cite it by basename in §6 and keep the full spelling in §2, §4 and Files touched.

## How to verify

Stage your edits under `memory/builds/dMindYourWords/` (`git add`, never commit), then run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25`, the one gate your role admits, and repeat until it
prints no finding on a dMindYourWords spec. The main loop re-runs `check-spec-tokens.py` after you return; its hits
above are stated whole, so fix them by reading. Return each finding with what you changed, and any you could not fix
with the reason.
