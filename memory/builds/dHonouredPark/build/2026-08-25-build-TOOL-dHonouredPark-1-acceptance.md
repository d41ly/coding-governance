# TOOL-dHonouredPark-1 — build record

**Serves:** journal TOOL-dHonouredPark-1

Node `d`, 2026-08-25, base `bd0348f3`. Makes the authored `roster:units` pair mandatory on every
tracked build README and gates its presence. Spec: `../spec/2026-08-25-spec-dHonouredPark-1.md`.

## The population, which is the whole unit

rev-1 bound the assertion to the set `memory/project/readme-contract.txt` marks BOUND — two rows —
and the spec audit established that nobody had ruled that. The contract's own header declares its
subject as which build READMEs the heading canon and the SLOT BUDGETS bind; a roster is neither. The
owner ruled the whole tracked set on 2026-08-25, and the reason it has to be the whole set is that
`build-complete` term 3 reads the pair on every build: binding a subset would leave a later deletion
silently restoring the vacuous pass this unit exists to remove.

## The migration, and the one pair it had to rewrite rather than create

52 READMEs gained a pair, each seeded from that build's own tracked spec ids. 11 already carried one.
188 unit rows written. Seven builds have no unit-shaped spec — five of them are the files that report
`NOT A UNIT (no status header)` — and their pairs carry the empty-case sentence, which is legal and
means the build plans exactly its specced units.

`aStandingWrit` was the exception. Its pair already existed and wrapped `S0..S8` HANDLES rather than
ids, so `roster_ids` matched none of them and the pair was inert. Its scope table is genuinely useful
prose, so it was moved OUT of the markers under a heading that records why, and the derived id roster
put inside. The inertness is recorded as fixed rather than silently kept.

## Two tools, one marker, and the discipline the assertion took

`region()` in the driver refuses unless there is exactly one open, exactly one close, and the open
comes first. `_marker_index` in the engine returns the FIRST match and has no notion of duplicates or
order. An assertion built on the engine's helper would have ACCEPTED what the driver REJECTS, so
trigger 4 counts markers itself and applies the driver's rule. Its vocabulary is the driver's too —
absent, duplicated, transposed — because `units_refusal` already spells those three words for the
sibling region.

## Acceptance ledger

**Evidences:** TOOL-dHonouredPark-1

- **AC1** — OBSERVED, `--check-format`. A README with its pair deleted:
  `no authored <!-- roster:units --> pair, which every build README must carry`. Staged against
  `aBranchedMandate` and restored.
- **AC2** — OBSERVED, `--check-format`. Duplicated: `the authored roster pair is DUPLICATED — 2 open
  and 1 close marker(s)`. Transposed: `the authored roster pair is TRANSPOSED — the close marker
  precedes the open one`. Each names WHICH condition, which is deliberately stronger than the
  driver's own one-line message that lists all three and distinguishes none.
- **AC3** — GREEN AT BASE, `unattended.test.sh:1586-1600`. A pair naming an id no spec defines is
  already asserted, and the term-3 arm already exists. Kept as a regression guard; this unit added no
  coverage here and says so.
- **AC4** — GREEN AT BASE, `missing_units` returns empty. A pair equal to its spec set makes the
  difference empty and term 3 passes today, unchanged by this unit.
- **AC5** — OBSERVED, `roster_ids` run against a duplicated pair: `rc=3`, empty output. At BASE the
  same input returned status 0 and whatever `region` had printed before failing. The pipeline ends in
  `sort -u`, so it took SORT's status, and no caller tested it either — `set -u` is on and `set -e`
  is not, so the fix had to reach `missing_units` to change anything observable.
- **AC6** — OBSERVED, `rc=0`, ids empty. A well-formed but EMPTY pair stays legal and the slot leg
  reports `slot contract clean`. This is the case `set -o pipefail` would have broken: `grep -oE`
  exits 1 on no match, so the obvious fix for AC5 would have turned the legal case into a refusal.
- **AC7** — OBSERVED, `--check-format` over the migrated tree: `slot contract clean (63 build
  README(s); heading canon BOUND on 2)`, and every one of the 63 carries exactly one well-formed
  pair.
- **AC8** — OBSERVED, `memory/backlog/TOOL.md` at HEAD: `TOOL-aPacedTurnstile-14 · CLOSED`, naming
  this unit.
- **AC9** — OBSERVED, `python tools/memory-tree/gen_build_index.py --selftest`: `PASS — all arms
  held`, including five new trigger-4 arms. Four pre-existing arms asserting `[]` had to be fixed
  first, because the shared canon fixture carried no pair — a fixture standing for a conforming file
  that would have redded the live leg.
- **AC10** — OBSERVED, `corpus_ids.py --report` before and after, with `.memory-tree.conf` carrying
  this unit's movement line.

## What was narrowed, and why it is here rather than done quietly

S7 named THREE dead guards. One was deleted: `missing_units`' `[ -n "$want" ] || return 0`, which was
measured inert — `comm` over an empty side emits one blank line, which command substitution strips to
length 0 and `for` word-splits to zero iterations.

The two in `roster_ids` were KEPT. An absent file and an absent marker are unreachable only once
trigger 4 has RUN, and the driver runs standalone against trees the leg has not graded — so deleting
them would be a behaviour change on exactly the input they exist for. The spec's §9 carries the same
note at rev-5.
