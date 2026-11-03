# TOOL-dFairHearing-25 — the replay verdicts: replay 1 misses its bar in both runs, so DESIGN_RECORD_PRESET keeps `unit-spec` and R-1 is reopened

**Serves:** research TOOL-dFairHearing-25 TOOL-dFairHearing-1 TOOL-dFairHearing-15

This is spec S6's record, written by pass (c), the unit's last pass. Replay 1 is judged here against
spec 1's bar, from the raw outputs named below. Unit 15's replay is not run by this unit. Spec §3's
hands-off edge gives it to `TOOL-dFairHearing-30`, whose S1 to S5 and AC1 to AC4 supersede this unit's
S4, AC4, the unit-15 half of S5, AC6, and the unit-15 lines of S6 and AC7, the `ungated` arm's class
set among them.

## The verdict

| Replay | Switch | Run 1, attempt `fhr1c` | Run 2, attempt `fhr2b` | Bar, in each run | Verdict | Switch state |
|---|---|---|---|---|---|---|
| 1, the design-audit preset blind | `DESIGN_RECORD_PRESET` in `tools/workflows/review_pin.py` | reviewed 26/59 · escaped 1/6 · high 5/8 | reviewed 26/59 · escaped 0/6 · high 6/8 | reviewed 45/59 · escaped 4/6 · high 7/8 | MISS: both runs miss all three figures | `unit-spec`, unchanged |
| unit 15's with and without | `--all-ungated` in `tools/memory-tree/gotchas.py` | — | — | — | superseded: `TOOL-dFairHearing-30` runs it | no product file of spec 15 S6 changes here |

The miss keeps the default and files spec 1 S9's ask: `TOOL-dFairHearing-42` in this build's
`BACKLOG.md` reopens R-1 with both runs' counts. `DESIGN_RECORD_PRESET` reads `unit-spec` at
`tools/workflows/review_pin.py:47`, and the template's `preset` default literal reads `'unit-spec'` at
`tools/workflows/tier2-review.template.js:330`. Neither changes in this commit. `tools/workflows/README.md`
names `DESIGN_RECORD_PRESET` as the value's one source and states no value (pass (b), §8 F4), so it
needs no edit after this verdict. `grep -c -- "--all-ungated" tools/memory-tree/gotchas.py` prints 0.

## The binding (S7)

- **The orchestrating commit:** `8ee00000a4316a999d4ec270887261ddc22bd651`, read by the main loop at call time, before the first call, by `git rev-parse --verify HEAD`, exit 0, at 2026-11-03T21:42:22Z
- **The blobs the runs read**, by `git hash-object` at that moment. Each equals the orchestrating
  commit's blob at its path, and this commit changes none of the three:
  - `tools/workflows/README.md` `8a2c8db0eb3d459f968727422a4d461e7381d544`
  - `tools/workflows/tier2-review.js` `357e2fadb4f42a0ccd0ab9e8bd7de702d8002264`
  - `tools/workflows/replay_scorer.py` `36043efc12277942301ebe1dd93403c1f4eb20e5`
- **Unit 23's build commit:** `7ff570cfac96a18cdb3ed5c3da33e6a5801ea22a`, subject `TOOL-dFairHearing-23`.
  `git merge-base --is-ancestor` exits 0 for it, and for unit 27's `e3bd1ad45`, against the
  orchestrating commit.
- **Each clone's `HEAD`**, the placement commit the recipe made for it:
  - `fhr1b` HEAD `d38dbeca34baa1fc37bce372c3d4ccbb2b1aef11`
  - `fhr1c` HEAD `9cdc6ba57a4ea411c030af7927c7f40935250834`
  - `fhr2b` HEAD `efa97aa342d2e9829aded9a6b1cad13c1e1ef555`

Every call ran from the orchestrating commit. Nothing was committed between pass (b)'s return
(`8ee00000a`) and this commit, `fhr1c`'s call included.

AC1 was re-read by this pass on 2026-11-04 over all three clones. In each one:

- `rev-list --all` holds one commit outside `git rev-list 6cfd21619`, its `HEAD`;
- `diff --name-only 6cfd21619 HEAD` prints the two placed paths;
- the placed subject reads blob `767187aa4073f6e64cb2b2ef6b798f0a538347fd`;
- `status --porcelain` shows only the report the run wrote.

`git for-each-ref refs/replay/` in this repository prints nothing. Pass (b) observed the second recipe
run into an existing `fhr1b` exit 2 before any fetch.

## Attempts (S10)

| Run | Attempt | Clone | Workflow run | Status | Cause |
|---|---|---|---|---|---|
| 1 | b | `%TEMP%/fhr1b` | `wf_3f1a7ce7-98b` | void | its synthesizer ran Grep on this worktree's `memory/guides/REVIEW-PROTOCOL.md`, an absolute path outside the clone and the scratchpad |
| 1 | c | `%TEMP%/fhr1c` | `wf_f86461ae-6a2` | scored | — |
| 2 | b | `%TEMP%/fhr2b` | `wf_f93d43b8-dd5` | scored | — |

Run 1 took its second and last attempt. Run 2 took one. No third attempt was made, and no clone serves
two attempts.

These two clones are not attempts: `fhr1a` (HEAD `1800b889883ec799d5359e21cf24e9b6f67f606b`) and `fhr2a`
(HEAD `857b513fd253751ba3a22fcd9aacd951b18da717`). They are pass (a)'s clones of rev-5's placement.
No agent read them, because the opt-in pack refused both calls before any agent ran: their one subject
named `builds/dClosedLoop/`, outside `reviewDir`'s build. All five clones stay on disk under `%TEMP%`.

## The void rule, applied

Spec 1 §4 "The isolation" gives three parts, which this spec's S3 reads in unit 23 S4's terms.
They were applied to each attempt.

1. **Parsed.** Each report's appendix is read by `parse_candidates`. `replay_scorer.py --experiment`
   prints `parsed design-audit: 2 of 2` over `fhr1c` and `fhr2b`. `fhr1b`'s report was parsed as well.
2. **Run integrity.** Each of the three reports says that 5 of 5 lenses and 5 of 5 skeptic batches
   returned, with 0 DIED. Each Workflow result reads `exit` `complete`, `lensesDead` 0 and
   `skepticsDead` 0.
3. **Transcripts.** Two probes in the session scratchpad ran over every agent transcript of each run,
   12 agents per run:
   - `transcript_probe.py` lists every absolute path a tool call's input names outside the clone and
     the session scratchpad. It folds Windows, MSYS and `DAILY-~1` spellings together.
   - `transcript_cwd_probe.py` lists the calls that would read through the agent's working directory,
     which is this worktree. These are Read, Grep and Glob calls with no path or a relative one, and
     Bash commands that name no clone.

   What each attempt's probes flagged:
   - **`fhr1b`:** 139 tool calls, 11 flagged paths. The synthesizer (`agent-a8276897831644664`) ran Grep
     on `C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c/memory/guides/REVIEW-PROTOCOL.md`
     with the pattern `CLEAN WITH FIXES|BLOCKED`, which matched nothing. That is a read outside both
     roots, so the attempt is **void**, matched or not. The other flags read nothing outside:
     - a skeptic `cd`'d into this worktree only to time `node -e 0`;
     - one Read hit the session's `tool-results/` file (see below);
     - the rest are drive-letter-shaped fragments of written text.

     No cwd-relative call.
   - **`fhr1c`:** 128 tool calls, 1 flagged path. It is `s:/` inside a grep pattern, in a Bash call
     that `cd`s into the clone. No cwd-relative call. **Clean.**
   - **`fhr2b`:** 152 tool calls, 14 flagged paths. These are:
     - drive-letter-shaped strings that name no file read: `/c/repo`, `/c/x.json` and `a:/b` as argv
       of a `python -I -c 'print(sys.argv[1:])'` probe of MSYS path conversion, one `e:/` fragment in a
       Bash command, and strings of the same kind in the finding text the run wrote;
     - four Reads of the session's `tool-results/` files.

     Its 2 cwd-relative calls are that argv probe, which reads no file. **Clean.**

   The `tool-results/` reads are admitted, as a departure below. Each such file is the harness's
   persisted copy of that same agent's own earlier tool result, too large to return inline, under the
   session's own directory. Their contents are the clone's runtime record or a listing of the clone's
   dClosedLoop `build/` folder.

## Scoring (S3)

Each scored run was run from this repository's root through
`python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate <report> --matched <list>`.
Both exited 0 and refused no pair:

- `fhr1c`: 359 address matches; 39 pairs over 27 tags; `reviewed 26/59`, `escaped 1/6`, `high 5/8`.
- `fhr2b`: 367 address matches; 37 pairs over 26 tags; `reviewed 26/59`, `escaped 0/6`, `high 6/8`.

The manifest is `2026-11-04-build-TOOL-dFairHearing-25-replay-1-manifest.json`, in unit 23 S4's terms. It
declares one arm, `design-audit`, with `dispatched` 2, and one `{case, report, matched}` entry per
scored run. The void attempt is no case, since a void run is never scored. Over it,
`python tools/workflows/replay_scorer.py --experiment memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-25-replay-1-manifest.json`
exited 0 and printed:

```text
arm design-audit: base
parsed design-audit: 2 of 2
labels rotated — recorded, not checked: no committed key
known-set design-audit run-1: reviewed 26/59 · escaped 1/6 · high 5/8
known-set design-audit run-2: reviewed 26/59 · escaped 0/6 · high 6/8
```

**The adjudication, judged by this pass.** The matched lists are the main loop's, as spec 1 §4
"Scoring" assigns them, and the scorer held every pair to a cited `[tag]`. This pass read the known
set's 8 high and 6 escaped rows against each list:

- **Highs.** Run 1 lacks `fixture-2-population`, `cycle-spawns` and `structured-output`. Run 2 lacks
  `cycle-spawns` and `structured-output`.
- **Escapes.** Run 1 matches `act-ceiling` alone, and run 2 matches none.

Run 1 pairs 36 of its 49 confirmed findings. If each of the other 13 were placed on a new defect, it
would reach 39/59, still short of 45. Its escapes would still need three more than it found. The
verdict needs both runs to hit, so it does not rest on how a disputed pair is judged.

## The opt-in pack (AC2)

Each scored report sits under its clone's `memory/builds/dFairHearing/reviews/`. Each opens
`**Serves:** spec-audit PLAY-dClosedLoop-1`, and its `Reviewed:` line names
`memory/builds/dFairHearing/replay/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@767187aa4073f6e64cb2b2ef6b798f0a538347fd`.

This pass replayed each call's payload on stdin through `node tools/workflows/spec-audit-optin.js` on
2026-11-04. The two payloads are `fhr2b`'s staged arguments, and `fhr1c`'s, which are `fhr1b`'s with
`repo` and `scratch` set to `fhr1c`:

- with the placed subject, each exited 0;
- with the subject at the record's dClosedLoop path, each exited 2, naming `subjects`.

## Raw outputs

- **The reports, as the clones hold them**, each pinned by `git hash-object`:
  - `fhr1c`, `C:/Users/DAILY-~1/AppData/Local/Temp/fhr1c/memory/builds/dFairHearing/reviews/2026-11-04-tier2-PLAY-dClosedLoop-1-layer-runtime.md`, blob `ec1c3fce45664b3d2a4bacc9f9d51ee592786ea8`.
  - `fhr2b`, `C:/Users/DAILY-~1/AppData/Local/Temp/fhr2b/memory/builds/dFairHearing/reviews/2026-11-03-spec-audit-PLAY-dClosedLoop-1-layer-runtime.md`, blob `85c7ec7b3c1835e28567fdf6f3a55c10be65e921`.
  - `fhr1b`, void, `C:/Users/DAILY-~1/AppData/Local/Temp/fhr1b/memory/builds/dFairHearing/reviews/2026-11-03-review-dClosedLoop-layer-runtime-spec-audit.md`, blob `77f5f6badd251a4ef95b0a6ee94e5e3b28f89a8f`.
- **The Workflow results**, in the session's `tasks/` folder: `wou0ruwji.output` (`fhr1b`),
  `wcikav9sa.output` (`fhr1c`) and `waolxmjdh.output` (`fhr2b`). The agent transcripts are under the
  session's `subagents/workflows/<run>/`, one folder per Workflow run named above.
- **The matched lists**, committed beside this record:
  - `2026-11-04-build-TOOL-dFairHearing-25-matched-fhr1c.md`
  - `2026-11-04-build-TOOL-dFairHearing-25-matched-fhr2b.md`
  - `2026-11-04-build-TOOL-dFairHearing-25-matched-fhr1b.md`, the void attempt's list, kept as its
    record and scored by nothing.

## Departures

1. **The main loop changed run B's report sentence.** In every run's staged context, run B's
   sentence naming a dClosedLoop report path was replaced by
   `Write the report under memory/builds/dFairHearing/reviews/, the reviewDir this call names.`
   The old sentence contradicted S2's placement and `reviewDir`.
2. **The main loop left pass (c)'s brief untracked.** This pass was dispatched on the tracked build
   brief, `2026-11-02-prompt-TOOL-dFairHearing-25-build-brief`, with the pass (c) brief and its addendum
   left in the session scratchpad. `--brief` refuses an untracked brief. Committing one before this
   commit would make it, and not the orchestrating commit, this record's first parent, which breaks
   S7.
3. **The main loop made `fhr1c` after a first pass (c) found `fhr1b` void.** That dispatch,
   `wf_5a0e8e88-fa3`, committed nothing. The main loop then made `fhr1c` with pass (b)'s
   `fhr-clone-b.sh` from the committed procedure, and the placement commit is `9cdc6ba57`. It called it
   with `fhr1b`'s arguments, `repo` and `scratch` set to `fhr1c`, and its checklist is byte-identical to
   `fhr1b`'s and `fhr2b`'s.
4. **This pass admits the `tool-results/` reads.** The void rule names the clone and the scratchpad
   alone. This pass admits a Read of the session's `tool-results/` file because it returns that same
   agent's earlier output of a clone read, so it brings in nothing from outside the clone.
5. **The reports stay in the clones.** This pass did not copy them into the tree. The manifest names
   them by absolute path and this record pins each by blob, so `--experiment` reproduces on this node
   while the clones stand under `%TEMP%`.
