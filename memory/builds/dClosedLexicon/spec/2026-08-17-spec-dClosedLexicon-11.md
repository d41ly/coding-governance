# TOOL-dClosedLexicon-11 — a build may have more than one unattended run

**Status:** SPECCED · rev-2 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

The unattended kit allows exactly ONE run per build folder, and nothing says so. `--preflight` writes
`<MEMORY_ROOT>/builds/<slug>/RUN.md`; once that record reaches a terminal phase, `refuse_if_terminal`
(`unattended.sh:574-581`) refuses every verb that would write it, including `--preflight`:

> the run is already finished and a finished record is not something to move, re-open or re-pin

That refusal is RIGHT about the record and WRONG as a policy about the build. Hit for real on
2026-08-16: this build's first run ABORTED, three units remained, and the second run could not start
— the remaining work proceeded on an explicit owner ask instead, outside the machinery meant to make
an unattended run checkable. A build that aborts once can never be carried unattended again.

The refusal is not incidental. `review-cFinalBerth-2` F2 reproduced what preflight did BEFORE it: a
second preflight over a `LANDED` record exited 0, kept `phase: LANDED`, and replaced the landing
witness with the current feature-branch HEAD — "a commit the remote never advertised". Rotation has
to keep that fixed, and it does, by giving the second run a FRESH record at `RUNNING` instead of
re-witnessing a finished one. Any design that merely relaxes the refusal reopens F2.

## 2. Scope (IN)

- **S1** — `--preflight` on a build whose run-state file is TERMINAL ROTATES that record to an
  immutable archive name and creates a fresh `RUN.md`. The rename is `GIT mv`, so BOTH sides enter
  the index in one operation: the leg's whole population is `git ls-files` (`check-unattended.sh:132`),
  and the driver already states the consequence at `unattended.sh:558-560` — "an unstaged run is
  invisible to every check it has". A failed rename is a named refusal, never a partial rotation.
- **S2** — the archive name is `RUN.<phase>.<blob8>.md`, where `<blob8>` is the first 8 hex of
  `git hash-object` over the record being retired. Both halves are DERIVED and the name is TOTAL:
  see §4 for why the previous `<witness8>` spelling was not.
- **S3** — the rotation runs at two different points, and this is the correctness core. The collision
  TEST runs with the other preconditions, before the single write gate at `unattended.sh:847`, so a
  refusal leaves the tree untouched. The RENAME runs AFTER that gate, in `scaffold_runmd`'s position,
  because the rename is what makes the tree dirty and `check_clean` (`:386-397`) fails on any
  non-zero count of diff/cached/untracked paths.
- **S4** — `check-unattended.sh`'s population becomes `RUN.md` PLUS `RUN.*.md`, at `:137` and in
  `check_single_live` (`unattended.sh:434`). Every archived record must be terminal; the live-run rule
  ("at most one in a non-terminal phase") is unchanged and now quantifies over the wider set, which is
  what makes rotation safe rather than a way to hide a second live run. Checks 9, 13 and 15 gain the
  archived records with it — 15 in particular, whose LANDED-witness ancestry assertion now covers every
  archived LANDED record and not only the live one.
- **S5** — memory-hygiene check 4 admits the archive. `check-memory-hygiene.sh:284` whitelists exactly
  seven entries at a build-folder root and `:285` requires every other file to match the recording
  grammar; the name S2 produces matches neither. Check 6's index cap set (`:337`) and check 7's prose
  exemption (`:384`) take it with them, since an archived record is the same document frozen. This
  moves a non-comment line of the hygiene engine, so `KIT_MEMORY_TREE_VERSION` moves with it (the
  verdict-epoch leg), and `memory/HYGIENE.md` + `tools/memory-tree/HYGIENE.template.md` are edited as
  one pair (the kit/dogfood parity leg).
- **S6** — protocol §2 records rotation as the way a build gets a second run, and states what it does
  NOT do: it does not re-open, re-pin or edit the retired record, whose bytes are preserved. A new
  check 16 in `check-unattended.sh` asserts the INSTALLED protocol spells the archive grammar
  literally, so a rotation shipped with a protocol that does not describe it reds. The existing
  protocol leg cannot see this: check 10 (`:377-393`) is a byte-diff of the shipped template against
  the installed copy and is green whatever both say.
- **S7** — the Skill's "Start a run" step names rotation, in `tools/unattended/SKILL.template.md` and
  therefore in the rendered `.claude/skills/unattended/SKILL.md`, which `adopt-unattended.sh --check`
  already holds to the template.
- **S8** — arms in `tools/unattended/unattended.test.sh` and `check-unattended.test.sh`. Two are
  CHANGES, not additions, and §7 says so: the five-writer drive at `unattended.test.sh:919` asserts
  every phase writer refuses a LANDED record and that `sum()` over `RUN.md` is unmoved — under S1 both
  fail for the `--preflight` member. That member moves to its own arm and the byte-identity operand
  re-points at the archived path. The population it drives is derived from source at `:912`
  (`grep -c 'set_fact "$rel" phase'`), so the drive list cannot shrink silently.

## 3. Non-goals (OUT)

- Relaxing `refuse_if_terminal` for any other verb. `--phase`, `--close`, `--landed` and `--abort`
  keep refusing a finished record — that quantifier is non-empty and stays so (`fail 31` at
  `unattended.sh:733-737`, `fail 15` and `fail 19`).
- Editing a retired record's CONTENT in any way. Rotation is a rename; the bytes are asserted equal.
- A run counter, a run id, or an index of runs. The archive names ARE the enumeration.
- Any change to what a run may DO. This is about how many runs a build may have, not their powers.
- Making `--preflight` refuse a NON-terminal record. It never has, deliberately — see §4.

## 4. Design

### Why rotate rather than reopen

The refusal protects a real property, and F2 above is the reproduction. Rotation keeps that property
intact — the finished record still exists, still says what it said, and is still readable — while
removing the policy nobody chose, that a build gets one run.

The alternative shapes are worse. Allowing `--preflight` to overwrite destroys the record. A
`runs/<seq>.md` directory changes the path shape every reader globs. A `--force` flag makes the
destructive path the one an operator reaches for when blocked, which is exactly when they should not
have it.

### The name is derived from the record's BYTES, because nothing else about a run is unique

rev-1 spelled the name `RUN.<phase>.<witness8>.md` and argued two runs could not collide "unless they
ended at the same phase AND the same witness, which is the same run". **The code refutes that.** The
witness is HEAD at the moment the phase was written (`verb_abort`, `unattended.sh:808-810`), and NO
driver verb commits — `grep -c "git commit"` over `unattended.sh` and `check-unattended.sh` returns 0
for both, and `stage_or_fail` (`:553-561`) reaches `GIT add` and stops. So run A aborts at commit W,
run B preflights, builds nothing and aborts at the same W, and run C computes a name that is already
taken. Under rev-1's AC3 that refuses forever with no operator path out, and the unit reproduces its
own §1 problem one abort later — the class the driver already carries in writing at `:855-858`, "the
refusal named a remedy that did not exist".

`git hash-object` over the retired record makes the name TOTAL. Two records with different content
get different names; two with identical content are the same record twice, and archiving one over the
other loses nothing. So the collision branch is no longer a dead end: an existing archive whose bytes
MATCH is a completed rotation and the verb proceeds; an existing archive whose bytes DIFFER is
impossible without a hand-placed file, and THAT refuses. The refusal survives as a guard rather than
as a policy.

This also deletes a second defect rather than guarding it. Nothing constrains a non-LANDED record's
witness to a sha — check 5 (`check-unattended.sh:216-218`) asserts presence only, check 6
(`:222-227`) skips a non-sha-shaped value by design, and the sha-shape refusal at `:239-244` is
guarded by `if [ "$ph" = LANDED ]` — so a hand-edited `witness: tag/v1` would have put a separator in
the path. A blob hash cannot. The `<phase>` half is safe because it is drawn from `PHASES_TERMINAL`
(`unattended.sh:74`, `LANDED ABORTED`) by the same `is_terminal` test that decides whether to rotate
at all: a phase outside that closed set does not rotate, so it never reaches the name.

### Where rotation runs, and why the split matters

rev-1 said "Rotation happens BEFORE those checks, so a refusal still leaves no fresh record". That is
a non-sequitur about the wrong artefact and it makes AC1 unreachable. `check_clean` counts
`git diff --name-only` + `git diff --cached --name-only` + `git ls-files --others --exclude-standard`
and fails on any non-zero count. The rotation is what makes the tree dirty — MEASURED in a scratch
repo, `mv` plus a fresh `RUN.md` gives 2, `git mv` plus a fresh `RUN.md` gives 2, `git mv` alone gives
1. Every spelling is non-zero. So a rotating preflight placed before the precondition block ALWAYS
reaches `:847`, prints `unattended: --preflight refused; the run-state file is unchanged`, and returns
1 — over a tree where the record has already been renamed away from the path `--resume` and every
reader glob look for. The claim in that refusal string would also be false, which is the invariant the
file states twice at `:845-846` and `:849`.

Hence S3: the TEST early, the RENAME late. The rename lands exactly where `scaffold_runmd` does, and
the fresh record is created and staged by the unchanged path below it.

### `--preflight` does not refuse a non-terminal record, and must not start

rev-1's AC4 asserted it does. It never has: `refuse_if_terminal` returns 0 for every non-terminal
phase (`:578`), `verb_preflight` skips scaffolding when the file exists (`:851`) and preserves an
existing phase (`:878`), and `check_single_live` passes at `n <= 1` so the build's own live record is
explicitly allowed. The driver's comment at `:875-877` says why in as many words — preflight is the
documented post-compaction re-entry verb, and it used to move a resumed `BUILDING` run back to
`RUNNING`. A gated arm asserts the current behaviour (`unattended.test.sh:532-544`), so building to
rev-1's AC4 would have RED that leg. AC4 is replaced by the property actually at risk: rotation must
not fire on a non-terminal record.

### Data model

No conf key. The run-state file's authored facts are unchanged.

### Files touched (estimate)

`tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, their two self-tests,
`tools/unattended/SKILL.template.md` + the rendered `.claude/skills/unattended/SKILL.md`,
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (kept byte-equal by
check 10 — rev-1 credited check 15, which is the LANDED-witness pair), the unattended kit version pair,
and for S5: `tools/memory-tree/check-memory-hygiene.sh`, `memory/HYGIENE.md`,
`tools/memory-tree/HYGIENE.template.md` and `KIT_MEMORY_TREE_VERSION`.

## 5. Production-readiness checklist

- security — a run cannot use rotation to escape the anchor: `--preflight` re-observes the remote and
  re-pins BASE exactly as it does on a first run. Rotation happens AFTER every precondition, so
  `the run-state file is unchanged` stays true on every refusal path.
- perf / scale — one rename per new run.
- a11y / i18n — N/A.
- error / empty / loading states — a build with no prior record is the unchanged path; a NON-terminal
  record is not rotated and preflight behaves exactly as today; an archive whose bytes differ refuses.
- observability — the rotation is printed with both names, so an operator sees what was retired.
- risks — the real one is rotating a record that is not actually finished. The terminal test is the
  same `is_terminal` the rest of the kit uses, and AC4 arms the non-terminal case. The second is the
  hygiene-engine edit in S5, which dates every verdict of that engine; the verdict-epoch leg forces
  the version move and `hygiene-parity.test.sh` derives its floor from the same constant.
- testing + left-shift gates — S8, on two legs that already ride the bar, with two arms CHANGING
  rather than being added (§7).
- migration / rollback — none; existing records keep their names until a second run rotates them.
- user docs — protocol §2 (S6) and the Skill's "Start a run" step (S7).

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a build whose `RUN.md` is `ABORTED` or `LANDED` in an otherwise
  clean tree, it exits 0, `RUN.<phase>.<blob8>.md` and a fresh `RUN.md` both exist, and the fresh one
  reads `phase: RUNNING`.
- **AC2** — When the rotation happens, `cmp -s` between the archived file and a copy of the retired
  record taken before the call reports them byte-IDENTICAL.
- **AC3** — When the rotation happens, `git ls-files` lists the archived path and does NOT list the
  retired path, after a REAL rotation rather than a hand-built fixture.
- **AC4** — When the run-state file is NON-terminal, `--preflight` does NOT rotate it: the file keeps
  its name, its recorded phase and its parked entries, no `RUN.*.md` appears, and the verb exits 0 as
  it does today — with `unattended.test.sh:543-544` ("a re-run preflight leaves a reached phase
  alone") still green.
- **AC5** — When an archive already exists at the computed name with IDENTICAL bytes, `--preflight`
  proceeds; when one exists with DIFFERENT bytes, it refuses, names both paths, and the tree is
  unchanged (`git status --porcelain` empty).
- **AC6** — When an archived record is left in a non-terminal phase, `check-unattended.sh` reds; when
  an archived record reads LANDED, check 15's witness-ancestry assertion runs over it.
- **AC7** — When a rotated record is present in the index, `bash tools/memory-tree/check-memory-hygiene.sh`
  is green — and when S5's whitelist edit is reverted, it reds naming that path.
- **AC8** — When the installed `memory/guides/UNATTENDED-PROTOCOL.md` does not spell the archive
  filename grammar, `bash tools/unattended/check-unattended.sh` reds at check 16.
- **AC9** — When the four non-preflight phase writers are driven over a LANDED record, all four still
  refuse with the `already finished` message, and the replacement arm proves `--preflight` alone
  rotates.
- **AC10** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`bash tools/unattended/check-unattended.sh`, `bash tools/unattended/check-unattended.test.sh`,
`bash tools/unattended/unattended.test.sh`, `bash tools/unattended/adopt-unattended.sh --check`,
`bash tools/check-kit-versions.sh` (it derives `KIT_UNATTENDED_VERSION` from `unattended.sh` and
requires the same literal in `check-unattended.sh`), and for S5
`bash tools/memory-tree/check-memory-hygiene.sh`, `bash tools/memory-tree/check-memory-hygiene.test.sh`,
`bash tools/memory-tree/check-verdict-epoch.sh` and `bash tools/memory-tree/kit-dogfood-parity.test.sh`.
No new leg. Two existing arms CHANGE rather than being added — `unattended.test.sh:919`'s drive list
and its `sum()` operand — which is stated here because rev-1 claimed arms were only added.

## 8. Open questions

- **F1 — should the archive live in the build folder or under `archive/`?** RESOLVED (agent,
  2026-08-17, delegated): the build folder. `check-unattended.sh:137` selects
  `^$M/builds/[^/]+/RUN\.md$`, and `--resume` and every reader glob look there. Moving it would put
  the record outside the population every existing reader globs, for no gain.
- **F2 — whitelist the archive at the build root, or file it under `build/`?** RESOLVED (agent,
  2026-08-17): whitelist it. Check 4's own comment at `:261-266` records that admitting `RUN.md`
  required exactly this amendment, and gives the reason — a resuming session must be able to COMPUTE
  the name. The `build/` route would need a date (a clock) and a seq (a chosen number), which
  reintroduces the "derived, not chosen" problem the name exists to avoid.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, written from the refusal that was hit on 2026-08-16 rather than
  from the backlog row's summary.
- rev-2 · 2026-08-17 · folds `review-dClosedLexicon-9`, 11 defects, 3 of them blockers. AC4 replaced —
  it asserted a `--preflight` refusal of a non-terminal record that has never existed and whose
  implementation would have red `unattended.test.sh:543-544` (11-B1). Rotation split into an early
  collision TEST and a late RENAME, because a rotation before `check_clean` refuses itself and leaves
  the record off the reader path (11-B2). Hygiene check 4 admits the archive, with the kit version
  cascade priced (11-B3) — reproduced by running check 4's awk verbatim over `git ls-files memory/`
  plus the hypothetical path. The name derives from `git hash-object` rather than the witness, because
  no verb commits so two runs share a witness (11-1) and nothing constrains a non-LANDED witness to a
  sha (11-5). Rotation stages both sides via `GIT mv` (11-2). S6 gains check 16 and S7 the Skill step
  (11-3). S8 states the two arms that CHANGE (11-4). Check 15 corrected to check 10 (11-6).
  `check-kit-versions.sh` added to §7 (11-7). §10 records what the probes actually returned (11-8, X-1).

## 10. Reuse audit

**Probe 1, `reuse_lookup.py` — RE-RUN, and it MISSES.**
`python tools/codebase-map/reuse_lookup.py "retire a record and start a fresh one"` returns `records`,
`extract_records`, `test_generated_artifacts_are_fresh`, `zero_record_diagnosis`,
`strip_records_sentence`, `t_zero_records_is_loud` plus dossier and inventory rows; grepping the output
for `rotat|archive` matches nothing. rev-1 claimed it "surfaces the memory-tree kit's index ROTATION".
It cannot: that rotation is a prose discipline in `check-memory-hygiene.sh:373` and `:468-474`, not an
indexed symbol. Recorded as an answer per M5 rather than deleted.

**Probe 2, `query.py` — terms recorded for M7 (satisfied once for the SET, per M5).**
Question: *how does this repo retire a finished record and start a fresh one without losing the old
bytes, and how does a preview verb stay in step with the verb that acts.*
Terms: `rotation archive retired record terminal phase preflight refusal preview parity plan apply
divergence symbol corpus census`. It returned the decisive prior art this spec now opens with —
`memory/builds/cFinalBerth/reviews/2026-08-13-review-cFinalBerth-2.md:98` (F2, the defect the refusal
was added to fix) and `TOOL-cFinalBerth-1` in `memory/DECISIONS.md:47` ("a terminal record cannot
re-open"). Neither was reachable through probe 1.

**Reuse, hand-verified.** The rotation precedent is the memory tree's own index rotation — a size
-triggered move to `memory/archive/<FAMILY>.<date>.md` whose retired copy is byte-identical and still
readable (`check-memory-hygiene.sh` checks 6 and 10, `HYGIENE.template.md` §"Index budgets, caps,
rotation"). This unit reuses that DISCIPLINE, not its code. `refuse_if_terminal` is the single branch
every phase-writer routes through (`unattended.sh:574-581`), so S1 extends one call site rather than
adding a second rule.
