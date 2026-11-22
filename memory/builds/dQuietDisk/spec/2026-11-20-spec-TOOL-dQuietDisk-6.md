# TOOL-dQuietDisk-6 — the manifest check's pickaxe diffs only the commits whose stamp moved

**Status:** SPECCED · rev-3 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

`skills/session-kickoff/manifest-check.sh`'s C5 finds the newest commit that re-stamped the
manifest with a pathspec-free `git log -G'^last-audit:' <stamp>..HEAD`. That pickaxe diffs every
file of every non-merge commit in the range to find a handful of candidates, then validates each
candidate by the manifest's stamp at the commit and at its parent. This unit reads the stamp at every
commit of the range first, through one batched read of the manifest's path, and runs the pickaxe
only over the commits whose stamp moved. C5's answer, its exit and its message are unchanged.

## 2. Scope (IN)

- **S1** — When C5 has a watched commit `W` to explain, it lists the range once with
  `git rev-list --no-merges <LA>..HEAD`, in the order `git log` lists it. Observed by AC1.
- **S2** — It reads the manifest's blob id at each listed commit and at each one's first parent with
  ONE `git cat-file --batch-check`, then the text of each distinct blob with ONE
  `git cat-file --batch`, and computes `blockstamp` once per distinct blob. Observed by AC2.
- **S3** — A commit is a candidate exactly when today's validation would accept it: the stamp at the
  commit or at its parent is empty, or the two differ. Observed by AC1 and AC3.
- **S4** — The candidates, in S1's order, are fed to ONE
  `git log --no-walk=unsorted --stdin --format=%H -G'^last-audit:'`, and `S` is the first line it
  prints, or empty. When there are no candidates, no pickaxe runs and `S` is empty. Observed by AC1
  and AC2.
- **S5** — Any failure of S1, S2 or S4 runs today's pathspec-free pickaxe and its validation loop
  unchanged, so a read this unit cannot make costs the saving, never the verdict. Observed by AC4.
- **S6** — The comment above C5 says why the pickaxe stays pathspec-free and why only stamp-moving
  commits are diffed. Observed by AC5.
- **S7** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S1,
  since `skills/session-kickoff/manifest-check.sh` is on its `watch:` line. Observed by AC6.

## 3. Non-goals (OUT)

- No pathspec on the pickaxe. A pathspec would make a pure `git mv` of the manifest read as an added
  stamp, the case the C5 comment names, and would miss a commit matched only by another file while
  the manifest's stamp line is indented, which `blockstamp` accepts.
- No change to the range. It is already `<LA>..HEAD`, the stamp's own range
  (`skills/session-kickoff/manifest-check.sh@609cd40b1:1989`); the brief's "unscoped" is the missing
  pathspec, which section 4 shows cannot be added without moving the answer.
- No change to `W`, to C3's ancestry checks, to the staged leg, or to any other check.
- No cache and no switch: the same question is asked of git with fewer diffs in one run.
- `skills/session-kickoff/` stays at the repository root.

### Edges

- **consumes-from** external — dWitnessedBar's landed tip, which this unit is built on, because its
  unit 27 changed this file.

## 4. Design

### C5 today

All citations are read at `609cd40b1`.

When `W`, the newest watch-touching commit since the stamp, exists, C5 runs
`git log --format=%H -G'^last-audit:' "$LA_SHA..HEAD"` with no pathspec
(`skills/session-kickoff/manifest-check.sh@609cd40b1:1989`). For each candidate in that order it
reads `blockstamp` of the manifest at the candidate and at its parent, two `git show` each, and
stops at the first candidate whose two stamps are not both present and equal. That commit is `S`,
and C5 fails when `W` is not an ancestor of `S`. The comment above it says why the search has no
pathspec (`skills/session-kickoff/manifest-check.sh@609cd40b1:1974`). `blockstamp` accepts leading
whitespace before `last-audit:` (`skills/session-kickoff/manifest-check.sh#blockstamp`), and the
pickaxe's regex does not.

### Why the reordered search gives the same `S`

Today `S` is the first commit, in `git log` order over `<LA>..HEAD`, that both matches the pickaxe
and passes the validation. `git log` with a pickaxe and no `-m` diffs no merge, so no merge is a
candidate. `git rev-list --no-merges` over the same range lists the non-merge commits in the same
order. The validation reads only the manifest's stamp at the commit and at its first parent, which
S2 computes for every commit without a diff. So the first commit of the range that passes the
validation and then matches the pickaxe is today's `S`, and `--no-walk=unsorted` keeps S1's order
through the pickaxe. A pure rename of the manifest still diffs with rename detection as today,
because the pickaxe runs without a pathspec over the very commits it ran over before.

### The saving

Today's pickaxe diffs every non-merge commit of the range. After, it diffs only the commits whose
stamp moved, which on a branch with one re-stamp is one or two. On dWitnessedBar's tip the stamp's
range holds 302 commits, DERIVED by `git rev-list --count <LA>..609cd40b1` on 2026-11-20 and
re-derived by AC2. The git process count stays about the same, four calls against one plus two per
tried candidate, so the saving is diff work and wall time, which AC2 counts.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `C5_STAMPS` | shell associative array, blob id to stamp | none, a local | nothing |

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` · `skills/session-kickoff/manifest-check.test.sh` · `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `-- <manifest>` on the pickaxe | A pure rename becomes a stamp, and an indented stamp edit matched only through another file is lost. |
| `--follow` on the manifest | It follows one path through renames but still diffs each commit, and its rename heuristics differ from the pathspec-free diff's. |
| Keep the per-candidate `git show` pairs | They are the validation's reads; batching them is what lets the pickaxe run last over few commits. |

## 5. Production-readiness checklist

- security: N/A — reads of the repository's own history.
- perf / scale: the pickaxe diffs the stamp-moving commits only (AC2).
- error / empty / loading states: any failed read falls back to today's search (S5); no candidate
  means no pickaxe and an empty `S`, as today when the log prints none.
- observability: C5's message is unchanged.
- risks: a merge reading that differs from today's. AC1's corpus includes the merge-heavy range.
- testing: the equivalence corpus (AC1), the count (AC2), the planted cases (AC3, AC4).
- migration: none.
- user docs: `help/` holds no page for C5; the comment above it is updated (S6).

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository the probe builds under
`%TEMP%/<short-name>`, in the shape `skills/session-kickoff/manifest-check.test.sh#write_manifest`
and `#restamp` build one, read and never run: a manifest with a `watch:` line and a `last-audit:`
stamp, a watched file, and a range of at least 300 commits [PINNED] past the stamp. "Old" is the check at
`609cd40b1` and "new" the unit's, each run there by path. A reading over the real tree is the gate's
own population, which a role agent may not run (scratch-guard row G1), so each such reading below is
owed to the main loop at the close.

- **AC1** — When the old and the new check run over the fixture at three tips, one whose watched file
  moved before the stamp, one whose range holds 300 commits [PINNED] with one re-stamp, and one whose watched
  file moved after the stamp, each pair prints the same lines and exits the same. When the main loop
  runs the same pairs of `bash skills/session-kickoff/manifest-check.sh` in scratch
  `git clone --shared` copies of the real tree at the build's base and at `609cd40b1`, with its
  302-commit range, each pair prints the same there too.
  Red when: `S` differs on any tip, so C5 passes where the old check fails or the reverse.
  permission: the real-tree pairs are owed to the main loop; the pass makes the fixture pairs.
  fixture: the real-tree clones under `%TEMP%` with their own `TEMP`.
- **AC2** — When both run under `GIT_TRACE2_EVENT=<dir>` over the fixture's 300-commit tip, the new
  run's one pickaxe `log` event carries `--no-walk=unsorted` and at most the stamp-moving commits,
  and the two runs' wall times are printed side by side. The main loop takes the same pair at
  `609cd40b1` at the close.
  Red when: the pathspec-free pickaxe still walks the whole range on the success path.
  figure: the range size is DERIVED by `git rev-list --count` at observation.
  permission: the real-tree pair is owed to the main loop.
- **AC3** — When the fixture's range holds a commit whose only `last-audit:` line sits in another
  file and a later commit that re-stamps the manifest, both versions name the same `S`, and with the
  re-stamp removed both fail C5 with the same message.
  Red when: the decoy is taken for a stamp, or the re-stamp is missed.
- **AC4** — When the batched read is made to fail by a `cat-file` stub on `PATH`, the new check over
  the fixture runs today's pickaxe and prints what the old check prints.
  Red when: a failed read reads as no candidate and C5 fails or passes on that alone.
- **AC5** — When `grep -c 'stamp moved' skills/session-kickoff/manifest-check.sh` runs, it prints 1 or
  more.
  Red when: the comment still describes only the pathspec-free search.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit that
  lands S1, it exits 0.
  Red when: the watched file moves without the re-stamp.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 AC4 · a fixture range with a decoy `last-audit:` line in another file, a re-stamp after it, and a failing batched read; its failing case is staged by taking the decoy as the stamp and by reading a failed read as no candidate · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 3, not the brief's 2: TOOL-dQuietDisk-5 edits
  `tools/run-gates/run-gates.sh`, which is also on the manifest's `watch:` line, so both units
  re-stamp `memory/guides/SESSION-KICKOFF.md` and their write sets meet.
- rev-2 · 2026-11-22 · §6 · AC1 · AC2 · AC4 · under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. AC1, AC2 and AC4 had the pass run the
  ratchet leg over real-tree clones. They now run old and new over a hermetic fixture, and the
  real-tree pairs of AC1 and AC2 are owed to the main loop at the close. The spec mints no
  function, so no name needed a rename.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  6 the fixture's commit range, in the fixture's description and in AC1, is marked PINNED as the size
  the spec fixes. Design, scope and acceptance unchanged.

## 10. Reuse audit

The seam extended is C5's own validation, `blockstamp` over the manifest at a commit and its parent
(`skills/session-kickoff/manifest-check.sh#blockstamp`), moved ahead of the pickaxe and batched; the
batch form is the one `tools/memory-tree/routed_commits.py#check_routed_commits` already uses for
first-parent reads. The chain build owning the area is dScopedBuild (Build: the history-derived exit
base); dWitnessedBar's unit 27 changed this file, and this unit is built on its landed tip and leaves
its wrong-shell refusal as it is.

`python tools/codebase-map/reuse_lookup.py "scope a pickaxe search to the manifest path and the audit range"`
returned name-token neighbours only (`search`, `manifest`, `scope`, `audit`). No existing seam fits
beyond C5's own validation. Recall returned TOOL-aHonedRuleset-5 and -13, and the aRatchetForge
review that shaped C5's rename handling. The source agreed: the pathspec-free choice is still the
comment's.

Recall terms used: manifest-check pickaxe last-audit blockstamp C5 drift watch rename stamp candidate range
