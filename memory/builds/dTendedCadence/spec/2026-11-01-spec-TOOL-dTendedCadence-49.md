# TOOL-dTendedCadence-49 — the written maintenance record carried unchanged to its landing, a parentless commit pushed under `refs/gov/maintain-record/<key>` and named by the landing intake

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-49-deviation-491.md](../build/2026-11-01-build-TOOL-dTendedCadence-49-deviation-491.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-49-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-49-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-49-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-49-promoted-fix-brief.md) | research | TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
BLOCKER, which shares item B1 with id 28 (TOOL-dTendedCadence-50) and id 42 (TOOL-dTendedCadence-51).
Unit 48 S24 has the records-only patch build re-derive the readings with `drift_report.py
--readings` at the base and refuse a digest that differs (spec-48:107-110). Unit 37 writes an
`over-pin:` line only for a reading whose stdin `route` is the walk's outcome (spec-37 S1, S2,
:28-35), and `--readings` emits the row's declared route instead (spec-8 S5, :54-57, :185). So either
every landing is refused, or the landed record carries no `over-pin:` line and the red leg reads green
while offenders stand. This unit removes the re-derivation at its source: the walk carries the record
it wrote, byte for byte, under a ref, and the landing intake names that ref's commit and the record's
digest.

## 2. Scope (IN)

- **S1** — The payload. `write_record_landing(root, path, key, base, filer)` in
  `tools/drift-audit/maintenance.py` reads the bytes of the record at `path`, the file
  `write_maintenance_record` wrote under the home, and builds one parentless commit whose tree holds
  that one file at its repository path. The commit's message is `gov-maintain-record <key>`, and its
  author and committer are `gov-maintain-record <gov-maintain-record@invalid>` at
  `1970-01-01T00:00:00Z`, so its sha depends on the path, the bytes and the key alone. Observed by AC1
  and AC2.
- **S2** — The push. It pushes `<commit>:refs/gov/maintain-record/<key>` to the clone's one remote,
  forced, as `write_claim` pushes `<commit>:refs/gov/runs/<slug>` (`tools/unattended/unattended.sh:2419-2422`),
  bounded at 30 s. A clone declaring other than one remote is refused before the commit is built, the
  rule `resolve_claim_remote` states (`unattended.sh:2097-2109`). Observed by AC1 and AC2.
- **S3** — The intake. After the push, it files `python <runtime>/intake.py file --origin cadence
  --filer <filer>` with §4 "The intake" on stdin and returns the filing's answer, `filed` or `seen`. A
  refused push or filing raises with its line. Observed by AC1 and AC3.
- **S4** — The walk's call. `item.maintain.record` (unit 1 S6) calls `write_record_landing(root,
  <written path>, key, base, "item.maintain.record")` once the record is written, in place of the text
  carrying the readings as JSON, and files nothing when no record was written. A raise exits the walk
  1, so the lease is handed over (unit 1 S2). Observed by AC3.
- **S5** — The docs. The maintenance record section of `tools/drift-audit/README.md` and the section
  "The Maintain run" of `help/maintain.md` name the ref, the four lines and the verb that lands them,
  `maintenance.py land` (TOOL-dTendedCadence-50). Observed by AC4.

## 3. Non-goals (OUT)

- Landing the payload: TOOL-dTendedCadence-50, which verifies and writes it in the patch build's tree.
- The round-trip arm over walk, intake and landing: TOOL-dTendedCadence-51.
- The security review's landing through this seam: TOOL-dTendedCadence-52.
- The stdin refusals of `maintenance.py write`: unit 48 S24's second half, unchanged.
- Deleting a landed ref: the `ponytail:` ceiling of §5.

### Edges

- **consumes-from** `TOOL-dTendedCadence-48` — S24's landing intake, whose readings digest and re-derivation this unit replaces with the written record carried unchanged
- **consumes-from** `TOOL-dTendedCadence-1` — `item.maintain.record` and its landing filing (S6), which this unit's seam performs with the written path
- **hands-off** `TOOL-dTendedCadence-50` — `refs/gov/maintain-record/<key>`, its one-path commit and the four-line text, which `maintenance.py land` reads and verifies
- **hands-off** `TOOL-dTendedCadence-51` — `write_record_landing`, the walk half of the round trip that unit's arm drives end to end
- **hands-off** `TOOL-dTendedCadence-52` — `write_record_landing`, through which the security review files its record's landing
- **hands-off** `TOOL-dTendedCadence-59` — `write_record_landing`, through which that unit lands one record of every family and documents the one grammar (review ids 5, 24)
- **hands-off** `TOOL-dTendedCadence-64` — `write_record_landing`'s push, which that unit wraps in the claim-push lock and the lander's marker test (review id 5)
- **hands-off** `TOOL-dTendedCadence-65` — the push, which that unit makes by remote name with the hook's refusal token read (review id 26)
- **hands-off** `TOOL-dTendedCadence-66` — §6's scratch repository, which that unit equips with the tracked hooks (review id 37)
- **hands-off** `TOOL-dTendedCadence-67` — the blob and tree lines of §4, which that unit builds through a scratch index over an unfiltered blob (review id 13)
- **hands-off** `TOOL-dTendedCadence-68` — S2's remote rule, which that unit answers with the kit's remote ladder (review id 21)
- **hands-off** `TOOL-dTendedCadence-74` — the security claim, its precondition edge, AC3's fixture, the push citation and the ref-name check, repaired by the minors batch (review ids 18, 32, 31, 19, 39)

## 4. Design

### The payload commit

```
write_record_landing(root, path, key, base, filer):
    derive_record_family(key) is None          -> raise   (TOOL-dTendedCadence-35)
    the clone declares other than one remote   -> raise
    blob   = git hash-object -w <path>
    tree   = git mktree   <- "100644 blob <blob>\t<path relative to root>"
    commit = git commit-tree <tree> -m "gov-maintain-record <key>"
             (GIT_AUTHOR_* and GIT_COMMITTER_* fixed as S1 states)
    git push --porcelain --force <remote> <commit>:refs/gov/maintain-record/<key>   (30 s)
    sha256 = SHA-256 of the bytes at <path>
    answer = intake.py file --origin cadence --filer <filer>  <- the four lines
    print "maintain — <key> · <filer> · landing <commit12> · <answer>"
```

A ref that names a commit, never a bare blob, is deliberate. The publishing boundary scans every
`refs/gov/*` update by the commits the update carries and every blob they add
(TOOL-dWellOiledMachine-17 S7, S8), and a ref naming a blob carries no commit for that scan to read.

### The intake

```
land maintenance-record <key>
base: <base, 40 hex>
payload: <commit, 40 hex>
sha256: <SHA-256 of the record's bytes, 64 hex>
```

Equal record bytes give an equal commit and an equal text, so a re-run that writes the same record
appends a receipt to the intake on record. A record that differs files a new intake.

### Evidence

- Spec-1 S6 (:92-100) files the landing with the record's key, base and readings as JSON, and spec-48
  S24 adds the digest and the re-derivation.
- Spec-6 §4 makes the path `<MEMORY_ROOT>/maintenance/<date>-maintenance-<key>.md`, `<date>` the UTC
  day of the write, so a write repeated on another day names another file (§8 F1).
- `write_claim` (`unattended.sh:2396-2440`) builds a parentless commit with a fixed identity and pushes
  it to one `refs/gov/` name, with no local ref.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `write_record_landing` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `refs/gov/maintain-record/<key>` | ref namespace on the one remote | none |
| `gov-maintain-record` | commit message head and identity | none |
| `payload:`, `sha256:` | intake text lines | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2, S3
- `tools/drift-audit/maintain.py`: S4
- `tools/drift-audit/selftest.py`: the cases of §6
- `tools/drift-audit/README.md`: S5
- `help/maintain.md`: S5

### Alternatives rejected

- **The readings JSON in the intake text.** The intake text is redacted and cut to `INTAKE_CAP_BYTES`
  (TOOL-dWellOiledMachine-4 S2), so a large period's readings are cut, and a redacted value changes
  the bytes the digest covers.
- **A local ref only.** A patch build placed on another node reads no ref of this node's.

## 5. Production-readiness checklist

- security — a new pushed ref class under `refs/gov/`. Its one blob is the record the patch build
  commits anyway, so it publishes nothing the landing does not, and it passes the publishing
  boundary's secret scan as every `refs/gov/*` push does. The key is held by `derive_record_family`
  and the path by `write_maintenance_record`'s containment under the home.
- perf / scale — one hash-object, mktree, commit-tree and bounded push per written record;
  `maintain.record-when: on-finding` bounds the count.
- error / empty / loading states — a push that fails or passes its bound, and a refused filing, each
  raise with their line, and the walk exits 1; no record written files nothing.
- observability — S3's line names the commit and the filing's answer.
- risks — one ref per key stays on the remote, about 366 a year for `daily`; `ponytail:` ceiling,
  the upgrade is the landing deleting its ref once committed. A re-run with different bytes moves the
  ref, and the older intake's landing is refused as superseded (TOOL-dTendedCadence-50 S2).
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no ref under `refs/gov/maintain-record/` exists at base.
- user docs — `help/maintain.md`, S5.

## 6. Acceptance criteria

The fixture is a scratch repository under `%TEMP%` with a short name, its one remote a scratch bare
repository, holding a copy of `tools/drift-audit/` and a stub `intake.py` that records its stdin and
answers `filed`.

- **AC1** — When `python maintenance.py write --key 2026-11-01 --base <sha>` writes a record and
  `write_record_landing` runs on its path, `git -C <bare> cat-file -p
  refs/gov/maintain-record/2026-11-01` prints a commit with no `parent` line, its tree lists the
  record's path alone, that blob is byte-equal to the written file, and the recorded text's `sha256:`
  value equals `sha256sum` of the file.
  Red when: the ref is not pushed, the commit carries a parent or a second path, or the digest covers
  other bytes.
- **AC2** — When `write_record_landing` runs twice over the same record, the two `payload:` values and
  the two recorded texts are byte-equal; after a one-byte change to the record both differ; in a clone
  with two remotes it raises and `git -C <bare> for-each-ref refs/gov/` prints nothing new.
  Red when: a date or an identity reaches the commit, or a clone with two remotes is pushed to.
- **AC3** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py` runs over unit 1's walk fixture with
  unit 6's writer in place of the record stub, the recorded text's first line is `land
  maintenance-record 2026-11-01`, it holds no `{`, and `git rev-list --count HEAD` is unchanged; under
  `record-when = "on-finding"` with nothing found, nothing is recorded and no ref is pushed.
  Red when: the walk files the readings as JSON, files a landing for an unwritten record, or commits.
- **AC4** — When `grep -n "refs/gov/maintain-record" README.md` runs in `tools/drift-audit/`, and the
  same over `maintain.md` in `help/`, each matches.
  Red when: a page omits the ref.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · a scratch repository with a bare remote and a recording intake stub, staged against a landing text carrying the readings · none

## 8. Open questions

- **F1 — What does the landing carry?** Options: (a) the record bytes the walk wrote; (b) the walk's
  stdin JSON, re-run through `maintenance.py write` at the landing, the report's corrected fix; (c)
  readings re-derived at the base, unit 48 S24 as written. (c) is the defect. (b) runs the writer on
  the landing node: the path's `<date>` is that node's UTC day (spec-6 §4), `maintain.record-when` is
  read there, and TOOL-dTendedCadence-43 S5's clean-record rule reads that node's newest committed
  record, three readings of the landing node's clock and state, which is the dependence id 42 names.
  (a) carries what the walk decided. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the
  survivor that makes the landed record byte-equal by construction. widens: none · relaxes: none
- **F2 — One ref per key, or one per payload?** Options: (a) `refs/gov/maintain-record/<key>`, moved
  by a re-run; (b) `refs/gov/maintain-record/<key>/<commit12>`, never moved. (b) leaves a ref per run
  and nothing reads the older ones once a newer record lands. RESOLVED (agent, 2026-11-01, delegated):
  (a), rung 3, with the older intake refused as superseded at its landing. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (BLOCKER, item B1) of the round-1
  spec audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 64, 65, 66, 67, 68, 74); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `write_claim`'s parentless commit pushed to one `refs/gov/` name
(`tools/unattended/unattended.sh:2396-2440`) and its one-remote rule (`resolve_claim_remote`,
`:2097-2109`), whose shape this unit ports to Python beside unit 6's writer, and unit 1 S6's filing
call. `python tools/codebase-map/reuse_lookup.py "carry a written record to another node under a git
ref and land it"` ranked `git`, `run_git`, `records`, `write_record` (`tools/runlog/record.py`) and
`read_landing_commit` (`tools/unattended/lib-unattended.sh`); none pushes a record under a ref from
Python, and drift-audit is copy-installed, so it calls neither shell helper, and no existing seam fits
beyond the claim's shape.

Recall terms used: `python tools/memory-recall/query.py "how does a records-only patch build land a
maintenance record the walk wrote" --terms "records-only patch intake landing maintenance record refs
gov ref parentless commit digest re-derive"`
