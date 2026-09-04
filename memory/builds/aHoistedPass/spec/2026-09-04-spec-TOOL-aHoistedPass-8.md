# TOOL-aHoistedPass-8 — the recipe-mode question, measured instead of argued

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-aHoistedPass-1-design-pass.md](../build/2026-09-04-build-aHoistedPass-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

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

At `c4fcf5ad`, `memory/builds/` holds 93 folders. Searching the whole memory tree for a
`authorized-by: recipe` value returns exactly one file, `memory/builds/aHoistedPass/build/2026-09-04-build-aHoistedPass-1-design-pass.md`,
which is this build's own design document quoting the key. **Zero build READMEs declare `recipe`.**
Every `authorized-by:` value in the corpus is `prompt`.

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
| 3 | the harness with `units: []` | **throws** the `unattended-build.js:118-124` message, which opens `unattended-build: args carries no` |
| 4 | control: the harness with one unit | passes that refusal, throws later at the spec-audit's empty-subject-set message |

Observation 2 makes observation 1 attributable to the fixture rather than to the snapshot.
Observation 4 makes observation 3 attributable to the empty set rather than to the harness shim.

**Observation 3 was made under a shim, and that is stated rather than glossed.** A workflow script has
no node entrypoint: the runtime supplies `args`, `agent`, `workflow`, `phase` and `log`, and permits a
top-level `return`. The shim supplies those five and wraps the file's body in an `async function`; it
edits nothing else. The refusal it exercises is `unattended-build.js:118-124`, which is module-scope
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

If a run gets past `--plan` and hands the harness the empty set anyway, `unattended-build.js:118-124`
throws with its message at `:120-122`. So the route is closed twice over, and the first closure is the
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
- **AC3** — When `tools/workflows/unattended-build.js` is evaluated with `units: []`, it throws the
  message at `:120-122` beginning `unattended-build: args carries no`.
- **AC4** — When the same evaluation is given one unit, it passes `:118-124` and refuses later with
  the spec-audit's `no spec subjects could be pinned` message, so AC3 is attributable to the empty set.
- **AC5** — When `scope_of` is evaluated against the shipped `DIRECTIVES_CORE`, `passes-harnessed`
  prints `all` and `researched` prints `prompt`, confirming the entry at `unattended.sh:469` carries
  no scope segment.
- **AC6** — When `tools/unattended/unattended.sh:1172` is read, the comparison is
  `[ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]`, a single-token equality against `all` or one
  member of `AUTH_MODES`, so no mode list is expressible.
- **AC7** — When the memory tree is searched for `authorized-by:[[:space:]]*recipe` at `c4fcf5ad`, the
  only hit is `memory/builds/aHoistedPass/build/2026-09-04-build-aHoistedPass-1-design-pass.md` and no
  build README matches.
- **AC8** — When the record lands at
  `memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-8-recipe-probe.md` carrying
  `**Serves:** research TOOL-aHoistedPass-8`, `bash tools/memory-tree/check-memory-hygiene.sh` exits 0
  and this spec's `rev-1` appears in its §9.
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
    `UNATTENDED-PROTOCOL.md:637`, `SKILL.template.md:95`. No line number needed moving.

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
