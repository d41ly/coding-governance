# TOOL-cBriefedPilot-6 — `--plan` sees the planned unit that has no spec

**Status:** CLOSED · rev-4 · 2026-08-16 · node c · Tier-2 · base 37c05e1b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Join the build README's authored roster to the tracked specs, so `--plan` reports a planned unit that
nobody has specced instead of enumerating the half of the roster it can see. This is finding F3: M2
names the README's Units table as the roster, and `verb_plan` deliberately does not parse it.

## 2. Scope (IN)

- **S1** — `roster_ids <slug>`: the ids inside the README's roster marker pair, matched as
  `[A-Z]+-<slug>-[0-9]+`, sorted and deduplicated. Presence of the pair is decided by grepping for
  `ROSTER_OPEN`, never by `region`'s exit status.
- **S2** — `spec_ids <dir>`: the ids `verb_plan` already derives — the level-one heading's first token
  on a tracked spec that carries a status header. Extracted so the listing and the join cannot
  disagree about what a unit's id is.
- **S3** — `missing_units <slug>`: the S1 set minus the S2 set. `verb_plan` prints one row per member
  in its existing three-column shape, with the state `MISSING`.
- **S4** — a NAMED refusal when the README carries `ROSTER_OPEN` but not exactly one well-formed
  pair. Its check number is DERIVED at build time as the next free one above every number then
  spelled in the driver, exactly as this unit's `ARMS_FLOORS` sentence is already stated relatively.
  A literal is wrong here: unit 3 lands first and takes 37 through 41, so an arithmetic counting only
  unit 4 is stale before it is read. It adds no second `fail 19`, so no existing per-check ordinal
  moves and the one row in `memory/project/unarmed-branches.txt` stays valid.
- **S5** — the `roster:` summary line is rewritten by case. With a roster it names the roster region
  and the id count; with no roster it keeps today's sentence, whose caveat is then true.
- **S6** — `unit_rows <run-state file>` and `nonterminal_units <run-state file>` extracted out of
  `verb_status`'s inline pipeline, the second a filter over the first. `verb_status`'s output is
  byte-identical across the extraction.
- **S7** — arms in `unattended.test.sh` for the malformed pair, the MISSING row, the no-roster path
  and the `verb_status` byte-identity, plus the `ARMS_FLOORS` raise for the one branch S4 adds, in
  the same commit as the branch.

## 3. Non-goals (OUT)

- **A second roster.** The marker pair already exists in the driver at `ROSTER_OPEN` /
  `ROSTER_CLOSE` and `check_authorization` already reads it. This unit adds a reader, not a grammar.
- **Blocking on a MISSING unit.** `--plan` reports; `build-complete` blocks. That item is unit 7, and
  it is what makes this unit's join consequential rather than advisory.
- **Making the roster mandatory.** The obligation P3 resolved is stated and enforced in unit 7. Here
  an absent roster is the documented no-roster path, exactly as today.
- **Reading `verb_plan`'s exit status or grepping its stdout.** Nothing in the kit does either, and
  wiring a consumer to this verb's text would make a reworded row a silent behaviour change.
- **A filename join to `reviews/`.** Already measured wrong on 7 of 7 multi-unit builds in this
  corpus and recorded in the driver's own comment; nothing here revives it.

## 4. Design

### Data model

The roster region is a slice of the build README, not a new file. Its ids are matched against the
build's OWN slug, which is why the pattern interpolates `$slug` rather than accepting any
`FAMILY-something-N`: a roster row that cites a sibling build's id names a dependency, not a unit of
this build, and a looser pattern would mint units out of prose.

`missing_units` is a set difference and nothing more. Both sides come from one extraction each — S1
from the README, S2 from the same lines `verb_plan` already reads — so a spec whose heading and
status header disagree is invisible to both halves in the same way, rather than counted as present by
one and absent by the other.

### Why the malformed pair is a refusal and not a skip

`region` exits 3 for an absent pair AND for a malformed or duplicated one. Treating that single
status as "absent" is the discarded-signal defect this kit has already paid for once, and
`check_authorization` carries the fix in writing at its own roster block: grep the open marker to
decide presence, then let a non-zero `region` mean malformed. A build whose roster markers are
duplicated or transposed would otherwise get today's complete-looking list back, which is the exact
output this unit exists to stop printing.

### Why `verb_status`'s pipeline moves in this unit

`verb_status` holds the non-terminal-unit selection inline. Unit 7's `build-complete` needs the same
two questions — is there any unit row at all, and is any of them non-terminal — and a second copy of
that pipeline would be two answers to one question in the two verbs that report on the same region.
The extraction lands here, ahead of the behaviour change that consumes it, with a byte-identity
acceptance criterion, so a refactor and a new rule are never in the same reviewable diff.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | five helpers, the `verb_plan` wiring, the check-37 refusal, the `roster:` line |
| `tools/unattended/unattended.test.sh` | four arms plus the byte-identity control |
| `.memory-tree.conf` | `ARMS_FLOORS` for the driver, raised by the one branch S4 adds, relative to whatever units 1 through 5 left |

### Alternatives rejected

- **Locating the roster structurally** — the slice between one heading and the next. Refused when the
  marker pair was introduced, for the reason recorded beside it: a renamed heading silently empties
  the comparison, which is a check that passes by finding nothing.
- **Deriving the roster from the README front matter's `ids:` key.** M2 names that key as a
  reservation range written as ranges and unions, and says in the same paragraph that reading it as a
  unit list drops every unit after the first.

## 5. Production-readiness checklist

- security — N/A, a read of two tracked files.
- perf / scale — one `region` and one `git ls-files` per invocation, on a verb an agent calls between
  passes.
- a11y · i18n — N/A, no user surface.
- error / empty / loading states — three states are distinguished by construction: no roster pair, a
  malformed pair, and a roster naming ids. The middle one is the branch S4 adds.
- observability — the MISSING rows and the rewritten `roster:` line are the whole output surface.
- risks — a roster that names no id at all is indistinguishable here from a roster naming ids that
  all have specs; both print no MISSING row. Unit 7's item is where that difference is made to
  matter, and it is stated in that spec rather than guessed at here.
- testing + left-shift gates — the four arms in S7. The join is exercised again from the other side
  by unit 7's `--close` fixtures.
- migration / rollback — additive. A build with no roster markers gets today's behaviour and today's
  sentence.
- user docs — the Skill's `--plan` blurb and protocol §7's `--plan` bullet both currently say the verb
  cannot see an unspecced planned unit. This unit is what falsifies both. The protocol bullet is unit
  18's S6 and the Skill blurb is unit 11's S5, each named in that unit's own scope; until they land
  the two documents understate what the verb does rather than overstating it.

## 6. Acceptance criteria

- **AC1** — When the README's roster names two ids and only one carries a tracked spec, `--plan`
  prints exactly one `MISSING` row, for the id with no spec.
- **AC2** — When the README carries a roster open marker and a second, transposed or duplicated one,
  `--plan` refuses with check 37 naming the README path, and prints no unit rows.
- **AC3** — When the README carries no roster marker, `--plan`'s output is unchanged from today,
  including the sentence that a planned unit with no spec is invisible.
- **AC4** — `--status`'s next-unit line is byte-identical before and after the S6 extraction, on a
  fixture with one non-terminal unit and one terminal one.
- **AC5** — The new refusal is observed RED with its arm in place and its branch removed, and
  `python tools/memory-tree/check-arms.py` is green with the branch armed and the floor
  raised, and RED when the branch is present and its arm is removed — twice over: once naming
  the unarmed branch, once at the armed count against the raised floor. *An UNRAISED floor does
  NOT red on an added branch: `ARMS_FLOORS` is a one-sided minimum, so a higher count passes.
  Measured on unit 4, where the same wording was an acceptance criterion no run could fail.*

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `harness arms`
(`tools/memory-tree/check-arms.py`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`) · the full bar at the push boundary.

## 8. Open questions

none — the one decision this unit could have deferred is settled by the build's own framing. A
malformed roster pair is a NAMED refusal rather than a silent fall-through to the no-roster path,
because the two states differ in exactly the way the discarded-signal class describes and this kit
has already shipped that mistake once.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds FG-4, FG-6 and FG-11.
- rev-2 · 2026-08-14 · two cross-read corrections against the sibling set. The refusal moves from
  check 34 to 37: unit 4 takes 34 and lands first, and 34 was the driver's ONLY gap — measured, the
  driver spells `fail` 1 through 33, 35 and 36 — so both units claiming it would have renumbered a
  landed unit's ordinal under its own arm pin. And the `ARMS_FLOORS` move is stated RELATIVELY, as
  every sibling that raises the same floor already states it: units 3 and 4 add six branches to this
  file ahead of this unit, so the absolute pair this spec named was stale before it could be read.

- rev-3 · 2026-08-15 · §8's audit fold. S4's check number is DERIVED rather than the literal 37, which was stale before it
  could be read: unit 3 lands first and takes 37 through 41.
- rev-4 · 2026-08-15 · the acceptance criterion asserting that an UNRAISED `ARMS_FLOORS`
  reds is corrected against measurement. It cannot: the floor is a one-sided minimum and a
  higher branch count passes. Found on unit 4 and swept across the set; three specs carried it.

## 10. Reuse audit

- **`region()` and the `ROSTER_OPEN` / `ROSTER_CLOSE` pair in `tools/unattended/unattended.sh`** —
  the reader and the grammar. Both already ship; `check_authorization` is the existing consumer, and
  this unit adds the second one rather than a second grammar.
- **`check_authorization`'s presence-then-parse idiom** — grep the open marker, then let a non-zero
  `region` mean malformed. Copied as a discipline, not as code: the two callers ask different
  questions of the same slice.
- **`verb_plan`'s id and status-header extraction** — S2 lifts it into `spec_ids` and both consumers
  read the one function, so the roster join and the printed listing cannot disagree.
- **`verb_status`'s non-terminal-unit pipeline** — extracted, not duplicated, and consumed by unit 7.

Probes run at authoring. `python tools/codebase-map/reuse_lookup.py "unattended run definition of
done item checked at close"` returned no seam for a roster reader; its top hits are the generic
`run` and `check` name stems and the `.unattended.conf` affordance seam, which is a miss recorded as
an answer. Recall terms used: unattended close DoD override roster README region generated units plan
spec status terminal review base.
