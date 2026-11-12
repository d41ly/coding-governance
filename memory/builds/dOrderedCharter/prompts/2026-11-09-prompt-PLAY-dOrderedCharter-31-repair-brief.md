**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 — the builder's hand-back on the project block's row and an empty population

## The prompt

> interrupted, rearm and resume unattended

— owner, 2026-11-09. Unit 31's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 31 so a builder can build it as written over this tree, with unit 34's CLOSED renderer left as it landed.

### Items

1. **The `ADOPTER_RULES` placeholder row.** S4 and the rows design take the row out of `tools/govkit/entries/playbook.kit.toml` with the
   `adopter_rules` key, and AC7 needs `charter-key:ADOPTER_RULES` to vanish. At HEAD `tools/playbook/render_playbook.py#render` refuses a
   template token with no row, the template still holds `{{ADOPTER_RULES}}`, and `#build_project_block` takes that row for its key and its
   default bullet, the only route level-0 overlay units render through. Removing the row breaks every render; removing the token leaves the
   step's level-0 units nowhere to render. Weigh under the fork rule:
   - the row stays, the step's `surfaces` names a member that does vanish, such as the deploy answers' `[charter] adopter_rules` key under a
     reader of its own, and AC7 is restated to match;
   - the project block stops reading a row, which changes CLOSED unit 34's mechanism and so is a new unit on top, not this one.
2. **AC10's empty population.** Unit 34's census record moves nothing, and the step gate registers no `unit` class (unit 33 deferred it
   to PLAY-dOrderedCharter-40's first gov unit row). There is no change record to write and no class or member to see red. Say so, and
   move AC10 to the unit that registers the class, or restate it so it observes something real; an empty population read as coverage
   is refused.
3. **What the builder found for the rebuild**, to fold where they belong:
   - the `budgets-cap-codex-instructions` case in `tools/policy/check_policy.py` runs the agent-instructions adopter; once the cap's enforcer
     is the renderer, it needs a render plant over a template larger than the Codex limit;
   - the `kit` and `installed` keys of that cap's row in `tools/policy/caps.toml` also name the agent-instructions kit;
   - with the seed rule gone the `playbook` entry ships no files while its `version_from` and placeholder hole still name the template; say
     whether the govkit selfcheck accepts that, from a probe.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks, and a Readers clause names readers only, never the command that found them. Every new
  fact a record states is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it mints passes
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 31 builds as written over HEAD, every edge it gains is mirrored, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it, its Readers check included.

### Non-goals

- No code. No edit to a CLOSED spec. No edit to another spec but a mirrored edge on spec 40 if AC10 moves there.
