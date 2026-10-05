# TOOL-aGraftedHelix-32 — the closing review's 21 MEDIUM and LOW findings, fixed as one batch

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-2 · base 018b5675 · streams tooling+kickoff · order 16 · closes TOOL-aBranchedMandate-9 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, confirmed 21 findings below HIGH: nine MEDIUM items
(M1 to M9) and four LOW items (L1 to L4), two pairs of which are one defect at two grades. The
owner's promote-every-finding ruling makes them one unit. This unit fixes each item as the review's
Fix line states, left-shifts each as its Left-shift line states, and reproduces the rotation
observation the spec brief carries. That observation turned out to be M4's class, and it is the
open ask `TOOL-aBranchedMandate-9`, which this unit closes.

## 2. Scope (IN)

Every item names the review section it answers. The review record is
`memory/builds/aGraftedHelix/reviews/2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md`.

- **S1** — M1, ids 3, 15 and 22. The spec commit block in `tools/workflows/unattended-build.template.js`
  commits by pathspec. Its delta loop reads the porcelain listing through process substitution and
  appends each path it stages to a bash array, `delta`. The commit line becomes
  `git commit --only -q ... -- <spec paths> "${delta[@]}"`, so an entry staged before the block,
  the run's own `RUN.md` included, stays staged and out of the commit. The prose around the block
  names that purpose without spelling the command. Observed by AC1.
- **S2** — M1's left-shift, the class gate. `tools/workflows/check-workflow-syntax.js` gains a second
  pass over the population it already discovers: a line whose string literal opens `git commit` and
  carries no ` -- ` exits 1, naming the file and the line. Its header says what the pass does not
  check. Observed by AC2.
- **S3** — M2, ids 6, 12 and 23. `renderChecklistUnion` emits its head from a one-line declaration,
  `const BY_DESIGN_FORMAT = '...{n}...'`, beside its `BY_DESIGN_HEAD`. The parity checker
  `tools/workflows/check_by_design_parity.py` evaluates both templates' `BY_DESIGN_HEAD` against the
  catalogue's rendered heads, and renders the build harness's `BY_DESIGN_FORMAT` at each count in
  `SAMPLE_COUNTS` and requires it byte-equal to the catalogue's head at that count. The "spelled
  twice" claims in the checker's docstring and in `tools/workflows/README.md` become a statement of
  the derived population. Observed by AC3 and AC4.
- **S4** — M2's left-shift. The checker derives its population. It scans its own directory and the
  memory-tree directory it is handed for files carrying the head's fixed tail, the trailing run of
  letters-only words of the head the catalogue renders, and a needle shorter than two words is a
  refusal. A hit outside the declared evaluated set exits 1 naming the file. A scan that finds no
  file of the evaluated set is a DEAD PROBE and a refusal, since every evaluated template spells the
  tail in its pattern. `--selftest` gains one arm per new outcome and `ARMS_DECLARED` rises with
  them. Observed by AC4 and AC5.
- **S5** — M3, id 2. While `<git-dir>/push-main-active` exists in the git dir the claim push would
  run in, `write_claim` in `tools/unattended/unattended.sh` pushes nothing, leaves both verdict files
  alone and returns 2 with a `WC_WHY` naming the marker. The header comment's "a token read after it
  came from THIS push's hook" is corrected to say when that holds. The class joins
  `memory/gotchas/decision-re-derived-by-a-second-process.md`. Observed by AC6 and AC17.
- **S6** — M4, id 7, and the rotation observation. `--preflight` validates the build README's
  source markers, and an existing record's generated markers when the call does not rotate it,
  above the write gate, joining `status`. Everything after the claim write, from the rotation to
  `stage_or_fail`, runs as one function, `write_preflight_record`. When it fails, `verb_preflight`
  restores the run-state path and the archive path to their bytes at `HEAD`, in the index and the
  work tree, before it returns. `check_clean` proved the tree clean at the gate, so that restore puts
  back exactly what the call found, and the refusal's "the run-state file is unchanged" line becomes
  true. Observed by AC7, AC8 and AC9.
- **S7** — M4's claim half. On that same failure branch, a claim this call CREATED is written
  `aborted` through the status-write block `--abort` uses. A claim this call renewed, rewrote or took
  is left in place, and one `claim left` line says so with the action. Observed by AC10 and AC11.
- **S8** — M4's left-shift. A driver-suite arm reads `verb_preflight`'s source and asserts that after
  the claim write its one `return 1` sits in the branch taken when `write_preflight_record` fails.
  The class joins `memory/gotchas/destructive-step-before-its-precondition.md` as its third instance,
  "a remote write counts as a write, and so does the rotation". Observed by AC12 and AC17.
- **S9** — M5, id 14. Where `RUN_CLAIMS` is not `on`, `--claims` prints the single line
  `claims: off`, exits 0 and reads nothing from the remote. The orientation card's `derive_claims_line`
  in `skills/session-kickoff/manifest-check.sh` renders that line as
  `claims — skipped: RUN_CLAIMS is off`. `tools/unattended/VERBS.template.md`, its rendered guide and
  the driver's two comments that say the read runs either way are corrected. Observed by AC13 and
  AC14.
- **S10** — M6, id 16. `read_claims soft` restores `status` and `RUNLOG_CHECKS` after
  `resolve_claim_remote` and silences its check-24 line, as the `quiet` branch does, so check 24
  reaches the caller only as `CL_WHY` in the one announced `claims not read` line. Observed by AC15.
- **S11** — M7, id 25. The location-probe class gate unit 27 handed to this run's orchestrator is
  parked with `--park`, recording the question, the options and the reason §8 F3 states. The
  `## Its gate` section of `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md` points
  at that parked row. A new class record carries the documented check: at the close, every spec line
  handing a discovery to the orchestrator resolves to a unit or a parked row. Observed by AC16 and
  AC17.
- **S12** — M8 and L1, ids 17, 9 and 27. The GH26 AC3 arm gains a separate leg with the bare origin
  in place, no mktemp shim on `PATH`, and a git shim failing only the claim fetch. It asserts the
  shim's log names no push and the claim ref is unmoved. Observed by AC18.
- **S13** — M9 and L2, ids 19, 4, 10 and 28. In `tools/memory-recall/selftest.py`,
  `test_empty_alias` asserts exactly one line equal to `EVIDENCE_BANNER`, directly after the hits
  line, and `_measure_spine_docs` asserts exactly one line opening `superseded ` that carries
  `unresolved`. No arm is added, so `SELFTEST_ARMS` holds. Observed by AC19.
- **S14** — L3, id 11. `derive_row_re(conf)` sits beside `id_pattern` in
  `tools/memory-tree/row_grammar.py`, and each of the five row-regex sites calls it. A `--selftest`
  arm counts the row regex's literal prefix in the module's own source and requires one. Observed by
  AC20.
- **S15** — L4, ids 13 and 26. `memory/map/features/unattended-stops.md` names the claim refusals as
  checks 107 and 108, and a read that does not complete as check 109. The renumber class joins
  `memory/gotchas/a-spelling-change-strands-its-readers.md`: a check renumber greps the whole tracked
  tree outside `memory/builds/` and lists every hit in its commit message. Observed by AC21 and AC17.
- **S16** — The bookkeeping the fixes owe. Each of the five kits whose shipped bytes move bumps its
  version once, after this unit's last move in it: `unattended`, `review-harness`, `memory-tree`,
  `memory-recall` and `kickoff-manifest`. Every render is re-rendered and the unattended guides are
  re-adopted. The codebase map's generated artifacts are re-rendered. The kickoff manifest is
  re-stamped, because `skills/session-kickoff/manifest-check.sh` is on its `watch:` list. Observed by
  AC22 and AC23.

## 3. Non-goals (OUT)

- **No HIGH item.** H1, H2 and H3 are units 29, 30 and 31.
- **No location-probe class gate.** S11 parks it; §8 F3 says why.
- **No change to the claim write table.** No row, mode or verdict of `CLAIM_READS` or
  `CLAIM_MODES` moves. S7 calls the table's existing `status` column.
- **No claim ref is ever deleted.** The stops guide's section 7 says a claim is never deleted, and S7
  keeps that.
- **No new `--claims` flag or mode.** §8 F2.
- **No restore of a pre-gate refusal.** A refusal above the gate writes nothing, which is the gate's
  existing rule; S6 only moves two pure reads up to it.
- **No change to the push-main or pre-push verdict files' format, nor to which process writes them.**
  S5 changes only when a claim push may run.
- **No new gate leg.** S2 rides `workflow script syntax`, S4 rides the review harness's parity leg,
  and every other arm lives in a suite that already exists. Shared invariant 5.
- **No new `recall` arm.** S13 adds assertions to two existing arms.
- **The `statusre` pattern beside the row regex in `row_grammar.py` is not hoisted.** It shares the
  prefix but carries a different tail, and L3 names the five row-regex copies only.
- **Prose copies of the by-design head stay ungraded**, as unit 28 ruled. S4 exempts `*.md`.

### Edges

none

## 4. Design

### Evidence

Read at `9024901c`, the run branch's tip. Every file this unit edits is byte-identical there to the
pinned BASE `018b5675`, since the commits between them touch records only.

- `tools/workflows/unattended-build.template.js:903-922` is the commit block. Its delta loop at
  `:917-919` is a pipeline, so the loop runs in a subshell, and the commit at `:920` names no path.
  `BY_DESIGN_HEAD` is declared at `:497` and the union's head is a string literal at `:516`.
- `tools/workflows/unattended-build.test.sh:2193-2216` builds the GH16 fixture, and
  `:2217-2223` runs the block extracted from the prompt. Its `FLOOR_ASSERTIONS` is at `:2325`.
- `tools/workflows/check_by_design_parity.py:7` says the head "is spelled twice", and
  `tools/workflows/README.md:202` says the same. `ARMS_DECLARED` is 13 at `:46`.
- `tools/workflows/check-workflow-syntax.js` discovers every `.js` declaring `export const meta`,
  renders and not templates, and parses each.
- `tools/unattended/unattended.sh:2041` is `write_claim`. It clears `pre-push-refusal` at `:2059`
  and pushes at `:2060`. `tools/push-main.sh:120` holds `push-main-active` in
  `git rev-parse --git-dir`, and `.githooks/pre-push:334` clears both verdict files on every run.
- `tools/unattended/unattended.sh:1834-1845` is `read_claims`. Only its `quiet` branch restores
  `status` and `RUNLOG_CHECKS`. `print_claims` is at `:1912`.
- `tools/unattended/unattended.sh:6245` is `--preflight`'s write gate, `:6253` its claim write,
  `:6276-6284` the rotation, `:6298-6302` the source-marker check, `:6306-6312` the scaffold and the
  generated-marker check, `:6342` `write_lease` and `:6450` `stage_or_fail`. Every refusal between
  `:6253` and `:6450` ends in a bare `return 1`, and `exit "$status"` at the end of the script makes
  the process exit.
- `tools/unattended/unattended.sh:5488` is the status-write block `--abort` uses:
  `read_claims soft`, then `check_claim_writable ... status ...`, then `write_claim ... aborted ... soft`.
- `skills/session-kickoff/manifest-check.sh:387` is `derive_claims_line`. It gates on the conf's
  existence and a resolvable driver, never on `RUN_CLAIMS`.
- `tools/unattended/unattended.test.sh:14095-14133` is the GH26 AC3 arm. Its once-only mktemp shim
  absorbs `write_claim`'s own `mktemp` at `unattended.sh:2054` before any push can run.
- `tools/memory-recall/selftest.py:543-556` is `test_empty_alias`, and `:564-574` is
  `_measure_spine_docs`. The `@check` decorator RUNS each arm when it is defined, so importing the
  module runs the whole suite. `query.py:1396` prints `EVIDENCE_BANNER`, and `extract.py:888`
  prints the `superseded` line.
- `tools/memory-tree/row_grammar.py:184` is `id_pattern`. The row regex is built at `:322`, `:811`,
  `:1062`, `:1142` and `:1291`. `_DIFF_ROW_TAIL` at `:1542` spells a similar prefix without the
  leading anchor, and `statusre` at `:812` shares the prefix with another tail. Both are near-misses
  the count in S14 must not take.
- `memory/map/features/unattended-stops.md:56-57` names the claim refusals as checks 89 and 90.

### The rotation observation, reproduced

The brief reports a first `--preflight` after the abort that printed
`--preflight refused; the run-state file is unchanged` while the ABORTED record had already been
archived and a fresh `RUN.md` written. That line is printed only at `unattended.sh:6245` and
`:6255`, both above the rotation at `:6276`, so one call cannot print it after rotating.

The probe was a scratchpad slice of the driver suite's prologue, lines 1 to 629 with `HERE` pinned to
`tools/unattended`, run on node `a` on 2026-10-05 with git 2.54.0.windows.1. Each case started from
the suite's preflighted `tRun` with its record set to `phase: ABORTED` and committed.

| case | call 1 | tree after call 1 | call 2 |
|---|---|---|---|
| P1, `WIRING_CHECK="false"` | check 4, then the refusal line; nothing archived | clean | not run |
| P2, the README's `<!-- /gen:build-index -->` line removed | archived, then check 9 at the source markers | `R  RUN.md -> RUN.ABORTED.074e0274.md` staged | check 2 (dirty tree), then the refusal line |
| P3, a session id carrying a carriage return | archived, scaffolded, then check 17 at `write_lease` | the rename staged and an untracked `RUN.md` | check 2, then the refusal line |

So it reproduces, across two calls. Call 1 archives and refuses after the rotation without printing
the line. Call 2 reads the tree call 1 left, refuses at check 2 and prints "the run-state file is
unchanged", which is true of call 2 and false of the tree. The observer's record of call 1 was not
captured, and the commit `018b5675` names check 4, which P1 shows cannot rotate. The likeliest
sequence is an earlier call that refused after its rotation. That is the
destructive-step-before-its-precondition class, and it is exactly `TOOL-aBranchedMandate-9`, open
since 2026-08-17. S6 closes it; §8 F5 records the probe as the decision.

### S1 and S2 — the pathspec commit and its class gate

The block's loop becomes:

```sh
delta=()
while IFS= read -r line; do
  if printf '%s\n' "$rec" | cut -c4- | grep -xF -- "${line#???}" >/dev/null; then :; else git add -- "${line#???}"; delta+=("${line#???}"); fi
done < <(git status --porcelain --untracked-files=all)
git commit --only -q -m '...' -m '...' --trailer 'Pass: none' --trailer '<attribution trailer>' -- <spec paths> "${delta[@]}"
```

The `--only` pathspec semantics were measured on node `a` on 2026-10-05 with git 2.54.0.windows.1,
in a scratch repository. A pre-staged edit, a staged deletion and a staged new file sat in the
index. `git commit --only -q -m t -- <modified> <deleted> <new>` committed all three of the named
paths and left the foreign staged edit staged and out of `HEAD`. Plain `git commit -- <path>`
behaved the same. `--only` is spelled anyway, so a reader does not need to know the default.

The S2 pass reads each discovered script's source lines. A line whose first string literal opens with
`git commit` and which carries no ` -- ` is a finding. Run over the real tree at `9024901c`, the
population was the six workflow scripts and the predicate hit one line, `unattended-build.js:920`,
the instance S1 fixes. A loose `git commit` match found no other line, so there was no near-miss. The
header states what the pass does not check: a commit built at runtime, a commit an agent composes
from prose, and a ` -- ` that sits inside a message argument.

### S3 and S4 — the by-design head, held across every spelling

`renderChecklistUnion`'s return becomes
`head.concat(items, [BY_DESIGN_FORMAT.replace('{n}', String(design.length + gap))], design)`. The
checker gains `run_format`, which evaluates the one-line `BY_DESIGN_FORMAT` string literal in `node`
the way `run_pattern` evaluates the regex literal, renders it at each count in `SAMPLE_COUNTS`, and
returns the strings. `check_parity` then:

1. renders the catalogue's heads, as today;
2. runs `run_pattern` over each template in `EVALUATED_TEMPLATES`, which is `tier2-review.template.js`
   and `unattended-build.template.js` beside the checker;
3. runs `run_format` over `unattended-build.template.js` and compares each string with the
   catalogue's head at that count, byte for byte;
4. runs `scan_head_spellings` and requires every hit to be in the declared set, the catalogue plus
   `EVALUATED_TEMPLATES`.

The other direction needs no scan. A declared template that is absent, or that declares no pattern,
already refuses in `run_pattern` before the scan runs. A declared template that spells the head in a
form the needle misses, an escaped space say, still has its pattern evaluated, so the scan must not
red it.

`scan_head_spellings` walks the checker's own directory and the memory-tree directory recursively,
skipping `__pycache__`, `*.md`, `*.test.sh` and any `X.js` beside an `X.template.js`. It returns each
file whose text carries the needle. The needle is the trailing run of letters-only words of the
catalogue's count-12 head, refused when it is shorter than two words, so the checker spells none of
the head itself. Run over the real tree at `9024901c` with the needle `this selection touches`, the
two directories held nine hits. The exemptions dropped six of them: two `.md` files, two `.test.sh`
files and two renders. That left exactly `gotchas.py`, `tier2-review.template.js` and
`unattended-build.template.js`. The whole-tree run added only records under `memory/`, which no
kit scan reaches. The near-miss `invariant(s)` hit one more file, `tools/workflows/README.md`,
already exempt as `.md`.

New outcomes, one self-test arm each: a format rendering a different head is DRIFT, exit 1; zero or
two `BY_DESIGN_FORMAT` declarations, or one that is not a one-line string literal, is REFUSING, exit
2; a hit outside the declared set is DRIFT naming the file; a needle shorter than two words is
REFUSING, because an empty needle is found in every file; a scan whose hits hold no file of the
declared set is REFUSING as a dead probe, because the declared templates exist by then and each
spells the tail, so a walk that reaches none of them would find a stray spelling no better. Its
fixture spells the tail through escapes and pieces only, so no file carries it as text. A catalogue that predates the block skips
before the scan, as today, so the flat fixture layout keeps its `SKIP`.

`check_parity` takes the directory holding the templates rather than one template path. Outside the
self-test that is the checker's own directory. The self-test's fixture head gains a letters-only tail
of at least two words, `# fixture head — {n} entry(s) in the fixture` for instance, or every
fixture would refuse on the needle. Its fixtures write both templates.

### S5 — one writer per verdict file

The skip sits before the `rm -f "$rf"` at `unattended.sh:2059`:

```sh
if [ -n "$RUNLOG_GITDIR" ] && [ -f "$RUNLOG_GITDIR/push-main-active" ]; then
  WC_WHY="push-main is landing from this git dir, so a claim push now would clear its verdict files: $RUNLOG_GITDIR/push-main-active"; rc=2
elif ...
```

The key is the git dir, not the repository. A landing pushed from the primary tree while beats run in
a linked worktree uses two git dirs, so the beat's push cannot touch push-main's files and is not
held back. Every caller already handles rc 2: `--beat` prints "skipped: the write did not complete",
the holder rows accept it, and a strict caller, `--preflight` or a take-over, refuses at check 109,
which is right while a landing is in flight. A marker leaked by a SIGKILL holds back claim writes in
that git dir until push-main's next run clears it on its EXIT trap, which the review's skeptic
judged acceptable.

### S6 and S7 — every refusal after the claim write leaves the call's writes undone

Above the gate, beside `check_ask_mandate`, `verb_preflight` runs the source-marker `region` test of
the build README, and the generated-marker `region` test of the record when the record exists and
`rotate` is not 1. Both are reads and both join `status` rather than returning. The scaffold's own
generated-marker test stays where it is, now inside the function.

The body from the rotation through `stage_or_fail` moves into `write_preflight_record`, called with no
arguments. Bash `local` is dynamically scoped, so it reads `verb_preflight`'s locals as the body does
today. `verb_preflight` becomes:

```sh
if ! write_preflight_record; then
  # restore both paths to HEAD; then the claim disposition below; then the refusal line
  return 1
fi
run_orphan_reap "$slug"
```

The restore takes each of the run-state path and, when one was derived, the archive path. A path
`HEAD` tracks gets `GIT checkout -q HEAD -- <path>`, which sets index and work tree. A path `HEAD`
does not track is unstaged with `GIT rm --cached -q --ignore-unmatch` and its file deleted. The
`PF_LCOPY` scratch copy is deleted as today. The tree was clean at the gate, so the restored state is
the found state, and the refusal then prints the existing "the run-state file is unchanged" line. A
restore step that itself fails prints one line naming the paths left changed, and the call still
exits 1 with its original check.

The claim disposition reads `CW_ACT` as the claim write left it:

| `CW_ACT` | on a failed `write_preflight_record` |
|---|---|
| `create` | `read_claims soft`, then `check_claim_writable "$slug" status "$_pf_cka" "${CLAUDE_CODE_SESSION_ID:-absent}" "$_pf_cka"`, then `write_claim "$slug" aborted "$_pf_cka" soft "" "$_pf_lu"`, and one line `unattended: claim marked aborted — <slug>, created by this refused call` |
| `renew`, `rewrite`, `take`, `take-announced` | nothing written, and one line `unattended: claim left — <slug> · <the action> · this call refused after it` |
| empty, with `RUN_CLAIMS` off or no claim written | nothing |

The created claim's status write passes through the `mine` row of the `status` column, because the
claim carries this call's keepalive and session. Writing `aborted` over a renewed claim would end a
live run's claim, and the claim a take replaced cannot be restored, which is why those rows leave it.
A status write that does not land prints `write_claim`'s own soft line. The slug's claim then reads
`live` and ages to `stale` after `RESUME_STALE_BOUND`, which the line names.

### S9 — `--claims` under an off switch

`print_claims` opens with `[ "$RUN_CLAIMS" = on ] || { echo "claims: off"; return 0; }`. Under the
switch's off value no verb writes or reads a claim, so a leftover claim on the remote is inert. It
shows again once the switch is on, and `git ls-remote <remote> 'refs/gov/runs/*'` reads it meanwhile.
The card's awk gains `$0 == "claims: off" { off = 1; next }`, and its `END` prints
`claims — skipped: RUN_CLAIMS is off` when `off` is set and no row was read. The card's fixture conf
for the existing claim arms declares `RUN_CLAIMS="on"`, so their verdicts do not move.

### S10 — check 24 under the soft policy

`read_claims` takes `quiet` and `soft` through the same branch: `resolve_claim_remote >/dev/null`,
then `status` and `RUNLOG_CHECKS` restored. The `soft` arm of the `CL_WHY` case already prints
`unattended: claims not read — the clone does not declare exactly one remote, check 24`, which
becomes the only trace. `strict` keeps check 24 as a refusal.

### S11 — the parked hand-off and its documented check

The park is one call:
`bash tools/unattended/unattended.sh --park aGraftedHelix --item location-probe-class-gate --reason "<question; options; reason>"`.
The reason is §8 F3's resolution in one line, without the field separator. The class record's
`## Its gate` section names the parked item and the run-state file holding it. The new class record,
`orchestrator-hand-off-owed-a-disposition`, says what M7 found. A spec's `hands-off` line addressed to
"this run's orchestrator" has no recipient the run tracks, so it is dropped unless the close checks it.
The documented check is to grep the build's specs for hand-offs naming the orchestrator and resolve
each to a unit or a parked row. It anchors on `RUN.md` and
`tools/workflows/unattended-build.template.js`, so a closing review's checklist selects it. Measured at
`9024901c`: 151 `hands-off** external` lines across all specs, of which one addresses an
orchestrator, unit 27's. A grep arm over the first population would red 150 legitimate deferrals,
which is why the check is documented rather than gated.

### S12 — the GH26 push leg

The leg runs after the existing one with the bare origin in place. `PATH` carries only a git shim
that fails `fetch ... refs/gov/runs/*` with exit 1 and logs every argument list. It runs the same
`s2` holder call and asserts three things: `grep -c ' push ' <log>` is 0, `git ls-remote origin
refs/gov/runs/tRun` prints the pre-call sha, and the call exits 0, its unread claim announced and its
lease recorded, as GH24's still-unreachable leg already asserts for the remote away. The staged break
is a driver copy routing the unread claim into a CAS with an empty expected sha. Under it the push is
attempted and rejected `(stale info)`, so the ref does not move and that assertion stays green, while
the push-count assertion reds; the exit reds beside it, because the rejected CAS is check 108 under
the holder policy. The existing leg keeps its add-failure assertions.

### S13 — the banner and the `superseded` line

Inside `test_empty_alias`, the arm splits stdout into lines and asserts that the line after the one
carrying ` hits for: ` equals `EVIDENCE_BANNER` and that `EVIDENCE_BANNER` occurs once. Inside
`_measure_spine_docs`, it asserts exactly one stdout line opens `superseded ` and that it carries
`unresolved`. Both arms that call the helper therefore assert it.

### S14 — one row regex

```python
def derive_row_re(conf):
    """The ONE row regex: a dash, optional emphasis, then an id of this tree's families."""
    return re.compile(r"^\s*[-*]\s+[`*]*(" + id_pattern(conf).pattern + r")\b")
```

Each of the five sites calls it, and `:811`'s `statusre` keeps its own build. The self-test arm reads
the module's own source through `__file__` with UTF-8 and counts the literal prefix of the row
regex. It requires one, so a sixth inline copy reds.

### Inventory

| identifier | where | cell |
|---|---|---|
| `write_preflight_record` | `tools/unattended/unattended.sh` | `sh.function` |
| `derive_row_re` | `tools/memory-tree/row_grammar.py` | `py.function` |
| `run_format`, `scan_head_spellings` | `tools/workflows/check_by_design_parity.py` | `py.function` |
| `EVALUATED_TEMPLATES` | `tools/workflows/check_by_design_parity.py` | constant |
| `BY_DESIGN_FORMAT` | `tools/workflows/unattended-build.template.js` | constant |
| `delta` | the spec commit block | shell array |
| `claims: off` | `--claims` output | the third line form of interface I2 |
| `orchestrator-hand-off-owed-a-disposition` | `memory/gotchas/` | class record |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` on
2026-10-05 and answered OK. No new check number is minted. The moved source-marker and
generated-marker branches keep their check-9 messages. The driver's fail branches are pinned in the
kit's sidecar, `tools/unattended/unarmed-branches.txt`, by check and per-check ordinal. Its one
check-9 row, ordinal 1, is `stage_or_fail`'s `cannot stage the run-state file`, which sits above
`verb_preflight`, so the moves leave its ordinal alone. AC9's arm asserts that message, which ARMS
the pinned branch, and the pin file is shrink-only and reds on an armed pin, so that row leaves the
file in the same commit.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js` by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/check-workflow-syntax.js`
- `tools/workflows/check_by_design_parity.py`
- `tools/workflows/tier2-review.template.js` and `tools/workflows/tier2-review.js`, the version line
- `tools/workflows/README.md`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/unarmed-branches.txt`
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`, the re-stamp
- `tools/memory-recall/selftest.py`
- `tools/memory-tree/row_grammar.py`
- `memory/map/features/unattended-stops.md`, `memory/map/features/review-harnesses.md`,
  `memory/map/features/session-kickoff.md`, `memory/map/generated/`
- `memory/gotchas/decision-re-derived-by-a-second-process.md`,
  `memory/gotchas/destructive-step-before-its-precondition.md`,
  `memory/gotchas/a-spelling-change-strands-its-readers.md`,
  `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`, the new class record,
  `memory/gotchas/INDEX.md` by `gotchas.py --write`
- `memory/builds/aGraftedHelix/RUN.md`, through `--park`
- every version carrier `tools/check-kit-versions.sh` pairs for the five kits

### Rollout

The batch is one pass. Its write sets overlap in three files, so it runs as these steps in this
order, each verified by its own criteria before the next starts:

1. `tools/unattended/unattended.sh` and its suite: S10, S5, S9's driver half, S6 with S7, S8's arm,
   S12. S10 goes first because S7's create row calls `read_claims soft`.
2. `skills/session-kickoff/manifest-check.sh` and its suite: S9's card half.
3. `tools/workflows/`: S1, then S2, then S3 and S4. S3 changes the template S1 also edits.
4. `tools/memory-recall/selftest.py`: S13. `tools/memory-tree/row_grammar.py`: S14.
5. Records: S15's dossier, the four gotcha sections and the new record, then S11's park.
6. S16: each kit's version once, renders and re-adoption, `gen_map.py --write`, `gotchas.py --write`,
   the manifest re-stamp.

Units 29, 30 and 31 are ordered before this one and edit `unattended.sh`, the gotcha catalogue and
the review harness. This unit reads the tree they leave, re-derives every line number above at its
pass's base, and bumps each kit once more after its own last move.

### Alternatives rejected

- **Delete the created claim with a lease** (the review skeptic's wording for M4). It contradicts the
  stops guide's "never deleted", a carrier change. §8 F1.
- **Card-only gating through a new `--claims` flag.** A new public surface. §8 F2.
- **Scaffold the record at a scratch path and rotate last** (the brief's suggested shape). Tested
  against the restore: a re-preflight of a LIVE record writes its facts in place, so a refusal after
  `write_lease` leaves the live record rewritten and the retry refuses at check 2, the same wedge.
  The restore covers it and the scratch path does not. §8 F4.
- **Refuse a non-empty index before the spec commit** (id 15's first option). The driver leaves
  `RUN.md` staged on every run, so it would refuse every spec commit, as the refuted id 5 showed.
- **A new leg for the pathless-commit ban.** Its population is the one `check-workflow-syntax.js`
  already derives, and a new leg trips the meta-gates shared invariant 5 names.
- **Derive the union's head from the first head it parsed.** With no input block there is nothing to
  derive from, so a literal fallback would return as a fourth spelling.

## 5. Production-readiness checklist

- security — S5 narrows a write channel and S7 writes only through the existing compare-and-swap
  path. No new credential, endpoint or ref namespace. The restore in S6 touches the two paths this
  call wrote, and only after the gate proved the tree clean.
- perf / scale — S9 removes one bounded remote read per SessionStart where the switch is off, up to
  `CARD_CLAIMS_BOUND`. S7 adds one claim read and one push on the create-then-refuse path only. S4
  walks two kit directories once per leg run. S13 adds no arm, so the recall self-test's wall clock
  does not move.
- error / empty / loading states — The restore names any path it could not put back. A status write
  that does not land names the claim left `live`. `claims: off` is a line, never an empty output. The
  checker's new outcomes exit 1 or 2 with a named line.
- observability — New lines: `claims: off`, `claims — skipped: RUN_CLAIMS is off`,
  `claim marked aborted —`, `claim left —`, the beat's skip naming `push-main-active`, the parity
  checker's per-template agreement lines and its population line.
- risks — AC9's arm arms a branch `tools/unattended/unarmed-branches.txt` pins, so that row is deleted
  from it in the same commit, or check-arms reds. The card suite's existing claim arms must
  declare `RUN_CLAIMS="on"` in their fixture conf, or they read `skipped`. Existing preflight arms
  that assert a refused call's tree state may now see a restored tree. The new class record meets the
  near-match relation check unit 9 added, so it names its relation to the nearest record. Five kits'
  version carriers move, and the kickoff manifest's re-stamp is owed beside them.
- testing — Every new assertion is observed red on its staged break before it lands: §6 names each
  break. The suites the arms live in run once at VERIFYING, at the main loop.
- migration — None. An adopter receives `claims: off` on update, and its card's cell reads `skipped`
  where its switch is off, which is the shipped default.
- user docs — `tools/unattended/VERBS.template.md` and its rendered guide, `tools/workflows/README.md`,
  and the three dossiers in §4.

## 6. Acceptance criteria

- **AC1** — When the GH16 real-git fixture of the build-harness suite also holds, before the block
  runs, a staged edit to its foreign tracked file and a staged new run-state file, and the extracted
  block runs over it in a scratchpad slice of that suite with `HERE` pinned to `tools/workflows`, the
  block exits 0. `git show --name-only --format= HEAD` then names neither path, and
  `git diff --cached --name-only` still lists both.
  Red when: the block's commit line names no pathspec, so `HEAD` holds the foreign edit.
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice.
- **AC2** — When `node tools/workflows/check-workflow-syntax.js` runs at the pass's commit, it exits
  0. Given explicitly a scratchpad copy of `tools/workflows/unattended-build.js` whose commit line has
  its ` -- ` pathspec part cut, it exits 1 and names the copy and the line.
  Red when: a workflow script carrying a pathless `git commit` line exits 0.
- **AC3** — When `cd tools/workflows && python check_by_design_parity.py ../memory-tree` runs at the
  pass's commit, it exits 0. Its output carries one agreement line for `tier2-review.template.js`
  and one for `unattended-build.template.js`, the latter naming both its pattern and its
  `BY_DESIGN_FORMAT` at each count in `SAMPLE_COUNTS`, and one population line naming three files.
  Red when: the build harness's format or pattern disagrees with the catalogue and the checker
  exits 0.
  figure: the counts are PINNED in `SAMPLE_COUNTS`, and the population count is DERIVED by the scan.
- **AC4** — When a scratchpad directory holds copies of `check_by_design_parity.py`,
  `tier2-review.template.js` and `unattended-build.template.js`, and
  `python <scratch-dir>/check_by_design_parity.py tools/memory-tree` runs over it, it exits 0 on the
  copies as shipped. With `by design` reworded inside the copy's `BY_DESIGN_FORMAT`, it exits 1 with a
  `DRIFT` line naming `unattended-build.template.js`. With that declaration cut, it exits 2 with a
  `REFUSING` line.
  Red when: a reworded or missing format exits 0.
- **AC5** — When the same scratchpad directory also holds a file `extra.py` carrying the head's
  fixed tail, the checker exits 1 with a `DRIFT` line naming `extra.py`. With `extra.py` gone and the
  `unattended-build.template.js` copy deleted, it exits 2 with a `REFUSING` line naming it.
  Its `--selftest` arm whose fixture spells the tail only through escapes reads a `DEAD PROBE`
  refusal. `python check_by_design_parity.py --selftest`, run in `tools/workflows`, prints
  `selftest: <n>/<n> arms`. Each new arm was observed FAIL once against a scratchpad copy of the
  checker with that arm's predicate disabled.
  Red when: an undeclared spelling exits 0, an absent declared template reads as parity, or fewer
  arms ran than declared.
  figure: `<n>` is DERIVED from `ARMS_DECLARED`.
- **AC6** — When a scratchpad slice of the driver suite plants `push-main-active` and a
  `pre-push-refusal` in the fixture's git dir, beside a live `tRun` whose claim is due under
  `RUN_CLAIMS="on"`, `--beat tRun` prints one `beat —` line skipped naming `push-main-active`.
  `pre-push-refusal` is byte-identical afterwards, and `git ls-remote origin refs/gov/runs/tRun`
  prints the pre-call sha.
  Red when: the claim push runs, which moves the ref and clears the refusal file.
- **AC7** — When the slice's `tRun` record reads `phase: ABORTED` and its README's build-index close
  marker is removed and committed, `--preflight tRun --keepalive-id k2` exits 1 with check 9.
  Its output carries no `retired the finished record` line, and `git status --porcelain` prints
  nothing. With a live record whose `<!-- /run:generated -->` line is removed and committed, under
  `RUN_CLAIMS="on"`, a re-preflight exits 1 with check 9, and `git ls-remote origin
  refs/gov/runs/tRun` shows the claim at its pre-call sha.
  Red when: the record is archived before the marker refusal, or the claim is pushed before it.
  fixture: the probe in §4 is this criterion's first half against today's driver, which reds it.
- **AC8** — When the ABORTED `tRun` is preflighted under a session id carrying a carriage return,
  `--preflight` exits 1 with check 17. `git status --porcelain` prints nothing, `git hash-object`
  of the record equals its `HEAD` blob, and no `RUN.ABORTED.*` path exists. A second
  `--preflight` under a clean session then prints `preflight OK` and archives the record.
  Red when: the archive and a fresh record are left in the tree, which is the probe's P3 row.
- **AC9** — When the ABORTED `tRun` is preflighted with a git shim on `PATH` failing only an `add`
  of the run-state file, `--preflight` exits 1 with check 9 and prints
  `the run-state file is unchanged`. `git status --porcelain` prints nothing and no
  `RUN.ABORTED.*` path exists.
  Red when: the restore is cut from a scratchpad copy of the driver, which leaves the rename staged.
- **AC10** — When `RUN_CLAIMS="on"`, no claim for `tRun` exists, and the ABORTED `tRun` is
  preflighted under AC9's shim, the call exits 1 and prints one `claim marked aborted` line.
  `bash tools/unattended/unattended.sh --claims` then prints `tRun` with status `aborted` and
  verdict `terminal`.
  Red when: the disposition is cut, so `--claims` prints `tRun` `live`.
- **AC11** — When a live `tRun` whose claim this session holds is re-preflighted under AC9's shim,
  the call exits 1 and prints one `claim left` line naming `renew`. `--claims` prints `tRun` `live`,
  and the record's `git hash-object` equals its `HEAD` blob.
  Red when: the create row's write runs on a renew, so the slug reads `aborted`, or the record is
  left rewritten.
- **AC12** — When `sed -n '/^verb_preflight()/,/^}/p' tools/unattended/unattended.sh` is read from
  its claim write to its end, it carries exactly one `return 1`, inside the branch taken when
  `write_preflight_record` fails. The suite arm that asserts this reds on a scratchpad copy of the
  driver with one `return 1` added after the claim write outside that branch.
  `python tools/memory-tree/check-arms.py --check` exits 0 at the pass's commit.
  Red when: a refusal after the claim write returns without the restore and the disposition.
- **AC13** — When a scratchpad fixture repository declares `RUN_CLAIMS="off"` and a git shim logs
  every call, `bash tools/unattended/unattended.sh --claims` prints exactly `claims: off`, exits 0,
  and the shim's log names no `fetch`. With `RUN_CLAIMS="on"` the same call logs one `fetch`.
  Red when: the remote is read under the off switch.
- **AC14** — When a scratchpad slice of the card suite runs `--card --write` over a fixture conf
  declaring `RUN_CLAIMS="off"`, the stored card's claims cell reads
  `claims — skipped: RUN_CLAIMS is off` and the git shim logs no `fetch`. The suite's existing claim
  arms keep their verdicts under a fixture conf declaring `RUN_CLAIMS="on"`.
  Red when: the off line is rendered as unreadable, or a fetch is logged.
  permission: the card suite is the main loop's; a pass runs the slice.
- **AC15** — When a preflighted `tRun` under `RUN_CLAIMS="on"` gains a second remote, `--dispatch`
  for a READY unit exits 0. Its output carries one `claims not read` line naming check 24 and no
  `UNATTENDED check 24 FAILED` line, and the run-state file gains exactly one dispatch row.
  Red when: the soft read keeps `status`, so the verb exits 1 after its record write.
- **AC16** — When `grep -n "location-probe-class-gate" memory/builds/aGraftedHelix/RUN.md` runs at
  the pass's commit, it prints one parked row carrying ` · reason `. When `grep -n
  "location-probe-class-gate" memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md` runs,
  it prints a line inside that record's `## Its gate` section.
  Red when: the hand-off has no parked row, or the class record still points at no recipient.
- **AC17** — When `python tools/memory-tree/gotchas.py --check` runs at the pass's commit, it exits
  0. `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` lists
  `decision-re-derived-by-a-second-process`, `destructive-step-before-its-precondition` and
  `a-spelling-change-strands-its-readers`. `--for-paths memory/builds/aGraftedHelix/RUN.md` lists
  `orchestrator-hand-off-owed-a-disposition`.
  Red when: a record's new section declares no gate or documented check, or no anchor selects it.
- **AC18** — When the driver suite's GH26 block runs as a scratchpad slice, the new push leg passes,
  its call exiting 0. Against a scratchpad copy of the driver routing an unread claim into a CAS with
  an empty expected sha, its `git ls-remote` assertion stays green and its push-count assertion reds,
  beside the exit assertion, since the rejected CAS is check 108.
  Red when: the push-count assertion stays green under that break.
- **AC19** — When a slice of the recall kit's self-test module runs, its source executed through
  `test_spine_nested_layout` with `__file__` set to the shipped module's path, every check the slice
  collects in `_checks` reads `ok`. With `tools/memory-recall/query.py` printing `EVIDENCE_BANNER` twice in the working tree,
  `test_empty_alias` reads `FAIL`. With `tools/memory-recall/extract.py`'s `superseded` print cut,
  both spine arms read `FAIL`. Restored, `git diff --quiet -- tools/memory-recall` exits 0.
  Red when: either break leaves the arms `ok`.
  cost: under a minute; the slice runs the arms defined above `test_spine_nested_layout` only.
- **AC20** — When `python tools/memory-tree/row_grammar.py --selftest` runs at the pass's commit, it
  prints `PASS — row_grammar: all arms held`. With a sixth inline copy of the row regex added to the
  module in the working tree, the new arm reads `arm FAIL`. Restored,
  `git diff --quiet -- tools/memory-tree/row_grammar.py` exits 0.
  Red when: a second copy of the row regex's literal prefix leaves the self-test passing.
- **AC21** — When `grep -nE "check (89|90)\b" memory/map/features/unattended-stops.md` runs at the
  pass's commit, it prints nothing. `grep -cE "check 10[789]" memory/map/features/unattended-stops.md`
  counts at least three.
  Red when: the dossier still sends a reader of the claim refusals to checks 89 and 90.
- **AC22** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, its `unattended`, `review-harness`, `memory-tree`, `memory-recall` and
  `kickoff-manifest` lines read `clean` at their bumped versions. `bash tools/check-kit-versions.sh`
  exits 0, and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a kit's shipped bytes moved and its version did not, or an installed guide differs from
  its template.
- **AC23** — When `python tools/codebase-map/test_codebase_map.py` runs at the pass's commit, every
  line reads `ok`. `bash skills/session-kickoff/manifest-check.sh` exits 0 over the re-stamped
  manifest.
  Red when: the map's generated artifacts are stale, or the manifest's audit stamp predates a change
  to a file it watches.

## 7. Gates

`unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `kickoff-manifest ratchet` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-grammar selftest` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `line length` · `govkit selfcheck` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · GH16 with a pre-staged foreign edit and run-state file; stage the commit line's pathspec cut · FLOOR_ASSERTIONS, raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · check-workflow-syntax.js over a fixture script with a pathless commit line and one with a pathspec; stage the ban's predicate inverted · FLOOR_ASSERTIONS
New arm: check_by_design_parity.py --selftest · a reworded format, a missing format, an undeclared spelling, a needle shorter than two words, a scan reaching no declared file; each predicate disabled in a scratch copy · ARMS_DECLARED, raised by five
New arm: tools/unattended/unattended.test.sh · the push-main marker (S5), the preflight restore and claim disposition (S6, S7), the post-claim return structure (S8), the soft check-24 read (S10), the GH26 push leg (S12); each break as §6 names it · the suite's printed count
New arm: skills/session-kickoff/manifest-check.test.sh · the claims cell under RUN_CLAIMS off; stage the off branch cut from the card's awk · FLOOR_ASSERTIONS, raised by the assertions added
New arm: tools/memory-recall/selftest.py · the banner and superseded assertions inside two existing arms; stage each print doubled or cut · none, SELFTEST_ARMS holds
New arm: row_grammar.py --selftest · the row regex's literal prefix counted once; stage a sixth inline copy · none

The kit suites are not on the bar. A pass runs every criterion above directly, through slices where a
criterion lives in a suite, and the main loop runs those suites once at VERIFYING.

## 8. Open questions

- **F1 — M4's claim, when this call created it: delete the ref with a lease, or write it `aborted`?**
  The review skeptic's corrected fix deletes it. The stops guide's section 7 says a claim is never
  deleted, and unit 1 kept terminal claims on purpose. A deletion therefore changes a governance
  carrier, which is M3 veto 2, and needs a new push form besides. Writing `aborted` reuses the
  status-write block `--abort` already runs, and the next preflight takes a terminal claim. That
  leaves an `aborted` row on the remote for a run that never started, which is truthful.
  RESOLVED (agent, 2026-10-05, delegated): write `aborted` through the status-write block, and only
  when `CW_ACT` is `create`.
- **F2 — M5: gate the card's read on the switch through `--claims` itself, or through a new mode?**
  A new flag or mode is a new public surface on the driver, M3 veto 2. A `claims: off` line keeps
  one reader of the switch, the driver. It costs the operator the read of leftover claims while the
  switch is off, and those claims are inert then. VERBS already documents the line forms, and its
  "reads whatever RUN_CLAIMS says" would state false behaviour, which is the edit rule shared
  invariant 10 gives the unattended templates.
  RESOLVED (agent, 2026-10-05, delegated): `claims: off`, with VERBS amended.
- **F3 — M7: adopt the location-probe class gate, or park it?** The options seen: build it inside
  this batch; adopt it as a new unit; park it. Inside this batch it is a second mechanism, a gate
  with its own population and home, which M2 makes a unit of its own. A new unit id is the
  orchestrator's to mint, and this writer may not. Measured in the class record at `f0971667`, the
  line predicate finds 26 probes. Whether a hook can reach one is a question about callers, so no
  line predicate discriminates the class, and M12 rejects a test that cannot change the pick. No
  option survives for this unit.
  RESOLVED (agent, 2026-10-05, delegated): park it with `--park`, recording these options and that
  reason, and point the class record at the row. The orchestrator or the owner may still adopt it.
- **F4 — The rotation fix: scaffold at a scratch path and rotate last, or restore the call's writes
  on any refusal after the gate?** The brief suggested the first. The test that separates them is a
  re-preflight of a LIVE record that refuses after `write_lease`. Rotating last does not cover it,
  because a live record is written in place and stays rewritten. Restoring to `HEAD` covers it,
  because `check_clean` proved the tree clean at the gate. The restore is also the smaller change,
  one branch around one function.
  RESOLVED (agent, 2026-10-05, delegated): the restore, with the two pure reads moved above the
  gate as the review's fix states.
- **FACT-QUESTION · F5 — Does one `--preflight` call print "the run-state file is unchanged" after
  it has rotated?** Probe: the scratchpad slice of the driver suite in §4, cases P1 to P3, reading
  each call's output and `git status --porcelain`. Liveness: P2 and P3 show the probe observes a
  rotation when one happens, and P1 shows it observes none when none does, so it can answer either
  way. Observation: in no case did one call print the line after rotating, and in P2 and P3 the
  second call printed it over the first call's rotation.
  RESOLVED (agent, 2026-10-05, delegated): one call does not; two calls do, and S6's restore makes
  the second call's line true by making the first call's refusal leave nothing behind.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the unit-29-to-32 spec brief and the closing review's M1
  to M9 and L1 to L4 sections, grounded at `9024901c`, with the rotation probe and the pathspec
  measurement run on node `a`.
- rev-2 · 2026-10-05 · S12 and AC18 disagreed with the driver: a holder call over an unread claim
  exits 0 on the correct driver, so "does not exit 0" would red it. Measured in the pass's slice of
  the driver suite, the leg asserts exit 0, and under the staged CAS break the exit reds beside the
  push count while the ref assertion stays green.
- rev-3 · 2026-10-05 · S4 and AC5: the pass's bug-class checklist selected
  `vacuous-selector-empty-population`, and the derived scan had no liveness. A walk that reached no
  file read `population — 0 file(s)` and exited 0, so a scan that finds no file of the evaluated
  set now refuses as a dead probe, with a fifth self-test arm.

## 10. Reuse audit

The map probes were these two:

```bash
python tools/codebase-map/reuse_lookup.py "undo a remote claim write when a later preflight step refuses"
python tools/codebase-map/reuse_lookup.py "commit only the named paths and leave other staged entries staged"
```

Both `reuse_lookup.py` probes ranked name-stem neighbours only, `write`, `claims` and `*_path` helpers
in other kits, and both printed `unscanned layers: .sh`. Their miss is no evidence about the driver or the commit block,
which are shell, so both were read by hand. The seams extended are these. The status-write block at
`tools/unattended/unattended.sh:5488` is reused verbatim for S7. `check_claim_writable` and
`write_claim` are called, not changed, except for S5's one guard. `read_claims` keeps one restore
branch for two policies. The existing `PF_LCOPY` clean-up and the gate's own refusal line carry S6.
`tools/workflows/check_by_design_parity.py` gains the third template through its own `run_pattern`
shape. `check-workflow-syntax.js` lends its `discovered()` population to S2. `id_pattern` gains its
sibling in S14. The GH16 fixture, the GH26 shims, the card suite's claim fixture and `selftest.py`'s
two arms are each extended in place.

Recall surfaced `TOOL-aBranchedMandate-9`, the open ask this unit closes, whose fix shape ("hoist both
region checks above the write gate") S6 takes and widens. It surfaced
`memory/gotchas/destructive-step-before-its-precondition.md` and
`memory/gotchas/decision-re-derived-by-a-second-process.md`, which S8 and S5 extend rather than
duplicate. It surfaced `TOOL-aGraftedHelix-10` S3, which made `write_claim` clear the refusal file and
which S5 bounds. And it surfaced `TOOL-aGraftedHelix-16` and `TOOL-aGraftedHelix-21`, the commit
block's two earlier repairs, which S1 keeps intact. The recall result and the current code disagreed
once: the aBranchedMandate-9 row says the scaffold runs before both region checks, and since
`TOOL-aPromptedMandate-6` the source-marker check runs before the scaffold, though still after the
rotation. §4 follows the code.

Recall terms used: write gate destructive-step precondition preflight rotation claim compare-and-swap refusal pre-push-refusal lander-marker verdict push-main-active

The question passed with them: "what rules govern a refusal after a destructive write, a remote claim
write, and the verdict files a lander reads".

Recall terms used: spec-commit pathspec foreign staged index Pass-none by-design head parity spelling population declared two-answers

The question passed with them: "how does the spec commit stage keep foreign staged work out of its
commit, and what holds the by-design head equal across kits".
