# TOOL-aDeferredBar-3 — the act refusal: a PreToolUse hook denies a flagged bar or a suite before VERIFYING

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base b2a330be · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md](../build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md) | research | TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 |
| [2026-09-13-prompt-TOOL-aDeferredBar-3-1-spec-brief.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-3-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Refuse the act where it is committed: `tools/unattended/gate-guard.js`, a `PreToolUse` hook on
matcher `Bash|PowerShell`, exits 2 on a command that would run the flagged merge bar or a self-test
suite while the unattended run on the current branch is in a phase before `VERIFYING`. It is the
only one of this build's three mechanisms that reaches an agent inside a `Workflow` sidechain, and
the corpus in §4 shows close to half of those runs come from there.

## 2. Scope (IN)

- **S1** — the hook, `gate-guard.js`, in the unattended kit: read stdin, blank strings and heredoc
  bodies, find a deny shape at command position, and only then resolve the repository root, the
  branch and the run-state record that keys the phase. Fails open on every unreadable input.
  Observed by AC1, AC2, AC3, AC4, AC5.
- **S2** — the key: the record under `<root>/<MEMORY_ROOT>/builds/*/RUN.md` whose `branch-ref:`
  equals the ref in the git dir's `HEAD`, read without spawning git. A record on another branch,
  a record without that field, a detached `HEAD`, a missing conf or no record at all keys nothing.
  Observed by AC3, AC4.
- **S3** — the allow set is the tail of the driver's `PHASES_CORE` from `VERIFYING`, spelled in the
  hook and pinned to the driver by a suite arm. Observed by AC3, AC6.
- **S4** — the fragment, `gate-guard.fragment.json`, and the wiring of `.claude/settings.json`
  through `tools/settings-merge.py --fragment`. Observed by AC7, AC8.
- **S5** — the withheld suite, `gate-guard.test.sh`, its `project-owned` row in the kit descriptor
  and its budget row, so `run-unattended-gates.sh` enumerates it and the bar does not. Observed by
  AC6, AC9.
- **S6** — the adopter's `--check` arm reports the hook UNWIRED, naming the merge command as the
  remedy. Observed by AC10.
- **S7** — the corpus measurement of the shipped predicate, hits and near-misses, recorded in the
  unit's build record. Observed by AC11.
- **S8** — the prose: the kit README, the skill template and its render, the map dossier, one trap
  line in the kickoff manifest, and the kit version one step past where this unit found it.
  Observed by AC8, AC12, AC13.

## 3. Non-goals (OUT)

- **No denial of the plain bar.** `run-gates.sh` with neither `GATE_FULL` nor `GATE_SELFTESTS` set
  is the scoped bar the owner allows at the main loop. The hook cannot tell a child from the main
  loop, so the plain bar inside a child is forbidden by the instruction unit 1 puts in the child
  prompt, not refused here.
- **No phase-vocabulary change**, no new conf key, no new gate leg. The hook reads what the kit
  already declares: `MEMORY_ROOT` from `.unattended.conf` and `phase:` from a run-state record.
- **No `tools/check-wiring.sh` arm.** The `hook destinations` leg and the adopter's `--check` arm
  cover the wiring; a check-wiring arm for this hook is a follow-up backlog row, filed at landing.
- **No change under `tools/hooks/`.** The predicate helpers the hook needs are copied inline, the
  way every copy-installed kit carries its contents, because a `require` of a sibling kit's file is
  a literal the install-prefix ban refuses and an adopter may not hold that kit.
- **No coverage of a path assembled at run time or a script fed through a heredoc.** The
  predicate is textual; `s=tools/unattended; bash $s/unattended.test.sh` walks past it, as does a
  python heredoc that spawns the suite. The same ceiling `scratch-guard.js` states of itself, and
  no call in the corpus has either shape; the upgrade path is a tokenizer, not more regexes.
- **No PowerShell-native spelling.** `$env:GATE_FULL=` occurs zero times in the corpus. The hook
  reads PowerShell calls too, but the shapes it knows are the shell ones.
- **This spec is written to pass the gate `TOOL-aDeferredBar-2` adds.** Every fixture command the
  hook must deny is a §4 table row, and §6 cites rows rather than spelling an invocation as an
  observation. That is a constraint on this document and not an edge of the unit, so it is not
  declared below.

### Edges

- **consumes-from** `TOOL-aDeferredBar-1` — the child-prompt instruction against the PLAIN bar
  inside a pass, which this hook admits by design; without it the scoped-bar case inside a child is
  neither refused nor forbidden. Also the kit version as that unit leaves it: this unit steps one
  past, and the render verb that unit's AC6 names is admitted by the read-only verb rule in §4.
- **consumes-from** external — `TOOL-cRefutedPremise-1`'s measurement that a `Bash|PowerShell`
  `PreToolUse` hook fires inside a `Workflow` sidechain. Nothing here re-measures it; if it were
  false the hook would still bind the main loop and nothing else.
- **hands-off** external — a `check-wiring.sh` arm for this hook, and a real tokenizer if the
  textual ceiling above ever stops being enough.

## 4. Design

### The order of work inside the hook

The predicate runs first and the filesystem is read only on a hit. The overwhelming majority of
tool calls carry no deny shape, and for them the hook costs one regex pass over one string and no
file read at all. A hit then costs a walk up from `cwd` to `.git`, one `HEAD` read, one conf read
and one `RUN.md` read per build folder, which is 51 files in this tree today.

```
stdin JSON -> tool_name in {Bash, PowerShell} -> tool_input.command
  -> buildCommandView(command)              strings and heredoc bodies blanked, offsets kept
  -> scanDenyHits(command, view)            rows D1-D4 on the view; row D5 re-enters once on the
                                            quoted body of a `bash -c`; no hit: exit 0, nothing read
  -> resolveRepoRoot(cwd)                   {root, headRef}; no .git or detached HEAD: exit 0
  -> readMemoryRoot(root)                   .unattended.conf absent: exit 0; key absent: "memory"
  -> resolveRunPhase(root, memoryRoot, ref) records whose branch-ref equals ref; none: exit 0
  -> every matched record's phase in PHASES_ALLOW: exit 0
  -> renderDeny(...) to stderr, exit 2
```

`cwd` is the hook payload's own field, the one `tools/hooks/agent-cap.js` already reads for its
budget directory, with `process.cwd()` as the fallback. The walk up to `.git` and the worktree
case, where `.git` is a FILE holding `gitdir: <path>`, follow that hook's `gitCommonDir` except
for one difference that matters: this hook wants the per-worktree `HEAD` under the `gitdir`
target, never the common dir's, because the common dir's `HEAD` is the primary tree's branch.

### The predicate

Command position is the line start or the text after `;`, `&&`, `||`, `|`, `(`, `then`, `do` or
`else`, followed by any of `env`, `export`, any number of `NAME=value` words, `timeout N`, and
`bash` or `sh` with one short option. In the blanked view, at that position:

| row | shape | what is matched | why |
|---|---|---|---|
| D1 | flag prefix | `GATE_FULL=` or `GATE_SELFTESTS=` followed by a non-empty value, bare or after `export` | `run-gates.sh:158` tests `-n`, so the empty assignment is the OFF spelling and is not a hit |
| D2 | runner | a word ending `run-selftests.sh` | every declared self-test |
| D3 | runner | a word ending `run-unattended-gates.sh` | this kit's own suites |
| D4 | suite | a word ending `.test.sh` | any one suite, other kits' included |
| D5 | nested | the quoted argument of `bash -c` or `sh -c`, read from the ORIGINAL text at the offset the blanked view locates, and scanned as a command of its own, one level deep | the blanked view alone would hide it, and the corpus holds eight such calls, every one a run: `bash -c 'timeout 5400 bash tools/unattended/unattended.test.sh'` among them |

A row D2, D3 or D4 token is NOT a hit when the same simple command, up to the next `;`, `&&`,
`||`, `|` or newline, carries one of `--list`, `--check`, `--rank`, `--help` or `--render`.
Measured on node `a`, 2026-09-13, each direct: `run-selftests.sh --list` 5 s, `--check` 17 s,
`--rank` 3 s, `--help` 3 s; `run-unattended-gates.sh --help` 1 s;
`kit-dogfood-parity.test.sh --render` 1 s and `--check` 2 s; `check-protocol-parity.test.sh
--render` 0 s. The render verb matters most: 934 raw corpus mentions of `--render` on
`kit-dogfood-parity.test.sh` alone, which is how the memory-tree kit's live guides are rewritten
from their templates, and unit 1's AC6 names it. The verb list is textual and generic, so a suite
that ignores an unparsed `--check` would run whole behind it; no call in the corpus has that
shape, and the `ponytail:` comment on the list names it as the ceiling.

Measured over the operator's transcript store on node `a`, 2026-09-13, by a probe in this session's
scratchpad that reads the store and builds nothing. The corpus is 3049 `.jsonl` files, 101 706
`Bash` or `PowerShell` `tool_use` records, 76 859 of them with `isSidechain` set. These figures are
PINNED to that date; AC11 re-derives them at build time from the shipped predicate.

| shape | hits at command position, blanked view | of which sidechain | near-misses: token present in raw text, absent at command position in the blanked view |
|---|---|---|---|
| D1 `GATE_FULL=` | 301 | 131 | 149 |
| D1 `GATE_SELFTESTS=` | 51 | 1 | 79 |
| D2 | 148 | 82 | 724 |
| D3 | 32 | 7 | 656 |
| D4 | 1740 | 778 | 6765 |
| plain bar, allowed | 326 | 75 | — |

The near-miss column is what the blanked view earns: 8373 commands carry a deny token inside a
heredoc'd python edit, a `git commit -F -` message, a `grep` or `sed -n` argument, and a predicate
over raw text would deny every one of them. The research record's first cut counted 1365 D4
invocations against this probe's 1740; the difference is this probe's wider command-position
grammar, which admits `then`, `do` and `else`, and the order of the rows is the finding either
way.

### The key

`branch-ref:` and `phase:` are the two fields read from a record, both already written by
`unattended.sh --preflight` and read by `lib-unattended.sh:405`. Three records in this tree prove
why the branch is the key and not the existence of a record: `aUnblockedFleet` and `aClosedDocket`
sit at `BUILDING` on branches nobody has checked out for days, and three older `LANDING` records
carry no `branch-ref:` field at all. Keyed on "any record is live", the hook would deny every
session in this repository forever; keyed on the branch, those five records key nothing.

When more than one record names the current branch, the hook reads them all and denies if any of
them is in a phase outside the allow set, naming that one. One live run per branch is the kit's
own invariant and this rule costs nothing when it holds.

### The allow set

`PHASES_ALLOW = ['VERIFYING', 'LANDING', 'LANDED', 'ABORTED']`, with the comment saying it is the
tail of `PHASES_CORE` in `unattended.sh:337` from `VERIFYING` onward. Those four are where the owed
`GATE_SELFTESTS=1` bar for kit work, the close's own bar and the lander run, all by the main loop.
Every other phase denies, a project's `PHASES_EXTRA` members included, because an extra phase is by
construction before landing. The restatement is pinned by a suite arm that reads the driver's line
and compares (AC6), which is the liveness the kit's own checker cannot supply — see §8.

### The deny message

```
BLOCKED by gate-guard: this command runs a self-test suite while the unattended run on this
branch is at BUILDING (memory/builds/<slug>/RUN.md), which is before VERIFYING.

  suite: tools/unattended/check-unattended.test.sh

Inside a build pass a unit is observed by the direct check its spec names, in seconds. The
flagged bar and the self-test suites run once, at VERIFYING, by the main loop. A quoted mention
of the file is not a hit.
```

The record path in the message is derived from the walk, never spelled; the first line names
the shape in words (`the flagged merge bar`, `a self-test suite`, `the self-test runner`) and the
indented line names the matched token. Two shapes in one command are two indented lines.

### Inventory

Cell `js.function camel` from `.lexicon.conf`, verbs from its table: `readStdin`,
`buildCommandView` (copied from `scratch-guard.js`, see §3), `scanDenyHits`, `resolveRepoRoot`,
`readHeadRef`, `readMemoryRoot`, `resolveRunPhase`, `checkCommand`, `renderDeny`, `main`.
Constants `PHASES_ALLOW`, `READ_ONLY_VERBS`, `TOOLS`. The header carries a `gov:kit unattended@`
marker the way `procmon-hook.js` carries its kit's; `check-kit-versions.sh:169` pairs four named
`.sh` carriers and every `*.template.md`, so this marker is a courtesy the gate does not read, and
the spec says so rather than letting a reader assume it is graded.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/gate-guard.js` | new, the hook; no `tools/` literal, the conf key and the record basename are the only spellings |
| `tools/unattended/gate-guard.fragment.json` | new: `{name, event: "PreToolUse", matcher: "Bash|PowerShell", marker: "gate-guard.js", hook_path: "{kit}/unattended/gate-guard.js"}`, the shape of `procmon-hook.fragment.json`; `{kit}` resolves against the fragment's own location, two directories up, as `check-hook-destinations.sh` and `settings-merge.py` both read it |
| `.claude/settings.json` | one entry appended into the existing `Bash|PowerShell` `PreToolUse` group beside `scratch-guard.js`, by `python tools/settings-merge.py --fragment tools/unattended/gate-guard.fragment.json` and never by hand; LIVE the moment it lands, hooks being re-read mid-session |
| `tools/unattended/gate-guard.test.sh` | new, the withheld suite; every fixture is a scratch repo under `mktemp -d` holding a `.git` `HEAD`, a conf and a record, never the real tree; prints `PASS (<n> assertions)` against a derived `FLOOR_ASSERTIONS` as `scratch-guard.test.sh:239` does |
| `tools/unattended/kit.toml` | `gate-guard.test.sh` joins the `project-owned` include list; the `**` engine rule already ships the hook and the fragment |
| `tools/run-gates/selftest-budgets.txt` | one row, budget from the measured reading times 1.5 floored at 60 s, so `run-unattended-gates.sh` enumerates it through `run-selftests.sh --kit tools/unattended --list` |
| `tools/install-prefix-carried.txt` | the `selftest-budgets.txt` row RAISED 14 to 15 by hand with its reason, because every budget row is a gov suite path by construction and the ban admits a hand-justified raise in the pass that wants it |
| `tools/unattended/adopt-unattended.sh` | a sixth artifact in the `--check` branch: the settings file lacks the fragment's marker, print the UNWIRED refusal naming `$PY $ROOT/tools/settings-merge.py --fragment $KIT_REL/gate-guard.fragment.json` and exit 1, in the branch's own sequential-refusal style. The brief named `adopt-process-monitor.sh`'s `add_problem` register; this adopter has no register and adding one for a single arm is a second style in one file |
| `tools/unattended/README.md` | the paragraph: the act is refused, not only forbidden, and which shapes |
| `tools/unattended/SKILL.template.md` | the half-sentence beside the instruction unit 1 adds |
| `.claude/skills/unattended/SKILL.md` | re-rendered by `bash tools/unattended/adopt-unattended.sh`, never edited |
| the version step | `KIT_UNATTENDED_VERSION` in `unattended.sh`, `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh` with their same-line markers, every `tools/unattended/*.template.md` marker, `README.md`, `playbook.fixture.md`, and the four installed copies the adopter re-copies or re-renders under `memory/guides/` and `.claude/skills/` — one step past the value read from `unattended.sh` at dispatch, DERIVED there and not pinned here |
| `memory/map/features/unattended.md` | prose refresh on touch; no inventory key is claimed, because `git-hooks` enumerates `.githooks/` and no class enumerates a `PreToolUse` hook |
| `memory/guides/SESSION-KICKOFF.md` | one trap line beside the `scratch-guard` line at `SESSION-KICKOFF.md:221`, with `last-audit` re-stamped and the delta line in the commit message |

### Alternatives rejected

- **The hooks kit as the home.** The key is this kit's record and conf key; a hook under
  `tools/hooks/` would name both by literal, which the install-prefix ban grades.
- **Deny whenever any record is live.** Refuted by the two stale `BUILDING` records above.
- **Deny the plain bar.** The main loop owes it; a hook that denied it would be disabled in a day.
- **Read `PHASES_CORE` from the driver at run time instead of spelling four names.** The hook fails
  open, so a driver it could not read would switch the hook off silently. Four literals pinned by
  a suite arm fail loudly on demand instead.
- **Refuse in the runner** (the research record's C3). Partial by construction and cross-kit.

## 5. Production-readiness checklist

- security — the hook reads and prints; it writes nothing and spawns nothing. It is a hygiene
  rule and fails open, which a containment boundary could not.
- perf / scale — no hit means no file read; a hit reads one `HEAD`, one conf and one record per
  build folder. Both paths are milliseconds against the 320 ms tool-call floor.
- error / empty / loading states — three outcomes and no fourth: silent exit 0 on allow and on
  every unreadable input, the §4 message and exit 2 on a deny. A broken hook never blocks a call.
- observability — the deny names the shape, the token, the phase, the record path and the
  substitute, so a reader acts without a second command.
- risks — a false deny on a read-only verb the list does not know; the remedy is one word added
  to `READ_ONLY_VERBS` with its measured cost. A false allow through a path assembled at run
  time; §3 names it and the corpus says it is not a live shape.
- testing — the suite drives the hook directly with a fixture stdin per arm; the corpus probe
  reports hits and near-misses of the shipped predicate.
- migration — none; the settings edit is idempotent by `settings-merge.py`'s own structure and
  the fragment on an existing matcher appends into the existing group.
- user docs — the kit README and the skill template, S8.

## 6. Acceptance criteria

Every observation below is the hook fed a fixture on stdin, or a direct checker, in seconds. No
criterion names the bar, a flag prefix or a suite as its observation, because once this hook is
wired the pass that builds it could not observe such a criterion.

- **AC1** — When `gate-guard.js` is fed a fixture whose record is at `BUILDING` on the fixture's
  own branch and whose command is row D1 with the `GATE_SELFTESTS` prefix, it exits 2 and stderr
  carries `BLOCKED by gate-guard`. Observed RED before the hook is wired, and it is the failing
  case the build rules require.
  Red when: the fixture's `HEAD` names the record's branch and the hook still exits 0.
- **AC2** — When the same fixture is fed each of rows D1 with `GATE_FULL`, D1 after `export`, D1
  behind `env`, a `NAME=value` word and `timeout 30`, D2, D3, D4, and D5 wrapping a D4 token in
  `bash -c` quotes, each exits 2 and each stderr names its matched token. Observed by
  `gate-guard.test.sh`, one arm per row.
  Red when: an arm's stderr names a token the fixture command does not contain, or the D5 arm
  allows because the nested body was blanked and never read.
- **AC3** — When the fixture's record is moved through `VERIFYING`, `LANDING`, `LANDED` and
  `ABORTED`, every row D1 to D4 exits 0 with empty stderr; and when the record is at `BUILDING`,
  the plain bar with `GATE_JOBS=1`, each read-only verb form of D2, D3 and D4, and the empty
  assignment `GATE_FULL=` exit 0. Observed by `gate-guard.test.sh`.
  Red when: `VERIFYING` is denied, which is the owed bar for kit work being refused.
- **AC4** — When the fixture record's `branch-ref:` names another branch, or carries no such
  field, or `HEAD` holds a bare sha, or no record exists, or `.unattended.conf` is absent, row D4 at
  `BUILDING` exits 0. Observed by `gate-guard.test.sh`, one arm each, plus one arm where `.git` is a
  worktree FILE whose `gitdir:` target holds the `HEAD` that keys a deny.
  Red when: the worktree arm allows, meaning the hook read the common dir's `HEAD` instead of the
  worktree's.
- **AC5** — When stdin is empty, not JSON, names another tool, or carries no command, the hook
  exits 0; and when `git commit -m` quotes row D4's token, or a heredoc body spells row D1, it
  exits 0. Observed by `gate-guard.test.sh`.
  Red when: the quoted mention is denied, which is the raw-text predicate the blanked view exists
  to replace.
- **AC6** — When `gate-guard.test.sh` reads `PHASES_CORE=` from `unattended.sh` and takes its tail
  from `VERIFYING`, the list equals the hook's exported `PHASES_ALLOW`; and when the suite finishes,
  it prints `PASS (<n> assertions)` with `n` at or above `FLOOR_ASSERTIONS`.
  Red when: the driver's tail and the hook's list differ by one member, which is a restatement
  that drifted.
- **AC7** — When `python tools/settings-merge.py --fragment` is run with `gate-guard.fragment.json`
  twice, the second run changes no byte, and `bash tools/check-hook-destinations.sh` prints an
  `ok` row for the fragment resolving to the hook's path.
  Red when: the fragment resolves to a path no descriptor rule ships, which is a wiring hole.
- **AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the kit version
  step, it exits 0; and when `bash tools/check-kit-versions.sh` runs, it exits 0 with every
  unattended carrier at the stepped value.
  Red when: one carrier holds the old value, the five-carrier class the `stamps` gotcha names.
- **AC9** — When `bash tools/run-gates/run-selftests.sh --kit tools/unattended --list` runs, it
  lists the new suite with its budget; and when `python tools/govkit/govkit.py selfcheck` runs, no
  line names `gate-guard.test.sh` as claimed by no rule.
  Red when: the budget row is absent, which is a suite exempt from the cost rule by arriving.
- **AC10** — When the settings file in a scratch tree lacks the fragment's marker,
  `adopt-unattended.sh --check` exits 1 naming the hook UNWIRED and the `--fragment` remedy; with
  the marker present the arm is silent. Observed by `gate-guard.test.sh`.
  Red when: an unwired tree passes `--check`, which is the silent-unwiring class.
- **AC11** — When the shipped predicate is run over every `Bash` and `PowerShell` `tool_use`
  command in the transcript store, the build record carries the hit and near-miss count per row and
  the plain-bar count, and every near-miss example printed is a mention, not a run.
  fixture: the store under `~/.claude/projects/` on node `a`; 3049 files on 2026-09-13.
  cost: about 70 s on node `a`.
  figure: DERIVED at observation time; §4's table is the 2026-09-13 reading.
  Red when: a listed near-miss is a run, which means the command-position grammar admits a shape
  the blanked view then hides.
- **AC12** — When `python tools/codebase-map/test_codebase_map.py` runs, it exits 0 with the
  `unattended` dossier refreshed and no new key claimed; and when `python tools/lexicon/lexicon.py`
  runs, it reports no new offender in cell `js.function camel`.
  Red when: a hook function leads with a verb outside the declared table.
- **AC13** — When `bash skills/session-kickoff/manifest-check.sh` runs after the trap line lands
  with `last-audit` re-stamped, it exits 0.
  Red when: the manifest line lands without the re-stamp and the ratchet refuses it.

## 7. Gates

`hook destinations (every declared hook path ships)` · `unattended skill wiring` · `unattended kit gate` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)`

The brief also named `verdict epoch (kit version dates the engine)`; dropped after reading
`tools/memory-tree/check-verdict-epoch.sh`, which grades the memory-tree engine's constant and
mentions this kit nowhere.

New arm: `tools/unattended/gate-guard.test.sh` · a fixture record at BUILDING and the flagged bar · none

## 8. Open questions

- **F1 — the hooks kit or the unattended kit as the home.**
  RESOLVED (agent, 2026-09-13, delegated): the unattended kit. The key is this kit's run-state
  record and conf key; a file under `tools/hooks/` reading them names a sibling kit by literal,
  which `tools/hooks/README.md` bans and the install-prefix leg grades. Two kits already ship
  their own hooks this way. Vetoes clean.
- **F2 — key on the phase, or deny whenever a record exists.**
  RESOLVED (agent, 2026-09-13, delegated): the phase. The main loop owes a full bar at
  `VERIFYING`, and two stale `BUILDING` records on other branches would otherwise deny every
  session in this repository. Vetoes clean.
- **F3 — deny the plain bar too.**
  RESOLVED (agent, 2026-09-13, delegated): no. It is the scoped form the owner allows; the child
  prompt forbids it by instruction where the hook cannot tell a child from the main loop.
- **F4 — `*.test.sh` broadly, or this kit's six suites only.**
  RESOLVED (agent, 2026-09-13, delegated): broadly. The ledger's three most expensive suites
  belong to other kits, and D4 is 1740 of the 2272 corpus hits.
- **FACT-QUESTION · F5 — may a kit file spell the four allowed phase names, or does
  `check-unattended.sh` red a restated set?**
  RESOLVED (agent, 2026-09-13, delegated): it may, and the liveness the brief assumed does not
  exist, so this unit supplies it. Probe: every reader of `PHASES_CORE` in
  `check-unattended.sh` (lines 331, 383, 387, 680, 702, 2013, 2033) reads the driver's value
  through `core_of`; no arm opens a sibling `.js`, and `check-unattended.test.sh` stages no
  restatement in a sibling file, so the checker's silence over the hook would be a zero that
  proves nothing. The positive control is the same grep finding the declaration at
  `unattended.sh:337`. The rule the checker states at its line 37 is a rule about ITSELF. So the
  four names are spelled in the hook with the comment the brief asks for, and AC6's parity arm is
  the restatement's liveness, on demand.
- **F6 — which read-only verbs the file-token rows admit.**
  RESOLVED (agent, 2026-09-13, delegated): `--list`, `--check`, `--rank`, `--help`, `--render`,
  each measured under 20 s in §4, generic over rows D2 to D4 and never over D1. The alternative,
  naming `kit-dogfood-parity.test.sh` for its `--render`, is a sibling-kit literal.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seams this unit EXTENDS, each verified against source at `b2a330be`:
`tools/settings-merge.py --fragment` for the idempotent settings edit, which appends a fragment on
an existing matcher into the existing group (`settings-merge.py:233`);
`tools/check-hook-destinations.sh` arm 1, which resolves `{kit}` against the fragment's own
location and joins it to the descriptor's shipped set; the `project-owned` include rule in
`tools/unattended/kit.toml` and the declared row population in
`tools/run-gates/selftest-budgets.txt`, which is how a withheld suite is enumerated;
and the `branch-ref:` and `phase:` fields `lib-unattended.sh:405` already reads. The hook's shape
follows `tools/hooks/scratch-guard.js` (blanked view, fail-open, exit-2 protocol) and its
`buildCommandView` is copied inline for the reason §3 states. The probe
`python tools/codebase-map/reuse_lookup.py "deny a tool call whose command runs the full merge bar
or a self-test suite while an unattended run is before verifying"` returned the `run` seam and the
`.unattended.conf` affordance and printed `unscanned layers: .sh`, so the shell surface was read
by hand: `run-gates.sh:158` and `:1229` for the two flag reads, and the two runners' verb tables.
The recall probe's top hits were `TOOL-cRefutedPremise-1`, `TOOL-aTetheredScratch-1`'s AC5 corpus
arm, and `TOOL-dRetiredFork-34` on the hook-destinations arms; the first is the external edge in
§3 and the second is the shape AC11 copies.

Recall terms used: `PreToolUse Bash PowerShell hook sidechain Workflow scratch-guard string-blanked
corpus transcript predicate fragment settings-merge phase run-state`
