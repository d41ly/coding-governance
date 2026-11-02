**Serves:** research TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15

# Fix brief — dScopedBuild, the spec stage's reds and the writers' disagreements

The five writers authored all 15 specs under `memory/builds/dScopedBuild/spec/`, staged and NOT committed. The main
loop ran `tools/check-spec-tokens.py`, the bootstrap `carries.py --report dScopedBuild` (green: 15 of 15 clauses
carried whole, 23 of 23 owned nodes named) and hygiene checks 2, 5, 12, 13, 21 and 25 over them, and read each
writer's return. Every item below is a finding in exactly the spec it names. Fix each in place and nothing else: no
new scope, no edit to a spec this list does not name. The specs have never been committed, so a fix stays at
`rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md`, its "Shared interfaces",
"Edges" and "What the last spec runs had to fix after their writers returned", before the first edit.

## `tools/check-spec-tokens.py` — three specs

- TOOL-dScopedBuild-10 AC2 cites `tools/x.sh`, and TOOL-dScopedBuild-11's criterion cites
  `memory/builds/tRun/BACKLOG.md`: both are planted fixture paths, not tracked, and the check reads them as
  repository citations. Spell each so the check does not read it as one (the fixture-relative path inside the planted
  clone, described in words, or passed as an argument), with the criterion's observation unchanged.
- TOOL-dScopedBuild-9's §4 Files touched names its own deviation record
  `memory/builds/dScopedBuild/build/2026-11-01-build-TOOL-dScopedBuild-9-deviation-91.md`, which trips the guards of
  legs `recall floor` and `recall floor arms`. A record of this spec run is not a product path the build run writes:
  remove it from §4 and keep the S8 citation.

## Hygiene check 25 — a retirement with no `**Readers:**` clause

Each §2 item below retires a named thing and carries no `**Readers:**` clause. Write one per item: `by name:` and every
reader that spells the name, then `by value:` and every reader of its value, or `NO VALUE READERS` and a reason; find
each reader with `git grep` over the tree, never from a record. If an item retires nothing and only a retirement word
made check 25 read it so, reword it instead.

- TOOL-dScopedBuild-13: S6, S8.
- TOOL-dScopedBuild-6: S1.

## The exit mode two writers minted twice — units 1, 3 and 14

TOOL-dScopedBuild-14 mints `routed_commits.py --build <slug>` and calls it inside unit 1's `check_build_exit`;
TOOL-dScopedBuild-3 mints `routed_commits.py --scope <slug> --write` and calls it from the `--build-exit` verb's
body, which `--close` never runs. Two exit modes of one host for one exit is two answers to one question, and a call
in the verb body leaves the unattended exit unscoped. Settle it so that:

- one mode exists, `routed_commits.py --build <slug>` (unit 14's, the earlier order), and unit 3 adds its scope arm
  and its `scope` record write to that mode rather than minting `--scope`; unit 9's touch join, which runs inside
  unit 3's check, rides the same mode;
- every exit arm of this build (units 3, 4, 7, 14) is called from inside unit 1's `check_build_exit`, never from a
  verb body, so `--build-exit` and `--close` run the same set; check units 4 and 7 say so and fix the one that does
  not;
- unit 1's S4 and S5, which call `check_build_exit` pure and writing nothing, say what it writes once unit 3's scope
  record and unit 9's grace-file write run inside it (unit 3's §8 F7 reads that as "no run-state file"): reword unit 1,
  and keep unit 3's F7 consistent with it;
- unit 3 names `read_gate_value`, `render_gate_outcome` and `write_gate_asks` exactly as unit 14 spells them (its
  writer says it does: verify), and unit 3's §3 edge to unit 1 and unit 1's reverse name the same tokens.

Edit units 1, 3 and 14 (and 4, 7 or 9 only where a call site or a token above is wrong in them).

## The write-set reader — unit 3

TOOL-dScopedBuild-3's `read_unit_writes` reads the dispatch rows in Python, taking every row that names the unit,
beside `read_pass_declarations` (`tools/unattended/lib-unattended.sh:1105-1112`), whose comment says it is the only
reader and which keeps only the latest key. Unit 5 grades the same write set through unit 3. Make unit 3's reader
agree with `read_pass_declarations`' semantics (latest declaration wins) or state in its §8, as a resolved fork by the
rungs, why the union is right and what the shell reader then owes; never leave two readers giving two answers.

## The acceptance reader — units 13 and 15

TOOL-dScopedBuild-13 (order 15) moves `AC_HEAD`, `AC_LABEL` and `extract_acceptance` from `tools/check-spec-tokens.py`
into `design_lib.py`, and its writer asks every other reader of a spec's §6 to import them from there. If
TOOL-dScopedBuild-15 (order 10) reads a spec's §6 through those names, a unit built at order 10 would import what an
order-15 unit creates: then move the move into unit 15, with a `hands-off` 15 → 13 on `extract_acceptance` and its
reverse. If unit 15 does not read them, change nothing and say so in your return.

## The build method's byte budget — units 2 and 13

`memory/guides/BUILD-METHOD.md` is 29354 bytes against M1's 30720-byte budget, and units 2 and 13 both edit M8 through
`tools/memory-tree/BUILD-METHOD.template.md`. Each spec that edits it states its byte delta; make the two deltas sum
inside the budget's 1366 spare bytes, rewording the smaller-change spec where they do not, and say the sum in your
return.

## Return

For each item: the spec and section you changed, or why no change was owed. Then rerun
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and report its verdict on these files. Write nothing
outside `memory/builds/dScopedBuild/spec/`, commit nothing, run no generator.
