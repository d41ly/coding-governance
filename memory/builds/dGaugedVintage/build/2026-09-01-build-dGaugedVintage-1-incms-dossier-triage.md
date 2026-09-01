<!-- The second inbound dossier from d41ly/incms, triaged against THIS tree rather than carried in.
     Measured 2026-09-01 against gov d65da7ab by five parallel lenses plus orchestrator
     re-verification of every cited line. Asks are DEPL-dGaugedVintage-1..11. -->

**Serves:** none — a triage of an inbound adopter dossier; this build authors no spec for it to serve

# inCMS dossier 2 — what it means for this tree

The owner asked one question of an inbound document: **are there fixes in it that would simplify
updating or adopting this repo's kits?** Yes — eleven, nine previously unrecorded. Almost none is
the fix the document proposes.

## The premise everyone had wrong

The document describes inCMS as a hand fork "with no `.governance/` receipt". `aFerriedDossier`
recorded the same in August, and this build's first commit repeated it. **It is false today.**

`C:/projects/incms/main/.governance/install.json` is a genuine govkit receipt: `schema 3`,
`gov_source` this repo, `gov_commit 14e21399`, `prefix scripts`, 14 kits, 95 file rows.
`govkit update --target <incms>` runs read-only against it and returns a per-file report. The
adopter did adopt; the probe does work. What it does not do is grade half the tree.

Two numbers, because they measure different things. The stored receipt carries **47 of 95 rows at
`evidence: unattributed`** (47 more read `vintage-match`, one carries neither). A live read-only
`update` run reports **34 of 95 ungraded**. A fresh walk therefore attributes rows the stored field
gives up on — which is the defect, not a discrepancy in the count.

## The eleven, ordered by what they cost an adopter

- **`-8` — half the receipt is never graded, and the anchor moves anyway.** `update` short-circuits
  any row whose evidence is `unattributed` (`tools/govkit/govkit.py:5529`): it tallies, prints and
  `continue`s *before* `classify_row`. Meanwhile `--write` re-stamps
  `receipt["gov_commit"] = to_commit` (`:6204`) regardless.

  **The skip itself is DESIGNED and ratified**, not an oversight —
  `memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-13.md:319` and that
  unit's acceptance ledger both state it: a row matching no gov vintage records
  `evidence: "unattributed"` with neither `commit` nor `gov_oid`, and a following `update` prints it,
  writes zero bytes and never reaches `classify_row`. That is the safe choice, because writing gov's
  bytes over a row with no known base is the destructive case.

  What is missing is a way OUT of that state. Nothing re-attempts attribution on a stored
  `unattributed` row, and `--write` moves `gov_commit` forward regardless — so the base that might
  have attributed the row recedes with every run. A live read-only `adopt --re-adopt` walk does
  attribute rows the stored field gives up on, which is the evidence that the state is escapable and
  simply has no path. This is why a five-lens manual audit happened where a verb should have answered.
- **`-3` — `memory-recall` lands no working program.** A registry DEFAULT
  (`tools/govkit/registry.toml:36`) whose `query.py` is `role = "forked"`
  (`tools/memory-recall/kit.toml:77`), which `LANDABLE_ROLES` excludes (`govkit.py:236`). `apply`
  writes no CLI while `SKILL.template.md` renders a Skill telling the agent to run it. The role is
  right for an adopter who already owns those bytes; nothing distinguishes a fresh target.
- **`-4` — drift-audit ships three version values at once.** `adopt-drift-audit.sh` says `@1.2`;
  `drift_report.py`, `drift_signals.py`, `drift_signals.template.py` and `selftest.py` say `@1.4`;
  the README and both workflow harnesses say `@1.8`, which is the constant. `check-kit-versions.sh`
  asserts three of those eight sites, so five stale markers ship green. The document blamed the fork
  for a version split it inherited from here by copy.
- **`-9` — no verb reports a per-kit version delta.** The receipt stores each row's kit version
  string and nothing in gov reads it back; `entry_version` (`govkit.py:333`) resolves gov's own
  constant, never the target's.
- **`-10` — nothing asserts the measuring gov checkout is current with its remote.** The only
  vintage guards are ancestry and reachability (`govkit.py:3769`), so `update --to HEAD` on a stale
  gov clone reports `current` for every row gov has since moved: a green meaning the measurer is
  behind.
- **`-5` — four of fifteen versioned entries ship no marker at all.** `check-wiring`,
  `codebase-map`, `kickoff-manifest` and `playbook-render` carry zero `gov:kit` tokens anywhere.
  `tools/check-kit-versions.sh:84` calls the marker the thing a deployer reads a kit's version from
  in an adopting tree; for these four that read returns nothing.
- **`-11` — the `relocate` rung goes quiet on fan-out.** `derive_carry_map` (`govkit.py:4840`) drops
  any gov directory fanning into more than one target directory — every kit that ships a rendered
  SKILL.md beside its engine files. Seven kits on this adopter.
- **`-1` — `selfcheck` never checks that a version constant ships.** Check 5 (`govkit.py:1047`)
  asserts the `version_from` file exists in gov and matches exactly one line, not that it sits in
  that entry's installed population. Latent: every kit's include covers its own version file today.
  The break was staged into `tools/govkit/entries/check-wiring.kit.toml` and selfcheck still exited 0.
- **`-7` — the prefix ratchet counts lines, not literals.** `tools/check-install-prefix.sh` uses
  `grep -c`, which counts hit LINES, so a second root-prefix literal on a line that already carries
  one — or one kit's path swapped for another's — keeps the count and passes.
- **`-6` — drift-audit's install block contradicts itself**, copying the kit to the ROOT prefix and
  then invoking it at the `tools/` prefix. Every later step agrees with the second spelling.
- **`-2` — a stale row, and a block behind it.** `DEPL-aFerriedDossier-1`'s declared closer
  `DEPL-dCarriedReceipt-13` has a spec reading CLOSED rev-8 and its code is in the tree, but its own
  row still reads SPECCED — as do `DEPL-dCarriedReceipt-1` through `-15`.

## What the document got wrong about this tree

Each row was checked by reading the named file here.

| The document says | Measured here |
|---|---|
| inCMS is a hand fork with no govkit receipt | A schema-3 receipt at `gov_commit 14e21399`, 14 kits, 95 rows |
| `adopt-memory-recall.sh` / `adopt-drift-audit.sh` are dead pointers | Both tracked, and both land: their kits' rule is `include = "**"`, role engine |
| `push-main.sh` would brick a non-`origin` lander | It reads `GOV_DEFAULT_BRANCH` first, falls back, then fails CLOSED naming both escapes |
| The gov-commit column is a stale batch anchor | It grades `install.index`, which gov never writes; each receipt row carries its own `commit` and `gov_oid` |
| Nothing answers "am I on the latest gov?" | `govkit update --target` does, read-only, today — see `-8` for what it withholds |
| `SKILL.template.md` is carried for two kits, not four | All four ship AND declare it here. That split is the fork's |
| memory-tree is unpinnable without a cross-repo probe | Gov ships the marker in three rendered docs; the fork carries one |

## Already recorded — do not re-file

`TOOL-aFlaggedScaffold-3` (`update` cannot land a newly-shipped source; no verb lands bytes without
running `[adopt]`), `DEPL-aFerriedDossier-1`, `TOOL-aScouredKit-26` (no cross-entry destination
token), `TOOL-aBoundedVerdict-29` (two gates disagree on a marker population — it enumerates five
drift-audit sites and there are eight), `DEPL-dCarriedReceipt-15` (root-prefix literals in kit
bodies), `TOOL-aPacedTurnstile-11` (an entry spelling another entry's command with no hard
dependency).

## Why the document is not carried into this tree

It cites 43 rooted-looking paths and 34 name files absent here — the adopter's `scripts/` layout
plus `.claude/` and `memory/` paths from its own tree. `DEAD_PATH_PIN` is `0` and hygiene check 15
demands set equality against an empty registry, so carrying it in would red the bar or cost 34
waiver rows for citations that are correct in the repo that wrote them. Its location is recorded in
this build's landing commits.

## How much of this is verified

Five parallel lenses measured this tree; all five returned, and the two that mattered most drove
gov's own resolvers and ran gov's deployer read-only against the live adopter rather than reading
about them. Every finding above was then re-verified by the orchestrator reading the cited file.

**The skeptic pass did not run** — the build landed on lens output plus orchestrator confirmation,
so these are two independent readings rather than adversarially refuted findings.

Not measured: whether `-3`'s rule precedence behaves as its descriptor comment says when driven
through `resolve_entry`; whether a genuinely receipt-less tree can be brought under the probe
end-to-end; how many of the adopter's 59 `not-installed` rows are renames rather than genuine
non-adoption; and the behavioural content of the ~1,900 upstream lines the document scopes as a pull.
