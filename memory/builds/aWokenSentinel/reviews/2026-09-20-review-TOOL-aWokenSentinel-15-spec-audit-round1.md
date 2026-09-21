**Serves:** spec-audit TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20

# aWokenSentinel — spec audit of units 15 to 20, round 1

*Node `a`, 2026-09-20. A Tier-2 adversarial pass over the six specs the round-2 disposal
commissioned, before any code: a fan of four primed finder lenses, a skeptic stage in five batches
prompted to REFUTE each finding, one synthesis. The mandate was the one both earlier rounds ran:
underspecification, contradiction between sibling specs on the four axes (scope, interface,
ordering, acceptance), unstated assumptions about the harness and the driver, and criteria that
cannot fail, with every code claim checked against the cited file and line at HEAD `830c46e8` and,
where a spec names it, at the build's base `12513c25`. The synthesis re-read at source every claim
the highs rest on and most of the mediums; what it re-read, and what it did not run, is listed at
the end.*

**Round: 1.** Subjects, each pinned at the blob the commission named:

- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-15.md@0d9a6f324435066a97d9a096c68ce5f0acbe59b9`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-16.md@3c9a8097dc9ec3b8bc32c9526f82e21cdc78160e`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-17.md@6da8a448907110d301c0ad66c89ed2a6aa5d80a2`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-18.md@ff4f175d5088ecddf416e9ced1a187733ea4ea08`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-19.md@ad43614ce06ba34fd745a4c4215ce90452f8a4a0`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-20.md@4e089c2db59c1e2d6d56aff27428df987e5857c3`

Every pin names the text that was reviewed. The synthesis ran `git rev-parse HEAD:<path>` and
`git hash-object <path>` for all six at the time of writing: each pair agrees with the pin above,
and `git status` lists no subject as modified. The provenance class round 2 found twice (B1, B2)
does not recur here, which is the outcome unit 15 exists to make structural.

## Verdict: CLEAN WITH FIXES

No blocker stands. No unit inverts its purpose, no sibling contradiction leaves a merge-bar leg red
with no unit owning the fix, and no pin names a text other than the one the lenses read. Six raw
findings in four defects are high, and every one is a fold with a named fix. Spec 15 places its
dirty-tree compare OUTSIDE the resolver branch, so as designed it throws on every caller-supplied
subject set, including all fifteen fixtures the harness suite already feeds through the audit stage,
and its §5 says the opposite. Spec 16 replaces one `fail 34` sentence with four, arms two of them,
calls them "the two new sentences" in §7, and lists the `harness arms` leg among its gates, which
reds on the two it did not arm. Spec 17's one-line helper reads an EMPTY stdout as one line, because
`printf '%s\n' "" | wc -l` prints `1`, so the case its §5 says "reds as loudly as 2" passes. Spec 18
spells its own staged break two incompatible ways, and the one its sibling agreement lands on
cannot produce the reading its AC states. Twenty-one raw findings in fifteen defects are medium and
six in six are low; the medium band is dominated by one class, a scope item whose claimed observer
cannot see it, and by a second, a base-side figure that the file at `12513c25` cannot produce
because a predecessor unit at a lower order writes it. Every unit drew at least one confirmed
finding; spec 18 drew the most.

## Review shape

Raw 43, confirmed 33, refuted 10, unverified 0, precision 0.77. That is above round 2's 0.58 and
close to round 1's 0.80, and above the ~0.5 floor §8 sets. The six specs are shorter and more
uniform than the fourteen before them, which is the likely reason: each names one audit finding in
its §1, one mechanism in its §4 and one to three arms in §7, so a lens has less surface to
misread.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by
the pipeline's dedup stage. The run is complete on its own terms. Because no lens died, no zero
below is a zero from absence; every unit was read by all four lenses. The pipeline's dedup found 0,
but the 33 confirmed ids contain several that name one defect from different lenses (three found
spec 15 AC4's check-arms clause, three found spec 16's unarmed sentences, two found spec 18's
base-lib break, two found each of the two case-sensitive needles, two found spec 7's third reader).
The fold below is editorial: it groups them into 25 distinct defects and keeps every raw id. Each
raw id takes the severity of the defect it evidences, so the per-id tally and the integers returned
with this report agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| H1 spec 15's compare sits outside the resolver branch; every supplied subject reads dirty | high | 26 |
| H2 spec 16 writes four `fail 34` sentences, arms two, and lists the leg that reds on the other two | high | 5, 17, 27 |
| H3 spec 17's one-line helper reads empty stdout as `1`; the empty case cannot fail | high | 28 |
| H4 spec 18 spells its staged break two ways; the sibling-agreed one cannot produce AC2's reading | high | 18 |
| M1 spec 15 AC4's check-arms clause names an observation the tool cannot make | medium | 1, 22, 36 |
| M2 spec 15 S1's `required: tree` is observed by no criterion | medium | 2 |
| M3 spec 15 S5's limit sentence is observed by no criterion; AC3's threshold is met without it | medium | 3 |
| M4 spec 16 S4's `-7` citation and does-not-prove sentence are observed by nothing | medium | 6 |
| M5 spec 17 AC2's driver copy refuses at exit 2 without the lib beside it; the red reading is unreachable as written | medium | 29 |
| M6 spec 7 AC5 is a third whole-line reader, one order before the helpers, and spec 17 hands it nothing | medium | 23, 41 |
| M7 spec 13's BLOCK-copy reading is recorded against a guard that lands one order later | medium | 19 |
| M8 spec 18's "lib at this unit's base" holds no `read_bound_key`; the RED reading is `command not found` | medium | 10, 32 |
| M9 spec 18 AC4's needle prints 0 on the landed fold; "two breaks" is four | medium | 20, 33 |
| M10 spec 18's `-f` half of the guard has no failing observation | medium | 9 |
| M11 spec 19 adopts the remedy `TOOL-dUnstalledConvoy-19` judged insufficient, cites it, and does not engage it | medium | 42 |
| M12 spec 19 names a per-suite log the close's runner never persists | medium | 31 |
| M13 spec 20 S4 names three folds; AC4 observes two, one by a count that cannot fail on the fold | medium | 14 |
| M14 spec 20 AC4's needle prints 0 on the landed fold | medium | 21, 35 |
| M15 spec 20 AC1's base figure is false at `12513c25` | medium | 34 |
| L1 spec 15 §4 says the prompt asks for 40 hex; the quoted sentence and the schema do not | low | 25 |
| L2 spec 18 S1's header sentence is unobserved; AC4's second clause has no command | low | 11 |
| L3 spec 19 S2's pin comment is unobserved | low | 13 |
| L4 spec 19 names units 3 and 5 as the adopter suite's arm writers; it is 3 and 4 | low | 24 |
| L5 spec 20 S1's verbatim move and `return 1` branch are unobserved | low | 15 |
| L6 spec 20 S3's header sentence is unobserved; AC3's threshold is met without it | low | 16 |

Tally by raw id: **0 blocker · 6 high · 21 medium · 6 low** = 33. One severity was LOWERED from
the skeptic's verdict: raw 1 (skeptic: high) sits in M1 beside 22 and 36 (skeptic: medium), because
the three ids name one defect and one defect has one severity; the argument for medium rather than
high is in M1's section — the arms the clause claims to certify are observed RED-first by AC1 and
AC2 against the base render, so what is vacuous is a meta-clause about them, not the arms. No
severity was raised. H1 and H2 were each weighed for blocker and left at high, argued in their
sections.

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| H1 | high | TOOL-15 | §2 S2; §4 'The refusal'; §5 migration; §6 AC1, AC2 | `badSubject` sits after and outside `if (!subjects)` (`unattended-build.js:642,669`); the compare "directly after" it runs over caller-supplied `{path, blob}` subjects, `undefined !== blob` is dirty, and fifteen suite fixtures throw. |
| H2 | high | TOOL-16 | §2 S1, S2, S3; §4 Inventory; §6 AC2, AC4; §7 | Four new `fail 34` sentences, two armed, §7 says "the two new", `harness arms` listed as a gate; `check-arms.py` already grades check 34's four branches ARMED and reds the two unarmed ones at the close. |
| H3 | high | TOOL-17 | §4 'The two helpers'; §5 error states | `printf '%s\n' "$_o" \| wc -l` prints `1` on empty `$_o`; `same … "1"` passes on a verb that wrote nothing; §5's "reads 0 lines" is false. |
| H4 | high | TOOL-18, TOOL-13 | TOOL-18 §3 Edges vs §2 S3 and §6 AC2; TOOL-13 §6 AC2, §7 | Edges remove "the two calls" with the block; S3/AC2 remove four lines and keep them; only the second can print the guard's sentence; spec 13 §6 defines the BLOCK copy as the whole seven-line §4 block, calls included. |
| M1 | medium | TOOL-15 | §6 AC4 second clause, against §7 | `check-arms.py discover()` reads tracked `*.sh` defining `fail() {` and skips `*.test.sh`; neither harness file is in its population; `--report` lists ten shell gates and nothing under `tools/workflows/`. |
| M2 | medium | TOOL-15 | §2 S1; §5 error states | No AC feeds the stub a `{path, blob}`-only return; the suite's `run_wf` agent stub never reads `opts.schema`, so `required` is unobservable through it anyway. |
| M3 | medium | TOOL-15 | §2 S5; §6 AC3 | AC3's `grep -c 'hash-object'` ≥ 2 is met by the prompt sentence plus the §4 schema comment; no string from the limit sentence is pinned. |
| M4 | medium | TOOL-16 | §2 S4; §6 AC4 | AC4 greps `dUnstalledConvoy-38` only; the `TOOL-aUnblockedFleet-7` citation and the does-not-prove sentence S4 requires are read by nothing. |
| M5 | medium | TOOL-17 | §4 'The staged breaks'; §6 AC2 | `unattended.sh:72-75` derives `KIT_DIR` from `$0` and exits 2 without `lib-unattended.sh` beside it; the suite's stripped-copy arm at `:2092-2095` copies the lib, the L2 arm at `:5022` deliberately does not; the spec names neither. |
| M6 | medium | TOOL-17, TOOL-7 | TOOL-17 §3 Non-goals, Edges; TOOL-7 §6 AC5, §7 | Spec 7 (order 16) AC5 asserts `run --status tRun \| wc -l` is 1 through `run`'s `2>&1`, the shape spec 17 §4 rejects; spec 17 says the whole-line readers are two and hands off to unit 9 only. |
| M7 | medium | TOOL-18, TOOL-13 | TOOL-18 §1, §2 S4; TOOL-13 §6 AC2, §7 | Unit 13 is order 13, unit 18 order 14; spec 13 AC2 records the BLOCK copy as "exit 2, the guard sentence, zero NOTEs", which at order 13 reads two empty-path NOTEs, exit 0, attempt 1 launched. |
| M8 | medium | TOOL-18 | §6 preamble, AC1, AC2, AC3; §7 | `git show 12513c25:tools/unattended/lib-unattended.sh \| grep -c read_bound_key` prints 0; the function is at `unattended.sh:358` there and unit 5 (order 11) hoists it; the bare-shell call at that base exits 127. |
| M9 | medium | TOOL-18, TOOL-13 | TOOL-18 §6 AC4 | `grep -c 'whole four-line'` over spec 13 prints 0 at HEAD (it spells `WHOLE four-line`); spec 13 §7 names four breaks, not two. |
| M10 | medium | TOOL-18 | §2 S1; §5; §6 AC1 | AC1 runs with `CONF` unset, AC2's block removal is also unset, AC3 sets an existing conf; `CONF=/nonexistent` is exercised nowhere, so `[ -n "${CONF:-}" ]` alone passes every AC. |
| M11 | medium | TOOL-19 | §3; §4 'Why a static count'; §5 risks; §10 | `TOOL-dUnstalledConvoy-19` (OPEN) rules a numeric floor with headroom "fixes the instance and not the class" and asks for a one-grep structural arm; spec 19 installs eight assertions of slack directly above `exit "$st"` and names no such arm. |
| M12 | medium | TOOL-19, TOOL-14 | TOOL-19 §2 S3, §4 last paragraph, §7; TOOL-14 §6 AC5 | `run-selftests.sh` writes each suite under a `mktemp -d` removed by its EXIT trap (`:492-493`) and prints only `ok <name> <s>s`; no per-suite log persists and `PASS (<n> assertions)` never surfaces. |
| M13 | medium | TOOL-20 | §2 S4; §6 AC4 | S4 names three folds (specs 11, 5, 2); AC4 says "both", greps spec 11 and spec 5, never spec 2; the spec 5 read is a `≥ 6` mention count that any unrelated mention satisfies. |
| M14 | medium | TOOL-20, TOOL-11 | TOOL-20 §6 AC4 | `grep -c 'code lines'` over spec 11 prints 0 at HEAD (it spells `CODE lines` and `code-line`); AC4 says the fold already landed, so the criterion is red on the state it declares satisfied. |
| M15 | medium | TOOL-20 | §6 AC1 | "At this unit's base the two print 0 and 1" — `git grep 'rev-parse --git-dir' 12513c25 -- <lib> <driver>` returns nothing; both print 0; the driver's 1 exists only at unit 2's tip. |
| L1 | low | TOOL-15 | §4 prose below 'The refusal', against the quoted prompt sentence and S1's schema | The quoted sentence carries no 40-character ask; the schema admits `{7,40}` on both fields; an abbreviated side refuses as "dirty" with a remedy that is false for a clean tree. |
| L2 | low | TOOL-18 | §2 S1 header; §6 AC3, AC4 second clause | AC3's grep matches the refusal echo, not the header; "spec 13's §7 names two breaks" has no command and spec 13 names four. |
| L3 | low | TOOL-19 | §2 S2; §6 AC4 | AC4's `grep -c 'FLOOR_ASSERTIONS'` ≥ 2 is the pin plus the compare; a bare `FLOOR_ASSERTIONS=64` with no rule passes. |
| L4 | low | TOOL-19 | §4; §6 AC1 figure note; §3 Edges | Spec 5 never touches `adopt-unattended.test.sh`; the arms before order 19 are unit 3's (order 6) and unit 4's (order 10), and spec 4 §7 still says "no floor exists in this suite". |
| L5 | low | TOOL-20 | §2 S1; §6 AC2 | AC2 runs the function only inside a repo and a worktree; the `[ -n "$_sd" ] \|\| return 1` branch and the verbatim move are diffed by nothing. |
| L6 | low | TOOL-20 | §2 S3; §6 AC3 | AC3's `grep -c 'resolve_sidecar_dir'` ≥ 2 is the definition plus the rule comment §4 places above it; the file header can stay untouched. |

### H1 — high — TOOL-15 §2 S2, §4 'The refusal', §5 migration, §6 AC1 and AC2 — raw 26

**The defect.** Re-read at source: `tools/workflows/unattended-build.js:635` is
`let subjects = Array.isArray(a.subjects) ? a.subjects : null`; the resolver agent runs only inside
`if (!subjects)` at `:642`; the `badSubject` refusal at `:669` sits AFTER that branch closes and runs
over whichever `subjects` survived, supplied or resolved. S2 and §4 place the compare
`subjects.filter(s => s.tree !== s.blob)` "directly after the existing `badSubject` refusal", which
puts it on the supplied path too. A supplied subject is `{path, blob}` by the callee's contract the
spec itself states in S3, so `s.tree` is `undefined`, `undefined !== s.blob` holds, and every
supplied subject is dirty. `tools/workflows/unattended-build.test.sh` carries fifteen fixtures
(`UNITS` at `:89`, `A_UNITS` at `:309`, `F_UNITS` at `:348` and their siblings) whose args hold
`"subjects":[{"path":…,"blob":…}]` and reach the audit stage; as designed every one throws
`Commit the fold` for a fold that does not exist. §5's migration row says "a caller passing
`subjects` itself is outside the resolver stage and unchanged", which is false as §4 is written.
Two consequences follow for §6: AC1 and AC2's stubbed `audit:subjects` return is consulted ONLY when
the args carry no `subjects`, so the two arms need a subjects-less fixture (the suite already has
one, `NOSUBJ` at `:742`), and the spec never says so.

Weighed for blocker and left at high: the unit still does what its §1 promises on the resolver
path, the harness suite sits on no `tools/gate-legs.json` leg and no `selftest-budgets.txt` row
(verified by grep, both files), so the breakage reds nothing at the close by itself, and the fix
is a placement sentence plus a fixture name.

**The fix.** State in S2 and §4 that the compare and the `tree` strip live INSIDE the resolver
branch, after `subjects = res.subjects` at `:657` — or guard the filter with `'tree' in s`. State in
§6's preamble that AC1 and AC2 use the `NOSUBJ` args so the stubbed resolver is the producer.
Re-word §5's migration row to the corrected placement.

**Left-shift.** The fifteen fixtures ARE the regression arm once the suite runs; the gap is that
nothing runs it. Spec 19 §3 already hands off a floor for this suite as "a backlog row the close
mints"; mint that row now with a `selftest-budgets.txt` line beside it so the close's runner
executes the harness suite, and until then AC4 should say the pass runs
`bash tools/workflows/unattended-build.test.sh` at the tip and reads its `PASS` line, since the
syntax check it names cannot see a throw.

### H2 — high — TOOL-16 §2 S1, S2, S3, §4 Inventory, §6 AC2 and AC4, §7 — raw 5, 17, 27

**The defect.** §4's code block replaces the string compare at `unattended.sh:2500` with four
`fail 34` sentences: the marker carries no commit sha; the sha is one this clone does not hold; the
commit does not contain the witness; the advertised default branch does not reach the commit. S3
and AC2 arm two — forty zeros reads "does not hold", the parent commit reads "does not contain the
witness". AC4 pins only `dUnstalledConvoy-38` and `is-ancestor "$wit"`. §7 says "the two new
`fail 34` sentences" and lists `harness arms (fail branches armed or pinned)` among the unit's
gates. Verified against the leg: `check-arms.py --report` discovers
`tools/unattended/unattended.sh -> unattended.test.sh` (it defines `fail() {` at `:390`) and lists
check 34 branches 1 to 4 at `:1242`, `:2481`, `:2493`, `:2500`, all ARMED; `cmd_check`
(`check-arms.py:241-260`) reds any branch that is neither armed by a positive assertion in the
sibling test nor pinned in `memory/project/unarmed-branches.txt`, which is shrink-only and holds no
check-34 row. As specced, the close's bar reds on the "carries no commit sha" and "does not reach"
branches. Two further inaccuracies in the same spec: §4 Inventory and §10 say "the two existing
sentences" — the marker block holds three (`:2481`, `:2493`, `:2500`) and check 34 a fourth at
`:1242`; and S1 claims the third read, `is-ancestor "$msha" "$ASHA"`, is observed by AC1 to AC3,
while no criterion drops it — a predicate omitting that read accepts a marker for a merge that was
never pushed and passes AC1 to AC4.

Weighed for blocker and left at high: the predicate itself is right and the accepting arms are
specified RED-first; what is missing is two arms and a count, and both are armable in the
fixture the spec already uses.

**The fix.** §7 reads "four new sentences, one existing removed". Add two arms to S3 and two
criteria beside AC2: a marker line with no 40-hex token (`landed main at nothing by push-main`)
reads `carries no commit sha`; a marker naming one extra local commit on the run branch that
contains HEAD but was never pushed to the fixture `origin` reads `the remote default branch does not
reach`. Extend AC4 to `grep -c 'is-ancestor "\$msha"'` printing 1 so the third read has an
observation. Correct Inventory and §10 to three marker sentences. If either branch is deliberately
left unarmed, the spec says so and names the `unarmed-branches.txt` row with its reason.

**Left-shift.** The `harness arms` leg is the gate and it already works; the audit-side check is
mechanical: for every `fail <n> "` line a spec's §4 code block adds, §6 or §7 names one arm whose
`hit` text is a slice of that sentence. A grep over the spec for `fail [0-9]+ "` against a grep for
the same sentences' distinctive words in §6 is a documented check a lens can run in seconds.

### H3 — high — TOOL-17 §4 'The two helpers', §5 error/empty states — raw 28

**The defect.** Ran it in this shell: `_o=""; printf '%s\n' "$_o" | wc -l | tr -d ' '` prints
`1`. The `check_status_one_line` helper as written therefore reads a verb that wrote NOTHING to
stdout as exactly one line, and `same "--status $1 is one stdout line" … "1"` passes. §5's "a verb
that prints nothing reads `0` lines under `check_status_one_line`, which reds as loudly as `2`" is
false as the helper is designed. The empty case is not a corner: it is the green-by-absence class
this unit exists to close (H3 of round 2 was "an arm only ever seen passing"), and with M5 below it
is the reading the AC2 break actually produces when followed literally. `printf '%s' "$_o" | grep -c ''`
prints `0` on empty and `1` on one line, verified beside it.

**The fix.** Count with `printf '%s' "$_o" | grep -c ''` or assert `[ -n "$_o" ]` before the count;
fold §5's empty-state sentence to what the helper then reads; add to AC2 a third reading — against
a driver copy whose status `printf` is deleted, the `same` reds with `0`.

**Left-shift.** The arm as fixed is the gate. For the class: any suite helper that counts lines of
a captured variable takes `grep -c ''` over `wc -l`, because `wc -l` counts newlines and
`printf '%s\n'` always adds one. That is a one-line entry for the kit's own bug-class list, and
the lens that reads §4 code blocks can grep for `printf '%s\n' "$` followed by `wc -l` on the same
line.

### H4 — high — TOOL-18 §3 Edges against §2 S3 and §6 AC2, and TOOL-13 §6 AC2, §7 — raw 18

**The defect.** Spec 18 defines its second arm's staged break twice and differently. §3 Edges:
the consumed block is "`CONF=`, the refusal, the source, the two calls", "whose whole removal is
the staged break this unit's second arm reads" — the calls go. S3 and AC2: "unit 13's whole
four-line conf block removed … made by the arm with `sed` over the four lines" — the calls stay.
Only the second reading can produce AC2's observation: with the two `read_bound_key` calls gone the
function is never entered, the guard never fires, and "exits 2 with the same sentence" cannot
print; the copy walks on whatever defaults the tick's own code carries. Spec 13 §6 defines the
BLOCK copy as "the whole conf block of §4", and spec 13 §4's block (its lines 95 to 101) is seven
lines including both calls, while its Files-touched row says "five lines" and its S3 says "WHOLE
four-line block". The sibling agreement spec 18 AC4 requires therefore lands on the reading that
cannot be observed. This is a defect in exactly one document under BUILD-METHOD's interface axis
and is unresolved as written.

**The fix.** State the removed lines once and identically in spec 18 Edges, S3 and AC2's fixture
line: `CONF=…`, the `[ -f "$CONF" ]` refusal, the clearing assignments, `. "$CONF"` (the
`shellcheck` comment goes with them, uncounted), with the two `read_bound_key` calls explicitly
KEPT. Fold spec 13 §6's BLOCK definition and its S3 and Files-touched counts to the same four lines.

**Left-shift.** The arm is the gate once its break is one thing. For the audit: a staged break that
a spec names in two sections is a grep for the break's noun (`block`, `copy`) across the spec, with
the line counts beside each hit compared — a documented check, run by the lens that reads §3
against §6.

### M1 — medium — TOOL-15 §6 AC4 second clause, against §7 — raw 1, 22, 36

**The defect.** AC4 has `python3 tools/memory-tree/check-arms.py --report` "filtered to the harness
suite's own file" list the two new arms' `has` sites as armed. Re-read `check-arms.py:125-142`:
`discover()` takes tracked paths ending `.sh`, skips every `*.test.sh`, and keeps a file only if it
defines `fail() {` and has `fail <n> "` call sites; `cmd_report` (`:300`) takes no filter and prints
only discovered pairs. `unattended-build.js` is JavaScript and `unattended-build.test.sh` is
excluded by name, so the filtered listing is empty at tip and base alike — ran `--report` and
grepped for `workflows` and `unattended-build`: 0 rows. The clause is satisfied by an empty listing
(green-by-absence) or read as red with no remedy. §7 correctly omits the `harness arms` leg from this
unit's gates, contradicting AC4's use of that leg's tool.

Lowered from the skeptic's high on raw 1 to medium: S4's two arms are specified RED-first against
the rendered harness at base and AC1/AC2 read the throw text and the traced `subjects` directly, so
the arms can be seen failing; the vacuous clause is a meta-assertion about them, the same shape as
round 2's M1, not an arm that can only pass.

**The fix.** Drop the check-arms clause. Observe the arms through their own needles:
`grep -c 'Commit the fold' tools/workflows/unattended-build.test.sh` ≥ 1 and
`grep -c '"tree"' tools/workflows/unattended-build.test.sh` ≥ 1, each 0 at base; and say the pass
runs the suite once at the tip (see H1's left-shift).

**Left-shift.** A criterion that names a tool names a file in that tool's population; the audit
lens checks the population predicate (here `discover()`'s docstring at `check-arms.py:14-17`) before
accepting the clause. Documented check.

### M2 — medium — TOOL-15 §2 S1, §5 error states — raw 2

**The defect.** S1 says `SUBJECTS_SCHEMA` requires `tree` and §5 says an omitted `tree` "fails
schema validation, which is the existing refusal shape". AC1 stubs a return that already carries
both fields; AC3 greps `hash-object`; nothing reads `required`. Worse for observability: the suite's
`run_wf` agent stub (`unattended-build.test.sh:46-54`) returns `returns[label]` verbatim and never
consults `opts.schema`, so no `run_wf` arm can see a schema refusal at all, and the existing
`badSubject` check validates only `blob` script-side. A pass that adds `tree` to the compare and not
to `required` passes every AC; an agent that omits `tree` is then refused as "dirty" with
`tree undefined` in the message, the wrong refusal with a misleading remedy.

**The fix.** Add an AC: a stubbed return holding `path` and `blob` only makes `run_wf` print
`THROW` with a text that names the missing field and NOT `Commit the fold`. Because the stub cannot
validate, that means the script-side `badSubject` predicate widens to require `tree` (a 7-40 hex
string) on the resolver path, and the spec says so in S1.

**Left-shift.** The AC as fixed is the arm. For the class: a spec that says "the schema refuses X"
in a harness whose test stub does not evaluate schemas has named an observation no arm can make;
the lens greps the suite's stub for `schema` before accepting the sentence.

### M3 — medium — TOOL-15 §2 S5, §6 AC3 — raw 3

**The defect.** S5 requires the resolver-stage header to state the pre-flight AND what it does not
prove (a fold written by a concurrent session after the check passes), "Observed by AC3". AC3's
only observation is `grep -c 'hash-object'` ≥ 2 per file. The prompt sentence §4 dictates supplies
one hit; the §4 schema-line comment `// tree = git hash-object <path>` landing in the template, or a
header that states the pre-flight without its limit, supplies the second. Nothing in §6 names any
string from the limit sentence, so AC3's "Red when: the header does not state the pre-flight and
its limit" has no observation behind its second half.

**The fix.** Add to AC3 a grep for a phrase the limit sentence must carry (`concurrent` or
`after the check passes`) over both template and render, ≥ 1 at tip and 0 at base.

**Left-shift.** Round 2's M1 rule, restated for this build's own checklist: a `grep -c` criterion
whose threshold equals the number of code carriers cannot see the prose carrier; every prose
requirement in §2 gets a needle only that prose can carry.

### M4 — medium — TOOL-16 §2 S4, §6 AC4 — raw 6

**The defect.** S4 requires the comment above check 34 to state the predicate, cite
`TOOL-dUnstalledConvoy-38`, and state what the predicate does NOT prove — the lander's identity and
the `TOOL-aUnblockedFleet-7` concurrent-landing tolerance §4 argues at length — "Observed by AC4".
AC4 greps `dUnstalledConvoy-38` and the `is-ancestor "$wit"` code line. The `-7` citation is a
greppable string the AC omits (0 hits in `unattended.sh` today, verified), and the limit statement
has no observation at all; a comment reading only "closes -38" passes.

**The fix.** Extend AC4: `grep -c 'aUnblockedFleet-7' tools/unattended/unattended.sh` ≥ 1 at tip
and 0 at base, and a grep for a phrase of the does-not-prove sentence (`does not prove`) ≥ 1.

**Left-shift.** As M3.

### M5 — medium — TOOL-17 §4 'The staged breaks, one per arm', §6 AC2 — raw 29

**The defect.** Re-read `unattended.sh:72-75`: `KIT_DIR` is derived from `$0` and the driver exits
2 to stderr ("the kit library is missing beside this script") when `lib-unattended.sh` is not
beside it. §4 stages AC2's break "by copying the driver to a scratch path and pointing `SCRIPT` at
the copy … which is how the suite's other driver-copy arms already work" — but the suite has two
shapes: the stripped-copy arm at `unattended.test.sh:2092-2095` copies the lib beside the copy and
its comment says why, and the L2 arm at `:5022` copies the driver WITHOUT the lib on purpose to
observe that refusal. Followed literally, the AC2 break refuses on stderr, which the helper drops,
writes nothing to stdout, and reads `1` under the §4 helper (H3) — the arm passes on its own break
and the RED-first observation is green. With H3 fixed it reads `0`, which is red for the wrong
reason.

**The fix.** State that the copy is made with `lib-unattended.sh` beside it (or the driver is
copied in place under a scratch kit dir), so the copy reaches its status `printf` and the second
line is what is counted.

**Left-shift.** The arm as fixed is the gate. For the class: "as the other arms already do" is a
citation the lens resolves to a line, and when two arms do it two ways the spec names which.

### M6 — medium — TOOL-17 §3 Non-goals and Edges, against TOOL-7 §6 AC5 and §7 — raw 23, 41

**The defect.** Spec 7 (rev-3, order 16, one order before this unit) AC5 is a NEW suite arm — its
§7 New-arm line lists "the one-line `--status` assertion of AC5" — asserting `run --status tRun |
wc -l` prints 1 over three fixtures, where `run()` at `unattended.test.sh:359` is
`bash "$SCRIPT" "$@" 2>&1`. That is the whole-output-count-over-merged-stderr shape spec 17 §4
'Why the one-line assertion drops stderr' rejects as "a test of the fixture's conf and not of the
verb", and spec 17 AC4 stages exactly that break (`GATE_BOUND` deleted so a NOTE prints). Spec 7's
arm passes today only because `mkconf` (`:112-119`) declares `GATE_BOUND` and `UNIT_STALL_BOUND`.
Spec 17 §3 says "the two whole-line readers are S3's" (true at base, false at order 17) and hands
off only to unit 9; spec 7 rev-3 cites unit 16 and never 17. The class this unit exists to close is
re-created one order earlier and left unrouted.

**The fix.** Add a `hands-off TOOL-aWokenSentinel-7` to spec 17 §3: AC5's one-line assertion
routes through `check_status_one_line` at this unit's tip (as spec 9's does), with spec 7 AC5 folded
to cite it; or re-derive the order so unit 17 lands before unit 7. Either way the "two readers"
count becomes a derivation over the file at the unit's order rather than a number.

**Left-shift.** A hygiene-shaped check the build can run over its own spec set: every criterion
that pipes `run --status` into `wc -l` names the helper, once the helper exists — one grep over
`spec/*.md` for `run --status[^|]*| *wc -l`.

### M7 — medium — TOOL-18 §1, §2 S4, against TOOL-13 §6 AC2 and §7, and the build order — raw 19

**The defect.** Build order: unit 13 at 13, unit 18 at 14. Spec 13 rev-2 AC2 and §7 record the
BLOCK copy's red reading as "exits 2 with `read_bound_key was called with CONF unset` on stderr,
zero `declares no` lines, and no launcher written — unit 18's guard". At order 13 that guard does
not exist. The BLOCK copy (calls kept, per H4's fixed reading) runs the unguarded function with
`CONF` unset: two NOTEs print with an empty path, exit 0, attempt 1 launches — which is exactly what
spec 18 AC2 records as its own BASE reading. So spec 13's pass cannot observe the reading its AC
states; it either records what it did not see or edits the sibling mid-pass. The arm is red either
way (the empty path fails `test -f`), so spec 18 §1's "spec 13's arm gains a break it reds against"
and spec 13 §3's matching claim are also wrong: the arm had a break before the guard, and spec 18's
own Alternatives-rejected concedes the BLOCK copy alone "makes one arm honest".

**The fix.** S4 states the reading at spec 13's order (two `Declare one in ` lines with an empty
path, refused by `test -f`) and that unit 18 re-reads the same copy as exit 2 with zero NOTEs;
fold spec 13 AC2 and §7 to that split. The alternative — re-derive the order so unit 18 lands
before 13 — depends on whether unit 5's pass built the tick's conf block (spec 13 Files-touched
makes that conditional), so the split reading is the safer fold.

**Left-shift.** A criterion's red reading names the order it is observed at when that reading
depends on a sibling at a later order; the audit lens greps each spec's `§6` for another unit's id
and compares orders. Documented check.

### M8 — medium — TOOL-18 §6 preamble, AC1, AC2, AC3, §7 — raw 10, 32

**The defect.** Verified: `git show 12513c25:tools/unattended/lib-unattended.sh | grep -c
read_bound_key` prints 0; at that sha the function sits in `unattended.sh:358` and no
`resume-tick.sh` exists (`git ls-tree` returns nothing). Unit 5 (order 11) hoists it. Spec 18 ties
"this unit's base" to `12513c25` itself (AC3's figure line; the status header) and names "the lib at
this unit's base" as the one staged break for both arms. Against that lib a bare shell calling
`read_bound_key` gets `command not found`, exit 127, never "exit 0 with `Declare one in  to change
it`"; AC2's "walks, prints two NOTEs" is equally unreachable; AC3's "0 at base" is vacuous. The red
readings AC1/AC2 describe exist only against the post-unit-5 lib minus the guard, which the spec
never names. Sibling spec 19 shows this build's authors know base and pre-pass tip differ ("72 at
base … expected to have moved with units 3 and 5"); spec 18 does not account for it.

**The fix.** Name the break as the lib at the tip of the preceding order (after units 5 and 13
landed) with the guard absent, or as the function extracted by
`sed -n '/^read_bound_key() {/,/^}$/p'` from `unattended.sh` at `12513c25` and sourced into the
bare shell; state that base's expected reading as the empty-path NOTE; make AC3's base figure a grep
over that same lib, which must already hold `read_bound_key`.

**Left-shift.** A base-side figure in an AC names the sha it was read at, and when the file is
written by a predecessor unit the sha is that unit's tip and the spec says so. The audit lens runs
`git show <base>:<path> | grep -c <needle>` for every "0 at base" and reds the spec when the file
does not exist there or the function the AC calls is absent. This is the same check M15 asks for.

### M9 — medium — TOOL-18 §6 AC4, against TOOL-13 — raw 20, 33

**The defect.** Ran `grep -c 'whole four-line'` over spec 13 at HEAD: prints 0. Spec 13 line 47
spells "the WHOLE four-line block removed" and grep is case-sensitive. Spec 13 §6/§7 name four
staged copies (SOURCE, BLOCK, WORKTREE, CLEAR), not "two breaks". AC4 is therefore red against a
fold this spec's §1 and §9 say already landed with its disposal (`830c46e8` confirms the rev-2), so
the first observation reds on a needle rather than a mechanism, and the pass either edits spec 13's
prose to satisfy a grep or misreports the criterion.

**The fix.** `grep -ci 'four-line'` (or the needle `four-line block`), and restate the second clause
as "spec 13 §7 names a break per arm, the whole-block copy among them" — with H4's four-line
definition as the phrase both specs carry.

**Left-shift.** Every `grep -c` in an AC whose file exists at the tip and whose spec says the fold
already landed is RUN at authoring time; a zero on a `≥ 1` criterion is a finding before the spec
is committed. That is one loop over backticked `grep` commands in `spec/*.md`, and it would have
caught M9, M14 and the `-7` half of M4 in seconds.

### M10 — medium — TOOL-18 §2 S1, §5, §6 AC1 — raw 9

**The defect.** The guard is two tests, `[ -n "${CONF:-}" ] && [ -f "$CONF" ]`; §1 says the refusal
fires when no `CONF` names an EXISTING file, and §5 lists unset, empty and missing-file as three
refusing states. AC1 runs with `CONF` unset, AC2's block removal is also unset, AC3 runs with a set,
existing conf so the guard never fires and its grep pins only the sentence. No criterion sets `CONF`
to a nonexistent path, so a guard reduced to `[ -n "${CONF:-}" ]` passes every AC and still emits a
NOTE naming a file that does not exist — the second half of the contract the spec's own goal names.

**The fix.** Add to AC1: with `CONF=/nonexistent/path` exported into the bare shell the same call
exits 2 with the sentence; at the (corrected, M8) base it exits 0 and the NOTE names the nonexistent
path.

**Left-shift.** The arm as fixed is the gate. For the audit: a guard with N conjuncts gets N failing
observations, one per conjunct; the lens counts `&&` in the §4 guard against arms in §6.

### M11 — medium — TOOL-19 §3, §4 'Why a static count', §5 risks, §10, against `TOOL-dUnstalledConvoy-19` — raw 42

**The defect.** `TOOL-dUnstalledConvoy-19` is OPEN and rules on this exact remedy shape in this
kit: appending arms after a suite's terminal `exit "$st"` strands them, hit twice in one session for
about fifty arms, "while the suite printed PASS and `check-arms.py` text-matched every one"; the
`FLOOR_ASSERTIONS` slack of sixty "hides fifty stranded arms exactly"; raising it "fixes the
instance and not the class"; "the class wants a STRUCTURAL arm — no executable line may follow the
suite's terminal `exit` — which is one grep and cannot go slack the way a numeric floor does". Spec
19's goal is that the adopter suite's green "must mean its arms RAN"; its design is a floor at 90 %
of a static count (64 against 72 sites — grep verified 72 at HEAD), eight assertions of slack,
inserted directly above `exit "$st"` at `adopt-unattended.test.sh:427`, the append-after-exit shape
`-19` was hit by. No structural arm exists anywhere in the kit (grepped). §10 lists `-19` as a
recall hit; §4 never engages its ruling; §5's risks row says "the discount makes it unlikely" — the
discount IS the slack `-19` recorded as the defect.

**The fix.** §2 adds the one-grep structural arm beside the floor — nothing executable after the
suite's terminal `exit`, e.g. `sed -n '/^exit "\$st"$/,$p' <suite> | grep -cvE '^\s*(#|$)'` prints
exactly 1 — with its own failing observation (a line appended after the exit reds it); or §3 states
the exemption with `-19` cited and hands the arm off as a named row. The floor stays; it catches a
different loss (an arm made unreachable by a seed change), which is the one §1 names.

**Left-shift.** The structural arm IS the gate, and it belongs in every `*.test.sh` in the kit
that ends `exit "$st"`, which is one loop in the kit gate rather than a per-suite line. A backlog
row for the kit-wide form, with `-19` cited, is the honest hand-off if this unit takes only its own
suite.

### M12 — medium — TOOL-19 §2 S3, §4 last paragraph, §7, and TOOL-14 §6 AC5 — raw 31

**The defect.** `run-unattended-gates.sh:263` delegates to
`tools/run-gates/run-selftests.sh --kit tools/unattended`. Re-read that runner: the sweep writes
each suite under `$SWEEP_ROOT`, a `mktemp -d` at `:492` removed by its EXIT trap at `:493`, and
prints only `ok <name> <s>s  cost withheld` on green (`:664`); the serial path captures into
`$out` and prints `ok <name> <s>s`. No per-suite log persists and `PASS (<n> assertions)` is never
surfaced. Spec 19 S3's "read from that run's per-suite log and never through `tail`", its §4 "the
close's first green prints `PASS (<n> assertions)` with the executed count, which is the
observation the comment defers to", and spec 14 AC5 (`:186`, the fold spec 19 says lands) all name
an artifact that does not exist. The pin is "confirmed" at the close only in the weak sense that the
floor did not red.

**The fix.** State that the close's run observes only that the floor held (a non-zero exit names
the suite). If the executed count is wanted on the record, have the close — not the pass — run
`bash tools/unattended/adopt-unattended.test.sh` once directly and record its `PASS` line, and fold
spec 14 AC5 to that observer.

**Left-shift.** `run-selftests.sh` persisting per-suite stdout under `<git-dir>/gate-logs/` as
`run-gates.sh` already does for legs is the kit-level fix, and a backlog row for it is the honest
hand-off; until then no spec names a per-suite log from that runner.

### M13 — medium — TOOL-20 §2 S4, §6 AC4 — raw 14

**The defect.** S4 names three folds — spec 11 rev-2, spec 5 rev-3, spec 2 rev-3 — "Observed by
AC4". AC4 greps spec 11 and spec 5 and says "both folds"; spec 2 is read by nothing. Verified: spec
2 at HEAD does carry the hand-off (`hands-off TOOL-aWokenSentinel-20`, its line 118) and the
code-line pin hand-off to unit 11 (line 115), and spec 5 rev-3 line 122 says the S4 root "is that
function's answer, never an inline" — so the folds landed and the defect is the criterion, not the
tree. The spec 5 read is `grep -c 'resolve_sidecar_dir'` ≥ 6: counts were 5 at `12513c25` and 8 at
HEAD, so the threshold separates the revs today, but any unrelated mention satisfies it and the
S4-specific hand-off (resume-log root through the lib, not an inline `rev-parse`) is not what it
reads. The three-versus-"both" disagreement is an internal spec error.

**The fix.** Add greps: over spec 2 for the hand-off (`aWokenSentinel-20` ≥ 1); over spec 5 for
`$(resolve_sidecar_dir)` in its S4 paragraph ≥ 1, or for `rev-parse --git-dir` printing 0 outside a
Non-goals or rejected-alternative line. Say "three folds".

**Left-shift.** As M3: a count threshold that unrelated mentions satisfy is a needle for the wrong
carrier; the audit lens asks of every `≥ N` grep whether the N-th hit can be the sentence the
scope item names.

### M14 — medium — TOOL-20 §6 AC4, against TOOL-11 — raw 21, 35

**The defect.** Ran `grep -c 'code lines'` over spec 11 at HEAD: prints 0. The landed rev-2
(`830c46e8`) spells the predicate `CODE lines` (its lines 25, 110, 229) and `code-line` elsewhere,
never lowercase `code lines`; `grep -ci 'code.line'` prints 11. AC4's own sentence says "both folds
land with the disposal that authored this spec", so the criterion is red on the state it declares
satisfied, and the remedy is an edit to a sibling's prose or to the needle — neither is the
two-spellings class the criterion claims to catch.

**The fix.** `grep -ci 'code.line'` (or the needle `CODE line`), threshold unchanged.

**Left-shift.** As M9: run every tip-side grep at authoring time.

### M15 — medium — TOOL-20 §6 AC1 — raw 34

**The defect.** AC1 says "at this unit's base the two print 0 and 1". Verified:
`git grep 'rev-parse --git-dir' 12513c25 -- tools/unattended/lib-unattended.sh
tools/unattended/unattended.sh` returns nothing (rc 1), and `resolve_sidecar_dir` has 0 hits in the
driver at that sha. Both files print 0 at `12513c25`; the driver's 1 exists only after unit 2
(order 2) lands, one order before this unit. Under the build's own vocabulary — specs 17, 18 and 19
spell "this unit's base" as `12513c25`, and the template defines `base` as the grounding sha — the
base half of AC1 reads 0 and 0, so the observation either fails or is silently re-based by the
builder.

**The fix.** State the base-side figure against the tip of unit 2's pass, the order-2 predecessor
that defines the function, not against the status header's `12513c25`.

**Left-shift.** As M8: one check covers both.

### L1 — low — TOOL-15 §4 prose below 'The refusal', against the quoted prompt sentence and S1's schema — raw 25

**The defect.** §4 quotes the prompt sentence verbatim ("run `git rev-parse HEAD:<specPath>` and
`git hash-object <specPath>` in `<repo>` and return both; an unspecced unit is omitted…") and then
asserts "the prompt asks for the full 40 hex characters of each". The quoted sentence carries no
such ask, and S1/§4 give both `blob` and `tree` the `^[0-9a-f]{7,40}$` pattern, so a schema-valid
return with one side abbreviated is refused as dirty with the remedy "Commit the fold", false for a
clean tree; §5 names that failure mode as accepted. Low because both git commands print 40 hex by
default.

**The fix.** Pin both fields at `^[0-9a-f]{40}$` and say so in S1, or put the 40-character ask into
the quoted sentence so §4's prose and its sentence agree.

**Left-shift.** A spec that quotes a prompt and then paraphrases it has two spellings; the lens
diffs the paraphrase's claims against the quote.

### L2 — low — TOOL-18 §2 S1 header comment, §6 AC3 and AC4 second clause — raw 11

**The defect.** S1 says the function's header states the contract and is "Observed by AC1, AC2 and
AC3"; AC3's `grep -c 'CONF unset or naming no file'` matches the refusal echo in §4's code block,
not the header line, and nothing else reads the header. AC4's second clause ("spec 13's §7 names
two breaks") has no command, and spec 13 names four (M9), so it is satisfiable by any wording,
including one that names the source-line-only copy for the NOTE arm, which is H4 of round 2
unchanged.

**The fix.** Add to AC3 a grep for the header phrase (`named it in CONF` or `sourced the conf into
THIS shell`) ≥ 1 over the lib; make AC4 grep spec 13 for a phrase per break, case-insensitively.

**Left-shift.** As M3.

### L3 — low — TOOL-19 §2 S2, §6 AC4 — raw 13

**The defect.** S2 requires the pin's comment to carry the authoring rule (static count, ten
percent, the close confirms) and names AC1 as its observer; AC1 observes only the pin's arithmetic,
and AC4's `grep -c 'FLOOR_ASSERTIONS'` ≥ 2 is the pin line plus the compare line with no comment at
all. A bare `FLOOR_ASSERTIONS=64` passes every AC, and the next session lowering it has no stated
procedure. Low because §4 gives the comment verbatim.

**The fix.** Extend AC4 with a grep for `static count` (or `headroom`) over the suite, ≥ 1 at tip
and 0 at base.

**Left-shift.** As M3.

### L4 — low — TOOL-19 §4, §6 AC1 figure note, §3 Edges — raw 24

**The defect.** §4 says "units 3 and 5 add arms to this suite before this unit's order" and AC1's
figure note repeats it. Spec 5's Files-touched (its lines 345-356) and its two New-arm lines name
`resume-tick.test.sh`, `unattended.test.sh` and one INFO line in `adopt-unattended.sh`; it never
touches `adopt-unattended.test.sh`. The arms added to the adopter suite before order 19 are unit
3's (order 6; its §7 line 517 already cites this unit's floor) and unit 4's (order 10; its §7 line
268 says "no floor exists in this suite"). §3 Edges consumes only unit 14. The pin is re-derived at
the pass, so no functional impact — a false citation and an unfixed sibling disagreement.

**The fix.** Name units 3 and 4 in §4 and AC1's figure note; fold spec 4 §7's "no floor exists" to
cite this unit's floor as spec 3 §7 does.

**Left-shift.** Check 12 already joins edges; the audit-side check is that every unit a spec's §4
names as a writer of a file appears in that unit's own Files-touched.

### L5 — low — TOOL-20 §2 S1, §6 AC2 — raw 15

**The defect.** S1 says the move is verbatim and that an empty `rev-parse` answer returns 1 under
the caller's dead-probe rule, "Observed by AC1 and AC2". AC1 is a literal count; AC2 runs the
function only inside a repo and a linked worktree, so the `[ -n "$_sd" ] || return 1` branch and the
`2>/dev/null` are never exercised, and no AC diffs the moved body against unit 2's. Spec 2's own
dead-probe arm (AC8) stages `stat`, not an empty git-dir answer, so nothing on the close's bar
catches a `return 1` dropped in transit; the caller would then compose a path from an empty root,
the liveness class charter §7 names. Low because the fix is one call and one diff.

**The fix.** Add to AC2: from a directory inside no repository the same bare-shell call prints
nothing and exits non-zero; and a `diff` of the function body extracted by
`sed -n '/^resolve_sidecar_dir()/,/^}/p'` from `unattended.sh` at unit 2's tip against the same
extraction from the lib at this unit's tip is empty.

**Left-shift.** "Moved verbatim" is a diff, and a spec that says it names the diff.

### L6 — low — TOOL-20 §2 S3, §6 AC3 — raw 16

**The defect.** S3 requires the lib's TOP header sentence (the one listing what the file holds) to
name the function; AC3's `grep -c 'resolve_sidecar_dir'` ≥ 2 counts the definition once and is
satisfied by any second mention — §4 places a rule comment directly above the definition and S1
gives the function "its own header", either of which supplies the second hit with the file header
(`lib-unattended.sh:1-19`, re-read) untouched. The "sends the next reader to the driver" Red-when
is not observable.

**The fix.** Scope the grep to the leading comment block:
`sed -n '1,19p' tools/unattended/lib-unattended.sh | grep -c 'resolve_sidecar_dir'` ≥ 1 at tip and
0 at base (the header's line count is derived at observation, not typed).

**Left-shift.** As M3.

## The cross-read on the four axes

Where two specs disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-15 §4's placement of the compare versus the callee contract its own S3
  states and the fifteen suite fixtures (H1). TOOL-16 §4's four sentences versus its §7's "two"
  and its Inventory's "two existing" (H2). TOOL-17 §4's helper versus its §5's empty-state claim
  (H3). TOOL-18 §3's five-item block versus its S3/AC2's four lines versus TOOL-13 §4's seven-line
  block, §6's "whole conf block", Files-touched "five lines" and S3's "four-line" (H4, M9).
- **Ordering.** Three "at this unit's base" readings that `12513c25` cannot produce because a
  lower-order sibling writes the file: TOOL-18 AC1/AC2/AC3 (unit 5 at order 11 hoists the function;
  M8), TOOL-20 AC1 (unit 2 at order 2 defines it; M15). TOOL-13 at order 13 records a red reading
  that exists only after TOOL-18 at order 14 (M7). TOOL-7 at order 16 installs the reader shape
  TOOL-17 at order 17 exists to retire (M6). TOOL-19 is the one spec in the set that says its base
  figure "is expected to have moved" — the correct spelling the others should copy.
- **Scope.** TOOL-19 names units 3 and 5 as arm writers for a suite spec 5 never touches, while
  spec 4 §7 disclaims the floor TOOL-19 creates (L4). TOOL-20 S4 names three folds and its AC4
  observes two (M13). TOOL-17 hands off to unit 9 and not to unit 7 (M6). TOOL-19 cites
  `TOOL-dUnstalledConvoy-19` and takes the remedy it rules against without saying why (M11).
- **Acceptance.** Criteria satisfied by an empty population: TOOL-15 AC4 (M1). Criteria red on
  the state they declare satisfied: TOOL-18 AC4 (M9), TOOL-20 AC4 (M14). Scope items whose claimed
  observer cannot see them: TOOL-15 S1, S5 (M2, M3); TOOL-16 S4 (M4); TOOL-18 S1 header, the `-f`
  half (L2, M10); TOOL-19 S2 comment (L3); TOOL-20 S1, S3 (L5, L6). A helper that cannot fail on
  the case its spec names (H3) and a break that produces a different reading than the one named
  (M5). An artifact named as the observer that no runner writes (M12).

**Prior art the specs re-invent or misread.** `TOOL-dUnstalledConvoy-19`, OPEN, on the exact
floor-with-headroom shape (M11). `check-arms.py`'s population predicate, read against a JavaScript
harness (M1) and against four new `fail` sentences (H2). The suite's two driver-copy idioms at
`unattended.test.sh:2092` and `:5022` (M5). `run-selftests.sh`'s scratch-and-trap log handling
(M12). The suite's existing `NOSUBJ` fixture at `unattended-build.test.sh:742`, which is what AC1
and AC2 of spec 15 need and do not name (H1).

**Harness and driver assumptions, and which were verified.** The `badSubject` placement at
`unattended-build.js:635-669` and the fifteen `"subjects"` fixtures were re-read (H1). The
check-34 branch table and `cmd_check`'s rule were re-read and `--report` was run (H2, M1). The
`wc -l` reading was run (H3). `unattended.sh:72-75` and the two copy arms were re-read (M5). Spec
7's AC5 and `run()` at `:359` were re-read (M6). Every `git show 12513c25:` and `git grep` figure
above was run (M8, M13, M14, M15). The `-19` row was read from `memory/backlog/TOOL.md` (M11).
`run-selftests.sh:492-493` and `:664` were re-read (M12). Spec 2's hands-off lines and spec 5's
line 122 were re-read (M13). The lib header's nineteen lines were re-read (L6). Not re-run here and
reported as the skeptic's: the `run_wf` stub's disregard of `opts.schema` (M2), spec 5's
Files-touched line range and spec 4's §7 line (L4), spec 2's AC8 shape (L5).

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture.** No arm was staged, no
  suite was run, no `--landed` was invoked. H3 is the one claim that was executed, and it is one
  shell line.
- **A spec audit grades what a document says.** Whether unit 5's pass builds the tick's conf block
  (which decides whether M7's reorder alternative is available) is a question for the build.
- **The units' §8 alternatives were read for what they resolve, not re-adjudicated.**
- **The 10 refuted findings were not re-opened.** The skeptic's verdicts stand; none was
  contradictory and none was spurious by the pipeline's own count.
- **Precision was 0.77.** Above the floor and reported. The two audit-side checks that would have
  removed six of the twenty-five defects before commissioning — run every tip-side `grep -c` at
  authoring time (M9, M14, the `-7` half of M4), and run every "0 at base" against `git show
  <base>:<path>` (M8, M15) — are one loop each over `spec/*.md` and belong in the commission's
  pre-flight beside the blob-pin check unit 15 builds. Round 2 over this set should re-audit the
  revised specs at their new blobs with one lens on H4/M7/M9 across specs 13 and 18 together, since
  three of the six defects on spec 18 are the same block spelled four ways across two documents.
