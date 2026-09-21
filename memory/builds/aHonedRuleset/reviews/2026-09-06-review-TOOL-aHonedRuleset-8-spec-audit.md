**Serves:** spec-audit TOOL-aHonedRuleset-8

# aHonedRuleset — spec audit of unit 8, round 1

*Node `a`, 2026-09-06. Four finder lenses read the rev-5 text of the unit-8 spec, five skeptic
batches were run to REFUTE each candidate, and this is the consolidation. Every surviving claim about
source was re-run against the tree before it was kept. This is the FIRST review this spec has had —
its five siblings were audited twice and this one zero times, so it is graded as fresh surface, not
as a fold. This round grades the SPEC, not the tree; nothing here is a finding about the deployer's
own behaviour except where the spec asserts that behaviour and the assertion is false.*

Subject, pinned at the blob it was read at:

- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-8.md@ea0f9c4adb6748445df67187fe0f80ce3f686a1d`

**ROUND: 1.**

## Verdict: BLOCKED

Two findings block. Both are the same shape and it is the shape this unit exists to attack: **an
instruction that, followed exactly as written, produces a broken artifact that every acceptance
criterion certifies as good.** B1 is the unit's own defect reproduced one layer down — on the runbook
path the spec elevates as load-bearing, the payload lands and no leg runs, and no criterion observes
which of the two outcomes occurred. B2 places S3's anchor where the parity checker re-parents 66
lines of a neighbouring section into it, and both bodies stay non-empty so the checker passes and
AC11 cannot see it.

Five HIGH findings follow, then six MEDIUM and one LOW. The dominant class across the whole set is
not novelty: it is **a rev-3 scope fold that was never carried into the sections that describe the
scope**. Four separate findings are one amendment leaving its other half standing — §5's security
bullet, §10's reuse audit, §10's precedent sentence, and §7's refusal-join negative all still
describe the three-file rev-2 unit, in a spec that now touches six files and writes two Python arms.

Neither blocker requires re-opening a fork. Both are spec edits, and the unit is buildable the
moment they land.

---

## Review shape

Raw findings 36, confirmed 20, refuted 16, unverified 0. Precision 0.56.

Precision 0.56 clears the charter's ~0.5 tighten-first threshold (§8), which is a first for this
build — round 2 over the sibling specs ran 0.38. The difference is the subject: a spec that cites
line numbers, function names and byte figures gives finders something falsifiable to check, and the
skeptic pass killed proportionally less style-grade noise. The finder brief for any round 2 on this
unit should say that the four F4-freshness reports are one defect, not four.

**The 20 confirmed findings are consolidated into 14 rows below.** Four reports (the `WIRE-INTO-PROJECT.md`
byte-identity and anchor-drift cluster) are one defect and are merged into L1; three further pairs are
merged into H3, M1 and M2. That merge is this synthesis pass, not the pipeline's dedup step, whose
own count is stated verbatim below.

## Run integrity

- Lenses: **4 of 4 returned, 0 DIED.**
- Skeptic batches: **5 of 5 returned, 0 DIED.**
- Contradictory verdicts demoted to unverified: **0.** Spurious verdicts discarded: **0.**
  Duplicates: **0.**

No lens died and no batch died, so the zero counts in this run are evidence rather than silence, and
the "also checked and clean" list at the bottom means what it says.

---

## Findings

| # | sev | address | one line |
|---|---|---|---|
| B1 | BLOCKER | §4 "The defect, measured" · §2 S3 | the runbook path yields an ORDERED leg, not an emitted one — the unit's own defect, one layer down |
| B2 | BLOCKER | §8 F4 placement bullet · §4 | the specified anchor placement re-parents 66 lines of the `playbook` section, invisibly |
| H1 | HIGH | §6 AC6, AC7, AC8 | three criteria observe `git diff` with no revision, so they are empty by construction |
| H2 | HIGH | §6 AC11 | cannot fail when the anchor lands with an EMPTY body — the half F4 calls load-bearing |
| H3 | HIGH | §7 refusal-join bullet · §5 testing bullet | `r.fail` IS a counted channel; the negative is stamped "verified" and its mechanism is false |
| H4 | HIGH | §8 F4 final bullet | asks for a backlog row that has existed since 2026-08-24; the run filed a third |
| H5 | HIGH | §8 F1 "overrides a precedent" | the precedent's authority and its M3 veto 2 ground are both misrecorded |
| M1 | MEDIUM | §10 reuse audit | "this unit writes no code" — false since rev-3; the probe was never re-run |
| M2 | MEDIUM | §5 security bullet | "Three declaration edits" against §4's own six-file table |
| M3 | MEDIUM | §10 precedent sentence | says the unit FOLLOWS the fork-B shape; §8 F1 says in bold that it overrides it |
| M4 | MEDIUM | §2 S4/S5, §3, §4 (×7) | `cmd_selfcheck` does not exist; the function is `selfcheck()` at `:976` |
| M5 | MEDIUM | §4 alternatives, bullet 4 | rejected on a carried-prefix ground the list's own bullets disprove |
| M6 | MEDIUM | §8 F1, §8 F4 (×3) | all three `memory/backlog/TOOL.md:<line>` pins now resolve to unrelated rows |
| L1 | LOW | §8 F4 byte/anchor figures | "byte-identical at base and at HEAD" is false; two anchor pins are 11 lines stale |

---

## B1 — BLOCKER · the runbook path yields an ORDERED leg, not an emitted one

**Address:** §4 "The defect, measured", the `--kits` REPLACES paragraph; and §2 S3.

§4 concludes that adding the id to `WIRE-INTO-PROJECT.md:82` is "what makes S1 reach the runbook's
reader". That assumes a `--kits` selection reaching `apply` also gets its gate legs EMITTED. It does
not. `govkit.py:8172-8176` emits a target `[gate_runner]` only when the selection carries an entry
declaring `[gate_runner_seed]`, and that key is declared in exactly one file — `tools/run-gates/kit.toml:105`.
`run-gates` and `gate_runner` appear **nowhere** in `WIRE-INTO-PROJECT.md`: grep returns zero hits.

So an operator following the edited runbook writes a `deploy.toml` with no `[gate_runner]`, `apply`
takes the ordered-not-emitted branch at `govkit.py:5064-5107`, writes the two microformat legs into
`.governance/outbox/gate-legs.md`, prints `gate legs: ORDERED, not emitted`, and exits 0. The payload
lands and no leg runs. That is this unit's own defect, reproduced one layer down, on the exact path
§4 elevates to load-bearing. The deployer's own comment at `:8165` calls that branch "the
silent-green direction this deployer refuses by name everywhere else".

It compounds twice. `cmd_intake` REFUSES to rewrite an existing `deploy.toml`, so the line-82 command
is that target's permanent selection. And every other kit's runbook section carries an explicit
wire-this-leg-into-your-gate-runner-and-CI step — confirmed at `:178`, `:262`, `:351`, `:402`, `:525`
and `:786` — while S3's single sentence carries none.

One sub-claim from the finder is a misread and is not carried: §7's "no adopter receives anything
new" is scoped to the two new ARMS and is consistent with §5's "a default install gains two engine
files and two emitted gate legs". `run-gates` IS in the default selection
(`registry.toml:36`), so the DEFAULT adopter does get emitted legs. The runbook adopter is the one
who does not, and the runbook adopter is S3's entire audience.

**Fix.** State the precondition in §4: the runbook path yields an ORDERED leg because the runbook
installs no gate runner. Then either extend S3 to carry the wiring instruction its six sibling
sections each carry, or record in §3 (OUT) that wiring the runbook adopter's legs is a follow-up row.
Either way add an AC that observes which of the two outcomes a
`--kits playbook,playbook-render,check-microformats` install actually produces.

**Left-shift gate.** A `selftest.py` arm asserting that any selection which installs a `gate_leg`-declaring
entry also carries the one `gate_runner_seed` entry, or else that the ordered-not-emitted branch was
taken deliberately. That is the class: the deployer already refuses two runners loudly and accepts
zero runners silently. Cheaper interim: extend `check_runbook_parity.py` to red when the runbook's
`--kits` example omits the seed entry.

## B2 — BLOCKER · the anchor placement re-parents the `playbook` section

**Address:** §8 F4, the placement bullet ("S3's anchor goes immediately above its own sentence and
not at the end of the file"), read against §4's "the sentence goes beside the `--kits` command it
changes".

`check_runbook_parity.py:71-81` derives a section body as every line from an anchor to the **next
anchor**. The runbook's anchors sit at `:55 :73 :150 :215 :299 :357 :497`. Line 82 — the `--kits`
example S3 edits — is mid-`playbook` section, between `:73` and `:150`. Placing the anchor beside
that command lands it around `:83` and re-parents roughly lines 84 to 149 to `check-microformats`.

The `playbook` section's derived body collapses to the intake command alone. The `adopt-playbook.sh`
invocations, the "Keep the `<!-- governance-template: vN.N -->` marker verbatim" note and the entire
"What the renderer cannot decide for you" list become the `check-microformats` section. Both bodies
stay non-empty, so the liveness half passes, the census still reads 8 anchored sections, and AC11 —
which deliberately asserts only the named line's absence and the census — cannot see any of it.

The spec priced only the end-of-file swallow. The one safe placement, immediately above the
`memory-tree` anchor at `:150`, is the placement its own "beside the command" instruction steers away
from.

**Fix.** Pin S3's placement against the EXISTING anchors rather than against the `--kits` line: the
new anchor goes after §2's content and immediately before `<!-- govkit:entry memory-tree -->`. Add
the observation to AC11 — the `playbook` section's derived body still contains the renderer list.

**Left-shift gate.** `check_runbook_parity.py` grows a third liveness arm: red when a section's
derived body contains a `govkit:entry` id other than its own anchor's, or when an existing section's
body shrinks below a declared floor. The EMPTY-body arm already exists because an anchor with nothing
under it reads as covered; an anchor that STEALS a neighbour's body reads as covered twice and is the
same defect with a bigger blast radius.

## H1 — three acceptance criteria are empty by construction

**Address:** §6 AC7, AC8 (second half), AC6 (second half).

All three observe `git diff -- <path>` with no revision. That compares working tree to index, so it
is empty for every path once the changes are staged or committed. AC8 explicitly stages first — "When
every change is staged … `git diff -- memory/guides/SESSION-KICKOFF.md` empty" — which makes its
own clause a tautology rather than a measurement. §4 Rollout is one commit, so AC7 is empty by
construction at "the end of the unit" too.

The impact is narrower than a first read suggests and the narrowing matters.
`coding-governance-agents.template.md` IS on the manifest `watch:` list
(`memory/guides/SESSION-KICKOFF.md:6`), and `manifest-check.sh` C5 (`:408-419`) fails a staged
watched-path edit with no `last-audit` update — so AC8's FIRST half does guard the charter-template
half of AC7. `AGENTS.md` is only in `verify-paths`, not `watch`, and nothing observes "no `last-audit`
re-stamp was taken". AC6's positive half (`carried-prefix clean`, exit 0) still fails on a rise.

This is not academic on this unit. Measured live today with the gate's own LF-normalised rule,
`coding-governance-agents.template.md` stands at 49144 B against a 49152 ceiling — **8 free bytes** —
and `AGENTS.md` at 64481 against 64512, **31 free**. That headroom is what §8 F3 rests on, and AC7 is
the only thing between it and an accidental charter edit.

**Fix.** Pin every one of these to the diff that actually spans the unit: `git diff --cached -- <paths>`
while staged, or `git diff 94958534..HEAD -- coding-governance-agents.template.md AGENTS.md` after
the commit. AC8 becomes `git diff --cached -- memory/guides/SESSION-KICKOFF.md` alongside the
`manifest-check.sh --staged` exit 0.

**Left-shift gate.** A spec-lint arm over `memory/builds/*/spec/*.md` that reds on the literal
`git diff -- ` inside a §6 acceptance criterion, since a revisionless diff in an acceptance position
is never a measurement. This is a five-line regex over a corpus that already carries a spec template,
and it gates the CLASS — three instances in one spec is a pattern, not an accident.

## H2 — AC11 cannot fail when the anchor lands with an empty body

**Address:** §6 AC11.

AC11 observes the absence of one named line plus the census reaching 8 anchored sections. Neither can
fail when the anchor lands with an EMPTY body — the liveness half §8 F4 itself calls "the half that
makes the anchor mean anything".

`check_runbook_parity.py` collects anchors by line index and appends a distinct `EMPTY body` problem;
`len(anchored)` counts anchors regardless of body. An anchor placed with its sentence ABOVE it, or
immediately before an existing anchor, removes `registry entry 'check-microformats' has no anchored
runbook section`, raises the census to 8, adds an `EMPTY body` problem, and AC11 passes word for
word. AC9's `grep -c` counts lines anywhere in the file and pins no placement, so the sentence and the
anchor both still count toward its threshold of 3. §8 F4 states the placement rule in prose and §6
never observes it.

**Fix.** One clause: the checker's problem count falls from 18 to 17, and NO `runbook-parity:` line
names `check-microformats` at all — not merely the no-anchored-section line. That single observation
covers presence, uniqueness and non-empty body together, and it composes with B2's fix.

**Left-shift gate.** Same arm as B2. Wiring `check_runbook_parity.py` onto the bar at all is
`TOOL-aHonedRuleset-9`, and see H4 for why that row should not be a new one.

## H3 — the refusal-join negative is stamped "verified" and its mechanism is false

**Address:** §7, the `govkit refusal join` bullet; repeated in §5's "testing + left-shift gates"
bullet.

Both sections state that `r.fail` arms add no refusal branch — "S4 and S5 are `r.fail` arms and raise
nothing, so the floor is unmoved" — and §7 markets the claim as verified rather than assumed. But
`refusal_join.py`'s `_is_refusal` matches TWO channels: `raise Refusal(...)` at `:131-134`, and a
bare `<obj>.fail(...)` expression statement at `:135-138`, returning kind `fail`. Its docstring at
`:130` says "The two channels", and the module docstring names them as the exception it raises AND
the finding it appends to a report. The spec cites `refusal_join.py:133` — the raise half — and stops
four lines short of the half that counts its own arms.

Measured live: `refusal-join: 244 branch(es) across 4 module(s)`, exit 0, `BRANCH_PIN = 217` at
`:41`. `fail` sites are the MAJORITY of that population, not outside it. S4 and S5 take it to 246.

The conclusion survives — nothing reds — but for a different reason than the one recorded: the pin is
shrink-only and already 27 behind. Three consequences go unbudgeted. `refusal_join.py`'s pin ledger
convention at `:42-115` shows every prior unit that added refusal branches naming them and stating
armed/unarmed, and no scope item or AC carries that. The join half at `:175-181` would report both new
branches as reached by NO arm the moment a reached-set is passed. And the anchor is
`(module, function, ordinal-within-function)`, so inserting arms mid-function renumbers every later
branch in `selfcheck()` should a reached-set ever be committed.

A negative stated with a false mechanism and stamped "verified" is the false-confidence class charter
§7 names by hand. It also teaches the next reader that `r.fail` sites sit outside `refusal_join`'s
population, which would license skipping arms for a new one.

**Fix.** Rewrite both bullets against the real predicate: `.fail(...)` IS one of the two counted
channels, 244 → 246 is growth, and the shrink-only pin at 217 is why nothing reds. Add the two new
branches to the pin ledger with the arms that reach them (AC16's), the way every prior
refusal-adding unit did, and name the anchor-ordinal consequence.

**Left-shift gate.** `refusal_join.py` already enumerates; give it a `--pin-check` mode that reds when
the ledger's comment block does not account for every branch above the pin. The general form is the
one this build keeps re-learning: a shrink-only floor cannot detect growth, so growth needs its own
observation or it is unrecorded by construction.

## H4 — F4 asks for a backlog row that has existed since 2026-08-24

**Address:** §8 F4, final bullet ("Flagged, explicitly NOT in this unit's scope").

The bullet asks for a new backlog row for a fact that already has two. `TOOL-dScaffoldedMirror-15`
(DEFERRED, `memory/backlog/TOOL.md:234`, verified 2026-08-24) records `check_runbook_parity.py`
exiting 1 with the same 18 problems, zero callers, and absence from `tools/gate-legs.json`.
`TOOL-dRetiredFork-28` (OPEN, `:333`) records the same. And
`memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-unwired.md:42-44`
explicitly DECLINED to re-report it as new *because* that row exists. The spec cites none of the
three.

The run then duly filed a third, `TOOL-aHonedRuleset-9` (OPEN, `:11`), which asserts "That spec asks
for this row by name and this is it" — while the spec names no id. So one measured fact now sits in
three rows with three framings and none cites another. The DEFERRED row's context, that the unwired
checker is the mechanical reason an adopter is never told a kit is deployable and why the live
adoption count is one, is lost to whoever picks up the OPEN one. The next unwired-lens review will
face the same choice a prior review already made and recorded.

**Fix.** Rewrite the bullet to cite `TOOL-dScaffoldedMirror-15` and the 2026-08-30 review that
confirmed it still live, and ask for that row to be re-stamped with AC11's new consequence rather than
for a fresh row. Then fold `TOOL-aHonedRuleset-9` into it, or state on each row what distinguishes the
wiring question from the adopter-discoverability one.

**Left-shift gate.** A backlog-hygiene arm reading `memory/backlog/*.md` for two OPEN rows naming the
same primary path in their trailing `→ <path>` field with overlapping measured figures. Three rows
for one checker is detectable by a `sort | uniq -d` over that field, and this is the second time this
build has produced a duplicate row rather than the first.

## H5 — the overridden precedent's authority and its ground are both misrecorded

**Address:** §8 F1, sub-bullet "It also overrides a precedent, deliberately".

The source mark reads `RESOLVED (agent, 2026-08-18, delegated)`
(`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md:360-364`) and grounds
itself in "Adding the arm inside this spec would change another kit's contract mid-unit, which M3
veto 2 reaches as a governance carrier change". This spec calls it "the earlier ruling" set against
"the owner has ruled the other way here", and quotes `TOOL-aPacedTurnstile-11`'s backlog paraphrase
instead of the source's reasoning, dropping veto 2 entirely.

Two things follow. The spec is scrupulous about mark authority for its own forks — rev-5's preamble
distinguishes three owner marks from one delegated one — and then frames an owner-vs-delegated-agent
supersession as owner-vs-owner, which is a harder override than the one that actually happened. And
the dropped ground is the same M3 veto 2 that rev-5's F2 mark invokes one fork later to discard the
opt-in build. A reader now finds two forks in one spec applying that veto to opposite dispositions,
with nothing recorded about which owner turn cleared it for S4 and S5.

**Fix.** Quote the source mark verbatim with its `(agent, 2026-08-18, delegated)` authority, name M3
veto 2 as the ground the precedent actually rested on, and add one sentence recording that the
owner's 2026-09-04 F1 ruling is the owner turn M3 requires to clear veto 2 for a govkit contract
assertion inside this unit.

**Left-shift gate.** Not gateable as prose. Documented check for the §10 checklist: **when a spec
cites a prior fork as precedent, it quotes that fork's RESOLVED mark verbatim including its
`(actor, date, authority)` triple** — a paraphrase drops exactly the field that decides how much
authority the override needs.

## M1 — §10's reuse audit says the unit writes no code

**Address:** §10 (Reuse audit), closing sentence (spec `:903-905`).

§10 reads "No function seam fits … the extension point is a data row in `tools/govkit/registry.toml`
plus a key in `tools/govkit/entries/check-microformats.kit.toml`, and this unit writes no code." That
was true of rev-2's three-file scope and is false since the rev-3 F1 fold: S4 and S5 write two arms in
`tools/govkit/govkit.py` plus exercising arms in `tools/govkit/selftest.py`. §4's own Rollout line
says so — "Three files at rev-2, six at rev-3" — and rev-3's log enumerates the sections it refolded,
with §10 not among them.

§10 is not a frozen snapshot: `memory/TEMPLATE-SPEC.md:133-135` defines it as the probe result naming
the seam THIS unit extends, and BUILD-METHOD M7 regrounds from it. The one section whose job is to
prove an existing seam was looked for before new code was written asserts that no code is written. The
seam does exist and §4 found it by hand — the `[[exempt]]` empty-reason loop at `govkit.py:1910-1917`,
spelled again at `:1575` and `:2508` — which is precisely what a reuse pass exists to surface.

**Fix.** Re-run the reuse probe for the arm subject (a selfcheck arm grading a descriptor escape
hatch), delete the "writes no code" clause, and carry §4's `govkit.py:1910-1917` / `:1575` / `:2508`
seam and arm 7b into §10 as the function seams the unit extends.

**Left-shift gate.** A spec-lint arm reding when §4's Files-touched table names a `.py` or `.sh` file
and §10 contains "writes no code" — the cheap instance. The class: §10's probe query is stale whenever
§4's file set grew after the last rev that touched §10, which is derivable from the rev log the
template already mandates.

## M2 — §5's security bullet prices three files against §4's six

**Address:** §5, first bullet (spec `:317`).

"security — N/A. Three declaration edits; no write path, no new surface, no credential handling" is
the rev-2 half left standing by the rev-3 fold. Every OTHER §5 bullet was updated to the six-file
scope: perf names two engine files, risks names the two mechanisms, testing names TWO new arms,
rollback says "restores all six files". The security bullet is the one half of the amendment left
behind, four bullets above a risks entry that contradicts it.

The N/A verdict itself survives — `r.fail` arms add no write path — but it is reached from a premise
describing a file set the unit no longer has, in the section a reviewer reads to size the change.

**Fix.** Re-price at six files: two declaration edits, one runbook edit, and two `r.fail` arms plus
their selftest arms — arms that read declarations and write nothing, which is why the verdict stays
N/A.

**Left-shift gate.** Shares M1's gate. One arm covering both: any §5 or §10 sentence stating a file
count that disagrees with §4's Files-touched table row count.

## M3 — §10 says the unit follows the fork-B shape; §8 F1 says in bold that it overrides it

**Address:** §10, the precedent sentence (spec `:908`).

§10 says the `TOOL-aPacedTurnstile-1` §8 fork B precedent was "resolved as the default-selection line
with the arm filed as its own govkit unit — which is the shape §8 F1 follows". §8 F1 (`:485-494`) says
in bold: "It also overrides a precedent, deliberately … The precedent is therefore cited as
OVERRIDDEN, not distinguished". The `which` clause attaches to the file-the-arm-separately
resolution, which is exactly what F1 refused.

Same root cause as M1 — §10 was never refolded after the F1 ruling — but a separate false sentence,
and this one records the answer the owner overruled, in the section a future session greps to learn
whether this build followed or broke the fork-B shape. That is how the still-OPEN
`TOOL-aPacedTurnstile-11` gets re-derived as settled practice.

**Fix.** Restate §10's precedent sentence as OVERRIDDEN per §8 F1, keeping the AC1 two-sided-criterion
attribution, which is unaffected.

**Left-shift gate.** Not mechanically gateable. §10 checklist entry: **when a §8 fork resolves against
§10's recorded precedent reading, §10 is refolded in the same rev.** The rev log already enumerates
refolded sections, so the omission is visible to a reader who thinks to look — which is the problem.

## M4 — `cmd_selfcheck` does not exist

**Address:** §2 S4 and S5, §3 bullet 4, §4 (S4's seam, S5's seam, Files touched) — seven occurrences
at spec `:38 :45 :67 :170 :197 :283 :427`.

`grep -n 'cmd_selfcheck' tools/govkit/govkit.py` returns nothing. The function is
`selfcheck(root, write=False)` at `:976`, and the seven real `cmd_*` functions are `cmd_plan`
(`:2615`), `cmd_check` (`:2832`), `cmd_apply` (`:4243`), `cmd_update` (`:5722`), `cmd_adopt`
(`:7727`), `cmd_intake` (`:8117`) and `cmd_contribute` (`:8469`). The verb dispatches straight to
`selfcheck` with no wrapper.

The spec's interface axis contradicts its own evidence: the seams it cites (`:1350-1353` for arm 7b,
`:1910-1917` for arm 8) both fall inside `selfcheck()`, so the citations are right and the function
name is wrong in seven places, including both scope items and the Files-touched row. A builder who
greps `cmd_selfcheck` finds nothing and re-derives the insertion point, and the live `cmd_` family
makes the wrong name read as a real symbol rather than a slip.

**Fix.** Replace every `cmd_selfcheck` with `selfcheck()` at `tools/govkit/govkit.py:976`.

**Left-shift gate.** A spec-lint arm resolving backticked `<identifier>` tokens that appear beside a
cited `tools/**.py` path: red when the symbol is absent from that file. This is a `grep -c` per token
and it catches the whole class of specs addressed to symbols that do not exist.

## M5 — an alternative rejected on a ground the runbook's own bullets disprove

**Address:** §4, Alternatives rejected, bullet 4 ("Add a runbook bullet to the 'What the renderer
cannot decide for you' list").

The stated reason — "a bullet in that list SPELLS A PATH, which is exactly what the carried-prefix ban
fires on" — is false. Read at HEAD `:89-125`, every bullet in that list names a bare kit directory:
`codebase-map/`, `drift-audit/`, `memory-recall/`, `agent-instructions/`,
`pytest-parallel-guardrails/`, `gate-lint/` (`:115`), `govkit/`, `lexicon/`, `unattended/`. Not one
spells a `tools/` segment. The epoch-2 predicate requires a literal `tools/` prefix AND an extension,
so a bullet in that list's own style matches neither arm — exactly as §4 establishes two paragraphs
earlier for S3's own sentence ("a bare id is not a path and matches no arm").

rev-3 replaced rev-1's wrong reason with a second wrong reason, in a spec whose F3 fork sets the
standard that "a right answer resting on wrong facts is a right answer nobody can re-derive". The
alternative was never priced on its merits, and it is not idle: that list is where an operator
assembles the kit set, which matters more given B1.

**Fix.** Reject bullet 4 on a true ground — the mention belongs beside the `--kits` command it
changes, and F4's anchored form already satisfies `check_runbook_parity.py` — or re-open and price it.
Delete the carried-prefix reason.

**Left-shift gate.** None warranted; a wrong rationale for a correct rejection is not a gateable
class. §10 checklist entry instead: **an alternative rejected on a mechanical ground states the
predicate and one existing instance that the predicate does or does not match.** Both of this
bullet's wrong reasons would have died on contact with that requirement.

## M6 — all three backlog line pins now resolve to unrelated rows

**Address:** §8 F1 and §8 F4, the three `memory/backlog/TOOL.md:<line>` citations.

All three were correct when written — `git show 94958534:memory/backlog/TOOL.md` at 179/245/302
returns exactly the cited rows. At HEAD the shard has taken 55 lines of change and the rows have moved:
`TOOL-aPacedTurnstile-11` to `:185`, `TOOL-dSpentCeiling-4` to `:251`, `TOOL-aScouredKit-23` to
`:308`. A reader following `:179` now lands on `TOOL-aBranchedMandate-12`, `:245` on
`TOOL-dHonouredPark-6`, `:302` on `TOOL-aScouredKit-17`.

This is not a style preference. The repo files this exact class as a defect in two of its own open
rows — `TOOL-aLoosenedCeiling-5` and `TOOL-dSpentCeiling-6` — and charter §5 states the general rule.
The shard is one charter §6 mandates be edited in place, so the pins will keep drifting for as long as
the spec is open. Each pin does sit beside its stable id, which bounds the damage to a wrong landing
rather than a lost row.

**Fix.** Drop the line numbers and cite by id alone — ids are unique and greppable — or cite id plus
status token, as the spec already does for `TOOL-aScouredKit-23`.

**Left-shift gate.** A hygiene arm reding on the literal `memory/backlog/<FAMILY>.md:<digits>` anywhere
under `memory/builds/`. A mutable in-place-edited shard cannot be addressed by line and the ids are
right there; this is a one-line regex with a real population behind it.

## L1 — `WIRE-INTO-PROJECT.md` is not byte-identical, and two anchor pins are stale

**Address:** §8 F4, the "Correction — the byte figure is node-local" bullet and the "option TAKEN"
bullet. *(Four separate finder reports; one defect.)*

F4 asserts "The file is byte-identical at this spec's base and at HEAD". It is not: the blob at base
`94958534` is `0d217e3d` (68069 B) and at HEAD is `22383488` (68747 B), 11 lines added by `36af6f9f`
(`TOOL-aTunedCompass-6`, 2026-09-05 12:33) — during the spec's own life. rev-3 landed at 11:45 the
same day, so the claim was true when written; rev-5 re-stamped on 2026-09-06 and left it standing.
Two of the seven cited anchors moved with it, exactly 11 lines: `memory-recall` `:346` → `:357`,
`push-main` `:486` → `:497`. F4's own correction "59833 B is now 68069 B" is now 68747.

Rated LOW because nothing in the ruling flips. Re-measured live today: the census of 7 anchors holds,
`:82` is unmoved and still the `--kits` example, `:115` resolves, `tools/install-prefix-carried.txt:11`
still records 47, and `bash tools/check-install-prefix.sh` is green at `118 recorded file(s), 5
hand-justified, none rising` — so AC6 and AC11 both still hold as written. The defect is an asserted
byte-identity that is measurably false, and two navigation anchors that land 11 lines short, in the
bullet whose job is to tell the builder the figures need no re-check.

Aggravating: the assertion is pinned against the moving ref `HEAD`, which charter §14 bans outright.

**Fix.** Strike the byte-identical sentence or re-measure it at the tree the unit will branch from,
update the blob size to 68747, and cite the two moved anchors by entry id rather than by line number.

**Left-shift gate.** Same arm as M6, widened: a hygiene check reding on `<tracked-path>:<digits>` inside
`memory/builds/**/spec/*.md` where the path is not the spec's own build folder. The general rule is
already in the charter — "a value stated in prose beside the source that OWNS it rots between changes"
— and this build has now produced six instances of it in one spec (M6's three, L1's two, plus F4's
byte figure).

---

## Also checked and clean

No lens died, so these zeros are evidence rather than silence.

- **AC1 through AC5, AC9, AC10, AC12 through AC16** carry no defect this round. The staged-break
  criteria (AC12–AC15) are notably well built: each has both halves, AC12 stages its break on a
  descriptor the unit does not otherwise edit so the arm is proven over the population rather than
  over its own fix, and AC15 is the criterion proving the specified quantifier shipped instead of the
  literal `default-reachable` reading that would red four innocent entries. That is the charter's
  "a new gate is not landed until its failing case has been observed" rule, applied correctly.
- **S1 and S2** are mechanically sound. `registry.toml:36`'s default selection is a six-id list and
  `check-microformats` is genuinely absent from it; `requires = ["playbook"]` staying put is the right
  call.
- **The §4 seam citations** are all correct at HEAD: arm 7b at `:1350-1353`, arm 8's `[[exempt]]`
  empty-reason loop at `:1910-1917` with the "an omission wearing a label" text, and the same sentence
  at `:1575` and `:2508`. Only the enclosing function's NAME is wrong (M4).
- **§8 F3's byte arithmetic** re-measured live and holds exactly:
  `coding-governance-agents.template.md` at 49144 B against 49152 (8 free), `AGENTS.md` at 64481
  against 64512 (31 free), both under the gate's LF-normalised rule.
- **The `check_runbook_parity.py` census** is 7 anchored sections, 25 registry entries, 0 exempt, 18
  problems, exit 1 — matching the spec's base measurement.

## What a round 2 should carry

Hand the finders the rev log and tell them the four F4-freshness reports are one defect. The
productive lens on this spec was the one that re-ran every cited figure against the tree: eleven of
the twenty confirmed findings are a citation that was true when written and is false now, which is a
measurement problem rather than a reasoning problem and is worth priming for directly.
