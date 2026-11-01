# Fix brief — dFoldedAudit: the M3 sweep and the M2 cross-read

**Serves:** research TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-5

## The brief

### Goal
Resolve the one open fork and fold the writers' flagged defects, then cross-read all eight specs so none disagrees with another before the first build pass. The writers' returns are at `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md`. Commit nothing; the main loop commits.

### Items
1. TOOL-dFoldedAudit-5 §8 F1 is RESOLVED to option (b): U leaves out P(N), and step 1's audit set is U with P(N) and F(N). Mark it in the §8 shape `memory/TEMPLATE-SPEC.md` states, `RESOLVED (agent, 2026-11-01, delegated)`, with the option's own reason: it alone meets both owner rulings and R1. Its §4, AC6 and AC8 are already written to it.
2. TOOL-dFoldedAudit-1's non-goal attributes the `.unattended.conf` writes to TOOL-dFoldedAudit-2. The briefs give them to TOOL-dFoldedAudit-7. Correct it.
3. TOOL-dFoldedAudit-1's carrier sentences name the `disposal` arg but not the `planState` requirement TOOL-dFoldedAudit-4 §3 hands to it. An unattended caller omitting `planState` meets refusal rows 15 and 16 on its first fold. State it, with a backticked payload a gate can read.
4. Run M2's cross-read over all eight specs on its four axes: scope, interface, ordering, acceptance. Every name, path, signature, conf key, flag, row field and record shape spelled twice must be spelled identically. Fix each disagreement in exactly ONE spec, rev bump and §9 line naming what disagreed.
5. Confirm the design's [cutoff] value and unit 7's check agree with `tools/unattended/unattended.sh:1009-1012`, which records a landing-day value redding a same-day record.

### Acceptance
Every folded spec carries a rev bump and a §9 line. `unattended.sh --plan dFoldedAudit` reads READY for all eight once committed. The return lists each fold by spec and rev, and each cross-read axis with its result.

### Gates
Hygiene checks 5, 12 and 25 in a scratch clone, as the writers ran them. No gate leg in this tree.

### Non-goals
A disagreement that is a choice rather than an error is reported, not decided. No design tag is re-opened. No code, and no write outside this build's `spec/`.
