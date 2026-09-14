# TOOL-dDerivedDocket-10 — driver refuses shard-into-view

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

After the switch-over, `memory/backlog/<FAMILY>.md` is a generated view, yet a branch forked before it
still edits that path as an authored shard, and a merge, squash or rebase can line-merge those rows
into the view with nothing refusing. Teach the row-keyed merge driver — the one every node already
has configured under `merge.rows.driver` — to refuse, fail-closed and with the relocation recipe,
whenever one side is a view and the other an authored shard; keep the attribute that routes the views
to it; make it count per-build `BACKLOG.md` rows by record class, so honest concurrent edits merge;
and bind all of that on every bar through one repo-subject check (design layer L3, amendments A2 and
A3).

## 2. Scope (IN)

- **S1** The refusal. Before any key merge, `merge()` classifies `%A` and `%B` with the view unit's
  view predicate. When exactly one side is a view, the driver writes a conflict — ours, then theirs,
  between markers, the closing marker naming the refusal — prints the refusal and the recipe from
  the view unit's one constant on stderr, and exits 1. It never auto-resolves such a pair. Observed
  by AC1 and AC2.
- **S2** Where the refusal reaches. Whenever the post-switch tree's attributes govern — a straggler
  merged into the default branch, `git merge --squash`, `git rebase` and `git pull --rebase` — the
  refusal fires, measured in design §18r.1. Observed by AC2.
- **S3** Fail-closed on its own dependency. The view predicate is imported lazily, the way the anchor
  grammar is; if it cannot be imported, the driver's existing handler writes a conflict rather than
  taking ours. Observed by AC3.
- **S4** Class-keyed census for `BACKLOG.md`. When `%P` names a `builds/<slug>/BACKLOG.md`, the id half
  of `no_new_duplicates` keys each row by the parser unit's classifier — an ask by its id, a status
  row by its target, a SEV row by its target, a provenance row by its target and sha — instead of by
  the first id on the line. Two status rows for one target on two branches still fail closed; a SEV
  row on one branch and a status row on the other merge clean. Without `%P` the generic census runs
  and the audit line says so. Observed by AC4 and AC5.
- **S5** A repo-subject `--check` mode of `merge-rows.py`. It asserts through `git check-attr` that
  every tracked governed path resolves `merge=rows` — `DECISIONS.md` and every `backlog/*.md`
  always, every `builds/*/BACKLOG.md` under `BACKLOG_MODE=builds` — over a population derived from
  the conf and refused when empty. It then runs an in-memory three-way of a view rendered with this
  repo's own header against an authored shard and asserts the refusal fires. It prints one liveness
  line. Observed by AC6 and AC7.
- **S6** A new gate leg runs S5 on every bar: chunk `declarations`, subject `repo`, no guard, so the
  kept attribute and the refusal cannot rot quietly between kit edits (design A3). The leg is claimed
  by the merge-driver dossier, with the map regenerated in the same commit. Observed by AC8.
- **S7** The kept attribute (design A2). `memory/backlog/*.md merge=rows` stays; S5 is what reds its
  removal. The `memory/builds/*/BACKLOG.md` line is the switch-over's to add, and this unit proves the
  driver merges that file class correctly before any such file exists. Observed by AC4, AC6 and AC7.
- **S8** Replay arms in the driver's own suite for every behaviour above, each driven through a real
  `git merge` in a scratch repository with the driver wired, and each observed RED with its fix
  unstaged. Observed by AC9.
- **S9** The driver's docstring and the merge-driver dossier say which files it governs now, that a
  view is never merged with a shard, and what the refusal does not cover. Observed by AC8.

## 3. Non-goals (OUT)

- The view, its header banner and the recipe's text. The view unit's; this unit reads its predicate
  and constant.
- Adding the `memory/builds/*/BACKLOG.md merge=rows` line to `.gitattributes`. The switch-over's S5.
- The case where the PRE-switch tree's attributes govern — the default branch merged into a straggler
  — where the straggler's own old driver runs. The view header's banner (design layer L4) is what the
  operator reads there, and the data-loss guard catches a view carrying authored rows afterwards.
- A rebase, squash or cherry-pick whose conflict is resolved by discarding rows. Design §18r.6 hole 1:
  nothing mechanical stops a deliberate discard.
- A node's `merge.rows.driver` configuration. `tools/check-wiring.sh` owns wiring; S5 asserts the
  tracked attribute, which is the half a commit can break.
- Any change to rules 1 to 4, the skeleton, or the other postconditions.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the row classifier the class-keyed census counts by.
  Without it the driver would spell a second copy of the ask grammar.
- **consumes-from** `TOOL-dDerivedDocket-7` — the view predicate the refusal classifies each side with,
  the recipe constant it prints, and the renderer the `--check` probe builds its view from. Without
  them the driver cannot tell a view from a shard.
- **hands-off** `TOOL-dDerivedDocket-12` — the refusal banner, whose recipe block the relocation
  engine's parity arm compares with its `--recipe` output.
- **hands-off** `TOOL-dDerivedDocket-34` — a driver that refuses a shard merged into a view, which is
  what makes keeping the backlog attribute worth it at the switch-over and what the landing reconcile
  meets when the remote tip's shards moved.
- **hands-off** `DEPL-dDerivedDocket-1` — the refusal the adopter runbook tells an adopter to expect
  once it adds the per-build attribute and switches.

## 4. Design

### The refusal

```text
merge(o, a, b, path):
  view_a, view_b = is_family_view(a), is_family_view(b)      # the view unit's predicate, lazily imported
  if view_a != view_b:
      raise ViewShardRefused(recipe)                        # before skeleton, key merge or postcondition
  ... unchanged ...
main():
  on ViewShardRefused:  write <<<<<<< ours / ours / ======= / theirs / >>>>>>> theirs (refused: view vs shard)
                        print the refusal and the recipe to stderr; exit 1
```

The written body is the fail-closed body the driver already writes on any exception, with its
dominant-terminator rule, so a CRLF worktree gets CRLF markers. Only the closing label and the stderr
text differ. When `%O` is a view and both sides are shards, or both sides are views, nothing new
happens: the first is a re-authored view on both branches, which check 9's data-loss guard reds, and
the second is an ordinary view merge that `--write` repairs.

### Which driver runs, by merge shape (design §18r.1, git 2.54.0.windows.1)

| Operation | Attributes and driver that govern | This unit |
|---|---|---|
| a straggler merged INTO the default branch | the post-switch tree's | refuses |
| `git merge --squash` of a straggler onto the default branch | the post-switch tree's | refuses |
| `git rebase` or `git pull --rebase` of a straggler onto the default branch | the post-switch tree's, during the replay | refuses |
| the default branch merged INTO a straggler | the straggler's own old driver | not reached; the banner and the data-loss guard |

### The class-keyed census

The id half of `no_new_duplicates` exists for rows the anchor grammar does not key, and at BASE it
counts a row by the first id on it (`row_ids` at `tools/memory-tree/merge-rows.py:329`). In a
`BACKLOG.md` every row about one ask carries that ask's id first — the ask itself, its SEV row, a
status row naming it — so a SEV row added on one branch and a KEEP added on another count as one id
written three times against two, and the whole file conflicts on an honest pair. Keying by the
classifier's (class, target) removes that false conflict and keeps the real one: two status rows for
one target are one class twice, which V4 forbids anyway. Design §7 measured three keyed and three
hashed disposition rows merging clean before severity rows existed; the SEV-plus-status pair is new
with owner ruling D7 and was never replayed.

### The `--check` mode

```text
merge-rows: check · <n> governed path(s) resolve merge=rows · mode <shards|builds> · view refusal armed
```

The probe renders an empty-family view through the view unit's renderer, so it tests the header this
repo actually writes, with its own kit prefix, and not a fixture's copy. It calls `merge()` in memory,
with no git process and no temporary file, and asserts the refusal type.

**What it does not check**, stated in the mode's header: whether a node configured the driver, whether
an old branch's driver conflicts, or whether anyone later discards rows by hand.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `ViewShardRefused` | exception class | lexicon python class cell |
| the class-keyed census helper | python function | lexicon python function cell; names pass `lexicon.py --suggest` first |
| `--check` | CLI mode of the driver | a flag |
| `row-driver view refusal` | gate leg | a gate-legs key, claimed by the merge-driver dossier |

### Files touched (estimate)

`tools/memory-tree/merge-rows.py` · `tools/memory-tree/merge-rows.test.sh` · `tools/gate-legs.json` ·
`memory/map/features/memory-tree-merge-driver.md` · `memory/map/generated/`.

### Alternatives rejected

- **Retargeting `memory/backlog/*.md merge=rows` to the per-build files** (design §7 before A2).
  Without the attribute `-X ours` merged a straggler clean and dropped a flip (bypass lab e04g2).
- **Refusing in a hook instead of the driver.** Hooks run from the node's primary tree and can be
  skipped with `--no-verify`; the driver runs inside every merge whose tree carries the attribute,
  whichever node performs it (design §18r.2).
- **Leaving the census keyed on the first id.** It false-conflicts the SEV-plus-status pair above,
  which the filer and a triager produce on ordinary work.
- **Arming the refusal only in the held replay suite.** Held suites run on demand, so a regression
  arriving through a header change in another file would go unseen until someone ran them; the
  repo-subject leg is design A3's answer, and it costs one python start.

## 5. Production-readiness checklist

- security — the refusal can only add a conflict, never auto-resolve; the `--check` probe writes
  nothing and runs no git merge on the real tree.
- perf / scale — one predicate call per side per merge; `--check` is one `git ls-files`, one
  `git check-attr --stdin` and an in-memory merge, seconds.
- error / empty / loading states — an import failure writes a conflict; an empty governed population
  refuses; zero tracked `BACKLOG.md` under `builds` is announced, because a young builds tree is legal.
- observability — the refusal line and recipe on stderr during the merge, the closing-marker label in
  the file, and the `--check` liveness line.
- risks — a conflict the operator resolves by taking theirs puts shard rows into a view; the
  data-loss guard reds that at the next `--check`, and the recipe says to relocate instead.
- testing — `tools/memory-tree/merge-rows.test.sh` replay arms through real merges, and the new leg on
  every bar; one hand observation on this repo, staging the attribute's removal and seeing `--check`
  red, recorded in the unit's journal.
- migration — none; the attribute line is unchanged and the `BACKLOG.md` line waits for the switch.
- user docs — the driver's docstring and the dossier's constraints section.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/merge-rows.test.sh` drives a three-way whose ours is a
  rendered view and whose theirs is an authored shard, the driver exits 1, the written file carries
  both sides between markers with the refusal on the closing marker, and stderr carries every recipe
  line.
  Red when: the pair is key-merged, which appends the shard's rows under the view's table at rc 0.
- **AC2** — When the suite merges a straggler branch into a fixture default branch holding a view, and
  separately squashes it and rebases it onto that branch, each operation stops conflicted on the view
  with the refusal on stderr.
  Red when: any of the three completes clean, which is the silent row loss or row injection the
  refusal exists to stop.
  fixture: built by the suite with the driver wired through `git config merge.rows.driver`.
- **AC3** — When the suite runs the driver with the view predicate's module made unimportable, the
  merge writes a conflict and exits 1, and ours-only content is never written.
  Red when: an import failure at module scope kills the driver before `%A` is written, which git
  reports as a conflict over ours-only content with no markers.
- **AC4** — When two fixture branches each append a row to one `BACKLOG.md` — a SEV row for an ask on
  one, a KEEP for the same ask on the other — `git merge` completes clean with both rows present once.
  Red when: the census counts both rows under the ask's id and the whole file conflicts.
- **AC5** — When the two branches instead each append a different status row for one ask, the merge
  fails closed; and with `%P` omitted from the driver's arguments the audit line names the generic
  census.
  Red when: the class keying lets two status rows for one target merge clean, trading a loud contest
  for a V4 verdict discovered later.
- **AC6** — When `python3 tools/memory-tree/merge-rows.py --check` runs on this repo, it exits 0 and
  its liveness line reports a governed-path count above zero and the refusal armed.
  Red when: the population is empty because the selector is mis-rooted and the check passes by finding
  nothing.
  figure: the governed-path count is DERIVED at run time.
- **AC7** — When the attribute line for `memory/backlog/*.md` is removed from a scratch copy of
  `.gitattributes` and `--check` runs there, it exits 1 naming `memory/backlog/TOOL.md`; with a
  driver copy whose refusal is disabled, it exits 1 naming the probe.
  Red when: `--check` greps `.gitattributes` instead of asking `git check-attr`, so an attribute
  overridden elsewhere passes.
- **AC8** — When `tools/gate-legs.json` is read it carries the new leg with subject `repo`, chunk
  `declarations` and no guard, and the codebase-map coverage leg is green with the leg claimed by the
  merge-driver dossier.
  Red when: the leg ships guarded on the kit directory, so an edit elsewhere that breaks the view
  header never re-runs it.
- **AC9** — When each of AC1 to AC7's fixes is unstaged in turn, its arm in
  `tools/memory-tree/merge-rows.test.sh` or its `--check` observation turns red, and restoring the fix
  turns it green.
  Red when: an arm passes with its fix removed, which is an arm grading nothing.

## 7. Gates

`row-keyed merge driver replay` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/merge-rows.test.sh` · a view-against-shard three-way, the three §18r.1 shapes the driver governs, an unimportable predicate, and the two `BACKLOG.md` concurrency pairs · none; the suite is on the testsuite-count waiver
New arm: `python3 tools/memory-tree/merge-rows.py --check` on the new `row-driver view refusal` leg · the attribute removed from a scratch `.gitattributes`, and a driver copy with the refusal disabled · none

## 8. Open questions

- **F1** — Where does design A3's repo-subject arm for L3 live? (a) Only in the held replay suite. (b)
  A new repo-subject `--check` mode on its own leg. (c) Inside the transition-audit suite. (c) needs an
  edge the transition-audit spec does not declare, and (a) leaves the refusal unbound between kit
  edits. RESOLVED (agent, 2026-09-14, delegated): (b), plus the replay arms in (a).
- **F2** — Does the census need class keys? FACT-QUESTION · Probe: `row_ids` at
  `tools/memory-tree/merge-rows.py:329` read against the grammar's row shapes. The probe would have
  come out the other way had `row_ids` keyed on the whole line or the verb. RESOLVED (agent,
  2026-09-14, delegated): yes; it keys on the first id, so every row about one ask shares a key.
- **F3** — Who adds the `BACKLOG.md` attribute line? The brief's note for this unit says ADDED; the
  switch-over spec already carries it as its S5. RESOLVED (agent, 2026-09-14, delegated): the
  switch-over, so one commit owns the attribute change and this unit proves the driver first.
- The rulings this unit executes: D11 made the straggler guard fleet-wide and permanent, and
  amendment A2 keeps the backlog attribute — RESOLVED (owner, 2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds three edges the brief's table does not list:
  consumes-from unit 6, for the row classifier, and hands-off to unit 12 and to the adopter runbook,
  reciprocating the consumes-from lines those specs declare.

## 10. Reuse audit

The seam is the driver itself, `tools/memory-tree/merge-rows.py`: its lazy `anchors()` import is the
pattern the view predicate's import copies, its fail-closed body in `main()` is the conflict the
refusal writes, and `no_new_duplicates` is the postcondition S4 re-keys. `python
tools/codebase-map/reuse_lookup.py "refuse a three-way merge when one side is a generated file and the
other authored"` returned that `merge` function and govkit's `three_way`, which merges a settings
file and refuses nothing of this shape, and it reports the shell layer unscanned. Recall returned
`TOOL-aMendedLedger-5`, which chose a row-keyed driver over `merge=union` on measurement, and
`TOOL-aCollapsedScan-7`, the inherited `GIT_DIR` that made the driver inert until its repo root was
derived — the reason S5 derives its root the same way.

Where the design and BASE disagree: design §7 says views carry no merge attribute; amendment A2 keeps
it and this spec follows A2. Design §7's clean-merge measurement of disposition rows predates severity
rows, and F2 finds the census would conflict on the new pair. `tools/check-wiring.test.sh` already
asserts the backlog attribute, but inside a held kit suite; S5 is the unheld reader of the same fact,
and the two are left to agree rather than one deleted, because the held one also covers the driver's
wiring.

Recall terms used: `merge-rows driver fail-closed conflict duplicate postcondition union skeleton row-keyed gitattributes merge=rows take-ours`
