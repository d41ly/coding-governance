**Serves:** spec-audit TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24

# aWokenSentinel — spec audit of units 21 to 24, round 1

*Node `a`, 2026-09-20. A Tier-2 adversarial pass over the four specs the round-3 disposal
commissioned as the promotions of its four highs, before any code: a fan of four primed finder
lenses, a skeptic stage in five batches prompted to REFUTE each finding, one synthesis. The mandate
was the one the three earlier rounds ran: underspecification, contradiction between sibling specs on
the four axes (scope, interface, ordering, acceptance), unstated assumptions about the harness and
the driver, and criteria that cannot fail, with every code claim checked against the cited file and
line at HEAD `53fd251c` and, where a spec names it, at the build's base `830c46e8`. The synthesis
re-read at source every claim the highs rest on and every medium but two; what it re-read, and
what it did not run, is listed at the end.*

**Round: 1.** Subjects, each pinned at the blob the commission named:

- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-21.md@208faf9380cee4d5d9b6f736a982b1d4ac1b56c4`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-22.md@8ac1b8d4ac38ae44f08ede4f7a0978a518a3539c`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-23.md@71ffb1f8e47aa7cb8d6b19960c64bccc49139f74`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-24.md@f4252457e210e4de2517c4e13bf4a0c696e29328`

Every pin names the text that was reviewed. The synthesis ran `git rev-parse HEAD:<path>` and
`git hash-object <path>` for all four at the time of writing: each pair agrees with the pin above,
and `git status --short` prints nothing, so no subject is modified in the working tree.

## Verdict: CLEAN WITH FIXES

No blocker stands. No unit inverts its purpose in a way its own criteria would miss, no sibling
contradiction leaves a merge-bar leg red with no unit owning the fix, and no pin names a text other
than the one the lenses read. Eleven raw findings in six defects are high, and every one is a fold
with a named fix inside the unit's own Files touched. Spec 22 writes the first `hit` of each arm
pair as a readable prefix of the branch's sentence and says that prefix "is what `check-arms.py`
reads as an arm"; the tool signs a branch by the longest literal run before the first
interpolation and arms it only when a test line CONTAINS that whole run, so both branches this unit
exists to arm read UNARMED as designed, and AC4's greps pass on the stranded arms. Spec 22's pushed
control lands the fixture's record and moves `origin main`, and the accepting arm that already
follows in the region has no setup of its own, so it reads `phase: LANDED` from the control's write
and its three `miss` lines pass on an unrelated refusal — green by absence, and nothing in §6 sees
it. Spec 21 adds a leg name to the manifest and names none of the three unguarded meta-gates that
red on a new leg from the landing commit: the testsuite-counts leg wants the `PASS` line §3 refuses,
`govkit selfcheck` wants a row in the GENERATED `subject-pins.tsv`, and the codebase map wants the
key claimed in a dossier; the gotcha `a-new-leg-trips-a-growing-set-of-meta-gates` records exactly
this trap. Spec 23 bans three spellings and stages one. Nine raw findings in seven defects are
medium and two in two are low. Spec 24 drew no confirmed finding; see the shape section for what
that zero is and is not evidence of.

## Review shape

Raw 36, confirmed 22, refuted 14, unverified 0, precision 0.61. That is above the ~0.5 floor §8
sets, below round 3's 0.77 and round 1's 0.80, and above round 2's 0.58. The four specs are
denser than the six before them in one respect: three of the four add or move a leg, an arm or a
check that a meta-gate grades, and a lens that reads the spec without reading the meta-gate
manufactures a refutable finding as easily as a confirmable one.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by
the pipeline's dedup stage. The run is complete on its own terms. Because no lens died, every unit
was read by all four lenses, and the zero confirmed findings on spec 24 is a zero from reading, not
from absence. It is still only a zero over what four lenses and five skeptic batches could see in
one round: the synthesis was handed the 22 confirmed ids and not the 14 refuted ones, so whether
any refuted finding named spec 24 is not in this record's inputs, and a unit that draws no
confirmed finding in one round has been read, not certified. The pipeline's dedup found 0, but the
22 confirmed ids contain several that name one defect from different lenses (three found spec 22's
stranded arm literals, two found its pushed control, two found its clean-tree `fixture`, two found
its AC3 base half, two found spec 21's missing `PASS` line, two found its unclaimed map key). The
fold below is editorial: it groups them into 15 distinct defects and keeps every raw id. Each raw
id takes the severity of the defect it evidences, so the per-id tally and the integers returned
with this report agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| H1 spec 22's arm literals stop short of the signature `check-arms.py` reads; both branches the unit exists to arm read UNARMED | high | 12, 22, 33 |
| H2 spec 22's pushed control lands the record and moves `origin main`; the accepting arm that follows reads the control's write | high | 1, 23 |
| H3 spec 21 enrols the suite in `testsuite counts` and refuses the `PASS` line that leg requires | high | 18, 29 |
| H4 spec 21's new leg name is an unclaimed key of the codebase map's `gate-legs` inventory | high | 20, 30 |
| H5 spec 21 never names `tools/govkit/subject-pins.tsv`, the GENERATED file `govkit selfcheck` reds a new leg without | high | 19 |
| H6 spec 23 bans three spellings and stages one; the here-string branch has no RED observation | high | 2 |
| M1 spec 22's `fixture` on a clean tree makes no commit; `_unpushed` is HEAD, which `origin main` holds | medium | 4, 21 |
| M2 spec 22 AC3's base half names a report the driver at `830c46e8` cannot produce | medium | 3, 13 |
| M3 spec 21 S1's ceiling rule is observed by no criterion; a ceiling of 1 passes AC1 | medium | 5 |
| M4 spec 21 AC4 bounds the pin from above only; a pin of 1 passes AC4 and AC5 | medium | 6 |
| M5 spec 21 withholds the after-exit structural arm `TOOL-dUnstalledConvoy-19` asks for, on the suite whose stranded fixtures are its reason to exist | medium | 31 |
| M6 spec 23's population includes `check-unattended.test.sh`, the file S4 has stage the offending bytes | medium | 16 |
| M7 spec 23 homes a repo-wide class in one kit's shipped checker on a false population premise, with `sh_hygiene.py` unweighed | medium | 35 |
| L1 spec 21 places the floor compare AFTER the `--- $n arms, exit $st` line, so a breach prints `exit 0` then exits 1 | low | 17 |
| L2 spec 22 cites `spec 16 §4` for the ordering `TOOL-aUnblockedFleet-7` records, in a shipped suite comment | low | 34 |

Tally by raw id: **0 blocker · 11 high · 9 medium · 2 low** = 22. Two severities moved from the
skeptic's verdict, both by the one-defect-one-severity rule. Raw 33 (skeptic: medium) was RAISED to
high inside H1 beside 12 and 22 (skeptic: high), because the three ids name one defect and the
argument for high is in H1's section. Raw 21 (skeptic: high) was LOWERED to medium inside M1
beside 4 (skeptic: medium), argued in M1's section: the arm as written reds loudly at the pass on
two assertions, so the defect is a staged input the pass has to debug, not a reading that ships.
H1 and H2 were each weighed for blocker and left at high, argued in their sections.

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| H1 | high | TOOL-22 | §4 'The two arms'; §2 S4; §6 AC3, AC4; §7 | `signature()` of spec 16's two sentences runs to `…fix what the lander writes. marker holds` and `…so the landing it records is not the one`; `classify()` arms on `sig in line` (`check-arms.py:235`); both `hit` literals in §4 stop at the first clause and contain neither, so both branches read UNARMED and AC4's fragment greps cannot see it. |
| H2 | high | TOOL-22 | §2 S2; §4 pushed control; §5 risks; §6 AC2 | The control reads `phase: LANDED` count 1, so it lands the record and `-f` pushes `tscratch:main`; the accepting arm at `unattended.test.sh:4549-4554` has no setup, so it runs `--landed` on a terminal record, its `miss`es pass on `fail 26`'s text and its `same 'phase: LANDED' == 1` reads the control's write. §5's "as every marker arm already does" is false for that arm. |
| H3 | high | TOOL-21 | §3 'No PASS line'; §2 S1, S4; §4 floor block; §7 | `testsuite counts (every bar self-test prints one)` is unguarded, `subject = repo`; its population is every `*.test.sh` string in the manifest (`check-testsuite-counts.sh:36`); `compliant()` requires an anchored `echo "PASS ($n assertions)"` beside the floor, and a floor with no such line reds with `pins a floor but does not print the agreed count line`. S1 enrols the suite, S4 pins the floor, §3 refuses the line. |
| H4 | high | TOOL-21 | §4 'Files touched'; §7 | `map_extractors.py` enumerates `gate-legs` as every leg name in the manifest; `codebase-map coverage + freshness` is unguarded and `test_every_inventory_key_is_claimed_or_baselined` reds on an unclaimed key; the three sibling legs are claimed at `memory/map/features/review-harnesses.md`; the spec names no dossier and no regeneration of `memory/map/generated/*`. |
| H5 | high | TOOL-21 | §4 'Why a held leg and not a bar leg'; 'Files touched'; §7 | `govkit.py:1743` reds any manifest leg with no row in `tools/govkit/subject-pins.tsv` (`a NEW leg reds until its subject is on the record`); that file is GENERATED by `selfcheck --write` and is not in Files touched; the `[[exempt_leg]]` row the spec says "is what keeps" selfcheck green covers the descriptor-claim check only. |
| H6 | high | TOOL-23 | §2 S1, S3; §4 'The staged break'; §6 AC1 | S1 scopes `printf '%s\n'`, `echo` and the here-string `wc -l <<< "$x"`; S3 and AC1 stage only the printf spelling; §4 says the pattern's escaping "is the pass's to get right against the fixture of S3, and the fixture is the proof". The `<<<` alternation is a separate regex branch with the variable on the other side of the command and has no RED observation. |
| M1 | medium | TOOL-22 | §2 S2; §4 'The two arms' (scratch line); §6 AC2 fixture line | `fixture()` is `git add -A && git commit -q -m fixture --no-verify` (`unattended.test.sh:363`); the preceding check-34 refusal leaves the tree clean, so on `tscratch` it makes no commit, `_unpushed` is HEAD, `origin main` already holds it, the driver accepts, and `hit 'does not reach'` reds. §4's "it is made on top of it" needs a tracked write nothing names. |
| M2 | medium | TOOL-22 | §6 AC3 base half, against §4, §10 and Edges | AC3 says "at this unit's base the report lists the two branches of S1 and S2 as unarmed"; `git show 830c46e8:tools/unattended/unattended.sh` holds 0 occurrences of either sentence and 4 `fail 34` sites, none of them these; the spec's own §10 says "the sentences do not exist before unit 16". The base half is unobservable as written. |
| M3 | medium | TOOL-21 | §2 S1; §6 AC1 | S1 says the ceiling is the budget times `sweep-ceiling-factor` (2, `selftest-budgets.txt:49`) "so the bar's hang bound and the on-demand runner's agree"; AC1 observes "a positive integer". The siblings do not follow the rule (tier2-review 60 → 1800, review-join 460 → 300, verifier 230 → 300), so nothing else enforces it, and `derive-ceilings.py` reports an unbacked leg without failing. |
| M4 | medium | TOOL-21 | §6 AC4, against §2 S4 and §4 | AC4 bounds the pin "at or below `c * 9 / 10` and above `0`"; S4 and §4 author it AT `floor(c * 0.9)` (285 of 317). A pin of 1 satisfies AC4 and AC5 and is a floor a lost arm never reaches; AC4's own Red-when names the zero pin and not the near-zero one. |
| M5 | medium | TOOL-21 | §3 'No structural after-exit arm'; §2 S4; against `TOOL-dUnstalledConvoy-19` and spec 19 S5 | The `-19` row (backlog `TOOL.md:68`) records that a numeric floor fixes the instance and not the class; spec 19 S5 writes the one-grep after-exit arm for the adopter suite and its round-3 M11 fold was for exactly this omission; spec 21 installs ~32 assertions of slack on a suite ending `exit $st` at `:1256` and defers the one-liner to a backlog row. |
| M6 | medium | TOOL-23 | §2 S1 population, S4; §4 header list; §3 and Edges population claim | S1's population is every `*.sh` beside the checker except the checker, which includes `check-unattended.test.sh`; S4 has that file write `_x=$(printf '%s\n' "$_o" \| wc -l)` into a copy, and the suite's quoted-heredoc idiom (`:188`) puts those bytes on a non-comment line the `^[^#]*` predicate matches. The fixture at `:65` copies no suite, so AC1 cannot see the self-hit; the close's `unattended kit gate` reds over the real directory. |
| M7 | medium | TOOL-23 | §3 'No scan outside the kit'; §4 'Alternatives rejected'; §2 S1, S5 | `check-unattended.sh:2728-2733` derives `KIT_SH` with `*.test.sh) continue` and is the checker's ONLY `*.sh` glob, so "the population every check in that gate reads" and "unit 11's check already reads the same files" are both false (spec 11 reads three named files and rejects the glob). `tools/gate-lint/sh_hygiene.py` already scans every tracked `*.sh` for silent-misbehaviour classes with a two-direction selftest, and `resolve-python.test.sh:113` bans a retired idiom in any tracked `*.sh`; neither is weighed. |
| L1 | low | TOOL-21 | §4 'The floor block' placement, against §2 S4's cited shape | §4 inserts the compare after `echo "--- $n arms, exit $st"` (`:1255`); the cited sibling `gate-guard.test.sh:455-457` compares BEFORE its summary line. As placed, a breach prints `--- N arms, exit 0` and then exits 1. |
| L2 | low | TOOL-22 | §2 S2; §4 pushed-control comment; §6 AC2 | The ordering the control accepts is the run-B-overwrites-run-A race `TOOL-aUnblockedFleet-7` records; spec 16 cites the id twice, spec 22 cites `spec 16 §4` three times and the id never, and the citation lands in a suite `kit.toml` ships to adopters, whose convention is full ids. |

### H1 — high — TOOL-22 §4 'The two arms, beside the accepting one', §2 S4, §6 AC3 and AC4, §7 — raw 12, 22, 33

**The defect.** Re-read at source and executed. `tools/memory-tree/check-arms.py`'s `signature()`
(`:106-122`) splits the branch's message on its interpolations, strips `:`, `"` and spaces from
each piece, and takes the LONGEST surviving literal run; `classify()` at `:235` arms a branch when
`any(b["sig"] in l for l in lines)`, a containment test over whole test lines. The docstring at
`:113-116` warns: "the run does not stop where the sentence does … An arm that stops at the last
WORD reads as unarmed with no hint why; run `--report` and copy the row it prints." The synthesis
ran `signature()` over spec 16 rev-2's two sentences (spec 16 `:94` and `:100`). The no-sha branch
signs as
`the lander marker carries no commit sha, so it is a touched file and not evidence; fix what the lander writes. marker holds`
and the unreachable branch signs as
`the lander marker names a commit the remote default branch does not reach, so the landing it records is not the one`.
Spec 22 §4's first `hit` of each pair is
`the lander marker carries no commit sha, so it is a touched file and not evidence` and
`the lander marker names a commit the remote default branch does not reach`; `sig in hit` is
`False` for both, checked programmatically. §4 states the opposite: "The first `hit` of each pair is
the branch's own failure text, which is what `check-arms.py` reads as an arm." Built as designed,
both branches this unit exists to arm read UNARMED, S4 cannot hold, AC3 reds at the pass, and
`harness arms (fail branches armed or pinned)` reds at the close on the unit whose §1 exists to
make it green. AC4 — the criterion written to red when "the arms exist under another text, which
`check-arms.py` does not read as arming these branches" — greps `carries no commit sha` and
`default branch does not reach`, both of which the stranded arms contain, so the one criterion
aimed at this class passes on it. `memory/gotchas/arm-literal-strands-on-message-edit.md` records
this shape ("An arm must contain the branch's ENTIRE literal signature. A readable PREFIX of a
long message reds") and its remedy, copy the `--report` row, which the spec did not follow.

Raw 33 raised to high: the three ids name one defect, two skeptics verified it as high, and the
argument that it is high rather than medium is that the design text asserts the tool's behaviour
and asserts it wrong on the unit's whole purpose, and that the AC written for this class cannot
fire on it. Weighed for blocker and left at high: AC3 at the tip DOES red on the stranded arms
(the `--report` lists them unarmed), so the pass sees a loud failure rather than a green, and the
fix is two literals copied from a row the tool prints.

**The fix.** S1, S2 and the §4 block state that the first `hit` of each pair quotes the signature
`check-arms.py --report` prints, verbatim to its last character (through `marker holds` and
through `is not the one`), and §4 says the literal is copied from `--report` per the gotcha. AC4's
two greps count those full signatures rather than the fragments, so AC4 can red on a stranded arm.
Keep the interpolated-tail `hit`s as the second line of each pair.

**Left-shift.** The class is gated already, at the close, by `harness arms`; what is missing is
the same predicate at authoring time. A one-loop pre-flight for the commission — for every
`hit "$out" "<literal>"` a spec's §4 writes, assert `literal` contains some row of
`check-arms.py --report` over the driver at the spec's order — would have caught H1 and the
round-3 H2 it descends from. Until that exists, every spec that says "which is what
`check-arms.py` reads as an arm" should carry the `--report` row it copied as a fenced line.

### H2 — high — TOOL-22 §2 S2, §4 pushed control, §5 risks, §6 AC2 — raw 1, 23

**The defect.** Re-read at source. `verb_landed` in `tools/unattended/unattended.sh` runs
`refuse_if_terminal` first (check 26; LANDED is terminal and prints `the run is already finished`),
then the `phase != LANDING` refusal (check 31, `:2379-2381`, which also refuses an UNCOMMITTED
LANDING), then `check_clean`, all before check 34. Spec 22's pushed control reads
`grep -c '^phase: LANDED'` as `1`: it lands the record, which dirties the tree, and its
`git push -q -f origin tscratch:main` moves `origin main` to the scratch commit. Files touched
places the two arms and the control "after the parent-commit arm spec 16 adds", which is before the
existing accepting arm at `unattended.test.sh:4549-4554` because that arm needs a LANDING record.
That accepting arm does no `reset_tree`, no `sed` to LANDING, no `fixture` and no push of its own;
the region's next arm, the MISSING-marker one at `:4556-4562`, has its own setup precisely
because, in the suite's own words, "the arm above lands the record and a terminal record refuses
this verb for an unrelated reason". So §5's risk line — "the arm that follows in the region
re-pushes `HEAD:main` before its own read, as every marker arm already does" — is false for the
arm that follows: the all-zero arm at `:4541` does not re-push either. With the control in place,
the accepting arm runs `--landed` on a LANDED record, `fail 26` prints, none of its three `miss`
strings is that sentence so all three pass, and its `same "the run reached LANDED …" == 1` reads
the phase the control wrote. An existing arm goes green by absence and no criterion in §6 can see
it, because §6 observes the two new arms and the control and not the arm they displace.

Weighed for blocker and left at high: the defect is a fixture after-state, the fix is three lines
the region already uses, and the arm it silences is spec 16 AC3's, whose own spec is in the same
build and is re-audited at every round.

**The fix.** S2 and AC2's fixture line state the after-state the control leaves and its
restoration: after the pushed read,
`sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md; fixture; git push -q -f origin HEAD:main`,
or give the two arms and the control their own `reset_tree; run --preflight; mkconf; phase LANDING;
fixture; push` block placed AFTER the accepting arm, the way the MISSING-marker arm is placed. State
as a precondition of S1 that the record is at a committed LANDING with HEAD advertised. Add an AC
that the accepting arm still reads its acceptance from a LANDING record after the new arms run: its
`grep -c '^phase: LANDING'` prints 1 at entry.

**Left-shift.** The class is an arm whose reading is inherited from a predecessor's write. The
accepting arm's three `miss`es pass on ANY refusal, which is the vacuous shape; giving that arm a
`same "entered at LANDING" "$(grep -c '^phase: LANDING' RUN.md)" "1"` before its `run` makes it
self-guarding against any future insertion, and is the one-line gate for this region.

### H3 — high — TOOL-21 §3 'No `PASS (<n> assertions)` line', §2 S1 and S4, §4 'The floor block', §7 — raw 18, 29

**The defect.** Re-read at source. `tools/gate-legs.json` carries
`testsuite counts (every bar self-test prints one)` with no `guard`, `subject = repo`, `chunk =
declarations`, so it runs on every bar. `tools/check-testsuite-counts.sh:36` derives its population
as every `"…\.test\.sh"` string in the manifest, regardless of the leg's chunk or guard; S1 puts
`tools/workflows/unattended-build.test.sh` in that set. `compliant()` at `:70` requires an
anchored `echo "PASS ($n assertions)"` line, a non-zero `FLOOR_ASSERTIONS=`, and a compare; a file
with `^FLOOR_ASSERTIONS=[0-9]+$` and no such line takes the branch at `:106`, `a self-test pins a
floor but does not print the agreed count line … wants echo "PASS ($n assertions)"`. S4 pins the
floor, §3 refuses the line ("the sentence a green prints is not this unit's to rename"), §7 does
not list the leg, so the close finds it cold. The sibling block S4 copies,
`tools/unattended/gate-guard.test.sh:455-457`, carries the `PASS` line at `:457`; the copy is half
the shape. `memory/project/testsuite-count-waivers.txt` is shrink-only by its own header, seeded
from a measured population, so a waiver row is the ratchet reversal and not a remedy. The leg reds
on every bar from the landing commit.

**The fix.** Drop the §3 non-goal. S4 adds, under the compare, the line the sibling has one line
below it: `[ "$st" = 0 ] && echo "PASS ($n assertions)"`, keeping `--- $n arms, exit $st`. Add
`testsuite counts (every bar self-test prints one)` to §7 and an AC that
`bash tools/check-testsuite-counts.sh` exits 0 at the tip and names the suite at a tip without the
line.

**Left-shift.** Already gated; the leg is the gate, and it would have fired. What is missing is
the spec-time check: a commission pre-flight that, for every `*.test.sh` a spec's S-items add to
the manifest, runs `compliant()` over the spec's own §4 block. One grep per spec.

### H4 — high — TOOL-21 §4 'Files touched', §7 — raw 20, 30

**The defect.** Re-read at source. `tools/codebase-map/map_extractors.py:72-93` enumerates the
`gate-legs` inventory as every leg name in `tools/gate-legs.json`, raising on a nameless leg
rather than dropping it. `codebase-map coverage + freshness` is unguarded, `subject = repo`, `chunk
= declarations`; `test_codebase_map.py:93`'s `test_every_inventory_key_is_claimed_or_baselined`
reds on any key no dossier claims and `baseline.toml` does not carry, and the baseline is
shrink-only. The three sibling legs are claimed at `memory/map/features/review-harnesses.md:11-15`
(`review-join self-test`, `tier2-review self-test`, beside two workflow-script keys). Spec 21 names
no dossier, no claim and no regeneration of `memory/map/generated/{MAP.md,inventories.json}`, and
§7 does not list the coverage leg; the charter's DoD makes the claim and the regen same-commit.
`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md` records this trap by name. The
leg reds every bar until claimed.

**The fix.** Add `unattended-build self-test` to `[claims].gate-legs` in
`memory/map/features/review-harnesses.md`, refresh its prose on touch, run
`python3 tools/codebase-map/gen_map.py --write` in the same commit; list the dossier and
`memory/map/generated/*` in Files touched; add `codebase-map coverage + freshness` to §7 with an AC
on `--check` at the tip.

**Left-shift.** Gated already, at the bar. The gotcha exists and `gotchas.py --for-diff` would
name it over a diff touching `tools/gate-legs.json` if the record anchors that path; the
synthesis did not run `--for-diff` to confirm the anchor and says so. If it does not anchor
there, anchoring it is the one-line left-shift; if it does, the commission's pre-flight should run
`--for-diff` over each spec's Files touched as if it were the diff, which is what the tool is for.

### H5 — high — TOOL-21 §4 'Why a held leg and not a bar leg', 'Files touched', §7 — raw 19

**The defect.** Re-read at source. `tools/govkit/govkit.py:1743` fails `selfcheck` for any
manifest leg with no row in `tools/govkit/subject-pins.tsv`: `gate leg '<nm>' has no row in
tools/govkit/subject-pins.tsv — a NEW leg reds until its subject is on the record … Regenerate
with python tools/govkit/govkit.py selfcheck --write`. That file's header at `:1700` says
GENERATED, and its current rows include every sibling self-test leg (`agent-cap self-test`,
`install-prefix self-test`, and so on at `:14-52`). Spec 21 lists `govkit selfcheck` as a close
gate and says in §4 and §7 that the `[[exempt_leg]]` row "is what keeps a held leg claimed by no
descriptor from redding"; that row satisfies the descriptor-claim check at `~:1670` and nothing
else. Files touched names four files and not `subject-pins.tsv`; every prior spec in this tree that
adds a leg names it. As specced the close gate reds with the sentence above.

**The fix.** Add `tools/govkit/subject-pins.tsv` to Files touched, regenerated by
`python tools/govkit/govkit.py selfcheck --write` in the same commit as the leg, and say in §4
that the exemption row and the subject pin are two different ratchets with two different refusals.

**Left-shift.** Gated already; the refusal names its own remedy. The spec-time class is "a Files
touched that omits a GENERATED artifact the change moves"; the commission pre-flight can grep each
spec's Files touched against the set of `# GENERATED` headers under `tools/` and `memory/map/`
whose generator reads a file the spec touches. H4 and H5 are the same omission twice.

### H6 — high — TOOL-23 §2 S1 and S3, §4 'The staged break', §6 AC1 — raw 2

**The defect.** S1 scopes three spellings: `(printf '%s\n'|echo) "$x" | wc -l` and
`wc -l <<< "$x"`. §4 disclaims its own snippet's escaping: "the exact escaping of the pattern is
the pass's to get right against the fixture of S3, and the fixture is the proof." S3 and AC1 stage
one line, `_x=$(printf '%s\n' "$_o" | wc -l)`, and observe RED on it, GREEN with it removed, and
GREEN on the near-miss. The `echo` spelling shares the printf group of the regex, so the one
staged line exercises that group's alternation weakly; the here-string spelling is a separate
top-level branch with the variable on the OTHER side of the command, and no observation reaches
it. §10's real-tree run had zero hits for any spelling, so it proves nothing about that branch
either. A regex whose `<<<` alternation is mis-escaped passes AC1 through AC4 and the class gate
lands with two thirds of its predicate never seen to fail, which is the charter §7 rule for a new
gate ("not landed until its failing case has been observed") broken on two of three cases.

**The fix.** S3 and AC1 stage each of the three spellings in turn in the suite copy —
`_x=$(echo "$_o" | wc -l)` and `_x=$(wc -l <<< "$_o")` beside the printf line — and require the
checker to red on each, naming the line; S4's suite arm stages all three so the `harness arms` leg
keeps them covered. The cost line rises from three kit-gate runs to five, and AC1 says so.

**Left-shift.** The class is "a predicate with N alternations and a fixture with one". A
commission pre-flight can count `|` at the top level of any regex a spec's §4 fences and compare
it to the number of distinct staged lines its S-items name; a mismatch is a finding before a lens
reads it. Spec 11's check, with its three named files, is the same shape one unit earlier.

### M1 — medium — TOOL-22 §2 S2, §4 'The two arms' (the scratch-commit line), §6 AC2 fixture line — raw 4, 21

**The defect.** Re-read at source. `fixture()` at `unattended.test.sh:363` is
`git add -A >/dev/null && git commit -q -m fixture --no-verify`; every one of its call sites in
the suite writes a tracked file first. `verb_landed` calls `check_clean` before check 34, and a
check-34 refusal writes nothing (the record is untouched, the marker lives under the git common
dir), so after S1's arm the tree is clean. §4's S2 line is `git branch -f tscratch HEAD; git
checkout -q tscratch; fixture; _unpushed=$(git rev-parse HEAD); git checkout -q -` with no write
before `fixture`; on a clean tree `git commit` prints `nothing to commit` and exits 1 with HEAD
unchanged, and the suite runs `set -u` without `set -e`, so execution continues. `_unpushed`
resolves to the run-branch HEAD, which the region already pushed as `origin main`; `is-ancestor` is
reflexive; the driver accepts, writes LANDED, `hit "… does not reach"` reds, and
`same "unpushed marker leaves the record at LANDING" … "1"` reds. §4's "`fixture` is the suite's
own commit-making helper, which is how the scratch commit contains HEAD: it is made on top of it"
is false without a tracked write, and neither S2 nor AC2's fixture line ("one `fixture` commit on
a scratch branch") names one.

Raw 21 lowered to medium: the skeptic's high rests on "the arm cannot be built as written", which
is true, but the arm as written reds on two assertions the moment the pass runs it, so the defect
is a staged input the pass debugs in minutes, not a reading that lands. Round 3's M5 (a driver
copy that refuses at exit 2 for a reason other than the one named) is the precedent shape.

**The fix.** State in S2 and AC2's fixture line the tracked write that precedes `fixture` on the
scratch branch (`printf 'scratch\n' >> memory/builds/tRun/RUN.md`, or a throwaway file), or use
`git commit -q --allow-empty -m scratch` and say why an empty commit is enough here. Have the arm
assert `[ "$_unpushed" != "$(git rev-parse <run-branch>)" ]` before it writes the marker, so a
no-op commit is named as such rather than mistaken for the predicate accepting.

**Left-shift.** `fixture()` itself: make it refuse a no-op with its own sentence
(`fixture: nothing to commit — the arm forgot its write`), one line in the helper, so every
future arm that forgets the write reds with the cause rather than with a downstream assertion.
That is the class fix in the shared function the ponytail rule asks for.

### M2 — medium — TOOL-22 §6 AC3 base half, against §4, §10 and §3 Edges — raw 3, 13

**The defect.** Re-read at source. The status header pins base at `830c46e8`, and AC4 uses "at
this unit's base" for the file at `830c46e8`, so the phrase is not the post-unit-16 tree.
`git show 830c46e8:tools/unattended/unattended.sh | grep -c 'carries no commit sha'` prints 0 and
`grep -c 'fail 34'` prints 4 — the equality compare is still there, and `check-arms.py --report`
keys branches by the `fail 34` sites that exist in the file it reads, so at base it lists check 34's
four existing branches (`:1242`, `:2481`, `:2493`, `:2500`) and cannot list S1's or S2's at all,
armed or otherwise. The spec agrees with this everywhere but AC3: §4 says "at this unit's order the
tree's driver already carries unit 16's predicate", §10 says "the sentences do not exist before
unit 16", the Edges say "Without the predicate neither sentence exists to read". AC3's base half —
"at this unit's base the report lists the two branches of S1 and S2 as unarmed" — is unreachable
as written, so the pass either skips it or reports a report listing no such branches and calls the
criterion satisfied.

**The fix.** Re-point AC3's RED-first reading to the file at the tip of unit 16's pass — "the
commit whose subject carries `TOOL-aWokenSentinel-16`" — the shape spec 24 AC3 already uses for
unit 18, and drop the `830c46e8` baseline from AC3 while keeping it for AC4, where it is right.

**Left-shift.** The round-3 report named this class (M8, M15: a base-side figure the base cannot
produce because a lower-order sibling writes it) and its pre-flight: run every "at this unit's
base" reading against `git show <base>:<path>` at authoring time. It was not run for this spec.
One loop over `spec/*.md`.

### M3 — medium — TOOL-21 §2 S1, §6 AC1 — raw 5

**The defect.** S1 says the leg's `ceiling` is the S2 budget times the budgets file's
`sweep-ceiling-factor` (2, `selftest-budgets.txt:49`) "so the bar's hang bound and the on-demand
runner's agree"; AC1 observes only that `ceiling` is "a positive integer", and its figure line
restates the derivation without observing it. Verified: the three siblings do not follow the rule
(tier2-review budget 60, ceiling 1800; review-join 460, 300; verifier 230, 300), so it is this
spec's own invariant and nothing else enforces it; `derive-ceilings.py` reports an UNBACKED leg
and does not fail (`:316-317`), and it never reads budgets. A ceiling of 1, or one below the
budget, passes every §6 criterion, and the first flagged bar can kill the suite at a hang bound
under its own cost verdict.

**The fix.** AC1 adds: the leg's `ceiling` equals the row's second field in
`tools/run-gates/selftest-budgets.txt` times the integer on the `# sweep-ceiling-factor:` line,
both read by the same `python3 -c` at observation.

**Left-shift.** The declaration leg `every held leg is budgeted, every budget row resolves`
already joins the two files by name; extending its join with `ceiling >= budget` for every held
leg is the gate for the class, and the three siblings it would red today are the finding it would
print first, which is the "run the predicate over the real tree first" rule paying for itself.

### M4 — medium — TOOL-21 §6 AC4, against §2 S4 and §4 — raw 6

**The defect.** AC4 bounds the pin "at or below `c * 9 / 10` and above `0`", while S4 and §4
author it AT ten percent under the static count (285 of 317 at base). AC4's own Red-when names
"the pin is zero, which cannot fail"; a pin of 1 is equally unable to fail short of the suite
executing nothing, and satisfies AC4 and AC5 alike. The floor exists to red when arms become
unreachable; a pin far under the executed count is the could-not-fail shape charter §7 names, and
§5's risk line covers only the overshoot direction. Spec 19 AC1 carries the identical loose bound,
which explains the copy but does not make it observe the undershoot.

**The fix.** Pin the lower bound in AC4 as well: `FLOOR_ASSERTIONS` equals `c * 9 / 10` rounded
down, or is at least `c * 8 / 10`, with `c` derived by the same grep at observation. Fold the same
line into spec 19 AC1 at its next revision, since the two ACs are one shape.

**Left-shift.** `check-testsuite-counts.sh` already rejects `FLOOR_ASSERTIONS=0`; a second predicate
there, "the pin is at least half the file's static `same|has|hasnt_` count", gates the near-zero
pin for every suite on the manifest at once.

### M5 — medium — TOOL-21 §3 'No structural after-exit arm', §2 S4, against `TOOL-dUnstalledConvoy-19` and spec 19 S5 — raw 31

**The defect.** `TOOL-dUnstalledConvoy-19` (backlog `TOOL.md:68`, OPEN) records that appending to
a suite past its terminal `exit` strands the arms while every static signal says they are fine, and
that a numeric floor fixes the instance and not the class; the class fix it names is a one-grep
structural arm. Spec 19 rev-2's S5 writes that line for the adopter suite, and its revision log
records round-3 M11 folding it in because the spec "cited it and installed eight assertions of
slack without engaging it"; spec 19's non-goal defers only the kit-wide LOOP. Spec 21, authored at
the same disposal, cites `-19`, installs about 32 assertions of slack on a suite that ends
`exit $st` at `:1256` — the suite whose fifteen unexecuted fixtures are the unit's reason to exist
— and defers the per-suite one-liner to the loop's backlog row. An arm a later unit appends past
`:1256` is invisible to the floor's slack, to `check-arms.py`, and to the `--- $n arms` line.

**The fix.** Add spec 19 S5's self-read to S4 beside the floor, anchored on this suite's spelling:
`sed -n '/^exit \$st$/,$p' "$0" | grep -cvE '^\s*(#|$)'` prints exactly 1, else
`FAIL a line follows the terminal exit and can never run` with `st=1`; stage its failing case the
way S5 stages the floor's, by evaluating the extracted line over a copy with one line appended.
Keep the backlog hand-off for the suites the build does not touch.

**Left-shift.** The one-liner IS the left-shift; `-19` asked for it. The kit-wide loop spec 19
hands off is the class gate and stays a backlog row.

### M6 — medium — TOOL-23 §2 S1 population and S4, §4 header list, §3 and Edges population claim — raw 16

**The defect.** Re-read at source. S1's population is every `*.sh` beside the checker except the
checker itself, which includes `check-unattended.test.sh` and `unattended.test.sh`. S4 has the
former write `_x=$(printf '%s\n' "$_o" | wc -l)` into a suite copy, and the suite's own staging
idiom is a quoted heredoc (`check-unattended.test.sh:188`), which puts those exact bytes on a
non-comment line of `check-unattended.test.sh` — a line the `^[^#]*` predicate matches. The
fixture at `:65` copies the checker, the driver, the lib and the two templates and no suite, so
AC1's three scratch runs never see the self-hit; the close's `unattended kit gate` runs the checker
over the real `tools/unattended/` and reds on the suite while every AC is green. Only an escaped
spelling of the staged line avoids it, and nothing in the spec asks for one. The header's stated
exclusion ("the checker's own file is outside the population because its grep carries the pattern")
names the one self-reference and not the other.

**The fix.** S1 says the population deliberately INCLUDES `*.test.sh` — unlike `KIT_SH` at `:2729`
and spec 11's three named files — and excludes by name both the checker and
`check-unattended.test.sh`, with the header naming that second exclusion and why; or S4 states the
arm assembles the staged line from fragments so its own bytes never match, and AC1 adds a grep
proving the suite file is not a hit. Either way, drop "the population every check in that gate
reads" from §3 and the Edges (see M7).

**Left-shift.** AC1's fixture should copy `check-unattended.test.sh` beside the checker so the
scratch run sees what the close sees; a fixture that omits the file that carries the bytes is the
green-by-absence shape one level up. A gotcha row for "a ban's own arm carries the banned bytes"
belongs on the class record S5 writes.

### M7 — medium — TOOL-23 §3 'No scan outside the kit', §4 'Alternatives rejected' and 'Home the check in `check-arms.py`', §2 S1 and S5 — raw 35

**The defect.** Re-read at source. `check-unattended.sh:2728-2733` derives `KIT_SH` with
`case "$_f" in *.test.sh) continue ;; esac`, and that loop is the checker's ONLY `*.sh` glob, so no
existing check reads a suite and spec 23's `for _lc_f in "$HERE"/*.sh` would be the gate's first;
`TOOL-aDeferredBar-4` records the skip. Spec 11's check reads three named files and its §4 rejects
"scan every `.sh` in the kit dir" because the suites carry the literal in fixtures. So "the
population every check in that gate reads" (§3) and "unit 11's check already reads the same files"
(§4) are both false. Meanwhile two records already home a shell-idiom ban over every tracked
`*.sh`: `tools/gate-lint/sh_hygiene.py` (population `git ls-files -z '*.sh'` at `:205`, a CLASSES
table, comment stripping, a shrink-only registry, `--selftest` in both directions at `:7`, a
`subject = repo` leg), and the retired-launcher ban at `tools/lib/resolve-python.test.sh:113`
("in any tracked `*.sh`", comments stripped first). Neither is weighed in §4 or §10, whose "no seam
fits" rests on `reuse_lookup.py`, which prints `unscanned layers: .sh` and which this repo's own
memory note says is unfounded alone for a shell seam. A repo-wide class (charter §7, "gate the
CLASS … one level up") is gated over one kit's directory by a checker `kit.toml` ships to
adopters, on a population the gate's own comment refuses, with a gotcha anchored to two files so
`--for-diff` never names the class over `tools/workflows/unattended-build.test.sh` or any other
suite helper — which is where round 3's H3 instance would have been just as likely to appear.

**The fix.** Either home the predicate in `tools/gate-lint/` beside `sh_hygiene.py` as one more
CLASSES row over every tracked `*.sh` (zero hits, eight near-misses all in one kit, printed by its
selftest both ways) and anchor the gotcha to that scanner; or keep the kit home and rewrite §3 and
§4 to say the check derives its OWN population including `*.test.sh`, why that departs from
`KIT_SH`, and why gate-lint was not taken. The first is the smaller diff and the wider gate; the
spec should say which it chose and why.

**Left-shift.** `sh_hygiene.py`'s CLASSES table is the gate for the class; adding the row there is
the left-shift and the fix in one. If the kit home stays, the gotcha's anchors must include
`tools/gate-lint/sh_hygiene.py`'s population statement or the class is a one-kit rule with a
repo-wide name.

### L1 — low — TOOL-21 §4 'The floor block' placement, against §2 S4's cited shape — raw 17

**The defect.** S4 cites `tools/unattended/gate-guard.test.sh:455` as the shape; that sibling
runs its compare at `:455`, prints `---- passed/failed ----` at `:456` and `PASS` at `:457`, so the
compare comes BEFORE the summary. §4 places the block "after the `--- $n arms` line so a breach
prints beside the count it grades", and S4 says that line is unchanged; on a breach the suite
prints `--- N arms, exit 0` and then exits 1, so the summary misreports the exit status on the one
run the floor exists for, and §5's ledger-reading remedy sends a reader to a log that says
`exit 0`.

**The fix.** Insert the block directly above `echo "--- $n arms, exit $st"`, matching the
sibling; AC4's "on a line above the file's `exit $st`" holds unchanged. With H3's `PASS` line
added under the compare, the order becomes compare, summary, `PASS`, `exit`, which is the sibling's.

**Left-shift.** None beyond H3's; once the `PASS` line is gated by `check-testsuite-counts.sh`, a
summary line that lies about `$st` is visible in the same log as the `FAIL executed` sentence.

### L2 — low — TOOL-22 §2 S2, §4 pushed-control comment, §6 AC2 — raw 34

**The defect.** The ordering the pushed control accepts — a later landing that contains this one
after another push moved `origin main` — is the race `TOOL-aUnblockedFleet-7` records (run B
overwrites run A's marker). Spec 16 cites the id twice; spec 22 cites `spec 16 §4` three times and
the id never (grep count 0). The citation lands as a comment in `tools/unattended/unattended.test.sh`,
which `kit.toml` includes for every adopter and whose convention is full ids; charter §2 forbids
build-local shorthand where ids are the permanent record and §6 asks non-obvious rules to carry
the motivating id inline. A spec section is a pointer the next fold can move; the id is not.

**The fix.** Cite `TOOL-aUnblockedFleet-7` in S2 and in the arm's comment beside the spec 16 §4
pointer.

**Left-shift.** A grep over shipped `*.test.sh` for `spec [0-9]+ §` with zero hits expected is a
one-line arm in the install-prefix suite, since that suite already reads the shipped surface for
literals that do not travel.

## The cross-read on the four axes

Where two records disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-22 §4's `hit` literals against `check-arms.py`'s `signature()` and the
  gotcha that records the prefix shape (H1). TOOL-22 §4's `fixture` call against `fixture()`'s
  own definition and its 45 call sites (M1). TOOL-21 §4's floor block against the sibling it cites
  (L1) and the `compliant()` predicate that grades the population it joins (H3). TOOL-23 S1's
  population against `KIT_SH`, spec 11 rev-2 and the fixture at `:65` (M6, M7).
- **Ordering.** TOOL-22 AC3's "at this unit's base" against its own §4, §10 and Edges, and
  against the same phrase in AC4 where it is right (M2). TOOL-22's arms placed before the accepting
  arm that needs the state they consume (H2). TOOL-24 AC3 is the one criterion in the set that
  reads a predecessor's tip by commit subject rather than the base sha — the spelling M2's fix
  copies.
- **Scope.** TOOL-21 names four files and trips three meta-gates whose artifacts it never names
  (H3, H4, H5); the gotcha for that class exists and is not cited. TOOL-21 withholds the `-19` arm
  spec 19 S5 builds one unit earlier (M5). TOOL-23 scopes three spellings and stages one (H6), and
  scopes a repo-wide class to one kit with the repo-wide scanner unweighed (M7).
- **Acceptance.** Criteria that pass on the thing their S-item specifies: TOOL-21 AC1 on the
  ceiling (M3), AC4 on the pin (M4). A criterion aimed at a class that passes on it: TOOL-22 AC4
  on stranded arms (H1). A criterion with an unreachable half: TOOL-22 AC3 (M2). An existing arm
  no criterion watches while the new arms displace its state: spec 16 AC3's accepting arm (H2).

**Prior art the specs re-invent or misread.** `check-arms.py`'s docstring and the
`arm-literal-strands-on-message-edit` gotcha, both of which name H1's shape and its remedy.
`a-new-leg-trips-a-growing-set-of-meta-gates`, which names H3, H4 and H5 as one class. The suite's
own comment at `unattended.test.sh:4558-4559`, which names H2's hazard for the arm it precedes.
`TOOL-dUnstalledConvoy-19` and spec 19 S5 (M5). `sh_hygiene.py` and `resolve-python.test.sh:113`
(M7). `TOOL-aUnblockedFleet-7` (L2). Spec 24 AC3's tip-of-unit spelling (M2's fix).

**Harness and driver assumptions, and which were verified.** `signature()` and `classify()` were
re-read and `signature()` was RUN over spec 16's two sentences with the three `hit` literals
tested for containment (H1). `verb_landed`'s ordering (`refuse_if_terminal`, check 31,
`check_clean`, check 34) and the marker region at `:4536-4566` were re-read (H2, M1). `fixture()`
at `:363` was re-read; the clean-tree `git commit` behaviour is reported as the skeptic's, who
tested it in a scratch repo (M1). `check-testsuite-counts.sh:30-40,66-76,100-110`, the leg's
`guard`/`subject`/`chunk` in the manifest, and the waivers header were re-read (H3).
`map_extractors.py:72-93`, `test_codebase_map.py:93`, `review-harnesses.md:11-15` and both gotcha
files' existence were re-read (H4). `govkit.py:1690-1748` and `subject-pins.tsv`'s sibling rows
were re-read (H5). `selftest-budgets.txt:49,94,110,120` and the sibling ceilings, and
`derive-ceilings.py:287-317`, were re-read (M3). `gate-guard.test.sh:452-460` and
`unattended-build.test.sh:1250-1257` were re-read (L1, H3). `check-unattended.sh:2726-2735`,
`check-unattended.test.sh:60-70,186-190`, `sh_hygiene.py:7,88,205` and
`resolve-python.test.sh:111-115` were re-read (M6, M7). `git show 830c46e8:` greps for `fail 34`
and `carries no commit sha` were run (M2). The `-19` row and the `-7` citation counts were read
(M5, L2). Not re-run here and reported as the skeptic's: `check-arms.py --report` over the base
driver listing four check-34 branches (M2), the here-string branch's escaping (H6, an argument
about the regex's shape rather than a measurement), and `gotchas.py --for-diff` over
`tools/gate-legs.json` (H4's left-shift).

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture.** No arm was staged, no
  suite was run, no `--landed` was invoked, no kit gate was run. `signature()` is the one function
  that was executed, over two strings.
- **It was handed the confirmed set only.** The 14 refuted findings and their verdicts were not
  in the synthesis's inputs, so they were neither re-opened nor read; whether any of them named
  spec 24 is not known to this record, and spec 24's zero is a zero over the confirmed set.
- **A spec audit grades what a document says.** Whether the pass that builds spec 22 would notice
  H1 from AC3's red and reach for the gotcha on its own is a question for the build; the finding
  is that the design text says the opposite of what the tool does.
- **The units' §8 open questions are all `none` and were not re-adjudicated.** H1, H3, H4 and H5
  are each a question the spec could have asked and did not.
- **Precision was 0.61.** Above the floor and reported. The three pre-flights that would have
  removed eight of the fifteen defects before commissioning are each one loop over `spec/*.md`:
  run every "at this unit's base" against `git show <base>:<path>` (M2, the same class round 3
  named twice and this round repeats); for every spec adding a `*.test.sh` to the manifest, run
  `check-testsuite-counts.sh`'s `compliant()` over its §4 block and grep its Files touched for
  `subject-pins.tsv`, a dossier and `memory/map/generated` (H3, H4, H5); for every `hit "$out"
  "<literal>"` a §4 writes, assert the literal contains a `--report` row (H1). Round 2 over this
  set should re-audit the revised specs at their new blobs with one lens on H2 and M1 across spec
  22's whole marker region together with spec 16's accepting arm, since the two units share one
  fixture state and three of spec 22's five defects are that state spelled wrong.
