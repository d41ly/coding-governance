**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-74

# Brief: dLinkedLibrary's specs re-grounded against dTotalRecall's landed specs

## The prompt

> Have `gov-spec-writer` agents revise only the mismatched specs. The main loop never edits a spec.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on dIndexedDesign's spec run until dLinkedLibrary is re-grounded.

## The brief

### Goal

Revise the 20 dLinkedLibrary specs that the cross-check record names under "For the re-ground". Each
one should state its parents' surfaces the way their specs now spell them on origin/main at
`1a61f21a2`: dTotalRecall as its re-ground `794a0f5fb` left it, dBoundRoles as `ac8ab8d5f` left it,
and the rules dOrderedCharter, dDeclaredLoop, dWitnessedBar and dPlacedRequest apply to every spec.
Each spec keeps its own design, and only its assumptions about the parents change.

### Items

Read the cross-check record first,
`memory/builds/dLinkedLibrary/build/2026-10-28-build-TOOL-dLinkedLibrary-1-parents-crosscheck.md`. Its
summary table numbers every assumption (rows 1 to 85). Section 2 of each group's return in
`memory/builds/dLinkedLibrary/build/2026-10-28-build-TOOL-dLinkedLibrary-1-crosscheck-returns.md`
quotes both sides of each MISMATCH and states its `Change:`. Read each parent spec the record cites,
at the lines it cites. This brief summarises them, and where the two differ, the specs win. Before you
edit for a row, re-read both sides. A row the parent's text does not bear out is not edited: return it
as refused, with the line that refutes it.

Facts every revision uses:

- **The record-kind factory's full call.** `record_kinds.py new` refuses a row with no `--purpose`
  (tr16:36), and every row carries non-empty `home`, `lifecycle`, `readers` and `layer`, which
  `check_record_kinds` reds when missing (tr18:45-47; tr1:65-67). tr25 S1 (tr25:33-37) is the precedent
  for a call spelling every column. `writer` is a door: the command that writes the kind,
  `generator:<path>` for a generated kind, or `hand` (tr1:186-187). The forms are `fields`, `header`
  and `rows`, and only `fields` is graded by tr1 S4 (tr1:174-176). Where tr1 S9's verb has no flag for
  a column, name the column's value and say the build run sets it through tr18's landed verb.
- **A typed record kind.** oc42 S2, S3 and S5 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list, read a `-<kind>-<n>.md` file whose Serves
  kind differs as malformed, and keep the closed kind list in the HYGIENE template (oc42:25, :35-49,
  :57). `RECORD_KIND_TOKENS` is the four untyped tokens plus `TYPED_RECORD_KINDS` (tr18:76-80); no
  registry row joins it on its own. `journal` is a read-only alias and writers write `log`
  (tr18:79, :95). The door `gov_record.py new <kind>` renders a `**Serves:**` line and one
  `- **<Key>:** ` line per field (tr2:51-54), and adds no validator (tr2:60).
- **A leg.** oc7 S3 reds a leg with no `enforces`, and the pending list only shrinks after
  dOrderedCharter's pass (oc7:58-63). wb11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row holding every manifest key, `enforces` among them;
  `leg_factory.py --write` renders `tools/gate-legs.json`, and `--check` reds a manifest that differs
  (wb11:36-49, :57-58). A spec that adds, reshapes or re-guards a leg does it in the declaration with
  `leg_factory.py new`, names its `enforces` (a clause's tag where the unit has one, else the
  `practice.*` tag whose break the leg's red reports, wb11:190-194), and an AC reads it. tr8:104 and its
  AC10 are the precedent. Where a later unit (ll52 S32 to S35) re-declares an earlier unit's leg, both
  say the same `enforces`, and the earlier unit no longer hand-writes `tools/gate-legs.json`.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205; wb28:63-64).
  Code in one kit reaches another kit's verb by subprocess, found through an inline `resolve_kit_dir`.
  In memory-tree a policy key is read through tr8 S10's `tools/memory-tree/policy_value.py` adapter,
  which runs `policy.py get`; elsewhere through the kit's own adapter or `policy.py get` by subprocess
  (oc7:379-380). A hook spawns `node <policy kit>/policy-mirror.js get <key>` instead of `require`-ing
  it (ks8:62-66). Shared code is carried inline under a parity row. Where the verb does not exist,
  write a §8 fork open for the owner: an ask to the kit's owning build for the verb, or a declared
  `requires_if` row like `tools/memory-tree/kit.toml:8`, with the reason the rule admits it. Recommend
  one.
- **The loop program's rows.** dl12 S1 to S3: one actor per item (dl12:125), `inputs` required for a
  non-role actor and each naming a layer tag of `tools/playbook/layers.toml` (dl12:43, :127),
  `returns` written `record-kind.<name>@<n>` (dl24:144-145; tr18:52-56 joins only that form), every
  route naming a declared item, `transition` or `stand-in` (dl12:41-42), and `routes` holding exactly
  the outcomes as keys (dl12:147-148). `program = "adopt"` in place of `step` stays ll8 F2's open ask.
- **An ask.** No dLinkedLibrary spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, and no other:

- **Group A, record kinds and the factory, led by spec 1:** specs 1, 3, 8, 13 and 22.
- **Group B, legs, led by spec 7:** specs 7, 9, 10, 14, 23, 46, 47 and 52.
- **Group C, sibling kits, led by spec 2:** specs 2, 4, 12, 16, 17, 19 and 74.

The spec files are `memory/builds/dLinkedLibrary/spec/2026-10-2?-spec-TOOL-dLinkedLibrary-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-beautiful-lalande-23ce8b/a46c346a-6f74-4403-a01d-0c3480a8d930/scratchpad/ll-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows; each row's `Change:` in the returns record is the starting point:

1. **Spec 1** (rows 1, 4, 5). The `decision` row's `new` call spells every column; the reuse-proposal
   record is written as `log` (through the door or by the module); `reuse.propose` and
   `decisions.major` are read through memory-tree's `policy_value.py`.
2. **Spec 3** (row 11). The `recall-index` row's call spells every column, and its `writer` is a
   command or `generator:<path>`, not a function.
3. **Spec 8** (rows 22, 24, 25, 26, 27). The `census`, `ruling` and `baseline` calls spell every
   column; drop the claim that tr18 S7 admits door kinds, and join `census` and `ruling` to
   `TYPED_RECORD_KINDS`, the factory's per-kind table and the HYGIENE closed list (Files touched gains
   `tools/memory-tree/tree_lib.py`); the item rows meet dl12 and dl24; the `retrofit.*` keys are read
   through `policy_value.py`. F2 stays open.
4. **Spec 13** (rows 39, 40). The `research-return` call spells every column; drop the door as a
   writer of the `kind:` line, or write the fork for an ask to dTotalRecall that the door render a
   declared line.
5. **Spec 22** (rows 64, 65, 66). The `gotcha` call spells every column; register it as the `header`
   form graded by `gotchas selftest`; read `platforms.supported` through `policy_value.py`. Keep spec
   52 S10 to S12's `ruling` wording consistent where it cites S4.
6. **Spec 7** (rows 20, 21). Its three legs are declared through `leg_factory.py new` (two in
   `tools/memory-tree/kit.toml`, the read-hook's in `tools/hooks/kit.toml`) with `enforces`, rendered
   by `--write`; `annotations-read.js` spawns `policy-mirror.js get` and finds bash without a policy-kit
   export.
7. **Spec 9** (row 33). Both `record origin` legs declared in `tools/memory-tree/kit.toml` with
   `enforces`.
8. **Spec 10** (row 34). The `retrofit progress selftest` leg declared with `enforces` in the kit that
   ships `retrofit_progress.py`.
9. **Spec 14** (row 43). The arm names ll46's `code record selftest` leg, not `code record`.
10. **Spec 23** (rows 67, 68). The `adopt instructions selftest` leg declared with `enforces` in
    `tools/playbook/kit.toml`; `item.adopt.instructions` spelled whole in dl12's schema, in ll8's
    shape, and AC8 grades it through `check_program`.
11. **Spec 46** (row 76) and **spec 47** (row 78). Name each new leg's `enforces`; an AC reads it from
    `tools/gate-legs.json`.
12. **Spec 52** (rows 80, 81, 82). S10 to S12 name the reader that closes the `Ruling` value set and drop
    the claim that a tr1 or tr2 check reads values; S32 to S35 name each leg's `enforces`, matching
    specs 7, 9, 10 and 23, and AC16 reads them; S17, S42 and S51 reach other kits by subprocess, a
    fork, or a declared `requires_if` row.
13. **Spec 2** (row 8). `house_index.py` reads `reuse.delivery` through its own kit's adapter or
    `policy.py get` by subprocess, not the playbook kit's `read_policy_value`.
14. **Spec 4** (rows 13, 15, 16). The `annotation-index` call spells every column; `TAG_RE` is carried
    inline under a parity row or checked by subprocess; each remaining cross-kit edge is a subprocess
    verb or a declared `requires_if` row. The spec's own "may import" reasoning goes.
15. **Spec 12** (row 38). The namespace row is read by memory-tree's own `record_extract` or as TOML
    data, not through the playbook kit's `read_namespaces`.
16. **Spec 16** (rows 47, 49). `code_record.py --dump --tree <rev>`; `replay_scorer.py` reaches
    `gov_code.py` and runlog by subprocess verbs, with the fork for the `callees` verb ll14 lacks, or
    declared `requires_if` rows.
17. **Spec 17** (row 52). `edge_grammar.py` reaches memory-tree's and codebase-map's readers through
    verbs printing JSON rows, or declared `requires_if` rows on `tools/playbook/kit.toml`.
18. **Spec 19** (row 56). `record_extract.py` reads `read_feature_nodes` through a codebase-map verb,
    or a declared `requires_if` row for codebase-map.
19. **Spec 74** (row 85). S26 validates `--build` and `--unit` by an inline parity copy of the two
    patterns, a memory-tree verb, or a declared `requires_if` row; keep spec 64 S14, which S26 amends,
    consistent, and name it in your return if you edit it.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-28, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-28, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes; replace text rather than append where a spec is near it.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `llN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### Non-goals

- No file outside the spec files of your group, but spec 64 for Group C's spec 74. No commit, no stage
  into the real index, no deviation record: the main loop writes those.
- No file of dTotalRecall, dBoundRoles, dKeptSession, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dPlacedRequest, dSafePassage or dGroundRules. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dTotalRecall's
re-ground brief,
`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md`, and its
rev-3 specs, as the precedent for how a revised spec reads.
