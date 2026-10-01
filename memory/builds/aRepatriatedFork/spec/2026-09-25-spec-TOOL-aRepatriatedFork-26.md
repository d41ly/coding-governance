# TOOL-aRepatriatedFork-26 — the runbook and every shipped doc name no install prefix

**Status:** CLOSED · rev-4 · 2026-10-01 · node a · Tier-1 · base 2143b6d6 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-26-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-26-1-acceptance-ledger.md) | journal | — |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-26-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-26-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |

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
  `TOOL-aRepatriatedFork-23` §8 F2. (rev-3) The executing `harness-migration` block lines are
  returned, as §4 says. Observed by AC1, AC2.
- **S3** — A doc govkit writes verbatim, which is every kit README, `LEXICON.md` and
  `skills/session-kickoff/SKILL.md`, uses the `<prefix>/` prose token. Observed by AC2.
- **S4** — A doc govkit renders, the `*.template.*` files whose role is `rendered`, uses the render
  token its renderer already substitutes, so the adopter reads the real path. (rev-3) Where the
  renderer substitutes none for the path, as the lexicon Skill marker's, the file is named in
  words, as §4 says. Observed by AC3.
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
- **S9** — (rev-3) The seams these spellings are read through move with them.
  `check-playbook-parity.sh` S1 counts a kit as named when the charter or WIRE spells
  `<prefix>/<kit>/`, beside the two forms it accepts today. `check-wiring.test.sh` AC12 still
  derives both merge-driver commands in fixtures, and requires the memory-tree README to publish
  the one `<prefix>/` line that yields each when `<prefix>/` is read as `tools/` and as empty.
  The review-harness descriptor declares `TOOL_ROOT` on `drift-audit-state.template.js`, which its
  renderer already substitutes. Observed by AC6.

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

### rev-3 — what the unit pass found before code

- **One token, both sides.** The gate's drained forms are `<prefix>/` and `<tool-root>/`, and
  `TOOL-aRepatriatedFork-25` already printed gov's side as `<gov>/<prefix>/`. WIRE defines
  `<prefix>` once, in its Definitions line: the directory a tree keeps its kits in, the operator's
  choice under `<project>` and whatever gov's checkout uses under `<gov>`. `<gov-repo>` leads
  keep their lead.
- **Executing lines are returned, not drained.** WIRE's `harness-migration` blocks are cut out
  and RUN by the govkit self-test, and seven of their lines join `tools/govkit/…` under the
  operator's `$GOV`. Deriving that path changes a program whose only observer is a suite this
  pass cannot run, which is M3 veto 3. They go to `TOOL-aRepatriatedFork-46` with the other
  executing derived-base joins, so WIRE keeps a row of exactly those seven.
- **The lexicon Skill marker names its file in words.** The lexicon renderer substitutes no token
  that names its own kit directory, so S4 has no render token to reuse there. The marker says
  "this kit's `SKILL.template.md`", and the rendered Skill still names the adopter's real paths
  through `{{SUGGEST_CLI}}` and `{{GATE_CLI}}`.
- **The kickoff manifest seed has no prefix token.** `check-script:` and the standing gate line
  take `<prefix>/manifest-check.sh`, and the Customize block names `<prefix>` as the one angle
  token to fill. A `check-script:` left unfilled names no tracked file, so the engine's trust
  guard falls through to its next candidate, which is existing behaviour.
- **The charter moves, so the playbook bumps to v3.2**, with the v3.1 text cut to
  `memory/archive/` as v3.1 was, and gov's own `AGENTS.md` render follows.

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
  this unit owns, except WIRE's row, which (rev-3) counts only the `harness-migration` block lines
  §4 returns, as a per-line scan with the gate's own counter shows.
  Red when: an owned file keeps a row, or WIRE's row counts a line outside those blocks.
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
- **AC6** — (rev-3) `bash tools/check-playbook-parity.sh` exits 0 over the drained charter and WIRE,
  and exits 1 naming kits under the pre-rev-3 `named_in_playbook`. The AC12 block of
  `check-wiring.test.sh`, run as a slice with its prologue, passes against the drained README and
  fails with the README's line put back to `tools/`.
  Red when: either check keeps its verdict across the break.

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
- rev-3 · 2026-09-29 · the unit pass, before code. S9 and AC6 name the three seams that read these
  spellings and would red on the drain: the playbook parity gate's kit coverage, the check-wiring
  suite's published-command arm and the review-harness placeholder declaration. §4 pins one
  `<prefix>` token for both sides, returns WIRE's seven executing migration-block lines to
  `TOOL-aRepatriatedFork-46` under M3 veto 3 and narrows AC2 to match, and records the lexicon
  marker, the manifest seed and the charter's v3.2 bump.
- rev-4 · 2026-10-01 · S9: gate repair at VERIFYING, leg `foreign-prefix parity (every self-test at
  three prefixes)`, row `playbook parity selftest`, red at `scripts/` and `vendor/gov/`. The
  documented-kit predicate in `check-playbook-parity.sh` took a kit named only as `tools/<kit>/`,
  `<prefix>/<kit>/` or a backticked `<kit>/`, so at any other install a runbook naming its own root
  was undocumented. Its first form is the gate's own derived root; at a root install there is none.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a doc with the install prefix placeholder"`
ranked `render_map_md` and its siblings in `tools/codebase-map/map_lib.py`, which render the map
and not a kit doc. No new seam is needed: S4 reuses the render tokens each `rendered` template's
renderer already substitutes, and S3 and S5 are a spelling rule.

Recall terms used: `WIRE runbook install destination prefix README rendered engine seed token
placeholder <prefix>`.
