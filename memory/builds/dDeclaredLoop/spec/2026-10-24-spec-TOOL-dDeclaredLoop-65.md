# TOOL-dDeclaredLoop-65 — the remote's freshness is the time of the last fetch, read from what a fetch and a clone write

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-65-deviation-651.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-65-deviation-651.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 55 at HIGH**, its item **H7**, alone in that item. `TOOL-dDeclaredLoop-56` S36
reads the remote-tracking ref's age from that ref's reflog. A fresh clone writes no reflog for
`refs/remotes/origin/main`, and a fetch that does not move the ref writes no entry, so the reflog
measures when the remote last moved, not when it was last fetched. On a fresh clone, and on any remote
quiet longer than the bound, the engine answers `stale-remote` right after a fetch, and
`TOOL-dDeclaredLoop-7` ranks that answer above `act`, so `--plan`'s next line stalls. This unit takes
the report's corrected fix. It repairs `TOOL-dDeclaredLoop-56`.

## 2. Scope (IN)

- **S1** — The last-fetch time is the newest of: the mtime of `FETCH_HEAD` in the common git directory
  and in each linked worktree's git directory (`git rev-parse --git-common-dir`, then `FETCH_HEAD` and
  `worktrees/*/FETCH_HEAD` under it), and the time of the newest reflog entry of the default branch's
  remote-tracking ref where one exists. This supersedes `TOOL-dDeclaredLoop-56` S36's "its age read from
  the ref's reflog". Observed by AC1, AC2.
- **S2** — When none of those exists, as on a fresh clone, the clone's own time stands in: the `clone:`
  entry of the reflog of `refs/heads/<default>`, so a just-cloned tree reads fresh. With none of the
  three and a tracking ref present, the claim is `unread` and the answer `stale-remote`, as
  `TOOL-dDeclaredLoop-7` ranks it. Observed by AC1, AC3.
- **S3** — Every reading names its source on the engine's read-set line,
  `remote: fresh · fetched <age> ago · from FETCH_HEAD` or `from reflog` or `from clone`, so a stale
  answer says which artefact was old. Observed by AC2, AC3.
- **S4** — The fixture cases `fresh-clone` and `quiet-remote` join `position.py --fixture`: a clone
  with no fetch since, and a remote fetched now whose ref has not moved for longer than the bound.
  Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The no-remote reading of `TOOL-dDeclaredLoop-56` S36: unchanged.
- The driver's own claim fetch, which writes a private namespace and no `FETCH_HEAD`
  (`tools/unattended/unattended.sh:2109`): it reads claims, never the default branch's freshness.
- A checklist entry that a time-of-last-event read names the artefact the event writes, the finding's
  left-shift: the class is recorded at the close; S4 is this reading's no-op fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-56` — the engine's remote-freshness reading of S36 in `tools/loop/position.py`, whose age source this unit restates

## 4. Design

### Evidence

- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1: after `git clone up cl`, `git reflog exists
  refs/remotes/origin/main` exited 1 and `.git/FETCH_HEAD` did not exist, while the reflog of
  `refs/heads/main` held `clone: from <url>`; a `git fetch` that moved nothing wrote `.git/FETCH_HEAD`
  with that minute's mtime and left the tracking ref's reflog at zero entries: PINNED, that date.
- `git rev-parse --git-path FETCH_HEAD` resolves to the current worktree's git directory, so a fetch run
  in another worktree of the same clone is found only under the common directory's `worktrees/`.

### The reading

```
times = mtime of <common>/FETCH_HEAD and <common>/worktrees/*/FETCH_HEAD, where present
      + newest reflog time of refs/remotes/<remote>/<default>, where it has entries
      + (if times is empty) the clone: entry of refs/heads/<default>'s reflog
age   = now - max(times) ; fresh when age <= bound ; unread when times is empty
```

### Files touched (estimate)

- `tools/loop/position.py`

### Alternatives rejected

- **A stamp the driver writes after each fetch.** A fetch the operator runs by hand writes no stamp and
  would read stale; `FETCH_HEAD` is written by every fetch.
- **The current worktree's `FETCH_HEAD` alone.** A fetch from the main worktree would leave every linked
  worktree reading stale.

## 5. Production-readiness checklist

- security — reads only.
- perf / scale — a few `stat` calls and one reflog read.
- error / empty / loading states — S2 names the empty case; an unreadable mtime is skipped, never zero.
- observability — S3's source on the read-set line.
- risks — `git fetch --no-write-fetch-head` writes no `FETCH_HEAD`; such a fetch reads by the reflog when
  the ref moved, and as stale when it did not, the conservative side.
- testing — AC1 to AC3 as fixture plants; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant fresh-clone` reads a scratch clone made
  seconds earlier with no fetch since, the answer is not `stale-remote` and the read-set line ends
  `from clone`.
  Red when: the tracking ref's reflog is the only source, so the clone reads unread.
- **AC2** — When `--plant quiet-remote` fetches a remote whose default branch has not moved for longer
  than the bound, the answer is not `stale-remote` and the line ends `from FETCH_HEAD`.
  Red when: the age is the ref's last move, so a quiet remote reads stale after a fetch.
- **AC3** — When `--plant offline-stale` sets every `FETCH_HEAD` mtime and the reflog past the bound,
  the answer is `stale-remote` and the line names the source that was newest.
  Red when: a source missing from the population makes a stale tree read fresh.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 · the fresh-clone, quiet-remote and offline-stale plants, staged against the reflog-only reading `TOOL-dDeclaredLoop-56` S36 specified · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 55 (HIGH, item H7).

## 10. Reuse audit

No existing seam fits: `python tools/codebase-map/reuse_lookup.py "time of the last fetch of a remote"`
ranked `parse_time` (`tools/runlog/extract.py`), `resolve_remote`, `build_remote_ci_red_streak`,
`check_time_sources`, `load_last_queries` and `scan_time_slots`; `resolve_remote` names which remote and
branch, and none reads when a fetch happened, so the reading is git's own artefacts as §4 lists them.

Recall terms used: stale-remote remote-tracking reflog FETCH_HEAD fetch clone fresh bound position engine worktree
