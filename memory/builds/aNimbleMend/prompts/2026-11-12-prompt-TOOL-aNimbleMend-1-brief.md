# Brief — aNimbleMend: inline red fixes with the record after, and budgeted fast pass legs

**Serves:** research TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12

The prompt arrived as a file, read from the path below; its content is quoted whole.

Source: `C:/Users/DAILY-~1/AppData/Local/Temp/claude/9d098fb74f3324d9/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/handoff-inline-bar-fixes-and-pass-legs.md`

## The prompt

> # Handoff: inline bar-red fixes, and fast pass legs
>
> ## The prompt
>
> > Build an opt-in mechanism (opted in by default in any repo) that allows two things:
> > 1. bar findings and red fixes to be made inline, without a spec, with the work record maintained AFTER the fact. ONLY bar
> >    findings/red fixes; the rest stays as it is right now.
> > 2. passes run ONLY fast legs: an opt-in pass leg list that should NOT EXCEED 10 minutes (with 10-15% fluctuation) per pass.
> >    Never check-unattended, self-tests or anything slow. Only the fast legs that produce the most reds; identify them.
> > This should be fully reconciled with the rearchitecture build that's ongoing.
>
> — owner, 2026-11-11.
>
> ## Why
>
> The dOrderedCharter close (2026-11-11) ran three full bars of about 2 hours each and added three fix units, 80, 81 and 82,
> one per bar. Each fix unit's change turned a neighbouring leg red, and the only place that red could be seen was the next full
> bar, because:
>
> - a unit pass runs no gate leg: the `gate-guard` hook refuses `GATE_FULL=1` before VERIFYING, and the scratch guard refuses gate
>   legs to role agents;
> - every product change needs a spec first (`[spec]`), so a one-line red fix costs a spec writer, a spec commit with its hooks,
>   a builder and a records commit, about 1.5 hours;
> - the full bar costs about 2 hours on a shared node.
>
> ## Goal
>
> 1. **Inline red fixes.** When a bar leg, or a pass leg (item 2), is red, the main loop or a builder may fix that red without a
>    spec. The work record is written after the fact, in the same commit or the next one. Every other product change keeps today's
>    spec-first path.
> 2. **Fast pass legs.** After every unit pass, a declared list of fast legs runs, chosen as the legs that red most often for the
>    least wall clock. Its total stays within 10 minutes per pass, with 10-15% tolerance. The full bar still runs once, at the close.
>
> Both are opt-in mechanisms that are on by default in every repository, gov included. An adopter turns either one off with one key.
>
> ## Scope
>
> 1. **Feature switches.** Two keys in the policy catalogue the policy kit reads (`.governance/policy.toml`), both defaulting on,
>    for example `bar.inline_red_fixes` and `pass.fast_legs`. Name them with `/lexicon`, and confirm the catalogue's
>    default-and-preset rules (P10, the policy reader's `--explain`).
> 2. **Inline red-fix lane (feature 1).**
>    - **Trigger.** The lane opens only for a leg recorded red in the bar's failure record (`gate-last-failure.txt`, the
>      gate ledger) or in a pass-leg run. A fix names the leg and the red line it clears.
>    - **Write gate.** It admits a product write without a specced unit only through this lane, for the paths the red names or
>      the narrowest code that produces it. Stay within the commit-message and trailer grammar the hooks already read: a
>      `Red-fix:` trailer naming the leg, beside the attribution trailer.
>    - **After-the-fact record.** A typed record kind, written by `build_records.py`, in the same commit or the next one. It names
>      the leg, the red line, the files, the commit, and the re-run that shows the leg green. It is joined by the hygiene checks the
>      way a deviation record is.
>    - **Hard limits.** Write them as gates, never as prose. No new feature, no new surface, no spec revision, no fork resolved
>      inline. A red whose fix needs a design choice, or touches another build's spec or a guarded `.governance/` file, still goes
>      through a spec or to the owner. Bound the size of an inline fix and state the bound.
> 3. **Fast pass legs (feature 2).**
>    - **Declaration.** Declared once, in `tools/gate-legs.json`, as a per-leg field or tag, never as a second hand-typed list.
>    - **Budget gate.** The sum of the declared legs' evidenced ceilings (`tools/run-gates/ceiling-evidence.txt`) must stay within
>      600 s, and the gate reds a list that would exceed about 690 s. A pass run that overruns its budget prints the overrun as a <!-- PINNED 2026-11-12 -->
>      finding, never silently.
>    - **Run point.** The main loop, or the builder after its commit (decide which and say why), runs the list scoped to the pass's
>      diff, with the guards the legs already declare.
>    - **Hooks.** The `gate-guard` hook and the scratch guard admit exactly these legs during a pass, and nothing else.
>    - **Excluded forever.** The `unattended kit gate` leg (`check-unattended.sh`), every self-test leg and chunk, the e2e chunk,
>      and any leg whose evidenced ceiling exceeds a stated per-leg cap.
> 4. **The starting list, to re-measure at your base.** The red count is over the six bar logs of the dOrderedCharter close.
>    Seconds are each leg's last measured wall time on node a, from the gate ledger.
>
>    | Leg | Reds | Seconds |
>    |---|---|---|
>    | dead-path carriers | 4 | 7.0 |
>    | install-prefix (shipped surface) | 3 | 7.9 |
>    | policy check | 5 (inherited) | 15.8 |
>    | govkit selfcheck | 2 | 19.7 |
>    | harness arms | 2 | 2.7 |
>    | kit epoch | 1 | 8.9 |
>    | govkit runbook parity | 1 | 0.2 |
>    | python reads | 1 | 17.2 |
>    | kickoff-manifest ratchet | 1 | 7.0 |
>    | shell hygiene | 1 | 2.8 |
>    | method carriers | 1 | 9.3 |
>    | remote literals | 1 | 1.1 |
>    | docs | 1 | 5.9 |
>    | lexicon naming predicates | 1 | 9.9 |
>    | held-leg budgets | 1 | 17.1 |
>    | lexicon wiring | 1 | 13.5 |
>    | instruction edits (manifest checks) | 2 | 64.9 |
>    | tags | 1 | 81.3 |
>
>    - **Memory hygiene** went red 5 times, but it runs 641.6 s over the whole tree. Include it only as its staged or scoped form
>      (`--staged`, or `--only` for the checks that red most: 9, 12, 21, 23 and 25), and measure that form.
>    - **Pinned facts and positional** (`writing_practice.py check pinned-facts`, `positional.py check`) are cheap and redded
>      several times mid-build. Make them pass legs too, if they are legs, or add them as legs.
>    - **Too slow for a pass:** spec tokens (905.7 s), the govkit acceptance matrix (1084.3 s), routed commits (636.8 s),
>      pass-order history (282.9 s), straggler-guard arms (184 s), brief-recorded (183.8 s), and the unattended kit gate (2240 s). <!-- PINNED 2026-11-12 -->
>      State each exclusion. Where a cheap, scoped form of one exists, for example the spec-token check graded only for the
>      pass's own spec, propose it.
>    - **Derive, never type.** The red counts and seconds above are evidence, not the list. Derive the list from the gate ledger
>      and ceiling evidence with a stated rule (red frequency per second, within the budget), and record that rule.
> 5. **Docs.** A help page for each mechanism, under `help/` (`[docs]`). Update `BUILD-METHOD.md` and
>    `memory/guides/UNATTENDED-PROTOCOL.md`, which state that no gate runs in a pass and that every product change is specced. Edit
>    them where they are rendered from, never in place.
>
> ## Reconciling with the rearchitecture
>
> - **Base.** Build on local main after `dOrderedCharter` lands. That build is the charter and playbook rearchitecture, in
>   VERIFYING on `branch/unattended-dorderedcharter-725f52`. It retires the agent-instructions kit into `playbook-render`, adds
>   the shared retired-kit reader, makes the renderer require `memory-tree` and `policy`, and adds `policy` to the default
>   selection. Read its README's build order and its last units, 78 to 82, before scoping.
> - **The chain.** This work belongs in the chain the rearchitecture runs through: dClosedLoop's packet, its carries join and its
>   `[chain]` registry. A new build there needs its `**Derived:**` or `**Carries:**` binding on every spec, and a row in the
>   chain registry if it joins the chain. Decide whether it joins the chain or stands alone, and say why.
> - **Kits touched.** Expect the unattended kit (its hooks, `gate-guard.js`, the scratch guard, `--dispatch` and `--check-commit`
>   checks), run-gates (the leg manifest and its runner), memory-tree (records, `build_records.py`, the hygiene checks, the write
>   gate) and policy (the two keys). Every kit-version bump happens once, after the last move.
> - **What these features must not break.** Inline fixes must not bypass the routed write gate for anything that is not a red fix.
>   They must not land a guarded `.governance/` file, and they must not rewrite a CLOSED spec (P19). Pass legs must not run inside a
>   role agent's pass where the scratch guard is the reason the pass is cheap; decide and record where they run.
> - **Two tool changes from the same week.** Units 80, 81 and 82 changed `tools/govkit/matrix.py` and `tools/gate-legs.json`. The
>   `aSwiftRefusal` and `aShelvedLeg` builds changed `--dispatch` (refuse fast, honour deferrals). Reconcile with both.
>
> ## Out of scope
>
> - The full bar at the close, which still runs once, with `GATE_FULL=1`, no self-tests and no unattended kit gate (owner rule,
>   2026-11-11).
> - Spec-first for anything that is not a bar or pass-leg red.
> - The inherited policy-check red: its five `review.*` reader findings belong to dFairHearing.
>
> ## Acceptance
>
> - In a scratch adopter and in gov, with the switches at their defaults:
>   - a planted red on a fast leg is fixed through the inline lane with no spec;
>   - the after-the-fact record is written and joined;
>   - a product write that answers no red is still refused by the write gate.
> - With `pass.fast_legs` on:
>   - one unit pass runs the declared list in at most 690 s on node a; <!-- PINNED 2026-11-12 -->
>   - the list excludes the unattended kit gate, every self-test and every leg over the per-leg cap;
>   - a budget gate reds a list planted over the budget.
> - With either switch off, the lane or the pass legs are absent, and the old behaviour holds byte for byte.
> - Every new gate has been seen red (`[gate]`).
>
> ## Gates
>
> The full bar at the close, `GATE_FULL=1`, without self-tests and without the unattended kit gate leg.

## The brief

### Goal
Two mechanisms, each behind a policy key that defaults on in every repository: a red bar leg or pass leg is fixed inline with no spec and its typed record written afterwards, and every unit pass is followed by a declared list of fast gate legs held to 600 s, 690 s at most. Every other product change stays spec-first, and the full bar still runs once, at the close. <!-- PINNED 2026-11-12 -->

### Items
1. Two policy keys in the policy kit's catalogue, both default on, one per mechanism, named through the lexicon and the catalogue's key grammar [planned TOOL-aNimbleMend-1]
2. The pass-leg list declared once, as a field on a leg's row in `tools/gate-legs.json`, derived from the gate ledger and the ceiling evidence by a recorded rule of red frequency per second inside the budget [planned TOOL-aNimbleMend-2]
3. A budget gate: the declared legs' evidenced ceilings sum to 600 s at most and red past 690 s, with a stated per-leg cap, and the unattended kit gate, every self-test leg and chunk and the e2e chunk excluded for good [planned TOOL-aNimbleMend-3] <!-- PINNED 2026-11-12 -->
4. Memory hygiene in a scoped form, pinned facts and positional as pass legs, each measured, and a scoped spec-token check proposed for the pass's own spec; every leg too slow for a pass has its exclusion stated [planned TOOL-aNimbleMend-4]
5. A runner for the declared list over the pass's diff, with the guards the legs already declare, that records its run and prints a budget overrun as a finding [planned TOOL-aNimbleMend-5]
6. The gate guard and the scratch guard admit exactly the pass legs during a pass, and nothing else [planned TOOL-aNimbleMend-6]
7. The run point decided and recorded: the main loop runs the list after each unit pass's commit, never inside a role agent's pass [planned TOOL-aNimbleMend-7]
8. The inline lane's trigger and write gate: a product write with no specced unit is admitted only for a leg recorded red in the bar's failure record or a pass-leg run, named by a `Red-fix:` trailer beside the attribution trailer [planned TOOL-aNimbleMend-8]
9. The after-the-fact record: a typed kind written by `build_records.py` in the fix's commit or the next, naming the leg, the red line, the files, the commit and the green re-run, joined by a hygiene check as a deviation record is [planned TOOL-aNimbleMend-9]
10. The lane's hard limits as gates: a stated size bound, no new feature or surface, no spec revision, no fork resolved inline, no guarded `.governance/` file, no closed spec rewritten [planned TOOL-aNimbleMend-10]
11. A help page per mechanism under `help/`, and the build method and the unattended protocol updated where they are rendered from [planned TOOL-aNimbleMend-11]
12. The acceptance observed in a scratch adopter and in gov, each switch on and off, with every new gate seen red [planned TOOL-aNimbleMend-12]
13. Reconciled with the rearchitecture: built on main after dOrderedCharter landed, the chain question decided and recorded, and the leg manifest and `--dispatch` changes of units 80 to 82, aSwiftRefusal and aShelvedLeg read before either is touched [planned TOOL-aNimbleMend-2 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8]

### Acceptance
- With both keys at their defaults, in a scratch adopter and in gov: a planted red on a fast leg is fixed through the lane with no spec, its record is written and joined, and a product write that answers no red is still refused by the write gate.
- With the pass-leg key on: one unit pass runs the declared list in at most 690 s on node a, the list holds no unattended kit gate, no self-test and no leg over the per-leg cap, and the budget gate reds a list planted over the budget. <!-- PINNED 2026-11-12 -->
- With either key off, the lane or the pass legs are absent and the earlier behaviour holds byte for byte.
- Every new gate has been seen red.

### Gates
The full bar once, at the close, with `GATE_FULL=1`, without the self-tests and without the unattended kit gate leg.

### Non-goals
- No change to the close's full bar.
- No spec-free path for any change that is not a fix of a bar red or a pass-leg red.
- No fix of the inherited policy-check red, whose five `review.*` reader findings are dFairHearing's.
- No reader for `verdict.red-route`, which stays dWitnessedBar's.

### Limitations
- The build stands alone and joins no chain: the chain registry is joined both ways with the design view, and this build is no row of that design.
- Kit versions are bumped once, after the last unit, through the lander's `mint`.
- A pass leg never runs inside a role agent's pass.
- An inline fix never bypasses the routed write gate for a write that answers no red.
- The red counts and seconds in the prompt are evidence to re-measure at this base, never the list itself.

### Reuse
- `python tools/codebase-map/reuse_lookup.py` on both behaviours named no single seam; the seams to extend are read from the code: `tools/gate-legs.json` and its runner `tools/run-gates/run-gates.sh`, the ceiling evidence `tools/run-gates/ceiling-evidence.txt`, the hook `tools/unattended/gate-guard.js`, the routed write gate in `tools/hooks/scratch-guard.js`, the commit grader `tools/memory-tree/routed_commits.py`, the record door `tools/memory-tree/build_records.py` with its `KINDS` table, and the catalogue `tools/policy/catalogue.toml`.
- Recall, terms `pass gate leg bar red inline fix spec-first write-gate routed deviation gate-guard scratch-guard`: `TOOL-dWitnessedBar-21` and `TOOL-dScopedBuild-15` design a fix pass routed by `verdict.red-route`, both in DEFERRED builds, so no built seam exists; `TOOL-aDeferredBar-3` is the gate guard's contract; `TOOL-dFoldedAudit-7` is the precedent for catalogue keys outside the design's table.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
