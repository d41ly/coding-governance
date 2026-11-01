# TOOL-dTendedCadence-69 — the landing asks the remote which payload its record ref names on every run, whether or not the payload object is local

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md) | research | TOOL-dTendedCadence-60 TOOL-dTendedCadence-67 TOOL-dTendedCadence-70 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H3 with id 36 (TOOL-dTendedCadence-70). Unit 50 fetches and compares
`refs/gov/maintain-record/<key>` only when `git cat-file -e <payload>^{commit}` fails (spec-50 S2,
:32-36, §4 :71-72); when the object is present it checks that "the local object" names `<payload>`,
which compares the payload with itself. The object is always present on the walk's own node, which
built it, in every worktree sharing that object store, and in any clone that already landed or fetched
it. So an older payload lands over a newer record of the same key, and the newest committed record
becomes whichever landed last. This unit puts the freshness check before the cache, on every run.

## 2. Scope (IN)

- **S1** — The query. `run_record_landing` (unit 50 S1) first runs `git ls-remote <name>
  refs/gov/maintain-record/<key>`, bounded at 30 s, `<name>` from TOOL-dTendedCadence-68, through
  `read_remote_record_ref(root, name, key)` in `tools/drift-audit/maintenance.py`, which answers the
  40-hex sha the remote's ref names, `""` for no such ref, or raises on a failed or killed query.
  Observed by AC1.
- **S2** — The verdict, before any object is read and before any write. A sha other than `<payload>`
  exits 1 with `land — superseded: refs/gov/maintain-record/<key> names <sha12>`; no such ref exits 1
  with `land — refused: refs/gov/maintain-record/<key> is not on <name>`; a failed query exits 1 with
  its line. Only a ref naming `<payload>` goes on. Observed by AC1 and AC2.
- **S3** — The fetch. With the ref naming `<payload>`, the object is fetched into
  `refs/gov/remote/maintain-record/<key>`, bounded at 30 s, only when `git cat-file -e
  <payload>^{commit}` fails; the cache decides whether to fetch, never whether the payload is current.
  Unit 50 S2's "or the local object where it was present" is not built. Observed by AC2.

## 3. Non-goals (OUT)

- The criteria that land with the object already local: TOOL-dTendedCadence-70.
- Unit 50 S3's checks and S4's write: unchanged, run after S2 passes.

### Edges

- **consumes-from** `TOOL-dTendedCadence-50` — `run_record_landing`'s fetch and superseded check (S2), which this unit runs against the remote on every landing
- **consumes-from** `TOOL-dTendedCadence-68` — the remote name the query and the fetch are made to
- **hands-off** `TOOL-dTendedCadence-70` — `read_remote_record_ref` and the always-run verdict, whose cases that unit runs with the payload already local

## 4. Design

```
run_record_landing(root, key, base, payload, sha256):
    name = resolve_remote(root)                          (TOOL-dTendedCadence-68)
    sha  = read_remote_record_ref(root, name, key)       (30 s)
    sha == ""         -> exit 1  not on <name>
    sha != payload    -> exit 1  superseded
    git cat-file -e <payload>^{commit} fails -> fetch the ref into the cache (30 s)
    ... unit 50 S3 and S4, unchanged
```

`ls-remote` reads the remote's ref without transferring objects, so the check costs one round trip
even when the object is local. The remote ref is the one fact that says which record of a key is
newest, because unit 49 moves it on every newer record of that key (spec-49 §8 F2).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_remote_record_ref` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1 to S3
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Always fetch the ref.** It transfers the payload's objects on every run to answer a question one
  ref read answers; S3 fetches only when they are missing.
- **Compare the local cache ref.** The cache is as old as the last fetch, the same staleness this
  unit closes.

## 5. Production-readiness checklist

- security — the landing writes only a payload the remote currently names, so a replayed older
  intake writes nothing.
- perf / scale — one bounded `ls-remote` per landing, plus a fetch only on a cache miss.
- error / empty / loading states — a failed or killed query, an absent ref and a moved ref each exit 1
  with one line, before any write.
- observability — the superseded line names the sha the remote holds.
- risks — a remote unreachable at landing time fails the patch build, which retries as any patch
  build does; it never lands unverified.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no landing exists at base.
- user docs — N/A — the verb's page line (unit 50 S5) is unchanged.

## 6. Acceptance criteria

The fixture is unit 50's: unit 49's scratch repository with its bare remote, and a second clone.

- **AC1** — When `read_remote_record_ref` is called in the second clone for a key the bare remote
  holds, it answers that ref's 40-hex sha; for a key it does not hold, `""`; and with the remote's URL
  pointed at a missing directory, it raises.
  Red when: an absent ref reads as current, or a failed query reads as absent.
- **AC2** — When `python maintenance.py land` runs in the second clone with the ref deleted on the
  bare remote, it exits 1 printing `is not on`; with the ref moved to another record's commit, it exits
  1 printing `superseded`, and `git for-each-ref refs/gov/remote/` in that clone prints nothing new,
  so no fetch ran; with the ref naming the payload, it lands and exits 0.
  Red when: a payload is fetched or written before the remote's ref is read.

The cases with the payload object already local are TOOL-dTendedCadence-70's.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · a deleted, a moved and a current remote ref read before any fetch, staged against the cache-miss-only check · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 4 (HIGH, item H3) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

The seam is unit 50's verb, its check moved ahead of its cache, and the claims' bounded remote read
(`read_claims`, `tools/unattended/unattended.sh:2118-2150`, whose shape unit 50 §10 already ports).
`python tools/codebase-map/reuse_lookup.py "check a remote ref names a commit before landing"` ranked
name stems only, `check`, `before`, `build_commit` and `check_line`, none a remote ref read from
Python, so no existing seam fits beyond the claims' shape.

Recall terms used: `python tools/memory-recall/query.py "how does a landing know its payload is the
newest record of its key" --terms "superseded payload ls-remote fetch cache-miss stale object local
refs gov maintain-record landing"`
