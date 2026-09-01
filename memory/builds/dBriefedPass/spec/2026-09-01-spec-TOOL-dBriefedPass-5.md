# TOOL-dBriefedPass-5 — the carriers declare the harness the route, and the brief the obligation

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 |

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
- **S3** — `tools/unattended/SKILL.template.md` gains the harness to its "While it runs" verbs and
  the `--brief` verb to the same place, in the shape that file already uses. Its directive table
  gains one handle.
- **S4** — a new kit-owned directive `passes-harnessed`, scoped `all`, pointing at the build method
  section the harness implements. `DIRECTIVES_FLOOR` moves from 16 to 17 in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`, because that pin is a shrink-only SIZE and adding a
  member without moving it leaves the new one unpinned.
- **S5** — `memory/guides/BUILD-METHOD.md` M6 gains ONE sentence naming the harness as how a pass
  sequence is performed under a mandate, and nothing else. M1 forbids a rule appearing both there and
  in a carrier it points at, so the rule stays in the protocol and M6 carries the pointer.
- **S6** — both rendered copies are regenerated so the parity legs that byte-compare template against
  render stay green, and `tools/unattended/kit.toml` records the version bump.
- **S7** — the protocol's section 7 verb list gains `--brief`. `TOOL-dUnstalledConvoy-17` records
  that this list is already incomplete and joined to nothing; this unit does not widen that gap.

## 3. Non-goals (OUT)

- The protocol's convergence rule is NOT changed and no review-round cap is added. Owner ruling,
  2026-09-01, at this run's single turn: the prompt proposed a two-round default and the owner kept
  convergence.
- `TOOL-dUnstalledConvoy-17`'s underlying defect — that nothing joins the protocol's verb list to the
  driver's three enumerations — is not fixed here. Adding one row to a list is not the same act as
  gating the list, and conflating them would smuggle a new gate past the round meant to price it.
- The charter template is not edited. Its §1 unattended block already points at the protocol by name
  and says explicitly that it is not paraphrased there.
- No new conf key is added by this unit. `PASS_ORDER_CUTOFF` belongs to `TOOL-dBriefedPass-3`.

## 4. Design

### Inventory

The carriers touched, what each gains, and the leg that grades it:

| carrier | gains | graded by |
|---|---|---|
| `PROTOCOL.template.md` | the harness section, the brief obligation, the dispatch requirement | protocol parity legs |
| `memory/guides/UNATTENDED-PROTOCOL.md` | the render of the above | the same, byte-compared |
| `SKILL.template.md` | two verbs, one directive row | skill render parity |
| `.claude/skills/unattended/SKILL.md` | the render | `check-wiring.sh` |
| `.unattended.conf` and its example | `DIRECTIVES_FLOOR` 16 to 17 | the directive floor pin |
| `BUILD-METHOD.md` M6 | one pointer sentence | method carriers leg |
| `tools/unattended/kit.toml` | version bump | kit version markers |

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

The seven rows of the inventory table above.

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
- **AC2** — `bash tools/check-wiring.sh --check` reports the installed Skill matches tracked, so the
  render in `.claude/skills/unattended/` is not left behind.
- **AC3** — under `bash tools/unattended/run-unattended-gates.sh --checks`, the directive handle appears in BOTH the driver's core set and the rendered Skill's
  table. The leg joins the two in both directions, so a handle in one and not the other is a refusal;
  this arm observes that refusal by staging the handle in only one and confirming RED.
- **AC4** — `DIRECTIVES_FLOOR` at 16 with 17 core directives is a REFUSAL, and at 17 it is green.
  Both arms, so the pin is proven armed rather than assumed.
- **AC5** — `memory/guides/BUILD-METHOD.md` stays inside its declared budget of 24 KB and 350 lines
  after S5's sentence. Measured, not assumed: M1 states the byte half binds first.
- **AC6** — `memory/guides/UNATTENDED-PROTOCOL.md` states both limits from S2. Graded by the closing review, and this
  criterion names that reader explicitly rather than pretending a leg reads prose.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` · `method carriers (every pointer
declared)` · `kit version markers` · `memory hygiene` · `template size <=48KiB`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.

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
