# TOOL-dDerivedDocket-12 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-12

The relocation engine inside `tools/memory-tree/migrate_backlog.py`: one planner, three writing
verbs (`--relocate`, `--repair`, `--ingest`), the two print modes `--stragglers` and `--recipe`, the
`--dry-run` rehearsal with its three exit codes, the classification table of section 4, the two
policy sets and their four policies, the all-or-nothing plan, the per-id confirmation gate, the
view-and-archive restore, and the post-write re-read through unit 9's accounting predicate.

NO MERGE BAR, NO GATE LEG AND NO `*.test.sh` SUITE RAN IN THIS PASS. The module's own `--selftest`
is the flag-form direct check the pass makes, held at the direct-check bound by unit 11 section 8
F9. Every observation below was made against a scratch fixture repository with real git history and
dated commits, or in process against such a repository's explicit root.

EVERY ARM'S RED WAS OBSERVED, and not by assertion. Twenty-three breaks were staged one at a time
into a COPY of the whole kit under the run's scratch root — never this tree — and the copy's own
`--selftest` was run against each: the provenance row's leaked loop variable, a `RELOCATED` row
citing the merge instead of the change commit, the two relocate sides resolved swapped, `filed`
mined from the newest lineage commit instead of the oldest, a write before the refusal, the
confirmation gate removed everywhere and again on the `--from` form alone, the idempotence filter
removed, the inventory narrowed to `refs/heads`, candidates taken one ref-label per commit, the
restore performed under `--dry-run`, the empty plan given exit 1, the recipe re-spelled, the mode
guard removed from `--relocate` and from `--repair`, the archive left tracked, the names-an-id test
reading only the target tree, an unnamed hold written verbatim, the migration set's disposition home
forced to the `--as` folder, the signed triage verdict moved to the owner's folder, the cutoff
always taken as the day after the newest `filed`, the concluded merge keeping `theirs=HEAD`, any
existing row replaced, a terminal removal made NEEDS-HUMAN, a live removal dropped silently, and the
assertion floor raised above the executed count. All twenty-three went RED.

ONE LIVE DEFECT the arms found rather than a break staged into them: `build_records` named the inner
record loop's variable in the provenance row instead of its verdict's id, so an entry that writes no
record — a dropped row, a live flip — produced a second `RELOCATED` row for the PREVIOUS id and none
for its own. Unit 9's accounting re-read named it as a duplicate beside an unaccounted entry, which
is the whole reason S3 re-reads after writing.

**Evidences:** TOOL-dDerivedDocket-12
- AC1 — `migrate_backlog.py --relocate --as <slug>` — over a fixture straggler that closed one row,
  repointed one path and filed one new ask, the MERGE_HEAD run exits 0; the new ask lands in its own
  id's folder, the CLOSED disposition cites the change commit and not the merge, the ask text
  carries the new path and no longer the old, each of the three entries gets exactly one `RELOCATED`
  row and all three sit in the `--as` folder, and `transition_audit.py --staged` accepts the pending
  merge against the index. The concluded-merge form and `--from <ref>` with `--confirm <flip id>`
  write records byte-identical to it. The new ask's `filed` is the day of the straggler commit that
  first added its row — neither the merge's day nor the day of the LATER lineage commit that also
  held the row, which the fixture carries for exactly that reason.
- AC2 — `--drop <id>=<why>` — a fixture whose straggler also rewrote one row's prose exits 1, names
  that id under NEEDS-HUMAN, prints the exact `--drop` re-run, leaves every record file as it was
  and leaves `git status --porcelain` exactly as the merge left it; re-run with the drop it exits 0
  and writes one `dropped:` provenance row for that id and no other record naming it.
- AC3 — `migrate_backlog.py --repair <merge-sha> --as <slug>` — over a fixture whose default side
  carries a REOPEN for the id the straggler closed, the repair exits 1 naming the id, its status
  before and after, and `--confirm`; the uncontested new ask is not held for confirmation; with
  `--confirm <id>` it writes, that new ask included. The straggler form of
  `migrate_backlog.py --ingest <the contested ref> --as <slug>` refuses the same id the same way.
- AC4 — amended rev-6 — the criterion named `bash tools/memory-tree/check-memory-hygiene.sh`; the
  arm now runs `transition_audit.py`, the module that check delegates to, in process against an
  explicit root, because that module's CLI resolves its repository from its own file location and a
  subprocess launched inside a fixture audits THIS tree instead. Observed there: an unaccounted
  transition reds, the same transition accepts after `--repair` and its commit, and a second
  `--repair` plans zero records.
- AC5 — `--stragglers` — a fixture ref is listed while it is unmerged; after
  `migrate_backlog.py --ingest <ref> --as <slug>` and the commit of its records the same ref stops
  being listed while it is still not an ancestor of HEAD, which is a judgement about content; the
  later merge of that ref then passes the transition audit with no further record.
- AC6 — `migrate_backlog.py --stragglers` — over a fixture holding a local straggler, a
  remote-tracking straggler and the clean default branch it prints `examined 3` and lists two,
  including the `refs/remotes` one; `--local` lists one; `--tsv` prints the row and its own
  `examined` count. Over a second fixture holding a straggler, a twin branch at the same tip and a
  fork above it with no backlog commit of its own, it lists all three. A repository with no ref, and
  a `git clone --depth 1`, each exit 1 as a DEAD PROBE.
- AC7 — `--dry-run` — a dry run over a writable plan exits 0, prints the plan and the conservation
  table, leaves `git status --porcelain` unchanged and creates not even the file it would write
  into; a dry run over a plan holding a NEEDS-HUMAN entry exits 1; a dry run whose plan is empty —
  the second `--repair` of AC4 — exits 2 naming the empty plan.
- AC8 — `migrate_backlog.py --recipe` — the block the fixture's `gen_build_index.py --write` render
  quotes in the family view, each line prefixed `> `, is those bytes; so is the block `merge-rows.py`
  prints when a rendered view meets an authored shard.
- AC9 — `--relocate` — with no `MERGE_HEAD`, no merge HEAD and no `--from` it exits 2 naming the
  missing condition and reprinting the recipe; against a shards-mode other side it exits 2 naming
  that side's mode; `migrate_backlog.py --repair <merge-sha> --as <slug>` from a shards-mode
  checkout exits 2 naming HEAD's mode and so does the straggler form of `--ingest` from it; an
  `--as` value outside the slug shape exits 2 naming the shape.
- AC10 — `migrate_backlog.py --selftest` — prints `PASS (205 assertions)` at the floor moved from 71
  to 205 in this commit, in 48 s on node `d`, with the leg's `ceiling` in `tools/gate-legs.json`
  unchanged at 300. `bash tools/check-testsuite-counts.sh` and `bash tools/check-install-prefix.sh`
  are gate-leg commands no pass runs and bind at the one post-build bar, as this criterion's
  permission line states.
- AC11 — `--relocate` — a fixture straggler that rotated its flipped row into
  `memory/archive/EXMP.2026-04-02.md` relocates that flip accounted exactly once, and the archive
  the default side does not carry leaves both the worktree and the index.
- AC12 — `--triage-ask EXMP-aFoo-9` — over the four hold rows shared with unit 11's own corpus, the
  straggler set plans NEEDS-HUMAN for the hold naming nothing and for the hold naming a decision id,
  plans `- BLOCKED · EXMP-aFoo-3 · on EXMP-aFoo-2` for the hold on an ask the same delta files, never
  marks that id NEEDS-HUMAN, and writes nothing because the plan holds a NEEDS-HUMAN entry; the
  migration set over the same rows writes `- DEFERRED · <id> · until EXMP-aFoo-9`,
  `- BLOCKED · <id> · on EXMP-aFoo-9` and the verbatim hold, all three in the ask owners' folders,
  over a shards-mode HEAD no mode guard refuses, and with no provenance row at all.
- AC13 — `--write` — the migration set over a fixture whose HEAD `.memory-tree.conf` reads shards
  puts the transferred legacy CLOSED in the ask owner's folder and the signed triage verdict in the
  `--as` folder, and plans nothing at all for the id the target tree already disposes.
- AC14 — `ASK_CUTOFF=` — the landing form's dry run lists both new asks, holds the flip under
  CONFIRM, puts the amendment under NEEDS-HUMAN, prints the cutoff line, exits 1 and leaves every
  record file as it was. With the amendment gone and `--confirm <flip id>` it writes each new ask in
  its own slug folder, the hold on the ask the same delta files verbatim, the flip in the owner's
  folder, the signed triage verdict and one `RELOCATED` row per entry in the `--as` folder, and
  prints the day after the newer ask's `filed`; with HEAD's `.memory-tree.conf` carrying a later
  cutoff it prints that value unchanged. `--signed` on the straggler form exits 2 naming the form.
- AC15 — `migrate_backlog.py --relocate --from <ref> --as <slug>` — over the same REOPEN fixture it
  exits 1 naming the id, its status before and after, and `--confirm`, and writes with
  `--confirm <id>`.
- AC16 — `git merge --no-ff --no-commit <tip>` — run inside that merge, and again on the merge once
  `git commit` concluded it, the landing form writes bytes identical to the run made before any
  merge. One commit further on it exits 2 naming `--repair`; so does a HEAD whose FIRST parent is
  the tip, and so does the straggler form over a HEAD that already contains its ref.
- AC17 — `gen_build_index.py --check` — the landing form replaces the hold the migration itself
  wrote with `- CLOSED · EXMP-aFoo-4 · by <change sha>` in the same file, leaving one status row for
  the id, and the generator names no V4 over the result; with that hold's wording edited by the
  receiving branch the same command exits 1, lists the id under NEEDS-HUMAN and writes nothing.

## What is NOT covered

The `--write` verb itself is unit 34's thin driver and is not a mode of this module; what this unit
ships is the migration policy set it will drive, exercised here through the planner's own entry
point. `--plan --signed`, unit 11's read-only prediction, is untouched by the `--signed` form rule
and is covered by that unit's arms, which still pass. The assertion floor catches a block of arms
that ran short of the count; it does NOT catch an early `return` from inside the suite body, which
skips the floor check entirely — that placement is unit 11's and this unit did not move it.
