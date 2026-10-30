# DEPL-dShippedRelease-6 — the first engine adapter, `compose-systemd`, for signed container images

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0416@7154a42c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-8 DEPL-dShippedRelease-15 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-26 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

The release program needs one real engine behind `release.promote`. This unit builds it: the adapter
`compose-systemd`, named for the engine it drives and never for an adopter, fitted to signed container
images on `compose` and `systemd` hosts, with every adopter's value in that adopter's own
`.governance/policy.toml`.

## 2. Scope (IN)

Build-run precondition: DEPL-dShippedRelease-15 has landed the `integrations` kit, `point.flow.release`,
`check_adapter_header` and the engine verbs. Before it, TOOL-dWellOiledMachine-20 and -17 land
`tools/runtime/points.toml` and the grant check, and dGroundRules' `policy.py get` reads the rows of S5.
This unit owns no node. It reads `item.release.promote`, `policy-key.deploy.runs` and
`policy-key.release.environments`.

- **S1** — The engine verbs (I12), in the new `tools/integrations/engines/compose_systemd.py`:
  `read-current <E>` prints E's deployment id; `promote <E> <sha> --expect <id>` and
  `rollback <E> <sha> --expect <id>` are one compare-and-swap; `read-back <E> <sha>` prints the id when the
  running image is that SHA's image, and exits non-zero otherwise. A deployment id is the running image's
  digest, `sha256:<hex>`, read from the host and never from a file the adapter wrote. Each verb exits by
  DEPL-dShippedRelease-15 S5's table: 0 done, 2 refused, 3 compare-and-swap refused, 4 unreachable. A
  promote whose running digest already equals the target exits 0 printing `already there`, whatever
  `--expect` says, since the item counts that as done. Observed by AC1, AC2, AC3.
- **S2** — The compare-and-swap, built because the hosts offer none (§8 F1). One POSIX `sh` script,
  `tools/integrations/engines/compose-systemd-host.sh`, reaches the host on stdin through the environment's
  `transport`, with its values as quoted positional arguments. It takes the lock `<state-dir>/<E>.lock` with
  `mkdir`, reads the live digest, compares it with `--expect` inside the lock, swaps, and clears the lock in
  an `EXIT` trap. A lock already held exits as `locked` and is never broken. Observed by AC2, AC4.
- **S3** — The two host kinds. Under `host-kind = "compose"` the swap writes `<state-dir>/<E>.env` holding
  `GOV_IMAGE=<image>@<digest>`, and runs `docker compose -p <unit> --env-file <that file> up -d`; the live
  digest is `docker inspect` of the project's containers. Under `host-kind = "systemd"` the swap writes the
  override file `<unit>.service.d/gov-image.conf` holding `Environment=GOV_IMAGE=<image>@<digest>`, then
  runs `systemctl daemon-reload` and `systemctl restart <unit>`; the live digest is
  `systemctl show <unit> -p Environment` read with `ActiveState=active`. An adopter's compose file or unit
  names `GOV_IMAGE`; a host naming nothing else keeps working by hand. Observed by AC3, AC5.
- **S4** — Signed images only. Before the lock, `check_signature` resolves `<image>:<tag>` to its digest and
  runs the environment's `verify-signature` command with `{image}` filled in as `<image>@<digest>`. A
  non-zero exit, a missing command and an empty value each refuse, nothing swapped. The adapter names no
  signing tool, so gov gains no dependency (§8 F2). Observed by AC6.
- **S5** — The adopter's values, seven catalogue rows in `tools/policy/catalogue.toml`, each
  `owner = "dShippedRelease"`, each with `summary` and `usage`, named
  `release.engine.compose-systemd.<environment>.<field>` for `host-kind`, `image`, `unit`, `state-dir`,
  `tag`, `transport` and `verify-signature` (§4 "The values"). `read_engine_values(E)` reads each through a
  literal `policy.py get` call, so the reader-coverage arm counts it. A value unset that the verb needs
  refuses naming the key. `<environment>` is the same name `release.environments` lists, and gov ships no
  value. Observed by AC7.
- **S6** — The registration, one `[[adapter]]` row in `tools/runtime/points.toml`, written by
  `python adapters.py new point.flow.release compose-systemd --kind deploy-engine`, the header
  `check_adapter_header` grades: `kind = "deploy-engine"`,
  `grant = { service = "local", scopes = [], secret = "anonymous" }`, `witness-source`, `probe`,
  `fallback = "no release; the build closes at landing"`, and `cas = "built"`. `probe` is `read-current`,
  whose failed read is a dead probe and never green. Observed by AC8.
- **S7** — The static cross-key rule, `check_engine_runs(row, runs)` in `tools/integrations/adapters.py`: a
  `deploy-engine` row whose `cas` is `none` is refused unless `deploy.runs` reads `operator`, and a `cas`
  outside `native`, `built` and `none` is refused. `python adapters.py --check` runs it over every engine
  row, and `run_release_promote`'s refusal (DEPL-dShippedRelease-15 S8), its run-time half, calls it, so the
  rule is spelled once. This adapter is `built`, so the arm's negative case is a planted row. Observed by
  AC9.
- **S8** — The fixture, `python compose_systemd.py --fixture --case <name>`: stub `docker` and `systemctl`
  scripts on a scratch `PATH`, an empty `transport`, and a state directory in the run's scratch, one case
  per criterion of §6. It prints what it observed beside what the case expects, exits 1 on a difference, and
  never touches a real daemon. Observed by AC1 to AC9.
- **S9** — A section of `help/release.md` (DEPL-dShippedRelease-15 S17): what the adapter drives, the seven
  values, the `GOV_IMAGE` contract, what `locked` means, and what the compare-and-swap does not stop.
  Observed by AC10.

## 3. Non-goals (OUT)

- No release program: `release.*`, `release/<E>`, the runner and the header factory are
  DEPL-dShippedRelease-15's.
- No verify adapter, no canary and no rolling fleet update. Round 3's fit is signed images on the two host
  kinds, and this clause names no rollout strategy.
- No image build, no signing and no registry write: the adopter's CI builds and signs, and this adapter only
  reads.
- No SSH code. `transport` is an argv prefix the adopter declares, and its authentication is that program's.
- No adopter's value in any shipped file: `release.engine.compose-systemd.*` rows carry defaults only.
- No lock breaking. A `locked` exit routes as `release.promote`'s "refused or unreachable": a retry, then an
  owner item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-15` — `check_adapter_header`, which grades this row, and `promote`, the engine verbs this adapter implements and `run_engine_verb` calls
- **consumes-from** external — TOOL-dWellOiledMachine-20's `points.toml` and -17's grant check, and dGroundRules' `policy.py get`, each specced and unbuilt at base `f4597719`
- **hands-off** `DEPL-dShippedRelease-77` — the verbs and the host script, which that unit gives `none`, a named service and a failed restart (review id 94)
- **hands-off** `DEPL-dShippedRelease-78` — S5, S7 and its write set, which the minors batch repairs (review ids 24, 62, 63, 96)

## 4. Design

### Evidence

- `check_value` (`tools/policy/policy.py:143`) grades a value, and `read_catalogue_row` (`:219-241`) refuses
  a key with no row, so "the adopter's values in that adopter's own policy file" needs rows. A `<word>`
  segment matches one segment (`tools/policy/README.md:50-53`), which `roles.effort.<role>`
  (`tools/policy/catalogue.toml:296`) already uses.
- `release.environments` (`tools/policy/catalogue.toml:1101-1105`) admits `[A-Za-z0-9][A-Za-z0-9_.-]*`, so
  `<environment>` is one segment.
- Arm 10 (`tools/govkit/govkit.py:3731`) bans each `tools/govkit/adopters.toml` name from every shipped
  file, so a name in this kit reds at selfcheck the day the row ships.
- Measured 2026-10-30 on this node (Docker Compose v5.1.4, PINNED): `docker compose up --help` prints
  `--wait` and no compare, expect or if-match flag, and `git-bash` holds no `flock`. `mkdir` of an existing
  directory exits 1 and leaves it, the one atomic create both host kinds share.

### The verbs and their exits

| Exit | Meaning | `release.promote`'s route |
|---|---|---|
| 0 | done, or `already there` | `release.verify` |
| 3 | `--expect` differs from the live digest | nothing promoted and nothing recorded |
| 2 | refused: a value unset, the signature refused, or an argument | refused → retry, then an owner item |
| 4 | unreachable, or `locked` | retry, then an owner item |

`rollback` is `promote` with the rolled-back SHA's image: one code path, `run_host_script`, so the
compare cannot differ between them. A stale holder's rollback after a take-over holds the old `--expect`,
the live digest has moved, and the script exits 3 with nothing swapped.

### The values

| `<field>` | `allowed` | Default | Reads as |
|---|---|---|---|
| `host-kind` | `["compose", "systemd"]` | `compose` | which swap S3 runs |
| `image` | `pattern`, `[a-z0-9][a-z0-9./_:-]*` or empty | empty | the repository, no tag |
| `unit` | `name`, `[A-Za-z0-9][A-Za-z0-9_.@-]*` or empty | empty | the compose project, or the systemd unit |
| `state-dir` | `pattern`, an absolute POSIX path | `/var/lib/gov-release` | the lock and env file |
| `tag` | `pattern`, holding `{sha}` or `{sha12}` | `{sha}` | how a SHA names its image |
| `transport` | `pattern`, words of `[A-Za-z0-9_./:@=+-]`, or empty | empty, run locally | the argv prefix reaching the host, split once by `shlex.split` |
| `verify-signature` | `pattern`, the same words plus `{}`, or empty | empty, refused at use | the command checking `{image}` |

A value reaches the host script only as a quoted positional argument after `sh -s --`, and each row's
pattern admits no shell metacharacter, so `check_value` at the file is the one validation.

### Inventory

| Minted | Cell or kind |
|---|---|
| `read_engine_values`, `check_signature`, `derive_image_digest`, `render_host_script`, `run_host_script`, `cmd_read_current`, `cmd_promote`, `cmd_rollback`, `cmd_read_back` | `py.function`, `compose_systemd.py`, each put to `lexicon.py --suggest`, OK |
| `check_engine_runs` | `py.function`, `adapters.py`, OK |
| `compose-systemd` | engine name, a tag segment |
| `GOV_IMAGE` | the host's environment variable |
| the seven `release.engine.compose-systemd.<environment>.<field>` rows | catalogue rows |

### Rollout

Dark: no environment is listed by default, so nothing calls the adapter until an adopter sets
`release.environments`, `release.env.<E>.engine = "compose-systemd"` and the seven values.

### Files touched (estimate)

- `tools/integrations/engines/compose_systemd.py` (new)
- `tools/integrations/engines/compose-systemd-host.sh` (new)
- `tools/integrations/adapters.py`: `check_engine_runs`
- `tools/integrations/kit.toml`: the files and the leg `compose-systemd engine fixtures`
- `tools/runtime/points.toml`: the `[[adapter]]` row
- `tools/policy/catalogue.toml`: the seven rows
- `tools/gate-legs.json`: rendered by `leg_factory.py --write` from the kit's `[[gate_leg]]`
- `help/release.md`: the section of S9

### Alternatives rejected

- **The gap declared, `cas = "none"`, operator only.** It needs no host write, and it loses by S7's own
  rule: under the `landing-node` default the adapter refuses to run at all, so the first adopter's
  unattended release never starts. It stays the path for a later engine, which is why S7 exists.
- **A lock through the daemon, `docker create --name <lock>`.** A container name is unique per daemon, so
  this needs no host shell. It loses on the clause's second host kind: a `systemd` host need run no Docker
  daemon, and the walkthrough's first adopter keeps native units beside compose.
- **A moved registry tag.** Promoting by moving `<E>-current` makes the tag the thing compared, and the tag
  is not what runs: a host that has not pulled still answers the old image. The compare would pass on a
  value that is not E's current deployment id, which is the clause's subject.
- **`flock`.** Absent on this node's `git-bash`, so the fixture could not run it, and a held `flock` on a
  network path is not portable. `mkdir` gives the same exclusion with no util-linux.

## 5. Production-readiness checklist

- security: a value reaches the host only as a quoted argument, under a pattern admitting no shell
  metacharacter. The adapter reads no secret, so `grant` is `anonymous`, and the adopter's `transport`
  program holds its own key. `verify-signature` is required: an empty value refuses, deny by default.
- perf / scale: one transport round trip per verb, plus a registry resolve on a promote.
- error / empty / loading states: unreachable and `locked` exit 4; a stale `--expect` exits 3; a value unset
  refuses naming the key.
- observability: each verb prints one line; `read-current` is the header's probe.
- risks: the lock binds only this adapter. A person running `docker compose up` between the compare and the
  swap is not stopped, though the next compare reads what they did. A killed script leaves `<E>.lock`, which
  stops every later promote until the owner removes it: the item's owner-item route carries that.
- testing: S8's stubs. No criterion needs a real daemon.
- migration: N/A — a new adapter, dark until an adopter opts in.
- user docs: S9.

## 6. Acceptance criteria

- **AC1** — When `python compose_systemd.py --fixture --case promote` runs, `read-current` prints the stub's
  digest, `promote` swaps it, and `read-back` prints the new digest and exits 0; with
  `--case read-back-other` a SHA whose image is not running exits non-zero.
  Red when: `read-back` reads the env file rather than the running digest.
- **AC2** — When `--case stale-rollback` runs, a holder reads id A, a second holder promotes to B, and the
  first holder's `rollback --expect A` exits 3, the stub recording no swap and `read-current` still printing
  B.
  Red when: the rollback swaps, or exits 0, or takes a generic refusal's exit.
- **AC3** — When `--case already-there` runs, a `promote` whose target is the live digest exits 0 printing
  `already there`, with a wrong `--expect` and no swap recorded.
  Red when: it re-swaps, or refuses on the stale `--expect`.
- **AC4** — When `--case locked` runs with `<E>.lock` planted, `promote` exits 4 printing `locked`, the lock
  is still there and no swap is recorded; with `--case lock-released` a failing swap leaves no lock.
  Red when: the lock is broken, or a failed swap strands it.
- **AC5** — When `--case systemd-promote` runs with a planted `.governance/policy.toml` reading
  `host-kind = "systemd"`, the stub records the override file, `daemon-reload` and `restart`, and
  `--case compose-promote` with `host-kind = "compose"` records `up -d` with the env file: each allowed
  value on its planted case.
  Red when: a value takes the other kind's swap.
- **AC6** — When `--case unsigned` runs, the stub signature command exits 1 and `promote` exits 2 with no
  lock taken and no swap; with `--case no-verify-value`, `verify-signature` empty refuses the same way.
  Red when: an unsigned image is promoted, or an empty value skips the check.
- **AC7** — When `--case planted-policy` runs, `read_engine_values` returns the seven values a planted
  `.governance/policy.toml` holds for E, and `--case unset-image` exits 2 naming
  `release.engine.compose-systemd.<E>.image`; `python policy.py check` over a value holding `;` refuses it.
  Red when: a metacharacter passes, or an unset value reaches the script.
- **AC8** — When `python adapters.py --check` runs, the `compose-systemd` row passes `check_adapter_header`
  and prints `cas built`, and `--case dead-probe` makes `probe` read as failed, never green.
  Red when: the row lacks a header field, or a failed probe reads green.
- **AC9** — When `python adapters.py --check` runs over a planted row `cas = "none"` under a planted
  `deploy.runs = "landing-node"`, it exits 1 naming the row and the key; under `deploy.runs = "operator"` it
  exits 0; a planted `deploy.runs = "adopter-ci"` exits 1; `cas = "maybe"` exits 1.
  Red when: an engine with no compare-and-swap runs off the operator.
- **AC10** — When `grep -n GOV_IMAGE release.md` and
  `python compose_systemd.py --fixture --case adopter-names` run, the page names the contract, and every
  `names` value of the deployer's adopter list is absent from both engine files.
  Red when: an adopter's name appears in a shipped engine file, the class arm 10 bans.

## 7. Gates

`policy fixtures` · `policy check` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/integrations/engines/compose_systemd.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC10 · the fixture's `stale-rollback`, its failing case a compare that reads the env file · none
New arm: tools/integrations/adapters.py · covers AC8 AC9 · a planted `cas = "none"` row under `landing-node` · none

## 8. Open questions

- **F1 — Build a compare-and-swap, or declare the gap?** Options: (a) a host-side `mkdir` lock with the live
  digest compared inside it; (b) `cas = "none"`, running only under `deploy.runs: operator`; (c) a lock
  through the Docker daemon; (d) a moved registry tag. (b) leaves the default `landing-node` refusing the
  first adopter's release; (c) fails the `systemd` host; (d) compares what is not running. (a) meets the
  clause on both host kinds at the default, and its limit is stated in §5. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3, the §4 tests. widens: none · relaxes: none
- **F2 — Which signing tool?** Sources name none. Options: (a) the adopter's own command as a policy value;
  (b) one tool built in. (b) is a new external dependency, veto 2, and fits one adopter. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Where do the adopter's values live, given `read_catalogue_row` refuses a key with no row?**
  Options: (a) seven rows with an `<environment>` placeholder; (b) one opaque map row; (c) a file of the
  kit's own. (b) leaves each value ungraded, and (c) is not "that adopter's own policy file". The catalogue
  header reads one row per design row and v2 has none of these, so the clause is what names them. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3.
  grants: PLAY-dClosedLoop-3 seven `release.engine.compose-systemd.<environment>.<field>` catalogue rows the clause's "adopter's own policy file" names. widens: none · relaxes: none
- **F4 — The adapter's name.** The walk leaves it to this spec under WK-8's rule (walk:746-749). Options:
  (a) `compose-systemd`, the two host engines; (b) `signed-image`, which names a property and no engine; (c)
  `container-host`, which names neither. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, "named for
  the engine it drives". widens: none · relaxes: none
- **F5 — Where the cross-key check lives.** Scout C fork 10 leaves it unowned. Options: (a) `adapters.py`,
  beside the header it reads; (b) `tools/policy/check_policy.py`, which reads no adapter row and would
  import across kits. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, the spec run.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 77, 78); no scope, design or criterion moved.

## 10. Reuse audit

No existing seam fits the engine:
`python tools/codebase-map/reuse_lookup.py "a deployment adapter comparing the running image digest and swapping it on a host"`
ranked name-stem hits only (`digest`, `resolve_compare_base`, `read_host_name`), and no engine code exists
at HEAD, which scout C's row confirms. The seams extended are DEPL-dShippedRelease-15's
`check_adapter_header` and the `[[adapter]]` row of TOOL-dWellOiledMachine-20 S4, whose "any further field
the point's own unit declares" is where the header sits. M12 applies, and §4 "Alternatives rejected" records
each candidate and the test that rejected it. Scout C's row holds at source: `:3731` and `policy.py:143`
read as it says. One recall hit disagrees: the research record's "each adopter's engine adapter"
(research-integrations-a:85), which WK-8 superseded.

Recall terms used: engine adapter compare-and-swap deployment id compose systemd signed image release
promote rollback
