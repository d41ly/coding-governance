---
slug: dScriptedRepeat
node: d
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-dScriptedRepeat-1 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 TOOL-dScriptedRepeat-12 TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15
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

Ruled at kickoff and unchanged since. The seven rows moved VERBATIM to
[the kickoff fork rulings](build/2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md)
when this file was trimmed to its cap — a ruling is not derivable from the thing it ruled on, so the
rows move rather than compress. Forks 1, 5 and 6 are cited by number further down this document and
resolve there; the trim that wrote this paragraph pointed at a "kickoff record" that did not exist,
which is round 4's MEDIUM 9.

## The owner rulings

Four rounds of them, made 2026-08-20 and 2026-08-21, moved VERBATIM to
[the owner rulings](build/2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md) when this file hit
its cap: the four forks the research opened, the three after the spec audit, the ones after the aborted
run, and the ones after the round-1 diff review. Forks 8 through 11 are defined there; forks 1 through 7
in [the kickoff fork rulings](build/2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md).
Both records spell their fork numbers in prose, so a grep for `fork 5` resolves — the table rows are
verbatim and number their first column bare, which is exactly how four citations went dangling at the
first move of this kind (round 4, MEDIUM 9). There is no gate for this; it is a documented check.

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

**Units 13, 14 and 15 were added after this table and are not in it.** They came out of the round-3
through round-6 folds rather than the original decomposition, each of them a finding the fold could not
close in place: 13 reads the declared bypass flag back out of tracked evidence records, 15 cuts the
kit gate's process spawns and re-declares its ceiling, and 14 adds a drift signal for the class this
paragraph is an instance of. None has a predecessor in 1-11 and none blocks another, so the table
above stays a statement about the original nine plus 10 and 11.

Two co-landing constraints, both from the specs' own reasoning. Units 6 and 8 land together because 6's
piece count consumes 8's diff population and counts the wrong thing without it. Units 6 and 7 land
together because `CORE_FLOOR`'s Definition-of-Done half moves ONCE, from eight to ten, rather than
twice — the two specs previously carried two different stories about which commit moves it.

## What the spec audits changed

Two adversarial rounds, both under `reviews/`. Round 1: BLOCKED, 24 confirmed against 31 refuted, 21
distinct defects. Round 2 over the fold: BLOCKED, 20 against 12, precision up to 0.625, 15 defects.
All 36 folded. Read the records rather than a summary — four are named here only because each was a
defect of MINE the specs would otherwise have shipped.

**The blocker reached past this feature.** `verb_close` evaluates `DOD_CORE` for EVERY run with no
mode branch, so two core items only a playbook run can satisfy would have blocked `--close` on every
`slug`- and `prompt`-mode run in the fleet. Units 6 and 7 carry a term zero now.

**Four artifacts had readers and no writer**, so both items reading them could only be met by hand,
which unit 5 forbids. **Two items were satisfied by recorded FAILURES** — `verified` was a hash-join
state alone, and `set-checks-recorded` asserted a verdict existed rather than what it said, so the
unit built to stop a monoculture green closed green on a failed set check. **And my own
diff-population repair measured worse than what it replaced**: enumerating a run's commits is a
superset of the `BASE..HEAD` range it rejects, because merged-in history is still in `rev-list`.

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
**Build status:** SPECCED · 14 unit(s) · node d · opened 2026-08-20 · streams tooling
ids TOOL-dScriptedRepeat-1 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 TOOL-dScriptedRepeat-12
ids TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dScriptedRepeat-1 — the mode vocabulary, published and joined](spec/2026-08-20-spec-dScriptedRepeat-1.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-10 — the two start paths and the playbook-scoped directives](spec/2026-08-20-spec-dScriptedRepeat-10.md) | CLOSED | rev-5 | 2026-08-21 |
| [TOOL-dScriptedRepeat-11 — authoring a playbook: creation, and owner-instructed amendment](spec/2026-08-20-spec-dScriptedRepeat-11.md) | CLOSED | rev-6 | 2026-08-21 |
| [TOOL-dScriptedRepeat-2 — the PLAYBOOK TEMPLATE, derived then frozen](spec/2026-08-20-spec-dScriptedRepeat-2.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-3 — the playbook validity gate](spec/2026-08-20-spec-dScriptedRepeat-3.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-4 — the declaration seam: README names the path, playbook holds the globs](spec/2026-08-20-spec-dScriptedRepeat-4.md) | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-dScriptedRepeat-5 — the per-piece record: its writer, its reader, and its states](spec/2026-08-20-spec-dScriptedRepeat-5.md) | CLOSED | rev-11 | 2026-08-22 |
| [TOOL-dScriptedRepeat-6 — `pieces-complete`, the ninth core Definition-of-Done item](spec/2026-08-20-spec-dScriptedRepeat-6.md) | CLOSED | rev-11 | 2026-08-22 |
| [TOOL-dScriptedRepeat-7 — SET-scoped checks, and where they run](spec/2026-08-20-spec-dScriptedRepeat-7.md) | CLOSED | rev-11 | 2026-08-22 |
| [TOOL-dScriptedRepeat-8 — the output-scope refusal, and what it cannot see](spec/2026-08-20-spec-dScriptedRepeat-8.md) | SPECCED | rev-6 | 2026-08-20 |
| [TOOL-dScriptedRepeat-9 — the `proposal` park kind and the `--propose` verb](spec/2026-08-20-spec-dScriptedRepeat-9.md) | CLOSED | rev-6 | 2026-08-21 |
| [TOOL-dScriptedRepeat-13 — the bypass-flag guard covers the evidence records too, in the leg that can see them](spec/2026-08-23-spec-dScriptedRepeat-13.md) | CLOSED | rev-4 | 2026-08-23 |
| [TOOL-dScriptedRepeat-14 — a build README asserting a mechanism its own spec set has since revised](spec/2026-08-23-spec-dScriptedRepeat-14.md) | CLOSED | rev-4 | 2026-08-23 |
| [TOOL-dScriptedRepeat-15 — the kit's self-test suite becomes affordable, and every number here carries the command that produced it](spec/2026-08-23-spec-dScriptedRepeat-15.md) | CLOSED | rev-4 | 2026-08-23 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md) | journal | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md) | journal | TOOL-dScriptedRepeat-1 |
| [2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md) | research | TOOL-dScriptedRepeat-1 |
| [2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md](build/2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md) | research | TOOL-dScriptedRepeat-2 |
| [2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md](build/2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md) | journal | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-23-build-TOOL-dScriptedRepeat-13-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-13-acceptance.md) | journal | TOOL-dScriptedRepeat-13 |
| [2026-08-23-build-TOOL-dScriptedRepeat-14-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-14-acceptance.md) | journal | TOOL-dScriptedRepeat-14 |
| [2026-08-23-build-TOOL-dScriptedRepeat-15-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-15-acceptance.md) | journal | TOOL-dScriptedRepeat-15 |
| [2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md](build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md) | journal | TOOL-dScriptedRepeat-5 |
| [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md) | spec-audit | TOOL-dScriptedRepeat-1 |
| [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md) | spec-audit | TOOL-dScriptedRepeat-1 |
| [2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md](reviews/2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 |
| [2026-08-23-review-TOOL-dScriptedRepeat-13-diff-round7.md](reviews/2026-08-23-review-TOOL-dScriptedRepeat-13-diff-round7.md) | diff-review | TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15 |
| [2026-08-23-review-TOOL-dScriptedRepeat-13-spec-audit-round1.md](reviews/2026-08-23-review-TOOL-dScriptedRepeat-13-spec-audit-round1.md) | diff-review | TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15 |

Ids no record names: TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-8.

Ids no `spec-audit` record has ever named: TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11 TOOL-dScriptedRepeat-2 TOOL-dScriptedRepeat-3 TOOL-dScriptedRepeat-4 TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-8 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15.
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
  - [2026-08-23-spec-dScriptedRepeat-13.md](spec/2026-08-23-spec-dScriptedRepeat-13.md)
  - [2026-08-23-spec-dScriptedRepeat-14.md](spec/2026-08-23-spec-dScriptedRepeat-14.md)
  - [2026-08-23-spec-dScriptedRepeat-15.md](spec/2026-08-23-spec-dScriptedRepeat-15.md)
- **`build/`**
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-corpus-anatomy.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-extension-seams.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-external-instruction-design.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-hard-problems.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-in-repo-prior-art.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-kickoff-fork-rulings.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md)
  - [2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md](build/2026-08-20-build-TOOL-dScriptedRepeat-1-research-contradictions.md)
  - [2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md](build/2026-08-21-build-TOOL-dScriptedRepeat-2-canon-derivation.md)
  - [2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md](build/2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md)
  - [2026-08-23-build-TOOL-dScriptedRepeat-13-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-13-acceptance.md)
  - [2026-08-23-build-TOOL-dScriptedRepeat-14-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-14-acceptance.md)
  - [2026-08-23-build-TOOL-dScriptedRepeat-15-acceptance.md](build/2026-08-23-build-TOOL-dScriptedRepeat-15-acceptance.md)
  - [2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md](build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md)
- **`reviews/`**
  - [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit-round2.md)
  - [2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md](reviews/2026-08-20-review-TOOL-dScriptedRepeat-1-spec-audit.md)
  - [2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md](reviews/2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md)
  - [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md)
  - [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md)
  - [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md)
  - [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md)
  - [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md](reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md)
  - [2026-08-23-review-TOOL-dScriptedRepeat-13-diff-round7.md](reviews/2026-08-23-review-TOOL-dScriptedRepeat-13-diff-round7.md)
  - [2026-08-23-review-TOOL-dScriptedRepeat-13-spec-audit-round1.md](reviews/2026-08-23-review-TOOL-dScriptedRepeat-13-spec-audit-round1.md)
<!-- /gen:build-docs -->
