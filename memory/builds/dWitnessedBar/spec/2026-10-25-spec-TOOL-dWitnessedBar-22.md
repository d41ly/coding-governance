# TOOL-dWitnessedBar-22 — the `tests=` and `enforces=` edge fields on legs

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 6 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0360@f873b4dc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

Declare on each leg's own row what the leg tests and which principles or practices it enforces, and
read both as typed edges of the one closed edge set, so the facts "this leg tests that feature" and
"this leg enforces that principle" are declared once, where the leg lives, and every inverse is
derived (night pass, point 4: `night-pass.md:250`). Today no leg carries either field, and the
feature-to-leg fact lives only in the dossiers' `gate-legs` claims.

## 2. Scope (IN)

- **S1** — The row key `tests` (shared interface I1): a list of tags, each a thing the leg tests.
  Written once at the pass from the dossiers' claims, per §4 "The `tests` values", on each manifest
  row of `tools/gate-legs.json` and on its descriptor `[[gate_leg]]` row; declared there thereafter.
  Observed by AC1.
- **S2** — The row key `enforces`, PLAY-dOrderedCharter-7 S2's: a list of `principle.*` or
  `practice.*` tags. This unit makes it an edge field read at the leg row; the values for every leg
  are TOOL-dWitnessedBar-11's and TOOL-dWitnessedBar-24's to write. Observed by AC3.
- **S3** — `LEG_KEYS` (TOOL-dWitnessedBar-12's one key set) gains `tests`, and `enforces` where
  PLAY-dOrderedCharter-50 S1 has not already put it there. Observed by AC2.
- **S4** — The leg-row site of the edge grammar: one adapter `read_leg_edges` in
  `tools/playbook/edge_grammar.py`, a row of PLAY-dOrderedCharter-28 S5's site table, yielding a
  `tests` edge and an `enforces` edge from the row's `tag` to each value, resolved through
  PLAY-dOrderedCharter-19's resolver; a `tests` target in a namespace no build has registered yet is
  counted and printed `unarmed`, never yielded as resolved and never red. Observed by AC3 and AC4.
- **S5** — The both-ways compare in `tools/run-gates/run-gates.gov.test.sh`: a leg whose row
  carries `feature.<f>` in `tests` is claimed by the dossier whose `feature` is `<f>`, and a leg a
  dossier claims carries that dossier's tag in `tests`. The dossiers are read, never edited.
  Observed by AC5.
- **S6** — govkit selfcheck 7h's both-ways join gains `tests` and `enforces`: a descriptor row and
  its manifest row carry the same lists. Observed by AC6.

## 3. Non-goals (OUT)

- The `enforces` key's creation and its meta-check: PLAY-dOrderedCharter-7 S2 and S3. The value
  "every leg declaring the principles it enforces" is TOOL-dWitnessedBar-11's; the portability
  pack's values are TOOL-dWitnessedBar-24's.
- The edge registry, the parser and the resolver: PLAY-dOrderedCharter-24, -28 and -19.
- The dossiers' `[claims] gate-legs` lists and the `feature` namespace: the map's and dTotalRecall's.
  This unit compares against them and edits none; making the dossier side derived from `tests` is
  the ask named in §8 F2.
- Carrying `tests` or `enforces` into an adopter's manifest: neither travels (§8 F4), so
  `LEG_KEY_FLOORS` gains no row for them.
- Reading a leg's own files from its `tests` edge: TOOL-dWitnessedBar-21's (shared interface I15).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-12` — `tag`, the leg's address every edge this unit reads
  starts from, its `leg.<owner>.<name>` member the form a `tests` target and an `enforces` row's leg
  are spelled in, and `LEG_KEYS`, where the key is admitted
- **hands-off** `TOOL-dWitnessedBar-11` — `enforces`, the edge field the leg factory emits from each
  pack's declaration and whose values for every leg it writes
- **hands-off** `TOOL-dWitnessedBar-24` — `enforces`, the field its portability legs fill with
  `practice.portable.*` tags
- **hands-off** `TOOL-dWitnessedBar-21` — `tests`, the edge a leg's own files are read through
- **consumes-from** external — PLAY-dOrderedCharter-7 S2 (the `enforces` key),
  PLAY-dOrderedCharter-24 (the `tests` and `enforces` edge rows) and -28 S5 (the site table)
- **hands-off** external — dTotalRecall: registering the `feature` namespace, which arms the
  `tests` edges' resolution, and deriving the dossiers' `gate-legs` claims from them
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 12 and 41: `fix_keeps.py` keeping no `tests` target, and the row hash dropping the `tests` and `enforces` keys, each a scope item of that unit

## 4. Design

### The `tests` values

At `cdfbd1cf`, 122 of the 142 legs are claimed by exactly one dossier under `memory/map/features/`,
in its `[claims] gate-legs` list, and 20 by none, those 20 being map baseline debt in
`memory/map/baseline.toml` (PINNED, measured 2026-10-25 by a probe over the dossiers' fenced TOML).
Each claimed leg's row gains `"tests": ["feature.<f>"]`, `<f>` the claiming dossier's `feature`
value. An unclaimed leg carries no `tests` key: a value the rule cannot derive is not guessed.

The key is declared at the leg from then on. A new leg states its own `tests`; a dossier that claims
it must agree, which S5 checks until dTotalRecall derives the claim from the edge.

### The edge read

```python
read_leg_edges(manifest_rows) -> [(type, from_tag, to_tag)]
# ("tests",    "leg.branch-reconcile.branch-reconcile-selftest", "feature.branch-reconcile")
# ("enforces", "leg.playbook-render.tags-the-resolver-s-checks", "principle.p33")
```

The adapter reads only the manifest's rows, keyed by each row's `tag` (TOOL-dWitnessedBar-12). The
edge checks of PLAY-dOrderedCharter-28 S8 then parse, type and resolve each yielded edge. The
`tests` row admits any target (PLAY-dOrderedCharter-24: `tests`, any to any), but a namespace word
not yet registered "admits nothing until its build registers it", so the adapter withholds an edge
whose target namespace is not in the registry and prints
`edges: <n> tests edges to feature.* unarmed until the feature namespace is registered`.

`enforces` follows the leg-row grammar of PLAY-dOrderedCharter-7 S2: its targets are `principle.*`
and `practice.*`. PLAY-dOrderedCharter-24's `enforces` row admits `unit` or `practice` in `to`, so a
`principle.*` target would red there. Where that row still lacks `principle` at the build run, this
unit's pass widens its `to` to `["unit", "practice", "principle"]` in `tools/playbook/edges.toml`
(§8 F1), the one-row change the ask in §8 F1 requests of dOrderedCharter.

### Inventory

Minted: the row key `tests` and its 122 values, `read_leg_edges`, the gov canary's compare arm, the
`LEG_KEYS` entry, the 7h join of both keys. Naming cells: `read_leg_edges` is asked of the
lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

Additive. No adopter row changes; no name-keyed file moves.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/playbook/edge_grammar.py`
- `tools/playbook/edges.toml` (the `enforces` row's `to`, only where §8 F1's ask has not landed)
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- the 26 descriptors carrying `[[gate_leg]]` rows, as TOOL-dWitnessedBar-12 lists them:
  `tools/agent-instructions/kit.toml`, `tools/branch-reconcile/kit.toml`,
  `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`, `tools/gate-lint/kit.toml`,
  `tools/lexicon/kit.toml`, `tools/memory-recall/kit.toml`, `tools/memory-tree/kit.toml`,
  `tools/playbook/kit.toml`, `tools/process-monitor/kit.toml`, `tools/roles/kit.toml`,
  `tools/run-gates/kit.toml`, `tools/runlog/kit.toml`, `tools/unattended/kit.toml`,
  `tools/workflows/kit.toml`, `tools/govkit/entries/check-agent-cap-restatement.kit.toml`,
  `tools/govkit/entries/check-install-prefix.kit.toml`,
  `tools/govkit/entries/check-kit-versions.kit.toml`,
  `tools/govkit/entries/check-line-length.kit.toml`,
  `tools/govkit/entries/check-microformats.kit.toml`,
  `tools/govkit/entries/check-placeholders.kit.toml`,
  `tools/govkit/entries/check-testsuite-counts.kit.toml`,
  `tools/govkit/entries/check-wiring.kit.toml`, `tools/govkit/entries/kickoff-manifest.kit.toml`,
  `tools/govkit/entries/push-main.kit.toml`, `tools/govkit/entries/settings-merge.kit.toml`

### Alternatives rejected

- **`tests` targets as `kit.<id>` tags.** The owner kit is already the tag's second segment, so the
  value would restate the tag; the feature a leg tests is the fact the dossiers hold.
- **Declare on both sides with no compare.** Two spellings of one fact with no gate is what the
  night pass's point 4 forbids.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one pass over the manifest's rows and the 31 dossiers' fences.
- error / empty / loading states — an unregistered target namespace prints `unarmed` with its count;
  a compare miss names the leg, the dossier and the side that disagrees.
- observability — the edges check's summary carries the leg-row site's edge counts.
- risks — 122 `tests` edges stay unresolved until dTotalRecall registers `feature`; the compare
  arm is what holds them meanwhile.
- testing — AC1 to AC6 by a pass; the arms of §7 at the close.
- migration — additive.
- user docs — none under `help/`; `tools/run-gates/README.md` names `tests` beside `tag` at the pass.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` after the pass, every leg a dossier claims
  carries `tests` equal to `["feature.<f>"]` for its claiming dossier, and no unclaimed leg carries
  the key.
  Red when: a value is guessed for an unclaimed leg, or a claimed leg's value names another feature.
  figure: 122 and 20 are PINNED at `cdfbd1cf`; the probe re-derives both from the dossiers.
- **AC2** — When the canary's key-set arm runs over a fixture manifest row carrying `tests` and
  `enforces`, it passes; with `tests` cut from `LEG_KEYS`, it fails.
  Red when: the manifest carries a key the canary does not admit.
- **AC3** — When `read_leg_edges` is called from `edge_grammar.py` on a fixture manifest holding a
  row with tag `leg.x.y`, `"tests": ["kit.x"]` and `"enforces": ["principle.p16"]`, it returns the
  `tests` edge to `kit.x` and the `enforces` edge to `principle.p16`, and the edges check resolves
  both in a fixture registry holding both tags.
  Red when: an `enforces` target `principle.*` is refused, or an edge is keyed by `name`.
- **AC4** — When the same call reads a row whose `tests` holds `feature.x` and the fixture registry
  has no `feature` namespace, the edge is withheld and the line
  `edges: 1 tests edges to feature.* unarmed` is printed, with the check's exit 0.
  Red when: the edge is reported resolved, or reds before dTotalRecall registers the namespace.
- **AC5** — When the gov canary's compare arm runs over a copy of the manifest with one claimed
  leg's `tests` emptied, it names that leg and its dossier; with a dossier's claim added for a leg
  whose `tests` does not name it, it names that pair too.
  Red when: the compare reads one direction only.
- **AC6** — When `govkit.py selfcheck` runs over a fixture whose descriptor row's `enforces`
  differs from its manifest row's, check 7h names the leg and both lists.
  Red when: the descriptor and the manifest disagree unseen.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `measure-legs selftest` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `agent-instructions self-test` · `branch-reconcile selftest` · `drift-audit selftest` · `lexicon selftest` · `pre-push run-log line` · `review-join self-test` · `run-gates run-log line` · `runlog selftest` · `shell-hygiene selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `memory hygiene`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC5 · the `tests`-to-claims compare, staged by one claimed leg's `tests` emptied · that suite's arm count
New arm: tools/playbook/edge_grammar.py · covers AC3 AC4 · the leg-row site under the edge checks' fixture, staged by `read_leg_edges` keying edges by `name` · none
New arm: tools/govkit/selftest.py · covers AC6 · 7h's `tests` and `enforces` join, staged by one descriptor list changed · none

## 8. Open questions

- **F1 — Which targets does `enforces` admit on a leg row?** PLAY-dOrderedCharter-7 S2 admits
  `principle.*` and `practice.*`; PLAY-dOrderedCharter-24's edge row admits `unit` or `practice`.
  Options: (a) follow -7 S2, the leg-row grammar, and widen -24's row `to` to admit `principle`;
  (b) follow -24 and drop `principle.*` from legs; (c) a second edge type for legs. (b) breaks
  -7 S3's meta-check, which joins principles to legs through `enforces`, and the clause of unit 11
  ("every leg declaring the principles it enforces"); (c) adds a type to the closed set.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the brief's direction; the ask for
  PLAY-dOrderedCharter-24's row is named in this unit's return, and the pass widens the row only
  where the ask has not landed. widens: none · relaxes: none
- **F2 — Where is `tests` declared, given the dossiers already claim legs?** Options: (a) the leg
  row, values derived once from the claims, a both-ways compare until the map derives its side;
  (b) the dossiers only, the edge derived from them; (c) both, with no compare. The clause and night
  pass point 4 put a leg's edges in "a leg's fields"; (b) keeps the fact away from its site; (c) is
  two spellings with no gate. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, the night pass's
  "declared once, where the fact lives"; the ask that dTotalRecall derive the dossiers' `gate-legs`
  claims from `tests` is named in this unit's return. widens: none · relaxes: none
- **F3 — Shared interface I15 reads "the targets of its `tests` edge" as a leg's own files; is a
  `tests` target the leg's own test file or the thing it tests?** Options: (a) the thing tested, the
  direction PLAY-dOrderedCharter-24's `tests` row and its text form (`tests=kit.y,kit.z`) give;
  (b) the leg's own suites. Under (a), excluding `tests` targets from a fix pass's allowance would
  fence the product code the pass must fix; under (b), the edge points the wrong way for every
  other site. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, -24's row; the reading of I15 is
  named in this unit's return for TOOL-dWitnessedBar-21's writer, whose own files are the argv's
  files and the gate script. widens: none · relaxes: none
- **F4 — Do `tests` and `enforces` travel into an adopter's manifest?** Options: (a) no: both name
  gov-side registries (gov's dossiers, its principle rows), and an adopter's legs arrive through
  their overlay (TOOL-dWitnessedBar-28); (b) yes, behind a `LEG_KEY_FLOORS` row each. (b) ships
  edges whose targets an adopter's registry may not hold. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 22, the brief's shared interfaces I1,
  I2 and I15, scout B's row for cl-0360, night pass point 4, PLAY-dOrderedCharter-7, -24 and -28,
  and the dossiers and manifest read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-7 S2's `enforces` key, PLAY-dOrderedCharter-24's edge
rows and parser and -28 S5's site table with its adapters in `tools/playbook/edge_grammar.py`, all
specced and DEFERRED; TOOL-dWitnessedBar-12's `LEG_KEYS` and leg tags; govkit selfcheck 7h
(`tools/govkit/govkit.py:2785`); and the dossiers' `[claims] gate-legs` lists, read by the map's
`_gate_legs` extractor (`tools/codebase-map/map_extractors.py:176`). The lookup
`python tools/codebase-map/reuse_lookup.py "declare which feature a gate leg tests"` with the words
`and which principles it enforces` appended ranked generic `leg`, `legs` and `declares` stems and
named no seam, as expected with neither key built. One disagreement with scout B: it gives the
dossiers' leg claims as front matter `gate-legs = [...]`; at `cdfbd1cf` they sit in each dossier's
fenced TOML under `[claims]`, 122 legs claimed once and 20 unclaimed. The recall probe returned
scout B's row and the brief's settle-in-§8 instruction; none disagreed with source otherwise.

Recall terms used: `python tools/memory-recall/query.py "how are the tests and enforces edges declared on a gate leg row" --terms "tests enforces edge field leg row gate-legs.json dossier gate-legs claims principle practice edge grammar"`
