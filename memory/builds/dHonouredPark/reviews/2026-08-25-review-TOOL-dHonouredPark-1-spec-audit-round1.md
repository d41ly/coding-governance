**Serves:** spec-audit TOOL-dHonouredPark-1..4

# Spec audit round 1 — the four dHonouredPark specs

*Node d, 2026-08-25, base 60ba1d60. Four primed finder lenses over the whole spec set, then five
batched skeptics each prompted to REFUTE and to default to refuted under uncertainty. Concurrency and
verifier total both at the charter's cap.*

## Verdict: BLOCKED

67 raw findings. 67 graded. 39 CONFIRMED, 25 CORRECTED, 3 REFUTED. Strict precision (confirmed over
raised) 0.58; survival rate 0.96.

Surviving by final severity: 4 BLOCKER, 18 HIGH, 23 MEDIUM, 19 LOW. The four blocker verdicts are
TWO distinct defects, each independently reached by two lenses — which is the run's strongest
precision signal and the reason both are treated as settled rather than as candidates.

25 of the survivors were CORRECTED, meaning something real was there but the finding as raised was
wrong. The fold acts on the correction, never on the original claim.

| Spec | Findings |
|---|---|
| [TOOL-dHonouredPark-1](../spec/2026-08-25-spec-dHonouredPark-1.md) — mandatory roster pair | 22 |
| [TOOL-dHonouredPark-3](../spec/2026-08-25-spec-dHonouredPark-3.md) — waivers key on line text | 16 |
| [TOOL-dHonouredPark-4](../spec/2026-08-25-spec-dHonouredPark-4.md) — `--plan` reads the region | 15 |
| [TOOL-dHonouredPark-2](../spec/2026-08-25-spec-dHonouredPark-2.md) — build-method budget | 11 |
| CROSS | 3 |

## THE RUN'S OWN DEFECT, recorded because it changes how these numbers must be read

The first execution of this audit produced a verdict table that was **discarded as unusable**, and
the reason is a defect in the orchestration and not in any agent. Each of the four finder lenses
numbered its findings from `F1` independently, so 67 findings carried only 18 distinct ids. The join
that attached skeptic verdicts to findings therefore paired most of them with a verdict written about
a different subject: `F1` alone drew CONFIRMED BLOCKER, CORRECTED LOW, CONFIRMED HIGH and CORRECTED
HIGH, about four unrelated claims.

The five skeptic batches did not align to lens boundaries either, so the verdicts could not be
re-joined after the fact and were thrown away in full. The findings were re-keyed orchestrator-side
(`L<lens>F<n>`, globally unique by construction) and the verify stage re-run from scratch. The
figures above are from that second run.

`tools/workflows/tier2-review.js` — the harness this repo already ships — assigns finding ids in the
orchestrator for exactly this reason. `memory/guides/BUILD-METHOD.md` M4 rules it out for spec audits
because it reviews diffs, so a bespoke script was written and reintroduced the defect the shipped one
exists to prevent. That is a gap in M4, not a licence to ignore it: **the rule that a fan-out's ids
are assigned by the orchestrator is independent of what is being reviewed**, and M4 should say so.
Carried to the backlog.

## BLOCKER 1 — the driver could not read this build's own units

**`L1F2` · `L2F3` · CONFIRMED and CORRECTED · raised BLOCKER, final BLOCKER · FIXED in this pass**

`roster_ids` and `unit_ids_of` (`tools/unattended/unattended.sh:1487-1502`) both select ids with
`grep -oE "[A-Z]+-$slug-[0-9]+"` against the build's own FOLDER slug. This build's units were minted
under the PARENT build's slug at sequence 10 through 13 while the folder is `dHonouredPark`, so
both readers returned EMPTY.
Measured: `unit_ids_of dHonouredPark` matched 0 of the 4 ids actually present in the generated region,
and `--plan dHonouredPark` printed the no-roster branch.

The consequence reaches past unit 1. `build-complete` term 2 refuses on an empty id set
(`unattended.sh:2712`) **before term 3 is evaluated at all**, so this build could not have closed an
unattended run without `--override build-complete` — authorizing itself past the one item that means
the build is done.

A skeptic corrected the finding's scope usefully: unit 1's own arms run against fixture builds
(`readme tPlan` + `mkspec tPlan ARCH-tPlan-1`, `unattended.test.sh:1586-1600`) where slug and id agree
by construction, so AC3 and AC4 remain demonstrable. What was undemonstrable was **this build's own
closing**.

**Disposition — FIXED, not deferred.** A sweep of all 63 build folders comparing each folder name
against the id slugs in its tracked specs found exactly one mismatch: this build, created two local
commits earlier. The ids appeared in seven tracked files, none of them the append-only
`memory/DECISIONS.md`, and `git grep` at `origin/main` found none of them — nothing had left this
machine. The four were renamed onto this folder's own slug as `TOOL-dHonouredPark-1..4`, preserving numeric
order because ids are labels and not ranks, with build order left in each spec's `order` verb.

The retired ids are described rather than spelled, deliberately: `rosters()` reads an id mentioned
anywhere under `memory/` as a CLAIM on it, so writing the old spellings here re-attached one to the
parent build's front matter and reds hygiene check 14. The record states the sequence instead.

Verified after: `unit_ids_of` matches 4 of 4, `--plan` lists all four units, and the front matter
`ids:` line now carries four ids where it carried one.

That single-id front matter was a second symptom of the same cause. `rosters()` falls back to front
matter when a slug owns no ids (`gen_build_index.py:673`) and `apply_front_matter_ids` rewrites `ids:`
from that same value (`:1420`), so the line was self-perpetuating at one id for a four-unit build.

**The residue worth recording:** the ENGINE tolerates an id/folder slug split deliberately —
`gen_build_index.py:1398` carries the comment that a build folder "HOUSES" specs whose ids may belong
to another build — while the DRIVER does not. Two tools, two answers to one question. With the rename
landed, the engine's tolerance is now exercised by nothing in the corpus, which is its own smell.
Backlog, not this build.

## BLOCKER 2 — the read path has 60 bytes and this build spends them several times over

**`L3F1` · `L2F1` · CONFIRMED · raised BLOCKER, final BLOCKER · OPEN**

`python tools/memory-tree/corpus_ids.py --report` prints `read path : 6 files, 133673 B` against
`READ_PATH_CEILING="133733"` (`.memory-tree.conf:244`) with `READ_PATH_WAIVER=""`. That is **60 bytes
of headroom**, and `corpus_ids.py:450-457` is check 16, which hard-fails on breach.

Unit 2 edits `memory/guides/BUILD-METHOD.md`, a capped member at 24126 B. Its S2 adds a dated
owner-call clause and its S3 adds an unruled-gate clause. A skeptic priced a maximally terse edit at
roughly 60–85 B, so unit 2's AC5 — which demands check 16 green — fails probably rather than
certainly. §3 forbids the offsetting trim (the owner declined it), and no scope item in any of the
four specs raises the ceiling.

**This is a build-wide blocker, not unit 2's.** A skeptic established that `memory/DECISIONS.md` is
itself a capped read-path member at 18096 B, and `.memory-tree.conf`'s own header records the previous
raise as `+122` for ONE decision row. Four units each recording a ruling exhausts 60 bytes several
times over, independent of which guide file each unit edits. Both read-path findings priced only the
guides; nobody priced the decision log.

**Disposition — OPEN. The build cannot land until a spec says where the room comes from.** The
options are to raise `READ_PATH_CEILING` with the movement recorded as this build's scope, to set
`READ_PATH_WAIVER`, or to trim a capped member. This needs a ruling before the fold, because the
answer changes which unit carries the change and whether unit 2's ACs are satisfiable at all.

## The decision the audit surfaced — unit 1's gate binds 2 files, and the owner ruled 51

**`L1F1` · `L4F3` · `L3F2` · `L4F6` · CORRECTED and CONFIRMED · final HIGH · NEEDS AN OWNER RULING**

Unit 1's S1 binds the presence assertion to the set `memory/project/readme-contract.txt` marks BOUND.
That set is two rows. The migration in S3 gives a roster pair to 51 READMEs. So **the spec migrates 51
files and gates 2 of them**, and after the migration 60 of 62 pairs carry no assertion at all — a
later deletion silently restores term 3's vacuous pass on that build, which is the failure the unit
exists to remove.

The sharpest form of the finding is not the arithmetic. It is that the population was never ruled:

- The contract's own header declares its subject as *which build READMEs the heading canon and the
  slot budgets bind*. Rosters are not canon and not a slot budget.
- The organic-growth constraint the owner ruled governs the CONTRACT, not the roster pair.
- Owner ruling 2 says plainly that 51 build READMEs gain a pair and the gate needs a presence
  assertion.
- Non-goal 4 ("no requirement on EXEMPT READMEs") is the spec author's inference presented as a
  constraint. **Widening S1 therefore needs no override — it needs a decision.**

Two internal contradictions fall out of the same conflation and are fixed either way: §4 Migration's
stated reason for the two-commit split ("or it reds 51 files on its own commit") is impossible under
S1 as scoped, which can red 2; and neither BOUND README carries a pair today, so the base-pinned 51
omits a bound file.

## HIGH — the findings that change what gets built

### Unit 3 — the waiver registry is twice the size the spec describes

**`L2F8` · `L1F5` · `L3F6` · `L4F2` · CONFIRMED · final HIGH**

`tools/dead-path-waivers.txt` holds **8 data rows across 3 files** — two in `WIRE-INTO-PROJECT.md`,
two in `tools/memory-tree/check-memory-hygiene.sh` (including the `:554` row the parent build's park
entry names as the incident that earned this ruling), four in `check-memory-hygiene.test.sh`. This is
true at HEAD and identically at the spec's own pinned base.

§4 Inventory ("Four rows today, all naming `check-memory-hygiene.test.sh`"), §5 ("the population is
four rows") and AC6 ("the four existing rows") are therefore all written over half the real
population, and **AC6 would certify a half-migration green**. Not escalated to blocker because §4
Migration says every row is rewritten, which prevents the half-migrated file — but the DoD as written
does not.

### Unit 3 — the proposed staleness rule is strictly weaker than the one that ships

**`L4F5` · `L2F9` · `L3F7` · CONFIRMED · final HIGH**

`tools/check-dead-paths.sh:156` computes `stale_rows` as a set difference of `waived_rows` against the
git-DERIVED hit set, not against file contents. A row goes stale today when its needle leaves the
derivation. S2's proposed predicate — "a row whose text matches no line in that file" — is membership
in the file's text, which is weaker.

Measured consequence: `--needles` confirms `STATUS.md` is a live needle, so re-adding any tracked
`STATUS.md` today reds the four rows covering `check-memory-hygiene.sh:554` and
`.test.sh:1314/1319/1375`. Under S2 those rows stay green while waiving nothing. S2 promises to keep a
property it removes, and neither AC3 nor AC5 reaches the case.

### Unit 3 — the reuse audit's negative finding is false, and its predicate could not have found the answer

**`L4F4` · CONFIRMED · final HIGH**

§10 records that no checker in this tree matches a waiver by line text, evidenced by a grep over
`tools/*.sh`. `memory/project/unarmed-branches.txt` is `gate<TAB>check<TAB>ordinal<TAB>signature` —
shrink-only, stale on rewording, and its header records **the same insertion-above-a-pin failure** that
earned this unit's ruling. `check-arms.py`'s docstring explains the capture rule.

The stated predicate is a glob over `tools/*.sh` and the checker is a `.py` file, so it structurally
could not see its own answer. This is the vacuous-selector class, in a reuse audit rather than a gate.
The `ordinal` field is precisely the disambiguator S3 reinvents as a refusal.

### Unit 4 — the two verbs still disagree after the change

**`L4F7` · `L2F6` · `L3F11` · CONFIRMED · final HIGH**

`verb_plan` falls through to `next="$miss (MISSING - spec it first)"` (`unattended.sh:1614-1618`)
while `verb_status` takes `nonterminal_units | head -1` (`:2226-2227`). S3 deliberately preserves the
MISSING join. So on a build whose specced units are all terminal and whose roster names an unspecced
id, the verbs still name different units — S2's "the same unit by construction" is false, and AC1/AC2
partition builds by whether they carry order values, never reaching that state.

Separately: `verb_status` fails 10 at `:2210` without a run-state file, which AC1 and AC2 both need
and no spec mentions.

### Unit 1 — arms and scope items that are already green at BASE

**`L1F14` · `L4F15` · `L4F12` · CONFIRMED · final MEDIUM, listed here as a class**

Three of unit 1's requirements pass on an untouched tree. AC3 and §5's "the fourth arm must be
observed RED first" are already asserted by `unattended.test.sh:1586-1600` and the term-3 arm at
`:968-974`; the malformed half of AC3 is already refused with `fail 42` at `:1572-1576` and already
armed at `:1601-1611`; S5's report-by-id is already done at `:1614-1616` and `:2719-2720`.

Unit 2 has the same shape: its AC2 (312 lines against the new 350 ceiling, 24126 B against 24576) is
green at BASE and cannot fail, and `BUILD-METHOD.template.md` already carries S3's first clause
verbatim, so an implementer reading S3 as new work adds a duplicate sentence.

**This is the parent build's own recurring class arriving one level up: an acceptance criterion that
cannot fail.** The fold must either delete these or restate them as the delta they actually require.

### The gates named in §7 cannot run the arms the specs rely on

**`L2F7` · CORRECTED · final HIGH**

`tools/gate-legs.json` (85 legs) holds only `unattended kit gate`, `playbook validity gate` and
`unattended skill wiring` for this kit. `GATE_FULL=1 GATE_SELFTESTS=1` runs **neither spec's arms**,
and unit 4's AC6 requires an arm observed RED first that lives in `unattended.test.sh`, which no
command either spec names will run.

The prescribed fix is unavailable: a standing owner instruction of 2026-08-23 forbids running the
`tools/unattended/` self-test suites, and the kit's own header records that they were pulled off the
bar for costing 68% of it. The specs must name the compensating path or hand the owner one command,
not add `--selftests` to §7. A declared skip with a compensating check, per §7's own rule that an
exemption is not coverage.

## MEDIUM — the ones that change how a unit is built

- **`L2F12`** — `region()` exits 3 on duplicated markers (`unattended.sh:467-475`) while
  `_marker_index` returns the first match with no duplicate or order notion
  (`gen_build_index.py:965-970`). An assertion built on the slot leg — which unit 1's own §8 F1
  recommends — **accepts what the driver rejects**. Worse: `roster_ids` pipes `region | grep -oE` and
  takes grep's status, so exit 3 is discarded and the lines printed before the failure are parsed as
  ids. The driver's vocabulary already says "absent, duplicated or transposed" at `:1557`, 40 lines
  from unit 1's inconsistent "absent, unpaired, or inverted".
- **`L3F10`** — the owner's 310→350 line raise buys about **6 usable lines, not 40**. 439 B of byte
  headroom at a 77 B mean line makes the byte half binding at roughly line 318, and no AC says which
  half binds. The ruling does not buy what it appears to buy, and the owner should know that.
- **`L4F16`** — five tracked specs (`aDeployScout`, `aKitHardener`, `aLeanRework`, `aPortableWarden`,
  `aRatchetForge`) produce a `NOT A UNIT (no status header)` row today. `unit_rows` selects only
  `^\| \[.*\]\(spec/`, so moving `--plan`'s enumeration onto the region drops those diagnostics. Unit
  4's "otherwise identical" is false and nothing parks the loss.
- **`L1F8`** — same mechanism, stated as the loss of both `NOT A UNIT` branches at `:1592-1602`; §8 F1
  restores per-unit classification but not the walk that produces them.
- **`L4F14`** · **`L3F12`** — unit 4's §4 claims three readers of the units region after the change.
  There are more, `verb_plan` is **already** one of them (`:1572-1573`), and the driver's own comment
  at `:1864` calls `unit_rows` the third before this unit adds anything. S1 extends an existing read
  rather than adding one.
- **`L4F9`** — unit 2's §8 F1 carries `RESOLVED (owner, 2026-08-25)` while its own text says the
  question stays unruled. `plan_state`'s regex (`:1432`) reads that mark, so the stamp is load-bearing
  and flips the spec FORKED→READY.
- **`L4F10`** — unit 2's "offered as the recommendation and declined" is contradicted by both records
  it derives from: `RUN.md:37` lists three options with no recommendation recorded, and ruling 3 says
  of the gate that nobody has been asked.
- **`L2F10`** · **`L1F12`** — `check-dead-paths.sh:51` pins the grammar as matching
  `install-prefix-waivers.txt` exactly, a second documentation site unit 3's §5 never names. Non-goal 3
  makes that parity sentence **permanently false** rather than merely stale, and
  `dead-path-waivers.txt:15-18` documents a line-keyed re-stamp protocol S1 deletes.
- **`L2F11`** — `tools/govkit/registry.toml:191-192` exempts the waiver file with a reason naming "gov
  line numbers", which S1 makes false. §7 also omits `govkit selfcheck` (unguarded, runs every bar) and
  `dead-path carriers self-test` (guarded on `tools/`, which this unit's diff trips).
- **`L1F6`** · **`L4F18`** — unit 4's §1 says `--plan` sorts by id. `unattended.sh:1578` is
  `git ls-files` consumed with no sort: it is lexical PATH order, which only coincides with id order
  while dates and unpadded ordinals agree.
- **`L1F7`** · **`L2F4`** · **`L3F3`** · **`L2F16`** — unit 1's §4 states opposite commit orders in
  adjacent sentences, and repeats the impossible 51-file figure in §5's risks bullet.
- **`L1F10`** — the arms and `UNATTENDED-PROTOCOL.md:423` both describe `--plan`'s output, so "nothing
  downstream parses it" is overstated. The actionable gap is narrow: `unit_rows` never opens the link
  target, so the arms break only if S1 resolves a row to its spec by link rather than by id — and S1
  does not say which.
- **`L4F8`** · **`L2F15`** — unit 4 names a capped read-path member as possibly touched and never
  prices the charge, which this build's own rules slot requires. The edit can be byte-neutral; the
  missing measurement is the defect.
- **`L1F15`** · **`L2F17`** — the authored counts have already drifted since the specs' own base (62
  READMEs and 1 bound row at `60ba1d60`; 63 and 2 at HEAD, inflated by this build's own README). AC8's
  "over 62 READMEs" contradicts `do_check_format`'s own `len(tracked)` message at
  `gen_build_index.py:1553`, which will print 63. The remedy is to DERIVE these at run time, which is
  what AC8 should assert — §7's no-count-in-prose rule, broken by the specs that cite it.
- **`L3F5`** — unit 4's AC6 names `bash tools/unattended/check-unattended.sh` as the runner that
  observes its arm RED. That script never invokes `unattended.test.sh`. Unit 1 is NOT defective here:
  it names no test file and lists `build-index selftest`, a real leg.

## LOW — folded without discussion

`L3F13` (the `scan_canon` justification covers 2 of 63 while triggers 1 and 2 bind all of them) ·
`L3F9` and note (unit 1's §7 omits `check-arms.py`; separately `check-dead-paths.sh` is absent from
that checker's discovered population, so unit 3's §7 names a leg that cannot fire on its subject) ·
`L1F16` and `L2F14` (the template already ships S3's first clause; AC4 is a conjunction so it retains
a failing state) · `L1F13` and `L2F13` ("well inside the byte cap" describes a file at 98.2% of it) ·
`L1F11` and `L4F17` (no waived line carries a tab today, and the truncation case fails closed — but
S3's ambiguity refusal has **no legal remedy**: two identical hit-carrying lines in one file would red
permanently with no row able to waive them, and nothing says what an author does then) · `L2F18` (a
live trap on 1 of the 8 rows: `awk -v` expands `\n` sequences in the assignment, so a text comparison
that Python gets right, awk reports as a non-match — it fails RED, not green) · `L4F13`, `L3F8` and
`L2F5` (S4's rationale is false — an absent pair stays a vacuous pass on the exempt majority — but the
deletion it proposes is behaviourally inert, verified over all three want/have combinations) ·
`L1F17` (the `check-arms` hedge is legitimately conditional; AC7 is incomplete rather than wrong; the
three arms at `check-dead-paths.test.sh:109-125` all need rewriting) · `L4F12` (S5 is green at base).

## REFUTED — 3

- **`L1F4`** — S3's one-time seed is not non-goal 3's tautology. Non-goal 3 forbids a RENDERER; a
  frozen seed leaves the pair authorable, and S3 says so in its own text.
- **`L3F14`** — invents a requirement that a positive arm's staged break be the pre-migration checker.
  Nothing in §7 or the charter says that.
- **`L1F9`** — misreads §8 F1's "classification" as the status header. §4's data model says the region
  carries id, status and title; F1's carve-out is `plan_state`'s THIN/FORKED/READY, which the region
  genuinely lacks. A stale region is also not a landable state — `check-memory-hygiene.sh:599` reds on
  a differing render.

## Findings the skeptics raised that no finder reached

1. **Unit 3's §5 mischaracterises the largest part of its own diff.** "One string comparison per hit
   instead of one integer comparison" is wrong. `check-dead-paths.sh:133-152` parses rows with
   `awk '{print $1}'` — whitespace-split, which a TAB-delimited grammar breaks outright — and then
   computes `unwaived` and `stale_rows` as set differences via `grep -vxF -f` over `<path>:<line>`
   tokens. Text keying makes both sides two-field records, so the set-difference design has to be
   restructured, not have one comparison swapped.
2. **Unit 4's AC1 has no fixture.** `grep -n Order tools/unattended/unattended.test.sh` returns
   nothing; the `readme()` fixture renders a 4-column region while the live corpus renders 6. AC1
   quantifies over a build that does not exist in the harness and must be built. The column mismatch
   itself is harmless — both selectors are column-agnostic.
3. **`memory/DECISIONS.md` is a capped read-path member nobody priced.** See BLOCKER 2.
4. **Unit 1's "11 of 62" is correct and a naive grep says 13.** `aRuledFrontispiece` and
   `dFramedEntrypoint` name the marker in prose only; exactly 11 carry a well-formed pair. Any finding
   built on 13 would be wrong.
5. **Unit 3's `#`-collision worry in §4 is moot.** A row begins with the PATH, so a waived line's own
   leading `#` never lands at column 0. Two of the eight rows do point at `#` comment lines and neither
   collides with the "a line with no tab is a comment" rule.
6. **Unit 1's `aStandingWrit` claim is exact.** Running `roster_ids`' own pattern over all 11 existing
   pairs gives that build 0 ids. Two more pairs yield only 1 each (`aMeteredTurnstile`,
   `dSettledRoster`) — under-populated rather than inert, and unclaimed by the spec.
7. **`exempt-pin: 61` plus 2 bound equals 63 and is consistent.** The migration owes no pin movement.
   Worth stating in §4 so a builder does not helpfully adjust it.
8. **Unit 3's ambiguity risk is measurably nil today.** All eight rows re-keyed by line text match
   exactly one line each, and none contains a tab. A green starting state worth pinning rather than
   leaving unknown.

## What the fold owes

The build is BLOCKED on two things and neither is a spec wording fix.

1. BLOCKER 2 is open: no spec says where the 60 bytes come from, and four decision-log rows alone
   exceed them.
2. Unit 1's gate population was never ruled. The spec gates 2 files where the owner's ruling named 51,
   and non-goal 4 is an inference, not a constraint.

Everything else folds into rev-2 of the four specs.
