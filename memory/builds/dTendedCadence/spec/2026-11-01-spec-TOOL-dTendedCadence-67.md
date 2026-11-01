# TOOL-dTendedCadence-67 — the record payload's tree built through a scratch index over an unfiltered blob, so a nested path builds and both digests cover one byte string

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-67-deviation-671.md](../build/2026-11-01-build-TOOL-dTendedCadence-67-deviation-671.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md) | research | TOOL-dTendedCadence-60 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 13 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, item H4. Unit 49 §4 builds the payload tree with one `git mktree` line naming the record's path
relative to the root (spec-49:79-80). `git mktree` refuses a name holding a slash and every record path
is nested (`memory/maintenance/<date>-maintenance-<key>.md`), so `write_record_landing` raises on every
record and no landing is ever filed. Separately, `git hash-object -w <path>` runs the path's clean
filter while `sha256` is taken over the raw bytes, so a record holding a CR has two digests over two
byte strings and unit 50 S3 refuses it. This unit builds the tree a way git accepts and hashes the
bytes it digests.

## 2. Scope (IN)

- **S1** — The blob. `write_record_landing` hashes the record with `git hash-object -w --no-filters
  <path>`, so the blob is the file's bytes as written, and `sha256` is taken over those same bytes.
  Observed by AC1 and AC2.
- **S2** — The tree. `build_record_tree(root, blob, rel)` in `tools/drift-audit/maintenance.py` writes
  a scratch index `<git-dir>/maintain-record.<pid>.index`, runs `GIT_INDEX_FILE=<scratch> git
  update-index --add --cacheinfo 100644,<blob>,<rel>` and then `GIT_INDEX_FILE=<scratch> git
  write-tree`, and returns the tree; the scratch index is unlinked in a `finally`. `<rel>` is the
  record's path relative to the root in POSIX form, `PurePosixPath`, never a backslash. Observed by
  AC1.
- **S3** — The probe recorded. §4 Evidence records the scratch-repository run of S1 and S2 over a
  nested path and a CR byte, the probe unit 49's mktree line never had. NOT OBSERVED by a criterion of
  its own: it is this spec's evidence, re-run by AC1.

## 3. Non-goals (OUT)

- The commit, the push and the intake text: unit 49, TOOL-dTendedCadence-64 and -65, unchanged.
- How the patch build's own commit stores the landed file: its `.gitattributes` normalise what it
  commits, which unit 50's landing does not control (§5 risks).

### Edges

- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`'s blob and tree lines (§4 "The payload commit"), which this unit replaces with a scratch-index build over an unfiltered blob
- **hands-off** `TOOL-dTendedCadence-50` — a payload blob holding the record's raw bytes, so the landing's SHA-256 over the blob equals the walk's over the file

## 4. Design

```
blob = git hash-object -w --no-filters <path>
idx  = <git-dir>/maintain-record.<pid>.index
GIT_INDEX_FILE=idx git update-index --add --cacheinfo 100644,<blob>,<posix rel>
tree = GIT_INDEX_FILE=idx git write-tree          ; finally: unlink idx
sha256 = SHA-256 of the bytes at <path>           # == the blob's bytes, by S1
```

A scratch index builds every parent tree in one `write-tree`, where a hand-rolled mktree needs one
call per path segment. The index file sits in the git dir, never in the work tree, so the walk leaves
no tracked file dirty, and its pid suffix keeps two walks of one git dir apart.

### Evidence

- `git mktree` over `100644 blob <b>\tmemory/m/f.md` prints `fatal: path memory/m/f.md contains
  slash`, rc 128 (finding id 13's probe).
- Probe at writing, 2026-11-01, a scratch repository under `%TEMP%` with `core.autocrlf=true` and
  `memory/** text eol=lf`, the record `a\r\nb\n` at
  `memory/maintenance/2026-11-01-maintenance-2026-11-01.md`: `hash-object --no-filters` gave
  `4565b4dc`, filtered `hash-object` gave `422c2b7a`, so the filter changes the blob; the scratch-index
  `update-index --cacheinfo` and `write-tree` gave a tree whose `ls-tree -r` lists that one nested
  path; `cat-file blob` printed the CR, and `sha256sum` of the file and of the blob agreed.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `build_record_tree` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `maintain-record.<pid>.index` | scratch index in the git dir | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **One mktree per path segment.** Three calls for `memory/maintenance/<file>`, and the segment loop is
  code the index already is.
- **Take `sha256` over the filtered blob.** The landed bytes would then differ from the walk's file,
  and unit 49's byte-equality claim would fail by construction.

## 5. Production-readiness checklist

- security — N/A — no new input; the path is `write_maintenance_record`'s, contained under the home.
- perf / scale — two plumbing calls in place of one, per written record.
- error / empty / loading states — a plumbing call that fails raises with git's line, and the scratch
  index is unlinked on every path.
- observability — unchanged: unit 49 S3's line names the commit.
- risks — the patch build commits the landed file through its own attributes, so a CR byte in a record
  is normalised in the committed blob even though the landing wrote the walk's bytes. Whether unit 6's
  writer can emit a CR from a reading value is UNVERIFIED: unit 6 is unbuilt at base.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no payload exists at base.
- user docs — N/A — internal plumbing.

## 6. Acceptance criteria

The fixture is unit 49's scratch repository.

- **AC1** — When `write_record_landing` runs on the fixture's record dated and keyed 2026-11-01,
  nested under `memory/maintenance/`, `git -C <bare> ls-tree -r
  refs/gov/maintain-record/2026-11-01` lists that one path, and no file `maintain-record.*.index`
  remains in the git dir.
  Red when: a nested path is refused, or the scratch index is left behind.
- **AC2** — When the record holds a CR byte and the fixture sets `core.autocrlf=true` with `text
  eol=lf` on `memory/`, `git cat-file blob` of the pushed blob is byte-equal to the file, and its
  `sha256sum` equals the recorded `sha256:` value.
  Red when: a clean filter changes the blob, so the two digests differ.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · a nested record path and a CR byte under a CRLF-normalising config, staged against the one-line mktree and a filtered hash · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 13 (HIGH, item H4) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "build a git tree object for one nested file path"` ranked
name stems only, `git`, `tree`, `build`, `run_git` and `build_commit`
(`tools/unattended/lib-unattended.sh`, shell), none a builder of a nested tree from Python, so no
existing seam fits; git's own index is the seam this unit uses.

Recall terms used: `python tools/memory-recall/query.py "how is the payload commit of a maintenance
record built" --terms "payload commit mktree update-index cacheinfo write-tree hash-object no-filters
autocrlf sha256 nested path"`
