# TOOL-dMindYourWords-48 — the history reads unit 31 never pinned run through the kit's pinned runner

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md) | research | TOOL-dMindYourWords-38 TOOL-dMindYourWords-40 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 21 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 3 (TOOL-dMindYourWords-47) and 22 (TOOL-dMindYourWords-49).
TOOL-dMindYourWords-31 S3 pins the contract walk and the ancestor reads at `lexicon.py:4129-4145` and
nothing else, while the kit already makes, or by order 21 will make, other reads over commits it did not
create: `check_merge_losses`' `git` lambda, which `--merge-losses` runs from the pre-push hook; the
signals of `lexicon_signals.py`; `read_rename_map`; and the ledger's index read. Under a graft the
merge-loss guard grades grafted parents and merge-bases while `read_defs_at_sha` reads real trees, so it
can skip a merge or invent a loss. This unit moves each of those spawns onto `run_git`.

## 2. Scope (IN)

- **S1** — The merge-loss guard. `check_merge_losses`' `git` lambda (`tools/lexicon/lexicon.py:4197`)
  calls `run_git(root, *args, text=True, encoding="utf-8", errors="replace")`, so its `rev-parse`,
  `rev-list --merges --parents`, `merge-base`, `diff` and `log` reads (`:4203`, `:4204`, `:4230`,
  `:4235`, `:4258`) run pinned. Observed by AC1 and AC3.
- **S2** — The signals module. Every git spawn of `tools/lexicon/lexicon_signals.py`
  (TOOL-dMindYourWords-16 S1), `check_record_stale`'s first-parent comparison among them, calls
  `run_git`. Observed by AC3.
- **S3** — The rename map. `read_rename_map` (TOOL-dMindYourWords-9 S4) runs its `git diff -M
  --name-status -z` through `run_git`. Observed by AC3.
- **S4** — The ledger's index read. `read_ledger_source`'s `git show :<home>` (TOOL-dMindYourWords-35
  S1) calls `run_git`, since a replace ref can substitute a blob as well as a commit. Observed by AC3.

## 3. Non-goals (OUT)

- The runner itself and the call sites unit 31 pinned: TOOL-dMindYourWords-47 (id 3).
- The reads units 36 and 37 add, the merge walk and the branch's added set: TOOL-dMindYourWords-49
  (id 22).
- The refusal over every spawn of the kit: TOOL-dMindYourWords-50 (id 2).
- The all-readers graft sweep the minors batch adds (id 32): TOOL-dMindYourWords-52.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-47` — `run_git`, the runner each spawn moves onto
- **consumes-from** `TOOL-dMindYourWords-41` — `build_graft_fixture`, through which AC1 stages its graft with the control in force
- **consumes-from** `TOOL-dMindYourWords-9` — `read_rename_map`, whose spawn S3 moves
- **consumes-from** `TOOL-dMindYourWords-16` — `lexicon_signals.py`, whose spawns S2 moves
- **consumes-from** `TOOL-dMindYourWords-35` — `read_ledger_source`'s index read, which S4 moves
- **hands-off** `TOOL-dMindYourWords-50` — the moved spawns, which that unit's inventory finds inside `run_git` calls and nowhere else

## 4. Design

### Evidence

- `check_merge_losses` defines `git = lambda *args: subprocess.run(["git", *args], cwd=root, …)` at
  `tools/lexicon/lexicon.py:4197` and calls it at `:4203`, `:4204`, `:4230`, `:4235` and `:4258`; the
  parents it reads feed `read_defs_at_sha` (`:4246`).
- `tools/unattended/unattended.test.sh:3120-3131` measured that a two-line `info/grafts` gives two
  unrelated histories a merge-base, so an unpinned `merge-base` is a graft-sensitive read.
- Unit 16 S1 moves `check_record_stale` into `lexicon_signals.py`, comparing a commit with its first
  parent (`spec/2026-10-29-spec-TOOL-dMindYourWords-16.md` S1); unit 9 S4 defines `read_rename_map`
  over `git diff -M --name-status -z` (`spec/2026-10-29-spec-TOOL-dMindYourWords-9.md` S4); unit 35 S1
  reads `git show :<home>` (`spec/2026-10-29-spec-TOOL-dMindYourWords-35.md` S1).
- `--merge-losses` prints one summary line, `merge-losses: graded=<n> skipped=<n> …`
  (`tools/lexicon/lexicon.py:4323`), and names a skipped merge `SKIPPED <sha8> — its parents share no
  merge base` (`:4233`).

### Inventory

Minted: none.

### Rollout

Live at landing, after TOOL-dMindYourWords-47 at the same order, which sorts first.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S3, S4
- `tools/lexicon/lexicon_signals.py`: S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Exporting the two pins in `os.environ` at the merge-loss entry point**: unit 31 §4 rejects the
  environment route, since an importer of the module reads unpinned.
- **Leaving the index read unpinned as not a history read**: a replace ref substitutes any object, a
  blob included, and the inventory of unit 50 is deny-by-default, so an exemption would have to be
  argued where a call costs nothing.

## 5. Production-readiness checklist

- security — the merge-loss guard on the pre-push path grades the real graph; no graft can skip a
  merge or invent a loss.
- perf / scale — none: the same spawns.
- error / empty / loading states — each reader keeps its own handling; a failed pinned read reads as
  the failure it was.
- observability — unchanged.
- risks — none beyond unit 47's.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — internal.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py --merge-losses <base>..<merge>` runs in a fixture whose
  two-parent merge has a real merge base, and the first parent was grafted onto no parent with
  `build_graft_fixture`, it prints `graded=1` and no `SKIPPED` line, as the ungrafted fixture does,
  once for a replace ref and once for a graft file.
  Red when: the `merge-base` read follows the graft, finds no base, and the merge is skipped.
  fixture: a scratch repository under `%TEMP%/<short>` with a `.lexicon.conf` arming `py`.
- **AC2** — When the same fixture runs ungrafted, it prints the same `graded=` and `skipped=` counts as
  AC1.
  Red when: the pinned runner changed the guard's verdict on the real graph.
- **AC3** — When `python -c` parses `tools/lexicon/lexicon.py` and its sibling `lexicon_signals.py`,
  the module unit 16 creates, with `ast` and lists, inside `check_merge_losses`, `read_rename_map`, `read_ledger_source` and every
  function of `lexicon_signals.py`, each call whose function is `subprocess.run` with a first argument
  beginning `"git"`, it prints none, and each of the four names calls `run_git` at least once, the
  signals module through any of its functions.
  Red when: one of the four readers still spawns git on its own.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · a merge whose first parent is grafted onto no parent, its failing case the lambda restored to a bare `subprocess.run`, under which the merge prints `SKIPPED` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 21 (HIGH, item H2, shared with ids 3 and
  22) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is `run_git`, TOOL-dMindYourWords-47's runner, itself carried from
`tools/memory-tree/transition_audit.py:82`; this unit moves four readers onto it and mints nothing.
`python tools/codebase-map/reuse_lookup.py "route every git history read through one pinned spawn
helper"` ranked `run_git`, `read_git_output` and `build_git_env`; the merge-loss guard's lambda is the
repository's last unpinned `merge-base` reader in a kit that has a runner to call.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git build_git_env inventory spawn class history"`
