**Serves:** research PLAY-dOrderedCharter-6

# Brief: spec 6 — the builder's hand-back on the drive rows gov selects

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 6's builder handed back a divergence before writing any code, and every later unit consumes from unit 6 directly
or through another unit, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 6 so a builder can build it as written over this tree, resolving the two conflicts below by the fork rule.

### Items

1. **AC2's gov half cannot pass under S3.** S2 seeds `[[drive]]` rows in the `run-gates` descriptor, among them the `gate-bar` stage's
   row; S3 says a kit the target did not select contributes nothing; AC2 says the render against gov holds every seeded row. Gov's
   `.governance/deploy.toml` selects 22 kits and `run-gates` is not one of them, so the gate-bar row never reaches gov's charter. The
   builder named three ways out; weigh them under the fork rule, and record the pick in section 8:
   - gov's `.governance/deploy.toml` gains `run-gates`, with that file in Files touched. The file says it carries every owner decision
     for gov's render, so test whether this option trips a veto before choosing it;
   - AC2's gov half reads every seeded row of a kit gov selects, and says run-gates' rows render only where run-gates is selected;
   - the `gate-bar` row moves to a kit gov selects, such as `push-main`, and S2's kit list drops `run-gates`.
2. **A selected flat entry without a descriptor.** Section 5 says a render refuses when a selected kit's descriptor cannot be found. S3
   ships flat-entry descriptors beside the engine through `root_relative` `[[files]]` rules in `tools/playbook/kit.toml`, but does not say
   whether every flat entry ships one or only the two with rows (`kickoff-manifest` and `push-main`). An adopter whose template carries the
   drive token and who selects another flat entry (`check-wiring`, `settings-merge`, `check-line-length`, and others) would be refused. Pin
   which flat entries ship a descriptor, or say that a selected kit without one contributes nothing, and make section 5, S3 and the
   acceptance agree.
3. **Carry the brief's rename.** Unit 6's build brief also takes the rename of unit 3's `plant_envelope_text`; if the spec's Files touched
   does not already list `tools/playbook/instruction_units.py`, it does, and S4 already edits it.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-08, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- The spec builds as written over HEAD, and each change has a history line.
- Your return names the pick for each conflict, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec. No change to gov's kit selection unless the fork rule picks it and no veto trips.
