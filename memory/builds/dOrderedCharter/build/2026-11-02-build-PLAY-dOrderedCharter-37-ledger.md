# PLAY-dOrderedCharter-37 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-37

Each line is a probe this pass ran at rev-7 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: each planted case ran in a scratch clone of the repository holding the pass, with that clone's own
renderer and leg, and the leg's own state was read by a probe of its functions. The units reference row, its
page, every row's unit line and the unit-line check are the later commit's (section 8 F10 and F11), so AC8 and
the later halves of AC1 and AC10 are not observed here. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-37
- AC1 — `render_playbook.py --reference --check` — over the clone it printed three pages checked and none drifted and exited 0; with one kinds row's summary edited it exited 1 naming help/reference/kinds.md as drifted (PINNED, counted at cee53246). The four-page half is the later commit's.
- AC2 — a planted help/reference/orphan.md exited 1 naming the page and the declaration; the kinds register cut to no `[[kind]]` row exited 1 naming `doc.reference.kinds` and its empty population.
- AC3 — a probe of the leg's state over the clone found no `STALE` line naming a reference page; with one kinds row's usage edited it printed one `STALE` line naming help/reference/kinds.md and `kind:kind.tool-kit`.
- AC4 — the kinds row `kind.command` with its usage taken out exited 1 naming `doc.reference.kinds row kind.command: no usage`, and `git status --short` in the clone named only the register, no page.
- AC5 — `docs_leg.py --fingerprints` printed one tab-separated line per row, each reference anchor equal to its line; with the clone's `derive_usage_fingerprint` keeping the digest's last eight hex, the clone's render wrote every reference anchor equal to the clone's own line and none equal to the tree's (deviation 376).
- AC6 — `docs_leg.py --run` over every page in a scratch clone of the pass ran eighteen commands, the tutorial's ten among them, printed twenty blocks marked `run: no`, and found nothing (PINNED, counted at cee53246); a planted page whose block runs `exit 3` gave `--run --page` exit 1 and one `RUN` line naming the page, its line and the command.
- AC7 — `git grep -n -e "concepts/instruction-layer.md" -e "tasks/change-a-gov-rule.md" -e "tutorial/adopt-gov.md" -- help/README.md` — found the three index lines, `help/README.md` lines 22 to 24 (DERIVED at de36424bf).
- AC8 — the later commit's: no `unit.` tag resolves until PLAY-dOrderedCharter-40's rows are tracked (section 8 F11).
- AC9 — the catalogue's first summarised row with its summary taken out rendered exit 0 and the policy page listed it under the unsummarised heading, its count one higher; over the tree the `help.enforce` section links help/docs-leg.md and the policy page carries no anchor for it.
- AC10 — `step_gate.py --list` printed a `drive` line and a `kind` line, each with a non-zero count; the drive plant, run as a function in a scratch clone, took out `drive:drive.start.gov-session` and the kind plant `kind:kind.scenario`, each staged; the step gate's own plant runs and the `unit-usage` half are owed. A probe of the leg's state found no `CLASS` finding.
- AC11 — `memory/project/docs-undocumented.txt` — its first column joined with the ids whose `<pages>` in `python tools/govkit/docs_leg.py --fingerprints` name a reference page was empty, and the list lost the twelve policy rows the policy page now anchors (PINNED, counted at cee53246).
- AC12 — the criterion's command printed `help page commands` and `help reference pages`.
- AC1 — `render_playbook.py --reference` — the four-page half, observed at PLAY-dOrderedCharter-76's pass, CLOSED at 8b16e46fb, as that unit's AC1: the render wrote four pages, the units page among them; the `--reference --check` run over the four is owed to the close, as unit 76's ledger says. Appended by PLAY-dOrderedCharter-55's pass, its S3.
- AC8 — `unit.nowhere` — observed at PLAY-dOrderedCharter-76's pass, CLOSED at 8b16e46fb, as that unit's AC3: `docs_leg.py --fixture --plant unit-lines` exited 1 naming `unit.nowhere` as naming no gov unit, and a probe of the unit-line check over the tree's pages found no finding; the leg's own run is owed to the close. Appended by PLAY-dOrderedCharter-55's pass, its S3.
- AC10 — `unit-usage` — the later half, observed at PLAY-dOrderedCharter-76's pass, CLOSED at 8b16e46fb, as that unit's AC4: `step_gate.py --list` printed a `unit-usage` line with its members, and the plant's staged member left in a scratch clone; the step gate's `--fixture --plant unit-usage` is owed to the close. Appended by PLAY-dOrderedCharter-55's pass, its S3.

**Owed to the close.** The bar, and the RED-first observation of each `New arm:` line: the renderer's selftest
arm over its fixture declaration, the leg's `synopsis-stale` and `failing-command` plants, and the step gate's
`drive` and `kind` plants with and without a witness row. The `docs`, `step-gate`, `help reference pages` and
`help page commands` legs over the tree, and the two new legs' ceiling evidence rows, are owed too (deviation 374).
