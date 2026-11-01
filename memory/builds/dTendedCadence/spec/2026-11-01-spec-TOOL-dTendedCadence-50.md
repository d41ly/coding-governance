# TOOL-dTendedCadence-50 — `maintenance.py land`: the records-only patch build verifies the carried record by commit and digest and writes it, never re-deriving a reading

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 28 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
BLOCKER, which shares item B1 with id 1 (TOOL-dTendedCadence-49) and id 42 (TOOL-dTendedCadence-51).
Unit 48 S24 has the patch build re-derive the readings with `drift_report.py --readings` and refuse a
digest that differs (spec-48:107-110). `--readings` produces neither the walk's routes nor the record's
`fields`, `log-band`, `security-head` and `unread-nodes` (spec-6:226-230), so re-derivation cannot
reproduce the record, and unit 48 AC20 cannot pass beside unit 37. This unit gives the patch build
one verb that lands the record TOOL-dTendedCadence-49 carried: it checks the commit and the digest the
intake names, checks the record's key, path and head, and writes those bytes, reading no reading.

## 2. Scope (IN)

- **S1** — The verb. `run_record_landing(root, key, base, payload, sha256)` in
  `tools/drift-audit/maintenance.py`, run as `python maintenance.py land --key <key> --base <sha>
  --payload <commit> --sha256 <hex>`, the four values of the landing intake's text
  (TOOL-dTendedCadence-49 §4). Observed by AC1.
- **S2** — The fetch. When `<commit>` is absent from this clone, it fetches
  `refs/gov/maintain-record/<key>` from the one remote into `refs/gov/remote/maintain-record/<key>`,
  bounded at 30 s. It then requires that ref, or the local object where it was present, to name
  `<commit>`; a ref naming another commit exits 1 with `land — superseded: refs/gov/maintain-record/<key>
  names <commit12>`. Observed by AC2.
- **S3** — The checks, each exiting 2 with one `land — refused: <why>` line before any write: the
  commit has no parent and its tree one path; that path is `<home>/<date>-maintenance-<key>.md`, its
  `<date>` an ISO date and its key admitted by `derive_record_family` (TOOL-dTendedCadence-35); the
  SHA-256 of the blob's bytes equals `<hex>`; and the record's `**Key:**` and `**Base:**` lines equal
  `<key>` and `<sha>`. Observed by AC3.
- **S4** — The write. It writes the blob's bytes at that path through a temp file and `os.replace`,
  contained under the home as `write_maintenance_record` writes (spec-6 §4), prints `land — <key> ·
  <path> · written`, or `· unchanged` when the file already holds those bytes, and exits 0. The patch
  build commits the path. It runs no `drift_report.py`, reads no policy key and reads no clock.
  Observed by AC1 and AC4.
- **S5** — The docs. `help/maintain.md`'s section "The Maintain run" and the drift-audit README's
  maintenance record section state that a `land maintenance-record` intake is landed by this verb.
  Observed by AC5.

## 3. Non-goals (OUT)

- Building and pushing the payload: TOOL-dTendedCadence-49.
- The commit the patch build makes, and placing it: Plan's patch disposition, as for unit 1 S6.
- `maintenance.py write`'s stdin refusals: unit 48 S24's second half, unchanged.
- The end-to-end arm: TOOL-dTendedCadence-51.

### Edges

- **consumes-from** `TOOL-dTendedCadence-48` — S24's patch build, whose re-derivation and readings digest this verb replaces
- **consumes-from** `TOOL-dTendedCadence-49` — `refs/gov/maintain-record/<key>`, its one-path commit and the four-line text, the payload this verb verifies
- **hands-off** `TOOL-dTendedCadence-51` — `maintenance.py land`, the landing half of the round trip that unit's arm drives
- **hands-off** `TOOL-dTendedCadence-59` — `maintenance.py land`, by which that unit lands one record of every family (review id 24)
- **consumes-from** `TOOL-dTendedCadence-67` — a payload blob holding the record's raw bytes, so the SHA-256 over the blob equals the walk's over the file (review id 13)
- **consumes-from** `TOOL-dTendedCadence-68` — the remote name `run_record_landing` queries and fetches from, resolved by the kit's ladder (review id 21)
- **hands-off** `TOOL-dTendedCadence-69` — S2's fetch and superseded check, which that unit runs against the remote on every landing (review id 4)
- **hands-off** `TOOL-dTendedCadence-70` — §6 AC2 and its fixture, which that unit restates with the payload object local (review id 36)

## 4. Design

### The verb

```
run_record_landing(root, key, base, payload, sha256):
    git cat-file -e <payload>^{commit}  fails  -> fetch the ref (S2)
    ref names a commit other than <payload>    -> exit 1  superseded
    git cat-file -p <payload>    carries a parent          -> exit 2
    git ls-tree -r <payload>     lists other than one path -> exit 2
    path, date and key grammar                 (S3)        -> exit 2
    bytes = git cat-file blob <blob>; SHA-256(bytes) != sha256 -> exit 2
    **Key:** != key or **Base:** != base                   -> exit 2
    the file at <path> holds <bytes>  -> "unchanged", exit 0
    else temp file + os.replace       -> "written",   exit 0
```

The verb reads only git objects and the intake's four values. Every fact the record states was
decided by the walk that wrote it, so the landing has nothing to re-decide.

### Evidence

- Spec-48 S24 (:107-110) and AC20 (:305-307) are the re-derivation and the criterion it fails.
- Spec-6 §4 (:226-230) gives the stdin members, among them the `fields` that no reading produces.
- `drift_signals.py:476` sets `AUTO_MEMORY_DIR` to `~/.claude/projects/{checkout}/memory`, a per-user,
  per-checkout path, which is why a reading taken at the landing differs from the walk's
  (finding id 42).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `run_record_landing` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `land` | CLI verb of `maintenance.py` | none |
| `refs/gov/remote/maintain-record/<key>` | fetch cache namespace | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1 to S4
- `tools/drift-audit/selftest.py`: the cases of §6
- `tools/drift-audit/README.md`: S5
- `help/maintain.md`: S5

### Alternatives rejected

- **Re-derive only the rows the base determines.** The finding's skeptic tested it: the routes and
  `keys` members are still the walk's, so the digest still fails.
- **Re-run `maintenance.py write` over a carried stdin.** TOOL-dTendedCadence-49 §8 F1: the path's
  date, the record-when key and the clean-record rule are read again on the landing node.

## 5. Production-readiness checklist

- security — the write boundary is S3's: a commit of one path, under the home, its key a family's and
  its bytes the digest's, so a forged or moved payload writes nothing; the verb writes one file and
  commits nothing.
- perf / scale — a bounded fetch only when the object is absent, then three `git cat-file` reads.
- error / empty / loading states — a fetch that fails or passes its bound exits 1 with its line; each
  refusal of S3 exits 2 naming its check.
- observability — one `land —` line per run, naming the path and whether it changed.
- risks — a superseded payload's patch build ends with exit 1 and its line; the newer intake lands
  the newer record.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no landing intake exists at base.
- user docs — `help/maintain.md`, S5.

## 6. Acceptance criteria

The fixture is TOOL-dTendedCadence-49's: a scratch repository with a bare remote and one record
landed through `write_record_landing`, and a second clone of the bare remote as the patch build's
tree.

- **AC1** — When `python maintenance.py land` runs in the second clone with the recorded text's
  `--key`, `--base`, `--payload` and `--sha256`, it exits 0 printing `written`, the file at the
  record's path is byte-equal to the walk's, and a second run prints `unchanged`.
  Red when: the landed bytes differ from the walk's, or a re-run rewrites the file.
- **AC2** — When the walk's clone pushes a second record under the same key and the first text's
  values are landed, `land` exits 1 printing `superseded` and writes nothing.
  Red when: an older payload lands over a newer one.
- **AC3** — When `land` runs with a `--sha256` differing in one hex digit, with a payload commit
  planted with a parent, with one planted with two paths, and with one whose path names
  `2026-11-01/../x`, it exits 2 each time and writes nothing.
  Red when: a payload failing a check is written.
- **AC4** — When `python -c "import inspect, maintenance; print(inspect.getsource(maintenance.run_record_landing))"`
  runs in `tools/drift-audit/`, its output holds none of `drift_report`, `read_policy_value` and
  `datetime`, and `land` run with `HOME` and `USERPROFILE` set to an empty scratch directory writes
  the same bytes as AC1.
  Red when: the landing reads a reading, a policy key or the clock.
- **AC5** — When `grep -n "maintenance.py land" maintain.md` runs in `help/`, and the same over
  `tools/drift-audit/README.md`, each matches.
  Red when: a page omits the verb.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 AC4 · a second clone landing the first clone's payload, a moved ref and three planted bad payloads, staged against a landing that re-derives the readings · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 28 (BLOCKER, item B1) of the round-1
  spec audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 67, 68, 69, 70); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are unit 6's write boundary, the temp-file and `os.replace` write it shares with
`write_record` (`tools/runlog/record.py:1179-1201`), unit 35's `derive_record_family`, and the
claims' fetch into a private cache namespace (`read_claims`, `tools/unattended/unattended.sh:2118-2150`),
whose bounded fetch shape this verb ports. `python tools/codebase-map/reuse_lookup.py "carry a
written record to another node under a git ref and land it"` ranked `git`, `run_git`, `write_record`
and `read_landing_commit`; `write_record` is runlog's own kind and none verifies a carried payload,
so no existing seam fits beyond those.

Recall terms used: `python tools/memory-recall/query.py "how does a records-only patch build land a
maintenance record the walk wrote" --terms "records-only patch intake landing maintenance record refs
gov ref parentless commit digest re-derive"`
