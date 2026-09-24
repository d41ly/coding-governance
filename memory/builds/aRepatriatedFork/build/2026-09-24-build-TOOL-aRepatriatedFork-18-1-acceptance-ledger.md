# TOOL-aRepatriatedFork-18 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-18

One unit pass under the mandate. It ran no merge bar and no self-test suite. Each criterion was
observed by the one checker it names, run on its own: `govkit selfcheck`, `check-arms.py --check`,
`--report` and `--selftest`, the lexicon, the kit-version and install-prefix checkers, a scratch
`govkit apply`, and `git grep`. The new `[aRF-18 AC1]` arm in `tools/govkit/selftest.py` was not
run, because that file is a suite; the break it stages was observed directly on this tree instead.
The close owes the suites: `govkit selftest`, the resolve-python parity arm for `derive_self_rel`,
and the memory-hygiene, method-carriers, manifest-check, check-unattended, check-playbook and
unattended suites whose text this unit edited.

The new check-arms arms were observed RED first. A copy of this unit's `check-arms.py` with the
a7c78ad2 `parse_pin`, `classify`, `cmd_check` and `cmd_report` spliced back in failed all five S5
and S6 arms that assert the new reads, and passed the S6 control that asserts a branch without its
local suite is named. The S9 arm failed against a copy carrying the a7c78ad2 `INTERP_RE`.

The adopters were not touched. AC2 ran in a scratch target under `%TEMP%/a18t`, not at inCMS.

**Evidences:** TOOL-aRepatriatedFork-18
- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0 and prints `shipped-gate arms: 8 shipped gate(s)`. With `unattended.test.sh` added back to the unattended descriptor's `project-owned` rule it exits 1, naming `tools/unattended/unattended.sh` and its sibling suite `tools/unattended/unattended.test.sh`. Restored, it exits 0 again
- AC2 — `python tools/govkit/govkit.py apply` — `apply --write` at prefix `scripts` into `%TEMP%/a18t/t2`, from a temporary commit of this tree, landed six S1 suites and `scripts/unattended/unarmed-branches.txt`. The run also needed review-harness, agent-cap and settings-merge, which the three kits require. `check-arms.py --check` then exited 0 once `--emit-floors` had declared the seeded `ARMS_FLOORS`, with no `memory/project/unarmed-branches.txt` in the target, and `--report` printed 15 `PINNED` rows from the sidecar. `apply` itself exited 1, because the unattended adopter found no `.unattended.conf` and review-harness rendered nothing. Neither is about the suites
- AC3 — `--report` — prints 15 `PINNED` rows, all in `tools/unattended/unarmed-branches.txt`, and their gate, check and ordinal are the same 15 keys as the a7c78ad2 central file. `--check` exits 0. With one sidecar row copied into the central file, `--check` exits 1 with `pinned in exactly one file`, naming both files
- AC4 — `python tools/memory-tree/check-arms.py --selftest` — PASS. `S5+S6: a sidecar pin and a local-suite arm leave the gate green` holds, and `S6: without the local suite the same branch is named unarmed` names `tools/kit/g.sh:3 check 2 branch 1`
- AC5 — `git grep -c '^# >>> derive_self_rel'` — counts one block in each of the five suites S2 names, plus the canonical copy. Each block is byte-identical to `tools/lib/kit-rel.sh` by the parity table's own `blk` extraction. The `KIT_REL:-tools` and `cp "$GOVROOT/tools/memory-tree` grep prints nothing over all seven S1 suites
- AC6 — `skip` — `git grep -n 'the spec-token checker is not beside this kit' -- tools/unattended/` prints one line, a `skip dispatch:` line naming govkit's registry `[[exempt]]`. No `FAIL` shares it, and the kit-source `FAIL` branch has different text
- AC7 — `VERB_OFFENDER_PIN` — `lexicon.py --list` names none of the seven old helpers. `--measure` prints `VERB_OFFENDER_PIN="982"`, which `.lexicon.conf` now declares, and `lexicon.py` exits 0
- AC8 — amended rev-2 — carried to `DEPL-aRepatriatedFork-20`, because inCMS's `gate-arms` leg runs inCMS's own fork of check-arms, which reads no sidecar and no `.local.test.sh`. The section 9 rev-2 line logs it
- AC9 — `bash tools/check-kit-versions.sh` — exits 0 after the descriptors changed what they ship and memory-tree, unattended, kickoff-manifest and playbook-render moved to 2.92, 1.32, 1.7 and 1.6 in every carrier. Before those bumps `govkit epoch --base f8fdd873` exited 1 naming the four kits, and after them it exits 0
