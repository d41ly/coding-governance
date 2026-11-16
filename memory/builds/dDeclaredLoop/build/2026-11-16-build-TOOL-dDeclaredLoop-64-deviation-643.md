# TOOL-dDeclaredLoop-64 deviation 643 — the sweep's stale figures, and the help page's plant list

**Serves:** deviation TOOL-dDeclaredLoop-64

- **Departs from:** `TOOL-dDeclaredLoop-64@rev-4` [§2, §5]
- **Hand-off:** spec-to-code
- **Before:** §5 "The sweep" reads the positional registry holding two rows for this spec, which the landing commit takes out with `python tools/playbook/positional.py shrink`, and its `git grep` for `no commit adds`, `breakpoints: held` and `unopened` over `tools`, `help` and `skills` matching nothing; its `help/loop.md` row and S4 name one prose sentence for that page.
- **After:** at this pass's base the registry holds no row naming this spec, so no shrink runs and the registry is not in the write set; the grep matched one check message of `TOOL-dDeclaredLoop-53`'s `pre-placement` plant in `tools/loop/breakpoints.py#run_breakpoint_plant`, the one this pass edits to expect the line under `tNone`. Beside S4's sentence, the page's "See it on a fixture" list of plant names gains `pre-placement-records-root`, so the list S3 extends stays whole.
- **Cause:** builder discovery
- **Reason:** both figures were read at `a7b105696`, before `TOOL-dDeclaredLoop-53` landed its plant and before the spec's own revision commit emptied the registry rows; the page lists every plant by name, and leaving the new one out would leave it stale.
- **Evidence:** `grep -c 'spec-TOOL-dDeclaredLoop-64.md' memory/project/positional-refs.txt` printed 0 at the base; `git grep -n -e "no commit adds"` over `tools help skills` named the one check message; `python tools/govkit/docs_leg.py --fingerprints` names the same anchor for `script:tools/loop/breakpoints.py`, since its usage row carries no plant name.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the close's `docs` and `positional (the citation check alone)` legs read the page and the registry as built
- **Caused-by:** TOOL-dDeclaredLoop-53
