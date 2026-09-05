# TOOL-aStagedLane-2 — an attended mode on the harness, so the stage order needs no mandate

**Status:** CLOSED · rev-6 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-3 TOOL-aStagedLane-4 |
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-3 TOOL-aStagedLane-4 |
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round3.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round3.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-3 |
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round4.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round4.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-3 |
| [2026-09-05-review-TOOL-aStagedLane-1-diff-review-round1.md](../reviews/2026-09-05-review-TOOL-aStagedLane-1-diff-review-round1.md) | diff-review | TOOL-aStagedLane-1 TOOL-aStagedLane-3 |
| [2026-09-05-review-TOOL-aStagedLane-1-diff-review-round2.md](../reviews/2026-09-05-review-TOOL-aStagedLane-1-diff-review-round2.md) | diff-review | TOOL-aStagedLane-1 TOOL-aStagedLane-3 |

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/workflows/unattended-build.js` runnable by a session that has no run-state file, so the
stage order it enforces is available to ordinary work. Today the harness is the only fixed route
from spec to build, and it is reachable only under a mandate, which leaves every other session
choosing its route per session.

## 2. Scope (IN)

- **S1** — a `mode` argument over the closed pair `attended` and `unattended`, defaulting to
  `unattended`. The default preserves the shipped contract, so an adopter's existing call is
  unchanged by this unit and no caller has to be migrated.
- **S2** — in attended mode the audit stage does not spawn the agent that records the round through
  the driver. `tier2-review.js` already returns a blocker count and a report path to the script, and
  those two values are what the stage needs.
- **S3** — in attended mode the verdict is computed from that blocker count alone: zero is terminal,
  a positive integer is converging, and a non-integer REFUSES. The degraded paths of the review
  harness return a null blocker count by design, so null must never be read as a clean bill.
- **S4** — in attended mode the build stage takes its per-unit refusal from the state `--plan`
  reports, and **the CALLER runs that verb**, matching §4's table rather than contradicting it.
  This script has no shell and no filesystem, so it cannot run `--plan` itself; rev-4 said the
  stage "takes its refusal from `--plan`" without saying who ran it or how the answer arrived, and
  the two texts gave different answers. **The mechanism is a `planState` field on each `units[]`
  entry**, resolved by the caller from `--plan`. That CHANGES the input contract, which today
  carries `{id, order, specPath, briefPath}`, and a missing `planState` in attended mode REFUSES
  rather than defaulting — a defaulted state is a refusal predicate grading a value nobody
  supplied.
  **WHEN it is resolved is the other half, and rev-5 did not say.** The caller resolves `planState`
  ONCE, at entry, because this harness runs SPEC, AUDIT and BUILD in a single invocation and the
  only early return before BUILD is the CONVERGING gate — there is no point between the stages at
  which a caller could re-run `--plan`. That makes the entry-time value STALE BY CONSTRUCTION for
  exactly the units the SPEC stage is about to author: a fresh build reports `MISSING` for every
  one of them, and a BUILD stage refusing on `MISSING` would refuse the whole build it just specced.
  **So the BUILD stage subtracts what stage 1 did**: a unit the SPEC stage returned in `authored`
  or `alreadyPresent` is treated as `READY` regardless of its entry-time `planState`, and the
  entry-time value governs only units that stage did not touch. That return already exists and is
  already schema-required, so this reuses it rather than adding a channel.
  **The state is matched as a PREFIX, not against a closed token set**, and rev-5 got this wrong in
  a way that would have halted attended mode at unit one for the third time. `--plan` does not emit
  five tokens: `verb_plan` at `unattended.sh:2144` prints `DONE ($state)` for a terminal unit whose
  underlying grade is not READY, so the live vocabulary includes `DONE (THIN)`, `DONE (FORKED)` and
  `DONE (MISSING)`. Reproduced on `cBriefedPilot`, which prints `DONE (FORKED)`; `dGaugedVintage`,
  the build rev-5 cited, happens to be the one with a uniform `DONE` column, which is why the
  five-token reading survived. So: **any state BEGINNING `DONE` is terminal and SKIPS**, whatever
  follows it in parentheses — the parenthetical records how complete the spec was, not whether the
  unit still needs building. Of the rest, `MISSING`, `THIN` and `FORKED` REFUSE and `READY` builds.
  **A state matching none of those REFUSES BY NAME** rather than falling through to either arm, so
  a vocabulary this spec has now twice mis-transcribed cannot silently pick a behaviour. Rev-4
  refused
  "any state that is not `READY`", and `--plan` reports every terminal unit as `DONE` —
  `verb_plan` at `unattended.sh:2144` rewrites `CLOSED` and `WONTDO` to it, and `--plan
  dGaugedVintage` prints all thirteen ids that way. So the first attended run over a resumed or
  partly built build would have halted at unit one, which is round-1 B4's failure recurring inside
  the fold that claimed to close it. It would also have made attended mode STRICTER than the mode
  §3 says it is deliberately weaker than: `verb_dispatch` refuses only MISSING, THIN and
  out-of-order, and refuses neither `DONE` nor `FORKED`.
- **S4b** — the BUILD stage's PROMPT TEXT is mode-dependent, and this is the scope item without
  which the unit does not achieve its goal. Three driver verbs the prompt instructs the agent to run
  hard-refuse with no run-state file: `--dispatch` (`unattended.sh:4584`, fail 49), `--brief`
  (`:4184`, fail 49) and `--rescope` (`:4481`, fail 48). The prompt also tells the agent that such a
  refusal means the order is wrong and to STOP. In attended mode the refusal is caused by the mode
  itself, so an unmodified prompt halts the build at unit one after units are already being written
  — strictly worse than the refusal the mode was meant to trade away. In attended mode the prompt
  therefore omits `--dispatch` and `--brief` entirely.
  **`--rescope` is a THIRD case and rev-3 got it wrong.** It appears only in the `disposal` clause,
  which `unattended-build.js:473` composes as `verdict === 'CONVERGED' ? '' : …`; under S3 attended
  mode reaches BUILD only at zero blockers, which is the terminal verdict, so that clause is ALWAYS
  the empty string in this mode. Rev-3 said it was "replaced … so M4's PROMOTE disposal stays
  available", which rewrites a string attended mode never builds. What this unit does instead is
  state the fact: **attended mode has no reachable non-clean terminal verdict, so M4's disposal
  clause is unreachable in it**, and that limitation is named in the S5 header rather than papered
  over with a substitution nothing composes.
- **S4c** — `GROUND`, the preamble every spawned agent receives, is mode-aware. It currently
  hard-codes "You are one stage of a harnessed unattended build" and "nobody reads a transcript
  under a mandate", and it prefixes EVERY agent this file spawns in both stages. In this repository
  a mandate is precisely the authority to merge and push with no owner turn, so an attended run
  telling its agents they hold one is the falsehood this unit would otherwise create. The attended
  preamble says an owner is in the loop and that the driver's recording verbs are unavailable.
- **S5** — the file states, in its own header, what attended mode does NOT check, and it names the
  losses SEPARATELY rather than as one list of "refusals", because one of them is not a refusal.
  They are: the `--review` round record, `--dispatch`'s order refusal, `--dispatch`'s write-set
  record, `--brief`'s record of what each pass was handed, and `--rescope`'s amendment row. A reader
  who assumes otherwise gets a weaker guarantee than the one they think they have. The header also
  states that M4's blocker-disposal clause is UNREACHABLE in attended mode, because under S3 that
  mode reaches BUILD only at a terminal verdict and the clause is composed only for a non-clean
  one.
- **S6** — arms in `tools/workflows/unattended-build.test.sh` covering both modes: that unattended
  mode still records through the driver, that attended mode does not, that a null blocker count
  refuses in both, that the attended BUILD prompt names neither `--dispatch` nor `--brief`, that the
  attended preamble carries no mandate vocabulary, that a zero blocker count terminates while a
  positive one converges, that a `DONE (FORKED)` unit skips, that an unrecognised state refuses, and
  that a unit specced in this invocation is built despite an entry-time `MISSING`. The prompt arms assert on the COMPOSED string rather than on a
  run's behaviour, because a prompt is the one artifact here that no gate downstream ever reads,
  and each absence assertion is paired with a positive one so an empty clause cannot pass for a
  removed substring.
- **S7** — when `mode` is `attended` and a run-state file exists for that slug, the run WARNS and
  CONTINUES. The warning names the slug and the refusals being skipped, so a session that meant to
  run under its own mandate sees the mismatch rather than discovering it at the merge bar. The
  script cannot detect the file itself, because it has no filesystem; the caller supplies the fact
  and the harness warns on what it is given. A caller that supplies nothing gets no warning, and
  S5's header statement says so rather than leaving a reader to assume detection.

## 3. Non-goals (OUT)

- Not a second harness file. The whole value of this script is that the build stage is unreachable
  except through spec and audit, and two files re-open exactly that gap.
- Not renaming the file. A rename costs edits in `tools/workflows/kit.toml`, `tools/gate-legs.json`,
  `memory/project/method-carriers.txt` and the install-prefix ratchet, and buys no behaviour.
- Not moving the convergence loop into this script. It stays in the caller, because a convergence
  loop's iteration count is data-dependent and has no bounded receiver a marker can name.
- Not giving attended mode the strength of `--dispatch`. That refusal reads and writes the run
  state, and there is none; the enforcement that survives is the merge-bar leg in
  `TOOL-aStagedLane-1`.
- Not registering the self-test as a merge-bar leg. That is the act `TOOL-dBriefedPass-7` says
  belongs to a unit that specs it, and this unit does not.

## 4. Design

### The mode boundary

**Enumerated by DRIVER VERB REACHED, not by call site**, because rev-2 counted call sites and
missed two verbs that the prompts name but the script does not itself invoke. Every driver verb
reachable from this file, with what it does when no run-state file exists:

| verb | reached from | with no run-state file |
|---|---|---|
| `--review` | the audit stage's recorder agent (`:391`) | refuses |
| `--dispatch` | the BUILD prompt (`:493`) | refuses, fail 49 at `unattended.sh:4584` |
| `--brief` | the BUILD prompt (`:495`) | refuses, fail 49 at `unattended.sh:4184` |
| `--rescope` | the BUILD prompt's disposal clause (`:480`) | refuses, fail 48 at `unattended.sh:4481` |
| `--plan` | the CALLER, never this script | works |

All four of the first four are mode-dependent, and the fifth is not this script's call at all —
S4 now agrees with this row rather than contradicting it, and names the `planState` field that
carries the caller's answer in.
`--plan` already works without a run-state file, measured on this node against a build that never
had one, returning a unit state with exit status zero. The driver ships an attended records-root
path for `record_set` and `record_piece` (`unattended.sh:4418`, `:4449`) and none for `--brief`, so
the verbs cannot all be disposed of the same way and S4b says which gets which treatment.

### What each mode buys

Unattended mode is unchanged. Attended mode keeps the stage ORDER, which is JS control flow and does
not depend on the driver at all, and loses the five things S5 enumerates. Stage order is the property
the harness exists to provide, so attended mode delivers the thing it is for and is honest about the
rest.

### Where the verdict comes from

In unattended mode the driver owns the verdict vocabulary, because convergence is a property of the
SEQUENCE of rounds and no JS can compute it. In attended mode there is no run state to hold a
sequence, so the script computes a per-round verdict only, from the blocker count. The rounds
themselves remain visible as the review artifacts under the build's reviews folder, which the review
protocol already requires; nothing new is written to disk to hold them.

### Files touched (estimate)

`tools/workflows/unattended-build.js` and `tools/workflows/unattended-build.test.sh`. Two files.

### Alternatives rejected

Reading the round count from the reviews folder to compute convergence inside the script was
rejected: the script has no filesystem, so it would be an agent's claim wearing a script's authority.

Making `attended` the default was rejected because it silently weakens every existing caller.

## 5. Production-readiness checklist

- security — the mode argument selects which refusals run, so a caller that passes `attended` gets
  fewer. That is stated in the file header per S5 rather than being discoverable only by reading the
  branches.
- perf / scale — unchanged. Attended mode spawns strictly fewer agents than unattended mode.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — a mode value outside the closed pair must refuse, not default.
- observability — each stage already logs; attended mode logs which refusals it is not performing.
- risks — the real risk is a reader treating the two modes as equivalent, which S5 addresses in
  prose and `TOOL-aStagedLane-4` addresses in the carriers.
- testing + left-shift gates — S6, and the arms land with a red observed first.
- migration / rollback — the default preserves current behaviour, so reverting is a no-op for every
  existing caller.
- user docs — the rendered protocol and method carriers are `TOOL-aStagedLane-4`, not this unit.

## 6. Acceptance criteria

- **AC1** — When the harness is invoked with `mode` set to `attended` on a build with no run-state
  file, the run reaches the build stage, and the transcript shows no invocation of
  `unattended.sh --review`.
- **AC2** — When the harness is invoked with no `mode` argument, its behaviour is byte-identical to
  the behaviour before this unit, verified by the existing arms in
  `tools/workflows/unattended-build.test.sh` passing unmodified.
- **AC3** — When the audit stage receives a null `blockers` value from `tools/workflows/tier2-review.js`
  in either mode, the run REFUSES with a message naming the degraded return, and the build stage is
  not reached.
- **AC4** — When `bash tools/workflows/unattended-build.test.sh` runs the build stage in attended
  mode against a unit whose `planState` is `FORKED`, the stage refuses and its message names both
  the unit id and the state. The refusal is observed before the arm asserting it is written. The
  arm supplies that bare `FORKED` directly rather than harvesting it from a closed build's roster:
  `:2144` rewrites a terminal unit's grade to `DONE (FORKED)`, so a bare `FORKED` and a real closed
  build are jointly unsatisfiable and rev-5 asked for both at once. The REAL-roster requirement
  moves to AC11, where the value under test is one a closed build actually emits.
- **AC11** — When the same stage is fed the REAL `--plan` output of a closed build on disk — one
  emitting `DONE (FORKED)` as `cBriefedPilot` does, not only bare `DONE` — every terminal unit is
  SKIPPED with a log line naming it and the stage proceeds. A double containing only `READY`, or
  only bare `DONE`, cannot discover what a closed unit actually reports, and that is precisely how
  the five-token reading survived to rev-5.
- **AC13** — When the stage meets a `planState` outside every arm above, it REFUSES and names the
  unrecognised value. Neither building nor skipping an unknown state is safe, and this spec has
  mis-transcribed that vocabulary twice.
- **AC14** — When the SPEC stage authors a unit in the same invocation, the BUILD stage builds it
  even though its entry-time `planState` was `MISSING`. This is the fresh-build path: without it
  the harness refuses every unit it has just specced.
- **AC12** — When a `units[]` entry carries no `planState` in attended mode, the harness REFUSES
  at entry and names the entry. A defaulted state would put the refusal predicate to work on a
  value nobody supplied.
- **AC5** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`
  runs, it exits 0, and `bash tools/workflows/check-verifier-fanout.sh` stays green.
- **AC6** — When the header of `tools/workflows/unattended-build.js` is read, it names all five
  losses S5 enumerates, each classified as a refusal or a record and not the two conflated, and
  states that the S7 warning depends on the caller rather than on detection, AND states that M4's
  blocker-disposal clause is unreachable in attended mode and why — all in the section saying what
  this harness cannot buy. That third clause is S5's rev-4 addition, and without it coverage FELL
  across that fold: AC8 dropped an observed assertion about the disposal clause and S5's header
  statement replaced it unobserved.
- **AC8** — When the BUILD prompt is composed in attended mode, it contains no `--dispatch` and no
  `--brief` instruction, AND it still contains the surrounding per-unit build instruction that those
  two were removed from. The paired positive assertion is the point: an arm that only checks a
  substring is ABSENT passes just as well when the whole clause is empty, which is the
  vacuous-selector class this spec set polices elsewhere. The arm asserts on the composed string,
  because the defect is what the agent is TOLD to run and no gate downstream reads a prompt. Rev-3
  also asserted the disposal clause names a roster edit; that clause is never composed in attended
  mode, so the assertion is dropped rather than left to pass for the wrong reason.
- **AC10** — When `bash tools/workflows/unattended-build.test.sh` runs its two S3 verdict arms: the
  audit stage in attended mode receiving a blocker count of ZERO, the verdict is
  terminal and the build stage is reached; when it receives a POSITIVE integer, the verdict is
  converging and the harness returns without reaching the build stage. Both arms, because S3 is a new
  scope item of this unit and rev-3 observed only its null-refusal third — a branch mapping a
  positive count to terminal would reach BUILD over open blockers and satisfy every other criterion
  here, which is the exact failure the audit stage exists to prevent.
- **AC9** — When any agent is spawned in attended mode, the preamble it receives contains neither
  the word `mandate` nor the claim that nobody reads its transcript. A grep over the composed
  attended prompt for that vocabulary returns nothing.
- **AC7** — When the harness is invoked with `mode` set to `attended` and told a run-state file
  exists for that slug, a `log()` line names the slug and the skipped refusals, and the run reaches
  the build stage rather than refusing.

## 7. Gates

`node tools/workflows/check-workflow-syntax.js`, `bash tools/workflows/check-verifier-fanout.sh`,
`bash tools/workflows/check-review-join.sh`, and `bash tools/memory-tree/check-method-carriers.sh`
because this file is a declared method pointer. The full bar is `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — should attended mode refuse to run at all when a run-state file IS present?** A session
  that passes `attended` inside a live unattended run would skip refusals that run is bound by.
  Options: refuse when a run-state file exists for that slug; warn and continue; ignore.
  Recommendation: refuse. The mode is a statement about which enforcement applies, and a run under a
  mandate does not get to opt out of the mandate's enforcement by passing an argument.
  RESOLVED (owner, 2026-09-04): warn and continue. This goes AGAINST the recommendation above, which
  is recorded rather than rewritten. In scope as S7, with the caller-supplied detection and its
  limit named there, and AC7 observing the warning.

- **F2 — how does an attended run record that a review round happened?** In unattended mode the
  driver's round record is the answer. In attended mode the review artifact under the build's
  reviews folder is the only trace, and nothing refuses a run that never files one.
  Options: leave it to the review protocol, which already requires the artifact; add a stage that
  refuses to reach build without one; defer to a later unit.
  Recommendation: leave it. Adding a refusal here would be the script claiming to verify a file it
  cannot read.
  RESOLVED (owner, 2026-09-04): leave it to the review artifact the protocol already requires.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-04 · both forks resolved at the owner's scope-approval turn. F1 was ruled AGAINST
  the recommendation, taking warn-and-continue, which added S7 and AC7; F2 confirmed the design
  unchanged.
- rev-3 · 2026-09-04 · round-1 spec audit folded: B4, M1, M2. B4 is the one that made the unit miss
  its own goal — `--brief` and `--rescope` refuse without a run-state file exactly as `--dispatch`
  does, and the BUILD prompt tells the agent to run all three and to STOP on a refusal, so attended
  mode would have halted at unit one. S4b puts the prompt text under the mode branch; §4's boundary
  is now enumerated by driver VERB reached rather than by call site, which is how rev-2 counted three
  and missed two. S4c makes `GROUND` mode-aware, since it told every spawned agent it was under a
  mandate in both modes and no scope item touched it. S5 and AC6 now name the five losses separately
  instead of calling a record a refusal, and AC8 and AC9 observe the composed prompt, which is where
  the defect lives and where no downstream gate looks.
- rev-4 · 2026-09-04 · round-2 spec audit folded: findings 12 and 13. S4b's `--rescope` third
  was rewriting a string attended mode never composes — the disposal clause is built only for a
  NON-clean terminal verdict, and under S3 attended mode reaches BUILD only at zero blockers — so
  the substitution is withdrawn, the unreachability is stated in the S5 header instead, and AC8
  drops the assertion that could only have passed because its subject was absent. AC8 also gains
  a paired POSITIVE assertion, since an absence arm and an empty clause are indistinguishable.
  AC10 added: S3 specifies three verdict outcomes and rev-3 observed only the null refusal, so a
  branch mapping a positive blocker count to terminal would have reached BUILD over open blockers
  and passed every criterion in the section.
- rev-5 · 2026-09-04 · round-3 spec audit folded: findings 5, 6 and 8. S4 had put the refusal on
  `--plan` without saying who runs it, while §4's own table rowed that verb as the caller's — two
  answers, and AC4 gradeable only against a double the builder writes to match whichever they
  picked. S4 now names the `planState` field, says the input contract changes, and refuses a
  missing value. It also ENUMERATES the states instead of allow-listing `READY`: `--plan` reports
  every terminal unit as `DONE` (`unattended.sh:2144`), so the rev-4 predicate would have halted
  at unit one on any resumed build — round-1 B4 recurring inside the fold that closed it — and
  would have made attended mode stricter than the mode §3 calls it weaker than. AC11 and AC12 arm
  the skip and the missing field, and AC4 is fed a real closed build's roster. AC6 gains the third
  clause S5's rev-4 addition needed, since that fold traded an observed assertion for an
  unobserved one.
- rev-6 · 2026-09-04 · round-4 spec audit folded, the TERMINATING fold: the blocker count went 4, 2,
  1, 3, so the loop exited NON-CONVERGENT and M4's disposition is FOLD. Two of the three blockers
  were in this spec's rev-5 S4, the paragraph written to close round 3. B1: the "enumerated" state
  set is not what `--plan` emits — `:2144` prints `DONE (THIN)` and `DONE (FORKED)`, reproduced on
  `cBriefedPilot`, and `dGaugedVintage` was the one build with a uniform column, which is why the
  five-token reading survived being checked. The match is now a PREFIX on `DONE`, with an
  unrecognised state refusing BY NAME rather than falling through; AC13 arms that. B3: S4 never said
  WHEN the caller resolves `planState`, and the harness has no point between its stages at which a
  caller could re-run `--plan`, so a fresh build's entry-time value is `MISSING` for exactly the
  units stage 1 authors — the BUILD stage now subtracts that stage's own return, and AC14 arms the
  fresh-build path. H2: AC4 asked for a bare `FORKED` from a real closed build's roster, which
  `:2144` makes impossible; the two requirements are split across AC4 and AC11.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "run the spec-audit-build harness outside an unattended
mandate"` returned no seam. Its candidates were `run` in `tools/settings-merge.py` and a set of
`build_*_index` functions matched on name stem; the tool indexes 645 Python symbols and this unit's
subject is a JavaScript workflow script, so the surface is outside its corpus. The seam found by
reading is the script itself: its three driver call sites are already isolated, the roster it needs
already arrives as an argument, and `--plan` already answers without a run-state file, so this unit
adds a branch rather than a mechanism.

Recall terms used: `unattended-build harness Workflow sidechain driver mandate review dispatch stage
verdict convergence attended`. The query was why the build harness is bound to the unattended driver
rather than usable attended; it returned 40 hits, and the ones that bind are the owner ruling to fix
rather than waive the harness, and the open row recording that its self-test is on no bar.
