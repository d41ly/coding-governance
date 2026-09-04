# TOOL-aJoinedCanon-7 — section 7 states the shape its join reads, and names where a new arm lives

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 7 · ratified 2026-09-05

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` resolves a §7 gate name against `tools/gate-legs.json` only when the
names sit on a line that is nothing but backticked tokens, and `memory/TEMPLATE-SPEC.md` never says
so — an author who writes §7 as prose opts out of the only check on it and is never told. This unit
makes §7 state its own shape, adds the one field §7 has never asked for (where a new gate's arm
lands), makes the checker report how much of the live corpus its leg join is not grading, and — per
the owner's ruling on §8 — turns that silence into a hit for any spec written from the cutoff date on.

## 2. Scope (IN)

- **S1** — A new explainer section in `tools/memory-tree/SPEC-TEMPLATE.template.md`, placed
  immediately above the existing `## §10 Reuse audit` explainer at `:126`, stating: the leg names go
  on a line of their own carrying nothing but backticked names and `·`/`,` separators; a line with a
  `- ` bullet marker, a prose prefix or a trailing clause is not read; prose may sit above or below
  that line freely; only a non-terminal spec is graded at all; and — the half the fork's resolution
  adds — a spec whose FILENAME date is at or after `SPEC_LEGLINE_CUTOFF` must carry such a line, so
  from that date the shape is a requirement and not only a reading rule.
- **S2** — The skeleton's §7 body (`tools/memory-tree/SPEC-TEMPLATE.template.md:216-218`) replaces
  its single sentence with the list-line instruction stated as a REQUIREMENT, a pointer to the S1
  section, and the arm-home line of S3. It stays short enough to be copied without being read as an
  essay, per the §10 precedent that instructional bodies live above the skeleton and not inside it.
  An author copying the skeleton after the cutoff is the only reader the S7 arm can still surprise,
  so the demand is stated where they are, not only where it is explained.
- **S3** — The arm-home line, defined in S1 and prompted by S2: when a unit adds or moves a gate arm,
  §7 carries one line per arm reading `New arm: <suite path> · <what stages its failing case> ·
  <assertion floor to move, or none>`. It is prose, it is not machine-graded, and S1 says so in the
  same breath as it defines it — including that it never satisfies S7: the prose prefix is exactly
  what keeps it out of the leg join, so a §7 carrying only an arm-home line still names no leg.
- **S4** — `tools/check-spec-tokens.py` gains two behaviours. A token that IS a manifest name is
  resolved BEFORE the shape exclusions at `:60`, so a leg name carrying a `/` stops being discarded
  unread. And the run report gains the ungraded population: how many live specs contributed no leg
  name to the join at all.
- **S5** — `tools/check-spec-tokens.test.sh` gains one arm per S4 behaviour plus one for a prose §7
  raising the ungraded count, and S7's three below, each observed RED against the unpatched checker
  first, and `FLOOR_ASSERTIONS` (`tools/check-spec-tokens.test.sh:15`) moves with them.
- **S6** — `memory/map/features/spec-tokens.md` records the new report field, the S7 arm and its conf
  key, and both limits the checker still has, so the dossier does not describe a checker that no
  longer exists.
- **S7** — The dated demand, which is the owner's ruling on §8's fork. `.memory-tree.conf` declares
  `SPEC_LEGLINE_CUTOFF="2026-09-06"`; `tools/check-spec-tokens.py` reads that one key; a live spec
  whose filename date is at or after it and whose §7 contributes no graded leg name becomes a hit.
  The hit's token is the spec's own path, so the existing waiver registry can hold it and the
  stale-waiver refusal keeps a cleared one from surviving. A blank or absent key turns the arm off,
  and the report line says which. Three test arms: the post-cutoff red, its pre-cutoff twin green,
  and the blank-key off.

## 3. Non-goals (OUT)

- **Redding a §7 that names no leg BEFORE the cutoff.** S7 grades a spec dated at or after
  `SPEC_LEGLINE_CUTOFF` and nothing earlier. The 31 live specs that contribute no graded leg name
  today all predate it and stay green; redding honest content written before the rule existed is
  what the dated key exists to prevent.
- **Widening `LEG_LINE` (`tools/check-spec-tokens.py:71`) to read prose lines.** The fork's losing
  branch (§8). Its cost is recorded in the checker's own header: treating every backticked §7 token
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
- **Re-measured at the fold, 2026-09-05: 42 live, 26 with no list line, 31 contributing no graded leg
  name.** The three bullets above were taken mid-build with six of this build's eleven specs on disk,
  so `750ca0ca` names the tree the design READ rather than the tree as committed. The ratio held
  while the corpus grew by nine specs in a day, which is the argument for a cutoff over a retrofit:
  the population S7 would have to red is not shrinking on its own.

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
2. Report the ungraded population, one more field on the line the tool already prints. It exists
   because this repo's rule is that a skip announces itself, which the same report line already does
   for the 274 skipped citations. Below the cutoff it stays a COUNT and not a verdict, so no landed
   spec goes red; at and above the cutoff the same silence is S7's hit.

### The cutoff, and the conf read it costs

`SPEC_LEGLINE_CUTOFF="2026-09-06"`, in this repo's `.memory-tree.conf` beside the dated cutoffs
already there — six at the fold, and the count is a `grep -cE '^[A-Z_]+CUTOFF=' .memory-tree.conf`
rather than a number this spec keeps fresh. The date is the build-wide one and is not re-derived here: `TOOL-aJoinedCanon-1`'s
fold measured it across all 44 local and remote refs and all 15 live worktrees — newest spec filename
date 2026-09-04, nothing dated 2026-09-05 anywhere — so 2026-09-06 is the first date this fleet can
no longer write into. Every cutoff this build introduces takes it.

The accepted cost is therefore a fact and not a trade: **the arm grades zero specs on day one**, and
S5's three fixtures are its entire coverage. That is the same state `STREAMS_CUTOFF`,
`SPEC_WITNESS_CUTOFF` and `SPEC10_EVIDENCE_CUTOFF` each shipped in, and the reason the S4 counter is
worth more than it looks: it is the only thing that will show the population crossing the cutoff
before anyone trips over it.

Three properties, each chosen against a precedent in the same conf rather than invented:

- **Blank or absent means OFF**, `SPEC10_EVIDENCE_CUTOFF`'s semantics and for its stated reason —
  this key only ADDS a demand, so it need not select between two canons the way `SPEC10_CUTOFF` must.
  The report line names the cutoff in force, or says the arm is off; a demand that silently
  evaporated would be indistinguishable from one that passed.
- **The hit's token is the spec's own path.** A silence hit has no offending token to name, and
  `memory/project/spec-token-waivers.txt` is keyed by token, so the path is what makes the hit
  waivable at all — and the checker's existing stale-waiver refusal then keeps a waiver alive only
  while the hit is.
- **A filename with no leading date prefix cannot be placed against a cutoff**, so this arm skips it
  and the report says how many. Three such files exist in the corpus and all three are pre-format-era
  records with no status header, so none is live today; the clause is written for the day one is.

The read is one key by regex over `.memory-tree.conf`, NOT a fourth copy of `load_conf` — see §10.
The key is deliberately absent from `tools/memory-tree/.memory-tree.conf.example`: that file's parity
arm (`tools/memory-tree/check-memory-hygiene.test.sh:1508-1524`) covers the keys the memory-tree
ENGINE reads, and `tools/check-spec-tokens.py` is not in that kit — shipping the key there would hand
an adopter a knob no tool of theirs reads, which is the same defect as naming the checker's path in
the shipped template below.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the S1 section, and the S2 skeleton body |
| `memory/TEMPLATE-SPEC.md` | RENDERED, never hand-edited — see below |
| `tools/check-spec-tokens.py` | two edits in the §7 loop, the conf read and S7's arm, one report field |
| `.memory-tree.conf` | the `SPEC_LEGLINE_CUTOFF` key and its comment |
| `tools/check-spec-tokens.test.sh` | six arms and the floor |
| `memory/map/features/spec-tokens.md` | the new field, the S7 arm and its key, and the two limits |

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
  new build reds work unrelated to the change that trips it. The honest version of that demand is
  per-spec and dated, which is what the owner ruled and what S7 builds.

## 5. Production-readiness checklist

- security: N/A — documentation plus a read-only lint counter; no new write path, no new input.
- perf / scale: the counter is one integer in a loop that already runs; the leg's ceiling is 60s and
  its self-test's is 120s (`tools/gate-legs.json`), and six scratch-repo arms cost about a second
  each. S7 adds one filename-date comparison per live spec and one file read per run.
- a11y: N/A — no interface.
- i18n: N/A — no user-facing strings.
- error / empty / loading states: every existing refusal path in the checker (empty spec population,
  unreadable manifest, absent waiver registry) is untouched. S7 adds no fourth refusal: an absent or
  blank `.memory-tree.conf` key turns the arm OFF and says so, because this checker must still run in
  a tree that never adopted the memory-tree kit.
- observability: this IS the observability change — the ungraded population becomes a printed number
  on every bar run instead of a fact only a research pass could find.
- risks: low, and no longer zero — S7 gives this checker its first way to red a spec. The blast
  radius is bounded by the cutoff rather than by argument: no spec in the corpus is dated at or after
  2026-09-06, so day one grades nothing, and the first spec it can red is one written after the rule
  exists and after the skeleton states it. The template edit still adds no requirement a gate reads
  BELOW the cutoff, so no landed spec changes verdict. The real risk is unchanged and is the fold-in
  order: units 1, 2 and 5 also edit `tools/memory-tree/SPEC-TEMPLATE.template.md`, so this unit
  re-renders after landing rather than assuming its own copy of the live file.
- testing + left-shift gates: six new arms in `tools/check-spec-tokens.test.sh`, each observed RED
  against the unpatched checker before the change lands — including S7's pre-cutoff twin, which must
  be seen to distinguish a cutoff that works from one that never fires. The ungated half — that an
  arm-home line is true — has no arm and no gate; its compensating check is the Tier-2 review, which
  reads §7 against the diff.
- migration / rollback: the checker change is three hunks and reverts cleanly; the template change is
  prose and reverts through `--render`. S7 has a rollback short of a revert, which is why blank means
  off: emptying `SPEC_LEGLINE_CUTOFF` disables the arm without touching code.
- user docs: `memory/map/features/spec-tokens.md` per S6. No `help/` page — this repo ships no
  end-user surface.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-tree/SPEC-TEMPLATE.template.md` carries the new section, `grep -c
  'LEG_LINE\|line of its own'` finds the shape stated there, and `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` exits 0 with `memory/TEMPLATE-SPEC.md` rendered from
  it rather than hand-edited.
- **AC2** — When the skeleton's §7 body is read at `tools/memory-tree/SPEC-TEMPLATE.template.md`, it
  names the list line and the `New arm:` line, and `bash tools/memory-tree/check-memory-hygiene.sh`
  still exits 0 over the corpus — the body change requires nothing of a landed spec, and every
  landed spec predates `SPEC_LEGLINE_CUTOFF`, which is the reason and not a coincidence.
- **AC3** — When `python tools/check-spec-tokens.py` runs on this tree, its report line names the
  ungraded live-spec population and the cutoff in force, and the number it prints AGREES with a live
  re-derivation over the same corpus. The pair moves with the corpus and is therefore evidence and
  not the pin: 31 of 42 measured at the fold on 2026-09-05, 24 of 33 when this unit was designed.
- **AC4** — When a scratch spec dated BEFORE the cutoff whose §7 is prose is added to a fixture repo,
  `bash tools/check-spec-tokens.test.sh` shows the ungraded count rise by one and the run still exit
  0 — observed RED first against the unpatched `tools/check-spec-tokens.py`, which prints no such
  field. Below the cutoff the silence is still only counted.
- **AC5** — When a fixture spec lists a manifest name containing a `/`, `bash
  tools/check-spec-tokens.test.sh` observes it graded rather than skipped, and against the unpatched
  checker the same arm fails.
- **AC6** — When `bash tools/check-testsuite-counts.sh` runs, `FLOOR_ASSERTIONS` in
  `tools/check-spec-tokens.test.sh` equals the new arm total and the suite compares the two, so the
  six added arms cannot be stranded silently.
- **AC7** — When `memory/map/features/spec-tokens.md` is read, it names the ungraded-population
  field, the S7 arm with its conf key, and both surviving limits, and `bash
  tools/run-gates/run-gates.sh` is green with `GATE_SELFTESTS=1`.
- **AC8** — When a fixture spec dated at or after `SPEC_LEGLINE_CUTOFF` carries a §7 of pure prose,
  `bash tools/check-spec-tokens.test.sh` observes the run exit 1 naming that spec's path, and the
  byte-identical fixture dated one day before the cutoff exits 0. Both arms observed against the
  unpatched checker first, where the post-cutoff one passes — a cutoff arm that has only ever been
  seen red on a fixture no cutoff could spare is an assertion about nothing.
- **AC9** — When `.memory-tree.conf` declares `SPEC_LEGLINE_CUTOFF=""`, or the file is absent
  entirely, `bash tools/check-spec-tokens.test.sh` observes the post-cutoff fixture of AC8 exit 0 and
  the report line say the arm is off, so a disabled demand cannot read as a satisfied one.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` ·
`kit version markers` · `kit/dogfood doc parity`

New arm: `tools/check-spec-tokens.test.sh` · a scratch repo whose §7 is prose, one whose §7 lists a
slash-carrying manifest name, and S7's three cutoff fixtures — post-cutoff prose red, pre-cutoff twin
green, blank key off — all run against the unpatched checker first · `FLOOR_ASSERTIONS` 12 → 18.

This unit adds no leg. S7's verdict lands in `spec tokens (a spec's own names resolve)` and its test
arms in `spec-tokens self-test`, both already in `tools/gate-legs.json`, so the manifest does not
move. The self-test leg carries `subject: kit` and the guard `tools/`, so the default bar holds it —
this is kit work and its DoD owes
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
  - RESOLVED (owner, 2026-09-05): branch A — a live spec dated at or after `SPEC_LEGLINE_CUTOFF`
    whose §7 contributes no leg name becomes a hit. Branch B loses and its text stays as the record
    of what was weighed, including its measured cost. The carrying argument is the recommendation's:
    the failure is SILENCE, which branch B cannot see — 31 of the 42 live specs name no leg at all at
    the fold. The cutoff takes this build's own ruling, `SPEC_LEGLINE_CUTOFF="2026-09-06"`, strictly
    past the newest spec filename date on any branch, so the 31 stay green and the arm grades nothing
    on day one. Folded into S1, S2, S5, the new S7, §3's first non-goal, §4's cutoff section, §5, AC3,
    AC4, AC8, AC9 and §7's arm line.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · folded the owner's ruling on
  FORK 1: branch A, a dated `SPEC_LEGLINE_CUTOFF="2026-09-06"` under which a §7 naming no leg reds.
  Added S7 and AC8–AC9, inverted §3's first non-goal, re-measured §4's population at the fold
  (31 of 42), and corrected §5, §7's arm line and §10, each of which described a checker that could
  not red.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a spec section 7 gate name resolved against the gate
manifest"` ranks `extract_section` in `tools/check-spec-tokens.py` and the `spec-tokens` affordance
seam above everything else, and that is the seam this unit extends: the §7 walk, the `LEG_LINE`
predicate and the report line all already exist in that file, so S4 is two hunks inside a loop rather
than a new module. No second checker is built. S7 does need a conf value, and the ranked alternative
seam — `tools/drift-audit/drift_report.py`'s `load_conf` — is deliberately NOT copied: that function
exists in three near-identical versions already, its own docstring records two silent divergences
that took two years to find, and this unit reads ONE key whose only legal values are a date or the
empty string. A regex for that key is smaller than the copy and cannot drift from a parser it never
claims to match. The cutoff itself is reused rather than derived: it is the build-wide date
`TOOL-aJoinedCanon-1`'s fold measured. The template half reuses the `## §10 Reuse audit` explainer's
own placement rule rather than inventing a second convention for instructional prose.

Recall terms used: `python tools/memory-recall/query.py "why does the spec format never state the
shape that makes its section 7 gate names resolvable" --terms "spec tokens leg line gate manifest
section 7 prose opt-out check-spec-tokens LEG_LINE gate-legs.json template skeleton cutoff"`. It
returned the finding itself, `TEMPLATE-SPEC.md`'s §10 explainer as the placement precedent, the
`spec-tokens` dossier's affordance list, and `TOOL-dTieredTribunal-6`, whose §7 text arm folded for
the same reason this unit exists.
