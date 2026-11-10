# TOOL-aSwiftRefusal-1 — `--dispatch` runs the spec-token check after every cheap refusal

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSwiftRefusal-1-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md) | journal | TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 TOOL-aSwiftRefusal-4 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md) | research | TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md) | research | TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 |
| [2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md) | diff-review | TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 |

<!-- /gen:spec-records -->

## 1. Goal

`verb_dispatch` runs the declared spec-token checker over the whole live tree, about ten minutes on
node a, before the order gate and condition 1, which need only the run-state file and the spec
headers. This unit moves that one block below every refusal those two sources decide, so an
out-of-order or overlapping dispatch is refused in seconds and the checker runs only for a dispatch
nothing cheaper would refuse.

## 2. Scope (IN)

- **S1** — The block headed `aDeferredBar closing review F3 (unit 2)` in `verb_dispatch`
  (`tools/unattended/unattended.sh:14312-14341`) moves, bytes and messages unchanged, to sit after
  condition 1's loop (ends `:14637`) and before the claim read (`:14662-14673`). Every refusal now
  above it is one the run-state file, the spec headers or `git` decide: the order gate, the edge
  shape, cycle and producer refusals, the hold gate, the `--writes` path refusals,
  `refuse_if_terminal`, the shared-record refusals, the generator pairing and condition 1. The
  block comment gains one sentence saying why it sits last. Observed by AC1, AC2, AC3, AC4.
- **S2** — The re-key in `tools/unattended/unarmed-branches.txt`. Moving three `fail 49` sites
  renumbers check 49's ordinals inside `verb_dispatch`, and the file pins by (check, ordinal,
  signature). The sibling malformed-order row moves 21 to 18 and the resolver row 18 to 38. The
  order-gate row at 22 is taken out, because AC2's arm asserts its text, and check-arms reds a
  pinned branch that is armed. The row at 8 sits above the block and keeps its ordinal. A comment
  line beside the rows records the re-key, as the file's earlier re-keys do. Observed by AC5.
- **S3** — The verbs guide's `--dispatch` entry says the spec-token checker runs after the cheap
  refusals and before the claim read, in `tools/unattended/VERBS.template.md:234` and its copy
  `memory/guides/UNATTENDED-VERBS.md:234`, byte-equal past the marker line. Observed by AC6.

## 3. Non-goals (OUT)

- Any refusal's text, its check number or its condition. Each moves with its block or stays put.
- The spec-token checker itself, its launcher resolution and its bounded call.
- The hold gate's own cost: its bounded witness call stays where it is, above the moved block.
- `check_chain_dispatch`, the MISSING and THIN refusals: they already sit above the block.
- The order gate's deferral predicate: TOOL-aSwiftRefusal-2.
- `read_open_passes` releasing a deferred unit's keys: TOOL-aSwiftRefusal-3.
- Arming the sibling malformed-order refusal, which stays pinned. The two-unit fixture AC2 builds
  could arm it; that is a follow-up, not this unit.
- The kit version bump: the lander's `mint` moves it.

### Edges

none

## 4. Design

### Evidence

Read at base `ae6735c1`, the branch tip `52e1f752` carrying no code change over it.

| Line | What sits there |
|---|---|
| `unattended.sh:14288` | `check_chain_dispatch`, then `load_spec_facts`, MISSING and THIN (`:14300-14311`) |
| `:14312-14341` | the spec-token block: `SPEC_TOKENS_CLI` presence, `resolve_python`, `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`, the refusal, and the blank-key announcement |
| `:14342-14385` | the order gate, its two malformed-verb refusals and the out-of-order refusal |
| `:14392-14461` | the edge refusal: roster read, unreadable edges, cycles, producers |
| `:14462-14499` | the hold gate, mandate-conditional |
| `:14500-14524` | the `--writes` path refusals; `refuse_if_terminal` at `:14525` |
| `:14533-14542` | the run-state and shared-record refusals |
| `:14547-14620` | the group key, `read_open_passes`, the empty-set announcement, the generator pairing |
| `:14621-14637` | condition 1 |
| `:14662-14673` | the claim read, "after every local refusal above and BEFORE the row is written" |
| `:14674` | `park "$rel" dispatch`, the row |

The block reads `SPEC_TOKENS_CLI`, `ROOT` and `resolve_python`, and writes only its own locals,
`RB_OUT` and `RB_TOOK`. Nothing below it reads those. So the move changes which refusal arrives
first and nothing else.

### The move

Cut `:14312-14341` whole and paste it between the `SIBS` heredoc's close (`:14637`) and the
`want=""` normalisation (`:14641`). The claim read stays below it: a claim is written only for a
dispatch every local refusal admitted, and the spec-token refusal is a local one. Add one sentence
to the block comment: it runs last among the local refusals because it is the one that costs a
tree-wide scan, and every refusal above it is decided from the run-state file, the spec headers or
`git` in seconds. The comment's other sentences stay true as written.

Two lines that printed after the checker now print before it: the terminal-unit note at `:14390`
and the empty-sibling-set announcement at `:14582`. Both are notes on stderr, and neither changes a
verdict.

### The ordinal re-key

`check-arms.py`'s `branches()` numbers each `fail <n>` site by its source order within check `n`.
At base, check 49's sites inside `verb_dispatch` run 14 to 39, the block holding 17, 18 and 19.
After the move the twenty sites from 20 to 39 shift to 17 to 36, and the block's three take 37,
38 and 39. The pinned rows follow:

| Signature | Base | After |
|---|---|---|
| `cannot hash the brief, so the row would carry no join` | 8 | 8 |
| `a sibling spec status header carries something shaped like the build-order verb…` | 21 | 18 |
| `and an earlier step still holds a unit that is neither terminal nor dispatched` | 22 | armed by AC2, so no row |
| `--dispatch: the inline resolver found no usable python…` | 18 | 38 |

The figures are DERIVED: AC5's probe re-derives them from the source.

### Inventory

This unit mints no identifier.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/unarmed-branches.txt`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Keep the order and cache the checker's verdict.** A cache keyed on the tree still pays the
  full run whenever any spec moved, which is every dispatch after a spec commit. It is also a new
  mechanism that a reorder makes unnecessary.
- **Move the block only below the order gate.** Condition 1 would still wait for the checker, and
  condition 1 refused two of the three dOrderedCharter dispatches the brief cites.
- **Move it below the claim read.** A claim would then be renewed for a dispatch the checker
  refuses, and the claim block's contract is that it runs after every local refusal.

## 5. Production-readiness checklist

- security — no new input, write path or surface; the checker's argv and launcher are unchanged.
- perf / scale — a cheap refusal stops costing a tree-wide checker run, measured by the brief at
  10 to 18 minutes per refusal in dOrderedCharter. A dispatch that is admitted costs the same.
- error / empty / loading states — a blank `SPEC_TOKENS_CLI` still announces its skip, now after
  the cheap refusals; a missing checker or launcher still refuses with its own text.
- observability — every refusal's text is unchanged, so the run log's check numbers and messages
  read as before.
- risks — the ordinal re-key: a wrong ordinal reds the harness-arms leg at the close. AC5 derives
  the ordinals from source before the commit.
- testing — AC1 to AC6, and the two arms on the `New arm:` line in §7.
- migration — N/A: no data or record shape moves.
- user docs — the verbs guide (S3); no page under `help/` describes `--dispatch`.

## 6. Acceptance criteria

- **AC1** — When `grep -nF` runs over `tools/unattended/unattended.sh` for the four anchors
  `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`, `neither terminal nor dispatched:$_blockers`,
  `two passes claiming one file are not disjoint: $p also in` and
  `check_claim_writable "$slug" holder "$_dk"`, the checker's line number is greater than the
  order gate's and condition 1's, and smaller than the claim read's.
  Red when: the block is left above the order gate, or moved below the claim read.
- **AC2** — When `unattended.sh --dispatch tRun --pass ARCH-tRun-5 --writes <path>` runs with
  `SPEC_TOKENS_CLI` naming a stub that exits 1, `ARCH-tRun-5` at order 2 and `ARCH-tRun-4` at
  order 1, SPECCED and never dispatched, the output carries the order gate's
  `an earlier step still holds a unit that is neither terminal nor dispatched: ARCH-tRun-4` and
  not `--dispatch refuses: the declared spec-token checker reds over the live tree`.
  Red when: the spec-token refusal arrives first, as it does at base.
  fixture: the driver suite's `tRun` build after `--preflight`, both units in the README's
  `gen:build-units` region; outside the suite the tree holds none, and a pass builds it in a
  `%TEMP%` repository the way the suite's `mkconf` and `readme` do.
  permission: the suite arm that re-observes this is the main loop's to run at the close.
- **AC3** — When the same fixture dispatches a second unit whose `--writes` path overlaps an open
  sibling's declared path, with the stub still declared, the output carries condition 1's
  `two passes claiming one file are not disjoint` and not the spec-token refusal.
  Red when: the spec-token refusal arrives first, as it does at base.
  fixture: as AC2, with the sibling dispatched first under a blank `SPEC_TOKENS_CLI`.
  permission: as AC2.
- **AC4** — When the same fixture dispatches a unit that every cheap refusal admits, with the stub
  declared, the output carries `--dispatch refuses: the declared spec-token checker reds over the
  live tree` and `RUN.md` gains no `dispatch` row for it.
  Red when: the moved block is deleted, or lands below `park "$rel" dispatch`.
  fixture: as AC2.
- **AC5** — When the probe below runs, loading `check-arms.py` by path and printing each check-49
  branch its `branches()` derives from `unattended.sh`,
  ```
  python -c "import importlib.util as u;s=u.spec_from_file_location('a','tools/memory-tree/check-arms.py');m=u.module_from_spec(s);s.loader.exec_module(m);[print(b['ord'],b['sig'][:50]) for b in m.branches('.','tools/unattended/unattended.sh') if b['num']==49]"
  ```
  the sibling malformed-order signature reads 18 and the resolver signature 38, and
  `grep -P '^unattended.sh\t49\t' tools/unattended/unarmed-branches.txt` prints rows at exactly
  8, 18 and 38, carrying those signatures, and no row carrying `an earlier step still holds`.
  Red when: a pinned row keeps its base ordinal, or the order-gate row stays pinned.
  figure: the ordinals are DERIVED by the probe from the source at observation time.
- **AC6** — When `grep -c "Before any of that it runs the DECLARED spec-token checker"` runs over
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, each prints 0, and
  the two copies past their marker line compare equal, this printing nothing:
  ```
  diff <(tail -n +2 tools/unattended/VERBS.template.md) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md)
  ```
  Red when: either copy still says the checker runs first, or the two copies differ.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · the driver at base ae6735c1, whose spec-token block sits above the order gate, so both arms read the spec-token refusal first · none

The arms sit in region 3 after the F3 spec-token group and before the region's end, set up and
restore their own units, and use a stub checker, so they run where the real checker is absent too.
The close's driver-suite run also re-observes every existing `--dispatch` arm, AC4's case included
as the F3 group's `first line: TOKENS-DIED-ON-STDERR` arm. The suite's floor is a minimum, and
these arms only add to it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.
- rev-2 · 2026-11-10 · the spec-token path hits folded, spelling only (TOOL-aSwiftRefusal-1 of
  the token-fix brief): AC5's inline python probe and AC6's diff command move out of backticks
  into fenced blocks, so no backticked word is the probe's quoted script path, its branches call or
  a path with a close paren glued on; AC5 names the arms checker and its branches function by
  basename in prose.

## 10. Reuse audit

The seam is `verb_dispatch` itself: the unit moves its own spec-token block,
`tools/unattended/unattended.sh:14312-14341`, within the function that already owns it, and
re-keys the existing pin file `tools/unattended/unarmed-branches.txt`. Nothing new is built. The
probe `python tools/codebase-map/reuse_lookup.py "dispatch refusal order spec-token check runs after cheap refusals"`
ranked `run`, `check` and `refusal` by name stem, and `check_landed_facts_due` and
`extract_run_facts` in `tools/unattended/lib-unattended.sh`; none orders refusals, so no other
seam competes. The recall hits
agree with the source: aDeferredBar F3 put the check inside `--dispatch`, and the pin file's
comments record that every `fail 49` inserted above the order gate re-keyed its rows, which is
the class S2 handles. `gotchas.py --for-paths` over the files touched selected
`fixture-passes-by-finding-nothing`, which AC2 and AC3 answer with a positive `hit` beside each
absence, and `staged-break-substitutes-a-synthetic-value`: the stub checker is synthetic on
purpose, because the arms prove refusal order, and the real checker's case stays with the F3 group.

Recall terms used: `python tools/memory-recall/query.py "why does the dispatch verb run the
spec-token check before the order gate and sibling overlap" --terms "dispatch spec-token
SPEC_TOKENS_CLI order gate condition 1 sibling overlap refusal run_bounded aDeferredBar F3"`
