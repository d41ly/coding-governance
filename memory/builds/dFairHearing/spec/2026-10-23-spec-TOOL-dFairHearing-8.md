# TOOL-dFairHearing-8 — fix verdicts judged by class behind a switch, and every confirmed finding given one disposition from the report's grammar

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 10 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0075@8c43970c whole
**Carries:** node:item.review.report
**Carries:** node:policy-key.review.unclassed

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

Proposed gates have no home and left-shift has no witness: 56% of 721 proposed gates name nothing,
724 of 907 confirmed findings carry no class, and two round-2 reports re-found a defect whose fix had
covered the instance and not the class (gap-review-07, gap-review-10). This unit lets the skeptic
judge a fix by its class, behind a default-off switch until TOOL-dFairHearing-1's replay decides, and
gives every confirmed finding one disposition from `review.report`'s grammar, `class:`, `new:`,
`gate:` or `none` under `review.unclassed`, checked against the leg manifest and the class slugs the
harness hands over and written to the review record.

## 2. Scope (IN)

- **S1** — The switch. `tools/workflows/tier2-review.template.js` takes `fixJudge`, a closed set
  `instance` and `class`, default `instance`, refused outside it in the shape `intensity` takes.
  Observed by AC1.
- **S2** — The class judge. Under `class` the skeptic's fix question asks whether applying the fix
  cures the defect's class, every instance of the pattern the claim names in the subject and the
  code or specs it reaches, and `FIX_VERDICTS` gains `instance`: the fix cures the cited instance and
  leaves another of its class standing, with `fixNote` holding the class-level fix. `instance` is
  accepted only under `class`; under `instance` it reads as unjudged. `renderFixLine`,
  `confirmedFindings`, the fix counts and the RUN INTEGRITY line carry it, and a fix judged
  `instance` with a note gives way to that note, as an unsound one does. Under `instance` every verify
  prompt is byte-identical to today's, and `fixJudge` joins the review key's print only under
  `class`. Observed by AC2 and AC3.
- **S3** — The `review.unclassed` stand-in. The harness takes `unclassed`, the policy key
  `review.unclassed` with v2's values `refuse`, `reason` and `owner-rules` and its default `refuse`,
  refused outside the set. It is passed directly as a pin argument through `review.pin` until
  dDeclaredLoop's `review.trigger` lands: `tools/workflows/review_pin.py`, TOOL-dFairHearing-3's
  stand-in, takes `--unclassed <value>` and prints it as the `unclassed` argument in its JSON line,
  checking its shape only. Observed by AC4.
- **S4** — The leg manifest. The harness takes `legManifest`, a repo-relative path refused on the
  rule `specs` members are refused by, defaulting to `{{TOOL_ROOT}}gate-legs.json`, rendered at
  install. The resume probe reads it and returns `legs`, the `name` of every object in its top-level
  array, and omits `legs` when the file is absent or not such an array. With no `legs`, the run says
  so in its log and RUN INTEGRITY and refuses every `gate:` disposition. Observed by AC5.
- **S5** — The class slugs the harness hands over are the checklist items' slugs, read by the rule
  `extractFindingClasses` already applies (:1570-1583); a `C<n>` label with no slug is no class.
  Observed by AC6.
- **S6** — The report step. The synthesis is handed the grammar, the leg names, the class slugs and
  the `unclassed` value, and returns `dispositions`, one `{id, disposition, reason}` per confirmed id,
  the field required by its schema. Observed by AC6.
- **S7** — The check. The harness accepts the set only when every confirmed id has exactly one
  disposition; each is `class:<slug>` with a handed slug, `gate:<leg>` with a handed leg name,
  `new:<slug>` with a slug in the class grammar that is no handed slug, or `none`; and `none` appears
  only under `reason` or `owner-rules`, with a non-empty `reason`. Otherwise it refuses the set: the
  return's `dispositions` is `null`, `dispositionFault` names each failing id and why, and the note
  says so, while `blockers` and `highs` keep their own derivation. Under `owner-rules` the return's
  `ownerItems` lists every id disposed `none`. Observed by AC7 and AC8.
- **S8** — The record. The appendix gains a tenth column, `disposition`, after `classes`. The harness
  renders each confirmed row's cell as `(synthesis)` and every other row's as `-`, and the synthesis
  is told to copy the appendix verbatim but for those cells, each written with the disposition it
  returns, a `none` as `none — <reason>`. The return's `appendix`, `ledger` and `confirmedFindings`
  carry the accepted dispositions, and `-` in every cell when the set was refused. Observed by AC9.
- **S9** — The kit's own records. `tools/workflows/README.md` states the three arguments and the new
  return fields, and the appendix's ten columns. `tools/workflows/kit.toml` declares `TOOL_ROOT` among
  the review harness render's placeholders, and the render is refreshed. The template's `version:`
  moves once against its value at base `3708a705` if no earlier unit of this build moved it. Observed
  by AC10 and AC11.

## 3. Non-goals (OUT)

- Routing the dispositions: filing each `new:` class, turning a `gate:` into an intake, raising an
  owner item for a `none`. That is dDeclaredLoop's `review.dispose`, and this unit is its stand-in:
  the dispositions are written to the review record and returned.
- Claiming a `new:` slug on the remote (`refs/gov/class-claims/<slug>`), and joining a `class:` slug
  to its record under the memory tree. The harness has no filesystem and no remote; the slugs it
  hands over come from the checker that read those records.
- Flipping `fixJudge`'s default. TOOL-dFairHearing-1's replay re-judges aRoutedQuill #23's fix and
  owns the verdict (the brief's S9).
- The diff skeptic's duplicate reason form, TOOL-dFairHearing-5's.
- The synthesizer role's input line, which TOOL-dFairHearing-10 brings in line.
- Reading the dispositions downstream: the brief's S7 names TOOL-dFairHearing-9 and
  TOOL-dFairHearing-15 as their readers, and neither declares an edge to this unit at this writing,
  so none is declared here; the return fields in section 4 are what either reads.

### Edges

- **consumes-from** `TOOL-dFairHearing-11` — the resume probe's declared stage and type, which S4 extends with the leg read; without it the probe this unit widens is the untyped one
- **consumes-from** `TOOL-dFairHearing-3` — `review_pin.py`, the `review.pin` stand-in this unit extends with the `review.unclassed` pin argument; without it the key reaches the harness only from a hand-written call
- **hands-off** `TOOL-dFairHearing-1` — the replay that re-judges aRoutedQuill #23's fix with the class judge switched on, and whose verdict sets the switch's default
- **hands-off** `TOOL-dFairHearing-10` — the synthesizer role's input line names the leg names, the class slugs and the disposition grammar it is handed
- **hands-off** external — dDeclaredLoop's dispose step routes each disposition; dPlacedRequest's claim ref makes a new slug unique across branches
- **hands-off** `TOOL-dFairHearing-23` — finding ids 5, 6, 9, 24, 31, 43 and 44 of the round-1 spec audit: AC4 run with a `--subject` (its S11, AC5), the version half of S9 and AC11 superseded by the lander's mint (its S12, S13, AC6), the `TOOL_ROOT` row kept this unit's (its S38, AC29), the argument named `gateManifest` (its S44, AC35), a leg count beside the probe's legs (its S31, AC22) and reason cells kept on one line (its S32, AC23)

## 4. Design

### Evidence

- The skeptic's fix question is one paragraph with three verdicts (`FIX_VERDICTS`, :670; the prompt at
  :1419-1426), judged against the instance the finding cites.
- `renderFixLine` (:1492-1503), the fix counts (:1535-1543) and `confirmedFindings` (:1607-1613) are
  the three readers of a fix verdict, and each tests membership in `FIX_VERDICTS`.
- The appendix has nine columns, `classes` last (:1629-1635), and `review_replay.py` finds columns by
  header name (its docstring, line 20), so a tenth column moves none of its reads.
- The harness has no filesystem (:614-618), and the resume probe is the one agent that reads files
  for it (:1004-1044). `tools/gate-legs.json` is a top-level array of 142 objects each carrying `name`
  (measured 2026-10-23 at base).
- The drift-audit state harness already defaults a leg-manifest argument to
  `{{TOOL_ROOT}}gate-legs.json` (`tools/workflows/drift-audit-state.template.js:78`), and the renderer
  substitutes every token into every template it pairs (`tools/workflows/kit.toml`, the comment above
  the review harness's render rule).
- The disposition grammar and its witness are the flow-steps row of `review.report`
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:573`) and the
  library layer's left-shift section (`2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:179-194`);
  the class-level fix verdict is the review system's `[adjudication]`
  (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:236-249`).

### Mechanism

The skeptic's class question is a second prompt variant of the fix paragraph, selected by `fixJudge`,
so the `instance` variant keeps today's bytes. The probe's prompt gains one numbered step reading the
manifest, and its schema an optional `legs` array of strings. A dead probe reads as no `legs`.

The synthesis prompt gains a DISPOSITIONS block after the RUN INTEGRITY block: the four forms, the
`unclassed` value and what it admits, the class slugs, and the leg names, or the sentence that no leg
manifest was read and `gate:` is refused. Its schema gains `dispositions`, an array of objects
requiring `id` and `disposition`, `reason` optional. The check runs after the tally, over confirmed ids
only, and a disposition naming an id that is not confirmed is a fault. The slug grammar is the one
`extractFindingClasses` reads, `[a-z][a-z0-9]*(-[a-z0-9]+)*`, held in one constant both read.

### Data model

| Field | Where | Shape |
|---|---|---|
| `fixJudge` | argument | `instance` or `class` |
| `unclassed` | argument | `refuse`, `reason` or `owner-rules` |
| `legManifest` | argument | a repo-relative path |
| `legs` | probe return | an array of leg names, or absent |
| `dispositions` | synthesis return and harness return | `[{id, disposition, reason}]`, or `null` when refused |
| `dispositionFault` | harness return | `''`, or the failing ids and why |
| `ownerItems` | harness return | the ids disposed `none` under `owner-rules` |
| `disposition` | ledger entry, confirmed finding, appendix column | the accepted disposition, or `-` |

### Inventory

Names this unit mints: the arguments `fixJudge`, `unclassed` and `legManifest`; the fix verdict
`instance`; the probe field `legs`; the return fields `dispositions`, `dispositionFault` and
`ownerItems`; the appendix column `disposition`; the placeholder cell `(synthesis)`. No naming cell
grades them.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (the render, by `check-protocol-parity.test.sh --render`)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/kit.toml`
- `tools/workflows/review_pin.py` (TOOL-dFairHearing-3's stand-in, the `--unclassed` argument only)

### Rollout

`fixJudge` ships dark at `instance` (charter `[small]`). The dispositions ship live: a synthesis that
cannot home a finding names it `new:<slug>`, so the default `refuse` always leaves a legal disposition,
and a refused set leaves the counts and the run's exit as they are.

### Alternatives rejected

- **The skeptic assigning the disposition.** It would let the harness render the column before the
  synthesis, but the grammar is the report step's (section 8 F1).
- **Nulling `blockers` and `highs` on a refused set.** Every caller reads a null count as a degraded
  run and stops, so one unhomed finding would halt an audit stage (section 8 F3).
- **The caller passing the leg names.** Each caller would re-read the manifest the probe can read once
  (section 8 F4).

## 5. Production-readiness checklist

- security — `legManifest` reaches a prompt line and is refused on the `specs` rule (no absolute, `~`,
  drive-lettered, backslashed or `..` path, no control character), so it cannot point the probe
  outside the repository or forge a prompt line.
- perf / scale — the probe reads one file more; the synthesis prompt grows by the leg names, about
  142 short lines here.
- error / empty / loading states — no checklist means no class slug and every class disposition is
  `new:` or `gate:`; no manifest means `gate:` is refused and announced; a refused set is named and
  never silently dropped.
- observability — RUN INTEGRITY states the leg source and count, the class slug count, the
  `unclassed` value and, under `class`, the instance-only count; the return carries every field above.
- risks — the synthesis may mis-copy a disposition cell; the return's `appendix` is the source a caller
  compares the record against, as it is for every other appendix cell today.
- testing — AC1 to AC11 as stub-agent probes and greps; the new suite arms under section 7.
- migration — none: absent arguments keep today's fix judge, and the appendix column is additive for
  every reader that finds columns by header name.
- user docs — `tools/workflows/README.md`; no page under `help/` names the fix verdict or the appendix.

## 6. Acceptance criteria

The probe is `$SCRATCH/t2-stub.js`, written by the pass under its scratch directory: it evaluates its
first argument as an AsyncFunction with stub `agent`, `parallel`, `phase` and `log` globals and its
second argument as `args`, the shape `tools/workflows/tier2-review.test.sh` uses, records each agent
call's label, prompt and options, and answers each from a canned table its third argument names.

- **AC1** — When `node "$SCRATCH/t2-stub.js" tools/workflows/tier2-review.js '{"repo":"/r","base":"aaaaaaa","fixJudge":"both"}'`
  runs, it throws naming `fixJudge` and its two values; with `instance`, with `class` and with the key
  absent it starts.
  Red when: an unknown value is defaulted instead of refused.
- **AC2** — When the probe runs with `fixJudge` absent, every skeptic prompt equals the one the render
  at the pass's starting commit builds for the same args, and with `class` each carries the class
  question and the verdict `instance`; the two runs' `key` values differ, and the absent run's equals
  the starting render's.
  Red when: the dark default moves a prompt byte or the key.
  fixture: the starting render, read with `git show 'HEAD:tools/workflows/tier2-review.js'` before the
  pass commits.
- **AC3** — When a `class` run's skeptic stub answers one confirmed finding `fixVerdict` `instance`
  with a note, its `confirmedFindings` entry's `fix` is the note and RUN INTEGRITY counts one
  instance-only fix; the same answer under `instance` counts the fix as not judged.
  Red when: `instance` is accepted under the dark default, or its note is dropped.
- **AC4** — When the probe runs with `{"unclassed":"maybe"}` it throws naming `unclassed` and its
  three values; absent, the synthesis prompt states `refuse`; and
  `python 'tools/workflows/review_pin.py' --unclassed reason` prints a JSON line whose `unclassed` is
  `reason`.
  Red when: the key is defaulted on a bad value, or the stand-in drops the argument.
- **AC5** — When the probe runs with `'{"legManifest":"../x.json"}'` it throws naming `legManifest`;
  with the key absent, the probe's prompt names the manifest at the rendered default, here
  `tools/gate-legs.json`; and when the probe stub returns no `legs`, the log and the synthesis prompt
  say no leg manifest was read and a synthesis stub answering `gate:memory hygiene` is refused.
  Red when: the default reaches the prompt unrendered, or a `gate:` passes with no legs.
- **AC6** — When the probe runs with a checklist of two slug-led items and one item with no slug, and
  the probe stub returns `legs` `["memory hygiene"]`, the synthesis prompt lists the two slugs, the one
  leg and the four forms, and its schema requires `dispositions`.
  Red when: a `C<n>` label is handed as a class, or the schema leaves the field optional.
- **AC7** — When the synthesis stub answers `class:<a handed slug>`, `gate:memory hygiene` and
  `new:fresh-class` for three confirmed ids, the return's `dispositions` lists the three and
  `dispositionFault` is `''`; answering `class:C3`, `gate:no such leg`, `new:<a handed slug>`, a
  repeated id, an id not confirmed, or one confirmed id with none, each makes `dispositions` `null`,
  `dispositionFault` name the id, and `blockers` keep the value the items give.
  Red when: any one of the six planted faults is accepted, or a fault nulls the counts.
- **AC8** — When the synthesis stub disposes a confirmed id `none` with a reason, the set is refused
  under `refuse`, accepted under `reason`, and accepted under `owner-rules` with `ownerItems` naming
  the id; `none` with an empty reason is refused under all three.
  Red when: `none` passes under the default, or passes with no reason.
- **AC9** — When a run with two confirmed findings and one refuted finding reaches the synthesis, the
  appendix in its prompt has ten columns ending `classes | disposition`, the confirmed rows' last cell
  reads `(synthesis)` and the refuted row's `-`; after an accepted set the return's `appendix` carries
  the two dispositions in that column.
  Red when: the column is absent, sits before `classes`, or the return's appendix keeps the placeholder.
- **AC10** — When `python tools/workflows/review_replay.py --known "$SCRATCH/k.md" --candidate "$SCRATCH/k.md"`
  runs over a spec-audit record holding a ten-column appendix, it scores and exits 0.
  Red when: the replay scorer reads the tenth column as a malformed table.
- **AC11** — When `grep -n "TOOL_ROOT" tools/workflows/kit.toml` runs, the review harness's render rule
  lists it; `grep -n "gate-legs.json" tools/workflows/tier2-review.js` prints the rendered default; and
  `grep -m1 "version: " tools/workflows/tier2-review.template.js` prints a version other than
  `git show '3708a705:tools/workflows/tier2-review.template.js' | grep -m1 "version: "` does.
  Red when: the token reaches the render unsubstituted, or the kit's version never moved over the
  build.
  figure: the base version, `1.53`, is pinned, read from the template at base `3708a705` on 2026-10-23.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `verifier fan-out` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit-placeholders self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · stub runs over each planted disposition fault, the dark and the class fix judge, and a probe returning no legs · FLOOR_ASSERTIONS raised by the arms added, from its value at dispatch

## 8. Open questions

- **F1 — Who assigns a finding's disposition: the skeptic or the synthesis?** (a) The synthesis, at
  the report step. (b) Each skeptic, beside its fix verdict, so the harness renders the column before
  the synthesis. The clause gives every confirmed finding a disposition "from `review.report`'s
  grammar" and writes "the report's dispositions" to the record, and the flow-steps row of
  `review.report` names the synthesizer; (b) departs from both. Recommendation (a). Rung 1. RESOLVED
  (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — How does a column the synthesis decides reach an appendix the harness renders?** (a) The
  harness renders a placeholder cell per confirmed row and the synthesis fills those cells only, the
  return's appendix carrying the checked values. (b) A separate dispositions section in the report,
  outside the appendix. (c) A second agent writing the record after the check. (b) departs from the
  brief's S7, which puts the column in the appendix after `classes`, and (c) adds a spawn and a stage.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes:
  none
- **F3 — What does refusing a synthesis output with an unhomed finding refuse?** (a) The disposition
  set alone: `dispositions` null and named, the counts kept. (b) The whole output, as the tally fault
  does: `blockers` and `highs` null. (b) halts every audit stage and closing review whose synthesis
  slips once, since the build harness reads a null count as a degraded run, which costs the review's
  verdict for a record defect. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated):
  (a). widens: none · relaxes: none
- **F4 — How does a harness with no filesystem learn the leg names?** (a) The resume probe reads
  `legManifest` and returns them. (b) Every caller passes the names. (b) puts a manifest read in every
  caller, the burden the probe was built to remove (:941-944). Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — How does the class judge say "instance only"?** (a) A fourth fix verdict, `instance`. (b) A
  separate `fixScope` field beside `fixVerdict`. (b) asks one question in two fields, and a skeptic
  could answer `sound` and `instance` together. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **FACT-QUESTION · F6 — Are the checklist's slugs the only class slugs the harness can hand over?**
  Probe: `grep -n "CHECKLIST_ITEMS\|extractFindingClasses" tools/workflows/tier2-review.template.js`
  for any other class input. Observation: the checklist is the one argument carrying classes, and
  `extractFindingClasses` reads its items alone. Liveness: an argument naming class records, or a
  second reader, would have printed. RESOLVED (agent, 2026-10-23, delegated): the checklist's slugs.
  widens: none · relaxes: none

- **F7 — Does the grant cover the harness, descriptor and stand-in edits?** Every path under
  `tools/` is a governance carrier by `PLAY-dClosedLoop-10`'s list (its routed product paths), and the
  clause names fix verdicts by class and the report's disposition grammar against the leg manifest.
  RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the review harness's class judge, its dispositions, the TOOL_ROOT render
  placeholder and the unclassed pin argument of the review.pin stand-in · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams are the harness's own: the fix-verdict question and its three readers (:670, :1419-1426,
:1492-1543, :1607-1613) take the class variant; the resume probe (:1004-1044) takes the manifest read,
as it already takes the blob reads a harness with no filesystem needs; `extractFindingClasses`
(:1570-1583) supplies the slug grammar; `renderAppendix` (:1629-1635) takes the column; the tally
(:1947-1992) is where the check sits; and the leg-manifest default is the drift-audit state harness's
`{{TOOL_ROOT}}gate-legs.json` idiom. `python tools/codebase-map/reuse_lookup.py "judge whether a
proposed fix covers the bug class and give each confirmed finding a disposition"` ranked
`renderFixLine` among name-stem hits and nothing for the disposition, which no code holds yet; no hit
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed review finding homed to a
bug class, a gate leg or a new class" --terms "fixVerdict sound unsound class instance disposition
gate-legs.json gotchas left-shift appendix classes review.unclassed"`
