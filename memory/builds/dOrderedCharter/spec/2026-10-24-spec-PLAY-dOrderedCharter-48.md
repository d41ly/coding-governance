# PLAY-dOrderedCharter-48 — the sources that tell a writer to cite path and line are a query over the directive sources, every hit re-pointed or kept by name

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 10 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-48-deviation-481.md](../build/2026-10-24-build-PLAY-dOrderedCharter-48-deviation-481.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 82 at HIGH**, its item **H9**. `PLAY-dOrderedCharter-26` S6 re-points a typed list
of four producers that direct writers at `file:line`, and misses two: the spec writer's role
(`tools/roles/agents/gov-spec-writer.agent.md:30`, "cite it by path and line") and the orientation
counterfactual's prompt (`tools/workflows/orient-counterfactual.js:111`, "Cite files by path and
line"). The next build's spec writer follows its role, writes path:line citations into new specs, and
unit 26's `shrink-only` reds the `tags` leg on every such spec commit. This unit replaces the typed list
with a declared query over the sources that render directives, re-points every hit that tells a writer
to cite a code location, keeps the rest on a keyed list with a reason, and reds a new hit that is
neither. It repairs unit 26 and is built right after it.

## 2. Scope (IN)

- **S1** — The query, declared once in `tools/playbook/positional.py`: `PRODUCER_RE`, the
  case-insensitive pattern `file:line|path and line|<path>:<line>`, run by `git grep` over
  `PRODUCER_PATHSPECS`, the directive sources: `tools/roles/agents/`, `tools/workflows/`, `skills/`,
  `coding-governance-agents.template.md`, `tools/*/SKILL.template.md` and `tools/*/*.template.md`. A hit in a
  rendered file whose source sits beside it (`<stem>.template.<ext>` for `<stem>.<ext>`) is attributed
  to the source and printed once. `python tools/playbook/positional.py producers` prints every hit as
  `<path>:<n>\t<line>`. This supersedes unit 26 S6's typed list as the population. Observed by AC1.
- **S2** — The re-points. Every hit that directs a writer to cite a location in a file of
  `CODE_EXTENSIONS` (unit 26 S1) names the stable forms instead, `path#symbol` or the blob-pinned line
  `<path>@<oid>:<n>`: at the base, unit 26 S6's four sources, `tools/roles/agents/gov-spec-writer.agent.md:30`
  (rendered to `.claude/agents/gov-spec-writer.md` by the roles render) and
  `tools/workflows/orient-counterfactual.js:111`. The pass re-runs S1's query, judges each hit, and
  names every re-pointed and every kept hit in its commit's `Decided:` trailer. Observed by AC2.
- **S3** — The kept hits, keyed. `tools/playbook/positional-producers.txt` holds one
  `<path>\t<the line's text, trimmed>` row per kept hit, keyed by text and never by line number, with
  a `# ` reason line above each group: narration of the old form, a read directive (re-read the
  cited line), or a citation of a document line, which `CODE_EXTENSIONS` does not hold
  (`tools/runlog/SKILL.template.md:54` cites record lines as `<path>:<line>`). `positional.py
  producers --seed` writes it once at the pass, after S2, and refuses when it already holds a row; it
  only ever shortens after that. Observed by AC3.
- **S4** — The arm. Inside unit 26's `positional` arm of `gov_tag.py check`, a `producers` limb reds a
  hit of S1's query that is not on the list and whose line names neither stable form, naming the path,
  the line and the remedy (re-point it, or add a row with its reason); a row whose text no hit carries
  is red as stale. It acts under `tags.positional` as unit 26 S3's limbs do. Observed by AC4.
- **S5** — The plants, through unit 19's fixture: `positional-producer-new` (a role source gains
  "cite it by file:line") and `positional-producer-stale` (a kept row whose line was re-pointed).
  Observed by AC4.

## 3. Non-goals (OUT)

- The reference forms, the list of citations, the remedy verb and the legs: unit 26's.
- Grandfathering records written before the check: `PLAY-dOrderedCharter-47`.
- Hook messages under `tools/hooks/`: they narrate a join and direct no writer
  (`tools/hooks/agent-cap.js:2414`), and the query's pathspecs leave them out by name in §4.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-26` — the stable forms, `CODE_EXTENSIONS`, the positional arm and S6's four re-points, which S1 makes a query and S4 joins as a limb; without them there is no form to point at

## 4. Design

### Evidence

Read at `ce13efbe`. `tools/roles/agents/gov-spec-writer.agent.md:30` reads "cite it by path and line";
`tools/workflows/orient-counterfactual.js:111` reads "Cite files by path and line, never ingest them into
the card."; neither has a `.template.` source. S1's query over the base tree printed 41 hits. Beside
unit 26 S6's four sources (`tools/roles/agents/gov-diff-reviewer.agent.md:26`,
`tools/workflows/REVIEW-PROTOCOL.template.md:193`, the two drift-audit templates and
`tools/workflows/tier2-review.template.js`, with their renders), it printed the two missed directives
and `tools/roles/agents/gov-skeptic.agent.md:26` (re-read the cited line), `tools/workflows/README.md:489`
and `:522`, `tools/workflows/check-review-join.sh:16` and `:20`, `tools/workflows/check-review-join.test.sh:159`,
`tools/workflows/review_replay.py:188`, `tools/runlog/SKILL.template.md:54` (a citation of record lines)
and `tools/memory-tree/HYGIENE.template.md:160` (a registry keyed on path alone), each narration, a read
directive or a document citation. Those are the seed's candidates; the pass judges them (PINNED 2026-10-24).

### Why the hooks stay out

`tools/hooks/README.md:119` and `tools/hooks/agent-cap.js:2414` describe why the review join keys on an
integer id rather than a `file:line` string. A hook message is read by an agent, but neither line
directs a citation, and adding the hooks to the pathspecs adds only kept rows. A hook that ever tells
a writer what to cite is a source this query names in a later unit.

### Inventory

Minted: `PRODUCER_RE`, `PRODUCER_PATHSPECS`, the verb `producers` and its `--seed`, the file
`tools/playbook/positional-producers.txt`, the limb name `producers`, and the plants
`positional-producer-new` and `positional-producer-stale`. Naming cells: `lexicon naming predicates`
grades the Python names.

### Files touched (estimate)

- `tools/playbook/positional.py`
- `tools/playbook/positional-producers.txt` (new)
- `tools/playbook/gov_tag.py` (the plants)
- `tools/roles/agents/gov-spec-writer.agent.md`
- `.claude/agents/gov-spec-writer.md` (its render)
- `tools/workflows/orient-counterfactual.js`

### Rollout

Live at landing, order 10, after unit 26 at order 9. `PLAY-dOrderedCharter-47` shares order 10 and also
writes `tools/playbook/positional.py`, and unit 25 shares it and writes `tools/playbook/gov_tag.py`, so
the dispatch sequences them (M6).

### Alternatives rejected

- **Adding the two missed files to unit 26 S6's typed list**: the next producer is missed the same
  way; the finding is that the list is typed.
- **Only the query, with no keyed list**: every narration hit would red, or the pattern would grow
  exceptions inside the regex, which is a typed list in a worse place.

## 5. Production-readiness checklist

- security: no new surface; one `git grep` over tracked sources.
- perf / scale: one `git grep` per check run, DERIVED and timed at the pass against the leg's ceiling.
- error / empty / loading states: an empty query result with a non-empty list reds every row as stale;
  a seed over an empty result writes a header and no row, printed as such.
- observability: each red names path, line and remedy; `producers` prints the population.
- risks: a directive phrased without the three spellings is not found; the list's reasons say what
  the pattern reads.
- testing: AC1 to AC4.
- migration: none.
- user docs: unit 26's paragraph in `tools/playbook/README.md` names the query and the list.

## 6. Acceptance criteria

- **AC1** — When `python positional.py producers` runs at the pass, before the
  re-points, it prints `tools/roles/agents/gov-spec-writer.agent.md:30` and
  `tools/workflows/orient-counterfactual.js:111`, and prints no line of `tools/workflows/tier2-review.js`,
  the render of `tools/workflows/tier2-review.template.js`.
  figure: DERIVED, the population read by the query at the pass; 41 hits at `ce13efbe` before render
  attribution, PINNED 2026-10-24.
  Red when: the population is typed, or a render is counted beside its source.
- **AC2** — When the same verb runs after the pass and its output is filtered to hits not on
  `positional-producers.txt`, every line printed names `path#symbol` or a blob-pinned
  line, and `git grep -n -i "path and line" -- tools/roles/agents/gov-spec-writer.agent.md` prints
  nothing.
  Red when: a directive still tells a writer to cite a code location by line.
- **AC3** — When `positional.py producers --seed` runs a second time, it exits 1 naming the list.
  Red when: the keyed list can be re-seeded.
- **AC4** — When `python gov_tag.py --fixture --plant positional-producer-new` runs, the
  arm reds naming the planted path and line; `--plant positional-producer-stale` reds the stale row.
  Red when: a new producer or a stale keep passes.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `roles render wiring` · `roles render selftest` · `roles catalogue` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC4 · the playbook-render selftest runs the two producer plants, each failing case staged by deleting the limb · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 26's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How a narration hit is told from a directive.** Options: (a) a keyed keep list with reasons,
  seeded once and shrink-only, as unit 26 S2's citation list is; (b) exceptions inside the pattern;
  (c) a marker comment on each kept line. (b) types the list into a regex and (c) edits files that
  narrate history to carry a marker. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the shape
  unit 26 already uses. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 82 (HIGH, item H9).

## 10. Reuse audit

The seam extended is unit 26's `positional` arm and its keyed-list shape (its S2 and S3) in
`tools/playbook/positional.py`; the list here is that shape applied to a second population. `python
tools/codebase-map/reuse_lookup.py "find every source that tells an agent to cite a file and line"`
ranked `check_line`, `render_line` (`tools/runlog/runlog_lib.py`) and `corpus_files` by name stem
and no producer census; no existing seam derives a directive population, so
none fits beyond unit 26's own. The recall query returned TOOL-aProbedToolkit-17, an ask recording
that the charter mandated `file:line` while the hygiene gate refused it, the conflict this unit and
unit 26 resolve, and the review's H9 text.

Recall terms used: `python tools/memory-recall/query.py "which role and workflow texts tell writers to cite a file and line" --terms "file:line citation path and line producer directive gov-spec-writer reviewer prompt blob-pinned"`
