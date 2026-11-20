# TOOL-dPlacedRequest-44 — the version-bump oracle walks the build's side of the prepared merge

**Status:** CLOSED · rev-9 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 25 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-deviation-441.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-deviation-441.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-44-deviation-442.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-deviation-442.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-44-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-44-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-44-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-44-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief.md) | research | TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 26 at BLOCKER**, its item **B1**, which holds no other finding. The same defect
is reported by finding 21 (item H1, HIGH), which `TOOL-dPlacedRequest-45` closes, and the old oracle
left beside it is finding 5 (item M2), an item of `TOOL-dPlacedRequest-49`. The defect was the
version-bump oracle `TOOL-dPlacedRequest-43` first wrote, a `git log --first-parent` walk run on the
prepared merge. `tools/push-main.sh#cmd_prepare` merges the run branch onto the advertised tip, first
parent that tip, so a first-parent walk from the merge reads the default branch and no commit of the
build, and certifies "no hand-bump" without reading one.

Spec 43 rev-11 folded this unit's old S3 before its build (its F6): its S24 and AC24 run this unit's
oracle, its text holds no first-parent walk, and it is CLOSED. The charter's P19 keeps it as built.
What this unit owns is the oracle itself. No tool in the tree refuses a hand-bumped version, so
the oracle lives as this spec's §4 command and runs once, at the close, on the prepared merge, as the
observation spec 43's AC24 names (F2). It names the parent it walks, says what it read, and refuses
an empty walk.

## 2. Scope (IN)

- **S1** — The range. The oracle reads the build's own commits, merges and `mint:` commits outside
  both the count and the walk. When HEAD's subject begins `merge: dPlacedRequest — land onto`, the
  message `tools/push-main.sh#cmd_prepare` writes and `tools/push-main.sh#write_merge_fold` keeps
  when it rewrites the merge over the mint, it walks `HEAD^1..HEAD^2`, the second parent's side. On
  any other HEAD it walks `$(git merge-base origin/main HEAD)..HEAD`. No form of it walks
  `--first-parent`. Observed by AC1 and AC2.
- **S2** — The walk is stated and never empty. The oracle first prints `version oracle: <range> · <n>
  commits`, `<n>` being `git rev-list --no-merges --invert-grep --grep='^mint:' --count <range>`;
  when `<n>` is 0 it prints `version oracle: walked no commit of the build` and exits 1. Its verdict
  is the lines after the header: a `KIT_` version line is a hand-bump, and none is a clean build. It
  lives as the §4 block and runs at the close on the prepared merge (F2). Observed by AC1 and AC3.
- **S3** — One oracle in the spec set, an observation. Spec 43 rev-11 carries it already: its text
  holds no `first-parent`, and its AC24 runs this unit's §4 oracle. This unit writes nothing into
  spec 43. Observed by AC4.

## 3. Non-goals (OUT)

- No edit to spec 43 or to `TOOL-dPlacedRequest-34` AC59: both specs are CLOSED, and finding 5's
  item of `TOOL-dPlacedRequest-49` points AC59 at this oracle.
- No oracle script and no gate: the oracle is a criterion's command, and no checker executes one
  (F2).
- No exit-status contract beyond S2's refusal. A clean walk ends at `grep`, whose no-match status is
  1, so the verdict is read from the printed lines; `TOOL-dPlacedRequest-52` S11 gives the oracle its
  exit contract.
- No bug-class record: finding 21's, `TOOL-dPlacedRequest-45`.
- No change to how `tools/push-main.sh` builds or mints the merge.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-43` — S24 and AC24, which since its rev-11 run this unit's §4 oracle at the close; without them the oracle is observed by no criterion of the build
- **hands-off** `TOOL-dPlacedRequest-49` — the corrected oracle, which that unit's item for finding 5 makes `TOOL-dPlacedRequest-34` AC59 run so one oracle stands
- **hands-off** `TOOL-dPlacedRequest-52` — the oracle, its fixture and AC1, AC3 and AC4, which that unit's items for findings 2, 3, 11, 17, 27 and 29 re-range, re-status and re-scope
- **hands-off** `TOOL-dPlacedRequest-54` — §4's oracle and AC1, which that unit gives the own-merge test and the base argument
- **hands-off** `TOOL-dPlacedRequest-55` — §4's oracle, whose verdict that unit makes read the walk's status
- **hands-off** `TOOL-dPlacedRequest-56` — S2, §4, §5, AC3 and §8 F1, which that unit's items for findings 8, 13 and 14 restate to one oracle contract
- **hands-off** `TOOL-dPlacedRequest-57` — AC1, which that unit gives the observing run's base read
- **hands-off** `TOOL-dPlacedRequest-59` — S1, §4, AC2, AC3 and §8 F1, which that unit's items for findings 5, 10, 16 and 23 restate
- **hands-off** `TOOL-dPlacedRequest-61` — AC1 and §4's oracle as units 57 and 59 leave them, which that unit's items for findings 5, 14 and 22 amend
- **hands-off** `TOOL-dPlacedRequest-63` — §4's oracle as unit 61 leaves it, which that unit's item for finding 21 gives the base refusal
- **hands-off** `TOOL-dPlacedRequest-64` — §4's oracle as units 61 and 63 leave it, whose base refusal that unit's item for finding 23 tries with a second input class

## 4. Design

### The oracle

```bash
case "$(git log -1 --format=%s HEAD)" in
  "merge: dPlacedRequest — land onto "*) r='HEAD^1..HEAD^2' ;;
  *) r="$(git merge-base origin/main HEAD)..HEAD" ;;
esac
n=$(git rev-list --no-merges --invert-grep --grep='^mint:' --count "$r")
echo "version oracle: $r · $n commits"
[ "$n" -gt 0 ] || { echo "version oracle: walked no commit of the build"; exit 1; }
git log --no-merges --invert-grep --grep='^mint:' -p "$r" \
  -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh \
  | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='
```

A clean build prints the header line and nothing after it.

### Where the oracle lives and runs

- It lives here, as the block above. No tool in the tree refuses a version a branch commit moved:
  `tools/govkit/govkit.py#cmd_mint` and the epoch rule beside it read the other direction, shipped
  bytes moved with no bump dating the move, and the lander mints that bump, so a branch owes none.
  Spec 43's non-goals leave the oracle to this unit, and its S24 calls this unit's part the
  oracle's text.
- It runs once, at the close. The build README's build-level rules close on the prepared merge after
  `--phase VERIFYING` and the last `push-main.sh --prepare`, so HEAD is the merge and the subject arm
  takes `HEAD^1..HEAD^2`. The close may commit its departures record on top of the merge; HEAD's
  subject is then not the merge's, and the merge-base form reads the same side while `origin/main`
  is the merge's first parent (Evidence).
- The mint stays outside the walk. `tools/push-main.sh#cmd_prepare` runs `run_minter "$R" "$oldb"`
  over the merged tree and folds the versions into the merge itself through
  `tools/push-main.sh#write_merge_fold`, which `--no-merges` leaves out. The attended landing's own
  `mint: kit versions onto …` commit (`tools/push-main.sh@72fc2ded:1854`) is left out by the grep.

### Evidence

- `tools/push-main.sh#cmd_prepare` sets `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`,
  runs `git merge --no-ff "$oldb"` from the advertised tip `R`, and prints `R` as the first parent;
  `tools/push-main.sh#write_merge_fold` rewrites it with `-p "$1" -p "$2"`, the same two parents.
- Measured 2026-11-20 in a fixture repository under `%TEMP%`: a base, two branch commits (the first
  bumping `KIT_UNATTENDED_VERSION=1.110` to `1.111`), one main commit after the branch point, and a
  `--no-ff` merge of the branch onto main with the S1 subject. On the merge the oracle printed
  `HEAD^1..HEAD^2 · 2 commits` and both version lines; 2 is PINNED, the two branch commits.
  `git log --first-parent --no-merges --format=%s <base>..HEAD` listed main's one commit alone.
  On the branch tip it took the merge-base form and printed the same lines. On main's tip it printed
  `0 commits` and the refusal, exit 1. With one commit planted on top of the merge it took the
  merge-base form and printed `· 3 commits` and both version lines; 3 is PINNED, two branch commits
  and the planted one.
- Measured 2026-11-20 on this run's branch tip at `555e5923f`: the merge-base form walked 235 commits
  (PINNED) and printed no `KIT_` line, and the block's exit was 1, the status `grep` gives no match.

### Files touched (estimate)

None: the oracle is this spec's text, spec 43 is CLOSED, and the unit's pass records its probes in
its acceptance ledger.

### Alternatives rejected

- **The merge-base form on the prepared merge too.** It reads `origin/main`, a tracking ref that can
  be older than the merge's first parent, while `HEAD^1` is the merge's own record of the tip.
- **A count of walked commits as the only guard.** A first-parent walk counts main's own commit on
  the fixture, so the guard alone passes a wrong parent.
- **A script under `tools/unattended/`.** It ships one build's close-time check to every adopter of
  the kit (F2).

## 5. Production-readiness checklist

- security — none: a read of local history.
- perf / scale — two `git` walks over the build's commits, once at the close.
- error / empty / loading states — an empty walk exits 1, named (S2).
- observability — the header line names the range and the count it read.
- risks — a prepared merge built by hand with another subject takes the merge-base form, which is
  still the build's side while `origin/main` is its first parent; a clean walk exits 1 from `grep`,
  so a reader of the status alone misreads it until `TOOL-dPlacedRequest-52` S11 lands.
- testing — the probes of §6; no suite arm, since the oracle runs once at the close.
- migration — none.
- user docs — none: a criterion's command.

## 6. Acceptance criteria

- **AC1** — When the §4 oracle runs on this build's prepared merge at the close, it prints
  `version oracle: HEAD^1..HEAD^2 · <n> commits` with `<n>` at least 1, and no `KIT_` line.
  Red when: a branch commit hand-bumps `KIT_UNATTENDED_VERSION` or `KIT_RUN_GATES_VERSION`.
  figure: `<n>` DERIVED at observation.
- **AC2** — When the §4 fixture repository is built under `%TEMP%` with the S1 merge subject, the
  oracle prints `HEAD^1..HEAD^2 · 2 commits` and `+KIT_UNATTENDED_VERSION=1.111`, and
  `git log --first-parent --no-merges --format=%s <base>..HEAD` lists the main commit alone.
  Red when: the oracle walks the first parent.
  fixture: built by the probe, not held in the tree.
  figure: 2 PINNED, the fixture's two branch commits.
- **AC3** — When the oracle runs on that fixture's main tip, it prints `walked no commit of the build`
  and exits 1.
  Red when: an empty walk reads as no hand-bump.
- **AC4** — When `grep -c 'first-parent' 2026-10-25-spec-TOOL-dPlacedRequest-43.md` runs, it prints
  0, and the AC24 paragraph of that spec, cut by `awk '/^- \*\*AC24\*\*/{f=1} f&&/^- \*\*AC2[5-9]\*\*/{exit} f'`
  and squeezed by `tr -s '[:space:]' ' '`, names `TOOL-dPlacedRequest-44`.
  Red when: a first-parent oracle stands in spec 43 beside this one.
  figure: 0 PINNED, read 2026-11-20 at `555e5923f`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the oracle is a criterion's command, observed once at the close.

## 8. Open questions

- **F1 — Which side does the oracle walk?** (a) `HEAD^1..HEAD^2` on the prepared merge and the
  merge-base form elsewhere; (b) the merge-base form everywhere; (c) `--first-parent`, as spec 43's S24 first read.
  (c) is the defect; (b) depends on a tracking ref's freshness. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound, with the empty-walk refusal of S2.
  widens: none · relaxes: none
- **F2 — Where does the oracle live and run?** (a) As the §4 block of this spec, run by the closing
  session on the prepared merge as the observation of spec 43's AC24; (b) a script under
  `tools/unattended/`; (c) a script in the build folder. (b) ships one build's check to every
  adopter; (c) is a second copy of the text spec 43 already points at. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; no tool in the tree refuses a
  hand-bumped version, spec 43 rev-11 runs this spec's §4 block by name, and the close rule of the build README
  already puts HEAD on the prepared merge. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  26 (BLOCKER, item B1).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edges to `TOOL-dPlacedRequest-54`, `TOOL-dPlacedRequest-55`, `TOOL-dPlacedRequest-56`, mirroring their consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-57` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-7 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-8 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.
- rev-9 · 2026-11-20 · §1 · §2 S1 S2 S3 · §3 · §4 · §5 · §6 AC2 AC4 · §8 F2 · §10 · re-grounded
  by `2026-11-20-prompt-TOOL-dPlacedRequest-44-order-25-reground-brief`: S3 and AC4 reduced to an
  observation of spec 43 rev-11, whose F6 folded them; the oracle's home and run probed and ruled
  (F2), S1, S2 and §4 amended to `tools/push-main.sh#cmd_prepare` and
  `tools/push-main.sh#write_merge_fold`; the fixture re-measured with its count; line citations
  swapped for symbol citations and one blob pin.

## 10. Reuse audit

The seam extended is the oracle spec 43 S24 runs, review 23's M17 fix, whose
`--no-merges --invert-grep --grep='^mint:'` filter this unit keeps; the merge it reads is the one
`tools/push-main.sh#cmd_prepare` builds. `python tools/codebase-map/reuse_lookup.py "walk the second
parent of a prepared merge for a version bump"`, re-run 2026-11-20, ranked `merge`, `walk`,
`build_walk` and `run_step_walk`, name stems only, none a history oracle; `tools/check-kit-versions.sh`
checks that each version constant is well formed, not who moved it. `python
tools/memory-recall/query.py "which parent does a check on the prepared merge walk"` with the terms
below returned `TOOL-dPlacedRequest-51`, this spec, `TOOL-dTendedCadence-58` (a DEFERRED unit of
another build stating the same population through `tools/push-main.sh#check_prepared_merge`), this
audit's B1 and `TOOL-dPlacedRequest-52`'s oracle sketch; none disagrees with source. A grep of
`memory/gotchas/` found `a-merge-of-the-default-branch-read-as-additions`, whose fix line S1 obeys.

Recall terms used: version bump oracle prepared merge first parent second parent push-main commit-tree mint no-merges invert-grep
