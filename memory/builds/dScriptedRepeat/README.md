---
slug: dScriptedRepeat
node: d
opened: 2026-08-20
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-dScriptedRepeat-1
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

**The reference playbooks are two different shapes and both are evidence.** `PLAYBOOK.md` is a
1,290-line step checklist where every step carries `GATE <leg>` or `CHECK <why>` — 92 GATE tags, 95
CHECK tags, 110 numbered steps — and its own I21 invariant reds a step that is untagged or names no
runnable leg. `HYBRID-PLAYBOOK.md` is a 245-line recipe: an exact parameter table, a prompt scaffold
with named slots, hard rules each traced to an owner correction, an accepted-instance library, a
"what was ruled out — don't re-try" section, and a dated bake-off marked don't-redo. The GATE/CHECK
tagging is the same discipline this repo already states as a rule (a gate's own header names what it
does not check; a skip must announce itself), which is why it is the template's spine rather than an
import.

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

Two budgets are nearly spent and both bind this build's design. `memory/guides/BUILD-METHOD.md` sits
at 20,567 B of its 22 KB budget and 283 of its 290 lines — roughly 1,961 B and 7 lines of headroom,
so a new method section is an owner call rather than an edit, exactly as M12's own budget rise was.
The corpus read path sits at 106,194 B against a declared ceiling of 112,987 — 6,793 B of margin,
which one protocol section plus this build's own generated row can plausibly exhaust. Externalizing
is preferred to spending either.

<!-- roster:units -->
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-08-20 · streams tooling
ids TOOL-dScriptedRepeat-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

*This build holds no records yet.*
<!-- /gen:build-docs -->
