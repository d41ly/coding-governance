**Serves:** journal TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46

# aRepatriatedFork: VERIFYING repair pass R2, per leg

*Node `a`, 2026-10-01. The full bar at `6e7cb0df` (`GATE_FULL=1 GATE_SELFTESTS=1`) redded six code
legs. Each was reproduced alone at `20dd409e` before any edit, its cause traced with `git log -S`,
and the cause checked against gov main `d6e1749c` by ancestry. Every fix folds into the unit whose
commit wrote the line, spec-first: the records commits `977e44c1`, `8a520790`, `95ddd8aa` and
`e82395c4` carry the revision entries, and each code commit follows its own. No merge, no push, no
hook bypassed. The whole bar did not run.*

## Per leg

| Leg | Reproduced at 20dd409e | Caused by this build | Fix | Owner | Exit after |
|---|---|---|---|---|---|
| `scratch-guard self-test` | yes, the liveness meta-arm | yes, `6830f257` | the meta copy pins `HERE` to the suite's own | TOOL-aRepatriatedFork-28 | 0 |
| `codebase-map kit selftest` | yes, 2 FAIL | yes, `6830f257` and `12acc633` | `abspath` in the prefix derivation, and the resolver below | TOOL-aRepatriatedFork-28, -46 | 0 |
| `run-gates run-log line` | yes, 4 FAIL in AC8 EXITS | yes, `f6f41cc3` | the EXITS row takes the parse line's new text | TOOL-aRepatriatedFork-29 | 0 |
| `govkit selftest` | yes, 10 FAIL and a crash | yes, `f6f41cc3`, `6830f257`, `e3d2cda9` | see below | TOOL-aRepatriatedFork-28, -29, -30 | 0 (1636 s) |
| `placeholder-catalogue self-test` | yes, `ROOT: unbound variable` | yes, `baa7289a` | `ROOT` restored for the repo-root template read | TOOL-aRepatriatedFork-24 | 0 |
| `foreign-prefix parity` | its calibrate at gov's prefix redded | partly, see below | see below | TOOL-aRepatriatedFork-2, -26, -28, -29, -30, -46 | RED, see below |

Every row above that the calibrate also read was re-run alone at `801fa7e6` in a frozen clone and
exited 0, with the unattended adopter, gate-guard, stall-recorder and stop-guard suites and
`pre-push run-log line` beside them.

## govkit selftest, item by item

- The crash: the `[gate_runner_seed]` arm joined a registry descriptor still spelled `{prefix}/…`. Owner -29.
- `[dBF]` AC2 and the integrity-count arm loaded a descriptor raw, so every source read `./<file>`. Owner -29.
- The leg-name arm pinned `tools/gate-legs.json`, and the message prints `<prefix>/gate-legs.json` since `f6f41cc3`. Owner -29.
- Arm 7e's staged edit matched the old one-line `default` and staged nothing; it now asserts the edit took. Owner -29.
- `ORDER|project-owned` 27 -> 28: `e3d2cda9` withheld `foreign-prefix.gov.test.sh`. Owner -30.
- `[-14]` AC8, `[-24]` AC5 twice, `[-26]` AC1 and AC4 ran an engine read out of git inside a fixture gov moved to the `{prefix}` spelling. `write_pre_fix_spelling` re-spells that copy. Owner -28.

## The foreign-prefix leg

Its first run, at `6e7cb0df`, never graded a foreign prefix: the calibrate at gov's own prefix redded
on ten rows. Five were the legs above. The other five:

- `unattended adopter e2e` arm 4, `unattended stall-recorder selftest` and `unattended stop-guard
  selftest`: TOOL-aRepatriatedFork-46 (`181f9f34`, after base). The sibling-kit resolver followed a
  junction, so a junctioned kit dir adopted nothing; and `seed()` read `MT_KIT`, which the borrowing
  suites never set. Fixed in `e40a24dd`: all 64 copies of the resolver take `absolute()`.
- `unattended gate-guard selftest`: the scratch-guard meta-arm defect. Owner -28.
- `pre-push run-log line`, exit 127, NOT this build: the budget row's rationale sat in its argv column since `ca2c20a0`, an ancestor of `d6e1749c`. Small and in a file this build changed, so fixed; recorded under -30.

The resolver repair moved twelve kits' shipped bytes, so `162f2d13` bumped each one. The kickoff
manifest's check 9 tripped, and `801fa7e6` re-audited §B.

Its ceiling: 8302.2 s, the leg's own seconds in `gate-run`, entered through `derive-ceilings.py
--write --observed`. The margin rule `max(120 s, 1.0x)` puts the ceiling at 16605 s, under the
profiles' 21600 s wall (`d09b731f`). That reading is of a run that stopped after its calibrate, one
pass of four, so it understates a green run.

### Its second run, at 801fa7e6

The calibrate at `tools/` read every row in about 1.6 hours (`codebase-map kit selftest` and `govkit
selftest` red there, see below). It then redded at `scripts/` on 9 rows and at `vendor/gov/` on 13.
The main loop killed it before the repo root, and the owner approved a redesign of the leg as a new
unit. Each foreign-only row was then run alone in a clone with the tool root moved, and the rows
the killed run never reached were triaged the same way at the root.

The rows whose suite could not find its own subject were real prefix defects, fixed and green at
`tools/` and at every prefix they redded at:

| Row | Prefix | Cause | Owner | Commit |
|---|---|---|---|---|
| `playbook parity selftest` | scripts, vendor/gov | the predicate's literal `tools/<kit>/` | -26 | `fcf03285` |
| `kit-placeholders self-test` | vendor/gov | a one-segment-only descriptor search | -29 | `6f380b08` |
| `runlog selftest` | scripts, vendor/gov | an arm planting the host prefix where the lint refuses a fixed head | -28 | `90c1be16` |
| `spec-tokens self-test` | vendor/gov | a one-segment-root arm built two segments deep | -28 | `90c1be16` |
| `codebase-map adopter e2e` | vendor/gov | fixtures deeper than the kit supports | -28 | `90c1be16` |
| `unattended-build self-test` | scripts | a negative control equal to its fixture at `scripts/` | -28 | `90c1be16` |
| `check-wiring self-test` | vendor/gov | the root taken as `$HERE/..`, older than base | -28 | `8fa4be5a` |
| nine suites | vendor/gov, root | the root taken as their grandparent | -28 | `80c859d8` |
| `hook destinations self-test` | root | the gate at a `.` prefix; the suite's `$KIT_REL/` | -2, -28 | `c22ac2b8`, `50de5e71` |
| `run-gates adopter e2e` | root | a no-prefix predicate that matched any mention | -28 | `475c274b` |
| `unattended adopter e2e` | root | a flat checklist expected without `./` | -28 | `475c274b` |
| `playbook parity selftest` | root | its fixture runbook's bare `memory-tree/` | -46 | `d9434d54` |

### What stays red, and why it is not repaired here

1. **Gov's own declarations do not move with the tool root.** `pre-push run-log line`, `pre-push
   self-test` (`GOV_KITROOT=tools` in `.githooks/gate-env.sh`), `run-gates gov canary` (the charter
   names `tools/run-gates/gate-profiles.txt`), `codebase-map kit selftest` (`.codebase-map.conf` and
   the generated map), `unattended playbook selftest`, and the render half of `unattended-build
   self-test`. Each went green in a clone where those declarations were re-spelled for the new root.
   That re-spelling belongs to the leg, and the owner's redesign takes it. The patch that did it is
   kept outside the tree, so none of it landed.
2. **govkit selftest's fixtures.** Its prologue finds its subject at every prefix tried: the suite
   ran 939 s through 496 arms at `scripts/`. It still reds 19 arms and then crashes, for three
   fixture reasons. The vintage arms read gov's history at gov's historical prefix (`24f39915`). A
   deploy-less target lands at the engine's default prefix, not at gov's. And the pre-fix engines
   predate prefix derivation entirely. Each needs a decision about what a relocated gov's history
   means, so it is recorded here rather than guessed.
3. **Two gates' semantics at a root install.** `check-playbook-parity.sh` derives kits as every
   top-level directory, so `.claude/` and `skills/` count as kits. `check-spec-tokens.py` grades a
   token only when it carries a directory, so a root install's bare file names go ungraded. Both
   need a declared kit population or path rule, which is a design choice.
4. **The leg's own population edit.** The leg removes its own row from `gate-legs.json` and leaves
   the govkit registry's `[[exempt_leg]]` row, the subject pin and the generated map behind. That is
   why `govkit selftest` and `codebase-map kit selftest` red at gov's own prefix inside the leg's
   clone, and green outside it.

The heavy rows were never run at the root, by the leg or by hand.
