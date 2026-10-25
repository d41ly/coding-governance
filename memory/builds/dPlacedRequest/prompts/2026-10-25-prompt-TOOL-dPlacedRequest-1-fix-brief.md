**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21

# Fix brief — dPlacedRequest, the spec stage's gate hits

The 21 specs under `memory/builds/dPlacedRequest/spec/` were written by five writers from
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md`; read that brief's
"Every spec, whatever its unit", "Shared interfaces" and "Edges" sections first. Coverage is complete
(`carries.py --report dPlacedRequest` reads 21 clauses whole and 37 nodes named) and must stay so. Fix every hit
below by editing the named spec, and nothing else: no product code, no commit, no index render. A fix that changes
a spec's design is out of scope; a hit you judge false goes in your return with the reason.

Rules for each class:

- **[guards]**: add the named leg to the spec's §7 leg line. `python tools/check-spec-tokens.py --list` prints the
  legs a path trips.
- **[path]**: a path in a criterion must exist at HEAD. A file this build will CREATE is cited by its basename in
  §6 and by its full path in §2, §4 and Files touched. An illustrative path inside a fixture's input (`tools/a.py`,
  `docs/b.md`, `tools/kitx/a.sh`) is written so it is not read as a repository path: put the fixture's inputs under
  the fixture's own temporary directory and name them without a tracked-looking prefix, or describe them in prose.
- **[handoff]**: the receiving sibling's spec names the token in backticks where it reads it, or the handing
  bullet is corrected to the token the sibling does name. The brief's I11 spells the content key
  `request_content_key`; keep one spelling across units 4, 7, 14, 19 and 21. Unit 3 names `--card --lookup` if it
  calls it, else unit 2's bullet names what unit 3 reads.
- **check 12, one-sided edge**: add the missing reverse bullet in the producer's §3, naming the token the consumer
  names. Every edge runs from an earlier `order` to a later one.
- **check 12, conformance**: fill the skeleton placeholder; give the named acceptance bullet a backticked witness.
- **check 25**: each §2 item that retires a named thing carries a `**Readers:**` clause, `by name:` the readers
  that spell it and `by value:` the readers of its value or `NO VALUE READERS` and a reason, each found by
  `git grep` over the tree.
- Bump each edited spec's rev and add its §9 line naming what changed.

When done, run `python tools/check-spec-tokens.py` and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
(the specs are staged, so the hygiene gate reads them) and return each hit's disposition and the two final counts.

## The hits

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md [path] `tools/kitx/a.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md [path] `tools/kitx/b.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md [guards] `recall floor <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md [guards] `recall floor arms <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor arms', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md [guards] `recall floor <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md [guards] `recall floor arms <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor arms', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md [guards] `recall floor <- memory/guides/UNATTENDED-STOPS.md` — §4 files-touched names memory/guides/UNATTENDED-STOPS.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md [guards] `recall floor arms <- memory/guides/UNATTENDED-STOPS.md` — §4 files-touched names memory/guides/UNATTENDED-STOPS.md, which trips the guard of leg 'recall floor arms', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [guards] `recall floor <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [guards] `recall floor arms <- memory/guides/UNATTENDED-VERBS.md` — §4 files-touched names memory/guides/UNATTENDED-VERBS.md, which trips the guard of leg 'recall floor arms', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md [path] `skills/session-kickoff/card-store.fixture.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md [guards] `recall floor <- memory/guides/UNATTENDED-STOPS.md` — §4 files-touched names memory/guides/UNATTENDED-STOPS.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md [guards] `recall floor arms <- memory/guides/UNATTENDED-STOPS.md` — §4 files-touched names memory/guides/UNATTENDED-STOPS.md, which trips the guard of leg 'recall floor arms', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md [guards] `tier2-review self-test <- tools/memory-tree/gen_build_index.py` — §4 files-touched names tools/memory-tree/gen_build_index.py, which trips the guard of leg 'tier2-review self-test', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md [guards] `run-gates gov canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates gov canary', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md [guards] `measure-legs selftest <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'measure-legs selftest', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md [guards] `run-gates gov canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates gov canary', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md [guards] `measure-legs selftest <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'measure-legs selftest', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md [path] `tools/loop/probe.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md [path] `tools/a.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md [path] `./tools/a.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md [path] `tools/a.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md [path] `docs/b.md` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [handoff] `TOOL-dPlacedRequest-19>TOOL-dPlacedRequest-7:derive_request_content_key` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [handoff] `TOOL-dPlacedRequest-19>TOOL-dPlacedRequest-4:derive_request_content_key` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [handoff] `TOOL-dPlacedRequest-19>TOOL-dPlacedRequest-14:derive_request_content_key` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md [handoff] `TOOL-dPlacedRequest-19>TOOL-dPlacedRequest-21:derive_request_content_key` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md [handoff] `TOOL-dPlacedRequest-2>TOOL-dPlacedRequest-3:--card --lookup` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
HYGIENE check 12 FAILED — a §3 edge names a sibling that declares no matching edge back, so one author read the handoff and the other never saw it:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md (§3 declares **consumes-from** `TOOL-dPlacedRequest-11` and that unit declares no matching **hands-off** `TOOL-dPlacedRequest-14` back)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md (§3 declares **consumes-from** `TOOL-dPlacedRequest-13` and that unit declares no matching **hands-off** `TOOL-dPlacedRequest-15` back)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md (§3 declares **consumes-from** `TOOL-dPlacedRequest-13` and that unit declares no matching **hands-off** `TOOL-dPlacedRequest-2` back)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md (§3 declares **consumes-from** `TOOL-dPlacedRequest-1` and that unit declares no matching **hands-off** `TOOL-dPlacedRequest-4` back)
HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-13.md (unfilled skeleton placeholder)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC3
HYGIENE check 25 FAILED — §2 scope items of LIVE specs that retire a named thing, and every **Readers:** clause, must answer by name: with names a reader spells and by value: with a reader or NO VALUE READERS and a reason:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1, S5, S7
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-13.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1, S3
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S7
```
