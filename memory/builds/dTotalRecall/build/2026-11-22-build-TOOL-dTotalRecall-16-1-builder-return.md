**Serves:** research TOOL-dTotalRecall-16

# TOOL-dTotalRecall-16 build pass 1 — the builder's return

The gov-builder return of `unattended-unit.js` run `wf_e581c10f-94e`, at base `8fbc5a337`, pass commit `f36ec323c`, follow-up `4054a5095`, saved in substance.

## why

TOOL-dTotalRecall-16 is built and committed as specced at rev-6. Before building I probed the spec against the code and every claim held: `read_policy_value`, `unfenced_lines`, `resolve_kind`, `parse_file`, `TERMINAL`, `render_ask_row`, `CHAIN_REGISTRY`, `check_chain_registry`, the layer-memory table, the catalogue row, the drain lists and the `requires_if` row. Two of the spec's figures are out of date but are not design claims: the registry holds 46 rows now, not 25, because unit 18 added witness rows; and all 22 chain rows have an H1 in their README, so the chain namespace drafts no ask. One addition the spec does not state went in as deviation record 161 (`author-recorded`): `--ask` used under any value but `review`, or used without `--write`, exits 2. The pass commit sets the spec header to CLOSED. A follow-up commit 4054a5095 (`Pass: none`) adds the purpose column to the header comment of `record-kinds.toml`, which the M6 bug-class checklist caught. (DERIVED, the builder's own run)

## summary

TOOL-dTotalRecall-16 is committed as f36ec323c01b38a775873b202a0a71b23898b933 (`Pass: TOOL-dTotalRecall-16`, spec header CLOSED), with a follow-up 4054a5095edbfacfad20c1de65a0fdf93e98b34b (`Pass: none`). No gate, suite or bar ran.

**What was built:**
- **The column:** every row of `tools/memory-tree/record-kinds.toml` now has a `purpose`, either a one-line text with its source or a pending id. `check_row` and `check_purpose_cell` red a row with no purpose, an unknown key, both forms at once, a text over 120 bytes or holding a newline, or a malformed source. (DERIVED, the builder's own run)
- **The pending rule:** `check_purpose` reads `memory.map-purpose` once through `read_map_purpose`. With no policy kit it falls back to `review` and prints one line; a refused read exits 2.
- **`new`:** it now requires `--purpose`.
- **The review:** `--purpose-review [--from] [--write [--ask]]` and `--print-purpose-pending` were added. The view gains a `Purpose` column and a `<n> kinds · <p> purposes pending` line.
- **The fixture:** it now has a BACKLOG with one open and one closed ask, a chain registry and the `--from` record. The repository is created on `main`. Eleven new plants were added.
- **The review over this tree:** 22 registry rows and all 22 chain rows got a purpose with its source cited. The other 24 kinds are pending on a new ask, TOOL-dTotalRecall-110, filed in `memory/builds/dTotalRecall/BACKLOG.md` with a LOW SEV row. (DERIVED, the builder's own run)
- **Docs and records:** the catalogue row got its summary and usage; the key was drained from `unsummarised-keys.txt` and `docs-undocumented.txt`; `help/reference/kinds.md`, `help/reference/policy.md` and `memory/HYGIENE.md` were re-rendered; the README, `kit.toml` and the docstring were updated. The records are the acceptance ledger, the purpose-review record and deviation record 161.

**Checks that ran, and the gate each stands in for:**
- **`record-kinds` leg and the new arm:** I ran `record_kinds.py --fixture` with no plant (green) and with every plant, old and new, in a throwaway repository. All 17 old plants behave as before. Of the new ones:
  - `purpose-missing`, `purpose-long`, `pending-closed` and `value-refuse` exit 1, each naming its row.
  - `value-ledger-unregistered` and `value-refused` exit 2, naming the population and the key.
  - `review`, `review-write`, `value-derive`, `value-ledger`, `new-purpose`, `new-row` and `pipe-cell` exit 0 with the expected lines.
- **AC1:** a `python -c` probe over the tree found no red from `check_purpose_cell` on any row, and `check_purpose` printed 22 texts and 24 pending. (DERIVED, the builder's own run)
- **AC2:** `new` without `--purpose` on the real tree exited 2 and left `git status --porcelain` unchanged.
- **AC7:** the three `grep -c` counts printed 0, 0 and 1.
- **Lexicon:** every new name, nested ones included, got OK from `lexicon.py --suggest`. `--measure` reads `VERB_OFFENDER_PIN` at 1445, unchanged.

**Owed to the close:**
- **The new arm's red-first observation:** `tools/memory-tree/record_kinds.py --selftest` (AC2 to AC6), seen red with `check_row` admitting a row with no `purpose`, then green restored.
- **AC1 in full:** `record_kinds.py --check` exiting 0. The hook refused it in this role. It will still red on the stray `dHomedResolver/` from unit 18's F2, which is not this unit's.
- **The legs in spec §7:** `memory hygiene`, `kit/dogfood doc parity`, `recall floor`, `recall floor arms`, `record-kinds`, `tags (the resolver's checks)`, `govkit acceptance matrix`, `playbook render selftest`, `core kinds`, `help reference pages`, `docs`, `policy check`, `policy fixtures`, `routed-commits selftest`, `scratch-guard self-test`, `writing practice (records and units)` and `lexicon naming predicates`.

**Write set:** beyond the dispatched list I declared three more paths with `--dispatch`: the purpose-review record, deviation record 161, and `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, whose deviation count `gen_build_index` rewrote. Another agent has uncommitted edits to specs 40, 54 and 6. I left those files unstaged and staged only my own rows of `memory/builds/dTotalRecall/README.md`, so the README stays modified in the working tree.

**Gotchas checklist:** I ran it over both commits. It caught that the header comment of `record-kinds.toml` still listed the old columns; 4054a5095 fixes that. Nothing else it listed needed a change.

No command was skipped for timing out.
