**Serves:** research TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75

# Promoted-fix brief — the round-3 promotions, before their commit

Fix the eight specs the round-3 spec audit's disposal added, `TOOL-dDeclaredLoop-68` to `-75`, so
`python tools/check-spec-tokens.py` names no dDeclaredLoop spec and `bash tools/memory-tree/check-memory-hygiene.sh
--only 12,25` prints no dDeclaredLoop line, changing nothing else.

- Each `[path]` hit below: cite a file the build run will create by BASENAME in §6, full paths staying in §2, §4 and
  Files touched, as earlier rounds did; correct a path that is simply wrong. `.governance/` files are created by
  other builds' runs: cite them in §6 by basename or by what they are.
- Each `[leg]` hit (a §7 leg-line name not in `tools/gate-legs.json`): a leg the build run will add is declared on a
  `New arm:` line, never on the leg line, which names only legs that exist at HEAD; a misspelled existing leg is
  corrected to its manifest name.
- Each check-12 hit (an acceptance bullet naming no backticked witness): give the bullet the backticked command or
  file that observes it.
- Each check-25 hit (a §2 item that retires a named thing): add a `**Readers:**` clause, `by name:` every reader
  that spells the name (each found by `git grep -n` at HEAD) and `by value:` its value's readers or
  `NO VALUE READERS` and a reason; or, where the item retires nothing, reword it so it no longer reads as a
  retirement. The passing clauses in `TOOL-dDeclaredLoop-7`, `-11` and `-21` show the shape.
- The specs are uncommitted at rev-1, so edit them in place with no rev bump. Touch no deviation record and no spec
  numbered 1 to 67.
- Do not commit, do not stage, do not run the build-index generator. Re-run the hygiene checks (`--only 12,25`) and
  report each file changed and the dDeclaredLoop lines left.

## The hits, verbatim

- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-68.md [path] `tools/loop/loop_witness.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md [path] `{prefix}/loop/breakpoints.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md [path] `tools/loop/breakpoints.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md [path] `memory/map/features/loop.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md [path] `tools/loop/budget.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md [path] `tools/loop/breakpoints.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [leg] `loop breakpoints fixtures` — not a name in tools/gate-legs.json
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [leg] `loop position fixtures` — not a name in tools/gate-legs.json
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [leg] `loop guard fixtures` — not a name in tools/gate-legs.json
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [leg] `loop transition tables` — not a name in tools/gate-legs.json
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/budget.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/budget.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `HEAD:.governance/install.json` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `.governance/outbox/.update.lock` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/position.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `memory/map/features/loop.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/loop_table.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/README.md` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/loop_witness.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md [path] `tools/loop/loop_witness.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC22
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-74.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1
