---
slug: dScriptedRepeat
node: d
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-dScriptedRepeat-1 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11
---

# dScriptedRepeat — playbook mode: a third authorization discipline for repeatable content

Node `d` · opened 2026-08-20 · streams tooling.

**The owner's ask, verbatim.** A new feature is required for the unattended kit: Playbook mode. It
creates fully-functional playbooks — a detailed checklist of instructions and steps to create
repeating content (plans, images, videos, articles, web-pages, websites, tests). It updates and
tweaks existing playbooks to improve their performance, from owner instruction or from detail
discovered during builds. It follows those playbooks to the letter to create the number of content
pieces the owner needs. It accepts either plain language or a playbook, plus how many pieces and
where they go; with no playbook it researches the topic and the code it must relate to, then specs
and creates a new checklist playbook from a PLAYBOOK TEMPLATE — a template itself researched, tested
and thoroughly reviewed for a format that excludes ambiguity and promotes instruction efficiency.
With a playbook present it is followed to the letter. Improvements surfaced during builds are logged
and put to the owner. The mode is for these cases and **refuses ordinary code builds**. Reference
playbooks live in another repo: `content-plan/PLAYBOOK.md` and `brand/art-style/HYBRID-PLAYBOOK.md`
in `nicocares`.

**This session's deliverable is not the implementation.** It is: ground in the existing kit,
adversarially research the options, recommend, then design, spec and adversarially review the spec
set. Building is a later authorization.

## What the grounding found

**The mode mechanism already exists and is gated.** `TOOL-aPromptedMandate-1` put an
`authorized-by:` key in the build README's front matter, read at the pinned BASE, recorded as `mode:`
in Run facts, over a CLOSED set the driver refuses to default outside of. `TOOL-aPromptedMandate-4`
then made directives SCOPE-TAGGED — `<handle>:<section>[:<scope>]`, absent field meaning `all` — with
`researched:M12:prompt` and `solution-tested:M12:prompt` as the first two scoped members, and a
driver refusal when a waiver names a handle out of scope. Playbook mode is a third member of that
closed set plus its own scoped directives. No authorization primitive is invented.

**What is portable, and what is not.** Portable: the mode declaration and its closed-set refusal, the
scoped-directive layer, `PHASES_CORE` as the phase vocabulary, the `--park` register and its
`parked-decisions-surfaced` DoD item, the run-state generated/authored split, and M12's
research→test→choose loop, which is exactly what "no playbook exists yet, do research" describes. Not
portable: the DoD item `build-complete`, which reads the units table and therefore counts units, not
pieces.

**The reference playbooks are two different shapes and both are evidence.** `PLAYBOOK.md` is a step
checklist where every step carries `GATE <leg>` or `CHECK <why>`, with its own I21 invariant redding a
step that is untagged or names no runnable leg. `HYBRID-PLAYBOOK.md` is a recipe: an exact parameter
table, a prompt scaffold with named slots, hard rules each traced to an owner correction, an
accepted-instance library, a "what was ruled out — don't re-try" section, and a dated bake-off marked
don't-redo. The GATE/CHECK tagging is the same discipline this repo already states as a rule (a gate's
own header names what it does not check; a skip must announce itself), which is why it is the
template's spine rather than an import. Every count over either file is DERIVED by the research
records under `build/`, never restated here — the first draft of this paragraph carried three and one
of them was already wrong.

## The seven forks, resolved at kickoff

The owner answered all seven before any design work. Recorded here because they are older than the
spec set and every spec is measured against them.

| # | Fork | Ruling |
|---|---|---|
| 1 | Home and coupling | **Third mode PLUS an attended path.** `authorized-by: playbook` joins the closed set; a second entry point runs the same checklist discipline with an owner in the loop, no anchor and no push mandate. Two entry points, ONE playbook artifact and ONE gate. |
| 2 | "Refuses normal builds" | **Gate the paths, document the judgment.** The playbook declares OUTPUT PATHS and a machine check reds a playbook-mode diff touching anything outside them plus its own records; the class that gate cannot see — a code change landing inside a declared output path — is a stated CHECK. |
| 3 | N pieces vs. the spec set | **The playbook is the spec; pieces are passes.** One unit per playbook RUN, never one per piece. Each piece is a pass with its own commit and reground point. The DoD must count pieces against the requested N rather than counting units. |
| 4 | Template evidence base | **Corpus-derived plus external research.** Derive from the two reference playbooks, this repo's spec template, hygiene grammar and GATE/CHECK philosophy; challenge that shape against external checklist and instruction-design literature; then freeze it and mark it human-curated. |
| 5 | When is a piece done | **The playbook declares its own GATE legs.** A playbook is VALID only if every step is tagged `GATE <leg>` or `CHECK <why>` and every named leg is runnable; piece-done is its declared legs green. This forces the adopting repo to own a checker, and that cost is the point. |
| 6 | The improvement loop | **A separate register, surfaced at close.** A proposal is not a park: a park is what a run refused to decide and blocks the close, a proposal comes from work that succeeded and must not. Distinct verb, distinct region, distinct DoD treatment. |
| 7 | Producer knowledge | **Agnostic — the playbook carries it.** The kit knows paths, counts, steps, gates and status. How a piece is produced is playbook prose. The kit grows no dependency on any generator. |

## Constraints already measured

Two budgets are nearly spent and both bind this build's design, and neither figure is written here —
read `bash tools/check-template-size.sh` and `python tools/memory-tree/corpus_ids.py --report` for the
live pair. `memory/guides/BUILD-METHOD.md` is close enough to its stated 22 KB / 290 lines that a new
method section is an owner call rather than an edit, exactly as M12's own budget rise was. The corpus
READ PATH is the tighter of the two, and the research measured its warning coming true before a design
byte was spent: opening this build rendered a row into the generated `memory/LIVE.md`, which is itself
on the read path, and that row alone cost 94 B. Externalizing is preferred to spending either, and
raising the ceiling is a fork for the owner rather than an edit.

## What the research changed

Six records under `build/` — five independent lenses and one contradiction hunt that cross-checked
them against source. Read the hunt first: it refuted four recommendations, found thirteen cites that
do not resolve, and ranked twelve decisions still open.

Three findings changed the design rather than confirming it. **Fork 6's stated premise is false** — a
park does not block the close, `park()` already writes four kinds through one region, and the
asymmetry the fork asked for already held, so the ruling buys a fifth KIND at a tenth of the cost.
**Fork 5 is the most damaged**: the reference the template derives from contains four measured
instances of fork 5's own defect, and the two references disagree on what a "step" is. **The sharpest
finding is in no fork at all** — every composition failure in the reference corpus was found by
measuring the SET, never a piece, so a Definition of Done that counts pieces and finds each piece's
legs green ships N monocultured pieces and reports GREEN. That is unit 7.

## The four forks the research opened, ruled 2026-08-20

The seven kickoff forks were ruled before evidence. These four were ruled after it, and each
overturns or completes something the first seven left wrong or unsaid.

**Fork 8 — where `outputs:` and `pieces:` are declared: the hybrid nobody had priced.** The build
README's front matter at BASE names the PLAYBOOK PATH; the gate takes a second `GIT show` of that path
at BASE and reads the globs from the playbook. The driver's `No second GIT show: one blob, one parse`
rule bounds ONE front-matter scan and does not forbid reading a second file. This is the only option
that keeps the playbook self-describing across runs, which is the mode's whole premise.

**Fork 9 — what fork 1's "ONE gate" means for the attended half: the per-piece record is a property of
the TREE.** Tracked, hash-joined to the piece, readable by a merge-bar leg with no run-state file in
sight. Both entry points then emit one evidence shape and "ONE gate" is literally true. The research
proved an attended run cannot close through the driver at all, so the alternative was an honour system
over half the surface.

**Fork 10 — the mode owns SET-scoped checks.** A playbook declares two check populations: per-piece,
and set-scoped over all N at close. Without the second, a Definition of Done that counts pieces and
finds each piece's legs green ships N monocultured pieces and reports GREEN.

**Fork 11 — the CHECK grammar is validated-when-present, with a drain census.** A `CHECK` may carry
`· witness <field>`; the gate validates every one present and REPORTS the drain rather than redding.
Measured precedent decides it: the soft rule drained voluntarily in 15 of 33 cases here, the
hard-equality canon in 0 of 11 — and hard equality FORBIDS a grandfathered file from conforming early,
which is a wall in front of the mode's second verb.

## The three owner rulings of 2026-08-20, after the audit

**The mode value is `recipe`, and the artifact stays a playbook.** `playbook` collided with the
`DISCIPLINES` enum, the `PLAY` family and the charter-renderer kit. None was a machine collision and
all four subjects answered one grep. The mode names the authorization DISCIPLINE, exactly as `slug` and
`prompt` do without naming any artifact; the playbook names the DOCUMENT. Unit 1 S3b states that once
so the pair is not read as drift.

**`READ_PATH_CEILING` rises 112987 to 131892**, which is 106292 measured plus the same 25,600 headroom
every movement uses. The previous allowance is spent — it was consumed from 87387 to 106292, leaving
6,695 — and this build owes a protocol mode row, two Definition-of-Done table rows, a parked-kind row
and eleven units' worth of decision appends. Measured BEFORE this build spent any of it, which is
stricter than the convention rather than looser, and the conf comment says so and tells whoever merges
to re-derive.

**The playbook directives point at existing build-method sections.** `BUILD-METHOD.md` does not move
and its stated budget does not rise, so the mode adds nothing to a document M7 re-reads whole at every
pass boundary. The accepted cost is that "follow a playbook to the letter" is described by the pass
loop and the wrap-up derivation rather than by prose written for it.

## The unit set

One mechanism each, per the build method's M2, and every one is Tier 2 — this is a kit contract change
throughout, which the manifest's tier rule makes Tier 2 by definition. The unit COUNT is not written
here: the generated region below derives it, and a prose count beside a table that grew is the class
this repo bans. Unit 9 carried a Tier-1 stamp until the round-2 audit observed that it adds a new write
path and changes a shared row grammar, which is Tier 2 by the charter's own first bullet.

The ORDER matters, is not the id order, and is stated as a PREDECESSOR list because the previous prose
version contradicted four dependencies the specs themselves assert. Units 5, 7 and 8 all deliver their
acceptance through `check-playbook.sh`, which unit 3 creates, so 3 cannot run parallel to them; and
every one of 5, 6, 7 and 8 reads a value unit 4's seam resolves.

| Unit | Must land after |
|---|---|
| 1 | — |
| 2 | 1 |
| 3 | 1, 2 |
| 4 | 1 |
| 5 | 3, 4 |
| 6 | 4, 5 · CO-LANDS with 8 |
| 7 | 4, 5 · CO-LANDS with 6 |
| 8 | 3, 4 · CO-LANDS with 6 |
| 9 | 1 |
| 10 | all of 1-9, 11 |
| 11 | 2, 3 · and its EXISTENCE is parked for the owner |

Two co-landing constraints, both from the specs' own reasoning. Units 6 and 8 land together because 6's
piece count consumes 8's diff population and counts the wrong thing without it. Units 6 and 7 land
together because `CORE_FLOOR`'s Definition-of-Done half moves ONCE, from eight to ten, rather than
twice — the two specs previously carried two different stories about which commit moves it.

## What the spec audit changed

The ten specs went through an M4 adversarial audit at base `7e2ac32f` — five lenses, batched refuting
skeptics, one synthesis. It returned **BLOCKED**: 24 confirmed against 31 refuted, collapsing to 21
distinct defects, fifteen of them HIGH. The record is under `reviews/`. All 21 are folded and every
spec that moved carries its rev-2 log.

**The blocker was mine and it reached runs that have nothing to do with this mode.** `verb_close`
evaluates `DOD_CORE` for EVERY run with no mode branch anywhere, so the two new core items — which only
a playbook run can satisfy — would have blocked `--close` on every `slug`- and `prompt`-mode run in the
fleet, on a non-overridable item whose only exit is `--abort`. Units 6 and 7 now carry a term zero that
meets the item and ANNOUNCES the skip when the mode does not match.

**Four artifacts had readers and no writer.** Nothing in the ten units wrote the per-piece record or
the set record, so the two Definition-of-Done items reading them could only be satisfied by hand — which
unit 5 forbids. Unit 5 now owns the writer verb and a second caller for the attended path.

**Two items were satisfied by recorded failures.** `verified` was a hash-join state alone, so
`pieces-complete` was met by N pieces whose every declared leg had FAILED, and fork 5 was implemented by
nothing. `set-checks-recorded` asserted a verdict existed and not what it said, so the unit built to
stop a monoculture green closed green on a failed set check. Both now read the verdicts.

**The owner's first stated verb had no owning unit.** Creating a playbook when none exists was in the
ask and absent from the roster, and unit 4's preflight structurally refuses a run with no playbook to
name. That is unit 11, and it also takes amendment — which removes the playbook from unit 8's exemption
set, where it sat on a premise unit 9 denied in the same build.

**And the audit re-measured my own repair and found it worse than what it replaced.** Unit 8's diff
population was "enumerate the run's own commits"; measured, that is a SUPERSET of the `BASE..HEAD` range
it rejects, because the merged-in default-branch history is still in `rev-list`. The population is now
the research's own merge-base-plus-first-parent form.

<!-- roster:units -->
| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dScriptedRepeat-1` | 2 | `AUTH_MODES` published as a driver constant, the third mode member, the directive scope set's third value, and the membership branch check 19 does not have |
| 2 | `TOOL-dScriptedRepeat-2` | 2 | the PLAYBOOK TEMPLATE — derived from the corpus and the literature, frozen, marked human-curated, with a section canon and a DERIVED per-segment length budget |
| 3 | `TOOL-dScriptedRepeat-3` | 2 | the playbook VALIDITY gate — the declared step selector and its shrink-only floor, the GATE/CHECK tag grammar, the witness drain census, and the leg-runnability oracle with a declared coverage mode and a named refusal |
| 4 | `TOOL-dScriptedRepeat-4` | 2 | the declaration seam — the README names the playbook path at BASE, the gate reads `outputs:`, `pieces:` and the piece GRAIN from the playbook at BASE |
| 5 | `TOOL-dScriptedRepeat-5` | 2 | the per-piece record as a TREE property — tracked, hash-joined to the piece, readable with no run-state file |
| 6 | `TOOL-dScriptedRepeat-6` | 2 | `pieces-complete` — a ninth CORE DoD item, its vacuity guard, its grain, and whether it may be overridden |
| 7 | `TOOL-dScriptedRepeat-7` | 2 | the SET-scoped check population and where it runs |
| 8 | `TOOL-dScriptedRepeat-8` | 2 | the output-scope refusal — the diff population, the exemption set, an observed failing case, and the stated CHECK half |
| 9 | `TOOL-dScriptedRepeat-9` | 1 | the `proposal` park kind and the `--propose` verb |
| 10 | `TOOL-dScriptedRepeat-10` | 2 | the Skill's start paths and the playbook-scoped directives |
| 11 | `TOOL-dScriptedRepeat-11` | 2 | authoring a playbook — the creation path, and where amendment lives |
<!-- /roster:units -->

## What is deliberately NOT in this build

Named here because the research raised each one and an unstated exclusion reads as an oversight.

- **No change to `check_authorization`, `resolve_base` or the anchor observation.** The precedent
  build established that a mode is a RECORD rather than a verdict, and nothing here needs the
  authorization to move. Repeating that finding is cheaper than re-deriving it.
- **No content producers.** Fork 7 holds and the research agreed three ways, with one clarification
  worth stating in the spec: the KIT is agnostic, the ADOPTER's checker is not and must not be.
- **No migration of the reference playbooks.** They live in another repo and are somebody's
  production artifacts. Fork 11's soft grammar exists so this build does not require one.
- **The drift the research found in the kit's own records is filed, not fixed here** — the verb set
  spelled in five places with three stale, a gate docstring stating a count of a derived population,
  and an installed conf the bar reads but no arm grades.


<!-- gen:build-index -->
**Build status:** INPROGRESS · 11 unit(s) · node d · opened 2026-08-20 · streams tooling
ids TOOL-dScriptedRepeat-1 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dScriptedRepeat-1 — the mode vocabulary, published and joined](spec/2026-08-20-spec-dScriptedRepeat-1.md) | INPROGRESS | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-10 — the two start paths and the playbook-scoped directives](spec/2026-08-20-spec-dScriptedRepeat-10.md) | SPECCED | rev-4 | 2026-08-20 |
| [TOOL-dScriptedRepeat-11 — authoring a playbook: creation, and owner-instructed amendment](spec/2026-08-20-spec-dScriptedRepeat-11.md) | SPECCED | rev-4 | 2026-08-20 |
| [TOOL-dScriptedRepeat-2 — the PLAYBOOK TEMPLATE, derived then frozen](spec/2026-08-20-spec-dScriptedRepeat-2.md) | INPROGRESS | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-3 — the playbook validity gate](spec/2026-08-20-spec-dScriptedRepeat-3.md) | SPECCED | rev-4 | 2026-08-20 |
| [TOOL-dScriptedRepeat-4 — the declaration seam: README names the path, playbook holds the globs](spec/2026-08-20-spec-dScriptedRepeat-4.md) | SPECCED | rev-4 | 2026-08-20 |
| [TOOL-dScriptedRepeat-5 — the per-piece record: its writer, its reader, and its states](spec/2026-08-20-spec-dScriptedRepeat-5.md) | SPECCED | rev-4 | 2026-08-20 |
| [TOOL-dScriptedRepeat-6 — `pieces-complete`, the ninth core Definition-of-Done item](spec/2026-08-20-spec-dScriptedRepeat-6.md) | SPECCED | rev-5 | 2026-08-20 |
| [TOOL-dScriptedRepeat-7 — SET-scoped checks, and where they run](spec/2026-08-20-spec-dScriptedRepeat-7.md) | SPECCED | rev-5 | 2026-08-20 |
| [TOOL-dScriptedRepeat-8 — the output-scope refusal, and what it cannot see](spec/2026-08-20-spec-dScriptedRepeat-8.md) | SPECCED | rev-5 | 2026-08-20 |
| [TOOL-dScriptedRepeat-9 — the `proposal` park kind and the `--propose` verb](spec/2026-08-20-spec-dScriptedRepeat-9.md) | SPECCED | rev-3 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md](build/2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md) | research | TOOL-dScriptedRepeat-2 |
| [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md) | spec-audit | TOOL-dScriptedRepeat-1 |
| [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md) | spec-audit | TOOL-dScriptedRepeat-1 |

Ids no record names: TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9.

Ids no `spec-audit` record has ever named: TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-dScriptedRepeat-1.md](spec/2026-08-20-spec-dScriptedRepeat-1.md)
  - [2026-08-20-spec-dScriptedRepeat-10.md](spec/2026-08-20-spec-dScriptedRepeat-10.md)
  - [2026-08-20-spec-dScriptedRepeat-11.md](spec/2026-08-20-spec-dScriptedRepeat-11.md)
  - [2026-08-20-spec-dScriptedRepeat-2.md](spec/2026-08-20-spec-dScriptedRepeat-2.md)
  - [2026-08-20-spec-dScriptedRepeat-3.md](spec/2026-08-20-spec-dScriptedRepeat-3.md)
  - [2026-08-20-spec-dScriptedRepeat-4.md](spec/2026-08-20-spec-dScriptedRepeat-4.md)
  - [2026-08-20-spec-dScriptedRepeat-5.md](spec/2026-08-20-spec-dScriptedRepeat-5.md)
  - [2026-08-20-spec-dScriptedRepeat-6.md](spec/2026-08-20-spec-dScriptedRepeat-6.md)
  - [2026-08-20-spec-dScriptedRepeat-7.md](spec/2026-08-20-spec-dScriptedRepeat-7.md)
  - [2026-08-20-spec-dScriptedRepeat-8.md](spec/2026-08-20-spec-dScriptedRepeat-8.md)
  - [2026-08-20-spec-dScriptedRepeat-9.md](spec/2026-08-20-spec-dScriptedRepeat-9.md)
- **`build/`**
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md)
  - [2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md](build/2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md)
- **`reviews/`**
  - [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md)
  - [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md)
<!-- /gen:build-docs -->
