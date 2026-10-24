# TOOL-dGroundRules-62 — an unset `budgets.<cap>` reads as no file value: the derived-default refusal is a type the caps module catches, and only that refusal

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-62-deviation-50.md](../build/2026-10-23-build-TOOL-dGroundRules-62-deviation-50.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-61-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-task.md) | research | TOOL-dGroundRules-61 TOOL-dGroundRules-63 |
| [2026-10-23-prompt-TOOL-dGroundRules-62-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-62-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md) | research | TOOL-dGroundRules-55 TOOL-dGroundRules-61 TOOL-dGroundRules-64 |
| [2026-10-24-prompt-TOOL-dGroundRules-62-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-62-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-62-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-62-probe-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
confirmed **id 8 at HIGH**, item **H4**: units 9 and 21 give two answers to one question.
`TOOL-dGroundRules-9` S2 reads an unset `budgets.<cap>` as "no file value", expecting source
`default` (its consumes-from edge on `TOOL-dGroundRules-3`). `TOOL-dGroundRules-21` S12 makes
`read_default_value` refuse every `{ derived = ... }` default, and `budgets.*` has only a derived
default. S31 then reads that refusal as a refused reader, so every cap's mode is `refuse`.

Both units are built. Commit `f6674a6a2` built S12 and S31 and left their joint effect to this unit
in its `Decided:` line, and `TOOL-dGroundRules-21`'s acceptance ledger names what it costs:
`budgets-switch-refuse`, `budgets-pinned-warn` and each `budgets-cap-` case's `warn` half read
`refuse`. On this repository today an unset cap prints mode `refuse` with the `READER_REFUSED` rule.
This unit is id 8's promotion with the skeptic's corrected fix: the derived-default refusal becomes
a type, the caps module answers that type alone, on the cap's value read, as no file value, and
every other refusal keeps the `READER_REFUSED` branch.

## 2. Scope (IN)

- **S1** — The type. `tools/policy/policy.py` defines `class DerivedDefault(Refusal)`, and
  `read_default_value` raises it for a row `check_derived` accepts, with the path, line and why it
  raises today, `DERIVED_WHY` among them, so `str()` and the `get` verb's exit 2 line are unchanged.
  The nested `add` of `render_mirror` catches `DerivedDefault` where it now tests
  `DERIVED_WHY in exc.why`, the text match its own comment leaves to this unit; every other refusal
  there passes through as today. Observed by AC2, AC6.
- **S2** — The read. `resolve_caps` in `tools/policy/budgets.py` keeps its one
  `policy.read_revision` read and its local `read_key`, whose `except policy.Refusal` collects the
  refusal once and answers `None`. `read_key` gains one keyword naming the refusal type it answers as
  no file value, catching nothing by default, and the `budgets.<cap>` value read alone passes
  `policy.DerivedDefault`. That answer carries no value, so the cap's value is the legacy home's or
  the `default:` handed in, source `default` or `constant` as `TOOL-dGroundRules-9` S2 states, and
  the `READER_REFUSED` override after that read does not fire: the mode stays the pin's or the
  switch's. The type is raised inside `policy.resolve_read`, so the read of the landed table and the
  `read_last_valid_value` branch over the last valid one both reach the catch. Observed by AC1, AC4,
  AC5.
- **S3** — The bound. The `budgets.enforce` and `budgets.pinned` reads pass no type, their catalogue
  defaults being literals, and every other refusal of any read keeps the `READER_REFUSED` branch:
  mode `refuse`, the refusal printed once. Observed by AC3, AC6.
- **S4** — The case. `budgets-unset-derived`, a branch of `run_budget_case` in
  `tools/policy/check_policy.py` named in `BUDGET_CASES`, builds three repositories under the shipped
  catalogue, census and limits file, each read by the `resolve --explain` verb for the `AGENTS.md`
  cap: (a) one commit whose policy file does not parse; (b) a valid revision V setting the switch to
  `warn` and pinning that cap, then a commit C whose policy file does not parse; (c) V with no pin,
  then C. Observed by AC3, AC4.
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
- A new parameter on `policy.resolve` or `policy.resolve_read`. The brief's shared interface S4 fixes
  `resolve`'s signature (§8 F1); the keyword of S2 is on the caps module's local `read_key` alone.
- Reading a derived default anywhere but the caps module. The `get` verb and the mirror keep
  `TOOL-dGroundRules-21` S12's refusal and its F4 omission.
- A new case for AC1: `budgets-switch-refuse` and `budgets-pinned-warn` already observe it.
- Rewriting `TOOL-dGroundRules-3`'s hands-off edge to unit 9. It is that unit's text; this unit states
  the corrected expectation in S2 and in its hands-off reciprocal on unit 9.

### Edges

- **consumes-from** `TOOL-dGroundRules-9` — `resolve_caps`, `CapAnswer` and S2's "no file value", which S2 here routes through the typed refusal
- **consumes-from** `TOOL-dGroundRules-21` — S12's derived-default refusal, which S1 types, and S31's `READER_REFUSED` branch, which S3 bounds

## 4. Design

### Evidence

Every line below was read on 2026-10-24 at `8fa309e89`, one gotchas commit past `8eab342e0` that
touched nothing under `tools/`; each is cited by symbol or by AC id.

- `tools/policy/budgets.py` `resolve_caps`: one `policy.read_revision` read in a `try` that appends
  a refusal to `refused`; the nested `read_key` calls `policy.resolve_read` and answers every
  `policy.Refusal` with `None`, collected once; the cap's value read is followed by the branch
  setting `READER_REFUSED` when it answered `None` over a landed read, its comment naming this unit.
  A pin sets the rule `budgets.pinned names it` before that branch, which overwrites it.
- `tools/policy/policy.py`: `read_default_value` raises a bare `Refusal` for a `check_derived` row,
  its why carrying `DERIVED_WHY`; `read_last_valid_value` and `resolve_read` catch nothing, so the
  refusal reaches `read_key` from either branch; `render_mirror`'s `add` matches `DERIVED_WHY` in the
  why, its ponytail comment reading "until TOOL-dGroundRules-62 types it".
- `tools/policy/catalogue.toml`: the `budgets.*` row's default is `{ derived = ... }`;
  `budgets.enforce` defaults to `warn`, `budgets.pinned` to an empty list, and
  `policy-file.on-invalid` to `last-valid`.
- Probes run from the root on 2026-10-24: `python tools/policy/budgets.py resolve --explain` over
  the build method and the live-spec class row printed each limits value with mode `refuse`, source
  `default`, the `READER_REFUSED` rule and one refusal line per cap; `get` of the `AGENTS.md` cap
  exited 2 naming `a derived default`.
- `TOOL-dGroundRules-9` AC8 expects mode `warn`, source `default` for those two caps;
  `TOOL-dGroundRules-21` S12 and S31 state the refusal and the branch, observed by its AC12 and AC31.
- `tools/memory-tree/migrate_backlog.py` `Refusal(Problem)` is the house precedent of a refusal
  typed by subclass.

### The read after this unit

```python
# tools/policy/policy.py
class DerivedDefault(Refusal):
    """A row whose default is { derived = ... }, which no reader computes yet (TOOL-dGroundRules-21 S12)."""
# read_default_value: `raise DerivedDefault(...)` with today's arguments
# render_mirror's add: `except DerivedDefault: return`, no text match

# tools/policy/budgets.py, inside resolve_caps
    def read_key(key, unset=()):                  # () catches nothing
        if read is None:
            return None
        path = policy.parse_key(key)
        try:
            return policy.resolve_read(path, policy.read_catalogue_row(path, rows), read)
        except unset:                             # no file value: held stays None, mode untouched
            return policy.Resolution(None, "default", "")
        except policy.Refusal as exc:             # THE REFUSED READER, unchanged
            ...
    hit = read_key(f"budgets.{seg}", unset=policy.DerivedDefault)   # the cap's value read alone
```

A file that sets the cap answers through `read_file_value` before `read_default_value` is reached,
so the catch never hides a set value. Under `last-valid`, an unset cap in the last valid table raises
the same type, so the pin and the switch that table holds still decide the mode.

**What each staging can tell apart.** A refusal of the cap's read that is not `DerivedDefault`, with
the switch's own reads resolving, has no reachable staging: a malformed file or one under
`policy-file.on-invalid = "refuse"` refuses every read alike, so `budgets.enforce` refuses first and
the mode is `refuse` whatever the cap's catch takes. AC3 therefore reds only when the no-file-value
answer reaches the switch's reads; the bound at the cap's call alone is held by AC6's probe. AC4's
mode alone is `refuse` before and after this unit; the `--explain` rule line is what tells a kept
pin, `budgets.pinned names it`, from a lost one, which reads `budgets.enforce is warn` as repository
(c) does, or from the refused read of today, `READER_REFUSED`.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `DerivedDefault` | py.type, lexicon `--suggest` OK on 2026-10-24 | `tools/policy/policy.py` |
| `budgets-unset-derived` | a `run_budget_case` branch, in `BUDGET_CASES` | `tools/policy/check_policy.py` |

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

- **Matching the refusal's text**, as the mirror does today. A later rewording breaks it silently.
- **A flag on `resolve` returning `None` for an unset derived default.** §8 F1.
- **A catch around `read_key`'s call site.** `read_key` already answers every refusal; a typed
  `except` beside its own keeps the one read and the once-printed refusal in one place.

## 5. Production-readiness checklist

- security — the no-file-value answer is one type on one read, so an invalid or refused policy file
  still refuses every cap (S3); nothing reads as `warn` that read as `refuse` before unit 21.
- perf / scale — none: the same one read, one more `except` clause.
- error / empty / loading states — an unset cap under the shipped catalogue resolves; a derived
  default read by any other caller still refuses, naming its row.
- observability — `budgets.py resolve` prints source `default` and the switch's or the pin's rule
  for the caught case, with no refusal line.
- risks — a future catalogue row with a derived default read through `resolve_caps` would read as
  unset; only `budgets.*` rows reach it.
- testing — AC1 to AC8 and the `New arm:` line under §7.
- migration — none.
- user docs — N/A: `help/size-caps.md`, "Where each cap's value is declared today", already says a
  cap keeps the value its home holds, the behaviour this unit restores.

## 6. Acceptance criteria

Every command runs from the repository root. A case passes when its run prints no `WRONG`. The
literals the criteria run are spelled whole here, once:

```text
CASE        = python tools/policy/check_policy.py --fixture <case>
CAP_GET     = python tools/policy/policy.py get 'budgets."AGENTS.md"'
LIVE_CAPS   = python tools/policy/budgets.py resolve --explain memory/guides/BUILD-METHOD.md 'memory/builds/*/spec/'
TYPE_PROBE  = grep -n "class DerivedDefault(Refusal)" tools/policy/policy.py
CATCH_PROBE = grep -c "policy.DerivedDefault" tools/policy/budgets.py
TEXT_PROBE  = grep -c "DERIVED_WHY in" tools/policy/policy.py
```

- **AC1** — When `CASE` runs `budgets-switch-refuse` and then `budgets-pinned-warn`, each prints no
  `WRONG`: an unset cap under `warn` passes a breach, and a pinned one refuses naming its pin.
  Red when: the derived-default refusal reaches the `READER_REFUSED` branch and the `warn` halves read `refuse`, as at `8eab342e0`.
- **AC2** — When `CAP_GET` runs it exits 2 printing `a derived default`, and `CASE` over
  `resolution-derived-default` prints no `WRONG`, its mirror rendered with no derived key. Both are
  green before this unit, by `TOOL-dGroundRules-21` S12 and its AC12; the break that can red them
  is staged on a scratch copy of the kit.
  Red when: the no-file-value answer moves into `read_default_value` and `get` exits 0, or the raise stays a bare `Refusal` while the mirror catches the type, and `mirror --print` exits 2.
- **AC3** — When `CASE` runs `budgets-unset-derived`, repository (a) prints the `AGENTS.md` row's
  value with mode `refuse` and the reader's refusal once. Green before this unit, by the
  `READER_REFUSED` branch of `f6674a6a2`; §4 says why only a widening that reaches the switch's
  reads can red it.
  Red when: `read_key` answers every refusal as no file value, and the invalid file reads as the `warn` default.
- **AC4** — When the same case reads repository (b), it prints the row's value, mode `refuse`,
  source `default`, the `--explain` rule `budgets.pinned names it` and no `policy: refused` line;
  repository (c) prints mode `warn` and the rule `budgets.enforce is warn`. Mode `refuse` in (b)
  holds before this unit; the rule line and (c) are red at `8eab342e0`, which print the
  `READER_REFUSED` rule for both.
  Red when: the cap's read under `last-valid` misses the catch, or the pin V holds is lost and (b) reads like (c).
- **AC5** — When `LIVE_CAPS` runs over this repository at the unit's commit, it prints each value
  its `template-size-limits.txt` row holds, mode `warn` and source `default`, and no refusal line:
  `TOOL-dGroundRules-9` AC8 observed after `TOOL-dGroundRules-21`.
  Red when: a correct build of units 9 and 21 together still refuses every cap, as on 2026-10-24.
  figure: the values are DERIVED from the rows at observation time.
- **AC6** — When `TYPE_PROBE` runs it prints one line, `CATCH_PROBE` prints `1` and `TEXT_PROBE`
  prints `0`; at `8eab342e0` they print nothing, `0` and `1`.
  Red when: the derived default is told apart by its text, or a second read in the caps module passes the type.
- **AC7** — When `grep -c "TOOL-dGroundRules-62" memory/gotchas/amendment-leaves-its-other-half-standing.md` runs it prints `1` or more, and `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the class gains no instance and no check, or the generated index is stale.
- **AC8** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's commit it exits 0.
  Red when: the map does not carry `DerivedDefault`.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The `policy fixtures` leg in `tools/gate-legs.json` runs every case §6 names, the two of AC1
among them, whose red `TOOL-dGroundRules-21`'s ledger records and which this unit turns green.

New arm: tools/policy/check_policy.py --fixture budgets-unset-derived · covers AC3 AC4 · repositories (b) and (c) print the READER_REFUSED rule on HEAD's budgets.py, its red; (a) reds only on a scratch copy whose read_key answers every refusal as no file value · none

## 8. Open questions

- **F1 — How does the caps module read an unset `budgets.<cap>` as no file value?** (a) A typed
  refusal: `read_default_value` raises `DerivedDefault`, a `Refusal` subclass, and `resolve_caps`
  answers that type alone on the cap's value read, inside its one read of the policy file. (b) A
  keyword on `resolve` that returns `None` for an unset derived default. (c) Catch `Refusal` and
  match the reason text. (c) breaks silently on a reworded reason. (b) respells the signature the
  brief's shared interface S4 fixes for every writer, `resolve(key, repo=".", rev=None)`. (a)
  changes no signature, keeps unit 4's ladder, and is the skeptic's first option made exact.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 8 (HIGH, item H4) of the spec run's
  closing diff review, from the skeptic's corrected fix, with units 1, 2, 3, 9 and 21 read at
  `7810198ad` on 2026-10-23.
- rev-2 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-3 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 · S2 · S3 · S4 · AC1 to AC6 · a read-only
  probe of steps 15 to 20 at `e1c7051cb` found this spec stale against the built branch, re-read
  at `8fa309e89`. Disagreements: S2 and the sketch wrapped a fresh `policy.resolve` per cap, where
  `resolve_caps` reads the file once and every key through `read_key`, which catches every
  refusal; AC2, AC3 and AC4 were stated as new while green before this unit; AC4's mode could not
  tell a kept pin from a lost one; §4 and §6 cited spec lines by number and said the policy files
  and legs could not run. Rulings: the typed catch is a keyword on `read_key`, passed only at the
  cap's value read, keeping the one read and the `READER_REFUSED` branch; S1 also types the
  mirror's text match its own comment leaves here; AC1 observes the existing cases unit 21's ledger
  records red, so S4 adds one case, not three; AC2 and AC3 are restated green before, each with the
  break that reds it, and §4 says why only a widening reaching the switch's reads reds AC3; AC4
  reads the `--explain` rule, with (c) as the lost-pin contrast; every citation is by symbol or AC
  id; the leg is named as live. No literal of the units retired at `8eab342e0` is consumed.

## 10. Reuse audit

The seam extended is the nested `read_key` of `resolve_caps` in `tools/policy/budgets.py`
(`TOOL-dGroundRules-9` S2, `TOOL-dGroundRules-21` S31), whose `except policy.Refusal` gains one
typed sibling clause, and the `Refusal` type of `TOOL-dGroundRules-2`, which gains one subclass, as
`tools/memory-tree/migrate_backlog.py` types its own `Refusal(Problem)`. The case is one more branch
of `run_budget_case`, built as its siblings build theirs.
`tools/codebase-map/reuse_lookup.py`, asked to "answer one typed policy refusal as no file value
inside the caps reader's local key read", ranked
`read`, `read_text`, `key` and the `Refusal` classes of seven kits; each `Refusal` is its own kit's
exception and none is importable by the policy kit, so the subclass lives in `policy.py`. The recall
probe returned the closing review's H4, this spec's F1 and the probe brief's item 1, each in
agreement with the code as read; no hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does resolve_caps read an unset budgets cap whose default is derived" --terms "resolve_caps read_key READER_REFUSED read_default_value DerivedDefault derived default refusal no file value budgets-switch-refuse transitional red"`
