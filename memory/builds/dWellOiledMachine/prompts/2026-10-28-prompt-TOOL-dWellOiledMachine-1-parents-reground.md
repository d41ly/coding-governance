**Serves:** research TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-90

# Brief: dWellOiledMachine's specs re-grounded against dBoundRoles' and dTotalRecall's landed specs

## The prompt

> `gov-spec-writer` agents revise only the mismatched specs, never the main loop, at effort medium or
> higher. Each revision adds one `spec-revised` deviation record.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on dMindYourWords', dShippedRelease's, dScopedBuild's and dTendedCadence's spec runs until this pass
lands.

## The brief

### Goal

Revise the 46 dWellOiledMachine specs that the cross-check record names under "For the re-ground".
Each one should state its parents' surfaces the way their specs now spell them on origin/main at
`d1721ef20`: dBoundRoles as its re-ground `ac8ab8d5f` left it, dTotalRecall as `794a0f5fb` left it,
and the rules dOrderedCharter, dDeclaredLoop, dWitnessedBar, dPlacedRequest and dKeptSession apply to
every spec. Each spec keeps its own design, and only its assumptions about the parents change.

### Items

Read the cross-check record first,
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 167), and its "For the re-ground" section names
the rows each spec answers. Section 2 of each group's return in
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-crosscheck-returns.md`
quotes both sides of each MISMATCH and states its `Change:`; that is the starting point for each row.
Read each parent spec the record cites, at the lines it cites. This brief summarises them, and where
the two differ, the specs win. Before you edit for a row, re-read both sides. A row the parent's text
does not bear out is not edited: return it as refused, with the line that refutes it.

Facts every revision uses:

- **A policy read (the I31 class, rows in 23 specs).** The build's spec brief row I31 named the policy
  kit's in-process `resolve(key)` and `readPolicy` as the readers; the parents do not admit them. Python
  outside the roles kit runs `<sys.executable> <policy kit>/policy.py get <key>` as a bounded
  subprocess, the policy kit found through the inline `resolve_kit_dir` block, with `--rev <sha>` for a
  read at a revision and `--explain` where the spec needs the catalogue row (oc7:202-205, :379-380;
  `policy.py get --help` lists `--rev`, `--explain` and `--json`). Exit 2 is a refusal the spec states
  what it does with. A JavaScript hook spawns `node <policy kit>/policy-mirror.js get <key> --repo
  <repo>` under a bounded timeout and never `require`s the module (ks8:62-66). `policy-shim.sh get` is
  already a subprocess and stays. Inside the roles kit, `read_policy_setting(key, root,
  with_default=True)` (br21:41-50, br43:105-110). Name no new shared helper: state the subprocess
  where the spec reads. wm33, wm40, wm41 and wm49 already read so; follow them.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205). A by-file load
  (`importlib`, `spec_from_file_location`, `load_kit_module`), a `sys.path` insert of another kit's
  directory, or a call of another kit's function by name is an in-process import. Code reaches another
  kit's verb by subprocess, found through the inline `resolve_kit_dir`. Where the verb exists, name it
  (for example `position.py <slug> --json`, `loop_transition.py record`, `endings.py derive`,
  `request.py key`, `budget.py draw`, `render_playbook.py --answers`, `ratify.py check`). Where it does
  not, write a §8 fork open for the owner: an ask to the owning build for the verb, or a declared
  `requires_if` row on `tools/runtime/kit.toml`, with the reason the rule admits it. Recommend one. A
  small pure helper, such as rendering a wall time, may instead be carried in the runtime kit.
- **A leg.** oc7 S3 reds a leg with no `enforces` (oc7:58-63). wb11 declares each leg once, in its kit's
  `[[gate_leg]]` row holding every manifest key, `enforces` among them, or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row; `leg_factory.py --write` renders
  `tools/gate-legs.json`, and `--check` reds a manifest that differs (wb11:36-49, :154). A runtime leg
  is a `[[gate_leg]]` row of `tools/runtime/kit.toml`, made with `leg_factory.py new`; a re-guard or
  re-shape of an existing leg edits its declaration and renders. Name `enforces` from the principle or
  practice the leg's spec carries; where the spec gives no ground for a tag, write a §8 fork open for
  the owner, as dDeclaredLoop unit 3's F7 does. `tools/gate-legs.json` leaves Files touched as an
  edit; an AC reads the declaration or `leg_factory.py --check`. `tools/run-gates/leg_factory.py` is
  not in the tree today: the pass records that a hand edit stands in for it until wb11 lands.
- **A lease read.** `unattended.sh --claims` prints fields 1 to 5 only: name, fleet tag, status,
  beat-age and verdict (pr1:206-208; `unattended.sh:2204`). Session, epoch, offer and node beats are not
  among them. The `--lease` verbs print `epoch <n>` (pr1:86). The lease holder's session is tr2 F6's open
  ask to dPlacedRequest (tr2:335-345): a spec that needs it names F6 and waits on its pick, and files
  no second ask. Any other field is a §8 fork for an ask to dPlacedRequest. A new `CLAIM_ROWS` column
  goes after field 18, `last-fetch` (pr1:203-207).
- **`record find`.** At most 40 rows, `key · kind · build · bytes · path:line`, no content, filtered
  only by `--kind`, `--tag`, `--build` and `--paths`; past 40 the last line is the total (tr9:89-96,
  :207-209). Fields are read per key through `record show`. A read that can exceed 40 rows narrows its
  filters until the total line is gone, or writes a §8 fork for an ask to dTotalRecall for an uncapped
  mode. Recommend one.
- **A record kind.** A build-folder record named `-<kind>-<n>.md` is typed: it joins
  `TYPED_RECORD_KINDS`, the factory's per-kind table and HYGIENE's closed list in one pass (oc42 S1 to
  S5; tr11 S3 and tr25 S6 are the pattern). A registry row in `tools/memory-tree/record-kinds.toml`
  carries tr1 and tr18's cells: `tag = "record.<name>"`, `layer` a layer tag, `lifecycle` from tr18's
  closed set, `readers` as read keys or `[]` with `readers-none`, `home`, and `fields` equal to any
  `schema.source` literal (tr1:62-81, :173-182; tr18:45-49, :130-133). The door mints only `<n>`,
  `<seq>`, `<slug>`, `<date>` and `<unit id>` (tr2:174-187), and refuses a non-root kind with no
  `--caused-by` (tr19:58-67).
- **dBoundRoles' surfaces.** br3's work order renders five blocks, `item`, `inputs`, `allowance`,
  `return` and `witness`; it carries no `allow` list, `script` or `fan` (br3:48-61). br22's stage rows
  hold `fan`, the most agents a stage spawns in one call, and `cap`, the most in flight at once
  (br22:108-109); a count of agents in flight reserves `cap`. The stage rows are read only through
  `load_workflows` in the roles kit (br22:38-44), and no roles verb prints them today: that is a §8
  fork (an ask to dBoundRoles for the verb, or a `requires_if` row). br11 rev-3's `owner-question` can
  refuse (br11:63-65). br1 F6's `check_layer_roles` reads `.claude/roles.json` by value.
- **An ask.** No dWellOiledMachine spec files a row in another build's `BACKLOG.md`. Where a fix needs
  a parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file. Before minting a fork, grep this build's other specs for one
  already open on the same verb, and cite it rather than open a second.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, for the rows the record names, and no other:

- **Group A, led by spec 1:** specs 1, 2, 3, 4, 5, 6, 7, 8 and 9.
- **Group B, led by spec 10:** specs 10, 11, 12, 15, 16, 17, 19, 20, 23 and 24.
- **Group C, led by spec 25:** specs 25, 26, 30, 32, 33, 34, 36, 37 and 39.
- **Group D, led by spec 41:** specs 41, 42, 43, 44, 45, 46, 47 and 48.
- **Group E, led by spec 50:** specs 50, 51, 52, 53, 54, 56, 58, 59, 79 and 90.

Where two specs of different groups share a fix (wm43 and wm45 share D's `fan`/`cap` read; wm34, wm44,
wm51 and wm53 share the `record find` cap; wm32's act record is read by wm19 and wm30), the brief's
facts above are the one answer, so each writer reaches the same form.

The spec files are `memory/builds/dWellOiledMachine/spec/2026-10-2?-spec-TOOL-dWellOiledMachine-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/wm-w<group letter>/`,
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
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `wmN:L`
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
- No file of dBoundRoles, dTotalRecall, dKeptSession, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dPlacedRequest, dSafePassage or dGroundRules, and no edit of the build's spec brief. A parent spec
  that looks wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dFurnishedOrders'
re-ground brief,
`memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md`,
and its revised specs, as the precedent for how a revised spec reads against the same two parents.
