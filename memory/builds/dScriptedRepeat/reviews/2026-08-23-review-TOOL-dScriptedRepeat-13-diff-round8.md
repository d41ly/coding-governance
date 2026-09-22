**Serves:** diff-review TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# dScriptedRepeat — diff review, round 8 (the fold of round 7)

**Range:** `12549562...HEAD` — ONE commit, `0a80f7bb`, 24 files, 1125 insertions and 88 deletions.
The subject is the FIX, not the diff round 7 already read: `tools/unattended/check-playbook.sh`
(+124), `tools/unattended/check-unattended.sh` (+43), `tools/unattended/run-unattended-gates.sh`
(+44), `tools/drift-audit/drift_report.py` (+70), the ten new arms across three suites, and the
records that carry them. **ROUND 8.**

**Review shape:** raw 20 · confirmed 16 · refuted 4 · unverified 0 · precision 0.80. The four refuted
(raw ids 4, 10, 11, 12) died in the skeptic pass and are not reproduced here. The 16 confirmed
findings collapse to **10 distinct defects**; three clusters were filed independently by two or three
lenses, and that corroboration is recorded per defect rather than counted again. Every mechanism
below was reproduced against a working tree before it was written down.

## Verdict: BLOCKED

**Two blockers, two highs, six lows. Zero mediums — not because none were filed, but because all four
medium findings were absorbed UPWARD into a blocker or a high cluster.** Nothing was downgraded.

**The grading rule, unchanged from round 7 so the two rounds are comparable.** A finding is a BLOCKER
when it makes the unit's own load-bearing claim false, not when it is merely severe. Unit 13's claim
is "the bypass flag is read back out of what landed"; blockers 1 and 2 each make that false, by a
different route, and both routes were OPENED by this fold. Unit 15's claim is that a degraded
`_pbatch` mode is never spelled with a passing value; low 2 falsifies it for exactly one arm, inside
a run that reds anyway, so it is a low. Unit 14 ships `gateable: False`, so nothing it does changes a
merge verdict; its one surviving finding is graded on report quality.

**The shape underneath both blockers, stated once: round 7's fixes were correct about the mechanism
and incomplete about the class, and each one opened a new hole on the way through.** Blocker 3 of
round 7 said the conf was read by a re-derived `sed` pipeline; the fold replaced it with a `source`,
which parses correctly and now cannot tell a failed read from an absent key — so a check that used to
mis-parse now silently turns itself off and prints a reason it never verified. High 1 of round 7 said
an unquoted `for` over `git ls-files` splits a path with a space; the fold converted five loops to
`while IFS= read -r` and left `core.quotePath` alone, so the same enumeration still mangles a
non-ASCII name — and left the SIXTH enumeration, the population loop, on the unsafe form while its
own comment claims the class covers "every place this leg walks `git ls-files` output". Two of round
7's three blockers are therefore still reachable, by narrower routes than before.

**What the current suite sees: none of it.** Ten arms landed and every one is green over every defect
below. The new check-10 arms all use the single shipped fixture and a well-formed `.unattended.conf`,
so no arm exercises a conf that fails to source, a records root that is empty while another is not,
or a path byte outside ASCII. The `--help` arm asserts a number, not the sentence beside it. The new
LOW 3 drift arm passes identically with the fix reverted (low 6). I did not re-run the full bar in
this pass; the reproductions were done in hermetic scratch clones built from the kit's own `seed()`.

**The named high-value lens that came back CLEAN, recorded as a negative** — a review that only
prints hits is indistinguishable from one that did not look.

- **No converted loop lost a variable lifetime.** All six `while IFS= read -r` loops in
  `check-playbook.sh` are HEREDOC-fed (`:107/117`, `:159/163`, `:376/381`, `:432/441`, `:456/500`,
  `:581/587`), never pipe-fed, so every body runs in the current shell and every counter the
  enclosing scope reads survives: `BYPASS_SEEN` and `_seen_here` at `:438`, and `v/f/st_/un/uc/inscope`
  at `:455-499`, which feed the `pieces=…` machine line at `:510`. The one subshell is
  `_rids_=$(while … done <<RIDEOF)` at `:542`, and it EMITS text rather than incrementing anything,
  so the substitution boundary costs nothing. Its outer `for rid_ in $(…)` is split-unsafe on
  purpose, with the reason stated in the comment at `:539` (run ids carry no whitespace) — a declared
  exemption, and a fair one. No finding.

---

## BLOCKER 1 — `_conf_key` cannot tell "the key is undeclared" from "the conf did not source", so check 10 disarms itself and announces a cause it never verified

**`tools/unattended/check-playbook.sh:83-86`** (the helper), consumed at `:98` and `:601`.
*Filed by three lenses as ids 15 (high), 3 (medium) and 8 (low) — one defect, three routes in.*

```sh
_conf_key() { # KEY -> the value this file's three siblings would see
  [ -f .unattended.conf ] || return 0
  ( . ./.unattended.conf >/dev/null 2>&1; eval "printf '%s' \"\${$1:-}\"" )
}
```

The subshell's exit status is discarded and its stdout is the whole answer, so **an abort mid-source
and an undeclared key are the same empty string.** `>/dev/null 2>&1` swallows the diagnostic, so
nothing on either channel hints at the real cause. `CONF_BYPASS` then tests empty at `:601` and the
leg prints:

```
bypass scan SKIPPED - no BYPASS_BAN declared in .unattended.conf, so tracked evidence records are not read back for it
```

which is FALSE — the key is declared. Reproduced in a hermetic clone seeded like
`check-playbook.test.sh`, with `landed with --no-verify` appended to a tracked evidence record. Clean
conf: RC=1 with the check-10 refusal. Same tree with one line added to the conf:

| line inserted in `.unattended.conf` | result |
|---|---|
| `exit 0` (anywhere before the key) | RC=0, `bypass scan SKIPPED`, corpus unread |
| `return 0` (before the key) | RC=0, `bypass scan SKIPPED`, corpus unread |
| a syntax error BEFORE the assignment | RC=0, `bypass scan SKIPPED`, corpus unread |
| `FOO=$UNSET_THING` under the inherited `set -u` | RC=0, `bypass scan SKIPPED`, corpus unread |
| a syntax error AFTER the assignment | **does not reproduce** — bash executes the assignment before it reaches the parse error |

Position matters and the last row is the honest limit of the defect: only an abort that lands *above*
the assignment kills it. Four of five routes do.

**Why this is a blocker and not a high.** The arming `case` added at `:100-104` fires only on a
NON-EMPTY resolved value, so the one resolution that turns the entire check off is precisely the one
state it exempts — the guard the fold added to make the read honest cannot see the read failing.
The `sed | tr -d '"' | head -1` reader this replaced could not be defeated this way; round 7's
blocker 3 was that the old reader mis-parsed a quoted value, and the fix traded a parse defect for a
liveness defect in the same read. **And the sibling leg is not a compensating control.**
`check-unattended.sh:110-115` sources the same file in its MAIN shell: the `return 0` and
syntax-error shapes are caught by its required-key loop, but `exit 0` terminates that leg at status 0
before it reaches a single check, and `run-gates` maps rc 0 to `GATE ok`. Both legs green, check 10
silently off. `.unattended.conf` is a tracked working-tree file the graded run can itself commit, and
the gotcha this very fold minted
([two-readers-of-one-config-one-re-derived.md](../../../gotchas/two-readers-of-one-config-one-re-derived.md))
records exactly that — which makes a one-line append a complete bypass of the second-opinion half of
a guarded surface.

**Fix.** Make the read's own liveness a verdict rather than a default:

```sh
_conf_key() { # KEY -> the value this file's three siblings would see; rc 9 = the conf did not source
  [ -f .unattended.conf ] || return 0
  ( unset -v "$1" 2>/dev/null; . ./.unattended.conf >/dev/null 2>&1 || exit 9
    eval "printf '%s' \"\${$1:-}\"" )
}
```

and have the caller `fail 10` on rc 9 with *"the project conf could not be sourced, so every key this
leg reads resolves to the empty string"*, never falling through to the SKIP note. `bypass scan
SKIPPED` must be reachable only when the file genuinely declares no `BYPASS_BAN`. (The `unset -v`
also closes low 1 below, which is why one edit answers both.)

**Left-shift gate.** Three arms in `check-playbook.test.sh`, one per degraded shape (`exit 0`, a
pre-assignment syntax error, an unbound reference under `set -u`), each seeding a tracked evidence
record that names the flag and asserting RC=1 plus the new refusal text — every one observed RED
against today's code first. Plus one arm in `check-unattended.test.sh` asserting that a conf
containing `exit 0` does not take THAT leg to rc 0: wrap its own read as `( . "$CONF" ) || fail`
before the top-level source, so neither leg can be ended by the file it is reading.

---

## BLOCKER 2 — the class fix closed word-splitting and left C-quoting: `GITLS` reds the merge bar on a legitimate tree, and drops records in silence everywhere else

**`tools/unattended/check-playbook.sh:135`**, with consumers at `:159`, `:434`, `:441`, `:456`,
`:545` and `:581`.
*Filed by two lenses as ids 1 (high) and 16 (medium) — one defect.*

```sh
GITLS() { git ls-files -- "$1" 2>/dev/null; }
```

`core.quotePath` defaults to **true**, so `git ls-files` C-quotes any path carrying a non-ASCII byte,
a double quote or a backslash. A tracked record at `tools/unattended/fixture-records/tools~über~x.md`
comes back as the literal `"tools/unattended/fixture-records/tools~\303\274ber~x.md"` — surrounding
quotes and octal escapes included — and `[ -f ]` on that string is false. Round 7's conversion from
`for` to `while IFS= read -r` closes the SPACE case and does nothing about this one; the comments at
`:157` and `:428` cite round 7's high 1 by name while the enumeration underneath them is still
byte-unfaithful.

Four consequences, all observed in a hermetic clone of the kit's own fixture:

1. **The bypass grep never runs on such a record.** With identical `landed with --no-verify` bytes in
   two records, the ASCII-named sibling fired the `:439` refusal once and the umlaut record fired it
   zero times. The single check whose job is reading a lander bypass out of what landed skips any
   record whose name carries one non-ASCII byte.
2. **The merge bar reds on a legitimate tree, with a false cause.** The new arm at `:434-436` takes
   the `[ ! -f "$bp_" ]` branch and exits 1 with *"a tracked evidence record is not readable in this
   worktree"* — the file is present and readable. Control tree RC=0; same tree plus one `café.md`
   record RC=1.
3. **The liveness counter now DEFLATES.** `bypass scan - tools/unattended/fixture-records: 3 tracked
   evidence record(s) read` over 4 tracked records, and `2` over 3 in a second run. Round 7 fixed the
   inflating direction of this counter and opened the deflating one.
4. **The census loses the piece silently.** `record_for` (`:159-161`), the run-id gather (`:545`) and
   the orphan sweep (`:581-583`) each take a bare `[ -f "$r" ] || continue`, so a quoted name is
   dropped with no note at all: renaming a real record to a non-ASCII name flipped the census from
   `verified 2 · unrecorded 0` to `verified 1 · unrecorded 1`, and `pieces-complete` reads that
   census.

**Why this is a blocker.** Evidence-record names are DERIVED from piece paths with `/`→`~`, so any
adopter whose content pieces carry one non-Latin character reaches all four at once — a false red
they cannot fix by fixing the named file, plus a silent coverage loss in the number a reviewer reads
to believe the run. Latent in this repo today (no tracked path has a byte outside ASCII), reachable
in a shipped kit.

**Fix.** Make the enumeration byte-faithful at the source rather than guarding six consumers:

```sh
GITLS() { git -c core.quotePath=false ls-files -z -- "$1" 2>/dev/null; }
```

with every consumer switched to `while IFS= read -r -d '' x`. `core.quotePath=false` alone (verified
to emit raw bytes with no surrounding quotes) closes the non-ASCII case but leaves a newline in a
path splitting a line reader, so the `-z` is not optional. Then KEEP the `[ -f ]` refusal at `:434`
for the genuine tracked-but-absent case it was written for — it is a good check aimed at the wrong
population today.

**Left-shift gate.** Two arms in `check-playbook.test.sh`: a record named with a non-ASCII byte and
one with a literal newline, each asserting the bypass refusal FIRES on flag-bearing content and that
the per-root counter equals the tracked count. The existing space-path arm passes today and proved
nothing about either. Then gate the class where the kit already gates git invocations: extend the
`check-unattended.sh` rule at `:2099-2161` so any `git ls-files` in the kit lacking both `-z` and
`core.quotePath=false` reds — one predicate, and it covers every future enumeration rather than the
six that exist.

---

## HIGH 1 — the new zero-teeth refusal keys on the repo-wide aggregate, so it can fire only inside the kit's own fixture

**`tools/unattended/check-playbook.sh:608-609`**, against the per-root note at `:446`.
*Raw id 2.*

```sh
if [ -n "$CONF_BYPASS" ] && [ "$BYPASS_ROOTS" -gt 0 ] && [ "$BYPASS_SEEN" -eq 0 ]; then
```

The block's own comment at `:443-444` names the failure mode verbatim — *"one repo-wide counter lets
a grained playbook's records keep the number healthy while another root contributes nothing at
all"* — and only the NOTE was moved per-root. The RED stayed on the aggregate.

Reproduced: a scratch repo carrying the shipped fixture (3 tracked records) plus a second, real
playbook declaring `records = "content/records"` over a root holding no tracked `.md`. Output:

```
bypass scan - content/records: 0 tracked evidence record(s) read
bypass scan - 3 tracked evidence record(s) read across 2 declared records root(s)
```

rc **0**. The second playbook's entire evidence corpus is asserted over an empty population — the
exact state this refusal was added to red — and the merge bar is green.

**It cannot fire in an adopter at all.** `kit.toml` installs with `include = "**"`, so every adopter
carries `playbook.fixture.md` and `fixture-records/`, and check 1 at `:130` reds on an empty playbook
population — which makes `BYPASS_SEEN >= 3` effectively unconditional. The only tree where the
refusal can fire is one that repoints the fixture's own single root at an empty dir, and
`check-playbook.test.sh:454-459` does exactly that (`sed -i 's|^records       = .*|… empty-records|'`).
**A gate whose only reachable failing case is its own fixture is the could-not-fail shape §7 names,
and the multi-root shape the comment describes is untested and unreachable.**

**Fix.** Move the refusal to the root, where `_seen_here` already lives — inside the
`[ -n "$CONF_BYPASS" ]` block after the `BPEOF` loop, redding when `_seen_here` is 0 for a declared
root and naming `$rr` and `$pb`. Keep the aggregate line as a note. A root that legitimately has no
records yet then needs a DECLARED exemption in the playbook (`records_empty_ok` or equivalent), not a
hole another playbook's records paper over.

**Left-shift gate.** Replace the single-fixture arm with a two-playbook one: fixture plus a second
playbook whose declared root is empty, asserting RC=1 and that the refusal names the empty root. Then
the arm and the defect describe the same population.

---

## HIGH 2 — the sixth enumeration was not converted, and it is the one whose failure also disarms the new liveness guard

**`tools/unattended/check-playbook.sh:268`**.
*Filed by two lenses as ids 5 and 17, both medium; graded HIGH here because round 7 graded the
identical defect HIGH at strictly less damaging sites.*

```sh
for pb in $PLAYBOOKS; do
```

`PLAYBOOKS` is accumulated newline-safely by the `while IFS= read -r f` loop at `:107-117` and then
consumed unquoted here. The file sets `set -u` only — no `IFS` pin, no `set -f` — so this
word-splits under the default IFS. With one tracked playbook at `memory/builds/my build/PLAYBOOK.md`:

```
population 1 playbook(s)
line 280: memory/builds/my: No such file or directory
line 280: build/PLAYBOOK.md: No such file or directory
```

then checks 2 and 3 fire twice each against paths that are not in the tree, while the real playbook
is **never graded at all**. `POP` still counts it as one, so the population note and the loop
disagree about how many things exist.

**The compounding half is what promotes this.** `$rr` is empty for both phantom names, so
`BYPASS_ROOTS` stays 0 and the run ends `bypass scan - 0 tracked evidence record(s) read across 0
declared records root(s)`. The new refusal at `:608` is gated on `[ "$BYPASS_ROOTS" -gt 0 ]` and
therefore **cannot fire** — the evidence corpus goes entirely unscanned and the only assertion added
this round to notice that is structurally blind to it. The comment at `:539-541` claims the fix
covers "every place this leg walks `git ls-files` output"; this line is that claim's counterexample,
in the same file.

**Fix.** The same heredoc form as its five siblings:

```sh
while IFS= read -r pb; do
  [ -n "$pb" ] || continue
  …
done <<PBLEOF
$PLAYBOOKS
PBLEOF
```

The body already `continue`s on empty, so nothing else changes.

**Left-shift gate.** An arm tracking a playbook whose path contains a space, asserting the leg names
it in its per-playbook messages, grades it, and counts its records root in `BYPASS_ROOTS`. Better,
gate the class: a scan refusing any `for … in $VAR` in this kit where `VAR` is fed from `git
ls-files`, so the seventh enumeration cannot be written unsafely either.

---

## LOW 1 — `_conf_key`'s subshell inherits the process environment, so an UNDECLARED key resolves to an exported value

**`tools/unattended/check-playbook.sh:85`.** *Raw id 7.*

The subshell sources the conf without pre-initialising the key, so a key the conf does not declare
falls through to whatever the environment exports. Reproduced twice: `PLAYBOOK_GLOB='**/*.md' bash
tools/unattended/check-playbook.sh` printed `… · declared glob **/*.md` against a conf declaring no
such key; and with `BYPASS_BAN` stripped from the conf, `BYPASS_BAN='--no-verify' bash …` ran the
whole scan where the clean-environment run correctly printed `bypass scan SKIPPED`. The helper's own
comment promises *"the value this file's three siblings would see"*, and the siblings diverge:
`unattended.sh:212` and `check-unattended.sh:105` both assign `BYPASS_BAN=""` immediately before
sourcing, so they would see the empty string. `CONF_GLOB` has two references (`:87`, `:127`) so the
glob half is cosmetic; the `BYPASS_BAN` half arms a real check from the environment.

**Fix.** `unset -v "$1"` inside the subshell before the source — the same edit blocker 1 needs.
**Left-shift gate.** An arm exporting a bogus `BYPASS_BAN` with the conf declaring none, requiring
`bypass scan SKIPPED`.

---

## LOW 2 — `_pbatch`'s empty-reply fill can spell 2, which is exactly the PASS value the multi-line arm asserts

**`tools/unattended/check-unattended.sh:2244-2251`**, against the arm at **`:2329`**. *Raw id 6.*

The fold split the two degraded shapes and gave the non-splitting one a `fail 28` plus the sentinel
125, which is right. The empty branch still fills every `_PB_RC` slot with the batch's own `$_rc`,
byte-identical to the pre-batching wrapper — and `bash -c` exits **2** on a syntax error (verified on
this machine). A parser extracted in a form that will not parse — the exact state this branch exists
for — makes `_res` empty and `_rc` 2, so `[ "$_rc" -eq 2 ] || fail 28` at `:2329` SUCCEEDS and the
multi-line refusal arm reports a correct refusal from a harness that ran nothing. Injecting an
identical syntax error into `declared_list` in both `unattended.sh` and `check-playbook.sh` produced
10 failures from the `_dl_specs` arm, 3 from the template-list loop, and **zero** from the multi-line
arm.

Bounded, and that is why it is a low: the single-line `_dl_specs` batch runs first over the same
`$dl_a` and reds on any nonzero rc, so the leg still exits 1. What is lost is one arm going silently
unexercised inside a red run — the "a skip must announce itself" class. The fold's own stated rule
("a degraded-mode substitute must never be a value some assertion reads as clean") does not hold for
this arm.

**Fix.** Set a `_PB_DEAD=1` flag in the empty branch and have every arm check it before grading, so
the equivalence with the old wrapper survives without any arm mistaking the fill for an answer.
**Left-shift gate.** An arm that breaks the parser body's SYNTAX (not its logic) and asserts the
multi-line refusal is reported as dead rather than as satisfied.

---

## LOW 3 — `BYPASS_ROOTS` counts playbooks that declare a root, not distinct roots

**`tools/unattended/check-playbook.sh:425`.** *Raw id 13.*

The increment sits in the population loop, once per playbook with a non-empty `records`. Two
playbooks declaring the same root print the per-root note twice and then `bypass scan - 6 tracked
evidence record(s) read across 2 declared records root(s)` over 3 records in 1 root; a record naming
the flag yields two byte-identical `fail 10` lines. The comment at `:430` calls `BYPASS_SEEN` *"the
number that proves the scan reached the corpus"*, and round 7's high 1 was filed precisely because
inflating it is the defect — that fix closed the word-splitting route and left this one. No false
green (the guard at `:608` scales both counters together), so the cost is a misreported liveness
figure, a duplicated scan and duplicated refusals.

**Fix.** Accumulate declared roots into a newline-separated list inside the population loop,
`LC_ALL=C sort -u` after it closes, scan once per distinct root, and set `BYPASS_ROOTS` from the
deduped list. **Left-shift gate.** An arm with two playbooks sharing one records root, asserting one
per-root note, one refusal, and `BYPASS_ROOTS = 1`.

---

## LOW 4 — the budget is still typed, just typed as identifiers; and the neighbouring `--checks` line was not converted at all

**`tools/unattended/run-unattended-gates.sh:66-67`** and **`:71`**. *Raw ids 9, 19 and 14 — one
defect at two sites.*

`bash tools/unattended/run-unattended-gates.sh --help` prints *"the sum of the `BUDGET_*` ceilings
this file declares, currently 57 minutes"*. The file declares EIGHT ceilings (`:44-52`); the
expression hand-enumerates five (1800+900+300+300+120 = 3420 s = 57 min) while all eight sum to
3720 s = 62 min. The number is right for the `--selftests` line it sits under and **the sentence
attached to it is false**, three lines under a comment block asserting "THE BUDGET IS DERIVED, NEVER
TYPED". Line `:71` still reads `--checks     the three record/wiring checks - about 35 s`, beside
three ceilings in the same file whose own measured comments sum to 41 s — already wrong.

Round 7's low 2 was a value stated in prose beside the source that owns it, broken inside the file
that owns it. The fold closed the raise-a-ceiling case (a ceiling change now propagates) and left the
add-a-suite case: `run_one` derives `bkey` from the label (`:122`) and reds a suite with no ceiling
(`:130`), so a sixth selftest is FORCED to declare one and is silently absent from the advertised sum
and from the adjacent hard-typed "the five suites". Same class, one indirection along.

**Fix.** Collect the selftest labels into one array used by both the `run_one` calls and the help
sum, and emit the `--checks` figure as `$(( BUDGET_kit_gate + BUDGET_playbook_validity_gate +
BUDGET_skill_wiring ))` — both help lines then read the declarations. **Left-shift gate.** An arm
that adds a fake selftest label with its own `BUDGET_*` and asserts the `--help` total moves; today
it would not.

---

## LOW 5 — moving check 10 left its entire header comment behind, above an unrelated sweep

**`tools/unattended/check-playbook.sh:568-578`.** *Raw id 18.*

The live check 10 carries its header at `:407-421` (four paragraphs: the second-opinion rationale,
`IT NEEDS $rr AND NOTHING ELSE`, `THE POPULATION IS THE CENSUS OWN`, the `--record-set` limitation)
with its code at `:424-448`. Lines `:568-578` repeat three of those four near-verbatim — same
`10: THE BYPASS FLAG, READ BACK OUT OF WHAT LANDED` heading — sitting directly above the ORPHAN
RECORDS sweep at `:579-590`, which has its own comment and which they do not describe. A reader
arriving at the sweep meets a heading for a check that is not there, and a maintainer editing the
check-10 rationale has two sites and will find one. **Two answers to one question, in the commit that
mints a gotcha about two answers to one question.**

**Fix.** Delete `:568-578` down to the `# ORPHAN RECORDS:` line. **Left-shift gate.** None warranted
mechanically; record it as a documented check in the leg's own header review (a moved block takes its
comment with it), which is where §7 sends an ungateable class.

---

## LOW 6 — the new LOW 3 drift arm passes identically with and without the fix it is written for

**`tools/drift-audit/selftest.py:993`.** *Raw id 20.*

Confirmed empirically, not by reading: `tools/drift-audit` copied to a scratch dir with exactly the
two folded lines reverted (`specs_by_build.setdefault(sp.split("/")[2], …)` and
`build = rel.split("/")[2]`), then `test_readme_mechanism_drift` run. Result — `FAIL LOW 3: a
two-segment MEMORY_ROOT still names the BUILD, not the literal 'builds' — got ['builds']` and
**`ok LOW 3: and each README grades against its OWN spec set only`**. Under the merged spec set each
README's own token is still named in a 2026-01-05 revision later than its 2026-01-02 blame date, so
`nest["value"] == 2` either way. Only the sibling assertion at `:991` discriminates; the failing case
for the arm as LABELLED has never been observed, which is the charter's own
"gate whose failing case was never seen" rule applied to a test arm.

**Fix.** Make the two builds' tokens CROSS — build `one`'s README naming `--two-flag` — so the merged
spec set yields a different row count from the per-build one. Otherwise drop the count assertion and
let the slug assertion carry the arm, rather than implying a second independent check.
**Left-shift gate.** The arm IS the gate; it needs its RED observed. Add the fold's own rule to the
suite's header: an arm added to close a review finding is not landed until it has been seen to fail
against the pre-fix code, per assertion and not per test function.

---

## What has to happen before this lands

1. **Blocker 1** — `_conf_key` returns a status; a conf that will not source reds instead of skipping.
   Same edit takes the `unset -v` that closes low 1.
2. **Blocker 2** — `GITLS` becomes `-z` + `core.quotePath=false`, six consumers switch to
   `read -r -d ''`, and the tracked-but-absent refusal keeps its job.
3. **High 2** — `:268` joins its five siblings. It is a three-line change and it un-blinds the guard
   high 1 is about.
4. **High 1** — the zero-teeth red moves to the root and the arm becomes multi-root.
5. The six lows are cheap; low 6 is the one that matters most for the NEXT round, because a suite
   that cannot fail is how three of these survived the fold that was written to close them.

**The round-7 → round-8 trend, which is the number worth watching.** Round 7: raw 17, precision 0.94,
9 distinct defects, 3 blockers. Round 8: raw 20, precision 0.80, 10 distinct defects, 2 blockers.
Defect count did not fall, and both blockers are the same two round-7 blockers reached by narrower
routes. Precision falling from 0.94 to 0.80 is the expected signal over a hardened surface (§8) and
does not by itself argue for more lenses next round — it argues for scoping round 9 to the fold
diff alone, which is what this round did.
