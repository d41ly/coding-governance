# TOOL-dLinkedLibrary-87 — the CI census plants every refusal branch of the Azure `variables:` closed set: an unknown key, a scalar expression and a template item

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 33 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-87-deviation-871.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-87-deviation-871.md) | deviation | — |
| [2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-87-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-87-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-1 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 81 to 86
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) confirmed
finding **id 1 at HIGH**, report item **H1**. No other id shares the item. Id 28, item M13, binds the same
gap at MEDIUM, seen through 81's "Observed by" claims, and is an item of the minors batch
`TOOL-dLinkedLibrary-91`.

`TOOL-dLinkedLibrary-81` S2 refuses every `variables:` item outside its closed set, but its S4 plants only
items that open with `${{` and one `- name:` control. Nothing plants an item with an unknown plain first
key, a scalar `variables:` value, or a `- template:` item for S3's interim refusal. So a reader that
catches `${{` alone passes 81's AC1 to AC3 and its arm, while `- someNewForm:` grades `importable`: the
deny-by-default rule 81 exists for ships with no plant behind it.

This unit plants each refusal branch 81 S2 and S3 name, with a criterion whose expected line quotes
that branch's reason, and stages each red by removing that branch. It repairs `TOOL-dLinkedLibrary-81`
and builds one step after it (order 33).

## 2. Scope (IN)

- **S1** — The unknown-key branch. A case of `adopt_program.py --fixture --plant ci-census`, a scratch
  tree of its own: an `azure-pipelines.yml` whose pipeline-level `variables:` list holds `- name:
  CONFIG` with `value: Release` and then `- foo: bar`, beside two plain jobs, `publish` running
  `./publish.sh` and `test` running `npm test`. 81 S2's "the item's first key otherwise" branch refuses
  both jobs, each reading `refused: unreadable variables item foo`. Observed by AC1.
- **S2** — The scalar branch. A case of the same plant, its own tree: an `azure-pipelines.yml` holding a
  `parameters:` list with `- name: vars` and `type: object`, and the pipeline-level line `variables: ${{
  parameters.vars }}`, beside the same two jobs. 81 S2's scalar branch refuses both, each reading
  `refused: unreadable variables item expression`. Observed by AC2.
- **S3** — The template item. A case of the same plant, its own tree: an `azure-pipelines.yml` whose
  pipeline-level `variables:` list holds `- template: vars.yml`, beside the same two jobs. With
  `TOOL-dLinkedLibrary-82` landed, both jobs read 82 S2's `refused: unreadable credentials template
  vars.yml`; over a scratch copy that lacks 82's template branch, they read 81 S3's interim `refused:
  unreadable variables item template`; neither reads `importable`. Observed by AC3.
- **S4** — The staged reds, one per branch: a scratch copy of `adopt_program.py` whose closed-set read
  catches only items and keys opening `${{` turns S1's jobs `importable`; one lacking the scalar branch
  turns S2's jobs `importable`; one lacking both 81 S3's fallback and 82's branch turns S3's jobs
  `importable`. Observed by AC4.
- **S5** — The observation 81 claims. 81 S2's unknown-key and scalar branches are observed by AC1 and
  AC2 here, and 81 S3's interim refusal by AC3 here; this unit's acceptance ledger names each 81 scope
  item beside the criterion that observes it. Observed by AC5.

## 3. Non-goals (OUT)

- A new item form or a new reason: 81 S1 to S3 and 82 S2 are unchanged; this unit adds plants and
  criteria only.
- Flow-style `variables:` values and items: `TOOL-dLinkedLibrary-88` (id 27).
- Re-pointing 81's own "Observed by" text and its ledger line: the minors batch
  `TOOL-dLinkedLibrary-91`, its item for id 28.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-81` — S2's unknown-key and scalar branches and S3's interim template refusal, which S1 to S4 plant and stage red (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-82` — S2's `unreadable credentials template <path>` reason, which S3's template tree reads once 82 has landed (id 1)
- **hands-off** `TOOL-dLinkedLibrary-91` — the plants and criteria S1 to S3 add, which unit 91 names as the observation of 81 S2 and S3 in 81's acceptance ledger (id 28)
- **hands-off** `TOOL-dLinkedLibrary-96` — its pass, which writes 91 S2's amendment line into 81's ledger, plants the quoted scalar `variables: '${{ parameters.vars }}'` with its restaged S4 red, and re-renders the map, by unit 96's S3, S13 and S12 (ids 2, 24, 11)

## 4. Design

### Evidence

- 81 S4 (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md`, S4) plants a `- ${{ if }}` item, a `${{ if }}` key, a
  `- ${{ each }}` stage item and a `- name:` control, and no other item form.
- 81 S3 says the interim `- template:` refusal is "Observed by AC3", while 81 AC3 grades only items whose
  first key is not `name`, `group` or `template`.
- 82 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-82.md`, S2) spells `refused: unreadable credentials
  template <path>`.
- `git ls-files tools/memory-tree/adopt_program.py` prints nothing at base, so the module and its plant
  are unbuilt and every plant here is new.

### Why the plants hold no credential

S1 to S3 nest no name 79 S2 reads as a credential, and S1's first item is the readable control, so the
only rule that can fire on each tree is the branch the tree plants. A tree that also tripped 79 would
leave the expected reason to a precedence no spec states.

### Rollout

Order 33 beside `TOOL-dLinkedLibrary-88`. Both write `adopt_program.py`, so BUILD-METHOD M6's clause 1
sequences the passes; neither reads the other's plant.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **One tree holding all three forms.** The first refusal would mask the others, so a branch could be
  missing with every job still refused.
- **A static check that every reason string in 81 S2 has a plant.** It is the report's left-shift gate
  and grades spec text; the plant is what observes the code.

## 5. Production-readiness checklist

- security — makes 81's deny-by-default observable for every branch it names; no behaviour changes.
- perf / scale — three scratch trees more in the plant.
- error / empty / loading states — unchanged from 81.
- observability — each criterion quotes the branch's reason string.
- risks — none beyond 81's: the plants exercise existing branches.
- testing — S1 to S3 under `adopt_program.py --fixture`, S4's reds on scratch copies.
- migration — none.
- user docs — none under `help/`: the page sentence for the item set is unit 91's item for ids 7 and 25.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  the tree whose list holds `- foo: bar` read `refused: unreadable variables item foo`.
  Red when: the closed set catches only `${{` and the unknown key passes.
- **AC2** — When the same plant runs, both jobs of the tree whose `variables:` value is `${{
  parameters.vars }}` read `refused: unreadable variables item expression`.
  Red when: a scalar `variables:` value is read as an empty block and passes.
- **AC3** — When the same plant runs, both jobs of the `- template: vars.yml` tree read `refused:
  unreadable credentials template vars.yml`; over a scratch copy of `adopt_program.py` with 82's template
  branch removed, run by `python -I` against the same plant, they read `refused: unreadable variables
  item template`.
  Red when: the template item reads `importable` in either order of the two passes.
- **AC4** — When each of S4's three scratch copies runs the plant, the tree its break targets prints
  `importable` for both jobs.
  Red when: a staged break leaves its tree refused, so the plant does not discriminate the branch.
- **AC5** — When `grep -n 'TOOL-dLinkedLibrary-81'` runs over this unit's acceptance ledger, it prints a
  line naming 81 S2 beside AC1 and AC2 and a line naming 81 S3 beside AC3.
  Red when: an 81 branch is left with no named observation.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's unknown-key, scalar-expression and template-item trees, the failing case staged by a `${{`-only closed-set read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 81 to 86, id 1 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the hands-off edge to unit 96, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is the `ci-census` case of unit 8's `--fixture --plant` mode in
`tools/memory-tree/adopt_program.py`, as 81 S4 extends it, with 81 S2 and S3 and 82 S2 unchanged. `python
tools/codebase-map/reuse_lookup.py "refuse an azure variables item whose form the reader does not know"`
ranked `read`, `read_text`, `note` and `read_conf`, none a CI reader, so no existing seam fits beyond
the census plant being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census refuse an azure variables item form it cannot read" --terms "census ci-job azure variables item deny-by-default refused unknown key expression template plant"`
