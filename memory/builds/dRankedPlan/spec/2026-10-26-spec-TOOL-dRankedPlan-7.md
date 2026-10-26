# TOOL-dRankedPlan-7 — kickoff reads the plan as `plan.kickoff` says, and the attended brief is gated

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 16 · advances TOOL-dRankedPlan-17
**Carries:** cl-dClosedLoop-0375@33084fbd whole
**Carries:** node:policy-key.plan.kickoff

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |

<!-- /gen:spec-records -->

## 1. Goal

A session's kickoff ignores the plan today, and an attended brief is checked only for existing:
`check_prompt_brief` (`tools/unattended/unattended.sh:3763`) grades a brief only for a prompt-mode
run (`:3765`), and route rule R5 (`skills/session-kickoff/manifest-check.sh:1051-1052`) asks only
that the brief is a tracked file in the right folder (gap-plan-07). This unit makes the orientation
card show the plan's next build and use it as `plan.kickoff` says, with `offer-next`, `binding` and
`advisory` each seen on its planted case. It also grades an attended brief at route time by the same
record rules a run-built brief meets.

## 2. Scope (IN)

- **S1** — The plan's next build. `read_plan_next` in `skills/session-kickoff/manifest-check.sh`
  reads `<MEMORY_ROOT>/PLAN.md`, the plan view TOOL-dRankedPlan-1 generates (I2). The plan's next
  build is the first data row of the first table whose header carries a `Build` cell, read before
  any `## Unplaced` heading. Its slug is that row's `Build` cell, or the text of the markdown link
  the cell holds. No such row prints nothing. Observed by AC1, AC4.
- **S2** — The `plan —` cell. `render_plan_cell`, called by `render_card` (`manifest-check.sh:517`)
  directly after the `live —` line and after any `kickoff —` cell TOOL-dRankedPlan-8 placed there,
  prints `plan — next <slug> · <value>`, the value being `read_card_policy plan.kickoff`
  (TOOL-dPlacedRequest-2 S11). Its `skipped:` forms are:
  - `plan — skipped: no .memory-tree.conf in this tree`;
  - `plan — skipped: .memory-tree.conf declares no MEMORY_ROOT`;
  - `plan — skipped: <memroot>/PLAN.md is absent`;
  - `plan — skipped: <memroot>/PLAN.md places no build`;
  - `plan — skipped: plan.kickoff refused`.

  The first three spell the `live —` cell's reasons (`:521-528`). Observed by AC1, AC3, AC4.
- **S3** — `binding`. Route rule R8 in `check_card_route` (`manifest-check.sh:1006`) applies when
  `plan.kickoff` reads `binding`. It refuses a route whose `- build:` line names a build other than
  S1's next, as `MANIFEST route R8 REFUSED — line <n>: - build: <slug> — plan.kickoff is binding
  and the plan's next build is <next>; …`, in the existing refusal form (`:1060`), and nothing is
  appended. When S1 finds no next build, or the key is refused, R8 does not apply. The append then
  prints `plan — binding holds nothing: <the skipped reason>`, so a binding that could not bind is
  visible and is never mistaken for a pass. Observed by AC2, AC4.
- **S4** — `advisory`. When `plan.kickoff` reads `advisory` and a route lands naming a build other
  than S1's next, the append prints `plan — advice: the plan's next build is <next>; this route
  names <slug>`. The card keeps the `plan —` cell above the route, so the plan sits beside the
  session's own choice. Under `offer-next` the same route lands with no line, and the card's cell is
  the offer. Observed by AC1, AC3.
- **S5** — One brief-record grader, carried by two kits. The record rules of `check_prompt_brief`
  (`unattended.sh:3802-3820`, rules 1 to 5) become `check_brief_record <want>`, which reads a record
  on stdin and prints nothing, or `rule <n>` and the sub-head at fault on a second line. The
  sub-head list extraction of `read_brief_subheads` (`:3731-3733`) becomes `derive_brief_subheads`,
  which reads a brief skeleton on stdin and prints its `###` sub-heads under `## The brief`,
  `|`-joined. Both functions sit in ONE marked block, `# >>> brief_rules`, whose canonical copy is
  `tools/unattended/unattended.sh`. `check_prompt_brief` and `read_brief_subheads` call the block
  and keep every verdict they print today. `manifest-check.sh` carries the block inline,
  byte-identical, because the kickoff kit requires no other kit (`manifest-check.sh:490`). A
  `brief_rules` row in the parity table of `tools/lib/resolve-python.test.sh` (`:168-187`) holds
  the two copies equal. Observed by AC7, AC8.
- **S6** — The attended brief is gated. R5 keeps its two existence checks. Then, for a brief under
  `<memroot>/builds/<build>/prompts/`, it grades the brief file by `check_brief_record`, with the
  sub-heads `derive_brief_subheads` reads from this script's own `BRIEF_SKELETON`. It refuses with
  `MANIFEST route R5 REFUSED — line <n>: - brief: <path> — the brief does not stand on its own: rule
  <n>[, ### <sub-head>]; …`, and nothing is appended. The grade applies when the routed build's
  README front matter `opened:` is on or after `ATTENDED_BRIEF_CUTOFF`, a date literal in
  `manifest-check.sh`. A README with no readable `opened:` date is graded, as
  `check_prompt_brief` grades one (`unattended.sh:3777-3780`). A brief that is the build
  `README.md`, the unattended authorization, is not graded here, because preflight grades that run.
  Observed by AC5, AC6.
- **S7** — The key has a reader `check_policy.py`'s reader coverage sees. `scan_reader_keys`
  (`tools/policy/check_policy.py:479`) reads a shell reader only in the `policy.py get <key>` shape
  (`:433-434`), so `read_card_policy plan.kickoff` is no reader to it, and the key would red as
  unread once dRankedPlan lands. `READER_SHAPES` (`:423`) gains one row for shell files reading
  `read_card_policy <key>`, unless the row is present at this unit's build base. Observed by AC9.
- **S8** — The plants. `card-store.fixture.sh` (TOOL-dPlacedRequest-2 S12) gains the plants
  `plan-offer-next`, `plan-binding`, `plan-advisory`, `plan-absent`, `plan-unplaced`,
  `plan-refused`, `brief-attended` and `brief-grandfathered`. Each plants its `PLAN.md`, its stub
  policy value, its build README and its brief, prints its observation, and exits 0 when the
  observation holds. Observed by AC1 to AC6.
- **S9** — The words. `render_card`'s comment block (`manifest-check.sh:483-498`) names the `plan —`
  cell. The `check_card_route` comment (`:997-1004`) names R8 and R5's grade, and its does-not-check
  list stops naming the brief's content. `help/policy.md` names `plan.kickoff`'s consumer in the
  paragraph listing keys with consumers (`help/policy.md:8-15`). Where `help/orientation-card.md`
  (KICK-dKeptSession-13 S10) exists at the build base, its cell list gains the `plan —` line.
  Observed by AC10.
- **S10** — The kickoff kit's vintage `KIT_MANIFEST_VERSION` (`manifest-check.sh:46`) is bumped, as
  its comment (`:47-51`) requires when a shipped byte moves. `MANIFEST_FORMAT` stays. NOT OBSERVED:
  a version literal moving is the epoch check's to grade at the close, and no criterion of this unit
  adds anything it does not.

## 3. Non-goals (OUT)

- The plan view, `priority:` and their order: TOOL-dRankedPlan-1's. This unit reads `PLAN.md` and
  never renders, sorts or edits it.
- `BRIEF_SKELETON`'s fields and `check_brief_derived`, the red on a brief that types a plan field:
  TOOL-dRankedPlan-16's. S6 grades whatever sub-heads the skeleton lists at the build base. A
  predicate unit 16 adds to the run-built record grade belongs in the `brief_rules` block, so both
  callers meet it; that placement is unit 16's call.
- `check_prompt_brief`'s roster join (`unattended.sh:3827-3863`, fail 115): an attended route names
  its units directly and R3 and R4 check them, and an attended brief's `### Items` carries no
  `planned`, `stale`, `duplicate` or `parked` disposition to join.
- The `## The prompt` heading test (`check_prompt_heading`): rule 1 already refuses a brief file
  with no `## The brief` sub-heads, which is what a file without that heading is.
- A lease or claim on the plan's next build. `binding` holds the session to the next build even
  when another session holds it, and the card's `claims —` cell shows that holding.
- The plan's next ASK. The plan view lists builds (I2), and walkthrough unit 8 reads builds.
- `placement.check` and `item.entry.place-check`: TOOL-dPlacedRequest-3's. R8 does not call them.
- The full-kickoff gate, the `kickoff —` cell and `kickoff.runs`: TOOL-dRankedPlan-8's.
- Prose in `skills/session-kickoff/SKILL.md`: 122 bytes of headroom under its size row
  (`tools/template-size-limits.txt:63`), already spent by TOOL-dPlacedRequest-3 S5 and S6. The engine
  reads the cell through TOOL-dPlacedRequest-3 S6's Step 1.
- `read_card_policy` itself and the fixture's harness: TOOL-dPlacedRequest-2 S11 and S12.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `BRIEF_SKELETON`, whose `## The brief` sub-heads S6
  grades an attended brief by; without it, S6 has no list to grade against.
- **consumes-from** `TOOL-dRankedPlan-1` — `PLAN.md`, the generated view whose first placed row is
  S1's next build; without it, every cell is `skipped:` and R8 binds nothing.
- **consumes-from** `TOOL-dRankedPlan-8` — `render_card`, with the `kickoff —` cell that unit adds,
  which S2's `plan —` cell sits after.
- **consumes-from** external — TOOL-dPlacedRequest-2's `read_card_policy` (S11) and
  `card-store.fixture.sh` (S12), built before this build run because dPlacedRequest is a parent of
  dTotalRecall and dBoundRoles; this unit's dispatch is refused while either is absent at its base.

## 4. Design

### The cell and the binding

`read_plan_next` is one awk over `PLAN.md`, in the style of the `live —` cell's row count
(`manifest-check.sh:529`). It locates the `Build` column by its header cell, not by position, so a
column unit 1 adds does not move it. It strips one surrounding markdown link and whitespace from the
cell. It stops at the first `## Unplaced` heading, because a build listed there has no place in the
order (I2). `render_card` calls `render_plan_cell` once. `--card --append` reads `plan.kickoff` once
inside `check_card_route`, only when the body carries a route, since R8 and the advice line are the
only consumers at append. Both reads go through `read_card_policy plan.kickoff`, the kickoff kit's one
policy reader, and that call names the key as S7's row reads it.

Rule order in `check_card_route` is R1 to R5 in the existing awk (`:1016-1053`), then S6's grade of
the brief, then R8, then R6 (`:1054`). The grade and R8 read the route's `- build:` and `- brief:`
values from the body with the same line grammar the awk holds (`:1023-1024`). The advice line of S4
is printed only after every rule has passed, so a refused body prints no advice.

| `plan.kickoff` | The cell | A route naming the next build | A route naming another build |
|---|---|---|---|
| `offer-next` | `plan — next <slug> · offer-next` | lands | lands, no line |
| `binding` | `plan — next <slug> · binding` | lands | refused, R8 |
| `advisory` | `plan — next <slug> · advisory` | lands | lands, `plan — advice: …` |

### The shared grader

The block moves bytes, it does not rewrite rules. `check_brief_record` is the awk program of
`unattended.sh:3802-3820` with `want` taken from `$1`. `check_prompt_brief` replaces its inline awk
with `printf '%s\n' "$txt" | check_brief_record "$want"`, and `read_brief_subheads` replaces its
inline list awk with `derive_brief_subheads`. Each keeps its output byte for byte, which AC8 measures
over every tracked prompt record. The marker lines follow the house shape, for example
`# >>> brief_rules — canonical copy: unattended.sh in the unattended kit (byte-identical; gated)`.
The parity row is `brief_rules|$ROOT/$UNATTENDED_DIR/unattended.sh|$UNATTENDED_DIR/unattended.sh`,
beside the `kickoff_region` and `mempause_sh` rows whose canonical is also a kit file
(`resolve-python.test.sh:170`, `:179`).

`ATTENDED_BRIEF_CUTOFF` is the day after the date of the build pass that commits it. A build opened
before the gate existed keeps routing its brief as it does today, and every build opened after it is
graded. The measurement behind the cutoff is in §8 F4.

### Inventory

| Minted | Kind | Where |
|---|---|---|
| `read_plan_next` | function | `manifest-check.sh` |
| `render_plan_cell` | function | `manifest-check.sh` |
| `R8` | route rule | `check_card_route` |
| `check_brief_record` | function, in the `brief_rules` block | `unattended.sh`, copied into `manifest-check.sh` |
| `derive_brief_subheads` | function, in the `brief_rules` block | the same two files |
| `brief_rules` | parity marker stem | both files, and the parity table |
| `ATTENDED_BRIEF_CUTOFF` | date literal | `manifest-check.sh` |
| `plan-offer-next`, `plan-binding`, `plan-advisory`, `plan-absent`, `plan-unplaced`, `plan-refused`, `brief-attended`, `brief-grandfathered` | fixture plants | `card-store.fixture.sh` |

Each function leads with a verb the lexicon already declares (`read`, `render`, `check`, `derive`),
which the `lexicon naming predicates` leg grades at the close.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `skills/session-kickoff/card-store.fixture.sh`
- `tools/unattended/unattended.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/policy/check_policy.py`
- `help/policy.md`
- `help/orientation-card.md`, only where it exists at the build base

### Alternatives rejected

- R5 calling the unattended driver's grader at run time: `check_prompt_brief` is no verb. It is a
  preflight step behind `AUTH_MODE=prompt` (`unattended.sh:3765`) that exits through numbered
  `fail` codes, and the kickoff kit would gain a runtime sibling it does not require today. §8 F3.
- A second, hand-written copy of rules 1 to 5 in the kickoff kit: the charter's `[reuse]` rule
  forbids a copy with no parity gate.
- Reading `plan.kickoff` with a raw `policy.py get` in the kickoff kit: a second reader path beside
  `read_card_policy`, whose bounded call and refused form the card already has.

## 5. Production-readiness checklist

- security — no new write path. The brief is read from a tracked file inside the tree (R5's first
  check, `:1051`), and `PLAN.md` from `MEMORY_ROOT`; the slug read from `PLAN.md` is only compared
  as text, never used as a path.
- perf / scale — one awk over `PLAN.md` per card write, and one over the brief per routed append;
  `read_card_policy` is one bounded call per verb.
- error / empty / loading states — each absent source has its own `skipped:` form (S2). A binding
  that binds nothing says so (S3). An unreadable `opened:` date is graded, never skipped (S6).
- observability — the cell on every card, R8's and R5's named refusals, and the advice line.
- risks — a plan view whose next build another session holds blocks every route under `binding`
  until the plan or the key moves (§3). Briefs of builds opened before `ATTENDED_BRIEF_CUTOFF` stay
  ungraded by design.
- testing — S8's plants, each red and green, the new parity row, and AC8's equivalence over the
  tracked prompt records.
- migration — none: no stored format moves. Existing cards keep their lines, and a card written
  before this lands has no `plan —` cell until its next write.
- user docs — `help/policy.md`, and the card page where it exists (S9).

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant plan-offer-next` runs over a planted `PLAN.md`
  whose first placed row is `aFirst`, under an `## Unplaced` heading listing `aEarly`, with
  `plan.kickoff` at `offer-next`, the card carries `plan — next aFirst · offer-next`. A route
  naming `aSecond` then lands and the append prints no `plan — advice` line.
  Red when: the cell names `aEarly` or `aSecond`, or the route naming `aSecond` is refused.
- **AC2** — When `bash card-store.fixture.sh --plant plan-binding` runs with `plan.kickoff` at
  `binding`, a route naming `aSecond` prints `MANIFEST route R8 REFUSED` and leaves the card
  byte-identical, and the same body naming `aFirst` lands.
  Red when: the route naming `aSecond` lands under `binding`.
- **AC3** — When `bash card-store.fixture.sh --plant plan-advisory` runs with `plan.kickoff` at
  `advisory`, the card carries `plan — next aFirst · advisory`, and a route naming `aSecond` lands
  and the append prints `plan — advice: the plan's next build is aFirst; this route names aSecond`.
  Red when: the advice line is absent, or the route is refused.
- **AC4** — When `bash card-store.fixture.sh --plant <case>` runs `plan-absent` (no `PLAN.md`),
  `plan-unplaced` (a `PLAN.md` whose builds all sit under `## Unplaced`) and `plan-refused` (the stub
  policy refusing `plan.kickoff`), each under `binding`, the card carries
  a `plan — skipped:` cell whose reason ends `PLAN.md is absent`, `PLAN.md places no build` and
  `plan.kickoff refused` in turn. In each case a route naming `aSecond` lands and the append
  prints `plan — binding holds nothing:`.
  Red when: R8 refuses a route with no next build to hold it to, or a cell is missing.
- **AC5** — When `bash card-store.fixture.sh --plant brief-attended` routes a brief under the build's
  `prompts/` folder whose `## Owner confirmation` section is empty, in a build opened after
  `ATTENDED_BRIEF_CUTOFF`, the append prints `MANIFEST route R5 REFUSED` naming `rule 4` and leaves
  the card byte-identical. The same brief with `Asked:` and `Answer:` lines lands. A brief missing
  `### Acceptance` is refused naming `rule 1` and `### Acceptance`.
  Red when: R5 checks existence alone and the incomplete brief lands.
- **AC6** — When `bash card-store.fixture.sh --plant brief-grandfathered` routes the incomplete brief
  of AC5 in a build whose README `opened:` is before `ATTENDED_BRIEF_CUTOFF`, it lands. The same
  brief in a build whose README carries no `opened:` key is refused by R5.
  Red when: the grandfathered build is refused, or the build with no date is waved through.
- **AC7** — When `sed -n '/^# >>> brief_rules/,/^# <<< brief_rules/p'` runs over
  `tools/unattended/unattended.sh` and over `skills/session-kickoff/manifest-check.sh`, the two
  outputs are byte-identical and non-empty.
  Red when: one copy is edited alone, or either file carries no block.
- **AC8** — When the rules awk of `check_prompt_brief` as it stands at base `0689e7fa`
  (`unattended.sh:3802-3820`, read from that commit's blob) and `check_brief_record` sourced from
  the block both run over every tracked `*-brief.md` under a build's `prompts/` that
  carries `## The prompt`, with `want` set to `BRIEF_FIVE` and then to the skeleton's list, their
  outputs are identical for every record.
  Red when: the move changed a rule, and any one record grades differently.
  figure: 149 records, 25 passing and 124 failing on the seven-sub-head list, PINNED by a probe on
  2026-10-26 at `911a70393`; the observation re-derives the population at run time.
- **AC9** — When `scan_reader_keys` (`check_policy.py:479`) runs over the built tree, through
  `PYTHONPATH=tools/policy python -c "import check_policy as c; print(c.scan_reader_keys('.'))"`,
  the set it prints holds `plan.kickoff`.
  Red when: the key is read only through a call shape `READER_SHAPES` does not read.
- **AC10** — When `grep -n 'plan.kickoff' help/policy.md` runs, it names the orientation card's
  `plan —` cell and route rule R8 as the key's consumer.
  Red when: the page still says every key other than the listed families changes no behaviour, with
  `plan.kickoff` read by the card.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · S8's plants, the failing case a route naming `aSecond` landing under `binding` and an incomplete attended brief landing · none

New arm: tools/lib/resolve-python.test.sh · covers AC7 · the `brief_rules` parity row, the failing case one copy edited alone · none

The unattended suite's existing `check_prompt_brief` cases (`tools/unattended/unattended.test.sh`)
re-observe AC8's equivalence at the close; they are not a new arm.

## 8. Open questions

- **F1 — What is "the plan's next item"?** Options: (a) the first placed build of the plan view;
  (b) the first open ask; (c) the first build no lease holds. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1. Walkthrough planned unit 8 reads "Kickoff reads the plan", and the plan
  record of P1 is builds ordered in a generated view (walkthrough:338-339, :351); I2's rows are builds. (c)
  needs a lease column I2 does not carry. widens: none · relaxes: none
- **F2 — Where is `binding` enforced?** Options: (a) a new route rule R8 in `check_card_route`; (b)
  `placement.check` (TOOL-dPlacedRequest-3); (c) prose in `SKILL.md`. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. The route is the line a session commits to a build with, and the write
  gate reads it. (b) is a parent's mechanism, and (c) has no byte budget and no refusal. R8 is the
  next number after TOOL-dPlacedRequest-2 S9's R7. widens: none · relaxes: none
- **F3 — How is an attended brief graded?** Options: (a) R5 runs the unattended driver's grader
  through `resolve_kit_file`, skipping where the driver is absent; (b) the record rules move into
  one parity-gated block, canonical in the unattended kit, carried inline by the kickoff kit; (c)
  the kickoff kit owns the rules and the driver runs the checker's blob at BASE for them, as
  `read_brief_subheads` runs it for `--brief-skeleton`. RESOLVED (agent, 2026-10-26, delegated):
  (b), rung 3. The scout's rung 2 probe question resolves by reading: `check_prompt_brief` is no
  verb and is gated to `AUTH_MODE=prompt` (`unattended.sh:3765`), so (a) has nothing to call without
  new driver surface, and its skip leaves an adopter without the driver ungated. (c) makes the
  run-built verdict depend on the kickoff checker's blob at BASE answering a new verb, a second
  failure point beside fail 117. (b) gates both kinds of brief with one predicate in every install,
  on the house pattern of inline copies held by the parity table. widens: none · relaxes: none
- **F4 — Which attended briefs does R5 grade?** Options: (a) every routed brief; (b) a brief whose
  build was opened on or after `.unattended.conf`'s `PROMPT_BRIEF_CUTOFF`, 2026-10-10; (c) a new
  `.memory-tree.conf` key; (d) a date literal in `manifest-check.sh`. RESOLVED (agent, 2026-10-26,
  delegated): (d), rung 3. A probe on 2026-10-26 graded the 149 tracked prompt records carrying
  `## The prompt` by rules 1 to 5 over the skeleton's seven sub-heads: 124 fail, 80 of them on rule
  3, and all are dated on or after 2026-10-11. So (a) and (b) refuse a route a resumed session sends
  for a build it already holds. (c) is a new key in an adopter's conf, a public surface veto 2
  discards. (d) grades every build opened after the gate exists and strands none.
  widens: none · relaxes: none
- **FACT-QUESTION · F5 — Does reader coverage see `read_card_policy plan.kickoff`?** Probe: read
  `READER_SHAPES` (`tools/policy/check_policy.py:423-435`) for a shell row matching a
  `read_card_policy <key>` call. Liveness: the same row set reads `policy.py get plan.kickoff` as a
  reader, so the probe can answer yes. Observation at `0689e7fa`: the one shell row reads only
  `policy\.py["']?[ \t]+get`, so the answer is no. RESOLVED (agent, 2026-10-26, delegated): S7 adds
  the row when the build base still lacks it. The same hole reds every card key TOOL-dPlacedRequest-2
  S11 reads once dPlacedRequest lands, so the main loop files this ask once. Ask for
  dPlacedRequest: READER_SHAPES reads `read_card_policy <key>` as a reader of `<key>`. Accept: when
  `scan_reader_keys` runs over a planted shell file whose one read of a key is `read_card_policy
  <key>`, it returns that key. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, the spec brief's I2, I5, I14 and
  I15, walkthrough P4 and planned unit 8 (walkthrough:351),
  night-pass point 1 item 7 (night-pass:111), and scout A's row 2 and forks F7a-c.

## 10. Reuse audit

The seams this unit extends, each read at `0689e7fa` and cited above. The `live —` cell of
`render_card` (`skills/session-kickoff/manifest-check.sh:517-531`) is the model for the `plan —`
cell. The rule awk of `check_card_route` (`:1006-1062`, R5 at `:1051-1052`, R6 at `:1054`) is where
R8 and R5's grade join. The record rules of `check_prompt_brief`
(`tools/unattended/unattended.sh:3802-3820`) and the list awk of `read_brief_subheads` (`:3731-3733`)
move into the shared block. The parity table (`tools/lib/resolve-python.test.sh:168-187`) gains a
row in the shape of the `kickoff_region` row (`:170`). `READER_SHAPES`
(`tools/policy/check_policy.py:423-435`) gains a row. The parent seams are TOOL-dPlacedRequest-2 S11
and S12.

`python tools/codebase-map/reuse_lookup.py "kickoff card offers the next planned build and refuses a
route to another build"` and `… "grade a prompt brief record's sub-heads and owner confirmation"`
each returned a shortlist of name-stem matches, such as `build_commit`, `render_record` and
`check_records`, and named no card, route or brief seam. The seams above come from reading source.

Where the scout record and source disagree: scout A's F7c offers R5 calling "`unattended.sh`'s
grader", but no such verb exists, since `check_prompt_brief` is a preflight step behind
`AUTH_MODE=prompt` (`:3765`). Scout A proposed a `Lease` column for the view, and the spec brief's I2
carries `Dormant` and `Plan` instead; this spec follows I2. The scout's line numbers for
`render_card` (`:517`), R5 (`:1051-1052`) and `check_prompt_brief` (`:3763`) match HEAD.

Recall terms used: `python tools/memory-recall/query.py "how does kickoff use the plan's next build
and gate an attended brief like a run-built one" --terms "plan.kickoff offer-next binding advisory
render_card check_card_route R5 check_prompt_brief BRIEF_SKELETON attended brief gap-plan-07"`. The
top hits were scout A's row 2 and the spec brief, then walkthrough:378 and TOOL-aRoutedQuill-7, the
unit that made the driver read the kickoff skeleton.
