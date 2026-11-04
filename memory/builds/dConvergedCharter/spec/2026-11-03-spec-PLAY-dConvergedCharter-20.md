# PLAY-dConvergedCharter-20 — the conf fold and the unattended kit's retirement shipped as upgrade steps, every shim closed when its window does, and the adopter exit check widened

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 7 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0494@4e004b72 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md) | research | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-03-build-PLAY-dConvergedCharter-20-deviation-201.md](../build/2026-11-03-build-PLAY-dConvergedCharter-20-deviation-201.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 11 folds every kit conf key the retrofit does not convert into the policy file, and unit 12
retires the unattended kit, each in gov's own tree. An adopter holds the same conf files and receives
neither change unless a step moves it (P38, v2:1062-1066). This unit ships both as upgrade steps through
the one conf-to-policy step, holds every forwarder to its window from the other side, so a shim whose
window has closed is a finding, and widens the exit check to every adopter at the converged release.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`0d1c1dda`: the shared step `tools/govkit/steps/conf_to_policy.py` (TOOL-dDeclaredLoop-21 S8), which
`fanout_cap.py` already calls by then; the folded keys' catalogue rows and their `legacy` field (unit
11's I5) and the both-homes reader that names a value's old home; the unattended kit's `[[retired]]`
row (unit 12); `derive_migration_state` (unit 5); `read_adopter_rows` (DEPL-dShippedRelease-31 S2);
and the owner-item mailbox (TOOL-dWellOiledMachine-48 S1, S4). `read_releases`
(`tools/govkit/shims.py:302`) stays the stand-in it is until DEPL-dShippedRelease-3 S1 replaces it.

- **S1** — The home mode of the shared step. `conf_to_policy.py up|down|witness <target> --home <conf>`
  derives its key map with `derive_home_folds(home)`: each catalogue row whose `legacy` field reads
  `<home> <KEY>`, so the step and the both-homes reader read one map (I5). For each key the up reads
  `policy.py get <key> --rev HEAD --explain` in the target and moves the value only where the reason
  names `<home>` as its source; a value the policy file or the default already gives moves nothing, so
  no default is restated. It writes through `render_policy_text` (`tools/govkit/upgrade_steps.py:1365`)
  behind one before-image, refuses writing nothing where the conf or the policy file differs from its
  blob at HEAD, as `fanout_cap.py`'s up does (`tools/govkit/steps/fanout_cap.py:168-171`), and takes the
  conf out last, the file itself where only blanks and comments remain. The witness exits 0 when no key
  of the map is assigned in the home, or the home is absent. `fanout_cap.py` keeps its argv and its
  bytes out, since its row is frozen. Observed by AC1 and AC2.
  **Readers:** by name: `tools/policy/policy.py:1211` (`derive_legacy_homes`, which lists each home's
  keys), `tools/policy/legacy-homes.txt`, and the kit descriptors' `[config]` tables, `tools/memory-tree/kit.toml:80`,
  `tools/codebase-map/kit.toml:70`, `tools/lexicon/kit.toml:78`, `tools/process-monitor/kit.toml:60` ·
  by value: unit 11's both-homes reader behind `policy.py get <key> --explain`, which reads the old
  home keyed by commit, so a value read before the step and after it is one value.
- **S2** — The conf fold's steps: one `[[upgrade]]` row per kit conf home that holds a key unit 11
  folds, in the descriptor of the kit that declares the home: `memory-tree/conf-to-policy`
  (`.memory-tree.conf`), `codebase-map/conf-to-policy` (`.codebase-map.conf`), `lexicon/conf-to-policy`
  (`.lexicon.conf`) and `process-monitor/conf-to-policy` (`.process-monitor.conf`), each running S1 with
  its `--home`, `needs-target = false`, and `surfaces` naming `conf-key:<home>#<KEY>` per folded key,
  the spelling of the `fanout_cap.py` row (`tools/hooks/kit.toml:138-145`). `.githooks/gate-env.sh` takes
  no step: no descriptor ships it, so no adopter holds it. Observed by AC3.
  **Readers:** by name: the keys' readers in each kit, re-pointed by unit 11 before this unit's steps
  land, and `tools/policy/legacy-homes.txt`, drained by `policy.py lists --write` · by value: each kit's
  conf-key gap check `read_conf_key_gaps` (`tools/govkit/govkit.py:4943`), which reads `*_keys` and
  unit 11 re-points.
- **S3** — The unattended kit's retirement as a step. `unattended/run-conf-retired`, an `[[upgrade]]`
  row in `tools/govkit/steps.toml`, the file for a surface no live entry owns, since unit 12's
  `[[retired]]` row takes the entry out of the registry. Its up runs S1 over `.unattended.conf` and then,
  under `--drop-rest`, takes out every key the catalogue does not carry, the run conf's extension keys
  unit 12 retires with the kit, and deletes the file; down restores both files from the before-image;
  the witness exits 0 when `.unattended.conf` is absent. `surfaces` names each dropped key as
  `conf-key:.unattended.conf#<KEY>`. The kit's installed files are `update`'s withdrawn arm for a claim
  retired to `none` (`resolve_claim`, `tools/govkit/upgrade_steps.py:1002`; TOOL-dSafePassage-9), an order
  or, under `--write-withdrawals`, a deletion, never the step's.
  Observed by AC4.
  **Readers:** by name: in an adopter's tree the file is read only by its installed copy of the
  unattended kit, which the same `update` withdraws, `tools/unattended/unattended.sh`,
  `tools/unattended/check-unattended.sh` and `tools/unattended/lib-unattended.sh` at base, and by
  `derive_legacy_homes` (`tools/policy/policy.py:1211`) as a home · by value: the 45 `.unattended.conf`
  rows of `tools/policy/legacy-homes.txt`, which a home with no file yields none of.
- **S4** — Every shim closed when its window does. `check_shim_windows` (`tools/govkit/shims.py:348`)
  gains the reverse arm: an open row whose window `derive_shim_window` (`:339`) allows to close prints
  `shims: <id> is open past its window: landed at <sha8>, <n> release(s) cut since, window <w>; close
  the row`, and selfcheck arm 11 (`tools/govkit/govkit.py:3530-3547`) fails on the line, as it fails on a held closed row. The rows
  it holds are unit 16's `kickoff-manifest/session-kickoff`, unit 17's `roles/build-skill` and unit 12's
  `unattended/resume-tick`, in either of the `skill` kind's forms, and any later one; this unit's steps
  move conf keys and leave no forwarder. While `read_releases` returns no release no window allows and the arm returns no line;
  arm 11's note then says no release exists, so an ungraded table never reads as a clean one.
  Observed by AC5.
- **S5** — The exit check widened, `check_adopters_converged(root, release)` in
  `tools/govkit/adopter_reading.py` and its verb `python adopter_reading.py converged --release <tag>`.
  Over every row of `read_adopter_rows(root)`, registered or not (deviation 201), a row passes when
  `derive_migration_state` (unit 5 S1) reads `migrated` at `release`, the converged release unit 5 S5
  names, or when an open owner item `adopter-unmigrated` keyed `<key> <release>` names it, read from
  the mailbox's open rows as `decide_owner_items` reads them (TOOL-dWellOiledMachine-48 S4). Each other
  row prints `adopters — RED <key> · <state>, and no owner item` and the verb exits 1; an empty register
  exits 2, not graded. It runs beside unit 14's fates join as convergence's exit check, over the register
  and never a second file population (I23). Observed by AC6.
- **S6** — The docs: `help/upgrade-steps.md` names the conf-fold steps and the unattended kit's step,
  and `help/shims.md` says an open row past its window reds. NOT OBSERVED by a criterion: prose, graded
  by the `docs` leg at the close.

## 3. Non-goals (OUT)

- The fold in gov's own tree, its catalogue rows and its reader re-points: unit 11's.
- The unattended kit's removal from gov, its `[[retired]]` row and its readers: unit 12's.
- A second conf-to-policy step module. TOOL-dDeclaredLoop-21 S8 extracts the one at its second
  instance; this unit is its third and fourth caller.
- Closing a shim row or deleting a forwarder: S4 reds the row, and the commit that closes it is the
  owning unit's, units 16 and 17 for theirs.
- Migrating an adopter: unit 5 drives the walk. S5 grades its result.
- The fates join itself: unit 14's.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `legacy-homes.txt` and the catalogue's `legacy` field it drains into, the key map S1 derives and S2's homes; without it no key is folded and the steps move nothing
- **consumes-from** `PLAY-dConvergedCharter-12` — `tools/unattended/` leaving gov under its `[[retired]]` row, which S3's step follows at the adopter; without it the step would strip a conf a live kit reads
- **consumes-from** `PLAY-dConvergedCharter-17` — `shims.toml`, the `roles/build-skill` row S4 holds to its window, closed and its held set removed when the window closes
- **consumes-from** `PLAY-dConvergedCharter-5` — `steps-pending`, read through `derive_migration_state`, the state S5 grades
- **hands-off** `PLAY-dConvergedCharter-21` — `fanout_cap.py`'s shared step `conf_to_policy.py` with S1's home mode, which unit 21's house-seed step calls with a reader of its own
- **hands-off** `PLAY-dConvergedCharter-14` — `derive_pending_steps`'s figure, read through `check_adopters_converged`, the adopter arm unit 14's exit check runs beside the fates join
- **consumes-from** external — TOOL-dDeclaredLoop-21 S8 (`conf_to_policy.py`), DEPL-dShippedRelease-31 S2 (`read_adopter_rows`) and TOOL-dWellOiledMachine-48 (the mailbox), each specced and unbuilt at base `0d1c1dda`

## 4. Design

### Evidence

Read at `d8a12f04`; no product file differs from base `0d1c1dda`.

- `tools/govkit/steps/fanout_cap.py` is the one conf-to-policy step at base: its up reads the value
  through `policy.py get runtime.agents-in-flight --rev HEAD --explain`, writes it through
  `render_policy_text`, and takes the conf out last (`:152-198`). TOOL-dDeclaredLoop-21 S8 extracts
  `conf_to_policy.py` from it at the second instance, `review_rounds.py`. Scout C's row 20 and the
  brief's I6 call this unit's fold the second instance; it is the third, so this unit extends the
  shared step and extracts nothing.
- `tools/policy/legacy-homes.txt` holds 116 rows across six homes at base; `.githooks/gate-env.sh` is
  one of them, and no descriptor's `[[files]]` ships it.
- `check_shim_windows` refuses a closed row before its window and returns nothing for an open one
  (`tools/govkit/shims.py:348-372`), so a forwarder can stand forever.
- `steps.toml` holds the rows of surfaces no live entry owns, its `<entry>` naming no registry entry
  (`tools/govkit/steps.toml:1-10`), so a retired kit's step lives there.

### The steps

| Step id | File | Home | Mode |
|---|---|---|---|
| `memory-tree/conf-to-policy` | `tools/memory-tree/kit.toml` | `.memory-tree.conf` | fold |
| `codebase-map/conf-to-policy` | `tools/codebase-map/kit.toml` | `.codebase-map.conf` | fold |
| `lexicon/conf-to-policy` | `tools/lexicon/kit.toml` | `.lexicon.conf` | fold |
| `process-monitor/conf-to-policy` | `tools/process-monitor/kit.toml` | `.process-monitor.conf` | fold |
| `unattended/run-conf-retired` | `tools/govkit/steps.toml` | `.unattended.conf` | fold, then `--drop-rest` |

A home whose keys unit 11 leaves unfolded, or that holds none at the build pass, takes no row. The
table is DERIVED at the pass from `legacy-homes.txt` and the catalogue's `legacy` fields, and is
pinned here as read at base.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_home_folds` | function, `tools/govkit/steps/conf_to_policy.py` | `py.function`, OK by `--suggest` |
| `--home`, `--drop-rest` | flags of `conf_to_policy.py` | none |
| `check_adopters_converged` | function, `tools/govkit/adopter_reading.py` | `py.function`, OK by `--suggest` |
| `converged` | verb of `adopter_reading.py` | none |
| the five step ids above | `[[upgrade]]` ids | none |
| `window-open` | `--fixture --plant` case of `tools/govkit/shims.py` | none |

### Migration

The steps are the migration. Each is reversible from its before-image, and `update` walks them in
the order `upgrade_steps.py list` prints.

### Rollout

The steps land after units 11 and 12, in the commit after the fold and the retirement each follows,
so a step never runs ahead of the gov-side change it ships. S4 lands dark in effect: it grades nothing
until a release is cut.

### Files touched (estimate)

- `tools/govkit/steps/conf_to_policy.py`: S1
- `tools/memory-tree/kit.toml`, `tools/codebase-map/kit.toml`, `tools/lexicon/kit.toml`,
  `tools/process-monitor/kit.toml`, `tools/govkit/steps.toml`: S2, S3
- `tools/govkit/shims.py`, `tools/govkit/govkit.py`: S4
- `tools/govkit/adopter_reading.py`: S5
- `tools/govkit/usage.toml`: the `[[usage]]` rows of the new flags and verb
- `tools/govkit/selftest.py`: the plants of §6
- `help/upgrade-steps.md`, `help/shims.md`: S6

### Alternatives rejected

- **A factory extracted here from `fanout_cap.py`.** Rejected by reading TOOL-dDeclaredLoop-21 S8,
  which extracts it first; a second extraction is the copy `[reuse]` forbids.
- **One step per folded key.** About 90 rows for one act per home, each an id an adopter's receipt
  records; a step per home walks the same keys under one before-image.
- **A step for `.githooks/gate-env.sh`.** Rejected by reading the descriptors: none ships the file,
  so no adopter holds a key to move.
- **Removing the unattended kit's installed files in the step.** `update` already withdraws a claim
  retired to `none`; the step would write files the withdrawal owns.

## 5. Production-readiness checklist

- security — the steps write only the target's conf and policy file, through the one policy writer,
  under `run_step_isolated`; a value is copied, never evaluated.
- perf / scale — one `policy.py get` per folded key per step; five steps.
- error / empty / loading states — an uncommitted conf refuses writing nothing; an absent home is a
  no-op; an empty register exits 2.
- observability — each step prints what it moved; S4 names the row, its landing and the count.
- risks — a key unit 11 folds and S1's map misses would stay in the conf, read by nothing after the
  re-point; the witness reads the map, so AC1 plants that case.
- testing — scratch targets for S1 to S3, a scratch shims table for S4, a planted register for S5.
- migration — §4.
- user docs — `help/upgrade-steps.md`, `help/shims.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python conf_to_policy.py up <target> --home .memory-tree.conf` runs over a scratch
  target whose conf assigns one folded key a non-default value and another its default, the policy file
  gains the first key and not the second, the conf loses both lines, and `down` restores both files
  byte-identical.
  Red when: a default is restated, or a folded key is left assigned with the witness reading applied.
- **AC2** — When `python fanout_cap.py up` runs over dSafePassage-1 S6's scratch target before and after
  S1, the files it writes are byte-identical.
  Red when: the home mode moves the frozen step's behaviour.
- **AC3** — When `python tools/govkit/upgrade_steps.py list` runs at the unit's tip, it prints the four
  conf-fold rows and `unattended/run-conf-retired`, each `surfaces` naming `conf-key:` members.
  Red when: a home holding a folded key has no step, so its adopters keep reading the old home.
- **AC4** — When `run-conf-retired`'s up runs over a scratch target holding `.unattended.conf` with one
  folded key and one extension key, the policy file gains the first, the file is gone, and `down`
  restores it byte-identical.
  Red when: an extension key is moved into the policy file, or the file survives with the witness green.
- **AC5** — When `python shims.py --fixture --plant window-open --window 2 --releases 2` runs, the
  open row's line reads `is open past its window` and the plant exits 0; with `--releases 1` no line
  names the row.
  Red when: a shim whose window has closed is left standing unreported.
- **AC6** — When `python adopter_reading.py converged --release <tag>` runs over a planted register of
  three rows, one `migrated`, one `pending` with an open `adopter-unmigrated` item, one `pending` with
  none, it prints one `adopters — RED` line naming the third and exits 1; with the third's item raised it
  exits 0, and over an empty register it exits 2.
  Red when: the planted adopter with a pending step and no owner item passes.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `upgrade-walk` · `step-rows-frozen` · `step-gate` · `docs` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `lexicon selftest` · `recall floor arms` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC4 · scratch targets for the home mode and the run-conf step, failing case a default restated · none
New arm: tools/govkit/selftest.py · covers AC5 · the window plant with an open row past its window · none
New arm: tools/govkit/selftest.py · covers AC6 · a planted register and mailbox, failing case a pending row with no owner item · none

## 8. Open questions

- **F1 — Which rows the widened exit check grades.** The clause names every registered adopter, and
  at base no row is registered. Options: (a) the registered rows alone, so with none registered the
  arm grades an empty population; (b) every row of the register, a registered one passing when migrated
  or held by an owner item, an unregistered one passing only when held by an owner item. (a) reads zero
  rows as done, which `[gate]` refuses, or never reads green until the owner acts, so the exit check
  cannot close. RESOLVED (agent, 2026-11-03, delegated): (b), rung 3, stricter than the clause, deviation 201. widens: none · relaxes: none
- **F2 — Where the retired kit's step lives.** Options: (a) `tools/govkit/steps.toml`, whose ids name
  no live entry; (b) a row kept in the unattended descriptor. Unit 12 removes the descriptor with the
  kit, and `read_steps` reads only the descriptors the registry names (`tools/govkit/upgrade_steps.py:808-830`).
  RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 20, v2:1062-1066 and :1860 (P38), scout C's
  row for 0494, and the spec brief's I6, which TOOL-dDeclaredLoop-21 S8 corrects (§4 Evidence).

## 10. Reuse audit

The seam extended is TOOL-dDeclaredLoop-21 S8's `conf_to_policy.py`, extracted from
`tools/govkit/steps/fanout_cap.py` with its before-image (`write_before_image`,
`tools/govkit/upgrade_steps.py:1121`) and writer (`render_policy_text`, `:1365`); `check_shim_windows`
(`tools/govkit/shims.py:348`) for S4; and DEPL-dShippedRelease-7's `adopter_reading.py` for S5.
`python tools/codebase-map/reuse_lookup.py "move a conf key into the policy file as an upgrade step with a
before-image"` ranked `parse_conf` (`fanout_cap.py`, `held_halves.py`, `tree_lib.py`), `load_conf`,
`read_conf_key` and `read_steps`; `fanout_cap.py`'s `parse_conf` is the seam, the rest read confs for
their own kits. The recall probe found what the scout missed: TOOL-dDeclaredLoop-1's scout C records
"the second conf-key-to-policy-key step after dSafePassage's", which TOOL-dDeclaredLoop-21 S8 extracts,
so the brief's I6 names an extraction a parent already owns. Scout C's other claims for this row hold
at HEAD: `tools/govkit/adopters.toml` holds no remote, branch or receipt.

Recall terms used: `python tools/memory-recall/query.py "how does a conf key move into the policy file through an upgrade step and when does a shim close" --terms "fanout_cap upgrade step conf fold policy legacy-homes before-image witness shim deprecation-window"`
