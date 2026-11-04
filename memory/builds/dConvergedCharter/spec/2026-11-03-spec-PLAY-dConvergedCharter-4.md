# PLAY-dConvergedCharter-4 — superseded parts retired through ratified proposals: one supersession proposer, its route and the ratification check

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 21 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0478@5ccb9b38 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-19 |
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

The chain leaves parts behind that its successors made redundant, and the design says they go "through the Loop
Review's ratified proposals, never by assertion" (walkthrough:789-790). Nothing proposes such a part today, and
nothing refuses a part removed with no owner's yes (gap-spine-04, gap-tool-09 in part). This unit adds one proposer
to the Loop Review's `PROPOSERS` that proposes retiring each part whose fate is `RETIRED` or `MERGED` while it still
stands, routes it under `review.loop.retire`, takes a decline as the `keep` record, and adds the check that reds a
superseded part removed with no ratified proposal.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `0d1c1dda`, re-grounded by the build run, which stops this
unit when one is absent: TOOL-dCalibratedLens-3 (`run_loop_file`, the proposal shape `{"kind", "id", "action",
"accept", "row"}`, `METRICS` and the walk, all in `tools/loop/loop_review.py`) and TOOL-dCalibratedLens-5
(`PROPOSERS`, `derive_proposals`, `resolve_retire_route`, `read_keep_records`, `write_keep_record` and the
`--fixture --plant` harness); TOOL-dWellOiledMachine-27 S3 (`check_intake_ratifies` and `intake.py ratifies
<key>`); TOOL-dPlacedRequest-19 S1 (`derive_request_content_key` and `request.py key <file>` in
`tools/loop/request.py`); TOOL-dDeclaredLoop-23 S3 (`read_commits` and `attribute` in
`tools/lib/commit_trailers.py`); and the part form of a `[[retired]]` id, `<entry>/<slug>`, that the ask
TOOL-dLinkedLibrary-29 asks of `read_retired` and TOOL-dLinkedLibrary-3's build run answers.

- **S1** — The proposer. `derive_supersede_proposals(root, window, rows, readings, retire, earlier)` in
  `tools/loop/loop_review.py`, one entry `("supersede", derive_supersede_proposals)` appended to `PROPOSERS`
  (TOOL-dCalibratedLens-5 S6, whose list is open to another unit's entry). It reads `readings["parts"]`, the parts
  reading: `{<part id>: {"fate": <fate>, "where": <text>, "paths": [<tracked path>, ...]}}`, each part's tracked
  paths at the walk's base, which PLAY-dConvergedCharter-14 supplies as a `METRICS` entry over the fates table
  `tools/govkit/fates.toml`. A part is superseded when its fate is in `SUPERSEDED_FATES` (`RETIRED`, `MERGED`) and
  its `paths` are not empty. Each yields `{"kind": "part", "id": <part id>, "action": "retire", "accept": <S3's
  line>, "row": "<fate> · <where> · <n> tracked path(s)"}`, in part-id order. A part whose `(part, id)` a live keep
  governs is left out, the rule `read_keep_records` gives every proposer (TOOL-dCalibratedLens-5 S8). With no
  `parts` key in `readings` it returns no proposal and the walk prints `supersede — unarmed · no parts reading`, so
  an empty population is announced and never read as nothing superseded. Observed by AC1 and AC2.
  **Readers:** by name: none, since this item mints the proposer and withdraws no name · by value: NO VALUE
  READERS, nothing this item names is taken out of the tree; its `retire` is a proposal action the parent mints.
- **S2** — The route. `resolve_retire_route` (TOOL-dCalibratedLens-5 S7) governs a `part` proposal as it governs a
  ledger row's `retire`: its governed set gains the kind `part`, and nothing else in it moves. Under
  `propose-ratify` the proposal is handed to `item.loop.file`; under `demote-then-propose` it is handed on as
  `demote` unless a committed `loop-review` record whose file-name date is at least the window's days before the
  walk carries a `proposals` segment naming `part <id> demote`, and is then handed on as `retire`; under `report`
  none is handed on, and the `proposals` line still names it. A `part` `demote` carries the accept line `the part
  <id>'s adopter-visible surfaces forwarded by a [[shim]] row or warned for install.deprecation-window releases,
  or kept by a keep record`. Observed by AC3.
  **Readers:** by name: none, since the governed set gains a kind and loses none · by value: NO VALUE READERS,
  the values of `review.loop.retire` are unchanged and read as the parent reads them.
- **S3** — The accept line of a `part` `retire`, one fixed text per id: `the part <id> retired by a [[retired]]
  row naming it and an [[upgrade]] step whose surfaces name its members, or kept by a keep record`. It is
  derived from the id alone, so the text filed for a part is reproducible and S5's check can key it. The loop
  writes no row and no step: the owner ratifies the filed intake with an owner-origin receipt
  (TOOL-dWellOiledMachine-27 S3), and the build that applies it lands the `[[retired]]` row, its id the part's
  `<entry>/<slug>` (`tools/govkit/registry.toml`, read by `read_retired`, `tools/govkit/upgrade_steps.py:890`),
  and the `[[upgrade]]` step P38 owes an adopter-visible surface; the step gate (`tools/govkit/step_gate.py`,
  TOOL-dSafePassage-10) already reds a vanished member no such row names, and this unit adds no second check of
  it. A decline is the owner's `python loop_review.py keep --kind part --id <id> --words <text> --caused-by
  <intake key>`, the `keep` record and no new kind. Observed by AC1.
  **Readers:** by name: none, since the accept line names the rows a ratification lands and withdraws none
  · by value: NO VALUE READERS, no row's value moves here.
- **S4** — One renderer of a filed proposal's text. `render_loop_text(proposal)` returns the stable text
  `run_loop_file` files (TOOL-dCalibratedLens-3 S7), `loop key <key hash> · <kind> <id> · <action>` with the clause
  tail `accept <accept>`; `run_loop_file` calls it, so the filing and S5's check build one text. Where the parent
  already factors that text under another name, S5 calls that function and this item adds nothing. Observed by
  AC6.
- **S5** — The ratification check. `check_ratified_retirements(root, base, head, parts_at)` in
  `tools/loop/loop_review.py`, `parts_at(rev)` returning the parts reading at a commit. A part whose `paths` are
  not empty at `base` and empty at `head` is retired in the range. It passes when either:
  (a) its `retire` proposal ratifies: the content key `derive_request_content_key` gives over
  `render_loop_text` of the part's `retire` proposal, S3's accept line its tail and no `row` in the text
  (TOOL-dCalibratedLens-3 S7), asked of `check_intake_ratifies`; or
  (b) every commit in `base..head` that deletes one of its paths (`git log --diff-filter=D`) names, through its
  `Pass:` or `Gov-Unit:` trailer read by `read_commits` and `attribute(commit, "replace")`, a unit whose spec
  carries a v2 clause, a `**Carries:**` binding of a clause read by `parse_binding_lines`
  (`tools/memory-tree/design_lib.py:352`) — the owner's approval of v2's `[chain]` row ratifies a retirement a
  clause states (§8 F3).
  Otherwise it prints `supersede — <id> retired at <sha8> with no ratified proposal` and the part is a finding;
  a pass prints `supersede — <id> retired at <sha8> · ratified <content key>` or `· carried by <unit> <clause id>`.
  It returns the findings, and its caller decides the exit: PLAY-dConvergedCharter-14's exit check runs it as an
  arm. Observed by AC4 and AC5.
  **Readers:** by name: none, since the check withdraws no name · by value: NO VALUE READERS, it reads
  retirements and retires nothing.
- **S6** — The plants of `python loop_review.py --fixture --plant <name>` (TOOL-dCalibratedLens-5's harness):
  `supersede` (S1, S3), `supersede-route` (S2) and `retired-unratified` (S4, S5), each in a scratch repository
  under `%TEMP%` with a short name, each red as planted and green with its fix. Observed by AC1 to AC6.
  **Readers:** by name: none, since this item mints plants and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S7** — The docs. `help/loop-review.md` gains "Superseded parts": what makes a part superseded, the route under
  each value of `review.loop.retire`, how the owner ratifies or declines, and what the check reds;
  `tools/loop/README.md` names `derive_supersede_proposals` and `check_ratified_retirements`. Observed by AC7.
  **Readers:** by name: none, since the docs describe the route key and the two functions this unit mints and
  withdraw no name · by value: NO VALUE READERS, the values of `review.loop.retire` are documented as the
  parent reads them and none moves.

## 3. Non-goals (OUT)

- Materializing the fates table, its path globs and the parts reading: PLAY-dConvergedCharter-14, which supplies
  the reading this proposer and S5's check read (§8 F2).
- Amending a declined part's fates row to `KEPT`: PLAY-dConvergedCharter-14's join reads the `keep` record and the
  amended row.
- Applying a ratified retirement. The loop files; the owner or a build lands the `[[retired]]` row and the step
  (TOOL-dCalibratedLens-5 §3, "Applying a proposal").
- The retirements this build's own clauses carry (the unattended kit, `/build`, `/session-kickoff`, the house
  seed, the guides): their units retire them, and S5 reads them as carried (§8 F3).
- Ledger rows that caught nothing, units that bear no load, broken units and recurring overrides:
  TOOL-dCalibratedLens-5's three proposers.
- A new filing path or a new record kind: the proposal is filed by `run_loop_file`, the decline is a `keep`.

### Edges

- **hands-off** `PLAY-dConvergedCharter-14` — the `keep` record of a declined part keyed `(part, id)`, which its join reads to require the amended row; the parts reading `readings["parts"]` this proposer and `check_ratified_retirements` read, which its `METRICS` entry supplies; and `check_ratified_retirements`, which its exit check runs as an arm
- **consumes-from** external — TOOL-dCalibratedLens-3 and -5 (`PROPOSERS`, `resolve_retire_route`, `run_loop_file`, `read_keep_records`, the plant harness), TOOL-dWellOiledMachine-27 S3 (`check_intake_ratifies`), TOOL-dPlacedRequest-19 S1 (`derive_request_content_key`), TOOL-dDeclaredLoop-23 S3 (`read_commits`), and the `[[retired]]` part form TOOL-dLinkedLibrary-29 asks for; each DEFERRED at base and of a parent or ancestor build

## 4. Design

### Evidence

At this base nothing proposes or refuses a part's retirement. The succession grammar is live: `RETIRED_KEYS`
(`tools/govkit/upgrade_steps.py:144`) and `read_retired` (`:890`), which validates an entry or step id and holds
no field naming why a row was written; `tools/govkit/registry.toml:190-195` says no row has landed. The step gate
(`tools/govkit/step_gate.py`, `derive_vanished_members` at `:219`) reds an adopter-visible member that vanishes
with no row, and asks nothing about who decided it. The Loop Review, its proposers and the keep record are
TOOL-dCalibratedLens-3 and -5's, specced and unbuilt. The fates record's `[table]` holds 138 rows, 18 of them
`RETIRED` and 25 `MERGED` (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`, PINNED,
parsed at `0d1c1dda`; the record states 139).

### The flow

1. A period's walk gathers `METRICS`; PLAY-dConvergedCharter-14's entry adds the parts reading.
2. `propose` runs `PROPOSERS` in list order; `derive_supersede_proposals` turns each superseded part into one
   `retire` proposal, leaving out a part a live keep governs.
3. `resolve_retire_route` hands it on as `review.loop.retire` says; `run_loop_file` files it as an intake keyed by
   its text, so a part proposed again period after period appends a receipt to one open intake (route `seen`).
4. The owner ratifies the intake from an owner session, or writes a `keep`. A ratified part is removed by a build
   that lands its `[[retired]]` row and step; a declined part's row is amended to `KEPT` by PLAY-dConvergedCharter-14's
   route, and the part leaves the superseded set.
5. At a landing, `check_ratified_retirements` reads the parts at the base and the tip; each part removed in between
   must show a ratifying receipt or a carrying clause.

### The lines

```
proposals: part unattended/slug-mode retire · part codebase-map/reuse-lookup retire · propose-ratify
supersede — unattended/slug-mode retired at 1a2b3c4d · ratified 3f2a9c01b4de
supersede — skills/deploy-governance retired at 5e6f7a8b with no ratified proposal
supersede — unattended/the-kit retired at 9c0d1e2f · carried by PLAY-dConvergedCharter-12 cl-dClosedLoop-0486
supersede — unarmed · no parts reading
```

### Inventory

Names this unit mints, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this
base and answered OK: `derive_supersede_proposals`, `check_ratified_retirements`, `render_loop_text`.
`SUPERSEDED_FATES` is a module constant; the `py.constant` cell is undeclared at this base, so no cell grades it.
Proposal kind: `part`. `PROPOSERS` entry name: `supersede`. Plants: `supersede`, `supersede-route`,
`retired-unratified`.

### Migration

None. The proposer is unarmed until the parts reading exists, and announces it; the check grades a range only once
a parts reading exists at both ends.

### Rollout

Lands at order 21, after every retirement unit of this build and before PLAY-dConvergedCharter-14, which arms it.

### Files touched (estimate)

- `tools/loop/loop_review.py` (S1, S2, S4, S5, S6)
- `tools/loop/README.md` (S7)
- `help/loop-review.md` (S7)
- `help/README.md` (S7, the page's row where an earlier unit did not write it)

### Alternatives rejected

- **The proposer reading the fates record's `[table]` markdown.** The test: the record is a frozen design record
  under `memory/builds/dClosedLoop/build/`, with no path column (scout D disagreement 3); a product reader of it
  would make the record a second home of the table PLAY-dConvergedCharter-14 materializes, against `[one-fact]`.
- **This unit materializing `tools/govkit/fates.toml`.** The test: M2's one mechanism per spec; the table is a
  separate artifact with its own join, and the brief's I22 gives it to PLAY-dConvergedCharter-14.
- **A `ratified` key on the `[[retired]]` row.** The test: `read_retired` refuses a key outside `RETIRED_KEYS`
  (`upgrade_steps.py:905-906`), and a part merged away needs no row when nothing an adopter sees vanishes, so a
  field there misses those parts; the intake's ratifying receipt is keyed by the proposal's own text instead.
- **Every part removal requiring an intake (no carried-clause leg).** Rejected by §8 F3's test: the build's own
  close would red on units 12, 16 and 17's removals with no owner turn to ratify them.

## 5. Production-readiness checklist

- security — the proposer reads the reading and writes no file; the check runs `git log`, `request.py key` and
  `intake.py ratifies` as bounded subprocesses with argv lists, a part id never reaching a shell or a path.
- perf / scale — one proposal per superseded part, at most 43 at base (PINNED, the fates record's `RETIRED` and
  `MERGED` rows); the check runs one `git log --diff-filter=D` per retired part in the range.
- error / empty / loading states — no parts reading prints the unarmed line; a part with no tracked path is never
  proposed; a failed `intake.py ratifies` reads as not ratified and names the error in the finding.
- observability — the `proposals` line, the `supersede —` lines and each finding's part, commit and cause.
- risks — the carried-clause leg admits any unit whose spec carries a clause, not only the clause that names the
  part; stated in §6's limit and §8 F3.
- testing — the three plants of S6, in `loop_review.py --fixture`; the `New arm:` line in §7.
- migration — none (§4).
- user docs — `help/loop-review.md` (S7).

## 6. Acceptance criteria

Each plant builds a scratch git repository under `%TEMP%` with a short name, runs `loop_review.py` from this tree
against it, and prints its observations; a plant exits 0 when every observation matches and 1 otherwise. What the
check does not see: whether the clause a carrying unit's spec carries is the one that names the part.

- **AC1** — When `python loop_review.py --fixture --plant supersede` plants a parts reading of four parts, one
  `RETIRED` with two tracked paths, one `MERGED` with one, one `RETIRED` with none and one `STAYS` with one,
  `propose --dry-run` prints exactly two proposals, `part <id> retire`, each with S3's accept line naming
  `[[retired]]`; after `keep --kind part --id <first id>` only the second prints.
  Red when: the `STAYS` part or the part with no tracked path is proposed, or the keep is ignored.
- **AC2** — When the same plant runs with no `parts` key in the readings, `propose --dry-run` prints
  `supersede — unarmed · no parts reading` and no `part` proposal.
  Red when: the missing reading passes silently, as an empty superseded set.
- **AC3** — When `python loop_review.py --fixture --plant supersede-route` commits a planted policy file setting
  `review.loop.retire` to each value in turn: `propose-ratify` hands `part <id> retire` to `file`;
  `demote-then-propose` hands `part <id> demote`, and with a committed record 60 or more days old whose
  `proposals` line names `part <id> demote` hands `retire`; `report` hands nothing and the `proposals` line
  still names it.
  Red when: a value is not read, `report` files the proposal, or a part is retired with no earlier demote under
  `demote-then-propose`.
- **AC4** — When `python loop_review.py --fixture --plant retired-unratified` commits a `RETIRED` part's two
  paths deleted by one commit whose `Pass:` trailer names a unit whose spec carries `**Derived:**` and no
  clause, `check_ratified_retirements` prints `supersede — <id> retired at <sha8> with no ratified proposal`;
  with an owner-origin receipt planted on the intake keyed by `request.py key` over the proposal's text, it
  prints `ratified <content key>`, and with only a `cadence` receipt it still reds.
  Red when: the unratified removal passes, a cadence receipt ratifies, or the ratified one reds.
- **AC5** — When the same plant's deleting commit names a unit whose spec carries a `**Carries:**` clause
  binding, `check_ratified_retirements` prints `carried by <unit> <clause id>`; when the two paths are deleted
  by two commits, one of each kind, it reds naming the commit whose unit carries no clause.
  Red when: a removal split across a carrying and a non-carrying commit passes.
- **AC6** — When `git grep -n "def render_loop_text"` runs, it prints one definition, and
  `git grep -n "render_loop_text("` shows the call in `run_loop_file` and in `check_ratified_retirements`; the
  plant of AC4 files the proposal through `run_loop_file`'s dry run and the key it prints equals the key the
  check asks.
  Red when: `run_loop_file` builds its text inline, so the check keys a different text.
- **AC7** — When `grep -n "Superseded parts" loop-review.md` runs in `help/` and
  `grep -n "derive_supersede_proposals" README.md` runs in the loop kit's directory, each prints the line.
  Red when: either page lacks it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `policy check`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base and is named
here in prose; it runs the plants of S6 once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC4 AC5 · the `--fixture` plants `supersede`, `supersede-route` and `retired-unratified`, staged red by a proposer that ignores the keep, a route that files under `report`, and a check that reads a `cadence` receipt as ratifying · none

## 8. Open questions

- **F1 — What is a superseded part?** Options: (a) a fates part whose fate is `RETIRED` or `MERGED` and whose paths
  are still tracked; (b) (a) and every `RESHAPED` part; (c) a part the Loop Review's ledger reads idle. (b)
  proposes retiring parts the fates record keeps in reshaped form; (c) is TOOL-dCalibratedLens-5's
  `derive_retire_proposals` already, and reads catches, not succession. Rung 3. RESOLVED (agent, 2026-11-03,
  delegated): (a), `SUPERSEDED_FATES` declared once. widens: none · relaxes: none
- **F2 — Where does the proposer read the parts, when the fates table lands one order later?** Options: (a) a
  `parts` key in the walk's readings, supplied by PLAY-dConvergedCharter-14's `METRICS` entry, the proposer
  unarmed and announcing it until then, its plants supplying the reading; (b) the fates record's `[table]`; (c)
  this unit materializes the table. (b) and (c) fail §4's alternatives. Rung 3, with M2's one mechanism per spec.
  RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — What ratifies a part removal this build's own clauses carry?** Options: (a) the clause: a deleting commit
  whose unit's spec carries a v2 clause is ratified by the owner's approval of v2's `[chain]`; (b) only an owner's
  receipt on a filed proposal; (c) the check grades only landings after this unit's own, from an arming commit.
  v2's own row retires the unattended kit, `/build` and `/session-kickoff` by clause with no proposal
  (`cl-dClosedLoop-0486`, `-0490`, `-0491`), so (b) contradicts sibling clauses of the same row and reds this
  build's close with no owner turn to clear it; (c) types an arming commit beside history, against `[derive]`.
  "Never by assertion" (walkthrough:789-790) is met by a clause the owner approved. Rung 1, v2 answers it.
  RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F4 — What does `demote-then-propose` do for a part?** Options: (a) as for a ledger row: the first proposal is
  `demote`, the part's surfaces forwarded or warned for `install.deprecation-window` releases (P38), and `retire`
  follows a window later; (b) treat a part as `propose-ratify`. (b) fails the value's own planted case (AC3).
  Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 4 (`cl-dClosedLoop-0478@5ccb9b38`), the spec brief's
  unit 4 row and I2, I22 and I24, scout A's row for unit 4, the walkthrough's Convergence step 4 (:789-790), the
  night pass's instrument text for `owner-item-without-its-reject-outcome`, and TOOL-dCalibratedLens-3 S7 and -5
  S6 to S8.

## 10. Reuse audit

The seams extended: TOOL-dCalibratedLens-5's `PROPOSERS` list and `resolve_retire_route` (one entry and one kind),
its `keep` record and `read_keep_records` (no new kind), TOOL-dCalibratedLens-3's `run_loop_file` (the filing, its
text factored once as `render_loop_text`), TOOL-dWellOiledMachine-27's `check_intake_ratifies` (the one ratifying
predicate), TOOL-dPlacedRequest-19's `derive_request_content_key` (the one content key), TOOL-dDeclaredLoop-23's
`read_commits` (the one trailer reader) and the live `parse_binding_lines` (`tools/memory-tree/design_lib.py:352`).
The probe `python tools/codebase-map/reuse_lookup.py "propose retiring a superseded part and refuse a retirement
no owner ratified"` ranked `read_retired` and `RetiredRow` (`tools/govkit/upgrade_steps.py`, SEAM) by name stem
and nothing that proposes or ratifies, so no existing seam fits the proposer or the check at HEAD, and both sit on
the parent seams above. The recall query surfaced the ask TOOL-dLinkedLibrary-29, which this spec takes as the
`[[retired]]` part form's home. Where scout A's row and source disagree: it names "the fates ratification record"
among this unit's product paths; the ratification is the intake's owner receipt and the decline the `keep`, so no
record file is added. Its `read_retired` citation at `upgrade_steps.py:890` holds at this base.

Recall terms used: `python tools/memory-recall/query.py "how is a superseded part retired only through a ratified
loop review proposal" --terms "supersede retire ratified proposal PROPOSERS keep review.loop.retire retired
successor upgrade step fates part"`
