# KICK-dKeptSession-36 — the transition guard runs the driver through a bash that shares this filesystem, never the bare name, and an unresolved shell refuses

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-36-deviation-361.md](../build/2026-10-26-build-KICK-dKeptSession-36-deviation-361.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 22 at HIGH**, report item **H4**, which no other id shares.

`KICK-dKeptSession-5` S9 has `write_transition`, a Windows python, run bare `bash
<prefix>/unattended/unattended.sh --mail read`. On this node the bare name reaches the WSL launcher,
which sees another filesystem, so the driver path does not resolve and S9 passes "an absent driver"
with a NOTE: the guard passes with open mail and certifies a check it never ran. The class is
recorded in `memory/gotchas/subprocess-resolves-a-different-shell.md`. This unit gives the loop kit
one resolver that runs each candidate, routes the guard through it, and makes "absent driver" a
Python file test rather than a shell's failure. It repairs `KICK-dKeptSession-5` and builds one step
after it (order 17).

## 2. Scope (IN)

- **S1** — id 22. The resolver, `resolve_bash()` in `tools/loop/loop_lib.py`, the contract of
  `tools/govkit/govkit.py:1144` carried inline because the loop kit is copy-installed: `GOV_BASH`
  first, a set but unusable value raising `LoopError` by name; then the candidates, the
  `C:/Windows/System32` and `WindowsApps` launchers refused; a candidate accepted only once
  `<cand> -c :` exits 0 and, on a Windows host, `uname -s` answers `MINGW` or `MSYS`. No candidate
  raises `LoopError`, never a fall-back to the bare name. Observed by AC1 and AC2.
- **S2** — id 22. The guard's argv. `KICK-dKeptSession-5` S9's step runs `[resolve_bash(), <driver>,
  "--mail", "read", <slug>, "--open"]`, `<driver>` an absolute path. Observed by AC3.
- **S3** — id 22. Absent is a file test. The guard passes as "an absent driver" only when
  `os.path.isfile(<driver>)` is false, tested in Python before any spawn. A present driver with no
  usable shell refuses with exit 2, `refused — <slug> · mail unknown: <the LoopError's why>`, and
  writes nothing. Observed by AC4.
- **S4** — id 22. `KICK-dKeptSession-5` S9's bare `bash` is superseded by name here, and that unit's
  acceptance ledger answers its AC5 and AC6 through AC3's argv. Observed by AC3.

## 3. Non-goals (OUT)

- The guard's other exits, a non-zero read with no rows among them: id 59, item M26, batched into
  `KICK-dKeptSession-44`.
- The position engine's own reads, `--claims` and `--mail read`: ids 23 and 24, items M13 and M14,
  batched into `KICK-dKeptSession-44`, which call this resolver.
- One resolver in `tools/lib` for every kit, `cl-dClosedLoop-0364`'s: another build's clause. This
  copy keeps govkit's contract so that extraction replaces it unchanged.
- The report's left-shift lint over `subprocess` argv. No clause of this build names it.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S9's transition guard in `write_transition`, whose bare `bash` launch this unit replaces (id 22)
- **hands-off** `KICK-dKeptSession-44` — `resolve_bash` in `loop_lib.py`, which the position engine's mail and claims reads take for ids 23 and 24
- **hands-off** `KICK-dKeptSession-42` — `resolve_bash`, through which the consuming step posts its `--mail ack`
- **hands-off** `KICK-dKeptSession-56` — `resolve_bash`, its override and §3's parity claim, and §7's legs, the batch's S3 to S6, S27, S44 and S42 (ids 5, 6, 23, 52, 36, 53, 41)

## 4. Design

### Evidence

- The audit's probe from Windows python: `subprocess.run(['bash','-c','uname -a; pwd'])` printed
  `microsoft-standard-WSL2` and `/mnt/c/projects/...`, while `shutil.which('bash')` named git-bash
  and `C:/Windows/System32/bash.exe` exists.
- `govkit.py:1144-1160` records the same measured failure and accepts a candidate only once it runs;
  the gotcha `memory/gotchas/subprocess-resolves-a-different-shell.md` names the remedy.
- Eight kits already carry a `resolve_bash` (`git grep -n "def resolve_bash" -- tools`): govkit,
  corpus_ids, handoff, profile_bar, regen and three selftests, with a nested
  one in `tools/settings-merge.py`.
- `KICK-dKeptSession-5` S9: "`mail — off`, an absent driver and zero rows each pass" (spec-5 S9).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_bash` | function, `tools/loop/loop_lib.py` | `py.function`, `resolve`, OK |

### Migration

None: the guard is new in `KICK-dKeptSession-5`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`: `resolve_bash`
- `tools/loop/loop_transition.py`: S2 and S3 in the guard
- `tools/loop/selftest.py`: the cases of §6

### Alternatives rejected

- **`shutil.which("bash")`.** It names a path that exists, which is not evidence it runs on this
  filesystem; govkit's docstring records the same mistake for the python stub.
- **Importing govkit's resolver.** govkit is copy-installed as a standalone directory, and the loop
  kit cannot reach it.

## 5. Production-readiness checklist

- security — the shell is chosen by running it, and `GOV_BASH` is honoured only when it runs.
- perf / scale — one or two short probe spawns per process, cached in a module global.
- error / empty / loading states — no usable shell refuses the transition as unknown, never as none.
- observability — the refusal names the `GOV_BASH` value or the candidates tried.
- risks — a host with only a WSL bash cannot transition; that is the intended refusal.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`'s guard paragraph (`KICK-dKeptSession-5` S14) names `GOV_BASH`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import loop_lib; print(loop_lib.resolve_bash())"` runs in the loop kit on
  this node, it prints an absolute path whose `uname -s` answers `MINGW` or `MSYS`, and never the
  Windows `System32` bash, the WSL launcher.
  Red when: the resolver returns the bare name or the WSL launcher.
- **AC2** — When `GOV_BASH` is set to the Windows `System32` bash, the WSL launcher, for that probe,
  it raises `LoopError` naming `GOV_BASH`.
  Red when: an unusable override falls through to another candidate.
- **AC3** — When the selftest records the guard's subprocess argv over a fixture build, `argv[0]` is
  `resolve_bash()`'s path and `argv[1]` the driver's absolute path.
  Red when: `argv[0]` is `bash`, as a copy of the base guard shows.
- **AC4** — When the selftest runs the guard with the driver file removed, it passes with the NOTE;
  with the driver present and `GOV_BASH` planted unusable, it exits 2 printing `mail unknown` and
  writes no transition.
  Red when: a present driver with no usable shell passes as absent.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC2 AC3 AC4 · the guard's recorded argv, the driver removed and an unusable `GOV_BASH`, staged red by a copy of the guard launching bare `bash` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H4 (id 22).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam is govkit's `resolve_bash` (`tools/govkit/govkit.py:1144`), whose contract this unit copies
into the loop kit because copy-installed kits carry shared primitives inline (the charter's Kinds
fact). `python tools/codebase-map/reuse_lookup.py "resolve the bash that shares this filesystem by
running each candidate"` ranked `resolve_bash` across eight files, `resolve_kit_dir` and
`resolve_python`; `resolve_bash` is the seam named, and `tools/lib` holds no bash resolver at this
base for the kit to inline instead.

Recall terms used: `python tools/memory-recall/query.py "how does a Windows python run bash without
reaching WSL" --terms "resolve_bash GOV_BASH WSL System32 bash.exe git-bash candidate runs uname
transition guard subprocess"`
