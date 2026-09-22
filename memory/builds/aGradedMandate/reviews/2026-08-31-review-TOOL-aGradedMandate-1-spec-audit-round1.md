**Serves:** spec-audit TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9

# aGradedMandate — spec audit of the nine unattended-kit units, ROUND 1

*Adversarial Tier-2 pass over the spec set this run authored, node `a`, 2026-08-31. Every finding
below was re-derived against the tree in this worktree before it was written down: the driver
(`tools/unattended/unattended.sh`, 4259 lines), the gate leg
(`tools/unattended/check-unattended.sh`, 2618 lines), the leg manifest, the profile table and the
two protocol copies were read at the line numbers the specs cite. The severities in the table are
this report's adjudication, not the finders' self-grading. Binding contract:
`memory/guides/UNATTENDED-PROTOCOL.md`. Method: `memory/guides/BUILD-METHOD.md`. Commissioning
review: `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.*

**Range:** nine spec records, each pinned at the blob reviewed —
`spec/2026-08-31-spec-TOOL-aGradedMandate-1.md@2355561c85ec2760398da47b4b5874ee5455849a` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-2.md@9e84c6d2d447bfe3471fd1750b32bd60886392ba` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-3.md@d78df097adf59cf4df9031125237b595f67153ce` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-4.md@d2723db304288ee104c31363afed247f54e5de64` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-5.md@96b51f7e343ab0744bcf718703b3eee0f148b471` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-6.md@43f31964432715eacaf29c2503a4276638a216be` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-7.md@8470bd5e3541716a6fbc16b363a3d13d24602762` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-8.md@9c7c3228d794f63970c3a9d64e3327bbe6dee7bb` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-9.md@fb21ea4d6d75c2ca1f16cf616dccc1757a58fb17`.

**ROUND:** 1.

## Verdict: BLOCKED

Two blockers. `TOOL-aGradedMandate-3` S2 writes `export GATE_SELFTESTS=1` into a file the kit copies
to every adopter, which a ratified decision and an owner ruling both forbid and which `govkit
selfcheck` check 7h3 fails by name; the spec's non-goals engage neither. `TOOL-aGradedMandate-5`
changes the member GRAMMAR of `PARK_KINDS_OWED` and inventories one of its two leg-side readers, so
the unit as specced reds `unattended kit gate` on the tree it ships with, contradicting its own AC4.

Seven high findings follow. Three of them are the same shape as the second blocker and are the
dominant defect class in this set: **build to the Inventory, red a gate the spec's own §7 names.**
`TOOL-aGradedMandate-2` misses the protocol's spelled-out count sentence (check 16) and the example
conf's `CORE_FLOOR` pin (`unattended.test.sh:1371`); `TOOL-aGradedMandate-4` misses the example conf
and the driver's conf-default init line (check 22). Each is a one-line omission with a mechanical
repair, but each lands red.

`TOOL-aGradedMandate-3` needs a rewrite rather than a patch: it carries a blocker and three of the
seven highs and mediums between them, and its load-bearing §5 perf claim and its §3 non-goal both
verify FALSE against the tree.

**Review shape.** Raw 49, confirmed 22, refuted 27, unverified 0, precision 0.45. The 22 confirmed
findings collapse to 19 distinct defects: two finders independently reported the `PARK_KINDS_OWED`
second reader (F2), two the orphaned `SPEC_THIN_CUTOFF` shape criterion (F16), and two the
double-owned protocol fact-3 edit (F17). Convergence across independent finders is corroboration,
so each merged entry carries the strongest reachability argument of its contributors. Precision at
0.45 is at the floor the charter names for tightening scope before adding agents; the refuted half
was dominated by re-reports of the specs' own stated non-goals.

## Findings

| # | Sev | Site | One line |
|---|-----|------|----------|
| F1 | BLOCKER | `spec-TOOL-aGradedMandate-3.md` §2 S2, §3 | `export GATE_SELFTESTS=1` in a kit-shipped file reverses an owner ruling and reds govkit 7h3 |
| F2 | BLOCKER | `spec-TOOL-aGradedMandate-5.md` §4 Inventory, §10 | `PARK_KINDS_OWED` has TWO leg-side readers; check 2's `pk_dead` loop is unnamed and reds on `rescope:retire` |
| F3 | HIGH | `spec-TOOL-aGradedMandate-3.md` §2 S1/S3, §3 | The `memory/` guard makes the escalation fire on 100% of closes, not on checker-touching ones |
| F4 | HIGH | `spec-TOOL-aGradedMandate-2.md` §2 S2, §4 | The `**Serves:**` id join ignores the `N..M` range form (18 live) and the id boundary |
| F5 | HIGH | `spec-TOOL-aGradedMandate-6.md` §2 S1/S2, §10 | Promoting an unvalidated `rb` to a named commit turns the provenance read into a git-INDEX read |
| F6 | HIGH | `spec-TOOL-aGradedMandate-2.md` §2 S4, §4 | The protocol's "Ten kit-owned core items." sentence is uninventoried; check 16 reds |
| F7 | HIGH | `spec-TOOL-aGradedMandate-4.md` §4 Inventory | `SPEC_THIN_CUTOFF` needs two more carriers; check 22's phantom arm reds without them |
| F8 | HIGH | `spec-TOOL-aGradedMandate-2.md` §4 Inventory | `.unattended.conf.example:54` `CORE_FLOOR` unmoved reds `unattended.test.sh:1371` |
| F9 | HIGH | `spec-TOOL-aGradedMandate-1.md` §4 Migration | The Migration section's one worked example is the record that FAILS the new term |
| F10 | MEDIUM | `spec-TOOL-aGradedMandate-3.md` §5 perf | "Inside it" inherits a width-8 figure; at width 2 the escalated close breaches `GATE_BOUND` |
| F11 | MEDIUM | `spec-TOOL-aGradedMandate-3.md` §2 S1/S5 | Four held legs declare NO guard, so no diff can ever escalate them, and S5 does not say so |
| F12 | MEDIUM | `spec-TOOL-aGradedMandate-8.md` §5 risks, AC6 | The stated size-ceiling mitigation does not exist, making AC6's size half vacuous |
| F13 | MEDIUM | `spec-TOOL-aGradedMandate-3.md` §2 S4, AC3 | S4 names two fault inputs; only the unreadable manifest has a criterion |
| F14 | MEDIUM | `spec-TOOL-aGradedMandate-6.md` §2 S3, AC3 | S3 says "either is unreadable"; only one direction has a criterion |
| F15 | MEDIUM | `spec-TOOL-aGradedMandate-4.md` §2 S2 | Term ORDERING is a stated requirement no criterion observes |
| F16 | MEDIUM | `spec-TOOL-aGradedMandate-4.md` §6 AC5 | AC5 demands a `SPEC_THIN_CUTOFF` shape validator no scope item or inventory row builds |
| F17 | MEDIUM | `spec-TOOL-aGradedMandate-5.md` §2 S5 · `-8.md` §2 S5 | One protocol edit, two owners, no cross-reference, and no criterion that can see it |
| F18 | MEDIUM | `spec-TOOL-aGradedMandate-8.md` §2 S6 | S6 has no criterion, and two other units discharge their user-docs obligation onto it |
| F19 | LOW | `spec-TOOL-aGradedMandate-8.md` §3 · `-9.md` §3 | "the ten items" is eleven by the time these units land |

---

### F1 — BLOCKER · `spec/2026-08-31-spec-TOOL-aGradedMandate-3.md` §2 S2, against §3 Non-goals

S2 says: on any hit, `export GATE_SELFTESTS=1` for that invocation. §10 restates it as "an
environment export before that call", where the call is `run_bounded` at
`tools/unattended/unattended.sh:181`. So the assignment lands in `unattended.sh`.

`tools/unattended/kit.toml` declares `home = "tools/unattended"` and `[[files]] include = "**"`, so
`unattended.sh` is copied verbatim into every adopter. `govkit selfcheck` check 7h3
(`tools/govkit/govkit.py:1498-1558`, subject `repo`, no guard, on every bar) derives the shipped set
through that same `**` expansion, exempts only `memory/` and `.md` paths, and its `policy_re`
accepts leading whitespace plus an optional `export`. An indented `export GATE_SELFTESTS=1` in
`unattended.sh` matches exactly, and the leg fails with the sentence written for this case: *carries
a bare GATE_SELFTESTS assignment AND is shipped by kit 'unattended'*.

The mechanical red is the smaller half. The block's own header cites `TOOL-dUnstalledConvoy-28` and
states the rule plainly: the mechanism may travel, the choice may not. `.githooks/gate-env.sh`
records the switch as OFF "here as well as in every adopter" by owner ruling 2026-08-27, and
`AGENTS.md:486` spells the same ruling as *ON DEMAND ONLY: no boundary sets it*. `--close` is a
boundary. §3 disclaims only the 2026-08-23 ruling about the kit's own suites and engages neither the
2026-08-27 ruling nor `TOOL-dUnstalledConvoy-28`, so the unit as specced reverses an owner ruling
with no owner turn — which is precisely the substitution the unattended protocol forbids.

**Fix.** Cite `TOOL-dUnstalledConvoy-28` and the 2026-08-27 ruling in §3, and route the choice
through the adopter's own channel: a `.unattended.conf` key defaulting OFF that the arm reads, so
the MECHANISM travels and the CHOICE does not. That is the same conf idiom `TOOL-aGradedMandate-4`
already uses for `SPEC_THIN_CUTOFF`, so no new pattern is owed. If the escalation is meant to bind
gov unconditionally, that is an owner fork and belongs in §8, not in scope.

**Left-shift.** Already gated — check 7h3 catches it. What is missing is the check on the SPEC:
add an arm to `tools/unattended/unattended.test.sh` asserting that the driver contains no bare
`GATE_SELFTESTS` assignment, so the kit's own suite reds at the same moment govkit does, and the
builder sees it from inside the kit rather than from a repo-subject leg two directories away. Stage
the break, confirm RED, unstage.

---

### F2 — BLOCKER · `spec/2026-08-31-spec-TOOL-aGradedMandate-5.md` §4 Inventory and §10

The unit changes `PARK_KINDS_OWED` from a list of bare kinds to a list of MEMBERS where a member may
be a `kind:act` pair, giving
`PARK_KINDS_OWED="decision abort override waiver rescope:retire rescope:supersede"`.

There are TWO leg-side readers of that variable, not one.

The spec names the second: its Inventory row reads *`check-unattended.sh` — the both-directions
taxonomy check accepts the pair form*, and §10 pins that reader at
`tools/unattended/check-unattended.sh:1943-1951`, which is check 27. The FIRST reader is check 2's
dead-member arm at `check-unattended.sh:366-371`, derived from the same `core_of PARK_KINDS_OWED`
read at `:219`:

```sh
for pk in $PARK_KINDS_OWED; do
  grep -qE "^[[:space:]]*park \"\\\$rel\" $pk " "$DRIVER" || pk_dead="$pk_dead $pk"
done
```

The driver's only `rescope` writer is `park "$rel" rescope "$act $unit…"` at `unattended.sh:3950`.
There is no `park "$rel" rescope:retire ` call site and there never will be — the act is a field of
the reason, not part of the kind. So both new members land in `pk_dead` and the leg fails check 2:
*the parked-kind taxonomy names a kind no park call site in the driver writes*. `unattended kit
gate` is `bash tools/unattended/check-unattended.sh`, subject `repo`, no guard, on every bar, and
§7 of this spec names it. AC4 asserts it stays green. It will not.

Two things make this a blocker rather than a missing inventory row. First, the repair is not
mechanical: teaching that loop the pair form means deciding how a `kind:act` member derives a
call-site assertion — match the bare kind, then assert the act separately — which is new predicate
logic no section of the spec authorizes. Second, the block the spec walks past is a recorded design
statement. Its header at `:351-365` argues at length that the check is ONE direction *by design*,
because `history` is the declared-nowhere complement and the converse assertion would force a future
unit to weaken the leg in the same commit that adds a legitimate kind. A unit that widens the member
grammar has to engage that argument, and this one does not read it.

**Fix.** Add a `check-unattended.sh:366-371` row to the Inventory naming the `pk_dead` loop
specifically, and specify the widened predicate: grep for the bare KIND at a `park` call site, then
assert the act is a first token some site can write. Reproduce the asymmetry rationale in the
widened predicate's header, since the widening is exactly the kind of edit that header was written
to survive. Widen AC4 to name both arms explicitly rather than "its both-directions check".

**Left-shift.** An arm in `unattended.test.sh` that sets `PARK_KINDS_OWED` to a member whose kind is
outside `PARK_KINDS` and asserts check 2 still reds, plus one that sets a valid `kind:act` member and
asserts it does not. Observe both RED against the current predicate before wiring the fix — a leg
whose failing case has never been seen is an assertion about nothing.

---

### F3 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-3.md` §2 S1/S3 and §3 Non-goals

S3 says "On no hit, behave exactly as today", and §3 says the escalation "escalates by DIFF and
never by default, so a run that touched no checker pays nothing". Both are unreachable for any real
run.

`tools/gate-legs.json` holds 86 legs, 46 of them held on `subject = kit OR chunk = selftests`. The
held leg `recall floor arms` declares `guard: ["tools/memory-recall/", "memory/", "tools/govkit/"]`.
`changed()` at `tools/run-gates/run-gates.sh:151` runs `git diff --quiet BASE -- <paths>`, a
PATHSPEC, so `memory/` prefix-matches every path beneath it. Every unattended run necessarily commits
`memory/builds/<slug>/RUN.md` and its spec records inside `base..HEAD`. S1's intersection therefore
hits on 100% of unattended closes.

The consequence is not merely a wrong sentence in the spec. Every `--close` then pays the
self-test-inclusive bar, which `.unattended.conf:29-32` sizes at roughly 9700 s of leg-sum, "about
26 minutes of wall at width 8" — see F10 for what that costs on a narrower profile row. AC2 ("the
diff touches no such path") becomes satisfiable only by the stub fixture and never by a real run,
which is the could-not-fail shape one level up.

**Fix.** Add a scope item narrowing the intersection to guard entries that are not ancestors of the
run's own record paths, or intersect against the diff with `memory/builds/<slug>/` excluded. Restate
§3's non-goal to say what the narrowed arm actually promises.

**Left-shift.** An arm whose fixture diff contains ONLY `memory/builds/<slug>/RUN.md` and asserts no
escalation, beside the existing hit arm. It fails today against the naive intersection, which is why
it is worth writing.

---

### F4 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-2.md` §2 S2, against §4

S2 requires, per CLOSED unit id, a tracked record whose first twelve unfenced lines carry a
`**Serves:**` line of kind `spec-audit` "naming that id". §4 spells the data model as
`**Serves:** spec-audit <id> …` and §10 commits the join to "a local grep instead of the memory-tree
parser", because the kit copy-installs standalone.

The binding grammar in `memory/HYGIENE.md:280-282` is wider than that. An id may carry a trailing
`@rev-N`, and a contiguous run may be written `N..M`, which "EXPANDS at authoring time". Only
`gen_build_index.py` expands it (`_expand_ids`, `:432`) — the parser this kit deliberately does not
carry. Of 123 tracked `**Serves:** … spec-audit` lines, 18 use the range form, including
`TOOL-aBoundedVerdict-1..5 TOOL-aBoundedVerdict-11..19` and `TOOL-aRuledFrontispiece-1..11`.

Two failure directions, both live:

- **False negative.** A build whose audit was recorded as `**Serves:** spec-audit
  TOOL-aBoundedVerdict-1..5` names no literal `TOOL-aBoundedVerdict-5`, so `--close` blocks on
  `specs-audited` for units that WERE audited. The only exit is a self-authored override, on an item
  whose whole point is that it cannot be talked out of.
- **False positive.** A naive substring join lets `TOOL-aBoundedVerdict-1` be satisfied by a line
  naming `TOOL-aBoundedVerdict-19` — a real id in that build (1..19) and in `aRuledFrontispiece`
  (1..11).

§4 states neither, and §10's claimed seam does no id join at all: the `closing-review-recorded` walk
greps `'^\*\*Serves:\*\*.*diff-review'`, which matches the KIND only.

**Fix.** Spell the id join in §4 as whole-token WITH range expansion: match `<id>` bounded by
whitespace or end-of-line, and expand `<family>-<slug>-N..M` before comparing. `id_in` in
`tools/unattended/lib-unattended.sh:37` already gives the whole-token half and is the seam to cite.
The range expansion has no seam and must be written; §10 should say so rather than implying the
walk covers it.

**Left-shift.** Two arms in `unattended.test.sh`, both over fixtures drawn from the real corpus
shapes: a record binding `TOOL-x-1..5` satisfying unit `TOOL-x-5`, and a record binding `TOOL-x-19`
NOT satisfying unit `TOOL-x-1`. This build is its own first subject, so both fire on landing.

---

### F5 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-6.md` §2 S1/S2 and §10

S1 adds `pinned_units` beside `baseline_units` with "the same cutoff handling and the same refusal
shapes"; S2 points check 24's RETIRE loop at `pinned_units "$rb" …`. §10 calls the input free: *`rb`
is already read in check 24's own neighbourhood and already handed to `baseline_units` as the
fallback commit, so the value this unit needs is in scope at the call site with no new derivation.*

`rb` is not free, because its current position is guarded and its new position is not. Today `rb`
reaches `baseline_units` as the FALLBACK argument (`check-unattended.sh:1608`), where
`lib-unattended.sh:175-179` catches an empty value: `[ -n "$_bu_base" ] || _bu_base=$_bu_fb`, then a
refusal when the result is still empty. Promoting `rb` to `pinned_units`'s NAMED primary commit
removes it from that slot, and check 24 never validates `rb` itself — unlike `dod_met`, which
refuses a `base:` shorter than 7 characters for this exact reason.

An empty `rb` does not fail the blob read. It changes what the read MEANS: `GIT show ":$bre"` is
index syntax, and it succeeds. Verified live on this tree — `git show
":memory/builds/aThawedCorpus/README.md"` returns the indexed file at rc 0. So a run-state file with
an absent, blank or truncated `base:` makes the RETIRE arm grade the working INDEX instead of the
pinned BASE, and S3's unreadable-baseline skip never fires because the read succeeded and returned
plausible bytes. The driver's own `closing-review-recorded` header records this same degeneration
from `check_authorization`, where an empty base turned a provenance test into a read of the git
index.

Note the trap in S1's own phrasing: `pinned_units`'s stated difference from its sibling is only "how
the commit is chosen", so the commit-CHOOSING refusal is exactly the one shape that "the same
refusal shapes" naturally omits.

**Fix.** Give `pinned_units` its own precondition before the blob read — refuse a `base:` shorter
than 7 hex characters, or one failing `GIT cat-file -e "$rb^{commit}"` — and name that refusal in S3
as a third distinguishable skip.

**Left-shift.** An arm whose fixture run-state file carries a blank `base:` and asserts check 24
reports the named skip rather than a verdict. AC3's "does not resolve" fixture does not reach this:
an empty base RESOLVES, to the index.

---

### F6 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-2.md` §2 S4 and §4 Inventory

S4 and the Inventory name "one table row, byte-identical" in `PROTOCOL.template.md` §4 and its
render. Directly above that table, at `memory/guides/UNATTENDED-PROTOCOL.md:313` and
`tools/unattended/PROTOCOL.template.md:313`, sits the sentence **"Ten kit-owned core items."** — and
check 16 at `check-unattended.sh:1523-1533` parses that word, maps it through its own number table
(which already spells `eleven`), and fails when it disagrees with the driver's `DOD_CORE` count:
*the protocol's stated count of core Definition-of-Done items disagrees with the set the driver
enforces*.

`DOD_CORE` at `unattended.sh:343` carries exactly ten items today. S1 appends an eleventh. Against a
protocol still reading "Ten", `unattended kit gate` reds — a `subject = repo`, unguarded leg on
every bar, and the first gate §7 lists.

AC5 cannot catch it. It asserts the two protocol copies are byte-identical to EACH OTHER, and the
count sentence would be wrong in both. That is exactly the arm's own recorded origin: the table grew
to eight rows while the sentence above it still said six, in both copies, and the row-join leg was
green over a document contradicting itself.

**Fix.** Add `PROTOCOL.template.md:313` and its render to S4 and the Inventory, "Ten" becoming
"Eleven", and add an AC asserting check 16 green after the change, beside AC5's byte-identity
assertion.

**Left-shift.** Check 16 already gates the class; nothing new is owed there. What is owed is the
DISCOVERY: `bash tools/unattended/check-unattended.sh` belongs in the unit's own build loop before
the close, not only in §7's list.

---

### F7 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §4 Inventory, against §7 Gates

The Inventory declares `SPEC_THIN_CUTOFF` in `.unattended.conf` and adds a row to §8 of both
protocol copies. Two more carriers are required and neither is named.

**The example conf.** Check 22 (`check-unattended.sh:1228-1256`) computes `phantom` as `comm -13` of
the example conf's keys against the protocol §8 table's key column, and fails on *documented but in
no example*. Its own header explains why the reverse population is the KIT's example and not the
adopting project's. A key added to §8 and absent from `tools/unattended/.unattended.conf.example`
reds `unattended kit gate`, the first leg §7 lists.

**The driver's conf-default init line.** `unattended.sh` runs under `set -u` (`:40`) and defaults
every driver-read conf key on the init block at `:288-291`. Both sibling cutoffs are handled that
way, and both are declared in the example at `:139` and `:170` with a blank value.

**Fix.** Add Inventory rows for `tools/unattended/.unattended.conf.example` (the key, blank, with
the header's grandfather semantics beside it, since that header tells adopters to measure) and for
the driver's init line at `:288-291`. Add an AC asserting check 22's three-way key join stays green.

**Left-shift.** Check 22 already gates the example-conf half. The init-line half is gated by the
existing `initblock` arm in `unattended.test.sh` only if the key is read at all; add one arm that
runs the driver with the key unset in the conf and asserts no unbound-variable abort.

---

### F8 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-2.md` §4 Inventory, against §7 Gates

The Inventory moves `CORE_FLOOR` from `12:10` to `12:11` in `.unattended.conf` and stops there.
`tools/unattended/.unattended.conf.example:54` carries the same `CORE_FLOOR="12:10"`, and
`unattended.test.sh:1371-1372` asserts that exact value equals `"$(wcw PHASES_CORE):$(wcw
DOD_CORE)"` read from the driver. Appending an eleventh `DOD_CORE` member makes that comparison
`12:10` against `12:11` and reds the arm.

The arm exists precisely because the example once shipped a slack floor — its header records that
`CORE_FLOOR="10:6"` sat against an eight-member `DOD_CORE` for the whole life of the file, because
the only arm reading that file iterated key NAMES and never a value. `run-unattended-gates.sh:175`
runs `unattended.test.sh` under `--selftests`, which §7 names as this unit's own gate. The example
file appears nowhere in the spec.

**Fix.** Add an Inventory row for `tools/unattended/.unattended.conf.example` (`CORE_FLOOR`,
`12:10` → `12:11`, with the reason beside it), and extend AC4 to assert the example and the driver
set sizes still agree.

**Left-shift.** Gated already, by the arm this would red. The left-shift owed is one level up: a
spec-authoring check that every conf key an Inventory moves is moved in BOTH the project conf and
the kit example. Cheapest form is a line in the kit's own README beside the example's header, since
this is the second unit in one build to miss the same file (see F7).

---

### F9 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-1.md` §4 Migration, against §6 AC1/AC2

§4 Migration reads: *The one live record in the tree, `memory/builds/aThawedCorpus/RUN.md`, is at
`LANDING` with `--close` already run; re-closing it would meet the new term, and that is the correct
answer for a loop that stopped at five blockers.*

That file holds exactly one review row:

```
2026-08-27T12:34:24Z review · item TOOL-aThawedCorpus-5 · reason verdict BLOCKED · blockers 5
```

The subject is a UNIT id, not the build slug. S1 requires rows "whose subject is the BUILD SLUG",
and S3 says the new reader mirrors `review_counts`, which compares the item EXACTLY
(`unattended.sh:3438`, `if (item != subj) next`). The join over `aThawedCorpus` returns zero rows,
so AC1 blocks — the criterion for "no `review` row for the build slug". Even under a loose subject
match the row carries no terminal token from `CONVERGED` / `NON-CONVERGENT` / `CEILING`, so AC2
blocks instead.

The one worked example the Migration section offers as evidence the term is safe is the example that
fails it. A builder trusting §4 will wire the term, watch the named record refuse, and either loosen
the term ad hoc or override it — and the migration analysis that was supposed to bound the blast
radius is wrong about its only subject.

**Fix.** Rewrite §4 Migration to state what the record actually holds — one row, subject
`TOOL-aThawedCorpus-5`, verdict BLOCKED, no terminal token — and state plainly that it would BLOCK.
Then either accept that (the record is at `LANDING` and nothing re-evaluates it, which is the
argument §4 wanted) or add the exemption to §2 explicitly.

**Left-shift.** Run the candidate predicate over every tracked `RUN.md` before wiring it, printing
hits AND near-misses, and record the output in the build's journal — the same probe
`TOOL-aGradedMandate-6` AC4 already requires for `pinned_units`. This finding is what that probe is
for, and unit 1 does not ask for one.

---

### F10 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-3.md` §5 perf / scale

§5 says the escalated bar is *roughly 26 minutes of wall clock against a 3600 s bound. Inside it.*
That figure is inherited from `.unattended.conf`'s `GATE_BOUND` comment, which sizes the
self-test-inclusive bar as "roughly 9700s of leg-sum with a 1320s longest leg, about 26 minutes of
wall **at width 8**". The qualifier is dropped.

`tools/run-gates/gate-profiles.txt` grants width 8 only to the `capable` row, which needs 8+ cores
AND 24000 MB. `modest` is width 4 and the `minimal` catch-all is width 2. The same escalated bar is
therefore roughly 2425 s and 4850 s of wall on those nodes. At width 2 the escalated close breaches
`GATE_BOUND=3600` and `gates-green` reports that the merge bar did not answer within the declared
bound — the bar never answers rather than a leg failing, on every run that touched a checker on
modest hardware. With F3 unfixed, that is every run.

The escalation in S1/S2 carries no width, budget or hardware precondition, and §5's risk line prices
only "a slower close", so the load-bearing justification for having no precondition is the claim
that verifies false.

**Fix.** State the width dependence in §5 and add either a precondition (skip the escalation with an
announced reason when the selected profile is below width 8) or an explicit acceptance that a modest
node's escalated close is expected to breach and must be closed by a recorded override. Read the
profile the runner PRINTS rather than assuming a row.

**Left-shift.** An arm that drives the escalation with `GATE_PROFILE=minimal` and asserts the
announced precondition fires. `gate-profiles.txt` already documents `GATE_PROFILE` as a by-name
selector, so the fixture costs nothing.

---

### F11 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-3.md` §2 S1 and S5

S1 escalates only on an intersection with a held leg's `guard` array. S5's whole job is to state
what the arm does NOT reach, and it names only the unattended kit's own suites.

Of the 46 held legs, exactly four declare no `guard` at all: `template size gate selftest`,
`method-carriers self-test`, `agent-cap restatement self-test` and `testsuite counts self-test`.
`run-gates.sh`'s own comment reads an unguarded leg as declaring "by its silence that it reads
everything" — so for the runner they always run, and for S1's intersection they can never be
selected. A run that edits `tools/check-template-size.sh` gets no escalation for the leg that tests
it, and no leg anywhere else guards that path either.

The arm's header would then certify a coverage it does not have, which is the disclosure defect the
charter's gate-header rule exists to prevent.

**Fix.** Add a clause to S1: a held leg with an empty `guard` is escalated unconditionally, matching
the runner's own reading of silence. Failing that, name the four legs in S5 as a second stated gap
beside the unattended suites.

**Left-shift.** An arm asserting the intersection routine returns every guard-less held leg for an
arbitrary non-empty diff. It is one assertion and it pins the reading of silence in the same place
the runner pins it.

---

### F12 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-8.md` §5 risks and §6 AC6

§5's sole risk line for this prose-only unit reads: *the Skill carries byte ceilings through the
kit's own size checks*. AC6 verifies the render "still passes whatever size and shape checks the
kit's own leg applies to it".

No such ceiling exists. `tools/template-size-limits.txt` declares exactly three subjects —
`coding-governance-agents.template.md`, `skills/session-kickoff/SKILL.md`, `AGENTS.md` — none of them
the unattended Skill. No leg in `tools/gate-legs.json` caps a skill other than the kickoff engine.
`check-unattended.sh` contains no byte or size measurement at all; `unattended skill wiring` compares
the render to the installed copy for IDENTITY, not for size.

So the stated mitigation is imaginary and AC6's size half passes at any byte count. Six additions to
a 731-line template land with nothing measuring the result. The shape half of AC6 is real, so the
criterion is not wholly vacuous — but the risk line is a false statement about the tree, and it is
the one load-bearing claim in that section.

**Fix.** Either add `.claude/skills/unattended/SKILL.md` to `tools/template-size-limits.txt` with a
measured ceiling and make AC6 name that number, or rewrite §5's risk line to say the Skill has no
size ceiling and AC6 to assert only the wiring byte-compare it actually verifies.

**Left-shift.** The first option IS the gate: one row in the declared limits table, which
`template size gate` already reads. It costs a line and closes the class for every future Skill edit.

---

### F13 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-3.md` §2 S4, against §6 AC3

S4 names TWO fault inputs — "the manifest cannot be read **or** the pinned BASE does not resolve" —
and requires a skipped escalation with an announced reason for each. AC3 observes only the
unreadable manifest, naming `tools/gate-legs.json`. AC1 and AC2 exercise the diff, AC4 the
announcement, AC5 the leg. The BASE half has no criterion, and no non-goal withholds it.

The untested half is the one that degrades silently: an unresolvable base makes the diff empty, the
intersection empty, and "no escalation is owed" indistinguishable from a clean run. That is the fault
S4 exists to forbid. Blast radius is smaller than it first looks — a run whose BASE will not resolve
also fails the non-overridable `authorization-reachable` — but the coverage gap in §6 is real and it
is the gap that lets the unit ship with exactly the defect its own scope names.

**Fix.** Split AC3 in two, adding: when the pinned `base:` does not resolve to a commit, `--close`
prints a named skip naming the BASE and does not invoke `GATE_CMD` unescalated.

**Left-shift.** The second arm is the gate. Stage a fixture with a garbage `base:` and confirm the
skip is printed and the stub `GATE_CMD` sees no `GATE_SELFTESTS`.

---

### F14 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-6.md` §2 S3, against §6 AC3

S3 requires the two baselines reported separately "when either is unreadable". AC3 observes only the
pinned RETIRE baseline failing while the ADD arm still runs. The mirror — `baseline_units`
unreadable while the pinned RETIRE arm still evaluates — has no criterion.

That mirror is the half that inherits today's whole-check skip. At `check-unattended.sh:1608`, a
`baseline_units` failure sets `rs_why` and the check reports *check 24 skipped for $f*, which skips
all three loops: the ADD loop, the RETIRE loop at `:1627` and the supersession-successor loop at
`:1635`. A build that adds a special case only for `pinned_units` satisfies every AC while leaving
that whole-check skip exactly as it is — which is the half S3 exists to remove.

**Fix.** Add AC3b: when `baseline_units` fails and the pinned BASE resolves, the check reports a skip
naming the ADD baseline specifically and still evaluates the RETIRE arm.

**Left-shift.** The arm behind AC3b. Both directions want a fixture, and the pair together is what
makes "reported separately" observable at all.

---

### F15 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §2 S2

S2 requires the THIN term ordered AFTER the five existing `build-complete` terms, so it never masks
a structural failure. No criterion in §6 observes ordering: AC1 exercises a thin unit alone, AC2 the
grandfather, AC3 a clean roster, AC4 `--plan`, AC5 the leg.

Ordering is a real behavioural requirement here, not decoration. `build-complete`'s terms return
early one at a time (`unattended.sh:3089-3131`, each failing term sets `DOD_OUT` and `return 1`), so
term order decides which message the operator gets. A build that evaluates the terms in any order
passes §6 while reporting THIN over a unit whose spec is actually MISSING, and the operator then
chases the wrong repair — the reason S2 exists.

§5's "a unit whose spec cannot be resolved is already reported by the existing `missing_units` term,
which runs first" is an assertion in prose with nothing exercising it, which is the pattern this
spec set calls out elsewhere.

**Fix.** Add an AC over a fixture that is BOTH structurally broken and thin: `--close` reports the
missing-unit failure and not the THIN grade.

**Left-shift.** That arm. One fixture, one assertion on the message, and it pins the order against
every future term inserted into the same arm.

---

### F16 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-4.md` §6 AC5, against §2 and §4

AC5's second clause requires `check-unattended.sh` to RED "when `SPEC_THIN_CUTOFF` carries a non-date
value". Nothing in the unit builds such a validator. §2's items S1-S5 do not ask for one, and §4's
Inventory carries no `check-unattended.sh` row at all — the leg is inventoried as untouched.

Nor is there a generic validator to inherit. `LANDED_ANCHOR_CUTOFF` is fed straight into a `sort -C`
comparison at `check-unattended.sh:912-913`; `UNITS_REGION_CUTOFF` is passed through to
`baseline_units` at `:1608`. Neither is shape-checked anywhere in the leg, and check 22's own header
states it grades key NAMES and nothing more. The only malformed-value refusal in that neighbourhood
is `CORE_FLOOR`'s at `:394-401`.

So the criterion is deliverable only as unspecced work in a file the spec says it does not touch, or
it is dropped silently — an unmet AC nobody notices, since §6 is the only place it is written. Both
outcomes defeat the spec-set discipline the rest of this build enforces.

**Fix.** Either add an S-item — refuse a `SPEC_THIN_CUTOFF` that is not `YYYY-MM-DD`, beside the
existing `CORE_FLOOR` malformed-value refusal at `check-unattended.sh:394-401` — plus the matching
Inventory row noting it is the first cutoff key to get one and why; or delete AC5's second clause and
state in §5 that a malformed cutoff sorts as an ordinary string and grandfathers unpredictably.

**Left-shift.** If the validator is built, the arm is a fixture conf with `SPEC_THIN_CUTOFF="soon"`
asserting the named refusal. If the clause is deleted instead, the left-shift is procedural: a
spec-audit question asking, per AC, which S-item delivers it — this build's own commissioning review
found the same orphan shape twice.

---

### F17 — MEDIUM · `spec-TOOL-aGradedMandate-5.md` §2 S5 and `spec-TOOL-aGradedMandate-8.md` §2 S5

Two units claim one edit. Unit 5's S5: *Correct `memory/guides/UNATTENDED-PROTOCOL.md` §2 fact 3 and
its template, which enumerate FIVE parked kinds against the driver's eight and state that all four
listed kinds are surfaced.* Unit 8's S5: *The protocol's §2 fact 3 enumerates five parked kinds
against the driver's eight and says all four listed kinds are surfaced. Correct the enumeration and
the surfaced claim, in the template and its render.* Both inventories carry `PROTOCOL.template.md`
§2 for it. Neither names the other — unlike unit 7's S4, which handles the identical situation by
saying explicitly that the edit lands in unit 8.

Nothing can observe whether the edit happened. Unit 5's AC5 and unit 8's AC5 both assert the protocol
pair is byte-identical, which is true before the correction, true after it, and equally true if only
one copy moves in a way that keeps them equal, or if neither does. No machine joins `PARK_KINDS_OWED`
to that prose — check 27 at `check-unattended.sh:1925-1955` is driver-internal.

Two consequences beyond the redundancy. Unit 5 lands at order 5 and unit 8 at order 8, so unit 8's S5
is a no-op whose acceptance nothing asserts and unit 8's §1 "Five statements … are wrong or missing"
is four. And unit 5's Inventory edits the RENDER `memory/guides/UNATTENDED-PROTOCOL.md` directly,
while unit 8's §4 says renders must come from `adopt-unattended.sh` because the wiring leg
byte-compares the pair — one edit, two owners, two mechanisms. A rebase or a fold that defers either
unit silently takes the correction with it.

**Fix.** Delete S5 from `TOOL-aGradedMandate-8` and adjust its §1 count, leaving fact 3 wholly owned
by `TOOL-aGradedMandate-5` and cross-referenced the way unit 7 S4 already cross-references unit 8.
Or the reverse, but not both. Then give the substance an observation:
`grep -c 'of eight kinds' memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/PROTOCOL.template.md`
both 1, and the surfaced-class sentence enumerating the members of `PARK_KINDS_OWED`.

**Left-shift.** Extend check 27 to join fact 3's enumeration to `PARK_KINDS` and its surfaced
sentence to `PARK_KINDS_OWED`, which is the same both-directions join unit 5 is already opening for
the pair form. That closes the class rather than this instance: a prose count beside a declared set
is the defect check 16 already gates one section further down the same document.

---

### F18 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-8.md` §2 S6

S6 asks for two sentences: the diff-driven self-test escalation named in the Skill's `--close`
section, and the retirement split named in its `--rescope` paragraph. No criterion in §6 observes
either. AC1-AC4 are one grep each for S1 (`pieces-complete`), S2 (`not retired`), S3 (`gotchas.py`)
and S4 (`--verdict FAIL`); AC5 is wiring and parity; AC6 is size and shape.

The gap is load-bearing because both dependent units discharge their user-docs obligation HERE.
`spec-3` §5: *user docs — `TOOL-aGradedMandate-8` names the escalation in the Skill's `--close`
section.* `spec-5` §5: names the split in the `--rescope` paragraph. So across the whole set nothing
observes either sentence: the escalation ships and the run that triggers it learns about it from no
carrier it reads — the exact defect class this unit exists to close. The kit's own arm comment names
it: a scope item with no arm is a scope item that can quietly not ship.

**Fix.** Add two greps in the AC1-AC4 idiom — `grep -c 'GATE_SELFTESTS'
.claude/skills/unattended/SKILL.md` at least 1, and a `retire` match inside the `--rescope`
paragraph.

**Left-shift.** Those two greps ARE the gate if they land in the kit's own leg rather than only in
the spec: `check-unattended.sh` already reads the rendered Skill for the directive join, so a third
assertion over the same file costs one comparison and survives the build.

---

### F19 — LOW · `spec-TOOL-aGradedMandate-9.md` §3 and `spec-TOOL-aGradedMandate-8.md` §3

Both units justify not rendering the DoD set into the Skill by naming "the ten items" — spec 9:
*The Skill deliberately does not enumerate the ten items*; spec 8: *Enumerating the ten items …
creates a fourth copy*. `DOD_CORE` at `unattended.sh:343` has exactly ten members today, and
`TOOL-aGradedMandate-2` at order 2 appends `specs-audited:machine` and raises the floor to eleven.
Units 8 and 9 land at orders 8 and 9. By then there are eleven.

A derived count written in prose, wrong on landing, in the two records a later reader consults for
why the Skill does not enumerate the set. Minor because the rationale is about COPIES and does not
depend on the figure — but the figure is wrong, and this repo reds that class elsewhere.

**Fix.** Replace "the ten items" with "the core Definition-of-Done set" in both non-goals.

**Left-shift.** None worth building. A gate over prose counts inside spec records would grade a
population that legitimately freezes at authoring time. The check that belongs here is the reviewer's
question, already in the charter: no count of a derived population is written in prose.

## What this pass did NOT cover

Stated so a green row is never misread as a verified one.

- **`TOOL-aGradedMandate-7` drew no confirmed finding.** That is a result, not a certification: it
  is the smallest unit in the set and its one cross-unit claim (S4 deferring the `not retired` edit
  to unit 8) is the only cross-reference in the whole set that is correctly written.
- **No finding grades whether a unit's IDEA is right.** This is a spec audit: it asks whether each
  spec describes the code it names, whether its criteria observe its scope, and whether building to
  its Inventory lands green. Whether `specs-audited` should exist at all is an owner question and is
  untouched here.
- **The refuted 27 are not re-litigated.** They were dominated by re-reports of stated non-goals and
  by findings whose reachability collapsed on a second read of the driver.
- **No arm was executed.** Every claim above is a read of tracked bytes at the shas in the range
  line, plus one live probe: `git show ":memory/builds/aThawedCorpus/README.md"` returning rc 0,
  which is F5's whole mechanism.
