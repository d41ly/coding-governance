**Serves:** diff-review TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4

# Diff review round 1 — the cumulative diff landing on main

*Range `bd0348f3b69be7af7c8452cf271990b176ddb43f...HEAD`, reviewed once at the integration boundary
per §8 rather than per increment. **ROUND 1.** Node d, 2026-08-25.*

**Review shape.** Raw 24, confirmed 20, refuted 4, unverified 0, precision 0.83. The 20 confirmed
reports collapse to **13 distinct defects** — four lenses independently found the `gen_build_index.py`
marker-predicate skew and three found the discarded `missing_units` status, which is itself a signal:
the same class was reachable from four different reading angles.

## Verdict: BLOCKED

One blocker, five high, five medium, two low. The blocker is not a peripheral defect — it is the
unit-1 deliverable. `TOOL-dHonouredPark-1` landed under the sentence "the authored roster pair is
mandatory on every build README, **and its DoD term can now fail**". The term still cannot fail on a
malformed pair, because the refusal `roster_ids` raises is thrown away one frame above where it was
carefully propagated. Three of the four `--plan` findings are regressions against BASE, reproduced by
running both revisions over one fixture tree.

Two shipped documents in this same diff — `memory/guides/UNATTENDED-PROTOCOL.md` and the rendered
`.claude/skills/unattended/SKILL.md` — assert behaviour the code does not deliver. That is a second
class worth naming on its own: the diff wrote the promise and the code in the same pass, and the
promise is the copy that is wrong.

| Severity | Count | Distinct sites |
|---|---|---|
| BLOCKER | 1 | `tools/unattended/unattended.sh` |
| HIGH | 5 | `unattended.sh`, `gen_build_index.py`, `memory/backlog/TOOL.md` |
| MEDIUM | 5 | `unattended.sh`, `gen_build_index.py`, `tools/check-dead-paths.sh` |
| LOW | 2 | `tools/check-dead-paths.sh`, `unattended.test.sh` |

---

## BLOCKER

### B1 — `missing_units`' exit 3 is discarded, so `build-complete` term 3 still passes vacuously

**`tools/unattended/unattended.sh:2762`** (defect also at `:1659` and `:1665`, reported as H1).

`roster_ids` (`:1487`) returns 3 when `region` refuses a malformed `<!-- roster:units -->` pair, and
`missing_units` (`:1536`) propagates it with `want=$(roster_ids "$1") || return 3` and empty stdout.
Term 3 then reads:

```sh
_bcmiss=$(missing_units "$slug" "$M/builds/$slug")
if [ -n "$_bcmiss" ]; then
```

A bare assignment whose status nothing consults. `set -e` is off (only `set -u`, `:40`), so the
propagation stops dead at the `=`. `_bcmiss` is empty, the test is false, and the term reports a pass
it did not earn.

Reproduced by three independent lenses. A README with a duplicated open marker gives
`missing_units rc=3, stdout empty` and `TERM 3 PASSES`; the same README with a well-formed pair
correctly reports both fixture units as missing. A trailing space on the open marker does the
same, because `region` (`:470`) sets `bad=1` unless the marker line equals the marker exactly.

Nothing upstream covers it. The guard at `:2738` validates the GENERATED `gen:build-units` pair, not
the authored one; terms 1, 2 and 4 all read the generated region. Term 3 is the only reader of the
authored roster at close, and the only term that can see a planned-but-unspecced unit.

**Why blocker rather than high.** This is the DoD item that means "the entire build is done", and it
gates an unattended merge and push with no owner turn. The comment at `:1520-1523` claims exactly this
vacuous pass was removed — "THE STATUS IS TESTED … a status this caller did not read would change
nothing observable". It was tested at the callee and left unread at the caller, which is §7's
gate-that-cannot-fail with the fix applied one frame too low. It is also reachable past a green bar:
the new hygiene trigger accepts marker shapes `region()` refuses (H4).

**Fix.**

```sh
if ! _bcmiss=$(missing_units "$slug" "$M/builds/$slug"); then
  DOD_OUT="the build README's authored roster pair is absent or malformed, so the planned-vs-specced join this term makes cannot be made: $(readme_of "$slug")"
  return 1
fi
if [ -n "$_bcmiss" ]; then
  ...
```

**Left-shift gate.** Two legs, because they fail differently.

1. A behavioural arm in `tools/unattended/unattended.test.sh`: stage a duplicated `<!-- roster:units -->`
   open marker on a build whose roster names an unspecced id, assert `--close` REFUSES with the new
   message. Observe it RED before wiring it — a gate whose failing case has never been seen is an
   assertion about nothing (§7).
2. A source-level arm gating the CLASS, not this instance: assert that no call site of `roster_ids`,
   `missing_units` or `unit_ids_of` is a bare `$( )` whose status nothing reads. The suite already
   carries source-level arms of this shape (`:1918-1922`), so the machinery exists. Fixing only line
   2762 and testing only line 2762 certifies coverage this diff does not have.

---

## HIGH

### H1 — the same discarded status in `verb_plan`, where it prints an affirmatively false sentence

**`tools/unattended/unattended.sh:1659` and `:1665`.**

`for miss in $(missing_units "$slug" "$dir")` discards rc 3 and iterates zero times, leaving
`nmiss=0`. `if [ -n "$(roster_ids "$slug")" ]` then tests only the string, so the else branch prints:

> `roster: the generated units region, in build order (the authored pair names no id of this build)`

That sentence is false. The pair exists; it could not be parsed. Reproduced on a README carrying two
`roster:units` pairs, the first naming an unspecced `ARCH-tPlan-9`: zero MISSING rows, `next: none`,
exit 0. `roster_ids` is also invoked twice more inside the branch, so no call in the region can
surface a status.

**High rather than medium** because two documents written by this same diff promise the opposite.
`.claude/skills/unattended/SKILL.md:465` and `tools/unattended/SKILL.template.md` both say "a roster
whose markers are malformed is a named refusal rather than a complete-looking list". The verb's own
comment block at `:1581-1587` states the same discipline for the sibling region. This is the
complete-looking list the unit exists to stop printing.

`memory/guides/UNATTENDED-PROTOCOL.md:429` is careful and scopes its promise to the generated region,
so only the skill doc overclaims.

**Fix.** Resolve once, keep the status, drive both consumers off the resolved value.

```sh
_want=$(roster_ids "$slug") || { fail 42 "the build README carries a roster marker but not exactly one well-formed pair: $_rmp"; return 1; }
```

**Left-shift gate.** The source-level arm from B1 covers this site too — that is the point of gating
the class. Add one behavioural arm asserting `--plan` over a malformed roster exits non-zero with the
refusal text, beside the existing ABSENT and MALFORMED arms for the units region.

### H2 — `--plan` over a well-formed but EMPTY units region claims every spec is terminal

**`tools/unattended/unattended.sh:1629`** (guard missing after `:1597`).

`region` exits 0 with empty stdout for a well-formed pair enclosing nothing, so `for id in
$(unit_rows ...)` runs zero times and `:1670` prints `next: none - every tracked spec is terminal`,
exit 0, over a build holding live SPECCED units.

Verified as a REGRESSION by running both revisions over one tree. Fixture: a well-formed
`gen:build-units` pair carrying no unit rows — the exact bytes `gen_build_index.py:746-747` emits for
a build with no status-header spec — plus one tracked spec at SPECCED. HEAD prints only the roster
line and `next: none`; the pre-diff copy at `c80d9233^` prints `ARCH-tPlan-1 SPECCED READY` and
`next: ARCH-tPlan-1 (READY - build it)`.

The state is not exotic. It is every build between its first `--write` and the next `--write` after
spec #1 exists — the first unit of every build. `build-complete` guards exactly this case at `:2751`
("the generated units region carries no unit ROWS, and 'no unit row is non-terminal' is vacuously true
over none of them"); `verb_plan` took the ABSENT and MALFORMED guards from that pattern and not the
EMPTY one.

**Fix.** Add the rows guard the DoD term already spells, after the `region` well-formedness check.

```sh
[ -n "$(unit_rows "$_rmp")" ] || { fail 42 "the generated units region carries no unit rows, so this verb has no unit set to grade: $_rmp · repair: the --write mode of tools/memory-tree/gen_build_index.py"; return 1; }
```

**Left-shift gate.** A `unattended.test.sh` arm per vacuity shape — absent pair, malformed pair, empty
pair — asserting each is a named refusal. The generic form worth adopting: any verb that derives its
unit SET from a region gets all three arms, because two of the three were already written and the
third is the one that shipped broken.

### H3 — `--plan`'s id extraction cannot match a slug containing a digit

**`tools/unattended/unattended.sh:1631`.**

```sh
grep -oE '[A-Z]+-[A-Za-z]+-[0-9]+' | head -1
```

No digits admitted in the slug segment. Every other reader in the repo admits them: `check_slug`
(`:923-928`) refuses only `*[!A-Za-z0-9-]*`, the memory-tree folder grammar is
`^[A-Za-z][A-Za-z0-9-]*$`, and the spec-heading parser is `^# [A-Za-z0-9][A-Za-z0-9-]* `.

Reproduced end-to-end: for slug `tRun2` with one OPEN spec `ARCH-tRun2-1` and a well-formed units
region naming it, `--plan` printed ZERO unit rows and `next: none - every tracked spec is terminal`,
exit 0 — while the same output's roster line reported `1 id(s)`. Two halves of one report
contradicting each other on screen.

Also a regression: at BASE the loop iterated the spec FILES and parsed the id from the wider heading
regex, so such units listed fine.

**Fix.** Scope the extraction to the build, matching `unit_ids_of`: `grep -oE "[A-Z]+-$slug-[0-9]+" |
head -1`. That fixes the digit case and the not-slug-scoped case at once, and it removes a third
spelling of a pattern whose sibling helper `_ids_of` (`:1563`) already spells
`[A-Z]+-[A-Za-z0-9]+-[0-9]+` — with a comment saying it exists so two callers cannot disagree. Three
copies, two spellings.

**Left-shift gate.** A grep-based source arm asserting `unattended.sh` contains exactly ONE id-shape
regex literal, and that every other id extraction routes through `_ids_of` or interpolates `$slug`.
This is the single-source-of-truth rule (§12) applied to a regex, and it is cheap: one `grep -c`.

### H4 — the hygiene gate certifies roster pairs the driver refuses

**`tools/memory-tree/gen_build_index.py:1283-1284`.**

```python
n_open = sum(1 for l in lines if l.strip() == PLAN_OPEN)
```

`l.strip()` — while every consumer of that pair requires the marker at column 0 with nothing around
it. `_marker_index` in the same file (`:965-970`) compares the whole line modulo one trailing CR;
`region()` in `tools/unattended/unattended.sh:470` requires `index(ln,o)==1 && ln==o`.

Measured on both sides, over three fixtures. An indented pair and a trailing-space marker both return
`[]` from `slot_violations` (gate GREEN) while `region`'s awk exits 3. A well-formed pair is green on
both, a duplicated pair is red on both, and a CR on the marker line is accepted by both — so the
divergence is exactly leading and trailing whitespace. A third shape passes too: a well-formed pair
plus a stray column-1 `<!-- roster:units --> (see below)` line placed before it.

For an UNBOUND build README — the majority, since the canon and slot budgets bind only the registry's
subset — trigger 4 is the only check that runs. So the gate is the sole enforcement, and it certifies
the shape that makes B1 reachable with a green bar. No trailing-whitespace leg exists in
`tools/gate-legs.json`, `core.whitespace` is unset, and `check-memory-hygiene.sh` has no such check,
so nothing else catches it.

The block's own comment asserts "THE DISCIPLINE IS THE DRIVER'S, not `_marker_index`'s", and that "an
assertion built on the helper would accept what the driver rejects". It avoided the helper and did not
adopt the driver's rules, so on this axis the new predicate is LOOSER than the helper it replaced —
stricter only on duplicates and order.

**Fix.** Match the driver byte-for-byte. A local predicate reused by `n_open`, `n_close` and both
`next(...)` lookups:

```python
def _is(l, m): return (l[:-1] if l.endswith("\r") else l) == m
```

and add a violation for any line where `l.rstrip("\r").startswith(PLAN_OPEN)` but is not equal to it —
the `bad = 1` arm of `region`.

**Left-shift gate.** Two selftest arms beside the existing absent / duplicated / transposed three: an
indented pair and a trailing-space marker, each asserting the gate REDS. Better still, and the general
form: a differential arm that feeds each fixture to BOTH `slot_violations` and the driver's `region`
awk and asserts the verdicts agree. Two readers of one marker must normalize identically or neither
verdict means anything.

### H5 — three backlog rows still read OPEN over work this diff shipped

**`memory/backlog/TOOL.md:7`** (and `:8`, `:9`).

`TOOL-dHonouredPark-2`, `-3` and `-4` still read `OPEN` while all four specs carry
`**Status:** CLOSED`, the build README's generated block reports every unit CLOSED, and
`memory/ledger/2026-08.md:53` reports the build CLOSED. Row `-4` still ends "NOT RULED" while
`memory/DECISIONS.md:97` records the very ruling it says is missing.

`git diff 60ba1d60..HEAD -- memory/backlog/TOOL.md` shows only `-1` was flipped. The correct treatment
is demonstrated in the same commit range: `TOOL-aPacedTurnstile-14` was flipped OPEN to CLOSED with a
closing clause naming what closed it.

This is a §1 Definition-of-Done miss on the landing commit, not a code defect. §6 makes this backlog
the mutable index a session reads at DoR to find live work, so three settled items now advertise
themselves as open and a later session routed by this index re-opens settled work or re-mints against
it.

**Fix.** Flip lines 7-9 to CLOSED and append the closing clause naming the unit that closed each,
matching the shape used on line 152.

**Left-shift gate.** A hygiene check that joins the backlog against the spec corpus: a backlog row
whose id is defined by a spec carrying a terminal status, while the row itself is non-terminal, reds.
This is derivable from data both files already carry, needs no new authored artifact, and catches the
whole class rather than these three rows.

---

## MEDIUM

### M1 — `--plan` and `--status` grade terminality from two different sources

**`tools/unattended/unattended.sh:1650`.**

`case "$st" in CLOSED|WONTDO) state="DONE"` reads `st` out of the SPEC file, while `nonterminal_units`
(`:1560`, feeding `--status` at `:2271`) filters on `| CLOSED |` / `| WONTDO |` in the rendered ROW.

Reproduced: a region row reading SPECCED beside a spec header reading CLOSED gives `--plan` →
`ARCH-tPlan-1 CLOSED DONE` and `next: none`, while `nonterminal_units` still returns that row and
`--status` names it. Two verbs, two answers, one question.

The skew is only possible on a stale region, but stale is the ordinary mid-pass state the driver is
read in — between editing a spec header and the next `gen_build_index.py --write`. The drift gate only
binds at the push boundary. The impact is not symmetric: `--plan` says the build is done, the agent
goes to `--close`, and `build-complete` term 5 blocks on the row the other source still calls
non-terminal.

`memory/guides/UNATTENDED-PROTOCOL.md:424` and `tools/unattended/PROTOCOL.template.md:424`, both
written by this diff, assert the two agree "by construction rather than by coincidence". The SET and
the ORDER now do. The terminality grading does not.

**Fix.** Take the status from the same place both verbs do — parse the row's Status column inside the
`unit_rows` loop and use it for the `CLOSED|WONTDO` mapping. Or drop the "by construction" clause from
both protocol copies and say the agreement holds only over a freshly rendered region. Do not ship both
sources and the claim.

**Left-shift gate.** An arm that stages a region row disagreeing with its spec header and asserts
`--plan` and `--status` name the SAME next unit. That arm fails today, which is the point.

### M2 — a HALF roster pair is reported as "DUPLICATED"

**`tools/memory-tree/gen_build_index.py:1287.`**

`elif n_open != 1 or n_close != 1` is a catch-all after the both-absent test, so every half pair is
labelled with a condition that did not occur. Measured: an open-only README yields "the authored
roster pair is DUPLICATED — 1 open and 0 close marker(s)"; the mirror yields "0 open and 1 close".

The pair is AUTHORED — nothing emits it — so a dropped close marker is the likeliest slip, and the
reader is sent to hunt a duplicate that does not exist. The trigger's own comment makes naming the
condition the whole point: "a single 'malformed' verdict sends a reader to diff a file against a rule
it does not state." A verdict naming the wrong condition is strictly worse than a generic one.

Verdict correctness is unaffected — the file still reds — and the counts are printed in the same
sentence, so a careful reader recovers. That is why this is medium.

**Fix.** Split the branch: `elif n_open == 0 or n_close == 0:` → "the authored roster pair is
INCOMPLETE — %d open and %d close marker(s); the pair needs one of each"; keep DUPLICATED for
`n_open > 1 or n_close > 1`.

**Left-shift gate.** Arms for 1/0 and 0/1 beside the existing 0/0, 2/1 and transposed 1/1 — the
existing arms cover four of the six reachable shapes, and both gaps are the same missing branch. The
general form: when a check's messages are armed BY NAME, every branch of the message needs an arm, and
a catch-all `elif` is the shape that hides one.

### M3 — the waiver resolver trims the file line but not its own needle

**`tools/check-dead-paths.sh:171`.**

`t = ENVIRON["NEEDLE"]` is taken verbatim while the file side is trimmed at `:172`
(`sub(/^[ \t]+/, "", s)`), so a row whose text field is a verbatim copy of an indented carrier never
resolves.

Reproduced against the live tree: `tools/memory-tree/check-memory-hygiene.test.sh:1314` is indented
two spaces, and feeding that line verbatim as NEEDLE produces no match. The row would print under
"stale waiver(s) — the carrier they excuse is gone; delete the row", whose remedy is the wrong action
and names the wrong cause.

Neither the gate header nor the registry header says the text must be pre-trimmed. The eight seeded
rows happen to be hand-trimmed, so the population that would have caught this is empty — which is why
it shipped, not why it is acceptable.

One correction carried from the skeptic and worth keeping: deleting such a row does NOT silently widen
the registry, because the carrier returns as an unwaived hit and reds at `:224`. The misdiagnosis is
the harm, not silent widening.

**Fix.** Normalize both sides. In the BEGIN block, after `t = ENVIRON["NEEDLE"]`, add
`sub(/^[ \t]+/, "", t); sub(/[ \t]+$/, "", t)`, and state in the registry header that surrounding
whitespace is not part of the key.

**Left-shift gate.** A `check-dead-paths.test.sh` arm whose fixture carrier is INDENTED and whose
waiver row copies it verbatim, asserting the row resolves. The population being empty on the real tree
is exactly why the arm has to build its own.

### M4 — the gate's own remedy prints a truncated copy of the key it tells you to paste

**`tools/check-dead-paths.sh:224`** (and `:200`).

Both the unwaived-hit report and the `--list` authoring aid print
`sed 's/^[[:space:]]*//' | cut -c1-90`. Under the old `<path>:<line>` keying the printed line number
WAS the key and copy-paste worked. The re-key made the printed TEXT the key, and 4 of the 8 rows in
the live registry carry text longer than 90 bytes (111, 105, 97, 137).

Following the sentence the gate itself prints — "add a row to `tools/dead-path-waivers.txt` with the
reason the name must stay" — therefore produces a row that lands in `unresolved` and reds as stale, on
a run the author was trying to make green. A regression the re-key introduced, with no test arm over
it.

**Fix.** Emit a paste-ready row rather than a preview: print the full trimmed line, or add a
`--waiver-row <path>:<line>` mode that prints the four tab-separated fields with the reason blank.
Keep the 90-character cut only for the `--list` overview column, where it is a display and not a key.

**Left-shift gate.** An arm that takes the gate's own remedy output for a carrier longer than 90
bytes, pastes it into the registry as-is, and asserts the next run is CLEAN. That is the round-trip the
message promises, and it is the only assertion that catches this class whatever the truncation width.

### M5 — the unresolved-waiver report sits after `exit 1`, and the comment above it says the opposite

**`tools/check-dead-paths.sh:226` and `:238`.**

The unwaived loop ends with `[ "$bad" = 0 ] || exit 1` at `:226`; the `unresolved` report sits at
`:238`. Whenever an unresolvable row's carrier still hits the needle set, the row is never mentioned.
Staged on the live tree: rewording the text field of one row prints only the generic unwaived message
and exits, with no mention of the row that stopped covering the carrier.

The comment at `:186-188` promises the opposite in as many words — that such a row is "reported by its
own reason and never by omission", and names the actual outcome ("the carrier it excused would come
back as an ordinary unwaived hit with no trace of the waiver") as the thing the design avoids. The
suite records the true behaviour at `check-dead-paths.test.sh:134-136`, "asserted as it behaves rather
than as it reads better". So the landing ships two answers to one question and the source comment is
the wrong copy.

Operationally the reader is told to ADD a row to a shrink-only registry that already carries one for
that carrier, converging only after a second red.

One clause from the finder does not survive and is dropped here: rewording is NOT "the drift this
re-key was built for". The re-key was built for an unrelated line inserted above the carrier, and the
suite declares reword-non-survival deliberate.

**Fix.** Hoist the unresolved report above the unwaived loop, or fold it into that loop's header, so
the red names the row and its reason. Then correct the comment. Fixing only the comment is legitimate
and cheaper; shipping both the comment and the behaviour is not.

**Left-shift gate.** Once hoisted, change the existing arm to assert the STALE reason text rather than
the generic message. The durable rule for the §10 checklist: a comment that describes ordering is a
claim about control flow, and the arm that contradicts it is evidence, not a style note.

---

## LOW

### L1 — a three-field waiver row parses as valid with a silently empty reason

**`tools/check-dead-paths.sh:161`.**

`_wtext=${_rest%"$TABC"*}` strips from the LAST tab, so `path\tordinal\ttext` with no reason finds no
tab to strip, the whole remainder becomes the text, and the row resolves and waives its hit with
nothing recording why the name must stay. Reproduced by running the expansions directly.

The registry's entire justification is a written reason per row — the header declares three legal
waiver classes and a reason each. The malformed branch at `:162-166` validates the ordinal and file
existence, and nothing validates field count. All eight current rows carry four fields, so the
population is empty today; that is why this is low, not why it is right.

**Fix.** Count tabs before splitting: reject a row whose tab count is below three into `malformed`
with `<row has fewer than four fields; the reason is absent>`.

**Left-shift gate.** A malformed-row arm per missing field, beside the existing ordinal arms. The
registry grammar has four fields and the gate validates two of them.

### L2 — the S5 fixture shells out to a bare, unchecked `python3`

**`tools/unattended/unattended.test.sh:1660`.**

`python3 - "$PWD/..." <<'PY'` with no launcher resolution and no status check — the only such
invocation in the file. `tools/lib/resolve-python.sh` exists in this repo because the MS-Store
`python3` stub answers `command -v` and exits 9009. The same suite states the convention at `:344`
("pure shell: a python launcher here is unresolved") and asserts it against the DRIVER at
`:1918-1922`. The harness now does what it forbids its subject to do.

Because the status is unchecked, an unresolved launcher leaves the README unmodified and the two
following assertions red with "missing: the build README carries no units marker at all" — accusing
the driver of a defect the fixture never staged. It resolves on node d today, so this is a latent
portability regression rather than an observed failure.

The edit is also gratuitous: the fixture only deletes two marker lines, which `sed` or `grep -v` does.

**Fix.** Write it in shell, matching the sibling `roster()` and `units()` helpers:
`grep -v -e '<!-- gen:build-units -->' -e '<!-- /gen:build-units -->' "$f" > "$f.t" && mv "$f.t" "$f"`.

**Left-shift gate.** Extend the existing source-level arm so it scans the SUITE as well as the driver
for a python launcher not routed through `tools/lib/resolve-python.sh`. The arm already exists and
points at only half the file set, which is §7's green-by-absence in one line.

---

## Cross-cutting notes

**One class produced the blocker and two of the highs.** A helper is taught to refuse, its refusal is
propagated with care through one frame, and every consumer captures it in a command substitution that
tests only the string. `set -e` is off, so nothing announces the loss. B1, H1 and the `for miss` loop
are three instances; the source-level arm proposed under B1 is the only thing that gates the class
rather than the instances. This is worth a `memory/gotchas/` entry as well as a gate — the shell
idiom `x=$(f)` followed by `[ -n "$x" ]` is invisible in review precisely because it looks complete.

**A second reader is not a second opinion.** H4 is a validator and its consumer answering one question
two ways, in a block whose comment says it set out to avoid exactly that. The general rule to carry
into §10: when two tools read one marker, the second one written must reuse the first one's predicate
or be differentially tested against it. Re-implementing "the same rule" from the prose describing it
is how the two drift.

**The diff wrote three claims it does not honour.** `UNATTENDED-PROTOCOL.md:424` ("the same unit by
construction"), `SKILL.md:465` ("a named refusal rather than a complete-looking list"), and the
comment at `unattended.sh:1520` ("THE STATUS IS TESTED"). Each was written in the same pass as the code
it describes, which is the condition under which prose is least likely to be checked and most likely
to be believed. Every fix above should be paired with a re-read of the sentence that promised it.

**Verification note.** All thirteen defects were reproduced by execution — fixtures, extracted
harnesses, or both revisions run over one tree. Nothing here rests on reading alone. Four raw findings
were refuted by the skeptic pass and are not carried; precision 0.83 is above the ~0.5 floor §8 sets
for tightening scope, so the lens set and priming stand for round 2.

*Note added when this record landed: the reproduction above originally spelled two fixture unit
ids. `rosters()` reads an id mentioned anywhere under `memory/` as a CLAIM on it, so writing them
here attached them to a build and red hygiene check 14. They are described instead. Same trap the
spec-audit round-1 record hit, one record later.*
