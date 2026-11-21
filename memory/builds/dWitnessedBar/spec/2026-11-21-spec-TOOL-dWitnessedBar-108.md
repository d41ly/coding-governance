# TOOL-dWitnessedBar-108 — the closing review round 1's four minors batched: a staged removal trips the commit-time guard, scaffolded ledger homes open with their rendered header, an unread parameter reds, and the charter's trailer is checked at commit time

**Status:** INPROGRESS · rev-1 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 51 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-108-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-108-build-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-108-promotion-brief.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-108-promotion-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-108-promotion-spec-writer.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-108-promotion-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 1
(`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md`)
read CLEAN WITH FIXES with six confirmed findings. Its two HIGHs are their own units. This unit takes
the four minors, each by the class-level fix and the left-shift gate the record carries, re-derived
against the code at `63be790a2`, so each class reds when it recurs.

| Report item | Severity | Finding | Lands on | Scope items |
|---|---|---|---|---|
| M1 | MEDIUM | 3 | `tools/run-gates/precommit.py#read_staged` | S1, S2 |
| M2 | MEDIUM | 4 | `tools/memory-tree/adopt-memory-tree.sh`, its `--scaffold` ledger homes | S3, S4, S5 |
| L1 | LOW | 5 | `tools/run-gates/verdict_flow.py#run_quiet_leg` | S6, S7 |
| L2 | LOW | 7 | the agent-commit trailer, `AGENTS.md@71a6071e:278` | S8, S9, S10 |

S11 keeps the pages that describe the changed behaviour current.

## 2. Scope (IN)

- **S1** — M1, the class fix. `read_staged` lists the staged set as the runner's `changed` counts it:
  `git diff --cached --name-only --no-renames -z`, with no `--diff-filter`. A staged `git rm` lists its
  path, and a staged `git mv` lists both its source and its destination, so either trips a guard the
  source sits under. Its docstring says so. Observed by AC1.
- **S2** — M1, the left-shift gate. `tools/run-gates/leg_factory.py#run_selftest` gains the arm §4 "The
  trigger parity arm" states, keyed to the runner's own `changed` line read from `run-gates.sh`, so a
  later divergence of either copy reds. Observed by AC2.
- **S3** — M2, the class fix. Every ledger home `--scaffold` writes opens with the header line its
  `[[ledger]]` table in the kit's `kit.toml` renders through `render_header`, through one shell
  function, `render_ledger_header`. That is the four homes the finding names, `legacy-files.txt`,
  `curation-debt.txt`, `unarmed-branches.txt` and `stale-header-waiver.txt`, and the two whose header
  is typed today, `readme-contract.txt` and `method-carriers.txt`. Observed by AC3.
- **S4** — M2. The `unarmed-branches.txt` comment states the ledger grammar and no field list of its
  own: each row is the header's key fields, then the count, the sha and the disposition,
  TAB-separated. The other three homes' prose lines stay, as `#` lines below the header. Observed by
  AC4.
- **S5** — M2, the left-shift gate. `tools/memory-tree/check-memory-hygiene.test.sh` gains the
  scaffold-then-witness arm §4 "The scaffold witness arm" states, which enumerates every
  `*-to-ledger` `[[upgrade]]` and every `[[ledger]]` table of the kit's `kit.toml`, so a later
  registration is covered with no edit to the arm. Observed by AC5.
- **S6** — L1, the class fix. The signature of `run_quiet_leg` becomes `(run, row, n, top)`, as its
  one caller, `cmd_quiet_rerun`, and the fixture's `run_rerun_stub` already call and spell it
  (§8 F3). Observed by AC6.
- **S7** — L1, the left-shift gate. `tools/run-gates/py_reads.py` gains a third arm, `params`, which
  reds a parameter its function's body never loads unless the `unread-params` ledger keeps it,
  and reds a kept row no hit carries (§4 "The params arm", §8 F4). Observed by AC7 and AC8.
- **S8** — L2, the value. The charter's trailer stands as AGENTS.md states it, because AGENTS.md is
  Level 0 and outranks a harness attribution reminder. The trailer reader in
  `tools/lib/commit_trailers.py` gains `read_charter_trailer` and `check_message_attribution`, and the
  `attribution` verb §4 "The attribution verb" states. Observed by AC9.
- **S9** — L2, the position. `check_commit_message` in `tools/unattended/unattended.sh` asks the
  `attribution` verb of every message a bound run's commit carries, `Pass: none` included, before
  its early return, and refuses with code 49 on a wrong value or a trailer that is not the last
  line. Its `Commit-Checked:` write moves to the start of the trailer block, so the charter's "ends
  with" stays true (§8 F5). Observed by AC10 and AC11.
- **S10** — L2, the left-shift gate. `tools/unattended/unattended.test.sh` gains the arm §4 "The
  attribution arms" states, beside the `--check-commit` arms, reading the expected value from the
  fixture's own `AGENTS.md`. Observed by AC10 and AC11.
- **S11** — The pages that describe these behaviours. `help/tags.md`'s trailer paragraph states where
  `Commit-Checked:` is written and the attribution refusal, and `tools/run-gates/README.md`'s
  commit-time paragraph states what the staged set lists. Observed by AC12.

## 3. Non-goals (OUT)

- The two HIGHs of the record, H1 and H2, which their own units take.
- Rewriting history: the commits before this unit lands keep the trailers they carry, both values.
- A history check of trailer values in the pass-order leg or the pre-push hook. The record's gate is
  the commit check; a range check would red every build range that predates it.
- A change to AGENTS.md or to `.governance/deploy.toml`'s `[charter] commit_trailer`, which owns the
  charter's value. §8 F5 keeps the charter's wording true instead.
- A rename of the `python reads (a name never bound, an import outside its guard)` leg or a change to
  its `purpose`. The manifest row and `tools/gate-legs.json` stay byte-identical.
- Renaming the parameters the `unread-params` seed keeps. Each one drains through the ledger.
- A kit version bump. Versions are minted at landing (`3cecd39a0`).
- A guard change on any leg. §8 F1 homes the M1 arm where no guard needs one.

This unit edits only the built code of CLOSED units, never their specs. `TOOL-dWitnessedBar-10`
built `read_staged` (`d15371e5e`), `TOOL-dWitnessedBar-16` built the ledger conversions of the four
populations and the scaffold's two typed headers (`87bc9f615`), `TOOL-dWitnessedBar-30` built
`run_quiet_leg` (`7b918f7e0`), and `TOOL-dWitnessedBar-2` built the `Commit-Checked:` write
(`7f3e24092`), each found by its `Pass:` trailer.

### Edges

none

## 4. Design

### Why one unit

M4 batches every MEDIUM and LOW of a review into one unit, or two where they split into disjoint write
sets by M6's clauses. The four items fall into four disjoint write sets: S1 and S2 under
`tools/run-gates/` in `precommit.py`, `leg_factory.py` and `README.md`; S3 to S5 in two memory-tree
files; S6 and S7 in `verdict_flow.py`, `py_reads.py`, the govkit registry, the memory conf, the
attributes file and the new home; S8 to S11 in the trailer reader's three copies, the unattended
driver, its suite and `help/tags.md`. The brief asks for one spec, so this one spec holds them, and
the return says the split exists.

### Evidence

Read on 2026-11-21 at `63be790a2`, the run branch's HEAD.

- `tools/run-gates/precommit.py#read_staged` runs `git diff --cached --name-only --diff-filter=ACMR -z`.
  `tools/run-gates/run-gates.sh@04da8977:599` defines `changed` as
  `! git diff --quiet "$BASE" -- "$@"`, with `GATE_FULL` and an empty `BASE` answering 0 first.
- Probed in a scratch repository holding `a/x`, `a/y` and `b/z`, with `changed` evaluated from the
  runner's own line and `BASE` at HEAD, guard `a/`: a staged `git rm a/x` read runner tripped,
  precommit quiet with an empty staged list; a staged `git mv a/y b/y` read runner tripped, precommit
  quiet with only `b/y`; a staged edit of `a/x` read both tripped; a staged edit of `b/z` read both
  quiet. `--no-renames` with no filter listed `a/x` for the first case and `a/y b/y` for the second,
  and `--diff-filter=ACDMR`, the finder's instance fix, listed only `b/y` for the rename.
- `tools/memory-tree/adopt-memory-tree.sh@277edcb9:743-753` and `:849-853` write the four homes with
  prose lines only, `:748` naming `gate<TAB>check<TAB>ordinal<TAB>signature`. `:800` and `:817` type
  the readme-contract and method-carriers headers. `_PY` is resolved at `:327`, before any of them.
- `tools/memory-tree/legacy_ledger.py#render_header` renders the line from five attributes of a
  registration; `#read_registrations` reads tracked descriptors only, so a kit copied in and not yet
  committed registers nothing. `#check_home_readable` refuses a home whose first line is neither that
  header nor an unarmed line, and `#read_home_state` reads a header with no row as armed.
- Probed: an `-I -c` program putting `tools/memory-tree` on `sys.path`, reading its `kit.toml` with
  `tomllib` and calling `render_header` on a `types.SimpleNamespace` of the population's table printed
  lines equal to the first lines of gov's six homes at `63be790a2`.
- Probed: a tree scaffolded today from a stand-in conf, `registry_to_ledger.py witness` exited 1 for
  each of the four homes, printing `is in its legacy grammar: not applied`, and 0 for readme-contract
  and method-carriers.
- `tools/memory-tree/kit.toml@f835ca7c` carries 16 `[[ledger]]` tables and 14 `*-to-ledger`
  `[[upgrade]]` rows (DERIVED 2026-11-21 by `grep -c` at `63be790a2`), each with a `witness` argv in
  the `{gov}` and `{target}` grammar, eight through `registry_to_ledger.py` and six through
  `conf_pins_to_ledger.py`.
- `tools/memory-tree/check-arms.py#parse_pin` reads pins through `read_rows` with `PIN_FIELDS`, the
  path, the check and the signature, and `PIN_VERBATIM` of `(1, 2)`.
- `tools/run-gates/verdict_flow.py#run_quiet_leg` takes `here=HERE` and reads its runner from
  `profile_bar.RUNNER`; `#cmd_quiet_rerun` calls `(rerun or run_quiet_leg)(run, r, n, top)` and uses
  its own `here` for `read_wait_ceiling`. The fixture's `run_rerun_stub` is defined
  `(run, row, n, top)`.
- Probed: an AST scan over the 209 tracked `*.py` outside `memory/` (DERIVED 2026-11-21), counting a
  parameter of a `def` that no `Name` load inside the function's body reads, `self`, `cls` and a name
  opening `_` left out, printed 112 hits in 32 files (DERIVED 2026-11-21 by that scan), and 109
  distinct path, function and parameter keys (DERIVED 2026-11-21 by that scan), one of them `run_quiet_leg`'s `here`. The rest are fixed-signature stubs,
  callbacks and uniform scanner signatures, which is why the arm keeps a ledger.
- `tools/run-gates/py_reads.py#scan_unbound_names` and `#scan_tracked_names` read the same population
  through `git ls-files`; `#load_readers` reaches the memory-tree kit; `#run_selftest` holds plants;
  `tools/run-gates/run-gates.gov.test.sh` runs `py_reads.py --selftest`. The leg is declared in
  `tools/govkit/registry.toml@d66bd829:2420-2431` with no guard.
- Gov-only ledger homes are each a `[[ledger]]` table in the govkit registry, a
  `PROJECT_REGISTRY_EXTRA` member in `.memory-tree.conf`, and a `merge=rows` row in `.gitattributes`,
  as `unpinned-facts.txt` is.
- `AGENTS.md@71a6071e:278` reads ``- **Commit trailer:** every agent commit ends with `Co-Authored-By:
  Claude Opus 5 <noreply@anthropic.com>`.``, rendered from
  `coding-governance-agents.template.md`'s `{{COMMIT_TRAILER}}` line.
- `git log --format=%B 9e21ac760dc0..63be790a2 | grep -o 'Co-Authored-By: Claude Opus [0-9.]*' | sort |
  uniq -c` printed 258 `Opus 5` and 287 `Opus 5.5` (DERIVED 2026-11-21).
- `tools/unattended/unattended.sh#check_commit_message` returns 0 before any check where no run binds
  the branch, reads the message through `commit_trailers.py message`, and returns 0 at
  `case " $trl " in *" none "*)`. Its last act is
  `git interpret-trailers --in-place --if-exists replace --trailer "Commit-Checked: ..."`, which
  appends after `Co-Authored-By:`. Probed with git 2.54 (PINNED 2026-11-21, node d): adding `--where start` placed
  `Commit-Checked:` above `Pass:`, kept `Co-Authored-By:` last, replaced an older `Commit-Checked:` in
  place, and left trailing comment lines alone.
- `tools/lib/commit_trailers.py#read_message_ids` reads a message's trailers through
  `git interpret-trailers --parse`. The file is one inlined block, byte-identical in
  `tools/memory-tree/commit_trailers.py` and `tools/unattended/commit_trailers.py`, held by the
  parity table in `tools/lib/resolve-python.test.sh`.

### The trigger parity arm

In `run_selftest`, after the existing cases, `check_precommit_trigger(scratch)` builds a scratch
repository holding `a/x`, `a/y` and `b/z` in one commit. It reads the runner's `changed` definition as
the one line of `run-gates.sh` beside this file that opens `changed()`, and runs it under the bash
`precommit.resolve_bash_launcher` finds, with `BASE` set to HEAD, through the nested
`read_runner_verdict(guard)`. For four staged cases, a `git rm a/x`, a `git mv a/y b/y`, an edit of
`a/x` and an edit of `b/z`, each from a clean reset, it compares that verdict for guard `a/` with
`any(check_guard_trips(p, "a/") for p in read_staged(top))`, and prints one `arm ok` or `arm FAIL`
line per case, naming the case and both answers. The work tree always equals the index, so the
runner's work-tree compare and the hook's index compare read the same change. `total` counts the
four cases. An absent `changed()` line, or no bash, is an `arm FAIL` naming why, never a skip.

WHAT IT DOES NOT CHECK: an unstaged edit, which the runner counts and the hook never sees by design,
and a guard the manifest spells with `{prefix}`, which `derive_trigger` resolves before the compare.

### The scaffold header

`render_ledger_header <population>` runs `"$_PY" -I -c` with a program that puts `$HERE` on
`sys.path`, imports `legacy_ledger`, reads `$HERE/kit.toml` with `tomllib`, takes the one
`[[ledger]]` table naming the population, refuses on `_check_table`'s findings or a count other than
one, and prints `render_header(types.SimpleNamespace(**table))`. The shell strips a trailing CR, as
`:579` warns for Windows python. A failure prints `memory-tree: <home> has no rendered ledger header:
<why>` on stderr and the scaffold exits 2: a home written without its header is the defect itself.
Each of the six writes opens with the function's line, then its existing prose as `#` lines, then
any seeded rows, so `read_rows` skips the prose and the readers see the header first.

### The scaffold witness arm

After the `$A` scaffold arms, one arm reads `$HERE/kit.toml` with `tomllib` under `$_PY`. For every
`[[upgrade]]` whose `id` ends `-to-ledger`, it runs the `witness` argv with `python` as `$_PY`,
`{gov}` as `$HERE/..` and `{target}` as `$A`, and owes exit 0. For every `[[ledger]]` table whose
`home` exists under `$A`, it owes that home's first line equal to `render_header` of the table, read
through the kit's own `legacy_ledger` and never through `render_ledger_header`. Each miss prints
`FAIL scaffold ledger · <id or home> · <what>`. It fails when it read no `-to-ledger` row or compared
no home, since an empty population is not coverage.

WHAT IT DOES NOT CHECK: a home the scaffold leaves absent, which the witness answers as applied, and
the rows of a seeded home, which the seed-across arms grade.

### The params arm

`scan_unread_params(source)` returns, for each `ast.FunctionDef` and `ast.AsyncFunctionDef`, every
positional, keyword-only, `*` or `**` parameter that no `ast.Name` load in the function's body reads,
nested bodies included, as `(function name, parameter)`. `self`, `cls` and a parameter opening `_`
are never hits, which is the corpus's spelling for an unused slot. `measure_unread_params(root,
id_grammar)` reads the same population as `scan_tracked_names` and counts hits per
`(path, function, parameter)` key. `check_unread_params(root, measured)` reads the `unread-params`
registration through `read_registrations`, and the home through `read_ledger`, and puts both through
`compare_counts` with the registration's direction. Each finding prints
`py-reads: RED params · <path> · <function> · <parameter> · <finding> (<measured> measured, <kept>
kept)`. `run_both` runs it after the name arm and prints
`py-reads: params · <h> hits, <k> kept rows, <u> unlisted, <s> stale` and the line
`py-reads: params, not read · a lambda, a parameter read only through locals() or a string`. An absent
home, or no registration, is a refusal, exit 2. `run_list_params(tool_root)`, behind `--list-params`,
prints each key's fields and count TAB-joined, the seed.

The registration, in the govkit registry beside `unpinned-facts`:

```toml
[[ledger]]
population = "unread-params"
leg = "python reads (a name never bound, an import outside its guard)"
seed = ["python", "{prefix}/run-gates/py_reads.py", "--list-params"]
key = "site"
fields = ["path", "function", "param"]
drain = "key"
direction = "shrink-only"
home = "memory/project/unread-params.txt"
```

The builder seeds the home with `python tools/memory-tree/legacy_ledger.py seed --population
unread-params` after S6, so it holds every key the scan measures and not `run_quiet_leg`'s.
`--selftest` gains four plants: an unread parameter is a hit, the same parameter read is none, an
`_`-opening one is none, and a parameter read only in a nested function is none.

### The attribution verb

Inside the `commit_trailers_py` block, so all three copies carry it:

- `read_charter_trailer(path)` returns `(line, why)`: the first backticked span of the first line of
  `path` opening `- **Commit trailer:**`, and `why` empty; or an empty line and why none was read, a
  file absent or a line missing.
- `check_message_attribution(text, expected)` returns `(state, detail)`. The agent trailers are the
  `Co-Authored-By` trailers, key in any case, of `git interpret-trailers --parse`, whose `<...>`
  address equals the expected value's. None is `none`. One whose value is not the expected line is
  `refused`, naming both. Otherwise the last line of the message, CRs stripped, lines opening `#`
  and blank lines dropped and nothing read past a scissors line, must equal the expected line, else
  `refused`, naming that last line. All else is `ok`.
- `commit_trailers.py attribution <message file> <charter file>` prints one line,
  `ATTRIBUTION <state> · <detail>`, and exits 0 for `ok`, `none` and `unarmed`, which an empty
  expected line reads as, 1 for `refused`, and 2 for an unreadable message file.

In `check_commit_message`, directly after the `PASSTRAILER` case and before the `none` return, it
runs `"$py" "$KIT_DIR/commit_trailers.py" attribution "$msg" "$ROOT/AGENTS.md"`. Exit 1 is
`fail 49 "--check-commit: <detail>; end the message with '<expected>' and nothing after it"`, return 1.
Exit 2 prints its line and the path checks continue. The `Commit-Checked:` write gains `--where start`.

WHAT IT DOES NOT CHECK: a commit no run binds, a `--no-verify` commit, a `core.commentChar` other than
`#`, and the commits already made.

### The attribution arms

Beside the `--check-commit` arms, after the fixture's run is bound, the arm commits an `AGENTS.md`
holding the fact line with the value `Co-Authored-By: Fx <fx@example.invalid>`. Messages: that
trailer last after `Pass: none`, exit 0; `Co-Authored-By: Fx 2 <fx@example.invalid>` after
`Pass: none`, exit 1 naming both values; the expected trailer followed by a `Commit-Checked:` line,
exit 1 naming that line; no `Co-Authored-By:` at all, exit 0. With the fixture's `AGENTS.md` value
changed and committed, the first message exits 1, which shows the value is read from the charter.
An admitted pass message ending with the expected trailer gains `Commit-Checked:` and still ends
with it.

### Inventory

Minted: `check_precommit_trigger` and its nested `read_runner_verdict` in `leg_factory.py`;
`render_ledger_header` in `adopt-memory-tree.sh`; `scan_unread_params`, `measure_unread_params`,
`check_unread_params`, `run_list_params` and the `--list-params` flag in `py_reads.py`;
`read_charter_trailer`, `check_message_attribution` and the `attribution` verb in the trailer
reader; the `unread-params` population and its home. Each function opens with a verb of
`.lexicon.conf`'s VERBS table, graded by the `lexicon naming predicates` leg's function-name cell.

### Migration

Additive. The new home is seeded once from the scan; an adopter receives no new home, since
`py_reads.py` is withheld. Reversible by reverting the commit.

### Rollout

Order 51, beside the two HIGH units of the same record, whose write sets name none of these paths
as far as their briefs say. The pass writes this unit's acceptance ledger with every criterion owed
to the close. This unit's own pass commit is the first graded by S9, so it ends with the charter's
trailer.

### Files touched (estimate)

- `tools/run-gates/precommit.py`, `tools/run-gates/leg_factory.py`, `tools/run-gates/README.md`
- `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/run-gates/verdict_flow.py`, `tools/run-gates/py_reads.py`, `tools/govkit/registry.toml`
- `memory/project/unread-params.txt`, `.gitattributes`, `.memory-tree.conf`
- `memory/guides/SESSION-KICKOFF.md`, its `last-audit` re-stamp, since `.memory-tree.conf` is watched
- `tools/lib/commit_trailers.py`, `tools/memory-tree/commit_trailers.py`,
  `tools/unattended/commit_trailers.py`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`, `help/tags.md`
- `memory/builds/dWitnessedBar/build/`, this unit's acceptance ledger
- `memory/builds/dWitnessedBar/spec/2026-11-21-spec-TOOL-dWitnessedBar-108.md`, its status header
- `memory/builds/dWitnessedBar/RUN.md`
- `memory/builds/dWitnessedBar/README.md`, `memory/backlog/TOOL.md` and `memory/LIVE.md`, rendered by
  `gen_build_index.py --write`

### Alternatives rejected

- **`--diff-filter=ACDMR`, the finder's fix for M1.** The probe shows a staged rename out of a guard
  still lists only its destination, so the two copies still disagree.
- **The pre-commit hook's suite as M1's arm home.** It already copies both files, but the
  `branch-guard self-test` leg's guard covers no path under `tools/run-gates/`, so an edit to
  `precommit.py` alone never runs it (§8 F1).
- **Typed header literals held by the arm (M2).** The record's fix takes the line from the
  registration; a typed copy is the second fact that drifted.
- **Thread `here` through `run_quiet_leg`.** No caller sets it, so the seam would still be unused
  (§8 F3).
- **The attribution check in shell inside `check_commit_message`.** The kit's trailers are read
  through the one reader, `commit_trailers.py`, and a second parse would be a second rule.
- **Read the value from `.governance/deploy.toml`.** That file owns the value, but the brief and the
  record name AGENTS.md, which every role reads, and the playbook render gates the two equal.

## 5. Production-readiness checklist

- security — no new write path. The attribution verb reads a message file and AGENTS.md; the arms
  write under their scratch roots.
- perf / scale — one AST walk per tracked Python file, beside the name arm's; one python spawn per
  commit in a bound run; one python spawn per scaffolded home.
- error / empty / loading states — no `changed()` line or no bash is an `arm FAIL`; a header that will
  not render stops the scaffold with exit 2; an absent home or registration refuses the params arm;
  a charter with no fact line reads `unarmed` and says so; an unreadable message exits 2 and says so.
- observability — every arm names its case; every refusal names the expected and the found value.
- risks — a bound run's commits written with another trailer are refused from this landing on, the
  refusal naming the line to write. The params ledger starts large; it only shrinks.
- testing — AC1, AC3, AC4, AC6 and AC9 by probe in the pass; AC2, AC5, AC7, AC8, AC10 and AC11 by the
  arms at the close; AC12 by `grep`.
- migration — one seeded home; reversible by revert.
- user docs — `help/tags.md`, S11; the run-gates README for the kit reader.

## 6. Acceptance criteria

- **AC1** — In a scratch repository holding `a/x`, `a/y` and `b/z`, with a staged `git rm a/x`,
  `read_staged` from `tools/run-gates/precommit.py` lists `a/x`, and with a staged `git mv a/y b/y` it
  lists `a/y` and `b/y`; `check_guard_trips` trips `a/` on both.
  Red when: a filter or rename detection leaves the source side out and the guard stays quiet.
- **AC2** — `python tools/run-gates/leg_factory.py --selftest` prints an `arm ok` line for each of
  the four cases of §4 "The trigger parity arm"; with `read_staged`'s argv put back to
  `--diff-filter=ACMR` in a scratch copy, the remove and rename cases print `arm FAIL` and it exits 1.
  Red when: the hook's list and the runner's `changed` disagree and no arm says so.
  permission: a held suite leg; the main loop observes it at the close.
- **AC3** — In a tree `adopt-memory-tree.sh --scaffold` writes from a stand-in conf, the first line of
  each of the six homes S3 names equals `render_header` of its `kit.toml` table, and
  `registry_to_ledger.py witness <tree> --home <home>` exits 0 for each.
  Red when: a scaffolded home opens with prose, or a header typed apart from its table.
  fixture: a scratch tree under the run's scratch directory.
- **AC4** — The scaffolded `unarmed-branches.txt` holds no `ordinal`, and a row
  `x.sh<TAB>exit<TAB>sig<TAB>1<TAB><sha>` plus the disposition `seeded`, appended as its comment says,
  reads through `legacy_ledger.read_rows(path, 3, verbatim=(1, 2))` with no malformed entry.
  Red when: the comment documents a grammar the pin reader refuses.
- **AC5** — The scaffold witness arm passes on the built tree; run over a scratch copy of the
  scaffolder at `277edcb9`, it prints `FAIL scaffold ledger` for each of the four homes.
  Red when: a scaffolded home reads as owing a conversion it never needed.
  permission: a suite run; the main loop observes it at the close.
- **AC6** — `python -c` with `inspect.signature` over `verdict_flow.run_quiet_leg` prints
  `(run, row, n, top)`, and `grep -n 'run_quiet_leg' tools/run-gates/verdict_flow.py` names the one
  definition and the one call.
  Red when: the parameter that implies a seam is still declared.
- **AC7** — `python tools/run-gates/py_reads.py` over the built tree exits 0 and prints a
  `py-reads: params ·` line with 0 unlisted and 0 stale. With `here=HERE` put back in a scratch copy,
  it exits 1 naming `run_quiet_leg · here`; with one kept row added that no hit carries, it exits 1
  naming that row as unmeasured.
  Red when: a parameter its body never reads lands without a row, or a drained row stays kept.
  figure: the hit and row counts are DERIVED at observation time.
- **AC8** — `python tools/run-gates/py_reads.py --selftest` prints its plants line with every plant
  held, the four of §4 "The params arm" among them.
  Red when: the scan counts an underscore, a nested read or a read parameter as a hit, or misses a
  planted one.
  permission: the `run-gates gov canary` leg runs it at the close.
- **AC9** — `python tools/lib/commit_trailers.py attribution <msg> AGENTS.md` exits 0 printing
  `ATTRIBUTION ok` for a message ending with the charter's line, and exits 1 printing
  `ATTRIBUTION refused` for one ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and
  for one whose charter line is followed by `Commit-Checked: unattended@1.129`; a message with no
  `Co-Authored-By:` prints `ATTRIBUTION none`, and a charter file with no fact line prints
  `ATTRIBUTION unarmed`, each exit 0.
  Red when: a wrong value or a trailer that is not last is admitted.
  fixture: message files under the run's scratch directory.
- **AC10** — The attribution arms of §4 pass: `--check-commit` refuses the wrong value and the
  trailing line with code 49 under `Pass: none`, admits the expected trailer and a message with none,
  and refuses the first message after the fixture's `AGENTS.md` value changes.
  Red when: the commit check admits a trailer the charter does not name, or reads a typed copy.
  permission: the owner's standing instruction forbids a pass running this kit's suites; the main
  loop observes it at the close.
- **AC11** — In the same arms, an admitted pass message carries `Commit-Checked:` and its last line
  is still the expected trailer.
  Red when: the commit check's own write breaks the charter's "ends with".
  permission: as AC10.
- **AC12** — `grep -n 'where start\|attribution' help/tags.md` names the trailer paragraph's new
  sentences, and `grep -n 'no-renames' tools/run-gates/README.md` names the commit-time paragraph.
  Red when: a page still describes the old trailer order or staged set.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms` · `leg-factory selftest` · `memory-hygiene self-test` · `python reads (a name never bound, an import outside its guard)` · `run-gates gov canary` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `ratchet (both ways)`

The guard join over Files touched owes `recall floor`, `recall floor arms`, `policy fixtures`, the
three govkit legs, the two legs guarding `unattended.sh`, and the three `.memory-tree.conf` legs. The
rest grade the arms, the inline parity of the trailer reader's copies, the minted names and the new
population, and the first two are the brief's.

New arm: tools/run-gates/leg_factory.py · covers AC2 · `read_staged` put back to `--diff-filter=ACMR` reds the remove and rename cases · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · the scaffolder at `277edcb9` writes four header-less homes · none
New arm: tools/run-gates/py_reads.py · covers AC7 AC8 · `here=HERE` put back on `run_quiet_leg`, and a planted unread parameter · none
New arm: tools/unattended/unattended.test.sh · covers AC10 AC11 · a message ending with another value, or with a line after the trailer · none

## 8. Open questions

- **F1 — Where does M1's parity arm live?** Options: (a) `leg_factory.py --selftest`, the leg the
  record names, beside both copies of the rule in the runner's kit; (b) the pre-commit hook's suite,
  whose derived block already copies both files, with the `branch-guard self-test` guard widened to
  them. (b) adds a guard edit and runs that leg on every runner edit. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3, the most feature-rich survivor with no guard change.
  widens: none · relaxes: none
- **F2 — Where is the scaffold header rendered from?** Options: (a) an `-I -c` program in the adopter
  reading `$HERE/kit.toml` and calling `render_header`; (b) a `header` verb on the kit copy of
  `legacy_ledger.py`; (c) typed literals held by the arm. (c) fails the record's fix, so veto 1 drops
  it; (b) adds a CLI surface, which veto 2 parks; `read_registrations` cannot serve, since it reads
  tracked descriptors and the runbook scaffolds before the kit is committed. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F3 — Thread `here` through `run_quiet_leg`, or take it out of the signature?** Options: (a) the
  signature without it; (b) the runner taken from `here / 'run-gates.sh'`, passed by
  `cmd_quiet_rerun`. No caller sets `here`, so (b) is an extension point no one uses, which the
  charter's `[yagni]` rules out. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F4 — How does the params arm pin the sites it does not red?** Options: (a) a shrink-only
  `[[ledger]]` population keyed by path, function and parameter; (b) renaming every kept parameter
  to open `_` now, a diff across 32 files of CLOSED units' code (DERIVED 2026-11-21, §4 Evidence);
  (c) an inline pin comment. (b) leaves this unit's scope, and (c) is a second pin grammar beside the
  ledger factory. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the reuse of the factory M5
  found.
  widens: none · relaxes: none
- **F5 — May a `Commit-Checked:` line follow the charter's trailer?** Options: (a) yes, with AGENTS.md
  reworded from "ends with"; (b) no: the commit check writes `Commit-Checked:` at the trailer block's
  start, and the attribution check holds the trailer last. (a) changes a governance carrier, which
  veto 2 parks. RESOLVED (agent, 2026-11-21, delegated): (b), rung 3, the charter's wording kept true.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-21 · initial draft, promoted from the closing diff review's round 1 per
  2026-11-21-prompt-TOOL-dWitnessedBar-108-promotion-brief: M1, M2, L1 and L2, batched.

## 10. Reuse audit

Each item extends the seam its finding names. S1 edits `read_staged` and keeps `check_guard_trips`;
S2 runs the runner's own `changed` line and the kit's `resolve_bash_launcher`. S3 calls
`render_header` and `_check_table` from the kit's `legacy_ledger.py`, the readers' own definition of
the line. S5 runs the `[[upgrade]]` witnesses as declared. S7 extends `py_reads.py` beside
`scan_unbound_names` and keeps its pins through the ledger factory's `read_registrations`,
`read_ledger` and `compare_counts`, as `tools/playbook/positional.py#check_producers` keeps its own.
S8 extends the one trailer reader, `commit_trailers.py`, whose `read_message_ids` already parses a
message's trailers. `python tools/codebase-map/reuse_lookup.py "render a ledger home's header from its
registration"` ranked `render_malformed`, `read_head_sha` and `read_registrations` of the factory
first on 2026-11-21, and `"check a function parameter that its body never reads"` ranked `read_rows`
among generic readers and no parameter scan, so no existing seam fits S7's scan and it joins
`py_reads.py`'s name arm.

Recall terms used: `python tools/memory-recall/query.py "how does a scaffolded ledger home get its header and how is a commit trailer value checked" --terms "ledger header render_header scaffold registration witness to-ledger Co-Authored-By trailer Commit-Checked diff-filter guard"`
