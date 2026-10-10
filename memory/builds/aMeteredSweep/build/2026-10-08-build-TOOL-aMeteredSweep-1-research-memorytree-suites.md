# Appendix — Memory-tree family self-test legs: where the time goes and how to cut it

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-08, kept verbatim below its first heading. It ran no suite: every saving is an ESTIMATE from static spawn counts against the profiled bar in `2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, and the synthesis that ranks across all five is `2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`. Line citations are against `fa68a767` plus this unit's fixes.


Read-only research, node `a`, 2026-10-08, tree at `9289116b` plus this worktree's uncommitted edits.
No leg, suite or `--selftest` mode was run. Every cost figure comes from three sources:

- **pool**: `research-input-legs.md`, the contended `GATE_FULL=1 GATE_SELFTESTS=1` bar at `fa68a767`.
- **quiet ref**: the minimum non-failing reading of the leg in `gate-ledger.tsv`, read from the
  primary `.git` and nine worktree git dirs. The reading count is `n`. These are the closest thing
  on record to a quiet reading. The median is given where it differs a lot.
- **spawn model**: per-spawn costs already recorded on node `a`. A git spawn is 0.3-0.75 s, a python
  startup is 0.29-0.77 s, and a small coreutil is 0.03-0.3 s (`aQuenchedHarness` README,
  `aRatifiedRulings-3` §4, the auto-memory note on git spawns). Under the pool these are 3-5x higher.

Spawn counts come from **static call sites multiplied by loop counts**, not from traces. Treat every
"seconds saved" figure as an estimate within a factor of 2. The deterministic claim to write down
after a change is the spawn count or the checker-invocation count, per
`memory/gotchas/process-creation-is-the-suite-cost.md`.

## Ranked levers

The pool column is what the full bar would see. The quiet column is what a standalone run would see.
Estimates do not simply add up within one leg: where two levers overlap, the second one's figure
assumes the first has not landed.

| # | leg | lever | est. saved, quiet / pool | effort | risk |
|---|---|---|---|---|---|
| 1 | manifest-check self-test | Arms that are not about `CARD_CLAIMS_BOUND` export a generous bound. The 15 s product default is what produced 9 of the 11 reds | turns a **red** leg green, which avoids a retry or a re-run of a 3252 s leg | XS | none: AC5 still grades the bound |
| 2 | drift-audit selftest | Arms that read one signal stop running the whole report: an in-process call per signal through the suite's own `_build_run_ctx`, or a `--signal NAME` flag | ~100 s / ~1200 s | M | M |
| 3 | memory-hygiene self-test (+ transition-audit) | A `--only N[,M]` selector in `check-memory-hygiene.sh`. It must print a mandatory liveness line naming the checks that ran. Single-check arms use it | ~270 s / ~1500 s, plus 30-60 s quiet in transition-audit | L | M |
| 4 | memory-hygiene self-test, corpus-ids, gotchas, memory hygiene, transition-audit | Stop the delegates re-entering the checker. The checker passes `APPEND_ONLY_ERE`, `INDEX_SET` and `GOV_BASH=$BASH` by env. `ask_shell` uses them, and `resolve_bash` is memoised | ~190 s / ~600 s in total across the five | S-M | L |
| 5 | manifest-check self-test | `unset AI_AGENT` at the top of the suite (the cli block already sets and restores its own). Every card write today runs the real `claude --version` | 55-165 s / 200-500 s | XS | L |
| 6 | memory-recall kit selftest | The nested adopter-layout run executes a derived layout-sensitive subset, not the whole suite again | ~35 s / ~300 s | S | M (owner call) |
| 7 | row-keyed merge driver replay | Direct driver calls use `"$PY"` instead of `bash pyrun.sh`, and the per-case oracle becomes one awk instead of about 12 small spawns | 40-100 s / 150-300 s | S-M | L |
| 8 | memory-hygiene self-test (+ memory hygiene leg) | Fuse the 9 python delegate calls into one interpreter, started once, optionally in the background | 180-450 s quiet if lever 3 has not landed, ~30% of that after it | L | M |
| 9 | transition-audit arms | Merge each `audit`+`audit_rc` pair into one run. Clone each fixture from a committed seed repo instead of `cp -r` + init + 5 config + re-hashing 3.1 MB | 30-75 s / 100-180 s | S | L |
| 10 | build-index, corpus-ids, gotchas, row-grammar, check-arms, backlog migration, drift-audit | Set fixture git config once through `GIT_CONFIG_COUNT`/`KEY_n`/`VALUE_n`, and read HEAD from the ref file instead of `git rev-parse HEAD` | each leg 10-30% of its spawns; 20-70 s per leg in the pool | XS each | L (but see the kit-bump caveat) |
| 11 | manifest-check self-test | Sparse clone and worktrees for the card fixture: today it does 3 full checkouts of 3633 files | 30-80 s / 100-250 s | M | M |
| 12 | corpus-ids, gotchas | Memoise `ask_shell` by (flag, conf bytes, checker bytes) within one process | 25 s / 250 s, plus 4 s / 70 s | S | L-M |
| 13 | memory-hygiene self-test | Replace the per-key `grep` loops (`check-memory-hygiene.test.sh:2465-2560`) with one awk join | 10-30 s / 30-100 s | XS | L |
| 14 | manifest-check, row-grammar | Wall-clock arms become causal assertions (flake list below) | 0 s, removes reds on a loaded host | XS | none |

**Kit-bump caveat for levers 3, 4, 8, 10 and 12.** `tools/memory-tree/check-verdict-epoch.sh:180` puts
these files in the verdict-epoch scan set:

- `check-memory-hygiene.sh`
- `tree_lib.py`, `row_grammar.py`, `gen_build_index.py`, `corpus_ids.py`, `gotchas.py`, `merge-rows.py`
- memory-recall's `extract.py`

The `--selftest` code of four of the legs here lives inside those modules. So even a selftest-only edit
to them moves behaviour-bearing lines and owes the five-carrier kit bump. Batch every edit to the
scan set into one change with one bump. `migrate_backlog.py`, `check-arms.py` and
`transition_audit.py` are outside the set.

## Wall-clock-timed arms (flake risk on a loaded host)

- `skills/session-kickoff/manifest-check.test.sh:1441-1446` (AGH2 AC5) asserts that a card write
  with `CARD_CLAIMS_BOUND=2` returns in **under 10 s**. It was observed red at 24 s in this bar. A
  loaded card write legitimately takes longer than 10 s even with the claims read killed:
  - the real `claude --version` up to `CARD_CLI_BOUND=5`;
  - `--overlaps` bounded at 1 s;
  - `git status` over 3633 files.

  The property the arm wants is "did not wait for the sleeper". Assert under the sleeper's own
  duration instead: it sleeps 30 s; raise it to 120 s and assert under 120 s. Alternatively assert
  against `cl_ms_off` plus the bound plus a margin.
- `manifest-check.test.sh:834` (S4) runs `timeout 10 bash "$CHECK" --card --path`. A loaded host
  can exceed 10 s with no defect. The arm only needs "it returned rather than blocking forever", so
  120 s keeps that discrimination.
- `manifest-check.test.sh:1376-1446`, the whole claims block. Every arm except AC5 writes a card
  under the shipped default `CARD_CLAIMS_BOUND=15` (`manifest-check.sh:140`). That bounds the
  **real** unattended driver's `--claims`, which took 66 s before this session's fix and 18 s after.
  On a loaded host the cell reads `claims — skipped: --claims did not answer within 15s`.

  That is exactly AC1, AC2, AC6, AC10, AC4, AC11 (two arms) and AC14 in the log, plus the
  executed-count floor red (245 against 248) that follows from it. Lever 1 fixes it. The bound's
  semantics stay graded by AC5 and AC12.
- `manifest-check.sh:136` `CARD_CLI_BOUND=5` with an inherited `AI_AGENT`. Every card write in the
  suite races the real `claude --version` against 5 s, so the `cli —` cell flips between a version
  line and `skipped` with load. No arm outside the cli block reads that cell, and AC1 compares stdout
  to the bytes of the same run, so today it is a cost, not a red. Lever 5 removes both.
- `manifest-check.test.sh:1376` `CARD_OVERLAP_BOUND=1` inside the claims block. The `overlaps —`
  cell becomes load-dependent. No claims arm reads it, so this is low risk; note it if anyone adds a
  whole-card byte compare there.
- `tools/memory-tree/row_grammar.py:1901` puts `timeout=60` on the `--print-rotated-archive-ere`
  probe. Past 60 s the cross-reader join arm turns into an **announced SKIP**. That is a silent
  coverage loss on a loaded host, not a red.
- `tools/memory-tree/gen_build_index.py:5466` runs `run_probe(..., sleep(30), 1)`. It is **not** a
  flake: whether the child starts or not, the 1 s bound kills it and the arm wants "never answered".
- No sleep and no elapsed-time assertion was found in:
  - `check-memory-hygiene.test.sh`, `merge-rows.test.sh`, `transition-audit.test.sh`;
  - the `--selftest` code of `corpus_ids.py`, `gotchas.py`, `migrate_backlog.py` and `check-arms.py`;
  - `memory-recall/selftest.py` and `drift-audit/selftest.py`.

---

## memory-hygiene self-test

`bash tools/memory-tree/check-memory-hygiene.test.sh`. Ceiling 4800.

- **(a) What it guarantees:** every check of the hygiene engine fires on a staged violation and
  stays silent on its clean twin. It covers 551 assertions across conf keys, scratch trees, the
  project-key arms and the engine-routed checks 24, 27 and 28.
- **(b) Measured cost:** pool 4801 s (timeout). The serial retry took 1442 s. Quiet ref 620 s
  (`n=3`, median 1439). The `aRatifiedRulings-3` traced quiet run was 598.7 s with 66 checker runs.
  That unit's loaded after-run was 775.7 s with 59.
- **(c) Where the time goes:**
  - **Checker invocations dominate.** Today's file holds the call sites below (statically, loops
    expanded). That totals **about 97 runs of a 2916-line engine, of which about 20 are cheap conf
    aborts** (rc 2 before python resolves, about 0.1 s).
    - 49 direct sites (`bash "$SCRIPT"` or `"$HERE/check-memory-hygiene.sh"`); the `for _bad` loop
      at `:2438` multiplies one of them by 7.
    - `run_pk_gate` 19 sites (`:2806`), plus loops at `:2829`, `:2843`, `:2853`, `:2869` and `:2876`
      (6 extra runs).
    - `bm_run` / `bmpair` / `bmbad` (`:3334`, `:3411`, `:3422`): 7.
    - `run_rel27_gate` 4, `run_cont28_gate` 3, `run_rot24_gate` 2 plus 1 (`:3514`, `:3584`, `:3648`, `:3664`).
    - The check-32 kit copy at `:3017`.
  - **Per-run floor on a small fixture: 8.0 s quiet** (`aRatifiedRulings-3` §4). 4.4 s of that is
    the python delegates, and **`corpus_ids.py --check` alone is 3.2 s**. The checker spawns 10
    python processes per run, listed after this bullet list. One more is the `resolve_python` probe
    at `check-memory-hygiene.sh:432`, which runs `python3 -c "import sys"` every invocation.
  - **The delegates re-enter the checker.** This applies to:
    - `corpus_ids.walk` (`corpus_ids.py:505`) via `ask_shell("--print-append-only-ere")`;
    - `check_read_path` (`:769`) via `ask_shell("--print-index-set")`;
    - `gotchas.append_only_re` (`gotchas.py:154`).

    Each `ask_shell` first calls `resolve_bash()` (`corpus_ids.py:387`). That walks `PATH` and
    **runs** a `bash -c :` per candidate, with no memo. `--print-index-set` returns at
    `check-memory-hygiene.sh:812`, which is **after checks 1-5 and after the python probe**. So
    every full checker run executes checks 1-5 twice and probes python twice.
  - **Main-tree conf re-runs** (`:1555-1840`): 15 full runs over one tree. Each grades one check:
    - `out2`, `out3`, `out3r`, `out3j` and `out3f` grade check 12 (plus check 11 for one negative);
    - `out6a-d` grade check 23;
    - `outl` and `outu` grade check 5.

    In §4 these were 15 runs at 6.2-18.5 s, 33% of the suite.
  - **Scratch trees** (`:1481-2176` region in §4, now further down): 28 runs, 7 of them aborts. 27%.
    Each tree is a fresh `git init` plus 2 `git config` plus `add` plus `commit`. The suite holds 24
    `git init`, 24 `git config` and 46 `git add` sites.
  - **Per-key grep loops** at `:2468`, `:2510`, `:2515` and `:2554-2560` (`_engkeys`, `_engreads`,
    `_engexempt` and `_pyparity` over 30 python keys): about 100 grep spawns.

  The 10 python processes per checker run:

  | module | flags | site |
  |---|---|---|
  | `gen_build_index.py` | `--check`, `--print-bindings` | `:1077`, `:1155` |
  | `row_grammar.py` | `--check-rotation`, `--check`, `--check-relations`, `--check-content` (4 interpreters, 4 corpus parses) | `:1373`, `:2527`, `:2544`, `:2558` |
  | `transition_audit.py` | (none) | `:1404` |
  | `corpus_ids.py` | `--check` | `:2496` |
  | `gotchas.py` | `--check` | `:2513` |

- **(d) Levers, ranked:**
  1. **`--only` selector** (lever 3, the charter §7 "run the ONE question an arm asks").
     - **Mechanism:** an env or flag such as `HYGIENE_ONLY="12 11"` wraps each `# N —` block in a
       membership test. The checker always prints `HYGIENE ran checks: <list>`, and every
       `--only` arm asserts that line. Without it, a negative assertion (`cnot`, "check 11 ran
       with a blank TOMBSTONE_ROOTS") passes vacuously, which is §7's "a skip must announce itself".
     - **Who uses it:** the 15 main-tree re-runs, most scratch-tree arms, the 7 project-key runs
       that proceed, and the bm arms. The rel27, cont28 and rot24 arms assert "**and no other
       check**", so they keep a full run.
     - **Estimate:** about 45 of about 75 full runs drop from about 8 s to about 1.5-2 s (prologue,
       `git ls-files`, conf, the PRE_* counts, one check). That is about 270 s quiet.
     - **Dependencies to audit:** check 6 computes `INDEX_SET`, which the print mode and corpus_ids
       consume. Checks 1-5 must stay a prefix for `--print-index-set`. Check 23 reads staged state.
  2. **Re-entry removal** (lever 4). Just before the delegates, export
     `HYGIENE_APPEND_ONLY_ERE="$APPEND_ONLY_ERE"`, `HYGIENE_INDEX_SET="$INDEX_SET"` and
     `GOV_BASH="$BASH"`. `ask_shell` returns the env value when it is set, and `resolve_bash`
     gains `functools.lru_cache`. Keep ONE arm that compares the env value to the print mode's
     answer, so the shell stays the owner and the pair is gated rather than trusted.
     - **Saved per full run:** 3 bash probes, 3 bash re-entries (one of them re-running checks 1-5
       plus a python probe), about 40-60 spawns. That is roughly 2-2.5 s of the 3.2 s `corpus_ids`
       figure plus the `gotchas` re-entry.
     - **Estimate:** × about 75 runs ≈ 150-190 s quiet. The lever also reaches every other suite
       that runs the engine.
  3. **Fused delegate bundle** (lever 8). One `hygiene_delegates.py` imports the modules and runs
     checks 9, 21, 24, 26, 13-16, 17-19, 20, 27 and 28 in one interpreter, printing per-check
     sections the shell splits. It starts after line 812 and can run in the background while the
     shell checks run.
     - **Saving:** about 8 python startups per run (2.4-6 s quiet), plus 3 duplicate corpus parses
       in `row_grammar`.
     - **Overlap with lever 1:** if `--only` lands first, only the about 30 remaining full runs
       benefit.
     - **Risk:** output order and rc mapping must stay byte-identical, and `hygiene-parity.test.sh`
       re-baselines.
  4. **Fixture git config through the environment** (lever 10). Set `GIT_CONFIG_COUNT=2`,
     `GIT_CONFIG_KEY_0=user.email` and so on once at the suite top, and delete the per-tree
     `git config` lines. About 50 spawns, 15-35 s quiet.
  5. **Per-key loops to one awk** (lever 13): 10-30 s quiet.
- **(e) Full rebuild:** **not warranted**.
  - The 2026-09-07 portability survey rated this suite unportable to the bash harness: 14 readable
    lines against 289 assertions, and 56 want-absent assertions.
  - Batching conf variants into one run was refuted in `aRatifiedRulings-3` §4, candidate A,
    because rc 0 over several keys names none of them on failure.
  - The two engine levers (selector plus re-entry removal) keep every arm, every staged break and
    one run per arm. Together they project about 620 s to about 200-250 s quiet.
  - **Cost:** about 2-3 sessions, including the five-carrier bump, the `hygiene-parity` re-baseline
    and `FLOOR_ASSERTIONS` re-measurement. Each new selector arm needs its RED observed.

## manifest-check self-test

`bash skills/session-kickoff/manifest-check.test.sh`. Ceiling 4370.

- **(a) What it guarantees:** the kickoff manifest ratchet and the orientation card. The card's
  verbs (write, replay, check, append and path) and its cells (tree, drift, overlaps, cli, live,
  claims and health) are graded against fixtures, along with the no-raw-`fatal:` contract on every
  path.
- **(b) Measured cost:** pool 3252 s, **failed**, 11 reds. Quiet ref 453 s (`n=4`, median 620,
  maximum 2162).
- **(c) Where the time goes:**
  - **About 150 checker runs:** 59 `run`, 53 `run_card` and 38 direct `bash "$CHECK"` lines. The
    checker has 98 `$(` sites and 33 git call sites.
  - **Card fixture** (`:697-708`): a `git clone --local` of the whole repo plus **two `worktree
    add`s, three full checkouts of 3633 files**. Every card write then runs `git status
    --porcelain` (`manifest-check.sh:397`) and `git worktree list` over a full tree.
  - **Every card write runs the real `claude --version`** (`manifest-check.sh:314`, a node startup,
    bounded at 5 s) whenever `AI_AGENT` is inherited, which it is under a Claude-launched bar.
  - **Claims block** (`:1352-1515`): each card write there runs the **real** unattended driver's
    `--claims`, which took 66 s before this session's `lib-unattended.sh` fix and 18 s after. There
    are about 10 such writes plus a direct driver run at `:1495`.
- **(d) Levers, ranked:**
  1. **Generous `CARD_CLAIMS_BOUND` in the claims block** (lever 1). The 15 s product bound fired
     under load, so 9 of the 11 reds plus the floor red are this. Saves no seconds; removes a red
     and its re-run.
  2. **`unset AI_AGENT`** after the prologue (lever 5). The cli block at `:970-1014` already saves
     and restores it. Estimated at 55+ card writes × 1-3 s (node startup) = 55-165 s quiet.
  3. **Causal wall-clock arms** (lever 14): `:1445` and `:834`, see the flake list.
  4. **Sparse card fixture** (lever 11). `git clone --local --no-checkout`, then `sparse-checkout`
     of the paths a card reads, then checkout. Do the same in both worktrees.
     - **Saving:** about 2 × 3600 fewer file writes, and cheaper `git status` per card.
       30-80 s quiet.
     - **Risk:** `check_card_citations` resolves basenames. Verify that it reads `git ls-files`,
       which sees skip-worktree entries, and not the disk. If it reads the disk, the cited paths
       must be in the cone.
  5. **The driver's `--claims` cost** is still 18 s per claims card. It is the subject, since the
     driver owns the verdict order, so do not stub it here. Cutting more spawns in
     `lib-unattended.sh` is the lever, and it is outside this leg.
- **(e) Full rebuild:** the survey rated it "partial, large" (62 of 62 arms mappable, but every arm
  needs the negative `fatal:` folded into rc, plus 15 structural arms). Levers 1, 2 and 3 are under
  an hour of work and remove the reds. Do those first and re-measure before considering a harness
  port.

## corpus-ids selftest

`python3 tools/memory-tree/corpus_ids.py --selftest`. Ceiling 2690.

- **(a) What it guarantees:** checks 13-16 (orphan ids, dead paths and the read-path rule) fire on
  their fixtures and stay silent on clean ones. Every `continue` in `walk()` is reached by a
  fixture, through a `sys.settrace` line tracer.
- **(b) Measured cost:** pool 558 s. Quiet ref 54 s (`n=4`, median 101).
- **(c) Where the time goes:**
  - **47 `walk()` calls.** Each one runs `git ls-files`, then `resolve_bash` (probe spawns), then a
    bash re-entry into `check-memory-hygiene.sh --print-append-only-ere`. That re-entry is
    `git rev-parse`, `git ls-files`, a `date` and several subshells before line 327, so about 11
    spawns per walk and about 520 in total.
  - **3 `check_read_path` calls:** the `--print-index-set` re-entry runs checks 1-5 plus a python
    probe, about 45 spawns each.
  - **25 `_scratch` calls** (`corpus_ids.py:994`) at 5 git spawns each (init, 2 config, add,
    commit), 125 in total.
  - **The tracer:** `sys.settrace` is global for the whole selftest (`:1088`). Each python call
    pays a trace-hook dispatch, which is minor next to the spawns.
- **(d) Levers:**
  1. **Memoise `ask_shell` and `resolve_bash`** (lever 12). Key by flag, a sha of the conf bytes
     and a sha of the checker bytes. The ERE depends only on `$M` after the conf is sourced, so
     most of the 47 walks share 2-5 keys.
     - **Saving:** about 400 spawns, 25 s quiet and 250 s pool.
     - **Risk:** the abort-conf arms are distinct keys, so they still run. Keep the first call of
       each key real.
  2. **Env pass-through** (lever 4) helps the engine path, not this selftest. The selftest calls
     `walk()` directly.
  3. **Fixture config through the environment** (lever 10): 50 spawns.
- **(e) Full rebuild:** not needed. The survey's own note ("drop redundant scratch commits and
  reuse corpora in-process") is lever 12 plus lever 10.

## row-keyed merge driver replay

`bash tools/memory-tree/merge-rows.test.sh`. Ceiling 2750.

- **(a) What it guarantees:** the row-keyed merge driver is never worse than `git merge-file` on
  identical blobs. Arithmetic LOSS and DUP comparisons against a live control, plus id-set and
  duplicate oracles, audit-line reconciliation, a sabotage harness and real `git merge` replays.
- **(b) Measured cost:** pool 770 s. Quiet ref 112 s (`n=3`, median 158).
- **(c) Where the time goes:**
  - **The driver launcher.** `DRV="bash $LIB_DIR/pyrun.sh .../merge-rows.py"` (`:161`). So every
    direct driver call is bash, plus a `cd`/`dirname` subshell, plus a **`python -c "import sys"`
    probe** (`lib/pyrun.sh`), plus the real python. That is **two python startups per call**.
    There are 27 `$DRV` sites, about 50 executions with loops.
  - **`run()`** (`:263`, 42 cases): about 12 small spawns besides the driver. That is
    `ids` × 2 (grep, sort and tr each), `minus`, `cp`, `git merge-file`, `dups` (4) and the
    `never_worse` sorts.
  - **`audit()`** (`:668`): 6 `sed` field extractions plus awk and grep.
  - **More python:** `keys()` (`:468`) is a python heredoc per call, 12 calls. `sab()` (`:1433`)
    is one python per call, 26 calls.
  - **Real merges:** 30 `git merge` replays, each of which invokes the configured driver through
    `pyrun.sh`.
- **(d) Levers:**
  1. **Direct `$PY` for the direct calls** (lever 7). Resolve once, set
     `DRV="$PY $KIT_REL/${KIT}/merge-rows.py"`, and keep `pyrun.sh` only where git invokes the
     driver, since that is the launcher under test. Saves about 50 × (one python startup plus 2
     spawns), 20-50 s quiet.
  2. **The oracle in one awk per case.** `ids`, `dups`, `minus` and the never-worse multiset
     comparison read the same 3-4 files. Saves about 10 spawns per case × 42, 15-40 s quiet.
  3. **Batch `keys()` into one python process** reading all lines. Do the same for `sab` over its
     mutation list. Saves about 35 python startups, 10-27 s quiet.
- **(e) Full rebuild:** an in-process python harness (cases as data, the control as one
  `git merge-file` per case) would cut it to about one python process plus about 90 git spawns.
  - **Blocker:** the survey found no per-arm output, so the inventory cannot be extracted. A
    rebuild must first make every case print an `ok`/`FAIL` line at today's tree. That is a
    separate commit, observed equal on both sides, before any port.
  - **Cost:** large, 2+ sessions. Levers 1-3 likely get 60% of the gain at 20% of the cost.

## build-index selftest

`python3 tools/memory-tree/gen_build_index.py --selftest`. Ceiling 350.

- **(a) What it guarantees:** the generated work-state index, roster, bindings, `--doctor`, the
  probe bound and the new-build/new-spec scaffolds are graded over temp fixtures.
- **(b) Measured cost:** pool 225 s. Quiet ref 14 s (`n=4`, median 15). The pool reading is **16x
  the quiet one**: this leg is a victim of the host (RAM at 94-96%), not of its code.
- **(c) Where the time goes:**
  - 72 `_fixture` calls (`gen_build_index.py:3679`) at 5 git spawns each (init, 2 config, add,
    commit), 360 in total.
  - 77 more `run()` git calls.
  - 2 `run_hygiene_offenders` calls, each a full checker `--offenders` run (`:6180`).
  - One 1 s probe-bound arm (`:5466`).
- **(d) Levers:** fixture config through the environment (lever 10) removes 144 spawns, about 4 s
  quiet and about 60 s pool. Everything else is noise against contention.
- **(e) Full rebuild:** not warranted.

## backlog migration selftest

`python3 tools/memory-tree/migrate_backlog.py --selftest`. Ceiling **300**.

- **(a) What it guarantees:** the shards-to-builds relocation engine. Covers stragglers, recipe,
  write, plan and the check-26 audit in-process over fixtures.
- **(b) Measured cost:** pool 300 s, **timeout**. The serial retry took 104 s. The one historical
  reading is 211 s.
- **(c) Where the time goes:** already in-process (`run_engine` at `:2879`, `run_writer`,
  `run_plan`), so the cost is git spawns.
  - `init_repo` (`:2668`) is 5 spawns: init plus 4 config.
  - `run_commit` and `run_commit_on` are 3 each: add, commit, `rev-parse HEAD`.
  - The engine's own git calls run inside 48 `run_engine`, 5 `run_writer` and 17 `run_plan` calls.
  - 56 direct `run` calls and 16 `run_unchecked` calls. The file has 103 `run("git"` sites.
- **(d) Levers:**
  1. Fixture config through the environment (lever 10).
  2. Read HEAD from `.git/HEAD` and the ref file instead of `rev-parse`.

  Together these are about 20-30% of spawns, 20-30 s serial.
- **Ceiling.** The 300 s ceiling sits **below** the loaded readings on record (211 s, and the pool's
  300+). That is a ceiling re-declaration by `selftest-budgets.txt`'s own rule, not a code fix.
- **(e) Full rebuild:** not warranted.

## row-grammar selftest

`python3 tools/memory-tree/row_grammar.py --selftest`. Ceiling 300.

- **(a) What it guarantees:** row grammar, relations, content, the rotation join (shell reader
  against python reader) and checks 27 and 28.
- **(b) Measured cost:** pool 241 s. Quiet ref 9.6 s (`n=4`). That is 25x, which is contention.
- **(c) Where the time goes:**
  - 36 fixtures, each with git init and config.
  - `run_fixture` respawns the module in a python subprocess per arm (`:2448`).
  - The rotation join spawns the shell checker's print mode with `timeout=60` (`:1900`); see the
    flake list.
- **(d) Levers:** lever 10 only. Port `run_fixture` to in-process `main(argv)` only if the leg ever
  matters quiet. It does not today.
- **(e) Full rebuild:** not warranted.

## gotchas selftest

`python3 tools/memory-tree/gotchas.py --selftest`. Ceiling 300.

- **(a) What it guarantees:** checks 17-19 (catalogue freshness, inert anchors, the universal
  budget and front-matter keys).
- **(b) Measured cost:** pool 154 s. Quiet ref 9 s (`n=4`).
- **(c) Where the time goes:**
  - 16 `cmd_check` calls. Each calls `append_only_re` (`:137-154`), which loads corpus_ids and
    calls `ask_shell` (bash probe plus checker re-entry), about 10 spawns each, 160 in total.
  - 14 `_scratch` calls at 5 git spawns each.
  - 32 `run` calls.
- **(d) Levers:** the `ask_shell` memo (lever 12) cuts 16 re-entries to about 2: about 140
  spawns, about 4 s quiet and about 70 s pool. Lever 10 trims 28 more.
- **(e) Full rebuild:** not warranted.

## check-arms selftest

`python3 tools/memory-tree/check-arms.py --selftest`. Ceiling 300.

- **(a) What it guarantees:** every failure-message signature in a tracked shell checker has an
  arm, or a pin in the unarmed registry.
- **(b) Measured cost:** pool 83 s. Quiet ref **2.4 s** (`n=4`). That is 35x, pure contention.
- **(c) Where the time goes:** about 50 git spawns (4 init, 8 config, 19 add, 19 commit).
- **(d) Levers:** lever 10 saves 8 spawns. **Not worth a change on its own**; fold it into the
  lever-10 sweep if one happens.
- **(e) Full rebuild:** none.

## memory hygiene (the leg itself)

`bash tools/memory-tree/check-memory-hygiene.sh`. Ceiling 12720.

- **(a) What it guarantees:** the real memory tree passes every hygiene check.
- **(b) Measured cost:** pool 129 s. Quiet ref 76 s (`n=10`, median 94, maximum 177).
- **(c) Where the time goes:** **no per-check trace of this tree is on record, and none was taken
  here** (read-only). From structure, one run on a 3633-file tree includes:
  - 10 python interpreters plus 1 probe, three of which are separate `row_grammar.py` corpus
    parses on top of the first, and two `gen_build_index.py` parses;
  - `corpus_ids` and `gotchas` re-entering the checker 3 times, one of which **re-runs checks 1-5
    over the whole tree** (`--print-index-set`, `:812`);
  - 3 `resolve_bash` probes.
- **(d) Levers:**
  - Lever 4: expected 5-15 s, the cost of checks 1-5 on the real tree plus the probes.
  - Lever 8: expected 5-20 s.
  - Take **one `PS4='+ ${EPOCHREALTIME} ${LINENO} '` trace on a quiet box first**. The current
    order of these two is a guess.
- **Ceiling.** 12720 s is about 100x this leg's readings. It looks mis-declared. This is outside
  the brief; flag it to whoever owns `gate-legs.json` ceilings.
- **(e) Full rebuild:** none.

## drift-audit selftest

`python tools/drift-audit/selftest.py`. Ceiling 2300.

- **(a) What it guarantees:** every gateable drift signal is silent on a clean fixture and fires on
  a violating one (no dead probes). The conf parser is checked against bash sourcing.
- **(b) Measured cost:** pool 2015 s. Quiet ref 170 s (`n=4`, median 204, maximum 755).
- **(c) Where the time goes:**
  - **93 `report()` calls** (`selftest.py:409`), each a fresh `python drift_report.py --json`.
    That computes **all 28 entries of `SIGNALS`** (`drift_report.py:3518`, run at `:4236`). Each
    signal spawns git: log walks, blame and the held-open `cat-file`. Some spawn more python
    (`gen_build_index --asks --json`, `migrate_backlog --stragglers`, `map_diff.py`).
  - **The arms read one signal.** 51 of the call sites subscript a single signal, and
    `closed_specs_with_no_product_commit` alone accounts for 16. Most of the 37 unsubscripted calls
    read one or two.
  - **39 `make_repo` calls** (`:274`), about 7 git spawns each.
- **(d) Levers:**
  1. **One signal per arm** (lever 2). The suite already holds `_build_run_ctx(dr, r)` (`:3259`)
     and calls signal functions in-process for 13 arms. Extend that: `one_signal(r, name)` builds a
     real `dr.Ctx` in-process, with `dr.repo_root` patched to the fixture and `drift_signals`
     reloaded from that fixture. It calls only the function whose record carries `name`.
     - **Name map:** derive the name-to-function map once, from one full report over a clean
       fixture. Never hand-type it, since a typed map is the two-answers class.
     - **CLI arms to keep:** a handful of full `--json` and `--check` runs that grade `main`'s own
       contract (pins, baselines, offline mode, refusals).
     - **Estimate:** a report drops from about 28 signals to 1, about 60-70% of report time. That
       is about 100 s quiet and about 1200 s pool.
     - **Risk:** module state across fixtures (cached `drift_signals`), and signals that read
       `ctx.signal_names` (handkept runs last on purpose; give it the derived name set).
  2. **A `--signal NAME` flag on `drift_report.py`** is the CLI alternative. It keeps arms
     out-of-process at about 0.5 s python each, so it saves less than lever 2.1 but is simpler to
     reason about. It does not touch the verdict-epoch scan set.
  3. **Build the `make_repo` base once and `copytree` it with `.git`.** About 200 spawns, 15-40 s
     quiet.
- **(e) Full rebuild:** not needed; lever 2 is the rebuild in miniature and keeps the arm list.

## memory-recall kit selftest

`python3 tools/memory-recall/selftest.py`. Ceiling 2730.

- **(a) What it guarantees:** the extraction, query, budget, bench and union contracts. Covers the
  adopter wiring (`adopt-memory-recall.sh`), the verbatim pins, the floor, and **that the whole
  suite passes from the adopter layout**.
- **(b) Measured cost:** pool 692 s. Quiet ref 85 s (`n=4`, median 174).
- **(c) Where the time goes:**
  - **The suite runs itself again, whole.** `test_adopter_layout` (`selftest.py:1712-1745`) copies
    the kit into a fixture and runs `selftest.py` there with `MRECALL_NESTED=1`. Only that arm
    skips in the child, so **every other arm runs twice**, which is about 45-50% of the leg.
  - **57 `make_repo` calls** (`:230`). Each is a git init plus copies of 6 kit files and every
    memory-tree `*.py` (about 15) plus `git add`.
  - **82 `run()` calls** (`:283`), each a fresh `python query.py`/`bench.py` process.
  - **16 `adopt()` calls**, each a bash run of the adopter.
- **(d) Levers:**
  1. **A layout subset in the nested run** (lever 6). Arms that resolve kit directories, the
     receipt, paths or the spine declare it, through a decorator flag beside `@check`, so the set
     is derived, not listed. The child runs only those arms.
     - **Estimate:** about 35-40 s quiet, about 300 s pool.
     - **Owner call:** the arm's claim narrows from "the whole selftest" to "every layout-sensitive
       arm". The `foreign-prefix parity` leg already re-runs whole suites at three prefixes, which
       may be the place that claim actually belongs.
  2. **In-process `query.main(argv)` for the `run()` arms**, with `chdir` and captured stdout. Saves
     about 82 python startups, 25-60 s quiet. Risk: global state in an 86 KB module, and
     `sys.exit`.
- **(e) Full rebuild:** not warranted. The survey rated it "no, inventory not extractable", and
  levers 1 and 2 keep the arm list.

## transition-audit arms

`bash tools/memory-tree/transition-audit.test.sh`. Ceiling 900. Repo subject.

- **(a) What it guarantees:** hygiene check 26 (`transition_audit.py`) classifies merges across a
  shards-to-builds transition, accounts for every relocated row, honours its cache and pin, and
  refuses shallow clones and dead probes. Its commit-msg hook carrier is graded, plus a both-ways
  hook population arm.
- **(b) Measured cost:** pool 277 s. Quiet ref 117 s (`n=10`, median 303, maximum 646).
- **(c) Where the time goes:**
  - **14 `new_repo` calls** (`:109`). Each does `cp -r` of a seed holding three kits (62 files,
    3.1 MB), `git init`, **5 `git config` spawns**, then `git add -A` (re-hashing 3.1 MB) and
    `commit`. 11 `flip_to_builds` calls add and commit again. There are 105 `git -C` sites.
  - **About 45 module runs:** `audit` × 26 and `audit_rc` × 19, each a python process walking git.
    **About 11 are an `audit` immediately followed by `audit_rc` on identical arguments**: `:161-162`,
    `:184-185`, `:235`, `:250-251`, `:299-300`, `:312-313`, `:319-320`, `:328-329` and `:381-382`.
    The output and the rc of one run are taken from two runs.
  - **5 `engine` calls** (`:143`): full hygiene runs over the fixture. They grep only check 26's
    prefix.
  - 11 inline python heredocs.
- **(d) Levers:**
  1. **One run per pair**: `out=$(audit ...); rc=$?`. Leave the cache arms at `:229-241` alone,
     since warm and cold state is their subject. About 9-11 python runs, 10-30 s quiet. Zero risk
     elsewhere.
  2. **Seed as a committed repo.** Commit the seed once, then `git clone -q --local --shared` per
     fixture, with config through the environment (lever 10). That drops 6 spawns and 3.1 MB of
     hashing per fixture, 20-45 s quiet. Verify that F11's `git checkout` arms do not depend on the
     index being freshly built.
  3. **`engine` calls with `--only 26`** once lever 3 exists. Keep one full engine run for the
     delegation claim. About 4 × 6-12 s.
- **(e) Full rebuild:** none.

---

## What this research does not establish

- **No figure here was measured by this pass.** Seconds saved are spawn counts × the recorded
  per-spawn cost, and the counts are static (call sites × visible loop bounds). A `bash -x` or
  `PS4` trace per suite is the check, and `_measure_git_calls` (`drift-audit/selftest.py:3267`) is
  a ready counter for the python side.
- **The pool-to-quiet ratios on the small python legs (16-35x) are host memory pressure**, at 94-96%
  RAM with 3 mempause holds. No code change in those legs recovers that. The big four (hygiene,
  manifest-check, drift-audit, merge-rows) are where code levers pay.
- **Lever 1's claim rests on log text**: the red lines name the claims cell's expected heads, and
  this session measured `--claims` at 66 s. It was not re-run here.
