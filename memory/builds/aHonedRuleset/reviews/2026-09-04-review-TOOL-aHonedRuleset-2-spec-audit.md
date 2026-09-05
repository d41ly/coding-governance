**Serves:** spec-audit TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6

# aHonedRuleset — spec audit of units 2–6, round 1

*Node `a`, 2026-09-04. Three auditors read the set on separate axes — scope boundaries, interfaces
and ordering, acceptance criteria — and this is the consolidation. Every claim any auditor made about
source was re-run here before it was kept; five did not survive and are named at the bottom with the
reason. Base `102e98f0`.*

Subjects, pinned at the blob each was read at:

- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-2.md@adc92d75044e9e3faed390973e0e8c3ac60464e0`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md@32783414140d3004c0513d19fc1b7ffed375a8d5`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md@6c314a1adaf5ace75a18b9397f265c8a28360b7d`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md@1f6b5ddbdd555dda64ba3b6f0433c2ae1a35f258`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-6.md@e2393c8832b1c3fad5e3fc956749cbb7f1f5afbb`

## Verdict: BLOCKED

Twenty-three findings survived verification, five were dropped. Three of the survivors block a
landing outright, and one of those is not in a spec at all: **the build README reds `memory hygiene`
check 9 on the tree as it stands today**, so no unit in this set can reach a green bar until it is
fixed.

Two owner forks are unsigned and gate executable scope: `TOOL-aHonedRuleset-6` §8 F1 (four of its
eight criteria are unsatisfiable until it is ruled) and the high-water row that units 3 and 5 both
claim.

---

## Blockers

### B1 — the build README reds `memory hygiene` today, before any unit is built

**`memory/builds/aHonedRuleset/README.md`**, front matter and the `roster:units` region.

Run at base, `python tools/memory-tree/gen_build_index.py --check` reports:

```
build-index: memory/builds/aHonedRuleset/README.md: front matter declares 'status: INPROGRESS'
but 5 spec(s) carry a status header — the build status is DERIVED from them … Delete the 'status:' key.
```

That invocation is `tools/memory-tree/check-memory-hygiene.sh:740`, wrapped as `fail 9`, and
`memory hygiene` is an unguarded `subject: repo` leg. So this is a live red, not a projection. With
the key removed the same command then reports three files stale against a fresh render —
`memory/LIVE.md`, this README, and `memory/ledger/2026-09.md` — verified by deleting the key,
re-running, and restoring the file.

Separately and NOT machine-caught: `ids:` names only `TOOL-aHonedRuleset-1` and the authored
`<!-- roster:units -->` table holds one row, while five specs exist. That region is never rendered
into (`gen_build_index.py:57-66` states the rule and the reason), and it is what the unattended
driver's `roster_ids` reads to answer which units are PLANNED but unspecced. A one-row roster makes
that answer wrong.

**Fix, in the README only:** delete the `status:` key, extend `ids:` to `TOOL-aHonedRuleset-1..6`,
add the five roster rows, then run `python tools/memory-tree/gen_build_index.py --write` in the same
commit. Nothing in any spec changes.

### B2 — `TOOL-aHonedRuleset-4` AC8 forbids the commit the pre-commit hook requires

**`…-4.md` §6 AC8.** It requires `git diff --stat` on the landing commit to show "exactly two files
… `coding-governance-agents.template.md` and `AGENTS.md`".

`memory/guides/SESSION-KICKOFF.md:6` lists `coding-governance-agents.template.md` as a `watch:`
pathspec — the line continues past `.memory-tree.conf` and carries four more specs than a short read
suggests. `.githooks/pre-commit:53-55` runs `manifest-check.sh --staged` unconditionally, and its
staged arm (`skills/session-kickoff/manifest-check.sh:412-421`) fails check 5 whenever
`git diff --cached --name-only -- "${WATCH[@]}"` is non-empty and the staged manifest's block stamp
equals HEAD's. The unit therefore owes a third file, and AC8 says it may not have one.

**Fix, in unit 4:** AC8 names three files — the two carriers plus
`memory/guides/SESSION-KICKOFF.md` — and a scope item adds the bundled `last-audit` re-stamp, copying
unit 5's S8. `tools/hooks/README.md` stays the excluded file the criterion is really about.

### B3 — `TOOL-aHonedRuleset-6`'s executable scope is gated on an unsigned fork, and four of its eight criteria assume one branch

**`…-6.md` §6 AC1–AC4, against §2 and §8 F1.** §2 opens "The executable scope is selected by the §8
F1 ruling"; F1 is marked UNRESOLVED and the spec explicitly does not sign it. Under option (b) there
is no limits row, no leg, no seeded high-water and no subject pin, so AC1, AC2, AC3 and AC4 are
unsatisfiable. Only AC8 carries an option-(b) clause.

**Fix, in unit 6:** mark AC1–AC4 as option-(a)-only and give each an option-(b) counterpart, the way
AC8 already handles both branches. This does not sign F1 — it makes the spec buildable in whichever
direction the owner rules.

---

## Scope and ordering defects

### S1 — three units stage a watched pathspec with no re-stamp in scope

Verified against `memory/guides/SESSION-KICKOFF.md:6`, whose full watch list is
`tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates/run-gates.sh;
tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf;
coding-governance-agents.template.md; skills/session-kickoff/SKILL.md; .unattended.conf;
memory/guides/BUILD-METHOD.md`.

| unit | watched file it stages | what is missing |
|---|---|---|
| 2 | `coding-governance-agents.template.md` | no scope item, no files-touched row, no `kickoff-manifest ratchet` in §7 |
| 3 | `SKILL.md`, `.unattended.conf`, `memory/guides/BUILD-METHOD.md` | §7 names the leg; §2 has no scope item and §4 no files-touched row |
| 6 | `tools/gate-legs.json`, `memory/guides/BUILD-METHOD.md` | no scope item, no files-touched row, no leg in §7 |

Unit 4 is B2 above. Unit 5 is the correct side and needs no change: S8 names the mechanism and both
its files are genuinely on the list.

**Fix, one per spec:** add a scope item copying unit 5's S8 — a `memory/guides/SESSION-KICKOFF.md`
`last-audit` re-stamp bundled into the same commit — plus the `kickoff-manifest ratchet` leg in §7
for units 2 and 6, and a files-touched row in all three.

### S2 — `TOOL-aHonedRuleset-3` S6 executes a decision unit 5 declares an unresolved owner call

**`…-3.md` §2 S6 and §6 AC11.** S6 runs `check-template-size.sh --bump skills/session-kickoff/SKILL.md`
with no fork. Unit 5 §8 F1 asks whether that same row moves down, recommends yes, and closes "It is a
merge-bar knob either way, so the owner rules." Both target `tools/template-size-highwater.txt:3`
(`skills/session-kickoff/SKILL.md	18215`, verified).

Unit 3 is the defective side on three verified grounds. Two siblings state the opposite rule with a
reason — unit 2 §3 ("Bumping would record the growth this build exists to reverse") and unit 4 §3
("The gate's `--bump` records intended GROWTH, and a shrink owes it nothing"). A region a sibling
declares an owner call may not sit in another unit's IN scope. And S6 buys nothing for AC11's second
clause: `tools/check-template-size.sh:183` WARNs only when `bytes > recorded`, and unit 3's own cut
takes the file from 18225 to roughly 16988, already below 18215.

There is a fourth reason the auditors did not raise. Unit 3 is `order 1` and unit 5 `order 2`, and
both edit that same file — a bump taken at order 1 records a figure order 2 immediately supersedes.

**Fix, in unit 3:** delete S6 from §2, drop AC11's first clause, and leave the row to unit 5 F1 as
the single owner decision.

### S3 — `TOOL-aHonedRuleset-3` §3 routes a question its own sibling carries

**`…-3.md` §3**, the bullet reading "`BUILD-METHOD`'s ungated prose budget is not converted to a
registry row — the build README parks that as an owner decision."

The README park is real, but the disposition has moved: `TOOL-aHonedRuleset-6` is that question, in
this same set. The cost is not cosmetic — unit 3 §8 F2 forks on `BUILD-METHOD.template.md` having 12
free bytes (verified: 24564 of a self-declared 24576) and unit 6 frees roughly 950 B (option a) or
1101 B (option b) from lines 8–18 of that file, disjoint from unit 3's lines 60 and 274.

**Fix, in unit 3:** the §3 bullet and §8 F2 name `TOOL-aHonedRuleset-6` as the carrier, and F2 states
that landing 6 first makes the fork moot.

---

## Acceptance criteria that cannot fail, or cannot pass

### A1 — `TOOL-aHonedRuleset-2` AC3 names a token that matches nothing

**`…-2.md` §6 AC3.** It asserts `grep -n 'pinned as STRUCTURE'` "returns exactly one hit" in both
carriers. Measured: `grep -c 'pinned as STRUCTURE'` returns **0** in
`coding-governance-agents.template.md` and in `AGENTS.md`, because the phrase straddles a wrap —
template line 369 ends `…Five glyphs are pinned as` and 370 begins `STRUCTURE:`. The criterion fails
before the unit is built, and would turn green only if S3's re-wrap happened to join those two words,
so it grades the wrap rather than G9's survival.

**Fix:** use `grep -c 'Five glyphs are pinned'`, which returns exactly 1 today in each carrier and
cannot straddle the wrap.

### A2 — `TOOL-aHonedRuleset-5` AC2 is satisfied by unit 3 alone

**`…-5.md` §6 AC2.** It asks for "at least 300 bytes under 18432" and no `TEMPLATE-SIZE WARN`
"because the file has fallen back below its recorded high-water of 18215". Unit 3 is `order 1`, edits
the same `skills/session-kickoff/SKILL.md`, and recovers roughly 1237 B. After it the file sits about
1444 B under 18432 and below 18215, so both clauses hold and unit 5's own 97 B is never observed.
This spec never mentions unit 3.

**Fix, in unit 5:** express AC2 as a delta against the measurement taken immediately before this unit
— "at least 90 bytes smaller than the pre-unit `wc -c`" — rather than as an absolute against a base
figure a predecessor moves.

### A3 — `TOOL-aHonedRuleset-6` AC2's staged break cannot go red on the landed tree

**`…-6.md` §6 AC2.** Base is 24564 of 24576, so appending 13 B reds `TEMPLATE-SIZE check 2 FAILED`.
But S5 relocates roughly 950 B out of that same file in the same unit, leaving it near 23614 — a
13-byte append then sits about 950 B under the ceiling and the new leg stays GREEN. §7 binds the
staged-break rule to AC2, so as written the new gate's failing case is never observed, which is the
"a gate you have only ever seen pass" class this repo already names.

**Fix, in unit 6:** size the append from the post-S5 free space — measure `wc -c` after S5 and append
`24576 − measured + 1`.

### A4 — `TOOL-aHonedRuleset-3` AC8 is unsatisfiable on one branch of its own fork

**`…-3.md` §6 AC8**, against §8 F2. AC8 requires
`grep -rn 'Step 5b exit' tools/ memory/guides/ .claude/` to return nothing outside `memory/builds/`
and `memory/archive/`. F2's own recommended fallback leaves `tools/memory-tree/BUILD-METHOD.template.md:60`
and its render `memory/guides/BUILD-METHOD.md:60` forwarding through Step 5b — verified, both lines
carry the literal `Step 5b exit 5`, and both sit inside AC8's search scope. The acceptance set is
satisfiable only on the branch F2 does not recommend.

**Fix, in unit 3:** condition AC8 on the F2 ruling, as unit 6's AC8 already does for its own fork.

### A5 — `TOOL-aHonedRuleset-3` AC8's pattern never reaches one of S5's three targets

**`…-3.md` §6 AC8.** S5 names three cross-references; `BUILD-METHOD.template.md:274` reads
`Step 5b says which one per exit`, which the pattern `Step 5b exit` does not match. Verified: a
`grep -rn 'Step 5b'` over the same scope returns :274 and its render, while `grep -rn 'Step 5b exit'`
does not. Line 274 can be left untouched with AC8 green.

**Fix, in unit 3:** add a second criterion keyed on line 274's own words, `grep -rn 'Step 5b says
which one per exit'` returning nothing outside `memory/builds/` and `memory/archive/`.

### A6 — `TOOL-aHonedRuleset-3` S2 has no criterion at all

**`…-3.md` §6.** Nothing observes that the pointer replacing engine lines 223–241 exists or names
`<MEMORY_ROOT>/guides/UNATTENDED-PROTOCOL.md` §13. A build that deletes the block outright and leaves
no pointer passes AC1 (engine count 0), AC2 (1467 B freed against a 1200 B floor), and AC3–AC11
unchanged.

**Fix, in unit 3:** add a criterion that the engine's Step 5b region still names
`UNATTENDED-PROTOCOL.md`.

### A7 — `TOOL-aHonedRuleset-3` S3's prose half has no criterion the gate can carry

**`…-3.md` §6 AC4.** AC4 leans on check 22, whose header states verbatim at
`tools/unattended/check-unattended.sh:1379-1381`: "It grades presence of the key name in the table
region, nothing more. A row whose prose is wrong is green here". So the false sentence at
`tools/unattended/.unattended.conf.example:78` — "MEASURE it against your own engine, because the
count is a property of that document and not of this kit" — survives the unit untouched with every AC
green, and §4 calls that sentence the sharper half of the change.

**Fix, in unit 3:** add `grep -c 'MEASURE it against your own engine' tools/unattended/.unattended.conf.example`
returning 0.

### A8 — `TOOL-aHonedRuleset-2` §7 names a constraint that cannot bind

**`…-2.md` §7 and §6 AC9.** §7 calls `line length` "the re-wrap's only constraint".
`tools/line-length-limits.txt:23` declares **450** characters for this file, and lines already in the
re-wrap region run to 115 characters (line 370). A re-wrap to ~100 columns cannot red that leg.

**Fix, in unit 2:** observe the house width directly — `awk 'length>100'` over the replaced range
returns nothing — or drop AC9 and state in §7 that the width is ungated.

---

## Pins, figures and wording

### P1 — `TOOL-aHonedRuleset-4` AC2 pins a line range an order-mate moves

**`…-4.md` §6 AC2**, citing "the five extractions in `tools/check-playbook-parity.sh:113-117`".
Verified: `PAIRS` opens at :112 and its five rows occupy 113–117 today. Unit 5 carries the same
`order 2` and its S7 adds two rows plus two header lines above them, moving the rows to 115–119. Unit
4 neither owns nor edits that file; unit 5 does.

**Fix, in unit 4:** cite the five rows by their `PAIRS` labels — `lens-array bound`,
`agent-cap hook matcher`, `verify-agent total`, `bounded-helper width`, `resolved-K ceiling` — not by
line span.

### P2 — `TOOL-aHonedRuleset-3` attaches a byte figure to the wrong file and mis-attributes a backlog row

**`…-3.md` §4 "Alternatives rejected".** It says `tools/unattended/SKILL.template.md` "has 48767 B
with no ceiling anywhere and `TOOL-aScouredKit-23` already has the uncapped Skill open as a row".
Measured now: that template is **52471 B**. 48767 is `TOOL-aScouredKit-23`'s figure for the *rendered*
`.claude/skills/unattended/SKILL.md` (`memory/backlog/TOOL.md:301`, verified verbatim), which today
measures 53234 B. Unit 6 §3 names the rendered file for the same row, so the set disagrees with
itself about which file that row covers. Unit 3's rev-1 log claims every §4 figure was measured at
base; this one was not.

**Fix, in unit 3:** name `.claude/skills/unattended/SKILL.md` as `TOOL-aScouredKit-23`'s subject and
re-measure the template at 52471 B.

### P3 — `TOOL-aHonedRuleset-5` names a gate leg that matches nothing on disk

**`…-5.md` §7**, last row: "`line length`, `memory-tree hygiene` and the rest of the bar".
`tools/gate-legs.json` spells that leg **`memory hygiene`**; units 3 and 6 spell it correctly.
`tools/check-spec-tokens.py` does not catch it because its leg join skips prose lines by shape, which
its own header states.

**Fix, in unit 5:** `memory-tree hygiene` → `memory hygiene`.

### P4 — the same cited line carries two numbers across the set

**`…-3.md` §4**, twice: "a budget its own line 7 declares" and the inventory row "budget at its own
line 7". On disk, `tools/memory-tree/BUILD-METHOD.template.md:8` is
`**Budget: ≤24 KB, ≤350 lines**`; line 7 is the merge-bar sentence. Unit 6 §4 and §8 say line 8 and
are right, as they are about line 16 (`No gate enforces the pair`) and line 20.

**Fix, in unit 3:** 7 → 8, both occurrences.

### P5 — `TOOL-aHonedRuleset-4`'s ceiling table is arithmetic against a superseded base

**`…-4.md` §1 ("a file with 8 free") and §4 "Files touched" (`Now 49144 / After 48766 / Free after
386`).** Unit 2 is `order 1` and takes 126 B out of the same two carriers first, so unit 4 starts at
49018 and lands at 48640 with 512 free; `AGENTS.md` likewise. AC4's binding half (`at most 48766`)
still fails if the cut is not made, so this is a build-record accuracy defect and not a blocker.

**Fix, in unit 4:** restate the table against the post-unit-2 tree and attribute the 8-free figure to
unit 2's base.

### P6 — `TOOL-aHonedRuleset-5`'s headroom premises are stated at a base unit 3 destroys

**`…-5.md` §4 ("`18225 / 18432 bytes (207 under, 98.9%)`") and §8 F1 ("After S3 the file sits near
18128").** Both are measured at base and ignore that unit 3 is `order 1`. After unit 3 the file is
near 16988, so F1's arithmetic is stale by roughly 1140 B against its own set's declared order. This
is the same root as A2 and S2 and is listed separately because the fix is a different edit.

**Fix, in unit 5:** restate §4's measurement and F1's arithmetic against the post-unit-3 tree, and
say which unit moved it.

### P7 — `TOOL-aHonedRuleset-5` S7's two header lines are unobserved

**`…-5.md` §6.** AC4 and AC5 cover the two new `PAIRS` rows. Nothing observes the two header
sentences S7 requires — the one saying the pair list is no longer playbook-only, and the one saying
what these rows do not cover.

**Fix, in unit 5:** add a criterion grepping both sentences out of
`tools/check-playbook-parity.sh`'s header.

### P8 — `TOOL-aHonedRuleset-4` AC9 cannot fail

**`…-4.md` §6 AC9**, requiring six named legs to "appear in the enumerated set rather than as skips".
All six — `playbook parity`, `agent-cap restatement`, `template size <=48KiB`, `charter size`,
`line length`, `playbook render wiring` — carry no `guard` in `tools/gate-legs.json`, so they run on
every bar unconditionally. The criterion asserts a property of the manifest, not of this change.

**Fix, in unit 4:** drop AC9's second clause, or restate it as the manifest assertion it actually is.

### P9 — the build's declared stream does not cover the tree its units write

**`memory/builds/aHonedRuleset/README.md` front matter**, `streams: tooling+playbook`, and the
`streams tooling` headers on units 3, 5 and 6. Three units write under `skills/session-kickoff/` and
one also writes `WIRE-INTO-PROJECT.md`; the charter's own routing table assigns those to `kickoff`
and `deployer`. Nothing gates the join, so this reds nothing.

**Fix, in the README:** widen `streams` to include `kickoff`, or record why the kickoff kit is being
edited under the tooling stream.

---

## Dropped, with the reason

Five findings the auditors raised did not survive re-checking at source.

1. **"Unit 3 claims a manifest obligation it does not owe"** (interface axis). It quoted
   `memory/guides/SESSION-KICKOFF.md:6` as ending at `.memory-tree.conf`. The line continues:
   `; coding-governance-agents.template.md; skills/session-kickoff/SKILL.md; .unattended.conf;
   memory/guides/BUILD-METHOD.md`. Both files unit 3 names ARE watched, and so is a third it also
   stages. The obligation is real — see S1.
2. **"Unit 5 claims two watched pathspecs where one is watched"** (interface axis). Same truncated
   read. `skills/session-kickoff/SKILL.md` and `skills/session-kickoff/manifest-check.sh` are both on
   the list. Unit 5's S8 and §7 are correct as written.
3. **"Unit 5 AC7 will red, or be satisfied by stamping HEAD in violation of the rule"** (acceptance
   axis). Traced through `skills/session-kickoff/manifest-check.sh:284-310`: when the re-stamp is
   bundled into the same commit as the watched change, the newest watch-touching commit `W` and the
   newest stamp-changing commit `S` are the same commit, and `git merge-base --is-ancestor W S` is
   true reflexively. Check 5 passes whatever sha value is stamped, provided check 3's ancestry holds
   — and a merge-base is an ancestor. `KICK-cSettledDocket-1`'s failure mode needs the stamp to
   PRECEDE the watched change, which is not what S8 does. Confirmed by running the checker at base:
   exit 0.
4. **"Unit 2 AC10 reads a file its order-mate writes"** (interface axis). `git diff -- <path>` with no
   revision compares the working tree to the index, so a sibling's committed bump is invisible to it.
   The finding is also moot under S2, which removes unit 3's bump entirely.
5. **"Delete unit 5's F1, the bump is unit 3's"** (interface axis, the direction of the fix). Rejected
   in favour of S2's direction. Unit 5 is the LAST unit to touch that file, so a bump recorded at
   order 1 is stale the moment order 2 lands; and two siblings state the no-bump-on-a-shrink rule
   with a reason, which makes unit 3 the outlier rather than unit 5.

Also checked and clean, so no finding was written: no two units claim the same region of the same
file for an edit (template 230–245 vs 363–374 are disjoint; engine 118–119 vs 223–241 are disjoint);
every path named across the five specs exists; every gate-leg name except P3 matches
`tools/gate-legs.json` including its subject, chunk and guard claims; all five parity phrases occur
exactly once in each carrier; `tools/check-microformats.sh` has exactly six numbered `fail` arms
mapping as unit 2's §4 table claims; and the byte spans 1218, 1488, 1467, 1101, 825, 24564, 18225,
49144, 64506 and 54772/54772 all reproduce at base.

---

## Classes — BUILD-METHOD M2

| unit | class | why |
|---|---|---|
| `TOOL-aHonedRuleset-2` | **FORKED** | §8 F1 decides whether a measured 126 B still earns the unit and whether the census re-ranks, and F2 decides whether S2's 86 B connective is in scope; both are owner calls the spec does not sign. |
| `TOOL-aHonedRuleset-3` | **FORKED** | §8 F2 leaves the two `BUILD-METHOD.template.md` repoints in or out of the write set, and one branch of it makes AC8 unsatisfiable (A4); S6 also executes a row unit 5 declares an owner call (S2). |
| `TOOL-aHonedRuleset-4` | **FORKED** | §8 F1 decides a token inside S1 and F2 decides how far S5's array-literal correction reaches against the OPEN `TOOL-dFramedEntrypoint-1`; scope is otherwise determined and disjoint. |
| `TOOL-aHonedRuleset-5` | **FORKED** | §8 F1 is an owner call on `tools/template-size-highwater.txt:3` and F2 decides whether S7's two rows live in `check-playbook-parity.sh` at all; the unit is otherwise the best-formed of the set and the only one that gets the re-stamp right. |
| `TOOL-aHonedRuleset-6` | **FORKED** | the hard case. §2 opens "The executable scope is selected by the §8 F1 ruling", and F1 is UNRESOLVED and unsigned, determining four of six carriers. Nothing is buildable here until it is ruled (B3). |

None is MISSING and none is THIN: every unit carries a full spec with measured figures, a
production-readiness pass, acceptance criteria and a reuse audit. What every one of them is missing
is a signature.

## Round

**Round: 1.** No unit is cleared to build. The cheapest ordering out of BLOCKED is B1 first (it is a
live red and touches no spec), then the two rulings — unit 6 F1 and the high-water row — because
between them they settle B3, S2, S3 and P6.
