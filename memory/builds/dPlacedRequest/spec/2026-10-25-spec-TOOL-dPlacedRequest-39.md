# TOOL-dPlacedRequest-39 — a feed append that aborts never takes its carrier down

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-39-deviation-391.md](../build/2026-10-25-build-TOOL-dPlacedRequest-39-deviation-391.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 32 at HIGH**. It shares item **H1**, "the node-lock factory is not self-contained
in the `gov_feed_sh` block", with findings 2, 13 and 24, which `TOOL-dPlacedRequest-36`,
`TOOL-dPlacedRequest-37` and `TOOL-dPlacedRequest-38` close. Its failure envelope: post-merge's bar-red
write goes through `add_feed_event` (`TOOL-dPlacedRequest-13` §4), so the first lock take there runs
the factory under `set -u` and an unbound name kills `post-merge.sh` at its marker write; the lander
dies the same way after its push has landed. `TOOL-dPlacedRequest-13` promises the appender never
fails its caller, but an abort is not a failure the appender can catch. This unit repairs
`TOOL-dPlacedRequest-24`, whose factory the append now runs, at order 5: the append runs where an
abort ends only the append, and a lock it took is released on the way out.

## 2. Scope (IN)

- **S1** — The contained append. `add_feed_event` resolves the common dir in the caller's shell, as
  today, then runs its lock, key check, counter and append in a subshell `( … )`. A non-zero subshell
  exit, whether an unbound name under the carrier's `set -u`, an undefined function or a failed
  write, prints one `feed: NOTE - <ref>: the append exited <rc>; nothing written` line on stderr and
  returns 0, so the carrier's next line runs. Observed by AC1.
- **S2** — The lock released on the way out. Inside the subshell an `EXIT` trap calls
  `remove_node_lock <lock dir> <token>` once the lock is taken, so an abort leaves no `gov-feed.lock`
  for the next writer to wait out; `remove_node_lock` checks the owner token, so the trap never clears
  a lock another writer broke and re-made. Observed by AC1.
- **S3** — The append unchanged when nothing aborts. The subshell sets no global a caller reads: the
  common dir is resolved before it, and `seq` and the key check stay inside it. A clean call appends
  one line, and a retried key appends none, as `TOOL-dPlacedRequest-13` S2 states. Observed by AC2.

## 3. Non-goals (OUT)

- No fix to the names the factory reads: findings 2 and 13, `TOOL-dPlacedRequest-36` and
  `TOOL-dPlacedRequest-37`; this unit bounds the damage of any such name, present or future.
- No containment of the driver's queue functions: `add_gov_queue` and `write_gov_queue` run only in
  the driver, which defines every name they read, and report their own exits.
- No retry of an aborted append: the next `--feed check` names the missing event, as for any failed
  append.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-13` — `add_feed_event` and its rule that the append never fails its caller, which this unit extends to an abort; without the appender there is nothing to contain
- **consumes-from** `TOOL-dPlacedRequest-24` — `write_node_lock` and `remove_node_lock`, which the contained append takes and its `EXIT` trap releases; without the factory there is no lock to release
- **hands-off** `TOOL-dPlacedRequest-49` — the contained append's trap order, AC1 and §4, which that unit's items for findings 9, 27 and 34 arm the trap before the take

## 4. Design

### The append

```
add_feed_event ref commit
  dir = GOVFEED_DIR, else git rev-parse --git-common-dir      (caller's shell, cached)
  tree = git rev-parse <commit>^{tree}                         (caller's shell)
  ( write_node_lock "$dir/gov-feed.lock" "$tok" || exit 3
    trap 'remove_node_lock "$dir/gov-feed.lock" "$tok"' EXIT
    key present? exit 0
    read gov-feed.seq; append the line; write the counter )
  rc 0                -> return 0
  rc 3                -> feed: NOTE - lock busy (today's line); return 0
  any other rc        -> feed: NOTE - <ref>: the append exited <rc>; nothing written; return 0
```

Under `set -u` bash ends a subshell on an unbound name with status 1 and runs its `EXIT` trap; the
parent continues. Probed 2026-10-25 under bash 5.3.9 on this Windows node: a subshell taking a `mkdir` lock
then expanding an unset name printed the bash error, ran the trap, removed the lock, and the parent
printed its next line with exit 0.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: `add_feed_event`'s body
- `tools/unattended/unattended.sh`: the inline block, carried
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the containment arms

### Alternatives rejected

- **`set +u` around the append.** It hides an unbound name instead of reporting it, and the factory
  would then compute a deadline from an empty string.
- **A guard per name the block reads.** It closes today's names and not the next one; the subshell
  closes the class.

## 5. Production-readiness checklist

- security — none.
- perf / scale — one subshell fork per governance write, none of which runs on a hot entrypoint of
  `memory/project/fork-ceilings.txt`; the common-dir read stays once per process.
- error / empty / loading states — an abort is a NOTE and rc 0; the lock is released by the trap.
- observability — the NOTE line names the ref and the subshell's exit; bash's own error line names the
  unbound name above it.
- risks — a global the append set for its caller would be lost in the subshell; S3 states there is
  none, and TOOL-aWrittenMethod-2 records the class.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: no guide states the append's failure modes beyond the NOTE line.

## 6. Acceptance criteria

The probe cuts `gov_feed_sh` from `gov-feed.sh` with `awk` into a scratch file, runs in a scratch git
repository with one commit `$h`, and prints a marker after the call.

- **AC1** — When a line `: "$GOVFEED_PLANT_UNSET"` is planted in the scratch cut directly after the
  lock take and `bash -c 'set -u; . cut.sh; add_feed_event refs/gov/bar-red "$h"; echo after'` runs,
  it prints one `feed: NOTE -` line and `after`, exits 0, and no `gov-feed.lock` remains in the common
  dir.
  Red when: the abort ends the carrier or leaves the lock held, the staged case being the cut without
  the subshell, which prints `GOVFEED_PLANT_UNSET: unbound variable` and never `after`.
- **AC2** — When the same probe runs without the plant, `gov-feed.log` holds one line with `seq` 1;
  run again with the same ref and commit, it still holds one line.
  Red when: the subshell loses the append or the key check.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the contained append over a planted unbound name and a clean retry, staged against the uncontained body · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does the append survive an abort inside it?** (a) A subshell with an `EXIT` trap that
  releases the lock; (b) `set +u` around the call; (c) no containment, relying on the block being
  clean. (b) masks the name; (c) leaves the lander dying after a landed push the next time a name
  slips. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, `TOOL-dPlacedRequest-13`'s
  never-fails-its-caller rule carried to an abort. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  32 (HIGH, item H1, shared with findings 2, 13 and 24).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-13`'s `add_feed_event` and its NOTE-and-return-0 rule,
borrowed from the health appender (`tools/lib/health-log.sh:21-23`), and `TOOL-dPlacedRequest-24`'s
`remove_node_lock`. `python tools/codebase-map/reuse_lookup.py "contain a failing append so it never
kills the caller"` ranked `fail`, `stage_or_fail` and `check_self_containment`, name stems only; the
last checks Python imports, not shell exits. `python tools/memory-recall/query.py "how does a feed
append avoid failing its caller"` returned TOOL-aWrittenMethod-2 (a global set inside a subshell never
reaches the caller, which S3 answers), `TOOL-dPlacedRequest-13` §4 and TOOL-aWokenSentinel-18; none
disagrees with source.

Recall terms used: add_feed_event never fails caller NOTE subshell set -u abort lock release trap
