# Brief — aScoutedSeam: fold the measured diff-mode prompt and level into TOOL-aScoutedSeam-3

**Serves:** research TOOL-aScoutedSeam-3

## The prompt

> first, record the prompt-writing method that improved the result, then go with 1, then 2. But also, add testing 'low' effort vs 'medium' in scope, based on the same or further improved prompting method to see the difference.

## The brief

### Goal
Revise TOOL-aScoutedSeam-3 so diff mode ships the measured design: the enumerated-coverage prompt
with a deterministic unit lister, at the `gov-reuse-scout` type's own level, `medium`. Close fork F2
on the measurements. This pass touches the spec only: no product code, and no commit.

### Items
1. **§8 F2: close it.** Record `RESOLVED (owner, 2026-10-18): medium, with the enumerated-coverage
   prompt`. Cite three records: the T1 trial `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`,
   the method `2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md`, and the judge and `low` record
   `2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`. The figures, judged on the 23 diff cases:
   - the enumerated prompt at `medium` covers 14 primaries, with 11 misleading seams of 130;
   - the open prompt at `extra` covers 11, and at `medium` 7;
   - the enumerated prompt at `low` covers 8, with 19 misleading of 105.

   `high` with the open prompt was never run. It is no longer needed, because the composition carried
   the gain.
2. **S6 and S7: drop the `high` override.** Remove the `[effort.stages.reuse] diffCheck = "high"`
   table. `diffCheck` runs at the agent type's level, `medium` in gov, exactly as the existing S6 text
   says an `efforts` that omits it does. S7 keeps the `workflows.toml` `diffCheck` stage and the
   catalogue re-render, and loses the policy edit. That removes the reason the edits had to share one
   commit for R12. Restate S7's single-commit rule only if something still binds it; verify that
   against `check_roles.py`. Change §4's files list to match.
3. **S2: rewrite the prompt per the method record's recipe.**
   - The DIFF-lens instruction becomes a COVERAGE job over a supplied unit list.
   - For each listed unit, the agent returns one row: the unit, the nearest existing `path::symbol`
     (or `none` with what it searched), a verdict from `duplicate`, `should-extend`, `new` or
     `not-a-unit`, and a one-line why.
   - The agent then adds rows, marked `added`, for repeated literals, hardcoded design values, renamed
     copied bodies and rebuilt JSON nodes.
   - The prompt names the failure it guards against: "do not stop at the first duplicate; a listed
     unit without a row is incomplete".
   - A duplicate becomes a MUST seam and a should-extend a SHOULD seam. The wiring half for `## reuse`
     MUST lines stays.
   - The worked examples are the T1 handoffs, `prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-13` to
     `-35-reuse-scout.md`.
4. **New scope item: the deterministic unit lister.** It is a codebase-map kit CLI that reads
   `git diff <base>..<head>` and prints the units the diff adds in product files, with their kind and
   path. The measured rules are in `2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py`'s `extract_units`:
   - **Population:** it skips memory, docs, help, tests and lockfiles, and lists definitions,
     constants, shell functions, schema fields and JSON tree keys.
   - **CSS:** CSS patterns run only in style files.
   - **Hunks:** a hunk that adds 4 or more lines and names no unit becomes a `hunk` unit.
   - **Cap:** the list stops at 60 units, followed by a count of the rest.
   - **Empty list:** when the lister finds nothing, the prompt tells the agent to enumerate the units
     itself.

   The caller runs the lister and passes its output to `reuse-scout.js` as a new `units` arg, because a
   Workflow script cannot run git. Add `units` to S1's refusals and to the §4 data model. Place the
   lister by the kit's seams, and run the reuse probes M5 names before naming a file. Give it its own
   criterion, which goes red when a hunk adding logic inside an existing function gets no unit, or when
   a CSS pattern fires outside a style file.
5. **S3: caps.** Keep "at most 10 duplicates, MUST first", and adopt the orient mode's cap of five MUSTs
   with demotion from TOOL-aScoutedSeam-1. The judge's 11 misleading seams at `medium` are what the cap
   is for. Cite the record.
6. **AC3:** it runs at the type level, `medium`, on the same three gov cases. All three were solved at
   `medium` in T1. The cost line becomes three agents at `medium`, measured at 19 s to 4 min 57 s per
   diff. **AC5:** `harness-args reuse-scout` prints `diffCheck`, and no policy override is required.
   Verify what `stage-efforts reuse` prints for a stage with no override before you write the
   criterion.
7. **§4 alternatives rejected:** add the open prompt at `extra`, the enumerated prompt at `low` and the
   un-run `high`, each with the figures from item 1. **§5:** replace the perf line with the T1 cost and
   the judge's precision figure.
8. **§9:** add one revision line naming every section, scope item and criterion moved.

### Acceptance
TOOL-aScoutedSeam-3 carries the new §9 line, and §8 F2 reads RESOLVED with the figures. S2, S3, S6, S7
and the new lister item read as above, the lister has a criterion, and AC3 and AC5 are rewritten.
`python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and
`--check-format` pass after the main loop re-renders the indexes. The spec stays under the 49152-byte
ceiling.

### Gates
memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### Non-goals
- No product code, and nothing under `tools/`, `skills/` or `.claude/`.
- No other unit's spec is edited. TOOL-aScoutedSeam-1's orient prompt adopting the method is a separate,
  untested question.
- No change to unit ids, order or titles, and no commit; the commit is the main loop's.

### Limitations
The T1 lister lives in a research instrument, so §6 cannot cite it as a built file. Cite it by
basename, or as the record it serves.

### Reuse
`2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py` (`extract_units`, `render_question`) is the measured
lister and prompt. TOOL-aScoutedSeam-1's merge cap and stage convention are the seams the diff mode
already extends.

## Owner confirmation

Asked: what to do after T1, with option 1 a precision pass (blind judge) and option 2 a fold into
TOOL-aScoutedSeam-3, closing F2 as `medium` with the enumerated prompt and adding the lister.
Answer: "first, record the prompt-writing method that improved the result, then go with 1, then 2. But
also, add testing 'low' effort vs 'medium' in scope, based on the same or further improved prompting
method to see the difference."
