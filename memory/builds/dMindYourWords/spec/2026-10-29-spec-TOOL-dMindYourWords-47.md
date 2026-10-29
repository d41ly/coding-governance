# TOOL-dMindYourWords-47 — one pinned git runner, so the kit's history pin is a property of a function and not of each call site

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 21 (TOOL-dMindYourWords-48) and 22 (TOOL-dMindYourWords-49).
TOOL-dMindYourWords-31 promises in §1 and §5 that every history read of the kit runs pinned and that no
graft can re-parent a commit under any reader, but its S3 pins a closed list of call sites, each passing
`build_git_env()` and `--no-replace-objects` by hand. A promise about a class kept by a list breaks at
the first reader the list omits, and the report found four existing ones and three new ones. This unit
makes the pin a property of one runner, `run_git`, that every history spawn of the kit calls, and
moves the call sites unit 31 pinned onto it, so the class claim holds by construction.

## 2. Scope (IN)

- **S1** — The runner. `run_git(root, *args, **kw)` in `tools/lexicon/lexicon_conf.py` runs
  `["git", "--no-replace-objects", *args]` with `cwd=root`, `env=build_git_env()` (TOOL-dMindYourWords-31
  S1) and `capture_output=True`, passing `input`, `text`, `encoding` and `errors` through, and returns
  the `subprocess.CompletedProcess`, so each caller keeps its own failure handling. It is the only
  spelling of `--no-replace-objects` and the only caller of `build_git_env()` under `tools/lexicon/`,
  `selftest.py` aside. Observed by AC1 and AC2.
- **S2** — The pinned call sites moved. Every spawn unit 31 pinned by hand calls `run_git` instead:
  `read_blame_lines` (unit 31 S2), each `diff-tree` of `read_vocabulary_record`'s `rev` mode, the
  single-commit and the per-parent read (units 32, 33, 36, 43 and 44), the `ls-tree` and `cat-file
  --batch` reads of `read_defs_at_sha` (`tools/lexicon/lexicon.py:4129`, `:4145`), and any spawn of the
  contract walk that carries the pin when this unit is built. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The history spawns unit 31 never pinned: the merge-loss guard, the signals module, the rename map and
  the ledger index read are TOOL-dMindYourWords-48 (id 21); the merge walk's new reads and the branch's
  added set are TOOL-dMindYourWords-49 (id 22).
- A refusal over every git spawn of the kit: TOOL-dMindYourWords-50 (id 2) reads the population this
  runner defines.
- Stripping `GIT_ENV_LEAKS` and silencing the graft-deprecation hint in the runner: review ids 17 and 8,
  the minors batch TOOL-dMindYourWords-52.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-31` — `build_git_env()` and the call sites it pinned by hand, which S2 moves onto the runner
- **consumes-from** `TOOL-dMindYourWords-41` — `build_graft_fixture`, through which AC1 stages its graft with the control in force
- **hands-off** `TOOL-dMindYourWords-48` — the runner, onto which that unit moves the spawns unit 31 never pinned
- **hands-off** `TOOL-dMindYourWords-49` — the runner, onto which that unit moves the reads units 36 and 37 add
- **hands-off** `TOOL-dMindYourWords-50` — the runner, the one function inside which that unit's inventory admits a history spawn
- **hands-off** `TOOL-dMindYourWords-52` — the runner, to which the batch adds the leak strip and the hint switch (ids 8, 17)

## 4. Design

### Evidence

- Unit 31 §1: "has `read_blame_lines` and every other history read in the kit run under it"; §5: "no
  replace ref or graft file can re-parent a commit under any reader"; S3 names the contract walk and
  `tools/lexicon/lexicon.py:4129-4145` (`spec/2026-10-29-spec-TOOL-dMindYourWords-31.md`).
- At base the kit spawns git at `tools/lexicon/lexicon.py:411`, `:4129`, `:4145`, `:4197`, `:4347` and
  `:4406`, and `scaffold_lexicon.py:207`, each with its own `subprocess.run(["git", …])`.
- The repository's pinned runners already have this shape: `run_git` in
  `tools/memory-tree/transition_audit.py:82-89` and `tools/memory-tree/routed_commits.py:86-100` put
  `--no-replace-objects` in the argv and `build_git_env()` in the environment of every call. The lexicon
  kit imports no sibling (`check_self_containment`, `tools/lexicon/lexicon.py:2359`), so it carries its
  own by the same name, as unit 31 carries `build_git_env`.

### The runner

```
def run_git(root, *args, **kw):
    return subprocess.run(["git", "--no-replace-objects", *args], cwd=root,
                          env=build_git_env(), capture_output=True, **kw)
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_git` | function, `tools/lexicon/lexicon_conf.py` | `py.function`; `lexicon.py --suggest run_git --as py.function` answered `OK` at writing |

### Rollout

Live at landing, one order after TOOL-dMindYourWords-31, and before TOOL-dMindYourWords-48, -49 and -50
at the same order, which sort after it.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2
- `tools/lexicon/lexicon.py`: S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Restating unit 31 §1 and §5 as the enumerated set**, the report's second route: it makes the claim
  true by making it small, and the next reader is again outside it.
- **A runner that raises on a non-zero exit**, `routed_commits.run_git`'s contract: the kit's readers
  each turn a failed read into their own refusal or `None` today (`read_defs_at_sha` returns `None`,
  `check_merge_losses` names a `DEAD PROBE`), so a raising runner changes every caller's failure path in
  a unit about the pin.

## 5. Production-readiness checklist

- security — the class claim of unit 31 holds by construction: a history read pinned is a read through
  `run_git`, and unit 50 refuses any other.
- perf / scale — none: the same spawns, one function call deeper.
- error / empty / loading states — each caller keeps its failure handling; the runner adds none and
  removes none.
- observability — unchanged.
- risks — a caller that relied on an ambient `GIT_DIR` or `GIT_INDEX_FILE` still inherits it until the
  batch's leak strip (id 17) lands; no caller at base does.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — TOOL-dMindYourWords-30 S3's README sentence covers every reader.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/lexicon'); import lexicon_conf as c;
  print(c.run_git(sys.argv[1], 'rev-list', '--parents', '-n', '1', sys.argv[2], text=True).stdout)"
  <repo> <c2>` runs in a fixture whose second commit `build_graft_fixture` grafted onto no parent, it
  prints `<c2> <c1>`, once for a replace ref and once for a graft file.
  Red when: the runner loses either pin and prints `<c2>` alone.
  fixture: two repositories under `%TEMP%/<short>`, each staged by `build_graft_fixture`.
- **AC2** — When `git grep -n -F -e '"--no-replace-objects"' -e 'env=build_git_env()' -- tools/lexicon
  ':!tools/lexicon/selftest.py'` runs after the pass, every line it prints falls inside `run_git`, and
  each of the two patterns matches at least one of them.
  Red when: a call site still spells its own pin beside the runner, or the runner lost one.
- **AC3** — When `python -c` parses `tools/lexicon/lexicon.py` and `tools/lexicon/lexicon_conf.py` with
  `ast` and lists, for `read_blame_lines`, `read_vocabulary_record` and `read_defs_at_sha`, every call
  whose function is `subprocess.run`, it prints none, and each of the three calls `run_git`.
  Red when: one of the three still spawns git on its own.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · the runner under a replace ref and a graft file staged by `build_graft_fixture`, its failing case `--no-replace-objects` cut from `run_git`, under which the replace-ref half prints one word · none

## 8. Open questions

- **F1 — Where does the class claim get its guarantee?** Options: (a) one runner every history spawn
  calls, with an inventory refusing any other (this unit and unit 50); (b) unit 31's list, widened to
  every reader known today; (c) unit 31's §1 and §5 reworded to the list. (b) breaks at the next reader
  and (c) gives up the claim. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the shape of
  `tools/memory-tree/transition_audit.py:82` and the most capable survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 3 (HIGH, item H2, shared with ids 21 and
  22) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is the repository's pinned runner, `run_git` in `tools/memory-tree/transition_audit.py:82-89`
and `tools/memory-tree/routed_commits.py:86-100`, carried by name into the kit beside unit 31's
`build_git_env`, because the kit imports no sibling. `python tools/codebase-map/reuse_lookup.py "route
every git history read through one pinned spawn helper"` ranked `run_git` (fan-in 8, a seam),
`read_git_output` and `build_git_env`, the three read above; this unit mirrors the first's argv and the
second's environment rule.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git build_git_env inventory spawn class history"`
