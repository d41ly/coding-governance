# KICK-dKeptSession-32 — the scaffold writes only the keys the named preset leaves unassigned, so a preset answered at intake is the posture the adopter reads

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 6 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-32-deviation-321.md](../build/2026-10-26-build-KICK-dKeptSession-32-deviation-321.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 1 at HIGH**, report item **H1**, which no other id shares.

`render_scaffold` writes every literal-defaulted row dGroundRules owns at its default, and
`budgets.enforce = "warn"` is one of them. `KICK-dKeptSession-4` S2 only adds `preset = "<name>"`
above those tables, and `KICK-dKeptSession-2`'s order reads the file before the preset, so the
file's literal `warn` beats strict's `refuse`. Every adopter answering `strict` at intake ships the
standard posture for that key, and `preset --diff` lists an exception nobody chose. This unit makes
the scaffold leave out every key the named preset assigns. It repairs `KICK-dKeptSession-4` and
builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — id 1. The rendered rows. `render_scaffold(rows, preset)` in `tools/policy/policy.py`
  writes a row only where `derive_preset_assignment(<preset>, …)` (`KICK-dKeptSession-1`) assigns it
  no value, by `KICK-dKeptSession-33`'s rule: the store's `never` keys and the rows it leaves
  unassigned. A row the preset assigns is written as one comment line instead, `# <key> = <value>
  (preset <name>)`, so the file still shows the posture it starts from. Observed by AC1 and AC2.
- **S2** — id 1. The one caller. `cmd_scaffold` passes the `--preset` value `KICK-dKeptSession-4`
  S2 adds; `render_scaffold` takes no default for `preset`, so a call naming none is a `TypeError`
  at the fixture rather than a silent standard scaffold. Observed by AC3.
- **S3** — id 1. The fixture case `scaffold-preset` in `tools/policy/check_policy.py`: per shipped
  preset, one scratch repository scaffolded with `--preset <name>`, then `policy.py get` over every
  key the preset assigns and `policy.py preset --diff` (`KICK-dKeptSession-3` S1). Observed by AC1,
  AC2.
- **S4** — id 1. `KICK-dKeptSession-4` S2's "above dGroundRules' tables" is superseded by name here:
  the tables hold only the rows S1 writes. Its AC3 is answered in that unit's acceptance ledger with
  AC1's output. Observed by AC1.

## 3. Non-goals (OUT)

- The intake answer, the token and the kept-file line: `KICK-dKeptSession-4`'s, unchanged.
- The wrapper's error path: the refusal `adopt-policy.sh` swallows is id 20, item M11, batched into
  `KICK-dKeptSession-44`.
- Which rows a preset leaves unassigned: `KICK-dKeptSession-33`'s rule, read here.
- The report's left-shift fixture, a scaffold under each shipped preset asserting an empty
  `preset --diff`: S3 is that fixture.

### Edges

- **consumes-from** `KICK-dKeptSession-4` — `render_scaffold`'s preset argument and `cmd_scaffold`'s `--preset`, whose written rows this unit narrows (id 1)
- **consumes-from** `KICK-dKeptSession-33` — the store's rule for which rows a preset assigns, which decides the rows S1 leaves out
- **consumes-from** `KICK-dKeptSession-2` — `read_preset_value`, without which a left-out row reads its default and not the preset
- **consumes-from** `KICK-dKeptSession-3` — `policy.py preset --diff`, whose `- no key differs` line AC2 observes

## 4. Design

### Evidence

- `render_scaffold(rows)` writes each row whose `owner` is `SCAFFOLD_OWNER` and whose default is not
  derived (`git show 3c8c4718a:tools/policy/policy.py`, lines 1313-1324; `SCAFFOLD_OWNER` at :98).
- At `3c8c4718a` those rows include `budgets.enforce` with default `warn` (catalogue row read with
  `tomllib`, 2026-10-26), and v2's table sets it `refuse` under strict (v2:1669).
- v2's never list holds `policy-file.on-invalid`, `runtime.agents-in-flight` and `budgets.pinned`,
  and not `budgets.enforce` (v2:1430-1437).
- `KICK-dKeptSession-2` S1's order is `(read_file_value, read_preset_value, read_default_value)`.

### The file, scaffolded under strict

```toml
preset = "strict"

[budgets]
# enforce = "refuse"  (preset strict)
pinned = []

[policy-file]
on-invalid = "last-valid"

[runtime]
agents-in-flight = 6
```

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `scaffold-preset` | fixture case | `tools/policy/check_policy.py` |

### Migration

None. A policy file already scaffolded is the repository's own and is never rewritten
(`KICK-dKeptSession-4` S3); a repository that answered strict before this unit lands runs
`policy.py preset --diff` and removes the literal it did not choose through the policy guard.

### Files touched (estimate)

- `tools/policy/policy.py`: `render_scaffold` and `cmd_scaffold`
- `tools/policy/check_policy.py`: the `scaffold-preset` case

### Alternatives rejected

- **Writing every row and letting the preset win over the file.** It inverts dGroundRules' order,
  where the file is the repository's explicit choice.
- **Writing only `never` keys.** The rows a preset leaves unassigned would vanish from the starter
  file, and an adopter could not see where their values come from.

## 5. Production-readiness checklist

- security — tightens: a strict or guarded adopter starts with its preset's refusals.
- perf / scale — one assignment lookup per row, once per scaffold.
- error / empty / loading states — an unknown preset is `KICK-dKeptSession-4` S2's refusal, raised
  before this function runs.
- observability — each left-out row is a comment naming its preset value.
- risks — a preset assigning a row dGroundRules adds later writes it as a comment, which is the
  intended posture.
- testing — the case of §6 and the arm in §7.
- migration — §4.
- user docs — `help/policy.md`'s intake paragraph (`KICK-dKeptSession-4` S5) needs no change: it
  already says the preset decides the starting posture.

## 6. Acceptance criteria

The fixture is dGroundRules' `check_policy.py --fixture`, one scratch repository per case under
`%TEMP%`.

- **AC1** — When the `scaffold-preset` case scaffolds with `--preset strict` and runs `python
  policy.py get budgets.enforce --explain`, it prints `refuse` with source `preset`.
  Red when: the scaffold writes `enforce = "warn"`, which reads `warn` with source `file`.
- **AC2** — When the same case runs `python policy.py preset --diff` for each of the four shipped
  presets, each prints `- no key differs`.
  Red when: any preset's scaffold carries a literal that differs from it.
- **AC3** — When a probe calls `render_scaffold(rows)` with no preset, it raises `TypeError`.
  Red when: a call naming no preset renders the standard file silently.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg runs the case once dGroundRules has landed it; the arm line
below declares it.

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the `scaffold-preset` case, staged red by a copy of `render_scaffold` writing every literal row · none

## 8. Open questions

- **F1 — What does the scaffold do with a row the preset assigns?** Options: (a) leave it out and
  write it as a comment naming the preset's value; (b) leave it out silently; (c) write the preset's
  value as a literal. (c) turns the preset into a frozen copy, so a later change to the shipped
  preset never reaches the adopter, and `preset --diff` stays empty only by accident. (b) meets the
  criteria and hides the posture. (a) meets AC1 and AC2 and shows it. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the skeptic's fix "write presettable keys as comments". widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H1 (id 1).

## 10. Reuse audit

The seam extended is dGroundRules' `render_scaffold` (`tools/policy/policy.py` at `3c8c4718a`, lines
1313-1324), with `KICK-dKeptSession-1`'s `derive_preset_assignment` as the one assignment and
`KICK-dKeptSession-33`'s rule for what it assigns. `python tools/codebase-map/reuse_lookup.py
"scaffold a starter policy file leaving out keys a preset assigns"` ranked `key`, `keys`,
`read_conf_key` and `load_policy` (`tools/roles/roles_lib.py`) by name stem only: the policy kit is
on `branch/unattended-dgroundrules-e47ae1`, not at this base, so no existing seam in the tree fits
and the branch's function is the one extended.

Recall terms used: `python tools/memory-recall/query.py "how does the scaffold write a policy file
under a named preset" --terms "render_scaffold scaffold preset strict budgets.enforce refuse warn
literal default intake adopt-policy"`
