# TOOL-dBriefedPass-5 — the carriers declare the harness the route, and the brief the obligation

**Status:** CLOSED · rev-4 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-TOOL-dBriefedPass-5-1-carriers.md](../build/2026-09-01-build-TOOL-dBriefedPass-5-1-carriers.md) | journal | — |
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |
| [2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |

<!-- /gen:spec-records -->

## 1. Goal

Bind the three mechanisms this build ships. The protocol declares the harness the route a
`prompt`-mode or `slug`-mode build's passes take, declares the brief an obligation of a build pass,
and the rendered Skill and the build method point at those rules without restating them.

## 2. Scope (IN)

- **S1** — `tools/unattended/PROTOCOL.template.md` gains one section stating: the harness is the
  route for `prompt` and `slug` modes; a build pass owes a recorded BRIEF; and a build pass is
  declared through `--dispatch`, which is what makes `TOOL-dBriefedPass-3`'s refusal reachable on a
  sequential pass and not only a concurrent one.
- **S2** — the same section states the harness's TWO LIMITS as rules rather than as caveats: it
  cannot read the tree, so it buys order and never enforcement; and it does not cover orientation,
  preflight, the owner turn, closing, landing or the keepalive.
- **S3** — `tools/unattended/SKILL.template.md` gains the HARNESS to its "While it runs" section, in
  the shape that file already uses, and its directive table gains one handle. It does NOT carry the
  `--brief` rows: check 26 joins a verb to three carriers and the leg that runs it is unguarded, so
  those rows land with the verb in `TOOL-dBriefedPass-2` or the bar is red for three units.
- **S4** — a new kit-owned directive `passes-harnessed`, scoped `all`, pointing at the build method
  section the harness implements. `DIRECTIVES_FLOOR` moves from 16 to 17 in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`, because that pin is a shrink-only SIZE and adding a
  member without moving it leaves the new one unpinned.
- **S5** — `memory/guides/BUILD-METHOD.md` IS NOT TOUCHED BY THIS UNIT. Its M6 pointer sentence was
  in scope at rev-1 and is withdrawn: the file has 16 bytes of headroom against M1's declared 24576
  and its byte-compared template half has 5, and M3 reserves M1's own budget from a standing
  mandate's delegated authority, so a sentence that does not fit is not this run's to make room for
  by raising the cap. `TOOL-dBriefedPass-1` S6 owns the one BUILD-METHOD edit this build makes and
  states its own byte constraint. M11's pointer table already carries the protocol, so the harness
  rule is reachable from the method without a new sentence in it.
- **S6** — the protocol and skill renders are regenerated so the parity legs that byte-compare
  template against render stay green, and the kit VERSION is bumped where it actually lives:
  `tools/unattended/kit.toml:6` declares `version_from = { file = "unattended.sh", pattern =
  "^KIT_UNATTENDED_VERSION=" }`, so the number is in the driver and the descriptor merely points at
  it. The bump is therefore an edit to `unattended.sh`'s constant plus every `gov:kit unattended@`
  marker the `kit version markers` leg joins to it. At rev-3 this item said the descriptor records
  the bump, which would have had a builder editing a file that carries no version.
- **S7** — WITHDRAWN. The protocol's section 7 verb row for `--brief` lands at order 2 with the verb
  itself, per `TOOL-dBriefedPass-2` S8, for the reason S3 already gives about the Skill's rows:
  check 26 joins a verb to three carriers on an unguarded leg, so a row claimed at order 5 reds the
  bar for three units. This unit adds NO verb row to any carrier. Its rev-2 ground was also false —
  `TOOL-dUnstalledConvoy-17` says the list is "incomplete and joined to nothing", and check 26
  landed 2026-08-21, the day after that row, joining all 17 declared verbs to a row in both the
  template and its render. What survives of that row is the reverse direction and its ordering
  principle, neither of which this unit touches.

## 3. Non-goals (OUT)

- The protocol's convergence rule is NOT changed and no review-round cap is added. Owner ruling,
  2026-09-01, at this run's single turn: the prompt proposed a two-round default and the owner kept
  convergence.
- `TOOL-dUnstalledConvoy-17`'s underlying defect — that nothing joins the protocol's verb list to the
  driver's three enumerations — is not fixed here. Adding one row to a list is not the same act as
  gating the list, and conflating them would smuggle a new gate past the round meant to price it.
- The charter template is not edited. Its §1 unattended block already points at the protocol by name
  and says explicitly that it is not paraphrased there.
- No new conf key is added by this unit. `PASS_ORDER_CUTOFF` belongs to `TOOL-dBriefedPass-3`, and
  so does the history-reading gate leg. The build README's roster cell for this unit said otherwise
  at rev-1 and the roster was the side corrected, because spec 3 S3/S4/S6 already own that leg.

## 4. Design

### Inventory

The carriers touched, what each gains, and the leg that grades it:

| carrier | gains | graded by |
|---|---|---|
| `PROTOCOL.template.md` | the harness section, the brief obligation, the dispatch requirement | protocol parity legs |
| `memory/guides/UNATTENDED-PROTOCOL.md` | the render of the above | the same, byte-compared |
| `SKILL.template.md` | the harness in "While it runs", one directive row | `unattended skill wiring` |
| `.claude/skills/unattended/SKILL.md` | the render | `check-wiring.sh` |
| `.unattended.conf` and its example | `DIRECTIVES_FLOOR` 16 to 17 | the directive floor pin |
| `unattended.sh`'s version constant and every `gov:kit unattended@` marker | the kit version bump | `kit version markers` |

`memory/guides/BUILD-METHOD.md` and its template are NOT in this table, by S5. They form a render
pair that `tools/memory-tree/kit-dogfood-parity.test.sh` byte-compares as the leg
`kit/dogfood doc parity`, so a unit editing one owes the other; `TOOL-dBriefedPass-1` owns that pair
and names both halves and that leg.

The parity legs compare the two COPIES to each other, so a claim false in both is green — the
protocol's own header says three defects survived exactly that way. The prose added here is therefore
graded by the closing review and not by a leg, and this unit says so rather than implying otherwise.

### Migration

`passes-harnessed` binds every unattended run from the commit it lands. It is a POINTER into the
build method, not a new obligation: M6 already requires the pass sequence this harness performs, and
the directive is what makes the obligation waivable-with-a-reason rather than silent.

### Alternatives rejected

- **Scope the directive to `prompt` only.** Rejected: a `slug`-mode build has the same pass set and
  the same defect. The owner's prompt names both modes explicitly.
- **State the harness rule in the build method instead.** Rejected by M1: the method forbids a rule
  living both there and in a carrier it points at, and the mandate-specific half belongs to the
  protocol, which is the mandate's contract.
- **Make `--dispatch` mandatory by a machine check.** Rejected as out of scope here and recorded
  rather than dropped: the observation would have to be "no build commit exists without a preceding
  dispatch row", which is a second history join over the same range as `TOOL-dBriefedPass-3`'s. It is
  a backlog row, not a fold.

### Files touched (estimate)

The carriers named in the inventory table above. No count is written here: the table owns it, and a
number authored beside the table that owns it is wrong on the next edit.

## 5. Production-readiness checklist

- **Security · data · write surface** — none. This unit edits documents and one numeric pin.
- **Performance** — none.
- **Error states** — the directive floor refuses if the count and the pin disagree, in both
  directions, which is the arm that proves S4 was done in both files.
- **Observability** — a waiver of `passes-harnessed` is recorded as a parked `waiver` entry and
  surfaces in the wrap-up, like every other directive.
- **Testing** — the parity legs plus AC4's floor arm.
- **Migration · rollback** — reverting is the seven files and the pin.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/run-unattended-gates.sh --checks` is green, which is where the
  protocol and skill parity legs live.
- **AC2** — `bash tools/unattended/adopt-unattended.sh --check` is green, which IS the
  `unattended skill wiring` leg by its declared argv, so the render in `.claude/skills/unattended/`
  is not left behind. `tools/check-wiring.sh --check` was named at rev-3 and is the SessionStart
  wiring check, a different program from the leg this criterion claims to observe.
- **AC3** — under `bash tools/unattended/run-unattended-gates.sh --checks`, the directive handle appears in BOTH the driver's core set and the rendered Skill's
  table. The leg joins the two in both directions, so a handle in one and not the other is a refusal;
  this arm observes that refusal by staging the handle in only one and confirming RED.
- **AC4** — `DIRECTIVES_FLOOR` at 16 with 17 core directives is a REFUSAL, and at 17 it is green.
  Both arms, so the pin is proven armed rather than assumed.
- **AC5** — `git diff --name-only` for this unit's commit names NO file under
  `memory/guides/BUILD-METHOD.md` or `tools/memory-tree/BUILD-METHOD.template.md`. The negative
  criterion is the observable form of S5's withdrawal, and it is checkable; at rev-1 this criterion
  asserted a budget held after an edit that does not fit in 16 bytes.
- **AC7** — `bash tools/unattended/check-unattended.sh` check 26 is green over every verb this build
  declares, asserting that the carrier rows S3 declines are present because
  `TOOL-dBriefedPass-2` S8 landed them, not because nobody looked.
- **AC6** — `memory/guides/UNATTENDED-PROTOCOL.md` states both limits from S2. Graded by the closing review, and this
  criterion names that reader explicitly rather than pretending a leg reads prose.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` · `unattended skill wiring` ·
`kit version markers` · `memory hygiene`. Every name resolves against `tools/gate-legs.json`.
`method carriers (every pointer declared)` and `template size <=48KiB` were listed at rev-2 and are
dropped: S5's withdrawal means this unit touches no method carrier and no charter template.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.
- rev-2 · 2026-09-01 · round-1 spec-audit fold. B2 (finding 16): S5's M6 sentence could not fit —
  `memory/guides/BUILD-METHOD.md` measures 24560 bytes against a 24576 cap, and AC5 asserted the
  budget held while never having measured the headroom, so the criterion would have read as verified
  on a false premise. S5 is withdrawn and AC5 becomes the negative observation. B3 (finding 17): the
  inventory omitted `tools/memory-tree/BUILD-METHOD.template.md`, the byte-compared half of a render
  pair whose leg is `kit/dogfood doc parity` and whose blob has 5 bytes of headroom; the pair now
  belongs to `TOOL-dBriefedPass-1` in one place, and this file says so. B1's share (finding 1): the
  `--brief` carrier rows leave S3 for `TOOL-dBriefedPass-2` S8, and AC7 observes the join. M1
  (finding 26): the README roster cell claimed this unit ships the history leg while §3 declines it;
  the roster was corrected.
- rev-3 · 2026-09-01 · round-2 spec-audit fold. S7 is WITHDRAWN, which closes five findings at once:
  H7, H8 and H9 (findings 36, 31 and 13) each read the same claim from a different axis — S7 claimed
  a check-26 carrier row that `TOOL-dBriefedPass-2` S8 already claims at order 2, which is the half
  of round 1's B1 fix that was not carried through; M4 (finding 10) is that S7 had no criterion of
  its own and the criterion that exists credits another unit; and L1 (finding 41) is that S7's
  stated ground was superseded by check 26 the day after the row it cites was written. M5 and M7
  (findings 19 and 9): the `SKILL.template.md` inventory cell said "two verbs" while S3 negates it
  in the same document. M6 (finding 40): §4 Files touched authored a row count beside the table that
  owns it.
- rev-4 · 2026-09-01 · round-3 spec-audit fold. H4: S6 asked `tools/unattended/kit.toml` to record
  the version bump, and that file carries `version_from` pointing at a constant in `unattended.sh` —
  `check-kit-versions.sh` never reads a version out of the descriptor, so the instruction named a
  file with no version in it. H2: AC2 named `tools/check-wiring.sh --check` as the
  `unattended skill wiring` leg, whose argv is `bash tools/unattended/adopt-unattended.sh --check`.

## 10. Reuse audit

No existing seam fits, and the evidence is that this unit's work is document edits in seven named
carriers rather than code: `python tools/codebase-map/reuse_lookup.py "declare a new directive and
render it into the skill and protocol"` returns the render and parity machinery
(`tools/playbook/render_playbook.py`, the protocol parity test) but no seam to extend, because
adding a directive is a data edit in a declared set the kit already owns. The mechanism this unit
FOLLOWS rather than extends is `TOOL-cBriefedPilot-2`, which established that the core directive set
is kit-owned with a shrink-only floor, and `TOOL-cSettledDocket-2`, which established the
project-owned row source — both read before writing S4, and both are why the floor moves in two files
rather than one.

Recall terms used: unattended mandate pass ordering workflow harness spec before code regrounding
compaction driver orchestration agent-cap fan-out build-method handoff prompt.
