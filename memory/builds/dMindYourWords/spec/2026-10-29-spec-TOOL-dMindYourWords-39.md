# TOOL-dMindYourWords-39 — check 7c2 refuses a graded leg whose argv names no file it can read

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 4 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 33 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H5 with id 7 (TOOL-dMindYourWords-38). Check 7c2 counts a leg as graded when it
merely carries a guard, then silently reads no argv file for it, so a leg 7c2 cannot read is reported
in `guarded bar legs graded <n>` exactly as one it judged. Its only liveness arm fires at zero graded
legs, which a manifest of unreadable legs never reaches. TOOL-dMindYourWords-34's own fixture spelled
a resolved argv path, the synthetic value the real manifest never spells, and no arm noticed. This unit
makes a graded leg with no readable argv file a refusal, so the class of leg 7c2 skips is named rather
than counted as coverage.

## 2. Scope (IN)

- **S1** — The per-leg refusal. When check 7c2 grades a leg (guarded, not `subject = kit`, not `chunk =
  selftests`) and, after TOOL-dMindYourWords-38's resolution, none of its argv elements is a tracked
  file, the check fails with `leg '<name>' names no argv file check 7c2 can read, so its root-conf
  reads are ungraded — its argv: <argv>`. Observed by AC1 and AC2.
- **S2** — The count says what was read. The note line becomes `guarded bar legs graded <n> · argv
  files read <n> · root-conf readers <n>`, so a reader of the bar log sees how many legs were actually
  inspected. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The `{prefix}` resolution itself: TOOL-dMindYourWords-38 (id 7).
- A leg whose argv names a file through an interpreter flag (`python -m`, `bash -c`): no leg 7c2
  grades spells one at base, and S1 refuses such a leg by name, which is the intended deny-by-default
  answer until a reader for that form exists.
- The checklist entry the report names under H5: a checklist is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-38` — the resolved argv read; without it seven of gov's eight graded legs name no readable file and S1 reds the bar

## 4. Design

### Evidence

- 7c2 increments `graded` for every guarded, non-kit, non-selftest leg before it reads any argv file,
  and its one liveness refusal fires only when `graded == 0` (`tools/govkit/govkit.py:2608-2657`).
- Of the 8 legs 7c2 grades at base, 7 spell their argv file `{prefix}/…` and are read by no element
  before TOOL-dMindYourWords-38; after it, all 8 are read (simulation over `tools/gate-legs.json`,
  PINNED 2026-10-29). So S1 is red on gov's real manifest before unit 38 and green after it, which is
  the observation the report asked for.
- The 7c2 arms read the note line by literal text (`tools/govkit/selftest.py:6224`, `:6227`, `:6232`).

### The rule

```
for leg in graded legs:
    argv_files = [resolved argv elements in tracked_set]          # TOOL-dMindYourWords-38
    if not argv_files: fail("leg '<nm>' names no argv file ...")   # S1
    else: read += 1
note("guarded bar legs graded <g> · argv files read <read> · root-conf readers <r>")  # S2
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `names no argv file check 7c2 can read` | refusal line | none |

### Rollout

Live at landing, after TOOL-dMindYourWords-38 at the same order, which sorts first; on gov's tree every
graded leg is then read, so the first bar stays green.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: the existing note-line assertions and the arm of §7

### Alternatives rejected

- **A selftest arm over gov's manifest requiring a nonzero read count**, the report's left-shift
  form: at base that count is 1, not 0, so the arm would pass on the defect it is written for.
- **A note instead of a failure**: a skipped leg printed as a note is the skip-wearing-a-pass's-clothes
  shape 7c2's own liveness comment refuses.

## 5. Production-readiness checklist

- security — N/A — a classifier over the deployer's own manifest; no write path or surface.
- perf / scale — none: one comparison per graded leg.
- error / empty / loading states — S1 is the empty state of one leg, named; the zero-graded refusal
  stays for the empty manifest.
- observability — S2's count and S1's line, which names the leg and its argv.
- risks — a future leg whose argv names its script through a flag reds until its form is read; the
  line names the leg, so the remedy is plain.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — govkit's internal check.

## 6. Acceptance criteria

- **AC1** — When `python <prefix>/govkit/govkit.py selfcheck` runs in a scratch gov tree whose one graded
  leg has argv `["python", "{prefix}/demo/missing.py"]`, an untracked path, it exits 1 printing `names
  no argv file check 7c2 can read` and the leg's name.
  Red when: the leg is counted as graded and the run exits 0.
  fixture: a scratch gov tree under `%TEMP%/<short>`, the planted break S1's branch cut out.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs on gov's own tree after the pass, it
  exits 0 and prints `argv files read` followed by the same number `guarded bar legs graded` prints.
  Red when: a graded leg of gov's manifest is skipped unread.
  figure: DERIVED at observation; 8 and 8 by the simulation in §4.
- **AC3** — When `git grep -n 'root-conf readers' -- tools/govkit/selftest.py` runs after the pass, every
  line it prints also carries `argv files read`.
  Red when: an existing 7c2 arm still matches the old note line and goes stale.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures`

New arm: tools/govkit/selftest.py · covers AC1 · a scratch leg whose argv names an untracked `{prefix}/demo/missing.py`, its failing case S1's branch cut, under which the leg is counted graded and the run exits 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 33 (HIGH, item H5, shared with id 7) of the
  round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is 7c2's own liveness refusal (`tools/govkit/govkit.py:2651-2657`), which already refuses a
probe that grades nothing; S1 applies that rule per leg. `python tools/codebase-map/reuse_lookup.py
"refuse a check that graded an item it could not read"` ranked generic readers and no per-item
liveness helper in govkit, so no existing seam fits beyond the function this unit changes.

Recall terms used: `python tools/memory-recall/query.py "how does govkit classify a guard pathspec naming a root file a kit owns" --terms "root-conf guard pathspec class derive_root_confs 7c 7c2 selfcheck argv prefix token resolve"`
