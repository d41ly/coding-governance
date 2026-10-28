**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-9 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-24 TOOL-dRankedPlan-29 TOOL-dRankedPlan-31 TOOL-dRankedPlan-37 TOOL-dRankedPlan-45

# Brief: dRankedPlan's specs re-grounded against dBoundRoles' and dTotalRecall's landed specs

## The prompt

> `gov-spec-writer` agents revise only the mismatched specs, never the main loop, at effort medium or
> higher. Each revision adds one `spec-revised` deviation record.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on dTendedCadence's spec run until this pass lands.

## The brief

### Goal

Revise the 15 dRankedPlan specs that the cross-check record names under "For the re-ground". Each one
should state its parents' surfaces the way their specs now spell them on origin/main at `d1721ef20`:
dBoundRoles as its re-ground `ac8ab8d5f` left it, dTotalRecall as `794a0f5fb` left it, and the rules
dDeclaredLoop, dOrderedCharter, dWitnessedBar, dPlacedRequest and dKeptSession apply to every spec.
Each spec keeps its own design, and only its assumptions about the parents change.

### Items

Read the cross-check record first,
`memory/builds/dRankedPlan/build/2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck.md`. Its
summary table numbers every assumption (rows 1 to 68), and its "For the re-ground" section names the
rows each spec answers. Section 2 of each group's return in
`memory/builds/dRankedPlan/build/2026-10-28-build-TOOL-dRankedPlan-1-crosscheck-returns.md` quotes both
sides of each MISMATCH and states its `Change:`; that is the starting point for each row. Read each
parent spec the record cites, at the lines it cites. This brief summarises them, and where the two
differ, the specs win. Before you edit for a row, re-read both sides. A row the parent's text does not
bear out is not edited: return it as refused, with the line that refutes it.

Facts every revision uses:

- **A policy read.** Memory-tree code reads a key through its kit's adapter, `read_policy_value(key,
  root)` in `tools/memory-tree/policy_value.py` (tr8 S10, tr8:81-82), which runs `policy.py get`. Loop
  kit code runs `<sys.executable> <policy kit>/policy.py get <key>` as a bounded subprocess, the policy
  kit found through the inline `resolve_kit_dir` block (oc7:202-205, :379-380). Exit 2 is a refusal
  the spec states what it does with. `read_slot_mode`'s `sys.path` insert and `import budgets`
  (`tools/memory-tree/gen_build_index.py:2293-2296`) is an in-process import, not a precedent.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205). A by-file
  load, a `sys.path` insert of another kit's directory, or a call of another kit's function by name is
  an in-process import. Code reaches another kit's verb by subprocess, found through the inline
  `resolve_kit_dir`. Memory-tree reaches the loop kit through `ratify.py` verbs (`ratify.py <slug>
  --exited`, rp21 S1's CLI); the loop kit reaches memory-tree through verbs such as `plan_record.py
  field`, `gov_record.py find` and `show` (tr9), or `gen_build_index.py --print-bindings`; a key of the
  roles kit's `derive_section_sha` shape is computed by memory-tree's own `derive_content_key`
  (tr2:62-66). Where the verb does not exist, write a §8 fork open for the owner: an ask to the owning
  build for the verb (a dRankedPlan unit when this build owns the file), or a declared `requires_if`
  row on the calling kit's `kit.toml`, with the reason the rule admits it. Recommend one. A caller
  check that counts callers must count the subprocess form it forces (rp22 S2).
- **A leg.** oc7 S3 reds a leg with no `enforces` (oc7:58-63). wb11 declares each leg once, in its kit's
  `[[gate_leg]]` row holding every manifest key, `chunk`, `ceiling` and `enforces` among them, or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row; `leg_factory.py --write` renders
  `tools/gate-legs.json`, and `--check` reds a manifest that differs (wb11:36-49, :154). A new leg is
  made with `leg_factory.py new`; a re-guard or re-shape of an existing leg edits its declaration
  (`tools/memory-tree/kit.toml`, `tools/loop/kit.toml`) and renders. A spec's list of the rows a new
  leg owes names `enforces` and the declaration. Name `enforces` from the principle or practice the
  leg's spec carries (rp13's `principle.p32` stays); where the spec gives no ground for a tag, write a
  §8 fork open for the owner, as dDeclaredLoop unit 3's F7 does. `tools/gate-legs.json` leaves Files
  touched as an edit; an AC reads the declaration or `leg_factory.py --check`.
  `tools/run-gates/leg_factory.py` is not in the tree today: the pass records that a hand edit stands
  in for it until wb11 lands.
- **A typed kind's writer.** A factory kind's writer is the command its owning spec names, else the
  factory with `--build`, `--unit` and the kind's field flags (tr1:187-193, :215; tr2:45-50,
  :296-298). `gov_record.py new <kind>` stays the door's adapter call, not the row's `writer`.
- **A role body.** Each body states the role's job and keeps every limit in `never`, as `<limit> —
  <enforcer>` entries (br1:149-150); br2 S3's R5 reds a body line carrying a prohibition word
  (br2:44-47).
- **The life items.** `item.life.request` and `item.life.close` have no `[[item]]` row (dl13:234-235),
  and `check_disposition_record` admits nothing for an item the definition does not declare
  (dl16:59-61). rp24 S1 and rp4 S3 must agree on one reader for those moves: either rp24 S1 admits a
  life-item record against the move tables, or rp4 takes rp24's records without that filter and relies
  on `derive_move`'s refusal. One writer revises both; pick the one the parents' text supports, state
  it in both specs, and return why.
- **An ask.** No dRankedPlan spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file. Before minting a fork, grep this build's other specs for one
  already open on the same verb, and cite it rather than open a second.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, for the rows the record names, and no other:

- **Group A, led by spec 1:** specs 1, 2, 3, 4, 9, 15, 16 and 24.
- **Group B, led by spec 13:** specs 13, 21, 22, 29, 31, 37 and 45.

rp13 S10 declares the `plan-fields selftest` leg and rp29 S25 re-shapes it; rp21, rp22 and rp37 share
the memory-tree to loop-kit read of `ratify.py`; each pair sits in one group.

The spec files are `memory/builds/dRankedPlan/spec/2026-10-2?-spec-TOOL-dRankedPlan-<n>.md`. Write
probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/rp-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and any
parent spec that looks wrong.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-28, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands, including its §4 Evidence and §10 cites.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-28, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes; replace text rather than append where a spec is near it.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `rpN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### Non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dBoundRoles, dTotalRecall, dDeclaredLoop, dKeptSession, dOrderedCharter, dWitnessedBar,
  dPlacedRequest, dSafePassage or dGroundRules. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dFurnishedOrders'
re-ground brief,
`memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md`,
and its revised specs, as the precedent for how a revised spec reads against the same two parents.
