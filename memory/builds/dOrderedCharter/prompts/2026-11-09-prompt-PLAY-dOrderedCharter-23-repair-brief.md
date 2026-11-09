**Serves:** research PLAY-dOrderedCharter-23

# Brief: spec 23 — the builder's hand-back on the attended route's drive row

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 23's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 23 so a builder can build it as written over this tree, resolving the conflict below by the fork rule.

### Items

1. **The `/build` drive row S2 rewrites does not exist.** S2 and the design's row block rewrite the `when` of "the row unit 6 seeds for
   /build" in `tools/roles/kit.toml`. At HEAD that descriptor holds three drive rows, none with a `/build` command, and no descriptor
   anywhere has one: unit 6's seeded rows never named it. The spec also says the unit rewrites rows and never adds one. The builder named
   two ways out; weigh them under the fork rule and record the pick in section 8:
   - S2 and the design declare a new drive row in `tools/roles/kit.toml` with command `/build`, a named stage and role, the `when` the spec
     already gives, and its place in the drive order; the inventory's "no new name", the rollout's two-line claim about gov's charter and
     AC2 follow;
   - S2, AC2 and fork F2 drop the attended-route row, leaving the exception to the charter's existing tools line naming `/build`.
2. **S1's command.** The unattended kit's `start` row exists with command `/unattended`; the spec's `/unattended <slug>` changes it, which
   the spec allows. Say so where S1 states the row.
3. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks. Every new fact a record states is pinned, keyed or marked PINNED or DERIVED.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- The spec builds as written over HEAD, and each change has a history line.
- Your return names the pick, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec.
