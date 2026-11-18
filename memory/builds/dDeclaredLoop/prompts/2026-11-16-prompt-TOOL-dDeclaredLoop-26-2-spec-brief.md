**Serves:** research TOOL-dDeclaredLoop-26

# Brief: revise spec TOOL-dDeclaredLoop-26 after its first builder return

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-26 returned a divergence before any write, naming four places rev-5
does not hold over the tree as built: Files touched leaves out the loop dossier's claim, the generated map files and
`tools/loop/README.md`; position reads through `loop_items.py#read_composed_items` since unit 29, not `read_composition`; the
tag resolver `gov_tag.py` reads the tag index of the tree it sits in, not its working directory, and the scratch's branch is not
`main`; and the plants' commit C1 is not the pin AC1 expects. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-26-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-26.md` as rev-6, with one revision-log line naming
that return, so every finding in it is answered and every acceptance criterion can be observed over the tree as built.

### Items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Finding 1: add `memory/map/features/loop.md` (its gate-legs claim for `loop composition fixtures`), the four
   `memory/map/generated/` files and `tools/loop/README.md` to Files touched and to §5.
3. Finding 2: re-ground §1 and S3 on `read_composed_items`. Write the choice as a section 8 fork: (a) `read_composed_items`
   takes a revision routed through `read_composition_at`, adding `tools/loop/loop_items.py` to Files touched; (b) position.py
   copies the mapping. Recommend by the ratify rule (the [reuse] practice weighs against (b)) and write the body on it.
4. Finding 3: S4 and §4 "The carry" find the tag resolver under the repository being read, and §4 "The plants" names the
   scratch's branch `main` or sets `GOV_DEFAULT_BRANCH`; take the one the return's probe showed working, and say why.
5. Finding 4: name the commit AC1's pin is, so the plant and AC1 agree with how `write_transition` commits each move.
6. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. Each Readers half sits on one line.
7. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Each of the return's four findings is answered in the body, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
