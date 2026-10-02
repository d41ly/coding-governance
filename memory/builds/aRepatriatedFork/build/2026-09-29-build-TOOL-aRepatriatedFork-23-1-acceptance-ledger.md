# TOOL-aRepatriatedFork-23 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-23

Written by the unit pass on node a, 2026-09-29. No merge bar and no whole suite ran. The suite's
arms ran as two temporary slices placed beside the gate: the prologue plus the blocks this unit
touched, then the prologue plus every other block. Both were removed after. The red-first runs
used the same slice beside a copy of the gate as `2143b6d6` holds it, which is byte-identical to the
gate at `c88a328b`. Fixture repositories were built under the temp root and removed after.

The census figures are PINNED at `2143b6d6`. Every epoch-5 figure below was DERIVED at observation
time over the tree this unit commits.

**Evidences:** TOOL-aRepatriatedFork-23
- AC1 — `check-install-prefix.test.sh` (sliced) — eight `ok   AC1 …` arms, one per spelling, each file listing as one counted occurrence: a `<project>/`-led path, a directory-only reference, a quoted `"tools"` joined to a kit, a loose name that names no file, the root spelling, a literal `scripts/` prefix (F4), a shell `$HERE/../` sibling path (F1) and a python `HERE.parent / "<kit>"` join (F1)
- AC2 — the fixture graded by the `2143b6d6` gate — before any edit, a fixture carrying the same eight spellings plus one epoch-4 literal as a control listed exactly one row, the control's. None of the eight counted. The slice replayed against that gate reads `FAIL — 14 arm(s) failed`, every new ban arm among them
- AC3 — `check-install-prefix.test.sh` (sliced) — `ok   AC3 a file NO descriptor resolves is counted` and `ok   AC3 ...and the ban list does not count its own rows`. The counted file is `tools/lib/notes.md` under the fixture's `tools/`, which no descriptor resolves, so the population is no longer `govkit shipped`. The first reds against the `2143b6d6` gate
- AC4 — `check-install-prefix.test.sh` (sliced) — `ok   AC4 a marked root spelling passes arm 1` and `ok   AC4 ...and the ban still counts it`, on a fixture line carrying the `gov:root-fixture` marker. The second reds against the `2143b6d6` gate
- AC5 — `check-install-prefix.test.sh` (sliced) — `ok   AC5 the homonyms count nothing and the control counts one`, plus four `census homonym still present` arms. With the dot-directory and operand rules switched off in a staged copy, the homonym file lists `5` and the arm reds. A mutated census string makes `git grep -qF` exit 1, and the real one exits 0. `git grep -n` over the real tree finds all four census sites, at `tools/codebase-map/map_diff.py:188`, `tools/codebase-map/reuse_lookup.py:752`, `tools/playbook/render_playbook.py:196` and `tools/runlog/extract.py:252`, and none of them is counted
- AC6 — `check-install-prefix.sh --rebaseline` — `REBASELINED for predicate epoch 4 -> 5.` and `rows 139 -> 223`. A second run printed `REFUSING to rebaseline` and exited 1. The total is 3674 occurrences over 223 files; the reconciliation follows. A `--check` on the real tree then reads `carried-prefix clean — 223 recorded file(s), 51 hand-justified, none rising`. Its wall time was 27-28 s at epoch 4 and 22-24 s at epoch 5, two runs each
- AC7 — `bash tools/check-kit-versions.sh` exits 0. `python tools/govkit/govkit.py epoch --base 2143b6d6` exits 0, and so does the same command with `--base f8fdd873`. Both print `check-install-prefix · skip · no declared version`, because the entry declares `version_from = { none = … }`. There is no version carrier, so S6 moved nothing
- AC8 — `check-install-prefix.test.sh` (sliced) — `ok   AC8 a dead counter REFUSES to write and names itself` and `ok   AC8 ...and --check reds on it`. With the three `|| { print_counter_death; exit 1; }` guards removed in a staged copy, both arms red

## Reconciliation — 3674 against the census's 904 + 930 + 562

The received set is `govkit shipped` plus the runbook, 266 files. The other 58 are tracked files
under the surface that no descriptor ships.

| Part | Epoch 5 | Census | Difference, named |
|---|---|---|---|
| Received, visible to epoch 4 | 899 | 904 | +1 is tree drift since `2143b6d6` (the ledger read 905 before this unit). +4 are this unit's new fixtures in the gate's suite. −10 is the waiver registry, which S2 takes out of the population |
| Received, newly visible, gov's prefix | 1001 | 930 | 83 are quoted-prefix joins, 321 are `/`-led, 151 are directory-only, 379 are loose names that name no file, and 67 are kit paths whose next segment is a subdirectory or an extensionless file, which epoch 4's `<kit>/<file>.<ext>` shape could not match. The +71 is the gap between these rules and the census's broad regex. That regex was never committed, so the gap cannot be split further. 8 of the 71 are this unit's own fixtures |
| Not shipped, visible to epoch 4 | 563 | 562 | +1 tree drift |
| Not shipped, newly visible | 752 | unmeasured | The census recorded these spellings as unmeasured. They are 451 quoted-prefix joins, 63 `/`-led paths, 151 directory-only references, 42 ghost loose names and 45 nested or extensionless paths |
| Kit segment without gov's prefix, both sets | 459 | none | This class is new at rev-3 and the census never counted it. 52 are root spellings, 296 are a kit after a literal prefix (F4) or a derived base (F1), and 111 are quoted kit segments joined as paths (F1) |

The rows sum to 3674. `govkit/selftest.py` alone holds 403 of the quoted-prefix joins, all
fixture-internal.
