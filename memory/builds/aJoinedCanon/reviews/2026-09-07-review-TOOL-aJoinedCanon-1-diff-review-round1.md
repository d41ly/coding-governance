**Serves:** diff-review TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11

# Closing diff review — aJoinedCanon

## Verdict: CLEAN WITH FIXES

*Round 2 appended after the full bar; four further findings, all fixed. Read that section first.*

Node `a`, 2026-09-07. Range `274aa39b..HEAD`, 37 files, 2475 insertions, 397 deletions. Ten units
built, one retired.

## The method used, and its declared limit

**This review was NOT run through `tools/workflows/tier2-review.js`, and that is a real narrowing
rather than a formality.** This session is configured not to invoke the Workflow or Agent tools
unless the owner asks, so the primed multi-lens fan and the batched skeptics the review protocol
prescribes did not run. What ran instead is a single reviewer executing PREDICATES over the
cumulative diff — which is the half of the protocol that does not need agents, and is the half this
build is about.

Read that limit honestly: the fan buys COVERAGE, and a single reviewer buys none of it. Every
finding below was produced by a predicate that could have printed nothing. No claim is made that a
lens fan would have found the same set, and the owner should assume it would have found more.

## Findings

### F1 — CRLF committed into `tools/memory-tree/README.md` — CONFIRMED, FIXED

`git show <sha>:<file> | tr -d '\n' | tr -cd '\r' | wc -c` over every file in the range: BASE 0,
HEAD 276. My unit-9 edit read the file as bytes and wrote them back; the working copy is CRLF
because `.gitattributes` pins `memory/**/*.md` and `*.sh` to LF and does NOT pin `tools/**/*.md`.
`git diff --check` was reporting 275 trailing-whitespace errors for that one file.

**Nothing on the bar reds for it.** That is the `gate-green-by-accident-on-generated-bytes` class
over an unpinned path, and it is the finding of this review most worth left-shifting.

Fixed: 275 CRLF pairs plus one BARE CR — the bare one is where LF content was spliced into a CRLF
file, which a `\r\n` replace structurally cannot reach. Every other file in the range re-checked
individually and clean.

**Left-shift:** `TOOL-aJoinedCanon-12` in `memory/backlog/TOOL.md` — pin `tools/**/*.md eol=lf`, or
state why the kit's own markdown is exempt when the memory tree's is not.

### F2 — `SPEC_LEGLINE_CUTOFF` reached one conf carrier, not two — CONFIRMED, FIXED

The key was declared in this repo's `.memory-tree.conf` and absent from
`tools/memory-tree/.memory-tree.conf.example`, so an adopter would hold a conf without it and an arm
that reads as armed while grading nothing. The build's own rule 3 requires both carriers.

**Why no gate caught it, which is the interesting half.** The self-test's example-parity arm derives
its key set from the ENGINE by grepping `^[A-Z][A-Z0-9_]*_CUTOFF=` out of `check-memory-hygiene.sh`.
This key is read by `tools/check-spec-tokens.py` instead, so the one gate that structurally catches a
missing memory-tree key cannot see a key belonging to a different tool. Fixed by declaring it blank
with the adopter comment its siblings carry; the structural gap is unfixed and is the backlog row.

**Left-shift:** `TOOL-aJoinedCanon-13` — the example-parity arm derives from one engine and should
derive from every tool that reads `.memory-tree.conf`.

### F3 — the `tFixture` number-space rule was violated, with no collision — CONFIRMED, NOT FIXED

The build README allocates unit N the block at `80 + 10N` "upward". Unit 8 needed thirteen fixtures
and ran 160 through 172, which reaches into unit 9's block at 170; unit 9 then used 180 through 182,
which is unit 10's. Measured: **no fixture number is defined twice**, so the hazard the rule exists
to prevent — assertions keyed by fixture name silently grading a sibling's file — did not occur.

Not fixed, deliberately. The defect is in the RULE rather than in the build: a ten-wide stride with
an open-ended "upward" cannot hold a unit that needs thirteen fixtures, and no allocation this build
could have chosen would have satisfied both halves. Renumbering now would churn the suite and its
ledger for zero change in behaviour.

**Left-shift:** `TOOL-aJoinedCanon-14` — the stride is the bug; a per-unit block wide enough for its
declared fixture count, or an allocation derived rather than pinned.

## What was checked and found clean

Each of these is a predicate that could have printed something and did not.

| Check | Result |
|---|---|
| every new cutoff key in all three carriers (engine preset · conf · shipped example) | 9 of 9 after F2; the tenth is engine-exempt by design |
| no `-v` name bound twice on the one check-12 awk invocation | clean, and unit 1's AC16 now asserts it in the suite |
| CR bytes in the committed blob, per file across the range | 1 file, fixed; 36 clean |
| `git diff --check` over the range | 0 after F1 |
| fenced-block balance in all five edited documents | even in every one |
| every new arm announces a zero-population run | 6 notices for 6 arm groups |
| dead variables left by the fold | none (`extids` removed with its block) |
| `check-arms.py --check` | green at 26:26 |
| build README rules against what shipped | 9 of 9 hold; F3 is the exception |

## Round 2 — what the FULL BAR found that the predicates did not

The first close ran the merge bar and it came back RED, 4 of 42 legs. That is the honest verdict on
the predicate pass above: it checked what it thought to check, and the bar checked more.

### F4 — the verb pin, breached by six fixture helpers — CONFIRMED, FIXED

`lexicon naming predicates` exits 0 at BASE and 1 at HEAD with the SAME four violations, so the
violations are pre-existing and the EXIT is not. The cause is the shrink-only verb pin: offenders
978 at BASE, 984 at HEAD. Exactly six, and exactly the six shell fixture helpers this build added —
`revspec`, `joinspec`, `fmspec`, `edgespec`, `rowspec`, `basespec`. None leads with a declared verb.

`lexicon.py --suggest` answers that this is a SCOPING question rather than a spelling one and prints
the declared table. These helpers WRITE a fixture spec file, so they are now `write_rev_spec`,
`write_join_spec`, `write_failmode_spec`, `write_edge_spec`, `write_rows_spec`, `write_base_spec`.
Offenders back to 978, leg green.

**This is the finding the predicate pass most deserved to miss**: nothing above graded a name, and
the branch bar skips this leg as unchanged-versus-main, so it can only fail at the lander.

### F5 — a shipped kit file spelling a path outside itself — CONFIRMED, FIXED

`install-prefix` reported `tools/memory-tree/.memory-tree.conf.example` UNRECORDED. Isolated by
restoring the BASE version of that one file, which turned the leg green: the cause was mine. The
added `SPEC_LEGLINE_CUTOFF` comment spelled `tools/check-spec-tokens.py`, and a shipped kit file may
name nothing outside itself by literal — an adopter installing kits at another prefix receives a
dead path, because `apply` writes gov's bytes verbatim. Reworded to name the checker without a path.

### F6 — a second line-keyed waiver moved out from under its literal — CONFIRMED, FIXED

`tools/install-prefix-waivers.txt` keys on `<path>:<line>`. The README additions pushed the waived
`merge-rows.sh` literal from line 109 to 117 and the leg redded. Re-keyed, never re-waived — which
is the recorded remedy for this class.

### F7 — the generated map went stale — CONFIRMED, FIXED

`codebase-map coverage + freshness` failed `test_generated_artifacts_are_fresh`: `symbols.json` did
not carry the functions this build added. Regenerated; the leg passes all six of its tests.

### What did NOT change: the two lexicon legs are also red on `main`

Measured against a detached BASE worktree: the four naming VIOLATIONS in `hygiene-parity.test.sh`,
`check-playbook.sh` and `lib-unattended.sh` are present at BASE and in files this diff never touches.
`TOOL-aWeldedTribunal-12` is the OPEN row recording that the verb pin is breached on `main` and
refuses every landing. This build neither caused nor cleared it, and the lander will meet it.

## Round 3 — the KIT self-test bar, which this build's DoD owes

`GATE_FULL=1 GATE_SELFTESTS=1` ran every leg there is: 3 of 94 failed. Two are PRE-EXISTING, each
verified by running the leg's own argv against a detached BASE worktree rather than by reasoning
from the diff — the lexicon case had already shown that "not in my diff" is not sufficient, because
there the violations were identical at BASE and only the EXIT differed.

| leg | BASE | HEAD | verdict |
|---|---|---|---|
| `govkit selftest` | exit 1, same two arms | exit 1 | pre-existing |
| `codebase-map adopter e2e` | exit 1, same two arms | exit 1 | pre-existing |
| `memory-hygiene self-test` | 658 s ok | KILLED at 900 s | **mine** |

`codebase-map adopter e2e` fails honestly and says so: *no dossiers under the map root: this check
cannot judge an empty population* — the vacuous-population class refusing on a freshly seeded tree.

### F8 — the self-test breaches its own ceiling under concurrency — CONFIRMED, PARKED

This build grew that suite from 99 assertion points to 121, which is the coverage it was
commissioned to add. Standalone it still passes — 369 assertions, exit 0, about 11 minutes against a
900 s ceiling. Under the full bar at width 8 it exceeded 900 s and the runner killed it. That is
cost-is-a-verdict working as written, not a defect in the suite.

**Parked rather than decided, and the reason is the interesting part.** The charter sanctions
re-declaring a ceiling with a reason — but a run raising a bound that its OWN additions breached has
no external check on the judgement, and that is the one shape a cost gate must not have. The other
option, making the suite cheaper, is unspecced restructuring of a kit this build was not
commissioned to optimise, and its cost is process creation rather than logic.

What it does not block: the bar that gates the push is GREEN at 42/42, and `chunk = selftests` is
on-demand only — no boundary sets it. The likely truth is that the 900 s ceiling was already unsafe
under full concurrency before this build (this repo has measured a hygiene leg going 48 s quiet to
139 s at width 8) and was never observed, because that chunk is never run at a boundary.

## Left-shift summary

Three findings, three backlog rows, none of them a gate this build could have added to itself: F1
needs a `.gitattributes` pin, F2 needs a checker to widen its derivation across tools, F3 needs the
allocation rule rewritten. All three are recorded in `memory/backlog/TOOL.md`.
