**Serves:** diff-review TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

# Tier-2 closing diff review — the aHoistedPass build

*Adversarial pass over the cumulative diff of all ten units, run at the integration boundary. Node
`a`, 2026-09-06, ROUND 1. Every finding below survived a skeptic prompted to refute it; each carries
its address, its fix, and the gate that would have caught it before a reader had to.*

**Reviewed range:** `e828f7784ce1fc713a9d008a82d524bb62dcb6a1...HEAD` — 91 files, +7106/-712.

## Verdict: BLOCKED

Two findings are BLOCKER as I adjudicate them, and both sit on the surfaces this build exists to
make real. Finding 1 lets one tracked `.unattended.conf` line redirect the kit gate's subject away
from the driver it grades — reproduced twice on the live tree, in the same diff that closes the
identical class one file over. Finding 7 is a regression this build introduced: attended mode now
halts at unit one, because the new per-unit child unconditionally orders two verbs that hard-refuse
without a run-state file, which is exactly the state attended mode is defined by. Neither is a
judgement call about taste; both were executed or read end to end.

Every other finding is a fix, not a stop. Five are worth landing before the merge, one is a nit.

## Review shape

Raw 14, confirmed 10, refuted 4, unverified 0, precision 0.71.

**Run integrity — all zero, so this run is complete.** Lenses 4/4 returned, 0 DIED. Skeptic batches
5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded,
0 duplicates. No lens died, so a zero count in a class below is evidence, not a gap.

**One adjudication the pipeline's duplicate counter did not make.** Four confirmed findings — ids 3,
4, 8 and 11 — are the same defect at the same line, `check-unattended.sh:1621`, found independently
by four lenses and each cleared by its own skeptic. The pipeline reported 0 duplicates because it
dedupes before adjudication, not after; I merged them into F3 below. So the honest pair is **10
confirmed reports over 7 distinct defects**. Four independent lenses converging on one line is a
signal about that line, not a reason to count it four times.

**Commits reviewed** (the range's unit-bearing tips): 8219a504, 4c255e61, f13c071a, 867b14a9,
8c759e50, 01c07a97, dd6bfbff, b0b13b54, 3cef2a2c.

## Findings

| # | Sev | Address | Defect |
|---|-----|---------|--------|
| F1 | BLOCKER | `tools/unattended/check-unattended.sh:151` | The gate's conf import assigns every uppercase key, so a tracked conf line redirects `DRIVER`, `SCOPE` and `HERE` |
| F2 | BLOCKER | `tools/workflows/unattended-unit.js:105` | The per-unit child is mode-blind and orders `--dispatch`/`--brief`, which hard-refuse in attended mode |
| F3 | HIGH | `tools/unattended/check-unattended.sh:1621` | Check 16's body term iterates `$core` (CORE + EXTRA) while its own comment promises CORE-only |
| F4 | HIGH | `tools/workflows/unattended-build.js:739` | The DISPOSAL guard ignores a non-empty `standing`, handing out the full roster over an undisposed blocker |
| F5 | MEDIUM | `tools/memory-tree/BUILD-METHOD.template.md:20` | The shipped template asserts a gate that no adopter tree receives |
| F6 | MEDIUM | `tools/unattended/SKILL.template.md:558` | Two carriers spell the harness route differently; the new ratchet grades only the correct half |
| F7 | LOW | `tools/workflows/unattended-build.test.sh:508` | Unescaped backticks in two double-quoted arm labels run as commands and blank the identifier |

---

### F1 — BLOCKER — `tools/unattended/check-unattended.sh:151`

**The kit gate's conf import assigns every uppercase key, so a tracked conf line points the gate at a
different file than the one it certifies.**

Line 151 is the open glob `[A-Z][A-Z0-9_]*) eval "$_ck=\$_cv"`. It runs after line 68 sets `HERE` and
line 69 sets `DRIVER="$HERE/unattended.sh"`, so the import overwrites both.

I reproduced it twice. Appending `DRIVER="/dev/null"` to the tracked `.unattended.conf` made
`bash tools/unattended/check-unattended.sh` report that it cannot read `AUTH_MODES` from the driver
at `/dev/null` — three check-1 refusals naming it. A decoy carrying plausible declarations instead of
`/dev/null` makes checks 1, 2, 16, 26, 28 and the check 31 this diff adds grade the decoy, while the
real `unattended.sh` enforces something else. The gate then certifies a driver it never read.

Two further reachable effects, both read at source. `SCOPE` is overridable identically, and line 2354's
`if [ "$SCOPE" != skip28 ]` is evaluated after the import, so `SCOPE="skip28"` in the conf silently
deletes the whole check-28 region including 28c, the pinned-git-read enforcement. `HERE` redirects the
`check-playbook.sh` byte-comparison at line 2677.

The one plausible mitigation does not hold. Check 22's project-conf key join at lines 1411-1417
extracts keys with `grep -oE '^[A-Z_]+='` — column 0, no `export`, no digits — while the importer's
sed at line 145 accepts leading whitespace and an `export` prefix. Verified directly:
`export DRIVER="/dev/null"` yields zero keys for check 22 and `DRIVER` for the importer, and a live
run with that exact line still graded `/dev/null`.

**Why it is this build's problem, not an inherited one.** The open allow-list predates this diff. But
this diff adds check 31 *into* that file, reading `$DRIVER` at line 2992 and deriving `${core:-}` from
`core_of DIRECTIVES_CORE` on it — while the sibling this same build ships,
`tools/unattended/check-brief-recorded.sh:109`, closes the identical class with a four-key allow-list
and arms it at `check-brief-recorded.test.sh:255` with a `DRIVER="tools/unattended/evil.sh"` arm. The
comment above that allow-list names this leg's `DRIVER` hole as its reason. The amendment left its
other half standing, and it added a check to the standing half. `.unattended.conf` is a tracked file
an unattended run itself commits, and this leg is an unguarded merge-bar leg.

The file's own header claims the worst a hostile conf can do is fail to deliver the sentinel, which is
a refusal. That is false as written. UNATTENDED-PROTOCOL section 1 cost 2 concedes that a leg reads its
subject's *answer*; it does not concede the leg reading a different *file*.

**Fix.** Replace line 151's open pattern with the closed allow-list of the keys this leg actually
declares, exactly as `check-pass-order.sh:~150` and `check-brief-recorded.sh:109` already do:
`MEMORY_ROOT|LANDER|BYPASS_BAN|GATE_CMD|WIRING_CHECK|KEEPALIVE_*|PHASES_EXTRA|DOD_EXTRA|CORE_FLOOR|LANDED_ANCHOR_CUTOFF|DISPOSITION_CUTOFF|KICKOFF_ENGINE|KICKOFF_EXITS|DIRECTIVES_EXTRA|DIRECTIVES_FLOOR|DIRECTIVES_EXTRA_TABLE|HALT_CODES_EXTRA|HALT_FLOOR|ADV_NAME`.

**Left-shift gate.** Port `check-brief-recorded.test.sh`'s evil-driver arm into
`check-unattended.test.sh` — one arm setting `DRIVER` to a decoy and asserting the leg refuses, one
setting `SCOPE="skip28"` and asserting check 28 still runs. Then close the class rather than the two
instances: a bar leg that greps every `tools/unattended/*.sh` conf importer for the open
`[A-Z][A-Z0-9_]*)` arm and reds on any that is not a named-key alternation. Three importers exist
today and two are already correct, so the predicate has a live positive and two live negatives to
prove itself against before it is wired.

### F2 — BLOCKER — `tools/workflows/unattended-unit.js:105`

**The new per-unit child is mode-blind and unconditionally orders two verbs that hard-refuse in
attended mode, so every attended dispatch reaches a binding refusal and stops.**

`unattended-unit.js:99-119` composes `PROMPT` from `cfg.ground` plus, unconditionally, *Declare the
write set with `<driver> --dispatch …`. A REFUSAL FROM IT IS BINDING — read it and stop*, and *Record
what you were handed with `<driver> --brief …`*. The child's own arg contract, the `check()` calls at
lines 74-81, has no mode key, and `unattended-build.js:881` hands it exactly
`{repo, slug, driver, ground, checklist}`. Mode is not among them.

`verb_dispatch` at `unattended.sh:4598` does `[ -f "$rel" ] || { fail 49 "no run-state file…"; }` and
`verb_brief` does the same. Attended mode's defining premise, per `unattended-build.js:36-60`, is that
no run-state file exists. Both verbs therefore refuse, and the child has been told a refusal is
binding.

`git show dd6bfbff` confirms this is a regression rather than a pre-existing gap. TOOL-6 deleted
`driverSteps`, whose ATTENDED branch read verbatim: *you must not call them: `--dispatch`, `--brief`
and `--rescope` all refuse without one*. The surviving comment at lines 815-819 acknowledges only the
lost write-down-paths advice; it does not acknowledge that the unattended branch is now issued to
attended runs.

The child also receives two contradictory instructions in one prompt. `GROUND` at lines 340-342 tells
an attended child that *the driver's recording verbs are unavailable because there is no run-state
file to record against*, and the next paragraph orders it to call two of them.

This is the exact failure `unattended-build.js:756-764` moved the planState grading forward to
prevent — attended mode halting at unit one after units were already being written.

**Fix.** Carry the mode into the child: add `mode: mode` to `dispatch.args` at
`unattended-build.js:881` and to `perUnit`/the `check()` list in `unattended-unit.js`, then branch
lines 105-113 back onto the two texts `driverSteps` held, with the attended branch writing the paths
down instead of calling the two verbs.

**Left-shift gate.** Two arms. One in `unattended-build.test.sh` asserting `dispatch.args` carries the
mode. One in a child-side suite asserting the attended prompt does not contain the substring
`--dispatch`. The general form is stronger and cheap: a test that renders the child prompt in both
modes and asserts that no verb named in the driver's own fail-49 set appears in the attended one —
that predicate keeps holding when a fourth verb joins the set, which a substring arm would not.

### F3 — HIGH — `tools/unattended/check-unattended.sh:1621`

*Merged from confirmed findings 3, 4, 8 and 11 — four lenses, one line, one defect.*

**Check 16's new body term iterates `$core`, which is `DIRECTIVES_CORE` plus `DIRECTIVES_EXTRA`,
while the comment eight lines above it promises the opposite.**

Read at source. `core` is built at lines 1474-1480 from `$DIRECTIVES_CORE $DIRECTIVES_EXTRA`;
`corescope` at lines 1481-1487 is the core-only list. The body term at line 1621 loops
`for pair in $core`. Its own rationale at lines 1600-1603 reads: *CORE-ONLY, on `corescope`'s own
principle. A project's `DIRECTIVES_EXTRA` rows are hand-authored and must not red an adopter for prose
the kit never asked them to write.* The code does the opposite of what the comment claims — the
false-confidence class this repo's own charter gates for, in a gate.

It is also a deviation from the ratified design, not a mis-transcribed comment. The spec
(`2026-09-04-spec-TOOL-aHoistedPass-2.md:177`) and the design pass (`design-pass.md:1197`) both say
the body term takes a THIRD CORE-only list.

**Consequence, and why it is HIGH rather than MEDIUM.** An adopter declaring
`DIRECTIVES_EXTRA="house-style:M9"` — a documented extension point, `.unattended.conf.example:89` —
puts `house-style:M9` in `$core`, and the kit-rendered `memory/guides/BUILD-METHOD.md` contains no
backticked `house-style`, so `fail 16` fires. They cannot clear it: `tools/memory-tree/kit.toml`
ships that file with `role = "rendered"` and the `kit/dogfood doc parity` leg — a declared
`[[gate_leg]]` adopters do receive — byte-compares the render, so hand-adding the anchor reds parity
instead. `DIRECTIVES_EXTRA_TABLE` is a row source for the Skill table, not for BUILD-METHOD prose.
The result is a permanent red on an unguarded merge-bar leg with no route to green, for the one
adopter who uses the documented knob.

Invisible on gov's own bar for two independent reasons, both checked: `.unattended.conf:78` sets
`DIRECTIVES_EXTRA=""`, and the suite's extras arms at `check-unattended.test.sh:1809` and `:2056` run
after a `reset_tree` that removes the carrier, so `[ -f "$M/guides/BUILD-METHOD.md" ]` is false and the
term is silent. The green arm *declared + shown is silent* proves nothing about it — a
fixture passing by finding nothing.

Arm B at line 1590 correctly keeps `$core`: existence is satisfiable by an adopter citing any real
section; body text is not. This is the strictest term in the leg applied to the widest population.

Two secondary claims that came in with the reports are wrong and are recorded here so they are not
re-litigated: `check-method-carriers.sh` does no byte-compare and excludes `$MEMORY_ROOT/*` at line
64, and the red count is one per extra handle, not seventeen.

**Fix.** Accumulate a third list beside `corescope` — `coresec="$coresec$_dh:$_ds\n"` inside the
`for _de in $DIRECTIVES_CORE` loop at line 1481 — and iterate that at line 1621. Four lines, and it is
what the spec ordered.

**Left-shift gate.** An arm in `check-unattended.test.sh` that declares a `DIRECTIVES_EXTRA` handle
whose cited section names no anchor and asserts check 16 stays green — run against a fixture that
*has* the carrier, since the existing extras arms are silent precisely because theirs does not. That
fixture gap is the reusable lesson: any arm exercising a term guarded by `[ -f ]` must assert the file
exists first, or it is testing the guard.

### F4 — HIGH — `tools/workflows/unattended-build.js:739`

**The DISPOSAL guard tests only `d.disposed !== true`, so `{disposed: true, standing: ['b1']}` logs
`disposal: done` and hands out the full roster over an undisposed blocker.**

`DISPOSAL_SCHEMA` at line 320 requires `standing` as a string array with `additionalProperties: true`,
so that pairing validates, clears the guard, logs done at line 753 and falls into the hand-out, which
maps the full `buildUnits` roster. Under the stage's own prompt at line 733 — *NAME in `standing`
every blocker you did NOT dispose* — the pair is self-contradictory.

This is reachable on exactly the two verdicts that structurally guarantee standing blockers,
NON-CONVERGENT and CEILING, which are the only verdicts reaching the stage at all since CONVERGED
short-circuits at line 721. This build itself exited NON-CONVERGENT at round 3. The impact is the
defect the stage's own header at line 714 names as its reason to exist: *the harness built a spec set
with open blockers*.

The same file refuses the analogous impossible pairing by name twelve lines earlier — CONVERGING with
0 blockers, line 659 — and again for a non-enum token at line 648. The pattern is established in this
file; this guard just did not get it.

Compounding it, `standing` never reaches the success return at lines 860-900, which carries `verdict`,
`blockers`, `specRefused` and `skippedTerminal` but not what stood. That is
`degradation-known-but-unreported`, a class this same file names three times.

No arm covers the pairing: `DISPOSE_OK` at `unattended-build.test.sh:79` uses `standing: []`, AC5 at
line 457 uses `disposed: false`, AC5b at line 470 uses a dead stage.

**Fix.** Widen the guard to the pairing and carry the list out:

```js
const stood = Array.isArray(d && d.standing) ? d.standing : []
if (!d || d.disposed !== true || stood.length) { /* the existing DEGRADED return */ }
```

plus `standing: stood` on the terminal return at line 859.

**Left-shift gate.** One arm feeding `{"disposed":true,"standing":["b1"],"summary":"x"}` through
`returns NON-CONVERGENT 2` and asserting `"roster":[]`. Worth generalizing while the shape is fresh:
this file now refuses three impossible pairings in three hand-written blocks, so a single
`refusePairing(cond, why)` helper with the three call sites would make the fourth omission
structurally visible. That is a suggestion, not a finding — the three blocks are correct as they
stand.

### F5 — MEDIUM — `tools/memory-tree/BUILD-METHOD.template.md:20`

**The shipped template tells every adopter that a gate enforces its byte budget, and no adopter tree
receives that gate.**

Line 20 ships: *The gate is `build-method size`, which measures this file's RENDER against the ceiling
declared for it, and its PAIR TERM reds when the figure above disagrees with that declaration.*

`tools/govkit/registry.toml:281-283`, added by this same unit, says the opposite in its own words:
`build-method size` is an `[[exempt_leg]]` and deliberately not a `gate_leg` in
`tools/memory-tree/kit.toml`, because *that kit ships BUILD-METHOD.template.md and ships no size gate,
so declaring it there would make `apply` emit an adopter a row running an engine gov never ships*.
`tools/check-template-size.sh` is a path exemption at `registry.toml:177` and
`tools/template-size-limits.txt` is one at `:239`. Neither the leg, the script, nor the declaration
travels. I enumerated the kit's 16 gate legs; this is not among them.

`kit.toml` declares `placeholders = ["KIT_DIR", "TOOL_ROOT"]` for the file and `render-doc.sh`
substitutes rather than dropping blocks, so nothing removes the sentence. Every rendered adopter copy
of M1 asserts a checker that does not exist there.

That is the same *a directive names a route that does not run* class this whole build was opened to
close at M6 / `passes-harnessed`, reintroduced one document over. The spec analyses the gov/adopter
asymmetry at length for the registry row and never mentions the template sentence, so it is not a
disclosed trade.

**Fix.** Drop the gate sentence from the template — keep the byte figure, which is a property of the
document — and leave the gate's identity in the comment block above the `memory/guides/BUILD-METHOD.md`
row in `tools/template-size-limits.txt`, where the declaration already lives. Re-render
`memory/guides/BUILD-METHOD.md` in the same commit so dogfood parity stays green. If the sentence must
survive in gov's render, it needs a conditional the renderer drops for a target with no size gate, the
way §1's unattended block is dropped.

**Left-shift gate.** The general predicate is worth more than this fix: a leg that greps every
`*.template.md` under `tools/` for a backticked leg name and reds when that name is an `[[exempt_leg]]`
in `registry.toml` or absent from the shipping kit's `gate_leg` set. `registry.toml` already holds both
halves, so the check is a join over data that exists. Run it over the tree before wiring and print
near-misses — a shipped template naming a gov-only leg is unlikely to be a population of one.

### F6 — MEDIUM — `tools/unattended/SKILL.template.md:558`

**The two carriers of the harness route disagree by construction, and the new ratchet grades only the
half that was already right.**

`SKILL.template.md:558` and `:560` spell `tools/workflows/unattended-build.js` and
`tools/workflows/unattended-unit.js` as literals. `tools/memory-tree/BUILD-METHOD.template.md:207,209`
spell the same two as `{{TOOL_ROOT}}workflows/…`. `adopt-unattended.sh`'s `render()` at lines 208-244
substitutes `KIT_DIR`, `MEMORY_ROOT`, `LANDER`, three `KEEPALIVE` keys, `ANCHOR_SCOPE` and
`AUTH_PARAM`. `TOOL_ROOT` is not among them, and unlike `adopt-memory-tree.sh:85-86` this adopter never
derives one.

At a root install `adopt-memory-tree.sh:85` renders `TOOL_ROOT` as the empty string, so BUILD-METHOD
names `workflows/unattended-build.js` and the Skill names `tools/workflows/unattended-build.js`, which
resolves to nothing — and the Skill mandates `scriptPath` calls, never `name`.

Check 31, added by this same build precisely to catch an unresolvable route, reads only
`$M/guides/BUILD-METHOD.md` at lines 2991 and 3002. It never reads the Skill, so it passes over exactly
this half. The decisive detail is check 31's own comment at lines 3013-3015: *TOOL_ROOT renders to the
empty string at a root install, so an install-prefix literal here would be wrong in an adopter tree in
both directions.* The build's own code declares the literal wrong while the same build ships it into
the Skill.

`tools/install-prefix-carried.txt:101` records the deviation in its own words, so the omission was
seen. But the recorded reason explains only why the placeholder was not used, not why the literal
resolves — and the one-line fix the sibling adopter already demonstrates was not taken.

**Fix.** Add `{{TOOL_ROOT}}` to `adopt-unattended.sh`'s substitution set and use it in the Skill
bullet, the shape `adopt-memory-tree.sh` already ships. Or drop the two literals from the Skill and
point the bullet at M6, which owns the route.

**Left-shift gate.** Widen check 31's subject to the rendered Skill, or it keeps certifying only the
half that was already correct. Stronger and barely more work: have the check derive the route from one
source and assert both carriers resolve to it, which is the pair term this build already used for the
byte budget in TOOL-3 — the technique is in the diff, it just was not applied here.

### F7 — LOW — `tools/workflows/unattended-build.test.sh:508`

**Two new arm labels are double-quoted around unescaped backticks, so the shell runs `built` and
`unbuilt` as commands while building the label.**

Reproduced. The suite prints `line 508: built: command not found` and `line 509: unbuilt: command not
found` to stderr, and the arms report as *S4 the return no longer carries a  count* and *an  list* with
the identifier gone. The needles are single-quoted (`'"built":'`), so the assertions are correct and
the suite exits 0. The cost is a verdict line that names nothing, plus command execution from a string
meant to be inert.

The trap is already documented in this tree: `check-unattended.test.sh`'s `_bm31` carries a loud
comment saying a backtick in a double-quoted string here is command substitution and cost a 50-minute
run to find.

**Fix.** Escape both, or single-quote the labels:
`hasnt_ 'S4 the return no longer carries a `built` count' "$o" '"built":'`.

**Left-shift gate.** A grep over `tools/**/*.test.sh` for an unescaped backtick inside a double-quoted
first argument to the assertion helpers, redding on a hit. The class is narrow and the predicate is
cheap; run it over the tree first, because the `_bm31` comment implies this has bitten before and the
sweep is likely to name more than these two.

## What was refuted

Four raw findings did not survive their skeptic and are not carried: they are recorded in the run
artifacts rather than restated here, since a refuted finding re-reported is exactly the noise the
skeptic stage exists to remove. Precision 0.71 is comfortably above the ~0.5 floor at which §8 says to
tighten scope before adding agents, so the lens set and priming held for this surface.

## Notes for the fold

Three of the seven defects — F1, F3 and F6 — are the same shape: a correct treatment exists in this
diff, one file over, and the amendment did not reach its other half. F1 has the allow-list in
`check-brief-recorded.sh`, F3 has `corescope`, F6 has the pair term TOOL-3 built. That is worth a
gotcha record of its own, because it is a property of how this build was sequenced rather than of any
one unit, and the next multi-unit build will sequence the same way unless something says otherwise.
