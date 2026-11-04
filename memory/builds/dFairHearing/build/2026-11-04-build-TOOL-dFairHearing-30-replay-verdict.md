# TOOL-dFairHearing-30 — unit 15's replay in nine clones: every record and arm has a completed attempt that is not void, after f2s1's unparsed report was re-run as f2s2

**Serves:** research TOOL-dFairHearing-30 TOOL-dFairHearing-15

This is spec S5's record, written by pass (b), the unit's last pass. It holds the runs of unit 15's
replay (spec 15 S5, its §4 corpus, arms `selected` and `ungated`): each attempt's clone, `HEAD`, status,
outcome, void cause and report, beside the orchestrating commit and the blobs the runs read. Scoring,
the pooled figures, the decision and the `ungated` class set are `TOOL-dFairHearing-35`'s (spec §3,
hands-off). Its S5 adds a `## Scoring` section here and adds itself to the `**Serves:**` line.

## The orchestrating commit (S8)

`run.log`, which the per-arm block appended to before each harness call, holds nine lines. Each names
one sha:

```text
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f1s1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f1u1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f2s1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f2u1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f3s1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f3u1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f4s1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f4u1
orchestrating 3cf918a65d76286ad35b699b510ed03d048087b0 clone C:/Users/DAILY-~1/AppData/Local/Temp/f2s2
```

The orchestrating commit:

`3cf918a65d76286ad35b699b510ed03d048087b0`

It is this record's commit's first parent. Nothing was committed between the first call and this
commit, f2s2's call included.

**The blobs the runs read**, each by `git hash-object` before the first call, and each equal to the
orchestrating commit's blob at its path. This commit changes none of the three:

- `tools/workflows/README.md` `4d819f03360b559f5956e60b747b9140afadcb42`
- `tools/workflows/tier2-review.js` `357e2fadb4f42a0ccd0ab9e8bd7de702d8002264`
- `tools/workflows/replay_scorer.py` `36043efc12277942301ebe1dd93403c1f4eb20e5`

**Unit 23's build commit:** `7ff570cfac96a18cdb3ed5c3da33e6a5801ea22a`. `git merge-base --is-ancestor`
exits 0 for it against the orchestrating commit.

## The four records

| # | Record (spec 15 §4) | Range |
|---|---|---|
| 1 | `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md` | `271aa59de..6f5f4ddec` |
| 2 | `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md` | `a60b0c7dc..033b15f24` |
| 3 | `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md` | `05357638b..0a6eff73e` |
| 4 | `memory/builds/dClosedLoop/reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-answers-b.md` | `f064bf378..f8ad789e1` |

## Attempts (S9)

| record | arm | attempt | clone | outcome | void |
|---|---|---|---|---|---|
| 1 | selected | 1 | f1s1 | completed | - |
| 1 | ungated | 1 | f1u1 | completed | - |
| 2 | selected | 1 | f2s1 | completed | not parsed: `parse_candidates` refuses the report, "liveness: 3 confirmed appendix row(s) against a stated confirmed count of 0" |
| 2 | selected | 2 | f2s2 | completed | - |
| 2 | ungated | 1 | f2u1 | completed | - |
| 3 | selected | 1 | f3s1 | completed | - |
| 3 | ungated | 1 | f3u1 | completed | - |
| 4 | selected | 1 | f4s1 | completed | - |
| 4 | ungated | 1 | f4u1 | completed | - |

No attempt was refused or `failed`, and no clone serves two attempts. f2s1 is void, so S9 re-ran its
record and arm in the next attempt's clone, f2s2. Under unit 35 S1's rule, f2s2 was that pair's
last eligible attempt. Which attempt is scored is unit 35's checker's to derive from this table.

## Each clone (S1, S2, AC1)

Every clone sits under `C:/Users/DAILY-~1/AppData/Local/Temp/` and was made by the replay section's
recipe (`f30-block.sh make`, composed from the committed README). Its status was read by the per-arm
block immediately before its call. That status was empty, which is the only case in which the block
prints `ready:`. After the run, `git -C <clone> status --porcelain --untracked-files=all` lists one
path, the arm's own report. The report blob is by `git hash-object`.

- `f1s1`, Workflow run `wf_326a16b0-574`, result `wk9sw9yal.output`
  - HEAD `6f5f4ddec49cd4789e8fe6883399c2040aeaf564`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-review-dTrueNorth-closing-diff-r1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f1s1/reviews/2026-11-04-review-dTrueNorth-closing-diff-r1.md`, blob `0d896612a2a975a0ea3706740037573957beee88`
- `f1u1`, Workflow run `wf_29780cc4-8db`, result `wek7vwe5s.output`
  - HEAD `6f5f4ddec49cd4789e8fe6883399c2040aeaf564`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-review-dTrueNorth-closing-diff-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f1u1/reviews/2026-11-04-review-dTrueNorth-closing-diff-round-1.md`, blob `b51c8214ae57d2a9b1904291476db72880e8d7b8`
- `f2s1`, Workflow run `wf_39e644b6-336`, result `wprke7qdt.output`
  - HEAD `033b15f240f740fdd3df219d94f8fc42bcaf7420`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f2s1/reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`, blob `decf0ad2a661dd7a3ee2e934cf410876f8aae436`
- `f2s2`, Workflow run `wf_45ddc1c4-99a`, result `w25dj4gg9.output`
  - HEAD `033b15f240f740fdd3df219d94f8fc42bcaf7420`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f2s2/reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`, blob `82f8e77eac64cbf9ef62cd413970918b5f2060a9`
- `f2u1`, Workflow run `wf_417eb157-41f`, result `w32zo1sga.output`
  - HEAD `033b15f240f740fdd3df219d94f8fc42bcaf7420`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f2u1/reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`, blob `a73b12cc40bee14cace653245b25392333c09361`
- `f3s1`, Workflow run `wf_1f55c805-df7`, result `wgn5v0qf4.output`
  - HEAD `0a6eff73e1a81f9841512dd9c5e7c4d8ab9229cb`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f3s1/reviews/2026-11-04-diff-review-dRenderedAnchor-round-1.md`, blob `7ff25de9fa2d128c36577e37b75cdf5853f48201`
- `f3u1`, Workflow run `wf_84e8cca4-c11`, result `wz9bxcghq.output`
  - HEAD `0a6eff73e1a81f9841512dd9c5e7c4d8ab9229cb`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f3u1/reviews/2026-11-04-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md`, blob `6ef086148c750303ee56a84d4c812973a0e7485a`
- `f4s1`, Workflow run `wf_ed0bb5dd-636`, result `wvhznwt9a.output`
  - HEAD `f8ad789e14c2c36b9b911bdd9551eef1d56d91a0`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-review-PLAY-dClosedLoop-1-closing-diff.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f4s1/reviews/2026-11-04-review-PLAY-dClosedLoop-1-closing-diff.md`, blob `5fdb5989eea620cd19a69e17f852d92bc96d1f4d`
- `f4u1`, Workflow run `wf_a607282a-905`, result `wqwtea28r.output`
  - HEAD `f8ad789e14c2c36b9b911bdd9551eef1d56d91a0`
  - status before the call: empty
  - status after: `?? reviews/2026-11-04-review-diff-dClosedLoop-round-1.md`
  - report `C:/Users/DAILY-~1/AppData/Local/Temp/f4u1/reviews/2026-11-04-review-diff-dClosedLoop-round-1.md`, blob `554d94065954868895a5f28e90a84d5fcad395ea`

Each HEAD equals its record's range head. The result files are in the session's `tasks/` folder,
`C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/tasks/`.
The agent transcripts are under
`C:/Users/daily-agent/.claude/projects/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/subagents/workflows/`,
one folder per Workflow run named above. The `<transcript file>:<line>` cites below are files in the
cited run's folder.

## The void rule, applied

Spec 1 §4 gives three parts, which unit 25 S3 reads in unit 23 S4's terms. Each was applied to every
attempt.

1. **Parsed.** `parse_candidates` in `tools/workflows/replay_scorer.py` read each report's appendix.
   It read rows from eight reports and refused f2s1's (see below).
2. **Run integrity.** Each Workflow result reads `exit` `complete`, `lensesRun` 5, `lensesDead` 0
   and `skepticsDead` 0. Each report's RUN INTEGRITY lines say every lens and every skeptic batch
   returned, with 0 died.
3. **Transcripts.** Unit 25's two probes ran over every agent transcript of each run.
   `transcript_probe.py` lists every absolute path a tool call's input names outside the clone and
   the session scratchpad. `transcript_cwd_probe.py` lists the calls that would read through the
   agent's working directory, this worktree. A third scratch probe, `f30-hits.py`, adds the
   `<transcript file>:<line>` of each flag. A fourth, `f30-prov.py`, checks whether each
   `tool-results/` file read was named by an earlier result in the same transcript.

| clone | rows parsed | agents | tool calls | flagged paths | cwd-relative calls | void |
|---|---|---|---|---|---|---|
| f1s1 | 12 | 13 | 259 | 8 | 1 | no |
| f1u1 | 13 | 11 | 258 | 9 | 0 | no |
| f2s1 | refused | 11 | 134 | 3 | 0 | yes, part 1 |
| f2s2 | 3 | 13 | 131 | 11 | 0 | no |
| f2u1 | 2 | 10 | 102 | 4 | 1 | no |
| f3s1 | 9 | 13 | 121 | 9 | 0 | no |
| f3u1 | 4 | 12 | 109 | 8 | 2 | no |
| f4s1 | 9 | 12 | 156 | 6 | 0 | no |
| f4u1 | 10 | 12 | 147 | 15 | 9 | no |

**Why f2s1 is void.** The report lists 3 confirmed appendix rows. `extract_stated_count` takes the
first number after the word "confirmed", and the synthesizer wrote "By raw confirmed finding the tally
is the same: 3 confirmed, 0 blocker". The pattern `confirmed\W{0,6}(\d+)` reads "confirmed, 0" as a
stated count of 0, so the liveness check refuses the report. f2s2's report parses: 3 rows, no refusal.

**What the transcript flags are.** No flag in any attempt is a read of content from outside the
clone. Each falls into one of these kinds:

- **Drive-letter-shaped fragments** inside code or finding text that name no file. Examples: `s:/n`
  from a Python `legs:\n`, `t:/n` from `as t:\n`, `e:/`, `c:/` inside StructuredOutput text, and in
  f2s2 the string `/etc/tier2-review.js`, a receipt-row path in a fixture testing the resolver's
  escape refusal (agent-a98db33906783c962.jsonl:74).
- **Session `tool-results/` reads.** Each is that same agent's own earlier persisted result: every one
  reads `own=True` under `f30-prov.py`. These are admitted as departure 3.
- **Scratchpad fixtures** each agent made for itself, which the rule admits. These cover every
  cwd-relative call: f1s1's `scratchpad/p12`, f2u1's `scratchpad/p.py`, f3u1's `scratchpad/p1` and
  `scratchpad/jp`, and f4u1's `scratchpad/d.diff`. The last was written by its own agent at
  agent-aeaf226f6f029b401.jsonl:29, before it was read. The other eight f4u1 cwd-relative calls read
  `Temp/claude/` files of the next kind.
- **Files outside both roots that the agent itself wrote before reading them**, from its own clone's
  git objects or from literal text. These are admitted as departure 2.

The agents also ran `rm -rf` on earlier units' scratch directories (`p12`, `rk`, `jp`, `p1`) before
rebuilding them. That is not a read, and it voids nothing.

## The manifest (unit 23 S4)

`2026-11-04-build-TOOL-dFairHearing-30-replay-manifest.json`, committed beside this record. It
declares `selected` as the base, with `checklist` `acquired`, and `ungated` varying `checklist` from
it, `dispatched` 4 each. It has one `{case, arm, report, matched}` entry per record and arm. Each
names the report of the pair's first completed attempt that is not void, so record 2 `selected` names
f2s2. `matched` is `null` throughout. Over it,
`python tools/workflows/replay_scorer.py --experiment memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-replay-manifest.json`
exited 0 and printed, before any figure:

```text
arm selected: base
arm ungated: varies checklist from selected
parsed selected: 4 of 4
parsed ungated: 4 of 4
labels rotated — recorded, not checked: no committed key
```

A copy naming f2s1's report in place of f2s2's prints `parsed selected: 3 of 4`.

The manifest grammar takes one `known`, and this one names record 1. The `recall` lines that follow
are therefore scored against record 1 for every case. For records 2 to 4 they are not those
records' recall, and this record reads none of them. Spec 15 S5 scores each run against its own
record, through `review_replay.py --known <record> --candidate <report>`, and that scoring is unit
35's (its S3).

## The `ungated` instrument (spec 15 §4)

`2026-11-04-build-TOOL-dFairHearing-30-ungated.py`, committed beside this record. It is the scratch
instrument that wrote the four `ungated` checklists, blob `954b641798fd8a1d6957a075f20adb04afb2e396`,
with two changes (departure 6). It runs the clone's own `--for-diff` over the range. It then
appends every other class record of the clone that this repository's `check_ungated` reads as
ungated, keeping the by-design block last. It is not one of S8's three blobs.

## The evidence kept (S10)

Every clone directory, report, Workflow result file and transcript this record names stays on disk
until `TOOL-dFairHearing-40`'s pass. This pass removed none of them. The reports stay in their
clones: the manifest names them by absolute path, and this record pins each by blob.

## Departures

1. **f2s1 was re-run as f2s2 after a first pass (b) dispatch stopped.** That dispatch
   (`wf_fa027457-7eb`) found f2s1 void and committed nothing. The main loop made f2s2 with
   `f30-block.sh make` from the committed per-arm block, `SCRATCH` and `ORCH` set. The clone was clean
   at `033b15f24` and `refs/replay/` was empty. `f30-block.sh call` printed `ready:` and appended
   `run.log`'s ninth line. Its arguments are f2s1's, with the clone name changed in `repo`, `scratch`
   and `context` and nothing else.
2. **This pass admits outside-root files the agent itself wrote before reading them.** The void rule
   names only the clone and the scratchpad. Each file below was written by the same agent, in the
   cited call or an earlier one, from its own clone's objects (`git show` or `git diff` at the
   record's range) or from literal text. So nothing from outside the clone enters.
   - f1s1: `C:/Users/DAILY-~1/AppData/Local/Temp/claude/s7.md`, written by `printf` and read in one
     call, agent-a24141d7921658b99.jsonl:39.
   - f1u1: `/tmp/cmh.sh`, written from `6f5f4ddec:tools/memory-tree/check-memory-hygiene.sh` and
     never read, and a `mktemp` file the same call wrote and read, agent-ae542147c98435f90.jsonl:68.
   - f2u1: a `mktemp -d` fixture under `C:/Users/DAILY-~1/AppData/Local/Temp`, made, read and removed
     in one call, agent-a47597332442b8d23.jsonl:75.
   - f3s1: `/tmp/au.sh`, written from `0a6eff73e:tools/unattended/adopt-unattended.sh` and read in
     one call, agent-a237dabe22d1b455d.jsonl:43.
   - f3u1: `/tmp/au.sh`, written from the same blob and read in the same call,
     agent-a513895ec04fdbda2.jsonl:44 and agent-ab231335de3c03e7f.jsonl:58. Also `/tmp/pp.sh`,
     written from `0a6eff73e:tools/workflows/check-protocol-parity.test.sh` and never read,
     agent-a026cbd0e8605f9e8.jsonl:36.
   - f4u1, all files under `C:/Users/DAILY-~1/AppData/Local/Temp/claude/`:
     - `wd.txt`, written from `git diff` of the clone's range at agent-a71d2ae0c827f985b.jsonl:29 and
       read at :34;
     - `np2.txt`, written at :67 and read at :71;
     - `npi.txt`, written at :96 and read at :100;
     - `npi_full.md`, written from `git show f8ad789e1:…night-pass-instruments.md` at :119 and read
       at :119 and :148;
     - `v2.md`, written from `git show f8ad789e1:…architecture-v2.md` at :76 and read at :81 to :91,
       :124 and :128;
     - `lr.md`, written and read at :133;
     - `v2.md` and `v2base.md`, written from the clone at agent-a5b9636585c1dd0ff.jsonl:51 and :61
       and read in those calls and at :56;
     - `/tmp/v2.md`, written and read at agent-a904a860eaf62874a.jsonl:44.

   Two of these paths had more than one writer. `/tmp/au.sh` was written by both record 3 arms, and
   `Temp/claude/v2.md` by two f4u1 agents. Each writer took the same blob at the same commit, so a
   write by the other between one agent's write and its read leaves the same bytes.
3. **This pass admits the session's `tool-results/` reads**, as unit 25's departure 4 did. Each is the
   harness's persisted copy of the reading agent's own earlier result. Across the nine runs,
   `f30-prov.py` finds 38 tool calls naming such a file, and every one is `own=True`. The lines
   `transcript_probe.py` flagged, by clone:
   - f1s1: agent-a85c6a8ce58443e3a.jsonl:29 and :43
   - f1u1: agent-ae542147c98435f90.jsonl:96 and agent-af3fc6650a2d047fd.jsonl:33
   - f2s1: agent-a78bece2242dd5efe.jsonl:30
   - f2s2: agent-acf8aabbdb23ca751.jsonl:32
   - f3s1: agent-a13f59a244747c221.jsonl:28, agent-a237dabe22d1b455d.jsonl:33,
     agent-a4e6397bf88477e25.jsonl:27 and agent-ae4712dcebbe2a45b.jsonl:27
   - f3u1: agent-a026cbd0e8605f9e8.jsonl:31, agent-a30926bf838e1b3c4.jsonl:27,
     agent-a5108f78030afc8c8.jsonl:27 and agent-ab231335de3c03e7f.jsonl:28
   - f4s1: agent-a1280eb9ee9845056.jsonl:33 and :51, agent-a9204fb513d38cb39.jsonl:33 and
     agent-af689e972da8ad528.jsonl:55
   - f4u1: agent-a71d2ae0c827f985b.jsonl:56
4. **The manifest's `known` is record 1** (see above). Each record's own known set is the scorer's
   input in unit 35's pass, not this manifest's.
5. **f4s1's report path is spelled long-form.** Its Workflow result names the report under
   `C:/Users/daily-agent/AppData/Local/Temp/f4s1/`. That is the same folder as the `DAILY-~1` path
   this record uses.
6. **The committed instrument differs from the one that ran in two ways.** A `# **Serves:**` line is
   put first, so the record binds. Its helper `tracked` is renamed `check_tracked`, at its definition
   and its one call, because the repository's naming lexicon admits no `tracked` verb. Behaviour is
   unchanged. Dropping the first line and reversing the rename gives back blob `954b6417`.
