**Serves:** research PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7

# Brief: drift sweep A — specs 47, 48, 25, 7 read against the code at HEAD

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03, approving a read-only drift sweep of the next DEFERRED specs against the code at HEAD
(`memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-38-owner-speedup.md`). This is a drift
probe, not a spec-audit round: it records no review round and files no spec-audit record.

## The brief

### Goal

For each spec below, list every place it no longer matches the tree at HEAD, so one spec-writer pass can fold the
drift before the unit dispatches and its builder does not hand back a divergence.

1. Read each spec whole, then check it against the code at HEAD. These are the specs:
   - `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md`
   - `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md`
   - `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md`
   - `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md`
2. Read the build's landed units first, by their builder returns in `memory/builds/dOrderedCharter/build/*-builder-return.md`
   (units 18, 16, 61, 62, 17, 19, 10, 44, 22, 51, 24, 63, 28): they moved what these specs assume. Earlier divergences
   were of these kinds, so look for each: a path, function, table, key or line a spec cites that moved or does not
   exist; a count pinned at `ce13efbe` that changed; a contract a closed unit built differently (`tools/playbook/tag_index.py`,
   `gov_tag.py`, `edge_grammar.py`, `edges.toml`, `namespaces.toml`, `layers.toml`, `check_layers.py`); a check whose
   first run over the real tree would red (run the spec's own predicate read-only where you can); a §7 leg line
   missing a leg whose guard in `tools/gate-legs.json` a Files-touched path trips; an AC that observes a suite, a bar
   or a gate leg; a new leg whose dossier claim the spec hands to a later unit (the codebase-map gate refuses that
   commit); a guard widening that would red a live spec outside this build.
3. For each finding give: the spec and section, what the spec says, what the tree has (path and line), and whether it
   is LOCAL (a fold of that spec) or needs a new mechanism. A spec with no finding says so.

Done means every spec above has a findings list or an explicit "no drift found", each finding with a tree path and
line. Return the findings; write nothing.

### Items

The goal above.

### Acceptance

- Every spec above has a findings list or an explicit "no drift found", each finding with a tree path and line.

### Gates

None: read-only.

### Non-goals

No write anywhere in the repository; no gate, suite or bar; no finding about a spec not listed; temporary files only under the session scratchpad `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`, and every command bounded.

### Limitations

- Temporary files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Bound every command; a probe that does not return in its bound is skipped and named.

### Reuse

The builder returns named above; `tools/check-spec-tokens.py --legs-for` for which legs a path trips.
