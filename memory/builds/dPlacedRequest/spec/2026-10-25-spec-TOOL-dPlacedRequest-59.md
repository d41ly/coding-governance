# TOOL-dPlacedRequest-59 — the round-5 promotions' minors: every oracle reader passes a base, one claim-line reader, criteria that can fail, and cites by label

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 31 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |
| [2026-10-25-build-TOOL-dPlacedRequest-59-deviation-591.md](../build/2026-10-25-build-TOOL-dPlacedRequest-59-deviation-591.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-59-deviation-592.md](../build/2026-10-25-build-TOOL-dPlacedRequest-59-deviation-592.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |
| [2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`)
exited CONVERGED with 23 confirmed findings. Its two highs are units 57 and 58. This unit is the batch
BUILD-METHOD M4 makes of the rest: 8 MEDIUM and 13 LOW findings by raw id, one scope item per id, each
naming its finding and, in brackets, the review item holding it (M1 to M5, L1 to L10). Five review
items hold more than one id (M1: 8 and 21; M2: 2, 9 and 16; L2: 4 and 11; L5: 7, 12 and 19), and M1
restates H1's defect, which unit 57 closes at HIGH. Each id still gets its own item and its own
observation. The minors land on units 53, 54 and 56 and on the specs and code those units amend, so
this unit repairs none in particular and sits above every unit of the build, at order 31, after unit
58 at 30. Criterion ACn observes item Sn.

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

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries. "The run's base" is unit 57 S1's read of the observing run's `base:`
fact; "the fixture's base" is the base commit of the fixture a criterion builds.

- **S1** — finding 8 (M1). 54 §4's sentence "The ancestor test rejects every merge the build started
  on top of, an earlier landing of this same slug included" is restated to hold when the base is the
  observing run's own pinned BASE, and 54 §4 Evidence's real-tree bullet says the merge found there
  was the base itself, so that measurement did not exercise the ancestor test. Observed by AC1.
- **S2** — finding 21 (M1). 54 AC2 and 52 AC12 read the fifth fixture row, an earlier own landing,
  twice: with the fixture's base taken after that landing it exits 2 `no prepared merge on HEAD`, and
  with the landing's first parent as base it walks the landing's commits. Observed by AC2.
- **S3** — finding 2 (M2). 54 §4 Files touched carries an inventory table of every criterion that
  runs the oracle, one row per criterion naming the base it passes: 43 AC24, 44 AC1 to AC3, 49 S3
  (through 34 AC59 and 44 AC1), 52 AC11 to AC14, AC17 and AC29, 54 AC1 and AC2, 55 AC1 and AC2, 56
  AC6 and AC10, and 57 AC1. Observed by AC3.
- **S4** — finding 9 (M2). 55 AC1 and AC2, 52 AC29 and 56 AC6 and AC10 each name the fixture's base
  as the oracle's argument. Observed by AC4.
- **S5** — finding 16 (M2). 44 AC2 and AC3 name the fixture's base, and 43 AC24 names the run's base.
  Every inventory row expecting exit 2 names the refusal line it expects, so the base refusal fails
  it rather than passing it on status. Observed by AC5.
- **S6** — finding 10 (M3). 44 S1 is restated to the oracle units 52, 54 and 57 leave: fact 1 of
  `check_prepared_merge`, the own-merge test (the lander's subject and `merge-base --is-ancestor`
  against the base argument), and a refusal otherwise. 54 S1's restatement list and its Files touched
  name 44 S1. Observed by AC6.
- **S7** — finding 14 (M4), the skeptic's corrected fix. One reader of a claim commit's body lines: a
  `CLAIM_KV_AWK` text in `tools/unattended/unattended.sh`, the shape `TASK_OPEN_AWK` has (`:8536`),
  holding one awk function that splits a line at its first `: ` and keeps a key's first occurrence
  when the key is in the caller's set. `read_claims`' program (`:2155-2172`) and the age walk's both
  prepend it; `want` and its `ok` completeness check are unchanged, and the walk passes its own keys.
  A bare `key:` line parses to an empty value inside the function for the walk's keys only, which 52
  S26's empty `renews:` needs. 56 S22, §5 and §10 say that `read_claims` does not read `renews`, and
  cite the shared function instead of `:2171`. Observed by AC7.
- **S8** — finding 17 (M5). 56 S11 states the overrun: when unit 34 measures over 48128 after every
  edit S11 names, a size-only cut of 34 brings it under, prose tightened with no item, criterion, edge
  or §9 line dropped, as 34's rev-7 did. 56 §3's "No edit to `TOOL-dPlacedRequest-34`" becomes "no
  edit beyond that cut", and 56 §4 Evidence states the measured size. The cut is made at this unit's
  pass when 56's pass left 34 over. Observed by AC8.
- **S9** — finding 3 (L1). 53 S1 and 52's hands-off edge to 53 each say that 52's pass at order 27
  leaves AC1, AC6 and AC9 to 53's pass, where they are read by 53's occurrence counts. Observed by
  AC9.
- **S10** — finding 4 (L2). 53 AC1 runs 52's rewritten AC1, AC6 and AC9 commands, extracted from 52's
  bullets, over the built 48 and 43, each printing at least 2. Observed by AC10.
- **S11** — finding 11 (L2). 53 AC1's `Red when:` names a break 53's own output can take: a scratch
  copy of 52 whose AC1 bullet keeps `grep -c`, read by the same extraction, prints 1. The scratch
  two-paragraph file stays as that red's fixture. Observed by AC11.
- **S12** — finding 5 (L3). 56 S19 says 44 §8 F1's options (a) and (b) are reworded in place to name
  the rejected forms without the phrases 56 AC10 and AC19 count, as "the `origin/main` tracking-ref
  range", and stay options under F1 beside the (a') resolution. Observed by AC12.
- **S13** — finding 6 (L4). 52 §4 "The oracle" becomes a pointer to 44 §4, its measurement paragraph
  kept, so the oracle is stated once. 54 AC3 also reads 44 AC1 for the base argument. Observed by
  AC13.
- **S14** — finding 7 (L5), the skeptic's corrected fix. 53 AC3's sweep matches the command shape over
  each criterion bullet joined to one line, the §4 sweep, so 53's own prose is not a hit. Observed by
  AC14.
- **S15** — finding 12 (L5). 53 §4 Evidence cites 52's criteria by label, AC1, AC6 and AC9, with no
  line numbers. Observed by AC15.
- **S16** — finding 19 (L5). The same bullet's cite of 49 names 49's AC16 by label, so 53 carries no
  `<unit>:<line>` cite into a sibling spec. Observed by AC16.
- **S17** — finding 13 (L6). 56 §4 Evidence's fourth bullet names 47's S1 and AC1 to AC3 by label with
  no line numbers. Observed by AC17.
- **S18** — finding 15 (L7). 54 gains a criterion that the lander still writes the subject the
  own-merge test matches: `grep -cF 'msg="merge: $SLUG — land onto '` over `tools/push-main.sh`
  prints 1, and 54 §5 risks names it. Observed by AC18.
- **S19** — finding 18 (L8). 56 AC5 reads 48's and 50's Files touched sections joined and squeezed,
  never line by line, by the §4 form. Observed by AC19.
- **S20** — finding 22 (L9). 56 S4 and §4's sketch, as unit 58 leaves it, and the built arm count an
  absent health log as `m = 0`: `m=$( [ -f "$log" ] && wc -l < "$log" || echo 0 )`. Observed by AC20.
- **S21** — finding 23 (L10). The own-merge test captures `merge-base --is-ancestor`'s status: 0
  refuses as `no prepared merge on HEAD`, 1 walks, and any other prints `version oracle: the ancestor
  test failed` and exits 2. Written into 44 §4 and 54 §4's sketch. Observed by AC21.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 57 and 58 own findings 1 and 20. S1, S2, S3 to S5 and S13 read
  the base as unit 57 leaves it, and S20 edits the sketch unit 58 leaves.
- No change to `tools/push-main.sh`: unit 54 §3 keeps the lander's wording out of scope, and S18
  observes it instead.
- No renumbering of any order: S8 and S9 carry their order gaps in text.
- No new gate leg, no lint over spec criteria and no new bug-class record: each arm joins an existing
  suite, and the closing review's left-shift decides any record (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-57` — the run's base read, which S1 to S5 and S13 pass and cite
- **consumes-from** `TOOL-dPlacedRequest-58` — 56 §4's per-attempt sketch and the arm with the handshake reset, in which S20 sets the absent log's count
- **consumes-from** `TOOL-dPlacedRequest-53` — S1, AC1, AC3 and §4 Evidence, which S9 to S11 and S14 to S16 amend
- **consumes-from** `TOOL-dPlacedRequest-54` — S1, §4, §5, AC2, AC3 and Files touched, which S1 to S3, S6, S13, S18 and S21 amend
- **consumes-from** `TOOL-dPlacedRequest-56` — S4, S11, S19, S22, §3, §4, §5, §10 and AC5, which S7, S8, S12, S17, S19 and S20 amend
- **consumes-from** `TOOL-dPlacedRequest-52` — AC12, AC29, §4's oracle and its hands-off edge to 53, which S2, S4, S9 and S13 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — S1, §4, AC2, AC3 and §8 F1, which S5, S6, S12 and S21 amend
- **consumes-from** `TOOL-dPlacedRequest-43` — AC24, which S5 gives the run's base
- **consumes-from** `TOOL-dPlacedRequest-55` — AC1 and AC2, which S4 gives the fixture's base
- **consumes-from** `TOOL-dPlacedRequest-34` — its size, which S8 cuts when unit 56's pass left it over 48128
- **hands-off** `TOOL-dPlacedRequest-61` — §1, §3, S1, S3, S7, S19, S21, §4's sketches, AC1, AC3, AC4, AC5, AC7 and AC13, which that unit's items for findings 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18, 20 and 22 amend
- **hands-off** `TOOL-dPlacedRequest-62` — AC13 as unit 61 extends it, whose clause over 54's head section that unit spells with the section form
- **hands-off** `TOOL-dPlacedRequest-63` — AC3, AC21, S21 and §4's key reader sketch as unit 61 leaves them, and the S7 arm, which that unit's items for findings 1, 4, 7, 11 and 24 amend
- **hands-off** `TOOL-dPlacedRequest-64` — §1, AC3 and AC13 as units 61 and 63 leave them, which that unit's items for findings 2, 3 and 19 correct

## 4. Design

### The sweep (S14) and the joined read (S19)

```bash
# S14: each criterion bullet joined to one line, then the command shape
awk '/^- \*\*AC/{if(b)print b; b=$0; next} /^(- |#|$)/{if(b)print b; b=""; next} b{b=b" "$0} END{if(b)print b}' "$f" \
  | tr -s ' ' | grep -oE 'flat [^|`]*\| grep -c [^`]*`( runs, it)? prints at least [2-9]'
# S19: a Files touched section joined, then the sequence sentence
sed -n '/### Files touched/,/### Alternatives/p' "$f" | tr -s '[:space:]' ' ' \
  | grep -o 'TOOL-dPlacedRequest-[0-9]* writes [^.]*unattended\.test\.sh[^.]*in sequence'
```

### The shared key reader (S7)

```
CLAIM_KV_AWK = function kv(line, keys, v, bare)
  p = index(line, ": ")
  p > 1             -> k = before p;  value = after p + 1
  bare and line ~ /^[a-z-]+:[ ]*$/ -> k = before ":";  value = ""
  (k in keys) and !(k in v) -> v[k] = value with tabs as spaces
read_claims:  awk "$CLAIM_KV_AWK"' … { kv($0, want, v, 0) } …'
age walk:     awk "$CLAIM_KV_AWK"' … { kv($0, walkkeys, w, 1) } …'
```

### The ancestor test's status (S21)

```bash
git merge-base --is-ancestor "$t" "$base"; a=$?
case $a in
  0) echo "version oracle: no prepared merge on HEAD"; exit 2 ;;
  1) ;;
  *) echo "version oracle: the ancestor test failed"; exit 2 ;;
esac
```

### Evidence

- Measured 2026-10-25 on node a: the S14 sweep over `memory/builds/dPlacedRequest/spec/*.md` printed
  three hits, 52's AC1, AC6 and AC9, and none in 53; the review's `grep -n -A1` sweep printed 53's own
  §1 line too. PINNED at that date.
- `tools/unattended/unattended.sh:2170` is the one `index($0, ": ")` split in the file, inside
  `read_claims`, whose `want` is `slug node host session keepalive status lease-utc beat-utc` (`:2168`);
  no line reads `renews` or `seen-utc`. Read 2026-10-25.
- `grep -cF 'msg="merge: $SLUG — land onto '` over `tools/push-main.sh` printed 1, the line at `:880`.
- Unit 34 measured 47782 bytes on 2026-10-25 before this round's mirror edges and 48046 after them,
  82 under 48128, with the §9 lines units 49, 52, 54 and 57 owe it still to come. PINNED at that
  date; S8 re-measures.
- 53 §4 Evidence cites `52:287`, `52:309`, `52:300` and `49:328`; 49's line is in its AC16. Read
  2026-10-25.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/`: the specs of units 34, 43, 44, 52, 53, 54, 55 and 56, each
  edit a rev bump with its §9 line
- `tools/unattended/unattended.sh`: S7's shared reader
- `tools/unattended/unattended.test.sh`: S20 in the placed-race arm

### Alternatives rejected

- **Two batches.** S2, S4, S9, S13 and S20 write 52, and S5, S6, S12 and S21 write 44, across the items
  landing on 53, 54 and 56, so no split gives M6 two disjoint write sets.
- **A shared subject prefix in `tools/push-main.sh` (S18's first fix).** It changes how the lander
  names the merge, which unit 54 §3 keeps out, and moves a shipped kit's bytes for a refusal that is
  already loud.
- **Dropping 53 AC1 (finding 11's alternative).** S10 and S11 make it read 52, which leaves 53 a
  criterion that runs the counts it rewrote.

## 5. Production-readiness checklist

- security — S7 keeps `read_claims`' key set and completeness check, so the strict reader admits
  nothing it refused before; S21 refuses on an ancestor test that errored instead of walking.
- perf / scale — one awk function shared by two programs; one more `case` in the oracle.
- error / empty / loading states — S20 names an absent log's count; S21 names a failed ancestor test.
- observability — S5 makes every exit-2 criterion name the line it expects.
- risks — S8's cut is prose only; a cut dropping a criterion is out of scope by its own text.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — none beyond the specs: no user-facing behaviour changes.

## 6. Acceptance criteria

`flat <file>` is `TOOL-dPlacedRequest-52` §6's. "Extracted" means by the `awk` paragraph form 52 S15
uses, from the item's label to the next label. The oracle fixtures are units 52's and 54's under
`%TEMP%` with a short name.

- **AC1** — When 54's `### The oracle's head` section is extracted to `### Evidence` and squeezed, it
  names `pinned BASE`, and 54 §4 Evidence's real-tree bullet names `the base itself`.
  Red when: a protection is claimed under a base that disables it.
- **AC2** — When the oracle runs on the fifth fixture row with the fixture's later base, it prints
  `no prepared merge on HEAD` and exits 2; with the landing's first parent as base, its header names
  the landing's `^1..^2` range. 54 AC2 and 52 AC12 each name both reads.
  Red when: the row is read only under the base that makes it pass.
- **AC3** — When each criterion bullet of the build's specs is joined to one line and grepped with
  `grep -E 'oracle[^.]*(runs|run )'`, every hit's unit and label appear in 54's inventory table, and
  each row names a base.
  Red when: an oracle-running criterion is missing from the inventory.
- **AC4** — When 55's AC1 and AC2, 52's AC29 and 56's AC6 and AC10 are extracted, each names
  `base`; 55 AC2's oracle run with the fixture's base prints `the walk failed`.
  Red when: a fixture criterion runs the oracle with no base and meets the base refusal.
- **AC5** — When 55 AC2's and 56 AC6's oracle runs omit the base, each prints `base does not
  resolve` and so fails its expected line; with the fixture's base each prints its expected line. 44
  AC2 and AC3 and 43 AC24 each name a base.
  Red when: a criterion passes on the wrong refusal.
- **AC6** — When 44's S1 paragraph is extracted with `awk '/^- \*\*S1\*\*/{f=1} f&&/^- \*\*S2\*\*/{exit} f'`
  and squeezed, it names `is-ancestor` and `land onto`, and 54's S1 names `44 S1`.
  Red when: 44's scope keeps a derivation with no ownership test.
- **AC7** — When `grep -c 'index($0, ": ")' tools/unattended/unattended.sh` runs it prints 1, inside
  `CLAIM_KV_AWK`, and both `read_claims` and the age walk name `$CLAIM_KV_AWK`; 56 §4's duplicate-key
  row and 52 AC26's `renews:` rows print `stale`; 56 S22 names `CLAIM_KV_AWK` and no `:2171`.
  Red when: a second split of the claim body grammar stands beside the first.
- **AC8** — When `gen_build_index.py --write` has rendered after every edit, `wc -c` of unit 34's
  spec prints at most 48128, and 56 S11 names the size-only cut and §3 names `no edit beyond`.
  Red when: a budget criterion reds with no unit allowed to act on it.
  figure: DERIVED at observation.
- **AC9** — When 53's S1 and 52's hands-off edge to 53 are read, each names `order 27` and 53's pass.
  Red when: a repaired criterion's reading pass is left to the builder.
- **AC10** — When 53 AC1's extraction runs 52's AC1, AC6 and AC9 commands over the built 48 and 43,
  each prints at least 2, and 53's AC1 bullet names `2026-10-25-spec-TOOL-dPlacedRequest-52.md`.
  Red when: the criterion reads a fixture of its own instead of the unit it repaired.
- **AC11** — When the same extraction reads a scratch copy of 52 whose AC1 bullet keeps `grep -c`, it
  prints 1, and 53 AC1's `Red when:` names that copy.
  Red when: a criterion is green on the unbuilt tree.
- **AC12** — When 56 AC10's and AC19's counts run over `flat 2026-10-25-spec-TOOL-dPlacedRequest-44.md`,
  each prints 0, and 44's F1 span still holds `(a)` and `(b)`.
  Red when: the record of rejected options is deleted to make a count pass.
- **AC13** — When 52's `### The oracle` section is extracted, `grep -c 'git rev-list'` over it prints
  0 and it names `TOOL-dPlacedRequest-44`; 54's AC3 bullet names `44 AC1`.
  Red when: the oracle is stated in two specs.
- **AC14** — When the §4 sweep runs over `memory/builds/dPlacedRequest/spec/*.md`, it prints nothing,
  and over a scratch copy of 52 with AC1 reverted to `grep -c` it prints one hit.
  Red when: the sweep matches its own spec's prose.
- **AC15** — When `grep -nE '(^|[ (])52:[0-9]+' 2026-10-25-spec-TOOL-dPlacedRequest-53.md` runs, it
  prints nothing, and 53 §4 Evidence names AC1, AC6 and AC9.
  Red when: evidence cites a sibling by a line that moves.
- **AC16** — When `grep -nE '(^|[ (])[1-9][0-9]:[0-9]+' 2026-10-25-spec-TOOL-dPlacedRequest-53.md`
  runs, it prints nothing, and 53 §4 Evidence names 49's `AC16`.
  Red when: any sibling cite by line number remains.
- **AC17** — When `grep -o '47 now holds[^.]*' 2026-10-25-spec-TOOL-dPlacedRequest-56.md` runs, its
  output holds no `:` followed by a digit and names `AC1`.
  Red when: the correction of a moved cite is itself a moved cite.
- **AC18** — When 54's new criterion runs over `tools/push-main.sh` it prints 1, and over a scratch
  copy whose `:880` reads another subject it prints 0.
  Red when: the lander's subject changes and the oracle's copy is not told.
- **AC19** — When 56's AC5 runs the §4 joined read over 48 and over a scratch copy of 48 whose
  sequence sentence wraps between `run in` and `sequence`, both print one match naming
  `TOOL-dPlacedRequest-50`.
  Red when: a correct wrap makes the criterion print nothing.
- **AC20** — When 56's placed-race arm runs its first attempt on a fresh clone with no health log, it
  reaches the hold with `m` at 0, and 56 S4 names the absent log.
  Red when: an absent log aborts or misreads a correct race.
- **AC21** — When the oracle runs on 54's prepared-merge fixture with a PATH-stub `git` whose
  `merge-base` alone exits 128, the stub shape of 55 AC2, it prints `the ancestor test failed` and
  exits 2; the head as unit 54 writes it walks the merge.
  Red when: an errored ancestor test reads as this build's own merge.
  fixture: the stub's directory enters `PATH` as `/c/…`, as 55 §4 Evidence records.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC7 AC20 · the shared reader's duplicate-key and bare-key rows and the absent-log attempt, staged against the walk's own line reader and an arm that reads `wc -l` of a missing file · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is the lander's subject tied to the oracle's copy (S18)?** (a) A criterion grepping
  `tools/push-main.sh` for the form the oracle matches; (b) a shared prefix the lander and the oracle
  both read. (b) changes how the lander names the merge, which unit 54 §3 keeps out. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's fallback fix judged sound. widens: none · relaxes:
  none
- **F2 — How do the two claim-line readers stay one (S7)?** (a) One awk function text both programs
  prepend; (b) restated prose citing the strict reader, as 56 S22 has it. (b) is the drift the
  finding names. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix
  for finding 14, on the `TASK_OPEN_AWK` seam. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-5 promotions' 8 MEDIUM
  and 13 LOW findings.
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edges to `TOOL-dPlacedRequest-62` and `TOOL-dPlacedRequest-63`, mirroring their consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new code reuses three seams: the one-text awk
program `TASK_OPEN_AWK` (`tools/unattended/unattended.sh:8536`) for S7's shared reader, unit 57's base
read for S1 to S5, and 55 AC2's PATH-stub `git` for S21. `python tools/codebase-map/reuse_lookup.py
"one awk function splitting a commit body key value line shared by two readers"` ranked `read`,
`read_text` and `key`, name stems only, none a body-line reader: no existing seam fits beyond
`TASK_OPEN_AWK`'s shape. `python tools/memory-recall/query.py "how is a spec audit's minor findings
batch promoted into one unit that amends several specs"` returned TOOL-aDistilledCharter-7,
TOOL-aGraftedHelix-32 and -36, `TOOL-dPlacedRequest-56` and `TOOL-dPlacedRequest-52`, batches of the
same kind; none disagrees with source.

Recall terms used: minors batch promote medium low spec audit round finding item amend in place edge mirror
