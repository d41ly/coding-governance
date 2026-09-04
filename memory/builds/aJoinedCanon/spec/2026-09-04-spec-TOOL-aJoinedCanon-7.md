# TOOL-aJoinedCanon-7 — section 7 states the shape its join reads, and names where a new arm lives

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 750ca0ca · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` resolves a §7 gate name against `tools/gate-legs.json` only when the
names sit on a line that is nothing but backticked tokens, and `memory/TEMPLATE-SPEC.md` never says
so — an author who writes §7 as prose opts out of the only check on it and is never told. This unit
makes §7 state its own shape, adds the one field §7 has never asked for (where a new gate's arm
lands), and makes the checker report how much of the live corpus its leg join is not grading.

## 2. Scope (IN)

- **S1** — A new explainer section in `tools/memory-tree/SPEC-TEMPLATE.template.md`, placed
  immediately above the existing `## §10 Reuse audit` explainer at `:126`, stating: the leg names go
  on a line of their own carrying nothing but backticked names and `·`/`,` separators; a line with a
  `- ` bullet marker, a prose prefix or a trailing clause is not read; prose may sit above or below
  that line freely; only a non-terminal spec is graded at all.
- **S2** — The skeleton's §7 body (`tools/memory-tree/SPEC-TEMPLATE.template.md:216-218`) replaces
  its single sentence with the list-line instruction, a pointer to the S1 section, and the arm-home
  line of S3. It stays short enough to be copied without being read as an essay, per the §10
  precedent that instructional bodies live above the skeleton and not inside it.
- **S3** — The arm-home line, defined in S1 and prompted by S2: when a unit adds or moves a gate arm,
  §7 carries one line per arm reading `New arm: <suite path> · <what stages its failing case> ·
  <assertion floor to move, or none>`. It is prose, it is not machine-graded, and S1 says so in the
  same breath as it defines it.
- **S4** — `tools/check-spec-tokens.py` gains two behaviours. A token that IS a manifest name is
  resolved BEFORE the shape exclusions at `:60`, so a leg name carrying a `/` stops being discarded
  unread. And the run report gains the ungraded population: how many live specs contributed no leg
  name to the join at all.
- **S5** — `tools/check-spec-tokens.test.sh` gains one arm per S4 behaviour plus one for a prose §7
  raising the ungraded count, each observed RED against the unpatched checker first, and
  `FLOOR_ASSERTIONS` (`tools/check-spec-tokens.test.sh:15`) moves with them.
- **S6** — `memory/map/features/spec-tokens.md` records the new report field and both limits the
  checker still has, so the dossier does not describe a checker that no longer exists.

## 3. Non-goals (OUT)

- **Making a prose §7 RED.** That is the §8 fork and it is the owner's to answer. It also owes a
  dated cutoff key, which S1–S6 deliberately do not spend.
- **Widening `LEG_LINE` (`tools/check-spec-tokens.py:71`) to read prose lines.** The other branch of
  the same fork. Its cost is recorded in the checker's own header: treating every backticked §7 token
  as a leg name produced 270 hits, 271 of them from prose in one spec.
- **Retrofitting the corpus.** 448 terminal specs are frozen records and are not graded; the 34
  near-miss §7 spellings the research counted stay as they are. Nothing in this unit edits a landed
  spec.
- **Closing the misspelling hole for a leg name containing `/`.** S4 grades such a name when it
  resolves; a MISSPELLING of one is still skipped by the path exclusion, because redding it would red
  every honest file path on a list line. Stated as a limit in S6, not fixed here.
- **Naming the checker's path inside the shipped template half.** See §4's rejected alternatives —
  it would ship an adopter a dead repo-path citation.
- **Grading whether a declared arm home is real.** The named suite usually does not exist yet when
  the spec is written; a resolver would red every honest spec.

## 4. Design

### What the join reads today, measured at writing time

`python tools/check-spec-tokens.py` prints, on this tree at `750ca0ca`:

```
spec-tokens: 33 live spec(s) · 448 terminal spec(s) not graded · 769 token(s) graded ·
274 citation(s) skipped (untracked path) · 23 waiver(s)
```

Exit 0. Of the 769 graded tokens, 56 are §7 leg names; the rest are §6 witness paths and `path:line`
citations. The join fires only inside `LEG_LINE` (`tools/check-spec-tokens.py:71`), only on specs
`LIVE` matches (`:64`), and each token must survive `NOT_A_LEG` (`:60`).

Three measurements, taken here rather than quoted, because the design depends on which of them is
true:

- **20 of the 33 live specs carry no `LEG_LINE` at all.** The findings record's post-skeptic number
  was 18 of 31, including 10 of `aSurfacedLexicon`'s 14 units; the two extra are this build's own
  tracked specs, so the count moved with the corpus and not with the predicate.
- **24 of the 33 contribute no graded leg token.** The four beyond the 20 have a list line whose
  every token is excluded by shape — a path, a command, or a SHOUTED key.
- **All six `aJoinedCanon` spec files on disk contribute zero.** They were written by six agents who
  had each read the finding that says §7 is silently ungraded, and the house style they used —
  `- ` bulleted leg names — is precisely the shape `LEG_LINE` cannot match. The one line that does
  match, in `TOOL-aJoinedCanon-4`, is a wrapped continuation carrying a `path:line` citation. That is
  the evidence that this is a discoverability defect and not an attention defect.

Two of the 93 manifest names contain a `/` and are therefore discarded by `NOT_A_LEG` before they can
resolve: `kit/dogfood doc parity` and `python resolver (behaviour + inline parity + idiom ban)`. The
first is cited by four of this build's own specs.

### What §7 gains

The S1 section is written the way `## §10 Reuse audit` is written, and for the same stated reason:
the skeleton is COPIED, so an instructional body inside it becomes spec content in every file. The
skeleton keeps a short instruction and a pointer; the explanation sits above.

The section states the shape as the rule and does not name the checker by path. The reason is in
§4's rejected alternatives.

### The arm-home line

`New arm: <suite path> · <what stages its failing case> · <assertion floor to move, or none>`

Three fields, one per question the corpus paid for. The suite is the field finding 26 is about: at
least four criteria were amended because the arm landed elsewhere than the spec said, and the worked
case is `memory/builds/dUnstalledConvoy/build/2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md:12`
— AC4 amended to `tools/run-gates/profile_bar.test.sh` from the `run-gates.test.sh` the spec named,
found at the closing review after the change had silently dropped 42 of 85 legs from every profile.
The second field is charter §7's observed failing case, named at design time rather than discovered
at build time. The third is the pin the arm moves, because a suite that gains an arm and keeps its
floor has stopped ratcheting.

The line carries a prose prefix, so `LEG_LINE` cannot match it and it can never be mistaken for a leg
list. That is a property of the shape, not a convention to remember.

### The checker change

Two edits inside the existing walk at `tools/check-spec-tokens.py:165`:

1. Resolve first. `if tok in legs` is tested before `NOT_A_TOKEN`/`NOT_A_LEG`, so a name that IS in
   the manifest counts as graded whatever its shape. This can never turn a green tree red: the hit
   list is only reachable from the else branch, which is unchanged. Simulated over the 33 live specs
   — graded §7 tokens 56 → 57, hits 4 → 4, all four already waived.
2. Report the ungraded population, one more field on the line the tool already prints. It is a
   COUNT, not a verdict; no exit status changes, so no landed spec goes red and no dated cutoff key
   is spent. It exists because this repo's rule is that a skip announces itself, which the same
   report line already does for the 274 skipped citations.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the S1 section, and the S2 skeleton body |
| `memory/TEMPLATE-SPEC.md` | RENDERED, never hand-edited — see below |
| `tools/check-spec-tokens.py` | two edits in the §7 loop and one report field |
| `tools/check-spec-tokens.test.sh` | three arms and the floor |
| `memory/map/features/spec-tokens.md` | the new field and the two limits |

The two template halves are one edit and the direction is fixed: edit
`tools/memory-tree/SPEC-TEMPLATE.template.md`, then run
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which rewrites `memory/TEMPLATE-SPEC.md`
from it. Hand-editing the live copy is what the `kit/dogfood doc parity` leg exists to red.

No kit version bump is owed. `tools/memory-tree/check-verdict-epoch.sh:68-69` scans the engine and
six delegate modules; a shipped `*.template.md` is not among them, and `kit version markers` asserts
only that each template's `gov:kit memory-tree@` marker equals `KIT_MEMORY_TREE_VERSION` (2.59 in
both carriers today), which an unchanged constant satisfies.

### Alternatives rejected

- **Name `tools/check-spec-tokens.py` in the shipped template.** The checker is not in any kit —
  no `kit.toml` includes it — so an adopter renders `memory/TEMPLATE-SPEC.md` naming a file their tree
  does not have. That copy lives under `MEMORY_ROOT`, which is exactly the corpus the dead-path
  classifier walks, and the rule is stated at `tools/memory-tree/kit-dogfood-parity.test.sh:25-27`: a
  citation is classified as a repo path when its first segment is a tracked top-level directory. In an
  adopting repo with a tracked `tools/`, that is a dead citation this kit shipped them. The shape is
  useful without the path; the path is not useful without the checker.
- **Require the arm home as a machine-graded field.** Nothing in a spec's text distinguishes a unit
  that adds an arm from one that does not, so the predicate would either grade every spec (and be
  satisfied by `New arm: none`) or grade none. That is the could-not-fail shape one level up.
- **Give the counter a threshold and red above it.** A ratchet over a number that moves with every
  new build reds work unrelated to the change that trips it, and the honest version of that demand is
  the §8 fork's branch A, which is per-spec and dated.

## 5. Production-readiness checklist

- security: N/A — documentation plus a read-only lint counter; no new write path, no new input.
- perf / scale: the counter is one integer in a loop that already runs; the leg's ceiling is 60s and
  its self-test's is 120s (`tools/gate-legs.json`), and three scratch-repo arms cost about a second
  each.
- a11y: N/A — no interface.
- i18n: N/A — no user-facing strings.
- error / empty / loading states: unchanged. Every refusal path in the checker (empty spec
  population, unreadable manifest, absent waiver registry) is untouched by S4.
- observability: this IS the observability change — the ungraded population becomes a printed number
  on every bar run instead of a fact only a research pass could find.
- risks: low. The template edit adds no requirement a gate reads, so no landed spec changes verdict;
  the checker edit can only increase the graded count. The real risk is the fold-in order: units 1,
  2 and 5 also edit `tools/memory-tree/SPEC-TEMPLATE.template.md`, so this unit re-renders after
  landing rather than assuming its own copy of the live file.
- testing + left-shift gates: three new arms in `tools/check-spec-tokens.test.sh`, each observed RED
  against the unpatched checker before the change lands. The ungated half — that an arm-home line is
  true — has no arm and no gate; its compensating check is the Tier-2 review, which reads §7 against
  the diff.
- migration / rollback: none needed. The checker change is two hunks and reverts cleanly; the
  template change is prose and reverts through `--render`.
- user docs: `memory/map/features/spec-tokens.md` per S6. No `help/` page — this repo ships no
  end-user surface.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-tree/SPEC-TEMPLATE.template.md` carries the new section, `grep -c
  'LEG_LINE\|line of its own'` finds the shape stated there, and `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` exits 0 with `memory/TEMPLATE-SPEC.md` rendered from
  it rather than hand-edited.
- **AC2** — When the skeleton's §7 body is read at `tools/memory-tree/SPEC-TEMPLATE.template.md`, it
  names the list line and the `New arm:` line, and `bash tools/memory-tree/check-memory-hygiene.sh`
  still exits 0 over the corpus — the body change requires nothing of a landed spec.
- **AC3** — When `python tools/check-spec-tokens.py` runs on this tree, its report line names the
  ungraded live-spec population, and the number it prints for the unchanged corpus is 24 of 33.
- **AC4** — When a scratch spec whose §7 is prose is added to a fixture repo, `bash
  tools/check-spec-tokens.test.sh` shows the ungraded count rise by one and the run still exit 0 —
  observed RED first against the unpatched `tools/check-spec-tokens.py`, which prints no such field.
- **AC5** — When a fixture spec lists a manifest name containing a `/`, `bash
  tools/check-spec-tokens.test.sh` observes it graded rather than skipped, and against the unpatched
  checker the same arm fails.
- **AC6** — When `bash tools/check-testsuite-counts.sh` runs, `FLOOR_ASSERTIONS` in
  `tools/check-spec-tokens.test.sh` equals the new arm total and the suite compares the two, so the
  three added arms cannot be stranded silently.
- **AC7** — When `memory/map/features/spec-tokens.md` is read, it names the ungraded-population field
  and both surviving limits, and `bash tools/run-gates/run-gates.sh` is green with
  `GATE_SELFTESTS=1`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` ·
`kit version markers` · `kit/dogfood doc parity`

New arm: `tools/check-spec-tokens.test.sh` · a scratch repo whose §7 is prose, plus one whose §7
lists a slash-carrying manifest name, both run against the unpatched checker first ·
`FLOOR_ASSERTIONS` 12 → 15.

This unit adds no leg. `spec-tokens self-test` carries `subject: kit` and the guard `tools/`, so the
default bar holds it — this is kit work and its DoD owes
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **FORK 1 · What happens to a §7 that names no leg at all — does the checker eventually RED it, or
  does it learn to read prose?** S1–S6 are common to both branches, deliberately, so answering this
  later costs no rework.
  - **Branch A — red it, behind a dated cutoff.** A live spec whose filename date is at or after a
    new `SPEC_LEGLINE_CUTOFF` and whose §7 contributes no leg name becomes a hit. Cost: one conf key,
    a conf read in a tool that currently reads none, one arm with an observed red, and a corpus that
    stays green because the 20 ungraded live specs all predate the cutoff. It makes the shape
    mandatory, which is the only thing that would have caught the six specs this build wrote.
  - **Branch B — widen `LEG_LINE` so prose lines are graded.** No author burden and no cutoff, but
    the checker's own header records what that costs: 270 hits, 271 of them from prose in a single
    spec. It also cannot see a §7 that names no leg at all, which is 24 of the 33 live specs today —
    so it addresses the near-miss spellings and not the silence.
  - **Recommendation: branch A.** The measured failure is silence, not misspelling, and branch B
    grades more text without grading more specs. The counter S4 adds is what makes branch A's blast
    radius readable before it is chosen: run the tool, read the number.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a spec section 7 gate name resolved against the gate
manifest"` ranks `extract_section` in `tools/check-spec-tokens.py` and the `spec-tokens` affordance
seam above everything else, and that is the seam this unit extends: the §7 walk, the `LEG_LINE`
predicate and the report line all already exist in that file, so S4 is two hunks inside a loop rather
than a new module. No second checker is built, and no conf reader is added — the ranked alternative,
`tools/drift-audit/drift_report.py`'s `load_conf`, is a seam this unit deliberately does not need,
because nothing here is cutoff-gated. The template half reuses the `## §10 Reuse audit` explainer's
own placement rule rather than inventing a second convention for instructional prose.

Recall terms used: `python tools/memory-recall/query.py "why does the spec format never state the
shape that makes its section 7 gate names resolvable" --terms "spec tokens leg line gate manifest
section 7 prose opt-out check-spec-tokens LEG_LINE gate-legs.json template skeleton cutoff"`. It
returned the finding itself, `TEMPLATE-SPEC.md`'s §10 explainer as the placement precedent, the
`spec-tokens` dossier's affordance list, and `TOOL-dTieredTribunal-6`, whose §7 text arm folded for
the same reason this unit exists.
