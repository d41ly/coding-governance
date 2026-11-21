# TOOL-dPlacedRequest-56 — the round-4 promotions' minors: fresh race attempts, failures staged so they take, one oracle contract, and criteria that read the places they name

**Status:** CLOSED · rev-8 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 29 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-10-25-build-TOOL-dPlacedRequest-56-deviation-561.md](../build/2026-10-25-build-TOOL-dPlacedRequest-56-deviation-561.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-56-deviation-562.md](../build/2026-10-25-build-TOOL-dPlacedRequest-56-deviation-562.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-56-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-56-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-56-deviation-711.md](../build/2026-11-21-build-TOOL-dPlacedRequest-56-deviation-711.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-56-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-56-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-56-orders-29-30-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-56-orders-29-30-reground-brief.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
exited CONVERGED with 25 confirmed findings. Its three highs are units 53, 54 and 55. This unit is
the batch `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`
makes of the rest: 12 MEDIUM and 10 LOW findings by raw id, one scope item per id, each naming its
finding and, in brackets, the review item holding it (M1 to M9, L1 to L7). It sits above every unit
of the build, at order 29, after units 53 to 55 at 28.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1, S2 | 7, 18 (M1) | MEDIUM | unit 52 |
| S3, S4 | 2, 23 (M2) | MEDIUM | unit 52 |
| S5 | 3 (M3) | MEDIUM | units 48, 50 |
| S6 | 8 (M4) | MEDIUM | units 44, 52 |
| S7, S8 | 9, 25 (M5) | MEDIUM | unit 52 |
| S9 | 12 (M6) | MEDIUM | units 45, 51, 52 |
| S10 | 13 (M7) | MEDIUM | units 43, 44 |
| S11 | 19 (M8) | MEDIUM | unit 52 |
| S12 | 24 (M9) | MEDIUM | unit 51 |
| S13, S14 | 4, 20 (L1) | LOW | unit 51 |
| S15, S16 | 5, 10 (L2) | LOW | unit 51 |
| S17, S18 | 6, 11 (L3) | LOW | units 50, 52 |
| S19 | 14 (L4) | LOW | units 44, 52 |
| S20 | 15 (L5) | LOW | units 47, 50, 52 |
| S21 | 21 (L6) | LOW | unit 51 |
| S22 | 26 (L7) | LOW | unit 52 |

Every unit the minors land on is now CLOSED, the charter's P19 keeps built work out of in-place
rewrites, and a builder writes no spec. Re-grounded on 2026-11-20 against the tree at `78b81e5ec` by
`2026-11-20-prompt-TOOL-dPlacedRequest-56-orders-29-30-reground-brief`, each item is one of four
kinds. The scope ids are kept so the siblings that cite them still resolve, and criterion ACn
observes item Sn.

| Kind | Items |
|---|---|
| builds a product change still owed | S7, S8, S20, S22 |
| carries the one version oracle, §4's block, observed by a probe | S6, S10 |
| observes built code or a record by a probe | S3, S4, S12, S14, S16, S21 |
| closed by a landed unit, or resolved in §4 as text a closed spec froze | S1, S2, S5, S9, S11, S13, S15, S17 to S19 |

Narrowed from rev-7: no item edits a spec; the race's fresh-clone attempts and their arm are not
built, since unit 52's rebuilt block resets each attempt another way; the `flat` note, the sequence
lines and the measurement of unit 34 are not made, since their targets are closed or moot.

## 2. Scope (IN)

- **S1** — finding 7 (M1). Closed by `TOOL-dPlacedRequest-52` rev-10: its AC1 counts nothing, its AC6
  is out with its S6, and its AC9 reads the checker's size join, so no criterion of 52 names a
  pattern in two places (52's §4 "The folds (F4)"). NOT OBSERVED here: spec text.
- **S2** — finding 18 (M1). Closed by the same rev: the `flat` definition went with the last
  criterion that read it. NOT OBSERVED here: spec text.
- **S3** — finding 2 (M2). Satisfied by unit 52's rebuilt race block, the `TOOL-dPlacedRequest-48`
  block of `tools/unattended/unattended.test.sh`. Each of its three attempts writes A's and B's texts
  with the marker `zq-race-marker-48-<n>`, so the key is new to the store and no stored
  `requests/<key>.md`, `.typed` line or origin ref of an earlier attempt is met. Before A starts it
  clears the handshake files `$pr_h/once`, `$pr_h/held` and `$pr_h/release`, which sit outside the
  clone (`TOOL-dPlacedRequest-58`'s fold, F5). Left, its observation. Observed by AC3.
- **S4** — finding 23 (M2). Satisfied by the same block. It counts the clone's `health.log` before A
  and reads only the lines past that count for `node-lock-broken` on `requests.lock`; `request race
  never placed` stops the attempts at once; A is waited for on every attempt, its hold bounded by
  the stub; and a `jobs -p` row asserts no job is left. Left, its observation. Observed by AC3.
- **S5** — finding 3 (M3). Resolved in §4: units 48 and 50 are CLOSED, so the two order-25 passes
  ran and no sequence line is owed. NOT OBSERVED here: spec text.
- **S6** — finding 8 (M4). §4's block is the build's one version oracle: spec 55's block with its
  count line corrected. `git rev-list … --count "$r" --` ends its revisions with `--`, and `n` is
  checked numeric before use, else `version oracle: rev-list failed` and exit 2. Spec 55's block is
  superseded there and is not edited (F4). Observed by AC6.
- **S7** — finding 9 (M5). `skills/session-kickoff/manifest-check.test.sh` gains the case no
  criterion stages today. It evaluates `skills/session-kickoff/manifest-check.sh#derive_claims_line`
  through the suite's `eval "$(awk …)"` seam, writes a file at `$s/f`, sets `CARD_DIR="$s/f/sub"`,
  and expects the cell's `claims — skipped: no scratch directory under` line. The case names no
  `chmod`. Observed by AC7.
- **S8** — finding 25 (M5). Before it calls the function, the case asserts its stage took:
  `mkdir -p "$CARD_DIR"` fails, else the case fails `the scratch-directory stage did not take` and
  judges no cell. Observed by AC8.
- **S9** — finding 12 (M6). Closed by `TOOL-dPlacedRequest-44` rev-9 and `TOOL-dPlacedRequest-45`:
  45's AC2 names `TOOL-dPlacedRequest-44` AC2's fixture and holds no `--no-ff`, as 52's S14 records.
  NOT OBSERVED here: spec text.
- **S10** — finding 13 (M7). The exit contract units 52, 54 and 55 leave stands in §4's block: an
  empty walk exits 2, and a merge that is not this build's own exits 2. Spec 44's text and 43's AC24
  are frozen and name spec 44's block, which spec 55 superseded and §4 supersedes in turn. Observed
  by AC6.
- **S11** — finding 19 (M8). Closed by `TOOL-dPlacedRequest-43` S22, as 52's S9 records: the size join
  reads the cap `tools/check-spec-tokens.py#read_size_ceilings` answers over live specs only, and
  unit 34 is CLOSED, so no edit S11 named is made and no ceiling is typed. NOT OBSERVED here: unit 34
  sits outside the size join's population.
- **S12** — finding 24 (M9). Satisfied: the record
  `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md` holds no rev-2 row, and 51's
  AC1 and AC2 are frozen. Left, the absence observed with its red. Observed by AC12.
- **S13** — finding 4 (L1). Resolved in §4: 51's S1 is frozen, and the record and 51's §4 and AC1
  spell the row `--first-parent -p <base>..HEAD`. NOT OBSERVED here: spec text.
- **S14** — finding 20 (L1). Left, the one grepped string observed where it is graded: the record
  holds the spelling 51's AC1 greps for. Observed by AC16.
- **S15** — finding 5 (L2). Closed by 51 rev-3, whose AC1 passes every `grep -cF` pattern after
  `-e`. NOT OBSERVED here: spec text; AC16 runs those commands.
- **S16** — finding 10 (L2). Left, the run: each command 51's AC1 spells runs once over the record
  and exits 0. Spec 51 is frozen, so this unit's acceptance ledger records it. Observed by AC16.
- **S17** — finding 6 (L3). Resolved in §4: 50's §4 Evidence is frozen. NOT OBSERVED here: spec
  text.
- **S18** — finding 11 (L3). Closed by 52 rev-10, which carries no AC15. NOT OBSERVED here: spec text.
- **S19** — finding 14 (L4). Resolved in §4: 44's F1 is frozen, 52's F1 names
  `TOOL-dPlacedRequest-54` F1 as superseding its pick, and §4's block runs no merge-base form.
  NOT OBSERVED here: spec text.
- **S20** — finding 15 (L5). A torn stamp joins its siblings in the `TOOL-dPlacedRequest-47` block
  of `tools/unattended/unattended.test.sh`, as §4's torn-stamp row: a three-commit `renews: no`
  tenure whose middle commit's only feed line carries `2026-10-2` reads `live`, and a scratch copy
  whose walk keeps no ISO-shape test reads it `unknown -`. Spec 47 carries no AC4 and 52 no AC21, so
  the row is this unit's own. Observed by AC20.
- **S21** — finding 21 (L6). Closed by 51 rev-3, whose §5 observability line says `gotchas.py`
  prints the record's name, description and path. Left, its observation. Observed by AC21.
- **S22** — finding 26 (L7). Satisfied in the walk: `tools/unattended/unattended.sh#read_claims`
  reads a `renews:` line only while `cr` holds its sentinel, so a commit's first line wins. Left, the
  row no suite stages, §4's duplicate-key row: a tip carrying `renews: no` then `renews: -` reads
  `stale`, and a scratch copy whose match keeps the last line reads it `live`. Observed by AC22.

## 3. Non-goals (OUT)

- No edit to any spec but this one: every unit the minors land on is CLOSED (F3).
- No second mechanism for a high: units 53, 54 and 55 own findings 1, 16 and 22.
- No race arm: unit 52's rebuilt block holds S3 and S4, and `TOOL-dPlacedRequest-58` owns the absence
  test of its handshake clear.
- No base read: `TOOL-dPlacedRequest-57` S1 spells it, and the close passes it to §4's block.
- No renumbering of any order, and no change to the driver: the walk already reads the first line.
- No new gate leg, no lint over spec criteria and no new bug-class record: each row joins an existing
  suite, and the closing review's left-shift decides any record
  (`doc.build-method#m8-closing-the-build`).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — the rebuilt race block and the rev-10 text, which S1 to S4, S18 and S22 observe or record closed
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's block and F1, frozen, which §4's block supersedes through spec 55's
- **consumes-from** `TOOL-dPlacedRequest-43` — AC24, frozen, whose oracle §4 resolves to its block
- **consumes-from** `TOOL-dPlacedRequest-45` — AC2, frozen, which S9 records closed
- **consumes-from** `TOOL-dPlacedRequest-47` — the observer clock block of the suite, which S20 extends with the torn-stamp row
- **consumes-from** `TOOL-dPlacedRequest-48` — the placed-race block as unit 52 rebuilt it, which S3 observes, and its Files touched, frozen, which S5 resolves
- **consumes-from** `TOOL-dPlacedRequest-50` — §4, frozen, which S5 and S17 resolve
- **consumes-from** `TOOL-dPlacedRequest-51` — AC1, §5 and the record, which S12 to S16 and S21 observe
- **consumes-from** `TOOL-dPlacedRequest-53` — 52's AC1, AC6 and AC9 as that unit left them, which S1 records closed
- **consumes-from** `TOOL-dPlacedRequest-54` — the own-merge test, which §4's block carries
- **consumes-from** `TOOL-dPlacedRequest-55` — §4's block, frozen, which this unit's block supersedes with the count line corrected
- **hands-off** `TOOL-dPlacedRequest-57` — §4's block, which that unit's AC1 runs with the observing run's base
- **hands-off** `TOOL-dPlacedRequest-58` — S3 and AC3, which name the handshake clear unit 52's block makes, folded at this rev; that unit builds the absence test
- **hands-off** `TOOL-dPlacedRequest-59` — S4, S11, S19, S22, §3, §4, §5 and §10 as this rev leaves them, which that unit's minors amend
- **hands-off** `TOOL-dPlacedRequest-61` — §1, the header order and the edge to 57, which that unit's items for findings 3 and 10 amend
- **hands-off** `TOOL-dPlacedRequest-63` — §3's renumbering bullet, which that unit's item for finding 18 restates

## 4. Design

### The oracle the close runs (S6, S10)

```bash
base=$1
git rev-parse -q --verify "$base^{commit}" >/dev/null \
  || { echo "version oracle: base does not resolve"; exit 2; }
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD --)
case "$(git log -1 --format=%s "${t:-HEAD}" --)" in
  "merge: dPlacedRequest — land onto "*) own=1 ;; *) own=0 ;; esac
if [ -z "$t" ] || [ "$own" = 0 ] || git merge-base --is-ancestor "$t" "$base"; then
  echo "version oracle: no prepared merge on HEAD"; exit 2; fi
r="$t^1..$t^2"
n=$(git rev-list --no-merges --invert-grep --grep='^mint:' --count "$r" --)
case $n in ''|*[!0-9]*) echo "version oracle: rev-list failed"; exit 2 ;; esac
echo "version oracle: ${t:0:8}^1..${t:0:8}^2 · $n commits"
[ "$n" -gt 0 ] || { echo "version oracle: walked no commit of the build"; exit 2; }
w=$(git log --no-merges --invert-grep --grep='^mint:' -p "$r" \
      -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh) \
  || { echo "version oracle: the walk failed"; exit 2; }
if printf '%s\n' "$w" | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='; then exit 1; fi
exit 0
```

It is spec 55's block with one line changed and one added. The count ends its revisions with `--`,
so git never weighs the range as a path, and a count that is empty or not a number refuses by name
instead of reading as an empty walk. Every other line, refusal and exit is spec 55's.

### Where it runs, and what it supersedes

- The close runs this block once, on the prepared merge, after `--phase VERIFYING` and the last
  `push-main.sh --prepare`, with the base `TOOL-dPlacedRequest-57` S1 reads as its one argument.
- Spec 55's §4 block, "The oracle the close runs", is superseded by this one and is not edited.
  Spec 44's block, which spec 55 superseded, stays superseded. Spec 55's AC1 to AC5 name the shapes
  this block is measured on (AC6).
- Specs 43, 44, 52 and 54 name an earlier block. Each is CLOSED, so its text stands as built, and
  this section is where the close finds the one block it runs (P19).

### The placed race as unit 52 rebuilt it (S3, S4, F5)

The block's loop, `tools/unattended/unattended.test.sh@7448c3f6:21728`, per attempt: clear the three
handshake files; write `a.md` and `b.md` with the attempt's marker; count `health.log`; start A and
wait for `held` (never placed stops the loop); run B; touch `release` and wait for A; read the log
past the count; keep the attempt or discard it. Unit 58 ordered 56's S3 and race sketch to carry the
clear. The built block clears before A, so S3 names the clear and AC3 observes it. Unit 58's absence
test is that unit's own (F5).

### The torn-stamp row (S20)

In the `TOOL-dPlacedRequest-47` block, after its AC3 row, with that block's helpers:

| Commit | `renews` | Feed line |
|---|---|---|
| tip | `no` | sighted 60 s ago, the ref's newest line (PINNED) |
| middle | `no` | one line, its `seen-utc` the torn `2026-10-2` |
| opener | `no` | sighted 3600 s ago (PINNED) |

On the driver the middle commit is unsighted and read past, the opener stands for the beat, and the
row prints `live` under the 24-hour default bound. The copy `torn.sh` under `$oc_copy` replaces the
walk's clause `!(x[2] in want) || x[6] !~ /…Z$/` with `!(x[2] in want)`; that clause is the walk's
alone, since `read_first_seen` reads no `want`. On the copy the torn stamp sorts before `thr`, the
walk stops at the middle commit, and `read_first_seen` still reads that beat unsighted:
`unknown -`. A `same` row checks the driver carries the clause once and the copy not at all.

### The duplicate-key row (S22)

After the `DPR46 AC3` loop, in its shape: a tip written by `add_lease_commit` with the whole-line
argument `$'renews: no\nrenews: -'`, sighted 60 s ago (PINNED), over a `renews: no` commit sighted
3600000 s ago (PINNED). The driver keeps `no`, reads on, and prints `stale`. The copy `last-line.sh`
matches `/^renews:/` without `cr == "\001"`, keeps `-`, stops there, and prints `live`.

### The scratch-directory case (S7, S8)

```bash
eval "$(awk '/^derive_claims_line\(\) \{/,/^}$/' "$CHECK")"
s=$(mktemp -d); : > "$s/f"; CARD_DIR="$s/f/sub"
if mkdir -p "$CARD_DIR" 2>/dev/null; then fail "the scratch-directory stage did not take"
else check_eq "…" "claims — skipped: no scratch directory under $CARD_DIR to capture the read in" \
  "$(derive_claims_line write)"; fi
```

The skip returns before `run_driver_bounded`, so no driver stub is needed. `CARD_DIR` is derived
from the git common dir in the script, so the case sets it in its own shell after the `eval`.

### The closed specs' text (S1, S2, S5, S9, S11, S13, S15, S17 to S19)

The closing mechanism is P19: a CLOSED spec is a frozen record, so its text stands as built, and the
fact each finding asked for stands here, or in the code this unit builds.

- S1, S2, S18: 52 rev-10 carries no `flat`, no AC6 and no AC15, and its AC1 and AC9 count nothing.
- S5: the order-25 passes of 48 and 50 ran and closed; a sequence line would order nothing.
- S9: 45's AC2 names 44's AC2 fixture; 52's S14 records it.
- S11: unit 34 measured 53340 bytes on 2026-11-20 (PINNED), CLOSED and outside the size join.
- S13, S15: 51's S1 spells the row `--first-parent <base>..HEAD` with `-p` or `--name-status`, and
  its §4 table and AC1 spell `--first-parent -p <base>..HEAD`; AC16 greps the record for the latter.
- S17: 50's §4 Evidence cites 47 as built; 47 is CLOSED and its labels stand.
- S19: 44's F1 keeps "the merge-base form elsewhere"; 52's F1 names 54's F1 as superseding, and the
  one block above runs fact 1 and no merge-base form.

### Evidence

- Measured 2026-11-20 on node a with git 2.54.0.windows.1, in the fixture of spec 55's §4 Evidence
  under the session scratch root, the base its root commit: this block printed the header ending
  `· 2 commits` and both version lines, exit 1 (2 PINNED); a stacked `records: close` commit read the
  same; a base naming no commit printed `base does not resolve`, exit 2; a merge built by
  `git commit-tree -p <tip> -p <base>` printed `· 0 commits` and `walked no commit of the build`,
  exit 2. PINNED at that date.
- Under a stub `git` first on `PATH`, exiting 128 with no output on a `rev-list` call carrying
  `--count`, this block printed `rev-list failed`, exit 2, and spec 55's block printed an `integer
  expected` error and `walked no commit of the build`, exit 2: a failed count read as an empty walk.
- The review's deep-path failure did not reproduce on node a: from working directories of 197 to 247
  characters (PINNED), spec 55's count line without `--` printed 2 (PINNED), with `core.longpaths` set
  true in the user config and with it overridden false. The `--` costs nothing where it is not needed.
- In this worktree, with the run's base read as `TOOL-dPlacedRequest-57` S1 reads it, the block
  printed `no prepared merge on HEAD`, exit 2.
- `derive_claims_line` under the `eval` seam, with a file in `CARD_DIR`'s parent place, printed the
  skip line, and `mkdir -p` failed with "Not a directory"; a `chmod 555` directory left `mkdir -p`
  working under Git Bash on NTFS. Measured 2026-11-20.
- `read_claims` admits a feed line to `seen` only when `seen-utc` is ISO-shaped, and sets `cr` only
  from its sentinel; read 2026-11-20 in `tools/unattended/unattended.sh#read_claims`.
- `grep -cE` for the rev-2 row over the record printed 0; each of 51's AC1 commands printed 1 and
  exited 0. Measured 2026-11-20.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: S20's and S22's rows and copies, and `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_8`, each with a `RAISED` comment
- `skills/session-kickoff/manifest-check.test.sh`: S7 and S8's case and its `FLOOR_ASSERTIONS`

### Alternatives rejected

- **A fresh unit-19 clone per race attempt (rev-7's S3).** Unit 52's block resets by a new key and
  the clear; a second reset beside it is a copy of one already built.
- **Edit spec 55's block in place.** P19 keeps it as built; a later text superseding it is how spec 55
  itself treated spec 44.
- **The block in `TOOL-dPlacedRequest-57`'s §4, beside the base read.** That unit changes no line of
  the block; this one does, and the block lives with its last correction.
- **The deep path as the red case.** It does not reproduce on node a; the stub stages the failure the
  guard reads, on every node.

## 5. Production-readiness checklist

- security — none: a read of local history, and two test rows over scratch fixtures.
- perf / scale — the oracle gains one `case`; each suite gains a few fixture commits.
- error / empty / loading states — a failed count exits 2 named (S6); a stage that did not take
  fails named (S8).
- observability — the oracle's refusal names the count; each row's label names its shape.
- risks — the torn row's red rests on `2026-10-2` sorting before `thr`, true of every date this
  build runs on; S7's stage rests on `mkdir -p` refusing a path under a file, measured on Git Bash.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — none: test code and criterion text.

## 6. Acceptance criteria

- **AC3** — When
  `awk '/THE REQUEST RACE, PLACED/{f=1} f; f&&/^rm -rf "\$LF"$/{exit}' tools/unattended/unattended.test.sh`
  cuts the race block from the suite, its `for pr_n in 1 2 3` loop holds
  `rm -rf "$pr_h/once" "$pr_h/held" "$pr_h/release"`, `zq-race-marker-48-%s`, `pr_e0=` and
  `tail -n "+$((pr_e0 + 1))"`, and the block holds the `jobs -p` row.
  Red when: an attempt meets a key, a handshake file or a log line an earlier attempt wrote.
- **AC6** — When §4's block runs in spec 55's fixture under `%TEMP%`, on each shape of spec 55's AC1
  to AC5 it prints what that criterion names; with a stub `git` whose `rev-list --count` exits 128
  and prints nothing, it prints `version oracle: rev-list failed` and exits 2, where spec 55's block
  prints `walked no commit of the build`.
  Red when: a count that failed reads as an empty walk.
  fixture: built by the probe under `%TEMP%`, not held in the tree.
  figure: the count PINNED at 2, the fixture's two branch commits.
- **AC7** — When the S7 case runs, `derive_claims_line write` prints
  `claims — skipped: no scratch directory under` and the staged path, and the case's own lines,
  `awk '/TOOL-dPlacedRequest-56 AC7/,/^$/' skills/session-kickoff/manifest-check.test.sh`, hold no
  `chmod`.
  Red when: the stage leaves the directory creatable and the skip never runs.
- **AC8** — When a scratch copy of the case stages a `chmod 555` directory under Git Bash instead of
  the file, the case fails `the scratch-directory stage did not take` and judges no cell.
  Red when: a stage that did not take is judged as a pass.
- **AC12** — When `grep -cE 'git log --first-parent <base>\.\.HEAD` *\|'` runs over
  `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`, it prints 0, and over a
  scratch copy with that row planted it prints 1.
  Red when: a stale row stands beside its correction.
- **AC16** — When each `grep -cF -e` command 51's AC1 spells runs over the record, each exits 0 and
  prints 1, the `--first-parent -p <base>..HEAD` one included.
  Red when: a criterion errors before it measures, or one grepped string has two spellings.
  figure: each count DERIVED by its `grep`.
- **AC20** — When the torn-stamp row runs, `read_clock_row` prints `live` on `$SCRIPT` and
  `unknown -` on `$oc_copy/torn.sh`.
  Red when: a torn `seen-utc` ages a lease.
- **AC21** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh`
  runs, the record's checklist entry prints its front-matter `description`, the field `build_record`
  in `tools/memory-tree/gotchas.py` reads.
  Red when: the checklist prints body text as the record's line.
- **AC22** — When the duplicate-key row runs, `read_clock_row` prints `stale` on `$SCRIPT` and `live`
  on `$oc_copy/last-line.sh`.
  Red when: a duplicate `renews` key resolves otherwise than the first line.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC20 AC22 · the torn-stamp row against a copy without the walk's ISO-shape clause, the duplicate-key row against a copy keeping the last `renews:` line · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` move by the rows gained · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC7 AC8 · a file in `CARD_DIR`'s parent place, staged against a `chmod 555` stage that does not take · `FLOOR_ASSERTIONS` rises by the rows gained

## 8. Open questions

- **F1 — How does each race attempt start clean (S3)?** (a) A fresh unit-19 clone and bare remote
  per attempt; (b) the stored copy, `.typed` and the remote's request ref reset in place. (b) must
  name every write an attempt makes and stay current with it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's first fix judged sound. widens: none · relaxes: none.
  Overtaken by unit 52's rebuilt block, whose attempt-numbered key and clear reset every write an
  attempt makes; S3 observes it (F3).
- **F2 — How are the named places observed (S1)?** (a) One extract per named place beside unit 53's
  counts; (b) the counts alone. (b) passes two mentions in one paragraph. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's second fix judged sound. widens: none · relaxes:
  none. Overtaken by 52 rev-10, whose criteria count nothing; S1 records it closed.
- **F3 — What becomes of an item that edits a CLOSED spec?** (a) A product change still owed is built
  and observed, and a text-only finding is resolved in §4 naming P19; (b) the closed spec is edited
  with a rev bump; (c) the item is dropped unrecorded. (b) rewrites built work; (c) loses the fact.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; P19 freezes every unit
  these minors land on, and the kinds table of §1 sorts each item by what the tree holds.
  widens: none · relaxes: none
- **F4 — Where does the oracle with the corrected count live, so the close runs one?** (a) In this
  spec's §4, whole, naming spec 55's block superseded and never edited; (b) a one-line patch here
  the close applies to spec 55's block; (c) spec 55's block edited. (b) makes the close assemble two
  texts; (c) rewrites a CLOSED spec. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated):
  (a), rung 3; of the four re-grounded units only this one changes a line of the block, so it is the
  last to correct it, and `TOOL-dPlacedRequest-57` names this block. widens: none · relaxes: none
- **F5 — Is the amendment `TOOL-dPlacedRequest-58` orders to this spec made at a pass or now?** (a)
  Now, once, in this text: S3 names the handshake clear the built block makes and AC3 observes it,
  and unit 58 reduces to observing that text beside its own absence test; (b) at unit 58's pass, by
  a builder. (b) has a builder write a spec, which no builder does. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; this spec is DEFERRED, so the amendment is a
  spec act the re-grounding makes once, as the brief's fold rule names. widens: none · relaxes: none
- **F6 — Is the count guard kept when node a does not reproduce the deep-path failure?** (a) Keep `--`
  and the numeric guard, staging the failure by a stub `git`; (b) take the item out as unreproduced;
  (c) keep the deep path as the red case. (b) leaves a failed count reading as an empty walk, which
  the stub shows on any node; (c) is a red no node here can observe. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the review reproduced it on the same git
  release, and the stub observes the guard everywhere. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-4 promotions' 12
  MEDIUM and 10 LOW findings.
- rev-2 · 2026-10-25 · AC5 observes the two specs by one grep pipeline, the shared suite file a
  `grep -F` argument rather than a token of its own, so the criterion reads as a grep over specs and
  never as a suite run (the promoted fix brief's [bar] hit); the suite stays on §7's `New arm:` line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the consumes-from edge to `TOOL-dPlacedRequest-57` and the hands-off edges to `TOOL-dPlacedRequest-58` and `TOOL-dPlacedRequest-59`, mirroring theirs.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-6 · 2026-11-19 · §7 · the spec-token checker's guards join: §4 Files touched names `tools/unattended/unattended.sh`, which `tools/gate-legs.json` lists in the guard of leg `tier2-review self-test`, so §7's leg line names that leg.
- rev-7 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-8 · 2026-11-20 · §1 · §2 S1 to S22 · §3 · §4 · §5 ·
  §6 AC3 AC6 AC7 AC8 AC12 AC16 AC20 AC21 AC22 · §7 · §8 F1 to F6 · §10 · re-grounded by
  `2026-11-20-prompt-TOOL-dPlacedRequest-56-orders-29-30-reground-brief`: every unit the minors land
  on is CLOSED, so no item edits a spec (F3) and §1 sorts the items by kind; §4 carries the one
  version oracle whole, spec 55's block with the count guarded, naming spec 55's block superseded
  (F4); `TOOL-dPlacedRequest-58`'s amendment folded into S3 and AC3 (F5); the race items observe
  unit 52's rebuilt block; the scratch-directory case, the torn-stamp row and the duplicate-key row
  are the product left; the edge with `TOOL-dPlacedRequest-57` turned to a hands-off, that unit
  running this block; line citations swapped for symbol citations and a blob pin, and the build
  method's sections for their alias tags.

## 10. Reuse audit

The seams extended: the oracle of `TOOL-dPlacedRequest-55`'s §4, kept whole but for its count line;
the observer clock fixture of the `TOOL-dPlacedRequest-47` block, `add_lease_commit`,
`add_claim_sighting`, `read_clock_row` and its `${oc_src/…/…}` copies, for S20 and S22; and the
`eval "$(awk …)"` function seam of `skills/session-kickoff/manifest-check.test.sh`, already used for
`resolve_kit_dir`, for S7. The brief's named seam, the governance-ref factory
`tools/unattended/unattended.sh#write_gov_ref`, writes refs, and this unit writes none.
`python tools/codebase-map/reuse_lookup.py "stage a failing scratch directory for a card cell skip in
a test"`, run 2026-11-20, ranked `fail`, `scratch`, `skip` and `build_scratch_tree`, name stems
only, none a stage for this skip; `python tools/codebase-map/reuse_lookup.py "test row for a torn
feed timestamp in the lease walk"` ranked `rows`, `row` and `walk`, none a lease row: no existing
seam fits beyond the three above. `python tools/memory-recall/query.py "re-ground a deferred minors
batch whose target specs are closed so a builder can build it"` with the terms below returned the
order-25 and unit-43 re-grounding briefs of this build and their returns; none disagrees with source.

Recall terms used: re-ground deferred minors batch closed spec P19 frozen fold superseded oracle torn stamp duplicate renews
