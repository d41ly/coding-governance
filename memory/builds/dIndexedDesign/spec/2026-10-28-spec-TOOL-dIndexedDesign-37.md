# TOOL-dIndexedDesign-37 — one write-set path predicate, `check_meet_path`, that keeps root files, so the stream plan and the build order refuse two writers of one root file

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 16 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md) | research | TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-38 |
| [2026-10-28-build-TOOL-dIndexedDesign-37-deviation-371.md](../build/2026-10-28-build-TOOL-dIndexedDesign-37-deviation-371.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-38 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-37-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-37-1-spec-writer.md) | journal | — |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 39 at HIGH**, report item **H4**, the item's only id. `TOOL-dIndexedDesign-15`
S1 lifts `derive_parallel_step`'s inline filter, "words of two or more non-empty segments"
(`tools/memory-tree/gen_build_index.py:1732-1734`), into `derive_write_meet`. That filter drops every
root-level file: over this build's specs it removes `.memory-tree.conf` from units 4, 6, 8 and 9,
though `check_writes_intersect(['.memory-tree.conf'], ['.memory-tree.conf'])` is True. So unit 15's
arm (c) passes a plan that runs units 6 and 8 in two streams while both write that file.
`TOOL-dIndexedDesign-2` S1 reads a token as a path when it carries a `/` or an extension, so the set
holds two path rules.

This unit defines the one predicate, `check_meet_path`, in `design_lib.py`, and makes
`derive_write_meet` filter by it, so the planner and the build-order region refuse a root-file meet.
Report id 23, the same defect seen from unit 2, is a MEDIUM batched into `TOOL-dIndexedDesign-38`,
which points unit 2's `--overlaps` at this predicate. This unit repairs `TOOL-dIndexedDesign-15` and
builds one step after it, at order 16.

## 2. Scope (IN)

- **S1** — The predicate. `check_meet_path(tok)` in `tools/memory-tree/design_lib.py`, beside
  `check_writes_intersect` (`:601`), returns True when a write-set token names a path two write sets
  can meet on, else False:
  - a token holding a space, `*` or `?`, or one `NOT_A_TOKEN` matches, is False;
  - a `/`-terminated token is True only when `check_dir_shaped` holds, so a one-segment directory such
    as `tools/` declares nothing;
  - any other token holding `/` is True when no segment is empty, `.` or `..`;
  - a token with no `/` is True when it holds a `.` and is not `.` or `..`, so a root file, a dotfile
    such as `.gitattributes` included, is a path.

  Observed by AC1.
- **S2** — The meet. `derive_write_meet(a, b)` (unit 15 S1) filters both write sets by
  `check_meet_path` in place of the two-segment rule, so `derive_parallel_step` and
  `plan_streams.py check`'s arm (c) read one rule. Observed by AC2 and AC3.
- **S3** — Verdicts that change, stated. Unit 15 S1's "its verdicts unchanged" and AC8's red-when are
  superseded: `derive_parallel_step` now also reads a step whose units meet only on a root file as
  `no`. Each build README whose `gen:build-order` step flips is re-rendered in this pass, and the
  pass names each flipped step. Observed by AC4.
- **S4** — The fixture cases. `plan_streams.py --fixture` gains `--plant pair-root-file`, two units
  in two streams both estimating `.memory-tree.conf`, on which `write` exits 1 naming arm (c) and the
  path; and its `parallel-step` plant gains a step whose units meet only on a root file, read `no`.
  Unit 15's ledger records, under its `- AC8` answer, the label `TOOL-dIndexedDesign-37 S3` and the
  backticked `check_meet_path` token on that one physical line. Observed by AC2, AC3 and AC5.

## 3. Non-goals (OUT)

- Unit 2's `--overlaps` filter and its F4: report id 23, in `TOOL-dIndexedDesign-38`, which calls this
  predicate.
- `check_writes_intersect` and `check_guard_trips`: unchanged; S1 filters what reaches them.
- A dotted token that is not a file, a policy key such as `design.forks` named in a Files touched
  line: S1 reads it as a path, so two specs naming one key meet. That residual is the price of keeping
  root files, and §4 says so.
- The report's left-shift text, a checklist entry for C33; this unit's AC2 and AC3 are its fixture.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-15` — `derive_write_meet`, arm (c) of `check_stream_pairing`, the `plan_streams.py --fixture` plants and AC8, whose two-segment filter S2 replaces with `check_meet_path` and whose "verdicts unchanged" S3 supersedes (id 39)
- **hands-off** `TOOL-dIndexedDesign-38` — `check_meet_path`, the one write-set path predicate that unit's id-23 item points unit 2's `--overlaps` filter at, so the three joins give one answer on a root file
- **hands-off** `TOOL-dIndexedDesign-46` — S1's `check_meet_path`, which that unit gives an optional tracked-file set so the spec-token join calls it too (id 21)

## 4. Design

### Evidence

- `tools/memory-tree/gen_build_index.py:1732-1743`, read 2026-10-28: `pathlike` keeps a word only when
  `len(parts) >= 2 and all(parts)`, then `derive_parallel_step` calls `check_writes_intersect` over
  the filtered sets.
- `tools/memory-tree/design_lib.py:579-586` `check_dir_shaped` (two or more real segments) and
  `:601-605` `check_writes_intersect`, read 2026-10-28.
- A read-only probe on 2026-10-28 ran `read_spec_writes` over every spec named in a `yes` step of every
  build README's `gen:build-order` region, under the old filter and under S1. One step flips:
  aRepatriatedFork step 17, where TOOL-aRepatriatedFork-32 and TOOL-aRepatriatedFork-47 both name
  `WIRE-INTO-PROJECT.md`. PINNED on 2026-10-28; AC4 re-derives the set at the pass.

### What it does not check

A dotted token that names no file passes S1, and a file with neither a `/` nor a `.` in its name,
`Makefile` say, is still dropped. Both are rare in a Files touched estimate; the second is the class
the old filter dropped wholesale.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_meet_path` | Python function, `design_lib.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `pair-root-file` | fixture plant, `plan_streams.py` | none |

### Migration

The build-order regions S3 names re-render; no authored record changes.

### Rollout

Live at its pass, order 16, one above unit 15's 15, beside `TOOL-dIndexedDesign-3`, whose write set
holds neither `design_lib.py` nor `plan_streams.py`.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1, S2
- `tools/memory-tree/plan_streams.py`: S4's plants
- `tools/memory-tree/gen_build_index.py`: the selftest arm §7 declares
- `memory/builds/aRepatriatedFork/README.md`: S3's re-rendered region, as measured
- `memory/builds/dIndexedDesign/build/`: S4's ledger note, at the close

### Alternatives rejected

- **Keep the two-segment rule and add root files by name.** Lost to the probe: the population is
  every root file a spec may estimate, and a list is a second fact beside the filter.
- **The finder's fix, the predicate with S1's verdicts held unchanged.** Lost to the skeptic's reading:
  `derive_parallel_step` calls `derive_write_meet`, so changing the filter must change a verdict, and
  holding them unchanged contradicts the fix.

## 5. Production-readiness checklist

- security — N/A: no write path; a read-time filter.
- perf / scale — one predicate call per token.
- error / empty / loading states — an empty write set meets nothing; an undeclared one stays
  `unknown` as unit 15 S3 (d) and `derive_parallel_step` read it.
- observability — arm (c)'s finding names the meeting path, a root file included.
- risks — a build-order step flips from `yes` to `no`; S3 names each flip, and `--dispatch` decides
  either way.
- testing — AC1 to AC3 by fixture and `python -c`, AC4 by re-render, AC5 at the close.
- migration — the flipped regions re-render.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` calls `design_lib.check_meet_path` over `.memory-tree.conf`,
  `README.md`, `.gitattributes`, `tools/memory-tree/design_lib.py`, `tools/x/`, `tools/`, `src/*.py`
  and `../x`, it returns True for the first five and False for the last three.
  Red when: a root file reads False, or a one-segment directory reads True.
- **AC2** — When `python plan_streams.py --fixture <dir> --plant pair-root-file` runs and its `write`
  verb is called on that plan, it exits 1 naming arm (c), both units and `.memory-tree.conf`.
  Red when: the plan writes with both units in two streams.
- **AC3** — When the `parallel-step` plant's root-file step is passed to
  `gen_build_index.derive_parallel_step`, it returns `no`, and `design_lib.derive_write_meet` returns
  the pair on `.memory-tree.conf`.
  Red when: the step reads `yes`.
- **AC4** — When `python gen_build_index.py --check` runs at this unit's pass tip, it reports no stale
  `gen:build-order` region, and the aRepatriatedFork README's step 17 reads `no`.
  Red when: a flipped region is left stale.
  figure: the flipped set is DERIVED at the pass by the §4 probe; it held one step on 2026-10-28.
- **AC5** — When `grep -n "TOOL-dIndexedDesign-37 S3"` runs over unit 15's acceptance ledger at the
  close, it prints one line holding `check_meet_path`, under the `- AC8` answer.
  Red when: unit 15 AC8 is answered on "verdicts unchanged".
  permission: the ledger is written at the close.

## 7. Gates

`policy fixtures` · `build-index selftest` · `tier2-review self-test` · `memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC2 AC3 · the `plan_streams.py --fixture` cases `pair-root-file` and the root-file `parallel-step`, staged by restoring the two-segment filter in `derive_write_meet` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 39
  (HIGH, item H4), on the skeptic's corrected fix, repairing TOOL-dIndexedDesign-15 S1, S3 (c) and
  AC8.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-46, promoted by the round-1 spec audit of units 31 to 38; nothing else
  moved.

## 10. Reuse audit

The seams are `design_lib.py`'s `check_dir_shaped` (`:579`), which S1 reuses for a directory token,
and `check_writes_intersect` (`:601`), which S1 filters for; unit 15's `derive_write_meet` is the one
caller S2 changes. The probe
`python tools/codebase-map/reuse_lookup.py "decide whether a write-set token declares a file path"`
ranked `write`, `write_text`, `resolve_prefix_token` and `declares`, none a
write-set token predicate, so no existing seam fits beyond the two named, each verified at base.

Recall terms used: `python tools/memory-recall/query.py "how is a write-set token read as a path for overlap" --terms "write set token path predicate root file pathlike two segments check_dir_shaped check_writes_intersect derive_parallel_step overlap"`
