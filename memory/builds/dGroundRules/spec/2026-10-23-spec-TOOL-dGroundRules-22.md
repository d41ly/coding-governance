# TOOL-dGroundRules-22 — each census row names where its kit installs the enforcer, and the census arm grades an adopter there

**Status:** DEFERRED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-22-deviation-10.md](../build/2026-10-23-build-TOOL-dGroundRules-22-deviation-10.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-22-deviation-68.md](../build/2026-10-23-build-TOOL-dGroundRules-22-deviation-68.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-22-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-22-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-24 TOOL-dGroundRules-23 TOOL-dGroundRules-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 13 to 21
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md`)
exited CONVERGED with finding **id 10 at HIGH**, which shares item **H1** with id 38
(`TOOL-dGroundRules-23`). This unit is id 10's promotion, built from the skeptics' corrected fix,
because the finder's proposal was judged unsound. It repairs `TOOL-dGroundRules-17`, which sits at
order 6, so it builds at order 7.

`TOOL-dGroundRules-17` §4 locates a census enforcer at "the enforcer's first segment below
`{prefix}`", and a root-level enforcer "at the tool root itself". Two census enforcers do not fit.
`check-line-length.sh` sits at the tool root and ships only through the conditional
`check-line-length` entry, so its home always resolves and an adopter without that entry reads a
finding. `skills/session-kickoff/manifest-check.sh` sits outside `{prefix}`, and the default
`kickoff-manifest` entry installs it at `{prefix}/manifest-check.sh`, a place the rule never names.
This unit gives each shipped census row the destination and the entry that install it, and grades an
adopter at that destination, reading the target's install receipt and never the registry.

## 2. Scope (IN)

- **S1** — The row fields. Each `[[cap]]` row of `tools/policy/caps.toml` whose `ships` is true
  carries `kit`, the registry entry id that installs its enforcer, and `installed`, the
  `{prefix}`-spelled destination that entry writes the enforcer to. The `manifest-bytes` row carries
  `kit = "kickoff-manifest"` and `installed = "{prefix}/manifest-check.sh"`; the `line-length` row
  carries `kit = "check-line-length"` and `installed = "{prefix}/check-line-length.sh"`. A
  `ships = false` row carries neither. `read_cap_census` in `tools/policy/budgets.py` refuses a
  shipped row missing either field, and a `ships = false` row carrying one, naming the row.
  Observed by AC1.
- **S2** — Which tree. `derive_census_tree(repo)` in `tools/policy/check_policy.py` answers
  `source` when the tree under test holds no `.governance/install.json`, and `adopter` with the
  parsed receipt when it holds one. A receipt that does not parse is a finding naming it, never a
  `source` answer. Observed by AC2.
- **S3** — The census arm by tree. `arm_cap_census` grades as §4 "The census by tree" states: on the
  source tree every row at its `enforcer` path, an absent enforcer a finding; in an adopter a
  `ships = false` row announced as `TOOL-dGroundRules-17` announces it, a row whose `kit` the
  receipt's `kits` list lacks announced as `<name> · kit <kit> not installed`, and every other row
  graded at `installed` with `{prefix}` spelled as the receipt's `prefix`. The home-segment rule of
  `TOOL-dGroundRules-17` §4 is not consulted. Observed by AC2, AC3, AC4.
- **S4** — The case `census-adopter-receipt` in `CASES` of `tools/policy/check_policy.py`. In its
  temporary repository it plants a receipt whose `kits` names `policy`, `memory-tree` and
  `kickoff-manifest` and not `check-line-length`, places each named kit's census enforcers at their
  `installed` paths, and holds no `{prefix}/govkit/` directory. Observed by AC3, AC4.
- **S5** — The written scope. The `arm_cap_census` row of the kit README's "Each arm in an adopter"
  table (`TOOL-dGroundRules-16` S2) states the receipt rule and the two announce lines.
  Observed by AC5.

## 3. Non-goals (OUT)

- The join holding `installed` and `kit` to the registry's claims, which is gov-side:
  `TOOL-dGroundRules-23`, id 38's promotion, which shares item H1.
- A real install of the registry's entries into a fresh target, observed through `govkit.py apply`:
  finding id 4's item in `TOOL-dGroundRules-25`.
- Reading `tools/govkit/registry.toml` at runtime. `tools/govkit/registry.toml:296` exempts
  `{prefix}/govkit`, so an adopter has no registry to read.
- Any change to which caps the census holds, to `ships`, or to `budgets.py`'s verdicts.

### Edges

- **consumes-from** `TOOL-dGroundRules-17` — `ships`, `arm_cap_census` graded by what ships, its `ships = false` announce line and the README table row, which this unit re-locates
- **hands-off** `TOOL-dGroundRules-23` — the `installed` and `kit` fields, which that unit's registry join holds equal to each entry's resolved writes
- **hands-off** `TOOL-dGroundRules-25` — `derive_census_tree` and the adopter grading, which that unit's legacy-home announce (finding 37) and real-install case (finding 4) read
- **hands-off** `TOOL-dGroundRules-29` — `derive_census_tree`'s no-receipt answer, which that unit splits into `source` and `unadopted` by the registry only gov's tree holds (finding 17)
- **hands-off** `TOOL-dGroundRules-32` — `derive_census_tree`'s receipt read, which that unit gives a required shape and an `invalid` answer (finding 25)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `TOOL-dGroundRules-17` §4 "The census in an adopter": "`home` is the enforcer's first segment
  below `{prefix}`, and a root-level enforcer is located at the tool root itself".
- `tools/govkit/entries/check-line-length.kit.toml:16-17` declare `home = "."` and
  `selectable = "conditional"`; the registry's default selection (`tools/govkit/registry.toml:38-53`)
  does not name it.
- `tools/govkit/entries/kickoff-manifest.kit.toml:6` homes the entry at `skills/session-kickoff`, and
  `:17` installs the engine `to = "{prefix}/manifest-check.sh"`.
- `apply` writes the receipt with `"prefix"` and `"kits"` (`tools/govkit/govkit.py:7980-7983`), and
  each engine row with `path`, `kit` and `source` (`:7893-7895`).
- `tools/run-gates/check-receipt.py:38-41`: "gov's own tree holds no receipt", and a tree with no
  receipt is read as one that adopted nothing.

### The census by tree

| Tree | Row | Verdict |
|---|---|---|
| `source` | enforcer present at `enforcer` | graded as `TOOL-dGroundRules-9` states |
| `source` | enforcer absent | finding |
| `adopter` | `ships = false` | announced: `<name> · enforcer not shipped` |
| `adopter` | `kit` not in the receipt's `kits` | announced: `<name> · kit <kit> not installed` |
| `adopter` | `kit` in `kits`, file at `installed` | graded as `TOOL-dGroundRules-9` states |
| `adopter` | `kit` in `kits`, no file at `installed` | finding naming `installed` |

`installed` expands `{prefix}` to the receipt's `prefix` and resolves against the target's top level.
On the source tree `ships` is not read, so a gov enforcer that goes missing stays a finding.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `installed`, `kit` | census fields | `tools/policy/caps.toml` |
| `derive_census_tree` | py.function | `tools/policy/check_policy.py` |
| `census-adopter-receipt` | `CASES` entry | `tools/policy/check_policy.py` |

`derive_census_tree` leads with `derive`: `lexicon.py --suggest` answered OK for it under
`py.function` on 2026-10-23.

### Files touched (estimate)

- `tools/policy/caps.toml`
- `tools/policy/budgets.py`
- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The home-segment rule with a special case per shape.** Each new flat or out-of-prefix entry
  would need another case; the destination is a fact the descriptor already states once.
- **Read the registry at runtime.** No adopter holds one (§3).
- **Match receipt rows by their `source` suffix.** A row's `source` is spelled under gov's own tool
  root, which an adopter does not know, so the suffix would be a guessed prefix.

## 5. Production-readiness checklist

- security — N/A: the arm reads two files the target holds and writes nothing.
- perf / scale — one receipt parse per run; one `stat` per census row.
- error / empty / loading states — an unparseable receipt is a finding; an uninstalled kit is an
  announce line naming it, never silence.
- observability — each announce line names the row and the entry or the reason it was not graded.
- risks — a census row whose `installed` drifts from its descriptor reads a wrong place;
  `TOOL-dGroundRules-23`'s join reds that on gov's tree.
- testing — `census-adopter-receipt` under `--fixture`, with AC1 to AC5.
- migration — `caps.toml` gains two fields on every shipped row in this unit's commit.
- user docs — the kit README's "Each arm in an adopter" row, S5.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py`, `caps.toml` and `README.md` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `installed` is staged off the `manifest-bytes` row of `caps.toml` in a scratch copy
  of the kit and `python check_policy.py` runs there, `arm_cap_census` prints a finding naming
  `manifest-bytes` and `installed`.
  Red when: a shipped row with no destination is graded somewhere the arm guessed.
- **AC2** — When `python check_policy.py` runs over this repository, `arm_cap_census` prints no
  `not installed` and no `not shipped` line; and over a scratch target whose receipt
  `install.json` holds `{`, it prints a finding naming the receipt.
  Red when: gov's own tree is read as an adopter, or a broken receipt reads as gov's tree.
- **AC3** — When `python check_policy.py --fixture census-adopter-receipt` runs, `arm_cap_census`
  prints `line-length · kit check-line-length not installed`, grades the `manifest-bytes` row at
  `manifest-check.sh` under the planted tool root, and reports no finding.
  Red when: an adopter without the conditional entry reds, or the manifest rows go ungraded.
- **AC4** — When the same case deletes the planted `manifest-check.sh` and runs again, it prints a
  finding naming `manifest-bytes` and the `installed` path; restored, it does not.
  Red when: an installed kit's missing enforcer goes unseen in an adopter.
- **AC5** — When `grep -n "install.json" README.md` runs under the kit, it prints the
  `arm_cap_census` row of the "Each arm in an adopter" table.
  Red when: the written scope still describes the home-segment rule.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture census-adopter-receipt`) · covers AC3 AC4 · the planted `manifest-check.sh` deleted, then `derive_census_tree` staged to answer `source` always · none

## 8. Open questions

- **F1 — How does the census arm tell an adopter from gov's own tree?** (a) The presence of
  `.governance/install.json`, whose `kits` and `prefix` the arm then reads. (b) The presence of
  `{prefix}/govkit/registry.toml`, a file only gov holds. (c) A flag on `check_policy.py`. (c) adds a
  public flag no clause names (veto 2). (b) still needs the receipt for `kits` and `prefix`, so two
  files answer one question. (a) is the discriminator `tools/run-gates/check-receipt.py:38-41`
  already states, and one file answers all three facts. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 10 (HIGH, item H1) of the round-1 spec
  audit of units 13 to 21, from the skeptics' corrected fix and the entry descriptors, the registry
  and `govkit.py`'s receipt writer read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-29, TOOL-dGroundRules-32 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 22 to 25 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §1 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.
- rev-4 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-17`'s `arm_cap_census` and `ships` field, which gain two
row fields instead of a second arm, and the install receipt govkit already writes, read with the
no-receipt rule `tools/run-gates/check-receipt.py:38-41` states. `python
tools/codebase-map/reuse_lookup.py "locate an installed kit file in an adopter from its install
receipt"` ranked `adopt`, `kit_rel`, `resolve_kit_dir` and `kit_dir`; `resolve_kit_dir`
(`tools/lib/resolve_kit_dir.py`) joins a receipt row on `<home>/<anchor>`, which cannot name a
root-level enforcer whose home is gov's own tool root, so it is not reused here. The recall probe
returned this audit's H1, the dClosedLoop distribution research noting that gov's tree holds no
receipt, and `TOOL-aClassedKnob-3`, which reads an adopter's vendored engine against its receipt;
all three agree with source and with this design.

Recall terms used: `python tools/memory-recall/query.py "how does an arm tell an adopter install from
the source tree" --terms "install receipt install.json adopter source tree census enforcer
destination registry exempt conditional kit"`
