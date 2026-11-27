**Serves:** journal TOOL-dTotalRecall-75
**Caused-by:** TOOL-dTotalRecall-75

# TOOL-dTotalRecall-75 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `8b31081ac` from [2026-11-24-prompt-TOOL-dTotalRecall-75-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-75-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `59c4af40d`.

## Why

Spec rev-3 was buildable as written: S1's re-read found no §B claim made stale by a watched edit, so S2 advanced last-body-change to the full sha of the pass base. last-audit stands, because neither the manifest body nor any watched path moved.

## Summary

C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/guides/SESSION-KICKOFF.md: last-body-change moved from 491dfe31c to 8b31081acce8bec56dfc2bee10555baf29f3251f. No other manifest line changed. The same commit closes the spec and carries the acceptance ledger, the re-rendered indexes and RUN.md.

**Observed by probes** (these stand in for the C9 and C5 conditions of the `kickoff-manifest ratchet` leg; all DERIVED 2026-11-24):
- AC1: the count over the 11 watched paths prints 0 at the tip 59c4af40d; it was 8 over the old value. Unit 69's f7011dd6f is an ancestor of the new value (exit 0); against the old value the same read exits 1. I found f7011dd6f with the AC1 search minus its trailing `$`, because the worktree guard refused my escaped form; it printed one line. (DERIVED 2026-11-24, the pass)
- AC2: W and S are both 408d05723. The 40-hex grep prints 1, and the value is an ancestor of HEAD (exit 0). (DERIVED 2026-11-24, the pass)
- AC3: the staged diff holds only the last-body-change pair, with no line below the manifest-audit block. The commit's Decided trailer names each §B claim re-read and `none corrected`.

**§B re-read:** it covered §4's seven watched commits plus 408d05723, unit 70's. Paths, flags, conf keys and symbols were probed. Claims about what a gate prints were read from its source, because scratch-guard refused my one `encoding_posture.py` call as a gate leg; I did not retry it.

**Reported, not edited:** the 2026-11-10 dated correction on `--rescope --act defer` has met its prune condition. The aSwiftRefusal fixes 3e8557dc6 and 17308b6c3 appear in the log of origin/main and HEAD, and I probed 17308b6c3 as an ancestor of origin/main. This build's watched edits did not cause that, and neither S1 nor §8 F1's grant reaches it, so the entry stands. The ledger and a Decided trailer both say so.

**Owed to the main loop or close:** the checker's own verdict, C9's age condition included, through the pass legs, and §7's `memory hygiene`, `recall floor` and `recall floor arms`. No new arm is owed. I ran no gate, suite or bar; the commit's pre-commit hook ran its own checks, including its kickoff-manifest ratchet, and passed.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` printed 24 anchored and 6 universal classes (DERIVED 2026-11-24). I read them; none needed a change.

With no unit INPROGRESS, the index generator now derives the build's status as DEFERRED. The working tree was clean after the commit. The route card in my context still read unit 75 as DEFERRED; the spec header read INPROGRESS. (DERIVED 2026-11-24, the pass)
