**Serves:** diff-review PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

# Diff review — the repair pass for the closing review's sixteen

**Reviewed range:** `c1b3734a34e6121e42422eff79c5a58e9819aa41...HEAD` (HEAD = `1a5a1895`, 3 commits,
26 files, +1138/-47). **ROUND: 1.**

**Review shape:** raw 24, confirmed 19, refuted 0, unverified 5, precision 1.00. The 24 raw findings
resolve to **10 distinct defects** after de-duplication — four of the ten were reported independently
by three or four lenses, which is what a narrow diff with a few load-bearing hunks produces. The five
unverified findings were re-read against the tree for this report, and every one of them collapses
into a cluster a skeptic already confirmed. None is outstanding.

## Verdict: BLOCKED

**Two blockers, four highs.** Both blockers sit in `verb_dispatch`, and between them they leave
condition 1 — the disjointness proof that is `--dispatch`'s entire reason to exist — unable to refuse
anything in the ordinary flow.

This is a repair pass, so the shape of the damage matters as much as the count. Of the ten defects,
**five are regressions this diff introduced** (F1, F2, F3, F4, F6), three are sites the sweep missed
(F5, F7, F8), and two are weaknesses in the new test arms themselves (F9, F10). Two of the regressions
are worse in kind than the defects they replaced: `check 23` is now **strictly less able to fail** than
it was at the base commit, reproduced red-at-base and green-at-HEAD on the same fixture.

The three shapes the fix commit set out to kill — status set in a subshell, an id matched as a
substring, containment tested one way — are each still live at exactly one site. In each case it is the
site the new fixture cannot reach.

---

## Blockers

### F1 — the sibling set closes a pass on its own bookkeeping commit, so condition 1 never runs

**`tools/unattended/unattended.sh:2225-2237`** (the `sibrows` openness filter; the id grep sits at
**2232**). *Reported four times: raw ids 2, 7, 12, 18 — two as blocker, two as high.*

The hunk widened the sibling set from "rows sharing this exact HEAD" to "every pass that has not
committed yet", and reads openness as: any commit in `$_g..HEAD` whose subject names the unit closes
that pass. The comment claims this is "read the same way the leg reads it". It is not. Check 23's
`dshit` loop at `check-unattended.sh:1103-1110` additionally requires the commit to touch something
other than the run-state file, under a header that says so in capitals — *A RUN-STATE BOOKKEEPING
COMMIT IS NOT A PASS COMMIT*. This loop has no such skip.

`--dispatch` stages the run-state file, and the run commits that declaration itself with the unit id in
the subject. Check 23's own header asserts exactly that, and M6 requires every pass commit to name its
unit. So the declaration's own bookkeeping commit closes the pass it declares, before the pass has
written a byte.

Reproduced end-to-end against the shipped driver, with two controls:

```
--dispatch tRun --pass ARCH-tRun-1 --writes work/shared
git commit -m "ARCH-tRun-1 declare dispatch"              # the staged RUN.md, nothing else
--dispatch tRun --pass ARCH-tRun-2 --writes work/shared   -> "unattended: dispatch declared"
```

Control A, with no commit between the two declarations, refuses correctly. Control B, with the
intervening commit subject `chore: park the run-state` not naming the unit, also refuses correctly. So
the mechanism is the openness filter and nothing else. This is the identical vacuous-selector hole the
comment at 2228-2231 says the change removes, reached through the new door instead of the old
HEAD-group key.

**Fix.** Mirror the leg exactly rather than approximately. Walk `GIT log --format=%H "$_g..HEAD"` and
close a pass only on a commit that both satisfies `id_in` on its subject **and** has non-empty output
from `GIT diff-tree --no-commit-id --name-only -r "$c" | grep -v -x -F "$rel"`. A commit touching
nothing but the run-state file must leave the pass OPEN.

**Left-shift gate.** The driver suite's condition-1 arms never commit between declarations, which is
precisely why this passed. Add an arm that commits the staged run-state file with a unit-naming subject
between two same-path declarations and asserts the refusal still fires. Stronger, and cheap: extract
the openness predicate into one place both the driver and the leg call, then assert the two agree, so
"read the same way the leg reads it" becomes a fact rather than a comment.

### F2 — `covers`/`overlaps` compare raw strings, so one trailing slash turns every containment refusal off

**`tools/unattended/unattended.sh:2162-2163`** (the helpers) and **`2176-2200`** (the `--writes`
validation loop, which normalises nothing). *Reported twice: raw ids 3 and 6 — one blocker, one high.*

`covers() { case "$2" in "$1"|"$1"/*) ...` is a literal string match. Given `memory/`, the pattern built
is `memory/|memory//*`, which matches neither `memory/DECISIONS.md` nor `memory/builds/...`. The
validation loop refuses empty, absolute, `..`, glob metacharacters and whitespace — and never
normalises a trailing slash or a `./` prefix.

Measured against the shipped driver with the shipped `SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`:

| declaration | result |
|---|---|
| `--writes memory` | refused (run-state overlap) |
| `--writes memory/` | **accepted** |
| `--writes memory/builds/tRun` | refused |
| `--writes memory/builds/tRun/` | **accepted** — and it contains the run-state file |
| `--writes ./memory/DECISIONS.md` | **accepted** — names a declared shared record outright |
| pass 1 `tools/beta/` then pass 2 `tools/beta/one.sh` | **accepted as disjoint** |

The widest declaration a pass can make sails through the very refusal whose comment at 2199-2202 says
it exists to stop, on a one-character spelling difference. All four containment sites the helpers were
introduced to unify are defeated the same way.

There is no downstream recovery, and the failure is worse than an escape. Check 23's subset test uses
the same one-way `case "$dsq" in "$dsp"|"$dsp"/*)`, so a slash-suffixed declaration cannot cover its own
writes. The leg then reds the pass for writing inside the directory it declared — a wedge with no
in-band repair.

**Fix.** Normalise before comparing, and normalise once at the argv boundary so the recorded row and the
leg's reader see the same bytes: strip repeated leading `./`, strip trailing slashes, refuse a path that
normalises to empty or `.` with its own named message, and record the normalised form in the row. Belt
and braces, make the helper defensive too:
`covers() { local a=${1%/} b=${2%/}; case "$b" in "$a"|"$a"/*) return 0 ;; esac; return 1; }`.

**Left-shift gate.** A paired-spelling arm, not a single-spelling one. For each of the four containment
refusals, assert that `X`, `X/` and `./X` all produce the SAME verdict. That shape catches the whole
class rather than the three spellings we happened to try, and it is what the existing symmetry fixtures
at `unattended.test.sh:2400-2417` should have been written as.

---

## Highs

### F3 — check 23's collapse takes the LAST row's paths with no ordering constraint, so a widening appended AFTER the commit erases the finding

**`tools/unattended/check-unattended.sh:1068-1077`**; `paths[u] = pth` is unconditional at **1075**.
*Reported three times: raw ids 1, 14, 20 — all high.*

The collapse keeps the FIRST row's anchor and the LAST row's paths. Nothing requires that last row to
predate the commit it grades. Reproduced with the suite's own `drow` helper:

```
drow ARCH-tRun-1 "work/one.txt"
commit touching work/one.txt AND work/stray.txt, subject "ARCH-tRun-1 builds its lane"
  -> check 23 FAILED — ...wrote work/stray.txt          (correct)
drow ARCH-tRun-1 "work/one.txt work/stray.txt"          (appended AFTER that commit)
  -> GREEN, no check 23 line at all
```

The identical fixture against base `c1b3734` reds in **both** states. This is the fix making the check
strictly less able to fail. Check 23 is the only mechanism binding a dispatched pass to what it declared
"before dispatch" — which is still what the failure message says, and is no longer what is graded.

The driver is no mitigation, it is an accomplice. `cur` at `unattended.sh:2275` is keyed on
`(grp, unit)`, so once HEAD has moved past the offending commit the narrowing refusal is not reached and
the widening is never compared. The driver prints a plain `dispatch declared` for what is a post-hoc
rewrite of the declaration. See F6.

This is not the "declare a wide set up front" escape the check's own header already concedes. That one
costs the run a wide declaration on the record from the start. This costs it nothing, and it is what a
sloppy-but-honest widening repair produces automatically. The ordering data needed to reject it is
already present: the widening row's own anchor is a descendant of the graded commit.

**Fix.** Bound the collapse in time. When folding rows for a unit, let a later row's paths supersede only
if that row's own group anchor is an ancestor of the commit being graded
(`GIT merge-base --is-ancestor "$g" "$dshit"`); otherwise red explicitly with "a declaration widened
after the commit it grades". The legitimate declare-then-widen-then-write repair still folds.

**Left-shift gate.** All three new arms park both rows BEFORE the pass commits, so none of them reaches
this ordering. Add the mirror arm: widen AFTER the violating commit and assert check 23 still reds. Then
stage the break and confirm RED before trusting it — the §7 rule the diff's three new gates did follow
and this one needs too.

### F4 — the collapse is keyed on the unit alone, conflating the several passes M6 allows per unit

**`tools/unattended/check-unattended.sh:1068-1077`**. *Reported once: raw id 8 — high.*

Same awk, different root cause, and this key was chosen deliberately — the fix commit's message explains
the re-key away from `(group, unit)`. M6 at `memory/guides/BUILD-METHOD.md:138` defines a pass as one of
five kinds: spec authored, spec reviewed, fixes folded, unit built, closing review. One unit therefore
owns several `--dispatch` rows at different anchors, legitimately. The collapse cannot tell a widening
repair from a genuinely new pass of the same unit, and it currently assumes the former.

Reproduced both ways against the real leg, each with a green control:

- **False RED on a correct run.** Row 1 declares `work/spec.txt`, its commit `ARCH-tRun-1 authors its
  spec` touches only `work/spec.txt`. Row 2 declares `work/build.txt`, its commit `ARCH-tRun-1 builds
  its unit` touches only that. Check 23 FAILS naming `work/spec.txt` — a path the row that governed it
  did declare.
- **Fail open.** The same shape with row 2 widened to both paths and its commit also writing
  `work/STRAY.txt`. Exit 0, no check 23 output, because the only commit ever graded is the first one and
  the second pass is never looked at. The single-row control with the same stray write reds.

**Fix.** Key the collapse on (unit, open-window) rather than on the unit: stop merging at the first row
whose unit has already been closed by a pass commit after the previous row's anchor — the same predicate
F1 asks the driver to compute. A widening repair still merges, a genuinely new pass starts a new row.
F3's ancestry constraint composes with this rather than replacing it.

**Left-shift gate.** An arm with two rows for one unit separated by a commit that names it and writes
inside the first declaration, asserting BOTH rows are graded. Pair it with the fail-open variant above,
since the false-RED case alone would be satisfied by a fix that simply stops grading the first pass.

### F5 — the ambiguity arm's sibling match is the one id test the sweep left as a substring

**`tools/unattended/check-unattended.sh:1135`**. *Reported four times: raw ids 4, 9, 15, 19 — two high,
two medium.*

```
case "$(GIT log -1 --format=%s "$dshit" 2>/dev/null)" in *"$dssunit"*) dsother="$dssunit" ;; esac
```

`id_in` is defined at 209 and used 32 lines above this, in the `dshit` loop. Grepping the file confirms
this is the **only** id comparison not routed through `id_rows`/`id_in`, directly contradicting the
helper's own header at 201-205: *"every id test in this file routes through these two"*. That header even
states the motivating relation — `TOOL-x-1` is a prefix of every `TOOL-x-1N`.

Reproduced: two rows at one anchor for `ARCH-tRun-1` and `ARCH-tRun-10`, each pass writing only inside
its own declared lane, subjects `ARCH-tRun-1 builds its lane` and `ARCH-tRun-10 builds its lane` —

> check 23 FAILED — one commit names two passes of the same dispatch group ... ARCH-tRun-10 and ARCH-tRun-1

The commit names one pass. The `ARCH-tRun-2`/`ARCH-tRun-3` control with the identical shape is green, so
it is the prefix relation and not the fixture. This build's own roster runs past `-19`, so a `-1` and a
`-1N` in one dispatch group is an ordinary pairing. It is a false RED on a correct run, naming the wrong
reason, with no in-band repair.

It reds at base `c1b3734` too, so this is a missed site in the sweep rather than a regression — which
makes F9 its direct cause.

**Fix.** `id_in "$(GIT log -1 --format=%s "$dshit" 2>/dev/null)" "$dssunit" && dsother="$dssunit"`.

**Left-shift gate.** Two layers. First, extend the prefix fixture so BOTH ids are declared in one group,
since the arm as shipped cannot enter the sibling loop at all (F9). Second, gate the convention the
header asserts: a `check-arms`-style scan over `check-unattended.sh` that reds on any `case` or `grep -F`
whose operand is a `$ds*unit` variable, so the next hand-spelled id test cannot land. Run the candidate
predicate over the real tree first and print hits and near-misses, per §7.

### F6 — the re-declaration rule is still keyed on `$grp` while the leg was re-keyed on the unit

**`tools/unattended/unattended.sh:2275`**. *Reported once: raw id 13 — high.*

```
cur=$(grep -F -- " dispatch · item $grp $unit · reason " "$rel" 2>/dev/null | tail -1)
```

`$grp` is the current short HEAD. The consuming leg was re-keyed on the unit alone in this same diff
(F4), and the fix commit's own message explains why: a widening after ANY commit sees a moved HEAD. The
driver's guard was not re-keyed to match. Once HEAD moves, the guard finds no `cur`, the narrowing
refusal cannot fire, and a narrower re-declaration is silently appended as a fresh row.

Reproduced: declare `--writes tools/a.sh tools/b.sh`, make one unrelated commit, re-declare
`--writes tools/a.sh` — output is `unattended: dispatch declared` and a second, narrower row lands at a
different anchor. With HEAD unmoved the same narrowing is correctly refused.

Two binding documents are now false: `PROTOCOL.template.md:355` ("A re-declaration widens or no-ops; it
never narrows") and `SKILL.template.md:227` ("narrowing is refused"). And `check-unattended.sh:1068`'s
header calls the last row "the WIDEST declaration", an invariant nothing enforces once this guard is
unreachable. The fix's own comments assert that a moved HEAD is the ordinary case, not a corner one.

**Fix.** Key `cur` on the unit alone, matching the leg:
`cur=$(grep -E -- " dispatch · item [0-9a-f]+ $unit · reason " "$rel" | tail -1)`. Keep `$grp` only for
the row this call writes.

**Left-shift gate.** The existing re-declaration arms never commit between declarations. Add one that
does, asserting the narrowing is still refused. Then add a driver-side assertion that the last dispatch
row for a unit is a superset of every earlier one, so "widest declaration" is checked rather than
asserted in a comment.

---

## Mediums

### F7 — the generated-index/generator pairing is the one containment site left one-directional

**`tools/unattended/unattended.sh:2245` and `2247`**. *Reported four times: raw ids 5, 10, 16, 23 — all
medium.*

Both halves ask `covers`, meaning "is the declared path at or under" — while the sibling-intersection and
shared-record sites in the same function were converted to `overlaps` by this diff. A declaration that
CONTAINS the index, or CONTAINS the generator, therefore escapes the one pairing M6's condition 3 forbids.

Reproduced against this repo's own `GENERATED_INDEXES`:

- `--writes memory/LIVE.md --writes tools/memory-tree/gen_build_index.py` — refused, correct.
- `--writes memory/LIVE.md --writes tools/memory-tree` — **accepted**, and that directory holds the generator.
- `--writes memory/ledger --writes tools/memory-tree` — **accepted**.

With `GENERATED_INDEXES="docs/generated/index.md:tools/gen.py"` and `SHARED_RECORDS=""`, the
container-of-the-index side reproduces too: `--writes docs/generated --writes tools/gen.py` is accepted
where the exact pair is refused.

Declaring a kit directory is the natural spelling for a pass touching that kit — the suite itself declares
`tools/beta` as a directory. So the refusal is bypassed by WIDENING rather than narrowing, which is
verbatim the sentence this same commit wrote for the shared-records site, and the class the record
`memory/gotchas/containment-tested-one-way.md` it added describes. In this repo it is partly masked
because `SHARED_RECORDS` refuses a container of `memory` first. An adopter whose index sits outside its
shared records has no such cover, and `.unattended.conf.example` ships both keys.

**Fix.** `overlaps "$idx" "$p"` and `overlaps "$gen" "$q"`. The refusal message already names `$idx` and
`$gen`, so it stays readable.

**Left-shift gate.** The symmetry arms at `unattended.test.sh:2400-2417` cover the run-state and
shared-records sites only. Rewrite them as a table driven over all four containment sites, asserting
exact / container / contained all refuse at each. That is the arm that would have caught this and F2 in
one go.

### F8 — `--landed`'s local arm prints a witness the record does not carry

**`tools/unattended/unattended.sh:1331`**, and `1329` for consistency. *Reported three times: raw ids 11,
17, 22 — one low, two medium.*

`head` is set once at 1248 and never reassigned. The fact is written from `wit` at 1304, where
`[ "$akind" = local ] && wit="$rbtip"` — that is the correct half of the fix. The local-arm report at 1331
still interpolates `$head` under the literal label `witness`.

On the local arm the two differ by construction. The fix's own comment at 1297-1301 says they differ
"exactly when the worktree has moved on since the merge — which is the ordinary case", and the new H7
fixture at `unattended.test.sh:1861-1873` FORCES `RUNTIP != HEADNOW`. So on exactly the fixture the fix
added, the terminal line reports a sha no later reader of the record will find. Reproduced: printed
`witness a590167…` (= `$head`) against recorded `witness: a321aff…` (= `$rbtip`).

Two answers to one question, in the one message a no-owner run leaves behind. State-correct,
report-wrong, which is why it is a medium and not a high.

**Fix.** Use `$wit` in both echoes. It equals `$head` on the remote arm, so the change is safe there.

**Left-shift gate.** The H7 arm asserts the recorded fact and the `anchor LOCAL` string, never the printed
sha — which is why the sweep that fixed the record missed the message. Add `hit "$out" "witness $RUNTIP"`
beside the existing `same` on the fact. Then generalise: for every terminal verb, assert the printed sha
and the recorded sha are the same bytes.

### F9 — the new prefix arm cannot fail

**`tools/unattended/check-unattended.test.sh:1334`**, the H3/H4 "a NARROWER unit id is not confused with a
wider one" arm. *Reported once: raw id 21 — medium.*

Reproduced by reverting the anchoring. I copied the kit to a scratch dir, restored
`check-unattended.sh:1103` to `case "$(GIT log -1 --format=%s "$dsc")" in *"$dsunit"*)`, and ran the arm's
exact fixture in isolation: `drow ARCH-tRun-10 "work/ten.txt"`, commit `ARCH-tRun-10 builds its lane`,
`miss "check 23 FAILED"`. Green under both the anchored and the un-anchored leg, `assertions=1 st=0` each
time.

The fixture declares only the LONGER id, so no shorter id exists for a substring match to over-reach. The
arm's verdict is independent of the anchoring it claims to pin. This is `fixture-passes-by-finding-nothing`
from the project's own class list, and it is the direct reason the surviving substring site at F5 went
unnoticed by an otherwise thorough sweep — the sweep converted the heredoc source at 1135 and left the
`case` beside it.

**Fix.** Put BOTH ids in the fixture: one dispatch group carrying `ARCH-tRun-1 · work/one.txt` and
`ARCH-tRun-10 · work/ten.txt`, each with its own commit, asserting `miss "$(run)" "check 23 FAILED"`.
Verify the arm goes RED with the anchoring reverted before landing it.

**Left-shift gate.** This is §7's "a new gate is not landed until its failing case has been observed",
applied to a test ARM rather than a gate leg — the diff's three new gates did observe RED, this arm did
not. Extend `check-arms`, or add a sibling, to flag an arm whose fixture contains no instance of the class
it names. A cheap approximation with real reach: an arm asserting `miss` on a failure string must be
paired, in the same fixture, with a positive control asserting `hit` on it.

---

## Low

### F10 — the example-conf parity arm exempts a live adopter key

**`tools/memory-tree/check-memory-hygiene.test.sh:1332-1350`**. *Reported once: raw id 24 — low.*

The arm subtracts `_engassigns` from `_engreads` on the stated rationale that self-assigned names are
"internals, not overrides". `comm -12` over the arm's own two derivations yields exactly one name,
`SPEC10_CUTOFF`, and it is a live counterexample: `check-memory-hygiene.sh:33` gives it a shipped default,
line 51 sources `.memory-tree.conf` on top of it, line 54 resolves blank forward. It is a conf-overridable
adopter key, declared at `.memory-tree.conf.example:44`. It reaches `_engreads` at all only because the
pattern matches comment prose at `check-memory-hygiene.sh:684` — the derivation reads comments.

No harm today, since the key IS declared. But the arm exists because two cutoff keys reached the engine and
never reached the example, and a third key written in the `SPEC10_CUTOFF` idiom would escape it the same
way. That is the exact failure the arm was added to prevent.

**Fix.** Drop the `_engassigns` subtraction. Require every `${NAME:-}` / `${NAME:=}` read not in
`_engexempt` to appear in the example, running the grep over comment-stripped source. `SPEC10_CUTOFF` then
reds only if the example stops declaring it, which is the intended behaviour.

**Left-shift gate.** The arm already asserts its exemption list in both directions, which is the right
instinct — extend the same discipline to the subtraction: assert that the `_engreads` minus `_engassigns`
difference is EMPTY, so a name silently dropped from the parity requirement reds instead of vanishing.

---

## Not findings

- **Every check here runs under the run's own uid.** A run with full shell access can defeat any of them.
  The protocol says so explicitly in its §9, and the control that binds lives on the remote. What these
  checks buy is catching a run that is wrong, not one that is malicious, so nothing in this report is
  graded on whether it survives a hostile run. F1, F2, F3 and F6 all matter under the honest reading:
  each is what an ordinary, correct-intentioned run produces by accident.
- **check 22's repair is sound.** The bare `GIT` to `git` fix, the hoisted listing routed through
  `pop_guard`, and the `- **AC1**` flattener all check out. The empty listing now reds where it previously
  printed a notice and exited 0.
- **The `| while` to `for` conversion is correct.** `fail` in a pipeline subshell set a status the parent
  never saw; the `for` form fixes it, and `memory/gotchas/status-set-in-a-subshell.md` captures the class.
  The surviving `| while` inside `sibrows` at `unattended.sh:2225` is safe — its body only prints — but it
  is worth one comment line saying so, since the next reader will stop to check.
- **Three shipped files attribute the sweep to a `…-21` unit id of this build's own family and slug**
  (`check-unattended.sh:202`, `unattended.sh:2161`, `unattended.test.sh:2400`). No spec in this tree
  defines it and the build README's roster stops at `-19`. Not a code defect, so it is not numbered here.
  It is, however, why this report's `Serves:` line cannot claim it: hygiene check 14 reds on a memory-side
  citation of an undefined id, so this bullet deliberately does not spell the token either. Mint the spec
  or re-attribute the comments; the code-side citations are outside check 14's corpus today, which is the
  only reason the bar is currently quiet about them.

## Ordering note for the repair

F1 and F6 both want the same predicate — "has this pass committed yet?" — and F4 wants it a third time
inside the leg. Extract it ONCE and have all three call it, rather than fixing three sites to agree by eye.
Fixing them separately is what produced this round: the fix commit wrote the leg's rule and the driver's
rule independently, asserted in a comment that they matched, and they did not.
