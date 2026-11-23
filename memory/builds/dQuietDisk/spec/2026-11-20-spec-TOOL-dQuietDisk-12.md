# TOOL-dQuietDisk-12 — `pre-push.test.sh` builds each repeated pushed-main fixture once and copies it per arm

**Status:** CLOSED · rev-3 · 2026-11-22 · node d · Tier-2 · base 7b8c737b · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-12-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-12-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-12-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-12-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-12-widen-11.md](../build/2026-11-22-build-TOOL-dQuietDisk-12-widen-11.md) | widen | — |
| [2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md](../build/2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-12-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-12-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-12-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-12-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md) | research | TOOL-dQuietDisk-6 TOOL-dQuietDisk-10 TOOL-dQuietDisk-13 TOOL-dQuietDisk-18 |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-push.test.sh` rebuilds a bare remote, a work repository, a commit and a push for every
fixture it asks for, and 29 of those calls ask for a fixture an earlier call already built with the
same arguments. This unit builds each fixture whose arguments recur at least three times once per
runner invocation through TOOL-dQuietDisk-7's template cache and copies it per call. So the suite
spends fewer git processes and fewer temp entries for the same arms with the same RED and GREEN
results.

### The saving, re-grounded at 7b8c737b0

- **Today:** a `build_ir_fixture` build costs 32 git processes and 105 temp entries, a
  `build_docs_fixture` build 30 and 95, and a `build_bg_fixture` build 19 and 157.
  figure: PINNED, measured 2026-11-22 at `7b8c737b0` by this spec's probe, each builder lifted out of
  the suite and run once under `GIT_TRACE2_EVENT`, its fixture counted with `find`, on
  `git version 2.54.0.windows.1`.
- **On the cache's clone:** a call keeps its push, because the clone drops the remote and carries
  none of the git-dir records the push writes. The clone's 3 git processes and a
  `config core.hooksPath` replace the work repository's `init`, two `config`, `add`, `commit` and
  `branch -M`, and the key costs 2 more, so the saving is none.
  figure: DERIVED from the argv list of one traced `build_ir_fixture` call.
- **On the cache's template, copied with its objects borrowed:** the four argument sets this unit
  templates spend at least 350 fewer git processes and at least 900 fewer temp entries at peak per
  run. The table in section 4 derives both bounds.
  figure: DERIVED from the per-call figures above and the copy's 55 entries, PINNED by the same
  probe.

## 2. Scope (IN)

- **S1** — Three builders split into a tree half and a call half: `build_ir_fixture`,
  `build_docs_fixture` and `build_bg_fixture` (`.githooks/pre-push.test.sh@a52afba8a1c3:1487`,
  `:2239` and `:2511`). The tree halves `build_ir_tree`, `build_docs_tree` and `build_bg_tree` take a
  fixture directory and a work directory and run today's body through its push, with `"$d/work"`
  or `"$BG_D/w"` read as the work directory. Each returns what today's builder returns at the same
  point: 1 at its `cd`, the push's status for `build_docs_tree`, and 0 for the other two, whose
  builders today end on a tail after the push. The call halves keep today's names and signatures and
  run today's tail. Observed by AC4.
- **S2** — One dispatcher, `build_pushed_fixture <dir> <work name> <tree fn> <arg>...`. Without
  `FX_TEMPLATE=1` on the call, or with the switch at `per-case`, it runs the tree half in place, which
  is today. With it, it copies the template of that tree half and those arguments into `<dir>`, as
  section 4 states. Observed by AC1, AC2 and AC4.
- **S3** — The template comes from unit 7's bash face, carried inline: `resolve_template_root` once,
  `derive_template_key <tree fn> fx-args "${FX_INPUTS[@]}"` and
  `resolve_template <root> <key> run_tree_in_stage <tree fn> <arg>...` once per argument set. The
  suite remembers each template path for the run, so a repeated set derives no key. Observed by AC1
  and AC3.
- **S4** — The copy borrows the template's objects. It copies every entry of the work tree, of its
  `.git` and of `remote.git` except the two `objects` directories, and gives each copy an
  `objects/info/alternates` line naming the template's, in the path form git reads. It then writes
  `core.hooksPath` and `remote.origin.url` to name the call's own directory. Observed by AC1 and AC2.
- **S5** — The 27 call sites in section 4's table opt in with `FX_TEMPLATE=1`, and no other site
  does. Observed by AC6.
- **S6** — The switch is unit 7's key `tests.fixture-templates`, read once in the prologue through
  the suite's own `$SRC/$KIT_REL/$PK/policy.py`, as `build_fixture` reads it
  (`tools/lib/lib-selftest.sh@4d0ce956a80b:180`): `per-case` is today, and anything else, an absent
  policy kit included, is `shared`. Observed by AC4.
- **S7** — The suite carries the `template_cache_sh` block byte-identical and sources no file under
  gov's lib directory, because the push-main kit ships it to adopters as a leg
  (`tools/govkit/entries/push-main.kit.toml@a1fe655815a4:98`). It already carries `resolve_python`
  and `refuse_wrong_shell` inline and calls `refuse_wrong_shell`, which unit 7's rev-6 asks of a
  suite carrying the block. Observed by AC5.
- **S8** — The shell-line ledger. `.githooks/pre-push.test.sh` grows past its row of 2459, so its
  key is widened through the ledger factory's door,
  `python tools/memory-tree/ratchet.py widen shell-role --key .githooks/pre-push.test.sh --reason <one line> --unit TOOL-dQuietDisk-12`,
  never by hand. The row equals the file's measured count at `7b8c737b0`, so the Reason names no base
  excess. Observed by AC7.
  figure: 2459 PINNED, `sh_hygiene.py --shell-role --measure`, 2026-11-22.
- **S9** — The arm set, every arm's verdict and the saving are observed on the whole suite, here and
  at an adopter fixture. Observed by AC8.

## 3. Non-goals (OUT)

- `build_sel_fixture` and `build_bp_fixture`: each builds its one repeated set twice, and a template
  built for two calls saves under 20 temp entries, inside the estimate's error. DERIVED from section
  1's per-call method, applied to their 128 and 143 entries.
- `build_pfx_fixture`: its repeated set is built three times, but its fixture holds 70 entries, and
  three copies and a template hold about 6 more than three builds. DERIVED by the same method.
- `build_vr_fixture` and `build_sg_fixture`: no argument set repeats.
- The suite's single-use inline fixtures, and the pushes the arms themselves make: each is the
  subject under test.
- `.githooks/pre-push` itself, and the push boundary's verdict and reuse rules (dWitnessedBar).
- The factory, its switch and its clone: TOOL-dQuietDisk-7. No factory file is written.
- A residue left by a killed run: the suite's `trap` removes `$tmp` with the templates in it, as it
  removes today's fixtures, and a killed run's leftovers are the owned swept root's,
  TOOL-dQuietDisk-9.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — `resolve_template_root`, `derive_template_key` and
  `resolve_template` as `tools/lib/template-cache.sh` defines them, and the policy key
  `tests.fixture-templates`. The suite ships with the push-main kit and is a leg at adopters, so it
  carries them inline.
- **hands-off** `TOOL-dQuietDisk-19` — the suite's before and after readings, if unit 19 takes them.

## 4. Design

### Where the code was read

Every citation is at `7b8c737b0` by symbol or as `<path>@<blob>:<line>`. No file under `.githooks/`
or `tools/` moved in `7b8c737b0..0318ce9c9`. Between `59e882afd` and `7b8c737b0` the suite added
`build_bp_fixture` and re-cut the call sites:
373 lines in, 14 out (PINNED, `git diff --stat`, 2026-11-22).

### What the cache can carry

A fixture here is three things under one directory: `hooks/pre-push`, a bare `remote.git` and a work
repository, whose `main` the builder has already pushed. The builder and its push leave git-dir
records the arms then read: `push-main-active`, `pre-push-allow`, `pre-push-bar`, the run log
`pushes.log` and `refs/remotes/origin/main`. The cache's `build_template_clone` gives a `--shared` clone with no
remote and none of those records (`tools/lib/template-cache.sh#build_template_clone`), so a call on
it would still init the remote, add it and push. The suite uses the cache's build, key and root, and
copies the template directory instead of cloning it.

`resolve_template` runs its builder in `<root>/.stage-<key>-<pid>/repo` and renames the whole stage
directory with `mv -T` (`tools/lib/template-cache.sh#resolve_template`). So `run_tree_in_stage` calls
the tree half with the stage as the fixture directory and `repo` as the work directory, and
`hooks/` and `remote.git` travel with the rename. The tree half commits its own tree, so the face's
`commit -m base` finds nothing to commit and passes on its `rev-parse` and `diff --cached` checks.

### The call half

```
FX_TEMPLATE unset, or the switch at per-case:
    <tree fn> <dir> <dir>/<work name> <arg>...                  today's commands, in place
FX_TEMPLATE=1, the first call of an argument set:
    printf the set's %q text into $tmp/fx-args
    key  = derive_template_key <tree fn> fx-args FX_INPUTS...    2 git, from a subshell in $tmp
    t    = resolve_template <root> <key> run_tree_in_stage <tree fn> <arg>...
    remember t and the two objects paths, in git's form, for the run
every FX_TEMPLATE=1 call:
    mkdir -p the copy's two objects/info and objects/pack
    cp -a hooks; the work tree but .git; .git but objects; remote.git but objects
    write each objects/info/alternates
    git -C <dir>/<work name> config core.hooksPath <dir>/hooks   1 git
    git -C <dir>/<work name> config remote.origin.url <dir>/remote.git   1 git
```

The entry lists are built with builtin globs, dotfiles included, so the copy spends four `cp` and one
`mkdir`, against the two `mkdir` and two `cp` today's builders spend. The call half then runs
today's tail: `cd`, and `IR_R=$(git rev-parse HEAD)` or `bg_gd=$(git rev-parse --git-dir)`, which is
one more git process for `build_ir_fixture` and `build_bg_fixture`.

`FX_INPUTS` lists the suite file, the hook, the four policy-kit files the ir and docs trees copy and
the `gate-fingerprint.sh` the bg tree copies, each under `$SRC`. The suite file stands for the
helpers the trees call, such as `write_ir_policy`, and for the green stub's text, whose definitions
`declare -f` of the tree does not read.

### Facts probed on the real tool

Each was checked in a scratch repository under the session scratch root on 2026-11-22, with
`git version 2.54.0.windows.1`:

- `git hash-object --no-filters --stdin-paths` refuses an MSYS path such as `/tmp/tmp.X/f` or
  `/c/projects/...` with `could not open`, and opens a `C:/...` path or a path relative to its cwd.
  `$SRC` is `git rev-parse --show-toplevel`'s output, in git's form, and the suite's `$tmp` comes from
  `mktemp -d` in MSYS form. So the key is derived from a subshell in `$tmp`, naming `fx-args`
  relative.
- An `objects/info/alternates` line in MSYS form is refused with
  `unable to normalize alternate object path`. The copy writes each line through the idiom
  `(cd <dir> && { pwd -W 2>/dev/null || pwd; })` (`tools/roles/adopt-roles.test.sh@c23a4909e9e0:222`).
- A copy made that way took a hooked push with the green stub, its `remote.git` `main` moved to the
  copy's `HEAD`, `git status --porcelain` printed nothing and `git fsck --connectivity-only` exited 0.
- The face's failed `commit -q -m base` writes `base` into `COMMIT_EDITMSG`. That is the one git-dir
  file a copy differs in, and the hook, the suite, `tools/run-gates/run-gates.sh` and
  `tools/push-main.sh` read it nowhere (`grep -c COMMIT_EDITMSG` prints 0 in each).
- `FX_TEMPLATE=1 f` in bash 5.3 sets the variable for the call of `f` alone.

### Inventory of the calls at 7b8c737b0

| Builder | Calls | Argument sets | Templated sets, calls |
|---|---|---|---|
| `build_ir_fixture` | 16 | 11 | `kit:own-mixed-contended` with `INHERITED_RED_MAX_AGE=10\n`, 6 |
| `build_docs_fixture` | 7 | 5 | `GATE_DOC_PATHS="notes/"\n`, 3 |
| `build_bg_fixture` | 22 | 4 | no second argument, 14; `$PM_DECL`, 5 |
| `build_sel_fixture` | 3 | 2 | none |
| `build_pfx_fixture` | up to 5 | 3 | none |
| `build_bp_fixture` | 4 | 3 | none |
| `build_vr_fixture` | 1 | 1 | none |
| `build_sg_fixture` | 2 | 2 | none |

A call inside a loop is counted once per iteration. The `$PM_DECL` set is `GATE_POST_MERGE=local\n`,
which the loop at `.githooks/pre-push.test.sh@a52afba8a1c3:2846` builds once more beside a single
`yes`, so that site stays per call.
figure: DERIVED from the call sites at `7b8c737b0`; the 29 repeated calls of section 1 are each
recurring set's calls less one, summed over the eight builders.

The 27 opted-in sites, at `.githooks/pre-push.test.sh@a52afba8a1c3`:

- `build_ir_fixture`: lines 1539, 1567, 1651, 1679, 1689 and 1698.
- `build_docs_fixture`: lines 2272, 2381 and 2392.
- `build_bg_fixture` with no second argument: lines 2578, 2626, 2673, 2739, 2765, 2781, 2794, 2803,
  2815, 2875, 2896, 2922, 2982 and 3009.
- `build_bg_fixture` with `$PM_DECL`: lines 2865, 2886, 2945 and 2966, the last a loop of two.

### The saving per templated set

| Set | Calls | Git today | Git after | Entries today | Entries after |
|---|---|---|---|---|---|
| ir, own-mixed-contended at 10 | 6 | 192 | 56 | 630 | 437 |
| docs, notes/ | 3 | 90 | 43 | 285 | 256 |
| bg, no second argument | 14 | 266 | 67 | 2198 | 1433 |
| bg, `$PM_DECL` | 5 | 95 | 40 | 785 | 614 |

A template costs its tree half, the face's 5 git processes and the key's 2, and holds a build's
entries plus `config-pins` and `ready`. A copy holds a build's entries less both objects directories
plus 8, which is 55 for ir as measured. The switch read adds 8 git processes per run. The sums are
437 fewer git processes less 8, and 1158 fewer entries less the root and `fx-args`, against the
bounds of 350 and 900.
figure: DERIVED from section 1's PINNED per-call figures; the switch read's 8 is PINNED, measured
2026-11-22 with `policy.py get tests.fixture-templates` under `GIT_TRACE2_EVENT`.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `build_ir_tree`, `build_docs_tree`, `build_bg_tree` | shell functions | `sh.function`, lexicon `--suggest` OK | AC4 |
| `build_pushed_fixture` | shell function | `sh.function`, lexicon `--suggest` OK | AC1, AC2 |
| `run_tree_in_stage` | shell function | `sh.function`, lexicon `--suggest` OK | AC3 |
| `FX_TEMPLATE` | per-call opt-in variable | none | AC6 |
| `FX_INPUTS` | array of key input files | none | AC3 |

### Files touched (estimate)

`.githooks/pre-push.test.sh` · `memory/project/shell-role.txt` · `memory/map/generated/symbols.json` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-12-widen-<n>.md`

The widen record's name is the door's: the day the pass runs it, and one past the highest widen
record in the build folder. The five new functions and the four the inline block defines are
column-0 definitions, so the codebase map's generator, run with `--write`, rewrites the symbol index.
No leg, kit or dossier is added, so no other generated map file moves.

### Shared paths at order 3

TOOL-dQuietDisk-28 names `memory/project/shell-role.txt` and `memory/map/generated/symbols.json`,
and TOOL-dQuietDisk-18 names `memory/map/generated/symbols.json`, as their specs stand at `HEAD`. So
this unit builds in sequence with both, and the later one regenerates the index and takes the next
widen number. TOOL-dQuietDisk-10 names only `tools/check-wiring.test.sh`, TOOL-dQuietDisk-6 is
WONTDO, and TOOL-dQuietDisk-13's spec at `HEAD` names only its three run-gates suites.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `build_template_clone` per call | It drops the remote and the push's records, so every call keeps its push: the saving is none. |
| `cp -a` of the whole template | It saves the git processes, but each copy holds the objects again, and the templates raise the peak by about 840 entries, DERIVED. |
| A suite-local template beside the factory | 28 fewer git processes, DERIVED, and no inline block, but a second instance of the kind the factory extracts (`[reuse]`). |
| Templating every call of the three builders | The 16 single-use calls would each pay a template and a copy, about 1,100 entries more, DERIVED. |
| Templating `build_sel_fixture` and `build_bp_fixture` too | Two calls per set save under 20 entries, for two more splits. |

Unit 13's suites copy fixtures too. If its re-ground copies a pushed fixture with borrowed objects,
that is the second instance, and the copy half moves into the factory in a unit of its own.

## 5. Production-readiness checklist

- security: N/A — no new write path; templates and copies land in the suite's own scratch or the
  bar's owned `$WORK`.
- perf / scale: at least 350 fewer git processes and 900 fewer peak temp entries per run, and 7
  fewer hooked pushes, all DERIVED from the section 4 table.
- error / empty / loading states: a failed key, template build or copy returns 1 from the builder,
  which every caller already reports as `could not build its fixture`.
- observability: `resolve_template` prints `template: <key8> built` once per templated set on
  stderr.
- risks: a copy's run log `pushes.log` start line names the template's stage path as `wt=`, which no
  arm reads, since the arms read their own push's END line. A detached `git maintenance run --auto`
  that the tree's commit or push starts could hold a stage file during the rename. The factory then
  says `could not place` and the call fails loudly. Two copies of one template share its commit id,
  where two builds differ by their timestamps. No arm compares an id across fixtures, and AC8's run
  observes it.
- testing: AC1 to AC7 are probes of this unit's code; AC8 runs the suite and is the main loop's.
- migration: N/A — templates live for one runner invocation.
- user docs: N/A — test fixtures; no `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — A probe under the session scratch root lifts the edited suite's prologue variables, its
  `write_ir_policy`, the three builders and tree halves, `build_pushed_fixture`,
  `run_tree_in_stage` and the `template_cache_sh` block out with `awk`. When it calls each of the
  four templated sets twice under `FX_TEMPLATE=1` with two tags and `GIT_TRACE2_EVENT` naming an
  empty directory, the second call adds at most 3 trace files, and at most 2 for
  `build_docs_fixture`. In each copy, `.git/objects` and `remote.git/objects` hold no loose object,
  each `objects/info/alternates` names the template's objects in `C:/` form, and
  `git fsck --connectivity-only` exits 0. `find <dir> | wc -l` prints fewer entries for the copy
  than for a call of the same set without `FX_TEMPLATE`.
  Red when: a repeated set rebuilds, a copy holds objects or an MSYS-form alternates line, or the
  call half spends more git than its two config writes and its tail's one read.
  figure: 3 and 2 DERIVED from the call half in section 4.
- **AC2** — When the same probe takes the reads below of a per-call build and of a copy, for each
  templated set, with `$d` replaced by a fixed token, the only difference is `COMMIT_EDITMSG`, `init`
  against `base`. The reads are `git for-each-ref --format='%(refname) %(objecttype) %(tree)'` and
  `git config --local --list` in the work repository and in `remote.git`, then `git ls-files -s`,
  `git rev-parse HEAD^{tree}` and `git status --porcelain` in the work repository. They also take
  the name of every entry outside `objects/`, and the bytes of every git-dir file but `index`,
  `logs/`, `refs/`, `pre-push-allow` and the run log `pushes.log`. A control over two per-call builds
  finds no difference. In each copy, a commit pushed with `GOV_GATE_CMD="bash $green"` lands: the
  copy's `remote.git` `main` equals its `HEAD`.
  Red when: a copy differs in a ref's tree, a config value, the index, the tree, the status, an entry
  name or an unmasked file, or its push does not land.
- **AC3** — When the probe calls `build_bg_fixture` with tags `a` and `b` and no second argument,
  then with `$PM_DECL`, stderr carries two `template: <key8> built` lines and no `reused` line, and
  `ls` of the root prints two key directories and no `.stage-*`. In a second shell, with `SRC`
  naming a scratch copy in which one byte of `.githooks/pre-push` differs, `derive_template_key`
  prints a different key for the same set.
  Red when: the tag enters the key, an argument is left out of it, a repeated set resolves again, or
  an input file's edit keeps the key.
- **AC4** — When the probe sets `_fx_mode=per-case` and calls each templated set under
  `FX_TEMPLATE=1`, the trace2 `start` events of each call carry the same git subcommands in the same
  order as the builder at the base, lifted with `git show` from `7b8c737b0`, for the same set, and
  no template root is made. With `$SRC/$KIT_REL/$PK/policy.py` absent, the suite's switch line sets
  `_fx_mode` to `shared`.
  Red when: `per-case` copies, or a split tree half runs a command today's builder did not.
- **AC5** — When the parity table's `blk` awk, copied out of the python resolver's suite, extracts
  `template_cache_sh` from `tools/lib/template-cache.sh` and from the edited suite, the two compare
  equal. `grep -nE '(^|[;&|] *)(\.|source) .*/lib/' .githooks/pre-push.test.sh` prints
  nothing.
  Red when: the inline copy drifts by a byte, or the suite sources a file under gov's lib directory,
  which no adopter holds.
- **AC6** — When `grep -c 'FX_TEMPLATE=1 build_' .githooks/pre-push.test.sh` runs, it prints 27, at
  the sites section 4 lists, re-found by their arm labels, and
  `grep -nE 'FX_TEMPLATE=1 build_(sel|pfx|vr|sg|bp)_fixture' .githooks/pre-push.test.sh` prints
  nothing.
  Red when: a site of a templated set is missed, or a single-use set opts in.
  figure: 27 DERIVED from the call sites at `7b8c737b0`.
- **AC7** — When `python tools/gate-lint/sh_hygiene.py --shell-role memory/project/shell-role.txt .`
  runs after the widen, it prints `sh-hygiene: OK`.
  `grep -n -P '^\.githooks/pre-push\.test\.sh\t' memory/project/shell-role.txt` prints one row ending
  `widened:<stem>`, and it is the only row `git diff -- memory/project/shell-role.txt` shows. The stem
  names a record under `memory/builds/dQuietDisk/build/` whose Keys field lists that path alone,
  whose Caused-by is `TOOL-dQuietDisk-12`, and whose Reason gives the lines this unit adds.
  Red when: the row is edited by hand with no record, or another row moves.
- **AC8** — The main loop runs the suite at the build base and at this unit's commit, each in a
  scratch `git clone --shared`. Each run has `GIT_TRACE2_EVENT` naming its own empty directory, and
  `TEMP`, `TMP` and `TMPDIR` naming an empty directory sampled every 0.5 s. Both runs print the same
  `ok` and `FAIL` lines. The trace files fall by at least 350 and the peak entries by at least 900,
  and the residual is 0 both times.
  Red when: a line changes, either count falls by less than its bound, or an entry remains.
  permission: a role pass may not run a `.test.sh` suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two whole runs of the suite, minutes each.
  figure: 350 and 900 DERIVED from section 4's table.
  fixture: the adopter half is a scratch target built from
  `tools/govkit/fixtures/release-0/deploy.toml`, whose `kits` name `push-main`, into which
  `python tools/govkit/govkit.py apply` at this unit's commit installs the shipped suite, where the
  main loop runs it. `python tools/govkit/govkit.py check --target C:/projects/incms/main` and
  `--target C:/projects/nicocares/main`, run read-only from gov, read the same before and after.

## 7. Gates

`pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `python resolver (behaviour + inline parity + idiom ban)` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `line length` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-push.test.sh · covers AC2 · after the first `FX_TEMPLATE=1 build_bg_fixture`, an arm reads `core.hooksPath` and `remote.origin.url` naming that call's own `$BG_D` and the remote's `main` equal to `HEAD`; its failing case is staged by dropping the two config writes from `build_pushed_fixture` · none

The bar runs once at the close. The suite's arms, the new one included, are observed by the main
loop, because a role pass runs no suite.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  3, section 4 and section 10 the call count of `build_pfx_fixture` is marked PINNED, the repeated-key
  count DERIVED from the call-site table, and dWitnessedBar's changed-line count PINNED. Design, scope
  and acceptance unchanged.
- rev-3 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §10 · S1 to S9 · AC1 to AC8 · re-grounded at 7b8c737b0
  (orders 1 and 2 built), under `2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task`. The suite moved
  since `59e882afd`, as section 4 counts, and every citation is re-pinned to blob `a52afba8a1c3`.
  The cache as built hands out clones with no remote, so the copy is of the template directory, and
  it borrows the template's objects through `alternates`, because a whole `cp -a` raised the peak
  entries the re-ground task requires to fall. `build_sel_fixture` leaves scope, each set saving
  under 20 entries in two calls, and `build_pfx_fixture` and the new `build_bp_fixture` stay out for
  the same counts. The call sites opt in per site, since 16 single-use calls would cost more than
  the saving. The saving is re-taken by a probe: at least 350 git processes and 900 peak entries,
  against the 168 git processes derived before. The key's inputs are named in git's path form after
  a probe found `hash-object --stdin-paths` refusing MSYS paths. The shell-line widen joins scope,
  and the shared paths with units 18 and 28 are named. The goal is unchanged.

## 10. Reuse audit

The seam is TOOL-dQuietDisk-7's bash face, `tools/lib/template-cache.sh#resolve_template`, with
`resolve_template_root` and `derive_template_key` beside it.
`python tools/codebase-map/reuse_lookup.py "copy a pushed fixture repository with its bare remote from a template built once"`
ranked `resolve_template` as a SEAM, with fan-in 3, beside `build_fixture`. The cache's clone does not
fit this suite, because it keeps no remote. For the copy that borrows objects, no existing seam
fits: every alternates file under `tools/` is written by `git clone --shared`
(`tools/govkit/matrix.py`, `tools/govkit/upgrade_walk.py`), and none copies a git directory beside
its pushed bare remote.

Chain owner: dWitnessedBar (Test). It landed in the merge `40def53f7`, which this base holds, so the
unit builds on its landed tip. The suite is a dWitnessedBar subject: its builders gained
`build_bp_fixture` and the sites re-cut in `59e882afd..7b8c737b0`. Nothing here changes a verdict
rule of theirs.

Recall terms used: `python tools/memory-recall/query.py "pre-push suite fixture built once from a template and copied with alternates" --terms "pre-push.test.sh build_bg_fixture build_ir_fixture build_docs_fixture resolve_template derive_template_key template-cache alternates remote.git hooksPath cp -a"`
