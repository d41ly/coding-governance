**Serves:** diff-review TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4

*Range `c80d9233356193d8053de00a0976455eac30ead9...HEAD`, the cumulative diff landing on main, reviewed
once at the integration boundary per §8 rather than per increment. **ROUND 2.** Node d, 2026-08-25.*

# Closing diff review, round 2 — the round that graded itself, and found the fold

This is the run item 5 of the aborted round-2 record left open: re-run the closing review from round
1's recorded tip and grade what the session limit left ungraded. It completed.

**Review shape.** Raw 15, confirmed 12, refuted 3, unverified 0, precision 0.80. The 12 confirmed
reports collapse to **8 distinct defects** — two pairs of lenses found the same `--plan` vacuity from
opposite directions, and two more found the same marker-message defect from the count side and the
whitespace side.

## Verdict: CLEAN WITH FIXES

Zero blockers, two high, four medium, two low. Round 1 confirmed one blocker; this round confirms
none, so the loop's convergence predicate is satisfied strictly rather than by oscillation, and no
finding is promoted to a unit.

That token is not a licence to skip the two highs. Both are live behavioural regressions against
BASE on the agent-facing diagnostic path, one of them reproducible on 7 of the 63 tracked builds
today. They are each a guard-placement change of a few lines, which is why they fold rather than
promote.

**Every one of the eight is a defect the round-1 fold introduced.** Not one is older code the fold
merely exposed. The build's own gotcha catalogue has the entry for this — fold text is unreviewed
surface — and this round is its cleanest instance yet: five separate fixes for round-1 findings
(H1, H2, H3's scoping, H4, and the arm added beside them) each shipped a new defect of the same
class they closed. Round 1 collapsed 20 reports into 13 defects; round 2 collapses 12 into 8, all of
them written between the two.

| Severity | Count | Distinct sites |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 2 | `tools/unattended/unattended.sh` |
| MEDIUM | 4 | `unattended.sh`, `gen_build_index.py`, `unattended.test.sh`, the acceptance record |
| LOW | 2 | `gen_build_index.py` |

---

## HIGH

### R2-H1 — the slug-scoped id extraction reopens the false-terminal vacuity one layer up

**`tools/unattended/unattended.sh:1646`** (the guard that should have caught it is at `:1606`).

Round 1's H3 fix scoped the row-to-id extraction to the build folder's own slug:

```sh
printf '%s\n' "$_row" | grep -oE "[A-Z]+-$slug-[0-9]+" | head -1
```

A rendered row whose id carries a **different** slug yields no word, the loop body never runs for it,
and the row vanishes before the S7 `NO TRACKED SPEC (rendered row without one)` branch — which exists
precisely so that no region row falls through unnamed — can ever see it. The sibling H2 emptiness
guard at `:1606` tests the **unscoped** `unit_rows`, so a README whose rows all carry a foreign slug
sails past it. The tail then prints `next: none - every tracked spec is terminal` at exit 0.

Reproduced both ways in a scratch tree. Folder `tHost`, one rendered unit row whose link text is
`ARCH-tGuest-1` and whose target is a spec under that folder, status SPECCED, plus one tracked spec
headed `# ARCH-tGuest-1`.
At base `c80d9233`, `--plan tHost` prints `ARCH-tGuest-1 SPECCED THIN` and `next: ARCH-tGuest-1 (THIN)`.
At HEAD it prints no unit row at all and `next: none - every tracked spec is terminal`, exit 0. That is
an affirmatively false statement over a live SPECCED unit, emitted by the verb an agent reads to pick
its next unit, and it is a regression against BASE.

The shape is engine-supported, not hypothetical. `gen_build_index.py`'s `rosters()` falls back to
front matter when a folder's slug owns no ids, the generator's own comment says a folder HOUSES specs
whose ids may belong elsewhere, and this same diff files that tolerance as a backlog row under the id
`TOOL-dHonouredPark-6`. This finding is not that row: the row describes `roster_ids` returning empty
and `build-complete` REFUSING at term 2, a safe failure. This is a silent false pass.

I swept the corpus at HEAD: **0 of 280 tracked unit rows** fail the scoped match, so today's blast
radius is nil. `build-complete` term 4 still reads `nonterminal_units` unscoped, so authorization is
not bypassed. What is wrong is §7's rule in its own words — the fold gated the digit-slug INSTANCE of
this vacuity (`tRun2`) and left the foreign-slug instance of the same CLASS.

**Fix.** Collect the loop's ids into a variable before iterating, and refuse when the region carried
rows but the id set is empty:

```sh
_ids=$(unit_rows "$_rmp" | while IFS= read -r _row; do
    printf '%s\n' "$_row" | grep -oE "[A-Z]+-$slug-[0-9]+" | head -1
  done)
[ -n "$_ids" ] || { fail 42 "the generated units region carries rows but none names an id of this build, so this verb has no unit set to grade: $_rmp"; return 1; }
```

The alternative is to keep the unscoped reading and route a foreign-slug row through the existing S7
arm. Either way the verb must never print `next: none` over a region it could not parse.

**Left-shift.** Two legs, because the fixture alone repeats the mistake. A `--plan` arm whose fixture
row id carries a slug different from the folder's, asserting the row is NAMED and `next:` is not
`none`; and a corpus leg over `memory/builds/*/README.md` asserting every rendered unit row yields at
least one id under the driver's own extraction, so the class reds on the tree and not only on a
fixture.

### R2-H2 — the empty-region guard is ordered above two diagnostics and names a repair that is a no-op

**`tools/unattended/unattended.sh:1606`** (the checks it short-circuits are at `:1610` and `:1619`).

The H2 guard sits above both the `git ls-files` tracked-spec check (fail 19) and the S6
`NOT A UNIT (no status header)` pass, so it swallows both. Measured base-vs-HEAD over every tracked
build, with the base script extracted from `c80d9233` and run beside the current one:

- aDeployScout, aKitHardener, aLeanRework, aPortableWarden and aRatchetForge each printed
  `<file> - NOT A UNIT (no status header)` plus the roster and next lines at base. At HEAD each
  prints only the check-42 refusal.
- aFerriedDossier and bThriftyBellows carry zero tracked specs. They lose check 19's accurate
  sentence — no tracked spec under this build, so every planned unit is MISSING — and get the same
  check-42 text.

I re-ran all seven at HEAD in this session and reproduced the refusal on every one.

The named repair is wrong in all seven cases. `python tools/memory-tree/gen_build_index.py --check`
reports `clean (338 artifact(s))` right now, so `--write` renders nothing new. These regions are empty
because no tracked spec carries a parseable `**Status:**` header — a state `--write` can never change
— so the refusal is a permanent dead end pointing at a command that cannot clear it, on the verb the
kit's own skill doc tells a resuming run to call.

The five spec-carrying builds are exactly the population unit 4's acceptance record claims survived
the move. See R2-M1.

**Fix.** Move the `[ -z "$(unit_rows "$_rmp")" ]` block below the `specs=$(git ls-files …)` check and
below the S6 loop, and gate it on at least one spec having produced a parseable status header — i.e.
refuse only when specs that WOULD render rows exist and the region has none. Where no spec parses,
keep printing the `NOT A UNIT` rows; where no spec exists, let check 19 own the message.

**Left-shift.** A corpus leg that runs `--plan` over every tracked build and reds on any refusal whose
named repair is provably inert — concretely, a check-42 exit while `gen_build_index.py --check` is
clean. That gates the CLASS (a refusal whose remedy cannot change the tree) rather than these seven
builds, and it would have redded the day this guard landed.

---

## MEDIUM

### R2-M1 — an acceptance criterion is recorded OBSERVED for behaviour the same fold removed

**`memory/builds/dHonouredPark/build/2026-08-25-build-TOOL-dHonouredPark-4-acceptance.md:66`.**

AC7 reads, verbatim, that `--plan` over the five builds carrying such a file still prints
`NOT A UNIT (no status header)` for each, and that the corpus diff confirms all five survived the
move. At HEAD none of the five prints that row at all; each prints the check-42 refusal from R2-H2.

The history explains it without excusing it. The acceptance record was written at `c80d9233`; the H2
guard landed afterwards at `5d21390e` and AC7 was never amended. This is the record-does-not-describe-
reality class the drift audit exists to catch, and the same record's AC6 and AC10 show the amend
mechanism was available and used.

**Fix.** Fixing R2-H2 restores AC7's observation, which is the preferred route. If the refusal is kept
deliberately, amend AC7 to state that the five builds now refuse and record why that is better than
the diagnostic they lost.

**Left-shift.** The acceptance ledger already gates that every AC of a CLOSED Tier-2 unit is EVIDENCED
or AMENDED; it grades presence, not truth. Add the §10 checklist entry the gate cannot express: an
acceptance record written before the build's last fold is stale by default, and every AC marked
OBSERVED whose evidence is a runnable command is re-run at the DoD, after the final fold. Where the AC
quotes its witness in backticks — which the spec-format ratchet already requires — that re-run is
mechanical.

### R2-M2 — a whitespace-perturbed marker is reported as DUPLICATED when nothing is duplicated

**`tools/memory-tree/gen_build_index.py:1305`** (the near-miss loop that should have caught it is at
`:1296`).

Round 1's H4 made `check_marker` byte-exact, which is right. What was not adjusted is the `elif`'s
wording: a marker perturbed by whitespace now drops out of `n_open`/`n_close`, so a README with
exactly one open and one close reports that the authored roster pair is DUPLICATED with 0 open and 1
close marker. Under the previous `l.strip()` comparison that branch was reachable only by a genuinely
absent marker, so the fold newly enables an affirmatively false sentence.

The near-miss loop cannot cover the indented case, because it is prefix-anchored at column 0
(`s.startswith(m) and s != m`), and an indented line does not start with the marker.

Reproduced in this session against `memory/builds/dHonouredPark/README.md`, whose marker sits at
line 50:

```
baseline  []
indented  [(1, 'the authored roster pair is DUPLICATED — 0 open and 1 close marker(s), …')]
trailing  [(1, '…DUPLICATED — 0 open and 1 close marker(s), …'), (50, "a roster marker line carries more than the marker itself…")]
```

For the indented case the false sentence is the ONLY message emitted, it reports line 1 rather than
line 50, and it sends the author hunting for a second marker that does not exist. The two halves of
one class diverge: trailing space gets an accurate second message, indentation gets nothing. Not a
false green — the gate still reds, matching the driver's column-0 refusal — but the H4 comment's
stated goal is that this gate speak the driver's vocabulary of absent, duplicated and transposed, and
this state is reported as none of the three.

**Fix.** Compute the near-miss set first and branch on it. Widen the loop's predicate to catch a line
that is a marker modulo leading or trailing whitespace (`s.strip() == m and s != m`, in addition to
the prefix test), emit only the malformed-marker message for such a file, and reword the count branch
to *not exactly one open and one close* so it never asserts duplication it did not observe.

**Left-shift.** Two arms beside the existing trigger-4 table, both asserting the message is NOT
DUPLICATED: one over the canon fixture with the open marker indented two spaces, one with a trailing
space. Both must be seen RED before the fix lands.

### R2-M3 — the roster guard sits after the listing, and the exit status it was written to read is still discarded

**`tools/unattended/unattended.sh:1674`** (the guard is at `:1684`).

`missing_units` correctly propagates `roster_ids`' exit 3, and round 1's H1 fix reads that status —
but 11 lines after the listing has already been printed, and the MISSING loop one line above still
throws it away:

```sh
for miss in $(missing_units "$slug" "$dir"); do
```

A command substitution whose status nothing consults, with `set -e` off. A malformed roster pair
therefore yields empty output, zero iterations, and every MISSING row vanishes with no marker.

Reproduced: a build whose roster region has two open markers and one close, one specced unit and one
roster-only unit, prints `ARCH-tX-1 SPECCED THIN`, omits the second unit's MISSING row entirely, and
only then prints the check-42 refusal at rc 1. `fail()` is a bare `echo`, so the partial table and
the refusal land on the same stream, one above the other.

The three sibling region guards all return before printing anything, precisely so that the
complete-looking list this unit exists to stop printing is never emitted. H1 reintroduced it one
region over. The exit code and the message are right, which is why this is a partial answer under a
loud refusal rather than a silent wrong one — and why it is medium.

**Fix.** Hoist the roster resolution beside the other region guards, before the S6 pass and the unit
loop: `local _rids; if ! _rids=$(roster_ids "$slug"); then fail 42 …; return 1; fi`, then feed
`$_rids` into the MISSING loop and the summary line instead of re-invoking `missing_units` unchecked.
One resolution, status read once, refusal before any row is printed.

**Left-shift.** An arm over the malformed-pair fixture asserting stdout carries **exactly one line** —
the refusal. Asserting the refusal text alone is what let this ship: the existing arm does exactly
that and passes over a table it never looks at.

### R2-M4 — the arm that certifies the row dedup passes with the dedup deleted

**`tools/unattended/unattended.test.sh:1699`.**

The arm titled *each unit appears ONCE — a row spells its id twice, in the link text and the target*
uses fixture rows whose targets are `spec/two.md` and `spec/one.md`. Those spell the id **zero**
times. I reproduced the driver's per-row pipeline over the exact fixture rows: the output is
identical with and without `head -1`, so the arm's count assertion holds either way and it passes
with the thing it protects removed.

The doubling it claims to cover is real and common. Measured at HEAD over `memory/builds/*/README.md`:
280 tracked unit rows, of which **143 match the scoped id twice**, because their targets are the dated
spec filenames and carry the uppercase family. The driver's own comment says the doubling was measured
on the real corpus. Every `units`/`setunits` fixture in the suite uses a bare `one.md`-shaped target,
and `mkspec` writes the dated filename only to disk and never into a region row, so no arm in the file
exercises the doubling at all.

This is §7's could-not-fail shape: a new gate is not landed until its failing case has been observed.

**Fix.** Give the fixture rows targets that carry the family-qualified id, matching what
`render_region` actually emits — a dated `spec/2026-08-01-spec-ARCH-tPlan-2.md` target rather than
`spec/two.md`, and likewise for the other row. Confirm the arm goes RED with `head -1` deleted before
keeping it.

**Left-shift.** Build the fixture rows from `render_region`'s own output rather than by hand, so a
fixture cannot be shaped unlike the thing it stands for. That is the general repair for both of this
build's fixture defects, and it is cheaper than a lint that tries to spot a hand-written row.

---

## LOW

### R2-L1 — the near-miss marker branch has no arm, so its failing case has never been observed

**`tools/memory-tree/gen_build_index.py:1296`.**

Verified by instrumentation, not by reading: a copy of the module with a stderr probe inside the
near-miss branch runs the full `--selftest` to a clean all-arms-held PASS with **zero probe hits**,
while driving `slot_violations` directly with a trailing-space marker fires it. The trigger-4 arm
table covers ABSENT, DUPLICATED, TRANSPOSED, canon-off and empty-legal only, and the message string
appears exactly once in the whole file — at the emission site.

That is what let R2-M2's false sentence ship green, and a later refactor restoring `l.strip()` would
remove the entire H4 fix without reddening anything.

**Fix.** The two arms named under R2-M2 close this as a side effect; add them.

**Left-shift.** Raise the arms floor for this module the way `check-arms.py` does for tracked shell:
every distinct violation message `slot_violations` can emit must be asserted by at least one arm, so
a new branch without an arm reds by that fact rather than passing silently.

### R2-L2 — a fourth spelling of the marker-line predicate, inside the function whose comment forbids two answers to one question

**`tools/memory-tree/gen_build_index.py:1287`.**

Four live spellings of one predicate in this file: `_is` at `:897`, `_marker_index` at `:968`, the new
`check_marker` at `:1288`, and a fourth inline strip at `:1297`. The last two hardcode a literal
carriage return where the module declares `CR`. None is dead — `_marker_index` has ten call sites and
`apply_region` three.

No divergence today, so nothing is wrong on this commit. The cost is that the next correction to this
contract has to find four sites, and the copy that misses it is the gate rather than the writer. The
file has already paid for that twice: `_is`'s docstring records one correction (one trailing CR, not
`rstrip`), and the comment above `check_marker` records a second — a `l.strip()` that certified a pair
the driver refuses, called out in its own words as the two-answers-to-one-question defect
reintroduced by the fix for it. A third and fourth copy re-arm it.

The by-design refutation does not reach. That comment defends not binding the DUPLICATE and ORDER
logic to `_marker_index`, which returns a first index and has no notion of duplicates. It says
nothing about the line-equality predicate, which is separable and shareable.

**Fix.** One module-level helper taking the line and the marker, returning the CR-stripped equality,
called from `apply_region`'s `_is`, from `_marker_index`, and from `slot_violations` in place of
`check_marker` and the inline strip.

**Left-shift.** A grep leg banning a second spelling of the CR-strip comparison outside that one
helper. The predicate is a fixed byte sequence, so the check is exact and has no near-miss population.

---

## The three refuted findings

Three reports did not survive the skeptic and are not carried here. None of them touched the two
regressions above; the surviving set is what the section headings say it is.

## Left-shift summary

| Finding | Gate proposed | Kind |
|---|---|---|
| R2-H1 | foreign-slug `--plan` arm, plus a corpus leg asserting every rendered row yields an id | new leg |
| R2-H2 | corpus leg reding on a refusal whose repair is inert against a clean `--check` | new leg |
| R2-M1 | §10 entry: re-run every OBSERVED AC's witness after the build's final fold | checklist |
| R2-M2 | two arms over whitespace-perturbed markers, asserting NOT DUPLICATED | new arms |
| R2-M3 | arm asserting stdout is exactly the refusal line over a malformed pair | new arm |
| R2-M4 | fixtures built from `render_region` output, not hand-written rows | fixture rule |
| R2-L1 | arms floor: every `slot_violations` message asserted by at least one arm | arms floor |
| R2-L2 | grep leg banning a second spelling of the CR-strip comparison | new leg |

Six of the eight are gateable. R2-M1 is the one that is not, and it takes the checklist entry §7
prescribes when no gate fits. R2-M4 is a rule about fixtures rather than a leg, because the defect is
that the fixture did not resemble its subject, and no predicate over a hand-written row can decide
that.

## The one thing this round says that round 1 could not

Round 1 found 13 defects in code written over four units. Round 2 found 8, every one of them written
in the fold that fixed round 1 — and five of them are the same class as the finding they were fixing,
re-entered one layer up or one region over. The build's own catalogue already carries the class. What
this round adds is the measurement: the fold's defect density was not lower than the original code's,
and the fold was the part nobody reviewed until now.
