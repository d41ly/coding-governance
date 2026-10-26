# TOOL-dTotalRecall-58 — the census keep marker is honoured only under the tool root, so no pass writes it into a pinned instrument

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**. It shares item **H1** with ids 4, 15 and 37, which
`TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-56` and `TOOL-dTotalRecall-55` close. Built as written,
`TOOL-dTotalRecall-53` S34 and S22 have the pass write `# census: kept` into the files it keeps. The
packet pins `asbuilt.py` at `97c8f8fb`, `deviations.py` at `30a1f15b` and `packet.py` at `20a7319c`
(`memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, its Pins
list), and `git hash-object` printed those blobs at base `462d20f3`. README:38-39 makes a moved
instrument blob a stop, never re-rendered away. So the run either stops at `packet.py --check` or
cannot keep those files. Units 55 to 57 give such files a keep outside their bytes. Nothing yet stops
a pass from writing the marker into one anyway, and the census would honour it. This unit makes
the marker reader refuse a marker outside the tool root and observes that no instrument blob moved.
It repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The marker's domain. The marker reader S34 builds, which `check_cause_writers` and
  `check_alias_compares` call, honours `# census: kept <census> <reason>` only in a file under
  `tools/`. A marker in any other file the census reads is a red finding naming the file and line,
  with the remedy `keep it by a CENSUS_KEPT_PATHS row; its bytes are not this build's`. Observed by
  AC1.
- **S2** — The instruments' bytes held. At the pass tip no tracked `memory/builds/*/build/*.py`
  differs from base `462d20f3`, and `packet.py --check dTotalRecall` exits 0, so S34, S22 and units
  55 to 57 moved no instrument blob. Observed by AC2.

## 3. Non-goals (OUT)

- The keep table and its rows: units 55, 56 and 57.
- The marker's grammar and its reader under `tools/`: `TOOL-dTotalRecall-53` S34's.
- The slug census's marker: its population is the tool root alone, so no file it reads sits outside
  `tools/`.
- Moving a pin: only the owner's `packet.py --repin` does.

### Edges

- **consumes-from** `TOOL-dTotalRecall-53` — S34's marker reader and S22's widened alias population,
  whose marker this unit bounds to the tool root
- **hands-off** `TOOL-dTotalRecall-66` — the marker's domain and AC2, which that unit sets per census, tests against the derived tool root and reads over this run's own commits (the round-1 audit of units 54 to 60, ids 12, 15, 18, 28 and 43)

## 4. Design

### The rule

The reader checks the path before it reads the line: a hit's file not under `tools/` never reaches
the marker test, and a marker found in it is reported rather than honoured. The one population this
excludes is the build folders' scripts, which `CENSUS_KEPT_PATHS` keeps.

### Inventory

Minted: the fixture plant `marker-in-build-script` in `record_causes.py --fixture`. Naming cell:
none, no function being minted.

### Files touched (estimate)

- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/tree_lib.py`

`TOOL-dTotalRecall-55`, `-56` and `-57` also write these modules at order 30, so BUILD-METHOD M6
sequences the passes.

### Alternatives rejected

- **Read the pinned paths from `packet.py`'s `INSTRUMENTS` and refuse a marker only there.** The five
  unpinned build-folder scripts are outside this build's write set too, so a list of pins is the
  narrower rule and the folder is the README's.
- **Observe the bytes only, with no refusal.** A marker written into an unpinned script in another
  build's folder moves no pin and `packet.py --check` stays green, so only the refusal catches it.

## 5. Production-readiness checklist

- security — narrows a keep: a file outside the tool root can no longer exempt itself.
- perf / scale — one prefix test per hit.
- error / empty / loading states — a marker outside the tool root is a red finding naming the line.
- observability — the finding prints the file, line and remedy.
- risks — none beyond S1: the build folders are kept by the table, so no honoured keep is lost.
- testing — AC1 and AC2 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --fixture --plant marker-in-build-script` runs from
  `tools/memory-tree/` and builds a fixture whose build-folder script carries `# census: kept check_cause_writers x` on its
  Serves line, `--check` exits 1 naming that file and line.
  Red when: the marker keeps a file outside the tool root.
- **AC2** — When `git diff --stat 462d20f3..HEAD -- 'memory/builds/*/build/*.py'` runs at the pass tip it
  prints nothing, and `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check dTotalRecall`
  exits 0.
  Red when: a pass wrote into a build-folder script, or an instrument blob moved.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/record_causes.py · covers AC1 · the plant `marker-in-build-script`, staged by skipping the path test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 24
  (HIGH, item H1 shared with ids 4, 15 and 37).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is the marker reader `TOOL-dTotalRecall-53` S34 builds, the one place both censuses
test a keep marker, and the observation reuses the packet instrument's own `--check`
(`packet.py:90-94` lists what it pins). `python tools/codebase-map/reuse_lookup.py "keep a census hit in a file that cannot be edited"`
ranked name-stem neighbours and no path bound on a keep marker, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
