**Serves:** research TOOL-aHoistedPass-8

# The recipe-mode probe — what a `recipe` run actually gets from `passes-harnessed`

*Node `a`, 2026-09-05. Four observations, two controls, five findings. Every figure below names the
command that produced it. The unit that owns this record changes no shipped byte and takes no side;
what it does is replace an argument with a measurement.*

## Why this exists

`tools/unattended/unattended.sh:469` declares seventeen core directives. The last of them,
`passes-harnessed:M6`, carries two fields rather than three, so `scope_of` returns `all` — every
authorization mode is bound. `memory/guides/UNATTENDED-PROTOCOL.md:637` states the opposite in prose:
*"Recipe mode does not take it: its pieces are not specs."* A carrier and a registry disagree, both
halves ship green, and nobody had established which one is right, because no recipe-mode build has
ever existed. Two prior revisions tried to settle it by reading the code. Finding 1 below is the one
nobody predicted from reading, and only running it produced it.

## The base this was measured at, and why it was measured twice

**Every observation below was re-run at the run's BASE `e828f778`.** The unit's spec took them at
`c4fcf5ad`, 66 commits earlier, and its own rev-4 had to fold a finding that one of the cited
mechanisms had MOVED between the two bases — the harness's empty-`units` guard went from `:118-124`
to `:182-188`. A record whose entire value is that a later reader can re-open it must not carry a
measurement from a tree that no longer exists. **All four observations reproduce at BASE**, with the
same exit codes and the same message text; the differences are stated where they exist and they are
in the harness, not in the result.

## The snapshot and the fixture

A snapshot repo was built with `git archive e828f778 | tar -x` into a short temp root — short because
a clone into a deep scratch path hits `MAX_PATH` on this node — then `git init` and `git add -A`,
giving an index of **1572 tracked paths** at BASE.

One build folder was added and STAGED: `memory/builds/aRecipeProbe/README.md` carrying the six
required keys plus `authorized-by: recipe`, `playbook:` and `pieces:`, an empty
`<!-- gen:build-units -->` marker pair, and **no `spec/` directory at all**. Staged rather than merely
written, because `verb_plan` reads `git ls-files "$dir/spec/*.md"`, so an unstaged folder would report
an empty spec set for a reason that has nothing to do with recipe mode.

The fixture lives in the snapshot and never in the live tree. `memory/project/readme-contract.txt`
has `gen_build_index.py --check-format` refuse a tracked build README named by no contract row, so a
probe folder in the real tree would owe a registry row and a pin move for a folder nobody intends to
keep.

## The four observations

Exit codes captured WITHOUT a pipe, because a pipe returns the pipe's status.

| # | observation | result at BASE `e828f778` |
|---|---|---|
| 1 | `--plan aRecipeProbe` on the recipe fixture | **exit 1** — `UNATTENDED check 19 FAILED — no tracked spec under this build, so every planned unit is MISSING; …: memory/builds/aRecipeProbe/spec`. **No line beginning `next:` is printed.** |
| 2 | *control* — `--plan dBriefedPass` in the same snapshot | **exit 0** — five `CLOSED DONE` rows, then `roster: the README roster region, 5 id(s); 0 with no tracked spec` and `next: none - every tracked spec is terminal` |
| 3 | `unattended-build.js` evaluated with `units: []` | **throws** — `unattended-build: args carries no `units`. The caller derives them from `--plan`…` |
| 4 | *control* — the same evaluation with one unit | **throws later** — `unattended-build: no spec subjects could be pinned at round 1. A spec-audit over an empty subject set would grade nothing…` |

Observation 2 makes observation 1 attributable to the FIXTURE rather than to the snapshot.
Observation 4 makes observation 3 attributable to the EMPTY SET rather than to the shim: the one-unit
case passes the guard observation 3 trips and refuses at a later stage for a different, named reason.

**Observation 3 and 4 were made under a shim, stated rather than glossed.** A workflow script has no
node entrypoint: the runtime supplies its globals and permits a top-level `return`. The shim supplies
stubs and wraps the file's body in an `async function`; it edits nothing else beyond turning
`export const meta` into `const meta`. The refusal it exercises is module-scope control flow reached
before any `agent()` call, so the shim reaches it by the same path the runtime would. It measures the
predicate, not the runtime.

**One difference from the `c4fcf5ad` run, and it is the shim's:** at BASE the script also references
a `parallel` global, so the first shim attempt at observation 4 died on `parallel is not defined`
before reaching any refusal of the script's own. Adding that stub produced the message in the table.
Observation 3 was unaffected in both shims, because its guard sits above that use. Recorded because
a reader re-running this needs to know the shim is a moving part and the guard is not.

## Finding 1 — there is no `next:` line, and the route refuses at its first command

The design of record expected `--plan` to emit a `next:` line for this fixture and asked for it to be
recorded. **It emits none.** `verb_plan` refuses at `tools/unattended/unattended.sh:2045` — one step
before the branch that would have printed `next: none - no tracked spec grades as a unit` at `:2173` —
because the tracked spec set is empty at `:2043`. A recipe run following `passes-harnessed` therefore
receives a named refusal at exit 1 from the first command the route asks it to run.

**That refusal is misleading for this input.** It reports every planned unit as MISSING and points at
`<dir>/spec` as the thing to repair, which is the correct reading for a `slug` or `prompt` build with
an unstaged spec and the wrong reading for a build whose declared vocabulary is pieces. It blames the
build folder for a shape the mode is defined to have. Repairing the wording is out of the owning
unit's scope and is named as such in its section 3.

## Finding 2 — the harness throws, second

If a run gets past `--plan` and hands the harness the empty set anyway, `unattended-build.js`'s
empty-`units` guard throws with a message opening `unattended-build: args carries no`. So the route is
closed twice over, and **the first closure is the driver's, not the harness's** — which matters,
because a reader who knows only the harness would conclude the route is merely unwired rather than
refused.

The guard is cited here by MESSAGE and not by span. Its address moved between the two bases this
record straddles, and that is precisely the class of citation a record like this must not carry.

## Finding 3 — the scope grammar compares for equality against one token

`check_waiver_scope` at `tools/unattended/unattended.sh:1172` is
`if [ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]; then`, refusing at `fail 45` on `:1173`. `$sc`
is whatever `scope_of` returned, compared for **string equality** against the literal `all` and
against exactly one mode. `AUTH_MODES` is `slug prompt recipe` (`:478`).

So a scope can name **every mode or one mode, and "every mode but recipe" is inexpressible.** Evaluated
against the shipped `DIRECTIVES_CORE` at BASE — 17 entries, `scope_of` sourced out of the driver and
run:

| handle | `scope_of` returns |
|---|---|
| `passes-harnessed` | `all` |
| `parallel-when-disjoint` | `all` |
| `researched` | `prompt` |
| `pieces-recorded` | `recipe` |

No entry in the shipped set names two modes, so the grammar's shape has never had to.

## Finding 4 — the scope field decides exactly one thing

`scope_of` has ONE functional caller in the tracked tree, `check_waiver_scope:1167`. Nothing else
reads a directive's scope, and **nothing anywhere grades whether a run FOLLOWED a directive.** So the
scope field decides only whether `--waive <handle>` is legal for this run's mode. `fail 45` sets
`status=1` through `fail()` at `:327`, and preflight's `check_waiver_scope || true` call at `:2625`
does not lose that, because `:2628` refuses on `status`.

The consequence is the one that matters for the fork. With the scope at `all`, a recipe run is bound
by a directive whose route refuses it, and its only sanctioned exit is `--waive passes-harnessed` —
legal for that run *precisely because* the scope is `all`. **Narrowing the scope makes that waiver
illegal**, which is correct only once the directive no longer binds recipe runs. The two edits are one
edit.

## Finding 5 — the protocol sentence is the accurate half

The design of record offered two decisions: widen the grammar, or leave the scope `all` and strike
`UNATTENDED-PROTOCOL.md:637`. **The measurement refutes the second.** That sentence says recipe mode
does not take the route, and observations 1 and 3 say the same thing about the shipped code. Striking
it would delete the true half of the disagreement and leave the protocol silent about a route that
refuses at exit 1. **The false half is the registry entry.**

## The population — the value has no live subject

Searched at BASE for `authorized-by:[[:space:]]*recipe` across the tracked memory tree: **every hit
sits inside this build's own folder**, and **no `memory/builds/*/README.md` matches at all**. Every
`authorized-by:` value carried by a build README in this corpus is `prompt`.

At `c4fcf5ad` the pattern has NO hit, because this build's folder does not exist at that sha. That
zero is the CONTROL and it is not the measurement.

**No count is written into this paragraph, deliberately.** The figure moves every time this build
writes another record about itself — it was one, then two, then three across three revisions of the
owning spec, none of them wrong about the fact that matters. What is asserted is CONTAINMENT.

## What this record does not settle

The fork. It is carried in the owning spec's section 8 with a recommendation and marked NOT TAKEN,
for two independent reasons either of which suffices: the spec's own section 3 and AC9 forbid this
unit from touching anything under `tools/`, and the recommended option moves `SKILL.template.md`'s
Scope cell, which ruling D1 put on the M3 veto-2 list that a standing mandate's delegation does not
reach. What ships is "leave both", written down as a deliberate choice rather than left as the
default nobody picked, and the fork is parked to the owner in this run's run-state file.

**The carrier and the registry therefore still disagree, on the bar, after this lands.** That is the
disclosed cost, not an oversight.
