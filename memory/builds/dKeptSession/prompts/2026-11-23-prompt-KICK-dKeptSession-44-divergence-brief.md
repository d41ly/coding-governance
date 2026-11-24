**Serves:** research KICK-dKeptSession-44

# Brief — dKeptSession: KICK-dKeptSession-44's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-44's builder (run `wf_976362ba-48e`) stopped before its first edit and returned a DIVERGENCE. AC29,
and the §7 `New arm:` line for `tools/policy/check_policy.py` that covers it, says `python policy.py check` exits 1
once the `presets-repo` case commits `[presets.strict]`. `tools/policy/policy.py#cmd_check` exits only 0 or 2, and the
case's other refused scenarios in `tools/policy/check_policy.py#run_presets_repo` (`extends-lax`, `never-key`) assert
`rc == 2` and a stderr line opening `policy: refused · .governance/policy.toml:<n>`. The builder also found four stale
texts. Every other code claim held at the builder's base `6a7a6a052`. Revise the spec to the main loop's rulings below.

### Items

1. F-exit: resolved by the main loop. AC29 and its `New arm:` line read exit 2, with the stderr refusal line naming the
   `[presets.strict]` line and `strict`, graded the way the case's other refused scenarios are. `tools/policy/policy.py`
   stays out of Files touched. S32's check in `tools/policy/presets.py#check_repo_presets` reaches the CLI through that
   same Refusal.
2. F-dependents: resolved by the main loop. Unit 7 has landed `tools/loop/loop_transition.py#read_dependents`. It is
   called by `write_dependency_notices` and by the `dependents` verb, which `tools/govkit/usage.toml` declares
   (`script:{prefix}/loop/loop_transition.py#dependents`, flags `--build=` and `--root=`) and `help/loop.md` anchors.
   `tools/unattended/unattended.sh#write_landed_notices` runs that verb through `run_loop_verb`.
   - S20's Readers line is rewritten to name those readers.
   - The verb and its flags stay; the usage row does not move.
   - The function's source is re-pointed to the parent README's rendered `<!-- gen:build-edges -->` "Child builds"
     line, as S20 says.
   - Two fixture sets write only the dependent's `parents:` and never the parent's region: the unattended suite's
     `write_landed_dependent` (tRun, tDep), and `tools/loop/loop_transition.py#write_transition_plant` for the
     `deps-notices`, `notices-*` and `chain-two-dependents` plants. Name each in S20 and in Files touched, and say how
     each comes to hold the parent's region as the tree does, so the arms do not read zero dependents. Mind the class
     a double you wrote grades nothing: a fixture spelling the region by hand needs something that holds its shape
     to the render.
   - State the render lag as a limit, in §3 or in S20: a dependent opened after the parent's last
     `gen_build_index.py --write` is not notified until the next render.
3. F-met: S31 is already met. `tools/unattended/mail-notice.js#runDetachedFetch` spawns with `windowsHide: true`.
   Make S31 an observation only, and drop `mail-notice.js` from Files touched unless another clause still edits it.
4. F-figures: the §7 `New arm:` line's floors read `FLOOR_ASSERTIONS` 4180 and `FLOOR_SHARD_8` 1397 at this base.
   Pin each with DERIVED and its derivation, so the builder raises from the figure it reads.
5. F-bound: AC30's 12 s (PINNED 2026-11-23, the rev-6 AC30) bound on the whole `--landed` run leaves 2 s (PINNED
   2026-11-23) past `PROGRESS_BOUND=10` and `timeout -k 5s`,
   which covers the rest of `verb_landed`, including `observe_anchor`, and nothing has measured it. Derive the bound
   from `PROGRESS_BOUND`, the kill grace and a stated margin, rather than a typed 12.
6. F-decisions: S23 writes `memory/DECISIONS.md` only when the driver's census passes its `REFUSAL_CEILINGS` row.
   - `check 49` refuses a pass that declares that shared record.
   - The census reads 347/347 at this base (`python tools/memory-tree/check-arms.py --report`, PINNED 2026-11-23).
   - Say in S23 that a census past its ceiling stops the builder, and the main loop writes the dated decision row
     and both `.memory-tree.conf` rows.
   - Drop `memory/DECISIONS.md` and `.memory-tree.conf` from Files touched.
7. Bump the spec one rev, with one revision-log line naming this brief by its file stem.
   - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED.
   - Write no `[..](..)` link shape outside the generated records table.
   - Keep within the live-spec size cap, and leave no fork open.

### Acceptance

These all report nothing for the spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-44`

### Gates

Only these: the memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts
check and the driver's `--check-specs`.

### Non-goals

- No product code, no commit and no index render.
- No spec other than KICK-dKeptSession-44's. Other writers may be revising other specs at the same time: read them,
  never edit them.
- Read files freely; edit only the spec, in the run worktree.
