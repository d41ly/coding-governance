# TOOL-dDeclaredLoop-53 — an owner gate holds only builds opened after the gate was placed

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 34 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-53-deviation-531.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-53-deviation-531.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 54 at HIGH**, its item **H19**, alone in that item. Under the default `autonomy =
plan-only`, `TOOL-dDeclaredLoop-19` S3 places an owner gate at `item.plan.exit` for every build, and S6
has `--phase` refuse any move past a gated step exit, and `--close` refuse, until a disposition record
names the gate. Every phase from RESEARCHING to LANDING lies past `step.plan`, and its §4 Migration says
"None … the plan's ratification already is" the gate, though nothing makes an existing ratification
satisfy `check_owner_disposition`. After landing, every in-flight unattended run's next `--phase` and
`--close` is refused until the owner commits a disposition for a gate it never had; this build lands
`TOOL-dDeclaredLoop-19` at order 33 of its roster, so its own close is held. This unit takes the report's
second option. It repairs `TOOL-dDeclaredLoop-19`.

## 2. Scope (IN)

- **S1** — The placement revision: the oldest commit on `HEAD`'s history that adds
  `tools/loop/breakpoints.py`, read with `git log --diff-filter=A --format=%H -- <path>` through the
  loop kit's own path, resolved by `resolve_kit_dir("loop", "breakpoints.py", here)` so an adopter's
  install commit is its placement revision. Observed by AC1.
- **S2** — A build is opened after the placement when the commit that added its `README.md` descends from
  the placement revision (`git merge-base --is-ancestor <placement> <readme-add>`). For a build that is
  not, every owner gate `derive_breakpoints` lists prints as `breakpoint: owner gate · <position> ·
  passed before placement` and is never held by `--phase` or `--close`. Review breakpoints are unaffected.
  This supersedes `TOOL-dDeclaredLoop-19` §4 Migration's "None". Observed by AC1, AC2.
- **S3** — A build opened after the placement is held exactly as `TOOL-dDeclaredLoop-19` S6 says.
  Observed by AC3.

## 3. Non-goals (OUT)

- Reading whether an in-flight build already passed a gate's position from its phase history: the
  run-state file keeps only the current `phase:`, so the history is not on disk to read.
- A template rule that a unit adding a refusal to a run verb states its in-flight migration, the
  finding's left-shift: a governance carrier no clause of this build names; AC1 is this refusal's
  pre-existing-run fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-19` — `derive_breakpoints` in `tools/loop/breakpoints.py` and the `--phase` and `--close` holds, which this unit scopes to builds opened after the placement
- **hands-off** `TOOL-dDeclaredLoop-64` — the README path of the opening-commit rule, which that unit resolves through the memory root (the round-2 spec audit's id 57)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 8, 28 and 45: the oldest-add ordering and this arm's home in the breakpoints fixture are scope items of that unit

## 4. Design

### Evidence

- The defaults `TOOL-dDeclaredLoop-19` S1 reads: `autonomy` `plan-only` places the owner gate at
  `item.plan.exit` (S3); `--phase` and `--close` hold on it (S6).
- The run-state file carries one `phase:` fact and no phase history (`memory/builds/dDeclaredLoop/RUN.md`,
  its `## Run facts`, read 2026-10-24), which is why S2 keys the rule to the build's opening commit.

### The rule

```
placement = oldest commit adding <loop kit>/breakpoints.py on HEAD's history
opened    = commit adding memory/builds/<slug>/README.md
held      = owner gate placed  and  merge-base --is-ancestor placement opened
otherwise print "passed before placement", hold nothing
```

### Files touched (estimate)

- `tools/loop/breakpoints.py`
- `tools/unattended/unattended.sh`

### Alternatives rejected

- **A gate passed before placement, by phase history.** The history is not recorded, so the rule would
  read the current phase and hold any build whose phase moved since.
- **A dated cutoff key.** A new conf key, a public surface the build's grant does not name; the opening
  commit is already in history.

## 5. Production-readiness checklist

- security — a narrowing of where a new refusal applies, to builds that existed before it; review
  breakpoints and every newer build keep it whole.
- perf / scale — two `git log` reads per `derive_breakpoints` call, cached per process.
- error / empty / loading states — a build whose README has no adding commit on `HEAD` is treated as
  opened after the placement and held, never silently exempt.
- observability — each exempt gate prints its own `passed before placement` line on `--plan`.
- risks — a build opened on a branch that forked before the placement and merged after reads as
  pre-placement, the conservative side for an in-flight run.
- testing — AC1 to AC3 as fixture probes; the arm under §7, observed at the close.
- migration — S2.
- user docs — the unattended protocol's breakpoint text, `TOOL-dDeclaredLoop-19` S10's, names the rule.

## 6. Acceptance criteria

- **AC1** — When a fixture repository opens a build, then adds the loop kit's `breakpoints.py`, and a run of
  that build in `REVIEWING` with no disposition record runs `unattended.sh --phase BUILDING`, the move is
  admitted and `--plan` prints `passed before placement` for the plan gate.
  Red when: the pre-existing build is held at its plan gate, as the finding records.
  fixture: a fixture repository under a short `%TEMP%` path; the unattended kit's suites are waived for
  this landing (README rule 8), so this is a probe.
- **AC2** — When `python breakpoints.py --fixture --plant pre-placement` runs, the owner gate
  is listed with `passed before placement` and the review breakpoints with their causes.
  Red when: the exemption reaches a review breakpoint.
- **AC3** — When the fixture opens a second build after the placement and runs the same
  `unattended.sh --phase BUILDING` move, it is refused naming the plan gate.
  Red when: the exemption holds for every build, so no owner gate ever holds.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC2 · the `pre-placement` plant beside a post-placement build, staged against `TOOL-dDeclaredLoop-19`'s rule, which holds both · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which in-flight rule?** Options: (a) a gate whose position the build passed before placement,
  from its phase history; (b) gates placed only for builds opened after the placement revision. (a) reads
  a history no file records. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3. It relaxes nothing
  against base, where no owner gate exists. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 54 (HIGH, item H19).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-64 and TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are git's ancestry query and `TOOL-dDeclaredLoop-19`'s `derive_breakpoints`; the placement
revision is read from history, never typed. `python tools/codebase-map/reuse_lookup.py "an owner gate
placed for builds opened after the placement"` ranked `build`, `opened` (a recall test helper),
`build_commit` and `build_fixture`, none of which scopes a refusal by a build's opening commit.

Recall terms used: owner gate autonomy plan-only in-flight placement revision opened README ancestor phase close
