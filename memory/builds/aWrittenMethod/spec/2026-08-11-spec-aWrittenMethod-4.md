# TOOL-aWrittenMethod-4 — a gate for the sixth carrier

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base 7f614a17 · streams tooling

## 1. Goal

The build method landed with four pointers, each a path and never a summary, and nothing stops a
fifth being added tomorrow as a paraphrase. This repo grew four spellings of the unattended rules
exactly that way, one well-meaning summary at a time. Make a new carrier a decision somebody makes,
rather than a thing that happens.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/check-method-carriers.sh`: enumerate every TRACKED file that mentions
  `BUILD-METHOD.md`, excluding the method, its template, and the memory tree's own records under
  `<MEMORY_ROOT>/`; require each to be listed in a declared registry; red on an undeclared one.
- **S2** — the registry `tools/memory-tree/method-carriers.txt`, one `<path> · <why>` row per
  declared carrier, seeded with the four that landed. Shrink-only in spirit and gated on staleness:
  a row whose file no longer mentions the method reds as stale, the same both-directions discipline
  `install-prefix-waivers.txt` uses.
- **S3** — the leg asserts each declared carrier's mention is a **path token**, not a paraphrase:
  the line carrying the mention must contain the literal `BUILD-METHOD.md`, and the carrier must not
  contain any `## M<n>` heading, which is the shape a copied section takes.
- **S4** — `tools/gate-legs.json` gains the leg, `memory/map/features/build-method.md` claims it in
  its `gate-legs` list, and `AGENTS.md`'s gate-suite section names it — the three obligations a new
  leg carries in this repo.
- **S5** — `tools/memory-tree/check-method-carriers.test.sh`, both directions: an undeclared carrier
  reds, a stale registry row reds, a paraphrase-shaped carrier reds, and the tree as it stands passes.
  The positive control is mandatory.

## 3. Non-goals (OUT)

No semantic detection of a summary. Nothing here reads prose and judges whether it restates M3. The
check is structural — is this file declared, and does it point rather than copy — and the spec says
so rather than implying a comprehension it does not have.

No equivalent gate for the other governing documents. The protocol, the review protocol and the
hygiene rules have the same exposure, and generalising before this one has survived a single fold-in
would be designing for a population of one. F2.

No change to the four existing pointers. They are correct; they are the seed.

## 4. Design

### Data model

`method-carriers.txt`: comment lines, blank lines, and rows of `<repo-relative-path> · <why>`. The
`why` is not decorative — it is the sentence a future author reads when deciding whether their new
carrier is the fifth pointer or the first summary.

### The two failure directions

An UNDECLARED carrier is the drift this unit exists to catch. A STALE row is the failure the
`install-prefix-waivers.txt` experience produced: `TOOL-aSealedCaravan-1` records that keying a waiver
on `<path>:<line>` unpinned it whenever an edit landed above the line, and the gate then redded on a
merge that touched nothing it guarded. This registry keys on PATH only, with no line number, for
exactly that reason.

### Why a structural check is enough

The paraphrase this unit fears has a shape: it copies a section. `## M<n>` is the method's own heading
grammar and appears nowhere else in the tree, so a file carrying one has copied rather than pointed.
That is a narrow test, and it catches the specific historical failure — the four unattended spellings
were each a bulleted restatement, not a subtle rewording.

### Files touched (estimate)

Seven. The leg, its test, the registry, `tools/gate-legs.json`, the map dossier, `AGENTS.md`, and
`memory/backlog/TOOL.md` for whatever F2 defers.

### Alternatives rejected

A count pin with no registry: a bare number tells the next author nothing about which carriers are
legitimate, and this repo has already learned that a pin RAISE is indistinguishable from a drain
(`TOOL-aNumeralWarden-3`).

Forbidding mentions outside a fixed list in the leg itself: that is the registry, spelled in a script
where an adopter cannot edit it without patching the kit.

## 5. Production-readiness checklist

- security — N/A. A read-only grep over tracked files.
- perf / scale — one `git ls-files` plus one grep. Comparable to `check-install-prefix.sh`.
- a11y · i18n — N/A.
- error / empty / loading states — an EMPTY carrier set is a refusal, not a pass: if the leg finds no
  mentions at all, the method has been unwired and that is the loudest possible drift. This repo's
  `vacuous-selector-empty-population` class, guarded explicitly.
- observability — the leg prints the carrier count and names every undeclared or stale path.
- risks — a false red on a record legitimately discussing the method. §2's exclusion of
  `<MEMORY_ROOT>/` covers specs, reviews and backlog rows, which is where such discussion lives.
- testing + left-shift gates — S5, four arms plus the positive control.
- migration / rollback — the registry is seeded with today's four carriers, so the leg is green on
  landing. Rollback is deleting the leg and its row.
- user docs — the registry's own header comment, and the `AGENTS.md` line S4 adds.

## 6. Acceptance criteria

- **AC1** — When a new tracked file mentioning `BUILD-METHOD.md` is added and not declared,
  `bash tools/memory-tree/check-method-carriers.sh` REDS naming that file.
- **AC2** — When a declared row names a file that no longer mentions the method, the leg REDS naming
  the row as stale.
- **AC3** — When a carrier contains a `## M<n>` heading, the leg REDS naming it as a copy rather than
  a pointer.
- **AC4** — When the tree stands as landed, the leg exits 0 and reports four carriers. Positive
  control.
- **AC5** — When every mention is removed from the tree, the leg REDS on the empty population rather
  than passing.
- **AC6** — When `bash tools/memory-tree/check-method-carriers.test.sh` runs, it passes with every
  arm above exercised by a fixture that can actually produce the condition.
- **AC7** — When `bash tools/run-gates.sh` runs, the new leg appears in its output and the run-gates
  canary passes with the leg single-sourced from `tools/gate-legs.json`.
- **AC8** — When `python tools/codebase-map/test_codebase_map.py` runs, the new leg is claimed by
  `memory/map/features/build-method.md` and coverage exits 0.

## 7. Gates

`tools/memory-tree/check-method-carriers.sh` (new) · its self-test (new) ·
`tools/run-gates.sh` canary · `python tools/codebase-map/test_codebase_map.py` ·
`tools/check-install-prefix.sh` · `python tools/memory-tree/check-arms.py` ·
`tools/memory-tree/check-memory-hygiene.sh` · `bash tools/run-gates.sh` at the push boundary.

**This unit ADDS a gate leg**, taking the bar from 47 to 48. Unit 1 declined to add one and gave its
reasons; those reasons were about the METHOD not needing a leg, and do not bind a unit whose entire
deliverable is a check.

## 8. Open questions

### F1 — the `## M<n>` heuristic, or nothing

S3's structural test catches a copied section and misses a fluent paraphrase that invents its own
headings. Options: ship the heuristic; ship the registry alone and rely on the declaration being a
decision point; ship neither. **Recommendation: ship the heuristic.** It is the most feature-rich
option that satisfies the constraints — it costs three lines, it catches the exact historical shape,
and §3 already states plainly that it is structural rather than semantic, so no reader is misled
about what it proves.

### F2 — generalise to the other governing documents

The protocol, `REVIEW-PROTOCOL.md` and `HYGIENE.md` have identical exposure. Options: generalise the
leg now to a declared set of documents; ship method-only and file the generalisation.
**Recommendation: ship method-only and file it.** The registry format and the two failure directions
are unproven; generalising an unproven mechanism across four documents multiplies whatever is wrong
with it by four. The follow-up row is S5's deferral in §4's file estimate.

### F3 — where the leg lives

It gates a memory-tree artifact, so `tools/memory-tree/` is the natural home; but it reads files
across the whole repo, which is `tools/check-*.sh`'s shape. **Recommendation: `tools/memory-tree/`.**
The document it guards ships with that kit, and an adopter who installs the kit should receive the
guard with it — a check living outside the kit would be gov-only, which is the asymmetry unit 1's
review already punished.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Raised by unit 1 as `TOOL-aWrittenMethod-4`, where it was
  explicitly declined as out of scope with the reasoning that enforcement was not that unit's job.

## 10. Reuse audit

`reuse_lookup.py` for this unit set returned `check-install-prefix.sh` as an affordance seam
(`shared-seams prose (install-prefix): docu, gat, rend, shipp`), which is the seam this unit extends:
it is the repo's existing "enumerate shipped files, compare against a declared registry, red on an
undeclared hit and on a stale row" leg, and S1 through S3 are that same shape pointed at a different
population. Its waiver file `tools/install-prefix-waivers.txt` is the format precedent for S2, and its
`<path>:<line>` keying is the precedent's own recorded MISTAKE — `TOOL-aSealedCaravan-1` — which is
why S2 keys on path alone.

The recall probe returned no prior decision on cross-reference gating; the nearest is the never-landed
playbook cross-reference gate this build's unit 1 filed as a decline, which has no spec and no
mechanism to inherit. So the technique is reused and the population is new, which is the case §10
exists to record rather than a claim that no seam fits.
