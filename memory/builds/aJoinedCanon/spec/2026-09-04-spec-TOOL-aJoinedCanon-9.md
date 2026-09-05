# TOOL-aJoinedCanon-9 — the production-readiness row set becomes a declaration

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 9 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Move §5's ten production-readiness rows out of the copied skeleton and into a `.memory-tree.conf`
declaration the skeleton renders from, so the sweep a project performs is the sweep that project
declared. This buys two things a copied skeleton cannot: the row set becomes CHECKABLE, and it
becomes a per-project tailoring hook symmetric with the way `DISCIPLINES` is already declared rather
than hardcoded.

The saving is author attention, not bytes. Finding C3 measures the dead rows at 22,287 B, 0.26% of
the corpus, and finding 32's own skeptic said MEDIUM overstates it under a cost lens. What is being
bought is that two of ten checklist rows stop being questions whose answer is known before the spec
is read, and that a row a project drops becomes visible instead of indistinguishable from a row it
answered.

## 2. Scope (IN)

- **S1** — `.memory-tree.conf` declares `READINESS_ROWS`, a `|`-separated list of the §5 row labels,
  and `READINESS_ROWS_CUTOFF`, the date from which the presence arm grades a spec. The kit's
  `tools/memory-tree/.memory-tree.conf.example` ships both, with the ten current rows as the value an
  adopter starts from, and the key's comment states that the value is the ADOPTER's to change and
  names the one edit that changes it.
- **S2** — the canonical `render_doc` in `tools/lib/render-doc.sh` gains a third substitution,
  `{{READINESS_ROWS}}`, which expands the `|` list into the skeleton's bullet lines. Its two inline
  copies move byte-identically in the same commit.
- **S3** — `tools/memory-tree/SPEC-TEMPLATE.template.md` replaces its ten literal skeleton rows with
  that token, and the prose above the skeleton states where the rows now live. `memory/TEMPLATE-SPEC.md`
  is re-rendered from it, never hand-edited.
- **S4** — `tools/memory-tree/kit.toml` declares `READINESS_ROWS` in the `SPEC-TEMPLATE.template.md`
  rule's `placeholders`, and both new keys in its `[config]` key lists.
- **S5** — check 12 gains a §5 row-presence arm inside its existing awk: for every declared row, the
  §5 body must contain that row's label. Gated by `READINESS_ROWS_CUTOFF`, blank means off.
- **S6** — the arm's predicate is run over the real tree BEFORE it is wired, printing hits AND
  near-misses, and the result is recorded in the conf comment beside the key.
- **S7** — `tools/memory-tree/check-memory-hygiene.test.sh` gains a red fixture (a post-cutoff Tier-2
  spec missing one declared row) and a green twin, and the red is OBSERVED failing before the arm
  lands.
- **S8** — gov's own `.memory-tree.conf` declares EIGHT rows, dropping `a11y` and `i18n` per F1. The
  kit example keeps all ten. That divergence is the point rather than a defect to reconcile: it is
  the first demonstration that the key is per-project, and it is safe because no gate compares the
  live conf's VALUES to the example's — the govkit selfcheck joins KEYS to the descriptor's lists,
  which is AC1, and nothing else reads the example at all outside the absent-conf seeding path.
- **S9** — the adopter tailoring path is documented and OBSERVED, because it is the half of F1's
  ruling that no other scope item carries. Three parts. The example's comment (S1) is where an
  adopter reads that the row set is theirs. `tools/memory-tree/README.md` gains `READINESS_ROWS` and
  `READINESS_ROWS_CUTOFF` in the conf list it already keeps at its "Copy … and edit" step, with the
  same statement, so the answer is reachable without opening the checker. And the no-overwrite
  property is ASSERTED rather than assumed: it already holds by construction at
  `adopt-memory-tree.sh:47-51` (the example is copied only when the conf is ABSENT, then the script
  exits 1) and `:57-60` (a tree already carrying the `gov:kit memory-tree@` marker is an early exit
  0), so this unit ADDS no code for it and instead pins it with AC9 — a property nobody observed is
  a property nobody can rely on.

## 3. Non-goals (OUT)

- Grading whether a row's ANSWER is considered. The arm reads presence only, exactly as the
  acceptance-witness arm reads shape only. A row answered `N/A` with no thought passes, and that
  limit is stated in the gate's own header rather than left for a reader to discover.
- Retrofitting the specs that already drop rows. There are 48 of them under this unit's own
  predicate, measured below, and every one is grandfathered by the cutoff.
- Deleting `a11y` or `i18n` from the kit's shipped example. The kit installs into repos with user
  interfaces; what gov declares for itself is §8's F1, RESOLVED as a drop, and gov's answer is not
  the kit's default. The ruling makes this non-goal load-bearing rather than incidental: the ten
  shipped rows are what an adopter with an interface starts from, S9 is how that adopter changes
  them, and the two files diverging is S8.
- The charter pair. `AGENTS.md:115` and `coding-governance-agents.template.md:37` both restate this
  row set as a nine-item chain that omits `risks`, so a third carrier of the same fact already
  disagrees with the skeleton. F1 widens that gap rather than closing it — the charter's menu keeps
  `a11y` and `i18n`, which gov's declaration now drops, so the two differ in three rows instead of
  one. Widening it is acceptable ONLY because the charter's menu is a design-pass prompt for any
  project and gov's declaration is gov's own sweep; they were never the same list, and this unit
  makes that visible instead of inventing it. Fixing it is a `playbook`-stream edit against a byte-gated 48 KiB
  ceiling, and it is named here as the follow-up this unit does not do. Until it lands, the
  declaration is the single home for the SKELETON's rows and not yet for the charter's menu.
- `TOOL-dTieredTribunal-17`, the open row where `plan_state` in `tools/unattended/unattended.sh` maps
  spec sections by ordinal and mis-grades every Tier-1 spec because §5 is legitimately absent. It is
  adjacent, it is another consumer of this section, and it is a different unit.

## 4. Design

### Data model

`READINESS_ROWS` holds the row LABELS, in skeleton order, separated by `|`. Two values ship, and
they are DIFFERENT on purpose (S8) — the example is what an adopter starts from, gov's conf is what
gov swept down to under F1:

```
# tools/memory-tree/.memory-tree.conf.example — all ten, the adopter's starting value
READINESS_ROWS="security|perf / scale|a11y|i18n|error / empty / loading states|observability|risks (concurrency, data-loss, rollback hazards)|testing + left-shift gates|migration / rollback|user docs"

# .memory-tree.conf (gov's own) — eight; a11y and i18n dropped per F1
READINESS_ROWS="security|perf / scale|error / empty / loading states|observability|risks (concurrency, data-loss, rollback hazards)|testing + left-shift gates|migration / rollback|user docs"
```

Each field is the row label byte-for-byte as the skeleton writes it, `risks` carrying its
parenthetical and all, because AC7 compares the rendered bullets to these fields directly. That is
NOT the token the measurement below was taken with, and the note under that table is the
reconciliation the builder owes.

A `|` list on one line rather than a multi-line value, for two reasons that are properties of this
tree. Every other multi-item key in this conf is a single line (`FAMILIES`, `ARMS_FLOORS`,
`ACCEPTANCE_LEDGER_GRANDFATHER`), and `.memory-tree.conf` is a declared member of
`RECALL_EXTRA_SOURCES`, whose extractor makes one chunk per `KEY=value` LINE — a value spanning lines
would put only its first row in the retrieval corpus.

`READINESS_ROWS_CUTOFF` is a date, taking the STREAMS_CUTOFF semantics rather than the
SPEC10_CUTOFF ones: it switches one rule on, so blank means off, and it does not resolve forward.

### Where the shipped default lives, and why there is no fourth copy

There is exactly one literal row set, and it is the conf. No script carries a default copy, because
three presets holding the same ten rows is the class this repo refuses and has a gotcha record for
(`memory/gotchas/two-answers-to-one-question.md`, whose own worked example is this very template
pair). Each reader resolves a blank value into a defensible outcome instead of into a literal:

| Reader | `READINESS_ROWS` blank |
|---|---|
| `check-memory-hygiene.sh` | arm off when the cutoff is also blank; REFUSES when the cutoff is armed, because an armed rule with no row set grades nothing |
| `adopt-memory-tree.sh` | refuses to render; it already refuses when the conf is absent, copying `.memory-tree.conf.example` and stopping so a person edits it |
| `kit-dogfood-parity.test.sh` | exit 2 misconfigured, its existing channel for a conf it will not render against |

An adopter therefore always holds a value by construction, because the only path that renders the
template is the one that first seeds the example. An adopter whose conf PREDATES the key is
unaffected: their rendered `memory/TEMPLATE-SPEC.md` already exists, `adopt-memory-tree.sh` refuses
to overwrite a tree carrying the marker, and the arm is off until they declare a cutoff.

All three readers still PRESET the variable above their conf source. That is not a default, it is
`set -u` safety, and the reason is recorded at `check-memory-hygiene.sh:52-56`: without the preset
the gate ABORTS rather than fails in every adopter tree whose conf predates the key.

### How an adopter changes the set (F1's second half)

The ruling that drops two rows from gov's declaration is only safe if an adopter can put them back,
so this is a scope item (S9) rather than a consequence. What was CHECKED in
`tools/memory-tree/adopt-memory-tree.sh` before writing it:

- The conf is never rewritten on an update. `:47-51` copies `.memory-tree.conf.example` only when
  `.memory-tree.conf` is ABSENT, prints "EDIT IT … then re-run", and exits 1 — so the copy happens
  exactly once, before the adopter has a declaration to lose. `:57-60` then makes a tree already
  carrying the `gov:kit memory-tree@` marker a clean no-op exit 0, which is the path every
  re-run after adoption takes. The property the owner asked for therefore already holds, and this
  unit adds no code for it; AC9 pins it so a later refactor cannot quietly take it away.
- The cost of that same property: a key ADDED to the example after adoption never reaches an
  existing adopter's conf. `READINESS_ROWS` is such a key. That is why every reader resolves blank
  into a defensible outcome in the table above rather than into a literal, and why the arm is off
  until the adopter declares a cutoff — an adopter who never touches their conf again is unaffected
  in both directions.

So the adopter-facing surface is two files and neither is kit-owned code: the comment beside the key
in their own `.memory-tree.conf`, and the kit README's conf list. Adding `a11y` back is editing one
`|`-separated string and re-running the render. Nothing requires reading
`check-memory-hygiene.sh`, which is the bar F1's ruling set.

### The render token

`render_doc` gains the token and the one transform that turns the list into bullets:

```sh
rows=${READINESS_ROWS//|/$'\n'- }
out=${out//\{\{READINESS_ROWS\}\}/"- $rows"}
```

The transform sits INSIDE the marked block rather than in the callers, so it is covered by the
parity table already gating that block (`tools/lib/resolve-python.test.sh:88-91`, the `render_doc`
row). A transform written per-caller would be a second duplication that nothing compares: gov's live
copy is written by the parity test's `--render` and an adopter's by the adopter, so the two
formatters never meet and no gate would see them diverge.

`tools/check-kit-placeholders.py` joins a descriptor's declared `placeholders` to the literal
`{{TOKEN}}` spellings its adopter substitutes, and its `scan_substituted` already matches the
backslash-escaped brace form the block is written in — so S4's declaration is satisfied by S2's edit
with nothing further. This is the seam §10 names.

### The check-12 arm

It sits in the Tier-2 block, after the empty-body walk and beside the §10 evidence arm, and it
follows that arm's shape: a section blob, `index()` over lowercased text rather than a regex, and
four conjuncts on the guard.

For each declared row, both the label and the §5 body are lowercased and stripped of every
non-alphanumeric byte; the row is present when the squashed label is a substring of the squashed
body. Squashing is what makes the corpus's real spellings agree: it takes the bolded form, the
`-`-led form, and the COMBINED row (`- a11y / i18n — N/A.` and `- a11y — N/A. i18n — N/A.`) that a
line grep counts once. That combined form is why finding C3's own denominators differ, 397 for a11y
against 282 for i18n, and it is an artifact rather than a fact about the corpus: 38 Tier-2 specs in
this tree write the two rows on one line.

The arm does not check that a row was ANSWERED, only that it is named. A `migration` row whose text
happens to appear inside the security row's answer satisfies it. That limit goes in the check's own
header, per the charter's rule that a gate states what it does not check.

### Measured before wiring, per §7's candidate-predicate rule

Run over the 358 tracked Tier-2 specs on this branch at `base 750ca0ca`, with the ten current rows as
the declaration:

| | |
|---|---|
| Tier-2 specs graded | 358 |
| specs missing at least one declared row | 48 |
| finding C3's line-grep count | 39 |

| Row | missing | of which a looser token is present (near-miss) |
|---|---|---|
| `user docs` | 39 | 12 |
| `risks` | 33 | 4 |
| `error / empty / loading states` | 30 | 11 |
| `perf / scale` | 28 | 17 |
| `a11y` | 27 | 0 |
| `i18n` | 27 | 0 |
| `testing` | 15 | 0 |
| `migration` | 12 | 0 |
| `security` | 10 | 0 |
| `observability` | 10 | 0 |

The near-miss column is the reason the rule is "measure first" rather than "wire and see". A dropped
row and an ABBREVIATED one are not the same defect, and this predicate calls them the same thing:
`2026-08-29-spec-TOOL-aGradedDoorway-7.md` writes `- help/ docs` where the skeleton says
`user docs`, which is a spelling variance and not a missing sweep. The a11y and i18n counts, 27 each,
reproduce finding C3's numbers exactly, which is the cross-check that the predicate is measuring the
thing the finding measured.

Nothing is repaired from that table. It is EVIDENCE FOR THE CUTOFF, the same use the conf already
makes of its other pre-wiring measurements, and the whole 48 is grandfathered.

**Two things re-measured at rev-2, when F1 was folded.** Both were run against the branch tip rather
than `base 750ca0ca`, where 364 Tier-2 specs are graded instead of 358; the table above is left at
its pinned base and is not restated with tip numbers.

- The 48 SURVIVES F1 unchanged. Re-running the union with `a11y` and `i18n` removed from the declared
  set returns the same 48 specs: every spec missing one of those two is already missing another row,
  so not one drops out. That is why §3's non-goal, §5's risks row and AC6 all keep the figure — they
  were checked rather than assumed, because a count that only made sense under the ten-row set is
  exactly the half this build's own gotcha record says gets left standing.
- The table's LABELS are the short tokens `risks`, `testing` and `migration`, and the declared value
  above carries the long ones. Under the arm as specified — squash the declared label, substring it
  against the squashed body — the long `risks (concurrency, data-loss, rollback hazards)` is missing
  from 324 of 364 Tier-2 specs, because almost nobody restates the parenthetical. So the declared
  value and this measurement do not describe the same predicate. It is inert while the cutoff is
  forward and it is fatal the first time anyone sets the cutoff backwards, AC6's own second sentence
  included. The builder reconciles it before wiring, under S6, and records which form the arm
  matches: either the declaration carries the short tokens and AC7's byte-identity is dropped, or the
  arm matches a label PREFIX up to its first parenthesis. This spec does not pick — it is a design
  question the measurement raised, not a fork the owner ruled on.

### Migration

The cutoff is set STRICTLY AHEAD of the newest spec filename date across every live branch at
landing, not ahead of this branch alone — the `SPEC10_EVIDENCE_CUTOFF` idiom, whose comment records
21 specs on three other branches that a landing-day cutoff would have redded. This paragraph is now
F2's RESOLUTION rather than the recommendation it started as: the ruling is build-wide, and it is
forward regardless of F1, so nothing in it depends on how many rows gov declares. Enumerated at writing
time: the newest spec filename date on this branch is 2026-09-04, and `git for-each-ref refs/heads`
shows twelve branches with 2026-09-04 commits whose spec dates are UNVERIFIED from here. The builder
re-enumerates and records the result beside the key.

The consequence, stated because it is the same trade three sibling cutoffs already record: the
corpus then exercises NEITHER arm on day one, so S7's fixtures are the coverage rather than a
supplement to it.

Rollback is reverting the conf keys, the template pair and the arm together. The rendered document
is regenerated, never edited, so there is no third thing to undo.

### Files touched (estimate)

| File | Change |
|---|---|
| `.memory-tree.conf` | both keys, each with its measurement and its blank semantics; `READINESS_ROWS` at gov's EIGHT rows per F1 |
| `tools/memory-tree/.memory-tree.conf.example` | both keys, the ten rows as the starting value, and the comment telling an adopter the set is theirs to change |
| `tools/memory-tree/README.md` | both keys in the conf list at its "Copy … and edit" step, with the same statement (S9) |
| `tools/lib/render-doc.sh` | the token and the one transform |
| `tools/memory-tree/adopt-memory-tree.sh` | the same block byte-identically, plus the blank refusal |
| `tools/memory-tree/kit-dogfood-parity.test.sh` | the same block byte-identically, plus the exit-2 path |
| `tools/memory-tree/kit.toml` | `placeholders`, `required_keys_render`, `optional_keys` |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | §5 skeleton rows become the token; the prose above the fence explains the declaration |
| `memory/TEMPLATE-SPEC.md` | re-rendered by `--render` |
| `tools/memory-tree/check-memory-hygiene.sh` | preset, `-v` bindings, the arm, the version marker |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixture conf keys, one red fixture, one green twin |

The kit version bump rides in the same commit and touches SIX `gov:kit memory-tree@` carriers, not
the three that `check-verdict-epoch.sh`'s remediation message names. That is an open defect in the
message, recorded twice as `TOOL-aSiftedFork-5` and `TOOL-dSettledRoster-4`, and following the
message alone costs a second full-bar cycle.

The arm adds no `fail` call site — check 12 has exactly one, at
`tools/memory-tree/check-memory-hygiene.sh:1291`, and the arm prints into the same collected stream.
So `ARMS_FLOORS` and the harness-arms leg are unmoved.

### Alternatives rejected

- **Keep the skeleton's ten literal rows and let the conf declare a possibly-different set.** This is
  the smallest diff and it is the defect. Two carriers of one fact, with no gate between them, is
  precisely the class whose gotcha record names this template pair as its worked example.
- **Delete the two dead rows from the kit skeleton and declare nothing.** Smaller still, and it buys
  most of gov's attention win, but it imposes a shell-and-Python repo's answer on every adopter and
  leaves the row set as uncheckable as it is today. F1 is NOT this alternative arriving by another
  route, and the difference is the whole ruling: the owner dropped the two rows for gov AND required
  that an adopter can declare their own set, which is the key rather than a deletion.
- **Grade the N/A RATE rather than row presence.** It measures the thing the finding actually
  observed, and it is unimplementable as a merge-bar leg: 26.9% of §5 bullets across the corpus carry
  `N/A` and a threshold over that would red honest specs for having little to sweep.

## 5. Production-readiness checklist

- security — N/A. The change reads two more declared values and writes no new path. The conf is
  already sourced by all three readers.
- perf / scale — one extra `split()` and a per-row `index()` inside an awk pass that already walks
  every spec body. The `memory hygiene` leg's declared ceiling in `tools/gate-legs.json` is untouched.
- a11y — N/A, no interface. This row is the unit's own subject and it is answered N/A, which is the
  evidence F1 was ruled on. It stays written here because this spec predates the cutoff and is
  graded against the ten-row skeleton it was drafted under; specs written after gov's declaration
  drops to eight will not carry it.
- i18n — N/A, no user-facing strings. Same standing as the row above.
- error / empty / loading states — the three blank cases are the design and are tabled above. A
  declared row that is empty between two `|` separators is skipped rather than demanded, because a
  trailing separator is a typo and not a request for a nameless row.
- observability — the finding message names the missing row and the cutoff that armed the rule, in
  the shape check 12's sibling arms already use.
- risks (concurrency, data-loss, rollback hazards) — the real risk is a cutoff set too early. It reds
  48 landed specs and blocks every run until reverted, which is why the date is enumerated across
  branches rather than taken from this one.
- testing + left-shift gates — S7's two fixtures, with the red observed before landing. The suite's
  own conf declares the cutoff ahead of every existing fixture, so no fixture in it changes verdict.
  S9's no-overwrite property is covered by AC9's observation rather than by a new test file, because
  the property is two early-exit branches that already exist and a fixture repo would be a second
  copy of the adopter to keep fresh.
- migration / rollback — no data migration. Reverting is the conf keys, the template pair and the arm
  in one commit.
- user docs — `tools/memory-tree/README.md` gains both keys in its conf list, stating that the row
  set is the adopter's to declare and naming the one edit that changes it; the template's own §5
  prose is where an author reads the rule. Under F1 this row stopped being bookkeeping: the README
  and the example's comment ARE the adopter tool the ruling required, so a missing sentence here is
  a missing deliverable rather than a thin doc.

## 6. Acceptance criteria

- **AC1** (S1, S4) — When `READINESS_ROWS` is declared in `.memory-tree.conf` and
  `python tools/govkit/govkit.py --selfcheck` runs, the key resolves in the memory-tree entry's
  config key lists and the run is green. It reds if the key is declared in the conf and in no list.
- **AC2** (S2, S3) — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the
  template edit and the re-render, it reports parity. Staging the render token in
  `tools/memory-tree/SPEC-TEMPLATE.template.md` WITHOUT re-rendering turns it red, naming the pair.
- **AC3** (S2) — When `bash tools/lib/resolve-python.test.sh` runs, every inline `render_doc` copy
  matches the canonical block. Editing `tools/lib/render-doc.sh` alone reds it, naming both copies.
- **AC4** (S2, S4) — When `python tools/check-kit-placeholders.py` runs, `READINESS_ROWS` appears as
  declared and substituted for the memory-tree kit. Declaring it in `tools/memory-tree/kit.toml`
  without the adopter substitution reds it.
- **AC5** (S5, S7) — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, the red fixture
  fails check 12 with a message naming both the missing row and `READINESS_ROWS_CUTOFF`, and its
  green twin is silent. The red is observed BEFORE the arm lands, by staging the fixture against the
  unmodified checker and confirming it passes there.
- **AC6** (S5, S6) — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tracked
  tree with the cutoff armed at the enumerated date, it reports no §5 row finding, because every
  spec that would trip it predates the cutoff. Setting the cutoff to `2026-01-01` instead reports 48.
- **AC7** (S3) — When `memory/TEMPLATE-SPEC.md` is read after the render, its §5 skeleton rows are
  byte-identical to the `|`-fields of `READINESS_ROWS`, in order. A row edited in the rendered file
  by hand is reverted by the next `--render` and reported by AC2's gate.
- **AC8** (S8) — When `bash tools/run-gates/run-gates.sh` runs with gov's `.memory-tree.conf`
  declaring EIGHT rows and `tools/memory-tree/.memory-tree.conf.example` declaring ten, the bar is
  green and `memory/TEMPLATE-SPEC.md` §5 carries eight bullets with no `a11y` and no `i18n` line.
  This is the criterion that the divergence is legal: a leg that redded on it would be a gate
  comparing the live conf's VALUES to the example's, which is the thing S8 asserts does not exist.
- **AC9** (S9) — When `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` is re-run in a tree
  that already carries the `gov:kit memory-tree@` marker, it exits 0 and `git diff --stat
  .memory-tree.conf` is empty — an adopter's declaration survives a kit update. Run in a tree with
  NO conf, the same command instead writes `.memory-tree.conf` from the example carrying all ten
  rows and exits 1. Both halves are observed; the second is what makes the first mean something,
  because a script that never writes the conf at all would pass the first alone.
- **AC10** (S9) — When `tools/memory-tree/README.md` is read at its "Copy … and edit" step,
  `READINESS_ROWS` and `READINESS_ROWS_CUTOFF` each appear with the statement that the row set is
  per-project and the pointer to the one edit that changes it. No leg binds this; §7 names it as a
  documented check with its compensating reviewer step.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` ·
`verdict epoch (kit version dates the engine)` ·
`python resolver (behaviour + inline parity + idiom ban)` ·
`kit placeholders (a declared token its adopter substitutes)` · `kit-placeholders self-test` ·
`spec tokens (a spec's own names resolve)` · `harness arms (fail branches armed or pinned)` ·
`marker contracts`

The new arm adds no leg. It lands inside check 12, whose leg is `memory hygiene` and whose self-test
leg is guarded on the kit directory, so a records-only commit still runs the first and skips the
second. `kit/dogfood doc parity` is the leg that binds the template pair and is named in AC2; its
name carries a `/`, which `tools/check-spec-tokens.py` treats as a path and does not resolve, so it
is written here in prose rather than in the list above.

F1's added scope adds no leg either, and two of its criteria are DOCUMENTED CHECKS rather than gated
ones, named here so the exemption travels with its compensating step. AC9 is observed by hand
because the adopter's no-overwrite behaviour is two early-exit branches and a fixture repo for them
would be a second copy of the adopter to keep fresh; the compensating check is that any diff
touching `adopt-memory-tree.sh:47-60` re-runs AC9's two halves. AC10 is prose in
`tools/memory-tree/README.md` and nothing grades prose; the compensating check is that the same diff
re-reads the README's conf list, which is where an adopter looks first and the checker is where they
must not have to look.

`tools/memory-tree/hygiene-parity.test.sh` is NOT on the bar — it appears in no row of
`tools/gate-legs.json` — but it copies the LIVE `.memory-tree.conf` into its fixture repos and its
spec fixtures are dated 2026-08-01. A cutoff set in the past would red it on demand while the merge
bar stayed green.

## 8. Open questions

- **F1 · Does gov's own declaration drop `a11y` and `i18n`, or ship all ten?** Dropping them is the
  whole attention argument: they are answered `N/A` in 99% and 88% of the specs that carry them, and
  a project with no interface and no localized strings is answering a question it has already
  answered 394 times. Keeping them costs two lines per spec and keeps the sweep's shape identical to
  the kit's. RECOMMENDATION: drop both, because the conf is one edit away the day this repo grows a
  rendered surface, and because a checklist row whose answer is known before the spec is read is
  training authors to skim the other eight. This is the owner's call and it is left open.
  **RESOLVED (owner, 2026-09-05): drop both from gov's own declaration, and give adopters a
  documented way to declare their own set.** Gov's `.memory-tree.conf` declares the eight rows that
  remain; the kit's example keeps all ten, which is §3's standing non-goal rather than an oversight.
  The ruling ADDED scope rather than only picking a branch: a repo that later grows a rendered
  surface must be able to put `a11y` back without editing a kit-owned file or reading the checker's
  source, which is S9 and AC9-AC10.
- **F2 · Where does `READINESS_ROWS_CUTOFF` land, and is this build's own set inside it?** F1 decides
  the safe answer, so the two are coupled. The arm demands only that DECLARED rows are present, so a
  spec carrying extra rows is never red — which means a smaller declared set makes an earlier cutoff
  safe. With all ten declared, a cutoff at 2026-09-04 grades this build's own eleven specs and every
  other node's specs of that date, none of which is verified from here. RECOMMENDATION: enumerate
  across `git for-each-ref refs/heads` at landing and set the cutoff one day past the newest spec
  filename date found. The `ACCEPTANCE_LEDGER_CUTOFF` precedent argues the other way, that a gate
  whose first run measures an empty set is an assertion about nothing, and it is a real cost: the
  fixtures become the only coverage. Left open.
  **RESOLVED (owner, 2026-09-05): ahead of the fleet — strictly past the newest spec filename date
  on ANY live branch, enumerated at landing.** This is the build-wide ruling and it is forward
  REGARDLESS of F1, so the coupling this fork asserted between the two is moot: a smaller declared
  set would have made an earlier cutoff safe, and no earlier cutoff is being taken. The
  `ACCEPTANCE_LEDGER_CUTOFF` counter-argument is accepted as the price, and §4's Migration paragraph
  is the procedure.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §2 · §3 · §4 · §5 · §6 · §7 · folded the owner's ruling on F1 (gov's own
  declaration drops `a11y` and `i18n`, AND the kit owes adopters a documented way to declare their
  own set) and on F2 (the cutoff lands ahead of the fleet, forward regardless of F1). §2 gained S8
  and S9 for the added half; §3 corrected the two non-goals that read as open questions; §4 gained
  gov's eight-row value beside the example's ten, a subsection on the adopter path, and two
  re-measurements; §5 restated the a11y, i18n, testing and user-docs rows under the ruling; §6
  gained AC8-AC10; §7 recorded the two documented checks the added scope brought with no leg.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a per-repo declaration of a closed row set the spec
skeleton renders from"` returned no seam that declares a ROW SET, and two this unit EXTENDS rather
than duplicates. The first is `extract_declared` in `tools/check-kit-placeholders.py`, surfaced with
the inventory key `kit placeholders (a declared token its adopter substitutes)`: the join from a
descriptor's declared `placeholders` to the literal spellings its adopter substitutes already exists,
already tolerates the backslash-escaped brace form, and covers `{{READINESS_ROWS}}` with no new code.
The second is the `render` cluster it ranked at the top, whose shell member is `render_doc` in
`tools/lib/render-doc.sh` — the substitution seam this unit adds one token to, with its inline copies
already held byte-identical by an existing parity table. Nothing in the map declares a row set from a
conf key, so the declaration itself is new; `DISCIPLINES` is the closest prior art and it is a closed
enum read by checks rather than a value rendered into a document.

Recall terms used: production-readiness checklist row set a11y i18n N/A declared conf key skeleton
rendered cutoff check 12. The query, `python tools/memory-recall/query.py "why is the
production-readiness row set fixed in the spec skeleton instead of declared per repo"`, returned 40
hits and no record proposing this. Its useful returns were `TOOL-aRuledParchment-1`, which
established the template-plus-conf-gated-check pattern this unit follows, and
`TOOL-dTieredTribunal-17`, the open row on the other consumer of §5's presence, named as a non-goal
in §3.
