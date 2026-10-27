# TOOL-dLinkedLibrary-7 — the `annotations` leg, the lookup under `annotations.lookup`, the read hook on shell reads, and the follow-through test

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 15 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0244@e14fc5fd whole
**Carries:** node:policy-key.annotations.lookup
**Carries:** node:system.annotations

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

The annotation checks need one leg that runs them, a lookup that finds notes by tag or path, and a
push that reaches the reads agents actually make: `pushed-at-read` reaches 3 to 5% of code reads,
since a Read hook misses reads made through the shell (gap-mem-19). The follow-through test that is to
choose that hook decides nothing: it has no threshold, sample size or window, and its measure cannot
separate following a pointer from working on the same build (gap-mem-12). This unit adds the
`annotations` leg over the arms TOOL-dLinkedLibrary-4, -11, -12 and -17 build; the lookup, the marker
query with the map's index rows where the map is installed, or either alone, as `annotations.lookup`
says (AN-1); the read hook on Read, Grep and shell reads (AN-2); and the follow-through test, its
threshold, sample size and window fixed here, its measure counting a follow only across builds
(systems `[design-annotations]` and `[answers]`,
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:338-358`, `:586-631`).

## 2. Scope (IN)

Preconditions this unit calls and does not build: `annotations.py` with `scan_annotations`,
`check_grammar`, `check_resolve`, `check_feature_anchors` and the generated `annotations.json`
(TOOL-dLinkedLibrary-4), `check_note_spans` (TOOL-dLinkedLibrary-17), `check_block_budget` with
`annotation-resolve-legacy` and `untouched-long-blocks` (TOOL-dLinkedLibrary-11), `check_marker_words`
(TOOL-dLinkedLibrary-12), the memory-tree policy adapter (TOOL-dTotalRecall-8 S10), and the landed
`readPolicy` (`tools/policy/policy-mirror.js:132`).

- **S1** — The leg. One row in `tools/gate-legs.json`, shaped like the `recall floor` row: `"name":
  "annotations"`, `"argv": ["python3", "{prefix}/memory-tree/annotations.py", "check"]`, `"chunk":
  "declarations"`, `"subject": "repo"`, no `guard`, so it runs on every bar as `drift-audit records`
  does, and a `ceiling` measured at its first clean run. `annotations.py check` with no `--only` runs
  every entry of the module's `ARMS` table in one process: `markers` (TOOL-dLinkedLibrary-12),
  `grammar`, `resolve` and `feature` (TOOL-dLinkedLibrary-4), `budget` (TOOL-dLinkedLibrary-11) and
  `span` (TOOL-dLinkedLibrary-17, the arm `annotations.py check --only span` runs alone), and exits 1
  when any arm finds. The leg's name is the `leg` value of TOOL-dLinkedLibrary-11's two `[[ledger]]`
  rows, which key both populations to this leg (TOOL-dWitnessedBar-13 S2). Beside it, the module's
  own suite (`annotations.py --selftest`, TOOL-dLinkedLibrary-12 S5) gets its leg,
  `annotations selftest`: argv `["python3", "{prefix}/memory-tree/annotations.py", "--selftest"]`,
  `chunk` `selftests`, `subject` `kit`, guard `{prefix}/memory-tree/annotations.py` and
  `{prefix}/memory-tree/marker-words.toml`, so the arms each unit declares on its `New arm:` line run
  on the bar. Both legs' meta rows land with them: a `[[gate_leg]]` table each in
  `tools/memory-tree/kit.toml`, rows in `tools/govkit/subject-pins.tsv`, the suite's row in
  `tools/run-gates/selftest-budgets.txt`, and both leg names in the `gate-legs` list of the
  annotation-style dossier. Observed by AC1 and AC2.
- **S2** — The lookup, `lookup_annotations(root, tags=(), paths=(), value)` in
  `tools/memory-tree/annotations.py`, behind `annotations.py lookup (--tag <tag> | --path <path>)… [--json]`,
  under `annotations.lookup` read once by `read_policy_value("annotations.lookup", root)`. The marker
  query is `scan_annotations` over the working tree, always fresh; the map index is the rows of
  `memory/map/generated/annotations.json`. `query-and-map`, the default, returns the union keyed by path
  and line, each row marked `query`, `map` or `both`; `query` returns the marker query alone;
  `map-index` returns the index alone, and where the map is not installed prints `annotations lookup ·
  map: not installed — the marker query answers` and returns the marker query. Each text row reads
  `<path>:<line> · <tags> · <definition> → <target>[ · refs <refs>]`. Observed by AC3.
- **S3** — The read hook, `tools/hooks/annotations-read.js`, PostToolUse on `Read|Grep|Bash|PowerShell`
  through `tools/hooks/annotations-read.fragment.json`, merged into `.claude/settings.json` by
  `settings-merge.py --fragment` as `scratch-guard.fragment.json` is. It reads `annotations.grammar`
  through `readPolicy` (`require` of `../policy/policy-mirror.js`, as `tools/hooks/agent-cap.js:465`
  does) and exits 0 printing nothing unless the value is `pushed-at-read`. Its paths: a Read's
  `file_path`, a Grep's `path`, and the path arguments of `grep`, `rg`, `sed -n`, `cat`, `head`,
  `tail`, `git grep`, `git show <rev>:<path>`, `Get-Content` and `Select-String` in a shell command, read
  with scratch-guard's `buildCommandView` and `readTokenAt` and folded to repo-relative with its
  `buildComparablePath` and `buildNativePath`, required from `scratch-guard.js` beside it as
  `format-guard.js` requires it; a leading `cd` or `git -C <dir>` re-roots the paths after it. A path
  already pushed this session, read from `<git-common-dir>/annotations/pushed-<session_id>.txt`, is
  skipped. For the rest it runs `annotations.py lookup --path … --json` through
  `tools/memory-tree/annotations.sh`, bounded by `ANNOTATIONS_READ_BOUND_MS = 4000`, and emits the rows
  as `hookSpecificOutput.additionalContext`, at most 2,048 bytes, a directory argument's tracked files
  nearest first, then appends the pushed paths. It never blocks: a throw, a refusal or a timeout prints
  nothing and exits 0. Observed by AC4 and AC5.
- **S4** — The launcher, `tools/memory-tree/annotations.sh`, carrying the inline `resolve_python` block
  under its `PARITY_ROWS` row in `tools/lib/resolve-python.test.sh` and exec'ing `annotations.py "$@"`,
  as `tools/memory-tree/merge-rows.sh` does for its driver; and `resolveBash`, added to
  `tools/policy/policy-mirror.js`'s exports so the hook runs the launcher under the bash that function
  finds. scratch-guard's exports gain `readTokenAt` and `buildNativePath`. Observed by AC4.
- **S5** — The hook's own suite, `tools/hooks/annotations-read.test.sh`, and its leg `annotations-read
  self-test` (`chunk` `selftests`, `subject` `kit`, guard the hook, its suite, `scratch-guard.js` and
  `annotations.py`), with its `[[files]]` rows in `tools/hooks/kit.toml` (the hook and fragment as
  `engine`, the suite `project-owned`, as format-guard's three are), its `subject-pins.tsv` and
  `tools/run-gates/selftest-budgets.txt` rows and its `harness-hooks` claim in the dossier. Observed
  by AC4 and AC5.
- **S6** — The follow-through test, `tools/runlog/follow_through.py`, over the transcripts the runlog
  kit already reads (`resolve_session_tree`, `read_records`, `extract_segments`, `tools/runlog/extract.py:266`,
  `:308`, `:372`). A qualifying read is a Read or shell read of a tracked code file whose read region,
  taken from the file at the last commit before the read's timestamp, holds a comment citing an id or a
  `memory/` path; a follow is a read, within the next 10 tool calls of that session, of the cited path
  or of a `memory/` record whose file name holds the cited id. The measure that separates following a
  pointer from working on the same build: a follow counts only when the cited record's build is none of
  the builds whose `memory/builds/<slug>/` paths the session read or wrote before the code read; the
  rest are printed as `same-build`, never counted. The control is the same count for the ids of the
  next qualifying file in path order that the session did not read. It prints `follow-through ·
  <window> · <n> reads · cross-build <k> (<p>%) · control <c>% · same-build <s>` and, given
  `--baseline <since>..<until> --after <since>..<until>`, one verdict. Observed by AC6 and AC7.
- **S7** — The test's parameters, fixed here before it runs (§8 F2): the after window is the 30 days
  starting 7 days after the `annotations` leg's landing commit, the baseline window the 30 days before
  that commit; each window needs at least 200 qualifying reads across at least 10 sessions, else the
  verdict is `insufficient`; the follow window is 10 tool calls, and the 3-call exact rate is printed
  beside it. The verdict is `keep voluntary` when the after window's cross-build rate is at least the
  baseline's plus 2 percentage points and at least the after control's plus 2 points, and `choose
  pushed-at-read` otherwise. At the pass the baseline is measured on the 30 days before the pass, its
  line recorded in the acceptance ledger, and the after run is an ask the pass files in
  `memory/builds/dLinkedLibrary/BACKLOG.md` (§8 F3). Observed by AC7.
- **S8** — `annotations.lookup`'s catalogue row (`tools/policy/catalogue.toml:1338`) gains a `summary`
  and the `usage` `annotations.lookup = "query"`; the name leaves `tools/policy/unsummarised-keys.txt`
  through `policy.py lists --write`, and `.governance/policy.json` regenerates in a second commit.
  Observed by AC8.
- **S9** — `help/annotations.md` (TOOL-dLinkedLibrary-4) gains the leg, the lookup and its three values,
  the hook and when it fires, and how to read the follow-through verdict. Observed by AC9.

## 3. Non-goals (OUT)

- The arms the leg runs: their units' (S1's list). This unit adds no rule to any arm.
- The work order's code-notes slot and `annotations.delivery`: dFurnishedOrders', which reads S2's
  lookup.
- Widening `tools/memory-recall/recall-opened.js`. It observes which recall hit was read and pushes
  nothing; the push is a different mechanism with a different kit's policy, so it is its own hook (§8 F1).
- Switching any repository's `annotations.grammar`. The verdict recommends; the owner's policy file
  sets the value.
- Reading a shell command's output. The hook reads its path arguments only, as AN-2 designs it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-12` — `marker`, the registry `check_marker_words` grades as the leg's `markers` arm, and `annotations.py`'s `ARMS` table and `annotations.py --selftest`, which the two legs run
- **consumes-from** `TOOL-dLinkedLibrary-4` — `parse_note_line`, with `scan_annotations`, `annotations.json` and the `grammar`, `resolve` and `feature` arms behind `annotations.py check`; and `pushed-at-read`, the value whose hook this unit builds
- **consumes-from** `TOOL-dLinkedLibrary-17` — `check_note_spans`, the leg's `span` arm, run alone by `annotations.py check --only span`
- **consumes-from** `TOOL-dLinkedLibrary-11` — `annotation-resolve-legacy`, with `untouched-long-blocks` and `check_block_budget`, the populations whose `[[ledger]]` rows name this unit's leg as their `leg`, and the leg's `budget` arm
- **consumes-from** external — the memory-tree policy adapter (TOOL-dTotalRecall-8 S10) and the landed `readPolicy`, `settings-merge.py --fragment` and the runlog kit's transcript readers
- **hands-off** `TOOL-dLinkedLibrary-52` — the `annotations selftest` and read-hook legs and the read hook's bounds, which unit 52 completes (ids 37, 48, 73)

## 4. Design

### Evidence

- `tools/memory-recall/recall-opened.js` is the only read hook at base: PostToolUse, matcher `Read`
  (`recall-opened.fragment.json`), telemetry only, and it fails open (`:200-208`).
- scratch-guard exports `buildCommandView` and `buildComparablePath` (`tools/hooks/scratch-guard.js:1615`)
  and defines `readTokenAt` (`:305`) and `buildNativePath` (`:819`); `tools/unattended/gate-guard.js:211`
  holds a diverged copy, so a third copy is refused and the hook requires the first.
- `format-guard.js` already requires `scratch-guard.js` beside it (`tools/hooks/kit.toml:84-86`), and
  `agent-cap.js:465` requires `../policy/policy-mirror.js` for `readPolicy`.
- The harness's bundled schema gives PostToolUse `hookSpecificOutput.additionalContext` (§8 F4).
- The research's measure: 2,866 code reads, 1,870 holding an id or pointer, 205 followed within 10 calls
  (11.0%), control 6.1%, exact within 3 calls 2.5%, "the hits are mostly sessions already working on that
  build" (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md:92-101`);
  its B4 rule: "If follow-through stays at or below the 11% baseline, B loses to C" (`:153`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `annotations` | gate leg | none |
| `annotations selftest`, `annotations-read self-test` | gate legs | none |
| `lookup_annotations` | function, `annotations.py` | `py.function`, asked at the pass |
| `lookup`, `--tag`, `--path`, `--json` | verb and flags of `annotations.py` | none |
| `tools/memory-tree/annotations.sh` | launcher | none |
| `tools/hooks/annotations-read.js`, its fragment and suite | hook | none |
| `ANNOTATIONS_READ_BOUND_MS` | constant, the hook | none declared |
| `tools/runlog/follow_through.py`, `derive_follow_through` | module and function | `py.function`, asked at the pass |
| `--baseline`, `--after` | flags of `follow_through.py` | none |
| `keep voluntary`, `choose pushed-at-read`, `insufficient` | verdict words | none |

### Rollout

The leg is live at landing and grades the tree under the defaults. The hook is wired at landing and
silent under every value but `pushed-at-read`; an adopter receives it with the hooks kit and its
fragment, merged by `settings-merge.py --fragment`.

### Migration

None. No repository's policy value changes, and the leg's first run reads the populations
TOOL-dLinkedLibrary-11 seeded.

### Files touched (estimate)

- `tools/gate-legs.json`: the three legs of S1 and S5
- `tools/memory-tree/annotations.py`: S2; `tools/memory-tree/annotations.sh` (new): S4
- `tools/memory-tree/kit.toml`: the `[[gate_leg]]` table
- `tools/hooks/annotations-read.js`, `tools/hooks/annotations-read.fragment.json`,
  `tools/hooks/annotations-read.test.sh` (new): S3, S5
- `tools/hooks/kit.toml`: S5's `[[files]]` rows; `tools/hooks/scratch-guard.js`: two exports
- `tools/policy/policy-mirror.js`: the `resolveBash` export
- `.claude/settings.json`: the hook's entry, merged by `settings-merge.py --fragment`
- `tools/lib/resolve-python.test.sh`: the launcher's `PARITY_ROWS` row
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`: the legs' meta rows
- `memory/map/features/annotation-style.md`: its `gate-legs` and `harness-hooks` lists
- `tools/runlog/follow_through.py` (new), `tools/runlog/selftest.py`: S6, its plants
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`: S8
- `memory/builds/dLinkedLibrary/BACKLOG.md`: S7's ask
- `help/annotations.md`: S9

### Alternatives rejected

- **Six legs, one per arm.** Each leg trips the growing set of meta-gates the bug class
  `a-new-leg-trips-a-growing-set-of-meta-gates` records; one leg running one process holds the arms.
- **Parsing a shell command's output for paths.** AN-2 reads arguments only, and output is the bytes
  a push would then repeat.
- **A follow counted whenever the cited record is read.** That is the research's measure, which cannot
  tell a pointer from a session already on that build.

## 5. Production-readiness checklist

- security — the hook writes only its per-session list under the git common dir, interpolates no path
  into a command line, and passes paths to the launcher as arguments; a refusal never blocks a read.
- perf / scale — under every value but `pushed-at-read` the hook costs one `readPolicy`, a git spawn,
  per matched call; under it, one bounded launcher run per call with an unpushed code path.
- error / empty / loading states — the lookup prints `not installed` for an absent map and answers from
  the marker query; the test prints `insufficient` under its floor and chooses nothing.
- observability — the leg prints each arm's summary line; the test prints its counts and windows.
- risks — a same-build session that never reads its build folder before the code read counts as
  cross-build; the control is measured the same way, so the bias falls on both sides of the lift.
- testing — the plants of §6 and the hook's suite.
- migration — none.
- user docs — `help/annotations.md`, S9.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py check` runs over the tree after the pass, it prints one
  `annotations: <arm>:` summary line for each of `markers`, `grammar`, `resolve`, `feature`, `budget`
  and `span`, and exits 0.
  Red when: an arm is missing from the run, or an arm's findings do not turn the exit to 1.
- **AC2** — When `python annotations.py --fixture --plant leg-all-arms` plants one finding per arm and
  runs `check`, it exits 1 naming six findings, one per arm; with each plant removed in turn, the count
  falls by one.
  Red when: an arm's finding is lost from the full run.
- **AC3** — When `python annotations.py --fixture --plant lookup-values` runs `lookup --tag
  feature.alpha` under a planted `annotations.lookup` of `query-and-map`, `query` and `map-index`, the
  first prints the scan's rows and the index's, marking a row added since the last render `query`, the
  second prints the scan's alone, and the third the index's alone; with the map removed, `map-index`
  prints `map: not installed — the marker query answers` and the scan's rows.
  Red when: a value returns another's rows, or an absent map returns nothing.
- **AC4** — When `node annotations-read.js` reads a PostToolUse payload in a fixture repository whose
  planted policy sets `pushed-at-read`, a Bash `sed -n 1,40p` call on a planted code file, a PowerShell
  `Get-Content` call naming the same file by its drive-letter path, and a Read of it each emit the
  file's note row as `additionalContext` the first time and nothing the second.
  Red when: a shell read pushes nothing, or a path is pushed twice in one session.
  fixture: the hook's suite builds the repository under `%TEMP%`.
- **AC5** — When the same payloads run under a planted `voluntary`, under a launcher that sleeps past
  `ANNOTATIONS_READ_BOUND_MS`, and with the policy kit absent, the hook prints nothing and exits 0 each
  time.
  Red when: the hook pushes under another value, or delays or blocks the call.
- **AC6** — When `python follow_through.py --fixture --plant same-build` runs over a planted
  transcript that reads `memory/builds/dX/` and then a code region citing `TOOL-dX-3` and then that
  spec, the follow prints as `same-build` and is not counted; under `--plant cross-build`, the same
  read sequence with no earlier `dX` read counts one cross-build follow; under `--plant beyond-window`
  the record read 11 calls later counts none.
  Red when: a same-build read counts as a follow, or a read past 10 calls counts.
- **AC7** — When `python follow_through.py --fixture --plant verdicts` runs `--baseline` and `--after`
  over planted windows, it prints `keep voluntary` for after 9% against baseline 6% and control 5%,
  `choose pushed-at-read` for after 7% against baseline 6%, and `insufficient` for 199 qualifying reads.
  Red when: a rise under 2 points keeps voluntary, or a short sample yields a choice.
  figure: PINNED in this spec, 2026-10-26: the 2-point margins, 200 reads, 10 sessions, 10 calls and the
  two 30-day windows.
- **AC8** — When `python tools/policy/policy.py get annotations.lookup` runs in a repository whose
  policy file sets no value, it prints `query-and-map`, and after `policy.py lists --write` the summary
  list does not name the key.
  Red when: the row is unsummarised, or its default differs from v2:1355.
- **AC9** — When `grep -n "annotations.lookup\|pushed-at-read" annotations.md` runs over the help page,
  it finds the lookup's three values and the hook's firing rule.
  Red when: the page does not describe the lookup or the hook.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map gate coverage` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/annotations-read.test.sh · covers AC4 AC5 · the hook over a fixture repository, staged by a shell read that pushes nothing and a second read that pushes again · none
New arm: tools/memory-tree/annotations.py · covers AC2 AC3 · the `leg-all-arms` and `lookup-values` plants, staged by an arm left out of `check` and a value returning another's rows · none
New arm: tools/runlog/selftest.py · covers AC6 AC7 · `follow_through.py`'s plants, staged by counting a same-build follow · none
New arm: tools/lib/resolve-python.test.sh · covers none · the launcher's `PARITY_ROWS` row, staged by one byte changed in its inline block · none

## 8. Open questions

- **F1 — Which hook carries the push?** Options: (a) a new hook in the hooks kit,
  `annotations-read.js`, requiring scratch-guard's parsers; (b) `recall-opened.js` widened, as the
  brief's I11 proposed; (c) a Python hook. (b) puts a core value's mechanism in the optional
  memory-recall kit, which TOOL-dLinkedLibrary-3 narrows, and joins a telemetry observer to a push; (c)
  pays an interpreter start on every matched call under every value. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor, firing under every install that carries the
  hooks kit; the brief's I11 spelling departs here, and the return names it. widens: none · relaxes:
  none
- **F2 — What threshold, sample and window decide the test?** Options: (a) a relative rise, the after
  window's cross-build rate at least the baseline's plus 2 points and the control's plus 2, over at least
  200 reads in 10 sessions per window, 30 days each, a 10-call follow window; (b) the research's absolute
  11%; (c) a rise of any size. (b) compares a cross-build rate with a figure that counted same-build
  sessions, so it would choose the hook on a measure the clause says cannot decide; (c) chooses on
  noise. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the only option comparing like with like,
  keeping B4's "rise over the baseline" rule with a margin and a floor fixed before any run. widens:
  none · relaxes: none
- **F3 — Who runs the after window?** It closes 37 days after landing, past this build run. Options:
  (a) the pass files an ask in this build's `BACKLOG.md`, accept the verdict line recorded and the owner
  ruling on it; (b) a scheduled run. (b) needs a schedule surface no clause of this row names.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does a PostToolUse hook's `additionalContext` reach the model?** Probe:
  `grep -a -o 'u({hookEventName:A("[A-Za-z]*")[^}]*})'` over the `claude` on PATH (`claude --version`
  2.1.292, 2026-10-26). Observation: the `PostToolUse` schema carries `additionalContext`. Liveness: the
  same probe reads `CwdChanged` and `PermissionDenied` without it. RESOLVED (agent, 2026-10-26,
  delegated): PostToolUse `hookSpecificOutput.additionalContext`, the channel S3 emits. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, systems `[design-annotations]`,
  `[forks]` and `[answers]` (AN-1, AN-2, M15), layer-memory `[annotations]` tests owed, the
  research-memory-annotations measure and B4 rule, v2:1195 and :1355, and scout B's row for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are the `recall floor` row's shape in `tools/gate-legs.json`; scratch-guard's
exported parsers (`tools/hooks/scratch-guard.js:1615`), required as `format-guard.js` requires them;
`readPolicy` (`tools/policy/policy-mirror.js:132`), required as `agent-cap.js:465` does; the launcher
pattern of `tools/memory-tree/merge-rows.sh`; the fragment wiring of `settings-merge.py --fragment`; and
the runlog kit's transcript readers (`tools/runlog/extract.py:266`, `:308`, `:372`).
`python tools/codebase-map/reuse_lookup.py "gate leg over annotation checks and a read hook on shell
reads"` ranked name stems (`read`, `read_text`, `check`, `legs`, `read_conf`); none is a read hook or a
shell-path parser, and the parser that exists, scratch-guard's, is the seam taken. Scout B's row
proposed copying scratch-guard's functions inline as `gate-guard.js:211` did; that copy has diverged
(`readTokenAt` takes a third `stop` argument there), which is why S3 requires the original. Scout B's
`scratch-guard.js:161-162` and `:818` in systems.md are stale (`:166` and `:819` at base). The recall
query returned scout B's row, the AN-1 answer and the brief's row.

Recall terms used: `python tools/memory-recall/query.py "how does the annotations leg find notes and when does the read hook fire on shell reads" --terms "annotations leg annotations.lookup query-and-map marker query map index read hook shell reads pushed-at-read follow-through threshold"`
