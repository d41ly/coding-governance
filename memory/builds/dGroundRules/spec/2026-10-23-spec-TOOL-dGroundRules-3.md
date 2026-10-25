# TOOL-dGroundRules-3 — one resolution order: the file's override, then the catalogue default with its reason

**Status:** CLOSED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0009@7d93fce9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-3-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-3-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-prompt-TOOL-dGroundRules-3-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-3-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-3-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-3-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-3-span-fold-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-3-span-fold-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

Every key resolves in one order, spelled once: an override in the file, then the named preset's
value once dKeptSession adds presets to the reader, then the catalogue default with the reason
recorded. This unit writes that order into `resolve` in `tools/policy/policy.py` as one tuple,
`RESOLUTION_ORDER`, so an absent file and a file naming no preset read every key's default and say
why, and a later build adds its step to the tuple instead of a second order beside it.

## 2. Scope (IN)

- **S1** — `RESOLUTION_ORDER`, a module-level tuple of step functions, `(read_file_value,
  read_default_value)`. `resolve` calls each in turn with the key's path, its catalogue row, the
  parsed table (`None` for an absent file), the sha and how it was found, and returns the first
  `Resolution` a step returns. No other function in the module chooses between a file value and a
  default. Observed by AC1, AC6.
- **S2** — `read_default_value` returns `Resolution(<the row's default>, "default", reason)`. The
  reason names the path and the sha8, and says which case it is: the file is absent at that revision,
  or present and not setting the key. Observed by AC2, AC3.
- **S3** — The preset step, stated rather than coded. No step returns a preset's value: dKeptSession
  adds presets, and with them a step between the file and the default. When the parsed table sets
  `preset`, the default's reason names that preset and says it is not applied until dKeptSession
  adds presets to this reader. Observed by AC4.
- **S4** — A catalogue row carrying no `default` field resolves to a `Refusal` naming the row in
  `tools/policy/catalogue.toml`, never to an invented value. Observed by AC5.
- **S5** — The two interim refusals `TOOL-dGroundRules-2` left in `resolve` for an absent file and an
  unset key are removed; the order answers both. Observed by AC2, AC3.
- **S6** — Cases in `CASES` of `tools/policy/check_policy.py`, grouped as `resolution-order`, each
  planting one case of AC1 to AC5 in a temporary repository under `--fixture` and printing its
  `policy-fixture:` line with the outcome it observed. Observed by AC1, AC2, AC3, AC4, AC5.
- **S7** — A paragraph on `help/policy.md` stating the order and what `--explain` prints for each
  source. Observed by AC7.

## 3. Non-goals (OUT)

- A preset step that returns nothing. The step is dKeptSession's to add, with the presets; a function
  standing in for it now would be scaffolding the charter's `[yagni]` rule refuses (§8 F2).
- Applying a named preset's values, or refusing a file that names one (§8 F3). The strict-named file
  is dKeptSession's arm, as the audit's FM9 fix left it.
- What an invalid file reads: `TOOL-dGroundRules-4`'s, which runs this order over the last valid
  revision's table.
- Legacy homes. Units 9 and 10 read `template-size-limits.txt` and `.agent-cap.conf`; where either
  needs a step, it adds it to `RESOLUTION_ORDER`, and this unit adds none.
- The catalogue's defaults themselves, and the shape audit that grades them: `TOOL-dGroundRules-1`'s.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — `tools/policy/catalogue.toml`, each row's `default` field, `load_catalogue`, and `check_policy.py`'s `CASES` with the `policy fixtures` leg
- **consumes-from** `TOOL-dGroundRules-2` — `resolve`, `read_file_value`, `Resolution` and `Refusal`, and the interim refusals this unit removes
- **hands-off** `TOOL-dGroundRules-4` — `RESOLUTION_ORDER`, which that unit runs over the table of the last valid revision when the current file is invalid
- **hands-off** `TOOL-dGroundRules-9` — a key the file does not set resolving with source `default`, which that unit reads as "no file value" for a `budgets.<cap>`
- **hands-off** `TOOL-dGroundRules-10` — the resolution order, whose result that unit lowers for `runtime.agents-in-flight`
- **hands-off** `TOOL-dGroundRules-21` — a derived default resolved to a refusal naming its row, and the regenerated codebase map (findings 3, 40)

## 4. Design

### Evidence

- The clause's own text fixes the order and its two default cases: "an override in the file, then
  the named preset's value once dKeptSession adds presets to this reader, then the catalogue default
  with the reason recorded, which is all an absent file or one naming no preset reads".
- The design audit's M10 raised the order because "the reader reads a key the file does not carry as
  its catalogue default" whatever preset the file names
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md:222-232`).
- The audit fold's FM9 fix moved the strict-named-file case out of this build, to the clause of
  the build that adds the preset step, which the record names as dDeclaredLoop's M10 clause
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-audit-fold-closing.md:174-185`).
- `preset` is a catalogue key whose Owner is dKeptSession, default `standard`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1141`).

### The order

```python
def resolve(key, repo=".", rev=None):
    path = parse_key(key)
    row = read_catalogue_row(path, load_catalogue(kit))     # TOOL-dGroundRules-1's loader
    sha, how = ...                                          # TOOL-dGroundRules-2
    text = read_policy_text(repo, sha)
    table = None if text is None else parse_policy(text)    # TOOL-dGroundRules-4 guards this line
    for step in RESOLUTION_ORDER:
        hit = step(path, row, table, sha, how)
        if hit is not None:
            return hit
    raise Refusal(...)                                      # unreachable while the default step stands

RESOLUTION_ORDER = (read_file_value, read_default_value)
```

Each step takes the same five arguments and returns a `Resolution` or `None`, so a step is added by
naming it in the tuple. `read_file_value` keeps its `TOOL-dGroundRules-2` signature and behaviour.

### Reasons, as `--explain` prints them

| case | source | reason |
|---|---|---|
| the file sets the key | `file` | `set in .governance/policy.toml at <sha8>, <how>` |
| the file is present and does not set it | `default` | `not set in .governance/policy.toml at <sha8>, <how>; the catalogue default` |
| the file is absent | `default` | `.governance/policy.toml is absent at <sha8>, <how>; the catalogue default` |
| either default case, the file naming `preset` | `default` | the reason above, then `; the file names preset <name>, not applied until dKeptSession adds presets to this reader` |

A file setting `preset = "standard"` gets the preset clause too: the reason reports what the file
names, and it does not decide whether a preset's values equal the defaults.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `RESOLUTION_ORDER` | module constant, a tuple of step functions | `tools/policy/policy.py` |
| `read_default_value` | function, a step | `tools/policy/policy.py` |
| `resolution-order` | fixture case group in `CASES` | `tools/policy/check_policy.py` |

The function leads with `read`, a verb `.lexicon.conf`'s `VERBS` declares. `KIT_POLICY_VERSION` in
`policy.py` moves with this unit.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `help/policy.md`

### Alternatives rejected

- **The order as nested `if` branches inside `resolve`.** It works, and the next build to add a step
  edits the body instead of naming a function; the tuple is the one place the order is read.
- **A `read_preset_value` step returning `None` until dKeptSession.** A step that cannot fire reads as
  coverage of a clause half it does not build (§8 F2).

## 5. Production-readiness checklist

- security — a default is read only where the file is absent or silent on the key; an invalid file
  never reaches the default step once `TOOL-dGroundRules-4` lands, and a row with no default refuses
  rather than inventing one. A file naming `strict` reads defaults at this build, and the reason says
  so on every read (§8 F3).
- perf / scale — no git call beyond `TOOL-dGroundRules-2`'s; the order is two function calls.
- error / empty / loading states — absent file, unset key and named preset each read a default with
  its own reason; a row with no default refuses with exit 2.
- observability — the reason of every default names its case and any named preset.
- risks — a consumer that ignores `source` cannot tell a default from an override; `--explain` and
  the mirror (unit 5) carry it.
- testing — AC1 to AC7; the arm under §7.
- migration — none: the file is new in this build.
- user docs — the order on `help/policy.md`.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the module and the arm CLI by bare
name, `policy.py` and `check_policy.py`, and the help page as `policy.md` under `help/`, because this
run creates them and the spec-token checker grades a path-shaped token in a criterion against the
tracked set. The fixture repositories sit under `%TEMP%`, short-named. Every `get` below reads with
`--rev HEAD` at the case's planted commit, so no case rests on the landed-ref rule
`TOOL-dGroundRules-2` observes.

- **AC1** — When `check_policy.py --fixture` reaches the `resolution-order` cases and one plants a
  policy file setting
  `budgets.enforce = "refuse"`, `policy.py get budgets.enforce --explain` prints `refuse` and a
  stderr line naming source `file`. Red when: the default `warn` is returned for a key the file sets.
- **AC2** — When a case plants a policy file that sets `budgets.enforce` only,
  `policy.py get runtime.agents-in-flight --explain` prints the catalogue default `6` with source
  `default` and a reason opening `not set in`. Red when: an unset key refuses, or reads anything but
  the row's `default`.
- **AC3** — When a case plants a revision with no policy file,
  `policy.py get budgets.enforce --explain` prints `warn` with source `default` and a reason
  naming `is absent at`. Red when: an absent file refuses, or its reason reads as an unset key.
- **AC4** — When a case plants a policy file setting only `preset = "strict"`,
  `policy.py get budgets.enforce --explain` prints `warn`, source `default`, and a reason naming
  `strict` and `not applied until dKeptSession`; with `budgets.enforce = "refuse"` added, it prints
  `refuse` with source `file`. Red when: the named preset is missing from the reason, or the default
  wins over a file override.
- **AC5** — When a case loads a catalogue whose `budgets.enforce` row carries no `default` and the
  policy file does not set the key, `policy.py get budgets.enforce` exits 2 naming `catalogue.toml`
  and the row. Red when: a value is printed for a row with no default.
  fixture: the catalogue is planted in the fixture's copy of the kit, never in the tracked one.
- **AC6** — When `python -c` imports `policy.py` from `tools/policy/` and prints
  `[f.__name__ for f in policy.RESOLUTION_ORDER]`, it prints
  `['read_file_value', 'read_default_value']`. Red when: the order is spelled elsewhere, a step
  that cannot fire stands in for the preset, or the default precedes the file.
- **AC7** — When `grep -n 'RESOLUTION_ORDER\|catalogue default'` runs over `policy.md` under
  `help/`, it prints the order's paragraph. Red when: the order ships undocumented.

## 7. Gates

`lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)`

The `policy fixtures` leg `TOOL-dGroundRules-1` declares runs these cases; it is named here rather
than on the line above, because it does not exist at this spec's base.

New arm: tools/policy/check_policy.py --fixture (the `resolution-order` cases) · covers AC1 AC2 AC3 AC4 AC5 · a fixture repository per case, a key the file sets, a key it does not, an absent file, a file naming `strict` with and without an override, and a planted catalogue row with no default · none

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens a spec header reuses
  (`memory/HYGIENE.md:105`). Liveness: the line would print `DRAFT` if the vocabulary declared it.
  Observed 2026-10-23: it does not. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, which
  `memory/TEMPLATE-SPEC.md:62` gives as "drafting".
- **F2 — Is the preset step a function that returns nothing, or a sentence in the default's
  reason?** The brief asks for "a no-op branch until dKeptSession adds presets, stated as such". (a) A
  `read_preset_value` step in the tuple that always returns `None`. (b) No step; the default's reason
  names a preset the file sets and says it is not applied. (a) is a dead branch that reads as
  coverage and that dKeptSession rewrites anyway; (b) states the same thing where an owner reads it,
  on every affected read. Recommendation (b), the more capable, and the charter's `[yagni]`. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b).
- **F3 — What does a file naming a preset read before dKeptSession?** The clause says the default is
  what "an absent file or one naming no preset reads" and is silent on a file that names one. (a) The
  default, with the reason of S3. (b) Refuse every read of such a file. (c) Refuse it at validation.
  (b) and (c) make a policy write the catalogue allows (`preset` is a key with `strict` among its
  values) stop every consumer, a rule no clause states. The audit fold's FM9 fix left the
  strict-named file to the build that adds presets, and no record asks this build to refuse it.
  (a) answers every read and names the unapplied preset on each. Recommendation (a), the more
  capable. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the reciprocal **hands-off** edges to TOOL-dGroundRules-9, TOOL-dGroundRules-10 added, each naming what that unit's own §3 **consumes-from** line takes from this one; hygiene check 12's edge join read them as missing. No scope, design or acceptance moved.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-4 · 2026-10-24 · §6 · AC3, AC6: a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "resolve a configuration value from an override,
then a default, recording which source answered"` ranked `resolve` in
`tools/memory-recall/recall_conf.py:277`, which loads one conf layer and refuses when it is absent,
and the kit-dir and Python resolvers; none orders sources or records which one answered. No existing
seam fits beyond `TOOL-dGroundRules-2`'s `resolve`, which this unit extends with the tuple. The recall
hits on the design audit's M10
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md:222`) name
dDeclaredLoop as the build adding presets; the clause and v2's `preset` row name dKeptSession, and
this spec follows the clause.

Recall terms used: `python tools/memory-recall/query.py "what order resolves a policy key between the
file override, the preset and the catalogue default" --terms "resolution order override preset
catalogue default reason absent file dKeptSession DA-M10 H4 standard"`
