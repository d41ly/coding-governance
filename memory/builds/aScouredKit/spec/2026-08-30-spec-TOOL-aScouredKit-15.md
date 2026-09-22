# TOOL-aScouredKit-15 — the drift-audit Skill stops pointing at a directory govkit never creates

**Status:** CLOSED · rev-2 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round3.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round3.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 |
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-30 TOOL-aScouredKit-31 TOOL-aScouredKit-32 |

<!-- /gen:spec-records -->

## 1. Goal

Stop `adopt-drift-audit.sh` from rendering a Skill whose two deep-tier commands name files that do
not exist in a govkit-deployed tree, and stop its `--check` arm from reporting that Skill in sync.

## 2. Scope (IN)

- S1. `DRIFT_WORKFLOWS_REL` overrides the derived sibling directory for a HAND-INSTALL, where one
  person runs both `adopt` and `--check` and can export it for both. It is NOT a deployment
  channel, and the attempt to make it one was withdrawn by `TOOL-aScouredKit-30`.
- S2. Both rendered paths are ASSERTED against the filesystem, and the result is REPORTED in both
  modes at exit 0. The original wording said `--check` REDS; `TOOL-aScouredKit-30` changed that
  to a report, because this kit does not require the review-harness kit and cannot distinguish
  "not installed" from "installed elsewhere" without the token `TOOL-aScouredKit-26` describes.
- S3. The refusal names both missing paths, the reason the derivation guesses wrong, and the
  override. Its suggestion derives from this kit's own parent, never from the value being
  complained about.

## 3. Non-goals (OUT)

- Changing the default derivation. Neither `workflows` nor `review-harness` is right for both a
  hand-install and a govkit deploy, so guessing better is not the fix; asserting is.
- Teaching govkit to pass the sibling's destination into this kit's `[adopt]` argv. That is the
  durable answer and it needs a cross-entry token this descriptor language does not have; it is
  reported as a backlog row rather than invented here.
- The other rendered-pointer sites in other kits. Only this one was measured.

## 4. Design

govkit lands a kit at `{prefix}/{entry-id}`, and the harnesses' entry id is `review-harness`
(`tools/workflows/kit.toml`), not `workflows`. `adopt-drift-audit.sh` derives the sibling as
`${KIT_REL%/*}/workflows`, so an adopter at `vendor/gov` gets a Skill naming
`vendor/gov/workflows/drift-audit-code.js`, a path govkit never creates. Gov itself is correct by
COINCIDENCE — its own directory is literally `tools/workflows` and it does not deploy into itself.

The comment already at that site claims a derived value "cannot drift from the install". It cannot
drift from the PREFIX, which is a weaker property, and this is what the gap cost.

`--check` could not see it because both operands come from one generator: it renders the template
and diffs the render against the rendered Skill, so a wrong answer appears identically on both
sides. That is `assertion-between-two-derived-values`, and the filesystem is the only operand
available that the render cannot supply itself.

## 5. Production-readiness checklist

- security — `DRIFT_WORKFLOWS_REL` reaches a `[ -f ]` test and the rendered text, both of which
  already carry an operator-supplied `KIT_REL`; no new class of value reaches a command.
- perf / scale — two `[ -f ]` tests.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the absent-sibling state is the state this unit adds, in both
  modes, deliberately at different severities.
- observability — the refusal is the observable, and it names paths rather than a condition.
- risks — an adopter who selected drift-audit WITHOUT the review-harness kit now gets a red
  `--check`. That is correct and is the point: their Skill names two files they do not have. The
  adopt path warns instead of refusing so the render, which is the useful part, still lands.
- testing + left-shift gates — `bash tools/drift-audit/adopt-drift-audit.sh --check` is itself the
  gate leg, and this unit is what makes it able to fail.
- migration / rollback — no artifact changes; the rendered Skill is byte-identical on this tree.
- user docs — the refusal text is the operator-facing doc.

## 6. Acceptance criteria

- **AC1** — When `bash tools/drift-audit/adopt-drift-audit.sh --check` runs on this tree, it exits 0
  and its in-sync line names the directory it verified.
- **AC2** — When the Skill is rendered and `--check` is then run over a tree whose sibling
  directory is absent — the adopter's real state, where the render matches and only the
  filesystem disagrees — the output NAMES both missing paths. Superseded from "exits 1" to
  "names them" by `TOOL-aScouredKit-30`, whose §4 gives the reason.
- **AC3** — When the suggestion in that refusal is read, it derives from `KIT_REL` — this kit's own
  parent — rather than from `WORKFLOWS_REL`, the value being complained about, so it never reads
  "set it to X" when X is already what is set.

## 7. Gates

`drift-audit wiring` · `drift-audit selftest` · `kit version markers` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-08-30 · SUPERSEDED IN PART by `TOOL-aScouredKit-30`. This unit's ASSERTION half
  stands and is what fixed the finding; its DELIVERY half — an override that had to reach the
  gate leg — was refuted by three consecutive review rounds and withdrawn. S1, S2 and AC2 are
  restated above to describe what actually shipped, rather than left as a spec the code no longer
  matches. This edit exists because the closing review kept finding exactly that class.
- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate. AC2 observed
  before the spec was written: rendering with `DRIFT_WORKFLOWS_REL=tools/review-harness` and then
  checking with the same value reproduces the adopter state exactly — the diff arm agrees, and the
  new arm exits 1 naming `tools/review-harness/drift-audit-code.js` and its sibling. Against the
  pre-change script that same state exits 0 with "in sync".

## 10. Reuse audit

The seam is the script's own `render()` and its `--check` mode, both of which already exist; this
unit adds one override and one assertion inside them and writes no new file. The reference for the
failure class is `memory/gotchas/assertion-between-two-derived-values.md`, which names exactly the
shape `--check` had. The build's reuse probe is recorded in `TOOL-aScouredKit-1` §10.
