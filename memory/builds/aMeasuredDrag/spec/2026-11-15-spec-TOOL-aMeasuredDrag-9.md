# TOOL-aMeasuredDrag-9 — `transition_audit.read_modes` parses each distinct conf blob once, not once per commit

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-9-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-9-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-9-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-9-1-builder.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`transition_audit.read_modes` already reads each distinct `.memory-tree.conf` blob once, in one
`cat-file --batch`, and then calls `read_mode` once per commit. Over this history that is 8720
parses of 272 distinct texts (PINNED, measured at `6d98c39ca` on 2026-11-15). This unit maps each
distinct blob through `read_mode` once and each commit through that map, so the walk the
SessionStart card, the commit-msg hook, the pre-push hook and hygiene check 26 each pay costs one
parse per blob. Finding derived-5 of the 2026-11-15 performance review; no verdict, refusal or
printed line moves.

## 2. Scope (IN)

- **S1** — In `tools/memory-tree/transition_audit.py#read_modes`, the final comprehension
  (`transition_audit.py@419c2700999d:380-381`) becomes two: a `mode_of` dict that maps every blob
  `read_blobs` returned through `read_mode` once, then the per-commit dict reading `mode_of`. A commit
  with no conf blob still reads `shards`. Observed by AC1 and AC2.
- **S2** — The docstring of `read_modes` (`:365-370`) adds that `read_mode` runs once per distinct
  blob, because it is a pure function of the blob text. NOT OBSERVED: a comment carries no
  behaviour, and the review reads it.

## 3. Non-goals (OUT)

- `read_mode` itself, `read_blobs`, the two `cat-file` processes, and every other function of the
  module. The single-blob call in `scan_history` (`:734`) stays as it is.
- A cache across processes or keyed by content. The review's §5 lists that class as structural, and
  the brief leaves it out.
- `migrate_backlog.py#read_conf_mode`, which calls `read_modes` with one rev
  (`tools/memory-tree/migrate_backlog.py@5c41430688ce:1325`). It gains nothing and loses nothing.
- The memory-tree kit version. The lander mints it at the push boundary, and off that boundary
  `kit epoch` prints `owed at the lander` rather than failing
  (`tools/govkit/govkit.py@37f075e4e93e:14044-14049`).
- Re-pointing `read_modes` at a second conf home. That is `PLAY-dConvergedCharter-41`, DEFERRED,
  which keys its reads per distinct blob pair; this change leaves that design open.
- Any help page. No page under `help/` names this module (grep, 2026-11-15).

## 4. Design

### Evidence

Read at `6d98c39ca`. The module is byte-identical at the base `aebbb4a7`.

- `read_modes` resolves each commit's conf blob id in one `cat-file --batch-check`, then reads the
  distinct ids in one `read_blobs` call (`transition_audit.py@419c2700999d:373-379`). It returns
  `read_mode(texts.get(blob) or "")` per commit, so `read_mode` runs once per commit that carries a
  blob (`:380-381`).
- `read_blobs` sets a key for every spec it is asked for, with `None` for an object it cannot read
  (`:345-362`). So every non-empty `blob_of` value is a key of `texts`, and `mode_of[blob]` cannot
  miss.
- `read_mode` parses the text with `tree_lib.parse_conf` into a fresh dict and returns
  `backlog.read_conf(conf).mode`, or `shards` on any exception (`:151-168`). It reads no
  environment, file or clock, so equal text gives an equal answer.
- `.githooks/straggler-guard.test.sh` breaks the module by renaming `def read_mode(`
  (`.githooks/straggler-guard.test.sh@9a59dd9e7a96:363`). The new code still calls `read_mode` by
  name, and the `scan_history` call at `:734` raises first in any case, so that arm reads as before.

### The change

```python
    texts = read_blobs(root, sorted({b for b in blob_of.values() if b}))
    mode_of = {blob: read_mode(text or "") for blob, text in texts.items()}
    return {sha: (mode_of[blob] if blob else "shards") for sha, blob in blob_of.items()}
```

`text or ""` is the old `texts.get(blob) or ""` for a key that is present, so a blob `cat-file`
could not read still parses as the empty text.

The writer checked this body in a scratch copy of the function before writing the spec, over
HEAD's history at `6d98c39ca` on 2026-11-15. It returned a map with the same JSON digest as
`read_modes`, in 0.48 s against 2.30 s (PINNED, node a, one run each).

### The probe

The builder saves this as `u9probe.py` under the run's scratchpad and runs it from the worktree
root. It counts `read_mode` calls by replacing the module attribute, which `read_modes` looks up at
call time, and prints the mode map's digest beside the count and the time.

```python
import collections, hashlib, json, pathlib, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, "tools/memory-tree")
import transition_audit as TA
root = pathlib.Path(".").resolve()
tip = TA.run_git(root, "rev-parse", "HEAD").strip()
_parents, order, _pos = TA.build_graph(root, [tip])
real, calls = TA.read_mode, collections.Counter()
def counted(text):
    calls["n"] += 1
    return real(text)
TA.read_mode = counted
t = time.perf_counter()
modes = TA.read_modes(root, order, TA.derive_conf_rel(root))
dt = time.perf_counter() - t
digest = hashlib.sha1(json.dumps(modes, sort_keys=True).encode()).hexdigest()
print(f"commits={len(order)} read_mode_calls={calls['n']} read_modes_s={dt:.2f} digest={digest}")
```

Run at `6d98c39ca` before any edit, it printed `commits=8750 read_mode_calls=8720
read_modes_s=2.34` (PINNED, 2026-11-15, node a). The count of distinct blobs is 272 (PINNED, same
day), from this pipeline:

```bash
git log --format=%H HEAD | sed 's/$/:.memory-tree.conf/' | git cat-file --batch-check \
  | awk '$2=="blob"{print $1}' | sort -u | wc -l
```

### What this does not check

- A commit whose conf blob `cat-file` lists and cannot read. Old and new both parse it as empty text,
  and no fixture holds one.
- Whether another caller depended on `read_mode` running once per commit. A grep of `tools/`,
  `.githooks/` and `skills/` for `read_modes` and `read_mode` on 2026-11-15 found no such caller.

### Files touched (estimate)

- `tools/memory-tree/transition_audit.py`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. The builder takes every "before" reading
before editing, at the same HEAD as the "after" reading.

- **AC1** — When the §4 probe runs with `python` after the edit, `read_mode_calls` equals the
  distinct-blob count the §4 pipeline prints at the same HEAD, and `commits` is unchanged.
  Red when: the per-commit comprehension stays, so `read_mode_calls` equals the number of commits
  carrying a blob.
  figure: PINNED for the before reading (8720 calls over 8750 commits, 272 blobs, at `6d98c39ca`).
  DERIVED at observation for the after reading, since a commit landing in between moves all three.
- **AC2** — When the §4 probe runs before and after the edit, the `digest` field is the same string,
  so `transition_audit.read_modes` returns a byte-identical map for every commit.
  Red when: `mode_of` is keyed or filled wrongly, so one commit maps to another blob's mode or a
  missing blob stops reading `shards`.
- **AC3** — When `python tools/memory-tree/transition_audit.py` runs with no flag, with
  `--expect-builds`, with `--report` and with `--pin`, each run's stdout, stderr and exit status are
  byte-identical before and after the edit. Each command runs once to warm the delta cache before
  its captured run, because the liveness line prints the cache hit count.
  Red when: a mode moves, so the boundary set, the transition list or the liveness line's counts
  differ.
  figure: PINNED at `6d98c39ca`: the no-flag run printed `transitions examined 4 · merges walked
  694` and exited 0 in 8.28 s wall on 2026-11-15 (PINNED).
- **AC4** — When the §4 probe runs before and after the edit, the builder records both
  `read_modes_s` readings beside `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` run in
  the same shell, in the acceptance ledger.
  Red when: the after reading is not below the before reading by more than the spawn baseline.
  figure: PINNED, 2026-11-15 at `6d98c39ca` on node a: before 2.34 s, baseline 0.35 s real.

## 6. Gates

`transition-audit arms` · `straggler-guard arms` · `memory-hygiene self-test` · `backlog migration selftest` · `kit epoch (shipped bytes move, the version moves)`

`python tools/check-spec-tokens.py --legs-for tools/memory-tree/transition_audit.py`, run on
2026-11-15 at `6d98c39ca`, names only broad guards. The legs above are the ones that run this
module: its own arms, the straggler guard's push arms, hygiene check 26, and the migration tool that
calls `read_modes`. The kit epoch leg reads the shipped byte move. The main loop runs them; this
pass runs none. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief
  `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`, item 9, grounded at `6d98c39ca`. The finding's
  17,647 parses was a count over a different tip set; this spec pins 8720 over HEAD's own history.

## 9. Reuse audit

The seam is the function the finding cites, `tools/memory-tree/transition_audit.py#read_modes`,
edited in place; its own `read_blobs` already de-duplicates the blob reads, and this extends that to
the parses. `python tools/codebase-map/reuse_lookup.py "map each distinct config blob to its parsed
mode once"` ranked name stems only (`parse`, `parse_conf`, `read_blobs_at`), and none memoises a
parse per blob, so no existing seam fits beyond the function itself. Recall returned
`PLAY-dConvergedCharter-41` (DEFERRED; it would re-point `read_modes` at a second conf home, per
distinct blob pair) and the review's own finding derived-5.

Recall terms used: `python tools/memory-recall/query.py "how does the transition audit read each commit's backlog mode from its conf blob" --terms "transition_audit read_modes read_mode conf blob backlog mode builds shards cat-file batch memo"`
