# gate-lint — drop-in source-hygiene scans

Project-agnostic checks for classes that make a script misbehave **silently**.

The kit declares its own gate legs in `kit.toml`: `shell hygiene (a loop fed by a command
substitution)`, `shell hygiene (a location probe asked from a moved directory)` and
`shell-hygiene selftest`. It declared NONE until
`TOOL-aLeakedHandle-1`, and the PowerShell half below is still on no leg anywhere — see
*What is still unwired*. Anything not declared there is the consuming project's to wire, and the
two-line adoption step for that is documented here rather than left implicit.

## ps-hygiene.py

```bash
python3 <prefix>/gate-lint/ps-hygiene.py [root]   # exit 0 clean, 1 findings, 2 refusal
python3 <prefix>/gate-lint/ps-hygiene.py --selftest
```

Scans **every tracked** `.ps1` under `root`, listed by `git ls-files` and never by a walk of the
disk, so a worktree parked untracked inside the tree is not graded. The suffix matches in any case,
because a git pathspec glob would not, and the walk it replaced graded `Deploy.PS1` on Windows. A failed listing and a root that
tracks no `.ps1` each refuse with exit 2: both yield zero files, and only one of them means there is
nothing to grade. A repository that wired the scanner with no tracked `.ps1` therefore reds; drop the
line until PowerShell exists. It looks for two classes:

- **Case-only identifier collisions.** PowerShell variable names are case-INSENSITIVE, so `$LEGS`
  and `$legs` are ONE variable. Upstream this bit one file three times: `$LEGS = @($legs.legs)`
  overwrote a parsed manifest with its own sub-array, and `foreach ($sel in ...)` clobbered a `$SEL`
  selection map — which also disabled the backstop that read `$SEL`, because a guard sharing a
  variable with the thing it guards is not a guard.
- **BOM-less scripts containing non-ASCII.** PowerShell 5.1 decodes them as CP1252, so an em dash
  inside a double-quoted string becomes three chars ending in U+201D — which PowerShell accepts as a
  string delimiter. It closes the string early and desynchronises the parser. Every text-mode read
  hides this, so the check is byte-level.

## sh_hygiene.py

```bash
python3 <tool-root>/gate-lint/sh_hygiene.py [registry-path] [root]   # exit 0 clean, 1 findings, 2 refusal
python3 <tool-root>/gate-lint/sh_hygiene.py --selftest
```

Scans **every tracked** `*.sh` for one class: a `while … done` loop whose input redirect is an
unquoted heredoc, or a here-string, whose body holds a command substitution. `$( )` reads until
EOF; EOF arrives when the LAST inherited write end closes, not when the direct child exits. Where
the substituted command is a shell FUNCTION the substitution forks a subshell which forks the real
program, so the reader waits on a grandchild — and under MSYS that is not reliably the write end
that closes. Measured in the kit's home repository: a merge-bar leg sat at zero CPU for 63 minutes
with the forked subshell holding both ends of its own pipe and no descendant alive. The remedy is
a scratch FILE — redirect the walk to it, then read it by redirect, which keeps the loop in the
current shell so a `return` inside it still returns from the enclosing function.

It derives its population from `git ls-files` and takes the registry path as an OPTIONAL argument,
so it names nothing outside the kit by literal — and it ships nothing to that path either. With no
argument the run grades against an empty declaration and reports every carried site as undeclared.
That is the correct first install: a RED leg naming exactly the sites the tree already had, which
is the list you need in order to write a registry at all. An argument that WAS supplied and does
not resolve is a typo and refuses, because a mis-spelled path grading against nothing reads exactly
like an honest first run.

It counts `done < <(…)` and prints the count WITHOUT gating it. That form carries the same EOF
dependency, and it is the only one left for a NUL stream, because command substitution strips NUL
bytes. An empty population is a refusal rather than a pass.

### The registry, and filling it on a first install

The registry is a shrink-only declaration of the sites that PREDATE the gate. One row per site,
TAB-separated:

```
<path>\t<delimiter>\t<count>\t<why it is carried>
```

The key is the path plus the redirect DELIMITER — the heredoc tag, or `<<<` for a here-string — and
never a line number: a line-keyed registry reds on an edit above the waived line, and a gate whose
steady state is red gets bypassed. Set equality runs in BOTH directions, so a measured site with no
row fails AND a row the scan no longer finds fails; draining a site forces its row out in the same
commit instead of leaving a widened exemption behind. The count may FALL with the sites and may not
rise.

To fill it: run the leg with no argument and write one row per reported site, with a real reason.
Keep the file wherever that repository keeps its gate registries, and add its path to the leg's own
argv in that repository's leg manifest — that row is the adopter's to edit, not the kit's. A tree
with no carried sites needs no file at all, and an empty file says the same thing.

No count is written here or in the registry. The scanner derives the site and row totals and prints
both on every run, green included; a number typed beside them would be wrong on the next commit.

### `--location-probes` — a location probe asked from a moved directory

```bash
python3 <tool-root>/gate-lint/sh_hygiene.py --location-probes [registry-path] [root] [pathspec ...]
```

A second class, in the same scanner. With `GIT_DIR` set and no `GIT_WORK_TREE`, git takes the
CURRENT directory for the top of the work tree, so `git -C <dir> rev-parse --show-prefix` — and
`cd <dir> && git rev-parse --show-*`, its other spelling — answers about `<dir>` as if it were the
root. Git exports `GIT_DIR` into a linked worktree's hooks and merge drivers, so such a probe is
right in a shell and silently wrong under one: an empty prefix, or the probed directory named as the
repository root, and every reader downstream treats that as a legal answer.

Whether a hook can reach a given probe is a question about callers that no line predicate answers,
so the mode BANS THE SPELLING. Every probe opens its own substitution with the scrub, or carries a
registry row whose reason the scan prints on every run, green included:

```bash
top=$(unset GIT_DIR GIT_WORK_TREE; git -C "$dir" rev-parse --show-toplevel)
```

One scrub spelling is accepted on purpose: the probe is the first command of the `(` that opens with
exactly that `unset`. An `unset` earlier on the line, the other variable order, or a third variable
grades bare, and the hit prints the scrubbed spelling as its remedy. Never unset the variables for
the whole process instead: a check that reads `GIT_DIR` on purpose goes blind, and `GIT_INDEX_FILE`
names a different index on a partial commit.

The population is every tracked `*.sh` plus every tracked extensionless file whose first line is a
shell shebang, narrowed by the pathspecs. The shebang rule reaches a repository's git hooks without
the kit naming where it keeps them. The `-C` operand is read as a whole shell word, so a quoted
`"$(dirname -- "$0")"` is one operand rather than two. Every run prints the scanned file count, the
bare count, the scrubbed count and three near misses it reports and does not gate: a `-C` probe
asking the git dir or the common dir, which an inherited `GIT_DIR` answers correctly from inside its
own repository; `--show-*` asked with no move, which asks the caller's directory; and the gated
spelling inside a comment. The scanner's header lists what the mode does NOT check.

The registry has the loop registry's four fields and both-directions rule, keyed on the PROBE AS
WRITTEN instead of a delimiter — `-C <word> --show-<x>` or `cd <word> --show-<x>`, the word exactly
as the source spells it — and never on a line number. The argument is optional with the same three
states: absent grades an empty declaration and says so, supplied-and-unresolvable refuses, and an
empty population or a failed `git ls-files` refuses with exit 2.

### `--spawn-idioms` — a fork spent on builtin work

```bash
python3 <tool-root>/gate-lint/sh_hygiene.py --spawn-idioms [registry-path] [root] [pathspec ...]
```

A third class. A command substitution forks a subshell — 89 to 315 ms each under MSYS — and some
idioms fork for work bash does in the shell that asked. Three have no false positive and are BANNED
on the population the pathspecs select, with no registry escape: `$(date +%s)` and its `%s%N` form
(`$EPOCHSECONDS`, or `${EPOCHREALTIME/[.,]/}` scaled), `$(cat <<…` (read the heredoc first with
`IFS= read -r -d '' v <<'TAG' || :`), and `$(<f …)` carrying a second redirection, which defeats
bash's no-fork read so it reads EMPTY and still forks. Six more are counted per (path, class) in the
registry: `pure-fn-subst` (a function defined in the file or in a library it sources, whose body runs
only builtins), `printf-subst`, `cat-file`, `path-subst`, `date-fmt` and `var-pipe`. The registry
classes also count every tracked `*.test.sh`, so a suite site is a row rather than unseen; a BANNED
class grades the selected population alone.

A quoted heredoc's body is data and never graded, a spelling in a comment is a near miss, and a
callee that calls another function grades impure — a miss, never a false red. Every run prints each
class's scanned, gated and near-miss counts and every registered row's reason. The registry is the
loop registry's four fields keyed on the CLASS, `<path>\t<class>\t<count>\t<reason>`; a row naming a
BANNED class is refused rather than honoured. A converted reader takes the out-variable convention:
it sets a fixed global, clears it first so a miss never leaves the previous answer, and still
prints, so a caller writes `f x >/dev/null; v=$_f`. The scanner's header lists what it does NOT
check — how often a site runs above all, which is what the counter below is for.

### `--temp-names` — a fixed-name temp renamed into place

```bash
python3 <tool-root>/gate-lint/sh_hygiene.py --temp-names [registry-path] [root] [pathspec ...]
```

A fourth class. A file written at a temp name anyone can know before the write, then renamed over
its destination, is a name a process that can write the directory plants a link at first; the write
goes through the link into whatever it names. A `fixed-temp` site is an `mv` whose source names a
temp no unpredictable part names: `"$f.tmp"`, `"$x.tmp.$$"`, or a variable assigned one. The `mv` is
read as a command word at a segment's start or after `;`, `&`, `|`, `{`, `(` or `!`, past any run of
the keywords `if`, `then`, `else`, `elif`, `do`, `while` and `until`, the prefixes `command`, `builtin`
and `exec`, and assignment words such as `LC_ALL=C`. The mode admits two forms: a source holding
`$(mktemp`, and a variable bound by a BINDER — a function of the same file whose body sets
`printf -v "$1"`, holds `mktemp`, and expands `SRANDOM` only beside the test `${SRANDOM:-`, called as
`<binder> <name> <dest>`. A bare `SRANDOM` name is fixed: a bash before 5.1 leaves the variable unset,
so `"$f.$SRANDOM.tmp"` expands to `<f>..tmp`. A source that is one expansion is followed one hop, to
the latest binding of its name above it in the innermost function holding the line, else the top
level. A positional source, and one with no binding or whose binding is itself one expansion or one
positional, is UNFOLLOWED, counted and printed, never gated.

The population is the location-probe mode's: tracked `*.sh` files and extensionless shell-shebang
files under the pathspecs. A comment half and a quoted heredoc's body are never graded. Every run
prints the scanned count, the `mv` count, the fixed, admitted and unfollowed counts with their file
counts, each unfollowed source, and every registered row's reason; a failing key, undeclared or
drifted, is ONE finding listing `path:line  <source>` for each site, and a remedy line names the
admitted forms. The registry is the loop registry's four fields keyed on the one CLASS,
`<path>\tfixed-temp\t<count>\t<reason>`, shrink-only with both-directions set equality. The argument
is optional with the same three states, and an empty population or a failed `git ls-files` refuses
with exit 2.

What it does NOT check is one table in the scanner, `TEMP_BOUNDARY`: `run_temp_scan`'s docstring and
this section name each row, and the selftest runs each row's example and finds its label in both.
Unfollowed, so a miss: a positional source; a binding that is itself one expansion; a temp bound in
another scope; a loop variable; a binder in a sourced library; and an mv split across a line
continuation. Unread, no `mv` counted, so a miss: an mv in a case arm; an mv run through a wrapper
command, `env`, `time`, `nohup`, `xargs` or `command -p`; an mv named by a path or escaped; an mv
inside a quoted string or under eval; a fixed name written with no mv; and Python inside a shell
string. Admitted, so a miss: a mktemp temp in another directory, whose `mv` is a copy. Fixed, the
mode's one known false red: a name a function prints, which is not followed into the function; its
remedy is a binder.

## fork-count.sh

```bash
bash <tool-root>/gate-lint/fork-count.sh <ceilings-file> [root] [--only <id>]   # 0 within ceilings, 1 red, 2 refusal
bash <tool-root>/gate-lint/fork-count.sh --selftest
```

Counts the forks per invocation of each declared entrypoint, with no clock read anywhere. Each runs
under `env SHELLOPTS=xtrace BASH_XTRACEFD=<fd>` with a PS4 carrying `${BASHPID}` and the source
line; the forks are the distinct BASHPID values less the root's — a deterministic LOWER bound, since
a subshell that traces nothing is unseen. Every run first counts a specimen written from a quoted
heredoc and refuses with 2 when the count disagrees with its declaration, because a counter that
cannot move reports the same zero a clean tree does.

The ceilings file is the caller's, one row per entrypoint and bash `major.minor`:
`<id>\t<bash>\t<ceiling>\t<base>\t<setup>\t<command>\t<reason>`. `setup` builds the fixture untraced
in a fresh scratch directory and `command` is the one traced invocation; both see `ROOT` (the graded
tree) and `SCRATCH`. A row whose setup fails, and an entrypoint with no row for the running bash,
print `skipped — <id> · <why>` and are never counted as passed. A count above its ceiling reds with
the delta and the top ten `file:line` sites the forked subshells first traced at; a ceiling more
than max(3, 5 %) above its count reds as a saving nobody banked.

A run that grades no row never reads as a measured pass. An `--only <id>` naming no declared row
refuses with 2 and lists the declared ids. A selection holding a row for the running bash whose
every row was skipped, by a failed setup or a missing trace, refuses with 2 naming that bash. A
selection with NO row for the running bash keeps the `skipped` shape and exits 0, and prints
`fork-count: NOT MEASURED — no row declares bash <major.minor>, so the spawn budget was not measured
on this bash`, so the log shows the gap until that bash's rows are declared. The counter ships with this kit;
the home repository's leg is its own, because its ceilings name that repository's entrypoints.

## encoding_posture.py

```bash
python3 <tool-root>/gate-lint/encoding_posture.py [registry-path] [root] [pathspec ...]   # exit 0 clean, 1 findings, 2 refusal
python3 <tool-root>/gate-lint/encoding_posture.py --selftest
```

Scans **every tracked** `*.py` under the root, narrowed by any pathspecs, for text IO that names no
encoding: `open` / `.read_text` / `.write_text` / a provably-Path `.open` in text mode, and
`subprocess.*` with `text=True` or `universal_newlines=True`, each with no `encoding=`. Such a call
decodes with the platform default — cp1251 or cp1252 on a Windows node, UTF-8 in CI — so it
crashes on one machine and passes on the other, and a session or hook running the script directly
never sees the runner's environment. It reads the AST, because a line grep cannot see a call split
across continuation lines. Its header states what it does NOT check.

The registry is the shell scanner's shape keyed on the ARM instead of the delimiter:
`<path>\t<arm>\t<count>\t<why it is carried>`, where the arm is `file-io` or `subprocess`. Same
optional argument, same both-directions set equality, same refusal of a supplied path that does
not resolve. The clean line prints the graded file count, and a run over an empty population exits
1 rather than reading as coverage. No leg ships for it: wiring it, and seeding a registry, is the
consuming project's choice.

## Wiring it into a host project

Add it as a gate leg wherever that project enumerates them, e.g. an entry in a leg manifest, a CI
step, or a pre-commit hook:

```bash
python3 <prefix>/gate-lint/ps-hygiene.py . || exit 1
```

Run `--selftest` in the same place. Per the charter's `[gate]` practice, a gate
whose failing case has never been observed is not a gate — `--selftest` is how these prove they
can still fail after a refactor.

## What is still unwired

`ps-hygiene.py` is on no leg, here or anywhere. That is deliberate and it is a gap rather than a
decision: the kit's home repository has zero tracked `.ps1` files, and both scanners refuse an empty
population, so a leg here would red on every run. Wiring it earns its place in a repo where
PowerShell exists.

**Adoption is not automatic.** A repo with no tracked `.ps1` files gets the refusal and exit 2, not
a green line; the scan only earns its place where PowerShell exists.
