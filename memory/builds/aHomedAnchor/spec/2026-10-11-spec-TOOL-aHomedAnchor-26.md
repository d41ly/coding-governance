# TOOL-aHomedAnchor-26 — the F4 filer harness initialises the driver globals the filer appends to

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-19

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Driver shard 8/8 is red on the F4 arm: the sliced filer appends to `WI_STAGED`, a driver global
`TOOL-dUnstuckLanding-27` added, and the arm's harness never initialises it, so `set -u` kills the
filer after the row write and before the views helper is called.

## 2. Scope (IN)

- S1. `run_f4_filer` in `tools/unattended/unattended.test.sh` declares `WI_STAGED` and `AV_STAGED`
  empty beside its other locals, with a comment naming why. Observed by AC1.

## 3. Non-goals (OUT)

The filer itself, which is correct; running the driver suite's shards (owner, 2026-10-11).

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`.
Reproduced by a slice of the F4 block, which printed `WI_STAGED: unbound variable` after
`gates-green: filed ask ARCH-tRun-2`.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`

## 6. Acceptance criteria

- **AC1** — When the F4 block is sliced with the suite's prologue and run, it prints `SLICE-PASS`
  with no `unbound variable`. Red when: either global is left unset.

## 7. Gates

`unattended kit gate`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits: the harness already declares its other driver globals as locals, and this
extends that list. Recall terms used: `--terms "F4 filer write_inherited_asks WI_STAGED AV_STAGED set -u unbound slice_fn views helper"`.
