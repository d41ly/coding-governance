**Serves:** research PLAY-dOrderedCharter-32

# Brief: spec 32 — the builder's hand-back on three seams that are not landed

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 32's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 32 so a builder can build it as written over this tree, and mirror each edge it gains in the spec at its other end.

### Items

1. **AC8's `policy.adopter.<seg>` tag.** No `policy` namespace is registered in `tools/playbook/namespaces.toml`: `gov_tag.py show
   policy.adopter.release-train` resolves to no row. Unit 10's spec gives the `policy` word to dDeclaredLoop, whose crosscheck record places
   the catalogue in that namespace in TOOL-dDeclaredLoop-18, not landed. Either drop or defer the `policy.adopter.` half of AC8's last
   clause, observing only that the overlay's policy key is read for its tag, or add a consumes-from edge on TOOL-dDeclaredLoop-18 and say
   the clause is owed until it lands. A builder may not register a namespace this spec does not design.
2. **S5's `fixed-by` grammar is unit 36's.** S5 and the derived-class design reuse the source grammar spec 36 declares for rows, and section
   10 names it as a seam, but unit 36 builds later than this unit, unbuilt, with no edge either way. Either this unit lands the grammar it
   needs and hands it to 36, which mirrors it as consumes-from, or S5's grammar moves after 36.
3. **S4 reads `instructions.exclude` through unit 35's reader.** Unit 35 builds later, unbuilt, and section 3 makes that reader 35's. Say
   how this unit reads the key until 35 lands, for example through the landed catalogue row and `policy_value.read_policy_value`, with 35
   re-pointing it later.
4. **S7's guard edit.** Adding the overlay to the legacy inputs in `tools/policy/policy.py` already records its blob, which the mirror guard
   and the mirror hook read; drop `tools/policy/guard.py` from Files touched if no edit there remains.
5. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8. Where a pick hands work to unit 35 or 36, edit that spec's edges and
the item it now owns to match, with its own history line; touch no other spec.

In each spec you change:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks. Every new fact a record states is pinned, keyed or marked PINNED or DERIVED.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 32 builds as written over HEAD, every edge it gains is mirrored, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to a spec other than 32, 35 and 36.
