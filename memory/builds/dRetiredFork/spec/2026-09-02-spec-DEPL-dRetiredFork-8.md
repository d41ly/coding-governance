# DEPL-dRetiredFork-8 — the falsification set stops counting a unit that absorbs nothing

**Status:** OPEN · rev-2 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams deployer · order 0

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED from spec-audit round 2, blocker 1. `DEPL-dRetiredFork-6` §6 AC2 requires `contribute` to
propose `TOOL-dRetiredFork-4` among six inCMS-sourced units. That unit was rescoped at `b17f22ed` to
"absorbs nothing until it has" and its §3 forbids editing `tools/hooks/agent-cap.js` at all. Under
every one of its three S3 dispositions the inCMS `KIT_AGENT_CAP_DELTA` D1 row is class 4, stale, or
already-absorbed — never a class-1 or class-2 contribution. So a CORRECT verb proposes five and reds
AC2.

That is round 1's H2 shape — a criterion a correct implementation fails — reintroduced by the commit
that fixed H2, in the file H2 was fixed in. This unit owns the correction; `DEPL-dRetiredFork-6` is
NOT edited by any other unit, so the defect has exactly one owner.

## 2. Scope (IN)

- **S1** — `DEPL-dRetiredFork-6` §6 AC2 names FIVE inCMS-sourced units — `TOOL-dRetiredFork-5`, `-6`,
  `-7`, `-8` and the C21 half of `-9` — and strikes `-4`.
- **S2** — AC2 gains a clause requiring the verb to report the D1 row as stale or ALREADY ABSORBED,
  which is that spec's own F2 shape, rather than as a contribution.
- **S3** — "nine" becomes "eight" at `DEPL-dRetiredFork-6` §1, §4 Rollout (both sites) and §5, and §4
  Rollout says ONCE why the ninth order-1 unit is excluded, so the set reads as deliberate.
- **S4** — The build README's two surviving nines — the Build-level rules bullet and the roster's
  order-1 sentence — are re-rendered to eight, matching the three sites already corrected.
- **S5** — Every edit is a WHOLESALE rewrite of the sentence or criterion it touches, never a
  prepend. Round 2 measured that 21 of its 30 defects were created by patch-in-place folding.

## 3. Non-goals (OUT)

- Re-opening `TOOL-dRetiredFork-4`'s rescope. It is correct and this unit follows it.
- The left-shift gate the review proposes for this class — extracting unit ids from a §6 criterion
  and redding when the named spec's §1 disclaims contributing. That is `TOOL-dRetiredFork-20`'s spec
  lint, which owns every spec-token check in this build.

## 6. Acceptance criteria

- **AC1** — `grep -c 'TOOL-dRetiredFork-4' memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md`
  returns `0` outside the generated records region.
- **AC2** — `grep -n 'nine' memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md`
  and the same over `memory/builds/dRetiredFork/README.md` return no hit describing the absorption
  count.
- **AC3** — The five unit ids AC2 names are each a row in the README's roster, checked by a join against the
  roster region of `memory/builds/dRetiredFork/README.md` rather than by eye.
- **AC4** — `bash tools/memory-tree/check-memory-hygiene.sh` exits `0` and
  `python3 tools/memory-tree/gen_build_index.py --check` exits `0` after the edit.

## 7. Gates

`memory hygiene` · `build README slot contract` · `build-index selftest`.

## 8. Open questions

none - it is a PROMOTED round-2 blocker whose correction round 2 already stated, and
it changes one falsification set in one direction. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. PROMOTED from spec-audit round 2 blocker 1 under BUILD-METHOD
  M4's disposition rule, on the owner's instruction to promote rather than fold.
- rev-2 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.
