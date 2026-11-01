# TOOL-dTendedCadence-68 — the record's push and the landing's fetch resolve their remote through drift-audit's own remote ladder, never a second exactly-one rule

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 21 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, item H5. Unit 49 S2 refuses a clone declaring other than one remote, porting
`resolve_claim_remote`'s exactly-one rule (`tools/unattended/unattended.sh:2097-2109`) into Python, and
unit 50 S2 fetches from "the one remote". drift-audit already carries the remote ladder inline and
gated, `resolve_remote(root)` (`tools/drift-audit/drift_report.py:3612-3664`, TOOL-dLadderedRemote-2:
`GOV_REMOTE`, then `branch.<current>.remote`, then the only remote), and `resolve_base_ref` in the same
file uses it (`:3696`). On a node with several remotes the landing raises every period while the rest of
the kit resolves fine, so no record from that node ever lands. This unit makes both halves ask the
ladder.

## 2. Scope (IN)

- **S1** — The walk's remote. `write_record_landing` (unit 49 S1) resolves its remote with
  `resolve_remote(root)`, imported from `drift_report` in the same kit directory, before the commit is
  built. A refusal raises `maintain — refused: <the ladder's refusal text>`; an empty remote with no
  refusal, a clone with no remote at all, raises `maintain — refused: no remote to carry the record
  to`; otherwise the push is made to the returned NAME (TOOL-dTendedCadence-65 S1). Unit 49 S2's
  exactly-one sentence and its citation of `resolve_claim_remote` are not built. Observed by AC1.
- **S2** — The landing's remote. `run_record_landing` (unit 50 S1) resolves its remote the same way and
  queries and fetches from the returned name (TOOL-dTendedCadence-69); a refusal or an empty remote
  exits 1 with the same text under its `land — refused:` prefix. Observed by AC2.

## 3. Non-goals (OUT)

- The ladder itself and its parity gate: TOOL-dLadderedRemote-2 and the resolver leg, unchanged.
- Extending that parity gate to refuse a second remote resolver: the report's left-shift gate, a gate of
  its own.
- The run-claim kit's exactly-one rule: `unattended.sh`, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-49` — S2's remote rule, which this unit answers with the kit's ladder
- **hands-off** `TOOL-dTendedCadence-50` — `run_record_landing`'s remote (S2), resolved by the same ladder
- **hands-off** `TOOL-dTendedCadence-65` — the remote name the record push is made to
- **hands-off** `TOOL-dTendedCadence-69` — the remote name the landing's freshness query and fetch are made to
- **hands-off** `TOOL-dTendedCadence-74` — the ladder, in whose terms the minors batch phrases unit 49 AC3's walk fixture (review id 31)

## 4. Design

```
remote, _branch, _observed, refusal = resolve_remote(root)    # drift_report.py:3613
refusal         -> raise / exit 1 with it
remote == ""    -> raise / exit 1 "no remote to carry the record to"
else            -> push to / query and fetch from <remote>
```

`import drift_report` from `maintenance.py` reads the module beside it; `drift_report.py` runs its CLI
only under `if __name__ == "__main__"` (`:4483`), so the import runs no audit. One copy of the ladder
stays in the kit, inside the block the parity gate holds byte-identical to `tools/lib/resolve_remote.py`
(`tools/lib/resolve-python.test.sh:182`).

### Inventory

Minted: nothing. `resolve_remote` is the kit's existing function, called from a second module.

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Keep the exactly-one rule.** A supported multi-remote node never lands a record, and the kit
  answers "which remote" two ways.
- **Copy the ladder into `maintenance.py`.** A second copy outside the parity gate, the defect's own
  shape.

## 5. Production-readiness checklist

- security — N/A — the remote is chosen by the same declared ladder the kit's base read uses.
- perf / scale — three `git` reads per resolution, as the ladder reads.
- error / empty / loading states — a refusal and a remote-less clone each raise or exit 1 with one
  line naming the cause.
- observability — the ladder's own refusal text names `GOV_REMOTE` and the listed remotes.
- risks — none beyond the ladder's own.
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no push or fetch of this ref exists at base.
- user docs — N/A — `GOV_REMOTE` is already documented with the ladder.

## 6. Acceptance criteria

The fixture is unit 49's scratch repository with its bare remote, plus a second bare remote.

- **AC1** — When `write_record_landing` runs with two remotes and no `GOV_REMOTE`, it raises with the
  ladder's `cannot choose a remote` text and neither bare remote gains a ref; with `GOV_REMOTE` naming
  the second, `git -C <second bare> for-each-ref refs/gov/maintain-record/` prints the ref; with no
  remote it raises `no remote to carry the record to`.
  Red when: a multi-remote node is refused although it names its remote, or a second resolver exists.
- **AC2** — When `python maintenance.py land` runs in a clone with two remotes and `GOV_REMOTE` naming
  the one holding the ref, it lands; with `GOV_REMOTE` unset it exits 1 with the ladder's text; and
  `grep -n '"remote"' maintenance.py` in `tools/drift-audit/` prints nothing, so no call lists the
  remotes itself.
  Red when: the landing picks its remote by a rule of its own.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · two bare remotes with and without `GOV_REMOTE`, and none, staged against the exactly-one rule · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 21 (HIGH, item H5) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

The seam is the kit's inline `resolve_remote(root)` (`tools/drift-audit/drift_report.py:3612-3664`),
called from `maintenance.py`. `python tools/codebase-map/reuse_lookup.py "resolve which git remote to
push to"` ranked name stems only, `git`, `resolve`, `resolve_kit_dir` and `run_git`, and missed the
ladder, which `git grep -l remote_ladder_py -- tools` finds in ten files, `drift_report.py` among them;
unit 49 §10 named neither, which is the finding.

Recall terms used: `python tools/memory-recall/query.py "which remote does drift-audit push a record
to" --terms "remote ladder resolve_remote GOV_REMOTE branch remote only remote multi-remote refusal
remote_ladder_py"`
