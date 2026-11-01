# TOOL-dScopedBuild-36 — the no-ask arm reads a checked-out fixture's index, status and bytes, and its planted red really stages a row

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 7 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 25 to 35
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, report item **H1**. `TOOL-dScopedBuild-27` S1, AC1 and AC2 check
that the push wrote no ask by comparing the bytes of every `BACKLOG.md` on disk under the fixture's
memory root. `routed_commits.build_fixture` (`tools/memory-tree/routed_commits.py:387-417`) runs
`git init` and one `git fast-import`, so the fixture has no working tree and no index, and the
"before" read is empty. The planted red unit 27 §7 names, the push calling the filer, goes through
`write_ask_rows` (`tools/unattended/unattended.sh:9984-10018`), which stages a row and then removes
it when the ask generator cannot read it back; the fixture declares no `ASKS_CMD`. So disk and index
end as they began, and AC1 and AC2 stay green on the regression unit 27 exists to stop.

This unit checks the fixtures out, reads index, status and bytes together, and plants a red that
really writes and stages a row. It repairs `TOOL-dScopedBuild-27` and builds one step after it
(order 7).

## 2. Scope (IN)

- **S1** — The fixture checked out. Each of unit 27's two selftest fixtures, after
  `build_fixture` returns, runs `git reset -q --hard` in the fixture, so its index and working tree
  hold HEAD's tree. Its first commit adds a tracked `BACKLOG.md` in its `tFix` build folder holding one ask
  row, so the "before" read is not empty. `memory/` is outside the fixture's `ROUTED_PATHS`, so the
  leg's findings do not change. `build_fixture` is defined at `routed_commits.py:387`, not at the
  `:403-404` unit 27 §4 cites. Observed by AC1 and AC2.
- **S2** — The observation. `read_backlog_state(repo, memory_root)`, a selftest helper in
  `routed_commits.py`, returns three reads: the lines of `git ls-files -s -- <memory root>` whose path
  ends `/BACKLOG.md`, the output of `git status --porcelain --untracked-files=all -- <memory root>`,
  and the bytes of every `BACKLOG.md` on disk under the memory root. The arm calls it before and
  after `check_routed_commits` and fails naming the first path that differs. This supersedes unit 27
  S1's "byte for byte" read and its §4 "The observation"; unit 27's other clauses stand. Observed by
  AC1, AC2 and AC3.
- **S3** — The plant writes. The arm's staged break runs the leg and then the filer's success path
  for each `ask ·` line it printed: append one row to that `tFix` backlog and `git add`
  it, as `write_ask_rows` writes and stages at `unattended.sh:9994`. A second plant writes an
  untracked `BACKLOG.md` into a `tOther` build folder and stages nothing. S2's read must name the moved path
  under each plant. Observed by AC3.
- **S4** — The real filer writes in the exit's fixture. In the driver suite's slug fixture with an
  `ASKS_CMD` stub that reads each row back, as unit 14 AC7 builds it, `write_gate_asks` handed the
  push leg's `ask ·` lines leaves one staged row in the slug's `BACKLOG.md`. That shows unit 27 §7's
  planted red, the push calling the filer, writes where a filer can read back. Observed by AC4.
- **S5** — Unit 27 answered. Unit 27's acceptance ledger answers its AC1 and AC2 with a note naming
  `TOOL-dScopedBuild-36 S2`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Where asks are filed. Unit 14 §8 F2 rules the Build exit, and unit 27 S2 observes it.
- Changing `build_fixture` for its other callers. S1 checks out only unit 27's two fixtures.
- The left-shift checklist entry the report names. No clause of this build names it.
- Rewording unit 27's text. Each clause is superseded by name and answered in its ledger.

### Edges

- **consumes-from** `TOOL-dScopedBuild-27` — S1's no-write read, AC1's and AC2's fixtures and §7's planted red, which S1 to S3 restate so the arm can go red (id 11)
- **consumes-from** `TOOL-dScopedBuild-14` — S6's `write_gate_asks` and AC7's slug fixture with `ASKS_CMD` declared, over which S4 shows the filer stages a row (id 11)
- **hands-off** `TOOL-dScopedBuild-41` — S1's two fixtures, which this unit's builder checks out through a `checkout=True` keyword it adds to `routed_commits.build_fixture`, and §4's write set, which it widens by `memory/map/generated/symbols.json` with its four legs by a rev bump before building, as that unit's S1 and S10 rule (ids 1, 21, 19)

## 4. Design

### Evidence

- `routed_commits.py:387-417`: `build_fixture` runs `git init -q --template=` and
  `git fast-import --quiet` into `refs/heads/main`. Nothing checks out, read-trees or resets.
- `routed_commits.py:420-425`: `set_fixture_conf` writes no `ASKS_CMD`.
- `unattended.sh:9994` writes and stages the row; `:10007` runs `GIT rm -q --cached -f` and
  `rm -f` on a file that did not exist before, when `read_ask_back` (`:9945`) fails.
- Unit 14 S6 makes `write_gate_asks` dark when `ASKS_CMD` is blank, so in unit 27's fixtures the
  planted filer call writes nothing at all.

### The observation, after this unit

```
build_fixture(...) ; git reset -q --hard           # index and tree hold HEAD, BACKLOG.md tracked
before = read_backlog_state(repo, "memory")        # ls-files -s, status --porcelain, bytes
check_routed_commits(...)   under warn-and-ask     # rc 0, one ask · line per finding
after  = read_backlog_state(repo, "memory")        # after == before, else name the path
plant: append + git add  -> after != before, names memory/builds/tFix/BACKLOG.md
plant: untracked write   -> after != before, names memory/builds/tOther/BACKLOG.md
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_backlog_state` | selftest function, `routed_commits.py` | `py.function`, OK at `--suggest` |

### Migration

None: no stored data changes.

### Rollout

Built at order 7, one step after unit 27 (order 6). It ties with unit 5 at order 7. Both write
`tools/memory-tree/routed_commits.py`, so BUILD-METHOD M6 sequences them within the step.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`: the selftest helper and arms of S1 to S3
- `tools/unattended/unattended.test.sh`: the arm of S4

### Alternatives rejected

- **Read the fixture's objects with `git cat-file` instead of checking out.** A write by a leg goes
  to disk or the index, never to HEAD's tree, so an object read cannot see it.
- **Keep the byte read and only add an `ASKS_CMD` stub.** On a fixture with no working tree a row the
  filer stages is still read against an empty "before", and a disk-only write by another path stays
  the only thing the arm could see.

## 5. Production-readiness checklist

- security — no new write path; the arm asserts the push has none.
- perf / scale — one `git reset --hard` and two reads per fixture, under a second each.
- error / empty / loading states — a fixture whose memory root holds no `BACKLOG.md` reads three empty
  values, and S1's tracked row keeps that case out of these arms.
- observability — the arm names the first path whose index entry, status line or bytes moved.
- risks — a plant that fails to write would leave the arm vacuous again; AC3 shows each plant moves
  the read.
- testing — AC1 to AC3 in the routed-commits selftest, AC4 in the driver suite.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the routed-commits selftest runs `check_routed_commits` on unit 3 AC2's fixture,
  checked out by `git reset -q --hard`, under `warn-and-ask`, it exits 0, prints one
  `ask · build.scope · TOOL-tFix-1` line, and `read_backlog_state` returns the same three reads after
  as before, the "before" index read holding the `tFix` build's tracked `BACKLOG.md`.
  Red when: the leg writes or stages any `BACKLOG.md`, or the "before" read is empty.
  fixture: unit 3 AC2's, built by `routed_commits.build_fixture`, with S1's tracked backlog.
- **AC2** — When the same arm runs on unit 9 AC3's map-adopting fixture, checked out the same way, it
  exits 0, prints the `feat · touched and still graced` finding as an `ask ·` line, and
  `read_backlog_state` is unchanged.
  Red when: the touch join's warn-and-ask half writes or stages a row at the push.
  fixture: unit 9 AC3's, with S1's tracked backlog.
- **AC3** — When the arm's staged break appends and `git add`s one row after the leg, the after read
  differs and the arm's failure names the `tFix` build's `BACKLOG.md`; when it writes an untracked
  `BACKLOG.md` in a `tOther` build folder instead, the failure names that path.
  Red when: either plant leaves `read_backlog_state` unchanged, the vacuous arm this unit closes.
- **AC4** — When the driver suite hands the push leg's `ask ·` lines to a sliced `write_gate_asks`
  over the slug fixture with an `ASKS_CMD` stub that reads rows back, `git diff --cached --name-only`
  names the slug's `BACKLOG.md`.
  Red when: the filer stages nothing in the fixture the plant runs in.
  fixture: unit 14 AC7's slug fixture with `ASKS_CMD` declared.
  permission: observed at the close, after unit 14 is built.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 · both checked-out fixtures read by `read_backlog_state` before and after, staged by the two writing plants · none

New arm: tools/unattended/unattended.test.sh · covers AC4 · the sliced filer over the push leg's lines in the `ASKS_CMD` fixture, staged by blanking the stub so the row rolls back · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 27's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 25 to 35, id 11
  (HIGH, item H1).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (ids 1, 21, 19).

## 10. Reuse audit

The seams are `routed_commits.build_fixture` (`tools/memory-tree/routed_commits.py:387`), checked out
rather than rebuilt, unit 27's two arms, whose read S2 widens, and unit 14 S6's `write_gate_asks`,
which S4 observes and does not copy. `python tools/codebase-map/reuse_lookup.py "compare a fixture
repository's index and working tree before and after a call"` ranked `tree`, `before`, `fixture` and
`build_fixture`; none reads a fixture's index and status together, so no existing seam fits beyond
the fixture builder named.

Recall terms used: `python tools/memory-recall/query.py "why does the push leg's no-write arm stay green on a staged row" --terms "build_fixture fast-import working tree index BACKLOG.md write_ask_rows ASKS_CMD warn-and-ask planted red"`
