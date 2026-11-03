# TOOL-dCalibratedLens-37 — a fence edit selects the format guard's suite through `AGENTS.md` alone, a guard pathspec check 7c classes exactly once

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-37-deviation-371.md](../build/2026-11-02-build-TOOL-dCalibratedLens-37-deviation-371.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 24, HIGH, item H4 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 25 S3 adds the bare root
path `coding-governance-agents.template.md` to the `format-guard self-test` guard. govkit's check 7c
(`tools/govkit/govkit.py:2317-2337`) needs every guard pathspec to fall into exactly one declared
class, and that path falls into none: it is under no memory, verbatim, renamed or kit directory, no
`[[exempt]]` row names it, and no kit declares it a root conf. The unguarded `govkit selfcheck` leg
then reds and unit 25 cannot land, and unit 25 §7 does not name that leg. This unit takes the guard
change out of unit 25 and puts it on `AGENTS.md` alone, which the registry already classes `exempt`
and which every fence edit reaches through the render. The round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`, id 23) found the guard edit
itself made in a manifest the leg factory will render, so the edit and its criteria are
`TOOL-dCalibratedLens-47`'s, which makes it in the leg's declaration; this unit keeps the disposal
of unit 25. It repairs `TOOL-dCalibratedLens-25`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 25's text (rev-2, id 24): unit 25
  edits no guard, its S3 and its third criterion name the guard's unit, and its Files touched lists
  no `tools/gate-legs.json`. Observed by AC1.
- **S2** — The guard, `AGENTS.md` and only that in the `format-guard self-test` guard, is
  `TOOL-dCalibratedLens-47`'s S2 and S3 (round-3 id 23): a fence edit lands in
  `coding-governance-agents.template.md` and its render `AGENTS.md` in one commit, so the rendered
  file selects the leg for both. NOT OBSERVED here — `TOOL-dCalibratedLens-47` AC1 and AC3 observe it.
- **S3** — The leg line naming `govkit selfcheck`, the always-run leg whose check 7c grades the new
  pathspec, is `TOOL-dCalibratedLens-47`'s S4, with the criterion that observes check 7c's classing
  (round-3 ids 7, 16 and 26). NOT OBSERVED here — `TOOL-dCalibratedLens-47` AC2.

## 3. Non-goals (OUT)

- A new pathspec class in `tools/govkit/govkit.py` for root template files, the review's other
  option. It widens a governance kit's taxonomy for one file the render already covers.
- The units field, its fixtures and their arms: `TOOL-dCalibratedLens-25` S1 and S2, unchanged.
- A spec-token join that owes `govkit selfcheck` to every spec editing a guard, the finding's
  left-shift line. Run over the live specs at base, the predicate reds two specs of other builds
  (`aMendedLedger-1` and `aQuarriedLantern-1`) besides unit 25; a join that reds other builds'
  records is not this build's to land.
- AC1 observes only the disposal's text in unit 25 and is green at writing; it is a precondition,
  not an observation of a build.

### Edges

- **hands-off** `TOOL-dCalibratedLens-47` — the guard edit of S2 and the leg line of S3, which that unit makes in the `format-guard self-test` declaration (round-3 id 23)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:2317-2337` at base: the classes are memory-root-relative, verbatim-repo-root,
  renamed, exempt, kit-relative and root-conf, and a pathspec in other than one fails.
- `tools/govkit/registry.toml:335-337` at base: an `[[exempt]]` row with `path = "AGENTS.md"`.
- `python tools/check-spec-tokens.py --legs-for AGENTS.md` at base prints only `policy fixtures <-
  AGENTS.md`; the same query for `coding-governance-agents.template.md` prints `no guarded leg`.
- The predicate "a live spec lists `tools/gate-legs.json` under Files touched and its §7 lacks
  `govkit selfcheck`", run over the 59 live specs at base (2026-11-02, PINNED), matched 3 of the 8
  that list the manifest.
- `tools/govkit/registry.toml:578-580` at base: the leg is an `[[exempt_leg]]`, the row
  TOOL-dWitnessedBar-11 S1 makes its one declaration once the factory lands (round-3 id 23).

### Inventory

No identifier is minted.

### Files touched (estimate)

None. The guard's files are `TOOL-dCalibratedLens-47`'s.

### Alternatives rejected

- **An `[[exempt]]` row for the template.** The template sits inside the registry's declared surface,
  so an exemption would narrow what the surface ships, which the review rules out.
- **Leave the template in the guard and add `govkit selfcheck` to §7.** The leg would observe the
  red, not prevent it.
- **Keep the guard edit here at rev-2.** The edit is made in the declaration the factory reads, which
  needs a which-case decision at the pass; one unit owns that decision for the leg.

## 5. Production-readiness checklist

- security — N/A: no build of its own.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — a template edit landed without its render: the render's own wiring check reds that drift,
  so the guard's reach through the render holds once unit 47 lands it.
- testing — AC1, a precondition read at writing.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -n "TOOL-dCalibratedLens-47"` runs over unit 25's spec, its S3 names that unit
  as the guard's, and `sed -n '/### Files touched/,/### Alternatives/p'` over the same spec, piped to
  `grep -c gate-legs.json`, prints 0.
  Red when: unit 25 still edits a guard, or names a guard unit that does not make the edit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 24 (HIGH, item H4) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 25 amended at the disposal (its rev-2),
  its guard change moving here.
- rev-2 · 2026-11-03 · §1 §3 §4 §5 §6 §7 §10 S2 S3 AC1 AC2 AC3 · amended at the disposal of the
  round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: S2 and S3 and their
  criteria move to `TOOL-dCalibratedLens-47`, which makes the edit in the leg's declaration (id 23);
  the criterion check 7c's classing needs is that unit's AC2 (ids 7, 16 and 26, from
  `TOOL-dCalibratedLens-48`); AC1 is a precondition; §10 records this unit's own probe phrase (id 21,
  `TOOL-dCalibratedLens-48`); §3 hands the guard to unit 47.

## 10. Reuse audit

The seam extended is the registry's existing `AGENTS.md` exemption, which check 7c already classes;
no class is added, and the guard row is `TOOL-dCalibratedLens-47`'s. `python
tools/codebase-map/reuse_lookup.py "classify a guard pathspec into exactly one declared class"`
ranked name stems only (`classify` in `tools/govkit/census.py`, `declares`, `classify_outcome`,
`declared_list`); none is check 7c's taxonomy, which was read by hand in
`tools/govkit/govkit.py`, and `--legs-for` of `tools/check-spec-tokens.py` is the query unit 47's
criteria use. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's
order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
