# TOOL-dSafePassage-46 — the spec audit of units 36 to 42, its three minors off the step module: the drift pin raised in the pass that arms its key, a lander arm that finds its sibling kit, and the `ac-order` key documented

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-46-deviation-92.md](../build/2026-10-23-build-TOOL-dSafePassage-46-deviation-92.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 36 to 42
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`)
exited CONVERGED with 24 minors, which split into two disjoint write sets by BUILD-METHOD M6's
clauses. `TOOL-dSafePassage-45` batches the 21 whose writes are the step module. This unit batches
the other three, 2 MEDIUM and 1 LOW, each by its report id and each its own scope item: they land on
TOOL-dSafePassage-34, TOOL-dSafePassage-41 and TOOL-dSafePassage-42, so this unit repairs none in
particular and builds after every unit, order 11. Where a minor would bite an earlier pass, the
faulted unit's own §3 hands-off bullet to this unit names it, so that pass may build it.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-10 | MEDIUM | 25 | S1 |
| D-11 | MEDIUM | 15 | S2 |
| D-20 | LOW | 16 | S3 |

The report refuted none and left none unverified. The skeptic re-graded id 16 from medium to low and
REJECTED its finder's fix, so S3 is built from the skeptic's corrected fix.

## 2. Scope (IN)

- **S1** — id 25. TOOL-dSafePassage-42 S9's raise of `cutoff_keys_armed` 36 -> 37
  (`tools/drift-audit/drift_signals.py:351`), its in-place comment naming `SPEC_AC_ORDER_CUTOFF` and
  its `memory/DECISIONS.md` row in TOOL-dTrueNorth-28's form, is read as landing in
  TOOL-dSafePassage-34's pass, the commit that arms that key. The `drift-audit records` leg runs
  `drift_report.py --check` with no guard (`tools/gate-legs.json:1053`), which exits 1 when a gateable
  signal is over its pin (`tools/drift-audit/drift_report.py:8`), so the raise and the key land in one
  commit and the leg 42 S9 hands to TOOL-dSafePassage-34's §7 is green at every commit from that pass
  on. 42 S9's sentence on the signal reading 37 against 36 until order 10 is read as void, and its §8
  F1 resolution (a) stands, carried out at that pass. TOOL-dSafePassage-34's `--dispatch --writes`
  gain `tools/drift-audit/drift_signals.py` and `memory/DECISIONS.md`. TOOL-dSafePassage-34's §3
  hands-off bullet to this unit names the reading. Observed by AC1.
- **S2** — id 15. TOOL-dSafePassage-42 S12's arm in `tools/push-main.test.sh` loads `check-arms.py`
  from the memory-tree kit's directory beside the lander, found by the scan arm 26 already runs, a
  sibling of `$HERE` holding `routed_commits.py` (`tools/push-main.test.sh:872`), never by a typed
  `tools/memory-tree/` path. Where no such directory exists, the arm prints a `skip —` line naming the
  absent kit, as arm 26 does (`:907`). The suite ships to adopters at any prefix
  (`WIRE-INTO-PROJECT.md:927`) and finds its subject through `KIT_REL` (`tools/push-main.test.sh:14-22`).
  TOOL-dSafePassage-42's §3 hands-off bullet to this unit names it. Observed by AC2.
- **S3** — id 16, the skeptic's corrected fix. The `ac-order` join TOOL-dSafePassage-41 builds gets a
  paragraph in the §6 body of the skeleton in `tools/memory-tree/SPEC-TEMPLATE.template.md`, the
  authored source, rendered into `memory/TEMPLATE-SPEC.md`; and
  `tools/memory-tree/.memory-tree.conf.example` gains a blank `SPEC_AC_ORDER_CUTOFF=""` row with its
  comment, as the convention at `memory/TEMPLATE-SPEC.md:274-275` gives the guard-legs key.
  TOOL-dSafePassage-41's §4 Files touched is read with these three files; its §3 hands-off bullet to
  this unit names the reading. Observed by AC3.

## 3. Non-goals (OUT)

- Every step-module minor: `TOOL-dSafePassage-45`.
- Both highs: `TOOL-dSafePassage-43` and `TOOL-dSafePassage-44`.
- A template paragraph and an example row for `SPEC_HANDOFF_CUTOFF` and `SPEC_CARRIES_CUTOFF`, which
  the skeptic of id 16 found missing too; they are not this finding's key, and a follow-up ask names
  them if the owner wants them.
- An arm holding every `SPEC_*_CUTOFF` key to a template paragraph and an example row, the report's
  left-shift gate, which would red on those two keys today.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here.

### Edges

- **consumes-from** `TOOL-dSafePassage-34` — the pass that arms `SPEC_AC_ORDER_CUTOFF`, into which S1 moves the pin raise and its decision row
- **consumes-from** `TOOL-dSafePassage-41` — the `ac-order` join, whose key S3 documents in the template and the example conf
- **consumes-from** `TOOL-dSafePassage-42` — S9's pin raise and S12's `tools/push-main.test.sh` arm, which S1 re-sequences and S2 locates

## 4. Design

### The three passes S1 orders

| Order | Unit | Commit carries | `drift-audit records` |
|---|---|---|---|
| 7 | TOOL-dSafePassage-34 | `SPEC_AC_ORDER_CUTOFF` armed, `cutoff_keys_armed` pinned at 37, the decision row | green: 37 of 37 |
| 10 | TOOL-dSafePassage-42 | no pin move; its AC6 reads the raise | green |
| 11 | this unit | no pin move; AC1 reads which commit raised it | green |

### The arm's locator

```
_mt_rc=$(cd "$HERE" && for d in */; do [ -f "$d/routed_commits.py" ] && { printf '%s' "${d%/}"; break; }; done)
if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then
  # load "$HERE/$_mt_rc/check-arms.py" by path, as S12 of TOOL-dSafePassage-42 counts
else
  echo "  skip — <arm> no memory-tree kit beside this lander, so the derived-count arm did not run"
fi
```

The scan is the one at `tools/push-main.test.sh:872`, which sets `_mt_rc` at the suite's top level,
reused rather than copied: the arm reads that variable, and the scan line above is shown only to name
what sets it.

### The template paragraph

One paragraph after the `SPEC_FAILURE_MODE_CUTOFF` paragraph of the skeleton's §6 body, in that
paragraph's shape: once a spec's filename date reaches `SPEC_AC_ORDER_CUTOFF` (`.memory-tree.conf`;
blank turns it off), a LIVE spec's §6 criterion labels must ascend, and the spec-token checker's
`ac-order` join names the spec and the first label out of order. The template spells the checker as
`{{SPEC_TOKEN_CHECKER}}`, the placeholder its sibling paragraphs use, and the dogfood copy is
re-rendered by the kit/dogfood parity suite's render mode, so the two stay byte-equal after
placeholders.

### Inventory

Minted: none. No function, conf key, gate leg, plant or policy key: `SPEC_AC_ORDER_CUTOFF` is
TOOL-dSafePassage-34's key, and S3 adds its blank example row only.

### Migration

None.

### Rollout

Live at landing. It builds at order 11, after every unit of the build. Its write set,
`tools/push-main.test.sh`, `tools/memory-tree/SPEC-TEMPLATE.template.md`, `memory/TEMPLATE-SPEC.md` and
`tools/memory-tree/.memory-tree.conf.example`, does not meet `TOOL-dSafePassage-45`'s; neither writes
a file the other reads as a contract or an acceptance input; and neither writes a shared mutable
record, since S1 moves the `memory/DECISIONS.md` write into TOOL-dSafePassage-34's pass. So the two
passes at order 11 run concurrently (M6). At order 7, TOOL-dSafePassage-31 writes no
`memory/DECISIONS.md` and no drift file, so S1 adds no shared record to that group.

### Files touched (estimate)

- `tools/push-main.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `tools/memory-tree/.memory-tree.conf.example`

### Alternatives rejected

- **Leaving `drift-audit records` off TOOL-dSafePassage-34's §7 and stating it red until order 10
  (S1).** The report's second option; it keeps three commits red on a leg the main loop may run
  mid-build (M6), the class `TOOL-dSafePassage-41` closed for the `ac-order` join, and that unit's rule,
  the gate lands in the pass that moves its signal, decides between the two options without a fork.
- **Inlining the blanking `check-arms.py` gives (S2).** A second copy of `scan_shell_lines` in the
  lander's suite, beside the one TOOL-dSafePassage-42 S12 reuses.
- **Writing the paragraph into `memory/TEMPLATE-SPEC.md` alone (S3).** The dogfood copy is rendered
  from the template, so a paragraph in the copy alone reds the parity leg, and an adopter never
  receives it; the skeptic's corrected fix names the template source for that reason.

## 5. Production-readiness checklist

- security: N/A — a pin's commit, a test locator and documentation.
- perf / scale: unchanged.
- error / empty / loading states: S2's skip line names the absent kit, so an adopter's suite run says
  why the arm did not run.
- observability: S1's raise and its decision row sit in the commit that arms the key.
- risks: S1 widens TOOL-dSafePassage-34's write set by two files; its dispatch records them.
- testing: AC1's history probe, AC2's grep and the arm of §7, AC3's grep.
- migration: none.
- user docs: `memory/TEMPLATE-SPEC.md` (S3); no `help/` page covers the spec-token checker.

## 6. Acceptance criteria

- **AC1** — When `git log --reverse --format=%H -S '"cutoff_keys_armed": 37' -- tools/drift-audit/drift_signals.py`
  runs, its first commit's subject names TOOL-dSafePassage-34, and `git show --stat` of that commit
  lists `.memory-tree.conf` and `memory/DECISIONS.md`; and `python tools/drift-audit/drift_report.py --json`
  reads `cutoff_keys_armed` at or under its pin.
  Red when: the raise lands in a commit after the one that arms the key, or the signal is over its pin.
- **AC2** — When `git grep -n -e "check-arms.py" -e "tools/memory-tree" -- tools/push-main.test.sh`
  runs, the arm's load spells `$HERE/` and the scanned directory variable, no line of the arm spells
  `tools/memory-tree/`, and the arm's `skip —` line names the memory-tree kit.
  Red when: the arm loads `check-arms.py` by a typed path, or has no skip.
- **AC3** — When `git grep -n -e "SPEC_AC_ORDER_CUTOFF" -e "ac-order" -- tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md tools/memory-tree/.memory-tree.conf.example`
  runs, each of the three files prints a line, the example conf's line reading `SPEC_AC_ORDER_CUTOFF=""`.
  Red when: an adopter's template or example conf carries no word of the join or its key.

## 7. Gates

`push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `drift-audit records` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC2 · the derived-count arm run from a copy of the lander pair at a foreign prefix and from one with no memory-tree kit beside it, its failing case staged by an arm copy that loads `tools/memory-tree/check-arms.py` by a typed path · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 36 to 42's 2 MEDIUM and 1
  LOW findings off the step module, one scope item per raw id.

## 10. Reuse audit

The seams extended are the lander suite's kit scan (`tools/push-main.test.sh:872`) and its skip line
(`:907`), the drift pin (`tools/drift-audit/drift_signals.py:351`) and its decision form
(`memory/DECISIONS.md`, TOOL-dTrueNorth-28), and the template's cutoff paragraphs
(`memory/TEMPLATE-SPEC.md:258-275`). `python tools/codebase-map/reuse_lookup.py "locate a sibling kit
beside the lander and skip when absent"` ranked `absent`, `skip`, `kit_rel` and `resolve_kit_dir`;
`resolve_kit_dir` installs into `tools/push-main.test.sh` already, but the scan at `:872` is the one
that suite uses to find the memory-tree kit, so S2 reuses that scan rather than a second locator.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted unit" --terms "spec audit minors batch promoted reading hands-off consumes-from order disposal rescope severity"`
