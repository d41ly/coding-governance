# TOOL-dSafePassage-21 — the step gate's `file` class reads gov's planned destinations when no source receipt is on the tree

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-21-deviation-67.md](../build/2026-10-23-build-TOOL-dSafePassage-21-deviation-67.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-21-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-21-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 5** at HIGH, its item **D-5**; the same defect seen by another lens is id 43
at MEDIUM, item D-27, which the minors batch `TOOL-dSafePassage-26` carries. TOOL-dSafePassage-10's
`file` class reads `.governance/install.json` (its spec, §4, line 108), an empty class at the tip
exits 2 (:156-157), and its AC1 and AC12 need a non-zero count in every class on the tree after the
pass. TOOL-dSafePassage-8 writes that receipt only at the lander, never from a branch (its spec, §3
and Files touched, lines 96-97 and 218), and `git ls-files .governance` lists only
`.governance/deploy.toml` at the base, so the class is empty at every pass. This unit is id 5's
promotion, the first branch of the report's fix: when the tree carries no source receipt, the class
reads the destinations gov's accepted plan derives, the population the receipt's `files` rows record.

## 2. Scope (IN)

- **S1** — One derivation of gov's destinations. `read_plan_destinations(root)` in
  `tools/govkit/govkit.py` returns the destination of every row `planned_writes`
  (`tools/govkit/govkit.py:3988`) derives for gov's own `.governance/deploy.toml` and selection over
  gov's own tree. TOOL-dSafePassage-8's source-mode rewrite of `files` calls it, so the receipt's rows
  and this class read one derivation. Observed by AC3.
- **S2** — The class's two sources. `read_file_members(root)` in `tools/govkit/step_gate.py` returns
  each `files` row's `path` when the tree carries a receipt with `"mode": "source"`, and
  `read_plan_destinations(root)` otherwise, each spelled under the `{prefix}` rule of
  TOOL-dSafePassage-10 §4. The empty-class refusal is unchanged. Observed by AC1 and AC2.
- **S3** — Every member, either way. The member set read from a source receipt that
  `update --target . --write` just wrote equals the set read from the plan on the same tree.
  Observed by AC3.

## 3. Non-goals (OUT)

- The prepared-merge observation of TOOL-dSafePassage-10's AC12 and its Rollout sentence:
  `TOOL-dSafePassage-26`'s item for id 43.
- The other eight classes and the gate's verdict.
- Accepting gov's plan, which is TOOL-dSafePassage-8's S3.

### Edges

- **consumes-from** `TOOL-dSafePassage-10` — `tools/govkit/step_gate.py`, its `file` class reader and the class registry; without them there is no class to give a second source
- **consumes-from** `TOOL-dSafePassage-8` — gov's accepted plan and the source-mode rewrite of the receipt's `files`, the call site the derivation is extracted from; without them `plan --target .` refuses and the class has no rows to read
- **hands-off** `TOOL-dSafePassage-26` — the observation on a prepared-merge fixture that carries a receipt, and the Rollout sentence that says the receipt arrives only in the one landing
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which filters gov's planned destinations to the rows apply lands and makes the plan the file class's one source

## 4. Design

### Data model

| Tree | `file` members |
|---|---|
| `.governance/install.json` with `"mode": "source"` | each `files` row's `path` |
| no receipt, or one without `"mode": "source"` | each destination `read_plan_destinations` returns |

A path is spelled `{prefix}/...` under the tool root, as every path-valued member is.

### Inventory

Minted: `read_plan_destinations` in `tools/govkit/govkit.py` (cell `py.function`, verb `read`, OK by
`python tools/lexicon/lexicon.py --suggest read_plan_destinations --as py.function` on 2026-10-23).
`read_file_members` is TOOL-dSafePassage-10's reader, changed here. No conf key, no gate leg, no
policy key.

### Migration

None: no adopter runs the gate.

### Rollout

Live at landing. It builds at order 5, after TOOL-dSafePassage-10 (order 4) and TOOL-dSafePassage-8
(order 3). TOOL-dSafePassage-10's AC1 and AC12 hold on the branch from this unit's pass on, and the
close's acceptance re-check reads them then; they cannot hold at TOOL-dSafePassage-10's own pass,
which this repair follows.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/step_gate.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Observing the gate only on the prepared merge**, the report's second branch. The leg is
  unguarded and runs on every bar, so a bar run on the branch between TOOL-dSafePassage-10's commit
  and the landing would exit 2 on an empty class.
- **Committing a source receipt from a branch.** TOOL-dSafePassage-8 §3 refuses it: the landing's own
  walk would also write it.

## 5. Production-readiness checklist

- security: read-only; `planned_writes` writes nothing.
- perf / scale: one plan derivation per gate run on a tree without a receipt, the cost of
  `plan --target .`.
- error / empty / loading states: a plan that refuses is the reader raising, which the gate's
  reader contract (`TOOL-dSafePassage-26`'s item for id 66) turns into exit 2 naming the class.
- observability: `--list` prints the `file` count, whichever source it read.
- risks: the two sources drift if TOOL-dSafePassage-8's writer stops calling the one derivation;
  AC3's parity observes it.
- testing: the probes of §6 and the arm of §7.
- migration: none.
- user docs: N/A — `help/step-gate.md` names the class, not its source.

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/step_gate.py" --list` runs on the branch after this pass,
  which carries no `.governance/install.json`, the `file` line prints a non-zero member count, and so
  does every other class line.
  Red when: the `file` class reads only the receipt and the gate exits 2 on an empty class.
- **AC2** — When `python "tools/govkit/step_gate.py" --fixture --plant file` runs, it still exits 1
  naming one `file:` member, and 0 with `--with-row`.
  Red when: the plan-read class sees no vanish the receipt-read one would.
- **AC3** — When a probe in a scratch clone of gov runs `python tools/govkit/govkit.py update --target . --write`
  and then calls `read_file_members` with the written receipt present and again with it removed, the
  two member sets are equal, and `git grep -n -e "def read_plan_destinations" -e "read_plan_destinations(" -- tools/govkit`
  prints one definition and the two callers.
  Red when: the receipt's rows and the plan's destinations differ, or the receipt writer derives its
  rows a second way.
  fixture: a scratch clone under `%TEMP%`, after TOOL-dSafePassage-8 is built.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 · the arm runs the gate's `file` plant with and without `--with-row` and the two-source parity over a scratch clone, its failing case staged by a reader copy that reads the receipt alone · none

The step gate's own leg re-observes AC1 at the close, through TOOL-dSafePassage-10's `New arm:` line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 5 (HIGH, item
  D-5; id 43, item D-27, is the same defect at MEDIUM, carried by `TOOL-dSafePassage-26`).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-35`; no other section moved.

## 10. Reuse audit

The seam extended is `planned_writes` (`tools/govkit/govkit.py:3988`), the one derivation of what a
plan writes, which `cmd_plan` already calls (`tools/govkit/govkit.py:5030`), wrapped for gov's own
deploy file and called by TOOL-dSafePassage-8's writer and TOOL-dSafePassage-10's reader alike.
`python tools/codebase-map/reuse_lookup.py "list the planned destinations of an accepted deploy plan"`
ranked `plan` (`gen_build_index.py`), `read_id_list`, `declared_list`, `outcome_accepted` and
`plan_state`, none a deploy plan's destinations; the probe does not rank `planned_writes`, which this
unit found by reading `cmd_plan`, so the hits and the source disagree there.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
