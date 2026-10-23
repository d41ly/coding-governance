# TOOL-dFairHearing-26 — every rule 0 and rule 5 arm of the hook's suite found at its new home and gone from the old one, counted by label whatever helper writes it

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 20 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-26-deviation-261.md](../build/2026-10-23-build-TOOL-dFairHearing-26-deviation-261.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-27 |
| [2026-10-23-prompt-TOOL-dFairHearing-26-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-26-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 20 to 23, finding id 10 (item H2, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`), is
closed. `TOOL-dFairHearing-23` AC9 builds its label population with `^check(_spec_audit)? "rule[05]:`,
so it misses 10 rule-5 arms written with the `js` and `jso` helpers, the loop-printed `rule0: pair`
and `rule0: fold` arms, and the indented MSYS-mount arm. Its pinned "4 for rule 5" is the regex's
count, not the number of arms. This spec measures a further miss: 28 rule-0 arms labelled
`rule0/U7:`, `rule0/aWardedAudit:` and `rule0/aWardedAudit-6:`, which the report's own corrected regex
`"rule[05]:` misses too, because a `/` comes before the colon. This unit takes the census from every
label, holds each one at its receiving suite and gone from the hook's suite, moves any arm the move
left behind, and is shown red on a planted miss before its count is trusted.

## 2. Scope (IN)

- **S1** — The census population, derived from base `3708a705`'s `tools/hooks/agent-cap.test.sh` by
  §4's command: every quoted label whose rule tag is `rule0` or `rule5`, with or without a `/<tag>`
  qualifier, an escaped `\"` inside it kept, whatever helper or indentation it sits under. The two
  loop-printed arms enter as the named labels `rule0: pair` and `rule0: fold`. Observed by AC1.
- **S2** — The move, completed. At this unit's commit, each rule-0 label is spelled in
  `tools/workflows/spec-audit-optin.test.sh` (the pack's suite) and each rule-5 label in
  `tools/workflows/check-review-join.test.sh` (the join suite), byte for byte, each run against the
  rule's new home with its base verdict. None of the population is spelled in
  `tools/hooks/agent-cap.test.sh` (the hook's suite). An arm units 16 and 23 left in the hook's suite,
  or did not land at its home, is moved by this unit. Observed by AC2.
- **S3** — The census refuses a planted miss before its count is trusted: one `js "rule5:"` arm left
  in a scratch copy of the hook's suite, one rule-5 arm cut from a scratch copy of its receiving suite,
  and the `rule0: fold` loop cut from a scratch copy of the pack's suite. Each is named. Observed by
  AC3.
- **S4** — Supersession. This unit's AC1 to AC3 answer the label half of `TOOL-dFairHearing-23` AC9,
  which unit 23's acceptance ledger records as superseded here. AC9's marker-count half, over
  `gov:fixed-verifiers` and `gov:sequential-agents`, stands. NOT OBSERVED by a criterion of this
  unit: it is a ledger entry in unit 23's record, read there.

## 3. Non-goals (OUT)

- No rule 2 arm: AC9's marker-count half is not part of this finding and stays unit 23's.
- No change to what any moved arm asserts. A moved arm keeps its label, its payload and its expected
  verdict. Only the helper that runs it may change, to reach the rule's new home.
- No permanent census arm in a suite. The move happens once, and a guard against an arm returning
  to the hook's suite guards nothing anybody does (§8 F1).
- No new gate leg, and no help page: `help/` covers no suite.

### Edges

- **consumes-from** `TOOL-dFairHearing-16` — the receiving suites and the rules' new homes the moved arms run against; without them there is nowhere to move an arm
- **consumes-from** `TOOL-dFairHearing-23` — AC9, whose label half this unit's census replaces, and the arms that unit moves

## 4. Design

### Evidence

Measured at `3708a705` on 2026-10-23, PINNED.

- `tools/hooks/agent-cap.test.sh` defines `check` (:126), `js` (:137), `jso` (:322) and
  `check_spec_audit` (:795). The rule-5 arms are 4 `check` arms (:299-310), 8 `js` arms and 2 `jso`
  arms (:334-376).
- The rule-0 arms are 24 `rule0:` labels, one of them indented under a platform guard (:944), and one
  holding an escaped quote, `kind [\"spec-audit\"] (an array)` (:874). Beside them sit 10 `rule0/U7:`,
  10 `rule0/aWardedAudit:` and 8 `rule0/aWardedAudit-6:` labels (:959-1086), and two loop arms that
  print `ok   rule0: pair` (:887) and `ok   rule0: fold` (:936).
- So the population is 54 rule-0 labels and 14 rule-5 labels. AC9's regex reads 24 and 4.

### The census

```bash
git show 3708a705:tools/hooks/agent-cap.test.sh \
  | grep -oE '"rule[05](/[^:"]*)?:([^"\\]|\\.)*"' | sed 's/^"//; s/"$//' | sort -u   # 66 labels
printf '%s\n' 'rule0: pair' 'rule0: fold'                                            # +2 loop labels
# per label L (rule0* -> spec-audit-optin.test.sh, rule5* -> check-review-join.test.sh):
#   home: grep -cF -- "L" <receiving suite>       >= 1
#   gone: grep -cF -- "L" tools/hooks/agent-cap.test.sh   == 0
```

The census runs as a scratch probe. It prints one line per label that fails either test, then the
two totals, and exits non-zero when any line printed. A label is matched as its source bytes,
escapes included, so a moved arm keeps its quoting.

### What it does not check

That a moved arm still asserts what it asserted at base. The receiving suites' own runs, observed
RED then GREEN at the close under unit 16's `New arm:` lines, own that. The census proves only
placement.

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`
- `tools/workflows/spec-audit-optin.test.sh`
- `tools/workflows/check-review-join.test.sh`

Each changes only where the census finds an arm left behind or missing.

### Alternatives rejected

- **The report's regex, `"rule[05]:[^"]*"`.** It misses the 28 `rule0/<tag>:` labels and truncates
  the escaped-quote label at its first `\"`.
- **A census arm in a suite** — §8 F1.

## 5. Production-readiness checklist

- security — N/A: test suites only, no new input or write path.
- perf / scale — one scratch probe of 68 `grep -cF` pairs.
- error / empty / loading states — an empty population reds the probe: it asserts 54 and 14 before it
  reads any tip suite, so a regex that matches nothing cannot pass.
- observability — the probe names each failing label and which test it failed.
- risks — a label unit 16 reworded on purpose reads as missing. The move keeps labels byte for byte
  (§3), and a deliberate rename is a spec change first.
- testing — AC1 to AC3; the receiving suites' arms observed RED then GREEN at the close.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When §4's census command runs at `3708a705`, it prints 66 distinct labels: 52 rule-0
  labels, among them the indented MSYS-mount arm and the escaped-quote array arm, and 14 rule-5
  labels, among them the 8 `js` and 2 `jso` arms. With `rule0: pair` and `rule0: fold` added, the
  population is 54 and 14.
  Red when: a helper's arms or a `/<tag>` qualifier fall outside the population, so a total is short.
  figure: the totals are PINNED, measured at `3708a705` on 2026-10-23.
- **AC2** — When §4's census probe runs at this unit's commit, it prints no failing label: every
  rule-0 label `grep -cF` finds at least once in the pack's suite, every rule-5 label at least once
  in the join suite, and none in the hook's suite (S2 names the three files). It exits 0.
  Red when: a moved arm stays in the hook's suite, or is deleted rather than moved.
- **AC3** — When the probe runs over three scratch copies, it names each planted miss and exits
  non-zero: the hook's suite with `js "rule5: the Map ban fires"` restored, the join suite with that
  arm cut, and the pack's suite with its `rule0: fold` loop cut. A probe whose population regex is
  replaced by AC9's prints a short total first and exits non-zero.
  Red when: any planted miss passes, which means the census counts the regex and not the arms.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `spec tokens (a spec's own names resolve)`

The leg `spec-audit opt-in pack self-test` runs the pack's suite once `TOOL-dFairHearing-16` adds it
to `tools/gate-legs.json`. It is not on the line above because it is not in the manifest at this
spec's base.

New arm: tools/workflows/check-review-join.test.sh · covers none · any rule-5 arm this unit moves, staged with the ref-keyed ban cut from the check · none
New arm: tools/workflows/spec-audit-optin.test.sh · covers none · any rule-0 arm this unit moves, staged with rule 0 cut from the pack · none

The hook's suite (S2) takes no `New arm:` line: it only loses arms, and it carries no arm floor at
base to move.

## 8. Open questions

- **F1 — Does the census become a permanent suite arm?** Options: (a) a scratch probe whose output
  the acceptance ledger records; (b) an arm in the join suite that reds when a rule-5 label reappears
  in the hook's suite. (b) guards a regression nobody makes: the move is one act, and the receiving
  suites' arms already red if a rule's arms are lost. (a) proves this unit's claim and adds no
  standing code. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 10 (item H2) of the spec audit of units 20
  to 23.

## 10. Reuse audit

No existing seam fits a label census, and none is built: the probe is `git show`, `grep -oE` and
`grep -cF` over three suites. `python tools/codebase-map/reuse_lookup.py "count test arm labels moved
between suites"` ranked `counts` in `tools/unattended/check-playbook.test.sh`, the suites' own `arm`
helpers and `run_arms`, none of them a cross-suite label join. Reading the suite's source found what
the report's corrected regex misses, the 28 `rule0/<tag>:` labels. The recall query returned the
audit's H2 item, spec 16 S5 (the move) and spec 23 AC9, the criterion this unit replaces.

Recall terms used: `python tools/memory-recall/query.py "how is a moved test arm proven present at its new suite and gone from the old one" --terms "moved arms census label rule0 rule5 agent-cap.test.sh spec-audit-optin check-review-join js jso planted miss"`
