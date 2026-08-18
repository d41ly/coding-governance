# TOOL-aFusedCharter-3 — an instruction file's lines get a declared maximum, defaulting to 450 characters

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

Gate the line length of the agent-instruction files this repo ships and reads, at a per-subject
DECLARED maximum defaulting to 450 characters, so a rule stays readable in a diff and an adopter can
move the number without editing a gate.

## 2. Scope (IN)

**S0 — Re-record the ruleset's size high-water, because this unit is the last to touch the file.**
`tools/template-size-highwater.txt` records 37 381 bytes for the template. The converged file lands
roughly 7 KB above that, so `check-template-size.sh` prints its advisory growth warning on every run
from the fold onward until somebody re-records it. `--bump` is deliberately a separate act that a
person performs, and no unit in this build performed it. This one does, with the growth argued in the
commit message — the file absorbed a whole companion and lost three sections — and an acceptance
criterion that the leg prints no warning afterwards. It lands here because a bump recorded before the
last edit records the wrong number.

**S1 — A gate keyed by subject, in the shape this repo already uses for a declared limit.**
`tools/check-line-length.sh` reads `tools/line-length-limits.txt`, whose grammar is a repo-relative
path, a tab, and a character count — deliberately the same grammar as
`tools/template-size-limits.txt`, which this repo already maintains for the same reason and with the
same comment discipline: every value carries its justification beside it, because a number with no
history is a number nobody can question.

**S2 — Resolution order, and why it is that order.** A positional argument, then THIS declaration,
then the environment, then the gate's hard default of 450. The declaration outranks the environment
for the reason `tools/template-size-limits.txt` records at length: a declared per-subject pin is
policy, and an environment variable is a local override for a subject nobody declared. Without that
ordering, one exported variable silently lifts every declared subject at once.

**S3 — The population is DECLARED, not globbed.** A glob over `*.md` would grade every record in
`memory/` and every archived snapshot, which are records of what was written and not instances of a
current rule. The declaration seeds with the two subjects this build creates: this repo's charter,
and the converged ruleset it renders from. The ruleset is in the population because gov must not
ship a template whose lines red the gate gov ships — an adopter would receive a file that fails its
own bar on the day they install it.

**S4 — Measure characters, not bytes, and normalise line endings first.** The subject files carry
non-ASCII glyphs, so a byte count would grade a line with six em dashes as eighteen characters longer
than it reads. This is not a theoretical difference: over these three files it moves the offender
count by one line and every "longest line" figure by 1 to 4 per cent, and `awk` in the C locale
counts BYTES, so the measurement tool has to be chosen deliberately rather than assumed. Carriage returns are stripped before measuring, exactly as
`tools/check-template-size.sh` does, so the verdict is checkout-independent on a Windows tree.

**S5 — Fenced blocks are exempt, the exemption is stated, and the fence parser is honestly a new
copy.** A fenced code block holds a command whose length is not the author's to choose, and wrapping
one changes what it means. The gate's header states the exemption so a reader does not mistake a
green run for a claim about the whole file. Markdown tables are NOT exempt: a table row is prose in a
grid and can be split.

An earlier revision said the gate reuses the hygiene gate's fence machine "rather than rewritten,
since a second fence parser is a second thing to drift". Measured, that is not available and the
claim was already false in the other direction: the hygiene gate's fence scanner is a private shell
function nothing exports, that script ALREADY carries four more inline copies of the machine — the
last one labelled as the machine verbatim — and this gate sits outside the memory-tree kit, so
sourcing it would be the cross-kit edge this repo forbids. This gate therefore writes copy number
six, says so, and follows the precedent that keeps such copies honest: one shared case table with
agreement proven across implementations, the way the marker-region contract is graded.

The exemption's RATIONALE also loses half its subject. It cited "a command or a shape definition"
inside a fence; after `PLAY-aFusedCharter-2` R1 the shape definitions are bare column-zero list items
and no longer fenced at all. The rationale is rewritten to the surviving category, and the spec states
what protects a long shape definition if one ever appears: nothing does, and the longest today is
about 110 characters, so the exposure is named rather than covered.

**S6 — Wrap the offenders this build creates, against a CHARACTER measurement, and NEVER inside the
rendered region.** At BASE, measured in characters after stripping carriage returns: the charter has
8 lines over 450, worst 1 047; the ruleset has **4**, worst 1 474; the companion has 8, worst 897. An
earlier revision said five in the ruleset and cited 1 051 and 1 499 — those are byte figures, and one
ruleset line measures 462 bytes but 449 characters, so it is already compliant and wrapping it would
have been work against a number rather than against the rule. Those files are rewritten by
`PLAY-aFusedCharter-1`, `-2` and `-3`, and this unit lands last precisely so it grades their output.
Wrapping is not a content change: a wrapped line is still one rule, which the ruleset's own preamble
states.

**Every one of the charter's eight long lines is inside the section `PLAY-aFusedCharter-3` S3
deletes.** Measured: all eight sit in the gate-suite section. So by the time this unit runs, the
charter's long lines are whatever the RENDERED REGION brings, and a hand-wrap inside that region is
deleted by the next render and reds `bash tools/playbook/adopt-playbook.sh --check` in the meantime.
The act is: wrap in the ruleset, re-render the charter, re-measure. This unit never edits a byte
between the region markers.

**Two literals inside the ruleset's longest line must survive the wrap.** That line is the
concurrency bullet — 1 474 characters, this unit's primary target — and it is the single line both of
`check-playbook-parity.sh`'s value-parity extractions match. `PLAY-aFusedCharter-1` S7 keeps them
there deliberately; a wrap that splits either one across a newline makes its extraction match nothing
and the gate reds on its own anti-vacuity arm. Wrap around them, and prove it by running that gate
rather than by reading the line.

**S7 — A sibling self-test, and TWO manifest rows.** The gate row is UNGUARDED. A guard naming only
the gate and its test would skip the gate on exactly the diffs that rewrite a subject file, and
"guarded on its subject paths" — offered as an equal alternative by an earlier revision — reds
`govkit selfcheck`: its guard-class arm requires every pathspec to land in exactly one declared
class, and a repo-root product file lands in none. The self-test row is guarded on the gate plus its
test. The suite
satisfies all three parts of the assertion-count contract: an anchored pass line carrying the count, a
non-zero literal floor, and a reference proving the two meet. The gate, its test and the declaration
are depth-1 paths under `tools/`, so they need a registry route: a new flat entry with
`selectable = "conditional"`, holding both `[[gate_leg]]` rows, modelled on `check-placeholders`.
`TOOL-aFusedCharter-2` takes the same route for the same reason, and neither leg may be both claimed
and exempted. Arms for: an over-length line reds naming the file, the
line number and the measured length; an exactly-at-limit line passes; a long line inside a fence
passes; a long line inside a table reds; a non-ASCII line is measured in characters; a declared row
beats an environment variable; a subject with no row falls through to 450; a declaration row naming
an absent path reds as stale, because a stale row silently narrows the population it was written to
cover. The suite prints its executed assertion count in the shape `tools/check-testsuite-counts.sh`
accepts.

**S8 — Ship the gate, SEED the declaration from the adopter's own tree, and never ship gov's rows.**
An earlier revision shipped `tools/line-length-limits.txt` as a seed carrying gov's two subjects.
Neither path exists in an adopter's tree, and S7's stale-row rule makes a row naming an absent path a
red — so the adopter would red on install day, which is the exact failure this spec's own F1 calls
decisive. Both precedents in this tree cut the other way: `check-method-carriers` ships NO registry
and has the adopter's seeded from their own measured population, and `template-size-limits.txt` is a
deployer EXEMPTION rather than a shipped seed.

So the target AUTHORS its own declaration and gov seeds nothing — the `check-install-prefix`
precedent, whose descriptor ships its registry as `generated`, "seeded empty rather than copied", with
a reason recording that gov never seeds the target's registry. An earlier revision said "the adopter
writes the declaration from what it finds", which named an actor that does not exist: this kit has no
adopter script, Scope and Files touched create none, and the entry shape S7 copies declares
`argv = []`. Rather than add an adopter for one row, the row is the target's to write, and a target
with no row is graded at the default and says so — which S7 already arms.

`WIRE-INTO-PROJECT.md` states the three things an adopter needs: the default is 450, the declaration
is where you change it, and the row is keyed by YOUR charter's path, which may not be named
`AGENTS.md`. The sibling `check-testsuite-counts` entry words the same instruction as "seeded by
running the leg once and pasting what it names", and this one follows it.

## 3. Non-goals (OUT)

**No wrapping of records.** Nothing under `memory/builds/`, `memory/archive/` or the backlog shards
enters the population. Those are append-only or frozen.

**No line-length rule for code.** The subject is instruction prose. Shell and Python line length is
a different question with different tools and is not opened here.

**No automatic wrapping.** The gate reports; an author wraps. A formatter that rewraps prose would
fight every deliberate line break in a bulleted ruleset.

**No second declaration file for anything else.** The grammar is copied from the size-limits file
deliberately, but the two files stay separate: one declares bytes for a whole file, the other
characters for a line, and merging them would put two predicates behind one column.

## 4. Design

### Data model

A row is a repo-relative path, a tab, and a positive integer. Comments carry justification. A
non-numeric value is a NAMED failure with its own exit code, not a shell error at the comparison —
the same contract `tools/check-template-size.sh` enforces for its own declaration, learned there
after a corrupt record reached an arithmetic expansion and died with an unbound-variable error.

### Inventory

**The offender population is stated once, in S6, and deliberately not repeated here.** An earlier
revision carried a table whose caption claimed a character measurement while its rows held BYTE
figures — 8/1 051 for the charter and 5/1 499 for the ruleset — which are the very numbers S6 was
rewritten to correct, one screen apart in the same document. Two carriers for one measurement is the
defect this whole build exists to remove, committed inside it.

The one fact that is not in S6: the companion is not in the population because it ceases to exist,
and its eight offenders become the ruleset's when `PLAY-aFusedCharter-1` folds it in — which is why
S6 sizes its work against the converged file rather than against any BASE-time row.

### Rollout

The gate lands green because S6 wraps first, in this unit, before the leg is wired. A leg wired
ahead of the wrapping would red the bar for the duration of the wrapping pass, and a pass whose gate
is red is not followed by another.

### Alternatives rejected

**A single hardcoded 450 in the gate.** Rejected by the owner's framing: adopters must be able to
adjust it. A constant would make that a fork of the gate.

**A key in `.memory-tree.conf`.** Rejected: that conf belongs to the memory-tree kit, and an adopter
can install this gate without that kit. A kit's conf is not a general settings file.

**Grade every tracked markdown file.** Rejected in S3's terms.

**Reuse `tools/check-template-size.sh` with a mode flag.** Rejected: one script, two predicates,
two declaration files and two exit-code tables is a mode that shares a positional slot with a path,
which that script's own comments record as the way one silently becomes the other.

### Files touched (estimate)

New: `tools/check-line-length.sh`, `tools/check-line-length.test.sh`, `tools/line-length-limits.txt`
(gov's own, holding gov's rows and NOT shipped), and
`tools/govkit/entries/check-line-length.kit.toml`.
Edited: `tools/gate-legs.json` (two rows), `tools/govkit/registry.toml`,
`tools/template-size-highwater.txt` (S0), `WIRE-INTO-PROJECT.md`, a map dossier claim for the two new
gate-leg keys, plus the wrapping in the two subject files.

## 5. Production-readiness checklist

- security — N/A; a read-only measurement.
- perf / scale — two files today, linear in lines.
- a11y — long unwrapped lines are a readability problem, which is the gate's purpose.
- i18n — S4 is the concern: character counting over a non-ASCII corpus.
- error / empty / loading states — an absent declaration falls through to the default with an
  explicit line; a declaration row for an absent path reds as stale.
- observability — the gate prints, per subject, the limit it resolved and where it resolved it
  from, so an operator can see whether the declaration or the default answered.
- risks — the wrapping in S6 touches every long rule in two product files, and a wrap that lands
  mid-token changes meaning. The mitigation is that S6 runs before the leg is wired and its diff is
  reviewed as content, not as formatting.
- testing + left-shift gates — S7, eight arms.
- migration / rollback — a new leg; removing the row disables it.
- user docs — `WIRE-INTO-PROJECT.md` per S8.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-line-length.sh` runs after S6's wrapping, it exits 0 over both
  declared subjects and prints the resolved limit for each.
- **AC2** — When a 451-character line is introduced into a declared subject,
  `bash tools/check-line-length.sh` exits 1 naming the file, the line number and the measured
  length; at exactly 450 it exits 0.
- **AC3** — When a declared row sets a subject to 200, that subject is graded at 200 even with
  `LINE_MAX=9999` exported — proving the declaration outranks the environment.
- **AC4** — When a subject has no declared row, it is graded at `450`, and the printed line says the
  limit came from the default.
- **AC5** — When a 600-character line sits inside a fenced block `bash tools/check-line-length.sh`
  does not red; the same line inside a markdown table does.
- **AC6** — When a line of 400 non-ASCII characters is measured, the gate reports `400`, not its
  byte length.
- **AC7** — When `tools/line-length-limits.txt` names a path that does not exist, the gate reds as
  stale naming that row; when it holds a non-numeric value, it fails with its own named exit code
  rather than a shell error.
- **AC8** — When `bash tools/check-line-length.test.sh` runs it exits 0, prints its executed
  assertion count in the accepted shape, and carries one arm per AC2 through AC7 branch.
- **AC9** — When `GATE_FULL=1 bash tools/run-gates.sh` runs, both new rows are present and green and
  every other leg is unchanged.
- **AC10** — When `bash tools/check-template-size.sh` runs after S0's `--bump`, it prints no growth
  warning, and `tools/template-size-highwater.txt` holds the converged file's measured size under
  its new key.
- **AC11** — When the adopter runs against a fixture target, the target's own
  `tools/line-length-limits.txt` holds ONE row naming that target's canonical instruction file, and
  gov's two rows appear nowhere in it — checked by reading that file, never by exit code.
- **AC12** — When a diff touches only a declared subject, the gate leg RUNS, verified by driving
  `tools/run-gates.sh` over that path set rather than by reading the guard in
  `tools/gate-legs.json`.
- **AC13** — When `bash tools/check-testsuite-counts.sh` runs, the new suite is compliant on all
  three requirements with a non-zero floor equal to its measured arm count.
- **AC14** — When S6's wrapping is complete, `bash tools/check-template-size.sh AGENTS.md` exits 0
  against the ceiling `PLAY-aFusedCharter-3` S8 declared, and `bash tools/check-template-size.sh`
  with no argument exits 0 against the ruleset's. This unit is the last to touch either file, so it
  is the last chance to observe that S8's headroom actually absorbed the wrapping.
- **AC15** — When S6 has wrapped the ruleset's longest line,
  `bash tools/check-playbook-parity.sh` exits 0 — proving both value-parity extractions still match
  after the wrap, which is the failure a wrap through either literal would cause.

## 7. Gates

`run-gates canary` · `testsuite counts` and its self-test · `govkit selfcheck` and `govkit selftest` ·
`install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `harness arms` ·
`template size <=48KiB` (S0 moves its high-water record, and S6's wrapping is re-measured against
both declared subjects) · `playbook parity` (S6 wraps the line both its value-parity extractions
match) · `playbook render wiring` (S6 must not wrap inside the rendered region) · the two new rows ·
the full bar.

## 8. Open questions

none — the forks below are RESOLVED.

- **F1 — is the ruleset in the population, or only the charter?** RESOLVED (agent, 2026-08-18,
  delegated by the build's stated order): both, in GOV's declaration. Shipping a template whose lines
  red the gate shipped beside it hands an adopter a red bar on install day, which is the strongest
  possible argument and is not a preference. The spec audit then found the same argument pointing at
  this spec's own S8, which shipped gov's rows into adopter trees where neither path exists — S8 now
  seeds from the adopter's tree instead, and gov's declaration is gov's.
- **F2 — are fenced blocks exempt?** RESOLVED (agent, 2026-08-18, delegated): yes, and the header
  says so. A command or a shape definition has a length its author does not choose. Tables are not
  exempt, because a table row can be split and a long one is the readability defect the gate exists
  to catch.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. The offender counts are measured, and the companion's eight
  are noted as migrating into the ruleset rather than disappearing.
- rev-3 · 2026-08-18 · folded the round-2 spec audit. S6 gains its two hard constraints: every one
  of the charter's eight long lines sits inside the section `PLAY-aFusedCharter-3` deletes, so the
  act is wrap-in-the-ruleset-and-re-render rather than edit-in-place; and the ruleset's longest line
  is the one both parity extractions match, so a wrap through either literal reds that gate. S8 stops
  naming an adopter this kit does not have and makes the declaration target-authored on the
  `check-install-prefix` precedent. S7's guard alternative is deleted for redding `govkit selfcheck`.
  The Inventory table is removed for duplicating and contradicting S6, §10 stops asserting the reuse
  S5 refutes, and three ACs are added including the post-wrap ceiling re-measure.
- rev-2 · 2026-08-18 · folded the M4 spec audit. New S0 performs the size high-water `--bump` no unit
  owned; S8 stops shipping gov's declaration rows into adopter trees and seeds from the adopter's own
  tree instead; S6's offender figures are restated in CHARACTERS, which drops one ruleset line that
  was already compliant; S5 admits the fence parser is a sixth copy rather than a reuse and rewrites
  an exemption rationale whose subject no longer exists; S7 becomes two manifest rows with a registry
  route and the three-part count contract; and five ACs are added.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a declared per-subject limit resolved before the environment"`
routes to `tools/check-template-size.sh` and `tools/template-size-limits.txt`, whose resolution
order, keying discipline, named non-numeric failure and comment grammar this unit copies wholesale.
That is the seam: the same problem shape already has a solved answer in this tree, and the only
reason this is a second script rather than a mode of the first is stated in `§4`. The fence machine
is NOT reused: S5 measured that it is a private shell function nothing exports,
that its own script already carries four inline copies, and that sourcing it across kits is forbidden
here — so this gate writes a sixth copy and follows the precedent that keeps such copies honest, one
shared case table with agreement proven across implementations. An earlier revision of this paragraph
asserted the reuse S5 refutes.

Recall terms used: `line length limit declared subject environment precedence charter instruction
file adopter conf knob fence table character byte normalise`. The binding prior record is
`TOOL-aSiftedPlaybook-1`, which moved the size ceiling into a declaration and established that the
declaration must outrank the environment — S2 is that finding applied to a second predicate, and
ignoring it would reintroduce a bug that unit already paid for.
