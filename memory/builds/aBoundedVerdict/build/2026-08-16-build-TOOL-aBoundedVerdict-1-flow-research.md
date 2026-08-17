# Research — the unattended review cycle, the fork rule, and the halt vocabulary

**Serves:** none — an adversarial research pass run BEHIND this build; it precedes the spec set and is what warranted it
**Commissions:** TOOL-aBoundedVerdict-1..5

Adversarial research pass behind `aBoundedVerdict`, run 2026-08-16 against base `96141aed` on node
`a`. Five evidence-producing probes, then batched skeptics defaulting to refute over every claim,
then one synthesis. Sixty-four claims raised, fifty-four confirmed, ten refuted, none left unjudged.
The refuted ten are recorded below rather than dropped, because three of them were load-bearing in a
probe's own recommendation.

Method: every claim required a file line actually read or a command actually run with its real
output. The live worktree was verified clean before and after; every experiment ran in a scratch
clone.

## 1. The three defect sites

### D1 — the review cycle has no bound and no exit rule

The build method requires every unreviewed spec be reviewed before its code, and defines a spec whose
rev moved since its last review as unreviewed. The verdict vocabulary is clean, clean with fixes, and
blocked. The only stated exit is to fold the fixes, bump the rev, and stop once a synthesis pass calls
the design clean.

Three facts about that loop, each confirmed:

- **No disposition exists for a blocked verdict.** Not a cap, not a park, not an abort.
- **A clean-with-fixes round re-arms the loop.** The fold bumps the rev, and a rev-moved spec is
  unreviewed by the method's own rule. The only clean exit is a literal clean verdict, and no verdict
  heading in the corpus says clean outright.
- **Nothing counts.** A repo-wide grep for any numeric review bound returns nothing.

Measured on the newest build in the tree: five consecutive spec-audit rounds over one seven-unit set
plus a sixth closing round, all on one day, verdicts clean-with-fixes, blocked, blocked, blocked,
clean-with-fixes, blocked. Final spec revs reached rev-12. Independently, every one of that build's
seven units is named by four or five of its six review records. The run did not stall — it
re-reviewed until a round came back clean enough, then landed with a blocked closing review on
record.

**Why a counter is hard.** The review filename carries the build slug and a per-build record counter,
so the unit is not recoverable from the name; the driver refuses that join in its own source, having
measured it wrong on seven of seven multi-unit builds and right on none. Across fifty-three records,
twenty-four name no unit id and eleven name two or more, the maximum being eleven. Twenty-two carry a
verdict heading and the wild vocabulary includes four spellings outside the method's three. Every
filename-based evasion was replayed against the live predicate and all pass: the sequence is
unbounded, the record tail lets one sequence appear twice, a family-qualified record is ambiguous
with a unit id, and filing the review one folder over changes its kind and hides it from any scanner.

All five inputs to any on-disk counter are written by the run being capped.

### D2 — the run stalls where the method still routes to an owner

The kickoff engine gives each of its six interactive exits a no-owner-turn disposition — three abort,
two park, one replaced by the hand-back — and states that the hand-back is the only one the mandate
buys. That count sits on a mechanical floor.

Three sites AFTER kickoff have no disposition:

- **A unit awaiting owner scope approval.** The playbook's Definition of Ready requires scope
  approval before building. The phrase and the status token appear zero times across all five
  carriers an unattended run reads. The planning verb branches on the status token in exactly one
  place, for the two terminal tokens, so such a unit prints as ready to build.
- **A fork tripping the method's second or third veto.** The text names these owner turns; the park
  sentence that resolves them sits a line further on, attached to a different condition. Two careful
  readers of this research disagreed about whether the disposition exists, which is the operational
  definition of a rule that is not stated.
- **A fork that is a plain question of fact.** No procedure at all.

**The measurement that decided the remedy.** Forty-six resolved forks were read in full across ten
specs, one per build, spanning three nodes and three id families, attended and mandated runs alike.
Classification rule, stated so it can be argued with: a fork is test-decidable only if running
something produces a result from which the winner falls out with no further judgment.

| Class | Count | Share |
|---|---|---|
| test-decidable | 3 | 6.5% |
| test-informed, decided on grounds no test supplies | ~12 | 26% |
| not testable at all | ~31 | 67% |

The three were all fact questions: whether a hook fires for a direct spawn, whether a remote query
returns anything against a bare origin, and whether two derivation rules agree over a population. A
deliberate adversarial hunt for a fourth found none — five further forks carry hard measurements, and
in every one the measurement constrains the option set while the pick turns on credibility, semver,
coverage or trust-model judgment.

**And in one of the forty-six, resolving on the measurement would have picked the wrong answer.** A
cutoff that measured zero misses was refused by name as this repo's own vacuous-selector class. One,
not two — the second example a probe offered is refuted below.

Separately, thirty corpus resolutions already read as agent-delegated, so the fork rule is already
non-asking for everything except the vetoes. Testing aims at the part already automated.

### D3 — the halt vocabulary has one member and no reader

The terminal set holds the landed and aborted members and is a file constant with no conf key, so the
aborted terminal is the only non-landing end a run can reach.

- **Nothing outside the unattended kit reads the phase.** Not the build-index generator, not the
  drift oracle, not the codebase map.
- **All thirteen in-kit readers branch on the terminal binary.** Resume produces byte-identical
  behaviour for the landed and aborted terminals. The one status-specific branch names the aborted
  terminal in order to check LESS, and its own comment says so.
- **The record already carries the reason twice and nothing reads either** — the park helper's kind
  argument, itself the product of a prior review finding, and the free-text reason. The only machine
  that touches the reason is a whole-file grep for the banned bypass flag, whose sole possible effect
  is to red the bar.

Corroborating: the reviews of a prior unattended unit criticised the abort path six times across two
records — a skipped attested item, a reason that wedges the bar, a parked entry mislabelled as a
Definition-of-Done override, a refusal naming the wrong record key. Not one is about the vocabulary.

## 2. The measured cost table

Every verdict below is a real leg result from the scratch-clone experiment, re-verified by an
independent skeptic applying the same diff in a fresh clone. Anything not run says unmeasured.

| Candidate | Files / lines | Legs | Real cost |
|---|---|---|---|
| A new core phase, terminal, with the core floor raised | 2 files, 3 lines | twelve green, none red | **The phase is UNWRITABLE.** The driver's guard refuses it and the refusal names two verbs that cannot write it, proven with a live control showing the branch is the terminal test rather than a special case. The binding protocol's phase list drifts silently — driver at eleven, protocol prose at ten, leg green |
| The same phase left non-terminal | same 3 lines | writable today; one wedged run leaves the leg green | Counts as live forever, so the NEXT run's preflight is hard-blocked and resume tells every future session to carry on |
| A halt reason code as convention only | 0 files, 0 lines | 0 legs move, with a live control | Appending one to a real tracked run-state file left both the unattended leg and the hygiene gate green; a control appending the banned flag reds. The leg reads the file and is genuinely blind to the code |
| A halt code validated against a declared set | unmeasured | unmeasured | Sites enumerated: a conf key and its kit-manifest row, the leg's required-key loop, new driver refusals, a new leg refusal against a fully-armed floor, protocol prose under byte parity, two kit version literals |
| Any new producer verb | 1 file | **measured RED** | Inserting one verb stub with a single refusal made the harness meta-gate print that the branch has no positive assertion naming its own failure text and is not pinned. One armed assertion per refusal branch is the real bill, for every candidate that adds a verb |
| A review counter over review records | unmeasured | unmeasured | No substrate measured to exist — see D1 |

Two legs were unmeasurable on the probe host and red at baseline for environmental reasons not
attributable to any diff, and are reported rather than hidden: the unattended adopter end-to-end test
(a whitespace-path arm plus a symlink-privilege skip) and the drift record check (its base ref does
not resolve inside a clone). Neither has been re-run in the live worktree; doing so is a prerequisite
before trusting the twelve-green line.

The driver's own sibling test took eighteen minutes on the probe host, and a corroborating baseline
run hit a seven-minute timeout with no output. The stall reproduces at baseline with the diff
stashed, so it is environmental — but every driver-side verdict above cost about twenty minutes to
obtain, and any unit adding a verb must budget for it.

## 3. The refuted claims

Recorded because three were load-bearing, and because a probe's recommendation resting on a refuted
premise is the failure mode this pass exists to catch.

| Claim | Why refuted |
|---|---|
| The run-state file is the only artifact an unattended run writes, and the only one a dedicated leg validates | Both halves false. An unattended run writes specs, review records and READMEs — the measured build wrote seven and six — and the hygiene gate validates those at six separate checks. The file may still be a fine seam; the uniqueness argument for it is not available |
| Nothing reads a review record's body | The link-integrity check reads every tracked markdown file under the memory root, and the recall extractor chunks every review body into the retrieval index. The true, narrower fact is that nothing parses the verdict heading and nothing joins a review to a unit |
| The second and third vetoes have no unattended disposition | The park sentence exists one line later, and the method's unattended section names park as one of three substitutes for asking. The disposition exists; what it lacks is proximity, which is why the remedy is to state the collapse where the vetoes are rather than to invent one |
| No gate constrains the parked region | The bypass-flag grep reads the file whole, parked region included — which is precisely why the abort verb refuses a reason spelling the flag |
| Authoring a conforming build folder takes four files and two iterations | An independent rebuild reached green with two files; two shipped builds already stand at two. The first staged attempt red on two separate checks, one of which fired again on the next pass, and the index generator refuses outright on a missing marker pair and on a stray front-matter key. Four iterations, not two |
| The status vocabulary is spelled in four places | Materially wrong as a worklist. The hygiene gate spells the seven tokens three more times and the spec-format document glosses all seven, while one of the four entries is a derived subset rather than a spelling |
| Two of the forty-six forks would have been decided wrongly by their own measurement | One. The companion example chose the option that measured better on the metric the fork states; what was refused there was a different property |
| A non-terminal halt phase wedges the run AND reds the bar | The wedge is real; the red is not. Measured green, because one wedged run leaves exactly one live record and preflight refuses before a second run-state file is ever scaffolded |

## 4. What remains unknown

Carried forward rather than closed, because each would change a unit's cost and none was settled.

1. Whether any producer-verb change keeps the driver's sibling test green. Every candidate that adds
   a verb is unmeasured against it, and the leg costs about twenty minutes.
2. Whether a review denominator exists that the run does not author. The fan-out hook's atomic slot
   ledger is the only named candidate and nobody checked whether its session-scoped key can be
   attributed to a unit or survives across sessions.
3. What the unbounded review loop actually costs. The only datapoint on disk is the six-round build;
   there are no token or wall-clock figures anywhere in the corpus. The honest framing is that the
   cap is justified by the missing blocked-verdict rule rather than by a measured spend.
4. Whether the protocol's phase-list join is cheap. A tracked backlog row carries a written spec for
   it that was never built, and its cost is unmeasured.
5. Whether the driver carries other misdirecting refusal messages. One was found by accident and no
   sweep was run.
6. Whether the two environmentally-red legs are green in the live worktree.

## 5. Where each finding landed

| Finding | Unit |
|---|---|
| the unanchored resolution predicate, in both readers | `TOOL-aBoundedVerdict-4` |
| parking has no verb | `TOOL-aBoundedVerdict-5` |
| the halt vocabulary has one member and no reader | `TOOL-aBoundedVerdict-2` |
| the review loop has no bound and no blocked-verdict rule | `TOOL-aBoundedVerdict-1` |
| the three undisposed stall sites, and the fact-question subclass | `TOOL-aBoundedVerdict-3` |
| the six unknowns in §4 | carried into the specs' gates and open questions, and into backlog rows |
