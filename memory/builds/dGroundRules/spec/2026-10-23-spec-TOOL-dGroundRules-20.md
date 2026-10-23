# TOOL-dGroundRules-20 — the `policy fixtures` guard covers the sibling files its cases run, and a join keeps the census's enforcers inside it

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-20-deviation-8.md](../build/2026-10-23-build-TOOL-dGroundRules-20-deviation-8.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-20-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-20-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 35 at HIGH**, item **H5**, which no other id shares. This unit is its
promotion. The guard row is `TOOL-dGroundRules-1`'s, and the cases that read past it are units 8, 9
and 10's; the guard can only be derived from those cases once they exist, so the unit repairs
`TOOL-dGroundRules-10`, the last of them, and builds at order 6.

`TOOL-dGroundRules-1` declares the `policy fixtures` leg with guard `{prefix}/policy/`. Unit 10's
`limit-hook-*` cases run `tools/hooks/agent-cap.js`; unit 9's `budgets-cap-<name>` cases run every
census enforcer across six kits; unit 8 reads the memory-tree kit's `tree_lib.py`; and every policy
module inlines `tools/lib/` blocks. No unit widens the guard, which is the recorded class
`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`: an edit to a sibling alone skips the leg
or reuses its stale green. This unit names each sibling file in the guard and adds a join that reds
when a census enforcer falls outside it.

## 2. Scope (IN)

- **S1** — The guard. The `policy fixtures` row in `tools/gate-legs.json` keeps `{prefix}/policy/`
  and gains `{prefix}/lib/`, `{prefix}/hooks/agent-cap.js`, `{prefix}/memory-tree/tree_lib.py` and
  every distinct `enforcer` of `tools/policy/caps.toml`, each spelled as that file spells it, exact
  files rather than directories. Observed by AC1, AC2.
- **S2** — The join. The case `fixtures-guard-census` in `CASES` of `tools/policy/check_policy.py`
  reads `tools/gate-legs.json` and the census in the source repository and reds each census
  enforcer the `policy fixtures` guard does not cover, by exact path or by a guard directory
  holding it. Observed by AC3.

## 3. Non-goals (OUT)

- The guard lines for `TOOL-dGroundRules-17`'s registry read and `TOOL-dGroundRules-18`'s template
  render: each of those units adds the file its own case reads, beside the case.
- Changing the leg's argv, subject or chunk.
- A join for the hook and `tree_lib.py` lines: each is one fixed file, and AC1 observes them.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the `policy fixtures` row in `tools/gate-legs.json` and the `--fixture` mode
- **consumes-from** `TOOL-dGroundRules-8` — the reader-coverage cases, which read the memory-tree kit's `tree_lib.py`
- **consumes-from** `TOOL-dGroundRules-9` — `tools/policy/caps.toml`, whose enforcers the `budgets-cap-` cases run
- **consumes-from** `TOOL-dGroundRules-10` — the `limit-hook-` cases, which run `tools/hooks/agent-cap.js`
- **hands-off** `TOOL-dGroundRules-25` — the `policy fixtures` guard and `fixtures-guard-census`, which that unit extends to the manifest, the enforcers' imports and the checker's own trip rule (findings 20, 41, 19, 33)

## 4. Design

### Evidence

- `TOOL-dGroundRules-1` §4 "The adopter": `policy fixtures` is "subject `kit` with guard
  `{prefix}/policy/`", carried by an `[[exempt_leg]]` row.
- `TOOL-dGroundRules-9` §4 Inventory lists the census's enforcers: `check-template-size.sh`,
  `check-spec-tokens.py`, `check-line-length.sh`, `memory-tree/check-memory-hygiene.sh`,
  `memory-tree/gen_build_index.py`, `roles/check_roles.py`, `roles/handoff.py`,
  `playbook/render_playbook.py`, `skills/session-kickoff/manifest-check.sh`, `memory-tree/gotchas.py`,
  `memory-recall/query.py`, and the consumer and correctness rows' enforcers, PINNED as read on
  2026-10-23; S1 derives the list from the census at build.
- Over `tools/gate-legs.json` at base, no guard names `{prefix}/hooks/agent-cap.js`,
  `{prefix}/memory-tree/tree_lib.py` or `{prefix}/check-template-size.sh`; `{prefix}/lib/` is carried
  by 36 legs. Measured on 2026-10-23 by a count of each guard over the manifest.
- `tools/check-spec-tokens.py:331` sets `BROAD_LEG_FLOOR = 5`, and the gotcha's fix prefers exact
  files so a shared guard is not tipped past it.

### The join

```text
for each distinct enforcer e of the census:
    p = e with {prefix} expanded to the source repository's tool root
    covered when some guard g of the `policy fixtures` row, expanded, equals p, or ends `/` and prefixes p
    else: finding "<e> is run by budgets-cap-<name> and is outside the policy fixtures guard"
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `fixtures-guard-census` | `CASES` entry | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/policy/check_policy.py`

### Alternatives rejected

- **Each sibling kit's directory in the guard.** Several of those directories are already carried by
  more than `BROAD_LEG_FLOOR` legs, and a directory re-runs the leg on every edit to its kit.
- **A declared tuple of every sibling read, joined to the guard.** For the fixed files it restates
  what the guard says; the census is the one population that grows, and it is already declared.

## 5. Production-readiness checklist

- security — N/A: a manifest guard and a test case.
- perf / scale — the leg re-runs on edits to the named sibling files, which is the intent.
- error / empty / loading states — a census that does not parse is the case's finding; a census with
  no rows is a finding, because a join over nothing proves nothing.
- observability — the finding names the enforcer and the case that runs it.
- risks — a new sibling read by a later case that is not a census enforcer still needs its guard
  line by hand; the gotcha names that obligation.
- testing — `fixtures-guard-census` under `--fixture`, with AC1 to AC3.
- migration — none.
- user docs — N/A: a gate manifest change.

## 6. Acceptance criteria

Every command runs from the repository root. The case spells the kit's file by bare name,
`check_policy.py`, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python tools/check-spec-tokens.py --legs-for tools/hooks/agent-cap.js
  tools/memory-tree/tree_lib.py` runs on the built tree, it names `policy fixtures` for each path.
  Red when: an edit to the hook or `tree_lib.py` alone skips the leg.
- **AC2** — When `python tools/check-spec-tokens.py --legs-for` runs over every enforcer path the
  census names, it names `policy fixtures` for each.
  Red when: a census enforcer outside the guard can change with the leg skipped.
  figure: the enforcer list is DERIVED from the census at observation.
- **AC3** — When one census enforcer is staged out of the `policy fixtures` guard in a scratch copy of
  the manifest and `python check_policy.py --fixture fixtures-guard-census` runs there, it prints
  `WRONG` naming that enforcer; restored, it does not.
  Red when: the census can gain an enforcer the guard misses unseen.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture fixtures-guard-census`) · covers AC3 · one census enforcer staged out of the guard · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 35 (HIGH, item H5) of the round-1 spec
  audit, from the review's sound fix and `tools/gate-legs.json` measured at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-25`, the reciprocal of each
  promotion of the round-1 spec audit of units 13 to 21 that repairs this unit; no scope moved.

## 10. Reuse audit

The seam extended is the `guard` field of a `tools/gate-legs.json` row, which `run-gates.sh` already
reads to hold a leg, and the gotcha's prescribed fix, exact files named in the guard.
`python tools/codebase-map/reuse_lookup.py "guard paths of a held selftest leg covering sibling kit
files"` ranked `legs`, `leg`, `kit_rel` and `resolve_kit_dir`, none of which joins a guard to the
files a suite reads, so no existing seam fits the join; the census it reads is
`TOOL-dGroundRules-9`'s. The recall probe returned `TOOL-aHeardState-6`, where the class was found,
and `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`, whose fix this follows; both agree
with source.

Recall terms used: `python tools/memory-recall/query.py "how does a guarded selftest leg cover the
sibling kit files its cases run" --terms "held suite guard sibling kit gate-legs guard stale green
leg skipped BROAD_LEG_FLOOR"`
