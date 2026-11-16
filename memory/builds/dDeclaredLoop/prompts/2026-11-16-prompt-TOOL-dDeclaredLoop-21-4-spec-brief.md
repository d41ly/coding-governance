**Serves:** research TOOL-dDeclaredLoop-21

# Brief: revise spec TOOL-dDeclaredLoop-21 after its second builder return, the refusal census

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The second dispatch of TOOL-dDeclaredLoop-21 returned a divergence before any write: rev-5's §4 "Budgets
and records" says no count rises, but `verb_review`'s `fail 37` is a new census branch while the retired load-time refusal is an
`echo ... exit 2` the census never counted, so the driver's refusal census goes 326 -> 327 against a ceiling of 326. The return
is `memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-21-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md` as rev-6, with one revision-log line naming
that return, so its refusal is graded and its ceiling raise is stated.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write the return's choice as a section 8 fork: (a) keep `verb_review`'s `fail 37`, the ceiling rising 326 -> 327; (b) keep
   the census flat with an echo refusal no arm grades. The run resolves it (a) by the ratify rule, and the decision row
   `TOOL-dDeclaredLoop-21` in `memory/DECISIONS.md` has landed ahead of the pass on the branch: mark the fork RESOLVED (agent,
   2026-11-16, delegated) with (a), and write the body on it.
3. §4 "Budgets and records" states the census move 326 -> 327 PINNED, the decision row, the comment line, and that the
   families stay as the return measured them, the new message spelling no family pattern; §4 Files touched gains
   `.memory-tree.conf` (the REFUSAL_CEILINGS token and its comment line) and the positional registry row that token's
   `path:number` text needs.
4. The return notes `memory/guides/BUILD-METHOD.md` sits 11 bytes under its cap: state the M4 rewording's exact text in §4
   so it fits, or say how it fits.
5. Change nothing else. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec
   file. Do not commit and do not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix
   every hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The return's divergence is answered in the body, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
