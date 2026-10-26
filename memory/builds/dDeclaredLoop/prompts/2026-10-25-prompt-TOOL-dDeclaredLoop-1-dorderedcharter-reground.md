**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56

# Brief: dDeclaredLoop's specs re-grounded against dOrderedCharter's landed specs

## The prompt

> Cross-check and re-ground three landed dClosedLoop chain spec sets against their re-grounded
> ancestors, in dependency order, and land each one. [...] Have `gov-spec-writer` agents revise
> only the mismatched specs.

— the dClosedLoop housekeeping session, 2026-10-25, relaying the owner's hold on the dBoundRoles,
dTotalRecall and dKeptSession spec runs until this re-ground lands.

## The brief

### Goal

Revise the 20 dDeclaredLoop specs that the cross-check record names under "For the re-ground", so
each one states dOrderedCharter's surfaces the way dOrderedCharter's landed specs spell them at
`462d20f35`. Each spec keeps its own design, and only its assumptions about dOrderedCharter change.

### Items

Read the cross-check record first,
`memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 127). "The mismatches, both sides quoted"
gives both sides of each MISMATCH as `dlN:L` and `ocN:L`. The dOrderedCharter specs are under
`memory/builds/dOrderedCharter/spec/`. Read each one the record cites, at the lines it cites. This
brief summarises them, and where the two differ, the specs win. Before you edit for a row, re-read
both sides. A row the parent's text does not bear out is not edited: return it as refused, with
the line that refutes it.

Facts every revision uses:

- **A new leg's `enforces`.** dOrderedCharter unit 7 S2 adds `enforces` to `tools/gate-legs.json`
  rows, and S3's meta-check reds any leg that carries none (oc7:55-63). The only excuse is a `leg` row
  of `tools/playbook/core-pending.txt`, a shrink-only list written once at dOrderedCharter's build
  pass (oc7:228). dOrderedCharter builds before dDeclaredLoop in the chain, so no dDeclaredLoop unit
  can add a row there. Every leg a dDeclaredLoop unit adds therefore carries `enforces` in that unit's
  own pass. The value is the principle tags the leg enforces, `principle.p<n>` from unit 7 S1's registry
  (oc7:50-51). The unit's acceptance criteria observe it the way spec 6's AC8 does. Where no
  principle fits a leg, write a §8 fork and do not invent a tag. A `[[kind]]` row out of the pending
  list names a `factory` that exists and a `gate` leg whose `enforces` holds every tag of the row's
  `binds` (oc7:72-74). dOrderedCharter unit 50's owed-rows probe never owes `enforces`
  (oc50:46-53), so a "rows a new leg owes" list built only from it leaves `enforces` out.
- **A typed record kind.** dOrderedCharter unit 42 S2 makes `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list. `build_records.py` refuses at import any
  kind table that differs from it (oc42:40-44). Under S3, a `-<kind>-<n>.md` file in `build/` whose
  Serves kind is not `<kind>` is malformed (oc42:45-49, :158-161). S5 keeps the closed kind list in
  `tools/memory-tree/HYGIENE.template.md`. A unit that adds a record kind therefore adds it to all
  three, in the same pass. Its records serve as `<kind> <id>`, never `journal`. One criterion
  observes the record bind: `print-bindings` names it. Whether `build_records.py new <kind>` is
  generic per kind is unknown until unit 7 builds (record rows 17, 43 and 60). State the flags your
  unit passes, and do not claim the door exists for your kind.
- **The composition's revision.** dOrderedCharter unit 46 S1 (rev-3) makes the overlay's landed
  revision `HEAD`, the node's own last commit, not dGroundRules' remote-ladder ref (oc46:42-47). Under
  S6, every `policy.py get` the composition makes passes `--rev HEAD` (oc46:65-71), and no caller reads
  another revision (oc46:78). Unit 35 S5 (rev-4) reads `instructions.exclude` that way (oc35:60-67),
  and unit 36 S4 reads the tag-valued keys the same way (oc36:183-189). Composing at an older pin
  with the parent's code as specced therefore mixes the pin's rows with `HEAD`'s policy values, which
  is the split oc46 AC5 reds. Spec 26 owns `compose_at`, and specs 27, 28 and 33 compose through it. Write
  the choice once in spec 26 as a §8 fork resolved on rung 1, and point at it from 27, 28 and 33. The
  options:
  - (a) `compose_at` composes in a scratch worktree detached at the pin, so every `--rev HEAD` read
    reads the pin and the parent is used as specced.
  - (b) an ask to dOrderedCharter for a `rev` threaded through `compose_rows`, `check_rows` and
    unit 46 S6.

  Recommend (a) unless reading the parent's text rules it out, and say what it costs.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4). dOrderedCharter unit 11 S4
  (rev-3), unit 19 S8 (rev-4) and unit 33 S3 (rev-3) restate this and run the sibling's verb as a
  subprocess, finding it through an inline `resolve_kit_dir` (oc11:90-94, oc19:99-102, oc33:90). A
  dDeclaredLoop unit in one kit that calls into another kit does the same. Where the verb it needs
  does not exist, it writes a §8 fork open for the owner. The options are an ask to dOrderedCharter
  for the verb, or a declared `requires_if` import row like `tools/memory-tree/kit.toml:8`, with the
  reason the rule admits it. Recommend one.
- **The owner proof.** dOrderedCharter unit 15 S5 (rev-5, the owner's pick, §8 F4) tests
  `sys.stderr.isatty()`, the stream dGroundRules' guard tests with `[ -t 2 ]`. Unit 7's
  `owner-only-expiring` proof is that check (oc15:77-81, :346-348). Any shared proof block tests stderr.
- **An ask.** No dDeclaredLoop spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  dOrderedCharter change, write a §8 fork open for the owner, with its options and a recommendation,
  and name the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, legs and records, led by spec 1:** specs 1, 3, 6, 16, 17, 22, 46 and 56.
- **Group B, composition and rows, led by spec 26:** specs 24, 25, 26, 27, 28 and 33.
- **Group C, kit seams and the proof, led by spec 12:** specs 2, 4, 5, 12, 18 and 34.

The spec files are `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-amazing-roentgen-42b269/e5868d60-4c6d-4ccd-a640-f987e8390bd7/scratchpad/w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any dOrderedCharter spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (rows 3, 7). AC9 compares the ordered drive rows, `drive --list` or the rendered region,
   line for line with their base-order copy, since `drive --check` tests membership (oc6:62-66).
   `loop definition` carries `enforces`.
2. **Spec 3** (rows 16, 18). Transition records serve as `transition <id>`, with the kind added to
   `TYPED_RECORD_KINDS` and the HYGIENE template. Restate the flood argument (dl3:133-134) on that
   binding. `loop transition record` carries `enforces`.
3. **Spec 6** (rows 32, 36). S1 cites unit 7 at rev-5 and names `core.py kinds` as a reader of the
   `kind` rows. Whether a landed `kind` pending row reds as stale is unknown until unit 7 builds
   (row 33): say so, and do not rest S1 on it. `loop factories fixtures` carries `enforces`.
4. **Specs 16 and 22** (rows 42, 59). Add `tree_lib.py` and the HYGIENE template to Files touched, and add
   the binding criterion.
5. **Spec 17** (rows 46, 47). Acceptance records serve as `acceptance <id>`, with the kind joined.
   `loop computed witness` carries `enforces`.
6. **Spec 46** (row 123). §4 Evidence states the `KNOWN` key set as it will be once dOrderedCharter
   lands, with `enforces` in both copies (oc7:167, oc50:37-39). S1's edit and AC1 are read against that set.
7. **Spec 56** (row 126 and the `enforces` rows). S4 takes only the `[[gate_leg]]` part from
   `owed_rows.py`. It keeps its own list for `enforces` and drops the `core-pending.txt` fallback. It
   rejects an `[[exempt_leg]]` row as an answer. Its table gains rows for units 3, 4, 17 and 27 if they
   are missing. It is at 44698 bytes, so replace text and do not append.
8. **Spec 24** (row 68). A `floor=` source is refused before its namespace registers (oc36:160-162).
   Use a source that is registered by order 24, or name the unit that registers `floor` first.
9. **Spec 25** (rows 74, 77). `exit` is fixed, or takes an ordered-list `widens`, because `add` is legal
   only on a set (oc36:155-156). The `removes` plant commits `.governance/policy.toml` with
   `[instructions] exclude = ["step.test"]` at the fixture's `HEAD`, and says the exclusion is the
   policy key.
10. **Spec 26** (rows 81, 82, 83). The composition revision is `HEAD`, as unit 46 S1 states. For a pin,
    write the fork above. A kind's `population` may be a reader command (oc7:69). Say how one is read
    at a revision; under option (a) it runs in the worktree. Re-date §9's stale "read at base
    `ed497191`" (dl26:250).
11. **Spec 27** (rows 91, 93, 99, 101, 103).
    - The factory writes gov-pack rows only. An adopter tag goes through unit 15's write door
      (oc35:122-123, oc15:72-74), or the factory prints a proposal.
    - The namespace row is unit 19 S2's, and you fill its required fields.
    - The pin follows spec 26's fork.
    - The scenario kind's reference page needs a `[[reference]]` row, a class in
      `tools/govkit/surface-classes.toml` and a `usage.toml` row, under unit 37's rev-4 (oc37:82-96).
      Otherwise defer the page by name. Either way, `help/reference/kinds.md` re-renders in the commit
      that adds `kind.scenario`.
    - `kind.scenario` names `binds` and `gate`, and its legs carry `enforces`.
12. **Spec 28** (rows 106, 107). A change record's `Before` and `After` are `<tag>@<hash8>` or `none`.
    Its `Action` is one of `WRITE_VERBS` (oc15:98-100, :180). Carry the proposed rows where the kind
    admits them, and map the four acts onto `WRITE_VERBS`. Where neither works without a parent
    change, write a fork. Drop "already carries rows".
13. **Spec 33** (rows 112, 114). The pin follows spec 26's fork. A numeric loop bound declares a
    direction unit 36 admits, such as an ordered list of its admitted values (oc36:61-64), or the
    spec writes the fork for an ask.
14. **Spec 2** (row 12). `check_terminal_proof` tests stderr. A typed `yes`, if kept, belongs only to
    `policy_edit.py`, outside the parity block. AC8 redirects stderr, not stdin, and the spec cites
    unit 15 F4 as the owner's settlement.
15. **Spec 4** (row 23). `loop stage coverage` carries `enforces`.
16. **Spec 5** (row 26). The unattended kit imports `resolve_compare_base` from
    `tools/memory-tree/coverage_join.py`. `tools/lib/` is gov-internal (oc19:115-119).
17. **Spec 12** (row 39). `loop_lib.py --check` runs `load_sets.py derive` as a subprocess through
    `resolve_kit_dir`, and prints `unarmed` when the playbook kit is absent. `derive` takes no item
    argument (oc11:201), so write the sibling-kit fork.
18. **Spec 18** (row 55). The policy join reads the policy kit by subprocess, not by import, and says
    what an unknown key reads as. Restate AC6's "Red when" against that call.
19. **Spec 34** (row 119). `pins.py` is reached by subprocess or by a declared `requires_if` import.
    Write the sibling-kit fork, since `derive_change_mark` has no verb (oc33:209-211).

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-25, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option dOrderedCharter now rules out is re-resolved on rung 1, naming
  the parent, and marked `RESOLVED (agent, 2026-10-25, delegated)`. A fork this brief tells you to
  leave open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does. None of
  dOrderedCharter's files is tracked until it builds.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `dlN:L`
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
- No dOrderedCharter, dSafePassage or dGroundRules file. A parent spec that looks wrong is a line in
  your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

dOrderedCharter's specs as the interface. The cross-check record as the map of what moved.
dOrderedCharter's own re-ground brief,
`memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md`,
as the precedent for how a revised spec reads.
