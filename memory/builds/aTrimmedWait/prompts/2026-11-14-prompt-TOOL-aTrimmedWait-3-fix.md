# Fix — TOOL-aTrimmedWait-3: an unencoded subprocess call and three literal check-9 spellings

**Serves:** research TOOL-aTrimmedWait-3

## The prompt

The main loop's pass-legs run over 78004fccb..634815f08 reported two red legs, quoted:

> encoding-posture: 1 finding(s) over 155 tracked *.py. Text IO with no encoding= decodes with the platform default, which is cp1251/cp1252 on a Windows node.
>   - [subprocess] `tools/memory-tree/gen_build_index.py#check_staged_write` — subprocess.run(...) has no `encoding=`

> tags: positional · unlisted · help/commit-render.md · HYGIENE check <N> (N = 9) · cite `doc.hygiene#the-check-catalog-all-in-tools-memory-tree-check-memory-hygiene-sh-this-file-is-the-prose-home`, the alias row's tag

The same positional line names `tools/memory-tree/README.md` and this unit's acceptance ledger.

## The brief

### Goal
Clear both reds with no behaviour change. The `git rev-parse --git-path index` call in
`check_staged_write` passes `encoding="utf-8"` beside `text=True`. Each of the three files stops
spelling the literal `HYGIENE check <N>` with a digit: where the text quotes the line the hook
matches, spell it with a placeholder and state N beside it (`HYGIENE check <N> FAILED`, N = 9),
as spec 3 already does; where it refers to the check, cite the tag the positional line names.
Set the header CLOSED again as the last commit.

### Items
1. `check_staged_write`'s subprocess call names its encoding.
2. `help/commit-render.md`, `tools/memory-tree/README.md` and the unit's acceptance ledger spell no
   `HYGIENE check` followed by a digit.
3. The acceptance ledger gains one row for this fix.

### Acceptance
- `grep -nE 'HYGIENE(\.md)?`? check [0-9]' help/commit-render.md tools/memory-tree/README.md` prints nothing.
- The pass's `probe_ws.sh` and `probe_hook.sh` in the scratchpad print what they printed at 634815f08.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals. No registry row: the encoding is fixed at the call, not waived.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
The `encoding="utf-8"` calls already in `tools/memory-tree/gen_build_index.py`, and spec 3's
`HYGIENE check <N> FAILED` spelling.
