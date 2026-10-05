# TOOL-aMendedFleet-44 — the map gate refuses a present-tense count of an inventory population in dossier prose

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 44

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The charter's §7 says no count of a derived population is written in prose, and the map is the one
place in this repo that derives the populations its own dossiers keep counting: `MAP.md` prints the
size of every inventory, yet `memory/map/features/run-gates.md` still says "the 86 legs" and
`memory/map/features/codebase-map.md` still says "69 inventory keys", both stale. This unit adds one
arm to the map gate that refuses a digit count of an inventory population in dossier prose unless
the sentence freezes it, which is `memory/guides/ANNOTATION-STYLE.md` A4's first disposition, and
drains the two live hits in the same commit.

## 2. Scope (IN)

- **S1** — `measure_typed_counts(text, inventory_ids)` in `tools/codebase-map/map_lib.py`, a pure
  function, returns the unfrozen hits, each with its line number and matched text, and the number of
  frozen candidates. It reads prose only, the text outside every fenced block, the toml fence
  included, and outside every inline code span, and it splits sentences after a `.` or `;` on the
  whitespace-squeezed paragraph. Observed by AC1, AC2 and AC3.
- **S2** — The predicate, every part a module constant:
  - a COUNT is a run of one to five digits not preceded by a word character, `§`, `#`, `.`, `/`,
    `-` or a backtick;
  - a NOUN is the last hyphen segment of each inventory id, as written and singular, plus `key`
    and `dossier` in both numbers, optionally preceded by `inventory`; the nouns are derived from
    `inventory_ids` at call time, never typed;
  - between the two sit at most an `of the <digits>` clause and one other word that is not one of
    `the`, `a`, `an`, `its`, `this`, `that` or `their`;
  - a candidate is FROZEN when its sentence carries a date, a hex run of 7 to 40 characters,
    `node <tag>`, `measured`, `PINNED`, `at review`, `on the day`, or one of the past-tense verbs
    `was`, `were`, `had`, `shipped`, `landed`, `found`, `named`, `redded`, `left` or `read`.
  Observed by AC2 and AC3.
- **S3** — `test_dossier_prose_carries_no_typed_count` in `tools/codebase-map/test_codebase_map.py`
  and in `tools/codebase-map/test_codebase_map.template.py` runs S1 over every text
  `load_dossier_texts` returns, `FOUNDATION.md` included, prints one line
  `typed-count lint: <c> candidate(s) read in <d> dossier(s), <f> frozen` on every run, and asserts
  no hit. A failure names each hit as `<dossier>:<line>: <match>` and the three remedies: freeze it
  as a past-tense reading that cites the record which measured it, point at the file that owns it,
  or rewrite the sentence without it. The first remedy never asks for a date or a node in the
  dossier, because `TOOL-aMendedFleet-89`'s rule keeps when, where and on which node in the record.
  The standalone runner's tuple gains it. Observed by AC1 and AC2.
- **S4** — The two live hits are drained: the `run-gates` sentence counting legs becomes a
  past-tense reading citing the record that made the measurement its own paragraph already dates,
  and the `codebase-map` bullet counting dossiers and baseline keys is rewritten as a pointer to
  `baseline.toml` and `MAP.md`, which own both figures. Each rewrite is checked against `git log -L`
  for the line before it is made, so the cited record is the one that measured it. Observed by AC1.
- **S5** — The rule is stated where a dossier author reads rules: one bullet in the `## Rules` list
  of `_README` in `tools/codebase-map/gen_map.py` and of its dogfood rendering `memory/map/README.md`,
  and the gate's row in `tools/codebase-map/README.md`, which also states the gap of F3. The bullet
  names S3's three remedies in S3's words. Observed by AC4.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the new definitions, and the prose
  of `memory/map/features/codebase-map.md` is refreshed in the same commit. Observed by AC1.
- **S7** — A selftest arm drives S1 over fixture strings, the positives and negatives of AC3 among
  them. NOT OBSERVED by a criterion here: the suite runs once at the close, and the arm is declared
  under `New arm:` in §7.

## 3. Non-goals (OUT)

- Counts spelled as words. F3 measured them and they are mostly fixed structure, "two files", so
  the arm reads digits only and the README row says so.
- Counts outside dossier prose: the toml fence's `title`, which is where `TOOL-dGatedProse-6`'s
  "Seven joins" sits, and nouns outside the map's inventories, such as the hygiene check count of
  `TOOL-dSpentCeiling-5`. Neither ask is closed here.
- Code comments, which unit 71 sweeps under the same A4 rule.
- A drift signal or a shrink-only pin. F2 chose the gate; the remedy for a false hit is to freeze
  the sentence, which a tolerance would only postpone.
- Bumping the codebase-map kit version, owed once after the last move, at the close.

### Edges

- **hands-off** external — spelled counts and counts in fence titles, recorded as the gap the README
  row states.
- **hands-off** external — the codebase-map kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `fee9f62b`.

- `test_dossier_decisions_are_declining` in the gate is the shape copied: it loads the tree,
  announces an ungraded state instead of passing silently, and asserts with a message naming the
  remedy. The other prose-reading arms, `test_dossier_prose_headings_pinned` and
  `test_dossier_affordance_present_or_graced`, grade presence, not content.
- `load_dossier_texts` in `map_lib.py` returns FOUNDATION and every dossier's raw text without
  parsing claims, and it is already the shared prose reader of `reuse_lookup.py`.
- `ANNOTATION-STYLE.md` A4 names the three safe dispositions of a number: frozen, gated, pointed.
  The arm cannot see "gated" or "pointed", so it refuses the one shape A4 calls unsafe and accepts
  a frozen sentence.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `measure_typed_counts` | function, `map_lib.py` | `py.function`, verb `measure`; `--suggest` answered OK |
| `FROZEN_MARKERS` | module constant, `map_lib.py` | none |
| `test_dossier_prose_carries_no_typed_count` | gate function | `py.function`, verb `test`; `--suggest` answered OK |

### Rollout

The gate template reaches an adopter only when absent, so an existing adopter gets the arm by
copying it in; the kit README's row says so. A new adopter's empty map reads zero candidates and
passes, and the line it prints says it read nothing.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/codebase-map/test_codebase_map.template.py`
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `memory/map/README.md`
- `memory/map/features/run-gates.md`
- `memory/map/features/codebase-map.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

Each predicate below was run read-only over the 27 dossiers and `FOUNDATION.md` at `fee9f62b` on
node a, PINNED, with the S2 freezing rule applied to all three; a hit counts as true when its count
is a present-tense figure of a population that moves.

| Predicate | Matches | Unfrozen | True |
|---|---:|---:|---:|
| A — digits or spelled, a broad noun list such as legs, checks and files | 79 | 38 | 2 |
| B — digits or spelled, the inventory nouns | 28 | 14 | 3 |
| C — digits only, the inventory nouns, determiners excluded (chosen) | 4 | 2 | 2 |

- **A** reds 36 innocent sentences: "two files", "three arms", "first two legs".
- **B** adds the spelled "Two feature dossiers so far", which sits in the same sentence as one of
  C's hits, at the cost of 11 innocent ones, "three writing verbs" and "two cap keys" among them.
- A first cut of C without the determiner exclusion also matched "43 the Skill", a check number
  followed by a noun phrase, which is the reason the exclusion exists.

## 5. Production-readiness checklist

- security — N/A: a read-only regex over committed markdown.
- perf / scale — one pass over the dossier texts the gate already loads.
- error / empty / loading states — no dossiers, or no candidate in them, prints a zero count and
  passes; the printed line is what distinguishes "read nothing" from "read and clean".
- observability — the per-run candidate and frozen counts, and file and line on every hit.
- risks — a future innocent digit count reds the gate; its remedy is a few words of freezing, and
  F1's measurement found no such sentence today. A stale count spelled in words passes, as stated.
- testing — AC2 stages the break on the real gate; AC3 drives the function directly; S7's arm.
- migration — N/A: the two live hits are drained in this unit, so the gate is green on landing.
- user docs — S5's three rows.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/test_codebase_map.py` runs at the unit's tip, it exits
  0, prints `ok   test_dossier_prose_carries_no_typed_count`, and prints a `typed-count lint:` line
  whose candidate count is above 0.
  Red when: the arm is missing from the runner, either live hit survives unfrozen, or the arm reads
  no candidate on a tree that holds some.
  figure: DERIVED at observation time; the F1 probe read 4 candidates, 2 frozen, after draining.
- **AC2** — When the sentence `The bar runs 124 gate legs.` is appended under `## Gaps` in
  `memory/map/features/run-gates.md` in the working tree and the gate runs, it exits 1 and prints
  `FAIL test_dossier_prose_carries_no_typed_count` naming `run-gates.md` with that line's number and
  `124 gate legs`; when the sentence instead reads `The bar ran 124 gate legs, measured 2026-10-04.`
  it exits 0; restoring the file leaves it at exit 0.
  Red when: the unfrozen count passes, or the frozen one reds.
- **AC3** — When a `python -c` caller passes `measure_typed_counts` from
  `tools/codebase-map/map_lib.py` the inventory ids `gate-legs` and `rendered-skills` and, one at a
  time, the texts `see the §7 leg line`, `Check 42 grades the wall, 43 the Skill's hold routing.`,
  a code span holding `86 legs`, and a fenced block holding `86 legs`, it returns no hit for each;
  for `Seven of the 86 legs name a network verb.` it returns exactly one.
  Red when: any of the four negatives hits, or the positive does not.
- **AC4** — When `git grep -n "typed count" -- memory/map/README.md tools/codebase-map/gen_map.py tools/codebase-map/README.md`
  runs, it hits each of the three files, and the `tools/codebase-map/README.md` hit's row names the
  spelled-count gap.
  Red when: an author can read the map's rules without meeting this one.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/codebase-map/selftest.py` · fixture strings for every S2 clause, positive and negative, through `measure_typed_counts`; staged red by dropping the determiner exclusion, which makes the check-number negative hit · none

## 8. Open questions

- **FACT-QUESTION · F1** — Which predicate?
  Probe: the three predicates of §4's table, applied read-only to the dossier prose at `fee9f62b`,
  printing every hit and every frozen near-miss. Observation: the unfrozen hits each predicate
  raises, judged true or innocent sentence by sentence. Liveness: predicate A raised 38 unfrozen
  hits, so the probe can produce a positive, and C's two hits are not a zero reading.
  RESOLVED (agent, 2026-10-04, delegated): C, the only one that reds no innocent sentence in today's
  tree, which the charter's §7 asks of a predicate before it is wired.
- **F2** — A gate arm, a shrink-only pin, or a report-only drift signal?
  RESOLVED (agent, 2026-10-04, delegated): a gate arm with zero tolerance, both hits drained here.
  A drift signal is the "detector nobody consumes" the review counted, and a pin buys tolerance for
  false hits whose remedy, freezing the sentence, costs less than raising a pin with a reason.
- **F3** — Read counts spelled as words?
  RESOLVED (agent, 2026-10-04, delegated): no. Predicate B measured 14 unfrozen spelled-or-digit
  hits with 3 true, and its one true spelled hit shares a sentence with a digit hit C already
  raises; the gap is stated in the kit README rather than paid for in 11 false reds.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#41] lint, A4 of the annotation
  guide, the gate's decisions-pin arm, and a three-predicate probe over the dossiers at `fee9f62b`.
- rev-2 · 2026-10-04 · S3 S4 S5 · the M2 cross-read: S3's first remedy told a dossier author to
  state when and where a number was measured, while `TOOL-aMendedFleet-89` adds a bullet to the same
  Rules list keeping when, where and on which node in the record that measured it; the remedy, and
  S4's drain of the `run-gates` hit, are now a past-tense reading citing that record, which S2's
  `measured` and past-tense markers already freeze, so the predicate does not move.

## 10. Reuse audit

The seams extended are `load_dossier_texts` in `tools/codebase-map/map_lib.py`, the shared prose
reader, and the gate's `test_dossier_decisions_are_declining` in
`tools/codebase-map/test_codebase_map.py`, whose announce-then-assert shape the new arm copies.
`python tools/codebase-map/reuse_lookup.py "flag a present-tense count of a derived population
written in dossier prose"` ranked `population` in `tools/govkit/refusal_join.py`, `derive_scope`,
`load_dossier_texts` and `count_never_falls`; none reads prose for counts, so no existing seam
fits the predicate, and the probe printed `unscanned layers: .sh`, where `git grep` finds no prose
count lint either. Recall returned `TOOL-dGatedProse-6` and `TOOL-dSpentCeiling-5`, two open asks
about typed counts that fall outside this predicate as §3 says, a closing review quoting the §7
rule against an undated count, and A4 itself. Where the report and the tree disagree: the report
named dossier typed counts without a list; the probe found two live ones, both stale.

Recall terms used: `python tools/memory-recall/query.py "is there a lint or gate that refuses a
typed count of a derived population written in prose or in a dossier" --terms "typed count derived
population prose dossier lint shrink-only pin frozen measured A4 annotation-style charter"`
