# TOOL-aRepatriatedFork-16 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-16

One unit pass under the mandate. It ran no merge bar and no self-test suite: neither
`check-install-prefix.test.sh` nor govkit's `selftest.py` was run whole. Every criterion below was
observed by a direct run of the gate, the verb, or the suite's own fixture builders (their function
definitions extracted and sourced, no arm run) against scratch fixtures under `%TEMP%/r16`. No
adopter tree was read: the consumer fixture copies gov's own four files that carry the five
spellings nc measured, which are the bytes nc received.

## The fixtures

- **Kit-source fixtures** built by the suite's `mkfix`: a green README, a red README, the gate moved
  to `solo/` (no kit directory), and the kit plus the gate's sidecars moved to `vendor/gov/` with
  the registry left at gov's layout.
- **Consumer fixture** built by the suite's `mkfix_consumer`: gov's check-wiring script and three
  codebase-map files under `scripts/`, a receipt under `.governance/`, no registry.
- **Red case**: a7c78ad2's gate bytes (blob `6b3c599a`) written over the consumer fixture's gate.
- **govkit arm**: `check_shipped_verb` called in-process over a fixture registry of one entry and
  two roles, then again with the verb's role column cut out of its row format, which failed the
  arm, then restored.

**Evidences:** TOOL-aRepatriatedFork-16
- AC1 — `python tools/govkit/govkit.py shipped` — exit 0, 262 distinct sources in column three, equal to the pre-change heredoc's set minus `WIRE-INTO-PROJECT.md` plus the gate's own ratchet; the heredoc run with an empty `CARRIED_SELF` printed exactly that one extra row, which rev-2 records
- AC2 — `bash tools/check-install-prefix.sh` — exit 0 over gov's tree after every edit: 301 shipped files, 11 declared waivers, 26 marked fixture lines, 141 recorded files of which 45 hand-justified, byte-equal to the run before the change
- AC3 — `cd scripts && bash check-install-prefix.sh` — exit 0 in the consumer fixture, both SKIP lines printed, no hit named
- AC4 — `6b3c599a` — the same fixture under a7c78ad2's gate exits 1 naming the five gov-waived spellings: two check-wiring probes and the three codebase-map legacy literals
- AC5 — `grep -c 'installs kits at tools/' tools/check-install-prefix.sh` — returns 0; the `vendor/gov/` fixture with its waiver emptied exits 1 and the refusal reads `vendor/gov/<kit>/`
- AC6 — `grep -n '^GATE=' tools/check-install-prefix.test.sh` — the line derives the gate from `$(dirname "$0")` and spells no prefix; the suite run from `scripts/` is a suite verdict and is owed to the close
