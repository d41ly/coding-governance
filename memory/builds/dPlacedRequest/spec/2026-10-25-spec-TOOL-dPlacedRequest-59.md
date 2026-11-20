# TOOL-dPlacedRequest-59 — the round-5 promotions' minors: every oracle reader passes a base, one claim-line reader, criteria that can fail, and cites by label

**Status:** CLOSED · rev-7 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 31 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |
| [2026-10-25-build-TOOL-dPlacedRequest-59-deviation-591.md](../build/2026-10-25-build-TOOL-dPlacedRequest-59-deviation-591.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-59-deviation-592.md](../build/2026-10-25-build-TOOL-dPlacedRequest-59-deviation-592.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-59-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-59-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-59-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-59-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief.md) | research | TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`)
exited CONVERGED with 23 confirmed findings. Its two highs are units 57 and 58. This unit is the batch
`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` makes of
the rest: 8 MEDIUM and 13 LOW findings by raw id, one scope item per id, each naming its finding and,
in brackets, the review item holding it (M1 to M5, L1 to L10). Four review items hold more than one
id (M1: 8 and 21; M2: 2, 9 and 16; L2: 4 and 11; L5: 7, 12 and 19), and M1 restates H1's defect,
which unit 57 closes at HIGH. It sits at order 31, after units 58 and 60 at 30.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1, S2 | 8, 21 (M1) | MEDIUM | units 52, 54 |
| S3 to S5 | 2, 9, 16 (M2) | MEDIUM | units 43, 44, 52, 54, 55, 56 |
| S6 | 10 (M3) | MEDIUM | units 44, 54 |
| S7 | 14 (M4) | MEDIUM | units 52, 56 |
| S8 | 17 (M5) | MEDIUM | units 34, 56 |
| S9 | 3 (L1) | LOW | units 52, 53 |
| S10, S11 | 4, 11 (L2) | LOW | unit 53 |
| S12 | 5 (L3) | LOW | units 44, 56 |
| S13 | 6 (L4) | LOW | units 52, 54 |
| S14 to S16 | 7, 12, 19 (L5) | LOW | unit 53 |
| S17 | 13 (L6) | LOW | unit 56 |
| S18 | 15 (L7) | LOW | unit 54 |
| S19 | 18 (L8) | LOW | unit 56 |
| S20 | 22 (L9) | LOW | units 52, 56 |
| S21 | 23 (L10) | LOW | units 44, 54 |

Every unit the minors land on is now CLOSED, the charter's P19 keeps built work out of in-place
rewrites, and a builder writes no spec. Re-grounded on 2026-11-20 against the tree at `8a52e8e3b` by
`2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief`, each item is one of four
kinds. The scope ids are kept so the siblings that cite them still resolve, and criterion ACn
observes item Sn.

| Kind | Items |
|---|---|
| builds a product change still owed | S7 |
| carries the one version oracle, §4's block, observed by a probe | S21 |
| observes built code, a frozen section or the live specs by a probe | S2, S3, S13, S18, S20 |
| closed by a landed unit, or resolved in §4 as text a closed spec froze | S1, S4 to S6, S8 to S12, S14 to S17, S19 |

Units 61 to 64, the later batches of this build, ordered amendments to this spec. Each is made here
once, at this rev, and the ordering unit observes this text (F4); §4's fold table lists them.
Narrowed from rev-6: no item edits a spec, no inventory table is written, no cut of unit 34 is made,
and the absent-log count and the oracle's single statement are observed where the closed units built
them.

## 2. Scope (IN)

- **S1** — finding 8 (M1). Resolved in §4: spec 54 is CLOSED, its sentence on the ancestor test holds
  under the one base the close passes, `TOOL-dPlacedRequest-57` S1's read of the observing run's
  pinned BASE, and the measurement on the real tree records a foreign landing the subject test
  refused, the corrected fix of unit 61's S15. NOT OBSERVED here: spec text.
- **S2** — finding 21 (M1). Left, the fifth fixture row read twice on §4's block. In spec 55's
  fixture, this slug's earlier landing refuses under a base taken after it, and the same landing is
  walked under its own first parent as base. Spec 54's AC2 and spec 55's AC3 are frozen with the
  first read alone. Observed by AC2.
- **S3** — finding 2 (M2). Every criterion of a live spec that runs the oracle names the base it
  passes. Spec 54 is CLOSED and carries no inventory, its rev-6 having resolved its S3, so the record
  is the live sweep of §4: each criterion bullet of a spec neither CLOSED nor WONTDO that matches
  `oracle[^.]*(runs|run |prints|exits)` names `RUN.md` or the fixture's base. That is the two-way
  sweep units 61 and 63 ordered (61's S1 to S4 and S12, 63's S1 and S9), over the population that
  can still change. Observed by AC3.
- **S4** — finding 9 (M2). Closed by `TOOL-dPlacedRequest-55` rev-3: its §6 runs every block criterion
  with the fixture's base commit as its argument, unit 52's AC29 among them as 55's AC2, and spec 56's
  AC6 runs in that fixture. NOT OBSERVED here: spec text.
- **S5** — finding 16 (M2). Closed by the same rev: 55's AC3 names the line each exit-2 run prints,
  the base refusal included. Specs 43 and 44 name spec 44's block, which the close no longer runs
  (§4). NOT OBSERVED here: spec text.
- **S6** — finding 10 (M3). Resolved in §4: spec 44's S1 is frozen, spec 54's S1 names the own-merge
  test, and §4's block carries fact 1, the subject test and the ancestor test. NOT OBSERVED here:
  spec text.
- **S7** — finding 14 (M4), the skeptic's corrected fix, re-grounded on
  `tools/unattended/unattended.sh#read_claims`, whose two awk programs each read claim body lines by
  hand: the record read splits at the first `": "`, and the walk matches `epoch: ` and `renews:` lines
  of its own. One reader serves both: `CLAIM_KV_AWK`, a quoted awk text in the driver in the
  multi-line shape `TASK_OPEN_AWK` has, holding §4's function `read_kv`, which each program
  prepends. The record read passes its key set in strict mode, so its split, first-occurrence rule,
  tab rule and `ok` completeness check read as today. The walk passes `epoch` and `renews` in loose
  mode, where the key ends at the first colon and the value is trimmed of `[[:blank:]]`, so a bare
  `renews:`, two spaces or a tab parse to the empty value, as unit 52's S26 built (61's S16 and 63's
  S12). The function strips a trailing CR itself and keeps its locals local (61's S11). The suite's
  rows are built with it: the lift by a variable mode of `slice_fn` (64's S6), and a CRLF row run
  under `awk -v BINMODE=3` that prints the value and its length (63's S7 and S8, 64's S7).
  Observed by AC7.
- **S8** — finding 17 (M5). Closed by `TOOL-dPlacedRequest-43` S22, as `TOOL-dPlacedRequest-56` S11
  records: the size join reads live specs only, and unit 34 is CLOSED, so no cut of it is made.
  NOT OBSERVED here: unit 34 sits outside the size join.
- **S9** — finding 3 (L1). Closed: units 52 and 53 are CLOSED, and 53's S1 records the fold made at
  52's rev-10, so no reading pass is left to a builder. NOT OBSERVED here: spec text.
- **S10** — finding 4 (L2). Closed by `TOOL-dPlacedRequest-53` rev-3: 52's AC1, AC6 and AC9 count
  nothing, and 53's AC2 reads those bullets. NOT OBSERVED here: spec text.
- **S11** — finding 11 (L2). Closed by the same rev: 53's AC1 is red when its line count over its
  own sample prints 1. NOT OBSERVED here: spec text.
- **S12** — finding 5 (L3). Resolved in §4: spec 44's F1 is frozen, and spec 56's S19 resolves the
  finding in its own §4. NOT OBSERVED here: spec text.
- **S13** — finding 6 (L4). The oracle is stated once, in §4's block. Satisfied in the closed specs:
  52's `### The oracle` section and 54's `### The oracle's head` section point at a block and hold no
  copy. Left, those reads by §4's section form, unit 62's fold, with 61's S13. Observed by AC13.
- **S14** — finding 7 (L5). Closed by 53 rev-3, whose AC3 reads the open specs' criteria. NOT OBSERVED
  here: spec text.
- **S15** — finding 12 (L5). Closed by 53 rev-3: its Evidence names 52's AC1, AC6 and AC9 by label.
  NOT OBSERVED here: spec text.
- **S16** — finding 19 (L5). Closed by 53 rev-3: it carries no `<unit>:<line>` cite into a sibling.
  NOT OBSERVED here: spec text.
- **S17** — finding 13 (L6). Closed by 56 rev-8, whose Evidence holds no cite of 47 by line.
  NOT OBSERVED here: spec text.
- **S18** — finding 15 (L7). Left, this unit's own observation, spec 54 being CLOSED: the lander still
  writes the subject §4's block matches. Observed by AC18.
- **S19** — finding 18 (L8). Closed by 56 rev-8, which carries no AC5: units 48 and 50 are CLOSED,
  as 56's S5 records. NOT OBSERVED here: spec text.
- **S20** — finding 22 (L9). Satisfied by unit 52's rebuilt race block in region eight of
  `tools/unattended/unattended.test.sh`, with unit 58's absence check before call A: an absent
  `health.log` counts 0 before A and breaks nothing after B. Left, its observation. Observed by AC20.
- **S21** — finding 23 (L10). §4's block is the build's one version oracle: spec 56's block with the
  ancestor test's status captured. The base refusal comes first, then the
  `[ -z "$t" ] || [ "$own" = 0 ]` short-circuit, then `merge-base --is-ancestor`, whose 0 refuses as
  `no prepared merge on HEAD`, 1 walks, and any other status prints
  `version oracle: the ancestor test failed` with exit 2 (61's S13 and S20, 63's S11 and 64's S19).
  Spec 56's block is superseded there and is not edited (F5). Observed by AC21.

## 3. Non-goals (OUT)

- No edit to any spec but this one: every unit the minors land on is CLOSED (F3).
- No second mechanism for a high: units 57 and 58 own findings 1 and 20.
- No change to `tools/push-main.sh`: S18 observes the subject it writes.
- No other reader of the claim grammar moves: the draw-hold read in
  `tools/unattended/unattended.sh#check_claim_writable`, and the hand reads of `epoch:` in
  `read_feed_lease_tip`, `write_gov_queue` and `write_fence_beat`, keep their own lines (F6).
- No renumbering of any order: unit 59 shares order 31 with no unit.
- No new gate leg, no lint over spec criteria and no new bug-class record: each row joins an existing
  suite, and the closing review's left-shift decides any record
  (`doc.build-method#m8-closing-the-build`).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-57` — S1's base read, which the close passes to §4's block and S1 names; frozen
- **consumes-from** `TOOL-dPlacedRequest-58` — the absence check before call A in the race block, which S20 reads beside the count; frozen
- **consumes-from** `TOOL-dPlacedRequest-53` — S1, AC1 to AC3 and Evidence, frozen, which S9 to S11 and S14 to S16 record closed
- **consumes-from** `TOOL-dPlacedRequest-54` — S1, §4 and its head section, frozen, which S1, S6 and S13 resolve or read
- **consumes-from** `TOOL-dPlacedRequest-56` — §4's block, which §4's block supersedes with the ancestor status captured, and S11, S19 and S22, frozen, which S8, S12, S17 and S19 record closed
- **consumes-from** `TOOL-dPlacedRequest-52` — the rebuilt race block and the `### The oracle` section, which S13 and S20 read, and its rev-10 text, frozen
- **consumes-from** `TOOL-dPlacedRequest-44` — S1, §4 and F1, frozen, which S6 and S12 resolve
- **consumes-from** `TOOL-dPlacedRequest-43` — AC24 and S22, frozen, which S5 and S8 resolve
- **consumes-from** `TOOL-dPlacedRequest-55` — the fixture of §4 Evidence and AC1 to AC5, frozen, in which AC2 and AC21 run the block
- **consumes-from** `TOOL-dPlacedRequest-34` — its size, frozen and outside the size join, which S8 records
- **hands-off** `TOOL-dPlacedRequest-61` — S3, S7, S21, §4's block, readers and key reader, AC3, AC7 and AC13 as this rev leaves them, which that unit's folded items observe
- **hands-off** `TOOL-dPlacedRequest-62` — §4's section form and AC13, which that unit's folded items observe
- **hands-off** `TOOL-dPlacedRequest-63` — S3, S7, §4's block and key reader, AC3 and AC7, which that unit's folded items observe
- **hands-off** `TOOL-dPlacedRequest-64` — §4's readers, Evidence and lift, AC3, AC7, AC13 and AC21, which that unit's folded items observe

## 4. Design

### The folds of units 61 to 64 (F4)

| Ordering unit | Its items | Made here in |
|---|---|---|
| `TOOL-dPlacedRequest-61` | S1 to S4, S12 | S3 and AC3: the live sweep, both directions |
| `TOOL-dPlacedRequest-61` | S5, S6 | AC7's split count and its scratch red |
| `TOOL-dPlacedRequest-61` | S11, S16 | S7: the CR strip, the locals and the loose trim |
| `TOOL-dPlacedRequest-61` | S13, S20, S15, S17 | S21's block, S1's resolution, §1's count |
| `TOOL-dPlacedRequest-62` | S1 to S4 | the section form below, AC13, AC21's order clause, this rev's log entry |
| `TOOL-dPlacedRequest-63` | S1, S9 | AC3's pattern and base alternation |
| `TOOL-dPlacedRequest-63` | S7, S8, S11, S12 | S7's CRLF row and blank class, S21's opening |
| `TOOL-dPlacedRequest-64` | S3, S8 | AC3 and AC13 |
| `TOOL-dPlacedRequest-64` | S5 to S7 | Evidence per input path, `slice_fn`'s variable mode, the CRLF row |
| `TOOL-dPlacedRequest-64` | S9, S10, S18, S19 | the readers below, defined once, and AC21's absent-sha row |

### The one version oracle (S2, S21)

```bash
base=$1
git rev-parse -q --verify "$base^{commit}" >/dev/null \
  || { echo "version oracle: base does not resolve"; exit 2; }
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD --)
case "$(git log -1 --format=%s "${t:-HEAD}" --)" in
  "merge: dPlacedRequest — land onto "*) own=1 ;; *) own=0 ;; esac
if [ -z "$t" ] || [ "$own" = 0 ]; then echo "version oracle: no prepared merge on HEAD"; exit 2; fi
git merge-base --is-ancestor "$t" "$base"; a=$?
case $a in
  0) echo "version oracle: no prepared merge on HEAD"; exit 2 ;;
  1) ;;
  *) echo "version oracle: the ancestor test failed"; exit 2 ;;
esac
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

It is spec 56's block with its one combined `if` split in two: the short-circuits keep their line,
and the ancestor test runs alone with its status captured. Every other line, refusal and exit is
spec 56's.

- The close runs this block once, on the prepared merge, after `--phase VERIFYING` and the last
  `push-main.sh --prepare`, with the base `TOOL-dPlacedRequest-57` S1 reads as its one argument.
- Spec 56's §4 block, "The oracle the close runs", is superseded by this one and is not edited, and
  the blocks of specs 55 and 44 stay superseded. Spec 57's AC1 names spec 56's block; spec 57 is
  CLOSED, its AC1 was observed on it, and this section is where the close finds the block it runs
  (P19).

### The criterion readers (S3, S13, F4)

```bash
d=memory/builds/dPlacedRequest/spec
sec()     { awk -v h="$2" 'index($0, h) == 1 {f=1; next} /^##+ /{f=0} f' "$1"; }
bullet()  { awk "/^- \*\*$2\*\*/{f=1;print;next} f&&/^(- |#|\$)/{exit} f" "$1" | tr '\n' ' ' | tr -s ' '; }
entries() { sec "$1" '## 9.' | awk '/^- rev-/{if(b)print b; b=$0; next} /^(- |#|$)/{if(b)print b; b=""; next} b{b=b" "$0} END{if(b)print b}' | tr -s ' '; }
```

`sec <file> <prefix>` prints a section's body, from the line after the heading its fixed prefix opens
to the next `##` or `###` heading, so a `# ` comment inside a fenced block does not close it (unit
62's form). `bullet <file> <label>` is unit 60 S1's bounded read with the label as an argument and the
join appended, its file a path (64's S9). `entries <file>` joins each revision-log entry with its own
continuation lines only. A criterion of this build's batches writing `bullet <unit> <label>` means
`bullet "$d/2026-10-25-spec-TOOL-dPlacedRequest-<unit>.md" <label>`, and the same for `sec` and
`entries`. They are defined here once, and units 61 to 64 read by them.

### The live sweep (S3)

```bash
crit() { awk '/^- \*\*AC[0-9]+\*\*/{if(b)print b; b=$0; next} /^(- |#|$)/{if(b)print b; b=""; next} b{b=b" "$0} END{if(b)print b}' "$1" | tr -s ' '; }
for f in $(grep -L -E '^\*\*Status:\*\* (CLOSED|WONTDO)' "$d"/*.md); do
  crit "$f" | grep -E 'oracle[^.]*(runs|run |prints|exits)' \
    | grep -vE "RUN\.md|fixture's( later)? base" | sed "s#^#${f##*/}: #"
done   # prints nothing
```

`crit` joins each criterion bullet of a file in one pass, which a label reader cannot, so the sweep
keeps its own join. A bullet that runs the oracle names it as the oracle, so the sweep finds it.

### The shared key reader (S7)

```
CLAIM_KV_AWK='function read_kv(line, keys, v, loose,   s, p, k, x) {
    sub(/\r$/, "", line); s = loose ? ":" : ": "
    p = index(line, s); if (p < 2) return
    k = substr(line, 1, p - 1); x = substr(line, p + length(s))
    if (loose) { sub(/^[[:blank:]]+/, "", x); sub(/[[:blank:]]+$/, "", x) }
    if ((k in keys) && !(k in v)) { gsub(/\t/, " ", x); v[k] = x } }
'
```

The text sits above `read_claims`, its closing quote alone on the last line, the shape
`TASK_OPEN_AWK` has. In `read_claims`:

| Program | Today | After S7 |
|---|---|---|
| the record read | `p = index($0, ": ")` and its `want`/`more` test | `read_kv($0, rk, v, 0)`, `rk` the union of `want` and `more` built in `BEGIN` |
| the walk | `/^epoch: / && !ge` and `/^renews:/ && cr == "\001"` | `{ read_kv($0, wk, cv, 1) }` after `cc == "" { next }`, `wk` holding `epoch` and `renews` |
| the walk's commit header | `ce = 0; ge = 0; cr = "\001"` | `split("", cv)` |
| `read_commit` | `ep[cc] = ce + 0; if (cr != "\001") rn[cc] = cr` | `ep[cc] = cv["epoch"] + 0; if ("renews" in cv) rn[cc] = cv["renews"]` |

Each program is passed as `"$CLAIM_KV_AWK"'<program>'`. The walk's array is `cv`, not `w`, since
`read_commit` already holds a local `w`. A hand-edited `epoch:3` with no space now
reads 3 in the walk where it read 0; `write_claim` writes `epoch: %s`, so no written commit moves.

### The suite's rows (S7)

`slice_fn` in `tools/unattended/unattended.test.sh` gains a variable mode, and a call with one
argument reads byte for byte as today:

```bash
slice_fn() { # <name> [var] -> eval that function, or that quoted variable, out of the SHIPPED driver bytes
  local s e o='()' c='^}' n='closing brace'
  [ "${2:-}" = var ] && { o="='"; c="'\$"; n='closing quote'; }
  s=$(grep -n "^$1$o" "$SCRIPT" | cut -d: -f1)
  [ -n "$s" ] || { echo "FAIL cannot find $1$o in the driver, so every arm that grades it would grade nothing"; st=1; return 1; }
  e=$(awk -v s="$s" -v c="$c" 'NR>s && $0 ~ c {print NR; exit}' "$SCRIPT")
  [ -n "$e" ] || { echo "FAIL cannot find the $n of $1$o in the driver, so the slice below would be a fragment"; st=1; return 1; }
  eval "$(sed -n "${s},${e}p" "$SCRIPT")"
}
```

The `DPR59 AC7` rows sit after the `DPR56 AC22` rows, each through one helper:

```bash
read_kv_row() { printf "$1" | awk -v BINMODE=3 "$CLAIM_KV_AWK"'BEGIN { K["'"$2"'"] = 1 }
  { read_kv($0, K, v, '"$3"') } END { printf "%s|%d", v["'"$2"'"], length(v["'"$2"'"]) }'; }
slice_fn CLAIM_KV_AWK var   # a failed lift prints its FAIL line, and every row below reads empty
```

- the CRLF row, `status: live` and a CR in strict mode, prints `live|4`;
- the trailing-blank row, `status: live ` in strict mode, prints `live |5`;
- the bare, two-space and tab rows, `renews:` alone, with two spaces and with a tab in loose mode,
  each print `|0`;
- the duplicate row, `renews: no` then `renews: -` in loose mode, prints `no|2`.

A mismatch prints a FAIL line holding the `od -c` of the output. The `DPR46 AC3` loop's `ds_v` list
gains the two-space and the tab tips, each read `stale`. Its red copies move onto the shared text:
`space-match.sh` stages `s = ": "` for `s = loose ? ":" : ": "`, reading the bare tip `live`, and
`last-line.sh` stages `(k in keys)` for `(k in keys) && !(k in v)`, reading the duplicate tip
`live`; each copy's `same` row counts its own staged line.

### The closed specs' text (S1, S4 to S6, S8 to S12, S14 to S17, S19)

The closing mechanism is P19: a CLOSED spec is a frozen record, so its text stands as built, and the
fact each finding asked for stands here, or in the code this unit builds.

- S1: 54's §4 says the ancestor test rejects every merge the build started on top of. Under 57 S1's
  read that base is the observing run's own, the only base the close passes, so the sentence holds.
  54's Evidence records fact 1 returning the run's base, a foreign landing whose subject the subject
  test refused, and 57's Evidence names both tests refusing it.
- S4, S5: 55's §6 preamble passes the fixture's base, and its AC3 names every refusal line.
- S6: 44's S1 is frozen; the block above holds the own-merge test whole.
- S8: unit 34 measured 47782 bytes on 2026-10-25 against its old ceiling, and is now outside the size join.
- S9 to S11, S14 to S16: 53 rev-3 records 52's rev-10 fold, and carries no line cite.
- S12: 44's F1 keeps its options as built; 56's S19 resolves the finding.
- S17, S19: 56 rev-8 holds no cite of 47 by line and no AC5.

### Evidence

- Measured 2026-11-20 on node a with GNU Awk 5.4.0, over `status: live` and a CR: through a pipe the
  default read printed length 12, the environment prefix `BINMODE=3 awk` 12, `awk -v BINMODE=3` 13
  and `BEGIN{BINMODE=3}` 12; from a file `-v BINMODE=3` and `BEGIN{BINMODE=3}` each printed 13. A
  `BEGIN` assignment comes too late for stdin, so `-v BINMODE=3` is the one form for the piped row.
  PINNED at that date.
- Measured 2026-11-20: §4's `read_kv`, run as the rows' helper, printed each row's value as the
  list gives it, and a `renews:` plus a tab and `no` read `no` in loose mode. The walk's program,
  cut from `read_claims` and rewired as §4's table states, chose the same beat and the same
  never-expires flag as the driver's over thirteen tip shapes: `yes`, `-`, `no` and `maybe`, no key,
  the bare, one-space, two-space and tab forms, the duplicate, a tab before `no`, a CR after `-`, and
  a second `epoch:` line. PINNED at that date.
- Measured 2026-11-20 on node a in a fixture under the session scratch root built as spec 55's §4
  Evidence builds it: §4's block with the fixture's base printed the header ending `· 2 commits` and
  both version lines, exit 1; with the merge as base it printed `no prepared merge on HEAD`, exit 2,
  and with the merge's first parent as base it walked the merge again, exit 1; an empty base and an
  absent 40-hex sha each printed `base does not resolve`, exit 2. Under a stub `git` first on `PATH`
  whose `merge-base` alone exits 128, it printed `the ancestor test failed`, exit 2, and spec 56's
  combined `if` walked the merge, exit 1. PINNED at that date.
- `grep -nE 'index\([^,)]*, *(s|": "|":")\)' tools/unattended/unattended.sh` printed one line, in
  `read_claims`' record read; the walk's two matches sit in the same function. Read 2026-11-20 at
  blob `6ee11ced`.
- `tools/push-main.sh#cmd_prepare` sets `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`,
  and `grep -cF` over the lander for its prefix printed 1. Read 2026-11-20.
- The race block in `tools/unattended/unattended.test.sh` reads `pr_e0=0; [ ! -f "$pr_hl" ] ||` and
  `pr_broke=0; [ ! -f "$pr_hl" ] ||`, after the `DPR58 AC1` absence check. Read 2026-11-20 at blob
  `9e03d5ed`.
- `sec` over 52's `### The oracle` and 54's `### The oracle's head` printed no `git rev-list`, and
  over 54 at rev-3, `git show 6df7a970:<path>`, it printed one, where the bullet form printed none.
  Measured 2026-11-20.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `CLAIM_KV_AWK` and the two programs of `read_claims` that
  prepend it (S7)
- `tools/unattended/unattended.test.sh`: `slice_fn`'s variable mode, the `DPR59 AC7` rows, the two
  tips of the `DPR46 AC3` loop, the restaged copies, and `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`,
  each with a `RAISED` comment
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Edit the closed specs with a rev bump (rev-6's design).** P19 keeps built work as built (F3).
- **The bare-key branch of rev-6, a strict split for the walk too.** It reads `renews:` plus a tab
  and a value as no key, which the built walk reads as that value (F7).
- **A `CLAIM_BINMODE` knob on the driver's calls.** It adds an environment surface to a shipped kit
  for a test row's sake; the lift runs the shipped text under `-v BINMODE=3` instead.
- **A `slice_var` beside `slice_fn`.** It copies one kind's guards at its second instance, which the
  charter's `[reuse]` refuses.
- **An inventory table in this spec.** It is a typed index of criteria the sweep reads directly.

## 5. Production-readiness checklist

- security — S7 keeps `read_claims`' key set and completeness check, and strict mode trims nothing,
  so the strict reader admits nothing it refused before; S21 refuses on an ancestor test that
  errored instead of walking.
- perf / scale — one awk function shared by two programs; one more `case` in the oracle.
- error / empty / loading states — an absent log counts 0 (S20); a failed lift prints its FAIL line
  and sets `st=1`; an empty base and an absent sha each refuse as `base does not resolve`, and a
  failed ancestor test exits 2 named (S21).
- observability — each row prints the value it read and its length; the sweep prints each bullet
  naming no base.
- risks — the walk's rewire moves the anchors of two red copies, which S7 restages, so a stale
  anchor reads as a FAIL row and never as a pass.
- testing — the probes of §6 and the arm of §7.
- migration — none: every surface is new in this build.
- user docs — none: no user-facing behaviour changes.

## 6. Acceptance criteria

`sec`, `bullet` and `entries` are §4's readers, a `<unit>` operand naming that unit's spec. The
fixture is spec 55's §4 Evidence fixture, built by the probe under `%TEMP%` and not held in the tree.

- **AC2** — When the oracle, §4's block, runs in that fixture on this slug's earlier landing with the
  fixture's later base, a base taken after the landing, it prints `version oracle: no prepared merge
  on HEAD` and exits 2; with the landing's first parent as the fixture's base it prints a header
  naming the landing's `^1..^2` range.
  Red when: the row is read only under the base that makes it pass.
- **AC3** — When §4's live sweep runs over `memory/builds/dPlacedRequest/spec/`, it prints nothing;
  over a scratch copy of the folder in which `sed` respells `fixture's base` as `a base` in this
  spec's AC21, it prints that bullet.
  Red when: a criterion that runs the oracle names no base it passes.
  fixture: the scratch copy is made under the run's scratch directory.
  figure: the hit set DERIVED at observation.
- **AC7** — When `grep -nE 'index\([^,)]*, *(s|": "|":")\)' tools/unattended/unattended.sh` runs, it
  prints one line, between `CLAIM_KV_AWK='` and its closing quote; `read_claims`, cut by
  `awk '/^read_claims\(\)/{f=1} f; f&&/^}/{exit}'`, names `$CLAIM_KV_AWK` twice and holds no
  `/^renews:`; and over a scratch copy of the driver whose walk adds `p = index(s, ": ")`, the grep
  prints two lines. The `DPR59 AC7` rows print §4's list, `live|4` for the CRLF row, and the
  `DPR46 AC3` loop, its two new tips and the `DPR52 AC25 AC26` and `DPR56 AC22` rows read as §4
  states.
  Red when: a second split of the claim body grammar stands beside the first, or the shared reader
  parses a line otherwise than the read it took over.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC13** — When `sec` reads two frozen sections, 52's `### The oracle` and 54's
  `### The oracle's head`, neither read holds `git rev-list`. Each of the two specs carries exactly
  one heading that its prefix opens. Over 54 at rev-3, `git show 6df7a970:<path>`, the read of the
  head section holds `git rev-list` once. `grep -lE '^t=\$\(git rev-list'` over the specs neither
  CLOSED nor WONTDO prints this spec alone.
  Red when: the version check is stated in two places, or a section read stops at its heading line.
- **AC18** — When `grep -cF 'msg="merge: $SLUG — land onto '` runs over `tools/push-main.sh`, it
  prints 1, and over a scratch copy of the lander whose `msg=` line names another subject, it prints
  0. The section `sec 59 '### The one version oracle'` holds `"merge: dPlacedRequest — land onto "*`.
  Red when: the lander's subject changes and the copy the check matches is not told.
- **AC20** — When
  `awk '/THE REQUEST RACE, PLACED/{f=1} f; f&&/^rm -rf "\$LF"$/{exit}' tools/unattended/unattended.test.sh`
  cuts the race block, its loop holds `pr_e0=0; [ ! -f "$pr_hl" ] ||` and
  `pr_broke=0; [ ! -f "$pr_hl" ] ||`, each after the loop's test of `$pr_h/once`, unit 58's
  absence check.
  Red when: an absent log aborts or misreads a correct race.
- **AC21** — When the oracle, §4's block cut from its fence, runs in that fixture with the fixture's
  base and a stub `git` first on `PATH` whose `merge-base` alone exits 128, it prints
  `version oracle: the ancestor test failed` and exits 2, where spec 56's block under the same stub
  exits 1. With the fixture's base and the real `git` it prints what each of spec 55's AC1 to AC5
  and spec 56's AC6 names; with the empty string and with
  `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef` as the fixture's base it prints
  `version oracle: base does not resolve` and exits 2. In `sec 59 '### The one version oracle'`,
  `[ "$own" = 0 ]` sits on a line before `merge-base --is-ancestor`.
  Red when: an errored ancestor test reads as this build's own merge.
  fixture: the stub's directory enters `PATH` as a POSIX path, as spec 55's §4 Evidence records.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC7 · the `DPR59 AC7` rows staged against scratch driver copies without `sub(/\r$/, "", line)`, which reads live and a CR, with the loose trim's class cut to a space, which reads the tab row as a blank, and with `CLAIM_KV_AWK` renamed, which prints the lift's FAIL line · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` move by the rows gained · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is the lander's subject tied to the oracle's copy (S18)?** (a) A criterion grepping
  `tools/push-main.sh` for the form the oracle matches; (b) a shared prefix the lander and the oracle
  both read. (b) changes how the lander names the merge, which unit 54 §3 keeps out. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's fallback fix judged sound. widens: none · relaxes:
  none
- **F2 — How do the two claim-line readers stay one (S7)?** (a) One awk function text both programs
  prepend; (b) restated prose citing the strict reader, as 56 S22 had it. (b) is the drift the
  finding names. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix
  for finding 14, on the `TASK_OPEN_AWK` seam. widens: none · relaxes: none
- **F3 — What becomes of an item that edits a CLOSED spec?** (a) A product change still owed is built
  and observed, and a text-only finding is resolved in §4 naming P19; (b) the closed spec is edited
  with a rev bump; (c) the item is dropped unrecorded. (b) rewrites built work; (c) loses the fact.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; P19 freezes every unit
  these minors land on, and §1's kinds table sorts each item by what the tree holds. widens: none ·
  relaxes: none
- **F4 — Are the amendments units 61 to 64 order to this spec made at their passes or now?** (a) Now,
  once, in this text, each ordering unit reduced to observing it; (b) at each pass, by a builder.
  (b) has a builder write a spec, which no builder does. Recommendation: (a). RESOLVED (agent,
  2026-11-20, delegated): (a), rung 3; this spec is DEFERRED, so each amendment is a spec act the
  re-grounding makes once, as the brief's fold rule names. widens: none · relaxes: none
- **F5 — Where does the oracle with the ancestor status captured live, so the close runs one?** (a)
  In this spec's §4, whole, naming spec 56's block superseded and never edited; (b) a one-line patch
  here the close applies to spec 56's block; (c) spec 56's block edited. (b) makes the close assemble
  two texts; (c) rewrites a CLOSED spec. Recommendation: (a). RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; with 61's S13 and S20 folded here, and 63's S11 and 64's S19 already true
  of the block, this unit is the last of the five to correct it. widens: none · relaxes: none
- **F6 — Which readers does `CLAIM_KV_AWK` serve (S7)?** (a) The two finding 14 names, the record
  read and the walk of `read_claims`; (b) those and every other hand read of the claim grammar in the
  driver. (b) widens a minors item to a class, which the closing review's left-shift owns.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the approved fix names
  two readers, and §3 names the others so the left-shift reads them. widens: none · relaxes: none
- **F7 — How does the walk's mode split, now that unit 52 built its `renews:` read (S7)?** (a) At the
  first colon, the value trimmed of blanks, as the built walk reads; (b) rev-6's strict split with a
  bare-key branch. (b) reads `renews:` plus a tab and a value as no key, a renewing beat, where the
  built walk reads the value. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a),
  rung 3; the shared reader must parse each line as the read it takes over did. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-5 promotions' 8 MEDIUM
  and 13 LOW findings.
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edges to `TOOL-dPlacedRequest-62` and `TOOL-dPlacedRequest-63`, mirroring their consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.
- rev-5 · 2026-11-19 · §7 · the spec-token checker's guards join, run over this spec by the
  spec stage: §7 also names `scratch-guard self-test` and `tier2-review self-test`, the legs that join
  names for `tools/unattended/unattended.sh` in Files touched, as units 61 and 63 carry them.
- rev-6 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-7 · 2026-11-20 · §1 · §2 S1 to S21 · §3 · §4 · §5 · §6 AC2 AC3 AC7 AC13 AC18 AC20 AC21 · §7 ·
  §8 F2 to F7 · §10 · re-grounded by
  `2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief`: every unit the minors land
  on is CLOSED, so no item edits a spec (F3) and §1 sorts the items by kind; the amendments of units
  61 to 64 made here once (F4), among them `TOOL-dPlacedRequest-62`'s AC13 and section form; §4
  carries the one version oracle whole, spec 56's block with the ancestor status captured, naming it
  superseded (F5); S7 re-grounded on both programs of `read_claims` (F6, F7); the inventory is the
  live sweep; §1's count of review items corrected to four; the criteria of closed items taken out
  with them; line citations swapped for symbol citations and blob pins, and the build method's
  section for its alias tag.

## 10. Reuse audit

The seams extended: the one-text awk program `tools/unattended/unattended.sh#TASK_OPEN_AWK`'s shape
for `CLAIM_KV_AWK`; `slice_fn` in `tools/unattended/unattended.test.sh`, given a variable mode rather
than a sibling; spec 56's §4 oracle, kept whole but for its ancestor test; spec 55's fixture and
PATH-stub `git`; unit 57's base read; and the copies of the `TOOL-dPlacedRequest-47` block's
`${oc_src/…/…}` seam for the restaged reds. The brief's named seam, the governance-ref factory
`tools/unattended/unattended.sh#write_gov_ref`, writes refs, and this unit writes none.
`python tools/codebase-map/reuse_lookup.py "one awk function splitting a claim commit body key value
line shared by two readers"`, run 2026-11-20, ranked `read_text`, `read`, `key` and `claims`, name
stems only, none a body-line reader: no existing seam fits beyond `TASK_OPEN_AWK`'s shape.
`python tools/memory-recall/query.py "re-ground a deferred minors batch whose amendments to sibling
specs fold into one spec and whose target specs are closed"` with the terms below returned the
minors batches of dKeptSession and aDistilledCharter and unit 56's re-grounding; none disagrees
with source.

Recall terms used: re-ground deferred minors batch fold closed spec P19 frozen superseded oracle CLAIM_KV_AWK read_claims slice_fn
