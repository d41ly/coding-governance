# PLAY-dConvergedCharter-19 deviation 191 — an adopter's line-ending block pins whole classes, its own files of each class included

**Serves:** deviation PLAY-dConvergedCharter-19

- **Departs from:** `cl-dClosedLoop-0493@0d92d2e3`
- **Hand-off:** design-to-spec
- **Before:** the per-directory line-ending pins retired into class pins
- **After:** the per-directory line-ending pins retired into class pins, in gov's `.gitattributes` and in the kits' `[[lf_pin]]` rows alike, so an adopter's govkit block pins every tracked `*.md`, `*.txt`, `*.toml`, `*.sh`, `*.js` and `*.json` file it holds, a kit's own or not, and the upgrade step `govkit/lf-pins-to-class` renormalizes the CRLF ones
- **Cause:** design defect
- **Reason:** A kit's per-directory row pins only the kit's own directory in an adopter. Retiring it into a class pin, as the clause asks, reaches every file of that class the adopter holds, and the step that ships it renormalizes those committed with CRLF: a write to adopter files the clause names only by its effect. Keeping the `md` and `txt` rows per-directory, or the kits' rows untouched, fails the clause (veto 1); the class option fails only veto 3, so the standing ruling ER:240 takes it, the most capable option that fails only the security veto or the goal bound. The step's `down` restores every renormalized file byte-identical. The work it leaves owed is PLAY-dConvergedCharter-19 S6 and S8, which ship the class pins and the step.
- **Evidence:** the clause, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:39`; research-compatibility's P-eol row, `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-research-compatibility.md:120`; `lf_pins` and `lf_pin_block`, `tools/govkit/govkit.py:5630-5692`; the 35 `[[lf_pin]]` rows (`git grep -n '^\[\[lf_pin\]\]'` at `0d1c1dda`); rung 5, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914`; PLAY-dConvergedCharter-19 §8 F3
- **Risk:** widening
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dConvergedCharter, citing ER:240, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0493@0d92d2e3
- **Caused-by:** PLAY-dConvergedCharter-19
- **Surface:** an adopter's .gitattributes block pins every tracked *.md, *.txt, *.toml, *.sh, *.js and *.json file
