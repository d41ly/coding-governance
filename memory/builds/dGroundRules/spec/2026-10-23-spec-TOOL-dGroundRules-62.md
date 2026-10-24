# TOOL-dGroundRules-62 — an unset `budgets.<cap>` reads as no file value: the derived-default refusal is a type the caps module catches, and only that refusal

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-62-deviation-50.md](../build/2026-10-23-build-TOOL-dGroundRules-62-deviation-50.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-61-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-task.md) | research | TOOL-dGroundRules-61 TOOL-dGroundRules-63 |
| [2026-10-23-prompt-TOOL-dGroundRules-62-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-62-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md) | research | TOOL-dGroundRules-55 TOOL-dGroundRules-61 TOOL-dGroundRules-64 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
confirmed **id 8 at HIGH**, item **H4**: units 9 and 21 give two answers to one question.
`TOOL-dGroundRules-9` S2 reads an unset `budgets.<cap>` as "no file value", expecting `resolve` to
return source `default` (its edge from `TOOL-dGroundRules-3`). `TOOL-dGroundRules-21` S12 makes
`read_default_value` refuse every `{ derived = ... }` default, and `budgets.*` can only have a
derived default, since v2's Default cell for it is prose. `TOOL-dGroundRules-21` S31 then turns that
refusal into `mode = refuse` for every cap, so once unit 21 builds on unit 9 the `budgets.enforce`
default of `warn` never takes effect, and unit 9's AC5 and AC8 cannot pass. This unit is id 8's
promotion, with the skeptic's corrected fix: the derived-default refusal becomes a type, the caps
module catches that type alone on the cap's value read and reads it as no file value, and every
other refusal keeps S31's rule. It repairs units 9 and 21, the later at order 7, so it builds at
order 18, after every unit of the spec run.

## 2. Scope (IN)

- **S1** — The type. `tools/policy/policy.py` defines `class DerivedDefault(Refusal)`, and
  `read_default_value` raises it, never a bare `Refusal`, for a row whose `default` is
  `{ derived = "..." }`. Its `path`, `line` and `why` are the ones `TOOL-dGroundRules-21` S12 states,
  so `str()` and the `get` verb's exit 2 line are unchanged. Observed by AC2, AC6.
- **S2** — The read. `resolve_caps` in `tools/policy/budgets.py` reads each requested cap's value
  through the full `policy.resolve(f'budgets."{cap}"', ...)`, so `TOOL-dGroundRules-4`'s invalid
  branch and its last valid revision still apply, inside `except DerivedDefault`. A caught
  `DerivedDefault` is "no file value": the cap's value comes from its legacy home or the enforcer's
  `default:` as `TOOL-dGroundRules-9` S2 states, and its `CapAnswer` source is `default`. This is the
  answer unit 9's edge from unit 3 expects, reached through unit 21 S12's refusal rather than through
  a `Resolution`. Observed by AC1, AC4, AC5.
- **S3** — The exemption, and its bound. The catch wraps the `budgets.<cap>` value read only. Any
  other `Refusal` inside `resolve_caps`, a malformed file with no valid revision or under
  `policy-file.on-invalid = "refuse"` among them, keeps `TOOL-dGroundRules-21` S31's rule: the cap's
  mode is `refuse` and the refusal prints once. The `budgets.enforce` and `budgets.pinned` reads
  catch nothing, their catalogue defaults being literals. Observed by AC3.
- **S4** — The cases, entries in `CASES` of `tools/policy/check_policy.py`, each under a copy of the
  shipped `tools/policy/catalogue.toml` and `tools/policy/caps.toml`: `budgets-unset-derived`,
  `budgets-derived-invalid` and `budgets-derived-last-valid`. Observed by AC1, AC2, AC3, AC4.
- **S5** — The left-shift. `memory/gotchas/amendment-leaves-its-other-half-standing.md` gains, in
  "Where it bit", this build's instance: a later unit changed a shared function's return for one
  case while an earlier unit's consumes-from edge still expected the old return. "The fix" gains the
  check: a later unit that changes a shared function's return for a case greps every consumes-from
  edge naming that function and restates the consumer's expectation in its own spec. The record's
  anchors already take `memory/builds/`, so no anchor moves; `memory/gotchas/INDEX.md` is
  regenerated. Observed by AC7.
- **S6** — The codebase map. `python tools/codebase-map/gen_map.py --write` regenerates
  `memory/map/generated/` for the new class. Observed by AC8.

## 3. Non-goals (OUT)

- A literal default for `budgets.*`. v2's Default cell for it is prose, so `TOOL-dGroundRules-1`'s
  grammar makes it a derived default, and changing that is a departure from the clause.
- A new parameter on `resolve`. The brief's shared interface S4 fixes its signature (§8 F1).
- Reading a derived default anywhere but the caps module. `policy.py get` and the mirror keep
  `TOOL-dGroundRules-21` S12's refusal and its F4 omission.
- Rewriting `TOOL-dGroundRules-3`'s hands-off edge to unit 9. It is that unit's text; this unit states
  the corrected expectation in S2 and in its hands-off reciprocal on unit 9.

### Edges

- **consumes-from** `TOOL-dGroundRules-9` — `resolve_caps`, `CapAnswer` and S2's "no file value", which S2 here routes through the caught refusal
- **consumes-from** `TOOL-dGroundRules-21` — S12's derived-default refusal, which S1 types, and S31's refused-reader rule, which S3 bounds

## 4. Design

### Evidence

Every line below was read on 2026-10-23, in the tree this unit is written in; a cited line number
is the file's as this unit leaves it.

- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md:44-57` (S2) reads each
  cap's value through `policy.resolve`; `:107` is its consumes-from edge on unit 3, expecting source
  `default` for an unset `budgets.<cap>`; `:296-299` (AC8) expects mode `warn`, source `default`.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-3.md:100` sets
  `RESOLUTION_ORDER = (read_file_value, read_default_value)`, and `:65` is the reciprocal edge.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:123-126` (S12) refuses a
  derived default; `:195-201` (S31) gives a cap whose read refuses `mode = refuse`.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:120` writes a default as a
  TOML value or `{ derived = "<v2's Default cell>" }`; the packet's Policy keys give `budgets.*` the
  prose Default "the value its legacy home held, `template-size-limits.txt` moved by dSafePassage's
  step, then re-derived from evidence".
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md:136` defines
  `class Refusal(Exception)` with `path`, `line` and `why`.
- `tools/memory-tree/migrate_backlog.py:154` defines `class Refusal(Problem)`, the house precedent of
  a refusal typed by subclass.

### The read after this unit

```python
class DerivedDefault(Refusal):
    """A row whose default is { derived = ... }, which no reader computes yet (TOOL-dGroundRules-21 S12)."""

def read_cap_value(cap, repo, rev):                  # inside resolve_caps, per requested cap
    try:
        hit = policy.resolve(f'budgets."{cap}"', repo=repo, rev=rev)
    except policy.DerivedDefault:
        return None, "default"                       # no file value: unit 9 S2's legacy or default: value
    return hit.value, hit.source                     # every other Refusal propagates to S31's rule
```

A file that sets the cap resolves through `read_file_value` before `read_default_value` is reached,
so the catch never hides a set value. Under `policy-file.on-invalid = "last-valid"`, unit 4's branch
runs `RESOLUTION_ORDER` over the last valid table, and an unset cap there raises the same type, so
the pins and the switch that table holds still apply.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `DerivedDefault` | py.type, lexicon `--suggest` OK on 2026-10-23 | `tools/policy/policy.py` |
| `budgets-unset-derived`, `budgets-derived-invalid`, `budgets-derived-last-valid` | `CASES` entries | `tools/policy/check_policy.py` |

The read is one `try` inside `resolve_caps`; whether it is a named helper is the builder's call, and
a helper's name is confirmed with `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/budgets.py`
- `tools/policy/check_policy.py`
- `memory/gotchas/amendment-leaves-its-other-half-standing.md`
- `memory/gotchas/INDEX.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`

### Alternatives rejected

- **Catching every `Refusal` whose reason names a derived default.** It matches on text a later
  rewording breaks silently.
- **A flag on `resolve` returning `None` for an unset derived default.** §8 F1.

## 5. Production-readiness checklist

- security — the catch is narrowed to one type on one read, so an invalid or refused policy file
  still refuses every cap (S3); nothing reads as `warn` that read as `refuse` before unit 21.
- perf / scale — none: the same `resolve` call, one `except` clause.
- error / empty / loading states — an unset cap under the shipped catalogue now resolves; a derived
  default read by any other caller still refuses, naming its row.
- observability — `budgets.py resolve` prints source `default` for the caught case, as unit 9 AC8
  states.
- risks — a future catalogue row with a derived default read through `resolve_caps` would read as
  unset; only `budgets.*` rows reach it.
- testing — AC1 to AC8 and the `New arm:` line under §7.
- migration — none.
- user docs — N/A: `help/size-caps.md` (unit 9) already says an unset cap reads its legacy home.

## 6. Acceptance criteria

Every command runs from the repository root. A case passes when its run prints no `WRONG`. The
literals the criteria run are spelled whole here, once; the files under `tools/policy/` are created
by `TOOL-dGroundRules-1`, `-2` and `-9`, so none of these can be run before the build:

```text
CASE       = python tools/policy/check_policy.py --fixture <case>
CAPS       = python tools/policy/budgets.py resolve AGENTS.md
CAP_GET    = python tools/policy/policy.py get 'budgets."AGENTS.md"'
LIVE_CAPS  = python tools/policy/budgets.py resolve memory/guides/BUILD-METHOD.md 'memory/builds/*/spec/'
TYPE_PROBE = grep -n "class DerivedDefault(Refusal)" tools/policy/policy.py
CATCH_PROBE = grep -c "except policy.DerivedDefault" tools/policy/budgets.py
```

- **AC1** — When `CASE budgets-unset-derived` runs `CAPS` over a policy file that sets no
  `budgets.<cap>` and leaves the switch at its default, it prints the `AGENTS.md` row's value, mode
  `warn` and source `default`, and exits 0.
  Red when: the derived-default refusal reaches `TOOL-dGroundRules-21` S31's rule and the mode reads
  `refuse`.
- **AC2** — When the same case runs `CAP_GET`, it exits 2 printing `a derived default`.
  Red when: the catch moved into `resolve` itself, and every consumer reads a derived default as set.
- **AC3** — When `CASE budgets-derived-invalid` runs `CAPS` over one commit whose policy file does
  not parse, it prints mode `refuse` and the reader's refusal once.
  Red when: the catch takes every `Refusal`, and an invalid file reads as the `warn` default.
- **AC4** — When `CASE budgets-derived-last-valid` runs `CAPS` over a valid revision V setting
  `pinned = ["AGENTS.md"]` under `[budgets]` followed by a commit C whose file does not parse, it
  prints the row's value, mode `refuse` and source `default`.
  Red when: the unset cap's read skips `TOOL-dGroundRules-4`'s branch, and the pin V holds is lost.
- **AC5** — When `LIVE_CAPS` runs over this repository at the unit's commit, it prints each value its
  `template-size-limits.txt` row holds, mode `warn` and source `default`, which is
  `TOOL-dGroundRules-9` AC8 observed after `TOOL-dGroundRules-21`.
  Red when: a correct build of units 9 and 21 together refuses every cap.
  figure: the values are DERIVED from the rows at observation time.
- **AC6** — When `TYPE_PROBE` runs it prints one line, and `CATCH_PROBE` prints `1`.
  Red when: the derived default is told apart by its reason text, or caught in more than one place.
- **AC7** — When
  `grep -c "TOOL-dGroundRules-62" memory/gotchas/amendment-leaves-its-other-half-standing.md` runs it
  prints `1` or more, and `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the class gains no instance and no check, or the generated index is stale.
- **AC8** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's commit it exits 0.
  Red when: the map does not carry `DerivedDefault`.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named on the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC2 AC3 AC4 · the three cases of S4, each planting its policy revisions in the temporary repository under the shipped catalogue and census and asserting the mode and source it prints · none

## 8. Open questions

- **F1 — How does the caps module read an unset `budgets.<cap>` as no file value?** (a) A typed
  refusal: `read_default_value` raises `DerivedDefault`, a `Refusal` subclass, and `resolve_caps`
  catches that type alone around the full `resolve`. (b) A keyword on `resolve` that returns `None`
  for an unset derived default, called through the full `resolve`. (c) Catch `Refusal` and match the
  reason text. (c) breaks silently on a reworded reason. (b) respells the signature the brief's
  shared interface S4 fixes for every writer, `resolve(key, repo=".", rev=None)`. (a) changes no
  signature, keeps unit 4's ladder, and is the skeptic's first option made exact. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 8 (HIGH, item H4) of the spec run's
  closing diff review, from the skeptic's corrected fix, with units 1, 2, 3, 9 and 21 read at
  `7810198ad` on 2026-10-23.
- rev-2 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.

## 10. Reuse audit

The seam extended is `resolve_caps` in `tools/policy/budgets.py` (`TOOL-dGroundRules-9` S2), whose
call to `policy.resolve` gains one `except`, and the `Refusal` type of `TOOL-dGroundRules-2`, which
gains one subclass, as `tools/memory-tree/migrate_backlog.py:154` types its own refusal.
`python tools/codebase-map/reuse_lookup.py "tell a refusal for an unset derived default apart from
other policy refusals"` ranked `refusal` (`tools/memory-recall/recall_conf.py`), `DesignRefusal`
(`tools/memory-tree/design_lib.py`) and the `Refusal` classes of six kits; each is its own kit's
exception and none is importable by the policy kit, so the subclass lives in `policy.py`. The recall
probe returned the closing review's H4, unit 9's edge on unit 3 and unit 1's default grammar, each in
agreement with the specs as read; no hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "what does resolve return for an unset
budgets cap whose default is derived" --terms "budgets resolve_caps read_default_value derived
default refusal Refusal source default warn S31 consumes-from"`
