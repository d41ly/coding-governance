# TOOL-dSafePassage-100 — arm 37's count runs the resolved launcher with no `python3` default, and skips naming what is not covered when none resolved

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f519c1934 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-82

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-prompt-TOOL-dSafePassage-100-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-100-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-100-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-100-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-100-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-100-spec-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md) | research | TOOL-dSafePassage-99 |
| [2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-99 |

<!-- /gen:spec-records -->

## 1. Goal

The lander suite's arm 37 runs its derived count under `"${_py_arms:-python3}"`
(`tools/push-main.test.sh:1409`). That is the parameter-default shape the resolver suite's launcher
ban refuses (`tools/lib/resolve-python.test.sh:774-791`), so the bar leg
`python resolver (behaviour + inline parity + idiom ban)` reds at HEAD. This unit makes `measure37`
call `"$_py_arms"` with no default, and gates the arm on a resolved launcher, so a host where none
resolves prints a `skip — 37` line naming what is not covered instead of running an unresolved name.

## 2. Scope (IN)

- **S1** — `measure37` (`tools/push-main.test.sh:1408-1419`) invokes `"$_py_arms" -c '` at line
  1409, with no parameter default. Observed by AC1.
- **S2** — the derived-count block's guard (`tools/push-main.test.sh:1423`) also requires a
  resolved launcher, spelled `[ -n "$_py_arms" ]`, beside its `_mt_rc` and `check-arms.py` tests.
  Both `measure37` call sites, at lines 1424 and 1436, sit inside that block, so neither runs with
  an empty launcher. The TOOL-dSafePassage-46 S2 comment above the guard (lines 1420-1421) gains one
  sentence saying the arm runs only under the launcher resolved at line 1093. Observed by AC2 and
  AC4.
- **S3** — the block's `else` branch (`tools/push-main.test.sh:1445`) names the launcher beside the
  kit, in the spelling of the sibling guard's skip at line 1453:
  `skip — 37 no memory-tree kit (check-arms.py) or python launcher beside this lander, so the derived-count arm is NOT covered`.
  The words `derived-count arm` stay, because TOOL-dSafePassage-58's AC2 pattern reads them.
  Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- Any change to the launcher ban `bare_scan` or to its plants in `tools/lib/resolve-python.test.sh`.
- Any change to the resolver block or to the `_py_arms` assignment at `tools/push-main.test.sh:1093`.
- Any other launcher site in any file. At `f519c1934` the parameter-default shape `:-python3}` has no
  other hit in a tracked `*.sh` file (§4, "The measured state").
- Arm 37's assertions, its `PREPARE_REFUSALS` rows, and the refusal loop from line 1447 on, whose
  own guard at line 1452 already names `_py_arms`.
- Any edit to a CLOSED spec, TOOL-dSafePassage-42, -46, -58 or -82 included.
- TOOL-dSafePassage-99's write set, `tools/govkit/selftest.py`. The two units share no path.

### Edges

none

## 4. Design

Every cited line holds at `f519c1934`, HEAD when this spec was written, read on 2026-11-01 on node
a. The edit is three lines of the lander suite plus one comment sentence.

### The measured state

- `tools/push-main.test.sh:1093` resolves `_py_arms` once with `resolve_python`, and its comment at
  line 1092 says it is empty when no launcher runs.
- Line 1409 reads `"${_py_arms:-python3}" -c '`. An empty `_py_arms` therefore runs `python3`
  unresolved, which on a host with only the MS-Store stub exits 9009.
- Line 1423 reads `if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then`, and line
  1445 is its `else` branch's skip echo, ending `so the derived-count arm did not run`.
- The sibling guard at line 1452 reads
  `if [ -z "$_mt_gk" ] || [ -z "$_rg_k" ] || [ -z "$_ml_lex" ] || [ -z "$_py_arms" ]; then`, and its
  skip at line 1453 names `python launcher` and ends `so this refusal is NOT covered`.
- `git grep -nF -e ':-python3}' -- '*.sh'` printed exactly one line, `tools/push-main.test.sh:1409`.
- The ban's own predicate, `bare_scan` cut from `tools/lib/resolve-python.test.sh:780-791` and run
  over the lander suite in a scratch shell, printed the same one line. Run over a scratch copy
  carrying S1 to S3, it printed nothing.

### The change

| Line | At `f519c1934` | After |
|---|---|---|
| 1409 | `"${_py_arms:-python3}" -c '` | `"$_py_arms" -c '` |
| 1420-1421 | the TOOL-dSafePassage-46 S2 comment | the same, plus one sentence: the arm runs only under the launcher line 1093 resolved, so `measure37` names no default |
| 1423 | `if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then` | `if [ -n "$_mt_rc" ] && [ -n "$_py_arms" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then` |
| 1445 | `... beside this lander, so the derived-count arm did not run"` | `... (check-arms.py) or python launcher beside this lander, so the derived-count arm is NOT covered"` |

The comment sentence must not spell the `:-python3}` shape, because AC1's grep reads comment lines
too, though the ban skips them.

### Inventory

No local, function, constant, type, file, check label, flag, conf key, gate leg or receipt field is
minted. The skip line is new text, not an identifier. The naming lexicon grades nothing new.

### Migration

None.

### Rollout

Live at landing, at order 16. On a host where a launcher resolves, arm 37 runs as before and prints
its two `ok — 37` lines. On a host where none resolves, it prints one `skip — 37` line.

### Files touched (estimate)

- `tools/push-main.test.sh`
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-100-ledger.md` — the
  acceptance ledger.

### Alternatives rejected

- **A `gov:literal-python` marker on line 1409.** The ban's header describes every marked line as a
  launcher name printed or rendered rather than executed (`tools/lib/resolve-python.test.sh:766-769`).
  This line executes it, so a marker would hide the defect the ban exists to catch.
- **A resolve inside `measure37`.** It would be a second resolver beside line 1093, which already
  serves arms 33, 34, 37 and 40.
- **`"${_py_arms:?}"`.** It passes the ban but aborts the whole suite on a host with no launcher,
  where every sibling arm skips.
- **Leaving the guard and letting `measure37` fail into its `|| echo 0` fallback.** An empty launcher
  would then print two `FAIL — 37` lines that name a count, not a missing launcher. AC4's red case
  measures exactly that.

## 5. Production-readiness checklist

- security: N/A — no write path, spawn site or surface is added. The edit narrows what the suite
  executes to the resolved launcher.
- perf / scale: N/A — two shell tests on one branch.
- error / empty / loading states: the empty-launcher state is the point of S2 and S3, observed by
  AC4.
- observability: the `skip — 37` line names both preconditions, so a skipped run says why.
- risks: the skip is not coverage. On a host with no launcher, arm 37 checks nothing and says so,
  as arms 34, 36, 39 and 40 already do. `measure37`'s `|| echo 0` fallback stays live for a launcher
  that resolves and then fails, so the guard does not make it dead.
- testing: AC1 to AC4, and one `New arm:` line (§7).
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` describes the lander suite's arms.

## 6. Acceptance criteria

- **AC1** — When `git grep -nF -e ':-python3}' -- '*.sh'` runs from the repository root, it prints
  nothing and exits 1. The resolver suite's `bare_scan`, cut from that suite and run over the lander
  suite tools/push-main.test.sh in a scratch shell, prints nothing either.
  Red when: the default is given back at line 1409. At `f519c1934` the grep prints one line, line
  1409 of the lander suite, reading `"${_py_arms:-python3}" -c '`, measured on 2026-11-01.
- **AC2** — When `git grep -nF -e 'if [ -n "$_mt_rc" ] && [ -n "$_py_arms" ]' -- '*.sh'` runs from
  the repository root, it prints exactly one line, the derived-count block's guard in the lander
  suite.
  Red when: the guard does not name `_py_arms`. At `f519c1934` the grep prints nothing and exits 1,
  measured on 2026-11-01.
- **AC3** — When
  `git grep -nF -e 'or python launcher beside this lander, so the derived-count arm is NOT covered' -- '*.sh'`
  runs from the repository root, it prints exactly one line, the skip echo in the `else` branch of
  AC2's guard.
  Red when: the skip keeps its `did not run` ending or names no launcher. At `f519c1934` the grep
  prints nothing, measured on 2026-11-01.
- **AC4** — When arm 37's lines, from the `measure37()` definition to the `fi` that closes the
  derived-count block, are cut from the lander suite and run in a scratch bash twice, first with
  `_py_arms=""` and then with `_py_arms` set to the output of `resolve_python`, the first run prints
  only
  `skip — 37 no memory-tree kit (check-arms.py) or python launcher beside this lander, so the derived-count arm is NOT covered`,
  and the second prints the two `ok — 37` lines, the first naming `refuses 6 way(s)`.
  Red when: the guard does not name `_py_arms`. On a scratch copy whose line 1409 reads
  `"$_py_arms" -c '` and whose guard is as at `f519c1934`, the first run printed two `FAIL — 37`
  lines, `cmd_prepare refuses 0 way(s)` and `0, not 0`, measured on 2026-11-01.
  fixture: the scratch bash sets `HERE` to the tools directory, `_mt_rc` by the suite's own scan at
  line 1030, `PREPARE_REFUSALS` from the suite's own array, a scratch `tmp`, and `ok` and `bad` as
  the suite spells them at lines 185-186. The tree holds every input today.
  figure: 6 is DERIVED by `measure37` from the lander at observation time, and must equal the row
  count of `PREPARE_REFUSALS`.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `recall floor arms` · `recall floor` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC4 · arm 37's derived-count block in a suite copy whose `_py_arms=` line assigns the empty string prints its `skip — 37 ... NOT covered` line and no `FAIL — 37` line; staged red by a copy whose guard lacks `[ -n "$_py_arms" ]`, which prints two `FAIL — 37` lines · none

The gate that reds today is the existing launcher ban, `bare_scan` in the resolver suite, and this
unit leaves that arm as it is. So it owes no `New arm:` line: its red is already observed at
`390033278` by the close's run of TOOL-dSafePassage-87 AC11, which named line 1409, and the close
observes it green once this unit lands. Arm 37's guard does move, which changes what the arm runs
with an empty launcher, and only a run shows that. That is the one `New arm:` line. TOOL-dSafePassage-46
and -58 declared one each for their own changes to the same guard and skip.

The lander suite's path trips only the `{prefix}/` guard, which twelve legs carry, so the
spec-token join drops it as broad (`BROAD_LEG_FLOOR = 5`, `tools/check-spec-tokens.py:368`), read on
2026-11-01. The acceptance ledger's `memory/` path trips `recall floor` and `recall floor arms`.
Both were printed by `python tools/check-spec-tokens.py --legs-for` over the full write set on
2026-11-01. The leg line names the resolver leg that reds, the lander suite's own leg, the leg that
runs it at three prefixes, the two recall legs the ledger trips, and the two that grade this spec
and its ledger.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-100-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-100-spec-brief.md`.
  The brief's finding, item 1 (high): the close's observation of TOOL-dSafePassage-87 AC11 ran the
  resolver suite in a clean clone at `390033278`, and its launcher ban exited 1 naming
  `tools/push-main.test.sh:1409:  "${_py_arms:-python3}" -c '`, so the bar leg at
  `tools/gate-legs.json:320` reds. Adopted under UNATTENDED-PROTOCOL §11, a measured red. Carried as
  S1 to S3, observed by AC1 to AC4. One correction to the brief's history, read with `git log -S`:
  the shape came in as `"${_py37:-python3}"` with TOOL-dSafePassage-42 at `ff6a6ff79`, and
  TOOL-dSafePassage-82 at `5fe2dab8e` renamed the variable to `_py_arms`, writing line 1409 as it
  reads today. The ban's parameter-default shape predates both, at `8c53af8f1`. Why the bar did not
  red at either landing is UNVERIFIED.
- rev-2 · 2026-11-01 · §4 · §7 · folded the round-1 spec audit
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md`
  from the brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md`.
  LOW 3 (id 2): §4's Files touched now lists the acceptance ledger, and §7's leg line names
  `recall floor` and `recall floor arms`, which the ledger's `memory/` path trips. Re-checked with
  `python tools/check-spec-tokens.py --legs-for` over both paths on 2026-11-01, at `6414e1dc6`.

## 10. Reuse audit

The seam is the lander suite's own launcher resolution and its sibling guards: `_py_arms` resolved
once at `tools/push-main.test.sh:1093`, and the guards that already test it, `:1216`, `:1253`,
`:1452` and `:1575`. S2 adds the same test to the one arm that reads `_py_arms` without it, and S3
copies the skip spelling of `:1453`. No helper is added.
`python tools/codebase-map/reuse_lookup.py "a suite arm skips with a NOT covered line when no python launcher resolved"`
ranked `resolve_python` as a SEAM whose callers include the lander suite, which is the line 1093
call this unit reuses. The recall probe ranked TOOL-cMendedVintage-11, "the census arm resolves its
launcher instead of trusting the name", and TOOL-aGradedDialect-12, whose fix was no fallback and a
named outcome when no launcher resolves. Both are the shape of S1 to S3. No code seam outside the
lander suite is touched: `tools/govkit/`, `tools/lib/` and `tools/push-main.sh` are not edited.

Recall terms used: `python tools/memory-recall/query.py "how does a suite arm guard on the resolved launcher instead of a parameter default python3" --terms "_py_arms resolve_python parameter default launcher ban bare_scan skip NOT covered arm 37 measure37"`
