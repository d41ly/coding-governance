# TOOL-aGatheredDeclaration-6 — every reader moves, and the second entry point closes

**Status:** CLOSED · rev-5 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md) | research | TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 |
| [2026-08-31-build-TOOL-aGatheredDeclaration-6-descriptor-census.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-6-descriptor-census.md) | research | — |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-7 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md) | diff-review | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |

<!-- /gen:spec-records -->

## 1. Goal

Move every reader of `tools/gate-legs.json` onto `gate-legs.toml`, retire the JSON, and make
`tools/run-gates/run-gates.sh` the SINGLE gate entry point by folding the second one into it. Until
this lands, unit 2's dual-format branch is carrying a format nobody should still be reading.

## 2. Scope (IN)

- **S1** — `tools/govkit/govkit.py`, and it is THREE changes rather than a filename. (a) A
  `toml-legs` member joins the grammar enum, which `govkit.py:2947` refuses by name today with
  `only 'json-array' is implemented` — a correct fail-closed refusal that this unit must answer
  rather than route around. (b) The writer becomes a TEXTUAL SPLICE between marker comments
  rather than a parse-and-reserialise, because Python ships no comment-preserving TOML writer and
  a reserialise would delete every argument this build exists to make storable. (c) The
  `[gate_runner_seed]` block gains the new file name AND its `grammar` key. `kit.toml:107`
  declares `grammar = "json-array"` on the line above `file`, and it is the ONLY place a
  target's grammar comes from — so without this, `toml-legs` has no producer anywhere in the
  build and a freshly intaken target declares a JSON grammar against a `.toml` file.
  `govkit.py:2947` accepts `None` or `json-array`, so nothing refuses: the grammar simply lies.
  (d) The emitter writes the `[bar]` table with ALL FOUR declared keys at the kit's shipped values —
  `enforce_ceilings = false`, `turnstile = false`, `default_ceiling` and `turnstile_ttl` — which is
  where `TOOL-aGatheredDeclaration-4` S7 and `TOOL-aGatheredDeclaration-5` S3 actually land, and what
  AC14 grades. rev-4 named two keys here and graded four there. (e) The DESCRIPTOR KEY MIGRATION: 68
  `subject = ` rows across 23 descriptor TOMLs, plus the selfcheck arms at `govkit.py:1235`, `:1239`, `:1264`, `:1271`,
  `:1285`, `:1290`, `:1322-1330`, `:4332-4334` and the `SUBJECT_FLOOR_RUN_GATES` pin at
  `:2971-2972`. The descriptor census: **18 rows across 11 files** under `entries/` and 50 rows
  across 12 other kits' `kit.toml`, re-derived in
  `build/2026-08-31-build-TOOL-aGatheredDeclaration-6-descriptor-census.md`. rev-3 said 21 under
  `entries/`, a figure carried from the round-2 audit without re-deriving — the class this build
  exists to remove, committed by the fold that was fixing it — and rev-4 corrected it three sentences
  below while leaving the wrong figure standing above, which is the class one level up.
  rev-2 priced govkit at three edits; S1b's own premise, *once `subject` is gone*,
  is the trigger for every one of them.
- **S12** — a below-floor INTAKE. The probe is ONE CANONICAL SOURCE inlined per this kit's
  no-gov-internal-dependency rule, gated the way `resolve_python` already is — not a shared file,
  because S12's caller is `tools/govkit/govkit.py` (Python, gov-internal) and
  `TOOL-aGatheredDeclaration-7` S9's is `tools/run-gates/adopt-run-gates.sh` (bash, shipped into
  every target), and no single file can be both. S1(c) makes a freshly intaken target declare a `.toml` file and
  a `toml-legs` grammar; a target whose resolved python predates 3.11 then has a declaration it
  cannot read and NO legacy pair to fall back to, because intake writes only the new file.
  Intake probes the target's interpreter and emits the JSON manifest instead, saying so. **It cannot
  emit "the legacy pair"**: S7 deletes `tools/run-gates/gate-profiles.txt` and the kit payload is
  `include = "**"`, so after S7 there is no profile table left for any intake to ship. The declared
  consequence is that a below-floor target runs on the runner's BUILT-IN formula, which is what the
  profile table's own header already calls the documented rollback for that mechanism, and
  `TOOL-aGatheredDeclaration-7` AC8b's refusal is scoped so it cannot fire on a target gov itself
  created this way.
- **S1b** — the SUBJECT RATCHET moves with the key it pins. `govkit.py:1354` resolves each leg's
  subject against `tools/govkit/subject-pins.tsv`, defaulting to `repo`. Once `subject` is gone,
  all 40 kit legs resolve to that default and `govkit selfcheck` — `chunk = declarations`,
  `subject = repo`, no guard, so on every bar — reds once per leg. Clearing it with
  `selfcheck --write` is worse than the failure: the ratchet whose purpose is that a subject
  cannot move without appearing in a diff would record the ENTIRE population moving, as a
  generated file. The pin file pins `opt_in` and moves in the same commit.
- **S2** — `.githooks/pre-push`: reads the TOML for its manifest-moved test and its blob compare.
  This is also where `TOOL-aBoundedCeiling-7` is fixed — the hook hardcodes `tools/gate-legs.json`
  and `tools/run-gates/gate-fingerprint.sh` while the install prefix is configurable, so a target at
  another prefix has a hook that cannot find its own gate.
- **S3** — `tools/drift-audit/drift_signals.py` and its `.template.py` twin.
- **S4** — `tools/codebase-map/map_extractors.py`, whose `_gate_legs` inventory keys the map's
  `gate-legs` population.
- **S5** — the SECOND ENTRY POINT closes, and the leg count does NOT move. Re-derived by matching
  ARGV rather than label: the script issues EIGHT `run_one` calls, not seven. THREE of them
  already have manifest rows — `unattended kit gate`, `playbook validity gate`,
  `unattended skill wiring` — and those route through `run-gates.sh --leg`. The other FIVE are
  the suites the 2026-08-23 owner ruling removed from the bar, and they STAY OFF it: the wrapper
  keeps dispatching them directly. **That is not a second gate entry point**, because they are
  not declared legs; the single-entry-point rule governs what the manifest declares, and the
  owner ruled these out of it. Folding them back in as `opt_in` rows would take the manifest
  86 -> 91 and partially reverse a governance ruling, which M3's veto 2 puts outside a mandate's
  delegated authority. rev-2 said "the seven legs it holds" and rev-3 kept it; both the count
  and the disposition were wrong.
- **S6** — the carriers that NAME the entry point to a session: `AGENTS.md`'s merge-bar section,
  `coding-governance-agents.template.md`, and whatever `tools/playbook/` renders from them. The
  command block gains the sharding verbs and drops nothing.
- **S7** — the LEGACY PAIR is deleted: `tools/gate-legs.json` AND
  `tools/run-gates/gate-profiles.txt`. Unit 2's dual-format arm keeps reading the pair in an
  adopter or below the interpreter floor; gov itself carries neither. Retiring the profile table
  is four further edits nobody owned at rev-1: its `[[lf_pin]]` at `tools/run-gates/kit.toml:146`,
  the `GATE_PROFILES` override the table's header calls the documented rollback for the whole
  mechanism, `run-gates.test.sh:1241-1242` which REDS if the kit README stops naming the file, and
  `run-gates.gov.test.sh:234-235` which reds if the charter does.
- **S7b** — the two canaries' GUARD LISTS name `tools/gate-legs.json` and move to the TOML in the
  same commit. `run-gates.test.sh:268-283` fails on a guard pathspec matching no tracked path, so
  leaving them is a leg that skips forever.
- **S9** — `tools/check-testsuite-counts.sh` and the other carriers in the inventory above move.
  The checker's population selector reads the manifest BYTES with a regex over quoted `.test.sh`
  strings, which needs restating for TOML rather than repointing.
- **S10** — `tools/dead-path-waivers.txt` gains one row per SURVIVING carrier of the string
  `gate-legs.json`. `tools/check-dead-paths.sh:76-84` derives its needles as BASENAMES from the
  deletion log minus every basename the tree still carries, then greps every tracked file outside
  `memory/`. **31 tracked files outside `memory/` carry that string today**, 30 of them surviving
  the deletion — the loader's own legacy branch, the hook and its test, `kit.toml`, the adopter
  fixtures. The permanent ones are reasoned as *a live path in an adopter, dead only in gov*. The
  waiver file's shrink-only header is being ratcheted the WRONG WAY in this one commit, and that
  is said here rather than discovered in the diff.
- **S11** — the SOURCE of the entry-point sentence is `.governance/deploy.toml:44`'s
  `gate_commands`, not `AGENTS.md`. `coding-governance-agents.template.md:180` carries
  `{{GATE_COMMANDS}}`, `AGENTS.md:250` is that value RENDERED, and it sits inside the
  `<!-- gov:playbook -->` region between `AGENTS.md:76` and `:470`. rev-2's S6 had the direction
  backwards: the renderer reads deploy.toml plus the template and WRITES the charter, so a hand
  edit inside the region is reverted by the next render. `.codebase-map.conf:13` carries the same
  string and is the second source. The merge-bar section BELOW `:470` is gov-authored and is
  edited directly.
- **S8** — the `run-gates` map dossier at `memory/map/features/run-gates.md` is refreshed: its
  `[paths]` globs and its `[claims]` gain the new file, which the map's coverage gate requires in
  the same commit as the claim edit.

## 3. Non-goals (OUT)

- Removing the JSON arm from the loader. Adopters upgrade on their own schedule; unit 7 is the tool,
  not a deadline.
- Changing what any of these readers CONCLUDES. Each reads a different file and reaches the same
  verdict; a reader whose behaviour changes here is a defect, not a feature.
- Fixing `TOOL-aBoundedCeiling-7`'s sibling problems. Only the two hardcoded paths this unit already
  has to touch are in scope; the row stays open for the rest if any remain.

## 4. Design

### Inventory

| reader | what it reads it for | change |
|---|---|---|
| `run-gates.sh` | dispatch | done in unit 2 |
| `govkit.py` | emit + selfcheck join | S1 |
| `.githooks/pre-push` | manifest-moved force, blob compare | S2 |
| `drift_signals.py` (+ template) | dead-path signal over leg argv | S3 |
| `map_extractors.py` | the `gate-legs` inventory | S4 |
| `run-unattended-gates.sh` | its own dispatch | S5, folded away |
| `check-testsuite-counts.sh` | its POPULATION, selected by grepping the manifest BYTES | S9 |
| `check-memory-hygiene.sh`, `template-size-limits.txt`, `drift-audit-state.js` | each names the file | S9 |
| `tools/run-gates/profile_bar.py` | reads the manifest to profile the bar | S9, AC15 |

**The inventory at rev-1 was certified by a grep nobody re-ran, and the grep refutes it.**
`tools/check-testsuite-counts.sh:27` hardcodes `MANIFEST=tools/gate-legs.json` and `:32` HARD
EXITS 2 when it is absent, with the message that the population would otherwise be empty and the
leg would pass by finding nothing. Its manifest row is `chunk = declarations`, `subject = repo`,
no guard — so it runs on EVERY bar, including a records-only one, and S7's deletion reds the
default bar at this unit's own landing.

### Migration

Ordered, and the order matters: S1 through S4 land first with the JSON still present, so each
reader is proven against a tree where both files exist and agree. S7 deletes the JSON last. A reader
moved and a file deleted in one commit gives a red no bisect can localise.

### Rollout

S5 is the only behaviour change a person will notice: `bash tools/unattended/run-unattended-gates.sh`
keeps its name and its output shape. **NOTHING moves into the declaration**: S5 rules that the
three legs already declared route through `--leg` and the five suites the 2026-08-23 owner ruling
removed keep being dispatched by the wrapper, off the bar. rev-2 wrote the opposite here and rev-4
rewrote S5 without opening this paragraph, so the replaced disposition survived the fold that
removed it — attributing to that ruling the very reversal it forbids.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/registry.toml` · `.githooks/pre-push` ·
`.githooks/pre-push.test.sh` · `tools/drift-audit/drift_signals.py` + `.template.py` ·
`tools/codebase-map/map_extractors.py` · `tools/unattended/run-unattended-gates.sh` ·
`tools/check-testsuite-counts.sh` · `tools/govkit/subject-pins.tsv` · `tools/run-gates/kit.toml` ·
`tools/gate-legs.toml` (the guard lists) · `tools/dead-path-waivers.txt` ·
`.governance/deploy.toml` · `.codebase-map.conf` · `tools/govkit/entries/*.kit.toml` and every
other kit's `kit.toml` `[[gate_leg]]` rows · `tools/run-gates/profile_bar.py` · `AGENTS.md` ·
`coding-governance-agents.template.md` · `memory/map/features/run-gates.md` · `tools/gate-legs.json`
and `tools/run-gates/gate-profiles.txt` (both deleted) · the affected suites.

### Alternatives rejected

**Move every reader in unit 2's commit.** One commit touching the runner, the deployer, the hook,
two audits and the charter is a diff no closing review can localise a finding in. The dual-format
branch exists precisely so this can be a second landing.

## 5. Production-readiness checklist

- security — `.githooks/pre-push` is a trust boundary and S2 changes what it reads. Its selftest
  covers the classification arms and must still pass unchanged.
- perf / scale — S5 removes a duplicate dispatcher. No other reader is on a hot path.
- a11y, i18n — N/A.
- error / empty / loading states — each moved reader keeps its existing refusal for an absent or
  malformed manifest; a reader that silently tolerated an absent JSON must not silently tolerate an
  absent TOML.
- observability — N/A beyond what unit 3 adds.
- risks — a partially moved reader set is the whole risk, and the ordered migration is the answer.
  `check-dead-paths.sh` is the backstop: a carrier still naming the deleted JSON reds.
- testing + left-shift gates — each moved reader's own suite, plus the dead-path leg.
- migration / rollback — revert S7 first; the loader's JSON arm makes that sufficient.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py` emits a target's manifest, the file written is
  `<prefix>/gate-legs.toml` and its rows match the selected descriptors' `[[gate_leg]]` blocks,
  asserted in `tools/govkit/selftest.py`.
- **AC2** — When `.githooks/pre-push` runs in a target installed at a prefix other than `tools`, it
  resolves the manifest and the fingerprint helper at that prefix, asserted in
  `.githooks/pre-push.test.sh` with a scratch repo installed at `scripts/`. Observed RED first —
  this is `TOOL-aBoundedCeiling-7`.
- **AC3** — When `python tools/drift-audit/drift_report.py` runs, its gate-legs signal reports the
  same population from the TOML that it reported from the JSON, asserted by running both at the
  commit where both files exist.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py` runs, the `gate-legs` inventory key
  count is unchanged across the format move, asserted the same way.
- **AC5** — When `bash tools/unattended/run-unattended-gates.sh` runs, it dispatches through
  `run-gates.sh --leg` for the THREE legs the manifest declares, and those three names appear in
  the runner's own summary, asserted by grepping the runner's report tail rather than a message this
  script prints. The other five never appear there and must not be asserted to: they are dispatched
  by the wrapper and are not declared legs.
- **AC6** — When `bash tools/check-dead-paths.sh` runs after S7 and S10, it is GREEN with the
  declared waiver set, and a CONTROL arm planting a fresh undeclared carrier still REDS.
  **rev-2's wording was unsatisfiable**: the gate's predicate is a BASENAME, and
  `TOOL-aGatheredDeclaration-2` S3 makes the loader's legacy branch spell `gate-legs.json`
  permanently, so "no carrier names it" and the permanent dual-format arm cannot both hold. The
  control arm is what stops the waiver edit widening the surface it was written to narrow.
- **AC11** — When `python tools/govkit/govkit.py selfcheck` runs with no `subject` key anywhere in
  the tracked descriptor population, it is GREEN, asserted after S1(e)'s migration. A grep for a
  surviving `^subject = ` row is the same arm's second half, so a kit added later cannot
  reintroduce the key.
- **AC12** — When a target is freshly intaken, its emitted `[gate_runner]` block carries
  `grammar = "toml-legs"` and a `.toml` `file`, asserted in `tools/govkit/selftest.py`. Without
  it the grammar lies and nothing refuses.
- **AC13** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs after S11, it is
  GREEN, asserted as its own arm. A hand edit inside the rendered region passes every other
  criterion here and is reverted by the next render.
- **AC14** — When a full intake runs into a scratch target, the EMITTED
  `<prefix>/gate-legs.toml` is parsed and its `[bar]` table carries ALL FOUR declared keys with
  the kit's shipped values, asserted key-by-key in `tools/govkit/selftest.py`, where this unit's
  other intake arms sit. This is where `TOOL-aGatheredDeclaration-4` S7 and
  `TOOL-aGatheredDeclaration-5` S3 are graded; both DECLARE the default and neither can grade it,
  because the emitter is here.
- **AC15** — When `python tools/run-gates/profile_bar.py` runs after S7, it profiles the bar from
  the TOML, asserted by `tools/run-gates/profile_bar.test.sh` — already a leg. Without this the
  reader degrades to a state nothing observes.
- **AC16** — When the emitter re-writes a target's manifest, every comment OUTSIDE the marker
  region survives byte-identically, asserted in `tools/govkit/selftest.py` by planting a sentinel
  comment in the authored half and re-running the emit. Observed RED first against a parse-and-reserialise implementation,
  which is the one this criterion exists to forbid.
- **AC17** — When a below-floor target is intaken, it receives the legacy pair and a line saying
  why, never a TOML it cannot read, asserted in `tools/govkit/selftest.py` against a stub
  interpreter. Observed RED first.
- **AC18** — When `bash tools/unattended/run-unattended-gates.sh` runs after S5, the leg count in
  `tools/gate-legs.toml` is DERIVED and equals its pre-S5 value with a stated delta of zero,
  asserted by counting both. rev-3 wrote the word "unchanged", which cannot survive a scope item
  that changes it — and this is the third round in which a prose count in this build disagreed
  with the tree.
- **AC7** — When `bash tools/run-gates/run-gates.sh --leg "run-gates canary" --leg "run-gates gov
  canary"` runs on this tree with the legacy pair deleted, both are GREEN. **Sharding, not
  `GATE_SELFTESTS=1`**: both canaries are `chunk = selftests`, so a DEFAULT bar holds them and
  rev-1's wording would have passed green over two guard pathspecs pointing at a deleted file —
  but rev-2's blanket `GATE_SELFTESTS=1` would have executed the five suites the 2026-08-23 owner
  ruling removed from the bar. `TOOL-aGatheredDeclaration-3`'s `--leg` runs exactly the two arms
  that grade guard liveness and nothing else, which is this build using its own new capability.
- **AC9** — When `bash tools/check-testsuite-counts.sh` runs after S9, it derives the same
  population from the TOML that it derived from the JSON, asserted by running both at the commit
  where both files exist. Observed RED first against the unmoved checker.
- **AC10** — When a leg's `opt_in` value is flipped against an unchanged
  `tools/govkit/subject-pins.tsv`, `python tools/govkit/govkit.py selfcheck` REDS naming that leg.
  Observed RED first, and asserted without `--write` anywhere in the arm.
- **AC8** — When `python tools/codebase-map/check_map.py` runs, the `run-gates` dossier claims the
  new file and no unclaimed key remains, asserted by the map coverage leg.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selfcheck` · `pre-push hook selftest` ·
`drift-audit selftest` · `codebase-map coverage` · `dead paths` · `unattended kit gate` ·
`check-wiring` · `testsuite counts` · `profile-bar selftest` · `template size <=48KiB` ·
`charter size` ·
`playbook render wiring` · `playbook placeholder catalogue` · `playbook parity`. The size pair is
here because S6 edits `coding-governance-agents.template.md` and `AGENTS.md`, both size-gated;
the playbook trio is here because S11 edits the render's SOURCE and all three are
`subject = repo` with no guard, so they run on every bar. rev-1 listed none of the five and rev-2
listed two. No new leg.

## 8. Open questions

- **F1 — does `run-unattended-gates.sh` survive at all, or is `--leg` enough?** With unit 3 landed,
  `bash tools/run-gates/run-gates.sh --leg "<name>" --leg "<name>" …` is the same command with the
  names spelled out. Keeping the wrapper is a named entry point an adopter's docs can point at;
  deleting it is one fewer thing. Recommendation: keep it, because it is what the kit's own
  descriptor names as the compensating check for legs held off the bar, and a compensating check
  that becomes a spelled-out argument list is one nobody runs.
  RESOLVED (agent, 2026-08-31, delegated): keep it as a thin wrapper. It satisfies the stated
  requirement — one dispatcher — while keeping the named check the exemption depends on.

## 9. Revision log

- rev-6 · 2026-08-31 · CLOSED on a DESCOPED scope, and the descope is the point of this line.
  SHIPPED: S2 (the push boundary — both predicates, and the install-prefix fix that is
  `TOOL-aBoundedCeiling-7`) and S5 (the second entry point folded into the first).
  NOT SHIPPED: S1 govkit's `toml-legs` grammar and its comment-preserving splice writer,
  S1(e) the 68-row `subject` -> `opt_in` descriptor migration, S3 `drift_signals.py`,
  S4 `map_extractors.py`, S9 `check-testsuite-counts.sh`, S10 the dead-path waiver set,
  S11 the `.governance/deploy.toml` render source, S12 the below-floor intake, and S7 the
  deletion of the legacy pair. Carried forward as a backlog row rather than left implied.
- rev-1 · 2026-08-31 · initial draft.
- rev-5 · 2026-08-31 · folded round-4 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md`), the round that
  ended the loop NON-CONVERGENT. Findings B1, H1, H3, H5, H6 and H7. B1 is the round's
  most-confirmed finding, five hits across three lenses: rev-4 rewrote S5 and left the Rollout
  paragraph and AC5 prescribing the disposition and the count it had just removed. H6 is the same
  shape one level up — rev-4 corrected a figure three sentences below the wrong one and left the
  wrong one standing.
- rev-4 · 2026-08-31 · folded round-3 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md`) findings R1, R3, R6, R8, R10, R11 and R14. The
  Rollout added leg rows while AC7 sixty lines below asserted the count was unchanged, and the
  disposition folded five suites back onto a bar an owner ruling had removed them from — outside
  a mandate's authority, so S5 now keeps them off and routes only the three declared legs through
  `--leg`. The whole emitted `[bar]` table, the comment-preserving splice, `profile_bar.py` and a
  below-floor intake each gained a criterion. The descriptor census was re-derived after rev-3
  carried a figure it had not checked.
- rev-3 · 2026-08-31 · folded round-2 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md`) findings R1, R3,
  R5, R6, R7 and R12. AC6 was unsatisfiable beside unit 2's permanent legacy branch and its
  landing would have redded a leg that runs on every bar, with the waiver file owned by nobody.
  govkit was priced at three edits against 68 descriptor rows and nine selfcheck sites. The
  entry-point sentence is owned by `.governance/deploy.toml`, not by the charter S6 proposed to
  edit. The seed's `grammar` key had no producer. `profile_bar.py` was still missing from an
  inventory rev-2 had just re-certified.
- rev-2 · 2026-08-31 · folded round-1 spec audit findings F1, F2, F7, F20, F27 and F28. The
  reader inventory was incomplete in the one direction that reds the default bar, and the grep
  rev-1's Section 10 cited as its evidence is what found the gap. The subject ratchet, the
  profile table's retirement, the two canary guard lists, the govkit grammar enum and two size
  gates each gained an owner.

## 10. Reuse audit

No new seam. Every change here is at a reader that already exists and already resolves its own path;
the work is changing what each resolves TO. The one place a seam is being CREATED rather than
extended is S5, and it consumes unit 3's `--leg`, which is why the two are separate units in the
same build rather than one.

The reader inventory in §4 was derived by grepping `gate-legs` across the tree, which is the
exhaustive form of the question a map probe answers by ranking. **The grep is the evidence here and
the probe is not**, stated so the difference is visible rather than implied.

The recall probe run for `TOOL-aGatheredDeclaration-7` reaches this unit and changes it:
`memory/builds/dUnstalledConvoy/reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-spec-rev2.md:328`
records that on an upgrade re-apply govkit fires `a leg that vanished is not a leg that passed`
once per MIGRATED leg, naming the wrong cause. **The line numbers that record cited are stale at
this base and are deliberately not repeated**; the behaviour was re-confirmed from the record and
the site is not re-cited rather than cited wrongly. S1 moves the emitter, so every leg in
every target becomes a migrated leg exactly once. **AC1 is not sufficient on its own for that**, and
the S1 work must either avoid the branch or the build must record that adopters meet it once. It is
carried as a known consequence rather than silently discovered at an adopter.
