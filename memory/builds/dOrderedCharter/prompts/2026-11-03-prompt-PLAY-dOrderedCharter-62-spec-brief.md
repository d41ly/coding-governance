**Serves:** research PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-17

# Brief: PLAY-dOrderedCharter-62 — the layer check resolves `{prefix}` in a flat entry's optional part

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 17's builder (run wf_2c160031-b97) returned
`DIVERGENCE:` before writing code: for a flat govkit entry (home `.`, under `tools/govkit/entries/`),
`tools/playbook/check_layers.py:321-323` compares an `optional` row's `part` against the edge's full repo path, since
`read_descriptors` (`:145`) gives every entry home `None`. So only `part = "tools/push-main.sh"` allows that file's
edges, and `tools/check-install-prefix.sh`'s GOVPFX rule (`:386`, zero-tolerance per its header `:24-27`) counts that
spelling in a `.toml`. `{prefix}/push-main.sh` passes the ban, and the check never resolves it. Units 16 and 61 are
CLOSED, so the check's correction is a new unit on top (BUILD-METHOD M4), and spec 17 is revised to consume it.

## The brief

### Goal

Author the spec of PLAY-dOrderedCharter-62, so an `optional` row's `part` in a flat govkit entry is spelled
`{prefix}/<file>` and the check resolves it to the tool root, as `read_descriptors` already does for `include`; and
revise spec 17 so its flat-entry rows use that spelling.

### Items

1. **Spec 62's scope.** `check_layers.py` resolves a leading `{prefix}/` in a flat entry's `part` to the tool root
   before comparing, by the same resolution `read_descriptors` applies to `include` (one reader, charter
   `[one-fact]`); a `part` spelled `tools/<file>` in a flat entry is refused by name, so the ban and the check cannot
   disagree silently. Verify every line cited above at HEAD first. ACs are fixture plants of the check (a flat entry
   allowing `{prefix}/x.sh` turns its edge allowed; a literal `tools/x.sh` part is refused), each observable without a
   gate; New arms on `New arm:` lines.
2. **Spec 62's header.** Tier-2, status `DEFERRED`, `order 3`, `streams playbook`, `base 8bec4cef`, `advances
   PLAY-dOrderedCharter-38`, and `**Derived:** PLAY-dClosedLoop-2` on its own line under the Status line; §3 Edges
   `consumes-from PLAY-dOrderedCharter-61` and `hands-off PLAY-dOrderedCharter-17`.
3. **Spec 17.** Add `consumes-from PLAY-dOrderedCharter-62` to §3 Edges; S8 says a flat entry's `part` is spelled
   `{prefix}/<file>`; §4's flat-entry rows (`tools/push-main.sh` `:869` `:964` `:994`, `tools/push-main.test.sh:1372`,
   `tools/check-install-prefix.sh:321`, `tools/check-install-prefix.test.sh` `:63` `:65` `:253` `:254`,
   `tools/check-kit-versions.sh` `:243-252`, `tools/check-wiring.sh` `:700` `:1101` `:1103`,
   `tools/check-wiring.test.sh:280`, `tools/settings-merge.py` `:620` `:711`) use it. Bump its rev with a §9 line
   naming this brief.

In every spec you write or revise:

- Follow `memory/TEMPLATE-SPEC.md`; §10 names the seam and the recall terms you used.
- Verify every path, count and line you cite against the tree at HEAD.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in the new spec file `memory/builds/dOrderedCharter/spec/2026-11-03-spec-PLAY-dOrderedCharter-62.md`,
  spec 17 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new spec's path, its AC list in one line each, and spec 17's new rev.

### Acceptance

- `grep -n '^# PLAY-dOrderedCharter-62'` prints the new spec's H1; its Status line reads `DEFERRED` with `order 3`.
- `grep -n 'consumes-from\*\* `PLAY-dOrderedCharter-62`'` prints spec 17's edge.
- `grep -c '{prefix}/' ` over spec 17's §4 counts every flat-entry row.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 62 and 17; specs 16 and 61 stay frozen; the install-prefix ban is not relaxed.

### Limitations

The items above, "For the run".

### Reuse

`read_descriptors`' `{prefix}` resolution for `include` in `tools/playbook/check_layers.py`; `tools/check-install-prefix.sh`'s
GOVPFX rule as the spelling the check must accept.
