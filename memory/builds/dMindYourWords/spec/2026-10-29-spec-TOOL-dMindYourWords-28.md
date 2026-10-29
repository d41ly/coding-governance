# TOOL-dMindYourWords-28 — suppression provenance refused in a shallow history, and judged at a root commit

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 7 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-28-deviation-281.md](../build/2026-10-29-build-TOOL-dMindYourWords-28-deviation-281.md) | deviation | — |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 49 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, item
H6. TOOL-dMindYourWords-5's `check_suppression_provenance` blames each suppression row to a commit and
asks whether that commit adds a `unit.lexicon.suppressions` record. In a shallow history, an adopter's
depth-1 CI checkout, blame attributes every older row to the parentless boundary commit, for which "the
records that commit adds" is undefined: either every row reds in CI while passing locally, or a
root-style diff makes the boundary add the whole tree and every row passes, certifying provenance
nobody examined. This unit refuses to judge provenance in a shallow history, and defines the added set
for a true root commit.

## 2. Scope (IN)

- **S1** — The shallow refusal. Before any blame, `check_suppression_provenance` asks `git rev-parse
  --is-shallow-repository`; `true` makes each registry holding rows one problem, `cannot judge
  provenance — shallow history <registry>`, a red, never a pass and never a per-row `SUPPRESSION WITHOUT
  PROVENANCE`, since the record is unknowable rather than absent. Observed by AC1.
- **S2** — Blame with `--root`. The one blame per registry runs `git blame --porcelain --root`, so a
  repository's true root commit is a commit and not a boundary; a porcelain `boundary` mark on any row
  that is still printed then means a grafted or truncated history the flag of S1 did not report, and
  that row reds `cannot judge provenance — history boundary at <sha8>`. Observed by AC3.
- **S3** — The root commit's added set. `read_vocabulary_record(root, tags, rev=<commit>)`
  (TOOL-dMindYourWords-11 S1) reads "the records that commit adds" with `git diff-tree --root -r
  --name-only --no-commit-id <commit>`, so a parentless commit in a full history adds exactly its own
  tree and a row written with its record in the repository's first commit is judged like any other.
  Observed by AC2.
- **S4** — The docs. The suppression section of `tools/lexicon/README.md` states that provenance needs
  a full history and that a CI checkout fetches it (`fetch-depth: 0`); `KIT_LEXICON_VERSION` moves
  once. NOT OBSERVED as behaviour: prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- The drift blame of TOOL-dMindYourWords-10 S5 in a shallow history: review id 48, the minors batch
  TOOL-dMindYourWords-29.
- Fetching history on the adopter's behalf: the check refuses and names why, and the adopter's CI owns
  its fetch depth.
- The checklist entry the report names as H6's left-shift gate, "every git-history reader states its
  shallow-clone behaviour": a gate is its own unit (BUILD-METHOD M2).

### Edges

- **consumes-from** `TOOL-dMindYourWords-5` — `check_suppression_provenance`, its one blame per registry and its problem lines; without it there is no provenance join to bound
- **consumes-from** `TOOL-dMindYourWords-11` — `read_vocabulary_record` with `rev` a commit, whose added set S3 defines for a parentless commit
- **hands-off** `TOOL-dMindYourWords-29` — `read_vocabulary_record`'s root-commit added set, which the batch keeps when it moves the reader onto the record factory, and the `--root` blame with its boundary mark, which the batch's one blame reader carries (ids 26, 27)
- **hands-off** `TOOL-dMindYourWords-30` — the provenance blame with `--root` and its boundary arm, which that unit pins to the real commit graph and deletes (review id 1)
- **hands-off** `TOOL-dMindYourWords-32` — S3's `diff-tree --root` added set, which that unit pins so a graft point adds only its real diff (review id 23)
- **hands-off** `TOOL-dMindYourWords-33` — S3's `diff-tree` added set, which that unit filters to added paths with renames excluded (review id 12)
- **hands-off** `TOOL-dMindYourWords-37` — the provenance shallow arm and its fixture, which the minors batch builds with a `file://` clone and a shallow probe shared through `read_blame_lines` (review ids 2, 13, 20 and 34)

## 4. Design

### Evidence

- Unit 5's join handles a blame to the zero id and a registry outside the repository and nothing else
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-5.md` S4 and §4 "The provenance join"); unit 11 S1 defines
  `rev` a commit as "only the records that commit adds count"
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-11.md` S1).
- `git blame -h` lists `--root`, "do not treat root commits as boundaries" (the report's id 49 reading).
- This repository already answers a shallow history by asking whether the repository is truncated:
  drift-audit's rate signal reads `rev-parse --is-shallow-repository` and reports a DEAD PROBE rather
  than a derived base (`tools/drift-audit/drift_report.py:1505-1509`), and `transition_audit.py:795` and
  `routed_commits.py:246` ask the same question of their own history reads.

### The join, bounded

```
if git rev-parse --is-shallow-repository == "true":
    for registry with rows: problem("cannot judge provenance — shallow history", registry); return
for registry with rows:
    blame = git blame --porcelain --root -- <registry>
    for row:
        if blame[row].boundary: problem("cannot judge provenance — history boundary at <sha8>", row); continue
        commit = blame[row].commit
        ok = read_vocabulary_record(root, TAG, rev="index" if commit is zero else commit)
        if not ok: problem("SUPPRESSION WITHOUT PROVENANCE", registry, row, commit)
```

### Inventory

Minted: the problem lines `cannot judge provenance — shallow history` and `cannot judge provenance —
history boundary`. No function.

### Migration

None in gov: both registries hold 0 rows at base (unit 5 §4 Migration).

### Rollout

Live at landing, one order after TOOL-dMindYourWords-5, before any suppression row is written.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, `KIT_LEXICON_VERSION`
- `tools/lexicon/lexicon_conf.py`: S3
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S4

### Alternatives rejected

- **Reading every boundary row as provenance found**: it certifies what nobody checked, the wrong green
  the finding names.
- **Reading every boundary row as `SUPPRESSION WITHOUT PROVENANCE`**: it tells the owner to write a
  record that already exists, and reds CI on a tree that passes locally.
- **Deepening the clone from inside the check**: a network fetch inside a grader is an egress surface no
  unit of this build priced (M3 veto 3).

## 5. Production-readiness checklist

- security — deny by default: an unknowable provenance reds; no fetch, no egress.
- perf / scale — one `rev-parse` per run before the blames; `--root` costs nothing extra.
- error / empty / loading states — a registry with no rows spawns nothing, shallow or not; a failed
  `rev-parse` reds `cannot judge provenance — <why>`.
- observability — each refusal names the registry and, for a boundary, its commit.
- risks — an adopter running the leg in a depth-1 CI checkout with a non-empty registry reds until it
  fetches full history, which S4's docs name.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a `git clone --depth 1` of a fixture repository whose
  registry holds one row with its record two commits back, it exits 1 printing `cannot judge provenance
  — shallow history` and no `SUPPRESSION WITHOUT PROVENANCE`.
  Red when: the shallow run passes the row, or reds it as lacking a record.
  fixture: the fixture and its clone under `%TEMP%/<short>`, since a clone under the scratch path fails
  on Windows with `Filename too long`.
- **AC2** — When the same run happens in a full clone of a fixture whose registry row and its
  `unit.lexicon.suppressions` record were both added in the repository's root commit, it exits 0 with the
  row judged; with the record absent from that commit, it exits 1 naming `SUPPRESSION WITHOUT
  PROVENANCE`.
  Red when: the root commit reads as adding nothing, or as adding everything.
- **AC3** — When a fixture's history is grafted so blame prints a `boundary` mark on the row while
  `--is-shallow-repository` reads `false`, the run exits 1 naming `history boundary`.
  Red when: a boundary row is judged against the boundary commit.
  fixture: a `git replace --graft` of the fixture's second commit onto no parent.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 · a depth-1 clone, a root-commit fixture and a grafted fixture, its failing case the shallow test cut out, under which AC1's row is judged against the boundary commit · none

## 8. Open questions

- **F1 — What does provenance read in a history it cannot see whole?** Options: (a) refuse, naming the
  shallow history or the boundary; (b) pass boundary rows; (c) red them as lacking a record. (b) is the
  wrong green and (c) the wrong red the finding names. RESOLVED (agent, 2026-10-29, delegated): (a),
  rung 3, the skeptic's corrected fix and the repository's own answer at
  `tools/drift-audit/drift_report.py:1505`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 49 (HIGH, item H6) of the round-1 spec
  audit, with the skeptic's corrected fix.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-30, TOOL-dMindYourWords-32, TOOL-dMindYourWords-33, TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seam is the `rev-parse --is-shallow-repository` check this repository already runs before trusting
a history read (`tools/drift-audit/drift_report.py:1505`, `tools/memory-tree/transition_audit.py:795`,
`tools/memory-tree/routed_commits.py:246`), carried here as one call because the lexicon kit imports no
sibling. `python tools/codebase-map/reuse_lookup.py "detect a shallow git history before trusting
blame"` ranked generic git wrappers (`git`, `run_git`, `read_git_output`) and no shallow predicate to
import, so no existing seam fits as an import; the call is the idiom those three files share.

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader behave in a shallow clone when blame attributes lines to the boundary" --terms "shallow clone is-shallow-repository blame porcelain boundary root commit provenance suppression depth fetch-depth"`
