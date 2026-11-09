**Serves:** research PLAY-dOrderedCharter-36

# Brief: spec 36 — the builder's hand-back on a refused name and four gaps

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 36's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 36 so a builder can build it as written over this tree.

### Items

1. **`classify_patch` fails the naming lexicon** (`classify` is not a declared verb). Rename it `derive_patch_class`, which passes, in
   the inventory and wherever S5 names it.
2. **Placeholder catalogue rows.** S4's exclusion walk reads tag-valued policy rows, and some rows are named with placeholders, such as
   `roles.effort.<role>`; `policy.py get` on such a name exits 2 because it is no TOML key, and the spec reads an exit 2 as a refusal.
   Say whether placeholder rows are skipped or their instances are listed, and from where.
3. **The composer's signature.** S7 calls `check_rows(kind, schema, composition, exclude, policy)` from
   `tools/playbook/overlay_rows.py#derive_row_composition`, which takes no `policy` and returns nothing `derive_widenings` can read the
   classified operations from. State the composer's new parameter and return value, what `composition` means to `derive_widenings`, and
   what `policy` is and where the fixture's `--policy` value merges in.
4. **AC8's plant.** S2 makes a field that declares neither key fixed, so a field with no `widens` cannot be open. Restate the plant, for
   example as a field declaring `widens` with no direction, which the reader's direction refusal catches.
5. **Unit 35's closed plants.** The data model breaks plants in `tools/playbook/fixtures/row_kind.py` that unit 35 closed on: a gov row's
   value falls outside the declared order, a patched row becomes the fixed one, and one plant's tree equals this unit's
   `exclude-needed` with the opposite exit. Say how each of those plants changes, so this pass does not silently rewrite what a closed
   unit's acceptance observed, and record each change as this unit's.
6. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

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

- Spec 36 builds as written over HEAD, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec.
