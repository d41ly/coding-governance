# TOOL-dCalibratedLens-14 — lens removal by a swap or an exclusion, a repository lens's replay result, and scenario promotion as `flow.promote` says

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 17 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0471@453f9872 whole
**Carries:** node:policy-key.flow.promote

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |

<!-- /gen:spec-records -->

## 1. Goal

No route turns a build's adaptation into a reusable variant: `promoted-from` covers only memory
promoted to instruction, and the Loop Review proposes only retirements, merges and caps
(`gap-review-18`, MED). This unit gives `flow.promote` its three values, `loop-proposes`, `owner-only`
and `off`: the Loop Review proposes a scenario from a recorded change two or more builds carried, the
owner ratifies it through `instructions.edit` with `promoted-from` edges to those changes, builds in
flight move to it only at a step boundary and only if they comply, and a declined proposal is not
raised again until a build carries a changed form. It also finishes the lens half of the night pass
two's NT-9: a default lens taken out by an exclusion has its slot filled by an opt-in, and a
repository lens records a replay result when one ran and never owes one.

## 2. Scope (IN)

- **S1** — Lens removal by a swap stays TOOL-dFairHearing-3's `optIn`, unchanged. Lens removal by an
  exclusion: `tools/workflows/review_pin.py` takes `--exclude <lens key>`, repeatable, and for each
  key that is a default of the run's literal requires the `--opt-in` entry for that literal to map an
  opt-in to it, so its slot is filled by that opt-in; an excluded default with no such entry exits 2
  naming `instructions.exclude`, the literal and the key. An excluded key that is no default of the
  run's literal changes nothing. Observed by AC1, AC2 and AC3.
- **S2** — `--trigger` (TOOL-dDeclaredLoop-20 S2) in `tools/unattended/unattended.sh` reads
  `instructions.exclude` with `policy.py get instructions.exclude` and passes each member tagged
  `lens.<key>` to `review_pin.py` as `--exclude <key>`. Observed by AC4.
- **S3** — A repository lens's replay result. An overlay `[[lens]]` row of the lens kind
  (TOOL-dCalibratedLens-13) takes an optional field `replay`, the repository path of the committed
  scorer output of a replay it ran (TOOL-dFairHearing-12's `replay_scorer.py`). `check_lens_replay` in
  `tools/workflows/render_lenses.py` refuses a `replay` naming no tracked file, naming the row's tag
  and the field, and never refuses a row that carries none, whatever its `optin`. Observed by AC5.
- **S4** — The candidates. `read_carried_changes(root, window)` in `tools/loop/loop_review.py` is a
  `gather` step: every change record a run-state file's `rescope · flow <act> <row tag> · change
  <stem>` row names, whose `flow-state <row tag> · applied` row the same file carries
  (TOOL-dDeclaredLoop-28 S2, S5), dated inside `review.loop.window-days`, each read as its `After`
  value, its build's slug and the scenario its build ran at the step it applied in, read from the
  `scenario=` field of the transition record into that step (TOOL-dDeclaredLoop-27 S8). A held or
  refused change is not carried. Observed by AC6.
- **S5** — The proposals. `derive_scenario_proposals(changes, keeps, mode)` is a `propose` step: under
  `loop-proposes` it raises one proposal per pair of an `After` value and a scenario carried by two or
  more distinct builds, unless a `keep` record keyed (`scenario`, that `After`) governs it; a row
  whose kind is not activatable (`kind.item` or `kind.splice`, TOOL-dDeclaredLoop-27 S3) is not
  raised. Each proposal is a `[[scenario]]` row, §4 "The proposed row", with the
  `instructions_edit.py add --manifest overlay` command that would write it and the `Promoted-from`
  value naming every carrying change record. `file` (TOOL-dCalibratedLens-3) files each as an owner
  item. Observed by AC6, AC7 and AC8.
- **S6** — The field. The `loop-review` record (TOOL-dCalibratedLens-3) gains `scenario-proposals`,
  `<n> · <After> under <scenario> from <slug>+<slug>` per proposal, or
  `none — flow.promote <value>` under `owner-only` and `off`. No second record kind. Observed by AC6
  and AC8.
- **S7** — The decline. The owner declines a proposal by writing a `keep` record
  (TOOL-dCalibratedLens-5, shared interface S2) keyed (`scenario`, `<After>`, date). The next review
  does not raise that `After`; a build carrying a changed form carries another `After`, which is a new
  candidate under S5's rule. Observed by AC7.
- **S8** — The ratification and the refusal. `tools/playbook/instructions_edit.py`'s write verbs
  (PLAY-dOrderedCharter-15 S2) take `--promoted-from <value>`, written to the change record's
  `Promoted-from` field (its S7), the `promoted-from` edge's one site (PLAY-dOrderedCharter-28 S1). A
  write of a `[[scenario]]` row carrying `--promoted-from` is a promotion: `check_promote_policy`
  reads `flow.promote` and, under `off`, exits 1 naming `flow.promote` and `off` and writes nothing.
  Under `loop-proposes` and `owner-only` it writes as `instructions.edit` says. Observed by AC9 and
  AC10.
- **S9** — Builds in flight. `derive_step_scenarios(build)` (TOOL-dDeclaredLoop-27 §4) adds, at a
  transition into a step, each promoted scenario `read_promoted_scenarios(root)` returns that the build
  complies with: its `extends` among the build's placed scenarios, its predicate holding over the
  build's facts, the build's composition with it passing every row check and `flow.scenario-conflict`,
  and `compare_path` (TOOL-dDeclaredLoop-28 S7) finding no `skip` against it over the steps already
  walked. A build that does not comply keeps its scenarios, and the writer prints
  `scenario: <tag> held — <the failing condition>`. Between boundaries nothing moves, and under `off`
  nothing moves. Observed by AC11 and AC12.
- **S10** — The catalogue row. `flow.promote` (`tools/policy/catalogue.toml:826-830`) gains `summary`
  and `usage`, its values and default unchanged, and `python tools/policy/policy.py lists --write`
  drains the name from `tools/policy/unsummarised-keys.txt` (`:65`). Observed by AC13.
- **S11** — The docs: `help/policy.md`'s key table (`:206-213`) gains the key's row; `help/loop.md`
  (TOOL-dDeclaredLoop-1 S7) gains a section on promotion, its three values, the decline and the move
  at a step boundary; `tools/workflows/README.md`'s `review_pin.py` section states `--exclude`.
  Observed by AC14.

**Build-run precondition.** TOOL-dFairHearing-3 and -12, TOOL-dDeclaredLoop-20, -27 and -28,
PLAY-dOrderedCharter-15, -28 and -35, and this build's units 3, 5 and 13 are unbuilt at `8bec4cef`.
The build run builds this unit once each is CLOSED, and re-grounds every line this spec cites.

## 3. Non-goals (OUT)

- The `lens` kind, its schema, the overlay's lens rows and their render, and the refusal of an
  exclusion of a lens `review.opt-in` names: TOOL-dCalibratedLens-13. This unit adds one optional
  field and its check.
- `instructions.exclude` itself and the composition's `excluded` state: PLAY-dOrderedCharter-35 S5.
- Running a replay for a repository lens, or owing one. A replay is TOOL-dFairHearing-12's scorer run
  by whoever chooses to.
- The Loop Review's lease, period, `file` and `record` verbs: TOOL-dCalibratedLens-3. The `propose`
  verb and the `keep` record: TOOL-dCalibratedLens-5.
- Promoting a change into gov's pack `tools/loop/scenarios.toml`: its factory is
  `python tools/playbook/core.py new scenario` (TOOL-dDeclaredLoop-27 S1), not `instructions.edit`
  (§8 F4).
- Re-picking a scenario other than a promoted one between placement and close: TOOL-dDeclaredLoop-27's
  `then` edges and dPlacedRequest's placement.
- A losing test for the stage lenses: TOOL-dCalibratedLens-1 §3.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — the `loop-review` record and the `gather` and `file` verbs, which S4 extends and S5 hands its proposals to
- **consumes-from** `TOOL-dCalibratedLens-5` — the `propose` verb S5 is a step of, and the `keep` record S7 reads
- **consumes-from** `TOOL-dCalibratedLens-13` — `kind.lens` and the overlay's `[[lens]]` rows, which S3 adds `replay` to
- **consumes-from** external — TOOL-dFairHearing-3 S8, `review_pin.py` and its `--opt-in`; TOOL-dFairHearing-12, the scorer whose output `replay` names
- **consumes-from** external — TOOL-dDeclaredLoop-20 S2 `--trigger`; TOOL-dDeclaredLoop-27's `derive_step_scenarios` and the `scenario=` field; TOOL-dDeclaredLoop-28's change records, state rows and `compare_path`
- **consumes-from** external — PLAY-dOrderedCharter-15's `instructions_edit.py` and its change record; PLAY-dOrderedCharter-35's `instructions.exclude`

## 4. Design

**Waits on:** TOOL-dFairHearing-3, TOOL-dFairHearing-12, TOOL-dDeclaredLoop-20, TOOL-dDeclaredLoop-27,
TOOL-dDeclaredLoop-28, PLAY-dOrderedCharter-15, PLAY-dOrderedCharter-28, PLAY-dOrderedCharter-35,
TOOL-dCalibratedLens-3, TOOL-dCalibratedLens-5 and TOOL-dCalibratedLens-13. This unit specs none of
their primitives.

### Evidence

- `flow.promote` is a catalogue row at base, `allowed = ["loop-proposes", "owner-only", "off"]`,
  default `loop-proposes`, owner `dCalibratedLens` (`tools/policy/catalogue.toml:826-830`), and
  `python tools/policy/policy.py get flow.promote` prints `loop-proposes` with no policy file setting it.
- v2:1267 carries the row "how a build's recorded change becomes a reusable scenario, the owner's
  NT-5". The night pass two states NT-5 (night-pass-two:114-116) and NT-9: "A lens is added as a
  catalogue row whose brief is a unit and removed by a swap or an exclusion; a repository lens records
  a replay result when one ran and never owes one" (night-pass-two:128-129).
- A change record carries `After` as `<tag>@<hash8>` over the row's canonical form
  (TOOL-dDeclaredLoop-28 S3, PLAY-dOrderedCharter-35 S6), so two builds carrying one row carry one
  `After`, and a changed form carries another. That is the clause's "keyed by the change's content".
- PLAY-dOrderedCharter-15 S7 defines the `Promoted-from` field and names no flag for it;
  PLAY-dOrderedCharter-14 composes the value in-process for its own `promote` verb.
- A scenario is selected at placement and changes only at a step boundary
  (TOOL-dDeclaredLoop-27 S8), so a scenario ratified after a build was placed reaches it only through
  that boundary.

### The exclusion

```
review_pin.py --subject <s> ... [--opt-in '<json>'] [--exclude <key> ...]
  literal = the run's preset (TOOL-dFairHearing-3 S8)
  for key in excludes:
    if key is a default of literal:
      need an entry k -> key in optIn[literal]          # its slot filled by that opt-in
      none -> exit 2: "instructions.exclude takes <key> out of <literal> and no review.opt-in entry fills its slot"
```

The swap then runs as TOOL-dFairHearing-3 S2 runs it, so an exclusion compiles to one swap per run
and the literal keeps five slots. The harness reads no policy and no overlay; `review_pin.py` reads
only its arguments, as at base.

### The proposed row

```toml
[[scenario]]
tag = "scenario.adopter.<the last segment of the carried row's tag>"
extends = "<the scenario every carrier ran at that step>"
activates = { "<kind.item or kind.splice>" = [ <the carried row, from the change record's fence> ] }
```

`admits`, `entry` and `then` are inherited from `extends` (TOOL-dDeclaredLoop-27 §4), so the
promoted scenario is placed beside its parent wherever the parent is, and a build in flight under the
parent can comply. The command printed beside it:

```
python tools/playbook/instructions_edit.py add --manifest overlay --row '<the row>' \
  --promoted-from 'change <stem>, <stem>'
```

### Each value

| `flow.promote` | The Loop Review | `instructions_edit.py` with `--promoted-from` | Builds in flight |
|---|---|---|---|
| `loop-proposes` | raises S5's proposals | writes, as `instructions.edit` says | move at a boundary if they comply |
| `owner-only` | raises none; the field reads `none — flow.promote owner-only` | writes, as `instructions.edit` says | move at a boundary if they comply |
| `off` | raises none; the field reads `none — flow.promote off` | exits 1 naming `flow.promote` | none move |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--exclude` | flag of `review_pin.py` | none |
| `replay` | optional field of an overlay `[[lens]]` row | none |
| `check_lens_replay` | Python function, `render_lenses.py` | `py.function`, `--suggest` OK |
| `read_carried_changes`, `derive_scenario_proposals` | Python functions, `loop_review.py` | `py.function`, `--suggest` OK |
| `scenario-proposals` | field of the `loop-review` record | none |
| `scenario` | key kind of a `keep` record | none |
| `--promoted-from` | flag of `instructions_edit.py`'s write verbs | none |
| `check_promote_policy` | Python function, `instructions_edit.py` | `py.function`, `--suggest` OK |
| `read_promoted_scenarios` | Python function, `scenario.py` | `py.function`, `--suggest` OK |

### Migration

None. No change record is a carried change until a build applies one, and an unset `flow.promote`
reads `loop-proposes`, whose proposals the owner must still ratify.

### Rollout

One landing, after the parents. The first proposal needs two builds carrying one change inside the
window, so the Loop Review raises nothing on a tree with none.

### Files touched (estimate)

- `tools/workflows/review_pin.py`
- `tools/workflows/render_lenses.py`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/loop/loop_review.py`
- `tools/loop/scenario.py`
- `tools/playbook/instructions_edit.py`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/policy.md`
- `help/loop.md`

### Alternatives rejected

- **A new record kind for a declined proposal.** Shared interface S4 admits no second record kind for
  the Loop Review, and the `keep` record already is the owner declining what the Loop Review proposed.
- **Matching carried changes by row tag alone.** It would read a changed form as the declined one, so
  a decline would hold forever, against the clause's "until a build carries a changed form".
- **Moving builds in flight as soon as a scenario is ratified.** A scenario changes only at a step
  boundary (TOOL-dDeclaredLoop-27 S8); a mid-step move is the rewrite that rule forbids.

## 5. Production-readiness checklist

- security — the one new write path is `instructions_edit.py`'s, behind its guard and
  `instructions.proof` (PLAY-dOrderedCharter-15 S4, S5); a proposal is printed and filed, never
  written by the Loop Review. `--promoted-from` is a field value the change record's field check
  validates.
- perf / scale — S4 reads every run-state file and change record once per period; the population is
  the builds folder, bounded by the window.
- error / empty / loading states — no carried change gives `scenario-proposals: 0`, a printed empty
  result rather than an absent field; an unreadable change record is named and skipped, never counted.
- observability — every proposal names its carriers, every held move prints its failing condition,
  and the `off` refusal names the key.
- risks — a promoted scenario inherits its parent's admission, so it reaches every later build the
  parent does; that is the reusable variant the clause asks for, and the owner's ratification is the
  gate. A carrier whose transition records name no scenario reads `flow.scenario-default`'s value.
- testing — AC1 to AC14 as probes and fixtures; the arms in §7.
- migration — none.
- user docs — `help/policy.md` and `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/review_pin.py --subject <a spec> --exclude blast-radius
  --opt-in '{"unit-spec": {"security": "blast-radius"}}'` runs, it exits 0 and prints `optIn` mapping
  `security` to `blast-radius`.
  Red when: the excluded default still runs, or the filled slot is refused.
- **AC2** — When the same call runs with `--opt-in none`, it exits 2 and its stderr names
  `instructions.exclude`, `unit-spec` and `blast-radius`.
  Red when: the run proceeds with four slots or with the excluded lens.
- **AC3** — When `review_pin.py --subject <a spec> --exclude intent --opt-in none` runs, it exits 0
  and prints the line it prints without `--exclude`.
  Red when: an excluded key that no default of the run's literal carries refuses the run.
- **AC4** — When `bash tools/unattended/unattended.sh --trigger <fixture slug> --subject <a spec>
  --cause opt-in` runs in a fixture whose policy file sets `instructions.exclude =
  ["lens.blast-radius"]` and no `review.opt-in`, it refuses naming `instructions.exclude`; with
  `review.opt-in` filling the slot its JSON line carries the swap.
  Red when: `--trigger` passes no `--exclude`.
  fixture: the `--trigger` fixture TOOL-dDeclaredLoop-20 lands in `tools/unattended/unattended.test.sh`.
- **AC5** — When `python tools/workflows/render_lenses.py` checks a scratch overlay holding three
  repository lens rows, one with no `replay`, one whose `replay` names a tracked file and one whose
  `replay` names no tracked file, only the third is refused, its message naming its tag and `replay`.
  Red when: the first is refused, so a repository lens owes a replay, or the third passes.
- **AC6** — When `python tools/loop/loop_review.py --fixture --plant promote-two-builds` runs, under
  `loop-proposes` with two builds applying one change under `scenario.feature`, the record's
  `scenario-proposals` field names that `After` once with both slugs; with one of the two held, or
  with the second build under another scenario, it reads `0`.
  Red when: one carrier, a held change, or two scenarios raise a proposal.
- **AC7** — When the fixture plants a `keep` record keyed (`scenario`, that `After`), the next review's
  field reads `0`; when two builds then carry a changed form of the same row, it names the new
  `After`.
  Red when: a declined proposal is raised again, or a changed form is held by the old decline.
- **AC8** — When the AC6 fixture runs under `owner-only` and under `off`, the field reads
  `none — flow.promote owner-only` and `none — flow.promote off`, and `file` files no owner item.
  Red when: either value raises a proposal.
- **AC9** — When `python tools/playbook/instructions_edit.py fixture --plant promote-off` runs, an
  `add --manifest overlay` of a `[[scenario]]` row with `--promoted-from` under `flow.promote = "off"`
  exits 1 naming `flow.promote` and writes no row and no change record; the same write with no
  `--promoted-from` is not refused by this check.
  Red when: a promotion under `off` writes, or an owner's unpromoted scenario is refused.
- **AC10** — When the same fixture plants the write under `owner-only` with the owner's proof, the
  change record it writes carries `Promoted-from: change <stem>, <stem>`.
  Red when: the edge is lost, so the promotion names no change.
- **AC11** — When `python tools/loop/scenario.py --fixture --plant promoted-in-flight` runs, a build
  under `scenario.feature` that complies gains the promoted scenario on its next transition record's
  `scenario=` field, and a build that skipped a promoted item in a walked step keeps its scenarios and
  prints `scenario: <tag> held — skip`.
  Red when: a non-complying build moves, or a complying one does not.
- **AC12** — When that fixture derives the scenario between two boundaries, and at a boundary under
  `flow.promote = "off"`, the build's scenarios are unchanged.
  Red when: a build moves mid-step, or moves under `off`.
- **AC13** — When `python tools/policy/policy.py lists --check` runs, it exits 0, and
  `grep -c '^flow.promote$' tools/policy/unsummarised-keys.txt` prints 0.
  Red when: the row has no `summary` or `usage`, or the name is still listed.
- **AC14** — When `grep -c 'flow.promote' help/policy.md help/loop.md` and
  `grep -c '\-\-exclude' tools/workflows/README.md` run, each file counts at least one.
  Red when: a page describes promotion or exclusion without the key or the flag.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `workflow script syntax` · `govkit acceptance matrix` · `playbook render selftest` · `policy check` · `policy fixtures` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's and the instruction command's legs, `loop scenario fixtures` (TOOL-dDeclaredLoop-27
S10) and `instruction edits (manifest checks)` (PLAY-dOrderedCharter-15 S10), are not in the manifest
at base, so they are named here and not on the line; the build pass adds them to the line once they
resolve.

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC5 · `review_pin.py` with an excluded default filled, unfilled and absent from the literal, and a scratch overlay of three repository lens rows, red against the pin with no `--exclude` and the renderer with no `replay` check · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/unattended/unattended.test.sh · covers AC4 · a `--trigger` call in a fixture excluding a default lens, red against the verb as TOOL-dDeclaredLoop-20 lands it, which reads no exclusion · none
New arm: tools/loop/loop_review.py · covers AC6 AC7 AC8 · fixture plants of two carriers, a held change, two scenarios, a `keep` record, a changed form and each value, red against the Loop Review with no promotion step · none
New arm: tools/playbook/instructions_edit.py · covers AC9 AC10 · fixture plants of a promotion under `off` and under `owner-only`, red against the command with no `--promoted-from` · none
New arm: tools/loop/scenario.py · covers AC11 AC12 · fixture plants of a complying build, a skipping build, a mid-step derivation and `off`, red against `derive_step_scenarios` as TOOL-dDeclaredLoop-27 lands it · none

## 8. Open questions

- **F1 — One unit, or the clause in parts?** The clause joins lens removal, a repository lens's replay
  result and scenario promotion. (a) One unit carrying it whole, as the roster gives one unit per
  clause. (b) Two units, 1/2 and 2/2, which needs an id the authored roster does not hold and the main
  loop's AMEND ADD. Both carry every criterion; (b) adds an open question and a unit no writer of
  this run may mint. Recommendation (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, the
  tie-break on fewer open questions. widens: none · relaxes: none
- **F2 — Which opt-in fills an excluded default's slot?** (a) The `review.opt-in` entry mapping an
  opt-in to that default for the run's literal, refused when there is none. (b) The first `optin =
  true` row the catalogue offers for the literal, in file order. (c) None, the slot left empty. (c)
  breaks the five-slot count (TOOL-dFairHearing-13 §8 F3); (b) runs a lens nobody chose. (a) keeps
  the swap the one mechanism and the fill a recorded choice. Recommendation (a). RESOLVED (agent,
  2026-11-02, delegated): (a), rung 3. This reads TOOL-dCalibratedLens-13's refusal of "an exclusion
  of a lens `review.opt-in` names" as an excluded opt-in KEY of that map, never a default it fills;
  the spec audit's interface axis is where the two specs are cross-read. widens: none · relaxes: none
- **F3 — Where is a declined proposal recorded?** (a) The `keep` record, keyed (`scenario`,
  `<After>`, date). (b) The owner's disposition record (TOOL-dDeclaredLoop-16), which lives in a
  build's folder under a unit id that a Loop Review does not have. (c) A new record kind, which shared
  interface S4 refuses. Recommendation (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, the
  charter's `[reuse]` rule. widens: none · relaxes: none
- **F4 — Where does a ratified scenario land?** The brief's row names `tools/loop/scenarios.toml`.
  (a) The overlay, a `[[scenario]]` row tagged `scenario.adopter.<name>`, written by
  `instructions_edit.py add --manifest overlay`. (b) Gov's pack `tools/loop/scenarios.toml`, whose one
  writer is `python tools/playbook/core.py new scenario` (TOOL-dDeclaredLoop-27 S1). The clause has
  the owner ratify "through `instructions.edit`", which writes the overlay and not gov's pack, so (b)
  fails the clause. Recommendation (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 1, the
  clause's text. widens: none · relaxes: none
- **F5 — What does the proposed row admit?** (a) It extends the carriers' common scenario and
  inherits its `admits`, `entry` and `then`, activating the carried row. (b) It admits a fact naming
  the variant, which placement must supply. Under (b) no build in flight carries that fact, so none
  could ever move to it, and the clause's in-flight half fails (veto 1). Carriers under two scenarios
  are two candidates, each needing two builds. Recommendation (a). RESOLVED (agent, 2026-11-02,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F6 — When does a build in flight comply?** (a) Its facts admit the scenario and its composition
  with it passes every check. (b) Its walked path also shows no `skip` against the promoted
  composition, by `compare_path`. (a) alone moves a build that already passed a step the promoted
  scenario adds an item to, so its record would claim a flow it did not walk. Recommendation (b),
  which includes (a). RESOLVED (agent, 2026-11-02, delegated): (b), rung 3. widens: none ·
  relaxes: none
- **F7 — How does the owner's write carry `promoted-from`?** PRIMITIVE GAP: PLAY-dOrderedCharter-15
  S7 defines the `Promoted-from` field and no flag passes it. (a) This unit adds `--promoted-from` to
  the write verbs. (b) An ask on dOrderedCharter, leaving the ratification without its edge until it
  lands, which fails the clause (veto 1). Recommendation (a). RESOLVED (agent, 2026-11-02,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F8 — Does the build's grant lift veto 2 for these files?** `tools/workflows/`, `tools/unattended/`,
  `tools/loop/`, `tools/playbook/` and `tools/policy/` are governance carriers. `cl-dClosedLoop-0471`
  names lens removal by a swap or an exclusion, a repository lens's replay result, the Loop Review's
  proposal, the ratification through `instructions.edit` with `promoted-from` edges, the move at a
  step boundary and each value of `flow.promote`; every file of §4's estimate is that change.
  RESOLVED (agent, 2026-11-02, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the exclusion fill, the replay field, the promotion route and its policy refusal
  · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft. The header carries `OPEN`, not the brief's `DRAFT`, which check
  12's header grammar (`tools/memory-tree/check-memory-hygiene.sh:2145`) does not admit.

## 10. Reuse audit

The seams extended: the swap is TOOL-dFairHearing-3's `review_pin.py` and `optIn`, so an exclusion
adds a check and no second removal mechanism; the candidates are TOOL-dDeclaredLoop-28's change
records and state rows, read as built; the decline is TOOL-dCalibratedLens-5's `keep` record; the
ratification is PLAY-dOrderedCharter-15's `instructions_edit.py` and its `Promoted-from` field; the
move is TOOL-dDeclaredLoop-27's `derive_step_scenarios` at the step boundary. `python
tools/codebase-map/reuse_lookup.py "propose a reusable flow variant from a change two builds
recorded"` returned name-stem neighbours only (`build`, `records`, `changed`, `build_run_model`), and
`python tools/codebase-map/reuse_lookup.py "take a default review lens out and fill its slot"`
returned `default_kits`, `DerivedDefault` and `derive_int_slots`, none a lens or a scenario: at base
no existing seam fits in code, because every seam named above is a DEFERRED spec. No hit disagreed with
source; the brief's row names `tools/loop/scenarios.toml` as the target, which §8 F4 corrects.

Recall terms used: `python tools/memory-recall/query.py "how does a build's recorded flow change
become a reusable scenario, and how is a lens taken out" --terms "flow.promote scenario promotion
promoted-from instructions.edit flow.adapt change record decline lens exclusion optIn swap"`
