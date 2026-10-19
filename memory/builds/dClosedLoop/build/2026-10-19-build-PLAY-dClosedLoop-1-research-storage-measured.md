# Research: storage and coordination, today and the design measured

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 130's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-11-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

I measured today's storage, the designed index and the designed coordination, all against the real tree; nothing in the repository was written. The short answer: markdown as the store of record holds at scale. The designed index shape (one JSON file per tree, fully rebuilt whenever the tree changes) does not hold at 10x. The coordination's transport is fast, but its read points make it minutes-to-hours late, and one mailbox ref per build causes push retries once several writers share it.

**Pin and bounds.** Every probe ran on one node (Windows 11, git 2.54.0, Python 3.14.5) against a `--no-hardlinks` clone pinned at `e1a54ac67`, under the session scratchpad, with its remote removed. The scratch directory is deleted. Remote probes were `git ls-remote` and fetches into a scratch bare repo only; nothing was pushed. While I worked, another agent moved the worktree's HEAD to `0657a86` and staged edits to `memory-plan.md`, `systems.md` and others. My record citations are pinned to `e1a54ac67` with `git grep`.

## 1. Today, measured

**Table 1: tracked files by kind at HEAD.** Command: `git ls-tree -r -l <ref>`, bucketed by path prefix (scratch `census.py`).

| Kind | at e1a54ac67: files / bytes | at 60bd6a4 (2026-09-18): files / bytes |
|---|---|---|
| trail: `spec/` | 1,322 / 27,288,488 | 648 / 13,054,656 |
| trail: `reviews/` | 559 / 19,258,178 | 374 / 11,049,072 |
| trail: `build/` (.md) | 1,151 / 15,172,306 | 375 / 4,028,094 |
| trail: `build/` instruments (other files) | 94 / 1,508,995 | 15 / 101,214 |
| trail: `prompts/` | 609 / 2,969,134 | 154 / 573,364 |
| trail: RUN*.md | 98 / 1,434,630 | 61 / 512,518 |
| trail: build README | 167 / 1,376,480 | 117 / 912,889 |
| trail: BACKLOG.md | 126 / 878,298 | absent |
| library: `map/`, `gotchas/`, DECISIONS | 39 / 981,881 · 149 / 501,519 · 1 / 55,083 | 30 / 395,071 · 71 / 232,933 · 1 / 41,656 |
| instruction: guides, HYGIENE, TEMPLATE-SPEC | 12 / 406,322 | 9 / 218,303 |
| instruction: charter files, `.claude/`, role definitions, `.governance/` | 3 / 30,438 · 19 / 100,626 · 10 / 19,586 · 1 / 5,496 | — |
| registries: TOML / JSON outside memory | 35 / 271,419 · 21 / 294,174 | 28 / 182,710 · 14 / 225,071 |
| views: archive, project, backlog, ledger, LIVE | 18 · 20 · 4 · 4 · 1 | — |
| **`memory/` total** | **4,375 / 72,680,673** (4,257 .md, 70.4 MB) | **1,893 / 31,975,704** |

**Growth.** Command: the same over `git rev-list -1 --before=<date> HEAD`, and `git log --format=%cd --date=format:%Y-%m | uniq -c`.
- `memory/` went from 439 files (7.0 MB) on 2026-08-19 to 1,893 (32.0 MB) on 09-18 and 4,375 (72.7 MB) now: +2,482 files and +40.7 MB in the last 30 days.
- Commits per month: 1,670 (Aug), 2,124 (Sep), 2,229 (Oct, through the 19th).
- dClosedLoop alone is 263 files and 11.0 MB.
- `main`'s `memory/` is 4,486 files and 71.7 MB, so this growth is not this branch's alone.

**Table 2: how each tool reads.** Run in the scratch clone, wall clock, repeated.

| Command | Result |
|---|---|
| `python tools/memory-tree/gen_build_index.py --check` | 3.79–4.39 s (6 runs); reads every file each run, no cache |
| `python tools/memory-tree/gen_build_index.py --asks --path tools/memory-tree` | 2.84 s |
| `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` | 0.21 s; over `ebce889c7..HEAD` 0.68 s; `--for-paths` 0.11 s |
| `python tools/memory-recall/query.py "<q>" --terms "<10 terms>"` | cold `--rebuild` 4.61–6.28 s (one outlier of 13.83 s after a mass checkout); warm 0.61–0.68 s |
| the same, after a one-line edit to `memory/LIVE.md` | 6.96 s: `rebuilt 6.28s, cause corpus digest`, a full rebuild |
| recall cache on disk | `chunks.db` 173,494,272 B + `records.db` 3,960,832 B; 2,816 records and 140,863 chunks |
| the real git dir: `du -sh .git/recall` (read-only) | 478 MB, three per-worktree caches (manifests: 4,121–4,346 files, built in 4.54–5.81 s) |
| `python -B .../2026-10-17-build-PLAY-dClosedLoop-1-map.py --check` | 0.83–0.88 s; 2,442 nodes, 31,267 B of 32,768 |
| bar leg `memory hygiene` (from `.git/gate-ledger.tsv`; I ran no gate) | 83.275 s on 2026-10-09, when `memory/` was 3,304 files and 54.4 MB |

The recall query already runs on SQLite FTS5 from the standard library (`tools/memory-recall/query.py:20-23`). Its freshness check is an mtime and size digest over the whole corpus (`query.py:280-288`, checked at `:737`). Its cache is per worktree (`query.py:291-298`). Any edit forces a full rebuild (`query.py:744`).

**Table 3: where relations live today.** Commands: `git grep -l '^\*\*Serves:\*\*' -- memory`, `git log --format='%(trailers:key=…)'`, and a regex prototype (below).

| Carrier | Count |
|---|---|
| `**Serves:**` lines | 2,330 files (2,337 lines) |
| headings in `memory/` and the other .md | 46,093, of which `[tag]`-headed 837 (1.8%), in 61 files |
| `**Edges:**` lines | 0 |
| `<record> [tag]` citations | 3,584 |
| `path:line` citations | 14,623 |
| FAMILY-id mentions, untyped | 127,781 |
| markdown links to .md | 8,035 |
| commits / `Pass:` / `Decided:` | 6,101 / 1,353 / 677 |
| `gov:handoff` marker | 74 of 609 prompt files |
| DECISIONS rows | 200 bullets |
| remote `refs/gov/*` (`git ls-remote origin`) | 17 `refs/gov/runs`, nothing else |

These counts agree with memory-plan `[pockets]`: 6,084 commits, 1,353 and 677 trailers, 17 claims, and 59 of 595 markers, all since grown.

## 2. The design, projected

**Prototype (scratch `proto.py`).**
- What it reads: `git ls-tree` plus `git cat-file --batch` over 4,350 .md blobs, and `git log` trailers.
- What it emits: the designed shape, i.e. nodes (file, section, commit) and typed edges (serves, cites, decides) with a derived inverse. One JSON file, written atomically as systems `[cross]` says (`systems.md:185-188`).
- At 1x: 56,544 nodes, 151,194 edges, 38,940,832 B. Full build 2.9 s (ls-tree 0.04, cat-file 0.52, parse 1.6, git log 0.12, inverse plus write 0.66). `json.load` 0.135 s, peak working set 173 MB. Inverse lookup 0.003 ms.

**Scale probe (scratch `scale.py`).** It replicates the 1x rows k times under renamed paths and measures both stores.

| | 1x (measured) | 10x (measured) | 100x (extrapolated) |
|---|---|---|---|
| JSON bytes | 38.9 MB | 403.6 MB | ~4 GB |
| JSON derive inverse plus write | 0.72 s | 7.39–7.55 s | ~75 s |
| JSON load / peak memory | 0.14 s / 173 MB | 1.64 s / 1,634 MB | ~16 s / ~16 GB |
| JSON full rebuild on a tree miss | 2.9 s | ~30 s | ~5 min |
| SQLite bytes (four indexes) | 80.8 MB | 839.8 MB | ~8.4 GB |
| SQLite full build | 0.82 s | 8.73 s | ~90 s |
| SQLite one-file update (delete plus reinsert its rows) | 6.8 ms | 9.0 ms | ~10 ms, since the indexes are B-trees |
| SQLite open plus inverse query | 0.82 ms | 1.15 ms | ~1–2 ms |
| recall FTS cache, per worktree | 177 MB, ~5–6 s per rebuild | ~1.7 GB, ~50–60 s | ~17 GB, ~10 min |
| `gen_build_index --check` | 3.8–4.4 s | ~40 s | ~7 min |
| `memory hygiene` leg (~1.53 s/MB) | ~111 s at 72.7 MB | ~18 min | ~3 h |

**Basis of the extrapolation.**
- The 10x rows are real measurements of replicated data. 10x parse time (16 s) is linear by construction (the same regexes over 10x the bytes).
- The 100x figures scale 1x→10x linearly: the measured ratios were 10.3–10.6 for write, load and build, and 9.4 for memory.
- The tool timings assume cost proportional to bytes read. They are not verified: today's tools refused older trees (`gen_build_index` exited 1 on the 2026-08 and 09 trees), so I have no clean second point.
- Adds 127,781 id-mention `cites` edges (85% of edges), as P33's derived `cites` implies. A sections-only index was 4.5 MB in `research-memory-structure-b.md` §4.

**When 10x arrives.** At last month's linear rate (+2,482 files a month), gov itself reaches 43,750 files in about 16 months. At last month's ratio (2.3x a month), it is about 3 months.

## 3. Coordination, measured

| Probe | Result |
|---|---|
| `git ls-remote origin` ×5 | 0.572–0.76 s |
| `git ls-remote origin 'refs/gov/*'` | 0.586 s |
| `git fetch --no-tags --no-write-fetch-head <url> '+refs/gov/runs/*:…'` into a scratch bare repo | cold 0.889 s; warm, with `--prune`, 0.616–0.641 s (17 refs) |
| push to GitHub (a CAS write) | **not measured** (no remote writes allowed). `pushes.log` times the pre-push hook only: `skip-nondefault` median 0.4 s over 110 runs |
| CAS contention on one ref (scratch bare repo, file://, `--force-with-lease` append loop, `cas.sh`) | 1 writer: 10 attempts for 10 messages. 4 writers: 100 for 40. 8 writers: 359 for 80. No message lost. |
| the same with one ref per sender | 8 writers: 80 attempts for 80 messages |
| pass cadence (gap between `Pass:` commits within one build, `git log --all`) | n=1,328; median 7.5 min, p90 54.2 min |
| dClosedLoop commit gap | median 10.9 min, p90 53.1 min, max 656 min |
| tool-call cadence (gaps between `tool_use` turns in the 40 latest gov transcripts, read-only) | n=29,641; median 10.5 s, p90 72.4 s |

**What a write costs as designed.**
- A message is one `fetch` (about 0.6 s) plus one CAS push (unmeasured; at least one more round trip). A lease or claim is the same.
- Each write puts one ref and one commit on the remote, and under contention every lost attempt repeats both.
- The network widens the race window, so contention on the real remote should be at least what file:// showed.
- No write leaves a git dir while the lander holds it (`unattended.sh:2413-2416`). The lander's full-bar push ran a median 334 s, max 630 s (12 runs in `pushes.log`).

**What is real-time.** Only the harness's live inbox: Claude only, per memory-plan `[sessions]`, unverified by me. Everything else is polled. A node learns of another's message, decision or landing only when it reads, and the design reads at transitions and passes (`coordination.md:106`, `:137`). So time-to-learn is at least the pass gap (median 7.5 min, p90 54 min), and longer when only transitions read. A dead holder is noticed after 5,400 s today (`.unattended.conf:95`) and after 24 h by the designed default (v2 `[policies]`, `architecture-v2.md:948`). The 0.6 s transport is about 0.1% of the median learn delay.

## 4. Where it breaks

1. **Recall cache.** It is per worktree and fully rebuilt on any edit (`query.py:280-298`, `:737-744`). It is 177 MB and about 6 s at 1x, and already 478 MB in the real git dir. At 10x: about 1.7 GB per worktree and about a minute after every edit.
2. **The designed per-tree JSON index.** It is keyed by tree id and "rebuilt on a miss" (`systems.md:257`), so every commit is a full rebuild: about 30 s at 10x and about 5 min at 100x. At gov's roughly 117 commits a day that is about an hour of CPU per node per day at 10x. Loading it whole needs about 1.6 GB at 10x and about 16 GB at 100x.
3. **Record disagreement: "never loaded whole".**
   - The two research forms were JSONL and TSV, which can be read line by line (`systems.md:164`). The audit's L3 changed them to one JSON file.
   - A single JSON file cannot be read in part without a streaming parser, so "never loaded whole" holds only if it means the agent's context, not the process.
   - The source is ambiguous about which it means.
4. **Linear readers in the bar.** `memory hygiene` (83 s at 54 MB) and `gen_build_index --check` (about 4 s) re-read the whole tree on every run, about 18 min and about 40 s at 10x.
5. **Committed generated views.** `memory/LIVE.md` took 331 commits in 30 days; 167 commit subjects in 30 days name reconcile or conflict.
6. **One mailbox ref per build** (`coordination.md:99`). CAS retries rise 4.5x at 8 writers, and each retry is a network round trip.
7. **Read points, not transport, set latency.** Minutes to an hour for news, 24 h for a dead lease.
8. **Lander lock.** No claim, lease or mail write leaves a git dir while it lands (5.5 min median).
9. **Lease history.** Today's claim is a parentless commit (`unattended.sh:2077-2079`, pushed at `:2423`), so the remote keeps only the latest. The design's "its history is the witness" (coordination `[design]` item 1) needs a parent chain the record does not spell out.
10. **Record overstates a measurement.** `research-orientation-preserve.md:103` calls the ref "a 0.56 s compare-and-swap", but `:60` measured `ls-remote`, a read. Write latency is unmeasured there and here.
11. **Positional citations.** The 14,623 `path:line` citations go stale on edit, and 98% of headings are untagged, so the index's edges are mostly derived `cites`, not typed facts.

## 5. Candidates

| Candidate | Mechanism | Smallest losing test | Result |
|---|---|---|---|
| **K1. Markdown plus one derived JSON per tree** (as designed) | Records stay in git. Extractors write `<git-common-dir>/gov/index/<tree>.json` in full on each tree miss. | Loses if, at 10x, `gov tag refs` after a one-file commit takes over 2 s or needs over 1 GB. | **Loses at 10x**: about 30 s rebuild, 1.6 GB load. Holds at 1x (2.9 s, 173 MB). Its markdown half survives; its file shape loses. |
| **K2. Markdown plus a derived SQLite cache, per node, updated per blob** | Records stay in git. Rows are keyed by blob, so a tree is a set of blobs: only changed blobs are re-parsed and N worktrees share one file. Stdlib `sqlite3`, the engine memory-recall already uses (`query.py:20-23`). | Loses if a one-file update plus an inverse query takes over 100 ms at 10x, or it needs a new dependency. | **Survives**: 9.0 ms update and 1.15 ms query at 10x; no new dependency. Costs 2x JSON on disk. Untested: that deleting it and rebuilding gives identical results, which the build must run. |
| **K3. A committed database file** | The index or records live in a tracked .db. | Loses if two branches each change one record and the merge conflicts. | **Loses**: `Automatic merge failed` (merge rc=1). LIVE.md's 331 commits in 30 days show how often that would hit. Growth after `gc --aggressive` was only 12.9 KB per change, so size is not why it loses. |
| **K4. A cloud relational database as the store of record** | A hosted Postgres or similar is the truth; nodes query it over the network. | Loses if the memory readers and verdict must run with no remote (P3, `leases.offline`). | **Loses**: in a clone with no remote, `gen_build_index`, `gotchas`, recall and the design map all exited 0. A cloud store fails this by construction, takes P2's witness out of committed history, and trips M3 veto 2 (a new external dependency). |
| **K5. A sync service** (pub-sub push, or replicated SQLite) | A daemon or service pushes changes to nodes. | Loses if the time to learn is set by when the consumer reads, not by transport. | **Loses**: transport is 0.6 s; learning takes 7.5 min median at pass reads. The only gain, reading at tool-call cadence (10.5 s median), is available by surfacing a background-fetched local copy of the existing refs at a hook. It also fails offline and trips veto 2. |
| **K1/K2 coordination sub-fork: one ref per build vs one ref per sender** | `refs/gov/mail/<slug>` appended by CAS, vs `refs/gov/mail/<slug>/<sender>` | Loses if 8 concurrent writers need over 1.5x the ideal attempts. | One ref per build **loses** (4.5x). One ref per sender **survives** (1.0x). |

## 6. Pick, and what it leaves open

**Pick: K2.**
- Markdown and TOML stay the records of record in git.
- The designed index becomes a derived SQLite file per node in the git common dir: rows keyed by blob, the tree id only its freshness key, JSON only as the output format of `gov tag`.
- memory-recall's FTS5 tables move into the same file. Today's whole-corpus mtime digest is replaced by the per-blob key, which removes breaking point 1. That reuses the seam `query.py` already has.

For coordination, keep git refs, but use one ref per sender, and add a read point at the tool-call hook. That read is served from a local copy a background fetch keeps fresh, so it costs no round trip on the hot path. The per-sender refs passed the contention test; the hook read is untested. Its losing test for the build: a message posted on node A must show on node B's next tool call within 2x the fetch interval, with no network call inside the hook.

**Left open:**
- **Hook-read test.** The background-fetch, tool-call-hook read above is untested.
- **Push latency.** CAS write latency on the real remote is unmeasured; the build must time one on a scratch remote of the same host.
- **Rebuild equality.** That K2's rebuild gives identical results is untested.
- **Index for the bar.** Whether the linear bar legs (`memory hygiene`, `gen_build_index`) read the index instead of the tree.
- **Lease history.** Lease refs need a parent chain if history is to be the witness.
- **Dead-lease detection.** 24 h is a policy default the owner may want lower.
- **The lander lock** (`unattended.sh:2413-2416`). It needs a write path that does not share the lander's git-dir lock.
- **The 100x figures** are linear extrapolation from 1x and 10x, not measured.

Files read for this: the two records the question names (`architecture-v2.md` and `2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`) plus `coordination.md`, `systems.md`, `research-memory-structure-b.md` and `research-orientation-preserve.md`, all under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`. Code: `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-recall\query.py`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\unattended\unattended.sh` and `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.unattended.conf`. Read-only from the git dir: `C:\projects\coding-governance\.git\gate-ledger.tsv` and `C:\projects\coding-governance\.git\runlog\pushes.log`.
