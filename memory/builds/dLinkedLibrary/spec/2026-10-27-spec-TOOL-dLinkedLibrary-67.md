# TOOL-dLinkedLibrary-67 — `--observe` resolves a leading bash and python before it runs an observed argv

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 8 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-67-deviation-671.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-67-deviation-671.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 2 at HIGH**, report item **H2**. No other id shares the item. Item M4 (id 12) is the same
defect at medium, and item M5 (id 42) its nested half, both batched in `TOOL-dLinkedLibrary-74`.

`TOOL-dLinkedLibrary-61` AC1 plants `bash -c 'python -c "…"; true'` and leaves the leading `bash`
unresolved, deferring that to `TOOL-dLinkedLibrary-64` S6 at order 29, while 61 runs at order 7. On a
Windows node with WSL installed, `Popen` resolves a bare `bash` to the System32 WSL launcher: the audit's
`subprocess.run(['bash','-c','uname -s'])` printed `Linux`, which is why `tools/run-gates/regen.py:273-279`
rewrites the name. At 61's own pass the grandchild then runs inside WSL, its pidfile holds a Linux pid,
and the Windows-side liveness check certifies a tree kill it never observed.

This unit lands the resolution in `--observe` itself, at the step after 61, and builds the
`observe-tree-hang` plant so no interpreter in it resolves through `PATH`. It repairs
`TOOL-dLinkedLibrary-61` and builds one step after it (order 8).

## 2. Scope (IN)

- **S1** — The resolver. `resolve_observed_argv(argv)` in `tools/memory-tree/gotchas.py` returns a copy
  whose first element is `corpus_ids.resolve_bash()` when it is `bash`, and `sys.executable` when it is
  `python` or `python3`, every other element unchanged; `corpus_ids` is reached the way the module
  already reaches it, by file path beside it (`tools/memory-tree/gotchas.py:146-158`). `resolve_bash` is
  called once per `--observe` call and its answer reused for both runs. Where it raises `Problem`, no usable
  bash on `PATH`, the run records what `TOOL-dLinkedLibrary-49`'s table reads for a run that cannot start,
  with the `Problem`'s text. Observed by AC1.
- **S2** — The call site. `--observe` passes each clean and planted argv through `resolve_observed_argv`
  before the `Popen` of 61 S2, so no observed run starts from a bare `bash` or `python`. Observed by AC1
  and AC2.
- **S3** — The plant. The `observe-tree-hang` selftest case (61 AC1) builds its planted argv as `["bash",
  "-c", "<python> -c \"…\"; true"]`, `<python>` being `shlex.quote` of `sys.executable` written with
  forward slashes, so the leading `bash` is S1's to resolve and the grandchild names its interpreter by
  path. Observed by AC2.

## 3. Non-goals (OUT)

- The tree kill, the file-routed output and the parity row: `TOOL-dLinkedLibrary-61` S1 to S3, unchanged.
- The `observe-bash-led` refusal case and the verdict spellings: `TOOL-dLinkedLibrary-64` S6 and S17;
  S6 re-observes this unit's resolver rather than adding a second.
- The pidfile's presence and the grandchild's visibility from the observer: `TOOL-dLinkedLibrary-74`'s
  items for ids 42 and 12.
- `regen.py`'s `run_command`: unchanged; its resolution is the precedent, not a callee.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-61` — S2's observed `Popen` and AC1's `observe-tree-hang` plant, which S2 feeds resolved argv and S3 rebuilds (id 2)
- **hands-off** `TOOL-dLinkedLibrary-64` — `resolve_observed_argv`, which S6 and AC5 re-observe rather than land a second resolution (id 2)
- **hands-off** `TOOL-dLinkedLibrary-74` — the `observe-tree-hang` plant, whose pidfile unit 74 checks (ids 12, 42 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-80` — `resolve_observed_argv` and the `observe-tree-hang` plant, which unit 80 completes (ids 43, 15, 37, 20, 3 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- `tools/memory-tree/corpus_ids.py:390-398`: `resolve_bash()` returns "the bash that shares THIS
  filesystem", skipping a candidate under `System32` or `WindowsApps` and accepting one only if it runs,
  `GOV_BASH` overriding; with none usable it raises `Problem` (:433).
- `tools/run-gates/regen.py:273-279`: `run_command` maps a leading `python` or `python3` to
  `sys.executable` and a leading `bash` to `BASH` or `shutil.which`, measured on node `a` against the WSL
  `bash` in the system directory.
- `tools/memory-tree/gotchas.py:146-158`: the module loads `corpus_ids.py` with
  `importlib.util.spec_from_file_location`, so no import path is added.
- `tools/memory-tree/kit.toml:7`: the memory-tree kit requires no other kit, so the resolver is the
  kit's own `resolve_bash` and never `regen.py`'s.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`: S1 to S3, and the `observe-resolves` selftest case

### Alternatives rejected

- **Leaving the resolution to unit 64 at order 29.** Every pass from 61 to 64 certifies a kill on a
  WSL node that it never observed.
- **Calling `shutil.which("bash")` as `regen.py` does.** The kit already owns a resolver that runs each
  candidate, and a second rule in the same kit is the duplicate the charter's reuse rule refuses.

## 5. Production-readiness checklist

- security — the resolved names are the kit's own bash and the running interpreter; nothing new reaches
  the observed argv.
- perf / scale — `resolve_bash` runs its candidates once per `--observe` call, S1.
- error / empty / loading states — a resolver `Problem` reads as a run that could not start, naming it.
- observability — a run past its bound prints the resolved first element beside its output tail.
- risks — a node whose only bash is WSL's now records the cannot-start reading, where it used to run
  the leg under another filesystem.
- testing — AC1 by probe, AC2 by the module's selftest case.
- migration — none.
- user docs — none under `help/`: `memory/HYGIENE.md`'s `--observe` sentence (unit 49 S4) already names
  the run.

## 6. Acceptance criteria

- **AC1** — When `python -I -c` loads `gotchas.py` by its path and calls `resolve_observed_argv` on
  `["bash", "-c", "true"]`, `["python3", "x.py"]` and `["git", "status"]`, the first result's head equals
  `corpus_ids.resolve_bash()`, the second's equals `sys.executable`, and the third is returned unchanged.
  Red when: a bare `bash` or `python` reaches `Popen`.
- **AC2** — When `python tools/memory-tree/gotchas.py --selftest` runs its `observe-resolves` and
  `observe-tree-hang` cases on node d, the first prints `ok` with the resolved head not under the
  `System32` directory, and the second returns within 5 seconds recording `unobservable: past 2s`.
  Red when: the planted bash resolves to the WSL launcher, or the grandchild is a bare `python`.

## 7. Gates

`gotchas selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC1 AC2 · the `observe-resolves` selftest case, the failing case staged by an `--observe` that passes the argv to `Popen` unresolved · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 24 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 2 (HIGH, item
  H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seam extended is the memory-tree kit's `resolve_bash` (`tools/memory-tree/corpus_ids.py:390`),
reached through the module's existing file-path load of `corpus_ids.py`, with `regen.py`'s
`run_command` as the precedent for the python half. `python tools/codebase-map/reuse_lookup.py "resolve
the bash executable that shares this filesystem before running an argv"` ranked `resolve`, `before`,
`resolve_kit_dir`, `resolve_caps` and `resolve_prefix_token`, each a name-stem match; it missed
`resolve_bash`, found by reading `corpus_ids.py`, and that miss is recorded here as M5 asks.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
