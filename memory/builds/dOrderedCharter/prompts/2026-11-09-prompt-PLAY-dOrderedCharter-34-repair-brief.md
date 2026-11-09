**Serves:** research PLAY-dOrderedCharter-34

# Brief: spec 34 — the builder's hand-back on the census and the project block

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 34's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 34 so a builder can build it as written over this tree.

### Items

1. **The census and the core meta-check.** The practice catalogue reads a row's `rules` as `<tag>.<rule>` tags that a leg's `enforces`
   pairs with, and `tools/playbook/core.py#check_meta` joins them. Read that way, the census predicate rules `practice.writing` gov-only:
   its line names no path, every leg enforcing its rules is an exempt leg in `tools/govkit/registry.toml`, and no role cites it. S8 then
   moves its row, leaving its rule tags in `tools/gate-legs.json` that no row holds, which the meta-check reds, and that check refuses an
   `enforces` tag outside the principle and practice namespaces. Say which reading of "a leg names its tag in `enforces`" the census uses,
   exact tag or tag plus its rule tags; under the second, what happens to a moved row's rule tags and its pending rows, with
   `tools/gate-legs.json` among S8's readers. Under the first, say why a row whose rules four legs enforce reads as having no evidence.
2. **The project block and `adopter_rules`.** Any moved row becomes a level-0 `repo.` unit in gov's overlay, and composition step 2 stops
   rendering `[charter] adopter_rules` once the overlay holds one. Gov's adopter rules reach the overlay only through unit 31, which
   builds after this unit, so they would drop out of gov's charter, against AC1 and S1. Say either that the project block renders the
   adopter rules beside the level-0 units until unit 31 converts them, or that this unit converts gov's own adopter rules itself.
3. **Level-3 placement.** No template holds a unit slot or a repo marker pair; S2 and step 3 do not say which level-3 document a level-3
   `repo.` unit renders into, nor how the marked part avoids printing a unit twice. `tools/playbook/overlay.py#derive_slot_units` already
   places an edge-free `repo.` unit into any slot its scope selects; say whether this unit reuses it.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks. Every new fact a record states is pinned, keyed or marked PINNED or DERIVED; a number
  beside a unit or spec number reads as a fact, so name a unit by its id. Every function name it mints passes
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 34 builds as written over HEAD, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec, except a mirrored edge on spec 31 if a pick hands it work.
