# DEPL-dGaugedVintage-5 — four kits an adopter cannot read a version out of

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`check-wiring`, `codebase-map`, `kickoff-manifest` and `playbook-render` carry a version constant and
zero `gov:kit` markers anywhere. `tools/check-kit-versions.sh:84` calls the marker the thing a
deployer reads a kit's version from in an adopting tree, so for these four that read returns nothing.

## 2. Scope (IN)

- **S1** — A `gov:kit <id>@<version>` marker added to one shipped file per affected entry, chosen so
  an adopter who installs that entry always receives the marker.
- **S2** — A `selfcheck` arm asserting that every entry declaring a version constant has at least one
  marker inside its own resolved file set. An entry declaring `version_from.none` is exempt by that
  declaration, not by omission.
- **S3** — The exemption for `playbook`, which versions by a `governance-template: vN.N` marker
  rather than `gov:kit`, declared in the descriptor rather than special-cased in the checker.

## 3. Non-goals (OUT)

- The stale drift-audit values. That is `DEPL-dGaugedVintage-4`, which owns the derivation this unit
  asserts against and is ordered beside it.
- Adding a constant to any of the ten entries that declare `version_from.none` with a reason. Their
  declaration is the answer and this unit does not overturn it.
- Deciding WHICH file carries the marker for each of the four. That is F1 and it is per-entry.
- Changing `check-kit-versions.sh`'s `need` list. S2 lives in `selfcheck`, where the registry is.

## 4. Design

### Inventory

| Entry | Constant | Markers today | Candidate carrier |
|---|---|---|---|
| `check-wiring` | `tools/check-wiring.sh:20` | none | the same file's header |
| `codebase-map` | `tools/codebase-map/map_lib.py:48` | none versioned | `map_lib.py`; `:46` has a bare `gov:kit codebase-map` with no `@` |
| `kickoff-manifest` | `skills/session-kickoff/manifest-check.sh:21` | none | the checker, which lands as `tools/manifest-check.sh` |
| `playbook-render` | `tools/playbook/render_playbook.py:621` | none | the renderer |

`codebase-map` is the interesting one: it already carries the marker's PREFIX with no version, so a
deployer grepping `gov:kit codebase-map@` finds nothing while a reader skimming finds something that
looks like a marker.

### Rollout

S1 and S2 land together. Arming S2 first would red the bar on all four until S1 lands, and a gate
whose steady state is red gets bypassed.

### Alternatives rejected

Placing every marker in each kit's README was rejected: `memory-recall` already does that and
`DEPL-dGaugedVintage-3`'s adopter shows a README is not guaranteed to be what a fork carries. The
carrier should be a file the entry cannot function without.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — S2 is a grep per entry over an already-resolved file set.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry with a `version_from.none` declaration must be reported
  as exempt-by-declaration, never skipped silently, so the exempt set stays visible.
- observability — `selfcheck` prints the per-entry marker count.
- risks — a marker placed in a file an adopter does not receive would satisfy S2 while failing its
  purpose, which is why S2 asserts membership of the RESOLVED set rather than mere existence.
- testing + left-shift gates — S2 is the gate; AC3 is its failing case.
- migration / rollback — none. Adding a comment marker changes no behaviour.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs after this unit, all four entries
  report a marker count of at least 1 and the command exits 0.
- **AC2** — When a deployer greps `gov:kit check-wiring@` in a tree that installed only that entry,
  the grep returns the entry's current version, observed on a scratch `apply` target.
- **AC3** — When the new marker is deleted from any one of the four, `python
  tools/govkit/govkit.py selfcheck` exits non-zero and names that entry, observed by staging the
  deletion and restoring it.
- **AC4** — When an entry declares `version_from.none`, the same run reports it exempt with its
  declared reason rather than omitting the row.
- **AC5** — The `codebase-map` bare `gov:kit codebase-map` token at `map_lib.py:46` either gains an
  `@<version>` or is shown by `bash tools/check-kit-versions.sh` to be distinguishable from a real
  marker.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `kit version markers`.

## 8. Open questions

- **F1 — the carrier file per entry.** The table in §4 proposes one each. `kickoff-manifest` is the
  awkward one: its constant lives under `skills/` and lands at `tools/manifest-check.sh`, so the
  marker must survive that relocation. Recommendation: the constant's own file in every case, on the
  line above the constant, so the two move together. Unresolved.
- **F2 — whether `playbook`'s separate convention should be unified.** It uses
  `governance-template: vN.N` and `WIRE-INTO-PROJECT.md:87` documents that. Unifying means two
  markers on one file or a migration of every adopter's grep. Recommendation: declare the exception
  in the descriptor per S3 and leave the convention alone. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- The seam is the same one `DEPL-dGaugedVintage-4` extends — `read_descriptors` and `selfcheck`
  check 5b in `tools/govkit/govkit.py`, which already walks every entry's declared version file;
  `python tools/codebase-map/reuse_lookup.py "assert every gov kit version marker site against its
  descriptor"` ranks it first. This unit adds an arm to that walk rather than a second walk.
- Recall terms used: `gov:kit marker population derive descriptor kit.toml check-kit-versions
  verdict-epoch remedy carriers bump sites`
