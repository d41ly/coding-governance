# DEPL-dShippedRelease-13 — `deploy.core`: the core checks read on the landed tree, the per-SHA verdict and the patch a red files

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 9 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0423@a0a019f7 whole
**Carries:** node:item.deploy.core

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-14 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-13-deviation-131.md](../build/2026-10-30-build-DEPL-dShippedRelease-13-deviation-131.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

A landing is released with nothing having read the landed tree. The lander starts a bar and returns,
its header saying it does not check "whether that bar ever finished" (`tools/push-main.sh:43-47`),
and undeclared it starts nothing. The verdict sits in one last-verdict file a later landing overwrites
(`gap-deploy-02`), and `GATE_POST_MERGE=ci` binds nothing (`gap-deploy-10`). This unit builds
`deploy.core`: it starts or finds the full bar on the landed SHA, reads a verdict keyed by that SHA
with its publication state apart, files a patch build on a red through the entry-point table's
post-close row, and answers whether that build may close. The build stays leased until `deploy.unlease` releases it, so this unit's verdict is read before that release.

## 2. Scope (IN)

- **S1** — The per-SHA verdict record (pin C6, `gap-deploy-02`). Every exit of `post-merge.sh` that has
  resolved `<sha>` writes, beside the last-verdict file, the record `write_core_verdict`: a
  node-local file `<common-dir>/gate-post-merge.d/<sha>` first, then the ref
  `refs/gov/core-verdict/<sha>`, one commit by `build_gov_commit`, written through the kit's inline
  `write_gov_ref` (TOOL-dPlacedRequest-11 S1). Its keys are `sha`, `verdict` (`GREEN`, `RED` or
  `REFUSED`), `published` (`pushed`, `cleared`, `kept`, `none` or `failed`), `why`, `run_id`, `source`
  (`post-merge` or `remote-ci`), `node` and `stamped`. The two facts are separate keys on every path,
  a `failed` publication beside a `RED` included, and a ref write that fails leaves the file and
  prints one line. Observed by AC1, AC2.
- **S2** — `post-merge.sh --publish <sha> [--verdict GREEN|RED --run-id <id> --source <s>]` runs the
  existing publication (`tools/run-gates/post-merge.sh:374-397`) and S1's write with no bar: the verdict
  comes from the flags, else from the file S1 wrote. A missing verdict is a refusal, exit 2. It is what
  a re-try of a failed publication and a remote read call, so `refs/gov/bar-red` has one publisher.
  Observed by AC2, AC6.
- **S3** — The reader, `read_core_verdict(sha, root)` in `tools/loop/deploy_items.py` and `python
  deploy_items.py read-core-verdict <sha>`, shared interface I9. One bounded fetch of the ref, then the
  file; it prints `verdict`, `published` and `run_id` as `<key><TAB><value>` lines. No record prints
  `verdict<TAB>none`, exit 0. A failed fetch with no file is a dead probe, exit 2, never `none`. A
  record whose `sha` differs from the ref's name is refused, exit 1. Observed by AC1, AC3.
- **S4** — The start, `push-main.sh --post-merge <sha>`, a fifth lander flag: `run_post_merge`
  (`tools/push-main.sh:427`) takes the SHA and an `undeclared` argument, so one start writes the
  detached run, the per-SHA log and `gate-post-merge.start` (`:454-459`). A start record or a per-SHA
  log naming `<sha>` starts nothing and prints `post-merge bar already shows for <sha8>`. Observed by AC3.
- **S5** — The verb, `unattended.sh --deploy core <slug> <sha>`, over `run_deploy_core(slug, sha, root)`
  in `deploy_items.py`. It reads `GATE_POST_MERGE` as committed at `<sha>` by the lander's own
  `read_policy_key` rule. Under `local` or undeclared, `read_core_verdict` answers; on `none` it runs
  S4 and answers `running`. The undeclared arm is the clause's: gov's own tree declares no key
  (`.githooks/gate-env.sh` holds none), and `flow-steps.md:452-456` has `deploy.core` start the bar
  there. The bar is the full bar, `GATE_FULL=1` as `post-merge.sh` runs it (`:310`), which covers the
  core checks. Observed by AC3, AC4.
- **S6** — `GATE_POST_MERGE=ci` (`gap-deploy-10`, pin C6). `deploy_items.py` runs `python
  verdict_backends.py read --backend remote-ci --sha <sha>` (TOOL-dWitnessedBar-6 S3, S6, its reader in
  `remote_verdict.py`). `GREEN` with witness `witnessed` and `RED` each run S2 with `--source
  remote-ci`, so a remote red reaches `refs/gov/bar-red` and the hook. `GREEN` with witness `claimed`,
  under `verdict.remote.trust: app-only`, is a claim: the verb runs S4 and advances on the local run.
  `NONE` answers `running`, `HELD` and `DEAD PROBE` answer no verdict and never green. With no
  `remote-ci` row in `read_backends`, `read_policy_value("policy-file.on-missing-expansion", root)`
  decides: `refuse` exits 2 naming the key and the backend, `fallback-reported` runs S4 and prints one
  report line. Observed by AC5.
- **S7** — The routes, each read from `read_core_verdict`, the verb's one exit per answer (§4 "The
  routes"). `green` and `red` set the landing record's `core` and, on a red, `patch-key`, through
  `set_landing_field` (DEPL-dShippedRelease-1 S6). `REFUSED` re-runs once after a fetch, then raises an
  owner item. `published: failed` routes as its verdict does and runs S2 once, then raises an owner
  item. `running` prints `core — <sha8> · running` and exits 3 for the next beat, and past
  `runtime.act-ceiling` hours, counted from the start record, raises an owner item. Owner items are
  `raise_owner_item("core-verdict", build, …)`, a kind this unit adds to `OWNER_ITEM_KINDS`. Observed
  by AC4, AC6.
- **S8** — The patch filing (pin C9). On a red, `run_deploy_core` derives `derive_red_key(sha)`, shared
  interface I9, the key `request.py key` gives the canonical text `default-branch-red <sha>`, and files
  `python intake.py file --origin landing --build <slug> --sha <sha>` with that text. So the key is
  (`default-branch-red`, landed SHA), the one Maintain's reading uses, and a second filing of one red
  is the same key and no second patch. The post-close row is stated here, §4 "The post-close row",
  since it exists only at `2026-10-14-build-PLAY-dClosedLoop-1-flow.md:628`. Observed by AC7.
- **S9** — The settlement, `read_core_settlement(sha, root)` and `python deploy_items.py core-settled
  <sha>`: `settled · green`, `settled · patch-green <sha>`, `settled · excepted <record>`, `open ·
  unfiled`, `open · filed <key>` or `open · no verdict`, exit 0 for settled and 1 for open. A red with
  no filing is `open · unfiled` whatever else exists. A filed red is settled only by a `GREEN` record
  at a SHA that contains the landed one whose landing record's build carries the patch's key (§8 F6),
  or by an exception under `core.exceptions` naming the landing (§8 F4). `check_core_settled`
  (DEPL-dShippedRelease-4) calls this and adds no rule. Observed by AC8, AC9.
- **S10** — The item armed: the `item.deploy.core` row's witness reads "the bar's verdict for the
  landed SHA", its `[[stand-in]]` row leaves `tools/loop/loop.toml`, and its outcomes are `green`,
  `red`, `refused` and `running`. Observed by AC10.
- **S11** — The docs: `tools/run-gates/README.md` states the per-SHA record and `--publish`; the
  header of `tools/push-main.sh` states `--post-merge`; `tools/unattended/VERBS.template.md`, rendered
  to `memory/guides/UNATTENDED-VERBS.md`, and `help/deploy.md` state the verb, the routes and what
  settles a red. `KIT_UNATTENDED_VERSION` and the run-gates kit's version move. NOT OBSERVED by a
  criterion: prose, read by the memory hygiene leg at the close.

**Build-run preconditions**: `write_gov_ref` (TOOL-dPlacedRequest-11), `read_backends` and the
`remote-ci` reader (TOOL-dWitnessedBar-6), `intake.py` (TOOL-dWellOiledMachine-4, -27, with the change
§8 F3 asks), `raise_owner_item` (TOOL-dWellOiledMachine-48), `core.py exceptions`
(PLAY-dOrderedCharter-7), `read_claim_body` (TOOL-dPlacedRequest-21), `read_landing` and
`set_landing_field` (DEPL-dShippedRelease-1).

## 3. Non-goals (OUT)

- The `deploy.close` term and the wait a red landing's close holds in: DEPL-dShippedRelease-4. This
  unit answers the question; that unit asks it. The clause's two seen-red cases are observed here on
  `core-settled` and again there on `--deploy close`.
- The budget a patch draws, a chain of patches and the double-filing case of cl-dClosedLoop-0440:
  DEPL-dShippedRelease-30.
- A hook change. Under an undeclared `GATE_POST_MERGE` a published red binds no later push
  (`.githooks/pre-push:1911-1912`). This unit leaves that as it is, §8 F7.
- Declaring `GATE_POST_MERGE` in this repository's `.githooks/gate-env.sh`: an owner's bar-cost choice.
- The `remote-verdict` record kind and the re-home of `remote-ci` into `tools/integrations/`: not in
  any clause of this build's 31.
- A second reader of `gate-post-merge`, the last-verdict file, which stays as it is for `--status`.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing` and `set_landing_field`, the record `core` and `patch-key` land on, which `core-settled` reads for the patch's build
- **hands-off** `DEPL-dShippedRelease-4` — `read_core_verdict` and `read_core_settlement`, which `check_core_settled` runs
- **hands-off** `DEPL-dShippedRelease-30` — `read_core_verdict` and `derive_red_key`, the key one red files one patch under
- **hands-off** `DEPL-dShippedRelease-15` — `read_core_verdict`, the green `release.pick` requires
- **consumes-from** external — TOOL-dWitnessedBar-6's `verdict_backends.py` and `remote_verdict.py`, TOOL-dWellOiledMachine-27's `intake.py` with the `landing` origin §8 F3 asks for, TOOL-dWellOiledMachine-48's `raise_owner_item`, PLAY-dOrderedCharter-7's `core.py exceptions`, TOOL-dPlacedRequest-11's `write_gov_ref` and -21's `read_claim_body`
- **hands-off** external — dTendedCadence's `maintain.patch` reads the same key by the same text; it has no spec to cite

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `run_post_merge` (`tools/push-main.sh:427`) reads the key at the landed tip, starts nothing on an
  empty value (`:433`) or on `ci` (`:434`), and writes the log and start record (`:454-459`). The
  start record holds one SHA; the log is per SHA.
- `post-merge.sh` writes one last-verdict file (`write_post_merge_record`, `:55`), keyed by nothing,
  from two sites: `write_refusal` (`:70`) and the end (`:408`). The refusals above `:94`, where `SHA`
  resolves, have no key, so S1 says "has resolved".
- Its publication has four outcomes and a `failed` (`:374-397`); `publish FAILED` prints instead of a
  verdict (`:402`), which is the disagreement `flow-steps.md:468` records.
- A run record is copied only past a non-REFUSED bar (`:370-371`), and the log names it only on RED
  (`:406`), so `flow-steps.md:469` ("reads the verdict from the bar's run record") has no SHA-to-run
  join. S1 makes that step unnecessary: `run_id` is on the per-SHA record.
- `.githooks/pre-push:1911-1912` binds a published red only where `PM_DECL` is non-empty.

### The routes

| `read_core_verdict` answer | Record | Then |
|---|---|---|
| `GREEN` | `core: green` | `deploy.record` |
| `RED` | `core: red`, `patch-key`, patch filed | `deploy.record`; the close waits on S9 |
| `REFUSED` | none on the first | fetch, one re-run; the second `REFUSED` sets `core: refused` and raises the owner item |
| `published: failed` beside either | as that verdict | `post-merge.sh --publish <sha>` once, then the owner item |
| `none`, a run showing | none | `core — <sha8> · running`, exit 3; past the ceiling, the owner item |
| dead probe | none | exit 2; the next beat re-reads |

`deploy.record` follows `deploy.core` in flow-steps:438-439. A `running` first answer does not hold it:
DEPL-dShippedRelease-1 §8 F2 writes `core: pending`, and this verb sets the field when it reads.

### The post-close row

From `2026-10-14-build-PLAY-dClosedLoop-1-flow.md:628`, the entry-point table: after its build closed
at landing, a post-landing core red, a landing-review finding or a decision-log row missing at the
landed SHA enters Design as a patch build, as a patch intake that `deploy.core`, the landing review or
`deploy.distill` files, placed by `entry.place`, then `entry.claim`, then `plan.dedupe`, then a
micro-spec at Design. `flow-steps.md:438`, `:440`, `:495` and `:574` all cite it, and neither `[entry]`
section holds it. This unit is its first filer; DEPL-dShippedRelease-14 and -30 cite this section.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_core_verdict`, `derive_red_key`, `run_deploy_core`, `read_core_settlement` | functions, `deploy_items.py` | `py.function`, each answered OK by `--suggest` at `5d1c82ac` |
| `write_core_verdict` | shell function, `post-merge.sh` | `sh.function`, OK |
| `--post-merge`, `--publish`, `--deploy core` | flags and a verb | none |
| `refs/gov/core-verdict/<sha>`, `<common-dir>/gate-post-merge.d/` | ref namespace and directory | none |
| `core-verdict` | `OWNER_ITEM_KINDS` member | none |

### Migration

None. A landing before this unit has no record, and `read_core_verdict` answers `none`.

### Rollout

The per-SHA record is live for every post-merge run from this landing. `deploy.core` runs when
DEPL-dShippedRelease-4 calls it. On a tree with `GATE_POST_MERGE` undeclared, this repository's, the
first `--landed` after that landing starts a full bar on the landed SHA, a cost the landing did not
pay before: about the bar's own time, on the turnstile.

### Files touched (estimate)

- `tools/run-gates/post-merge.sh`: S1, S2, the `write_core_verdict` calls
- `tools/push-main.sh`: S4 and its header
- `tools/push-main.test.sh`: the arms of §7
- `tools/loop/deploy_items.py`: S3, S5, S6, S7, S8, S9
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/loop/loop.toml`: S10
- `tools/runtime/owner_items.py`: the `core-verdict` member
- `tools/unattended/unattended.sh`: the verb, `KIT_UNATTENDED_VERSION`
- `tools/run-gates/README.md`: S11
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S11
- `help/deploy.md`: S11

### Alternatives rejected

- **`refs/gov/verdict/<sha>` as the record.** Rejected by pin C6: TOOL-dWitnessedBar-6 S5 gives that
  ref to the peer's annotated tag, a candidate before landing, with no `published` key. Test: S5's
  field list.
- **A node-local per-SHA file alone.** Rejected: a second node after a take-over reads nothing. Test:
  cl-dClosedLoop-0508's killed-supervisor case. The file stays as the copy a failed ref write leaves.
- **Reading the run record as `flow-steps.md:469` writes.** Rejected: no SHA-to-run join exists, and a
  REFUSED run has no copy (scout A disagreement 4). Test: `post-merge.sh:370-371`.
- **Copying the start into `deploy_items.py`.** Rejected: fifteen lines of detach, log and start record
  twice, and the copy is the one that drifts. Test: `tools/push-main.sh:440-463`.
- **`check_expansion_value` for the missing backend.** Rejected: it reads a catalogue default on
  `fallback-reported`, and `GATE_POST_MERGE` has no catalogue row. Test: TOOL-dDeclaredLoop-2 S8.

## 5. Production-readiness checklist

- security — `refs/gov/core-verdict/` sits outside the coordination door, as `refs/gov/bar-red` does,
  so a pusher can forge a green: the same trust the default branch already extends to that grant, and
  S3 refuses a mismatched SHA. `--publish --verdict` is reached only from a read of the backend. The
  record holds no secret: `why` is a git or bar line, stripped of tabs and newlines.
- perf / scale — a full bar per landing where none ran before, on the host turnstile.
- error / empty / loading states — S7's table: every answer has a route, and `none`, dead probe and
  `HELD` are never green.
- observability — one `core —` line per run, naming the answer; the record names its `run_id`.
- risks — a run killed by a reboot leaves no record: past the ceiling the owner item says so. Two nodes
  can run one bar after a take-over: the second write parents on the first and the tip is the newest.
- testing — `deploy_fixture.py` for the verb and `tools/push-main.test.sh` for the two shell flags.
- migration — none.
- user docs — `help/deploy.md`, `memory/guides/UNATTENDED-VERBS.md`, `tools/run-gates/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case core-record` runs a stub bar through `post-merge.sh` on
  one clone and `python deploy_items.py read-core-verdict <sha>` on the other, the second prints
  `verdict`, `published` and `run_id`; a later landing's run leaves the first SHA's record unchanged.
  Red when: the verdict is overwritten by a later landing, the defect of `gap-deploy-02`.
- **AC2** — When `python deploy_fixture.py --case core-publish-failed` breaks the push of `refs/gov/bar-red`
  beside a RED, the record reads `verdict RED` and `published failed`; a `REFUSED` run writes a record
  too; and `post-merge.sh --publish <sha>` with the push restored reads `published pushed` with no bar run.
  Red when: any exit path with a resolved SHA leaves no record, or the two facts share one key.
- **AC3** — When `python deploy_fixture.py --case core-undeclared` runs `--deploy core` on a tree that
  declares no `GATE_POST_MERGE`, a run starts and `gate-post-merge.start` names the SHA; a second run
  prints `already shows` and starts none; with the fetch broken and no file `read-core-verdict` exits 2.
  Red when: an undeclared key starts nothing, or a dead read reads `none`.
- **AC4** — When `python deploy_fixture.py --case core-routes` plants each of a green, a red and a
  running bar, the verb sets `core green`, sets `core red` with a `patch-key`, and exits 3 printing
  `running`; with the planted start older than `runtime.act-ceiling` it raises one `core-verdict` item.
  Red when: a running bar reads as green, or the ceiling raises nothing.
- **AC5** — When `python deploy_fixture.py --case core-ci` plants `GATE_POST_MERGE=ci` and a stub
  backend answering each of `GREEN`, `RED`, `HELD` and `DEAD PROBE`, then `claimed`, a remote `RED`
  appears at `refs/gov/bar-red` and on the record with `source remote-ci`, `HELD` and `DEAD PROBE` set
  no `core`, and `claimed` starts the local run; with the `remote-ci` row absent, `.governance/policy.toml`
  planted `policy-file.on-missing-expansion = "refuse"` exits 2 and `"fallback-reported"` starts the local run.
  Red when: a remote red misses `refs/gov/bar-red`, the defect of `gap-deploy-10`.
- **AC6** — When `python deploy_fixture.py --case core-republish` plants a `failed` publication, the verb
  routes on the verdict, runs `--publish` once, and on a second failure raises one owner item; a
  planted `REFUSED` re-runs once after a fetch and then raises one.
  Red when: a failed publication blocks the verdict's route, or the retry repeats.
- **AC7** — When `python deploy_fixture.py --case core-patch-filed` runs the verb twice on a planted red,
  `python intake.py ratifies <key>` prints `ratifies · landing`, and the fixture's one request is
  named by the key `python deploy_items.py derive-red-key <sha>` prints.
  Red when: a landing red files nothing, or two filings make two keys.
- **AC8** — When `python deploy_fixture.py --case core-settled-unfiled` plants a red landed tree with no
  filing, `python deploy_items.py core-settled <sha>` exits 1 printing `open · unfiled`; a green prints
  `settled · green`.
  Red when: a build could close on a red with no filing, the clause's first seen-red case.
- **AC9** — When `python deploy_fixture.py --case core-settled-filed` plants a filed red, `core-settled`
  exits 1 printing `open · filed`; a `GREEN` record at a descendant SHA of an unrelated build leaves it
  open; the patch build's green prints `settled · patch-green`; and an exception whose `Excuses` reads
  `landing:<sha>` prints `settled · excepted`, while `.governance/policy.toml` planted
  `core.exceptions = "none"` leaves it open.
  Red when: a filed patch not yet green reads settled, the clause's second seen-red case.
- **AC10** — When `grep -c 'item = "item.deploy.core"' loop.toml` runs at the pass, it prints 0.
  Red when: the stand-in row outlives the armed item.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `push-main self-test` · `run-gates canary` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit version markers` · `python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms`

New arm: tools/push-main.test.sh · covers AC2 AC3 · `--post-merge` on an undeclared key and a shown run, and `--publish` with a broken push, staged against the base lander, which refuses the flag · none

New arm: tools/loop/deploy_fixture.py · covers AC1 AC4 AC5 AC6 AC7 AC8 AC9 · the `core-` cases, the failing case `core-settled-filed` staged against `read_core_settlement` with its green join unkeyed · none

## 8. Open questions

- **F1 — What form does the post-landing verdict take?** Options: (a) a ref distinct from
  `refs/gov/verdict/<sha>`, with a node-local copy; (b) the file alone; (c) a tracked record. (b) fails
  a take-over and (c) is the post-push commit `unattended.sh:6354-6357` refuses. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3, pin C6, scout A's fork 8. widens: none · relaxes: none · grants:
  PLAY-dClosedLoop-3 the ref namespace `refs/gov/core-verdict/` and the flags `--post-merge` and `--publish`
- **F2 — Does the verb start the bar itself, or only read?** The clause says the lander runs the
  checks and it only starts them (scout A disagreement 3). Options: (a) `deploy.core` starts or finds
  the run and reads by SHA; (b) make the lander wait for the bar, holding the push's process for its
  whole length. (b) fails on a killed lander, the clause's own take-over case in
  cl-dClosedLoop-0508. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, flow-steps:438 and :452;
  the difference from the clause's word is deviation 131. widens: none · relaxes: none
- **F3 — How is the patch filed?** TOOL-dWellOiledMachine-27 S1 offers `mailbox` and `cadence`, S3 says a
  cadence receipt never ratifies, and S4 refuses a placement for one, so `deploy.core` cannot place a
  build as specced (scout A disagreement 10). Options: (a) a new origin `landing`, ratified through
  the originating build's mandate; (b) a `cadence` receipt and an owner breakpoint for every red. (b)
  fails "before that build closes" on an owner's silence. RESOLVED (agent, 2026-10-30, delegated): (a),
  rung 3, pin C9. Ask for dWellOiledMachine, filed by the main loop: TOOL-dWellOiledMachine-27 S1, S3
  and S4 admit `--origin landing --build <slug> --sha <sha>`, whose receipt ratifies when `<build>`'s
  mandate is on the default branch and `<sha>` is that build's landing; accept `python intake.py
  ratifies <key>` prints `ratifies · landing` on a fixture landing's red and a `landing` receipt
  naming a SHA no landing record names does not ratify. widens: none · relaxes: none
- **F4 — How does an exception join its landing?** `core.exceptions`' record carries `Principle`,
  `Excuses`, `Reason`, `Expires` and `Caused-by`, none a SHA (scout A disagreement 11). Options: (a)
  `--excuses landing:<sha>`, the `<part>` the door already takes, read through `core.py exceptions` so
  the key's value is honoured; (b) a new `Landed` field, a change to PLAY-dOrderedCharter-7 S8. (a)
  needs no parent change. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, reuse of a seam, the
  tie-break. widens: none · relaxes: none
- **F5 — Is an exception the owner's alone?** flow-steps:446 says "the owner's alone"; the clause says
  "an exception under `core.exceptions`", whose default `any-session-recorded` admits any session's
  record. Options: (a) the clause and the key's value; (b) require the owner whatever the value. (b)
  overrides a policy key. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, v2's clause governs a
  design record; the flow-steps sentence stands for the owner item it describes. A session can
  therefore excuse its own red under the default, which `owner-only-expiring` closes. widens: none · relaxes: none
- **F6 — What is "the patch build's" green?** Options: (a) a `GREEN` record at a SHA containing the
  landed one, whose landing record's `builds` hold a build whose claim's `content-key` equals the
  `patch-key` (`read_claim_body`, TOOL-dPlacedRequest-21); (b) any green descendant. (b) closes a
  red build on an unrelated landing, looser than the clause. RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 1, the clause's "that build's patch". widens: none · relaxes: none
- **F7 — Must an undeclared key's red bind the next push?** Options: (a) leave the hook, the record
  and the patch being what the clause asks; (b) have the hook read `refs/gov/bar-red` undeclared, a
  bounded remote read on every push of every adopter. RESOLVED (agent, 2026-10-30, delegated): (a),
  rung 3, (b) widens a boundary no clause names. widens: none · relaxes: none
- **F8 — Which ceiling bounds a running bar?** Options: (a) `runtime.act-ceiling`, flow-steps:438's
  "the act's ceiling"; (b) `flow.wait-ceiling`, which `deploy.close` uses. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 1, flow-steps:438. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 13, `gap-deploy-02`, `gap-deploy-10`,
  flow-steps:438 and :451-472, pins C6 and C9, shared interface I9, and scout A's row and disagreements
  3, 4, 6, 10 and 11.

## 10. Reuse audit

The seams extended are `run_post_merge` (`tools/push-main.sh:427`) for the start, and
`write_post_merge_record` (`tools/run-gates/post-merge.sh:55`), `run_bar` (`:305`) and the publication
(`:374-397`) for the verdict. `python tools/codebase-map/reuse_lookup.py "read the post-merge bar verdict
for a landed sha and record it apart from its publication"` returned name-stem neighbours (`merge`,
`records`, `read_conf_key`), so the shipped seams are the ones scout A read. Scout A's row holds at
`5d1c82ac`, with one correction from the brief: `read_remote_verdict` is TOOL-dWitnessedBar-6 S6 and
S7 is the held reader, though both live in `remote_verdict.py`. The recall probe's hits were this
build's scout records; neither disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does a post-merge red reach a landing and who files the patch" --terms "post-merge bar-red GATE_POST_MERGE verdict publication per-sha record patch intake default-branch-red"`
