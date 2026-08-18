# TOOL-aFusedCharter-3 — an instruction file's lines get a declared maximum, defaulting to 450 characters

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

Gate the line length of the agent-instruction files this repo ships and reads, at a per-subject
DECLARED maximum defaulting to 450 characters, so a rule stays readable in a diff and an adopter can
move the number without editing a gate.

## 2. Scope (IN)

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
non-ASCII glyphs, so a byte count would grade a line with six em dashes as eighteen characters
longer than it reads. Carriage returns are stripped before measuring, exactly as
`tools/check-template-size.sh` does, so the verdict is checkout-independent on a Windows tree.

**S5 — Fenced blocks are exempt, and the exemption is stated.** A fenced code block holds a command
or a shape definition whose length is not the author's to choose, and wrapping one changes what it
means. The gate skips fenced regions using the same fence machine the hygiene gate's unfenced
scanner already implements, and its header states the exemption so a reader does not mistake a
green run for a claim about the whole file. Markdown tables are NOT exempt: a table row is prose in
a grid and can be split.

**S6 — Wrap the offenders this build creates.** Eight lines in the charter and five in the ruleset
exceed 450 at BASE, the worst at 1 051 and 1 499. Those files are rewritten by
`PLAY-aFusedCharter-1`, `-2` and `-3`, and this unit lands last precisely so it grades their output.
Wrapping is not a content change: a wrapped line is still one rule, which the ruleset's own preamble
states.

**S7 — A sibling self-test, and a leg.** Arms for: an over-length line reds naming the file, the
line number and the measured length; an exactly-at-limit line passes; a long line inside a fence
passes; a long line inside a table reds; a non-ASCII line is measured in characters; a declared row
beats an environment variable; a subject with no row falls through to 450; a declaration row naming
an absent path reds as stale, because a stale row silently narrows the population it was written to
cover. The suite prints its executed assertion count in the shape `tools/check-testsuite-counts.sh`
accepts.

**S8 — Ship it to adopters as a knob.** The kit descriptor carries the limits file as a seed so an
adopter receives a working declaration they own afterwards, and `WIRE-INTO-PROJECT.md` states the
one thing they need to know: the default is 450, the file is where you change it, and the row is
keyed by the path of your own charter, which may not be named `AGENTS.md`.

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

Measured at BASE with an awk pass over character length.

| Subject | Lines over 450 | Longest |
|---|---|---|
| the charter | 8 | 1 051 |
| the ruleset | 5 | 1 499 |
| the domain companion | 8 | — |

The companion is not in the population because it ceases to exist. Its eight offenders become the
ruleset's when `PLAY-aFusedCharter-1` folds it in, which is why S6's wrapping is sized against the
converged file rather than against these two rows.

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

New: `tools/check-line-length.sh`, `tools/check-line-length.test.sh`,
`tools/line-length-limits.txt`.
Edited: `tools/gate-legs.json`, the govkit registry and a descriptor, `WIRE-INTO-PROJECT.md`, plus
the wrapping in the two subject files.

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
- **AC9** — When `GATE_FULL=1 bash tools/run-gates.sh` runs, the new leg is present and green and
  every other leg is unchanged.

## 7. Gates

`run-gates canary` · `testsuite counts` · `govkit selfcheck` · `install-prefix (shipped surface)` ·
`codebase-map coverage + freshness` · `harness arms` · the new leg itself · the full bar.

## 8. Open questions

none — the forks below are RESOLVED.

- **F1 — is the ruleset in the population, or only the charter?** RESOLVED (agent, 2026-08-18,
  delegated by the build's stated order): both. Shipping a template whose lines red the gate shipped
  beside it hands an adopter a red bar on install day, which is the strongest possible argument and
  is not a preference.
- **F2 — are fenced blocks exempt?** RESOLVED (agent, 2026-08-18, delegated): yes, and the header
  says so. A command or a shape definition has a length its author does not choose. Tables are not
  exempt, because a table row can be split and a long one is the readability defect the gate exists
  to catch.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. The offender counts are measured, and the companion's eight
  are noted as migrating into the ruleset rather than disappearing.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a declared per-subject limit resolved before the environment"`
routes to `tools/check-template-size.sh` and `tools/template-size-limits.txt`, whose resolution
order, keying discipline, named non-numeric failure and comment grammar this unit copies wholesale.
That is the seam: the same problem shape already has a solved answer in this tree, and the only
reason this is a second script rather than a mode of the first is stated in `§4`. The fence machine
is reused from `check-memory-hygiene.sh`'s unfenced scanner rather than rewritten, since a second
fence parser is a second thing to drift.

Recall terms used: `line length limit declared subject environment precedence charter instruction
file adopter conf knob fence table character byte normalise`. The binding prior record is
`TOOL-aSiftedPlaybook-1`, which moved the size ceiling into a declaration and established that the
declaration must outrank the environment — S2 is that finding applied to a second predicate, and
ignoring it would reintroduce a bug that unit already paid for.
