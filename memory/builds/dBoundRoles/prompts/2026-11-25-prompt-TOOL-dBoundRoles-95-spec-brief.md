**Serves:** journal TOOL-dBoundRoles-95

# Brief — dBoundRoles: TOOL-dBoundRoles-95, the policy guard admits no live run's own write of the policy file

## The prompt

> Unit 23 F6: "Close it before landing".

— the owner's words on 2026-11-25, as the session that started this run quoted them, forwarded here; no answer was typed
in this session. That session's own words on what the choice means, not the owner's: "The guard is fixed before dBoundRoles lands.
Adds a unit and delays the landing." The question answered is the decision row `TOOL-dBoundRoles-23 F6` of
`memory/builds/dBoundRoles/RUN.md`: "should tools/policy/guard.py stop admitting a live run's own change to the policy file under
policy-file.guard = owner-only, so a run's write can never pass as the owner's?"

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-95.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-25, node a,
base `735060358`, `streams tooling`, and the tail `order 48`. It binds by `**Derived:** PLAY-dClosedLoop-2`, the line
this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is a security surface: write it as substantive.

### The gap

`check_run_mandate` of `tools/policy/guard.py` admits any guarded path on the run-branch of a live run, the policy file among
them, whatever `policy-file.guard` reads. TOOL-dBoundRoles-23 admits a below-medium effort level in the policy file only under
`owner-only`, as the owner's explicit write (its §8 F3 and F6, option (e) taken, the run admission left as a named gap). So a
run can commit such a level on its own branch, and it lands as the owner's.

### Items

1. Probe at HEAD that the gap holds: in a scratch repository under `%TEMP%`, a live run's branch, a staged policy-file change
   alone, `guard.py --staged` and the loop kit's `guard.py --staged` each exit 0.
2. The property, to state and grade: under `policy-file.guard = owner-only`, read at the landed revision and never the staged
   file, no agent commit of a live run changes `.governance/policy.toml` except in a shape that is no write of the owner's, the one
   raised cap, and a merge taking a parent's blob whole. The change may not be reached by staging the policy file with
   other guarded paths, by deleting, retyping, renaming or adding it, by a merge that writes a new blob, or by
   `policy-file.guard` itself switched in the same commit or an earlier one of the run. Every other guarded path of
   `tools/policy/guarded-paths.txt` keeps the run admission of PLAY-dOrderedCharter-84, the owner's 2026-11-12 ruling, which the
   answer above narrows for the policy file alone; say so and edit no other build's spec.
3. The two other values of `policy-file.guard`, `agents-with-reason` and `agents-within-mandate`, were not asked about: each keeps
   admitting what it admits on a live run's branch today, its records owed as today. The minimal guard imports no policy
   reader and runs alone where no loop kit is installed; settle by M3 where the value is read, in one place, with
   `tools/loop/guard.py` as the wrapper that already resolves it. `agents-within-mandate` and `owner-only` stop admitting one
   set; name each text and fixture that says they admit the same.
4. The wrappers and doors: `tools/loop/guard.py` (its guard-self step and its owner-only step both call `check_run_mandate` for
   leaves of the policy file), and `tools/loop/policy_edit.py set` on a live run's branch, whose proof line reads `none — run mandate`.
   Under `owner-only` neither may write or admit what the minimal guard refuses, and each refusal names the owner's terminal
   commit as the remedy. Read every other caller of `check_run_mandate` and every upgrade step that writes the policy file
   (`git grep -l policy.toml -- tools/govkit/steps`); name on a **Readers:** line what each sees after. A run whose landing
   step writes the policy file then hands that commit to the owner: state the consequence, and that
   gov's own policy file holds no key the steps of this build write (verify it, do not take it from here).
5. The push arm of `tools/loop/guard.py` and the merge bar's own reading of the policy file are unchanged unless the probe shows
   one certifies a run's write as the owner's; say which.
6. §6: RED-first arms, each naming the command that observes it and the break that reds it: `guard-run-live` in the policy
   fixtures split so the policy file refuses and another guarded path still admits, in either `run-branch` spelling; the
   loop guard's `owner-only-live` case refusing and `mandate-live` still admitting with its records; a run that switched
   `policy-file.guard` in an earlier commit of its branch, still judged by the landed value; the `policy_edit.py` `set-run-live` case;
   a merge that writes a new policy blob; the cap raise and the parent-side merge still admitted, as near misses. Each arm is
   seen red on its named break by the main loop after the build. Floors and budget rows move in one place each.
7. Docs: `help/policy.md`, `help/roles.md`, `help/verdict-backends.md` where they say it, `tools/policy/README.md`, `tools/loop/README.md`,
   `tools/roles/README.md`, the two guards' headers, and the clause of `.githooks/pre-commit` if it says so. TOOL-dBoundRoles-23 is CLOSED
   and frozen: its named gap is restated in ONE deviation record of this unit, never in its text.
8. §3 Edges: no **hands-off** or **consumes-from** bullet naming another unit of this build, since each is CLOSED and
   frozen; `external` bullets stay allowed.
9. Resolve every fork by M3 as a delegated agent resolution, with `options`, `pick`, `admitted-by`, `widens:` and
   `relaxes:`. A fork that M3's vetoes refuse, or one that would widen what any agent may write, is left open and
   returned as such: the main loop asks the owner.
10. §10 reuse audit, with `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and a recall query, each named.
11. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count on its own line; never set
    a number before a counted noun in prose, and never write a section number beside one.
12. Files touched names every file, each `help/` page a changed verb or fixture documents included; §7 lists every leg
    Files touched trips (`python tools/check-spec-tokens.py --list` prints them), one `New arm:` line per new arm.
13. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-95.md` and
    `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-95.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. No change to `tools/memory-tree/routed_commits.py`,
`tools/loop/position.py` or anything on `origin/main`: two other sessions change those.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-95.md` alone. Work at HEAD of this worktree; do not merge or read another branch.

### Reuse

`check_run_mandate`, `check_parent_sides`, `check_raise_shape` and the fixture scenarios of both guards.
