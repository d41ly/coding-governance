# TOOL-dScriptedRepeat-10 — the two start paths and the playbook-scoped directives

**Status:** CLOSED · rev-5 · 2026-08-21 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md](../build/2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md) | journal | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md](../reviews/2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-11 |

<!-- /gen:spec-records -->

## 1. Goal

Author the agent-facing half: an unattended playbook start path, an attended one that shares the
artifact and the gate but not the driver, and the mode-scoped directives that bind a playbook run to
the parts of the build method it must actually perform.

## 2. Scope (IN)

- **S0.** The Skill gains a routing preamble naming FOUR paths, not three: slug, prompt, playbook-run
  (S1) and playbook-CREATION, which is unit 11's and is a `prompt`-mode run rather than a `recipe`-mode
  one. A reader arriving with no playbook must be sent to the path that makes one, because unit 4's
  preflight refuses a `playbook:` that does not resolve at BASE — so a no-playbook start cannot reach
  preflight at all.
- **S1.** The UNATTENDED playbook-RUN start path in `tools/unattended/SKILL.template.md`, alongside the
  slug and prompt paths: orient, ask ONCE if under-determined, write the build folder carrying the owner's
  prose plus `playbook:` and `pieces:`, commit, push, preflight, kickoff hand-back. Ordered, and the
  order is the point — everything before the push is provably older than the commit that authorizes
  the run.
- **S2.** The ATTENDED path, which writes NO run-state file, calls no driver verb, and produces the
  same tracked per-piece and set records unit 5 and unit 7 define. It is documented in the Skill as a
  path that the merge bar sees and the driver does not, and it says that plainly.
- **S3.** The MODE-SCOPED DIRECTIVES: `playbook-followed` and `pieces-recorded`, each a POINTER into a
  build-method section, scoped to `recipe` mode, appended to `DIRECTIVES_CORE` with
  `DIRECTIVES_FLOOR` rising in the same commit in this repo's INSTALLED conf as well as the example.
- **S4.** The build-method carrier for those pointers. `memory/guides/BUILD-METHOD.md` is at its stated
  budget, so this unit does NOT add a section to it. §4 gives the alternative and §8 F1 carries the
  fork if the owner prefers the budget rise.
- **S5.** The REFUSAL of ordinary code builds, agent-facing: the Skill states that this mode is for
  producing declared content and that a code build uses the slug or prompt path. It is written as a
  CHECK, and the PAIRING is stated per path rather than in general: on the UNATTENDED path it is paired
  with unit 8's machine refusal; on the ATTENDED path there is no machine half at all, because unit 8's
  two inputs — the recorded mode and the run's commit set — both exist only through the driver. The
  previous revision claimed the pairing without that qualifier, which is true of one entry point and
  false of the other.
- **S6.** The Skill/registry JOIN, in both directions, for the directive table and — new this unit —
  for `AUTH_MODES`, closing unit 1's F2.
- **S7.** Rendered-artifact arms: the render carries no surviving brace-shape, and the byte-compare
  against the shipped template passes. Placeholder completeness and template parity are two different
  questions and this repo has a recorded failure conflating them.

## 3. Non-goals (OUT)

- No new build-method SECTION. S4.
- The attended path gets no verb, no phase and no DoD. That is what "not the driver" means, and
  pretending otherwise would put a run-state file in a tree with nobody to close it.
- No change to the prompt or slug paths.

## 4. Design

### Why the directives do not get a new method section

The two prompt-scoped directives point at a method section that was ADDED for them, and its budget rose
by owner ratification to make room. That budget is nearly spent again. Rather than ask for a second
rise, these two directives point at sections that ALREADY state the obligation: following a declared
procedure to the letter is the pass loop and its regrounding rule, and recording what was produced is
the wrap-up derivation. A directive is a POINTER, and a pointer at an existing section is the design
working; adding a section per directive is how the method grows until nobody re-reads it, which is the
exact failure its own budget exists to prevent.

If the owner would rather have an explicit section, §8 F1 is the fork and it costs a ratified budget
rise.

### The attended path's honest limit

It leaves no run-state file, so every run-state-keyed check in the kit gate sees nothing. What it DOES
leave is unit 5's per-piece records and unit 7's set record, both tracked and both hash-joined, and
those are what the playbook leg reads. So the sentence the Skill must carry is precise: the attended
path is gated on WHAT IT PRODUCED and not on how it ran, and the unattended path is gated on both.
Fork 1's "ONE gate" is true of the artifact gate and was never true of the driver.

### The one owner turn

Reused from the prompt path, including its strongest property: the turn sits BEFORE the push, so the
owner's answers are provably older than the commit that authorizes the run. A run cannot have taken an
answer later than the commit it is authorized by. For `recipe` mode the under-determined fields are
narrower than the prompt path's — usually just `pieces:` and the output location — because the playbook
itself answers most of what would otherwise be asked.

### Alternatives rejected

**A separate `/playbook` Skill.** Rejected: two Skills naming one artifact and one gate is two answers
to one question, and the unattended Skill already carries the start-path pattern twice.

**Making the attended path write a run-state file it never closes.** Rejected: a non-terminal run-state
file in the tree breaks the protocol's at-most-one-live-run rule and every later run is measured
against a counter that includes it.

## 5. Production-readiness checklist

- security — the Skill is prose an agent reads. It cannot enforce S5; unit 8 does. Saying so in the
  Skill is the requirement.
- perf / scale — N/A.
- a11y — N/A. i18n — the rendered Skill is ASCII.
- error / empty / loading states — the Skill must state what happens when the anchor scope forbids the
  path, the way the prompt path already does: say so and stop, rather than writing a build folder
  nothing can authorize.
- observability — the directive table and the mode list are joined to their registries in both
  directions, so a handle in one and not the other is a refusal rather than a discrepancy nobody sees.
- risks — the rendered Skill is where a placeholder can survive as literal prose and pass every check,
  because the detector greps the brace shape only. S7's separate arm is the control and the kit already
  carries a `[[hole]]` for exactly this class.
- testing + left-shift gates — S6 and S7; the join arms fail in both directions.
- migration / rollback — additive; the two existing paths are untouched.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — When the rendered `.claude/skills/unattended/SKILL.md` is grepped for a brace-shape, there
  are zero hits, AND separately for an angle-bracket placeholder left as literal prose. Two arms.
- **AC2** — When a directive handle is in `DIRECTIVES_CORE` and absent from the Skill table,
  `bash tools/unattended/check-unattended.sh` REDS; and when the reverse holds, it also REDS. Both
  directions observed.
- **AC3** — When a mode is in `AUTH_MODES` and absent from the Skill's mode list, the leg REDS,
  closing unit 1 F2.
- **AC4** — When `DIRECTIVES_CORE` grows by two, `DIRECTIVES_FLOOR` rises in the same commit in BOTH
  `.unattended.conf` and `.unattended.conf.example`, and an arm reads the INSTALLED file — the research
  found the installed conf graded by nothing.
- **AC5** — When a `playbook`-scoped directive is waived on a run of another mode, the driver refuses,
  exercising unit 1 S4 end to end.
- **AC6** — When the attended path is followed in a scratch tree, `bash tools/unattended/check-playbook.sh`
  reads the per-piece and set records and reports on them with NO run-state file present. Observed.
- **AC7** — When `tools/unattended/SKILL.template.md` is read, S5's refusal is labelled a CHECK and names unit 8's gate as the
  machine half, so a reader cannot mistake the prose for the enforcement.

## 7. Gates

`bash tools/unattended/adopt-unattended.sh --check` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — a new build-method section for the playbook directives?** RESOLVED (owner, 2026-08-20): NO —
  the two directives POINT at existing sections. `memory/guides/BUILD-METHOD.md` does not move and its
  stated budget does not rise, so the mode adds nothing to a document M7 re-reads whole at every pass
  boundary. The accepted cost is that "follow a playbook to the letter" is described by the pass loop
  and the wrap-up derivation rather than by prose written for it.
- **F2 — does the attended path need its own entry in the kickoff engine's exit list?** RESOLVED
  (agent, 2026-08-20, delegated): NO. That list enumerates the interactive exits an UNATTENDED run
  resolves without an owner turn, and an attended path has an owner by definition. The Skill states
  that reason, so the absence reads as a decision rather than an oversight.

## 9. Revision log

- rev-5 · 2026-08-21 · BUILT. The routing preamble, the playbook-run path, the attended path, the two
  `recipe`-scoped directives, and two new leg checks.

  **S5 and AC7 came out weaker than specced and the Skill says so in those words.** Both were written
  around unit 8's refusal supplying the machine half on the unattended path. Unit 8 is withdrawn, so
  the content-scope rule now has NO machine half on EITHER entry point, and the path text states that
  rather than implying a gate. Check 25 exists precisely because prose is the whole enforcement here:
  it greps the section for the qualifier and for the sentence naming what the mode is not for, in the
  literal-string manner check 12 uses on the kickoff engine, because a heading survives a gutted body.

  **S0 grew a fifth entry that is deliberately not in the table.** The attended path is not a run and
  cannot be started like one, so listing it beside four `authorized-by:` values would have taught a
  reader to look for a mode it does not have. It is named under the table and documented after the
  unattended paths it shares its records with.

  **AC4 needed no new arm and that is worth recording**, so nobody adds a third. Two arms already
  join the floors to the driver's own counts — the example conf's `DIRECTIVES_FLOOR` in the driver
  self-test, the installed conf's slack arm in the leg — and growing `DIRECTIVES_CORE` by two forces
  both floors to 15 or reds. The pre-existing machinery is the acceptance criterion's enforcement.

  **F1 held under contact.** Neither directive states its rule: `playbook-followed` points at M7's
  pass loop and regrounding, `pieces-recorded` at M9's wrap-up derivation. The build method does not
  move and its budget does not rise.
- rev-4 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-1 · 2026-08-20 · initial draft. S2's shape follows from the research proving an attended run
  cannot close through the driver; S4's refusal to add a method section follows from the measured budget
  and from M1's own rule about re-reading cost.
- rev-3 · 2026-08-20 · owner ruled F1: the directives point at existing build-method sections, so the
  method's budget does not move and this build adds no re-read cost to a document M7 re-reads whole at
  every pass boundary.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F17 added S0's routing preamble and the fourth path,
  after the audit found that the owner's FIRST stated verb — create a playbook when none exists — had no
  owning unit anywhere in the roster and was structurally refused by unit 4's own preflight. The path
  itself is unit 11. F10 qualified S5's pairing claim per entry point.

### What was built, against what was specced

- S1's path is the third instance of the ordered start-path shape, exactly as the reuse audit
  predicted, and the audit's own note stands: a FOURTH should extract the shared shape rather than
  copy again. Not done here, and named for a successor rather than left implicit.
- S6 landed as check 24, joining `AUTH_MODES` to the routing table in both directions with two
  vacuity arms ahead of the comparison — the extraction takes the LAST backticked lowercase cell per
  row, so the prose columns are free to change and the mode column is not.
- AC5's arm is a second scope value with its own test, plus the accepting direction on a
  `recipe`-authorized run. This file's own history is the reason: an arm naming one scoped member
  twice left a later member unenforced and green.
- AC1 became two SHAPE arms rather than two more named placeholders. A list cannot notice a
  placeholder nobody added it to, and the render is where an unfilled one survives as literal prose.

## 10. Reuse audit

The prompt start path is the seam and this unit is its third instance rather than a new pattern: the
same ordered steps, the same single `AskUserQuestion`, the same turn-before-the-push property, the same
anchor-scope precondition check with its say-so-and-stop rule. Reaching instance three is what fork 12
of the charter would call a factory moment, and the honest reading is that the Skill's three start paths
now share enough structure that a fourth should extract a common shape rather than copy again — noted
for a successor, not built here. The DIRECTIVE-AS-POINTER discipline is reused exactly, including its
rule that a gloss must not grow into a condition. The BOTH-DIRECTIONS JOIN between a driver registry and
the Skill table already exists for directives and is extended to modes rather than reimplemented. Recall
terms used: skill template start path render placeholder brace parity directive pointer registry join
both directions scope waiver mode attended run state absent build method budget.
