# TOOL-dGroundRules-9 — one switch over every size cap, each cap's value through the policy reader

**Status:** DEFERRED · rev-4 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0015@8ce57bfb whole

**Carries:** node:policy-key.budgets.*

**Carries:** node:policy-key.budgets.enforce

**Carries:** node:policy-key.budgets.pinned

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-9-deviation-54.md](../build/2026-10-23-build-TOOL-dGroundRules-9-deviation-54.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

Eighteen of the 24 size caps the caps research lists refuse a commit, a push or a render, each in
its own way, and a refusal has bought raises rather than trims: one ceiling moved 26 times in 17 days
(gap-tool-24; `research-caps.md` §1 and §2). This unit gives every gate that enforces a size cap on a
document or record one switch to read, `budgets.enforce`, warning by default as the owner set it, with
`budgets.pinned` naming caps that refuse whatever the switch says. Each cap's value is read under
`budgets.*` through the policy reader, `template-size-limits.txt` kept as a legacy home that reader
reads, and a limit its consumer enforces by dropping what is over, or a check of correctness, stays
outside the switch.

## 2. Scope (IN)

- **S1** — The cap census, `tools/policy/caps.toml`: one `[[cap]]` table per cap the caps research
  lists, with `name` (the key under `budgets.*`), `class` (`switch`, `consumer`, `correctness` or
  `exempt`), `unit` (`bytes`, `lines`, `chars` or `count`), `enforcer` (a `{prefix}`-relative path as
  `tools/gate-legs.json` spells one), `home` (where the value is declared today, in one of the four
  forms §4 Data model gives), `family` (true where the value is per subject) and `research` (the
  caps research's row number). A cap whose home is a row of `template-size-limits.txt` is named by
  that row's key, the measured file's repo-relative path or the class label, which is the spelling
  TOOL-dGroundRules-6's admitted raise reads (§8 F7). Its rows are §4 Inventory's table. Observed by
  AC7.
- **S2** — The budgets module, `tools/policy/budgets.py`, the policy reader's half for caps:
  - `read_cap_census(repo=".")` parses S1;
  - `resolve_caps(requests, repo=".", rev=None)` answers, per requested cap, a `CapAnswer`
    `(value, mode, source, reason)`: the value is the policy file's `budgets.<cap>` when it sets one,
    else the cap's legacy home, read by this module for a `limits` home and handed in by the enforcer
    for the other three forms; `mode` is `refuse` when the cap is in `budgets.pinned` or
    `budgets.enforce` resolves `refuse`, and `warn` otherwise; all of it read through
    `policy.resolve` at the one revision `rev` names (§8 F5);
  - `check_cap(answer, measured)` returns a `CapVerdict` `(over, refuse, line)`;
  - a CLI, `python tools/policy/budgets.py resolve <cap>[=legacy:<n>|=default:<n>] ...`, printing one
    tab-separated row `<cap> <value> <mode> <source>` per cap, and `python tools/policy/budgets.py
    check <cap>[=…] <measured>`, printing the verdict line and exiting 0 when under or warned, 1
    when refused; a refusal exits 2 as `policy: refused · <path>:<line> · <why>`.
  Observed by AC3, AC8, AC10.
- **S3** — The two-homes rule. A cap whose policy file value and legacy-home value are both present
  refuses at resolution, exit 2, as `policy: refused · <home path>:<line> · budgets.<cap> is held in
  both homes`. A `default` handed in is a code constant and not a home: a policy value overrides it.
  Observed by AC3.
- **S4** — The schema rule, `check_budgets(doc)` in `budgets.py`, returning the brief's `Problem`
  list, called from `validate` (TOOL-dGroundRules-4) for the `[budgets]` table: a `budgets.pinned`
  name whose census class is `consumer` or `correctness` (outside the switch) or `exempt`, or that
  names no census row, is refused on its line; so is a `budgets.<cap>` naming no census row, one on a
  `family` cap, or one that is not a positive integer. Observed by AC1.
- **S5** — The enforcers re-pointed. Each `switch` row's enforcer asks S2 once per run for its caps,
  handing in its legacy value, and on a subject over its cap prints a `BUDGET WARN` line and passes
  under `warn`, and refuses as it does today, the line naming `budgets.enforce` or `budgets.pinned`,
  under `refuse`. §4 The enforcers lists each one's change. The two readers of
  `template-size-limits.txt`, `check-template-size.sh` and `check-spec-tokens.py`'s size join, stop
  parsing it: `budgets.py` is its one reader. Observed by AC2, AC4, AC5, AC9.
  **Readers:**
  by name: `tools/check-template-size.sh`, `tools/check-spec-tokens.py`,
  `tools/check-template-size.test.sh`, `tools/check-spec-tokens.test.sh`.
  by value: the same four; `check-template-size.sh`'s positional limit, its `MAX_BYTES` environment
  read and its `LIMITS` path override retire with its own parse of the file.
- **S6** — The outside classes untouched. Each `consumer` and `correctness` row's enforcer reads no
  switch, and its answer is the same under each value; `CODEX_MAX` in
  `tools/agent-instructions/adopt-agent-instructions.sh` is today's consumer limit. The correctness
  failures inside a switch enforcer stay refusing under `warn`: `check-template-size.sh`'s checks 3, 5
  and 6, and `check-spec-tokens.py`'s non-numeric-row refusal. Observed by AC6, AC11.
- **S7** — The arms. Two repository arms in `ARMS` of `tools/policy/check_policy.py`:
  `arm_limits_readers`, finding each tracked script outside `tools/policy/` and outside a self-test
  that spells `template-size-limits.txt` on a line that is not a comment, and `arm_cap_census`, joining
  the census to the tree both ways. Cases in `CASES` whose names open `budgets-`, one
  `budgets-cap-<name>` per census row among them. Observed by AC1 to AC7, AC9 to AC11.
- **S8** — `help/size-caps.md`, new, listed in `help/README.md`. Observed by AC12.

## 3. Non-goals (OUT)

- Moving `template-size-limits.txt`'s rows, or any other legacy home's value, into the key, and its
  four raise conditions into the key's declaration: dSafePassage's step. No cap's value moves in this
  unit, so gov's policy file sets no `budgets.<cap>`.
- Raising a cap through the guarded policy command (dDeclaredLoop) or the minimal guard's one admitted
  write shape (TOOL-dGroundRules-6). A class row, a lowering, a new row and a removal stay the owner's.
- Showing a warning on a passing run and attributing it to a unit (dWitnessedBar), pricing breaches
  and re-deriving values (dCalibratedLens), and the load set's and composition's refusals
  (dOrderedCharter).
- Memory slices, which `memory.over-budget` answers (dTotalRecall): no census row exists for them.
- The catalogue rows for `budgets.*`, `budgets.enforce` and `budgets.pinned`: TOOL-dGroundRules-1.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the `policy` kit, `tools/policy/check_policy.py` with `ARMS`, `CASES` and its `--fixture` mode, and the catalogue rows for `budgets.enforce` (warn by default), `budgets.pinned` (none by default) and `budgets.*`; without them the switch has no default
- **consumes-from** `TOOL-dGroundRules-2` — `policy.resolve` at the landed revision and its blob reader, which S2 calls for the file layer and for the limits home
- **consumes-from** `TOOL-dGroundRules-3` — a `budgets.<cap>` the file does not set resolving with source `default`, which S2 reads as "no file value"
- **consumes-from** `TOOL-dGroundRules-4` — `validate` and its `Problem`, which S4 extends with one call
- **consumes-from** `TOOL-dGroundRules-6` — the spelling its admitted raise reads, a measured-file cap being a leaf under `budgets` named by the measured file's repo-relative path, which S1 adopts for every `limits` row
- **hands-off** external — dSafePassage: the step that moves each legacy home's rows under `budgets.*` with their argued history and the four raise conditions
- **hands-off** external — dWitnessedBar, dCalibratedLens and dOrderedCharter: a warning that reaches a reader, the pricing and re-derivation of values, and the load-set and composition refusals
- **hands-off** `TOOL-dGroundRules-17` — the census's `ships` field and `arm_cap_census` graded by what ships (finding 37)
- **hands-off** `TOOL-dGroundRules-20` — every census enforcer named in the `policy fixtures` guard, and the join that keeps them there (finding 35)
- **hands-off** `TOOL-dGroundRules-21` — 0 as unchecked, the read-shape limits scanner, the refused-reader rule, `read_blob_at` and the regenerated codebase map (findings 8, 18, 36, 44, 10, 40)
- **hands-off** `TOOL-dGroundRules-34` — `budgets-census-join` and the census-to-tree join of S7, which that unit keeps live under `unadopted` (id 24 of the round-1 spec audit of units 26 to 32)
- **hands-off** `TOOL-dGroundRules-62` — S2's read of an unset `budgets.<cap>`, which that unit routes through `resolve_caps` catching `DerivedDefault` as no file value, the answer this unit's edge from unit 3 expects (id 8 of the spec run's closing diff review)

## 4. Design

One module answers every cap, so the switch, the pins and the two-homes rule live once; each
enforcer keeps measuring what it measures today and asks only what its cap is and whether a breach
refuses. The census is the population, so "every cap" is a join over data and never a list typed in
an arm.

### Data model

The four `home` forms in `caps.toml`:

| Form | Meaning | Who reads the value |
|---|---|---|
| `limits:<row key>` | a row of `{prefix}/template-size-limits.txt` | `budgets.py`, the file's one reader |
| `file:<path>:<row key>` | a row of another declared limits file | the enforcer, handed in as `legacy:` |
| `conf:<path>:<KEY>` | a key of a kit conf, falling back to the enforcer's constant | the enforcer: `legacy:` when the conf sets it, `default:` when not |
| `constant:<path>:<NAME>` | a code constant | the enforcer, handed in as `default:` |

In `.governance/policy.toml` a cap is a key of the `[budgets]` table, quoted where it carries a `/`,
`.` or `*`: `"AGENTS.md" = 20480`, `guide-bytes = 98304`. `budgets.pinned` lists the same names. A
`family` cap is one name over per-subject values (line lengths, README slots, role bodies): the
enforcer asks only its mode, and the policy file may not set its value. A value of 0 keeps meaning
unchecked, as each enforcer reads it today. Class `exempt` has no row today; it exists because the
schema must refuse a pinned exempt name, and a case plants one.

### Inventory

The census, verified against source on 2026-10-23 (a value below is PINNED at that date; the cases
read the live one):

| `name` | class | enforcer | home | today | row |
|---|---|---|---|---|---|
| `coding-governance-agents.template.md` | switch | `check-template-size.sh` | `limits:` its key | 49152 | 1 |
| `AGENTS.md` | switch | same | `limits:` its key | 20480 | 2 |
| `skills/session-kickoff/SKILL.md` | switch | same | `limits:` its key | 18432 | 3 |
| `memory/guides/BUILD-METHOD.md` | switch | same | `limits:` its key | 30720 | 4 |
| `memory/guides/UNATTENDED-PROTOCOL.md` | switch | same | `limits:` its key | 66860 | 5 |
| `.claude/skills/unattended/SKILL.md` | switch | same | `limits:` its key | 10240 | 6 |
| `memory/builds/*/spec/` | switch | `check-spec-tokens.py` | `limits:` its key, a class row | 49152 | 7 |
| `line-length` | switch, family | `check-line-length.sh` | `file:line-length-limits.txt`, `HARD_DEFAULT` | 450 | 8 |
| `guide-bytes`, `guide-lines` | switch | `memory-tree/check-memory-hygiene.sh` | `conf:.memory-tree.conf:GUIDE_CAP_*` | 98304, 1200 | 9 |
| `index-bytes`, `index-lines` | switch | same | `conf:.memory-tree.conf:INDEX_CAP_*` | 61440, 0 | 10 |
| `readme-bytes`, `readme-lines` | switch | same | `conf:.memory-tree.conf:BUILD_README_CAP_*` | 25600, 0 | 11 |
| `dossier-bytes`, `dossier-lines` | switch | same | `conf:.memory-tree.conf:DOSSIER_CAP_*` | 20480, 0 | 12 |
| `entry-chars`, `readme-entry-chars` | switch | same | `conf:.memory-tree.conf:ENTRY_CAP_CHARS`, `…BUILD_README_ENTRY_CAP_CHARS` | 300, 350 | 13 |
| `readme-slot` | switch, family | `memory-tree/gen_build_index.py` | `file:memory-tree/build-readme-slot-limits.txt` | 500 to 1800 | 14 |
| `role-body` | switch, family | `roles/check_roles.py` | `constant:roles/check_roles.py:BODY_CEILINGS` | 1536 to 4096 | 15 |
| `one-line-rule` | switch | `playbook/render_playbook.py` | `constant:…:ONE_LINE_MAX` | 200 | 16 |
| `roster-line` | switch | `roles/handoff.py` | `constant:…:ROSTER_LINE_MAX` | 200 | 17 |
| `manifest-bytes` | switch | `skills/session-kickoff/manifest-check.sh` | `constant:…:MAX_MANIFEST_BYTES` | 25600 | 18 |
| `manifest-line`, `manifest-trap` | switch | same | `constant:…` (checks 8 and 11) | 400, 400 | 18 |
| `universal-gotchas` | switch | `memory-tree/gotchas.py` | `conf:.memory-tree.conf:UNIVERSAL_BUDGET` | 6 | 20 |
| `recall-export` | switch | `memory-recall/query.py` | `constant:…:EXPORT_CAP` | 20480 | 22 |
| `orientation-card` | consumer | `skills/session-kickoff/manifest-check.sh` | `constant:…:CARD_CAP_BYTES` | 8192 | 19 |
| `cited-file-cap` | correctness | `memory-tree/corpus_ids.py` | `conf:.memory-tree.conf:READ_PATH_WAIVER` | — | 21 |
| `codex-instructions` | consumer | `agent-instructions/adopt-agent-instructions.sh` | `constant:…:CODEX_MAX` | 32768 | 23 |
| `runlog-record` | consumer | `runlog/record.py` | `constant:…:RECORD_CAP_BYTES` | 24576 | 24 |
| `feature-card` | consumer | `codebase-map/map_lib.py` | `constant:…:FEATURE_CARD_CAP_BYTES` | 1024 | 24 |
| `hook-context` | consumer | `hooks/scratch-guard.js` | `constant:…:ROUTE_CONTEXT_CAP` | 10000 | 24 |

Enforcer paths are under `{prefix}` except `skills/session-kickoff/`. Minted names, each answered OK by
`python tools/lexicon/lexicon.py --suggest` on 2026-10-23: `read_cap_census`, `resolve_caps`,
`check_cap`, `check_budgets` (py.function); `Cap`, `CapAnswer`, `CapVerdict` (py.type). Also minted:
`arm_limits_readers` and `arm_cap_census` in `ARMS`; the cases `budgets-pinned-outside`,
`budgets-pinned-exempt`, `budgets-pinned-unknown`, `budgets-family-value`, `budgets-pinned-warn`,
`budgets-two-homes`, `budgets-limits-reader`, `budgets-census-join`, `budgets-switch-refuse`,
`budgets-no-kit`, `budgets-correctness-kept` and one `budgets-cap-<name>` per census row in `CASES`.

### The enforcers

| Enforcer | Its change |
|---|---|
| `tools/check-template-size.sh` | maps its subject's repo-relative key to a census `limits:` row and asks `budgets.py check`; check 2 (over) obeys the verdict; checks 3, 5 and 6 still refuse; a subject with no row keeps the 49152 default as `default:`; positional `$2`, `MAX_BYTES` and `$4` retire |
| `tools/check-spec-tokens.py` | `read_size_ceilings` takes the class row's value from `resolve_caps`; `scan_spec_sizes` hits and the held-spec growth hit carry the verdict, a warned hit printed and not counted |
| `tools/check-line-length.sh` | asks the `line-length` mode once; a line over its row warns or refuses |
| `tools/memory-tree/check-memory-hygiene.sh` | asks the ten check 6 and 7 caps once, handing in each conf or constant value; curation-debt exemption unchanged |
| `tools/memory-tree/gen_build_index.py` | asks the `readme-slot` mode; a slot over its ceiling warns or raises `Problem` |
| `tools/roles/check_roles.py` | R5's over-ceiling defect becomes a warning under `warn`; R5's other defects stay |
| `tools/playbook/render_playbook.py`, `tools/roles/handoff.py` | a rule or roster line over 200 renders with a warning under `warn` |
| `skills/session-kickoff/manifest-check.sh` | checks 7, 8 and 11 obey their verdicts; the card's check stays as it is (§8 F3) |
| `tools/memory-tree/gotchas.py` | check 19's universal-record count warns or refuses |
| `tools/memory-recall/query.py` | an export over `EXPORT_CAP` writes with a warning under `warn` |

Each copy-installed enforcer locates the policy kit with the sibling-kit resolver its kit already
inlines, or inlines `resolve_kit_dir` from `tools/lib/` as that file's parity table requires. With no
policy kit installed every cap refuses over, as today, and the enforcer says so once (§8 F4). Each kit
whose shipped bytes move bumps its version marker.

### Migration

None for values: every cap keeps the value its home holds. The behaviour change is the default: with
gov's policy file at the catalogue default, every `switch` cap warns rather than refuses from landing.
An adopter gets the same on installing the policy kit, and today's refusals without it.

### Rollout

Live at landing. An owner who wants a cap to keep refusing names it in `budgets.pinned`.

### Files touched (estimate)

`tools/policy/budgets.py` · `tools/policy/caps.toml` · `tools/policy/policy.py` ·
`tools/policy/check_policy.py` · `tools/check-template-size.sh` · `tools/check-template-size.test.sh` ·
`tools/template-size-limits.txt` · `tools/check-spec-tokens.py` · `tools/check-spec-tokens.test.sh` ·
`tools/check-line-length.sh` · `tools/check-line-length.test.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/gen_build_index.py` ·
`tools/memory-tree/gotchas.py` · `tools/roles/check_roles.py` · `tools/roles/handoff.py` ·
`tools/playbook/render_playbook.py` · `skills/session-kickoff/manifest-check.sh` ·
`tools/memory-recall/query.py` · `help/size-caps.md` · `help/README.md`

`tools/template-size-limits.txt` changes only its RESOLUTION paragraph, which names the policy
reader as its reader. Each enforcer's own suite changes where it set a limit through a retired channel.

### Alternatives rejected

- **The caps research's pick, a third outside class for limits that define a format.** The night
  pass two's point 5 departs from it: line and entry lengths are size caps, under the switch.
- **One switch over everything, correctness included.** `research-caps.md` test A2: a correctness
  check is no cap.
- **The census in `catalogue.toml`.** §8 F6.

## 5. Production-readiness checklist

- security — no new write path. The default loosens enforcement: a breach no longer blocks a commit
  or a push unless pinned, which is the owner's stated direction (v2:1347), and the policy file that
  holds the switch is guarded by TOOL-dGroundRules-6.
- perf / scale — one Python start per enforcer run, never per measured file; check 6's single awk
  pass is kept, fed the answered values.
- error / empty / loading states — an absent policy file reads the catalogue default `warn`; an
  absent policy kit refuses as today; an unknown cap, a family value and a two-homes cap refuse, exit
  2, naming the line.
- observability — every warned breach prints `BUDGET WARN — <cap> · <subject> · <measured> <unit>
  over <value>`; `budgets.py resolve` names each value's source.
- risks — `research-caps.md` test A1: a warning in a passing leg reaches nobody until dWitnessedBar.
  The limits home is read at the landed revision (§8 F5), so under `refuse` or a pin a raise lands
  before the growth it funds.
- testing — AC1 to AC11 by fixture and probe; the `New arm:` lines under §7.
- migration — §4 Migration.
- user docs — `help/size-caps.md`: the switch, the pins, which caps sit outside and why, and where
  each cap's value is declared today.

## 6. Acceptance criteria

- **AC1** — When the `--fixture` run of `python check_policy.py` reaches
  `budgets-pinned-outside`, `budgets-pinned-exempt`, `budgets-pinned-unknown` and
  `budgets-family-value`, planting under `[budgets]` a `pinned` naming `codex-instructions`, a census
  row of class `exempt` that `pinned` names, a `pinned` naming `no-such-cap`, and `role-body = 9000`,
  `validate` returns a `Problem` on each planted line naming the cap and the reason.
  Red when: `check_budgets` is not called from `validate` and the file validates.
- **AC2** — When the run reaches `budgets-pinned-warn`, which sets `enforce = "warn"` and
  `pinned = ["AGENTS.md"]` and plants a fixture `AGENTS.md` over its row, `bash
  tools/check-template-size.sh AGENTS.md` exits 1 and its line names `budgets.pinned`; with the pin
  removed it exits 0 printing `BUDGET WARN`.
  Red when: the pin is ignored under `warn`.
- **AC3** — When the run reaches `budgets-two-homes`, which plants `"AGENTS.md" = 30000` under
  `[budgets]` while the `AGENTS.md` row stands, `python budgets.py resolve AGENTS.md`
  exits 2 printing `policy: refused · tools/template-size-limits.txt:<line> · budgets.AGENTS.md is
  held in both homes`; with the row removed it prints `30000` with source `file`.
  Red when: either home silently wins.
- **AC4** — When the run reaches `budgets-limits-reader`, which removes the `AGENTS.md` row, sets the
  cap under the key, and plants a script outside `tools/policy/` reading `template-size-limits.txt`,
  `arm_limits_readers` is red naming the script; over this repository at the unit's commit
  `python check_policy.py` reports it green, `budgets.py` being the file's one reader.
  Red when: `check-template-size.sh` or `check-spec-tokens.py` still parses the file.
- **AC5** — When the run reaches each `budgets-cap-<name>` case of a `switch` row of
  `caps.toml`, its subject planted over its cap, the enforcer exits 0 printing
  `BUDGET WARN` under `warn` and refuses under `refuse`, one line per cap and value.
  Red when: any enforcer refuses under `warn` or passes under `refuse`.
  figure: the case count is DERIVED from the census at observation time.
- **AC6** — When the run reaches each `budgets-cap-<name>` case of a `consumer` or `correctness`
  row, the enforcer's exit and output are the same under each value; for `codex-instructions` a
  fixture canonical of 32769 bytes gets the same over-`CODEX_MAX` announcement from
  `bash tools/agent-instructions/adopt-agent-instructions.sh` under `warn` and `refuse`.
  Red when: an outside enforcer reads the switch.
- **AC7** — When the run reaches `budgets-census-join`, a planted request for `no-such-cap` in an
  enforcer and a planted census row with no case each turn `arm_cap_census` red; over this repository
  `python check_policy.py` reports it green, every census row having a case and an
  enforcer that names it in a `budgets.py` call or a `resolve_caps` request.
  Red when: either direction of the join is unchecked and a plant passes.
- **AC8** — When `python budgets.py resolve memory/guides/BUILD-METHOD.md
  'memory/builds/*/spec/'` runs over this repository at the unit's commit, it prints each value its
  `template-size-limits.txt` row holds, mode `warn`, source `default`.
  Red when: a value differs from its row, or the mode reads `refuse` with no pin and the default switch.
  figure: the values are DERIVED from the rows at observation time.
- **AC9** — When the run reaches `budgets-no-kit`, which runs
  `bash skills/session-kickoff/manifest-check.sh` over a manifest planted over `manifest-bytes` in a
  fixture holding no policy kit, it refuses as today and prints once that the policy kit is absent.
  Red when: an absent kit reads as `warn`.
- **AC10** — When the run reaches `budgets-switch-refuse`, which sets `enforce = "refuse"`,
  `python budgets.py check AGENTS.md 999999` exits 1 and its line names
  `budgets.enforce`; at `warn` it exits 0.
  Red when: `check_cap` ignores the switch.
- **AC11** — When the run reaches `budgets-correctness-kept`, which plants under `warn` a
  `BUILD-METHOD.md` whose `**Budget:` line disagrees with its row,
  `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exits 6.
  Red when: a correctness check was moved under the switch.
- **AC12** — When `grep -n "budgets.enforce\|budgets.pinned\|caps.toml" size-caps.md` runs, it
  prints at least one line for each, and `help/README.md` links the page.
  Red when: the page is absent or names none of them.

## 7. Gates

`line-length gate selftest` · `manifest-check self-test` · `scratch-guard self-test` · `memory-hygiene self-test` · `build-index selftest` · `tier2-review self-test` · `lexicon naming predicates` · `govkit acceptance matrix` · `playbook render selftest` · `template size <=48KiB` · `charter size` · `build-method size` · `unattended protocol size` · `unattended skill size` · `kickoff engine size <=18KiB` · `template size gate selftest` · `line length` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory hygiene` · `roles catalogue` · `kit version markers`

New arm: tools/policy/check_policy.py · covers AC4 AC7 · `arm_limits_readers` and `arm_cap_census` over the repository, in the `policy check` leg TOOL-dGroundRules-1 declares, staged by a planted reader of the limits file and a planted unknown cap request · none
New arm: tools/policy/check_policy.py --fixture · covers AC1 AC2 AC3 AC5 AC6 AC9 AC10 AC11 · the `budgets-` cases in `CASES`, each planted in the temporary repository, the census cases run under both switch values, in the `policy fixtures` leg · none
New arm: tools/check-template-size.test.sh · covers AC2 AC11 · its fixtures re-pointed from the retired positional limit and `MAX_BYTES` to a fixture policy file, a warned breach and a pinned refusal staged in a scratch repository · none
New arm: tools/check-spec-tokens.test.sh · covers AC5 · the size join's fixtures under `warn` and `refuse`, a spec planted over the class row · none

AC8 and AC12 are probes the close reads directly.

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n "OPEN · SPECCED" memory/HYGIENE.md` prints the seven tokens a spec header reuses (line
  105). Liveness: the line would print `DRAFT` if the vocabulary declared it. Observed 2026-10-23:
  it does not. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, which TEMPLATE-SPEC gives as drafting.
- **F2 — Which legacy homes does the reader itself read?** (a) Every one: `budgets.py` parses the
  three limits files and the kit confs, and every code constant moves into the census as its
  default, deleted from its enforcer; eight kits then cannot run without the policy kit, and the
  census copies sixteen constants until each is deleted. (b) `template-size-limits.txt`, the home the
  clause names, read by `budgets.py` alone; every other enforcer hands in the value its own home holds,
  so the switch, the pins, the two-homes rule and the policy file's override live once and no kit
  needs the policy kit to run. (c) The two readers the clause names, the switch read nowhere else,
  which fails the clause's every-cap case (veto 1). (a) and (b) both meet every case the clause
  states; tie-break, fewer open questions and reuse of each enforcer's existing read: (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F3 — Is the orientation card's 8192 bytes a size cap under the switch, or a consumer's limit?**
  `research-caps.md` §6 keeps it outside, as a consumer limit beside the harness's 10000-character
  hook context, which drops what is over it; the night pass two's point 5 names only that context and
  Codex's 32 KiB. (a) Outside, class `consumer`: the card keeps refusing at 8192. (b) Under the switch:
  a card between 8192 and 10000 bytes is written under `warn`, and above 10000 the harness drops text
  with nothing checking it, so (b) needs a new consumer check at 10000 that no clause states.
  Recommendation (a), which loosens nothing and adds no check; rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — What does a switch enforcer do where the policy kit is not installed?** (a) Refuse over its
  cap, as today, saying once why. (b) Refuse to run, a red on every adopter until it installs the kit.
  (c) Warn, the catalogue default, read with no reader. (c) reads a policy no reader resolved, against
  the clause's "through the policy reader" (veto 1); (b) reds every adopter that has not installed a
  kit nothing yet requires. Recommendation (a); rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F5 — At which revision does `budgets.py` read `template-size-limits.txt`?** (a) The landed
  revision, as the reader reads everything (clause 0008, the brief's S4); under `refuse` or a pin a
  raise then lands before the growth it funds. (b) The working tree, today's behaviour, so a raise
  takes effect in the commit that needs it, against clause 0008's "never from the working tree"
  (veto 1). Recommendation (a); rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F6 — Where does the cap census live?** (a) `tools/policy/caps.toml`, beside the catalogue whose
  one `budgets.*` row it enumerates. (b) One catalogue row per cap in `tools/policy/catalogue.toml`,
  TOOL-dGroundRules-1's file, whose rows the brief's S3 fixes as v2's `[policies]` table, where
  `budgets.*` is one row; the census's `class`, `enforcer`, `home` and `family` fields are not
  catalogue fields. Recommendation (a), which changes no shared interface; rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — How is a measured-file cap named under `budgets.*`?** TOOL-dGroundRules-6 §8 F5 settled
  that its admitted raise reads a leaf under `budgets` whose last segment is a file tracked at HEAD,
  and hands that spelling to this unit. (a) By its row key in `template-size-limits.txt`, the
  repo-relative path, so the guard, the legacy home and the census share one key and a class label
  such as `memory/builds/*/spec/` is no tracked file and is never admitted as a raise. (b) By a
  descriptive name such as `agents-md`, which the guard would never see as a measured file, so the
  one admitted write shape could raise nothing (veto 1 against clause 0012's admitted raise).
  Recommendation (a); rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-17, TOOL-dGroundRules-20, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-4 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-62 added, the reciprocal of that unit's **consumes-from** line: the promotion of the spec run's closing diff review's id 8 (item H4), which repairs this unit's S2 read of an unset cap. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "read a declared size ceiling for a measured file and
refuse or warn when over it"` ranked name-stem matches (`read`, `read_conf`, `read_conf_key`), none a
size-cap reader. Read against source: `template-size-limits.txt` has two parsers today, an `awk` in
`tools/check-template-size.sh` and `read_size_ceilings` in `tools/check-spec-tokens.py:1248-1276`, whose
docstring says it parses "the way check-template-size.sh parses them"; this unit makes `budgets.py`
the one parser and both callers of it. No existing module answers a mode for a cap: each switch
enforcer in §4 Inventory hard-codes its refusal, so no existing seam fits the switch, and the shared
core is new. The file layer is `policy.resolve` (TOOL-dGroundRules-2), extended rather than parsed
again. Recall hit [2] (`2026-08-24-review-TOOL-dFramedEntrypoint-1-claim-verification.md:190`)
describes `check-template-size.sh`'s resolution as positional, declaration, environment, default,
which matches source at `tools/check-template-size.sh:100`; hit [4] is the caps research this unit's
census copies. The research's enforcer line numbers were re-read: `check-memory-hygiene.sh` declares
its caps at `:137-158`, not `:133-154`, and `EXPORT_CAP` is spelled `20_480` at `query.py:177`.

Recall terms used: `python tools/memory-recall/query.py "where are the document size caps declared and
which gates refuse a file over its cap" --terms "template-size-limits check-template-size ceiling
high-water ratchet size join spec ceiling curation-debt guide cap warn refuse"`
