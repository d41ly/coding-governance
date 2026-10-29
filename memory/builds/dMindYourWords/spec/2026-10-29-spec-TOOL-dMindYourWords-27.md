# TOOL-dMindYourWords-27 — the `lexicon-debt` ledger homed at the repository root beside `.lexicon.conf`, outside the memory tree's closed name set

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 2

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md) | research | TOOL-dMindYourWords-22 TOOL-dMindYourWords-24 TOOL-dMindYourWords-29 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 45 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, item
H5. TOOL-dMindYourWords-1 homes the debt ledger at the literal `memory/project/lexicon-debt.txt` and
widens only gov's own hygiene whitelist for it. `{memory_root}/project/` is a closed name set at every
target, an older or forked memory-tree checker refuses the file, a non-default memory root puts the
ledger outside the tree its guard watches, and an adopter with no memory tree gains a `memory/` folder.
This unit homes the ledger where the kit's other adopter-owned file already lives, the repository root
beside `.lexicon.conf`, a path that is the same at every target and that no hygiene checker grades.

## 2. Scope (IN)

- **S1** — The home. The `lexicon-debt` registration in `tools/lexicon/kit.toml` sets
  `home = ".lexicon-debt.txt"`, and the `lexicon naming predicates` guard carries `.lexicon-debt.txt`
  where unit 1 put `{memory_root}/project/lexicon-debt.txt`, re-rendered into `tools/gate-legs.json`.
  Observed by AC2 and AC5.
- **S2** — gov's file moves. `git mv memory/project/lexicon-debt.txt .lexicon-debt.txt`, its rows
  unchanged, and `.gitattributes` gives the new path `merge=rows` and `text eol=lf`, beside the
  `.lexicon.conf` pin (`.gitattributes:230`). Observed by AC2.
  **Readers:** by name: READER NOT IN TREE — the old path is minted by TOOL-dMindYourWords-1 at order 1
  and no tracked file spells it at base ccd1292e; the specs of units 11, 13, 14 and 15 quote it as
  records and take this home through their consumes-from edges · by value: the factory's
  `read_registrations`, which returns the home every reader and writer of the population opens.
- **S3** — No literal home in code. The engine, the scaffold (`tools/lexicon/scaffold_lexicon.py`, unit
  1 S8) and the upgrade step (`tools/govkit/steps/lexicon_pin_ledger.py`, unit 1 S9, its `up`, `down`
  and `witness`) take the home from the registration's `home` field, never from a spelled path, so a
  later move edits one line. Observed by AC1, AC3 and AC4.
- **S4** — The memory-tree whitelist case goes. The `F:lexicon-debt.txt` case unit 1 S3 adds to check 3
  of `tools/memory-tree/check-memory-hygiene.sh` is deleted, since no file of that name sits under
  `<M>/project/` any more, and `KIT_MEMORY_TREE_VERSION` moves. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — unit 1 S3 writes the case at order 1 and no tracked file
  spells it at base ccd1292e · by value: check 3's case statement in
  `tools/memory-tree/check-memory-hygiene.sh`, which admits a file under `<M>/project/` by these cases
  and finds no `lexicon-debt.txt` there once S2 has run.
- **S5** — The docs. The debt-ledger section of `tools/lexicon/README.md` names the home and why it sits
  at the root, and step 5 of the `govkit:entry lexicon` section of `WIRE-INTO-PROJECT.md` lists
  `.lexicon-debt.txt` among the files committed in one landing; `KIT_LEXICON_VERSION` moves once.
  Observed by AC6.

## 3. Non-goals (OUT)

- The ledger's rows, its grammar, its producers and its verdict: TOOL-dMindYourWords-1, -22 and -23.
- Shipping gov's ledger to an adopter: the file sits outside the kit's directory, so neither `govkit
  apply`'s `**` rule nor a `cp -r` of the kit carries it; the adopter's scaffold or upgrade step writes
  the adopter's own measurement.
- The check-spec-tokens rule the report names as H5's left-shift gate, refusing a literal `memory/` path
  in a shipped kit's write target: a gate is its own unit (BUILD-METHOD M2).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — the `lexicon-debt` registration, its guard, the scaffold's and the upgrade step's writes, and the whitelist case; without them there is no home to move
- **hands-off** `TOOL-dMindYourWords-14` — the home `.lexicon-debt.txt`, where that unit deletes the three accessor rows it drains
- **hands-off** `TOOL-dMindYourWords-15` — the home `.lexicon-debt.txt`, which S7's rows join
- **hands-off** `TOOL-dMindYourWords-11` — the home `.lexicon-debt.txt`, the debt ledger S3's `--check-record` reads and S4's hook block stages for
- **hands-off** `TOOL-dMindYourWords-13` — the home `.lexicon-debt.txt`, where its Migration seeds the tag rows
- **hands-off** `TOOL-dMindYourWords-29` — the home `.lexicon-debt.txt`, where the batch keeps the pin falls of units 2, 3 and 10 and which its runbook line names in place of the two offender pins (ids 6, 17)
- **hands-off** `TOOL-dMindYourWords-34` — the `[[ledger]]` home `.lexicon-debt.txt` and its guard pathspec, which that unit classes in govkit's `root-conf` guard class (review id 22)
- **hands-off** `TOOL-dMindYourWords-37` — the root home, its Readers line and the kit README's removal order, which the minors batch completes (review ids 6, 7 and 29)

## 4. Design

### Evidence

- govkit refuses any descriptor rule planning a file under `{memory_root}/project/`: "That directory is
  a CLOSED NAME SET at every target ... a FORKED checker takes it never ... Land the file inside the
  entry's own home" (`tools/govkit/govkit.py:3240-3283`, DEPL-cMendedVintage-9).
- gate-lint shipped a registry there once and it blocked updates at two adopters; the case
  `F:substitution-fed-loops.txt` was added to check 3 afterwards
  (`tools/memory-tree/check-memory-hygiene.sh:810-816`), and gate-lint's descriptor stopped shipping the
  file (`tools/gate-lint/kit.toml:14-30`).
- The factory's `home` is a literal repo-relative path with no token resolution
  (`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md:120-128`), and the
  registration ships verbatim in `tools/lexicon/kit.toml`. A literal under `memory/` therefore misses an
  adopter whose memory root is not `memory`; a literal under the kit's directory misses one whose
  prefix is not `tools`. A root path is the one literal true at every target.
- The kit already owns one root file, `[config] file = ".lexicon.conf"` (`tools/lexicon/kit.toml:77-79`),
  which `.gitattributes:230` pins `text eol=lf`; the `lexicon naming predicates` guard already carries
  `.lexicon.conf` (`tools/lexicon/kit.toml:167`).
- The kit's directory is no home for adopter rows: its `**` rule is `engine`, so `apply` writes gov's
  copy over the target's, which is why the waiver registries need their own `seed` rule
  (`tools/lexicon/kit.toml:15-65`), and a ledger seeded from gov would carry gov's 1,200 rows.

### Files touched (estimate)

- `tools/lexicon/kit.toml`: S1
- `tools/gate-legs.json`: the guard, rendered from `tools/lexicon/kit.toml`
- `tools/lexicon/lexicon.py`: S3, `KIT_LEXICON_VERSION`
- `tools/lexicon/scaffold_lexicon.py`: S3
- `tools/govkit/steps/lexicon_pin_ledger.py`: S3
- `tools/lexicon/selftest.py`: the arm of §7
- `memory/project/lexicon-debt.txt` and `.lexicon-debt.txt`: S2
- `.gitattributes`: S2
- `tools/memory-tree/check-memory-hygiene.sh`: S4, `KIT_MEMORY_TREE_VERSION`
- `tools/lexicon/README.md` and `WIRE-INTO-PROJECT.md`: S5

### Migration

gov: S2's `git mv` in this unit's pass. An adopter never held the old home: this unit lands in the
same landing as TOOL-dMindYourWords-1, and the upgrade step ships writing the root home from its first
release.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-1, before any later unit writes ledger rows.

### Alternatives rejected

- **The `{memory_root}` token, with a fallback to the count form when the hygiene admission refuses**:
  the factory resolves no token in `home`, an older or forked checker still refuses the file, and the
  fallback lands an adopter on a count form unit 1 S8's scaffold no longer seeds a pin for.
- **The kit's own directory**: `apply`'s `engine` rule and a `cp -r` both overwrite it with gov's rows,
  and its path moves with the adopter's prefix.

## 5. Production-readiness checklist

- security — no new write path: the factory's `write_rows` writes the registration's `home`, now a root
  path; no file lands under `{memory_root}/project/`.
- perf / scale — N/A — the same file at a different path.
- error / empty / loading states — an absent root home is unit 1 S6's count form, unchanged.
- observability — the registration is the one place the home is spelled; S3 makes every reader print
  what it read from there.
- risks — a second root file per adopter, of the class `.lexicon.conf` already is; an adopter with no
  memory tree gains no `memory/` folder, which closes the risk unit 1 §5 names.
- testing — AC1 to AC6 and the arm of §7.
- migration — S2 on gov; none for an adopter.
- user docs — `tools/lexicon/README.md` and `WIRE-INTO-PROJECT.md` (S5).

## 6. Acceptance criteria

- **AC1** — When `bash <prefix>/lexicon/adopt-lexicon.sh --scaffold` runs in a fixture adopter whose
  `.memory-tree.conf` sets `MEMORY_ROOT="docs/mem"` and whose `check-memory-hygiene.sh` carries no
  lexicon case, `.lexicon-debt.txt` exists at the root, `git status --porcelain -- docs/mem memory`
  prints nothing, and `python <prefix>/lexicon/lexicon.py` exits 0.
  Red when: the scaffold writes under the memory tree, or creates a `memory/` folder.
  fixture: a scratch adopter under `%TEMP%`, the lexicon kit copied at `scripts/lex/`.
- **AC2** — When `git ls-files -- '*lexicon-debt.txt'` runs at the pass, it prints only
  `.lexicon-debt.txt`, so the old home under the memory tree is gone;
  `git check-attr merge -- .lexicon-debt.txt` prints `rows`; and
  `python legacy_ledger.py read lexicon-debt` exits 0.
  Red when: the old home survives, the new one has no merge driver, or the factory cannot read it.
- **AC3** — When `grep -c 'F:lexicon-debt.txt' tools/memory-tree/check-memory-hygiene.sh` runs, it prints
  0, and `git grep -n 'memory/project/lexicon-debt' -- tools .gitattributes WIRE-INTO-PROJECT.md help`
  prints nothing.
  Red when: a whitelist case or a literal of the old home is left in a shipped file.
- **AC4** — When `python lexicon_pin_ledger.py up <target>` runs on a fixture adopter
  carrying the three legacy seams, `.lexicon-debt.txt` is written at the target's root, `witness` exits 0
  and `down` restores both files byte-identical.
  Red when: the step writes the old home, or its `witness` reads one.
- **AC5** — When `grep -c 'project/lexicon-debt' tools/gate-legs.json` runs, it prints 0, and `grep -c
  '"\.lexicon-debt\.txt"' tools/gate-legs.json` prints at least 1.
  Red when: the leg's guard watches a path the ledger never lives at.
- **AC6** — When `grep -n 'lexicon-debt' WIRE-INTO-PROJECT.md` runs, it prints a line of the
  `govkit:entry lexicon` section naming `.lexicon-debt.txt`.
  Red when: the runbook's landing list omits the ledger.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `memory hygiene` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 · a fixture adopter with `MEMORY_ROOT="docs/mem"` scaffolded, its failing case the registration's `home` set back to `memory/project/lexicon-debt.txt`, under which `git status` names a path under the memory tree · none

## 8. Open questions

- **F1 — Where does the ledger live at a target?** Options: (a) `{memory_root}/project/` through a token,
  with a count-form fallback when the target's checker refuses; (b) the kit's own directory; (c) the
  repository root beside `.lexicon.conf`. (a) needs token resolution the factory lacks and still meets
  forked checkers; (b) is overwritten by `apply` and moves with the prefix. (c) is the kit's existing
  root-file class, so it adds no install location of a new kind (M3 veto 2). RESOLVED (agent,
  2026-10-29, delegated): (c), rung 3, the only option true at every target, derived from govkit's own
  refusal text and the factory's literal `home`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 45 (HIGH, item H5) of the round-1 spec
  audit; the report's two fixes were measured against the factory's literal `home` and govkit's refusal,
  and §8 F1 records the third home they point to.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-34, TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seam is the kit's existing root-file class, `.lexicon.conf` (`[config]` in `tools/lexicon/kit.toml`,
its guard row and its `.gitattributes` pin), which this unit gives a second member, and the factory's
registration `home`, which every reader already opens. `python tools/codebase-map/reuse_lookup.py
"locate a sibling kit directory through the install receipt"` ranked `resolve_kit_dir`, which locates a
kit and not a data file, so it does not fit here; the govkit refusal at `tools/govkit/govkit.py:3240-3283`
is the record that rules out `{memory_root}/project/`.

Recall terms used: `python tools/memory-recall/query.py "where may a kit ship an adopter-owned registry file without the memory tree's closed name set refusing it" --terms "memory_root project closed name set whitelist PROJECT_REGISTRY_EXTRA seed home ledger kit.toml adopter forked checker"`
