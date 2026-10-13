# TOOL-aOrientedCast-25 — the second closing review's roles minors: one marker reading, armed rules, one fence reading, and records that say what was built

**Status:** OPEN · rev-3 · 2026-10-13 · node a · Tier-2 · base 646d4a73581393acbf42f33864a9808c96d00a0c · streams tooling · order 27 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-24-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-24-1-spec-brief.md) | journal | TOOL-aOrientedCast-24 |
| [2026-10-13-prompt-TOOL-aOrientedCast-24-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-24-2-build-brief.md) | journal | TOOL-aOrientedCast-24 |
| [2026-10-13-prompt-TOOL-aOrientedCast-25-1-spec-writer.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-25-1-spec-writer.md) | journal | — |
| [2026-10-13-prompt-TOOL-aOrientedCast-27-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-27-1-spec-brief.md) | journal | TOOL-aOrientedCast-27 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes review items M4, M5, M6, L4, L5, L6 and L7 of
[the second closing review, round 1](../reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md).
Two readers of one marker line and three of one fence are made to give one answer and a check
compares them; the rules and verbs the reviewed diff added gain the persisted arms they lack; and
the records that misstate what was built are corrected where a CLOSED spec can be corrected.

## 2. Scope (IN)

- **S1** — M4, the reader. `tools/roles/roles_lib.py` gains `extract_prompt_marker(prompt)`, the
  one Python reading of the marker line an `Agent` prompt opens with, written to give the hooks
  kit's spawn guard's answer (its rule 6). The `--handoff` matcher in `print_agent_lines`
  (`tools/roles/handoff.py:814-816`) calls it instead of comparing the prompt's raw first line. The
  `handoff.py` docstring and the `agents` paragraph of `tools/roles/README.md` (`:84-86`) say so.
  Observed by AC1 and AC2.
- **S2** — M4, the arms. Arm 9 of `tools/roles/adopt-roles.test.sh` gains one assertion: its
  session's `Agent` prompt, prefixed with one blank line, still yields arm 9's two lines. A new
  arm 11, part A, feeds five prompt variants to `extract_prompt_marker` and to the spawn guard and
  asserts the two agree on each. Observed by AC1 and AC2.
- **S3** — M5. A new arm 10 of `tools/roles/adopt-roles.test.sh` runs, in one scaffolded fixture,
  the stand-in refusal of `handoff.py render --stand-in`, the R15 join of `check_roles.py` in both
  directions and over eight malformed rows, R13, R14, and R0's refusal of a conf with no memory
  root, one assertion per step of §4 "Arm 10". Observed by AC3 and AC4.
- **S4** — M6. Arm 9 gains two assertions over the fixture it already writes:
  `handoff.py agents --run wf_00000001-aaa` prints exactly the three lines of §4 "Arm 9", and the
  build's agent ledger gains exactly those three. Observed by AC5.
- **S5** — L4, the reader. `extract_microformat_shapes` in `tools/roles/roles_lib.py`
  (`:220-235`) reads the fence as format-guard's `readCharterShapes` reads it: each marker a whole
  line, the first opener and the first closer, and the last definition of a head kept. Its
  docstring, the module docstring and the README's sentence (`:82-83`) say so. Observed by AC6.
- **S6** — L4, the parity arm. Arm 11, part B, feeds three charter copies to
  `extract_microformat_shapes` and to `readCharterShapes` and asserts the same `agent` and
  `returned` definitions from both. Observed by AC6.
- **S7** — L4, the source. `tools/check-microformats.sh` counts only whole-line fence markers, and
  a new `fail 9` refuses a head two definitions share. `tools/check-microformats.test.sh` gains one
  arm for each, and its floor moves from 18 to 20. The meta-gate's floor for the gate in
  `.memory-tree.conf`'s `ARMS_FLOORS` moves from 8:8 to 9:9, and because that conf is in the
  kickoff manifest's `watch:` list, `memory/guides/SESSION-KICKOFF.md` takes a `last-audit`
  re-stamp. Observed by AC7; the re-stamp is NOT OBSERVED by a criterion, because the kickoff
  manifest ratchet grades it at the close.
- **S8** — The suite's bookkeeping. The header of `tools/roles/adopt-roles.test.sh` lists arms 10
  and 11 and states what arm 11 does not compare, and `FLOOR_ASSERTIONS` moves from 19 to 33.
  Observed by AC5.
- **S9** — L5 and L6. This unit's acceptance ledger record carries a section,
  `## Criteria amended in closed specs`, with one sub-head for `TOOL-aOrientedCast-21` AC2 and one
  for `TOOL-aOrientedCast-22` AC6, each giving the criterion as written, what the code does, and the
  observation that stands. The record's Serves line names both units. Observed by AC8.
- **S10** — L5 and L6, the class. The gotcha record
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains a fourth form, an
  absence its own records break by quoting the pattern, with both instances under "Where it bit",
  and `memory/gotchas/INDEX.md` is regenerated. Observed by AC9.
- **S11** — L7. The Shared seams bullet of `memory/map/features/roles.md` (`:123-126`) that calls
  two charter readings the only contract read from outside the kit becomes a list of every outside
  read, each marked a contract or a reading. Observed by AC10.
- **S12** — The roles kit moves from 1.3 to 1.4 over its four carriers, after the unit's last edit
  of `tools/roles/`, and the map's generated artifacts are re-rendered for the new function.
  Observed by AC11.
- **S13** — `handoff.py agents` prints and writes nothing unless given `--write`, which adds the
  complete lines to the agent ledger as before (§4 "The write flag"). Its docstring, the README's
  "The agent lines", `help/roles.md`'s "What each agent line tells you" and the Skill template's
  agents bullet (`:26-30`) say a mid-pass call runs without it. Observed by AC12.

## 3. Non-goals (OUT)

- No edit of `tools/hooks/` or of the run-log kit. The spawn guard's rule 6 and format-guard's
  fence reader are read as they stand, and both hooks files are `TOOL-aOrientedCast-24`'s. M4's
  fix needs no hooks edit: rule 6 stays the owner of the marker reading, the Python reader points
  at it, and arm 11 compares the two, which is the second form of the charter's `[one-fact]` rule.
- No edit of a CLOSED spec. L5 and L6 are corrected in this unit's record (F4).
- No `closes` verb in the status header (F3).
- No fixture arms for R1 to R12, which the review notes lack them too: a convention older than the
  reviewed diff. This unit arms the rules that diff added.
- No change to spec 22's AC7 or to the unattended README: review item L2 is
  `TOOL-aOrientedCast-24`'s.
- No new gotcha record. M4, M5, L4 and L7 carry classes the catalogue already holds, and each gains
  an arm here or is documentation; L5 and L6 extend an existing record (S10).
- No refusal of a repeated head inside `handoff.py` or either hook: the source refuses it (S7), and
  every reader keeps the last.
- No `help/` page: the only behaviour a user can see move is a prompt with a leading blank line now
  matching its handoff.
- No version bump for the hooks, unattended or run-log kits. `check-microformats.sh` carries no
  version: its descriptor's `version_from` is `none`, and `govkit.py epoch` skips such an entry.

**What it is built on.** S1, S2 and S4 extend `TOOL-aOrientedCast-20`'s `print_agent_lines` and arm
9; S3 arms the rules of `TOOL-aOrientedCast-17` and `TOOL-aOrientedCast-19`; arm 11 reuses
`TOOL-aOrientedCast-15`'s arm 6 idiom and reads `TOOL-aOrientedCast-7`'s rule 6. Those specs are
CLOSED and declare no edge to this unit, and a one-sided edge reds the hygiene gate's join, so the
dependency is stated here rather than as an edge.

**It writes none of `TOOL-aOrientedCast-24`'s files, and reads two of them.** Arm 11 runs the
spawn guard and loads format-guard's exported `readCharterShapes`, and AC8's probe calls its
exported `checkAgentLines`. That unit is `order 26`, builds first and moves none of the three. Both
units may re-render `memory/gotchas/INDEX.md` and `memory/map/generated/`; a generated index is
re-rendered from the tree, never reconciled, and this unit renders second.

### Edges

none

## 4. Design

### The marker reader (S1)

The spawn guard admits an `Agent` call by two tests (`tools/hooks/agent-cap.js:2099` and
`tools/hooks/agent-cap.js:2121-2125`): exactly one line of the prompt, carriage returns removed and
nothing else trimmed, matches its whole-line marker pattern (`tools/hooks/agent-cap.js:2041-2053`),
and that line equals the prompt's first line once CRLF is folded, the two ends trimmed and that
line's trailing whitespace dropped. `handoff.py` compares only the raw first line
(`tools/roles/handoff.py:815`), so a prompt opening with a blank line is admitted by the guard and
unmatched by the verb.

```python
def extract_prompt_marker(prompt):
    """The `MARKER_RE` match of the marker line an `Agent` prompt opens with, read as the hooks
    kit's spawn guard reads it (its rule 6): exactly one line, carriage returns removed, is a whole
    marker line, and it is the prompt's first line once CRLF is folded, the two ends trimmed and
    that line's trailing whitespace dropped. None otherwise (TOOL-aOrientedCast-25)."""
    text = str(prompt)
    marks = [ln for ln in (raw.replace("\r", "") for raw in text.split("\n")) if MARKER_RE.fullmatch(ln)]
    first = text.replace("\r\n", "\n").strip().split("\n")[0].rstrip()
    return MARKER_RE.fullmatch(first) if len(marks) == 1 and first == marks[0] else None
```

The matcher at `tools/roles/handoff.py:814-816` keeps its other two tests and reads the prompt
through it: `(m := lib.extract_prompt_marker(c["input"].get("prompt", ""))) and m.group(0) ==
marker.group(0)`. A probe at writing answered as arm 11's table states, and None for a second
marker line. The README
sentence reads: every `Agent` call whose prompt opens with that file's marker line as the spawn
guard reads it, through `roles_lib.extract_prompt_marker`, and whose result names an agent.

### Arm 9, extended (S2, S4)

After arm 9's two `--handoff` runs, from the fixture root:

1. `handoff.py agents --run wf_00000001-aaa --session "$A9S"` exits 0 and its stdout, CR stripped,
   equals these three lines in order:

   | Line | Text |
   |---|---|
   | A9L3 | `- agent — gov-builder · effort xhigh · model claude-test-2 · TOOL-tFix-1 · prompt [${A9H##*/}]($A9H) · writes product · gates lexicon naming predicates · run wf_00000001-aaa/a0000000000000002` |
   | A9L4 | `- returned — gov-builder · committed abc123def · 45s · 1.5k out · run wf_00000001-aaa/a0000000000000002` |
   | A9L5 | `- agent — workflow-subagent · effort high · model claude-test-2 · commit:specs:tFix · prompt [${A9H##*/}]($A9H) · writes none · gates none · run wf_00000001-aaa/a0000000000000003` |

   Derived by reading `print_agent_lines` (`tools/roles/handoff.py:829-893`) over the fixture
   `A9_WRITE` already writes; `a0000000000000003` has no `result`, so it prints no `returned` line.
   The pass confirms each line by running the verb once; a line that differs is a defect against
   `TOOL-aOrientedCast-20`'s AC2, recorded in the ledger, and never re-pinned.
2. The build's one agent ledger holds five `- ` lines: arm 9's two and these three, each once, the
   prompt link re-rooted to `(../prompts/${A9H##*/})` as `_ll1` re-roots arm 9's.
3. A python edit of `$A9S` prefixes the `toolu_A` prompt with one `\n`. Then
   `handoff.py agents --handoff "$A9H" --session "$A9S"` exits 0 and prints exactly `$A9L1` and
   `$A9L2`.

Labels: `arm 9 agents --run prints the run's two agent lines and its one returned line`,
`arm 9 ...and the ledger gains exactly those three`, and
`arm 9 a prompt opening with a blank line still matches its handoff`.

### The write flag (S13)

At `3a57a986a`, `print_agent_lines` always calls `write_agent_ledger`
(`tools/roles/handoff.py:894-895`), so a mid-pass call dirties a tracked file. The `agents`
subparser (`:921-925`) gains `--write`; `print_agent_lines` gains `write=False` and writes only when it is true, else one note
names the held lines and `--write`. Arm 9's `--handoff` runs and step 1 of "Arm 9, extended" pass
`--write`, and one more step runs `--run` without it and asserts `git hash-object` of the ledger
and the listing of the build's `build/` folder unchanged.
The docs say to pass `--write` only at a bookkeeping step, when no pass is running.

### Arm 10 (S3)

One `build_fixture`, then the steps below in order, one `check_arm` each, so `n` rises by ten. The
checker runs as `(cd "$FX" && "$PY" -B "$KREL/check_roles.py" 2>&1)`. The registry is
`$FX/$MR/project/role-stand-in-waiver.txt`. The good row is the five TAB-separated fields
`2026-10-13`, `owner a`, `gov-researcher`, `tFix` and `this tool exposes no sub-agent primitive`.
The render is `handoff.py render --role gov-researcher --build tFix --unit TOOL-tFix-1 --input
"question=q" --stand-in` from the fixture root, after `mkdir -p "$FX/$MR/builds/tFix/prompts"`.

| Step | Staged | The answer asserted |
|---|---|---|
| 1 | nothing | the checker exits 0, its summary carrying `0 stand-in waiver(s), 0 stand-in declaration(s)` |
| 2 | no registry; the render | exit 1, stderr naming `role-stand-in-waiver.txt`, the prompts folder still empty |
| 3 | the good row written; the render again | exit 0, stdout a path ending `-researcher-stand-in.md` |
| 4 | nothing more | the checker exits 0 with exactly one `roles: note: stand-in waiver` line, summary `1 stand-in waiver(s), 1 stand-in declaration(s)` |
| 5 | the registry moved aside | exit 1, exactly one `R15` line, naming the declaration's path, `gov-researcher` and `tFix` |
| 6 | the registry back, the declaration moved aside | exit 1, exactly one `R15` line carrying `stale` |
| 7 | the declaration back, eight staged rows appended under the good row | exit 1, exactly eight `R15` lines, naming registry lines 2 to 9 once each |
| 8 | the registry back to the good row alone; `gov-orienter.agent.md`'s `mandatory:` set to `for every session` | exit 1, exactly one `R13` line, naming `gov-orienter.agent.md` |
| 9 | that line restored; `gov-spec-writer.agent.md`'s `output:` set to `specs` | exit 1, exactly one `R14` line, naming `{{MEMORY_ROOT}}/builds/<slug>/spec/` |
| 10 | that line restored; the conf rewritten with its `CHARTER` line alone | exit 2, the output naming `MEMORY_ROOT` |

The eight staged rows of step 7, after `TOOL-aOrientedCast-19`'s AC1, each otherwise the good row:
four fields; the date `2026-13-01`; the attribution `agent a`; the role `gov-ghost`; the role
`gov-session`, the catalogue's one `agent: false` role; the build `t-Fix`; an empty reason after a
fifth TAB; and a second copy of the good row. Step 8 stages R13 because the `orient` workflow's
`enforced-by` names `manifest-check.sh --card --append`, whose first word is no `.js` file.

The fixture copies the shipped role files, the shipped charter and the shipped renderer, so no step
substitutes a synthetic value for the one under test. Step 1 is the liveness half: a fixture that
is not clean reds there, before any staged break is read. The arm defines no shell function.

### Arm 11 (S2, S6)

Arm 11 resolves the hooks kit twice, as arm 6 does:
`roles_lib.resolve_kit_dir("hooks", "agent-cap.js", "$HERE")` and the same call with
`format-guard.js`. With neither found, or with no `node`, it prints `SKIP arm 11 — <what is
absent>` and adds no assertion. It stays out of `FLOOR_ASSERTIONS`, as arm 6 does, because a skip
must not red the floor.

**Part A, the marker.** A `build_fixture`, then the render arm 6 runs, `--role gov-researcher
--build bx --unit TOOL-bx-1 --input question=<text> --out <its prompts path> --part task`, whose
stdout is T and whose first line is the marker M. Five variants, each written by python with
`newline=""` so its bytes are exact:

| Variant | Bytes | Both readers |
|---|---|---|
| v1 | T | admit |
| v2 | `\n` then T | admit |
| v3 | T with every `\n` written `\r\n` | admit |
| v4 | T with one space after the marker's `-->` | refuse |
| v5 | two spaces, then T | refuse |

The spawn guard's answer is arm 6's payload with this variant as `prompt`, its own `session_id`,
`prompt_id` and `tool_use_id`, piped to `node <hooks kit>/agent-cap.js` under
`env -u CLAUDE_PROJECT_DIR`: admit when it exits 0 with empty stderr. The Python answer is admit
when `roles_lib.extract_prompt_marker(<variant>)` returns a match whose `group(0)` is M. One
`check_arm` per variant asserts the two answers are equal, and one asserts the five answers hold
both an admit and a refuse.

**Part B, the fence.** Three copies of `$REPO/$CH`, each written as `AGENTS.md` in its own folder
under `$TMP_ROOT`, the file name format-guard reads:

| Copy | Change | Both readers' `agent` definition |
|---|---|---|
| c1 | none | the charter's own |
| c2 | the line D2 below inserted directly above `<!-- /microformats -->` | the one D2 carries |
| c3 | the line `<!-- microformats -->` rewritten to `x <!-- microformats -->` | none |

```text
- `agent — <role> · run <run-id|direct>/<agent-id>`
```

Node prints, per copy, the `def` of `agent` and of `returned` from
`require(<hooks kit>/format-guard.js).readCharterShapes(<folder>).shapes`, or `none`; python prints
`extract_microformat_shapes(load_text(<copy>))`'s values for the same two heads, or `none`. One
`check_arm` per copy asserts the two outputs are equal, and one asserts the three node `agent`
answers hold two distinct definitions and one `none`.

### The fence reader (S5)

```python
def extract_microformat_shapes(text):
    """`{head: definition}` for every ``- `<definition>` `` line between the fence's two markers,
    each marker a whole line: the first line that is exactly `<!-- microformats -->` and the first
    that is exactly `<!-- /microformats -->`, CRLF folded. Keyed by the text before the
    definition's first ` — `; a head defined twice keeps its last definition. `{}` when either marker is absent or the closer comes first. This is how
    the hooks kit's format guard and the run-log kit's prose reader read the fence
    (TOOL-aOrientedCast-20, TOOL-aOrientedCast-25)."""
    lines = text.replace("\r\n", "\n").split("\n")
    if MICROFORMATS_OPEN not in lines or MICROFORMATS_CLOSE not in lines:
        return {}
    a, b = lines.index(MICROFORMATS_OPEN), lines.index(MICROFORMATS_CLOSE)
    shapes = {}
    for line in lines[a + 1:b]:
        m = MICROFORMAT_LINE_RE.match(line)
        if m:
            shapes[m.group(1).split(" — ", 1)[0]] = m.group(1)
    return shapes
```

A closer before the opener leaves `lines[a + 1:b]` empty, which is format-guard's `b < a` refusal
(`tools/hooks/format-guard.js:171-174`) and the run-log reader's empty slice
(`tools/runlog/prose.py:65`). The README sentence adds: each marker a whole line and the last
definition of a head winning, as the hooks kit's format guard reads the fence.

### The source refusal (S7)

In `tools/check-microformats.sh`:

- `n_open` and `n_close` count with `grep -cxF` (`:37-38`), and the block is cut with
  `awk -v o="$OPEN" -v c="$CLOSE" '$0 == o {f=1; next} $0 == c {f=0} f'` (`:46`), so a marker inside
  a longer line is no marker, the same as the readers. A part-line opener therefore counts zero and
  takes the existing exit 2, "not delimited by exactly one fence pair".
- The per-definition loop appends each `head`, right where it computes it, to a newline-joined
  list. After the loop, each head `sort | uniq -d` prints from that list takes
  `fail 9 "a definition head is defined more than once, so a reader keeping its first definition and one keeping its last read two different shapes: $h"`,
  read from a heredoc as the loop reads `$defs`, so no loop is fed by a command substitution.
- The header's "WHAT IT KEYS ON" paragraph says each marker is a whole line, and names check 9.

`tools/check-microformats.test.sh` gains two `arm` calls, and `FLOOR_ASSERTIONS` moves to 20:

```bash
arm "a head defined twice reds" red \
  "a definition head is defined more than once, so a reader keeping its first definition and one keeping its last read two different shapes" \
  '/^- `gates/a\
- `gates — RED · <leg>`'
arm "an opener that is not a whole line is cannot-run" cannot \
  "not delimited by exactly one fence pair" 's/^<!-- microformats -->$/x <!-- microformats -->/'
```

The first `want` is the branch's whole literal signature up to its interpolation, as the harness
meta-gate requires. `ARMS_FLOORS` in `.memory-tree.conf` changes `tools/check-microformats.sh:8:8`
to `tools/check-microformats.sh:9:9` and nothing else. At writing, this probe of the shipped
template printed nothing, then 1:

```bash
awk '$0 == "<!-- microformats -->" {f=1; next} $0 == "<!-- /microformats -->" {f=0} f && /^- `/' \
  coding-governance-agents.template.md | sed -E 's/^- `//; s/ — .*//' | sort | uniq -d
grep -c '^<!-- microformats -->$' coding-governance-agents.template.md      # 1
```

The pass re-stamps the kickoff manifest's `last-audit` line (S7), and its commit carries a
`manifest-audit: delta none · …` line naming the floor move.

### The criterion amendments (S9)

The record is this unit's own acceptance ledger under `memory/builds/aOrientedCast/build/`, its
Serves line `**Serves:** journal TOOL-aOrientedCast-25 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22`.
After its `**Evidences:** TOOL-aOrientedCast-25` block comes the heading
`## Criteria amended in closed specs`, which ends that block for hygiene check 23, then two
sub-heads. Neither carries an `AC<n>` bullet, so check 23 reads no second answer for either unit.

`### TOOL-aOrientedCast-21 AC2` states the criterion as written (spec 21, `:278-281`): with its last
field cut, the line blocks with "does not match its charter shape". It states what the code does,
citing `checkAgentLines` (`tools/hooks/format-guard.js:396-415`): a line still ending `/a1` with the
`run ` label cut, `· direct/a1`, gets the shape message; a line with the run field cut whole names
no agent and gets "no agent line for agent a1, which this turn dispatched". It names the suite's
staged break, `${A1/run direct/direct}` in `tools/hooks/format-guard.test.sh`, as the observation
of record, and the commit `6fb62ffa5` whose Decided trailer recorded the deviation. The probe that
stands, observed at writing as `[]`, then the shape message, then the no-agent message:

```bash
node -e "
const g = require('./tools/hooks/format-guard.js')
const { shapes } = g.readCharterShapes('.')
const req = [{ head: 'agent', agentId: 'a1', why: 'dispatched' }]
const A = '- agent — gov-builder · effort high · model m · TOOL-tBuild-1 · prompt [x.txt](x.txt) · writes product · gates none'
for (const t of [A + ' · run direct/a1', A + ' · direct/a1', A]) console.log(JSON.stringify(g.checkAgentLines(g.scanMessageLines(t), shapes, req)))
"
```

`### TOOL-aOrientedCast-22 AC6` states the criterion as written (spec 22, `:263-267`): a search for
the old marker with no pathspec prints nothing. It states why that never holds: the search spans
the spec and its ledger, which quote the pattern. The observation that stands, the first printing
nothing and the second listing the kit's carriers at writing:

```bash
git grep -l "gov:kit unattended@1.104" -- ':!memory/builds'
v=$(sed -n 's/^KIT_UNATTENDED_VERSION=//p' tools/unattended/unattended.sh)
git grep -l "gov:kit unattended@$v" -- ':!memory/builds'
```

The second search is the liveness twin: a pathspec that excluded everything would print nothing for
both. Both sub-heads cite review items L5 and L6. The commit stage's index render lists the record
in both closed specs' generated records regions.

### The gotcha (S10)

In `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`:

- the front matter's `description` ends: `…, a state that holds when the scope item is skipped, or
  an absence its own records break by quoting the pattern`;
- "Symptom" gains a fourth bullet, **Its own records answer it**: a "prints nothing" search with no
  pathspec spans the spec and the ledger that quote its pattern, so it never holds for a correct
  build, and read loosely it also misses a real carrier;
- "Where it bit" gains one paragraph naming `TOOL-aOrientedCast-21` AC2 (the command does not print
  that, and the deviation lived only in a commit trailer) and `TOOL-aOrientedCast-22` AC6 (its own
  spec answered the search), from review items L5 and L6, by unit id and never by path, so no
  anchor is added;
- "The fix" gains: a "prints nothing" search carries a pathspec that leaves out the records quoting
  its pattern, and a liveness twin, the same search for the current value, that must list the
  carriers; and a criterion found wrong at build time is amended where its spec allows, never only
  in a trailer.

Then `python tools/memory-tree/gotchas.py --write` re-renders `memory/gotchas/INDEX.md`.

### The dossier (S11)

The bullet at `memory/map/features/roles.md:123-126` becomes a list headed "What the kit reads from
outside itself, and which of it is a contract", one sub-bullet each:

| Read | From | Kind |
|---|---|---|
| the section 1 `- [<tag>] ` rule lines and the `## Protocols` and `## Facts` sections, inside the `gov:playbook` region | the governing doc, found by the conf's `CHARTER` key (TOOL-aOrientedCast-16) | contract |
| the `agent` and `returned` definitions of the `<!-- microformats -->` fence, each marker a whole line, the last definition winning | the governing doc (TOOL-aOrientedCast-20, TOOL-aOrientedCast-25) | contract |
| `MEMORY_ROOT` and `CHARTER` | the memory-tree conf | contract |
| leg names, for R12's `[gates]` | the tool root's gate manifest, when it reads | contract |
| `--card --path` and `--task-skeleton` output, and the card field grammar ported from it | the kickoff checker (TOOL-aOrientedCast-2, TOOL-aOrientedCast-15) | contract |
| rows naming a kit's source and installed path | the install receipt, through `resolve_kit_dir` | contract |
| the marker reading of a prompt, which `extract_prompt_marker` mirrors and arm 11 compares | the hooks kit's spawn guard (TOOL-aOrientedCast-25) | contract |
| the fields `handoff.py agents` reads | the session transcript, each subagent's `.meta.json`, a run's `journal.jsonl` (TOOL-aOrientedCast-20) | a reading, not a contract: a renamed field prints `unknown` |

The first row keeps the bullet's existing clause: a cited tag the charter drops reds the
`roles catalogue` leg, and a pre-tag charter is one reseed note.

### The roles bump (S12)

`KIT_ROLES_VERSION = "1.4"` (`tools/roles/roles_lib.py:25`) and `<!-- gov:kit roles@1.4 -->` in
`tools/roles/README.md:1` and `tools/roles/SKILL.template.md:5`; `tools/check-kit-versions.sh:387-393`
pairs the constant with the README's marker. The rendered `.claude/skills/build/SKILL.md:5` follows
by `bash tools/roles/adopt-roles.sh --scaffold`, the main loop's second pass. The bump lands after S1 to S8, so no later
edit of this unit moves the kit's bytes past 1.4. The pass re-renders the map with
`python tools/codebase-map/gen_map.py --write`, which adds the new function to its symbol index.

### Inventory

One function is minted: `extract_prompt_marker` in `tools/roles/roles_lib.py`, cell `py.function`;
`lexicon.py --suggest extract_prompt_marker --as py.function` answered OK at writing, the verb
`extract` read as "pull a declared shape out of a larger one", the reading `extractHandoffMarker`
takes in the hook. No shell function, constant or gate leg is minted. The new branch is
`fail 9` of `tools/check-microformats.sh`.

### Files touched (estimate)

`tools/roles/roles_lib.py`
`tools/roles/handoff.py`
`tools/roles/adopt-roles.test.sh`
`tools/roles/README.md`
`tools/roles/SKILL.template.md`
`.claude/skills/build/SKILL.md`
`help/roles.md`
`tools/check-microformats.sh`
`tools/check-microformats.test.sh`
`.memory-tree.conf`
`memory/guides/SESSION-KICKOFF.md`
`memory/map/features/roles.md`
`memory/map/generated/`
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
`memory/gotchas/INDEX.md`
`memory/builds/aOrientedCast/build/`

### Alternatives rejected

- A `--selftest` in `check_roles.py` for M5, the review's first suggestion: the adopter self-test
  already scaffolds the fixture the rules need, with the shipped renderer beside the checker, and a
  second fixture builder in a shipped script would be a second answer to how a fixture is built.
- The agreement and parity arms in `agent-cap.test.sh` and `format-guard.test.sh`: both files are
  `TOOL-aOrientedCast-24`'s, and the brief requires the two write sets not to meet.
- Putting arm 11's two parts in two arms: each would resolve the hooks kit and build its own
  fixture, and the suite's 300-second ceiling is better spent once.
- The other three readers of §8 F1.

### Rollout

Adopters receive the roles kit at 1.4 and the gate's two rules at `govkit update`. The template
carries neither a repeated head nor a part-line marker, so no adopter's rendered charter reds on
update unless its block was edited by hand, which is what the rule exists to catch. Nothing
migrates. Rollback is a revert of the unit's commit and a re-render of the Skill and the map.

## 5. Production-readiness checklist

- security — No new write path. The arms run the shipped hooks on payloads they build themselves;
  the stand-in arm writes only inside its scratch fixture.
- perf / scale — `extract_prompt_marker` scans one prompt per `Agent` call of a session, linear in
  its lines. The suite gains two fixtures and about twenty process runs under its 300-second
  ceiling.
- error / empty / loading states — A prompt the guard would refuse matches nothing, so the verb's
  refusal names the handoff as before; a charter with no whole-line fence yields no shape, and
  `agents` refuses naming the missing shape.
- observability — The gate's new refusal names the repeated head; arm 11's SKIP names what is
  absent.
- risks — The suite's wall clock rises; a breach of its ceiling at the close is a finding for the
  close to dispose. A charter that carried a part-line marker would now read as having no fence in
  the roles kit, as it already did in format-guard.
- testing — The arms of §7, observed RED-first by the main loop at the close; the direct probes and
  fixtures of §6 in the pass.
- migration — None: no stored data changes shape.
- user docs — None beyond the README sentences; no `help/` page describes the marker matching or
  the fence reading.

## 6. Acceptance criteria

No criterion runs a gate leg or a suite. Each runs the unit's own code on a scratch fixture, a probe
of code it reads, or a search of a file. Fixture F is the repository `build_fixture` scaffolds, made
in the run's scratch path. S is arm 9's session tree and H its handoff, both written by `A9_WRITE`,
cut out of the suite and run with python against F. The suite arms are under `New arm:` in §7.

- **AC1** — When S's `Agent` call `toolu_A` has its prompt prefixed with one `\n`,
  `python tools/roles/handoff.py agents --handoff <H> --session <S>` run from F's root exits 0 and
  prints exactly arm 9's two lines; and `grep -n "extract_prompt_marker" tools/roles/handoff.py tools/roles/README.md`
  shows the matcher's call and the README's sentence.
  Red when: the matcher compares the prompt's raw first line, as `tools/roles/handoff.py:815` does
  at base, and the verb exits 1 naming no `Agent` call.
- **AC2** — When the five variants of §4 "Arm 11", part A, are each read by
  `roles_lib.extract_prompt_marker` and, as an `Agent` payload, by the hooks kit's `agent-cap.js`
  in F, both readers admit v1, v2 and v3, and both refuse v4 and v5.
  Red when: one reader trims a leading blank line, a carriage return or a trailing space the other
  keeps, so the two answer one variant differently.
  fixture: F with `node` on PATH, the render arm 6 makes.
- **AC3** — When steps 1 to 7 of §4 "Arm 10" run in F, the render with `--stand-in` and no registry
  exits 1 naming `role-stand-in-waiver.txt` and adds no file; with the good row it exits 0 printing
  a path ending `-researcher-stand-in.md`; and `python tools/roles/check_roles.py` then answers
  exit 0 with one `roles: note: stand-in waiver` line, exit 1 with one `R15` line naming the
  declaration, exit 1 with one `R15` line carrying `stale`, and exit 1 with eight `R15` lines
  naming registry lines 2 to 9, in that order.
  Red when: a declaration with no row, a row with no declaration or any staged row passes, or a
  stand-in renders with no row.
  fixture: the checker's exit codes assume F is otherwise clean, which step 1 asserts first.
- **AC4** — When steps 8 to 10 of §4 "Arm 10" run in F, `python tools/roles/check_roles.py`
  exits 1 with one `R13` line naming `gov-orienter.agent.md`, then exits 1 with one `R14` line
  naming `{{MEMORY_ROOT}}/builds/<slug>/spec/`, then exits 2 naming `MEMORY_ROOT` for a
  `.memory-tree.conf` holding its `CHARTER` line alone.
  Red when: a mandatory role under a hookless workflow, a writer whose output lacks its folder, or
  a conf with no memory root passes.
- **AC5** — When, in F after arm 9's two `--handoff` runs,
  `python tools/roles/handoff.py agents --run wf_00000001-aaa --session <S> --write` runs, it exits 0 and
  prints exactly A9L3, A9L4 and A9L5 of §4 in that order, and the build's agent ledger then holds
  five `- ` lines, those three once each with the link re-rooted to `../prompts/`; and
  `grep -c "^FLOOR_ASSERTIONS=33$" tools/roles/adopt-roles.test.sh` prints 1.
  Red when: the journal branch drops an agent, reports `a0000000000000003` as returned, reads its
  unit as anything but its label, or adds a line to the ledger twice.
  figure: 33 is PINNED: 19 at base, plus arm 9's four new assertions and arm 10's ten. Arm 11
  SKIPs without `node` and stays out of the floor, as arm 6 does.
- **AC6** — When `extract_microformat_shapes` and format-guard's exported `readCharterShapes` read
  the three copies of §4 "Arm 11", part B, in the run's scratch path, they return the same `agent`
  and `returned` definitions for each: the charter's own for c1, the inserted one for c2, none for
  c3; and `grep -n "whole line" tools/roles/roles_lib.py tools/roles/README.md` shows the reading
  in both.
  Red when: the roles reader keeps the first definition of a head, as `tools/roles/roles_lib.py:234`
  does at base, or finds the opener inside a longer line, as `tools/roles/roles_lib.py:226` does.
- **AC7** — When `bash tools/check-microformats.sh <copy>` grades scratch copies of its test's
  fixture, it exits 1 naming `defined more than once` for a copy holding a second `gates`
  definition, exits 2 naming `not delimited by exactly one fence pair` for a copy whose opener reads
  `x <!-- microformats -->`, and exits 0 for the fixture as written; the §4 `uniq -d` probe over
  `coding-governance-agents.template.md` prints nothing; `grep -c "^FLOOR_ASSERTIONS=20$" tools/check-microformats.test.sh`
  prints 1; and `grep -c "tools/check-microformats.sh:9:9" .memory-tree.conf` prints 1.
  Red when: a charter carrying two definitions of one head, or a marker inside a longer line,
  passes the gate.
  figure: PINNED at `debc4bad6`, where the suite's floor is 18 and the gate's meta-gate floor 8:8.
- **AC8** — When `git grep -c "^### TOOL-aOrientedCast-21 AC2$\|^### TOOL-aOrientedCast-22 AC6$" -- memory/builds/aOrientedCast/build`
  runs, it prints one record with the count 2, whose Serves line names `TOOL-aOrientedCast-21` and
  `TOOL-aOrientedCast-22`; the §4 `checkAgentLines` probe prints the charter-shape message for the
  run field cut to `direct/a1` and `no agent line for agent a1` for the run field cut whole, as the
  first sub-head states; and the §4 `git grep` pair prints nothing for the old marker and the kit's
  carriers for the version `tools/unattended/unattended.sh` declares, as the second states.
  Red when: an amendment states a reading the code does not give, or the corrected search still
  spans the records that quote its pattern.
- **AC9** — When `grep -c "its own records break by quoting the pattern" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md memory/gotchas/INDEX.md`
  runs, it prints 1 for each file, and `grep -c "TOOL-aOrientedCast-2[12]" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  prints at least 1.
  Red when: the record gains the form and the generated index keeps the old description, or the
  form names no instance.
- **AC10** — When `grep -c "the only contract" memory/map/features/roles.md` runs it prints 0, and
  `grep -n "microformats\|journal.jsonl\|meta.json\|gate manifest\|task-skeleton\|install receipt\|extract_prompt_marker\|not a contract" memory/map/features/roles.md`
  prints a line for each term, every one inside the Shared seams section.
  Red when: the dossier still calls the two charter readings the only outside contract, or leaves
  out a read §4 "The dossier" lists.
- **AC11** — When `grep -c '^KIT_ROLES_VERSION = "1.4"' tools/roles/roles_lib.py` runs it prints 1;
  `grep -c "gov:kit roles@1.4" tools/roles/README.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md`
  prints 1 for each file; and `git grep -l "gov:kit roles@1.3" -- ':!memory/builds'` prints
  nothing.
  Red when: a carrier keeps 1.3, or the rendered Skill was not re-rendered after its template.
  permission: the rendered Skill reads 1.4 only after the main loop's second pass runs
  `bash tools/roles/adopt-roles.sh --scaffold`.
  figure: PINNED at `debc4bad6`, where the kit reads 1.3.
- **AC12** — When AC1's command runs in F, it leaves `git hash-object` of the ledger unchanged and
  stderr names `--write`; with `--write` the ledger gains its lines; and
  `grep -c -- "--write" tools/roles/README.md help/roles.md tools/roles/SKILL.template.md` prints at
  least 1 for each file.
  Red when: a call without `--write` changes the ledger, or a doc still says every run writes it.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `micro-format definitions` · `micro-format gate selftest` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a location probe asked from a moved directory)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit acceptance matrix` · `install-prefix (shipped surface)` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `check-wiring self-test` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `kickoff-manifest ratchet` · `gotchas selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC5 · arm 9's three new assertions, against `print_agent_lines` staged to read every journal agent as not returned, and against the `--handoff` matcher staged back to the raw first line · `FLOOR_ASSERTIONS` raised by 3
New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC4 · arm 10, against the R15 join in `check_roles.py` staged to report no uncovered declaration · `FLOOR_ASSERTIONS` raised by 10
New arm: tools/roles/adopt-roles.test.sh · covers AC2 AC6 · arm 11, against `extract_microformat_shapes` staged back to keeping the first definition of a head · none, as it SKIPs without node or the hooks kit
New arm: tools/roles/adopt-roles.test.sh · covers AC12 · arm 9's no-write step, against `print_agent_lines` staged to write the ledger without `--write` · `FLOOR_ASSERTIONS` raised by 1
New arm: tools/check-microformats.test.sh · covers AC7 · the repeated-head and part-line opener arms, against the repeated-head check staged out of `check-microformats.sh` · `FLOOR_ASSERTIONS` 18 to 20, and the gate's `ARMS_FLOORS` entry 8:8 to 9:9

The main loop observes each arm RED on its staged break and GREEN once restored, at the close
(M8). No pass runs a leg above.

## 8. Open questions

- **F1 — How is the third reader of the micro-format fence brought into agreement: made to read as
  the two existing readers do, or reduced to a call of one of them?**
  Options: (a) `extract_microformat_shapes` reads whole-line markers and keeps the last definition
  of a head, as `readCharterShapes` and the run-log kit's `read_charter_shapes` do, and arm 11
  compares it with `readCharterShapes`; (b) `roles_lib` resolves the run-log kit at run time and
  calls its reader; (c) all three readers refuse a repeated head, the review's alternative.
  (b) makes the roles kit, a default install, depend at run time on a sibling kit a target may not
  hold, and that reader returns nothing for a charter lacking a `BUILD` or `SPEC` shape, which
  `handoff.py agents` does not need: M3 veto 2. (c) edits `format-guard.js`, a
  `TOOL-aOrientedCast-24` file, and the run-log kit, against the brief's disjoint write sets, and
  leaves the part-line marker split open. (a) closes both splits the review measured inside this
  unit's files, and §4 "The source refusal" adds the refusal at the one place it binds every reader.
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The fence reader" states it.
- **F2 — Does the fence's gate refuse a repeated head too, as the review's left-shift line
  suggests?**
  Options: (a) `check-microformats.sh` refuses a head two definitions share as `fail 9`, and counts
  only whole-line markers, each observed by an arm of its test; (b) the readers agree and the gate
  stays as it is.
  (a) is the more feature-rich: no governed charter can then carry the two definitions on which a
  first-wins and a last-wins reader would differ, and the gate finds the fence as every reader
  does. No veto applies: no new dependency, surface or carrier, and the shipped template holds
  neither shape, so no leg reds on landing.
  RESOLVED (agent, 2026-10-13, delegated): (a).
- **FACT-QUESTION · F3 — Does the status header carry `closes M4 M5 M6 L4 L5 L6 L7`, as the spec
  brief asks?**
  Probe: `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import gen_build_index as g; print(g._expand_ids('M4 L5 TOOL-aOrientedCast-24', 'TOOL|KICK|PLAY'))"`.
  Observation at writing: it printed `(['TOOL-aOrientedCast-24'], ['M4', 'L5'])`, so
  `read_header_verbs` (`tools/memory-tree/backlog.py:741-744`) refuses such a header as "not an id
  or an id range", and every render of the build index refuses with it. Liveness: the real id in
  the same call expands, so the probe answers either way. The build keeps no `BACKLOG.md`, so the
  verb would join nothing.
  RESOLVED (agent, 2026-10-13, delegated): the verb is left out and §1 names the seven items, as
  `TOOL-aOrientedCast-15`'s F2 resolved the same question.
- **F4 — Where do the corrections of spec 21's AC2 and spec 22's AC6 live, when both specs are
  CLOSED?**
  Options: (a) a rev-2 of each spec, the review's fix; (b) a section appended to each unit's own
  acceptance ledger; (c) a section of this unit's acceptance ledger, whose Serves line names both
  units.
  (a) rewrites a landed record, which `memory/TEMPLATE-SPEC.md` freezes and the brief rules out.
  (b) writes `TOOL-aOrientedCast-22`'s ledger, which `TOOL-aOrientedCast-24` may also write for
  review item L2, spec 22's AC7, against the brief's disjoint write sets. (c) stays inside this
  unit's own record, and the index the commit stage renders lists it in each spec's records region,
  one hop from the criterion it corrects.
  RESOLVED (agent, 2026-10-13, delegated): (c), as §4 "The criterion amendments" states it.
- **F5 — Does this unit raise the meta-gate's floor for `check-microformats.sh` after adding its
  ninth branch?**
  Options: (a) `ARMS_FLOORS` moves the gate from 8:8 to 9:9, and because `.memory-tree.conf` is in
  the kickoff manifest's `watch:` list, the manifest takes a `last-audit` re-stamp; (b) the floor
  stays at 8:8.
  (b) leaves one branch of slack, so the new arm could be dropped under a pin and the armed floor,
  which exists for that case (`memory/HYGIENE.md`, "The harness meta-gate"), would not see it; the
  raise would stand as a follow-up. (a) costs one token and one stamp. No veto applies.
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The source refusal" states it.

- **F6 — Which spelling keeps a mid-pass `agents` call from writing?**
  (a) Print by default, the write behind `--write`; (b) write by default, a `--no-ledger` flag to
  skip it. Under (b) a call that forgets the flag dirties the tree again, the defect itself. (a)
  makes the safe call the default and is the house spelling (`render_agents.py --write`,
  `gen_map.py --write`, `gotchas.py --write`).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The write flag" states it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · S13 · S8 · AC5 · AC12 · §4 · §7 · §8 · the `agents` ledger write moves
  behind `--write` after a mid-pass call dirtied the tree: S13, §4, F6, AC12, a New arm line, the
  docs in files touched, and the floor at 33.
- rev-3 · 2026-10-13 · §1 · §3 · §4 · §6 · §10 · trimmed under the spec size ceiling: history
  and restated evidence cut; no scope item and no criterion's meaning moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "normalise a handoff prompt's marker line the way the
spawn guard admits it"` ranked name-token neighbours (`check_line`, `render_line`,
`derive_marker_basis`) and the four hook inventory keys, none of which reads a prompt's marker. `"read
the micro-format fence of the governing doc into shapes"` ranked `read_charter_shapes` in the
run-log kit, one of the two readers this unit's reader must match. `"fixture arm that builds a
scratch repo and runs the roles catalogue checker"` ranked `build_fixture`, a seam at fan-in 5, with
`tools/roles/adopt-roles.test.sh` among its homes. The seams this unit extends, found by those
probes and by reading: `MARKER_RE` and `extract_microformat_shapes` in `tools/roles/roles_lib.py`;
`print_agent_lines` in `tools/roles/handoff.py`; `build_fixture`, `check_arm`, arm 6's hooks-kit
resolution and arm 9's `A9_WRITE` in `tools/roles/adopt-roles.test.sh`; the per-definition loop of
`tools/check-microformats.sh` and the `arm` helper of its test; the gotcha record
`criterion-asserts-what-its-own-command-cannot-show`; and the roles dossier. No new seam is built.
The recall probe surfaced `TOOL-aReplayedCard-2`'s three readers of one token held together by a
parity check, the shape arm 11 takes. `python tools/memory-tree/gotchas.py --for-paths` over the write set
selected `amendment-leaves-its-other-half-standing`, `staged-break-substitutes-a-synthetic-value`
and `fixture-passes-by-finding-nothing`, which §4's liveness steps and shipped fixtures answer.

Recall terms used: `handoff marker normalise agent-cap rule 6 parity arm micro-format fence reader readCharterShapes extract_microformat_shapes adopt-roles.test.sh`
