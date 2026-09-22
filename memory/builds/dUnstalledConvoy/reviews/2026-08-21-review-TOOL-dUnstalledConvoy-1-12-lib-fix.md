**Serves:** diff-review PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

# Diff review — one library instead of three agreements

**Reviewed range:** `1a5a1895...HEAD` (HEAD = `a8bd64a`, 1 commit, 10 files, +726/-97). **ROUND: 1.**

**Review shape:** raw 18, confirmed 18, refuted 0, unverified 0, precision 1.00. The 18 raw findings
resolve to **8 distinct defects** after de-duplication — three of the eight were reported by four
independent lenses each, which is what a diff with three load-bearing hunks produces. No finding was
refuted and none is outstanding.

## Verdict: BLOCKED

**Three blockers, one high, one medium, three lows.**

The extraction was the right move and the library is well written. What it did not do is change the
number of questions being asked. `pass_commit` now answers three of them — the driver's condition-1
openness, the driver's re-declaration key, and the leg's commit attribution — and those three want
*different* answers at the edges. Two of the three blockers are the two directions that seam can fail
in, and they are now coupled: tightening the predicate for B1 makes B2 strictly worse. That coupling
is new in this diff and it is the single most important thing in this report. Read the **Ordering note**
before touching anything.

Shape of the damage, since this is a repair pass: of the eight defects, **two are regressions this diff
introduced** (B2, and the stale-anchor half of B2), **one is a mismatch this diff created between two
halves that previously agreed by being equally wrong** (B3), **one is the round-2 blocker surviving
under a different commit shape** (B1), and **four are new arms that arm nothing** (H1, M1, L1, L2).
L3 is a pre-existing document-versus-behaviour divergence round 2 flagged on a neighbouring path.

Four of the new fixtures were verified by mutation: reverting the fix they name leaves the suite green
at its stated assertion count. The commit message claims *"Every new arm observed RED against the exact
regression it pins"*. For the four named below, that claim does not hold.

---

## Blockers

### B1 — `pass_commit` closes a pass on any commit that carries one file besides the run-state file

**`tools/unattended/lib-unattended.sh:84-85`** (the filter; the function opens at **79**).
*Reported once: raw id 1 — high. Graded blocker here because it re-opens the round-2 blocker.*

```sh
_ptouch=$(GIT diff-tree --no-commit-id --name-only -r "$_pc" 2>/dev/null | grep -vxF -- "$_prel" || true)
[ -n "$_ptouch" ] || continue
```

The skip subtracts exactly one path — the run-state file — from a candidate commit's tree, and closes
the pass if anything at all is left. So a declaration commit that names the unit and touches
`memory/LIVE.md`, a formatter fix, or any other stray tracked file closes the pass **at declaration
time**, `sibrows` empties, and condition 1 proves disjointness against nobody.

Reproduced against a pristine HEAD copy with the kit's own harness:

```
--dispatch tRun --pass ARCH-tRun-1 --writes work/shared
git commit -m "ARCH-tRun-1 declare dispatch"        # RUN.md alone      -> second declaration REFUSED
git commit -m "ARCH-tRun-1 declare dispatch"        # RUN.md + LIVE.md  -> "unattended: dispatch declared"
```

The second form ends with two rows both claiming `work/shared`. That is the round-2 F1 defect intact,
under the commit shape a real run produces constantly: `git add -A` with a regenerated index is the
ordinary case, not the exotic one. Neither `PROTOCOL.template.md` nor `SKILL.template.md` ever tells a
run that the declaration commit must carry the run-state file alone, and the new F1 regression arm at
`unattended.test.sh:2455` commits only `RUN.md`, so nothing guards the shape.

One correction to the raw finding, measured: when the extra file lies **outside** the declared set,
check 23 does red downstream (`wrote memory/LIVE.md`). When it lies **inside** it, no check anywhere
reports the collision. The escape is real either way, and silent in the inside case.

Independently of the fix: **nothing announces an empty sibling set.** The condition-1 loop at
`unattended.sh:2272-2286` iterates zero rows and returns success, so a proof over nobody is
byte-indistinguishable from a proof over somebody. §7 requires a probe that cannot move to say so.

**Fix.** Stop inferring the pass commit from the subject alone for the *openness* question. Give the
driver's openness check the row's declared path set and require the candidate commit's
`diff-tree --name-only` to intersect it — the driver already holds it as `${_r#* · reason }`.
**Do not put that filter inside `pass_commit` itself** — see the Ordering note; the leg's use of the
same function is an attribution question and must not gain the filter.

**Left-shift gate.** Three layers.
1. Re-shape the F1 arm so the declaration commit carries one extra tracked file, and assert the sibling
   collision is still refused. Add the mirror control where the extra file is *inside* the declared set.
2. Emit a `report`/stderr line from `verb_dispatch` when `sibrows` is empty, and assert it, so a
   disjointness proof over an empty set is visible in the run log rather than silent.
3. Class-level: assert that every call site using a predicate as an *openness oracle* passes a declared
   path set. Today there is one such site and it passes none.

### B2 — the re-declaration lookup keys on the unit's open row at any anchor, so a legal second pass is refused forever

**`tools/unattended/unattended.sh:2296-2300`** (the `cur` fold; the refusal it reaches is **2321**, the
stale-anchor park is **2314/2323**). *Reported four times: raw ids 2, 6, 9, 14 — all high.*

```sh
cur=$(printf '%s\n' "$sibrows" | grep -F -- " dispatch · item " | while IFS= read -r _r; do
    _i=${_r#* dispatch · item }; _i=${_i%% · reason *}
    [ "${_i#* }" = "$unit" ] && printf '%s\n' "$_r"
  done | tail -1)
```

The group is dropped from the key and only the unit is matched. `sibrows` carries rows from **every**
anchor whose pass has not committed, and a pass that produced no change never commits — M6 sanctions
exactly that, and the leg has a dedicated arm for it at `check-unattended.sh:1096-1113` reporting
*"a pass that produced no change"*. Such a row stays open for the rest of the run, and every later
dispatch of that unit with a set that is not a superset is read as a **narrowing** and refused.

Reproduced end to end:

```
--dispatch tRun --pass ARCH-tRun-1 --writes work/spec     -> dispatch declared
git commit -m "ARCH-tRun-1 declare dispatch"              # run-state only; pass_commit skips it
                                                          # the pass changes nothing, so it commits nothing
--dispatch tRun --pass ARCH-tRun-1 --writes work/build    -> check 49 FAILED — ... narrowing is not: work/spec
```

Base `1a5a1895` keyed on `" dispatch · item $grp $unit · reason "` and printed `dispatch declared`.
This is a regression introduced by this pass, in the hunk written to fix round-2's F6.

Three things make it a blocker rather than a corner case:

- **There is no owner turn.** In an unattended run the refusal is terminal for that unit.
- **The driver now refuses a state its own leg calls legal.** `check-unattended.sh:1057-1059` states in
  capitals that the leg is keyed on (group, unit) *because* "one unit legitimately owns several rows at
  several anchors", and arms D/E assert that shape. Driver and leg disagree about a legal state.
- **The documented in-band repair is worse than the block.** Widening to the union parks the replacement
  at `$curgrp`, the *superseded row's* anchor (2314/2323). Measured: the leg then opens the window at
  pass one's anchor, finds pass two's commit as the first qualifying one, and grades it against the
  **union** — so pass two's disjointness is proved against a set containing pass one's paths, and no
  check 23 failure is printed. The second pass's own write set is never graded.

The same trigger fires for a pass whose only product is a parked decision: `verb_park` writes only the
run-state file, which `pass_commit` skips by design.

The refusal message is also a misdiagnosis — nothing was narrowed, a different pass kind was declared —
which is what will send the next reader looking in the wrong place.

**Fix.** A narrowing shares paths with the row it narrows; a new pass of the same unit need not. Enter
the re-declaration branch only when `$want` **overlaps** `$curpaths` (or when `$curgrp` = `$grp`), and
otherwise fall through to `park "$rel" dispatch "$grp $unit" "$want"` as a fresh row at the current
anchor. That preserves both properties the hunk was written for: a narrowing is a strict subset, which
always overlaps, so it is still refused after HEAD moves; and a genuine widening still reuses the
superseded anchor.

**Left-shift gate.** Two layers.
1. A driver arm for the M6 flow the leg's arms D/E already assume: dispatch a pass kind, commit nothing
   for it, dispatch the same unit's next kind with a disjoint set, assert `dispatch declared` and two
   rows at two anchors.
2. This belongs in `cross-component.test.sh`, not in either suite alone. The defect is precisely that
   the driver refuses what the leg grades, and that class is invisible to any fixture that hand-writes
   its rows with `drow`. Drive the driver, then run the leg over what it produced, and assert both are
   quiet.

### B3 — the declaration is normalised for the refusals and recorded raw, and the leg grades it raw

**`tools/unattended/unattended.sh:2291`** (`want=$(printf '%s ' "$@")`) **and
`tools/unattended/check-unattended.sh:1138`** (`case "$dsq" in "$dsp"|"$dsp"/*)`).
*Reported four times: raw ids 4, 7, 11, 17 — two high, two medium.*

The library's own header promises that the driver and the leg answer path containment identically.
The refusals now do. The **recording** and the **grading** do not: `want` is built from raw argv, and
the leg's subset test is a bare `case` against git's canonical output. `grep -n normpath
tools/unattended/check-unattended.sh` returns nothing — the leg sources the library for `GIT`, `id_in`
and `pass_commit` and calls none of its four path predicates.

Reproduced on both sides, with a clean control:

| declared | driver | leg |
|---|---|---|
| `work/sub` | accepted | green |
| `work/sub/` | accepted, parked verbatim | `check 23 FAILED — ... wrote work/sub/f.txt` |
| `./work/other` | accepted, parked verbatim | `check 23 FAILED — ... wrote work/other/f.txt` |
| `work/./sub` | accepted, parked verbatim | `check 23 FAILED` |

These are contemplated inputs, not exotic ones: the driver's own arms at `unattended.test.sh:2439-2441`
pin that `memory/`, `./memory` and `.//memory//` are one path, which is the reason `normpath` exists.

**There is no in-band repair.** Narrowing is refused by string equality at 2319-2321, so the bad
spelling cannot be dropped; and once the pass has committed, `cur` is empty, so a corrected declaration
lands at a new anchor while the stale raw row is still graded. Only a widening that adds the second
spelling clears it, and only before the pass commits. In an unattended run that is a permanent RED on
the merge bar.

The leg half reds at base `1a5a1895` too, so that half is a missed site rather than a regression. What
this diff created is the *asymmetry*: making the refusals spelling-insensitive while leaving what is
recorded and what is graded spelling-sensitive turned two components that were consistently wrong into
two components that disagree.

**Fix.** Normalise once, at the write boundary: build `want` from `normpath "$p"` for each argument, so
the parked row carries the one spelling the refusals already validated. Belt and braces, and cheap:
replace the leg's `case` with `covers "$dsp" "$dsq" && { dsok=1; break; }`, which also fixes rows
written by an older driver.

**Left-shift gate.** Two layers.
1. Arms on both sides for `work/sub/`, `./work/other` and `work/./sub`: the driver must park a
   normalised row, the leg must stay silent.
2. Class-level, and this is the one that generalises: the GIT pin is already asserted in **two** arms
   (`unattended.test.sh:1567-1571`) on the stated reasoning that *a lib nobody sources pins nothing*.
   Apply the same discipline to the path predicates — assert that `check-unattended.sh` contains at
   least one call site of `covers`/`overlaps`. Today it contains zero, and the two-arm rule the file
   already articulates would have caught that.

---

## Highs

### H1 — the fixture named as coverage for the `id_in` repair contains no instance of what it names

**`tools/unattended/check-unattended.test.sh:1356-1368`** (arm F), against
**`tools/unattended/check-unattended.sh:1124`** (the repair) and **:1126** (the sibling filter).
*Reported four times: raw ids 3, 8, 10, 15 — two high, two medium.*

Arm F declares `ARCH-tRun-1` and `ARCH-tRun-10` through two `drow` calls. `drow`
(`check-unattended.test.sh:1275-1279`) reads `git rev-parse --short=8 HEAD` and then **commits**, so the
second row's anchor is the first row's commit and the two ids land in different dispatch groups.
The ambiguity loop is fed by `grep -F -- " dispatch · item $dsgrp "`, so each row's sibling set holds
only itself, which `[ "$dssunit" = "$dsunit" ] && continue` then skips. The repaired line is never
reached with the pair the arm exists for. Measured anchors on two independent runs: `bb7ae5e8` /
`cea01899` and `f3f5c767` / `871f7fc1`.

Proved by mutation, twice, independently: reverting 1124 to the pre-fix
`case "$(GIT log -1 --format=%s "$dshit") in *"$dssunit"*)` leaves the leg suite at
**`PASS (257 assertions)`, exit 0** — byte-identical to the shipped form. The fix at the one site
round 2 named landed with its failing case never observed, which §7 makes a landing bar.

The site is genuinely reachable and the fix is genuinely load-bearing. Built as a control — both rows
at one anchor, one commit naming only `ARCH-tRun-10` — the substring form emits
`check 23 FAILED — one commit names two passes of the same dispatch group ... ARCH-tRun-10 and
ARCH-tRun-1` on a correct run, and the shipped `id_in` form is silent. One reviewer wrote the missing
arm and measured `PASS (258 assertions)` green on the shipped form, red on the substring form.

No other fixture can reach it: `ARCH-tRun-10` appears nowhere else in `check-unattended.test.sh`,
`unattended.test.sh` or `cross-component.test.sh`, `drows` writes two rows for the **same** unit (so the
sibling loop skips both), and the same-anchor ambiguity fixture at 1396-1406 uses `ARCH-tRun-1` /
`ARCH-tRun-2`, where no substring can join the pair.

The arm's own comment names `fixture-passes-by-finding-nothing` as the failure mode it exists to
prevent, and then reproduces it one level up. Round 2's left-shift instruction was explicit —
*"extend the prefix fixture so BOTH ids are declared in one group, since the arm as shipped cannot enter
the sibling loop at all"* — and was not carried out.

**Fix.** Rewrite arm F on single-anchor emission; the `drows` helper this same pass added for arms A/B
already does exactly that, and needs only a second unit parameter. Both rows at one anchor, one commit
whose subject names only one of the ids, then `miss "$(run)" "one commit names two passes of the same
dispatch group"`. Observe it RED with the substring spelling restored before landing it.

**Left-shift gate.** Keep arm F as the `pass_commit`-window arm it actually is, and add the class gate
round 2 already prescribed: a source scan over `check-unattended.sh` that reds on any `case` or `grep -F`
whose operand is a `$ds*unit` variable. Round 2 found this site by eye and round 3 fixed it by eye; the
next one added will go the same way. Run the candidate predicate over the real tree first and print hits
and near-misses, per §7.

---

## Mediums

### M1 — the `covers` to `overlaps` change at the generated-index pairing is unarmed

**`tools/unattended/unattended.sh:2259` and `:2264`**, against
**`tools/unattended/unattended.test.sh:2380-2399`**. *Reported once: raw id 16 — medium.*

Proved by mutation: reverting **both** sites to `covers` leaves the driver suite at
**`PASS (484 assertions)`**. `GENERATED_INDEXES` is declared in exactly two places in the kit
(`unattended.test.sh:2383` and `:2394`, both `memory/LIVE.md:tools/memory-tree/gen_build_index.py`) and
every arm under them declares those **exact** paths, where `covers a b` and `covers b a` are both true
because the arguments are equal. The direction the repair added — a declaration that *contains* the
generator or the index, which is the one-way reading that let `--writes memory` through the
shared-records refusal — has no instance in any fixture. The containment block at 2405-2446 runs under
an `mkconf` that declares no `GENERATED_INDEXES` at all, so the loop is skipped there entirely.

**Fix.** None needed in product code — the change is correct. The gap is the arms.

**Left-shift gate.** One arm per direction against the declared pair: a pass declaring
`tools/memory-tree` (which contains the generator without sitting under it) alongside a sibling
declaring `memory/LIVE.md`, and a pass declaring a path under a directory-valued index entry alongside
the generator. Both must `hit` the pairing refusal; both are green under `covers`, which is what makes
them arms.

---

## Lows

### L1 — `head="$wit"` has no assertion; reverting it leaves the suite green

**`tools/unattended/unattended.sh:1320`**, against **`unattended.test.sh:1864-1881`**.
*Reported twice: raw ids 5, 18 — both low.*

Verified by deletion: replacing the line with `:` gives **`PASS (484 assertions)`, exit 0** — the same
484 the introducing commit reports. The line feeds only the two `echo`s at 1342/1344, which print
`witness $head`, and no arm reads a sha out of that message. The H7 witness fixture forces `$RUNTIP` and
`$HEADNOW` apart and then asserts `hit "$out" "anchor LOCAL"` (a substring carrying no sha) plus the
**record** via `sed -n 's/^witness: //p'`. The other local-arm fixture at 1848 runs with HEAD == RUNTIP,
so it cannot tell the two apart. A repo-wide grep for `LANDED · witness` returns only the two source
lines.

The record stays correct either way, so severity is genuinely low — but this is the run's **last
message before it hands back with no owner turn**, and the defect it repairs is the operator being told
one sha while the record keeps another.

**Fix.** None in product code.

**Left-shift gate.** In the fixture that already forces the two apart, add
`hit "$out" "witness $RUNTIP"` and `miss "$out" "witness $HEADNOW"`. Two lines, and the state they need
already exists.

### L2 — the missing-library refusal is landed unobserved in both scripts, and sits outside every armed population

**`tools/unattended/unattended.sh:61-64`** and **`tools/unattended/check-unattended.sh:43-46`**.
*Reported once: raw id 13 — low.*

The only assertions touching the wiring are two greps (`unattended.test.sh:1567` for the wrapper in the
lib, `:1569` for the driver's source line). Nothing runs either script with the library absent.
`check-arms.py`'s population regex is `\bfail (\d+) "`, so a bare `echo >&2; exit 2` is outside it by
construction, and `memory/project/unarmed-branches.txt` carries no pin for it — the branch is outside
*every* armed population, which is the one state the registry exists to prevent.

Probed behaviourally and it works: the driver copied alone into a temp dir prints its refusal and exits
2. What is unguarded is the ordering it depends on — `_LIB_DIR` is resolved from `$0` at
`unattended.sh:60` and `check-unattended.sh:42`, both above the `cd` to the repo root. An edit that
moved either below the `cd` would leave `$0`-relative resolution pointing at the repo root, and nothing
in the suite would notice.

This is also inconsistent with established practice in the same files: the sibling bootstrap refusal
*is* armed behaviourally (`check-unattended.test.sh:146`, `adopt-unattended.test.sh:194`).

**Fix.** None in product code.

**Left-shift gate.** One arm per script: copy the script alone into a temp dir, run it, assert exit 2
and the `kit library is missing beside this script` text. Three lines each, and they reach the branch
directly. Separately, either widen `check-arms.py`'s population to bare `exit 2` refusals or pin these
two rows in `unarmed-branches.txt` with their reason — a refusal outside every population is worse
than a pinned one.

### L3 — narrowing is still accepted once the pass has committed, while two binding documents say it never is

**`tools/unattended/unattended.sh:2319-2328`**, against **`PROTOCOL.template.md:354`** and
**`SKILL.template.md:227`**. *Reported once: raw id 12 — low.*

Reproduced: declare `--writes work/a --writes work/b`, commit the pass's real work naming the unit, then
`--dispatch ... --writes work/a` prints `dispatch declared` and the file carries two rows, the later one
strictly narrower. The mechanism is the openness filter doing its job — the closed row leaves `sibrows`,
`cur` is empty, and the narrowing branch is never reached.

The two claims are verbatim and unqualified: *"A re-declaration widens or no-ops; it never narrows"* and
*"narrowing is refused, because narrowing after the fact is how a write gets hidden"*. Neither document
describes the several-rows-per-unit model that would scope the claim to an open pass. No verdict is
lost — the leg still grades the original wide row and the narrow one grades as a changeless pass — but
the terminal record ends up claiming a narrower declaration than the one the pass worked under, and a
reader of the binding protocol is told a rule the driver does not enforce. Round 2 flagged the same pair
of documents as false for the moved-HEAD path.

**Fix.** Choose one: extend the refusal to every earlier row of the same unit regardless of openness, or
amend both documents to state that the rule binds while the pass is open.

**Left-shift gate.** Whichever is chosen, gate it with an arm that commits before re-declaring — the
shape neither suite covers today.

---

## Ordering note for the repair — read this first

**Fix B2 before B1, and do not put B1's filter inside `pass_commit`.**

The extraction gave one predicate three callers, and the three want different answers at the edges:

| caller | question | wants |
|---|---|---|
| `unattended.sh:2248` (`sibrows`) | has this pass committed yet? | **strict** — a bookkeeping commit must not close it |
| `unattended.sh:2296` (`cur`) | is this a re-declaration? | **strict**, but only for *this* pass kind |
| `check-unattended.sh:1095` (check 23) | which commit is this pass's? | **permissive** — it must find a commit that wrote in the wrong place |

B1 says the predicate is too permissive. B2 says it leaves rows open too long. Those are opposite
directions on one function, so the naive B1 fix makes B2 strictly worse: requiring the candidate commit
to intersect the declared set leaves *more* rows open, and every one of them is a row `cur` will
mis-read as a narrowing. Fix the `cur` key first, then tighten openness.

And the tightening must not land in the shared function. Derived by reading the leg, not measured: if
`pass_commit` itself required intersection with the declared set, a pass that committed **entirely
outside** its declaration would return no commit at all, fall into check 23's no-commit arm at
`check-unattended.sh:1096`, find that none of its *declared* paths moved, and report *"a pass that
produced no change"*. Check 23 would go green on the exact defect it exists to catch — strictly less
able to fail than it is today, which is the regression class round 2 recorded against this same check.
The intersection filter belongs in the driver's openness call site, or behind an explicit mode
parameter with both modes armed. One predicate answering three questions is the shape that produced
this round; a single spelling is right, a single *answer* is not.

---

## Not findings

- **Both `pass_commit` callers pass the right run-state path.** The driver passes `$rel` from
  `runmd_of`, the leg passes `$f` from the `git ls-files` population at `check-unattended.sh:166`, and
  both are repo-relative, which is the form `diff-tree --name-only` emits. Checked explicitly because a
  mismatch here would silently disable the run-state skip; it is correct on both sides.
- **The library's source-before-`cd` ordering is correct in both scripts.** `_LIB_DIR` is resolved from
  `$0` before either script changes directory. It is unguarded (L2), not wrong.
- **`normpath`'s slash-collapse-first ordering is correct**, and its own arm found the bug that made it
  so. Stripping `./` before collapsing turned `.//x` into the absolute `/x`. The comment recording that
  is the best thing in the diff.
- **Check 23's return to a `(group, unit)` LAST-row fold is right** — given the anchor-reuse property.
  B2 is what breaks that property, not the fold.
- **The `| while` subshell inside `sibrows` is safe.** Its body only prints; no status escapes it.
  Same for the `cur` fold.
- **The hygiene-test parity change is sound** (`check-memory-hygiene.test.sh:1331-1352`). Dropping the
  `_engassigns` subtraction and stripping comments before deriving `_engreads` both narrow the
  population in the right direction, and the exemption list is still asserted in both directions.
- **Everything in the unattended kit runs under the run's own uid.** A run with full shell access
  defeats any of it, the protocol's §9 says so, and the control that binds lives on the remote. Nothing
  here is graded on surviving a hostile run — every defect above is what an ordinary, correct-intentioned
  run produces by accident.
- **Three shipped files still attribute this sweep to unit ids of this build's family and slug that no
  spec in this tree defines.** Unchanged from round 2, still not a code defect, and still not spelled
  here: hygiene check 14 reds on a memory-side citation of an undefined id, which is why this report
  cannot name the tokens even to report them. Mint the specs or re-attribute the comments.

## What the round-3 arms actually bought

Four of the diff's new fixtures were verified by mutation to arm nothing (H1, M1, L1, and the two greps
behind L2). All four revert cleanly with the suite green at its stated count: 257 for the leg, 484 for
the driver. The commit message's claim that every new arm was observed RED against the regression it
pins is false for those four.

The arms that *do* hold — and they are the majority — are the F1 controls at `unattended.test.sh:2455`
(three shapes plus a closes-when-committed control, which is exactly the "would this filter ever close
anything" question a lesser fixture skips), the anchor-reuse arm with both of its tautology guards, and
`normpath`'s own arms. That is good fixture work. The four that fail are all the same shape: a fixture
built with a helper that commits, where the class under test needs two rows at one anchor.
