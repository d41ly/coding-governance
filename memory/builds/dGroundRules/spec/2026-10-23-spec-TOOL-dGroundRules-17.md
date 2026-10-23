# TOOL-dGroundRules-17 — the legacy-home list withheld from installs and the cap census graded by what ships, so neither arm reds an adopter

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-17-deviation-5.md](../build/2026-10-23-build-TOOL-dGroundRules-17-deviation-5.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-15 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 37 at HIGH**, which shares item **H2** with id 4
(`TOOL-dGroundRules-16`). This unit is id 37's promotion, built from the skeptic's corrected fix,
because the finder's own proposal was judged unsound. It repairs `TOOL-dGroundRules-7` and
`TOOL-dGroundRules-9`; the census half cannot exist before unit 9 builds, so it is placed after
`TOOL-dGroundRules-9`, at order 6.

Two arms in the shipped `policy check` leg hold only on gov's tree. `legacy-homes`
(`TOOL-dGroundRules-7` S5) compares `tools/policy/legacy-homes.txt`, gov's 115 measured rows, with a
derivation over the tree under test, so in an adopter every gov row reads as stale and every adopter
key as a new legacy home. `arm_cap_census` (`TOOL-dGroundRules-9` S7) joins the census to the tree
both ways, and some census enforcers are registry `[[exempt]]` paths that never reach an adopter.
This unit withholds the legacy-home list from installs, so its arm grades gov's tree alone, and
grades each census row by whether its enforcer ships.

## 2. Scope (IN)

- **S1** — The list withheld. `tools/policy/kit.toml` gains a `[[files]]` rule claiming
  `legacy-homes.txt` with `role = "project-owned"`, the mechanism `tools/runlog/kit.toml` uses for
  its suite, so no install writes it. Observed by AC1.
- **S2** — The arm where it is absent. `legacy-homes` finds no list at its own kit directory and
  prints one announce line, `policy-check: legacy-homes · not graded · the list is gov's own and is
  withheld from installs`, and reports no finding. `lists --write` updates the legacy list only
  where it exists and never creates it. Observed by AC2.
- **S3** — Gov's witness. The case `legacy-homes-present` in `CASES` asserts that the source
  repository's kit directory holds `legacy-homes.txt` and that `kit.toml` withholds it, so deleting
  the list on gov's tree, which would turn the arm into an announcement there, reds the
  `policy fixtures` leg, which is gov's alone. Observed by AC3.
- **S4** — The census field. Each `[[cap]]` row of `tools/policy/caps.toml` may carry
  `ships = false`; absent means `true`. The rows whose `enforcer` is a `{prefix}` path the registry
  exempts carry it. Observed by AC4, AC5.
- **S5** — The census arm by what ships. `arm_cap_census` locates each row's enforcer through the
  inlined `resolve_kit_dir`. A row with `ships = false` whose enforcer is absent is announced and
  not graded. A row whose enforcer's kit does not resolve is announced as that kit not installed.
  A row whose kit resolves and whose enforcer is absent is a finding, as before. Observed by AC4.
- **S6** — The registry join, gov's half. The case `budgets-ships-join` reads
  `tools/govkit/registry.toml` in the source repository and asserts that the census enforcers
  carrying `ships = false` are exactly those its `[[exempt]]` rows name, both ways. The
  `policy fixtures` guard in `tools/gate-legs.json` gains `{prefix}/govkit/registry.toml`, the file
  the case reads. Observed by AC5.

## 3. Non-goals (OUT)

- A repo-owned legacy-home list seeded by the adopter. An adopter's kit confs grow with each kit
  update gov ships, so a shrink-only list of them would red on every update (§8 F1).
- The fresh-target case that proves both arms green in an adopter: `TOOL-dGroundRules-16`'s.
- Any change to which caps are under the switch, to `budgets.py`'s verdicts, or to the legacy-home
  derivation.

### Edges

- **consumes-from** `TOOL-dGroundRules-7` — `tools/policy/legacy-homes.txt`, the `legacy-homes` arm and the `lists --write` half that writes it
- **consumes-from** `TOOL-dGroundRules-9` — `tools/policy/caps.toml`, `read_cap_census` and `arm_cap_census`
- **consumes-from** `TOOL-dGroundRules-16` — `adopter-fresh-target`, the case that reds both arms in a fresh target until this unit lands
- **hands-off** `TOOL-dGroundRules-22` — `ships`, `arm_cap_census` and its announce lines, which that unit grades by each row's `installed` destination and the install receipt (finding 10)
- **hands-off** `TOOL-dGroundRules-23` — `budgets-ships-join`, which that unit extends to each row's `installed` and `kit` (finding 38)
- **hands-off** `TOOL-dGroundRules-25` — the withheld list's plan row, its announce line, the adopter-tree announce, the real-install census case and the derived source paths (findings 3, 11, 37, 4, 33)

## 4. Design

### Evidence

- `TOOL-dGroundRules-7` S2 and §4: the list is generated into the kit directory and the arm runs
  "on the real tree by unit 1's leg"; its homes are root `.*.conf` files, `.githooks/gate-env.sh` and
  the roles house file, all read from the tree under test.
- `TOOL-dGroundRules-9` S7 joins the census "to the tree both ways"; its §4 Inventory names
  `check-template-size.sh` and `check-spec-tokens.py` as enforcers.
- `tools/govkit/registry.toml:211` and `:215` exempt `{prefix}/check-template-size.sh` and
  `{prefix}/check-spec-tokens.py`, so neither reaches an adopter.
- `tools/runlog/kit.toml:18-29` withholds a kit file by claiming it with `role = "project-owned"`,
  because govkit has no `exclude` key and `apply` never writes a project-owned file.
- The `policy fixtures` leg is gov's alone, carried by an `[[exempt_leg]]` row
  (`TOOL-dGroundRules-1` §4 "The adopter").

### The census in an adopter

| Row state in the target | Verdict |
|---|---|
| enforcer present | graded as `TOOL-dGroundRules-9` states |
| enforcer absent, `ships = false` | announced: `<name> · enforcer not shipped` |
| enforcer absent, its kit's home does not resolve | announced: `<name> · kit <home> not installed` |
| enforcer absent, its kit resolves | finding, as today |

`resolve_kit_dir(home, anchor, here)` is inlined from `tools/lib/resolve_kit_dir.py`, held by its
parity row; `home` is the enforcer's first segment below `{prefix}`, and a root-level enforcer is
located at the tool root itself.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `ships` | optional census field | `tools/policy/caps.toml` |
| `legacy-homes-present`, `budgets-ships-join` | `CASES` entries | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/policy/kit.toml`
- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/caps.toml`
- `tools/policy/budgets.py`
- `tools/policy/README.md`
- `tools/gate-legs.json`

### Alternatives rejected

- **A repo-owned list seeded by `adopt-policy.sh --scaffold`.** §8 F1.
- **The whole census arm gov-only.** An adopter whose installed enforcer goes missing would then
  never hear of it; graded by what ships, the arm keeps that finding for every kit the target has.

## 5. Production-readiness checklist

- security — N/A: no write path changes; the withheld file is data gov alone reads.
- perf / scale — one directory resolve per census row's home, cached per home.
- error / empty / loading states — an absent list or an uninstalled kit is an announce line, never
  silence; on gov's tree the absent list is a finding through S3.
- observability — each announce line names why the row or the list was not graded.
- risks — a census enforcer moved under a new home without a `ships` update; S6's join reds it on
  gov's tree.
- testing — the two cases under `--fixture`, with AC1 to AC5; `TOOL-dGroundRules-16`'s fresh target
  observes both arms in an adopter.
- migration — none: the list was never installed anywhere before this build.
- user docs — the rows for both arms in the kit README's "Each arm in an adopter" table.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py`, `policy.py`, `kit.toml` and `caps.toml` under the kit, as `TOOL-dGroundRules-5`
§6 does.

- **AC1** — When `python tools/govkit/govkit.py plan --target <t> --kits policy` runs over a scratch
  target `<t>`, the plan names no destination ending `legacy-homes.txt`.
  Red when: the list would be installed.
  fixture: the scratch target sits under `%TEMP%`, short-named; the tree holds none today.
- **AC2** — When `python check_policy.py --repo <t>` runs over a target holding the installed kit
  without the list, it prints the `legacy-homes` announce line and no finding; and
  `python policy.py lists --write` there leaves no legacy list behind.
  Red when: the arm reds every gov row as stale in an adopter, or the write seeds the list.
- **AC3** — When `legacy-homes.txt` is staged deleted from a scratch copy of the kit and
  `python check_policy.py --fixture legacy-homes-present` runs there, it prints `WRONG`; restored,
  it does not.
  Red when: gov's own list can vanish and its arm turn into an announcement unseen.
- **AC4** — When `arm_cap_census` runs over a target holding only the policy kit and the kits it
  requires, the `ships = false` rows and the rows of uninstalled kits are announced and no row is a
  finding; with one installed kit's enforcer staged absent, that row is a finding.
  Red when: an exempt enforcer reds an adopter, or a missing installed enforcer goes unseen.
- **AC5** — When `python check_policy.py --fixture budgets-ships-join` runs on the built tree, it
  passes; with `ships = false` staged off one exempt row, or onto a shipped row, it prints `WRONG`
  naming the row.
  Red when: the census's `ships` flags drift from the registry's exemptions.
  figure: the exempt rows are DERIVED from the registry at observation; two were read on 2026-10-23.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `codebase-map coverage + freshness` · `govkit selfcheck` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture legacy-homes-present budgets-ships-join`) · covers AC3 AC5 · the list staged deleted, then one census row's `ships` flag staged against the registry · none

## 8. Open questions

- **F1 — Where does the legacy-home list live for an adopter?** (a) Nowhere: the list is gov's own
  product list, withheld from installs, and its arm announces where it is absent. (b) A repo-owned
  path seeded by `adopt-policy.sh --scaffold` from the target's own homes. (c) The arm moved to a new
  gov-only leg. (b) reds an adopter on each kit update that adds a conf key, since the list only
  shrinks and an update is a new key, which fails `TOOL-dGroundRules-16` AC1 (veto 1). (c) adds a
  manifest leg no clause names (veto 2). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 37 (HIGH, item H2) of the round-1 spec
  audit, from the skeptic's corrected fix and the registry and runlog descriptor read at base
  `3708a705`.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-22`, `TOOL-dGroundRules-23`,
  `TOOL-dGroundRules-25`, the reciprocal of each promotion of the round-1 spec audit of units 13 to
  21 that repairs this unit; no scope moved.

## 10. Reuse audit

The seams extended are govkit's `project-owned` file role, which `tools/runlog/kit.toml:18-29` uses
to withhold a kit file, the registry's `[[exempt]]` rows, which the census join reads rather than
restates, and the inlined `resolve_kit_dir`. `python tools/codebase-map/reuse_lookup.py "withhold a
kit file from adopters as project-owned"` ranked `adopt`, `kit_rel`, `resolve_kit_dir` and `kit_dir`;
none withholds a file, which was found by reading the runlog descriptor, so the probe's answer and
the source disagree only in that the probe is blind to descriptor rules. The recall probe returned
`TOOL-aScouredKit-11` and `TOOL-dLoggedFlight-1`, which withhold gov-only files from installs; they
agree with this design.

Recall terms used: `python tools/memory-recall/query.py "how is a gov-only data file withheld from
adopters" --terms "project-owned withheld registry exempt gov-specific install day red shrink-only
list"`
