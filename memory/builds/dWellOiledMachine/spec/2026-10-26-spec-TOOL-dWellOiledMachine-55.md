# TOOL-dWellOiledMachine-55 — the transport points in Runtime's `[extend]`: a lease store with git refs its only adapter and its conformance probes, a doorbell, and an offer source

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0333@dce4872c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-d.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-d.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-61 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-55-deviation-551.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-55-deviation-551.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

Coordination has no transport point: leases and mail are written to `refs/gov/*` directly, which
hosted cloud sessions cannot push, and no host declares whether it can (gap-rt-41). This unit adds
three points to Runtime's `[extend]`: a lease store, git refs its only adapter, with a conformance
fixture holding the fence, tombstone and atomic-landing probes; a doorbell, arming
`deps.messaging`'s registered names; and an offer source, the node's own pick built in. Each host
declares whether it can write custom refs and which auth class it needs, a host that cannot taking a
branch-namespaced fallback or acquiring nothing, and every adapter row declares its tenancy,
retention and region (P40; the owner's CL-1).

## 2. Scope (IN)

- **S1** — Three `[[point]]` rows in `tools/runtime/points.toml` (I4, TOOL-dWellOiledMachine-20):
  `point.lease-stores`, whose `contract` names the acts acquire, renew, release, take over, read and
  fence, the epoch rule of TOOL-dPlacedRequest-1 S3 and the three probes of S4; `point.doorbells`,
  whose contract is a ring carrying only `<ref> <id>` (KICK-dKeptSession-21's payload rule); and
  `point.offer-sources`, whose contract is an ordered list of claimable units for one project. The
  packet's owned nodes lack all three, which v2:1905 and cloud-and-scale items 9 and 11 declare; the
  clause's text is unchanged, so the gap is an ask on dClosedLoop's owned-node rows, never a deviation.
  Observed by AC1.
- **S2** — Two built-in `[[adapter]]` rows: `git-refs` at `point.lease-stores`, wrapping the lease
  verbs of TOOL-dPlacedRequest-1 S5 and the one ref writer `write_gov_ref` (TOOL-dPlacedRequest-11
  S1), never a copy; and `node-pick` at `point.offer-sources`, the node's own pick, whose function
  is TOOL-dWellOiledMachine-54's. No doorbell adapter is built. Each row carries I4's `grant`,
  graded by TOOL-dWellOiledMachine-17's `check_adapter_grant`, as
  `{ service = "local", scopes = [], secret = "anonymous" }`: the `git-refs` adapter holds no
  credential of its own, the remote's credential being the host's `auth-class` (S3). Each row
  declares `tenancy`, `retention` and `region` in the shapes TOOL-dWellOiledMachine-20's
  `check_points` grades: `git-refs` `project`, `forever`, `remote`, and `node-pick` `local`, `none`,
  `local`. Observed by AC1.
- **S3** — The host declarations: every `[[adapter]]` row at `point.host-adapters`
  (TOOL-dWellOiledMachine-13) gains `custom-refs` (`true` or `false`), `auth-class` (`ambient`,
  `token` or `oauth`) and, where `custom-refs` is `false`, `fallback` (`branch` or `none`).
  TOOL-dWellOiledMachine-13's `check_host_row(row)` (`tools/runtime/hosts.py`) gains the refusal of
  a host row missing one of these fields or naming a value outside its set, naming the row and the
  field. Observed by AC1.
- **S4** — The conformance fixture,
  `python <prefix>/runtime/lease_store.py conform --remote <url> [--host <name>]`, one line per
  probe, `<probe> — pass` or `<probe> — fail · <why>`, exit 1 on any fail, against a remote it may
  write scratch refs to:
  - **fence** (`check_store_fence`): holder A reads the lease tip, B takes the lease over, and A's
    `git push --atomic --force-with-lease=<lease>:<tip>` of a branch and a new beat is rejected with
    the branch unchanged; a re-push of the lease ref unchanged is refused by `check_fence_beat`
    (TOOL-dPlacedRequest-15) before it is sent.
  - **tombstone** (`check_store_tombstone`): a claim queued against the lease tip it last fetched is
    refused once another holder has claimed it and once it carries a terminal tombstone
    (TOOL-dPlacedRequest-16 S3), and the tombstone's ref is still present after the release.
  - **atomic-landing** (`check_store_landing`): one atomic push of a branch, a lease beat with
    `renews: no` and a mail ref writes all three or none; with the mail ref refused by the remote,
    the branch and the lease are unmoved; with all accepted, the lease's status still reads live.
  Observed by AC2, AC3, AC4.
- **S5** — The host probe, `check_store_host` under `--host <name>`: a host whose row declares
  `custom-refs = true` must be able to push a scratch `refs/gov/` ref to the remote; a refusal
  prints `host — fail · <name> declares custom-refs and the remote refused <ref>`. Observed by AC5.
- **S6** — The fallback: `derive_store_ref <ref>` in `tools/unattended/unattended.sh`, beside
  TOOL-dPlacedRequest-1's `derive_lease_ref`, maps `refs/gov/leases/<rest>` to
  `refs/heads/gov/leases/<rest>` when the host `run.host` names declares `custom-refs = false` and
  `fallback = "branch"`, and is applied to every lease ref the verbs write and to the lease fetch
  refspec of `read_claims`; under `fallback = "none"` every lease act prints
  `lease — not acquired · host <name> writes no refs` and exits 2, writing nothing. A host with
  `custom-refs = true` maps nothing. Observed by AC5.
- **S7** — The doorbell names. The catalogue row `deps.messaging`
  (`tools/policy/catalogue.toml:174`) keeps its values and its owner, and its `registry` text becomes
  the point tag `point.doorbells`. `check_value` (`tools/policy/policy.py:143`) gains its registry
  arm: for an `enum` row whose `registry` is a `point.` tag, a value outside `of` is admitted when an
  `[[adapter]]` row at that point in the installed runtime kit's `points.toml` names it, the file
  found through the policy kit's inline `resolve_kit_dir` block and read as TOML data, never
  imported; with no runtime kit installed, or no such row, the value is refused as today. Observed by
  AC6.
- **S8** — The page `help/runtime.md` gains a section on the transport points: the three points,
  the two built-in adapters, the host fields, the fallback and the conformance command. Observed by
  AC7.

## 3. Non-goals (OUT)

- A second lease-store adapter, a doorbell adapter or a cloud host: the fleet expansion's endpoint
  adapters (v2:1900-1910).
- The pick function and the claimable ready set: TOOL-dWellOiledMachine-54.
- The lease grammar, record, verbs, tombstone and fenced push: TOOL-dPlacedRequest-1, -15 and -16.
- The lander's landing push carrying the beat and the notice: TOOL-dWellOiledMachine-60, through
  this point's `git-refs` adapter.
- The grant's own schema and the secret scan at each adapter's boundary: TOOL-dWellOiledMachine-17
  and -57.
- Mail and binding refs under the fallback: only the lease store's refs are mapped.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-20` — `points.toml`, the registry the three points and two adapters are rows of
- **consumes-from** `TOOL-dWellOiledMachine-13` — `point.host-adapters`, the host rows and `check_host_row` S3 adds `custom-refs`, `auth-class` and `fallback` to
- **hands-off** `TOOL-dWellOiledMachine-60` — `point.lease-stores`, the store whose `git-refs` adapter carries the atomic landing
- **hands-off** `TOOL-dWellOiledMachine-54` — `point.offer-sources`, the point whose built-in `node-pick` row names that unit's pick
- **consumes-from** external — TOOL-dPlacedRequest-1's lease verbs and `derive_lease_ref`, -11's `write_gov_ref`, -15's `check_fence_beat`, -16's tombstone; KICK-dKeptSession-6's ring point and -21's payload rule

- **hands-off** `TOOL-dWellOiledMachine-44` — `check_value`'s registry arm, which admits `memory.mirror`'s registered names once S2 names the point
- **hands-off** `TOOL-dWellOiledMachine-79` — its catalogue edit (finding 56), which the spec audit's minors batch repairs
## 4. Design

### Evidence

- Today's only gov ref writer is `write_claim` (`tools/unattended/unattended.sh:2396`), over
  `refs/gov/runs` (`:2087-2088`); nothing declares a host's ref capability, tenancy, retention or
  region.
- `deps.messaging` is a literal enum with `registry = "a registered doorbell"`
  (`tools/policy/catalogue.toml:174-177`), and `check_value`'s registry arm defers a registered name
  to a registry (`tools/policy/policy.py:143-159`).
- The research probes: P2(b) an atomic push with a stale lease is rejected and the branch unchanged;
  P2(c′) an unchanged lease ref is never checked; P3 a queued claim yields to a claim or a terminal
  commit, and a pruned tombstone lets it win; P5 one atomic push of branch, lease and mail writes
  all or none
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-headless.md:34-41`).
  The fixture repeats P2(b), P3 and P5, the three the clause names.
- The point's acts and its fixture are the research's seam S3 (`:115`), and cloud-and-scale item 11
  states the host fields (`2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md:249-253`).

### The rows

```toml
[[point]]
name = "point.lease-stores"
purpose = "where a lease lives, and how it is fenced"
contract = "acquire, renew, release, take-over, read and fence; the epoch rule; conform: fence, tombstone, atomic-landing"

[[adapter]]
point = "point.lease-stores"
name = "git-refs"
grant = { service = "local", scopes = [], secret = "anonymous" }   # the remote's credential is the host's auth-class
tenancy = "project"
retention = "forever"        # a tombstone is pruned only by --lease prune, past leases.queued-claim-days
region = "remote"

[[adapter]]
point = "point.offer-sources"
name = "node-pick"
grant = { service = "local", scopes = [], secret = "anonymous" }
tenancy = "local"
retention = "none"
region = "local"
```

A host row, after this unit: `custom-refs = true`, `auth-class = "ambient"` for the OS scheduler
host on a node whose git remote takes custom refs.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `point.lease-stores`, `point.doorbells`, `point.offer-sources` | points | none |
| `git-refs`, `node-pick` | adapter names | none |
| `custom-refs`, `auth-class`, `fallback` | host-row fields | none |
| `tools/runtime/lease_store.py` | module, verbs `conform`, `--selftest` | none |
| `check_store_fence`, `check_store_tombstone`, `check_store_landing`, `check_store_host` | Python functions | `check`, OK |
| `derive_store_ref` | shell function | `derive`, OK |

`check_store_host` and `derive_store_ref` were checked with `python tools/lexicon/lexicon.py
--suggest <name> --as py.function`, each OK; the other three `check_` names share their verb.

### Migration

Additive: the host rows gain three fields, each host registered before this unit is given
`custom-refs = true` and `auth-class = "ambient"`, its behaviour at this base. A deployment whose
remote refuses custom refs learns it from S5 and sets `fallback`.

### Files touched (estimate)

- `tools/runtime/points.toml`
- `tools/runtime/lease_store.py`
- `tools/unattended/unattended.sh`
- `tools/policy/catalogue.toml`
- `tools/policy/policy.py`
- `tools/runtime/hosts.py`
- `help/runtime.md`

### Alternatives rejected

- **The fallback over every `refs/gov/` namespace.** Mail and bindings have no point of their own
  here, and their readers would all move; the clause scopes the fallback to acquiring a lease.
- **A doorbell adapter built in.** The live channel is a session's inbox (TOOL-dWellOiledMachine-35)
  and any other is the fleet expansion's endpoint adapter.

## 5. Production-readiness checklist

- security — every row declares its grant, tenancy, retention and region; the conformance probes
  write scratch refs only, under a `refs/gov/conform/` prefix they delete.
- perf / scale — the probes run on demand, never on a beat; the fallback is one string mapping.
- error / empty / loading states — a missing field is refused at registration; `fallback = "none"`
  exits 2 with one named line and writes nothing.
- observability — each probe prints one line; each host refusal names the host and the ref.
- risks — a remote that refuses `--atomic` fails the fence and the atomic-landing probes, which is
  the signal TOOL-dPlacedRequest-15's `unfenced` class reports at landing.
- testing — the fixture cases AC1 to AC6 and the arm in §7.
- migration — the host rows' defaults above.
- user docs — `help/runtime.md`'s section (S8).

## 6. Acceptance criteria

The fixture is a bare remote and two clones under `%TEMP%` with short names, `RUN_CLAIMS` on, a
second bare remote whose `pre-receive` hook refuses every `refs/gov/` ref, and a third configured
with `receive.advertiseAtomic false`.

- **AC1** — When `grep -n -E 'point\.(lease-stores|doorbells|offer-sources)' points.toml` runs, the
  three points and the `git-refs` and `node-pick` rows are listed and `python points.py check` exits
  0; and `check_host_row` refuses a planted host row with no `custom-refs`, naming the row and the
  field.
  Red when: a host row lacking a transport field registers.
- **AC2** — When `python lease_store.py conform --remote <first remote>` runs, it prints
  `fence — pass`; against the third remote it prints `fence — fail` naming the refused atomic push.
  Red when: the third remote's fence reads pass.
- **AC3** — When the conformance run's tombstone probe runs, it prints `tombstone — pass`; with a
  planted store that prunes a released lease ref, it prints `tombstone — fail` naming the queued
  claim that won.
  Red when: the pruning store passes.
- **AC4** — When the atomic-landing probe runs against the first remote it prints
  `atomic-landing — pass` and the lease record reads `renews: no` with its status unchanged; with a
  planted `pre-receive` refusing the mail ref, `git ls-remote` shows the branch and the lease
  unmoved.
  Red when: a branch or lease moves while the mail ref is refused, or the landing releases the
  lease.
- **AC5** — When `conform --remote <second remote> --host fx-host` runs for a host row declaring
  `custom-refs = true`, it prints
  `host — fail · fx-host declares custom-refs and the remote refused` and exits 1; with the row at
  `custom-refs = false` and `fallback = "branch"`, `--lease acquire build fx` writes
  `refs/heads/gov/leases/fx/build`, and with `fallback = "none"` it prints `lease — not acquired`
  and exits 2.
  Red when: the refused host passes, or the fallback writes under `refs/gov/`.
- **AC6** — When `python policy.py get deps.messaging` reads a planted value `stub-bell`, it refuses
  it with no adapter row registered at `point.doorbells`, and admits it once a planted row registers
  `stub-bell` there.
  Red when: an unregistered name is admitted.
- **AC7** — When `grep -n "point.lease-stores"` runs over the runtime kit's page `runtime.md`, the
  section names the three points, the host fields and the `conform` command.
  Red when: any of them is missing.

## 7. Gates

`policy fixtures` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/lease_store.py · covers AC1 AC2 AC3 AC4 AC5 · the `--selftest` fixture's three remotes and planted rows, staged against a registration check that reads no transport field · none
New arm: tools/policy/check_policy.py · covers AC6 · a planted doorbell name, staged with the point row absent · none

## 8. Open questions

- **F1 — Is the branch-namespaced fallback built, or only the acquire-nothing arm?** (a) Both, the
  host choosing by `fallback`; (b) `none` only, `branch` refused until a host needs it. The clause
  says a host takes "a branch-namespaced fallback or acquires nothing", and (b) leaves its first arm
  unbuilt. Rung 3, the most feature-rich option. RESOLVED (agent, 2026-10-26, delegated): (a).
  widens: none · relaxes: none
- **F2 — How do the three points the packet omits enter the build?** (a) As I4 rows here, the gap a
  deviation record; (b) a packet edit. The packet's Non-goals bar this run from editing it, and the
  brief names (a). Rung 1, v2:1905, which declares the points. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F3 — Who arms the registered doorbell names, which TOOL-dWellOiledMachine-1 and -20 each leave
  unbuilt?** (a) This unit: the row's `registry` names `point.doorbells` and `check_value`'s registry
  arm reads the installed `points.toml` as data; (b) the ring point admitting a name the policy kit
  refused. (b) reads a refused value past the policy kit's deny-by-default, and leaves the clause's
  "arming `deps.messaging`'s registered names" unbuilt at the reader every key goes through. Reading
  the file as data imports no runtime code, so the kit cycle unit 20 names does not arise. Rung 1,
  layer-runtime `[extend]`: names are "validated against the registry, never against a literal
  enumeration". RESOLVED (agent, 2026-10-26, delegated): (a); the arm admits names for any `enum` row
  whose `registry` is a point tag, so a later row joins it by naming its point. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-79.

## 10. Reuse audit

The seams extended are the point registry `points.toml` and its `check_points` (I4,
TOOL-dWellOiledMachine-20), the host row check `check_host_row` (TOOL-dWellOiledMachine-13), the lease
verbs and the one constructor `derive_lease_ref` (TOOL-dPlacedRequest-1 S1, S5), the one ref writer
`write_gov_ref` (TOOL-dPlacedRequest-11 S1), `check_fence_beat` (TOOL-dPlacedRequest-15), and the
policy kit's registry arm (`tools/policy/policy.py:143-159`). The probe `python
tools/codebase-map/reuse_lookup.py "register transport points for lease stores doorbells and offer
sources with conformance probes"` ranked `probe` (`tools/unattended/check-playbook.test.sh`),
`resolveLease` (`tools/unattended/run-lease.js`) and `check_conformance` (`tools/runlog/model.py`) by
name stem; `resolveLease` reads a run's lease file for a hook and `check_conformance` grades run-log
lines, and neither registers a point or probes a remote. Scout D's line cites `catalogue.toml:174` and
`unattended.sh:2396`, `:2088`, which hold at this base.

Recall terms used: `python tools/memory-recall/query.py "which transport points does the runtime
declare for leases and doorbells" --terms "lease-store point doorbell offer source git refs adapter
custom-refs auth class tenancy retention region"`
