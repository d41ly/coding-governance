# TOOL-dWitnessedBar-25 — the verdict names its bar run and its cause, and a failing leg's output tail is kept by hash

**Status:** CLOSED · rev-5 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 18 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0363@4ad46937 whole
**Carries:** node:policy-key.trace.leg-output

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-26-build-TOOL-dWitnessedBar-25-deviation-251.md](../build/2026-10-26-build-TOOL-dWitnessedBar-25-deviation-251.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-25-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-25-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-25-deviation-972.md](../build/2026-11-20-build-TOOL-dWitnessedBar-25-deviation-972.md) | deviation | — |
| [2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-77.md](../build/2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-77.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-78.md](../build/2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-78.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-79.md](../build/2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-79.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-80.md](../build/2026-11-20-build-TOOL-dWitnessedBar-25-red-fix-80.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-26 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-55 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-25-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-25-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-25-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-25-reground-brief.md) | journal | TOOL-dWitnessedBar-40 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-25-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-25-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

The runner's verdict record names neither the bar run it closes nor what started that run: the run
record's verdict block (`tools/run-gates/run-gates.sh@86758a96:5747-5765`) carries no `run_id`, which
sits in the run's header (`tools/run-gates/run-gates.sh@86758a96:3669`) and on unit 4's per-tree
verdict, and nothing records the push, pass or session behind it (P35, the away pass's point 4). A failing leg's output is copied, redacted,
into `<git-dir>/gate-run/<run id>/<i>.out` and dies with its worktree, or with the five-run sweep
(gap-test-20). This unit puts `run_id` and `cause` on the verdict, keeps each failing leg's output
tail by its hash in the common dir, and under `trace.leg-output: tail-by-hash`, the default (the
owner's AP-22), commits it as a record a later reader finds by that hash.

## 2. Scope (IN)

- **S1** — `run_id`. The run record's verdict block (`tools/run-gates/run-gates.sh@86758a96:5747-5765`)
  gains `run_id`, the `RUNID` its header already writes; the per-tree verdict of unit 4 already carries
  it (`tools/run-gates/run-gates.sh@86758a96:5878`). Observed by AC1.
- **S2** — `cause`. The runner reads `GATE_CAUSE` once and unsets it before any leg starts, as it does
  `GATE_RUN_ID` (read at `tools/run-gates/run-gates.sh@86758a96:1629`, unset at
  `tools/run-gates/run-gates.sh@86758a96:2787`), and writes `cause` into the verdict block and the
  per-tree verdict: `<kind>:<id>` from the caller, else `attended`. The callers that start a bar
  export it: `.githooks/pre-push` as `push:<pushed sha>`, beside its `GATE_RUN_ID` export
  (`.githooks/pre-push@100bfdc7:2399`); `tools/run-gates/post-merge.sh` as `post-merge:<landed sha>`
  in `tools/run-gates/post-merge.sh#run_bar`; `tools/unattended/unattended.sh` as `run:<slug>` on the
  bar's `env` argv in `tools/unattended/unattended.sh#dod_met`; and `tools/run-gates/pass-legs.sh`,
  landed since the base, as `pass:<head sha>` on its one runner call
  (`tools/run-gates/pass-legs.sh@0a13e66a:364`, §8 F6). That is every tracked caller pinning
  `GATE_RUN_ID`, by `git grep -n 'GATE_RUN_ID='` outside the suites, re-derived at `c34f63b6` on
  2026-11-20; `tools/run-gates/run-held-wsl.sh`'s halves, which run in a scratch clone or mirror no
  boundary reads, are outside it and read `attended`. Observed by AC2.
- **S3** — The tail. For each leg whose result is a failure, the runner takes the last 60 lines of its
  redacted output copy, at most 8192 bytes, hashes them with `git hash-object --stdin`, writes them to
  `<common-dir>/gate-tails/<hash>` when no file holds that hash, and adds `tail.<n>` with the value
  `<hash> <leg name>` to the verdict block and the per-tree verdict, `<n>` an index from 1 (I8,
  runlog's grammar). Observed by AC3 and AC4.
- **S4** — The sweep. The run sweep past `GATE_RUN_KEEP` (`tools/run-gates/run-gates.sh@86758a96:5929-5933`)
  also sweeps the tails directory, so it holds exactly the tails some retained run record names.
  Observed by AC5.
- **S5** — The committed home. `tools/run-gates/keep_tails.py --run <run id> --build <slug> --unit <id>`
  reads `trace.leg-output` through `policy.py get` (TOOL-dGroundRules-2), the catalogue default where
  the reader cannot run (TOOL-dGroundRules-3), as `tools/run-gates/product_tests.py#read_product_value`
  reads `tests.product`. Under `tail-by-hash` it writes, for each `tail.<n>` of the run, one `leg-tail`
  record through the record factory's `tools/memory-tree/build_records.py#write_record`
  (PLAY-dOrderedCharter-7 S7), skipping a hash a tracked `leg-tail` record already holds. It reaches
  the factory as `tools/drift-audit/drift_report.py` reaches a memory-tree module: the kit found by the
  run-gates kit's inline `tools/run-gates/leg_factory.py#resolve_kit_dir`, then imported (§8 F4). It
  hands `write_record` the build, the unit, the five fields of S6 and the tail; under `node-local` it
  writes nothing and says so. The unattended driver calls it on the red path of its one bar,
  `gates-green` in `tools/unattended/unattended.sh#dod_met`, with `--run` that bar's pinned id and
  `--unit` the build's record anchor `tools/unattended/unattended.sh#derive_review_signals` derives,
  staging what it wrote where that path stages its `gates-run` fact, so the records commit with the
  close's (§8 F5). Each tail is masked by runlog's `scan_secrets` before it is written (§8 F3).
  Observed by AC6, AC7 and AC9.
- **S6** — The `leg-tail` kind. A kind row of `tools/memory-tree/build_records.py`: name
  `<date>-build-<unit id>-leg-tail-<n>.md` in the build's `build/` folder, served as
  `**Serves:** leg-tail <unit id>`, required fields `Leg`, `Hash`, `Run`, `Sha`, `Cause`, the tail in
  one fenced block after them. The kind joins the reader in the same pass: `leg-tail` is added to
  `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`, which the factory's kind table must equal at
  import (PLAY-dOrderedCharter-42 S1, S2), and to the closed `<kind>` list of
  `tools/memory-tree/HYGIENE.template.md` (its S5); under its S3 a `-leg-tail-<n>.md` file served as
  any other kind is malformed. The landed factory's `new` verb takes only its closed door tuple
  (`tools/memory-tree/build_records.py#DOORS`), every other kind being `write_record`'s alone, as
  `widen` is; this unit adds no door (§8 F4). The factory's `--fixture --plant typed-kinds` writes one
  record of every `TYPED_RECORD_KINDS` member, so the kind joins that round trip with no fixture edit.
  The closed list's sentence "The ten after `research` are the typed kinds" counts the members, ten
  at HEAD (PINNED 2026-11-20, DERIVED by `len(tree_lib.TYPED_RECORD_KINDS)`), and reads eleven after
  this unit. `write_record` refuses a line after the fields that would read as a field or holds a CR,
  so a tail holding one is refused whole; its fence and decode are unit 51's (id 61). Observed by AC6
  and AC10.
- **S7** — The key's catalogue row. `trace.leg-output`'s row of `tools/policy/catalogue.toml`
  (TOOL-dGroundRules-1 S3) gets its `summary` and `usage`, drained from
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`; no row is added. The rendered
  `help/reference/policy.md`, which lists the key under its unsummarised heading, is re-rendered by
  `python tools/playbook/render_playbook.py --reference`, giving the key a section of its own, as
  unit 4's S7 did for `verdict.tree`. The mirror `.governance/policy.json` renders a committed
  catalogue only, so `python tools/policy/policy.py mirror --write` re-renders it after the pass
  commit, as unit 4's red-fix `56569347a` did. Observed by AC8.
- **S8** — The kit page. `tools/run-gates/README.md` states `run_id`, `cause`, `tail.<n>`, the tails
  directory and the keep verb, in its sections "The run record" and "The verdict per tree".
  NOT OBSERVED — prose, read by the closing review.

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
- **consumes-from** external — PLAY-dOrderedCharter-7 S7's record factory `build_records.py`, which the `leg-tail` kind joins, and PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS`, file-name join and closed kind list; dGroundRules' catalogue row and reader for `trace.leg-output`
- **hands-off** `TOOL-dWitnessedBar-42` — the tail sweep, which unit 42 widens to every worktree's retained runs, with a grace for fresh tails and a renamed write (id 60)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 11 and 61: its `New arm:` line's flag read by suite path, and the tail's byte cut, decode and fence, each a scope item of that unit

## 4. Design

### The keys

| Key | Value | Written in |
|---|---|---|
| `run_id` | `RUNID` | the run record's verdict block |
| `cause` | `push:<sha40>`, `post-merge:<sha40>`, `run:<slug>`, `pass:<sha40>`, or `attended` | the verdict block and the per-tree verdict |
| `tail.<n>` | `<hash> <leg name>`, the hash first, the name the rest of the value | both |

`cause`'s value matches `[A-Za-z0-9._:@-]+`; an exported value outside it is recorded as `attended`
with a stderr line naming what was refused, so a leg's environment cannot write a field separator into
the record. `GATE_CAUSE` is unset before the first leg for `GATE_RUN_ID`'s reason: a leg driving a
nested runner, as the kit's suites do, would otherwise name its caller's cause. The unset also
precedes the runner's environment digest, which lists every `GATE_*` name it still sees
(`tools/run-gates/run-gates.sh@86758a96:3594`), and the hook exports the cause after its reuse view
writer, so no reuse key moves with the cause. A cause a caller set before `git push` reaches the view
and costs a cache miss, never a false hit.

### The tail and its hash

The tail is taken from `$RUNDIR/<i>.out`, the copy `write_redacted` already masked
(`tools/run-gates/run-gates.sh@86758a96:4130`), so nothing reaches a durable file that the run record
does not already hold. 60 lines and 8192 bytes are this unit's bound (PINNED, the author's choice): enough
for a stack and its assertion, small enough that a red bar of twenty legs commits under 200 KB. The
hash is git's blob id of the tail bytes, so the same failure on two nodes is one hash and one record.
`<common-dir>` is resolved as unit 4's per-tree writer resolves it from `RG_COMMON_RAW`
(`tools/run-gates/run-gates.sh@86758a96:5863`), so every worktree of a clone writes one directory and
the tail outlives the worktree that produced it.

### `trace.leg-output`

| Value | The runner | `keep_tails.py` |
|---|---|---|
| `tail-by-hash` (default) | keeps the tail node-locally and names it in the verdict | commits each tail as a `leg-tail` record |
| `node-local` | the same | writes nothing, printing `trace.leg-output is node-local` |

The runner never reads the key: the node-local half is the same under both values, and the committed
half is the keep verb's, which is the key's one reader.

### Inventory

Minted: the verdict keys `run_id` (in the run record), `cause` and `tail.<n>`; the variable
`GATE_CAUSE` and the value forms of the table above; the directory `<common-dir>/gate-tails/`; `tools/run-gates/keep_tails.py`; the record kind
`leg-tail` with its five fields, a member of `TYPED_RECORD_KINDS`. Naming cells: each is asked of `python tools/lexicon/lexicon.py
--suggest <name>` at the pass.

### Migration

Additive: every reader selects verdict keys by name (`tools/run-gates/run-gates.sh#read_record_keys`,
`.githooks/pre-push#read_bar_file`), so a record without the new keys still reads.

### Rollout

Live at landing. The first red bar after it writes the first tail.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/keep_tails.py`
- `tools/run-gates/post-merge.sh`
- `tools/run-gates/pass-legs.sh`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `tools/unattended/unattended.sh`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/tree_lib.py`: `leg-tail` in `TYPED_RECORD_KINDS`
- `tools/memory-tree/HYGIENE.template.md`, and its render `memory/HYGIENE.md`: `leg-tail` in the closed kind list
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/reference/policy.md`
- `.governance/policy.json`, re-rendered after the pass commit (S7)
- `memory/guides/SESSION-KICKOFF.md`: its `watch:` line holds `tools/run-gates/run-gates.sh`, so its
  `last-audit` is re-stamped

### Alternatives rejected

- **A new top-level directory under `memory/` for tails.** It needs hygiene check 3's fixed directory
  set and `memory/HYGIENE.md`'s layout widened, a governance-carrier change this clause does not name;
  a build-folder record under an existing kind grammar needs neither, only its kind's member of the
  closed kind list (§8 F1).
- **The full log committed.** A red suite's log runs to megabytes, and the tail is what a reader acts on.
- **A `new leg-tail` door the keep verb runs as a subprocess.** A new public verb of the factory, for
  one caller that can reach `write_record` the way other kits already reach a memory-tree module
  (§8 F4).

## 5. Production-readiness checklist

- security — the tail is cut from the copy already redacted by `redact`, which masks URL userinfo
  only, and committing it widens its reach to the remote. So `keep_tails.py` also runs runlog's
  `scan_secrets` (`tools/runlog/runlog_lib.py#scan_secrets`) over each tail and masks every span it
  returns before the record is written, through `tools/runlog/runlog_lib.py#render_redacted`, which
  replaces each span with its placeholder; the runlog kit is reached as the factory is (S5). It is
  the same scan the run log applies to committed text (§8 F3).
- perf / scale — one `git hash-object` per red leg; the sweep is one directory listing.
- error / empty / loading states — a red with no output copy writes `tail.<n>` with the empty tail's
  hash; a keep run over a green run writes nothing and says so; a tail `write_record` refuses (S6) is
  named on stderr with the refusal and writes no record.
- observability — the verdict names the run, the cause and each tail; the keep verb prints each record
  it wrote or skipped.
- risks — a large output committed through a tail; bounded by S3's bytes.
- testing — fixtures on scratch clones; the suite arm in §7 is observed RED then GREEN by the main loop
  at the close.
- migration — additive, as §4 Migration says.
- user docs — `tools/run-gates/README.md` (S8); no page under `help/` covers the runner.

## 6. Acceptance criteria

- **AC1** — When the runner closes a run over a fixture manifest (`GATE_LEGS=<fixture>`, the runner's
  manifest knob at `tools/run-gates/run-gates.sh@86758a96:416`) in a scratch clone,
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
  `tail-by-hash`, and `grep -cx 'trace.leg-output' unsummarised-keys.txt` under `tools/policy/` prints 0,
  and `grep -c '^## .trace\.leg-output.$' help/reference/policy.md` prints 1.
  Red when: the row keeps an empty `summary` or `usage`, or the reference page still lists the key as
  unsummarised.
- **AC9** — When the keep verb runs over a tail holding a value one of runlog's default secret rules
  matches, the written `leg-tail` record holds the masked span and not the value.
  Red when: the committed tail carries a secret the redacted run copy kept.
- **AC10** — When `python gen_build_index.py --print-bindings` runs in `tools/memory-tree/` over AC6's
  scratch tree with the record committed, it prints an `S` row for `<date>-build-TOOL-x-1-leg-tail-1.md`
  with kind `leg-tail`, and no `A` row for it.
  Red when: the record serves as `journal`, or the kind is added to the factory alone, so the factory
  refuses at import or the record reads malformed.

## 7. Gates

`measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates run-log line` · `pre-push self-test` · `memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `routed-commits selftest` · `tier2-review self-test` · `policy fixtures` · `policy check` · `help reference pages`

The guards join's broad `.githooks/`, `tools/`, `tools/run-gates/` and `tools/memory-tree/` guards are
excluded by the checker's floor. `memory-hygiene self-test` runs the factory's typed-kinds round trip
that S6's kind joins; `policy check` and `help reference pages`, landed since the base, carry no guard
and run on every bar: they read S7's row and its render. The unattended kit's suites are waived for
this build's landing.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a failing fixture leg, a credential-shaped line, a tabbed `GATE_CAUSE` and a run count past `GATE_RUN_KEEP`, each staged on a scratch clone · none
New arm: tools/run-gates/keep_tails.py --selftest · covers AC6 AC7 AC9 · a tail already tracked, the key planted `node-local`, and a secret-shaped line, each staged in a scratch tree · none

## 8. Open questions

- **F1 — Where is the committed tail kept, so that HYGIENE admits it?** Options: (a) a `leg-tail` kind of
  the record factory, one build-folder record per hash, named by check 5's existing build-record grammar;
  (b) a new `memory/traces/` directory admitted by check 3 and the layout in `memory/HYGIENE.md`; (c) a
  tracked file under `tools/run-gates/`. (b) changes a governance carrier's layout the clause does not
  name, which the `may:` grant PLAY-dClosedLoop-3 does not lift, and (c) puts run output in kit source
  that ships. Rev-2 bound (a) as `journal`, which PLAY-dOrderedCharter-42 S3 makes malformed for a
  `-leg-tail-<n>.md` file. Its S5 makes the closed kind list of `tools/memory-tree/HYGIENE.template.md`
  the place every typed kind is declared, so (a) adds one member there, the edit dDeclaredLoop's units
  3, 16, 17 and 22 make for their kinds, and no directory or layout. RESOLVED (agent, 2026-10-26,
  delegated): (a), served as `leg-tail`, rung 1, PLAY-dOrderedCharter-42 S2, S3 and S5, tie-broken by
  reuse of S7's factory. widens: none · relaxes: none
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
- **F4 — How does the keep verb reach the record factory now that it has landed?** Rev-3 had it run
  the factory as a subprocess and left the call to this re-ground. The landed `new` verb takes only
  `tools/memory-tree/build_records.py#DOORS`, and a kind outside it is `write_record`'s alone, as
  `widen` is. Options: (a) resolve the memory-tree kit with the run-gates kit's inline
  `resolve_kit_dir` and import `write_record`, as `tools/drift-audit/drift_report.py`,
  `tools/codebase-map/map_lib.py` and the loop kit reach memory-tree modules; (b) add a `new leg-tail`
  door the verb runs as a subprocess; (c) write the record file in the factory's grammar from
  `keep_tails.py`. (b) adds a public verb to the factory (veto 2), the precedent unit 4's F4 set for a
  new flag; (c) is a second writer of one grammar without the factory's forged-field refusals.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3, the most feature-rich survivor, tie-broken by
  reuse of the resolve-then-import seam. widens: none · relaxes: none
- **F5 — Where does the driver call the keep verb, and for which unit?** Rev-4 said "a red bar of a
  dispatched pass", and the driver runs one bar, `gates-green` at its close
  (`tools/unattended/unattended.sh#dod_met`), which belongs to no single unit. Options: (a) that bar's
  red path, `--unit` the build's record anchor `derive_review_signals` derives for the driver's own
  close-time records, the written records staged where that path stages its `gates-run` fact; (b) no
  driver call, the verb run by hand; (c) `pass-legs.sh` calls it, which knows no build or unit and
  would need new flags (veto 2). (b) leaves an unattended run's red tails uncommitted, against §1.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3, the one survivor that keeps §1, tie-broken by
  reuse of the driver's anchor. widens: none · relaxes: none
- **F6 — Does `pass-legs.sh`, a bar caller landed since the base, export a cause?** Options: (a) yes,
  `pass:<head sha>`, the value §1 names as "pass"; (b) no, its runs read `attended`. (b) records a
  builder's pass bar as attended, which §1 says nothing records today. RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3, the more feature-rich option. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 25 and Obligations row v2:1395, the brief's
  I8, scout A's row for cl-0363, research-observability-trace.md OB-4 and the away pass's AP-22.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-42, TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-26 · §2 S5, S6 · §3 Edges · §4 Inventory, Files touched, Alternatives rejected ·
  §6 AC10 · §7 · §8 F1 · §10 · re-grounded on dOrderedCharter at `462d20f35` and dDeclaredLoop at
  `783f1ad3a` by the cross-check record `build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md`,
  row 77: the record serves as `leg-tail`, joined to `TYPED_RECORD_KINDS` and the HYGIENE kind list;
  the binding is observed; the factory is run as a subprocess; F1 re-resolved; no `new leg-tail` door
  is claimed.
- rev-4 · 2026-11-19 · §7 · the leg line gains `scratch-guard self-test`, `routed-commits selftest`,
  `tier2-review self-test` and `policy fixtures`, whose manifest guards hold the §4 paths
  `tools/unattended/unattended.sh`, `tools/policy/catalogue.toml` and `tools/memory-tree/build_records.py`,
  per brief 2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief; nothing else moved.
- rev-5 · 2026-11-20 · §1 · S1 S2 S5 S6 S7 S8 · §4 · §5 · AC1 AC8 · §7 · §8 F4 F5 F6 · §10 · re-grounded
  at `c34f63b6` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-25-reground-brief: runner and hook lines
  blob-pinned, the rest cited as `path#symbol`; S2's callers re-derived, `pass-legs.sh` added and
  `run-held-wsl.sh` named outside; S5 reaches the landed factory's `write_record` by import and the
  driver's call sits on `gates-green`'s red path; S6 names the landed door tuple and the kind count;
  S7 re-renders `help/reference/policy.md` and the policy mirror; AC1's manifest is `GATE_LEGS`, and
  AC8 greps the reference page; Files touched gains `pass-legs.sh`,
  those two renders and the kickoff manifest; the leg line gains `memory-hygiene self-test`,
  `policy check` and `help reference pages`.

## 10. Reuse audit

The seams extended are the runner's verdict block and header
(`tools/run-gates/run-gates.sh@86758a96:5747-5765`, `tools/run-gates/run-gates.sh@86758a96:3669`), its
redacted output copy (`tools/run-gates/run-gates.sh@86758a96:4130`) and run sweep
(`tools/run-gates/run-gates.sh@86758a96:5929-5933`), the `GATE_RUN_ID` read-and-unset idiom, unit 4's
per-tree verdict writer (`tools/run-gates/run-gates.sh@86758a96:5858-5888`), the policy read of
`tools/run-gates/product_tests.py#read_product_value`, the driver's record anchor
`tools/unattended/unattended.sh#derive_review_signals`, and PLAY-dOrderedCharter-7 S7's record factory
`tools/memory-tree/build_records.py#write_record`, extended by one kind and its `TYPED_RECORD_KINDS`
member (PLAY-dOrderedCharter-42) and reached as `tools/drift-audit/drift_report.py` reaches a
memory-tree module. `python tools/codebase-map/reuse_lookup.py "keep a failing leg's output tail by
its hash beyond the worktree"`, re-run at `c34f63b6`, ranked generic stems (`legs`, `fail`,
`read_git_output`) and named no tail store, which is the expected answer: scout A found output living
only in the run directory, and `tools/run-gates/run-gates.sh#derive_fail_tail` names a failure's
reason, not its output. The recall probe returned the brief's row, scout A's row and v2's
`[policies]` row; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a failing leg's output tail kept by hash and the verdict named by its run and cause" --terms "trace.leg-output tail-by-hash node-local run_id cause verdict record failing leg output worktree P35 AP-22 OB-4"`
