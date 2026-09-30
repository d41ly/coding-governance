# TOOL-dAlignedCarrier-2 — the protocol's gates-green text points at the inherited-red contract

**Status:** CLOSED · rev-2 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · closes TOOL-dDerivedDocket-73 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-build-TOOL-dAlignedCarrier-2-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-dAlignedCarrier-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |

<!-- /gen:spec-records -->

## 1. Goal

The unattended protocol says a `gates-green` close means the full merge bar ran and PASSED, and its
Definition-of-Done section presents overrides as open for every item but the two it names. Both
predate the inherited-red policy: under `INHERITED_RED=land` a red made only of inherited legs lands,
and check 83 refuses a `gates-green` override unless every red is inherited, under any policy. This
unit makes both places point at `UNATTENDED-STOPS.md` §13, which owns that rule, instead of stating a
boundary the kit no longer implements.

## 2. Scope (IN)

- **S1** — The `gates-green` row of the protocol's §4 table (`tools/unattended/PROTOCOL.template.md:343`
  at BASE) is rewritten to the cell §4 "Wording" gives: the full merge bar ran on the tip being
  landed, and its verdict is one the inherited-red policy of `UNATTENDED-STOPS.md` §13 lands. The
  words "and passed" go with the old cell. Observed by AC1.
- **S2** — The §4 paragraph that opens "**`authorization-reachable` has NO override**" gains one
  closing sentence, §4 "Wording": `gates-green` is outside that set, and check 83 refuses its override
  except on the terms `UNATTENDED-STOPS.md` §13 states. It names the check and the section and
  restates neither the condition nor the policy. Observed by AC2.
- **S3** — The render follows in the same pass: `bash tools/unattended/adopt-unattended.sh` copies the
  template to `memory/guides/UNATTENDED-PROTOCOL.md`. Observed by AC3.
- **S4** — The pass grows the protocol by at most 300 bytes, its share of the 582 bytes free under the
  protocol's row in `tools/template-size-limits.txt` at BASE. Observed by AC4.
- **S5** — The kit gate stays green. No check reads these two sentences: check 16's no-override join
  reads the Skill's paragraph, not the protocol's. Observed by AC5.

## 3. Non-goals (OUT)

- The charter's merge-bar sentence in `AGENTS.md`. The owner's ruling on this ask wants it to point at
  the inherited-red policy too, but no accept clause of this build names `AGENTS.md`, so M3 veto 2
  leaves it to an attended edit.
- The charter template's §7 line. The same ruling keeps it: it is true under the kit default `park`.
- The protocol's §1 paragraph on the non-overridable set. It names the two items that take no
  override at all, and it stays true.
- `UNATTENDED-STOPS.md` §13 and the Skill's Close section, which already state the rule and are its
  owners.
- A `memory/DECISIONS.md` row: the owner's ruling row exists under the ask's own id.
- The kit version. The orchestrator moves it once, at VERIFYING.

### Edges

Files shared with a sibling, which are not edges: `tools/unattended/PROTOCOL.template.md` and its
render are also written by unit 3, which owns §10, and by unit 6, which owns the
`SELFTESTS_OWED_PATHS` row of the §8 table. This unit owns only the `gates-green` row of §4's table
and the no-override paragraph of §4. The protocol's byte headroom is shared as well: this unit takes
at most 300 bytes, unit 6 at most 120, and unit 3 none, which together fit the 582 free at BASE.

- **hands-off** external — the `AGENTS.md` merge-bar sentence the owner's ruling also names, for an
  attended edit; veto 2 holds it outside this run.

## 4. Design

### Evidence

At `87c245b3`, read on 2026-09-30. The row reads "the project's full merge bar ran on the tip being
landed and passed", byte-equal in the template and its render. `check_inherited_override`
(`tools/unattended/unattended.sh:6948`) is reached from `--close --override gates-green` (`:7197`) and
from `--abort --code gate-red-out-of-scope` (`:4700`) with no policy test, so check 83 binds under
`park` as under `land`. `grep -c 'check 83' memory/guides/UNATTENDED-PROTOCOL.md` prints 0: nothing in
the protocol names it. `UNATTENDED-STOPS.md` §13 carries the policy and, in its paragraph opening "The
two escape routes are backed or refused", both refused routes and their remedy.
`bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` reports 65110 of 65692 bytes.

### Wording

The row, whole:

```
| `gates-green` | machine | the project's full merge bar ran on the tip being landed, and its verdict is one the inherited-red policy of `UNATTENDED-STOPS.md` §13 lands |
```

The sentence appended to the no-override paragraph, after "every other check decorative.":

```
`gates-green` is outside that set, and check 83 refuses its override except on the terms `UNATTENDED-STOPS.md` §13 states.
```

Both are pointers: they name where the rule lives and which check enforces it, and neither states
the policy's values, its age bound or the condition check 83 tests. The builder may reword for the
line width, and must keep both anchors and the check number.

As built, the appended sentence opens "`gates-green` does take an override, and check 83 refuses
one": the paragraph names one item and no set, so "that set" had no antecedent there. Both anchors
and the check number are unchanged.

### Rollout

The render is `bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template
edit; it re-renders the Skill and re-copies the protocol and the stop contract. `bash tools/unattended/adopt-unattended.sh --check`
is the parity observation.

### Files touched (estimate)

`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md`

### Alternatives rejected

- Restating the land and park outcomes in the row. That is the drift the ask is filing.
- Putting the pointer in the "`--close` BLOCKS on any unmet item" paragraph. The accept clause names
  the non-overridable text, and that is where an agent whose override was refused reads.

## 5. Production-readiness checklist

- security — N/A: two sentences of documentation; no code path moves.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — N/A: check 83's refusal text is unchanged and already names its condition.
- risks — the protocol sits 582 bytes under its cap and three units write it; S4 bounds this one.
- testing — the greps, the render comparison, the size check and one kit-gate run below.
- migration — none.
- user docs — this is the user doc; the render carries it to adopters on their next pull.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'on the tip being landed and passed' memory/guides/UNATTENDED-PROTOCOL.md`
  runs after the pass, it prints 0, where BASE prints 1; and `grep -n '^| .gates-green. |' memory/guides/UNATTENDED-PROTOCOL.md`
  prints one row that names `UNATTENDED-STOPS.md` and §13.
  Red when: the row still asserts a pass, or points at no section.
- **AC2** — When `grep -c 'check 83' memory/guides/UNATTENDED-PROTOCOL.md` runs, it prints 1, where
  BASE prints 0; and `awk '/has NO override, and this is where a close meets that/,/^$/' memory/guides/UNATTENDED-PROTOCOL.md`
  prints a paragraph whose last sentence names check 83 and `UNATTENDED-STOPS.md` §13.
  Red when: the pointer sits outside that paragraph, or names only one of the two anchors.
- **AC3** — When `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` runs,
  it exits 0, and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: the render was not re-copied, or the copy differs by a byte.
- **AC4** — When `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` runs, it
  exits 0; and `wc -c < tools/unattended/PROTOCOL.template.md`, read before the pass and after it,
  differs by at most 300.
  Red when: the protocol breaches its row, or this pass takes more than its share.
  figure: the 300-byte share is PINNED, allocated on 2026-09-30 from the 582 bytes free at BASE; the
  growth is DERIVED at observation from the two readings.
- **AC5** — When `bash tools/unattended/check-unattended.sh --skip 28`, the argv of the
  `unattended kit gate` leg scoped past the 28 region, runs over the staged pass tree, it exits 0
  and prints no `FAILED` line.
  Red when: a check reads either sentence and reds.
  cost: one scoped run of the kit gate, its seconds MEASURED at observation. The unscoped leg, 593 s
  whole on node d on 2026-09-30 (PINNED), sits at a unit pass's 600 s command bound, so its verdict
  over the 28 region, which reads the playbook template and not the protocol, is the close bar's.

## 7. Gates

`unattended protocol size` · `unattended skill wiring` · `unattended kit gate` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — Which carriers owe the pointer?** The owner ruled on this ask's parked decision: the
  protocol's `gates-green` text owes the pointer to the inherited-red policy, the charter's
  merge-bar sentence owes it too, and the charter template's §7 line stays. RESOLVED (owner,
  2026-09-30): the protocol here; the charter sentence is handed off in §3 under veto 2, since no
  accept clause of this build names `AGENTS.md`.
- **F2 — Where in the protocol does the override pointer go?** (a) The no-override paragraph of §4.
  (b) The "`--close` BLOCKS" paragraph above it. (c) §1's non-overridable paragraph. (c) is about
  the two items with no override at all and is decided at run start; (b) is about the override
  mechanics in general. Recommendation (a). RESOLVED (agent, 2026-09-30, delegated): (a), the text
  the accept clause names and the one an agent reads when a close refuses it.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, from the ask's accept clause, the owner's ruling and the
  build's spec brief.
- rev-2 · 2026-09-30 · §4 §6 · AC5 · the build pass. AC5 runs the kit gate scoped `--skip 28` over
  the staged pass tree, the scope unit 1 took for the same reason: the unscoped leg measures 593 s
  against a unit pass's 600 s command bound, and the 28 region reads the playbook template and not
  the protocol, so the scope reads every check that could grade either sentence. The 28 region's
  verdict, and the grading of this pass's committed writes against its declaration, are the close
  bar's. §4 records the appended sentence as built, reworded under the licence §4 already gave.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "point a protocol row at the stop contract instead of
restating the gate verdict"` ranked name-stem neighbours only (`extract_row`, `render_ask_row`,
`scan_verdicts`); none is a carrier. No existing seam fits a two-sentence documentation edit; the
idiom reused is the protocol's own pointer form, "`UNATTENDED-STOPS.md` carries the rest", which §3,
§5 and §6 of the protocol already use for the stop contract.

Recall terms used: `gates-green inherited-red INHERITED_RED land park check 83 override protocol STOPS
section 13 non-overridable`.
