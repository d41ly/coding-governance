**Serves:** spec-audit TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3

# aClosedDocket — spec audit of the three-unit set, round 1

*Node `a`, 2026-08-31. A Tier-2 adversarial pass over the three specs: a primed finder fan, a
skeptic stage prompted to REFUTE each finding, one synthesis. Every claim any finding made about
existing code was re-checked at source before it was written down here; where a sub-claim did not
survive that re-check it is named in the finding that carried it.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md@f711e3967c8dad0d3b9e87de370a88121112da15`
- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-2.md@cf1481c46ff032013ae84000f8bfbabf9dbdbbf9`
- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-3.md@8618f59871ec51c6079b489e6a9614d6f77d1b42`

## Verdict: BLOCKED

Three blockers stand. Two of them are on unit 1 and they are independent: the document it edits has
27 bytes of headroom against its own declared budget and no scope item pays for the prose, and a
merge-bar leg already machine-enforces the promotion-only rule that unit 1 exists to relax, so the
first run to take the new disposition reds a leg that cannot then be un-red. The third is on unit 2,
whose new self-test arm writes into the very log the item under test counts. Units 2 and 3 also
carry acceptance criteria that cannot fail — three of them — which is the class §7 names by name.
Nothing here is a disagreement about taste; each blocker is a statement about the tree that was
measured rather than argued.

## Review shape

Raw 51, confirmed 22, refuted 29, unverified 0, precision 0.43. The 22 confirmed findings collapse
to 10 distinct defects, because four independent lenses found the byte budget and four found the
arm-count arithmetic. Precision at 0.43 sits just under the ~0.5 floor §8 sets for adding agents
rather than tightening scope; the refutation rate was concentrated in lenses reading the specs'
prose for rule-conformance rather than checking their claims against source, which is where a
future pass on a document set should tighten first.

| Defect | Raw ids folded in |
|---|---|
| B1 the byte budget | 1, 15, 30, 44 |
| B2 the promotion gate | 29, 42 |
| B3 the arm writes the evidence | 21 |
| H1 the third carrier | 31, 46 |
| H2 the arm's home | 7, 37 |
| H3 the field names | 47 |
| H4 the git dependency | 36 |
| H5 the arm population | 12, 25, 40, 51 |
| H6 the staged break | 13, 41 |
| L1 the dangling `S6` | 3, 19, 33 |

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 1 | §6 AC2, against §2 and §4 Rollout | The budget AC2 re-asserts is already spent — 27 bytes of headroom — and no scope item pays for S1–S3. |
| B2 | blocker | 1 | §4 Inventory, against §7 | `check-unattended.sh` clause 3 machine-enforces promotion as the only disposition, and the file is in no inventory row. |
| B3 | blocker | 2 | §2 S6, §6 AC6, §7 | The new map arm appends to the real lookup log, so the merge bar manufactures the evidence `reuse-probed` counts. |
| H1 | high | 1 | §4 Inventory, the S4 rows | `tools/unattended/SKILL.template.md` restates the promotion rule in full and is not in scope. |
| H2 | high | 2 | §2 S6, §4 Inventory, §6 AC6, §7 | S6's arm is routed to the adopter-instantiated gate file, not the kit self-test; AC6 then grades nothing. |
| H3 | high | 2 | §2 S2, §6 AC1 | The one-reader parity claim is contradicted by the field names S2 pins. |
| H4 | high | 2 | §2 S1, S3 | S1 makes git a dependency of a tool that today makes no git call, and S3's guard does not cover it. |
| H5 | high | 3 | §2 S1, §3 N4, §6 AC3 | "The three arms" and "the other five" reconcile against no counting of the file, so AC3 has no referent. |
| H6 | high | 3 | §6 AC2 | The staged break reds through assertions that already exist and are not in scope, so it cannot distinguish the fix from a deletion. |
| L1 | low | 1 | §5 Testing | The Testing row cites `S6`; this spec defines S1–S5. |

---

### B1 — blocker — unit 1 §6 AC2, against §2 and §4 Rollout

**The defect.** AC2 requires the edited `memory/guides/BUILD-METHOD.md` to still fit its own stated
`≤24 KB` and `≤350 lines`. Measured at the pinned blob: the render is **24 549 B / 317 lines** and
the authored template `tools/memory-tree/BUILD-METHOD.template.md` is **24 560 B / 317 lines**,
against 24 576 B. That is 27 and 16 bytes of headroom. The template's own M1 header states the
condition plainly — the byte half binds first, and the bytes run out near line 316.

S1 adds a whole disposition case, S2 adds the test that selects between the two, S3 adds the record
obligation. At this file's roughly 100 B prose line that is several hundred bytes minimum. §2 holds
no item naming text to displace, and §4 Rollout says "One commit. The change is to a document and a
message; nothing is generated from it and nothing flips" — so no trim is scoped and no cap raise is
scoped either. M3's delegation clause reads, verbatim, that the delegation does not reach veto 2's
governance-carrier clause, *M1's own budget included*, and M1 records every prior raise of the figure
as an owner call. The run therefore hits the wall at its first edit with no ratified exit: break its
own AC, or make an unscoped displacement decision, or raise a budget it is not authorised to raise.

A second, smaller edge: AC2 does not say WHICH file it measures, and the pair differ by 11 B against
16 B of headroom, so the ambiguity is load-bearing rather than cosmetic.

**Fix.** Add a §2 item naming what pays for the new case — the specific M4 or M11 prose displaced,
or an owner-granted budget raise recorded as its own scope item and its own decision. Then restate
AC2 as a delta against a measured base written into the spec: `wc -c` on BOTH
`tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md`, before and after,
each `≤24576`, with 24 560 and 24 549 recorded as the before-figures so the criterion can be checked
rather than believed.

**Left-shift.** A memory-tree hygiene leg that PARSES the `**Budget: ≤N KB, ≤M lines**` line out of
`BUILD-METHOD.template.md` and measures both the template and its render against it, reddening on
breach. M1 currently states the budget beside a file nothing enforces — the exact "a value stated in
prose beside the source that owns it" class §6 names, in the document that teaches it. The leg must
derive N and M from the header rather than carry them, or it becomes the next copy to rot.

---

### B2 — blocker — unit 1 §4 Inventory, against §7

**The defect.** `tools/unattended/check-unattended.sh` already machine-enforces promotion as the ONLY
disposition. Its third review-loop clause (`:246`–`:303`) walks every run-state record, counts into
`nneed` each subject whose review rows carry `NON-CONVERGENT` or `CEILING`, then reds unless the
build README's `gen:build-units` region gained at least that many unit ids the run's pinned BASE
lacked, with the message "so at least one blocker was neither fixed nor promoted". There is no
alternative satisfier: a terminal token does not clear it, and the delta is computed against the
BASE commit rather than against anything the run can restate.

A fold promotes no unit id. So the first run to take S1's new disposition reds that clause — and
reds it permanently, because the `NON-CONVERGENT` row sits on an append-only committed run record no
verb rewrites. `tools/gate-legs.json` carries the script as `unattended kit gate` with
`subject: repo` and no guard, so it runs on every bar in this repo.

Unit 1's §4 inventory does not list the file. No AC runs it. And §7's "what no gate here checks"
asserts the opposite of the truth — it discusses only whether a run chose the RIGHT disposition,
never that a gate constrains which dispositions are legal at all. The unit as specced ships a rule
the merge bar refuses.

The near miss that makes this worse: `aProvenReuse` passed the same clause only because its README
did not exist at its BASE, which took the `rv_readable != 1` path and handed it free ids. That is
luck, not coverage.

**Fix.** Add `tools/unattended/check-unattended.sh` to the §4 inventory with a scope item that makes
clause 3 accept a folded spec-subject exit against an observable the fold actually leaves — the
subject spec's `rev-N` moving since BASE is the natural one, since S1 already makes that the fold's
signature. Add an AC observing a folded `NON-CONVERGENT` exit passing that leg **with a README that
DID exist at BASE**, so the fixture does not reproduce `aProvenReuse`'s accident. Delete or correct
the §7 sentence.

**Left-shift.** A spec-audit checklist entry, because this class is not gateable by a predicate over
the diff: *a unit that edits a RULE greps the tracked checkers for the rule's current wording before
it is written*, and the grep result goes in the §4 inventory. The cheap mechanical half is available
now — `check-unattended.sh` clause 3's failure text should NAME the dispositions it accepts, so the
next reader of a red learns which rule is being enforced instead of inferring it from an id count.

---

### B3 — blocker — unit 2 §2 S6, §6 AC6, §7

**The defect.** S6 asks for a `codebase-map` arm "asserting the row is written", and nothing in the
spec pins that arm to a scratch tree. Run in this repo, `reuse_lookup.py` writes to
`<git-common-dir>/codebase-map/lookups.jsonl` with `worktree` set to the tree it ran in — which is
exactly the row `reuse-probed` counts, and the driver's existing recall arm matches that field with
`grep -xF` against `$ROOT` from `--show-toplevel`.

So a bar run in a worktree deposits, in the shared common-dir log, a row indistinguishable from a
real probe by that worktree. `reuse-probed` becomes unfalsifiable in this repo: a build that ran no
map probe reports MET, silently and forever. The unit whose stated goal is to give the map half
liveness evidence would ship an instrument that manufactures its own evidence. That is the
could-not-fail shape §7 bans, one level up from the arm.

It is a blocker rather than a high because the consequence is not a wrong document, it is a wrong
mechanism: build it as written and the DoD item is worse than before, since it now reports MET with
authority. Severity here is about what ships, not about what the fix costs — the fix is one clause.

§7's "What no gate here checks" names neither this nor the adopter copy that inherits it.

**Fix.** State in S6 that the arm invokes `reuse_lookup.py` with its cwd inside a scratch repo whose
own git common dir receives the row, and that it must never write into the tree under test. Add the
observation to AC6: the real `<git-common-dir>/codebase-map/lookups.jsonl` row count is unchanged
across a full suite run.

**Left-shift.** An arm in the `codebase-map` suite that snapshots the real log's row count before and
after the suite and reds on any delta — it gates the CLASS (any future logging arm), not this one
instance. Generalisable further as a kit-suite convention: a test that exercises a write path
asserts its cwd is under a `mktemp -d` at the moment of the call.

---

### H1 — high — unit 1 §4 Inventory, the S4 rows

**The defect.** A third carrier restates the promotion disposition in full, and it is the one an
unattended run reads first. `tools/unattended/SKILL.template.md:571-573` says: "every blocker still
standing becomes a UNIT of this build: specced at its tier, built, closed. Not parked, not waived,
and not re-reviewed — a promoted unit is audited as a SPEC, which is what makes promotion
terminate." It renders byte-identically to `.claude/skills/unattended/SKILL.md:571`, the file loaded
at `/unattended` step 0.

Both are REGISTERED in `memory/project/method-carriers.txt`, and both rows describe them as
pointers — "the source of the rendered Skill's step 0", "rendered; its step 0 tells an unattended
run to read the method first". Neither appears in §4's inventory; S4 names only `unattended.sh`'s
message, and Q2 covers `PROTOCOL.template.md` alone.

After S1 lands, the Skill a run loads asserts promotion-only for precisely the case M4 will call a
fold. `check-method-carriers.sh` cannot catch it — its own header says it does not read prose. S4's
own rationale, that a run reads the deciding text at the moment it decides, applies with more force
here than at the message S4 does cover. Precedent for the missing row exists one build back:
`aProvenReuse-2`'s inventory carries `SKILL.template.md` and its render as their own rows for the
same kind of prose edit.

Q2 can also be resolved now rather than at build time: `tools/unattended/PROTOCOL.template.md:502`
does restate the disposition, so the answer is yes.

**Fix.** Add `tools/unattended/SKILL.template.md` and its render to the §4 inventory under S4.
Resolve Q2 to yes, citing `PROTOCOL.template.md:502`. Add an AC that greps all four carriers for the
promotion sentence and asserts each hit names both dispositions, with `unattended skill wiring` and
`bash tools/memory-tree/check-method-carriers.sh` both green.

**Left-shift.** Extend `check-method-carriers.sh` from a path registry to a restatement probe: for
each registered carrier whose row calls it a pointer, red if the file carries a distinctive literal
from the rule it points at. That converts an unenforceable convention ("point, do not restate") into
a leg, and it is the gate that would have caught this before the review did.

---

### H2 — high — unit 2 §2 S6, §4 Inventory, §6 AC6, and §7

**The defect.** S6 and AC6 route the map-side arm to `tools/codebase-map/test_codebase_map.py`. That
file is not a kit self-test. It is byte-identical to `test_codebase_map.template.py` (verified with
`cmp`), `adopt-codebase-map.sh:207` copies the template into an adopter's suite, `.codebase-map.conf`
calls it project-owned, and `tools/gate-legs.json` runs it as the `subject: repo`, unguarded
`codebase-map coverage + freshness` leg. The kit's own suite is `tools/codebase-map/selftest.py`,
the `subject: kit` leg, which already holds `test_reuse_lookup`.

Consequences, in order of cost. The shipped kit gains no arm, so every adopter's tree gets none.
`AC6`'s observation — `python -m pytest tools/codebase-map/test_codebase_map.py` passes — is
satisfied whether or not S6's arm exists, since it belongs in the other file: an acceptance criterion
that grades nothing. And a byte-identity that today holds between the copy and the template is
broken by the edit, with nothing to notice.

§7 contradicts AC6 on the same point, naming "the codebase-map kit self-test for AC6". The builder
must guess between two files with different subjects, and one guess is wrong in a way no gate
reports.

One sub-claim from the raw findings did NOT survive re-check and is dropped: `adopt-codebase-map.sh`
leaves an existing gate file in place rather than overwriting it, so an adopter's edit would not be
clobbered on re-adoption. The placement defect stands without it.

**Fix.** Point S6 and AC6 at `tools/codebase-map/selftest.py`, beside the existing
`test_reuse_lookup`. Remove `test_codebase_map.py` from the §4 inventory. Align §7 with AC6.

**Left-shift.** A parity leg asserting `test_codebase_map.py` is byte-identical to
`test_codebase_map.template.py` — nothing enforces that today, and it is the check that turns this
whole class (an edit landing in a generated adopter copy) from a review finding into a red bar. The
kit already runs template-vs-render parity elsewhere; this is the same idiom one file over.

---

### H3 — high — unit 2 §2 S2, §6 AC1

**The defect.** S2's rationale is that the row's fields are "spelled the way the recall log spells
its equivalents, so one reader can parse both without a per-kit branch". The fields it then pins are
`at`, `query`, `worktree` and `n_candidates`. At source, `tools/memory-recall/query.py:1225-1234`
writes the query row as `{type, query, terms, rewritten, k, budget, bytes_emitted, worktree, n_hits,
n_shown}` plus `qid` and `at` from `log_event`. The count is spelled `n_shown` (and `n_hits`), never
`n_candidates` — a fact Q1's own resolution concedes in the same document that pins the other
spelling.

The `type` omission is the more expensive half. The existing reader at
`tools/unattended/unattended.sh:3271` opens with `grep '"type": "query"'` as its FIRST filter, so a
map row carrying no `type` cannot be counted by that idiom without a branch — the branch S2 exists
to prevent. The driver's own comment above that block records that every step of the join was a
review blocker, which is a direct measurement of how expensive this half is to get wrong.

Three of four pinned fields (`at`, `query`, `worktree`) do match. The two that do not are the count
and the discriminator, and they are the two the reader actually touches. AC1 makes the wrong
spelling the graded observable, so AC1 passes on a log S5's single reader cannot parse uniformly.

**Fix.** Spell the map row `"type": "lookup"` plus `n_shown`, so the existing extractor shape carries
over verbatim — or drop "without a per-kit branch" from S2 and state in S5 that the arm reads two
grammars. Update AC1's field list to whichever is chosen.

**Left-shift.** A driver-side arm that reads one fixture row per declared CLI and asserts the keys
the extractor greps for are present in each — a gate on the CONTRACT between the two logs rather than
on either writer. It fails the day a third kit gains a log with a different spelling, which is the
whole reason the parity claim was made.

---

### H4 — high — unit 2 §2 S1 and S3

**The defect.** S1 places the log at `<git-common-dir>/codebase-map/lookups.jsonl`, which requires
`reuse_lookup.py` to resolve a git common dir. It makes no git call today: `grep -nE
'subprocess|git' tools/codebase-map/reuse_lookup.py` returns nothing, and its header promises it
reads only committed artifacts, dossiers and the conf via the repo root. The kit deliberately
supports a tree with no `.git` at all — `selftest.py`'s `test_gate_template_boundary` names a `git
archive` tarball, a docker build whose `.dockerignore` drops `.git`, and a vendored source drop, with
`.codebase-map.conf` as the boundary that survives the export.

S3 tells the builder to copy `log_event`, and `log_event`'s own shape is the trap. At `query.py:755`,
`p = log_path(repo)` sits OUTSIDE the `try`; `log_path` reaches `common_git_dir` at `:205`, which
shells `git rev-parse --git-common-dir` with `check=True`. A `CalledProcessError`, or an empty stdout
yielding a garbage path, is not an `OSError` and is not caught. Copied verbatim, S3's promise that the
lookup "still answers" fails in exactly the export layouts the kit's own selftest defends, and
`main`'s closing guarantee that a RESULT never fails is what breaks.

**Fix.** Extend S3 to cover the LOCATION resolution as well as the write, and state what a tree with
no resolvable git dir does — skip the log, answer normally. Add an AC running the lookup in a
`.git`-less export and observing exit 0 with candidates printed.

**Left-shift.** Add the `.git`-less export case to `selftest.py`'s existing
`test_gate_template_boundary`, which already builds that layout — one more assertion inside a fixture
that exists. It gates the class: any future dependency `reuse_lookup.py` acquires on the environment
reds there.

---

### H5 — high — unit 3 §2 S1, §3 N4, §6 AC3

**The defect.** The arm population does not close over the file under any counting. Measured:
`_t0=$(date +%s)` matches exactly four lines — `unattended.test.sh:4649`, `:4658`, `:4693`, `:4706`
— and the `*_t0=` family matches nine (`3518`, `3521`, `3588`, `3610`, `3651`, plus those four).
S1's own descriptor is an arm that wraps a VERB and asserts a ceiling; that selects exactly TWO,
`:4693` (`run --preflight`, `-lt 25` at `:4696`) and `:4706` (`run --close`, `-lt 25` at `:4709`).
`:4649` and `:4658` wrap `run_bounded` itself, in-process from the sourced copy, against a 20 s
ceiling — a different shape with a different instrument, since there `RB_TOOK` is a live shell
variable and no message parse is involved.

§1's own Goal names exactly two sites, `check_wiring` and the `gates-green` site. The suite's closing
`fi` comment calls them "both assertions above". Backlog row `TOOL-aProvenReuse-6` records "FAILED at
35s, 44s and 66s" as three MEASUREMENTS across those two arms — which is what S4 then re-narrates as
three arms against a 25 s assertion. The arm count is the half that is wrong.

N4's "other five `_t0=$(date +%s)` sites" reconciles with nothing: 3 + 5 = 8 against nine `*_t0=`
sites, or against four exact-literal ones. AC3 then grades "no arm outside the three named in S1
changes" against a set the spec never fixes, by line or by predicate — so the scope boundary N4
exists to draw is not drawn, and a builder can satisfy AC3 while touching a third arm of their
choosing.

**Fix.** Name the arms in S1 by line and by failure-message literal ("the bound does not reach
check_wiring", "the bound does not reach the gates-green arm"), say two rather than three, and move
`:4649`/`:4658` into N4 with their reason — their instrument is already in-process. Restate S4 as
three measurements over two arms, attributed to the assertion each was measured against. Replace
N4's count with its derivation (`grep -c '_t0=$(date +%s)'`) or drop the figure.

**Left-shift.** `check-unattended.sh` already runs arm-count and message-literal gates over this
suite; add a pin on the number of timing sites so any change to the population reds rather than
passing silently. And a spec-audit checklist entry for the general class: **a scope item that names
a count of code sites carries the command that derives it**, which is §7's "no count of a derived
population is written in prose" applied to specs rather than to checkers.

---

### H6 — high — unit 3 §6 AC2

**The defect.** AC2 stages a break — `run_bounded`'s kill path disabled so the bound cannot fire —
and requires the arms to FAIL. They do, but not for the reason AC2 needs. `hit "$out" "the declared
wiring check did not answer within the declared"` already exists at `:4694`, and its `gates-green`
twin at `:4707`; neither is in scope. With the kill path inert the sleeper runs to completion, the
breach message is absent, and those pre-existing assertions red on their own. So AC2's observation is
satisfied whether or not the new instrument was wired — it cannot distinguish the fix from a plain
deletion of the timing line. §5's claim that "AC2 is what proves they can still fail" does not hold.

It gets worse for the `check_wiring` arm specifically. S2 says that where the output carries no
`RB_TOOK`, the arm asserts on the BREACH MESSAGE — which is byte-for-byte the assertion already at
`:4694`. In fact both breach messages already carry `${RB_TOOK}s` (`unattended.sh:1093` and `:2852`),
so S2's fallback condition has no member among the arms in scope: it is either dead scope or
evidence that S1's population is not the one §1 names, which is H5.

Second half: AC2 does not name the artifact it edits. The two verb arms spawn the real script as a
subprocess (`run() { bash "$SCRIPT" ... }`), and `unattended.sh:154` assigns
`GATE_BOUND_LIVE=$REMOTE_BOUND_LIVE` unconditionally after its own probe, so no harness-side env
reaches the child. The mktemp'd `rb_fn` copy the suite extracts at `:4631` IS trivially breakable —
the suite already sets `GATE_BOUND_LIVE=0` on it a few lines later. Staging the break there leaves
both verb arms green and certifies nothing: the class the suite's own comment at `:4612-4614` names,
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`. And the suite's closing `fi` comment
says outright that with the bound inert the arms "red for a property of the box rather than a defect
in the code" — the conclusion §4 tells readers not to draw.

**Fix.** Stage a break only the NEW assertion can see: leave the breach message intact and force the
reported elapsed past the ceiling, patching `RB_TOOK` in the extracted copy the suite already
sources. Name the artifact edited in AC2's text. Require that the pre-existing `hit` assertions still
PASS while the arm fails — that clause is what makes the criterion grade the new instrument rather
than the old one.

**Left-shift.** A recurring-bug-class entry, since `gotchas.py --for-diff` is already the mechanism
that puts these in front of a review: **an AC of the form "with X disabled, the arm FAILS" names the
artifact it edits AND asserts the pre-existing assertions still pass.** The gotcha for the substitute
half already exists; what is missing is the assertion-overlap half, and it is the half that fired
here.

---

### L1 — low — unit 1 §5 Testing

**The defect.** The Testing row reads "S6 in §7's sense"; §2 of this spec defines S1 through S5 and
nothing else, and `S6` appears nowhere else in the file. The sibling spec 2 does have an S6 and its
§5 reads "Testing — S6, both sides", so the shape was copied and the referent was not. A reader
cannot tell whether a sixth scope item was dropped in drafting or the label is a typo for S5.

**Fix.** Repoint the row at the scope item actually meant — S5 carries the version and render
carriers — or, if a sixth item was intended, write it into §2 and give it a criterion in §6.

**Left-shift.** A hygiene check over `memory/builds/*/spec/*.md`: every `S<n>`, `N<n>`, `AC<n>` and
`Q<n>` reference resolves to a label the same document defines. It is a regex, it is one leg, and it
gates the class in a repo whose charter requires pointers that resolve.

---

## What the hunt was pointed at, including where it found nothing

- **Unit 1's veto-2 authority argument.** It holds for S1 and S2 as written: they ADD a case for a
  spec subject and leave the diff-subject rule untouched, which is the row as stated and is N2. It
  does NOT hold for the edit's actual blast radius. B1 forces an unscoped displacement decision or
  an unauthorised budget raise, and H1 shows a fourth carrier the inventory never enumerated. The
  argument is sound about intent and wrong about extent, and extent is what veto 2 governs.
- **Contradiction with the two prior NON-CONVERGENT exits.** None found. `aScouredKit`'s subject was
  a DIFF and its three standing blockers named undone work, so promotion stays correct there;
  `aBoundedVerdict` exited with an empty standing set, so neither disposition applies. N2 states
  this and it survives the cross-read.
- **Is the fold/promote test decidable by a run?** Half. "Closing it edits a document the review was
  already reading" is checkable against the review's own subject. "Needs a MECHANISM this build does
  not have" restates the judgement M2 already asks an author to make, which N4 concedes openly. The
  test narrows the judgement rather than eliminating it; §7's "no predicate reads intent" already
  says so. Recorded as a limit, not filed as a finding.
- **Unit 2's cross-kit boundary.** No coupling found, and this was checked directly: S1 keeps the
  map log under the map kit's own name, N1 refuses a shared file or writer, and neither kit gains an
  import of the other. The `MAP_CLI` declaration set is complete across all five carriers the
  `RECALL_CLI` idiom occupies — driver default (`unattended.sh:290`), `.unattended.conf`,
  `.unattended.conf.example:74`, `kit.toml`'s `optional_keys:38`, and the protocol's key table at
  `PROTOCOL.template.md:546` — and §4's inventory names each. The `not adopted` outcome stays
  reachable and AC5 observes it. The unit's defects are H2, H3, H4 and B3, none of them the coupling
  the row was filed over.
- **Is `RB_TOOK` the right instrument?** Yes, and this was verified rather than accepted:
  `unattended.sh:193` sets it inside the bound's own scope, and both breach messages carry it. Unit
  3's defects are its population (H5) and its staged break (H6), not its choice of number.
- **Criteria that name no observation which could fail.** Three: AC6 in unit 2 (H2), AC3 in unit 3
  (H5), AC2 in unit 3 (H6). **Figures pinned without a derivation:** N4's "other five" and S4's
  attribution of three measurements to three arms, both in unit 3 (H5).

## What this pass did NOT do, said rather than implied

- **It read documents, not code paths.** Every claim a spec makes about existing source was checked
  at that source, which is why B2, B3, H2, H3 and H4 exist. But a spec audit grades what a document
  SAYS; it cannot find the defect a correct-sounding sentence hides in a mechanism nobody has built
  yet. `aScouredKit`'s own spec audit recorded that every blocker its build produced came from
  reading code, and that limit applies here unchanged.
- **No fixture was driven.** Nothing below was observed by running the driver, the suite or the bar.
  `check-unattended.sh` clause 3 was read at source and its behaviour derived from the awk; the fold
  case was not staged. B2's claim would be strengthened by a fixture and is filed as a blocker on
  the strength of the code, which is the weaker of the two evidences.
- **The three specs were cross-read on M2's four axes** — scope, interface, ordering, acceptance —
  and no cross-spec disagreement was found. The units share only the prompt record; they touch
  disjoint files. Every finding here is internal to one spec.
- **Precision was 0.43, below §8's floor.** Reported rather than smoothed. The refuted 29 were
  concentrated in prose-conformance reads, and the correct response by §8's own rule is to tighten
  scope and priming before adding lenses, not to add them.
