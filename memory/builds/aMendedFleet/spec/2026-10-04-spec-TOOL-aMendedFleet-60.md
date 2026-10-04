# TOOL-aMendedFleet-60 — a cross-run overlap probe over unmerged remote refs runs at preflight

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 60

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two runs learn they edit the same files only when the second one merges. `check_single_live` sees
only the run-state files this clone tracks, and the remote run claim another live build is
specifying is keyed by slug, so it cannot see two slugs on one subject. This unit adds
`check_cross_run_overlap` to `--preflight`: it reads every remote-tracking ref not yet merged into
the observed default branch, joins the paths each one changed and the paths its live specs declare
under "Files touched" with the same two sets for this run, and ANNOUNCES each ref that shares a
path. It ignores edits that only move a kit version marker, ignores refs whose tip has aged past a
bound, and refuses nothing.

## 2. Scope (IN)

- **S1** — THE CALL. `check_cross_run_overlap <slug>` in `tools/unattended/unattended.sh` is defined
  after `check_single_live` and called on the line after `check_single_live || true` in
  `verb_preflight`, as `check_cross_run_overlap "$slug" || true`; the slug names the build whose
  specs S4 reads. It always returns 0 and writes nothing. Observed by AC1, AC6 and AC7.
- **S2** — THE REFS. With the observed anchor `ASHA` empty, or naming no commit here, it prints one
  line, `unattended: overlap probe UNAVAILABLE — <why>`, and returns. Otherwise ONE
  `git for-each-ref --no-merged=<anchor> --no-merged=HEAD` over the single remote's
  `refs/remotes/<remote>/` lists each candidate with its tip sha and committer time, which excludes
  the default branch, every merged branch, and this run's own pushed branch while it is an ancestor
  of `HEAD`. The remote's `HEAD` symref is skipped. A ref whose tip is older than
  `OVERLAP_AGE_DAYS`, a driver constant of 14, is counted as aged out and not read further. Observed
  by AC3 and AC5.
- **S3** — THEIR PATHS, per surviving ref: the names `git diff --name-only <anchor>...<ref>` prints,
  plus the backticked path tokens under `### Files touched (estimate)` of every spec that diff
  changed whose status header is not `CLOSED` or `WONTDO` at the ref, read with ONE `git show` of
  all those specs at once and parsed by `read_files_touched`. Observed by AC1 and AC4.
- **S4** — OUR PATHS: the names `git diff --name-only <anchor>...HEAD` prints, plus the same
  Files-touched tokens from the specs under the slug's build folder at `HEAD` that are not terminal.
  Observed by AC1.
- **S5** — THE JOIN, in ONE `awk` process per ref: two paths are shared when they are equal or one
  is a directory the other sits under, after both are normalised by dropping a leading `./`, a
  trailing `/` and any interior `/./`. A path covered by a `SHARED_RECORDS` entry or by the index
  half of a `GENERATED_INDEXES` entry, as the driver resolved them at startup, is never shared: those
  are reconciled additively or re-rendered, never contested. Observed by AC1 and AC5.
- **S6** — THE MARKER FILTER. A shared path that only the ref's DIFF contributes, and that no spec
  on the ref declares, is dropped when every added and removed line of
  `git diff -U0 <anchor>...<ref>` for it carries a kit version marker, matched as `gov:kit`, a space,
  a kit name, `@` and a version. One such call per ref with candidates. A path the ref's specs
  declare stays, whatever its diff holds. Observed by AC2.
- **S7** — THE ANNOUNCEMENT. The summary line always prints first, and always opens
  `unattended: overlap probe — `: `<n> unmerged remote ref(s) read as of this clone's last fetch,
  <a> aged out past 14 days, <u> unreadable, ` and then either `no shared path`, the whole output, or
  `<s> sharing a path; this run is NOT blocked`. In the second form one line per ref with a shared
  path follows: the ref, its tip's first 8 hex, its age in days, the count shared, and at most five
  paths followed by `and <k> more`, each path tagged `diff` or `declared`. Observed by AC1, AC3 and
  AC4.
- **S8** — The kit README gains a section on the probe: what it reads, that it never fetches and so
  reads the refs as of the last fetch, what it excludes, and that it refuses nothing. Observed by
  AC7.
- **S9** — Test arms in `tools/unattended/unattended.test.sh` over a fixture remote with an
  overlapping branch, a marker-only branch, an aged branch and a spec-only branch. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arms are declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Refusing anything. The review's item says announce, never refuse; a refusal would make a stale
  remote-tracking ref a reason to stop, and a remote-tracking ref is a local write any process can
  move.
- Fetching. The driver never fetches; the probe reads what the last fetch left and says so.
- A slug-keyed remote claim, its card listing, or its renewal. Those are the live `aGraftedHelix`
  build's first two units, this probe's complement: a claim names one slug, this names paths.
- Running at `--dispatch` or on every pass. Remote refs are not refetched per pass, so a per-pass
  probe would re-read the same refs.
- The orientation card's overlap line. It is a later unit of this build, which reads this probe's
  output; see Edges.
- A conf key for the age bound. `OVERLAP_AGE_DAYS` is a constant until an adopter asks for another
  value.
- The unattended protocol's concurrency paragraph. It already says concurrent runs are announced and
  never refused, which stays true.
- Bumping the unattended kit version, owed once at the close.

### Edges

- **hands-off** `KICK-aMendedFleet-2` — the orientation card's line listing this probe's overlaps,
  which owes the readable entry point the card calls and the empty-slug reading it needs.
- **hands-off** external — the unattended kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/unattended/` equal base `7af5f564`'s.

- `check_single_live` counts the run-state files this clone TRACKS and announces them; it never
  reads a remote ref. `observe_anchor` records the observed default-branch tip in `ASHA`, and
  `verb_preflight` calls both, each as `|| true`, so every precondition prints in one pass.
- `lib-unattended.sh` defines `covers`, `overlaps` and `normpath`, the kit's path-containment
  predicates. `.unattended.conf` declares `SHARED_RECORDS` as `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`; `GENERATED_INDEXES` resolves at startup from the kits'
  `[[generated]]` rows, among them `memory/LIVE.md`, `memory/ledger` and the map's `generated`
  directory.
- On node a, `git for-each-ref --no-merged=origin/main --no-merged=HEAD` over `refs/remotes/origin/`
  listed two refs, both under a day old: the live `aGraftedHelix` branch and node d's
  `dUnstuckLanding` branch. A scratch join of this build's live specs' Files touched, 109 paths,
  against each ref's diff and declared paths shared 40 and 25 paths; with the shared records and
  generated indexes excluded, 32 and 19, among them `tools/drift-audit/drift_report.py` and
  `.githooks/pre-push`, which node d's branch edits and this build's specs declare. None was
  marker-only. PINNED, measured 2026-10-04.
- A kit version bump changes only lines carrying `gov:kit <name>@<version>`, including the
  `KIT_UNATTENDED_VERSION` line, whose trailing comment carries the marker: commit `6d1ae3a63`.
- The review found the `aGraftedHelix` overlaps were spec estimates and several shared files
  overlapped only in marker lines; S6 drops the second only where a diff, not a spec, is the source.

### Data model

Nothing is stored. Per ref, the probe holds two newline lists, its diff names and its declared
names, each path tagged by source, and prints the join.

### Inventory

- `check_cross_run_overlap` and `read_files_touched` — cell `sh.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest check_cross_run_overlap --as sh.function`, and the same
  for `read_files_touched`.
- `OVERLAP_AGE_DAYS` — a driver constant; no naming cell grades shell variables.

### Rollout

Node d's live branch rewrites `tools/unattended/unattended.sh` and keeps `check_single_live` and its
preflight call byte-identical, so the new function after it and the one call line after its call
reconcile as an insertion. The `aGraftedHelix` branch adds its claim reader to the same file; the two
probes print separate lines and share no state.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/README.md`

### Alternatives rejected

- **Call `overlaps` from `lib-unattended.sh` per path pair.** Each call forks `normpath` twice; at
  109 of our paths against 113 of one ref's, that is about 25,000 forks per ref on a host where a
  fork is the dominant cost. The awk join applies the same three normalisation steps in one process.
- **One `git show` per spec on the ref.** The measured `aGraftedHelix` branch changes 19 specs and
  this build 55; one call per ref with every spec path is one spawn.
- **Refuse on overlap.** The review's item and the protocol both say announce; see §3.
- **Probe at every `--dispatch`.** See §3.

## 5. Production-readiness checklist

- security — reads local refs and objects only; a forged remote-tracking ref can only add or remove
  an announcement, never a refusal or a write.
- perf / scale — one `for-each-ref`, then per surviving ref one name diff, one `git show` and at most
  one `-U0` diff; 2 refs on node a today.
- error / empty / loading states — no anchor prints UNAVAILABLE; no candidate ref prints the
  one-line zero; a ref whose diff fails is counted as unreadable on the summary line, never as clean.
- observability — the summary line always prints, so a clean result is distinguishable from a probe
  that did not run.
- risks — a remote-tracking ref may be stale by however long since the last fetch; the line says
  "as of this clone's last fetch".
- testing — AC1 to AC7 here; the arms in S9.
- migration — N/A: nothing stored changes.
- user docs — the README section in S8.

## 6. Acceptance criteria

- **AC1** — When, under a short `%TEMP%` path, a bare repository is cloned from the unit's tip, a
  second clone pushes a branch whose one commit edits `tools/drift-audit/drift_report.py`, which a
  live spec of this build declares, and a third clone fetches and runs
  `bash tools/unattended/unattended.sh --preflight aMendedFleet --keepalive-id probe`, stdout
  carries the overlap header and a line naming that branch with `tools/drift-audit/drift_report.py`
  tagged `diff`; the exit status equals the status of the same command before the branch was pushed.
  Red when: an overlapping branch is not announced, or its presence changes the verb's outcome.
  cost: about a minute on node a; the clones are the only things written.
- **AC2** — When that branch's one commit instead changes only the `KIT_UNATTENDED_VERSION` line in
  `tools/unattended/unattended.sh`, which this unit's own spec declares, and the third clone
  fetches and re-runs the preflight, no line names that path tagged `diff`; it is named tagged
  `declared` only if a spec on the branch declares it.
  Red when: a version-marker-only edit is announced as an overlap.
- **AC3** — When the branch's commit is made with `GIT_COMMITTER_DATE` thirty days in the past and
  the preflight re-runs, the summary line counts one ref aged out and no line names the branch.
  Red when: an abandoned ref is announced, or an aged ref vanishes from the count.
- **AC4** — When the branch instead adds one spec under its own build folder whose status is
  `SPECCED` and whose Files touched names `tools/runlog/runlog.py`, with no product edit, the
  preflight names `tools/runlog/runlog.py` tagged `declared` for that branch; flipping the spec's
  status to `WONTDO` removes the line.
  Red when: a spec-only branch's declared intent is invisible, or a terminal spec still declares.
- **AC5** — When the branch's commit edits only `memory/DECISIONS.md`, the preflight prints the
  one-line zero; and when the third clone's remote URL names a path that does not exist and the
  preflight re-runs, stdout carries `overlap probe UNAVAILABLE`.
  Red when: a shared record is announced as contested, or a probe that could not run reads as clean.
- **AC6** — When `grep -n "check_cross_run_overlap" tools/unattended/unattended.sh` runs at this
  unit's commit, it prints the definition and exactly one call, on the line after
  `check_single_live || true`. The one later caller this build adds is `print_overlaps`
  (`KICK-aMendedFleet-2`), a read-only verb outside every run.
  Red when: the probe runs from a pass verb, or not at preflight.
- **AC7** — When `grep -n "overlap probe" tools/unattended/README.md` runs, it hits the new section,
  which states the probe never fetches and refuses nothing.
  Red when: the driver prints an announcement its README does not describe.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture remote carrying an overlapping branch, a marker-only branch, an aged branch and a spec-only branch, staged red by deleting the `check_cross_run_overlap` call · none

## 8. Open questions

- **F1** — Which remote refs are "unmerged"?
  Options: refs not merged into the observed anchor; refs not merged into the anchor or into `HEAD`;
  every remote ref but the default. The second excludes this run's own pushed branch while it is
  behind or at `HEAD`, and still shows it when another session pushed past `HEAD`, which is the
  double-drive case worth announcing.
  RESOLVED (agent, 2026-10-04, delegated): not merged into the anchor or into `HEAD`, per S2.
- **F2** — Do shared records and generated indexes count as overlaps?
  The probe measured 40 and 25 shared paths against the two live refs, 8 and 6 of them the decision
  log, the generated work-state views and the map's generated artifacts, which every build writes
  and which reconcile additively or by re-render.
  RESOLVED (agent, 2026-10-04, delegated): excluded through the driver's resolved `SHARED_RECORDS`
  and `GENERATED_INDEXES`, per S5.
- **F3** — The age bound: a constant, a conf key, or none?
  A conf key is a new adopter surface the review did not ask for; no bound announces refs abandoned
  months ago.
  RESOLVED (agent, 2026-10-04, delegated): a driver constant of 14 days, per S2.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the report's Q3 rank 3 ([B#10]) and the synthesis's
  cross-node claim gap ([#9]), and a scratch join of this build's specs against the two live remote
  refs at base.
- rev-2 · 2026-10-04 · S1 S2 S4 S7 AC6 §3 · cross-read with `KICK-aMendedFleet-2`: the function now
  takes the slug, which that unit calls empty; the UNAVAILABLE and summary lines are spelled, the
  summary first in both forms, since the card prints the first line verbatim; AC6 counts the call at
  this commit and names the card's verb as the one later caller; the external edge naming unit 77
  now names `KICK-aMendedFleet-2`. §4's Files touched drops `memory/map/generated/symbols.json`:
  the map enumerates Python and JavaScript definitions only, so the two shell functions move nothing
  there, as the build's other shell-only units already declare.

## 10. Reuse audit

The seams extended are `check_single_live` and its call in `verb_preflight`, which this probe sits
beside, `observe_anchor`'s `ASHA`, the driver's resolved `SHARED_RECORDS` and `GENERATED_INDEXES`,
all in `tools/unattended/unattended.sh`, and the normalisation rules of `normpath` in
`tools/unattended/lib-unattended.sh`, applied in one awk process rather than called per pair (§4).
`python tools/codebase-map/reuse_lookup.py "detect two concurrent runs on unmerged remote branches
touching the same files"` returned `detect_collisions` and `drop_touched_exemptions` in
`tools/codebase-map/map_lib.py`, which join inventory keys within one tree, `branches` in
`tools/memory-tree/check-arms.py`, which reads arm branches and not git refs, and `tracked_files` in
the lexicon kit; none reads remote refs, and none is in this kit. The scan names `.sh` as
unscanned, so it could not see `check_single_live` or `overlaps`; both were found by grep and read
at source. Recall returned `TOOL-aStandingWrit-2`, that a remote-tracking ref reads like an
observation of the remote and is a local write, which is why the probe announces and never refuses,
and `TOOL-aPromptedMandate-9` on preflight's cost, which is why the probe spends a bounded handful of
spawns and no network. Where the report and the tree disagree: the report placed the probe on the
card as well; that line is a later unit of this build, and the probe here is preflight-only.

Recall terms used: `python tools/memory-recall/query.py "how do concurrent runs on different nodes
learn they touch the same files before landing" --terms "check_single_live overlap preflight remote
refs unmerged branch Files touched claim collision announce"`
