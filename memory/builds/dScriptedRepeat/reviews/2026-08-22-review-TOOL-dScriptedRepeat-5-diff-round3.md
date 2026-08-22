**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 3 (the FOLD-OF-THE-FOLD review)

**Range:** `a564ce2b98f4c8ea645b5f885ab9f26d535b9e19...70fda314728320717a60dca9587992234f02d90f` —
what round 2's nine confirmed defects turned into, not the whole build. 18 files, 859 insertions,
85 deletions. **ROUND 3.**

**Review shape:** raw 19 · confirmed 18 · refuted 1 · unverified 0 · precision 0.95. The 18
confirmed findings collapse to **11 distinct defects**; four clusters were found independently by
two or three lenses each, and that corroboration is recorded per defect rather than inflating the
count. Every mechanism below was re-reproduced by the synthesis pass before it was written down.

## Verdict: BLOCKED

One blocker, five highs.

**The trend is the finding.** Round 1 found 16 defects in code that passed 92 gate legs. Round 2
found 9 in the fold that fixed round 1, and both of its blockers were round-1 repairs that
reintroduced the defect they closed. Round 3 finds the same shape a third time, and it has moved
one level up the stack.

Rounds 1 and 2 broke on a *field* — the escape landed on `set_checks` and not on `piece_checks`,
the pin covered `grain` and `records` and not `piece_checks`. This fold's stated thesis was to close
that class structurally: one parser instead of three, one sha instead of five positionals, one
`set_field` instead of two `sed` re-stamps. The consolidation is the right move and it did close the
per-field class. What it did not do is change the *shape* of the repair.

- The one parser is now consolidated **and still fed `head -1` at all three call sites**, so a legal
  multi-line TOML array parses to the declared null and every unchecked piece grades `verified`.
  That is the round-1 blocker restored, one line break away, by the commit that consolidated the
  parser to prevent exactly this. **(BLOCKER 1)**
- The five positionals became one positional, and **the one positional is still advisory** — an
  empty `$4` silently reverts to the working-tree parse. Round 2 blocked the per-field pin; the fold
  replaced it with a per-sha pin that is optional in the same way. **(HIGH 2)**
- The escape that round 2 asked for was applied to the *parsed* value instead of the raw one, so it
  now prefix-matches real check names. **(HIGH 3)**
- And the three new gates written to hold all of this — check 28's answer arm, check 28's template
  population, and the `--counts` behavioural arm — **have between them no failing case that has ever
  been observed.** All three pass over the code they were written to catch. **(HIGH 4, 5, 6)**

That last cluster is why the bar is 92/92 green with a blocker in the tree, and it is the most
important sentence in this report. The fold did not merely leave defects in; it wrote the gates that
certify them as correct. Three of the six top findings are gates that cannot fail, one of them
guarding the fold's own headline fix.

**One structural note in the fold's favour, recorded so the trend is read honestly.** The
consolidations are genuinely better engineering than what they replaced, and two of them are working:
the byte-compare in check 28 would now catch the round-2 desynchronisation that cost this build a
round, and the `none — <why>` escape is correct on the set side in both readers. The defects below
are in the *arming*, not the design. A fourth round that fixes the six gate-and-parser findings and
changes nothing else would plausibly land.

---

## BLOCKER 1 — a legal multi-line TOML array parses to the DECLARED NULL, and every unchecked piece grades `verified`

**`tools/unattended/check-playbook.sh:245`** (and the sibling call sites at `:316` and
`tools/unattended/unattended.sh:2117`) · *raw finding 1*

The consolidated `declared_list` is fed a single line — `sed -n 's/^piece_checks…//p' | head -1` at
all three call sites. A TOML array written across lines, which is legal TOML and the ordinary way to
write one:

```toml
piece_checks = [
  "fixture-shape",
]
```

...hands the parser the bare `[`, which strips to the empty string. `pchk` is then the DECLARED NULL,
the `for lg_ in $pchk` join never runs, and a piece record carrying **no verdict at all** counts as
`verified`. That is verbatim the round-1 blocker, restored by the commit that consolidated the parser
to prevent it.

Reproduced directly against the shipped parser text:

```
RAW-MULTILINE=[[]
PARSE=[]
```

And end to end in a scratch tree with one record's verdict rows deleted: the single-line declaration
prints `unchecked — …/one/piece.md records no verdict for declared leg(s): fixture-shape` and
`verified 1 · unchecked 1`; the same tree with the array across three lines prints
`verified 2 · unchecked 0`, and `--counts` returns
`pieces=2 verified=2 failed=0 stale=0 unrecorded=0 unchecked=0`. Leg exit 0, silent.

That census is what `pieces-complete` reads, and `DOD_NO_OVERRIDE="authorization-reachable
pieces-complete"` (`unattended.sh:184`) confirms it is the one Definition-of-Done item that takes no
`--override`. So the item this build deliberately made unbuyable is bought with a line break, on a run
that then merges and pushes with no owner turn.

**Why the bar cannot see it.** Every fixture and the shipped template write the list on one line, and
nothing anywhere constrains a declaration to one line. Worse, check 28 asserts the parse must come
back EMPTY (HIGH 4), so the gate written to validate this parser **certifies this exact output as
correct**. No attacker is needed; an author formatting a TOML array the ordinary way is enough.

**Fix.** Fold the line selection INTO `declared_list` and make it span the value: select from the
`<key> =` line through the first line whose stripped tail ends in `]`, then parse. Or — cheaper, and
honest — REFUSE rather than accept: when the selected line's value opens `[` and does not close `]`
on the same line, `fail 8` naming the key. An unarmed parse must red, not return the declared null
(charter §7). Both inlined copies change together.

**Left-shift gate.** Add a positive arm to check 28 (see HIGH 4) feeding the extracted parser a
multi-line specimen and requiring either the members or the refusal, whichever the fix chooses —
without it, check 28 passes over either fix. Then add a `check-playbook.test.sh` arm committing a
multi-line `piece_checks` alongside a record with no verdict row, asserting `unchecked 1`.

---

## HIGH 2 — `--counts`'s BASE sha is still ADVISORY, so an empty pin silently reads the file the run can edit

**`tools/unattended/check-playbook.sh:47`, falling through at `:135`** · *raw findings 5, 10, 15 —
three independent lenses*

`COUNTS_AT="${4:-}"` at `:47`; `if [ -n "$COUNTS_AT" ]` at `:135`; `else body=$(tr -d '\r' < "$pb")`.
An empty or omitted 4th positional reverts to the working-tree parse — the read this file's own
header (`:38-45`) calls "wrong at the close" — with no note. The new liveness refusal only fires when
a sha WAS given and does not resolve.

Reproduced on this tree, with one uncommitted edit to the fixture's `piece_checks`, then reverted:

```
PINNED : pieces=2 verified=2 failed=0 stale=0 unrecorded=0 unchecked=0
EMPTY4 : pieces=2 verified=0 failed=0 stale=0 unrecorded=0 unchecked=2
OMITTED: pieces=2 verified=0 failed=0 stale=0 unrecorded=0 unchecked=2
```

Same one-line edit, verdict flipped on `pieces-complete`, in either direction.

**Reachable.** The only caller, `unattended.sh:2052`, passes `"$(fact "$rel" base)"` with no emptiness
assertion, and `fact()` (`:314`) returns the empty string with exit 0 for an absent `base:` line.
Nothing non-overridable refuses that absence: `trusted_base` validates the recorded base only inside
`if [ -n "$rec" ]` (`:637`), so `authorization-reachable` still passes; the empty-base refusal at
`:601-605` lives only in the merge-base==HEAD arm. Both sibling arms already carry the assertion this
one lacks — `set-checks-recorded` refuses an unresolvable blob at `:2104`, `closing-review-recorded`
refuses `[ ${#rb} -lt 7 ]` at `:2252`.

**Two honest qualifications, neither refuting.** The DoD loop (`:1919-1962`) evaluates every item
rather than short-circuiting, so an empty base also reds `closing-review-recorded` — meaning a green
close needs that one override on top. But `closing-review-recorded` IS overridable and
`pieces-complete` is not: the item that refuses the absence can be waived, and the item whose pin the
absence silently supplies cannot. Round 2 blocked the per-field pin for precisely this reason; the
fold replaced it with a per-sha pin that is optional in the same way.

**Fix.** Make the sha mandatory: after `:47`,
`[ -n "$COUNTS_AT" ] || { echo 'check-playbook: --counts requires the sha to read the playbook at; an absent pin would silently parse the working tree the run can edit'; exit 2; }`.
Mirror it at the call site — bind `_at=$(fact "$rel" base)` and refuse before invoking the leg.

**Left-shift gate.** A `check-playbook.test.sh` arm passing an empty 4th positional and asserting the
refusal — the failing case this fix has never been observed to have. `check-playbook.test.sh:203`
covers an unresolvable sha and `:210` a real one; the empty one is the gap.

---

## HIGH 3 — the declared-null escape now prefix-matches the PARSED member list, so a check named `nonempty-*` reads as "declares nothing"

**`tools/unattended/unattended.sh:2119`** and the newly-introduced twin at
**`tools/unattended/check-playbook.sh:323`** · *raw finding 2*

Before this fold, `_declared` still carried its brackets and quotes, so `["nonempty-check"]` started
with `[` and could not match `none*`. The fold moved the parse ahead of the escape without anchoring
it, so the case now tests the bare member list. Reproduced against the shipped parser:

```
SETPARSE=[nonempty-distinct]
ESCAPE TAKEN -> declares nothing
```

One character apart on the live leg with the shipped fixture: `set_checks = ["xonempty-distinct"]`
prints `set checks unrecorded — …/set-dScriptedRepeat.md carries no verdict for declared check(s)`;
`["nonempty-distinct"]` prints nothing at all. `set-checks-recorded` returns MET on a run that
recorded no set verdict — no record opened, no message, no `--override` entry in the audit trail, on
a path with no owner turn. `check-playbook.sh:323` carries the identical `case "$schk" in none*)`, so
the leg goes quiet in the same breath and nothing downstream catches it.

Reachability is narrow — a check name beginning with `none`, e.g. any `nonempty-*`. Severity is high
anyway because the escape is matching the wrong surface: the correct predicate is a first-word test,
not a prefix test, and the fold moved it from accidentally-correct to structurally-wrong.

**Fix.** Match the declared null on the RAW value before parsing, and anchor it:
`case "$_raw" in none|none[[:space:]]*|'[]'|'') … esac`. Apply the identical anchored form at
`check-playbook.sh:323` so the two readers keep giving one answer.

**Left-shift gate.** A fixture arm with a declared check named `nonempty-*`, asserting the
unrecorded note fires. No existing fixture can reach this branch, which is why 92 legs are green.

---

## HIGH 4 — check 28's answer arm is one-directional, so a parser that returns NOTHING for every input scores as correct

**`tools/unattended/check-unattended.sh:1449`** · *raw findings 4, 14 — two lenses*

The arm's only assertion is `[ -z "$got" ]`, fed only the shipped template's `*_checks` lines, with
`bash -c … 2>/dev/null`. Every `*_checks` key in the template is `[]`, so the check has **no input
whose expected parse is non-empty**. It is structurally incapable of distinguishing a working parser
from one that answers nothing — and "nothing" is the answer that disables both consumers.

Staged and observed: replacing the `declared_list` body with `printf ''` in BOTH scripts
(byte-identical, so the drift compare at `:1424-1431` is satisfied) leaves check-unattended.sh silent
and exit 0. With `piece_checks = ["phantom"]` committed and no record carrying that leg, the honest
parser reports `verified 0 · unchecked 2` and blocks; the dead parser reports `verified 2 ·
unchecked 0` and the close goes green over pieces nothing checked.

A dead harness is byte-indistinguishable from a correct parse. Verified directly:

```
GOT=[]      # from  bash -c "this ((is not )) valid …" 2>/dev/null
```

A syntax error, a truncated extraction and a correct parse of `[]` all produce the empty string that
satisfies the assertion. The arm's own header claims it grades "THE ANSWER, not just the agreement",
and that header is what a later reader will trust — the §7 green-by-absence shape, in the check that
guards the two inlined copies. This also answers the hunt item about a parser body containing a quote
or a `$`: it cannot be fooled into wrong *output* (the body is passed literally to `bash -c` and
parsed as shell, so a `$` behaves correctly), but it CAN die silently, and dying silently passes.

**Two clauses of the raw findings I refute, recorded so the severity is read honestly.** Check 28 is
not the last line for the all-empty-parser instance: `check-playbook.test.sh` reds with five failures
against a gutted tree, and it is a declared kit leg (`tools/unattended/kit.toml:76`), so adopters get
it too. And check 28 never feeds a multi-line array, so it does not "certify" that output — it simply
never asks. What survives is exact and cheap to fix: no assertion in the non-empty direction, and
stderr discarded with empty treated as success.

**Fix.** Add the positive half in the same loop — feed the extracted `dl_a` a fixed non-empty
specimen and require the exact members back:
`got=$(bash -c "$dl_a"$'\n'"declared_list \"\$1\"" _ '["a", "b#c"]    # trailing comment'); [ "$got" = 'a b#c' ] || fail 28 …`.
Add a multi-line specimen requiring whatever BLOCKER 1's fix chooses. And prove the execution ran
rather than inferring it from empty output: drop the `2>/dev/null`, capture the exit status, and
`fail 28` on a non-zero rc, so an unexecutable parser reds instead of scoring as the declared null.

**Left-shift gate.** This finding IS the gate suggestion; the left-shift is that check 28's own
failing case must be observed before it lands — stage `printf ''` into both copies, confirm RED,
unstage (charter §7).

---

## HIGH 5 — the only behavioural regression arm for round-2 blocker B2 cannot fail

**`tools/unattended/check-playbook.test.sh:213`** · *raw findings 3, 16 — two lenses*

The arm computes `C0`, runs `sed -i '/^piece_checks/d'` on the working tree, computes `C1`, and
asserts `C0 = C1`. The break is staged in the one direction where "declared nothing" and "declared
legs all PASS" produce the same census, because the fixture's records carry PASS for every declared
leg. All four cells measured in a seeded scratch tree:

| | before the edit | after the edit |
|---|---|---|
| **pinned** | `verified=2 unchecked=0` | `verified=2 unchecked=0` |
| **unpinned** | `verified=2 unchecked=0` | `verified=2 unchecked=0` |

The assertion holds byte-for-byte on the defective working-tree read that round 2 blocked. This is
`fixture-passes-by-finding-nothing` from the project's own checklist, sitting on a blocker — and it is
why the 92/92 bar does not see HIGH 2.

The distinguishing direction exists and is not asked for: committing `piece_checks = ["phantom-leg"]`
and deleting it on disk gives pinned `verified=2 unchecked=0` against unpinned `verified=0
unchecked=2`.

**The companion arm is vacuous too.** `unattended.test.sh:1750` asserts
`grep -c 'COUNTS_GRAIN\|COUNTS_RECORDS'` over the DRIVER is 0 — and it was 0 at the pre-fix base as
well, measured: `git show a564ce2b:tools/unattended/unattended.sh` returns 0 hits, because those
variable names only ever existed in `check-playbook.sh` (6 hits there at the same sha). That leaves B2
with exactly one armed assertion — the source-text grep at `unattended.test.sh:1746`, which does fail
at the base — and zero behavioural coverage.

**Fix.** Invert the staged break: commit `piece_checks = ["phantom-leg"]`, delete it on disk, assert
the pinned read is literally `verified=2 unchecked=0` AND that an explicit tree read of the same tree
reports `unchecked=2`. Assert both halves in one arm, so the pair is what passes rather than one
number. Repoint the `unattended.test.sh:1750` grep at `check-playbook.sh` or delete it as noise.

**Left-shift gate.** `tools/memory-tree/check-arms.py` already refuses absence-shaped assertions; the
generalisable ratchet is an arm-level rule that a regression arm asserting equality must be
accompanied by a control proving the two sides CAN differ. Cheapest concrete version: require every
`bad "…"` regression arm added for a numbered review finding to carry a sibling assertion that the
defective code path produces a different value.

---

## HIGH 6 — check 28's template arm covers 2 of the shipped block's 10 declaration keys, and the other 8 carry the same comment

**`tools/unattended/check-unattended.sh:1451`** · *raw finding 11*

The arm greps `^[a-z_]+_checks[[:space:]]*=`. Measured against the shipped template: **2 keys
matched, 10 declaration keys present.** (The raw finding said 11 in its summary and 10 in its
evidence; 10 is what the tree gives.) The check's own failure text states a key-independent argument —
"an adopter who copies the template verbatim" — while its population is `*_checks` only. `declared_list`
generalised the PARSE across list keys; check 28 generalised the GATE across `*_checks` only.

Reproduced by building an adopter playbook from `PLAYBOOK-TEMPLATE.template.md`'s own block with the
comments kept and the values filled, exactly as the failure text describes:

- `coverage = "probe"    # how completely…` — **check 6 red**, refusing a correctly-filled mode and
  naming its own comment back at the author.
- `grain = "out/*/piece.md"    # a glob…` — **DEAD PROBE** over a tree holding two real pieces; the
  census reads zero, so `pieces-complete` would refuse "this run produced no piece" for a false
  reason. Stripping only that comment and re-running the same tree prints `pieces 2 · verified 0 ·
  unrecorded 2`.
- `curated = ""    # who ratified this playbook…` — **check 2, the FREEZE, PASSES** on an unratified
  playbook. A gate satisfied by its own comment prose.
- `step_selector` — **check 3 red** at `matched 0 against floor 3`. (An instance the raw finding did
  not list.)
- `records` parses to comment text in the leg and to a DIFFERENT comment slice in the driver — the
  leg's `sed` yields `recs    # where…`, the driver's `awk -F=` + `gsub(/^[[:space:]"]+/)` at
  `unattended.sh:2688/2718` yields `recs"    # where…`. Two readers, two answers, on the key that
  decides where records are written.

**Fix.** Widen the parse assertion to every key the block declares: grep `^[a-z_]+[[:space:]]*=` over
the template's toml fence and assert each value parses to its declared null through the same extracted
function. Or give the scalar keys a shared `declared_scalar()` — comment strip, quote strip, trim —
inlined and byte-compared the same way, and route `grain`, `records`, `coverage`, `curated` and
`step_selector` through it in both the leg and the driver's `awk` reads.

**Left-shift gate.** The generalisable form: check 28 should derive its key population from the
template's toml fence rather than from a hand-typed pattern, so a key added to the template reds until
a parse assertion claims it — the same declared-population discipline the charter §7 already applies
to kit descriptors.

---

## MEDIUM 7 — `pchk` did not get the `none — <why>` escape its sibling got 74 lines below, in this same fold

**`tools/unattended/check-playbook.sh:245`** · *raw finding 17*

`check-playbook.sh:323` carries `case "$schk" in none*) schk="" ;; esac` for the set reader, and
`unattended.sh:2118` carries `''|'none'*` for the driver's set arm. `pchk` goes straight from
`declared_list` into the join loop with no escape, so the value word-splits into phantom leg names no
record can satisfy. Reproduced against the shipped parser:

```
PCHK_NONE=[none — this playbook makes one piece ever]
```

In-tree with `piece_checks = none — this playbook makes one piece ever` committed, the leg prints
`unchecked — …/piece.md records no verdict for declared leg(s): none — this playbook makes one piece
ever` for every piece and `pieces 2 · verified 0 · unchecked 2`, while the set-side reader correctly
reports nothing. `--counts` returns the same, and `unattended.sh:2090` fails `pieces-complete` on
`_xc != 0` — so the close BLOCKS with nobody present and no in-band repair.

`none — <why>` is ratified as a declared null by the template (line 11, and section 8's line 156) and
is explicitly accommodated for `set_checks` in two separate readers. This is the round-2 B1 shape one
declaration over: the escape landed on one sibling and not the other, in the same file, in the commit
that wrote it. Filed MEDIUM rather than HIGH because the consequence is a loud false BLOCK rather than
a silent false PASS — but it is the same authoring failure.

**Fix.** Fold the escape into `declared_list` itself so no future caller can omit it. Then check 28's
byte compare keeps both copies honest about it, which is the whole argument for having one parser. The
minimal alternative is `case "$pchk" in none*) pchk="" ;; esac` after `:245`, mirroring `:323` — but
that leaves the third call site free to forget it again, which is how this build got here.

**Left-shift gate.** A `check-playbook.test.sh` arm committing `piece_checks = none — <why>` and
asserting `unchecked 0`.

---

## MEDIUM 8 — `GITSHOW` dereferences a sha with plain `git show`, outside the pin the driver's own header says every such read goes through

**`tools/unattended/check-playbook.sh:100`** · *raw finding 7*

```
GITSHOW() { git show "$1" 2>/dev/null | tr -d '\r'; }
```

Plain git. Confirmed: no `useReplaceRefs` pin anywhere in the leg, no lib sourced, no graft variable
set. `unattended.sh:57` states the invariant this fold broke — "Every read below that turns a sha into
bytes or into ancestry goes through `GIT()`" — and `GIT()` is `git -c core.useReplaceRefs=false` plus
`export GIT_GRAFT_FILE=/dev/null`. The fold moved the load-bearing dereference out from under it.

Reproduced in a scratch repo with `refs/replace/<A>` installed: `git show "$A:f.txt"` printed
SUBSTITUTED, `git -c core.useReplaceRefs=false show "$A:f.txt"` printed ORIGINAL, and
`GIT_GRAFT_FILE=/dev/null git show "$A:f.txt"` printed SUBSTITUTED — that last one is the load-bearing
result, because `GIT_GRAFT_FILE` is the only hardening the child `bash check-playbook.sh` inherits,
and the driver's own header (`:52-55`) records that it does not cover replace refs.

So inside one `--close`, `pieces-complete` (non-overridable) can measure a substituted playbook while
`set-checks-recorded` at `unattended.sh:2119` measures the true one — two readers, one blob, one sha,
two answers. Check 14 (`check-unattended.sh:237`) does detect a replace ref, but it reds `gates-green`,
which IS overridable, and its own header concedes: "nothing binds the next tool that reads the same
objects." This fold created that next tool.

**Fix.** Pin the leg's own read:
`GITSHOW() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false show "$1" 2>/dev/null | tr -d '\r'; }`,
and set `GIT_GRAFT_FILE=/dev/null` near the top of `check-playbook.sh`.

**Left-shift gate.** Both scripts install standalone so the wrapper cannot be shared — but the two
spellings can be byte-compared by the same leg check that already compares `declared_list`. Extend
check 28's extraction to cover the `GIT`/`GITSHOW` definitions, so a future unpinned dereference reds.

---

## MEDIUM 9 — the new `--counts` liveness refusal is computed, printed, and thrown away by its only caller

**`tools/unattended/unattended.sh:2052`** · *raw findings 12, 19 — two lenses*

`check-playbook.sh`'s `fail()` prints to stdout, and the driver's only call site pipes the leg through
`| grep -m1 '^pieces='`. Measured on this tree:

```
PLAYBOOK check 8 FAILED — the playbook does not resolve at the sha this count was asked for … 0000000000000000000000000000000000000000 and tools/unattended/playbook.fixture.md
--- through the driver's pipeline: ---
captured=[]
```

`dod_met` then falls to its generic "the piece enumerator produced no machine-readable count line",
which is identical for an unresolvable sha, an undeclared `records`, a git failure and an `exit 2`.
The one line that distinguishes those causes is exactly the one filtered out.

The sibling comparison sits eleven lines up in the same function: the `gates-green` arm carries the
comment "SURFACED, not discarded. `>/dev/null 2>&1` meant a blocked `--close` reported THAT the bar was
red and never WHICH leg" — the identical defect, fixed for gates and re-introduced for counts in the
same file. Reachability is not theoretical: a run that creates its playbook during the run has no blob
for it at the pinned BASE, which is precisely the case that lands here.

Capped at medium: the close still correctly refuses, so this is diagnostic loss rather than a wrong
verdict. The operator must re-run the leg by hand to learn why.

**Fix.** Capture once, select from it:
`_raw=$(bash "$KIT_DIR/check-playbook.sh" --counts "$_pb" "$slug" "$_at" 2>&1); _counts=$(printf '%s\n' "$_raw" | grep -m1 '^pieces=')`,
and on the empty branch put the leg's own `FAILED` line into `DOD_OUT` instead of the generic sentence.

**Left-shift gate.** The only test arm (`check-playbook.test.sh:203`) invokes the leg directly with
`2>&1`, so nothing exercises the path the close actually takes. Add a driver-suite arm asserting the
leg's refusal text reaches `DOD_OUT` — which generalises to the class: any refusal whose text is
written for an operator needs one arm proving it survives the caller's pipeline.

---

## LOW 10 — both widened separator guards report field values that cannot contain the offender

**`tools/unattended/unattended.sh:2578` and `:2643`** · *raw findings 8, 13, 18 — three lenses*

`case "$leg$piece$pbsha$runid" in *" · "*)` tests four fields and prints `field follows: $leg $piece`.
`case "$leg$runid$hashes" in *" · "*)` tests three and prints `field follows: $leg $runid`. All of
`$pbsha`, `$runid` and `$hashes` are argv-supplied and unvalidated on the attended path (`--playbook-sha`
→ RP_PBSHA `:3046`, `--run` → RP_RUN `:3047`, `--set` → RP_SET `:3048`), so an operator who passes
`--set 'AAAA · leg honest · verdict PASS'` is refused correctly and then told the offender is
`other R9` — neither of which contains the separator.

The widening comment at `:2565-2573` says explicitly that the guard now covers EVERY caller-supplied
field; the message was not extended with it. This is the kit's own recorded class — "a true refusal for
a false reason, which sends the reader to the wrong file" — reappearing in the guard the fold widened,
one line from the bypass-flag message where the fold accepted and fixed exactly this.

**Fix.** Print the fields the guard actually tests: `- fields follow: leg [$leg] piece [$piece]
playbook-sha [$pbsha] run [$runid]` and `- fields follow: leg [$leg] run [$runid] set [$hashes]`. Better,
test each field in its own `case` so the message names the single offender.

**Left-shift gate.** The arms at `unattended.test.sh:2652` and `:2664` match only the message prefix up
to `field follows:`, so they pass whichever fields are printed. Extend them to assert the OFFENDING
VALUE appears in the message — the generalisable rule being that a refusal test asserts the refusal
names its cause, not merely that it refused.

---

## LOW 11 — the README's owner-ruling bullet, rewritten in this diff, describes the opposite of what this diff shipped

**`memory/builds/dScriptedRepeat/README.md:172`** · *raw finding 9*

The bullet still reads: "**`--counts` takes the recorded FACTS** and stops re-parsing the playbook,
which also gives the pinned `grain` fact its first reader." The shipped code does the opposite —
`check-playbook.sh:47` takes a BASE sha and re-parses the blob; `COUNTS_GRAIN`/`COUNTS_RECORDS` are
gone from `tools/` entirely and `unattended.test.sh:1750` asserts their absence. `grain` and `records`
are still written at `unattended.sh:1740-1741` and read by nothing, so the second clause is false in
fact, not merely stale in emphasis.

Spec 6's rev-8 log, added in the same fold, states the new mechanism correctly. So the build's README
and its spec now give two answers to one question about the mechanism guarding the one DoD item that
takes no override — and the README is the file a session reads first. `git log -L` puts the bullet's
authorship inside the diff under review, so it is not inherited drift at cumulative-diff scope, and no
later section corrects it.

**Fix.** Keep the ruling as history and mark it superseded: append "— superseded at the round-2 fold:
`--counts` takes the pinned BASE sha and reads the blob, so `grain` and `records` remain provenance
facts with no machine reader (spec 6 rev-8)".

**Left-shift gate.** The `two-answers-to-one-question` class already has a home: the drift audit.
`python tools/drift-audit/drift_report.py` should grow a probe that flags a build README asserting a
mechanism its own spec set contradicts at a later rev — or, minimally, a DoD item on the fold checklist
that every owner-ruling bullet naming a shipped mechanism is re-read against the code at fold time.

---

## Negative results — the hunt list items that came back clean

Recorded because a hunt that finds nothing is only worth something if it says so.

- **`set_field` and `%` / backslash — CLEAN.** `printf '%s: %s\n' "$key" "$val"` passes the value as an
  ARGUMENT, never as the format string, and `IFS= read -r` preserves backslashes. Measured:
  `set: a%sb\nc%%d` round-trips byte-identical.
- **`set_field` rewriting a line that merely CONTAINS the key — CLEAN.** `case "$line" in "$key: "*)`
  is anchored at line start by `case` semantics, so mid-text occurrences are untouched.
- **`set_field` and a missing trailing newline — CLEAN.** `|| [ -n "$line" ]` handles the final partial
  line; it normalises by appending a newline, which is what every writer emits anyway.
- **`set_field` and a cross-filesystem `mktemp` — CLEAN enough.** `mv` falls back to copy+unlink across
  devices. The destination inherits the temp file's mode, which is immaterial for a tracked text record.
- **`declared_list`'s trim-first ordering and leading whitespace inside quotes — CLEAN, and not a
  regression.** A member with leading whitespace is unrepresentable either way: `tr -d '"'` removes the
  quotes and `for lg_ in $pchk` word-splits, so internal whitespace cannot survive by design, before or
  after the reordering.
- **check 28's `bash -c` fooled by a quote or a `$` in the parser body — CLEAN as to output.** The body
  is expanded once by the outer shell and then parsed as shell source by the child, so a `$` behaves
  correctly. It CAN die silently on a quote imbalance, and that folds into HIGH 4 rather than standing
  alone.
- **`--counts`'s `continue` outside its loop — CLEAN.** The refusal sits inside `for pb in $PLAYBOOKS`,
  so `continue` is valid. It skips the rest of THAT playbook's checks, which is correct for an
  unreadable body, and `fail 8` sets status.
- **Census with `COUNTS_AT` set and the playbook unchanged — CLEAN.** Pinned and tree reads agree
  (`verified=2 unchecked=0` both ways) when there is no uncommitted edit.
- **Widened write guards breaking the SLUG path — CLEAN.** `$runid` on that path is the session slug,
  which §2 constrains to `[A-Za-z]` only; it cannot contain a newline, the separator, or the bypass flag.
- **The two `stage_or_fail` calls added to the idempotent early-returns — CLEAN.** `:2613` and `:2665`
  stage `$rec`, the record the caller just asked to be written. No verdict changes and no unexpected
  file is staged.

### One residual observation, NOT a confirmed finding

`set_field` silently rewrites nothing and returns 0 when the key line lacks the trailing space —
measured: a record containing `hash:` (no space, no value) survives `set_field … hash deadbeef`
unchanged, `rc=0`. Every in-kit writer emits `key: value`, so this needs a hand-malformed record to
reach, and no finder filed it and no skeptic verified it. Recorded because it is the repo's own
"a probe that cannot move says so" class in a helper this fold introduced, and a `return 1` on zero
substitutions would close it for the cost of a counter.

---

## What the bar says, and why it says it

`bash tools/unattended/check-playbook.test.sh` → **PASS (61 assertions)** at this head, with BLOCKER 1
live in the tree. The full bar is 92/92 green. Every finding above explains its own invisibility:

| # | Defect | Why 92 green legs miss it |
|---|---|---|
| 1 | multi-line array → declared null | every fixture and the template write the list on one line; check 28 asserts the empty parse is correct |
| 2 | advisory BASE sha | no arm passes an EMPTY 4th positional — `:203` tests a bad sha, `:210` a good one |
| 3 | `none*` prefix-matches parsed members | no fixture declares a check named `nonempty-*` |
| 4 | check 28 one-directional | every template `*_checks` key is `[]`, so no input expects a non-empty parse |
| 5 | B2 arm cannot fail | the staged break produces identical output pinned or unpinned |
| 6 | check 28 covers 2 of 10 keys | the other 8 are never fed to a parser by any check |
| 7 | `pchk` missing the `none` escape | no fixture spells `piece_checks = none — <why>` |
| 8 | unpinned `GITSHOW` | check 14 detects replace refs but reds an OVERRIDABLE item |
| 9 | refusal discarded by the pipeline | the only arm invokes the leg directly with `2>&1` |
| 10 | wrong fields in the guard message | the arms match the message prefix and stop before the tail |
| 11 | README contradicts the spec | no gate reads build-README prose against its spec set |

Seven of eleven are population-of-one defects — the fixture corpus cannot spell the input that
triggers them. That is the same diagnosis round 2 wrote about round 1, in the corpus written to close
round 2.

## The recommendation

Fold findings 1 through 6 before this lands, and fold them in that order — 1 is the blocker, and 4, 5
and 6 are what would otherwise let the next round's fold reintroduce it. Findings 7 through 11 are
cheap and can ride the same fold. Then, before calling it done, run the charter §7 discipline that
would have caught most of this: **stage each new gate's failing case, confirm RED, unstage.** Three of
the six top findings in this report are gates that have never been observed to fail, and one of them
is the guard on this fold's headline fix.
