# TOOL-aHonedRuleset-5 — the last-audit stamp rule gets exactly one home

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling · order 3 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-6 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-6 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

One rule — how to compute the sha for a kickoff manifest's `last-audit` stamp — is written out in
seven places across five files, in two spellings that already disagree. Reduce it to one prose home
and one machine home, point the rest at them, and gate the pair so the disagreement cannot come back.
Then, in a second commit, fix what the rule SAYS at that single home: `KICK-cSettledDocket-1` records
that the sha it prescribes cannot satisfy the checker's own check 5 on a feature branch.

## 2. Scope (IN)

The items are ORDERED, and the order is load-bearing rather than editorial. S1-S9 land as **commit
A**, which changes where the rule is written and nothing about what it says. S10-S13 land as
**commit B**, which changes what it says. The split is what lets the new parity row be shown to have
caught something: its failing case is observed in commit A over text commit A does not semantically
touch, and observed AGAIN in commit B over the pattern that actually ships. §8 F3 records why a
single commit was rejected and who overruled it.

- **S1** — `skills/session-kickoff/MANIFEST-TEMPLATE.md:29-31` becomes the single PROSE home. Its
  text is unchanged in commit A; S11 rewrites it. Every other prose carrier points at it or at the
  manifest instantiated from it.
- **S2** — `skills/session-kickoff/MANIFEST-TEMPLATE.md:121-124` loses the parenthetical restating
  the rule. The sentence already says "per the stamp rule"; the pointer stays and the restatement
  goes. Its unborn-branch clause is unique content and survives verbatim.
- **S3** — `skills/session-kickoff/SKILL.md:118-119` loses the inline rule. Step 2b's repair
  instruction becomes "sha per the manifest's own stamp rule", which resolves in whatever tree the
  engine is standing in and names no path.
- **S4** — `WIRE-INTO-PROJECT.md:437-439` loses the parenthetical. The step already opens with "per
  the template's Customize notes", so the pointer is already written and only the restatement is cut.
- **S5** — `skills/session-kickoff/manifest-check.sh:265` becomes the single MACHINE home. Its
  `STAMP_SHA_RULE` constant MOVES above line 197 so `RETROFIT` can interpolate it. Its text is
  unchanged in commit A: the no-remote fallback it omits is not written in, because S10 deletes that
  clause from the rule outright. The drift the census found is resolved by deletion, not repair.
- **S6** — `skills/session-kickoff/manifest-check.sh:197` stops re-typing the rule inside `RETROFIT`
  and interpolates `$STAMP_SHA_RULE` instead.
- **S7** — one row joins `PAIRS` in `tools/check-playbook-parity.sh`, comparing the sha expression
  the template STATES against the one `STAMP_SHA_RULE` OWNS. The gate's header gains a line saying
  its pair list is no longer playbook-only and one saying what the row does not cover. Both lines
  carry a pinned anchor so AC7 can observe them: the widening line contains the literal `no longer
  playbook-only`, and the scope-limit line contains the literal `compare the stamp rule's sha
  expression`. Neither string occurs in that file today, measured at 0 apiece. Both anchors are
  worded to survive S11, so commit B does not have to rewrite them.
- **S8** — `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp in commit A, because
  `skills/session-kickoff/SKILL.md` and `skills/session-kickoff/manifest-check.sh` are both watched
  pathspecs on line 6 of that file.
- **S9** — the row's failing case is OBSERVED before commit A lands, per §7 of the charter: the
  `git merge-base <remote>/<default> HEAD` clause in `skills/session-kickoff/MANIFEST-TEMPLATE.md:29`
  is staged with one word changed, `bash tools/check-playbook-parity.sh` is run and must exit 1
  naming the row, and the break is unstaged. This is the last item of commit A and the gate is not
  landed without it.
- **S10** — the semantic fix, commit B. The stamp rule's non-default-branch clause becomes `HEAD`
  too, so the rule reads `sha = HEAD on any branch` — the commit §B was actually verified against.
  The `no remote → git merge-base <local-default> HEAD` fallback goes with it: it existed only
  because `merge-base` needs a remote ref to resolve. §4 states the mechanism and what the change
  trades away.
- **S11** — the fix is applied at the two homes ONLY: the prose home at
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:29-31` and the machine home `STAMP_SHA_RULE`. The four
  carriers S2, S3, S4 and S6 became pointers in commit A and inherit the new text with no edit, which
  is the concrete payoff of doing the single-homing first.
- **S12** — this repo's own instantiated copy at `memory/guides/SESSION-KICKOFF.md:22` is
  re-instantiated to the fixed rule, and that file takes its second `last-audit` re-stamp, because
  commit B touches `skills/session-kickoff/manifest-check.sh` again. Commit B's stamp is written by
  the NEW rule, which is this unit's own dogfood of the fix.
- **S13** — the parity row's extraction is re-anchored onto the fixed sha expression in the same
  commit, its failing case is observed a SECOND time against the shipped pattern, and
  `KICK-cSettledDocket-1` in `memory/backlog/KICK.md` flips to CLOSED naming this unit. Closing it IS
  in this unit: the row records exactly the defect S10 removes, and AC10 is its closing evidence.

## 3. Non-goals (OUT)

- **No change to check 5's logic in `skills/session-kickoff/manifest-check.sh`.** The checker is not
  the thing that is wrong. It reads `LA_SHA` from the WORKING-TREE manifest and derives both the
  watched-change commit and the re-stamp commit from committed history, which is the correct
  question to ask; the rule was telling stampers to write a sha that makes the answer red. S10 is a
  text change at two homes and touches no shell logic.
- **Not adjudicating adopter manifests.** S12 re-instantiates THIS repo's copy because the home it
  instantiates changed. Whether any other adopting tree's manifest is re-stamped is that tree's
  business, and the checker's own failure messages carry the new rule to it.
- **Not editing the charter's merge-exception parenthetical.** `AGENTS.md:140` and
  `coding-governance-agents.template.md:68` both say "post-merge HEAD on the default branch, the
  merge-base otherwise". They are NOT carriers of the stamp-sha rule — the last bullet in this
  section says why, and it governs — but they name the same two shas, so S10 gives them a reason
  to move. That is a real downstream and it is FILED rather than
  fixed here: `TOOL-aHonedRuleset-4` shares `order 3` with this unit and edits that same template,
  and `AGENTS.md` is regenerated from it rather than hand-edited. A new `KICK` backlog row is opened
  at landing, with the id minted then, naming both carriers.
- **No `--stamp-rule` verb on the checker.** `--locations` and `--task-skeleton` exist because a
  consumer needed to read a value at runtime. Nothing needs to read this one at runtime, and the
  parity row extracts from the file with `sed` exactly as the five existing rows do.
- **No seal.** Check 10 byte-compares the manifest's task region against `TASK_SKELETON`. The
  equivalent here is impossible and the checker's own header at lines 40-42 says why. See §4.
- **No cut to `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md:81`.** A landed spec is a
  frozen record and is cited, never edited.
- **No charter edit of any kind.** Those two lines state the MERGE-CONFLICT rule for the stamp line,
  which is a different rule that happens to name the same two shas, so they were never carriers of
  this one. S10 gives them a second reason to move, and the bullet above says why that move is filed
  instead.

## 4. Design

### Inventory

Every carrier, located with `grep -n "merge-base <remote>/<default> HEAD\|merge-base <local-default>
HEAD\|merge-base origin/main HEAD"` over the five files at base `102e98f0`. Byte figures are
LF-normalised and were measured by reading the file in binary and slicing the span, because
`WIRE-INTO-PROJECT.md` and `MANIFEST-TEMPLATE.md` sit CRLF in this Windows working tree while their
committed blobs are LF.

| # | Carrier | Spelling | Bytes | Disposition |
|---|---|---|---|---|
| 1 | `skills/session-kickoff/MANIFEST-TEMPLATE.md:29-31` | full | 234 | the PROSE home, unchanged |
| 2 | `skills/session-kickoff/MANIFEST-TEMPLATE.md:121-124` | full | 135 | cut to the pointer already there |
| 3 | `skills/session-kickoff/SKILL.md:118-119` | full | 180 | cut to a pointer, 83 B replacement |
| 4 | `WIRE-INTO-PROJECT.md:437-439` | full | 135 | cut to a pointer, 29 B replacement |
| 5 | `skills/session-kickoff/manifest-check.sh:265` | SHORT | 100 | the MACHINE home, hoisted in A, rewritten in B |
| 6 | `skills/session-kickoff/manifest-check.sh:197` | SHORT | 83 | interpolates the constant, 17 B |
| 7 | `memory/guides/SESSION-KICKOFF.md:22` | concretised | 104 | re-instantiated in B, see S12 |

**The census undercounted, and its line numbers have moved.** It found four copies in three files.
There are seven in five, and three of the four it named are off by one to two lines. Carriers 5 and 6
are the ones it missed, and they are the interesting ones: the checker already half-owns this rule in
a variable literally named `STAMP_SHA_RULE`, and its spelling omits the no-remote fallback that all
four doc copies carry. The drift the census predicted has already happened, in the file that grades
the contract. That specific disagreement is settled by DELETION rather than repair: S10 removes the
fallback from the prose home, because a rule that no longer resolves a remote ref has no use for a
no-remote branch. Writing the clause into the constant in commit A and deleting it in commit B would
be churn with no reader.

**The census also over-estimated the recovery.** Its cut 4 read "Est. 250-400 B in the kickoff
engine". Measured, the whole duplicated clause in `SKILL.md` is 180 B gross and the pointer costs
83 B, so the net is **97 B**. My measurement wins and the unit's case shifts accordingly: this is a
drift fix that happens to recover bytes, not a byte recovery.

**And the byte half of the case is smaller still once the build's own order is honoured.** At base
`102e98f0`, `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` reports
`18225 / 18432 bytes (207 under, 98.9%)`, against which 97 B would be a 47% rise in free space. But
`TOOL-aHonedRuleset-3` is `order 2`, edits the same `skills/session-kickoff/SKILL.md`, and its own
AC binds it to leave the file at least 1200 B under 18432 — its estimate is a 1237 B recovery,
landing near 16988. So by the time this unit runs the free space is near 1444 B rather than 207, and
97 B is roughly a 7% rise, not 47%. Nothing in this unit's scope changes; the argument for it is the
drift, and the bytes are a rounding error a predecessor already banked.

### Why the floor is two homes rather than one

Three candidate single homes were tested against the tree, not assumed.

**The checker alone cannot be it.** `WIRE-INTO-PROJECT.md` §4 step 2 fills `{{AUDIT_SHA}}`, and step
4 is what copies `manifest-check.sh` into the target. At the one moment the rule is first needed the
checker is not yet in the adopter's tree, so a home reachable only by running it is unreachable
exactly when it matters. A verb would not help; the script is absent.

**The template alone cannot be it either.** A failure message must be self-contained. When check 2
reds because the audit block is missing, or check 3 reds because the stamp is foreign, the manifest
is the thing that is wrong — telling the reader to consult it is worthless. That is why
`STAMP_SHA_RULE` is interpolated into four failure messages today, and why it stays.

**A seal is not available.** Check 10 byte-compares the manifest's `kickoff:task` region against
`TASK_SKELETON`, and the checker's header at lines 40-42 states why that constant lives in the script
and not the template: "the template is a SEED that BECOMES the manifest, so an adopting tree has no
reference copy left to compare against." The same is true here, and worse — instantiation SUBSTITUTES
`<remote>/<default>`, so an adopter's correct manifest is guaranteed not to match the constant
byte-for-byte. Carrier 7 is the live proof.

So the answer is one prose home and one machine home, in the same directory, with a gate holding them
equal in the gov repo where every future edit is made. The adopter's instantiated copy is downstream
of the prose home and the checker's failure message is the backstop when that copy is broken.

**Which of the two `MANIFEST-TEMPLATE.md` copies survives is carrier 1, decisively.** Carrier 2 sits
inside the "Customize before use" block that `WIRE-INTO-PROJECT.md` step 3 orders deleted at
scaffolding, so it does not exist in any adopting tree. Carrier 1 sits in the ratchet section, which
survives instantiation and is the copy every re-stamp reads. Carrier 1 also carries two facts carrier
2 lacks: why a branch sha is refused, and that the datetime always advances. Carrier 2's one unique
fact is the unborn-branch clause, which is scaffolding-time advice, is kept verbatim, and is backed
at runtime by check 3's own message.

### What the fix changes, and what it trades

The rule's non-default-branch clause becomes `HEAD`, so the whole rule reads `sha = HEAD on any
branch`. The mechanism the old clause failed, read out of `skills/session-kickoff/manifest-check.sh`
rather than reproduced here: check 5 takes `LA_SHA` from the WORKING-TREE manifest at line 238, but
derives the last watched-file commit (`git rev-list -1 "$LA_SHA..HEAD" -- watch`, line 294) and the
last re-stamp commit (`git log -G'^last-audit:'`, line 302) from COMMITTED history. Stamping the
merge-base therefore opens a range spanning every branch commit that already touched a watched file,
with the matching re-stamp still sitting uncommitted in the working tree — so the check reds at
exactly the moment a Definition of Done runs it, before the commit that would satisfy it exists.
Stamping `HEAD` closes that range: empty before the commit, and one commit wide after it, where the
watched change and the re-stamp are the same commit and `merge-base --is-ancestor` holds trivially.
`KICK-cSettledDocket-1` records the three attempts that discovered this; it is NOT re-reproduced here,
because the branch this spec is written on has no watched-file commits to reproduce it with.

What the fix trades away is the reason the merge-base was chosen: a branch sha is orphaned by a
squash-merge, and check 3 then reds it as foreign. That cost is already paid for. `AGENTS.md:140`
mandates a fresh post-merge audit and re-stamp after any merge that brought in watch-touching commits,
so the post-squash re-stamp check 3 demands is an obligation the charter already carries — while the
merge-base prophylaxis bought that at the price of a red on every feature branch. One check's failure
is covered by a standing rule; the other's was not.

The no-remote fallback goes with it. It existed only because `git merge-base <remote>/<default> HEAD`
needs a remote ref to resolve, and `HEAD` needs nothing.

### The parity row

`tools/check-playbook-parity.sh` S2 already holds five rows of the shape
`<label>~<stated-file>~<stated-extraction>~<owning-file>~<owning-extraction>`, with the anti-vacuity
arm that reds when either extraction matches nothing. ONE row joins it:

| label | stated side | owning side | value compared |
|---|---|---|---|
| `stamp rule sha` | `MANIFEST-TEMPLATE.md` stamp-rule line | `manifest-check.sh` `STAMP_SHA_RULE` | the sha the rule prescribes |

The compared value is `git merge-base <remote>/<default> HEAD` in commit A and `HEAD` in commit B —
the same row, re-anchored, because the fix changes what the rule prescribes and not what the row is
for. Each extraction captures the value out of its own delimiter, backticks on the template side and
`$(…)` or bare on the constant side, and the loop already strips whitespace, so neither side's line
wrapping matters and `head -1` is not a problem. Capturing from inside backticks inside `PAIRS` is
precedented: the `agent-cap hook matcher` row already backslash-escapes each backtick, which is what
keeps the double-quoted assignment from running a command substitution.

One row rather than two, and the reason is worth stating because rev-2 specified two. A second row
over the no-remote fallback could not be green in commit A — the fallback exists on the template side
and not in `STAMP_SHA_RULE`, so the anti-vacuity arm would red it as unresolvable — and commit B
deletes the clause, so the row would be born and buried in one unit. Commit A therefore covers the
remote form and leaves the fallback uncompared, which is stated plainly rather than left for a
reviewer to find; after commit B the rule has one clause and the row covers all of it.

**What the row does not check**, stated because a structural check reads as a semantic one to
everyone who did not write it: it compares the stamp rule's sha expression. It does not grade the
surrounding prose, it does not grade an adopter's instantiated manifest, and it cannot — see the seal
argument above. It also cannot tell whether the rule is CORRECT, which is the whole subject of S10 and
is exactly the property a byte-parity gate is unable to hold. That sentence goes in the gate's header
beside its existing "WHAT IT DOES NOT DO" paragraph.

### Files touched (estimate)

| Commit | File | Change |
|---|---|---|
| A | `skills/session-kickoff/MANIFEST-TEMPLATE.md` | S2 — delete the parenthetical at 121-124 |
| A | `skills/session-kickoff/SKILL.md` | S3 — the Step 2b pointer |
| A | `WIRE-INTO-PROJECT.md` | S4 — the step 2 pointer |
| A | `skills/session-kickoff/manifest-check.sh` | S5, S6 — hoist the constant, interpolate it |
| A | `tools/check-playbook-parity.sh` | S7 — one `PAIRS` row and two header lines |
| A | `memory/guides/SESSION-KICKOFF.md` | S8 — re-verify §B, re-stamp `last-audit` |
| B | `skills/session-kickoff/MANIFEST-TEMPLATE.md` | S10, S11 — the prose home's new rule text |
| B | `skills/session-kickoff/manifest-check.sh` | S11 — `STAMP_SHA_RULE`'s new text |
| B | `memory/guides/SESSION-KICKOFF.md` | S12 — re-instantiate line 22, second re-stamp |
| B | `tools/check-playbook-parity.sh` | S13 — the row's extraction re-anchored |
| B | `memory/backlog/KICK.md` | S13 — `KICK-cSettledDocket-1` to CLOSED, one new row filed |
| both | `memory/map/features/session-kickoff.md` | dossier prose refreshed on touch; no claim key moves |

No new file, no new gate leg, no inventory key. `tools/gate-legs.json` is not edited, which is why
`memory/map/generated/inventories.json` does not move either.

### Couplings checked and clear

- `skills/session-kickoff/manifest-check.test.sh:617` seeds a fixture from the real template, but it
  compares only the `kickoff:task` region. The ratchet block is not in that comparison.
- `tools/govkit/fixtures/incms-2cff5855.receipt.json` records a `gov_oid` for the template that
  currently equals the live blob. `govkit.py:2924` compares it against gov's blob AT THE RECEIPT'S
  RECORDED COMMIT, not at HEAD, so editing the template does not red it.
- `tools/check-wiring.sh:778` cksum-compares the junction-installed engine against the tracked one
  and will report `UNWIRED` while this branch is unmerged. It is not a gate leg — only the per-kit
  adopters and its own selftest are — so it blocks nothing. Named so the next session does not
  re-derive it.
- `tools/line-length-limits.txt` declares no row for any file here and the gate's default is 450
  characters. Every line touched is under 100.
- The staged leg C5s at `skills/session-kickoff/manifest-check.sh:408-421` survives the fix. It
  compares the staged manifest's `blockstamp` against HEAD's, and `blockstamp` (line 153) captures the
  WHOLE `last-audit:` value, datetime included — so it was never sensitive to which sha the rule
  prescribes, and both commits satisfy it by advancing the datetime alone.
- `AGENTS.md:140` and `coding-governance-agents.template.md:68` are made stale by S10 and are FILED,
  not edited. §3 carries the reason: `TOOL-aHonedRuleset-4` shares `order 3` and owns that file.

### Alternatives rejected

- **A new gate leg for the pair.** A separate script plus a `tools/gate-legs.json` row, to hold one
  data row, when a gate with exactly this mechanism, an anti-vacuity arm and a completion sentinel
  already runs on every bar. Rejected as one more moving part.
- **One commit for the whole unit.** The obvious shape once §8 F3 was overruled, and the one this
  spec's own recommendation warned against: the parity row and a semantic rewrite of the text it
  grades would land together, so the row would never have been green over any text but its own, and
  "the gate caught nothing" would be unfalsifiable. Two commits cost one extra `last-audit` re-stamp
  and buy two observed REDs, one of them over the pattern that ships.
- **Adding the arms to `manifest-check.test.sh`.** That leg is `chunk: selftests, subject: kit`, so
  it is held on the ordinary bar and needs `GATE_SELFTESTS=1`. A session editing the template would
  not run it, which is the green-by-absence class.
- **A conditional check inside `manifest-check.sh`.** It would be dark in every adopting tree, where
  the template does not exist, and would owe an announced skip on every adopter run. The checker is
  adopter-facing and should not carry gov-only logic.
- **Cutting `WIRE-INTO-PROJECT.md`'s copy for the bytes.** The file is 69030 B with no ceiling
  anywhere, so the 105 B is worth nothing. It is cut because it is a fourth prose spelling with no
  gate on it, and because the step already points at the template two clauses earlier.

## 5. Production-readiness checklist

- security — N/A. No write path, no input boundary, no new execution.
- perf / scale — N/A. Two `sed` extractions inside a gate whose declared ceiling is 560 s.
- a11y — N/A. No interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the parity row inherits S2's anti-vacuity arm, so an extraction
  that matches nothing reds by name rather than passing by finding nothing. That arm is also what
  catches a re-anchoring in S13 that misses.
- observability — the failure names the label and prints both sides, per the existing `PAIRFAIL`
  format.
- risks — two. A pointer whose target an adopter has deleted: carrier 1 sits in a section
  `WIRE-INTO-PROJECT.md` never tells anyone to delete, and the checker's failure messages are the
  backstop when the manifest itself is broken. And S10 trades check 5's failure on every feature
  branch for check 3's failure after a squash-merge, which is real but is already an obligation —
  `AGENTS.md:140` mandates the post-merge fresh audit and re-stamp regardless.
- testing + left-shift gates — the `PAIRS` row IS the left shift, and its failing case is observed
  TWICE: in commit A over the unchanged rule text (S9, AC4) and in commit B over the re-anchored
  pattern that ships (S13, AC5). One observation would have graded a pattern the unit then replaced.
- migration / rollback — none for adopters; the fix changes what a stamper writes next, never what an
  existing stamp means. Two commits, each revertable on its own, and reverting B alone leaves the
  single-homing intact.
- user docs — `WIRE-INTO-PROJECT.md` is the adopter runbook and is edited by S4. No `help/` page.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'merge-base <remote>/<default> HEAD' skills/session-kickoff/SKILL.md
  skills/session-kickoff/MANIFEST-TEMPLATE.md WIRE-INTO-PROJECT.md` runs at commit A, the only hit is
  `MANIFEST-TEMPLATE.md:29`. It is observed at commit A and not later, because S10 removes that
  string from the prose home too.
- **AC2** — `wc -c skills/session-kickoff/SKILL.md` is taken immediately BEFORE this unit's first
  edit and again after commit A; the second figure is at least 90 bytes smaller than the first.
  Stated as a DELTA and not as an absolute against 18432, because `TOOL-aHonedRuleset-3` is `order 2`
  and edits the same file: an absolute threshold is satisfied by that unit alone and never observes
  this unit's 97 B. Separately, the `skills/session-kickoff/SKILL.md` row of
  `tools/template-size-highwater.txt` equals that second figure — the bump-down §8 F1 resolves — and
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` emits no `TEMPLATE-SIZE WARN`
  line.
- **AC3** — When `grep -c 'STAMP_SHA_RULE=' skills/session-kickoff/manifest-check.sh` runs it returns
  `1`, and `grep -n 'STAMP_SHA_RULE' skills/session-kickoff/manifest-check.sh` shows the assignment
  above the `RETROFIT=` line with `RETROFIT` interpolating it.
- **AC4** — The FIRST observed RED, in commit A and over text commit A does not semantically change.
  When the `git merge-base <remote>/<default> HEAD` clause in
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:29` is staged with one word changed, `bash
  tools/check-playbook-parity.sh` exits 1 and its output names `stamp rule sha`; the break is then
  unstaged. Without this observation the row is not landed (§7 of the charter).
- **AC5** — The SECOND observed RED, in commit B and over the pattern that ships. After S13
  re-anchors the row onto the fixed sha expression, the same stage-break-unstage is repeated against
  the rewritten `skills/session-kickoff/MANIFEST-TEMPLATE.md` stamp-rule line, and `bash
  tools/check-playbook-parity.sh` again exits 1 naming `stamp rule sha`. AC4 alone would have graded
  only a pattern this unit then replaced.
- **AC6** — When `bash tools/check-playbook-parity.sh` runs on the unmodified tree it exits 0 and
  prints the `pairs in agreement` line, at BOTH commits.
- **AC7** — When `grep -c 'no longer playbook-only' tools/check-playbook-parity.sh` runs it returns
  `1`, and `grep -c "compare the stamp rule's sha expression" tools/check-playbook-parity.sh` returns
  `1`. Both return 0 at base `102e98f0`, measured, so this observes S7's two header lines — which
  AC4, AC5 and AC6 do not reach, since those grade the `PAIRS` row only. Both counts hold at commit B
  as well, which is why the anchors are worded without `merge-base` in them.
- **AC8** — After commit B, `grep -rn 'merge-base <remote>/<default> HEAD\|merge-base
  <local-default> HEAD' skills/ WIRE-INTO-PROJECT.md memory/guides/SESSION-KICKOFF.md` returns
  nothing, and `grep -c 'HEAD on any branch' skills/session-kickoff/MANIFEST-TEMPLATE.md
  skills/session-kickoff/manifest-check.sh` returns `1` for each — the fixed rule at both homes and
  the old spelling nowhere.
- **AC9** — When `bash skills/session-kickoff/manifest-check.test.sh` runs it exits 0 after each
  commit, so the constant's hoist and then its rewrite broke no fixture and the shipped-seed arm
  still passes.
- **AC10** — When `bash skills/session-kickoff/manifest-check.sh` runs after commit B, on this
  FEATURE branch, it exits 0 with commit B's `last-audit` stamp written by the new rule. This is the
  closing evidence for `KICK-cSettledDocket-1`, which records that same run failing check 5 under the
  old rule at a cost of three attempts.
- **AC11** — When `grep -n 'cSettledDocket' memory/backlog/KICK.md` runs, the row leads with `CLOSED`
  and names `TOOL-aHonedRuleset-5`, and one new `KICK` row is present naming `AGENTS.md:140` and
  `coding-governance-agents.template.md:68` as the carriers the fix leaves stale.
- **AC12** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary it is green, with the
  `playbook parity`, `kickoff-manifest ratchet` and `kickoff engine size <=18KiB` legs all reported.

## 7. Gates

- `playbook parity` — `bash tools/check-playbook-parity.sh`. The leg this unit extends. `subject:
  repo`, unguarded, so it runs on every bar.
- `kickoff engine size <=18KiB` — `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed TWICE, once per
  commit: commit A edits two watched pathspecs and commit B edits one of them again.
- `manifest-check self-test` — `bash skills/session-kickoff/manifest-check.test.sh`. Guarded on
  `skills/session-kickoff/`, `chunk: selftests`, so it needs `GATE_SELFTESTS=1` and this unit's DoD
  owes that run because it edits the kit.
- `playbook parity selftest` — `bash tools/check-playbook-parity.test.sh`. Same guard shape; the new
  row uses the already-covered check 7 arm, and AC4 and AC5 supply the row-level failing cases.
- `line length`, `memory hygiene` and the rest of the bar — no new leg is added.

## 8. Open questions

- **F1 — does the high-water record move down?** `tools/template-size-highwater.txt:3` holds
  `skills/session-kickoff/SKILL.md 18215`, and at base `102e98f0` the gate WARNs
  `18215 -> 18225 (+10)`. **That WARN is not this unit's to clear.** `TOOL-aHonedRuleset-3` is
  `order 2` on the same file and lands it near 16988, below the mark, so the WARN is already gone
  before S3 runs; S3 then takes it near 16891. The question this fork settles is therefore not "does
  the WARN clear" but "does the recorded mark follow the file down", and it is asked HERE because
  unit 5 is the LAST unit in this build to touch that file — a `--bump` taken at order 2 records a
  figure order 3 immediately supersedes. `--bump` writes the current measurement unconditionally, so
  it can lower as well as raise.
  **Recommendation: bump it down in the same commit, to the post-S3 measurement.** The ratchet exists
  to price growth against the last deliberate measurement, and leaving 18215 standing quietly hands
  back roughly 1324 B of headroom this build just bought — most of it unit 3's, which is the reason
  to record it rather than let it evaporate. It is a merge-bar knob either way, so the owner rules.
  **RESOLVED (owner, 2026-09-04): bump the high-water down, in the same commit, to the post-S3
  measurement.** Matches the recommendation. The bump rides commit A, which is the commit S3 lands
  in, and AC2 observes the row equal to the post-commit `wc -c` with no `TEMPLATE-SIZE WARN`. Commit
  B does not touch `skills/session-kickoff/SKILL.md`, so one bump is the whole obligation.
- **F2 — do the two rows belong in `check-playbook-parity.sh`?** Its header says "the playbook's
  claims about THIS repo" and S2 is described as "a value the playbook STATES". A row whose stated
  side is `MANIFEST-TEMPLATE.md` widens that subject, and the leg is named `playbook parity`.
  **Recommendation: take the rows and widen the header, do not rename the leg.** The mechanism is
  general, the cost is two data rows against a whole new script, and a leg rename touches
  `tools/gate-legs.json` and the timing cache keyed by leg name for no reader benefit. If the owner
  prefers the narrow reading, the fallback is a `stamp-rule parity` leg of its own, which is the
  rejected alternative in §4 and costs a file.
  **RESOLVED (owner, 2026-09-04): take the row into `tools/check-playbook-parity.sh`, widen that
  script's header sentence to describe its real subject, and do NOT rename the leg.** Matches the
  recommendation. S7 lands the row and both header lines in commit A; the leg name in
  `tools/gate-legs.json` is untouched, so the timing cache keyed by it is untouched too. The row
  count fell from two to one for a reason unrelated to this fork — see F3 and §4.
- **F3 — should this unit also fix what the rule SAYS?** `KICK-cSettledDocket-1` is OPEN and records
  that stamping the merge-base fails the checker's own check 5 on a feature branch, at a cost of
  three attempts. The rule is about to have one home, so fixing it here would be cheap.
  **Recommendation: no.** One mechanism per unit, and a byte-parity gate landed in the same commit as
  a semantic change to the text it grades cannot be shown to have caught anything. Land this, then
  file the fix against the single home.
  **RESOLVED (owner, 2026-09-04): fold the `KICK-cSettledDocket-1` fix in. This goes AGAINST the
  recommendation directly above, which is kept visible because its objection is real and does not
  disappear by being overruled.** The objection is answered by SEQUENCING rather than by waving at
  it: §7 of the charter says a new gate is not landed until its failing case has been observed, so
  the unit splits into two commits. Commit A single-homes the rule and lands the parity row, whose
  RED is staged and observed over text commit A does not semantically change (S9, AC4). Commit B
  applies the fix, re-anchors the row onto the new text, and observes the RED again over the pattern
  that actually ships (S13, AC5). Two observations, one of them on the shipped pattern, is what the
  recommendation said a single commit could not buy. Closing `KICK-cSettledDocket-1` is in this unit
  (S13), its closing evidence is AC10, and the one carrier the fix leaves stale — the charter's
  merge-exception parenthetical — is filed rather than edited because `TOOL-aHonedRuleset-4` shares
  `order 3` and owns that file.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Carrier census re-run against source at base `102e98f0`; found
  seven carriers rather than the four the prose census reported, corrected three of its four line
  numbers, and measured the `SKILL.md` recovery at 97 B net against its 250-400 B estimate.
- rev-2 · 2026-09-04 · folded the spec audit
  ([2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md)),
  four findings addressed to this unit. **A2** — AC2 was an absolute against 18432 that
  `TOOL-aHonedRuleset-3` satisfies alone at `order 1`; it is now a ≥90 B delta against a `wc -c`
  taken immediately before this unit, and its no-WARN clause is restated to hold under either branch
  of §8 F1. **P6** — §4's headroom case and F1's arithmetic were both computed at base and ignored
  that unit 3 lands first: the free space this unit inherits is near 1444 B, not 207, so 97 B is a 7%
  rise rather than 47%, and F1's `18128` became `16891` with unit 3 named as the mover. **P7** — S7's
  two header lines had no criterion; they now carry pinned anchors and new AC6 greps both, which
  renumbered the old AC6-AC8 to AC7-AC9. **P3** — §7's `memory-tree hygiene` corrected to the leg
  `tools/gate-legs.json:1021` actually declares, `memory hygiene`.
  Re-measured at source rather than taken from the report: `SKILL.md` 18225 B, the high-water row
  18215, unit 3's recovery estimate 1237 B against its own ≥1200 B floor, and both AC6 anchor strings
  at 0 occurrences in `tools/check-playbook-parity.sh`. Every §8 fork stays UNRESOLVED and unsigned.

- rev-3 · 2026-09-04 · the owner ratified all three §8 forks; header gains `ratified 2026-09-04` and
  the order verb moves from `order 2` to `order 3`, sharing that step with `TOOL-aHonedRuleset-4`.
  **F1** — bump down, as recommended; AC2 gains the high-water clause and its "holds under either
  branch" hedge is gone. **F2** — rows taken into `tools/check-playbook-parity.sh`, header widened,
  leg not renamed, as recommended. **F3** — the `KICK-cSettledDocket-1` fix is folded IN, against
  this spec's recommendation, and the recommendation is kept visible because its objection stands.
  That ruling drove every other edit in this rev. §2 became an ORDERED two-commit sequence and gained
  S9 through S13: the observed RED, the semantic fix, its application at the two homes, the
  re-instantiation of `memory/guides/SESSION-KICKOFF.md:22`, and the row's re-anchoring plus the
  backlog closure. §3 lost the two non-goals the ruling reversed and gained three: no change to check
  5's logic, no adjudication of adopter manifests, and no charter edit, that last one filed as a new
  `KICK` row because `AGENTS.md:140` and `coding-governance-agents.template.md:68` are made stale by
  the fix and `TOOL-aHonedRuleset-4` owns that file at the same order. §4 gained
  `### What the fix changes, and what it trades`; its parity subsection went from two rows to ONE,
  because a second row over the no-remote fallback cannot be green in commit A and is deleted by
  commit B; S5 no longer repairs the constant, since S10 deletes the clause the repair would have
  added; the files-touched table is now per-commit; the C5s staged leg and the charter carriers
  joined the couplings; and one-commit-for-the-whole-unit joined the rejected alternatives. §5
  restated the risk and left-shift lines. §6 went from nine criteria to twelve, splitting the observed
  RED into AC4 and AC5 and adding AC8 (the old spelling gone, the new one at both homes), AC10 (the
  checker exits 0 on a feature branch, the closing evidence for `KICK-cSettledDocket-1`) and AC11 (the
  backlog rows). AC7's second anchor changed from `compare two git merge-base invocations` to
  `compare the stamp rule's sha expression` so it survives commit B; re-measured at source, that
  string occurs 0 times in `tools/check-playbook-parity.sh` today, as does `no longer playbook-only`.
  Also re-verified at source: `skills/session-kickoff/SKILL.md` at 18225 B, the high-water row at
  18215, and the check-5 line numbers now cited in §4 (238, 294, 302).

- rev-4 · 2026-09-04 · §3's third bullet said the charter parenthetical states a rule "which S10
  supersedes" while its last bullet said those lines "were never carriers of this one". The last
  bullet is the correct one; the third now defers to it instead of contradicting it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "one rule stated in several documents with the source that
owns it"` ranked `kit-dogfood-parity.PAIRS [build-method]` and `check-playbook-parity.sh [playbook]`
among its affordance-seam hits. That is the seam this unit extends: `tools/check-playbook-parity.sh`
S2 holds a declared `PAIRS` list of exactly this shape, with an anti-vacuity arm and a completion
sentinel already built, and its in-script comment records that the list is in-script rather than a
data file because it "reuses the seam kit-dogfood-parity.PAIRS already establishes". Two rows join it
and no new mechanism is built. The probe also surfaced
`manifest-check.sh [session-kickoff]` as a seam, which is the second half of the answer: that script
already owns `MANIFEST_LOCATIONS` and `TASK_SKELETON` as single homes for values that used to be
spelled across several files, and `STAMP_SHA_RULE` is the third instance of the same pattern in the
same file.

Recall terms used: `python tools/memory-recall/query.py "why does the last-audit stamp sha rule live
where it does, and what decided the kickoff kit's single-home pattern" --terms "last-audit stamp rule
merge-base manifest-check MANIFEST-TEMPLATE single source kickoff engine restatement drift playbook
parity PAIRS"`. Thirty-six hits; the two that changed this design are `KICK-cSettledDocket-1` in
`memory/backlog/KICK.md:4`, which the owner's F3 ruling pulled INTO scope as S10 through S13, and
`memory/guides/SESSION-KICKOFF.md:16`, which is how the seventh carrier was found.
