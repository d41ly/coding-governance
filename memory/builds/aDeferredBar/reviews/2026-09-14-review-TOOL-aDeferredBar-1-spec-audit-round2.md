**Serves:** spec-audit TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

# aDeferredBar — spec audit of the three-unit set, round 2

*Node `a`, 2026-09-14. A Tier-2 adversarial pass over the three rev-2 specs of the `aDeferredBar`
build, reading the FOLD round 1 introduced rather than re-reading the whole set: four primed finder
lenses, five batched skeptic passes prompted to REFUTE every finding, one synthesis. Three claims
the surviving findings rest on were re-run at source during synthesis — unit 2's `BAR` regex, typed
from its §4, over the graded populations of all three rev-2 specs with the checker's own `TICK`,
`LEG_LINE` and `extract_gates`; the §4 Rollout reading of the newest spec filename date over every
ref and worktree; and the three fixture facts in `adopt-unattended.sh`, `unattended.test.sh` and
`test_codebase_map.py` — and the figures below are what those runs printed on this tree.*

**Round: 2.** Subjects, each pinned at the blob it was read at (all three match the working tree
at `ee7dabc2`, the tip that recorded phase `REVIEWING`; the fold itself is `e45578e8`):

- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md@d23187a7347cdd61977bf2831dc40b4d926e16d3`
- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md@893d1aa7c1cf000ad46ba6d2eb0b6f3db8b8a262`
- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-3.md@9faaf041b43d1da738da663ebe29746089f50b6c`

## Verdict: CLEAN WITH FIXES

No blocker, one high, seven mediums, four lows, after consolidating the fifteen confirmed findings
into the twelve below. Round 1's blocker is gone: unit 3's §6 no longer names the withheld suite as
an observation in six criteria, and the direct-observation shape unit 2 S5 set is now the shape all
three specs use. What round 2 finds is the residue of the fold, and it is of one kind throughout:
a value or a claim CARRIED into a criterion or a self-description when the sibling document, or
the source the claim is about, says it is DERIVED and has already moved.

The high is in unit 2 and is a design fact rather than wording. The cutoff relation the spec cites
as ratified has two clauses, and rev-2 applies one. The precedent it names, and the
`REV_SCOPE_CUTOFF` register comment in `.memory-tree.conf` that records it, put a new cutoff strictly
past the newest spec filename date on any ref AND past a date the fleet can still write into; the
second clause is why that value moved twice and why the comment reads "today is itself a date the
fleet can still write into". Unit 2 measured on 2026-09-14, found 2026-09-13, and set 2026-09-14 —
today — so a spec any node dates today and gives a bar token reds at its merge, which is the H3
class rev-2 records as closed. The §4 Rollout re-derivation command cannot repair it, because it
computes newest-plus-one and never reads the clock. Two mediums are the same defect one level down:
AC8 and AC9 assert the date as a literal byte string while §4 Rollout says the key follows the
relation, and unit 3's §3 asserts a property of its own §6 that unit 2's predicate, run over the
blob under review, shows is false by exactly one token.

The other five mediums are fixture and file-set facts a builder would hit at `BUILDING` or, worse,
at `VERIFYING` inside the 2569 s driver suite: an AC10 fixture that exits 1 today for a reason that
is not the hook, a files-table literal `run-branch: refs/heads/main` the fixture cannot produce and
the driver refuses outright, a generated artifact the new hook moves that the files table never
names, a half-stamp unit 1 declares and never observes, and a hand check unit 1 calls temporary that
is permanent by the sibling's own cutoff.

Every fix below is a fold into the document it names — a clause, a value, a grep, a fixture
precondition — and none needs a mechanism this build lacks, so the method's disposition is FOLD
for all twelve and the loop does not re-arm: the blocker count went from one to zero, and folding a
round's own fixes is what the next round would measure, not a reason to hold one.

**Review shape:** raw 34 · confirmed 15 · refuted 19 · unverified 0 · precision 0.44. Precision sits
below the charter's tighten-priming threshold of about 0.5. The refuted nineteen were mostly claims
about the fold being incomplete on a point it had in fact covered — a lens reading rev-1 text from
memory rather than the rev-2 blob — which is the priming defect the charter names and is the note
for a round 3 lens brief, should one ever be owed. The confirmed fifteen consolidate to twelve
because three pairs are one defect each found by two lenses, listed under one heading with both raw
ids; the counts on this line are the orchestrator's and are not re-derived by that consolidation.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every
lens and every skeptic batch came back, so the finding set is complete as far as a four-lens fan
reaches, and the zero unverified count is a count and not an absence of evidence. The dedup pass
reported zero duplicates and three of the pairs below are the same defect twice; that is a
consolidation this report makes, not a correction of the pass's count.

## Findings

| # | Sev | Spec | Address | One line |
|---|-----|------|---------|----------|
| H1 | high | 2 | §4 Rollout · §2 S4 · §8 Fork C · §6 AC8 red-when | The ratified relation has two clauses and the fold applies one; `2026-09-14` measured on 2026-09-14 is stale by construction |
| M1 | medium | 2 | §6 AC8, AC9 · §2 S4 | Two criteria assert the literal `SPEC_DIRECT_CUTOFF 2026-09-14` while §4 says the key follows a relation re-run at the build commit |
| M2 | medium | 3 | §3 last bullet · §6 AC9 · §8 F8 | §3 says the suite "appears in §6 only as prose"; AC9 backticks `gate-guard.test.sh` bare, and unit 2's `BAR` hits it — the one graded hit left in the set |
| M3 | medium | 3 | §6 AC10 | The fixture `seed()` builds exits 1 from `--check`'s first arm before any sixth arm runs; the RED-first `rc=0` is false and the positive half cannot be observed |
| M4 | medium | 3 | §4 Files touched (`unattended.test.sh` row) · §6 AC14 | The row pins `run-branch: refs/heads/main`; the fixture sits on `unit`, and a preflight with HEAD on `main` is refused at `unattended.sh:903` |
| M5 | medium | 3 | §4 Files touched (map row) · §6 AC12 | The `kit-js` layer indexes every `tools/**/*.js`, so `gate-guard.js` moves `symbols.json`; the files table names the dossier only and AC12 reds without a regen |
| M6 | medium | 1 | §2 S5 · §6 AC13 | S5 owes `last-audit` AND `last-body-change` in one commit; AC13 observes the first and `manifest-check.sh` grades the second only as non-empty and un-stalled |
| M7 | medium | 1 | §2 S6 · §3 line 72 | The hand check "until `TOOL-aDeferredBar-2` lands the gate that grades it" is permanent: unit 2's cutoff excludes this file by filename date forever |
| L1 | low | 2 | §2 S5 · §7 New arm | "`FLOOR_ASSERTIONS` from 20 to 31" has no observation; 31 executed against a floor left at 20 passes, and eleven arms could strand silently |
| L2 | low | 2 | §2 S2 | `NOT OBSERVED — a sentence in a docstring has no command that observes it` is false; AC10 and AC13 observe prose by pinned-phrase `grep -c` |
| L3 | low | 2 | §3 second bullet · §4 The one-token alignment | "differ on exactly one, unit 3's bare `GATE_FULL=`, which is unit 3's own fold to make" measures a unit 3 text the same commit replaced |
| L4 | low | 3 | §3 Edges, hands-off external | "a backlog row the main loop files at landing" is already filed as `TOOL-aDeferredBar-4`, in the same commit as this rev-2 |

Raw-id map, so the transcript reconciles: H1 = 26 · M1 = 4, 11 · M2 = 3, 10 · M3 = 22 · M4 = 23 ·
M5 = 21 · M6 = 5 · M7 = 8, 15 · L1 = 6 · L2 = 9 · L3 = 16 · L4 = 30. Raw ids 8 and 15 arrived as
low and medium for one defect; the severities in the table are this report's, adjudicated per
consolidated finding.

---

### H1 — high — unit 2 §4 Rollout, §2 S4, §8 Fork C, §6 AC8 red-when: half of the ratified relation, and a value that is stale the day it is written

The precedent the spec cites is an owner ruling, `TOOL-aJoinedCanon-1` §8 F1, and the register
comment on `REV_SCOPE_CUTOFF` in `.memory-tree.conf` (lines 131 to 140) records what it says: a new
cutoff sits "strictly past the newest spec filename date on any branch, AND past a date this fleet
can still write into". The comment then records the value moving twice for the second clause alone —
measured 2026-09-06 on 2026-09-05, re-derived 2026-09-07 on 2026-09-06, re-derived again at landing
on 2026-09-07 to 2026-09-08, "today is itself a date the fleet can still write into with live
unattended runs in it. The relation returns [today plus one]" — and names it the reason a value
carried across a day boundary is stale by construction. `SPEC10_EVIDENCE_CUTOFF` records the same
correction a week earlier.

Unit 2 §4 Rollout, S4 and Fork C quote the first clause only. The reading was taken 2026-09-14, the
newest spec anywhere was 2026-09-13, and the key is set to 2026-09-14 — the measuring day. Re-run
at synthesis over 77 refs and every worktree of `git worktree list`: the newest spec filename date
is still 2026-09-13, so the first clause returns 2026-09-14 and the second returns 2026-09-15, and
the spec's value is the one the precedent corrected twice. Any spec another node dates today and
gives a bar token — a live unattended run on nodes `b`, `c` or `d` writes specs dated today — reds
`spec tokens` at its merge with `origin/main`, the leg being `subject: repo` and unguarded. That is
the H3 class the rev-2 log records as closed. The §4 Rollout re-derivation command cannot catch it:
both pipelines compute newest-plus-one and neither reads the clock, so re-running it today returns
the same wrong value. AC8's red-when carries the first clause only as well.

**Fix.** State both clauses in §4 Rollout, Fork C and the S4 conf comment, in the register's own
idiom. Derive the value as the day after the LATER of the newest spec filename date on any ref or
worktree and the build commit's own date (`git log -1 --format=%cs`), re-derived at the build commit
and again at landing, as `REV_SCOPE_CUTOFF`'s comment prescribes. Add to AC8's red-when: the cutoff
is not strictly past `git log -1 --format=%cs` of the build commit. Record the consequence the
register already states for every other cutoff: on the landing day the join grades zero specs, and
the first real verdict arrives with the first spec dated after landing.

**Left-shift.** The relation is a documented check on every cutoff row and this is the second time
the second clause was dropped in a fold, so it earns a machine form. One `spec-tokens self-test`
arm: the fixture sets `SPEC_DIRECT_CUTOFF` equal to a spec date present in the scratch tree and
asserts the checker REFUSES with a line naming the key and the newest date it saw, exit non-zero —
a liveness assertion in the checker itself for the first clause on the tree it grades. The second
clause stays a documented check at the register comment, because a bar grades a tree and not a
calendar; AC8's new red-when is where it is observed for this unit.

### M1 — medium — unit 2 §6 AC8, AC9 and §2 S4: a literal for a value the same spec says is derived

AC8's expected bar line reads `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF
2026-09-14`, AC9's expected `NEAR` text reads `predates SPEC_DIRECT_CUTOFF 2026-09-14`, and S4 pins
the key "at `2026-09-14`". §4 Rollout says the command "is re-run at the build commit — if the day
has rolled and a sibling has landed a spec dated 2026-09-14, the relation moves and the key follows
it", and AC8's own red-when independently asserts the relation. Both cannot hold once any ref
carries a spec dated 2026-09-14, and under H1's fold the value moves to 2026-09-15 or later before
the unit is built, so a correct build reds AC8 and AC9 on the literal while satisfying their red-when.
No `figure:` line marks the date PINNED; the spec applies its own DERIVED-versus-PINNED convention to
every count and not to the date.

**Fix.** In AC8 and AC9 replace the literal with the relation's reading: the date the line names
equals the conf's value and is strictly past both clauses of H1 at that commit; add
`figure: DERIVED at the build commit; 2026-09-14 was the first-clause reading on 2026-09-14` to AC8.
S4 and Fork C state the value as "the relation's answer at the build commit, 2026-09-15 by both
clauses as measured 2026-09-14".

**Left-shift.** H1's checker refusal covers the class for the value; nothing further is owed for
the criteria, because a criterion asserting the relation rather than the byte string cannot rot.

### M2 — medium — unit 3 §3 last bullet, §6 AC9, §8 F8: the one graded hit the fold left, under a sentence that says there are none

Unit 3 §3's rev-2 bullet asserts "§6 cites rows and never spells an invocation as an observation,
and the suite S5 names appears in §6 only as prose". AC9's third clause reads "its printed set names
`gate-guard.test.sh` under the kit directory" — a bare `*.test.sh` basename inside a backticked §6
bullet, which unit 2 §4 and Fork E say in so many words "stays a hit, because naming a suite as the
observation is the exact shape the owner forbade". Reproduced at synthesis with unit 2's `BAR`
typed from its §4, the checker's `TICK` and `LEG_LINE`, the bullet regex and an `AC_HEAD`-located
acceptance section over all three rev-2 blobs: units 1 and 2 yield zero graded hits, unit 3 yields
exactly one, that token on line 403. Round 1's B1 listed AC9 among the nine; the fold removed eight.
So §3's claim, the rev-2 log's "named in prose and under New arm: only", and F8's premise ("a
document that no longer needs it") are all false on the blob under review, and unit 2 §3's "24
carriers at HEAD, because this build's own unit 3 is one" is carried by this very token.

Caveat on impact, stated so the severity is read correctly: `SPEC_DATE` in
`tools/check-spec-tokens.py:79` is filename-derived, so this file stays pre-cutoff forever and unit
2's gate will never red on it. The defect is a false self-description and an incomplete fold, not a
future red; it is medium because F8 and unit 2's carrier count both rest on the false sentence.

**Fix.** Un-backtick the second AC9 mention ("its printed set names the suite S5 names, under the
kit directory"); the first mention, a `grep` argument with `grep` at command position, is not a hit
and may stay. Add to §3's last bullet the sentence unit 1 S6 carries: unit 2's `BAR` regex, typed
from its §4, matches no backticked token of this §6, probed on the date. Re-read F8 against the
result; its resolution stands, its premise sentence does not.

**Left-shift.** For post-cutoff specs the class is unit 2's gate, and the SPEC-stage writer running
`--list` before returning is `TOOL-aDeferredBar-6`, already filed. For this pre-cutoff file the
observation is unit 2's own AC9 at its build commit: the distinct-spec count on `NEAR` lines must
not include unit 3 once folded, which is one number the pass already prints.

### M3 — medium — unit 3 §6 AC10: a fixture that cannot reach the arm it observes

AC10's fixture is "a scratch tree seeded as the adopter suite's `seed()` seeds one but with no
`.claude/settings.json`", and its RED-first observation says that tree "against the adopter as it
stands prints `rc=0`". `seed()` (`adopt-unattended.test.sh:34-56`) copies the kit files and writes
the conf and nothing else. `adopt-unattended.sh --check` refuses sequentially, and its FIRST arm
(line 259, `$SKILL_OUT is not rendered — run $0`) exits 1 on exactly that tree, before any sixth
arm could run; the suite's own arm 1 reaches `--check` at line 76 only after running the adopter's
install at line 63. Reproduced: a tree seeded as `seed()` seeds one exits 1 from the Skill arm. So
the RED-first claim is false as stated, and the positive half ("stdout names the hook UNWIRED", then
`rc=0` with the marker) cannot be observed on that fixture at all, because `--check` never reaches
a sixth artifact on a tree where the first five are absent.

**Fix.** State the precondition in AC10: after seeding, run the adopter's install
(`bash tools/unattended/adopt-unattended.sh`, no verb, as arm 1 does) inside `FIX` so the five
existing artifacts are present, THEN omit or remove `.claude/settings.json` and run `--check`. The
RED-first then reads `rc=0` on the adopter as it stands, and `rc=1` naming UNWIRED once the sixth
arm exists.

**Left-shift.** The adopter suite's new arm is the gate once its fixture carries the precondition —
which is the H5 fold the files table already records for `seed()`. Observe the sixth arm RED first
by running `--check` on an installed-then-unwired scratch tree; nothing else is owed.

### M4 — medium — unit 3 §4 Files touched, the `unattended.test.sh` row, and §6 AC14: a literal the fixture cannot produce

The row pins the new driver-suite arm to "a default-branch-anchored preflight writes
`run-branch: refs/heads/main`". The fixture it names ("beside 50d at line 2897", an existing
fixture) opens with `reset_tree`, which is `git checkout -q unit` (`unattended.test.sh:355`), so
`git symbolic-ref HEAD` at that preflight is `refs/heads/unit`. Worse than fixture-specific: a
preflight with HEAD on `main` cannot succeed in that suite at all, because `unattended.sh:903`
returns the refusal when the merge-base equals HEAD on the default-branch anchor. The literal is
impossible, and it also contradicts the spec's own definition of the fact — the run's LOCAL branch,
distinct from the anchor branch, which is the whole point of unit 3's F7. §4 "The key" and AC14 say
only `refs/heads/<branch>` and "reads the fact back", so the row is the only place the wrong value
is spelled — and a builder writing the arm to the row fails it at `VERIFYING` inside the 2569 s
driver suite, the most expensive place this build exists to stop verdicts arriving, and pays a
second full run for the fix.

**Fix.** Spell the expected value from the fixture — `run-branch: refs/heads/unit` — or, better,
have the arm assert against `$(git symbolic-ref HEAD)` of the fixture rather than any literal, and
say so in the files-table row and in AC14's last sentence.

**Left-shift.** An arm that reads the expected value from the fixture cannot carry this class. The
break the §7 line names — a driver that does not write the fact — is the RED-first observation; make
it directly, on the driver with the `set_fact` line removed, before the suite runs at `VERIFYING`.

### M5 — medium — unit 3 §4 Files touched, the map row, and §6 AC12: a generated artifact the hook moves and the table never names

AC12 asserts `python tools/codebase-map/test_codebase_map.py` exits 0 at the build commit "with the
`unattended` dossier refreshed and no new key claimed". Its `__main__` path (lines 244 to 252) runs
`test_generated_artifacts_are_fresh`, which byte-compares the tracked
`memory/map/generated/symbols.json` against a live render, and the `kit-js` symbol layer
(`map_extractors.py:212-213`, `enumerate_exports` plus `scan_js_definitions` over all of `tools/`)
indexes every kit `.js` — `symbols.json` already carries `tools/hooks/scratch-guard.js` and
`tools/process-monitor/procmon-hook.js`. A new `tools/unattended/gate-guard.js` exporting ten
functions therefore moves `symbols.json`, and AC12 reds unless `python tools/codebase-map/gen_map.py
--write` runs in the same commit. The files table (line 296) names the dossier only and says "no
inventory key is claimed", which is true of `inventories.json` and silent about the generated set;
unit 2's table (line 290) does name `memory/map/generated/` for a one-function edit. The
`codebase-map coverage + freshness` leg is a merge-bar leg the charter forbids exempting, so the pass
either discovers the omission by a red AC12 or lands a stale artifact for the main loop's bar.

**Fix.** Add a `memory/map/generated/` row to the files table — `symbols.json` re-rendered by
`python tools/codebase-map/gen_map.py --write` after the hook lands, because the `kit-js` layer
enumerates the new file's definitions — and reword AC12 to say the freshness test covers
`symbols.json` and passes only after that re-render. The dossier-only claim stays true for
inventories.

**Left-shift.** The freshness test IS the gate and reds with the regen remedy printed; the fold
only moves the discovery from `BUILDING` to the spec. Nothing new is owed.

### M6 — medium — unit 1 §2 S5 and §6 AC13: the half-stamp, declared and not observed

S5 says the manifest "is re-stamped in the same commit: `last-audit` and `last-body-change`",
observed by AC12 and AC13. AC12 runs `manifest-check.sh`; AC13 greps the delta line and
`@ $(git merge-base origin/main HEAD)`, which is `last-audit`'s sha. `manifest-check.sh` grades
`last-body-change` as non-empty (line 219, check 2), as a full ancestor sha, and against the
ten-commit and three-month stall (lines 386 to 403, check 9); nothing ties it to the body edit, and
C5 reads `last-audit`. So a build that qualifies line 263, re-stamps `last-audit` and leaves
`last-body-change` at `2661b66b` passes every unit 1 criterion and lands the half-stamp the `stamps`
gotcha records ("the gate's own remedy names only three"). Unit 3's rev-2 added the observation for
its own manifest row — AC13 there greps `^last-body-change: $(git rev-parse HEAD~1)` "as unit 1's S5
spells them" — while unit 1's fold list (M2, M3, M4, M7) never touched AC13. The set already
confirmed this class once, as round-1 L4.

**Fix.** Append to AC13: `grep -c "^last-body-change: $(git rev-parse HEAD~1)"
memory/guides/SESSION-KICKOFF.md` prints `1`, with the red-when "or `last-body-change` still names
`2661b66b`".

**Left-shift.** C9 is late by design and C5 reads one stamp. The class is gateable in the kickoff
kit: when the diff touches the manifest BODY outside the audit block, `last-body-change` must name a
sha at or after the last body-touching commit before HEAD. That is one arm for `manifest-check.sh`
and a backlog row for the kickoff kit, not this unit's build.

### M7 — medium — unit 1 §2 S6 and §3 line 72: a hand check called temporary that is permanent

S6 says the bar-token absence "is hand-checked at the acceptance ledger until
`TOOL-aDeferredBar-2` lands the gate that grades it", and §3 says of the live bar-naming specs that
"the live ones are unit 2's population". Unit 2 §3 states that its cutoff grades zero tracked specs
at landing, "this build's own three specs included, which are dated 2026-09-13 and are therefore not
graded either", and unit 3 §3 absorbed that and says so of itself. `SPEC_DATE` reads the filename
date, which never changes, so unit 2's gate never grades this file: the hand check S6 presents as an
interim is the only observation there will ever be, and a reader waits for a machine verdict that
cannot arrive. Line 72's population claim is false against the sibling for every live spec too,
since none is dated at or after the cutoff. The property itself holds today — the synthesis probe
under M2 returned zero for this file.

**Fix.** Reword S6 the way unit 3 §3 does: this spec is outside that gate's population by the
cutoff, and the acceptance-ledger hand check is the observation, not a stopgap. Reword line 72 to
say the live ones are graded by unit 2 only when dated at or after its cutoff, which none is. If a
criterion is wanted, add AC16: unit 2's `BAR` regex, typed from its §4 into a one-line `grep -cE`
over this file's acceptance section, prints `0` — a heredoc-free form, because a `python - <<EOF`
observation is a heredoc and the ledger cannot run one.

**Left-shift.** None. A false clause about which gate observes a scope item is caught by exactly
this kind of read; the S6 probe sentence, once the spelling is fixed, is the documented check.

### L1 — low — unit 2 §2 S5 and §7 New arm: the floor moves and nothing reads it

S5 and the §7 `New arm:` line both say `FLOOR_ASSERTIONS` moves "from 20 to the count the suite
prints, 31 if all land"; S5's "Observed by AC1 through AC7, AC15 and AC16" names criteria that
observe the arms' fixtures, none of which reads the floor. `tools/check-spec-tokens.test.sh:15`
sets `FLOOR_ASSERTIONS=20` and line 196 tests `[ "$total" -lt "$FLOOR_ASSERTIONS" ]`, so 31
executed against a floor left at 20 passes, and the suite's verdict at `VERIFYING` cannot tell a
moved floor from a stale one. The floor exists to red when arms strand past an early exit; left at
20, eleven of the new arms can vanish with the suite green — the green-by-absence class §7 of the
charter names, and the shape round 1 confirmed as M8.

**Fix.** One clause in AC8 or a new criterion: `grep -c '^FLOOR_ASSERTIONS=31'
tools/check-spec-tokens.test.sh` prints `1`, the count being static (the nine arms and the inline
`--list` check sum to it).

**Left-shift.** None beyond the grep. The floor is a shrink-only pin by the pattern
`scratch-guard.test.sh:239` states, and a pin is observed by reading it.

### L2 — low — unit 2 §2 S2: NOT OBSERVED on a reason the same spec disproves

S2 is marked `NOT OBSERVED — a sentence in a docstring has no command that observes it; the spec
audit reads it`. The template admits the marker with a reason, but the reason is false and this
spec's own criteria say so: AC10 and AC13 observe prose carriers by `grep -c` on a pinned phrase,
and units 1 and 3 pin one phrase per prose carrier. The docstring paragraph is load-bearing — §5 risk
5 names "the docstring says so" as the remedy for the runtime-path and `sh -c` evasions, and §7 of
the charter requires a gate's own header to state what it does not check — and as written it can be
dropped or half-written with no red anywhere, including at `VERIFYING`.

**Fix.** Pin one phrase per docstring clause in §4 (`the body of a \`sh -c\` string`, `finds the
acceptance section by heading text`, and the two others) and add a criterion: each `grep -c` over
`tools/check-spec-tokens.py` prints `1`. Drop the `NOT OBSERVED` clause from S2.

**Left-shift.** None; pinned-phrase greps are the observation.

### L3 — low — unit 2 §3 second bullet and §4 "The one-token alignment": a measurement of a text that no longer exists

§3 says "on this tree at HEAD the count is 24, because this build's own unit 3 is one", and §4 says
the old and new `BAR` spellings "differ on exactly one, unit 3's bare `GATE_FULL=`, which is unit 3's
own fold to make". Both were measured against unit 3 rev-1. At `27ba9c0c` unit 3's graded
populations held one bare `GATE_FULL=` plus seven `gate-guard.test.sh` tokens and one
`run-selftests.sh` invocation; at HEAD, rev-2 carries `GATE_FULL=` only in §3 and §4 prose (three
mentions, none graded), and its one graded token is the AC9 `gate-guard.test.sh` M2 names, which
BOTH spellings hit. So the fold §4 directs was already made in the commit that wrote this sentence,
and the token that keeps unit 3 in the carrier count is misnamed. No criterion breaks — every figure
is DERIVED — but the rev-2 measurement prose is false at the HEAD it claims to measure.

**Fix.** Re-run the measurement against unit 3 rev-2, name the actual token (or state that the two
spellings agree on every graded token once M2 is folded, which makes unit 2's count 23 at HEAD), and
drop "which is unit 3's own fold to make".

**Left-shift.** None; the figures are DERIVED and the prose beside them is the thing that rots,
which is the charter's own warning about numbers typed beside their source.

### L4 — low — unit 3 §3 Edges, hands-off external: a landing action already done

The edge describes the govkit `selfcheck` arm for a `*.test.sh` under a kit directory with a budget
row and no `project-owned` claim as "a backlog row the main loop files at landing", and §9 says the
arm "is the backlog row §3 hands off" without naming it. `TOOL-aDeferredBar-4`
(`memory/backlog/TOOL.md:468`) is that row, filed from round-1 M8 naming the same
`check-brief-recorded.test.sh` instance, and it landed in `e45578e8` — the commit that wrote this
rev-2. A landing that follows the spec files a duplicate row for one defect.

**Fix.** Cite `TOOL-aDeferredBar-4` in the edge and in §9's hands-off clause; delete "a backlog row
the main loop files at landing".

**Left-shift.** None. The backlog's stable-id discipline is the check; a duplicate row is caught by
the next reader of the family backlog, which is where this was caught.

## What this round did not cover, said so a green row is not misread

- No code exists yet; every finding is against a spec, and the refuted nineteen are not listed here.
- Round 2 read the fold. Criteria round 1 passed and rev-2 did not touch were not re-audited; the
  method says a synthesis that called a spec clean stops reviewing it, and units 1 and 2 were called
  CONVERGED at round 1 with fixes folded. M6, M7, L1, L2 and L3 sit in those units because the fold
  itself introduced or exposed them.
- The `BAR` reproduction used the checker's `TICK`, `LEG_LINE` and `extract_gates` imported from
  `tools/check-spec-tokens.py` at `ee7dabc2` and unit 2's regex typed from its §4, with an
  `AC_HEAD`-located acceptance section; the shipped regex may differ once built, and unit 2's own
  AC8 is where that is graded.
- The relation reading under H1 was re-run at synthesis over 77 refs and every worktree; it is a
  reading on 2026-09-14 and moves the moment any node lands a spec dated today.
- No in-flight spec on another ref was audited; the four round-1 H3 named were not re-read.

## Disposition

- All twelve are FOLD, into the document each names; none needs a mechanism this build lacks and
  none is promoted.
- Unit 2: rev-3 folds H1, M1, L1, L2, L3. H1's fold is a value derivation and three clauses, and it
  changes the value the unit lands.
- Unit 3: rev-3 folds M2, M3, M4, M5, L4. The round-1 blocker is closed; the residue is one token,
  two fixture preconditions, one files-table row and one citation.
- Unit 1: rev-3 folds M6 and M7 — one grep clause and one reworded sentence.
- The loop does not re-arm: confirmed blockers went 1 → 0, and the method's rule is that folding a
  round's own fixes is what a next round measures, not a reason to hold one. The main loop verifies
  the fold by three probes this report already ran: the `BAR` probe under M2 prints `0` for every
  spec, the relation reading under H1 returns a date the conf value is strictly past by both clauses,
  and the AC10 fixture under M3 prints `rc=0` after the install step on the adopter as it stands.
