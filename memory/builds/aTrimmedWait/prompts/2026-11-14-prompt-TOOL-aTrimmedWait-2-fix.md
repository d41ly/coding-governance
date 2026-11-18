# Fix — TOOL-aTrimmedWait-2: the scoped selection's loop is fed by a here-string

**Serves:** research TOOL-aTrimmedWait-2

## The prompt

The main loop's pass-legs run over 72ad7a950..91e91ed35 reported one red, quoted:

> sh-hygiene: 1 finding(s). A `while … done` fed by a heredoc or here-string whose body holds a command substitution reads until EOF, and EOF can never arrive.
>   tools/memory-tree/check-memory-hygiene.sh: the registry declares 8 site(s) at `<<<` and the scan measures 9 — the count may fall with the sites and may not rise

The ninth site is the pass's own line in the `--build` arm of the scoped selection:
`while IFS= read -r _l; do [ -z "$_l" ] || STAGED_SET["$_l"]=1; done <<<"$FILES"`, where `FILES` is
assigned from a command substitution one line above.

## The brief

### Goal
Feed that loop without a here-string, so the shell-hygiene leg's count for the file returns to the
registry's 8 and the scoped selection reads exactly the same paths. The house form is a process
substitution: `done < <(printf '%s\n' "$FILES")`. Change nothing else, keep the verdicts the pass's
probe and unchanged-verdict fixture observed, and set the header CLOSED again as the last commit.

### Items
1. The `--build` arm's loop reads `FILES` through a process substitution, not `<<<`.
2. The pass's `u2.sh` probe (rev-4) prints the same AC1 to AC3 lines as at 91e91ed35.
3. The acceptance ledger gains one row for this fix.

### Acceptance
- `grep -c '<<<' tools/memory-tree/check-memory-hygiene.sh` falls from 28 to 27: only the loop site leaves. DERIVED from the file at 911f4371b
- The scratchpad probe `u2.sh` prints its AC lines unchanged.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals. No registry change: the count goes back down, never up.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
The `done < <(...)` loops already in `tools/memory-tree/check-memory-hygiene.sh`.
