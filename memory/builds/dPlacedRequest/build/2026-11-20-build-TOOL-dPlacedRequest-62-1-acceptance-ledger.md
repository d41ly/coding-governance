# TOOL-dPlacedRequest-62 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-62

The unit was observed from its spec at rev-3 on base `1f1774d4c`. It builds nothing and touches no
product file: every criterion reads the text of specs 59, 61, 54 and 52, frozen at their close,
through the readers `sec`, `bullet` and `entries` cut from the fence of spec 59's
`### The criterion readers` section and sourced unchanged. No gate, suite or bar ran in this pass.
Every reading below is the criterion's own read over the tree, or over a scratch copy made under the
run's scratch directory.

**Evidences:** TOOL-dPlacedRequest-62
- AC1 — `/^##+ /`: the read of `sec 59 '### The criterion readers'` holds it as a fixed string, once. (DERIVED)
- AC1 — `index($0, h) == 1`: the same read holds it as a fixed string, once; a heading no section opens, `### No such heading`, read empty. (DERIVED)
- AC1 — `sec 61 '## 2.'`: the read names `bullet` and `sec` in backticks; a token no section carries read zero through the same read. (DERIVED)
- AC1 — `grep -c "^### The oracle's head"`: over 54 it printed 1. (DERIVED)
- AC1 — `grep -c '^### The oracle'`: over 52 it printed 1. (DERIVED)
- AC1 — `grep -c '^### The one version oracle'`: over 59 it printed 1. (DERIVED)
- AC2 — `### The oracle's head`: `sec` read that section of 54 as its body, not its heading, and `grep -c 'git rev-list'` over it printed 0. (DERIVED)
- AC2 — `git show 6df7a970:<path>`: the scratch copy is 54 at rev-3, and over it the `sec` read's count printed 1 and the `bullet` form's printed 0. (DERIVED)
- AC2 — `bullet`: unit 60 S1's form given that heading printed the heading line alone over the scratch copy, and its count printed 0. (DERIVED)
- AC2 — `6df7a970`: `bullet 59 AC13` names it, and names `sec`. (DERIVED)
- AC3 — `[ "$own" = 0 ]`: in the read of `sec 59 '### The one version oracle'` its first line is line 9. (DERIVED)
- AC3 — `merge-base --is-ancestor`: in the same read its first line is line 10, after the short-circuit. (DERIVED)
- AC3 — `sec 59`: over a scratch copy of 59 with those two lines swapped inside that section alone, the read put the ancestor test on line 9 and the short-circuit on line 10; `bullet 61 AC20` names `sec 59`, and `sec 58` read zero through it. (DERIVED)
- AC4 — `entries 59`: piped to `grep -cE 'TOOL-dPlacedRequest-62\b.*AC13'` it printed 1. (DERIVED)
- AC4 — `entries 61`: piped to the same grep it printed 1, and to `grep -cE 'TOOL-dPlacedRequest-62\b.*AC20'` it printed 1; an `AC77` no entry names printed 0. (DERIVED)
- AC4 — `entries`: over a scratch copy of 61 whose rev-6 entry wraps directly after the id, a line-wise grep of the revision log printed 0 and `entries` piped to the AC13 grep printed 1. (DERIVED)

## Readings beside the criteria

- The rev-6 entry of 61 itself wraps between the id and `to AC13`, so a line-wise grep of 61's revision log for the AC13 pattern prints 0 over the tree while `entries` prints 1. (DERIVED)
- The read of 54's current oracle-head section runs to the next heading and holds prose naming the ancestor and subject tests, so its zero count reads a body, not an empty section. (DERIVED)
- The read of 52's `### The oracle` section holds no `git rev-list` either, as 59's AC13 states. (DERIVED)
- The scratch copy of 54 at rev-3 keeps its `# ` comment line inside the fence within the `sec` read, the line the next-heading-of-any-level closer would stop on. (DERIVED)
- The bug-class checklist over the pass commit selected `fixture-passes-by-finding-nothing`: every zero above is paired with a read of the same population that printed its token, and every hold with an empty heading, label or token, or a scratch copy that reads otherwise. (DERIVED)
- It selected `criterion-asserts-what-its-own-command-cannot-show`: 59's `bullet`, given a heading as its label, matches no bullet line and prints nothing, so its zero over the scratch copy holds whatever the section says; unit 60's form, which opens on the heading, is the read that shows the heading line alone, and it was run beside it. (DERIVED)
- It selected `staged-break-substitutes-a-synthetic-value`: AC3's swap moves the shipped lines, AC4's wrap rewraps the shipped entry, and AC2's copy is the historical blob. (DERIVED)
- It selected `ledger-token-wrapped-across-a-line-joins-nothing`: every answer keeps its tokens on one line. (DERIVED)
- It selected `inline-fence-swallows-the-rest-of-the-file` and `pipe-in-a-code-span-splits-a-table-cell`: this record holds no fence, no table and no pipe. (DERIVED)
- It selected `heredoc-escape-reaches-the-regex`: the probe's two Python steps ran from quoted heredocs with raw-string patterns, and this record was written by the edit tools. (DERIVED)

## Items diverged

None.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec declares no new arm.
