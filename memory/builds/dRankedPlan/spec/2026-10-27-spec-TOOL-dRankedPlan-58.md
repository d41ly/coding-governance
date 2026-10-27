# TOOL-dRankedPlan-58 — every `ratify.py` word comparison of the shell reader goes through one resolving test

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 22 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-58-deviation-581.md](../build/2026-10-27-build-TOOL-dRankedPlan-58-deviation-581.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-59 TOOL-dRankedPlan-55 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 29 at HIGH**, item **H5**, whose `timeout` instance is finding 8 at MEDIUM, item M6.
`TOOL-dRankedPlan-49` S2 resolves a `$name` word only "wherever unit 32 S2 compares a word with
`ratify.py`". `TOOL-dRankedPlan-50` S1's wrapper-call test and `TOOL-dRankedPlan-52` S13's textual line
rule each compare a word with `ratify.py` on their own, and S2 names neither. A builder reading S2
literally leaves them unresolved, so `with_hook_index "$py" "$r" "$slug"` with `r="$d/ratify.py"`
passes the deny-by-default ban. That is `.githooks/pre-commit:212`'s own shape. This unit makes one
test the only place the shell reader asks whether a word names `ratify.py`, so every comparison site,
present or later, resolves. It repairs `TOOL-dRankedPlan-49`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The one test. `resolve_ratify_word(word, bindings)` in `tools/loop/ratify.py` answers
  whether a shell word names `ratify.py`: the word with its quote characters stripped ends in
  `ratify.py`, or it is `$name` or `${name}` and `TOOL-dRankedPlan-49` S2 resolves it through
  `bindings` to a value that names `ratify.py`. Every rule of `read_shell_callers` that tests a word
  against `ratify.py` calls it. Today those are `TOOL-dRankedPlan-32` S2's two invocation forms as
  `TOOL-dRankedPlan-41` S3 restates them, `TOOL-dRankedPlan-50` S1's wrapper-call test, and
  `TOOL-dRankedPlan-52` S13's textual line rule, and a site a later unit adds calls it too, such as
  `TOOL-dRankedPlan-59`'s restated wrapper arm. This supersedes unit 49 S2's first sentence, "Wherever
  unit 32 S2 compares a word with `ratify.py`", and its "Both invocation forms of unit 32 S2 read the
  resolved word". Observed by AC1.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-shell-bound-wrapper` plants a `.githooks/pre-commit` defining `with_hook_index() { "$@";
    }`, then `r="$d/ratify.py"` and `with_hook_index "$py" "$r" "$slug"`. It is refused.
  - `caller-shell-bound-wrapper-exit` plants the same with `--exit` after `"$slug"`. It is admitted.

## 3. Non-goals (OUT)

- The `timeout` instance of the same defect, `r="$d/ratify.py"; timeout 60 "$py" "$r" "$slug"`
  (finding 8): `TOOL-dRankedPlan-62`'s item, which plants it over S1.
- What a binding's value is: `TOOL-dRankedPlan-49` S1 and `TOOL-dRankedPlan-57` S1.
- The Python and JavaScript readers, which compare `str` constants and tokens, not shell words.

### Edges

- **consumes-from** `TOOL-dRankedPlan-49` — S1's bindings and S2's resolution, which S1 makes the one test; without them there is nothing to resolve
- **consumes-from** `TOOL-dRankedPlan-50` — S1's wrapper-call test, a comparison site S1 routes through the test
- **hands-off** `TOOL-dRankedPlan-52` — `resolve_ratify_word`, which that unit's S13 line rule calls for its `ratify.py` comparison
- **hands-off** `TOOL-dRankedPlan-62` — `resolve_ratify_word`, over which that unit's item for finding 8 plants the bound path behind `timeout`
- **hands-off** `TOOL-dRankedPlan-67` — `resolve_ratify_word`, S1 and §4 Evidence, over which that unit's items for findings 11 and 20 plant and re-cite; carry S13 and S28 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-49` S2 (its lines 35-40) limits the resolution to unit 32 S2's comparisons.
- `TOOL-dRankedPlan-50` S1 (its lines 31-38) tests whether "one of its argument words ends in
  `ratify.py`", a third comparison site.
- `TOOL-dRankedPlan-52` S13 (its lines 121-129) adds "a line holding a word ending in `ratify.py`", a
  fourth.
- `.githooks/pre-commit:11` defines `with_hook_index`, whose body passes `"$@"`, and :212 reads
  `elif ! with_hook_index "$py" "$g" --staged; then`.

### The reading after this unit

| Hook lines | Site | Answer |
|---|---|---|
| `r="$d/ratify.py"`, then `"$py" "$r" "$slug"` | unit 32 S2 | caller |
| `r="$d/ratify.py"`, then `with_hook_index "$py" "$r" "$slug"` | unit 50 S1 | caller |
| `r="$d/ratify.py"`, then `timeout 60 "$py" "$r" "$slug"` | unit 50 S1 | caller, planted by unit 62 |
| an expanded Python-fed body line `"$r" "$slug"` with the same `r` | unit 52 S13 | caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_ratify_word` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest resolve_ratify_word --as py.function` answered OK |
| `caller-shell-bound-wrapper`, `caller-shell-bound-wrapper-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 22. Units 52, 55, 57, 58 and 60 share order 22 and all write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside that step, this unit
before unit 52, which consumes from it. The pass re-renders `memory/map/generated/symbols.json` with
`gen_map.py --write` for the minted function, as `TOOL-dRankedPlan-61` S1 states.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `memory/map/generated/symbols.json`: the render of S1's function

### Alternatives rejected

- **List the sites in unit 49 S2 instead of a test.** A list is the defect this finding names: the
  next unit that adds a comparison is again outside it.

## 5. Production-readiness checklist

- security — narrows: a bound path is resolved at every site the shell ban compares.
- perf / scale — one dictionary lookup per `$name` word compared.
- error / empty / loading states — an unbound `$name` resolves to nothing, as `TOOL-dRankedPlan-49`
  §5 states.
- observability — the refusal names the file and the invoking command's line.
- risks — none beyond `TOOL-dRankedPlan-49`'s fail-closed reuse of a name.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-bound-wrapper` runs, the check exits 1
  naming the `with_hook_index "$py"` line.
  Red when: the wrapper-call test compares `"$r"` unresolved and passes it.
- **AC2** — When the plant `caller-shell-bound-wrapper-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a bound wrapped `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `caller-shell-bound-wrapper` and its `--exit` twin, staged by a wrapper-call test that compares the raw word with `ratify.py` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 29 (HIGH,
  item H5; finding 8 is its medium face), repairing `TOOL-dRankedPlan-49`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-49` S2's resolution, which becomes the body of S1's test, and
each comparison site of `read_shell_callers` calls it. `python tools/codebase-map/reuse_lookup.py
"resolve a shell variable bound to a script path where a command invokes it"`, run 2026-10-27, ranked
name stems only (`resolve`, `resolve_kit_dir`, `resolve_caps`), none of which reads a shell word, so no
existing seam fits beyond unit 49's rule. The recall query returned units 47 to 52 and dWitnessedBar's
resolver scouts, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
