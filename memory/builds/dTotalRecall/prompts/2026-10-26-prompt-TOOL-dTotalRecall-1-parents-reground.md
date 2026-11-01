**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-15 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-43 TOOL-dTotalRecall-76

# Brief: dTotalRecall's specs re-grounded against dDeclaredLoop's, dWitnessedBar's and dPlacedRequest's landed specs

## The prompt

> Have `gov-spec-writer` agents revise only the mismatched specs. The main loop never edits a spec.

— the dClosedLoop housekeeping session's hand-off to this session, 2026-10-26, relaying the owner's
hold on the next four spec runs until this wave lands.

## The brief

### Goal

Revise the 15 dTotalRecall specs that the cross-check record names under "For the re-ground". Each one
should state its parents' surfaces the way their specs now spell them on origin/main at `c8d46e188`:
dDeclaredLoop as its re-ground `783f1ad3a` left it, dWitnessedBar as `443775a2f` left it, and
dPlacedRequest as `2740f0a3d` left it. Each spec keeps its own design, and only its assumptions about
the parents change.

### Items

Read the cross-check record first,
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`. Its
summary table numbers every assumption (rows 1 to 64), and "The mismatches, both sides quoted" gives
both sides of each MISMATCH. Read each parent spec the record cites, at the lines it cites. This brief
summarises them, and where the two differ, the specs win. Before you edit for a row, re-read both
sides. A row the parent's text does not bear out is not edited: return it as refused, with the line
that refutes it.

Facts every revision uses:

- **A typed record kind.** dOrderedCharter unit 42 S2 and S3 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list, refuse at import a factory table that
  differs from it, and read a `-<kind>-<n>.md` file in `build/` whose Serves kind differs as malformed
  (oc42:35-49); S5 keeps the closed kind list in the HYGIENE template (oc42:57-59). A spec that adds a
  kind joins all three in its own pass. `RECORD_KIND_TOKENS` becomes the untyped tokens plus
  `TYPED_RECORD_KINDS` (oc42:35-39).
- **No `new <kind>` door.** The parents claim no `build_records.py new <kind>` verb: whether `new` is
  generic per kind is unknown until dOrderedCharter unit 7 builds (dl16:53-56; pr7:104-106;
  pr2:115-116; wb14:63). A writer names the parent's own command or the factory and its per-kind
  flags, and says the build run re-grounds the call on the landed factory.
- **A leg.** dOrderedCharter unit 7 S3 reds a leg with no `enforces`, and the pending list only
  shrinks after dOrderedCharter's pass (oc7:58-63, :227-228). dWitnessedBar unit 11 declares each leg
  once, in a kit's `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row holding
  every manifest key, `enforces` among them; `leg_factory.py --write` renders `tools/gate-legs.json`,
  and `--check` reds a manifest that differs (wb11:36-49, :73-74). A spec that adds, reshapes or
  re-guards a leg does it in the declaration, names its `enforces`, and an AC reads it. Under
  `core.bypass = never` a guarded leg with `enforces` reds (oc7:109-111); wb11 F5 is open on it.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205; wb28:63-64).
  Code in one kit reaches another kit's verb by subprocess, found through an inline `resolve_kit_dir`
  block; a policy key is read by `policy.py get` as a subprocess (oc7:379-380). Where the verb does
  not exist, write a §8 fork open for the owner: an ask to the parent for the verb, or a declared
  `requires_if` row like `tools/memory-tree/kit.toml:8`, with the reason the rule admits it.
  Recommend one.
- **dPlacedRequest's lease.** `--claims` prints fields 1 to 5 only, with no session (pr1:206-208,
  :396-397); `read_claims` fetches `refs/gov/leases/*` from the remote into its cache namespace
  (pr1:76-77).
- **An ask.** No dTotalRecall spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, record kinds and the factory, led by spec 1:** specs 1, 2, 4, 19, 25 and 43.
- **Group B, legs, led by spec 8:** specs 8, 9, 11, 15, 22, 26 and 76.
- **Group C, sibling kits, led by spec 18:** specs 18 and 20.

The spec files are `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`. Write
probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-silly-jang-ffa5af/b141ae93-c1d4-4429-8ac9-f3aa88a427dc/scratchpad/tr-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (rows 2, 4, 5, 6).
   - Each factory kind's `writer` names the parent's own command, or the factory and its flags,
     re-grounded at the pass; the `new probe` example goes.
   - F1 re-cites pr1:145-146 and keeps its two asks as preconditions.
   - The `record-kinds` leg's `enforces` holds the binds of the `kind.record-kind` row, and an AC
     observes it.
   - The registry rows the four untyped tokens and joins the factory side through
     `TYPED_RECORD_KINDS`, so `deviation` has one row, a factory kind with its source in the factory.
2. **Spec 2** (rows 8, 9). The lease holder is read through a surface that exposes `session` and
   `fleet-tag`, or the fork for an ask to dPlacedRequest for a `--claims` column or holder verb. AC5
   plants the lease on the fixture's bare remote.
3. **Spec 4** (row 17). The routing region gives every `TYPED_RECORD_KINDS` member's records a route:
   a purpose listing them, or one row per typed kind.
4. **Spec 19** (rows 38, 39). The causes check meets the parents' typed kinds that declare no
   `Caused-by` (pr2:107-108, pr7:93-96, wb1:78-79): write the fork with its options (those kinds as
   roots, a registry exemption, asks to the parents for the field, or the cause read from the Serves
   unit) and recommend one. S12 names the leg's `enforces`.
5. **Spec 25** (row 45). `stream-plan` joins `TYPED_RECORD_KINDS`, the factory's table and the HYGIENE
   list, or drops the typed `-<n>.md` name; if the fence schema cannot be a factory row, say so and
   have `check_stream_plan` apply oc42 S3's two-way name join itself. Keep spec 43 S9 consistent.
6. **Spec 43** (rows 49, 50). It is at 48839 bytes: replace text, never append. S29 adds a non-empty
   `enforces` to each leg's rows and AC29 reds a leg without it. S4's factory-kinds writer names the
   factory and its per-kind flags, not a `new <kind>` verb, and S4 and AC4 say the build run
   re-grounds the call.
7. **Spec 8** (row 25). S13 names the `code record` leg's `enforces`, and a criterion reds a
   declaration without it.
8. **Spec 9** (row 27). S4 and Files touched edit the `recall floor` guard in its `[[exempt_leg]]`
   declaration (`tools/govkit/registry.toml:380`) and regenerate with `leg_factory.py --write`.
9. **Spec 11** (rows 29, 30). S6 names the `shape-run records` leg's `enforces`, with an AC;
   `shape-run` joins the HYGIENE template's closed kind list and its render, with an AC.
10. **Spec 15** (row 32). Both `map` legs carry `enforces` in their declarations, with a criterion;
    §5 names the guard's red under `core.bypass = never` until wb11 F5 settles.
11. **Spec 22** (row 43). S6 declares `edge cardinality` through the leg factory with `enforces` in
    its own pass, and AC7 checks `enforces`.
12. **Spec 26** (row 46). S10 names `atlas selftest`'s `enforces` in its `[[gate_leg]]` row, and AC14
    checks it.
13. **Spec 76** (row 58). S16 confirms or adds the `record causes` row's `enforces` beside `reads`, and
    AC10 prints it.
14. **Spec 18** (rows 34, 36). `read by` derives from something declared: an ask for a typed input
    reference, or the role read keys alone with items dropped, since an item input names a layer tag
    (dl12:43, :111). The roles kit's constants are read by `ast.literal_eval` over the file text, a
    roles verb by subprocess, or a declared `requires_if` row.
15. **Spec 20** (rows 40, 41). S5 reads `memory.legacy-anchors` through govkit's own
    `read_policy_value` (TOOL-dSafePassage-9 §4) or `policy.py get` by subprocess, not oc19 S8's
    playbook module. S1 and S4 reach memory-tree by subprocess (`gen_build_index.py --print-bindings`
    exists), with the fork for a front-matter print verb, or state the in-process load as an exception
    with its reason.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-26, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-26, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `trN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### Non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No file of dOrderedCharter, dDeclaredLoop, dWitnessedBar, dPlacedRequest, dSafePassage or
  dGroundRules. A parent spec that looks wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dWitnessedBar's
re-ground brief,
`memory/builds/dWitnessedBar/prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md`,
and its rev-3 specs, as the precedent for how a revised spec reads.
