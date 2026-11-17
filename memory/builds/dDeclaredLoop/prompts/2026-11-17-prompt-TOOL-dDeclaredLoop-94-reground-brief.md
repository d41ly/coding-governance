**Serves:** research TOOL-dDeclaredLoop-94

# Brief: re-ground spec TOOL-dDeclaredLoop-94 on the code as built

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. This build's specs predate the code the parent builds and its own earlier units landed. This spec is
re-grounded before its builder is dispatched.

## The brief

### Goal

Revise the spec of TOOL-dDeclaredLoop-94 in place, as a rev bump with one revision-log line, so a builder can build it as written
over HEAD. Where every claim already holds, change nothing and say so in your return.

### Items

1. Read the whole spec against the code at HEAD of branch/unattended-declared-loop-d56bf0 and settle every claim the landed
   code has moved. The branch has built every unit through build order 45, each a CLOSED spec in this build's spec folder
   (unit 91, c7a472129: `derive_conf_rebinds` takes a class as a global loader and reads every module-scope part of a definition
   from `_MODULE_SCOPE_PARTS`, and the conf-read-forms module-scope group with an exec parity line per row). Unit 92 (order 46,
   rev-5) is building now: only its S8 (the shared git-env-leaks block carried inline in `tools/loop/loop_witness.py`, so
   `read_clean_env` stops importing tree_lib and `TREE_LIB_SYMBOLS` keeps two names, F3 (c)) and S17 (the guard's `OSError` detail
   from the exception's own text, F4) build. Unit 93 (order 47) is re-grounded at rev-3 as an observation pass that writes no
   file. Under 92's F3 (c), any item here that puts `GIT_ENV_LEAKS` behind `load_tree_lib` or adds a `need` argument to it has
   nothing left to change: settle it in section 3. Built since the last re-grounds, in the files this spec most likely reads: unit 79 (a8b4dca02: the round-4
   minors, `read_driver_conf`'s isolated subshell, the gained prune's D-to-E row owing exit 2); unit 82 (a0ba898db, rev-8:
   `derive_import_aliases`, `derive_conf_reads` counting a conf name anywhere, an aliased reader and a `loop_lib` conf constant,
   `derive_docstring_ids` in `tools/memory-tree/tree_lib.py`, eight PLANTS descriptions naming each conf in words); unit 86
   (16829da16: `derive_conf_constants(loop_lib_path)`, the guard's usage probe and failure detail, the url-forms credential
   isolation); unit 87 (82087c644: the conf-constant kind as a class); unit 89 (20362ef2b: `load_tree_lib`, `derive_conf_rebinds`,
   `check_conf_name`); unit 88 (5b4e1a339: `derive_constant_charges` in tree_lib as the one charge walk, `load_tree_lib`'s
   LookupError, ImportError and SyntaxError catches, four guard plants, the guard row at 140 s); unit 90 (b10a81331:
   `TREE_LIB_SYMBOLS` and `load_tree_lib` testing each name, three conf-read-forms rows, the version-skew row). Every PLANTS
   description names a conf in words, never by its file name. Unit 34 is deferred against ask TOOL-dDeclaredLoop-113, and unit
   33's numeric direction against ask TOOL-dDeclaredLoop-114. A CLOSED spec is frozen: never plan an edit to one. An item the
   built code or a committed spec already satisfies leaves the spec's scope, said so.
2. THE SWEEP, before you return: for every function, file, constant and fixture the revised body changes or removes, find every
   caller, reader, fixture, suite arm, test population and frozen or pinned contract (upgrade step rows, subject pins,
   verdict-epoch delegates, census and family ceilings, size caps, the lexicon pin, help anchors and usage rows, the new leg's
   companions with a `stage` key) at the branch tip, and say in section 5 what keeps each green, with the commands that
   re-derive the counts. Unit 21's builder diverged four times on gaps its spec writers had not swept.
3. Check the write set against what the change really touches: registry rows, usage rows, subject pins, the verdict-epoch
   gate's delegate list, the kickoff manifest's watch list, generated map files, any line the install-prefix ban flags, and
   every existing fixture or selftest arm the change could newly red; name each in section 5 with what keeps it green.
4. A choice between designs is a section 8 fork with its options and your recommendation, and the spec body is written on the
   recommendation: the run takes it under its mandate. Every fork in section 8, old or new, ends with its own mark,
   `RESOLVED (agent, 2026-11-17, delegated): (<option>)`, on a line inside its span; a fork with no mark refuses the CLOSED commit.
5. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index.
6. Run the spec-token checker with its spec flag over the revised spec and fix every hit it names. Do not run the whole-tree
   memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on its line,
   a code citation is a symbol citation, a scope item that takes something away carries its readers clause, and no sentence
   in section 2 uses a retirement word for something it keeps. A by-name reader in a Readers clause is a tracked path,
   never `path#symbol`; name the symbol in words after the path.
7. Never kill a process you did not start, and never match processes by a script's name to stop them: other sessions run the
   same scripts on this node.
8. Unit 92 builds at build order 46, unit 93 at order 47, unit 94 at order 48 and unit 95 at order 49; where this spec reads a sibling's or an
   earlier order's code, write it on that unit's committed spec and name the dependency in section 5. Your worktree may be cut from main, which lacks the
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
