# TOOL-dDeclaredLoop-7 — the position engine: each unit's step, the build's step and the next item, from witnesses

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 17 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0092@0abbde28 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

One engine answers "where is this build, and what next" from witnesses alone: each unit's step, the
build's step, the next item with its actor and its interrupts, items idempotent by witness and keyed
by round or pass and input SHAs, answering from the closed set `act`, `awaiting`, `blocked`,
`terminal`, `stuck`, `invalid-input`, `stale-remote`, and printing its read set and every claim it
used with its key and verdict. `--plan` and `--status` read it, and the `NEXT_RUNGS` ladder, which
reads typed state, is retired (gap-orient-03; the orientation record's `[position]`,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:121-145`).

## 2. Scope (IN)

- **S1** — The engine, `derive_position(repo, slug)` in `tools/loop/position.py`, returning a
  `Position` (§4 Data model). It reads only witnesses: commits and their trailers through
  `commit_trailers.py`, the build's loop transition record (unit 3), the loop definition's step,
  item and transition rows through `loop_lib.py` (units 1, 12, 13), the run-state file's parked
  entries, and the remote-tracking refs. No status header, README status word or `phase:` fact
  decides a step. Observed by AC1, AC2, AC9.
- **S2** — A unit's step, the four witnesses of `[position]`: `designed` when its spec is committed
  and derives READY; `built` when an attributed pass commit (`Pass: <id>`, read by unit 23's `read_commits` and
  `attribute` in the `replace` view)
  sits on the run branch, `--first-parent`, and the unit's acceptance record holds; `tested` when the
  verdict for the build's prepared merge holds, read until dWitnessedBar lands it from the run-state
  `gates-run` fact naming the bar and the tip it graded; `deployed` when the default branch's
  remote-tracking tip contains the pass commit. The build's step is its least-advanced unit's (FI-1).
  Observed by AC1.
- **S3** — The next item: the first item of the build's current step, in the loop definition's
  order, whose witness does not hold and whose needs are witnessed, with its actor. Each item instance
  carries the key `<item tag>@<round|pass>#<inputs>`, `<inputs>` the first eight hex digits of the
  SHA-1 of its input SHAs sorted and NUL-joined; an instance whose key matches a witnessed instance is
  done and never re-run, and a crashed one re-checks its witness before it runs again. Observed by
  AC2, AC3.
- **S4** — The interrupts, before the next item and in `[position]`'s order: an owner decision the
  build waits on (an owed parked entry of the run-state file with no settling row), mailbox messages
  (printed `unarmed` until dWellOiledMachine lands the mailbox), witnesses invalidated since the last
  transition (a claim whose verdict is not `fresh`), and dependency gates (a build the README's
  `parents:` names that has not landed on the default branch). Observed by AC4, AC5.
- **S5** — The answer, one of I4's seven, chosen in the precedence of §4: `invalid-input`,
  `stale-remote`, `terminal`, `awaiting`, `blocked`, `act`, `stuck`. Observed by AC4 to AC8.
- **S6** — The read set and the claims: every file read as `<path>@<blob8>` and every ref as
  `<ref>@<sha8>`, and every claim used printed as `claim — <name> · key <k> · <verdict>` through unit
  8's `derive_claim_key` and `derive_claim_verdict`. Observed by AC9.
- **S7** — The CLI, `python tools/loop/position.py <slug> [--json]`: line output (§4) or one JSON
  object with the same fields. Exit 0 for every answer but `invalid-input`, which exits 2.
  Observed by AC1 to AC9.
- **S8** — `--plan` reads the engine: its `next:` line is rendered from the engine's answer into the
  five shapes it prints today, byte for byte (§4 "The `next:` line"), the roster rows it prints above
  that line unchanged. The engine reads each unit's M2 state from those rows, handed to it by `--plan`
  in `GOV_POSITION_STATES`, so `plan_state` keeps one implementation and the call is not circular.
  Observed by AC10.
  **Readers:** by name: `tools/unattended/unattended.sh` spells `NEXT_RUNGS` and `derive_next_shape`
  (:5882, :5899, :5914, :6076, :6131) and is re-pointed in this unit; `tools/unattended/unattended.test.sh`
  spells both (:2891, :2900-2918) and its arms move to the engine's shapes in this unit;
  `memory/map/generated/symbols.json` spells `derive_next_shape` and is regenerated; and
  `memory/project/spawn-idiom-sites.txt` spells `derive_next_shape` in its `unattended.sh` row and
  loses it in this unit · by value: the five `next:` shapes, read by `.claude/skills/build/SKILL.md:59`,
  `tools/roles/SKILL.template.md:59` and `tools/unattended/VERBS.template.md:754-757`, each keeping
  its bytes because the engine renders the same shapes.
- **S9** — `--status` reads the engine: after its phase and witness lines it prints the engine's
  `position —`, `unit —`, `next —` and `interrupt —` lines for the slug, and its first-non-terminal-unit
  line is the engine's least-advanced unit. Observed by AC11.
- **S10** — The leg `loop position fixtures` in `tools/gate-legs.json`, running
  `python tools/loop/position.py --fixture`. Observed by AC1 to AC9.

## 3. Non-goals (OUT)

- The `next` command, the executor that calls it, and the card rendering it: dWellOiledMachine's. The
  stand-in is `--plan`'s `next:` line (I26).
- The default failure route and the frontier: unit 14, which reads this engine's `position`.
- The transition record, the tables and the item declarations the engine reads: units 3, 13, 9 and
  12. The engine refuses an input those units make malformed; it does not define them.
- The acceptance record's kind and the computed witnesses: unit 17's (I22). The engine reads the
  record through the record factory's reader and decides nothing about it.
- A position for a build with no loop items: such a build answers from its units' steps alone, its
  next item the step's first unit-level item.
- The driver's UPPERCASE phases, which stay unattended's run-state vocabulary and decide no position
  (I3).

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py`, its `replace` view for `Pass:`, through which every pass commit the `built` witness needs is read
- **consumes-from** `TOOL-dDeclaredLoop-8` — the claim key: `claims.py`, `derive_claim_key` and `derive_claim_verdict`, which S6 prints for every claim; without it a claim carries no key
- **hands-off** `TOOL-dDeclaredLoop-14` — the `position`, the frontier's input: the build's current step, its items' witnesses and the needs each item declares
- **hands-off** `TOOL-dDeclaredLoop-28` — the `position`, read at each step boundary to compare the witnessed path with the pinned composition
- **hands-off** `TOOL-dDeclaredLoop-26` — the `position`, which that unit points at the composition revision pinned on the step's transition record, deriving position inside the step from the pin
- **consumes-from** external — the driver's `--plan` roster rows and `plan_state` (`tools/unattended/unattended.sh:4458`), and the run-state `gates-run` fact, both in the tree at base

## 4. Design

### Evidence

- The ladder: `NEXT_RUNGS` and `derive_next_shape` (`tools/unattended/unattended.sh:5882-5921`), read
  once by `verb_plan` (:6131). Its inputs are the README roster's typed state.
- `--status` reads the run-state file's typed `phase:` through `read_derived_phase` (:1439) and the
  first non-terminal unit through `nonterminal_units` (:4815), a grep over status words.
- `plan_state` (:4458) is the M2 classifier, awk over a spec's sections, sliced by a sibling harness;
  a second implementation in Python would be a second answer to one question.
- The `gates-run` fact names the bar and the HEAD it graded (:2717).
- The `[position]` record: only witnesses decide a position; a unit's step is designed, built, tested
  or deployed; the build's step is its least-advanced unit's; interrupts come first in a stated
  order; one call returns the read set and every claim with its key and verdict.
- Items are idempotent by witness: "a witnessed instance is never re-run"
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:101-103`).

### Data model

```python
Position = {
  "slug": str, "state": str,                  # the build's state, I3, from the transition record
  "build_step": str,                          # step tag of the least-advanced unit
  "units": [{"id": str, "step": str}],        # designed | built | tested | deployed | none
  "next": {"item": str, "actor": str, "key": str} | None,
  "interrupts": [{"kind": str, "subject": str}],
  "answer": str,                              # one of ANSWERS
  "reason": str,
  "read": [str],                              # "<path>@<blob8>" or "<ref>@<sha8>"
  "claims": [{"name": str, "key": str, "verdict": str}],
}
ANSWERS = ("act", "awaiting", "blocked", "terminal", "stuck", "invalid-input", "stale-remote")
```

### The answer

| Precedence | Answer | When |
|---|---|---|
| 1 | `invalid-input` | the slug names no build, the README or a spec header does not parse, no tracked spec grades as a unit, or a recorded transition is one unit 13's `derive_move` refuses with `TransitionRefused` |
| 2 | `stale-remote` | the claim on the default branch's remote-tracking tip is not `fresh`: unread, or past its bound |
| 3 | `terminal` | the build's state is in unit 15's terminal set, or every unit is past its last step |
| 4 | `awaiting` | an owner-decision interrupt or a hold whose `until` has not passed |
| 5 | `blocked` | a dependency gate: a `parents:` build not landed |
| 6 | `act` | a next item exists |
| 7 | `stuck` | none of the above: no item of the current step can run and its exit item is unwitnessed |

`stuck` is the only answer reached by elimination, and its reason names the step and the unwitnessed
exit item.

### Line output

```
position — <slug> · state <state> · step <step tag> · answer <answer> · <reason>
unit — <id> · <step>
next — <item tag> · actor <actor> · key <instance key>
interrupt — <kind> · <subject>
read — <path>@<blob8>
claim — <name> · key <k> · <verdict>
```

### The `next:` line

`--plan` keeps its five shapes; the engine's answer picks one.

| Engine answer | `next:` shape, as printed today |
|---|---|
| `act`, its item a Design or Build item of unit `<id>` | the live-unit shape for `<id>`, its M2 state as `--plan` renders it |
| `act`, its unit's spec missing | `<id> (MISSING - spec it first)` |
| `invalid-input`, no tracked spec grades as a unit | `none - no tracked spec grades as a unit (see the NOT A UNIT rows above)` |
| `terminal` | `none - every tracked spec is terminal` |
| `awaiting` on an undecided ask | the undecided-ask shape, empty until TOOL-dDerivedDocket-16 supplies it, as today |

Any other answer prints `none - <answer>: <reason>`, a shape no reader matches as an all-clear, which
is the property the ladder's last rung bought.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_position`, `derive_unit_step`, `derive_next_item`, `derive_interrupts`, `derive_answer`, `derive_instance_key` | function | `tools/loop/position.py` |
| `Position`, `ANSWERS` | data shape, constant | `tools/loop/position.py` |
| `GOV_POSITION_STATES` | environment hand-over | `tools/unattended/unattended.sh` to `tools/loop/position.py` |
| `--json`, `--fixture` | CLI flags | `tools/loop/position.py` |
| `loop position fixtures` | gate leg | `tools/gate-legs.json` |

Retired: `NEXT_RUNGS` and `derive_next_shape` in `tools/unattended/unattended.sh` (S8's Readers).

### The fixture cases

`position.py --fixture` builds one repository per case under `%TEMP%` with a short prefix: a build
README, its specs, a run-state file, a loop definition with a three-item step, commits with trailers
and a bare remote; `--plant <case>` runs one.

| Case | Plant | Answer |
|---|---|---|
| `steps` | unit 1 deployed, unit 2 built, unit 3 designed | `act`, build step that of unit 3 |
| `typed-status` | unit 2's header typed `CLOSED`, no pass commit | unit 2 `designed`, never `built` |
| `idempotent` | item 1 witnessed at its key, item 2 not | next is item 2; item 1's key re-read, not re-run |
| `owner-decision` | an owed `decision` park, unsettled | `awaiting` |
| `parent-unlanded` | `parents:` names a build not on the default branch | `blocked` |
| `terminal` | the transition record's last state `landed` | `terminal` |
| `stale-remote` | the remote-tracking ref unreadable | `stale-remote` |
| `bad-transition` | a recorded transition unit 13's table lacks | `invalid-input`, exit 2 |
| `deadlock` | the step's only unwitnessed item needs an item of a later step | `stuck` |

### Files touched (estimate)

- `tools/loop/position.py`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/project/spawn-idiom-sites.txt`
- `tools/gate-legs.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The ladder widened with more rungs.** Its inputs are typed state; more rungs read more of it.
- **The engine classifying specs itself.** A second `plan_state`; the hand-over keeps one.
- **`--plan` printing the engine's lines instead of `next:`.** It breaks three readers that match the
  shapes, and the harness that parses `--plan --paths`.

## 5. Production-readiness checklist

- security — read-only: the engine writes nothing and runs no command but `git` reads and the
  driver's `--plan`.
- perf / scale — one `git log --first-parent` per build and one blob read per input; `--plan` gains
  one Python spawn.
- error / empty / loading states — every malformed input is `invalid-input` with its reason, exit 2;
  an empty roster is the nothing-graded case; an unreadable remote is `stale-remote`, never `act`.
- observability — the read set and claims lines are the audit trail of each answer.
- risks — a reader matching the `next:` wording: S8 keeps the five shapes byte for byte and the
  fall-through shape cannot read as done.
- testing — the nine fixture cases and the `--plan` and `--status` probes.
- migration — none; no record changes shape.
- user docs — `tools/unattended/VERBS.template.md`'s `--plan` and `--status` rows; no page under
  `help/` describes `--plan`.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant steps` runs, it prints `unit —` lines
  `deployed`, `built` and `designed` and the build step of the designed unit, and with
  `--plant typed-status` the unit whose header says `CLOSED` reads `designed`.
  Red when: a typed status word moves a unit's step.
- **AC2** — When `python position.py --fixture --plant idempotent` runs, the `next —` line names the
  second item and its key, and the first item's witness is read and its instance not re-run.
  Red when: a witnessed instance is named as next.
- **AC3** — When `derive_instance_key` is called through `python position.py --fixture --plant idempotent`
  with one input SHA changed, the key's `<inputs>` part changes.
  Red when: an input SHA leaves the key unchanged.
- **AC4** — When `python position.py --fixture --plant owner-decision` runs, the answer is `awaiting`
  and an `interrupt —` line names the decision.
  Red when: the engine answers `act` over an unsettled owner decision.
- **AC5** — When `python position.py --fixture --plant parent-unlanded` runs, the answer is `blocked`
  naming the parent.
  Red when: a dependency gate is skipped.
- **AC6** — When `python position.py --fixture --plant terminal` runs, the answer is `terminal`.
  Red when: a landed build answers `act`.
- **AC7** — When `python position.py --fixture --plant stale-remote` runs, the answer is
  `stale-remote`, and with `--plant bad-transition` it is `invalid-input` at exit 2.
  Red when: an unreadable remote or an undeclared transition yields `act`.
- **AC8** — When `python position.py --fixture --plant deadlock` runs, the answer is `stuck` naming
  the step's exit item.
  Red when: the deadlocked step answers `act` or `terminal`.
- **AC9** — When `python position.py --fixture --plant steps` runs, it prints at least one `read —`
  line per file it read and a `claim —` line for the remote tip carrying `key k1:` and a verdict.
  Red when: a claim prints without its key or verdict.
- **AC10** — When `bash tools/unattended/unattended.sh --plan <slug>` runs over the `steps` fixture,
  its `next:` line equals the shape the table maps the engine's answer to, and
  `grep -c NEXT_RUNGS tools/unattended/unattended.sh` prints 0.
  Red when: the line differs from the mapped shape or the ladder remains.
  fixture: the `steps` fixture repository; the unattended kit's own suites are waived for this landing
  (README rule 8), so this probe is the observation.
- **AC11** — When `bash tools/unattended/unattended.sh --status <slug>` runs over the `steps` fixture
  with a run-state file, it prints the engine's `position —` line.
  Red when: `--status` prints no position.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · each `--plant` case, and `typed-status` red with the header read as a witness · none
New arm: tools/unattended/unattended.test.sh · covers AC10 · the ladder's arms re-pointed to the engine's shapes, red with one shape's wording changed · none

## 8. Open questions

- **F1 — How does the engine read each unit's M2 state without a second classifier?** (a) `--plan`
  hands its rows to the engine in `GOV_POSITION_STATES`, and a standalone call runs `--plan` with the
  hand-over set empty and the `next:` line suppressed; (b) the engine slices `plan_state` out of the
  driver; (c) a Python classifier. (c) is a second answer to one question and (b) couples the engine
  to the driver's bytes. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the driver's `--plan` and `--status` re-pointed to the engine ·
  widens: none · relaxes: none
- **F2 — What does `tested` read before dWitnessedBar lands the per-tree verdict?** (a) The run-state
  `gates-run` fact naming the bar and the prepared merge it graded; (b) nothing, `tested` unarmed.
  (b) leaves every build short of `deployed` unable to pass Test. Rung 1, flow-steps' rule that a
  route into an unlanded build reaches today's stand-in. RESOLVED (agent, 2026-10-24, delegated): (a).
  widens: none · relaxes: none
- **F3 — How is `stuck` told from `act`?** (a) By elimination after the six others, with the step and
  its unwitnessed exit item named; (b) a repeat count of one instance. (b) is the budget's and the
  route-backs' job, units 30 and 32. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.

## 10. Reuse audit

The seams extended are `verb_plan`'s single `next:` writer (`tools/unattended/unattended.sh:6131`),
which keeps its five shapes and takes its choice from the engine; `verb_status`
(`tools/unattended/unattended.sh:8175`), which prints the engine's lines; and `plan_state`
(:4458), read through `--plan`'s rows rather than re-implemented. The position engine itself has no
seam: `python tools/codebase-map/reuse_lookup.py "derive which step a build and each unit is at from
commits and witnesses"` ranked name-stem hits only (`build`, `units`, `build_commit`, `step` in
`govkit.py`), none deriving a step. The scout cited the ladder at :5882-5921 and the line at :6131;
both agreed with source.

Recall terms used: `python tools/memory-recall/query.py "what decides the next unit and pass a build
should run" --terms "position engine next rung ladder plan status phase witness derived READY
idempotent interrupt"`
