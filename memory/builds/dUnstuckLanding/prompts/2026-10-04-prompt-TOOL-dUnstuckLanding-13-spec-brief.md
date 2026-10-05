# TOOL-dUnstuckLanding-13 to -20 — spec brief (the kit fix)

**Serves:** journal TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20

node d · 2026-10-04 · one brief for the eight spec authors. Each author writes ONE spec, for the unit
named in the call. These units BUILD the design at rev-2. The owner widened the build when it stopped
the close: rulings `TOOL-dUnstuckLanding-21` to `-24` in `memory/DECISIONS.md`.

## What to read first, whole

1. `memory/guides/BUILD-METHOD.md` and `memory/TEMPLATE-SPEC.md` — the spec shape. Every unit here is
   Tier-2, a shipped-kit edit.
2. The design record, `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-2-design.md`,
   at rev-2. Read your unit's section whole, and also "The shape of the answer" and "Order".
3. Your unit's ask row in `memory/builds/dUnstuckLanding/BACKLOG.md`. Its `accept` clause is the floor
   of your acceptance criteria. It is not the ceiling.
4. The closing review the design was folded from,
   `memory/builds/dUnstuckLanding/reviews/2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md`.
   Read the items your section's rev-2 notes name, so that you do not reintroduce them.
5. The kit you are changing:
   - `tools/unattended/README.md`;
   - the templates `PROTOCOL.template.md`, `STOPS.template.md`, `VERBS.template.md` and
     `SKILL.template.md`;
   - the code your section's "What it owes" names, at its line references.

## The units

| Unit | Order | Closes | Design section | Mechanism |
|---|---|---|---|---|
| `TOOL-dUnstuckLanding-13` | 1 | `TOOL-dUnstuckLanding-3` | §1 | `--handoff`, two hold codes, the recipe and landing facts, a fail-83 guard, `HANDOFF_CUTOFF` and the abort notice |
| `TOOL-dUnstuckLanding-14` | 2 | `TOOL-dUnstuckLanding-4` | §2 (c1)+(c2) | HELD-handoff derives LANDED; `--settle`; the content predicate; `work-landed-at`; `abandoned`; check 15 |
| `TOOL-dUnstuckLanding-15` | 3 | `TOOL-dUnstuckLanding-5` | §2 (c3) | the drift-audit signals `aborted_work_landed` and `discarded_work_landed` |
| `TOOL-dUnstuckLanding-16` | 4 | `TOOL-dUnstuckLanding-6` | §3 | an INHERITED red lands at any age; the age escalates; `ATTR_LANDABLE`; kit default `land` |
| `TOOL-dUnstuckLanding-17` | 5 | `TOOL-dUnstuckLanding-7` | §4 | the history legs grade the run's own range; `UNDECLARED_WRITE_BUDGET`; `fleet_over_budget` |
| `TOOL-dUnstuckLanding-18` | 6 | `TOOL-dUnstuckLanding-8` | §5 | the close-decision table; the carry-forward `build-complete`; the M3 sentence |
| `TOOL-dUnstuckLanding-19` | 7 | `TOOL-dUnstuckLanding-9` | §6 | one refresh helper: `refreshed-at` on park, handoff, abort, and the primary close |
| `TOOL-dUnstuckLanding-20` | 8 | `TOOL-dUnstuckLanding-10` | §7 | `LANDING_NODES` resolved from machine and user; a planned hand-off |

The header tail carries `order <n>` and `closes <ask id>` exactly as the table gives them. The build
runs them ONE AT A TIME in that order, because nearly all of them write `tools/unattended/unattended.sh`.
So each spec may consume what an earlier unit ships, and declares that as a §3 `consumes-from` edge.
The earlier unit carries the matching `hands-off`.

## Constraints every spec carries

- **One mechanism per spec** (M2). When a section owes something another unit's section owns,
  declare the edge. Do not build it twice.
- **Kit rules the gate enforces.** A spec must plan for each of these, or it will red at the close:
  - A kit file names nothing outside itself by literal. The ban is in `tools/hooks/README.md`, and
    the conformance legs enforce it.
  - Every new numbered `fail N` branch gets an arm in its sibling `*.test.sh` that asserts a literal
    slice of the branch's own text, or else a row in `memory/project/unarmed-branches.txt`. That is
    the harness meta-gate in `memory/HYGIENE.md`.
  - A new conf key joins the closed import allow-list in `tools/unattended/check-unattended.sh`, the
    kit's example conf, and the key table in PROTOCOL §8. Check 22 joins those three.
  - The renders under `memory/guides/UNATTENDED-*.md` and `.claude/skills/unattended/SKILL.md` are
    byte-copies of their templates, re-copied by `bash tools/unattended/adopt-unattended.sh`. A
    template edit owes that re-copy in the same pass.
  - The kit version is bumped ONCE, by the orchestrator, at VERIFYING. Not in any unit.
- **Acceptance criteria are DIRECT.** Each one is a staged break, a fixture or a probe, written so the
  builder can observe it without running a suite. Name the suite arm a criterion would live in under
  §7 `New arm:` lines. No AC may spell a bar or suite invocation (`SPEC_DIRECT_CUTOFF`). Each AC
  carries a backticked witness and a `Red when:` clause.
- **§7's leg line** names every leg whose manifest `guard` a path under §4 `### Files touched (estimate)`
  trips. `python tools/check-spec-tokens.py` reports the hits; run it on your spec and clear them.
- **§10.** Run both probes, and record the seam you extend, by path:
  - `python tools/codebase-map/reuse_lookup.py "<behaviour phrase>"`
  - `python tools/memory-recall/query.py "<question>" --terms "<8-14 terms>"`

  Then record the recall terms you used.
- **§8.** Resolve every fork you raise, marked `RESOLVED (agent, 2026-10-04, delegated)`, by M3's
  rule. A fork that needs a new external dependency, or a carrier the design did not name, is parked
  and reported in your return; it is not resolved.
- **Status `INPROGRESS`, rev-1, Tier-2, base `98926870`, streams tooling.** The filename is
  `memory/builds/dUnstuckLanding/spec/2026-10-04-spec-<unit id>.md`.
- **Do not edit any file but your spec.** Run no gate leg and no suite. After writing, run
  `bash tools/memory-tree/check-memory-hygiene.sh --staged` on your file, staged, and fix what it
  names.
