# TOOL-aDeferredBar-3 — the act refusal: a PreToolUse hook denies a flagged bar or a suite before VERIFYING

**Status:** SPECCED · rev-3 · 2026-09-14 · node a · Tier-2 · base b2a330be · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md](../build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md) | research | TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 |
| [2026-09-13-prompt-TOOL-aDeferredBar-3-1-spec-brief.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-3-1-spec-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md) | spec-audit | TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md) | spec-audit | TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 |

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
- **S2** — the key: the record under `<root>/<MEMORY_ROOT>/builds/*/RUN.md` whose `run-branch:`
  equals the ref in the per-worktree `HEAD`, read without spawning git, falling back to
  `branch-ref:` for a record written before `run-branch:` existed. `run-branch:` is a NEW fact
  `--preflight` writes on BOTH anchors — the value of `git symbolic-ref HEAD` at preflight, pinned
  once beside `anchor-kind` — and it is fact 13 of the protocol's section 2, so the write set
  reaches the driver, the protocol template and its render, and the driver suite. A record on
  another branch, a record with neither field, a detached `HEAD`, a missing conf or no record at
  all keys nothing. Observed by AC3, AC4, AC14.
- **S3** — the allow set is the tail of the driver's `PHASES_CORE` from `VERIFYING`, spelled in the
  hook and pinned to the driver by a direct read and by a suite arm. Observed by AC3, AC6.
- **S4** — the fragment, `gate-guard.fragment.json`, and the wiring of `.claude/settings.json`
  through `tools/settings-merge.py --fragment`. LAST in the pass order, after every direct
  observation S1 to S3 and S5 to S8 name, because the entry is live the moment it lands and the
  hook then denies its own suite shapes for the rest of the run. Observed by AC7, AC8.
- **S5** — the withheld suite, `gate-guard.test.sh`, its `project-owned` row in the kit descriptor
  and its budget row, so `run-unattended-gates.sh` enumerates it and the bar does not. Its verdict
  is the main loop's at `VERIFYING`, returned in `summary`; the pass never runs it. Observed by
  AC9.
- **S6** — the adopter's `--check` arm reports the hook UNWIRED, naming the merge command as the
  remedy, and the adopter suite's fixture carries the precondition the arm reads. Observed by AC10.
- **S7** — the corpus measurement of the shipped predicate, hits and near-misses, recorded in the
  unit's build record. Observed by AC11.
- **S8** — the prose: the kit README, the skill template and its render, the map dossier, one trap
  line in the kickoff manifest, and the kit version one step past where this unit found it. Each
  carrier has a pinned phrase in §4. Observed by AC8, AC12, AC13, AC15.

## 3. Non-goals (OUT)

- **No denial of the plain bar.** `run-gates.sh` with neither `GATE_FULL` nor `GATE_SELFTESTS` set
  is the scoped bar the owner allows at the main loop. The hook cannot tell a child from the main
  loop, so the plain bar inside a child is forbidden by the instruction unit 1 puts in the child
  prompt, not refused here.
- **No phase-vocabulary change**, no new conf key, no new gate leg. The hook reads what the kit
  already declares: `MEMORY_ROOT` from `.unattended.conf` and `phase:` from a run-state record. One
  new run-state FACT, `run-branch:`, and that is the whole protocol change.
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
- **Every criterion in §6 is a direct observation, and not because a gate demands it.** Unit 2's
  cutoff is 2026-09-14, so this spec, dated 2026-09-13, is outside that gate's population; the
  criteria are direct because the build README's fifth rule and the child prompt unit 1 ships bind
  the pass regardless, and because once S4 lands the hook itself denies a suite invocation in the
  pass that built it. Every deny shape is a §4 table row, §6 cites rows and never spells an
  invocation as an observation, and the suite S5 names appears in §6 as prose and once as a
  `grep` argument with `grep` at command position, never bare inside a backticked token. Unit
  2's `BAR` regex, typed from its §4, matches no backticked token of this §6's bullets or of §7's
  leg line: probed 2026-09-14 on that regex over this file's two graded populations with the
  checker's own `TICK`, `LEG_LINE` and `extract_gates`, and the probe's liveness control is the
  same regex matching a bare suite basename. Round 2 M2 found the one token rev-2 had left, in
  AC9; rev-3 removed it. Row D1 reads the empty assignment as the OFF spelling, which is the
  plain bar, and unit 2's predicate agrees.

### Edges

- **consumes-from** `TOOL-aDeferredBar-1` — the child-prompt instruction against the PLAIN bar
  inside a pass, which this hook admits by design; without it the scoped-bar case inside a child is
  neither refused nor forbidden. Also the kit version as that unit leaves it: this unit steps one
  past, and the render verb unit 1 §4 Carrier 3 names is admitted by the read-only verb rule in §4.
  Unit 1 leaves `tools/unattended/PROTOCOL.template.md` untouched but for its version marker; this
  unit is the one that edits its section 2, after that bump has landed.
- **consumes-from** external — `TOOL-cRefutedPremise-1`'s measurement that a `Bash|PowerShell`
  `PreToolUse` hook fires inside a `Workflow` sidechain. Nothing here re-measures it; if it were
  false the hook would still bind the main loop and nothing else.
- **hands-off** external — a `check-wiring.sh` arm for this hook, a govkit `selfcheck` arm for a
  `*.test.sh` in a kit directory with a budget row and no `project-owned` claim (already filed as
  `TOOL-aDeferredBar-4` from round-1 M8, in the same commit as rev-2, so the landing files no
  second row; the resolution probe in AC9 found `check-brief-recorded.test.sh` shipping through
  the `**` rule today), and a real tokenizer if the textual ceiling above ever stops being
  enough.

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
  -> resolveRunPhase(root, memoryRoot, ref) records whose run-branch, else branch-ref, equals ref;
                                            none: exit 0
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
from their templates, and unit 1 §4 Carrier 3 names it as the render of the method. The verb list
is textual and generic, so a suite that ignores an unparsed `--check` would run whole behind it; no
call in the corpus has that shape, and the `ponytail:` comment on the list names it as the ceiling.

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
way. That grammar is the defining property of the predicate, so AC2 places a deny token after a
separator and AC5 places one as the argument of a `grep`: a line-start-only predicate fails the
first and an anywhere predicate fails the second.

### The key

`phase:` and the branch fact are what the hook reads from a record. `branch-ref:` is NOT that
fact: `unattended.sh:2742` writes it only under `[ -n "$BREF" ]`, the comment at `:2353` says it is
written only where the anchor scope makes the run's own branch meaningful, and protocol fact 10
reads "present only when the second anchor fired". Tallied 2026-09-14 over every
`memory/builds/*/RUN.md` in this tree: 17 of 44 anchored records are `anchor-kind: default-branch`
and none carries `branch-ref:` — the strict-mandate form, the protocol's primary anchor, and the
kit default for every adopter whose conf leaves `ANCHOR_SCOPE` blank. Keyed on `branch-ref:`
alone the hook reads as wired and never fires on any of them.

So `--preflight` records the run's LOCAL branch under a new fact on BOTH anchors: `run-branch:`,
the value of `git symbolic-ref HEAD` at preflight (`refs/heads/...`), pinned once beside the
`anchor-kind` pin at `unattended.sh:2724` in the same `[ -n "$(fact ...)" ] ||` idiom, written
only when `symbolic-ref` resolves — a detached preflight writes nothing, and the hook keys nothing
there, which AC4 already lists. The hook keys on `run-branch:` first and falls back to
`branch-ref:` for a record written before the fact existed, so the 27 `run-branch`-anchored records
in this tree key exactly as before. The protocol's section 2 gains fact 13, opening
`**The run's local branch ref**`, recorded by `--preflight` on both anchors, and the sentence after fact 12 that says
which facts are absent when keeps fact 13 out of its absent set. The render
`memory/guides/UNATTENDED-PROTOCOL.md` is a placeholder-free copy the adopter re-copies; it
measures 57815 bytes against the 61440-byte `GUIDE_CAP_BYTES` in `check-memory-hygiene.sh:84`
(3625 bytes of headroom, PINNED 2026-09-14) and 666 lines against 750, and the fact costs about
300 of those bytes. No gate grades the fact list itself: check 10 of `check-unattended.sh`
byte-compares the shipped protocol to the installed copy and nothing reads section 2 as data, so
the liveness of the write is one arm in the driver suite beside its arm 50d, asserting a
default-branch-anchored preflight writes `run-branch: refs/heads/<branch>`.

Three records in this tree prove why the branch is the key and not the existence of a record:
`aUnblockedFleet` and `aClosedDocket` sit at `BUILDING` on branches nobody has checked out for
days, and three older `LANDING` records carry no branch fact at all. Keyed on "any record is
live", the hook would deny every session in this repository forever; keyed on the branch, those
five records key nothing.

When more than one record names the current branch, the hook reads them all and denies if any of
them is in a phase outside the allow set, naming that one.

### The allow set

`PHASES_ALLOW = ['VERIFYING', 'LANDING', 'LANDED', 'ABORTED']`, with the comment saying it is the
tail of `PHASES_CORE` in `unattended.sh:337` from `VERIFYING` onward. Those four are where the owed
`GATE_SELFTESTS=1` bar for kit work, the close's own bar and the lander run, all by the main loop.
Every other phase denies, a project's `PHASES_EXTRA` members included, because an extra phase is by
construction before landing. The restatement is pinned by a direct read (AC6) and by a suite arm
that reads the driver's line and compares, which is the liveness the kit's own checker cannot
supply — see §8.

### The fixture and the direct observation

Every §6 observation is one payload fed to the hook on stdin —
`{"tool_name":"Bash","cwd":"<FIX>","tool_input":{"command":"<row>"}}` — with the exit code and
stderr asserted; `node` at command position is no deny shape, so the observation is admitted
whatever phase the run is in. `FIX` is a scratch tree under `mktemp -d` holding `.git/HEAD` (`ref:
refs/heads/fx`), a `.unattended.conf` with `MEMORY_ROOT=memory`, and one `memory/builds/fx/RUN.md`
carrying `phase:`, `anchor-kind:` and the keying fact the arm needs, never the real tree. `HOOK` is
the hook's path from the files table below, and `P` holds the arm's payload; the row's command
string is stated in prose beside each criterion and never as a token, because the pass runs none
of it. The suite S5 names is these same payloads with the assertions around them, and it runs at
`VERIFYING` by the main loop. The hook exports its functions through `module.exports` and runs
`main` only under `require.main === module`, so a `require` for AC6's parity read and AC11's corpus
probe reads no stdin and denies nothing.

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
Constants `PHASES_ALLOW`, `READ_ONLY_VERBS`, `TOOLS`; all of them exported, `main` guarded by
`require.main === module`. The header carries a `gov:kit unattended@` marker the way
`procmon-hook.js` carries its kit's; `check-kit-versions.sh:169` pairs four named `.sh` carriers
and every `*.template.md`, so this marker is a courtesy the gate does not read, and the spec says
so rather than letting a reader assume it is graded.

### Pinned phrases, one per prose carrier

| carrier | phrase, grep-counted by AC13 or AC15 |
|---|---|
| `tools/unattended/README.md` | `refused at the tool call, not only forbidden` |
| `tools/unattended/SKILL.template.md` and its render | `gate-guard.js refuses it at the tool call` |
| `memory/map/features/unattended.md` | `gate-guard.js` |
| `memory/guides/SESSION-KICKOFF.md` | `gate-guard` on the trap line beside `scratch-guard` |

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/gate-guard.js` | new, the hook; no `tools/` literal, the conf key and the record basename are the only spellings; keys on `run-branch:` then `branch-ref:` |
| `tools/unattended/gate-guard.fragment.json` | new: `{name, event: "PreToolUse", matcher: "Bash|PowerShell", marker: "gate-guard.js", hook_path: "{kit}/unattended/gate-guard.js"}`, the shape of `procmon-hook.fragment.json`; `{kit}` resolves against the fragment's own location, two directories up, as `check-hook-destinations.sh` and `settings-merge.py` both read it |
| `.claude/settings.json` | one entry appended into the existing `Bash|PowerShell` `PreToolUse` group beside `scratch-guard.js`, by `python tools/settings-merge.py --fragment tools/unattended/gate-guard.fragment.json` and never by hand; LIVE the moment it lands, hooks being re-read mid-session — which is why S4 is the LAST write of the pass |
| `tools/unattended/unattended.sh` | the `run-branch:` preflight write beside the `anchor-kind` pin at line 2724, pinned once in the same idiom, from `git symbolic-ref HEAD`, skipped when that does not resolve |
| `tools/unattended/PROTOCOL.template.md` | fact 13 in section 2's numbered list, and the sentence after fact 12 amended so fact 13 is named as always written when `HEAD` is a branch |
| `memory/guides/UNATTENDED-PROTOCOL.md` | re-copied by `bash tools/unattended/adopt-unattended.sh`, never edited; check 10 of `check-unattended.sh` grades the pair |
| `tools/unattended/unattended.test.sh` | one arm beside 50d at line 2897: a default-branch-anchored preflight writes `run-branch:` equal to `$(git symbolic-ref HEAD)` read from the fixture at the moment of the preflight, and the arm asserts against that read, never a literal — `reset_tree` at line 355 checks out `unit`, so the value there is `refs/heads/unit`, and a preflight with `HEAD` on `main` is refused outright at `unattended.sh:903` where the merge-base equals `HEAD`; its budget row (3860 s against 2569 s measured) does not move for one arm on an existing fixture |
| `tools/unattended/gate-guard.test.sh` | new, the withheld suite; every fixture is a scratch repo under `mktemp -d` holding a `.git` `HEAD`, a conf and a record, never the real tree; prints `PASS (<n> assertions)` against a derived `FLOOR_ASSERTIONS` as `scratch-guard.test.sh:239` does; carries the `PHASES_CORE` parity arm and every payload §6 feeds by hand |
| `tools/unattended/adopt-unattended.test.sh` | `seed()` gains `gate-guard.fragment.json` in its copy list and writes a `.claude/settings.json` carrying the fragment's marker, so its two `--check` arms at lines 76 and 119 keep exit 0 once the S6 arm exists; its 60 s budget row (38 s measured) does not move for one file write and one grep |
| `tools/unattended/kit.toml` | `gate-guard.test.sh` joins the `project-owned` include list; the `**` engine rule already ships the hook and the fragment |
| `tools/run-gates/selftest-budgets.txt` | one row, budget from the measured reading times 1.5 floored at 60 s, so `run-unattended-gates.sh` enumerates it through the runner's list verb |
| `tools/install-prefix-carried.txt` | the `selftest-budgets.txt` row RAISED 14 to 15 by hand with its reason, because every budget row is a gov suite path by construction and the ban admits a hand-justified raise in the pass that wants it |
| `tools/unattended/adopt-unattended.sh` | a sixth artifact in the `--check` branch: the settings file lacks the marker read from the kit's fragment, print the UNWIRED refusal naming `$PY $ROOT/tools/settings-merge.py --fragment $KIT_REL/gate-guard.fragment.json` and exit 1, in the branch's own sequential-refusal style. The brief named `adopt-process-monitor.sh`'s `add_problem` register; this adopter has no register and adding one for a single arm is a second style in one file |
| `tools/unattended/README.md` | the paragraph: the act is refused, not only forbidden, and which shapes; pinned phrase above |
| `tools/unattended/SKILL.template.md` | the half-sentence appended to the bullet unit 1 adds; pinned phrase above |
| `.claude/skills/unattended/SKILL.md` | re-rendered by `bash tools/unattended/adopt-unattended.sh`, never edited |
| the version step | `KIT_UNATTENDED_VERSION` in `unattended.sh`, `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh` with their same-line markers, every `tools/unattended/*.template.md` marker, `README.md`, `playbook.fixture.md`, and the four installed copies the adopter re-copies or re-renders under `memory/guides/` and `.claude/skills/` — one step past the value read from `unattended.sh` at dispatch, DERIVED there and not pinned here |
| `memory/map/features/unattended.md` | prose refresh on touch naming the hook; no inventory key is claimed in `memory/map/generated/inventories.json`, because `git-hooks` enumerates `.githooks/` and no class enumerates a `PreToolUse` hook |
| `memory/map/generated/` | `symbols.json` re-rendered by `python tools/codebase-map/gen_map.py --write` after the hook lands, in the same commit: the `kit-js` symbol layer (`map_extractors.py:212`, `enumerate_exports` plus `scan_js_definitions` over all of `tools/`) indexes every kit `.js` and already carries `scratch-guard.js` and `procmon-hook.js`, so a new `gate-guard.js` exporting ten functions moves the artifact and the freshness test reds until the regen |
| `memory/guides/SESSION-KICKOFF.md` | one trap line beside the `scratch-guard` line at `SESSION-KICKOFF.md:221`, with BOTH stamps re-stamped in the same commit as unit 1's S5 spells them: `last-audit` (datetime advanced, sha of `git merge-base origin/main HEAD`) and `last-body-change` (the sha of the commit's parent, the way `a4a512de` stamped `2661b66b`), and a `manifest-audit: delta` line in the commit message |

### Alternatives rejected

- **The hooks kit as the home.** The key is this kit's record and conf key; a hook under
  `tools/hooks/` would name both by literal, which the install-prefix ban grades.
- **Deny whenever any record is live.** Refuted by the two stale `BUILDING` records above.
- **Key on `branch-ref:` alone.** Refuted by the 17 of 44 default-branch records that never carry
  it; the alternative to a new fact was to scope the refusal to run-branch-anchored runs only, which
  leaves the protocol's primary anchor and the adopter default unguarded — see §8 F7.
- **Deny the plain bar.** The main loop owes it; a hook that denied it would be disabled in a day.
- **Read `PHASES_CORE` from the driver at run time instead of spelling four names.** The hook fails
  open, so a driver it could not read would switch the hook off silently. Four literals pinned by
  a direct read and a suite arm fail loudly on demand instead.
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
  time; §3 names it and the corpus says it is not a live shape. A record preflighted before this
  unit lands carries no `run-branch:`; the `branch-ref:` fallback keys the run-branch-anchored
  ones and the default-branch ones stay unkeyed until their next preflight, which is today's state
  and not a regression.
- testing — the pass observes each arm by feeding the hook the arm's payload directly, in
  seconds; the suite re-runs the same payloads and its `PASS (<n> assertions)` verdict, the
  `PHASES_CORE` parity arm, the adopter suite's two `--check` arms on the seeded fixture and the
  driver suite's `run-branch:` arm are the main loop's at `VERIFYING`, named in `summary`. The
  corpus probe reports hits and near-misses of the shipped predicate.
- migration — none; the settings edit is idempotent by `settings-merge.py`'s own structure and
  the fragment on an existing matcher appends into the existing group. The new fact is additive:
  a reader that does not know it ignores it, and the driver pins it once like `anchor-kind`.
- user docs — the kit README and the skill template, S8.

## 6. Acceptance criteria

Every observation below is the hook fed one payload on stdin, or a direct checker, in seconds;
`HOOK`, `FIX` and `P` are the §4 fixture paragraph's. The suite S5 names is not an observation
here: it runs at `VERIFYING` by the main loop and its verdict travels in `summary`. S4 is the last
step of the pass, so every hook-fed observation precedes the wiring; what is observed after it
(the seventh, eighth, twelfth, thirteenth and fifteenth criteria) is greps and checkers carrying
no deny shape.

- **AC1** — When `P` names a `FIX` whose record is at `BUILDING` on the fixture's own branch and
  whose command is row D1 with the `GATE_SELFTESTS` prefix on the plain bar,
  `printf '%s' "$P" | node "$HOOK"; echo "rc=$?"` prints `rc=2` and stderr carries
  `BLOCKED by gate-guard`. Observed RED before the hook file exists, where `node` reports the
  module missing and the code is not 2; that is the failing case the build rules require.
  Red when: the fixture's `HEAD` names the record's branch and the hook still exits 0.
- **AC2** — When the same `FIX` is fed, one invocation of
  `printf '%s' "$P" | node "$HOOK"; echo "rc=$?"` per payload, each of eleven payloads — row D1
  with the `GATE_FULL` prefix, D1 after `export`, D1 behind `env`, D1 behind a `NAME=value` word,
  D1 behind `timeout 30`, D1 after `&&`, D1 after `then`, D2, D3, D4, and D5 wrapping a D4 token in
  `bash -c` quotes — prints `rc=2` and each stderr names its matched token.
  Red when: an arm's stderr names a token the fixture command does not contain, the D5 arm allows
  because the nested body was blanked and never read, or either separator arm allows, which is a
  predicate matching at line start only.
- **AC3** — When the fixture's record is moved through `VERIFYING`, `LANDING`, `LANDED` and
  `ABORTED`, every row D1 to D4 prints `rc=0` from the same invocation with empty stderr; and when
  the record is at `BUILDING`, the plain bar with `GATE_JOBS=1`, each read-only verb form of D2, D3
  and D4, and row D1's OFF spelling, the empty assignment, print `rc=0`.
  Red when: `VERIFYING` is denied, which is the owed bar for kit work being refused.
- **AC4** — When the fixture record's branch fact names another branch, or the record carries
  neither `run-branch:` nor `branch-ref:`, or `HEAD` holds a bare sha, or no record exists, or
  `.unattended.conf` is absent, row D4 at `BUILDING` prints `rc=0`, one payload each; when `.git`
  is a worktree FILE whose `gitdir:` target holds the `HEAD` that keys a deny, it prints `rc=2`;
  when the record is `anchor-kind: default-branch` with no `branch-ref:` and a `run-branch:` equal
  to the fixture's `HEAD` ref, at `BUILDING`, it prints `rc=2`; and when the record carries
  `branch-ref:` equal to that ref and no `run-branch:`, it prints `rc=2`. The default-branch
  payload is observed RED first against a scratch copy of the hook with the `run-branch:` read
  removed, which prints `rc=0`: that is the 17-of-44 hole as rev-1 keyed it.
  Red when: the worktree arm allows, meaning the hook read the common dir's `HEAD` instead of the
  worktree's; or the default-branch arm allows on the shipped hook.
- **AC5** — When stdin is empty, not JSON, names another tool, or carries no command, the same
  invocation prints `rc=0`; and when the payload's command is `git commit -m` quoting row D4's
  token, a heredoc whose body spells row D1, or a `grep` whose argument is a bare suite name, it
  prints `rc=0`.
  Red when: the quoted mention is denied, which is the raw-text predicate the blanked view exists
  to replace; or the `grep` argument is denied, which is a predicate matching anywhere.
- **AC6** — When `sed -n 's/^PHASES_CORE="\(.*\)"/\1/p' tools/unattended/unattended.sh | grep -o 'VERIFYING.*'`
  runs, it prints `VERIFYING LANDING LANDED ABORTED`; and when
  `node -p "require(require('path').resolve(process.argv[1])).PHASES_ALLOW.join(' ')" "$HOOK"`
  runs, it prints the same four words. The suite's parity arm re-derives this comparison at
  `VERIFYING`.
  Red when: the two prints differ by one member, which is a restatement that drifted.
- **AC7** — When `python tools/settings-merge.py --fragment` is run with `gate-guard.fragment.json`
  twice, the second run changes no byte, and `bash tools/check-hook-destinations.sh` prints an
  `ok` row for the fragment resolving to the hook's path. Observed once every hook-fed criterion
  above has been, because the first merge is the moment the hook goes live.
  Red when: the fragment resolves to a path no descriptor rule ships, which is a wiring hole.
- **AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the kit version
  step, it exits 0; and when `bash tools/check-kit-versions.sh` runs, it exits 0 with every
  unattended carrier at the stepped value.
  Red when: one carrier holds the old value, the five-carrier class the `stamps` gotcha names.
- **AC9** — When `grep -c 'gate-guard.test.sh' tools/run-gates/selftest-budgets.txt` runs, it
  prints `1`; when `grep -cP 'selftest-budgets\.txt\t15\t' tools/install-prefix-carried.txt` runs,
  it prints `1`; and when
  `python -c "import sys,pathlib as p;sys.path.insert(0,str(p.Path('tools','govkit')));import govkit as g;r=p.Path('.');print(sorted(g.resolve_entry(r,g.load_toml(p.Path('tools','unattended','kit.toml')),g.canonical_ctx('unattended'))['carved']))"`
  runs, its printed set names the suite S5 names, under the kit directory — the resolution govkit
  applies, so the `**` rule's pool has dropped the file.
  Red when: the budget row is absent, which is a suite exempt from the cost rule by arriving; or
  the printed set lacks the suite, which is the `**` rule shipping it to every adopter.
- **AC10** — When `(cd "$FIX" && bash tools/unattended/adopt-unattended.sh --check); echo "rc=$?"`
  runs in a scratch tree prepared in this order — seeded as the adopter suite's `seed()` seeds one,
  THEN the adopter's install run inside it with no verb, `bash tools/unattended/adopt-unattended.sh`
  from `FIX` as the suite's arm 1 does at its line 63, so the five existing artifacts are present, THEN
  `.claude/settings.json` omitted or removed — it prints `rc=1` and stdout names the hook UNWIRED
  and the `--fragment` remedy; with the marker present it prints `rc=0` and the arm is silent. The
  install step is the precondition: `--check` refuses sequentially and its first arm
  (`adopt-unattended.sh:259`, the unrendered Skill) exits 1 on a tree that is only seeded, before
  any sixth arm runs, so a seed-only fixture observes the Skill arm and not this one. Observed RED
  first: the installed-then-unwired tree against the adopter as it stands prints `rc=0`.
  Red when: an unwired tree passes `--check`, which is the silent-unwiring class.
- **AC11** — When `node "$PROBE" "$HOOK" ~/.claude/projects` runs, where `PROBE` is the probe
  script the build record carries verbatim and which requires the hook's exported `scanDenyHits`
  and `buildCommandView`, it prints the hit and near-miss count per row and the plain-bar count
  over every `Bash` and `PowerShell` `tool_use` command in the store, the build record carries
  that table, and every near-miss example printed is a mention, not a run.
  fixture: the store under `~/.claude/projects/` on node `a`; 3049 files on 2026-09-13.
  cost: about 70 s on node `a`.
  figure: DERIVED at observation time; §4's table is the 2026-09-13 reading.
  Red when: a listed near-miss is a run, which means the command-position grammar admits a shape
  the blanked view then hides.
- **AC12** — When `python tools/codebase-map/test_codebase_map.py` runs, it exits 0 with the
  `unattended` dossier refreshed, no new key claimed in `memory/map/generated/inventories.json`, and
  `memory/map/generated/symbols.json` re-rendered by `python tools/codebase-map/gen_map.py --write`
  in the same commit as the hook — its `test_generated_artifacts_are_fresh` byte-compares that
  artifact against a live render, and the `kit-js` layer indexes the new file's ten exports, so
  the test passes only after the regen; and when `python tools/lexicon/lexicon.py` runs, it
  reports no new offender in cell `js.function camel`. Observed RED first: the freshness test
  against the tracked `symbols.json` with the hook present and no regen, which reds naming the
  regen remedy.
  Red when: a hook function leads with a verb outside the declared table, or `symbols.json` is
  stale, which is a generated artifact landed for the main loop's bar to red.
- **AC13** — When `grep -c 'gate-guard' memory/guides/SESSION-KICKOFF.md` runs after the trap line
  lands, it prints `1`; `bash skills/session-kickoff/manifest-check.sh` exits 0;
  `git log -1 --format=%B | grep -c 'manifest-audit: delta'` prints `1` at the build commit;
  `grep -c "@ $(git merge-base origin/main HEAD)" memory/guides/SESSION-KICKOFF.md` prints `1`; and
  `grep -c "^last-body-change: $(git rev-parse HEAD~1)" memory/guides/SESSION-KICKOFF.md` prints
  `1`.
  Red when: the trap line lands without the re-stamp and the ratchet refuses it, the commit
  message carries no delta line, or `last-body-change` still names unit 1's parent — the half-stamp
  the `stamps` gotcha records.
- **AC14** — When `grep -c 'set_fact "$rel" run-branch' tools/unattended/unattended.sh` runs, it
  prints `1`; when `grep -c "^13\. \*\*The run's local branch ref" tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  runs, it prints `1` for each; and when `wc -c memory/guides/UNATTENDED-PROTOCOL.md` runs, it
  prints a figure under 61440. The driver suite's arm that preflights a default-branch fixture and
  reads the fact back is the main loop's at `VERIFYING`, and it asserts the value against
  `$(git symbolic-ref HEAD)` read from the fixture at the preflight, never a literal: the fixture
  sits on `unit` after `reset_tree`, so `refs/heads/main` is a value it cannot produce, and a
  preflight with `HEAD` on `main` is refused at `unattended.sh:903` before any fact is written.
  Red when: the template and the render disagree, which check 10 of `check-unattended.sh` also
  reds; or the render crosses the guide cap, which `memory hygiene` check 6 reds; or the arm
  spells the expected branch as a literal, which the fixture fails at `VERIFYING` inside the
  driver suite's 2569 s.
- **AC15** — When `grep -c 'refused at the tool call, not only forbidden' tools/unattended/README.md`
  runs, it prints `1`; when `grep -c 'gate-guard.js refuses it at the tool call' tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md`
  runs, it prints `1` for each; and when `grep -c 'gate-guard.js' memory/map/features/unattended.md`
  runs, it prints a figure of `1` or more.
  Red when: any count is `0`, or the template carries the phrase and the render does not.

## 7. Gates

`hook destinations (every declared hook path ships)` · `unattended skill wiring` · `unattended kit gate` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The brief also named `verdict epoch (kit version dates the engine)`; dropped after reading
`tools/memory-tree/check-verdict-epoch.sh`, which grades the memory-tree engine's constant and
mentions this kit nowhere. `memory hygiene` joins for the protocol render's byte cap, and
`spec tokens` for this document's own tokens.

New arm: tools/unattended/gate-guard.test.sh · a fixture record at BUILDING and the flagged bar, one arm per §6 payload, the `PHASES_CORE` parity arm, and the default-branch record keyed by `run-branch:` · `FLOOR_ASSERTIONS` derived at the suite's first green, none moved

New arm: tools/unattended/unattended.test.sh · a default-branch-anchored preflight read back for `run-branch:` against the fixture's own `git symbolic-ref HEAD`, never a literal; the break is a driver that does not write it · none

New arm: tools/unattended/adopt-unattended.test.sh · no new arm — `seed()` writes the settings file the S6 arm reads; the break is an unseeded tree, `--check` exits 1 · none

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
  four names are spelled in the hook with the comment the brief asks for, and AC6's parity read
  and arm are the restatement's liveness.
- **F6 — which read-only verbs the file-token rows admit.**
  RESOLVED (agent, 2026-09-13, delegated): `--list`, `--check`, `--rank`, `--help`, `--render`,
  each measured under 20 s in §4, generic over rows D2 to D4 and never over D1. The alternative,
  naming `kit-dogfood-parity.test.sh` for its `--render`, is a sibling-kit literal.
- **F7 — a branch fact on both anchors, or a refusal scoped to run-branch-anchored runs.**
  RESOLVED (agent, 2026-09-14, delegated): the fact. Review round 1 H4 measured 17 of 44 anchored
  records keying nothing under `branch-ref:`, the protocol's primary anchor among them; a new
  `run-branch:` fact written on both anchors is a protocol field-list change inside the byte
  headroom §4 states, and the scoped alternative leaves the adopter default unguarded. Vetoes
  clean: no new dependency, surface or governance carrier, and the write surface is one fact in a
  file the driver already writes.
- **F8 — direct criteria in this spec, or a wider `BAR` in unit 2.**
  RESOLVED (agent, 2026-09-14, delegated): direct criteria, the default under unit 2 §4. The
  build README's fifth rule and unit 1's child prompt bind the pass whichever way unit 2's
  predicate reads, and with unit 2's cutoff at 2026-09-14 this spec is outside that gate's
  population either way; widening the predicate to admit a bare suite basename would reverse unit
  2's fork D, and this document does not need it: rev-2 wrote that sentence while AC9 still
  carried one bare `*.test.sh` basename inside a backticked token, which round 2 M2 found, and
  rev-3 un-backticked it, so the premise holds by the probe §3's last bullet states rather than
  by assertion. The resolution stands.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-14 · folded review round 1: B1 and H1 (§3 last bullet rewritten, §6 AC1 to AC10
  re-observed by feeding the hook each payload directly, the suite named in prose and under
  `New arm:` only, S4 last in the pass order, §8 F8) · H4 (S2, §4 The key, files table, AC4, AC14,
  §8 F7: the `run-branch:` fact on both anchors with the `branch-ref:` fallback, the protocol's
  fact 13 and its headroom, the driver-suite arm) · H5 (the adopter suite's `seed()` row and its
  unmoved budget) · M5 (AC2's separator payloads, AC5's `grep` payload) · M8 (AC9's role
  resolution through `resolve_entry`; the govkit `selfcheck` arm is the backlog row §3 hands off,
  `TOOL-aDeferredBar-4`) · L1 (§4 pinned phrases, AC13's delta-line grep, AC15) · L2 (unit 1 §4
  Carrier 3 cited in §3 and §4) · L4 (the manifest row names both stamps, AC13 observes both) ·
  L5 (the retired per-branch invariant deleted from §4 The key).
- rev-3 · 2026-09-14 · §3 · §4 · §6 · §7 · §8 · AC9 · AC10 · AC12 · AC14 · folded review round 2:
  M2 (AC9's second suite mention un-backticked; §3's last bullet now states the `BAR` probe over
  this file's two graded populations, run 2026-09-14 and printing zero hits, instead of asserting
  it; §8 F8's premise sentence rewritten, its resolution kept) · M3 (AC10's fixture precondition:
  seed, run the adopter's install with no verb, THEN omit or remove `.claude/settings.json`, then
  `--check`; the RED-first re-stated on that fixture) · M4 (the `unattended.test.sh` files-table
  row, the §7 `New arm:` line and AC14 assert `run-branch:` against the fixture's own
  `git symbolic-ref HEAD`, never the impossible literal `refs/heads/main`) · M5 (a
  `memory/map/generated/` row for the `symbols.json` regen the `kit-js` layer forces; AC12 names
  the freshness test's subject and its RED-first) · L4 (§3 hands-off edge and the rev-2 line cite
  `TOOL-aDeferredBar-4` instead of promising a row the landing would file twice).

## 10. Reuse audit

The seams this unit EXTENDS, each verified against source at `b2a330be`:
`tools/settings-merge.py --fragment` for the idempotent settings edit, which appends a fragment on
an existing matcher into the existing group (`settings-merge.py:233`);
`tools/check-hook-destinations.sh` arm 1, which resolves `{kit}` against the fragment's own
location and joins it to the descriptor's shipped set; the `project-owned` include rule in
`tools/unattended/kit.toml` and the declared row population in
`tools/run-gates/selftest-budgets.txt`, which is how a withheld suite is enumerated, and
`resolve_entry` in `tools/govkit/govkit.py`, which is the resolution AC9 reads rather than a
second one; the `branch-ref:` and `phase:` fields `lib-unattended.sh:405` already reads, and the
pinned-once `set_fact` idiom at `unattended.sh:2724` that `run-branch:` copies. The hook's shape
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
