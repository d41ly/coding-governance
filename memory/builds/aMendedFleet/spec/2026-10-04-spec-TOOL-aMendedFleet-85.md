# TOOL-aMendedFleet-85 — the charter states what the codebase map's ratchet binds, and stops promising an inventory that cannot rot

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling+playbook · ratified 2026-10-04 · order 85 · closes TOOL-aProbedToolkit-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The charter's §5 calls for "a system inventory that CANNOT rot into fiction" whose "coverage and
freshness checks are merge-bar legs". The codebase map is that inventory, and its ratchet is honest
about less: it binds the EXACT KEYS an extractor enumerates, in both directions, while path globs are
digest-only and never gated and dossier prose is not graded at all. Unit 37 measured 26 of 27
dossiers older than the paths they describe, and the "freshness" leg byte-compares generated
artifacts, not prose. The sentence ships in `coding-governance-agents.template.md`, so every adopter
inherits the overclaim `TOOL-aProbedToolkit-15` filed. Split from unit 39 at its F1, this unit
rewords the sentence to state what the ratchet binds and what it does not, in the template, its
render in `AGENTS.md`, and the runbook line that repeats it to adopters.

## 2. Scope (IN)

- **S1** — THE TEMPLATE. The §5 bullet of `coding-governance-agents.template.md` that opens "A system
  inventory that CANNOT rot into fiction" becomes, as one wrapped bullet:
  "A system inventory whose KEYS cannot rot into fiction is worth more than one that is merely
  current: per-feature records claiming EXACT KEYS from machine-enumerated sets, with a ratchet
  failing on any unclaimed new key AND any claim naming a dead one. It binds only what an extractor
  enumerates, never a path glob and never record prose; where kept, its coverage and
  generated-artifact checks are merge-bar legs like any other (§7)."
  Observed by AC1 and AC3.
- **S2** — THE RENDER. `bash tools/playbook/adopt-playbook.sh --target .` re-renders `AGENTS.md`'s
  charter region, so S1 lands there byte-identical in the same commit. Observed by AC2.
- **S3** — THE RUNBOOK. In `WIRE-INTO-PROJECT.md`'s codebase-map bullet, the clause "so the map
  cannot rot into fiction" becomes "so its claimed keys cannot rot into fiction; path globs and dossier
  prose are not gated". Observed by AC1.
- **S4** — The header's `closes TOOL-aProbedToolkit-15` stands only while unit 39, ordered first and
  answering the ask's unclaimed-steering-files half, is not retired. If it is retired before this
  unit closes, the pass flips the verb to `advances` in a rev bump with its §9 line. Observed by AC4.
- **S5** — THE SIZE, by the rule `PLAY-aMendedFleet-2` S3 states. Both size subjects stay inside
  their declared ceilings, and where a subject's measured figure passes its recorded high-water,
  the pass re-records it with `bash tools/check-template-size.sh --bump <subject>` and names the
  byte delta in a `Decided:` trailer. Units 79 and 80 may move both high-water rows first, so
  whether either is passed is read at build time. Observed by AC3.
- **S6** — THE MANIFEST STAMP. The template is on the kickoff manifest's `watch:` line, so the same
  commit re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` with a delta line in its
  message; the staged manifest leg of `.githooks/pre-commit` refuses the commit otherwise.
  Observed by AC5.

## 3. Non-goals (OUT)

- The unclaimed steering files the same ask names, which unit 39's harness-hooks inventory answers.
- The `codebase-map` dossier's title, "CI-verified inventory claims", and the kit README's opening:
  both name the claims, which are CI-verified, and neither promises the inventory cannot rot.
- The module docstring of `tools/codebase-map/map_lib.py`, whose "cannot rot into fiction" sits under
  the keyed-claims plane it is true of, beside a line saying globs are never gated.
- The §1 and §7 lines inside the template's `kit:codebase-map` blocks, which name the legs by what
  they are and promise nothing about prose.
- Gating dossier freshness, which unit 37 reports and unit 83 prints at the close.
- Bumping the charter template's version marker, owed once at the close for every unit of this build
  that moves the template.

### Edges

- **consumes-from** `TOOL-aMendedFleet-39` — the half of `TOOL-aProbedToolkit-15` that S4's `closes`
  relies on; without it the ask is only advanced.
- **consumes-from** `PLAY-aMendedFleet-1` — the wrapper trim that frees the `AGENTS.md` headroom the
  reworded bullet's render spends; at base the charter sits 168 bytes under its row.

## 4. Design

### Evidence

Read at base `7af5f564`; the template, `AGENTS.md`, `WIRE-INTO-PROJECT.md` and the kit files are
byte-identical at the worktree tip `8312d315`.

- `git grep -n -i "rot into fiction"` outside build records and the archive hits five lines: the
  template's §5 bullet, its render in `AGENTS.md`, `WIRE-INTO-PROJECT.md` line 103, and two lines of
  `tools/codebase-map/map_lib.py` that scope the claim to keyed claims.
- `tools/codebase-map/gen_map.py`'s scaffolded rules say claims are exact keys gate-enforced both
  directions and path globs are digest-only and never gated. The `codebase-map coverage + freshness`
  leg runs `test_codebase_map.py`, whose freshness half byte-compares the generated artifacts.
- The aProbedToolkit measurements journal records the correction: the ratchet is honest and binds
  inventory KEYS; what does not survive is the framing around it.
- The §5 bullet is four lines and 358 bytes; S1's text is about 60 bytes longer.
  `bash tools/check-template-size.sh` reports 48193 of 49152 bytes for the template, and
  `AGENTS.md` measures 64344 against its 64512 row. Both PINNED 2026-10-04.
- The bullet sits outside any `kit:` block, so every adopter's render carries it, with or without
  the map.

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `AGENTS.md`
- `WIRE-INTO-PROJECT.md`
- `tools/template-size-highwater.txt`
- `memory/guides/SESSION-KICKOFF.md`

### Rollout

One commit after `PLAY-aMendedFleet-1` has trimmed the wrapper, so the charter's headroom covers
the growth. Unit 38 also edits `WIRE-INTO-PROJECT.md`, in a different bullet; dispatch is sequential.

### Alternatives rejected

- **Deleting the bullet.** The template's §1 and §7 kit blocks point at "Codebase map adopted (§5)",
  so §5 must still say what the map is.
- **Keeping the sentence and adding a caveat bullet.** Two bullets, one of which contradicts the
  other's first clause, is the stated-twice class the charter warns against.

## 5. Production-readiness checklist

- security — N/A — prose only.
- perf / scale — every session reads about 60 bytes more of the charter, ESTIMATED.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — N/A — no runtime behaviour.
- risks — the charter's headroom is thin until `PLAY-aMendedFleet-1` lands.
- testing — direct greps, the render check and the two size checks.
- migration — N/A — no stored state; adopters receive the reworded bullet on their next render.
- user docs — `WIRE-INTO-PROJECT.md`, per S3.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "CANNOT rot into fiction\|so the map cannot rot into fiction" -- coding-governance-agents.template.md AGENTS.md WIRE-INTO-PROJECT.md`
  runs, it prints nothing, and `git grep -c "never a path glob" -- coding-governance-agents.template.md AGENTS.md`
  prints 1 for each file.
  Red when: any carrier still promises an inventory that cannot rot, or the template and its render
  disagree.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it exits 0.
  Red when: the template moved and the rendered region did not.
- **AC3** — When `bash tools/check-template-size.sh` and `bash tools/check-template-size.sh AGENTS.md`
  run, each exits 0, and neither prints a WARN this pass introduced without a matching `--bump` row
  in `tools/template-size-highwater.txt`.
  Red when: the reworded bullet pushes either subject past its declared ceiling, or its growth past
  a high-water went unpriced.
  figure: 49152 and 64512 are the declared rows, read at observation time.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --asks TOOL-aProbedToolkit-15` runs
  after the pass, it lists `TOOL-aMendedFleet-85` among the ask's live specs and the ask reads
  SPECCED or INPROGRESS until this unit closes.
  Red when: the header's verb names an ask the fold cannot join, or still reads `closes` after unit
  39 was retired.
- **AC5** — When `bash skills/session-kickoff/manifest-check.sh` runs after the unit's commit, it
  exits 0, and `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` shows the `last-audit:`
  line moved.
  Red when: check 5 reports unaudited drift on `coding-governance-agents.template.md`.

No new refusal or gate clause is added, so nothing here is observed RED on a staged break; each
`Red when:` names the break an existing checker or grep reports.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook render wiring` · `playbook parity` · `govkit runbook parity` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

All run once, at the close.

## 8. Open questions

- **F1** — Which carriers does this unit reword?
  Options: the template and its render, the two the ask names; those plus the runbook line; those
  plus the `map_lib.py` docstring and the dossier title. The runbook repeats the unscoped promise to
  every adopter; the docstring scopes it to the keyed plane, and the title names claims, which are
  CI-verified.
  RESOLVED (agent, 2026-10-04, delegated): the template, its render and the runbook line, per S1 to
  S3.
- **F2** — Does this unit close `TOOL-aProbedToolkit-15` or only advance it?
  Options: `closes`; `advances`. The ask's pointer is the template, and its other half is unit 39's,
  ordered first in the same build.
  RESOLVED (agent, 2026-10-04, delegated): `closes`, with S4's fallback to `advances`.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 39 at its F1, from the four carriers of the
  phrase, the map kit's scaffolded rules and the aProbedToolkit measurements journal at base.
- rev-2 · 2026-10-04 · S5 · S6 · AC3 · AC5 · §3 · §4 · §7 · M2 cross-read: `PLAY-aMendedFleet-2`
  prices template and charter growth past a high-water with `--bump` and this unit, which grows
  both after it, did not; the template is a watched path, which units 78 and 94 re-stamp for and
  this spec did not; and the wrapper-trim dependency its Rollout states is now a declared edge.

## 10. Reuse audit

No code is added; the seams are the existing §5 bullet, reworded in place rather than joined by a
second one, and `tools/playbook/adopt-playbook.sh`, the one renderer of the charter region.
`python tools/codebase-map/reuse_lookup.py "state what the codebase map gate does not check"`
returned the `check` selftest entry points and the `map_lib.py` loaders by name stem, none of which
carries charter prose, so no existing seam fits beyond the bullet itself. Recall returned the ask
`TOOL-aProbedToolkit-15`, the aProbedToolkit measurements journal and graded findings that record
the correction, the archived v3.0 and v3.1 template snapshots carrying the same bullet, and
`TOOL-aProbedToolkit-8` on the digest's coverage figure, which unit 86 owns. Where the report and the
tree disagree: none; the phrase sits on the lines the ask names, and the runbook line is a fourth
carrier the ask did not list.

Recall terms used: `python tools/memory-recall/query.py "does the charter oversell what the codebase
map guarantees about coverage and freshness" --terms "codebase map system inventory cannot rot into
fiction coverage freshness merge-bar legs path globs digest-only overclaim template"`
