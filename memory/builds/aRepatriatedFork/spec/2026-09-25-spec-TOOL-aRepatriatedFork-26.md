# TOOL-aRepatriatedFork-26 — the runbook and every shipped doc name no install prefix

**Status:** SPECCED · rev-2 · 2026-09-25 · node a · Tier-1 · base 2143b6d6 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-26-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-26-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`WIRE-INTO-PROJECT.md` prescribes where an operator puts each kit, and it prescribes `tools/`. Kit
READMEs, skills and seeded templates repeat gov's prefix in every command they show. The runbook
is the highest-leverage member of the population: a spelling there becomes an install in every
repo that follows it. This unit spells every kit path in a shipped or gov-side doc in a form correct
at any prefix, chosen by the doc's role.

## 2. Scope (IN)

- **S1** — WIRE's install destinations, `<project>/tools/<kit>` in each `cp` step, name the prefix
  the operator chose, as §8 F1 resolves. There are 19 of them. Observed by AC1.
- **S2** — Every other kit path in WIRE, the `contribute` verb's among them, is spelled with the
  `<prefix>/` prose token. A `<gov>/tools/…` or `<gov-repo>/tools/…` spelling follows
  `TOOL-aRepatriatedFork-23` §8 F2. Observed by AC1, AC2.
- **S3** — A doc govkit writes verbatim, which is every kit README, `LEXICON.md` and
  `skills/session-kickoff/SKILL.md`, uses the `<prefix>/` prose token. Observed by AC2.
- **S4** — A doc govkit renders, the `*.template.*` files whose role is `rendered`, uses the render
  token its renderer already substitutes, so the adopter reads the real path. Observed by AC3.
- **S5** — A seeded doc, which is the charter template, `MANIFEST-TEMPLATE.md` and
  `drift_signals.template.py`, uses the token its adopter substitutes at seed time where one exists,
  and the `<prefix>/` prose token where none does. `drift-audit-state.template.js`'s commented
  example value follows S4. Observed by AC3.
- **S6** — `skills/deploy-governance/SKILL.md`, which no descriptor resolves, spells its seven
  govkit invocations the way S2 spells WIRE's. Observed by AC2.
- **S7** — The waived line `tools/memory-tree/README.md:117` and the marked line
  `.codebase-map.conf.example:28`, arm 1's two class-C lines, follow S3 and S4. Their waiver row is
  struck. Observed by AC4.
- **S8** — The ledger rows for these files are lowered, and every kit moved takes its version bump in
  every carrier. Observed by AC5.

## 3. Non-goals (OUT)

- Changing a doc's role. A README moving from `engine` to `rendered` is a receipt `role-moved` row
  at every adopter, which §8 F2 weighs.
- Fixture records shaped like docs, such as the two unattended `fixture-records` files.
  `TOOL-aRepatriatedFork-28` owns them.
- Doc content beyond the path spelling.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger, which counts the 19 `/`-led
  destinations, and the `<gov>/tools/…` ruling of its §8 F2.

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed). PINNED,
measured 2026-09-25.

- Census §4 lists 112 class-C literals over 18 files, 52 of them in WIRE. WIRE also carries 19
  `<project>/tools/…` destinations and 17 `<gov>/tools/…` spellings that no arm counts, and one
  class-F literal at `:1028`, the `contribute` verb.
- The ownership rule (the census record's section 7) gives this unit 194 literals over 21 files: 115 counted
  today, 72 invisible and 7 in `skills/deploy-governance/SKILL.md`, which no descriptor resolves.
  WIRE holds 112 of them; `tools/lexicon/README.md` 10; `tools/memory-recall/README.md` 8;
  `tools/drift-audit/README.md` and `skills/deploy-governance/SKILL.md` 7 each;
  `skills/session-kickoff/SKILL.md` 6.
- `govkit shipped` gives every kit README, `LEXICON.md` and the kickoff `SKILL.md` role `engine`,
  so they land byte for byte. The `SKILL.template.md` files and the workflow templates are
  `rendered`. The charter template, `MANIFEST-TEMPLATE.md` and `drift_signals.template.py` are
  `seed` (the census record).
- `apply` substitutes into no engine body (census §6), which is why S3 cannot use `{prefix}`.

### Ownership rule

This unit owns every literal in a `.md` file, in WIRE, and in a file census class C names, except
the fixture records `TOOL-aRepatriatedFork-28` owns. The rule is `TOOL-aRepatriatedFork-23` §8 F3's.

### Files touched (estimate)

`WIRE-INTO-PROJECT.md` · `coding-governance-agents.template.md` · `skills/session-kickoff/SKILL.md` ·
`skills/session-kickoff/MANIFEST-TEMPLATE.md` · `skills/deploy-governance/SKILL.md` · the READMEs
of eleven kits under `tools/` · `tools/lexicon/LEXICON.md` · `tools/lexicon/SKILL.template.md` ·
`tools/drift-audit/drift_signals.template.py` · `tools/workflows/drift-audit-state.template.js` ·
`tools/codebase-map/.codebase-map.conf.example` · `tools/install-prefix-waivers.txt` ·
`tools/install-prefix-carried.txt`

### Alternatives rejected

- `{prefix}` in a verbatim README. It would reach the adopter unrendered.
- Deleting the manual `cp` steps from WIRE in favour of govkit alone. That changes the runbook's
  supported install paths, which is a deployer decision outside this build.

## 5. Production-readiness checklist

- security — none; prose.
- perf / scale — none.
- error / empty / loading states — a render token with no value is refused by the renderer that
  owns it, which is existing behaviour.
- observability — none.
- risks — the charter template is size-gated at 48 KiB. A token is no longer than the prefix it
  replaces, which AC5's size leg confirms. The memory-tree README's published driver command is
  derived and required by the check-wiring suite's AC12 arms, which `TOOL-aRepatriatedFork-24` S5
  already re-derives; the two move together.
- testing — the playbook parity and kit/dogfood doc parity legs compare rendered copies.
- migration — none. An adopter's copy of a verbatim README updates on the next `govkit update`.
- user docs — this unit is the user docs.

## 6. Acceptance criteria

- **AC1** — When `git grep -nE '<project>/tools/' -- WIRE-INTO-PROJECT.md` runs, it finds nothing, and every `cp`
  step names the prefix the §8 F1 ruling gives.
  Red when: a destination still prescribes `tools/`.
- **AC2** — When `bash tools/check-install-prefix.sh --list` runs, no ledger row remains for any file
  this unit owns.
  Red when: an owned file keeps a row.
  figure: DERIVED at observation time.
- **AC3** — When `python tools/govkit/govkit.py apply` writes a fixture target at prefix `scripts`,
  every rendered doc and every seeded doc this unit touched names `scripts/` paths, and
  `git grep -n 'tools/'` over those written files finds none.
  Red when: a rendered or seeded doc reaches the target with gov's prefix or an unrendered token.
- **AC4** — Red-first control: the same `apply` from `2143b6d6` writes `tools/` paths into those
  docs. Recorded in the acceptance ledger.
  Red when: the old apply already writes derived paths, so AC3 proves nothing.
- **AC5** — `bash tools/check-kit-versions.sh` exits 0, `python tools/govkit/govkit.py epoch --base
  2143b6d6` names no kit this unit moved, and `bash tools/check-template-size.sh` exits 0.
  Red when: a moved kit's carrier was missed, or the charter template grew past its cap.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit runbook parity` · `template size <=48KiB` · `playbook parity` · `kit/dogfood doc parity` · `line length` · `dead-path carriers (deleted files still named)` · `lexicon wiring` · `memory-recall skill wiring` · `drift-audit wiring` · `kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `drift-audit selftest` · `lexicon naming predicates` · `lexicon selftest`

## 8. Open questions

- **F1 — what does WIRE's install step name as the destination?** Option (a): `<project>/<prefix>/<kit>`,
  with one sentence saying the operator chooses `<prefix>` and govkit's `--prefix` takes the same
  value. Option (b): keep a concrete default, `<project>/tools/<kit>`, stated as a default. It is
  still a hard-coded prefix under the owner's ruling. Option (c): drop the manual steps and
  prescribe `govkit intake`/`apply` only, which is §3's rejected alternative. Recommendation: (a).
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F2 — should kit READMEs become `rendered`, so an adopter reads real paths?** Option (a): keep
  role `engine` and use the `<prefix>/` prose token. Option (b): make them `rendered`, so each lands
  with the adopter's real prefix. Every adopter's receipt then carries a `role-moved` row per
  README, which `DEPL-aRepatriatedFork-17` resolves at `update`. Recommendation: (a) now. (b) is a
  deployer change of its own, and the token is correct if less convenient.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: drain every hard-coded kit
  prefix, with no class exempted, before `TOOL-aRepatriatedFork-18`'s held leg. This unit is census
  class C, WIRE's destinations first as census §6 recommends.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a doc with the install prefix placeholder"`
ranked `render_map_md` and its siblings in `tools/codebase-map/map_lib.py`, which render the map
and not a kit doc. No new seam is needed: S4 reuses the render tokens each `rendered` template's
renderer already substitutes, and S3 and S5 are a spelling rule.

Recall terms used: `WIRE runbook install destination prefix README rendered engine seed token
placeholder <prefix>`.
