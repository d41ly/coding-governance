**Serves:** diff-review TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# dScriptedRepeat — diff review, round 9 (the fold of round 8)

**Range:** `0a80f7bb...HEAD` — ONE commit, `4db111fa`, 12 files, 812 insertions and 74 deletions.
The subject is the FIX, not the diff round 8 already read: `tools/unattended/check-playbook.sh`
(+150), `tools/unattended/check-unattended.sh` (+27), `tools/unattended/run-unattended-gates.sh`
(+13), `tools/drift-audit/selftest.py` (+14), eleven new arms across two suites, and the records that
carry them. **ROUND 9.**

**Review shape:** raw 27 · confirmed 19 · refuted 8 · unverified 0 · precision 0.70. The eight refuted
died in the skeptic pass and are not reproduced here. The 19 confirmed findings collapse to **11
distinct defects**; five clusters were filed independently by two, three or four lenses, and that
corroboration is recorded per defect rather than counted again. Every mechanism below was reproduced
against a working tree before it was written down.

## Verdict: BLOCKED

*Two defects are landing-blocking, both in one file. The rest can land.*

**One blocker, two highs, two mediums, six lows.** This is the last round: the owner has authorised
this fold and then a merge and push with no further review. So this report grades for **what must not
land**, not for what could be better, and it says so per defect.

**The grading rule for "landing-blocking", stated once and applied uniformly.** A defect is
landing-blocking when it lets a violated tree read as **GREEN** — a silent pass, or a pass with the
failure text printed above an exit 0 that `run-gates` classifies as `ok`. A defect that reds a
legitimate tree is a shipped false refusal and it is genuinely bad, but it fails **loud**: an adopter
sees a message, is stopped, and can act. Silent green is the class that must not land, because it
removes the only signal anybody has. Two defects are on that side of the line and **both are in
`tools/unattended/check-unattended.sh`, within six lines of each other**. Everything else can land.

**The shape underneath both, stated once: the fold hardened one of two readers of the same file.**
Round 8's blocker 1 was `.unattended.conf` sourced into a leg's main shell, where an appended
`exit 0` ended the leg at status 0. The fold's answer was a sentinel probe. In `check-playbook.sh`
the answer is complete — `_conf_key` only ever sources inside a command substitution, so the conf
never touches the leg's shell at all, and both hijack shapes below bounce off it. In
`check-unattended.sh` the probe was bolted on **in front of** the main-shell source that was the
actual defect, and the source is still there at line 125. The probe closed the one shape it was
tested against and left the shell open. The fold record's claim that "both legs carry that now" is
true of the sentinel and false of the isolation.

---

## BLOCKER 1 — the conf can still HIJACK the leg it can no longer END

`tools/unattended/check-unattended.sh:125` (the probe it defeats is at `:120`)

The new sentinel probe stops `.unattended.conf` from terminating the leg. It does not stop the conf
from taking the leg over, because line 125 still sources that file into the leg's **main shell**,
below the `status=0` at `:81` and the `fail()` definition at `:82`. Round 8's blocker 1 is re-opened
by two one-line appends to the same tracked file, by the same commit-it-yourself route the fix's own
comment names as the threat.

**Shape A — an appended `trap 'exit 0' EXIT`.** The probe subshell runs an EXIT trap only when that
subshell exits, which is **after** `printf OK` has already been written to the command substitution.
The sentinel is therefore satisfied. The real source at `:125` then installs the trap in the main
shell, and the script's own final `exit "$status"` at `:2433` fires it.

**Shape B — an appended `fail()` that does nothing.** The source at `:125` sits **below** the `fail()`
definition at `:82`, so the conf silently replaces the verdict recorder itself. Every violation the
leg finds is recorded into a no-op.

Reproduced twice: once by the finder against the real script at `4db111fa` in a clone with `LANDER`
blanked, and once independently for this report against a minimal harness carrying the shipped
structure. Control run: rc 1 with one FAILED line. Shape A: **rc 0 with the FAILED line still
printed**. Shape B: **rc 0 with zero bytes of output** — byte-indistinguishable from a clean tree, and
strictly stealthier than the `exit 0` shape this same fold graded a blocker one round ago. `run-gates`
classifies purely on the exit code (`runleg` maps rc 0 to `st=ok`), so both read as `GATE ok`.

**Landing-blocking. This is the one that must not land.** The file's own header claims THE CONF CANNOT
END THIS LEG; shape A ends it, at 0.

**Fix (correct).** Stop sourcing into the main shell. Import the declared keys through a subshell, the
same isolation `_conf_key` already has: source inside `$( … )` with `|| exit 9`, loop the declared key
names emitting NUL-delimited name/value pairs, terminate the stream with an `OK` sentinel, and assign
from that stream in the parent.

**Fix (two-line stopgap, if the import is too large for this fold).** Move the `fail()` definition to
**after** line 125, and immediately after the source assert that `trap -p EXIT` is empty, exiting 2
with a message if it is not.

**Left-shift gate.** Add an arm to `check-unattended.test.sh` that appends each hijack shape to the
fixture conf and asserts the leg still **exits non-zero**. Grade the exit code, not the output text —
shape B produces no output to grep, so an output-only assertion cannot see it. The general form is one
arm per "the conf takes over the shell" primitive: `exit`, `return`, an EXIT trap, and a redefinition
of `fail`.

---

## HIGH 2 — the probe omits its sibling's abort guard, so a syntax error passes it

`tools/unattended/check-unattended.sh:120`

The probe sources the conf in a command substitution and checks for an `OK` sentinel, but without the
`|| exit 9` its sibling `_conf_key` carries at `check-playbook.sh:98`. A bash **parse error** in
`.unattended.conf` aborts the file but **returns to the caller** rather than ending the subshell, so
`printf OK` still runs and the probe passes. A `return 0` above an assignment behaves identically.
Only `exit 0` is actually caught.

Measured, in a clean clone at HEAD with one malformed `if` inserted above `LANDED_ANCHOR_CUTOFF`:
probe **PASSED**, the real source at `:125` returned 2 having sourced only the lines above the break,
all six keys the required-key loop at `:127` checks were still set, and `LANDED_ANCHOR_CUTOFF` came
back **empty** — which `:846-857` reads as `ak=remote`, grandfathering every LANDED record's missing
anchor kind. Leg rc 0, empty stdout, the bash error on stderr in a log nobody opens on a green run.
The same silent disarm is available for `SHARED_RECORDS`, `GENERATED_INDEXES` and
`UNITS_REGION_CUTOFF`.

Two corrections to the raw reports, neither of which saves the defect: the syntax error **does** reach
stderr, and an error placed **above** the floor keys reds loudly (measured rc 1 with
`CORE_FLOOR`/`HALT_FLOOR`/`DIRECTIVES_FLOOR` refusals). "Announcing nothing" holds only for an error
below the floor keys — which is where an attacker would put it, and where an accident is equally
likely, since the floors are declared early in the file.

**Landing-blocking.** Same class as blocker 1 — a one-line append to a tracked file the graded run can
commit itself, leaving `GATE ok` — and it is the fold's own headline guard, half-closed, with a
one-token repair. The fold's comment enumerates "a syntax error above the assignment" as a shape it
closes. It does not close it.

**Fix.** One token. Mirror the sibling exactly by adding `|| exit 9` to the source inside the probe's
command substitution, before the `printf OK`. The `|| exit 9` catches the non-zero-return shapes; the
missing `OK` catches the `exit` and `set -u` shapes.

**Left-shift gate.** One arm per abort shape against **both** readers, asserting they agree: append an
`exit 0`, a `return 0`, a parse error, and an unbound reference under `set -u` to the fixture conf,
and assert that `check-unattended.sh` and `check-playbook.sh` both refuse. Two readers of one config
giving two answers about whether it loaded is the invariant worth pinning, and it is cheaper to assert
than either shape list.

---

## HIGH 3 — `_conf_key` reds the bar on the kit's own documented empty-declaration idiom

`tools/unattended/check-playbook.sh:109`

The cross-check asserts "the file spells the key AND the sourced view is empty, therefore the source
never reached the assignment". That is unsound for a key **deliberately declared empty**, which is
this kit's own documented idiom: `tools/unattended/.unattended.conf.example` ships **eleven** keys
that way — `KICKOFF_ENGINE`, `KICKOFF_EXITS`, `DIRECTIVES_EXTRA`, `DIRECTIVES_EXTRA_TABLE`,
`ANCHOR_SCOPE`, `UNITS_REGION_CUTOFF`, `PHASES_EXTRA`, `DOD_EXTRA`, `HALT_CODES_EXTRA`,
`LANDER_MARKER`, `LANDED_ANCHOR_CUTOFF` — with comments reading "BLANK turns that check off" and
"Empty is legal".

Reproduced end to end. Declaring `PLAYBOOK_GLOB` empty in this repo's own `.unattended.conf` takes the
leg from rc 0 to **rc 1** with `PLAYBOOK check 10 FAILED - the project conf could not be sourced…` —
printed three lines above `bypass scan - tools/unattended/fixture-records: 3 tracked evidence
record(s) read`, which is a value read out of the conf the refusal claims did not source. The same run
disproves its own refusal. Isolated probe: rc 9 for a double-quoted empty value, rc 9 for a bare
trailing `=`, rc 9 for a single-quoted empty value, rc 9 for an untaken `if`-guarded assignment (the
leading-whitespace tolerance in the pattern), and rc 0 for the key absent or commented out.

`PLAYBOOK_GLOB` makes it worse rather than better: it has exactly one consumer in the whole kit, the
optional-glob decoration on the population note at `:157`, and
`memory/map/features/playbook-mode.md` records it as not yet widening the population. So an adopter
can hard-red the merge bar by spelling an empty value for a key the leg does not use for anything.

**NOT landing-blocking**, by the rule at the top: it fails loud, and this repo's conf declares neither
affected key empty, so the bar is green today. It ships to every adopter as a false red whose message
sends them hunting an abort that is not there. One caveat on severity, recorded because it narrows the
blast radius: an empty `BYPASS_BAN` is independently refused as a required key by
`check-unattended.sh:127-130`, so that half is a correct red with a wrong cause rather than a wholly
false one.

**Fix.** Have the sentinel report **set-ness** rather than the value: emit a marker derived from the
`${VAR+…}` form beside the value, separated by a control byte, and take the `return 9` branch only
when the grep matches **and** the set-marker is absent. That keeps the `return 0`-above-the-assignment
case redding while letting an explicitly empty declaration resolve to the empty string at rc 0, and it
stops reading the file's text to guess at a fact the shell already knows.

**Left-shift gate.** An arm asserting the leg stays **green** with each of the eleven example keys
spelled as an empty declaration — the shipped example file is the natural fixture, and the invariant is
"the kit's own documented conf never reds the kit's own leg". The suite currently pins three abort
shapes and no legal shape at all, which is why a false refusal shipped: an arm set that only ever
stages breaks cannot see an over-refusal.

---

## MEDIUM 4 — `_conf_key` reads the source's exit STATUS as a liveness verdict

`tools/unattended/check-playbook.sh:98`

The source inside the helper carries `|| exit 9`, which treats a non-zero return as "the conf did not
load". But a sourced file returns the status of its **last executed command**, so a fully loaded,
entirely legitimate conf whose tail is a conditional returns non-zero with every key correctly set.

Reproduced against the shipped helper. Appending an ordinary CI-guarded conditional assignment to this
repo's own conf makes the source return 1 with `BYPASS_BAN` and `LANDER` both correctly set,
`_conf_key` exit 9, and the leg red at rc 1 with two `check 10 FAILED` lines reading "the project conf
could not be sourced" plus a "bypass scan NOT RUN" note. Every key loaded; nothing was unsourced. A
trailing conditional, `case` or `grep` is an ordinary idiom in a shell config that the driver, the
sibling leg and every adopter all source.

**NOT landing-blocking** — loud, and this repo's conf ends on an assignment. Same false-cause class as
HIGH 3 and a distinct line with a distinct mechanism, which is why it is filed separately.

**Fix.** Separate "the file aborted" from "the file's last command returned non-zero": drop the
`|| exit 9` and rely on the `OK` sentinel alone, since `exit`, an unbound reference under `set -u`,
and a parse error all suppress it; or fold the status into the sentinel and treat only a genuine abort
as rc 9.

**Left-shift gate.** Same arm family as HIGH 3, on the legal-shapes side: a conf whose last line is a
false conditional must leave the leg green.

---

## MEDIUM 5 — the per-root zero-records refusal reds every freshly authored playbook

`tools/unattended/check-playbook.sh:498`

The relocated refusal fires whenever a playbook declares a records root, a bypass flag is declared,
and that root holds no tracked records. `BYPASS_BAN` is a required key (`check-unattended.sh:127`), so
the refusal is armed in **every** adopter tree, and the playbook-validity leg in
`tools/gate-legs.json:588-594` carries **no guard**, so it runs on every bar including the pre-push
full run.

That is the ordinary state of a newly authored playbook. Check 8 at `:501` forces a playbook declaring
a grain to declare a records root, and `:498` then reds until at least one tracked record exists under
it — which only a **run** can produce, and a run cannot read the playbook until it is reachable from a
remote-observed BASE, which pushing is what the red blocks. Reproduced: committing a second playbook
pointed at a fresh empty root takes the leg from rc 0 to rc 1. The fold's own new arm at
`check-playbook.test.sh:463-470` constructs exactly this shape and calls it the failing case.

It also contradicts the leg's own stated split fifteen lines below and in its header at `:19-21`: a
zero-**piece** enumeration is a DEAD PROBE note precisely because only `--close` blocks on it, while a
zero-**record** root is a hard fail. A brand-new playbook has both, and gets two opposite verdicts
from one leg.

**NOT landing-blocking** — this tree ships one playbook and its root holds three records, so the bar is
green. An escape exists (an attended piece-record writer, or a placeholder record) but is
undocumented. Deliberate and tested is not the same as correct: it reds a legitimate tree.

**Fix.** Red only where the emptiness is not explained by "nothing has run yet": keep `fail 10` when
the root enumerates zero records **while the playbook's own grain enumerates pieces**, and downgrade
to the existing per-root note when both are zero. That leaves the fixture-shaped failing case — a full
grain joined to an empty root — reachable, which is what the new arm is really testing.

**Left-shift gate.** An arm asserting a playbook with an empty grain and an empty records root is
**green**, beside the existing arm asserting a playbook with a full grain and an empty root is red.
The pair is the actual rule; only one half is currently pinned.

---

## LOW 6 — `CONF_SOURCE_OK` is derived from one of two reads, so the leg contradicts itself

`tools/unattended/check-playbook.sh:124`

`CONF_SOURCE_OK` is assigned from the `BYPASS_BAN` read's status only. The `PLAYBOOK_GLOB` read at
`:112` has its own `fail 10` and never touches the flag, so the two `_conf_key` calls can disagree.
Reproduced in the same run as HIGH 3, verbatim: `PLAYBOOK check 10 FAILED - the project conf could not
be sourced…` followed later by `playbook: bypass scan - 3 tracked evidence record(s) read across 1
declared records root(s)`. One leg, two contradictory statements about whether the conf sourced, and a
reader cannot tell which to believe.

Contingent on HIGH 3 for its only realistic trigger — fixing the value-keyed cross-check removes the
disagreement — but it is a distinct line with a distinct fix.

**Fix.** Accumulate rather than overwrite: initialise `CONF_SOURCE_OK=1` before `:112` and set it to 0
after **each** `_conf_key` call that returns 9.

**Left-shift gate.** Assert that no single run emits both a "could not be sourced" refusal and a
"bypass scan - N records read" note. That is a cheap whole-output invariant and it catches the class
rather than this instance.

---

## LOW 7 — the two numbers in the bypass-scan note count different populations

`tools/unattended/check-playbook.sh:648` (the counter is at `:487`)

Round 8's low 3 was "the number beside the record count described a different population". The fold
de-duplicated `BYPASS_ROOTS` via the `BYPASS_ROOT_LIST` case at `:471-473` and left `BYPASS_SEEN`
incrementing once per **(playbook, record)** at `:487`. The pair now describes two populations in the
opposite direction from before.

Reproduced: two playbooks sharing `tools/unattended/fixture-records` print the per-root note twice and
then `bypass scan - 6 tracked evidence record(s) read across 1 declared records root(s)` over a
three-record corpus — a reader computes six records under one root. The pre-fix pair, six across two,
was at least self-consistent. `BYPASS_SEEN`'s only remaining consumer is this note, since the
aggregate refusal that used to read it moved per-root, so the counter's only remaining job is to be
wrong. The corpus is also re-grepped once per playbook, so a record carrying the flag emits the
check-10 refusal N times.

**Note-only, never reds. Not landing-blocking.** Filed because the counter's stated job is proving the
scan reached the corpus, and the figure it prints is provably not that.

**Fix.** Increment `BYPASS_SEEN` (and run the scan) only on a root's **first** sighting — move the
bypass-scan block inside the fresh-root arm of the `BYPASS_ROOT_LIST` case.

**Left-shift gate.** An arm with two playbooks sharing one root, asserting the aggregate equals
`git ls-files` over the distinct roots. Derive the expected number in the arm; do not type it.

---

## LOW 8 — `_seen_here` counts records that were READABLE, and the refusal claims they were not ENUMERATED

`tools/unattended/check-playbook.sh:498` (the counter is at `:487`, the branch that skips it at `:483`)

The unreadable-record branch fails and `continue`s **without** touching `_seen_here`, which is
incremented only past the file-exists test. A root whose tracked records are all absent from the
worktree therefore leaves `_seen_here` at 0, and the `:498` refusal fires with the cause "that root
enumerates ZERO tracked records" — which is false, since `GITLS` enumerated them.

Reproduced: moving the three tracked fixture records out of the worktree yields rc 1 with three
truthful "not readable in this worktree" refusals **and** a fourth asserting the root enumerated
nothing. Reachable beyond sparse checkouts — an unstaged `rm` is an ordinary working state — and the
second sentence sends the reader to look for a missing directory that is fully populated in the index.

**Not landing-blocking**: the leg already reds correctly at `:484`, so only the stated cause is wrong.

**Fix.** Count enumeration separately from readability: increment a new `_enum_here` **before** the
file-exists test and gate `:498` on that being zero, leaving `_seen_here` as the read counter for the
note at `:497`.

**Left-shift gate.** An arm that removes a tracked record from the worktree and asserts the
"enumerates ZERO" refusal does **not** appear. This is the general "a refusal's stated cause is the
cause that happened" class, and it is worth one arm per refusal that names a mechanism.

---

## LOW 9 — the new HIGH-1 arm's second assertion cannot fail

`tools/unattended/check-playbook.test.sh:472`

The arm greps the whole captured leg output for the empty root's path, to prove the `:498` refusal
names the root that contributed nothing. But `check-playbook.sh:497` emits a per-root
`bypass scan - <root>: <n> tracked evidence record(s) read` note for **every** declared root, gated
only on `COUNTS_FOR` being empty — and the suite's `run()` at `check-playbook.test.sh:55` invokes the
leg with no arguments, so `COUNTS_FOR` is always empty and the note always fires, before the `fail 10`
and irrespective of it.

Delete the `fail 10` at `:498` entirely and this assertion stays green. Only the first assertion, the
long refusal sentence at `:469`, discriminates. It also contributes to the suite's assertion total as
if it were coverage.

**Test-only, not landing-blocking.** Filed because it is exactly the could-not-fail shape this fold
went hunting for in the drift-audit fixture, one file over — the fold found that instance and created
this one.

**Fix.** Assert the root name **inside** the refusal's own text: grep for the refusal's distinctive
tail with the root and the playbook path appended, rather than for the bare root anywhere in the
stream.

**Left-shift gate.** The class fix, not this instance: every new arm is landed only after its failing
case has been observed (§7's stage-the-break, confirm RED, unstage). Mechanically, a suite-level
mutation check — revert the fix under test, assert the arm reds — is the only thing that catches a
vacuous assertion, and it is cheap here because each arm already stages its own fixture.

---

## LOW 10 — the help budget sums inherited environment variables, and evaluates their contents

`tools/unattended/run-unattended-gates.sh:70`

The `${!BUDGET_@}` expansion enumerates every `BUDGET_`-prefixed name in scope, which includes
**inherited exported** variables, and the arithmetic accumulation then evaluates their contents. Both
halves reproduced: with two budgets totalling 30 declared, a third exported from the caller's
environment pushed the sum to 1029, falsifying the help text's own claim that the figure is "every
`BUDGET_*` ceiling this file declares". The arithmetic-injection half also holds under this script's
`set -u`, because the array-subscript form names a variable that is bound — a crafted value executed a
command substitution during `--help`.

**Not landing-blocking.** Help-text path only, and the environment holder already runs code here, so
no privilege boundary is crossed. It is nonetheless a real derivation defect in a block whose own
comment insists the set must never be hand-kept.

**Fix.** Filter to integers inside the loop, skipping any value that is empty or contains a non-digit,
and restrict the name set to the file's own declarations rather than to everything in scope.

**Left-shift gate.** Run `--help` with a hostile `BUDGET_*` exported and assert the printed figure is
unchanged. One arm, and it pins both halves at once.

---

## LOW 11 — three specs bumped to rev-5 and left the header date at the previous day

`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:3`, and `-14.md:3`, `-15.md:3`

All three read `CLOSED · rev-5 · 2026-08-23` while each file's own §9 rev-5 entry is dated
**2026-08-24** (specs `-13:111`, `-14:103`, `-15:109`) and the fold commit `4db111fa` is dated
2026-08-24. `memory/TEMPLATE-SPEC.md:52` defines the header date as the last-change date and `:53`
requires a rev bump on any material content change — the rev moved and the date did not.

Not a dead field: `tools/drift-audit/drift_signals.py:37` keys signal 6's cutoff on exactly that
header date. The generated units table at `memory/builds/dScriptedRepeat/README.md:196-198` now
renders `rev-5 | 2026-08-23` for all three, and no gate reds on it.

**Not landing-blocking.** Filed because it is a record contradicting its own content, inside the fold
whose entire subject is that class.

**Fix.** Set the header date to 2026-08-24 in all three files and re-run
`python tools/memory-tree/gen_build_index.py` so the units table and `memory/LIVE.md` regenerate in
the same commit.

**Left-shift gate.** A hygiene check asserting a spec's status-header date is not older than the date
of its highest rev-log entry. Both values are already in the file, so the comparison needs no new data.

---

## What the fold got right, recorded so the next reader does not re-litigate it

Six of round 8's ten defects are closed cleanly, and each of the prompt's named high-value lenses
returned a negative that is worth writing down.

- **`GITLS` and the NUL stream.** `git -c core.quotePath=false ls-files -z` with all six consumers
  reading NUL-delimited from **process substitution** is correct, and the choice is load-bearing
  rather than stylistic: command substitution strips NUL bytes, so a heredoc could not have carried
  this stream. The variable-lifetime lens found no regression — process substitution keeps each loop in
  the current shell, so `BYPASS_SEEN`, `_seen_here` and `npieces` survive their loops and the `return`
  inside `record_for` still returns from the function rather than from a subshell. This was the
  highest-risk mechanical change in the fold and it is sound.
- **`npieces` counted by the loop** equals what the census reports; the second-pass-over-a-variable
  shape is gone and no lens found a divergence.
- **The distinct-root membership test cannot collide.** Roots are pipe-delimited and matched with the
  delimiters included, so no root is a prefix-match for another. LOW 7 is about the *other* counter,
  not this one.
- **`exit "$status"` in `check-unattended.sh` always runs after `status` is set** — `status=0` sits at
  `:81`, above every path that reaches an exit.
- **The drift-audit crossed-token fixture** now discriminates on both assertions; the count assertion
  yields 2 under correct grouping and 3 under a slug collapse, which is what the round-8 finding asked
  for.
- **Ten of the eleven new arms** stage a break that the fix actually repairs. Only the one at LOW 9 is
  vacuous, and only in its second assertion.

## Landing recommendation

**Fix BLOCKER 1 and HIGH 2 before the merge.** They are the same file, six lines apart, and both have
a repair small enough to land without a further review round: one is a two-line stopgap (move `fail()`
below the source, assert no EXIT trap) or the subshell import, and the other is inserting `|| exit 9`.
Both are silent-green defeats of a merge-bar leg, which is the only class that genuinely must not
land.

**Everything else can land.** HIGH 3, the two mediums and the six lows are either loud false refusals
that stop an adopter with a wrong message, note-only miscounts, one vacuous test assertion, or a stale
date. All are worth a follow-up unit; none of them lets a violated tree read as green, and none of
them is worth blocking a fold the owner has already authorised.

One caveat on this report's own coverage, stated plainly because a reader should not assume more than
it has: this round read the **fix**, not the diff round 8 already read, and its lenses were pointed at
the six mechanisms the fold changed. The unchanged bulk of `check-playbook.sh` and
`check-unattended.sh` was not re-reviewed here, and rounds 1 through 8 are where that coverage lives.
