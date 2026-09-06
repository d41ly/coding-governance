**Serves:** diff-review TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

# Tier-2 closing diff review — the aHoistedPass build, the FOLD

*Adversarial pass over the fold itself, not over the build. The subject is round 1's seven fixes plus
the records they owed: does each fix do what its own commit message claims, is it complete, and did
it introduce a defect of its own. Node `a`, 2026-09-06, ROUND 2. Every finding below survived a
skeptic prompted to refute it; each carries its address, its fix, and the gate that would have caught
it before a reader had to.*

**Reviewed range:** `6b8026d310a55317425a1e9ea452bd64ce29656b...HEAD` — 27 files, +807/-85, four commits.

## Verdict: CLEAN WITH FIXES

All seven fixes are real and none is inert. The two round-1 BLOCKERs are closed at the mechanism and
not at the symptom: F1's importer allow-list is derived correctly, and F2's mode refusal is a closed
set rather than a truthiness assertion. Nothing here blocks the landing. What survives is one fix
that landed its new field on the only return where it can never carry information, one descriptor
left half-amended, one new hand-typed list joined to nothing, and three prose halves the amendments
did not follow through — the same class that produced three of round 1's seven findings, still the
most productive lens in this build.

**Review shape:** raw 15 · confirmed 10 · refuted 5 · unverified 0 · precision 0.67.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by the harness.
Nothing died, so a zero count in this report is evidence and not silence — the finding set is
complete as far as the four lenses reach.

**Consolidation, done here rather than by the harness.** The ten confirmed findings describe six
distinct defects: three lenses filed the F4 `standing` gap independently (ids 3, 7, 12), two filed
the check-31 header count (4, 14), and two filed the check-pass-order comment (6, 9). They are merged
below with their source ids named, so the confirmed count and the table reconcile without either
being restated wrongly.

**Severity as adjudicated here:** 0 BLOCKER · 0 HIGH · 3 MEDIUM · 3 LOW.

---

## What was verified clean

Stated because a fold review that reports only defects tells you nothing about the fixes it was
convened to grade.

- **F1's allow-list derivation is correct.** I re-derived the three populations mechanically rather
  than trusting the comment. The list is exactly (keys initialised above the import ∩ keys the
  shipped `.unattended.conf.example` declares) − `ADV_NAME` + `UNITS_REGION_CUTOFF`, twenty keys.
  Every other key the example declares — `GATE_BOUND`, `RECALL_CLI`, `ANCHOR_SCOPE`, `AUTH_PARAM`,
  `SPEC_THIN_CUTOFF`, `LANDER_MARKER`, `SHARED_RECORDS`, `GENERATED_INDEXES`, `PASS_ORDER_CUTOFF`,
  `BRIEF_RECORDED_CUTOFF`, `KEEPALIVE_INTERVAL` — appears zero times in `check-unattended.sh`, so no
  key was wrongly dropped. `ADV_NAME` is referenced five times and every one is a write or a read of
  the leg's own parse of the remote HEAD advertisement, so excluding it closes the hole rather than
  removing a feature. No key was wrongly kept. The specific hazard the brief asked about does not
  exist today; finding 3 below is about the day it starts to.
- **F3 is real and its comment now matches its loop.** `coresec` is built at :1519 inside the same
  registry parse that builds `core` and `corescope`, so there is no second spelling to drift. The
  body term at :1663 iterates `coresec` (CORE only) and arm B at :1622-1626 still iterates `core` (core
  plus a project's `DIRECTIVES_EXTRA`), which is the split the paragraph claims. The BACKTICK form
  and the block-wise HTML-comment strip both do what their comments say.
- **F2's refusal is a closed set and deliberately not `check()`.** `unattended-unit.js:89` compares
  against the two literals and refuses anything else by name. A typo can no longer select the
  unattended text, which is the exact failure `check()`'s truthiness assertion would have passed.
- **F5 is complete in both halves.** `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md` lost byte-identical six-line blocks, and the gate's
  identity now sits in the comment block above the `memory/guides/BUILD-METHOD.md 27648` row in
  `tools/template-size-limits.txt`, together with what the leg does not cover. Nothing was dropped
  without a home.
- **F6's runtime half works.** `adopt-unattended.sh:116` derives `TOOL_ROOT` the way
  `adopt-memory-tree.sh` does, :241 substitutes it, and `SKILL.template.md` carries the token twice.
  Finding 2 below is about the descriptor, not the render.
- **The records the fold owed are present.** `memory/project/method-carriers.txt` declares both new
  carriers with a `why` each; the kickoff manifest re-stamp landed; the closing review record carries
  check 5's filename grammar.

**One observation, not a finding.** `memory/guides/SESSION-KICKOFF.md` is 25579 bytes against a
25600-byte cap — 21 bytes of headroom. The next §B fact will require another trim, and the trim in
this range already spent a dated correction to buy the one it added. Worth knowing before someone
discovers it mid-landing.

---

## Findings

| # | Sev | Where | What |
|---|-----|-------|------|
| 1 | MEDIUM | `tools/workflows/unattended-build.js:757, :844, :889` | F4's `standing` key is on the one return where it is provably empty and absent from the two where it is not |
| 2 | MEDIUM | `tools/unattended/kit.toml:17, :46-48` | F6 left the descriptor half-amended: `TOOL_ROOT` undeclared, and the recorded reason it cannot be declared is now false |
| 3 | MEDIUM | `tools/unattended/check-unattended.sh:174-177` | F1's allow-list is a fourth hand-typed spelling of the conf key set, joined to nothing |
| 4 | LOW | `tools/unattended/check-pass-order.sh:101`, `check-unattended.sh:162` | F1's other half: the sibling importer still documents the open glob as safe, and the new comment misattributes its own precedent |
| 5 | LOW | `tools/unattended/check-unattended.sh:3004`, `check-unattended.test.sh:1663` | F6 added two announced skips and two test arms without moving either typed count |
| 6 | LOW | `memory/guides/SESSION-KICKOFF.md:78` | the new §B bullet front-loads a hard count of a set the driver owns, and names the wrong arm |

---

### 1 — MEDIUM — F4's `standing` reaches the return where it cannot carry information

**Where:** `tools/workflows/unattended-build.js:889` (added), `:757-765` (DEGRADED, missing),
`:844-857` (attended all-terminal, missing).
**Merged from lens findings 3, 7 and 12**, filed independently by three lenses.

F4 hoisted `stood` out of the disposal stage with the comment *"so the hand-out can report it"* and
added `standing: stood` to the terminal hand-out. The guard at :752 returns whenever `stood.length`
is non-zero, so by the time the hand-out is reached `stood` is provably `[]` — the added field's own
comment concedes this. The DEGRADED return at :757 is the sole path on which `stood` is non-empty,
and it carries no `standing` key at all. The attended all-terminal return at :844 is also
post-disposal and omits it.

The field was therefore added exactly where it can never say anything and omitted exactly where it
carries the payload. The comment at :885-889 states the rule the other two returns break: a missing
key *"is indistinguishable from a disposal stage that never ran"*. A caller applying that stated rule
reads `undefined` on the one path where blockers actually stood and concludes disposal never ran —
the inverted reading the key was added to prevent. The blocker ids survive only inside the English
`note` string, so a machine consumer must parse them back out of prose.

This is the "a fix that cannot fail" shape, and it is worth naming as such: `standing: stood` at :889
is an assertion that can only ever emit `[]`, and the existing test arm at
`unattended-build.test.sh:600` asserts exactly `'"standing":[]'`, so the arm passes on a fixture that
could not have produced anything else.

Impact is bounded today. No in-repo consumer reads the key, and `roster: []` still stops a caller on
both omitting paths. The file's own convention is the argument: `roster` carries the comment *"EVERY
NON-THROWING EXIT CARRIES `roster`"* (added after a caller threw on `undefined.length`) and
`skippedTerminal` follows it too; both are present on all four non-throwing returns and `standing` is
present on one.

**Fix.** Add `standing: stood,` to the DEGRADED return at :760 and to the attended all-terminal
return at :847 — `stood` is in scope at both. Add `standing: []` to the pre-disposal CONVERGING
return at :690 if the every-exit invariant is wanted in full; that one is defensible as key-less
since disposal has not run, so it is a judgement call and the other two are not.

**Left-shift gate.** The fixture already exists: `unattended-build.test.sh:587` builds the
disposed-true-with-standing run and asserts roster, note, blocker name and the absent done-log. One
line on the same `$o` covers the payload path —
`has "F4 the DEGRADED return names what stood" "$o" '"standing":["b1"]'` — and one on the
all-terminal run at :540. The durable version is one arm per non-throwing return asserting the key's
presence, which is the shape that would also have caught the original `roster` defect this file
records.

---

### 2 — MEDIUM — F6 left `kit.toml` half-amended, and the surviving rationale is now false

**Where:** `tools/unattended/kit.toml:17` (the declaration), `:46-48` (the recorded reason).
**Lens finding 11.**

The same commit that taught `adopt-unattended.sh` to derive and substitute `{{TOOL_ROOT}}` left the
descriptor declaring the old eight-token set for `SKILL.template.md`, and left the comment that says
this adopter cannot compute `TOOL_ROOT`:

> `TOOL_ROOT` is computed only by the memory-tree adopter; this kit's adopter never computes it, so
> declaring it here would ship an unresolved brace to every adopter.

That is the instruction the next author reads before touching this rule, and it now describes code
that no longer exists. `python tools/check-kit-placeholders.py --list` prints for this kit:
`substituted but undeclared (reported, never gated): K, TOOL_ROOT`. The reverse direction is ungated
by ratified design (that checker's own F2), so nothing reds and the declared population is provably
under-stated — in a repo whose §7 rule is that tooling is a DECLARED population asserted against the
tracked surface in both directions.

`K` in that same line is noise, not a second instance: it comes from a comment at
`adopt-unattended.sh:230` illustrating substitution semantics with `{{K}}`. It matters only because
it constrains the gate suggested below.

The fixture rule's conclusion (`KIT_DIR` alone) is still correct — all five spellings sit under the
kit directory — so the declaration there is not wrong. The defect is the stale premise plus the
under-declared SKILL row.

**Fix.** Add `"TOOL_ROOT"` to the `placeholders` array at :17. Verified safe: the checker greps the
adopter text for the literal `{{TOOL_ROOT}}`, which :241 now carries, so the
declared-subset-of-substituted join stays green. Then rewrite :46-48 so the ONE-token justification
for the fixture stands on its own ground and drop the clause about this adopter never computing
`TOOL_ROOT`.

**Left-shift gate.** The full reverse direction was ratified out, but a narrower join would have
caught this and would not red on `K`: for each `[[files]]` rule with a non-empty `placeholders` list,
red when the adopter substitutes a `{{TOKEN}}` that the rule's own template file actually contains
and the rule does not declare. `TOOL_ROOT` appears in `SKILL.template.md`; `K` appears in no template
at all, only in an adopter comment. Template-side scoping is what separates them.

---

### 3 — MEDIUM — F1's allow-list is a fourth hand-typed spelling, joined to nothing

**Where:** `tools/unattended/check-unattended.sh:174-177`.
**Lens finding 13.**

F1 replaced the open `[A-Z][A-Z0-9_]*` arm with a `case` allow-list carrying no catch-all, which is
the right shape and closes the blocker. The list is now the fourth hand-typed spelling of this leg's
conf key set — beside the initialiser block at :116-119, the shipped `.unattended.conf.example`, and
PROTOCOL section 8's table — and it is the only one of the four that nothing joins. Check 22 joins
the example against the protocol table in both directions and the project conf in one; it never reads
this `case`, and neither does any test in `check-unattended.test.sh`, `unattended.test.sh` or
`cross-component.test.sh`.

A key added to the initialiser, the example and the table but forgotten here is dropped silently and
keeps its default, with every gate green. That is the same silent-drift class the F3 fix in this very
diff removed by splitting `coresec` from the shared parse — its comment says so in as many words:
*"no second spelling of the handle set exists to drift — which is the class this whole build is
about."*

No live instance exists today; see "verified clean" above, where I re-derived all three populations
and they agree exactly. The blast radius on the next key addition does reach this repo and not only
adopters: `KICKOFF_ENGINE`, `KICKOFF_EXITS`, `LANDED_ANCHOR_CUTOFF`, `DISPOSITION_CUTOFF` and
`UNITS_REGION_CUTOFF` are all non-blank in gov's own `.unattended.conf`, and an emptied
`LANDED_ANCHOR_CUTOFF` is the "grandfather every anchor" state this file's own sentinel comment names
as a reproduced round-9 defect.

**Fix.** Keep the closed literal list — deriving it from the conf at runtime would reopen the hole.
Add the join instead.

**Left-shift gate.** The join is the gate: after the import, red when a key declared in
`$HERE/.unattended.conf.example` is one this leg initialises but the `case` does not name. That
derives the intersection the comment at :165 asserts rather than asking a reader to trust it, and it
reds on the commit that adds the fifth spelling instead of on the run that silently defaults.

---

### 4 — LOW — F1's other half: the sibling importer still documents the open glob as safe

**Where:** `tools/unattended/check-pass-order.sh:101`, and `tools/unattended/check-unattended.sh:162`.
**Merged from lens findings 6 and 9.**

`check-pass-order.sh:100-103` still reads, in the present tense:

> The sibling assigns EVERY uppercase key it sees, which is safe THERE because that script sets
> nothing it cares about above the import.

Both halves are false. The sibling it names is `check-unattended.sh`, which now carries the twenty-key
allow-list at :174-177 — so the first clause describes deleted code. And that script sets `HERE` at
:68, `DRIVER` at :69, `CONF` at :70 and `SCOPE` at :84, all above the import at :147 — so the second
clause was never true, and `check-unattended.sh:154-165` now records two exploits reproduced through
exactly that gap. This is the one place left in the kit telling a maintainer the open glob was fine
somewhere, which is the reasoning that produced the hole. `check-brief-recorded.sh:102-108` got the
treatment right and uses the past tense; it needs no change.

Second half, same amendment: `check-unattended.sh:161-163` claims *"the comment above the latter's
list names THIS leg's hole as its reason"*. `check-brief-recorded.sh:102-108` in fact describes a
sibling that *"sets `DRIVER` above its import - the path it eval's a classifier out of"*, which is
`check-pass-order.sh` (its `eval` of the sliced plan state at :135). `check-unattended.sh` evals
nothing but its own import assignment and required-key read, so that comment names pass-order's
incident, not this leg's.

**Fix.** Rewrite `check-pass-order.sh:100-103` to say the sibling carried the same open glob and had
to stop for the same reason — naming its `HERE`/`DRIVER`/`CONF`/`SCOPE` — and that both legs now
carry their own declared key list. Correct the attribution at `check-unattended.sh:162` to name
check-pass-order rather than "the latter".

**Left-shift gate.** Not gateable as prose, so it belongs in §10's checklist for this repo, phrased as
the class rather than the instance: *when a defect is fixed in one member of a copied block, grep the
other members for prose asserting the old behaviour is safe.* Three of round 1's seven findings and
three of this round's six are that class; it has earned a checklist row.

---

### 5 — LOW — check 31's header and its test both carry a count F6 moved

**Where:** `tools/unattended/check-unattended.sh:3004`, `tools/unattended/check-unattended.test.sh:1663`.
**Merged from lens findings 4 and 14.**

The header still reads *"FIVE ANNOUNCED SKIPS, one per case this check cannot COMPARE"*. F6 added the
absent-Skill skip and the Skill-names-no-route skip, so there are now seven report sites: :3045,
:3060, :3064, :3070, :3072, :3074, :3082. The header makes that enumeration load-bearing — *"The
announcement is therefore this check's liveness assertion and no separate vacuity branch is owed"* —
so a reader auditing what this check can and cannot reach is handed a figure two short by the same
commit that added the two. The test half holds the same defect from the other side:
`check-unattended.test.sh:1663` says *"SIX breaks and one green control, one per branch of the
check"* while the block now runs ten arms. The count was noticed on the test side — a nearby comment
was reworded from "the six above" to "the announcing ones" — and missed on the source side.

A typed count of a derived population beside the thing it counts is banned by name in `AGENTS.md` §7.

**Fix.** Drop the numeral from both. `:3004` becomes "ONE ANNOUNCED SKIP PER CASE this check cannot
COMPARE, each naming its OWN subject"; `:1663` becomes "ONE BREAK PER BRANCH plus a green control".
The branches are then the count, which is how this same file's own header already handles the check
total.

**Left-shift gate.** A cheap and general one: a leg over `tools/unattended/*.sh` and `*.test.sh` that
reds when a comment contains an English cardinal immediately followed by a countable noun the file
itself enumerates. That is a fuzzy predicate and would need its near-misses printed before wiring,
per §7. The narrow version that certainly pays: for `check 31` specifically, assert that the number
of `report "check 31 skipped` sites equals the numeral in its header — a one-line `grep -c` join,
and the header stops being able to lie.

---

### 6 — LOW — the new §B bullet front-loads a count the driver owns, and names the wrong arm

**Where:** `memory/guides/SESSION-KICKOFF.md:78`.
**Lens finding 15.**

The added bullet reads *"All seventeen core handles are anchored in the sections they cite and check
16 arm B reads the BODY, not just existence."* It is correct on the count today —
`DIRECTIVES_CORE` at `tools/unattended/unattended.sh:473` holds exactly seventeen — and it is a hard
count of a set the driver owns, typed into a front-loaded document. Nothing grades the document's
arithmetic: `manifest-check.sh` ratchets freshness stamps and never reads a body claim. Check 16 does
force a `DIRECTIVES_FLOOR` bump when the core count moves, so an eighteenth handle reds the conf —
but that reds the conf, not this sentence, and the sentence goes stale silently. The bullet's own
closing clause is the argument against it: *"M6 owns it and check 31 grades it — do not restate it
here."*

The same commit deleted three prose counts from this same file and replaced them with pointers, so
the diff carries its own standard and this line is on the wrong side of it.

**Noted during synthesis, not skeptic-verified:** the second clause is also wrong about which arm.
`check-unattended.sh:1622` labels arm B "every cited section RESOLVES" and the body term at :1663 is
a separate term whose own comment says *"Arm B above asserts the cited section EXISTS and never opens
it"*. Arm B is precisely the arm that does not read the body. Both halves of the sentence are fixed
by the same edit, which is why it is recorded here rather than filed separately.

**Fix.** Replace the sentence with: *"Every core handle is anchored in the section it cites, and
check 16's body term grades that rather than mere existence."* The bullet loses nothing a session
needs and stops carrying a figure only the driver can be right about.

**Left-shift gate.** The manifest is already ratcheted; extend it rather than adding a leg. A C-check
in `manifest-check.sh` that reds when a §B bullet contains an English cardinal is over-broad, so the
targeted form: red when the manifest names a count of a set the kit declares as a constant — today
`DIRECTIVES_CORE`, `DOD_NO_OVERRIDE`, `AUTH_MODES` — by joining the numeral against the constant's
member count. One join, three constants, and the class stops recurring in the one document every
session front-loads.

---

## What this review did not run

- The merge bar was not run as part of this review. The findings above are read-level and none of
  them changes a gate verdict, but no green is claimed here.
- The four lenses covered the fold's diff and the files it touches. Files outside
  `6b8026d3...HEAD` were read only where a fix's other half lives — `check-pass-order.sh`,
  `check-brief-recorded.sh`, `kit.toml`, `template-size-limits.txt`, `unattended.sh` — and were not
  themselves reviewed.
- Round 1's findings were taken as `fixed in this range` per the brief and re-graded rather than
  re-derived. The two BLOCKERs were re-read at source; the five others were graded from their diffs.
