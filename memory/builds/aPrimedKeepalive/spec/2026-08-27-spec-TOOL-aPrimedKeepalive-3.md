# TOOL-aPrimedKeepalive-3 — the `discoveries-adopted` directive, so the rule is in the set a run reads at step 0

**Status:** INPROGRESS · rev-3 · 2026-08-27 · node a · Tier-2 · base b4e1d5be · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md](../prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md) | research | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aPrimedKeepalive-2` writes the adoption rule into the contract. A run reads the contract's
rules through the directive table at step 0, and a rule with no handle is not in that table — which
is exactly how the reported failure happened, in orientation, before anything else was read. Mint the
handle so the rule is in the set the run is told it is bound by, and so the owner can waive it by
name with a reason.

## 2. Scope (IN)

- **S1** — `DIRECTIVES_CORE` in `tools/unattended/unattended.sh` gains `discoveries-adopted:M10`,
  scope `all` by the absent-third-field default.
- **S2** — the Skill's directive table gains the matching row, whose handle cell is
  `` `discoveries-adopted` ``, whose carrier cell is `M10`, whose scope cell is `all`, and whose
  `From` cell is `D12` — the next value in the owner-instruction sequence the column records.
- **S3** — `DIRECTIVES_FLOOR` in `.unattended.conf` moves from `15` to `16`, the driver's own core
  member count, which is what check 16 arm C compares against.
- **S4** — the Skill render is regenerated in the same commit.
- **S5** — `tools/unattended/.unattended.conf.example` moves `DIRECTIVES_FLOOR` from `15` to `16` in
  the SAME commit. It is a FIFTH artifact carrying this value and the first draft of this scope
  dropped it, while `TOOL-aPromptedMandate-4` — the worked example §10 names — moved it when it took
  the floor 11 to 13. The example ships a FILLED value, so every adopter copying it verbatim would
  red their own kit gate on arm C.

## 3. Non-goals (OUT)

- Stating the rule in the table. The table's own header says each row NAMES a rule and points at the
  section that states it, and a cell that grew into a rule would be a defect in the table.
- A new `M<n>` section in the build method. The carrier is M10, which exists, and
  `TOOL-aPrimedKeepalive-2` is what makes M10 name the rule. Sequencing is why this unit is ordered
  after that one.
- Any change to the waiver machinery. `--waive` already accepts any effective-set handle and already
  refuses one it cannot resolve.
- A merge-bar CHECK asserting the example's floor equals the driver's core count. The arm exists at
  `tools/unattended/unattended.test.sh:1372`, in a suite the 2026-08-23 owner ruling took off the bar,
  so the invariant is real and unenforced at the push boundary. Moving it into `check-unattended.sh`,
  whose subject IS the repository, is the left-shift this unit's audit named and it is a unit of its
  own — recorded here so the gap is deliberate rather than unnoticed.
- A scope narrower than `all`. Adoption binds every unattended run, not only a prompt-authorized
  one: a slug-mode run orienting into a blocker has the same absent reader.

## 4. Design

### The three artifacts that must agree

Check 16 of `tools/unattended/check-unattended.sh` joins them in both directions, which is the whole
reason a handle can be added safely:

| Artifact | What it holds | Read by |
|---|---|---|
| `unattended.sh` `DIRECTIVES_CORE` | the registry, `<handle>:<section>[:<scope>]` | the driver's `--waive`, and the leg's `core_of` |
| `SKILL.template.md` directive table | the list an agent reads at step 0 | arm A, against the registry |
| `.unattended.conf` `DIRECTIVES_FLOOR` | the shrink-only core count | arm C |

Arm A compares the registry's `handle:M<n>` pairs against the table's rows, where a row's handle must
be its FIRST cell and its carrier is the one cell matching `^M[0-9]+$`. Arm B resolves each section
and asserts `^## M<n>` exists in `BUILD-METHOD.md`; M10 does. So the row, the registry entry and the
floor move together or the leg reds — which is the property being relied on rather than a hazard.

### Why a directive and not prose alone

A directive is how this kit makes a rule VISIBLE at step 0 and WAIVABLE by name. The reported failure
was a run that did not know adoption was available; a rule in the contract that never reaches the
table is a rule the run meets only if it reads the whole contract, which step 0 does not require.
Waivability is the cost and it is the right cost: an owner who wants a run to park everything can
say so once, with a reason, on the record.

### Files touched (estimate)

`tools/unattended/unattended.sh` — one constant. `tools/unattended/SKILL.template.md` — one table
row. `.unattended.conf` — one value. `.claude/skills/unattended/SKILL.md` — the render.

### Alternatives rejected

**Scope it `prompt`.** Research and a solution test are prompt-scoped because a build whose solution
was given has already chosen. Adoption has no such asymmetry — a slug-mode run finds blockers too.

**Ship it without the floor bump.** Arm C reds on a floor below the core count, so the bar would go
red immediately. Not an alternative, recorded because the three-artifact coupling is the kind a
reader discovers by breaking it.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a mismatch between the three artifacts is a named leg refusal,
  not a silent state.
- observability — a waiver of this handle lands in the run-state file's parked region and surfaces
  in the wrap-up, like every other waiver.
- risks — the directive is waivable, so an owner can turn the adoption rule off. That is the
  designed escape and it leaves a named record; it is not a hazard to mitigate.
- testing + left-shift gates — check 16's three arms are the left-shift and they already exist.
- migration / rollback — four one-line edits; revert is the rollback. **An adopter DOES inherit this
  floor**, and the first draft of this line denied it: `tools/unattended/.unattended.conf.example`
  ships a filled `DIRECTIVES_FLOOR`, unlike `CORE_FLOOR` two blocks above it whose comment reads
  "MEASURE, do not copy". S5 is what makes the denial true again.
- user docs — the Skill table is the user doc and it is in scope.

## 6. Acceptance criteria

- **AC1** — When `grep DIRECTIVES_CORE tools/unattended/unattended.sh` runs, the constant contains
  `discoveries-adopted:M10` and its member count is 16.
- **AC2** — When `.claude/skills/unattended/SKILL.md` is read, the directive table carries a
  `` `discoveries-adopted` `` row whose carrier cell is `M10` and whose scope cell is `all`.
- **AC3** — When `grep DIRECTIVES_FLOOR .unattended.conf` runs, the value is `16`.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, check 16 is green across all
  three arms, proving the registry, the table and the floor agree in both directions.
- **AC5** — amended rev-3. The staged break is NOT run: arm C's refusal is reachable only through
  `bash tools/unattended/check-unattended.sh`, ~25 minutes per invocation, and this run spent three of
  those. What IS observed is the same arm in the same green run with all five artifacts moved
  together. Recorded as a gap rather than claimed.
- **AC7** — When `grep DIRECTIVES_FLOOR tools/unattended/.unattended.conf.example` runs, the value is
  `16` and it equals the word count of the driver's `DIRECTIVES_CORE`.
- **AC6** — When `bash tools/unattended/unattended.sh --preflight` is offered `--waive
  discoveries-adopted --reason "<text>"` on a fixture, it is accepted rather than refused as an
  unknown handle — observed through the driver's own refusal path, not assumed from the registry.

## 7. Gates

`unattended kit gate` · `unattended skill wiring`, and `bash tools/run-gates/run-gates.sh` at the
push boundary. Compensating check, because the example-floor invariant's only arm is off the bar:
`bash tools/unattended/run-unattended-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft.
- rev-3 · 2026-08-27 · folded spec-audit round 1, findings 11 and 29 — both BLOCKERS and both live in
  the tree. Scope named four artifacts and the kit ships FIVE; §5 asserted no adopter inherits the
  floor, which the shipped example makes false. S5 and AC7 added, §5 rewritten, §3 records the
  unenforced invariant, §7 names the compensating check.
- rev-2 · 2026-08-27 · AC5's staged-break red-proof is recorded as a GAP rather than claimed. Arm
  C's refusal is reachable only through the full leg, which costs about fifteen minutes, and this
  run had already spent two of those. What the leg DID observe is the same arm in the same run with
  all three artifacts moved together; the deliberate break was not fired.

## 10. Reuse audit

The seam is the directive registry itself and it is extended, not replaced:
`tools/unattended/unattended.sh` `DIRECTIVES_CORE` at `:352` already carries fifteen entries in the
`<handle>:<section>[:<scope>]` grammar, and `check-unattended.sh` check 16 already joins it to the
Skill table and the floor in both directions. `TOOL-aPromptedMandate-4` added the two `prompt`-scoped
entries by exactly this route and is the worked example this unit follows.

The `From` column's meaning was traced to `memory/builds/cBriefedPilot/README.md`, where D1–D8 are
the owner's original numbered instructions and the handles are the waiver-grain decomposition of
them; `D12` continues that sequence for the instruction this build serves.

Recall terms used: `directive registry core floor waiver handle skill table carrier section scope
arm join drift`.
