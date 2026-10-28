# TOOL-dSafePassage-46 — the spec audit of units 36 to 42, its three minors off the step module: the drift pin raised in the pass that arms its key, a lander arm that finds its sibling kit, and the `ac-order` key documented

**Status:** CLOSED · rev-3 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-46-deviation-92.md](../build/2026-10-23-build-TOOL-dSafePassage-46-deviation-92.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-46-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-46-ledger.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-46-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-46-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 |

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
  (`tools/drift-audit/drift_signals.py:352`), with its in-place comment naming TOOL-dSafePassage-34,
  `SPEC_AC_ORDER_CUTOFF` and ER:388, is read as landing in TOOL-dSafePassage-34's pass, the commit
  that arms that key. The `drift-audit records` leg runs
  `drift_report.py --check` with no guard (`tools/gate-legs.json:1053`), which exits 1 when a gateable
  signal is over its pin (`tools/drift-audit/drift_report.py:8`), so the raise and the key land in one
  commit and the leg 42 S9 hands to TOOL-dSafePassage-34's §7 is green at every commit from that pass
  on. 42 S9's sentence on the signal reading 37 against 36 until order 10 is read as void, and its §8
  F1 resolution (a) stands, its pin raise carried out at that pass. TOOL-dSafePassage-34's
  `--dispatch --writes` gain `tools/drift-audit/drift_signals.py` alone. The `memory/DECISIONS.md`
  row F1 (a) owes, in TOOL-dTrueNorth-28's form (`memory/DECISIONS.md:239`), is the main loop's,
  written at the close in a `Pass: none` commit, as that row landed at dTrueNorth's close
  (`53321feef`): `--dispatch` refuses a pass declaring a shared mutable record
  (`tools/unattended/unattended.sh:14004`, check 49), and BUILD-METHOD M6 clause 3 names
  `memory/DECISIONS.md` one. The ratchet reads only the in-place `36 -> 37` comment
  (`tools/drift-audit/drift_report.py:268-275`), so TOOL-dSafePassage-34's pass is green on that leg
  without the row. TOOL-dSafePassage-34's §3 hands-off bullet to this unit names the reading.
  Observed by AC1: its pin half at this pass, its row half by the main loop at the close, as
  TOOL-dSafePassage-52 S1 leaves an observation to the main loop.
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

- **consumes-from** `TOOL-dSafePassage-34` — the pass that arms `SPEC_AC_ORDER_CUTOFF`, into which S1 moves the pin raise; the decision row is the main loop's, at the close
- **consumes-from** `TOOL-dSafePassage-41` — the `ac-order` join, whose key S3 documents in the template and the example conf, this unit alone writing those three files, finding 5 of the spec audit of units 43 to 46
- **consumes-from** `TOOL-dSafePassage-42` — S9's pin raise and S12's `tools/push-main.test.sh` arm, which S1 re-sequences and S2 locates
- **hands-off** `TOOL-dSafePassage-50` — S2's arm placed after the `_mt_rc` scan with a criterion that it prints `ok` in gov's own tree, its locator cited by content, and S3's three files written by this unit alone, findings 30, 8, 13, 17 and 5 of the spec audit of units 43 to 46

## 4. Design

### The three passes S1 orders

| Order | Unit | Commit carries | `drift-audit records` |
|---|---|---|---|
| 7 | TOOL-dSafePassage-34 | `SPEC_AC_ORDER_CUTOFF` armed, `cutoff_keys_armed` pinned at 37 with its `36 -> 37` comment | green: 37 of 37 |
| 10 | TOOL-dSafePassage-42 | no pin move; its AC6 reads the raise | green |
| 11 | this unit | no pin move; AC1 reads which commit raised it | green |
| close | the main loop | the decision row, in a `Pass: none` commit | green |

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
record, since S1 leaves the `memory/DECISIONS.md` row to the main loop at the close. So the two
passes at order 11 run concurrently (M6). At order 7, S1 adds only
`tools/drift-audit/drift_signals.py` to TOOL-dSafePassage-34's write set, a file
TOOL-dSafePassage-31 does not write, and no shared record to that group.

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
- observability: S1's raise sits in the commit that arms the key; its decision row in the close's
  `Pass: none` records commit.
- risks: S1 widens TOOL-dSafePassage-34's write set by one file; its dispatch records it.
- testing: AC1's history probe, AC2's grep and the arm of §7, AC3's grep.
- migration: none.
- user docs: `memory/TEMPLATE-SPEC.md` (S3); no `help/` page covers the spec-token checker.

## 6. Acceptance criteria

- **AC1** — When `git log --reverse --format=%H -S '"cutoff_keys_armed": 37' -- tools/drift-audit/drift_signals.py`
  runs, its first commit is TOOL-dSafePassage-34's pass commit, its subject naming that unit, and
  `git show --stat` of that commit lists `.memory-tree.conf` and `tools/drift-audit/drift_signals.py`
  and not `memory/DECISIONS.md`; and `python tools/drift-audit/drift_report.py --json` reads
  `cutoff_keys_armed` at or under its pin. At the close, after the main loop's records commit,
  `git log --format='%h %(trailers:key=Pass,valueonly)' -S 'TOOL-dSafePassage-34' -- memory/DECISIONS.md`
  prints the commit that added the decision row, its `Pass` trailer reading `none`.
  Red when: the raise lands in a commit after the one that arms the key, the pass commit carries the
  decision row, or the signal is over its pin.
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
- rev-2 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotions of the spec audit of units 43 to 46, `TOOL-dSafePassage-50`, and the `TOOL-dSafePassage-41` bullet is amended for them, written by the disposal stage; no other section moved.
- rev-3 · 2026-10-27 · S1 · AC1 · §3 · §4 · §5 · §10 · S1 moves the pin raise alone into
  TOOL-dSafePassage-34's pass, its write set gaining `tools/drift-audit/drift_signals.py` only: the
  `memory/DECISIONS.md` row is the main loop's, at the close in a `Pass: none` commit, because
  `--dispatch` refuses a pass declaring a shared mutable record (check 49); AC1 reads the raise in
  that pass commit and the row in the close's records commit; the `TOOL-dSafePassage-34` Edges
  bullet, §4's pass table and Rollout, and §5's observability and risk lines follow, and §10's pin
  and row cites move to `:352` and `:239`; by
  `memory/builds/dSafePassage/prompts/2026-10-27-prompt-TOOL-dSafePassage-34-2-spec-writer.md`.

## 10. Reuse audit

The seams extended are the lander suite's kit scan (`tools/push-main.test.sh:872`) and its skip line
(`:907`), the drift pin (`tools/drift-audit/drift_signals.py:352`) and its decision form
(`memory/DECISIONS.md:239`, TOOL-dTrueNorth-28), and the template's cutoff paragraphs
(`memory/TEMPLATE-SPEC.md:258-275`). `python tools/codebase-map/reuse_lookup.py "locate a sibling kit
beside the lander and skip when absent"` ranked `absent`, `skip`, `kit_rel` and `resolve_kit_dir`;
`resolve_kit_dir` installs into `tools/push-main.test.sh` already, but the scan at `:872` is the one
that suite uses to find the memory-tree kit, so S2 reuses that scan rather than a second locator.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted unit" --terms "spec audit minors batch promoted reading hands-off consumes-from order disposal rescope severity"`
