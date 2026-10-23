# TOOL-dFairHearing-28 — the hook suite's census re-pinned to 59 and 14, measured by a script file whose pattern no shell can fold

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 21 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-28-deviation-281.md](../build/2026-10-23-build-TOOL-dFairHearing-28-deviation-281.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit's blocker, finding id 11 (item B1, BLOCKER,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`), is
closed. `TOOL-dFairHearing-26` pins its census at 66 labels and a population of 54 and 14. Base
`3708a705` holds 71 labels and a population of 59 and 14. The 66 came from an agent shell that folded
the regex's `\\` to `\`, which drops every label holding an escaped quote. A correct census therefore
reds against unit 26's pin, and a census tuned to the pin leaves 5 arms unchecked. This unit re-pins
the totals, measures them with a script file whose pattern is built so no quoting layer can fold it,
and runs unit 26's placement check over the whole population.

## 2. Scope (IN)

- **S1** — The census is a Python script written to the pass's scratch directory as a file, never
  run as inline command text. Its pattern is built with `chr(92)` for every backslash, and the script
  asserts that its own pattern holds exactly four backslashes before it reads anything. §4 gives the
  script. Observed by AC1 and AC3.
- **S2** — The population, PINNED at `3708a705` on 2026-10-23: 71 distinct labels, which are 25
  `rule0:`, 13 `rule0/U7:`, 10 `rule0/aWardedAudit:` and 9 `rule0/aWardedAudit-6:` labels (57 rule-0)
  and 14 `rule5:` labels. With the loop labels `rule0: pair` and `rule0: fold` added, the population
  is 59 rule-0 and 14 rule-5. The script asserts 59 and 14 before it reads any suite at the tip.
  Observed by AC1.
- **S3** — Placement over the whole population. At this unit's commit every rule-0 label is found in
  `tools/workflows/spec-audit-optin.test.sh` (the pack's suite), every rule-5 label in
  `tools/workflows/check-review-join.test.sh` (the join suite), and no label in
  `tools/hooks/agent-cap.test.sh` (the hook's suite). An arm the move left behind, the five
  escaped-quote arms in particular, is moved by this unit with its label, payload and verdict
  unchanged. Observed by AC2.
- **S4** — Supersession. Unit 26's AC1 totals (66, 52, and the population of 54 and 14), §4
  Evidence's counts (24, 10, 10 and 8) and §5's assertion of 54 and 14 are answered by this unit's S2
  and AC1. Unit 26's AC2 is answered by this unit's AC2, over the population S2 pins. Unit 26's
  acceptance ledger records them superseded here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED
  by a criterion of this unit: it is a ledger entry in unit 26's record, read there.

## 3. Non-goals (OUT)

- No member list. The five escaped-quote labels by name are `TOOL-dFairHearing-29`'s mechanism,
  finding id 1. This unit pins totals and runs placement.
- No change to what a moved arm asserts, as unit 26 §3 states.
- No permanent census arm in a suite. Unit 26 §8 F1 resolved the census as a scratch probe, and this
  unit keeps that.
- No new gate leg, and no help page: `help/` covers no suite.

### Edges

- **consumes-from** `TOOL-dFairHearing-26` — the census's placement rule, the two loop labels and the move of rule 0 and rule 5 arms; this unit corrects that census's population and totals

## 4. Design

### Evidence

Measured at `3708a705` on 2026-10-23, PINNED, by a Python script file building the pattern with
`chr(92)` over `git show 3708a705:tools/hooks/agent-cap.test.sh`. It printed 71 labels: `rule0` 25,
`rule0/U7` 13, `rule0/aWardedAudit` 10, `rule0/aWardedAudit-6` 9 and `rule5` 14. The five labels that
hold an escaped quote sit at :874, :959, :985, :988 and :1063. The folded text, read as `grep -E`
reads it (`[^"\]` a class, `\.` a literal dot), prints 66 labels and a population of 54 and 14, unit
26's figures. Python refuses the folded text outright as an unterminated class, so the script's
self-check is the guard that holds under either reading.

### The census script

```python
# census.py <base-ref> [<hook suite> <pack suite> <join suite>]
import re, subprocess, sys
BS = chr(92)
PAT = '"rule[05](/[^:"]*)?:([^"' + BS * 2 + ']|' + BS * 2 + '.)*"'
if PAT.count(BS) != 4:
    sys.exit(f"census: the pattern lost a backslash: {PAT}")
base = subprocess.run(["git", "show", f"{sys.argv[1]}:tools/hooks/agent-cap.test.sh"],
                      capture_output=True, text=True, check=True).stdout
found = sorted({m.group(0)[1:-1] for m in re.finditer(PAT, base)})
for tag in ("rule0", "rule0/U7", "rule0/aWardedAudit", "rule0/aWardedAudit-6", "rule5"):
    print(f"{tag}: {sum(1 for l in found if l.split(':')[0] == tag)}")
print(f"labels {len(found)}")
pop = found + ["rule0: pair", "rule0: fold"]
r0 = [l for l in pop if l.startswith("rule0")]
r5 = [l for l in pop if l.startswith("rule5")]
print(f"population {len(r0)} {len(r5)}")
if (len(r0), len(r5)) != (59, 14):
    sys.exit("census: the population is not 59 and 14")
if len(sys.argv) == 5:
    hook, pack, join = (open(p, encoding="utf-8").read() for p in sys.argv[2:5])
    bad = [f"home {l}" for l in r0 if l not in pack] + [f"home {l}" for l in r5 if l not in join]
    bad += [f"gone {l}" for l in pop if l in hook]
    print("\n".join(bad))
    sys.exit(1 if bad else 0)
```

A label is matched as its source bytes, escapes included, so a moved arm keeps its quoting. The
pass writes the file with its file-writing tool. A heredoc or a `python -c` string is the inline form
S1 refuses, because the layer that folded the original regex sits between the author and the shell.

### What it does not check

That a moved arm still asserts what it asserted at base, as unit 26 §4 says. The census proves the
population's size and each label's placement.

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`
- `tools/workflows/spec-audit-optin.test.sh`
- `tools/workflows/check-review-join.test.sh`

Each changes only where AC2 finds an arm left behind or missing.

### Alternatives rejected

- **Keep the regex as inline shell text and re-measure.** The fold happens between the author and the
  shell, so a re-measure through the same channel can fold again. The `chr(92)` build and the
  pattern self-check fail closed instead.
- **A committed census script.** Unit 26 §8 F1 refused a permanent census, and a script nobody re-runs
  after the move guards nothing.

## 5. Production-readiness checklist

- security — N/A: a read-only scratch probe and test suites, no new input or write path.
- perf / scale — one `git show` and three file reads.
- error / empty / loading states — a folded pattern exits at the self-check before any read. A short
  population exits before any suite is read, so a pattern matching nothing cannot pass.
- observability — the script prints each tag's count, the label total, the population and each
  failing label with the test it failed.
- risks — a label reworded on purpose reads as missing; unit 26 §3 keeps labels byte for byte.
- testing — AC1 to AC3; the receiving suites' arms observed RED then GREEN at the close.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`census.py` is the script of §4, written under the pass's scratch directory.

- **AC1** — When `python census.py 3708a705` runs, it prints `rule0: 25`, `rule0/U7: 13`,
  `rule0/aWardedAudit: 10`, `rule0/aWardedAudit-6: 9`, `rule5: 14`, `labels 71` and `population 59 14`,
  and exits 0.
  Red when: the pattern loses a backslash, so the escaped-quote labels drop and the totals read 66
  and 54.
  figure: the totals are PINNED, measured at `3708a705` on 2026-10-23.
- **AC2** — When `python census.py 3708a705` runs at this unit's commit with the hook's suite, the
  pack's suite and the join suite as its three paths (S3 names the files), it prints no failing line
  and exits 0.
  Red when: a moved arm stays in the hook's suite, an arm is deleted rather than moved, or one of the
  five escaped-quote arms never reached the pack's suite.
- **AC3** — When a scratch copy of `census.py` builds the escape alternative with `BS` in place of
  `BS * 2`, which is the literal-dot reading `grep -E` gave the folded text, it exits non-zero naming
  `the pattern lost a backslash` before any `git show`. When that copy also drops the self-check, it
  prints `labels 66` and `population 54 14` and exits non-zero on the 59 and 14 assertion.
  Red when: either copy exits 0, which means the census counts whatever the pattern matched.
  figure: 66 and 54 are PINNED, reproduced at `3708a705` on 2026-10-23 by that copy.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/check-review-join.test.sh · covers none · any rule-5 arm this unit moves, staged with the ref-keyed ban cut from the check · none
New arm: tools/workflows/spec-audit-optin.test.sh · covers none · any rule-0 arm this unit moves, the five escaped-quote arms included, staged with rule 0 cut from the pack · none

The hook's suite takes no `New arm:` line: it only loses arms, and it carries no arm floor at base.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 11 (item B1, BLOCKER) of the round-3 spec
  audit of specs 4, 14, 25, 26 and 27.

## 10. Reuse audit

No existing seam fits a label census, as unit 26 §10 found. The round-3 audit refuted
`tools/workflows/extract-arms.sh` as one (finding id 18): it reads a suite's printed total, and the
hook's suite prints `---- $pass passed, $fail failed ----`, which it refuses. `python
tools/codebase-map/reuse_lookup.py "count labels in a test suite with a regex read from a file"`
ranked the generic `read`, `read_text` and `counts` stems, none a cross-suite label join. The recall
query returned `TOOL-aBatchedTribunal-1b`, whose measurement that every inline `Workflow` script never
became a file is the same channel S1 refuses, and the audit's B1 item.

Recall terms used: `python tools/memory-recall/query.py "a regex pinned in a spec measured from an inline shell string folds its backslashes" --terms "census label rule0 rule5 escaped quote backslash fold agent-cap.test.sh population pin script file"`
