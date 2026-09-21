# TOOL-dDerivedDocket-19 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-19

A `may:` grant is honoured from one place, an owner-committed `slug` build README: the driver reads
it in the authorization scan, refuses it under any other mode and refuses a token that is neither a
decision id nor a repo-relative path, and pins it normalised; the leg second-opinions the pin and
walks each run's own commits for one writing a grant into any build README; the backlog verdicts
refuse a `SCOPE` row carrying `may`. No merge bar, no gate leg and no `*.test.sh` suite ran in this
pass. What ran instead, from a scratch root outside the tree:

- the driver-suite block this unit adds, run behind a copy of that suite's own prologue by hand —
  thirty-one assertions, green — and RED under two staged breaks, each on only the arm it targets:
  the S2 refusal keyed on `prompt` alone, and the leading-slash test dropped from the grant grammar;
- the leg-suite block, run the same way over five fixture repositories with bare remotes —
  thirty-three assertions, green — and RED under four staged breaks: the run's range taken with no
  exclusion plus the README read at HEAD, a merge read by its first-parent diff, the run side of a
  merge read from parent order, and the mode arm skipping non-`slug` records;
- the backlog verdicts and the new-build scaffold, called over scratch fixtures by a probe script
  importing the two modules rather than through either selftest.

Found on the way, and fixed in `tools/unattended/unattended.test.sh`: that suite's `mkconf` heredoc
quoted its run helper in backticks, so every conf written after the helper existed ran the driver
into the file and left the tree dirty — every preflight arm after a `reset_tree` was refusing on a
dirty tree. It entered with `TOOL-dDerivedDocket-3` and was invisible because no pass ran the suite.

AC1 and AC9 carry `permission:` lines and get no line here; the orchestrator writes them after the
post-build bar. AC1's hand observation over the scratch fixture pinned
`tools/push-main.sh TOOL-aStandingWrit-1` from a backticked-and-bare `slug` README and `none` from
one declaring nothing.

**Evidences:** TOOL-dDerivedDocket-19
- AC2 — `recipe` — `--preflight` over a `prompt`-mode README carrying `may:` and over a `recipe` one
  carrying `may: none` each refuses under check 78 naming the mode, prints no pin and leaves the
  tree clean. Staged RED: with the refusal keyed on `prompt` alone the `recipe` arm misses it.
- AC3 — `EXMP-aFoo3` — five fixtures, one per negative S3 declares (`EXMP-aFoo3`, a leading `/`, a
  `..` segment, a backslash, `pushmain`), each refuses under check 79 naming its token and writes
  nothing; the backticked and the bare `tools/push-main.sh` both pin `tools/push-main.sh`, and the
  leg's check 19 is silent over records carrying each spelling. Staged RED: with the leading-slash
  test dropped, that fixture pins and its arm misses the refusal.
- AC4 — `may:` — a record whose fact reads `tools/push-main.sh` over a README declaring nothing at
  its recorded BASE reds check 19 naming `[tools/push-main.sh] against [none]`, and still reds after
  the README is edited at HEAD to match. Staged RED: with the README read at HEAD the second arm
  misses it.
- AC5 — `prompt` — a `prompt` record carrying `may: tools/push-main.sh` reds check 19 naming the
  mode and the grant. Staged RED: with the arm skipping non-`slug` records it misses it.
- AC6 — `BASE..HEAD` — over an owner commit on the default branch adding `may:` to one README and a
  run commit adding one to another, check 19 reds naming the run's commit and never the owner's in
  nine gradings: live over a prepared merge, the in-place close on it, a primary landing merge
  unpushed and pushed, a fix commit on the pushed merge, push-main's reconcile over a second owner
  grant another node pushed, and an aborted run's plain reconcile graded live, as the witness and
  under a commit after it. Staged RED three ways: no exclusion, so the owner's grant reds all nine
  and the second one too; a merge read by its first-parent diff, so the owner's grant reds through
  the reconcile and push-main's; and the run side taken from parent order, so the run's own commit
  is excluded in five and the owner's reds in four.
- AC7 — `SCOPE` — a `SCOPE` row carrying `may` with a grant, and one carrying `may none`, each
  returns V13 naming the row and the label; a `SCOPE` row carrying only `accept`, and an ask row
  carrying `may`, return nothing. The same probe over the parent commit's `backlog.py` returns
  nothing for the grant, which is the label admitted.
- AC8 — `may:` — `cmd_new_build` over a fixture ask carrying ``may `tools/push-main.sh` `` wrote its
  README, exit 0, with no `may:` line in the front matter or anywhere else.
- AC10 — `git grep -n "TOOL-dDerivedDocket-19" memory/DECISIONS.md` — one row: a grant is honoured
  only from an owner-committed `slug` build README and lifts veto 2 only.
- AC11 — `git cat-file -s` — at the parent and at the working tree: the protocol pair 59779 to
  59649 B (671 lines, under 61440 B and 750), the build-method pair 27289 and 27264 to 27058 and
  27033 B (under 27648) and 347 to 345 lines. The rule sentence counts 1 in each protocol copy and
  names the owner-committed `slug` README, veto 2 only, and ask-row and `SCOPE`-row clauses; the
  build-method copies count 2 for `protocol §1` where the parent counts 1. `fork-unresolvable`
  counts 1 in the verbs guide, now 15613 B, and `and it may WRAP` counts 1 in `memory/TEMPLATE-SPEC.md`.
