# TOOL-dWellOiledMachine-56 — the act's harness and credential resolved per role through Roles' resolver, a harness row for how it reads the credential, and the launch pinned out of bare mode

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 30 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0334@4fe16106 whole
**Carries:** node:policy-key.runtime.act-harness
**Carries:** node:policy-key.runtime.act-auth
**Carries:** node:policy-key.roles.harness.<role>
**Carries:** node:policy-key.roles.auth.<role>

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

The harness and its credential are set once for the repository, so a head or a judge role cannot run
on another subscription or key without drawing on the workers' plan, and a headless act loses the
subscription login once `--bare` becomes `-p`'s default, since bare mode reads neither the OAuth login
nor the setup token (gap-rt-42, gap-rt-43). This unit resolves `runtime.act-harness` and
`runtime.act-auth` per role through Roles' resolver, as `roles.harness.<role>` and
`roles.auth.<role>`, keys each role's stored credential to that role alone, records on each harness
adapter how it reads a credential, and pins the act launch out of bare mode.

## 2. Scope (IN)

- **S1** — The harness per role, `resolve_role_harness(slot, root)` in `tools/roles/roles_lib.py`:
  `read_policy_setting(f"roles.harness.{slot}", root)` (TOOL-dBoundRoles-21 S1), else
  `read_policy_setting("runtime.act-harness", root)`, else the catalogue default `claude-code`
  (`tools/policy/catalogue.toml:1602-1605`), as a list in the order written. A name with no adapter
  table under `tools/runtime/harnesses/` (TOOL-dWellOiledMachine-14 S1) refuses with `RolesError`
  naming the key and the name. Observed by AC1.
- **S2** — The credential classes per role, `resolve_role_auth(slot, root)` in `roles_lib.py`:
  `roles.auth.<slot>`, else `runtime.act-auth`, else its default `setup-token, oauth-shared`
  (`catalogue.toml:1607-1611`). The `roles.auth.<role>` row (`:326-331`) gains `last = ["api-key"]`,
  so the policy schema refuses api-key before another entry there as TOOL-dWellOiledMachine-37 S6
  refuses it on `runtime.act-auth`. Observed by AC2.
- **S3** — The credential keyed to its role, `derive_credential_target(slot, cls, own)` in
  `roles_lib.py`: for `setup-token` and `api-key`, the secret reference `act_<cls>_<slot>` when the
  role sets its own `roles.auth.<slot>` in the policy file (`own`, the resolution's source `file`), and
  the shared `act_<cls>` otherwise, each with `-` folded to `_`; `oauth-shared` has no reference, the
  harness's own login being one per node. `check_credential_role(slot, ref)` refuses a reference keyed
  to another role's slot, `launch — refused · credential-role · <ref> is not <slot>'s`. Observed by AC3.
- **S4** — The launch per role: `launch_act` (TOOL-dWellOiledMachine-1 S2) reads the act's role from
  `work_order["role"]`, takes the first harness S1 returns, and hands TOOL-dWellOiledMachine-37's
  `run_with_credentials` the classes S2 returns with the references S3 derives, each checked by
  `check_credential_role` before any store is read. Observed by AC1, AC3.
- **S5** — How each adapter reads a credential, the `credential-read` row of the capability table
  (I7, a name `CAPABILITY_NAMES` already holds): `claude-code.toml` records
  `setup-token=env:CLAUDE_CODE_OAUTH_TOKEN; oauth-shared=harness-store; api-key=env:ANTHROPIC_API_KEY`,
  written by this unit's live arm with the binary version it launched; `codex.toml` stays
  `unmeasured`. A class whose `credential-read` part is unmeasured on the act's adapter is skipped,
  printing `credential — <class> · skipped: credential-read unmeasured`. Observed by AC4.
- **S6** — The launch pinned out of bare mode, `derive_bare_pin(adapter, version)` in
  `tools/runtime/launch.py`: the adapter's `bare-default` row, a capability name this unit adds to
  `CAPABILITY_NAMES`, reads `no` when bare mode is opt-in, `yes:<flag>` when it is `-p`'s default and
  `<flag>` turns it off, and `yes` when nothing does. `launch_act` adds nothing for `no`, appends
  `<flag>` for `yes:<flag>`, and refuses `launch — refused · bare-default` for `yes` and for
  `unmeasured`. It also refuses an environment it built that carries a non-empty `CLAUDE_CODE_SIMPLE`.
  The claude-code row is seeded `no` from `claude --help` on CLI 2.1.292 (node a, 2026-10-26), which
  lists `--bare` as an opt-in flag. Observed by AC5.
- **S7** — The fixture, `python roles_lib.py --fixture --plant <case>` for S1 to S3 and
  `python launch.py --fixture --plant <case>` for S4 to S6, each over a planted policy file and a
  planted adapter table, the second with a stub harness recording its argv and environment. Observed
  by AC1 to AC5.
- **S8** — The documentation: `help/runtime.md` gains the per-role harness and credential, the
  `credential-read` and `bare-default` rows and how an owner gives a judge role its own setup token;
  `help/roles.md` gains the two `roles.*.<role>` keys. Observed by AC6.

## 3. Non-goals (OUT)

- Picking which node runs a role's work by the harnesses it has: TOOL-dWellOiledMachine-54, which reads
  `resolve_role_harness`.
- The credential order, the store reader and the transient class: TOOL-dWellOiledMachine-37 and -17.
- A per-role OAuth login: `oauth-shared` is the node's one harness login; a role's own subscription
  comes by its own setup token.
- `roles.model.<role>.<harness>`: TOOL-dBoundRoles-21 S5's `resolve_role_model`.
- Measuring Codex's rows: TOOL-dWellOiledMachine-36.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch_act`, which takes the per-role harness and credential and gains the bare pin
- **consumes-from** `TOOL-dWellOiledMachine-37` — `run_with_credentials`, which S4 calls with a role's classes and references, and the `last` field S2 puts on `roles.auth.<role>`
- **consumes-from** `TOOL-dWellOiledMachine-14` — `[[capability]]`, the table holding S5's `credential-read` row and S6's `bare-default` row, read through `read_capability`
- **hands-off** `TOOL-dWellOiledMachine-54` — `resolve_role_harness`, the harnesses a role's work needs, which the pick and the preset check read
- **consumes-from** external — TOOL-dBoundRoles-21's `read_policy_setting` and `RolesError`, the one policy read of the roles kit

## 4. Design

### Evidence

- The four keys have catalogue rows and no reader: `roles.harness.<role>` and `roles.auth.<role>` at
  `tools/policy/catalogue.toml:319-331`, derived defaults naming the two runtime keys, and
  `runtime.act-harness` and `runtime.act-auth` at `:1601-1611`; `git grep -n "roles.harness\."
  -- tools` finds only the catalogue and its shrink-only list `tools/policy/unsummarised-keys.txt`.
- `claude --help` on CLI 2.1.292 says `--bare` makes "Anthropic auth … strictly ANTHROPIC_API_KEY or
  apiKeyHelper via --settings (OAuth and keychain are never read)" and sets `CLAUDE_CODE_SIMPLE=1`;
  this session's own environment carries `CLAUDE_CODE_SIMPLE`, which TOOL-dWellOiledMachine-37's
  allowlist keeps from an act.
- TOOL-dBoundRoles-21 S5 resolves the model per role and harness the same way, a key then a fallback,
  through `read_policy_setting`, so the harness and credential follow its shape and need no second
  policy reader.

### Resolution, for a judge role

| Key read | Planted value | Resolved |
|---|---|---|
| `roles.harness.judge` | unset | `runtime.act-harness`: `claude-code` |
| `roles.auth.judge` | `["setup-token"]` | `setup-token`, reference `act_setup_token_judge` |
| `roles.auth.builder` | unset | `runtime.act-auth`: `setup-token, oauth-shared`, reference `act_setup_token` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_role_harness`, `resolve_role_auth` | Python functions | `resolve`, OK |
| `derive_credential_target` | Python function | `derive`, OK |
| `check_credential_role` | Python function | `check`, OK |
| `derive_bare_pin` | Python function | `derive`, OK |
| `bare-default` | capability name | none |
| `act_<class>`, `act_<class>_<slot>` | secret reference names | none |

### Files touched (estimate)

- `tools/roles/roles_lib.py`: S1 to S3 and the fixture
- `tools/runtime/launch.py`: the per-role call and `derive_bare_pin`
- `tools/runtime/harness.py`: `bare-default` in `CAPABILITY_NAMES`
- `tools/runtime/harnesses/claude-code.toml`, `tools/runtime/harnesses/codex.toml`: the two rows
- `tools/policy/catalogue.toml`: `last` on `roles.auth.<role>`
- `help/runtime.md`, `help/roles.md`

### Alternatives rejected

- **A credential per role under `CLAUDE_CONFIG_DIR`.** A separate harness login per role would need the
  harness to read a second config home, a capability no row records; a role's own setup token gives it
  its own subscription with the store gov already reads.
- **The harness picked in `launch_act` from `runtime.act-harness` alone.** The owner's P40 resolves it
  per role so a judge or a head never draws on the workers' plan.

## 5. Production-readiness checklist

- security — a role's stored credential is keyed to its slot and refused for any other; api-key stays
  last by schema; bare mode, which reads no subscription login, cannot be launched.
- perf / scale — two policy reads per launch, through the run's one resolution.
- error / empty / loading states — an unknown harness, an unmeasured bare row and an unmeasured
  credential read each answer by name.
- observability — each refusal names the role, the key or the reference; each skipped class prints one
  `credential —` line.
- risks — a binary whose bare default changes reads its old row until re-measured; the row carries
  `binary-version`, and a newer binary with no row reads `unmeasured`, which refuses.
- testing — the fixture cases under AC1 to AC5 and the arms in §7.
- migration — none: with no `roles.*` key set every role resolves to today's `runtime.*` values and the
  shared references.
- user docs — `help/runtime.md` and `help/roles.md`.

## 6. Acceptance criteria

- **AC1** — When `python roles_lib.py --fixture --plant harness` sets `roles.harness.judge = ["codex",
  "claude-code"]`, `resolve_role_harness("judge")` returns both in order and the builder role returns
  `claude-code`; a planted `roles.harness.judge = ["nohost"]` raises `RolesError` naming `nohost`.
  Red when: a role reads another role's harness, or an unregistered name is returned.
- **AC2** — When `python policy.py check` reads a planted `roles.auth.judge = ["api-key",
  "setup-token"]`, it refuses with `"api-key" must be last`; `["setup-token"]` is admitted.
  Red when: api-key before another entry is admitted on the role key.
- **AC3** — When `--plant credential-role` resolves the judge role with its own `roles.auth.judge`,
  the reference is `act_setup_token_judge`; with a resolver planted to hand the judge
  `act_setup_token_builder`, `python launch.py --fixture --plant credential-role` prints
  `launch — refused · credential-role` and the stub never starts.
  Red when: a role resolving another role's credential launches.
- **AC4** — When `python harness.py capability claude-code credential-read` runs, it prints the
  three-part value with a binary version and date; on the codex table it prints `unmeasured`, and a
  launch whose role resolves `setup-token` on codex prints `skipped: credential-read unmeasured`.
  Red when: an unmeasured row is read as a way to pass a credential.
- **AC5** — When `python launch.py --fixture --plant bare` runs with the adapter's `bare-default`
  planted `yes`, it prints `launch — refused · bare-default`; planted `yes:--no-bare`, the stub's argv
  ends with `--no-bare`; seeded `no`, the argv carries neither `--bare` nor `--no-bare`; and a built
  environment carrying `CLAUDE_CODE_SIMPLE=1` is refused.
  Red when: a launch reaches the stub in bare mode.
- **AC6** — When `grep -n "roles.auth\|bare-default" runtime.md help/roles.md` runs over the two
  pages, each names its terms.
  Red when: either page omits them.

## 7. Gates

`policy fixtures` · `policy check` · `roles catalogue` · `roles render selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/roles/roles_lib.py · covers AC1 AC3 · a role resolved through another role's key and reference, staged against a resolver reading only the runtime keys · none
New arm: tools/runtime/launch.py · covers AC4 AC5 · an unmeasured credential read and each bare row, staged against a `launch_act` with `derive_bare_pin` returning nothing · none

## 8. Open questions

- **F1 — Is an unmeasured `bare-default` row a launch or a refusal?** (a) A refusal: a binary nobody
  measured may launch bare and lose the subscription login; (b) a launch, bare assumed opt-in. (b) is
  the failure gap-rt-43 names, silent until the login is lost. Rung 3, deny by default, with the
  claude-code row seeded from this node's measurement so today's launches pass. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — How does a role get its own subscription?** (a) Its own setup token, stored under
  `act_setup_token_<slot>`; (b) its own harness login under a per-role config home. (b) rests on a
  capability no row records. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seam extended is Roles' resolver, TOOL-dBoundRoles-21's `read_policy_setting` and the
key-then-fallback shape of its `resolve_role_model` (S5), which the harness and credential follow;
the launch is I2's `launch_act`, the credential order TOOL-dWellOiledMachine-37's
`run_with_credentials`, and the rows land in TOOL-dWellOiledMachine-14's capability table. The probe
`python tools/codebase-map/reuse_lookup.py "resolve a per-role setting through the policy reader with
a fallback"` ranked `resolve` (`tools/policy/policy.py`), `resolve_kit_dir`, `read_conf` and
`read_conf_key` by name stem; `resolve` is the policy read `read_policy_setting` wraps, so the seam is
the roles kit's wrapper, not a second caller of `resolve`. Scout A's row cites
`tools/roles/roles_lib.py:596` for `resolve_stage_efforts`, which holds at this base.

Recall terms used: `python tools/memory-recall/query.py "how does a judge role run on its own harness
and credential" --terms "roles.harness roles.auth act-harness act-auth per role resolver judge head
subscription bare mode credential"`
