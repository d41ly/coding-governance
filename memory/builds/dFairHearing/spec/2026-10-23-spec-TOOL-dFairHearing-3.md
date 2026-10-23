# TOOL-dFairHearing-3 — opt-in lenses swapped into a five-slot literal, and review.pin as the stand-in that maps them

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0070@00ce4e3c whole
**Carries:** node:item.review.pin
**Carries:** node:policy-key.review.opt-in

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-3-deviation-39.md](../build/2026-10-23-build-TOOL-dFairHearing-3-deviation-39.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-30 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-3-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-3-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-3-readers-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-3-readers-fix-brief.md) | research | TOOL-dFairHearing-9 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

A review cannot today aim a lens at security, alternatives, cost, portability, adopter migration or
topology unless the harness is edited, and the owner settled that a run opts in to such a lens by
swapping it for a named default of its preset (R-1, "Both"). This unit adds that swap: per-run
`optIn` and `preset` arguments, checked once at the argument boundary, that replace one default slot
of the five-element literal each, so the literal keeps five slots. It adds `review.pin`, run directly
with its pin arguments, as the stand-in that maps `review.opt-in` and the pinned revisions' record
kind to those two arguments until dDeclaredLoop's `review.trigger` lands (the whole-design audit's
C2-F6). It catalogues the six opt-in lenses as rows, each shipping on its losing test.

## 2. Scope (IN)

- **S1** — `tier2-review.template.js` takes `optIn`, `{ "<opt-in lens key>": "<default lens key it
  replaces>" }`, absent meaning `{}`. Its shape is refused before any agent where `intensity` and
  `preset` are checked: not a plain object, or a key or value that is not a lens-key string. Observed
  by AC1.
- **S2** — The swap: a rendered `OPTIN_LENSES` array of the shipped opt-in rows, and every default slot
  rendered as `deriveSlotLens('<literal>', { key, brief })`, which returns the opt-in row `optIn`
  maps to that slot's default when the slot belongs to the run's literal, carrying
  `replaces: <default key>`, and the slot unchanged otherwise. The literal keeps five elements after
  every swap. Observed by AC2 and AC6.
- **S3** — One membership check, beside the `lensNotes` check (:852-879) and before the resume probe,
  refuses by name, in this order: an opt-in that is already a lens of the run's literal; an opt-in no
  shipped row offers for that literal (absent, or folded into one of its defaults); a default named as
  an `optIn` value that the literal lacks; and one default named as the value of two `optIn` keys.
  Observed by AC3.
- **S4** — A light diff run selects its slots by each slot's DEFAULT key, so a swap into a light slot
  runs the opt-in there, and `LIGHT_LENSES` is checked against the default keys, never refused because
  a swap put an opt-in in one's slot (:843-850, :887-894). Observed by AC4.
- **S5** — `optIn` joins the review key's input print when it is not empty, and is announced: a log
  line per swap before the first agent, a RUN INTEGRITY line when a swap ran, and `optIn` on every
  return beside `intensity`. Observed by AC2 and AC5.
- **S6** — `tools/workflows/render_lenses.py` renders the slot wrapper and fills a token under the
  marker `// gov:lens-optins` with every `optin = true` row as `{ key, presets, brief }`; rule 11 of
  TOOL-dFairHearing-13 covers the new marker. Observed by AC2, AC6 and AC10.
- **S7** — Six rows in `tools/workflows/lenses.toml`, `default_in = []`, each with the brief and the
  literals §4 states, every one `optin = false` until its losing test is recorded (§8 F1). Observed by
  AC10.
- **S8** — `tools/workflows/review_pin.py`, the stand-in for `review.pin` (`item.review.pin`): given
  each pinned subject's path, the `review.opt-in` value and the design-record preset, it prints the
  `preset` and `optIn` arguments as one JSON line. A subject's record kind comes from the harness's own
  `SPEC_SUBJECT_PATH` (:317), read from the rendered harness beside it. Every subject a design record
  maps to the design-record preset, whose default is `unit-spec` (S9, dark); any spec subject maps to
  `unit-spec`. It checks `--opt-in`'s shape only: membership is S3's, once. Observed by AC7 and AC8.
- **S9** — `review.opt-in` (`policy-key.review.opt-in`): `none`, the default, or a JSON object keyed by
  literal name whose values are `optIn` maps, v2's "a set of named lenses, each replacing a named
  default lens of its preset". It is read only as `review_pin.py --opt-in`, the stand-in until a policy
  file route exists (shared interface S14). Observed by AC7.
- **S10** — `unattended-build.template.js` forwards `optIn` and `preset`, when its caller passes them,
  to the audit stage's review call (:1636-1663), unchecked: the callee's boundary is the one check.
  Its input header block documents both. Observed by AC9.
- **S11** — One ask row in `memory/builds/dCalibratedLens/BACKLOG.md` files the six losing tests (§8
  F1), its id the next `TOOL-dCalibratedLens-<n>` the index generator reports. `tools/workflows/README.md`
  documents `optIn`, the swap and `review_pin.py`. Observed by AC11.

## 3. Non-goals (OUT)

- Running the six losing tests: they are blind replays that need the bundle and known-set file the
  replay unit builds and the scorer factory, both ordered after this unit (§8 F1).
- A second pass of lenses, concatenation, or a sixth slot: the hook denies a literal grown past five
  and a filtered catalogue (the lens research, `[shape]`).
- Flipping the design-record preset to `design-audit`: the replay verdict of shared interface S9,
  `TOOL-dFairHearing-1`'s.
- The other policy keys read through `review.pin`'s arguments, `review.unclassed`, `review.twin`,
  `review.design-audit.runs` and `review.design-audit.seed`: their owning units add them.
- Invoking the harness. `review_pin.py` prints the arguments of one harness call and runs nothing; a
  key that needs several calls, such as `review.design-audit.runs`, prints one argument set per call
  for its caller to run, and that output is the owning unit's to add.
- Lens notes after a swap: `TOOL-dFairHearing-9`. Until it lands a note keyed to a replaced default
  is refused by today's check, since `LENS_KEYS` (:859) reads the swapped literal.
- A policy file, its loader, or the unattended skill calling `review_pin.py`: with no caller the
  default is `none`, which is today's behaviour.
- `REVIEW_SHAPE` (:970): a swapped prompt runs only under a key `optIn` separates (S5).

### Edges

- **consumes-from** `TOOL-dFairHearing-13` — the catalogue, its `optin` field and the renderer this unit extends with the wrapper and the opt-in marker
- **consumes-from** `TOOL-dFairHearing-2` — the `preset` argument and the design-audit literal a swap may target
- **hands-off** `TOOL-dFairHearing-9` — a lens note keyed to a default a swap replaced, which the post-swap `LENS_KEYS` refuses until it lands
- **hands-off** `TOOL-dFairHearing-1` — `review.pin`'s record-kind mapping, whose dark default the design-audit replay's verdict keeps or flips
- **hands-off** `TOOL-dFairHearing-11` — `review.twin`, read as a further `review.pin` argument
- **hands-off** `TOOL-dFairHearing-8` — `review.unclassed`, read as a further `review.pin` argument
- **hands-off** `TOOL-dFairHearing-18` — `review.design-audit.runs` and `review.design-audit.seed`, read as further `review.pin` arguments
- **hands-off** external — the six losing tests, filed as one ask in dCalibratedLens, the build that draws its stage lenses from this catalogue
- **hands-off** `TOOL-dFairHearing-23` — finding ids 3, 5, 7, 21, 35 and 50 of the round-1 spec audit: review_pin.py's per-run lines for whole-design (its S5, S6, AC3), keys printed only with their flags (its S11, AC5), the `gov:lens-optins` marker admitted by the renderer (its S14, AC7), AC5's key arm re-derived (its S29, AC20) and a backslashed subject refused (its S46, AC37)
- **hands-off** `TOOL-dFairHearing-32` — finding id 24 of the round-3 spec audit: this unit's AC7 arm reads its expected no-flag preset from `DESIGN_RECORD_PRESET` rather than the literal, so a replay-1 hit does not red it (its S19)

## 4. Design

### Evidence

- The hook admits a slot that is a call: measured 2026-10-23, a copy of `tools/workflows/tier2-review.js`
  whose first `SPEC_LENSES` slot reads `swapIn('coherence', { ... })` beside a six-element opt-in
  array that nothing fans over exits 0 from `node tools/hooks/agent-cap.js --only=scripts`; a sixth
  slot in the same copy exits 2. The hook counts top-level elements and refuses a spread
  (`tools/hooks/agent-cap.js:934-968`); it never reads an element's content.
- The lens research measured that concatenating opt-ins onto a preset and filtering a larger
  catalogue are both denied, and a swap admitted (`[shape]`, its lines 173-183).
- The light run's skip and the dead-key check read `LENS_KEYS` and `DIFF_LENSES` keys
  (`tools/workflows/tier2-review.template.js:846-850`, :890), so a swap that renamed a light slot
  would red the check on every light run.
- A note for a lens a run does not run is already accepted and reported unread, not refused
  (:895-901); that is the precedent TOOL-dFairHearing-9 extends.
- `SPEC_SUBJECT_PATH = /(?:^|\/)builds\/[^/]+\/spec\//` (:317) is the harness's one spelling of what a
  spec subject is; every other subject is a design subject (:313-316).
- The audit stage's review call passes a fixed argument set (:1636-1663) and validates nothing the
  callee refuses beyond two refusals it copies (:276), which it says it copies.

### The swap, in the template

Declared above the literals, because each slot calls into them when its literal is evaluated:

```js
const OPTIN_LENSES = [ // gov:lens-optins
{{LENS_SLOTS}}
]
const SLOT_LITERAL = isSpec ? preset : 'diff-review'
const SLOT_DEFAULTS = []                     // the run literal's default keys, in slot order
function deriveSlotLens(literal, L) {
  if (literal !== SLOT_LITERAL) return L
  SLOT_DEFAULTS.push(L.key)
  const k = Object.keys(optIn).find((x) => optIn[x] === L.key)
  const row = k && OPTIN_LENSES.find((r) => r.key === k && r.presets.indexOf(literal) !== -1)
  return row ? { key: row.key, brief: row.brief, replaces: L.key } : L
}
```

A rendered default slot keeps today's `key:` and brief lines, so TOOL-dFairHearing-13's comparison
of keys and briefs still holds:

```js
  deriveSlotLens('unit-spec', {
    key: 'coherence',
    brief:
      '...',
  }),
```

The S3 check runs after `LENSES` is chosen and reads `SLOT_DEFAULTS`, `OPTIN_LENSES` and `optIn`;
nothing it reads is an agent's output, so checking after the pure evaluation is still before any
spawn. The light selection becomes `LENSES.filter((L) => LIGHT_LENSES.indexOf(L.replaces || L.key) === -1)`
for the skipped slots, and the dead-key check compares `LIGHT_LENSES` with the diff literal's defaults.

### The six rows

Briefs are the lens research's (`[candidates]`, lines 140-172), each one line in the catalogue.

| key | kinds | presets | Why that set |
|---|---|---|---|
| `security` | `spec-audit` | `unit-spec` | the diff literal has a `security` default; the design-audit folds it into `failure-envelope` |
| `alternatives` | `diff-review`, `spec-audit` | `diff-review`, `unit-spec` | the design-audit folds it into `alternatives-and-cost` |
| `cost` | `diff-review`, `spec-audit` | `diff-review`, `unit-spec` | the same fold |
| `portability` | `diff-review` | `diff-review` | the review-system record scopes it to the diff kind (`[lenses]`, lines 146-147) |
| `adopter-migration` | `diff-review`, `spec-audit` | all three literals | none of the three carries it |
| `topology` | `diff-review`, `spec-audit` | all three literals | none of the three carries it |

Every row is `optin = false`. A row with no default and `optin = false` is catalogued and selectable
by nothing, which is the state of a lens awaiting its losing test; recording a test it did not lose
flips that row to `optin = true` and nothing else.

### review.pin's stand-in

```
python <kit>/review_pin.py --subject <path> [--subject <path> ...]
                           [--opt-in none|'<json>'] [--design-record-preset unit-spec|design-audit]
# stdout: {"preset": "<literal>"} or {"preset": "<literal>", "optIn": {"<opt-in>": "<default>"}}
```

`DESIGN_RECORD_PRESET = "unit-spec"` is the module default `--design-record-preset` falls back to;
the replay's verdict edits that one value. `read_spec_subject_path` reads the line
`const SPEC_SUBJECT_PATH = /.../` from the `tier2-review.js` beside the module and refuses, exit 2,
naming it, when the line is absent. `--opt-in` must be `none` or a JSON object of JSON objects of
strings; anything else exits 2 naming the flag. `optIn` is the value's entry for the chosen preset,
omitted when the value is `none` or has no entry for it. Usage errors exit 2. Output is LF bytes on
`sys.stdout.buffer`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/render_lenses.py`
- `tools/workflows/lenses.toml`
- `tools/workflows/review_pin.py`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js` (its render)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `memory/builds/dCalibratedLens/BACKLOG.md`

### Alternatives rejected

- **The swap at the prompt site, `LENSES` untouched.** Every reader keyed on `L.key`, the lens-yield
  table among them, would name the default, and the table is the witness the review-system record
  names for the policy value (§8 F2).
- **`review.pin` inside the build harness.** It has no filesystem, so it can read neither the policy
  value nor a record, and the clause has `review.pin` run directly (§8 F3).
- **A copy of the spec-subject regex in `review_pin.py`.** Two spellings of one predicate drift
  (§8 F4).
- **Re-checking `optIn` in the build harness**, as it copies two callee refusals (:276). The clause
  checks it once.

## 5. Production-readiness checklist

- security — `optIn` keys and values are shape-checked strings and are matched only against rendered
  catalogue keys; no value reaches a prompt except a catalogued brief. `review_pin.py` reads one
  sibling file and writes nothing.
- perf / scale — no agent added; the literal keeps five slots.
- error / empty / loading states — an absent or empty `optIn` is today's run with today's key; a
  catalogue with no shipped opt-in renders an empty `OPTIN_LENSES`, and every swap refuses as unknown.
- observability — each swap is logged, stated in RUN INTEGRITY, returned, and visible in the
  lens-yield table by its key.
- risks — a swap drops the replaced lens's coverage for the run, as the review-system record states;
  the log line names the dropped lens.
- testing — AC1 to AC11; the arms in §7.
- migration — none: every existing call passes no `optIn` and keeps its key; the new module and rows
  arrive under the kit's `**` rule.
- user docs — `tools/workflows/README.md`; no `help/` page covers the review harness.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  as `tools/workflows/tier2-review.test.sh:67-81` cuts it, `optIn: {}` proceeds, and `optIn: []`,
  `optIn: { topology: 7 }` and `optIn: { 'Topology!': 'reuse' }` each throw naming `optIn`.
  Red when: a malformed `optIn` reaches the literals.
- **AC2** — When a scratch render of `tools/workflows/tier2-review.template.js` over a scratch
  catalogue that sets `optin = true` on `topology` is run as an AsyncFunction, the shape
  the tier2-review suite's full-run arms use, as a unit-spec spec audit with
  `optIn: { topology: 'blast-radius' }`, its five finder prompts carry, in order, the briefs of
  `coherence`, `grounding`, `reuse`, `topology` and `failure-envelope`, and its return carries
  `optIn: { topology: 'blast-radius' }`.
  Red when: the swap adds a slot, drops one, or lands the opt-in in another slot.
  cost: a scratch harness modelled on that suite's stub agents.
- **AC3** — When the same scratch harness runs with `{ coherence: 'reuse' }`, `{ portability: 'reuse' }`,
  `{ topology: 'nope' }` and, over a catalogue that also ships `adopter-migration`,
  `{ topology: 'reuse', 'adopter-migration': 'reuse' }`, each throws before the stub `agent` is
  called, naming in turn: already a lens, no opt-in of `unit-spec`, no default `nope`, and `reuse`
  replaced twice.
  Red when: a refusal proceeds, fires after an agent, or names the wrong rule.
- **AC4** — When the scratch harness, over a catalogue that ships `portability`, runs a light diff
  review with `optIn: { portability: 'seams' }`, it proceeds, its three finder prompts carry
  `correctness`, `portability` and `verification`, and `skippedLenses` reads `security` and `intent`.
  Red when: the swap makes the dead-key check throw, or the light run drops the swapped slot.
- **AC5** — When the scratch harness derives the review key for one subject set with and without
  `optIn: { topology: 'blast-radius' }`, the keys differ, and the key without it equals the key
  base's harness derives for those args.
  Red when: a swapped run can resume an unswapped one's lens files, or an existing key moved.
- **AC6** — When `bash tools/workflows/check-verifier-fanout.sh <render>` runs on a scratch render
  over a catalogue shipping all six opt-ins, it exits 0 and every marked literal reads 5 slots.
  Red when: the wrapper or the opt-in array makes the hook deny the harness, or a literal's count moves.
- **AC7** — When `python 'tools/workflows/review_pin.py'` runs with one spec subject
  `'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md'`, it prints `{"preset": "unit-spec"}`; with two
  design subjects under `memory/builds/dX/build/`, `{"preset": "unit-spec"}`; with those two and
  `--design-record-preset design-audit`, `{"preset": "design-audit"}`; with one of each and that flag,
  `{"preset": "unit-spec"}`; and with the spec subject and
  `--opt-in '{"unit-spec": {"topology": "blast-radius"}}'`, an `optIn` of that map.
  Red when: a mixed set maps to `design-audit`, the dark default maps design records to
  `design-audit`, or the opt-in entry is lost.
- **AC8** — When `review_pin.py` runs from a scratch directory holding it beside a `tier2-review.js`
  with no `SPEC_SUBJECT_PATH` line, and when it runs with `--opt-in '[1]'` or no `--subject`, each
  exits 2 and its stderr names `SPEC_SUBJECT_PATH`, `--opt-in` or `--subject`.
  Red when: a missing predicate falls back to a guess, or a malformed value prints arguments.
- **AC9** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js`, the shape
  the unattended-build suite uses, with `specAudit` set passes
  `optIn: { topology: 'blast-radius' }` and `preset: 'design-audit'`, the audit's `workflow()` stub
  receives both keys unchanged; without them it receives neither key.
  Red when: the arguments are dropped, rewritten, or sent when the caller passed none.
- **AC10** — When `python -c "import tomllib; ..."` reads `'tools/workflows/lenses.toml'`, it finds the
  six keys of §4's table with the kinds and literals the table states, each `optin = false` and
  `default_in = []`; and the render of `tools/workflows/tier2-review.template.js` carries an empty
  `OPTIN_LENSES` body.
  Red when: a lens ships before its losing test, or a row's literals differ from the table.
- **AC11** — When `grep -n "losing test" memory/builds/dCalibratedLens/BACKLOG.md` runs, one ask row
  names the six lenses and accepts on each test recorded and each row it does not lose flipped to
  `optin = true`; and `grep -c "optIn" tools/workflows/README.md` counts at least one.
  Red when: the tests are deferred with no tracked ask, or the argument is undocumented.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 · the shape refusals, a swap over a scratch catalogue, the four named refusals, a light swap, the key, and the `review_pin.py` cases, red against the base harness and a tree with no `review_pin.py` · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · covers AC9 · an audit-stage run with and without the two arguments, red against the base harness that forwards neither · that suite's assertion floor, raised by the arms added

## 8. Open questions

- **F1 — How does each opt-in lens ship on its losing test, when the replay machinery lands after
  this unit?** Each test is a blind replay (the lens research, `[candidates]`), and the bundle, the
  known-set file and the scorer factory arrive with units ordered 13 and 15. (a) Run the six tests in
  this unit with replay machinery of its own. (b) Land the six rows `optin = false`, flip each only on
  a recorded test it does not lose, and file the six tests as one ask in dCalibratedLens. (c) Land
  them `optin = true` with the tests owed. (c) ships a lens before its test, against the clause's
  "each shipping on its losing test": veto 1. (a) builds a second scorer, which shared interface S10
  forbids and its conformance arm reds, and needs the known-set file before it exists: veto 1.
  (b) keeps the clause and leaves the tests tracked. Recommendation (b). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (b). widens: none · relaxes: none
- **F2 — Where does the swap apply?** (a) Inside each slot, by a wrapper call, so the literal keeps
  five elements and every reader sees the opt-in's key. (b) A catalogue concatenated or filtered into
  the receiver, which the hook denies. (c) At the prompt site, `LENSES` untouched, so the lens-yield
  table names the replaced default. (b) fails at the tool call; (c) loses the policy's witness.
  Recommendation (a), measured admitted. Rung 2, the hook probe in §4. RESOLVED (agent, 2026-10-23,
  delegated): (a). widens: none · relaxes: none
- **F3 — What form does `review.pin`'s stand-in take?** (a) A python command beside the harness, run
  directly by the caller, printing the arguments. (b) Logic inside the build harness, which has no
  filesystem and cannot read a policy value or a record. The clause has `review.pin` "run directly
  with its pin arguments". Recommendation (a). Rung 1, v2's `cl-dClosedLoop-0070`. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Where does `review_pin.py` learn what a spec subject is?** (a) A copy of the regex. (b) The
  harness's `SPEC_SUBJECT_PATH` line, read from the rendered harness beside it. (a) is a second
  answer to one question (charter `[one-fact]`). Recommendation (b). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (b). widens: none · relaxes: none
- **F5 — What does a set of design records map to before the replay's verdict?** (a) `design-audit`.
  (b) `unit-spec`, the module default, with `--design-record-preset` to run the other arm. Shared
  interface S9 ships the preset dark and gives the flip to the replay; the brief's commit records it
  (`3dca04036`, its second `Decided:` trailer). Recommendation (b). Rung 1. RESOLVED (agent,
  2026-10-23, delegated): (b). widens: none · relaxes: none
- **F6 — Does the build's grant lift veto 2?** `tools/workflows/` is a governance carrier on
  `PLAY-dClosedLoop-10`'s list; `cl-dClosedLoop-0070` names the opt-in lenses, the `optIn` and
  `preset` arguments, the argument-boundary check and `review.pin`. The ask row sits in another
  build's `BACKLOG.md`, which README rule 7 admits and which is no carrier. RESOLVED (agent,
  2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the
  opt-in swap, its catalogue rows and the review.pin stand-in in the review kit · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.
- rev-3 · 2026-10-23 · §3 · the round-3 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-32,
  which re-pins this unit's AC7 arm to `DESIGN_RECORD_PRESET`.

## 10. Reuse audit

The seams extended are the marked receiver's literals and the `lensNotes` boundary check in
`tools/workflows/tier2-review.template.js` (:842-879), the light selection beside them (:843-901),
TOOL-dFairHearing-13's renderer, and the audit stage's review call in
`tools/workflows/unattended-build.template.js` (:1636-1663). `review_pin.py` reads its predicate from
the harness's `SPEC_SUBJECT_PATH` (:317) rather than restating it. `python
tools/codebase-map/reuse_lookup.py "map the pinned record kind and a policy value to review harness
arguments"` ranked `records` in `tools/memory-tree/gotchas.py` and `load_policy` in
`tools/roles/roles_lib.py`; neither maps a subject to a review argument, and the roles policy file is
the roles kit's, not a review policy route, so no existing seam fits `review.pin` itself. `python
tools/codebase-map/reuse_lookup.py "forward a caller argument from the build harness to the review
sub-workflow"` returned name-stem neighbours only (`build`, `build_commit`); the forwarding precedent
is the spread arguments already in that call (`roles`, `efforts`, `checklist`). No hit disagreed with
source.

Recall terms used: `python tools/memory-recall/query.py "how does a review run opt in to a lens that
replaces a default lens" --terms "opt-in lens swap optIn review.pin review.opt-in five-element literal
losing test catalogue R-1"`
