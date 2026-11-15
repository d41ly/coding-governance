# Brief — aLightenedLoop: per-unit overhead cut, verdicts unchanged

**Serves:** research TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5

## The prompt

> Open a new build, suggested slug `aLightenedLoop`, which is free at `main` 846d51d39; mint it by the kickoff's own rules. It covers the five overhead fixes below.

> Every fix MUST leave each check's verdict, refusal text and rendered byte exactly as they are. Each unit's acceptance proves that parity: the same verdicts and bytes before and after on the real tree, plus the new timing, measured.

> Done means: the build folder and the four specs committed through `/build`, with READY → go, the units built, the closing review and the bar run, then the owner asked to land.

## The brief

### Goal
Cut the fixed per-unit overhead that dominated dSafePassage (a median builder spent 9.6 of 17.6 min before its first product edit and 5.1 after its last) without moving any check's verdict, refusal text or rendered byte. The measurements, with the line numbers and the profile behind each fix, are in `memory/builds/aLightenedLoop/build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md`.

### Items
1. TOOL-aLightenedLoop-1, the commit tail: `gen_build_index.py` writes only the files whose bytes changed; an input-hash cache lets `--check` right after `--write` answer without a re-render; check 9's `--staged` skip admits a modify-only records edit under a build's `build/` folder that moves no header, binding or cited id (today `check_index_input`, `tools/memory-tree/gen_build_index.py@5a0864b8:927`, classes every such path as structural); and check 29's `--check-coverage --staged` exits early when no staged spec is an INPROGRESS chain spec.
2. TOOL-aLightenedLoop-2, the idle-wake tick: one cheap tick verb prints a healthy line in about 1 s and the model ends its turn, with `--resume`/`--audit` only on a non-healthy verdict; and a longer cadence while a tracked task is registered (`--register-task`), restored when it unregisters. Hang detection stays as it is. <!-- PINNED 2026-11-14 -->
3. TOOL-aLightenedLoop-3, `--dispatch`: the harness or main loop runs `--dispatch` before spawning the builder (`tools/workflows/unattended-unit.js@71852dc0:264` today has the builder run it); the spec-token cache keys on the hashes of the files the checker reads, not HEAD (TOOL-aSmoothedDispatch-4 S2); and the check is scoped to the dispatching build where the cross-build joins are shown not to move.
4. TOOL-aLightenedLoop-4, divergence rework: a feasibility-first step in the builder brief (`unattended-unit.js`, `gov-builder.agent.md`) that probes every spec claim about current code and diverges within about 10 min; spec writers cite the file:line each claim about current code was checked against (`gov-spec-writer.agent.md`, `memory/TEMPLATE-SPEC.md`); and a template rule that a spec touching a manifest-watched file lists the manifest and its `last-audit` re-stamp in files-touched.
5. TOOL-aLightenedLoop-5, the stop-guard: `tools/unattended/stop-guard.js` caches the `--liveness` verdict, keyed by the run-state file's mtime plus HEAD, and expires the entry before the soonest time the verdict could change on its own (the liveness clock), so a STALE flip is never served from cache.

### Acceptance
Per unit: the touched checks run on the real tree before and after, with identical exit codes, refusal text and rendered bytes (a diff of the captured outputs is empty), plus a wall-clock timing before and after on node `a`, recorded beside the instrument. Unit 4 changes prompts only: its acceptance is the rendered handoff bytes plus the role-render parity gates, and its timing is not measurable within the build.

### Gates
The full merge bar, `bash tools/run-gates/run-gates.sh`, with legs from `tools/gate-legs.json`; and, for the `tools/unattended/` units, `bash tools/unattended/run-unattended-gates.sh --pooled`.

### Non-goals
No change to what any check grades, its refusal text or its rendered bytes. No new gate leg. No kit-version moves except through the lander's mint. No edits under `memory/builds/dDeclaredLoop/` or its run branch.

### Limitations
The DEFERRED chain units dWellOiledMachine-28 (the unattended kit dissolved into a runtime kit, moving `stop-guard.js` and the tick) and -10/-21/-31/-64 (hook packs over stop-guard) touch the same files: this build lands first and those specs re-ground on it. The live run on `branch/unattended-declared-loop-d56bf0` has changed `unattended.sh` and the hygiene script (TOOL-dDeclaredLoop-5 and -23), so expect a reconcile. Hooks are never bypassed. Landing and pushing need the owner's explicit ask.

### Reuse
`reuse_lookup.py` named no caching seam that fits. The nearest seams are `derive_spec_token_key` plus run-gates' `gate-fingerprint.sh` (the existing dispatch cache), `check_staged_render` / `check_index_input` (the aTrimmedHook-1 classifier), and `runLiveness` in `stop-guard.js`. The recall query returned TOOL-aSwiftRefusal-1, TOOL-aSmoothedDispatch-4, TOOL-dDerivedDocket-61, TOOL-aOrientedCast-4 and the aWokenSentinel / aSparedHolder keepalive records.

## Drawn from the session

> The goal is speed with identical verdicts: any change that alters what a check grades is out of scope.
— agent (the session that started this one), its handoff background

> Fix 1 scope: Write only changed bytes, Input-hash cache, Narrow check 9's staged skip, Short-circuit check 29 · Fix 2 shape: Both · Fix 3 scope: Dispatch before the spawn, Key the cache on input hashes, Scope to the unit's build · Fix 4 scope: Builder feasibility-first, Spec writer verifies claims, Re-stamp rule in template · Unit roster: Five units, one per fix · Spec audit: No audit
— owner, kickoff fork answers, 2026-11-14

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: Go
