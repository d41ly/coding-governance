**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 rev-15 — the renderer reads a retired kit id as govkit does

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. Unit 31's builder (run wf_0fdda6ef-55d) handed rev-14 back: F10's pick maps a retired id only inside
govkit's selection resolver, but the playbook renderer reads gov's deploy kits on its own and refuses the id.

## The brief

### Goal

Revise spec 31 so its pass leaves gov's own charter render, the step gate's listing and every adopter's render working once the
agent-instructions entry leaves, keeping F10's pick: gov's guarded deploy file is not edited.

### Items

1. **The divergence, observed with S1, S5, S9, S10 and S11 applied:** `python tools/playbook/render_playbook.py --target . --check`
   printed `render-playbook: REFUSED — kits names agent-instructions, which is not a registry entry id`, and
   `python tools/govkit/step_gate.py --list` exited with a traceback from the `drive` class reader. The refusing readers are
   `tools/playbook/render_playbook.py#read_kits` and `tools/playbook/render_playbook.py#read_drive_rows`, the second reached through
   `tools/playbook/instruction_units.py#read_drive`. Confirm each at HEAD.
2. **Extend S10.** The renderer's kit readers read a retired id as its successor through the registry's `[[retired]]` rows, or skip it
   when the successor is `none`, exactly as `tools/govkit/govkit.py#resolve_selection` does under S10. The renderer already reads the
   registry to refuse a non-entry id, so it can reach the table. By the reuse rule, the second reader of the `[[retired]]` format
   extracts one shared reader both callers use rather than copying the mapping; say where it lives so a renderer installed without
   govkit still reaches it, and rewrite the non-goal that limited the mapping to `resolve_selection`'s two branches.
3. **Criteria.** AC16 gains the renderer half: the render check exits 0 over gov's tree with the entry gone, and `step_gate.py --list`
   lists the `drive` class. Give the shared reader an arm that can fail.
4. **Three findings from the same hand-back, folded or named:**
   - Release-0's fixture deploy file has no `[charter] adopter_rules`, so the upgrade-walk leg reads the new step as not load-bearing;
     add the fixture's `plants.toml` row and put the file in Files touched.
   - Deleting `tools/agent-instructions/` removes verb offenders, so the lexicon's two-sided `VERB_OFFENDER_PIN` must be re-measured
     in the pass; say so in the scope.
   - The govkit selftest arm for the `[answers]` trailer refusal already fails at HEAD, before this unit; name it in section 5 as a
     known red this unit does not own.
5. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words include an untracked
   path, no `path#symbol` in an acceptance bullet, no suite as the observation, each backticked span on one line, every tripped leg on
   the leg line. Cite code as `path#symbol` or a blob-pinned line. Every fork carries a resolution mark; every new fact is pinned on its
   own line outside backticks; every minted function passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
6. Edit the spec in the repository directly; no builder is running.

Bump the **Status:** rev to rev-15, dated 2026-11-10, status kept `DEFERRED`, with a revision-log line naming this brief and the
sections, scope ids and acceptance ids it touches.

### Acceptance

- Spec 31 builds as written over HEAD with the renderer half of S10 in scope, and passes the pinned-facts, spec-shape and positional
  checks.

### Gates

Run the pinned-facts check, memory hygiene's spec-shape check and the positional check over the spec; the main loop runs the
spec-token check.

### Non-goals

- No code. No edit to any other spec or file. No edit to gov's guarded deploy file.
