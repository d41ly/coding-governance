**Serves:** research TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 TOOL-dScopedBuild-13

# Reuse scout C — dScopedBuild

The scout's final return, extracted from its transcript by script, never retyped.

# Scout C: reuse report for TOOL-dScopedBuild-2, -4 and -13

All three clauses can be built on code that already exists. None of them needs a new subsystem. Two of them lean on grandparent specs that are still DEFERRED: `TOOL-dDeclaredLoop-20` (it owns `review.findings`) and `TOOL-dDeclaredLoop-29` (it owns the `upstream` rows). I ran `reuse_lookup.py` with four behaviour phrases. All layers were scanned and none was recall-dark. The shortlists pointed at `design_lib.read_spec_revisions` (SEAM), `deviation_join.py`, the driver's `closing-review-recorded` arm and `tier2-review.js`. I then read each source; the line numbers below are at HEAD `2bba66753`. I wrote nothing in the repository.

## Table: one row per clause

| | TOOL-dScopedBuild-2 (`cl-dClosedLoop-0400@d5dcbafa`) | TOOL-dScopedBuild-4 (`cl-dClosedLoop-0402@19e9688b`) | TOOL-dScopedBuild-13 (`cl-dClosedLoop-0411@78cc90dd`) |
|---|---|---|---|
| **Seam to extend** | **(a) The freeze.** Reuse `deviation_join.check_material(before, after)` at `tools/memory-tree/deviation_join.py:436`. It is the existing status-only predicate: it strips the `**Status:**` line in `extract_authored` (`:422-433`) and every generated region with the unattended kit's `GEN_REGION_AWK` (`tools/unattended/lib-unattended.sh:1136`), read through `read_gen_region_awk` (`:355`). The "landed" test reuses `read_decision_ref` (`deviation_join.py:676`), the remote ladder that gives the mainline ref; the unit's spec header is read at that ref with `tree_lib.HDR_RE` (`tools/memory-tree/tree_lib.py:376`). For the host, copy the `--staged` pass-through that hygiene checks 29 and 30 use (`tools/memory-tree/check-memory-hygiene.sh:1802`, `:1843`). The pre-commit hook already runs `check-memory-hygiene.sh --staged` whenever `memory/**` is staged (`.githooks/pre-commit:226-233`). **(b) The disposal.** Call the `TOOL-dDeclaredLoop-20` S4 promotion count; do not re-spec it. That count sits in `verb_review`'s owe arithmetic at `tools/unattended/unattended.sh:12823`, in check 2's floor, and in the DISPOSAL floor/ceiling at `tools/workflows/unattended-build.template.js:2203-2205`. This unit edits only the in-loop blocker-fold instructions. | Extend the `closing-review-recorded` case of the DoD (`tools/unattended/unattended.sh:11767-11893`). It already joins a tracked `diff-review` record that names a commit in BASE..HEAD (`:11826-11838`) and the last terminal `--review` round on the build-slug subject (`:11872-11890`). Read the key with `policy.py get review.build.when`; the row is at `tools/policy/catalogue.toml:1224-1227` (allowed per-build, per-unit, per-landing; default per-build; owner dScopedBuild). Get each unit's range from `pass_commit` (`tools/unattended/lib-unattended.sh:1026`) and `read_run_commits` (`:1307`). | **(a) The rows.** Use `TOOL-dDeclaredLoop-29` §2 S3–S8: the `## Establishes` grammar, `derive_upstream_rows`, `join_upstream(rows, answers, gate)`, gate `record` or `measured` with `measured-by`, and the record `…-upstream-<n>.md`. **(b) The criteria.** Read them with `extract_acceptance` (`tools/check-spec-tokens.py:539`) and the AC-label regex (`check-memory-hygiene.sh:2104`). **(c) The MUST seams.** Use `TOOL-dIndexedDesign-13` §2 S6, rows `- seam-<n> · seam · <path> :: <symbol>`. **(d) The hand-off.** Extend `tools/workflows/tier2-review.template.js` beside `priorFindings`: arg parse at `:293`, the lens-prompt block at `:1161-1168`, the input print at `:985` (each new input must join it, or a resume reuses stale lens files), and `FINDING_SCHEMA` at `:630` (an answers array). |
| **What already exists** | `deviation_join` already finds a spec revision made after the unit's first pass (`:582-607`). Hygiene check 30 only *reports* a missing record (values `report`, `author-recorded`), and the join runs at push time (`gate-legs.json:1095`). Nothing refuses at the commit. Nothing refuses *with* a record. Nothing reads the mainline. The unattended `--review` already promotes at every terminal exit and refuses `fold` there (`unattended.sh:12786-12830`). The mid-loop blocker fix in place is still prescribed in M8 (`tools/memory-tree/BUILD-METHOD.template.md:274`) and in the attended Skill's Stage 6 (`tools/roles/SKILL.template.md:78-80`, rendered to `.claude/skills/build/SKILL.md:78-80` by `tools/roles/adopt-roles.sh:129`). | Per-build is built for unattended runs only (`DOD_CORE`, `unattended.sh:868`). Attended runs have nothing: M8 owes the review and nothing checks it (research-build.md:78, 97-99). Per-unit and per-landing do not exist. `verb_review` treats every subject other than the slug as a spec audit (`:12694-12698`), so a per-unit closing-review subject has no home today. | `tier2-review.js` takes `specs` as free intent documents (`:116`). The `intent` lens asks finders to "report an acceptance criterion with no code behind it" (`:798`), but no rows are handed and no answers are required. Nothing in `tools/` implements upstream rows; probe: grep `upstream` over `tools/loop` and `tools/roles` finds no such field. |
| **Design sources that decide it** | v2:914-916 (P19); v2:41-43; flow.md:382-387 (FL-B3, owner's words); flow-steps.md:302-306; final-questions.md:186-188 ("a fold into a built unit" is drift; after landing, a change is a new unit); gap-register:110 (gap-flow-05); dSweptBranches README:49-50 (the motivating case); v2:1338 and 1660 (`review.findings`, owner dDeclaredLoop) | walkthrough.md:498-500 (unit 3: "a build whose units close in the pushed range needs a review record naming a commit in that range"); walkthrough.md:523-524 and 536 (fork B3, default per-build); v2:1337 and 1659 (presets: one preset is per-unit); research-build.md:97-99 and 147 (pick A: push-boundary, same contract attended and unattended); gap-register:363 (gap-build-02) | night-pass-two.md:197-199 (rows recorded on every edge, gating where measured, NT-10); :214 (S-item and acceptance rows into the closing review "wait on measurement"); :349-350; research-handoffs-design.md:129 (§5 item 6, the verifier's packet); gap-register:128 (gap-flow-22) |
| **Owned nodes to name** | None of the 23 fits cleanly; carry the clause only. It *reads* `policy-key.review.findings`, which is dDeclaredLoop's; cite it, don't carry it. | `policy-key.review.build.when` | None fits cleanly; carry the clause only. The gate value is `TOOL-dDeclaredLoop-29`'s, not a key of this build. |
| **Product paths** | `tools/memory-tree/deviation_join.py` (a new frozen arm plus a `--staged` verb); `tools/memory-tree/check-memory-hygiene.sh` (a new check that passes `--staged` through); `tools/memory-tree/HYGIENE.template.md` → `memory/HYGIENE.md`; `tools/memory-tree/BUILD-METHOD.template.md` (M8:274); `tools/roles/SKILL.template.md` (Stage 6); `tools/gate-legs.json` (fixture leg) | `tools/unattended/unattended.sh` (the `closing-review-recorded` arm and `verb_review`'s subject kinds); the both-mode exit host that TOOL-dScopedBuild-1 builds; `tools/roles/SKILL.template.md` Stage 6 | `tools/workflows/tier2-review.template.js` → `tier2-review.js`; `tools/workflows/tier2-review.test.sh`; `tools/memory-tree/BUILD-METHOD.template.md` (M8's args block, :262-265); `tools/roles/SKILL.template.md` Stage 6; the caller that derives the rows (`tools/loop/upstream.py` once dDeclaredLoop-29 is built) |

### Where records and source disagree

1. **"Landed" is not the same as CLOSED at HEAD.**
   - TEMPLATE-SPEC:64 defines CLOSED as "built and landed".
   - But the harness writes CLOSED in the build commit on the run branch, before landing (ask PLAY-dClosedLoop-20).
   - So the freeze's "landed" test must read the spec header at the mainline ref. HEAD's header is not enough.

2. **The clause's trigger does not catch its own motivating case.**
   - gap-flow-05's example (dSweptBranches rev-3) was a fold *before* landing. A "landed" trigger does not refuse it.
   - That case is caught two other ways: the disposal half (blockers become units, not folds), and TOOL-dScopedBuild-14's deviation gate over the existing first-pass arm.
   - The spec should say this explicitly, or an owner should widen the trigger to "built".

3. **"At the commit" in the deviation_join docstring does not mean the pre-commit hook.**
   - The docstring (`deviation_join.py:68-72`) means a per-commit join that runs at push.
   - `.githooks/pre-commit` names neither `deviation_join` nor `routed_commits` (grep count 0).

4. **`TOOL-dDeclaredLoop-20` §1 cites stale line numbers.**
   - It cites `unattended.sh:12819` for the owe count; at HEAD that is `:12823`.
   - It cites `unattended-build.template.js:2205-2208`; the `adjudicated` line is at `:2203`.

5. **M8 and the attended Skill's Stage 6 still prescribe what P19 forbids.**
   - Both tell the builder to fix each blocker as a pass of the built unit it lands in.

6. **No parent spec defines how a spec "carries" its MUST seams.**
   - dIndexedDesign-13 S6 hands the seam rows to `item.design.decompose`, and stops there.
   - Clauses -12 and -13 both read "the MUST seams its spec carried".

## Shared interfaces

1. **The status-only predicate.** `deviation_join.check_material` (`deviation_join.py:436`). Shared by TOOL-dScopedBuild-2's freeze and TOOL-dScopedBuild-14's gate (scout A). Call it; never re-strip.

2. **The landed predicate.** Proposed name: `read_landed_units(root, units)` in `deviation_join.py`. It reads each spec's header at `read_decision_ref(root)` (`:676`) and returns the units that are CLOSED there. Shared by -2 and -14, and by -1 (scout A) if its history-derived base needs "landed".

3. **The commit-time host.** One `deviation_join.py --staged` verb, called from a new hygiene check that passes `--staged` through as checks 29 and 30 do.
   - It holds two arms: the freeze arm (-2, always refuses) and the `deviation.gate` arm (-14, graded by its key).
   - The check number must be agreed across the chain. `TOOL-dIndexedDesign-13` S8 already claims 31, so I propose **32**: "a landed unit's spec is not revised in place".

4. **The disposal count.** `review.findings` through `TOOL-dDeclaredLoop-20` S4. It is computed in `verb_review` (`unattended.sh:12823`). Both -2 and -4 read it. No unit of this build re-derives it.

5. **The closing-review predicate.** The `closing-review-recorded` arm (`unattended.sh:11767`).
   - -4 makes it read `review.build.when`; -1 (scout A) moves it into the exit contract shared by both modes.
   - One function is proposed for both: `check_closing_review_recorded <slug> <when>`, lifted out of the case arm.

6. **The review subject grammar.** Today there are two kinds: the build slug means a closing review, and anything else means a spec audit (`:12694`).
   - Proposed spelling: per-build uses `<slug>`; per-unit uses `<slug>:<unit id>`; per-landing uses `<slug>@<landing sha7>`.
   - `review_last_reason` (`:12630`) and the `--close` term must read the same spelling.

7. **The row grammar.** `- <row id> · <kind> · <text>` for rows, and `- <row id> · used|bypassed|not-applicable · <reason>` for answers. Both come from `TOOL-dDeclaredLoop-29` S3 and S5.
   - Shared by -12 (scout D: its MUST-seam rows and the disputed rows sent to the closing review) and -13.
   - Criterion rows: `criterion-<unit id>-AC<n>`. Seam rows: `seam-<n>`, as dIndexedDesign-13 S6 spells them.

8. **The MUST-seam reader for a unit's spec.** One reader, shared by -12 and -13.
   - Proposed: `read_spec_musts(spec_text)`, reading `- seam-<n> · seam · <path> :: <symbol>` lines in the spec's §10 Reuse audit.
   - No source spells this yet (see disagreement 6). Scouts C and D must agree on it before either spec is written.

9. **The acceptance-criteria reader.** `extract_acceptance` (`tools/check-spec-tokens.py:539`) plus the AC-label regex at hygiene `:2104`. Used by -13. Scout A's -15 (`build.acceptance`) reads the same §6.

10. **The tier2-review argument.** Proposed name: `upstream: [{id, kind, text}]`, after the `### upstream:rows` block in dDeclaredLoop-29 S5.
    - It is rendered beside `PRIOR ROUND'S FINDINGS` and joined into `inputPrint`.
    - Its answers are a required `upstream` array on `FINDING_SCHEMA`.
    - -12's disputed rows enter the closing review through this same argument.

11. **The rows record.** `memory/builds/<slug>/build/<date>-build-<unit id>-upstream-<n>.md` with `**Serves:** journal <unit id>` (dDeclaredLoop-29 S8). -13 records into it and does not mint a review-local shape.

## Proposed build order within this group

1. **TOOL-dScopedBuild-2, freeze half first.** It needs nothing unbuilt: `check_material`, `read_decision_ref` and the `--staged` pass-through pattern all exist at HEAD. It also mints shared interfaces 2 and 3, which -14 consumes. Its disposal half (the M8 and Skill Stage 6 edits) can land at the same time as text, but its counts come live only once `TOOL-dDeclaredLoop-20` is built.

2. **TOOL-dScopedBuild-4 next.** It extends the per-build arm that exists and adds the subject kinds of interface 6. It must follow -1's both-mode exit host (scout A), because attended runs have no exit contract to carry the predicate until then. It must come before -13, because -13 hands rows per unit and needs the per-unit review shape.

3. **TOOL-dScopedBuild-13 last.** It consumes `TOOL-dDeclaredLoop-29`'s rows and join and `TOOL-dIndexedDesign-13`'s seam rows, both DEFERRED and unbuilt. It needs -4's per-unit subject. It needs interface 8 agreed with -12. Its "gating once a measurement passes" arm stays at gate `record` until a measured-by record exists; dDeclaredLoop-29 S2 says no gov entry ships at `measured`.
