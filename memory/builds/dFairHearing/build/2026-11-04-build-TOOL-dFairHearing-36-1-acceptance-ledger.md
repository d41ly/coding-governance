# Acceptance ledger — TOOL-dFairHearing-36

**Serves:** journal TOOL-dFairHearing-36

Built against spec rev-5 at pass commit `e69ecfcf0`. The main loop drafted this ledger at the close from
the builder return of that commit. Each criterion was observed at its parent `631666c3f`, and the commit
holds only the spec's status flip and the renders it forces. `census.py`, `members.py` and `base.py` are
the spec's scripts, written under the pass's scratch directory. The pass before it, at rev-4, was
refused at dispatch on AC3's spelling and committed nothing. No suite, gate or bar ran in the pass. The
spec's legs and the RED-first observation of its two `New arm:` lines are owed to the close.

**Evidences:** TOOL-dFairHearing-36
- AC1 — `python members.py 3708a705` — over the live hook and pack suites it printed 5 `member` lines and nothing else and exited 0. With the :874 arm pasted twice it printed that label's `twice` line and exited 1
- AC2 — `census.py` — a copy expecting `(60, 14)` printed `population 59 14` and `census: the population is not 59 and 14`, and exited 1
- AC3 — `census.py` — as rev-5 words it: base's hook suite, as `git show 3708a705:` prints it, was written to scratch and given as every suite path. Under both `PYTHONUTF8=1` and `PYTHONUTF8=0` the census printed 73 `gone` lines and `members.py` printed 5, with no `Traceback`
- AC4 — `census.py 3708a705` — restoring the :1063 arm printed its `gone` line, cutting the :874 arm printed its `home` line, and cutting the `rule5: the Map ban fires` arm printed its `home` line, and each exited 1. Over the live suites the census exited 0
- AC5 — `members.py` — a copy with 864 in place of 874 printed `not a member :864` and exited 1, with no `Traceback`
- AC6 — `git ls-files` — `precondition` evidence: it listed `tools/lib/extract-arms.sh` alone, and the grep for `PASS (N assertions)` printed 2. Unit 40's ledger, on its AC14 line, shows the criterion held at this unit's parent, so it observes no change of this unit
- AC7 — `spec-audit opt-in pack self-test` — `tools/gate-legs.json:781` holds the leg, running `{prefix}/workflows/spec-audit-optin.test.sh`
- AC8 — `python base.py .` — with `GATE_BASE` unset it printed `base 8bec4cefd957… from merge-base of HEAD and origin/main`, which equals `git merge-base HEAD origin/main`. In the `%TEMP%/fgb` clone, whose `HEAD` equals its `origin/main`, it exited 2 with no `base` line. With `GATE_BASE=origin/side`, a commit that is no ancestor of `HEAD`, it printed side's sha `f9a966d4`, not the merge-base `ae5933b5`. `merge-base` appears 0 times in `base.py`, and the fixtures under `%TEMP%/fga` and `%TEMP%/fgb` were removed
