# TOOL-dLinkedLibrary-101 — the raw blob read's two arms each fail on their own staged break

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 38 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-101-deviation-1011.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-101-deviation-1011.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
finding **id 29 at HIGH**, report item **H2**. Id 10 shares the item and is its own unit,
`TOOL-dLinkedLibrary-98`.

Id 29 is the failure-envelope half of the item. `TOOL-dLinkedLibrary-96` AC8's red clause, "the raw mode
decodes or folds, or the default changes for an existing caller", names two breaks and stages neither.
Its "folds" arm cannot fire over a blob git already folded, and its "default changes" arm reads only a
blob holding `FF`, for which the default path returns None whether it decodes, folds or does neither. On
this repository's Windows nodes neither arm of AC8 is ever seen red.

This unit stages each arm's break against the blob unit 98 proves: a copy of `read_blobs_at` whose raw
branch folds CR LF must fail 98's compare, and a second blob without `FF` makes the default path's decoded,
folded text observable, so a default that changed fails too. It repairs `TOOL-dLinkedLibrary-96` and
builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The folding red. A scratch copy of `tools/memory-tree/tree_lib.py` whose `raw` branch returns
  the body with `.replace(b"\r\n", b"\n")` applied, imported in place of the real module by `python -I`
  with the copy's directory first on `sys.path`, runs unit 98's probe over 98's blob; the probe prints a
  mismatch naming `cr=0` against the three CRs written and exits non-zero. Observed by AC1.
- **S2** — The decoding red. A second scratch copy whose `raw` branch returns `body.decode("utf-8",
  "replace")` runs the same probe, which prints a mismatch naming the type returned, `str` for `bytes`.
  Observed by AC1.
- **S3** — The default arm, made discriminating. A second blob, written filter-free and proved by 98 S1
  and S2, holds `EF BB BF`, `jobs:\r\n` and `  t:\r\n` with no `FF`. `read_blobs_at` without `raw` returns
  for it the text `"\ufeffjobs:\n  t:\n"`, the default path's strict decode with CR LF folded and the BOM
  kept, exactly as `tree_lib.py:364` gives it today; for 98's `FF` blob it returns None. Observed by AC2.
- **S4** — The default red. A scratch copy whose default path no longer folds CR LF returns
  `"\ufeffjobs:\r\n  t:\r\n"` for S3's blob, and the probe exits non-zero naming the default arm.
  Observed by AC2.
- **S5** — The record. 96's acceptance ledger carries an amendment line citing this unit, recording AC8's
  two arms each seen red on its staged copy. Observed by AC3.

## 3. Non-goals (OUT)

- How the blob keeps its CRs and the precondition before the read: id 10, `TOOL-dLinkedLibrary-98`.
- Changing `read_blobs_at`: 96 S8 builds `raw`; the staged copies live under the run's scratch root and
  are deleted after the read.
- A repo-wide check that a staged red exists for every arm a red clause names: the report's left-shift
  class, a separate mechanism.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-96` — S8's `raw` keyword and AC8's red clause, whose two named breaks S1 to S4 stage (id 29)
- **consumes-from** `TOOL-dLinkedLibrary-98` — S1's filter-free blob and S2's precondition, which S1 and S3 read the staged copies against (id 29)

## 4. Design

### Evidence

- `tools/memory-tree/tree_lib.py:364` is `out[(rev, path)] = body.decode("utf-8").replace("\r\n", "\n")`,
  inside a `try` whose `except UnicodeDecodeError` stores None (`:365-366`); the codec is `utf-8`, so a
  leading U+FEFF is kept.
- 96 AC8 (`2026-10-27-spec-TOOL-dLinkedLibrary-96.md`, AC8) reads one blob holding `FF`, for which the
  default path returns None under every variant of the decode.
- The report's skeptic showed on this node that a plain `git add` under the inherited `core.autocrlf=true`
  drops every CR of such a blob (finding id 29).

### The four reads

| Copy of `tree_lib.py` | 98's `FF` blob, `raw=True` | S3's blob, no `raw` | Verdict |
|---|---|---|---|
| the real module | the written bytes, `cr=3` | `"\ufeffjobs:\n  t:\n"` | held |
| raw branch folds (S1) | bytes, `cr=0` | as real | red, raw arm |
| raw branch decodes (S2) | a `str` | as real | red, raw arm |
| default stops folding (S4) | as real | `"\ufeffjobs:\r\n  t:\r\n"` | red, default arm |

### Rollout

Order 38, one step after `TOOL-dLinkedLibrary-96`, after `TOOL-dLinkedLibrary-98`'s pass, whose blob it
reads. The pass writes no product code: it runs the four reads by `python -I -c` under a short absolute
scratch root and writes S5's line.

### Files touched (estimate)

- `memory/builds/dLinkedLibrary/build/`: S5's amendment line and this unit's acceptance ledger

### Alternatives rejected

- **A selftest arm in `tree_lib.py`'s callers.** `deviation_join.py`'s `check_blob_reader` grades the
  join's reader, not `raw`; a durable arm for one keyword's two arms is scaffolding no later unit reads.
- **Dropping the `FF` byte from 98's blob.** It loses the case 96 S9 exists for, a non-UTF-8 file the raw
  read must still return; S3 adds a blob instead.

## 5. Production-readiness checklist

- security — keeps the raw read the census's CR scan depends on from passing while it folds.
- perf / scale — four reads over two blobs.
- error / empty / loading states — each staged copy exits non-zero naming its arm.
- observability — the probe names the arm and the CR count or type it read.
- risks — none beyond the probe: no product code changes.
- testing — AC1 to AC3 by the probe, its staged copies and a ledger grep.
- migration — none.
- user docs — none under `help/`: no behaviour changes.

## 6. Acceptance criteria

- **AC1** — When the probe runs by `python -I` against S1's folding copy and then S2's decoding copy of
  `tree_lib.py`, each run exits non-zero over 98's blob, the first naming `cr=0` and the second naming a
  `str` return, while the real module prints `cr=3`.
  Red when: a copy whose raw branch folds or decodes passes the compare.
- **AC2** — When the probe reads S3's blob without `raw`, the real module returns `"\ufeffjobs:\n  t:\n"`
  and S4's copy returns text holding `\r`, and the run over S4's copy exits non-zero naming the default
  arm.
  Red when: the default arm reads only a blob for which every variant returns None.
- **AC3** — When `grep 'TOOL-dLinkedLibrary-101'` runs over 96's acceptance ledger, it prints the line
  recording AC8's raw and default arms each seen red.
  Red when: AC8 stands answered with no arm ever seen red.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, id 29 (HIGH, item
  H2, which id 10 shares).

## 10. Reuse audit

The seam extended is 96 AC8's probe of `read_blobs_at` (`tools/memory-tree/tree_lib.py:328`), as unit 98
corrects its blob. `python tools/codebase-map/reuse_lookup.py "write a git blob without line ending
conversion"` ranked `git`, `write`, `write_text` and `run_git`, none a staged-copy harness for a module,
so no existing seam fits beyond the probe; the staged copies are scratch files of one run.

Recall terms used: `python tools/memory-recall/query.py "how does a scratch repository keep crlf bytes for a raw blob read" --terms "read_blobs_at raw crlf autocrlf scratch repository hash-object no-filters cat-file od precondition"`
