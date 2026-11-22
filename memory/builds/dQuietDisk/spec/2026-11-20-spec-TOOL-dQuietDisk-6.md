# TOOL-dQuietDisk-6 — the manifest check's pickaxe diffs only the commits whose stamp moved

**Status:** WONTDO · rev-5 · 2026-11-22 · node d · Tier-2 · base 7b8c737b · streams tooling · order 3 · retired: section 8 F1, today's pickaxe already stops at its first valid match

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md) | research | TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-18 |

<!-- /gen:spec-records -->

## 1. Goal

`skills/session-kickoff/manifest-check.sh`'s C5 finds the newest commit that re-stamped the
manifest with a pathspec-free `git log -G'^last-audit:' <stamp>..HEAD`. It then validates each
match by the manifest's stamp at the commit and at its parent, and stops at the first that passes.
This unit reads the stamp at every commit of the range first, through one batched read of the
manifest's path, and runs the pickaxe only over the commits whose stamp moved. C5's answer, its exit
and its message are unchanged.

The saving, measured at the re-ground and stated in section 4, is confined to the red path. Where a
validated match is the newest, today's pickaxe dies of a broken pipe after its first two matches,
so it never walks the whole range. On that path the new search spends one git process more than
today and about the same wall time. Only where no match validates, or the first valid one is deep,
does today's pickaxe walk the whole range, and there the new search saves that walk. Neither search
creates a file. Section 8's F1 asks whether the unit is built at all.

## 2. Scope (IN)

- **S1** — When C5 has a watched commit `W` to explain, it lists the range once with
  `git rev-list --no-merges <LA>..HEAD`, in the order `git log` lists it. Observed by AC1.
- **S2** — It reads the manifest's blob id at each listed commit and at each one's first parent with
  ONE `git cat-file --batch-check`, then the content of each distinct blob with ONE
  `git cat-file --batch`. The new function `blockstamps` turns that one stream into one
  `<oid> <stamp>` row per blob, with no process per blob or per commit. Observed by AC2 and AC7.
- **S3** — A commit is a candidate exactly when today's validation would accept it: the stamp at the
  commit or at its parent is empty, or the two differ. A path that is missing or is not a blob at a
  commit has an empty stamp there, as `git show` piped to `blockstamp` gives today. Observed by AC1
  and AC3.
- **S4** — The candidates, in S1's order, are fed to ONE
  `git log --no-walk=unsorted --stdin --format=%H -G'^last-audit:'`, and `S` is the first line it
  prints. When there is no candidate, no pickaxe runs and `S` is empty, because that log with an
  empty stdin walks `HEAD` instead. Observed by AC1 and AC2.
- **S5** — A read this unit cannot make costs the saving, never the verdict. It runs today's
  pathspec-free pickaxe and its validation loop unchanged when any of these holds. Observed by AC4.
  - a git call of S1, S2 or S4 exits non-zero;
  - the `--batch-check` answers number other than twice the listed commits;
  - `blockstamps` returns fewer rows than the distinct blobs it was handed.
- **S6** — The comment above C5 says why the pickaxe stays pathspec-free and why only commits whose
  stamp moved are diffed. Observed by AC5.
- **S7** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S1,
  since `skills/session-kickoff/manifest-check.sh` is on its `watch:` line. Observed by AC6.

## 3. Non-goals (OUT)

- No pathspec on the pickaxe. A pathspec would make a pure `git mv` of the manifest read as an added
  stamp, the case the C5 comment names, and would miss a commit matched only by another file while
  the manifest's stamp line is indented, which `blockstamp` accepts.
- No change to the range. It is already `<LA>..HEAD`, the stamp's own range
  (`skills/session-kickoff/manifest-check.sh@b12d3cd4b588:2644`). The brief's "scoped by path and
  range" is the missing pathspec, which section 4 shows cannot be added without moving the answer.
- No change to `W`, to C3's ancestry checks, to the staged leg, or to any other check.
- No cache and no switch: the same question is asked of git with fewer diffs in one run.
- No new floor on bash: `blockstamps` uses no associative array and no `read -N`, which the kit's
  file uses nowhere today.
- `skills/session-kickoff/` stays at the repository root.

### Edges

- **consumes-from** external — dWitnessedBar's landed tip, because its unit 27 changed this file.
  It is met: the base carries the merge `40def53f7` of dWitnessedBar's landing.

## 4. Design

### C5 today

All citations are read at the worktree's `HEAD`, where the file's blob is the base's.

When `W`, the newest watch-touching commit since the stamp, exists
(`skills/session-kickoff/manifest-check.sh@b12d3cd4b588:2636`), C5 runs
`git log --format=%H -G'^last-audit:' "$LA_SHA..HEAD"` with no pathspec, through a process
substitution (`skills/session-kickoff/manifest-check.sh@b12d3cd4b588:2644`). For each match in that
order it reads `blockstamp` of the manifest at the match and at its parent, one `git show` each
(`skills/session-kickoff/manifest-check.sh@b12d3cd4b588:2641`). It breaks at the first match whose
two stamps are not both present and equal. That commit is `S`, and C5 fails when `W` is not an
ancestor of `S`. The comment above it says why the search has no pathspec
(`skills/session-kickoff/manifest-check.sh@b12d3cd4b588:2629`). `blockstamp` accepts leading
whitespace before `last-audit:` (`skills/session-kickoff/manifest-check.sh#blockstamp`), and the
pickaxe's regex does not. The file sets `set -u` and no `pipefail`.

When the loop breaks, the read end of the substitution closes, and the pickaxe exits 141 at its
next write. A trace of today's search over dWitnessedBar's stamp range at `59e882afd` showed it: the
pickaxe's `exit` event carried code 141 at 0.21 s [PINNED, `GIT_TRACE2_EVENT` 2026-11-22], beside
the two `git show` processes. So on the green path, where the newest match validates, today's search
diffs only the newest commits, up to its second match.

### Why the reordered search gives the same `S`

Today `S` is the first commit, in `git log` order over `<LA>..HEAD`, that both matches the pickaxe
and passes the validation. `git log` with a pickaxe and no `-m` diffs no merge, so no merge is a
candidate. `git rev-list --no-merges` over the same range lists the non-merge commits in the same
order. The validation reads only the manifest's stamp at the commit and at its first parent, which
S2 computes for every commit without a diff. So the first commit of the range that passes the
validation and then matches the pickaxe is today's `S`, and `--no-walk=unsorted` keeps S1's order
through the pickaxe. A pure rename of the manifest still diffs with rename detection as today,
because the pickaxe runs without a pathspec over commits it ran over before.

Each claim was probed in a scratch repository under the session scratch root on 2026-11-22:

| Claim | What the probe showed |
|---|---|
| `git log -G` with no `-m` lists no merge | a merge that itself adds a `last-audit:` line was not listed |
| `rev-list --no-merges` keeps `log`'s order | the two lists were equal with the merge removed |
| `--no-walk=unsorted --stdin` keeps input order | an oldest-first input printed oldest-first, filtered by the pickaxe |
| an empty stdin walks `HEAD` | `log --no-walk=unsorted --stdin` with no input printed `HEAD` |
| a pure `git mv` of the manifest is not a match | neither the move nor the move back was listed |
| `--batch-check` takes `<commit>^:<path>` | it answered each, and `<input> missing` for an absent path or a root's parent, exit 0 |

### How `blockstamps` reads one stream

`blockstamps` reads a `git cat-file --batch` stream of blobs on stdin and prints one
`<oid> <stamp>` row per blob, with an empty stamp where `blockstamp` gives none. It is a fixed
pipeline, about six processes [DERIVED from the pipeline as written], whatever the blob count:

- An awk under `LC_ALL=C` frames the stream: each `<oid> blob <size>` header, then `<size>` bytes
  counted as each line's byte length plus its newline, then git's separator newline. A header of any
  other shape, or a stream ending inside a blob, stops it, so its rows fall short and S5 falls back.
- The same awk applies `blockstamp`'s block filter per blob: lines after the first line holding
  `<!-- manifest-audit`, up to the next line holding `-->`. It prints each kept line behind the blob's
  oid and one space, and one marker row per blob, so a blob with no block still yields a row.
- The `tr -d '\r'`, the `last-audit:` extraction, the first match per blob and the trailing-space
  strip then run as `blockstamp` runs them, in the caller's locale.

Only the framing runs under `LC_ALL=C`, because its regexes are ASCII literals and its byte count
needs bytes. The `[[:space:]]` classes stay in the caller's locale, as in `blockstamp`.

`blockstamp` stays as it is, since C5s and S5's fallback call it. Two forms of one extraction is the
risk this design takes, and AC7's arm grades the pair over every blob shape the extraction reads.

### The saving

Measured on 2026-11-22 over dWitnessedBar's stamp range at `59e882afd`, with a prototype of S1 to
S4 under the session scratch root. The range holds 308 non-merge commits [DERIVED by
`git rev-list --count --no-merges <LA>..59e882afd`], 28 distinct manifest blobs [DERIVED by the
prototype's `--batch-check` answers] and 25 candidates [DERIVED by the prototype]. Both searches
named the same `S`.

| Path | Today | New |
|---|---|---|
| green: the newest match validates | 3 git processes [PINNED, traced], 0.25 to 0.33 s [PINNED] | 4 git processes [PINNED, traced], 0.32 to 0.36 s [PINNED] |
| red: no match validates | the whole range diffed, 0.95 s for the pickaxe alone [PINNED], plus 2 `git show` per match | 4 git processes, the same constant cost |

At the worktree's `HEAD` the real tree's range holds 6 commits [DERIVED by
`git rev-list --count <LA>..HEAD` at `0318ce9c9`], so neither path costs anything there. The red
path runs only while a branch owes a re-stamp, the state C5 exists to fail. A first prototype that
piped each blob to `blockstamp` cost 2.67 s [PINNED], from a process chain per blob, which is why S2
forbids one.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `blockstamps` | shell function in `skills/session-kickoff/manifest-check.sh` | `blockstamp`'s, plural for a stream | AC7 |

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` · `skills/session-kickoff/manifest-check.test.sh` ·
`memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

None of these is in the Files touched of units 10, 12, 13, 18 or 28 as their specs stand at the
worktree's `HEAD`, and none of those names a path on the manifest's `watch:` line. A sibling that
lands a watched path first moves the stamp this unit's commit re-stamps, and the lander re-stamps at
the merge as the build's earlier units did.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `-- <manifest>` on the pickaxe | A pure rename becomes a stamp, and an indented stamp edit matched only through another file is lost. |
| `--follow` on the manifest | It follows one path through renames but still diffs each commit, and its rename heuristics differ from the pathspec-free diff's. |
| `tools/lib/history-store.sh#read_bh_blob`, one blob per call | Each blob then needs its own `blockstamp` chain, the 2.67 s prototype, and the block is gov-internal, carried inline only into the unattended kit. |
| An associative array of stamps read by `read -N` | It raises the kit's bash floor to 4.1, and `read -N` counts characters, not bytes, unless `LC_ALL=C` scopes that one read: a probe read 5 bytes for 3 characters [PINNED, probed 2026-11-22]. |

## 5. Production-readiness checklist

- security: N/A — reads of the repository's own history.
- perf / scale: the pickaxe diffs the commits whose stamp moved, at a constant 4 git processes
  [PINNED, the bound this spec fixes] (AC2); section 4 states where that saves and where it does not.
- error / empty / loading states: any failed read falls back to today's search (S5); no candidate
  means no pickaxe and an empty `S`, as today when the log prints none.
- observability: C5's message is unchanged.
- risks: a merge reading that differs from today's, which AC1's corpus covers; the two forms of the
  stamp extraction, which AC7 covers.
- testing: the equivalence corpus (AC1), the count (AC2), the planted cases (AC3, AC4), the stamp
  parity (AC7).
- migration: none.
- user docs: `help/` holds no page for C5; the comment above it is updated (S6).

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository the probe builds under
`%TEMP%/<short-name>`, in the shape `skills/session-kickoff/manifest-check.test.sh#write_manifest`
and `#restamp` build one, read and never run: a manifest with a `watch:` line and a `last-audit:`
stamp, a watched file, and a range of at least 300 commits [PINNED] past the stamp. The probe builds
that range with one `git fast-import`, never a commit per step. "Old" is the check at the base
`7b8c737b0` and "new" the unit's, each run there by path. A reading over the real tree is the gate's
own population, which a role agent may not run (scratch-guard row G1), so each such reading below is
owed to the main loop at the close.

- **AC1** — When the old and the new check run over the fixture at three tips, each pair prints the
  same lines and exits the same. The tips are one whose watched file moved before the stamp, one
  whose 300-commit [PINNED] range holds one re-stamp, and one whose watched file moved after the
  stamp. When the main loop runs the same pairs of `bash skills/session-kickoff/manifest-check.sh`
  in scratch `git clone --shared` copies of the real tree at the build's base and at `59e882afd`,
  each pair prints the same there too.
  Red when: `S` differs on any tip, so C5 passes where the old check fails or the reverse.
  figure: the range at `59e882afd` is DERIVED by `git rev-list --count --no-merges` at observation.
  permission: the real-tree pairs are owed to the main loop; the pass makes the fixture pairs.
  fixture: the real-tree clones under `%TEMP%` with their own `TEMP`.
- **AC2** — When both run under `GIT_TRACE2_EVENT=<dir>` over the fixture's green tip and over a red
  tip whose 300 commits [PINNED] hold no re-stamp after `W`, the new run's trace holds one each of
  `rev-list --no-merges`, `cat-file --batch-check`, `cat-file --batch` and `log --no-walk=unsorted`,
  and no `git show` of the manifest at a commit. Its one pickaxe event names at most the commits whose
  stamp moved. Both runs' git process counts and wall times print side by side, per tip.
  Red when: the new search launches a git process per commit or per blob, or the pickaxe still
  walks the whole range.
  figure: the per-run counts are DERIVED by counting the trace files at observation.
  permission: the real-tree pair at `59e882afd` is owed to the main loop.
- **AC3** — When the fixture's range holds a commit whose only `last-audit:` line sits in another
  file and a later commit that re-stamps the manifest, both versions name the same `S`. With the
  re-stamp removed both fail C5 with the same message.
  Red when: the decoy is taken for a stamp, or the re-stamp is missed.
- **AC4** — When a `git` shim first on `PATH` fails `cat-file --batch-check`, then in a second run
  fails `cat-file --batch`, then in a third truncates the `--batch` stream, the new check over the
  fixture runs today's search each time and prints what the old check prints. The shim passes every
  other call to the real git, so C3's `cat-file -e` still answers.
  Red when: a failed or short read reads as no candidate and C5 fails or passes on that alone.
- **AC5** — When `grep -c 'stamp moved' skills/session-kickoff/manifest-check.sh` runs, it prints a
  count other than 0.
  Red when: the comment still describes only the pathspec-free search.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit that
  lands S1, it exits 0.
  Red when: the watched file moves without the re-stamp.
- **AC7** — When `blockstamps` reads one `--batch` stream of fixture blobs, each row equals what
  `blockstamp` prints for that blob. The blobs hold CRLF lines, multibyte UTF-8 before the block, an
  indented stamp, a body decoy, two blocks, a stamp with an empty value, no trailing newline, and no
  bytes at all.
  Red when: any row differs, or a blob yields no row.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 AC4 AC7 · a fixture range with a decoy `last-audit:` line in another file, a re-stamp after it, a failing and a truncated batched read, and the blob shapes AC7 names; its failing case is staged by taking the decoy as the stamp, by reading a failed read as no candidate, and by a `blockstamps` that strips no CR · none

## 8. Open questions

- **F1 — Build the reordered search, whose saving section 4 confines to the red path, or retire the
  unit?**
  - (a) Build S1 to S7 as written. The red path's whole-range walk goes,
    0.95 s at 308 commits [PINNED, measured 2026-11-22],
    and the green path spends 4 git processes against today's 3 [PINNED, traced 2026-11-22],
    at about the same wall time. It is the owner's prompt's ask, and an
    unattended fork has ranked that above YAGNI before (TOOL-dQuietDisk-17 F1).
  - (b) Retire the unit, `WONTDO`, with section 4 as its reason, and record in the build README's
    item for the pickaxe that today's search already stops at its first valid match.
  - Recommendation: (b). The build's measure is git processes and file creates, (a) raises the first
    on the common path and touches neither on any path, and its second form of the stamp extraction
    is a standing cost. The resolver should weigh M3's feature-rich rule openly against that.
  - RESOLVED (agent, 2026-11-22, delegated): (b), retire the unit. The build measures git processes
    and file creates; section 4's measurements show the unit adds one git process on the common green
    path and saves no file creates, and today's pickaxe already exits at its first valid match, so
    the analysis's premise does not hold.

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
- rev-4 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S2 S3 S5 · AC2 AC4 AC5 AC7 · re-grounded at
  7b8c737b0 (orders 1 and 2 built), under `2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task`:
  - The file's blob moved from `d704bfffde03` to `b12d3cd4b588` through dWitnessedBar's landing; the
    pickaxe, the validation and the comment are re-cited at their new lines, and C5 is unchanged.
  - The saving moved. A trace showed today's pickaxe dying of a broken pipe once the loop breaks, so
    the green path never walked the range. Section 1 now confines the saving to the red path, and
    F1 asks whether to build. The 302-commit figure was re-derived as 308 at `59e882afd`.
  - S2 changed how the stamps are read. Rev-3 named no parser; a per-blob `blockstamp` cost 2.67 s,
    and a bash `read -N` counts characters. `blockstamps` frames the stream in one awk, the
    associative array `C5_STAMPS` is gone, and AC7 is new to grade it against `blockstamp`.
  - S5 names what counts as a failed read, since the file sets no `pipefail`. AC4's stub became a
    `git` shim, because `cat-file` is a builtin a `PATH` stub cannot replace and C3 also calls it.
  - The edge on dWitnessedBar's tip is met by the merge `40def53f7`. AC5's count is worded as other
    than 0, and the fixture is built by one `git fast-import`.
- rev-5 · 2026-11-22 · §8 · status WONTDO · the run's coordinator ruled F1 as (b), retire, marked in
  place as delegated. The unit adds one git process on the green path and saves no file creates, so
  it is not built. Section 4's measurements table stays as the record of why; scope, design and
  acceptance are kept as written and unbuilt.

## 10. Reuse audit

The seam extended is C5's own validation, `blockstamp` over the manifest at a commit and its parent
(`skills/session-kickoff/manifest-check.sh#blockstamp`), moved ahead of the pickaxe and batched.
The batch-check form is the one `tools/memory-tree/routed_commits.py#check_routed_commits` uses for
first-parent reads (`tools/memory-tree/routed_commits.py@e3088f9bcba9:576`). The shell batch reader
`tools/lib/history-store.sh#read_bh_blob` was read and rejected in section 4: it answers one blob
per call, which costs a `blockstamp` chain per blob. The chain build owning the area is dScopedBuild
(Build: the history-derived exit base); dWitnessedBar's unit 27 changed this file, and this unit
leaves its wrong-shell refusal as it is.

`python tools/codebase-map/reuse_lookup.py "scope a pickaxe search to the manifest path and the audit range"`
returned name-token neighbours only (`search`, `manifest`, `scope`, `audit`). At the re-ground,
`python tools/codebase-map/reuse_lookup.py "read many blobs from one cat-file batch stream in bash and extract a value per blob"`
returned python readers, `read_blobs_at` among them, which a bash kit cannot call on C5's path. No
existing seam fits beyond C5's own validation. Recall returned TOOL-aHonedRuleset-5 and -13, and the
aRatchetForge review that shaped C5's rename handling. The source agreed: the pathspec-free choice is
still the comment's.

Recall terms used: manifest-check pickaxe last-audit blockstamp C5 drift watch rename stamp candidate range cat-file batch
