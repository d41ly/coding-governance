**Serves:** research TOOL-dGroundRules-33

# Rename brief — TOOL-dGroundRules-33 consumes `build_install_target`, not `build_fresh_target`

## The prompt

> TOOL-dGroundRules-32 rev-6 rules, on its builder's measurement at HEAD 93e4b4d31, that no second install-target builder is added: S16 extends `build_install_target(name, ids)` in `tools/policy/check_policy.py` in place, returning `(target, snapshot)` and reading its answers from `DEPLOY_FULL`'s `[answers]` table in the snapshot's `selftest.py`; `build_fresh_target` never exists. Its hands-off edge to this unit now names `build_install_target`, and the spec-tokens `[handoff]` arm reds because this spec still names `build_fresh_target` in seven places.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-33.md` so every mention of the builder names `build_install_target` with its rev-6 signature and meaning. Author only: no product code, no commit, no gate.

### Items
1. Replace each `build_fresh_target` with `build_install_target`, keeping each sentence's meaning, in §1, §3 (the consumes-from edge from TOOL-dGroundRules-32), §4, §6 and the `New arm:` line; where a sentence relies on the old signature `(snapshot_root, source_root, kits)`, restate it on `build_install_target(name, ids)`.
2. The status header's rev rises by one, with one §9 line naming the rename and TOOL-dGroundRules-32 rev-6 as its cause; no design change. Keep the file under 48600 bytes; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`grep -c build_fresh_target` on the spec prints 0; `python tools/check-spec-tokens.py` exits 0 with this spec and TOOL-dGroundRules-32 read as INPROGRESS (the main loop runs it).

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
None beyond the items.

### Reuse
TOOL-dGroundRules-32 rev-6's S16 is the source of the signature.
