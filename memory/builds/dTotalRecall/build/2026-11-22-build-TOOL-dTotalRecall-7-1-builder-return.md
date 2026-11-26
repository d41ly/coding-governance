**Serves:** journal TOOL-dTotalRecall-7

# TOOL-dTotalRecall-7 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `ed5a7d523` from [2026-11-22-prompt-TOOL-dTotalRecall-7-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-7-build-brief.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: TOOL-dTotalRecall-7 rev-5 can't be built as written. Two parts of the door verb are left undecided, and one sentence contradicts the stated order. The spec writer needs to settle all three.

(1) §2 S2, §4 "The door verb" and AC4 never say which <FAMILY> the ask id is minted in. The registry row's id-rule is <FAMILY>-<slug>-<seq>, and both mint routes need a family: `gov-claim.sh ask <FAMILY> <slug>` and the no-remote `derive_ask_seq <FAMILY> <slug>` reached through `breakpoints.py#run_sourced`. The CLI has no family argument, and its `--unit` is the ask row's boolean unit marker (`render_ask_row`'s `unit`), not a serving unit id. So the door can't take the family from the serving unit the way TOOL-dTotalRecall-2's built `build_records.py#write_new_record` does for its seq mint. The shell filers' precedent is `unattended.sh#read_roster_family`, the first family of the build's derived roster. Probed: `gen_build_index.py#read_derived_front_matter` runs a whole-tree `collect`. That took 9 s on this tree (DERIVED, the builder's probe at `ed5a7d523`), and it refuses on any unparseable README anywhere in the tree. In a scratch fixture it also needs a stale-header waiver, a README carrying opened and ids, and a spec with a parseable Status header. A family rule is a user-visible design choice, so the spec has to state it: the roster read with its cost and its refusal, a cheaper rule, or a `--family` flag. §6 AC4 and the fixture text then need to say what the fixture plants for it.

(2) §4 "The door verb" gives the order as "read asks.acceptance, mint the id, render the ask row and its SEV row, grade the ask row with S1, then write or refuse". The same paragraph says "a refused filing commits no mint, as the door's idempotence rule (I2) treats any refused write". Both can't hold in a clone that has a remote. There the mint is `gov-claim.sh ask`, which pushes a counter commit to `refs/gov/claims/asks/<FAMILY>-<slug>` before the grade runs, so an ask refused under `refuse` has already used up a sequence number on the remote. They hold together only if the grade runs before the mint: render with a provisional id, grade, then mint and render again. That is the pattern `write_new_record` uses (check_text before run_claim_cli). The spec should either state that order or drop the sentence.

(3) TOOL-dTotalRecall-2 §4 (CLOSED) says the ask handler "ends in write_new_record's mint, idempotence and refusal path". But `write_new_record` refuses every schema form except `fields` ("written only by a kind handler"), and it writes one file per record. Unit 7's ask is a `rows` kind written as two rows into BACKLOG.md, so it can't end there. Unit 7 §3 hands idempotence to units 2 and 3, so no unit gives `new ask` a replay rule. With a remote, a replayed filing gets the first id back from the counter (claimant-key replay) and writes a second row with that id. The read-back then finds two asks, rolls back and exits 2. Without a remote, `derive_ask_seq` mints a new id and files a duplicate ask. §3 or §4 should say what a replayed `new ask` does.

Probes that held at base: AC3 at HEAD prints [12, 14] and [12]. AC2's `parse_seen(v).command` count is 2. `policy.py get asks.acceptance --explain` prints refuse. `asks.acceptance` carries no summary or usage and appears in unsummarised-keys.txt, docs-undocumented.txt and the help page's list. No `ask` row exists in record-kinds.toml, and the purpose source line `:455` is the layer table's ask row. `check_row`'s writer red and the `ask rows` count shape match AC8. `record_kinds.py --write`, `adopt-memory-tree.sh --render`, `policy.py lists --write` and `render_playbook.py --reference` all exist. Nothing was written to the repository and no draft patch was made. The probe fixture at %TEMP%/u7p was removed.

## Summary

TOOL-dTotalRecall-7 was not built and nothing was committed: the spec can't be built as written, so this pass returns a DIVERGENCE (see why). Base is ed5a7d523b44270d4e0a8f531a395ecf56cd74fc.

The brief record was already in place: `unattended.sh --brief` answered "already recorded, unchanged — TOOL-dTotalRecall-7 at 1e323bd15624". The staged RUN.md rows were there before this pass and I left them as they were. The untracked reground prompts for units 9, 21, 36, 39 and 47 belong to another session and were not touched.

Checks that ran, all before any product edit; no gate, suite or bar ran:
- An AC3 probe at HEAD printed [12, 14] for a bare ask and [12] with accept, which confirms §8 F5's V12 claim. It stands in for the build-index selftest's V14 arms.
- AC2's grep at HEAD counts 2 copies of the expression, as the spec expects before the change.
- AC9's `policy.py get asks.acceptance --explain` printed refuse. This stands in for the policy fixtures and policy check legs.
- I read `record_kinds.py#check_row`, `#check_home`, `#check_purpose_cell` and the `check_record_kinds` count line against the planned ask row (stands in for the record-kinds leg).
- The naming lexicon `--suggest` passed on check_ask_acceptable, write_new_ask, write_seq_mint, read_ask_family, check_ask_plant and run_ask_door.
- In a scratch fixture under %TEMP%/u7p (removed afterwards) I probed `policy.py get` with no remote (it read the local main branch) and `gen_build_index.read_derived_front_matter` (it needs a waiver, a full README and a spec). That probe is how I found divergence (1).

Owed at the close once the spec is revised and the unit rebuilt (both arms are unobserved): New arm in gen_build_index.py (V14 through check_ask_acceptable, covers AC3) and New arm in check-memory-hygiene.test.sh (the ask-door plant, covers AC4 to AC7), each RED first. The legs on the spec's gates section also run at the close. Nothing timed out or was skipped. The gotchas checklist did not run because no commit was made.
