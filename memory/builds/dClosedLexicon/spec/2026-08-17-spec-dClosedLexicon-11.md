# TOOL-dClosedLexicon-11 — a build may have more than one unattended run

**Status:** SPECCED · rev-3 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

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
  immutable archive name and creates a fresh `RUN.md`. The rename is `GIT mv -f`, so BOTH sides enter
  the index in one operation: the leg's whole population is `git ls-files`
  (`check-unattended.sh:132`), and the driver already states the consequence at `unattended.sh:558-560`
  — "an unstaged run is invisible to every check it has". **`-f` is what the early collision TEST
  buys** (S3): a byte-DIFFERING destination has already refused before the tree was touched, so the
  only destination the rename can reach is absent or byte-identical, and forcing over byte-identical
  bytes changes nothing. Plain `GIT mv` cannot do this — MEASURED rc=128, `destination exists`, with
  the destination tracked and with it merely present. A rename that fails for any other reason is a
  named refusal, never a partial rotation.
- **S2** — the archive name is `RUN.<phase>.<blob8>.md`, where `<blob8>` is the first 8 hex of
  `git hash-object` over the record being retired. Both halves are DERIVED and the name is TOTAL:
  see §4 for why the previous `<witness8>` spelling was not.
- **S3** — the rotation runs at two different points, and this is the correctness core. The collision
  TEST runs with the other preconditions, before the single write gate at `unattended.sh:847`, so a
  refusal leaves the tree untouched. The RENAME runs AFTER that gate, in `scaffold_runmd`'s position
  (`:851-853`), because the rename is what makes the tree dirty and `check_clean` (`:386-397`) fails
  on any non-zero count of diff/cached/untracked paths.
- **S4** — `check-unattended.sh`'s population becomes `RUN.md` PLUS `RUN.*.md`, at **`:138`** — the
  `RUNS=` selector every per-file check iterates — and in `check_single_live` (`unattended.sh:434`).
  `:137`'s `PRE` counter stays as it is: it is the mis-segmentation PRECONDITION, not the population,
  and an archives-only tree reading `PRE=0` with `POP>0` is silent by design. Checks 9, 13 and 15 gain
  the archived records with the widening — 15 in particular, whose LANDED-witness ancestry assertion
  now covers every archived LANDED record and not only the live one.
- **S5** — an archived record must be TERMINAL, and that gets its own branch rather than riding the
  live-run rule. `check-unattended.sh:375` is `[ "$nlive" -le 1 ] || fail 7`, which fires at TWO: a
  `RUN.md` that has reached LANDED plus one archived record hand-edited to `RUNNING` gives
  `nlive = 1` and the leg is silent — and that is the steady state after every completed second run.
  So the per-file loop gains a SECOND `fail 4` branch beside the existing phase-vocabulary one
  (`:208-211`): a path matching the archive grammar whose phase is outside `PHASES_TERMINAL` fails,
  naming the path and the phase. No new check number — this is a membership rule about a record's
  phase, which is what check 4 already owns.
- **S6** — memory-hygiene check 4 admits the archive, by GRAMMAR. `check-memory-hygiene.sh:284` is
  string equality over seven literals, so admitting a family needs a regex, and the one this unit adds
  is **`^RUN\.[A-Z]+\.[0-9a-f]{8}\.md$`**. SHAPE, not vocabulary: a phase token and a content hash.
  It rejects `RUN.notes.md` and `RUN.md.bak`, and it deliberately does NOT spell `LANDED|ABORTED`,
  because hard-coding the unattended kit's `PHASES_TERMINAL` into the memory-tree engine is a
  cross-kit coupling this repo has no reason to buy — the unattended leg owns the vocabulary (S5) and
  the hygiene engine owns the folder grammar. Check 6's index cap (`:337`) and check 7's prose
  exemption (`:384`) take the archive with it, since an archived record is the same document frozen;
  both are already regexes and need no such decision. This moves a non-comment line of the hygiene
  engine, so `KIT_MEMORY_TREE_VERSION` moves with it — and that bump is THREE marker pairs, not one
  (§4).
- **S7** — protocol §2 records rotation as the way a build gets a second run, and states what it does
  NOT do: it does not re-open, re-pin or edit the retired record, whose bytes are preserved. A new
  check 16 in `check-unattended.sh` asserts the INSTALLED protocol spells the archive grammar
  literally, so a rotation shipped with a protocol that does not describe it reds. The existing
  protocol leg cannot see this: check 10 (`:377-393`) is a byte-diff of the shipped template against
  the installed copy and is green whatever both say.
- **S8** — the Skill's "Start a run" step names rotation, in `tools/unattended/SKILL.template.md` and
  therefore in the rendered `.claude/skills/unattended/SKILL.md`, which `adopt-unattended.sh --check`
  already holds to the template.
- **S9** — arms, stated as ONE change, ONE addition and ONE restatement, because the arm layer here is
  more entangled than "two arms change" admits:
  - **CHANGE**: the five-member drive list at `unattended.test.sh:919` loses `--preflight`. That arm
    asserts every phase writer refuses a LANDED record and that the record is unmoved; under S1 both
    fail for `--preflight`.
  - **ADD**: a replacement arm proving `--preflight` alone rotates, with byte-identity taken the way
    AC2 already specifies — `cmp -s` against a copy made before the call — over the computed archive
    path.
  - **RESTATE**: `unattended.test.sh:913` checks the derived writer COUNT against a literal 5 and its
    message says "this arm drives 5". Dropping a member makes that false, and setting the literal to 4
    reds. Re-word the message, or replace the literal with a derivation over the drive list plus the
    separately-armed member, so the ratchet still names what it bounds.
  - **UNCHANGED**: `sum()` at `unattended.test.sh:137` is a SHARED helper — `$(sum)` appears 18 times
    across nine arms, every one proving a refused verb wrote nothing. Re-pointing its definition would
    make eight unrelated arms dead probes: `git hash-object <missing>` exits 128 with EMPTY stdout, so
    `before` and after are both `""` and `same` passes.
  - Arms also land in `check-unattended.test.sh` (S5's new branch, S7's check 16, the widened
    population) and in `tools/memory-tree/check-memory-hygiene.test.sh` (S6's grammar, AC7).

## 3. Non-goals (OUT)

- Relaxing `refuse_if_terminal` for any other verb. `--phase`, `--close`, `--landed` and `--abort`
  keep refusing a finished record — that quantifier is non-empty and stays so (`fail 31` at
  `unattended.sh:733-737`, `fail 15` and `fail 19`).
- Editing a retired record's CONTENT. Rotation is a rename; the bytes are asserted equal. The ONE
  touch this permits is `GIT mv -f` over a destination whose bytes are already identical (S1) — which
  writes the same bytes that were there, and is why the non-goal survives the force flag.
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
MATCH is overwritten with those same bytes and the verb proceeds; an existing archive whose bytes
DIFFER refuses at the early TEST, before the tree is touched.

**What actually reaches the proceed branch is a hand-placed byte-identical copy** — nothing the driver
produces. rev-2 said "a completed rotation", and that is wrong: after a completed rotation `RUN.md` is
the fresh RUNNING record, so `refuse_if_terminal` returns 0 and rotation is never re-attempted; an
interrupted rotation leaves no `RUN.md` to retire. Saying so matters, because it is the sentence that
decides whether the branch is a guard (it is) or a workflow (it is not).

This also deletes a second defect rather than guarding it. Nothing constrains a non-LANDED record's
witness to a sha — check 5 (`check-unattended.sh:216-218`) asserts presence only, check 6
(`:222-227`) skips a non-sha-shaped value by design, and the sha-shape refusal at `:239-244` is
guarded by `if [ "$ph" = LANDED ]` — so a hand-edited `witness: tag/v1` would have put a separator in
the path. A blob hash cannot. The `<phase>` half is safe because it is drawn from `PHASES_TERMINAL`
(`unattended.sh:74`, `LANDED ABORTED`) by the same `is_terminal` test that decides whether to rotate
at all: a phase outside that closed set does not rotate, so it never reaches the name.

The name is also stable across this fleet: `.gitattributes` pins `memory/**/*.md text eol=lf`, which
covers `RUN.*.md` as well as `RUN.md`, and `git hash-object` applies the path's clean filter — so the
derived name is the INDEX blob's on Windows and Linux alike.

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

### Files touched

`tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, their two self-tests,
`tools/unattended/SKILL.template.md` + the rendered `.claude/skills/unattended/SKILL.md`,
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (kept byte-equal by
check 10 — rev-1 credited check 15, which is the LANDED-witness pair), and the unattended kit version
pair.

`AGENTS.md`, because its gate-suite bullet reads "fifteen checks" and S7 adds a sixteenth. **Nothing
gates that number** — the only charter probe over the gate suite,
`_charter_mentions_every_leg` (`tools/drift-audit/drift_signals.py:104-136`), matches leg argv script
paths and never reads a count.

For S6, the memory-tree side, which is SEVEN marker spots and not one:
`tools/memory-tree/check-memory-hygiene.sh` (the whitelist, plus its own inline marker at `:13`),
`tools/memory-tree/check-memory-hygiene.test.sh` (AC7's arm),
`tools/memory-tree/{HYGIENE,SPEC-TEMPLATE,BUILD-METHOD}.template.md` and their three dogfooded twins
`memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`. All six carry
`<!-- gov:kit memory-tree@N.N -->` at line 1; `check-kit-versions.sh:81-96` derives that population
from `git ls-files 'tools/memory-tree/*.template.md'` and `kit-dogfood-parity.test.sh:53` pairs them.
MEASURED: bumping the constant alone reds `check-kit-versions.sh` with three findings.
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` moves the renders.

## 5. Production-readiness checklist

- security — a run cannot use rotation to escape the anchor: `--preflight` re-observes the remote and
  re-pins BASE exactly as it does on a first run. Rotation happens AFTER every precondition, so
  `the run-state file is unchanged` stays true on every refusal path — that string is emitted only at
  `unattended.sh:847`, above the rename's position.
- perf / scale — one rename per new run.
- a11y / i18n — N/A.
- error / empty / loading states — a build with no prior record is the unchanged path; a NON-terminal
  record is not rotated and preflight behaves exactly as today; an archive whose bytes differ refuses
  before the tree is touched.
- observability — the rotation is printed with both names, so an operator sees what was retired.
- risks — the real one is rotating a record that is not actually finished. The terminal test is the
  same `is_terminal` the rest of the kit uses, and AC4 arms the non-terminal case. The second is the
  hygiene-engine edit in S6, which dates every verdict of that engine; the verdict-epoch leg forces
  the version move and `hygiene-parity.test.sh` derives its floor from the same constant. The third is
  `-f`: it is safe only because the early TEST refused a byte-differing destination, so the two must
  land together or not at all.
- testing + left-shift gates — S9, across three self-tests, with one arm CHANGING and one message
  restated (§7).
- migration / rollback — none; existing records keep their names until a second run rotates them.
- user docs — protocol §2 (S7), the Skill's "Start a run" step (S8), and `AGENTS.md`'s check count.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a build whose `RUN.md` is `ABORTED` or `LANDED` in an otherwise
  clean tree, it exits 0, `RUN.<phase>.<blob8>.md` and a fresh `RUN.md` both exist, and the fresh one
  reads `phase: RUNNING`.
- **AC2** — When the rotation happens, `cmp -s` between the archived file and a copy of the retired
  record taken before the call reports them byte-IDENTICAL.
- **AC3** — When a REAL rotation runs (not a hand-built fixture), `git ls-files` lists the archived
  path, and `git hash-object` over `RUN.md` no longer equals its pre-call value — the fresh record is
  staged, not the retired one. `RUN.md` is expected to be listed: the same verb re-creates and stages
  it at `unattended.sh:851-853` and `:880`, which is why rev-2's "does NOT list the retired path"
  could only ever have held on a refusal.
- **AC4** — When the run-state file is NON-terminal, `--preflight` does NOT rotate it: the file keeps
  its name, its recorded phase and its parked entries, no `RUN.*.md` appears, and the verb exits 0 as
  it does today — with `unattended.test.sh:543-544` ("a re-run preflight leaves a reached phase
  alone") still green.
- **AC5** — When an archive already exists at the computed name with IDENTICAL bytes, `--preflight`
  proceeds and exits 0; when one exists with DIFFERENT bytes, the early TEST refuses, names both
  paths, and `git status --porcelain` is empty afterwards.
- **AC6** — When `GIT mv -f` fails for a reason the collision test did not cover, `--preflight` emits
  a named refusal carrying both paths and does not scaffold a fresh record — the branch is armed by an
  assertion naming its own failure text, per `check-arms.py`.
- **AC7** — When an ARCHIVED record carries a phase outside `PHASES_TERMINAL`,
  `bash tools/unattended/check-unattended.sh` reds at check 4 naming that path and phase — asserted
  over a fixture where the live `RUN.md` is already LANDED, so `nlive` is 1 and check 7 is silent.
- **AC8** — When an archived record reads LANDED with a witness not reachable from the anchor,
  `bash tools/unattended/check-unattended.sh` reds at check 15; with the population un-widened, the
  same fixture is silent. (Stated as its red because check 15 prints nothing on success, so "it ran
  and passed" and "it never saw the file" are the same empty stdout.)
- **AC9** — When a fixture carries `RUN.<terminal>.<8 hex>.md` at a build root, check 4 does NOT name
  it; when a fixture carries a near-miss the grammar must still reject (`RUN.notes.md`), check 4 DOES
  name it — the `cnot`/`chit` pair at `check-memory-hygiene.test.sh:476-478` is the shape, and it is
  the arm that pins the GRAMMAR rather than merely the amendment.
- **AC10** — When a rotated record is present in the index,
  `bash tools/memory-tree/check-memory-hygiene.sh` is green over the whole tree.
- **AC11** — When the installed `memory/guides/UNATTENDED-PROTOCOL.md` does not spell the archive
  filename grammar, `bash tools/unattended/check-unattended.sh` reds at check 16.
- **AC12** — When the four non-preflight phase writers are driven over a LANDED record, all four still
  refuse with the `already finished` message, and the replacement arm proves `--preflight` alone
  rotates.
- **AC13** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`bash tools/unattended/check-unattended.sh`, `bash tools/unattended/check-unattended.test.sh`,
`bash tools/unattended/unattended.test.sh`, `bash tools/unattended/adopt-unattended.sh --check`,
`bash tools/check-kit-versions.sh` (it derives `KIT_UNATTENDED_VERSION` from `unattended.sh` and
requires the same literal in `check-unattended.sh`, and it is the leg that catches an under-scoped
memory-tree bump), `python tools/memory-tree/check-arms.py --check` (the meta-gate over the three new
`fail` branches — S1's rename refusal, S5's archive-terminal branch and S7's check 16; it carries NO
guard, so it runs on every invocation), and for S6
`bash tools/memory-tree/check-memory-hygiene.sh`, `bash tools/memory-tree/check-memory-hygiene.test.sh`,
`bash tools/memory-tree/check-verdict-epoch.sh` and `bash tools/memory-tree/kit-dogfood-parity.test.sh`.

No new leg. One existing arm CHANGES rather than being added — the drive list at
`unattended.test.sh:919` — and one message is restated at `:913`; §2 S9 spells out which, because
rev-2 said "two arms CHANGE" and it is one change, one addition and one restatement.

`.memory-tree.conf`'s `ARMS_FLOORS` needs no edit: its rows are one-sided MINIMUMS, so an armed new
branch moves 38/38 to 39/39 and no floor moves. `memory/project/unarmed-branches.txt` needs none
either: it pins `unattended.sh` check 9 branch 1 = the `fail 9` at `:559`, and the rename sits below
it, so no ordinal renumbers.

## 8. Open questions

- **F1 — should the archive live in the build folder or under `archive/`?** RESOLVED (agent,
  2026-08-17, delegated): the build folder. `check-unattended.sh:138` selects
  `^$M/builds/[^/]+/RUN\.md$`, and `--resume` and every reader glob look there. Moving it would put
  the record outside the population every existing reader globs, for no gain.
- **F2 — whitelist the archive at the build root, or file it under `build/`?** RESOLVED (agent,
  2026-08-17): whitelist it. Check 4's own comment at `:261-266` records that admitting `RUN.md`
  required exactly this amendment, and gives the reason — a resuming session must be able to COMPUTE
  the name. The `build/` route would need a date (a clock) and a seq (a chosen number), which
  reintroduces the "derived, not chosen" problem the name exists to avoid.
- **F3 — tight or loose archive grammar in check 4?** RESOLVED (agent, 2026-08-17):
  `^RUN\.[A-Z]+\.[0-9a-f]{8}\.md$`, the middle. `RUN\..*\.md` would admit `RUN.notes.md` and
  `RUN.md.bak` at every build root forever with no waiver registry and no ratchet;
  `RUN\.(LANDED|ABORTED)\.…` would hard-code the unattended kit's phase vocabulary into the
  memory-tree engine. The shape is the hygiene engine's business and the vocabulary is the unattended
  leg's (S5), so each gate asserts the half it owns.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, written from the refusal that was hit on 2026-08-16 rather than
  from the backlog row's summary.
- rev-2 · 2026-08-17 · folds `review-dClosedLexicon-9`, 11 defects, 3 of them blockers. AC4 replaced —
  it asserted a `--preflight` refusal of a non-terminal record that has never existed and whose
  implementation would have red `unattended.test.sh:543-544`. Rotation split into an early collision
  TEST and a late RENAME, because a rotation before `check_clean` refuses itself. Hygiene check 4
  amended, with the kit version cascade priced. The name derives from `git hash-object` rather than
  the witness, because no verb commits so two runs share a witness. Rotation stages both sides.
- rev-3 · 2026-08-17 · folds `review-dClosedLexicon-10` (CLEAN WITH FIXES, 10 defects, no blockers;
  all three prior blockers confirmed closed). The three majors were all criteria the design could not
  satisfy: `GIT mv` returns rc=128 on an existing destination, so the identical-bytes PROCEED branch
  AC5 requires was unreachable — it is `GIT mv -f` now, and §4 names the state that actually reaches
  it, a hand-placed copy rather than "a completed rotation" (11-9). AC3's "does NOT list the retired
  path" contradicted AC1 and could hold only on a refusal (11-10). S6 now writes the admitted GRAMMAR
  out — check 4's whitelist is string equality, so a family needs a regex, and F3 records why the
  middle one — and AC9 restates the falsifying half as the `cnot`/`chit` near-miss pair the harness can
  actually express (11-11, which neither pass had filed). S5 gives the archive-terminal rule its own
  `fail 4` branch, because `nlive <= 1` is silent in the post-landing steady state (11-12). The
  memory-tree cascade is priced at all seven marker spots (11-13). `check-arms.py --check` joins §7
  and the rename refusal gains AC6 (11-14). S9 replaces "two arms CHANGE" with one change, one
  addition, one restatement and one explicit UNCHANGED — `sum()` is a shared helper whose re-pointing
  would make eight arms dead probes, and `:912`'s derivation counts writers in the DRIVER, not the
  drive list (11-15). Population re-cited to `:138` (11-16). §10's quotation re-attributed (11-17).
  `AGENTS.md` and `check-memory-hygiene.test.sh` added to Files touched (11-18).

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
divergence symbol corpus census`. It returned the decisive prior art this spec opens with —
`memory/builds/cFinalBerth/reviews/2026-08-13-review-cFinalBerth-2.md:98`, F2's heading line, the
defect the refusal was added to fix. `memory/archive/TOOL.2026-08-14.md:53` carries "a terminal record
cannot re-open" (rev-2 attributed that sentence to `memory/DECISIONS.md:47`, which does not carry it).
`memory/DECISIONS.md:47` says something sharper and is cited for it: **a terminal phase is written by
a verb that EVALUATES what it claims, never by a phase move** — which is the constraint on a rotation
that hands a second run a fresh record, and the reason S1 scaffolds at `RUNNING` rather than clearing
a phase in place.

**Reuse, hand-verified.** The rotation precedent is the memory tree's own index rotation — a
size-triggered move to `memory/archive/<FAMILY>.<date>.md` whose retired copy is byte-identical and
still readable (`check-memory-hygiene.sh` checks 6 and 10, `HYGIENE.template.md` §"Index budgets,
caps, rotation"). This unit reuses that DISCIPLINE, not its code. `refuse_if_terminal` is the single
branch every phase-writer routes through (`unattended.sh:574-581`), so S1 extends one call site rather
than adding a second rule. AC9's `cnot`/`chit` near-miss pair is lifted from
`check-memory-hygiene.test.sh:476-478`, the arm the house already wrote for the previous amendment to
this same whitelist.
