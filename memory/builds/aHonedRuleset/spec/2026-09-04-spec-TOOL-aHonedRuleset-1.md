# TOOL-aHonedRuleset-1 — the prose census

**Status:** CLOSED · rev-1 · 2026-09-04 · node a · Tier-1 · base c4fcf5ad · streams tooling+playbook · order 0

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

Measure byte pressure and cross-document redundancy across this repo's load-bearing governing prose,
and produce a ranked cut list, so the instruction-optimization work that follows is grounded in
measurement rather than in reading impressions.

## 2. Scope (IN)

- **S1** — a re-runnable census script under this build's `build/` folder, declaring its corpus as
  rows rather than globbing it, refusing when a declared row names a file that does not exist.
- **S2** — per-file size against whatever ceiling owns it, resolved from the owning file in every
  case: `tools/template-size-limits.txt`, `GUIDE_CAP_BYTES`, or a budget a document declares about
  itself in prose.
- **S3** — cross-document verbatim overlap by word shingling, reported per pair and as passages with
  both locations.
- **S4** — a scan for typed magnitudes in prose, as the cheapest available proxy for the restatement
  class shingling cannot see, reported as candidates and never as findings.
- **S5** — the census report: the two theses tested, the confirmed duplication by name, the ranked
  cut list, and a separately-kept proposed-drop list.

## 3. Non-goals (OUT)

No protocol, template or skill prose is edited by this unit. No ceiling is raised, lowered or added.
No open backlog row is answered — `TOOL-aScouredKit-23`, `TOOL-dSpentCeiling-4` and
`TOOL-dFoldedVerdict-7` are cited and left to their owners. The cuts the census ranks are specced as
`TOOL-aHonedRuleset-2` through `-6` and built by none of them here.

## 4. Design

The script is stdlib-only and reads every file in binary before decoding, because a text-mode read
eats a bare CR and the byte count then disagrees with every gate that measures the same file. Ceiling
resolution reads the declaring file rather than carrying a copy of the number, so a ceiling that
moves is reported at its new value and never as a stale constant. The report cites figures the script
emits, names the command, and cedes to that output on any disagreement.

## 5. Production-readiness checklist

- security — N/A: the script reads tracked files and writes nothing.
- perf / scale — runs in seconds over a corpus of tens of files; no ceiling declared or owed.
- a11y — N/A: no user interface.
- i18n — N/A.
- error / empty / loading states — a declared row naming a missing file is a refusal, not a skip.
- observability — every figure is re-derivable by re-running one command.
- risks — the shingle method is blind to restatement in different words; the script's header says so
  where it reports, rather than leaving a reader to infer it.
- testing + left-shift gates — no new gate. The census is a measurement, not a checker.
- migration / rollback — N/A: additive records only.
- user docs — N/A: an internal build record.

## 6. Acceptance criteria

- **AC1** — When `python memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py`
  is run from the repo root, it exits 0 and prints all five sections.
- **AC2** — When a row is added to `CORPUS` naming a file that does not exist, the script refuses
  with `REFUSED` rather than reporting a clean corpus.
- **AC3** — When the report quotes a figure, that figure appears in the script's output; `§1` of the
  output carries the ceiling table the report's headline cites.

## 7. Gates

`memory hygiene`, `build README slot contract`, `codebase-map coverage + freshness`,
`spec tokens (a spec's own names resolve)`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · **Authored AFTER the unit was built, as a record repair, and this line is the
  disclosure rather than a formality.** The census was built and committed at `102e98f0` with no
  spec, which BUILD-METHOD M2's hard floor forbids — "I will spec it afterwards is the same act with
  the record written last". It was written here because `HYGIENE.md` check 21 refused the two census
  records: their `**Serves:**` ids resolve against a spec H1 and no H1 defined this id. The honest
  repair was to write the missing spec and say when, not to re-point the records at a sibling unit
  they did not serve. Status is CLOSED because the work it describes is landed and verified.

## 10. Reuse audit

N/A — Tier-1. `SPEC10_EVIDENCE_CUTOFF` binds the ten-section canon on Tier-2 specs; this unit is
Tier-1 and takes the light profile. The reuse probes were nonetheless run before the script was
written and found no existing duplication or census tooling in `tools/` to extend.
