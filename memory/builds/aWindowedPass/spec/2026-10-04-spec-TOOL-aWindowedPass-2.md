# TOOL-aWindowedPass-2 — a pass commit carries a `Pass:` trailer, and the legs attribute by it

**Status:** CLOSED · rev-5 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 2 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aWindowedPass-2-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aWindowedPass-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-2-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-2-2-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-aWindowedPass-1 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 |
| [2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round2.md](../reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-aWindowedPass-1 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

`pass_commit` (check 23, and the driver's `check_pass_open`) and `build_commit` (pass-order and
brief-recorded) find a unit's commit by the unit id appearing in a commit SUBJECT. A records commit
whose subject names a unit, or a range such as `-1..4`, is taken as that unit's pass, which is how
aHalvedInstall's brief commit counted as unit 1's undeclared write. This unit makes the attribution
structural: a commit trailer `Pass: <unit-id>` names a pass commit, and `Pass: none` names a commit
that is no pass.

## 2. Scope (IN)

- **S1** — `read_attribution_tokens` in `tools/unattended/lib-unattended.sh` prints one tokenised line
  per commit from one `git log` read: `PASSTRAILER <ids>` for a commit carrying a `Pass:` trailer, its
  subject's tokens otherwise. Both build-commit legs build their subject cache from it. Observed by
  AC3.
- **S2** — `pass_commit` and `build_commit` attribute PER COMMIT: a commit carrying any `Pass:`
  trailer is attributed by that trailer alone, so `Pass: none` names no unit and its subject is never
  read; a commit with no trailer is attributed by its subject as before, so a landed record keeps its
  verdict. Observed by AC1, AC2 and AC3.
- **S3** — `tools/workflows/unattended-unit.js` tells the child to end its pass commit with
  `Pass: <unit-id>` in the trailer block, and `Pass: none` on a commit naming a unit that is no pass.
  Observed by AC4.
- **S4** — The Skill's dispatch bullet and the verb carrier's `--dispatch` entry state the trailer.
  Observed by AC4.

## 3. Non-goals (OUT)

- Requiring the trailer at commit time is the commit-time step's job (`TOOL-aWindowedPass-3`).
- No rewrite of landed history; legacy walks keep subject attribution.

### Edges

- **hands-off** `TOOL-aWindowedPass-3` — the commit-time step reads the same trailer reader.
- **hands-off** `TOOL-aWindowedPass-1` — the overlap test reads the pass commits this unit picks.

## 4. Design

### Data model

```bash
read_attribution_tokens HEAD   # <sha> PASSTRAILER TOOL-x-1   or   <sha> <subject tokens>
```

In `pass_commit`, the existing `%H%x09%s` walk appends `%x1f%(trailers:key=Pass,valueonly)`, so the
trailer rides the same single spawn. `build_commit` reads the callers' cache, which
`read_attribution_tokens` builds, and calls it for a single commit on a cache miss.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/workflows/unattended-unit.js`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`

### Alternatives rejected

- **Tightening the subject match.** A subject is prose a commit author writes for people; any rule
  over it is another substring rule with a new edge.
- **Recording pass shas in the run-state file.** The commit graph already carries the claim if the
  commit carries it; a second record would be a second answer.

## 5. Production-readiness checklist

- security — N/A: attribution only.
- perf / scale — no new spawn: the trailer rides the existing walk.
- error / empty / loading states — a commit with no trailer falls back to its subject, unannounced.
- observability — none added: attribution is per commit, so no walk-level mode exists to report.
- risks — a non-canonical trailer spelling; one token rule reads it alike at commit time and at
  the close.
- testing — fixture arms for structural, legacy and `Pass: none`.
- migration — none: landed records stay legacy.
- user docs — the Skill and verb carrier name the trailer.

## 6. Acceptance criteria

- **AC1** — When `pass_commit` walks a fixture window holding a `Pass: none` records commit whose
  subject names the unit, then a `Pass: TOOL-x-1` commit, it returns the second.
  Red when: the walk still matches the subject in a structural window.
- **AC2** — When the window carries no trailer at all, `pass_commit` returns the first subject match,
  as at base.
  Red when: legacy windows lose subject attribution.
- **AC3** — When `build_commit` walks the same structural fixture, it returns the trailered commit.
  Red when: `build_commit` keeps the subject-only walk.
- **AC4** — When `grep -c 'Pass: <unit-id>' tools/workflows/unattended-unit.js` runs, it prints at
  least 1, and the rendered `SKILL.md` names the trailer.
  Red when: the harness still asks for the id in the subject alone.

## 7. Gates

`unattended kit gate` · `brief-recorded` · `pass-order history` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test`

New arm: tools/unattended/check-unattended.test.sh · structural, legacy and `Pass: none` windows · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's part (4) and `pass_commit` and `build_commit` at base.
- rev-2 · 2026-10-04 · build pass · S1 · S2 · S3 · §4 · attribution is per COMMIT, not per walk: a
  walk-wide switch would flip a landed build's verdict the moment a later trailered commit entered
  its range, since `build_commit` walks to HEAD. The build harness carries no commit text of its own,
  so only the unit harness changes; the two legs' caches move to the shared token producer.
- rev-3 · 2026-10-04 · closing review r1 · M3 · L2 · L6 · §5 · one token rule for every trailer reader: ids split on
  any non-id character and a `none` anywhere attributes the commit to nothing; check 23's ambiguity
  test reads a trailered commit's trailer, not its subject; §5 struck the per-walk announcement and
  attribution line, which the per-commit design never needed.
- rev-4 · 2026-10-04 · closing review r2 · S1 · M8 · `read_attribution_tokens`'s `none` rule has a `build_commit` arm,
  observed red with the rule removed.
- rev-5 · 2026-10-04 · close · §4 · S1 · the token producer is renamed `read_attribution_tokens`, since the lexicon
  leg declares `read` and not `log`; behaviour unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "attribute a commit to a pass by a trailer"` ranked
name-stem neighbours only and printed `unscanned layers: .sh`. Extended: `pass_commit` and
`build_commit` in `tools/unattended/lib-unattended.sh`, whose single-walk shape TOOL-aQuenchedHarness-7
measured; `id_in` stays for legacy walks.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
