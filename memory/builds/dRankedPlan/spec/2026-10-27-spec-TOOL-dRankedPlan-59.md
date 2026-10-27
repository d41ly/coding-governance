# TOOL-dRankedPlan-59 — a wrapper call reads its script word past the interpreter's options, as a bare call does

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 10 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-59-deviation-591.md](../build/2026-10-27-build-TOOL-dRankedPlan-59-deviation-591.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-55 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-60 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 30 at HIGH**, item **H6**. `TOOL-dRankedPlan-50` S1 accepts the `ratify.py` word of a wrapper
call only when it follows an interpreter word directly, or when it is the first argument that is
neither a dash word nor a duration. In `timeout 60 "$py" -B "$d/ratify.py" "$slug"` the script word
follows `-B`, and the first qualifying argument is `"$py"`, so neither arm matches and the call passes
the deny-by-default ban. `TOOL-dRankedPlan-32` S2 skips `-` words after the interpreter of a bare call,
and the wrapper rule dropped that skip. The tree writes `"$PY" -B script.py` often. This unit restates
the wrapper rule's first arm as unit 32 S2's own reading. It repairs `TOOL-dRankedPlan-50`, so it sits
one order above it.

## 2. Scope (IN)

- **S1** — The first arm restated. A wrapper call of `TOOL-dRankedPlan-50` S1 invokes `ratify.py` when,
  after an argument word of `TOOL-dRankedPlan-32` S2's interpreter class, the first later word not
  beginning `-` ends in `ratify.py`. That is unit 32 S2's reading of a bare call, applied from the
  interpreter word inside the wrapper call. This supersedes unit 50 S1's "follows an interpreter word of
  unit 32 S2's class directly". Unit 50 S1's second arm, the first argument word that neither begins
  `-` nor is a `timeout` duration, is unchanged. Observed by AC1 and AC2.
- **S2** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-timeout-opt` plants a `.githooks/pre-commit` holding `timeout 60 "$py" -B
    "$d/ratify.py" "$slug"`. It is refused.
  - `caller-shell-func-wrapper-opt` plants `TOOL-dRankedPlan-50`'s `with_hook_index` definition and
    then `with_hook_index "$py" -B "$d/ratify.py" "$slug"`. It is refused.
  - `caller-shell-timeout-opt-exit` plants `caller-shell-timeout-opt` with `--exit` after `"$slug"`.
    It is admitted.

## 3. Non-goals (OUT)

- An interpreter option that takes an argument, such as `-W ignore` or `-X utf8`. Unit 32 S2 reads the
  argument as the script word for a bare call, and S1 inherits that ceiling unchanged, recorded in §4.
- The direct-script arm `timeout -k 5s 60 "$d/ratify.py"`: `TOOL-dRankedPlan-62`'s item for finding 9,
  which plants it.
- A bound script word behind a wrapper: `TOOL-dRankedPlan-58`, whose test S1's comparison calls once
  it lands.

### Edges

- **consumes-from** `TOOL-dRankedPlan-50` — S1's wrapper call and `SHELL_WRAPPER_COMMANDS`, whose first arm S1 restates; without them there is no wrapper call to read
- **hands-off** `TOOL-dRankedPlan-62` — S1's restated arm, which that unit's item for finding 17 matches in unit 50's §4 table
- **hands-off** `TOOL-dRankedPlan-67` — §4 Evidence, which that unit's item for finding 20 re-cites; carry S28 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-50` S1 (its lines 31-38) reads "either follows an interpreter word of unit 32 S2's
  class directly, or is the first argument word that neither begins `-` nor is a `timeout` duration".
- `TOOL-dRankedPlan-32` S2 (its lines 49-57) reads "its first later word not beginning `-` ends in
  `ratify.py`".
- `tools/policy/adopt-policy.sh:87` reads `"$PY" -B "$HERE/check_policy.py" --repo "$TARGET"`. `git grep
  -nE '"\$\{?(py|PY|PYBIN|PYTHON)\}?" -B ' -- '*.sh' '.githooks/*'`, run 2026-10-27 at base 0689e7fa,
  printed 55 lines. The count is PINNED.
- `scan_shell_tokens('timeout 60 "$py" -B "$d/ratify.py" "$slug"\n')`, run 2026-10-27 at base 0689e7fa
  from `tools/lexicon/lexicon.py`, printed the six words in order, `-B` between `"$py"` and the script
  word. The output is PINNED.

### The reading after this unit

| Command | Arm | Answer |
|---|---|---|
| `timeout 60 "$py" "$d/ratify.py" "$slug"` | first | caller |
| `timeout 60 "$py" -B "$d/ratify.py" "$slug"` | first, past `-B` | caller |
| `with_hook_index "$py" -B "$d/ratify.py" "$slug" --exit` | first | not a caller |
| `timeout 60 "$py" -W ignore "$d/ratify.py"` | first, reads `ignore` | unread, unit 32 S2's ceiling |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-timeout-opt`, `caller-shell-func-wrapper-opt`, `caller-shell-timeout-opt-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 10, one above `TOOL-dRankedPlan-50`. `TOOL-dRankedPlan-3` and
`TOOL-dRankedPlan-19` share order 10, and whether the step runs in parallel is BUILD-METHOD M6's
decision over the three write lists.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Skip a fixed list of Python options.** The list grows with every flag, and unit 32 S2 already
  decided the reading for a bare call, so a second reading for the same words is two facts.

## 5. Production-readiness checklist

- security — narrows: a wrapped call with an interpreter option is read by the deny-by-default ban.
- perf / scale — unchanged: one walk over the wrapper call's words.
- error / empty / loading states — a wrapper call whose interpreter is followed only by dash words is
  not an invocation.
- observability — the refusal names the file and the wrapper call's line.
- risks — none beyond unit 32 S2's ceiling for an option that takes an argument.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-timeout-opt` runs, the check exits 1
  naming `.githooks/pre-commit` and the `timeout` line.
  Red when: a `-B` between the interpreter and the script word lets a wrapped call pass.
- **AC2** — When the plant `caller-shell-func-wrapper-opt` runs, the check exits 1 naming the
  `with_hook_index "$py"` line.
  Red when: a same-file wrapper function's call with an interpreter option passes.
- **AC3** — When the plant `caller-shell-timeout-opt-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a wrapped `--exit` call with an interpreter option is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `*-opt*` plants, staged by a wrapper rule that takes the script word only directly after the interpreter word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 30 (HIGH,
  item H6), repairing `TOOL-dRankedPlan-50`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-50` S1's wrapper call, whose first arm now reuses
`TOOL-dRankedPlan-32` S2's script-word reading instead of a second one. `python
tools/codebase-map/reuse_lookup.py "resolve a shell variable bound to a script path where a command
invokes it"`, run 2026-10-27, ranked name stems only (`resolve`, `resolve_kit_dir`, `resolve_caps`),
none of which reads a wrapper's arguments, so no existing seam fits beyond the two units.
`tools/runlog/extract.py:479` `_derive_program` is the sibling wrapper reader `TOOL-dRankedPlan-50` §4
already cites. The recall query returned units 47 to 52 and dWitnessedBar's resolver scouts, and they
agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
