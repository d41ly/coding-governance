# TOOL-dDeclaredLoop-36 deviation 363 — the count word that opens the section the new upgrade bullet joins

**Serves:** deviation TOOL-dDeclaredLoop-36

- **Departs from:** `TOOL-dDeclaredLoop-36@rev-3` [§2 S2]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-36`'s spec at rev-3 has `help/upgrade-steps.md` gain a bullet for the join under "What this release's steps do to your repository", and names no other edit to that page.
- **After:** the pass also moves the count word in that section's opening sentence from `Four` to `Five`, since the sentence counts the section's bullets and the join is one more.
- **Cause:** builder discovery
- **Reason:** the opening sentence says how many moves reach an installed repository and that each is named below it; with the new bullet and the old word the page would state a count its own list contradicts.
- **Evidence:** the opening sentence of the section "What this release's steps do to your repository" in `help/upgrade-steps.md`, before and after the pass commit of `TOOL-dDeclaredLoop-36`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** none
- **Caused-by:** TOOL-dDeclaredLoop-36
