# TOOL-aRepatriatedFork-23 — the install-prefix ban counts every kit path it cannot see today

**Status:** CLOSED · rev-3 · 2026-09-29 · node a · Tier-2 · base 2143b6d6 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-23-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-23-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md) | journal | TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46 |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-23-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-23-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |

<!-- /gen:spec-records -->

## 1. Goal

The carried ban in `tools/check-install-prefix.sh` counts 904 kit-path literals over 139 files at
predicate epoch 4. The 2026-09-25 census found 930 more in shipped files and 562 in tracked files
no descriptor resolves, and no arm counts any of them. A drain graded by that ledger would reach
zero with most of the population still in place. This unit widens the predicate to epoch 5, so
that every class the owner's 2026-09-25 ruling puts in scope is counted, and re-records the ledger
once. Units 24 to 29 then lower it, and `TOOL-aRepatriatedFork-30` deletes it.

## 2. Scope (IN)

- **S1** — Epoch 5's predicate counts five spellings that epoch 4 does not: a `/`-led path
  (`$ROOT/tools/…`, `<project>/tools/…`); a directory-only reference (`tools/<kit>` and
  `tools/<kit>/` with no file); a quoted `"tools"` segment joined by `/`, `,` or a `join(` call; a
  loose name under `tools/` whether or not that file exists in gov; and the root spelling
  `<kit>/<file>` that arm 1 bans. A `<gov>/tools/…` spelling is counted or not as §8 F2 resolves.
  A path led by a `<prefix>/` prose token or a `{prefix}`, `{kit}` or `{{TOOL_ROOT}}` render token
  is never counted, because it is the drained form. Observed by AC1, AC2.
- **S1a** (rev-3) — F4 and F1 carried into the predicate. The kit-segment spelling
  `<kit>/<file>.<ext>` counts at the root, under ANY literal prefix (`scripts/`, `vendor/gov/`), and
  under a derived base (`$HERE/../`, `$KIT_REL/`, `${VAR}/`), because a kit's name typed as a literal
  is the class whatever precedes it. A quoted kit segment used as a path segment counts the same way:
  joined by `/` (`HERE.parent / "<kit>"`, arm 3's P3 shape) or by `,` after a quoted literal prefix
  segment (`join(x, "scripts", "<kit>")`). A `<tool-root>/` prose token is drained like `<prefix>/`.
  Outside every spelling, and recorded as near-misses rather than counted: a bare `tools/` with no
  segment after it, a directory-only kit reference under any prefix but `tools/`, and a kit segment
  with no file after it. Observed by AC1, AC2.
- **S1b** (rev-3) — the counter is a python program inside the gate, run through the resolver the
  gate already sources. A `grep -oE` cannot read the operand a join starts from, and S4 needs it. A
  producer that dies refuses rather than yielding zero rows (the D3 class), and `carried_live`
  counts S2's population, the one the counter reads. Observed by AC8.
- **S2** — The ledger's population is every tracked file under `tools/`, `skills/` and `.githooks/`,
  every `*.template.*` file and `WIRE-INTO-PROJECT.md`, shipped or not. Tests, seeds and
  `.conf.example` files are in it. The ledger file itself and the waiver registry are not, because
  both are lists of paths and would count their own rows. Observed by AC3.
- **S3** — A `gov:root-fixture` marker, a `gov:prefix-literal` marker and a waiver row keep their
  current effect in arms 1 and 3, and have none in the ledger. The ledger is then the one account of
  what is left to drain. Observed by AC4.
- **S4** — The four true homonyms in the census's arm-3 table are not counted: a mapping key
  `"tools"`, the `.github/workflows` directory, a sidecar joined under the git directory, and a
  transcript's `workflows` directory. The rule reads the literal's context; it is not a marker.
  The six kit segments joined under an already-derived base are handled as §8 F1 resolves.
  Observed by AC5.
- **S4a** (rev-3) — the context rule, stated once. A kit-named segment is a homonym when its path
  runs through a tool-owned dot directory (`.git`, `.github`, `.claude`, which also covers a
  `.claude/skills/<name>/` Skill directory that F4's widening would otherwise count), or when the
  operand it is joined onto names a git directory or a transcript (`git`, `gd`, `common`, `sdir`,
  `session`, `transcript`). A quoted `"tools"` counts only when it is joined, so a mapping key, a list
  member or a `.get("tools", [])` argument is not. The operand rule is a name heuristic, and its
  ceiling is written beside it in the gate: a git directory held in a variable named otherwise counts,
  and the remedy is a name that says what it holds. Observed by AC5.
- **S5** — `PREDICATE_EPOCH` moves 4 to 5 and `--rebaseline` runs once, the path epochs 2, 3 and 4
  took. Every reason column is preserved. The epoch block records what the epoch cost, and the
  script header's "does not check" paragraph is rewritten for the new population. Observed by AC6.
- **S6** — The check-install-prefix entry takes its version bump in every carrier. Observed by AC7.

## 3. Non-goals (OUT)

- Lowering any count. Every literal the widening makes visible is drained by units 24 to 29.
- Changing arms 1 and 3, or deleting a marker or a waiver row. `TOOL-aRepatriatedFork-30` does that
  once the ledger is empty.
- Deciding whether drain units may run in parallel. That is §8 F3.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-24` — the ledger rows for the stranding sites, which this
  unit makes visible: `.githooks/pre-commit:54`, three `$ROOT/tools/…` suite lines, a `"tools"` join.
- **hands-off** `TOOL-aRepatriatedFork-25` — the ledger rows for printed and usage strings.
- **hands-off** `TOOL-aRepatriatedFork-26` — the ledger rows for docs, the `<project>/tools/…`
  install destinations among them.
- **hands-off** `TOOL-aRepatriatedFork-27` — the ledger rows for markers and comment prose.
- **hands-off** `TOOL-aRepatriatedFork-28` — the ledger rows for test and fixture files.
- **hands-off** `TOOL-aRepatriatedFork-29` — the ledger rows for gov-side files.
- **hands-off** `TOOL-aRepatriatedFork-30` — an epoch-5 ledger it can drive to zero and delete.

## 4. Design

### Evidence

Every count here is from the 2026-09-25 prefix census at `2143b6d6` (the census record `2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md`). PINNED, measured on
2026-09-25.

- Arm 2, the ledger, counts 904 occurrences over 139 files, equal row for row to
  `tools/install-prefix-carried.txt` (census §0).
- Arm 1 sees 43 root-spelling lines: 11 waived and 32 marked. Arm 3 sees 24 lines, all marked, and
  16 of them are arm-3-only (census §0).
- 1098 occurrences in shipped files have no counting arm (the census record). 168 are inside
  the ledger file itself, which leaves 930: 514 in withheld files and 416 in received ones (census
  §1, "What the gate cannot see").
- The four causes are the `/` lead, a directory-only reference, a fixture loose name the epoch-2
  existence filter drops, and test or seed files outside arm 3's population (same section).
- 57 tracked files under the gate's globs are absent from `govkit shipped`. They hold 562 literals
  under the arm-2 predicate (the census record). The census did not run its broad
  regex over them, so their `/`-led, directory-only and join spellings are UNMEASURED. AC6
  measures them.
- The census's arm-3 table lists 10 lines that are not prefix literals: four homonyms and six kit
  segments joined under a derived base.

### Inventory

This unit mints no identifier that a naming cell grades. It adds alternatives to the regex that
`carried_rows` builds, and it replaces the population derivation `derive_received_files` feeds
the ledger with a `git ls-files` over S2's globs. Rev-3: the alternatives live in a python program
inside the gate, beside arm 3's, and `carried_rows` pipes S2's population into it. The shell side
keeps the row shape, the ban, the rebaseline guard and the four verdicts unchanged.

### Migration

One `--rebaseline`, guarded by the epoch it moves. The row count rises by roughly the census's
invisible and unresolved totals. AC6 records the exact figure and reconciles it to the census.

### Rollout

The ledger stays a ban: `--write-ratchet` may lower a count and never raise one. Every drain unit
lowers rows in the commit that drains them.

### Files touched (estimate)

`tools/check-install-prefix.sh` · `tools/check-install-prefix.test.sh` ·
`tools/install-prefix-carried.txt` · `tools/govkit/entries/check-install-prefix.kit.toml`

### Alternatives rejected

- Draining against the epoch-4 ledger. It would read zero with roughly 1500 literals left.
- A second ledger for the newly visible classes. Two accounts of one population is two answers to
  one question, and nothing would join them.

## 5. Production-readiness checklist

- security — none. The gate reads tracked text and writes one tracked file.
- perf / scale — the population grows from 291 shipped sources to every tracked file under the
  globs. It is still one `grep -oHE` over a file list; AC6 records the wall time before and after.
- error / empty / loading states — an empty population still refuses as a dead probe, which is
  `carried_live`'s job and is unchanged.
- observability — `--list` prints each row with its count, and the epoch block states the cost.
- risks — a predicate that matches prose which is not a path. S4 and §8 F1 bound it, and AC5
  observes the homonyms uncounted.
- testing — one fixture per widened class in the gate's self-test, run red on epoch 4 first.
- migration — the one rebaseline.
- user docs — the gate header. No `help/` page covers this gate.

## 6. Acceptance criteria

- **AC1** — When `check-install-prefix.sh --list` runs at epoch 5 inside a fixture kit source that
  carries exactly one literal of each S1 spelling, each of the five appears as one counted
  occurrence. Rev-3: so do the three S1a spellings, a literal `scripts/` prefix, a shell
  derived-base sibling path and a python `parent / "<kit>"` join, each in its own file.
  Red when: any S1 or S1a spelling is absent from the rows.
- **AC2** — Red-first control: the same fixture graded by `2143b6d6`'s gate counts none of the five.
  Recorded in the acceptance ledger before the predicate changes.
  Red when: epoch 4 already counts one of them, so the widening proves nothing about it.
- **AC3** — When the fixture adds an untracked-by-descriptor file under its `tools/` carrying one
  literal, the row for that file appears; a literal in the fixture's ledger file does not.
  Red when: the population is still `govkit shipped`, or the ledger counts its own rows.
- **AC4** — When a fixture line carrying a literal also carries a `gov:root-fixture` marker, arm 1
  still passes it and the ledger still counts it.
  Red when: the marker suppresses the ledger count.
- **AC5** — When the fixture carries the four homonym shapes of S4, the ledger counts none of them,
  and `git grep -n` over the real tree finds each of the four census sites still present.
  Red when: a homonym is counted, or a census homonym no longer exists, so the arm matches nothing.
- **AC6** — When `check-install-prefix.sh --rebaseline` runs once on the real tree, it prints
  `REBASELINED for predicate epoch 4 -> 5`, and a second invocation refuses. The acceptance ledger
  records the new total and reconciles it to the census's 904 + 930 + 562, naming every difference.
  Red when: the second run writes, or the total differs from the census by an unexplained amount.
  figure: DERIVED at observation time; the census figures are PINNED at `2143b6d6`.
- **AC7** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit.
  Red when: a check-install-prefix carrier was missed.
- **AC8** (rev-3) — When the resolver the counter runs through is replaced by one naming a python
  that does not exist, `--write-ratchet` does not leave an empty ledger at exit 0 and `--check`
  exits non-zero.
  Red when: a dead counter reads as a population carrying zero literals.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates`

New arm: `tools/check-install-prefix.test.sh` · one fixture literal per S1 spelling, the S3 marker
case and the S4 homonyms, each staged red against epoch 4 · the suite's assertion floor rises by
the new arms

## 8. Open questions

- **F1 — how does a pure ban treat the six kit segments joined under an already-derived base?**
  Examples are `settings-merge.py:554` and `test_codebase_map.template.py:65`. The path is correct
  and the base is derived, but the segment is a kit's name typed as a literal.
  Option (a): count them, and have the owning drain unit derive the segment too, from the
  descriptor's own directory name. Option (b): a predicate rule that skips a kit segment whose left
  operand is a variable. That cannot be verified textually, so it would also skip a variable that
  holds a literal. Option (c): a new marker for this class, which survives
  `TOOL-aRepatriatedFork-30`. Recommendation: (a). The owner's end state has no marker and no
  grandfathering, and (b) opens a hole that looks like a pass.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F2 — is a `<gov>/tools/…` spelling a hard-coded prefix?** WIRE carries 17 of them, and
  `adopt-memory-recall.sh:203` prints one. They name gov's own checkout, where the prefix really
  is `tools/`, so each is correct today. Option (a): count them and drain them to a prose token
  naming gov's kit root, which `TOOL-aRepatriatedFork-26` spells once. Option (b): the `<gov>/`
  lead puts a spelling outside the ban by rule, because it describes gov's layout and not the
  adopter's. Option (c): derive where printed, and use (a)'s token in prose. Recommendation: (c).
  The owner ruled that all kit prefixes are relative, and gov relocating its own kits would rot
  every one of them under (b).
  RESOLVED (owner, 2026-09-25): (c), the recommendation.
- **F3 — may the drain units run in parallel?** Under the ownership rule in each unit's §4, three
  groups are FILE-disjoint: 24, 25 and 26, then 27 and 29, then 28 after both. But every drain unit
  lowers `tools/install-prefix-carried.txt`, whose SLACK state reds until the fallen count is
  written, and bumps the version carriers of every kit it moves. Most kits are moved by several
  units. BUILD-METHOD M6 clause 3 forbids parallel passes over a shared mutable record.
  Option (a): run them in sequence, each unit lowering its rows and bumping its kits in its own
  commit; this is the order every header in this set declares. Option (b): run the file-disjoint
  groups in parallel, with no unit writing the ledger or a version carrier; after each group joins,
  the main loop runs `--write-ratchet` and bumps each moved kit once. That join step is not an M6
  pass kind, so (b) also needs a BUILD-METHOD change. Recommendation: (a). (b) trips M3 veto 2 as
  a governance-carrier change, and the wall clock it saves is spent by passes that run no suite.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F4 — does the ban see a hard-coded prefix other than gov's own?** Epoch 5 as first specced
  counts only `tools/`, so a new literal `scripts/<kit>/...` would pass. Option (a): the predicate
  counts a kit segment under ANY literal install prefix, not only gov's. Option (b): count `tools/`
  alone. Recommendation: (a). Raised by the orchestrator from the spec set's own gap note.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: the remaining hard-coded kit
  prefixes are found and drained first, before `TOOL-aRepatriatedFork-18`'s held leg; the drain
  covers every class, fixtures and gov-side files included; and the end state is a pure ban with
  no carried list, no waiver file and no marker. This unit is the widening that makes that
  population countable, on the epoch precedent of `TOOL-cMendedVintage-5`.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation. F4 added and resolved: the ban counts a kit segment under any literal install prefix.
- rev-3 · 2026-09-29 · the unit pass, before code. Measuring the predicate over the real tree
  showed three things rev-2 did not say. F4 and F1(a) reach a kit's name typed after a derived base
  in shell too, not only in the six python joins, so S1a counts both. F4's widening makes a
  `.claude/skills/<name>/` Skill directory and a bare repo's `hooks/` count as kit paths, so S4a
  states the context rule as one rule rather than four instances. And a regex over `grep -oE` cannot
  read a join's operand, so S1b moves the counter into python and adds AC8 for the dead producer
  that move makes possible.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count hardcoded kit prefix literals in shipped files"`
ranked `kit_rel`, `corpus_files` and `kit_dir`. None of them grades a spelling, and the probe
cannot see shell (`unscanned layers: .sh`). The seam is `carried_rows` and the epoch guard in
`tools/check-install-prefix.sh`, extended in place: epochs 2, 3 and 4 widened the same regex
through the same `--rebaseline` (`TOOL-aScouredKit-20`, `TOOL-cWidenedNet-1`,
`TOOL-cMendedVintage-5`), so no existing seam is bypassed.

Recall terms used: `install-prefix carried ban predicate-epoch rebaseline widening root-fixture
prefix-literal waiver shrink-only literal`.
