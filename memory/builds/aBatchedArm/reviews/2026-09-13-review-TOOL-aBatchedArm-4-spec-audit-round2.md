**Serves:** spec-audit TOOL-aBatchedArm-4

# Tier-2 spec audit — TOOL-aBatchedArm-4, ROUND 2

*The fold audit. Round 1 (BLOCKED, twelve defects) was folded into rev-2 of the unit that changes
`tools/run-gates/run-selftests.sh`, the runner that grades 61 kit self-test suites; a wrong change
there reds every kit's self-test at once. This round grades the FOLD — where it is wrong and where it
is incomplete — and does not re-report what round 1 already found. Node `a`, 2026-09-13, ROUND 2.
Every finding below survived a skeptic prompted to REFUTE it, and every cited line was re-read in the
tree by the author of this report rather than transcribed from a lens: the six carried-literal
occurrences were re-counted with the ban's own regex, the sweep TSV rows were re-read, and the four
DoD carriers were opened. Each row carries its address inside the spec, the fix, and the gate that
would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md`@`a2b804b4964a8b22406f735f06a3618770f94bc0` — rev-2, the fold of round 1's twelve defects. ROUND 2.

The sibling specs are NOT in scope and are not re-graded. `TOOL-aBatchedArm-3` rev-2 and the build
README are cited in exactly one row (E-8) because THIS unit's roster position collides with theirs,
which is a fact about the build's records rather than about either sibling's design.
`TOOL-aBatchedArm-5` has no spec yet; where a row names it, it is because this unit hands it a
consequence it does not declare.

## Verdict: BLOCKED

Three rows at BLOCKER, nine at HIGH, seven at MEDIUM, one at LOW. Those twenty rows collapse to
**ten distinct defects**; the table below names which rows share one, so a fold that repairs a defect
repairs every row under it.

One defect is enough on its own, and it is the fold's answer to round 1's B6. Round 1 blocked rev-1
for wiring the only consumer to `--serial`, so that nothing in the tree issued `--pooled`. Rev-2
corrects that by making `run-unattended-gates.sh --selftests` — the invocation four tracked files
record as the Definition of Done for every `tools/unattended/` change — issue `--pooled` under the
inherited `budget × 2` bound. The tree's only measurement at exactly that bound is the full-sweep
record this spec's own §3 cites, and its slots 51-57 show FIVE of the seven rows that invocation
pools killed `rc=124` at bounds byte-equal to today's budgets times two, one green, and the gate
self-test never finishing. The spec orders this unit first and hands the bound to an unspecced unit
5, so from this landing until unit 5's the recorded DoD renders TIMEOUT on the tree's own evidence
with every acceptance criterion green (E-1). That is round 1's could-not-fail shape in the other
direction, and it lands risky behaviour as the DEFAULT against charter §1's land-dark rule. The fix
is one sequencing decision, stated in E-1.

The rest of the fold is right about the three things round 1 said mattered most — the factor is
gone, the edges point the right way, five arms not four — and wrong or incomplete on five mechanical
items it claimed to close: the DoD's four carriers are untouched while their verdict changes (E-2);
AC7's predicate cannot see four of the five lines S5 exists to rewrite (E-3); S6's raise rests on a
literal that already exists, so the described edit reds the install-prefix leg SLACK (E-4); §7's gate
list is wrong in both directions and round-1 D-10 was never folded although the log says the round
was (E-5); and §5 migration still carries rev-1's wiring sentence (E-6). Three further rows are new
to this rev: AC4 has no mechanism and no cost line (E-7), the build's roster and derived order
contradict the 4 → 3 → 5 → 1 → 2 chain this spec depends on (E-8), the manifest left-shift round-1 M5
named was dropped (E-9), and one design paragraph misattributes a host property (E-10).

Under `memory/guides/BUILD-METHOD.md` the loop re-arms on a STRICTLY SMALLER confirmed-blocker
count: round 1 stood at eight blocker rows, this round at three, so the fold converged and a round 3
is owed after the next fold. Disposition of the standing blocker: FOLD — the defect is in the
document this review read, and the mechanism it needs (a `--selftests --pooled` spelling beside a
`--serial` default, or a `consumes-from` edge) exists in this unit's own scope.

## Review shape

- raw 35 · confirmed 20 · refuted 15 · unverified 0 · precision 0.57

Precision at 0.57 is above the ~0.5 floor `AGENTS.md` §8 sets for adding agents, so the lens fan was
scoped about right for this target. Read the confirmed count with the table below in hand: the
pipeline reports zero duplicates because each row addresses a different section of the spec, but
four lenses hit the DoD-flip seam independently (three rows) and four hit the S6 seam (four rows).
Twenty rows is ten defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty. The count of round-1 defects NOT re-found here (D-1, D-2, D-4, D-5, D-11, D-12) is
likewise a measured zero: those seams were read and nothing stood. D-3, D-7, D-8, D-9 and D-10 each
stand again in some form, and the table names which.

## The ten defects, and which rows carry each

| Defect | Descends from | Rows | Severity |
|---|---|---|---|
| E-1 · S3 flips the recorded DoD to `--pooled` at the inherited bound that killed five of the seven rows it pools; §5 perf denies it; risky default not landed dark | round-1 B6 (D-3), over-corrected | id=8, id=22, id=31 | blocker |
| E-2 · the DoD's verdict changes in four tracked carriers the spec neither names nor touches; nothing owes the serial cost pass | round-1 B6 (D-3), incomplete | id=2, id=25 | high |
| E-3 · AC7's grep cannot see four of the five lines S5 exists for; the M4 arm is missing from §7 | round-1 D-8 (M4), could-not-fail fold | id=1, id=10, id=23 | high |
| E-4 · S6/AC8 rest on a false premise: the usage line is ALREADY counted, so the described edit reds SLACK, which AC8 does not name | round-1 D-7 (M3/H7), false premise | id=4, id=9, id=26, id=35 | high |
| E-5 · §7 Gates wrong in both directions; round-1 D-10 not folded though the log says folded | round-1 D-10 (L1/L2), unfolded | id=12 | medium |
| E-6 · §5 migration still wires the one bare caller to `--serial` — rev-1's sentence contradicting S3 | round-1 B6 (D-3), leftover sentence | id=13, id=24 | medium |
| E-7 · AC4 has no mechanism for the withheld count to cross the process boundary, admits any integer, and carries no `cost:`/`fixture:` | new in rev-2 (S3's rewrite) | id=6, id=15 | medium |
| E-8 · the README roster and derived build-order contradict the 4 → 3 → 5 → 1 → 2 chain | new in rev-2 (spec-3 moved, roster did not) | id=18 | medium |
| E-9 · the manifest left-shift M5 named (watch `run-selftests.sh`) was dropped; the S5 commit owes a re-stamp it does not list | round-1 D-9 (M5), half-folded | id=33 | medium |
| E-10 · the cost-model paragraph misattributes the scanner and dropped its cite | new in rev-2 (§4 rewrite) | id=21 | low |

---

# BLOCKERS

## B1 · id=8, id=22, id=31 — the DoD lands on the pooled bound the record shows killing the rows it pools

**Address:** section 2 S3 · section 4 "Why the kit runner's verdict path is pooled" · section 5
perf, risks · section 6 AC4 · Edges (`consumes-from none`).

Verified at source, every step. `run-unattended-gates.sh:121` defaults `ONLY` to `--selftests`, and
`:263` is `bash "$ROOT/tools/run-gates/run-selftests.sh" --kit tools/unattended || st=1` — the bare
call S3 makes `--pooled`. That invocation is the compensating check recorded as the Definition of
Done at four carriers: `.githooks/gate-env.sh:27`, `tools/unattended/kit.toml:125-126`,
`run-unattended-gates.sh:26-27` and `:203`, and `AGENTS.md:519`. `--list` resolves seven rows for
that filter (`selftest-budgets.txt:110-116`), serial readings summing 12657 s, budgets 19430 s.
Under `--sweep` the outer width is `OUTER=$W` (`:298`), 8 on this node, so all seven start together;
each is bounded at `budget * SWEEP_FACTOR` (`:562`) with `sweep-ceiling-factor: 2`
(`selftest-budgets.txt:49`); the run wall is floored at the largest product, 27200 s.

The tree's one measurement at exactly that bound is the record §3 itself cites to reject the factor:
`memory/builds/aPooledSweep/build/2026-09-08-build-TOOL-aPooledSweep-1-full-sweep-rows.tsv`, slots
51-57, the sweep's last wave where those seven rows ran together:

| slot | rc | took | bound | row |
|---|---|---|---|---|
| 51 | 124 | 122 | 120 | unattended adopter e2e |
| 52 | 0 | 556 | 1200 | unattended brief-recorded selftest |
| 53 | 124 | 1022 | 1020 | unattended cross-component |
| 54 | 124 | 7722 | 7720 | unattended driver selftest |
| 55 | - | - | 27200 | unattended gate selftest |
| 56 | 124 | 341 | 340 | unattended pass-order selftest |
| 57 | 124 | 1261 | 1260 | unattended playbook selftest |

The bounds are byte-equal to today's budgets times two (60→120, 510→1020, 3860→7720, 170→340,
630→1260). Five kills at roughly 3x their serial reading, one green, the longest never finished. The
record notes a concurrent serial `--kit tools/unattended` run confounded that window and cannot
attribute — so this is the only evidence, not a clean prediction — but the spec cites the same
record for its §3 rejection and cannot lean on it for one claim and set it aside for the other.

What the spec says against that: §5 perf, "on its own it changes no suite's wall clock" — true per
suite and false for the invocation, whose wall becomes `max(38860/8, 27200) = 27200 s` against a
12657 s serial sum, during which any tracked-tree change renders the run UNSOUND (`:731-736`); §5
risks, "a quarter of its population", never joining the record's rows to the seven S3 pools; and
AC4, whose red condition is mode and count only, so AC4 is green with five TIMEOUT rows. The
runner's own pooled-RED remedy at `:751-758` (from `TOOL-dSpentCeiling-8`) then sends the operator to
the serial re-run anyway, and the population is already RED at BASE per `TOOL-aQuenchedHarness-9`, so
while that stands the pooled DoD is prefix cost with a 27200 s wall and no diagnosis: a killed suite
renders no FAIL lines (`TOOL-aReapedSpinner-22`), so a kit edit that guts a check and a busy box
render identically. `consumes-from none` is true of the code and false of the DoD the default is
wired into; unit 5 is unspecced and unordered.

Round 1 B6 offered the serial-DoD alternative. The fold took the other without pricing it, and the
result is B6's shape one level up: criteria green, the invocation the charter says "not done until
this prints GREEN" broken by TIMEOUT.

**Fix.** One sequencing decision, two honest forms:

- (a) Land the pooled path DARK. `--selftests --pooled` and `--selftests --serial` both land now as
  declared spellings — a program then issues `--pooled`, which is all round-1 D-3 required — and the
  bare `--selftests` default stays `--serial` until `TOOL-aBatchedArm-5`'s bound exists; that unit
  flips the default as the last step of its scope after an observed non-killing run, and this spec
  lists the flip as `hands-off` unit 5. Or, equally honest and this spec's own §4 rule applied to the
  kit runner: bare `--selftests` REFUSES naming both.
- (b) Keep the flip here and price it: add `consumes-from TOOL-aBatchedArm-5` to the default flip,
  say so in Rollout, state the assumption in §4 and cite the TSV slots against it.

In both: delete §5 perf's "changes no suite's wall clock" and replace it with the pooled DoD's cost
today from the sweep rows; §5 risks names "five of the seven rows S3 pools were killed at this exact
bound on 2026-09-08" with the slots; AC4 gains a red condition an operator can observe — "a pooled
run of the seven rows renders TIMEOUT for any row that passes serially"; and the four carriers name
the mode the pasted verdict must come from (see H1).

**Left-shift gate.** A spec-audit DoR check with a predicate: any S item that changes the argv of a
command named in a `DoD`/`compensating check` sentence anywhere in the tree (grep the carriers for
the command's basename) must list every carrier in Files touched and cite the last recorded run of
the new argv, or declare `land dark`. The mechanical half — "a DoD command's argv moved and its
carriers did not" — is a one-line grep over `gate-env.sh`, `kit.toml`, the kit runner and
`AGENTS.md` that check 12's witness arm could carry.

---

# HIGH

## H1 · id=2, id=25 — the DoD's verdict changes in four tracked files the spec never touches

**Address:** section 2 S3 · section 2 S5 (absence) · section 4 Files touched · section 5 migration
· section 6 AC4.

Today `run-unattended-gates.sh --selftests` GREEN is the cost-bearing verdict: `run_one`'s OVER
BUDGET reaches `unattended gates RED — … over budget` at `:277`. S3 makes that same command pooled
and withholding, so what the four DoD sentences certify changes — `.githooks/gate-env.sh:25-27`,
`tools/unattended/kit.toml:123-126`, `run-unattended-gates.sh:26-27`, `AGENTS.md:519` — and three of
the four are absent from Files touched. Nothing in shipped text then owes the `--selftests --serial`
pass: §4 hands the cost pass to "the periodic serial sweep `TOOL-aQuenchedHarness-9` already calls
owed", but that row (`memory/backlog/TOOL.md:423`) owes a periodic sweep as a red-suite SIGNAL, not a
serial cost pass, and it is OPEN, not a DoD. §5 migration's "no other invocation exists in the tree"
is false against four documented ones. The runner's own line 2 says it exists for "a cost verdict for
each"; the spec retires that from the DoD without touching the DoD.

Distinct from B1, and it stays live under B1's fix (b) and returns under fix (a) the day unit 5
flips the default: a kit edit that doubles a suite's cost satisfies the recorded DoD, because the
recorded command no longer grades cost and no carrier says the serial pass is owed alongside it.

**Fix.** S3 decides what the DoD names — pooled GREEN plus `--selftests --serial` GREEN both pasted,
or the serial pass alone for kit work — and S5 names the four sentences by file and line. Add the
four carriers to Files touched. Add a criterion: `grep -n 'run-unattended-gates.sh'
.githooks/gate-env.sh tools/unattended/kit.toml tools/unattended/run-unattended-gates.sh AGENTS.md`
shows each DoD line naming the declared mode and the verdict it carries; red when any carrier still
presents the pooled GREEN as the cost check. Rewrite §5 migration (see M2).

**Left-shift gate.** The same grep, on the bar: `tools/check-playbook-parity.sh` already
machine-compares five values against the sources that own them; a sixth pair — the kit runner's
`--help` mode list against the mode each DoD sentence names — reds a carrier that describes an
invocation the runner no longer has.

## H2 · id=1, id=10, id=23 — AC7 cannot see four of the five lines S5 exists to rewrite

**Address:** section 2 S5 · section 6 AC7 · section 7 New arm.

Ran AC7's predicate. `grep -n 'run-selftests.sh' memory/guides/SESSION-KICKOFF.md
tools/run-gates/run-selftests.sh` hits exactly `:2` (the header comment), `:77` (the usage line),
`:566` (a comment) and `SESSION-KICKOFF.md:132`. The five sites that TEACH the bare form are:

- `:93-94` — the `--sweep` usage text, "Use the no-flag mode for that";
- `:78` — the usage row `(no flag)   run the declared population`;
- `:412` — the no-`timeout` refusal, "Use the no-flag mode, which reports each suite as it finishes";
- `:746` — the unconditional end of the pooled branch, "for a cost verdict, run the serial mode:
  `bash $SELF`";
- `:758` — the pooled-RED remedy, "the serial re-run: `bash $SELF`".

None but `:77` contains the literal `run-selftests.sh`: `$SELF` is DERIVED at `:29-33` precisely so
that the file spells no literal, and it resolves to the bare path only at runtime. So AC7 is green
today with every remedy still teaching the form S2 turns into exit 2, and after S3 EVERY run of the
recorded DoD prints `:746` — an invocation that now refuses. `:412` is newly reachable from the DoD
because pooled requires a `timeout` binary, and it too sends the operator to the refused form. S5's
"every printed remedy" has a criterion that cannot fail on four of its five subjects: the predicate
never matches its target population, which is the could-not-fail class `AGENTS.md` §7 names. §7's
New arm list (bare-run refusal, regex pair, withhold/grade pair) also omits the arm round-1 M4's fix
named — every printed `bash $SELF` followed by a mode.

**Fix.** AC7 observes emitted bytes, not source text: run the fixture under `--pooled`, under
`SELFTEST_TIMEOUT_BIN=definitely-not-a-binary --pooled`, and `--help`, and assert every
stdout/stderr line containing `run-selftests` or `$SELF`'s expansion names `--serial` or `--pooled`
and none says `no-flag` or `(no flag)`. Keep the `SESSION-KICKOFF.md:132` grep. List the five sites
by line in S5 so the builder edits them. Add the M4 source arm to §7: every `bash $SELF` in the
runner is followed by `--serial|--pooled|--check|--list|--rank`, staged RED first.

**Left-shift gate.** That M4 arm, in `run-selftests.test.sh`, is the gate; it is one grep over the
runner and reds the day a remedy is added without a mode.

## H3 · id=4, id=9, id=26, id=35 — S6's raise has no literal; the described edit reds SLACK, which AC8 does not name

**Address:** section 2 S6 · section 4 Rollout · section 6 AC8.

Reproduced the epoch-2 carried-literal regex from `check-install-prefix.sh:250` over the runner: six
occurrences, at `:9`, `:42`, `:77`, `:82`, `:199`, `:229`, matching the pinned 6 at
`tools/install-prefix-carried.txt:109`. The usage line `:77` IS one of them. So Rollout's "the usage
line is the new literal" and S6's "naming the new literal the raise admits" rest on a false premise:
rewriting `:77` in place to add `--serial|--pooled` adds nothing. The refusal shape S2 reuses
(`:301-315`) and both remedies (`:746`, `:758`) print `$SELF` or no path, so a refusal in that shape
adds zero occurrences too. The checker counts occurrences per path (`:236-243`) and reds `SLACK` when
live < pin (`:466-468`, `bad++`, exit 1) — the other arm of the two-sided ban `TOOL-dRetiredFork-17`
made, and the verdict round-1 H7 already flagged. AC8's red condition names `ROSE` only. The leg is
unguarded, so it reds every bar.

Round-1 M3 said exactly this — name the line, and why `$SELF` is refused there — and rev-2 restated
the false premise. The builder is left to raise for a literal that already exists (SLACK at the
push, AC8 green) or to invent one, a repo-relative path in the refusal text, which ships gov's prefix
into adopters — the ban's whole point. On the kit-runner side, a pooled summary that spells `bash
tools/unattended/run-unattended-gates.sh --selftests --serial` literally is a ROSE 4→5 on that file,
outside S6's single raise (the `$ROOT/...` calls at `:258`/`:263` are not hits because the lead
character is `/`).

**Fix.** Either S6 names the line — "the bare-run refusal prints both forms with the repo-relative
path, one new occurrence at the refusal" — and says why `$SELF`, derived at `:32` before any
refusal can fire, is refused there (round-1 M3's ask, still unanswered); or S6 and AC8 are replaced
with "no count moves; every remedy and the refusal print `$SELF`, and the kit runner's summary
derives its own path". The second is the shorter diff and the one the runner's `:29-33` rule
already argues for. Either way, replace
the typed +1 with the rule the `tools/workflows/unattended-build.js` row already records: measure
with `bash tools/check-install-prefix.sh --list` at staging, raise by the measured delta per file,
justify each in the fourth column. AC8 red when the leg reds `ROSE` OR `SLACK` on any row this
commit touches.

**Left-shift gate.** Exists: the install-prefix leg is two-sided and unguarded. The gap is the
SPEC's: a `figure:`-bearing raise in an S item should have to name the line that carries the new
occurrence, which is the same witness tightening round-1 B1 asked of AC6 and check 12 does not do.

---

# MEDIUM

## M1 · id=12 — §7 Gates is wrong in both directions, and round-1 D-10 was not folded

**Address:** section 7 Gates · section 4 Files touched · section 9 revision log.

Verified against `tools/gate-legs.json`. §7 rev-2 lists `memory hygiene · install-prefix (shipped
surface) · run-selftests self-test · run-gates canary · unattended skill wiring`. Missing, all three
grading a touched file: `every held leg is budgeted, every budget row resolves` (`run-selftests.sh
--check`, unguarded — the predicate S1 rewrites and AC1/AC3 are observed by; round-1 D-10, confirmed,
and the rev-2 log claims the round folded while not listing §7, which did change from four legs);
`kickoff-manifest ratchet` (`manifest-check.sh`, whose manifest is `SESSION-KICKOFF.md`, now in Files
touched); `run-gates gov canary` (guard `tools/run-gates/`). Present but reading none of the five
touched files: `unattended skill wiring` (`adopt-unattended.sh --check`) — grep confirms zero
references to the runner, the kit runner, the test, the manifest or the carried ratchet.

The consequence is bounded because every missing leg is unguarded or guarded on `tools/run-gates/`,
so the BAR runs them regardless; what is wrong is the spec's own statement of what grades it, and a
fold that claims a round closed while leaving a confirmed row unfolded. MEDIUM on that basis, not
HIGH: the bar cannot miss these legs, the record does.

**Fix.** List the three by manifest name; drop `unattended skill wiring` or state which touched file
it reads. Add §7 to the rev-2 log's section list, or to rev-3's.

**Left-shift gate.** A spec-audit DoR check that derives §7 rather than authoring it: for each path
in Files touched, the legs whose `guard` covers it or whose `argv` names it, from `gate-legs.json`;
§7 states the derived set or explains each difference. Same rule as "derive over author".

## M2 · id=13, id=24 — §5 migration still wires the one bare caller to `--serial`

**Address:** section 5 migration vs section 2 S3 · section 4.

§5 migration reads "the five bare-mode arms and the one bare caller declare `--serial` in the same
commit; no other invocation exists in the tree". S3 wires that one caller (`:263`) to `--pooled` and
§4 calls rev-1's `--serial` wiring the inversion this rev corrects. Two answers to which mode `:263`
gets; a builder reading §5 lands rev-1's shape, and every criterion except AC4 stays green. The
second clause is also false: four documented invocations exist (H1).

**Fix.** "the five arms declare `--serial`; the one bare caller becomes the two declared kit-runner
invocations of S3 (or, under B1 fix (a), the `--serial` default plus a `--selftests --pooled`
sibling); the four DoD sentences name the mode they paste from".

**Left-shift gate.** None; a documented consistency check for the fold — every mode assignment is
stated in exactly one S item and every other mention points at it. This is round-1 B2's rule for
"the factor", applied to "the caller".

## M3 · id=6, id=15 — AC4 has no mechanism, admits any integer, and carries no `cost:` or `fixture:`

**Address:** section 4 Design (first paragraph) vs section 6 AC4 · section 5 observability · section
2 S4.

Verified at source. `:263` streams the runner's stdout uncaptured and reads only the exit code, and
§4's own first paragraph says so. Under `--sweep` the width pair is a preamble line, the withheld
count is a separate `run-selftests: N cost verdict(s) WITHHELD` line (`:745`), and the `sweep
GREEN|RED —` summary (`:748`/`:750`) carries neither. AC4 and §5 require the KIT RUNNER's summary
line to name `pooled` and the count; §5 says the runner prints both "on its summary line" while S4
and Rollout say the pooled output is `--sweep`'s unchanged. No design line says how the count crosses
the process boundary — a tee file, a capture of hours of output, an exit-code encoding. And "names
the withheld count" is satisfied by any integer: `withheld 0` on a seven-row green run passes.

The observation runs the real seven-row population (19430 s declared, 27200 s pooled wall) and the
kit runner has no self-test fixture of its own (`:263` hard-codes `--kit tools/unattended` against the
real `selftest-budgets.txt`; no `*.test.sh` in the tree exercises it). `memory/TEMPLATE-SPEC.md:346-348`
requires a `cost:` line where the observation is not seconds and a `fixture:` line where the tree
lacks one; AC4 carries neither, and its `OVER BUDGET` half is observable only if a breach happens to
occur that day. Hours per direction, and it cannot be staged RED — §7 says a gate not seen failing is
not landed.

**Fix.** One design line naming the mechanism (for instance: the runner prints its withheld count on
a greppable line the kit runner tees to a scratch file and re-reads). Pin the figure: on a green
pooled run, withheld equals the row count `--list` reports for the filter — the `_uc` the kit runner
already derives at `:258`. Add `cost:` and `fixture:` lines; for the fixture, copy the kit runner and
the runner into a scratch tree the way `run-selftests.test.sh`'s `build_repo` does at `:40`, with a
one-row unattended budget file, so both halves are seconds and can be staged RED. Reword §5 to
"prints the withheld count" unless the `sweep GREEN` line is meant to change, in which case AC5's
scope names the `--sweep` arms too.

**Left-shift gate.** Check 12's witness arm: a criterion whose `Red when` names a count should have
to name the derivation of the expected count, or it is `any integer`. A documented spec-audit rule
until then.

## M4 · id=18 — the roster and the derived build-order contradict the 4 → 3 → 5 → 1 → 2 chain

**Address:** `memory/builds/aBatchedArm/README.md` `roster:units` (`:66-70`) · `gen:build-order`
(`:104`) · spec-4 §1/§3 · spec-3 order 2.

Verified. The authored roster lists three units — 3 at order 1, then 1, 2 — with no row for 4 or 5.
The status headers now read spec-4 order 1, spec-1 order 2, spec-3 order 2, spec-2 order 3. The
generated `gen:build-order` therefore derives step 2 = `TOOL-aBatchedArm-1`, `TOOL-aBatchedArm-3`
in PARALLEL, against the README's own owner ruling (2) at `:58` ("the batching units are BUILT,
after the shard route"), against spec-3's `hands-off TOOL-aBatchedArm-1 — the conversion, which
lands on top of this split` (`:55`), and against the 4 → 3 chain spec-4 §3 and §4 depend on. Spec-3
rev-2 moved to order 2 without spec-1 and spec-2 shifting or the roster being re-authored. The
build's records give two orderings, and the derived one starts batching before the shard rows exist.
The orchestrator's stated roster — five units, 4 → 3 → 5 → 1 → 2 — is in neither file.

**Fix.** Roster rows for 4 and 5 with their mechanism; spec-1 to order 4 and spec-2 to order 5 (3
and 4 until unit 5's spec exists); re-render with `gen_build_index.py --write`.

**Left-shift gate.** Check 12's build-order region compares headers to the roster; it did not red
here because the roster table is authored prose and the collision is two specs sharing an order,
which the renderer treats as `Parallel: yes`. A check that an order shared by two units is declared
parallel-safe by a `hands-off` in NEITHER direction — spec-3 `hands-off` spec-1 — would have redded
this at the commit.

## M5 · id=33 — the manifest left-shift M5 named was dropped, and the S5 commit owes a re-stamp it does not list

**Address:** section 2 S5 · section 4 Files touched · section 5 user docs · section 6 AC7.

Verified: `manifest-check.sh` C5 and C5s (`:408-420`) key only on `watch:` pathspecs, and
`SESSION-KICKOFF.md:6` lists `run-gates.sh` and `gate-legs.json` but not
`tools/run-gates/run-selftests.sh`, so nothing can red the catalog line at `:132` on this or any
future runner change. Round-1 M5 named the one-token left-shift — add the runner to `watch:` — and
the spec neither adopts nor refuses it; S5 fixes the instance and leaves the class, against §7 "gate
the CLASS, not the instance". The manifest's own ratchet rule (`:19-21`, charter §1 DoD) also
requires a unit that changes a gate command to re-stamp `last-audit` with a delta line; the S5 commit
does that by rule and the spec lists it nowhere, so the commit breaks the manifest DoD while passing
the ratchet by construction.

**Fix.** Files touched and §5 user docs: the manifest-audit block re-stamp bundled in the S5 commit
with its delta line (stamp rule at `:22`), and `tools/run-gates/run-selftests.sh` added to `watch:`
in the same edit. AC7's red condition adds "or the commit touching `:132` leaves the audit block's
stamp equal to HEAD's".

**Left-shift gate.** The `watch:` entry IS the gate; once the runner is watched, C5s reds any future
runner change that does not re-audit the catalog line.

---

# LOW

## L1 · id=21 — the cost-model paragraph misattributes the scanner and dropped its cite

**Address:** section 4 "What the cost model says about the goal".

`run-unattended-gates.sh:170-171`, written on node `d`, records that "an on-access antivirus scanner
sits in front of every exec on this node, and one spawn costs 0.019-0.039 s here against roughly a
millisecond on a machine without one" — the 19-39 ms node HAS the scanner. Spec-4 §4 `:111` reads
"on a node without the on-access scanner (19 to 39 ms per spawn against 251 here)", misattributing
the host property it argues from. The paragraph also gives two spawn costs for node `a` in one breath
— 190 ms (`:107`, the `TOOL-aPooledSweep-1` record) and 251 ms (`TOOL-aGradedDoorway-7` S3) — with no
cite for either; git shows rev-1 (`d19e7b75`) carried `TOOL-aGradedDoorway-8` at that sentence and
rev-2 (`9b00bc7b`) removed it. The pair 251 versus 19-39 is `TOOL-aGradedDoorway-10`.

**Fix.** Cite `TOOL-aGradedDoorway-10`; one per-spawn figure for node `a` with its record; "on node
`d` (scanner present, 19-39 ms)".

**Left-shift gate.** None; a wording fix. A documented rule: a figure in a design paragraph carries
the id of the record that measured it, or it is a number typed beside the source that owns it.

---

## What a fold should do first

One decision precedes the redraft, and it is the same one round 1 put second: **which invocation
carries the goal, and when** (B1). Rev-1 answered "serial, so nothing pooled exists"; rev-2 answered
"pooled, as the default, at the bound the record shows killing the rows". The honest third answer is
both spellings now and the default flip owned by the unit that owns the bound. Whichever form the
fold takes, H1 follows from it — the four DoD carriers say what the pasted verdict must come from —
and M2's sentence is rewritten in the same pass.

After that, the mechanical set is a single pass with every line number in hand: AC7 observes bytes
and the five sites are listed (H2); S6 names its line or is deleted, AC8 names SLACK (H3); §7 is
derived from `gate-legs.json` (M1); AC4 gets its mechanism, its pinned count and its two template
lines (M3); the roster gets rows for 4 and 5 and the orders stop colliding (M4); the runner joins
`watch:` and the re-stamp is listed (M5); one cite comes back (L1).

Two things the fold got RIGHT should not be reopened: the factor is gone and the bound is unit 5's,
and the edges now point the right way with unit 3's mirror written. Round-1 D-1, D-2, D-4, D-5, D-11
(the caller count) and D-12 (S4 lands with S2) were read again this round and nothing stood against
them.
