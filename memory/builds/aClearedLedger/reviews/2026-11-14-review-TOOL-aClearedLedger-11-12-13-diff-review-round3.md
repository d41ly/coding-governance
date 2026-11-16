**Serves:** diff-review TOOL-aClearedLedger-11 TOOL-aClearedLedger-12 TOOL-aClearedLedger-13

# aClearedLedger — Tier-2 diff review, round 3

*2026-11-14. Subject: the cumulative diff landing on main. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages to read intent from. Lens notes: none supplied, so every lens ran on the kit's generic brief. Checklist: 30 items, acquired by the harness from `--for-diff a54346eead0c..HEAD`, each assigned to exactly one of the 5 lenses (6 each). By design: none supplied, no caller byDesign and a block of 0.*

**Range reviewed: `a54346eead0c83ed4c660b36f3357f45d06dccfc...64673441a3e6698a63af859fdf7b8f9381f580c8`**

**Round: 3.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER, HIGH or MEDIUM. Two LOW items remain, and each has a fix to apply before or after landing. L1: a regex in a spec table row holds unescaped pipes, so a GFM renderer splits the row and truncates the regex (id 1). L2: the gate guard's new read-on test has a `|&` branch that no arm reaches, and the only input that reaches it is a quoted `&`, which the branch misreads as a redirection (id 4).

## Review shape

Intensity full, raw 4, confirmed 2, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.50.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| seams | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

Adjudicated tally by item: 2 items, 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW. By raw confirmed finding: 2 findings, 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW. Every finding keeps its binding grade.

| item | severity | ids | defect |
|---|---|---|---|
| L1 | LOW | 1 | A regex in a spec table cell holds unescaped `\|`, so the rendered row splits |
| L2 | LOW | 4 | The read-on test's `\|&` branch has no arm and misreads a quoted `&` |

## Run integrity

Lenses 5/5 returned, 0 died. Skeptic batches 4/4 returned, 0 died. 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates. Fixes on confirmed findings: 1 judged sound (id 1), 0 judged UNSOUND, 1 judged INSTANCE-ONLY (id 4), 0 none proposed, 0 not judged. Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic. Unverified findings: 0 answered uncertain, 0 with no usable verdict. Refuted findings shown: 2 (ids 2, 3). Same-address pairs shown: 2. Dispositions: unclassed refuse, 30 class slugs handed, 174 leg names read from `tools/gate-legs.json`.

Every count above is zero where a non-zero would mark the run incomplete, so the run is complete.

Neither refuted finding is a twin of a confirmed one. Ids 2 and 3 share address `tools/unattended/gate-guard.js@77894998:402` with id 4, but they concern the `[<>]*` part of the predicate keeping `<>` whole while REDIRECT_RE matches only its `<`. Their skeptics showed that miss was already present at the base. Id 4 concerns the `|&` alternative and a quoted `&`, which is a different defect. No twin is flagged.

The intent lens returned no finding, but it had commit messages only. Its zero does not show that the range has no spec-level intent miss.

## LOW

### L1 — A regex in a spec table cell holds unescaped `|`, so the rendered row splits (id 1)

**Where:** `memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md@b50a3aa9:162`

**What is wrong.** This range adds the spec. Its "Read / Raw words / What it is for" table has a `quoted` row whose code span holds `re.findall(r"(?:[^\s\"']|\"[^\"]*\"|'[^']*'|[\"'])+", command)`. That span contains three unescaped `|`. In a GFM table, a pipe splits a cell even inside a code span unless it is escaped as `\|`.

**Consequence.** The row renders with more cells than the 3-column header, and GFM drops the extra ones. The rendered regex is truncated and the "What it is for" text is lost. Someone who copies the pattern from the rendered table gets a wrong regex. `tools/check-spec-tokens.py` does not read this cell, so no behaviour changes and the damage stays in the document.

**Fix (judged SOUND by the skeptic).** Escape each `|` inside the code span as `\|`, or move the regex into a fenced block below the table and point to it from the cell. Then render the row, or count its cells with a pipe-split probe, to confirm it has three cells.

**Left-shift gate.** A table-shape check in the record lint: every row of a markdown table under `memory/` splits, on unescaped `|`, into exactly the header's cell count, code spans included. Class `pipe-in-a-code-span-splits-a-table-cell`.

### L2 — The read-on test's `|&` branch has no arm and misreads a quoted `&` (id 4)

**Where:** `tools/unattended/gate-guard.js@77894998:402`

**What is wrong.** This range changes `readTokenAt`'s read-on test from `!/^\d+$/` to `!/^(?:\d*|&)[<>]*$/`. An unquoted `&` is a break character at `:400`, so it ends the word before the `>` check runs. `out` can therefore equal `&` only when the `&` was quoted. On `python3 x.py --selftest '&'>x.log`, the reader reads on and builds the one word `&>x.log`. REDIRECT_RE then drops that word as an `&>` redirection. A node probe gave `scanSegments` → `["python3","x.py","--selftest","&>x.log"]` and `scanDenyHits` candidates `["python3","x.py","--selftest"]`. For the control `a>x.log` the candidates keep `a`. Bash passes `&` as an argument here. At the base, the word broke before the `>` because `&` is not all digits.

**Consequence.** No arm of `tools/unattended/gate-guard.test.sh` quotes `&`, so removing or changing the branch fails nothing. On the one input that reaches it, the hook drops a real argument. Row D6 then reads a longer, out-of-scope spelling as the exact leg and denies it. The harm is an over-deny on a contrived spelling. The branch is also unchecked dead weight that the comment presents as part of the REDIRECT_RE prefix.

**Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix below is the skeptic's).** Track whether any quoted character entered `out`, for example with a flag set in the quote branch. Read on past `>` or `<` only while `out` is made entirely of unquoted characters that match `^(?:\d*|&)[<>]*$`. Then `'&'>`, `'>'>` and `'2'>` each end the word, as bash does. Add one `run_planted` arm with a quoted `&` and one with a quoted `>`, each glued before a `>`. The finder's proposal cures the cited instance alone. It removes the `|&` branch so the predicate is `/^\d*[<>]*$/`, or keeps the branch and pins its behaviour on a quoted `&` with one arm. Either way, a quoted `>` or a quoted digit glued before a `>` is still read as an operator.

**Left-shift gate.** The gate-guard suite carries one arm per quoted operator character (`&`, `>`, `<`, a digit) glued before a redirection. `harness arms (fail branches armed or pinned)` counts each alternative of a read-on predicate as a branch that needs an arm. Class `quoted-character-read-as-an-operator` (new).

review-shape kind=diff-review round=3 intensity=full at=synth raw=4 confirmed=2 refuted=2 merged=0 unverified=0 blocker=0 high=0 medium=0 low=2 agents=10 out-tokens=56634
review-round round=3 limit=- prior=- count=0 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md:162 | low | low | confirmed | Line 162 of the spec is in a new file this diff adds. The row's code span holds three unescaped `\|` (between `[^\s\"']`, `\"[^\"]*\"`, `'[^']*'` and `[\"']`). In a GFM table a pipe splits a cell even inside a code span unless it is escaped. The row therefore breaks into more cells than the 3-column header, and GFM drops the extra cells. The rendered regex comes out truncated, and the 'What it is for' text is lost. Only the rendered document is affected: tools/check-spec-tokens.py does not read this cell, so nothing behaves differently. That makes it low. | sound | pipe-in-a-code-span-splits-a-table-cell | class:pipe-in-a-code-span-splits-a-table-cell |
| 2 | correctness | tools/unattended/gate-guard.js@77894998:402 | medium | low | refuted | The defect is pre-existing, so it is out of scope. I loaded the base copy of gate-guard.js (a54346ee) and the head copy and ran scanDenyHits plus checkSuiteLeg on both, with legs=[t/over.py --selftest]. For `python t/over.py --selftest <> f.log`, both versions give the same candidate words [python, t/over.py, --selftest, f.log], and both give checkSuiteLeg false. At base, readTokenAt split `<>` into `<` and `>`. The bare `<` then skipped `>` as its 'target', which left f.log in the words. At head the word stays whole as `<>` and REDIRECT_RE matches only `<`. Either way row D6 allowed this spelling before and after the diff. The diff did not change REDIRECT_RE, and its new read-on test did not introduce the miss or make it reachable. Base also missed `>>` (I observed false at base), and the head fixes that, which is what TOOL-aClearedLedger-12 targeted. The only new thing is that the spec lint's widened REDIRECTION fullmatch now catches `<>` while the hook does not. That makes the lint the stricter of the two, the same direction as the divergences the header already lists. Leaving `<>` off that list is a documentation omission. It is not the D6 allow the finding grades. | sound | - | - |
| 3 | seams | tools/unattended/gate-guard.js@77894998:402 | medium | - | refuted | This is PRE-EXISTING. The diff changed how `<>` is tokenised but not which candidate words come out. I loaded both revisions' gate-guard.js and ran scanSegments and scanDenyHits on `python3 zz/s.py --selftest <> x.log`. At base a54346e the reader broke the word before `>` because the old test was /^\d+$/. The tokens were ["<",">","x.log"]. REDIRECT_RE read `<` as a bare operator, so line 606's j++ skipped the `>` word as its target and `x.log` stayed. The candidate words were ["python3","zz/s.py","--selftest","x.log"]. At head 6467344 the word is now `<>`, REDIRECT_RE matches only `<` of it, and the candidate words are again ["python3","zz/s.py","--selftest","x.log"]. The glued form `<>x.log` gives the same result at both revisions: candidate words [python3, zz/s.py, --selftest]. So row D6 already missed the spaced `<>` spelling at the base, and the hook-versus-lint gap for this spelling was already missing from the base's list of differences. The finding says this diff introduced or exposed it, and that is not the case. | sound | - | - |
| 4 | verification | tools/unattended/gate-guard.js@77894998:402 | low | low | confirmed | This diff introduced the problem. Line 402 used to test `!/^\d+$/` and now tests `!/^(?:\d*\|&)[<>]*$/`. An unquoted `&` is a break character on line 400, so `out` can only be `&` when the `&` was quoted. I loaded the module in node and ran scanSegments on `python3 x.py --selftest '&'>x.log`. It returned ["python3","x.py","--selftest","&>x.log"], and the scanDenyHits candidates came back as ["python3","x.py","--selftest"]. For the control `a>x.log`, the candidates keep `a`. Bash passes `&` as an argument here, so the hook drops a real word. At the base the word broke before the `>`, because `&` is not all digits. No arm of gate-guard.test.sh quotes `&`. The effect is contained: the only harm is that row D6 over-denies a contrived spelling, so I grade it low. | instance | - | new:quoted-character-read-as-an-operator |
