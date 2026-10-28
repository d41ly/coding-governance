# TOOL-dWellOiledMachine-8 — the persisted-return store, keyed per spawn site, and the shared deferral block

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 31 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0286@459158b1 whole
**Carries:** node:record-kind.return

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-8-deviation-81.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-8-deviation-81.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

Spawned work dies with its session: limits killed 57 agents in 16 Workflow runs, 7 of 12 all-errored
runs report `completed`, and a null `agent()` result becomes `committed:false` with no reason
(gap-rt-03; `tools/workflows/unattended-unit.js:344`). This unit persists every role agent's return
of an act from where it lives, at SubagentStop, keyed by the item instance, the work order and the
spawn site, so a fresh relaunch hands the returns back and the harness spawns only the agents without
one; and it carries one deferral shape, `deferred-platform`, as a byte-identical block in every role
harness under a parity check (layer-runtime `[spawn]`, :543-591).

## 2. Scope (IN)

- **S1** — The store (I25, refined here as its owner). `<git-common-dir>/gov/returns/<key>/<site>.json`,
  node-local and never committed. `<key>` is `derive_return_key(instance_key, task_sha)` in the new
  `tools/runtime/returns.py`: the first 12 hex of the SHA-256 of the I14 instance key, a newline and
  the work order's `task-sha`, `derive_section_sha`'s rule (`tools/roles/handoff.py:307`). `<site>` is
  the first 12 hex of the SHA-256 of the spawn site label (S2). The file is one JSON object: `key`,
  `instance`, `task-sha`, `site` (the label in clear), `act`, `agent`, `agent-type`, `written-utc`,
  `bytes`, `outcome` (`return` or `refusal`), and `return` or `why`. `write_return` writes it through
  a temp file and `os.replace`; a second write for one site that differs in content is refused, so a
  persisted return never changes. Observed by AC1, AC2.
- **S2** — The spawn site. For an agent whose `agent_transcript_path` lies under
  `subagents/workflows/<run id>/`, the site is the `description` of the sibling
  `agent-<id>.meta.json`, which is the `label` the harness passed to `agent()`; for a direct `Agent`
  spawn it is `direct · <description>`. Both survive a relaunch with identical args, unlike
  `agent_id`. Observed by AC1.
- **S3** — The SubagentStop pack. `tools/runtime/returns.fragment.json` (I9: class `record`, failure
  `open`, `budget-ms` 5000, key `roles.retries`, and a `witness` naming the record `returns` and
  the reader `supervise.py`) runs `returns.py stop` through the new `tools/runtime/pyrun.sh`, a shim carrying the
  inline `resolve_python` block (`tools/lib/resolve-python.sh`), as `tools/lib/pyrun.sh` does for a
  merge driver, so every Python pack of the runtime kit has one launcher. It acts only in an act
  session, where the launch environment carries `GOV_ACT` and `GOV_RETURN_KEY` (S6); anywhere else it
  prints nothing, writes nothing and exits 0. The return is the input of the agent's last
  `StructuredOutput` call in its transcript, else `last_assistant_message` (layer-runtime `[spawn]`).
  Observed by AC1, AC3.
- **S4** — A failing return held, then refused. An empty or unparseable return, or one over
  `RETURN_CAP_BYTES`, exits 2 with one stderr line naming why, so the agent keeps running; holds are
  counted per site in `<site>.holds`. At `roles.retries` holds (`tools/policy/catalogue.toml:259`,
  default 3, read through `resolve`, I31) the pack writes the site with `outcome: refusal` and the
  reason, and exits 0. Observed by AC3.
- **S5** — The deferral block (I25's second half), `// >>> gov_returns_js` to `// <<< gov_returns_js`,
  canonical in `tools/runtime/returns-block.js` and carried byte-identical by
  `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`, their
  renders, and `tools/workflows/unattended-unit.js`. It holds `renderDeferral(key, pending, durable)`,
  returning `{exit: 'deferred-platform', key, pending, durable}`, and `readKeptReturn(a, label)`,
  returning `a.returns[label]` or `undefined`. Every `agent(` call site of the three harnesses asks
  `readKeptReturn` first and spawns only on `undefined`; every `exit: 'deferred-platform'` literal
  they hold today becomes a `renderDeferral` call. Observed by AC4, AC5.
- **S6** — `unattended-unit.js`'s null path. A null `agent()` result returns
  `renderDeferral(identity, [identity], false)` beside `committed: false` and `why: 'deferred-platform'`,
  never a bare `committed:false`. Its callers re-run once with identical args and hold on a second, as
  they already do for a review (`tools/unattended/VERBS.template.md:747-753`): the `/build` Skill's
  stage 5 source `tools/roles/SKILL.template.md` (:66-71) and `VERBS.template.md:762` each gain that
  clause. Observed by AC5.
- **S7** — The supervisor's half (I21, TOOL-dWellOiledMachine-6). At each S4 launch `supervise.py`
  sets `GOV_RETURN_KEY` from the act's instance key and work order; on a `fresh` relaunch it passes
  `read_returns(key)`, a `{label: return}` map of every `return` outcome, as the harness args'
  `returns`; under the `headless` backend it writes the process's `structured_output` from its
  `result.json` as site `headless`; and at an `act-exit` whose item is witnessed it clears the key's
  directory. A relaunch therefore re-pays only the sites with no return. Observed by AC6.
- **S8** — The kind. `record-kind.return` is a `[[record-kind]]` row in
  `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1 S1): name `return`, tag
  `record.return`, layer `runtime`, home `<git-common-dir>/gov/returns/`, schema form `header` sourced
  at `tools/runtime/returns.py:RETURN_FIELDS`, writer `returns.py`, readers `supervise.py`, lifecycle "written once per spawn site, cleared when the item is witnessed", and
  `check` the leg of S9. The `SubagentStop` row of `tools/runtime/witnesses.toml`
  (TOOL-dWellOiledMachine-10 S10) names `returns` and `supervise.py`, armed by this unit. Observed by
  AC7.
- **S9** — The parity check. `python returns.py --check-block` derives its population as every
  tracked `*.js` carrying the opening marker, refuses an empty population, and prints one line per
  file that differs from the canonical, exit 1 on any; the leg `runtime returns block parity` in
  `tools/gate-legs.json` runs it. `tools/runtime/kit.toml` (I1) lists the three new files. Observed
  by AC4.
- **S10** — `help/runtime.md` gains the store, its key, the hold and refusal, the hand-back and the
  deferral shape. Observed by AC8.

## 3. Non-goals (OUT)

- Validating a return against the item's schema and the return contract: dBoundRoles' return check
  (TOOL-dBoundRoles-5, -39); this unit checks size and parse only, before the write.
- The DURABILITY writes three harnesses ask of their agents, and `tier2-review.js`'s key-directory
  reuse under `workerType: 'none'`: unchanged; the kept return is asked first and the key directory
  after it.
- Whether SubagentStop fires for every way an agent ends: TOOL-dWellOiledMachine-1's spike rows. A
  site with no return is re-paid, so a stop that never fires costs a re-spend, never a wrong result.
- Routing a refusal by the item's outcome table: the loop kit's (TOOL-dDeclaredLoop-7); this unit
  persists the refusal it routes.
- `resumeFromRunId`: not relied on, since it replays only in the same session (layer-runtime
  `[spawn]`).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, whose launch sets `GOV_RETURN_KEY`, whose fresh relaunch hands the persisted returns back as `returns`, and whose clean exit removes them
- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, on whose `SubagentStop` entry the returns pack registers, and the `SubagentStop` row of `witnesses.toml`
- **hands-off** `TOOL-dWellOiledMachine-4` — `pyrun.sh`, the launcher the prompt-submit pack runs its Python through
- **hands-off** `TOOL-dWellOiledMachine-7` — `pyrun.sh`, the launcher the act-binding pack runs through
- **hands-off** `TOOL-dWellOiledMachine-43` — `pyrun.sh`, the launcher the in-flight ledger pack runs through
- **consumes-from** external — TOOL-dTotalRecall-1's `record-kinds.toml`, where the `return` row lands, and the I14 instance key of TOOL-dDeclaredLoop-7 S3
- **hands-off** `TOOL-dWellOiledMachine-74` — the `gov_returns_js` block and `readKeptReturn`, which that unit keys by the spawn input (finding 59)
- **hands-off** `TOOL-dWellOiledMachine-79` — the returns pack, `pyrun.sh` and the `gov_returns_js` block (findings 13, 14, 40, 42), which the spec audit's minors batch repairs

## 4. Design

### Evidence

- The deferral shape exists in one harness and one hold: `tier2-review.template.js:1312`, `:1337`,
  `:1667`, `:1701`, `:2020`, held on at `unattended-build.template.js:1710-1725`; the unit harness's
  null path is `unattended-unit.js:333-348`.
- A Workflow agent's files sit under `<session dir>/subagents/workflows/<run id>/`: `journal.jsonl`
  with `{"type":"started","key","agentId","label","phase"}` lines, and per agent `agent-<id>.jsonl`,
  `.meta.json` (`agentType`, `description`, `workflowPhase`) and `.prefix.json`. Measured on this
  node on 2026-10-26 over this session's own run `wf_7c0507f0-43d`, whose `description` equals the
  journal's `label`. PINNED: re-measured by the spike's case directories (TOOL-dWellOiledMachine-1
  S4).
- Agent call sites today: `tier2-review.template.js` 4 (`:1004`, `:1181`, `:1381`, `:1721`),
  `unattended-build.template.js` 5 (`:977`, `:1194`, `:1425`, `:1860`, `:2054`),
  `unattended-unit.js` 1 (`:333`). DERIVED by `grep -n "agent(" <file>`.
- A hook's interpreter is the closed pair `node` and `bash` (`tools/settings-merge.py:247`), so a
  Python pack needs a bash launcher; `tools/lib/pyrun.sh` is gov-internal and ships nothing.
- TOOL-dBoundRoles-40 replays a recorded harness-stage stop against every `SubagentStop` hook and reds
  any stdout, any blocking exit and any return-check record. Its payload carries no `GOV_ACT`, so S3
  stays silent there.

### Data model

```json
{"key": "3f9c0a1b2c4d", "instance": "build.unit@1·1#a1b2", "task-sha": "0a1b2c3d4e5f",
 "site": "fx · find:security", "act": "act-0a1b2c3d4e5f", "agent": "a50e64c0d2d6cb0a5",
 "agent-type": "gov-diff-reviewer", "written-utc": "2026-10-26T21:00:00Z", "bytes": 812,
 "outcome": "return", "return": {"findings": []}}
```

`RETURN_FIELDS` is the tuple of those keys plus `why`. `RETURN_CAP_BYTES` is 262144, PINNED
2026-10-26 as a bound on a runaway return, not measured from a population.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `returns.py` with `stop`, `write`, `read`, `--check-block`, `--fixture` | runtime kit file | none |
| `derive_return_key`, `write_return`, `read_returns` | Python functions | `derive`, `write`, `read`, OK |
| `pyrun.sh` | runtime kit file | none |
| `returns-block.js`, `gov_returns_js` | block canonical and marker | none |
| `renderDeferral`, `readKeptReturn` | JS functions | `render`, `read`, OK |
| `GOV_RETURN_KEY` | launch environment variable | none |
| `RETURN_CAP_BYTES`, `RETURN_FIELDS` | constants | none |
| `runtime returns block parity` | gate leg | none |

### Files touched (estimate)

- `tools/runtime/returns.py`, `tools/runtime/returns-block.js`, `tools/runtime/pyrun.sh`,
  `tools/runtime/returns.fragment.json` (new)
- `tools/runtime/supervise.py`, `tools/runtime/witnesses.toml`, `tools/runtime/kit.toml`
- `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js`
- `tools/workflows/unattended-build.template.js`, rendered to `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-unit.js`
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/memory-tree/record-kinds.toml`
- `tools/gate-legs.json`
- `help/runtime.md`

### Alternatives rejected

- **The store keyed by `agent_id` or run id.** Both change on a relaunch, so a fresh act could find
  nothing it lost (layer-runtime `[spawn]`).
- **Returns written through the door into the build folder.** The door writes tracked records into
  the act's working tree (TOOL-dTotalRecall-2), where an uncommitted return would ride the act's own
  commit; a node-local store survives every session death and touches no tree.
- **A parity row in `tools/lib/resolve-python.test.sh`.** Its population grep reads `# >>>` markers
  over `*.sh`, `*.py` and the git hooks only (`:226`), so a JS block is invisible to it.

## 5. Production-readiness checklist

- security — a new node-local write path, reached only by a pack that refuses outside an act session;
  a return is size-capped and parsed before the write; no return is ever committed.
- perf / scale — one bash and one Python start per agent stop; one directory per item instance, removed
  at its witness.
- error / empty / loading states — no `GOV_ACT` writes nothing; a missing `.meta.json` writes nothing
  and leaves the site re-payable; a crashed pack persists nothing, and the item stays re-dispatchable.
- observability — each held return names why on stderr; each refusal is a stored `why`.
- risks — a harness that labels two agents alike in one run loses the second return to S1's refusal,
  which re-pays it; a label carrying a run-varying value never matches on relaunch.
- testing — the fixture cases of §6 and the arms of §7.
- migration — none: no store exists; the harnesses' argument shape gains an optional `returns`.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python returns.py --fixture --plant <case>`: a scratch git repository under `%TEMP%`
with a short name, a session directory holding one Workflow run's `journal.jsonl`, agent transcripts
and `.meta.json` files, and the launch environment the case names.

- **AC1** — When `--plant persist` pipes a SubagentStop payload for a schema-forced agent, the store
  holds one site file whose `return` byte-equals the run journal's `result` value for that agent,
  and the `site` is its `description`.
  Red when: the pack reads `last_assistant_message` for a schema-forced agent, or keys by `agent_id`.
- **AC2** — When `--plant rewrite` stops the same site twice with different returns, the second write
  is refused and the file is unchanged; with equal content it exits 0.
  Red when: a persisted return changes.
- **AC3** — When `--plant oversized` stops an agent whose return is `RETURN_CAP_BYTES` plus one byte,
  the pack exits 2 three times and on the fourth writes `outcome: refusal` naming the cap; when
  `--plant unbound` pipes the TOOL-dBoundRoles-40 payload with no `GOV_ACT`, stdout is empty, exit 0,
  and nothing is written.
  Red when: an oversized return is stored, the hold never ends, or an unbound stop writes.
- **AC4** — When `python returns.py --check-block` runs over the tree, it prints
  `5 file(s) carry gov_returns_js · 0 differ`; with one byte changed in a scratch copy of `unattended-unit.js`'s block it
  exits 1 naming that file.
  Red when: a drifted copy passes, or an empty population passes.
- **AC5** — When `node run.js tools/workflows/unattended-unit.js` (the stub runner the
  tier2-review suite on the §7 `New arm:` line writes) runs with `agent()` answering null, the result carries
  `exit: 'deferred-platform'` and `why: 'deferred-platform'`; with `returns` holding the unit's label,
  no `agent()` call is made and the kept return is the result.
  Red when: a null becomes a bare `committed: false`, or a kept return is spawned again.
- **AC6** — When `python supervise.py --fixture --plant relaunch-returns` kills a five-agent act after
  two sites are stored and relaunches it `fresh`, the relaunch's harness args carry exactly those two
  labels under `returns`, the stub harness spawns exactly three agents, and after a witnessed exit the
  key directory is gone.
  Red when: the relaunch respawns a stored site, or the store outlives the witness.
- **AC7** — When `grep -n 'name = "return"' record-kinds.toml` runs over the registry, it prints the
  row, and the `SubagentStop` row of `witnesses.toml` names `returns`.
  Red when: the kind has no row.
- **AC8** — When `grep -n "deferred-platform\|GOV_RETURN_KEY" runtime.md` runs over the help page, both
  are named.
  Red when: the page omits either.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/returns.py · covers AC1 AC2 AC3 AC4 · each plant staged against a pack keyed by `agent_id` and with the cap check removed, and the parity check fed one drifted copy · none
New arm: tools/workflows/tier2-review.test.sh · covers AC5 · a stub run of the unit harness with a null `agent()`, staged on today's null path · none
New arm: tools/runtime/supervise.py · covers AC6 · the relaunch plant staged against a supervisor that passes no `returns` · none

## 8. Open questions

- **F1 — Where does a return live?** (a) A node-local store under the common git directory, keyed by
  instance and work order; (b) a tracked record through TOOL-dTotalRecall-2's door in the build folder.
  (b) lands an uncommitted file in the act's working tree, which the act's own commit would carry, and
  survives no better: a take-over on another node relaunches from the work order either way. Rung 3,
  the option meeting every criterion of §6. RESOLVED (agent, 2026-10-26, delegated): (a), registered as
  a kind whose `home` is the store. widens: none · relaxes: none
- **F2 — How is the spawn site named?** (a) The `agent()` label, read from the agent's `.meta.json`;
  (b) a new marker line every harness prepends to each agent prompt. (b) edits every prompt and is
  refused on a direct spawn, whose prompt TOOL-aOrientedCast-7's rule 6 holds to the marker and the
  task section (`tools/hooks/agent-cap.js:1700-1712`). Rung 3, reuse of a field the platform already
  writes. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-74, TOOL-dWellOiledMachine-79.

## 10. Reuse audit

The seams extended: the deferral shape `tier2-review.template.js` already returns and
`unattended-build.template.js:1710` already holds on, made one block; the Workflow run's own files,
whose `.meta.json` names each agent's label; `derive_section_sha` (`tools/roles/handoff.py:307`) for
the key's rule; and the merge-driver shim `tools/lib/pyrun.sh`, whose shape the kit's `pyrun.sh`
copies with the parity-gated `resolve_python` block. The probe
`python tools/codebase-map/reuse_lookup.py "persist a subagent return keyed by spawn site and hand it
back on relaunch"` ranked `key`, `keys`, `read_conf_key` and `readConfKey` by name stem, none a store;
scout A's row 4 holds at this base, its `load_run_journal` (`handoff.py:686`) read for the evidence
and not called, since `.meta.json` names the label without a journal scan.

Recall terms used: `python tools/memory-recall/query.py "how are subagent returns persisted and the
deferral shape shared across harnesses" --terms "persisted return SubagentStop deferred-platform
pending durable spawn site relaunch structured_output harness"`
