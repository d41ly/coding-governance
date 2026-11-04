# dOrderedCharter — unit 53's builder return

**Serves:** journal PLAY-dOrderedCharter-53

Run wf_cce2cd82-5ff, summarized from its return.

- Built at rev-2 as pass commit `9f6710021`.
- `tools/playbook/positional.py` gains `read_line_commits`.
  - It runs one working-tree `git blame --porcelain -M` per record and names no revision, so an uncommitted line reads
    as the all-zero sha.
  - A failed blame is a refusal.
- `read_grandfathered` now keys on each line that holds the reference. A row is grandfathered only when every such line
  was written by a commit outside the check's descendant set, and the all-zero sha counts as inside it.
- The print reads `written in <sha8>`.
- `gov_tag.py` gains three plants, `positional-edited-after`, `positional-renamed-after` and `positional-uncommitted`.
  They share `write_forked_record`, extracted from unit 47's plant.
- The playbook README states the per-line rule.
- Observed by probe:
  - AC1: edited-after exits 1, with the appended citation unlisted.
  - AC2: renamed-after exits 0, grandfathered.
  - AC3: uncommitted exits 1.
  - Unit 47's forked-before still holds.
  - A probe of `read_line_commits` returns a full sha for every line of the module, and refuses a missing path.
- No divergence.
- Owed at the close:
  - RED then GREEN for the `New arm:` line on `positional.py`.
  - `positional.py --selftest` over every positional row.
  - The section-7 legs.
