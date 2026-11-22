# TOOL-dWitnessedBar-1 leg-tail 2 — shell hygiene (a location probe asked from a moved directory) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** shell hygiene (a location probe asked from a moved directory)
- **Hash:** 261b10b6b57b5cb2bce7bee7fbcafa51581fba46
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg shell hygiene (a location probe asked from a moved directory) | exit 1
sh-hygiene: location probes — 151 tracked shell source(s) scanned
sh-hygiene:   [GATED] 1 site(s) in 1 file(s) — a location probe asked from a moved directory with no scrub
sh-hygiene:   [scrubbed] 139 site(s) in 66 file(s) — the same probe, first in a substitution opening `(unset GIT_DIR GIT_WORK_TREE;`
sh-hygiene:   [near miss] 31 site(s) in 19 file(s) — `-C <dir> rev-parse` asking the git dir or the common dir
sh-hygiene:   [near miss] 82 site(s) in 69 file(s) — `rev-parse --show-*` with no `-C` and no `cd` — it asks the caller's directory
sh-hygiene:   [near miss] 3 site(s) in 3 file(s) — a comment carrying the gated spelling — it never runs
sh-hygiene: 1 finding(s). With GIT_DIR set and no GIT_WORK_TREE, which git exports into a linked worktree's hooks and merge drivers, git takes the current directory for the top of the work tree, so a probe asked from a moved directory answers about that directory as if it were the root.
  tools/unattended/lib-unattended.sh: the location probe `-C "$here" --show-toplevel` is asked bare and no registry row declares it — scrub each site in place:
    tools/unattended/lib-unattended.sh@9d2e1e71:213: top=$(unset GIT_DIR GIT_WORK_TREE; git -C "$here" rev-parse --show-toplevel 2>/dev/null) || top=$here
```
