# TOOL-aHoistedPass-8 — the recipe-mode question, measured instead of argued

**Status:** CLOSED · rev-4 · 2026-09-05 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-04-build-TOOL-aHoistedPass-8-recipe-probe.md](../build/2026-09-04-build-TOOL-aHoistedPass-8-recipe-probe.md) | research | — |
| [2026-09-05-prompt-TOOL-aHoistedPass-8-brief.md](../prompts/2026-09-05-prompt-TOOL-aHoistedPass-8-brief.md) | journal | — |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md](../reviews/2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md) | diff-review | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

Settle by measurement what a `recipe`-mode run actually gets when it follows the `passes-harnessed`
directive, and hand the owner one named fork with a recommendation. The unit lands a record and
changes no shipped byte, because the disagreement it is about was argued twice and never observed.

## 2. Scope (IN)

- **S1** — Run `bash tools/unattended/unattended.sh --plan <slug>` against the smallest honest
  `authorized-by: recipe` build, in a scratch snapshot repo, and record the exit code and the exact
  output. Run a control on a real build in the same snapshot so the result is attributable.
- **S2** — Feed `tools/workflows/unattended-build.js` the unit set S1 produces, and record whether it
  throws. Run a control with a non-empty set so the throw is attributable to emptiness.
- **S3** — Read `scope_of` and `check_waiver_scope` in `tools/unattended/unattended.sh`, record what
  the scope grammar can and cannot express, and record which callers read it.
- **S4** — Establish the size of the recipe-mode build population at `c4fcf5ad`.
- **S5** — Land the measurement at
  `memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-8-recipe-probe.md`, carrying
  `**Serves:** research TOOL-aHoistedPass-8`.
- **S6** — Carry the fork into §8 with a recommendation, and leave it OPEN for the owner.

**S1 through S4 were performed while this spec was written**, at `c4fcf5ad`, and §4 carries their
results rather than a plan to obtain them. What remains for the build pass is S5 and S6.

## 3. Non-goals (OUT)

- **This unit is not the fix.** `DIRECTIVES_CORE` (`unattended.sh:469`), `scope_of` (`:505-514`),
  `check_waiver_scope` (`:1163-1179`), the Skill's Scope cell (`SKILL.template.md:95`) and the
  protocol sentence (`UNATTENDED-PROTOCOL.md:637`) are all untouched.
- **The contradiction stays LIVE on the bar for the whole of this build and after it**, until the
  owner takes the §8 fork. `UNATTENDED-PROTOCOL.md:637` says recipe mode does not take the harness
  route while `unattended.sh:469` binds `passes-harnessed` with no scope segment, which `scope_of`
  resolves to `all`. Both halves ship green today and both keep shipping green after this unit lands.
- **No other unit of this build takes a side**, and this one does not either. It reports.
- Not a repair of `--plan`'s refusal wording, which §4 records as misleading for this input.
- No new gate leg, and no arm for `fail 45`. The `fail 45` branch has never been observed to fire and
  `memory/backlog/TOOL.md:309` (`TOOL-aScouredKit-34`) records three fixture attempts that failed;
  arming it belongs to whoever takes fork F1 option (a), not here.
- Not an answer to whether a recipe build ought to carry specs. The probe measures what the shipped
  code does with one that does not.

## 4. Design

### The question

`unattended.sh:469` declares seventeen core directives. `passes-harnessed:M6` is the last of them and
carries two fields, not three, so `scope_of` returns `all` — verified by evaluation, not by reading
alone. `UNATTENDED-PROTOCOL.md:637` states the opposite in prose: *"Recipe mode does not take it: its
pieces are not specs."* A carrier and a registry disagree, on the bar today. Nobody had established
which one is right, because no recipe-mode build has ever existed.

### The population

At `c4fcf5ad`, `memory/builds/` holds 93 folders and searching the whole memory tree for an
`authorized-by: recipe` value returns **no hit at all** — this build's folder does not exist there.
That zero is the CONTROL and it is not the measurement.

On the LANDING tree the pattern hits only inside this build's own folder, and the files are named by
the `gen:spec-records` table rather than retyped here: the design of record, this spec, and the
round-1 spec-audit record. **Zero build READMEs declare `recipe`**, which is the finding; every
`authorized-by:` value carried by a README in the corpus is `prompt`.

**No count is written into this paragraph, deliberately.** rev-1 stated one hit, rev-2 corrected AC7
to two and left this paragraph at one, and by the time round 1's review record landed the true figure
was three — a number that moves every time this build writes a record about itself. What AC7 grades
is CONTAINMENT, not arithmetic, and this paragraph now says the same thing the criterion does.

### What the driver requires of a recipe build

`SKILL.template.md:332-338` names what a `recipe` build folder declares: the six required keys
(`:261`), the generated-region marker pair, plus `authorized-by: recipe`, `playbook: <path>` and
`pieces: <n>`. `verb_plan` (`unattended.sh:2010`) never reads `authorized-by` at all. What it reads is
the units region of the README and `git ls-files "$dir/spec/*.md"` at `:2043`, so the fixture is
staged rather than merely written — an unstaged folder would report an empty spec set for a reason
that has nothing to do with recipe mode.

### The probe

A snapshot repo was built with `git archive HEAD | tar -x` into a short temp root, then `git init` and
`git add -A`, giving an index of all 1510 tracked paths at `c4fcf5ad`. One build folder was added and
staged: a README with the nine keys above, an empty `<!-- gen:build-units -->` pair, and no `spec/`
directory. Exit codes were captured without a pipe.

| # | observation | result |
|---|---|---|
| 1 | `--plan` on the recipe fixture | **exit 1**, `UNATTENDED check 19 FAILED — no tracked spec under this build, so every planned unit is MISSING …: memory/builds/<slug>/spec` |
| 2 | control: `--plan dBriefedPass` in the same snapshot | **exit 0**, `next: none - every tracked spec is terminal` |
| 3 | the harness with `units: []` | **throws** the `unattended-build.js` empty-`units` refusal, whose message opens `unattended-build: args carries no` |
| 4 | control: the harness with one unit | passes that refusal, throws later at the spec-audit's empty-subject-set message |

Observation 2 makes observation 1 attributable to the fixture rather than to the snapshot.
Observation 4 makes observation 3 attributable to the empty set rather than to the harness shim.

**Observation 3 was made under a shim, and that is stated rather than glossed.** A workflow script has
no node entrypoint: the runtime supplies `args`, `agent`, `workflow`, `phase` and `log`, and permits a
top-level `return`. The shim supplies those five and wraps the file's body in an `async function`; it
edits nothing else. The refusal it exercises is `unattended-build.js`'s empty-`units` throw, which is module-scope
control flow reached before any `agent()` call, so the shim reaches it by the same path the runtime
would. It is a measurement of the predicate, not of the runtime.

### Finding 1 — there is no `next:` line

The design of record expected `--plan` to emit a `next:` line for this fixture and asked for it to be
recorded. **It emits none.** `verb_plan` refuses at `:2045` — one step before the branch that would
have printed `next: none - no tracked spec grades as a unit` (`:2173`) — because the tracked spec set
is empty at `:2043`. A recipe run following `passes-harnessed` therefore gets a named refusal at exit
1 from the first command the route asks it to run.

**That refusal is misleading for this input.** It reports every planned unit as MISSING and points at
`<dir>/spec` as the thing to repair, which is the correct reading for a `slug` or `prompt` build with
an unstaged spec and the wrong reading for a build whose declared vocabulary is pieces. It blames the
build folder for a shape the mode is defined to have. Repairing it is not in this unit's scope.

### Finding 2 — the harness throws, second

If a run gets past `--plan` and hands the harness the empty set anyway, `unattended-build.js`'s
empty-`units` guard throws, and its message opens `unattended-build: args carries no`. So the route is
closed twice over, and the first closure is the
driver's, not the harness's.

### Finding 3 — the scope grammar compares for equality against one token

`check_waiver_scope:1172` is `if [ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]; then`, refusing at
`fail 45` on `:1173`. `$sc` is whatever `scope_of` returned, compared for **string equality** against
the literal `all` and against exactly one mode. `AUTH_MODES` is `slug prompt recipe` (`:478`). So a
scope can name every mode or one mode, and **"every mode but recipe" is inexpressible**. Evaluated
against the shipped `DIRECTIVES_CORE`: `passes-harnessed` → `all`, `parallel-when-disjoint` → `all`,
`researched` → `prompt`, `pieces-recorded` → `recipe`. No entry in the set names two modes, so the
grammar's shape has never had to.

### Finding 4 — the scope field decides exactly one thing

`scope_of` has one functional caller in the tracked tree: `check_waiver_scope:1167`. Nothing else
reads a directive's scope, and nothing anywhere grades whether a run FOLLOWED a directive. So the
scope field decides only whether `--waive <handle>` is legal for this run's mode. `fail 45` sets
`status=1` through `fail()` (`:327`), and preflight's `check_waiver_scope || true` call at `:2625`
does not lose that — `:2628` refuses on `status`.

The consequence is the one that matters for the fork. With the scope at `all`, a recipe run is bound
by a directive whose route refuses it, and its only sanctioned exit is `--waive passes-harnessed` —
legal for that run *precisely because* the scope is `all`. Narrowing the scope makes that waiver
illegal, which is correct only once the directive no longer binds recipe runs.

### Finding 5 — the protocol sentence is the accurate half

The design of record offered two decisions: widen the grammar, or leave the scope `all` and strike
`UNATTENDED-PROTOCOL.md:637`. **The measurement refutes the second.** That sentence says recipe mode
does not take the route, and observations 1 and 3 say the same thing about the shipped code. Striking
it would delete the true half of the disagreement and leave the protocol silent about a route that
refuses at exit 1. The false half is the registry entry.

### The fork this feeds

Stated as F1 in §8, open, with a recommendation. The probe does not resolve it.

### Files touched (estimate)

| path | change |
|---|---|
| `memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-8-recipe-probe.md` | new — the record, with the four observations, the two controls and the five findings |
| `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-8.md` | this file, status flipped at the close |
| `memory/builds/aHoistedPass/README.md` | generated regions only, re-rendered by `gen_build_index.py --write` |

No file under `tools/` is touched, and no gate leg is added or moved.

### Alternatives rejected

- **Staging the fixture in the live tree instead of a snapshot.** `memory/project/readme-contract.txt`
  has `gen_build_index.py --check-format` refuse a tracked build README named by no contract row, so a
  probe folder in the real tree would owe a row and a pin move for something nobody intends to keep.
- **Deciding the question from the code alone.** Reading `:469` and `:637` is how this disagreement
  survived two prior revisions. Finding 1 is the one nobody predicted, and only running it produced it.
- **Recommending the fix inside this unit.** Ruling D3 reserves the decision for the owner, and a
  probe that lands its own preferred change is not a probe.

## 5. Production-readiness checklist

- security — N/A. No code, no new surface, no new input path.
- perf / scale — N/A. The probe is two commands in a scratch clone, seconds.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the empty case IS the subject: the probe's whole finding is what
  two programs do with an empty unit set.
- observability — the record is the artifact; every figure in it names the command that produced it.
- risks — one, and it is disclosed in §3: the contradiction stays live on the bar until the owner
  decides. The probe does not make it worse and does not make it better.
- testing + left-shift gates — none owed. This unit adds no mechanism, so there is no class to gate.
  The measurement's own attribution is carried by controls 2 and 4 rather than by a test.
- migration / rollback — N/A. Rollback is deleting one record file.
- user docs — N/A. Nothing in `help/` describes recipe-mode scope.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --plan <slug>` runs against a staged
  `authorized-by: recipe` README with an empty `<!-- gen:build-units -->` pair and no `spec/`, it exits
  1 and prints `UNATTENDED check 19 FAILED` naming that build's `spec` path, and prints no line
  beginning `next:`.
- **AC2** — When the same snapshot runs `--plan dBriefedPass`, it exits 0 and prints
  `next: none - every tracked spec is terminal`, so AC1's refusal is attributable to the fixture.
- **AC3** — When `tools/workflows/unattended-build.js` is evaluated with `units: []`, it throws a
  message beginning `unattended-build: args carries no`. **The criterion asserts the MESSAGE and no
  line span**, because a span rots between authoring and landing and this one already did: rev-1 cited
  `:118-124` with the message at `:120-122`, correct at `c4fcf5ad`, and at BASE `e828f778` the guard
  is at `:182-188` with its message at `:184-186`. An acceptance criterion is executable, so it may
  not be anchored on a line range.
- **AC4** — When the same evaluation is given one unit, it passes that same guard and refuses later
  with the spec-audit's `no spec subjects could be pinned` message, so AC3 is attributable to the
  empty set.
- **AC5** — When `scope_of` is evaluated against the shipped `DIRECTIVES_CORE`, `passes-harnessed`
  prints `all` and `researched` prints `prompt`, confirming the entry at `unattended.sh:469` carries
  no scope segment.
- **AC6** — When `tools/unattended/unattended.sh:1172` is read, the comparison is
  `[ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]`, a single-token equality against `all` or one
  member of `AUTH_MODES`, so no mode list is expressible.
- **AC7** — When the tracked memory tree is searched for `authorized-by:[[:space:]]*recipe` on the
  landing tree, **every hit sits inside this build's own folder** and no `memory/builds/*/README.md`
  matches, so the value has no live subject. The criterion asserts CONTAINMENT and neither a count nor
  an enumeration: rev-1 said one file, rev-2 said two, and round 1's own review record made it three
  without any of them being wrong about the fact that matters. At `c4fcf5ad` the
  pattern has no hit at all, this build's folder not existing there; that is the control, and rev-2
  corrects rev-1, which named a hit at a base where the file did not exist.
- **AC8** — When the probe record lands in this build's `build/` folder carrying
  `**Serves:** research TOOL-aHoistedPass-8`, `bash tools/memory-tree/check-memory-hygiene.sh` exits 0
  — which is what grades the record's filename against the naming rule — and this spec's header
  `rev-2` appears in its §9.
- **AC9** — When the unit's commit is diffed, it touches no path under `tools/`, and
  `git grep -c "Recipe mode does not take it"` still returns 1 for each of
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` — the unit
  changed no shipped byte and took no side.

## 7. Gates

- **`memory hygiene`** (chunk `records`, subject `repo`, no guard) — every bar. It is the only leg
  this unit's output is on, because the output is a record.
- **No gate runs the probe**, and no gate is added by this unit. The measurement lives in a scratch
  snapshot that is deleted afterwards; what survives is the record, and nothing re-derives it. A later
  reader who needs it re-run has the commands in §4 and in the record.
- Nothing here needs a staged failing case, because nothing here is a new gate.

## 8. Open questions

- **F1 — how the `passes-harnessed` scope and `UNATTENDED-PROTOCOL.md:637` are reconciled.** OPEN;
  this unit measures, the owner decides.

  - **(a) Widen the scope grammar to a mode list**, and declare `passes-harnessed:M6:slug|prompt`.
    `check_waiver_scope:1172`'s equality becomes a membership test over a `|`-separated field, which
    `REVIEW_VERDICTS` (`unattended.sh:466`) already precedents as a shape in this file. `scope_of` is
    unchanged — it returns the third field whatever is in it. `DIRECTIVES_FLOOR="17"`
    (`.unattended.conf:87`) counts entries, not fields, and is unaffected: the set is 17 words with or
    without a third field. The Skill's Scope cell at `SKILL.template.md:95` moves with it, and the
    prose at `:101-107` gains the list case.
  - **(b) Leave the scope `all` and strike `UNATTENDED-PROTOCOL.md:637`.** **Refuted by finding 5**:
    that sentence is the accurate half, and striking it leaves the protocol silent about a route the
    driver refuses at exit 1.
  - **(c) Leave both, and let a recipe run waive the handle.** Available today at no cost, because the
    scope `all` is exactly what makes `--waive passes-harnessed` legal for a recipe run (finding 4).
    It spends an owner-visible waiver on every recipe run, forever, to relax a rule the protocol
    already says does not bind — and there has never been a recipe run to spend it.

  **Recommendation: (a).** It is the only option that makes the registry say what the code does, and
  it is small: one `case` in place of one `!=`, one field on one entry, one table cell. Its real price
  is not the diff. Any edit to `unattended.sh` owes the kit-version bump, which edits
  `SKILL.template.md`'s marker (`check-kit-versions.sh:179-192`) and so makes the unit an owner turn;
  and honest landing owes an arm for `fail 45`, which has never been observed to fire —
  `memory/backlog/TOOL.md:309` records three fixture attempts and why each failed, and that row, not
  the grammar, is the work. **Option (c) is the honest fallback if that price is refused**, and it
  should then be written down as a deliberate choice rather than left as the default nobody picked.

RESOLVED (agent, 2026-09-05, delegated): **F1 is NOT TAKEN, and that is the resolution rather than a deferral by omission.**
Two independent reasons, and either alone is sufficient. **First, this spec forbids it**: section 3
says "This unit is not the fix", "No other unit of this build takes a side, and this one does not
either. It reports", and AC9 requires the unit's commit to touch no path under `tools/`. Taking any
option here would fail M3 veto 1 against this unit's own acceptance. **Second, option (a) trips M3
veto 2**: it moves `SKILL.template.md`'s Scope cell and its prose, and ruling D1 put that file and
its render on the veto-2 list, which the mandate's delegation does not reach. Option (b) is already
refuted by finding 5.

**So what ships is option (c) — leave both — and this line is the deliberate record of that choice
rather than the default nobody picked**, which is precisely what the option's own text asks for. The
carrier/registry disagreement stays live on the bar exactly as section 3 says it does, and the fork
is PARKED to the owner in this run's run-state file so it reaches the wrap-up as a decision they
still hold.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `c4fcf5ad` with S1–S4 performed during the
  writing. Three corrections to the design of record, all silent in the sections above:
  - D3 asks the probe to record `--plan`'s *"exact `next:` line and the exit code"*. There is no
    `next:` line; `verb_plan` refuses at `:2045` before reaching any of the four `next:` shapes.
    Recorded as finding 1.
  - D3 and §7's U8 row offer two decisions and treat them as symmetric. Option (b) is refuted by the
    measurement, so §8 carries it marked refuted rather than as a live alternative, and adds (c),
    which the reading of `scope_of`'s single caller revealed.
  - D3 describes the harness half as *"the harness invoked with the unit set that produces"*. A
    workflow script cannot be invoked; §4 states the shim and its five stubbed globals, and adds
    control 4 so the throw is attributable.
  - Every design citation this unit depends on was re-opened at `c4fcf5ad` and **holds**:
    `unattended.sh:469`, `:478`, `:505-514`, `:1163-1179` with the comparison at `:1172` and `fail 45`
    at `:1173`, `:2043`, `unattended-build.js:118-124` with its message at `:120-122`,
    `UNATTENDED-PROTOCOL.md:637`, `SKILL.template.md:95`. No line number needed moving. **rev-4 marks
    one of those as since-expired: the `unattended-build.js` pair moved to `:182-188` and `:184-186`
    at BASE. The rest were re-derived at BASE by rev-3 and hold.**
- rev-2 · 2026-09-05 · AC7 CORRECTED, not merely re-pointed, and the correction is the reason this
  rev exists. rev-1 claimed that searching the memory tree for `authorized-by:[[:space:]]*recipe` at
  `c4fcf5ad` yields the design of record as its only hit. Re-run rather than re-read, that claim is
  false three ways. At `c4fcf5ad` the pattern has NO hit, because `memory/builds/aHoistedPass/` does
  not exist at that sha — it first appears in `fa273fc7`. On the landing tree the pattern has TWO
  hits, the design record and this spec, which quotes the pattern it searches for. And the design
  record has since been renamed, so rev-1's path is stale as well as mis-based. AC7 now asserts what
  the unit actually needs: on the landing tree every hit is inside this build's own folder, no build
  README matches, and the `c4fcf5ad` empty is stated as the control it is. The probe still has no
  live subject, which is the finding AC7 exists to carry.
  In the same pass, AC8's witness was re-pointed off the record's own filename, which does not exist
  until the unit lands, onto `bash tools/memory-tree/check-memory-hygiene.sh`, which is what grades
  that filename against the naming rule. Its `rev-1` self-reference is updated to `rev-2` to match
  this header, the pairing the hygiene gate checks.
- rev-3 - 2026-09-05 - M3 fork sweep under the standing mandate. F1 marked RESOLVED as NOT
  TAKEN, with both grounds recorded: this spec's own section 3 and AC9, and M3 veto 2 over
  `SKILL.template.md` under ruling D1. Option (c) ships and is written down as the choice. The fork
  is additionally parked to the owner through the driver, so it surfaces in the wrap-up. Premises
  re-derived at the run's BASE `e828f778` and BOTH HOLD, with exact line numbers: `DIRECTIVES_CORE`
  at `tools/unattended/unattended.sh:469` still carries `passes-harnessed:M6` with no scope segment,
  and `memory/guides/UNATTENDED-PROTOCOL.md:637` still reads "Recipe mode does not take it: its
  pieces are not specs."
- rev-4 - 2026-09-05 - folded round-1 spec-audit findings 36 and 30, both of them the same defect in
  two places: a citation that outlived its base, inside a unit whose entire product is a record a
  later reader re-opens. **36** - section 4 and AC3 anchored the harness's empty-`units` refusal at
  `unattended-build.js:118-124` with its message at `:120-122`, correct at `c4fcf5ad`; at BASE
  `e828f778` that guard is at `:182-188` with its message at `:184-186`, and `:118` reads
  `return out`. Every one of those spans is now gone from the prose and from the criterion, which
  asserts the MESSAGE TEXT the shim actually exercised - cite by NAME, not by span, because an AC is
  executable and a line range rots between authoring and landing. rev-3's own claim that no line
  number needed moving is marked as since-expired in place rather than deleted. **30** - section 4's
  population paragraph named a path that has never been tracked and a hit count rev-2 had already
  superseded. Rewritten, and rewritten WITHOUT a count: rev-1 said one, rev-2 said two, and round 1's
  review record made it three, so AC7 is restated to grade CONTAINMENT and the paragraph now says
  what the criterion says. Neither fold touches a path under `tools/`, so AC9 is unaffected.

## 10. Reuse audit

**No existing seam fits, and the unit builds nothing that could sit on one.** Its whole output is one
record file. `python tools/codebase-map/reuse_lookup.py "resolve an unattended directive's
authorization-mode scope and refuse a waiver a run's mode is not bound by"` returned a shortlist over
645 symbols, 188 inventory keys, 19 affordance seams and 20 dossiers; its ranked candidates are
unrelated resolvers (`resolve` in `tools/memory-recall/recall_conf.py`, `resolve_bash` in
`tools/run-gates/profile_bar.py`, `resolve_root` in `tools/memory-tree/row_grammar.py`) plus the
`unattended` affordance seam `.unattended.conf`, which is the conf channel and not the scope grammar.
The two functions this unit's findings are about, `scope_of` and `check_waiver_scope`, are absent from
the corpus by construction: `memory/map/generated/symbols.json` holds 769 symbols across `.py` (697)
and `.js` (72) files and no shell function at all, so no query could have surfaced them.

Recall terms used: passes-harnessed, DIRECTIVES_CORE, scope_of, check_waiver_scope, AUTH_MODES,
authorized-by recipe, verb_plan, unattended-build units refusal, waiver scope fail 45,
UNATTENDED-PROTOCOL section 12, DIRECTIVES_FLOOR, build README units region, pieces-recorded,
smallest honest fixture.
