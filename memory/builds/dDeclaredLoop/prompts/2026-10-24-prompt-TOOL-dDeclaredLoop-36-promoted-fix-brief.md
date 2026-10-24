**Serves:** research TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56

# Promoted-fix brief — the round-1 promotions, before their commit

Fix the twenty-one specs the round-1 spec audit's disposal added, `TOOL-dDeclaredLoop-36` to `-56`, so
`python tools/check-spec-tokens.py` names no dDeclaredLoop spec and `bash tools/memory-tree/check-memory-hygiene.sh
--only 12,25` prints no dDeclaredLoop line, changing nothing else.

- Each `[path]` hit below: cite a file the build run will create by BASENAME in §6, full paths staying in §2, §4 and
  Files touched, as earlier spec runs did; correct a path that is simply wrong. `.governance/policy.toml` is
  dGroundRules' file, created by its build run: cite it in §6 as "the policy file" or by basename.
- The `[guards]` hit on `TOOL-dDeclaredLoop-56`: §4 names `.claude/skills/unattended/SKILL.md`, which trips the
  guard of the leg `check-wiring self-test`; add that leg to its §7 leg line, or drop the path from Files touched
  if the unit does not write it.
- Each check-12 hit (an acceptance bullet naming no backticked witness): give the bullet the backticked command or
  file that observes it.
- Each check-25 hit (a §2 item that retires a named thing): add a `**Readers:**` clause, `by name:` every reader
  that spells the name (each found by `git grep -n` at HEAD) and `by value:` its value's readers or
  `NO VALUE READERS` and a reason; or, where the item retires nothing, reword it so it no longer reads as a
  retirement. The passing clauses in `TOOL-dDeclaredLoop-7`, `-11` and `-21` show the shape.
- `TOOL-dDeclaredLoop-56` stays under the 49152 B ceiling in `tools/template-size-limits.txt`; trim prose, never
  split it (M4 admits a second batch unit only on disjoint write sets).
- The specs are uncommitted at rev-1, so edit them in place with no rev bump. Touch no deviation record and no spec
  numbered 1 to 34.
- Do not commit, do not stage, do not run the build-index generator. Re-run the hygiene checks (`--only 12,25`) and
  report each file changed, the dDeclaredLoop lines left, and spec 56's size.

## The hits, verbatim

- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-36.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-38.md [path] `tools/lib/commit_trailers.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-39.md [path] `tools/lib/commit_trailers.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-40.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-40.md [path] `tools/unattended/commit_trailers.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md [path] `records/builds/dWellOiledMachine/README.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md [path] `tools/loop/README.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-42.md [path] `tools/loop/loop_witness.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-43.md [path] `.governance/policy.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-44.md [path] `tools/loop/guard.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-45.md [path] `tools/loop/position.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-46.md [path] `tools/loop/stage_coverage.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-46.md [bar] `tools/run-gates/run-gates.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-47.md [path] `tools/loop/factories.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-47.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-47.md [path] `tools/loop/loop_table.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-48.md [path] `tools/loop/budget.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-49.md [path] `tools/loop/budget.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-51.md [path] `command:tools/unattended/unattended.sh` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-51.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-52.md [path] `tools/loop/loop_table.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-52.md [path] `tools/loop/loop_table.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-53.md [path] `tools/loop/breakpoints.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-53.md [path] `tools/loop/breakpoints.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md [path] `tools/loop/loop_table.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md [path] `tools/loop/termination.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-55.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/stage_coverage.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `memory/map/features/loop.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_parents.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/position.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/guard.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_witness.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/upstream.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/position.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_checklist.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_parents.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `.governance/policy.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [path] `tools/loop/loop_transition.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md [guards] `check-wiring self-test <- .claude/skills/unattended/SKILL.md` — §4 files-touched names .claude/skills/unattended/SKILL.md, which trips the guard of leg 'check-wiring self-test', absent from the §7 leg line
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-43.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC2
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-53.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC3
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-36.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S2
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-39.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S4
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S42
