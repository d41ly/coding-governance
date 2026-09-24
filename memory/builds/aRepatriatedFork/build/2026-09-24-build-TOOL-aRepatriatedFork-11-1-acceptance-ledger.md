# TOOL-aRepatriatedFork-11 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-11

One unit pass under the mandate. It ran no merge bar and no self-test suite. AC1, AC2 and AC5 were
observed on a SLICE of `tools/unattended/check-unattended.test.sh`: its prologue, which builds the
suite's scratch fixture repository, followed by the one block of arms this unit adds to region 8,
plus one slice-only arm that puts check 21's plain pathspec back and asserts the nested README is
then named. The slice ran 13 assertions and all held; the file was deleted after. The whole suite
was not run, and the close owes it. S3 and S4 were observed through `check_fragment_wiring`, the
arm group this unit adds to `tools/govkit/selftest.py`, run alone by importing the suite: 7 arms,
all held. The whole govkit selftest was not run. No adopter tree was read or written.

**Evidences:** TOOL-aRepatriatedFork-11
- AC1 — `tOne` — a fixture build `tOne` with a marker-less README at its root and another in `tOne/notes/`: `bash tools/unattended/check-unattended.sh` named only `memory/builds/tOne/README.md` in check 21; with the `:(glob)` magic removed from the check 21 pathspec, the nested file was named too.
- AC2 — `"$M/builds/*/RUN.md"` — with the magic stripped from `unattended.sh`'s preflight pathspec, check 35 failed naming `unattended.sh:` and its line; an appended `builds/*/spec/*.md` tail left check 35 silent.
- AC3 — `wired` — `check_fragment_wiring`: over a target with only `gate-guard` wired, the step printed `wired` for stall-recorder and stop-guard and `already wired` for gate-guard, and `settings-merge.py --check` then passed for all three. The ordering half, the step before the verify pass inside a real `python tools/govkit/govkit.py update --write`, is by the call site's placement and was not observed on a fixture.
- AC4 — `python tools/settings-merge.py --check --fragment` — after `remove_wired_fragments`, it exited 1 for both fragments the run added and 0 for the `gate-guard` baseline; a stale command the step rewrote was not returned as added, so a rollback never unwires it.
- AC5 — `UNDECLARED_WRITE_CEILING="2"` — two dispatched passes each committing one stray file: `bash tools/unattended/check-unattended.sh --emit-ceiling` printed exactly that line on stdout and exited 0; on the unmodified fixture it printed nothing and exited 1.
- AC6 — `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` — exit 1 with the render one byte over its 65692-byte row, exit 0 on the committed render.
- AC7 — `GUIDE_CAP_BYTES="61440"` — appended to this repo's `.memory-tree.conf` for the run and then restored: `bash tools/unattended/adopt-unattended.sh` printed the NOTE line naming `GUIDE_CAP_BYTES` and exited 0 in both modes, and with no cap declared it printed no NOTE.
- AC8 — `bash tools/check-kit-versions.sh` — exit 0 with unattended at 1.33 and settings-merge at 1.7.
