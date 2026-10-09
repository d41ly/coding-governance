# TOOL-aDistilledCharter-3 — the parity gate drops the retired pairs, the canary re-points, and a new arm bans section-number citations

**Status:** CLOSED · rev-3 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

Three gates read the v3.5 charter's wording: the parity gate pins five phrases of §8, the run-gates
canary requires `AGENTS.md` to name two runner files, and nothing stops a live file citing a charter
section by number, which is how the runbook's kit-block counts went stale. This unit re-keys the
first two to v4.0 and adds the third as an arm, so a later restructure reds where it breaks a
citation instead of leaving it to rot.

## 2. Scope (IN)

- **S1** — `tools/check-playbook-parity.sh` S2 keeps the pairs `verify-agent total` and
  `stamp rule sha expression` and loses `lens-array bound`, `agent-cap hook matcher`,
  `bounded-helper width` and `resolved-K ceiling`, whose phrases v4.0 no longer states.
  `tools/check-playbook-parity.test.sh` follows. Observed by AC1.
  **Readers:** by name: `check-playbook-parity.sh` `PAIRS` and its header, the sibling test's
  fixtures, and the v3.5 template's §8 sentence counting FIVE compared values; by value:
  `tools/hooks/agent-cap.js` `MAX_LENSES` and `MAX_VERIFIERS` stay owned there, and the
  `verifier fan-out` leg keeps comparing the harness against them.
- **S2** — A new stage S4 in `check-playbook-parity.sh` scans the tracked product surface — §4
  "The population" — for a charter section cited by number, §4 "The predicate", and fails naming
  each hit's file and line. Near-misses print and do not fail. Observed by AC2 and AC3.
- **S3** — `tools/run-gates/run-gates.gov.test.sh` G4/G5 read `memory/guides/MERGE-BAR.md`, the
  guide gov's charter sends a reader to for the bar, instead of `AGENTS.md`; one new arm asserts
  `AGENTS.md` names that guide. `MERGE-BAR.md` gains the `<git-dir>/gate-ledger.tsv` pointer it
  lacks. This also clears the canary's latent red: at BASE `AGENTS.md` names neither file. Observed
  by AC4.

## 3. Non-goals (OUT)

- A bare `§<n>` with no charter word beside it. It is indistinguishable from a citation of the
  citing document's own section; the stage's header says so, and TOOL-aDistilledCharter-4 re-points
  the bare ones by hand.
- Frozen records under `memory/builds/`, `memory/DECISIONS.md` and `memory/archive/`. They are not
  in the population.
- A new gate leg. S4 rides the existing `playbook parity` leg.

### Edges

- **consumes-from** `PLAY-aDistilledCharter-1` — the v4.0 text the pairs and the canary now read.
- **consumes-from** `TOOL-aDistilledCharter-4` — a clean surface, so S4 lands green and its red is
  observed on a staged break rather than on the tree.
- **hands-off** `TOOL-aDistilledCharter-6` — the S2 stage it narrowed, which that unit widens again

## 4. Design

### The population

`git ls-files` over `tools/`, `skills/`, `.githooks/`, `.claude/rules/`, `.claude/skills/`,
`memory/guides/`, `WIRE-INTO-PROJECT.md`, `README.md`, `AGENTS.md` and the template. The stage
asserts the population is non-empty and contains the template, the sentinel this gate's anti-vacuity
arm 2 already uses for its kit set.

### The predicate

Case-insensitive, per line:

```
\b(charter|template|playbook|governance)('s)?[^a-z0-9§]{0,3}§[0-9]+   a charter word, then a section
§1 Landing | §16 R1                                                   the two named v3.5 subsections
```

A line citing the SPEC template's own sections (`spec template's §8`) is excluded: it names
`TEMPLATE-SPEC.md`, whose numbered sections are real, and two live guides cite it that way. A
near-miss is `§[0-9]+` on a line of the population that is not a hit, the excluded lines among them;
it prints with its count so the stage visibly measured something on a clean tree. A hit names
`file:line` and the match.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| S4 stage | shell block | no new function; `fail` with a new number |

### Files touched (estimate)

`tools/check-playbook-parity.sh` · `tools/check-playbook-parity.test.sh` · `tools/run-gates/run-gates.gov.test.sh` · `memory/guides/MERGE-BAR.md`

### Alternatives rejected

- **A dead-anchor check resolving every `§<n>` against the cited document.** Most citations name
  no document, so the resolver would guess its target.
- **A separate leg.** A new guarded leg reds every live spec touching its guard
  (`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`); the parity leg already reads
  the template and the runbook.

## 5. Production-readiness checklist

- security — N/A — a read-only gate.
- perf / scale — one `git grep` over the population.
- error / empty / loading states — an empty population exits 2 rather than passing.
- observability — every hit is printed; the near-miss count prints on a clean run.
- risks — a citation of another document's section that happens to follow the word "template"
  reds; the remedy is to name the document, which is the better citation anyway.
- testing — new arms in `tools/check-playbook-parity.test.sh`; the canary's own arms.
- migration — none.
- user docs — the gate's header.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-playbook-parity.sh` runs over the v4.0 tree, S2 reports its pairs
  in agreement and names no retired pair. Red when: an extraction matches nothing.
- **AC2** — When a staged copy of `README.md` gains the line `see the charter's §7`, the gate fails
  naming that file and line; unstaged, it passes. Red when: the staged break passes.
- **AC3** — When `bash tools/check-playbook-parity.sh` runs over the clean tree it prints the
  near-miss count, a number above zero. Red when: the stage is silent.
- **AC4** — When `grep -c 'gate-ledger.tsv' memory/guides/MERGE-BAR.md` runs it counts at least one,
  and the canary's G4/G5 arms read that file. Red when: the canary still reads `AGENTS.md` for them.

## 7. Gates

`playbook parity` · `playbook parity selftest` · `run-gates gov canary` · `harness arms (fail branches armed or pinned)` · `dead-path carriers (deleted files still named)` · `recall floor` · `recall floor arms`

New arm: tools/check-playbook-parity.test.sh · covers AC1 AC2 AC3 · a fixture line citing a charter section by number · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §4 · AC2 · the predicate excludes citations of the spec template's sections,
  which TOOL-aDistilledCharter-4's sweep found live and correct.
- rev-3 · 2026-10-10 · §3 · the hands-off edge back to TOOL-aDistilledCharter-6, which the closing bar's
  check 12 found missing.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; the extended
seams are `check-playbook-parity.sh`'s existing `PAIRS` stage and its kit-coverage haystack, and the
canary's G4/G5 block in `tools/run-gates/run-gates.gov.test.sh`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
