# TOOL-dRedressedBar-4 — the `workflows` homonyms the install-prefix ban reads as a kit path, held in a named constant

**Status:** SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |

<!-- /gen:spec-records -->

## 1. Goal

The `install-prefix (shipped surface)` leg is red at `ebce889c` on two lines. Each line's quoted
`workflows` names Claude Code's own per-session directory of Workflow runs, not the review-harness
kit. Each site holds that directory name in one named constant, so the gate's pure ban reads no kit
literal there and the leg goes green without a waiver, a predicate change or a pin.

## 2. Scope (IN)

- **S1** — `tools/hooks/format-guard.js` declares `const WORKFLOW_RUNS_DIR = 'workflows'` in its
  module-level constants block (format-guard.js:93-101). The join in `readJournalAgents`
  (format-guard.js:333) names `WORKFLOW_RUNS_DIR` where it now spells the quoted literal.
  Observed by AC1 and AC2.
- **S2** — The arm-9 fixture program `A9_WRITE` in `tools/roles/adopt-roles.test.sh` (lines 197-236)
  declares `WORKFLOW_RUNS_DIR = "workflows"` beside `sub = sess.with_suffix("") / "subagents"`
  (line 222). The `wf =` line (line 228) becomes `wf = sub / WORKFLOW_RUNS_DIR / "wf_00000001-aaa"`.
  Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- No edit to `tools/check-install-prefix.sh` or its self-test. The ban stays as written, and its
  rule 4 and `NONKIT` heuristic are not widened (§4, Alternatives rejected).
- No edit to the other sites that spell the same directory and read clean today:
  `tools/roles/handoff.py:854` and `:885`, `tools/runlog/extract.py:256`, and `tools/runlog/selftest.py`.
  `tools/runlog/extract.py:256` holds the census site `sdir / "workflows"` that
  `tools/check-install-prefix.test.sh:149` requires to exist, so touching it would red that census.
- No change to what `readJournalAgents` reads, refuses or returns, and no change to arm 9's
  assertions.
- No kit version bump. Both touched files ship: `format-guard.js` from the hooks kit
  (tools/hooks/kit.toml:88) and `adopt-roles.test.sh` from the roles kit (tools/roles/kit.toml:47).
  The bump is unit 7's, measured over the finished tree.
- No conversion of the fork idioms in `tools/roles/adopt-roles.test.sh` (unit 5's) and no new arm in
  it (unit 6's).

### Edges

- **hands-off** `TOOL-dRedressedBar-7` — the hooks and roles kit version bumps for the shipped bytes
  this unit moves, which that unit derives by measurement over the tree the build leaves.

## 4. Design

### The cause, measured

The leg log at `.git/worktrees/gov-bar-profile-failures-b80cc3/gate-logs/install-prefix__shipped_surface_.log`
names exactly two hits, both under the kit name `workflows`:

| Site | Line | Rule-4 branch that counts it |
|---|---|---|
| `tools/hooks/format-guard.js:333` | `path.join(sessionDir, 'subagents', 'workflows', runId, 'journal.jsonl')` | comma: a quoted literal segment and a comma before it inside an open `join(` (check-install-prefix.sh:355-359) |
| `tools/roles/adopt-roles.test.sh:228` | `wf = sub / "workflows" / "wf_00000001-aaa"` | slash: joined by `/`, and the operand `sub` matches no `NONKIT` alternative (check-install-prefix.sh:352-354, 272) |

The kit-name alternation is derived from the directories under the tool root
(check-install-prefix.sh:215), so `workflows` is a kit name because `tools/workflows/` is a kit.
The comma branch never consults `check_homonym`; only the slash branch does. A homonym on the comma
branch is therefore counted whatever the join's first argument is named.

The gate's header states what it does not read (check-install-prefix.sh:59-60): "a path ASSEMBLED
FROM TWO VARIABLES. A kit's name held in a variable and joined at run time spells no literal". A
named constant is that form.

### The change

At each site, one constant holds the directory name. The join names the constant. The literal
appears once, as a plain assignment with nothing beside it that rule 4 reads.

- **format-guard.js.** Add `const WORKFLOW_RUNS_DIR = 'workflows'` to the constants block at
  lines 93-101, after `RUN_ID_RE`. It has the same shape as `SIDECAR_DIR = 'format-guard'` at line 97.
  A one-line `//` comment goes on the line ABOVE it. The comment says the constant is Claude Code's
  per-session directory holding one subdirectory per Workflow run, not the review-harness kit.
  Line 333 becomes `path.join(sessionDir, 'subagents', WORKFLOW_RUNS_DIR, runId, 'journal.jsonl')`.
  The doc comments at lines 48 and 325 stay as they are. Their `/workflows/<run id>/` spelling
  is followed by no `<name>.<ext>`, so rule 3 does not count it, and the log confirms they are clean.
- **adopt-roles.test.sh.** Inside the `A9_WRITE` program, add `WORKFLOW_RUNS_DIR = "workflows"` on
  its own line directly after line 222, with a one-line `#` comment above it saying the same thing.
  Line 228 becomes `wf = sub / WORKFLOW_RUNS_DIR / "wf_00000001-aaa"`. The fixture keeps its own
  constant rather than importing anything from `tools/roles/handoff.py`. A fixture that derived the
  path from the reader under test could not catch that reader drifting.

Both sites use the same constant name, so the two places this directory is held read alike.

### Constraints the builder must hold

These were measured by running a copy of rule 4's regexes over the candidate lines. That probe was
a script of this spec writer's, not the gate.

- **Nothing may follow the declaration's closing quote on its line.** A trailing
  `/* … */` comment makes rule 4's slash branch count the declaration
  (`re.match(r"\s*/(?!/)", after)` at check-install-prefix.sh:352). A trailing `//` comment is safe,
  but the comment goes above the line anyway, so the rule needs no reading.
- **No apostrophe anywhere in the `A9_WRITE` program.** It is a bash single-quoted string from
  line 197 to the closing quote on line 236. One apostrophe, as in "Claude Code's", ends the string
  early. Write "the Claude Code session" or similar. The extracted program carries zero apostrophes
  at `ebce889c`, and AC4 pins that.
- **Neither comment may spell `workflows/` directly followed by a `<name>.<ext>` file name.** That is
  rule 3's shape (check-install-prefix.sh:335-346).
- The constant's line must not sit inside a `join(`, `joinpath(` or `Path(` call, nor after a quoted
  segment and a comma.

### Inventory

| Identifier minted | Where | What grades it |
|---|---|---|
| `WORKFLOW_RUNS_DIR` | `tools/hooks/format-guard.js`, module scope | no naming cell: `lexicon naming predicates` grades function declarations and arrow functions (tools/lexicon/lexicon.py:146), not a string constant |
| `WORKFLOW_RUNS_DIR` | `tools/roles/adopt-roles.test.sh`, inside the `A9_WRITE` Python program | the same; it is a fixture-local name |

### Files touched (estimate)

`tools/hooks/format-guard.js`
`tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **Rename the operand so `NONKIT` exempts it.** This is the remedy the gate's own comment names
  (check-install-prefix.sh:269-271). It is also how `tools/roles/handoff.py:854` spells this path
  clean, as `sdir / "subagents" / "workflows"`. It works for the slash site only. The probe shows the
  comma site at format-guard.js:333 still counts under any first-argument name, because the comma
  branch never calls `check_homonym`. Taking it at one site and the constant at the other would be
  two remedies for one class, so it is rejected.
- **Widen rule 4's comma branch to consult `check_homonym` on the join's first argument.** This
  would clear format-guard.js:333 through the existing `session` alternative and gate the class
  rather than the instance. It is rejected for four reasons. It moves a second shipped engine,
  `tools/check-install-prefix.sh`. It moves that gate's self-test floor and its `NONKIT` census.
  It narrows a ban the gate's header calls pure. And the owner-confirmed brief directs the
  code-side remedy. The brief's non-goal refuses relaxing a guard to absorb a red that a code
  change can fix.
- **Spell the two segments as one string, `'subagents/workflows'`.** Rules 3 and 4 do not count it.
  But it hides the homonym inside a string the gate cannot parse, and it names nothing. A named
  constant says what the directory is.
- **The laundering objection, answered.** `TOOL-dRetiredFork-39` confirmed a variable that carried
  real kit paths past this ban without buying portability. This constant carries no kit path.
  `<session dir>/subagents/workflows/` is a directory of Claude Code's, which no install prefix
  moves, so nothing is laundered. The ceiling is stated in §5 risks.

## 5. Production-readiness checklist

- security — N/A — the read path is unchanged. `readJournalAgents` still builds the path only from a
  run id that matches `RUN_ID_RE` (format-guard.js:330-332), and the constant is a fixed literal.
- perf / scale — N/A — a module-scope constant replaces a literal. There is no new work per call.
- error / empty / loading states — unchanged. An unreadable journal still returns
  `{ error: "the journal … is unreadable (…)" }` (format-guard.js:335). AC2 observes the success
  path, and its red case observes this one.
- observability — N/A — no message, log line or exit status changes.
- risks — The constant sits in the gate's stated blind spot (check-install-prefix.sh:59-60). A
  later edit that put a REAL kit's name into such a constant would also pass the ban. The name
  `WORKFLOW_RUNS_DIR` and its comment are what tell a reader the value is Claude Code's directory.
  Nothing gates that the value stays a homonym. A second risk is the apostrophe trap in `A9_WRITE`
  (§4), which AC4 observes.
- testing — AC2 probes `readJournalAgents` directly against a planted journal. AC4 runs the
  extracted arm-9 fixture writer. At the close, the `format-guard self-test` exercises the same read
  through the hook (its `journal("workflows/wf_t-1", …)` scenario, tools/hooks/format-guard.test.sh:357).
  The `roles adopter self-test` exercises arm 9 end to end.
- migration — N/A — no data, conf or receipt shape changes. An adopter receives the new bytes on
  its next `govkit apply` once unit 7 bumps the two kits.
- user docs — N/A — no behaviour changes. `help/` has no page naming the journal path (`git grep -l
  journal -- help` prints nothing). `tools/hooks/README.md:462` describes the path, and that path
  is unchanged.

## 6. Acceptance criteria

- **AC1** — When `git grep -nE "['\"]workflows['\"]" -- tools/hooks/format-guard.js` runs, it prints
  exactly one line, the `const WORKFLOW_RUNS_DIR = 'workflows'` declaration, with nothing after the
  closing quote. When `git grep -n WORKFLOW_RUNS_DIR -- tools/hooks/format-guard.js` runs, it prints
  that declaration and the `readJournalAgents` join line, and no third line.
  Red when: the quoted literal is put back into the `path.join` call, and the first command prints
  a second line naming line 333's successor.
  figure: DERIVED — "one line" is counted at observation time. At `ebce889c` the first command
  prints one line, the join itself.
- **AC2** — Plant `<scratch>/s/subagents/workflows/wf_p-1/journal.jsonl` holding the two lines
  `{"type":"started","agentId":"a1"}` and `{"type":"result","agentId":"a1"}`. Then
  `node -e 'const g = require("./tools/hooks/format-guard.js"); console.log(JSON.stringify(g.readJournalAgents(process.argv[1], "wf_p-1")))' <scratch>/s`
  run from the repo root prints `{"started":["a1"],"ended":["a1"]}`.
  Red when: `WORKFLOW_RUNS_DIR` holds any other value, and the same command prints an `error` key
  naming the journal as unreadable.
  fixture: built by the probe under the run's scratchpad. This spec writer ran the same probe at
  `ebce889c` and it printed the expected line.
- **AC3** — When `git grep -nE "['\"]workflows['\"]" -- tools/roles/adopt-roles.test.sh` runs, it
  prints exactly one line, `WORKFLOW_RUNS_DIR = "workflows"`, with nothing after the closing quote.
  `git grep -n "wf = sub / WORKFLOW_RUNS_DIR / " -- tools/roles/adopt-roles.test.sh` prints the
  fixture's `wf =` line.
  Red when: the `wf =` line spells the quoted literal again, and the first command prints that line
  too.
- **AC4** — Extract the arm-9 program with
  `sed -n "/^A9_WRITE='/,/'\$/p" tools/roles/adopt-roles.test.sh | sed "1s/^A9_WRITE='//; \$s/'\$//" > <scratch>/a9.py`.
  `grep -c "'" <scratch>/a9.py` prints `0`. Then
  `python <scratch>/a9.py <scratch>/fx <scratch>/sess/x.jsonl memory/builds/tFix/prompts/p.md`
  exits 0, and `test -f <scratch>/sess/x/subagents/workflows/wf_00000001-aaa/journal.jsonl` succeeds.
  Red when: the constant holds any other value, so the journal lands elsewhere and `test -f` fails.
  Also red when the new comment carries an apostrophe, so the `grep -c` prints a non-zero count.
  fixture: built by the probe. `eval` of the extracted assignment is refused by this repo's
  worktree hook, which is why the probe writes the program to a file. This spec writer ran the
  extraction and the writer at `ebce889c`: 0 apostrophes, and the journal was planted at that path.
  figure: DERIVED — the apostrophe count is taken at observation time, and it is 0 at `ebce889c`.

## 7. Gates

The leg this unit turns green, the six legs the `{prefix}/hooks/` guard owes for the hook edit, and
the suites that run both edited sites end to end. The main loop observes them once, at the close.

`install-prefix (shipped surface)` · `format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `roles adopter self-test` · `foreign-prefix parity (every self-test at three prefixes)`

At the close, `install-prefix (shipped surface)` reads `GATE ok` with its two logged hits gone and
no other hit added. That is this unit's own red leg, and the build brief's acceptance names it.
`kit epoch (shipped bytes move, the version moves)` and `kit version markers` read red at this
unit's tip by construction, until unit 7 bumps the hooks and roles kits. They are judged at the
close, not here. `foreign-prefix parity (every self-test at three prefixes)` reds at `ebce889c` on
the roles adopter's missing probe stop, which is unit 1's fix. Unit 1 is ordered before this unit.

This unit adds no suite arm and moves none. The ban it satisfies is an existing leg that was already
observed red, in the leg log §4 cites.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, authored by the dRedressedBar build harness's spec writer from
  the brief at `memory/builds/dRedressedBar/prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md`.

## 10. Reuse audit

The seam this unit extends is the existing module-level constants block of
`tools/hooks/format-guard.js` (lines 93-101). Its `SIDECAR_DIR = 'format-guard'` already holds a
directory name in a named constant. The fixture side extends the `A9_WRITE` program's own top-level
names. `python tools/codebase-map/reuse_lookup.py "hold a directory name that collides with a kit name in a named constant so a path join spells no kit literal"`
returned `resolve_kit_dir`, `kit_rel` and `kit_dir` as the leading seams. Every one of them resolves
a REAL kit's directory in an install, and `workflows` here is not a kit, so none of them fits a
homonym. The recall probe surfaced the precedent spelling at `tools/roles/handoff.py:854`. It reads
clean through the `NONKIT` name heuristic, and §4 records why that remedy does not reach the comma
site. It also surfaced `TOOL-dRetiredFork-39`, the laundering finding that §4 answers. The map and
the source agree on every line cited here, and no hit was stale.

Recall terms used: `python tools/memory-recall/query.py "how does a shipped file spell Claude Code's own subagents workflows session directory without tripping the install-prefix ban" --terms "install-prefix homonym workflows subagents journal session NONKIT pure ban kit segment constant"`
