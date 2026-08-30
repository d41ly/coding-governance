**Serves:** spec-audit TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8

# Spec audit — aGatheredDeclaration, round 3

Reviewed 2026-08-31 on node `a`, in worktree
`.claude/worktrees/gate-bar-tooling-review-020565`, against the working tree at base `44734f15`.
Round 1 returned BLOCKED with 5 blockers over 29 findings; round 2 returned BLOCKED with 4 blockers
over 18 rows. This round audits the ROUND-2 FOLD — rev-3 of the eight specs — with the fold text
treated as unreviewed surface, because three of round 2's four blockers were themselves round-1 fold
artifacts. Every source citation below was re-derived against the tree at this base: no claim is
carried from a finder, from round 1, or from round 2 without being re-read.

**Range · ROUND 3.**
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-1.md@c94f2e0d506427755e8c611d8e49f3590d522294` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-2.md@67e0384e73036d1cdf9fc48a19e8ece44d85f5a0` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-3.md@a16b2fe5d09fbbd5795fd54dbb7b882e0e8f41d3` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-4.md@abbbf97df465c1233bf4cb04595966308bb8f6de` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-5.md@98553830ccb3b78007cf7e3497cd702e9f9012cd` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-6.md@bc9bdb6a67ff5b74d080648c1852dca722129cd8` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-7.md@f48ec67feeeaf4984b49f0c38991cf315dccb824` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-8.md@8eeb8846dbd6ce741c547484e62347a2952bfb5f`

## Verdict: BLOCKED

Three blockers and nine highs. Three is strictly smaller than round 2's four, so under
`memory/guides/BUILD-METHOD.md` M4 the loop CONVERGES rather than terminating, and one more fold is
owed. The count is the honest one and not a manufactured one: seven of this round's twenty-five
confirmed findings are the SAME cross-unit join reached from three documents, and they are merged
into a single row here rather than counted seven times.

All three blockers are fold-introduced, and all three are the same failure mode at different
addresses: rev-3 corrected a mechanism and did not carry the correction through to the sequence, the
file list, or the sibling criterion that grades it. Round 2's fold named a wrong writer; round 3's
fold named the right writer and put it two steps too late. Not one of the three is a design
disagreement — each is a criterion that cannot be green at the landing of the unit that owns it.

## Review shape

Raw 42 · confirmed 25 · refuted 17 · unverified 0 · precision 0.60.

The 25 confirmed findings de-duplicate to **14 rows**. Four merges, source ids named on each row:
seven findings reached the units 4/5 → unit 6 forward dependency (ids 1, 2, 13, 14, 22, 23, 34) and
are one row; three reached the half-emitted `[bar]` table (ids 6, 18, 36); two the stale
files-touched lists (ids 32, 35); two the `LEG` row output-contract collision (ids 15, 26); two the
`S1(e)` miscount (ids 20, 33). Precision at 0.60 is up from round 2's 0.54 and round 1's 0.42, which
is the expected shape for a third pass over a shrinking surface with the priming carried forward.

**Severity criterion, carried verbatim from round 2 so the three rounds are comparable.** BLOCKER — a
merge-bar leg reds at the unit's own landing, two criteria in the reviewed set cannot both pass, or a
scope item names a mechanism that provably cannot perform it, so the implementer is blocked or must
invent the design the spec claims to have made. HIGH — nothing in the build catches it: a
could-not-fail acceptance criterion, a guard disarmed by absence, or a sibling contradiction the ACs
are blind to. MEDIUM — a real gap that an existing acceptance criterion or gate WILL catch during the
build, at the cost of a rework loop rather than a wrong landing. LOW — a false claim in a spec whose
argument survives it.

Two severities differ from the incoming finder grade, both stated where they occur: R7 is raised from
MEDIUM to HIGH (the evidence it grades is destroyed at unit 6 and cannot be recovered afterwards),
and R14 is settled at LOW (round 2 graded the identical class at LOW as R18). No finding was lowered
to keep the blocker count under four; the three that are blockers are blockers under the criterion
above and the rest fail it on their own terms.

## The fold's two new joins

Both joins the fold created were audited directly, since a join is where a spec set fails without any
single document being wrong.

**Units 4, 5 and 7 → unit 6 S1(d).** The three consumers spell the same thing three ways and only one
of them is sequenced possible. Unit 7 S10 seeds `[bar]` "from the same defaults
`TOOL-aGatheredDeclaration-6` S1(d) emits" and is `order 7` against unit 6's `order 6` — legal, and
its defect is the key SET rather than the sequence (R4). Units 4 and 5 are `order 4` and `order 5`
and grade an artifact unit 6 first emits at `order 6` — illegal under M2's ordering axis (R1). The
build README's `gen:build-order` table sequences all eight units strictly, none parallel, so there is
no reading under which units 4 and 5 land after unit 6.

**Unit 8 → unit 2 S11.** Sequenced correctly (`order 2` before `order 8`) and spelled identically on
both sides: `short_circuit`, a `[[lane]]` key, boolean, default `false`. The join is possible. It is
also unarmed — neither half of the declaration has a criterion anywhere in the set, and unit 8 grades
only the `true` behaviour (R9).

## What the fold closed, and what it did not

Round-2 findings are not re-reported except where the fold left a gap. Six did.

| Prior | What the fold did | Gap |
|---|---|---|
| R1 (u4/u5 route `[bar]` through `[gate_runner_seed]`) | repointed both at unit 6 S1(d)'s splice emitter | the emitter is sequenced AFTER both consumers, and both files-touched lists still name the refuted block — **R1**, **R5** |
| R4 (u7 `--upgrade` emits no `[bar]`/`[[profile]]`) | added S10 and AC8c | S10 seeds from S1(d)'s set, which is two keys of the four unit 2 declares — **R4** |
| R5 (u6 inventory omits `profile_bar.py`) | added S9 putting the file in scope | no criterion names it and §7 omits the leg that exercises it — **R8** |
| R6 (`subject` → `opt_in` priced at three edits) | added S1(e) with the full 68-row pricing | one of the three figures in it is wrong — **R14** |
| R15 (u3 pinned `LEG` row vs the fold-new columns) | pinned the row as an OUTPUT CONTRACT with an append-only rule | unit 4 AC8 overwrites the pinned column one step later — **R2** |
| R16 (`short_circuit` declared by no unit) | added u2 S11 | neither the validation nor the default has a criterion — **R9** |

Closed cleanly: R2 (predicate 6 now moves, S8/S8b/AC10b), R10 (`turnstile_ttl` now graded by u2
AC14), R3 (u6 AC6 rewritten to the waiver-set form that is actually satisfiable), R11, R12, R13, R14,
R18 (36 corrected to 38 of 86, with the two `guard = []` rows named).

**R17 is knowingly still standing** and is not re-litigated here: the stale `govkit.py:2510-2512`
citation survives at unit 6 §10 line 271 and unit 7 §10 line 228, re-read at this base. LOW, owner's
call, listed once so the next round does not rediscover it.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| R1 | BLOCKER | 4, 5, 6 | u4 §2 S7 / §6 AC9; u5 §2 S3 / §6 AC5; u6 §2 S1(d) | two criteria grade an artifact the emitter first writes two steps later, and the emitter itself lands unarmed |
| R2 | BLOCKER | 3, 4 | u3 §4 `LEG` row / §2 S9 / §6 AC11; u4 §4 / §6 AC8, AC1b | one output contract spelled twice and incompatibly; u3 AC11 and u4 AC8 cannot both be green |
| R3 | BLOCKER | 6 | §2 S5 · Rollout · §6 AC7 | the Rollout adds leg rows and AC7 in the same section asserts the leg count is unchanged |
| R4 | HIGH | 2, 6, 7 | u6 §2 S1(d); u7 §2 S10 / §6 AC8c; u2 §4 | the emitted `[bar]` table is two keys of the declared four, and nothing defaults or refuses the other two |
| R5 | HIGH | 4, 5 | u4 §4 · u5 §4 Files touched | both lists still name the block rev-3 disproved, and neither names the file rev-3 points at |
| R6 | HIGH | 6 | §2 S1(b) against §6 | the comment-preserving splice is graded by no criterion a reserialise would fail |
| R7 | HIGH | 2 | §2 S5 against §6 | gov's own migration carries no criterion that the comments survived it |
| R8 | HIGH | 6 | §2 S9 · §7 | `profile_bar.py` degrades to UNVERIFIED after S7 and no criterion or leg observes it |
| R9 | HIGH | 2, 8 | u2 §2 S11 / §5 / §6 | `short_circuit` validation and default are unruled by every criterion in the set |
| R10 | HIGH | 2, 6 | u6 §2 S7b / §4; u2 §4 | both canaries re-derive the manifest path themselves; u2 §4 says the derivation is one seam |
| R11 | HIGH | 6 | §2 S1(c) · §5 | a fresh intake of a below-floor target gets a TOML declaration and no legacy pair to fall back to |
| R12 | HIGH | 2 | §2 S7 · §6 AC11 | the `GATE_OPTIN` rename leaves govkit's kit-payload policy guard keyed on the old spelling |
| R13 | MEDIUM | 2 | §4 Files touched | the estimate omits `.githooks/pre-push` and its test, which fold-new S8 and three ACs work in |
| R14 | LOW | 6 | §2 S1(e) | "21 under `tools/govkit/entries/`" is 18 rows in 11 files |

---

### R1 — BLOCKER — two criteria grade an artifact their own units cannot produce

**Address:** unit 4 §2 S7 and §6 AC9; unit 5 §2 S3 and §6 AC5; unit 6 §2 S1(d).
*(source ids 1, 2, 13, 14, 22, 23, 34)*

Rev-3 fixed round 2's R1 by naming the correct writer of the adopter `[bar]` defaults —
`TOOL-aGatheredDeclaration-6` S1(d)'s textual-splice emitter — and left both grading criteria where
they were. Unit 4 AC9 parses an emitted `<prefix>/gate-legs.toml` and asserts
`enforce_ceilings = false`; unit 5 AC5 parses the same file and asserts `turnstile = false`. Unit 4 is
`order 4`, unit 5 is `order 5`, unit 6 is `order 6`, and the README's `gen:build-order` block
sequences all eight strictly with `Parallel = no` on every row.

At steps 4 and 5 there is no producer of that file at all. Verified against source at this base:
`tools/run-gates/kit.toml:107-108` still declares `grammar = "json-array"` above
`file = "{prefix}/gate-legs.json"`; `tools/govkit/govkit.py:2947-2948` refuses any other grammar with
`[gate_runner].grammar = '<x>' — only 'json-array' is implemented`; and the intake emitter writes the
target's `[gate_runner]` block from a closed key tuple. Both criteria therefore grade a file that
does not exist at the landing of the unit that owns them, which is
`memory/guides/BUILD-METHOD.md:65`'s ordering axis by name — "no sub-spec depends on a unit sequenced
after it". A builder either fails the DoD or performs unit 6's S1(b)+(c)+(d) work inside unit 4,
which is the scope violation the fold was written to remove.

The mirror is the same defect seen from the other end: unit 6's S1(d) — now the single write path
three units rest on — is graded by NO criterion of its own. AC1 grades the emitted rows against the
descriptors' `[[gate_leg]]` blocks, AC12 grades the grammar key and the filename, and no unit 6
criterion reads `[bar]`. The scope item lands unarmed at step 6 while its only two arms sat two steps
upstream against nothing.

**Fix.** Move S7/AC9 and S3/AC5 into `TOOL-aGatheredDeclaration-6` beside S1(d), merged into one
criterion that parses the emitted `<prefix>/gate-legs.toml` in a freshly intaken scratch target and
asserts the whole `[bar]` table — asserted in `tools/govkit/selftest.py`, where unit 6's other intake
arms already sit, not in `tools/run-gates/adopt-run-gates.test.sh`, which runs no intake (it
hand-writes `$t/$pfx/gate-legs.json` at line 39) and drives a verb whose non-check path prints
`nothing to write — the [gate_runner] declaration is emitted by govkit intake`. Leave units 4 and 5 a
one-line §3 pointer saying the adopter default is DECLARED here and GRADED at unit 6, naming that AC
id. Resequencing unit 6 ahead of units 4 and 5 also closes it, but drags the whole legacy-pair
deletion forward and is the larger edit.

**Left-shift gate.** The build-record renderer already computes `gen:build-order`. A spec-audit
check that greps each unit's §6 for `TOOL-a<slug>-<n>` references and reds when a criterion cites a
unit with a HIGHER order number than its own would have caught this fold and round 2's, mechanically,
for about twenty lines of Python beside `gen_build_index.py`. That is the cheapest gate this review
has produced across three rounds and it is worth building before the next fold.

### R2 — BLOCKER — one output contract, two specs, incompatible on the shipped configuration

**Address:** unit 3 §4 ("The `LEG` row format is an OUTPUT CONTRACT"), §2 S9, §6 AC11; unit 4 §4 and
§6 AC8, AC1b.
*(source ids 15, 26)*

Rev-3 pinned the `--manifest` row at unit 3 §4 line 87 as
`LEG  <name>  <lane>  <opt-in|always>  <ceiling|none>  <guards>  <would-run|held|guarded-out>`, with a
header ending `ceilings <on|off>`, and declared the format append-only precisely so a later unit could
not overwrite a column. Unit 3 S9 states that its ceiling/measured/ratio join exists "once
`TOOL-aGatheredDeclaration-4` turns enforcement off", and AC11 requires each row to carry the declared
ceiling, the ledger seconds and their ratio, flagging any ratio under 3.

Unit 4 §4 line 69 and AC8 line 162 then redefine that same column in that same state: "every leg's
ceiling column reads `declared, not enforced`, asserted by grepping the output". A two-word,
comma-bearing string in a whitespace-delimited row, replacing the number AC11 computes on. Unit 3's
arm lands at step 3 and stands; unit 4 lands at step 4 and breaks it. AC11 and AC8 cannot both be
green on the configuration this build ships, and the ratio S9 exists to publish loses its numerator —
the rot-detector unit 3 built for exactly the state unit 4 creates.

AC1b compounds it: it requires the header to name the resolution SOURCE (`declaration` versus the
environment), and the pinned header has no field for one. Unit 4 nowhere amends unit 3's contract; it
simply restates the row differently. That is M2's interface axis — one interface spelled twice,
spelled differently — and a builder cannot arbitrate between two ratified specs.

**Fix.** Spell the row once, in unit 3 §4, and have unit 4 cite it. Keep the declared number in the
ceiling column, APPEND an `enforced|declared-only` column at the end of the row per unit 3's own
append-only rule, and extend the header to `ceilings <on|off> from <env|declaration|default>`. Then
reword unit 4 AC8 and AC1b to grade those two fields rather than a substitute string.

**Left-shift gate.** Unit 3 already owns the right shape and does not use it: make the `LEG` row
format a fixture in `tools/run-gates/run-gates.test.sh` — one recorded row, field-by-field — so any
later unit changing a column reds the arm instead of quietly redefining the contract in prose. The
same fixture is what AC11's ratio arm parses, so it costs one file and pays for both.

### R3 — BLOCKER — the Rollout adds leg rows and the criterion beside it asserts none were added

**Address:** unit 6 §2 S5, the Rollout paragraph (line 134-136), and §6 AC7 (line 205).
*(source id 17)*

S5 makes `tools/unattended/run-unattended-gates.sh` a thin call into `run-gates.sh --leg`, and the
Rollout states plainly: "Its seven leg names move into the declaration as `opt_in = true` rows
carrying the 2026-08-23 owner ruling as their comment." This is required rather than optional —
unit 3 S1/AC4 make `--leg` refuse a name the manifest does not hold. AC7, sixty lines later in the
same document, asserts that a `GATE_SELFTESTS=1` bar on this tree "is GREEN and its leg count is
unchanged".

Re-derived at this base: `tools/gate-legs.json` holds 86 rows.
`tools/unattended/run-unattended-gates.sh` dispatches EIGHT `run_one` calls, not seven — three of
them (`kit gate`, `playbook validity gate`, `skill wiring`) already exist as manifest legs
(`unattended kit gate`, `playbook validity gate`, `unattended skill wiring`); the other five
(`gate selftest`, `driver selftest`, `playbook validity selftest`, `cross-component`, `adopter e2e`)
are in neither the manifest nor `tools/unattended/kit.toml`, because the 2026-08-23 owner ruling
removed them so adopters stop receiving them. Folding them in takes the declaration to 91 rows, which
contradicts AC7 outright. Worse, AC7's own arm runs `GATE_SELFTESTS=1`, so it would then EXECUTE the
suites that ruling took off the bar — the script's own declared budgets for those five are 3800 s,
970 s, 300 s, 300 s and 120 s.

A builder cannot satisfy both lines, and the arbitration between them is a partial reversal of a
recorded owner ruling, which is not a builder's decision to make.

**Fix.** Decide it in this document. Either state in S5 that the five absent suites become
`opt_in = true` rows, reword AC7 to "86 plus the five folded-in rows, enumerated", and record the
partial reversal of the 2026-08-23 ruling in §3 with the owner's assent; or give `--leg` a declared
exemption for kit self-test names in unit 3, keep the manifest at 86, and leave AC7 as written.
Either way correct "seven leg names" — the script dispatches eight, three of which are already legs.

**Left-shift gate.** The count claim is the gateable half: AC7 should assert the leg count against
`tools/gate-legs.toml` as a DERIVED figure with the expected delta stated in the criterion, not as
the word "unchanged". A criterion that says "unchanged" cannot survive a scope item that changes it,
and this is the third round in which a prose count in this build has disagreed with the tree.

### R4 — HIGH — the emitted `[bar]` table is half the declared table, in both write paths

**Address:** unit 6 §2 S1(d); unit 7 §2 S10 and §6 AC8c; unit 2 §4 data model and §5.
*(source ids 6, 18, 36)*

Unit 2 §4 declares a four-key `[bar]`: `enforce_ceilings`, `default_ceiling = 1800`, `turnstile`,
`turnstile_ttl = 1800`. Unit 6 S1(d) emits two of them. Unit 7 S10 seeds the upgrader's `[bar]` "from
the same defaults `TOOL-aGatheredDeclaration-6` S1(d) emits" and AC8c grades it "key-by-key against
`TOOL-aGatheredDeclaration-6` S1(d)'s emitted set rather than against a list typed here" — so the
second write path inherits whatever the first names, and both agree on a manifest missing half the
table.

The two missing keys are the two with live consumers. Unit 2's own consumer table names
`[bar].turnstile_ttl` as the replacement for the TTL derivation at `run-gates.sh:434` and
`[bar].default_ceiling` as the replacement for the per-leg bound fallback at `:1104`; unit 4 §3 and
§10 both lean on `default_ceiling` as the thing that lets ceiling declaration stay mandatory without
every leg carrying a number. No unit declares a built-in fallback for either key's absence, and
unit 2's refusals cover an unparseable file, an unknown leg key, an undeclared lane, an empty leg
list, an escaping `cwd` and (AC15) a missing `[[profile]]` row — nothing for a partial `[bar]`. So
unit 2's "`ceiling` absent means `[bar].default_ceiling`" resolves to nothing the moment an adopter
sets `enforce_ceilings = true`.

The charitable reading of S1(d) — "the table, including these two" — does not rescue it. It relocates
the defect into AC8c, which then grades key-by-key against a set no document states, and unit 6 has
no criterion over `[bar]` at all (see R1's mirror) to pin it down.

**Fix.** State the emitted set once, in S1(d), as all four keys with their shipped values, and give
unit 6 a criterion over that set. Add to unit 2 a refusal — exit 2 naming the key — for a `[bar]`
missing any key the loader resolves a default against, the same shape AC15 already gives
`[[profile]]`. AC8c and unit 7 S10 then inherit the fix without further edit.

**Left-shift gate.** The refusal IS the gate: a loader that reds on a partial `[bar]` cannot be
satisfied by a partial emitter, so the two write paths are held by one check rather than by two
criteria agreeing with each other. Observe it RED first against today's two-key emission.

### R5 — HIGH — both files-touched lists name the block their own spec disproves

**Address:** unit 4 §4 Files touched (line 93) and unit 5 §4 Files touched (line 82).
*(source ids 32, 35)*

Rev-3 corrected the prose in both units and never touched the estimates. Unit 5 S3 says the adopter
`turnstile = false` is written by unit 6 S1's emitter and is "**NOT `[gate_runner_seed]`**"; twenty
lines later its Files touched ends with "`tools/run-gates/kit.toml` (the `[gate_runner_seed]`
block)" as its only adopter-facing file, and `tools/govkit/govkit.py` — the file that does the
writing — appears nowhere. Unit 4 carries the identical stale entry, annotated "(for S7)", four lines
above the paragraph that refutes it by name and by source, plus `tools/run-gates/adopt-run-gates.sh`
"(S7)" — the read-only verb the same section proves seeds nothing.

One document, two answers to "which file carries the adopter default", eight lines apart, with the
refuted answer sitting in the operative list an implementer and a closing review both work from.
Unit 4's `adopt-run-gates.test.sh` entry is legitimate only as long as AC9 lives there; if R1 is
taken, it goes too.

**Fix.** Delete the `[gate_runner_seed]` and `adopt-run-gates.sh` entries from both lists. If R1 is
taken, both lists lose their adopter-seed entries entirely and unit 6's estimate — which already
names `tools/govkit/govkit.py` — carries the emitter edit alone. Add one line to each saying so, so
the two lists cannot drift apart again.

**Left-shift gate.** A spec-audit check that reds when a unit's §6 cites a file its §4 estimate does
not name would catch this class and R13 at once. Cheap, mechanical, and it fires on the exact
symptom: a criterion asserted in a file nobody budgeted to open.

### R6 — HIGH — the comment-preserving splice is graded by nothing a reserialise would fail

**Address:** unit 6 §2 S1(b), against §6.
*(source id 3)*

S1(b)'s entire justification for a textual splice over a parse-and-reserialise is that a reserialise
"would delete every argument this build exists to make storable". No §6 criterion observes that a
re-emit preserves owner prose outside the marker comments. AC1 grades only that the emitted rows
match the selected descriptors' `[[gate_leg]]` blocks — which a full reserialise satisfies perfectly
while destroying every comment in a target's `gate-legs.toml`. AC12 grades grammar and filename;
AC11, AC7 and AC9 grade selfcheck, bar and testsuite population. An implementation that skips the
splice entirely passes the whole set.

The failure is silent and it repeats: this emitter runs on every adopter's `govkit apply`, not once
per migration. And the build already knows how to grade the class — `TOOL-aGatheredDeclaration-7` AC3
asserts prose survival by grepping a sentinel planted in the fixture. The sibling unit grades it; the
unit whose scope item is ABOUT it does not.

**Fix.** Add a criterion to §6: when `govkit intake`/`apply` re-emits a target's `gate-legs.toml`
that already carries owner comments above a leg and outside the marker pair, those bytes are
unchanged — asserted in `tools/govkit/selftest.py` against a fixture carrying a sentinel comment,
observed RED first against a reserialising writer.

**Left-shift gate.** That criterion is the gate; it belongs in `selftest.py` as a permanent arm, not
as a one-time build check. A sentinel comment in the emitter fixture costs one line and fails the day
anyone "simplifies" the splice into `tomlkit`-less reserialisation.

### R7 — HIGH — gov's own migration has no criterion that the comments survived it

**Address:** unit 2 §2 S5, against §6.
*(source id 7. Raised from the finder's MEDIUM: the evidence is destroyed at unit 6 and cannot be
recovered afterwards, which puts it past "a rework loop".)*

S5 requires "every `gate-profiles.txt` comment carried across verbatim and every ceiling exceeding
`[bar].default_ceiling` gaining a comment stating why". No §6 criterion observes either half. AC1
compares leg count and manifest order, AC5 compares the held set by resolving both loaders, AC12
grades knob KEYS in the `[[profile]]` rows, AC13 asserts a green bar. A migration that dropped every
comment paragraph greens all four.

This is the build's stated reason for existing — the README's problem statement is that JSON "keeps
silently deleting the reasoning" — and gov's own 86-leg migration is the single instance of it that
ships. The loss becomes permanent at unit 6, where S7 deletes `gate-profiles.txt`, after which the
evidence to grade against no longer exists in the tree. Unit 7 AC3 grades exactly this class for a
FOREIGN manifest, so the tool built for adopters is held to a bar gov's own migration is not.

**Fix.** Add a criterion: after S5, every comment paragraph in `tools/run-gates/gate-profiles.txt` at
BASE appears in `tools/gate-legs.toml` — computed by extracting both comment sets and diffing, not by
a spot grep — and every leg whose `ceiling` exceeds `[bar].default_ceiling` carries a preceding
comment line. It must be an arm at unit 2, not a manual check at unit 6.

**Left-shift gate.** A one-shot arm is correct here and a permanent gate is not: the source file is
deleted two units later, so there is nothing for a standing check to compare against. Say that
explicitly in the criterion, so the next reader does not "generalise" it into a leg that silently
passes on a missing input — which is the dead-probe shape this repo names by name.

### R8 — HIGH — `profile_bar.py` degrades to UNVERIFIED and no criterion or leg watches it

**Address:** unit 6 §2 S9 and §7.
*(source id 4)*

S9 puts `tools/run-gates/profile_bar.py` in scope; no §6 criterion names it, and §7's gate list omits
`profile-bar selftest` — the leg that exercises it — while units 2 and 8, neither of which edits the
file, both list it.

Verified against source: `profile_bar.py:319` resolves `GATE_LEGS` or
`os.path.join(os.path.dirname(KITDIR), "gate-legs.json")`; `measure_orphans` returns None on an
unreadable manifest, and `:523` renders that as "timing-cache orphans: UNVERIFIED, manifest or cache
unreadable." So after S7 deletes the JSON, an unmoved reader degrades to a reassuring UNVERIFIED
rather than a red. AC9 grades only `check-testsuite-counts.sh`, whose hard `exit 2` makes it
self-announcing; the carrier that fails SILENTLY is the one nothing grades. AC7 does not rescue it —
`profile-bar selftest` is `chunk = selftests`, `subject = kit`, guarded on `tools/run-gates/`, and its
arms drive scratch fixtures, so it is green whether or not the reader moved. Nor does the dead-path
backstop: S10 waives 30 surviving `gate-legs.json` carriers and AC6 grades green with the declared
waiver set, so `profile_bar.py`'s reference is waived along with the legitimate ones.

**Fix.** Add a criterion: after S9, `python tools/run-gates/profile_bar.py` resolves the TOML and its
timing-cache-orphan line reports a real count rather than UNVERIFIED, asserted against a tree with
the JSON deleted and observed RED first against the unmoved reader. Add `profile-bar selftest` to §7.

**Left-shift gate.** The generalisable one: any probe whose "cannot look" branch prints a
non-failing line needs an arm that asserts the branch is NOT taken on a healthy tree. One arm per
UNVERIFIED-style renderer, in that tool's own selftest. This is the second UNVERIFIED-degradation
finding in this build across three rounds.

### R9 — HIGH — `short_circuit` is declared and then ruled by nothing

**Address:** unit 2 §2 S11, against §5 and §6; unit 8 §6 AC3/AC4.
*(source id 5)*

Fold-new S11 gives unit 8 the declaring owner round 2 said it lacked, and declares two properties —
"validated as a boolean and defaulting to `false`". Neither has a criterion. AC9's refusal is
leg-scoped in both clauses ("a leg carries a key the schema does not declare, or names a lane no
`[[lane]]` row declares"); AC7's byte-marshalling is scoped to `[bar]` booleans; §5's error-state
list covers an unparseable file, an unknown leg key, an undeclared lane, an empty leg list and an
escaping `cwd`, and never mentions lane-row validation. A `[[lane]]` row carrying
`short_circuit = "yes"` is unruled everywhere in the set.

That is the exact inversion unit 5 S2 and AC1c exist to close one table over: a truthy non-boolean
makes unit 8 S3 skip every later lane, and the run reports skips rather than a refusal — a silent
narrowing of the bar. The default half is equally dark: unit 2 §4's example writes
`short_circuit = false` explicitly, so gov's shipped file never exercises the absent-key path, and
unit 8 AC3/AC4 grade only the `true` behaviour.

**Fix.** Extend AC9 to cover a `[[lane]]` row with an undeclared key or a non-boolean
`short_circuit`, exit 2 naming the lane and the key, observed RED first. Extend AC7's byte-comparison
to `[[lane]]` booleans so a declared value cannot reach a string test as a word. Add the absent-key
default to the same arm, or add a criterion asserting a lane declaring no `short_circuit` does not
short-circuit.

**Left-shift gate.** Validate the `[[lane]]` table the same way the `[[gate_leg]]` table is
validated, in the same pass, rather than adding a per-key check. One schema walk over every declared
table closes this key and the next one somebody adds.

### R10 — HIGH — the manifest derivation is three copies, and unit 2 says it is one

**Address:** unit 6 §2 S7b and §4 Files touched; unit 2 §4 (the "one seam" paragraph).
*(source id 27)*

S7b moves only the two canaries' GUARD LISTS. Verified against source, both canaries independently
RE-DERIVE the manifest path with a hardcoded basename — `run-gates.test.sh:57` and
`run-gates.gov.test.sh:82` both read
`LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"` — and then `json.load` it across many
arms, with two more sites hardcoding `$ROOT/tools/gate-legs.json` outright. Unit 2 §4 asserts the
derivation is one seam and "nothing else about it moves"; there are three. Unit 6 §4's reader
inventory — the table rev-3's own log says was re-derived after "a grep nobody re-ran" — lists neither
canary as a reader, and `tools/run-gates/run-gates.gov.test.sh` appears in Files touched only under
the catch-all "the affected suites".

The deletion half of this reds loudly (AC7 runs `GATE_SELFTESTS=1` and both canaries would fail to
resolve their manifest), so this is not ungradeable. What earns HIGH is the false inventory claim
that a second implementer will trust, and the interval between units 2 and 6 in which both canaries
certify a file the bar no longer reads — that half is silent.

**Fix.** Widen S7b from "guard lists" to "the canaries' own manifest derivation and every arm that
parses it", name `tools/run-gates/run-gates.gov.test.sh` in Files touched, and correct unit 2 §4's
"nothing else about it moves" to name the two duplicate derivations.

**Left-shift gate.** Ban the duplicate derivation rather than fixing its three instances: one
resolver, sourced by both canaries and by `profile_bar.py`, plus a grep-based check that reds on any
tracked file outside it computing a manifest path from `dirname`. Gate the class, not the instance —
this is the third inventory-incompleteness finding in unit 6 alone.

### R11 — HIGH — a fresh intake below the interpreter floor gets a file it cannot read and no fallback

**Address:** unit 6 §2 S1(c) and §5 (error states).
*(source id 28)*

S1(c) makes every freshly intaken target declare `grammar = "toml-legs"` and a `.toml` file
unconditionally; S7 deletes `tools/run-gates/gate-profiles.txt` and its `[[lf_pin]]` from the kit.
Nothing in unit 6 probes the TARGET's interpreter for the CPython 3.11 floor unit 2 S4 establishes.

A target whose runtime python is below 3.11 is therefore intaken with a TOML-only declaration and,
after S7, no `gate-profiles.txt` either — so unit 2 S3's fallback ("the legacy PAIR is read
otherwise") has nothing to fall back TO, and that target's merge bar cannot load a manifest at all.
Unit 6 S7's own reassurance — "Unit 2's dual-format arm keeps reading the pair in an adopter or below
the interpreter floor" — is exactly what fails for a freshly intaken target, which has neither half of
the pair. The only floor probe in the build is unit 7 S9, deliberately built as "a SHARED preflight
every write verb calls" — but on `adopt-run-gates.sh`, a shell verb in a different program, landing
one step later. Unit 6 §5's error-state bullet covers only an absent or malformed manifest.

**Fix.** Add a scope item requiring `cmd_intake` to run the same interpreter probe — refuse, or emit
the legacy pair alongside, naming the interpreter and its version — and a criterion in
`tools/govkit/selftest.py` for an intake into a below-floor target. State in §5 what a below-floor
adopter receives.

**Left-shift gate.** Unit 7 S9 already has the right instinct: make the floor probe a shared
preflight that BOTH write programs call, and have govkit's selfcheck red if a write verb reaches the
emitter without it. A capability floor checked in one of two writers is a floor with a door in it.

### R12 — HIGH — the `GATE_OPTIN` rename leaves the policy guard watching the old spelling

**Address:** unit 2 §2 S7 and §6 AC11.
*(source id 37)*

S7 makes `GATE_OPTIN` the new canonical spelling and names two carriers: pre-push predicate 8 and the
run-record byte. It misses the machine guard keyed on the old one. Verified against source,
`tools/govkit/govkit.py:1441` compiles its policy regex with the literal alternation
`(?:GATE_SELFTESTS=\S*|\$\{GATE_SELFTESTS:?=[^}]*\})` and `:1473` fails any kit-shipped file carrying
it. Its own header (`:1417-1439`, `TOOL-dUnstalledConvoy-28`) states why it exists: a repo-local hold
policy must not ride out inside a kit payload, because doing so "would turn the kit self-tests back
ON for exactly the repositories `TOOL-dUnstalledConvoy-26` exists to spare".

After the rename, a kit shipping `export GATE_OPTIN=1` matches nothing and nothing reds. The
enforcement half of a recorded owner ruling would cover only the deprecated alias — gate-the-instance
rather than the class, created by the spec's own change. Check `7h3` appears in no unit's scope and no
non-goal withholds it. The secondary carriers the finder listed (`run-gates.sh:1175` and `:1366`
messages, `tools/run-gates/README.md`, `AGENTS.md`, `subject-pins.tsv`, `profile_bar.test.sh`) are
cosmetic while the alias stays valid and are not part of this finding.

**Fix.** Extend S7 so the govkit gate-policy predicate accepts BOTH spellings, and add a criterion in
`tools/govkit/selftest.py` that a bare `GATE_OPTIN` assignment inside a kit payload REDS, mirroring
the existing arm at `selftest.py:1588`. Observed RED first against the unmoved regex.

**Left-shift gate.** Any rename scope item should state where the OLD spelling is machine-matched, not
only where it is read: `git grep -n GATE_SELFTESTS -- '*.py' '*.sh'` is the whole derivation, and it
belongs inside S7 as the command rather than beside it as a list. This is the second rename in this
build that missed a regex.

### R13 — MEDIUM — the unit 2 estimate omits the trust-boundary file the unit edits

**Address:** unit 2 §4 Files touched (lines 186-188).
*(source id 31)*

The list names exactly six paths — `gate-legs.toml`, `run-gates.sh`, `run-gates.test.sh`,
`run-gates/README.md`, `run-gates/kit.toml`, `.gitattributes` — and neither `.githooks/pre-push` nor
`.githooks/pre-push.test.sh`, while fold-new S8 widens predicate 6's pathspec inside the hook and
AC10, AC10b and AC11 all assert in the hook's selftest. rev-3 added S8, S8b and AC10b and did not
carry the change into the estimate. This is not a convention of the set: unit 4 lists
`.githooks/pre-push` and unit 6 lists both the hook and its test, so unit 2 is inconsistent with its
siblings and with itself. The one file in the unit that is a trust boundary is invisible to the
estimate a closing review scopes against.

**Fix.** Add `.githooks/pre-push` (predicate 6 pathspec) and `.githooks/pre-push.test.sh` (AC10,
AC10b, AC11) to the line, and note there that predicate 7 is deliberately NOT touched per S8b.

**Left-shift gate.** Same check as R5: red when a §6 criterion names a file the §4 estimate does not.
One check, two findings, and it fires on the fold's exact failure mode — a criterion added without
the estimate behind it.

### R14 — LOW — a derived split, typed in prose, wrong in its third figure

**Address:** unit 6 §2 S1(e).
*(source ids 20, 33)*

S1(e) prices the descriptor key migration as "68 `subject = ` rows across 23 descriptor TOMLs, 21
under `tools/govkit/entries/` and the rest in other kits' `kit.toml`". Re-derived at this base: 68
rows across 23 files — both correct — of which 18 rows in 11 files sit under `tools/govkit/entries/`
and 50 rows in 12 files elsewhere. The directory holds 12 tracked files in total, so "21" matches
neither the row count nor the file count nor the files present, under any reading. The wrong figure
sits inside an otherwise-verified sentence, which is what makes it worth a row: it reads as
re-derived because its neighbours are.

**Fix.** Restate as "18 rows across 11 files under `tools/govkit/entries/` and 50 across the other
kits' `kit.toml`", or drop the split and keep the 68/23 totals with the derivation command beside
them.

**Left-shift gate.** None to build — the charter rule already covers it: no count of a derived
population is written in prose. This is the same class round 2 caught as R18 (36 versus 38 of 86) and
the fold corrected there while creating this one, in the sentence that was correcting a mispricing.
The cheap habit, not a gate: when a spec must state a count, state the command that produced it on
the same line.

---

**Convergence.** 5 blockers (round 1) → 4 (round 2) → 3 (round 3). Strictly decreasing, so the loop
continues under M4. R1 and R5 are one fold's work and close seven of this round's confirmed findings
between them; R2 and R3 each need one sentence chosen and written down rather than any new design.
The pattern across three rounds is now unmistakable and worth naming in the fold: every blocker this
build has produced was created by a fold that corrected one half of a statement and left the other
half — the sequence, the file list, or the criterion — pointing at the version it just replaced.
