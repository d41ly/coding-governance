# TOOL-aStagedLane-2 — an attended mode on the harness, so the stage order needs no mandate

**Status:** SPECCED · rev-3 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-3 TOOL-aStagedLane-4 |

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
- **S4** — in attended mode the build stage takes its per-unit refusal from
  `bash tools/unattended/unattended.sh --plan <slug>`, which runs with no run-state file. The stage
  refuses a unit whose reported state is not `READY` and names the state it saw.
- **S4b** — the BUILD stage's PROMPT TEXT is mode-dependent, and this is the scope item without
  which the unit does not achieve its goal. Three driver verbs the prompt instructs the agent to run
  hard-refuse with no run-state file: `--dispatch` (`unattended.sh:4584`, fail 49), `--brief`
  (`:4184`, fail 49) and `--rescope` (`:4481`, fail 48). The prompt also tells the agent that such a
  refusal means the order is wrong and to STOP. In attended mode the refusal is caused by the mode
  itself, so an unmodified prompt halts the build at unit one after units are already being written
  — strictly worse than the refusal the mode was meant to trade away. In attended mode the prompt
  therefore omits `--dispatch` and `--brief` entirely, and replaces `--rescope` with the direct
  roster edit M2 describes, so M4's PROMOTE disposal stays available rather than leaving the method
  one of its two admitted routes.
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
  who assumes otherwise gets a weaker guarantee than the one they think they have.
- **S6** — arms in `tools/workflows/unattended-build.test.sh` covering both modes: that unattended
  mode still records through the driver, that attended mode does not, that a null blocker count
  refuses in both, that the attended BUILD prompt names none of the three refusing verbs, and that
  the attended preamble carries no mandate vocabulary. The last two assert on the COMPOSED prompt
  string rather than on a run's behaviour, because a prompt is the one artifact here that no gate
  downstream ever reads.
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

All four of the first four are mode-dependent, and the fifth is not this script's call at all.
`--plan` already works without a run-state file, measured on this node against a build that never
had one, returning a unit state with exit status zero. The driver ships an attended records-root
path for `record_set` and `record_piece` (`unattended.sh:4418`, `:4449`) and none for `--brief`, so
the verbs cannot all be disposed of the same way and S4b says which gets which treatment.

### What each mode buys

Unattended mode is unchanged. Attended mode keeps the stage ORDER, which is JS control flow and does
not depend on the driver at all, and loses the two driver-side refusals. Stage order is the property
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
- **AC4** — When the build stage runs in attended mode against a unit that `--plan` grades `FORKED`,
  the stage refuses and its message names both the unit id and the state `FORKED`. The refusal is
  observed before the arm asserting it is written.
- **AC5** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`
  runs, it exits 0, and `bash tools/workflows/check-verifier-fanout.sh` stays green.
- **AC6** — When the header of `tools/workflows/unattended-build.js` is read, it names all five
  losses S5 enumerates, each classified as a refusal or a record and not the two conflated, and
  states that the S7 warning depends on the caller rather than on detection, in the section saying
  what this harness cannot buy.
- **AC8** — When the BUILD prompt is composed in attended mode, it contains no `--dispatch` and no
  `--brief` instruction, and its disposal clause names the roster edit rather than `--rescope`. The
  arm asserts on the composed string, because the defect is what the agent is TOLD to run and no
  gate downstream reads a prompt.
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
