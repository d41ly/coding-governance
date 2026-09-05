# TOOL-aJoinedCanon-7 — section 7 states the shape its join reads, and names where a new arm lives

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 7 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` resolves a §7 gate name against `tools/gate-legs.json` only when the
names sit on a line that is nothing but backticked tokens, and `memory/TEMPLATE-SPEC.md` never says
so — an author who writes §7 as prose opts out of the only check on it and is never told. This unit
makes §7 state its own shape, adds the one field §7 has never asked for (where a new gate's arm
lands), makes the checker report how much of the live corpus its leg join is not grading, and — per
the owner's ruling on §8 — turns that silence into a hit for any spec written from the cutoff date on.
Because that turns a silent read into a verdict, it also moves the read off the section ORDINAL and
onto the Gates heading TEXT: a Tier-1 spec written under the light profile must not be the first
thing this arm reds.

## 2. Scope (IN)

- **S1** — A new explainer section in `tools/memory-tree/SPEC-TEMPLATE.template.md`, placed
  immediately above the existing explainer whose heading reads
  `## §10 Reuse audit — the two facts, and what satisfies each`, stating: the leg names go
  on a line of their own carrying nothing but backticked names and `·`/`,` separators; a line with a
  `- ` bullet marker, a prose prefix or a trailing clause is not read; prose may sit above or below
  that line freely; only a non-terminal spec is graded at all; the section is found by its HEADING
  TEXT and not by its number, so a spec that carries no Gates heading at all is not graded and a
  Gates section at another ordinal still is; and — the half the fork's resolution
  adds — a spec whose FILENAME date is at or after `SPEC_LEGLINE_CUTOFF` and which DOES carry a Gates
  heading must carry such a line, so from that date the shape is a requirement and not only a reading
  rule. The anchor is cited by heading text rather than by line, per the build rule — every unit at a
  lower `order` that lists this file edits it first, and §5's risks row says how that set is derived.
- **S2** — The skeleton's `## 7. Gates` body — one sentence today, reading `The named gate legs this
  unit must keep green, plus any new gate it adds.` — replaces it with the list-line instruction
  stated as a REQUIREMENT, a pointer to the S1
  section, and the arm-home line of S3. It stays short enough to be copied without being read as an
  essay, per the §10 precedent that instructional bodies live above the skeleton and not inside it.
  An author copying the skeleton after the cutoff is the only reader the S7 arm can still surprise,
  so the demand is stated where they are, not only where it is explained.
- **S3** — The arm-home line, defined in S1 and prompted by S2: when a unit adds or moves a gate arm,
  §7 carries one line per arm reading `New arm: <suite path> · <what stages its failing case> ·
  <assertion floor to move, or none>`. It is prose, it is not machine-graded, and S1 says so in the
  same breath as it defines it — including that it never satisfies S7: the prose prefix is exactly
  what keeps it out of the leg join, so a §7 carrying only an arm-home line still names no leg.
- **S4** — `tools/check-spec-tokens.py` gains three behaviours. The §7 body is located by HEADING
  TEXT (`^## [0-9]+\. Gates`) rather than by the ordinal `extract_section(text, 7)` passes today, so
  a Tier-1 spec written under the light profile is graded on the section it actually has and not on
  whatever sits seventh. A token that IS a manifest name is
  resolved BEFORE the `NOT_A_LEG` shape exclusions, so a manifest name excluded by shape — one
  carrying a `/`, and one whose first word is a command verb — stops being discarded
  unread. And the run report gains the ungraded population: how many live specs contributed no leg
  name to the join at all, and — as a separate field, because the two silences have different
  remedies — how many carry no Gates heading to grade.
- **S5** — `tools/check-spec-tokens.test.sh` gains eight arms, each named by a criterion below:
  AC4's prose §7 raising the ungraded count; AC5's and AC10's two excluded-name classes; AC8's
  post-cutoff red and its pre-cutoff twin; AC9's blank key; and AC11's two Tier-1 fixtures — one
  with no Gates heading, which stays silent, one whose Gates section sits at another ordinal, which
  is graded there. Each is observed RED against the unpatched checker first, and `FLOOR_ASSERTIONS`
  moves with them.
- **S6** — `memory/map/features/spec-tokens.md` records the two new report fields, the heading-text
  location, the S7 arm and its conf key, and the three limits the checker still has — a misspelled
  shape-excluded name is still skipped, the §6 witness walk still keys on its ordinal, and a spec
  that omits its Gates section is silent by design — so the dossier does not describe a checker that
  no longer exists.
- **S7** — The dated demand, which is the owner's ruling on §8's fork. `.memory-tree.conf` declares
  `SPEC_LEGLINE_CUTOFF="2026-09-06"`; `tools/check-spec-tokens.py` reads that one key; a live spec
  whose filename date is at or after it, which CARRIES a Gates heading, and whose Gates section
  contributes no graded leg name becomes a hit. The Gates-heading precondition is the whole of the
  Tier-1 accommodation and it is S4's heading-text location doing the work: under the light profile a
  spec may legally omit the section, and a spec that omits it is silent rather than red, so the only
  spec this arm can red is one that wrote a Gates section and named no leg in it.
  The hit's token is the spec's own path, so the existing waiver registry can hold it and the
  stale-waiver refusal keeps a cleared one from surviving. A blank or absent key turns the arm off,
  and the report line says which. Four test arms: the post-cutoff red, its pre-cutoff twin green,
  the blank-key off, and AC11's post-cutoff Tier-1 spec with no Gates heading staying silent.

## 3. Non-goals (OUT)

- **Redding a §7 that names no leg BEFORE the cutoff.** S7 grades a spec dated at or after
  `SPEC_LEGLINE_CUTOFF` and nothing earlier. Every live spec that contributes no graded leg name
  today predates it and stays green — the population is §4's derived figure, not a number kept fresh
  here; redding honest content written before the rule existed is
  what the dated key exists to prevent.
- **Redding a spec that carries no Gates section at all.** `memory/TEMPLATE-SPEC.md` states the
  Tier-1 light profile plainly — the nine-section canon is not enforced, write the few sections that
  matter — and ten terminal specs in this corpus already carry no `## N. Gates` heading, derived by
  `grep -L` for that heading over the spec glob and counted, never quoted from here. A check that reds one of those reds a
  spec that is legal under the format it enforces, which is the class
  `check-memory-hygiene.sh`'s check 12 records in its own header and which sibling unit 3's S5 pins
  deliberately. S7 fires only on a spec that HAS the section, and S4's heading-text location is what
  makes that distinguishable at all.
- **Re-keying the §6 witness walk off its ordinal.** S4 moves the §7 half only. A Tier-1 spec that
  puts Gates at §6 still has its Gates body read as §6 witness paths, which is a pre-existing limit
  of the §6 walk and not one S7 creates; it is recorded as a surviving limit under S6 rather than
  fixed here, because the §6 population belongs to sibling unit 3.
- **Widening `LEG_LINE` to read prose lines.** The fork's losing
  branch (§8). Its cost is recorded in the checker's own header: treating every backticked §7 token
  as a leg name produced 270 hits, 271 of them from prose in one spec.
- **Retrofitting the corpus.** 448 terminal specs are frozen records and are not graded; the 34
  near-miss §7 spellings the research counted stay as they are. Nothing in this unit edits a landed
  spec.
- **Closing the misspelling hole for a shape-excluded leg name.** S4 grades such a name when it
  resolves against the manifest; a MISSPELLING of one is still skipped by whichever `NOT_A_LEG`
  alternative caught it, because redding a near-miss with a `/` would red every honest file path on a
  list line, and redding one with a leading command verb would red every honest command. Stated as a
  limit in S6, not fixed here.
- **Naming the checker's path inside the shipped template half.** See §4's rejected alternatives —
  it would ship an adopter a dead repo-path citation.
- **Grading whether a declared arm home is real.** The named suite usually does not exist yet when
  the spec is written; a resolver would red every honest spec.

## 4. Design

### What the join reads today, measured at writing time

`python tools/check-spec-tokens.py` printed, on this tree at `750ca0ca`:

```
spec-tokens: 33 live spec(s) · 448 terminal spec(s) not graded · 769 token(s) graded ·
274 citation(s) skipped (untracked path) · 23 waiver(s)
```

That is the design pass's transcript and every number in it has already moved — run the command, do
not read this block as current. It is kept for its SHAPE: the report line S4 extends is that line,
and the ungraded population becomes one more field on it.

Exit 0. Of the graded tokens, the §7 leg names are a minority; the rest are §6 witness paths and
`path:line` citations. The join fires only inside `LEG_LINE`, only on specs `LIVE` matches, and each
token must survive `NOT_A_LEG` — all three predicates named by their constants, because
`tools/check-spec-tokens.py` is this unit's own write set and its line numbers move under it.

Every figure below is DERIVED, and the deriving command is written beside it rather than the value
being trusted from here. Re-derive them at the start of this unit's build pass; the design depends on
which of them is true, not on the digits.

- **26 of the 42 live specs carry no `LEG_LINE` at all**, and **31 of the 42 contribute no graded leg
  token** — the five between them have a list line whose every token is excluded by shape. Derived by
  running `LIVE`, the Gates-heading regex, `LEG_LINE` and `NOT_A_LEG` over the tracked spec glob, which is
  what S4's new report field turns into a printed number so this stops being a research pass.
- **Nine of the eleven `aJoinedCanon` specs contribute zero.** They were written by agents who
  had each read the finding that says §7 is silently ungraded, and the house style most of them used —
  `- ` bulleted leg names — is precisely the shape `LEG_LINE` cannot match. That is
  the evidence that this is a discoverability defect and not an attention defect. The two exceptions
  are this unit, which is about the defect, and unit 9.
- **The figures moved with the corpus and not with the predicate.** The findings record's
  post-skeptic number was 18 of 31; the design pass measured 20 of 33; the fold measures 26 of 42.
  `750ca0ca` names the tree the design READ, not the tree as committed. The ratio held while the
  corpus grew by eleven specs in a day, which is the argument for a cutoff over a retrofit: the
  population S7 would have to red is not shrinking on its own.
- **Every live spec today carries its Gates section at `## 7.`, and ten terminal specs carry no Gates
  heading at all.** So the heading-text location S4 adds changes no verdict on the corpus as it
  stands, and buys exactly the Tier-1 headroom §3's first non-goal is written around.

Two of the 93 manifest names are discarded by `NOT_A_LEG` before they can resolve, and by two
DIFFERENT alternatives — which is why S4's resolve-first change needs a criterion per class rather
than one. Exactly ONE name contains a `/`: `kit/dogfood doc parity`, cited on a matching list line by
two live specs. The other, `python resolver (behaviour + inline parity + idiom ban)`, is caught by
`NOT_A_LEG`'s `^python3? ` command-verb alternative and never touches the path alternative at all; it
is cited on a matching list line by one live spec. Both counts derive from the same run as the
figures above.

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

Three edits inside the existing per-spec walk over `specs`:

1. Locate by heading TEXT. The §7 read is `extract_section(text, 7)` today, whose `SEC` template
   interpolates the ORDINAL, so a section that is not seventh is invisible and an absent one returns
   `""` — indistinguishable, in S7's eyes, from a Gates section that named no leg. That is the whole
   defect: `memory/TEMPLATE-SPEC.md`'s Tier-1 light profile lets a spec write only the sections that
   matter, so the first post-cutoff Tier-1 spec would red with no remedy but a per-path waiver. The
   Gates body is instead matched by `^## [0-9]+\. Gates`, and whether the heading was FOUND is
   returned alongside the body, because S7 must tell "no Gates section" from "a Gates section naming
   nothing". The regex is not invented here — it is check 12's acceptance-witness regex with one word
   changed, tab class and all, so the two checkers cannot drift on what a heading looks like.
2. Resolve first. `if tok in legs` is tested before `NOT_A_TOKEN`/`NOT_A_LEG`, so a name that IS in
   the manifest counts as graded whatever its shape. This can never turn a green tree red: the hit
   list is only reachable from the else branch, which is unchanged. Simulated over the live specs at
   the fold, it grades three tokens that are discarded today — two citations of the slash-carrying
   name and one of the command-verb name — and moves no hit.
3. Report the ungraded population, one more field on the line the tool already prints. It exists
   because this repo's rule is that a skip announces itself, which the same report line already does
   for the skipped citations. Below the cutoff it stays a COUNT and not a verdict, so no landed
   spec goes red; at and above the cutoff the same silence is S7's hit. Specs with no Gates heading
   are counted in their own field rather than folded into the ungraded number, because those two
   silences have different remedies and one report field cannot say which you have.

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

**The key is deliberately absent from `tools/memory-tree/.memory-tree.conf.example`, and this is the
build's cutoff rule taking its one declared exception.** The rule exists because a key the adopter's
engine READS and their conf never declares leaves them a dead arm reading as armed. Neither half of
that reaches here, and both halves are checkable at source rather than argued. The example's parity
arms derive their population from `check-memory-hygiene.sh` itself — the arm builds `_engpresets` by
grepping the comment-stripped ENGINE for `*_CUTOFF=` and `_engreads` for its `${NAME:-}` reads — so a
key no engine line mentions is not in the population and the arm stays green either way. And the
consumer, `tools/check-spec-tokens.py`, ships to no adopter at all: `tools/govkit/registry.toml`
carries a tracked `[[exempt]]` row for it whose stated reason is that it grades gov's OWN corpus
against gov's OWN manifest and is "Prescribed for copy nowhere." Shipping the key would therefore
hand an adopter a knob no tool of theirs reads, which is the same defect inverted, and the same one
as naming the checker's path in the shipped template below. If this unit ever moves the arm into the
engine, the exception dies with it and the key owes both carriers.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the S1 section, and the S2 skeleton body |
| `memory/TEMPLATE-SPEC.md` | RENDERED, never hand-edited — see below |
| `tools/check-spec-tokens.py` | the heading-text location, resolve-first, the conf read and S7's arm, two report fields |
| `.memory-tree.conf` | the `SPEC_LEGLINE_CUTOFF` key and its comment |
| `tools/check-spec-tokens.test.sh` | eight arms and the floor |
| `memory/map/features/spec-tokens.md` | the two new fields, the heading-text location, the S7 arm and its key, and the three limits |

The two template halves are one edit and the direction is fixed: edit
`tools/memory-tree/SPEC-TEMPLATE.template.md`, then run
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which rewrites `memory/TEMPLATE-SPEC.md`
from it. Hand-editing the live copy is what the `kit/dogfood doc parity` leg exists to red.

No kit version bump is owed BY THIS UNIT. `tools/memory-tree/check-verdict-epoch.sh` scans the file
its `ENGINE=` line names plus the modules its `DELEGATES=` line lists; a shipped `*.template.md` is
among neither, so a prose edit to the template moves no verdict this gate dates. `kit version
markers` asserts an INVARIANT and not a value — each template's `gov:kit memory-tree@` marker equals
`KIT_MEMORY_TREE_VERSION` — which an unchanged constant satisfies and a bumped one satisfies equally,
provided both carriers move together. No number is pinned here on purpose: several units at a lower
`order` each declare a bump of that constant, so any literal this unit named would be stale before it
ran. Whatever the constant reads when this unit lands, it must be unchanged BY THIS DIFF and equal in
every carrier, the carrier set derived with `grep -rl` rather than listed.

### Alternatives rejected

- **Name `tools/check-spec-tokens.py` in the shipped template.** The checker is in no kit and
  `tools/govkit/registry.toml` exempts it by exact path as gov-specific, so an adopter renders
  `memory/TEMPLATE-SPEC.md` naming a file their tree
  does not have. That copy lives under `MEMORY_ROOT`, which is exactly the corpus the dead-path
  classifier walks, and `tools/memory-tree/kit-dogfood-parity.test.sh` states the rule in its own
  header comment: a
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
- perf / scale: the two counters are integers in a loop that already runs; the ceilings for both legs
  are declared in `tools/gate-legs.json` and are read there rather than quoted here, and a
  scratch-repo arm costs about a second. S7 adds one filename-date comparison per live spec and one
  file read per run; the heading-text match replaces a regex with a regex.
- a11y: N/A — no interface.
- i18n: N/A — no user-facing strings.
- error / empty / loading states: every existing refusal path in the checker (empty spec population,
  unreadable manifest, absent waiver registry) is untouched. S7 adds no fourth refusal: an absent or
  blank `.memory-tree.conf` key turns the arm OFF and says so, because this checker must still run in
  a tree that never adopted the memory-tree kit.
- observability: this IS the observability change — the ungraded population and the no-Gates-heading
  population each become a printed number on every bar run instead of a fact only a research pass
  could find.
- risks: low, and no longer zero — S7 gives this checker its first way to red a spec. The blast
  radius is bounded by the cutoff rather than by argument: no spec in the corpus is dated at or after
  2026-09-06, so day one grades nothing, and the first spec it can red is one written after the rule
  exists and after the skeleton states it. The template edit still adds no requirement a gate reads
  BELOW the cutoff, so no landed spec changes verdict. The real risk is unchanged and is the fold-in
  order: EVERY unit at a lower `order` that lists
  `tools/memory-tree/SPEC-TEMPLATE.template.md` in its own Files-touched table edits it before this
  one does, and on the spec set as it stands that is all five of them. The list is not enumerated
  here — derive it with `grep -l` over the sibling specs at build time, because an enumeration typed
  into this spec was already short by seven units once. Two consequences, both binding: this unit
  re-renders after landing rather than assuming its own copy of the live file, and every anchor it
  cites into that file is a heading or a literal string, never a line number.
- testing + left-shift gates: eight new arms in `tools/check-spec-tokens.test.sh`, each observed RED
  against the unpatched checker before the change lands — including S7's pre-cutoff twin, which must
  be seen to distinguish a cutoff that works from one that never fires, and AC11's Tier-1 fixtures,
  which must be seen to distinguish a heading-text location from the ordinal it replaces. The ungated half — that an
  arm-home line is true — has no arm and no gate; its compensating check is the Tier-2 review, which
  reads §7 against the diff.
- migration / rollback: the checker change is four hunks and reverts cleanly; the template change is
  prose and reverts through `--render`. S7 has a rollback short of a revert, which is why blank means
  off: emptying `SPEC_LEGLINE_CUTOFF` disables the arm without touching code.
- user docs: `memory/map/features/spec-tokens.md` per S6. No `help/` page — this repo ships no
  end-user surface.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-tree/SPEC-TEMPLATE.template.md` carries the new section, `grep -c
  'LEG_LINE\|line of its own'` finds the shape stated there, and `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` exits 0 with `memory/TEMPLATE-SPEC.md` rendered from
  it rather than hand-edited.
- **AC2** — When the body under the `## 7. Gates` heading of
  `tools/memory-tree/SPEC-TEMPLATE.template.md` is read, it
  names the list line and the `New arm:` line, and `bash tools/memory-tree/check-memory-hygiene.sh`
  still exits 0 over the corpus — the body change requires nothing of a landed spec, and every
  landed spec predates `SPEC_LEGLINE_CUTOFF`, which is the reason and not a coincidence.
- **AC3** — When `python tools/check-spec-tokens.py` runs on this tree, its report line names the
  ungraded live-spec population, the no-Gates-heading population and the cutoff in force, and each
  number it prints AGREES with a live re-derivation over the same corpus. Red when the printed figure
  and the re-derivation disagree, or when either field is absent. The figures move with the corpus and
  are therefore evidence and not the pin — 31 of 42 at the fold, 24 of 33 at design time, DERIVED at
  observation time and never compared against either.
- **AC4** — When a scratch spec dated BEFORE the cutoff whose Gates section is prose is added to a
  fixture repo,
  `bash tools/check-spec-tokens.test.sh` shows the ungraded count rise by one and the run still exit
  0 — observed RED first against the unpatched `tools/check-spec-tokens.py`, which prints no such
  field. Below the cutoff the silence is still only counted.
- **AC5** — When a fixture spec's Gates section lists the one manifest name containing a `/`, `bash
  tools/check-spec-tokens.test.sh` observes it graded rather than skipped, and against the unpatched
  checker the same arm fails. This is `NOT_A_LEG`'s path alternative only; its command-verb sibling is
  AC10, because one arm covering both would pass while either half regressed.
- **AC6** — When `bash tools/check-testsuite-counts.sh` runs, `FLOOR_ASSERTIONS` in
  `tools/check-spec-tokens.test.sh` equals the arm total the suite actually executes and the suite
  compares the two, so the eight added arms cannot be stranded silently. The floor's VALUE is derived
  at observation time — the criterion is the equality, and this unit is the only one that moves
  either side of it.
- **AC7** — When `memory/map/features/spec-tokens.md` is read, it names both new report fields, the
  heading-text location, the S7 arm with its conf key, and all three surviving limits of S6, and `bash
  tools/run-gates/run-gates.sh` is green with `GATE_SELFTESTS=1`.
- **AC8** — When a fixture spec dated at or after `SPEC_LEGLINE_CUTOFF` carries a Gates section of
  pure prose,
  `bash tools/check-spec-tokens.test.sh` observes the run exit 1 naming that spec's path, and the
  byte-identical fixture dated one day before the cutoff exits 0. Both arms observed against the
  unpatched checker first, where the post-cutoff one passes — a cutoff arm that has only ever been
  seen red on a fixture no cutoff could spare is an assertion about nothing.
- **AC9** — When `.memory-tree.conf` declares `SPEC_LEGLINE_CUTOFF=""`, or the file is absent
  entirely, `bash tools/check-spec-tokens.test.sh` observes the post-cutoff fixture of AC8 exit 0 and
  the report line say the arm is off, so a disabled demand cannot read as a satisfied one.
- **AC10** — When a fixture spec's Gates section lists the one manifest name whose first word is a
  command verb — the `python resolver …` leg — `bash tools/check-spec-tokens.test.sh` observes it
  graded rather than skipped, and against the unpatched checker the same arm fails. Red when
  resolve-first is wired only ahead of `NOT_A_LEG`'s path alternative, which is the shape the
  spec's own §4 asserted before it was re-derived and found to describe one name, not two.
- **AC11** — When a LIVE Tier-1 fixture spec dated at or after `SPEC_LEGLINE_CUTOFF` carries NO
  `## N. Gates` heading at all, `bash tools/check-spec-tokens.test.sh` observes the run exit 0 and
  that spec named in the no-Gates-heading field rather than in the hits; and when a second fixture
  carries a legal Gates section at a NON-seventh ordinal naming a real leg, the same run observes
  that leg graded. Both arms fail against the unpatched checker, where the first reds a legal Tier-1
  spec and the second grades whatever sits seventh. This is the criterion that keeps S7 off the light
  profile. The class is `TOOL-dTieredTribunal-17`, an OPEN backlog row against a DIFFERENT reader
  (`plan_state` in `tools/unattended/unattended.sh`) that maps spec sections by ordinal and mis-grades
  every Tier-1 spec for it; that row prescribes the same remedy this criterion observes — key on the
  heading title, which is what the titles are for. This unit closes the class in its own checker and
  leaves that row where it is.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` ·
`kit version markers` · `kit/dogfood doc parity`

New arm: `tools/check-spec-tokens.test.sh` · scratch repos staging each of AC4, AC5, AC10, AC8's two
cutoff twins, AC9's blank key and AC11's two Tier-1 fixtures, all run against the unpatched checker
first · `FLOOR_ASSERTIONS` advances by eight, from whatever value the file declares at this unit's
base — no unit but this one writes either side of that equality.

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
- rev-3 · 2026-09-05 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · folded spec-audit round 1: H5 re-keys
  the §7 read off its ordinal onto the `## N. Gates` heading text, so a Tier-1 spec written under the
  light profile is silent instead of red with no remedy (new S4 behaviour, two §3 non-goals, AC11,
  two arms); M3 corrects "two of the 93 names contain a `/`" to one name per exclusion class and
  splits the coverage into AC5 and AC10; M5 replaces the co-editor enumeration in §5's risks row with
  a derived statement and re-anchors every citation into the shared template by heading text rather
  than by line; H2 strips the `2.59` kit-version literal for the invariant it was standing in for.
  Every §4 figure is now DERIVED with its command beside it, and §4's example-conf paragraph names
  the build cutoff rule's one declared exception with the registry row that grounds it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a spec section 7 gate name resolved against the gate
manifest"` ranks `extract_section` in `tools/check-spec-tokens.py` and the `spec-tokens` affordance
seam above everything else, and that is the seam this unit extends: the §7 walk, the `LEG_LINE`
predicate and the report line all already exist in that file, so S4 is three hunks inside a loop rather
than a new module. No second checker is built. The Gates-heading regex is likewise reused rather than
written: `check-memory-hygiene.sh`'s acceptance-witness arm already matches a spec heading by TEXT,
literal-tab character class and all, and S4 copies that spelling with one word changed. Sibling unit
3's S5 copies the same regex for the same reason, so the three sites agree on what a spec heading
looks like by construction and not by three authors happening to write the same pattern. S7 does need a conf value, and the ranked alternative
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
