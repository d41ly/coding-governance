**Serves:** journal KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

# Cross-read handoff — aOrientedCast's eleven specs, before the first code pass

## Role

You are a specification reviewer. You are checking whether a set of unit specs written by
different authors AGREE with each other and with the interfaces they were all handed. You write
nothing and change nothing. Your output is a list of disagreements, each one concrete enough that
an author can fix it without asking you a question. Every disagreement is a defect in exactly ONE
document, and you name that document. You leave out praise, summaries of what the specs do, style
remarks and anything outside the four axes below. "No disagreement on this axis" is a valid answer,
and you state it.

## Task

**The set.** The eleven files under `memory/builds/aOrientedCast/spec/` at HEAD in
`C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**What they were all handed.** The section "Pinned interfaces" of
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`. Read
it first: it is the contract every spec was told to spell identically.

**The rule.** `memory/guides/BUILD-METHOD.md` M2, the paragraph beginning "Sub-specs must AGREE".
Its four axes:
1. **Scope.** Nothing one spec puts IN is OUT in a sibling.
2. **Interface.** Any name, path, CLI verb or flag, front-matter key, input key, JSON key, file
   shape or harness argument spelled in two specs is spelled identically, and matches the pinned
   interfaces. Check every place one unit HANDS OFF to or CONSUMES FROM another: the `§3 ### Edges`
   lines on both ends must name the same thing.
3. **Ordering.** No spec depends on a unit sequenced after it, by the `order` verbs in the status
   headers. One owner ruling changes the headers as written: `TOOL-aOrientedCast-8` moves to order
   7, and `PLAY-aOrientedCast-1` to order 8. Grade ordering against those values.
4. **Acceptance.** The build brief's acceptance (each mechanism RED on a staged break and then
   GREEN; an attended dry run renders a handoff from a card; the write gate refuses an inline spec
   write) is implied by the union of the specs' `§6`.

**Also report, as their own sections:**
- every `§8` item in every spec, with its state: RESOLVED, FACT-QUESTION, or open;
- any `§6` criterion that runs the merge bar, a `GATE_*=` prefix, or a whole `*.test.sh` suite;
- any `§6` criterion that names, as a backticked path, a file its own unit creates.

**Bounds.**
- Read-only. No write anywhere in the repository.
- Bound every command: no merge bar, no suite.
- Temporary files go under
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-deterministic-attended-workflows-943570/e131d82c-aaf3-45ad-abb9-258d7ab9ad1b/scratchpad`.

**Return.** Markdown with these sections:
- `## Disagreements`: one bullet each, carrying the axis; both `file:line` locations; what each
  says; which ONE document is wrong and why; and the fix in one sentence.
- `## Open questions`
- `## Suite criteria`
- `## Self-created paths in §6`

An empty section reads `none`.
