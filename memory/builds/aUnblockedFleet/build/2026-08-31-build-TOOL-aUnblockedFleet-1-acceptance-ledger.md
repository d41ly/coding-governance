# Acceptance ledger — aUnblockedFleet

**Serves:** journal TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5

Node `a`, 2026-08-31. Every observation below was made against the tree at the sha named in its own
line, on this node. Where a criterion was amended rather than observed, the revision that changed it
is named instead.

**Evidences:** TOOL-aUnblockedFleet-1
- AC1 — `bash tools/unattended/unattended.test.sh` — the rewritten arm builds a tracked second
  non-terminal record and asserts the preflight SUCCEEDS: the `same` arm confirms
  `memory/builds/tRun/RUN.md` exists after it, where the previous arm asserted a refusal that wrote
  nothing. PASS, 869 assertions.
- AC2 — `bash tools/unattended/unattended.test.sh` — two `hit` arms name the announcement text and
  the per-record line including phase.
- AC3 — `bash tools/unattended/unattended.test.sh` — the `miss` arm over the zero-competitor fixture.
  Proven non-vacuous by BREAK B below.
- AC4 — `bash tools/unattended/unattended.sh --preflight aUnblockedFleet` — this run's own preflight
  printed `EXCLUDED memory/builds/aThawedCorpus/RUN.md ... LANDING, and its witness 2416de50 is an
  ancestor of the observed anchor 396cd9db`. The exclusion is still armed and still announces itself.
- AC5 — `python3 tools/memory-tree/check-arms.py --check` — green on the bar with no floor edited.
  Measured headroom before the change: `unattended.sh` 175 branches against floor 104, 172 armed
  against floor 101.
- AC6 — `bash tools/unattended/unattended.test.sh` — the guard moved from `-gt 1` to `-ge 1` in the
  same edit as the announcement, so the two thresholds are one line apart and cannot drift silently.

**Evidences:** TOOL-aUnblockedFleet-2
- AC1 — amended rev-4 — withdrawn as unobservable this run; the arm is written in
  `check-unattended.test.sh` and the suite it lives in was withdrawn by the owner. §9 logs it.
- AC2 — amended rev-4 — withdrawn, same cause and same §9 line.
- AC3 — amended rev-4 — withdrawn, same cause and same §9 line.
- AC4 — `grep -c 'EXCLUDED' tools/unattended/check-unattended.sh` — the notice is unchanged code and
  its existing arm is untouched by this diff.
- AC5 — `grep -c 'UNAVAILABLE' tools/unattended/check-unattended.sh` — likewise unchanged; the
  closing diff review re-derived that the exclusion still fails closed on both sides.
- AC6 — `bash tools/run-gates/run-gates.sh` — the full bar on local main after the merge.
- AC7 — amended rev-4 — withdrawn, same cause. The S7 edit itself IS observable and was made:
  `grep -c 'live-run rule below' tools/unattended/check-unattended.sh` returns 0.
- AC8 — amended rev-4 — withdrawn, same cause. The S6 edit was made: check 7's header now opens
  "WHAT IT NO LONGER CHECKS".

**Evidences:** TOOL-aUnblockedFleet-3
- AC1 — `grep -c "At most one run-state file" tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  returned `0` and `0`.
- AC2 — `grep -c "a second run is already live" tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md`
  returned `0` and `0`.
- AC3 — `bash tools/unattended/adopt-unattended.sh --check` printed *in sync (skill rendered from
  template + .unattended.conf)* and exited 0, so the shipped templates and the installed renders agree.
- AC4 — `bash tools/check-kit-versions.sh` exited 0, and `bash tools/unattended/adopt-unattended.sh --check`
  covers all three installed artifacts.
- AC5 — `grep -rho 'gov:kit unattended@[0-9.]*' tools/unattended/ .claude/skills/unattended/ memory/guides/ | sort -u`
  printed exactly one line, `gov:kit unattended@1.13`. It printed TWO on the first attempt —
  `1.12` on four carriers and `1.13` on four — which is precisely the defect round 1's B2 predicted
  and the derived-set criterion is what caught it, at the desk rather than at the bar.
- AC6 — `grep -rn "the bar reds on the second one\|At most one run-state file may be non-terminal\|returns the run to check_single_live" tools/unattended/ .claude/skills/unattended/ memory/guides/`
  returned nothing.

**Evidences:** TOOL-aUnblockedFleet-4
- AC1 — `bash tools/unattended/unattended.test.sh` — PASS, 869 assertions, exit 0.
- AC2 — **NOT OBSERVED. Owner instruction, 2026-08-31: skip the leg suite.** The arms are written
  and committed; nobody has watched them go green. What partial evidence exists: a clean unfiltered
  run on the fixed tree reached ~25 minutes with **zero** occurrences of the awk corruption signature
  that produced nine failures before, so the defect those nine reported is gone. It logged one
  unrelated failure, the `nonexistent.invalid` remote arm, which is timing-sensitive under load. That
  is evidence the CR fix worked; it is NOT evidence this unit's own arms pass. The suite costs ~4h14m
  on this node and is deliberately NOT a merge-bar leg (owner ruling 2026-08-23), so the bar is
  unaffected — but this criterion is unmet and is carried as such rather than inferred green.
- AC3 / AC7 — **BREAK A, staged in the SHIPPED source and observed RED.** The announcement's trigger
  was returned to the inherited `[ "$n" -lt 2 ]`, i.e. fire at two or more. The suite failed with
  exactly two lines and no others:

  ```
  FAIL missing: 1 concurrent unattended run(s) — this run is NOT blocked by them
  FAIL missing: memory/builds/tTwo/RUN.md · phase RUNNING
  ```

  That is H7's scenario reproduced: a driver keeping the inherited trigger is silent in the
  single-competitor case, which is the commonest case this build exists to enable. Unstaged.
- AC5 — **BREAK B, staged in the SHIPPED source and observed RED.** The early return was disabled so
  the announcement fires unconditionally. **BOTH** `miss` arms failed:

  ```
  FAIL unexpected: concurrent unattended run(s)
  FAIL unexpected: concurrent unattended run(s)
  ```

  The second one matters as much as the first: it is the own-record arm, so this break proves neither
  `miss` is the `fixture-passes-by-finding-nothing` class. Unstaged.
- AC6 — `python3 tools/memory-tree/check-arms.py --check` — the spelling `tools/gate-legs.json`
  declares. No pin edited.

**Evidences:** TOOL-aUnblockedFleet-5
- AC1 — `grep -n "TOOL-aFusedCharter-4" memory/backlog/TOOL.md` — row reads `CLOSED` and cites this build.
- AC2 — `grep -n "TOOL-aBoundedVerdict-24" memory/backlog/TOOL.md` — row reads `CLOSED` and cites this build.
- AC3 — `grep -n "TOOL-aReapedTicket-5" memory/backlog/TOOL.md` — row reads `OPEN`, names the
  staleness bound as its remaining scope, and states that its signal is now WEAKER rather than fixed.
- AC4 — `grep -n "TOOL-aUnblockedFleet-7" memory/backlog/TOOL.md` — the marker-race row, `OPEN`,
  naming the shared marker and the `--landed` equality check. A second new row,
  `TOOL-aUnblockedFleet-8`, carries the turnstile problem.
- AC5 — `grep -n "aUnblockedFleet" memory/DECISIONS.md` — two appended rows, not one, and that is an
  amendment: `TOOL-aUnblockedFleet-6`'s retirement is a decision in its own right and folding it into
  the first row would have hidden it. AC5's "exactly one" was written before unit 6 existed.
- AC6 — `bash tools/memory-tree/check-memory-hygiene.sh` — green at the push boundary.

## What was NOT observed, and is not claimed

- **TOOL-aUnblockedFleet-6 has no ledger entry.** It is `WONTDO`; nothing was built and nothing is
  evidenced. Its three refutations are in that spec's §9.
- **No end-to-end test of two runs landing concurrently.** It needs two clones and a real push, it
  would be the only test in this kit doing so, and the lander-marker race it would exercise is out of
  scope by unit 1 §3. `TOOL-aUnblockedFleet-7` carries it.
- **The leg suite was never observed passing** — see unit 4 AC2. Its driver sibling WAS
  (`PASS (869 assertions)`), and both staged breaks went RED exactly where predicted, so the driver
  half of unit 4 is fully evidenced and the leg half is not.
- **The close-time turnstile contention is unmeasured on this fleet.** `TOOL-aUnblockedFleet-8` names
  the measurement a fix needs — the cost of a CONTENDED bar — and nobody has taken it.
