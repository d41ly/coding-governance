**Serves:** journal TOOL-dBoundRoles-44

# TOOL-dBoundRoles-44 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit on its worktree before the pass commit at base
`2698e0c3e`, with `git grep`, `git log`, `git diff`, `wc -c`, `node --check` over the tier2 suite's embedded script,
the dead-path checker's authoring aid `bash tools/check-dead-paths.sh --list`, the widen door
`python tools/memory-tree/ratchet.py widen` and `python tools/policy/policy.py mirror --check`. No gate, suite or bar ran
in the pass, and a worktree-isolated agent may run no git command outside its worktree, so no fixture repository was
built: AC6's hygiene run over a scratch tree, the spec-audit arm's RED-first observation and the legs section 7 lists
are owed to the main loop at the close. The departures from the spec are the deviation record of this unit,
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-44-deviation-443.md`.

## S1 — the `memory/` readers at the build run's base

`git grep -l -F 'agent-cap.js' 8b8b1374c -- memory ':!memory/builds' ':!memory/ledger'`, the reader grep of unit 25's
answer filtered to `memory/` at the build run's base `8b8b1374c` (DERIVED), each file with the class that takes it in
the table "The classes" of `TOOL-dBoundRoles-42`'s spec:

| File | Class |
|---|---|
| `memory/DECISIONS.md` | append-only record |
| `memory/archive/DECISIONS.2026-08-10.md` | append-only record |
| `memory/archive/parallel-coding-governance.template-v-2-1.md` to `-v-2-7.md` | append-only record |
| `memory/backlog/TOOL.md` | append-only record |
| `memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md` | gotcha page |
| `memory/gotchas/a-view-fix-trades-one-blindness-for-another.md` | gotcha page |
| `memory/gotchas/amendment-leaves-its-other-half-standing.md` | gotcha page |
| `memory/gotchas/check-grades-one-layer-of-a-layered-config.md` | gotcha page |
| `memory/gotchas/concurrency-is-not-a-budget.md` | gotcha page |
| `memory/gotchas/trailing-comma-counted-as-an-element.md` | gotcha page |
| `memory/guides/MERGE-BAR.md` | rendered guide in the table; a live guide edited in place, as `TOOL-dBoundRoles-51` S5 classes it |
| `memory/guides/REVIEW-PROTOCOL.md` | rendered guide |
| `memory/map/features/agent-cap.md`, `review-harnesses.md`, `unattended.md` | map dossier |
| `memory/map/generated/CARDS.md`, `MAP.md`, `inventories.json`, `symbols.json` | generated map |
| `memory/project/positional-refs.txt` | registry |
| `memory/project/spec-token-waivers.txt` | registry |

The gotcha pages are the set the table counts at HEAD `c93f676e2` (DERIVED by the same grep at that sha). No file the
grep prints stands outside a class, so none is recorded here as new. Unit 25's answer is cited, not restated: its
acceptance ledger's reader-grep line, AMENDED, names `TOOL-dBoundRoles-42` S4 as the population, and its section
"Amended by TOOL-dBoundRoles-44" points here.

## S3 — unit 25's reader list re-derived at the build run's base

`git grep -l -F 'agent-cap.js' 8b8b1374c -- ':!memory/builds'` (DERIVED), compared with the paths unit 25's S8 names:

- Printed and not in unit 25's S8: the `memory/` files of the table above, which S8 hands to `TOOL-dBoundRoles-42`'s
  classes; `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, the frozen receipt this unit waives; and
  `tools/workflows/drift-audit-code.js`, `tools/workflows/drift-audit-state.js` and `tools/workflows/unattended-build.js`,
  covered by S8's "the renders of the harness templates above".
- In unit 25's S8 and not printed: the leg's readers, derived by `git grep -l -F 'agent-cap self-test'`, and the
  charter's `agent-cap hook` line in `coding-governance-agents.template.md` and `AGENTS.md`, each read by another
  needle; `tools/workflows/tier2-review.template.js`, which at that base names the `agent-cap hook` and not the file;
  and `tools/loop/stage_coverage.py`, cited in S8's prose for the harness-hooks inventory join, not as a by-name reader.

## S10 — the fork-record cutoff, recorded for unit 11

`grep -l 'admitted-by: '` over `memory/builds/dBoundRoles/spec/` prints 15 specs at `2698e0c3e` (DERIVED), not the six the
spec counted at `c93f676e`; the cutoff `2026-11-24` is later than every filename date there, the latest `2026-11-23`.

**Evidences:** TOOL-dBoundRoles-44
- AC1 — `memory/` — the grep at the build run's base printed only the files of the S1 table above (DERIVED at `8b8b1374c`), each in a class of `TOOL-dBoundRoles-42`'s table; none needed a line of its own.
- AC2 — `gov-(spec|diff)-reviewer` — `git grep -n -E 'gov-(spec|diff)-reviewer' -- tools/workflows/README.md tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh` printed nothing on the built tree, exit 1. The spec run's arm reads FULL with `diffFinder` set to `gov-other-reviewer`, so it still reds when the harness reads the wrong kind's key; `node --check` over the suite's embedded script exited 0. OWED: the arm's RED-first observation and the `tier2-review self-test` and `unattended-build self-test` legs at the close.
- AC3 — `git diff --quiet` — `git diff --quiet 8b8b1374c HEAD -- tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` exits 0, the receipt unwritten; `bash tools/check-dead-paths.sh --list` marks `waived` every receipt line naming `agent-cap.js` or `agent-cap.test.sh`, each by a row `widened:2026-11-23-build-TOOL-dBoundRoles-44-widen-13` the widen door wrote after the hand-written `carried:TOOL-dBoundRoles-25` rows were removed. OWED: the `dead-path carriers (deleted files still named)` leg at the close.
- AC4 — `Read/Grep` — `grep -n 'Read/Grep' skills/session-kickoff/SKILL.md` prints nothing, and `wc -c < skills/session-kickoff/SKILL.md` prints 18385, at most 18432 (DERIVED). OWED: the `kickoff engine size <=18KiB` and `manifest-check self-test` legs at the close.
- AC5 — `memory/gotchas/` — `bash tools/check-dead-paths.sh --list` prints no line under `memory/gotchas/`: the narrative line of `memory/gotchas/amendment-leaves-its-other-half-standing.md` now names `tools/roles/spawn-guard.js`, that of `memory/gotchas/inline-marker-breaks-a-line-continuation.md` names `tools/roles/spawn-guard.test.sh`, and the waiver row of each is gone.
- AC6 — `F:work-order-legacy.txt` — `grep -n 'F:work-order-legacy.txt' tools/memory-tree/check-memory-hygiene.sh` names the case unit 17 built in check 3, by name with its comment naming the roles kit; `grep -n 'work-order-legacy' .memory-tree.conf` prints nothing; the guide row stands in `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`. OWED: `check-memory-hygiene.sh --only 3` over a scratch tree holding the seeded registry, at the close.
- AC7 — `.claude/skills/unattended/SKILL.md` — `wc -c` prints 11454 against the row's 11455 (DERIVED), CR-stripped the same; `grep -n "handoff.py facts" tools/unattended/SKILL.template.md` names unit 13's line, as the main loop's decision `2026-11-23-build-TOOL-dBoundRoles-44-1-main-loop-decision` binds; `memory/guides/UNATTENDED-VERBS.md` equals `tools/unattended/VERBS.template.md` CR-stripped. No trim is owed and unit 13's build raised no row, so no `memory/DECISIONS.md` row is named. OWED: the `unattended skill size` leg at the close.
- AC8 — `python tools/policy/policy.py mirror --check` — exits 0, `policy: mirror fresh`; `git log --format=%h 8b8b1374c..HEAD -- .governance/policy.json` prints `df3ed4fbe` and `2ddf17089`, each changing that path alone.
- AC9 — `git diff --quiet` — answered amended: `grep -n 'git diff --quiet' memory/builds/dBoundRoles/README.md` names the close rule among the build-level rules; unit 25's acceptance ledger records the swap check's exit per swapped harness at the close under a `Pass: none` commit, where the swap happens, as `TOOL-dBoundRoles-51` S2 completes it. No harness was swapped through this pass.
- AC10 — `FORK_RECORD_CUTOFF` — `grep -n FORK_RECORD_CUTOFF .memory-tree.conf` prints `2026-11-24`, later than every filename date under `memory/builds/dBoundRoles/spec/`, the latest `2026-11-23`.
- AC11 — `help/roles.md` — `grep -n "anchor" help/roles.md` names the refusal under "How a task reaches an agent", closing the prompt writer's step after the frame paragraph.
