**Serves:** research KICK-dKeptSession-69

# Brief — dKeptSession: KICK-dKeptSession-69's divergence, the two new ledger homes registered

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-69's builder returned a DIVERGENCE before any edit. S5 seeds `memory/project/unnamed-keys.txt` and
`memory/project/unpurposed-namespaces.txt`. Memory hygiene check 3 (`tools/memory-tree/check-memory-hygiene.sh`) admits a
file directly under `memory/project/` only when the kit's named list holds it, or when `PROJECT_REGISTRY_EXTRA` in
`.memory-tree.conf` names it exactly. Neither new name is there, and `.memory-tree.conf` is not in §4's Files touched.
`legacy-homes.txt` went the same route on main (TOOL-dWitnessedBar-20 §8 F7, its member note in `.memory-tree.conf`).

### Items

1. S5 adds the two names to `PROJECT_REGISTRY_EXTRA`, each with a member note in the style of `legacy-homes.txt`'s, and
   `.memory-tree.conf` joins Files touched, tied to S5. Add a criterion, or extend one, that observes check 3 admitting
   both homes.
2. Re-read the rest of S5 for any other path the two new homes or their registrations move, a `.gitattributes`
   `merge=rows` line and govkit's registry included, and list each in Files touched.
3. Bump the spec to rev-2, with one revision-log line naming this brief by its file stem.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-69` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, no spec other than KICK-dKeptSession-69's, and no change to the merge
that is in progress in the run worktree. Read files; edit only the spec.
