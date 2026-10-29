# TOOL-dMindYourWords-41 — every graft arm stages its graft through one helper that proves the graft is in force

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 9 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 15 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H4 with id 6 (TOOL-dMindYourWords-40). A graft arm judges the kit under a graft
it staged, but nothing checks that the graft actually re-parents the commit in the environment the arm
runs in. When anything neutralises it, an ambient `GIT_GRAFT_FILE`, a replace-ref base or a fixture
written to the wrong `.git`, the arm reads the real graph, the pinned and the unpinned kit agree, and
the arm greens with the pin cut. The unattended suite already met this exact failure and answered it
with a control (`tools/unattended/unattended.test.sh:3120-3131`). This unit gives the lexicon selftest
the same control, once, in a helper every graft arm stages through.

## 2. Scope (IN)

- **S1** — The helper. `build_graft_fixture(repo, commit, kind, parents=())` in the prologue of
  `tools/lexicon/selftest.py`, above the first arm, stages a graft of `commit` onto `parents`: `kind`
  `"replace"` runs `git replace --graft <commit> <parents…>` and `kind` `"file"` writes the line
  `<commit> <parents…>` to `<repo>/.git/info/grafts`, the path taken from `git -C <repo> rev-parse
  --git-dir` so it never lands in another repository's `.git`. Observed by AC1 and AC3.
- **S2** — The control. Before it returns, the helper runs an unpinned `git -C <repo> rev-list --parents
  -n 1 <commit>` in the selftest's own environment and raises `AssertionError("graft not in force: …")`
  naming the kind, the commit and what git printed, unless the output is exactly `<commit>
  <parents…>`. An arm whose graft is neutralised therefore reds instead of judging the real graph.
  Observed by AC2.
- **S3** — The arms stage through it. The replace-ref and graft-file arms of TOOL-dMindYourWords-30 and
  -32 stage their graft with `build_graft_fixture`, and no other line of the selftest spells `git
  replace --graft` or `info/grafts`. Observed by AC3.

## 3. Non-goals (OUT)

- Clearing the variables that neutralise a graft: TOOL-dMindYourWords-40 (id 6); this unit's control is
  what reds if that clear is ever lost.
- Any kit code: the helper and its control live in the selftest only.
- The checklist entry the report names under H4: a checklist is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-40` — the cleared environment the control runs in; without it the control reds every graft-file arm on the unattended close
- **consumes-from** `TOOL-dMindYourWords-30` — the provenance graft arms S3 re-stages through the helper
- **consumes-from** `TOOL-dMindYourWords-32` — the added-set graft arms S3 re-stages through the helper
- **hands-off** `TOOL-dMindYourWords-31` — the helper, through which that unit's drift-blame graft arms stage their graft
- **hands-off** `TOOL-dMindYourWords-47` — the helper, through which that unit's pinned-spawn graft criterion stages its graft
- **hands-off** `TOOL-dMindYourWords-48` — the helper, through which the merge-loss graft fixture stages its graft
- **hands-off** `TOOL-dMindYourWords-49` — the helper, through which the merge-walk and branch-walk graft fixtures stage their graft
- **hands-off** `TOOL-dMindYourWords-52` — the helper, through which the batch's all-readers graft sweep stages its graft

## 4. Design

### Evidence

- `tools/unattended/unattended.test.sh:3120-3131` stages a graft with `.git/info/grafts`, then asserts
  under `env -u GIT_GRAFT_FILE` that the graft gives two unrelated histories a merge-base (the
  control) before asserting the pinned read gives none (the arm); its comment records that the
  driver's export once turned that control red under `--close`.
- The graft arms of units 30 and 32 name "the pin cut out" as their failing case and stage the graft
  inline (`spec/2026-10-29-spec-TOOL-dMindYourWords-30.md` §7, `spec/2026-10-29-spec-TOOL-dMindYourWords-32.md`
  §7); neither checks the graft took effect.
- Measured on git 2.54.0 in a fixture under `%TEMP%`: `git rev-list --parents -n 1 <c2>` printed `<c2>`
  alone after `git replace --graft <c2>`, and `<c2> <c1>` under `GIT_REPLACE_REF_BASE=refs/nothing/`
  or `--no-replace-objects`. So the control's one read separates an effective graft from a neutralised
  one. PINNED 2026-10-29.

### The helper

```
def build_graft_fixture(repo, commit, kind, parents=()):
    if kind == "replace": git -C repo replace --graft commit *parents
    elif kind == "file": write "<commit> <parents…>\n" to <git-dir>/info/grafts
    else: raise ValueError(kind)
    got = git -C repo rev-list --parents -n 1 commit        # unpinned, the selftest's environment
    if got.split() != [commit, *parents]: raise AssertionError("graft not in force: ...")
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `build_graft_fixture` | function, `tools/lexicon/selftest.py` | `py.function`; `lexicon.py --suggest build_graft_fixture --as py.function` answered `OK` at writing |
| `graft not in force` | assertion text | none |

### Rollout

Live at landing, one order after TOOL-dMindYourWords-30 and -32 and after TOOL-dMindYourWords-40 at the
same order, which sorts first. Later graft arms of units 31, 47, 48, 49 and 52 stage through it.

### Files touched (estimate)

- `tools/lexicon/selftest.py`: S1, S2, S3

### Alternatives rejected

- **A control inside each arm**: the shape the finding describes, where the next arm is the one that
  forgets it.
- **Asserting the pinned kit's verdict differs from an unpinned run**: that needs the unpinned kit, a
  build of the pin's absence the selftest does not have, while one `rev-list` reads the graft directly.

## 5. Production-readiness checklist

- security — N/A — a test helper; no product surface.
- perf / scale — one `rev-list` per staged graft.
- error / empty / loading states — an unknown `kind` raises `ValueError`; a neutralised graft raises
  the control's assertion, naming what git printed.
- observability — the assertion names the kind, the commit and git's output.
- risks — an arm built later that stages its own graft bypasses the control; AC3's grep reds it.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — selftest internals.

## 6. Acceptance criteria

- **AC1** — When the selftest prologue is executed as TOOL-dMindYourWords-40 AC1 executes it and
  `build_graft_fixture(r, c2, "replace")` and then `build_graft_fixture(r2, c2b, "file")` are called on
  two scratch repositories of two commits each, both return, and `git -C <r> rev-list --parents -n 1
  <c2>` prints `<c2>` alone.
  Red when: the helper stages nothing, or writes the graft file outside the repository's git dir.
  fixture: two scratch repositories under `%TEMP%/<short>`.
- **AC2** — When the same call with `kind` `"file"` runs after `os.environ["GIT_GRAFT_FILE"] =
  "/dev/null"` is set in the probe, it raises an `AssertionError` whose text holds `graft not in force`.
  Red when: a neutralised graft passes the control and an arm would judge the real graph.
- **AC3** — When `git grep -n -e 'info/grafts' -e '"--graft"' -- tools/lexicon/selftest.py` runs after
  the pass, every line it prints falls inside the body of `build_graft_fixture`, and `git grep -h -c
  'build_graft_fixture(' -- tools/lexicon/selftest.py` prints a count of at least 5, its definition
  and the four arms of units 30 and 32.
  Red when: an arm still stages its own graft beside the helper.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC2 · the control itself, its failing case `GIT_GRAFT_FILE=/dev/null` set before a graft-file stage, under which the helper must raise rather than return · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 15 (HIGH, item H4, shared with id 6) of the
  round-1 audit of units 30 to 37, with the control's read measured.

## 10. Reuse audit

The seam is the graft control the unattended suite already wrote (`tools/unattended/unattended.test.sh:3120-3131`),
carried as one helper in the lexicon selftest because a selftest of a kit that imports no sibling cannot
import another suite. `python tools/codebase-map/reuse_lookup.py "stage a git graft in a fixture and
assert it took effect"` ranked generic git readers and no graft fixture helper in any kit, so no
existing seam fits beyond the pattern carried.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git build_git_env inventory spawn class history"`
