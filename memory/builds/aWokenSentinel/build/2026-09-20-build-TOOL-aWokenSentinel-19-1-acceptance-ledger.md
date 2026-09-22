# TOOL-aWokenSentinel-19 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-19

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite, and the adopter suite itself was not run — the pin is authored from the static count and the
close's `run-unattended-gates.sh` run is its named observer, as spec 19 S2 and spec 14 AC5 say. The
pass verified with the direct checks the spec's section 6 names: the greps of AC1, AC3 and AC4 over
the tip and over the file at `12513c25`; the floor block extracted with `sed -n` and evaluated by
`bash -c` on both sides of the pin for AC2; the structural arm's one line extracted the same way and
run by `bash -c '<line>' <path>` over the tip and over a scratch copy with `echo stranded` appended
after its exit for AC5, plus a near-miss copy with a blank and a comment appended, which the arm
correctly ignores; `bash -n` over the suite; and a `cat -A` probe over the diff for CR bytes. Those
stand in for the `unattended kit gate`, `memory hygiene`, `spec tokens`, `install-prefix (shipped
surface)` and `lexicon naming predicates` legs, which run once at the close. No spec fold was owed:
S3's fold of spec 14 had already landed as that spec's rev-3 and rev-4 at the audit disposal, and
AC3's three greps hold on it unchanged, so spec 14 is not in this pass's write set. The one design
addition beyond the spec's block text is a sentence in the pin's comment recording that the inline
`n=$((n+1))` sites are outside the static count, which makes the count a lower bound; it changes no
mechanism and the spec's rev stays at 2.

**Evidences:** TOOL-aWokenSentinel-19
- AC1 — `grep -cE '^\s*(same|hit|miss|absent|present) ' tools/unattended/adopt-unattended.test.sh` printed `87` at the tip and `sed -n 's/^FLOOR_ASSERTIONS=//p'` over the same file printed `78`, which is `c * 9 / 10` exactly (783 / 10 rounded down) and above 0; over `git show 12513c25:tools/unattended/adopt-unattended.test.sh` the sed printed nothing and the grep printed `72`, the figure the spec pinned at base, moved by units 3 and 4 as the spec expected. OBSERVED.
- AC2 — the floor block extracted with `sed -n '/^FLOOR_ASSERTIONS=/,/^\[ "\$n" -ge "\$FLOOR_ASSERTIONS" \]/p'` (two lines) and run by `bash -c` with `n=77` and `st=0` printed `FAIL executed 77 assertions against a floor of 78 — arms are UNREACHABLE rather than absent` and left `st=1`; with `n=78` it printed nothing and `st` stayed `0`. OBSERVED; the suite's own green under this pin is observed at --close.
- AC3 — `grep -c 'run-unattended-gates' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md` printed `2`, `grep -c 'reads no change'` over the same file printed `0`, and `grep -c 'per-suite log'` over the same file printed `0`, all over spec 14 at rev-4 as committed before this pass, so S3's fold was already discharged by the audit disposal's sibling fold and this pass changed nothing in spec 14. OBSERVED.
- AC4 — `grep -c 'FLOOR_ASSERTIONS' tools/unattended/adopt-unattended.test.sh` printed `3` at the tip (the comment's first line, the pin and the compare) and `0` over the file at `12513c25`; `grep -c 'static count' tools/unattended/adopt-unattended.test.sh` printed `2` at the tip (the authoring rule and the lower-bound sentence, both in the pin's comment) and `0` at base. OBSERVED.
- AC5 — the structural arm's line extracted with `sed -n` and run by `bash -c '<line>' <path>` with `st=0` and `$0` bound to `tools/unattended/adopt-unattended.test.sh` printed nothing and `st` stayed `0`; with `$0` bound to a scratchpad copy of the suite with `echo stranded` appended after its `exit "$st"` it printed `FAIL a line follows the terminal exit and can never run` and left `st=1`; and `sed -n '/^exit "\$st"$/,$p' tools/unattended/adopt-unattended.test.sh | grep -cvE '^\s*(#|$)'` printed exactly `1` at the tip. Near-miss: a copy with a blank line and a comment appended after the exit read `st=0`, so the arm counts only executable lines. The same predicate run over every `*.test.sh` in `tools/unattended/` and `tools/workflows/` that ends `exit "$st"` printed `1` for each of the five that do (adopt-unattended, check-playbook, check-unattended, cross-component, unattended), so the kit carries no stranded arm today and the predicate reds no innocent suite; the ten suites ending another way are the kit-wide loop's, handed off per §3. OBSERVED.
- checkers — `bash -n tools/unattended/adopt-unattended.test.sh` exited 0; `git diff -- tools/unattended/adopt-unattended.test.sh | cat -A | grep -c '\^M'` printed `0`. OBSERVED; the legs are observed at --close.
