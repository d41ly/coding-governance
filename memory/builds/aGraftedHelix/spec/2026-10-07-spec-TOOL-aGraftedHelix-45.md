# TOOL-aGraftedHelix-45 — a leg bans a location probe asked from a moved directory unless it scrubs an inherited GIT_DIR or a registry row waives it

**Status:** CLOSED · rev-3 · 2026-10-07 · node a · Tier-2 · base e1f4d8c0 · streams tooling+kickoff · order 26 · ratified 2026-10-07

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-45-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-45-1-acceptance-ledger.md) | journal | — |
| [2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md](../prompts/2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md) | journal | TOOL-aGraftedHelix-46 TOOL-aGraftedHelix-47 |

<!-- /gen:spec-records -->

## 1. Goal

With `GIT_DIR` set and no `GIT_WORK_TREE`, git takes the current directory for the top of the work
tree. So a shell probe that moves into a directory and asks `rev-parse --show-*` answers about that
directory as if it were the root. Git exports `GIT_DIR` into a linked worktree's hooks and merge
drivers, so each such probe is correct in a shell and silently wrong under one. The owner ruled on
2026-10-07 to gate the class by its spelling. Every probe in shipped shell either opens its
substitution with the scrub the two `tools/workflows/` gates already use, or carries a registry row
whose reason the leg prints. Reachability is not decided, because unit 27 measured that no line
predicate can decide it.

## 2. Scope (IN)

- **S1** — `tools/gate-lint/sh_hygiene.py` gains a `--location-probes` mode. Its population is every
  tracked `*.sh`, plus every tracked extensionless file whose first line is a shell shebang, filtered
  by the pathspecs its arguments carry. It grades the probe spellings §8 F2 settles, with the `-C`
  operand read as any shell word, a quoted command substitution included. A site is scrubbed only
  when the innermost `$(` or `(` holding it opens with `unset GIT_DIR GIT_WORK_TREE;`. Comment text
  is cut by the existing `extract_code`, so a comment never grades. Observed by AC2 and AC3.
- **S2** — The mode reads an optional registry with the existing four-field grammar,
  `<path> TAB <key> TAB <count> TAB <reason>`, compared in both directions by the existing
  `check_registry`. The key is the probe's form, operand and flag as written, never a line number.
  A waived site prints its reason on every run, green included. Observed by AC1 and AC3.
- **S3** — Every run prints the scanned file count, the gated count, the scrubbed count and three
  near-miss counts that are reported and not gated. A hit names its path, line and key, and prints
  the scrubbed spelling as the remedy. A failed `git ls-files` and an empty population each refuse
  with exit 2, as the sibling scan does. Observed by AC2 and AC3.
- **S4** — `run_selftest` gains one arm per row of §4's fixture table, and `FLOOR_ASSERTIONS`
  rises by exactly the arms added. Observed by AC1.
- **S5** — The leg, homed as §8 F1 settles. It needs a `tools/gate-legs.json` row carrying gov's
  arguments and a `[[gate_leg]]` block in `tools/gate-lint/kit.toml`. The gate-lint dossier lists the
  leg's name under `gate-legs`, with the generated map refreshed. A header-only registry under
  `memory/project/` is named in `PROJECT_REGISTRY_EXTRA` in `.memory-tree.conf`.
  Observed by AC2, AC8 and AC9. The row's `:!*.test.sh` exclusion ends like a suite path, and
  `tools/check-testsuite-counts.sh` selects every quoted manifest string ending in `.test.sh`, so it
  refused the row as naming a suite it cannot read. Its selector skips a string opening with `:`,
  which is a git pathspec and never a file, and its self-test gains the arm that pins that, with its
  floor raised by the two assertions the arm adds.
- **S6** — Every bare site in the population is scrubbed in place, one token per line, so no line
  moves. The one exception is `read_settle_command` in `tools/unattended/unattended.sh`. It
  calls `derive_self_rel`, which unit 27 made the answer to the same question for its sibling probe
  in the same file. Observed by AC2, AC4, AC5 and AC10.
- **S7** — The class record `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`
  rewrites its "Its gate" section to name the leg as the class's gate, and rewrites "The probes
  left, and why" to say what the leg leaves. It gains the scanner's path, so a diff touching the
  scanner selects it. Observed by AC6.
- **S8** — Each kit whose shipped bytes move bumps its version once, last, in every carrier
  `tools/check-kit-versions.sh` pairs. The unattended renders are re-adopted. The kickoff
  manifest is re-stamped, because the pass edits files its `watch:` line names. Observed by AC7.
- **S9** — `tools/gate-lint/README.md` documents the mode, the class and the registry. Its
  sentence that states how many legs the kit declares is reworded to name the legs without a count,
  and so are the two sentences in `tools/gate-lint/kit.toml` and the one in the gate-lint dossier
  that count the kit's legs. The leg's subject is pinned in `tools/govkit/subject-pins.tsv` by
  `govkit.py selfcheck --write`, which reds an unpinned leg. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- No reachability analysis. Whether a hook, a merge driver or a submodule operation can run a
  probe is a question about callers, which no line predicate answers (unit 27, §4).
- No `*.test.sh` in the population. The predicate the owner adopted excludes them. A suite runs
  under the pre-push bar, and `.githooks/pre-push` already scrubs `GIT_DIR` for every leg.
- No `memory/` records in gov's population. A build record is frozen once it lands, so a gate
  cannot ask its author to edit it.
- No Python or JavaScript callers, unless §8 F3 adopts them.
- No probe that asks for the git dir or the common dir. From inside the same repository an
  inherited `GIT_DIR` answers those correctly, and only a probe into another repository answers
  wrong, which a spelling cannot tell apart. The identity count is printed as a near-miss.
- No gate on `rev-parse --show-*` asked with no directory move. It asks the caller's directory,
  which is the top of the work tree under every hook git runs. It is printed as a near-miss.
- No process-wide unset of `GIT_DIR`. The class record forbids it, and the scrub recognizer grades
  an `unset` outside the probe's own substitution as bare.
- No edit to the charter template, `memory/guides/REVIEW-PROTOCOL.md` or the method guide beyond
  version marker lines (shared invariant 10).

### Edges

- **consumes-from** external — git exporting an absolute `GIT_DIR` into a linked worktree's hooks
  and merge drivers, measured by unit 27 on git 2.54.0.windows.1 and again here on 2026-10-07. Also
  the inline copy of `derive_self_rel` that unit 27 put in `tools/unattended/lib-unattended.sh`,
  which the settle-command fix calls. This unit builds neither.
- **hands-off** external — under §8 F3 (a), the Python location probes §4 lists, for the owner to
  adopt as a unit of their own or leave. One of them is the deferred ask `TOOL-aCollapsedScan-8`.

## 4. Design

### The population, measured

Measured on node `a`, 2026-10-07, at `03a0956c`, PINNED. The brief's predicate, as unit 27 ran it,
printed 25 lines. Two are comments, in `tools/check-kit-versions.sh` and
`tools/unattended/adopt-unattended.sh`. Two are scrubbed, in `tools/workflows/check-review-join.sh`
and `tools/workflows/check-verifier-fanout.sh`. That leaves 21 bare code lines, where unit 27's
count left 20. The extra one is `read_settle_command`, added by `e63806aa` for
`TOOL-dUnstuckLanding-14` on another lineage and merged in at `1e027341`. A new instance arrived
after the class was measured, which is the case for a gate.

The brief's operand, `-C +[^ ]+`, cannot read a quoted word holding a space. It misses
`tools/run-gates/run-selftests.sh` lines 44 and 53, whose operand is `"$(dirname -- "$0")"` and
`"$(dirname -- "$HERE")"`. With the operand read as a shell word the `-C` spelling has 23 bare
sites, and that widening is a predicate fix rather than a scope choice.

The `cd <dir> && git rev-parse --show-*` spelling has 11 bare sites in seven files, six of which
hold no `-C` site. Its failure is the same one, measured here with `GIT_DIR` exported to this
worktree's absolute git dir:

| probe from the worktree root, into `tools/unattended` | shell | `GIT_DIR` exported | scrubbed under export |
|---|---|---|---|
| `git -C tools/unattended rev-parse --show-prefix` | `tools/unattended/` | empty | `tools/unattended/` |
| `cd tools/unattended && git rev-parse --show-prefix` | `tools/unattended/` | empty | `tools/unattended/` |

One `cd` site is live in a file whose other probe the brief counts as scrubbed.
`tools/workflows/check-review-join.sh` line 62 derives its population prefix by the `cd` spelling.
Run with the export, its clean line named `the repository root` as its population, where a shell
run named `tools/ or .claude/workflows/`. Its own suite's L1 arm exports `GIT_DIR` over a fixture
holding only `.claude/workflows/` files, where both populations are the same, so that arm cannot
see the widening. That is read from the suite, not run.

Two `-C` sites were observed failing the same way:

| site | shell | `GIT_DIR` exported |
|---|---|---|
| `bash tools/check-kit-versions.sh` | exit 0 | exit 1, `2 problem(s)`, a `settings-merge.py` marker unreadable |
| `read_settle_command s`, from a scratch file over the library | `bash tools/unattended/unattended.sh --settle s` | `bash unattended.sh --settle s` |

No site reads `GIT_DIR` on purpose. Over the files holding a bare site, only
`tools/unattended/unattended.sh` and `tools/workflows/check-review-join.sh` spell it, the first in
the env list of its injected-config tripwire and a comment, the second in the scrub itself. So every
site is scrubbable, the registry ships with no row, and no waiver is planned.

### Near-misses, printed and not gated

Measured at `03a0956c` over gov's population of 57 files, PINNED, and DERIVED again on every run:

| near-miss | count | why it is not gated |
|---|---|---|
| `-C <dir> rev-parse` asking `--git-dir`, `--git-common-dir` or `--absolute-git-dir` | 7 | §3; five copies of the health-log appender and the two identity probes in `tools/unattended/adopt-unattended.sh` |
| `rev-parse --show-*` with no `-C` and no `cd` before it on the line | 38 | §3; it asks the caller's directory |
| a comment carrying the spelling | 2 | a comment never runs |

The population rule was measured too. The tracked tree holds four extensionless files, and all four
are `.githooks/commit-msg`, `pre-commit`, `pre-push` and `pre-rebase`, each with a bash shebang. The
shebang rule reaches them without the scanner naming `.githooks`, which keeps the kit free of a
literal outside itself. The brief's `'.githooks/*'` pathspec also swept
`.githooks/pre_push_bar_selftest.py` into a shell scan, which the shebang rule does not.

### The mode

`main` branches on `--location-probes` before its positional parse. The arguments are
`[registry] [root] [pathspec...]`, so the sibling's grammar holds and the pathspecs extend it. Gov's
row passes the registry, `.`, and two exclusions: every `*.test.sh`, and the memory root. With no
registry argument the run grades an empty declaration and says so, the sibling's posture.

`scan_probe_tree` derives the population through one `git ls-files -z` with `cwd` at the root and
`encoding="utf-8"`. It keeps `*.sh`, and an extensionless path whose first line matches a sh, bash,
dash, ksh or zsh shebang. `scan_probe_file` reads each file's bytes, decodes them as UTF-8 with
`replace`, and runs each line's code half through two compiled patterns:

- the `-C` form: `git` or `GIT`, any `-c <k=v>` options, `-C <word>`, any options, `rev-parse`, any
  `--` flags, then `--show-prefix`, `--show-toplevel` or `--show-cdup`;
- the `cd` form: `cd <word>`, then `&&` or `;`, then the same `rev-parse` tail.

A `<word>` is a double-quoted string that may hold one level of `$( )`, a single-quoted string, or
an unquoted run. `check_probe_scrubbed` reads the code before the match and requires that it end in
`(` followed by `unset GIT_DIR GIT_WORK_TREE;` and whitespace. One spelling is accepted on
purpose: the other order, a third variable, or an `unset` earlier on the line at top level grade
bare. A false red names its remedy. A false pass would be silent.

`build_probe_measured` returns `{(path, key): count}` over the bare sites. `read_registry` and
`resolve_declaration` gain a key-shape parameter, the pattern with the two phrases a malformed key
is refused in, whose default is the existing `DELIMITER` and its phrases, so the sibling's behaviour
is byte-identical. They also take an optional dict that `read_registry` fills with each row's
reason, which is how a waived site's reason reaches the run. `check_registry` takes an optional map
of undeclared-site text per key, so a bare probe is reported in the probe's own words with each
site's line and remedy, and every other key keeps the loop text. The probe key shape is
`-C <word> --show-<x>` or `cd <word> --show-<x>`, which a line number cannot match.
`print_probe_populations` prints the counts in a fixed order, and `run_probe_scan` returns 0, 1 or 2
like `main`.

### Fixture table for the selftest arms

| case | verdict |
|---|---|
| `x=$(git -C "$d" rev-parse --show-prefix)` | bare hit |
| `x=$(GIT -C "$d" rev-parse --show-toplevel)` | bare hit |
| `x=$(git -C "$(dirname -- "$0")" rev-parse --show-prefix)` | bare hit, the quoted operand |
| `x=$(git -c a.b=c -C "$d" rev-parse --path-format=absolute --show-toplevel)` | bare hit |
| `x=$(cd "$d" && git rev-parse --show-prefix)` | bare hit under F2 (b), a near-miss under (a) |
| `x=$(unset GIT_DIR GIT_WORK_TREE; git -C "$d" rev-parse --show-toplevel)` | scrubbed |
| `x=$(unset GIT_DIR GIT_WORK_TREE; cd "$d" && git rev-parse --show-prefix)` | scrubbed |
| `unset GIT_DIR GIT_WORK_TREE; x=$(git -C "$d" rev-parse --show-prefix)` | bare hit, a top-level unset |
| `x=$(unset GIT_WORK_TREE GIT_DIR; git -C "$d" rev-parse --show-prefix)` | bare hit, the other order |
| `# x=$(git -C "$d" rev-parse --show-prefix)` | comment near-miss |
| `x=$(git -C "$d" rev-parse --git-common-dir)` | identity near-miss |
| `top=$(git rev-parse --show-toplevel)` | cwd near-miss |
| a registry row for case 1 with a reason | green, the reason printed |
| a row whose site is gone, a count that disagrees, a line-number key | each a finding |
| an extensionless file with a bash shebang, and one with a python shebang | scanned, not scanned |
| a `:!*.test.sh` pathspec over a suite holding case 1 | not scanned |
| a population of zero files, and a registry path that does not resolve | each exit 2 |

The arms build their trees with the selftest's existing `tempfile` pattern, so they run at any
install prefix.

### What the header states it does NOT check

Reachability. A probe split across a line continuation. A probe built in a variable, through
`eval`, or behind any wrapper but `GIT`. Python and JavaScript callers. Other subcommands run with
`-C` into a subdirectory, whose answers move the same way, such as `ls-files`. Quoting carried
across lines, the limit `extract_code` already states. A scrub that unsets the variables for a
whole function rather than inside the substitution. Each is a MISS, never a false red.

### Inventory

| identifier | where | cell |
|---|---|---|
| `--location-probes` | `tools/gate-lint/sh_hygiene.py`, a CLI flag | not graded |
| `scan_probe_tree` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `scan_probe_file` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `check_probe_scrubbed` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `build_probe_measured` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `print_probe_populations` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `run_probe_scan` | `tools/gate-lint/sh_hygiene.py` | `py.function` |
| `shell hygiene (a location probe asked from a moved directory)` | `tools/gate-legs.json` | map key, `gate-legs` |
| `location-probe-waivers.txt` | `memory/project/` and `PROJECT_REGISTRY_EXTRA` | registry file |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for all six names on
2026-10-07. The leg's name is the one new map key, listed in the gate-lint dossier beside its two
siblings.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/README.md`
- `tools/gate-lint/kit.toml`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `.memory-tree.conf`
- `memory/project/location-probe-waivers.txt`
- `memory/map/features/gate-lint.md`
- `memory/map/generated/`
- `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`
- `memory/gotchas/INDEX.md`
- `memory/guides/SESSION-KICKOFF.md`
- `skills/session-kickoff/manifest-check.sh`
- `tools/check-agent-cap-restatement.sh`
- `tools/check-dead-paths.sh`
- `tools/check-hook-destinations.sh`
- `tools/check-install-prefix.sh`
- `tools/check-kit-versions.sh`
- `tools/check-line-length.sh`
- `tools/check-playbook-parity.sh`
- `tools/check-testsuite-counts.sh`
- `tools/check-testsuite-counts.test.sh`
- `tools/drift-audit/adopt-drift-audit.sh`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/process-monitor/adopt-process-monitor.sh`
- `tools/run-gates/run-selftests.sh`
- `tools/unattended/resume-tick.sh`
- `tools/unattended/run-unattended-gates.sh`
- `tools/unattended/unattended.sh`
- `tools/lexicon/adopt-lexicon.sh`
- `tools/memory-recall/adopt-memory-recall.sh`
- `tools/run-gates/adopt-run-gates.sh`
- `tools/run-gates/run-gates.sh`
- `tools/runlog/adopt-runlog.sh`
- `tools/workflows/check-review-join.sh`

The last six carry only `cd`-form sites, so under §8 F2 (a) they leave the estimate. The version
bumps also move the marker on every carrier `tools/check-kit-versions.sh` pairs for each moved kit,
the method guide's marker line included. Which kits move is DERIVED by `govkit.py epoch` at the
pass. The estimate today is the kickoff engine, drift-audit, memory-tree, process-monitor,
run-gates, unattended and the versioned tool-root entries, plus lexicon, memory-recall, runlog and
workflows under F2 (b). The gate-lint kit declares no version constant.

### Rollout

1. Write the arms first and observe the new ones red against the parent's scanner run as a scratch
   copy, then write the mode until `--selftest` is green.
2. Run the mode over a clone of the parent and keep its list of bare sites as the scrub worklist.
3. Scrub every site in place, and fix `read_settle_command` through `derive_self_rel`. Re-run the
   mode until it prints no bare site.
4. Add the leg row, the `[[gate_leg]]` block, the registry and its conf token. List the leg in the
   dossier, then run `gen_map.py --write`.
5. Rewrite the class record, then run `gotchas.py --write`.
6. Bump each moved kit's version once, last, re-adopt the unattended renders, and re-stamp the
   kickoff manifest with a delta line in the commit message.

### Alternatives rejected

- **Gate reachability instead of spelling.** Unit 27 measured 26 probe lines at `f0971667` that
  differ only in whether a hook can reach them. A predicate over the line cannot change between a
  reachable site and an unreachable one, so it cannot discriminate, which M12 refuses.
- **Scrub the environment once in each hook.** Unit 27 rejected it: adopters wire their own hooks,
  and `commit-msg` must keep `GIT_INDEX_FILE`, which named a `next-index` lock file on a partial
  commit while another path stayed staged.
- **The brief's operand pattern.** Measured above: it misses two live sites in
  `tools/run-gates/run-selftests.sh`.
- **A `git grep` predicate in a new shell script.** Measured above: it matched 2 comment lines of
  25, because it cannot cut a comment the way `extract_code` does. A shell script is also a new
  kit file for the arms floor to grade.
- **A line-keyed registry.** The sibling scanner refuses one, and `TOOL-dSpentCeiling-6` records
  two registries that redded on unrelated edits for exactly that reason.
- **The `.githooks/*` pathspec.** It names gov's own convention inside a shipped kit, and it swept a
  Python file into a shell scan. The shebang rule reached the same four hooks.

## 5. Production-readiness checklist

- security — The scrub narrows nothing and widens nothing. Inside one substitution it makes git
  discover the repository from the probed directory, which is what a shell run already does. No
  write path is added, and the registry is read-only data the leg prints.
- perf / scale — The sibling scan read every tracked `*.sh` in 1.5 s on node `a`, 2026-10-07. The
  mode reads 57 files, and its declared ceiling is the sibling's 300 s. Each scrub adds no process,
  because `unset` is a builtin inside a subshell the substitution already forks.
- error / empty / loading states — A failed `git ls-files` and an empty population refuse with exit
  2. A registry argument that does not resolve refuses. No registry argument grades an empty
  declaration and says so.
- observability — Every run prints the scanned, gated and scrubbed counts and the three near-miss
  counts. A hit prints path, line, key and the remedy. A waived site prints its reason on green runs.
- risks — Roughly eleven kits bump a version in one pass, and the epoch check is what proves none
  was missed. The kickoff manifest stamp is owed, because the pass touches watched files. The
  scrubs keep every line in place, so no line-keyed registry moves.
- testing — The selftest arms observe each fixture row, and the new ones are seen red first. The
  mode is observed red over a parent clone and over a reverted site, and green over the pass.
- migration — None. The leg is additive, and an adopter of gate-lint receives a mode its own
  manifest has not wired.
- user docs — `tools/gate-lint/README.md` documents the mode. The class record is the operator
  note.

## 6. Acceptance criteria

A clone is `git clone --local` of the named commit under a short directory in %TEMP%. The mode's
arguments are the ones the new manifest row declares unless a criterion says otherwise.

- **AC1** — When `python tools/gate-lint/sh_hygiene.py --selftest` runs at the pass commit, it
  exits 0, every arm of §4's fixture table prints its verdict, and the printed assertion count is at
  least the raised `FLOOR_ASSERTIONS`. Red when: a scratch copy of the scanner whose scrub check
  accepts an `unset` anywhere earlier on the line is run the same way. The top-level-unset arm then
  fails and the exit is 1.
  figure: the floor is DERIVED, the parent's value plus the arms the pass adds.
- **AC2** — When `python tools/gate-lint/sh_hygiene.py --location-probes` runs at the pass commit's
  root, it exits 0, prints no bare site, and prints the scrubbed count and each near-miss count. Run
  with the same scanner over a clone of the pass's parent and an empty scratch registry, it exits 1
  and lists every bare site §4 counts. Red when: the parent run exits 0, which would mean the
  predicate matched none of the sites it was written for.
  figure: §4's 23 and 11 are PINNED at `03a0956c`, and the counts at observation are DERIVED.
- **AC3** — When the quoted-substitution operand at line 44 of the run-gates kit's selftest runner
  is reverted to the bare spelling in a clone of the pass commit,
  `python tools/gate-lint/sh_hygiene.py --location-probes` over that clone exits 1. It names that
  path and line and prints the scrubbed spelling. With a scratch registry holding a row for that key and a
  reason, it exits 0 and prints the reason. With that row kept and the site scrubbed again, it exits
  1 naming the stale row. Red when: the operand is read as one unquoted word, as the brief's
  pattern reads it, so the reverted site goes unreported and the first run exits 0.
- **AC4** — When `GIT_DIR` is exported to this worktree's absolute git dir and
  `bash tools/check-kit-versions.sh` runs from the repository root at the pass commit, it exits 0,
  as it does without the export. Red when: its probe is bare. At the parent the exported run exits 1
  with `2 problem(s)`, as measured on 2026-10-07.
- **AC5** — When the same export precedes `bash tools/workflows/check-review-join.sh` at the pass
  commit, its clean line names `tools/ or .claude/workflows/` as its population, as a shell run does.
  This criterion stands under §8 F2 (b) or (c). Red when: its `cd` probe is bare, and the exported
  run names `the repository root`, as it did at the parent on 2026-10-07.
- **AC6** — When `python tools/memory-tree/gotchas.py --check` runs at the pass commit, it exits 0.
  `grep -c 'a location probe asked from a moved directory'` over
  `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md` prints at least 1, and
  `python tools/memory-tree/gotchas.py --for-paths tools/gate-lint/sh_hygiene.py` lists the record.
  Red when: the record still says the class has no machine gate, or names no backticked scanner
  path, so no derived anchor reaches it.
- **AC7** — When `python tools/govkit/govkit.py epoch --base <the parent>` runs at the pass commit,
  it names no kit whose shipped bytes moved without its version. `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py selfcheck`, `bash tools/unattended/adopt-unattended.sh --check` and
  `bash skills/session-kickoff/manifest-check.sh` each exit 0. Red when: a scrubbed kit moved and its
  version did not, or a watched file moved and the manifest was not re-stamped.
  figure: the kit set is DERIVED by epoch at observation.
- **AC8** — When `python tools/codebase-map/gen_map.py --check` runs at the pass commit, it exits 0,
  and `python tools/codebase-map/test_codebase_map.py` passes. `grep -c -- '--location-probes'`
  over `tools/gate-lint/README.md` prints at least 1. Red when: the manifest gains the row while the
  gate-lint dossier lists no such name, which the coverage test reports as an unlisted key.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the pass commit, it prints
  no check 3 finding. Red when: the registry lands under `memory/project/` and the conf token does
  not, so check 3 names the file.
  cost: the hygiene script's full run, minutes on node `a`.
- **AC10** — When a scratch script sources `tools/unattended/lib-unattended.sh`, sets `KIT_DIR` to
  the kit directory, and evaluates the `read_settle_command` definition that `sed` extracts from
  `tools/unattended/unattended.sh`, it prints `bash tools/unattended/unattended.sh --settle s` with and
  without `GIT_DIR` exported. Red when: the probe is bare. At the parent the exported run printed
  `bash unattended.sh --settle s` on 2026-10-07.

## 7. Gates

`shell hygiene (a loop fed by a command substitution)` · `shell-hygiene selftest` · `encoding posture (text IO names its encoding)` · `memory hygiene` · `gotchas selftest` · `kickoff-manifest ratchet` · `manifest-check self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `govkit selfcheck` · `govkit acceptance matrix` · `install-prefix (shipped surface)` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `dead-path carriers (deleted files still named)` · `agent-cap restatement` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `line-length gate selftest` · `playbook parity selftest` · `lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `drift-audit selftest` · `drift-audit wiring` · `process-monitor adopter selftest` · `process-monitor wiring` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `pre-push run-log line` · `run-selftests self-test` · `run-gates wiring` · `runlog selftest` · `runlog skill wiring` · `memory-recall skill wiring` · `recall floor` · `recall floor arms` · `review-join self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `unattended skill wiring` · `scratch-guard self-test` · `straggler-guard arms` · `transition-audit arms` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)`

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC1 · a scratch copy whose scrub check accepts an earlier top-level unset · FLOOR_ASSERTIONS rises by the arms added
New arm: tools/gate-lint/sh_hygiene.py --location-probes, as the new manifest row · covers AC2 AC3 · one site reverted to the bare spelling in a clone of the pass commit · none

The new leg is not on the line above because it does not exist until the pass adds it. The close
runs the bar once, and the kit suites stay the owner's manual run (owner ruling of 2026-10-06).

## 8. Open questions

- **F1 — Where does the gate live?**
  (a) A `--location-probes` mode in `tools/gate-lint/sh_hygiene.py`, on a new leg row of its own,
  with its arms in the existing `--selftest` and so on the existing `shell-hygiene selftest` leg.
  It costs one manifest row, one `[[gate_leg]]` block and one dossier line, and it reuses the
  sibling's comment cutter, registry reader and registry compare.
  (b) A second class inside the existing `shell hygiene (a loop fed by a command substitution)`
  leg. The leg's name then states one class of two, so it is renamed in the manifest, the kit
  descriptor, the dossier and the README, and the timing history keyed on the old name is lost. One
  run would also need two populations, since the loop class grades every suite and this one
  excludes them. The registry file's name and its delimiter key would carry a second kind of row.
  (c) A new script in the gate-lint kit with its own scan leg and its own selftest leg, either
  copying the registry machinery or importing it across files. That is two new legs.
  Recommendation: (a). It is a check inside an existing gate script, which is the cheaper unit the
  new-leg gotcha prices, and it is the only option that adds one leg and renames none. Under (b) or
  (c), a rev bump re-cuts S5, AC2 and AC8.
  RESOLVED (agent, 2026-10-07, delegated): (a). All three satisfy the same criteria; (a) adds one
  leg, renames none and reuses the sibling's cutter and registry pair, which M3's tie-break prefers.
- **F2 — Which spellings does the ban cover?**
  (a) The `-C` spelling only, with the operand read as a shell word: 23 bare sites in 16 files. The
  `cd` spelling is printed as a fourth near-miss count.
  (b) Both the `-C` spelling and `cd <dir> && git rev-parse --show-*`: 34 bare sites in 22 files.
  It adds the lexicon, memory-recall, runlog and workflows kits to the version bumps.
  (c) Option (b) plus the 7 identity probes asking `--git-common-dir`. Five are copies of the
  health-log appender under a parity gate.
  Recommendation: (b). The `cd` spelling fails identically, as §4 measured, and one instance is live
  in `tools/workflows/check-review-join.sh`, whose other probe the brief counts as scrubbed. Option (c)
  gates a probe that answers correctly from inside its own repository, so most of its hits would be
  scrubbed for no defect. Under (a), a rev bump drops AC5 and moves the `cd` row of §4's fixture
  table to the near-miss column.
  RESOLVED (agent, 2026-10-07, delegated): (b). It is the most feature-rich survivor, keeping AC5;
  (c) is vetoed by §3's non-goal on probes that ask for the git dir or the common dir.
- **F3 — Are the Python callers in this unit?** Measured at `03a0956c`, seven Python sites ask
  `git -C <dir> rev-parse --show-toplevel`, or run it with `cwd=` at a subdirectory. They are
  `tools/lexicon/lexicon.py` line 4347, `tools/drift-audit/drift_report.py` line 111,
  `tools/memory-recall/recall_conf.py` line 123 and `tools/memory-tree/merge-rows.py` line 1516.
  The others are `tools/run-gates/derive-ceilings.py` line 126, `tools/run-gates/check-receipt.py`
  line 214 and `tools/memory-tree/migrate_backlog.py` line 2737. `govkit.py` and `recall_conf.py`
  already document the class in their own docstrings.
  (a) Leave them out. §3 hands them off, for the owner to adopt as a unit of their own or leave.
  (b) Add a Python arm to this unit, scrubbing through `env=` or walking up as `govkit.py` does, and
  close the deferred ask `TOOL-aCollapsedScan-8`.
  Recommendation: (a). A Python predicate reads argv lists that span lines and `cwd=` keywords, so it
  is a second parser with its own population and near-misses. M2 makes that a second mechanism, and
  this unit is already a large diff. Under (b), a rev bump adds a scope item, a criterion and a
  `closes` verb.
  RESOLVED (agent, 2026-10-07, delegated): (a). Option (b) is a second mechanism in one spec, which
  M2's one-mechanism rule refuses, so it is handed off as §3 states.

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft from the unit 45 spec brief and the owner's ruling, grounded on
  the run branch at `03a0956c`. The predicate, its widenings and the near-misses were run over the
  real tree, and the exported-`GIT_DIR` failures were measured on node `a`. The three forks are left
  open for the owner, at the owner's request.
- rev-2 · 2026-10-07 · node a · the build pass resolved the three forks under the run's delegation,
  F1 (a), F2 (b) and F3 (a), each by its own recommendation. §4 "The mode" now says what the
  registry pair gains: the key shape with its refusal phrases, a reason map, and per-key
  undeclared text for `check_registry`. S9 adds the kit descriptor's and the dossier's leg-count
  sentences and the subject pin the new leg owes, which the pass found graded by `govkit selfcheck`.
- rev-3 · 2026-10-07 · node a · S5 adds the testsuite-counts selector fix. After the build commit,
  that checker read the new row's `:!*.test.sh` pathspec as a self-test it could not read and
  refused; a slice of its self-test's prologue plus the new arm went red against it before the fix.

## 10. Reuse audit

The map probe was `python tools/codebase-map/reuse_lookup.py "ban a shell spelling over the tracked
tree with a content-keyed waiver registry"`, then the same with "classify each tracked shell line
and gate an undeclared site against a shrink-only registry". Both printed
`unscanned layers: none`, and both ranked name-stem neighbours only, `tree`, `key`, `tracked`,
`classify` and `check_line` first. None of them is a shell-line ban. The seam this unit extends is
the gate-lint scanner, which the gate-lint dossier's reuse affordance points at as
`sh_hygiene.scan_file`, for any per-line shell source classifier. This unit reuses its
`extract_code`, `read_registry`, `resolve_declaration`, `check_registry` and `run_selftest`, and the
registry grammar of `memory/project/substitution-fed-loops.txt`. The `PROJECT_REGISTRY_EXTRA`
route for a project-added registry follows `encoding-posture-sites.txt`, the gate-lint kit's other
gov-wired scan. The scrub spelling is the one `TOOL-aRepatriatedFork-46` put in the two
`tools/workflows/` gates, and the settle-command fix reuses unit 27's inline `derive_self_rel`.

Recall surfaced the class's prior instances, `TOOL-aCollapsedScan-7`, `TOOL-aCandidStub-4` and
`TOOL-aPacedTurnstile-10`, each fixed one site at a time. It surfaced `TOOL-aCollapsedScan-8`, the
deferred Python instance in `tools/drift-audit/drift_report.py`, which §8 F3 weighs. It surfaced
`TOOL-aRootedPrefix-1c`, which prefers a bounded walk to `--show-toplevel` because git resolves a
junction away; the scrub keeps today's junction answer, and only the settle command takes the walk.
No record rules against a spelling ban.

Recall terms used: `python tools/memory-recall/query.py "how should a gate ban a git location probe that answers wrong under an inherited GIT_DIR in a hook" --terms "inherited GIT_DIR rev-parse show-prefix show-toplevel location probe linked worktree commit-msg hook scrub derive_self_rel waiver registry"`
