# TOOL-dPlacedRequest-44 — the version-bump oracle walks the build's side of the prepared merge

**Status:** OPEN · rev-7 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 25 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-deviation-441.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-deviation-441.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 26 at BLOCKER**, its item **B1**, which holds no other finding. The same defect
is reported by finding 21 (item H1, HIGH), which `TOOL-dPlacedRequest-45` closes, and the old oracle
left beside it is finding 5 (item M2), an item of `TOOL-dPlacedRequest-49`.
`TOOL-dPlacedRequest-43` S24 rewrites the version-bump oracle as `git log --first-parent --no-merges
… c63aabbb..HEAD`, and its AC24 runs that on the prepared merge. `tools/push-main.sh:921` builds the
prepared merge with `git commit-tree … -p "$R" -p "$oldb"`, and `:947` prints the first parent as
"the advertised tip", so a first-parent walk from the merge follows the default branch and reads no
commit of the build. AC24 then prints nothing whatever the branch did: it certifies "no hand-bump"
without reading a build commit. This unit repairs `TOOL-dPlacedRequest-43`, at order 24, so it sits at
order 25: the oracle names the parent it walks, says what it read, and refuses an empty walk.

## 2. Scope (IN)

- **S1** — The range. The oracle reads the build's own commits, merges and `mint:` commits excluded.
  On the prepared merge, a tip whose subject begins `merge: dPlacedRequest — land onto` (the `msg`
  `push-main.sh:880` writes), it walks `HEAD^1..HEAD^2`, the second parent's side. On any other tip
  it walks `$(git merge-base origin/main HEAD)..HEAD`. No form of it walks `--first-parent`.
  Observed by AC1 and AC2.
- **S2** — The walk is stated and never empty. The oracle first prints `version oracle: <range> · <n>
  commits`, `<n>` being `git rev-list --no-merges --invert-grep --grep='^mint:' --count <range>`; when
  `<n>` is 0 it prints `version oracle: walked no commit of the build` and exits 1. Observed by AC1
  and AC3.
- **S3** — One oracle in the spec set. `TOOL-dPlacedRequest-43` S24 and AC24 are rewritten in place, as
  a rev bump with its §9 line, to run this unit's §4 oracle, so no `--first-parent` oracle stands
  beside it. Observed by AC4.

## 3. Non-goals (OUT)

- No edit to `TOOL-dPlacedRequest-34` AC59: finding 5's item of `TOOL-dPlacedRequest-49` points it at
  this oracle.
- No bug-class record: finding 21's, `TOOL-dPlacedRequest-45`.
- No change to how `push-main.sh` builds or mints the merge.
- No machine gate over spec criteria: an oracle is a command a criterion names, and no checker
  executes one.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-43` — S24 and AC24, the oracle this unit re-ranges and rewrites in place; without them there is no oracle to correct
- **hands-off** `TOOL-dPlacedRequest-49` — the corrected oracle, which that unit's item for finding 5 makes `TOOL-dPlacedRequest-34` AC59 run so one oracle stands
- **hands-off** `TOOL-dPlacedRequest-52` — the oracle, its fixture and AC1, AC3 and AC4, which that unit's items for findings 2, 3, 11, 17, 27 and 29 re-range, re-status and re-scope
- **hands-off** `TOOL-dPlacedRequest-54` — §4's oracle and AC1, which that unit gives the own-merge test and the base argument
- **hands-off** `TOOL-dPlacedRequest-55` — §4's oracle, whose verdict that unit makes read the walk's status
- **hands-off** `TOOL-dPlacedRequest-56` — S2, §4, §5, AC3 and §8 F1, which that unit's items for findings 8, 13 and 14 restate to one oracle contract
- **hands-off** `TOOL-dPlacedRequest-57` — AC1, which that unit gives the observing run's base read
- **hands-off** `TOOL-dPlacedRequest-59` — S1, §4, AC2, AC3 and §8 F1, which that unit's items for findings 5, 10, 16 and 23 restate
- **hands-off** `TOOL-dPlacedRequest-61` — AC1 and §4's oracle as units 57 and 59 leave them, which that unit's items for findings 5, 14 and 22 amend
- **hands-off** `TOOL-dPlacedRequest-63` — §4's oracle as unit 61 leaves it, which that unit's item for finding 21 gives the base refusal

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

A clean build prints the header line and nothing after it. A minted version is written into the
merge itself (`push-main.sh:896-902`, "MINT INTO THE MERGE"), which `--no-merges` drops; a `mint:`
commit (`:1092`) is dropped by the grep.

### Evidence

- `push-main.sh:880` sets `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`; `:921` writes
  the merge with `-p "$R" -p "$oldb"`; `:947` names `R` the advertised tip and `oldb` the branch.
- Measured 2026-10-25 on node a, in a fixture repository under `%TEMP%` (a base, a branch commit
  bumping `KIT_UNATTENDED_VERSION=1.110` to `1.111`, one main commit after the branch point, and a
  `--no-ff` merge of the branch onto main): S24's command printed nothing; the §4 oracle printed
  `HEAD^1..HEAD^2 · 2 commits` and both version lines; on the branch tip it took the merge-base
  form and printed the same lines; on main's tip it printed `0 commits` and exited 1. S24's range
  counted 1 commit there, main's own, so a count alone cannot tell the wrong parent from the right
  one, and S1's range is what does.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md`: S24, AC24 and its
  §9 line. `TOOL-dPlacedRequest-48` writes this file at the same order, so the two passes run in
  sequence.

### Alternatives rejected

- **The merge-base form on the prepared merge too.** It reads `origin/main`, a tracking ref that can
  be older than the merge's first parent, while `HEAD^1` is the merge's own record of the tip.
- **A count of walked commits as the only guard.** S24's range counted main's own commit in the
  fixture, so the guard alone passes a wrong parent.

## 5. Production-readiness checklist

- security — none: a read of local history.
- perf / scale — two `git` walks over the build's commits, once at the close.
- error / empty / loading states — an empty walk exits 1, named (S2).
- observability — the header line names the range and the count it read.
- risks — a prepared merge built by hand with another subject takes the merge-base form, which is
  still the build's side.
- testing — the probes of §6; no suite arm, since the oracle runs once at the close.
- migration — none.
- user docs — none: a criterion's command.

## 6. Acceptance criteria

- **AC1** — When the §4 oracle runs on this build's prepared merge at the close, it prints
  `version oracle: HEAD^1..HEAD^2 · <n> commits` with `<n>` at least 1, and no `KIT_` line.
  Red when: a branch commit hand-bumps `KIT_UNATTENDED_VERSION` or `KIT_RUN_GATES_VERSION`.
  figure: `<n>` DERIVED at observation.
- **AC2** — When the §4 fixture repository is built under `%TEMP%` with the merge subject `merge:
  dPlacedRequest — land onto origin/main at <sha8>`, the oracle prints
  `+KIT_UNATTENDED_VERSION=1.111`, and S24's `git log --first-parent` command as written prints
  nothing.
  Red when: the oracle walks the first parent.
  fixture: built by the probe, not held in the tree.
- **AC3** — When the oracle runs on that fixture's main tip, it prints `walked no commit of the build`
  and exits 1.
  Red when: an empty walk reads as no hand-bump.
- **AC4** — When `grep -n 'first-parent' 2026-10-25-spec-TOOL-dPlacedRequest-43.md` runs, it prints
  nothing, and its AC24 names `TOOL-dPlacedRequest-44`.
  Red when: the vacuous oracle stands beside this one.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the oracle is a criterion's command, observed once at the close.

## 8. Open questions

- **F1 — Which side does the oracle walk?** (a) `HEAD^1..HEAD^2` on the prepared merge and the
  merge-base form elsewhere; (b) the merge-base form everywhere; (c) `--first-parent`, as S24 reads.
  (c) is the defect; (b) depends on a tracking ref's freshness. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound, with the empty-walk refusal of S2.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  26 (BLOCKER, item B1).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edges to `TOOL-dPlacedRequest-54`, `TOOL-dPlacedRequest-55`, `TOOL-dPlacedRequest-56`, mirroring their consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-57` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.
- rev-7 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-43` S24's oracle, itself review 23's M17 fix, whose
`--no-merges --invert-grep --grep='^mint:'` filter this unit keeps; only the range and its guard
change. `python tools/codebase-map/reuse_lookup.py "walk the second parent of a prepared merge for a
version bump"` ranked `merge`, `walk` and `parent_of`, name stems only, none a history oracle;
`tools/check-kit-versions.sh` checks that each version constant is well formed, not who moved it, and
`tools/unattended/check-pass-order.sh` walks build commits for spec-before-code order, neither a fit.
`python tools/memory-recall/query.py "which parent does a check on the prepared merge walk"` returned
TOOL-dUnstalledConvoy-38 (the run's HEAD is the landing merge's second parent), this audit's B1, and
TOOL-aMendedFleet-65's ledger and TOOL-aMendedFleet-3 on the mint into the merge; none disagrees with
source. A grep of `memory/gotchas/` found `a-merge-of-the-default-branch-read-as-additions`, whose
shape table S1 obeys.

Recall terms used: version bump oracle prepared merge first parent second parent push-main commit-tree mint no-merges invert-grep
