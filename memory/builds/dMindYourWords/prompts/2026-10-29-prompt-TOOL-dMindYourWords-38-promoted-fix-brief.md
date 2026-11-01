**Serves:** research TOOL-dMindYourWords-38 TOOL-dMindYourWords-40 TOOL-dMindYourWords-48 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52

# Promoted-fix brief — dMindYourWords, the round-3 promotions' mechanical reds

The round-3 spec audit's disposal authored fifteen promoted units, TOOL-dMindYourWords-38 to -52, under
`memory/builds/dMindYourWords/spec/`, staged and NOT committed. The main loop ran the hygiene gate and
`tools/check-spec-tokens.py` over them, and every red below is a finding in exactly one spec. Fix each in place, in
the spec it names, and nothing else: no design change, no new scope, no edit to a spec this list does not name. These
specs have never been committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit.

## Hygiene check 25 — a retirement with no `**Readers:**` clause

- TOOL-dMindYourWords-40, §2 S1 retires a named thing and carries no `**Readers:**` clause. Write one: `by name:` and
  every reader that spells the name, then `by value:` and every reader of its value, or `NO VALUE READERS` and a
  reason; find each reader with `git grep` over the tree, never from a record. If S1 retires nothing, reword it so
  no retirement word ("drops", "retired", "replaces") sits beside a backticked token.

## Paths the check reads as citations of tracked files

Each is a planted fixture path, an install-prefix placeholder, or a file a unit of this build creates. Keep its full
spelling in §2, §4 and Files touched where it belongs there, and in §6 cite it so the check does not read a tracked
repository path: by basename, with a `<fixture>/` prefix for a planted path, or as the earlier fix passes did.

- TOOL-dMindYourWords-38: `{prefix}/demo/reader.py`.
- TOOL-dMindYourWords-48: `tools/lexicon/lexicon_signals.py` (unit 16 creates it).
- TOOL-dMindYourWords-51: `govkit/registry.toml` reads as a root-relative path that does not exist; the tracked file
  is `tools/govkit/registry.toml`. Spell it whole.
- TOOL-dMindYourWords-52: `requirements/x.txt`, twice (a planted fixture path).

## Legs a §4 files-touched path trips and the §7 leg line omits

- TOOL-dMindYourWords-52: `recall floor` and `recall floor arms`, both from `memory/HYGIENE.md`. That file is a render
  of `HYGIENE.template.md` and is never the edit: name the source the unit edits and the render as its copy, and add
  the two legs to §7's leg line if the unit's edit still trips them.

## How to verify

Stage your edits under `memory/builds/dMindYourWords/` (`git add`, never commit), then run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25`, the one gate your role admits, and repeat until it
prints no finding on a dMindYourWords spec. The main loop re-runs `check-spec-tokens.py` after you return; its hits
above are stated whole, so fix them by reading. Return each finding with what you changed, and any you could not fix
with the reason.
