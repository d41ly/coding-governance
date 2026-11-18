**Serves:** research TOOL-dDeclaredLoop-5

# Brief: revise spec TOOL-dDeclaredLoop-5 for the unattended checker's refusal ceiling

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The dispatch of TOOL-dDeclaredLoop-5 built rev-4 whole, then restored it and returned a divergence: the
spec's check 53 adds two refusal sites to `tools/unattended/check-unattended.sh`, whose census already stands at its ceiling of
264 in `.memory-tree.conf`'s `REFUSAL_CEILINGS`. The return is
`memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-5-1-builder-return.md`, and the built change is saved
as a patch the next builder may read.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-5.md` in place, as a rev bump with one revision-log
line naming that return, so the unit builds with the `harness arms` leg green.

### Items

1. Read the growth-budget rule above `REFUSAL_CEILINGS` in `.memory-tree.conf` and the retirement review it names, and the
   precedent there: TOOL-dTrueNorth-27 raised the driver's ceiling under decision TOOL-dTrueNorth-28, citing the standing
   ruling ER:388, after its retirement review found no candidate. Weigh three routes as a section 8 fork with your
   recommendation, the body written on it: (a) run the retirement review over the checker's refusal sites, and if it finds no
   candidate raise the ceiling by the sites check 53 adds under a decision row citing ER:388, with `.memory-tree.conf`,
   `memory/DECISIONS.md` and the unattended suite arm that pins the figure in Files touched; (b) retire or consolidate
   existing sites the review finds, recorded in `memory/project/refusal-retirements.txt`; (c) grade the declaration sites
   somewhere outside the budgeted checker, such as the loop kit's own leg, if the clause it carries allows that. Read the
   clause the unit carries before choosing (c). Prefer the route that keeps the clause whole with the least governance
   change; mark a route that changes a governance carrier with its ruling and `widens:` as the README's rules require.
2. Add the two helper names the builder needed beyond the inventory, `ACTOR_LIST` and `read_actor_rows`, to section 4.
3. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the revised spec and fix every hit. Do not run
   the whole-tree memory hygiene gate, and do not ask any checker for its help text.

### Acceptance

- The revised spec's design leaves every refusal census at or under its ceiling, or raises a ceiling only under a cited ruling.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
