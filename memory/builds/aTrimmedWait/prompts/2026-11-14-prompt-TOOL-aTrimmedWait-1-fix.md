# Fix — TOOL-aTrimmedWait-1: the unattended Skill never invokes `--check-specs`

**Serves:** research TOOL-aTrimmedWait-1

## The prompt

The unit's own builder reported, on its pass commit 78cc7c112, quoted:

> check 26 also requires every declared verb to be invoked in `tools/unattended/SKILL.template.md` (the `*"unattended.sh $v "*` case in `tools/unattended/check-unattended.sh`, near line 4946). `--check-specs` is now in `VERBS_INLINE` but the Skill does not invoke it, so check 26 will fail with "a declared verb is never invoked in the Skill".

The main loop's pass-legs run over b9ad1f6ba..78cc7c112 then reported these reds the pass owns, quoted:

> install-prefix: a tracked file spells a kit path ... tools/workflows/unattended-build.test.sh@5118b298:3760, :3761 and :3764 (the three new `TW1 AC5` assertions)

> HYGIENE check-arms: tools/unattended/unattended.sh@cdfd8502:15453 exit site (delegated) has no POSITIVE assertion naming its own failure text ('refuse_waive_unless_preflight --check-specs || { RUNLOG_CLEAN=1; exit 1; }') and is not pinned ... mark its block with `# arm-signature: <text its callee prints>` and assert that text, or pin it

> HYGIENE check-arms: tools/unattended/unattended.sh@cdfd8502:14618 check 49 branch 23 has no POSITIVE assertion naming its own failure text ("a sibling spec status header carries something shaped like the build-order verb that does not conform, so this build's order cannot be sequenced against it") and is not pinned

> HYGIENE check-arms: tools/unattended/unarmed-branches.txt:50 pins tools/unattended/unattended.sh check 49 branch 21, which IS armed now — delete the row (the pin is shrink-only)

> HYGIENE check-arms: tools/unattended/unattended.sh has 326 fail branch(es) and refusal site(s) against a ceiling of 324 (REFUSAL_CEILINGS, 2026-11-10, TOOL-aSmoothedDispatch-2) — growth past the budget is raised only through the retirement review in the memory-tree README, with a dated decision id; retire or consolidate a site first

> lexicon: verb offenders 1209 over pin 1208 — the one new definition is the suite helper `cs_mk` (leading token `cs`, unruled)

> pinned-facts: red · memory/builds/aTrimmedWait/build/2026-11-14-build-TOOL-aTrimmedWait-1-1-acceptance-ledger.md · unpinned fact `60 s` (DERIVED from the pass-legs log)

## The brief

### Goal
Close the check-26 gap the pass left: the unattended Skill invokes `--check-specs`, so every verb
the driver declares is one an agent following the Skill would call, and clear every red the pass legs
reported over its pass commit. gov-spec-writer revised the spec first (rev-2, Files touched gains the
Skill template and its render); build to it, then set the header CLOSED again as the last commit.

### Items
1. `tools/unattended/SKILL.template.md` carries one `unattended.sh --check-specs <slug> <unit-id>...`
   line in its verb block beside `--plan <slug> --paths`.
2. The rendered `.claude/skills/unattended/SKILL.md` is re-rendered from it, and
   `bash tools/unattended/adopt-unattended.sh --check` agrees.
3. Every red the prompt section quotes is cleared in the same pass: the three `TW1 AC5` lines spell
   no kit path; the `--check-specs` exit site is marked and asserted or consolidated; branch 23 is
   armed or pinned and the stale branch-21 pin row is deleted; the driver's refusal sites return to
   the 324 ceiling by consolidation (no ceiling raise: that needs a dated decision this build has
   not taken); `cs_mk` takes a declared verb (`python tools/lexicon/lexicon.py --suggest cs_mk --as sh.function`);
   and the ledger's `60 s` carries a pin. DERIVED from the pass-legs log
4. The spec was revised by gov-spec-writer before this pass (rev-2: Files touched gains the Skill
   template and its render); build to that revision.

### Acceptance
- `grep -c 'unattended.sh --check-specs ' tools/unattended/SKILL.template.md` prints 1.
- The rendered Skill carries the same line, and the render check exits 0.
- The acceptance ledger gains a row for this fix, under the same ledger file.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals. No version bump: kit versions move once, after the last code move.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
The existing `--plan`, `--claims` and `--overlaps` invocation lines in the Skill template's verb block.
