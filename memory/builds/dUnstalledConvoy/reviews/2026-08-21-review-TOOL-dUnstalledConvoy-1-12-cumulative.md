**Serves:** diff-review PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

# Diff review — the cumulative diff landing on main

**Reviewed range:** `4bd2a45a5a11eeb85b902df16b04b9c2453cd1dd...HEAD` (HEAD = `c1b3734a`, 24 commits,
45 files, +2111/-153). **ROUND: 1.**

## Verdict: BLOCKED

One blocker, eight highs. The blocker makes the diff's newest gate vacuous on every case-sensitive
host, which is every adopter this kit is copy-installed into.

## Review shape

- **raw 27 · confirmed 21 · refuted 6 · unverified 0 · precision 0.78.**
- After dedupe the 21 confirmed collapse to **16 distinct defects: 1 BLOCKER, 8 HIGH, 5 MEDIUM,
  2 LOW.** Nothing was downgraded in the merge; each merged section names the raw ids that reached it.
- Every finding below was verified against the tree, most by reproduction on the kits' own harnesses.
  No finding rests on reading alone except where the section says so.

## Read these first — the diff has three repeating shapes, not sixteen separate bugs

1. **A gate that prints a violation and exits 0.** B1, H1 and M2 are all this. Two of them are in
   code added by this diff, and the merge bar grades legs on the exit code alone, so each one is a
   printed `FAILED` under a green `GATE ok`. This is the exact green-by-absence class the units in
   this build were written to close.
2. **A unit id compared as a substring.** H3 and H4 both throw away the anchoring the extractor
   already had, so `TOOL-x-1` matches `TOOL-x-10`. This build's own roster runs `-1` through `-19`,
   so the collision is live on the corpus, not hypothetical — and both fixture sets pick ids that
   cannot collide, so the suites are structurally blind to it.
3. **A containment test that uses the wrong relation, in the one verb that decides M6's disjointness
   proof.** H5, H6, H8 and M3 are four different ways `verb_dispatch` certifies two overlapping
   passes as disjoint. Three of them fail OPEN and announce nothing.

H2 is the one that fails the other way: the driver's own documented repair permanently reds the leg,
with no in-band fix, because the run-state file is append-only.

---

## BLOCKER

### B1 — check 22 calls an undefined `GIT`, and only resolves on this box because MSYS is case-insensitive

*raw id 22 · `tools/memory-tree/check-memory-hygiene.sh:990` (and `:1002`)*

`GIT()` is defined in the sibling `check-unattended.sh`, not in this file. `grep -n '\bGIT\b'` over
`check-memory-hygiene.sh` returns exactly the two new call sites and no definition, no assignment,
and no `source` that could supply one; the file's five pre-existing git calls are all lowercase. On
this box `command -v GIT` resolves `/mingw64/bin/GIT`, which is the only reason the leg passes.

On any case-sensitive host — Linux CI, a case-sensitive macOS volume, and every adopter repo this
kit is copy-installed into — both command substitutions produce nothing, with stderr already sent to
`/dev/null`. The script is `set -u` with no `set -e`, so execution continues: `alledger` is empty AND
the spec loop iterates zero times. `alpop` stays 0, and the check then prints `check 22 measured NO
unit — every closed Tier-2 spec predates ACCEPTANCE_LEDGER_CUTOFF`, misattributing a broken command
to the cutoff, without setting `status`. The leg exits 0. The check is vacuous and announces itself
as legitimately empty.

Reproduced: `PATH=/nonexistent; out=$(for r in $(GIT ls-files "x" 2>/dev/null); do echo "$r"; done)`
yields an empty `out` and rc=0 — the `2>/dev/null` swallows the command-not-found.

This is the kit's own `vacuous-selector-empty-population` and `subprocess-resolves-a-different-shell`
classes firing at once, inside the check that was added to close a coverage hole.

**Fix.** Use `git ls-files` at both 990 and 1002, matching the five existing call sites. If a
graft/replace pin is genuinely wanted here, define `GIT()` at the top the way `check-unattended.sh`
does — but do not leave a bare `GIT` that only a case-insensitive filesystem resolves.

**Left-shift gate.** A `check-memory-hygiene` self-test arm that runs the script with `PATH` reduced
to a directory holding a lowercase `git` only (no `GIT`), and asserts the leg still measures a
non-zero `alpop`. Cheaper and broader: a bar leg that greps every tracked `tools/**/*.sh` for a
capitalised command word that the same file does not define as a function — this class recurs the
moment a second kit borrows a helper by sight.

---

## HIGH

### H1 — check 22's orphan-successor arm sets `status` in a subshell, so the leg prints `FAILED` and exits 0

*raw ids 1, 12, 23 (three lenses, one defect) · `tools/unattended/check-unattended.sh:1009-1014`*

The third arm is `printf … | grep -oE … | awk … | sort -u | while IFS= read -r rssucc; do … fail 22
…; done`. `fail()` (line 47) does nothing but echo and set the global `status`, the script ends
`exit "$status"` (line 1185), and there is no `shopt -s lastpipe` anywhere in the file. `grep -n '|
while'` returns exactly one hit — this new arm; every other loop in the file is a `for` or is fed by
a heredoc, including its own two sibling arms directly above it.

Reproduced three ways. In a bare shell: `status=0; fail(){ echo FAILED; status=1; }; printf 'a\n' |
while read -r x; do fail; done; echo $status` prints `FAILED` then `0`. On an instrumented copy of
the real script with `status` zeroed immediately before the arm: `ISOLATED_STATUS_AFTER_ORPHAN=0`,
rc=0 — while the same instrumentation on the sibling WONTDO arm (a plain `for` in the main shell)
gives `1`, rc=1.

`gate-legs.json:579` runs this script directly and `run-gates.sh` grades on rc alone
(`case "$rc" in 0) st=ok`), printing a leg's captured output only in the FAIL branch. So a run that
supersedes a unit into a successor its executing roster never carries emits `UNATTENDED check 22
FAILED — a rescope row supersedes into a successor the executing roster does not carry …` and the
merge bar reports the leg green. Nobody sees the line.

The covering test cannot see it either, by construction: `run()` at `check-unattended.test.sh:125` is
`bash "$SCRIPT" 2>&1` — rc discarded — and the arm at 1247 is a stdout grep, so `check-arms.py` reads
the branch as ARMED and the harness meta-gate reports full coverage.

**Fix.** Feed the loop from a heredoc, matching the `DSSIBS`/`DSROWS` idiom the same file already
uses: `while IFS= read -r rssucc; do … done <<SUCCS` / `$(printf '%s\n' "$rs_rows" | grep -oE … |
awk … | sort -u)` / `SUCCS`.

**Left-shift gate.** Two, and the second matters more than the first. (a) Make `run()` in
`check-unattended.test.sh` capture and assert the exit code on at least one failing arm, so a `fail`
that cannot reach `status` is red rather than invisible. (b) Extend the harness meta-gate
(`check-arms.py`) so a `fail` branch is ARMED only when its sibling assertion covers the EXIT CODE,
not merely the text — otherwise this whole class is certified covered while being unreachable.

### H2 — check 23 grades every dispatch row, so the driver's own sanctioned widening repair permanently reds the leg

*raw ids 9, 15 (both reproduced end-to-end) · `tools/unattended/check-unattended.sh:1041`*

`park()` (`unattended.sh:1956-1958`) appends with `>>`, so `--dispatch` widening
(`unattended.sh:2233`) writes a SECOND row for the same (group, unit) and never retires the narrow
one. The driver reads only the last (`cur=… | tail -1`, `unattended.sh:2222`). Check 23's row loop
has no dedupe by (group, unit), so it runs the subset test against the same commit once per row, and
the stale narrow row always fails. The same-unit skip in the ambiguity loop does not help.

REPRODUCED on the real leg with the suite's own fixture harness: declare `work/one.txt`, widen to
`work/one.txt work/two.txt` (the driver prints `dispatch WIDENED`), commit both files —

```
UNATTENDED check 23 FAILED — a dispatched pass committed a path outside the set it declared
before dispatch … ARCH-tRun-1 at e364d2fd wrote work/two.txt
```

— leg rc=1. The control carrying only the widened row was clean.

`SKILL.template.md:227` prescribes widening as THE repair ("re-declare with the WIDER set BEFORE the
commit"), the suite asserts the driver's half of it at `unattended.test.sh:2320`, and RUN.md rows are
append-only with no verb that rewrites one. So the red has no in-band repair — which is precisely the
wedge M6 and TOOL-dUnstalledConvoy-10 exist to remove.

**Fix.** Collapse `dsrows` to the LAST row per (group, unit) before the loop — the same last-wins
`tail -1` selection the driver already uses — and grade only that one.

**Left-shift gate.** A leg arm that performs the widening through the DRIVER and asserts the leg
stays green. The suite currently tests widening only at the driver and never through the leg, which
is how a two-sided protocol ships with the two sides disagreeing.

### H3 — check 23 joins a declaration to a commit by unanchored substring, so `-1` claims `-10`'s commit

*raw ids 11, 25 · `tools/unattended/check-unattended.sh:1067` and `:1099`*

Both the window scan and the ambiguity refusal use `case "$(GIT log -1 --format=%s …)" in
*"$dsunit"*)`. Confirmed in a shell that subject `TOOL-dUnstalledConvoy-10 build: something` matches
unit `TOOL-dUnstalledConvoy-1`.

Reproduced in both orderings on the kit harness with a group holding `ARCH-tRun-1 -> work/one.txt`
and `ARCH-tRun-11 -> work/eleven.txt`, one correctly-named commit each. With `-1` committing first:
one failure. With `-11` first: both mirrors fire — `one commit names two passes of the same dispatch
group … ARCH-tRun-1 and ARCH-tRun-11` and its reverse — leg rc=1. Two genuinely disjoint passes,
each commit correctly attributed, red the bar with no in-band repair.

Line 1067 carries the same defect on the window scan, so pass `-1` can also select pass `-11`'s
commit as its `dshit` and subset-test one pass's declaration against another pass's diff — a verdict
that is meaningless in either direction. The header calls this join "the whole of its correctness",
and the ambiguity refusal that was written to "refuse rather than guess" is defeated by the same
defect it was meant to guard.

Live shape: this build's roster carries `TOOL-dUnstalledConvoy-1` alongside `-10`, `-11` and `-12`.
The kit matches ids exactly everywhere else (`grep -qxF`, `grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+'`),
so this is not a house convention. Mitigating but not refuting: no dispatch row exists in the corpus
yet, so this is shipped-but-unexercised.

**Fix.** Require a delimiter on both sides at both sites:
`grep -qE "(^|[^A-Za-z0-9-])$dsunit([^A-Za-z0-9-]|$)"` against the subject, or an equivalent `case`
on a space-padded subject.

**Left-shift gate.** A fixture whose dispatch group holds `ARCH-tRun-1` and `ARCH-tRun-10`, asserting
the leg green. Generalise it: a suite convention that every id-matching fixture set includes a
prefix-colliding pair, since `-1`/`-1x` is the ordinary shape of a real roster and the current
fixtures (`-1`, `-2`, `-7`, `-9`) cannot fail.

### H4 — check 22 tests roster membership with unanchored `grep -F`, so an unrecorded scope change passes

*raw ids 18, 24 (and raw 13, the same defect at the 1004 anchor) ·
`tools/unattended/check-unattended.sh:997`, `:1004`, `:1012`*

Ids are extracted with the bounded regex `[A-Z]+-[A-Za-z0-9]+-[0-9]+` and then re-searched as free
substrings — the anchoring information the extractor already had is thrown away at the comparison.

Simulated against the live row shape in `memory/builds/dUnstalledConvoy/README.md`:

- **Line 997 (added-id arm):** a baseline holding only `| [TOOL-x-10] | OPEN |` (the roster's own row shape, link elided) makes
  `grep -qF -- TOOL-x-1` succeed, so an added `-1` is treated as PRE-EXISTING and no rescope row is
  demanded. No fail emitted.
- **Line 1004 (WONTDO arm), worse:** with `| [TOOL-x-10] | WONTDO |` at the baseline, the piped
  pair also succeeds, so `-1` may go WONTDO whenever ANY of `-10..-19` was already WONTDO. Arm
  skipped, no fail.
- **Line 1012 (successor-present arm):** a supersession into `TOOL-x-1` reads as landed when only
  `TOOL-x-10` is present.

The gen:build-units region of this build's own README carries `TOOL-dUnstalledConvoy-1` alongside
`-10`, `-11` and `-12`, so the check is one roster edit away from silently passing the drift it
exists to catch. The fixture ids are `ARCH-tRos-1`, `-7`, `-9` — none can prefix-collide, so the
suite is structurally blind (`fixture-passes-by-finding-nothing`).

The sibling half of the pair does it correctly: `verb_rescope` tests membership with `grep -qxF`
against an extracted id list. Driver and leg therefore disagree on what "in the roster" means, and
the leg is the lenient one.

**Fix.** Extract the baseline and executing id sets with the same bounded regex used at line 996 and
test membership with `grep -qxF`, exactly as `unit_ids_of`/`verb_rescope` already do. Fix all three
lines together — a partial fix leaves the pair still disagreeing.

**Left-shift gate.** A fixture pair whose ids are `-1` and `-10`, asserting each arm fires. Pair it
with the H3 suite convention so one rule covers both checks.

### H5 — condition 3's refusals test "under", never "ancestor of", so `--writes memory` licenses every shared record

*raw id 2 · `tools/unattended/unattended.sh:2180-2188`*

The run-state refusal is exact equality (`[ "$p" = "$rel" ]`) and the shared-record refusal is
`case "$p" in "$q"|"$q"/*)` — both only ask whether the DECLARED path is under the FORBIDDEN one.
With `SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`, declaring `memory`, or
`memory/builds/<slug>`, matches neither branch.

But the declaration then COVERS all of them: check 23's subset test at line 1112 accepts by prefix
(`case "$dsq" in "$dsp"|"$dsp"/*`). So a pass declaring its own build folder — the natural
granularity, not a contrivance — silently covers `RUN.md`, and a pass declaring `memory` covers
`memory/DECISIONS.md` and `memory/backlog/`. Two concurrently dispatched passes can both write the
shared decision log with a green disjointness proof.

Grepped the leg: it never re-reads `SHARED_RECORDS`, so this verb is the only place condition 3 is
decided. There is no defence in depth.

**Fix.** Make the containment test bidirectional in `verb_dispatch`: refuse when the declared path is
under the forbidden path OR the forbidden path is under the declared path — add
`case "$q" in "$p"|"$p"/*) fail …` beside the existing arm, and the same both-ways test for `$rel`
in place of `[ "$p" = "$rel" ]`.

**Left-shift gate.** Driver test arms for `--writes memory` and `--writes memory/builds/<slug>`,
asserting a refusal on each. Structurally better: a shared containment helper (`path_covers`) used by
the verb AND by check 23's subset test, so the two halves cannot drift on what "covers" means — the
divergence is the actual defect, and one function removes the whole class.

### H6 — the sibling-intersection test uses exact string equality, so overlapping declarations are certified disjoint

*raw id 3 · `tools/unattended/unattended.sh:2209-2219`*

Condition 1's loop compares with `[ "$p" = "$q" ]`, while every other containment test in the same
function (lines 2185, 2200, 2202) and check 23's subset test use prefix semantics
(`case … in "$x"|"$x"/*`).

Pass A declaring `memory/builds/x/spec` and pass B declaring `memory/builds/x/spec/unit-1.md`
therefore never compare equal, `--dispatch` prints `dispatch declared` for both, and check 23's
prefix subset test then accepts a commit touching that file for EITHER pass. Two passes are
dispatched against the same file with the disjointness proof green — the lost-write the verb exists
to prevent.

Grepped `check-unattended.sh`: nothing there re-tests sibling intersection. Condition 1 is decided
only here, and it is decided with the wrong relation.

**Fix.** Use the same prefix relation, both directions:
`case "$p" in "$q"|"$q"/*) collide;; esac` plus `case "$q" in "$p"/*) collide;; esac`.

**Left-shift gate.** A red control declaring a directory in one pass and a file beneath it in
another, asserting the refusal. Same shared `path_covers` helper as H5 — one fix, both findings.

### H7 — the local landing arm validates one commit and records a different one as the witness

*raw id 4 · `tools/unattended/unattended.sh:1279` grants, `:1292` records*

On the remote arm, `akind=remote` is granted by `merge-base --is-ancestor "$head" "$ASHA"`, so the
recorded witness is validated by construction. On the local arm the grant tests `rbtip` (the run's
pinned `branch-ref` tip) against `refs/heads/$lbranch`, and then line 1292 writes
`set_fact "$rel" witness "$head"` — an entirely different object, with nothing tying the two together.

`verb_landed` calls only `check_slug`, `refuse_if_terminal`, the phase test, `check_clean` and
`observe_anchor`. `check_clean` tests dirtiness only; `check_branch` is never called here. So HEAD is
unconstrained, and `--landed` invoked from ANY clean worktree whose HEAD is not on the local default
branch produces a LANDED record whose witness sits on no landed history at all. `branch-ref` is
write-once (line 1558 sets it only when the fact is empty), so a run that continues on a different
branch after a resume hits this on the normal path.

Nothing downstream catches it. Check 6 only asks whether the witness resolves, and check 15's local
arm degrades to a silent report (`check-unattended.sh:466`: "a local anchor is a record of a merge
rather than an observation of one, so this clone cannot judge it"). The record is unfalsifiable. The
protocol calls LANDED "the one phase claim you cannot simply assert"; on the local arm it is asserted.

**Fix.** On the local arm, additionally require the recorded witness itself to be an ancestor of the
local default branch — `GIT merge-base --is-ancestor "$head" "refs/heads/$lbranch"` — and refuse
otherwise. Or record `rbtip`, the ref actually validated, as the witness.

**Left-shift gate.** A driver arm that runs `--landed` from a clean worktree whose HEAD is off the
local default branch and asserts a refusal. The general rule worth adding to the kit's own bug-class
list: **the object a grant validates and the object the record stores must be the same object** —
grep the driver for any `set_fact … witness` whose value was not the argument of the ancestry test
that authorised it.

### H8 — the dispatch group key is HEAD, so a commit between two declarations disarms condition 1 silently

*raw id 16 · `tools/unattended/unattended.sh:2192`*

`grp=$(GIT rev-parse --short=8 HEAD)`, and the sibling scan is
`grep -F -- " dispatch · item $grp "`. A moved HEAD yields an empty sibling set, so condition 1
cannot fire.

REPRODUCED on the real driver: `--preflight`, commit, `--dispatch tRun --pass ARCH-tRun-1 --writes
tools/shared.sh`, **commit**, `--dispatch tRun --pass ARCH-tRun-2 --writes tools/shared.sh` printed
`dispatch declared — 3b7cb950 ARCH-tRun-1` and `dispatch declared — 9df2084d ARCH-tRun-2` — both
accepted on the IDENTICAL path. The control with no commit between correctly fired check 49 ("two
passes claiming one file are not disjoint").

The contradiction is internal to the diff. Check 23's own header asserts the opposite workflow —
"`--dispatch` STAGES the run-state file, so the run commits the declaration itself" — and the leg
suite comments that "declaring them in two commits gives them two anchors and no sibling relation".
Neither `SKILL.template.md:214-226` nor `PROTOCOL.template.md:348-354` tells the run to declare every
pass of a group before committing any of them; the skill only says to re-declare wider "BEFORE the
commit". So the documented workflow disarms the primary disjointness proof, and it fails OPEN with no
announcement — the direction nobody notices.

**Fix.** Either (a) make the ordering binding in `SKILL.template.md` and `PROTOCOL.template.md` §7
and have the verb refuse a declaration whose group already carries a COMMITTED row, or (b) key the
group on something stable across the declaration commits — the phase-entry sha, or an explicit
`--group` the run mints once — and test intersection across that key. (b) is the stronger fix,
because (a) leaves a rule a run can forget.

**Left-shift gate.** The reproduction above, as a driver arm: declare, commit, declare the same path,
assert refusal. Beyond that, a self-consistency leg that reds when a group key is derived from a
mutable ref — the same "pin the base to an immutable SHA" rule §14 already states for review bases.

---

## MEDIUM

### M1 — `--writes` accepts glob metacharacters, and both consumers re-expand the recorded row unquoted

*raw id 6 · `tools/unattended/unattended.sh:2159-2175` (refusals), `:2213` and
`check-unattended.sh:1080`, `:1112` (consumers)*

The refusals cover empty, absolute, `..`, whitespace and the bypass spelling — no glob
metacharacter. Neither script sets `-f`/noglob (only `set -u`), and both consumers re-expand the
recorded row unquoted: `for q in ${sib#* · reason }` and `for dsp in $dsdecl`.

So a recorded declaration's MEANING is resolved against whatever tree reads it. Verified: `--writes
'*'` passes every current refusal, and `for dsp in $dsdecl` expands it to 47 top-level entries in
this repo — every tracked path is then a prefix match and check 23's subset test can never fail. Two
passes declaring the identical glob also pass the intersection test, because `$p` stays the literal
`*` from `"$@"` while `$q` expands to filenames and the two are never string-equal.

One sub-claim from the finder is WRONG and should not be carried into the fix note: an unmatched glob
does NOT red an innocent pass — POSIX word-splitting leaves `nomatch/*` literal. Confirmed in this
shell. The defect stands on the other leg: the same row naming different sets in different clones
breaks the record's whole purpose, whatever the header's "declare wide" allowance says.

**Fix.** Refuse `*`, `?` and `[` in a `--writes` path alongside the whitespace refusal, and add
`set -f` (or quote-safe IFS splitting) around both unquoted expansions so a recorded declaration can
never be re-globbed.

**Left-shift gate.** Driver arms for `--writes '*'` and `--writes 'tools/*'` asserting refusal, plus
a leg arm that plants a literal `*` row in a fixture RUN.md and asserts the subset test still
discriminates. The class worth pinning: a recorded field that is re-split by the shell is data whose
meaning depends on the reader's cwd.

### M2 — check 22's disarmed-population announcement is a bare `printf`, so a fully dark check exits 0

*raw id 7 · `tools/memory-tree/check-memory-hygiene.sh:1044`*

`[ "$alpop" -gt 0 ] || printf 'memory-hygiene: check 22 measured NO unit …'` — with no `status=1`,
unlike the `pop_guard`/`POP_MISSING` idiom in the same file (lines 1050-1056), which sets it for
exactly this situation. `fail()` at line 117 sets it too.

The file's own header states "Exit 0 + no output = clean. Anything printed is a hygiene regression",
so this arm violates the contract it ships with. Worse, `run-gates.sh`'s `report_one` prints a leg's
captured output ONLY in the FAIL branch, so on a green leg the announcement never reaches the bar at
all — it is written to nobody. The arm is untested: no assertion in `check-memory-hygiene.test.sh`
names its text.

Reachable by any adopter who sets `ACCEPTANCE_LEDGER_CUTOFF` forward or to adoption day — and
`.memory-tree.conf`'s own comment argues "a gate whose first run measures an empty set is an
assertion about nothing", which is the exact state this arm lets pass green. It is also the
downstream half of B1: when the `GIT` bug empties the population, this is the line that reports it as
legitimate.

**Fix.** Route it through the same mechanism as everything else: `fail 22 "… a green verdict here is
coverage of nothing"`, or append to `POP_MISSING` so the existing end-of-run block sets `status=1`.

**Left-shift gate.** A test arm that sets the cutoff past every spec date and asserts a NON-ZERO exit.
Then generalise: extend `check-arms.py` (or add a bar leg) so any line matching
`printf .*measured NO|empty population` in a gate script must be accompanied by `status=1` in the same
branch. Three findings in this diff are one `status=1` away from correct.

### M3 — condition 3's conditional half is order-dependent: declaring the index first admits the forbidden pairing

*raw id 17 · `tools/unattended/unattended.sh:2199`*

The outer loop is `for p in "$@"` gated on `case "$p" in "$idx"|"$idx"/*`, and the sibling paths are
consulted only in the inner `q` loop. So when the declaration being made carries only the GENERATOR,
the loop body never runs and `$sibpaths` is never read.

REPRODUCED under `GENERATED_INDEXES="memory/LIVE.md:tools/memory-tree/gen_build_index.py"`:
`--pass ARCH-tRun-1 --writes memory/LIVE.md` then
`--pass ARCH-tRun-2 --writes tools/memory-tree/gen_build_index.py` both printed `dispatch declared`
at the same group `94e925aa`. The mirror order refused with check 49. Condition 1 cannot catch it
either, since the two paths differ.

The exact pairing the build method's condition 3 forbids — one pass rendering an artifact while
another edits its generator — is admitted half the time, decided by nothing but which pass declared
first. `unattended.test.sh:2360-2366` tests only the generator-first direction, so the blind half is
untested.

**Fix.** Build the union once — `all="$@ $sibpaths"` — and refuse when `all` holds a path under
`$idx` AND a path under `$gen`. Symmetric by construction, so no ordering can dodge it.

**Left-shift gate.** The reverse-order arm beside the existing cross-pass one. The convention worth
adopting: every pairwise refusal gets both orderings as arms, since a one-sided test of a symmetric
rule is half a test and reads as a whole one.

### M4 — the shipped example conf omits both acceptance-ledger keys, so every scaffolded adopter runs check 22 dark and silent

*raw id 19 · `tools/memory-tree/.memory-tree.conf.example` (no anchor — the keys are absent)*

`grep -nE 'CUTOFF|GRANDFATHER'` over the example returns exactly four keys — `SPEC_FORMAT_CUTOFF`,
`STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF`, `SPEC10_CUTOFF` — and neither `ACCEPTANCE_LEDGER_CUTOFF` nor
`ACCEPTANCE_LEDGER_GRANDFATHER`. `adopt-memory-tree.sh:40` is a straight `cp` of this file, so every
scaffolded adopter inherits the omission.

The engine reads `alcut="${ACCEPTANCE_LEDGER_CUTOFF:-}"` at line 986 and wraps ALL of check 22 —
including the liveness `printf` at 1044 — inside `if [ -n "$alcut" ]`. An absent key means the check
never runs AND nothing announces that it is dark. Meanwhile `HYGIENE.template.md:270-296` ships the
full ledger grammar to adopters and `SPEC-TEMPLATE.template.md` tells authors their criteria will be
answered by it.

The existing example-conf parity arm (`check-memory-hygiene.test.sh:1305-1316`) derives its key list
from the engine's cap-validation loop only (`sed -n 's/^for _k in \(.*\); do$/\1/p'` plus a literal
`READ_PATH_HEADROOM`), so date cutoffs are structurally outside its population — the exact "example
half-done" failure its own header narrates.

**Fix.** Add both keys to the example with blank, documented defaults. Separately, either widen the
parity arm's derived population to every `${NAME:-}` conf read in the engine, or move check 22's
guard so a blank cutoff still prints the disarmed-population line (which, per M2, should also set
`status`).

**Left-shift gate.** Widen the parity arm's population by DERIVING it from the engine's own reads
rather than from one loop: `grep -oE '\$\{[A-Z_]+:-' check-memory-hygiene.sh` is the honest
population, and every name it yields must appear in the example. That is the difference between a
parity gate and a gate over the subset somebody remembered.

### M5 — the ledger flattener rejects the bold `AC` form the spec-side extractor accepts

*raw id 21 · `tools/memory-tree/check-memory-hygiene.sh:995` vs `:1024`*

Line 995's pattern is `/^- *AC[0-9]+/`, which cannot match `- **AC1** — …`. Line 1024 (and the
sibling acceptance-witness rule at line 796) use
`^([ \t]*(-|\*)[ \t]*)?(\*\*)?AC[0-9]+[a-z]?…`, which does. The ledger side also accepts only `-`
bullets where the spec side accepts `*` too.

Reproduced: ran the flattener awk over a fixture holding both `- **AC1** — \`t\` — obs` and
`- AC2 — \`t\` — obs`; the output was only `TOOL-x-1 AC2 obs`.

Not hypothetical on this corpus — `2026-08-20-spec-TOOL-dUnstalledConvoy-12.md` writes every
criterion as `- **AC1** — …` while the ledger record writes `- AC1 — …`, so the two carriers of one
token already use different bullet styles and a mirrored spec bullet is one copy-paste away. The
consequence is a MISDIRECTING false red: the gap arm fires with "a CLOSED unit numbers an acceptance
criterion that no journal record evidences" when the record exists and is in a legal form.

Weaker than first reported in one respect: `HYGIENE.template.md`'s grammar block only ever shows the
plain form, so bold is not documented-legal. The divergent regexes for one token inside one check,
and the wrong diagnosis they produce, are real regardless.

**Fix.** Use one label pattern on both sides of check 22 — match
`^[ \t]*(-|\*)[ \t]*(\*\*)?AC[0-9]+[a-z]?` in the flattener and strip the bold markers before taking
the label, rather than relying on awk's `$2`.

**Left-shift gate.** A fixture whose ledger uses the bold form, asserting green. The rule underneath:
when one token is parsed in two places, the pattern is a shared constant, not two regexes — and a
test that feeds both parsers the same fixture line is the cheapest way to keep it that way.

---

## LOW

### L1 — `SHARED_RECORDS`'s default interpolates `MEMORY_ROOT` before the conf is sourced, so it is dead

*raw id 20 · `tools/unattended/unattended.sh:73`*

Line 72 sets `MEMORY_ROOT=memory`; line 73 sets
`SHARED_RECORDS="$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog"` in the same pre-conf block;
`. "$CONF"` is line 75-76; `M="$MEMORY_ROOT"` is line 80. The interpolation therefore always expands
to the literal `memory/…` and can never track a project's declared `MEMORY_ROOT`.

A project declaring `MEMORY_ROOT=docs/memory` and no `SHARED_RECORDS` gets a default naming paths
that do not exist there, so condition 3's flat half guards nothing while `$rel` — derived from the
post-conf `M` via `runmd_of` — still resolves correctly. One function spells the memory root two
different ways. The verb's own comment three lines above claims "an adopter whose layout differs gets
refusals about THEIR paths and not this repo's", which this default does not deliver.

Placement is forced rather than accidental: `unattended.test.sh:1160` greps `^MEMORY_ROOT=memory; `
with `-A1` and demands every example key be defaulted in that two-line block. Low only because
`.unattended.conf.example:105` declares an explicit value, so the default is reached solely by an
adopter who relocates the tree and deletes that line.

**Fix.** Either write the default literally as `memory/DECISIONS.md memory/backlog` so the comment's
claim is honest, or move the derivation to after the conf is sourced and build it from `$M` alongside
`runmd_of`.

**Left-shift gate.** A driver arm running with a conf that sets `MEMORY_ROOT=docs/memory` and no
`SHARED_RECORDS`, asserting `--dispatch --writes docs/memory/DECISIONS.md` is refused. That arm also
catches the next key someone defaults by interpolation in the same block.

### L2 — `verb_rescope`'s id-shape refusal names a flag that does not exist

*raw id 26 · `tools/unattended/unattended.sh:2079`*

The message reads `--rescope --unit is not id-shaped by the driver's own spelling…`, but the argument
parser (lines 2286-2296) has cases for `--pass` and `--item` (both writing `PK_ITEM`) and no `--unit`
at all. `--unit` falls to the `*)` arm at 2312 and exits 1 with "unknown argument; the verbs are …",
a message about a completely different problem.

The header docstring (line 13), the usage string (line 2319) and the rendered Skill all spell it
`--item <id>`, and the sibling refusal at 2085 correctly says `--successor` — so this is a lone
drifted spelling, not a naming the file shares. Reachable by exactly the operator the message exists
for: anyone who mistypes an id. Real but cosmetic; no wrong verdict, no data loss.

**Fix.** Change the message at 2079 to name `--item`.

**Left-shift gate.** A cheap driver-consistency arm: for every flag spelling appearing inside a
`fail` message, assert the parser has a matching case. This is the three-places-one-set drift the
neighbouring S10 comment was written to stop, so the gate belongs beside that comment.

---

## Left-shift summary

Sixteen defects, but the gates worth adding are six, and three of them cover more than one finding.

| Gate to add | Covers |
|---|---|
| `check-arms.py` requires a `fail` branch's assertion to cover the EXIT CODE, not just text | B1, H1, M2 |
| Any `printf` announcing an empty or disarmed population must set `status=1` in the same branch | B1, M2 |
| One shared `path_covers` helper used by `verb_dispatch` AND check 23's subset test | H5, H6 |
| Every id-matching fixture set includes a prefix-colliding pair (`-1` with `-10`) | H3, H4 |
| Every pairwise refusal is tested in BOTH orderings | M3, H8 |
| The example conf's parity population is DERIVED from the engine's `${NAME:-}` reads | M4 |

Two of those are not new rules. "A probe that cannot move says so" and "a gate you have only ever
seen pass is an assertion about nothing" are already in the charter; the diff added three gates that
break the first and two suites that cannot exercise the second. The mechanical enforcement is what is
missing, not the rule.

## What this review did not cover

- No leg was run against a tree carrying a real dispatch row, because none exists in the corpus yet.
  Every check-23 finding was reproduced on the kit's scratch harness instead, and H3's live-collision
  claim rests on the roster shape rather than on an observed red bar.
- The prose diff — `PROTOCOL.template.md`, `SKILL.template.md`, `BUILD-METHOD.template.md`,
  `HYGIENE.template.md` and their rendered copies — was read only where a finding needed it (H8, M4).
  It was not audited for its own internal consistency.
- No performance or wall-clock claim was measured; unit 7's parallelism numbers were taken as given.
