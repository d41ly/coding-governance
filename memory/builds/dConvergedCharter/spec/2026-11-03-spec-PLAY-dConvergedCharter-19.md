# PLAY-dConvergedCharter-19 — the guides' positional citations migrated to tags, legacy anchors kept as aliases, and the per-directory line-ending pins retired into class pins

**Status:** DEFERRED · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 12 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0493@67838f7a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-13 |
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-19-deviation-191.md](../build/2026-11-03-build-PLAY-dConvergedCharter-19-deviation-191.md) | deviation | — |
| [2026-11-03-build-PLAY-dConvergedCharter-19-deviation-192.md](../build/2026-11-03-build-PLAY-dConvergedCharter-19-deviation-192.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

P34 names every section by a tag and P37 pins line endings by class (v2:1044-1061; the execution plan has no P34
or P37 hit, scout A). At base the guides name their own sections by position (`M5`, `§13`) and cite each other
that way, and `.gitattributes` holds 78 `eol=lf` pin lines, most of them per-directory instances of a class
(gap-tool-13). This unit gives each guide section that carries a positional label an authored tag, rewrites the
guides' positional citations as tag citations, keeps every legacy anchor as an `[[alias]]` row, and retires the
per-directory pins, in gov's `.gitattributes` and in the kits' `[[lf_pin]]` rows, into class pins, shipping the
adopter's half as an upgrade step.

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at base `0d1c1dda`: PLAY-dOrderedCharter-19 S3 and S11 (the
`doc` section rows, `tools/playbook/aliases.toml`, `tools/playbook/positional-refs.txt`), PLAY-dOrderedCharter-26
S2-S5 (the `positional` arm under `tags.positional` and its remedy verb), PLAY-dOrderedCharter-29 S8 (a vanished
section with no `[[alias]]` row is red), TOOL-dTotalRecall-9 (`extract_section`'s authored-heading rule),
TOOL-dTotalRecall-10 S1 (`derive_anchor`), TOOL-dWitnessedBar-24 S2 (`tools/gate-lint/eol_class.py` and the class
lines `*.py`, `*.js`, `*.json`, `*.toml` beside `*.sh`), ask A1 of §8 F5, and this build's PLAY-dConvergedCharter-12,
which retires the four `UNATTENDED-*` guides and the unattended kit's pin rows first. `PLAYBOOK-TEMPLATE.md`
stays until PLAY-dConvergedCharter-7 removes it after this unit, so it is in this unit's population; it carries
no positional label or citation at base (`grep -cE '§[0-9]|\bM[0-9]+\b'` prints 0), so S1 and S3 change none of
its bytes, and `SESSION-KICKOFF.md` is in the population too (§4 Files touched).

- **S1** — The authored section tags. Each `##` heading of a guide under `memory/guides/` that carries a
  positional label (`M<n> —`, `§<n>`) takes the form `## [section.<seg>] <Title>`, the label cut from the title
  and `<seg>` the `derive_anchor` fold of the title, so the BUILD-METHOD heading `## M5 — Recall and reuse` becomes
  `## [section.recall-and-reuse] Recall and reuse` and its address `doc.build-method#recall-and-reuse` (I12). The
  edit is each guide's source: `tools/memory-tree/BUILD-METHOD.template.md` rendered by `adopt-memory-tree.sh
  --render`, and a hand-written guide in place. Observed by AC1.
- **S2** — The legacy anchors. For each heading S1 changes, `tools/playbook/aliases.toml` holds
  `[[alias]] ref = "<DOC> <label>"` (`ref = "BUILD-METHOD M5"`) with `target` the new address, re-pointing the
  row PLAY-dOrderedCharter-19 S11 seeded at the old fold, and one `[[alias]]` row whose `ref` is the vanished
  address (`doc.build-method#m5-recall-and-reuse`) with the same `target`, so PLAY-dOrderedCharter-29 S8's
  check over vanished sections passes it. Observed by AC2.
- **S3** — The citations. Every positional citation inside a guide whose target is a `##` section with a
  `doc` row is rewritten as that section's tag citation, `doc.<name>#<seg>`, and its row leaves
  `positional-refs.txt` through PLAY-dOrderedCharter-26 S5's remedy verb, never by hand. A citation whose target
  has no section row (a hygiene check number, a skeleton section inside a fence) keeps its row for
  PLAY-dConvergedCharter-2. Observed by AC3.
- **S4** — The budget the citations cost. `memory/guides/BUILD-METHOD.md` measures 30659 bytes against its
  30720-byte row (`tools/template-size-limits.txt:129`) at base, PINNED, and S1 and S3 grow it. Its row and M1's
  `**Budget:` line move together to the measured render, no headroom, the movement argued above the row as the
  file's grammar asks (`:16-23`), under §8 F4. Observed by AC4.
- **S5** — The class pins in gov's file. `.gitattributes` keeps `*.sh` (`:5`) and TOOL-dWitnessedBar-24's four
  class lines, gains `*.md`, `*.txt`, `*.tsv`, `*.yml`, `*.conf` and `*.example text eol=lf`, each a
  `[[gov_only_pin]]` row of `tools/govkit/registry.toml` beside the three at `:492-502`, and keeps the four
  extensionless hooks `.githooks/commit-msg`, `pre-commit`, `pre-push` and `pre-rebase` as path lines. Every
  other `eol=lf` line, each covered by a class line, leaves the file; the `merge=` lines stay. Observed by AC5.
  **Readers:** by name: the pin lines are spelled by `.gitattributes` alone, and its comment at `:128` names
  `check-wiring.sh`'s eol arm · by value: `check_eol` in `tools/check-wiring.sh`, which reads
  each path's attribute through `git check-attr`, so a class line resolves its population unchanged, and
  `eol_population` in `tools/govkit/govkit.py`, which asks git the same way.
- **S6** — The class pins in the kits' rows. A kit's `[[lf_pin]]` row whose pattern a class covers, one file
  or one directory of `*.md`, `*.txt`, `*.toml`, `*.sh`, `*.js` or `*.json`, leaves its `kit.toml`, and the kit
  declares the class row `pattern = "*.<ext>"` instead, which `lf_pins` dedupes across kits
  (`tools/govkit/govkit.py:5671-5692`). A pattern's placeholders are resolved before its extension is taken:
  `{kit}`, `{prefix}` and `{memory_root}` to gov's own values, as `lf_pins` resolves them. The rows whose
  pattern no kit class covers stay instances: the root confs `.codebase-map.conf`
  (`tools/codebase-map/kit.toml:141`) and `.memory-tree.conf` (`tools/memory-tree/kit.toml:366`),
  `{kit}/.memory-tree.conf.example` (`:369`), the two hooks of `push-main.kit.toml`, the `{user_skills}` row
  outside the tree, and the `{playbook_path}` row (`tools/govkit/entries/playbook.kit.toml:65`), whose value
  is an adopter's answer with no fixed extension, so no class can cover it. `.process-monitor.conf`'s row
  leaves with the file in PLAY-dConvergedCharter-11 S2, before this unit. Observed by AC6 and AC7.
  **Readers:** by name: `lf_pins` and the plan's attribute rows in `tools/govkit/govkit.py` (`:3833`, `:5685`),
  `tools/govkit/selftest.py` and `WIRE-INTO-PROJECT.md`'s pin section (`:1418`) · by value: `lf_pin_block`'s
  block bytes, which `update` recomputes (`govkit.py:10231-10276`), and the selftest assertion that the block
  holds `.claude/skills/memory-recall/SKILL.md text eol=lf` (`tools/govkit/selftest.py:7558`), re-pointed to
  `*.md text eol=lf`.
- **S7** — The covered-pin arm. `check_covered_pins(root)` in `tools/gate-lint/eol_class.py`, run by the class
  leg, grades two populations against two class sets and never crosses them. Each `eol=lf` line of gov's
  `.gitattributes` that is not a class line reds while one of gov's own class lines covers its extension,
  those of S5 among them. Each kit `[[lf_pin]]` pattern, its `{kit}`, `{prefix}` and `{memory_root}`
  placeholders resolved first, reds while one of the class rows the kits declare covers its extension,
  `*.md`, `*.txt`, `*.toml`, `*.sh`, `*.js` and `*.json` (S6), never gov's gov-only class lines such as
  `*.conf` and `*.example`, which reach no adopter's block. A pattern holding a placeholder that resolves
  to an adopter's answer or outside the tree, `{playbook_path}` and `{user_skills}`, is an instance and is
  not graded. A red reads `eol-class: <pattern> pinned per path, covered by *.<ext>`. Observed by AC7.
- **S8** — The adopter's step. An `[[upgrade]]` row `govkit/lf-pins-to-class` in `tools/govkit/steps.toml`,
  `surfaces` one `attributes:<pattern>` per withdrawn pattern, `resume = "atomic"`, its program
  `tools/govkit/steps/lf_class_pins.py` with `up`, `down` and `witness`: `up` rewrites the target's block through
  govkit's own `lf_pins` and `lf_pin_block` and renormalizes the paths `eol_population` reports changed, `down`
  restores the before-image through TOOL-dSafePassage-1's helpers, and `witness` reads the block current. No
  second block writer. Observed by AC8.
- **S9** — The docs. `WIRE-INTO-PROJECT.md`'s pin section says a kit declares a class row and an instance only
  where no class covers it, and `help/upgrade-steps.md` lists `govkit/lf-pins-to-class`. Observed by AC9.

## 3. Non-goals (OUT)

- Positional references outside the guides, `memory/HYGIENE.md`'s and `memory/TEMPLATE-SPEC.md`'s numbered
  checks and sections included, and the `REV_SCOPE_CUTOFF` rule: PLAY-dConvergedCharter-2.
- The guides of the unattended kit: retired with it by PLAY-dConvergedCharter-12 before this unit.
- The class leg, its arms over the index and the four class lines: TOOL-dWitnessedBar-24 S2.
- The `doc` extractor's change to honour an authored heading: asked of dOrderedCharter (§8 F5, ask A1).
- Rewriting a guide's prose beyond its labels and citations: PLAY-dConvergedCharter-1 and -13.
- Renaming a Skill or re-pointing its kit rows: PLAY-dConvergedCharter-9.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-12` — `tools/unattended/`, whose guides and pin rows leave with the kit before this unit, so S1 to S6 never migrate them
- **hands-off** `PLAY-dConvergedCharter-2` — `aliases.toml`, the guide aliases on which unit 2 drains the rest of `positional-refs.txt`
- **hands-off** `PLAY-dConvergedCharter-13` — `extract_section`, the authored-heading rule a guide section now carries, by which unit 13 addresses the prose it moves
- **hands-off** `PLAY-dConvergedCharter-7` — `extract_section`, the authored-heading rule by which unit 7 maps a guide section to a unit's rationale
- **hands-off** `PLAY-dConvergedCharter-9` — `.gitattributes`, which holds no per-Skill pin after S5, and the kits' rows, which hold none after S6, so a Skill rename re-points no pin
- **consumes-from** external — PLAY-dOrderedCharter-19, -26 and -29, TOOL-dTotalRecall-9 and -10 and TOOL-dWitnessedBar-24, each specced and DEFERRED at base and landed in an ancestor before the build run

## 4. Design

### Evidence

- `.gitattributes` holds 78 `eol=lf` lines at base, one of them a comment (`:72`): 77 pins, PINNED at
  `0d1c1dda` by `git show 0d1c1dda:.gitattributes | grep -c 'eol=lf'`. By the last
  segment's extension they are 22 `md`, 10 `txt`, 10 `toml`, 5 `py`, 5 `conf`, 4 `sh`, 4 `json`, 3 `tsv`, 3 `js`,
  2 `example`, 1 `yml`, 2 whole directories (`memory/map/generated/*`, `tools/runlog/fixtures/*`) and 5 with no
  extension, the four hooks and `*.fragment.json`'s class (PINNED at base).
- `git ls-files --eol` at base: 10992 index entries `i/lf`, 3 `i/-text`, 10 `i/none`, no `i/crlf`. A class line
  on any text extension changes no committed blob in gov's tree.
- 35 `[[lf_pin]]` rows sit in 16 descriptors (`git grep -n '^\[\[lf_pin\]\]'`), rendered into an adopter's block
  by `lf_pins` and `lf_pin_block` (`tools/govkit/govkit.py:5630-5692`).
- `check_eol` (`tools/check-wiring.sh:1235`) takes its population from `git check-attr eol`, never from the file's
  text, so a class line keeps every rendered Skill in it.
- The `doc` rows fold a heading's text, so `## M5 — Recall and reuse` is `m5-recall-and-reuse`
  (PLAY-dOrderedCharter-19 S3): the positional label survives inside the address unless the heading drops it.
- The guides' positional lines at base (lines carrying `§<n>`, `M<n>`): BUILD-METHOD 24 and 48, SESSION-KICKOFF 3
  and 2, MERGE-BAR 1 and 0, REVIEW-PROTOCOL and ANNOTATION-STYLE none; the unattended guides' lines leave with
  their kit (PINNED at base, re-derived by `positional-refs.txt`'s rows for those paths).

### The pins after

```
* text=auto
*.sh text eol=lf          *.py text eol=lf          *.js text eol=lf          *.json text eol=lf
*.toml text eol=lf        *.md text eol=lf          *.txt text eol=lf         *.tsv text eol=lf
*.yml text eol=lf         *.conf text eol=lf        *.example text eol=lf
.githooks/commit-msg text eol=lf    .githooks/pre-commit text eol=lf
.githooks/pre-push text eol=lf      .githooks/pre-rebase text eol=lf
```

The `merge=rows` and `merge=ours` lines and their comments stay as they are.

### Rollout

Gov first, in the unit's pass: S1 to S7 land together, the `kit/dogfood doc parity` render with them. An adopter
receives S6 through S8's step at its next `govkit update`, whose `attributes` arm then reads the block `current`.

### Inventory

Minted, each asked of `lexicon.py --suggest <name> --as py.function` at base and answered OK:
`check_covered_pins`. The step id `govkit/lf-pins-to-class`, its program `lf_class_pins.py`, the surface class
word `attributes`, the line `eol-class: … pinned per path`, and one authored tag `section.<seg>` per relabelled
heading, BUILD-METHOD's twelve among them.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md`, rendered to `memory/guides/BUILD-METHOD.md`: S1, S3, S4
- `memory/guides/MERGE-BAR.md`, `memory/guides/SESSION-KICKOFF.md` where it stands at base: S1, S3
- `tools/playbook/aliases.toml`, `tools/playbook/positional-refs.txt`: S2, S3
- `tools/template-size-limits.txt`: S4
- `.gitattributes`, `tools/govkit/registry.toml`: S5
- `tools/memory-tree/kit.toml`, `tools/hooks/kit.toml`, `tools/roles/kit.toml`, `tools/run-gates/kit.toml`,
  `tools/process-monitor/kit.toml`, `tools/workflows/kit.toml`, `tools/branch-reconcile/kit.toml`,
  `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`, `tools/lexicon/kit.toml`,
  `tools/memory-recall/kit.toml`, `tools/runlog/kit.toml`, `tools/govkit/entries/playbook.kit.toml`: S6
- `tools/govkit/selftest.py`: S6's re-pointed assertion, S8's arm
- `tools/gate-lint/eol_class.py`: S7
- `tools/govkit/steps.toml`, `tools/govkit/steps/lf_class_pins.py` (new): S8
- `WIRE-INTO-PROJECT.md`, `help/upgrade-steps.md`: S9

### Alternatives rejected

- **Keeping the label in the heading** (`## M5 — Recall and reuse`). The address keeps `m5`, so a renumbering
  moves every citation: the defect CV2 names.
- **Class lines for gov's file only, the kits' rows untouched.** The kits' per-directory rows stay
  per-directory in every adopter, which fails the clause.
- **`* text=auto eol=lf`, one universal line.** It reaches binary-adjacent and Windows-native files an adopter
  may hold (`.bat`, `.cmd`), and `check_eol`'s own comment records the `--fix` hazard of that selector
  (`tools/check-wiring.sh:1238-1241`).
- **`govkit update`'s `pins-moved` rewrite alone, no step.** It rewrites the block, but the adopter-visible change
  then has no declared step, no `down` and no witness (P38).

## 5. Production-readiness checklist

- security — no new surface in gov; in an adopter, S6 widens the block to whole classes (§8 F3, deviation 191).
- perf / scale — `check_covered_pins` reads one file and 16 descriptors.
- error / empty / loading states — a descriptor with no `[[lf_pin]]` row contributes nothing; a target whose
  pin set empties takes `update`'s existing `pins-withdrawn` path (`govkit.py:10251-10263`).
- observability — each covered pin is a named line; the step prints the patterns it withdrew.
- risks — an adopter file of a pinned class committed with CRLF is renormalized by the step; the step's `down`
  restores it.
- testing — AC1 to AC8, and the arms of §7.
- migration — S8.
- user docs — S9.

## 6. Acceptance criteria

- **AC1** — When `grep -nE "^## " BUILD-METHOD.md` runs in `memory/guides/`, every heading reads
  `## [section.<seg>] <Title>` and none carries `M<n> —`.
  Red when: a heading keeps its positional label.
- **AC2** — When `python gov_tag.py check` runs at the tip, PLAY-dOrderedCharter-29 S8's retired check passes
  every address S1 moved, and `python gov_tag.py where "BUILD-METHOD M5"` prints the `recall-and-reuse` section's
  line.
  Red when: an old address vanishes with no `[[alias]]` row, or a label's alias still targets the old fold.
- **AC3** — When a fixture plants `see M5` in a copy of `BUILD-METHOD.template.md`, `python gov_tag.py check`'s
  `positional` arm exits 1 naming the path and `M5`; without the plant it exits 0 and `positional-refs.txt` holds
  no row keyed to a guide whose target has a section row.
  Red when: the planted positional citation passes, the clause's first seen-red case.
- **AC4** — When `python budgets.py resolve` reads the BUILD-METHOD row, its value equals the render's
  CR-stripped byte count, and M1's `**Budget:` line spells the same figure.
  Red when: the row and the prose disagree, or the row carries headroom.
- **AC5** — When `git check-attr eol` runs over every tracked path under `tools/`, `.claude/`, `skills/` and
  `memory/` of a text class, each reads `lf`; and `grep -c "^[^#].*eol=lf" .gitattributes` prints 15.
  Red when: a path of a class reads unspecified, or a covered per-directory line survives.
  figure: 15 is PINNED from §4 "The pins after".
- **AC6** — When `python govkit.py plan` runs over a fixture target selecting every kit, its attribute rows name
  only class patterns and the uncovered instances S6 lists.
  Red when: a per-directory or single-file pattern a kit class covers reaches the block, or a kept instance of
  S6 is dropped.
- **AC7** — When a fixture adds `tools/x/*.py text eol=lf` to a copy of `.gitattributes`, `python
  eol_class.py` exits 1 printing `pinned per path, covered by *.py`; the same with a planted
  `[[lf_pin]] pattern = "{kit}/*.sh"` row in a copy of a descriptor. Over gov's own descriptors after S6 it
  exits 0, and a planted kit row `pattern = ".codebase-map.conf"` and one `pattern = "{playbook_path}"` each
  pass, while gov's `.gitattributes` with a planted `.codebase-map.conf text eol=lf` line reds, covered by
  `*.conf`.
  Red when: the planted per-directory pin passes, the clause's second seen-red case, or a kit instance S6
  keeps reds against a gov-only class line.
- **AC8** — When `python lf_class_pins.py up <target>` runs on a fixture adopter holding the pre-step block, the
  block equals `lf_pin_block` of the class rows, `witness` exits 0, and `down` restores the block and every
  renormalized file byte-identical.
  Red when: `up` writes a block `update` would call `pins-moved`, or `down` leaves a byte moved.
  fixture: a scratch adopter under `%TEMP%/<short>` with one CRLF `.md` of its own.
- **AC9** — When `grep -n "lf-pins-to-class" upgrade-steps.md` runs in `help/` and `grep -n "class row"
  WIRE-INTO-PROJECT.md` runs at the root, each names the step and the class rule.
  Red when: either page still describes per-path pins as the rule.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms` · `policy fixtures` · `kit/dogfood doc parity` · `playbook render selftest` · `shell-hygiene selftest` · `build-method size` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `branch-reconcile selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `lexicon selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line`

New arm: tools/gate-lint/eol_class.py · covers AC7 · `check_covered_pins` over a planted per-directory line, a planted per-directory `[[lf_pin]]` row, a root-conf row and a placeholder row, staged red with the arm reading only class lines or grading kit rows against gov's class lines · none

New arm: tools/govkit/selftest.py · covers AC6 AC8 · the step `govkit/lf-pins-to-class` up, witness and down on a fixture adopter, staged red by an `up` that writes the pre-step block · none

## 8. Open questions

- **F1 — How does a positional label leave a guide's address?** (a) The authored form `## [section.<seg>]
  <Title>`, the label cut from the title (I12); (b) the label cut and the fold of the bare title kept as the
  address; (c) the label kept. (c) fails the clause's "survive reordering" reading of CV2; (b) re-addresses the
  section on every title edit; (a) pins the address and needs the extractor change ask A1 states. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a), ask A1 a build-run precondition. widens: none · relaxes: none
- **F2 — Which classes pin gov's own file?** Research-compatibility's P-eol names the execution class (`*.py`,
  `*.js`, `*.json`, `*.toml`, extensionless hooks); 43 of gov's 77 pins are `md`, `txt`, `tsv`, `yml`, `conf` or
  `example`. (a) Those six extensions also become gov-only class lines; (b) they stay per-directory. (b)
  fails the clause's "per-directory pins retired"; (a) changes no blob (§4 "Evidence") and reaches no adopter, the
  `[[gov_only_pin]]` rows being kept out of every block (`govkit.py:5677-5680`). Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — Which classes reach an adopter's block?** (a) Every class a kit's per-directory row names, so the
  kits' per-directory rows retire, and the single-file rows a class then covers with them; (b) the execution
  class only, `md` and `txt` rows staying per-directory; (c) the kits' rows untouched. (b) and (c) fail the
  clause (veto 1). (a) widens the block to an adopter's own files of each class, whose CRLF ones the step
  renormalizes (veto 3). Rung 5, the standing ruling ER:240. RESOLVED (agent, 2026-11-03, delegated): (a), recorded as deviation 191. widens: an adopter's .gitattributes block pins every tracked *.md, *.txt, *.toml, *.sh, *.js and *.json file · relaxes: none
- **F4 — The BUILD-METHOD budget.** S1 and S3 take the render past its 30720-byte row, which reserves its next
  movement to the owner ("Spent, it is the owner's again", `tools/template-size-limits.txt:126`). (a) Raise the
  row and M1's line to the measured render; (b) pay for the citations by cutting method prose, which rewrites a
  governance carrier beyond the clause; (c) leave BUILD-METHOD's citations positional, which fails the clause.
  (c) fails veto 1; (a) and (b) are veto-2 changes outside the grant, and (a) keeps every criterion. Rung 5, the standing ruling ER:388. RESOLVED (agent, 2026-11-03, delegated): (a), recorded as deviation 192. widens: tools/template-size-limits.txt memory/guides/BUILD-METHOD.md row and M1's Budget line · relaxes: none
- **F5 — The ask this unit needs filed.** RESOLVED (agent, 2026-11-03, delegated): file A1. widens: none · relaxes: none
  Ask A1 for dOrderedCharter, target build dOrderedCharter: "PLAY-dOrderedCharter-19 S3's `doc` extractor
  honours an authored `## [section.<seg>] <Title>` heading by TOOL-dTotalRecall-9 `extract_section`'s rule, the
  authored `<seg>` its address, never a third fold"; accept: a fixture guide heading `## [section.forks] Forks`
  resolves as `doc.<name>#forks`, and an unauthored heading keeps S3's fold.

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the spec brief's unit row, scout A's row 19 and disagreements 1, 2
  and 5, and the census of §4.
- rev-2 · 2026-11-04 · §2 S6 S7 §4 AC6 AC7 §7 §10 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings 13, 26 and 51 (S7 grades gov's lines
  against gov's class lines and kit rows against the kit class rows only, placeholders resolved first,
  `{playbook_path}` kept as an instance, `.process-monitor.conf` dropped from S6, AC7's root-conf and
  placeholder plants), 12 (`PLAYBOOK-TEMPLATE.md` stays in this unit's population, unit 7 removing it
  after) and 29 (78 lines and 77 pins, scout A's figure no longer corrected).

## 10. Reuse audit

The seams extended: PLAY-dOrderedCharter-19 S11's `aliases.toml` and `positional-refs.txt` (drained, never a
second inventory), PLAY-dOrderedCharter-26 S5's remedy verb, govkit's `lf_pins` and `lf_pin_block`
(`tools/govkit/govkit.py:5630-5692`), which the step composes rather than copies, the `[[gov_only_pin]]` rows
(`tools/govkit/registry.toml:492-502`), and TOOL-dWitnessedBar-24 S2's `eol_class.py`, which gains the
covered-pin arm. `python tools/codebase-map/reuse_lookup.py "pin line endings by file class instead of per
directory"` ranked name stems only (`check_line` in `tools/runlog/runlog_lib.py`, `unfenced_lines` in
`tools/memory-tree/tree_lib.py`), none a pin reader, so no existing callable fits beyond the govkit functions
read by hand. Where a record and source disagreed: scout A's 78 `eol=lf` lines agree with source, one of them a
comment; scout A's row omits that BUILD-METHOD sits 61 bytes under its owner-reserved row, which §8 F4 settles;
and the `[[lf_pin]]` rows number 35 in 16 descriptors, which scout A's row leaves uncounted.

Recall terms used: `python tools/memory-recall/query.py "how are the per-directory line ending pins retired into class pins and the guides positional citations migrated to tags" --terms "eol=lf lf_pin gitattributes class pin positional citation alias doc section tag BUILD-METHOD M-step"`
— its hits were the brief and scout A's rows 2 and 19, which agree with §4.
