# DEPL-dShippedRelease-25 — the receipt's schema 5: `release`, `source_remote` and the step that raises it

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 18 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0435@e8f82801 whole
**Carries:** node:record-kind.receipt
**Carries:** node:policy-key.install.from
**Carries:** node:policy-key.install.steps

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-25-deviation-251.md](../build/2026-10-30-build-DEPL-dShippedRelease-25-deviation-251.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-25-deviation-252.md](../build/2026-10-30-build-DEPL-dShippedRelease-25-deviation-252.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

A receipt records gov's source as a local path, so an adopter cannot say where its install came from or how
far behind it sits. Schema 5 records the tag and gov's remote beside dSafePassage's `steps`, gains the
supersession fields, and ships as an upgrade step whose down restores schema 4, closing `gap-deploy-12`.

## 2. Scope (IN)

**Build-run preconditions**, each specced and unbuilt at this base: schema 4, `steps`, `read_step_states`
and the rule that only a step raises a receipt (TOOL-dSafePassage-3); `steps.toml`, the step reader and the
before-image (TOOL-dSafePassage-1); `run_step_isolated` and `derive_step_mode` (TOOL-dSafePassage-7); gov's
source-mode receipt (TOOL-dSafePassage-8); `read_shim_rows` (TOOL-dSafePassage-6); `read_python_floor`
(DEPL-dShippedRelease-10); and `read_release_tags` (DEPL-dShippedRelease-3).

- **S1** — The constant. `RECEIPT_SCHEMA = 5` at `tools/govkit/govkit.py:49`, its comment saying readers
  accept 1 to 5 and that schema 5 is reached by the step `govkit/receipt-schema-5` or by a fresh `apply` or
  `adopt`. `update`'s re-stamp stays `max(<the receipt's schema>, 3)`. The integrity message
  TOOL-dSafePassage-3 S4 already spells 3, so the comment is the one sentence left of "its messages and the
  constant's comment updated". Observed by AC1, AC2.
- **S2** — The fields, seven, written by `derive_receipt_fields(root, target, prior)` at both envelope
  writers (`tools/govkit/govkit.py:7981`, `:13030`), and by `update` on a receipt at schema 5 or above:

  | Field | Holds |
  |---|---|
  | `release` | the tag this install came from, or `null` |
  | `install_from` | `release-tag`, `any-commit` or `source`, the marker S6 grades |
  | `source_remote` | gov's remote, S4, or `null` |
  | `superseded` | one `{id, successor}` per claim `resolve_claim` carried through a succession row |
  | `deprecations` | one `{id, from, to}` per open `[[shim]]` row whose `from` this receipt lists |
  | `prior_commit` | the `gov_commit` the last `update` moved from, `null` on a fresh install |
  | `python_floor` | `read_python_floor(root)`, `tools/lib/python-floor.txt`'s value |

  `steps` stays dSafePassage's. `install_from` and `python_floor` are two fields the clause's list lacks: S6
  needs the first, and cl-dClosedLoop-0436 says the floor is recorded in the receipt, so both join here,
  deviation 251. Observed by AC1, AC3.
- **S3** — `install.from`, default `install.from: release-tag`, read by a literal
  `read_policy_value("install.from", target)`. A tag at the installed commit is `read_release_tags`' row,
  and it writes `release` and `install_from = "release-tag"` under either value. No tag at that commit,
  under `any-commit`, writes `release: null`, `install_from = "any-commit"`. No tag at that commit under
  `release-tag`, while some `gov/v*` tag exists, refuses the install naming the newest tag. While no
  `gov/v*` tag exists it writes as `any-commit` and prints `install.from — no release cut yet`, so the first
  release is not a precondition of every install (§8 F2). Observed by AC4.
- **S4** — `source_remote`, `derive_public_remote(root)`: the remote the ladder resolves (`resolve_remote`,
  `tools/govkit/govkit.py:558`) read by `git remote get-url`, kept only as `https://` or `ssh://` or
  scp-shaped, its userinfo password stripped. A filesystem path or no remote writes `null` and prints that
  no remote can be recorded. It is a value that ships into an adopter's tree, so no credential may survive
  it. Observed by AC5.
- **S5** — `gov_source` leaves the receipt. Both envelope writers stop writing the key, `source_remote`
  standing in its place. `deploy.toml`'s same-named key (`tools/govkit/govkit.py:13160`), read by
  `tools/lib/render-doc.sh:268` and its copies, is a different fact and stays. `run_fresh_target` compares
  `gov_commit` with the snapshot's HEAD in place of its path compare, since the commit is what proves which
  checkout installed the target. Observed by AC6.
  **Readers:** by name: `tools/govkit/govkit.py`, `tools/policy/check_policy.py`,
  `tools/check-install-prefix.test.sh`, `tools/govkit/fixtures/make_adopter_receipt.py`,
  `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, `tools/govkit/selftest.py` · by value:
  `run_fresh_target` in `tools/policy/check_policy.py`, which compares it with the snapshot root, the one
  value reader; the fixtures hold older receipts, and an older receipt keeps the key.
- **S6** — Receipt integrity. `check_release_field(receipt)` in the new `tools/run-gates/receipt_fields.py`
  returns the reason a schema-5 receipt fails: `install_from` outside the three, `release-tag` with no
  `release`, `release` set with any other value, or a `source_remote` that is a path or holds a password.
  `tools/run-gates/check-receipt.py` runs it and prints `FAIL`, exit 1, and `govkit check` counts it a
  problem. Below schema 5 it prints that the arm did not grade, never a pass. Observed by AC7.
- **S7** — The one reader. `read_receipt_release(receipt)` in `receipt_fields.py` returns
  `(release, source_remote, install_from)`, `(None, None, "any-commit")` below schema 5. `kits.currency`
  reads it, `kits.adopters` through `resolve_tool_path`, and `tools/run-gates/check_currency.py` beside it
  in the same kit. Observed by AC8.
- **S8** — The step `govkit/receipt-schema-5`, a row of `tools/govkit/steps.toml`, `needs-target = false`,
  `surfaces = []`, program `tools/govkit/steps/receipt_schema_5.py`, written with TOOL-dSafePassage-1's
  before-image. Its up takes a schema-4 receipt to schema 5 in one atomic write, the fields of §4 "The
  step"; its witness exits 0 at schema 5 or above with `install_from` valid; its down restores schema 4 from
  the image, byte-identical, `gov_source` back, exiting 1 while `steps` holds an `applied` row of a later
  step. A receipt below schema 4 reaches it through the walk, after `govkit/receipt-schema-4`.
  `python receipt_schema_5.py --fixture --case <name>` builds a scratch gov and target for this unit's other
  cases, each planted input its own case. Observed by AC9, AC10.
- **S9** — A source receipt. In source mode (TOOL-dSafePassage-8) the receipt writes
  `install_from = "source"`, `release: null` and `source_remote: "."`, and `gov_source` leaves it too. So
  gov's own receipt reads "source, 0 behind" without a key every other receipt has lost (§8 F4). Observed by
  AC11.
- **S10** — `install.steps`, read by a literal `read_policy_value("install.steps", target)` in
  `derive_step_modes(rows, target)` in `tools/govkit/upgrade_steps.py`. A row whose `derive_step_mode` is
  `attended` stays `attended` under every value, the owner's NP-22. Otherwise `offer` runs it unattended,
  and `attended` holds it for the adopter's own run. `kits.offer` reads this answer; the step's spawn stays
  `run_step_isolated`, the ninth kind's one site, and its `OFFER_MODE` row is DEPL-dShippedRelease-16's.
  Observed by AC12.
- **S11** — The readers by value, §4 "Inventory": each row disposed in this unit, re-derived at the build
  run's base by `git grep -n -E 'RECEIPT_SCHEMA|get\("schema"' -- tools skills .githooks`. `build_role_pair`
  (`tools/govkit/matrix.py:482`) takes this unit's fields out of a receipt it forces below schema 5, as it
  does for `steps`. Observed by AC13.
- **S12** — The keys. `install.from` and `install.steps` (`tools/policy/catalogue.toml:1052`, `:1652`) gain
  `summary` and `usage`, each name drained from `tools/policy/unsummarised-keys.txt` by
  `policy.py lists --write`, no second row added, allowed values and defaults verbatim. Observed by AC14.
- **S13** — `help/upgrade-steps.md` gains the receipt's schema-5 fields and what `install.from` does before
  a first release. NOT OBSERVED by a criterion: prose, read by the memory hygiene leg at the close.

## 3. Non-goals (OUT)

- No `kits.currency` and no adopter register: DEPL-dShippedRelease-7 reads this reader, and reads `steps`
  pending and shim calls itself. Shim calls reach gov's reading as `unread`, deviation 252.
- No mode and no `OFFER_MODE` row: DEPL-dShippedRelease-16's.
- No tag: DEPL-dShippedRelease-3's.
- No per-kit floor: one declaration, `tools/lib/python-floor.txt`.
- No change to `deploy.toml`, whose `gov_source` is answered at `intake` and read by the renderers.
- No rewrite of an old receipt fixture: a receipt below schema 5 keeps what it has, which is what they test.
- No new policy key: the marker `install_from` is a receipt field, since an adopter's check reads no policy.

### Edges

- **consumes-from** `DEPL-dShippedRelease-3` — `read_release_tags`, the tag a release-tag install names
- **consumes-from** `DEPL-dShippedRelease-10` — `read_python_floor`, the value `python_floor` records
- **hands-off** `DEPL-dShippedRelease-7` — `read_receipt_release`, the receipt's `release`, `source_remote` and `install_from`
- **hands-off** `DEPL-dShippedRelease-16` — `install.steps`, which says which pending steps its mode runs
- **hands-off** `DEPL-dShippedRelease-26` — `python_floor`, the receipt's record of the floor
- **consumes-from** external — TOOL-dSafePassage-1, -3, -6, -7 and -8, each specced and unbuilt at base `f4597719`
- **hands-off** `DEPL-dShippedRelease-61` — S3's read of `install.from`, which that unit makes a harness able to declare (review id 6)
- **hands-off** `DEPL-dShippedRelease-62` — `derive_receipt_fields`'s writers, ahead of which that unit moves S3's refusal (review id 91)
- **hands-off** `DEPL-dShippedRelease-63` — `derive_public_remote`, whose strip that unit widens (review id 46)
- **hands-off** `DEPL-dShippedRelease-64` — `check_release_field`, whose read that unit tightens (review id 92)
- **hands-off** `DEPL-dShippedRelease-78` — the empty tag list, which the minors batch repairs (review ids 93)

## 4. Design

### Evidence

- `RECEIPT_SCHEMA = 3` at `tools/govkit/govkit.py:49`; both envelopes write `gov_source: str(root)`
  (`:7981`, `:13030`). Schema 4 is unbuilt, and after TOOL-dSafePassage-3 S5 only a step raises a receipt.
- Scout D found no reader of the receipt's `gov_source`. There is one: `run_fresh_target` reads it at
  `tools/policy/check_policy.py:1249-1252` and reds on a mismatch (TOOL-dGroundRules-34 S29). Without S5's
  change the policy kit's fresh-install fixture reds on this unit's first commit.
- `check-receipt.py` reads no policy (`tools/run-gates/check-receipt.py:60-71`, `:401-456`), and no `gov/*`
  tag exists, only three `archive/*`, so a "release-tag receipt" needs a marker the receipt itself carries:
  `install_from`.
- TOOL-dSafePassage-3 S7 reads every reader that lists `files`, `kits` or `gov_commit`, and none compares
  the key set, so an added key reaches none of them.
- This repository's `origin` is an `https://` URL with no userinfo (`git remote -v`, 2026-10-30, PINNED). A
  remote naming a token is the class S4 exists for.

### The step

| Field | Up writes |
|---|---|
| `release` | the `read_release_tags` tag at `gov_commit`, else `null` |
| `install_from` | `release-tag` where a tag was found, else `any-commit` |
| `source_remote` | `derive_public_remote` at gov's checkout |
| `superseded`, `deprecations` | `[]`, since no record of an earlier carry exists |
| `prior_commit` | `null` |
| `python_floor` | `read_python_floor` at gov's checkout |

The up runs from gov's checkout, the step row's contract, so `{gov}` answers the tags and the remote, and
the receipt alone is written. `gov_source` leaves in the same write. The receipt's serialization is govkit's
`json.dumps(receipt, indent=2) + "\n"`. With no release cut, every commit-vintage receipt reads
`any-commit`, so `kits.currency` counts tags dated after the install, which is `any-commit`'s definition.

### Inventory

Minted: `derive_receipt_fields`, `derive_public_remote`, `derive_superseded`, `read_deprecations`
(`tools/govkit/govkit.py`); `read_receipt_release`, `check_release_field`
(`tools/run-gates/receipt_fields.py`); `derive_step_modes` (`tools/govkit/upgrade_steps.py`); `cmd_up`,
`cmd_down`, `cmd_witness`, `main` (`receipt_schema_5.py`); the step id `govkit/receipt-schema-5`; the
receipt keys of S2. Each `py.function`, OK from `lexicon.py --suggest` or put to it in the build pass.

The receipt's readers by value, at this base:

| Reader | What it does with the value | Disposition |
|---|---|---|
| `tools/govkit/govkit.py:49` | the constant | 5, comment re-worded (S1) |
| `tools/govkit/govkit.py:7981`, `:13030` | writes `schema` and `gov_source` | S2, S5 |
| `tools/govkit/govkit.py:8407`, `:13074` | prints the schema | unchanged |
| `tools/govkit/govkit.py:9175` | reads `schema` | unchanged |
| `tools/govkit/govkit.py:9323`, `:9330`, `:9385`, `:9388` | pinned to 3 by TOOL-dSafePassage-3 S4 | unchanged |
| `tools/govkit/govkit.py:12407` | the re-stamp | unchanged: `max(<schema>, 3)` (TOOL-dSafePassage-3) |
| `tools/govkit/matrix.py:482` | forces a schema | S11 |
| `tools/run-gates/check-receipt.py:198`, `:437` | writes a schema-3 fixture, prints the value | unchanged; S6 adds an arm |
| `tools/policy/check_policy.py:1249` | compares `gov_source` | S5 |
| `tools/govkit/census.py:138`, `tools/govkit/census.test.sh:103` | reads `gov_commit` | unchanged |
| `tools/check-install-prefix.test.sh:240` | writes a schema-2 fixture | unchanged |
| `tools/govkit/fixtures/make_adopter_receipt.py:302` | writes a schema-3 fixture | unchanged |
| the schema assertions of `tools/govkit/selftest.py` (17 `"schema"` lines at this base, DERIVED by `git grep -c`) | writes fixtures, and asserts the key set at `:12472` | S2's keys added to `:12472`; the fixtures are unchanged |

### Migration

The step of S8. An adopter on schema 3 walks `govkit/receipt-schema-4`, then this step. A receipt whose walk
stops between them reads schema 4 and every reader of S7 answers `any-commit`.

### Rollout

Live at landing. The first `apply` after a first tag is the first to refuse an untagged commit under
`release-tag`.

### Files touched (estimate)

- `tools/govkit/govkit.py`, `tools/govkit/upgrade_steps.py`, `tools/govkit/matrix.py`,
  `tools/govkit/selftest.py`
- `tools/govkit/steps.toml`, `tools/govkit/steps/receipt_schema_5.py` (new)
- `tools/run-gates/receipt_fields.py` (new), `tools/run-gates/check-receipt.py`, `tools/run-gates/kit.toml`
- `tools/policy/check_policy.py`, `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`
- `help/upgrade-steps.md`

### Alternatives rejected

- **`release-tag` refusing every install while no tag exists.** Tested by S3's first case: no `gov/v*` tag
  exists at this base, so the default would refuse every `apply` and every fixture that runs one until the
  first cut, and the first cut needs a landing record first.
- **`gov_source` kept beside `source_remote`.** The clause says "in place of", and two fields for one fact
  is `[one-fact]`. The test is a remote and a local path disagreeing in one receipt, which only the second
  reader could notice.
- **A policy read in `check-receipt.py`.** It ships with no policy reader and runs at an adopter's bar, and
  a receipt's own marker is true at install even if the key moves later.
- **The reader inline in `tools/lib/`.** It has one kit's two readers and gov's one, so `resolve_tool_path`
  serves it, and a third consumer in another shipped kit is where it would move.

## 5. Production-readiness checklist

- security: `derive_public_remote` runs at the write boundary, and S6 grades the field again at the read, so
  a credential in a URL neither lands nor passes.
- perf / scale: one `git remote get-url` and one tag list per write.
- error / empty / loading states: no remote and a path remote write `null` with a printed line; a
  below-schema receipt prints that the arm did not grade.
- observability: `receipt:` line of `check-receipt.py`, and `install.from —` lines.
- risks: a tag-less gov installs `any-commit`, so `kits.currency` counts by date until the first cut;
  `release-tag` then starts refusing untagged installs, which is the key's stated meaning and is a change an
  operator notices on the next `apply`.
- testing: a scratch gov with and without a tag, each value planted.
- migration: S8, its up and down each observed, TOOL-dSafePassage-1's frozen-row rule applying once landed.
- user docs: S13.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py apply --target <scratch>` runs from a fixture gov, the
  receipt reads `schema` 5 and holds all seven fields of S2 and no `gov_source`.
  Red when: a field is missing, or `gov_source` is still written.
- **AC2** — When a schema-4 receipt runs through `update` with no step applied, it stays at schema 4, and
  the constant's comment names `govkit/receipt-schema-5`.
  Red when: the re-stamp raises a receipt past what a step did.
- **AC3** — When `python receipt_schema_5.py --fixture --case update-fields` updates a schema-5 receipt from
  commit A to B through a planted `[[retired]]` row and an open `[[shim]]` row, `prior_commit` reads A,
  `superseded` names the row, and `deprecations` names the shim.
  Red when: `prior_commit` is the new commit, or either list stays empty.
- **AC4** — When `--case install-from` runs with a planted `.governance/policy.toml` reading
  `install.from = "release-tag"`: at a tagged commit the receipt holds `release`; at an untagged commit with
  a tag elsewhere `apply` exits 2 naming that tag; with no tag at all it writes `any-commit` and prints
  `no release cut yet`. With `install.from = "any-commit"` an untagged commit writes `release: null`.
  Red when: an untagged install under `release-tag` lands with a tag to name, or the default refuses before
  any release exists.
- **AC5** — When `python -c` calls `derive_public_remote` over a remote
  `https://user:tok@example.invalid/g`, the value holds no `tok`; over a filesystem path and over no remote
  it returns `None` and prints the line.
  Red when: a password survives, or a local path is recorded.
- **AC6** — When `python check_policy.py` runs its `fresh-target` case, the case passes on `gov_commit`
  equal to the snapshot's HEAD, and fails on a planted different commit;
  `grep -n gov_source tools/lib/render-doc.sh` still prints line 268.
  Red when: the deploy file's key is removed with the receipt's.
- **AC7** — When `python tools/run-gates/check-receipt.py <scratch>` reads a planted receipt
  `install_from = "release-tag"` with no `release`, it prints `FAIL` and exits 1; with the tag restored it
  exits 0; a schema-3 receipt prints that the arm did not grade; a `source_remote` holding a path exits 1.
  Red when: the planted release-tag receipt passes.
- **AC8** — When `python -c` calls `read_receipt_release` over a schema-5 receipt and a schema-3 one, it
  returns the three values and `(None, None, 'any-commit')`.
  Red when: a below-schema receipt raises, or reads a release it does not hold.
- **AC9** — When `python receipt_schema_5.py up <scratch>` then `witness <scratch>` run on a schema-4
  receipt, the witness exits 0 at schema 5, a second `up` changes no byte, and `gov_source` is gone.
  Red when: `up` is not idempotent, or the witness passes at schema 4.
- **AC10** — When `python receipt_schema_5.py down <scratch>` runs after AC9, the receipt equals its
  schema-4 bytes under `cmp`; with a later step's `applied` row planted it exits 1.
  Red when: the down leaves schema 5's fields, or discards a later step.
- **AC11** — When `--case source-receipt` writes gov's source-mode receipt, `install_from` reads `source`,
  `source_remote` reads `.`, and `check_release_field` passes it.
  Red when: a source receipt reads `release-tag`, or reds at integrity.
- **AC12** — When `--case step-modes` runs `derive_step_modes` over a `needs-target` row and a plain row,
  under `install.steps = "offer"` the plain row is `offer` and under `install.steps = "attended"` it is
  `attended`; the `needs-target` row is `attended` under both.
  Red when: a step needing target code runs unattended.
- **AC13** — When `git grep -n -E 'RECEIPT_SCHEMA|get\("schema"' -- tools skills .githooks` runs, each line
  is in §4's table, and `python receipt_schema_5.py --fixture --case role-pair` shows a receipt
  `build_role_pair` forces to schema 4 holding no `release` key.
  Red when: a reader of the value goes undisposed.
- **AC14** — When `python policy.py get install.from` and `python policy.py get install.steps` run with no
  file value they print `release-tag` and `offer`, and
  `grep -c -E 'install.(from|steps)' tools/policy/unsummarised-keys.txt` prints 0, the reader-coverage arm
  counting both literal calls.
  Red when: a row has no `summary`, or no literal reader.

## 7. Gates

`policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `receipt sync (installed files match the receipt)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC11 AC12 · scratch gov and target, its failing case an untagged install under `release-tag` with a tag elsewhere · none
New arm: tools/run-gates/check-receipt.py · covers AC7 AC8 · `--selftest`, a planted release-tag receipt with no `release` · none
New arm: tools/govkit/steps/receipt_schema_5.py · covers AC9 AC10 · a fixture schema-4 receipt, its failing case a down that leaves `release` · none

## 8. Open questions

- **F1 — A "release-tag receipt" has no marker.** The clause names no field for `install.from`, and
  `check-receipt.py` reads no policy. Options: (a) a new field `install_from`; (b) read the policy at the
  check; (c) infer it from `release`, which makes the red unreachable. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3, the only option leaving the clause's red observable. widens: none · relaxes: none
- **F2 — What `release-tag` does while no tag exists.** Options: (a) write `any-commit` and say so; (b)
  refuse every install until the first cut; (c) a placeholder tag. (b) fails every fresh install, and (c) is
  a tag no cut made. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, scout D fork 4.
  widens: none · relaxes: none
- **F3 — The floor has no field in the clause's list.** Scout C disagreement 11. Options: (a) `python_floor`
  in schema 5; (b) a sixth schema for it. cl-dClosedLoop-0436 requires the record, and
  DEPL-dShippedRelease-26 reads it. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3; the departure is
  deviation 251. widens: none · relaxes: none
- **F4 — What a source receipt's `source_remote` holds.** TOOL-dSafePassage-8 writes `gov_source: "."`.
  Options: (a) `"."`, the source is here; (b) the remote URL, which reads as an install of itself. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3. An ask for dSafePassage, filed by the main loop:
  TOOL-dSafePassage-8's source receipt writes `source_remote` and `install_from` from schema 5, seen as
  `python upgrade_steps.py gov-first` green over a schema-5 source receipt. widens: none · relaxes: none
- **F5 — `kits.currency` and the register "reading … shim calls".** The journal lies under the git
  directory, so a remote read never sees it (scout D disagreement 4). Options: (a) the adopter's own reading
  counts it, and gov's reads `unread`; (b) commit the journal. (b) was rejected by TOOL-dSafePassage-6 §8
  and would dirty every tree. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, DEPL-dShippedRelease-7
  S6 builds it; the departure is deviation 252. widens: none · relaxes: none
- **F6 — A `source_remote` with a credential.** Options: (a) strip the password at the write and grade it at
  the read; (b) refuse the install. (b) stops an operator whose remote URL embeds a token from installing at
  all. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, the spec run.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 61, 62, 63, 64, 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: `RECEIPT_SCHEMA` and its two writers (`tools/govkit/govkit.py:49`, `:7981`, `:13030`),
the step pattern of `govkit/receipt-schema-4` (TOOL-dSafePassage-3 S6), `tools/run-gates/check-receipt.py`,
and `resolve_remote` (`:558`).
`python tools/codebase-map/reuse_lookup.py "the install receipt schema and its readers and an upgrade step raising it"`
ranked name-stem hits only (`read`, `read_text`, `step`), so the seams come from scout D's row, verified at
source. It disagrees with source once: it found no reader of the receipt's `gov_source`, and
`tools/policy/check_policy.py:1249` is one, §4 "Evidence". Its disagreements 4, 6, 7, 8 and 9 are each acted
on here, at S7, S5, S11, S1 and S6. The recall hit on DEPL-dRetiredFork-2 predates schema 4, and its schema
statement is stale.

Recall terms used: receipt schema RECEIPT_SCHEMA upgrade-step gov_source source_remote install.from
release-tag steps superseded
