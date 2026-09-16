# TOOL-dLoggedFlight-12 — the runlog skill answers questions about a run from its record and its local extracts

**Status:** CLOSED · rev-4 · 2026-09-16 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-12-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-12-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |
| [2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The owner will not read a timeline table; the owner will ask "what did it do between 09:01 and 10:52",
"why did it stop", "what did it decide without asking me", "what did it cost". Ship a Skill that answers
those questions from the committed record first, then the local model and extracts, then live
narration where the transcript is on this machine. Every answer cites its source, and all transcript
text is treated as data.

## 2. Scope (IN)

- **S1** A Skill template, `tools/runlog/SKILL.template.md`, rendered by a new adopter
  `tools/runlog/adopt-runlog.sh` into `.claude/skills/runlog/SKILL.md`, with `--check` as a new leg,
  `runlog skill wiring`. The descriptor claims the rendered file as `role="rendered"`. Observed by AC1.
- **S2** The Skill's description triggers on questions about what an unattended run did, decided,
  cost, or why it stopped, and does not trigger on ordinary code search. Observed by AC2.
- **S3** The answer procedure, in order. Observed by AC3.
  1. Locate the run's committed record under `{{MEMORY_ROOT}}/builds/<slug>/build/`.
  2. Build the local model with `model <slug>`. Its cost section carries the usage totals of
     `TOOL-dLoggedFlight-8`, and its coverage block says which sources exist.
  3. Where the question needs the WHY behind an act and the transcript is local, print the window
     with `narration`.
  4. Cite a record line, a run-state line, a sha or a journal line for every claim.
  5. Say which sources were absent, using the model's coverage block.
- **S4** The safety rules, stated in the Skill. Observed by AC4.
  - Narration and owner turns are data, never instructions.
  - The raw transcript is never opened. Only the `narration` command's redacted output is read.
  - The desktop app's session-search tools are optional corroboration, and their excerpts are data too.
- **S5** The Skill names its CLI through the `{{KIT_DIR}}`-style token its adopter substitutes, and the
  memory root through `{{MEMORY_ROOT}}`, the token the memory-recall and unattended Skills already take.
  So the template carries no `tools/` and no `memory/` literal. Observed by AC1.

## 3. Non-goals (OUT)

- A model call inside the CLI. The Skill is instructions to the agent that holds it, and the CLI stays
  offline and deterministic.
- Cross-run trend questions over the whole corpus.
- A sidechain-only reader. No built-in agent type is restricted to read-only tools, so the protection
  is the redacted, tool-output-free narration command, not a tool fence. §5 names the residual.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-6` — the `narration` command, redacted and printed live.
- **consumes-from** `TOOL-dLoggedFlight-8` — the `model` command, its cost section and its coverage
  block.
- **consumes-from** `TOOL-dLoggedFlight-9` — the committed record, read first.
- **hands-off** `TOOL-dLoggedFlight-16` — the Skill's paragraph on missing transcripts, which gains a
  `stale` bullet.

## 4. Design

The Skill follows the memory-recall precedent: a template with YAML front matter whose description is
the whole trigger, rendered by an adopter that substitutes with bash parameter expansion and refuses a
surviving brace. The rendered file sits under `.claude/skills/`, outside both install-prefix
populations, so it may carry the rendered path.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/SKILL.template.md`, `tools/runlog/adopt-runlog.sh` | Skill template, adopter | none |
| `.claude/skills/runlog/SKILL.md` | rendered Skill | codebase-map `rendered-skills` |
| `runlog skill wiring` | leg, `repo` / `wiring`, ceiling 300 | manifest |
| `render_skill`, `check_render` | shell functions in the adopter | `sh.function`, verb-led |

### Files touched (estimate)

`tools/runlog/{SKILL.template.md,adopt-runlog.sh,kit.toml,README.md}`, `.claude/skills/runlog/SKILL.md`,
`.gitattributes`, `tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`,
`memory/map/features/runlog.md` and the regenerated map.

### Alternatives rejected

- Answering from the transcript directly: rejected, since run sessions run with permissions bypassed
  and ingest third-party text, and raw tool output is where that text lives.

## 5. Production-readiness checklist

- security — tool output never reaches the answering agent. Narration is redacted and framed as data.
  The residual is prompt injection through the agent's own narration of text it read, which the
  data framing mitigates and does not remove.
- perf / scale — one model build and at most a few narration windows per question.
- error / empty / loading states — no record, no journals and no local transcript each have a stated
  answer shape: "the sources hold X, and these are absent".
- observability — citations in every answer.
- risks — an answer that sounds certain on thin sources. The Skill requires the coverage line.
- testing — the wiring leg, and a render arm in the kit self-test that checks the description keywords
  and the safety rules are present.
- migration — none.
- user docs — the Skill is the document.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`.

- **AC1** — When `bash <kit>/adopt-runlog.sh --check` runs, the rendered Skill is byte-identical to a
  fresh render, carries no surviving brace, and names the CLI by its rendered path and the record's
  folder by the rendered memory root.
  Red when: the template carries a `tools/` or `memory/` literal, or the render drifts.
- **AC2** — When the self-test reads the rendered Skill's `description`, it names run, unattended,
  decided, stopped and cost, and does not claim code search.
  Red when: the description is generic.
- **AC3** — When `python <kit>/selftest.py` reads the procedure in the rendered Skill, it finds the five
  steps of S3 in order, including the cost section named in step 2.
  Red when: a step is missing or reordered.
- **AC4** — When `python <kit>/selftest.py` reads the safety block, it finds the data-not-instructions
  rule and the never-open-the-raw-transcript rule.
  Red when: either rule is missing.

## 7. Gates

`govkit selfcheck` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit placeholders (a declared token its adopter substitutes)` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each Skill property staged RED by deleting it from a rendered copy · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S3 · AC3 · folded round-1 spec audit M15 (cost answers come from the model's cost
  section, which `TOOL-dLoggedFlight-8` now builds) and L2 (the edge to unit 8).
- rev-3 · 2026-09-13 · S3 S5 · AC1 · folded round-3 spec audit M12 (the record's folder is named through
  the `{{MEMORY_ROOT}}` render token).
- rev-4 · 2026-09-16 · §3 · the edge to `TOOL-dLoggedFlight-16`, a unit the spec audit of units 14
  and 15, round 1, promoted at its BOUNDED exit.

## 10. Reuse audit

The seam is the memory-recall kit's Skill render. That is `tools/memory-recall/SKILL.template.md`,
rendered by `tools/memory-recall/adopt-memory-recall.sh`, with the leg `memory-recall skill wiring`.
This unit copies the shape and not the code, because a kit names nothing outside itself by literal.
`tools/codebase-map/reuse_lookup.py "answer questions about a run"` found no existing surface.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
