# TOOL-aSealedCaravan-1 — one declared install prefix, and the gates that make it true

**Status:** SPECCED · rev-3 · 2026-08-10 · node a · Tier-2 · base 16aeb5ef · streams tooling

## 1. Goal

Declare `tools/<kit>/` the single install prefix for every kit a new adopter lands, and close the four
silent-green failures the unresolved prefix question already causes. An adopting repo that follows
`WIRE-INTO-PROJECT.md` today puts its kits in five different homes, because the runbook prescribes
five; the gates that should notice a wrong prefix report success instead.

## 2. Scope (IN)

- **S1** `tools/<kit>/` is the declared install prefix in `WIRE-INTO-PROJECT.md` and in every kit
  README, replacing the five homes inventoried in section 4. The prefix is exactly ONE segment, and
  the runbook states that ceiling rather than leaving it to be discovered: the codebase-map gate
  template resolves only `<ancestor>`, `<ancestor>/codebase-map` and `<ancestor>/*/codebase-map`
  (`tools/codebase-map/test_codebase_map.template.py:41`), and `adopt-codebase-map.sh:107` refuses a
  two-segment prefix before writing anything.
- **S2** The two non-kit installs move with it. `manifest-check.sh` lands at `tools/manifest-check.sh`
  instead of `scripts/`, and the review harness lands at `tools/workflows/` instead of `workflows/`.
  `.claude/hooks/agent-cap.js` does NOT move: `tools/settings-merge.py:57` hardcodes that literal as
  the fragment's hook path and `tools/check-wiring.sh:95` probes it, so it is a Claude Code path
  rather than a kit path.
- **S3** `tools/memory-tree/adopt-memory-tree.sh` derives its own repo-relative path and prints it,
  replacing the hardcoded hints at its lines 151 and 153. It is the last of the four shell adopters
  that does not already do this.
- **S4** `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md` carry a kit-path placeholder that
  `adopt-memory-tree.sh` substitutes at scaffold time, so a target's committed `memory/HYGIENE.md`
  names kit paths that exist in that repo.
- **S5** Hygiene check 15 stops being structurally blind to a wrong-prefix citation.
  `tools/memory-tree/corpus_ids.py:231` classifies a citation as a repo path only when its first
  segment is a tracked top-level directory, so at a `tools/` prefix a `memory-tree/x.sh` citation is
  never considered at all.
- **S6** `SKILL.template.md` in the drift-audit kit stops naming `workflows/drift-audit-code.js` and
  `workflows/drift-audit-state.js`. Both live at `tools/workflows/`, and the rendered
  `.claude/skills/drift-audit/SKILL.md` in this repo carries the same dead spelling.
- **S7** Two guards stop skipping silently at a non-`tools/` prefix. `tools/hooks/agent-cap.test.sh`
  gates its two-copy parity arm on a literal `tools/hooks/agent-cap.js`, and `.githooks/pre-commit`
  gates each of its three legs on a literal path. Each gains a population assertion: a skip names the
  path it looked for, and a guard that finds a kit installed elsewhere FAILS naming that kit rather
  than reporting success.
- **S8** A new merge-bar leg proves the declaration mechanically: no file that is copied or rendered
  into a target repo spells a root-install kit path. The predicate, its measured population and its
  waiver registry are in section 4, measured rather than estimated.
- **S9** The memory-tree kit ships its own launcher, `tools/memory-tree/merge-rows.sh`, so a
  copy-installed kit can start its merge driver. `tools/lib/` is NOT delivered to adopters and does
  not become a kit — see section 4. `check-wiring.sh` probes the kit-internal launcher alongside the
  two `tools/lib/pyrun.sh` spellings it already resolves.
- **S10** The fourteen provably false runbook claims listed in section 4 are corrected as part of the
  rewrite.
- **S11** The five stale records listed in section 4 are corrected, headed by the charter line at
  `AGENTS.md:94`. Each gets its own named assertion in section 6; one grep does not stand in for all.
- **S12** Every kit entrypoint's USAGE HEADER and every remedy string spells `tools/<kit>/`. These are
  the copy-paste surface: `check-memory-hygiene.sh:8`, `drift_report.py:6`, `adopt-memory-recall.sh:4`,
  `adopt-drift-audit.sh:9` and `drift_signals.template.py:5` all print a root-prefix command an
  adopter runs verbatim. `gen_build_index.py:42` is the sharpest case — its `GEN_HEADER` is STAMPED
  INTO every generated artifact in the target, so a wrong prefix is committed to the adopter's tree.
- **S13** The three cross-kit path references outside any kit README: the shipped
  `tools/workflows/REVIEW-PROTOCOL.template.md`, which no other scope item converts and which its own
  parity gate compares prefix-blind; `skills/session-kickoff/SKILL.md:58`, the kickoff engine's
  default map-diff command; and `parallel-coding-governance.template.md:148`, which names
  `workflows/tier2-review.js`.

## 3. Non-goals (OUT)

- Retrofitting existing adopters. Owner-stated: the prefix applies to new and future adopters only.
  `swydee` and `nicocares` keep their root installs, and every dual-spelling probe that supports them
  stays — which is why those probes are the waiver set in section 4 rather than defects.
- Changing any engine's root resolution. All ten engines already resolve the repo root from git or
  from a walk-up for a root-anchored config, and all ten already work at `tools/`. This unit changes
  prose, rendered artifacts, remedy strings and gates.
- A `KIT_DIR` configuration key. No prior record refused one; this unit is the first to. The reason is
  `TOOL-aRootedPrefix-1c`'s: resolution answers WHERE by walking up for the kit's own config, and a
  declared prefix would be a second place to be wrong.
- Two-segment prefixes such as `tools/gov/<kit>/`. Refused by the codebase-map kit and by nothing
  else, which would half-adopt every other kit.
- The deployer. That is `DEPL-aSealedCaravan-2`, and it consumes this unit's declaration.
- Marker-fencing the playbook's conditional blocks. The 2026-07-12 research resolved to do it while
  one live instantiation existed; measured today, the template carries zero such fences, so the
  window that resolution assumed has closed. Re-cost it in its own unit.
- Extending `check-arms.py` to Python sources. Named in `DEPL-aSealedCaravan-2` section 8 as fork F3.

## 4. Design

The engines are not the problem. Every kit resolves its own root, and this repo dogfoods all ten at
`tools/`. What breaks at a prefix is everything around them: prose, remedy strings, rendered
artifacts, and cross-kit gates that spell a prefix literally. Three mutually inconsistent conventions
ship today — the kits' own docs spell paths root-relative, the workflows gates and
`check-kit-versions.sh` hard-bind to `tools/`, and the runbook prescribes five homes.

### Inventory

The five homes the runbook prescribes today, and where each lands under this unit.

| Artifact | Today | Prescribed at | Under S1/S2 |
|---|---|---|---|
| memory-tree kit | `<project>/memory-tree/` | `WIRE-INTO-PROJECT.md:103` | `tools/memory-tree/` |
| codebase-map kit | `<project>/codebase-map/` | `WIRE-INTO-PROJECT.md:176` | `tools/codebase-map/` |
| memory-recall kit | `<project>/memory-recall/` | `WIRE-INTO-PROJECT.md:228` | `tools/memory-recall/` |
| drift-audit kit | undocumented | nowhere | `tools/drift-audit/` |
| review harness | `<project>/workflows/` | `WIRE-INTO-PROJECT.md:394` | `tools/workflows/` |
| manifest ratchet | `<project>/scripts/` | `WIRE-INTO-PROJECT.md:303` | `tools/manifest-check.sh` |
| settings-merge | `<project>/tools/` | `WIRE-INTO-PROJECT.md:263` | unchanged |
| check-wiring, push-main | `<project>/tools/` | `WIRE-INTO-PROJECT.md:360` | unchanged |
| agent-cap hook | `.claude/hooks/` | `WIRE-INTO-PROJECT.md:377` | unchanged, per S2 |

Only codebase-map already documents that its prefix is free. The memory-recall instruction is the
strongest root assertion in the file and is false: `tools/check-wiring.sh:122` accepts both spellings
and `adopt-memory-recall.sh:36` derives its own. Only the kit dir NAME is load-bearing.

### The four silent-green failures

Each was proved cold in a throwaway repo, not inferred. These are the reason this unit is Tier 2
rather than a documentation pass.

| Failure | Mechanism | Scope item |
|---|---|---|
| A target's own rule-set document ships dead paths | `adopt-memory-tree.sh` copies `HYGIENE.template.md` verbatim; at a `tools/` install its seven kit-path occurrences are all wrong, and the hygiene gate exits 0 | S4, S5 |
| Check 15 cannot see them | `corpus_ids.py:231` skips any citation whose first segment is not a tracked top-level dir; `memory-tree/` is not one at a `tools/` prefix | S5 |
| agent-cap's two-copy parity arm disarms | `agent-cap.test.sh:216` gates on a literal `tools/hooks/agent-cap.js`; a scratch repo with the kit elsewhere and NO wired copy at all reported 39 passed, exit 0 | S7 |
| Every pre-commit leg skips | `.githooks/pre-commit:26,32,37` gate on literal paths with no population assertion, then exit 0 | S7 |

Only three of `HYGIENE.template.md`'s seven occurrences are in a token shape check 15 could ever see,
so S5 closes three and S4 closes all seven. That split matters for acceptance and is why AC4 and AC3
are separate criteria rather than one.

A fifth is live in this repo rather than hypothetical: `.claude/skills/drift-audit/SKILL.md:72`
instructs an agent to run two files that do not exist, and
`bash tools/drift-audit/adopt-drift-audit.sh --check` prints "in sync" because
`SKILL.template.md:72` carries the same wrong spelling with no placeholder. The render parameterizes
its own kit dir and hardcodes a sibling's. That is S6.

### The enforcement gate, measured

S8 adds `tools/check-install-prefix.sh` plus its self-test. The naive predicate — any kit-dir name
followed by a slash, over `tools/**`, `skills/**`, every `*.template.*` and `*.fragment.json`,
`.githooks/**` and the playbook with its two companions — was RUN at base over its 99 tracked files
before this section was written, per the recorded trap. It fires **95 times across 37 files**. That is
not a waiver list; it is a different unit.

Two narrowings make it the gate this unit actually wants, and both are principled rather than
convenient. First, the match must be a RUNNABLE path — a kit name followed by a filename with an
extension — because a bare `memory-tree/` in prose names the kit, not a path an adopter executes.
Second, the population excludes `*.test.sh`, `*.test.py`, `selftest.py` and `*.conf.example`, because
those fixtures build root-prefix installs ON PURPOSE, to prove the dual-prefix support this unit keeps
by non-goal; gating them would forbid testing the thing the non-goal preserves.

Narrowed, over 74 files: **50 hits across 22 files**. Measured distribution:

| Disposition | Files | Hits | Which |
|---|---|---|---|
| Closed by S4 | 2 | 9 | `HYGIENE.template.md`, `SPEC-TEMPLATE.template.md` |
| Closed by S3 | 1 | 4 | `adopt-memory-tree.sh` |
| Closed by S1 (kit READMEs) | 4 | 11 | memory-tree, memory-recall, drift-audit, codebase-map |
| Closed by S6 | 1 | 2 | drift-audit `SKILL.template.md` |
| Closed by S12 (usage headers, remedy strings) | 8 | 15 | incl. `gen_build_index.py`'s `GEN_HEADER` |
| Closed by S13 (cross-kit references) | 3 | 5 | `REVIEW-PROTOCOL.template.md`, kickoff `SKILL.md`, playbook |
| WAIVED | 3 | 4 | see below |

The waiver registry is a tracked file in the gate's own directory, one path and line per entry with
its reason, seeded at **4 entries** and pinned shrink-only. Every entry is a deliberate root spelling:

| Entry | Why it stays |
|---|---|
| `check-wiring.sh:122` | the `first_of` dual-prefix probe for the memory-recall fragment |
| `check-wiring.sh:265` | the same probe for the merge driver |
| `map_lib.py:1165` | `REGEN_CMD`, preserved for adopters carrying a pre-1.1 gate the maintenance rule never overwrites; documented in-source at `:1160` |
| `codebase-map/.codebase-map.conf.example` | the shipped example's `MAP_DIFF_CMD` default, re-stamped by the adopter at install |

S12 and S13 exist because running the predicate found them; at rev-1 they were fifteen and five hits
with no owning scope item, and the builder would have met them mid-commit-3.

### Why `tools/lib/` is not delivered, and what ships instead

`tools/lib/` reads as an unclassified leftover — no README, no version constant, no adopter, and
`check-kit-versions.sh` asserts nothing about it. `map_extractors.py:42` records that this is
deliberate: `tools/hooks`, `tools/lib` and `tools/workflows` carry no README and the kits inventory
is therefore not README-gated. Every surface signal that marks a kit is absent, and it is still one
of the most load-bearing directories here.

| Consumer | What it needs | What breaks without it |
|---|---|---|
| `resolve-python.test.sh:85` | `resolve-python.sh` as the CANON | 11 inline copies have nothing to be byte-compared against; the leg is vacuous |
| `run-gates.sh:9`, `run-gates.test.sh:7`, `check-wiring.sh:54`, `agent-cap.test.sh:13`, `merge-rows.test.sh:43` | source it at runtime | the runner and four gates cannot resolve an interpreter |
| `merge.rows.driver` git config | `pyrun.sh` | the driver never starts, so it never writes its output — git prints CONFLICT and leaves ours-only content with NO markers |

So it stays, gov-internal, and it is neither a kit nor a registry entry: `DEPL-aSealedCaravan-2`
carries it as a declared exemption with that reason. The boundary
`TOOL-aBatchedTribunal-6j` drew is preserved rather than crossed.

What an adopter actually needs is one file, not the directory. `merge-rows.py` names a launcher at
runtime, and a kit copy-installed as a standalone directory cannot reach `tools/lib/pyrun.sh` — the
gap the merge-driver dossier records as "a packaging question rather than a rewrite". S9 ships
`merge-rows.sh` INSIDE the kit, carrying the resolver inline byte-identically like every other
copy-installed kit file, rather than copying `tools/lib/` across. That keeps one canon, adds one
member to the existing inline-copy parity population, and leaves `tools/lib/pyrun.sh` free to keep
SOURCING the resolver, which is why `merge-rows.test.sh:257` asserts it carries no inline block —
that assertion is re-scoped to `tools/lib/pyrun.sh` by path rather than to any launcher by name.

### Migration

None for existing adopters, by non-goal. For this repo, S4's placeholder substitution changes
`HYGIENE.template.md`, which `kit-dogfood-parity.test.sh` byte-compares against the installed
`memory/HYGIENE.md` modulo the prefix. That gate currently implements `norm()` as an unanchored global
`sed "s|$PREFIX||g"` over the live copy. With S4 landed, the placeholder IS the parity mechanism and
the blind substitution is DELETED rather than inverted — which also removes a latent defect, because
the global form strips every occurrence of `tools/`, not only a leading kit path. `S13`'s
`REVIEW-PROTOCOL.template.md` change carries the identical treatment in
`check-protocol-parity.test.sh:36`.

Order matters. S4 must land in the same commit as the parity-gate change, or the gate reds between
them; the same holds for S13 and its parity gate.

### Rollout

Three commits, each independently green:

1. S11 plus S6 — the stale records and the dead Skill spelling. Pure corrections, no behaviour change.
2. S3, S4, S5, S7, S9, S12 — the adopters, the templates, the check-15 scope, the two disarmed guards
   and the copy-paste surface, with each parity-gate change bundled beside the template it grades.
3. S1, S2, S8, S10, S13 — the runbook rewrite, the cross-kit references, and the gate that holds them.

### Files touched (estimate)

Derived from the measured distribution above, not estimated.

| Area | Files | Note |
|---|---|---|
| Runbook | `WIRE-INTO-PROJECT.md` | ~36 root-path lines plus 14 claim fixes |
| Kit READMEs | 4 | 11 hits |
| Adopters | 3 | `adopt-memory-tree.sh` body plus two usage headers |
| Templates | 4 | `HYGIENE`, `SPEC-TEMPLATE`, drift-audit `SKILL`, `drift_signals` |
| Engines, usage + remedy strings | 5 | incl. `gen_build_index.py`'s stamped `GEN_HEADER` |
| Cross-kit | 3 | `REVIEW-PROTOCOL.template.md`, kickoff `SKILL.md`, playbook |
| Gates | 5 | new prefix gate + self-test, `agent-cap.test.sh`, `.githooks/pre-commit`, two parity tests |
| Records | 4 | `AGENTS.md`, `memory/backlog/TOOL.md`, `check-wiring.sh` header, map dossier |
| Manifest, map | 2 | `gate-legs.json` is watched; the new legs need a dossier claim |

The playbook is INSIDE S8's surface and therefore inside this table. Its cost is one line
(`workflows/tier2-review.js` at `:148` becomes `tools/workflows/tier2-review.js`), so it spends 6 of
the 80 free bytes under `tools/check-template-size.sh` (32688 of 32768, measured). That fits without
trimming. `parallel-coding-governance.customize.md` carries no runnable kit path under the narrowed
predicate, but its line 40 declares the OPPOSITE default from S1 in shipped prose, so it joins S10's
correction list.

### The fourteen runbook corrections

Grouped, since several share a cause. Section 0 still offers memory-tree as optional, which playbook
v2.5 made required, and four downstream conditionals inherit that error. Two cross-references name
steps that do not exist: line 79 points at section 5 for agent-instructions, and line 263 says "skip
if section 5 did it" of a copy section 5 never performs — an adopter who obeys hits the errno-2
failure the next paragraph warns about. Two placeholder-verify recipes contradict each other for the
same file, and neither greps the companion holding 13 of the 36 placeholders. The retrofit stamps
marker v2.2 on a copy pulled from a v2.5 source. The `.gitattributes` block pins 2 of the 5 registries
the scaffolder writes; the config-key list names 5 of 15 keys. Three shipped kits appear nowhere:
drift-audit and `check-kit-versions` are gate-legged, and `gate-lint` hands leg wiring to the
consuming project, so the runbook owes it an adopter step rather than a gov leg. The row-keyed merge
driver is likewise absent, and `cp -r tools/memory-tree` delivers half of it.

### Alternatives rejected

**Keep both spellings forever and gate nothing.** This is today's state. It is what produced the
mixed-prefix merge-driver command recorded at `tools/memory-tree/README.md:109`, where a driver that
never starts never writes its output, git prints CONFLICT, and the path is left holding ours-only
content with zero conflict markers. Silent data loss is the cost of the ambiguity, and it is measured
rather than theoretical.

**Gate the naive predicate and waive 95 hits.** Rejected on measurement: a 37-file waiver registry is
larger than the change it guards, and most of its entries would be fixtures that exist to prove the
dual-prefix support the non-goal keeps.

**Make the prefix a configuration key.** A declared prefix is a second place to be wrong, and the
walk-up already answers the question without one.

**Retrofit the existing adopters.** Out of scope by owner decision, and the dual-prefix probes make it
unnecessary — both spellings resolve.

## 5. Production-readiness checklist

- security — N/A: no new write path, no new input surface. The gate added by S8 reads tracked files.
- perf / scale — the S8 gate is a `git ls-files` sweep plus a regex over 74 files; budget it alongside
  `check-template-size.sh` at well under a second.
- a11y — N/A: no user interface.
- i18n — N/A: no user-facing strings.
- error / empty / loading states — the S7 population assertions ARE this line: a guard whose
  population is empty must say so and fail, never pass. Same class as the vacuous-selector gotcha.
- observability — every changed guard names the path it resolved in its output, so a skip is
  attributable rather than silent.
- risks — S4 and S13 must each land in one commit with their parity gate, or the bar reds between
  them. The S8 predicate is a new source-level ban and both prior bans were wrong on first run, so it
  was run over the real tree before this section was written and its numbers are measured.
- testing + left-shift gates — S8 ships with a red/green self-test; S5 needs a fixture proving check
  15 fires on a wrong-prefix citation, since this repo's present-tense corpus contains none.
- migration / rollback — no data migration. Rollback is a revert; no adopter state changes.
- user docs — `WIRE-INTO-PROJECT.md` is the deliverable, plus four kit READMEs.

## 6. Acceptance criteria

- **AC1** When `bash tools/check-install-prefix.sh` runs on the tree as landed, every hit of the
  narrowed predicate over its 74-file population is listed in the waiver registry, and the registry
  holds 4 entries. The predicate cannot report a `tools/`-prefixed path as a hit by construction, so
  the criterion is "every hit is waived", not "waived or prefixed".
- **AC2** When a root-install spelling is reintroduced into any file in the population, the gate exits
  non-zero naming that file and line; when the waiver registry is emptied, it exits non-zero naming
  the four entries. Both arms are in the self-test, alongside the empty-population arm.
- **AC3** When `adopt-memory-tree.sh --scaffold` runs from `tools/memory-tree/` in a fresh repo, all
  seven kit-path occurrences in the scaffolded `memory/HYGIENE.md` resolve in that repo, and the
  printed next-step commands are runnable as printed.
- **AC4** When a fixture repo is scaffolded at a `tools/` prefix and a memory record cites
  `memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/corpus_ids.py --check` fails naming
  that citation. The fixture is built by the test, because this repo's corpus contains no such
  citation to observe.
- **AC5** When `bash tools/hooks/agent-cap.test.sh` runs in a repo whose kit is installed at a
  non-`tools/` prefix with no wired copy, it FAILS naming the kit it found; a run with no kit at all
  reports a skip that names the paths it looked for.
- **AC6** When `.githooks/pre-commit` runs in a repo whose kits are installed but not at the literal
  guarded paths, it FAILS naming each kit it located, rather than exiting 0 with three silent skips.
- **AC7** When `bash tools/drift-audit/adopt-drift-audit.sh --check` runs after S6, the rendered Skill
  names `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js`, and both
  paths exist.
- **AC8** When `kit-dogfood-parity.test.sh` and `check-protocol-parity.test.sh` run after S4 and S13,
  both pass and neither contains a global prefix substitution in `norm()`.
- **AC9** Each S11 record has its own assertion: `grep -c 'non-canonical `tools/` prefix' AGENTS.md`
  returns 0 (1 at base); `grep -c 'kit 1.8' AGENTS.md` returns 0; `AGENTS.md`'s dossier sentence names
  two dossiers; `memory/backlog/TOOL.md`'s `TOOL-aRootedPrefix-1` row reads CLOSED; and
  `check-wiring.sh:3` cites a path that `git ls-files` resolves.
- **AC10** When every kit entrypoint named in S12 is run with no arguments or `--help`, no printed
  command spells a root-install path, and a fresh `gen_build_index.py --write` stamps a `GEN_HEADER`
  naming `tools/memory-tree/gen_build_index.py`.
- **AC11** When `manifest-check.sh` is installed at `tools/manifest-check.sh` per S2 and the kickoff
  engine's four-path manifest search runs, the checker resolves and exits 0; the engine's fallback
  chain still accepts a `scripts/` install for an existing adopter.
- **AC12** When a memory-tree kit is copy-installed alone into a fresh repo and
  `merge.rows.driver` is wired to its own `merge-rows.sh`, a per-family append collision on
  `memory/DECISIONS.md` merges cleanly with no row missing or duplicated. Today the shim it names
  lives outside the kit and the merge leaves ours-only content with no conflict markers.
- **AC13** When `bash tools/lib/resolve-python.test.sh` runs after S9, `merge-rows.sh` is in the
  inline-copy parity population and byte-identical to the canon, and `tools/lib/pyrun.sh` is still
  excluded from it.
- **AC14** When the runbook's own verification steps are executed against a fresh fixture repo, the
  memory-tree, codebase-map, memory-recall and drift-audit kits all sit under `tools/` and every gate
  the runbook names is green.

## 7. Gates

`bash tools/run-gates.sh` (40 legs today, **42** after S8 — the gate and its self-test are both legs)
must be green at the push boundary. The legs this unit moves: `memory/` hygiene (check 15's scope
changes); `kit-dogfood-parity.test.sh` and `check-protocol-parity.test.sh` (the `norm()` deletion);
`agent-cap.test.sh`; `.githooks/pre-commit.test.sh`; and `check-verdict-epoch.sh`, because a
non-comment change to `check-memory-hygiene.sh` or its delegates must move `KIT_MEMORY_TREE_VERSION`
in the same diff.

Adding legs trips four gates at once, and the spec states it here so the builder does not discover it
serially: the codebase-map `gate-legs` coverage assertion needs both legs claimed in a dossier; the
codebase-map freshness byte-compare needs a regenerated `MAP.md` and `inventories.json`; the
kickoff-manifest ratchet needs a `last-audit` re-stamp because `tools/gate-legs.json` is a watched
pathspec; and drift-audit's handkept signal needs BOTH new script paths cited in the charter's gate
suite section. That last has zero slack — the pin is 7 of 40 at tolerance 0, so two uncited legs push
it to 9 and red immediately.

Before review: `python tools/memory-tree/gotchas.py --for-diff 16aeb5ef..HEAD`.

## 8. Open questions

- **F1 — does `manifest-check.sh` move to `tools/`?** S2 says yes, for one home rather than three.
  Against: the manifest template's `check-script:` field already parameterizes it, and existing
  adopters carry `scripts/`. RECOMMENDATION: move it, keep the kickoff engine's fallback chain
  accepting both, and cover the move with AC11 — at rev-1 this fork had no observer at all.
- **F2 — should the S8 gate also cover a target repo?** RECOMMENDATION: shipping surface only. A
  target-side check belongs to `govkit check` in unit 2, which already reads a target's state.
- **F3 — what happens to `tools/lib/`?** RESOLVED (owner, 2026-08-10): it is not a kit. The fork was
  mis-framed at rev-2 as "does it become a shipped kit", a binary whose other branch reads as
  "delete it" — and it is load-bearing three ways (section 4). It stays gov-internal, becomes a
  declared registry exemption in `DEPL-aSealedCaravan-2`, and ships nothing. The packaging
  sub-question it was hiding is now S9, and the choice there is mine to confirm: ship
  `merge-rows.sh` inside the memory-tree kit with the resolver inlined, rather than copying
  `tools/lib/` across. Confirm that shape before commit 2 — it adds one member to the inline-copy
  parity population and re-scopes one assertion in `merge-rows.test.sh`.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, grounded on a five-probe inventory run over the adoption
  surface. Four silent-green failures proved cold in throwaway repos; five stale records identified.
- rev-2 · 2026-08-10 · folded review 1 (20 findings on this spec, 3 blockers). Ran the S8 predicate
  over its declared surface for the first time: 95 hits across 37 files naive, 50 across 22 narrowed.
  Added the narrowing rule, the measured disposition table and a 4-entry waiver registry; added S12
  and S13 for the 20 hits that had no owning scope item; put the playbook in Files touched with its
  measured byte cost; corrected "41 legs" to 42; re-anchored AC9 on text that exists at base and split
  it into five named assertions; corrected the check-15 claim from seven citations to the three in a
  shape it can see; strengthened AC5 and AC6 from negatives a no-op satisfies to failures that name
  what they found; added AC11 for S2, which had no observer; and re-cited the `KIT_DIR` non-goal,
  which `TOOL-aRootedPrefix-1b` does not support.
- rev-3 · 2026-08-10 · resolved F3 on the owner's steer that `tools/lib/` is not a kit. Audited its
  consumers repo-wide first: it is load-bearing three ways, so "not a kit" does not mean "leftover".
  Rewrote S9 — the memory-tree kit ships its own `merge-rows.sh` with the resolver inlined instead of
  the runbook copying `tools/lib/` across, which keeps one canon and preserves the
  `TOOL-aBatchedTribunal-6j` boundary. Added section 4's consumer table, AC12 for the behaviour S9
  actually buys and AC13 for the parity-population change.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py "deploy a kit into a target repo: copy files, render
config, wire gates, write an install receipt"` over 277 symbols, 72 inventory keys, 3 affordance seams
and 2 dossiers. The shortlist surfaced `kit_rel` (`tools/codebase-map/map_lib.py`, fan-in 3, SEAM) and
`relative_kit` in the same module, which are the existing prefix-derivation seam. S3 and S12 wire
`adopt-memory-tree.sh` and the usage headers through the same computation those express — a `relpath`
of the kit dir against the resolved root — rather than inventing a second spelling; the three adopters
that already do it (`adopt-codebase-map.sh`, `adopt-memory-recall.sh`, `adopt-drift-audit.sh`) are the
pattern.

For S8 the lookup returned no seam: the ranked hits were `write`, `write_text` and `render`, none of
which is a source-level ban. The nearest existing pattern is the pair of source-level bans in
`tools/lib/resolve-python.test.sh`, and S8 follows their structure — a `git ls-files` population, a
regex, a tracked waiver registry — without sharing code, because bash gates in this repo are
deliberately standalone. Recorded as "no existing seam fits; nearest pattern reused by shape".

Note that bash is a declared recall-dark layer in `.codebase-map.conf`, so the lookup's silence on a
bash gate is a known partial-recall notice rather than evidence of absence.
