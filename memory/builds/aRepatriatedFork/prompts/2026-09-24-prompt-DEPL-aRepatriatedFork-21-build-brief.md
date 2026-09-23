# Build brief — DEPL-aRepatriatedFork-21

**Serves:** journal DEPL-aRepatriatedFork-21

## What you are handed

The spec at `memory/builds/aRepatriatedFork/spec/2026-09-24-spec-DEPL-aRepatriatedFork-21.md` is the design, and its §8 is resolved in place: every fork carries a
`RESOLVED` mark naming who decided it. Build what it says. Where the code disagrees with the spec,
change the spec first, as a rev-N bump with its §9 line naming the section, scope id or acceptance id
it moved; a §9 line naming none of those reds hygiene check 12.

The build's rules are in the `## Build-level rules` slot of `memory/builds/aRepatriatedFork/README.md`,
and they bind this unit: a fork retires only when gov's bytes run verbatim at the adopter, an adopter
fix is reproduced at gov HEAD before it is absorbed, a path fix is a derivation or a render and never
a new conf key for layout, no new bar leg lands without its ceiling and testsuite-count row, and a
new gate's red case is observed before it lands.

## The adopters are READ-ONLY

An acceptance criterion observed at inCMS or NicoCares runs in a `git clone --local --shared` of
`C:/projects/incms/main` or `C:/projects/nicocares/main`, under a SHORT directory in `%TEMP%` because
a clone under the scratchpad fails with Filename too long. Never write, commit, stash or check out
anything in either real tree. Say in `summary` which clone and which adopter HEAD each observation
used.

## Traps this repo has already paid for

- The working copy may hold CRLF. Edit files with the editor tools, or with Python in BINARY mode; a
  text-mode `open()` or a multi-line `str.replace` over CRLF silently matches nothing or eats bare CRs.
- Backslash escapes die inside Bash heredocs. Author scripts and fixtures with the file tools.
- A new Python function name is graded by the lexicon leg: ask
  `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>` before naming it.
- Touching a kit's shipped bytes owes that kit's version stamp in every carrier.
  `python tools/govkit/govkit.py selfcheck` names a carrier you missed; run it after such a change.
- `python tools/memory-tree/gen_build_index.py --write` sees tracked files only: `git add` a new file
  before rendering.
- `git rev-parse "<rev>:.claude/x"` is mangled by MSYS; use `git ls-tree <rev> -- <path>`.
- Two legs this build has already redded twice from inside a unit: run BOTH before committing, and
  commit only when both exit 0. `python tools/lexicon/lexicon.py` grades every new function name
  against a pin that is an equality; `bash tools/check-install-prefix.sh` is a BAN on new carried
  `tools/` literals, and its `--write-ratchet` cannot absorb one. Both are single checkers, not
  suites.

## What to return

`summary` names the direct check each acceptance criterion was observed by, and any criterion only
the merge bar or a self-test suite can observe, which the main loop runs once at the close.
