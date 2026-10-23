# TOOL-dGroundRules-50 — the help-page parity prints where it found the deferral line, so the install section is read by one rule

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-50-deviation-38.md](../build/2026-10-23-build-TOOL-dGroundRules-50-deviation-38.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 22 at HIGH**, which shares item **H2** with ids 2
(`TOOL-dGroundRules-48`) and 11 (`TOOL-dGroundRules-49`). Id 22 is H2 seen from reuse:
`TOOL-dGroundRules-41` reads the `## Install` section twice, once in `adopter-fresh-target`'s
parity (S1) and once in an `awk` literal (AC4), and the second spelling is the one that lost its
path. This unit is id 22's promotion: when the parity holds, the case prints the page line where it
found the deferral line, so a criterion that wants the section's content reads the case's own output,
and the section bounds are spelled once, in the case. It repairs `TOOL-dGroundRules-41`, which sits at
order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The witness. After the parity of `TOOL-dGroundRules-41` S1 holds, `adopter-fresh-target`
  prints `policy-fixture: adopter-fresh-target · help/policy.md:<n> carries the deferral line`,
  where `<n>` is the 1-based number of the page line holding both halves. Observed by AC1.
- **S2** — No witness without the parity. When the parity fails, the case prints its `WRONG` and no
  witness line, so the line is never printed for a deferral line outside the section.
  Observed by AC2.

## 3. Non-goals (OUT)

- The parity rule, its section bounds and its `WRONG`: `TOOL-dGroundRules-41` S1. This unit prints
  what that rule found and moves no bound.
- The two one-off observations: `TOOL-dGroundRules-48` and `TOOL-dGroundRules-49`.

### Edges

- **consumes-from** `TOOL-dGroundRules-41` — `adopter-fresh-target`'s parity of the help page's `## Install` section with the deferral line, whose found line S1 prints

## 4. Design

```text
adopter-fresh-target, after TOOL-dGroundRules-41's parity:
    n = the 1-based index, in help/policy.md, of the section line that held head then tail
    print "policy-fixture: adopter-fresh-target · help/policy.md:<n> carries the deferral line"
```

The index is the one the parity loop already visits, so the case reads the page once.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `carries the deferral line` | a `policy-fixture` line | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/policy/check_policy.py`

## 5. Acceptance criteria

Every command runs from the repository root. `check_policy.py` names the policy kit's file under the
kit, as `TOOL-dGroundRules-41` §6 does. A scratch copy is a git clone of this repository under
`%TEMP%/gr50`, checked out at the commit under test. The literal is spelled whole here, once:

```text
WITNESS_LINE = python tools/policy/check_policy.py --fixture adopter-fresh-target |
               sed -n 's/.*help\/policy\.md:\([0-9]*\) carries the deferral line.*/\1/p' |
               xargs -I{} sed -n '{}p' help/policy.md
```

- **AC1** — When `WITNESS_LINE` runs on the built tree, it prints one page line, and that line
  carries `mirror deferred`.
  Red when: the case prints no witness, or a line number that does not hold the deferral line.
- **AC2** — When `HELP_MOVED` of `TOOL-dGroundRules-41` §6 runs in the scratch copy and
  `python check_policy.py --fixture adopter-fresh-target` runs there, it prints a `WRONG` naming
  `policy.md` and no line carrying `carries the deferral line`.
  Red when: the witness is printed for a deferral line outside the install section.

## 6. Gates

`memory hygiene`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the case;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture adopter-fresh-target`) · covers AC2 · the deferral line moved out of `## Install` in a scratch copy's help page · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 22 (HIGH, item H2) of the round-1 spec
  audit of units 35 to 43, with unit 41's parity and its `awk` restatement read on 2026-10-23.

## 9. Reuse audit

The seam extended is `adopter-fresh-target`'s parity, `TOOL-dGroundRules-41` S1, which already
holds the line number it prints. `python tools/codebase-map/reuse_lookup.py "read test table rows
from a suite file to probe two overlap rules"` and the probe `TOOL-dGroundRules-41` §10 ran ranked no
seam that reads a help page's section, so no existing seam fits beyond that case. The recall probe
returned `TOOL-dGroundRules-41` and `TOOL-dGroundRules-42`; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
