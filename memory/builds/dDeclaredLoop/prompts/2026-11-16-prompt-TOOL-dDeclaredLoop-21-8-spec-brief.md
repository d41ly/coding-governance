**Serves:** research TOOL-dDeclaredLoop-21

# Brief: revise spec TOOL-dDeclaredLoop-21 after its fourth builder return, with a builder's sweep before it returns

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The fourth dispatch of TOOL-dDeclaredLoop-21 returned a divergence before any write, naming two design gaps
in rev-7: S8 and AC8 re-point `tools/govkit/steps/fanout_cap.py`, the program of the landed upgrade step
`agent-cap/fanout-cap-to-agents-in-flight`, which `tools/govkit/upgrade_steps.py#check_frozen` reds for any byte change; and §4
"How the shell reads it" names no reading where `review_bounds.py` or the policy kit does not resolve beside the driver, while
about 46 `--review` calls in `tools/unattended/unattended.test.sh` run on `write_switch_fixture` trees with no loop kit, no remote
and a bound of 1. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return.md`. Each of the four returns so far
found gaps the revision before it did not probe.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md` as rev-8, with one revision-log line naming
that return, so a builder can build it as written over HEAD with no further divergence.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read all
   four returns whole: `build/2026-11-16-build-TOOL-dDeclaredLoop-21-1-builder-return.md` to `-4-`.
2. Write each gap as a section 8 fork with the return's options, marked RESOLVED (agent, 2026-11-16, delegated) on the run's
   pick, and write the body on it:
   - the frozen step: (a) `fanout_cap.py` stays byte-identical, `conf_to_policy.py` has `review_rounds.py` as its one caller,
     and AC8 drops its import clause, the second caller left to a later step row; this needs no owner turn.
   - the absent module or policy kit: the driver reads the four catalogue defaults with a NOTE, as
     `tools/unattended/unattended.sh#read_spec_audit_switch` does with its `SPEC_AUDIT_*_DEFAULT` constants, so §4's
     no-shell-copy wording admits those four constants; the `write_switch_fixture` population then reads spec bound 1 with no
     edit, and no census site is added. State the census after the change.
3. THE SWEEP, before you return: for every function, file, constant and fixture the revised body changes or removes, find
   every caller, reader, fixture, suite arm, frozen or pinned contract (upgrade step rows, subject pins, verdict-epoch
   delegates, census and family ceilings, size caps, the lexicon pin) and every test population that runs it, at the branch
   tip, and say in §5 what keeps each green. Record the sweep's population and its counts in §5. A builder will re-run it.
4. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec, on the branch's tree as the last
   writer did, and fix every hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Both gaps are answered in the body, §5 carries the sweep, and the spec-token checker reports no unwaived hit on the branch.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
