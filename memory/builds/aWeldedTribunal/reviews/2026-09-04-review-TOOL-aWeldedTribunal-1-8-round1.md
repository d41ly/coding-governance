**Serves:** spec-audit TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Spec audit — aWeldedTribunal, round 1

Tier-2 adversarial spec review of the eight-unit spec set, run before any build pass. Fan of primed
finder lenses over the spec set and the sources it claims about, then a skeptic pass prompted to
REFUTE each finding, then this synthesis. Findings below are the survivors; every source claim in
them was re-checked against the tree while writing this report.

**Range — ROUND 1**, subjects pinned at these blobs:
`memory/builds/aWeldedTribunal/spec/2026-09-04-spec-TOOL-aWeldedTribunal-1.md@aff203366d74` ·
`…-2.md@54159465d1df` ·
`…-3.md@a9619630078e` ·
`…-4.md@bc3b031ebdba` ·
`…-5.md@2c8da6e14bea` ·
`…-6.md@5e022309a157` ·
`…-7.md@6a9ca69800ac` ·
`…-8.md@9f0557966cba`

## Verdict: BLOCKED

Two blockers, and each is a case where building the spec faithfully produces the outcome the spec
was written to prevent. `TOOL-aWeldedTribunal-7`'s resolved Option A reds `check-wiring.sh --check`
on a condition its own section 4 documents as normal, which is the behaviour section 8 vetoed Option
B for. `TOOL-aWeldedTribunal-4`'s S3 builds a scanner an owner ruling already refused, with a
predicate a comment satisfies. Neither is repairable by a builder judgement call: one needs a
severity decision written into S2, the other needs an owner reversal or the scope item dropped.

Everything else is repairable in place with the edits named below. Nothing here says a unit is a bad
idea; twelve of the fourteen non-blocker findings are acceptance sets that cannot observe the scope
item they belong to.

**Review shape:** raw 46 · confirmed 20 · refuted 26 · unverified 0 · precision 0.43.

Precision 0.43 is at the bottom of the useful band. Read that as a signal about the target: eight
specs, all repairs to a hardened tree, is exactly the "over hardened code it manufactures refuted
noise" surface §8 warns about — but the two blockers and the acceptance-coverage class justify the
run on their own.

**Collapsed.** The 20 confirmed findings are 16 distinct defects here. Four collapses: `21`+`25` are
one omission (the sixth loop predicate) and `25` supplies the behavioural chain; `14`+`26` are one
defect (spec-2's AC1 cannot reach its own mechanism) reached from two directions; `17`+`20`+`40` are
one defect (the `GATE_SELFTESTS` hold) at six sites, of which `40` is the general statement.

One correction to the merged evidence, since it is load-bearing: finding `14` reads `ok`/`markedWhy`
together and cites `:719` as a `markedWhy` site. Verified — `grep -n markedWhy tools/hooks/agent-cap.js`
returns writes at 769/777/847 and exactly ONE read, at `:918`. `:719` reads `ok`. Finding `26` has it
right; the merged finding uses `26`'s account.

| # | Sev | Unit | Address | Defect |
|---|-----|------|---------|--------|
| B1 | BLOCKER | 7 | §8 F1 / §3 non-goal 1 | Option A reds `--check` — it ships Option B's behaviour |
| B2 | BLOCKER | 4 | §2 S3/S4, §6 AC2 | Builds the scanner `TOOL-dTieredTribunal-9` refused |
| H1 | HIGH | 6 | §4 "Where the gap set comes from" | `coverage_rows` does NOT honour the decline registry |
| H2 | HIGH | 2 | §6 AC1 vs §2 S3 | The one isolating criterion exercises unit 1's mechanism |
| H3 | HIGH | 1 | §2 S1, §4 Inventory | SIX loop predicates, not five — `:910` omitted, and it fails open |
| H4 | HIGH | 3 | §2 S4 | Rule 4's fallback is observed by no criterion |
| H5 | HIGH | 7 | §2 S3 | The `pre-commit` half of the comparison is observed by no criterion |
| H6 | HIGH | 4 | §2 S5 | The derived-population requirement is observed by no criterion |
| H7 | HIGH | 1,2,3,5,6,7 | §7 (and 7's AC6) | Six specs nominate legs the named gate command HOLDS |
| H8 | HIGH | 2 | §2 S1 vs §4 | The "existing" verb list has six verbs, not the seven claimed |
| H9 | HIGH | 4 | §3 non-goal 3 | False premise — the conflicts counter exists and is logged |
| H10 | HIGH | 5 | §2 S1, §4 Inventory | A SIXTH `.memory-tree.conf` reader, in the host module |
| H11 | HIGH | — | `README.md` bullet 4 + roster row 6 | README says unit 6 LANDS; the unit says it REPORTS |
| H12 | HIGH | 7 | §2 S1/S3, §4 Liveness | Unbounded UNKNOWN for any adopter with no tracked pre-push |
| M1 | MEDIUM | 7 | §2, §5 user docs | The gotcha record still says this check was not written |
| L1 | LOW | 5 | §6 AC1 | "four of them" — it is five |

---

## B1 — BLOCKER · unit 7 · §8 F1 (Option A) and §3 first non-goal

Option A's "no exit-code change beyond the existing unwired tally" is not a no-op. `unwired` is
precisely what decides the exit code: `tools/check-wiring.sh:809` is
`[ "$unwired" = 0 ] && exit 0 || exit 1`, and the script's own header says only `UNWIRED` gates.
S2 and AC1 mandate an `UNWIRED`-class line for a divergence, and AC3 counts an unreadable side as
unwired.

So a planted divergence makes `bash tools/check-wiring.sh --check` exit 1 — on the condition section
4 documents as a NORMAL state of this layout, and section 8 vetoes Option B for redding on. The
resolved option delivers the vetoed behaviour under the accepted option's name.

The consumer is not hypothetical. `.unattended.conf:38` is
`WIRING_CHECK="bash tools/check-wiring.sh --check"`, so every unattended run's wiring precondition
refuses whenever the primary tree is parked on a branch that touched `.githooks/`. The header even
names the severity written for this case: `note`, for a condition that is TRUE and worth printing
but is not dormant wiring.

**Smallest fix:** say in S2 that the divergence line uses the non-gating `note` severity and does
NOT increment `unwired`, and add an AC that `--check` still exits 0 over a planted divergence.
Otherwise re-open F1 and record that Option A as scoped is a red, with the unattended `WIRING_CHECK`
consumer named as the party it blocks.

**Left-shift:** an arm in `check-wiring`'s self-test that plants one instance of each non-`UNWIRED`
severity and asserts `--check` exits 0 — the severity vocabulary's gating half, gated. It is the
class, not this instance: any future check that reaches for `UNWIRED` when it means `note` reds.

## B2 — BLOCKER · unit 4 · §2 S3 and S4, §4 "The criterion…", §6 AC2

S3 builds the scanner the owner explicitly ruled against. `memory/DECISIONS.md:116` records
`TOOL-dTieredTribunal-9`: "the left-shift M8 owed for the closing review's D1 and D2 is a
`memory/gotchas/` RECORD, not a scanner (owner, 2026-08-26)". The gotcha this unit cites,
`memory/gotchas/degradation-known-but-unreported.md`, gives the reason under "The fix" and names this
exact predicate shape: a rule that every returned counter must appear in a prompt string is
satisfiable by a comment.

Section 4's predicate is weaker still — assert the literal `RUN INTEGRITY` appears in the file — and
a comment carrying those two words satisfies it. AC2's staged break therefore proves only that
deletion reds; any restoration greens it, comment included. The gate cannot fail for the reason it
exists.

The spec cites the gotcha as its class in section 5 and never cites the ruling that governs it, so
it reverses a ratified owner decision without superseding it per the charter's own record rule.

**Smallest fix:** cite `TOOL-dTieredTribunal-9` and the record's "The fix" in section 3, then either
get an explicit owner reversal before building S3/S4/AC2, or drop them and left-shift as the record
the ruling names. If the criterion survives a reversal, its predicate must assert what AC1 asserts —
that `lensesDead`, `skepticsDead`, `spurious` and `duplicates` are INTERPOLATED into the synthesis
prompt string — never that a literal appears in the file.

**Left-shift:** a spec-lint arm that is genuinely derivable — run `gotchas.py --for-diff` over the
paths a spec's §4 inventory names, parse every `FAMILY-slug-seq` id out of the SELECTED records'
bodies, and red when one of those ids appears nowhere in the spec. It fires on this instance today:
the record is anchored on `tools/workflows/`, spec-4's inventory names `tier2-review.js`, the record
names `TOOL-dTieredTribunal-9`, and the spec never cites it. What it does NOT check: whether the
citation engages with the ruling. That stays a documented check.

---

## H1 — HIGH · unit 6 · §4 "Where the gap set comes from"

Section 4 asserts `coverage_rows` "honours the decline registry". It does not. Its body
(`tools/govkit/govkit.py:2296-2305`) filters on `kind == "write"`, `not missing` and
`dest not in tracked(target)` — no decline lookup anywhere. Both existing call sites do the grading
themselves: `:2673` computes gaps then calls `decline_findings` at `:2679` and prints `GAP` only
where the decline lookup is `None`; `:2869-2870` does the same for `check`.

The claim is load-bearing: S1 reuses the predicate and §4 says "This unit is call site three and
adds no predicate". Built faithfully, `update` prints every deliberately-declined file as a gap and
S3 pins the summary to INCOMPLETE permanently for any target with a decline registry. That is the
crying-wolf failure the decline contract's own header (`:2308-2321`) says makes an operator stop
running the report — applied to the verb operators run most.

**Smallest fix:** correct the sentence, and add a scope item wiring `decline_findings` into the
update call the way both existing call sites do (it also needs `commit_now`, and it grades
staleness). Or state as an explicit non-goal that `update` reports raw gaps, and adjust S3 so a
fully-declined gap set does not report INCOMPLETE.

**Left-shift:** a `govkit selftest` arm over a fixture target whose only gap is declined — `update`
must print no `GAP` row and must summarise COMPLETE. One arm covers all three call sites' shared
contract, and a fourth call site that forgets the grading step reds on arrival.

## H2 — HIGH · unit 2 · §6 AC1, against §2 S3 and §4

AC1's script exercises none of this unit's mechanism. `markedWhy` is read at exactly one place,
`agent-cap.js:918`, inside the `hit.kind === 'iter'` arm. `ITER_CALL` (`:426`) is
`map|flatMap|forEach|filter|reduce|…` and does not contain `push`, so on AC1's stated line
`batches.push(() => agent(f))` the innermost opener does not classify as `iter`; the brace walk at
`:944` attributes the call to the enclosing loop header, and the message emitted is the loop-body
text built from `checkSeqMarker` at `:955-963`, which never consults `markedWhy`. AC1's other line,
`boundedParallel(batches, 5)`, contains no `agent(` at all, so the scan returns immediately.

So the refusal AC1 observes is unit 1's loop denial naming the loop — the one message AC1 says must
NOT appear. The mutation take-back could be entirely inert and AC1 still goes green. The spec calls
AC1 the single criterion that distinguishes this unit's mechanism from unit 1's.

**Smallest fix:** rewrite AC1 onto a shape that reaches the iter arm — `const batches = []` grown by
a top-level `batches.push(...)`, then fanned via `batches.map((b) => agent(b))`: exit 0 today,
denied naming `batches` and the mutation after this unit. State in §4 that the take-back affects the
`iter` arm only. If the loop-arm denial should also carry the per-name reason, that is a second
scope item with its own criterion, not an assumption.

**Left-shift:** the `agent-cap self-test` arm asserts on the refusal TEXT, not just the exit code.
A criterion that only checks non-zero cannot tell which rule fired, which is the whole defect here.

## H3 — HIGH · unit 1 · §2 S1 and §4 Inventory (`tools/hooks/agent-cap.js:910`)

There are SIX loop-keyword predicates in the file, not five. Verified:
`grep -n 'for|while' tools/hooks/agent-cap.js` returns 705, 711, 738, 910, 934, 944; the inventory
table lists five and omits `:910`, `if (/\b(for|while)\s*$/.test(before)) { hit = { kind: 'loop' } }`.

It asks the same question — is this open paren a loop opener — from the opener-walk anchor, and it is
blind to `for await (` in exactly the way S2 names. It also cannot simply take `LOOP_HEADER`: `:910`
tests the text BEFORE an opener position, so a pattern ending in `\(` or `do\s*\{` never matches
there.

The residual is not cosmetic. `openersOf()` walks right-to-left, so when `before` ends in `for await`
the `:910` predicate misses, `hit` stays null, and the walk continues outward. If the next enclosing
opener is a bounded `.map(`/`.forEach(` receiver in `ok`, the call-site arm returns at `:912-919`
with no finding and the loop arms at `:934`/`:944` are never reached — a fail-open the widened
`LOOP_HEADER` does not close. So S1's "ONE predicate at every site that asks is this a loop header"
and AC5's "LOOP_HEADER is the single source" are both unmet after the change, and §3's non-goals and
§5's residual list — which do name three other residuals — name this one nowhere.

**Smallest fix:** add a sixth inventory row for `:910` and say what it takes: a keyword-tail sibling
derived from the same source (as site 710 already does for the global flag), or an explicit §3 note
that the site is out of scope, with the fail-open above written down. Add an AC arm for `for await (`
reached through the OPENER walk, not only through the brace walk.

**Left-shift:** an `agent-cap self-test` arm per walk, not per keyword: the same fan expressed as
`for await (` must deny whether it is reached through the opener walk or the brace walk. Gate the
class — "every loop-recognition path sees the same keyword set" — and a seventh copy cannot hide.

## H4 — HIGH · unit 3 · §2 S4 (no matching §6 criterion)

S4 requires rule 4 `scanJoinFindings` to take the same unterminated-view fallback as rule 3, and no
acceptance criterion observes rule 4 at all. AC1 exercises a per-finding fan (rule 3), AC3 pins only
the dispatcher's return SHAPE, AC2/AC4/AC5 are negative or regression arms.

Verified in source: `scanJoinFindings` (`agent-cap.js:1411-1413`) reads `renderBlankedLiterals`
exactly as `capFindings` (`:1117`) does, and the spec's own inventory marks both as lacking the
fallback. Once S1/S2 change the return to an object, the minimum work that stops rule 4 crashing is
adding `.code` at `:1413` — which passes AC1-AC5 whole while leaving rule 4 blind under an
unterminated literal. That is the gate-the-class-not-the-instance failure S4 exists to prevent,
shipped under a green spec. §3 explicitly rejects "give only rule 3 the fallback", so no non-goal
withholds this.

**Smallest fix:** add the AC1/AC2 pair mirrored onto rule 4 — a script whose JOIN sits below an
unterminated backtick is DENIED, and a legal join under a multi-line template literal still exits 0.

**Left-shift:** every rule that consumes the blanked view gets one arm in the pair. Stated in the
self-test as a per-rule loop over the rule table rather than as hand-written arms, so rule 5 arrives
with its arms already demanded.

## H5 — HIGH · unit 7 · §2 S3 (no matching §6 criterion)

S3 extends the blob comparison to `pre-commit` on the stated ground that one arm covering one of two
hooks certifies coverage it does not have. Every criterion in section 6 names `pre-push` only: AC1,
AC2, AC3 and AC5 are all pre-push, AC4 is a no-op arm, AC6 asserts only leg greenness. §1's goal
sentence, S1 and S2 also name pre-push alone, so a pre-push-only build is the likely one — and it
passes AC1-AC6 whole.

The unimplemented half is the one that matters most: the branch guard lives in `pre-commit`, which is
what the charter's §3 machine-enforcement depends on.

**Smallest fix:** duplicate AC1 and AC3 for `pre-commit` — a planted `<hooksPath>/pre-commit`
divergence prints the divergence line naming both hashes, and an unreadable
`HEAD:.githooks/pre-commit` reports UNKNOWN rather than ok.

**Left-shift:** write the comparison over a LIST of tracked hook names and have the self-test derive
its arms from that list, so adding a third hook to the list adds its arms rather than needing them
remembered.

## H6 — HIGH · unit 4 · §2 S5 (no matching §6 criterion)

S5 requires the criterion's population to be DERIVED — "naming the three files that have the problem
today certifies coverage for tomorrow's fourth" — and no section-6 criterion fails for a hardcoded
three-filename predicate. AC1 reads `tier2-review.js`; AC2/AC3 stage a break in that already-known
file; AC5 is a green bar; AC4 is the negative direction (a harness binding no counter must not red),
which a literal filename list satisfies trivially.

The positive derived-population arm exists nowhere. So the hardcoded predicate S5 names as the
failure passes the whole acceptance set, and the class returns silently at the fourth harness. §3's
exclusions are about counter semantics, not population derivation.

**Smallest fix:** add an AC with the positive arm — a NEW file that binds a `lensesDead`/
`skepticsDead`-shaped counter and carries no `RUN INTEGRITY` block makes
`node tools/workflows/check-workflow-syntax.js` exit non-zero and name it.

**Left-shift:** the arm IS the left-shift, and it is the general one: any check whose subject is "all
files of kind K" owes a criterion that creates a NEW member of K. Worth a line in the spec template's
acceptance guidance. (Subject to B2 — if the scanner does not survive the owner ruling, this finding
dies with it.)

## H7 — HIGH · units 1, 2, 3, 5, 6, 7 · §7, and unit 7's AC6

Six specs nominate gate legs the command they name will not run. `tools/run-gates/run-gates.sh:947`
marks any leg with `subject = kit` OR `chunk = selftests` as `ondemand` unless `GATE_SELFTESTS=1` is
set, and AGENTS.md records that no boundary sets it (owner, 2026-08-27) — `.githooks/pre-push` forces
`GATE_FULL`, which deliberately does not lift this hold. In `tools/gate-legs.json`,
`agent-cap self-test`, `agent-cap restatement self-test`, `memory-hygiene self-test`,
`govkit selftest` and `check-wiring self-test` are all subject `kit` / chunk `selftests`.

So unit 7's AC6 asserts an outcome the named command cannot produce, and units 1, 2, 3, 5 and 6 claim
coverage for arms the bare bar never executes. Read literally, each spec's new arms — the whole
left-shift — go unexercised. Units 5 and 7 compound it by reasoning from the leg's GUARD ("so they
run on this diff by construction"): wrong mechanism. The guard scopes a run; the subject and chunk
decide whether the leg runs at all. Every one of these units is kit work, for which AGENTS.md says
the DoD owes `GATE_FULL=1 GATE_SELFTESTS=1`.

**Smallest fix:** in each of those §7s, name `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for
the kit-subject legs and keep the plain bar for the repo-subject ones, and drop the guard-based
reasoning. Unit 4 already gets this right ("subject `repo`, so it runs on every bar") and is the
model.

**Left-shift:** a spec-lint leg — every backticked leg name in a spec's §7 or §6 is looked up in
`tools/gate-legs.json`, and a leg with subject `kit` or chunk `selftests` requires
`GATE_SELFTESTS=1` in the same section. Fully derived from the manifest, so it cannot rot, and it
would have caught all six sites in one run.

## H8 — HIGH · unit 2 · §2 S1 and §4 "Why the vocabulary is shared", against §6 AC5

S1 calls its seven-verb list "the one the file already uses for a right-hand side". The quoted
existing constant (`agent-cap.js:759`) is
`/\b(concat|push|flat|flatMap|fill|repeat)\s*\(|\.\.\./` — six verbs, no `unshift`, no `splice`. §4
accounts for the difference as `repeat` and the spread only, which is false in the other direction
too.

AC5 demands both forms derive from one source. Satisfying it either drops `unshift`/`splice`
(contradicting S1) or adds them to the marked-branch RHS veto — a widening of a different rule that
no section scopes and no arm covers.

**Smallest fix:** state the two sets explicitly in §4 — receiver = RHS ∪ {`unshift`, `splice`} \
{`repeat`, spread} — say in S1 that `unshift` and `splice` are NEW verbs, and either scope the RHS
widening in §2 with its own arm or exclude them from the shared source.

**Left-shift:** an arm per NEW verb in whichever rule the widening lands in. A verb added to a shared
constant without an arm is a rule change nobody voted for, and one arm per verb makes the vote
explicit.

## H9 — HIGH · unit 4 · §3 third non-goal, against §1 and §4 Inventory

The non-goal's premise is false. `tier2-review.js` DOES compute a contradictory-verdict counter:
`const conflicts = new Set()` at `:434`, `conflicts.add(v.id)` at `:443`, the discarded verdicts at
`:445`, the WARNING at `:455-456` ("demoted to UNVERIFIED"), and `conflicts: conflicts.size` at
`:480` and `:593`. Only the spelling differs from the siblings' `conflictIds`
(`drift-audit-code.js:393`).

The justification — "would put a number in a report that nothing derives" — does not hold for a
counter the file derives and already logs. So the `RUN INTEGRITY` block and AC1 omit the one counter
that says findings were DEMOTED because two skeptics disagreed: exactly the degradation §1 exists to
surface, kept out of the durable record on a premise that nothing needs inventing.

`downgrades`/`severityCorrection` genuinely is absent from this file. The conflicts half is not.

**Smallest fix:** add `conflicts.size` to the §4 inventory, to the block text ("<n> contradictory
verdict(s) demoted to unverified") and to AC1; narrow the non-goal to `downgrades` alone.

**Left-shift:** covered by the AC1 interpolation assertion in B2's fix — if AC1 names the counter
set, a counter dropped from the block reds. Nothing new is needed beyond adding `conflicts` to it.

## H10 — HIGH · unit 5 · §2 S1 and §4 Inventory, against `corpus_ids.py:122-136`

`corpus_ids.read_declared_keys` is a SIXTH reader of `.memory-tree.conf`, living in the very module
that is to host the shared parser. It re-partitions the file on `=` with the same skip-blank/skip-`#`
rule and takes the key as `line.partition('=')[0].strip()`. It is absent from §4's five-copy
inventory and from every non-goal (which withhold the drift-audit copy, the defaults merge, format
changes and a general shell grammar).

After S2's `export ` handling, `export MEMORY_ROOT=memory` yields key `MEMORY_ROOT` from the shared
parser and `export MEMORY_ROOT` from `read_declared_keys` — so the retired-key and undeclared-CHARTER
checks disagree with the parser inside one file. A new two-answers-to-one-question, created by the
unit whose goal is one parser, and invisible to AC6, whose grep keys on a quote strip this function
does not have.

**Smallest fix:** add `read_declared_keys` to the §4 inventory and to S3's caller list (it needs the
key normalisation, not the values), or state in §3 why it is excluded and how AC6 detects the second
parse.

**Left-shift:** a `memory-hygiene self-test` arm that writes `export MEMORY_ROOT=memory   # note` into
a fixture conf and asserts every reader agrees on the key set. The parity is between readers, so the
arm survives the next reader being added — the count in the inventory does not.

## H11 — HIGH · `memory/builds/aWeldedTribunal/README.md` — "Expected improvements" bullet 4 and roster row 6

The README promises "`govkit update` can land a file gov started shipping" and the roster says unit 6
"lands a descriptor source with no receipt row". Spec-6's title says it REPORTS a source gov started
shipping, and its first non-goal says "WRITING the gap. This unit reports; it does not land bytes."

The README even disagrees with itself: the generated build-units table two tables below the roster
carries the spec's "reports" title. The build's headline deliverable and the unit disagree on the
scope axis, so a closing review or an owner reading only the README concludes the adopter's six-day
ImportError class is fixed when the shipped change is one report line and a summary word.

**Smallest fix:** rewrite both README lines to "reports a source gov ships that the adopter does not
hold, and says the install is INCOMPLETE", and note the landing verb is the filed follow-up.

**Left-shift:** the generated build-units table already carries the spec's own title; make the roster
rows generated from the same source instead of hand-written, and the class is structurally
impossible rather than proof-read. If the roster must stay authored, a hygiene arm comparing roster
row text to the spec title for the same unit id is the cheap version.

## H12 — HIGH · unit 7 · §2 S1/S3 and §4 Liveness

Check H's entry guard is tracked `.githooks/pre-commit` alone (`tools/check-wiring.sh:190-193`).
Nothing in check H or in this spec requires `.githooks/pre-push` to exist or be tracked, yet §4 rules
that an unreadable side is UNKNOWN "and counted the same as a divergence", and AC3 pins that with no
bound.

The population is real, and this kit is copy-installed. `check-wiring` is its own registry entry
(`tools/govkit/entries/check-wiring.kit.toml`) while both hooks ship from a DIFFERENT entry,
`push-main` — whose pre-commit rule is `merged` into "the target's own pre-commit", so the deployer
explicitly models targets that already own a pre-commit. Such an adopter, with no pre-push, gets a
permanent UNKNOWN, a permanent `unwired++`, and a permanently non-zero `--check` — which is the
unattended precondition — with no action available to clear it.

**Smallest fix:** add to S1 that the pre-push comparison runs only when
`git ls-files --error-unmatch .githooks/pre-push` succeeds, and otherwise emits a `skip` line naming
the absent tracked hook. Restate AC3 so UNKNOWN-counted-as-unwired applies only to an
expected-but-unreadable hook.

**Left-shift:** a self-test arm over a fixture repo that tracks a pre-commit and no pre-push:
`--check` exits 0 and prints the skip line. That is the §7 "a skip must announce itself" rule as an
arm, and it generalises to every check whose subject may be absent in an adopter.

---

## M1 — MEDIUM · unit 7 · §2 (S1-S5) and §5 user docs

S4 corrects the stale claim in `.githooks/pre-push`'s header and §5 corrects the matching sentence in
AGENTS.md, but neither touches `memory/gotchas/hookspath-resolves-into-another-checkout.md`. Its "Its
gate" section still reads that the check-wiring comparison "is opened as a backlog item rather than
written here, because a check whose subject is the operator's environment needs a decision about
whether it reds or reports" — the decision this unit takes (§8 F1) and the check it writes (S1-S3).

That leaves the record the unit cites as its own class asserting that the thing it just built does
not exist: the same two-answers-to-one-question class S4 exists to close for the hook header, one
carrier fixed and its sibling left standing. No §3 non-goal excludes it — they cover redding, a
pre-push refusal, per-worktree hooksPath, and auto-fixing.

**Smallest fix:** add an S-item refreshing that record's "Its gate" and "What to do" sections in the
same commit: name the decision (Option A, report), name the check, and keep the landing-boundary
documented check the record prescribes, since a SessionStart report does not cover the window §5
already admits to.

**Left-shift:** none proposed as a gate. A predicate for "a record's prose still describes an
un-built thing" is the class B2's ruling already refused. The honest version is a DoD line: when a
unit closes a gap a `memory/gotchas/` record names as open, that record is a carrier and gets swept
with the others.

## L1 — LOW · unit 5 · §6 AC1

AC1 says "Today four of them return `memory   # note`". All FIVE readers hold the identical naive
body — `check-arms.py:82`, `corpus_ids.py:118`, `gen_build_index.py:287`, `gotchas.py:92`,
`row_grammar.py:93` all do `conf[k.strip()] = v.strip().strip('"').strip("'")` with no inline-comment
or `export ` handling. The AC appears to have counted the four adopting callers S3 names, excluding
`corpus_ids`, which is equally broken.

Impact is small — §1 and §4 state the correct picture and the AC's requirement covers all five — but
the criterion states a false baseline and reads as though `corpus_ids.load_conf` is already correct
and out of the fix.

**Smallest fix:** change AC1 and AC2 to "today all five" and keep the §4 enumeration as the single
source for the count.

**Left-shift:** none. This is the "NO count of a derived population is written in prose" rule (§7)
applied to an acceptance criterion — the durable fix is that criteria say "every reader in the §4
inventory", never a number.

---

## The pattern worth naming

Eight of the sixteen findings are the same shape: a scope item states a class-coverage requirement
(rule 4 as well as rule 3, pre-commit as well as pre-push, a derived population rather than three
filenames, the sixth reader, the sixth predicate) and section 6 observes only the instance. The specs
argue gate-the-class-not-the-instance in their own prose and then write instance-shaped acceptance.

The cheapest structural answer is a bookkeeping lint: every `S<n>` in section 2 carries an explicit
`covers` annotation on at least one section-6 criterion, and a spec with an uncovered S-item reds.
What it does NOT check — and the header must say so — is whether the criterion actually exercises the
item. H4, H5 and H6 would each have needed a human to notice that too. But an S-item with no
criterion at all is machine-visible, and three of the four went unnoticed by everyone until this run.
