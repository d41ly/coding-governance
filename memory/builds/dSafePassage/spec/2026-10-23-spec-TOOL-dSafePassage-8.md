# TOOL-dSafePassage-8 — gov first for every step: the lander walks each new step on gov's own tree, recorded in gov's source-mode receipt

**Status:** DEFERRED · rev-4 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0025@4e486ab9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-8-deviation-143.md](../build/2026-10-23-build-TOOL-dSafePassage-8-deviation-143.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-8-deviation-152.md](../build/2026-10-24-build-TOOL-dSafePassage-8-deviation-152.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-8-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-8-1-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-8-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-8-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

Every upgrade step runs on gov's own tree in the lander's prepared merge before any adopter meets
it (P38, AP-30, SA-3). It is recorded in gov's source-mode receipt, which this unit creates at
`.governance/install.json` with `"mode": "source"` (the brief's S10). The receipt's `steps` lists
every declared step id, and a step whose witness does not hold on gov's tree refuses the landing.
To get there, gov's deploy plan must be accepted and `update` must run on gov's own tree the way
an adopter runs it. Today neither holds: `update` refuses the gov checkout as its target
(`tools/govkit/govkit.py:9167-9168`), and `plan --target .` exits 2 on gov's own answers. This
closes `gap-deploy-20`.

## 2. Scope (IN)

- **S1** — Source mode. `test_source_target(root, target)` in `tools/govkit/govkit.py` holds when the
  target resolves to the gov checkout. There, `update` stops refusing (`:9167-9168`) and runs in
  source mode, which treats the receipt and the walk as follows:
  - **The receipt.** It is `.governance/install.json` with `"mode": "source"`, written through
    TOOL-dSafePassage-3's receipt writer at schema 4. An absent receipt is created there. It holds
    the deploy file's `prefix` and `kits`, `gov_source` `.`, `files`, `steps` and no
    `gov_commit`.
  - **File rows recorded, never graded.** `files` holds one row per destination the accepted plan
    of S3 derives for gov's selection, each with `path`, `kit`, `role` and `source` and no hash
    field. They are rewritten whole at each source walk, so a file gov stops shipping leaves the
    next landing's rows. The row grid does not grade or write them, because gov's files are their
    own sources. They are the `file` class TOOL-dSafePassage-10's step gate reads.
  - **The vintage.** The vintage preconditions do not apply (`:9212-9222`, `:9231-9232`), because a
    source receipt has no vintage commit. The write preconditions do apply
    (`demand_writable_target`, `:7449-7460`).
  - **The walk.** TOOL-dSafePassage-2's `run_step_walk` runs over `derive_pending_steps`, which
    gains a source-mode branch: every declared step whose id `steps` does not hold as `applied`,
    in the brief's S5 order, since a source receipt has no vintage commit to walk from.

  Observed by AC3, AC4, AC8 and AC9.
- **S2** — The landing's check. After the walk, `check_gov_first(receipt, declared, target)` in
  `tools/govkit/upgrade_steps.py` asks two things. First, the `steps` ids must equal the declared
  ids both ways, where a listed id that no row declares must be the old id of a succession row in
  `tools/govkit/registry.toml` (the brief's S2). Second,
  every step listed `applied` must have its witness hold now on gov's tree, which it re-runs under
  TOOL-dSafePassage-7's runner. Any miss exits 1 and names each id. Observed by AC3 and AC4.
- **S3** — Gov's deploy plan is accepted. Two refusals stand between gov's
  `.governance/deploy.toml` and an accepted plan, both measured on 2026-10-23:
  - **The answers.** `target_context` (`:1436-1500`) grades every `[answers]` string through the
    prose class, so nine answers that only the charter renderer consumes are refused. They carry
    `—`, `·`, `>`, `;`, `<`, `(` and a backtick. From now on it grades and enters an answer only
    when the entry's own descriptor names its `{token}`. An answer that no template of that entry
    names never reaches a substitution there, and is not entered.
  - **The playbook path.** The playbook entry's seed row has `to = "{playbook_path}"`, which gov's
    deploy file does not answer. In source mode, a destination naming a token the descriptor
    leaves unanswered resolves to the row's own source path, because in gov's tree the row's bytes
    already sit where they are read from.

  Observed by AC1 and AC2.
- **S4** — The lander runs gov first. `run_gov_first` in `tools/push-main.sh` runs
  `govkit.py update --target "$top" --write`, found the way `run_minter` finds the deployer
  (`:802-822`). It runs in `cmd_prepare` after the mint and before the regeneration (`:902-911`), so
  the receipt joins the one rewritten merge. It runs in the attended landing after the mint commit
  (`:1084-1096`), as its own commit `steps: gov first onto <remote>/<branch> at <sha8> for <unit>`
  with a `Pass: none` trailer, named the way the mint commit is. A refusal takes a refused mint's
  exit shape: the branch is left unmoved, exit 1. Observed by AC5 and AC6.
- **S5** — The adopter's lander is unchanged. Where no govkit deployer resolves beside the lander,
  which is every adopter, `run_gov_first` prints one line and returns 0, as `run_minter` does. Where
  the deployer resolves and no Python does, it refuses. No later gate re-runs a step on gov, so
  skipping there would land a step gov never ran. Observed by AC6.
- **S6** — `tools/run-gates/check-receipt.py`, which the `receipt sync` leg runs on gov's tree,
  reads a source-mode receipt's unhashed rows as a named `SKIP`, as it reads no receipt today
  (`:429-433`). Otherwise it would grade each unhashed engine row for existence only
  (`check_engine_rows`), so a branch that stops shipping a file would red until the next landing
  rewrites the rows. A row in a source-mode receipt that does carry a `sha256` is graded as any row
  is, so the mode silences no hash it records. Observed by AC7.
- **S7** — The comment in `tools/memory-tree/check-verdict-epoch.sh` that says "gov has no
  receipt" (`:407`) is rewritten to say that gov's receipt records no `oid`, so its verdict still
  never takes the vendored path. That is true, because a row with no `oid` fails the vendored test
  at `:424-426`. Observed by AC7.

## 3. Non-goals (OUT)

- Grading a source-mode receipt in `govkit check`, and `apply` or `adopt` on gov's own tree. Both
  refusals stay (`:7528`, `:12647`).
- Planning gov's selection into a fresh target with gov's answers. There, `playbook_path` is an
  adopter's own answer, and planning still refuses without it. Gov's `deploy.toml` is the owner's
  file under dGroundRules' minimal guard (`cl-dClosedLoop-0012`).
- Running a gov-first walk in a unit pass, or committing gov's receipt from a branch. Only a
  landing writes it (§4 "### Rollout").
- The walk, the lock reclaim, the receipt's schema and the isolated runner. They are
  TOOL-dSafePassage-2's, -3's and -7's.
- The floor step's own record in remote CI. TOOL-dSafePassage-12 observes it.
- A help page. §5 user docs says why.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — `read_steps` and `read_retired`, the one reader of the declared step rows and the registry's succession rows; without it the source branch of `derive_pending_steps` and `check_gov_first` have no declared set
- **consumes-from** `TOOL-dSafePassage-2` — `run_step_walk`, `derive_pending_steps`, the walk's `witness does not hold after up` stop and its lock reclaim; without them S1 has nothing to run
- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, the one writer of the receipt's `steps` rows `{id, introduced, state}` at schema 4; without it the source receipt has no writer and no field
- **consumes-from** `TOOL-dSafePassage-7` — `run_step_isolated`, under which the walk and the witness re-runs of `check_gov_first` go; without it a witness runs on the lander's ambient environment
- **consumes-from** `TOOL-dSafePassage-11` — `lib/python-floor-3.15`, the second declared step, whose application to gov is the first the floor makes; without it AC5's receipt lists one step fewer than this landing declares
- **hands-off** `TOOL-dSafePassage-12` — gov's receipt in the prepared merge, holding `lib/python-floor-3.15` as `applied`, which its AC7 reads
- **hands-off** `TOOL-dSafePassage-10` — gov's source-mode receipt at `.governance/install.json`, whose `files` rows, one per planned destination, are the step gate's `file` class
- **consumes-from** external — dGroundRules' minimal guard (`cl-dClosedLoop-0012`), which never fires at a landing (`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:105-107`), so no step a landing declares may write gov's policy file at the walk: TOOL-dSafePassage-1's fan-out step writes nothing on gov, which tracks no `.agent-cap.conf`, and the size-limits step, whose up writes that file, is declared only by TOOL-dSafePassage-61, whose pass migrates gov under the guard in the commit that declares the row, so the walk finds its witness holding; without that rule a landing commits a write the guard refuses
- **consumes-from** `TOOL-dSafePassage-20` — the writer taking the reader's unlanded value as null; without it every step this landing introduces refuses at its record
- **hands-off** `TOOL-dSafePassage-21` — the derivation of gov's planned destinations, shared by the source receipt's rows and the step gate's file class, the repair of finding 5
- **hands-off** `TOOL-dSafePassage-25` — the refused landing removing the untracked files its walk made, the repair of finding 54
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### The flow at a landing

`cmd_prepare` merges the branch onto the advertised tip `R` and mints into the working tree. It
then calls `run_gov_first`, which runs `update --target "$top" --write` on the merged tree. In
source mode that update:

1. takes the write lock (`demand_writable_target`);
2. reads or creates the source receipt, and rewrites its `files` from the plan S3 accepts;
3. reads the declared steps from the merged tree's descriptors and `tools/govkit/steps.toml`
   through TOOL-dSafePassage-1's reader;
4. runs `run_step_walk` over the source branch of `derive_pending_steps`, each step under
   `run_step_isolated`;
5. writes each step's row through `set_step_state`;
6. runs `check_gov_first`;
7. releases the lock.

`run_regen` follows. The `git add -A` and `commit-tree` at `:919-921` fold the receipt into the
merge with the mint and the regeneration. A refusal anywhere resets to the merge and checks the
branch out unmoved (`:903-906`).

### Why a source receipt has no vintage commit

The prepared merge is rewritten after the walk, and a receipt inside a commit cannot name that
commit. A vintage at the first parent would be reachable but would not hold this landing's steps.
So the source receipt's vintage is its `steps` list itself. A step is pending when `steps` does
not hold it as `applied`, and a re-walk skips each step whose witness holds anyway
(TOOL-dSafePassage-2). §8 F2 records the choice.

### Data model

```json
{"schema": 4, "mode": "source", "gov_source": ".", "prefix": "tools",
 "kits": ["playbook", "..."],
 "files": [{"path": "tools/memory-tree/gen_build_index.py", "kit": "memory-tree",
            "role": "engine", "source": "tools/memory-tree/gen_build_index.py"}, "..."],
 "steps": [{"id": "govkit/receipt-schema-4", "introduced": "<sha>", "state": "applied"},
           {"id": "lib/python-floor-3.15", "introduced": "<sha>", "state": "applied"}]}
```

`kits` is copied from `.governance/deploy.toml`'s `kits`, so gov's own selection is recorded. A
`files` row carries no `sha256`, `oid`, `gov_oid` or `commit`, because nothing was installed: the
bytes at `path` are gov's own, graded by gov's own gates.
`introduced` is the row's own value. A `failed` row adds `"failure"` (the brief's S4).

### Readers of gov's receipt

Readers of gov's receipt, read at the base. Gov has no receipt today, so each reader was checked
for what a source receipt with unhashed rows at gov's own paths changes:

| Reader | What it reads | A source receipt |
|---|---|---|
| `tools/run-gates/check-receipt.py:429-444` | engine rows, each graded for existence and, with a `sha256`, for its bytes | a named `SKIP` (S6) |
| `.githooks/pre-push:1176-1177` | presence: the receipt must be tracked at the pushed sha | passes, because the lander commits it |
| `tools/memory-tree/check-verdict-epoch.sh:413-426` | each scanned file's row `oid` at HEAD | no row has an `oid`, so every file fails the vendored test, as with no receipt |
| the `resolve_kit_dir` copies, `resolve_kit_dir.py:1-30` and its inline copies | a row whose `source` ends in the anchor and whose `path` exists | the row's directory, which is gov's own kit directory, the one its probe finds today |
| `.githooks/pre-commit:155-165`, `tools/check-wiring.sh:346-356` | the row for a kit file | gov's own path for it, the one the probe finds |
| `tools/check-wiring.sh:230` | whether any row is `adopter-owned` | none is |
| `tools/lib/render-doc.sh:183-185` | rendered rows and `prefix` | gov's own rendered paths, and `prefix` `tools` |

Each row answers what the probe answers today, because gov's planned destinations are gov's real
paths. AC9 observes two of these readers unchanged, and the table is the inventory of the rest.

### Inventory

Minted:

- `test_source_target` in `govkit.py`;
- `check_gov_first` in `tools/govkit/upgrade_steps.py`, beside the functions TOOL-dSafePassage-1,
  -2, -4 and -7 put there (the brief's S3), and a source-mode branch in TOOL-dSafePassage-2's
  `derive_pending_steps`, extended rather than copied;
- `run_gov_first` in `tools/push-main.sh`;
- the receipt envelope key `mode` with its one value `source`;
- the commit subject prefix `steps: gov first onto`.

Naming cells: `tools/lexicon/lexicon.py --suggest <name> --as py.function` printed OK for the
two new Python functions on 2026-10-23, and `--as sh.function` printed OK for `run_gov_first`.
No conf key, policy key or gate leg is minted.

### Migration

Additive. The first landing after this unit creates gov's receipt in its prepared merge, with
every step declared at that tip walked. Each step whose witness already holds on gov is skipped
and listed `applied`, as TOOL-dSafePassage-2's walk lists a skipped step.

### Rollout

The change is live at the first landing after the build. Units 1, 3 and 11 declare the first rows,
and gov meets them in that landing before the push. The lander runs from the run's worktree in the
unattended path, so the walk writes that worktree's tree, which is the prepared merge. No unit pass
runs `run_gov_first`. The pass observes it in a scratch fixture, so the branch never carries a
receipt that the landing's own walk would also write.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/run-gates/check-receipt.py`
- `tools/memory-tree/check-verdict-epoch.sh`

`.governance/install.json` is written by the lander at the close, never by this unit's pass.

### Alternatives rejected

- **Source mode grades gov's own file rows.** The grid would grade each row against itself. This
  lets the lander write gov's tracked files through the row engine in every landing, a write
  surface nothing priced (veto 3). Its only yield is rows equal to their own sources (§8 F1).
- **A source receipt with no file rows.** TOOL-dSafePassage-10's `file` class reads gov's rows,
  and the step gate refuses green on an empty population (`cl-dClosedLoop-0027`), so no rows fails
  that clause (§8 F1).
- **Widening the prose class to admit gov's answers.** `;`, `<`, `>` and a backtick are shell
  metacharacters, and the class exists to refuse them (`:1254-1270`). Narrowing which answers are
  graded refuses every value that still reaches a substitution.
- **Adding `playbook_path` to gov's `deploy.toml`.** That is an agent write to a file the parent's
  minimal guard reserves for the owner (`cl-dClosedLoop-0012`).
- **The source receipt's vintage at the merge's first parent.** It is reachable, but it does not
  hold the steps this landing introduces (§8 F2).

## 5. Production-readiness checklist

- security: the answers guard still grades every value that can reach an argv, a destination or a
  pattern of the entry, because the token set is read from that entry's own descriptor.
  `test_source_target` compares resolved paths. An adopter cannot reach source mode: it needs the
  target to be the gov checkout running the verb. The witness re-run goes under the isolated
  runner.
- perf / scale: one `update` per landing. Steps whose witness holds cost one witness run each,
  measured by AC5's fixture. Nothing runs at an adopter's landing.
- error / empty / loading states: no deployer is one line and exit 0. A deployer with no Python
  refuses. A walk failure, a declared id missing from `steps` and a witness failing on gov's tree
  each refuse the landing by name, with the branch unmoved. The unhashed rows of a source receipt
  are a named `SKIP` in `receipt sync`.
- observability: the lander prints each step walked and its outcome. The attended path's commit
  subject names the landing, and the receipt names each step's state.
- risks: the guard never sees a landing, since the lander commits through `commit-tree`
  (`tools/push-main.sh:921`) and `--no-verify` (`:1092`). The steps this build declares write
  nothing guarded there: gov tracks no `.agent-cap.conf`, whose absence is the fan-out step's
  witness, and TOOL-dSafePassage-61's pass migrates gov's policy file under the guard in the commit
  that declares the size-limits step (§3 Edges). A step
  whose up writes outside the receipt writes those files into the merge, and they land with it.
  That is the point of gov first, and it is named in the lander's output.
- testing: the probes of §6, and the arms in `tools/push-main.test.sh` and `tools/govkit/selftest.py`
  (§7).
- migration: §4 "### Migration".
- user docs: N/A for `help/`. The only operator of this path is gov's own landing, the adopter's
  lander prints one line and changes nothing, and no `help/` page covers the lander.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py plan --target .` runs in gov's tree, it exits 0 and
  writes nothing.
  Red when: `target_context` grades an answer no template of the entry names, which is the base's
  exit 2 on `answers.stream_ownership`, or the playbook seed row still refuses on `playbook_path`.
  figure: the base's exit 2 is PINNED, measured on 2026-10-23 at `a255d0de`.
- **AC2** — When `python tools/govkit/govkit.py plan --target <scratch target>` runs with a deploy
  file whose `[answers]` sets `memory_root` to `x; touch PWNED`, it exits 2 naming
  `answers.memory_root`. With `stream_ownership` set to `a; b`, it exits as it does without that
  key.
  Red when: the narrowing skips a value some template interpolates, or still grades one none does.
  fixture: a scratch target under `%TEMP%` with a copy of gov's deploy file.
- **AC3** — When `python tools/govkit/govkit.py update --target . --write` runs in a scratch clone
  of gov with no receipt, it exits 0 and writes the receipt with `"mode": "source"` and schema 4.
  A probe comparing its `steps` ids with the declared ids prints no difference either way. Its
  `files` paths equal the destinations `python tools/govkit/govkit.py plan --target .` lists, and
  no row carries `sha256`, `oid` or `gov_oid`. `git status --porcelain` names no path under
  `.governance/outbox/`.
  Red when: the gov checkout is refused as the target (`tools/govkit/govkit.py:9168`), a declared
  id is missing, `files` is empty, or the lock file is left behind.
  fixture: a scratch clone under `%TEMP%`, after TOOL-dSafePassage-1, -2, -3 and -7 are built.
- **AC4** — When AC3's command runs with a planted row in the clone's steps file, whose `up` exits
  0 and whose `witness` exits 1, it exits 1. It names the planted id with the walk's
  `witness does not hold after up`, and every row before the plant stays `applied`. Separately,
  with the clean receipt of AC3 holding an `applied` row whose witness is then planted to exit 1,
  it exits 1 and `check_gov_first` names that id as not holding on gov's tree.
  Red when: the landing check trusts the recorded state without re-running each witness.
- **AC5** — When `bash tools/push-main.sh --prepare --slug fx` runs in a fixture, it reads as
  follows. The fixture is a scratch clone, its bare remote and a run branch, with AC4's plant on
  the branch. The command exits 1, names the planted id, and leaves the branch at its old sha.
  Without the plant it exits 0, and the prepared merge's tree holds the receipt, every declared id
  `applied`.
  Red when: the lander does not call `run_gov_first`, or calls it after the merge is rewritten, so
  that the receipt is not in the merge.
  fixture: a scratch clone and a bare remote under `%TEMP%`.
- **AC6** — When the same `--prepare` runs in a fixture where no govkit deployer resolves beside
  the lander, it prints `steps were NOT run on gov first` once, with its reason, and exits 0. With
  the deployer present and the resolver refusing, it exits 1.
  Red when: an adopter's landing changes, or gov's landing proceeds with no Python.
- **AC7** — When `python tools/run-gates/check-receipt.py <scratch tree>` runs on a tree whose
  receipt is the one AC3 wrote, with one of its rows' files deleted, it prints a `SKIP` line naming
  source mode and exits 0. With a `sha256` added to that row, it exits 1 naming the file.
  Separately, `git grep -n 'gov has no receipt' -- tools/memory-tree/check-verdict-epoch.sh`
  prints nothing.
  Red when: an unhashed row of a source receipt reds a branch, or the mode skips a hash it records.
- **AC9** — When `bash tools/check-wiring.sh` and `bash tools/check-install-prefix.sh` run in the
  scratch clone of AC3 with its receipt, and again with the receipt removed, each prints the same
  lines and exits the same way.
  Red when: a row of the source receipt sends a row reader to a path its probe would not choose.
- **AC8** — When AC3's command runs a second time on the same clone, the receipt's bytes are
  unchanged and no step's up runs.
  Red when: a source walk re-runs an `applied` step, or rewrites the receipt with no change.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `push-main self-test` · `receipt sync (installed files match the receipt)` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/push-main.test.sh · covers AC5 AC6 · a fixture landing whose branch carries a step row with a failing witness, and one with no deployer beside the lander · none
New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC8 AC9 · gov's own deploy file planned in place, a planted metacharacter in an interpolated answer, and a planted step row with a failing witness on a source-mode clone · none
New arm: tools/run-gates/check-receipt.py · covers AC7 · its in-file fixtures gain a source-mode receipt whose unhashed row's file is absent, and the same row with a `sha256` · none

What these arms do not check: that the minimal guard admits TOOL-dSafePassage-61's write of gov's
policy file, which that unit's pass meets; that no step writes a guarded path
at a landing, where no guard fires; and the attended landing's own commit, which AC5's prepared path
stands in for.

## 8. Open questions

- **F1 — What does "`update` run on gov's own tree as an adopter runs it" run?** Options: (a) a
  source receipt recording every planned row, with the row grid grading and writing each against
  itself; (b) the same verb, preconditions, walk and stamp over a receipt recording no file row;
  (c) the same verb, preconditions, walk and stamp, over a receipt whose file rows are recorded
  from the accepted plan and never graded. (a) makes the lander write gov's tracked files through
  the row engine in every landing, a write surface beyond this unit's pricing (veto 3). (b) leaves
  the `file` class of TOOL-dSafePassage-10 empty, and the step gate refuses green on an empty
  population (`cl-dClosedLoop-0027`, veto 1). The design record answers the rest: "The lander runs
  each step that a landing introduces on gov's own tree", and "Gov's source-mode receipt (DI-1)
  records the steps" (the supersession research, `research-supersession.md:117`). RESOLVED (agent,
  2026-10-23, delegated): (c), rung 1, which keeps the verb an adopter runs and gives the step gate
  gov's rows. widens: none · relaxes: none
- **F2 — What is a source receipt's vintage, given the merge is rewritten after the walk?**
  Options: the merge itself, which the rewrite drops; the merge's first parent, which is reachable
  but does not hold this landing's steps; the `steps` list, with a step pending until it is listed
  `applied`. RESOLVED (agent, 2026-10-23, delegated): the `steps` list, since it is the only option
  that names every applied step and survives the rewrite. TOOL-dSafePassage-2's witness skip keeps
  a re-walk idempotent. Rung 3. widens: none · relaxes: none
- **F3 — How is gov's deploy plan accepted?** Options: (a) widen the prose class, which admits
  shell metacharacters (veto 3); (b) the owner adds `playbook_path` and rewrites gov's answers,
  which is an owner turn on a guarded file, and `commit_trailer` cannot lose its `<` and `>`;
  (c) grade only the answers an entry's descriptor names, and in source mode resolve an unanswered
  destination to its source path. RESOLVED (agent, 2026-10-23, delegated): (c). Every value that
  reaches a substitution is still graded by its class, so no surface widens. Rung 3.
  widens: none · relaxes: none
- **F4 — Which sibling functions does this unit call, given their specs were written beside it?**
  RESOLVED (agent, 2026-10-23, delegated): the names each owner's Inventory mints, read before this
  draft closed: `read_steps` and `read_retired` (TOOL-dSafePassage-1), `run_step_walk` and
  `derive_pending_steps` (TOOL-dSafePassage-2), `set_step_state` (TOOL-dSafePassage-3) and
  `run_step_isolated` (TOOL-dSafePassage-7). The M2 cross-read amends this spec if one moves. The
  build run re-grounds against the landed dGroundRules first, before its first pass, for
  `cl-dClosedLoop-0012`'s guard. Rung 1, from the brief's S3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-20`, `TOOL-dSafePassage-21`, `TOOL-dSafePassage-25`, `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-24 · §3 Edges' external line, §5 risks and the note under §7 · the guard never fires at a landing, so it binds TOOL-dSafePassage-1's unit-pass commit and the landing's walk finds that step's witness holding, re-grounded by `2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md` row 27; no other section moved.
- rev-4 · 2026-10-26 · §3 Edges' external line · §5 risks · §7 · the size-limits step and gov's
  migration moved from TOOL-dSafePassage-1 to TOOL-dSafePassage-61 at that unit's §8 F8 stop, so the
  guard binds TOOL-dSafePassage-61's pass and no landing walk writes gov's policy file, by
  `2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md`; no other section moved.

## 10. Reuse audit

The seams extended are the lander's landing-time stages, `run_minter` (`tools/push-main.sh:802-822`)
and `run_regen` (`tools/push-main.sh:757-775`), and their two call sites (`:902-911`, `:1084-1112`).
`run_gov_first` copies their deployer resolution and exit shape. The other seams are `update`'s
precondition order (`tools/govkit/govkit.py:9225-9232`) and `target_context`'s answer loop
(`tools/govkit/govkit.py:1488-1499`). `reuse_lookup.py "run a deployer verb on gov's own tree inside
the lander's prepared merge"` ranked `tree`, `run`, `merge` and `run_arms`, which are name-token
neighbours, and none is a lander stage. The map ranks no function of `tools/push-main.sh` for that
phrase, while the source holds two exact precedents, so the hits disagree with source there.
`gotchas.py --for-paths` over this set selected `verdict-printed-before-the-step-that-reverts-it`,
which the flow answers by printing the walk's outcome before the rewrite only on success. It also
selected `foreign-code-runs-on-the-ambient-credential`, answered by the isolated runner. The recall
probe found the shape audit's M1 (`2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-b.md:196`) and
the owner's SA-3, "In dSafePassage (Recommended)", which put gov first here.

Recall terms used: `python tools/memory-recall/query.py "how does gov run each upgrade step on its own tree first at the lander's prepared merge" --terms "gov first source-mode receipt lander prepare mint regen steps update self target deploy plan refusal"`
