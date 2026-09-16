# DEPL-cMendedVintage-7 — `GOVKIT_RERENDER` defaults ON, and `=0` becomes the revert

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

The re-render stage in `_cmd_update` reads `os.environ.get("GOVKIT_RERENDER") == "1"`, so it is off
for every operator who has not heard of the variable. That was the correct first release — the
charter's dark-landing rule applied to the deployer — and it is why `update --write` still moves
bytes without performing the install effects those bytes need. Flip the default on, keep `=0` as a
readable revert that needs no code change, and pin the two self-test arms whose SUBJECT is the off
path so the flip does not turn them red.

## 2. Scope (IN)

- **S1** The read in `tools/govkit/govkit.py` becomes a default-on test whose off value is the
  literal `0`, so an operator reverts with `GOVKIT_RERENDER=0` and nothing else. The variable keeps
  its name and its one reader. Observed by AC1.
- **S2** Every site in `tools/govkit/selftest.py` that removes `GOVKIT_RERENDER` from a child's
  environment is decided explicitly in this unit: an arm whose subject is the OFF path pins the value
  `0`, and an arm that strips the variable to keep a node's exported environment out of its result
  keeps the strip and says in one line that it now runs with the step ON. Observed by AC2.
- **S3** Every tracked non-record carrier whose sentence states the OLD default is corrected. The
  population is derived at build time from `git grep -l GOVKIT_RERENDER` over `tools/` and the
  repo-root runbook; records under `memory/` are frozen history and are not touched. Observed by AC3.
- **S4** The charter's dark-landing obligation is discharged in the form this repo can discharge it:
  in-place verification against a fixture before the commit lands. The second half of that rule, one
  adopter, cannot be run here and is declared rather than claimed. Observed by AC1 and section 8.

## 3. Non-goals (OUT)

- No change to the re-render stage's structure: the decline list, the inert skip, the outcome
  classification and the printing are all untouched. This unit moves one default.
- No new flag, and no `deploy.toml` key. A target-declared re-render switch would put the decision in
  the file this engine already refuses to take argv from.
- No change to which kits declare `[[regenerate]]`. That population is `DEPL-cMendedVintage-5` and
  `TOOL-cMendedVintage-1`, and this unit is what makes their declarations execute.
- The `memory/` records that describe the old default stay exactly as written. A landed record is a
  statement about its own date.

### Edges

- **consumes-from** `DEPL-cMendedVintage-6` — the flip must not land first. With the step on by
  default the regenerate runs on every update, so the fixture-record clobber that unit closes would
  otherwise be armed at every adopter, which is the fork rule's third veto in one sentence.
- **consumes-from** `DEPL-cMendedVintage-5` — three of the kits whose artifacts this flip refreshes
  have no regenerate to run until that unit lands.
- **consumes-from** `TOOL-cMendedVintage-1` — the fourth.
- **hands-off** external — the adopter half of the dark-landing rule. The first adopter to take this
  release is the in-place verification this repo cannot perform, and the runbook step is theirs.

## 4. Design

### Data model

One expression. `_rerender_on` is the only reader of the variable in the engine, and everything
downstream — the decline list, the `ran` lines, the outcome classification — already branches on that
one boolean. An off value spelled `0` keeps the revert greppable and keeps the variable's existing
name meaningful in both directions.

### Inventory

Nothing is minted. The variable, the boolean and the printing all exist at BASE.

### Migration

An operator's next `update --write` runs target-side code where the previous one did not. What runs
is each claimed kit's declared regenerate argv, which comes out of a gov-authored descriptor and
never out of the target's `deploy.toml`. So the TRUST boundary is unchanged — the argv is still
gov's — and that is a different sentence from the blast radius, which grows: a verb that wrote only
bytes now also executes a program per touched kit, in the operator's tree, under their uid. The
revert is one environment variable and needs no release.

### Rollout

Land the flip in the same commit as the self-test pins of S2. Splitting them leaves the suite red in
between, and a red suite between two commits of one unit is indistinguishable from a broken flip.

### Alternatives rejected

- **A `deploy.toml` key instead of an environment default.** It moves the decision into the target's
  own descriptor, which is the file this engine refuses to take argv from for reasons recorded at
  `target_context`. A posture the target genuinely owns is `deploy["inert"]`, which already exists.
- **Leaving the default off and documenting the flag harder.** Measured consequence at BASE: the
  declines are printed only when the flag is set, so an operator who has not set it sees no line at
  all, and the artifacts go stale in silence. That is the skip-that-looks-like-a-pass class.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | one expression, and the comment above it that explains the dark landing |
| `tools/govkit/selftest.py` | the env-handling of the arms S2 enumerates |
| `tools/unattended/kit.toml` | the sentences naming the old default |
| `tools/workflows/kit.toml` | ditto |
| `tools/workflows/README.md` | ditto |
| `WIRE-INTO-PROJECT.md` | ditto |

## 5. Production-readiness checklist

- security — the argv is gov's, from a gov-authored descriptor, and every value interpolated into it
  is graded by `demand_safe_token` at the boundary. What changes is that the execution now happens by
  default, so the guard that matters is the one refusing target-supplied argv, and it is unchanged.
- perf / scale — one subprocess per touched kit per `update --write`, where there were none.
- error / empty / loading states — a regenerate that exits non-zero and matches no declared outcome
  still fails the run and names the kit. That path is untouched and is now reachable by default.
- observability — the flip makes the `re-render` summary and every `DECLINED` line print on an
  ordinary run, which is the half of this the previous release could not have.
- risks — the sharp one is that a defect in any kit's regenerate now reaches every operator instead
  of the one who opted in. The mitigations are the sequencing edges in section 3 and the one-variable
  revert.
- testing — AC1 observes both directions on a fixture; AC2 and AC3 are greps over the tree.
- migration — none on disk. Reverting the default is a one-line change and reverting a single run is
  an environment variable.
- user docs — `WIRE-INTO-PROJECT.md` and the kit READMEs are the carriers S3 corrects.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py update --target <dir> --write` runs against a scratch
  target with the variable UNSET, the run prints its re-render summary and a `ran` line for each
  claimed kit declaring a regenerate; when the same command runs with `GOVKIT_RERENDER=0` exported,
  it prints no `ran` line and the target's rendered artifacts are unchanged.
  Red when: the new expression treats an unset variable as off, or treats `0` as on, either of which
  leaves one of the two runs indistinguishable from the other.
  fixture: a scratch install under the run's scratch root; this repo keeps no receipt of its own.
- **AC2** — When `git grep -n "GOVKIT_RERENDER" -- tools/govkit/` is read, every site that removes
  the variable from a child environment either sets it to `0` or carries a line saying the arm now
  runs with the step on, and no site is left silently inheriting the new default.
  Red when: an arm whose assertions describe the off path is left env-stripped, which turns a correct
  flip into a red suite at the close.
  figure: DERIVED — the site list comes from that grep, not from a count written here.
- **AC3** — When `git grep -ln "GOVKIT_RERENDER" -- tools/ WIRE-INTO-PROJECT.md` is read, every file
  it names describes the step as running by default and names `0` as the way off.
  Red when: a carrier still tells a reader the step is declined unless the variable is set, which is
  the stale-prose-beside-the-source class this repo keeps a rule about.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0.
  Red when: a sentence edited by S3 says a flag-off update is silent without naming the
  `re-rendered` row it still prints, which arm 7l refuses.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `install-prefix (shipped surface)` · `unattended kit gate` · `playbook validity gate`

New arm: `tools/govkit/selftest.py` · no arm is added; two existing arms are MOVED, from stripping
the variable to pinning its off value, and the failing case for the move is the flip itself run
against those arms' own fixtures · no assertion floor to move.

## 8. Open questions

- **Q1 — the charter's dark-landing rule asks for verification against a fixture AND then one
  adopter, and this repo has no adopter install.** RESOLVED (owner, 2026-09-16): all six phases of
  the fix plan are in scope for this build, which is the build README's first build-level rule. The
  fixture half is AC1 and is discharged here. The adopter half is declared as an external edge: the
  first consumer to pull this release performs it, and this unit does not claim it.
- **Q2 — should the off value admit `false` and `off` as well as `0`?** RESOLVED (agent, 2026-09-16,
  delegated): no. One spelling is greppable, and a second one is a second place the meaning is
  written. The engine's other environment reads are exact-match too.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

No existing seam fits, and the evidence is that there is nothing to reuse: the change is one
expression at the single reader of one variable, `_rerender_on` in `tools/govkit/govkit.py`, and the
codebase-map probe over "re-render a kit's rendered artifacts during an update" returned no seam and
named `.sh` as an unscanned layer. What the recall probe returned instead is the RULE this unit is
bound by, which is worth more here than a seam: the re-render step shipped gated off by the charter's
dark-landing rule and is to be flipped on only after in-place verification against a fixture and then
one adopter, recorded in
`memory/builds/dRetiredFork/prompts/2026-09-03-prompt-DEPL-dRetiredFork-3-1-build-brief.md`. Section
8 is where this unit answers it.

Recall terms used: `--terms "dark flag default landing verification fixture adopter blast radius
trust boundary selftest arm environment revert govkit"`, with the question "what does a dark
default-off flag owe before it is promoted to default on in this repo".
