**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 4 (the fold of round 3's eleven)

**Range:** `70fda314728320717a60dca9587992234f02d90f...376c2c63` — two commits, `c46b5681`
(round-3 findings 4, 5, 6) and `376c2c63` (the rest). 15 files, 1020 insertions, 81 deletions.
**ROUND 4.**

**Review shape:** raw 26 · confirmed 22 · refuted 4 · unverified 0 · precision 0.85. The 22
confirmed findings collapse to **9 distinct defects**; five clusters were found independently by
two to four lenses each, and that corroboration is recorded per defect rather than inflating the
count. Every mechanism below was re-reproduced against the working tree by the synthesis pass
before it was written down.

## Verdict: BLOCKED

Three blockers, two highs, four mediums.

**The standing pattern held for a fourth round, and it now has a second form.** Rounds 1–3 each
broke on the previous round's blocker restored by the commit that fixed it, one abstraction level
up: no join, then wrong parser, then `head -1` — and now, in this fold, **a terminator test placed
one `sed` stage too early**. The consolidated `declared_list` grew exactly the refusal round 3 asked
for, and it tests the RAW line before the comment strip. So the plain multi-line array it was
written to catch is refused, and a multi-line array whose opening line carries a bracketed comment
sails through to the declared null. The new test arm and check 28's new multi-line specimen both use
the comment-free form. That is the fourth consecutive round in which the repair reintroduced its own
defect one level up (**BLOCKER 1**).

The second form is new and worse: **a fix that was recorded as landed and does not exist in the
tree.** `git show 70fda314:tools/unattended/check-playbook.sh` line 100 and
`git show 376c2c63:tools/unattended/check-playbook.sh` line 108 are byte-identical, while
`376c2c63`'s message lists round-3 MEDIUM 8 among the folded findings and spec 5 rev-9 — changed by
that same commit — records the pin as shipped. The code and the record are two answers to one
question, and the question is the guard on the one Definition-of-Done item that takes no override
(**BLOCKER 3**).

Two of the three blockers land on `pieces-complete` and one on `set-checks-recorded`. Two of them
are the same failure of a claim — "every reader treats the refusal as a red", "`GITSHOW` reads the
blob under the same pins" — asserted in a commit message about code that does not do it.

**The full bar is 92/92 green over this diff.** Everything below is something 92 legs certified.

### Checklist classes hit (`python tools/memory-tree/gotchas.py --for-diff 70fda314..HEAD`)

`fixture-passes-by-finding-nothing` — findings 5 and 8.
`two-answers-to-one-question` — findings 3 and 9.
`inputs-inside-the-subjects-reach` — finding 3.
`containment-tested-one-way` — finding 5.
`assertion-between-two-derived-values` — finding 6, in the arm rewritten this round to remove it.
`second-implementation-is-not-a-second-opinion` — findings 1, 4 and 7, the ad-hoc reads left beside
the consolidated parser.

---

## BLOCKER 1 — the unterminated-array guard tests the line before the comment is stripped

**`tools/unattended/check-playbook.sh:144`**, and its byte-identical copy at
**`tools/unattended/unattended.sh:2356`**.
*Found by one lens; reproduced end to end by the synthesis pass.*

`declared_list` selects the raw line, then runs its terminator `case` on that raw text:

```sh
raw=$(printf '%s\n' "$1" | sed -n "s/^$2[[:space:]]*=[[:space:]]*//p" | head -1)
case "$raw" in
  *'['*']'*) ;;
  *'['*) return 2 ;;
esac
```

A `]` anywhere in a trailing comment on the opening line satisfies the first arm. The comment strip
runs one line later, reduces the value to a bare `[`, and the bracket strip reduces that to the
empty string — **rc 0, zero members, the DECLARED NULL.**

Measured against the shipped parser body:

```
piece_checks  = [   # one per piece [see section 7]   ->  rc=0  members=[]
piece_checks = [                                     ->  rc=2  members=[]
```

A declared null means "this playbook declares no per-piece checks", so the `miss_` loop at
`check-playbook.sh:329-336` becomes a no-op, every piece that hash-joins and carries no FAIL
increments `v`, `_xc` stays 0, and **`pieces-complete` returns MET** — the item `unattended.sh:184`
puts in `DOD_NO_OVERRIDE`, so no waiver is recorded and none is needed. With every `leg … · verdict
…` row deleted from both fixture records, the census still prints
`pieces 2 · verified 2 · failed 0 · stale 0 · unrecorded 0 · unchecked 0`.

No attacker is required. A bracketed cross-reference in a comment is ordinary TOML authoring, and
the kit's own template puts a trailing comment on every declaration line. The plain multi-line form
correctly refuses, which is exactly why the new suite arm at `check-playbook.test.sh:243` and check
28's new multi-line specimen at `check-unattended.sh:1485` both pass.

**Fix.** Strip the trailing comment BEFORE the terminator test, in both copies byte-identically:

```sh
raw=$(printf '%s\n' "$1" | sed -n "s/^$2[[:space:]]*=[[:space:]]*//p" | head -1 \
      | sed 's/[[:space:]][[:space:]]*#.*$//')
```

then run the existing `case "$raw"` and drop the now-redundant strip from the pipeline below.

**Left-shift gate.** Add a check-28 specimen `k = [   # note [x]` with an expected rc of **2**, and a
`check-playbook.test.sh` arm using a fixture whose multi-line `piece_checks` opening line carries a
bracket-bearing comment. Both must be staged RED before re-arming: the existing arms cover only the
comment-free multi-line form, which is why 92 legs were green over this.

---

## BLOCKER 2 — `set-checks-recorded` discards the rc 2 the fold added, and grades MET

**`tools/unattended/unattended.sh:2135`**
*Found independently by four lenses; reproduced by executing the shipped parser body.*

Commit `376c2c63`'s message states that the new refusal is honoured because "every reader treats the
refusal as a red", and spec 7 rev-9 states that `set_checks` inherits the parser refusal because one
parser meant one fix. The parser has three readers. Two of them branch on the status:

```sh
check-playbook.sh:282   if ! pchk=$(declared_list "$body" piece_checks); then …
check-playbook.sh:365   if ! schk=$(declared_list "$body" set_checks);   then …
```

The third does not:

```sh
unattended.sh:2135   _declared=$(declared_list "$_blob" set_checks)
unattended.sh:2139   case "$_declared" in
                       ''|none|'none '*|none[!A-Za-z0-9-]*) DOD_OUT=""; return 0 ;;
```

`unattended.sh` sets `set -u` only (line 38), so nothing aborts. Executed against the shipped body,
`set_checks = [` with its members on following lines returns **rc 2 with empty stdout**. `_declared`
is therefore empty, the `''` alternative matches first, and the item returns 0 with `DOD_OUT=""`.
The refusal is converted straight back into "this playbook declares nothing".

The consequence is the one HIGH 3 was graded on. The set record is never opened, its FAIL rows are
never read, the set-identity comparison below is skipped, **no `--override` entry is written and no
line reaches the report**. The population the spec says a per-piece review structurally cannot see
goes ungraded and silent.

The leg is not a backstop, and that matters because it looks like one. Its own `set_checks` refusal
at `:365` is nested inside `if [ -n "$gr" ] && [ -n "$rr" ]`. The machine `pieces=` line is printed
at `:350`, BEFORE it. And `unattended.sh:2065-2066` captures the leg's whole output and then greps
only `^pieces=`, discarding the leg's exit status entirely. So a `--counts` run that printed a census
AND refused arrives at the close as a clean census.

**Fix.** Mirror the two leg call sites, before the `case`:

```sh
if ! _declared=$(declared_list "$_blob" set_checks); then
  DOD_OUT="the playbook at the pinned BASE opens a set-scoped check list it does not close on the same line, so this item would read the declared null and certify set coverage over a declaration nothing could parse: $_pb"
  return 1
fi
```

While there, check the leg's exit status at `:2065` rather than discarding it. A run that printed a
census and a FAILED line is not a clean census.

**Left-shift gate.** A `unattended.test.sh` arm on the `tDoD` fixture committing a multi-line
`set_checks` at BASE and asserting `--close` blocks. Stronger and cheaper: extend check 28 to grep
every `declared_list` and `declared_scalar` call site in both scripts and red on any whose result is
not consumed under an `if !` or an explicit `|| return`. Three call sites needed one rule, two got
it, and nothing counted them.

---

## BLOCKER 3 — round-3 MEDIUM 8's fix never landed, and three records say it did

**`tools/unattended/check-playbook.sh:108`**
*Found independently by four lenses; reproduced in a scratch repo.*

```sh
GITSHOW() { git show "$1" 2>/dev/null | tr -d '\r'; }
```

Plain `git show`. `check-playbook.sh` sources no lib, defines no `GIT()` wrapper, exports no
`GIT_GRAFT_FILE`, and pins no `core.useReplaceRefs` — grep finds none of the four in the file, unlike
`check-unattended.sh:37` and `unattended.sh:59` / `lib-unattended.sh:20`. It is the only sha
dereference in the leg, and `git show 70fda314:…` line 100 is byte-identical to `git show
376c2c63:…` line 108: **the commit that lists MEDIUM 8 as folded touches no `GITSHOW` line.**

The lever works. Measured in a scratch repo with `git replace -f <base> <forged>` installed:

```
git show $A:f.txt                              -> SUBSTITUTED
GIT_GRAFT_FILE=/dev/null git show $A:f.txt     -> SUBSTITUTED
git -c core.useReplaceRefs=false show $A:f.txt -> ORIGINAL
```

`dod_met` spawns the leg as a child at `unattended.sh:2065`, so the child inherits the exported
`GIT_GRAFT_FILE=/dev/null` and NOT the per-invocation `-c core.useReplaceRefs=false` that `GIT()`
applies. A `-c` is per-git-invocation and nothing propagates it. The driver's own header at
`unattended.sh:52-55` records exactly this: the graft pin alone leaves replace refs fully effective.
`check-playbook.sh:177` (`body=$(GITSHOW "$COUNTS_AT:$pb")`) is the single read producing every
declaration the `--counts` census grades, and that census is the sole evidence for
`pieces-complete`. End to end against the fixture, one `git replace -f` flipped the census at the
unchanged honest sha from `pieces=2 verified=0 unchecked=2` to `pieces=2 verified=2 unchecked=0`.

So **the run supplies the playbook it is graded against, on the item it cannot override.** The
committed BASE blob is one of only two inputs the security model places outside the subject's reach;
one `git replace`, touching no tracked byte, puts it back inside.

The tripwires do not close it and are not claimed to. Driver check 23 refuses at `--preflight`.
`check-unattended.sh` check 14 reads `refs/replace` at bar time, and its own comment says the run can
add one at any moment. Create-after-preflight, delete-before-push slips between both while the
close's verdict is already written.

The record disagreement is a defect in its own right: `376c2c63`'s message, spec 5 rev-9 and the
acceptance ledger's round-3 paragraph all assert a pin that is not in the tree.

**Fix.**

```sh
export GIT_GRAFT_FILE=/dev/null    # near `set -u`
GITSHOW() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false show "$1" 2>/dev/null | tr -d '\r'; }
```

Correct spec 5 rev-9 and the ledger either way — they currently record a fix that did not land.

**Left-shift gate.** Two, because the missing arm is how this got signed off. First, extend check
28's awk extraction to cover the `GIT` and `GITSHOW` definitions in both scripts, so any sha
dereference in this kit that is not routed through a pinned wrapper reds. Second, a
`check-playbook.test.sh` arm that stages a `git replace -f` and asserts the pinned read is unmoved —
staged RED against the current tree before re-arming, which is precisely what round 3 asked for and
what this fold skipped.

---

## HIGH 4 — `AUTH_OUTPUTS` was left ad-hoc in the block the fold consolidated

**`tools/unattended/unattended.sh:944`**, guard at **`:952`**.
*Found independently by three lenses; measured against the shipped template.*

The fold moved `grain` and `records` onto `declared_scalar` and left the line above them alone:

```sh
944  AUTH_OUTPUTS=$(printf '%s\n' "$_pb" | sed -n 's/^outputs[[:space:]]*=[[:space:]]*//p' | head -1)
945  AUTH_GRAIN=$(declared_scalar "$_pb" grain)
946  AUTH_RECORDS=$(declared_scalar "$_pb" records)
```

No comment strip, no trim — and the guard at `:952` string-compares that raw text against `''|'[]'`.
The shipped `PLAYBOOK-TEMPLATE.template.md:45` line is:

```
outputs      = []    # globs. Where pieces land. A `recipe`-mode run's diff may touch
```

The parsed value, verified with `cat -A`, is the whole remainder of that line, comment and all:

```
[]    # globs. Where pieces land. A `recipe`-mode run's diff may touch
```

That matches neither alternative, so **`fail 46` never
fires**. An adopter who copies the shipped template and never fills `outputs` is authorized for a
recipe-mode run declaring no output globs — exactly the state the refusal's own message says leaves
the scope refusal with nothing to compare against. A multi-line `outputs = [` array evades it
identically via the bare `[`.

This is round-2's M1 — the escape matched against a trimmed value, while the line the kit's own
template ships does not equal `[]` — restored one key over, inside the three-line block this commit
edited. It sits on the authorization path behind `authorization-reachable`, the other member of
`DOD_NO_OVERRIDE`.

There is no second gate. `grep -n AUTH_OUTPUTS tools/unattended/*.sh` returns only `:357`, `:944`
and `:952`, and `outputs` has no consumer in either check script because unit 8 is withdrawn, so
this refusal is the whole machine consequence of the key. The only negative fixture,
`content/pb-noout.md` at `unattended.test.sh:197`, OMITS the key entirely — it exercises the `''`
half, and the `[]` half has never been observed to fire.

Check 28 makes it look covered: its list loop selects `^[a-z_]+[[:space:]]*=[[:space:]]*\[`, matches
`outputs`, and feeds it to `declared_list` — a parser this consumer does not use.

**Fix.**

```sh
if ! AUTH_OUTPUTS=$(declared_list "$_pb" outputs); then
  fail 46 "the playbook at the pinned BASE opens an output-glob list it does not close on the same line…"
  return 1
fi
case "$AUTH_OUTPUTS" in '') fail 46 "…declares no output globs…"; return 1 ;; esac
```

A correctly parsed `[]` is already the empty string, so the `'[]'` alternative goes with the ad-hoc
read.

**Left-shift gate.** Two fixtures — `outputs = []` carrying the template's own trailing comment, and
a multi-line `outputs = [` — each asserting check 46 speaks. Then the structural one that would have
caught findings 1, 4 and 7 at once: a check-28 assertion binding **each declaration key to the parser
its real reader calls**, so a key certified through `declared_list` while its consumer reads it with
`sed` reds.

---

## HIGH 5 — check 28's scalar half asserts only a negative, so a parser that answers nothing scores correct

**`tools/unattended/check-unattended.sh:1523`**
*Found independently by three lenses; reproduced by execution.*

The scalar loop at `:1516-1527` asserts exactly two things: `rc -ne 0`, and `case "$got" in *'#'*)`.
Both are negatives. `declared_scalar` ends in a `sed` pipeline that exits 0 for every input, so the
rc arm **cannot fire on a semantically dead parser**; and every value in the shipped fence is a
declared null, so the `#` arm cannot fire on one either.

Measured, running the loop verbatim over the shipped template's fence with `declared_scalar` gutted
to `printf ""`: **7 keys visited, 0 failures, check green.** Sharper still, swapping the
comment-strip `sed` for `sed '/#/d'` in both copies — which makes every declaration carrying a
trailing comment parse to EMPTY, the mirror image of the HIGH 6 defect this arm exists to cover —
leaves `check-unattended.sh` green, `check-playbook.sh` green and `check-playbook.test.sh` green at
72/72.

The `ds_a`/`ds_b` byte-compare gives no protection: two identically dead copies are still identical,
and `[ -z "$ds_a" ]` only catches a missing function. Nothing else in the kit covers it either. The
fixture playbook carries no trailing comment on any declaration line (`playbook.fixture.md:9-18`),
so the shipped template read by this arm is the ONLY input in the kit that exercises the comment
strip at all.

This is round-3 HIGH 4's finding against the list half, reproduced in the arm the same commit added
for the sibling parser. The list half got the right treatment here — three specimens with expected
non-empty answers at `:1469`, an exit-status assertion at `:1471`, and an rc-2 specimen at `:1489`.
The scalar half got none of the three. The suite matches, carrying `gut_parser declared_list "
printf ''"` at `check-unattended.test.sh:1442` and, for the scalar sibling, only the
unexecutable-body arm at `:1455`. The loop's own comment notes it has no specimens of its own,
without noticing that the answer assertion is therefore untestable.

**Fix.** Give the scalar half the two directions the list half has: a `ds_run` helper, fixed
specimens with expected NON-EMPTY answers (`k = "v"   # note` to `v`, `k = 0` to `0`, `k = {}   #
note` to `{}`), and an exit-status assertion. Keep the `#`-leak case as an additional assertion
rather than the only one, and set `dlk_builtin` after them.

**Left-shift gate.** `reset_tree; gut_parser declared_scalar "  printf ''"` in
`check-unattended.test.sh`, asserting the new positive failure text. Observe RED before re-arming —
today that mutation is silent.

---

## MEDIUM 6 — one liveness counter for two independent loops, so either half can go dark

**`tools/unattended/check-unattended.sh:1538`**
*Found independently by two lenses.*

```sh
[ "$dlk" -gt "$dlk_builtin" ] || fail 28 "the shipped template's declaration block yielded no key this check could parse…"
```

`dlk_builtin` is stamped at `:1491` after four built-in specimens, and **both** template loops then
increment the same `dlk`. Counting the shipped fence: the list awk matches 3 keys, the scalar awk
matches 7. Either half alone satisfies the assertion. Measured: replacing the scalar loop's
population awk at `:1528` with one that matches nothing leaves the check green at rc 0 with zero of
the seven scalar keys parsed, while the failure text still claims the template half covered
something.

That is round-3 HIGH 6 restored one level up. The population is now derived, and the assertion that
says the derivation found anything cannot see one of the two halves going empty. The comment's own
justification, that what is worth asserting is that the template half RAN, is true of the union and
false of either half. The only suite arm for it indents ALL keys, killing both loops together, so no
fixture distinguishes them.

Related, in the same block: the list loop at `:1496` deliberately drops `rc` under a comment saying
such a branch could be reached by no fixture. A template list key written multi-line reaches it
exactly — rc 2, empty stdout, `[ -n "$got" ]` false, silent pass. That matters because
`check-playbook.sh:80` excludes `PLAYBOOK-TEMPLATE.template.md` from its population, making check 28
the ONLY grader of the shipped template's declaration lines. A template edit the driver would
mis-parse into MET (BLOCKER 2) is blessed green by its sole grader.

**Fix.** Count the loops separately as `dlk_list` and `dlk_scalar`, and assert each is greater than
zero with its own refusal naming which half covered nothing. Restore an rc branch in the list loop
that fails when the shipped template's own declaration is refused by the parser.

**Left-shift gate.** Neuter one population awk at a time and observe RED for each. The existing
all-keys indent mutation cannot tell them apart and must not be the arm.

---

## MEDIUM 7 — `step_floor` splices comment digits into the floor

**`tools/unattended/check-playbook.sh:192`**
*Found independently by two lenses.*

```sh
flo=$(printf '%s\n' "$body" | sed -n 's/^step_floor[[:space:]]*=[[:space:]]*//p' | head -1 | tr -dc '0-9')
```

This is the one fence key the fold left on an ad-hoc pipeline. Every sibling moved to
`declared_scalar` — `:187` curated, `:191` step_selector, `:228` coverage, `:277` grain, `:278`
records — and that helper strips the comment first. `tr -dc '0-9'` instead concatenates every digit
in the trailing comment into the number. Measured:

```
step_floor    = 3     # at least 3, per section 5 and F2   ->  3352
step_floor =    # TBD 5                                    ->  5
```

The first direction reds check 3 on a valid playbook with "matched, floor and playbook follow: 6
against 3352" — a true refusal for a false reason, this kit's own recorded class, naming a floor the
author never wrote and cannot find in their file. The second is a false green: it bypasses the
`[ -z "$flo" ]` "declares no floor" refusal at `:201`, which is the guard against a selector that
quietly matches nothing, and invents an undeclared floor. The shipped template survives today only
because its own `step_floor` comment happens to carry no digits, which is luck rather than coverage.

Check 28's scalar population is derived from the fence and includes `step_floor`, so the gate
certifies comment-stripping through `declared_scalar` for a key whose only real reader never calls
it.

**Fix.** `flo=$(declared_scalar "$body" step_floor)`, then refuse a non-numeric value explicitly with
`case "$flo" in ''|*[!0-9]*) fail 3 "…declares a non-numeric step floor…" ;; esac`, instead of
laundering arbitrary text through `tr -dc`.

**Left-shift gate.** A `check-playbook.test.sh` arm with a digit-bearing comment on the floor line,
asserting the parsed floor. Covered structurally by HIGH 4's key-to-parser binding gate.

---

## MEDIUM 8 — the round-3 replacement arm passes when the tree read produces nothing

**`tools/unattended/check-playbook.test.sh:234`**
*Found independently by two lenses; reproduced by perturbing the scratch tree.*

```sh
case "$PIN1" in *"verified=0"*) [ "${TREE1#*verified }" != 0 ] || bad "…" ;; *) bad "…" ;; esac
```

The pinned half carries an explicit refusal; the tree half does not. `TREE1` is captured at `:229`
from `check-playbook.sh | grep -oE 'pieces [0-9]+ · verified [0-9]+' | head -1`, with the pipeline's
exit status unchecked. With `TREE1` empty, `${TREE1#*verified }` finds no match and yields the empty
string, `[ "" != 0 ]` is **true**, and the arm goes green having compared one number against
nothing.

Reproduced: deleting `step_selector` in the WORKING TREE only, which hits check 3's fail-and-continue
at `:195` and leaves the pinned read unaffected, gave `TREE1=''` with `PIN1` unchanged at
`verified=0` — and the arm PASSED. Four code paths suppress the census note: `:195`, the new
`piece_checks` rc-2 continue at `:286`, the `[ -n "$gr" ] && [ -n "$rr" ]` guard at `:295`, and the
DEAD-PROBE branch at `:352`. The capture greps free-text prose that nothing pins, so a wording change
empties it silently, and `bad()` at `:17` sets `st=1` without exiting, so nothing upstream halts
first.

It is live today with `TREE1='pieces 2 · verified 2'`, which is exactly the state that makes it
invisible. This is the sole behavioural regression gate for round-2 blocker B2 and round-3 HIGH 5,
and half of its comparison degrades to a pass rather than a refusal —
`fixture-passes-by-finding-nothing`, from the project's own checklist, in the arm rewritten this
round to remove it. It is also inconsistent with the file's own discipline two lines up, where `PIN0`
is asserted against an exact literal that fails loudly on any format change.

**Fix.** Refuse an unreadable tree read before comparing:

```sh
case "$TREE1" in
  'pieces '*' · verified '*) ;;
  *) bad "the tree read produced no census line, so this arm compared the pinned read against nothing: [$TREE1]" ;;
esac
```

then compare the extracted count numerically with `-ne 0`.

**Left-shift gate.** The class, not the instance: a suite-wide convention that every capture feeding
an assertion is shape-asserted before use. The cheap mechanical form is a `require_shape` helper in
the leg suite, plus a grep arm redding on any `$( … | grep -oE …)` whose result reaches a `[ ]` test
with no preceding shape guard.

---

## MEDIUM 9 — the seven kickoff fork rulings were deleted, and the prose still cites them by number

**`memory/builds/dScriptedRepeat/README.md:60`**
*Found by one lens; verified in git.*

Commit `4946d7d0` removed the whole seven-row ruling table and replaced it with a two-sentence stub:
the reasoning is in the kickoff record and the specs that cite them, **kept as a list because a
fork's RULING is not derivable from the thing it ruled on** — while keeping no list.

The kickoff record does not exist. `git show --stat 0d88d5f2`, the kickoff commit whose subject is
"seven forks owner-ruled", touched only `LIVE.md`, `backlog/TOOL.md`, the ledger and `README.md`
itself. The rulings were written INTO the README that later deleted them, and there is no kickoff
record under `build/`, `spec/` or `reviews/`. `grep -rn "kickoff record"` matches only the new
sentence.

The dangling references survive in the same document. Line 84 refers to a ruling that "buys a fifth
KIND" for fork 6, line 86 to "instances of fork 5's own defect", line 91 to "the seven kickoff forks"
being ruled before evidence, and line 102 to "what fork 1's 'ONE gate' means" — while forks 8 through
11 immediately below are still spelled out in full. The document defines 8-11 and cites 1, 5 and 6
with no definition anywhere in the tree. None of round 3's eleven findings asked for this deletion,
and it removes exactly the non-derivable content the sentence replacing it says must be kept.

**Fix.** Restore the seven-row ruling table, or move it verbatim into a `build/` record and make the
sentence name that file by path instead of "the kickoff record". Either way the fork numbers
referenced later in the same document must resolve to a definition in the tree.

**Left-shift gate.** A memory-tree hygiene check that every `fork <n>` reference in a build's records
resolves to a definition within that build folder — the same shape as the existing id-claim ratchet,
applied to the build's own numbered vocabulary.

---

## Recommendation

**BLOCKED.** Fold the three blockers first. They are one `sed` stage, one branch and one wrapper
respectively, and two of them are already claimed as landed in the records.

Two process notes carry more weight than any single finding here.

**The claim "every reader" is not verifiable by writing it in a commit message.** Two blockers this
round are the gap between such a claim and the code: three readers of one parser, two of them fixed;
three records asserting a pin that was never written. The mechanical form of that claim is a check
that ENUMERATES the readers, which is what the left-shift gates for BLOCKER 2 and BLOCKER 3 propose.
Until one exists, the next fold can restate the claim just as cheaply as this one did.

**Round 3's own recommendation — stage every new arm RED before re-arming — was followed for the arms
the fold wrote and not for the fixes it recorded.** MEDIUM 8's pin has no arm and did not land.
BLOCKER 1's new arm covers the comment-free form only. HIGH 5's scalar arm covers the unexecutable
branch only. The discipline binds the arm and the fix equally: a repair with no observed RED is the
same object as a gate with no observed RED, and this build has now produced four of each.
