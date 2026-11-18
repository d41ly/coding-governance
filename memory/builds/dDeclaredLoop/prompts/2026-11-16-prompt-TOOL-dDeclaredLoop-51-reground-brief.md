**Serves:** research TOOL-dDeclaredLoop-51

# Brief: re-ground spec TOOL-dDeclaredLoop-51 on the code as built

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. This build's specs predate the code the parent builds and its own earlier units landed. This spec is
re-grounded before its builder is dispatched.

## The brief

### Goal

Revise the spec of TOOL-dDeclaredLoop-51 in place, as a rev bump with one revision-log line, so a builder can build it as written
over HEAD. Where every claim already holds, change nothing and say so in your return.

### Items

1. Read the whole spec against the code at HEAD of branch/unattended-declared-loop-d56bf0 and settle every claim the landed
   code has moved. The branch has built every unit through build order 31, and of order 32 unit 50 is building now and unit
   22 builds after it (each built unit a CLOSED spec in this build's spec folder); it merged local main and origin/main. The
   review round bounds are policy keys read through `tools/loop/review_bounds.py` (unit 21, with unit 20's review.dispose
   keys and pin verb); the rework budget lives in `tools/loop/budget.py` (units 30, 48, 49, 61, 60, 62), with an `ending` verb
   and the ending rows (31) and a `target` verb (32); the driver gained `--fix-pass` (32), `--exhausted` (31) and `--trigger`
   (20), and its refusal census is 338, with unit 22 raising it to 340 under its landed decision row. Units 50 (rev-3, the six
   review `[[item]]` rows with step none) and 22 (rev-4, `--recommend`) are written on their committed specs. Unit 34 is
   deferred against ask TOOL-dDeclaredLoop-113. Unit 31's re-ground noted unit 52's S1 expects a row reading
   `hold = "exhaustion"`, which 31's built design (an owner-decision hold with an exhaustion row) does not match. An item the
   built code already satisfies leaves the spec's scope, said so.
2. THE SWEEP, before you return: for every function, file, constant and fixture the revised body changes or removes, find every
   caller, reader, fixture, suite arm, test population and frozen or pinned contract (upgrade step rows, subject pins,
   verdict-epoch delegates, census and family ceilings, size caps, the lexicon pin, help anchors and usage rows, the new leg's
   companions with a `stage` key) at the branch tip, and say in section 5 what keeps each green, with the commands that
   re-derive the counts. Unit 21's builder diverged four times on gaps its spec writers had not swept.
3. Check the write set against what the change really touches: registry rows, usage rows, subject pins, the verdict-epoch
   gate's delegate list, the kickoff manifest's watch list, generated map files, any line the install-prefix ban flags, and
   every existing fixture or selftest arm the change could newly red; name each in section 5 with what keeps it green.
4. A choice between designs is a section 8 fork with its options and your recommendation, and the spec body is written on the
   recommendation: the run takes it under its mandate.
5. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index.
6. Run the spec-token checker with its spec flag over the revised spec and fix every hit it names. Do not run the whole-tree
   memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on its line,
   a code citation is a symbol citation, a scope item that takes something away carries its readers clause, and no sentence
   in section 2 uses a retirement word for something it keeps. A by-name reader in a Readers clause is a tracked path,
   never `path#symbol`; name the symbol in words after the path.
7. Never kill a process you did not start, and never match processes by a script's name to stop them: other sessions run the
   same scripts on this node.
8. Units 19 and 51 build in parallel at build order 33, and units 33, 52 and 53 together at order 34; where this spec reads a sibling's code, write it on that sibling's committed spec and name the dependency in section 5. Your worktree may be cut from main, which lacks the
   loop kit: read every code claim from branch/unattended-declared-loop-d56bf0 through git show, and say which tree each
   check ran on.
   Never run check-memory-hygiene.sh, not even with --help. Keep each Readers clause's by name: and by value: halves each on
   one line, and name no unit id in a by name: half.
9. Four budgets and records stopped this build's earlier builders; name each the change reaches in section 5 with what
   keeps it green: the lexicon offender pin (every new function name through the lexicon's suggest verb), the shared
   records in `.unattended.conf`'s SHARED_RECORDS (a pass never writes `memory/DECISIONS.md`; spell out any decision row
   the run must land ahead), each script's refusal ceiling and its `.families.txt` families (measured with
   `tools/memory-tree/check-arms.py`'s own readers), and a help anchor for any new verb or flag.

### Acceptance

- Every claim the revised spec makes about current code is one you read at HEAD.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
