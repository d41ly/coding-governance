# TOOL-dPlacedRequest-54 — the version oracle walks only this build's own prepared merge

**Status:** CLOSED · rev-6 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 28 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-10-25-build-TOOL-dPlacedRequest-54-deviation-541.md](../build/2026-10-25-build-TOOL-dPlacedRequest-54-deviation-541.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-54-deviation-542.md](../build/2026-10-25-build-TOOL-dPlacedRequest-54-deviation-542.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-54-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-54-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-54-deviation-709.md](../build/2026-11-21-build-TOOL-dPlacedRequest-54-deviation-709.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief.md) | research | TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
confirmed **finding 16 at HIGH**, its item **H2**, which holds no other finding. The oracle found
its merge by fact 1 of `tools/push-main.sh#check_prepared_merge` alone,
`git rev-list --first-parent --min-parents=2 --max-count=1 HEAD`, and dropped fact 2, the check of
the merge's first parent against the advertised tip. Every landing leaves a merge on the default
branch's first-parent line, so before `--prepare` that command returns another build's landing, and
the oracle walks its commits, finds no `KIT_` line and reads a clean build without reading one commit
of this one. This unit's fix is the own-merge test: the merge found must be this build's own, or the
oracle refuses with exit 2.

Re-grounded on 2026-11-20 against the tree at `0d700d256` by
`2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief`. Specs 44 and 34 are CLOSED,
and the charter's P19 keeps them as built; unit 52 is DEFERRED. The oracle now has one home, the §4
block of `TOOL-dPlacedRequest-55`, which carries this unit's test whole (that unit's F3). So no item
here edits a spec: unit 52's text took this unit's amendments at its rev-10 (F2), the closed specs'
text is resolved in §4 (F4), and this unit narrows to observing the test on this repository's own
history and in the text that carries it.

## 2. Scope (IN)

- **S1** — The own-merge test, folded. The oracle takes the build's base as its one argument and
  refuses with exit 2 when the base does not resolve, when no merge sits on HEAD's first-parent line,
  when the merge's subject does not begin `merge: dPlacedRequest — land onto `, the `msg`
  `tools/push-main.sh#cmd_prepare` writes, and when `git merge-base --is-ancestor "$t" "$base"`
  succeeds. `TOOL-dPlacedRequest-55`'s §4 block carries it. Left, its observation on this
  repository's history. Observed by AC1.
- **S2** — The foreign shapes staged, folded. Unit 52's AC12 moved with the oracle to unit 55, and
  that unit's AC3 stages this unit's three foreign shapes: another build's landing under a branch
  commit, a merge of the default branch into the branch, and this slug's earlier landing under a
  later base. Observed by AC2.
- **S3** — The close reads the oracle on the prepared merge. Resolved in §4: spec 34's AC59 and spec
  44's AC1 are frozen, and the close runs unit 55's block on the prepared merge with the observing
  run's base. NOT OBSERVED here: spec text only.
- **S4** — One live resolution, folded. Unit 52's §8 F1 names this unit's F1 as superseding its
  "fact-1 derivation alone" pick since 52's rev-10. Observed by AC4.

## 3. Non-goals (OUT)

- No fact 2 in the oracle: it reads the remote's advertised tip, which a fixture lacks and the local
  history check does not need.
- No change to how `tools/push-main.sh` writes or names the merge.
- No change to the walk, its status or its count: unit 55's S2 and finding 8's item of
  `TOOL-dPlacedRequest-56`.
- No base read: `TOOL-dPlacedRequest-57` S1 spells it.
- No edit to spec 34 or 44, each CLOSED (F4).
- No new bug-class record: the closing review's left-shift decides one
  (`doc.build-method#m8-closing-the-build`).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — the oracle's S12, S17, AC12 and F1, whose own-merge amendments this unit made in 52's text at its rev-10; without them 52 keeps a fact-1-only derivation live
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's oracle and AC1, frozen, which unit 55's block supersedes
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59, frozen, whose close-time read §4 resolves to unit 55's block
- **hands-off** `TOOL-dPlacedRequest-55` — the own-merge test and the base argument, which that unit's §4 block carries whole and its AC3 stages
- **hands-off** `TOOL-dPlacedRequest-56` — the own-merge test, which that unit's items for findings 13 and 14 restate across 44, and 34 AC59 cut to one line, after which its item for finding 19 measures unit 34 against its ceiling
- **hands-off** `TOOL-dPlacedRequest-57` — S1, S3, AC1 and AC3, which that unit restates to the observing run's `base:` fact; this unit's pass runs AC1 with that fact, never a sha an earlier run pinned
- **hands-off** `TOOL-dPlacedRequest-59` — S1, §4, §5, AC2, AC3 and Files touched, which that unit's items for findings 2, 6, 8, 10, 15, 21 and 23 amend
- **hands-off** `TOOL-dPlacedRequest-61` — §4's inventory, Evidence and head section as unit 59's pass leaves them, which that unit's items for findings 1, 5, 8, 9, 17 and 18 amend
- **hands-off** `TOOL-dPlacedRequest-63` — §4's inventory, excluded sub-table and Evidence as unit 61 leaves them, and AC1, which that unit's items for findings 1, 2, 9 and 23 amend
- **hands-off** `TOOL-dPlacedRequest-64` — the no-merge fixture, which that unit's item for finding 23 runs with an absent sha as the base

## 4. Design

### The oracle's head, where it lives

The test is the head of `TOOL-dPlacedRequest-55`'s §4 block, "The oracle the close runs": the base
check, fact 1, the subject read of `$t` (never of HEAD), and the ancestor test, ahead of the range
`$t^1..$t^2`. This spec carries no copy, so the close runs one oracle.

The ancestor test rejects every merge the build started on top of, an earlier landing of this same
slug included. The subject test rejects a merge made on the branch after the base, which the
ancestor test cannot see.

### The folds into unit 52 (F2)

Made in unit 52's text at its rev-10, once: its S12 and S17 name unit 55's block and its own-merge
test, its AC12 moved with the oracle to unit 55's AC3, and its F1 names this unit's F1 as
superseding. Unit 52's oracle fixtures went with them.

### The closed specs' text (S3, F4)

The closing mechanism is P19: a CLOSED spec is a frozen record. Spec 34's AC59 keeps the form its
acceptance ledger observed, and spec 49's S3 records that the close runs one oracle; spec 44's AC1
runs spec 44's block. Unit 55's §4 names that block superseded, so the close runs unit 55's block,
on the prepared merge after the last `--prepare`, with the observing run's base.

### Evidence

- `tools/push-main.sh#check_prepared_merge` derives `t` by fact 1 and rejects a merge whose first
  parent is not the advertised tip by fact 2; `tools/push-main.sh#cmd_prepare` sets
  `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`; read 2026-11-20.
- Measured 2026-10-25 on node a before `--prepare`: fact 1 alone returned `c63aabbb`, dOrderedCharter's
  landing, and the oracle without the test walked it and exited 0. PINNED at that date.
- Measured 2026-11-20 on node a in this worktree at `0d700d256`, with the base the run-state file's
  `## Run facts` section holds, `9e21ac76`: fact 1 returned `9e21ac76`, subject
  `merge: dDeclaredLoop — land onto origin/main at c1f80c00`; unit 55's block printed `version
  oracle: no prepared merge on HEAD` and exited 2, and a copy without the subject and ancestor tests
  walked `9e21ac76^1..9e21ac76^2` and exited 0. The landings `60d90cb71` and `ed2fbc1f2` of this
  slug sit deeper on the default branch's first-parent line. PINNED at that date.
- Measured 2026-10-25 in a fixture under `%TEMP%`: a copy with the ancestor test alone walked the
  default branch's commits through a branch-side merge, and a copy with the subject test alone walked
  an earlier landing of the slug under a later base. PINNED at that date.

### Files touched (estimate)

None: the test is unit 55's text, unit 52's amendments were made at its rev-10, and specs 34 and 44
are CLOSED.

### Alternatives rejected

- **The subject test alone.** It walks an earlier landing of this slug once a later run starts from
  it.
- **The ancestor test alone.** It walks the default branch's commits through a merge made on the
  branch.
- **Fact 2, the advertised tip.** It needs the remote, which the fixtures and a local read lack.

## 5. Production-readiness checklist

- security — none: a read of local history.
- perf / scale — one `rev-parse`, one `log -1` and one `merge-base` more, once at the close.
- error / empty / loading states — each refusal exits 2 with a named line (S1).
- observability — the refusal names what was missing; the header still names the merge walked.
- risks — a prepared merge written by hand with another subject is refused, which is loud; the
  lander writes only `tools/push-main.sh#cmd_prepare`'s subject.
- testing — the probes of §6.
- migration — none: the oracle is a criterion's command.
- user docs — none: criterion text.

## 6. Acceptance criteria

- **AC1** — When `TOOL-dPlacedRequest-55`'s §4 block runs in this build's worktree before
  `--prepare`, with the base `TOOL-dPlacedRequest-57` S1 reads, it prints `version oracle: no
  prepared merge on HEAD` and exits 2; a scratch copy without the subject and ancestor tests prints a
  header naming the merge fact 1 finds and walks it.
  Red when: the oracle walks another build's landing merge and reads it as a clean build.
  figure: the merge fact 1 finds DERIVED at observation; `9e21ac76` on 2026-11-20 PINNED.
- **AC2** — When the AC3 bullet of `2026-10-25-spec-TOOL-dPlacedRequest-55.md` is read, it names the
  three foreign shapes of S2, each expecting `no prepared merge on HEAD`.
  Red when: a merge of the right shape that is not this build's own goes unstaged.
- **AC4** — When the F1 item of `2026-10-25-spec-TOOL-dPlacedRequest-52.md`'s §8 is read, it names
  `TOOL-dPlacedRequest-54` as superseding its pick.
  Red when: 52 keeps a live resolution for the fact-1-only derivation.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the oracle is a criterion's command, observed once at the close.

## 8. Open questions

- **F1 — How does the oracle prove the merge is this build's own (S1)?** (a) The subject test and
  the ancestor test together; (b) the subject test alone; (c) the ancestor test alone; (d) fact 2,
  the advertised tip. (b) and (c) each walked a foreign merge on one measured shape; (d) needs the
  remote. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's two fixes judged sound,
  combined because the measurement rejected each alone. Supersedes `TOOL-dPlacedRequest-52` F1's
  "fact-1 derivation alone". widens: none · relaxes: none
- **F2 — Is an amendment this unit orders to unit 52 made at a pass or now?** (a) Now, once, in 52's
  text and, where the oracle moved, in unit 55's; (b) at unit 52's pass; (c) at this unit's pass.
  (b) and (c) have a builder write a spec, which no builder does. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; unit 52 is DEFERRED, so the amendment is a
  spec act the re-grounding makes once, as the brief's fold rule names. widens: none · relaxes: none
- **F3 — Where does the corrected oracle, this unit's test included, live?** (a) In unit 55's §4,
  the last of the three correcting units, with this spec naming it; (b) in this spec's §4, as the
  head only; (c) in unit 52's §4. (b) splits one block across two specs; (c) is the earliest text.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; ruled whole at unit
  55's F3, so the close runs one block. widens: none · relaxes: none
- **F4 — What becomes of S3's restatement of the closed specs 34 and 44?** (a) Resolved in §4 naming
  P19, the closed text untouched; (b) the closed specs edited with a rev bump; (c) dropped
  unrecorded. (b) rewrites built work; (c) loses the fact. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; P19 freezes a CLOSED spec, and S3 owes no
  product change. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  16 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-57` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.
- rev-6 · 2026-11-20 · §1 · §2 S1 S2 S3 S4 · §3 · §4 · §5 · §6 AC1 AC2 AC4 · §8 F2 F3 F4 · §10 ·
  re-grounded by `2026-11-20-prompt-TOOL-dPlacedRequest-52-orders-27-28-reground-brief`: the test
  lives in unit 55's §4 block (F3) and this spec carries no copy; unit 52's S12, S17, AC12 and F1
  amended in 52's text at its rev-10 (F2), the refusal rows moving with the oracle to unit 55's AC3;
  S3 resolved in §4 and its criterion taken out (F4); AC1 measured on this worktree's own history
  with the run's base, the pinned `c63aabbb` no longer the base; hands-off `TOOL-dPlacedRequest-55`
  added; Files touched now none; line citations swapped for symbol citations and the build method's
  section to its alias tag.

## 10. Reuse audit

The seam extended is the lander's own prepared-merge derivation, fact 1 of
`tools/push-main.sh#check_prepared_merge`, and the subject `tools/push-main.sh#cmd_prepare` writes,
both read by unit 55's block. The brief's named seam, the governance-ref factory
`tools/unattended/unattended.sh#write_gov_ref`, writes refs, and this test writes none.
`python tools/codebase-map/reuse_lookup.py "one version oracle block carried whole where the close
runs it"`, run 2026-11-20, ranked `run`, `run_git` and `run_selftest_cases`, name stems only, none a
merge-ownership test: no existing seam fits beyond the lander the oracle already copies. `python
tools/memory-recall/query.py "where does the corrected version oracle live once the spec that wrote it
is closed"` with the terms below returned this spec, this run's brief and `TOOL-dPlacedRequest-44`;
none disagrees with source.

Recall terms used: prepared merge first-parent foreign landing oracle refusal base ancestor subject lander superseded
