**Serves:** research DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31

# Reuse scout D — dShippedRelease

The scout's final return, extracted from its transcript by script, never retyped.

# Scout D: Items 7, 16, 17, 18, 20, 25, 28, 29, 31 (HEAD `f4597719e`)

**Coverage**
- **Not read whole.** The task asked for `tools/govkit/` whole with its selftest. I read `govkit.py` by its full outline plus targeted ranges, and `selftest.py` by grep only.
- **Also partial.** `WIRE-INTO-PROJECT.md` was read by headings and grep. Of the adopt scripts I read only parts of the memory-tree and agent-instructions ones. All other adopters I saw only through the live apply runs. The research records, the architecture and the specs were grepped, except TOOL-dSafePassage-7, read whole, and the sections quoted from -2, -3, -6, -8, -24.
- **Line numbers.** Every `path:line` below was read at HEAD, unless it cites a spec.
- **Lookup.** `reuse_lookup.py` ran once. It reported no unscanned layers, but its shortlist was name-stem noise, so the seams below come from reading source.
- **Experiment.** I ran `govkit intake` and `apply --all` on two empty repositories under the scratchpad. The repository tree is unchanged. `scratch-guard` blocked one command, which set `HOME` and global git config. I removed both rather than work around it.
- **Parents.** Nothing named `TOOL-*`/`PLAY-*` below is built. The files they specify (`upgrade_steps.py`, `steps.toml`, `shims.py`, `tools/loop/`, `tools/runtime/`, `tools/playbook/core.py`, `kinds.toml`, `record-kinds.toml`) do not exist at HEAD.

## 1. One row per unit

**Unit 7: adopter register and currency watch**
- **Seam, adopter side:** `tools/run-gates/check-receipt.py`, shipped, reads the receipt with no gov checkout, leg at `tools/run-gates/kit.toml:156`. Extend via a sibling program in that kit.
- **Seam, probe:** `resolve_measurer_currency` (`tools/govkit/govkit.py:612`) has the `ls-remote` read and the rule that `unverified` is never green. govkit does not ship, so this is the second instance: extract a `tools/lib/` inline block, modelled on `remote_ladder_py` (`govkit.py:555-558`).
- **Seam, gov side:** `tools/govkit/adopters.toml:17-25` with its reader at `govkit.py:3742`. `census.py:122` needs a checkout, so it is shape reference only.
- **Exists:** no currency code. Rows hold only `key` and `names`.
- **Decides it:** layer-expansions:458-459, :463-467, :470-477; v2:1306-1308, :1315-1316; gap register:394; layer-memory:436-438.
- **Nodes:** `item.kits.currency`, `item.kits.adopters`, `record-kind.currency`, the five keys below.
- **Keys, each with a row but no summary or usage (on `unsummarised-keys.txt`):**

| Key | `tools/policy/catalogue.toml` |
|---|---|
| `deploy.currency` | :1034 |
| `currency.max-behind` | :1040 |
| `currency.on-behind` | :1046 |
| `kits.host` | :1089 |
| `kits.watch-cadence` | :1095 |

- **Paths:** `tools/govkit/adopters.toml`, `govkit.py`, new `tools/run-gates/check_currency.py`, new `tools/govkit/adopter_reading.py`, `tools/lib/`, `tools/run-gates/kit.toml`, `tools/policy/catalogue.toml`, `selftest.py`, help page.

**Unit 16: unattended `kits.offer`**
- **Seam, mode:** `_rerender_on` (`govkit.py:11227`) is today's only switch. Extend it into one mode predicate.
- **Seam, census:** `SHELL_EXEC_SITES` (`govkit.py:4731`), joined by selftest:12923. Give each row a mode disposition so a new spawn reds. This is the in-tree form of the `target_spawns.py` probe, which exists only as a record instrument.
- **Refuse points:**

| Kind | Function | Call sites |
|---|---|---|
| Parity probes | `derive_parity_lines` | :10035 (spawns at :6321) |
| Check baseline, then verify | `run_kit_check` | :10392, :11595 |
| Hole probes | `run_hole_probes` | :11330, :12181 |
| Regenerate | `run_target_argv` | :11363 |
| Fragment wiring | `run_fragment_merges` | :11469 |
| Gained adopters | `run_target_argv` | :11497 |

- **Exists:** nothing unattended. `update --write` stages and never commits or pushes.
- **Needs:** TOOL-dSafePassage-7 `build_step_env`, TOOL-dSafePassage-24 config check, TOOL-dWellOiledMachine-17 grant.
- **Decides it:** layer-expansions:460; gap register:403; v2:308, :314.
- **Node:** `item.kits.offer`. No key.
- **Paths:** `govkit.py`, `selftest.py`, new `tools/govkit/offer.py`, help.

**Unit 17: install and update hooks, migration, fresh install**
- **Seams:** `derive_install_order` (`govkit.py:911`), `resolve_selection` (:1098), `[[outcome]]` with `classify_outcome` (:6557), `_cmd_update` (:9154), `tools/memory-tree/migrate_backlog.py` (`--plan`, `--write`, `--stragglers`).
- **Exists:** verbs `intake`, `apply` and `update`. Ordering is `requires`-driven, but the edges are insufficient (see §2 item 5).
- **Needs:** TOOL-dSafePassage-2 walk, TOOL-dWitnessedBar-15 `legacy_ledger.py seed`, TOOL-dLinkedLibrary-8 `core.py adopt`.
- **Outcomes to close:** layer-expansions:461-462.
- **Nodes:** `item.kits.install`, `item.kits.update`, `item.kits.install-attended`, `item.kits.update-attended`.
- **Keys:** none.
- **Paths:** `govkit.py`, adopters and `kit.toml` for memory-tree, agent-instructions, kickoff-manifest, playbook-render, process-monitor, unattended, plus a migration step row, `WIRE-INTO-PROJECT.md`, `selftest.py`.

**Unit 18: every release updates gov first**
- **Seam:** TOOL-dSafePassage-8 `run_gov_first`, `check_gov_first`, source mode, all unbuilt. At HEAD `update` refuses gov at `govkit.py:9167`.
- **Left for this unit:** refuse a `kits.cut` tag at a SHA whose gov-first record is absent or red.
- **Decides it:** v2:877 (P8), layer-expansions:461.
- **Nodes and keys:** none.
- **Paths:** the cut program from unit 3, `selftest.py`.

**Unit 20: offer runs neither `adopt` nor `test.seed`, its order names both**
- **Seam:** `render_order_slug` (`govkit.py:5735`), the receipt `orders` list (written at :7984, read at :5653), TOOL-dSafePassage-2 S5's attended-order shape.
- **Exists:** orders, but none naming a hook run.
- **Decides it:** layer-expansions:460 (eighth kind).
- **Nodes and keys:** none.
- **Paths:** `govkit.py`, `selftest.py`.

**Unit 25: receipt schema 5**
- **Seam:** `RECEIPT_SCHEMA` (`govkit.py:49`), writers :7981 and :13030, the step pattern `govkit/receipt-schema-4` (TOOL-dSafePassage-3 S6), `run_step_isolated` (TOOL-dSafePassage-7 S3), `read_releases` (TOOL-dSafePassage-6).
- **Exists:** schema 3 at HEAD. Schema 4 is unbuilt. After it, the `update` re-stamp is `max(schema, 3)`, so only a step can raise a receipt.
- **Decides it:** v2:600, layer-expansions:442, gap register:402.
- **Nodes:** `record-kind.receipt`, `policy-key.install.from` (row at `catalogue.toml:1052`), `policy-key.install.steps` (row at :1652), both on the unsummarised list.
- **Paths:** `govkit.py`, `tools/run-gates/check-receipt.py`, `tools/govkit/matrix.py`, `selftest.py`, `tools/govkit/fixtures/make_adopter_receipt.py`, `census.py`, new `tools/govkit/steps/receipt_schema_5.py`, `help/upgrade-steps.md`.

**Unit 28: `adopt.declarations`**
- **Seam:** the TOOL-dLinkedLibrary-8 `core.py adopt` dispatcher, with TOOL-dLinkedLibrary-23 as the sibling to copy (propose each item, rule once). The dispatcher reserves only `instructions`, so a `declarations` verb is an addition. Rows land through the PLAY-dOrderedCharter-46 write door.
- **Inputs at HEAD:**
  - `tools/roles/house/policy.toml` through `load_policy` (`tools/roles/roles_lib.py:398`).
  - `receipt.gate_runner.emitted` against the manifest, to find hand-added legs.
  - `tools/unattended/.unattended.conf.example:265-382`, the `*_EXTRA` keys.
  - Role files under `tools/roles/agents/`.
- **Decides it:** flow-roles-adoption:145-147, :262-270; flow-steps:719.
- **Node:** `item.adopt.declarations`. It is an item, so no catalogue row. `roles.effort.*` is dBoundRoles' (TOOL-dBoundRoles-21).
- **Paths:** `tools/playbook/core.py` once built, new `tools/playbook/adopt_declarations.py`, `tools/loop/loop.toml`, the fixture.

**Unit 29: the update's report over every kind**
- **Seam:** the tally line (`govkit.py:10033`), and PLAY-dOrderedCharter-34 S6 `render_delta_report`, which `update` relays. The states come from PLAY-dOrderedCharter-35 S9, `derive_widenings` from PLAY-dOrderedCharter-36 S6.
- **Left for this unit:** every-repository-row lines, new gov rows upstream of a repository item in the needs graph, the widening comparison and its planted reds, and gap-deploy-28's separation of a lost change from unrelated holes.
- **Decides it:** flow-roles-adoption:213-217, :256-261; gap register:418.
- **Nodes and keys:** none.
- **Paths:** `govkit.py`, `tools/playbook/render_playbook.py`, `selftest.py`.

**Unit 31: the word fleet**
- **Seam:** `tools/govkit/adopters.toml`, plus the prose and identifier sites in §2 item 13.
- **Nodes:** `record-kind.adopter-register`, `record-kind.adopters`.
- **Writer:** a `govkit` registration verb, the owner's FK-11-2 (layer-memory:438).
- **Paths:** `adopters.toml`, `govkit.py`, `tools/codebase-map/README.md`, `map_lib.py`, `test_codebase_map.py` and its template, `WIRE-INTO-PROJECT.md`, optionally the drift-audit and unattended sites.

## 2. Where records and source disagree

1. **Spawn citations are stale by about 380 lines.** layer-expansions:460 and the gap register cite older lines. TOOL-dSafePassage specs cite correctly.

| Spawn | Cited | HEAD |
|---|---|---|
| Regenerate | :10986 | :11363 |
| Gained adopters | :11114-11119 | :11497 |
| `run_kit_check` | :10015, :11214 | :10392, :11595 |
| Fragment wiring | :11094 | :11469 |
| Hole probes | :10953, :11800 | :11330, :12181 |
| Parity | :9658, :6065 | :10035, :6321 |
| `--unwire` | :11304 | :11685 |
| `decline_findings` | :11949, run at :4757 | :12330, run at :5013 |
| `gov_source` | :8020, :12652 | :7981, :13030 |

2. **"Fifteen" git writes in `_cmd_update` is sixteen.** My count covers :9270 to :12165, including `git_pathspec` calls. The three in `land_through_index` and `write_gate_legs` are correct.

3. **The seven kinds, with `core.hooksPath` as the git answer, are incomplete.** TOOL-dSafePassage-24 reproduced `git add` running a local `filter.<x>.clean` under the contract's environment. `core.fsmonitor` and `diff.external` are the same class. A fresh throwaway clone does not carry the adopter's `.git/config`, so the mode needs either that clone or the -24 check. `hooksPath` alone is not enough.

4. **Clause 25's "`kits.currency` and the adopter register reading … shim calls" cannot hold for gov.** The journal is `govkit/shim-calls.jsonl` under the git directory (TOOL-dSafePassage-6 §4), and a working-tree journal was rejected at its :292. A remote read never sees it. Only the adopter's own `kits.currency` can read it. Also, a register holds rows, so the reader is `kits.adopters`.

5. **gap-deploy-27 is real, but ordering cannot close it.** With `manifest_path=memory/MANIFEST.md` and `playbook_path=docs/charter.template.md`:
   - `agent-instructions` exits 2, before the charter exists.
   - `memory-tree` seeds its conf and stops at exit 1, accepted.
   - A later run of its adopter gives the gap's refusal: `memory/ exists without a memory-tree marker`.

   But `memory/` comes from the kickoff seed at LAND, before any adopter, so reordering adopters cannot change it. No `agent-instructions` to `playbook-render` edge exists either. Other stops, none of them ordering:
   - `process-monitor` refuses blank `PROCMON_ROOTS`.
   - `playbook-render` refuses with no `CI_FILE`.
   - `unattended` stops at `no-project-layer`.
   - `roles` stops with exit 3.
   - `codebase-map` is blocked by the hole `map-extractors`.

   In that run the apply exited 1. With `playbook_path=AGENTS.md`, `agent-instructions` exits 0 instead, and `playbook-render` refuses because template and charter are one file. In that run 34 problems were reported. The clause's "seen on an empty repository" needs more than ordering.

6. **Clause 25 and gap-deploy-12 miss a second local path.** `intake` writes `gov_source` and `gov_commit` into `deploy.toml` (`govkit.py:13160`). That same-named key has readers (`tools/lib/render-doc.sh:268` tests `ans["gov_source"] == "."`). The receipt's key has no reader I could find by `git grep`, so removing it looks safe, but the deploy key must not be conflated. TOOL-dSafePassage-8's source receipt also writes `gov_source: "."` at schema 4, so schema 5 must say what a source receipt holds.

7. **Clause 25's reader inventory is too narrow.** Beyond govkit, matrix and `check-receipt.py`:
   - `tools/govkit/census.py:138`, `tools/govkit/census.test.sh:103`
   - `tools/check-install-prefix.test.sh:240`
   - `tools/govkit/fixtures/make_adopter_receipt.py:302`
   - many `selftest.py` receipt fixtures

8. **"Its messages … updated" is mostly gone after TOOL-dSafePassage-3.** Its S4 makes the message at `govkit.py:9380-9389` spell 3. Only the constant's comment stays owed.

9. **A "release-tag receipt with no `release`" has no marker.** The clause names no receipt field for `install.from`, and `check-receipt.py` reads no policy. No `gov/*` tag exists, only three `archive/*`, so every existing receipt lacks `release`.

10. **`kits.watch-cadence: every-session` has no period.** TOOL-dWellOiledMachine-59 S1 admits `daily` and `weekly` only.

11. **`session-start` and `cloud-routine` have no host row.** TOOL-dWellOiledMachine-13 leaves them to dShippedRelease and dTendedCadence, so `kits.host`'s default registers nothing until one of them acts.

12. **"A refused push → an outbox order" has no destination.** The outbox lives in the adopter's tree, which a refused push cannot reach. The same holds for an attended step stopped in a throwaway clone.

13. **The fleet claim has moved.** No source calls `adopters.toml` a fleet register, and `render_playbook.py` and `fleet.toml` use the word for nodes. The stale term lives in records, for example `TOOL-dSafePassage-6:101` and ownership:363. Two senses remain in source:
    - Adopters: `WIRE-INTO-PROJECT.md:545`, `tools/codebase-map/README.md:123`, `map_lib.py:62`, `test_codebase_map.py:194` and its template.
    - A third sense, all builds in a tree: the parsed line `unattended: check 23 fleet —` (`tools/unattended/check-unattended.sh:4415`) with its reader at `tools/drift-audit/drift_report.py:3197`, and `fleet_over_budget`. A rename there changes a parsed interface.

14. **Register fields are absent, and one row has no key.** `adopters.toml` has no remote, branch or grant. The `swydee` row has no `key`, so an `adopters` record cannot use the neutral key for it.

15. **The packet's parent status is stale.** It says `specs done no` for five parents, but their spec folders are populated. This matches your note.

16. **Clause 18 largely overlaps TOOL-dSafePassage-8.** Gov first runs at every landing there, so a release is a subset of that. Only the tag-side refusal is new.

## 3. Shared interfaces (proposed names)

**Within this group**
- `read_receipt_release(receipt) -> (release, source_remote, install_from)`: unit 25 owns it, units 7 and 31 read it.
- `OFFER_MODE`, a `SHELL_EXEC_SITES` disposition column: unit 16 owns it, unit 20 adds the hook kind, unit 25 adds the step kind.
- `render_attended_order(kind, argv, why)`: units 17 and 20 share one writer with TOOL-dSafePassage-2 S5's order.
- `adopter_rows(root)`, the one register reader: unit 31 owns it, used by unit 7 and by selfcheck arm 10.
- `derive_kit_report(...)`: unit 29 owns it, unit 16 records its unrun list through it.

**With other groups**
- `read_releases` and the tag grammar `gov/v<date>.<n>`: unit 3 replaces TOOL-dSafePassage-6's stand-in. Units 7, 18 and 25 read it.
- A gov-first witness, `read_gov_first(sha)`: read by unit 18 and the cut.
- `remote_probe_py`, the inline block: unit 7 owns it, govkit consumes it. Unit 26 and the emitted CI may too.
- `descriptor.requires` additions, shared with units 10 and 21 (kit factory, purpose field).
- A wiring verdict and Codex re-trust step at the update's close: unit 27 adds to unit 17's walk.

## 4. Order constraints

**Within the group:** 25 → 7 (needs `release` and `source_remote`) · 31 → 7 (register fields and record kinds) · 25 → 16 (ninth kind, step rows) · 16 → 20 · 17 → 28 and 29 (install and update carry them) · 3 → 18.

**Parent surfaces per unit**

| Unit | Needs, none built |
|---|---|
| 7 | TOOL-dWellOiledMachine-13, -59; dTotalRecall record kinds; TOOL-dSafePassage-6 journal; `catalogue` summaries, TOOL-dGroundRules-1 |
| 16 | TOOL-dSafePassage-2, -7, -24, -29; TOOL-dWellOiledMachine-17; PLAY-dOrderedCharter nothing direct |
| 17 | TOOL-dSafePassage-2, -4, -9; TOOL-dWitnessedBar-15; TOOL-dLinkedLibrary-8, -23; `tools/loop/loop.toml`, TOOL-dDeclaredLoop-12 |
| 18 | TOOL-dSafePassage-8, unit 3 |
| 25 | TOOL-dSafePassage-1, -3, -6, -7, -16 |
| 28 | TOOL-dLinkedLibrary-8, -23; PLAY-dOrderedCharter-35, -36, -46; TOOL-dBoundRoles-19, -20, -21, -23 |
| 29 | PLAY-dOrderedCharter-34, -35, -36; each kind's widening declarations; TOOL-dBoundRoles-20 |
| 31 | dTotalRecall record kinds, TOOL-dDeclaredLoop kinds only if the register is registered as a kind |

The `session-start` host row is shared with dTendedCadence, whose parents do not include dShippedRelease, so whichever lands first should extract it.

## 5. Forks

**Could not settle from source**
1. Where a refused push's order lands: gov's `adopters` record, a mailbox, or a new owner item (§2 item 12).
2. Whether the currency record is committed. layer-expansions:463-467 reads "the newest committed currency record", but a `session-start` hook cannot land a commit in an adopter.
3. Whether `deploy.currency` is one gov policy value or a per-register-row consent. A preset setting `push-branches` would otherwise apply to every adopter. Distribution research A's `channel` field fits the second.
4. What a schema-5 step writes for `release` on a commit-vintage receipt, given no tag exists (§2 item 9). Options: null with a declared `install_from: any-commit`, or wait for the first cut.
5. Whether an offer is possible at all for a kit with rendered files. Regenerate is refused, so the pushed branch may red at the adopter's bar on stale renders. That may reduce most offers to orders.
6. What "one pass" means for `memory-tree`'s deliberate seed-and-stop and `process-monitor`'s required roots. Options: more intake answers or a declared continuing stop. Either changes shipped adopters.
7. Whether a house `default` below medium is proposed as-is or held for TOOL-dBoundRoles-23's owner authorization. I did not read that floor's text in detail.

**Probably decidable by the spec writer**
8. Whether the mode is a fresh clone only, or a clone plus TOOL-dSafePassage-24's check. I would take both.
9. Whether the mode sets `build_step_env` on the whole process or per site. Whole process covers all sixteen writes, but `autocrlf` then falls away on this fleet.
10. Treat the push as a separate gov-side step, because the contract removes credentials from the update itself.
11. Whether `kits.adopters` uses a shallow fetch, as distribution research B proposes. `git archive --remote` may not be available on every host, which I did not test.
12. Whether `source_remote` is scrubbed for embedded credentials. TOOL-dSafePassage-38's predicate is the likely reuse.
13. Whether unit 31 renames the third `fleet` sense, or the clause reads as adopters only.
14. Whether `every-session` becomes a period kind in TOOL-dWellOiledMachine-59 or a non-period program.

Scratch evidence: `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-dshipped-release-1a351d\3b045209-e7b3-481f-972c-10cfbdeab2b1\scratchpad\fresh\apply.out` and `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-dshipped-release-1a351d\3b045209-e7b3-481f-972c-10cfbdeab2b1\scratchpad\fresh\apply2.out`
