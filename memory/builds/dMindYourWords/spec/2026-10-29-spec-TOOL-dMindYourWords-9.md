# TOOL-dMindYourWords-9 — enforcement: the work order's vocabulary slice, staged names at commit, offenders by name at the bar

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 14 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0270@01096b8c whole
**Carries:** node:policy-key.lexicon.at-commit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md](../build/2026-10-29-build-TOOL-dMindYourWords-7-reuse-scout-b.md) | research | TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Naming is enforced only as a corpus count at the bar: nothing judges a name at commit or by name, a
fixed offender plus a new one nets to zero, and landings absorbed raises instead (gap-lex-03). This
unit supplies the vocabulary at the point of naming, refuses a staged offender at commit as
`lexicon.at-commit` says, and compares the branch's offenders with its base's by name on every bar,
with move-aware keys proven by replaying the merges since 2026-08-16 (lexicon review
`[enforcement]` :328-353, L-2 :527-533, settled :569).

## 2. Scope (IN)

Build-run preconditions: TOOL-dFurnishedOrders-4 (`render_slot`, `ORDER_SLOTS`) for S2; until
TOOL-dWitnessedBar-11's leg factory lands, S8's leg is also a hand-written row of
`tools/gate-legs.json`; until TOOL-dTotalRecall-13's `read_defs_at` lands, S3 reads a revision itself.

- **S1** — The slice. `lexicon.py --vocabulary <spec> [--paths <path>...]`, through
  `render_vocabulary_slice(root, spec, paths)`, prints four blocks: `#### verbs`, each `VERBS` row
  with its gloss, its `NOT` negatives included; `#### nouns`, each cluster of `canon.NOUNS` merged
  with the `NOUNS:` overlay as `<representative> — NOT <alternative>, ...`
  (TOOL-dMindYourWords-10); `#### packs`, the packs `resolve_packs` (TOOL-dMindYourWords-8) returns
  under `lexicon.packs` for the files `--paths` names; and `#### names`, one answer per
  identifier the spec's `### Inventory` names. An identifier is a backticked token with no space on a
  line that also names a declared cell `<ext>.<surface>` in backticks; it is answered by
  `--suggest <name> --as <cell>`, with `--base <dotted.Base>` (TOOL-dMindYourWords-6) where the line
  names a backticked dotted name right after the word `base`. A line naming no declared cell is listed
  under `not answered: no cell on its line`. Exit 0, 1 on a declaration refusal, 2 on usage. Observed
  by AC1.
- **S2** — The work-order slot. `render_handoff` (`tools/roles/handoff.py:312`) renders
  `render_slot("vocabulary", state, body)` (TOOL-dFurnishedOrders-4 S1) on every order whose
  `input:spec` hands a spec, running the lexicon as a subprocess found by
  `resolve_kit_dir("lexicon", "lexicon.py", KIT_DIR)` with `--vocabulary <spec>` and, after
  `--paths`, every backticked path under the spec's Files touched sub-head. States: `filled` with its
  stdout;
  `not-installed: no lexicon declaration; name by this repository's conventions` when the kit or
  `.lexicon.conf` is absent. Exit 1 refuses the render, naming the spec and the lexicon's line.
  `ORDER_SLOTS` (`tools/roles/roles_lib.py`) gains `vocabulary` (§8 F1). Observed by AC2.
- **S3** — Reading a revision. `measure_pass` and `scan_corpus` (`tools/lexicon/lexicon.py:2796`,
  `:2262`) gain two keywords, `rev=None` and `paths=None`, keeping `scan_corpus`' 4-tuple. With `rev`
  set, the walk lists the tree with one `git ls-tree -r -z <rev>` and reads every armed blob with one
  `git cat-file --batch`, as `read_defs_at_sha` does (`:4113-4164`), and the readers that re-read a
  file's text (`:2510`, `:2561`, `:2596`) read that blob text instead of the working tree. With
  `paths` set, only those paths are graded. Both pass `rev` to `derive_established_verbs`
  (TOOL-dMindYourWords-10 S5). Once TOOL-dTotalRecall-13 lands, the revision read is
  `read_defs_at(root, rev, paths)`. Observed by AC3.
- **S4** — Move-aware comparison. `read_rename_map(root, base, tip=None, cached=False)` returns
  `{old path: new path}` from `git diff -M --name-status -z`, against the working tree when `tip` is
  `None` and against the index under `cached`. `check_added_keys(base_keys, tip_keys, renames)` maps
  each base key's path through `renames`, then reads each tip key the mapped base lacks as a move when
  its `<rule>\t<identifier>` tail, without its ordinal, occurs among the mapped base keys at a path
  whose tip keys lack that tail, each base occurrence excusing one tip key; the rest are added.
  It returns `(added, moved)`. Keys are `render_offender_keys`' (TOOL-dMindYourWords-1, I4), whose
  path stays in every key. Observed by AC4.
- **S5** — The commit arm. `lexicon.py --staged`, through `check_staged_names(root)`, reads
  `read_policy_value("lexicon.at-commit", root)`. Under `off` it prints one line and grades nothing.
  Otherwise it reads the staged set from `git diff --cached -M --name-status -z`, keeps the paths an
  armed extension declares and `check_out_of_scope` (TOOL-dMindYourWords-15) leaves in, and grades
  them at the index's tree (`git write-tree`) against their old paths at `HEAD`, both through S3 with
  this tree's `.lexicon.conf`. For a staged definition in a declared family it adds to both sides the
  files `git grep -l -i` finds over `HEAD` and over `--cached` spelling any form of its object, so a
  drift group is graded whole. `check_added_keys` with the staged renames names each addition;
  `refuse` prints each and exits 1, `warn` prints each and exits 0. Observed by AC5, AC6 and AC7.
- **S6** — The hook block. `.githooks/pre-commit` gains one block, after the policy guard and before
  the memory-tree leg, run when `.lexicon.conf` exists and any path is staged: it resolves the gate
  through `resolve_kit_gate lexicon lexicon.py`, announces a miss through `print_kit_miss`, skips a
  merge commit (`git rev-parse -q --verify MERGE_HEAD`) with one line saying the bar grades it, and
  otherwise runs `with_hook_index "$py" "$g" --staged` through the python the tracked
  `resolve-python.sh` resolves, as the policy guard does (`:204-214`), setting `rc=1` on exit 1 and on
  a missing launcher. Its header comment
  declares the pack fields of TOOL-dWellOiledMachine-10 S1, `owner=dMindYourWords`,
  `class` from `lexicon.at-commit`, `failure=closed`, `budget-ms=2000`, `key=lexicon.at-commit`, and
  its gate name is `lexicon`, so TOOL-dWellOiledMachine-49 S3 journals a refusal as
  `git:pre-commit/lexicon`. Observed by AC5 and AC8.
- **S7** — The bar arm. `lexicon.py --compare`, through `check_offenders_by_name(root)`, reads its base
  through `resolve_compare_base`, carried inline with the remote ladder as `compare_base_py` and
  `remote_ladder_py` (`tools/lib/compare_base.py:15-50`, held byte-identical by
  `tools/lib/resolve-python.test.sh`'s parity rows). It measures the working tree and the base, both
  under this engine and this tree's declaration, and runs `check_added_keys` with
  `read_rename_map(root, base)`. It prints one summary line,
  `lexicon by name: base <sha8> (<why>) · <b> at base · <t> at tip · <a> added · <m> moved`, then each
  added key with its detail, and exits 1 on any added key. With no base it prints
  `lexicon by name: not graded — <why>` and exits 0. Under `lexicon.pin = "no-gate"`, read through
  `read_policy_value("lexicon.pin", root)`, it reports and exits 0; under `absorb` it still refuses.
  Observed by AC9 and AC10.
- **S8** — The leg. A `[[gate_leg]]` in `tools/lexicon/kit.toml`, `name = "lexicon offenders by name"`,
  `subject = "repo"`, `argv = ["python", "{kit}/lexicon.py", "--compare"]`, its `guard` the guard of
  `lexicon naming predicates` (`tools/lexicon/kit.toml:163-167`), under which every graded definition
  of this tree sits, and `reads` naming the base and the history; it runs on every bar whose diff
  touches a graded path, never only under `GATE_ATTRIBUTE` (`tools/run-gates/run-gates.sh:256`,
  `:4921`). Registered through `leg_factory.py` (TOOL-dWitnessedBar-11 S1, S8), and until then a row
  of `tools/gate-legs.json` with `chunk = "declarations"` and `ceiling = 300`. The lexicon dossier
  claims the leg. Observed by AC11.
- **S9** — The replay. A record script under `memory/builds/dMindYourWords/build/` walks every merge
  `git rev-list --merges --since=2026-08-16 <tip>` names (DERIVED at the build tip; 577, 269 of them
  on the first parent, from `ba8b3c8c`, measured 2026-10-29), and for each compares the merge with
  its first parent over the armed paths `git diff -M --name-status <M>^1 <M>` names, through S3 and `check_added_keys`, every rule but
  `drift`, `noun` and `problem`, whose groups span the corpus. A red key is attributable to a move when
  its path is the new side of a rename, or its tail stood at the base in a file the merge left absent or
  changed. Its record states the population, the move reds under the shipped keys, which must be 0,
  and the move reds under path-only keys, the raw set difference `derive_attribution` takes today
  (`run-gates.sh:4788-4789`). Observed by AC12.
- **S10** — `lexicon.at-commit`'s three values, the catalogue row's verbatim
  (`tools/policy/catalogue.toml:400`), each a planted case, and the split table's nine cells across
  `lexicon.at-commit` and `lexicon.drift` (lexicon review :377-381), each a planted case. The row gains
  `summary` and `usage`, and `policy.py lists --write` drains its name from
  `tools/policy/unsummarised-keys.txt` (`:103`). Observed by AC6, AC7, AC13 and AC14.
- **S11** — `help/lexicon.md` gains a section on the slice, the commit arm, its bypass and the bar's
  by-name comparison, and `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` state the three
  modes. Observed by AC15.

## 3. Non-goals (OUT)

- The debt pin and its keyed ledger: TOOL-dMindYourWords-1. This arm measures both trees and reads no
  ledger; the pin stays the backstop.
- Rendering git-hook packs into `.githooks/pre-commit`: no parent specs it (§8 F4). The block is
  written by hand and the rendering is asked of dWellOiledMachine.
- Journaling a refusal or a bypass: TOOL-dWellOiledMachine-49. A `--no-verify` bypass runs no hook,
  and S7's comparison grades what it skipped.
- The drift and noun predicates: TOOL-dMindYourWords-10. This unit only compares their keys.
- Forced-name answers: TOOL-dMindYourWords-6 answers `--suggest --base`; this unit hands it the base.
- Grading merge commits at commit: left to the bar, whose diff from the merge base is the branch's.
- The Loop Review's reading of trends and the reviewer's lens: other builds' surfaces.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, `render_offender_keys` and `read_policy_value`, the keys S4 compares and the reads of `lexicon.at-commit` and `lexicon.pin`
- **consumes-from** `TOOL-dMindYourWords-15` — `check_out_of_scope`, which S5 applies to the staged set and S3's walk honours
- **consumes-from** `TOOL-dMindYourWords-6` — `--base`, which S1 passes for a name whose Inventory line names its base
- **consumes-from** `TOOL-dMindYourWords-10` — `canon.NOUNS` for S1's nouns block, the `drift` and `noun` keys S5 and S7 compare, and `derive_established_verbs`, to which S3 passes `rev`
- **consumes-from** `TOOL-dMindYourWords-8` — `resolve_packs`, the packs `lexicon.packs` selects for the write set, which S1 lists
- **hands-off** `TOOL-dMindYourWords-16` — the leg `lexicon offenders by name`, which that unit puts in the lexicon's leg pack
- **hands-off** external — dWellOiledMachine: rendering a git hook's staged arm from its pack fields (§8 F4)
- **hands-off** external — dFurnishedOrders: `vocabulary` in `ORDER_SLOTS` (§8 F1)
- **hands-off** `TOOL-dMindYourWords-29` — `check_added_keys`, the commit arm's candidates, the replay boundary and `--compare`'s base, which the minors batch repairs (review ids 20, 25, 30, 47)

## 4. Design

### Evidence

At this base the bar's only by-name reading is the attribution block, which runs only under
`GATE_ATTRIBUTE` and only on a red leg (`run-gates.sh:256`, `:4921-4923`); the leg's verdict is the
scalar `VERB_OFFENDER_PIN="1212"` (`.lexicon.conf:327`). The `--offenders` keys already carry the path
and no line (`lexicon.py:3482-3515`), so a `git mv` of a file holding an offender reads as one
offender added and one fixed. `lexicon.py --offenders` took 6.25 s here (scout B finding 3, PINNED
2026-10-29), so the commit arm grades staged paths only. The hook has no lexicon block
(`.githooks/pre-commit:1-310`), and its staged reads follow `with_hook_index` (`:9-11`); four legs
that do not (`:227`, `:247`, `:256`, `:280`) are not this unit's to fix. A policy read costs 0.24 s
(`python tools/policy/policy.py get lexicon.at-commit`, PINNED, measured 2026-10-29).

### The three arms over one comparison

| Arm | Base side | Tip side | Renames | Decides |
|---|---|---|---|---|
| commit (`--staged`) | `HEAD`, old paths | the index's tree, staged paths | `git diff --cached -M` | `lexicon.at-commit` |
| bar (`--compare`) | `resolve_compare_base`, whole tree | working tree, whole tree | `git diff -M <base>` | binding unless `lexicon.pin = "no-gate"` |
| replay (S9) | `<M>^1`, changed paths | `<M>`, changed paths | `git diff -M <M>^1 <M>` | the proof |

All three measure both sides with this engine and this tree's `.lexicon.conf`, so a vocabulary change
is never read as the branch's code adding offenders; a vocabulary change has its own path, the write
path and its re-baseline (TOOL-dMindYourWords-11). All three call `check_added_keys`, so the replay
proves the comparison the arms run.

### The split table, as the arms read it

| `lexicon.at-commit` | `lexicon.drift: refuse-new` | `report` | `off` |
|---|---|---|---|
| `refuse` | `--staged` exits 1; `--compare` exits 1 | no key; both exit 0 | not measured |
| `warn` | `--staged` warns, exit 0; `--compare` exits 1 | no key; both exit 0 | not measured |
| `off` | `--staged` grades nothing; `--compare` exits 1 | no key; both exit 0 | not measured |

`report` and `off` emit no `drift` or `noun` key (TOOL-dMindYourWords-10 S7), so neither arm can
refuse a split under them, and the tally line counts them under `report`.

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and
answered OK: `render_vocabulary_slice`, `read_rename_map`, `check_added_keys`, `check_staged_names`,
`check_offenders_by_name`. CLI modes: `--vocabulary`, `--staged`, `--compare`. Leg:
`lexicon offenders by name`. Slot point: `vocabulary`.

### Rollout

The bar arm binds first: the commit arm's bypass relies on it (lexicon review :336). The replay runs
before either arm refuses, and its record is committed with the unit. The slot lands last, on
TOOL-dFurnishedOrders-4.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`
- `tools/lexicon/kit.toml`
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`
- `tools/gate-legs.json` (the fallback row; rendered by `leg_factory.py --write` once it lands)
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `tools/roles/handoff.py`
- `tools/roles/roles_lib.py`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`)
- `memory/map/features/lexicon.md`
- `memory/map/generated/` (re-rendered by `gen_map.py --write`)
- `memory/builds/dMindYourWords/build/` (the replay script and its record)
- `help/lexicon.md`

### Alternatives rejected

- **Promote the attribution block to binding.** Rejected: it runs only on a red leg and only under
  `GATE_ATTRIBUTE`, and its rule 5 compares raw sets (`run-gates.sh:4788-4789`), the path-only keys
  the replay shows red on a move.
- **Keys with the path dropped.** Rejected by I4: a path-free key cannot say which site a refusal
  names, and two offenders of one name in two files would collapse into one.
- **Measure the base with the base's own engine and declaration.** Rejected by §8 F2's test.
- **Call `run()` from the hook.** Rejected by its cost: a full pass took 6.25 s against a 2 s budget.

## 5. Production-readiness checklist

- security — the hook runs this tree's own kit through `resolve_kit_gate`; nothing reads a network.
  The refusal is fail-closed: an exit other than 0 sets `rc=1`.
- perf / scale — the commit arm grades only staged paths and their drift candidates; the bar arm costs
  two full measurements, about twice the 6.25 s pass; the replay is a one-off build cost.
- error / empty / loading states — no base: `not graded` with its reason; no `.lexicon.conf`: the
  block does not run; a kit no rung resolves: `print_kit_miss`; a merge: one line, nothing graded.
- observability — the summary line, each added key with its detail, the replay record.
- risks — a rename git's similarity index misses reads as a delete and an add; S4's tail rule excuses
  it, and the replay measures how often.
- testing — fixtures in `tools/lexicon/selftest.py` and `.githooks/pre-commit.test.sh`; §7 New arms.
- migration — N/A: no data changes; an adopter's hook gains a block that runs only where the
  declaration exists.
- user docs — `help/lexicon.md` (S11).

## 6. Acceptance criteria

The commit fixture is a scratch git repository under `%TEMP%` with a short name, its hooks path at
this repository's `.githooks/` copy, a `.lexicon.conf` declaring `LANGS="py:python-ast:parser"` and the
`VERBS` rows `load`, `read`, `parse` and `check`, `FAMILIES: acquire load read parse`, a first commit
adding `a.py` defining `load_conf` and `get_x`, and a `main` branch with a remote-tracking copy for
`resolve_compare_base`. Policy is a committed `.governance/policy.toml` on its default branch.

- **AC1** — When `python lexicon.py --vocabulary spec.md --paths a.py` runs on a planted spec whose
  `### Inventory` line names `` `read_conf` `` and `` `py.function` ``, and another naming
  `` `emit` ``, `` `py.function` `` and base `` `logging.Handler` ``, it prints the four blocks, an
  answer for each, and a `not answered` line for a third line naming no cell.
  Red when: a block is missing, or `--base` is not passed for the second name.
- **AC2** — When a probe calls `render_handoff` for a builder order whose `input:spec` is the planted
  spec, the order holds `### vocabulary` and `slot vocabulary · filled`; with `.lexicon.conf` absent
  it holds `slot vocabulary · not-installed:`.
  Red when: the slot is absent, or an absent declaration renders `filled`.
  fixture: needs TOOL-dFurnishedOrders-4 landed.
- **AC3** — When `measure_pass` runs with `rev` set to the fixture's first commit after a second
  commit renamed `get_x`, its offender keys name `get_x` and `git status` shows the working tree
  untouched; with `paths=["a.py"]` no other file is read.
  Red when: a revision read touches the working tree, or `paths` grades another file.
- **AC4** — When `check_added_keys` runs on the fixture after `git mv a.py b.py`, with the map
  `read_rename_map` returns, it returns no added key and one moved; the raw difference
  `set(tip) - set(base)` names `b.py\tverb\tget_x`, the path-only red.
  Red when: the move is returned as added, or the raw difference is empty.
- **AC5** — When the fixture stages a new `fetch_y` and `git commit` runs, the hook exits 1 naming
  `fetch_y`; after `git mv a.py c.py` alone, the commit succeeds.
  Red when: a staged offender commits, or a move is refused.
- **AC6** — When the fixture's committed policy sets `[lexicon]` `at-commit = "warn"`, the commit
  staging `fetch_y` succeeds and prints `fetch_y`; with `at-commit = "off"`, `lexicon.py --staged`
  prints its one line and grades nothing; with `refuse` or no key, the commit is refused.
  Red when: any value acts as another.
- **AC7** — When the fixture stages `parse_conf` beside the committed `load_conf`, `lexicon.py
  --staged` names `parse_conf` as `drift` against `load`, the drift candidate found by `git grep`
  although `a.py` is not staged.
  Red when: the split passes because the established site is outside the staged set.
- **AC8** — When `bash .githooks/pre-commit` runs during a merge with `MERGE_HEAD` set and a staged
  offender, it prints the merge line and does not refuse; when the lexicon kit is absent it prints the
  `print_kit_miss` line; the staged one-file commit's lexicon block finishes within 2000 ms.
  Red when: a merge is graded, a miss is silent, or the block exceeds its budget.
  cost: about 0.5 s per run on this node; figure: the 2000 ms budget is PINNED, the run's time
  DERIVED.
- **AC9** — When a fixture branch adds `fetch_y` and fixes `get_x`, `lexicon.py --compare` exits 1
  naming `fetch_y` and its summary reads `1 added`; a branch that only moves `a.py` exits 0 with
  `1 moved`.
  Red when: the fix and the addition net to green, or a move is refused.
- **AC10** — When the fixture's committed policy sets `[lexicon]` `pin = "no-gate"`, `--compare`
  prints the added key and exits 0; with `pin = "absorb"` it exits 1; with no remote-tracking ref it
  prints `not graded` and its reason.
  Red when: `absorb` passes an added key, or a missing base reads green with no line.
- **AC11** — When `grep -n "lexicon offenders by name" tools/lexicon/kit.toml tools/gate-legs.json`
  runs, each holds the leg with the predicates leg's guard, and `memory/map/features/lexicon.md`
  claims it.
  Red when: the leg is unguarded differently, or unclaimed.
- **AC12** — When the replay script runs over this repository, its record reads 577 merges or the
  count the rev-list derives at the build tip, move reds under the shipped keys 0, and the path-only
  move reds as measured.
  Red when: any move red remains under the shipped keys.
  cost: one pass per merge over its changed paths; figure: the merge count is DERIVED by
  `git rev-list --merges --since=2026-08-16`, and 577 is its value from `ba8b3c8c`.
- **AC13** — When the fixture stages a new split `parse_conf` under each of the nine combinations of
  `lexicon.at-commit` and `lexicon.drift` in its committed policy, `--staged` and `--compare` exit as
  §4's split table states, cell by cell.
  Red when: any cell's exits differ from the table.
- **AC14** — When `git grep -n 'read_policy_value("lexicon.at-commit"' -- tools/lexicon/lexicon.py`
  runs, it finds the literal reader, and `grep -c "^lexicon.at-commit$"
  tools/policy/unsummarised-keys.txt` prints 0.
  Red when: the key has no literal reader, or the row lacks `summary` or `usage`.
- **AC15** — When `grep -n "lexicon.at-commit\|--compare\|--vocabulary" lexicon.md` runs in `help/`,
  each matches.
  Red when: the page omits one.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `branch-guard self-test` · `codebase-map kit selftest` · `measure-legs selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `roles catalogue` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/lexicon/selftest.py · covers AC1 AC3 AC4 AC6 AC7 AC9 AC10 AC13 · a moved offender, a fixed-plus-added pair, a split under each policy pair and a missing base, staged against today's engine, which has no `--compare`, `--staged` or `--vocabulary` · none
New arm: .githooks/pre-commit.test.sh · covers AC5 AC8 · a staged offender, a `git mv`, a merge and an absent kit, staged on today's hook, which commits the offender · none

## 8. Open questions

- **F1 — Where does the slice's `vocabulary` point come from?** (a) This unit adds `vocabulary` to
  `ORDER_SLOTS` in `tools/roles/roles_lib.py` once TOOL-dFurnishedOrders-4 lands, and an ask makes
  that spec agree; (b) the slice waits until dFurnishedOrders admits the point itself; (c) the slice
  renders its own block beside `render_slot`. (b) may never arrive, and (c) is a second renderer of
  one block grammar. Rung 3. RESOLVED (agent, 2026-10-29, delegated): (a). Ask for dFurnishedOrders:
  `ORDER_SLOTS` (TOOL-dFurnishedOrders-4 S1) carries `vocabulary`, the lexicon's work-order slice ·
  accept `render_slot("vocabulary", "filled", body)` returns its block rather than raising, and
  TOOL-dFurnishedOrders-4 S1's tuple lists it. widens: none · relaxes: none
- **F2 — How is the base's offender set measured?** (a) This engine and this tree's declaration over
  the base's sources, read at the revision; (b) the base's committed debt ledger; (c) the base's own
  engine and declaration in a checkout. The test: a branch whose write-path change removes a verb row
  re-grades definitions it never touched. Under (b) and (c) those definitions read as added, so the
  re-baseline's own commit is refused; under (a) they stand at both ends. Rung 3. RESOLVED (agent,
  2026-10-29, delegated): (a). widens: none · relaxes: none
- **F3 — Which merges does the replay walk?** (a) Every merge since 2026-08-16 reachable from the tip,
  577 from `ba8b3c8c`, each against its first parent; (b) the 269 first-parent landings only. (a)
  contains (b) and adds the merges of the default branch into a branch, the class
  `a-merge-of-the-default-branch-read-as-additions` the debt fold names (lexicon review :630). Rung 3,
  the most feature-rich. RESOLVED (agent, 2026-10-29, delegated): (a). widens: none · relaxes: none
- **F4 — How does the commit check reach `.githooks/pre-commit`?** (a) A block written by hand,
  declaring the pack fields in its header so a renderer can take it over, and an ask; (b) wait for a
  parent to render git-hook packs. No parent does: TOOL-dWellOiledMachine-10's dispatcher handles
  harness events only and gives `pre-commit` a witness row (its S2, S10). Rung 3. RESOLVED (agent,
  2026-10-29, delegated): (a). Ask for dWellOiledMachine: render a git hook's staged arm from a kit's
  pack fields (`owner`, `class`, `failure`, `budget-ms`, `key`) into `.githooks/pre-commit`'s
  staged-arm sequence · accept the lexicon's block renders byte-identical to its hand-written form,
  and a pack whose `class` is `refuse` sets the hook's `rc`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: `render_offender_keys`, the bar's leg signature at this base
(`tools/lexicon/lexicon.py:3482-3515`, `tools/gate-legs.json:1455-1477`); `read_defs_at_sha`'s batched
revision read (`lexicon.py:4113-4164`), generalised into S3 rather than copied; `resolve_compare_base`
(`tools/lib/compare_base.py:15-50`), inlined as every consumer inlines it; the hook's
`with_hook_index`, `resolve_kit_gate` and `print_kit_miss` (`.githooks/pre-commit:9-11`, `:174-185`);
`render_handoff` (`tools/roles/handoff.py:312`) and TOOL-dFurnishedOrders-4's `render_slot`. The probe
`python tools/codebase-map/reuse_lookup.py "compare the branch offender keys with the base offender
keys and map renamed paths"` ranked `resolve_compare_base` (SEAM) and nothing that maps renames;
`python tools/codebase-map/reuse_lookup.py "grade staged definitions at commit inside the pre-commit
hook within a time budget"` ranked commit readers by name stem, none a staged grader. So no existing
seam fits the rename map or the move rule, and both are new over the seams above. Where scout B's
record disagrees with source: it reads the attribution's compare at `run-gates.sh:4774-4799`, where
the set compare itself is `:4788-4789`; its `:256` and `:4921` hold.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon judge names at commit
and compare offenders by name at the bar with move-aware keys" --terms "lexicon at-commit pre-commit
offenders signature attribution rename git-diff-M move-aware replay merge-base"`
