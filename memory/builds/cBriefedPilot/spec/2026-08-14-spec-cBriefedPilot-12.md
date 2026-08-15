# TOOL-cBriefedPilot-12 — leg check 16, the registry joined both ways and the pointers resolved

**Status:** OPEN · rev-2 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Make the two spellings of the directive layer answer to each other on the bar: the kit-owned
`DIRECTIVES_CORE` in the driver and the hand-authored table in the Skill template. A registry the
agent never sees and a table nothing pins are the same defect from two sides.

## 2. Scope (IN)

- **S1** — check 16 arm A in `tools/unattended/check-unattended.sh`: every `DIRECTIVES_CORE` member
  has a table row, and every table row is a member, joined on the pair `(handle, M<n>)`. Both
  directions, always.
- **S2** — the table is located in `tools/unattended/SKILL.template.md` by row shape: a line matching
  `^| ` followed by a backticked lowercase handle and a closing pipe. An EMPTY extraction is a NAMED
  refusal, never a skip.
- **S3** — the pair is extracted by CONTENT, not by column ordinal: the handle is the row's first
  backticked cell and the carrier is the row's `M<n>` token wherever it sits. A row carrying two
  `M<n>` tokens is a refusal, because then the join has no single answer to read.
- **S4** — arm B: every cited `M<n>` resolves to a `^## M<n>` heading in
  `$M/guides/BUILD-METHOD.md`. SILENT when that file is absent.
- **S5** — arm C: `DIRECTIVES_FLOOR` declared and numeric, and the core member count at or above it.
  Undeclared is a refusal and malformed is a refusal, mirroring `CORE_FLOOR`'s two branches.
- **S6** — an absent `SKILL.template.md` is a NAMED refusal. A shipped kit always has one, so its
  absence is a broken install and not an adopter choice.
- **S7** — the LEG's default-init line at the top of `check-unattended.sh` gains `DIRECTIVES_EXTRA`
  and `DIRECTIVES_FLOOR`, so a conf omitting either does not abort the leg under `set -u`. The conf
  keys themselves are unit 2's, already declared before this unit lands; this unit is their first
  reader.
- **S8** — `tools/unattended/check-unattended.test.sh`: the fixture kit dir gains a copy of
  `SKILL.template.md`, `mkconf` emits `DIRECTIVES_FLOOR` derived from the driver the way
  `CORE_FLOOR_DERIVED` already is, and every refusal above gets a RED arm beside the green control.
- **S9** — the same commit carries the bookkeeping the new branches create: a
  `memory/project/method-carriers.txt` row for this leg, the `ARMS_FLOORS` raise, the leg header's
  check-count word, and the charter's gate-suite count moved by the one check this unit adds.
- **S10** — `tools/unattended/kit.toml` gains `DIRECTIVES_FLOOR` to `required_keys_gate` and
  `DIRECTIVES_EXTRA` to `optional_keys`, plus a `directives-floor` `[[hole]]` mirroring the existing
  `core-floor` one. Arm C is what makes an undeclared key a refusal, and the deployer reads that TOML
  to tell an adopter which keys their conf owes — so the declaration ships in the same commit as the
  branch, not six units later, or an adopter deploys green through govkit and reds their own
  `unattended kit gate` with no declared key and no hole. That is the half-stamped class the
  `core-floor` hole exists for.

## 3. Non-goals (OUT)

- **The table.** Unit 9 authors it; this unit only joins to it. The dependency runs both ways in
  practice — `unattended kit gate` carries no `guard`, so landing a both-directions join before the
  table exists reds every commit until it does.
- **The constant.** Unit 2.
- **The protocol's own phase and DoD tables.** Unit 22 extends this arm's shape to them, after unit
  18 has written the two rows it would otherwise red on.
- **The waiver record and the kickoff order.** Checks 17 and 18, units 13 and 14.
- **Grading the gloss column.** No gate can see a gloss growing from a name into a restatement of the
  rule it points at. Arm A pins the pairs, `check-method-carriers.sh` catches a copied section
  heading, and the gap between them is the review lens's, recorded as a build residual.

## 4. Design

### Data model

Arm A reduces both sides to the same set of `handle M<n>` pairs and diffs them. The driver side comes
from `core_of DIRECTIVES_CORE` — the parser that already reads `PHASES_CORE`, `DOD_CORE` and
`PHASES_TERMINAL` out of the driver rather than sourcing a script whose tail runs a verb. The Skill
side comes from the row selector in S2.

### Why the join is on content and not on a column ordinal

The design pass specified "columns 1 and 4". Unit 9's S2 names FOUR columns in the order handle,
gloss, carrier, owner directive, and its S5 adds a fifth fact to one row — so the carrier is not at
ordinal 4 and the count is not fixed. Column order is authorial and will move again; the pair is not.
Reading the handle as the first backticked cell and the carrier as
the row's sole `M<n>` token survives every column edit that keeps the two facts on the row, and S3's
two-token refusal is what stops the "sole" from being an assumption.

### Why an empty extraction is a refusal

A selector that matches nothing passes by finding nothing, and this repo has been bitten by that
shape often enough to have named it. The leg already answers it twice: check 1 refuses when
`core_of` returns empty, *"so every membership check below would pass over an empty set"*, and
`check-method-carriers.sh` refuses an empty carrier population for the same reason. Arm A joins that
list. It also removes the only argument for putting a marker pair into the Skill template — the
marker exists to make a renamed heading loud, and a refusal on an empty extraction is loud already.

### Why arm B is silent when the carrier is absent

The leg grades the TREE; the driver grades the RUN. A tree that ships no build method is a tree where
the pointers cannot be resolved, and refusing there would red a bar the adopter cannot make green.
The RUN's obligation is unit 4's: `--preflight` refuses when the carrier is missing. This is the same
disposition check 12 already takes for a blank `KICKOFF_ENGINE`, and the two are consistent on
purpose.

### One constraint on how arm B is spelled

This leg becomes a method carrier the moment it contains the literal `BUILD-METHOD.md`, so it needs a
`method-carriers.txt` row. That registry's check 5 then greps it for `^## M[0-9]+`, the shape a COPY
takes. Arm B's own pattern must therefore never begin a source line — it sits inside a `grep`
invocation, which is where it would naturally sit anyway. Stated because it is the kind of constraint
found the second time, in a red gate.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | check 16 arms A, B and C; two default-init keys; the header's check count |
| `tools/unattended/check-unattended.test.sh` | the template copy into the fixture, the derived floor in `mkconf`, one arm per refusal |
| `memory/project/method-carriers.txt` | one row for this leg |
| `.memory-tree.conf` | `ARMS_FLOORS` for this leg, raised by the branch count |
| `tools/unattended/kit.toml` | the two key lists and the `directives-floor` hole |
| `AGENTS.md` | the gate-suite bullet's check count, fifteen to sixteen |

### Alternatives rejected

- **Rendering the table into the Skill from the constant at adopt time.** It converts a
  second-opinion join into a generator and its output, which checks nothing, and it makes the gloss
  column unwritable. Rejected once already in unit 9 and recorded there.
- **Joining the gloss column too.** There is nothing to join it against; see the non-goal.
- **Extending `CORE_FLOOR` to a triple.** Rejected in unit 2 on the leg's own recorded failure mode:
  one malformed value already disarms both pins, and a third field makes one typo disarm three.

## 5. Production-readiness checklist

- security — N/A. The leg stays READ-ONLY, and its own source-level arm greps for a write.
- perf / scale — one extra file read per invocation. `core_of` is already the pure-bash accessor.
- a11y · i18n — N/A.
- error / empty / loading states — the three named refusals: empty extraction, absent template,
  undeclared or malformed floor. Each leaves the leg reporting rather than skipping.
- observability — every branch prints its own sentence; nothing is silent except arm B on an absent
  carrier, and that silence is argued above.
- risks — the gloss column is ungated, and the fixture's green control must be re-verified in this
  commit: it copies only three kit files today, so both new arms would fire on a conforming tree
  unless the fixture moves with them.
- testing + left-shift gates — `unattended gate selftest`, one arm per refusal, each observed RED
  before its branch is written.
- migration / rollback — additive. The check is inert until `DIRECTIVES_CORE` exists, which is why
  this unit is sequenced after unit 2 and unit 9.
- user docs — the protocol's new §10 is unit 18; this leg's own comments carry the rest.

## 6. Acceptance criteria

- **AC1** — When a row is added to the Skill's table and the constant is not touched, the leg reds
  naming the unmatched handle.
- **AC2** — When a member is added to `DIRECTIVES_CORE` and the table is not touched, the leg reds
  naming the unmatched handle.
- **AC3** — When a row cites an `M<n>` with no `^## M<n>` heading in the build method, arm B reds;
  when the build method is absent from the fixture, arm B prints nothing.
- **AC4** — When the row selector matches nothing, the leg reds with the empty-extraction refusal
  rather than exiting 0.
- **AC5** — When `DIRECTIVES_FLOOR` is undeclared, and again when it is non-numeric, the leg reds.
- **AC6** — The fixture's green control still exits 0 and prints nothing with all three arms live.
- **AC7** — `python tools/memory-tree/check-arms.py` is green with the raised `ARMS_FLOORS`, and red
  with the floor left at 39:39. The absolute is safe to spell here: this is the first unit in the
  build that touches `check-unattended.sh`, so nothing has moved that pin ahead of it.
- **AC8** — `python tools/govkit/govkit.py selfcheck` is green with S10's `kit.toml` edit, and the
  `directives-floor` hole's discharge probe passes against this repo's own `.unattended.conf`.

## 7. Gates

`unattended gate selftest` (`tools/unattended/check-unattended.test.sh`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`) · `method carriers`
(`tools/memory-tree/check-method-carriers.sh`) · `harness arms`
(`tools/memory-tree/check-arms.py`) · the full bar.

**No leg is added.** Check 16 rides `unattended kit gate`, which already exists, so
`tools/gate-legs.json`, the dossier's `gate-legs` claim and the codebase-map re-render are all
untouched. The charter's gate-suite bullet is the one of the four that does move, and only because it
spells a check COUNT the bar does not read — which is exactly why it rots, so it moves in this commit.

## 8. Open questions

**Does arm A read the template or the render? — RESOLVED at authoring: the template.**
`adopt-unattended.sh --check` already diffs the render against a fresh render of the template, and it
is a leg on this bar. Reading both here would be a second answer to a question one leg already owns,
and the fixture would need a rendered Skill it has no adopter to produce. This is a decision by the
spec's author, not a fork the owner declined.

**Does arm C's floor pin the CORE count or the EFFECTIVE count? — RESOLVED at authoring: CORE.**
`DIRECTIVES_FLOOR` mirrors `CORE_FLOOR`, which counts `PHASES_CORE` and `DOD_CORE` and not the
composed sets — because the effective set is composed as core plus the project's extras, so core is a
subset by construction and a floor over the effective set could be held up by extras while a core
member was deleted underneath it. That vacuity was measured on the phase floor's first cut and is
recorded in the leg's own comment.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C10, D4, D5, D8 and FG-10's
  reasoning about count-only checks. Corrects the design's "columns 1 and 4" against unit 9's
  four-column table, whose S5 adds a fifth fact to one row.
- rev-2 · 2026-08-14 · two cross-read corrections. S10 is new: `tools/unattended/kit.toml` was in no
  unit's scope, so arm C's undeclared-`DIRECTIVES_FLOOR` refusal would have shipped without the
  deployer declaration an adopter reads, which is the half-stamped class the `core-floor` hole was
  written for. And this log said "five-column table" where §4 and unit 9's S2 both say four.

## 10. Reuse audit

- **`core_of()` in `tools/unattended/check-unattended.sh`** — the seam. It parses a `KEY="…"` line
  out of the driver and already serves three constants; `DIRECTIVES_CORE` is the fourth and the
  parser needs no change.
- **`CORE_FLOOR`'s two branches** — the undeclared refusal and the malformed refusal, both already
  written with their reasoning. `DIRECTIVES_FLOOR` copies the behaviour and deliberately not the
  spelling, so one malformed value cannot disarm two pins.
- **Check 12's declared-off silence** — the precedent for arm B's disposition on an absent carrier.
- **`check-method-carriers.sh`'s registry** — the existing declaration surface for a file that points
  at the build method — ten rows today. This leg becomes a carrier the moment arm B spells the
  path, and it takes a row rather than a new mechanism.
- **The fixture's `CORE_FLOOR_DERIVED`** — the shape for deriving a floor from the driver inside the
  self-test, so the fixture cannot drift from the constant it grades.

Recall terms used: unattended gate leg check directive registry core floor shrink-only skill template
table join both directions build method section pointer carrier fixture arm vacuous selector.
