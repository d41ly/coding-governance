# TOOL-aMendedFleet-72 — the gate runner reaps the dead `gate-timings.tsv` it no longer reads

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · advances TOOL-aMeteredTurnstile-3 · order 72

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The gate runner renamed its timing cache to `<git-dir>/gate-ledger.tsv` and stopped reading the old
`<git-dir>/gate-timings.tsv`, but never removed it. On node a the common-dir copy still sits there,
last written 2026-08-20, and three build records had to warn readers not to cite it as a measurement.
The report lists it under "what to delete or demote" `[B#14]`. No code on main reads or writes the
file, so the only thing left to remove is the file itself, on every node that still holds one. This
unit makes the runner delete it where it writes the ledger, so each node's next bar clears its own
copy and no node needs a manual act.

## 2. Scope (IN)

- **S1** — Where `tools/run-gates/run-gates.sh` writes the ledger after a run, it also deletes
  `gate-timings.tsv` from its own git dir and from the git common dir, quietly and without failing
  the run if the delete fails. The delete names that one file and nothing else. Observed by AC1, AC2.
  **Readers:** by name: `tools/run-gates/run-gates.sh` and `tools/run-gates/profile_bar.py` spell
  `gate-timings.tsv`, both in comments that say the ledger replaced it; neither opens it.
  by value: NO VALUE READERS — nothing has read the file since the ledger rename, which AC3 shows.
- **S2** — The comment above the ledger write says the runner deletes the retired file, and why: it is
  a stale second store of one fact, and the runner is the one program every node runs. Observed by
  AC3.
- **S3** — THE MANIFEST STAMP. `tools/run-gates/run-gates.sh` is on the kickoff manifest's `watch:`
  line, so the same commit re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` with a
  delta line in its message; the staged manifest leg of `.githooks/pre-commit` refuses the commit
  otherwise. Observed by AC5.

## 3. Non-goals (OUT)

- The ledger's own eviction predicate. `TOOL-aMeteredTurnstile-3` also says the ledger carries forward
  a row for a leg the manifest has dropped. That is still true at base, and it is a separate
  mechanism in the same write block. This unit removes the dead file that holds the ask's surviving
  orphan rows, which is why the header says `advances` and not `closes`.
- Rewriting the historical comments and build records that name `gate-timings.tsv`. They describe a
  rename that happened, and they stay true.
- A legacy-filename read fallback. `TOOL-aScannedThrottle-8` proposes one among three remedies; §8 F2
  records why deleting the file does not conflict with that ask.
- Deleting node a's copy by hand. That reaches one node, and the runner reaches all four.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04.

- `git grep -n gate-timings -- tools .githooks skills` returns three lines, and every one is a
  comment: `run-gates.sh` near line 3114 ("It replaces the old `gate-timings.tsv`"), and
  `profile_bar.py` near line 332 ("THE LEDGER, not the retired `gate-timings.tsv`"). The runner sets
  `TIMINGS="$LEDGER"` near line 284, so its dispatch hint reads the ledger.
- `C:/projects/coding-governance/.git/gate-timings.tsv` exists on node a: 90 rows, 2,869 bytes,
  modified 2026-08-20 13:30. 82 of its rows name a leg in today's 124-leg manifest. PINNED,
  measured 2026-10-04. No linked-worktree git dir under it holds a copy.
- Fixture probe on 2026-10-04, at base: in a scratch repository under `%TEMP%/af72` holding a
  `.git/gate-timings.tsv`, the worktree's gate runner with `GATE_LEGS` naming a one-leg manifest
  whose leg runs `true` exited 0 in 4 seconds, wrote `gate-ledger.tsv`, and left
  `gate-timings.tsv` in place. That is the staged red AC1 inverts.
- The runner already deletes a file it owns in the same git dir: `rm -f "$gd/gate-queue-status"` near
  line 1140. S1 follows that shape.
- The common dir is already resolved as `TS_COMMON` near line 801 for the turnstile, so S1 adds no
  git call.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `memory/guides/SESSION-KICKOFF.md`

### Rollout

The first bar on each node after landing deletes that node's copy. A bar run from a linked worktree
reaches the common-dir copy, so the close's own bar on node a clears node a. The run-gates kit
version moves once, minted at the lander by unit 65 or owed at the close.

### Alternatives rejected

- **A one-time `rm` on node a.** It reaches one of four nodes, and adopters who ran an older runner
  hold the same file.
- **Deleting it in `tools/check-wiring.sh --session`.** That hook wires tools; a runtime artifact of
  the runner belongs to the runner.

## 5. Production-readiness checklist

- security — the delete is a fixed filename inside the git dir the runner already writes; it takes
  no input and follows no link.
- perf / scale — one `rm -f` per bar.
- error / empty / loading states — an absent file is a no-op, and a failed delete never changes the
  run's exit code.
- observability — none added: the file is dead, and announcing its removal on every bar is noise.
- risks — a reader nobody knows about loses the file. AC3 shows no tracked reader exists, and the
  file has not changed since 2026-08-20.
- testing — AC1 and AC2 on a scratch fixture; AC3 by grep; AC5 by the manifest checker.
- migration — the deletion is the migration.
- user docs — N/A: no operator-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a scratch repository under a short `%TEMP%` path holds the retired timing file in
  its `.git`, and this worktree's gate runner runs there with `GATE_LEGS` naming a one-leg manifest
  whose leg runs `true`, the run exits 0, the ledger exists in `.git`, and `ls .git` no longer lists
  the retired file.
  Red when: the base runner leaves the file in place, as the probe in §4 observed.
  cost: about 4 seconds.
- **AC2** — When the same scratch repository gains a linked worktree through `git worktree add`, a
  fresh copy of the retired file is written to its common `.git`, and the runner runs from the linked
  worktree, `ls .git` in the main checkout no longer lists the retired file.
  Red when: only the linked worktree's own git dir is cleaned and the common-dir copy survives.
- **AC3** — When `git grep -n gate-timings -- tools .githooks skills` runs at the unit's tip, every hit
  is a comment line except the one delete S1 adds, and no hit opens, reads or writes the file.
  Red when: a read or a write of the file survives anywhere under those trees.
- **AC4** — When the close's bar has run on node a, a listing of the directory
  `git rev-parse --git-common-dir` prints no longer shows the retired file.
  Red when: the file survives a bar run from this build's worktree.
  permission: observable only after the close runs the bar, which no unit pass may do.
- **AC5** — When `bash skills/session-kickoff/manifest-check.sh` runs after the unit's commit, it
  exits 0, and `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` shows the `last-audit:`
  line moved.
  Red when: check 5 reports unaudited drift on the run-gates runner script.

## 7. Gates

`run-gates canary` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Where does the deletion live?**
  Options: a one-time manual delete on node a; a line in the session-start wiring check; a line in
  the runner beside the ledger write. Only the runner runs on every node and every adopter, and it
  already owns the file's directory.
  RESOLVED (agent, 2026-10-04, delegated): the runner, per S1.
- **F2 — Does deleting the file take away a remedy `TOOL-aScannedThrottle-8` proposes?**
  That ask lists three remedies for a cold worktree's missing dispatch hint: read the ledger from the
  common dir, fall back per worktree, and fall back to the legacy filename. The legacy file holds
  durations last written 2026-08-20, while the common-dir ledger is rewritten by every bar run in the
  primary tree, so the first remedy always reads newer data than the third.
  RESOLVED (agent, 2026-10-04, delegated): no conflict worth keeping a dead file for; the first remedy
  stands and the third is superseded by it.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; the report's "dead path" re-verified as a dead file with no
  tracked reader, and a fixture run at base observed the file surviving a bar.
- rev-2 · 2026-10-04 · S3 · AC5 · §4 · §7 · M2 cross-read: the runner is a watched path, which
  units 78 and 94 re-stamp for and this spec did not, so S3 re-stamps the manifest, AC5 observes
  it, and §7 names the manifest leg and the two recall legs the manifest's `memory/` path owes.

## 10. Reuse audit

The seam extended is the runner's own delete of a git-dir file it owns,
`rm -f "$gd/gate-queue-status"` in `tools/run-gates/run-gates.sh`, and its already-resolved
`TS_COMMON`. `python tools/codebase-map/reuse_lookup.py "remove a stale legacy cache file the runner
no longer reads"` returned only name-stem neighbours such as `read_text` and `read_conf`, and printed
`unscanned layers: .sh`, so it cannot see the runner; `grep -n 'rm -f "$gd'` over the runner was the
probe and found the one precedent. Recall returned `TOOL-aMeteredTurnstile-3` and
`TOOL-aScannedThrottle-8`, both of which name the dead file, and the aScannedThrottle unit 1 build
record that first measured it as unread. Where the report and the tree disagree: the report calls it
a "path"; at base no path to it remains in code, only the file on disk.

Recall terms used: `python tools/memory-recall/query.py "why was the gate timing cache replaced by
the ledger and is the old timing file still read" --terms "gate-timings.tsv gate-ledger.tsv timing
cache dispatch hint ledger rename orphan rows legacy fallback run-gates profile_bar"`
