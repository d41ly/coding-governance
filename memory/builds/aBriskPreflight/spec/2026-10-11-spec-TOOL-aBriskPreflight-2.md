# TOOL-aBriskPreflight-2 — check-wiring reads the settings file and each fragment once, and resolves python once

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 2 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-build-TOOL-aBriskPreflight-2-spawns-ab.md](../build/2026-10-11-build-TOOL-aBriskPreflight-2-spawns-ab.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-2-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-2-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-2-spec-brief.md) | research | — |
| [2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md) | diff-review | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 TOOL-aBriskPreflight-10 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-wiring.sh` re-reads the same input and re-starts the same interpreter once per
question: one `sed | head` per key per fragment, a seven-stage pipeline over the whole settings file
on every `matchers_of` call, and a launcher probe plus a second interpreter start on every
`resolve_kit_file` call. The baseline record charges 136 s of a 568 s traced `--check` at BASE to
the functions holding these readers (PINNED, run `cw-base-traced`, node `a`, 2026-10-11). This unit
makes each of them one read per RUN, answered from memory after that, with every printed line, every
verdict and the exit status unchanged.

## 2. Scope (IN)

Line numbers are at b726385f and move once TOOL-aBriskPreflight-1 lands first in the same file.

- **S1** — ONE FRAGMENT READER. A new `read_fragment_keys <path>` reads a fragment file once with
  bash's own `read` and `[[ =~ ]]`, starting no process, and takes `marker`, `matcher`, `event` and
  `hook_path` in that one pass. Each value is the one `json_str`'s `sed` yields today: the LAST
  `"key": "value"` on the FIRST line carrying one, a final line with no newline included. The four
  values are kept per path for the rest of the run, keyed by the repo-relative spelling
  `resolve_fragment_hook` already derives. `check_scratch_guard`, `check_recall_opened`,
  `check_card` and `resolve_fragment_hook` read through it, and each arm calls it in its own shell
  before it opens `$(resolve_fragment_hook …)`, so the subshell answers from the arm's read.
  `json_str` is retired. Observed by AC1, AC4 and AC6.
  **Readers:**
  by name: `tools/check-wiring.sh` spells `json_str` at its definition and at the eight call sites
  this item rewrites, and `memory/map/generated/symbols.json` lists it until S8 re-renders it; no
  other tracked file outside the build records spells it, by a git grep at writing.
  by value: NO VALUE READERS, because a shell function's name is called and never compared, counted
  or derived from, except by the lexicon leg, which grades the name this item adds in its place.
- **S2** — THE SETTINGS VIEW, BUILT ONCE. `matchers_of` builds its view of the settings file the
  first time it runs in a shell. It asks `settings_json` for the path and runs today's first two
  stages once, the `tr -d ' \t\r\n'` flatten and the event-key `sed`, keeping their output and the
  resolver's status in shell variables. Every call then filters that view with builtins only,
  applying today's five later tests unchanged, mapped in §4. Called with no argument, it builds the
  view and prints nothing. The view is built inside `matchers_of`'s own body, so the copy
  `settings-merge.py --selftest` lifts with a stubbed `settings_json` still runs alone. Observed by
  AC2, AC3, AC7 and AC8.
- **S3** — THE SETTINGS PATH, RESOLVED ONCE. The block that reports the settings scope
  (`tools/check-wiring.sh:685`) calls `settings_json` in the parent shell rather than in a
  substitution, so `_SETTINGS_CACHE` survives it, and then makes S2's no-argument call there. Every
  later `matchers_of` call, in a pipeline or a substitution, inherits the built view. A refusal is
  recorded once, in the view's status, which `matchers_of` returns as 2 on every call without asking
  again. `render_settings_path` reads `_SETTINGS_CACHE` directly when it is set. Observed by AC5.
- **S4** — PYTHON RESOLVED ONCE. The line that sets `PY` (`tools/check-wiring.sh:491`) also records
  in `PY_OK` whether a launcher ran. `resolve_kit_file` and the straggler arm read `PY_OK` and `PY`
  instead of calling `resolve_python` again, and the straggler arm's `command -v resolve_python`
  test goes with that call. With no launcher both take today's no-python paths and print today's
  `note` lines. Observed by AC9 and AC10.
- **S5** — KIT FILES THROUGH ONE INTERPRETER START. After the `--resolve-fragment` exit, a new
  `resolve_kit_files` resolves every pair in `KIT_FILE_PAIRS`, the `<home> <file>` pairs the arms
  pass to `resolve_kit_file`, through one python start, when `PY_OK` says one runs. The block
  between the `resolve_kit_dir` markers is unchanged; only the driver after it answers several
  pairs from one start, one line per pair, empty for a refused pair. `resolve_kit_file` answers a
  listed pair from those results, and a pair not listed through one start of its own, as today.
  Observed by AC10 and AC12.
- **S6** — THE TWO INLINE COPIES STAY BYTE-IDENTICAL. No line between the `resolve_python` markers
  or between the `resolve_kit_dir` markers changes; S4 and S5 memoize around them. Observed by AC11.
- **S7** — `tools/check-wiring.test.sh` gains three arms, each observed RED on its staged break: a
  shipped fragment carrying no `matcher` key, every launcher shadowed while `GOV_PYTHON` names one
  that does not run, and a literal pair absent from `KIT_FILE_PAIRS`. NOT OBSERVED by a criterion
  of its own: AC6, AC9 and AC12 are the observations those arms repeat, and the suite runs once, at
  the close.
- **S8** — `memory/map/generated/symbols.json` re-rendered by `gen_map.py --write` after S1 and S5.
  NOT OBSERVED by a criterion: the `codebase-map coverage + freshness` leg grades it.

## 3. Non-goals (OUT)

- `$(first_of …)` and `$(resolve_receipt_path …)` stay substitutions. `TOOL-aSparedSpawn-8` S3
  plans them.
- TOOL-aBriskPreflight-1's three loops: the merge-rows family harvest, the smoke's per-id count and
  the eol attribute read.
- The two `dirname` calls and the token `sed` inside `resolve_fragment_hook`. They are path
  arithmetic, not a re-read of an input, and `--resolve-fragment`'s byte parity with
  `settings-merge.py` rides on them. Named below as a follow-up.
- The consumers of a reader's output: `wired`'s `grep -qxF`, the `paste` and `tr` fallbacks the
  arms pipe `matchers_of` into, and `check_agentcap`'s two line greps over the settings file.
- Any edit to `tools/settings-merge.py`, its selftest's lift of `matchers_of`, or the hook
  destinations gate.
- Any bash-4-only construct, such as `mapfile` or an associative array. `tools/check-wiring.sh`
  uses none today and runs at SessionStart on hosts this repository does not choose.
- Any reader that needs python. The file runs as a SessionStart hook on hosts that may have none.
- The check-wiring kit's version bump. The build makes one bump per kit, after its last move.

### Edges

- **hands-off** `TOOL-aBriskPreflight-3` — the measurement of which arms preflight needs is taken
  once this unit's readers land, so the wall and spawn counts it compares are the ones this unit
  leaves.
- **hands-off** external — the path arithmetic in `resolve_fragment_hook`, a candidate for builtins
  once someone prices its byte parity with the merger's resolver.

## 4. Design

### Evidence

Read at 748ca395 on 2026-10-11. Its `tools/` bytes equal b726385f's, because a `git diff --stat`
from b726385f2 to HEAD over `tools/` prints nothing.

- `json_str` is `tools/check-wiring.sh:148`, a `sed -n` with a greedy `.*` piped to `head -1`. Its
  eight call sites are `:173` in `resolve_fragment_hook`, `:812`, `:813` and `:820` in
  `check_scratch_guard`, `:875` and `:885` in `check_recall_opened`, and `:942` and `:948` in
  `check_card`. Every one runs inside a `$(…)`, so each key costs a fork, a `sed` and a `head`.
- `matchers_of` is `:348` to `:373`. It asks `settings_json` through a substitution on every call,
  so `_SETTINGS_CACHE` (`:95`) never survives into the next call, then runs the eight-process
  pipeline. Its callers are `wired` (`:380`) and the arms' found-matcher lines.
- `tools/settings-merge.py:955` lifts `matchers_of` with `^matchers_of\(\) \{.*?^\}` under
  `re.S | re.M`, prepends a stub `settings_json` printing `$SJ`, and runs `matchers_of "$1"` in a
  fresh bash per tracked fragment (its arm 17). The lift stops at the first column-0 `}`.
- `resolve_python` (`:389` to `:417`) and `resolve_kit_dir` (`:424` to `:470`, its Python block
  `:426` to `:460`) are inline copies the resolve-python self-test's parity table compares block by
  block with `tools/lib/resolve-python.sh` and `tools/lib/resolve_kit_dir.py`. Only the text
  between the markers is compared.
- `resolve_kit_file` (`:478`) runs `resolve_python`, which RUNS each candidate, and then
  `resolve_kit_dir`, a second start. It is reached only through `$(…)` arguments to `first_of`, so
  a memo set inside it dies with its subshell. Its seven call sites ask six pairs:

| Call site | Arm | Pair |
|---|---|---|
| `:731` | `check_agentcap` | `hooks agent-cap.js` |
| `:799` and `:1463` | `check_scratch_guard`, `check_routed` | `hooks scratch-guard.fragment.json` |
| `:868` | `check_recall_opened` | `memory-recall recall-opened.fragment.json` |
| `:1111` | `check_merge_rows` | `memory-tree merge-rows.py` |
| `:1121` | `check_merge_rows` | `lib pyrun.sh` |
| `:1450` | `check_routed` | `memory-tree adopt-memory-tree.sh` |

- `PY` is set once at `:491`, above the `--resolve-fragment` exit at `:507`. The straggler arm
  re-runs `resolve_python` at `:1704` behind a `command -v resolve_python` test.
- The baseline counts at BASE: 17 `python3` starts, 182 `sed`, 21 `head` and 19 `tr` in one
  `--check` (PINNED, run `cw-base-traced`). 17 is the top-level probe, seven per-call probes, seven
  `resolve_kit_dir` starts, the straggler arm's probe and the straggler inventory itself.
- `tools/check-wiring.sh` contains no `mapfile`, `readarray` or `declare -A` (`grep` at writing).
- The `shell hygiene (a loop fed by a command substitution)` leg (`tools/gate-lint/sh_hygiene.py`)
  refuses a `while read` fed through a heredoc or a here-string by a command substitution, and
  follows one assignment back. A loop fed by a FILE redirect is its own named remedy.

### The fragment reader

`read_fragment_keys` reads the file with `while IFS= read -r _l || [ -n "$_l" ]`, the idiom
`read_proc_ledger` in `tools/unattended/unattended.sh` uses, so a last line with no newline is read.
For each key not yet found it tests `[[ $_l =~ $re ]]` against a regex held in a variable,
`.*"<key>"[[:space:]]*:[[:space:]]*"([^"]*)".*`, the `sed` pattern rewritten for ERE, and takes
`BASH_REMATCH[1]`. The first matching line wins, as `head -1` makes it win today. Within a line the
leading `.*` is leftmost-longest in both engines, so a key written twice on one line yields its last
value in both. A carriage return lands after the closing quote and is absorbed by the trailing `.*`
in both, whichever of them sees it.

The values go to `FRAG_MARKER`, `FRAG_MATCHER`, `FRAG_EVENT` and `FRAG_HOOK_PATH`. The cache is
five indexed arrays, one per value plus the path, searched linearly: at most a dozen fragments are
ever read. A path that is not a file yields four empty values and prints nothing, where `sed`
printed an error; no caller reaches that case, because each tests `-f` first.

In the arms the order of the verdicts does not move. Each arm reads all four keys before its first
test, and its tests run in today's order on the same values.

### The settings view

| Today's stage | The view's equivalent |
|---|---|
| `settings_json` in a substitution, every call | asked once per shell, the path and status kept |
| `tr -d ' \t\r\n' < "$_sj"` | run once, at the build |
| `sed 's/"\([A-Z][A-Za-z]*\)":\[/\n@\1@/g'` | run once, at the build; its output is the view |
| `grep -F -e "@${3:+$3@}"` | a substring test of each view line for `@<event>@`, or for `@` |
| `sed 's/{"matcher":/\n{"matcher":/g'` | the line cut at each `{"matcher":`, the leading piece kept |
| `sed 's/\].*$//'` | each piece cut at its first `]` |
| `grep -F -e "$1"`, then `grep -F -e "${2:-$1}"` | two fixed-string substring tests |
| `sed -n 's/^{"matcher":"\([^"]*\)".*/\1/p'` | the value of a piece opening `{"matcher":"`, to the next `"` |

The view is ONE string variable assigned from ONE substitution, and a call walks it with parameter
expansion. No `while read` is fed from it through a heredoc or a here-string, which the shell
hygiene leg would grade. The substring tests quote their operand, so a marker or a basename
carrying a glob character or a backslash, such as the `{CLAUDE_PROJECT_DIR}/<path>\"` filter
`wired` builds, matches as a literal string, as `grep -F` matches it. Every variable the view uses
is read defaulted, because `tools/check-wiring.sh` runs under `set -u` and the lifted copy does not.
`matchers_of`'s body carries no column-0 `}` before its own closing brace, because the lift stops
at the first one.

The view is never rebuilt within a run. No mode of the script writes the settings file, as its
header states at `:28` to `:31`, so a view built once describes the file every arm reads.

### Python and the kit files

`PY_OK` is set beside `PY`, on the line carrying the `gov:literal-python` marker, which stays on it.
`resolve_kit_file` keeps its no-python rung, the bash probe of the same two places and its
`note     resolver` line on stderr, printed per call as today.

`resolve_kit_files` runs after the `--resolve-fragment` exit, so the hook destinations gate's eleven
calls of that verb pay nothing for it, and only when `PY_OK` is set. It passes the inline block and
a driver that loops over the pairs, all in one `-c` string, exactly as `resolve_kit_dir` passes
them today. The results reach the cache without a loop fed by a substitution, and without an IFS
split that collapses an empty answer (`memory/gotchas/empty-field-collapses-unless-it-is-last.md`).

`KIT_FILE_PAIRS` is a declared list, so a call site whose pair it lacks still gets a correct
answer, through a start of its own. S7's third arm and AC12 compare it with the literal pairs the
source passes, so the list cannot drift without a red at the close.

### Verification in the pass

Every criterion runs in the pass, on its own, in seconds to minutes. A fixture clone lives at
`%TEMP%/bp2`: a short path, because a clone under the scratchpad fails with `Filename too long`.
Scratch probes and their logs live under the run's scratchpad. "Old" is `tools/check-wiring.sh` at
the commit the pass started from, and "new" is the pass's file; each is copied in turn to the
clone's `tools/check-wiring.sh`.

Each staged break edits a SHIPPED value in the clone, the real fragment or the real settings file,
never a synthetic one (`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`). The build
README asks for a break observed through a sliced arm. A slice of this suite must sit inside the
kit directory to derive its paths, and this run's temporary files go under the scratchpad. So the
pass runs the checker on the staged break directly, which is what the arm runs, and the arms run
with their suite at the close.

### Inventory

| Identifier | What it is | Cell |
|---|---|---|
| `read_fragment_keys` | the one fragment reader | `sh.function` |
| `resolve_kit_files` | the batched kit-file resolution | `sh.function` |
| `FRAG_MARKER`, `FRAG_MATCHER`, `FRAG_EVENT`, `FRAG_HOOK_PATH` | the reader's four outputs | none: no cell grades a shell variable |
| `_FRAG_PATHS`, `_FRAG_MARKERS`, `_FRAG_MATCHERS`, `_FRAG_EVENTS`, `_FRAG_HOOKS` | the per-path cache | none |
| `_SJ_VIEW`, `_SJ_RC` | the settings view and the resolver's status | none |
| `PY_OK` | the launcher memo | none |
| `KIT_FILE_PAIRS`, `_KF_KEYS`, `_KF_DIRS` | the declared pairs and their answers | none |

Both function names were asked of `tools/lexicon/lexicon.py` with `--suggest` and
`--as sh.function` at writing, and both answered OK.

### Files touched (estimate)

`tools/check-wiring.sh`
`tools/check-wiring.test.sh`
`memory/map/generated/symbols.json`

### Alternatives rejected

- One `sed` per fragment printing all four keys, the owner's "one interpreter call" read
  literally. It costs one process per fragment where the builtin read costs none (§7 F1).
- A Python JSON parse. It breaks the SessionStart contract on a host with no python, and JSON
  semantics take a key's first value where `sed` takes the last on a line.
- A loader function beside `matchers_of`. The selftest lifts `matchers_of` alone, so arm 17 would
  call a function its lifted script does not define (§7 F3).
- A memo inside `resolve_kit_file`. It runs in a substitution, so the memo dies with the subshell,
  and seven calls would still start six interpreters.
- Deriving the pairs with a `sed` over the script's own text. It reads its own comments as call
  sites and spends the spawn the list saves (§7 F2).

## 5. Acceptance criteria

- **AC1** — When a scratch probe runs old `json_str` and new `read_fragment_keys`, each extracted
  from its own file by its definition line, over every file `git ls-files '*.fragment.json'` lists
  and over seven scratch fixtures, the two give equal values for `marker`, `matcher`, `event` and
  `hook_path` on every file. The fixtures are: a one-line compact fragment carrying `"marker"`
  twice; a CRLF fragment; a fragment whose `hook_path` line ends with no newline; a fragment with
  no `matcher`; a value carrying `\"`; spaces and a tab around the colon; and `"marker_x"` written
  before `"marker"`.
  Red when: the new reader takes the first value on a line, misses a last line with no newline, or
  returns a value for an absent key.
  fixture: built by the pass under the scratchpad; the tracked fragments are counted by that
  `git ls-files` at observation, DERIVED.
- **AC2** — When a scratch probe lifts old and new `matchers_of` with the regex
  `tools/settings-merge.py` uses, each behind a stub `settings_json`, the two print identical lines
  for every marker, basename and event triple the arms pass on this tree, over `.claude/settings.json`
  and over a scratch settings file. That file carries two events, a group without the marker, an
  empty matcher, two groups sharing one marker, a `]` inside a command string, the dash-led marker
  `--write`, and a basename filter ending in an escaped quote. The new copy called with no argument
  prints nothing.
  Red when: any triple's lines differ, or the no-argument call prints a matcher.
- **AC3** — When `python tools/settings-merge.py --selftest` runs, it prints
  `settings-merge selftest: PASS` and no `SKIP arm 17` line.
  Red when: the lifted `matchers_of` needs anything the lift does not carry, so a fragment's
  matcher is not returned.
  cost: one bash start per tracked fragment and the rest of the selftest; under a minute on node
  `a` UNVERIFIED.
- **AC4** — When `bash tools/check-hook-destinations.sh` runs, it exits 0 and prints neither
  `the two readers DISAGREE` nor `a reader refused it`.
  Red when: `--resolve-fragment` resolves a fragment's `hook_path` to bytes `settings-merge.py` does
  not.
- **AC5** — When old and new each run `bash tools/check-wiring.sh --check` in the clone, their
  stdout, their stderr and their exit statuses are equal byte for byte. The same holds for a second
  pair of runs with `GOV_SETTINGS_JSON` naming a file that does not exist.
  Red when: a line or a status differs on either pair, including the settings refusal's `note`
  lines.
- **AC6** — When the clone's `tools/hooks/scratch-guard.fragment.json` loses its `matcher` line and
  new runs `bash tools/check-wiring.sh --check`, it exits 1 and its `UNWIRED  scratch` line names
  that fragment and reads `declares no marker/matcher/event/hook_path`. With the line restored,
  the `ok       scratch` line for `PreToolUse` returns.
  Red when: the absent key is read from the cache of another fragment, or the arm passes.
- **AC7** — When the `Workflow|Agent` matcher in the clone's `.claude/settings.json` is edited to
  `Workflow` and new runs `bash tools/check-wiring.sh --check`, its `UNWIRED  agent-cap` line reads
  `wired under matcher 'Workflow', not 'Workflow|Agent'`. Restored, it prints `ok       agent-cap`.
  Red when: the view keeps the old matcher, or the found matcher is not named.
- **AC8** — When the `resume|compact` matcher in the clone's `.claude/settings.json` is edited to
  `resume` and new runs `bash tools/check-wiring.sh --check`, its `UNWIRED  card` line reads
  `wired under matcher 'resume', not 'resume|compact'`. Restored, it prints `ok       card`.
  Red when: a card replay wired for `resume` alone reads as wired.
- **AC9** — When old and new each run `bash tools/check-wiring.sh --check` in the clone with stubs
  named `python3`, `python` and `py` that exit 9 first on `PATH`, and `GOV_PYTHON` naming a fourth
  such stub, their outputs and statuses are equal. Stderr carries the `note     resolver` line and
  stdout carries `note     straggler — no usable python launcher resolved`, and no line reads
  `skip     agent-cap`.
  Red when: the memo reads a launcher as resolved, or the bash probe rung does not run.
- **AC10** — When `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` traces old and new in the
  clone, one after the other on one host state, `2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`
  reports both forks and execs lower for new. In new's trace exactly one row carries
  `-c 'import sys'` and exactly one carries `-c '# >>> resolve_kit_dir`, each from
  `check-wiring.sh`; exactly one row carries `tr -d ' \t\r\n'`; and no row carries
  `sed -n 's|.*"`. Old's trace carries those rows once per call.
  Red when: a per-call launcher probe, kit-dir start, flatten or `json_str` row survives in new.
  figure: the totals are DERIVED from the two traces; the counts of one are this design's on this
  tree, where every arm's pair is in `KIT_FILE_PAIRS`.
- **AC11** — When `awk '/^# >>> resolve_python/,/^# <<< resolve_python/'` extracts the block from
  new and from `tools/lib/resolve-python.sh`, `diff` prints nothing; the same holds for the
  `resolve_kit_dir` block against `tools/lib/resolve_kit_dir.py`.
  Red when: any line between either pair of markers changes.
- **AC12** — When a grep over new lists the two literal words after every `resolve_kit_file` call,
  each pair is in `KIT_FILE_PAIRS`. With one pair taken out of the list, the same comparison names
  it.
  Red when: a call site asks a pair the list lacks, or the comparison passes with a pair missing.

## 6. Gates

`transition-audit arms` · `straggler-guard arms` · `check-wiring self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `hook destinations (every declared hook path ships)` · `settings-merge selftest` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-wiring.test.sh · covers AC6 · a shipped fragment with its matcher line taken out, checked RED and then restored · none

New arm: tools/check-wiring.test.sh · covers AC9 · every launcher name shadowed by a stub that exits 9 and GOV_PYTHON naming one more, with the resolver and straggler notes asserted · none

New arm: tools/check-wiring.test.sh · covers AC12 · one literal pair taken out of KIT_FILE_PAIRS · none

The pass verifies with AC1 to AC12 only. The listed legs run once, at the close, after the last
unit is terminal.

## 7. Open questions

- **F1 — How is a fragment read once: one interpreter call, or no process at all?** (a) One `sed`
  per fragment printing the four keys, the owner's words read literally. (b) bash's own `read` and
  `[[ =~ ]]`, which the brief admits because it satisfies "parsed once" and costs less. AC1 is the
  observation that would refute (b), by any value differing from the `sed` reader's.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b). It starts no process, which is the most this item
  can cut, and it trips no veto: no dependency, surface or carrier moves.
- **F2 — How does `resolve_kit_file` learn the pairs to resolve in one start?** (a) A declared
  `KIT_FILE_PAIRS`, with a start of its own for a pair it lacks and an arm comparing it with the
  call sites. (b) A `sed` over the script's own text at run time. (c) A memo per pair. (c) fails,
  because the function runs in a substitution. (b) reads comments as call sites and spends a spawn.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). A stale list costs one start and never a wrong
  answer, and the arm makes it red at the close.
- **F3 — How does the view reach the arms when `settings-merge.py` lifts `matchers_of` alone?**
  (a) The view is built inside `matchers_of` on its first call, and the parent makes one
  no-argument call to build it before any subshell opens. (b) A separate loader, with the
  selftest's lift widened to carry it, an edit to another kit's file and leg. Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). It keeps the edit inside this file, and (b) changes
  a file outside the unit's write set, which veto 2 leaves to the owner.

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft, from the spec brief
  `2026-10-11-prompt-TOOL-aBriskPreflight-2-spec-brief.md`.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py`, asked the phrase in the first fenced line below, ranked
`read_text`, `read`, `run` and `read_conf` by name stem, and `resolve_python` as a SEAM with 66
installs. `resolve_python` is the seam this unit
memoizes AROUND, without an edit between its markers. None of the others is a shell helper a
copy-installed kit can call, because the shared library ships to no adopter. So no existing seam
fits the batching or the memo, and this unit extends the readers it edits in place: `matchers_of`,
`resolve_kit_file` and the `resolve_kit_dir` driver. The builtin file-read idiom is the one
`read_proc_ledger` uses in `tools/unattended/unattended.sh`, verified in source. The other fragment
parser, `load_fragment` in `tools/settings-merge.py`, is Python and is ruled out by the SessionStart
contract.

The recall probe returned `TOOL-aReplayedCard-2`, which made `resolve_fragment_hook` one function
and gave it the `--resolve-fragment` parity S1 keeps, and `TOOL-aRepatriatedFork-46`, the no-python
probe rung S4 keeps. It also returned `TOOL-aDeferredBar-7`, an open ask that no arm grades the
gate-guard fragment; that is TOOL-aBriskPreflight-3's question and not this unit's.

Recall terms used: check-wiring json_str matchers_of settings_json resolve_python resolve_kit_file
resolve_kit_dir fragment marker matcher SessionStart no-python parity. The two probes, verbatim:

```bash
python tools/codebase-map/reuse_lookup.py "read a JSON fragment once and memoize settings flatten and python launcher resolution per run"
python tools/memory-recall/query.py "how does check-wiring read fragments and the settings file and resolve python without spawning a process per item" --terms "check-wiring json_str matchers_of settings_json resolve_python resolve_kit_file resolve_kit_dir fragment marker matcher SessionStart no-python parity"
```
