**Serves:** research TOOL-dGroundRules-32

# Divergence brief 2 — TOOL-dGroundRules-32, S12 against a reader-free guard

## The prompt

> Its builder probed TOOL-dGroundRules-32 rev-6 at HEAD 3e16f3efe and handed it back as a DIVERGENCE before writing anything. S12/AC12 (finding 27) route "the guard's parse of the policy file and arm_schema's" through `parse_policy` in `tools/policy/policy.py`, but `tools/policy/guard.py` is built never to import the reader (its docstring, and the kit README), and CLOSED TOOL-dGroundRules-6 AC10 requires `grep -nE "^\s*(import|from)\s+policy\b" guard.py` to print nothing; loading the reader by path would build around it. S12 also has `on-invalid-bom` run `guard.py --staged` and `--check`, but the guard accepts only `--staged`. And `arm_schema` calls `policy.validate`, which parses with `tomllib` itself, then runs `scan_keys(tomllib.loads(text))`, both needing the nested table where `parse_policy` returns flattened leaves. Other items: S3's `{prefix}/memory-tree/kit.toml` is already in the guard (unit 23); S8's WRONG already fires in `run_ships_join`, only the `read_shipped_descriptors` refactor remains; AC9's code spans are the stripped pair fragments TOOL-dGroundRules-34 S15 restates whole; §4 files touched lacks `memory/guides/SESSION-KICKOFF.md` though S3 and S10 write `tools/gate-legs.json`; S16's `DEPLOY_FULL` answers were not probed against `apply`.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-32.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S12 and AC12: the reader's BOM strip lives in one helper in `tools/policy/policy.py` that `parse_policy`, `validate` and `arm_schema`'s nested parse all call before parsing, so the three readers agree; `tools/policy/guard.py` strips a leading BOM inline before its own `tomllib` parse and imports no policy reader, keeping TOOL-dGroundRules-6 AC10 true, with one comment naming the helper it mirrors; `on-invalid-bom` runs `guard.py --staged` only. AC12 observes both the helper's three callers and the guard's inline strip, and that the guard's import grep still prints nothing.
2. S3 and AC3: restate that the descriptor lines are already in the guard (unit 23); what remains is the run-time derivation from the registry's `descriptor` field and its `WRONG`.
3. S8: restate that the `WRONG` already fires; what remains is the `read_shipped_descriptors` refactor, observed by its criterion.
4. AC9 keeps its audited text; S9 or §7 says its probe is observed with the pair spellings TOOL-dGroundRules-34 S15 restates whole.
5. §4 files touched adds `memory/guides/SESSION-KICKOFF.md`.
6. S16 says the builder probes `DEPLOY_FULL`'s answers against `apply` in the fresh target before building, and hands back a divergence naming the failing answer if `apply` refuses.
7. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec, TOOL-dGroundRules-33 and TOOL-dGroundRules-34 read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's per-finding statuses at 3e16f3efe stand: S1, S2, S5, S6 and S7 hold; S4, S9, S10, S11, S13, S16 to S20 are buildable as written.

### Reuse
TOOL-dGroundRules-6's closed spec is the source of the guard's reader-free rule.
