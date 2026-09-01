---
slug: dGaugedVintage
node: d
opened: 2026-09-01
status: OPEN
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

Node `d` · opened 2026-09-01 · streams deployer.

This build authors no product change. It answers one question the owner asked of an inbound
document: **are there fixes in it that would simplify updating or adopting this repo's kits?**

**Yes — eleven, nine of them previously unrecorded.** Almost none is the fix the document proposes.
Its own headline claims mostly refute here; the real defects sit one layer below, in what an adopter
RECEIVES, what they can read a version out of, and what the update path silently declines to grade.

**The one that matters most is `DEPL-dGaugedVintage-8`.** The mechanical update path this document
was written in the absence of already exists, already runs against this adopter, and leaves 47 of
its 95 receipt rows with no verdict at all — permanently, and drifting further every run. That is
the reason a five-lens manual audit happened, and it is a one-branch fix.

## The inbound document, and a premise everyone had wrong

inCMS carries gov kits at a `scripts/` prefix. The document describes it as a hand fork "with no
`.governance/` receipt", `aFerriedDossier` recorded the same thing in August, and this build's first
commit repeated it. **It is false today.** `C:/projects/incms/main/.governance/install.json` is a
genuine govkit receipt: `schema 3`, `gov_source` this repo, `gov_commit 14e21399`, `prefix scripts`,
14 kits, 95 file rows. `govkit update --target <incms>` runs read-only against it and returns a
per-file report. The adopter did adopt; the probe does work.

What it does not do is grade half the tree. Of those 95 rows, **47 carry `evidence: unattributed`**,
and those rows never reach `classify_row` at all.

**The document itself is deliberately NOT carried into this tree.** It cites 43 rooted-looking
paths, 34 of which name files absent here. `DEAD_PATH_PIN` is `0` and check 15 demands set equality
against an empty registry, so carrying it in would red the bar or cost 34 waiver rows for citations
that are correct in the repo that wrote them. Its location is in this build's landing commit.

## What the document got wrong about this tree

Each row was checked by reading the named file here, not by reasoning about the claim.

| The document says | Measured here |
|---|---|
| inCMS is a hand fork with no govkit receipt | It carries a schema-3 receipt at `gov_commit 14e21399`, 14 kits, 95 rows |
| `adopt-memory-recall.sh` / `adopt-drift-audit.sh` are dead pointers | Both are tracked, and both land: their kits' `[[files]]` rule is `include = "**"`, role engine |
| `push-main.sh` hardcodes `origin/HEAD` and would brick a non-`origin` lander | `tools/push-main.sh:20` reads `GOV_DEFAULT_BRANCH` first, then falls back, then fails CLOSED naming both escapes |
| The gov-commit column is a stale batch anchor | It grades `install.index`, a file gov never writes. Gov's receipt is `install.json`, and each row carries its own `commit` and `gov_oid` |
| Nothing answers "am I on the latest gov?" | `govkit update --target` does, read-only, today — see `-8` for what it withholds |
| `SKILL.template.md` is carried for two kits and not the other two | All four ship it AND declare it here. That split is the fork's |
| memory-tree is unpinnable without a cross-repo probe | Gov ships the marker in three rendered docs and the fork carries one |

## The eleven that are real

Ordered by what they cost an adopter.

- **`-8` — half the receipt is never graded, and the anchor moves anyway.** `update` short-circuits
  any row whose evidence is `unattributed` (`govkit.py:5529`): it tallies, prints, and `continue`s
  before `classify_row`. Meanwhile `--write` re-stamps `receipt["gov_commit"] = to_commit` (`:6204`)
  regardless. So rows that were attributable at the receipt's own vintage stay ungraded forever and
  get further from any base that could attribute them. 47 of 95 rows on this adopter.
- **`-3` — `memory-recall` lands no working program.** A registry DEFAULT (`registry.toml:36`) whose
  `query.py` is `role = "forked"` (`kit.toml:77`), which `LANDABLE_ROLES` excludes (`govkit.py:236`).
  `apply` writes no CLI while `SKILL.template.md` renders a Skill telling the agent to run it. The
  role is right for an adopter who owns those bytes; nothing distinguishes a fresh target.
- **`-4` — drift-audit ships three version values at once.** `adopt-drift-audit.sh` says `@1.2`;
  `drift_report.py`, `drift_signals.py`, `drift_signals.template.py` and `selftest.py` say `@1.4`;
  the README and both harnesses say `@1.8`, the constant. `check-kit-versions.sh` asserts three of
  those eight sites. The document blamed the fork for a split it inherited from here by copy.
- **`-9` — no verb reports a per-kit version delta.** The receipt stores each row's kit version
  string and nothing in gov reads it back; `entry_version` (`:333`) resolves gov's own constant.
- **`-10` — nothing asserts the gov checkout is current with its remote.** The only vintage guards
  are ancestry and reachability (`:3769`), so `update --to HEAD` on a stale gov clone reports
  `current` for every row gov has since moved. A green that means the measurer was behind.
- **`-5` — four of fifteen versioned entries ship no marker at all.** check-wiring, codebase-map,
  kickoff-manifest, playbook-render carry zero `gov:kit` tokens. `check-kit-versions.sh:84` calls the
  marker the thing a deployer reads a version from in an adopting tree.
- **`-11` — the `relocate` rung goes quiet on fan-out.** `derive_carry_map` (`:4840`) drops any gov
  directory fanning into more than one target directory — every kit shipping a rendered SKILL.md
  beside its engine files. Seven kits on this adopter.
- **`-1` — `selfcheck` never checks that a version constant ships.** Check 5 (`:1047`) asserts the
  `version_from` file exists in gov and matches one line, not that it is in that entry's installed
  population. Latent today; the staged break in `entries/check-wiring.kit.toml` still exited 0.
- **`-7` — the prefix ratchet counts lines, not literals.** `check-install-prefix.sh` uses `grep -c`,
  so a second root-prefix literal on a line that already carries one keeps the count.
- **`-6` — drift-audit's install block contradicts itself**, copying to the ROOT prefix then
  invoking at `tools/`. Every later step agrees with the second spelling.
- **`-2` — a stale row, and a block behind it.** `DEPL-aFerriedDossier-1`'s declared closer
  `DEPL-dCarriedReceipt-13` has a spec reading CLOSED rev-8, but its own row reads SPECCED, as do
  `DEPL-dCarriedReceipt-1` through `-15`. Filed rather than swept: fifteen status flips across a
  build this session did not build carry their own judgement calls.

## Already recorded — do not re-file

`TOOL-aFlaggedScaffold-3` (`update` cannot land a newly-shipped source; no verb lands bytes without
running `[adopt]`), `DEPL-aFerriedDossier-1`, `TOOL-aScouredKit-26` (no cross-entry destination
token), `TOOL-aBoundedVerdict-29` (two gates disagree on a marker population — it enumerates five
drift-audit sites and there are eight), `DEPL-dCarriedReceipt-15` (root-prefix literals in kit
bodies), `TOOL-aPacedTurnstile-11` (an entry spelling another entry's command with no hard
dependency).

## How much of this is verified

Five parallel lenses measured this tree; all five returned. Every finding above was then re-verified
by the orchestrator reading the cited file or, for `-8`, reading the adopter's own receipt. The
**skeptic pass did not run** — the build landed on lens output plus orchestrator confirmation, so
these are two independent readings rather than refuted findings.

Not measured: whether `-3`'s rule precedence behaves as the descriptor comment says when driven
through `resolve_entry`; whether a genuinely receipt-less tree can be brought under the probe
end-to-end; and the behavioural content of the ~1,900 upstream lines the document scopes as a pull.

## Non-goals

No change to `govkit.py`, to any `kit.toml`, to the runbook, or to a gate leg. No fix for any of the
eleven — each is a follow-up unit, and the two wanting new assertions owe a failing case observed
before they land.

<!-- roster:units -->

*No unit is planned under this build; its output is eleven backlog rows and the triage above.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11

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
