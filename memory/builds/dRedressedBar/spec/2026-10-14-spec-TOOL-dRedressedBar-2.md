# TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb

**Status:** SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |

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
- **S4** — The retired name `clean` has no reader outside `extractAskQuestions`.
  **Readers:**
  by name: `tools/unattended/gate-guard.js` lines 694 and 696, both inside the function that declares
  it, and no other file in this tree. The `clean` in `tools/unattended/check-unattended.sh:1861` is
  an unrelated awk function and is not this helper.
  by value: NO VALUE READERS — the helper is a local closure that `module.exports` at line 796 does
  not export, so nothing outside the function compares, counts or derives from it.
  Observed by AC1.

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
- No run of `tools/unattended/gate-guard.test.sh`. The standing owner instruction of 2026-08-23 holds
  every `tools/unattended/` self-test suite off this build.

### Edges

- **hands-off** `TOOL-dRedressedBar-7` — the rename in `tools/unattended/gate-guard.js` moves the
  unattended kit's shipped bytes, and that unit bumps the kit once the build's tree is final.

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

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `renderAskQuote` | a local arrow function inside `extractAskQuestions` | `js.function`, camel, P1 verb `render` |

### Files touched (estimate)

- `tools/unattended/gate-guard.js`

### Alternatives rejected

- Raising `VERB_OFFENDER_PIN` to 1088: the build's non-goal, and the pin's ledger exists to record
  departures and frozen-record arrivals, not a live helper that one rename clears.
- `extractQuote`: `extract` pulls a declared shape out of a larger one, and this helper reshapes the
  value it is handed rather than pulling a part out of it.
- `checkQuote`: `check` returns a verdict, and this returns text.
- Inlining the expression at both call sites: it states the strip-and-cap rule twice in one function,
  the duplication the closure was written to avoid.

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
  its rule. AC1 refuses that state, and AC2 exercises both call sites.
- testing — AC1 to AC3 are probes of the changed file and of the lexicon engine. The hook's own suite
  is a `tools/unattended/` suite the standing instruction holds off this build.
- migration — N/A — no data, conf or receipt shape moves.
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

## 7. Gates

`lexicon naming predicates` · `lexicon wiring`

`unattended gate-guard selftest`, the self-test tier's row for `tools/unattended/gate-guard.test.sh`,
grades the question arm. It is held off this build by the standing owner instruction, so the close
reads it only if the owner asks for it.

No arm is added or moved. The two lexicon legs already compare the offender count with the pin, and
they are the legs this unit turns green.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the build brief; the arrival re-read against `301a36664`
  and the new name checked with `lexicon.py --suggest`.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "strip control characters from a quoted value and cap its length
for display"` returned name-stem neighbours only: `read_conf_value`, `build_counted_values`,
`read_clause_values` and `run_constant_control`, none of which strips or caps a quoted value, plus the
unattended conf's affordance seam, which names TOOL-aOrientedCast-22 as its decision. No existing seam
fits. A fixed-string grep of every JavaScript file under `tools/` for the control-character class
finds it only in `tools/unattended/gate-guard.js:689`. So the helper stays local and is renamed in place; no shared helper is
extracted for a single instance. The lexicon engine's own `--suggest` is the seam that judged the
name. The brief and the code agree: the arrival is the only one, and the pin's commit lacks it.

Recall terms used: `python tools/memory-recall/query.py "why do suite arms go red after a bar-less
landing moves the code under them, and how were they re-armed" --terms "bar-less landing stale
fixture re-armed probe marker WHOLE_RUN GATE_SELFTESTS cleared default-gained verb offender pin"`
