# TOOL-dIndexedDesign-3 — design review by policy: `review.design` read at the guarded revision, its effort, and the opt-in guard

**Status:** DEFERRED · rev-4 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 16 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0385@7bdb7329 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-16 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 |

<!-- /gen:spec-records -->

## 1. Goal

The Design stage's review, the pre-code spec audit, is decided by policy end to end: whether it runs is
`review.design`, read only where the owner alone can write it, and the effort its lenses run at is
`review.design.effort`. The stage-exit recommendation stays dDeclaredLoop's (AF-1). Today the opt-in is a
README date or a conf default (`tools/unattended/unattended.sh:3975`, `:4022-4035`), its owner-only
guard is fail 89 (`:4113`, `:4125`), and the audit's effort is the roles kit's house file alone
(`tools/roles/roles_lib.py:596-601`), so 3 of 173 builds declared an audit (`gap-design-03`).

## 2. Scope (IN)

TOOL-dDeclaredLoop-19 S8 already specs the opt-in derivation over `review.design`: its value table, the
`policy` source of `AUTH_SPEC_AUDIT_FROM`, the preflight line and BUILD-METHOD M4's "When". This unit
consumes that derivation (§8 F1) and owns what the clause adds to it: the revision the read takes, the
split of its refusal, the guard's remedy text, and the effort.

- **S1** — The guarded revision. The `review.design` read TOOL-dDeclaredLoop-19 S8 adds to
  `check_authorization` (`tools/unattended/unattended.sh:3927`) takes `--rev "$AUTH_CONF_AT"`, the
  default-branch side of the pinned BASE where `SPEC_AUDIT_DEFAULT` is read (`:4016-4021`), spelled
  literally as `"$PY" "$_pk/policy.py" get review.design --rev "$AUTH_CONF_AT"` and run in the
  repository root, since `get` reads `.` (`tools/policy/policy.py:1348`). It never reads HEAD, the
  working copy or the landed revision. A blank `AUTH_CONF_AT` runs no read and takes the `opt-in` arm,
  announced, by the guard `SPEC_AUDIT_DEFAULT`'s read already uses (`:4022-4023`). The opt-in this read
  derives is the build's spec-audit declaration that `design.coverage.semantic`'s `with-spec-audit`
  value reads (TOOL-dIndexedDesign-16 S9), so the re-pointed opt-in and that test read one fact.
  Observed by AC1, AC2.
- **S2** — Unknown is not absent. When that `get` exits non-zero, the driver runs
  `policy.py check --rev "$AUTH_CONF_AT"`: exit 0 means the refusal was the default step's, which for
  `review.<stage>` is the derived default of an unset key, and the derivation takes its `opt-in` arm;
  a non-zero exit is a refusal with a new driver fail code naming `review.design` and the line `check`
  printed. The read and its refusal sit before `AUTH_SPEC_AUDIT_DERIVED=1` (`:4041`), so a refusal
  leaves the `specs-audited` grader NOT GRADABLE, as fail 52, 54 and 55 do. Observed by AC3.
- **S3** — The guard's remedy. Both fail 89 messages (`:4113`, `:4125`) name the policy file's key as
  the owner's third route: "or `review.design` in `.governance/policy.toml` there", beside the
  README key and `SPEC_AUDIT_DEFAULT`. The README key keeps its refusal under every `review.design`
  value, since a run that writes an opt-in key has made the attempt whether or not the key is read
  (TOOL-aWardedAudit-1, "refused rather than ignored"). Observed by AC4.
- **S4** — The design review's effort. In TOOL-dBoundRoles-21's effort order, re-pointed into
  `resolve_stage_efforts` in `tools/roles/roles_lib.py`, a step 1a between `roles.effort.<w>.<s>` and
  `roles.effort.<r>` reads `read_policy_setting("review.design.effort", root)` for the stage keys of
  the `spec-review` workflow, in the two workflows `DESIGN_REVIEW_WORKFLOWS` names, `spec-review` and
  `spec-write`. A value outside `EFFORT_LEVELS` (`tools/roles/roles_lib.py:45`) is a `RolesError` naming
  `review.design.effort` and the levels. No value leaves the order as TOOL-dBoundRoles-21 reads it,
  which is the catalogue's derived default, "the role's declared effort" (`tools/policy/catalogue.toml:1212-1215`).
  `handoff.py stage-efforts` prints the result, and the build harness forwards the three review
  levels to the audit's review call unchanged (`tools/workflows/unattended-build.template.js:535-537`,
  `:1661`). Observed by AC5, AC6.
- **S5** — The literal readers. Both reads spell their key first as a literal, the shapes the policy
  kit's reader-coverage arm counts (`tools/policy/check_policy.py:423-435`), and the driver's read
  relies on `"policy"` in `tools/unattended/kit.toml`'s `requires`, which the first unit whose driver
  code reads a policy key adds. Observed by AC7.
- **S6** — The carriers. `tools/roles/README.md`'s effort section, `tools/unattended/VERBS.template.md`
  with its render `memory/guides/UNATTENDED-VERBS.md` at the `efforts` bullet (`:734`), and
  `help/policy.md`'s consumer paragraph state the step 1a level and the revision `review.design` is
  read at. Observed by AC8.
- **S7** — The suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC3, AC4, AC5 and AC6
  through those lines, RED first at the close.

**Build-run precondition.** TOOL-dDeclaredLoop-19 (its S8 read) and TOOL-dBoundRoles-21 (its S1
`read_policy_setting` and S2 order) are DEFERRED at `57bc3b91`. The build run re-grounds on both at its
base and builds this unit only once both are CLOSED; until then the README key and `SPEC_AUDIT_DEFAULT`
decide the audit as today, and the audit's lenses run at the house levels (§8 F8).

## 3. Non-goals (OUT)

- The opt-in derivation: TOOL-dDeclaredLoop-19 S8's table of `off`, `opt-in`, `owed` and
  `owed-above-tier`, its `policy` source, `print_spec_audit_line`'s line, the pinned BASE date for
  `owed` and M4's "When". This unit moves the revision of that read and splits its refusal.
- `derive_breakpoints`' read of `review.<stage>` for `--plan` (TOOL-dDeclaredLoop-19 S1): it lists
  breakpoints and opts nothing in; §8 F2's ask names its revision.
- The stage-exit recommendation: TOOL-dDeclaredLoop-22's `--recommend <slug> --stage design`, its record
  and the harness's `reason` stage, consumed as built (§8 F6).
- Effort for the Plan, Build, Test, Deploy and Maintain reviews: dCalibratedLens's `cl-dClosedLoop-0458`.
  Step 1a reads the design key alone.
- `review.design.rounds` and `review.design.round-count`: dDeclaredLoop's keys, read by its review program.
- Catalogue rows: `review.<stage>` and `review.<stage>.effort` belong to dDeclaredLoop and dCalibratedLens,
  so this unit writes no `summary` and touches `tools/policy/unsummarised-keys.txt` not at all.
- The README `spec-audit:` key and `SPEC_AUDIT_DEFAULT`: kept as TOOL-dDeclaredLoop-19 §8 F2 ruled, with
  every reader unchanged.
- The policy guard itself: `tools/policy/guard.py` and `tools/policy/guarded-paths.txt` are read, not edited.
- The build harness: no `.template.js` changes, since the review levels already pass through.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — `read_design_policy`: I3, the shared policy reader, whose
  shell form, the literal `policy.py get <key>` call key first, is the spelling S1's driver read takes;
  without it the read is a variable key the reader-coverage arm cannot count; and its S9
  `with-spec-audit` test, which reads the audit declaration S1 re-points
- **consumes-from** external — TOOL-dDeclaredLoop-19 S8, the `review.design` read in `check_authorization`
  and its `opt-in` arm, which S1 and S2 move and split; without it nothing reads the key
- **consumes-from** external — TOOL-dBoundRoles-21 S1 and S2, `read_policy_setting` and the effort
  order step 1a sits in; without them the roles kit has no policy read
- **consumes-from** external — TOOL-dDeclaredLoop-22, `item.design.recommend`, the recommendation the
  owner reads before opting in, never called here
- **consumes-from** external — dGroundRules' landed `policy.py get` and `check`, and the policy guard
  over `.governance/policy.toml`
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 3, 15 and 24, each a scope item of that batch unit
- **hands-off** `TOOL-dIndexedDesign-41` — its unreadable `review.design` refusal, which that unit's S3 joins to an existing `check_authorization` site in this unit's pass commit (id 3)
- **hands-off** `TOOL-dIndexedDesign-53` — its unreadable `review.design` refusal, which that unit's S11 composes into the `fail 55` site of `check_authorization` in this unit's pass commit, naming `its review.design value` as its cause (id 18)

## 4. Design

### The read and its refusal

```
# check_authorization, at the review.design read TOOL-dDeclaredLoop-19 S8 adds, before AUTH_SPEC_AUDIT_DERIVED=1
rd=opt-in
if [ -n "$AUTH_CONF_AT" ]; then
  if   rd=$("$PY" "$_pk/policy.py" get review.design --rev "$AUTH_CONF_AT" 2>"$err"); then :
  elif "$PY" "$_pk/policy.py" check --rev "$AUTH_CONF_AT" >"$chk" 2>&1;               then rd=opt-in
  else fail <new> "...review.design at <AUTH_CONF_AT> is unknown and is not read as absent: <check's line>"
       return 1
  fi
else
  echo "unattended: spec-audit — review.design unread: no default-branch side of BASE was observed"
fi
# rd then selects TOOL-dDeclaredLoop-19 S8's arm, unchanged
```

| Policy file at `AUTH_CONF_AT` | `get` | `check` | Reads as |
|---|---|---|---|
| valid, sets the key | 0, the value | not run | the value |
| valid and unset, or absent | 2, the derived default | 0 | `opt-in` |
| invalid, the last valid revision read | 0, or 2 on its derived default | 0 | that value, or `opt-in` |
| invalid with no valid revision, or `on-invalid` not `last-valid` | 2 | 2 | refused, the new fail code |
| `AUTH_CONF_AT` blank | not run | not run | `opt-in`, announced |

`check` passes exactly when `get`'s refusal came from the default step: `check_revision`
(`tools/policy/policy.py:665-676`) refuses on the same last-valid conditions `read_last_valid_value`
(`:631-662`) refuses on, and never reads a key. The probe in §8 F3 observed both rows of the split.

### The guard

The policy route is owner-only by two facts, neither of them new. Provenance: `AUTH_CONF_AT` is the
merge-base of the observed default-branch tip and BASE on the second and local anchors, and BASE itself
on the first (`tools/unattended/unattended.sh:4016-4021`), so a policy commit on the run's branch is not
at it. Authorship: the pre-commit policy guard refuses an agent's commit to `.governance/policy.toml`
(`tools/policy/guarded-paths.txt:5`, `tools/policy/guard.py`). That is how fail 89's question, "could the
run have written its own opt-in", is answered for the policy route without a refusal of its own; fail 89
keeps answering it for the README route. `guard.py` "stops forgetting, not evasion" (its docstring), and
provenance is what holds against evasion, as it does for `SPEC_AUDIT_DEFAULT`.

### The effort order

| Step | Source | Applies to |
|---|---|---|
| 1 | `roles.effort.<w>.<s>` | every stage (TOOL-dBoundRoles-21) |
| 1a | `review.design.effort` | a stage key of `spec-review`, in `spec-review` or `spec-write` |
| 2 to 5 | `roles.effort.<r>`, `roles.effort.default`, the house file, the declared effort | TOOL-dBoundRoles-21 §4 |

The review's stage keys are derived from the `spec-review` workflow's stage map, the one
`resolve_stage_efforts` already resolves (`specFinder`, `skeptic` and `synthesis` at base,
`tools/roles/workflows.toml:47`), never typed. In `spec-write` they are the AUDIT stage's three keys,
and `specWriter`, `disposal` and `builder` keep their order. The key is read once per call, not per
stage key. `closing-review` shares `skeptic` and `synthesis` and is the Build review, so it is not in
`DESIGN_REVIEW_WORKFLOWS`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `DESIGN_REVIEW_WORKFLOWS` | Python constant, `tools/roles/roles_lib.py` | `py.constant`, asked of `python tools/lexicon/lexicon.py --suggest` at the pass |
| the new fail code | driver refusal, the next free number at the build run's base | none |

No verb, flag, policy key, record kind or harness argument is minted.

### Migration

None. An unset `review.design` reads `opt-in`, which TOOL-dDeclaredLoop-19 makes today's behaviour, and
an unset `review.design.effort` leaves TOOL-dBoundRoles-21's order as it lands.

### Rollout

One landing, after both parents. A repository whose policy file sets neither key sees no change.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/roles/roles_lib.py`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `help/policy.md`

`memory/guides/UNATTENDED-VERBS.md` is the render of `tools/unattended/VERBS.template.md`; the template
is the edit.

### Alternatives rejected

- Read at the landed revision, as TOOL-dDeclaredLoop-19 §4 states — lost to AC2's case: `--close`
  re-derives the opt-in and compares it with the pinned fact (`tools/unattended/unattended.sh:11943-11946`),
  so a landing between `--preflight` and `--close` trips fail 53 on a run that changed nothing.
- Every refusal read as `opt-in` — lost to the §8 F3 probe: an unreadable file and an unset key both
  exit 2 from `get`, so this option reads an owner's lost `owed` as an opt-out, fail 52's class.
- A distinct exit code for `DerivedDefault` in `policy.py get` — lost to veto 2: a change to the policy
  kit's public CLI that no clause of this build names, outside the `may:` grant.
- The effort composed by the driver and handed to the caller — lost to the harness's own statement that
  it grades the shape only (`tools/workflows/unattended-build.template.js:505-509`), so a mistyped level
  runs unrefused; `stage-efforts` is where a level is checked today.
- I3's `read_design_policy` imported into the roles kit — lost to the sibling-kit rule: TOOL-dBoundRoles-21
  §8 F2 and TOOL-dDeclaredLoop-18 §4, "a kit imports no sibling kit", observed in `roles_lib.py:147`,
  which reaches the policy kit through `resolve_kit_dir` and imports nothing of memory-tree.
- `review.design.effort` ahead of the stage key — lost to AC5's last case: an owner's
  `roles.effort.spec-review.skeptic` would be unreachable whenever the review key is set.

## 5. Production-readiness checklist

- security — the policy route is owner-only by provenance and by the policy guard (§4 "The guard"); an
  unreadable file refuses rather than reading as an opt-out; an effort is checked against
  `EFFORT_LEVELS` before it reaches a harness argument. No write path is added.
- perf / scale — one `get` per `check_authorization` call and a `check` only on its refusal; one `get`
  per `stage-efforts` call for the two design-review workflows.
- error / empty / loading states — unset key: `opt-in`, or the house order for the effort; unreadable
  file: refusal; blank `AUTH_CONF_AT`: `opt-in`, announced; unknown level: `RolesError`.
- observability — the preflight line names the opt-in's source (TOOL-dDeclaredLoop-19 S8); the refusal
  names the key and the policy kit's line; `stage-efforts` prints every resolved level.
- risks — a parent landing with another spelling of its read: the build run re-grounds (§8 F8); the effort
  read inherits TOOL-dBoundRoles-21's handling of a derived default, which its S1 states as a refusal
  (§8 F5's ask).
- testing — fixture probes per criterion; the two `New arm:` lines in §7, observed RED then GREEN at the
  close by the main loop.
- migration — none.
- user docs — `help/policy.md`, the roles README and the verbs carrier.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --preflight <slug>` runs on a fixture whose default branch's policy
  file does not set `review.design` and whose run branch alone commits `review.design = "owed"`, the
  spec-audit line reads not owed, the `opt-in` arm's text; with `owed` committed on the default branch
  at BASE instead, the line names the `policy` source.
  Red when: the read takes the run branch's HEAD or the working copy, so a run's own commit opts it in.
  fixture: a committed repository under `%TEMP%` whose build README carries no `spec-audit:` key, built
  by the probe; none in the tree today.
  permission: TOOL-dDeclaredLoop-19 S8's read lands before this unit's build run.
- **AC2** — When `unattended.sh --close <slug>` re-derives the opt-in on the AC1 fixture after its
  default branch landed `review.design = "owed"` past the BASE `--preflight` pinned with the key unset,
  the `specs-audited` term reads not owed and no fail 53 is printed.
  Red when: the read takes the landed revision, the re-derivation reads `owed` against the pinned fact,
  and fail 53 refuses a run that changed nothing.
  cost: a fixture run carried to `--close`'s Definition-of-Done terms, about a minute.
- **AC3** — When `unattended.sh --preflight <slug>` runs on a fixture whose policy file at the
  default-branch side of BASE is invalid TOML with no earlier valid revision, it refuses with the
  new fail code, naming `review.design` and the line `policy.py check --rev <sha>` printed; with the
  file valid and the key unset, or the file absent, it prints the `opt-in` arm's line.
  Red when: the unreadable file reads as `opt-in`, the silent opt-out fail 52 and fail 55 refuse.
  figure: the split is PINNED by the §8 F3 probe of 2026-10-28 and re-derived by this criterion's run.
- **AC4** — When `unattended.sh --preflight <slug>` runs on a fixture whose `prompt`-mode README declares
  `spec-audit:` and whose prompt record quotes no owner ask, fail 89 refuses and its text names
  `review.design` in `.governance/policy.toml` beside the README key and `SPEC_AUDIT_DEFAULT`; the
  local-anchor fail 89 text names it too.
  Red when: the remedy names only the two README-era routes, so the owner is never told the guarded one.
- **AC5** — When `python handoff.py stage-efforts spec-review` runs in a fixture repository whose
  landed policy file sets `review.design.effort = "max"`, it prints `max` for `specFinder`, `skeptic`
  and `synthesis`; `stage-efforts spec-write` prints `max` for those three and the house levels for
  `specWriter`, `disposal` and `builder`; `stage-efforts closing-review` prints the house levels; and
  with `roles.effort.spec-review.skeptic = "low"` also set, `skeptic` prints `low`.
  Red when: the key reaches the closing review or a non-review stage, or outranks the stage key.
  fixture: a git repository with a committed `main` under `%TEMP%`, the kit's house file as shipped.
  permission: TOOL-dBoundRoles-21's `read_policy_setting` and order land before this unit's build run.
- **AC6** — When the AC5 fixture's policy file sets no `review.design` table,
  `python handoff.py stage-efforts spec-write` prints JSON byte-identical to the same command at the build
  run's base; with `effort = "turbo"` under `[review.design]` it exits 1 naming `review.design.effort` and
  the levels `low medium high xhigh max`.
  Red when: the unset key, whose catalogue default is derived, refuses the whole verb, or an unknown level
  is handed to a harness, which `policy.py get` admits since the catalogue checks only the name shape.
  figure: the base output is DERIVED at observation time from the base checkout.
- **AC7** — When `grep -c 'read_policy_setting("review.design.effort"' tools/roles/roles_lib.py` runs it
  prints 1; `grep -cE 'policy\.py"? get review\.design --rev' tools/unattended/unattended.sh` prints at
  least 1; and `grep -c '"policy"' tools/unattended/kit.toml` prints at least 1.
  Red when: a key is built from a variable, which the reader-coverage shapes cannot see, or the driver
  reaches a kit its descriptor does not require.
- **AC8** — When `grep -c 'review.design.effort'` runs over `tools/roles/README.md`,
  `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` and `help/policy.md`, each
  prints at least 1, and `grep -c 'default-branch side'` over `help/policy.md` prints at least 1.
  Red when: the template is edited and its render is not, or the help page still says every `review.*`
  value changes no behaviour.

## 7. Gates

`unattended kit gate` · `roles catalogue` · `roles adopter self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · a run-branch policy commit, a landing past BASE, an unreadable policy file and a prompt-mode README key, staged against the driver as TOOL-dDeclaredLoop-19 lands it, which reads the landed revision and splits no refusal · none

New arm: tools/roles/adopt-roles.test.sh · covers AC5 AC6 · a fixture policy file setting `review.design.effort`, a stage key beside it, no key, and an unknown level, staged against the resolver as TOOL-dBoundRoles-21 lands it, which reads no review key · none

## 8. Open questions

- **F1 — Does this unit re-point the opt-in, or consume TOOL-dDeclaredLoop-19 S8's?** Options: (a) consume S8's derivation and build the revision, the refusal split, the guard's remedy and the effort; (b) spec the derivation again here. (b) is a second spec of one code path, which M2's interface axis refuses and the brief's parent rule forbids ("never re-spec it"); the scout record's row for this unit predates that reading. RESOLVED (agent, 2026-10-28, delegated): (a), rung 1, v2:1334 placing `review.<stage>` with dDeclaredLoop and the clause's own split, "the stage-exit recommendation being dDeclaredLoop's". widens: none · relaxes: none
- **F2 — Which revision does the `review.design` read take?** Options: (a) the landed revision, as TOOL-dDeclaredLoop-19 §4 states; (b) `AUTH_CONF_AT`, the default-branch side of the pinned BASE; (c) the run's HEAD. (c) lets a run opt itself in, fail 89's own shape. (a) moves under a running build, so AC2 fails, and on a clone with no remote it reads local `main`. (b) passes AC1 and AC2 and is the revision `SPEC_AUDIT_DEFAULT` is read at. RESOLVED (agent, 2026-10-28, delegated): (b), rung 3. The parent spec is not edited; an ask for dDeclaredLoop, filed by the main loop: "TOOL-dDeclaredLoop-19 §4 READS `review.design` AT THE LANDED REVISION, while the run's opt-in is derived at the pinned BASE and re-derived at `--close` · accept TOOL-dDeclaredLoop-19 §4's opt-in and `derive_breakpoints`' design row read `review.design` at the default-branch side of the pinned BASE, seen as `--close`'s specs-audited term agreeing with the pinned fact on a fixture whose default branch lands `review.design = "owed"` after BASE". widens: none · relaxes: none
- **FACT-QUESTION · F3 — Can an unset `review.design` be told from an unreadable policy file without a new policy-kit surface?** Probe: a fixture repository under `%TEMP%`, `python tools/policy/policy.py get review.design --rev HEAD` and `python tools/policy/policy.py check --rev HEAD` over four commits. Observation, 2026-10-28: invalid with no valid revision, `get` 2 and `check` 2; valid and unset, `get` 2 naming the derived default and `check` 0; set to `owed`, `get` 0 printing `owed`; invalid after the valid `owed`, `get` 0 printing `owed` and `check` 0. Liveness: the first commit makes `check` exit 2, so the probe can return the negative. RESOLVED (agent, 2026-10-28, delegated): yes, `check --rev` splits them, so S2 needs no new exit code. widens: none · relaxes: none
- **F4 — Where does `review.design.effort` join the effort order?** Options: (a) step 1a, after `roles.effort.<w>.<s>` and before `roles.effort.<r>`; (b) ahead of every key; (c) composed by the caller beside `stage-efforts`. (b) makes an owner's stage key unreachable whenever the review key is set; (c) loses the level check, since the harness grades shape only. (a) keeps both keys meaningful, the narrower one winning. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — Which reader reads `review.design.effort`?** Options: (a) TOOL-dBoundRoles-21's `read_policy_setting`, the roles kit's one reader; (b) I3's `read_design_policy`, a memory-tree import; (c) the caps reach `read_cap_answer` (`tools/roles/roles_lib.py:136`). (b) imports a sibling kit, which TOOL-dBoundRoles-21 §8 F2 rules out; (c) answers every refusal with the handed-in value and reads caps only. RESOLVED (agent, 2026-10-28, delegated): (a), rung 1, TOOL-dBoundRoles-21 §8 F2. Its S1 makes a `get` exit 2 a `RolesError`, and `get` exits 2 for every unset key whose default is derived (`tools/policy/policy.py:687-698`), which `review.<stage>.effort` and each of its own four keys are; an ask for dBoundRoles, filed by the main loop: "TOOL-dBoundRoles-21 S1 READS AN UNSET DERIVED-DEFAULT KEY AS A REFUSAL · accept `read_policy_setting` returns None for an unset key whose catalogue default is derived and keeps `RolesError` for every other refusal, seen on a fixture setting no `roles.effort` key where `handoff.py stage-efforts` prints the house levels". widens: none · relaxes: none
- **F6 — Does this unit call the stage-exit recommendation?** Options: (a) no call, consuming TOOL-dDeclaredLoop-22 as built; (b) call `--recommend <slug> --stage design` from `--preflight`. (b) scores before SPEC has written the specs whose forks are a signal, and makes this unit a second caller of a verb whose caller TOOL-dDeclaredLoop-22 §2 S5 and S7 document; a recommendation also writes no opt-in (its §3). RESOLVED (agent, 2026-10-28, delegated): (a), rung 1, the clause "the stage-exit recommendation being dDeclaredLoop's (AF-1)". widens: none · relaxes: none
- **F7 — `review.<stage>.effort` is dCalibratedLens's key (v2:1335), a build after this one. Does this unit read it?** Options: (a) read it for the design review alone; (b) leave every review's effort to dCalibratedLens. (b) carries the clause without its "effort", which fails veto 1. RESOLVED (agent, 2026-10-28, delegated): (a), rung 1, the clause and the walkthrough's candidate 3 (walkthrough:419-420, "`review.design` opt-in by default with its effort"). dCalibratedLens's own clause names Plan, Test, Deploy and Maintain, so step 1a is the seam it extends. widens: none · relaxes: none
- **F8 — Both parents are specced and not built at `57bc3b91`.** Options: (a) a build-run precondition, the unit built only once TOOL-dDeclaredLoop-19 and TOOL-dBoundRoles-21 are CLOSED; (b) a stand-in read here until they land. (b) is a second reader of `review.design` and a second policy read in the roles kit, each deleted the day its parent lands. RESOLVED (agent, 2026-10-28, delegated): (a), rung 1, the brief's rule for unbuilt parents; the build run re-grounds on both at its base and stops this unit if either is absent. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 3, scout A's row for this unit, the driver's
  opt-in derivation and fail 89 at base `57bc3b91`, the policy kit's `get` and `check`, the roles kit's
  effort resolver, and the parent specs TOOL-dDeclaredLoop-19, -22 and TOOL-dBoundRoles-21.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-41, promoted by the round-1 spec audit of units 31 to 38; nothing else
  moved.
- rev-4 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seams, each read at `57bc3b91`. The opt-in read extends `check_authorization`'s
`SPEC_AUDIT_DEFAULT` derivation (`tools/unattended/unattended.sh:4016-4041`): its revision `AUTH_CONF_AT`,
its blank-revision guard and its unknown-is-not-absent rule are reused, not restated. The refusal split
reuses the policy kit's own `check` verb (`tools/policy/policy.py:1363-1379`, `check_revision` at
`:665-676`). The effort extends `resolve_stage_efforts` (`tools/roles/roles_lib.py:596-601`) as
TOOL-dBoundRoles-21 re-points it, read through its `read_policy_setting`; the harness's existing
`efforts` forwarding (`tools/workflows/unattended-build.template.js:535-537`, `:1661`) carries the level
with no change. The guard is the landed policy guard (`tools/policy/guarded-paths.txt:5`).

`python tools/codebase-map/reuse_lookup.py "read the spec audit opt-in from the policy file at the pinned
base"` ranked the generic `read`, `read_text`, `read_conf_key`, `resolve_compare_base`, `readPolicy` and
`load_policy`; none reads a policy key at a pinned revision, and source agrees that the driver reads no
policy key at HEAD (no `policy.py` call in `tools/unattended/unattended.sh`). `python
tools/codebase-map/reuse_lookup.py "resolve the reasoning effort a review stage spawns at"` ranked
`resolve` (`tools/policy/policy.py:752`), `resolve_caps` and `resolve_kit_dir`, and did not rank
`resolve_stage_efforts`, found instead by reading `print_stage_efforts` (`tools/roles/handoff.py:474`).

`python tools/memory-recall/query.py "how is the design review opted in by policy with its effort and the
owner-only guard"` returned scout A's row and the brief (hits 1 to 4), TOOL-dBoundRoles-21's effort order
(hit 6) and TOOL-dDeclaredLoop-19 §4's opt-in table (hit 10). Where a record and source disagree: scout A
names the re-point as this unit's work, while TOOL-dDeclaredLoop-19 S8 already specs it (§8 F1); scout A
places the effort at `tier2-review.js`'s `efforts` argument (`tools/workflows/tier2-review.template.js:254`),
which is where it arrives, while the level is composed by `handoff.py stage-efforts`, which
TOOL-dBoundRoles-21 re-points; and TOOL-dDeclaredLoop-19 §4 reads at the landed revision, which §8 F2
answers with an ask. The scout's line citations (`:3975`, `:4024-4034`, `:4113`, `:4125`,
`catalogue.toml:1206-1212`, `policy.py:687-698`) match source at `57bc3b91`.

Recall terms used: review.design spec-audit opt-in SPEC_AUDIT_DEFAULT fail 89 guarded policy.toml effort stage-efforts AUTH_CONF_AT
