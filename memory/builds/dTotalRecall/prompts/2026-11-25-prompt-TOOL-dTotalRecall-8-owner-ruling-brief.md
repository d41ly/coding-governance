**Serves:** journal TOOL-dTotalRecall-8 TOOL-dTotalRecall-37 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26
**Caused-by:** TOOL-dTotalRecall-109

# Brief — dTotalRecall: the owner's answers to asks TOOL-dTotalRecall-109 and TOOL-dTotalRecall-111

## The prompt

> redesign the record under a bound it can meet, run the replay again with more runs per arm. Why weren't those decisions made under the unattended protocol?

— owner, 2026-11-25, in this run's session on node a, answering the two asks the run named as held. It lifts the resume
prompt's rule that TOOL-dTotalRecall-8, -37, -14, -15 and -26 are never built, for what these answers name.

## The brief

### Goal

Spec TOOL-dTotalRecall-8 is re-specced, at its next rev, as a code record redesigned under a bound it can meet, so that a
builder pass can build it; TOOL-dTotalRecall-37's spec is revised where its premise moves with it.

### Items

1. Read the spec, the deviation records of the unit, and the first builder return
   `2026-11-22-build-TOOL-dTotalRecall-8-1-builder-return`: the record measured 10884519 bytes cold in 10.80 s against
   the clause's 1 MB and 30 s lines, and the smallest parts measured alone were 1255628 (file paths), 850731 (definitions)
   and 2318591 (call edges), each DERIVED there. The draft patch it names stands on node d, not here.
2. Read cl-dClosedLoop-0219 and what reads the record: the gaps, the owned nodes `record-kind.code` and
   `policy-key.memory.code-languages`, and the child builds' readers. The redesign serves every reader the clause names, or
   says which one it drops and why the record still closes the gap.
3. Redesign first, bound second. Choose the smallest faithful record: say what each part serves and cut what no reader
   reads, derive what the index can derive at read time, and store references where a blob already holds the text. Then
   MEASURE the redesigned record on gov's tree with a probe, in a scratch directory, and set the bound from that
   measurement with stated headroom. Never set a bound a probe did not meet, and never the old 10 MB record under a raised line.
4. The bound's change is a departure from the clause: write it as the deviation record the build's values call for,
   `report` and `author-recorded`, its approver the owner by this brief's prompt, its `relaxes:` value naming the old line
   and the new. Re-pin the spec's Carries to the as-built view's hash after it.
5. State the loss route again: what happens when the built record misses the NEW bound. It must not uncover the clause.
6. The grammar and checks of a build spec: `--check-specs`, `check-spec-tokens.py --spec`, hygiene check 12 over each spec
   touched. Run no gate leg. Every number carries an id, a blob-pinned path, PINNED or DERIVED.
7. Your write grant is specs 8 and 37 and the one deviation record; read this brief's own Limitations at `memory/builds/dTotalRecall/prompts/2026-11-25-prompt-TOOL-dTotalRecall-8-owner-ruling-brief.md` before the first edit.

### Acceptance

The spec states a record whose bound a probe met, with the probe's command and figures, and every reader of the clause is
served or dropped by name. The commands name no finding.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No probe left in the tree. Spec 17 and the map's units are another brief's.

### Limitations

The write grant is specs 8 and 37 and the one deviation record. The status of each stays `DEFERRED` until the main loop
re-opens it. Do not commit. A worktree-isolated session refuses an inline command that embeds git: put it in a script
file. Scratch goes under `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u8/`.

### Reuse

Unit 13's shared extraction primitive, unit 9's section read and the one tag index, each landed by this build.
