**Serves:** research PLAY-dOrderedCharter-28

# Brief: unit 28's divergence — the resolve-section plant's edge type

## The prompt

> Try again

— owner, 2026-11-03, after unit 28's first builder died on an API network error. The retry (run wf_ae4be551-417)
returned `DIVERGENCE:`: spec 28's §4 "### The resolve plants" gives `resolve-section` as
`implements=doc.build-method#m5-recall-and-reuse`, and AC6 says it exits 0. Unit 24's committed `implements` row in
`tools/playbook/edges.toml` has `to = ["feature", "spec"]` (the memory plan's `[edges]` table), so a `doc` section
target is red: `implements=doc.build-method#m5-recall-and-reuse · is outside implements's to [feature, spec]`.

## The brief

### Goal

Revise spec 28 so the `resolve-section` plant uses a registered type whose `to` admits a `doc` section, and AC6 can pass
as written.

### Items

1. **The plant.** In §4 "### The resolve plants" and wherever else spec 28 spells it, write the plant as
   `part-of=doc.build-method#m5-recall-and-reuse` (`part-of`'s `to` is `any` in `tools/playbook/edges.toml`), or another
   registered type whose `to` admits a `doc` section, verified against that file. Leave `implements` and every unit-24
   row untouched (§3).
2. **AC6** reads true for the revised plant; nothing else in the spec changes.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-03, and add one §9 line naming this brief. The status stays as it is
  in the working copy (`INPROGRESS`, set by the builder); do not move it.
- Verify every name you cite against the tree at HEAD.

For the run:

- Writes stay in spec 28 and the files `gen_build_index.py --write` rewrites.
- Do not commit and run no check: the main loop commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new rev and the plant's line as it now reads.

### Acceptance

- `grep -n 'resolve-section'` over spec 28 prints no `implements=doc.` target.
- The Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 28; `tools/playbook/edges.toml` stays as unit 24 built it.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/edges.toml`'s rows as unit 24 built them.
