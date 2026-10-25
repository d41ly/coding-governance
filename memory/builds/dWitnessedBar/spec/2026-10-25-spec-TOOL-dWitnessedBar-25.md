# TOOL-dWitnessedBar-25 — the verdict names its bar run and its cause, and a failing leg's output tail is kept by hash

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 18 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0363@4ad46937 whole
**Carries:** node:policy-key.trace.leg-output

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-26 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

The runner's verdict record names neither the bar run it closes nor what started that run: `run_id`
sits only in the run's header (`tools/run-gates/run-gates.sh:3481`), and nothing records the push,
pass or session behind it (P35, the away pass's point 4). A failing leg's output is copied, redacted,
into `<git-dir>/gate-run/<run id>/<i>.out` and dies with its worktree, or with the five-run sweep
(gap-test-20). This unit puts `run_id` and `cause` on the verdict, keeps each failing leg's output
tail by its hash in the common dir, and under `trace.leg-output: tail-by-hash`, the default (the
owner's AP-22), commits it as a record a later reader finds by that hash.

## 2. Scope (IN)

- **S1** — `run_id`. The run record's verdict block (`tools/run-gates/run-gates.sh:5552-5570`) gains
  `run_id`, the `RUNID` its header already writes; the per-tree verdict of unit 4 already carries it.
  Observed by AC1.
- **S2** — `cause`. The runner reads `GATE_CAUSE` once and unsets it before any leg starts, as it does
  `GATE_RUN_ID` (`tools/run-gates/run-gates.sh:2617-2623`), and writes `cause` into the verdict block
  and the per-tree verdict: `<kind>:<id>` from the caller, else `attended`. The callers that start a bar
  export it: `.githooks/pre-push` as `push:<pushed sha>`, `tools/run-gates/post-merge.sh` as
  `post-merge:<landed sha>`, `tools/unattended/unattended.sh` as `run:<slug>`. Observed by AC2.
- **S3** — The tail. For each leg whose result is a failure, the runner takes the last 60 lines of its
  redacted output copy, at most 8192 bytes, hashes them with `git hash-object --stdin`, writes them to
  `<common-dir>/gate-tails/<hash>` when no file holds that hash, and adds `tail.<n>` with the value
  `<hash> <leg name>` to the verdict block and the per-tree verdict, `<n>` an index from 1 (I8,
  runlog's grammar). Observed by AC3 and AC4.
- **S4** — The sweep. The run sweep past `GATE_RUN_KEEP` (`tools/run-gates/run-gates.sh:5688-5696`)
  also sweeps the tails directory, so it holds exactly the tails some retained run record names.
  Observed by AC5.
- **S5** — The committed home. `tools/run-gates/keep_tails.py --run <run id> --build <slug> --unit <id>`
  reads `trace.leg-output` through `policy.py get` (TOOL-dGroundRules-2), the catalogue default where
  the reader cannot run (TOOL-dGroundRules-3). Under `tail-by-hash` it writes, for each `tail.<n>` of the
  run, one record through the record factory's `leg-tail` kind (PLAY-dOrderedCharter-7 S7), skipping a
  hash a tracked `leg-tail` record already holds; under `node-local` it writes nothing and says so. The
  unattended driver calls it on a red bar of a dispatched pass, before its records commit. Each tail is
  masked by runlog's `scan_secrets` before it is written (§8 F3). Observed by AC6, AC7 and AC9.
- **S6** — The `leg-tail` kind. A kind row of `tools/memory-tree/build_records.py`: name
  `<date>-build-<unit id>-leg-tail-<n>.md` in the build's `build/` folder, binding
  `**Serves:** journal <unit id>` (`memory/HYGIENE.md`, "Record bindings"), required fields `Leg`,
  `Hash`, `Run`, `Sha`, `Cause`, the tail in one fenced block after them. Observed by AC6.
- **S7** — The key's catalogue row. `trace.leg-output`'s row of `tools/policy/catalogue.toml`
  (TOOL-dGroundRules-1 S3) gets its `summary` and `usage`, drained from
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`; no row is added. Observed by AC8.
- **S8** — The kit page. `tools/run-gates/README.md` states `run_id`, `cause`, `tail.<n>`, the tails
  directory and the keep verb. NOT OBSERVED — prose, read by the closing review.

## 3. Non-goals (OUT)

- The per-tree verdict file and the verdict's `tree`: unit 4's, which this unit writes keys into.
- `warn.<k>`: unit 29's, which joins the block after `run_id`.
- The causal edge `caused-by` and a required `parent` field on every record kind: dOrderedCharter's and
  dTotalRecall's (research-observability-trace.md:114-118); `cause` is the verdict's own key until
  then, its value the act that started the bar.
- `gov trace` and `gov why`: dWellOiledMachine's.
- A full output log committed: the tail alone travels, the full redacted copy stays in the run record.
- The unattended kit's own self-test suites: waived for this build's landing (README rule).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-4` — `gate-verdict`, the per-tree verdict and the run record's verdict block this unit adds `cause` and `tail.<n>` to; without it the tail has no per-tree record to ride
- **hands-off** `TOOL-dWitnessedBar-29` — `run_id`, the verdict-record key the warning keys `warn.<k>` sit after, so a breach is joined to the run that showed it
- **consumes-from** external — PLAY-dOrderedCharter-7 S7's record factory `build_records.py`, which the `leg-tail` kind joins; dGroundRules' catalogue row and reader for `trace.leg-output`
- **hands-off** `TOOL-dWitnessedBar-42` — the tail sweep, which unit 42 widens to every worktree's retained runs, with a grace for fresh tails and a renamed write (id 60)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 11 and 61: its `New arm:` line's flag read by suite path, and the tail's byte cut, decode and fence, each a scope item of that unit

## 4. Design

### The keys

| Key | Value | Written in |
|---|---|---|
| `run_id` | `RUNID` | the run record's verdict block |
| `cause` | `push:<sha40>`, `post-merge:<sha40>`, `run:<slug>`, or `attended` | the verdict block and the per-tree verdict |
| `tail.<n>` | `<hash> <leg name>`, the hash first, the name the rest of the value | both |

`cause`'s value matches `[A-Za-z0-9._:@-]+`; an exported value outside it is recorded as `attended`
with a stderr line naming what was refused, so a leg's environment cannot write a field separator into
the record. `GATE_CAUSE` is unset before the first leg for `GATE_RUN_ID`'s reason: a leg driving a
nested runner, as the kit's suites do, would otherwise name its caller's cause.

### The tail and its hash

The tail is taken from `$RUNDIR/<i>.out`, the copy `write_redacted` already masked
(`tools/run-gates/run-gates.sh:3938-3942`), so nothing reaches a durable file that the run record does
not already hold. 60 lines and 8192 bytes are this unit's bound (PINNED, the author's choice): enough
for a stack and its assertion, small enough that a red bar of twenty legs commits under 200 KB. The
hash is git's blob id of the tail bytes, so the same failure on two nodes is one hash and one record.
`<common-dir>` is resolved as the `.shared` stamp resolves it, so every worktree of a clone writes one
directory and the tail outlives the worktree that produced it.

### `trace.leg-output`

| Value | The runner | `keep_tails.py` |
|---|---|---|
| `tail-by-hash` (default) | keeps the tail node-locally and names it in the verdict | commits each tail as a `leg-tail` record |
| `node-local` | the same | writes nothing, printing `trace.leg-output is node-local` |

The runner never reads the key: the node-local half is the same under both values, and the committed
half is the keep verb's, which is the key's one reader.

### Inventory

Minted: the verdict keys `run_id` (in the run record), `cause` and `tail.<n>`; the variable
`GATE_CAUSE`; the directory `<common-dir>/gate-tails/`; `tools/run-gates/keep_tails.py`; the record kind
`leg-tail` with its five fields. Naming cells: each is asked of `python tools/lexicon/lexicon.py
--suggest <name>` at the pass.

### Migration

Additive: every reader selects verdict keys by name (`read_record_keys`,
`tools/run-gates/run-gates.sh:2387`), so a record without the new keys still reads.

### Rollout

Live at landing. The first red bar after it writes the first tail.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/keep_tails.py`
- `tools/run-gates/post-merge.sh`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `tools/unattended/unattended.sh`
- `tools/memory-tree/build_records.py`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`

### Alternatives rejected

- **A new top-level directory under `memory/` for tails.** It needs hygiene check 3's fixed directory
  set and `memory/HYGIENE.md`'s layout widened, a governance-carrier change this clause does not name;
  a build-folder record under an existing kind grammar needs neither (§8 F1).
- **The full log committed.** A red suite's log runs to megabytes, and the tail is what a reader acts on.

## 5. Production-readiness checklist

- security — the tail is cut from the copy already redacted by `redact`, which masks URL userinfo
  only, and committing it widens its reach to the remote. So `keep_tails.py` also runs runlog's
  `scan_secrets` (`tools/runlog/runlog_lib.py:522`) over each tail and masks every span it returns
  before the record is written, the same scan the run log applies to committed text (§8 F3).
- perf / scale — one `git hash-object` per red leg; the sweep is one directory listing.
- error / empty / loading states — a red with no output copy writes `tail.<n>` with the empty tail's
  hash; a keep run over a green run writes nothing and says so.
- observability — the verdict names the run, the cause and each tail; the keep verb prints each record
  it wrote or skipped.
- risks — a large output committed through a tail; bounded by S3's bytes.
- testing — fixtures on scratch clones; the suite arm in §7 is observed RED then GREEN by the main loop
  at the close.
- migration — additive, as §4 Migration says.
- user docs — `tools/run-gates/README.md` (S8); no page under `help/` covers the runner.

## 6. Acceptance criteria

- **AC1** — When the runner closes a run over a fixture manifest (`--legs <fixture>`) in a scratch clone,
  `grep -P '^run_id\t' verdict` in the run's directory prints the id the run's `header` names.
  Red when: the verdict block omits the id, so a verdict cannot be joined to its run without the header.
- **AC2** — When the same run is started with `GATE_CAUSE` set to `push:` and a SHA, the verdict and the
  per-tree verdict both read `cause push:<sha>`; with `GATE_CAUSE` unset they read `cause attended`; with
  a tab in the value they read `attended` and stderr names the refusal; and a fixture leg that prints
  its own environment shows no `GATE_CAUSE`.
  Red when: a leg inherits the cause, or a malformed value reaches the record.
- **AC3** — When the fixture's one leg prints 100 numbered lines and exits 1, the verdict holds
  `tail.1` naming that leg, and `<common-dir>/gate-tails/<hash>` holds its last 60 lines, its name equal
  to `git hash-object` of its bytes.
  Red when: the tail is cut from unredacted output, or its file name is not its hash.
- **AC4** — When a leg prints a URL carrying `user:secret@` before failing, the tail file holds
  `***:***@` and not `secret`.
  Red when: the tail bypasses the redacted copy.
- **AC5** — When more runs than `GATE_RUN_KEEP` complete and the oldest run alone named a tail, the
  sweep removes that tail and keeps every tail a retained run names.
  Red when: tails accumulate past every run that named them, or a named tail is removed.
- **AC6** — When `python keep_tails.py --run <id> --build x --unit TOOL-x-1` runs in a scratch tree under
  `trace.leg-output = "tail-by-hash"` over a run holding one tail, one `leg-tail` record exists under
  the build's `build/` folder with `**Hash:**` equal to the tail's hash and the tail in a fenced block;
  a second run of the verb writes nothing new.
  Red when: the verb writes a second record for a hash already tracked.
- **AC7** — When the same verb runs under `trace.leg-output = "node-local"`, it writes no record and
  prints `trace.leg-output is node-local`.
  Red when: `node-local` commits the tail.
- **AC8** — When `python policy.py get trace.leg-output` runs on the built tree, it prints
  `tail-by-hash`, and `grep -cx 'trace.leg-output' unsummarised-keys.txt` under `tools/policy/` prints 0.
  Red when: the row keeps an empty `summary` or `usage`.
- **AC9** — When the keep verb runs over a tail holding a value one of runlog's default secret rules
  matches, the written `leg-tail` record holds the masked span and not the value.
  Red when: the committed tail carries a secret the redacted run copy kept.

## 7. Gates

`measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates run-log line` · `pre-push self-test` · `memory hygiene`

The guards join's broad `.githooks/`, `tools/` and `tools/run-gates/` guards are excluded by the
checker's floor; dOrderedCharter's record-factory leg and dGroundRules' `policy check` leg are not in
the manifest at this spec's base. The unattended kit's suites are waived for this build's landing.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a failing fixture leg, a credential-shaped line, a tabbed `GATE_CAUSE` and a run count past `GATE_RUN_KEEP`, each staged on a scratch clone · none
New arm: tools/run-gates/keep_tails.py --selftest · covers AC6 AC7 AC9 · a tail already tracked, the key planted `node-local`, and a secret-shaped line, each staged in a scratch tree · none

## 8. Open questions

- **F1 — Where is the committed tail kept, so that HYGIENE admits it?** Options: (a) a `leg-tail` kind of
  the record factory, one build-folder record per hash, named by check 5's existing build-record grammar
  and bound `journal`; (b) a new `memory/traces/` directory admitted by check 3 and the layout in
  `memory/HYGIENE.md`; (c) a tracked file under `tools/run-gates/`. (b) changes a governance carrier the
  clause does not name, which the `may:` grant PLAY-dClosedLoop-3 does not lift, and (c) puts run output
  in kit source that ships. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the record's home
  registered through the grammar and binding HYGIENE already states, tie-broken by reuse of S7's
  factory. widens: none · relaxes: none
- **F2 — What is a verdict's `cause` before dOrderedCharter's `caused-by` edge and dTotalRecall's
  `parent` field land?** Options: (a) the act that started the bar, exported by its caller as
  `GATE_CAUSE`, `attended` when none; (b) the run's parent record id, which no kind declares yet. (b)
  has no value to write today. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; the later edge
  reads the key as data. widens: none · relaxes: none
- **F3 — Does a committed tail need more masking than the run copy's?** Options: (a) the keep verb runs
  runlog's `scan_secrets` and masks each span before writing; (b) the run copy's `redact` alone. (b)
  commits to the remote any secret shape `redact` does not know, a write surface wider than the run
  record's node-local one (veto 3). RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by
  reuse of runlog's scanner. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 25 and Obligations row v2:1395, the brief's
  I8, scout A's row for cl-0363, research-observability-trace.md OB-4 and the away pass's AP-22.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-42, TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are the runner's verdict block and header (`tools/run-gates/run-gates.sh:3481`,
`:5552-5570`), its redacted output copy (`:3938-3942`) and run sweep (`:5688-5696`), the
`GATE_RUN_ID` read-and-unset idiom (`:2617-2623`), unit 4's per-tree verdict, and PLAY-dOrderedCharter-7
S7's record factory. `python tools/codebase-map/reuse_lookup.py "keep a failing leg's output tail by its
hash beyond the worktree"` ranked generic stems (`legs`, `fail`, `read_git_output`) and named no tail
store, which is the expected answer: scout A found output living only in the run directory, and
`derive_fail_tail` (`:4012`) names a failure's reason, not its output. The recall probe returned the
brief's row, scout A's row and v2's `[policies]` row; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a failing leg's output tail kept by hash and the verdict named by its run and cause" --terms "trace.leg-output tail-by-hash node-local run_id cause verdict record failing leg output worktree P35 AP-22 OB-4"`
