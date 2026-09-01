---
slug: dGaugedVintage
node: d
opened: 2026-09-01
status: OPEN
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

Node `d` · opened 2026-09-01 · streams deployer.

This build authors no product change. It answers one question the owner asked of an inbound
document: **are there fixes in it that would simplify updating or adopting this repo's kits?**

**Yes — seven, and five were not previously recorded.** None of them is the fix the document
proposes. The document's own headline findings mostly refute against this tree; the real defects sit
one layer down, in what an adopter actually RECEIVES and what they can read a version out of once
they have it. The largest is a default kit that lands no working program.

## The inbound document

inCMS — a hand-forked adopter carrying gov kits at a `scripts/` prefix with no `.governance/`
receipt — audited its own adoption on 2026-09-01, against this repo at `d65da7ab`. `aFerriedDossier`
carried its first dossier in on 2026-08-16; this is its second.

**The document itself is deliberately NOT carried into this tree.** It cites 43 rooted-looking
paths, and 34 of them name files that do not exist here — the adopter's own `scripts/` layout, plus
`.claude/` and `memory/` paths from its tree. `DEAD_PATH_PIN` is `0` and check 15 demands set
equality against an empty registry, so carrying the file in would red the bar or cost 34 waiver rows
for citations that are correct in the repo that wrote them. What is durable about it is the triage
below, which cites this tree instead. Its own location is in this build's landing commit.

## What the document got wrong about this tree

Each row was checked by reading the named file here, not by reasoning about the claim.

| The document says | Measured here |
|---|---|
| `adopt-memory-recall.sh` / `adopt-drift-audit.sh` are dead pointers | Both are tracked, and both land: their kits' `[[files]]` rule is `include = "**"`, role engine |
| `push-main.sh` hardcodes `origin/HEAD` and would brick a non-`origin` lander | `tools/push-main.sh:20` reads `GOV_DEFAULT_BRANCH` first, then falls back, then fails CLOSED naming both escapes |
| The gov-commit column is a stale batch anchor | It grades `.governance/install.index` — a file gov never writes. Gov's receipt is `install.json`; `install.index` is the fork's own, and gov carries a fixture modelling it |
| So per-file update distance is underivable | Each row carries its own `commit` and `gov_oid` (`tools/govkit/govkit.py:4095`), advanced only on rows actually written (`:5741`, `:5859`, `:5975`) |
| Nothing answers "am I on the latest gov?" | `govkit adopt` measures a receiptless tree against gov history; `coverage_rows()` at `:2051` joins planned writes against what the target holds |
| `SKILL.template.md` is carried for two kits and not the other two | All four ship it AND declare it here. That split is the fork's |
| memory-tree is unpinnable without a cross-repo probe | Gov ships the marker in three rendered docs and the fork carries one of them |

The document marked its own `push-main` claim unverified, and it is among these. Its "what nothing
here measured" section is honest and worth trusting on that point.

## The seven that are real

Two were already known to this repo in another form; five were not recorded anywhere.

- **`DEPL-dGaugedVintage-3` — `memory-recall` lands no working program.** It is a registry DEFAULT
  (`registry.toml:36`). Its `query.py` and `extract.py` are declared `role = "forked"`
  (`kit.toml:77-79`), and `LANDABLE_ROLES` is `("engine", "seed")` (`govkit.py:236`), so `apply`
  never writes them — while `SKILL.template.md` is `rendered` and the Skill it produces tells the
  agent to run the CLI that did not arrive. The role is CORRECT for an adopter who owns those bytes
  already, which is why it exists; nothing distinguishes that adopter from a fresh target.
- **`DEPL-dGaugedVintage-4` — drift-audit ships three version values at once.**
  `adopt-drift-audit.sh:4` says `@1.2`; `drift_report.py:4`, `drift_signals.py:3`,
  `drift_signals.template.py:3` and `selftest.py:4` say `@1.4`; the README and both workflow
  harnesses say `@1.8`, which is the constant. `check-kit-versions.sh` asserts three of those eight
  sites, so five stale markers ship green. The document blamed the fork for a version split it
  inherited from here by copy.
- **`DEPL-dGaugedVintage-5` — four of fifteen versioned entries ship no marker at all.**
  check-wiring, codebase-map, kickoff-manifest and playbook-render carry zero `gov:kit` tokens
  anywhere. `check-kit-versions.sh:84` calls the marker the thing "a deployer reads a kit's version
  [from] in an adopting tree"; for these four that read returns nothing.
- **`DEPL-dGaugedVintage-6` — the drift-audit install block contradicts itself.**
  `README.md:67-69` copies the kit to the ROOT prefix and then invokes it at the `tools/` prefix.
  Every later step agrees with the second spelling, so the copy line is the wrong one.
- **`DEPL-dGaugedVintage-7` — the prefix ratchet counts lines, not literals.**
  `check-install-prefix.sh:217-223` uses `grep -c`, which counts hit LINES. A second root-prefix
  literal on a line that already carries one, or one kit's path swapped for another's, keeps the
  count and passes.
- **`DEPL-dGaugedVintage-1` — `selfcheck` never checks that a version constant ships.** Check 5
  (`govkit.py:1047`) asserts the `version_from` file EXISTS in gov and matches exactly one line, not
  that it is inside that entry's own installed population. Latent: every kit's include covers its
  own version file today, checked one by one. The break was staged into
  `entries/check-wiring.kit.toml` and selfcheck still exited 0.
- **`DEPL-dGaugedVintage-2` — a stale row, and a block behind it.** `DEPL-aFerriedDossier-1` says a
  hand fork gets no update path; its declared closer `DEPL-dCarriedReceipt-13` has a spec reading
  CLOSED rev-8 and the code is in the tree. But that closer's own row still reads SPECCED, as do
  `DEPL-dCarriedReceipt-1` through `-15`. Flipping fifteen statuses across a build this session did
  not build is a sweep with its own judgement calls, so it is filed rather than done here.

## Already recorded — do not re-file

Seven of the document's implications map onto live rows: `TOOL-aFlaggedScaffold-3` (`update` cannot
land a newly-shipped source; and no verb lands bytes without running `[adopt]`),
`DEPL-aFerriedDossier-1`, `TOOL-aScouredKit-26` (no cross-entry destination token),
`TOOL-aBoundedVerdict-29` (two gates disagree on a marker population — though it enumerates five
drift-audit sites and there are eight), `DEPL-dCarriedReceipt-15` (root-prefix literals in kit
bodies) and `TOOL-aPacedTurnstile-11` (an entry spelling another entry's command with no hard
dependency).

## The fact worth more than any single row

The adopter ran a five-investigator manual audit to hand-derive per-file distance from gov.
`govkit adopt` shipped 2026-08-26 and does that by measuring the tree against gov's own history;
`WIRE-INTO-PROJECT.md` §5b is a top-level section titled for exactly this situation. Gov even ships
`tools/govkit/fixtures/make_incms_receipt.py`, a fixture built from inCMS's own `install.index`.

The verb, the runbook section and a fixture for this tree all existed, and the path from "I have
hand-forked kits and want to update them" to §5b still did not carry. This build does not guess at
the fix, because the adopter is the only one who can say what they reached for first.

## How much of this is verified

Five parallel lenses measured against this tree; four returned. Every finding above was then
re-verified by the orchestrator reading the cited file. The **skeptic pass did not run** — the
staleness-probe lens was still out when the build landed, so nothing here has been adversarially
refuted, and the confidence is "two independent readings" rather than "survived refutation". The
`memory-recall` rule-precedence question in `-3` was read from the descriptor and its comment, not
driven through `resolve_entry` by the orchestrator.

## Non-goals

No change to `govkit.py`, to any `kit.toml`, to the runbook, or to a gate leg. No fix for any of the
seven — each is a follow-up unit, and the two that want new assertions owe a failing case observed
before they land.

<!-- roster:units -->

*No unit is planned under this build; its output is seven backlog rows and the triage above.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 0 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
