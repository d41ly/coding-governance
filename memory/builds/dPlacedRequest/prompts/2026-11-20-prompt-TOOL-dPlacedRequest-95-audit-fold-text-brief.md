**Serves:** research TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99

# Brief — dPlacedRequest: the spec audit's folds, pinned and cited by tag

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The spec audit of units 95 to 99 folded its findings into those specs at rev-2, and the folded text fails two
writing checks the merge bar runs: the plain pinned-facts check reads nine durations in specs 95, 98 and 99 with no
mark on their own line, and the positional check reads seven bare build-method section citations in the same three
specs. Correct both; change nothing else.

### Items

1. In specs `TOOL-dPlacedRequest-95`, `TOOL-dPlacedRequest-98` and `TOOL-dPlacedRequest-99`, every line carrying one of the durations `python tools/playbook/writing_practice.py check pinned-facts` names gets PINNED or DERIVED on that same line (DERIVED where the figure is computed from others in the spec), or is reflowed so the figure and its mark share a line.
2. In the same three specs, every bare build-method section citation `python tools/playbook/positional.py check` names is replaced by the alias tag the check prints for it: `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` or `doc.build-method#m6-passes-commits-parallelism`.
3. These are editorial corrections inside the audit's own disposal: keep each spec at rev-2 and add no revision-log line beyond one naming this brief.

### Acceptance

A plain `python tools/playbook/writing_practice.py check pinned-facts` and `python tools/playbook/positional.py check`
report no red for the three specs, and `check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over
each report nothing.

### Gates

The pinned-facts check, the positional check, the memory hygiene gate (`--only 12,25 --spec`) and the spec-token
checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip, no other line and no other spec. Never quote a check's
hit literally in prose.
