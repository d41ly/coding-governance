# TOOL-dDeclaredLoop-65 — the remote's freshness is the time of the last fetch, read from what a fetch and a clone write

**Status:** CLOSED · rev-3 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-65-deviation-651.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-65-deviation-651.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-65-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-65-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-65-deviation-652.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-65-deviation-652.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-65-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-65-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-65-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-65-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-65-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-65-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 55 at HIGH**, its item **H7**, alone in that item. The position engine reads the
remote-tracking ref's age from that ref's newest reflog entry (`tools/loop/position.py#read_remote_claim`),
and `TOOL-dDeclaredLoop-56` S36 keeps that age. A fresh clone writes no reflog for
`refs/remotes/origin/main`, and a fetch that does not move the ref writes no entry, so the reflog
measures when the remote last moved, not when it was last fetched. On a fresh clone, and on any remote
quiet longer than the bound, the engine answers `stale-remote` right after a fetch, and
`tools/loop/position.py#derive_answer` ranks that answer above `act`, so `--plan`'s next line stalls.
This unit takes the report's corrected fix. It repairs `TOOL-dDeclaredLoop-56`.

## 2. Scope (IN)

- **S1** — In `tools/loop/position.py`, where the default branch's remote-tracking ref resolves, the
  remote claim's age is the time of the last fetch: the newest of the mtime of `FETCH_HEAD` in the
  common git directory, the mtime of each `worktrees/*/FETCH_HEAD` under it, and the time of the
  tracking ref's newest reflog entry where it has one. The common directory is the answer of
  `git rev-parse --git-common-dir` run in the repository, a relative answer read against the
  repository's path. A file whose mtime cannot be read is skipped, never read as zero. The claim's
  name, key and verdict keep their shape, and the absent reading of `TOOL-dDeclaredLoop-56` S36, where
  the ref does not resolve, is not reached by this item. Observed by AC2, AC3.
- **S2** — When the population of S1 is empty, as on a fresh clone, the clone's own time stands in:
  the newest `clone: ` entry of the reflog of `refs/heads/<default>`, so a just-cloned tree reads
  fresh. The clone entry is read only then. With neither, the claim is unread and the answer
  `stale-remote`, as `derive_answer` ranks it. Observed by AC1, AC3.
- **S3** — The tracking ref's `read —` line names the reading:
  `read — <ref>@<sha8> · fetched <n>s ago · from <source>`, where `<n>` is the whole seconds from the
  time read to the engine's `now`, never below 0, and `<source>` is `FETCH_HEAD`, `reflog` or `clone`
  for whichever gave the newest time; with no time read the line is `read — <ref>@<sha8> · fetched never`.
  A stale answer so says which artefact was old. Observed by AC1, AC2, AC3, AC5.
- **S4** — The plants `fresh-clone`, `quiet-remote` and `offline-stale` join `PLANTS` of
  `position.py`, listed ahead of `plan-line` and `status-line` so those two stay the last two, each
  staged as §4 "The plants" gives. The check of the `stale-remote` plant, as `TOOL-dDeclaredLoop-56`
  S36 restages it, also owes the line ending `from reflog`. Observed by AC1, AC2, AC3, AC5.
- **S5** — `help/loop.md`'s `stale-remote` paragraph states the last-fetch reading and its three
  sources, and its fixture list names the three plants. The module docstring of `position.py` states
  the same reading in the answer's `stale-remote` clause, and its "WHAT THIS DOES NOT CHECK" paragraph
  names a fetch run with `--no-write-fetch-head` and a `FETCH_HEAD` whose content is not read, in place
  of the fetch-against-move limit this unit closes. Observed by AC4.

## 3. Non-goals (OUT)

- The no-remote reading of `TOOL-dDeclaredLoop-56` S36: unchanged, and so is a ladder refusal, which
  still answers `stale-remote`.
- The claim's key: it stays over `<ref>@<sha>` (`tools/loop/claims.py#derive_claim_key`). The fetch
  time is the claim's age, never its identity.
- The driver's own claim fetch, `tools/unattended/unattended.sh#read_claims`, which fetches into a
  private namespace and writes no `FETCH_HEAD`: it reads claims, never the default branch's freshness.
- A `FETCH_HEAD`'s content: `TOOL-dDeclaredLoop-74` validates it.
- `tools/loop/README.md`: its paragraph on `position.py` names no age source, and the plants join
  ahead of the last two, so its "the last two over the unattended driver" stays true. It is not edited.
- A checklist entry that a time-of-last-event read names the artefact the event writes, the finding's
  left-shift: the class is recorded at the close; S4 is this reading's no-op fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-56` — S36's remote reading in `tools/loop/position.py`, its absent case and its restaged `stale-remote` scratch, on whose aged tracking ref the `quiet-remote` plant stages; this unit restates its age source
- **hands-off** `TOOL-dDeclaredLoop-74` — the `FETCH_HEAD` members of S1's population, which that unit validates by content (the round-3 spec audit's id 45)
- **hands-off** `TOOL-dDeclaredLoop-75` — the other-branch plant, the absolute common directory and the fixture's git config (the round-3 spec audit's ids 8, 15, 25); this pass keeps the `loop position fixtures` leg green (id 31)

## 4. Design

### Evidence

- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1: after `git clone up cl`, `git reflog exists
  refs/remotes/origin/main` exited 1 and `.git/FETCH_HEAD` did not exist, while the reflog of
  `refs/heads/main` held `clone: from <url>`; a `git fetch` that moved nothing wrote `.git/FETCH_HEAD`
  with that minute's mtime and left the tracking ref's reflog at zero entries: PINNED, that date.
- The same probe: `git rev-parse --git-path FETCH_HEAD` resolved to the current worktree's git
  directory, so a fetch run in another worktree of the same clone is found only under the common
  directory's `worktrees/`: PINNED, that date.
- This pass could not re-run either probe, because the worktree it ran in refuses a git command aimed
  at a scratch repository outside it. AC1 and AC2 re-observe both at the close, and a git that writes
  otherwise turns them red.
- Read through `git show` at the branch tip `689e1b07d`:
  - `tools/loop/position.py#read_remote_claim` names the remote and branch through
    `tools/loop/claims.py#resolve_remote`, reads the tracking ref's sha, and takes `at` from
    `git reflog show --date=unix -n1 --format=%gd <ref>`, parsing `@{<unix>}`. It keys the claim over
    `<ref>@<sha>`, judges it with `tools/loop/claims.py#derive_claim_verdict`, which reads `at` against
    the bound for the `remote` class alone, and returns the sha, the ref and the claim.
  - `tools/loop/position.py#derive_position_into` is its one caller. It uses the ref only to append
    `<ref>@<sha8>` to the read list where the sha resolves, and passes the claim's `fresh` verdict to
    `derive_answer`, which answers `stale-remote` ahead of every other answer.
  - `tools/loop/position.py#render_position_lines` prints each read-list entry as `read — <entry>`.
  - `tools/loop/position.py#write_position_plant` builds every plant as a `git init` of `<top>/r` with
    a bare `<top>/o.git` it pushes to, and builds no clone and no linked worktree.
    `tools/loop/position.py#render_handover` writes a bound of 5400 PINNED seconds.
  - `tools/loop/loop_witness.py#read_git` runs `git -C <repo>`, and
    `tools/loop/loop_witness.py#run_fixture_git` runs git in a directory under a fixed identity.
  - `PLANTS` holds 21 PINNED plants, `plan-line` and `status-line` last.

### The reading

```
read_fetch_time(repo, ref, branch) -> (at, source), or (None, None)
  common = repo / (git rev-parse --git-common-dir)          # an absolute answer stands as it is
  times  = [(mtime of f, "FETCH_HEAD") for f in common/FETCH_HEAD, sorted(common/worktrees/*/FETCH_HEAD)
            where os.stat(f) answers]
         + [(newest reflog time of ref, "reflog")]         where ref's reflog has an entry
  if times is empty:
      times = [(time of the newest "clone: " entry of refs/heads/<branch>'s reflog, "clone")]
                                                            where one exists
  the newest of times, the first listed on a tie; (None, None) when times is empty
```

`read_remote_claim` calls it where its inline reflog read sits and takes `at` from it. Its second value
is the tracking ref's whole read entry, `<ref>@<sha8> · fetched <n>s ago · from <source>` or
`<ref>@<sha8> · fetched never`, which `derive_position_into` appends where it appends `<ref>@<sha8>`.
`<n>` is computed against the `now` `derive_position_into` already reads. The clone entry is read with
`--date=unix` and `--format=%gd%x09%gs`, its time parsed as the reflog read parses it. This is written on
`TOOL-dDeclaredLoop-56` rev-6, which keeps the reflog read and adds the absent case ahead of it; where
its built shape moved the read entry, the entry this unit extends is the one naming the tracking ref.

### The plants

| Plant | Staged | Owed |
|---|---|---|
| `fresh-clone` | the generic plant's `r`, pushed to `o.git`, then `git clone -q --template= o.git <top>/c`; the engine reads `c` | the answer is not `stale-remote`; the ref's read line ends `from clone` |
| `quiet-remote` | the restaged `stale-remote` scratch of 56 S36, whose tracking ref's newest reflog entry is older than the bound; `git worktree add --detach <top>/w`, then `git fetch -q origin` in `w`; the engine reads `r` | the answer is not `stale-remote`; the line ends `from FETCH_HEAD` |
| `offline-stale` | the `fresh-clone` clone, `git fetch -q origin` in it, then `os.utime` dating its `FETCH_HEAD` back by twice the hand-over's bound; the engine reads `c` | the answer is `stale-remote`; the line ends `from FETCH_HEAD` |

Each plant's owed reading is one entry of `tools/loop/position.py#check_plant`'s table, read from the
answer and `render_position_lines`. `write_position_plant` returns the clone's path as the repository
for the two clone plants, and `run_plant`'s `remove_tree(top)` takes the clone and the worktree with
the rest. The fetch in `offline-stale` moves no ref, so the clone holds no tracking reflog and the
population is the one dated `FETCH_HEAD`; the clone entry, fresh, is the source a wrong fallback reads.

### Inventory

| Minted | Kind | Where | Lexicon |
|---|---|---|---|
| `read_fetch_time` | Python function | `tools/loop/position.py` | `py.function`, `OK` |
| `fresh-clone`, `quiet-remote`, `offline-stale` | plants | `PLANTS` of `tools/loop/position.py` | not graded |

`python tools/lexicon/lexicon.py --suggest read_fetch_time --as py.function` printed OK, leading with
`read`. It ran in this spec's worktree at `179486e8f`, whose lexicon kit differs from the branch tip's
only in tag-name grading, the `stage` keys of its two legs and `VERB_OFFENDER_PIN`.

### Files touched (estimate)

- `tools/loop/position.py`
- `help/loop.md`
- `memory/map/generated/symbols.json`, with any generated sibling `gen_map.py --write` rewrites
- `tools/run-gates/selftest-budgets.txt`, only where the close's timed reading re-prices the leg's row

### Alternatives rejected

- **A stamp the driver writes after each fetch.** A fetch the operator runs by hand writes no stamp and
  would read stale; every fetch but one run with `--no-write-fetch-head` writes `FETCH_HEAD`.
- **The current worktree's `FETCH_HEAD` alone.** A fetch from the main worktree would leave every linked
  worktree reading stale.
- **`offline-stale` on the restaged `stale-remote` scratch, as 56's sweep foresaw.** That scratch is a
  `git init`, which holds no clone entry, so the plant could not see the clone entry standing in beside
  a stale source; the clone is the scratch that can.

## 5. Production-readiness checklist

- security — reads only: one `rev-parse`, a few `stat` calls, and the reflog reads git already answers.
- perf / scale — one git spawn added on every reading, the common directory; one more only where the
  population is empty.
- error / empty / loading states — S2 names the empty case and S3 prints it as `fetched never`; an
  unreadable mtime is skipped, never zero.
- observability — S3's age and source on the tracking ref's `read —` line.
- risks — `git fetch --no-write-fetch-head` writes no `FETCH_HEAD`: such a fetch reads by the reflog
  when the ref moved, and as stale when it did not, the conservative side. An mtime ahead of `now`
  reads as `fetched 0s ago`. The leg's ceiling, 300 PINNED seconds in `tools/gate-legs.json`, already
  sits under its 411 PINNED seconds budget, and three plants add to both readings; this unit moves no
  ceiling, and a reading past it is recorded at the close.
- testing — AC1 to AC3 and AC5 as plants, AC4 as a page probe; the arm under §7, observed RED then
  GREEN at the close. `fetched never` is not planted: every scratch whose tracking ref resolves holds a
  push's reflog entry or a clone entry.
- migration — none; no stored data changes shape.
- user docs — `help/loop.md` (S5).

### The sweep

Read at the branch tip `689e1b07d`; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `read_remote_claim`'s `at` (S1, S2) | `derive_position_into`, its one caller; `derive_answer` through the verdict; `check_plant`'s `steps` entry, which reads the remote claim's name, key and verdict | the claim's three fields keep their shape; the new time includes the reflog time, so it is never older and a fresh reading stays fresh; only a reading that expects `stale-remote` can move, and that word is spelled in `tools/loop/position.py` and `help/loop.md` alone |
| `read_remote_claim`'s second value, the read entry in place of the bare ref | `derive_position_into` alone | it appends the entry where it appended `<ref>@<sha8>` |
| the tracking ref's `read —` line (S3) | `render_position_lines` and `--json`'s `read` list; `tools/loop/composition.py#run_composition_plant`, which asks for the `composition@` entry alone; `check_plant`'s `steps` entry, which asks for an entry opening `memory/`; `tools/loop/scenario.py#run_scenario_plant`, which reads the `position —` and `scenario=` lines; the driver's `--status`, which prints the lines | no reader parses the ref's entry; each named reader asks for another entry |
| 56's restaged `stale-remote` plant | its staging at this unit's pass | it reads stale `from reflog` while its staging writes no `FETCH_HEAD` and is no clone; the builder reads that staging at the pass, and where it writes a `FETCH_HEAD`, dates that file past the bound with `os.utime` in the same plant |
| `PLANTS` gains three (S4) | `run_selftest`, which runs every entry; the leg `loop position fixtures` and its budget row, 411 PINNED seconds; `tools/loop/README.md`'s "the last two over the unattended driver" and `help/loop.md`'s "the last two run the unattended driver" | the three sit ahead of `plan-line` and `status-line`; the row is re-priced from a timed reading of the leg alone where that reading passes it |
| the `--plant` values | the `script:{prefix}/loop/position.py` row of `tools/govkit/usage.toml`, its `--plant=` flag; the anchor `script:tools/loop/position.py 8d078234` on `help/loop.md` | `tools/govkit/docs_leg.py#derive_usage_fingerprint` hashes the row's fields, which name the flag and not its values, so the anchor stays current |
| `read_fetch_time` minted | `memory/map/generated/symbols.json` under `codebase-map coverage + freshness`; the lexicon's verb census | the map is re-rendered by `gen_map.py --write` in the pass commit; the name grades OK |
| the docstring and the help paragraph (S5) | `install-prefix (shipped surface)`, whose population holds `position.py` and not `help/`; `docs` and `help page commands` | the new text spells no kit path and adds no command span, no link and no flag |
| this spec's line citation | `memory/project/positional-refs.txt`, its 1 PINNED row for this spec, under `positional (the citation check alone)` | this revision cites symbols only, so the commit landing it runs `python tools/playbook/positional.py shrink` |
| sibling specs | `TOOL-dDeclaredLoop-74` (S1, AC2: `quiet-remote` and the `from FETCH_HEAD` ending), `TOOL-dDeclaredLoop-75` (S12, S17, S22), `TOOL-dDeclaredLoop-77` (the `from FETCH_HEAD` ending) | the plant names, the labels AC1 to AC3 and the line's `from <source>` ending keep their meaning; each re-grounds on S3's line at its own pass |

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -e 'read_remote_claim' "$B" -- tools                         # position.py alone: the def and one call
git grep -n -e 'stale-remote' "$B" -- tools help skills                  # position.py and help/loop.md alone
git grep -n -e '\["read"\]' "$B" -- tools/loop                           # position.py, and composition.py's rename check
git grep -n -e 'position\.py' "$B" -- tools skills                       # every caller of the engine
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop position fixtures'   # 411
git show "$B:tools/govkit/usage.toml" | grep -A3 'script:{prefix}/loop/position.py'
git show "$B:help/loop.md" | grep -n 'usage: script:tools/loop/position.py'          # 8d078234
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-65.md'   # 1
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED, since the one name
  minted, `read_fetch_time`, grades OK (§4 "Inventory").
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead, since
  no ceiling or pin is raised.
- The refusal ceilings and families: `tools/memory-tree/check-arms.py#scan_refusal_sites` reads tracked
  `*.sh` files alone, and this unit edits none. The driver's ceiling in `REFUSAL_CEILINGS` stays 343
  PINNED, and `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb and no flag is added; the three plants are values of the anchored `--plant`.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added; no file of the
  memory-tree engine `check-verdict-epoch.sh` delegates to is edited; no data changes shape, so no
  `[[upgrade]]` row is owed; neither edited path is on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md`.
- Shipped bytes: the loop kit's version is minted at the lander, as `tools/govkit/govkit.py#cmd_epoch`
  states, so the branch owes no bump.

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                  # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'               # the driver's 343
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
```

### Dependency

`TOOL-dDeclaredLoop-56` (order 36, committed rev-6) is read for S36: the absent reading, the reflog age it
keeps and the restaged `stale-remote` scratch, on which `quiet-remote` stages. It edits
`read_remote_claim`, `write_position_plant`, `check_plant`, `PLANTS` and `help/loop.md`'s `stale-remote`
paragraph before this unit, and this unit edits each after it. `TOOL-dDeclaredLoop-33` (order 34,
committed rev-7) extracts `read_build_items` out of `derive_position_into`, and `TOOL-dDeclaredLoop-72`
(order 36, committed rev-6) moves that function's memory-root read onto `resolve_memory_root`; neither
touches the remote read. `TOOL-dDeclaredLoop-53`, `-64` and `-70` edit `help/loop.md` at other sections.
At order 37, `TOOL-dDeclaredLoop-68` edits `tools/loop/loop_witness.py`'s witness normaliser and leaves
`read_git` and `run_fixture_git`, which this unit calls, as they are; `TOOL-dDeclaredLoop-76` edits
`loop_lib.py`, `budget.py` and `breakpoints.py`, none of them here. At order 38, `TOOL-dDeclaredLoop-67`
adds its own plant to `PLANTS` and `TOOL-dDeclaredLoop-74` validates S1's `FETCH_HEAD` members; at
order 39, `TOOL-dDeclaredLoop-75` and `TOOL-dDeclaredLoop-77` read the same reading. `TOOL-dDeclaredLoop-34`
is deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s numeric direction against ask
TOOL-dDeclaredLoop-114; neither shares the remote read. Every code claim was read through `git show` at
the branch tip; the lexicon and the reuse probe ran on the worktree at `179486e8f`, cut from main.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant fresh-clone` runs in `tools/loop/`, it prints
  `position: fixture · fresh-clone · held`, the answer is not `stale-remote`, and the tracking ref's
  `read —` line ends `from clone`.
  Red when: the reflog is the only source, or the clone entry is never read, so the clone reads
  unread and answers `stale-remote`.
- **AC2** — When `python position.py --fixture --plant quiet-remote` runs in `tools/loop/`, it prints
  `position: fixture · quiet-remote · held`, the answer is not `stale-remote`, and the line ends
  `from FETCH_HEAD`.
  Red when: the age is the ref's last move, or only the reading worktree's own `FETCH_HEAD` is read,
  so a fetch from a linked worktree leaves the tree stale.
- **AC3** — When `python position.py --fixture --plant offline-stale` runs in `tools/loop/`, it prints
  `position: fixture · offline-stale · held`, the answer is `stale-remote`, and the line ends
  `from FETCH_HEAD`.
  Red when: the clone entry is read beside a `FETCH_HEAD`, or a `FETCH_HEAD` is missing from the
  population so the clone entry stands in, and the stale tree reads fresh.
- **AC4** — When `grep -c "from clone" loop.md` runs in `help/`, it prints 1 or more, and
  `grep -c "finds nothing new leaves it stale" loop.md` prints 0.
  Red when: the page still says the reflog's age is the remote's freshness.
- **AC5** — When `python position.py --fixture --plant stale-remote` runs in `tools/loop/`, it prints
  `position: fixture · stale-remote · held`, and the tracking ref's line ends `from reflog`.
  Red when: the line names no source, or a source the restaged scratch does not hold.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

The pass keeps the sibling-minted `loop position fixtures` leg green, which runs every plant of
`position.py`. That leg is in the branch's `tools/gate-legs.json` and not in main's, which the spec-token
checker reads, so it is named here and not on the leg line, as `TOOL-dDeclaredLoop-74` §7 names it.

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC5 · the fresh-clone, quiet-remote and offline-stale plants and the stale-remote plant's source, staged against the reflog-only reading `TOOL-dDeclaredLoop-56` S36 keeps · the `loop position fixtures` budget row, re-priced where the close's timed reading passes it

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Where does the reading name its age and source?** rev-2 wrote a `remote: fresh · fetched <age>
  ago · from <source>` line, a shape the engine prints nowhere. Options: (a) the tracking ref's existing
  `read —` line gains ` · fetched <n>s ago · from <source>`; (b) a second `read —` line of its own, in
  rev-2's shape; (c) the remote tip's `claim —` line gains the field. (b) prints two lines about one ref,
  its `fresh` restating the claim line's verdict; (c) puts a field on a line `render_position_lines` prints
  alike for every claim. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), under the
  run's mandate, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-65-1-spec-writer`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 55 (HIGH, item H7).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-74 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S5 · AC1 to AC5 · §8 F2 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `689e1b07d` and on the committed spec of TOOL-dDeclaredLoop-56
  rev-6, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-65-1-spec-writer`: S1 names the common
  directory's resolution and reaches only a resolving ref; S3's source rides the ref's `read —` line by F2;
  S4 places the plants ahead of the last two, stages `quiet-remote` on 56's restaged scratch from a linked
  worktree and `offline-stale` on a clone, and owes `stale-remote` its source by AC5; S5 and AC4 bring
  `help/loop.md` and the docstring current; the driver's claim fetch cited by symbol; the sweep.

## 10. Reuse audit

The seam is `tools/loop/position.py#read_remote_claim`, the engine's one remote reading, whose inline
reflog read the new `read_fetch_time` takes over; no second reader of a fetch time exists to extend.
`python tools/codebase-map/reuse_lookup.py "time of the last fetch of a remote"`, run on the worktree at
`179486e8f`, which lacks the loop kit, ranked `resolve_remote`, `parse_time` (`tools/runlog/extract.py`),
`build_remote_ci_red_streak`, `check_time_sources`, `load_last_queries` and `scan_time_slots`;
`resolve_remote` names which remote and branch, and none reads when a fetch happened. The branch's
`tools/memory-recall/query.py#resolve_worktree_reflog` finds a worktree's HEAD reflog file, not a fetch
time. So no existing seam fits beyond the engine's own reader, and the reading is git's own artefacts as
§4 lists them.

Recall terms used: stale-remote remote-tracking reflog FETCH_HEAD fetch clone fresh bound position engine worktree
