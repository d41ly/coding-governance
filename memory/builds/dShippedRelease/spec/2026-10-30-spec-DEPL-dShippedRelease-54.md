# DEPL-dShippedRelease-54 — `emitted ci pins` grades row use only over a `--workflow`, so an adopter's base argv is green

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 28 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 57 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, item B4, which stands beside id 7 (DEPL-dShippedRelease-57). Unit 8 S4's third bullet reds
any row used by neither a template nor a `--workflow` file. `upload-artifact` appears in gov's
workflow alone, and `--workflow` is passed only under `[gate_leg.gov]`, so `ci_emit.py check` with
no `--workflow` always exits 1 and the shipped leg is red at every adopter holding the kit. This
unit scopes the arm to the case it can answer.

## 2. Scope (IN)

- **S1** — The arm. `check_rows_used(rows, files)` in `tools/integrations/ci/ci_emit.py`, the third
  bullet of unit 8 S4, runs only when `--workflow` is passed. Without it `check` prints
  `row use — not graded · no --workflow` and the arm adds no finding, so a skip reads as a skip and
  never as coverage. Observed by AC1.
- **S2** — The other two bullets of S4 grade as they did: every `uses:` of a template, and
  `permissions:`. Observed by AC2.
- **S3** — The adopter's run. `tools/run-gates/adopt-run-gates.test.sh`'s scratch target runs the
  leg's base argv and reads exit 0, so a leg shipped to adopters is seen green where it ships.
  Observed by AC1 and the arm of §7.

## 3. Non-goals (OUT)

- The fixture's baseline and the criteria that rest on it: DEPL-dShippedRelease-57.
- Splitting `action-pins.toml` into template pins and gov-only pins: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-8` — `ci_emit.py check`, `action-pins.toml` and the two legs, without which there is no arm to scope
- **hands-off** `DEPL-dShippedRelease-57` — `check_rows_used` and the printed skip, under which that unit restates the row criteria

## 4. Design

### Evidence

- Unit 8 S1 declares three rows; S2's template carries `{{ACTION_CHECKOUT}}` alone; unit 26 adds `{{ACTION_SETUP_PYTHON}}`.
- `.github/workflows/remote-ci.yml` uses `actions/upload-artifact`, a file only gov's tree holds, as unit 8 S5 says.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_rows_used` | function, `tools/integrations/ci/ci_emit.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/integrations/ci/ci_emit.py`: S1
- `tools/run-gates/adopt-run-gates.test.sh`: S3's assertion

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — the skip line on every run with no `--workflow`.
- risks — an adopter's stale row goes unread, which costs nothing there, since the declaration ships
  from gov and gov's leg grades it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py check --root <scratch copy>` runs with no `--workflow` and no
  plant, it exits 0 and prints `row use — not graded · no --workflow`.
  Red when: the base argv exits 1, so the leg is red at an adopter holding the kit.
  fixture: a scratch copy of the integrations kit under `%TEMP%`.
- **AC2** — When `check` runs with a template's checkout line planted as
  `uses: actions/checkout@v6`, it exits 1 naming the file and line.
  Red when: scoping the row arm also blinded the `uses:` arm.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/run-gates/adopt-run-gates.test.sh · covers AC1 · a scratch target holding the integrations kit, its failing case the arm run with no `--workflow` · none

## 8. Open questions

- **F1 — Scope the arm or split the declaration?** Options: (a) grade row use only over a
  `--workflow`; (b) split rows into template pins and gov-only pins. (b) puts two tables behind one
  reader for one row's sake, and a gov-only row still needs a reader at gov. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3, the audit's corrected first branch. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 57 (BLOCKER, item B4) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-8's `ci_emit.py check`.
`python tools/codebase-map/reuse_lookup.py "pin third party action uses lines by sha in a workflow and check them"`
ranked name-stem helpers (`check`, `check_line`, `load_workflows`) and no pin reader, since the
module is specced and unbuilt, so no existing seam fits apart from that parent. The recall probe
surfaced unit 8 itself and the shape audit's row on gov's own workflow, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how are emitted ci action pins graded for an adopter that holds no workflow file" --terms "action pins uses sha workflow emitted ci adopter rendered outcome stopped_ok gate leg"`
