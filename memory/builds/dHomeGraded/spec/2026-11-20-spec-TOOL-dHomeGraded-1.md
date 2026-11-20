# TOOL-dHomeGraded-1 — adopter scans skip gov's unmodified kit files, and four re-adoption defects close

**Status:** OPEN · rev-1 · 2026-11-20 · node d · Tier-1 · base a0ae4dca · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

An adopter's bar grades what the adopter wrote. Re-adopting gov 608aa364 into nicocares and inCMS
redded 19 and 17 legs before either tree changed a line, most of them on kit files installed
byte-identical to gov's sources, and the rest on four deployer defects the re-adoption exposed.

## 2. Scope (IN)

- **S1** — A canonical block `home_graded_py` in gov's lib dir answers which tracked paths of a tree
  are gov's to grade: a `.governance/install.json` row of role `engine` whose `oid` equals its
  `gov_oid` and whose working-tree blob still hashes to that `oid`. No receipt, an unreadable one, or a
  failed hash answers the empty set. Observed by AC1.
  **Readers:** by name: `tools/lib/resolve-python.test.sh`, `tools/gate-lint/sh_hygiene.py`,
  `tools/lexicon/lexicon.py`, `tools/memory-tree/check-arms.py` · by value: `sh_hygiene.py`,
  `lexicon.py` and `check-arms.py`, each dropping the answer from its population.
- **S2** — The five `sh_hygiene.py` scans and the lexicon's corpus walk drop the S1 set and print how
  many files they dropped, and the lexicon's walk also drops `.governance/`, the deployer's own state
  dir. Observed by AC1 and AC2.
  **Readers:** by name: none, since the dropped paths are named by no file · by value: NO VALUE READERS, since
  a dropped path is read by no caller: the scan's verdict is its only output.
- **S3** — check-arms grades a families sidecar the S1 set holds without asking this tree's
  DECISIONS.md for its decision ids: those ids are gov's records. Observed by AC3.
- **S4** — The policy kit's cap census resolves an installed enforcer through `resolve_kit_dir` when
  the receipt's prefix path holds no file, so a kit an adopter homes flat is found. Observed by AC4.
- **S5** — `govkit` drops a prior emitted gate leg whose kit no descriptor declares and whose name no
  descriptor's `[[gate_leg]]` carries: from the receipt's `emitted`, and from the runner when the
  runner row still carries the recorded argv. Observed by AC5.
  **Readers:** by name: `tools/run-gates/run-gates.sh`, which reads the runner rows · by value:
  `write_gate_legs`' own claim test on the next run, which reads `emitted` as ownership.
- **S6** — `pass_legs.py` reads `[gate_runner].file` from `.governance/deploy.toml` when `GATE_LEGS`
  is unset and the deploy file names one, before falling back to the sibling manifest. Observed by AC6.

## 3. Non-goals (OUT)

- A gov registry shipped to adopters: gov's own rows name gov's paths and stay home.
- A kit file the adopter edited: its bytes no longer match the receipt and it is graded as before.
- The seed-to-engine template move and `apply`'s two bar runs, also seen on the re-adoption.

### Edges

none

## 4. Design

The receipt already records, per installed engine file, the blob gov shipped (`gov_oid`) and the blob
written (`oid`); an engine row's two are equal when gov's bytes were copied unchanged. One
`git hash-object --stdin-paths` call hashes every such path through the tree's own filters, and a path
whose hash still equals `oid` holds gov's bytes. Those bytes are graded on gov's bar, against gov's
registries and gov's decisions, so an adopter scan that grades them again grades gov against the
adopter's empty registries. The block is inline in each consumer, byte-identical and held by the
parity table, as `resolve_kit_dir` is.

The census fix reuses `resolve_kit_dir`, which `check_policy.py` already carries. The leg fix keys on
the descriptor set the caller already read: a retired kit is in no descriptor, and a renamed kit's
successor declares the same leg name, which the existing claim path keeps.

### Files touched (estimate)

- `tools/lib/home_graded.py`
- `tools/lib/resolve-python.test.sh`
- `tools/gate-lint/sh_hygiene.py`
- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`
- `tools/memory-tree/check-arms.py`
- `tools/policy/check_policy.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/run-gates/pass_legs.py`
- kit version markers and `memory/map/generated/symbols.json`

## 5. Acceptance criteria

- **AC1** — When `python scripts/gate-lint/sh_hygiene.py --temp-names` runs in nicocares' re-adoption
  worktree with this unit's scanner, it names no site in a receipt-claimed engine file and prints the
  count it dropped. Red when: the unchanged scanner runs there, which listed 59 sites in 19 files.
- **AC2** — When `python scripts/lexicon/lexicon.py` runs in the same worktree with this unit's
  lexicon, no offender line names a receipt-claimed engine file and `lock` is no undeclared extension.
  Red when: the unchanged lexicon runs there, which counted 2073 verb offenders over a pin of 1898.
- **AC3** — When `python scripts/memory-tree/check-arms.py` runs in the same worktree with this unit's
  check-arms, no HYGIENE line names `TOOL-aSparedSpawn-14`. Red when: the unchanged check-arms runs.
- **AC4** — When `python scripts/policy/check_policy.py` runs in the same worktree with this unit's
  policy kit, no cap census row says its enforcer is not a file. Red when: the unchanged census runs,
  which named 11 rows.
- **AC5** — When `govkit update --write` runs against a target whose receipt emitted the
  `agent-instructions wiring` leg, the runner and the restamped receipt no longer carry it. Red when:
  the unchanged govkit runs, which kept the row and left the leg exiting 127.
- **AC6** — When `python tools/run-gates/pass_legs.py --check` runs in inCMS' re-adoption worktree
  with `GATE_LEGS` unset, it reads `scripts/run-gates/gate-legs.json`. Red when: the unchanged reader
  runs there, which refused the object-shaped `scripts/gate-legs.json`.

## 6. Gates

`routed commits name a specced unit` · `shell-hygiene selftest` · `lexicon selftest` · `check-arms selftest` · `policy fixtures` · `govkit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-20 · initial draft.
