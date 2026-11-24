# TOOL-dBoundRoles-89 deviation 891 — the builder's departures from its own section 4

**Serves:** deviation TOOL-dBoundRoles-89

- **Departs from:** `TOOL-dBoundRoles-89@rev-1` [§4 "The verb and the reader"]
- **Hand-off:** spec-to-code
- **Before:** the block's shape prints the object after the clean grade; each refusal of the graded object is raised with the lines' text, which `place` prints as `placement — refused · <text>`, where section 5 states every refusal opens `placement: refused`; nothing states where the verb's text comes from, nor what an object UTF-8 cannot write does.
- **After:** (1) `tools/roles/handoff.py#check_return_file` answers `(defects, text)`, so the object is read from the text graded; its one caller is the verb. (2) An object holding a lone surrogate, which JSON admits and UTF-8 does not, makes the verb exit 2 naming it, and `place` refuses it, where an unhandled error would print a traceback. (3) A refusal of the graded object, and of a printed line that is no JSON object, prints `placement: refused — return — <text>`, as a defect of the typed channel does; the text of the outcome refusal is the lines' own, held once as `tools/loop/placement.py#OUTCOME_REFUSED`, and the lines' refusals print as before.
- **Cause:** builder discovery
- **Reason:** S3 asks that the text be read once, section 5 states the refusal's opening, and the placement file's writer would meet the surrogate after its checks.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-89-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-89
