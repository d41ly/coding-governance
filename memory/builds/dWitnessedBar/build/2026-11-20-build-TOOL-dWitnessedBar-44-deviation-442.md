# TOOL-dWitnessedBar-44 deviation 442 — the step's three verbs gain `[[usage]]` rows

**Serves:** deviation TOOL-dWitnessedBar-44

- **Departs from:** `TOOL-dWitnessedBar-44@rev-4`
- **Hand-off:** spec-to-code
- **Before:** S5 documents the step in `help/upgrade-steps.md` with its three verbs in a `run: no` fence, and Files touched names no `tools/govkit/usage.toml`.
- **After:** `tools/govkit/usage.toml` gains `script:{prefix}/govkit/steps/inherited_red.py#up`, `#witness` and `#down`, `verb`-shaped with no flags, and the page's section anchors each by its fingerprint, as the `.agent-cap.conf` and review-round sections anchor theirs.
- **Cause:** builder discovery
- **Reason:** the `docs` leg tests each line of a page's `sh` fence against the `verb` rows, and a tracked entrypoint with no `[[usage]]` row and no row in the shrink-only `memory/project/docs-undocumented.txt` reds `UNROWED` (`tools/govkit/docs_leg.py#check_page_command`), so the section S5 asks for cannot land without them.
- **Evidence:** `tools/govkit/docs_leg.py#derive_usage_fingerprint` over each row's resolved shape printed `7d308cd4`, `79b2b797` and `14a9242d`, the anchors the page carries; the same call over `review_rounds.py`'s rows printed the anchors its section already carries.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-44
