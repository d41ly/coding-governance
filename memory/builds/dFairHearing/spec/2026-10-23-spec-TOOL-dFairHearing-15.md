# TOOL-dFairHearing-15 — the review's bug-class checklist, selected by the pinned range and handed by the harness itself

**Status:** OPEN · rev-4 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 16 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0082@8ac81dad whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

A diff review sweeps the project's bug classes only when its caller remembers to run the lookup and
pass its stdout as `checklist`: the harness "produces none and names no checker"
(`tools/workflows/tier2-review.template.js:519-523`), and the charter carries the reminder "run it
before any review" (`coding-governance-agents.template.md:118`). This unit makes the harness hand
the checklist itself, selected by the pinned range and ordered by anchors, so the lookup's charter
line retires. A replay with the checklist and without it over the known-defect corpus decides whether
review keeps that selection or takes every ungated class (night pass two, point 6, the owner's
NT-25). The cut of fully gated classes stays dLinkedLibrary's, once it derives each class's status.

## 2. Scope (IN)

- **S1** — On the diff kind, when the caller passes no `checklist`, the harness spawns one agent in
  the `Resume` phase, labelled `resume:checklist`, before the input print
  (`tools/workflows/tier2-review.template.js:985`) and the resume probe (:1003). It runs `python
  <checker> --for-diff <base>..<head>` in `repo` with a 120-second bound, the range the call pinned,
  and returns its stdout verbatim as `checklist`, or `checklistError` naming why none was produced:
  no checker tracked, a non-zero exit with its code, a timeout, or no line starting `- `
  (`no bug class selected`). The schema copies the resolver's three optional fields
  (`tools/workflows/unattended-build.template.js:767-771`). The returned text then takes the path a
  caller's string takes today: `extractByDesign`, then `parseChecklist`, with their refusals
  (:555-584), so its items keep the checker's order into the `C<n>` labels. A caller's `checklist`
  wins and no agent spawns. Observed by AC1, AC2, AC3 and AC5.
- **S2** — The checker is found at run time, never guessed: the agent asks `git -C <repo> ls-files
  --error-unmatch` for `{{TOOL_ROOT}}memory-tree/gotchas.py`, then `{{TOOL_ROOT}}gotchas.py`, the
  nested and the flat spelling in the renderer's own order, and uses the first tracked. The template
  gains the `TOOL_ROOT` token and `tools/workflows/kit.toml`'s `tier2-review.template.js` row lists it
  beside `FANOUT_CAP` (:76-79), so the render fills it. Observed by AC6.
- **S3** — Every outcome is announced. An acquired checklist logs `checklist from --for-diff
  <base>..<head>` and RUN INTEGRITY says so; a `checklistError` or a dead agent logs a `WARNING:`
  naming the reason, and the RUN INTEGRITY `Checklist:` line (:1808-1811) names it instead of
  "absent". Nothing is passed as an empty checklist. Observed by AC3.
- **S4** — The lookup's charter line retires. The `kit:memory-tree` fence at
  `coding-governance-agents.template.md:117-119`, holding only the line
  `<prefix>/memory-tree/gotchas.py --for-diff <base>..<head>`, is taken out, and its render
  `AGENTS.md:121` goes with it; the second `kit:memory-tree` fence (:173-177) stands. The kit README's
  `checklist` paragraph (`tools/workflows/README.md:200-218`) says the harness acquires it on the diff
  kind and the caller's wins. Observed by AC7.
  **Readers:** by name: `AGENTS.md`, the charter's render, which spells the line at :121 until the
  render runs. by value: NO VALUE READERS — the line is prose an agent reads; no tool compares,
  counts or derives from its text, and `tools/check-template-size.sh` measures the file's bytes,
  which fall.
- **S5** — The replay. Over the known-defect corpus of §4, each record's range is reviewed twice in a
  blind clone: arm `selected`, the harness acquiring its own checklist (S1), and arm `ungated`, the
  caller passing every ungated class in anchor order. Each run is scored by `review_replay.py
  --known <record> --candidate <report>`, paired over the records both arms answered through the
  factory, under a manifest `check_experiment` accepts. Pooled recall decides: `selected` at or above
  `ungated` keeps the selection; below it, the harness takes every ungated class. Observed by AC8.
- **S6** — The decision's product change, made only when `ungated` wins: `gotchas.py` gains
  `--all-ungated`, which after the range's selection in tier order prints every other class whose
  record names no leg of `LEG_MANIFEST`, and the S1 command carries the flag. When `selected` holds,
  no product file changes beyond S1 to S4. Observed by AC9.

## 3. Non-goals (OUT)

- Taking fully gated classes off the checklist: dLinkedLibrary's derived gate status does it. This
  unit's "ungated" is a stand-in reading (§8 F3): the replay's arm, and S6's flag only if the replay
  picks it, until dLinkedLibrary's status replaces it.
- The spec kind. A spec audit pins blobs, not a range; `unattended-build`'s resolver already hands it
  a `--for-paths` checklist (`tools/workflows/unattended-build.template.js:1372-1460`).
- BUILD-METHOD M8's "Bug classes FIRST" sentence, a governance carrier no clause of this build names;
  the harness acquiring the checklist leaves that sentence true.
- Changing how `gotchas.py --for-diff` selects or orders: selection by range and order by anchor tier
  are what it does today (`tools/memory-tree/gotchas.py:76-80`, :682).
- A no-checklist control arm (§8 F2).

### Edges

- **consumes-from** `TOOL-dFairHearing-11` — the agent type and stage declaration every harness spawn carries, which the `resume:checklist` agent takes as the resume probe does
- **consumes-from** `TOOL-dFairHearing-12` — `derive_paired_cases` and the `review-replay` instance the replay scores through
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment`, under which the two arms are declared one variable apart
- **consumes-from** `TOOL-dFairHearing-1` — the bundle-and-clone procedure each blind replay reuses
- **hands-off** external — dLinkedLibrary's derived gate status, which replaces S6's leg-name reading of "ungated" and cuts fully gated classes
- **hands-off** `TOOL-dFairHearing-23` — finding ids 2, 9, 13, 23, 33, 36, 41, 48 and 49 of the round-1 spec audit: the manifest's terms for `dispatched 4` and `paired 4 of 4` (its S4, AC2), S2's kit.toml claim and AC6's kit.toml half superseded (its S38, AC29), the replay recipe (its S17, S18, AC10), the ungated arm read through one shared predicate (its S21, AC12), the kickoff manifest re-stamp (its S28, AC19), the three docs still naming the by-hand lookup (its S45, AC36), the tail-truncation refusal (its S36, AC27) and the checklist agent under `probeOpts` (its S37, AC28)
- **hands-off** `TOOL-dFairHearing-25` — finding id 1 (item H1) of the spec audit of units 20 to 23: the with-and-without replay and its decision, run on unit 23's corrected contract (its S4 to S6); this unit's AC8 and AC9 are superseded by its AC4, AC6 and AC7
- **hands-off** `TOOL-dFairHearing-30` — finding id 28 (item H2) of the round-3 spec audit: the with-and-without replay runs each record and arm in its own fresh clone, in place of `TOOL-dFairHearing-25`, which handed it over; the criteria of this unit that unit 25 superseded are answered there

## 4. Design

### Evidence

Measured 2026-10-23 at `3dca04036`, PINNED.

- `gotchas.py` over this tree reads 145 class records, 6 universal; 15 name a leg of
  `tools/gate-legs.json` in their text, so the `ungated` arm carries about 130 items where a range's
  selection carries tens.
- `review_replay.py --corpus memory/builds` lists 94 replayable records, 41 at round 1.
- The charter line is spelled in `coding-governance-agents.template.md:118` and `AGENTS.md:121` and in
  no other tracked file outside `memory/`.

### The acquiring agent

```
resume:checklist — Resume phase, before the input print
  1. git -C <repo> ls-files --error-unmatch <TOOL_ROOT>memory-tree/gotchas.py, else <TOOL_ROOT>gotchas.py
  2. python <found> --for-diff <base>..<head>   (120 s)
  3. return {checklist: <stdout verbatim>} or {checklistError: <why>}
```

It runs before the input print because the parsed checklist joins the review key
(`tools/workflows/README.md:218`), so the key is computed over what the lenses will sweep, and before
the resume probe because the probe's directory name carries that key. It sits outside the review
shape's agent formula, as the resume probe does. What it does not check: that the agent ran the
command it was told to and returned stdout unaltered; the by-design head-count refusal catches a
truncated block, as the resolver's comment says of its own agent
(`tools/workflows/unattended-build.template.js:1379-1380`).

### The known-defect corpus

The four newest round-1 records `review_replay.py --corpus memory/builds` lists whose appendix carries
a `classes` column, by filename date, PINNED 2026-10-23:

| Record | Files in range |
|---|---|
| `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md` | 343 |
| `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md` | 83 |
| `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md` | 13 |
| `memory/builds/dClosedLoop/reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-answers-b.md` | 15 |

Each record is its own known set: its confirmed findings, read as `review_replay.py` reads any past
record. The four span a large diff, where the selection takes most of the catalogue, and small ones.

### The two arms

Each record's range is reviewed in a clone of a bundle of the history to the range's head, made as
`TOOL-dFairHearing-1`'s §4 makes its own, so the review record and every later object are absent. Both
arms run this repository's rendered `tools/workflows/tier2-review.js`, full intensity, at medium, with
the record's own `base` and `head`.

- `selected` passes no `checklist`; S1 acquires `--for-diff <base>..<head>` from the clone's checker
  and catalogue.
- `ungated` passes `checklist`: an instrument committed beside the replay record imports this
  repository's `tools/memory-tree/gotchas.py` and calls its `records` and `load_leg_names` over the
  clone, printing the `selected` arm's items first in their order and then every other class record
  whose text names no manifest leg, by name. Universal classes ride both arms.

The manifest declares `selected` as the base and `ungated` varying `checklist`, `dispatched` 4 each.

### The decision

Pooled recall is the matched known items over the scorable known items, summed over the records both
arms answered. `selected` at or above `ungated` keeps the selection, the smaller checklist breaking a
tie. Below it, S6 lands. Either way the verdict record states both figures, each record's pair, and
the decision.

### Inventory

| Identifier | Kind | Lexicon verb |
|---|---|---|
| `resume:checklist` | agent label | — |
| `{{TOOL_ROOT}}` in `tier2-review.template.js` | render token | — |
| `--all-ungated` | `gotchas.py` flag, only on an `ungated` win | — |

No new JavaScript function is named; the acquisition sits inline before the input print.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.test.sh`
- `coding-governance-agents.template.md`
- `AGENTS.md`, its render
- `memory/builds/dFairHearing/build/`
- `tools/memory-tree/gotchas.py`, only on an `ungated` win

### Rollout

The harness renders with `check-protocol-parity.test.sh --render`, and the charter with
`tools/playbook/adopt-playbook.sh --target .`. An adopter's next `govkit update` re-renders
`tier2-review.js` with its own `TOOL_ROOT`, which every install derives from the kit's location, so no
adopter loses the render; one with no memory-tree kit gets a `checklistError` naming no checker
tracked, the same review it gets today with the reason stated.

### Alternatives rejected

- **The `MEMORY_TREE_DIR` token, as `unattended-build` uses.** The renderer skips a pair whose
  template carries it when no `gotchas.py` is tracked (`tools/workflows/check-protocol-parity.test.sh:44-49`),
  so an adopter without the memory-tree kit would stop receiving `tier2-review.js` updates, a kit
  dependency the review harness does not have today (`tools/workflows/kit.toml:9`).
- **Folding the acquisition into the resume probe.** The probe's directory name carries the review
  key, and the key carries the checklist, so the checklist must exist first.
- **The harness always acquiring, overriding a caller.** `unattended-build` and a light review's caller
  pass curated checklists today; overriding them changes what those calls sweep.

## 5. Production-readiness checklist

- security — one more read-only agent; its command is fixed text with the call's `base` and `head`,
  which the harness already validates before any spawn (:203-210).
- perf / scale — one agent and one `gotchas.py` run per diff review; the replay costs about 8 review
  runs of 12 to 13 agents.
- error / empty / loading states — every way the checklist can fail to arrive is named in the log and
  in RUN INTEGRITY, never read as an empty catalogue.
- observability — `checklist from` names the range; the split line names each lens's share.
- risks — a dead acquiring agent costs the sweep, announced; a caller who relied on the charter line
  still may pass one.
- testing — AC1 to AC9; the arms under §7, observed red at the close against the parent render.
- migration — kit.toml's placeholder row; adopters re-render on update.
- user docs — the kit README's `checklist` paragraph; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When the rendered `tools/workflows/tier2-review.js` is evaluated with stub agents, in the
  AsyncFunction shape the kit's review suite uses, over diff arguments with no `checklist`, the first
  agent spawned is labelled `resume:checklist`, its prompt names `--for-diff <base>..<head>` with the
  call's refs and both spellings of §4's step 1, `tools/memory-tree/gotchas.py` and the flat
  fallback `gotchas.py` directly under the tool root, and the
  three items its stub returns reach the finder prompts as `C1`, `C2` and `C3`.
  Red when: the parent render spawns no such agent and logs its no-checklist `WARNING:`.
- **AC2** — When the same evaluation passes a caller `checklist`, no `resume:checklist` agent spawns
  and the finder prompts carry the caller's items.
  Red when: the harness acquires over the caller's.
- **AC3** — When the stub returns `checklistError` `no checker tracked`, then stdout holding no `- `
  line, then null, the log carries a `WARNING:` naming each reason, the RUN INTEGRITY `Checklist:` line
  names it, and no run throws.
  Red when: any of the three reads as `supplied with no item` or as absent with no reason.
- **AC4** — When the evaluation runs spec-audit arguments with no `checklist`, no `resume:checklist`
  agent spawns.
  Red when: the spec kind spawns it.
- **AC5** — When the stub returns the stdout of `python tools/memory-tree/gotchas.py --for-diff
  3708a705..HEAD`, captured in scratch, the `C<n>` labels in the finder prompts follow that stdout's
  item order and its by-design block reaches `byDesign`.
  Red when: the harness re-sorts the items or sweeps a by-design entry as a class.
- **AC6** — When `grep` reads the render `tools/workflows/tier2-review.js`, it finds
  `tools/memory-tree/gotchas.py` and no surviving `{{TOOL_ROOT}}`, and the `tier2-review.template.js`
  row of `tools/workflows/kit.toml` lists `TOOL_ROOT`.
  Red when: the template carries the token and the row does not, so an adopter's render keeps it raw.
- **AC7** — When `git grep -n "run it before any review"` runs over `coding-governance-agents.template.md`
  and `AGENTS.md` after the charter's render, it prints nothing, and the template's remaining
  `kit:memory-tree` fence still opens and closes.
  Red when: the template loses the line and the render keeps it, or the other fence is cut.
- **AC8** — When the replay's verdict record lands, it names each of the four records' recall under
  both arms, `paired 4 of 4`, both pooled figures and the decision; and `replay_scorer.py --experiment`
  over its committed manifest prints `arm ungated: varies checklist from selected` and the parsed
  counts before any figure.
  Red when: a record one arm did not answer is pooled, or the decision disagrees with the figures.
  cost: about 8 review runs, roughly 100 agents.
  fixture: four clones under `%TEMP%`, one per record's range head, made by the pass.
- **AC9** — When `selected` holds, `git diff --stat` over the unit's passes names no
  `tools/memory-tree/gotchas.py`; when `ungated` wins, `gotchas.py --for-diff <range> --all-ungated`
  over a fixture catalogue prints the range's selection first, then every class naming no manifest
  leg, and omits a planted class whose text names `memory hygiene`, and the S1 command carries the
  flag.
  Red when: the product changes against the decision, or the flag keeps a class that names a leg.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `review-replay selftest` · `charter size` · `template size <=48KiB` · `playbook parity` · `playbook render wiring` · `recall floor` · `recall floor arms` · `gotchas selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the parent render, which spawns no acquiring agent, so every arm finds no `resume:checklist` and the AC1 items in no prompt · the suite's assertion floor, raised by the arms added

New arm: tools/memory-tree/gotchas.py (its selftest, only on an `ungated` win) · covers AC9 · a planted class record naming a manifest leg, which the flag must omit · none

## 8. Open questions

- **F1 — On which kind does the harness acquire?** (a) The diff kind, where the call pins a range.
  (b) Both, the spec kind reading each subject's Files-touched paths. (b) duplicates the resolver
  `unattended-build` already runs for every spec audit it hands a checklist, a second answer to one
  question. Both survive veto 1; (a) is the clause's "selected by the pinned range". Recommendation
  (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — What are the replay's two arms?** The clause: "a replay with the checklist and without it
  … deciding whether review keeps that selection or takes every ungated class". (a) `selected` against
  `ungated`, "without it" read as without the selection. (b) Three arms, adding no checklist at all.
  (b)'s third arm measures the checklist's lift, which no decision in the clause reads, at half again
  the cost. Both pass veto 1; (a) decides exactly what the clause asks. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — What is "ungated" before dLinkedLibrary derives it?** (a) A class record whose text names no
  leg of `LEG_MANIFEST`, read through `gotchas.py`'s own `load_leg_names`. (b) Wait for
  dLinkedLibrary, a later build, leaving the replay unrunnable here (veto 1). (c) Every class. (c)
  ignores the clause's "ungated". Recommendation (a), named a stand-in. Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — How does the template find the checker?** (a) A run-time probe over two `TOOL_ROOT`
  spellings. (b) The `MEMORY_TREE_DIR` token. (b) makes the review harness's render depend on the
  memory-tree kit, a kit dependency change outside every clause of this build (veto 2). (a) changes
  only the placeholder row. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F5 — May this unit change the charter template?** The template is a governance carrier, and the
  clause names the change: "the lookup's charter line retired as the harness hands the checklist
  itself". RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the memory-tree kit's charter line in `coding-governance-agents.template.md` and
  its `AGENTS.md` render, retired as cl-dClosedLoop-0082 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.
- rev-3 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-25, which runs this unit's replay after unit 23's corrections and supersedes AC8 and AC9.
- rev-4 · 2026-10-23 · §3 · the round-3 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-30,
  which runs this unit's replay in per-arm clones in place of TOOL-dFairHearing-25.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "hand the review its bug class checklist selected by
the diff range"` ranked range readers in the unattended and runlog kits (`read_history_range`,
`read_git_range`), none a checklist source. The seam is the one the probe missed and the source shows:
`unattended-build`'s subject resolver already runs the checker from inside a workflow and forwards its
stdout as `checklist` (`tools/workflows/unattended-build.template.js:1372-1460`), and this unit gives
the review harness the same act on the diff kind, with the same three schema fields and the same
`- ` item rule; the harness's own `extractByDesign` and `parseChecklist` (:555-584) read the result
unchanged. The ordering is `gotchas.py`'s tier sort, reused as is. The recall query returned
`TOOL-aFoldedQuarry-6` ("`--for-diff` stdout IS the reviewer checklist"), `TOOL-aMendedFleet-74` (the
write-set checklist the night pass two retires) and the night pass two's point 6, whose measured
precision figures this spec cites and does not re-derive.

Recall terms used: `python tools/memory-recall/query.py "why does the review harness not produce its
own bug class checklist" --terms "checklist gotchas for-diff tier2-review harness produces none charter
line run it before any review anchors"`
