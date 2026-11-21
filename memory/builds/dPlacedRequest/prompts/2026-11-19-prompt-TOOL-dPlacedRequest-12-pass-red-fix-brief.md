**Serves:** research TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63

# Brief — dPlacedRequest: the spec-side reds the first pass's legs found

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The pass legs after TOOL-dPlacedRequest-11's commit (`d057ad30d`) read red on facts the spec audit's folds wrote
into unbuilt specs: unpinned size facts, one line-number citation, and revision-log lines citing a review file by a
name that no longer exists. Make the specs carry them in the forms the checks accept, changing no design.

### Items

1. Pinned facts (`python tools/playbook/writing_practice.py check pinned-facts`): a line quoting a number before a unit word carries a pin on that line, an id, a `path:line`, or the word PINNED or DERIVED. Unpinned today: spec 12 `240 bytes` and `241 bytes`; spec 34 `48128 bytes`; spec 43 `1 KiB`, `1 s`, `47885 bytes` and `48128 bytes`; spec 49 `1562 bytes`; spec 60 `47885 bytes` and `48046 bytes`; spec 61 `47885 bytes`; spec 63 `47885 bytes`. Add the pin on each such line: DERIVED for a figure measured from the tree, PINNED for a figure the spec fixes as a rule, or a `path:line` citation where one is the source.
2. The positional citation in spec 13, `tools/run-gates/post-merge.sh@a0462621:13`: rewrite it as a `path#symbol` citation where a symbol names the place, else pin it with `python tools/playbook/positional.py pin <spec> --at 9fdc501aa`, the commit before the first unit moved that file.
3. The stale review-file name: revision-log lines cite `2026-11-19-review-dPlacedRequest-spec-audit-round-1`, a file the main loop renamed. A line the round-1 fold commit `850305e8c` introduced means `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`; a line the round-2 fold commit `909f90db9` introduced means `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`. Decide each by `git log -L` or `git blame` on the line, never by guessing, and rewrite the name. A line neither commit introduced is returned, unchanged.

### Acceptance

`python tools/playbook/writing_practice.py check pinned-facts` and `python tools/playbook/positional.py check` print no red row naming a dPlacedRequest spec, and `git grep -c 2026-11-19-review-dPlacedRequest-spec-audit-round-1 -- memory/builds/dPlacedRequest/spec` prints nothing.

### Gates

The two checks above, the memory hygiene gate (`--only 2,12,25`) and the naming lexicon; no other gate.

### Non-goals

No design change, no new scope item or criterion, no status flip, no commit and no index render. Change no rev and add no revision-log line for these marker edits, unless a hook refuses the edit without one: then bump the rev once per spec and add one §9 line saying the edit pins facts and corrects citations only. Return the per-spec list of lines changed and every check's last line.
