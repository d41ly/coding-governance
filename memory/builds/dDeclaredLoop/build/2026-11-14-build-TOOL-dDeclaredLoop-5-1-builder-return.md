**Serves:** journal TOOL-dDeclaredLoop-5

# Builder return — TOOL-dDeclaredLoop-5, dispatch 1: a divergence, the built unit restored

## Why

DIVERGENCE: §4 "Check 53, the unattended side" (and §5 testing, its `harness arms` bullet) asks for check 53 with "Two branches, each one `fail 53` call site" in tools/unattended/check-unattended.sh. That file's refusal census is already at its budget. `.memory-tree.conf`'s REFUSAL_CEILINGS holds the token `tools/unattended/check-unattended.sh:264:2026-10-12:TOOL-aSparedSpawn-14`. Today the file has 264 `fail <n> "` call sites (grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' gives 264, PINNED), and under ARMS_REFUSALS="graded" a `status=1` refusal site counts toward the same census. So check 53's two sites would make it 266 against a ceiling of 264, and `tools/memory-tree/check-arms.py#cmd_check` would red the `harness arms (fail branches armed or pinned)` leg of the bar. A one-site variant in the shape of check 52 still reaches 265 and reds. Raising the ceiling is an owner act recorded as a dated memory/DECISIONS.md row under TOOL-aSparedSpawn-14's rule (TOOL-aSmoothedDispatch-2 and TOOL-aSweptBar-6 are the precedents: "owner, ... Raise to 324"). That is a change to a governance carrier, so it falls under M3 veto 2 and is outside a builder's authority. The unattended suite's arm `FA9 AC15 the leg's census holds`, which asserts <= 264 in tools/unattended/unattended.test.sh, pins the same figure (that suite is waived under README rule 8). To be buildable, §4 Check 53 and §5 need to say one of three things: (a) the ceiling rises 264 -> 266 (or 265 for a single site) under an owner decision row the spec cites, with .memory-tree.conf, memory/DECISIONS.md and that FA9 arm added to Files touched; (b) two existing sites of the leg are retired or consolidated through the retirement review and recorded in memory/project/refusal-retirements.txt, named in the spec; or (c) check 53 is placed somewhere outside the budgeted gate, with a spec-named carrier. Everything else in rev-4 held against current code. I built it and probed it before stopping, and the patch is saved.

## Summary

I committed nothing. Building check 53 as rev-4 specifies would push check-unattended.sh past its refusal ceiling, and raising that ceiling needs the owner, so I stopped and returned this as a divergence.

**Write set and records:**
- The write set was declared once with `--dispatch`, 25 paths, each passed as its own `--writes` (it named the acceptance ledger, a planned deviation record 53, and the generated map and index files). The dispatch was accepted.
- `--brief` said the brief was already recorded and unchanged.
- The dispatch left `memory/builds/dDeclaredLoop/RUN.md` staged with its dispatch row. I left it as the tool wrote it, uncommitted.

**What was built, then restored (spec §4):**
- `tools/loop/loop.toml`:
  - the `[witnesses]` table and the two `[[witness-alias]]` rows;
  - a `witness` of class `history` on every step.
- `tools/loop/actor-witnesses.txt` with the two seeded rows.
- `tools/loop/loop_lib.py`:
  - all seven spec functions;
  - `DECLARATION_SITES`;
  - an inline `resolve_kit_dir` copy, byte-identical to the canonical;
  - the seven plants;
  - the `--grade-site` verb.
- `checker_of` in `tools/unattended/unattended.sh` now returns 1 with no silent default.

Beyond the inventory I added `ACTOR_LIST` and `read_actor_rows`, because two places read the list. That needs a deviation record when the unit is re-dispatched. The patch, including the new list file, is at C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/TOOL-dDeclaredLoop-5.patch. The product tree is restored, and every name was checked with the naming lexicon's suggest verb (OK).

**Probes that ran** (each stands in for the `loop definition` leg or the unit's acceptance arms):
- **AC2 and AC3:** every new plant exits as the spec says.
- **Earlier plants:** byte-identical refusal messages for `disposition-alias` and `missing-step`.
- **AC1's red case:** probed with `python -c`; a step with no witness is refused, naming the step.
- **AC4:** `rc=1` then `machine` on the built code; it prints `machine` with rc=0 at HEAD.
- **AC6:** all five calls exit as specified, and the driver's real `DOD_CORE` grades green.
- **Readers that copy the module:** `load_loop`, `read_workflow_order` and `resolve_disposition` read the HEAD definition with no witness from a copy of `loop_lib.py` alone. Neither `coverage_join` nor `subprocess` was imported.
- **`read_actor_base`:** in a scratch git repository with an origin, it returned the base list and its sha, and a grown row was refused.

**A gate ran once by mistake:** before the hook started blocking it, I ran `python loop_lib.py --check` once from inside the loop kit's directory. That command is the `loop definition` leg. It exited 0 and printed "no comparison · the list is absent at the base". After the hook blocked the next run I used only function probes.

**Owed at the close once the unit is re-dispatched and built:**
- AC5, AC7 and AC8.
- The §7 legs.
- Both `New arm:` RED-first observations: the `witness-actor-unlisted` plant, and check 53's two branches in `check-unattended.test.sh`.

**Not done because nothing was committed:** the M6 bug-class checklist (`gotchas.py --for-diff`), which needs a commit to read; the codebase-map regeneration; the kickoff-manifest re-stamp; and the build-index write.
