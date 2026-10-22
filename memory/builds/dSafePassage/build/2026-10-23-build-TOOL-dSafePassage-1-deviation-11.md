# TOOL-dSafePassage-1 deviation 11 — a step row's introducing commit is derived, never typed

**Serves:** deviation TOOL-dSafePassage-1

- **Departs from:** `cl-dClosedLoop-0018@ed08a364` [the row's fields]
- **Hand-off:** design-to-spec
- **Before:** a kit descriptor's `[[upgrade]]` row (id, introducing commit, up and down argv run from gov's checkout, witness, surfaces, whether it needs the target's code) and the registry's `[[retired]]` succession rows, every step row frozen once it lands on the default branch: its id, introducing commit and argv compared with the landed row
- **After:** a kit descriptor's `[[upgrade]]` row (id, up and down argv run from gov's checkout, witness, surfaces, whether it needs the target's code), its introducing commit derived by the one reader as the oldest commit on the default branch's first-parent line whose tree holds the row, and the registry's `[[retired]]` succession rows, their retiring commit derived the same way, every step row frozen once it lands on the default branch: its id and argv compared with the landed row, and its derived introducing commit equal by construction
- **Cause:** design defect
- **Reason:** A row cannot name the commit that lands it, because that commit's id is a hash over the tree that holds the row. Any other typed commit is a second copy of a fact git owns, which can disagree with it (charter `[derive]`), and the clause's frozen comparison would red on the first row it carries. The reader still returns `introduced` for every row, so the walk, the receipt's `steps` rows and the frozen leg read the brief's spelling unchanged.
- **Evidence:** TOOL-dSafePassage-1 §8 F2 and §4 Data model; the spec brief's S1 and S2 (`memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md:72-80`)
- **Risk:** stricter
- **Approver:** author, TOOL-dSafePassage-1 §8 F2, under the chain's `author-recorded` value
- **Follow-through:** amends cl-dClosedLoop-0018@ed08a364
- **Caused-by:** TOOL-dSafePassage-1
