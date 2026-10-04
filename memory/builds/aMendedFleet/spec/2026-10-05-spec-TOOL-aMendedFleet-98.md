# TOOL-aMendedFleet-98 — held-red C2: a Python suite's `bash` resolves to Git-Bash, never the System32 WSL launcher

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · advances TOOL-dUnstalledConvoy-15 · order 99

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The daily held job's `lexicon selftest` is red on cause C2 of unit 7's census
(`memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md`): 22 of
its 789 arms fail with the WSL launcher's "no installed distributions" message. `tools/lexicon/selftest.py`
spawns the bare name `bash`, Windows process creation resolves that from System32 before PATH, and
the hosted runner has the WSL launcher there and no distribution behind it. This unit makes the suite
name the bash that shares its filesystem, and refuse by name when there is none, so it passes on the
runner and stops depending on whether a host happens to have WSL installed.

## 2. Scope (IN)

- **S1** — `tools/lexicon/selftest.py` gains `resolve_bash()`. It takes `GOV_BASH` when set, else
  walks PATH for `bash.exe` or `bash`, skipping any candidate under System32 or WindowsApps, and
  accepts a candidate only when it can `test -f` this selftest file by its POSIX-spelled absolute
  path. The result is bound once, at module level, before the first arm. Observed by AC2, AC3, AC4.
- **S2** — When no candidate is accepted, or `GOV_BASH` is set and fails that probe, `resolve_bash()`
  itself raises `SystemExit` with status 2 and one stderr line naming what it tried and `GOV_BASH` as
  the remedy, so the suite stops before its first arm. It never falls back to the bare name. Observed
  by AC2 and AC3.
- **S3** — Each of the 11 `subprocess.run` calls in `tools/lexicon/selftest.py` whose argv opens with
  the bare `bash` opens with the S1 executable instead. Observed by AC1 and AC5.

## 3. Non-goals (OUT)

- `tools/govkit/selftest.py`'s 53 `["bash"` tokens, which the census left unobserved. Read
  2026-10-05: each sits inside a descriptor or manifest string the fixture writes, or in an argv the
  arm compares, and `tools/govkit/govkit.py` runs such an argv through `resolve_shell_argv`, which
  rewrites a leading bare `bash`. None is passed to `subprocess` directly.
- A source-level gate for the class. `memory/gotchas/subprocess-resolves-a-different-shell.md` records
  that it has no signature worth banning, and the open ask `TOOL-dUnstalledConvoy-15` asks for a rule
  routing every python-side execution through one seam. This unit fixes its lexicon instance, the
  only direct bare spawn left in tracked Python (§4), and leaves the rule to that ask.
- One shared resolver. The lexicon kit is copy-installed and names nothing outside itself, which is
  why `tools/runlog/selftest.py`, `tools/memory-tree/corpus_ids.py` and `tools/govkit/govkit.py` each
  carry their own copy. Which probe the copies share is the open ask `TOOL-dSettledRoster-6`.
- That gotcha's "THREE copies" sentence, already stale before this unit adds one.
- Moving the lexicon kit version; the build moves every kit version it owes once, after the last pass
  touching that kit, and the close's `kit epoch` leg grades it.

### Edges

none

## 4. Design

### Evidence

Read 2026-10-05 on node a at HEAD `34a99ad17`, whose `tools/lexicon/selftest.py` equals base
`7af5f564`.

- `git grep -n -E` for a `subprocess` call whose argv literal opens with `"bash"`, over every tracked
  `tools/` and `skills/` Python file, prints 11 lines, all in `tools/lexicon/selftest.py`: ten run
  `adopt-lexicon.sh` or a fixture script and one runs `bash -c` over a grep.
- Node a has `C:/Windows/System32/bash.exe` and a WSL distribution. A Python
  `subprocess.run(["bash", "-c", ...])` there runs WSL's `/bin/bash`, measured. The suite is green on
  node a only because that distribution maps the working directory under `/mnt/c/`; the runner has the
  launcher and no distribution, so the same call prints the "no installed distributions" message the
  census quotes, mostly in UTF-16.
- `tools/runlog/selftest.py`'s `resolve_bash()` is the closest existing shape: a suite-local copy, a
  PATH walk skipping System32 and WindowsApps, a candidate accepted when it runs `-c :`. The open ask
  `TOOL-dSettledRoster-6` records that `tools/run-gates/profile_bar.py` probes the stronger property,
  whether the bash can SEE the script. S1 takes that property: a WSL bash with a distribution starts
  fine and cannot see a `C:/` path.
- The refusal shape follows `tools/memory-tree/corpus_ids.py`: a set and unusable `GOV_BASH` is a
  named failure, never a fall-through.

### Mechanism

`resolve_bash()` runs each candidate with `-c`, the script `test -f "$1"`, and this file's absolute
path spelled with forward slashes as `$1`, with output captured and no text decode, and returns the
first candidate exiting 0. It uses only `os`, `pathlib`, `subprocess` and `sys`, which is what lets
§6 observe it alone. The module binds `BASH` once, immediately after `PFX`, so the probe mode that
stops after the first arm still exercises it. The name leads with the declared verb `resolve`, whose
`.lexicon.conf` gloss is to run the candidate where that is the only proof.

### The resolver fixture

§6 observes `resolve_bash()` alone, without running the suite: this executes only that function's
definition out of the suite's source, with the four modules it uses supplied, and calls it. At base
the function does not exist and the fixture ends on a `KeyError`.

```bash
python -c 'import ast, os, pathlib, subprocess, sys
p = "tools/lexicon/selftest.py"
fn = [n for n in ast.parse(open(p, encoding="utf-8").read()).body if getattr(n, "name", "") == "resolve_bash"]
g = {"__file__": os.path.abspath(p), "os": os, "pathlib": pathlib, "subprocess": subprocess, "sys": sys}
exec(compile(ast.Module(fn, []), p, "exec"), g)
print(g["resolve_bash"]())'
```

### Files touched (estimate)

- `tools/lexicon/selftest.py`

### Alternatives rejected

- **`shutil.which("bash")`.** It may report Git-Bash while the loader still runs System32's launcher,
  the gotcha's own warning, and it accepts a launcher without running it.
- **Falling back to the bare name when nothing resolves.** That is the defect itself, made silent.
- **PATH reordering in the workflow.** The loader searches System32 before PATH, so no
  PATH order fixes it, and the bug would stay on every adopter host with WSL installed.

## 5. Production-readiness checklist

- security — N/A: a test suite choosing which local shell runs its fixtures; `GOV_BASH` is the
  operator's own override, as in three other kits.
- perf / scale — one probe spawn per PATH candidate, once per suite run.
- error / empty / loading states — S2's refusal is the empty state, exit 2 with a named remedy.
- observability — the refusal line names every skipped launcher and the override.
- risks — a host whose only bash cannot see the tree now refuses where it used to run some arms under
  the wrong filesystem; that is the intended change.
- testing — AC2 and AC3 stage the two refusals through §4's fixture; AC4 observes the resolver
  accepting Git-Bash on a node whose bare name is the WSL launcher.
- migration — none.
- user docs — N/A: no operator-facing surface changes beyond the refusal line.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -F '["bash"' -- tools/lexicon/selftest.py` runs, it prints nothing and
  exits 1.
  Red when: any spawn still opens with the bare name; at base it prints 11 lines, measured 2026-10-05.
- **AC2** — When §4's resolver fixture runs with PATH holding only Git's `cmd` directory, which
  carries `git` and no `bash`, it exits 2 and its stderr names `GOV_BASH`.
  Red when: a resolver that falls back to the bare name prints `bash` and exits 0; at base the fixture
  ends on a `KeyError` because no `resolve_bash` exists.
  fixture: the interpreter is invoked by absolute path, since that PATH holds no python.
- **AC3** — When §4's resolver fixture runs with `GOV_BASH` set to the System32 launcher's path, it
  exits 2 and its stderr names that path as an override that cannot see the tree.
  Red when: the override is taken on a run-only probe; node a's launcher has a WSL distribution behind
  it and starts, so only the `test -f` probe refuses it.
  fixture: node a, measured 2026-10-05 to run WSL's `/bin/bash` for a bare `bash` spawn.
- **AC4** — When §4's resolver fixture runs on node a with its ordinary PATH, it exits 0 and prints a
  path under Git's install directory, never one under System32 or WindowsApps.
  Red when: it prints the bare name or a launcher path, or refuses although node a's PATH lists
  Git's `usr/bin` ahead of System32, measured 2026-10-05.
- **AC5** — When the first scheduled remote CI run after landing completes,
  `gh run view <id> --repo d41ly/coding-governance --log-failed` carries no line of the
  `held lexicon selftest` job naming the Windows Subsystem for Linux.
  Red when: any lexicon arm still reaches the WSL launcher on `windows-latest`.
  permission: observable only after the landing push, which the close performs.
  cost: one day, the schedule's period.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)`

No new arm: AC2 and AC3 stage the refusals directly, and the held job on `windows-latest` is the
suite-level observer.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft; the 11 bare spawns counted over every tracked Python file, and
  the census's unobserved govkit instance read and found to be descriptor data.

## 10. Reuse audit

The seam is the `resolve_bash()` shape `tools/runlog/selftest.py` carries suite-locally, with the
see-the-file probe of `tools/run-gates/profile_bar.py` and the override refusal of
`tools/memory-tree/corpus_ids.py`. A copy, not an import: the lexicon kit is copy-installed and names
nothing outside itself. `python tools/codebase-map/reuse_lookup.py "resolve the git-bash executable
instead of the windows wsl launcher before spawning a shell script"` listed `resolve_bash` in
`tools/govkit/govkit.py`, `tools/memory-tree/corpus_ids.py`, `tools/run-gates/profile_bar.py` and
`tools/runlog/selftest.py`, and missed `tools/settings-merge.py`'s nested one, found by grep. The
recall query returned the gotcha, the open asks `TOOL-dUnstalledConvoy-15` (this exact lexicon
instance) and `TOOL-dSettledRoster-6` (probe strength), and the aGradedDialect precedent of a named
refusal with no fallback.

Recall terms used: resolve_bash GOV_BASH WSL launcher System32 WindowsApps git-bash subprocess bare name lexicon selftest
