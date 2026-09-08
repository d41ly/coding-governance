# Brief — TOOL-aReapedSpinner-3, the classifier

**Serves:** journal TOOL-aReapedSpinner-3

What this pass was handed: the unit's spec at rev-4, the D18 and D32 findings — which are mirror
images of one another and both landed on this predicate — and the union-graph record's measured
parentless population.

What it builds: `classify.py`, a five-member closed vocabulary and a `--report`, plus nine arms.

The three things that are not obvious:

- **`msys_ppid` participates in NEITHER predicate.** Reading its absence as a dead parent grades
  every native row ORPHAN (D18); reading it as PARENT-UNKNOWN grades every native row UNKNOWN and
  makes `reap-orphans` inert (D32). The parent question is `win_ppid`'s, which has no sentinel.
- **PARENTLESS is a label, never a licence.** 24 of 337 rows here are parentless and 18 are over an
  hour old, including explorer and csrss. Only the fence separates those from a real orphan.
- **The coverage arm demands a PRODUCING fixture per member**, not a member count. rev-3 carried an
  `OVERAGE` member nothing could emit and its closed-set arm passed on the spelling of the enum.
