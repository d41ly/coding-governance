# TOOL-aRoutedQuill-3 — every pushed commit that touches a product path names a unit specced before it

**Status:** CLOSED · rev-5 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 4 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-3-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aRoutedQuill-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-3-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-3-build-brief.md) | journal | — |
| [2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md](../reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md) | diff-review | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-7 |
| [2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md](../reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The write gate sees only Edit and Write calls, so a product file changed through a shell, a hook-less
run or an unwired install reaches a commit with no unit behind it. This unit adds a merge-bar leg to
the memory-tree kit that grades the commits themselves: every non-merge commit touching a path under
`ROUTED_PATHS` must name a unit id whose spec existed at that commit's first parent. It runs at the
push boundary on the pushed range, and everywhere else over the history since a declared cutoff.

## 2. Scope (IN)

- **S1** — `routed_commits.py` in `tools/memory-tree/` grades every non-merge commit in its range
  that touches a product path. The commit passes when at least one id its attribution names has a
  spec at the commit's first parent; otherwise it is a violation naming the commit, its subject, the
  ids it named and the reason. Observed by AC1 and AC2.
- **S2** — Attribution is the union F2 resolved: the ids among the subject's whole tokens together
  with the ids a `Pass:` trailer names. `Pass: none` adds no id and keeps the subject's, so a commit whose
  subject names a unit and whose trailer reads `Pass: none` is attributed to that unit. This
  deliberately differs from `read_attribution_tokens` in `tools/unattended/lib-unattended.sh`,
  where a trailer replaces the subject: that reader decides which commit is a unit's PASS, and this
  leg asks only whether a commit is attributed to any unit. An id is `<FAMILY>-<slug>-<seq>` over
  the families `.memory-tree.conf` declares in `FAMILIES`. Observed by AC2 and AC11.
- **S3** — Which spec defines an id is answered by `parse_spec_h1` in `tools/memory-tree/tree_lib.py`
  over every spec blob at HEAD. Existence at a commit's first parent is asked for every pair in one
  `git cat-file --batch-check` read. Observed by AC1.
- **S4** — The range is RANGE, `$GATE_PUSH_BASE..HEAD`, when that variable is set, not all zeros and
  resolves to a commit; otherwise it is WHOLE, all of HEAD's history, and the summary names which
  mode ran and why. Observed by AC3.
- **S5** — Three populations are not graded, and each is counted: merge commits, commits whose
  committer date precedes `ROUTED_COMMIT_CUTOFF`, and commits touching no product path. Renames are
  read as a deletion plus an addition, so a file moved out of `ROUTED_PATHS` is graded. Observed by
  AC7.
- **S6** — Cost is a constant number of git spawns whatever the range holds: one
  `git log -z --no-renames --name-only` pass carrying every commit's sha, parents, committer date,
  subject and `Pass:` trailer, plus a fixed handful of reads. No process runs per commit. Observed
  by AC6.
- **S7** — The leg refuses at exit 2 when it cannot give an answer worth reading: `ROUTED_PATHS` or
  `ROUTED_COMMIT_CUTOFF` blank or absent, an entry that is absolute, climbs through `..`, names
  nothing tracked at HEAD or covers `MEMORY_ROOT` (a spec commit would then need a spec before
  itself), a cutoff that is not an ISO date, a shallow clone, a parsed commit count
  that differs from `git rev-list --count` over the same range, and an empty id map while the tree
  tracks spec files. Observed by AC4 and AC9.
- **S8** — A summary line prints on every run, and a range holding no graded commit prints `graded
  0` with the range's commit count and the `ROUTED_PATHS` value. Observed by AC5.
- **S9** — `ROUTED_COMMIT_WAIVED` names landed commit shas the leg excuses, read in WHOLE mode only.
  A listed sha that is not a violation in the graded population reds as stale. Observed by AC8.
- **S10** — The kit declares the leg and its self-test in `kit.toml`, the two keys in
  `optional_keys` and as documented lines in `.memory-tree.conf.example`, and a README row. Gov's
  manifest, budget file, codebase-map dossier and `.memory-tree.conf` gain the matching rows, and
  `build_git_env` moves to `tree_lib.py` so the kit keeps one git pin policy. Observed by AC10.
- **S11** — The attended lander's own mint commit names a unit. `tools/push-main.sh` writes
  `mint: kit versions onto <remote>/<branch> at <sha8>` with `--no-verify`, touching version
  carriers under `tools/`, inside gov's `ROUTED_PATHS`, and RANGE mode reads no waiver, so without
  this every attended landing that owes a kit version would red its own pre-push leg. The mint's
  SUBJECT names the newest unit id the pushed range's own commits attribute, read by S2 over
  `<remote>/<branch>..HEAD`, and the commit carries a `Pass: none` trailer so the pass-order history
  leg's `read_attribution_tokens` does not take it for that unit's pass. A range attributing no id
  leaves the mint subject with none, and the leg reds it as it reds the range. The lander reads
  that id from `routed_commits.py --newest-unit <range>`, found through its sibling-kit resolver the
  way it finds the lexicon and govkit kits, and spells it `mint: kit versions onto <remote>/<branch>
  at <sha8> for <id>`; no python or no memory-tree kit beside it leaves the subject as it was.
  Observed by AC11.

## 3. Non-goals (OUT)

- Grading a spec's quality, tier or status. `pass-order history` grades MISSING and THIN for CLOSED
  units, and the write gate reads BUILDABLE; this leg grades ORDER and attribution only.
- Whether the named unit's scope covers the change. Any named id with a spec at the parent passes.
- A merge commit's own content. A conflict resolution that adds product code is not graded; its
  non-merge parents are.
- A commit-time or pre-commit form. Gov ships no `commit-msg` hook to adopters, and the write gate is
  the early layer.
- Sharing code with `check-pass-order.sh`. §4 "Alternatives rejected" says why.
- Scaffolding `ROUTED_PATHS` and the cutoff in an adopter, and the session-start red for an unarmed
  tree. That is `TOOL-aRoutedQuill-5`.
- The kit version bump. It happens once, after the build's last unit touching the memory-tree kit.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-2` — the `ROUTED_PATHS` key and its grammar, which this leg
  reads and does not define. Without it the leg has no product set and refuses as unarmed.
- **hands-off** `TOOL-aRoutedQuill-5` — writing `ROUTED_COMMIT_CUTOFF` beside `ROUTED_PATHS` when an
  adopter installs or updates the kit, so the adopter's first bar after the pull is armed rather
  than refused.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `check-pass-order.sh` grades only units a README marks CLOSED (`:9-10`, `:370-373`) and turns its
  term off on a blank `PASS_ORDER_CUTOFF` (`:177-180`). Its subject cache replaced two spawns per
  commit, measured at 751 ms each on node a, after the leg cost 10184 s (`:251-284`). It decides
  "spec at the first parent" with one `git grep` per unit over a five-line header window
  (`:436-476`, the window at `:458-468`).
- `read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1030-1036`) yields a `Pass:`
  trailer's ids in place of the subject and treats `Pass: none` as no unit. `build_commit`
  (`:1067-1145`) selects one build commit per unit. `read_history_range` (`:1292-1307`) learns the
  tip from `ls-remote`, and `GATE_PUSH_BASE` may only refuse that tip (`:1276-1278`).
- `tools/unattended/kit.toml:10` makes the unattended kit require memory-tree. The reverse edge
  does not exist, and memory-tree is a default kit while unattended is opt-in.
- `.githooks/pre-push` reads git's ref lines (`:444-447`), refuses a push whose default-branch sha
  is not HEAD (`:1028-1029`), and exports `GATE_PUSH_BASE` from git's own line, overwriting an
  inherited value (`:1557-1561`). A declared branch bar runs with the variable unset (`:949`).
- `run-gates.sh` runs a leg with no guard on every bar (`:2102-2104`). A leg that declares
  `doc_reads` skips on a doc-only push (`:2095-2100`), and gov's doc class holds
  `WIRE-INTO-PROJECT.md` and the charter template (`.githooks/gate-env.sh:104`), both product paths.
- `parse_conf` (`tools/memory-tree/tree_lib.py:131-142`) reads the conf without executing it.
  `parse_spec_h1` (`:202-225`) is the kit's declared single predicate for which id a spec defines.
- `build_git_env` and `run_git` (`tools/memory-tree/transition_audit.py:77-97`) are the kit's git
  pins: `--no-replace-objects` and `GIT_GRAFT_FILE=/dev/null`.
- The memory-tree hygiene leg carries `history_depth = "full"` (`tools/memory-tree/kit.toml:170-175`).
  Gov's remote CI checks out full history and pins `main` at the pushed sha, so HEAD is the tip
  there (`.github/workflows/remote-ci.yml`, steps `checkout, full history` and `pin the pushed sha`).
- `TOOL-aMendedFleet-65` §8 resolved that a leg knows it is at the push boundary by
  `GATE_PUSH_BASE`, which only a default-branch push sets.
- Measured on node a, Git-Bash, 2026-10-09, PINNED: one `git log --name-only` over all 4932 commits
  took 1.0 s, and streaming all 1083 spec blobs (23.7 MB) through one `git cat-file --batch` took
  3.0 s. Both grow linearly with the corpus.
- The candidate predicate, run over the 493 commits since 2026-09-25 that touch gov's
  `ROUTED_PATHS`, PINNED: 412 name an id in the subject, 6 only in a `Pass:` trailer, and 75 name
  none. The 75 are mostly a close's `fix(<slug>):` repairs and reconcile `mint:` version bumps; 23
  of them carry `Pass: none`. One commit names an id in its subject and carries `Pass: none`.

### The predicate

For each commit the log pass yields, in order:

1. Two or more parents: count as a merge, grade nothing.
2. Committer date, its first ten characters, earlier than `ROUTED_COMMIT_CUTOFF`: count as exempt.
3. No listed path equal to a file entry, or under a directory entry at a segment boundary: count as
   not routed.
4. Read the attribution by S2, the subject's ids together with the `Pass:` trailer's. No id:
   violation, `names no unit`.
5. For each id, every spec path whose H1 defines it at HEAD. An id with none: `no spec defines it at
   HEAD`. A root commit has no parent: `no first parent`.
6. Query `<first parent>:<path>` for every remaining pair, in one batch after the walk. Any pair
   present passes the commit; otherwise the violation names the spec path and the parent's short
   sha.
7. In WHOLE mode, a violation whose sha `ROUTED_COMMIT_WAIVED` lists counts as waived.

### The range

| Context | `GATE_PUSH_BASE` | Mode | Graded |
|---|---|---|---|
| `.githooks/pre-push`, default-branch push | the remote's sha before the push | RANGE | the pushed commits |
| the same, a push creating the branch | all zeros | WHOLE | history since the cutoff |
| a worktree or branch bar, a declared branch bar, CI, an adopter's bar | unset | WHOLE | history since the cutoff |
| any, the variable naming no commit in this clone | set | WHOLE, the reason printed | history since the cutoff |

RANGE reads no waiver, so at the push boundary every pushed commit is graded and nothing excuses one.
A hand-run bar given a forged `GATE_PUSH_BASE` fools only itself: the leg carries no guard, so the
push bar runs it again with the hook's own value. An unresolvable value widens and never narrows.

### Output and exit codes

```text
routed-commits: <RANGE <base8>..<head8>|WHOLE (<why>)> · graded <n> · <x> exempt by the <cutoff> cutoff · <m> merge(s) · <r> not routed · <w> waived · <k> spec id(s) at HEAD · ROUTED_PATHS <value>
routed-commits: graded 0 — the range holds <t> commit(s) and none of its non-merge commits on or after the <cutoff> cutoff touches ROUTED_PATHS <value>
routed-commits FAILED — a commit touching ROUTED_PATHS names no unit specced before it:
  <sha8> <subject> — <ids or "no unit id"> — <reason>
```

Exit 0 clean, 1 on a violation or a stale waiver, 2 on any S7 refusal. The runner reds on both.

### Data model

```sh
# .memory-tree.conf
ROUTED_COMMIT_CUTOFF="<ISO date>"     # commits committed before it are not graded; blank refuses
ROUTED_COMMIT_WAIVED=""               # landed shas the leg excuses in WHOLE mode; a stale one reds
```

The example ships both keys as commented lines, since `TOOL-aRoutedQuill-5`'s scaffold writes the
cutoff. Gov declares the cutoff as the date this unit lands, in the commit that adds the leg.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_routed_commits` | function, the one log pass | `py.function`; `lexicon.py --suggest` answered OK |
| `load_spec_paths` | function, id to spec paths at HEAD | `py.function`; answered OK |
| `derive_commit_range` | function, RANGE or WHOLE | `py.function`; answered OK |
| `test_routed_path` | function, the entry match | `py.function`; answered OK |
| `check_routed_commits` | function, the grade | `py.function`; answered OK |
| `run_selftest` | function | `py.function`; answered OK |
| `read_newest_unit` | function, the `--newest-unit` verb S11 reads | `py.function`; answered OK |
| `run_git` | function, the pinned and counted git call | `py.function`; answered OK |
| `load_conf` · `check_conf` | functions, the conf read and its S7 refusals | `py.function`; answered OK |
| `build_id_re` · `extract_unit_ids` · `extract_families` | functions, the S2 id reading | `py.function`; answered OK |
| `build_fixture` · `set_fixture_conf` | functions, the self-test's one-`fast-import` fixture | `py.function`; answered OK |
| `Refusal` | type, the S7 exit 2 | `py.type` |
| `read_mint_unit` | shell function in `tools/push-main.sh` | `sh.function`; answered OK |
| `ROUTED_COMMIT_CUTOFF` | conf key | none: conf keys carry no naming cell |
| `ROUTED_COMMIT_WAIVED` | conf key | none, as above |
| `routed commits name a specced unit` | gate leg, `subject = "repo"`, no guard, no `doc_reads`, `history_depth = "full"` | none |
| `routed-commits selftest` | gate leg, `subject = "kit"`, guard the kit directory | none |

### Files touched (estimate)

`tools/memory-tree/routed_commits.py` · `tools/push-main.sh` · `tools/push-main.test.sh` · `memory/guides/SESSION-KICKOFF.md` · `tools/memory-tree/tree_lib.py` · `tools/memory-tree/transition_audit.py` · `tools/memory-tree/kit.toml` · `tools/memory-tree/.memory-tree.conf.example` · `tools/memory-tree/README.md` · `tools/gate-legs.json` · `tools/run-gates/selftest-budgets.txt` · `.memory-tree.conf` · `memory/map/features/memory-tree-hygiene.md` · `memory/map/generated/symbols.json` · `memory/map/generated/inventories.json` · `memory/map/generated/MAP.md` · `memory/map/generated/CARDS.md`

### Rollout

Lands at order 4, after the write gate. The commit adding the leg also declares gov's
`ROUTED_COMMIT_CUTOFF`, so gov's bar is never armed without it. Commits other sessions landed earlier
on the cutoff day are graded too; AC10's run over gov's history names any, and the landing commit
lists each in `ROUTED_COMMIT_WAIVED`. From then on every commit this build
pushes that touches a product path names a unit, the build's single kit-version mint included: it
names the build's last unit. Adopters receive the leg when the memory-tree kit's version moves,
which happens once after the build's last unit touching that kit, and `TOOL-aRoutedQuill-5` scaffolds
both keys in the same release. Gov's ceiling row is 300 s, in the `declarations` chunk beside
`pass-order history`. The lander's mint subject (S11) changes in the same unit, so the first
attended landing after the leg arms already names its unit; `tools/push-main.sh` moving owes the
push-main kit's version, minted with the others. `.memory-tree.conf` and `tools/gate-legs.json` are
both on the kickoff manifest's `watch:` line, so the commit staging them re-stamps `last-audit` in
`memory/guides/SESSION-KICKOFF.md` with a delta line in its commit message.

### Alternatives rejected

- **Lifting pass-order's predicate.** Its home, `lib-unattended.sh`, ships only with the opt-in
  unattended kit, and memory-tree cannot depend on a kit that depends on it. The predicates also
  answer different questions: `build_commit` picks one commit per CLOSED unit and pass-order then
  grades that spec's plan state, while this leg grades every routed commit's attribution. The one
  join both make, which spec defines an id, is taken here from `parse_spec_h1`, the kit's declared
  predicate. Pass-order reads a whole token in a spec's first five lines instead, so the two differ
  at the edges: an id cited in a header line passes there and not here, and an H1 below line five
  passes here and not there. The attribution readings differ on purpose (S2): pass-order lets a
  `Pass:` trailer replace the subject, this leg reads the union. An arm in this file's self-test
  pins the union and `Pass: none`; nothing machine-joins the two files, and that is stated in the
  header.
- **A per-commit spawn**, as pass-order once had. Priced at 751 ms per spawn on node a, it is the
  shape that cost 10184 s.
- **A sha cutoff.** It grades by graph rather than by a date the committer sets, but every branch
  cut before the rule landed would red on its first push, and the conf that holds either kind is a
  file the graded run commits.
- **Narrowing WHOLE mode to `origin/<default>..HEAD`.** That is a local ref the run controls, and in
  CI HEAD is the tip, so the range would be empty and the leg would grade nothing.
- **A waiver registry file under `<MEMORY_ROOT>/project/`.** Hygiene check 3 would have to admit its
  name, and a conf key carries a short sha list with no engine edit.
- **Declaring `doc_reads`.** Gov's doc class holds two product files, so a doc-only push would skip
  the one leg that grades them.

## 5. Production-readiness checklist

- security — Read-only. The graded run controls the conf, so it can narrow `ROUTED_PATHS`, move the
  cutoff or list a waiver; the summary prints all three as a trace, not a guard. Replace refs and
  graft files are pinned off. RANGE mode honours no waiver, so the push boundary has no bypass but
  git's own `--no-verify`, which remote CI's WHOLE run then catches.
- perf / scale — Constant spawns. Measured 1.0 s for the log pass and 3.0 s for the spec read over
  gov's whole corpus (PINNED, node a, 2026-10-09); both grow linearly, against a 300 s ceiling.
- error / empty / loading states — S7's refusals and S8's zero line. A truncated stream refuses
  rather than reporting the commits it lost as clean.
- observability — The summary names the mode, the range, every count and the product set; each
  violation names sha, subject, ids, spec path and parent.
- risks — 75 of 493 recent routed commits name no unit, so a close's repair commits and reconcile
  mints must name one after landing (§8 F3). An adopter without the push-main kit has no RANGE
  mode, so a waiver there can excuse an unlanded commit, and a shallow CI checkout refuses until it
  fetches full history.
- testing — `--selftest` arms over scratch repositories, a held leg with a budget row.
- migration — Gov declares its cutoff in the landing commit. Adopters move with
  `TOOL-aRoutedQuill-5`.
- user docs — The kit README's file row and a CI line saying the leg needs full history; the
  refusal text names `fetch-depth: 0`.

## 6. Acceptance criteria

- **AC1** — When `routed_commits.py --selftest` builds a fixture whose routed commit names a unit
  whose spec landed one commit earlier, that commit passes; when the spec lands in the same commit as
  the code, the run exits 1 naming the commit, the spec path and the parent's short sha.
  Red when: a spec committed with its code passes, or a spec committed earlier is not found.
- **AC2** — When a fixture's routed commit names no id, or carries `Pass: none` and names no id in
  its subject, the run exits 1 naming the commit and `no unit id`; when its subject names no id and
  its `Pass:` trailer names the specced unit, it passes; when its subject names the specced unit and
  it carries `Pass: none`, it passes.
  Red when: an unattributed routed commit passes, a trailer's attribution is ignored, or `Pass: none`
  erases the subject's id.
- **AC3** — When `GATE_PUSH_BASE` names a fixture commit, only the commits after it are graded, a
  violation before it does not red, a violation after it reds even when `ROUTED_COMMIT_WAIVED`
  lists it, and the summary reads `RANGE`; unset, all zeros or naming no commit, the summary reads
  `WHOLE` with its reason and the whole history since the cutoff is graded.
  Red when: a push is redded by a commit it does not carry, a waiver admits a pushed commit, or an
  unresolvable base narrows the range.
- **AC4** — When `ROUTED_PATHS` or `ROUTED_COMMIT_CUTOFF` is blank, an entry names nothing tracked,
  climbs through `..` or covers the fixture's `MEMORY_ROOT`, the cutoff is not an ISO date, or the
  fixture clone is shallow, the run exits 2 naming the key, the entry or `fetch-depth: 0`.
  Red when: any of these exits 0.
- **AC5** — When the fixture's range holds commits and none touches `ROUTED_PATHS`, the run exits 0
  and prints `graded 0` with the range's commit count and the `ROUTED_PATHS` value.
  Red when: the zero line is absent, or omits the count.
- **AC6** — When the self-test's spawn counter wraps every `git` call over a fixture of 3 routed
  commits and again over 30, both runs record the same count.
  figure: DERIVED, the two counts compared in the arm.
  Red when: the count grows with the commits.
- **AC7** — When a fixture commit made with `GIT_COMMITTER_DATE` before the cutoff touches a
  product path and names no unit, it is counted as exempt; a merge is counted and not graded; a
  commit moving a product file out of `ROUTED_PATHS` with no unit id reds.
  Red when: an exempt commit reds, or the moved file escapes through rename detection.
- **AC8** — When `ROUTED_COMMIT_WAIVED` lists a violating sha in WHOLE mode the run exits 0 and
  counts it waived; when it lists a sha that is not a violation, the run exits 1 naming the sha as
  stale.
  Red when: a stale waiver passes.
- **AC9** — When the fixture's `FAMILIES` is blank, or its spec H1s define no id while spec files
  are tracked, the run exits 2 naming the empty id map; when the parsed count differs from
  `git rev-list --count`, it exits 2 naming both counts.
  Red when: a dead id map or a truncated log reports a clean run.
- **AC10** — When `python tools/govkit/govkit.py selfcheck` runs, it reports no problem for the
  memory-tree descriptor's two new gate legs, and `routed_commits.py` run over this repository after
  landing prints a `WHOLE` summary naming the cutoff and exits 0.
  Red when: a descriptor row is malformed, or gov's own history since its cutoff carries a commit
  the leg reds.
- **AC11** — When the self-test's fixture range holds a routed commit attributed to a specced unit
  followed by a commit shaped as the lander's mint, subject
  `mint: kit versions onto origin/main at <sha8>` naming that unit and a `Pass: none` trailer,
  touching a product path, the leg passes it in RANGE mode; the same mint whose subject names no id
  reds naming `no unit id`. When `tools/push-main.sh` lands from a scratch-clone fixture whose
  pushed range attributes a unit and owes a kit version, the mint commit's subject names the range's
  newest unit id and its `Pass:` trailer reads `none`.
  Red when: the lander's mint reds its own pre-push leg, an id-less mint passes, or the mint lacks
  `Pass: none`.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `install-prefix (shipped surface)` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `kickoff-manifest ratchet` · `pass-order history` · `spec tokens (a spec's own names resolve)` · `push-main self-test`

New arm: routed_commits.py --selftest · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC11 · a fixture whose spec lands in the same commit as its code, against a predicate that grades nothing · none
New arm: push-main.test.sh mint subject · covers AC11 · a lander whose mint subject names no unit id · none

AC10 is a direct observation of this repository and adds no arm.

## 8. Open questions

- **F1 — Does any attributed id suffice, or must the first id in the subject be the owner?**
  Any id is the membership test pass-order already applies, and a subject citing a second unit in
  prose still names one with a spec. First-only binds the house shape `build(<slug>): <ID> — <what>`
  harder and reds `TOOL-x-1, -2`-style subjects only when the first id fails.
  Recommendation: any id, stated in the header as what the leg does not check.
  RESOLVED (owner, 2026-10-09): any id, stated in the header as what the leg does not check.
- **F2 — Is the attribution the subject alone, as the shared contract says, or
  `read_attribution_tokens`' rule?**
  Subject alone reds the 6 recent routed commits that name their unit only in a `Pass:` trailer.
  The trailer rule reds the 1 that names an id in its subject and carries `Pass: none`, and keeps
  one attribution reading across the kits' history legs.
  Recommendation: the trailer rule, as S2 is written.
  RESOLVED (owner, 2026-10-09): the trailer rule: an id in the subject or in the `Pass:` trailer attributes the commit.
- **F3 — Does a close's repair commit or a reconcile's version mint need a unit id?**
  They are 75 of 493 recent routed commits. Option (a): every routed commit names a unit; a repair
  names the unit it repairs and a mint names the build's last unit. Option (b): exempt commits that
  move only version markers. RESOLVED (owner, 2026-10-09): (a), by owner decision D3 that every
  product-code write needs a specced unit.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · cross-read fold: order 3 to 4, because `KICK-aRoutedQuill-1` moved
  from order 1 to 2, which shifts every later step by one.
- rev-3 · 2026-10-09 · §8 · owner resolves F1 (any id) and F2 (subject or `Pass:` trailer).
- rev-4 · 2026-10-09 · §2 · §4 · §6 · §7 · the M2 cross-read of 2026-10-09 found that
  `tools/push-main.sh`'s attended mint commit names no unit and touches `ROUTED_PATHS`, so under
  F3(a) every attended landing owing a kit version would red its own RANGE leg; S11 and AC11 make
  the mint name the range's newest unit id with `Pass: none`, and S2 and AC2 now read the union
  F2's resolution states rather than the trailer-replaces-subject rule that would red such a mint.
  Files touched gains `tools/push-main.sh` and `memory/guides/SESSION-KICKOFF.md`, Gates gains
  `push-main self-test`, and Rollout re-stamps the kickoff manifest for the watched conf and legs.
- rev-5 · 2026-10-09 · §2 · §4 · the build: S11 names how the lander reads the unit — a
  `--newest-unit <range>` verb on this file, reached through push-main's sibling-kit resolver — and
  the subject's ` for <id>` spelling; the zero line names the cutoff, because a range of exempt
  commits also grades zero and "touches ROUTED_PATHS" alone would be false there; the Inventory
  gains the helpers the build wrote. `FAMILIES` prefixes are validated as letters before they reach
  a regex, the conf-value-into-a-regex class.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a push-time gate leg that grades every commit touching
product paths for a unit id in its subject whose spec existed at its first parent, one git log pass"`
ranked `build_commit` and `GIT` in `tools/unattended/lib-unattended.sh` and `parse_spec_h1` and
`build_spec_path_re` in `tools/memory-tree/tree_lib.py`. The unattended seams are unreachable from a
default kit, for §4's reason. The extended seams are `parse_spec_h1` and `parse_conf` in `tree_lib.py`
and the pinned runner in `transition_audit.py`, whose `build_git_env` moves to `tree_lib.py` because
a second engine now reads it, the rule that file's header states.

Recall terms used: `pass-order first-parent build-commit attribution Pass-trailer GATE_PUSH_BASE
advertised-tip whole-token range-mode cutoff waiver subject-cache liveness` — which surfaced
`TOOL-dBriefedPass-3`, `TOOL-aWindowedPass-2`, `TOOL-dUnstuckLanding-17` and `TOOL-aMendedFleet-65`.
