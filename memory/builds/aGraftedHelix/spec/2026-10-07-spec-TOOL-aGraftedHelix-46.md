# TOOL-aGraftedHelix-46 — govkit reads a quoted conf value followed by a comment the way the shell that sources it does

**Status:** SPECCED · rev-3 · 2026-10-07 · node a · Tier-1 · base e1f4d8c0 · streams tooling · order 27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md](../prompts/2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md) | journal | TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-47 |

<!-- /gen:spec-records -->

## 1. Goal

`read_conf_key_gaps` in `tools/govkit/govkit.py` peels one quote layer only when a value both opens
and closes with it, so a quoted value followed by a comment keeps its quotes and its comment. Every
kit adopter SOURCES the conf, so govkit grades a different value from the one the kit reads, and a
required key that is empty or still the example's placeholder reads as covered. This unit gives
govkit bash's rule and pins it to the shell and to the memory-tree kit's `parse_conf_line` with one
arm.

## 2. Scope (IN)

- **S1** — `tools/govkit/govkit.py` gains `parse_conf_assignment(line)`, which returns
  `(key, value)` for one assignment line or `None`. The key grammar and the `export` prefix are
  `CONF_KEY_RX`'s, as today. The value follows the rule `TOOL-aRepatriatedFork-38` S1 gave every
  kit reader:
  whitespace right after `=` is an empty value; a quoted value, single or double, ends at its
  matching quote whatever follows; an unquoted value ends at a `#` that follows whitespace, so a
  `#` opening the word is data. `read_conf_key_gaps` takes every value from it, and the last
  assignment still wins. Observed by AC1 and AC3.
- **S2** — The docstring of `read_conf_key_gaps` states that rule and what it does not read: an
  unterminated quote, an escaped quote, adjacent concatenation, and spellings bash itself rejects.
  Observed by AC5.
- **S3** — `tools/govkit/selftest.py` gains a module-level `check_conf_reader_parity(tmp)`, called
  from `main()`. It feeds one spelling table to three readers: govkit's `parse_conf_assignment`,
  the memory-tree kit's `parse_conf_line` loaded from `KIT_DIRS["memory-tree"]`, and bash sourcing
  the line through govkit's `resolve_shell_argv`. Bash is the reference row, and a sentinel row
  proves the reference ran before any other row is graded. Three verdict rows then run
  `read_conf_key_gaps` over a fixture conf. Its header comment states what it does not check.
  Observed by AC1, AC2, AC3 and AC4.
- **S4** — `memory/map/generated/symbols.json` is regenerated for the two new functions, and both
  names lead with a declared lexicon verb. Observed by AC6.

## 3. Non-goals (OUT)

- The process-monitor kit's line readers in `tools/process-monitor/reap.py` and
  `tools/process-monitor/classify.py`. They refuse a legal commented spelling rather than misread
  it; whether this unit takes them is F2.
- Every other kit's conf reader. `TOOL-aRepatriatedFork-38` brought each one it found to the rule
  and pinned each with an arm in its own suite.
- The bytes of `tools/memory-tree/tree_lib.py`. The probe in §4 measured `parse_conf_line` agreeing
  with bash on every legal row of the table, so the memory-tree kit moves no byte and owes no bump.
- Shell grammar beyond the table, as `parse_conf_line`'s own docstring rules out. A `K=<x>` that
  bash reads as a redirect and a `K= word` that bash runs as a command are not conf spellings.
- `KIT_GOVKIT_VERSION`. `tools/govkit/registry.toml` exempts govkit as "never installed into a
  target", so it ships no bytes and no carrier is owed a bump.
- A new gate leg. The arm lives in the existing `govkit selftest` leg (shared invariant 5).
- Reporting the VALUE govkit read. `read_conf_key_gaps` reports gap states only, and this unit
  keeps that contract.

### Edges

- **consumes-from** external — the bash rule `TOOL-aRepatriatedFork-38` landed in
  `parse_conf_line`, which the arm reads as the second reader.
- **hands-off** external — the process-monitor readers named above, unless F2 adopts them.
- **hands-off** external — the whole `govkit selftest` suite verdict, which the owner runs by hand
  from the merged tree (owner ruling of 2026-10-06, quoted in the brief).

## 4. Design

### Evidence

Probe of 2026-10-07 on node `a` at `e1f4d8c0`, a scratch script feeding each line to bash
(`set -a; . ./c`), to `parse_conf_line`, and to `read_conf_key_gaps` with the key declared
required. PINNED measurement; S3's arm re-derives it on every run.

| Line | bash | `parse_conf_line` | govkit gap today | bash implies |
|---|---|---|---|---|
| `K='--no-verify'` | `--no-verify` | `--no-verify` | none | none |
| `K="--no-verify"   # the flag the lander bans` | `--no-verify` | `--no-verify` | none | none |
| `K='--no-verify'   # note` | `--no-verify` | `--no-verify` | none | none |
| `K="<your-tool>"   # fill me` | `<your-tool>` | `<your-tool>` | none | placeholder |
| `K=""   # left blank` | empty | empty | none | empty |
| `K=   # note` | empty | empty | none | empty |
| `K=plain   # note` | `plain` | `plain` | none | none |
| `K=#x` | `#x` | `#x` | none | none |
| `K="a # b"` | `a # b` | `a # b` | none | none |
| `export K="TOOL DEPL"` | `TOOL DEPL` | `TOOL DEPL` | none | none |
| `K=plain` | `plain` | `plain` | none | none |

Three rows disagree, and all three are a MISSED gap. The brief's two `BYPASS_BAN` spellings change
no verdict, because govkit prints no value: the defect is visible only where the shell's value is
empty or a placeholder. Unit 40 recorded the same on 2026-10-06 over `A=""   # x` and
`B="<flag>"   # y`. A fourth line, the unquoted `K=<your-tool>   # fill me`, is a redirect to bash
and leaves K unset, so it is excluded from the table rather than graded.

The probe's first run printed `<UNSET>` for every row. A bare `bash` argv from Windows Python
resolved to the WSL launcher, whose `pwd` printed `/mnt/c/...`. That is the documented class
`memory/gotchas/subprocess-resolves-a-different-shell.md`, and it is why S3 resolves bash through
`resolve_shell_argv` and grades a sentinel before trusting the reference.

### Reader census in govkit

`git grep` over `tools/govkit/` for `CONF_KEY_RX`, `partition("=")`, `split("=", 1)` and a
`KEY=` regex found ONE reader of a kit conf's values: `read_conf_key_gaps`, called from `check`
and from `update`. Near misses, none of them a conf value reader:

- `build_policy_re` decides whether a shipped line ASSIGNS a policy key and reads no value; its
  quoted and commented spellings are pinned by `TOOL-dThriftyLanding-10`'s arms.
- The selfcheck scrape near `_resolve_vars` reads a gate SCRIPT's variable aliases, not a conf.
- The `KIT_RUN_GATES_VERSION` search reads the runner script's version line.
- `leg_words` reads the install receipt, which is JSON.

`tools/govkit/census.py`, `matrix.py`, `refusal_join.py` and `check_runbook_parity.py` read no conf.

### The reader

`parse_conf_assignment` matches `CONF_KEY_RX`, then decides the value on the text right after `=`,
in `parse_conf_line`'s order: leading whitespace gives the empty value; a quote opens a value that
ends at the next matching quote; otherwise a `#` preceded by whitespace cuts the value. An
unterminated quote falls through to the unquoted scan, as `parse_conf_line` does.
`read_conf_key_gaps` keeps its gap states, its unreadable-conf pair and its last-assignment-wins
rule, and calls the helper in its line loop in place of the two-line peel.

### The arm

`check_conf_reader_parity(tmp)` holds the legal rows of the Evidence table as data. For each
row it writes the line to a fixture file under `tmp` and reads bash's value with
`set -a; . ./c; printf '%s' "${K-<UNSET>}"`, the argv passed through
`govkit_module().resolve_shell_argv` at call time. The sentinel row `K=plain` must read `plain`
from bash first; otherwise the arm records one `FAIL` naming the argv it ran and grades nothing
against a dead reference. Each graded row is one `check()` line naming the spelling, and a
disagreement prints all three values. The verdict rows write
`KEEPALIVE_CREATE="<your-schedule-create-tool>"   # fill me`, `BYPASS_BAN=""   # left blank` and
`LANDER=   # note` into one fixture conf and assert `read_conf_key_gaps` returns `placeholder`,
`empty` and `empty`. A final `check()` asserts the graded row count equals the table's length.

Its header says what it does not check: spellings outside the table, the `check` and `update`
verbs end to end (their arms already cover the gap wording), and any reader outside govkit and the
memory-tree kit.

### Inventory

- `parse_conf_assignment` in `tools/govkit/govkit.py`, cell `py.function`; the lexicon answered OK
  on 2026-10-07.
- `check_conf_reader_parity` in `tools/govkit/selftest.py`, cell `py.function`; the lexicon
  answered OK on 2026-10-07.

Both are symbol-tier names that feed `memory/map/generated/symbols.json` and never the coverage
ratchet, so no dossier key is minted. No conf key, leg or file is minted.

### Rollout

Edit `govkit.py`, then the arm, then observe the arm red on the staged break of AC2, then run
`python tools/codebase-map/gen_map.py --write` last, since it reads the finished functions.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

Option (b) of F1 is weighed there, with the fixture observation that costs it.

## 5. Production-readiness checklist

- security — N/A: a read-only parser of a file the target owns; no write path moves.
- perf / scale — the arm spawns one bash per row plus the sentinel. At the measured cost of a spawn
  on node `a` that is seconds, and it runs in a suite that is not on the bar.
- error / empty / loading states — an unreadable conf still returns its one `unreadable` pair; an
  unterminated quote reads as the unquoted scan does; a dead bash reference is a `FAIL`, never a
  skip that reads green.
- observability — each row prints its own `ok` or `FAIL` line naming the spelling and the values.
- risks — `TOOL-aReapedSpinner-18` records the whole govkit selftest red on main for unrelated
  assertions, so this unit's evidence is the slice, never a whole-suite exit.
- testing — the arm of S3, observed red on the prior peel (AC2) and on a dead reference (AC4).
- migration — N/A: no stored format moves; a conf that read correctly before reads identically.
- user docs — N/A: no `help/` page covers govkit's internal gap reader.

## 6. Acceptance criteria

- **AC1** — When the arm runs as a slice, it prints one `ok` line per table row naming the
  spelling, the row-count `ok` line, and `FAILURES []`. The slice:
  `python -c "import sys,pathlib,tempfile as t; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_conf_reader_parity(pathlib.Path(t.mkdtemp(prefix='g46-'))); print('FAILURES', s.FAILURES)"`
  Red when: any row's `parse_conf_assignment` or `parse_conf_line` value differs from bash's, or
  fewer rows are graded than the table holds.
  cost: about 45 s, most of it the import of the govkit selftest module (UNVERIFIED for this arm).
  fixture: the temp root is a fixture directory under `%TEMP%`, never the scratchpad, whose path
  length false-reds other govkit arms.
  figure: the row count is DERIVED from the table's length at run time.
- **AC2** — When `parse_conf_assignment`'s value rule is set back to the prior one-layer peel, the
  `v[0] == v[-1]` test from `read_conf_key_gaps` at `e1f4d8c0`, with `tools/govkit/govkit.py`
  saved to the run's scratchpad first and restored from it after, AC1's slice prints `FAIL` lines
  naming `K="<your-tool>"   # fill me`, `K=""   # left blank` and `K=   # note`.
  Red when: the slice stays green on the prior peel, which is the shipped body and not a synthetic
  value.
- **AC3** — When AC1's slice runs, its verdict rows print `ok` for `read_conf_key_gaps` returning
  `placeholder` for `KEEPALIVE_CREATE`, `empty` for `BYPASS_BAN` and `empty` for `LANDER`.
  Red when: any of the three reads as no gap, the behaviour the Evidence table pins at `e1f4d8c0`.
- **AC4** — When AC1's slice runs with `s.govkit_module().resolve_shell_argv = lambda a:
  ['g46-no-such-bash'] + a[1:]` set before the call, the arm prints one `FAIL` naming the dead
  bash reference and the argv it tried, and prints no row `ok` line.
  Red when: a row reports agreement with no bash value behind it.
- **AC5** — When `grep -n "keeps any trailing comment" tools/govkit/govkit.py` runs it prints
  nothing, and the docstring of `read_conf_key_gaps` names `parse_conf_assignment` and the
  unterminated quote, escaped quote and adjacent concatenation it does not read.
  Red when: the docstring still states the one-layer peel or omits its limits.
- **AC6** — When `python tools/codebase-map/gen_map.py --check` runs after the regeneration it
  exits 0, and `python tools/lexicon/lexicon.py --suggest parse_conf_assignment --as py.function`
  and the same for `check_conf_reader_parity` each print `OK`.
  Red when: `memory/map/generated/symbols.json` is stale or either name leads with an undeclared
  verb.

## 7. Gates

The close runs these once, after the last unit is terminal. No pass runs them.

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: `tools/govkit/selftest.py` · covers AC1 AC2 AC3 AC4 · `check_conf_reader_parity` on the prior one-layer peel and on a dead bash reference · none

## 8. Open questions

- **F1 — One derivation, or a pinned copy?** The brief allows either.
  - (a) A copy plus an arm. govkit carries `parse_conf_assignment` following `parse_conf_line`'s
    rule, and S3's arm pins the two to bash, so a drift between the copies reds instead of hiding.
  - (b) One derivation. govkit loads `parse_conf_line` from gov's own memory-tree home through
    `resolve_kit_dir`, the way selfcheck already loads `check-arms.py`. The reason
    `TOOL-aRepatriatedFork-38` rejected a shared reader does not bind govkit, which the registry
    says is never installed into a target. The cost is measured: `build_gov17` in
    `tools/govkit/selftest.py` builds its scratch gov from `govkit.py`, `adopters.toml` and
    `registry.toml` alone, so every `check` and `update` arm run there would find no reader. (b)
    therefore also owes memory-tree in that fixture, a refusal when the home does not resolve, and
    the same bash arm.
  - Recommendation: (a). It is the smaller diff and adds no runtime dependency to `check` or
    `update`. The §2 scope above is written for (a); choosing (b) rewrites S1 and §4 "The reader".
  RESOLVED (agent, 2026-10-07, delegated): (a). Option (b) fails AC1 and AC2 as written, which
  grade a govkit-owned `parse_conf_assignment`, so M3's first veto removes it.
- **F2 — Does this unit also take the process-monitor kit's line readers?** `run_sweep` in
  `tools/process-monitor/reap.py` and `main` in `tools/process-monitor/classify.py` read
  `PROCMON_AGE_CEILING`, `PROCMON_SPIN_RATE` and `PROCMON_REAP_MODE` by a `startswith` match and a
  bare quote strip. Probe of 2026-10-07: `PROCMON_AGE_CEILING="14400"   # four hours` raises
  `ValueError`, which both callers print as `REFUSED`. An `export ` prefix leaves the key unread.
  Both fail closed, so nothing is misread silently, but a spelling the shell accepts is refused.
  - (a) Leave it to a separate unit in that kit, with its own version bump and suite arm.
  - (b) Fold it in here. That widens this Tier-1 unit's write set to a shipped kit and owes that
    kit's version bump in every carrier.
  - Recommendation: (a). One mechanism per spec, and the class here is govkit's reader.
  RESOLVED (agent, 2026-10-07, delegated): (a). Option (b) is a second mechanism in one spec,
  which M2's one-mechanism rule refuses, and it widens a Tier-1 write set to a shipped kit, which
  M3's third veto removes. The readers stay handed off as §3 states.

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft, from the owner's adoption of 2026-10-07 and the unit's brief.
- rev-2 · 2026-10-07 · AC1's cost line no longer backticks the selftest file, which the spec-token bar join read as a suite cited as the observation; the slice itself is unchanged.
- rev-3 · 2026-10-07 · node a · §8: the build pass resolved both forks under the run's delegation,
  F1 (a) and F2 (a), each by its own recommendation. No scope, design or criterion moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a kit conf value the way the shell that sources
it does"` ranked `load_conf` across the kit readers and `parse_conf` in
`tools/memory-tree/tree_lib.py`. The seam reused is the rule in `parse_conf_line`, which
`TOOL-aRepatriatedFork-38` copied into every kit reader and which S1 copies into govkit; F1 asks
whether to import it instead. The recall probe returned `TOOL-aRepatriatedFork-38` (the class
fixed in every kit reader it found, govkit not among them), `TOOL-aScouredKit-28` (the
quoted-plus-comment spelling in two readers) and `TOOL-dThriftyLanding-10` (govkit's policy
predicate, a near miss).
`gotchas.py --for-paths` over the two govkit files selected
`staged-break-substitutes-a-synthetic-value`, which AC2 answers by staging the shipped prior body,
and `a-new-local-collides-in-a-long-function`, which S3 answers by a module-level function.

Recall terms used: `python tools/memory-recall/query.py "how should a python reader of a sourced
kit conf handle a quoted value followed by an inline comment" --terms "parse_conf_line conf reader
quoted value inline comment bash sourcing semantics govkit read_conf_key_gaps load_conf
aRepatriatedFork-38 two readers re-derived"`.
