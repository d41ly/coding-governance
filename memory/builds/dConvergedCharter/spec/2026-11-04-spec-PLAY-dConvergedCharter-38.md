# PLAY-dConvergedCharter-38 — the memory root's live carriers declared once in the dead-path gate and read by the reader inventory, so a retirement's inventory names a dossier or gotcha still citing the retired path

**Status:** DEFERRED · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 3 · advances PLAY-dConvergedCharter-24

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-04-build-PLAY-dConvergedCharter-38-deviation-381.md](../build/2026-11-04-build-PLAY-dConvergedCharter-38-deviation-381.md) | deviation | — |
| [2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-39 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's 23 specs
(`memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md`)
confirmed finding **id 45 at MEDIUM**, report item **M26**, and named it the root of items M23, M24 and
M25 (ids 41, 43 and 44). PLAY-dConvergedCharter-11 S6 builds `derive_readers`, the shared reader
inventory (I1) that units 3, 9, 12, 16, 17 and 21 treat as complete when it exits clean, over every
tracked text file outside the memory root. The dead-path gate grades two folders under the memory root
as live carriers, the map dossiers and the gotcha pages (`tools/check-dead-paths.sh:57-62`, its haystack
at `:192-197`), and the codebase-map legs grade the dossiers' claims. So a retiring unit's clean inventory
misses a carrier that later reds the bar. This unit closes the finding with one declaration of the live
carriers, owned by the dead-path gate, which `derive_readers` reads, never a typed copy beside it. It is
one unit for one MEDIUM finding because its write set, the gate and the policy kit's inventory, is
disjoint from PLAY-dConvergedCharter-39's dossiers (BUILD-METHOD M6), and it lands right after the unit
it repairs, at order 3, strictly before the first retiring units that read the inventory, units 12 and
17 at order 4, so every later inventory reads the widened walk.

## 2. Scope (IN)

Build-run precondition: PLAY-dConvergedCharter-11 S6 has landed `derive_readers` and its `--readers`
CLI in `tools/policy/check_policy.py`.

- **S1** — id 45, the one declaration. `tools/check-dead-paths.sh` holds the live carriers as one array,
  `LIVE_CARRIERS=('memory/map/features/*' 'memory/gotchas/*')`, and a new mode `--carriers` prints its
  members one per line and exits 0. The haystack's second `git grep` (`:197`) reads the array in place
  of its two literal pathspecs, so the gate and every reader of `--carriers` read one list. The mode
  joins the usage line and the `case` of `:111-112`, but it is parsed and answered before any git call:
  ahead of the git-repo check (`:75`) and of `tracked=$(git ls-files)` and the history walk
  (`:117-121`), so `--carriers` prints the array and exits 0 in a tree with no history, no deletion and
  no sentinel, never coupled to a full-history `git log`. Observed by AC1, AC2 and AC4.
- **S2** — id 45, the inventory reads it. `derive_readers(repo, needle, kind)` gains a second walk:
  beside every tracked text file outside the memory root, it walks the pathspecs `read_live_carriers(repo)`
  returns. It runs the script `<repo>/<derive_tool_root()>/check-dead-paths.sh`, the tool root being the
  one `budgets.derive_tool_root` (`tools/policy/budgets.py:100`) derives, a module `check_policy.py`
  already imports (`:212`), with cwd `<repo>`, the repository under inventory, so a fixture's own copy is
  the one read. The argv is `[resolve_bash(script), script, '--carriers']`, the bash found by
  `check_policy.resolve_bash` (`check_policy.py:896`, the inline copy of `tools/lib/resolve_bash.py`
  held by its `resolve_bash_py` row of `PARITY_ROWS`), as `run_case_argv` spawns every bash argv
  (`:3253-3254`), never a bare `bash`: from Windows Python a bare `bash` can resolve to the System32 WSL
  launcher, which cannot open a `C:/` path (gotcha subprocess-resolves-a-different-shell). A `None`
  from `resolve_bash` takes the announce line below with the reason `no bash sees <script>`. A path matched by both
  walks is returned once. Every other path under the memory root, the records, stays outside the walk.
  Where the script is absent or its mode exits non-zero, the inventory prints `live carriers: not read —
  <tool root>/check-dead-paths.sh <absent|exit n>; the memory root is excluded whole` once and walks
  outside the memory root only, so an unread carrier list is said and never read as an empty one; the
  `<absent|exit n>` field reads `no bash sees <script>` when no candidate sees it. The
  `--except` paths apply to both walks. Observed by AC2 and AC3.
- **S3** — id 45, the docs. `tools/policy/README.md`'s `--readers` paragraph names the second walk and
  its source, and `tools/check-dead-paths.sh`'s header names `--carriers` beside `--list` and
  `--needles`. NOT OBSERVED by a criterion: prose, graded by the `docs` and `memory hygiene` legs at
  the close.

## 3. Non-goals (OUT)

- Which folders are live carriers: the dead-path gate's decision (TOOL-aRepatriatedFork-30 S9, S10);
  this unit moves its declaration, never its membership.
- The records under the memory root: specs, reviews, build ledgers and archives are frozen and stay
  outside every walk.
- Re-pointing the carriers units 12 and 16 retire or move: those units list them by `bash
  tools/check-dead-paths.sh --list` in their own passes; this unit makes the inventory find them.
- The codebase-map dossiers of the renamed Skills: PLAY-dConvergedCharter-39.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers`, the inventory whose walk S2 widens to the live carriers; without it there is no walk to widen
- **hands-off** `PLAY-dConvergedCharter-17` — `read_live_carriers`, the widened walk that unit's `/build` inventory reads at order 4, so the dossier `memory/map/features/roles.md` is among its readers

## 4. Design

### Evidence

Read at `e6909dcaa`; no product file differs from base `0d1c1dda`.

- The haystack is two `git grep` calls, the second over `'memory/map/features/*' 'memory/gotchas/*'`
  typed inline (`tools/check-dead-paths.sh:192-197`), with the reason in the header (`:57-62`): a dossier
  and a gotcha page are served as live, not kept as records.
- The mode parse is `MODE="${1:---check}"` and a `case` over `--check|--list|--needles`
  (`tools/check-dead-paths.sh:111-112`).
- `derive_readers` does not exist at base; PLAY-dConvergedCharter-11 S6 specifies its walk as "every
  tracked text file outside the memory root".
- Measured at `0d1c1dda`: 50 live carriers name a file of the unattended kit
  (PLAY-dConvergedCharter-12 §4), five gotcha pages and four dossiers name the kickoff engine's path
  (PLAY-dConvergedCharter-16 S3), and four dossiers claim the Skills unit 9 renames.

### The interface

```
bash tools/check-dead-paths.sh --carriers
memory/map/features/*
memory/gotchas/*

check_policy.read_live_carriers(repo) -> list[str] | None   # None: the announce line, the root excluded whole
    argv: [resolve_bash(script) or <announce>, script, "--carriers"], cwd repo,
    script = <repo>/<derive_tool_root()>/check-dead-paths.sh
```

### Inventory

Minted: the array `LIVE_CARRIERS` and the mode `--carriers` of `tools/check-dead-paths.sh`;
`read_live_carriers` in `tools/policy/check_policy.py`, `OK` by `python tools/lexicon/lexicon.py
--suggest read_live_carriers --as py.function` at `e6909dcaa`; the fixture cases `live-carrier` and
`no-dead-path-gate` of `check_policy.py --fixture`.

### Rollout

Gov's tree, one pass at order 3, after PLAY-dConvergedCharter-11 and strictly before the first retiring
units read the inventory (units 12 and 17 at order 4, the latter with a consumes-from edge to this
unit). Nothing ships to an adopter that it did not hold: an adopter without the gate reads the announce
line.

### Files touched (estimate)

- `tools/check-dead-paths.sh`, `tools/check-dead-paths.test.sh`: S1
- `tools/policy/check_policy.py`: S2
- `tools/policy/README.md`: S3

### Alternatives rejected

- **The two folders typed again in `check_policy.py`.** The skeptic's verdict on the finder's fix: a
  second list drifts from the gate's the first time a carrier folder is added, the
  two-answers-to-one-question class.
- **A new shared list file read by both.** A third artifact for a fact the gate already owns; the
  gate's own array, printed by a mode, is the one source with no new file.
- **The whole memory root walked.** Records name deleted files correctly (`tools/check-dead-paths.sh:52-56`),
  so every retirement's inventory would red on frozen history.

## 5. Production-readiness checklist

- security — no write surface: one read-only subprocess of a tracked script by argv list, its bash the
  one `resolve_bash` runs and sees the script with, never a bare `bash` a PATH search resolves.
- perf / scale — one `bash` spawn per inventory run, after `resolve_bash`'s `test -f` probes, and one
  more `git grep` over two folders; `--carriers` makes no git call, so the history walk is not paid.
- error / empty / loading states — an absent or failing gate prints the announce line and walks
  outside the memory root only; an empty array would print nothing and the inventory says `0 live
  carrier pathspec(s)`, never silent.
- observability — the inventory names the carrier source on every run.
- risks — a carrier folder added to the gate later widens every inventory at once, which is the point.
- testing — the fixture cases of §6 and the arm of §7.
- migration — none.
- user docs — `tools/policy/README.md`, S3.

## 6. Acceptance criteria

The fixture is `python check_policy.py --fixture <case> <dir>`, PLAY-dConvergedCharter-11's verb, which
writes a scratch repository under `%TEMP%` with a short name.

- **AC1** — When `bash tools/check-dead-paths.sh --carriers` runs at the unit's tip, it prints
  `memory/map/features/*` and `memory/gotchas/*`, one per line, and exits 0; and `grep -c
  "memory/gotchas/\*" tools/check-dead-paths.sh tools/policy/check_policy.py` counts one line in the gate,
  the array, and none in `check_policy.py`.
  Red when: the carriers are typed twice, or the mode prints nothing.
- **AC2** — When `python check_policy.py --readers 'tools/x/gone.sh' --kind path` runs over the
  `live-carrier` fixture, which plants `<fixture>/tools/x/gone.sh` named in the dossier
  `<fixture>/memory/map/features/x.md` and in the spec `<fixture>/memory/builds/b/spec/2026-01-01-spec-T-b-1.md`,
  and a byte copy of the tracked `tools/check-dead-paths.sh` at `<fixture>/tools/check-dead-paths.sh`,
  never a stub, in a tree whose history holds no deletion, it exits 1 naming the dossier and its line
  and not the spec; with `--except 'memory/map/features/x.md'` it exits 0. The same run with `GOV_BASH`
  unset and a `PATH` whose first `bash` cannot see the tree still exits 1 naming the dossier; with
  `GOV_BASH` pointed at a stub that exits 127 and no other candidate seeing the script, it prints
  `live carriers: not read` with `no bash sees` and exits 0.
  Red when: a live carrier naming the path is not returned, a frozen record is, or a bare `bash` that
  cannot see the tree reads the carriers as not read.
  fixture: the copy is the tracked script byte for byte, so the shipped mode's position is what is
  graded.
- **AC3** — When the same command runs over the `no-dead-path-gate` fixture, the `live-carrier` tree with
  its copy of `check-dead-paths.sh` absent, it prints `live carriers: not read` once and exits 0, the
  dossier not returned.
  Red when: an unread carrier list is read as an empty one with no line.
- **AC4** — When `bash tools/check-dead-paths.sh --list` runs over a scratch clone holding a dossier that
  names a deleted file, it lists that dossier's line as it did before S1, and with the array emptied in a
  copy of the script it does not.
  Red when: the gate's haystack no longer reads the array, so the inventory and the gate read two lists.

## 7. Gates

`dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `policy fixtures` · `policy check` · `python resolver (behaviour + inline parity + idiom ban)` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/check-dead-paths.test.sh · covers AC1 AC4 · the `--carriers` mode and the haystack over a planted dossier, staged red with the haystack's literal pathspecs restored beside an emptied array · none
New arm: tools/policy/check_policy.py · covers AC2 AC3 · the fixture cases `live-carrier` and `no-dead-path-gate`, staged red with `read_live_carriers` returning an empty list silently, spawning a bare `bash`, or reading a copy of the gate whose `--carriers` mode is moved below the needle derivation, over the history-less fixture · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft, promoted by the disposal of
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` for finding 45 (MEDIUM, item M26), repairing
  PLAY-dConvergedCharter-11; that unit's S6 and AC6 rewritten as this unit's sibling edit (its rev-3).
- rev-2 · 2026-11-04 · S1 S2 §1 §3 §4 §5 §10 AC2 AC3 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` findings 17, 24 and 39 (S2 spawns the
  gate through `resolve_bash`, a `None` announced, AC2's bash variants), 40 (`--carriers` answered
  before any git call, AC2's fixture a byte copy of the tracked gate, the arm's staged red the mode moved
  below the derivation), 12 (S2 runs `<repo>/<tool root>/check-dead-paths.sh` with cwd `<repo>`, AC2 and
  AC3 stating the fixture's copy) and 4 (strictly before units 12 and 17 at order 4, the hands-off edge
  to PLAY-dConvergedCharter-17).

## 10. Reuse audit

The seam extended is the dead-path gate's own haystack, `tools/check-dead-paths.sh:192-197`, whose
inline pathspecs become the array a mode prints, so the one declaration stays where the class was
decided (TOOL-aRepatriatedFork-30 S9, S10); and PLAY-dConvergedCharter-11's `derive_readers`, which gains
the second walk. `python tools/codebase-map/reuse_lookup.py "list the live carrier paths under the memory
root that the dead-path gate grades"` ranked name stems only (`live` in `run-gates.sh`, `repo_root`,
`derive_tool_root`, `map_root`, `resolve_memory_root`); none lists carriers, so no existing callable
fits beyond the gate's array, and `derive_tool_root` is the seam S2 finds the gate through. The second
seam is the bash rule: `resolve_bash`, canonical in `tools/lib/resolve_bash.py` and inlined in
`check_policy.py:896` under the `resolve_bash_py` row of `PARITY_ROWS`
(`tools/lib/resolve-python.test.sh:369`), which `run_case_argv` (`:3253-3254`) already applies to every
bash argv; S2 calls it and writes no resolver. The recall
hits agree: TOOL-aRepatriatedFork-30 joined the gotcha pages to the haystack as "a surface served as
live", and TOOL-dTendedCadence-40 grades the same leg's served-text record, a separate question this
unit does not touch.

Recall terms used: `python tools/memory-recall/query.py "which memory files are live carriers graded
like product text rather than frozen records" --terms "dead-path carriers map dossiers gotcha pages
memory root live surface served as live derive_readers inventory"`
