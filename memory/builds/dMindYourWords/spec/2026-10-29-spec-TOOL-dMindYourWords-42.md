# TOOL-dMindYourWords-42 — the kit's blame clears every ambient ignore-revs list, so a row stays on the commit that wrote it

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 9 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-42-deviation-421.md](../build/2026-10-29-build-TOOL-dMindYourWords-42-deviation-421.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, item H6. TOOL-dMindYourWords-30 pins the provenance blame against replace refs and graft files,
but git blame also honours `blame.ignoreRevsFile`, commonly set beside a committed
`.git-blame-ignore-revs`. A commit listed there that rewrites an admitted suppression row to suppress a
different site is blamed to the earlier commit, whose record admits it: a wrong green on the
provenance join. The drift blame re-dates lines the same way. This unit clears every ignore list on the
kit's blame, so blame always names the commit that wrote the line.

## 2. Scope (IN)

- **S1** — The cleared list. The provenance blame of `check_suppression_provenance`
  (TOOL-dMindYourWords-30 S1) passes `--ignore-revs-file=` in its argv, the empty value that clears
  every list `blame.ignoreRevsFile` or an earlier flag configured, beside the pin unit 30 adds. A
  configured ignore list then moves no row. Observed by AC1.
- **S2** — The rule for every blame of the kit. The kit's blame argv carries `--ignore-revs-file=` and
  `--ignore-rev` is never passed, so when TOOL-dMindYourWords-29 S42 makes `read_blame_lines` the one
  blame reader and TOOL-dMindYourWords-31 S2 respells its argv under the kit's pin, the flag travels
  with it into the drift blame. Observed by AC2.

## 3. Non-goals (OUT)

- The replace-ref and graft-file pin: TOOL-dMindYourWords-30 and -31.
- Other ambient configuration that changes blame's attribution (`blame.markIgnoredLines`,
  `blame.markUnblamableLines`): both only mark lines an ignore list already moved, so clearing the
  list removes their effect.
- The checklist entry the report names under H6: a checklist is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-30` — the pinned provenance blame whose argv S1 extends
- **hands-off** `TOOL-dMindYourWords-29` — `--ignore-revs-file=` on the provenance blame, which S42's `read_blame_lines` keeps when it becomes the kit's one blame reader
- **hands-off** `TOOL-dMindYourWords-31` — `--ignore-revs-file=` in `read_blame_lines`' argv, which S2's pinned respelling keeps

## 4. Design

### Evidence

- Unit 30 S1 spells the provenance blame `git --no-replace-objects blame --porcelain --root --
  <registry>` with `GIT_GRAFT_FILE=/dev/null` (`spec/2026-10-29-spec-TOOL-dMindYourWords-30.md` S1);
  unit 31 S2 respells `read_blame_lines` the same way (`spec/2026-10-29-spec-TOOL-dMindYourWords-31.md`
  S2); neither names an ignore list.
- Measured on git 2.54.0 in a fixture under `%TEMP%`: commit w1 wrote `site-a r` and w2 rewrote it to
  `site-b r`; with `blame.ignoreRevsFile` naming w2, `GIT_GRAFT_FILE=/dev/null git --no-replace-objects
  blame --porcelain --root -- reg.txt` attributed the line to w1, and adding `--ignore-revs-file=`
  attributed it to w2. PINNED 2026-10-29, matching the report's reproduction.

### The argv

```
git --no-replace-objects blame --porcelain --root --ignore-revs-file= -- <registry>   # env GIT_GRAFT_FILE=/dev/null
```

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-30, beside TOOL-dMindYourWords-40 and -41.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **`-c blame.ignoreRevsFile=` before the subcommand**: it blamed normally when measured on 2026-10-29,
  but it is a global option where the flag is the blame's own, and AC2 reads the blame's argv per call;
  one spelling, the one beside the command it changes.
- **Refusing provenance when an ignore list is configured**: it reds every adopter who keeps a
  `.git-blame-ignore-revs` for formatting commits, where the cleared list reads their real history.

## 5. Production-readiness checklist

- security — deny by default holds: no configured list can re-attribute a suppression row to a commit
  whose record admits it.
- perf / scale — none: one argv element.
- error / empty / loading states — unchanged; a blame that fails still reds `cannot judge provenance —
  <why>`.
- observability — the refused row names the commit that wrote it, the one an adopter can inspect.
- risks — drift dates on a node that set an ignore list for formatting commits move to those commits;
  that is the true writer of the line, and the drift signal is a measure, not a verdict.
- testing — AC1, AC2 and the arm of §7.
- migration — none.
- user docs — N/A — TOOL-dMindYourWords-30 S3's README sentence states provenance reads the real
  history; an ignore list is part of what that excludes.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a fixture whose first commit adds a
  `unit.lexicon.suppressions` record and a suppression row for site a, whose second commit rewrites
  that row to suppress site b with no record, and whose `blame.ignoreRevsFile` names the second commit,
  it exits 1 naming `SUPPRESSION WITHOUT PROVENANCE` and the second commit's sha8.
  Red when: the row is blamed to the first commit, whose record admits it, and the run exits 0.
  fixture: the repository under `%TEMP%/<short>`, `git config blame.ignoreRevsFile .git-blame-ignore-revs`.
- **AC2** — When `git grep -n -e '"blame"' -- tools/lexicon/lexicon.py` lists the kit's blame spawns after
  the pass, each listed call's argv carries `"--ignore-revs-file="`, read with `git grep -n -A4`.
  Red when: a blame spawn of the kit omits the flag.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · a fixture whose `blame.ignoreRevsFile` names the row-rewriting commit, its failing case `--ignore-revs-file=` cut from the blame argv, under which the row is admitted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 30 (HIGH, item H6) of the round-1 audit of
  units 30 to 37, with the cleared list measured.

## 10. Reuse audit

The seam is the pinned blame TOOL-dMindYourWords-30 S1 adds and TOOL-dMindYourWords-29 S42 shares as
`read_blame_lines`; this unit adds one argv element to it. `python tools/codebase-map/reuse_lookup.py
"clear ambient git blame configuration before attributing a line"` ranked generic git readers and no
blame wrapper that clears an ignore list anywhere in the tree (`git grep -n 'ignore-revs' -- tools`
prints nothing at base), so no existing seam fits beyond the reader this unit extends.

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader stay honest when replace refs graft a commit onto no parent" --terms "graft replace no-replace-objects blame porcelain root boundary provenance ignore-revs blameIgnoreRevsFile attribution"`
