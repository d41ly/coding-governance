# TOOL-dFairHearing-29 — the five escaped-quote arms of the hook's suite checked by name, at their home and gone from the old one

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 21 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-29-deviation-291.md](../build/2026-10-23-build-TOOL-dFairHearing-29-deviation-291.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-28 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-29-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-29-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md) | spec-audit | TOOL-dFairHearing-28 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit's finding id 1 (item H1, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`) is
closed. `TOOL-dFairHearing-26`'s S1 and AC1 say the census population holds the escaped-quote array
arm, while its pinned counts hold only the reading that drops every escaped-quote label. Its members
and its counts therefore disagree, and a probe tuned to the counts drops 5 arms. This unit names
those five arms by their source bytes and checks each one by name: present in the base population,
at its home at this unit's commit, and gone from the hook's suite. A count cannot stand in for a
named member, so no pinned total can hide one.

## 2. Scope (IN)

- **S1** — The five members, PINNED at `3708a705` on 2026-10-23 as the labels of
  `tools/hooks/agent-cap.test.sh` at lines 874, 959, 985, 988 and 1063. Each is a `rule0` label that
  holds an escaped quote. A member check reads each label from its pinned line by an escape-aware
  scan with no regex, so no quoting layer can fold it, and refuses a line whose label is not such a
  member. §4 gives the script. Observed by AC1 and AC3.
- **S2** — Placement by name. At this unit's commit each member is spelled in
  `tools/workflows/spec-audit-optin.test.sh` (the pack's suite) and none in
  `tools/hooks/agent-cap.test.sh` (the hook's suite). A member the move left behind, or one spelled in
  neither suite, is moved by this unit with its label, payload and verdict unchanged. Observed by AC2.
- **S3** — Supersession. Unit 26's AC1 member clause, "among them the indented MSYS-mount arm and the
  escaped-quote array arm", is answered by this unit's S1 for every escaped-quote member, and unit 26's
  S1 sentence keeping escaped quotes by this unit's AC1. Unit 26's acceptance ledger records them
  superseded here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by a criterion of this unit: it
  is a ledger entry in unit 26's record, read there.

## 3. Non-goals (OUT)

- No totals. The population's size is `TOOL-dFairHearing-28`'s mechanism, finding id 11. This unit
  checks named members only, so the two hold independently.
- No rule-5 member: no rule-5 label at base holds an escaped quote.
- No change to what a moved arm asserts, as unit 26 §3 states.
- No permanent arm in a suite, by unit 26 §8 F1. No help page: `help/` covers no suite.

### Edges

- **consumes-from** `TOOL-dFairHearing-26` — the move of rule 0 arms to the pack's suite and the census's membership claim this unit checks by name
- **hands-off** `TOOL-dFairHearing-36` — the round-4 spec audit's minors on this spec, ids 3, 7, 21, 24, 28 and 30: S2's move sentence and AC2 superseded, the move being unit 28's alone and each member checked once there, the member check decoding and printing UTF-8, label() naming a quote-less line, AC1 recorded as a precondition, the extractor's path and the pack suite's leg (its S1, S4, S6, S7, S9 and S10)


## 4. Design

### Evidence

Measured at `3708a705` on 2026-10-23, PINNED. The five labels, as their source bytes:

| Line | Label |
|---|---|
| 874 | `rule0: kind [\"spec-audit\"] (an array) on the undeclared README → deny` |
| 959 | `rule0/U7: README without the key, conf SPEC_AUDIT_DEFAULT=\"<date>\" → allow by project default` |
| 985 | `rule0/U7: conf SPEC_AUDIT_DEFAULT=\"yes\" → deny naming the key, not a date` |
| 988 | `rule0/U7: conf SPEC_AUDIT_DEFAULT=\"\" (blank) → the README deny, unchanged` |
| 1063 | `rule0/aWardedAudit-6: harness reviewDir \"\" → placed in builds/tSA, the live run denies` |

Each sits under `check_spec_audit`. The folded reading that produced unit 26's 66 drops exactly these
five, as the audit's ids 1 and 11 measured.

### The member check

```python
# members.py <base-ref> [<hook suite> <pack suite>]
import subprocess, sys
LINES = (874, 959, 985, 988, 1063)
base = subprocess.run(["git", "show", f"{sys.argv[1]}:tools/hooks/agent-cap.test.sh"],
                      capture_output=True, text=True, check=True).stdout.splitlines()
def label(line):
    i = j = line.index('"') + 1
    while line[j] != '"':
        j += 2 if line[j] == chr(92) else 1
    return line[i:j]
members = [label(base[n - 1]) for n in LINES]
for n, m in zip(LINES, members):
    print(f"member :{n} {m}")
bad = [f"not a member :{n}" for n, m in zip(LINES, members)
       if not m.startswith("rule0") or chr(92) + '"' not in m]
if len(sys.argv) == 4:
    hook, pack = (open(p, encoding="utf-8").read() for p in sys.argv[2:4])
    bad += [f"home {m}" for m in members if m not in pack]
    bad += [f"gone {m}" for m in members if m in hook]
print("\n".join(bad))
sys.exit(1 if bad else 0)
```

The pass writes it as a file with its file-writing tool, under its scratch directory. The scan steps
over a backslash and the character after it, so `\"` never ends a label, and it holds no pattern a
shell could fold.

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`
- `tools/workflows/spec-audit-optin.test.sh`

Each changes only where AC2 finds a member left behind or missing.

### Alternatives rejected

- **Name the members inside unit 28's census.** One script then carries both the totals and the
  members, and a fix tuning one answer can move the other. Two checks that share no state hold
  independently, which is the point of finding id 1.
- **Name only the array arm, as unit 26's AC1 does.** Four of the five dropped arms are not the array
  arm, so one named member leaves four unnamed.

## 5. Production-readiness checklist

- security — N/A: a read-only scratch probe and test suites, no new input or write path.
- perf / scale — one `git show` and two file reads.
- error / empty / loading states — a pinned line that holds no escaped-quote `rule0` label is named as
  `not a member`, so a moved base line cannot pass as an empty check.
- observability — the script prints each member with its line, then each failing member and the test
  it failed.
- risks — the pinned line numbers are base's, read through `git show 3708a705:`, so later edits to the
  hook's suite do not move them.
- testing — AC1 to AC3; the pack's suite arms observed RED then GREEN at the close.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`members.py` is the script of §4, written under the pass's scratch directory.

- **AC1** — When `python members.py 3708a705` runs, it prints five `member` lines, at :874, :959,
  :985, :988 and :1063, each label holding `\"` and equal to §4's table row, and exits 0.
  Red when: the scan ends a label at its first escaped quote, so a member prints truncated.
  figure: the line numbers are PINNED, measured at `3708a705` on 2026-10-23.
- **AC2** — When `python members.py 3708a705` runs at this unit's commit with the hook's suite and the
  pack's suite as its two paths (S2 names the files), it prints no `home`, `gone` or `not a member`
  line and exits 0.
  Red when: a member is left in the hook's suite, or is deleted rather than moved.
- **AC3** — When the check runs over a scratch copy of the pack's suite with the :874 arm cut, it
  prints `home rule0: kind [\"spec-audit\"]` and the rest of that label, and exits non-zero. Over a
  scratch copy of the hook's suite with the :1063 arm restored, it prints a `gone` line naming that
  label and exits non-zero. With `LINES` holding 873, it prints `not a member :873` and exits non-zero.
  Red when: any of the three exits 0, which means the check matches nothing and passes.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/spec-audit-optin.test.sh · covers none · any of the five members this unit moves, staged with rule 0 cut from the pack · none

The hook's suite takes no `New arm:` line: it only loses arms, and it carries no arm floor at base.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (item H1, HIGH) of the round-3 spec audit
  of specs 4, 14, 25, 26 and 27.
- rev-2 · 2026-10-23 · §3 · the round-4 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-36 (six minors);
  S2's move sentence and AC2 are superseded there.

## 10. Reuse audit

No existing seam fits a named-member check over a suite's labels. `python
tools/codebase-map/reuse_lookup.py "count labels in a test suite with a regex read from a file"`
ranked the generic `read`, `read_text` and `counts` stems; `tools/workflows/extract-arms.sh` reads a
printed total and refuses this suite (the audit's refuted id 18). The script is `git show` and a
character scan. The recall query returned the audit's H1 and B1 items, which share the defect and
take two mechanisms, and `TOOL-aBatchedTribunal-1b` on inline text that never became a file.

Recall terms used: `python tools/memory-recall/query.py "a regex pinned in a spec measured from an inline shell string folds its backslashes" --terms "census label rule0 rule5 escaped quote backslash fold agent-cap.test.sh population pin script file"`
