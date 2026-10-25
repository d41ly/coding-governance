# TOOL-dWitnessedBar-6 — the verdict backends registered under `verdict`: the local hook, the peer-node verifier and the `remote-ci` slot with its witness rule and pin

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 28 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0344@5cea08b4 whole
**Carries:** node:policy-key.verdict
**Carries:** node:policy-key.verdict.remote.trust
**Carries:** node:policy-key.verdict.remote.pin-scope
**Carries:** node:policy-key.verdict.remote.pin

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

The binding verdict is one node's bypassable hook, and remote CI blocks nothing
(`.github/workflows/remote-ci.yml:10-12`, gap-test-02). A remote verdict also certifies itself: its
workflow sits in the tree it judges, and nothing grades the workflow's text (gap-test-11). The one
live outside reader, `read_held_reds`, sits inside the unattended kit with no registration
(`tools/unattended/unattended.sh:10109`, gap-test-13). This unit declares the verdict backends as a
registry under the policy key `verdict`: `local-hook` and `peer-node`, both core, and `remote-ci`, the
slot the integrations expansion fills (R5.2, "Local + peer node", remote CI a slot). A remote verdict
stands as a witness only under the rule the clause states, and the held-CI reader moves into the slot
as its reader.

## 2. Scope (IN)

- **S1** — The registry: `[[verdict_backend]]` rows in a kit descriptor, read across every
  `tools/*/kit.toml` by `read_backends(tool_root)` in `tools/run-gates/verdict_backends.py`, each row
  `name`, `reader` (`<module>:<function>` under its kit), `off_node` (boolean) and `owner`. The
  run-gates kit declares three rows in `tools/run-gates/kit.toml`: `local-hook` (off_node false),
  `peer-node` (true) and `remote-ci` (true). A name declared twice is refused naming both
  descriptors. Observed by AC1.
- **S2** — The key `verdict`, read through dGroundRules' reader, `python tools/policy/policy.py get
  verdict` (TOOL-dGroundRules-2 S7), default `local-hook` (v2:1270) until that reader lands.
  `check_backend(name, backends)` refuses a value no row declares, naming the value and the declared
  names; the lander and `verdict_backends.py read` call it before any read. Observed by AC2.
- **S3** — One read for every backend, `read_verdict(backend, sha, tree)` returning
  `Verdict(state, witness, why)`, `state` one of `GREEN`, `RED`, `NONE`, `HELD` and `DEAD PROBE`, and
  the CLI `python verdict_backends.py read --backend <name> --sha <sha>`, printing one line
  `verdict: <backend> · <state> · <sha8> · <why>`. Only `GREEN` stands; `NONE`, `HELD` and
  `DEAD PROBE` are no verdict and never green. Observed by AC2 and AC5.
- **S4** — `local-hook`'s reader reads the runner-written per-tree verdict
  `<common-dir>/gate-verdict/<tree hash>` (shared interface I8, unit 4's) for the SHA's tree, and stands
  when its `verdict` line reads `GREEN`. Observed by AC3.
- **S5** — `peer-node`: the verb `python verdict_backends.py verify-peer [--remote <name>]`, run on
  a second fleet node, lists `refs/gov/candidate/*` on the remote with one bounded `git ls-remote`,
  fetches each candidate, runs the bar on it in a detached worktree of the node's own clone, and pushes
  an annotated tag `refs/gov/verdict/<sha>` whose message carries `verdict`, `tree`, `node` and
  `run_id` lines in I8's `<key>TAB<value>` grammar. The reader fetches that ref and stands only when
  the tag points at the SHA, `tree` equals the SHA's tree, `verdict` reads `GREEN`, and `node` is not
  the reading node's tag. Observed by AC4.
- **S6** — `remote-ci`'s reader, `read_remote_verdict` in `tools/run-gates/remote_verdict.py`, by
  integrations' witness rule (layer-expansions.md:334-341): **key**, the run's `head_sha` is the SHA
  judged and that SHA's `^{tree}` is the verdict's tree; **writer**, the run's check suite app slug
  `github-actions`, its `path` the row's declared workflow `.github/workflows/remote-ci.yml`, its
  `event` `push`, and the declared job `bar`; **liveness**, the job's declared bar step concluded
  `success` and not `skipped`; **source**, each file `verdict.remote.pin-scope` names has a blob at
  `head_sha` equal to its entry in `verdict.remote.pin`, as `verdict.remote.trust` says (S8); **a
  failed read**, `DEAD PROBE`. Observed by AC5 and AC6.
- **S7** — The held-CI reader moved: `read_held_reds`' program, unchanged in behaviour, becomes
  `read_held_runs(anchor_url, workflow)` in `tools/run-gates/remote_verdict.py`, beside S6's reader and
  sharing its one bounded GET (`fetch_api`: no redirect, no credential, 30 s, 4 MiB); its CLI
  `python remote_verdict.py held <anchor URL> <workflow file>` prints the rows and liveness line the
  bash function printed. `write_held_asks` (`unattended.sh:10184`) reaches it through
  `resolve_kit_dir("run-gates", "remote_verdict.py", here)` and files each red through `write_leg_ask`
  (unit 8's, shared interface I13). The bash function leaves `unattended.sh`. Observed by AC7.
  **Readers:**
  by name: `tools/unattended/unattended.sh` (the definition at `:10109` and the call at `:10207`),
  `tools/unattended/unattended.test.sh` (the stub at `:14325` and the `unset -f` at `:14357`).
  by value: `write_held_asks`, which reads its `held` rows and its liveness line; the stub's
  `h9-calls` file, which the suite counts.
- **S8** — The trust values: under `pinned-workflow` (default, v2:1280) a pinned file that differs
  reads `HELD` and an owner item asks to re-pin or to refuse; under `owner-reviews-workflow-change`
  the owner item opens at the first differing read and the read stays `HELD` until the owner re-pins;
  under `app-only` the source check is skipped and a passing read is `GREEN` with witness `claimed`,
  never `witnessed`. The owner item: the unattended driver's gates-green term, the site that calls
  `write_held_asks` (`unattended.sh:11287`), reads the slot under `verdict = remote-ci` and files a
  pin `HELD` through `write_leg_ask <slug> 'remote-ci pin' ...` (unit 8's), reused while open;
  outside a run the lander's refusal line names it. Observed by AC6.
- **S9** — The pin: `verdict.remote.pin` is a table of `<path> = "<blob id>"`, written only by the
  owner's guarded command, `python tools/loop/policy_edit.py set verdict.remote.pin <value>`
  (TOOL-dDeclaredLoop-2 S4, its terminal proof). `tools/loop/guard.py --staged` refuses a staged
  change to that key without the command's `Gov-Policy:` trailer whatever `policy-file.guard` allows,
  through one constant `OWNER_ONLY_KEYS`. `python remote_verdict.py pin` prints, and never writes,
  the value the owner would set: the blob of each file `verdict.remote.pin-scope` names at HEAD,
  `workflow` naming `.github/workflows/remote-ci.yml` and `dispatch-closure` adding
  `tools/run-gates/run-gates.sh`, `tools/gate-legs.json` and `.githooks/gate-env.sh`. With no pin
  set, `remote-ci` reads `HELD` with `why` `no pin`. Observed by AC8.
- **S10** — The lander: `tools/push-main.sh` reads `verdict` before the landing push. Under
  `local-hook` it lands as today. Under `peer-node` it publishes `<sha>:refs/gov/candidate/<sha>` and
  lands only when `read_verdict` is `GREEN` for the SHA it is about to push, otherwise exits 1 naming
  the state; under `remote-ci` it reads the slot the same way. An unregistered value refuses before any
  push. Observed by AC2 and AC9.
- **S11** — `tools/run-gates/README.md` states the registry, the three rows, the five states and the
  witness rule; `help/` gains the page `help/verdict-backends.md`, linked from `help/README.md`.
  Observed by AC10.

## 3. Non-goals (OUT)

- The integrations expansion: its kit, its header factory, the `remote-verdict` record kind and the
  candidate publication remote CI would need to run before a landing (GitHub runs a push workflow
  for branches and tags, never `refs/gov/*`). This unit fills the slot's reader and leaves its re-home
  to that expansion.
- `GATE_POST_MERGE=ci` and `deploy.core` reading the remote verdict after the landing: dShippedRelease.
- Making a remote job a required check: a repository setting, the owner's (`remote-ci.yml:11`).
- Repairing the hosted bar, red since 2026-10-13 (gap-test-12): the reader reports it `RED`.
- Recording a bypass under `hooks.bypass`: TOOL-dWitnessedBar-2, which reads this registry.
- A scheduler for `verify-peer`: the peer's operator runs it, by hand or from its own cadence.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-4` — `gate-verdict`, the runner-written per-tree verdict `<common-dir>/gate-verdict/<tree hash>` that `local-hook`'s reader reads and `verify-peer` publishes
- **consumes-from** `TOOL-dWitnessedBar-8` — `write_leg_ask`, through which the moved held reader's reds and the pin's owner item are filed, keyed by name and reused while open
- **hands-off** `TOOL-dWitnessedBar-2` — `verdict`, the registry's `off_node` field and `read_verdict`, which `hooks.bypass = refused` needs as its off-node witness
- **hands-off** `TOOL-dWitnessedBar-43` — `read_peer_verdict` and `verify-peer`, which unit 43 binds to the source pin and to a tag signed by a registered node key (id 63)
- **hands-off** `TOOL-dWitnessedBar-56` — `read_local_verdict`, to which the verdict-boundary minors batch adds the hook's reuse-pair and selection refusals (ids 15, 33)

## 4. Design

### The registry

```toml
# tools/run-gates/kit.toml
[[verdict_backend]]
name = "local-hook"
reader = "verdict_backends:read_local_verdict"
off_node = false
owner = "dWitnessedBar"

[[verdict_backend]]
name = "peer-node"
reader = "verdict_backends:read_peer_verdict"
off_node = true
owner = "dWitnessedBar"

[[verdict_backend]]
name = "remote-ci"
reader = "remote_verdict:read_remote_verdict"
off_node = true
owner = "dWitnessedBar"
workflow = ".github/workflows/remote-ci.yml"
job = "bar"
step = "the merge bar, every leg guard ignored, walled inside the job limit"
```

The descriptor table is the precedent PLAY-dOrderedCharter-6 S1 set with `[[drive]]` and
TOOL-dDeclaredLoop-6 S3 with `[[command]]`: a row govkit's install does not read, read across
descriptors by its own reader. An expansion registers a backend by declaring a row in its own kit.

### The remote read

```
GET /repos/<o>/<r>/actions/workflows/remote-ci.yml/runs?head_sha=<sha>&event=push&per_page=10
GET /repos/<o>/<r>/actions/runs/<id>/jobs?per_page=100
GET /repos/<o>/<r>/check-suites/<check_suite_id>
```

The owner and repository come from the anchor URL, as `read_held_reds` parses them today
(`unattended.sh:10126`). Every request goes through `fetch_api`, the same bounded GET the held reader
uses; a non-200, an oversize body or a non-JSON body is `DEAD PROBE`. The pinned blobs at `head_sha`
are read from the local object database (`git rev-parse <sha>:<path>`); a SHA the clone lacks is
`DEAD PROBE`, never fetched implicitly.

| Plant | Fixture response | State |
|---|---|---|
| `remote-green` | push run of the declared workflow, `bar` job's step `success`, pinned blob equal | `GREEN` |
| `swapped-workflow` | the same, with `remote-ci.yml` at `head_sha` differing from the pin | `HELD` |
| `other-path` | a run whose `path` is another workflow file | `NONE` |
| `step-skipped` | the bar step concluded `skipped` | `NONE` |
| `api-404` | the runs listing answers 404 | `DEAD PROBE` |
| `unregistered` | `verdict = "ci-cloud"` in the fixture policy | refused, exit 2 |

`--responses <dir>` points `fetch_api` at canned JSON files named by request path, an arm seam and
not a conf key, as `GATE_VERDICT_FAULT` is one for the runner (`run-gates.sh:3733`, `:3742`).

### Inventory

Minted: the descriptor table `[[verdict_backend]]` and its keys; `tools/run-gates/verdict_backends.py`
with `read_backends`, `check_backend`, `read_verdict`, `read_local_verdict`, `read_peer_verdict`
and the verbs `read`, `verify-peer`, `--fixture`, `--plant`; `tools/run-gates/remote_verdict.py` with
`read_remote_verdict`, `read_held_runs`, `fetch_api`
and the verbs `read`, `held` and `pin` with the flag `--responses`; the
refs `refs/gov/candidate/<sha>` and `refs/gov/verdict/<sha>`; `OWNER_ONLY_KEYS`; the states `HELD`
and `NONE`; the witness word `claimed`. Naming cells: each function is asked of `python
tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Under the default `local-hook` the landing path is unchanged. `HELD_CI_WORKFLOW`
(`.unattended.conf:221`) keeps its meaning and its one reader, `write_held_asks`.

### Rollout

Live at landing, dark by default: `verdict` defaults to `local-hook`, and `remote-ci` reads `HELD`
until the owner pins. The run-gates and unattended kits' versions move.

### Files touched (estimate)

- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/remote_verdict.py`
- `tools/run-gates/kit.toml`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.sh` (the version line only)
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/loop/guard.py`
- `help/verdict-backends.md`
- `help/README.md`

### Alternatives rejected

- **A registry file of its own.** A backend's reader lives in its kit, so its row lives in that kit's
  descriptor, and an expansion registers without editing a core file.
- **Peer verdicts in a shared branch file.** A ref per SHA is written once by the peer, and
  `refs/gov/bar-red` is the precedent (`tools/run-gates/post-merge.sh:13`).

## 5. Production-readiness checklist

- security — a new outbound read: https to `api.github.com` only, no redirect, no credential sent or
  read, 30 s and 4 MiB bounds, all kept from `read_held_reds`; the pin is owner-only through the
  terminal proof and a guard constant; a peer verdict counts only from another node's tag and for the
  SHA's own tree. The peer pushes refs under `refs/gov/` only, with the node's own push grant.
- perf / scale — at most three GETs per remote read; one `ls-remote` and one fetch per peer read; a
  `verify-peer` pass runs one bar per candidate.
- error / empty / loading states — every failed read is `DEAD PROBE` and names why; an empty pin
  reads `HELD` with `no pin`; an unregistered value refuses before any push.
- observability — one `verdict:` line per read, and the lander's line naming the state it refused on.
- risks — under `peer-node` a landing waits on a peer that may never run; the lander exits 1 and
  says so rather than polling, and `flow.wait-ceiling` governs the owner item the loop raises.
- testing — AC1 to AC10 by fixture and probe; the arms in §7.
- migration — none under the default value, per §4.
- user docs — `help/verdict-backends.md` (S11).

## 6. Acceptance criteria

- **AC1** — When `python verdict_backends.py --fixture --plant registry` runs in `tools/run-gates/`, it
  prints the three declared names with their `off_node` values, and with a second descriptor declaring
  `local-hook` again it exits 2 naming both descriptors.
  Red when: a duplicate row overrides the first silently.
- **AC2** — When `python verdict_backends.py --fixture --plant unregistered` runs, `read` and the
  fixture lander each exit non-zero naming `ci-cloud` and the three declared names, and no push is made.
  Red when: an unregistered value falls back to `local-hook`.
- **AC3** — When `python verdict_backends.py --fixture --plant local-green` runs over a fixture common
  dir holding a `gate-verdict/<tree hash>` file reading `verdict GREEN`, `read --backend local-hook`
  prints `GREEN`; with the file reading `RED` it prints `RED`, and with no file `NONE`.
  Red when: a missing per-tree verdict reads as green.
- **AC4** — When `python verdict_backends.py --fixture --plant peer` runs, a fixture remote holding
  `refs/gov/verdict/<sha>` from node `b` reads `GREEN` on node `a`, the same tag from node `a` reads
  `NONE`, and a tag whose `tree` line differs reads `NONE`.
  Red when: a node's own verdict, or one for another tree, stands as off-node.
- **AC5** — When `python remote_verdict.py read --responses <dir> --sha <sha>` runs over the
  `remote-green` fixture, it prints `GREEN`; over `other-path` and `step-skipped`, `NONE`; over
  `api-404`, `DEAD PROBE`.
  Red when: any of the writer, liveness or failed-read fields is not checked.
- **AC6** — When the same command runs over the `swapped-workflow` fixture, it prints `HELD` naming
  `.github/workflows/remote-ci.yml` under `pinned-workflow`, and `GREEN` with witness `claimed` under
  `app-only`: the clause's swapped workflow seen red.
  Red when: a workflow that differs from the pin stands as witnessed.
- **AC7** — When `python remote_verdict.py held --responses <dir> https://github.com/o/r remote-ci.yml`
  runs over a fixture of two held jobs, one `failure`, it prints two `held` rows and the liveness line
  `held reader: run <id> at <sha8> · 2 held job(s) read · 1 red`; and
  `git grep -n 'read_held_reds()' tools/unattended` prints nothing.
  Red when: the moved reader's rows differ from the bash function's, or the function stays.
- **AC8** — When `python remote_verdict.py pin` runs at HEAD with `verdict.remote.pin-scope` at
  `dispatch-closure`, it prints four `<path> = "<blob>"` lines whose blobs equal
  `git rev-parse HEAD:<path>`, and `python guard.py --staged`, run in the loop kit's directory over a fixture
  staging a change to `verdict.remote.pin` with no `Gov-Policy:` trailer, exits 1 naming the key.
  Red when: the pin helper writes the policy file, or the guard admits an agent's pin.
- **AC9** — When the fixture lander `push-main.sh` runs in the fixture repository of
  `verdict_backends.py --fixture --plant lander-peer` under `verdict = "peer-node"` with no peer
  verdict, it publishes `refs/gov/candidate/<sha>` and exits 1 naming `NONE`.
  Red when: the lander lands on its own hook's verdict under an off-node backend.
  fixture: the fixture repository and its bare remote are built by the plant in the system temp dir.
- **AC10** — When `grep -n 'verdict-backends' help/README.md` runs, it names the page, and
  `grep -c 'verdict_backend' tools/run-gates/README.md` prints at least 1.
  Red when: the registry ships with no user page.

## 7. Gates

`govkit selfcheck` · `run-gates wiring` · `push-main self-test` · `unattended kit gate` · `remote literals (kit code names no remote)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant of §4 run through `verdict_backends.py --fixture` and `remote_verdict.py --responses`, staged red by removing the source check from `read_remote_verdict` and the off-node test from `read_peer_verdict` · none
New arm: tools/push-main.test.sh · covers AC9 · the `lander-peer` fixture under `peer-node`, staged red by skipping `read_verdict` before the push · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · the h9 arm re-pointed at the moved reader's `held` verb, staged red by restoring the bash stub's rows · none

## 8. Open questions

- **F1 — Where is the registry declared?** Options: (a) `[[verdict_backend]]` rows in each kit's
  descriptor, read across descriptors; (b) one core file listing every backend; (c) a `case` in the
  lander. (b) makes an expansion edit a core file to register, which P28 as EX-1 amended forbids;
  (c) is a hand-typed list. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by reuse
  of the descriptor-table seam `[[command]]` and `[[drive]]` set. widens: none · relaxes: none
- **F2 — Is the peer-node verifier built here or only registered?** Options: (a) registered and built:
  the reader and `verify-peer`; (b) a registered row whose reader reads `NONE` until a later build.
  layer-expansions' `[core-points]` row says `local-hook` and `peer-node` are "both core and built by
  dWitnessedBar", and R5.2's answer is "Local + peer node". RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 1. The two pushes it adds, `refs/gov/verdict/<sha>` and `refs/gov/candidate/<sha>`, sit
  under `refs/gov/` as `post-merge.sh` already pushes `refs/gov/bar-red`, and this Tier-2 unit prices
  them in §5. widens: none · relaxes: none
- **F3 — What does a remote-ci landing read before CI can run on a candidate?** GitHub runs a push
  workflow for branches and tags only, so no workflow runs on `refs/gov/candidate/<sha>`. Options:
  (a) the slot reads by SHA and the integrations expansion supplies the candidate publication; (b)
  this unit publishes candidates as branches and edits `remote-ci.yml` to run on them. (b) builds the
  expansion's surface and changes the pinned workflow this unit's pin protects. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 1, the clause's "a `remote-ci` slot the integrations expansion
  fills". widens: none · relaxes: none
- **F4 — How is "the platform's own app" read?** Options: (a) the run's check suite `app.slug` is
  `github-actions`; (b) the run's `actor`. (b) names the pusher, not the writer. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 2 by research-integrations-b's witness table, "Writer:
  `app.slug=github-actions`". widens: none · relaxes: none
- **F5 — Is a new user-facing surface and a guard constant within this build's authority?** RESOLVED
  (agent, 2026-10-25, delegated): yes, rung 3 with veto 2 lifted by the README's `may:` grant, because
  the carried clause names the backends, the pin and its keys. grants: PLAY-dClosedLoop-3 the
  `[[verdict_backend]]` descriptor table, the `verify-peer` verb, the `refs/gov/candidate/<sha>` and
  `refs/gov/verdict/<sha>` refs and the guard's `OWNER_ONLY_KEYS`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 6, the brief's shared interfaces I8 and
  I13 and owned-node table, scout A's row for cl-0344, layer-expansions' witness rule and the
  design rounds' R5.2, at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-43, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams extended: the anonymous bounded GitHub read inside `read_held_reds`
(`tools/unattended/unattended.sh:10109-10182`), moved whole and given a second caller; its caller
`write_held_asks` (`:10184`); the `refs/gov/` publication precedent of `tools/run-gates/post-merge.sh`
and its reader `read_post_merge_red` (`.githooks/pre-push:1922`); the guarded policy writer
`policy_edit.py set` and the loop guard (TOOL-dDeclaredLoop-2 S1, S4), both specced and built by the
chain before this build. `python tools/codebase-map/reuse_lookup.py "read a remote CI verdict for a
commit sha from the GitHub API"` ranked generic stems (`read`, `git`, `run_git`) and missed
`read_held_reds`, whose body is a Python program inside a bash function, outside the symbol tier; scout
A found it by reading. No registry of verdict backends exists at base: no `verdict_backend` token in
the tree.

Recall terms used: `python tools/memory-recall/query.py "when does a remote CI verdict stand as a witness for a landing and what backends exist" --terms "verdict backend remote-ci peer-node local-hook head_sha workflow pin trust held reader registry"`
