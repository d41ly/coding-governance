# TOOL-dTrueNorth-23 — the kit's glob-pathspec readers strip the four pathspec-mode variables

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-23-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-23-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-31 TOOL-dTrueNorth-32 TOOL-dTrueNorth-33 |
| [2026-10-22-build-TOOL-dTrueNorth-23-deviation-22.md](../build/2026-10-22-build-TOOL-dTrueNorth-23-deviation-22.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-23-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-23-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-23-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-23-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md) | research | TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 |
| [2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md) | diff-review | TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`)
confirmed **finding 2 at HIGH**, its item **H1**. `design_lib.read_spec_revisions` and
`tree_lib.read_adding_commits` pass a `:(glob)` pathspec through `tree_lib.read_git_output`, which
keeps every variable outside `GIT_ENV_LEAKS`. Under an ambient `GIT_LITERAL_PATHSPECS` the magic is
off, the log matches nothing and no error is raised. The carries join's `stopped` arm and the
deviation join's revision population and pin anchors then read empty and report green over a
population they never read. This unit takes the review's fix, which the skeptic judged sound: the
runners that read the kit's one leak list strip the four pathspec-mode variables, and every
`:(glob)` reader of the kit reaches git through such a runner, row_grammar's age walk included. It
repairs `TOOL-dTrueNorth-20`'s runner and leaves an arm for the class.

## 2. Scope (IN)

- **S1** — `GIT_ENV_LEAKS` in `tools/memory-tree/tree_lib.py:251` gains `GIT_LITERAL_PATHSPECS`,
  `GIT_GLOB_PATHSPECS`, `GIT_NOGLOB_PATHSPECS` and `GIT_ICASE_PATHSPECS` after its eight location
  variables. `read_git_output` (`tools/memory-tree/tree_lib.py:270`) and
  `gen_build_index._build_git_env` (`tools/memory-tree/gen_build_index.py:263`), the two runners
  that read the list today, then strip all twelve. The comment above the tuple names its two halves
  and where each is taken from, verbatim: the eight from the hook-side scrub at
  `.githooks/pre-push:100`, the four from `tools/check-playbook-parity.sh:334`
  (TOOL-aDistilledCharter-7 G6). The comment above `_GIT_ENV_LEAKS` at
  `tools/memory-tree/gen_build_index.py:245-249` points at that comment instead of restating it, and
  `read_git_output`'s docstring says the modes are stripped and why. Observed by AC1, AC2 and AC3.
- **S2** — `row_grammar.derive_first_seen` (`tools/memory-tree/row_grammar.py:1658`), the age walk
  over the two `:(glob)` pathspecs `_build_backlog_pathspecs` returns, reads git through
  `tree_lib.read_git_output` and no longer through its own `subprocess.run` under the whole ambient
  environment (`tools/memory-tree/row_grammar.py:1677-1680`). It decodes the bytes as UTF-8 with
  replacement, as it does today, and a failed call is the same `Problem`, naming the command and
  git's first stderr line from the `OSError`. Observed by AC4.
- **S3** — The class arm, in the build-index selftest. It derives the kit's `:(glob)` readers by an
  `ast` walk over every `*.py` in the kit's own directory: each top-level function, and each
  module-level assignment's target, holding a string constant that carries `:(glob)`, a docstring
  excepted. That set must equal the arm's table both ways, and the walk must have met at least one. Each table row names the reader its
  probe calls: `design_lib.read_spec_revisions` itself; `deviation_join.read_population` and
  `gen_build_index.derive_audit_writers` through `tree_lib.read_adding_commits`;
  `row_grammar._build_backlog_pathspecs` through `row_grammar.derive_first_seen`; and
  `gen_build_index.cmd_selftest`, whose constants are the suite's own fixtures, exempt by name.
  Over one fixture repository of the arm's own, each probe runs unset and then under each of the
  four variables set to `1`, and must return the unset answer, which must not be empty. A second
  half captures the `env` each runner of S1 hands `subprocess.run` with all four set, and none may
  reach it. Observed by AC3 and AC5.

## 3. Non-goals (OUT)

- `design_lib.run_git` and routed_commits' `GIT_LOCATION_VARS`, the two runners that read no leak
  list. They are the review's M1 and L6, which `TOOL-dTrueNorth-26` builds by importing
  `tree_lib.GIT_ENV_LEAKS`, so both strip the four modes once that unit lands. `design_lib.run_git`
  passes `--literal-pathspecs`, and git refuses that flag beside an ambient `GIT_GLOB_PATHSPECS` or
  `GIT_ICASE_PATHSPECS` (§4 Evidence). That refusal is loud, never a silent empty read, and curing
  it is M1's.
- Passing the pathspecs without magic and filtering in Python, the review's alternative fix; §4
  "Alternatives rejected" says why.
- The hooks' own unset lines, `.githooks/pre-commit:8` and `.githooks/pre-push:100`. Git exports
  the location variables to a hook, so a hook scrubs them; it exports no pathspec mode. The kit's
  runners strip the modes for every caller, hook or not.
- The other members of the class outside this kit's Python runners, handed off below.
- A bug-class checklist entry. The review asks for `fixture-inherits-ambient-machine-state` if it is
  absent, and it is present: `memory/gotchas/fixture-inherits-ambient-machine-state.md`.
- The `KIT_MEMORY_TREE_VERSION` bump these kit edits owe. `push-main.sh` mints it into the prepared
  merge (`tools/memory-tree/check-verdict-epoch.sh`, its header).

### Edges

- **consumes-from** external — TOOL-dTrueNorth-20, CLOSED, so read as built rather than as an edge: `tree_lib.read_git_output`, the leak list's home in `tree_lib.py` and `read_adding_commits`, which S1 and S3 extend; without them there is no one runner to strip the modes in
- **consumes-from** external — row_grammar's age walk, TOOL-aRepatriatedFork-9's `derive_first_seen` over `_build_backlog_pathspecs`, which S2 moves onto the kit's runner
- **hands-off** `TOOL-dTrueNorth-26` — `GIT_ENV_LEAKS` with the four modes, and `read_git_output`, which that unit's M1 and L6 runners strip by once they import the list, so they strip the modes too
- **hands-off** external — the class outside this kit's Python: the unattended kit's shell readers of `:(glob)` pathspecs (`tools/unattended/check-unattended.sh:481`, `tools/unattended/unattended.sh:3313`, `tools/unattended/lib-unattended.sh:831` and their siblings), `tools/run-gates/regen.py:110`, and the hygiene engine's plain-wildcard listings at `tools/memory-tree/check-memory-hygiene.sh:3082` and `:3122`, which read empty under `GIT_LITERAL_PATHSPECS` or `GIT_NOGLOB_PATHSPECS`; the close's left-shift files them

## 4. Design

### Evidence

Measured 2026-10-22 at `6f5f4ddec`, git 2.54.0.windows.1, PINNED.

- A scratch repository holding one spec of two commits: `git log -- ':(glob)memory/builds/*/spec/**/*-spec-*.md'`
  listed 2 commits unset and under `GIT_GLOB_PATHSPECS`, `GIT_NOGLOB_PATHSPECS` or
  `GIT_ICASE_PATHSPECS`, and 0 under `GIT_LITERAL_PATHSPECS`, exit 0 each time. The same repository
  with `--literal-pathspecs` on argv and `GIT_GLOB_PATHSPECS` or `GIT_ICASE_PATHSPECS` set died:
  "global 'literal' pathspec setting is incompatible with all other global pathspec settings".
- On this tree, with `GIT_LITERAL_PATHSPECS=1` against unset:
  `row_grammar.derive_first_seen` dated 0 ids against 912;
  `design_lib.read_spec_revisions` read 0 revisions of
  `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-19.md` against 5;
  `tree_lib.read_adding_commits` over `:(glob)memory/builds/*/reviews/**` answered `{}` for
  `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md` against its
  adding commit `3ce234bd8`. No call raised.
- S3's walk, run over the kit's directory before writing this spec, found five functions holding
  seven constants: `design_lib.read_spec_revisions` (`tools/memory-tree/design_lib.py:484`),
  `deviation_join.read_population` (`tools/memory-tree/deviation_join.py:529-530`),
  `gen_build_index.derive_audit_writers` (`tools/memory-tree/gen_build_index.py:874`),
  `gen_build_index.cmd_selftest` (`tools/memory-tree/gen_build_index.py:6226`) and
  `row_grammar._build_backlog_pathspecs` (`tools/memory-tree/row_grammar.py:1655`, two). The
  review named two readers; the walk is what found the other two.
- Of those readers, three reach git through `read_git_output`: `read_spec_revisions` directly
  (`tools/memory-tree/design_lib.py:491`) and the two adding-commit callers through
  `read_adding_commits` (`tools/memory-tree/tree_lib.py:282`). The fourth,
  `derive_first_seen`, spawns its own `subprocess.run` with no `env`, so it inherits the location
  variables too, not only the modes.
- A grep of the kit's Python for `ls-files`, `log` and `grep` argv found no plain-wildcard
  pathspec, and no file of the kit spells `PATHSPECS`. No caller sets a mode on purpose.

### Why the list and not a second tuple

`GIT_ENV_LEAKS` is the kit's one answer to "what must a git reader not inherit", and
`tools/memory-tree/tree_lib.py:244-250` says so: "ONE list for the kit". The two runners that strip
it today, and the two `TOOL-dTrueNorth-26` moves onto it, all answer that one question. A second
tuple of four would be a second answer every runner must remember to apply, which is how
`design_lib.run_git` came to strip nothing (the review's M1). The tuple's comment keeps the
verbatim claim true by naming its halves: the hook list is a subset, unchanged.

### The arm

One fixture repository under the selftest's temporary base, built the way the selftest's other
git fixtures are: a spec of two commits under `memory/builds/<slug>/spec/`, a review record under
`memory/builds/<slug>/reviews/`, and a backlog shard holding one row of a declared family, with a
conf naming that family. Each probe's unset answer is read first and must be non-empty, so a
fixture that reads nothing fails the arm rather than passing it. Then each variable is set in
`os.environ`, the probe runs, and the variable is restored in a `finally`, so no later arm runs
under it. The env half wraps `subprocess.run` for one call of each runner, as the selftest's
existing redirect arms do (`tools/memory-tree/gen_build_index.py:6253`), and reads the `env`
keyword it was handed.

What the arm does not check: the behavioural half can red only on `GIT_LITERAL_PATHSPECS`, because
a `:(glob)` pathspec answers the same under the other three modes on a fixture whose paths differ
in no case; the env half is what reds on each of the four. The walk reads `*.py` only, so a
`:(glob)` built at runtime from pieces, or spelled in a shell script of the kit, is not seen. It
reads a module-level constant as its own row, so a pathspec lifted out of its reader into one is
seen, and the reader using it must be named on that row.

### Inventory

No identifier is minted. `GIT_ENV_LEAKS` gains four values; the arm's labels open
`TOOL-dTrueNorth-23 AC`.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/gen_build_index.py`

### Rollout

A staged path under the kit's directory is a build-index input (`check_index_input`), so check 9
renders under `--staged`. The pass runs `gen_build_index.py --write` before its commit and stages
whatever it re-renders; none of these edits changes a rendered byte.

### Alternatives rejected

- **A second tuple, `GIT_PATHSPEC_MODES`, stripped in `read_git_output` alone.** It leaves
  `_build_git_env` and the two runners `TOOL-dTrueNorth-26` repairs inheriting the modes, and it is
  a second list for one question.
- **Pathspecs without magic, filtered in Python.** `read_spec_revisions` already filters with
  `inside`, but a plain `memory/builds` log reads every commit that touched any build file, and
  each other reader would need its own filter. It cures today's four readers and not the next one.
- **Unsetting the modes in the hooks.** A gate run by hand or in CI goes through no hook.

## 5. Production-readiness checklist

- security — no new surface. The four variables are ambient caller state, and stripping them
  narrows what a reader inherits, deny by default.
- perf / scale — none measurable: the same spawns, four more keys skipped while each env is built.
- error / empty / loading states — a failed git call stays an `OSError` naming the command and git's
  first stderr line, and `derive_first_seen`'s stays a `Problem`. The silent empty read under
  `GIT_LITERAL_PATHSPECS` can no longer happen.
- observability — the arm names each reader and each variable whose answer moved.
- risks — a caller that sets a pathspec mode on purpose loses it. None does (§4 Evidence).
- testing — AC1 to AC5 as probes of this tree and of a fixture; the arm under §7, observed red at
  the close against the base runner.
- migration — none.
- user docs — the tuple's comment and `read_git_output`'s docstring; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When a probe at this repo's root calls `design_lib.read_spec_revisions` over
  `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-19.md` unset, and again with
  `GIT_LITERAL_PATHSPECS=1` in its own environment, both calls return the same revision count, and
  it is at least one.
  Red when: `read_git_output` keeps the variable, so the second call returns zero revisions and
  raises nothing (measured: 5 against 0).
  figure: DERIVED, the unset count read in the same probe.
- **AC2** — When the probe repeats AC1's call, and `tree_lib.read_adding_commits` over
  `:(glob)memory/builds/*/reviews/**` for
  `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`, under each
  of the four variables set to `1` one at a time, every answer equals the unset answer.
  Red when: the adding-commit read answers `{}` under `GIT_LITERAL_PATHSPECS`, as it does at base.
- **AC3** — When a probe sets all four variables and captures the `env` that
  `tree_lib.read_git_output` and `gen_build_index._build_git_env` each hand `subprocess.run`, none
  of the four keys is in either, and `tree_lib.GIT_ENV_LEAKS` holds the eight location variables
  and the four modes.
  Red when: a runner builds its env from a list missing one, so that variable reaches git.
- **AC4** — When a probe calls `row_grammar.derive_first_seen` over this repo's conf unset and with
  `GIT_LITERAL_PATHSPECS=1`, both return the same number of dated ids, at least one, and an `ast`
  walk of the function finds a `read_git_output` call and no `subprocess.run`.
  Red when: the walk keeps its own `subprocess.run`, which dates zero ids under the variable
  (measured: 912 against 0).
  cost: about a second per call, over this tree's backlog history.
- **AC5** — When a probe runs S3's walk over `tools/memory-tree/`, it returns exactly the five
  functions of §4 Evidence; and run over a scratch copy of that directory holding one more module
  whose top-level function returns a `:(glob)` string, it names that function as a reader the
  table does not hold, and likewise a module-level constant holding one.
  Red when: the walk reads one module, or matches only docstrings, so the planted function passes.
  figure: PINNED, five functions at `6f5f4ddec`; a later unit that adds a reader adds its row.

## 7. Gates

`memory hygiene` · `build-index selftest` · `row-grammar selftest` · `routed-commits selftest` · `spec-tokens self-test` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC1 AC2 AC3 AC4 AC5 · the base runner, which keeps the four variables, so every probe reads empty under the literal mode and the env half finds all four keys; and a planted sixth function holding a glob pathspec, which the table lacks · none

The row-grammar, routed-commits and spec-tokens suites run the readers S1 and S2 change; their
existing arms re-observe the unset answers.

## 8. Open questions

- **F1 — Which binding line does a unit the closing review promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it
  adds (ER:320). (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds
  `unbound` and (c) reds `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F2 — Where are the four modes stripped?** (a) `GIT_ENV_LEAKS` gains them, so every runner
  reading the list strips them. (b) A second tuple stripped in `read_git_output` alone. (c)
  Magic-free pathspecs filtered in Python, the review's alternative. All three pass every veto; (a)
  is the most capable, covering four runners where (b) covers one and (c) covers the readers it is
  written into. §4 says why. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-22, delegated):
  (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the kit edits here?** S1 and S3 harden the readers
  `cl-dClosedLoop-0002`'s carries join (`read_spec_revisions`), `cl-dClosedLoop-0004`'s deviation
  join (its revision population and pin anchors) and `cl-dClosedLoop-0005`'s audit pin
  (`derive_audit_writers`) read. S2 moves row_grammar's age walk onto the same runner. No clause
  names that walk; it is lifted here as the class member the brief's "every `:(glob)` reader in the
  kit" names, changing which runner it uses and not its CLI, its output or its exit. Leaving it out
  fails that bound (veto 1). RESOLVED (agent, 2026-10-22, delegated): lifted by
  `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the memory-tree kit's git runners and
  the build-index selftest arm, made for the readers of cl-dClosedLoop-0002, cl-dClosedLoop-0004
  and cl-dClosedLoop-0005 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, promoted from the closing diff review's finding 2 (HIGH,
  item H1).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "drop pathspec mode environment variables before
a git glob read"` ranked `read`, `git`, `run_git` and `build_git_env` (`tools/memory-tree/tree_lib.py`)
by name stem. The seam this unit extends is `tree_lib.GIT_ENV_LEAKS` with its reader
`tree_lib.read_git_output` (`tools/memory-tree/tree_lib.py:251`, `:263`), which the probe did not
rank; it was found by reading the finding and the source. The mode list is taken from
`tools/check-playbook-parity.sh:334`, the tree's one existing unset of the four. The recall query
returned the review's H1 and `TOOL-cListedCensus-1`, whose fix lists files with no pathspec magic and
filters by suffix; that is the alternative §4 rejects for this kit, because its readers already
share one runner. The probe ranked `build_git_env` as the env seam; it copies the environment whole
and strips nothing, so it is not where the strip lives, and the hit disagrees with source on that.

Recall terms used: `python tools/memory-recall/query.py "why does a glob pathspec git read return
nothing under an ambient environment variable" --terms "GIT_LITERAL_PATHSPECS pathspec glob magic
GIT_ENV_LEAKS read_git_output ambient environment fixture-inherits-ambient-machine-state hook scrub
unset"`
