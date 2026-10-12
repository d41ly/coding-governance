# TOOL-aOrientedCast-9 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-9

Direct checks only; no gate, suite or bar ran in the pass. Every criterion is a direct read of the
installed carrier, the adopter's `--check`, the roles kit's renderer and the kit version checker. The
adopter's `--check` was observed RED first: one byte appended to the installed copy made it exit 1
naming `UNATTENDED-VERBS.md`, and restored it exited 0. The greps of AC1 to AC3 were run against the
base `646d4a73` too and moved as each criterion states, and AC2's second grep was red on the first
render because the line wrapped mid-phrase, which the re-wrap fixed. The close owes the spec's section 7
list, the `unattended kit gate` and `kit epoch` legs among them, which this pass ran only as the checks
below.

**Evidences:** TOOL-aOrientedCast-9
- AC1 — `handoff.py harness-args` — `grep -o` counts 1 in the installed carrier where base counts 0; the bullet names `unattended-build`, `unattended-unit`, `tier2-review` and `.claude/roles.json`.
- AC2 — `diverged: true` — `A child returning` counts 1 as at base and that line carries `diverged: true`; `Any other .committed:false. stops the loop` counts 1 where base counts 0.
- AC3 — `dispatches every judge again` — `because the build harness runs its audit under` counts 0 where base counts 1; the deferred sub-bullet names `roles` and counts 1 for the phrase.
- AC4 — `adopt-unattended.sh --check` — exits 0 and `cmp` of template and installed copy exits 0; one byte appended made `--check` exit 1 naming `UNATTENDED-VERBS.md`, restored it exits 0.
- AC5 — `handoff.py harness-args <name>` — `unattended-build`, `unattended-unit` and `tier2-review` each exit 0 and print a non-empty JSON object, `builder` in the first two.
- AC6 — `gov:kit unattended@` — `git diff -U0 646d4a73` over the Skill template and render prints only the two marker lines, and `check-template-size.sh` exits 0 at 10239 of 10240 bytes.
- AC7 — `unattended@1\.95` — `git grep -c` prints nothing, 27 carriers read `1.99`, and `check-kit-versions.sh` exits 0.
