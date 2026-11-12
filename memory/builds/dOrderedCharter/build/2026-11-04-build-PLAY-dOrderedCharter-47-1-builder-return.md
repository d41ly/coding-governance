# dOrderedCharter — unit 47's builder return

**Serves:** journal PLAY-dOrderedCharter-47

Run wf_7bee3c71-9bc, summarized from its return.

- Built at rev-3 as pass commit `db1119c7e`.
  - `tools/playbook/positional.py` gains `read_grandfathered`. It finds the commit that added the check, through
    `tree_lib.read_adding_commits`, and grades an unlisted citation as print-only. That applies only in a build record
    whose adding commit does not descend from that commit.
  - The summary line counts grandfathered rows apart from unlisted ones.
  - `tools/playbook/gov_tag.py` gains the plant `positional-forked-before` and four selftest rows.
  - `tools/playbook/README.md` gains one sentence.
- Observed by probe:
  - AC1: the check's adding commit is `fe22fcf80`, and the tree reads 0 unlisted and 0 grandfathered.
  - AC2 and AC3: the plant exits 0. Both failing cases were seen by patching the function: base rule, and every path
    grandfathered.
- No divergence. This is the first unit built from a spec the drift sweep folded.
- Owed at the close:
  - RED then GREEN for the `New arm:` line on `positional.py`, inside unit 26's `tags positional selftest` leg.
  - The spec's own section-7 legs.
