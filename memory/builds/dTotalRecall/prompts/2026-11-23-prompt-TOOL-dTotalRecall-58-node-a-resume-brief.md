**Serves:** journal TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

# Brief — dTotalRecall: resume the unattended build run on node a

## The prompt

> I need this build to resume on node a, wrap it up here, push it, and give me a fully oriented handoff to resume it
> there.

— owner, 2026-11-23, on node d, during the dTotalRecall unattended run started there on 2026-11-22 with
`/unattended dTotalRecall`.

## The brief

### Goal

Continue the dTotalRecall unattended build run on node a from the HELD record node d left: build every remaining
DEFERRED roster unit from its spec in build order, then run the close and land it, with no owner turn.

### Where the run stands

- Branch `branch/unattended-dtotalrecall-ae256e`, pushed to `origin`. Run state `memory/builds/dTotalRecall/RUN.md`,
  phase `HELD`, hold code `host-owner-action`, release condition `owner`: the owner moved the run to node a. The
  hold released the slug's lease and node d reaped its idle-wake, so nothing on node d still fires into it.
- Built and CLOSED: 53 of the 91 roster units (DERIVED 2026-11-23, `bash tools/unattended/unattended.sh --plan
  dTotalRecall`), the last being TOOL-dTotalRecall-57. Every pass's pass legs ran; the only red left is the
  inherited check 21 on `memory/builds/dWitnessedBar/build/2026-11-22-build-TOOL-dWitnessedBar-1-replay.py`, owed at
  the close.
- Held unbuilt on owner asks, never to be dispatched by the run: TOOL-dTotalRecall-8 and -37 (ask
  TOOL-dTotalRecall-109), TOOL-dTotalRecall-14, -15 and -26 (ask TOOL-dTotalRecall-111). Ask TOOL-dTotalRecall-113
  carries unit 53's S36 (the build method's guide sits at its byte budget).
- Next: TOOL-dTotalRecall-58, order 30, spec rev-3, already re-grounded on 2026-11-23 and committed DEFERRED. It is
  the last of order 30 and has no build brief yet. Then orders 31 to 41, each unit re-grounded before its dispatch:
  31 is units 60 and 65; 32 is 66, 68 and 69; 33 is 70, 73 and 75; 34 is 74 and 87 (parallel); 35 is 76, 83 and 84;
  36 is 77, 78, 79, 80, 85, 86 and 90; 37 is 88, 91, 93, 94 and 95; 38 is 89, 96 and 97; 39 is 92; 40 is 98 and 99;
  41 is 100 (the README's generated build-order table is the source; read it, not this list, if they differ).

### Resume on node a

1. Fetch and open a worktree on the branch, under the node's worktree root, outside the primary tree.
2. In that worktree, run `/unattended dTotalRecall`. Its Resume path schedules a fresh idle-wake with `CronCreate`
   (every 10 minutes), then `bash tools/unattended/unattended.sh --status dTotalRecall` and
   `bash tools/unattended/unattended.sh --resume dTotalRecall --keepalive-id <the new id>`; condition `owner` is met
   on any resume.
3. Run `/session-kickoff` there and append the card from that worktree: the scratch-guard refuses a commit whose
   card names another tree. Before each dispatch, re-append a `## route` section naming the unit you build.
4. If `Agent` or `Workflow` is refused for missing agent limits, render them with
   `python tools/policy/policy.py settings --write .claude/settings.local.json` in the worktree.
5. Read `memory/guides/BUILD-METHOD.md` whole before the first pass.

### The per-unit loop, as node d ran it

1. Re-ground: write a brief under `prompts/` modeled on
   `2026-11-23-prompt-TOOL-dTotalRecall-55-reground-brief.md` (its items 1 to 6 are generic; items 7 and 8 name what
   the unit's built neighbours actually landed). Render it with `python tools/roles/handoff.py render --role
   gov-spec-writer --build dTotalRecall --unit <id> --input prompt=<brief> --input spec=<spec> --out
   <prompts/...-reground-spec-writer.md> --part task`, and spawn `gov-spec-writer` with the stdout as the prompt and
   the description the render prints on stderr (rule 6 of the agent-cap hook). Writers of one order run in
   parallel, each editing only its own spec. Commit the specs only after every writer of the batch has returned:
   the index render writes into spec files.
2. Build brief: copy the previous unit's `prompts/2026-11-23-prompt-<id>-build-brief.md`, update its "Built so far"
   paragraph and the unit's own notes, and name the acceptance ledger `build/<date>-build-<id>-1-acceptance-ledger.md`.
3. Flip the spec header `DEFERRED` to `INPROGRESS`, run `python tools/memory-tree/gen_build_index.py --write`, and
   commit the flip with the brief (`Pass: none`). Route the card. Then `unattended.sh --brief dTotalRecall --unit
   <id> --path <brief>` and `unattended.sh --dispatch dTotalRecall --pass <id> --writes <path> ...`: every path in
   the spec's Files touched, plus `tools/gate-legs.json`, `tools/govkit/registry.toml`, `.lexicon.conf`,
   `memory/map/generated/symbols.json`, `memory/guides/SESSION-KICKOFF.md`, the build's `BACKLOG.md`, the spec and the
   ledger. Add `memory/LIVE.md`, `memory/backlog/TOOL.md` and the build README only when `gen_build_index.py` is not
   itself in the write set (check 49 refuses an index beside its generator). A path list read from a Python file on
   Windows ends in CR; strip it, or check 49 refuses the whitespace.
4. Build: `Workflow` with `scriptPath` `tools/workflows/unattended-unit.js` and these args, `<REPO>` the node-a
   worktree and `<SCRATCH>` that session's scratchpad, both spelled absolute with forward slashes:

   ```json
   {"repo": "<REPO>", "slug": "dTotalRecall", "scratch": "<SCRATCH>", "mode": "unattended",
    "driver": "bash tools/unattended/unattended.sh",
    "ground": "You are one stage of a harnessed unattended build in the repository at <REPO>. Read `memory/guides/BUILD-METHOD.md` WHOLE before acting; it is the procedure you are bound by. No stage of this program runs the merge bar or a self-test suite, and neither does any agent it spawns: a role agent runs no gate beyond what its role allows, and a hook refuses the rest. A unit verifies with a fixture or a probe of its own code, and the bar and every new arm's RED-first observation run once at the main loop after the last unit is terminal. The build is `dTotalRecall` and its record is `memory/builds/dTotalRecall/`. Every temporary file, backup, probe or log this run makes goes under <SCRATCH>, spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp, a bare mktemp, or any OTHER path outside the repository. The ONE exception is a git clone or a fixture repository, which needs a SHORT path on Windows because that scratchpad path is long enough that a clone under it fails with Filename too long: it goes under %TEMP%/<short-name>, never inside the worktree and never at a drive root. Speak only in your return value: nobody reads a transcript under a mandate. No gate, suite or bar runs inside a unit pass: the merge bar runs ONCE, at the close, so a spec's section 7 lists what the close runs and declares each new arm on a `New arm:` line, and a pass verifies with a fixture or a probe of the code it changed. ",
    "checklist": "python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD",
    "passLegs": "bash tools/run-gates/pass-legs.sh",
    "roles": {"builder": "gov-builder"}, "efforts": {"builder": "high"},
    "unitId": "<id>", "specPath": "<spec path>", "briefPath": "<build brief path>"}
   ```

   Register it with `unattended.sh --register-task dTotalRecall --task build-<n> --heartbeat <its journal.jsonl>`
   and release it with `--release-task` when it returns.
5. Pass legs: `bash tools/run-gates/pass-legs.sh --base <dispatch sha>`. A unit's own red goes through the red-fix
   lane (a `Red-fix: <leg>` commit carrying the fix alone, its record from `build_records.py new red-fix` in the next
   commit); a record red (pinned facts, positional) is fixed in the record (`positional.py pin <file> --at <sha>`,
   a DERIVED or PINNED tag on the number's line).
6. Record the builder's return as `build/<date>-build-<id>-1-builder-return.md` (Serves and Caused-by head; the
   return's why and summary whole), commit it with the index render, and push the branch.
7. A divergence: record the return, write a fold brief, have a writer fold the spec as a rev bump, write a
   `-build-2-brief.md`, re-run `--brief` and `--dispatch` (with an explicit write set), then the Workflow again.

### Notes the remaining re-grounds need

- Unit 58 rev-3: the marker's bound lives in the build-folder walks through a new `id_grammar.py#check_marker_domain`,
  never in `read_kept_reason`; two `slug-grammar` markers outside the tool root stay honoured.
- Unit 60: its S7 to S9 re-check only (unit 45 rev-3 landed the keyword-only slug); S12 and AC12 replace unit 47's
  AC2; S17's site count is unit 44 rev-3's, with `derive_run_kind` listed apart; S21 and S25 are done by unit 48
  rev-3 (rewrite as re-observations); unit 48 left the runlog README head and its `RECORD_SCHEMA` cause key to it;
  S33 names `tools/lib/resolve-python.test.sh`, not `legacy_ledger.py`; its edge to unit 53 names S20's govkit
  lines, which now ride with unit 37.
- Unit 65: re-point `read_kept_rows`, the `table` argument and the `kept` argument when it moves the table into a
  project registry (units 55 and 57 as built).
- Unit 66: S8's section is `2o`; S34's temporary-directory concern is moot; AC5's grep finds unit 59's plant; S19
  assumes a path-testing reader, while unit 58 puts the bound in the walks; fixture plants other than
  `kept-row-drained` must pass their own `kept` or its S1 reds them; its legacy greps read
  `tools/govkit/registry.toml` and the ratchet's `new at` line.
- Unit 70: its S14 deviation record is still owed with a corrected cause; its §4 suffix claim is wrong; its
  legacy-ledger greps re-point as unit 66's do.
- Unit 92: unit 81 rev-4 F2 changed AC1's fourth input, so S1 and S2 record no departure; S3 holds.
- Unit 88: legacy tables live in `tools/govkit/registry.toml`, never a shipped `kit.toml`.
- Every re-ground: a §8 mark is exactly `RESOLVED (agent, YYYY-MM-DD, delegated)`; a new leg's ceiling clears its
  evidenced maximum by max(120 s, 1.0x) (PINNED 2026-11-22, deviation 15); `canonical_kind` is
  `tree_lib.py#resolve_kind`; a New arm at `id_grammar.py` has no suite to live in.

### The close, after the last unit

- RED-first observation of every `New arm:` line the passes declared (each builder return names its own), by hand.
- Two strays in the git common dir red `record-kinds --check`: `dHomedResolver` and `history-verdicts`; record and
  move them before the bar.
- The inherited check-21 red on dWitnessedBar's `replay.py` record: a red-fix adding its Serves line.
- The record-causes leg reds two fixture writers spelling Serves with no cause, in `tools/memory-tree/record_find.py`
  and `tools/playbook/gov_tag.py` (unit 9's own).
- Re-measure the suite ceilings and self-test budgets units 3, 9, 12, 19, 22 and 43 grew; the build README slot
  contract warns on READMEs unit 53's parallel note grew.
- Spec 21 sits over the spec ceiling (warn only); name it at wrap-up.
- Then the closing review (`tools/workflows/tier2-review.js`, roles from `handoff.py harness-args tier2-review`),
  `--phase VERIFYING`, `push-main.sh --prepare --slug dTotalRecall`, the deviations report, `--authorization`,
  `--close`, `push-main.sh --land --slug dTotalRecall`, `--landed`, `CronDelete` the idle-wake, and the attests.

### Owner decisions to name at the wrap-up

- dWitnessedBar's packet pins dClosedLoop's `schedule.py` at a blob HEAD no longer holds; `--repin` is the owner's.
- Asks TOOL-dTotalRecall-109, -111, -112 and -113 stand; the spec audit was not owed (opt-in, the owner's).
- PLAY-dClosedLoop-1003's "until then" clause names a row unit 56 moved from `record_kinds.py` to `tree_lib.py`.
- A record-kind owner column no unit adds; a lost create race read as offline in `unattended.sh#run_entry_claim`;
  the record door's doubled deviation title prefix; `tools/policy/check_policy.py#load_run_readers` omits
  `id_grammar.py`.

### Acceptance

The run resumes on node a from HELD, builds every remaining unit, and lands; `unattended.sh --landed dTotalRecall`
reads its landing.

### Non-goals

No unit held on an owner ask is built. No spec audit.
