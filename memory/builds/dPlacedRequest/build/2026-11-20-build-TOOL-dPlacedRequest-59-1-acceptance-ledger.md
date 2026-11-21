# TOOL-dPlacedRequest-59 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-59

The unit was built from its spec at rev-7 on base `a6b248b8b`. Built: item S7 alone, the shared
claim-line reader `tools/unattended/unattended.sh#CLAIM_KV_AWK`, which both programs of
`tools/unattended/unattended.sh#read_claims` prepend, and its suite rows in
`tools/unattended/unattended.test.sh#read_kv_row`, with `tools/unattended/unattended.test.sh#slice_fn`
given its variable mode. Every other item is observed by probe or recorded closed, as the spec's
kinds table sorts them. No gate, suite or bar ran in this pass. Every reading below is the
criterion's own command run over the tree, or over a scratch copy or fixture made under the run's
scratch directory, or under `%TEMP%` for the git fixture, and removed after.

**Evidences:** TOOL-dPlacedRequest-59
- AC2 — `version oracle: no prepared merge on HEAD`: the block cut from the fence of the one version oracle, run in spec 55's fixture on the landing with the landing itself as the later base, printed that line alone, exit 2. (DERIVED)
- AC2 — `^1..^2`: with the landing's first parent as the fixture's base, it printed `version oracle: <t8>^1..<t8>^2 · 2 commits` and both version lines, exit 1. (DERIVED)
- AC3 — `fixture's base`: the live sweep over `memory/builds/dPlacedRequest/spec/` printed nothing. (DERIVED)
- AC3 — `a base`: over a scratch copy of the folder, a line-wise `sed` respelling in this spec's AC21 printed nothing too; see Items diverged. (DERIVED)
- AC7 — `CLAIM_KV_AWK='`: the criterion's `grep -nE` over the driver printed one line, `p = index(line, s)`, between `CLAIM_KV_AWK='` and its closing quote line. (DERIVED)
- AC7 — `$CLAIM_KV_AWK`: `read_claims`, cut by the criterion's `awk`, named it twice and held no `/^renews:` line. (DERIVED)
- AC7 — `p = index(s, ": ")`: over a scratch copy of the driver whose walk adds that line, the same `grep -nE` printed two lines. (DERIVED)
- AC7 — `DPR59 AC7`: the rows' lift and helper, cut from the suite and run outside it over the shipped driver, read `live|4`, `live |5`, `|0` three times and `no|2`, six of six passing. (DERIVED)
- AC7 — `DPR46 AC3`: the walk program cut from the base driver and from this one, run over thirteen tip shapes, chose the same beat, never-expires flag and walk status for all thirteen. (DERIVED)
- AC7 — `DPR46 AC3`: the shapes are `yes`, `-`, `no`, `maybe`, no key, bare, one space, two spaces, tab, the duplicate, a tab before `no`, a CR after `-`, and a second `epoch:` line. (DERIVED)
- AC7 — `DPR56 AC22`: the same comparison over a copy keeping the last line of a key differed on two shapes, the duplicate and the second epoch, so the comparison can fail. (DERIVED)
- AC7 — `DPR52 AC25 AC26`: over a copy whose split is staged strict in loose mode it differed on three shapes, bare, tab and tab before `no`. (DERIVED)
- AC7 — `shared reader`: the record read cut from both drivers printed the same row over ten record shapes, CRLF, a tab value, a duplicate key, a missing colon space and a missing key among them; the last-line copy differed on one. (DERIVED)
- AC13 — `git rev-list`: `sec` over 52's `### The oracle` and over 54's `### The oracle's head` each held it zero times. (DERIVED)
- AC13 — `### The oracle's head`: each of the two specs carries exactly one heading its prefix opens, by `grep -c` printing 1 for each. (DERIVED)
- AC13 — `6df7a970`: over 54 at rev-3, `git show 6df7a970:<path>`, the read of the head section held it once. (DERIVED)
- AC13 — `^t=\$\(git rev-list`: the `grep -lE` over the specs neither CLOSED nor WONTDO printed this spec alone. (DERIVED)
- AC18 — `msg="merge: $SLUG — land onto`: `grep -cF` over the lander printed 1, and over a scratch copy whose `msg=` line names another subject it printed 0. (DERIVED)
- AC18 — `"merge: dPlacedRequest — land onto "*`: the section of the one version oracle, read by `sec`, held it once. (DERIVED)
- AC20 — `pr_e0=0; [ ! -f "$pr_hl" ] ||`: the criterion's cut of the race block holds it, and `pr_broke=0; [ ! -f "$pr_hl" ] ||`, at cut lines 44 and 52. (DERIVED)
- AC20 — `$pr_h/once`: the loop's test of it sits at cut line 41, before both. (DERIVED)
- AC21 — `version oracle: the ancestor test failed`: under a stub `git` first on `PATH` whose `merge-base` alone exits 128, the block printed it, exit 2; spec 56's block under the same stub walked the merge, exit 1. (DERIVED)
- AC21 — `version oracle: base does not resolve`: the empty base and `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef` each printed it, exit 2. (DERIVED)
- AC21 — `AC1`: with the real `git`, spec 55's AC1 shapes printed the header ending `· 2 commits` and both version lines, exit 1, and the header alone with no bump, exit 0. (DERIVED)
- AC21 — `AC5`: its AC2 stub printed `the walk failed`, exit 2; its AC3 shapes refused as named, exit 2; its AC4 merge printed `walked no commit of the build`, exit 2; its AC5 header named the merge's range, exit 1. (DERIVED)
- AC21 — `AC6`: under spec 56's AC6 stub, whose `rev-list --count` exits 128, the block printed `version oracle: rev-list failed`, exit 2. (DERIVED)
- AC21 — `[ "$own" = 0 ]`: in that section it sits on line 9 of the read, before `merge-base --is-ancestor` on line 10. (DERIVED)

## Readings beside the criteria

- The bug-class checklist over the pass commit selected `a-helper-extraction-blinds-a-per-function-rule`: no suite arm, gate or tool outside the driver cuts any line the rewire removed, and the arms that call `read_claims` in process source the whole driver, whose sourcing returns well below `CLAIM_KV_AWK`'s assignment. (DERIVED)
- It selected `ledger-token-wrapped-across-a-line-joins-nothing` too: every answer above keeps its token on its own line, and the AC18 token was cut so it ends on no trailing blank. (DERIVED)

- The pass mints the suite helper `read_kv_row` and the awk function `read_kv`; the codebase map was regenerated and its one new symbol staged. (DERIVED)
- The lexicon accepted both names for cell `sh.function`, and neither was defined before. (DERIVED)
- The fixture's stub directories entered `PATH` as POSIX paths, as spec 55's Evidence records. (DERIVED)

## Items diverged

- AC3's red half, as written, does not come out. In this spec's AC21 one `fixture's base` breaks
  across a line, `fixture's` ending one line and `base` opening the next. A line-wise `sed` respells
  the two whole ones, but `crit` joins the bullet, so the joined text still holds `fixture's base`
  and the sweep's exemption hides it: the sweep printed nothing. (DERIVED)
- Respelling the split one too, by a second `sed` turning the line-final `fixture's` into `a`, the
  sweep printed the AC21 bullet, so the sweep itself is live; the criterion's respell needs to read
  joined text, or name every occurrence. (DERIVED)

## Owed at the close

- The unattended suite's reading of the `DPR59 AC7` rows, the two new tips of the `DPR46 AC3` loop
  and the restaged `DPR52 AC25 AC26` and `DPR56 AC22` rows, waived for this landing by README rule
  8 and owed with PLAY-dClosedLoop-14.
- The new arm's RED-first observation: the `DPR59 AC7` rows against scratch driver copies without
  the CR strip, with the loose trim's class cut to a space, and with `CLAIM_KV_AWK` renamed.
- The legs the spec's Gates section names, run once by the main loop.
