# TOOL-dPlacedRequest-54 — the version oracle walks only this build's own prepared merge

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 28 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-10-25-build-TOOL-dPlacedRequest-54-deviation-541.md](../build/2026-10-25-build-TOOL-dPlacedRequest-54-deviation-541.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
confirmed **finding 16 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-52` S17 finds the oracle's merge by fact 1 of `check_prepared_merge` alone,
`git rev-list --first-parent --min-parents=2 --max-count=1 HEAD` (`tools/push-main.sh:516`), and
drops fact 2, the first-parent check against the advertised tip (`:521-526`). Every landing leaves a
merge on the default branch's first-parent line, so on this build's branch before `--prepare` that
command returns `c63aabbb`, dOrderedCharter's landing merge. The oracle walks its two foreign
commits, finds no `KIT_` line and exits 0. `TOOL-dPlacedRequest-34` AC59 is read "before the lander's
mint", so it goes green without reading one dPlacedRequest commit, and 52 AC12's fixture holds no
merge at all, so the shape the real tree always presents is never staged. This unit repairs
`TOOL-dPlacedRequest-52`, at order 27, so it sits at order 28: the oracle proves the merge it found
is this build's own, and refuses with exit 2 otherwise.

## 2. Scope (IN)

- **S1** — The own-merge test. The oracle takes the build's base as its one argument and refuses
  with exit 2 in three named cases. A base that does not resolve to a commit prints `version oracle:
  base does not resolve`. A found merge `$t` is this build's own only when its subject begins `merge:
  dPlacedRequest — land onto ` (the `msg` `tools/push-main.sh:880` writes) and `git merge-base
  --is-ancestor "$t" "$base"` fails; no merge, or one failing either test, prints `version oracle: no
  prepared merge on HEAD`. The test is written into the oracle where unit 52 left it: 44 §4, and
  52's §4 sketch, S12 and S17 are restated to it, S17's "no subject match on HEAD" kept, since the
  subject read is `$t`'s and never HEAD's. Observed by AC1 and AC2.
- **S2** — The foreign shapes staged. 52 AC12 gains three rows, each expecting `no prepared merge on
  HEAD` and exit 2: another build's landing merge on HEAD's first-parent line under a plain branch
  commit; a merge of the default branch into the build branch, whose subject is git's own; and this
  build's earlier landing merge under a base taken after it. 52's oracle fixtures (S14, AC11, AC13,
  AC17) write the lander's subject on their merge and pass their own base commit. Observed by AC2.
- **S3** — The close reads the oracle where it is true. `TOOL-dPlacedRequest-34` AC59 is restated in
  place as one line pointing at 44 AC1: the oracle run with base `c63aabbb` on the prepared merge
  after the last `--prepare`, header line, exit 0, no `KIT_` line. 44 AC1 names the base argument.
  Observed by AC3.
- **S4** — One live resolution. 52 §8 F1 is amended in place to name this unit's F1 as superseding
  its "fact-1 derivation alone" pick, and 52 and 34 each take a rev bump with its §9 line naming this
  unit. Observed by AC4.

## 3. Non-goals (OUT)

- No fact 2 in the oracle: it reads the remote's advertised tip, which a fixture lacks and the local
  history check does not need (52 F1's reason, kept).
- No change to how `push-main.sh` writes or names the merge.
- No change to the walk itself, its status or its `--` guards: `TOOL-dPlacedRequest-55` and finding
  8's item of `TOOL-dPlacedRequest-56`.
- No new bug-class record: the closing review's left-shift decides one (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — the oracle's S12, S17, §4 sketch, AC12, its fixtures and F1, which this unit restates so the merge found must be this build's own; without them there is no derivation to correct
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's oracle and AC1, as unit 52 leaves them, which this unit gives the own-merge test and the base argument
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59, which this unit restates as one line pointing at 44 AC1 on the prepared merge
- **hands-off** `TOOL-dPlacedRequest-56` — the own-merge test, which that unit's items for findings 13 and 14 restate across 44, and 34 AC59 cut to one line, after which its item for finding 19 measures unit 34 against its ceiling
- **hands-off** `TOOL-dPlacedRequest-57` — S1, S3, AC1 and AC3, which that unit restates to the observing run's `base:` fact; this unit's pass runs AC1 with that fact, never a sha an earlier run pinned
- **hands-off** `TOOL-dPlacedRequest-59` — S1, §4, §5, AC2, AC3 and Files touched, which that unit's items for findings 2, 6, 8, 10, 15, 21 and 23 amend
- **hands-off** `TOOL-dPlacedRequest-61` — §4's inventory, Evidence and head section as unit 59's pass leaves them, which that unit's items for findings 1, 5, 8, 9, 17 and 18 amend

## 4. Design

### The oracle's head, as this unit leaves it

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
# the rest of the oracle as units 52 and 55 leave it
```

The ancestor test rejects every merge the build started on top of, an earlier landing of this same
slug included. The subject test rejects a merge made on the branch after the base, which the
ancestor test cannot see.

### Evidence

- `tools/push-main.sh:514-526`: `check_prepared_merge` derives `t` by fact 1 and rejects a merge whose
  first parent is not the advertised tip by fact 2. `:880` writes the subject; `:921` writes the merge
  by `commit-tree` with the same `msg`.
- Measured 2026-10-25 on node a in this worktree before `--prepare`: fact 1 alone returned
  `c63aabbb4a73d44315dd5dd1219ff1dac5055cf8`, subject `merge: dOrderedCharter — land onto
  origin/main at cdfbd1cf`; unit 52's §4 oracle as written printed `version oracle:
  c63aabbb^1..c63aabbb^2 · 2 commits` and exited 0; the §4 head run with base `c63aabbb` printed `no
  prepared merge on HEAD` and exited 2. PINNED at that date.
- Measured the same day in a fixture under `%TEMP%` with a short name, five shapes: a foreign landing
  under a branch commit, a default-branch merge into the branch, this build's prepared merge, that
  merge under a stacked commit, and an earlier own landing under a later base. The §4 head refused
  the first, second and fifth with exit 2 and walked `b1` and `bump` on the third and fourth. A copy
  with the ancestor test alone walked the default branch's `m2` on the second shape; a copy with the
  subject test alone walked the earlier landing's commits on the fifth. A base naming no commit
  exited 2. PINNED at that date.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md`: S12, S17, §4, AC11
  to AC14, AC17, F1 and its §9 line. `TOOL-dPlacedRequest-53` and `TOOL-dPlacedRequest-55` write
  this file at the same order, so the three passes run in sequence.
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md`: §4, AC1 and its §9
  line. `TOOL-dPlacedRequest-55` writes this file at the same order, in the same sequence.
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md`: AC59 and its §9 line

### Alternatives rejected

- **The subject test alone.** It walks an earlier landing of this same slug once a later run starts
  from it, measured on the fifth shape.
- **The ancestor test alone.** It walks the default branch's commits through a merge made on the
  branch, measured on the second shape.
- **Fact 2, the advertised tip.** It needs the remote, which the fixtures and a local read lack.

## 5. Production-readiness checklist

- security — none: a read of local history.
- perf / scale — one `rev-parse`, one `log -1` and one `merge-base` more, once at the close.
- error / empty / loading states — each refusal exits 2 with a named line (S1).
- observability — the refusal names what was missing; the header still names the merge walked.
- risks — a prepared merge written by hand with another subject is refused, which is loud; the
  lander writes only `:880`'s subject.
- testing — the probes of §6.
- migration — none: the oracle is a criterion's command.
- user docs — none: criterion text.

## 6. Acceptance criteria

- **AC1** — When the oracle as 44 §4 states it runs in this worktree before `--prepare` with base
  `c63aabbb`, it prints `version oracle: no prepared merge on HEAD` and exits 2; a scratch copy
  without the own-merge test prints a header naming `c63aabbb` and exits 0.
  Red when: the oracle walks another build's landing merge and reads it as a clean build.
- **AC2** — When the five-shape fixture of §4 Evidence is built and the oracle runs on each with the
  fixture's base, the foreign landing, the branch-side merge and the earlier own landing each exit 2
  printing `no prepared merge on HEAD`; the prepared merge and the stacked commit each walk the two
  branch commits; and 52 AC12 names the three refusal rows.
  Red when: a merge of the right shape that is not this build's own is walked.
  fixture: built by the probe under `%TEMP%`, not held in the tree.
- **AC3** — When the AC59 bullet of `2026-10-25-spec-TOOL-dPlacedRequest-34.md` is read, it names
  `TOOL-dPlacedRequest-44`, the base `c63aabbb` and the prepared merge, and carries no `before the
  lander's mint`.
  Red when: the close reads the oracle before the merge it walks exists.
- **AC4** — When 52's §8 is read, F1 names `TOOL-dPlacedRequest-54` as superseding its pick.
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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  16 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-57` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is the lander's own prepared-merge derivation, `check_prepared_merge` in
`tools/push-main.sh:514-526`, whose fact 1 the oracle already copies, and the subject `:880` writes.
`python tools/codebase-map/reuse_lookup.py "prove the newest merge on the first-parent line is this
build's own prepared merge"` ranked `merge` (`tools/memory-tree/merge-rows.py`), `build` and
`build_commit`, name stems only, none a merge-ownership test: no existing seam fits beyond the lander
the oracle already copies. `python tools/memory-recall/query.py "which check proves the prepared merge
it reads is this build's own and not another build's landing"` returned TOOL-dGroundRules-14 (the
landing replay, which reads no merge ownership), this audit's H2, `TOOL-dPlacedRequest-44` and round
4's M9; none disagrees with source.

Recall terms used: prepared merge first-parent foreign landing merge oracle refusal base ancestor subject lander
