# DEPL-aTetheredConvoy-6 — the merged role, the attributes block, and the renormalize

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Build the one shape the deployer has always refused by name: writing a gov-owned region into a file
the target owns. That unlocks the three declared `merged` rules, which today strand their whole
entries and make an all-kits install land zero files, and it is the mechanism the first step of the
hard order needs — the line-ending pin block and the renormalize that follows it, which nothing in
this repo writes or performs.

## 2. Scope (IN)

- **S1 — one parameterized anchored-region writer inside the deployer**, reproducing the shipped
  region splice's refusal table exactly — column-0 exact match after stripping one trailing carriage
  return, exactly one open and one close, close after open, replacement by LINE INDEX and never by a
  regex over the file — and adding the one thing that table deliberately lacks: an INSERT path, for a
  first apply into a file that has no markers yet. REPRODUCED, not imported: the marker contract's own
  harness names a cross-kit edge as the forbidden shape and says the deliverable is agreement, proven.
- **S2 — one function owns the marker pair.** Neither merged source carries the markers its rule
  names, so the pair cannot be found — only synthesized — and the writer and the checker must
  synthesize the identical pair. One function, called by the source extractor, the writer and the
  drift extractor.
- **S3 — a per-destination insert policy, DECLARED as data.** A new rule key with two values: append,
  or refuse-and-order. Keyed on the rule, never on the filename — a filename switch inside the engine
  is the second spelling this repo names. The branch-guard destination gets refuse, because its
  position is SEMANTIC: the guard reads variables set near the top of the hook and must precede the
  legs, and guessing a position in a hook the target owns is a behavioural change to their commit path.
- **S4 — an append never joins two lines.** Before appending, read the destination's bytes and prepend
  a newline when they are non-empty and do not end in one. Measured: appending to a file whose last
  line lacks a trailing newline produces a concatenated line that destroys the target's own rule, makes
  git report an invalid attribute name on every attribute query in that repository, and leaves the
  block's open marker off column 0 — so every later apply refuses forever while the receipt claims a
  block that can never be found again.
- **S5 — the structural destination is DELEGATION, not a second writer.** The deployer does not write
  the settings document; it stops refusing the rule, runs the entry's existing adopter, FAILS the run
  on a non-zero exit, and computes the block hash itself over the marker-carrying entries only. Exit 0
  is not the write signal: the adopter returns unchanged when a matching marker substring is already
  present, so the delegation is followed by that adopter's own check arm AND an assertion that the
  extracted block is non-empty and its command equals the path the descriptor declares — not merely
  contains the marker.
- **S6 — the line-ending pin block, in TWO phases.** The block is WRITTEN early, before the first kit
  content write, because it is what every later checkout and the renormalize read. The PROBE, the
  renormalize and the post-condition run LAST, after configure, because on a first install the pinned
  population does not exist yet: the memory tree is scaffolded by an adopter, the confs are adopter
  outputs, and the rendered artifacts are produced at configure. A one-phase design either refuses
  every first install or reports success over nothing.
- **S7 — the renormalize's population comes from git, never from a pattern string.** An attributes
  PATTERN and a git PATHSPEC are different languages. Measured, one pattern that the attribute engine
  applies to a file at two depths matches only the deeper one as a pathspec, and another crosses a
  directory separator as a pathspec while not doing so as an attribute — they disagree in BOTH
  directions on the exact patterns this unit seeds. So the population is derived by asking git which
  tracked paths resolve to the pinned setting, and THOSE LITERAL PATHS are what the renormalize and the
  post-condition both operate on.
- **S8 — the pins are a new per-descriptor declaration**, with the gov-only remainder in a registry
  table on the same reason-and-staleness rule as the existing exemptions. Zero descriptors declare any
  line-ending data today; the seed population is read off gov's own attributes file and attributed to
  the entry that owns each path.
- **S9 — the block is the union of the receipt's kits AND the current selection.** A narrower later
  selection must not un-pin files whose kit is still installed; that would be invisible until someone
  re-checks-out on a foreign platform and a byte-comparing gate reds for reasons nothing records.
- **S10 — every artifact this unit writes is a `files` row through unit 1's single expansion**, so
  `plan` names the attributes destination and the renormalized set, and unit 2's verdict table can see
  them. A gov-owned artifact recorded as a top-level block is invisible to a per-row consumer forever.
- **S11 — merged-block drift in `check`**, which unit 5 deferred here because its precondition cannot
  occur until this writer exists: gone, removed, refused, drifted, or silent — and an edit OUTSIDE the
  block asserted POSITIVELY as not-a-finding rather than left as an omission.
- **S12 — the deployer becomes the fifth reader of the marker contract**, enrolled in BOTH halves of
  that harness: the behavioural case table, and the source-level assertion that its predicate carries
  the exact one-carriage-return literal. The behavioural half alone is CR-blind on this host, which the
  harness itself records, so a plausible-but-wrong predicate would pass all ten cases. The harness's
  reader count becomes derived rather than spelled in two places.

## 3. Non-goals (OUT)

- **The markdown pointer as a merged destination.** No descriptor declares it; the kit that owns that
  file deletes and rewrites it wholesale behind a force flag, and its detector is line-shaped because a
  one-line import has no region to anchor. If the append behaviour is wanted it belongs in the file
  that already detects, not in a region writer — putting a merged rule on that path would be a second
  writer on one file. So this unit has two mechanisms, not three.
- **Editing the target's attributes file beyond one block.** Gov owns a delimited region and nothing
  else.
- **Repairing a target's malformed pre-existing files.** The append into the packaging manifest parses
  the target's file first, to detect a duplicated table that would otherwise produce a document no
  reader can load. A target whose file was ALREADY malformed gets a refusal that says which file failed
  to parse and that gov did not write it.
- **A three-way merge on a merged region.** Unit 2's verdict table gains a `merged` row here, and it
  caps at report-and-refuse rather than reaching the three-way. A gov-owned region has an owner; a
  conflict in it is a decision, not a merge.

**Assumes:** units 1 (the expansion, the reserved `merged` and `attributes` receipt rows), 2 (the
verdict table this unit fills a row of) and 5 (`check`'s per-row dispatch, which this extends rather
than adding a second loop to).

**SUPERSEDES:** unit 2's refusal of `merged` rows and the acceptance criterion asserting the shared
refusal constant. Both must be rewritten in THIS unit's diff, and unit 2's `merged` verdict row filled
here — landing this without that leaves `update` permanently blind to the only three entries this unit
makes deployable. Also supersedes the deployer engine's own module docstring, whose two lists of
unbuilt work disagree with each other and would gain a third disagreeing spelling.

## 4. Design

### The measured starting point

Three descriptors declare a merged rule. Their sources carry no markers of any grammar, so the pair
must be synthesized. Two declared keys naming the grammar and the block are read by ZERO code, so a
typo in either passes the bar green today. One of the three rules declares an EMPTY include list — a
rule enumerating no files while still declaring a destination and a block, which is a fixture that
passes by finding nothing living inside the descriptor set.

The refusal is ENTRY-scoped, so a merged rule also strands its entry's landable rules: measured, an
all-kits install exits 1 with three refusals and lands ZERO files, and the criterion asserting the
all-kits selection cannot pass.

The nearest reusable writer is the shipped region splice, and the reuse is real for the REFUSAL TABLE
and false for the INSERT: its markers are hardcoded, and it refuses rather than inserting when no pair
is present, which is exactly the first-apply case.

### Why the pin phase splits in two

The natural design writes the block, renormalizes and checks the post-condition in one step before the
first content write. Measured, that fails in the direction this repo cares about most: on a first
install NONE of the pinned files is tracked yet — the memory tree does not exist until an adopter
scaffolds it, the confs are adopter outputs, and the rendered artifacts appear at configure. So the
post-condition either refuses every install or reports success over an empty population, which is the
pass-by-finding-nothing class sitting inside the step written to close it.

Writing early is still required: the block is what the renormalize and every later checkout read.
Hence two phases, and the acceptance criterion carries the arm the one-phase design has no room for —
a virgin target must exit 0 AND end with at least one ADOPTER-PRODUCED file reporting the pinned
setting in the index.

### Why the pathspec is derived from git

An attributes pattern and a git pathspec are different languages, and feeding one string to both was
measured wrong in both directions on the exact patterns this unit seeds. The population is therefore
obtained by asking git which tracked paths resolve to the pinned setting — the same mechanism the
wiring checker already uses — and the literal paths it returns are what the renormalize touches and
what the post-condition re-reads. That makes the renormalized set exactly the set the attribute
governs, makes the two steps quantify over one population, and turns "this pattern matches nothing"
into a question about git's own answer rather than about a second glob engine.

### The renormalize's price, and the refusal that bounds it

Measured: the pin alone changes nothing in the index; the renormalize is what converts it, so the step
is load-bearing and has a real failing direction. It touches tracked files only and cannot sweep an
operator's untracked work in. But it DOES rewrite a deliberately staged blob, and a tracked file
deleted in the worktree makes it abort entirely, staging nothing — which in the stated order happens
AFTER the block is written, leaving gov's block in the target's file with no renormalize and no
receipt.

So the precondition is not "no unstaged modification". It is: the pinned population is clean relative
to the last commit — which covers staged, unstaged and both — and no path in the population is missing
from the worktree. Both are one comparison each, and both run BEFORE the block write.

An in-progress merge, rebase or cherry-pick is a separate refusal: renormalizing mid-conflict rewrites
index stages the operator cannot reconstruct.

### Refusals write nothing

Stated once, because the design that produced this spec asserted both that a refusal writes an order
into the target and that a refusal writes nothing. Refusals write NOTHING; the block text and its
position rule go to standard output. The acceptance arm asserts the target's whole status is
byte-identical to the pre-apply capture, not merely that the receipt is absent — so any write on a
refusal path reds.

### The delegation, and why exit 0 is not the signal

The adopter returns unchanged when a matching marker substring is already present in the target's
settings, and then reports success. So a target carrying a foreign, disabled entry whose command
merely CONTAINS the marker would have that entry selected as gov's block, its hash recorded, and
`check` comparing it to itself and staying green forever over a hook that never runs. The delegation is
therefore followed by the adopter's own check arm, an assertion that the extracted block is non-empty,
and an assertion that its command EQUALS the path the descriptor declares. The rule's block-matching
declaration gains the event name it needs rather than leaving the engine to hardcode a second spelling
of it, and a `selfcheck` arm asserts both declared literals appear in the engine the adopter names —
so if the shipped matcher narrows, the descriptor's value stops being present and the arm reds.

That adopter also wires a SECOND gov-owned hook, which the one-block-per-rule model cannot represent.
It is declared here as a named non-goal with its reason rather than silently unmodelled.

### The accepted reformat, recorded rather than assumed

The structural merge re-serializes the whole document, so the FIRST apply reformats bytes the target
owns. That is recorded on the receipt row as an accepted reformat with the before and after hashes and
the backup path; on a second apply it is absent, because the adopter guarantees byte equality on a
no-op. Without that field the idempotency criterion still passes while every statement about that
file's bytes is wrong.

The block hash normalizes line endings before hashing, at write and at check, so the check stays green
after a foreign-platform re-checkout — correct, and it means the receipt does not describe the file's
literal bytes on disk. That is recorded as a field too, on the same principle.

### Rollout

1. **S1, S2, S3, S4, S12** — the writer, the pair, the insert policy, the newline guard, and
   enrollment in the marker contract. No pins yet.
2. **S5** — the delegation and its three post-conditions.
3. **S6, S7, S8, S9, S10** — the pin declaration, the two-phase attributes step, the git-derived
   population, and the plan rows.
4. **S11** — the drift arm, plus unit 2's superseded criterion rewritten and its `merged` verdict row
   filled.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the region writer, the attributes phase, the delegation |
| Registry | `tools/govkit/registry.toml` | the gov-only pin table |
| Descriptors | the pin declarations, the insert keys, the block-matching key | the count is DERIVED, and is deliberately not written here |
| Shipped files | the branch-guard hook and the packaging snippet gain their marker pairs | one delimited copy beats two undelimited spellings |
| Tests | `tools/govkit/selftest.py`, `tools/memory-tree/marker-contract.test.sh` | the fifth reader, both halves |
| Gates | `tools/gate-legs.json` | one leg's guard widens; one leg's name stops spelling a count |
| Map | `memory/map/features/govkit.md` | the Gaps section loses its largest entry |

### Alternatives rejected

**Import the shipped region splice.** Rejected: it lives in another kit, the deployer requires nothing,
and that harness names a cross-kit edge as the forbidden shape. Reproduce and prove agreement.

**Keep the branch guard in a separate snippet file, as the packaging kit does.** Rejected: two
spellings of the guard with nothing asserting they agree. One copy, delimited.

**Derive the pins from the receipt's own file list rather than declaring them.** Tempting — the first
review of the contract argued for it — and rejected: a pin's PATTERN covers files the receipt does not
name, including files an adopter will produce later, and the reason a pattern exists is not derivable
from a path list. Declared, with the derivation used for the renormalize's population instead.

## 5. Production-readiness checklist

- security — this unit mutates the index of a repo gov does not own, and writes into files the target
  authored. Every such write is bounded by a delimited region, preceded by a cleanliness refusal, and
  recorded. Nothing is committed.
- perf / scale — one attribute query over the tracked set, twice.
- a11y — N/A: a command-line tool.
- i18n — N/A for the interface; the block's own bytes are written with a fixed line ending by design.
- error / empty / loading states — the insert policy's three cases, the refusal list, and the
  two-phase split are this line.
- observability — the receipt's attributes row, the renormalized list, and the printed counts.
- risks — appending gov's pins at the END makes gov's rules win, so a target that deliberately set the
  opposite is silently overridden. The mitigation is a REPORT, not a refusal — refusing would make gov
  undeployable into any repo with an opinion — and the report compares the WHOLE resolved population
  before and after, not one sample per pattern, because attribute precedence is per-directory-depth
  first and a deeper file in the target overrides gov's root block regardless of where it was appended.
  Second risk: a target with the platform's line-ending conversion enabled and a foreign-ending history
  sees a large staged diff on the first apply; bounded by never renormalizing the whole tree, disclosed
  by a printed count, and never committed — and it must be priced in the operator-facing text, not only
  in the receipt. Third: an adopter installed without the memory-tree kit gets no marker-contract
  coverage at all, because that harness skips loudly when a sibling kit is absent; a deployer-side arm
  fails if the contract leg was skipped for the run that graded it.
- testing + left-shift gates — every arm has a liveness half, and three of them were reproduced in
  scratch repositories while this spec was written.
- migration / rollback — a target that already pasted the packaging snippet by hand receives the
  markers with it, so a later apply can find and update it; that is why the source-side markers are
  uniform rather than a per-destination fork in the engine.
- user docs — the runbook and the Skill carry the index-mutation disclosure.

## 6. Acceptance criteria

- **AC1** When `apply --kits push-main` runs against a fixture whose branch-guard hook already carries
  the operator's own line and gov's marker pair, the file afterwards contains BOTH the gov block and
  that line, and a second apply leaves it byte-identical. Liveness: one line INSIDE the block edited
  makes `python tools/govkit/govkit.py check --target <fixture>` exit 1 naming the block as drifted;
  the two marker lines deleted makes it exit 1 naming it REMOVED. The fixture's hook must be non-empty
  and NOT gov's copy, or "outside survives" quantifies over nothing.
- **AC2** When a destination whose rule declares refuse-and-order exists and carries no pair, `apply`
  refuses naming it, and `git status --porcelain` in the target is byte-identical to the pre-apply
  capture. Refusals write nothing, asserted on the whole status rather than on the receipt's absence.
- **AC3** When an append destination's last line lacks a trailing newline, the block is written on its
  own line: the target's pre-existing final rule still resolves through `git check-attr`, and a second
  apply SPLICES rather than refusing. Liveness: without the guard the same fixture produces a
  concatenated line — measured, and it is what makes every later apply refuse forever.
- **AC4** When a packaging-manifest append would redeclare a table the target already has, `apply`
  refuses naming the table; when the target's own file is already unparseable, the refusal says which
  file failed to parse and that gov did not write it.
- **AC5** When a fixture COMMITS a memory-tree file with foreign line endings and `apply --kits
  memory-tree` runs, `git ls-files --eol` reports the pinned setting in the index afterwards.
  Liveness, both measured: with the renormalize removed the attribute changes and the index does not;
  with the block write removed the attribute is absent.
- **AC6** When `apply` runs against a VIRGIN target with no memory tree and no rendered artifacts, it
  exits 0 AND at least one ADOPTER-PRODUCED file reports the pinned setting in the index afterwards.
  This is the arm a one-phase pin step has no room for.
- **AC7** When a declared pin resolves to zero tracked paths AFTER configure, `apply` reports a
  finding naming the pattern and its declaring entry. Liveness: measured, a pathspec matching nothing
  exits 0 silently, so without this arm the phase reports success over an empty set.
- **AC8** When the pinned population is not clean relative to the last commit — staged, unstaged, or
  both — or when a tracked path in it is missing from the worktree, `apply` refuses BEFORE the block
  write, naming every such path, and the target is byte-identical afterwards. Liveness, measured: a
  deliberately staged foreign-ending blob is REWRITTEN by an unguarded renormalize, and a deleted
  tracked path makes it abort staging nothing.
- **AC9** When an `apply --kits` run follows an earlier apply with a NARROWER selection, the pin block
  still carries the earlier kits' patterns, asserted against the receipt's kit list rather than the current
  selection.
- **AC10** When `apply --kits agent-cap,settings-merge` runs against a fixture whose settings document
  is differently indented and carries an unrelated key, run 1's receipt row records an ACCEPTED
  reformat with differing before and after hashes, the file still parses with that key intact, and the
  backup holds the original bytes; run 2 is byte-identical and its row carries no reformat. Liveness:
  the fixture must not start already-wired, or run 1 reformats nothing.
- **AC11** When the target's `.claude/settings.json` already carries a FOREIGN entry whose command merely
  contains the marker, the delegation does not record it as gov's block: the post-conditions red, naming the
  command that does not equal the declared path. Liveness: the correctly-wired fixture passes through
  the same three post-conditions.
- **AC12** When `python tools/govkit/govkit.py selfcheck` runs, it reds when a block-matching
  declaration's literals do not appear in the engine file the entry's adopter names, and reds on a
  marker style outside the enum, on a merged source carrying zero or more than one pair for its block,
  and on a rule declaring a block with an empty include list.
- **AC13** When `bash tools/memory-tree/marker-contract.test.sh` runs, it drives the deployer's
  predicate over the whole case table AND asserts at SOURCE level that the predicate carries the exact
  one-carriage-return literal, and prints a reader count DERIVED from the reader list. Liveness: the
  behavioural half alone is carriage-return-blind on this host — the harness records that measurement
  — so a plausible-but-wrong predicate passes all ten cases and must fail the source half.
- **AC14** When `plan` runs, the attributes destination and the renormalized path set appear as rows,
  and `apply` produces exactly that set — through unit 1's single expansion, asserted as sets.
- **AC15** When `apply --all` runs, it lands the engine files of the three entries a merged rule
  strands today. Liveness: measured, the same command exits 1 with three refusals and lands ZERO
  files, so each named path provably does not exist before this unit.
- **AC16** When unit 2's `update` runs against a target carrying a merged row, it reports the row
  against its recorded block hash and never invokes a three-way on it. The criterion unit 2 wrote
  asserting a shared refusal constant is REWRITTEN in this unit's diff, not left dead.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. No new leg; two
existing legs change. The marker-contract leg gains a reader and stops spelling a reader count in its
own name, and the deployer's selftest leg's guard widens to include the hook directory — otherwise a
diff touching only the merged source would not re-run the arms that depend on its markers.

Gov's own branch-guard hook gains two comment lines. Its behaviour is unchanged and its bytes are not,
and three repo-wide readers scan tracked files outside the memory tree; the guard widening above is
part of this unit, not a follow-up.

The kit version constant moves.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. Two classes are live
by construction: `gate-green-by-accident-on-generated-bytes`, because this unit writes the pins that
gate reads; and `heredoc-escape-reaches-the-regex`, because the block text passes through shell in
several arms.

## 8. Open questions

none — the forks below are RESOLVED. Authority: the owner's instruction to execute this build
delegates resolver authority for THIS build only, and every fork here is one the spec already stated,
which is exactly M3's condition. Each was taken through M3's veto order; none was discarded by a veto,
and the two that touch a write or security surface are called out in the wrap-up as owner-review items
rather than treated as settled by silence.

- **F1 — does the settings adopter's SECOND gov-owned hook become a merged rule?** RESOLVED (agent,
  2026-08-16, delegated): no — a named non-goal with a backlog row. The one-block-per-rule model cannot
  represent two blocks in one destination, and widening it to carry a list changes the shape every
  other consumer dispatches on, for one hook whose adopter already manages it correctly.
- **F2 — per-entry pins only, or a registry table for the remainder?** RESOLVED (agent, 2026-08-16,
  delegated): both, as written. Several pins belong to no deployable, and forcing them into an entry
  would attribute a gov-internal rule to a kit an adopter receives.
- **F3 — is the attribute-override report a refusal instead?** RESOLVED (agent, 2026-08-16, delegated):
  a report. Refusing would make gov undeployable into any repository with an opinion about line
  endings. **Flagged for the wrap-up as an owner-review item**: it is the one place this build
  knowingly overrides a target's own declared rule and answers with a message rather than a stop.

## 9. Revision log

- rev-2 · 2026-08-16 · M3 fork sweep: F1, F2 and F3 resolved in place under the owner's
  execute-the-build delegation. F3 is FLAGGED for the wrap-up: it is the one place this build
  knowingly overrides a target's own declared rule and answers with a message rather than a stop.
- rev-1 · 2026-08-16 · initial draft. Grounded on a twelve-agent audit and adversarial pass. Four of
  this spec's load-bearing decisions came from the adversary rather than the designer, each reproduced
  in a scratch repository: the trailing-newline guard, without which the first apply into an ordinary
  repository destroys a rule gov did not write and refuses forever afterwards; the two-phase pin step,
  without which a first install either refuses or reports success over an empty population; deriving
  the renormalize's population from git rather than from the pattern string, because the two languages
  were measured disagreeing in both directions on the exact patterns seeded here; and staging the
  attributes file as a receipt row, without which the pins live only in an untracked working-tree file
  and every assertion about them passes on a target that would lose them at the next clone.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the anchored region and the structural merge.

The shipped region splice is the REFUSAL TABLE this unit reproduces — one open, one close, close after
open, column-0 exact match after one carriage return, replacement by line index. Reproduced rather than
imported, because that harness names a cross-kit edge as the forbidden shape and the deliverable as
agreement proven; enrollment as its fifth reader, in both halves, is how the agreement is proven.

The shipped structural merger is the settings destination's whole implementation and its only existing
definition of where that block starts and stops. This unit delegates to it and adds post-conditions
rather than reimplementing a JSON anchor.

The wiring checker's attribute query is the seam for deriving the renormalize's population from git
rather than from a pattern string.

Two declared keys naming the merge grammar and the block, and a third naming a rule's side effects,
already exist on the three merged rules and are read by ZERO code. This unit is their first consumer;
before it, all three pass the bar green with a typo'd value, which is why the acceptance criteria
include arms for exactly that.

The report channel, the outbox convention and the entry-scoped pre-write refusal pass are reused
unchanged.

No seam exists for the insert path, for a line-ending pin declaration of any kind — measured, zero
occurrences across every descriptor and the registry — or for the renormalize, which nothing in this
repo performs. All three are new, and the first is the one sentence of new logic the shipped splice
deliberately does not contain.
