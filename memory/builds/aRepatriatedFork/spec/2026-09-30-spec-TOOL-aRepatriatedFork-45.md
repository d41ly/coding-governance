# TOOL-aRepatriatedFork-45 — a renamed-away filename is a dead-path needle

**Status:** CLOSED · rev-2 · 2026-09-30 · node a · Tier-1 · base 6830f257 · streams tooling · order 15 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-build-TOOL-aRepatriatedFork-45-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-45-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-prompt-TOOL-aRepatriatedFork-45-build-brief.md](../prompts/2026-09-30-prompt-TOOL-aRepatriatedFork-45-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-dead-paths.sh` builds its needles from `git log --diff-filter=D`, and git records a
`git mv` as a rename, so the old name of a renamed file is never a needle. `TOOL-aRepatriatedFork-44`
measured it: after renaming the adopter receipt fixture, a planted citation of the old basename in
`tools/push-main.sh` exited 0. This unit makes the source name of a rename a needle too.

## 2. Scope (IN)

- **S1** — The needle derivation takes the SOURCE path of every rename row that
  `git log --diff-filter=R --name-status` reports, when that path lies outside `memory/`, and joins
  its basename to the deletion set before the tracked-basename subtraction. The tail rule and the
  tracked-suffix filter then apply to it unchanged. Observed by AC1, AC2, AC3.
- **S2** — The rename half carries its own frozen sentinel, `parallel-coding-governance.template.md`:
  the v3.0 product template's old name, reachable only through a rename. Its absence from the
  rename half's own basenames, read before the union, refuses as the deletion sentinel does. Read
  there so a deletion of the same name could never mask an empty rename read. Observed by AC4.
- **S3** — The gate's "what it does not catch" paragraph states the `memory/` rename exclusion and
  git's rename threshold. Observed by AC5.
- **S4** — The self-test's fixture base records a rename in its history, and its header no longer
  says a fixture must never `git mv`. Three arms join it, listed in §7. Observed by AC6.

## 3. Non-goals (OUT)

- Renames whose SOURCE sits under `memory/`. Those are records re-filed, and the one such basename a
  file outside `memory/` still spells, `BACKLOG.md`, is an adopter's live backlog name (§8 F1).
- Prose carriers that describe a renamed file without spelling its name. The gate already states
  that it matches filenames only.
- Rewriting the carriers under `memory/`, which the gate's haystack excludes by rule.

### Edges

none

## 4. Design

### Evidence

Measured at `6830f257` with the gate's own pipeline run over a union of the two sets:

- The deletion half yields 26 basenames and today's needle set holds 24.
- Rename rows name 154 source basenames. With every rename source included, 110 basenames join the
  gone set, and 14 lines outside `memory/` then hit, all spelling `BACKLOG.md`. They are the
  recall kit's documented definition home and its suites' fixture layouts, so none is a dead path.
- With sources under `memory/` excluded, 8 needles join the set:
  `2026-07-12-tier2-cumulative-main.md`, `conf.template`, `incms-2cff5855.receipt.json`,
  `make_incms_receipt.py`, `manifest-ratchet-build-report.md`, `orient.agent.template.md`,
  `parallel-coding-governance.template.md` and `process-monitor.conf.template`. None of the 8 hits a
  line outside `memory/`, so the gate stays green on the real tree with no waiver row added.

### Mechanism

The existing `deleted_base` assignment keeps its pipeline. A second read,
`git log --diff-filter=R --name-status --pretty=format: -- .`, keeps column 2 of each row whose path
does not start with `memory/`. Both are reduced to basenames, and the union replaces `deleted_base`
as the input of the `gone` subtraction. A rename whose content also changed past git's similarity
threshold is recorded as a delete plus an add, so the deletion half already covers it.

### Inventory

This unit mints one shell variable for the rename half, `renamed_base`, and one sentinel constant
beside `SENTINEL`, `RENAME_SENTINEL`. `.lexicon.conf` declares no shell-variable cell, so
`--suggest --as sh.function` answers a function-verb scoping question that does not apply to either.
Both names follow the siblings they sit beside, `deleted_base` and `SENTINEL`.

### Files touched (estimate)

- `tools/check-dead-paths.sh`
- `tools/check-dead-paths.test.sh`

### Alternatives rejected

- Every rename source, `memory/` included. It adds 14 hits that are not dead paths, and each would
  need a row in a waiver registry whose header says its count may only fall (§8 F1).
- `git log --no-renames --diff-filter=D`. It is one flag, but it turns every rename under `memory/`
  into a deletion as well, which is the option above.

## 5. Production-readiness checklist

- security — none; a read-only gate over tracked text.
- perf / scale — one more `git log` over the same history. The deletion read already walks it.
- error / empty / loading states — an empty rename half refuses through its sentinel, and an empty
  union still refuses as it does today.
- observability — the clean line already prints the needle count, which moves from 24 to 32.
- risks — a needle that is a real name in some adopter's layout. The `memory/` exclusion removes the
  one measured case, and the gate stays exempt from shipping.
- testing — AC1 to AC6.
- migration — none. The gate ships nowhere, so no kit version moves.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-dead-paths.sh --needles` runs on the built tree, it prints
  `incms-2cff5855.receipt.json` and `make_incms_receipt.py`, and does not print `BACKLOG.md`.
  Red when: a rename source outside `memory/` is missing from the set, or a `memory/` source joins it.
  figure: 32 needles, PINNED at `6830f257` by the emulated pipeline in §4.
- **AC2** — Red-first control: a line citing `incms-2cff5855.receipt.json` is planted in the working
  copy of `tools/push-main.sh`. `bash tools/check-dead-paths.sh` exits 1 naming that file, and the same
  plant against the gate as it stands at `6830f257` exits 0. Recorded in the acceptance ledger, then
  discarded.
  Red when: the built gate stays green with the plant in place.
- **AC3** — When `bash tools/check-dead-paths.sh` runs on the clean built tree, it exits 0 with no
  waiver row added to `tools/dead-path-waivers.txt`.
  Red when: a new needle hits a carrier, or the registry grows.
- **AC4** — When a scratch copy of the gate has its rename read emptied, `bash
  check-dead-paths.sh` run from that copy exits 1 naming `parallel-coding-governance.template.md`.
  Red when: it exits 0, so the rename half can go vacuous unseen.
- **AC5** — When the header of `tools/check-dead-paths.sh` is read, its "what it does not catch"
  paragraph names the `memory/` rename exclusion and the similarity threshold.
  Red when: either is absent.
- **AC6** — When `git grep -n 'never .git mv.' -- tools/check-dead-paths.test.sh` runs, it prints
  nothing, and the suite's `FLOOR_ASSERTIONS` is 3 higher than at `6830f257`.
  Red when: the old header survives, or the floor did not move with the new arms.

## 7. Gates

`dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/check-dead-paths.test.sh` · a fixture commit that renames a file away and a carrier
naming the old basename · `FLOOR_ASSERTIONS` rises by 3

The three arms are: red on a renamed-away basename carried outside `memory/`; green on a basename
renamed away from under `memory/` and cited outside it; and a refusal when the rename sentinel is
absent from the fixture's history.

## 8. Open questions

- **F1 — which rename sources become needles?** Option (a): every rename source. Fourteen lines
  outside `memory/` then spell `BACKLOG.md`, an adopter's live file name, and each needs a waiver row
  in a registry whose header says its count may only fall. Option (b): sources outside `memory/`
  only, mirroring the haystack's own exclusion. Eight needles join, none hits, and the evidence case
  is caught. Option (c): every source, with `BACKLOG.md` special-cased by name. That is a per-name
  list, which the gate's header rejects as the shape that turns it into a waiver form.
  Recommendation: (b). It catches the class `TOOL-aRepatriatedFork-44` measured with no false
  positive, and (a) books fourteen non-defects as defects.
  RESOLVED (agent, 2026-09-30, delegated): (b). Under M3, (a) satisfies no criterion (b) does not,
  and it leaves fourteen false hits open.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, adopted under the unattended protocol §11 from
  `TOOL-aRepatriatedFork-44`'s rev-2 measurement.
- rev-2 · 2026-09-30 · before code: §4 Inventory names the two identifiers, since the lexicon has no
  shell-variable cell to suggest them from. S2 reads the rename sentinel from the rename half before
  the union, so the deletion half cannot mask an empty rename read.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive dead filename needles from git rename history"`
ranked `git`, `derive_scope` and other name-stem matches, none of which derives needles. The probe
reports `.sh` as an unscanned layer, so it cannot see the seam. The map's install-prefix dossier
names it: `tools/check-dead-paths.sh`, "extend by widening the haystack; the sentinel is what stops
it going quietly vacuous". This unit widens the needle half by the same rule and gives the new half
its own sentinel.

Recall terms used: `dead-path needles deletion diff-filter rename sentinel carrier waiver basename
tail vacuous`, with the question "why does the dead-path gate derive its needles from deletions only
and not renames". The top hits were `TOOL-dHonouredPark-3`, the waiver keying, and
`TOOL-aRepatriatedFork-44`'s rev-2 line, which is this unit's evidence.
