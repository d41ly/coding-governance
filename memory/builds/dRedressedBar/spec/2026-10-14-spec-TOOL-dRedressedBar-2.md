# TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb

**Status:** CLOSED · rev-3 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |
| [2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-2-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-3-spec-writer.md) | journal | — |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |

<!-- /gen:spec-records -->

## 1. Goal

`lexicon naming predicates` and `lexicon wiring` are red at `ebce889c`, each reading 1088 verb
offenders against `VERB_OFFENDER_PIN="1087"` (`.lexicon.conf:268`). The one arrival since the pin was
set is the arrow helper `clean` in `tools/unattended/gate-guard.js:689`. Renaming it to lead with a
declared verb brings the count back to the pin, so both legs go green with no pin moved.

## 2. Scope (IN)

- **S1** — `extractAskQuestions` in `tools/unattended/gate-guard.js` names its local helper
  `renderAskQuote` where it now names `clean`: the declaration at line 689 and its two calls at lines
  694 and 696. Observed by AC1.
- **S2** — The helper's behaviour does not move. It still turns any value into a string, strips the
  C0 and C1 control characters, and cuts the result to `ASK_QUOTE_MAX` characters. Observed by AC2.
- **S3** — The new name leads with `render`, a verb the `VERBS:` table declares
  (`.lexicon.conf:555-578`), so the definition leaves the P1 offender population and the count meets
  the pin it was set against. Observed by AC3.
- **S4** — The retired name `clean` has no reader outside `extractAskQuestions` but the generated
  symbol index, which S5 rewrites.
  **Readers:**
  by name: `tools/unattended/gate-guard.js` lines 694 and 696, both inside the function that declares
  it. `memory/map/generated/symbols.json`, whose entry at lines 5420-5424 lists `clean` as a function
  of `tools/unattended/gate-guard.js`; it is a generated reader, and S5 rewrites it in the same
  commit. No other file in this tree. The `clean` in `tools/unattended/check-unattended.sh:1861` is
  an unrelated awk function and is not this helper.
  by value: NO VALUE READERS — the helper is a local closure that `module.exports` at line 796 does
  not export, so nothing outside the function compares, counts or derives from it.
  Observed by AC1 and AC4.
- **S5** — The symbol index moves with the name. After S1, the pass runs
  `python tools/codebase-map/gen_map.py --write` alone, before the product commit. That one commit
  carries `tools/unattended/gate-guard.js` and `memory/map/generated/symbols.json`, and the map then
  lists `renderAskQuote` for `tools/unattended/gate-guard.js` and no `clean` entry for that file. If
  `--write` moves any other path, the pass commits nothing and returns to the main loop, because the
  map read fresh before this unit (§4, "The symbol index"). Observed by AC4.

## 3. Non-goals (OUT)

- No change to `.lexicon.conf`. `VERB_OFFENDER_PIN` stays at 1087, and no `VERBS:` row, canon cluster
  or waiver is added for `clean`. The brief's non-goal bars a pin raised to absorb a red a code change
  can fix.
- No rename of the awk `clean` in `tools/unattended/check-unattended.sh:1861`. It counted toward the pin
  when 1087 was set at `301a36664`, so it is not this red.
- No other edit to `tools/unattended/gate-guard.js`: not its question arm, not its deny text, and not
  `KIT_GATE_GUARD_VERSION` at line 122.
- No kit version bump. The unattended kit's shipped bytes move here, and the bump is measured over the
  finished tree by `TOOL-dRedressedBar-7`.
- No `python tools/run-gates/regen.py --write`, and no generated output other than the map S5
  regenerates. Every other declared output is `TOOL-dRedressedBar-7`'s, and this rename moves none
  of them.
- No run of `tools/unattended/gate-guard.test.sh`. The standing owner instruction of 2026-08-23 holds
  every `tools/unattended/` self-test suite off this build.

### Edges

- **hands-off** `TOOL-dRedressedBar-7` — the rename in `tools/unattended/gate-guard.js` moves the
  unattended kit's shipped bytes, and that unit bumps the kit once the build's tree is final.
- **hands-off** `TOOL-dRedressedBar-10` — report id 17, that S4's Readers missed
  `memory/map/generated/symbols.json` and §7 omitted `codebase-map coverage + freshness`, is closed
  in this spec by rev-3: S4 names the map, S5 regenerates and commits it in this unit's own pass, and
  §7 names the leg. That unit's AC14 observes those lines and the map this pass commits, and writes
  nothing into this spec. Unit 7's `regen.py --write` then finds the map fresh.

## 4. Design

TOOL-aOrientedCast-22 (`8ddc0a482`) added the question arm to the gate guard, and with it the
closure `const clean = (v) => String(v).replace(/[\u0000-\u001f\u007f-\u009f]/g, '').slice(0, ASK_QUOTE_MAX)`
inside `extractAskQuestions` (`tools/unattended/gate-guard.js:688-701`). That commit is not an
ancestor of `301a36664`, the commit TOOL-aSweptBar-6 measured 1087 at, and `git show
301a36664:tools/unattended/gate-guard.js` holds no `const clean`. The engine's P1 rule grades an
arrow assigned to a `const` as a function definition, and `clean` is not a declared verb. The brief
diffed `--offenders` between `301a36664` and `ebce889c` and found this the only arrival. The bar log's
own count, `verb offenders 1088 over pin 1087`, agrees with one arrival and no departure.

The rename is the whole change. Three tokens move, and the expression and both call shapes stay byte
for byte. `render` is the declared verb for "turn structure into text", and that is what the helper
does: it renders an arbitrary payload value as the bounded, control-free text the deny message
quotes. `lexicon.py --suggest renderAskQuote --as js.function`, run at spec time, answers
`OK — renderAskQuote leads with \`render\`, which the declaration carries, and satisfies camel for
cell \`js.function\``. For `clean` it answers that the name is a scoping question with no canon
cluster, so no rename target is derived for it and the verb is chosen here.

`renderAskQuote` collides with nothing. The file's other `render*` names are the module-level
`renderDeny` (line 669) and `renderAskDeny` (line 739), and the new name is a local inside a function
that declares no other `renderAskQuote`. The checklist's `a-new-local-collides-in-a-long-function`
class is answered by `grep -n 'renderAskQuote' tools/unattended/gate-guard.js` returning only the
three new lines.

### The symbol index

The map's JS layer lists every definition a rule in `JS_DEFINITION_RULES` matches
(`tools/codebase-map/map_lib.py:414-424`). A `const` bound to an arrow function is one of those
forms, so `memory/map/generated/symbols.json` lists `clean` at lines 5420-5424. `.githooks/pre-commit`
runs the codebase-map gate on any commit that stages a `.js` file (lines 233-246). That gate refuses
a stale `symbols.json` and names `gen_map.py --write` as the remedy. Lines 253-257 refuse
regenerated artifacts left unstaged. So the rename and the regenerated map land as one commit. This
build's specs 17 (S10) and 19 (§4, "Order, and unit 7") take the same step for the functions they
mint.

`gen_map.py --write` is the one generator of `memory/map/generated/`, the `[[generated]]` row at
`tools/codebase-map/kit.toml:148-156`. It renders `inventories.json`, `MAP.md`, `CARDS.md` and
`symbols.json` (`tools/codebase-map/gen_map.py:137-152`). The first three are built from the kit,
hook, gate-leg and dossier inventories, not from function names, so this rename moves only
`symbols.json`. At `3d1adca9`, `python tools/codebase-map/gen_map.py --check` exited 0 (PINNED,
2026-10-14). A second moved path would therefore be a sibling's staleness, which S5 returns to the
main loop rather than commits.

`TOOL-dRedressedBar-9` mints `check_outcome_states` in `tools/govkit/matrix.py`, and its pass also
commits a regenerated `symbols.json`. Both units sit at order 1. Their write sets meet on that file,
so by M6 clause 1 they are not disjoint and are built one after the other. `--dispatch` refuses a
path a still-open sibling pass in the same group already declared
(`tools/unattended/unattended.sh:13718-13729`). Whichever unit runs second regenerates over a tree
holding the first one's commit, so its map carries both names. Unit 7's `regen.py --write` then finds
the map fresh.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `renderAskQuote` | a local arrow function inside `extractAskQuestions` | `js.function`, camel, P1 verb `render` |

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- Raising `VERB_OFFENDER_PIN` to 1088: the build's non-goal, and the pin's ledger exists to record
  departures and frozen-record arrivals, not a live helper that one rename clears.
- `extractQuote`: `extract` pulls a declared shape out of a larger one, and this helper reshapes the
  value it is handed rather than pulling a part out of it.
- `checkQuote`: `check` returns a verdict, and this returns text.
- Inlining the expression at both call sites: it states the strip-and-cap rule twice in one function,
  the duplication the closure was written to avoid.
- Leaving `symbols.json` for unit 7's `regen.py --write`: the pre-commit hook refuses the rename's
  commit without it, so the pass could land only through `--no-verify`. Writing the map in a later
  commit of this pass leaves the product commit itself stale.
- Running `regen.py --write` here in place of `gen_map.py --write`: it renders every declared output,
  and the gotchas index among them is unit 7's S1. This rename moves the map alone.

## 5. Production-readiness checklist

- security — Unchanged by construction. The strip of control characters and the `ASK_QUOTE_MAX` cap
  are the deny message's guard against a payload that writes terminal escapes or floods the hook's
  output. AC2 compares the result byte for byte with the base copy's, so the guard is observed intact.
- perf / scale — N/A — a rename of a local closure; the same expression runs the same number of times.
- error / empty / loading states — Unchanged: a missing or blank question still yields
  `(no question text)`, and a non-string label is still dropped. AC2's payload carries each case.
- observability — N/A — the hook's output is the same bytes; nothing new is logged.
- risks — A call site left spelling `clean` would throw a `ReferenceError` on the first
  `AskUserQuestion` payload the hook reads, and the hook would then deny on a crash rather than on
  its rule. AC1 refuses that state, and AC2 exercises both call sites. A commit without the
  regenerated map is refused by the pre-commit hook, and AC4 reads the map the commit carries.
- testing — AC1 to AC4 are probes of the changed file, the lexicon engine and the committed map. The
  hook's own suite is a `tools/unattended/` suite the standing instruction holds off this build.
- migration — N/A — no data, conf or receipt shape moves. The generated map is re-rendered from the
  tree, not migrated.
- user docs — N/A — no user-facing surface, flag or message changes.

## 6. Acceptance criteria

- **AC1** — When `grep -nw 'clean' tools/unattended/gate-guard.js` runs, it prints nothing, and
  `grep -n 'renderAskQuote' tools/unattended/gate-guard.js` prints exactly three lines: the `const`
  declaration and the two calls, all inside `extractAskQuestions`.
  Red when: one call still spells `clean`, which is then undefined at that call.
- **AC2** — When a `node` program requires `tools/unattended/gate-guard.js` and prints
  `JSON.stringify(extractAskQuestions(p))` for a payload `p` holding a 400-character question carrying
  a BEL and a C1 byte, a label carrying a NUL, a non-string label, a blank question and a null
  question, and then for `{}`, its output equals byte for byte the output of the same program run
  against `git show ebce889c:tools/unattended/gate-guard.js` written to a scratch file. The first
  question reads 300 characters, and the empty input reads `[{"question":"(no question text)","labels":[]}]`.
  Red when: the rename alters the expression, so a control byte survives, the cut moves, or a call
  throws.
  fixture: the base copy is written under the run's scratchpad. `extractAskQuestions` reaches no
  `require` of a sibling file, so the copy loads alone; measured at spec time over `ebce889c`.
- **AC3** — When `python tools/lexicon/lexicon.py --suggest renderAskQuote --as js.function` runs, it
  prints `OK — renderAskQuote leads with`. When `python tools/lexicon/lexicon.py --offenders` runs,
  no line names `tools/unattended/gate-guard.js`. When `python tools/lexicon/lexicon.py --measure`
  runs, the P1 verb offender count equals the `VERB_OFFENDER_PIN` value in `.lexicon.conf`.
  Red when: the helper keeps a name whose leading token is not a declared verb, and the count reads
  one over the pin.
  figure: the pin is PINNED at 1087 by `.lexicon.conf:268`; the count is DERIVED by `--measure` at
  observation.
  cost: `--offenders` and `--measure` each read the whole tree, tens of seconds on node d.
- **AC4** — When a `python` one-liner loads `memory/map/generated/symbols.json` at the unit's tip, it
  finds one entry with id `renderAskQuote` and file `tools/unattended/gate-guard.js`, and no entry with
  id `clean` and that file. Over `git show 3d1adca9:memory/map/generated/symbols.json` the same
  one-liner finds `clean` and no `renderAskQuote`. `python tools/codebase-map/gen_map.py --check`
  exits 0 at the tip. `git show --name-only --format= <p2>`, over the pass's product commit, lists
  `tools/unattended/gate-guard.js` and `memory/map/generated/symbols.json`, and no other path under
  `memory/map/`.
  Red when: the rename is committed without the map, so the map still lists `clean` for the file
  and `--check` names `symbols.json` stale, as the pre-commit hook found on the first attempt.

## 7. Gates

`lexicon naming predicates` · `lexicon wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`codebase-map coverage + freshness` reads the map S5 regenerates. `recall floor` and
`recall floor arms` are owed by the guard join: `memory/map/generated/symbols.json` sits under the
`memory/` guard both carry (`tools/gate-legs.json:868-890`).

`unattended gate-guard selftest`, the self-test tier's row for `tools/unattended/gate-guard.test.sh`,
grades the question arm. It is held off this build by the standing owner instruction, so the close
reads it only if the owner asks for it.

No arm is added or moved. The two lexicon legs already compare the offender count with the pin, and
they are the legs this unit turns green. The codebase-map leg already compares the map with a live
render.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the build brief; the arrival re-read against `301a36664`
  and the new name checked with `lexicon.py --suggest`.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to TOOL-dRedressedBar-10, the batch the round-1
  spec audit's minors were promoted into, for report id 17. No scope, design or criterion moves.
- rev-3 · 2026-10-14 · S4 · S5 · §3 · §4 · §5 · AC4 · §7 · the builder's divergence
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md`): the pre-commit hook refused the
  rename's commit on a stale `symbols.json`. S5 regenerates the map with `gen_map.py --write` alone
  and commits it with the rename. S4's Readers and §4 Files touched name the map, and §4 gains "The
  symbol index", with the M6 sequencing against unit 9. AC4 observes the committed map. §7 names
  `codebase-map coverage + freshness` and the two recall legs the guard join owes. The Edges line to
  `TOOL-dRedressedBar-10` no longer defers the map to unit 7's regen: report id 17 is closed
  here, and that unit only observes it.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "strip control characters from a quoted value and cap its length
for display"` returned name-stem neighbours only: `read_conf_value`, `build_counted_values`,
`read_clause_values` and `run_constant_control`, none of which strips or caps a quoted value, plus the
unattended conf's affordance seam, which names TOOL-aOrientedCast-22 as its decision. No existing seam
fits. A fixed-string grep of every JavaScript file under `tools/` for the control-character class
finds it only in `tools/unattended/gate-guard.js:689`. So the helper stays local and is renamed in place; no shared helper is
extracted for a single instance. The lexicon engine's own `--suggest` is the seam that judged the
name. The brief and the code agree: the arrival is the only one, and the pin's commit lacks it.

S5 builds nothing. Its seam is the map's declared generator, `gen_map.py --write`, from the
`[[generated]]` row at `tools/codebase-map/kit.toml:148-156`, the remedy the pre-commit hook names.
This build's specs 17 and 19 already take it for their own mints.

Recall terms used: `python tools/memory-recall/query.py "why do suite arms go red after a bar-less
landing moves the code under them, and how were they re-armed" --terms "bar-less landing stale
fixture re-armed probe marker WHOLE_RUN GATE_SELFTESTS cleared default-gained verb offender pin"`
