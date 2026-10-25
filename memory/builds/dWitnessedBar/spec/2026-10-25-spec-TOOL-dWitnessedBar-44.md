# TOOL-dWitnessedBar-44 — the inherited-red upgrade step reads both policy files and maps every value today's readers accept

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 21 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 62 at HIGH**, its item **H5**, alone in that item. `TOOL-dWitnessedBar-3` S8's
upgrade step reads `INHERITED_RED` from `.githooks/gate-env.sh` only and maps `park`, `land` and absent.
The driver reads it from the file `.unattended.conf`'s `GATE_POLICY_FILE` names
(`tools/unattended/unattended.sh:9545-9592`), and both readers read any other value as `park`
(`.githooks/pre-push:1343`, `unattended.sh:9592`). The step deletes the line either way. An adopter with a
custom `GATE_POLICY_FILE`, or a value such as `Park`, blocks every red today; the step writes nothing, the
catalogue default `own-only` applies, and MIXED, CONTENDED and INHERITED reds that blocked yesterday land
silently. This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-3`.

## 2. Scope (IN)

- **S1** — Both files read. The step's `up` reads `INHERITED_RED` from `.githooks/gate-env.sh`, the
  file the hook reads, and from the file `GATE_POLICY_FILE` names in the target's `.unattended.conf`,
  the file the driver reads, each only where present. A blank or absent `GATE_POLICY_FILE` names
  `.githooks/gate-env.sh`, as the driver falls back. Observed by AC1.
- **S2** — Every value mapped. A value is mapped by the reader's own table: `land` to
  `own-mixed-contended`, `park` to `every-red`, and any other non-blank value to `every-red`, which is
  what both readers make of it today. A `GATE_POLICY_FILE` that is not a repo-relative path inside the
  tree maps to `every-red`, as the driver reads it (`unattended.sh:9566-9568`). Observed by AC2.
- **S3** — Two files, one key. Where the two files map to different values, the step writes the one
  that blocks more, `every-red` over `own-mixed-contended`, and its witness names both. Observed by AC3.
- **S4** — The witness. `witness` prints one line per file read, naming the file, the value found and the
  value written, and exits 0 only when no `INHERITED_RED` assignment remains in either file. `up`
  deletes the assignment from every file it read it from; `down` restores each from the before-image.
  Observed by AC1 and AC3.
  **Readers:** by name: the readers of the second file this step now edits, `tools/unattended/unattended.sh`
  (`read_gate_policy`, which reads the file `GATE_POLICY_FILE` names), `tools/unattended/unattended.test.sh`,
  `tools/unattended/.unattended.conf.example` and `.unattended.conf`, beside the readers of
  `.githooks/gate-env.sh`, `.githooks/pre-push` and `.githooks/pre-push.test.sh`; every other reader that
  spells `INHERITED_RED` is on TOOL-dWitnessedBar-3 S8's list, whose retirement this step completes ·
  by value: `.githooks/pre-push` `read_policy_at` and `tools/unattended/unattended.sh` `read_gate_policy`,
  whose value table §4 maps and which read `verdict.blocks` once unit 3 lands.

## 3. Non-goals (OUT)

- The block table, `verdict.blocks`, the runner and the readers: `TOOL-dWitnessedBar-3`'s.
- The absent path, where neither file declares `INHERITED_RED` and today's readers read `land`: the
  minors batch's id 19 item (`TOOL-dWitnessedBar-51`), which this step leaves writing nothing.
- `INHERITED_RED_MAX_AGE`: kept, as unit 3 §3 keeps it.
- An `[[upgrade]]` conformance rule that a key-deleting step maps every value its reader accepts, the
  report's left-shift: AC2 is the table-driven fixture for this step.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-3` — the step row `govkit/inherited-red-to-verdict-blocks` and its script `inherited_red.py`, whose reads and mapping this unit widens
- **hands-off** `TOOL-dWitnessedBar-51` — the absent-key path of `inherited_red.py up`, where the minors batch's id 19 item adds the loosening's witness line
- **hands-off** `TOOL-dWitnessedBar-55` — the step's two-file read and mapping table, whose line-selection rule unit 55 states (id 43)
- **hands-off** `TOOL-dWitnessedBar-56` — the run-gates README migration note of §5, which the verdict-boundary minors batch lands if this pass leaves it out (id 41)
- **hands-off** `TOOL-dWitnessedBar-57` — the step script `inherited_red.py`, whose `up` the resolver and ledger minors batch makes byte-preserving (id 18)

## 4. Design

### Evidence

- The driver: `GATE_POLICY_FILE` read from the conf at R; blank or absent falls back to
  `.githooks/gate-env.sh`; a path that is absolute or climbs out reads `park`; an absent named file reads
  `land`; then `INHERITED_RED` of `land`, `park`, blank (`land`) or anything else (`park`)
  (`tools/unattended/unattended.sh:9545-9592`).
- The hook reads `.githooks/gate-env.sh` alone, whatever `GATE_POLICY_FILE` says, with the same value
  table (`.githooks/pre-push:1322-1343`).
- Gov's own conf: `GATE_POLICY_FILE=".githooks/gate-env.sh"` (`.unattended.conf:208`); the example
  ships it blank (`tools/unattended/.unattended.conf.example:222`).

### The mapping

| Read | Written to `[verdict] blocks` |
|---|---|
| `land` | `own-mixed-contended` |
| `park` | `every-red` |
| any other non-blank value, `Park` and `LAND` included | `every-red` |
| `GATE_POLICY_FILE` absolute or climbing out of the tree | `every-red` |
| blank or absent in every file read | nothing (the minors batch's id 19) |
| two files, two values | the stricter, `every-red` |

The value set is the readers' own `case` arms, so a value no arm names reads as the `*` arm does.

### Inventory

Minted: nothing new by name; the step script gains the second read and the table rows.

### Migration

This unit is itself the migration's correction; gov's own run through the step reads one file
(`GATE_POLICY_FILE` names `.githooks/gate-env.sh`) and writes `own-mixed-contended` as before.

### Rollout

Live at landing, in the same kit version as `TOOL-dWitnessedBar-3`'s step.

### Files touched (estimate)

- `tools/govkit/steps/inherited_red.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Read only the driver's file.** The hook reads `.githooks/gate-env.sh` whatever the conf says, so a
  value declared there alone would be lost.
- **Refuse a value outside `park` and `land`.** An update that refuses on a typo leaves the adopter on
  the retired key; the readers already decided what such a value means.

## 5. Production-readiness checklist

- security — the step never loosens: every input it cannot map to `land` writes `every-red`.
- perf / scale — two file reads per target.
- error / empty / loading states — an unreadable named file is read as absent, as the driver reads it,
  and the witness names it.
- observability — one witness line per file.
- risks — an adopter whose two files disagree lands on the stricter value; the witness says why.
- testing — AC1 to AC3 by fixture; the arm of §7 at the close.
- migration — §4.
- user docs — none under `help/`; the run-gates README's migration note names both files at the pass.

## 6. Acceptance criteria

- **AC1** — When `python inherited_red.py up <target>` runs over a fixture target whose `.unattended.conf`
  sets `GATE_POLICY_FILE` to a custom file, ops/gate-policy.sh, holding `INHERITED_RED=park`, and whose
  hooks directory holds no `gate-env.sh`, the target's `policy.toml` holds `blocks = "every-red"` under
  `[verdict]`, the line is gone from the custom file, and `witness` exits 0 naming it.
  Red when: the step reads `.githooks/gate-env.sh` alone, so the custom file's `park` writes nothing.
  fixture: scratch targets under the run's scratch path, built by the suite.
- **AC2** — When the same verb runs over fixtures holding `INHERITED_RED=Park`, `=LAND`, `=bogus` and a
  `GATE_POLICY_FILE` of `/etc/x`, each writes `every-red`; `land` writes `own-mixed-contended`.
  Red when: a value outside `park` and `land` writes nothing, so the target loosens.
- **AC3** — When a fixture's `.githooks/gate-env.sh` holds `land` and its `GATE_POLICY_FILE` names a file
  holding `park`, `up` writes `every-red`, `witness` prints two lines naming both files and values, and
  `down` restores both files byte for byte.
  Red when: the step writes the milder value, or leaves one file holding the retired key.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `memory hygiene` · `recall floor arms`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the step's table over a custom `GATE_POLICY_FILE`, four off-table values and a two-file disagreement, staged red by restoring the `.githooks/gate-env.sh`-only read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-3`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — When the hook's file and the driver's file disagree, which value does the step write?**
  Options: (a) the stricter; (b) the driver's; (c) refuse the update. (b) loosens the hook's push where
  the hook's file was stricter; (c) leaves the adopter on the retired key. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the option that never loosens a landing. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 62 (HIGH, item H5).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-55, TOOL-dWitnessedBar-56, TOOL-dWitnessedBar-57, promoted by the
  round-1 spec audit of units 40 to 51; nothing else moved.

## 10. Reuse audit

The seam is the readers' own value table, `read_gate_policy` (`tools/unattended/unattended.sh:9545`)
and `read_policy_at` (`.githooks/pre-push:1322`), copied as the step's mapping rows rather than
re-invented. `python tools/codebase-map/reuse_lookup.py "convert a retired policy key in an upgrade step
mapping every value"` ranked `key`, `keys`, `step` (govkit), `read_conf_key`, `load_policy` and
`readConfKey`, each a reader of one conf key and none a value table, so no existing seam fits beyond
the two readers whose table the step copies; the step reads its two files with the same
`KEY=value` reader `TOOL-dWitnessedBar-3` S8 gives it.

Recall terms used: `python tools/memory-recall/query.py "how does the inherited red policy migrate onto verdict.blocks" --terms "INHERITED_RED GATE_POLICY_FILE park land verdict.blocks every-red own-mixed-contended upgrade step gate-env.sh"`
