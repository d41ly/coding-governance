**Serves:** research KICK-dKeptSession-19

# Brief — dKeptSession: KICK-dKeptSession-19's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-19's builder (run `wf_eac72422-66e`) returned a DIVERGENCE before any edit. S2, the factory's
last paragraph in section 4, the Inventory and AC4 say the legacy-home list reads its base and writes its file
through S1's helpers, but S1 defines only `check_shrink_list(kit, name, derived, compare)` and `write_shrink_list`:
no read half returns a list's names at the base for `read_base_pairs`, and `write_shrink_list`'s write (the list's
names intersected with the derived set, the whole set seeded only where the list is absent) seeds an empty list from
`build_legacy_repo`'s header-only `legacy-homes.txt`, so the `legacy-homes` cases red and AC5 cannot hold; a typed row
would be dropped instead of corrected. AC4's grep cannot cover the legacy list, and the factory has no argument for
the not-listed finding's wording that S2 and AC2 each spell differently. Revise the spec to the main loop's rulings.

### Items

1. F-helpers: add to the open-questions section, resolved by the main loop at rung 3: S1 and the Inventory name the two lower-level helpers the factory is built from, `read_shrink_base(kit, name, base)` (the list's names at the base, or None where it is absent there) and `write_shrink_file(kit, name, header, names)` (the file write); `check_shrink_list` and `write_shrink_list` are built on them; `read_base_pairs` maps `read_shrink_base`'s names onto its (home, key) pairs and `write_legacy_homes` writes its derived rows through `write_shrink_file`, keeping its own new-home refusal and its seeding and correcting behaviour as at the base, so AC5's four cases read as before. AC4's grep counts those helpers' calls across the three lists. `check_shrink_list` takes the not-listed finding's wording as an argument, so `check_list` keeps its message and the new list says "unnamed and not listed". Run each name through the naming lexicon.
2. F-behaviour: before you return, run or read each criterion's command against the verb it calls and the fixture that seeds it (here `build_legacy_repo` and `lists --write`), and confirm the exit, output and seed each criterion names are the ones the code gives; say what you checked.
3. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap, pin every figure with DERIVED or PINNED, and leave no fork open.

### Acceptance

Spec 19 at a new rev carries the rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-19` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-19's.
