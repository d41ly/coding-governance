**Serves:** journal TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69

# Brief — dBoundRoles: seven unbuilt specs corrected before their dispatch

## The prompt

> Unit 60's spec needs a spec-writer fix before dispatch.

— owner, 2026-11-24, in the resume request for this run.

## The brief

### Goal

Seven specs of this build, each DEFERRED and unbuilt, are not conforming as they stand, so none of them is "already
present": revise each in place, as one rev bump on the existing file, and return each id as `authored`. Keep each
spec's status word `DEFERRED`, its tier, its base, its streams, its order verb and its `advances` verb.

### Items

1. Every one of the seven, TOOL-dBoundRoles-58, -60, -62, -63, -64, -66 and -69: the leg `agent-cap self-test` reads
   `spawn-guard self-test` wherever the spec names it as a leg that exists, in section 7 and in any sentence beside it
   that explains why it is named. TOOL-dBoundRoles-25 renamed it at `00a96bb43`, and the name in
   `tools/gate-legs.json` is the one a spec may hold. Where the spec already names the new leg, the old name leaves
   and the new one stands once. A sentence saying unit 25's pass will rename it is past now, so it says it did or it
   goes. A sentence quoting the old name as history stays. Then
   `python tools/check-spec-tokens.py --spec <spec>` prints no unwaived hit for that spec.
2. TOOL-dBoundRoles-60 only, its S10, S11, AC5 and whatever line of its section 1 table, section 3, section 4 or
   section 5 restates them. They ask unit 54's criterion to grep unit 49's S3 and AC2 bullets and its revision log,
   and they bump unit 49's CLOSED spec. Unit 54's rev-6 already took another route, its section 8 F3: unit 49's spec
   stays frozen, deviation record 543
   (`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-deviation-543.md`) carries the restatement,
   and 54's AC3 reads that record and an untouched spec 49. So ids 5 and 13 are closed by what unit 54 built. S10 and
   S11 state that end state and this pass records it, and AC5 observes it: the record read by
   `python tools/memory-tree/build_records.py read` with no malformed row and its Departs from, Approver and After
   rows, and the spec-49 diff over unit 54's pass commit printing nothing. Read 54's AC3 at its live revision and make
   AC5 red on a tree where the record is missing or spec 49 was edited. No bump of spec 49 is left anywhere in spec 60,
   its Files touched list included.
3. Change nothing else in any of the seven. Items that rev-bump a CLOSED spec are settled by the main loop's decision
   `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`. They are not
   rewritten here.
4. Each rev bump has its section 9 line, dated 2026-11-24, naming the sections and ids that moved and this brief.
5. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`. Pin any count. Never set a number
   before a counted noun in prose, and never set a section number beside one.
6. `python tools/check-spec-tokens.py --spec <spec>` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <spec>` exit 0 for each spec you revise before you
   return.

### Acceptance

`git grep -n 'agent-cap self-test'` over the seven specs prints only lines quoting the old name as history, spec 60
holds no bump of spec 49, and both checks of item 6 exit 0 for each of the seven.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but these seven specs.

### Limitations

The write grant is the seven specs' own files under `memory/builds/dBoundRoles/spec/`, and a writer edits only the ones
its own group holds.
