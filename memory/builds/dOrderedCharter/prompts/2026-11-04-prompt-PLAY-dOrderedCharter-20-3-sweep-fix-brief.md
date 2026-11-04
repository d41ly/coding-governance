**Serves:** research PLAY-dOrderedCharter-20

# Brief: the spec-token hits a live read of the DEFERRED specs found

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. The main loop graded every DEFERRED spec as if live, because a spec's tokens are otherwise first
read at a builder's re-dispatch. This build's specs drew 21 hits. These items fold the ones a builder would stop on.

## The brief

### Goal

Clear the spec-token hits below from specs 20, 15, 3, 6, 2, 11, 31 and 32, so none refuses a dispatch.

### Items

1. **Specs 20 and 15, guards.** Files touched names `tools/codebase-map/gen_map.py`, which trips three legs section 7
   does not list: `codebase-map kit selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e`.
   - The pass runs that generator and writes none of its source. Reword the Files touched line so it names the map's
     generated outputs and not the generator, or add the three legs. Decide which by what the pass really touches.
2. **Specs 3 and 6, the fold onto unit 20's leg.** Spec 20's hands-off bullets give those two specs the tokens
   `instruction units selftest` and `PLANTS`, and neither spec spells them, so the token join reds on spec 20.
   - Fold both specs onto that leg. A plant joins the `PLANTS` tuple, and the leg runs it through the bare `fixture`
     verb.
   - Spec 3's S8 and its `New arm:` line spell `instruction_units.py --fixture --plant`, which that module's `main`
     refuses; the verb is `fixture --plant`. Fix them.
   - Spec 6's S4, its `New arm:` line, its Files touched and its fork F6 fold the same way. A drive case rides the leg
     by joining `PLANTS`, so the third argument to `run_plant_rows` and its rows go. Re-decide F6 in the fork record,
     delegated, with the loser and the observation that rejected it.
3. **A stable form inside an acceptance bullet.** The path check reads every path-shaped word in the acceptance bullets,
   and a `#symbol` or `HEAD:` prefix makes the word match no tracked path. Respell each:
   - spec 11: `tools/playbook/tag_index.py#REGISTRY_FIELDS`;
   - spec 6: `tools/policy/budgets.py#resolve_caps`;
   - specs 2 and 3: `HEAD:tools/template-size-limits.txt`.
   Keep the observation the same: put the symbol or the revision in words or as a separate token beside the plain path.
4. **Two older hits.** Spec 31's `agent-instructions/adopt-agent-instructions.sh` needs its full tracked path. Spec 32's
   `.governance/instructions.toml` names a file that does not exist yet; say so in a form the check does not read as a
   path, or point at the unit that creates it.
5. **Left alone.** `help/charter.md` in spec 1, `tools/playbook/load_sets.py` in spec 11 and
   `tools/playbook/instructions_edit.py` in spec 15 are files those units create; they pass at a DEFERRED dispatch.

In every spec you revise:

- Spec 20 stays at rev-9 with its Status word left as it is, and gains one history line.
- Every other spec bumps its **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`, and adds one
  history line naming this brief and the S or AC ids it touched.
- Each listed `path:line` citation stays byte for byte.
- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it adds no `path:line`.
- A `**Readers:**` by-name half names readers by plain tracked path.
- Stay under the 47000-byte authored budget.
- A consumes-from or hands-off edge you change has its mirror; say so in the return.

For the run:

- No unit is building, so edit the specs in the tree. Prior product work sits uncommitted around spec 20: leave it.
- Writes stay in the eight specs.
- Do not commit and run no gate. You may run `check_path_shaped` from `tools/check-spec-tokens.py` as a read-only probe.
- Return each spec's new rev, any fork decision with its loser, and any item you did not clear.

### Acceptance

- Every item above is folded, or listed in the return with the reason it was not.

### Gates

The main loop re-runs the live sweep before the commit.

### Non-goals

- No code.
- No other spec.

### Limitations

The items above, "For the run".

### Reuse

Spec 20's section 8 forks F11 and F12; `tools/check-spec-tokens.py`.
