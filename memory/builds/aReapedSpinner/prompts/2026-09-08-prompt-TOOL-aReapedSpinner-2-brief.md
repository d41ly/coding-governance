# Brief — TOOL-aReapedSpinner-2, the scope fence

**Serves:** journal TOOL-aReapedSpinner-2

What this pass was handed: the unit's spec at rev-4, three spec audits whose findings D9, D11, D16,
D17, D19, D20 and D34 all landed on this one predicate, and the union-graph measurement record.

What it builds: `scope.py` — `derive_scope(rows, roots, self_chain)` returning the in-scope SET,
plus `--explain` and `--check-conf`, and sixteen arms.

The four things that are not obvious, each from a finding rather than a preference:

- **Attribution is a TREE CLOSURE, not a per-row predicate.** A leaf's argv names nothing and a leg
  shell carries a relative path, so per-row attribution refused every real tree. Closure admits
  them by ancestry.
- **Self-chain rows ARE in scope and MAY be roots.** Barring them empties the set in the shape the
  kit ships into, because the session shell is both the only attributable root and a chain member.
  "Ours" and "killable" are two questions.
- **Every `NAME=value` is stripped wherever it appears, including inside a `-c` body.** Every agent
  shell here carries `export TEMP=` in its argv, and matching the raw string admits every session
  on the machine.
- **`msys_ppid` is translated to a winpid before the union**, and an edge whose child predates its
  claimed parent is dropped. The two graphs disagree on 7 of 330 rows.
