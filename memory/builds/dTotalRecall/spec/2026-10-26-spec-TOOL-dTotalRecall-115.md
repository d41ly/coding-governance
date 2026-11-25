# TOOL-dTotalRecall-115 — the change feed appends a record event once across a merge landing, and its check reads every logged commit as a tip

**Status:** INPROGRESS · rev-1 · 2026-11-25 · node d · Tier-2 · base acbb74bb · streams tooling · order 43

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-115-widen-27.md](../build/2026-11-25-build-TOOL-dTotalRecall-115-widen-27.md) | widen | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-115-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-115-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-115-spec-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-115-spec-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-115-spec-writer.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-115-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

H1 of the closing review (findings 4, 8 and 19 of `2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md`):
after a merge landing the feed's record walk re-lists commits it already fed, the append writes them again, and
`check_feed` is falsely red. Every landing here is a merge. This unit makes the append idempotent by key and gives
the check an anchor that dominates what the feed holds.

## 2. Scope (IN)

- **S1** — `tools/lib/gov-feed.sh#derive_record_rows` leaves out every row whose (ref, blob, commit) key a `record` line of
  the log already holds, read under the node lock its caller holds; a refused walk still returns non-zero (§4).
  Observed by AC1.
- **S2** — `check_feed`'s record arm derives the expected set from every logged `record` commit of the ref that a
  branch or remote-tracking branch reaches, the union as the walk's tips, read by `derive_record_events` from
  stdin (§4). Observed by AC1 and AC3.
- **S3** — `check_feed`'s record arm prints `duplicate <ref> <commit>` for a (ref, blob, commit) key a second line
  holds, and the ref arm passes over `record` lines, so one duplicate prints once (§4). Observed by AC2.
- **S4** — The block's header comment says what the append skips, what the check walks from, and no longer holds the clause
  on a rewritten default branch re-listing commits the feed holds, which S1 ends. Observed by AC5.
- **S5** — The four carriers of the block, `tools/push-main.sh`, `tools/run-gates/post-merge.sh`,
  `tools/unattended/unattended.sh` and `tools/memory-tree/gov-claim.sh`, take its bytes. Observed by AC4.
- **S6** — The `rr_` block of `tools/unattended/unattended.test.sh` gains the merge landing (§4 "The arms"), its
  `whole.sh` mutant is re-cut, and the floors move. Observed by AC6.
- **S7** — The `shell-role` rows of the five shell files above and of the suite take the measured count, each risen
  row through `python tools/memory-tree/ratchet.py widen shell-role --key <path> --reason <text> --unit
  TOOL-dTotalRecall-115`. No `spawn-idiom-sites`, `quoting-sites`, `temp-name-sites` or `fork-ceilings` row moves:
  the new reads are here-strings. Observed by AC7.

## 3. Non-goals (OUT)

- The per-ref landed-tip cursor, finding 4's equal alternative (§4 "Alternatives rejected").
- The merge commits themselves: the walk stays `--no-merges`, so a merge's own resolution joins no event.
- A repair of a feed that already holds duplicates: this node's log holds no `record` line (DERIVED 2026-11-25,
  `gov-feed.log` under the common dir), and a node that has some reads each as `duplicate` until its feed is rebuilt.
- `write_feed`, `derive_feed_row` and the ref arm's own rules, the `record` skip of S3 excepted.

### Edges

- **consumes-from** external — the closing review's report and the landed units whose code it read
- **hands-off** `TOOL-dTotalRecall-116` — this unit's bytes of the symbol map, the shell-role rows
- **hands-off** `TOOL-dTotalRecall-117` — this unit's bytes of the symbol map, the shell-role rows
- **hands-off** `TOOL-dTotalRecall-118` — this unit's bytes of the symbol map
- **hands-off** `TOOL-dTotalRecall-119` — this unit's bytes of the symbol map, the shell-role rows
- **hands-off** `TOOL-dTotalRecall-120` — this unit's bytes of the symbol map, the shell-role rows
- **hands-off** `TOOL-dTotalRecall-121` — this unit's bytes of the symbol map, the shell-role rows, the claim CLI
- **hands-off** external — the close's next bar, the held suites and the landing, each the main loop's

## 4. Design

Read at `acbb74bb` on 2026-11-25. The report holds: the walk starts at the newest `record` line's commit, is
`--no-merges`, and nothing tests a key after it; `check_feed` walks to that same commit. The probe below printed, on
today's block, the second landing's check `extra` with exit 1, then five lines for four keys after the third (PINNED
2026-11-25), and with the edits below four lines for four keys and every check 0 (PINNED 2026-11-25).

### The append

```bash
derive_record_rows() { # ref · tip · feed log -> derive_record_events' rows the log does not hold, walked from that line's commit, the whole history where none
  local from="" rows
  if [ -f "$3" ]; then from=$(…) || return 1; fi          # the read as it stands
  rows=$(derive_record_events "$1" "$2" ${from:+"$from"}) || return 1
  [ -n "$rows" ] || return 0
  FEED_FILE="$3" awk -F'\t' '
    BEGIN { f = ENVIRON["FEED_FILE"]; while ((getline ln < f) > 0) { sub(/\r$/, "", ln)
              if (split(ln, x, "\t") == 6 && x[3] == "record") k[x[2] SUBSEP x[4] SUBSEP x[5]] = 1 } }
    !(($1 SUBSEP $3 SUBSEP $4) in k)' <<<"$rows"
}
```

The walk's start is unchanged, so a commit the start dominates is not listed and a listed one the log holds is
dropped. The rows stay in walk order, a parent's before its child's.

### The check

The ref arm's `awk`, after its `torn` test, gains `if (x[3] == "record") continue`. The record arm reads tips in
place of one tip and prints a repeated key:

```bash
tips=$(FEED_FILE="$f" awk -F'\t' -v ref="$g" '
  { sub(/\r$/, ""); r[$0] = 1 }
  END { f = ENVIRON["FEED_FILE"]
        while ((getline ln < f) > 0) { sub(/\r$/, "", ln)
          if (split(ln, x, "\t") == 6 && x[2] == ref && x[3] == "record" && (x[5] in r) && !(x[5] in t)) {
            t[x[5]] = 1; print x[5] } } }' <<<"$rr")
dr=""
if [ -n "$tips" ] && ! dr=$(derive_record_events "$g" --stdin <<<"$tips"); then
  printf 'unread %s walk\n' "$g"; rc=1; continue
fi
```

and, in the compare, `if (k in got) { print "duplicate " ref " " x[5]; bad = 1; continue }` ahead of `got[k] = 1`.
`derive_record_events` needs no edit: its tip argument lands before the `--`, where git reads `--stdin`, and its two
earlier git reads take nothing from stdin. A `git log --stdin` over this repository's memory
commits, 10214 of them, returned in 3.4 s (PINNED 2026-11-25, node d), and the check takes no lock.

### The probe

In a scratch repository, with `gov-ref.sh` and the canonical file sourced and the two health functions stubbed: commit
`p` under `memory/`; branch `b1` with commit `b`; back on `main`, commit `m1`; append and check; merge `b1`
`--no-ff`; append and check; commit `n`; append and check; append again; then copy the log's first line to its end
and check.

### The arms

The `rr_` block's clone `a` gains the probe's sequence after its AC8 case, over keys of its own: a branch forked
before the last fed commit, merged `--no-ff`, two landings, then the same call again. Its arms assert one line per
key (`sort | uniq -d` over the key columns empty) and the check's exit after each landing, and one copied line
printing `duplicate` once. `whole.sh` today cuts the walk's start and expects the history again; under S1 that copy
appends nothing, so the mutant cuts the start and turns the key test into `1`, and its arm's expected count stands.
A second mutant, the key test alone turned into `1`, is the merge arm's staged red.

### Inventory

Minted: none in the block, the local names `rows` and `tips` excepted; the suite's mutant file `keyless.sh` under
`$rr_d` and its `rr_` output keys.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`
- `tools/push-main.sh`
- `tools/run-gates/post-merge.sh`
- `tools/unattended/unattended.sh`
- `tools/memory-tree/gov-claim.sh`
- `tools/unattended/unattended.test.sh`
- `memory/project/shell-role.txt`
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (the widen record and this unit's ledger)

### Alternatives rejected

- **A per-ref landed-tip cursor, read by both append and check.** Sound too, and a second stored fact that can drift
  from the log it describes; the log's own keys need no new file and also cover a rewritten branch.
- **Every logged commit excluded through `--stdin`.** It drops a commit whose rows were torn mid-write; the key test
  re-appends the rows it lacks.
- **Dedupe alone.** INSTANCE-ONLY: the check keeps its non-dominating anchor.

## 5. Production-readiness checklist

- security — no new surface; the ref and the paths pass through as they do.
- perf / scale — one `awk` pass over the log more per record append, under the node lock; the check walks from every
  logged tip and is unlocked.
- error / empty / loading states — an absent log drops nothing; a refused walk returns non-zero and prints the standing NOTE.
- observability — `duplicate` names the ref and the commit.
- risks — a log line planted with a side branch's commit widens the check's walk and reads that branch's commits
  `missing`, where today it reads `extra`.
- testing — AC1 to AC7 by the pass; §7's arm by the main loop.
- migration — none; a feed holding duplicates prints them.
- user docs — N/A, `help/loop.md` already names each `missing`, `duplicate` and `extra` line.

## 6. Acceptance criteria

- **AC1** — When §4's probe runs over `tools/lib/gov-feed.sh`, the feed holds 2, 3, 4 and 4 lines (DERIVED, its commits)
  after the four appends, four distinct keys, and `check_feed refs/gov/remote/` exits 0 after each landing.
  Red when: the key test is turned into `1`, or the check walks from the newest line alone; today it prints `extra`.
- **AC2** — When the probe's first line is copied to the log's end, `check_feed` prints one `duplicate refs/heads/main`
  line naming that commit, no `extra` line, and exits 1.
  Red when: the record arm compares sets alone, or the ref arm prints the line too.
- **AC3** — When the probe's log gains a `record` line of a commit on no branch, `check_feed` prints `extra` for it
  alone; and when a commit is landed with no append and a later one is logged by hand, it prints `missing` for the
  first, each with exit 1.
  Red when: every logged commit is a tip whether a branch reaches it or not, or the walk stops at a tip's parents.
- **AC4** — When `awk '/^# >>> gov_feed_sh/{f=1} f{print} /^# <<< gov_feed_sh/{exit}' <file>` runs over the canonical
  file and each of the four carriers, the five outputs are byte-identical, and `bash -n` passes over each carrier.
  Red when: a carrier keeps the old block.
- **AC5** — When `grep -c 'can list commits the feed holds' tools/lib/gov-feed.sh` runs, it prints 0 (DERIVED, S4), and
  `grep -n 'SETS' tools/lib/gov-feed.sh` shows the record arm's line naming the duplicate it prints.
  Red when: the header still discloses a limit the code no longer has.
- **AC6** — When `bash -n tools/unattended/unattended.test.sh` passes and `grep -c 'keyless.sh' tools/unattended/unattended.test.sh`
  runs, it prints at least 2 (DERIVED, the mutant made and sourced), and the ledger names each floor before and after.
  Red when: the mutant is made and never run, or a floor stands below its arms.
- **AC7** — When `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` runs, each of the six paths of
  S7 reads the count its row of `memory/project/shell-role.txt` holds.
  Red when: a row stands under or over its measure.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `ratchet (never gains)` · `ratchet (both ways)` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a fork spent on builtin work)` · `push-main self-test` · `unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the `rr_` block's merge landing and copied line, staged by the key test turned into `1` and by today's block, which prints `extra` · `FLOOR_ASSERTIONS` and the floor of the shard holding the block, each by the arms added

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-114` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none
- **F2 — Is the append's key test or a stored cursor the class-level fix?** Options: (a) the key test, the review's
  class-level fix; (b) the cursor, its equal alternative. (b) adds a stored fact beside the log that owns it.
  RESOLVED (agent, 2026-11-25, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's H1.

## 10. Reuse audit

The seams, each read at `acbb74bb`: `tools/lib/gov-feed.sh#write_feed_lines`, the one append path that hands its
builder the log under the lock; `derive_record_events`, whose tip argument already admits `--stdin`; the
`getline` read of `FEED_FILE` that `derive_feed_events` and the record arm use; and the suite's `mutate` helper.
`python tools/codebase-map/reuse_lookup.py "append only rows whose key a log does not already hold"` ranked no seam:
no existing seam fits beyond these. The task's two build-folder walks and `id_grammar.py#read_kept_reason` read no
feed.

Recall terms used: `python tools/memory-recall/query.py "change feed record events appended once across a merge landing" --terms "gov-feed derive_record_rows check_feed merge landing idempotence duplicate"`
