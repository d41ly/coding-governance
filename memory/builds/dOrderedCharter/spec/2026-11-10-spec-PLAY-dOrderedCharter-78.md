# PLAY-dOrderedCharter-78 — the close's three parked fixes: the renderer requires the kits it reads, an adopter's tags check unarms what it does not hold, and A25r asserts its whole slice

**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base dfe4edb9f · streams playbook · order 37 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-PLAY-dOrderedCharter-78-1-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-78-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-78-spec-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-78-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close parked three reds for the owner, and the owner took the recommended option for each
(`memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-owner-fork-picks.md`).
This unit builds those picks: the playbook renderer declares the memory-tree and policy kits it reads,
and the acceptance matrix's scratch install carries them; the tags check skips an owner the target's
own chain registry does not hold, printing an unarmed line; and A25r asserts check 8 branch 1's whole
signature so its pin row leaves. The pass leaves the govkit acceptance matrix and the harness-arms leg
green over the tree, and an adopter's tags check green in a scratch install. It also has the runlog
kit's record write its one counted slot with a DERIVED mark, so a re-rendered run record no longer
reds the pinned-facts check until a row is added by hand.

## 2. Scope (IN)

- **S1** — The renderer's requirement. `tools/playbook/kit.toml` (entry `playbook-render`) declares
  `requires = ["playbook", "memory-tree", "policy"]`, its comment naming the two readers below. The
  `playbook` entry, `tools/govkit/entries/playbook.kit.toml`, keeps `requires = []`: its `[adopt]`
  argv is empty, so it runs no reader (section 4, Evidence). `tools/govkit/registry.toml`'s
  `[selection] default` gains `policy`, beside `memory-tree`, which it already holds (section 8 F1).
  Observed by AC1.
- **S2** — The matrix's scratch install carries what its entries require. In
  `tools/govkit/matrix.py#main`, shape 5 reads the descriptors before it writes the target's
  `deploy.toml`, and widens `SCRATCH_KITS` to its requirement closure by repeating
  `tools/govkit/govkit.py#derive_unsatisfied_requires` until it answers nothing. That closure is the
  `kits` list the target's `deploy.toml` declares and the `--kits` argument `apply` takes. The leg loop
  and `SCRATCH_EXPECT` stay over `SCRATCH_KITS` alone, and the comment above `SCRATCH_KITS` says the
  required kits ride along with their legs unexecuted. The pass runs once PLAY-dOrderedCharter-31 is
  CLOSED (section 8 F2). Observed by AC2.
- **S3** — The purpose arm's owner clause. `tools/playbook/tag_index.py#check_namespace_purpose`
  grades a row's `owner` only where the chain registry holds it. An owner it does not hold is
  collected in the returned state under `unarmed`, `{owner: rows}`, and is never red; the row's
  `purpose-source` is graded as before. `tools/playbook/gov_tag.py#run_purpose_check` prints one line
  per such owner,
  `tags: purpose · owner '<owner>' · unarmed: no build of <chain registry path>, <n> namespace row(s) not graded for it`.
  `tools/playbook/gov_tag.py#run_check` reads the chain registry once, through
  `tools/playbook/tag_index.py#read_chain_registry`, and hands the rows to `run_purpose_check` and the
  slugs to the native arm (S4). The plant `ghost-owner` keeps its fixture and its row in
  `tools/playbook/adopt-playbook.sh` is re-expected: exit 0, printing `owner 'dGhost' · unarmed`, and
  not printing `names no build of`. Observed by AC3 and AC6.
- **S4** — The native arm by the same rule. `tools/playbook/edge_grammar.py#check_native_classes`
  takes the chain registry's slugs as a third argument. A class whose `owner` is not among them
  prints `tags: native · <class> (owner <owner>) · unarmed: no build of the chain registry` and runs
  no resolver; a held owner's class is resolved and graded as today, `resolves nothing` staying red.
  `tools/playbook/gov_tag.py` gains two plants, built by `build_tags_fixture` and run through the
  check as `ghost-owner` is: `foreign-native` adds `DISCIPLINES="arch"` and `FAMILIES="arch:ARCH"` to
  the fixture's conf and a `[[native]]` row of class `family-id`, owner `dGhost`, pattern
  `id_grammar:grammar_for`, resolver `corpus_ids:--print-defined-ids` to its namespace registry;
  `held-native` is the same with owner `fixture`, the one build `FIXTURE_CHAIN` registers. Each gets a
  row in `tools/playbook/adopt-playbook.sh`'s tag block. Observed by AC4 and AC6.
- **S5** — The positional arm at a target with no memory tree. Where the list is absent and its own
  folder, `<MEMORY_ROOT>/project/`, is absent too, `tools/playbook/positional.py#check_positional`
  answers no red and prints
  `tags: positional · unarmed: <MEMORY_ROOT>/project is absent, so no memory tree is adopted here`.
  An absent list whose folder exists stays red, as today (section 8 F3).
  `tools/playbook/gov_tag.py#run_positional_plant` gains `positional-no-tree`, which commits the
  fixture without its `memory/project/` folder, and `positional-absent`, which commits it without the
  list alone; `SELFTEST_ROWS` in `tools/playbook/positional.py` gains a row for each. Observed by AC5
  and AC6.
- **S6** — The A25r arm. In `tools/check-template-size.test.sh`, A25r's expected text becomes the
  branch's whole signature, opening `). Lower the cap to CODEX_MAX or under`, as the pin row holds it.
  The row naming `tools/check-template-size.sh` check 8 ordinal 1 leaves
  `memory/project/unarmed-branches.txt` in the same commit, since check-arms reds a pinned branch that
  an arm reaches. Observed by AC7.
- **S7** — Docs. `help/tags.md`'s `purpose` bullet says that an owner the chain registry does not
  hold is printed `owner '<owner>' · unarmed` and never red, which at a repository that installed the
  kit is every owner, and its native-id paragraph says a class of such an owner prints `unarmed` the
  same way. The page names the positional arm's unarmed line where it lists the arms. `tools/playbook/README.md`'s purpose paragraph says the
  same in one sentence. `WIRE-INTO-PROJECT.md` section 2's `intake` line names
  `memory-tree,policy`, with one sentence that `playbook-render` requires both, and section 3i says the
  policy kit is in the default selection because the renderer requires it. Observed by AC8.
- **S8** — The run record's duration. In `tools/runlog/record.py`, `RECORD_SCHEMA`'s Summary fact
  `duration` takes two templates, `{duration} · DERIVED from the window` first and the bare
  `{duration}` second. `tools/runlog/record.py#render_markdown` writes the first, as every Summary fact
  writes `templates[0]`, so the line reads `- duration: <n>s · DERIVED from the window`; the record's
  check accepts either, so every run record already landed keeps its verdict. The `duration` class
  fills no other slot of the schema, so this is the class's whole population.
  `tools/runlog/selftest.py` gains the arm section 7 names. Observed by AC9.

## 3. Non-goals (OUT)

- The older readers' `no policy kit found` branches, such as
  `tools/playbook/render_playbook.py#render_override_line`, stay as they are; S1 makes them
  unreachable at a fresh install, and deleting them is a cleanup of its own.
- Any kit version bump by hand.
- Any edit to `tools/playbook/namespaces.toml`'s rows: the owner's pick fixes the class, not each row.
- Moving CODEX_MAX or re-pointing the `codex-instructions` cap row, which is PLAY-dOrderedCharter-31
  S1's.
- Grading the legs of the kits S2 adds to the scratch install: the matrix's stated ceiling over
  entries it does not grade stands.
- `.governance/deploy.toml`, gov's own selection, a guarded path the owner edits.
- A typo'd namespace owner at gov, which S3 no longer reds there (section 5, error states).
- The packet's coverage line, `over <n> specs`, written by the dClosedLoop carries instrument this
  build may not edit; it is the owner's act (section 8 F4).
- Re-rendering a run record already landed: S8 changes what the next render writes.

This unit rests on CLOSED units it does not declare as edges, since a CLOSED spec's text is frozen and
a consumes-from edge into one reds memory hygiene's edge check. PLAY-dOrderedCharter-22 built the
purpose arm and the `ghost-owner` plant S3 re-expects. PLAY-dOrderedCharter-28 built the native-id
classes S4 gates. PLAY-dOrderedCharter-72 moved the positional list under the memory root, whose AC6
observation at e517511e2 found the adopter reds S3 to S5 answer; PLAY-dOrderedCharter-70 built
`tools/playbook/render_playbook.py#write_empty_lists`, which seeds that list only where its folder
exists. PLAY-dOrderedCharter-6 minted A25 and PLAY-dOrderedCharter-77 S4 added A25r. PLAY-dOrderedCharter-77
S8 and S11 moved three legs to gov and announce four plant blocks unarmed where a sibling kit is absent,
and PLAY-dOrderedCharter-73 measured that `requires = ["playbook", "memory-tree", "policy"]` passes the
three plant legs it then held.

One dependency is on a unit that is not CLOSED. PLAY-dOrderedCharter-31, DEFERRED at order 36, moves
CODEX_MAX into the renderer in its S1 and adds `playbook-render` to the default selection by its F11.
AC2 holds only after the first, and S1's default change answers the second (section 8 F1, F2). It is
not declared as an edge because the edge join asks that unit's spec for the reciprocal hands-off line,
and this pass edits no other spec. The order fields carry it: 31 builds at 36, this unit at 37.

### Edges

none

## 4. Design

### Evidence

Read at dfe4edb9f; every commit after e517511e2 touches records only, so the bar's logs over e517511e2
stand for the code.

- The matrix log over e517511e2 shows three failures, all in shape 5: `apply` renders no region, so
  `playbook render wiring` finds no `AGENTS.md`, and `playbook render selftest` reports `61 of 185` arms
  failed behind `looked in ... install.json, ... policy` (PINNED, the leg's log over e517511e2).
- Reproduced by this writer at dfe4edb9f in a scratch install built as shape 5 builds it (PINNED). The
  `playbook-render` adopter dies in
  `tools/playbook/instruction_units.py#load_memory_tree_path`, reached from
  `tools/playbook/render_playbook.py#render_delta_report` through `overlay` and `instructions_edit`,
  with `no memory-tree kit holding design_lib.py`. With `memory-tree` added it refuses
  `the composition is refused: policy instructions.exclude: no policy kit found`, the read of
  `tools/playbook/overlay.py#read_excluded_tags`. With `policy` added too it refuses at the load set:
  `tools/playbook/load_sets.py#read_cap_answers` asks `tools/policy/budgets.py#read_cap_home` for the
  `codex-instructions` cap, whose home `tools/policy/caps.toml` places in the agent-instructions kit.
  With that kit added as well, the region renders. Every lookup is the `playbook-render` entry's;
  the `playbook` entry declares `[adopt] argv = []` and ships the template alone.
- `tools/govkit/govkit.py#_cmd_apply` refuses a selection whose requirement is neither selected nor
  claimed, and `tools/govkit/selftest.py#check_roles_default` asserts the default selection satisfies
  its own requirements. PLAY-dOrderedCharter-31 rev-13 S11, which builds first, puts
  `playbook-render` in that default and gives `tools/govkit/govkit.py#selfcheck`'s 7b arm a check that
  fails on any requirement the default leaves unmet; `policy` is not in the default at dfe4edb9f.
- The pinned-facts check at dfe4edb9f reds one fact, `676237s`, on the `- duration:` line of this
  run's record, `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md`;
  the record's Data line repeats it beside a sha, which pins it there (PINNED, this writer's run). The
  line is `RECORD_SCHEMA`'s Summary `duration` fact, written through `render_fact` from its first
  template; `tools/runlog/runlog.py`'s `record` verb only dispatches to it.
- The packet's `over 70 specs:` line (PINNED, the dOrderedCharter packet at dfe4edb9f) is written by
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py#report`, which
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` embeds, and not by
  `tools/memory-tree/gen_build_index.py`. That generator's coverage region writes `spec(s)`, which the
  fact pattern does not match. Each packet pins that instrument's blob, and the packet itself names
  `packet.py --repin`, the owner's at a console inside a chain run, as the only way a pin moves.
- `tools/govkit/govkit.py#_cmd_update` installs an entry the default gained since a receipt's vintage,
  so an existing adopter's unscoped `update` gains `policy` once S1 lands.
- The tags check over an adopter: PLAY-dOrderedCharter-72's ledger records an exit 1 there at
  e517511e2, ten namespace owner reds and the family-id native's `resolves nothing` (PINNED, its AC6
  line), with the positional arm's absent-list line beside them. `tools/playbook/namespaces.toml`
  names `dOrderedCharter` for every namespace row and for the `family-id` class, and no kit ships a
  `chain.toml`, so `tools/playbook/tag_index.py#read_chain_registry` answers no row at an adopter.
- The `resolves nothing` line is a red: `tools/playbook/edge_grammar.py#check_native_classes` appends
  it to its reds, and `run_check` adds those to the check's. `tools/memory-tree/corpus_ids.py#print_defined_ids`
  exits 0 with only its grammar line in a repository whose conf declares `FAMILIES` and that holds no
  record, which this writer reproduced at dfe4edb9f (PINNED).
- The positional absent line is a red too: `tools/playbook/positional.py#check_positional` returns it
  as its first, red element. `write_empty_lists` writes the list only where `<MEMORY_ROOT>/project/`
  exists, and a fresh install's memory-tree adopter seeds its conf and stops before making it.
- A25r asserts `Lower the cap to CODEX_MAX or under; ...`, and the pin row added at fd220d40b holds the
  signature with its leading `). `, which follows the `(exit $_hrc` field of `fail 8`'s text.

### The three readers, and what each no longer checks

The purpose arm's owner clause reds today only on an owner the chain registry lacks; after S3 that
case prints unarmed, so the clause reds nothing anywhere. At gov every owner is held, so gov's
verdict does not move. At gov the `one owner` leg still reds a namespace owner naming no build that
`memory/builds/` holds (`tools/playbook/writing_practice.py#check_one_owner`); a build folder present
and missing from `chain.toml` is caught by nothing.

The native arm reads no member list for a class whose owner is not held, so a populated class at an
adopter prints unarmed rather than its member count, and an adopter's own family ids are never counted
there.

The positional arm reads a whole absent `<MEMORY_ROOT>/project/` folder as unarmed, so a deletion of
the folder with the list in it is not red in this arm.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| no function | the changed functions take one more argument or one more branch | none |
| the plants `foreign-native`, `held-native` | `tools/playbook/gov_tag.py` `PLANTS` | the fixture's plant list |
| the plants `positional-no-tree`, `positional-absent` | the same, and `SELFTEST_ROWS` | the positional selftest's rows |
| the three unarmed lines S3 to S5 quote | `tools/playbook/gov_tag.py`, `tools/playbook/edge_grammar.py`, `tools/playbook/positional.py` | none |
| the state key `unarmed` | `tools/playbook/tag_index.py#check_namespace_purpose`'s return | none |

### Files touched (estimate)

- `tools/playbook/kit.toml`, `tools/govkit/registry.toml` (S1)
- `tools/govkit/matrix.py` (S2)
- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py` (S3, S4, S5)
- `tools/playbook/edge_grammar.py` (S4)
- `tools/playbook/positional.py` (S5)
- `tools/playbook/adopt-playbook.sh` (S3, S4)
- `tools/check-template-size.test.sh`, `memory/project/unarmed-branches.txt` (S6)
- `help/tags.md`, `tools/playbook/README.md`, `WIRE-INTO-PROJECT.md` (S7)
- `tools/runlog/record.py`, `tools/runlog/selftest.py` (S8)

### Rollout

Live at landing, in one pass commit, after PLAY-dOrderedCharter-31's. The pass first runs F2's
precondition and stops, handing back, where it fails. S6's arm and its pin row land in the same
commit. S1 and S2 land together, so no commit declares a requirement the matrix's install lacks.

### Alternatives rejected

| Option | Why not |
|---|---|
| The renderer's readers degrade where a kit is absent | The option the owner did not take; it was the close's second option |
| `requires_if` with no condition key for `policy` | A declaration that refuses nothing, so a default install still refuses at its render once `playbook-render` is a default |
| Editing each namespace row's owner | The owner's pick fixes the class |
| Unarming the purpose arm only where `chain.toml` is absent | An adopter that keeps its own chain registry still reds on gov's owners |
| Listing the required kits in `SCRATCH_KITS` | Their legs would join the graded set, and a typed list goes stale when a requirement moves |

## 5. Production-readiness checklist

- security: N/A — no write path, input boundary or grant changes. S1 widens every default install by
  the policy kit, whose adopter writes `.governance/policy.toml` only where none exists.
- perf / scale: S2 adds two kits' copy and adopter to one matrix shape. S4 skips a resolver run per
  unheld class.
- error / empty / loading states: each arm the pass touches prints a named unarmed line for what it
  does not grade, never a silent skip. What S3 does not check: an owner missing from the chain
  registry, at any tree. What S4 does not check: the members of a class whose owner is not held. What
  S5 does not check: a list deleted together with its whole folder.
- observability: the three unarmed lines name the owner, the class or the folder they skip.
- risks: the matrix's scratch install may red on a further arm once these clear; the pass hands that
  back rather than widening. The two native plants add `FAMILIES` to the fixture's conf, which other
  arms of the same check read; a red there names it. PLAY-dOrderedCharter-55 at order 41 edits the same
  tag files and builds after this unit.
- testing: AC1 to AC9, each a probe, a plant, a render or a grep; the suite arms are the `New arm:`
  lines in section 7. A `runlog selftest` arm may assert the schema's word that a fact's alternative
  carries no value slot, which S8's second template contradicts; the builder re-reads
  `tools/runlog/record.py#scan_time_slots`, which reads the first template only.
- migration: additive. An adopter's next unscoped `govkit update` gains `policy` as a default; one
  whose `update` is scoped by `--kits` keeps its selection and is told the requirement by `plan`.
- user docs: `help/tags.md` and `WIRE-INTO-PROJECT.md` (S7).

## 6. Acceptance criteria

A criterion that runs a leg's own checker, or a scratch install, is the main loop's at the close where
the builder's role may not run it.

- **AC1** — When
  `python -c "import sys, pathlib; sys.path[:0] = ['tools/govkit']; import govkit as g; r = pathlib.Path('.'); reg = g.load_registry(r); d = g.read_descriptors(r, reg, g.Report()); print(g.derive_unsatisfied_requires(['playbook-render'], d, None)); print(g.derive_unsatisfied_requires(list(g.default_kits(reg)), d, None)); print('policy' in g.default_kits(reg))"`
  runs after the pass, it prints the three edges `playbook-render` has to `memory-tree`, `playbook` and
  `policy`, then `[]`, then `True`. At dfe4edb9f it prints the `playbook` edge alone, `[]` and `False`.
  Red when: the renderer declares less than it reads, or the default selection leaves a requirement
  unmet.
- **AC2** — When `python tools/govkit/matrix.py` runs after the pass, it prints no line opening
  `FAIL scratch install:` or `FAIL default install:`, and it prints `ok` for
  `scratch install: apply RENDERS the region into the target's own charter` and for both lines of each
  of `playbook render wiring` and `playbook render selftest`.
  Red when: the scratch install lacks a kit the renderer reads, or the default install refuses a
  requirement.
  fixture: PLAY-dOrderedCharter-31 CLOSED; `git grep -n "agent-instructions" -- tools/policy/caps.toml`
  prints nothing, its S1 having moved the `codex-instructions` row to the renderer.
  cost: one matrix run, under the leg's ceiling in `tools/gate-legs.json`.
  permission: the main loop runs it at the close; a role agent's scratch guard refuses a scratch install.
- **AC3** — When
  `python tools/playbook/gov_tag.py --fixture --plant ghost-owner --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new`
  runs after the pass, it exits 0, printing `owner 'dGhost' · unarmed` and no line holding
  `names no build of`; at dfe4edb9f it exits 1 naming that red.
  Red when: an owner the chain registry lacks still reds, or reads silently.
- **AC4** — When the same command runs with `--plant foreign-native` after the pass, it exits 0,
  printing `family-id (owner dGhost) · unarmed` and no line holding `resolves nothing`; and with
  `--plant held-native` it exits 1, printing `family-id (owner fixture) · resolves nothing`.
  Red when: an unheld class still reds, or a held class that resolves nothing passes.
- **AC5** — When `python tools/playbook/gov_tag.py --fixture --plant positional-no-tree` runs after
  the pass, it exits 0, printing `tags: positional · unarmed: memory/project is absent`; and
  `python tools/playbook/gov_tag.py --fixture --plant positional-absent` exits 1, printing
  `tags: positional · the list memory/project/positional-refs.txt is absent`.
  Red when: a target with no memory tree reds on the list, or a deleted list beside its folder passes.
- **AC6** — When, in a scratch install made by the commands of `help/tutorial/adopt-gov.md` after
  `bash tools/playbook/adopt-playbook.sh --target .` there and a commit,
  `python tools/playbook/gov_tag.py check --base HEAD` runs after the pass, it exits 0, printing
  `owner 'dOrderedCharter' · unarmed`, `family-id (owner dOrderedCharter) · unarmed` and
  `tags: positional · unarmed`, and no line holding `names no build of` or `resolves nothing`. Over gov's
  own tree the same check prints no line holding `· unarmed: no build of`.
  Red when: an adopter's install reds on gov's owners, or gov's own owners go ungraded.
  permission: the tags leg is the main loop's, at the close, in both places.
- **AC7** — When `python3 tools/memory-tree/check-arms.py --check` runs after the pass, it prints no
  line naming `tools/check-template-size.sh`;
  `git grep -n "check-template-size.sh" -- memory/project/unarmed-branches.txt` prints nothing; and
  `git grep -c "). Lower the cap to CODEX_MAX or under" -- tools/check-template-size.test.sh` counts 1.
  Red when: A25r asserts less than the signature and the pin row is gone, or the row stays beside an
  arm that reaches it.
- **AC8** — When `git grep -n "owner '<owner>' · unarmed" -- help/tags.md` runs after the pass, it
  prints a line; `git grep -n "The kit is not in the default selection" -- WIRE-INTO-PROJECT.md` prints
  nothing; and `git grep -n "playbook-render,memory-tree,policy" -- WIRE-INTO-PROJECT.md` prints the
  section 2 `intake` line.
  Red when: a page still tells an adopter the owner red or the policy kit's absence from the default.
- **AC9** — When `python tools/runlog/runlog.py record dOrderedCharter` runs after the pass, the record
  it prints carries a line opening `- duration: ` and ending `· DERIVED from the window`; and once the
  main loop writes that render with `--write`, `python tools/playbook/writing_practice.py check pinned-facts`
  prints no red naming `2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md`.
  Red when: the render writes the bare count, or the mark sits where the fact pattern cannot see it.
  permission: the record's `--write` is the main loop's, a record of the run it is in.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `govkit selfcheck` · `govkit runbook parity` · `playbook render wiring` · `playbook render selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `template size gate selftest` · `tags (the resolver's checks)` · `tags positional selftest` · `docs` · `help page commands` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `writing practice (records and units)`

The guarded legs on the line are those the files touched trip: the four govkit legs for
`tools/govkit/`, the matrix and the render selftest for `tools/playbook/`, `policy fixtures` for the
two descriptors and the record module, both recall floor legs for
`memory/project/unarmed-branches.txt`, and the three run-log legs for `tools/runlog/`.

New arm: tools/govkit/matrix.py · covers AC2 · shape 5's install selection, whose apply dies on the memory-tree lookup before S2 · none
New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 · the ghost-owner row re-expected and the foreign-native row, each red before S3 and S4, beside the held-native control that stays red · none
New arm: tools/playbook/positional.py · covers AC5 · the positional-no-tree row, red before S5, beside the positional-absent control that stays red · none
New arm: tools/check-template-size.test.sh · covers AC7 · A25r over the 40960 cap A25 builds, read unarmed by check-arms before S6 · none
New arm: tools/runlog/selftest.py · covers AC9 · a rendered record whose duration line must carry the DERIVED form, red before S8, beside a record holding the bare form that the record check still grades clean · none

## 8. Open questions

- **F1 — Whether `policy` joins the default selection.** S1 makes `playbook-render` require it, and
  PLAY-dOrderedCharter-31 S11 makes `playbook-render` a default and fails selfcheck on any requirement
  the default leaves unmet. Options: (a) `policy` joins the default, `memory-tree` being in it already;
  (b) the default stays, and both unit 31's new selfcheck check and `check_roles_default` red, while
  a default `apply` refuses; (c) `requires_if` with no condition key, which declares and refuses
  nothing, so the default stays closed under `requires`. (b) refuses every default install. (c)
  leaves a default install whose render refuses at `instructions.exclude`, as section 4's second
  reproduction shows. (a) widens what every adopter installs by default by one kit, and an existing
  adopter's `update` gains it through the default-gained path. Recommendation (a).
  RESOLVED (agent, 2026-11-10, delegated): (a), the one option a default install renders under.
  widens: every default install, by the policy kit · relaxes: none
- **F2 — The `codex-instructions` cap's home until PLAY-dOrderedCharter-31 S1 moves it.** With the
  policy kit carried, the load set's harness read asks for CODEX_MAX in the agent-instructions kit,
  which the matrix's install lacks. Options: (a) build after unit 31, whose S1 moves the row to the
  renderer, with AC2's fixture line as the pass's first check; (b) `read_cap_home` answers no value for a
  cap whose kit the receipt does not claim, the rule `tools/policy/check_policy.py#arm_cap_census`
  already prints; (c) the matrix carries the agent-instructions kit too. (c) names an entry unit 31
  retires. (b) is code no install reaches once unit 31 lands. Recommendation (a).
  RESOLVED (agent, 2026-11-10, delegated): (a), with no code that outlives its reason. widens: none ·
  relaxes: none
- **F3 — The positional arm's absent list at a target with no memory tree.** The owner's pick names
  the owner and native reds; the same install reds a third time here. Options: (a) leave the arm, and
  AC6's install adopts its memory tree first; (b) `write_empty_lists` makes the folder; (c) the arm
  prints unarmed where the folder itself is absent. (a) leaves the tutorial's own install red. (b) makes
  `<MEMORY_ROOT>/project/` before the memory-tree adopter runs, the state its `refused-foreign-tree`
  outcome names. (c) is the pick's rule, skipping what the target does not hold. Recommendation (c).
  RESOLVED (agent, 2026-11-10, delegated): (c), the owner's rule applied to the third red. widens:
  none · relaxes: the positional arm, at a target whose memory project folder is absent
- **F4 — Who marks the packet's coverage count.** The count is written by the dClosedLoop carries
  instrument's `report`, which every chain build's packet pins, and the dOrderedCharter packet forbids
  this build to edit that instrument or move a pin. Options: (a) the owner edits the line to read
  `over <n> specs (DERIVED):` and re-pins with `packet.py --repin` at a console, outside this unit;
  (b) this unit edits the instrument, and every live packet's pin arm reds until the owner re-pins;
  (c) the pinned-facts check skips a file that names its generator; (d) the main loop keeps re-pinning
  the list row by hand. (b) breaks a rule the packet states and still needs the owner. (c) exempts a
  record class from a check, wider than one line. (d) is the hand edit made three times already.
  Recommendation (a), handed off. RESOLVED (agent, 2026-11-10, delegated): (a), handed to the owner,
  the one holder of the re-pin. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from `2026-11-10-prompt-PLAY-dOrderedCharter-78-spec-brief.md`
  and the owner's picks record. Every reader re-read at dfe4edb9f; the matrix's install reproduced
  four ways in scratch installs, which found F1's default conflict, F2's dependency on unit 31 and F3's
  third adopter red. Before its first commit it took the coordinator's two folds: F1 now meets
  PLAY-dOrderedCharter-31 rev-13 S11's selfcheck check, and S8 and F4 answer the two unmarked
  generated counts, the second found to be the carries instrument's and not the build index's.

## 10. Reuse audit

Every change extends a seam the tree holds; no mechanism is minted. S1 is the descriptor's own
`requires` and the registry's `[selection] default`. S2 reuses
`tools/govkit/govkit.py#derive_unsatisfied_requires`, the one predicate apply and plan share, rather
than a second closure. S3 to S5 extend the unarmed line the tag check already prints for a namespace or
class it cannot grade, and their plants extend `PLANTS`, `SELFTEST_ROWS` and the tag block of
`tools/playbook/adopt-playbook.sh#run_plant_rows`. S8 uses the schema's own alternative-template
form, which the `commitment` fact already declares, and the writing practice's DERIVED mark as the
pin. Run at dfe4edb9f,
`python tools/codebase-map/reuse_lookup.py "derive the requires closure of a kit selection"` ranked
`resolve_kit_dir` and the kit-path helpers and no closure helper, and
`python tools/codebase-map/reuse_lookup.py "skip a check whose subject the target install does not hold, printing an unarmed line"`
ranked generic `check` and `skip` names and no unarmed-skip helper, so each change is a branch in its
reader. The recall query returned PLAY-dOrderedCharter-73's measurement of the three-kit requirement
and PLAY-dOrderedCharter-72's ledger line for the adopter's reds.

Recall terms used: `python tools/memory-recall/query.py "an adopter's tags check reds on gov's namespace owners and a kit requires a sibling kit for the scratch install" --terms "chain registry owner unarmed namespaces purpose native family-id requires scratch install policy memory-tree default selection positional absent"`
