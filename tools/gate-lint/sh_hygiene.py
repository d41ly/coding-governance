#!/usr/bin/env python3
"""Shell source-hygiene scan — a loop reader fed by a command substitution, which can block forever,
and, as a second mode, a location probe asked from a moved directory, which answers wrong in a hook.

Project-agnostic. Run over any repo:

    python <this file> [registry-path] [root]     # scan; exit 0 clean, 1 on an undeclared site
    python <this file> --location-probes [registry-path] [root] [pathspec ...]   # the second class
    python <this file> --selftest                 # prove both predicates in BOTH directions

THE SECOND CLASS, `--location-probes`. With `GIT_DIR` set and no `GIT_WORK_TREE`, git takes the
CURRENT directory for the top of the work tree. So `git -C <dir> rev-parse --show-prefix`, and the
`cd <dir> && git rev-parse --show-*` spelling of it, answer about `<dir>` as if it were the root.
Git exports `GIT_DIR` into a linked worktree's hooks and merge drivers, so every such probe is
right in a shell and silently wrong under one. Whether a hook can REACH a given probe is a question
about callers, which no line predicate decides, so this is a BAN on the spelling: every probe opens
its own substitution with `unset GIT_DIR GIT_WORK_TREE;`, or carries a registry row whose reason is
printed on every run. The population is every tracked `*.sh` plus every tracked extensionless file
whose first line is a shell shebang, narrowed by the pathspecs. The registry is the grammar below,
keyed on the probe AS WRITTEN, `-C <word> --show-<x>` or `cd <word> --show-<x>`, never a line.
Three near-miss counts are printed and not gated: a `-C` probe asking the git dir or the common dir,
which an inherited `GIT_DIR` answers correctly from inside its own repository; `--show-*` asked
with no move, which asks the caller's directory; and the gated spelling inside a comment.

WHAT `--location-probes` DOES NOT CHECK, each a MISS and never a false red: reachability; a probe
split across a line continuation; a probe built in a variable, through `eval`, or behind any wrapper
but `GIT`; a `cd` carrying an option or a redirect before its `&&`; Python and JavaScript callers;
other subcommands run with `-C` into a subdirectory, such as `ls-files`, whose answers move the
same way; quoting carried across lines; and a scrub that unsets the variables for a whole function
rather than inside the substitution, which grades BARE — one spelling is accepted on purpose, so the
other order, a third variable and an earlier top-level `unset` all grade bare and name the remedy.

THE CLASS. `while read … done <<TAG` with `$(cmd)` in the heredoc body, or `done <<< "$(cmd)"`.
The substitution reads until EOF, and EOF arrives when the LAST inherited write end of its pipe
closes — not when the direct child exits. Where the substituted command is a shell FUNCTION the
substitution forks a subshell which forks the real program, so the reader depends on a grandchild's
write end; under MSYS that is not reliably the one that closes. Measured in this repository on
2026-09-10: a merge-bar leg sat at zero CPU for 63 minutes with the forked subshell holding both
ends of its own pipe and no descendant alive. The remedy is a file — redirect the walk to a scratch
file and read the file — which keeps the loop in the current shell, so a `return` inside it still
returns from the enclosing function.

AND THE SAME CLASS ONE ASSIGNMENT AWAY, which is the widening and the reason it exists. A body
spelled `$var`, where `var` took its value from a command substitution earlier in the file, is the
identical defect written over two lines: the fork, the EOF dependency and the stall are all at the
assignment, and the loop is only the shape that tells a reader the value had to be carried whole.
The narrow predicate graded such a body as a substitution-free heredoc — a NEAR MISS — and on
2026-09-18 that blind spot was found holding a live instance in this tree, in a reader called once
per commit, which had already cost four runs of its own driver. A check that cannot fail for the one
shape it most needed to reach is the failure this leg was written about. So a plain expansion in a
loop-feeding body is now followed back ONE assignment, and a hit there is gated like any other.

WHY THE LOOP-FEEDING FORMS ALONE. A command substitution that is an ARGUMENT (`x=$(cmd)`,
`f "$(cmd)"`) has the same EOF dependency but a bounded consumer, and banning those would red every
assertion helper in every test file here. Run over this tree before the ban was wired, the four
near-miss populations separated cleanly from the failing one — the counts are printed on every run,
green included, and they are DERIVED, never authored.

WHAT THIS DOES NOT CHECK, said here because a structural check reads as a semantic one to everyone
who did not write it:

  * `done < <(cmd)`, the process-substitution form. It has the same EOF dependency and it is NOT
    banned: a NUL stream cannot ride a heredoc, because command substitution strips NUL bytes, so
    process substitution is the only form left for those consumers. It is COUNTED and its count is
    PRINTED, so a green line is never read as covering it.
  * `out=$(timeout N cmd)` and every other non-loop command substitution. Out of the failing
    population by construction, and gated — partially — somewhere else.
  * Whether a substitution can ACTUALLY hang. This reads shape. A `$(printf …)` in a heredoc body
    is a hit because the shape is what a later edit turns dangerous, not the command of the day.
  * Anything a quoted delimiter disables. `<<'TAG'` performs no expansion, so it cannot hold a
    substitution and is graded as a substitution-free loop heredoc.
  * A feed the shell honours but this reader cannot see on ONE line: a second heredoc on the
    same line (`cmd <<A <<B` — only the first is classified) and a redirect split across a line
    continuation. Neither exists in the tree this landed against. A repo that writes them gets a
    silent MISS rather than a refusal, and it is written down because a heuristic with an
    unstated blind spot is how the sibling scanner in this kit got its first one.
  * Quoting carried ACROSS lines. `extract_code` cuts the comment half of each line on its own,
    so an unterminated quote opened on a previous line leaves this one's tail reading as code.
    The failure direction is a MISS and never a false RED, which is the way round this leg needs
    it: it is `subject = repo` with no guard, so a red on an innocent file blocks every push.
  * MORE THAN ONE assignment, and every scope rule a shell has. The follow is one hop, over a FLAT
    per-file table keyed on the name: the latest assignment textually above the loop wins, an
    assignment from anything but a substitution CLEARS the name, and a function boundary, a
    subshell, a branch not taken and a same-name local are all invisible. Two directions, both
    written down because a heuristic with an unstated blind spot is how the sibling scanner here
    got its first one. A value that arrives through two hops (`a=$(cmd); b=$a`) is a MISS. A name
    assigned from a substitution in one function and expanded in a loop in another is a false HIT,
    and the registry is where one lands until someone drains it — so the widening is kept to one
    hop deliberately, because each further hop buys misses back at a worse rate than it costs.
  * `read var`, `mapfile`, `printf -v`, array elements and `${var:=$(cmd)}`. None of them is an
    assignment this reader sees, so each is a MISS.
  * A `;` inside quotes, which splits a line into segments the shell would not. The anchored
    assignment pattern makes that mostly a miss, and the residue is a possible false HIT on a
    fragment such as `msg="a; b=$(cmd)"`. It costs a registry row and never a wrong verdict about
    behaviour, and the population this landed against was checked by hand and holds none.

THE REGISTRY is a shrink-only declaration of the sites that predate the gate, one row per
`<path>\t<delimiter>\t<count>\t<reason>`, keyed on the delimiter and NEVER on a line number — a
line-keyed registry reds on unrelated edits, and a gate whose steady state is red gets bypassed.
Set equality in both directions: a measured site with no row fails, and a row the scan no longer
finds fails, so draining a site forces its row out instead of leaving a widened exemption behind.

THE REGISTRY ARGUMENT IS OPTIONAL, and omitting it is a POSTURE rather than a mistake. With no
argument the run grades against an empty declaration and reports every measured site as undeclared
— a RED leg, which is the honest first reading of a tree nobody has graded yet, and byte-identically
what an empty registry file produces. An argument that WAS supplied and does not resolve is a typo
and refuses: `resolve_declaration` keeps those two apart, because collapsing them would let a
mis-spelled path grade silently against nothing while reading exactly like a first install.
"""
from __future__ import annotations

import contextlib
import io
import os
import pathlib
import re
import subprocess
import sys
import tempfile

# A command substitution, arithmetic expansion excluded — `$((` is not a fork.
SUBSTITUTION = re.compile(r"\$\((?!\()|`")
# `done` as a word. The hyphen guard keeps `well-done` and `done-with` out.
DONE = re.compile(r"(?<![\w-])done(?![\w-])")
# `< <(` — process substitution feeding a redirect. Spelled with the gap because `<<(` is not it.
PROCESS_SUB = re.compile(r"<[ \t]+<\(")
# `<<TAG`, `<<-TAG`, `<<'TAG'`. The `(?!<)` is what keeps a here-string out of this branch.
HEREDOC = re.compile(r"<<(-?)[ \t]*(?!<)(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\2")
HERESTRING = "<<<"
# A registry delimiter is a heredoc tag or the here-string operator. A line number matches neither,
# which is what makes AC6's malformed-key arm a shape test rather than a convention.
DELIMITER = re.compile(r"\A(<<<|[A-Za-z_][A-Za-z0-9_]*)\Z")
# `name=value`, through any number of declaration keywords. Anchored at the start of a `;`-split
# segment, so `a=$1; b=$(cmd)` is two assignments and a `foo --flag x=1` argument is none.
ASSIGNMENT = re.compile(
    r"\A[ \t]*(?:(?:local|export|declare|readonly|typeset)[ \t]+)*([A-Za-z_][A-Za-z0-9_]*)\+?=(.*)\Z",
    re.S)
# A parameter expansion's NAME. `${x#y}` and `$x` both yield `x`; `$1` and `$@` yield nothing, which
# is right — a positional is not a name this scan can follow to an assignment.
EXPANSION = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)")

# The taxonomy, in report order. The first two are the failing population; the rest are printed so
# the reader can tell "no hits" from "nothing was looked at", and so the process-substitution count
# is never mistaken for coverage.
CLASSES = [
    ("loop-heredoc-sub", "loop fed by a heredoc holding a command substitution", True),
    ("loop-herestring-sub", "loop fed by a here-string holding a command substitution", True),
    ("loop-var-sub", "loop fed by a heredoc or here-string over a VARIABLE assigned from a "
                     "command substitution — the same defect, one assignment away", True),
    ("loop-heredoc-plain", "loop fed by a heredoc with NO command substitution", False),
    ("heredoc-sub", "non-loop heredoc holding a command substitution", False),
    ("herestring-sub", "non-loop here-string holding a command substitution", False),
    ("procsub", "loop fed by a process substitution, `done < <(...)` — REPORTED, NOT GATED", False),
]
GATED = [key for key, _label, gated in CLASSES if gated]

# ---- the LOCATION-PROBE class, `--location-probes` ----------------------------------------------
# One level of `$( )` holding plain text and quoted strings. A probe's `-C` operand is often one,
# `"$(dirname -- "$0")"`, and a `[^ ]+` operand reads that as two words and misses the probe.
_PROBE_SUB = r"\$\((?:[^()\"']|\"[^\"]*\"|'[^']*')*\)"
# A shell WORD: double-quoted, single-quoted and unquoted runs, concatenated.
PROBE_WORD = (r"(?:\"(?:[^\"\\$]|\\.|" + _PROBE_SUB + r"|\$(?!\())*\"|'[^']*'|" + _PROBE_SUB
              + r"|\\.|\$(?!\()|[^\s\"'`();&|$\\])+")
_PROBE_GIT = r"(?<![\w$.-])(?:git|GIT)(?:[ \t]+-c[ \t]+" + PROBE_WORD + r")*"
_PROBE_FLAG = r"[ \t]+--[A-Za-z][\w-]*(?:=" + PROBE_WORD + r")?"
_PROBE_TAIL = r"[ \t]+rev-parse(?:" + _PROBE_FLAG + r")*[ \t]+--"
_PROBE_ASKS = r"(show-(?:prefix|toplevel|cdup))(?![\w-])"
_PROBE_MOVE = (_PROBE_GIT + r"[ \t]+-C[ \t]+(" + PROBE_WORD + r")(?:[ \t]+-c[ \t]+" + PROBE_WORD
               + r"|" + _PROBE_FLAG + r")*" + _PROBE_TAIL)
# The two gated forms. Group 1 is the moved-to word and group 2 the flag asked, in both.
PROBE_C = re.compile(_PROBE_MOVE + _PROBE_ASKS)
PROBE_CD = re.compile(r"(?<![\w$.-])cd[ \t]+(" + PROBE_WORD + r")[ \t]*(?:&&|;)[ \t]*" + _PROBE_GIT
                      + _PROBE_TAIL + _PROBE_ASKS)
# Two of the near misses: the git dir asked from a moved directory, and `--show-*` with no move.
PROBE_IDENTITY = re.compile(_PROBE_MOVE + r"((?:absolute-)?git-dir|git-common-dir)(?![\w-])")
PROBE_CWD = re.compile(_PROBE_GIT + _PROBE_TAIL + _PROBE_ASKS)
# The one scrub accepted: the probe is the FIRST command of the substitution that opens with it.
PROBE_SCRUB = "unset GIT_DIR GIT_WORK_TREE; "
SCRUBBED = re.compile(r"\(unset GIT_DIR GIT_WORK_TREE;[ \t]+\Z")
# A shell shebang on an extensionless file — sh, bash, dash, ksh or zsh, direct or through `env`.
SHELL_SHEBANG = re.compile(rb"\A#![^\n]*?[/ \t](?:ba|da|k|z)?sh(?:[ \t\r]|\Z)")
# A probe registry key. A line number matches neither form, which is AC3's malformed-key arm.
PROBE_KEY = re.compile(r"\A(?:-C|cd) \S.* --show-(?:prefix|toplevel|cdup)\Z")
# The registry key shapes: the pattern, what a malformed key is not, and what the key is.
DELIMITER_SHAPE = (DELIMITER, "a heredoc tag or `<<<`", "DELIMITER")
PROBE_KEY_SHAPE = (PROBE_KEY, "a probe as written, `-C <word> --show-<x>` or `cd <word> --show-<x>`",
                   "PROBE as written")
# The probe taxonomy, in report order: (key, mark, label).
PROBE_CLASSES = [
    ("bare", "GATED", "a location probe asked from a moved directory with no scrub"),
    ("scrubbed", "scrubbed", "the same probe, first in a substitution opening `(unset GIT_DIR GIT_WORK_TREE;`"),
    ("identity", "near miss", "`-C <dir> rev-parse` asking the git dir or the common dir"),
    ("cwd", "near miss", "`rev-parse --show-*` with no `-C` and no `cd` — it asks the caller's directory"),
    ("comment", "near miss", "a comment carrying the gated spelling — it never runs"),
]

#: The executed-assertion floor for `--selftest`, compared against the count it prints.
#: A printed count nothing reads is the same nothing as no count: this repository has shipped
#: nine arms stranded past an unconditional exit while the suite printed a total and every
#: other gate held. Raise it with the arms; it may never be lowered to fit a regression.
FLOOR_ASSERTIONS = 55


def check_substitution(text: str) -> bool:
    """True when the text holds a command substitution rather than a plain expansion."""
    return bool(SUBSTITUTION.search(text))


def extract_code(line: str) -> str:
    """The CODE half of one line: everything before the `#` that opens an unquoted comment.

    A line that is code with a trailing comment used to be classified WHOLE, so `# … <<EOF` in the
    comment was matched as a real heredoc opener, the rest of the file became its body, and an
    innocent file was reported under a GATED key. This leg is `subject = repo` with no guard, so it
    runs at the push boundary — a false RED here blocks every push with no remedy the registry can
    supply, and a gate whose steady state is red gets bypassed.

    A `#` opens a comment only where the shell says it does: outside quotes, and at the start of a
    word. `x=a#b` and `${x#y}` keep their `#`, and a quoted one is data. The backslash escape is
    honoured everywhere but inside single quotes, where bash does not honour it either.

    WHAT THIS DOES NOT DO: track quoting ACROSS lines. An unterminated quote makes this line's tail
    look like code; that direction can only cost a hit, never invent one, and a heredoc body is
    read by `extract_heredoc_body` and never by this.
    """
    quote = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and quote != "'":
            i += 2
            continue
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "'\"":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t;&|("):
            return line[:i]
        i += 1
    return line


def extract_heredoc_body(lines: list[str], start: int, dash: str, tag: str) -> tuple[list[str], int]:
    """The body after line `start`, and the index of its terminator (or -1 when unterminated).

    An unterminated heredoc returns the rest of the file and -1. The caller must then NOT skip
    ahead: swallowing the remainder of a file on one malformed tag is how a scan goes dark over
    everything below it, which is worse than reporting the tail twice.

    THE TERMINATOR IS EXACT, because bash's is: for an unquoted `<<TAG` the body ends only on a line
    that is the tag and nothing else, and tabs are stripped only for `<<-`. A `.strip()` here ended
    the body at an INDENTED line bash reads as body — so the scanner resumed at a fake terminator
    and graded the real body as code, missing the gated class outright. The `\\r` is the one
    tolerance the strip was actually buying: on a CRLF checkout every terminator carries one, and
    a naive column-0 match flips innocent sites into GATED hits.
    """
    body = []
    for i in range(start + 1, len(lines)):
        probe = lines[i].lstrip("\t") if dash else lines[i]
        if probe.rstrip("\r") == tag:
            return body, i
        body.append(lines[i])
    return body, -1


def scan_file(text: str) -> dict[str, list[tuple[int, str]]]:
    """Classify every heredoc, here-string and process substitution in one shell source.

    Returns `{class-key: [(1-based line, delimiter), ...]}`. A heredoc BODY is skipped once its
    terminator is known, so a fixture that writes a shell script through a heredoc is graded as the
    data it is rather than as code this repository runs.

    EVERY CLASSIFIER READS THE CODE HALF of the line and never the comment — `extract_code` says
    why. The BODY is read from `lines` untouched: a body is data, and a `#` in it is a character.

    THE ONE-HOP FOLLOW is `forked`: the names whose latest assignment above this line took its value
    from a command substitution. It is updated BEFORE the line is classified, so an opener sharing a
    line with its own feeding assignment is graded — and a heredoc BODY never reaches it, because
    the walk skips to the terminator, so a shell script written inside a fixture heredoc cannot
    seed the table of the file that carries it.
    """
    lines = text.split("\n")
    found: dict[str, list[tuple[int, str]]] = {key: [] for key, _l, _g in CLASSES}
    forked: set[str] = set()
    i = 0
    while i < len(lines):
        # A whole-line comment strips to its own indentation and matches no classifier, so the
        # skip that used to sit here is this call's tail case rather than a second predicate.
        line = extract_code(lines[i])
        for segment in line.split(";"):
            assigned = ASSIGNMENT.match(segment)
            if not assigned:
                continue
            # A re-assignment from anything else CLEARS the name. Leaving it set would credit every
            # later expansion of a common name to one long-dead substitution, which is the shape
            # that makes a widened predicate red innocent files.
            if check_substitution(assigned.group(2)):
                forked.add(assigned.group(1))
            else:
                forked.discard(assigned.group(1))
        loop = bool(DONE.search(line))
        if loop and PROCESS_SUB.search(line):
            found["procsub"].append((i + 1, "<("))
        if HERESTRING in line:
            tail = line.split(HERESTRING, 1)[1]
            if check_substitution(tail):
                found["loop-herestring-sub" if loop else "herestring-sub"].append((i + 1, HERESTRING))
            elif loop and forked.intersection(EXPANSION.findall(tail)):
                found["loop-var-sub"].append((i + 1, HERESTRING))
            i += 1
            continue
        match = HEREDOC.search(line)
        if not match:
            i += 1
            continue
        dash, quote, tag = match.group(1), match.group(2), match.group(3)
        body, end = extract_heredoc_body(lines, i, dash, tag)
        text_body = "\n".join(body)
        carries = not quote and check_substitution(text_body)
        if loop and carries:
            found["loop-heredoc-sub"].append((i + 1, tag))
        elif loop and not quote and forked.intersection(EXPANSION.findall(text_body)):
            # A QUOTED DELIMITER EXPANDS NOTHING, so `$var` in it is four characters of data and the
            # `not quote` guard is what keeps this from reading them as a feed.
            found["loop-var-sub"].append((i + 1, tag))
        elif loop:
            found["loop-heredoc-plain"].append((i + 1, tag))
        elif carries:
            found["heredoc-sub"].append((i + 1, tag))
        i = end if end > i else i + 1
    return found


def scan_tree(root: pathlib.Path) -> tuple[dict[str, list[tuple[str, int, str]]], int]:
    """Every tracked `*.sh` under `root`, classified. Returns (findings, files scanned).

    The population is DERIVED from the index, never from a list somebody maintains: a scan that
    graded a hand-kept set would go quiet on the file that arrives without being added to it.
    """
    listing = subprocess.run(
        ["git", "ls-files", "-z", "*.sh"],
        cwd=str(root), capture_output=True, text=True, encoding="utf-8",
    )
    if listing.returncode != 0:
        # A DEAD PROBE, and it must not be spelled the same way as an empty tree. Both yield
        # zero files; only one of them means "there is nothing here to grade".
        raise OSError("git ls-files failed, so the population could not be derived at all: "
                      + (listing.stderr or "").strip())
    paths = [p for p in listing.stdout.split("\0") if p]
    total: dict[str, list[tuple[str, int, str]]] = {key: [] for key, _l, _g in CLASSES}
    scanned = 0
    for rel in sorted(paths):
        full = root / rel
        if not full.is_file():
            continue
        scanned += 1
        for key, sites in scan_file(full.read_bytes().decode("utf-8", "replace")).items():
            total[key].extend((rel, line, delim) for line, delim in sites)
    return total, scanned


def build_measured(findings: dict[str, list[tuple[str, int, str]]]) -> dict[tuple[str, str], int]:
    """The failing population as `{(path, delimiter): count}` — the registry's own key."""
    measured: dict[tuple[str, str], int] = {}
    for key in GATED:
        for rel, _line, delim in findings[key]:
            measured[(rel, delim)] = measured.get((rel, delim), 0) + 1
    return measured


def read_registry(path: pathlib.Path, shape: tuple = DELIMITER_SHAPE,
                  reasons: dict | None = None) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites, plus every malformed row. A row is `path TAB delim TAB count TAB reason`.

    `shape` is the key's pattern with the two phrases a malformed key is refused in; its default is
    the loop scan's, byte-identically. `reasons`, when given, is filled with each row's reason, which
    the probe mode prints for every waived site.
    """
    pattern, label, keyname = shape
    declared: dict[tuple[str, str], int] = {}
    malformed: list[str] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        row = raw.rstrip("\r")
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        fields = row.split("\t")
        if len(fields) < 4 or not fields[3].strip():
            malformed.append(f"line {number}: not <path> TAB <delimiter> TAB <count> TAB <reason>: {row}")
            continue
        rel, delim, count = fields[0].strip(), fields[1].strip(), fields[2].strip()
        if not pattern.match(delim):
            malformed.append(
                f"line {number}: {delim!r} is not {label} — the key is the {keyname}, "
                f"never a line number, because a line number moves on an unrelated edit: {row}")
            continue
        if not count.isdigit() or int(count) < 1:
            malformed.append(f"line {number}: count {count!r} is not a positive integer: {row}")
            continue
        if (rel, delim) in declared:
            malformed.append(f"line {number}: ({rel}, {delim}) is declared twice: {row}")
            continue
        declared[(rel, delim)] = int(count)
        if reasons is not None:
            reasons[(rel, delim)] = "\t".join(fields[3:]).strip()
    return declared, malformed


def resolve_declaration(arg: str | None, shape: tuple = DELIMITER_SHAPE,
                        reasons: dict | None = None) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites for the OPTIONAL registry argument, or a refusal. Three states.

    ABSENT is the posture this scanner ships in, and it used to be the one state it refused. An
    empty declaration grades every measured site as undeclared, which is byte-identically what an
    empty registry file produces and what a first install is documented to see — so the refusal
    forbade the state the kit hands a new adopter, and did it at the leg the adopter runs first.

    SUPPLIED AND UNRESOLVABLE raises. The two must not collapse into one: a mis-spelled path that
    graded against an empty declaration would report the whole population as new and read exactly
    like an honest first install, which is a typo wearing a posture's clothes.
    """
    if arg is None:
        return {}, []
    path = pathlib.Path(arg)
    if not path.is_file():
        raise OSError(f"no registry at {path} — the argument was SUPPLIED and does not resolve to "
                      f"a file, which is a typo and not a posture; OMIT it to grade against an "
                      f"empty declaration")
    return read_registry(path, shape, reasons)


def check_registry(measured: dict[tuple[str, str], int],
                   declared: dict[tuple[str, str], int],
                   explained: dict[tuple[str, str], str] | None = None) -> list[str]:
    """Set equality in both directions, with the counts. Returns one line per violation.

    `explained` carries the undeclared-site text for a key, where the caller's class needs its own
    words; a key it does not carry gets the loop scan's.
    """
    problems = []
    for key in sorted(set(measured) | set(declared)):
        rel, delim = key
        have, want = measured.get(key), declared.get(key)
        if want is None and explained and key in explained:
            problems.append(explained[key])
        elif want is None:
            problems.append(
                f"{rel}: a loop is fed by `{delim}` holding a command substitution, and no registry "
                f"row declares it ({have} site(s)) — feed the loop from a scratch FILE instead")
        elif have is None:
            problems.append(
                f"{rel}: the registry declares `{delim}` and the scan no longer finds it — delete "
                f"the row, or a drained site leaves a widened exemption behind")
        elif have != want:
            problems.append(
                f"{rel}: the registry declares {want} site(s) at `{delim}` and the scan measures "
                f"{have} — the count may fall with the sites and may not rise")
    return problems


def print_populations(findings: dict[str, list[tuple[str, int, str]]], scanned: int) -> None:
    print(f"sh-hygiene: {scanned} tracked *.sh scanned")
    for key, label, gated in CLASSES:
        sites = findings[key]
        files = len({rel for rel, _l, _d in sites})
        mark = "GATED" if gated else "near miss"
        print(f"sh-hygiene:   [{mark}] {len(sites)} site(s) in {files} file(s) — {label}")


def check_probe_scrubbed(code: str, start: int) -> bool:
    """True when the probe at `start` is the first command of a `(` opening with the scrub."""
    return bool(SCRUBBED.search(code[:start]))


def scan_probe_file(text: str) -> dict[str, list[tuple[int, str, str]]]:
    """Classify every location probe in one shell source: `{class-key: [(line, key, remedy), ...]}`.

    Only the gated forms carry a key, and only a bare one a remedy: the line with the scrub put in,
    after the `(` the probe opens, or around the probe in a subshell of its own where none does.
    """
    found: dict[str, list[tuple[int, str, str]]] = {key: [] for key, _m, _l in PROBE_CLASSES}
    for number, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip("\r")
        code = extract_code(line)
        if PROBE_C.search(line[len(code):]) or PROBE_CD.search(line[len(code):]):
            found["comment"].append((number, "", ""))
        moved: list[tuple[int, int]] = []
        for pattern, form in ((PROBE_C, "-C"), (PROBE_CD, "cd")):
            for match in pattern.finditer(code):
                key = f"{form} {match.group(1)} --{match.group(2)}"
                moved.append(match.span())
                if check_probe_scrubbed(code, match.start()):
                    found["scrubbed"].append((number, key, ""))
                    continue
                head = code[:match.start()].rstrip()
                remedy = (head + PROBE_SCRUB + code[match.start():] if head.endswith("(") else
                          head + " (" + PROBE_SCRUB + match.group(0) + ")" + code[match.end():])
                found["bare"].append((number, key, remedy.strip()))
        found["identity"].extend((number, "", "") for _m in PROBE_IDENTITY.finditer(code))
        found["cwd"].extend((number, "", "") for match in PROBE_CWD.finditer(code)
                            if not any(start <= match.start() < end for start, end in moved))
    return found


def scan_probe_tree(root: pathlib.Path, pathspecs: list[str]
                    ) -> tuple[dict[str, list[tuple[str, int, str, str]]], int]:
    """Every tracked shell source under `root` and the pathspecs, classified. Returns (found, files).

    A shell source is a `*.sh`, or an extensionless file whose first line is a shell shebang — which
    reaches a repository's git hooks without this kit naming where it keeps them.
    """
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--", *(pathspecs or ["."])],
        cwd=str(root), capture_output=True, text=True, encoding="utf-8",
    )
    if listing.returncode != 0:
        raise OSError("git ls-files failed, so the population could not be derived at all: "
                      + (listing.stderr or "").strip())
    total: dict[str, list[tuple[str, int, str, str]]] = {key: [] for key, _m, _l in PROBE_CLASSES}
    scanned = 0
    for rel in sorted(p for p in listing.stdout.split("\0") if p):
        full = root / rel
        name = rel.rsplit("/", 1)[-1]
        if not full.is_file() or not (name.endswith(".sh") or "." not in name):
            continue
        data = full.read_bytes()
        if not name.endswith(".sh") and not SHELL_SHEBANG.match(data.split(b"\n", 1)[0]):
            continue
        scanned += 1
        for key, sites in scan_probe_file(data.decode("utf-8", "replace")).items():
            total[key].extend((rel, line, probe, remedy) for line, probe, remedy in sites)
    return total, scanned


def build_probe_measured(found: dict[str, list[tuple[str, int, str, str]]]) -> dict[tuple[str, str], int]:
    """The bare sites as `{(path, probe key): count}` — the registry's own key."""
    measured: dict[tuple[str, str], int] = {}
    for rel, _line, key, _remedy in found["bare"]:
        measured[(rel, key)] = measured.get((rel, key), 0) + 1
    return measured


def print_probe_populations(found: dict[str, list[tuple[str, int, str, str]]], scanned: int) -> None:
    print(f"sh-hygiene: location probes — {scanned} tracked shell source(s) scanned")
    for key, mark, label in PROBE_CLASSES:
        sites = found[key]
        files = len({site[0] for site in sites})
        print(f"sh-hygiene:   [{mark}] {len(sites)} site(s) in {files} file(s) — {label}")


def run_probe_scan(args: list[str]) -> int:
    """`--location-probes [registry] [root] [pathspec ...]`: 0 clean, 1 findings, 2 refusal."""
    root = pathlib.Path(args[1] if len(args) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"sh-hygiene: not a directory: {root}", file=sys.stderr)
        return 2
    reasons: dict[tuple[str, str], str] = {}
    try:
        declared, malformed = resolve_declaration(args[0] if args else None, PROBE_KEY_SHAPE, reasons)
        found, scanned = scan_probe_tree(root, args[2:])
    except OSError as exc:
        print(f"sh-hygiene: {exc}", file=sys.stderr)
        return 2
    if scanned == 0:
        print("sh-hygiene: no tracked shell source under the root and pathspecs, so this run graded "
              "NOTHING — that is a refusal and not a pass", file=sys.stderr)
        return 2
    if not args:
        print("sh-hygiene: no registry argument, so this run grades against an EMPTY declaration")
    print_probe_populations(found, scanned)
    measured = build_probe_measured(found)
    # A WAIVED SITE SAYS WHY ON EVERY RUN, green included: a reason nobody reads is no reason.
    for key in sorted(set(measured) & set(declared)):
        print(f"sh-hygiene: waived — {key[0]}: `{key[1]}` × {declared[key]} — {reasons[key]}")
    explained: dict[tuple[str, str], str] = {}
    for rel, line, key, remedy in found["bare"]:
        explained.setdefault((rel, key), f"{rel}: the location probe `{key}` is asked bare and no "
                                         f"registry row declares it — scrub each site in place:")
        explained[(rel, key)] += f"\n    {rel}:{line}: {remedy}"
    problems = malformed + check_registry(measured, declared, explained)
    if not problems:
        print(f"sh-hygiene: OK — {sum(declared.values())} declared site(s) in {len(declared)} row(s), "
              f"no undeclared location probe asked from a moved directory")
        return 0
    print(f"sh-hygiene: {len(problems)} finding(s). With GIT_DIR set and no GIT_WORK_TREE, which git "
          f"exports into a linked worktree's hooks and merge drivers, git takes the current directory "
          f"for the top of the work tree, so a probe asked from a moved directory answers about that "
          f"directory as if it were the root.")
    for problem in problems:
        print(f"  {problem}")
    return 1


def run_selftest() -> int:
    """Stage the break, confirm RED. A gate whose failing case has never been observed is not one."""
    ok = True
    n = 0

    def test(claim: str, got: object, want: object, say: bool = False) -> None:
        nonlocal ok, n
        n += 1
        if got != want:
            print(f"SELFTEST FAIL: {claim} — got {got!r}, wanted {want!r}")
            ok = False
        elif say:
            print(f"sh-hygiene selftest: ok — {claim}")

    # THE FIXTURE IS THE WORK. It carries the failing form and its nearest innocent neighbour in one
    # file, so an arm that passes by grading nothing is not available: the same run must name one
    # and not the other.
    fixture = "\n".join([
        "while IFS= read -r a; do echo $a; done <<HIT",
        "$(git log --format=%H)",
        "HIT",
        "while IFS= read -r b; do echo $b; done <<PLAIN",
        "$PLAIN_VAR is a plain expansion and forks nothing",
        "PLAIN",
        "while IFS= read -r c; do echo $c; done <<'QUOTED'",
        "$(this is literal text because the delimiter is quoted)",
        "QUOTED",
        "cat <<NOTALOOP",
        "$(git rev-parse HEAD)",
        "NOTALOOP",
        "while IFS= read -r d; do echo $d; done < <(git ls-files)",
        "while IFS= read -r e; do echo $e; done <<< \"$(git status)\"",
        "",
    ])
    seen = scan_file(fixture)
    test("the substitution-fed loop heredoc is named",
         [d for _l, d in seen["loop-heredoc-sub"]], ["HIT"])
    test("the substitution-free loop heredoc is NOT named",
         [d for _l, d in seen["loop-heredoc-plain"]], ["PLAIN", "QUOTED"])
    test("a non-loop heredoc holding a substitution is a near miss, not a hit",
         [d for _l, d in seen["heredoc-sub"]], ["NOTALOOP"])
    test("the process-substitution loop is counted, not gated",
         len(seen["procsub"]), 1)
    test("the substitution-fed here-string is named",
         [d for _l, d in seen["loop-herestring-sub"]], ["<<<"])
    test("arithmetic expansion is not a command substitution", check_substitution("$((1 + 2))"), False)
    test("a backtick is a command substitution", check_substitution("`ls`"), True)
    test("a heredoc body is skipped, so a fixture inside one is not graded twice",
         len(scan_file("cat <<OUTER\nwhile read x; do :; done <<INNER\n$(ls)\nINNER\nOUTER\n")
             ["loop-heredoc-sub"]), 0)
    test("an unterminated heredoc still reports rather than swallowing the file",
         len(scan_file("while read x; do :; done <<NEVER\n$(ls)\n")["loop-heredoc-sub"]), 1)

    # ---- the ONE-HOP FOLLOW, with its near misses in the same file ------------------------------
    # The fixture carries the hit and every innocent neighbour that shares its shape, so an arm
    # cannot pass by grading nothing: the same run must name two of these seven and not the others.
    widened = "\n".join([
        "v=$(git log --format=%H)",
        "while IFS= read -r a; do echo $a; done <<VARHIT",
        "$v",
        "VARHIT",
        "p=\"a literal\"",
        "while IFS= read -r b; do echo $b; done <<VARPLAIN",
        "$p",
        "VARPLAIN",
        "w=$(git ls-files)",
        "w=$STATIC",
        "while IFS= read -r c; do echo $c; done <<CLEARED",
        "$w",
        "CLEARED",
        "while IFS= read -r d; do echo $d; done <<'VARQUOTED'",
        "$v",
        "VARQUOTED",
        "cat <<VARNOTALOOP",
        "$v",
        "VARNOTALOOP",
        "while IFS= read -r e; do echo $e; done <<< \"$v\"",
        "two=$v",
        "while IFS= read -r f; do echo $f; done <<TWOHOP",
        "$two",
        "TWOHOP",
        "",
    ])
    widened_seen = scan_file(widened)
    test("a loop fed over a variable assigned from a substitution is named, heredoc and here-string",
         [d for _l, d in widened_seen["loop-var-sub"]], ["VARHIT", HERESTRING])
    # THE CONTROL, and it is four claims in one list: a plain value is not followed, a name
    # re-assigned from a literal is CLEARED, a quoted delimiter expands nothing, and a value two
    # hops from its substitution is a documented MISS rather than a silent one.
    test("the innocent neighbours in that same file stay near misses",
         [d for _l, d in widened_seen["loop-heredoc-plain"]], ["VARPLAIN", "CLEARED", "VARQUOTED", "TWOHOP"])
    test("a NON-loop heredoc over a forked variable is not gated — the loop is still the population",
         widened_seen["heredoc-sub"], [])
    test("an assignment sharing the opener's line still feeds it",
         [d for _l, d in scan_file("x=$(ls); while read y; do :; done <<SAME\n$x\nSAME\n")
          ["loop-var-sub"]], ["SAME"])
    test("an assignment written INSIDE a heredoc body is data and seeds nothing",
         scan_file("cat <<OUTER\nv=$(ls)\nOUTER\nwhile read x; do :; done <<INNER\n$v\nINNER\n")
         ["loop-var-sub"], [])

    # ---- the FALSE-POSITIVE half, which shipped without one --------------------------------------
    # A false-positive arm alone passes when the scanner goes dark, so each of the two below is
    # paired with a control proving the same run still names the real thing. This leg is
    # `subject = repo` with no guard and runs at the push boundary, so a red on an innocent file
    # blocks every push on the repository it is installed in.
    test("a trailing comment mentioning a heredoc is NOT an opener",
         scan_file('while read -r x; do :; done < "$f"   # used to be <<EOF\n$(git log)\n')
         ["loop-heredoc-sub"], [])
    test("the CONTROL — the same line with the comment marker gone is still a hit",
         [d for _l, d in scan_file("while read -r x; do :; done <<EOF\n$(git log)\nEOF\n")
          ["loop-heredoc-sub"]], ["EOF"])
    test("a trailing comment mentioning a here-string is NOT one",
         scan_file('while read -r x; do :; done < "$f"   # see <<<"$(x)"\n')
         ["loop-herestring-sub"], [])
    test("a `#` inside quotes is data, so the opener beside it is still graded",
         [d for _l, d in scan_file('while read -r x; do echo "# $x"; done <<EOF\n$(git log)\nEOF\n')
          ["loop-heredoc-sub"]], ["EOF"])

    # ---- the terminator is EXACT, and the CR tolerance is the only thing the old strip bought ----
    _indented = "while read -r x; do :; done <<EOF\n  EOF\n$(git log)\nEOF\n"
    test("an INDENTED line is body, not a terminator, so the gated class is still named",
         [d for _l, d in scan_file(_indented)["loop-heredoc-sub"]], ["EOF"])
    # The CR tolerance, pinned on a fixture where it CHANGES the verdict. The indented one above
    # cannot do that job: dropping the tolerance makes it unterminated, whose body is the rest of
    # the file, which is a hit either way — an arm that agrees with itself for the wrong reason.
    # Here the body is clean and the substitution sits BELOW the terminator, so a terminator missed
    # over one CR swallows the code under it and turns an innocent site into a GATED hit. That is
    # measured, not hypothetical: three live sites in one tracked script of the kit's home repo
    # flip from a near miss to a GATED hit on a CRLF checkout when the tolerance is dropped. The
    # file is not named here — a kit body naming a path outside itself is banned, and the ban is
    # what the sibling `install-prefix` arm enforces.
    _crlf = "while read -r x; do :; done <<EOF\nplain body, no fork\nEOF\ny=$(git log)\n"
    test("a CRLF terminator still ENDS the body, so the code under it is not swallowed",
         scan_file(_crlf.replace("\n", "\r\n")), scan_file(_crlf))

    # ---- the registry, in both directions and on both malformed shapes -------------------------
    measured = {("a.sh", "HIT"): 1}
    test("an undeclared measured site fails", len(check_registry(measured, {})), 1)
    test("a declared measured site passes",
         check_registry(measured, {("a.sh", "HIT"): 1}), [])
    test("a stale row fails", len(check_registry({}, {("a.sh", "GONE"): 1})), 1)
    test("a count that no longer matches fails",
         len(check_registry(measured, {("a.sh", "HIT"): 2})), 1)
    with tempfile.TemporaryDirectory() as scratch:
        reg = pathlib.Path(scratch) / "reg.txt"
        reg.write_text("# a comment\na.sh\tHIT\t1\tpredates the gate\n", encoding="utf-8")
        rows, bad = read_registry(reg)
        test("a well-formed row parses", rows, {("a.sh", "HIT"): 1})
        test("a well-formed row is not malformed", bad, [])
        reg.write_text("a.sh\t153\t1\tkeyed on a line number\n", encoding="utf-8")
        _rows, bad = read_registry(reg)
        test("a line-numbered key is refused as malformed", len(bad), 1)
        reg.write_text("a.sh\tHIT\t1\n", encoding="utf-8")
        _rows, bad = read_registry(reg)
        test("a row with no reason is refused as malformed", len(bad), 1)
        reg.write_text("a.sh\tHIT\tzero\twhy\n", encoding="utf-8")
        _rows, bad = read_registry(reg)
        test("a non-numeric count is refused as malformed", len(bad), 1)

        # ---- the OPTIONAL argument, in all three of its states ---------------------------------
        # Asserted here rather than through a run, because a tree scan cannot tell the absent case
        # from the empty-file case — they produce the same declaration, which is the whole claim.
        test("an absent argument resolves to an empty declaration, not a refusal",
             resolve_declaration(None), ({}, []))
        reg.write_text("a.sh\tHIT\t1\tpredates the gate\n", encoding="utf-8")
        test("an argument naming a file is read through the same parser",
             resolve_declaration(str(reg)), ({("a.sh", "HIT"): 1}, []))
        try:
            resolve_declaration(str(pathlib.Path(scratch) / "nosuch.txt"))
            refusal = "resolved"
        except OSError as exc:
            refusal = "named" if "nosuch.txt" in str(exc) else f"refused without naming it: {exc}"
        test("an argument that was supplied and does not resolve refuses, naming the path",
             refusal, "named")

    # ---- the LOCATION-PROBE class: every row of the unit's fixture table, each with its verdict ----
    # One line per case, and each case must land in EXACTLY one class, so an arm cannot pass by
    # grading nothing: the gated forms, both scrubs, the three spellings the scrub check refuses on
    # purpose, and one of each near miss share this one run.
    probe_cases = [
        ('x=$(git -C "$d" rev-parse --show-prefix)', "bare"),
        ('x=$(GIT -C "$d" rev-parse --show-toplevel)', "bare"),
        ('x=$(git -C "$(dirname -- "$0")" rev-parse --show-prefix)', "bare"),
        ('x=$(git -c a.b=c -C "$d" rev-parse --path-format=absolute --show-toplevel)', "bare"),
        ('x=$(cd "$d" && git rev-parse --show-prefix)', "bare"),
        ('x=$(unset GIT_DIR GIT_WORK_TREE; git -C "$d" rev-parse --show-toplevel)', "scrubbed"),
        ('x=$(unset GIT_DIR GIT_WORK_TREE; cd "$d" && git rev-parse --show-prefix)', "scrubbed"),
        ('unset GIT_DIR GIT_WORK_TREE; x=$(git -C "$d" rev-parse --show-prefix)', "bare"),
        ('x=$(unset GIT_WORK_TREE GIT_DIR; git -C "$d" rev-parse --show-prefix)', "bare"),
        ('# x=$(git -C "$d" rev-parse --show-prefix)', "comment"),
        ('x=$(git -C "$d" rev-parse --git-common-dir)', "identity"),
        ("top=$(git rev-parse --show-toplevel)", "cwd"),
    ]
    for case, want in probe_cases:
        verdict = [key for key, sites in scan_probe_file(case + "\n").items() if sites]
        test(f"probe [{want}] {case}", verdict, [want], say=True)
    quoted = scan_probe_file(probe_cases[2][0])["bare"]
    test("the quoted-substitution operand is ONE word, so the key is the probe as written",
         [key for _l, key, _r in quoted], ['-C "$(dirname -- "$0")" --show-prefix'], say=True)
    test("the remedy a bare site prints is itself graded scrubbed, top-level unset included",
         [[key for key, sites in scan_probe_file(remedy).items() if sites]
          for case, _w in probe_cases[7:9] for _l, _k, remedy in scan_probe_file(case)["bare"]],
         [["scrubbed"], ["scrubbed"]], say=True)

    # ---- the population, the registry and the refusals, over a real repository ---------------------
    # A git hook exports GIT_DIR, and this block runs git in a scratch repository, so the three
    # variables are held out of the environment for its length and put back after.
    held = {name: os.environ.pop(name) for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")
            if name in os.environ}
    try:
        with tempfile.TemporaryDirectory() as scratch:
            tree = pathlib.Path(scratch)
            probe = probe_cases[0][0] + "\n"
            files = {"a.sh": probe, "hook": "#!/usr/bin/env bash\n" + probe,
                     "tool": "#!/usr/bin/env python3\n" + probe, "b.test.sh": probe}
            for rel, body in files.items():
                (tree / rel).write_bytes(body.encode("utf-8"))
            for argv in (["git", "init", "-q", "."], ["git", "add", "-A"]):
                subprocess.run(argv, cwd=str(tree), capture_output=True, check=True)
            found, scanned = scan_probe_tree(tree, [":!*.test.sh"])
            test("a bash-shebang extensionless file is scanned, a python one and an excluded suite are not",
                 sorted({site[0] for site in found["bare"]}), ["a.sh", "hook"], say=True)
            found, scanned = scan_probe_tree(tree, [])
            test("the CONTROL — without the exclusion the suite is scanned too",
                 sorted({site[0] for site in found["bare"]}), ["a.sh", "b.test.sh", "hook"], say=True)
            reg = tree / "reg.txt"
            key = '-C "$d" --show-prefix'
            outcomes = []
            for rows in (f"a.sh\t{key}\t1\tread by no hook\nhook\t{key}\t1\tthe hook's own\n",
                         f"a.sh\t{key}\t1\tread by no hook\nhook\t{key}\t1\tthe hook's own\n"
                         f"gone.sh\t{key}\t1\ta drained site\n",
                         f"a.sh\t{key}\t2\tread by no hook\nhook\t{key}\t1\tthe hook's own\n",
                         f"a.sh\t153\t1\tkeyed on a line\nhook\t{key}\t1\tthe hook's own\n"):
                reg.write_text(rows, encoding="utf-8")
                said = io.StringIO()
                with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
                    code = run_probe_scan([str(reg), str(tree), ":!*.test.sh"])
                outcomes.append((code, said.getvalue()))
            test("a registry row for each bare site is green", outcomes[0][0], 0, say=True)
            test("and a waived site prints its reason on that green run",
                 "read by no hook" in outcomes[0][1], True, say=True)
            test("a row whose site is gone is a finding", (outcomes[1][0], "no longer finds" in outcomes[1][1]),
                 (1, True), say=True)
            test("a count that disagrees is a finding", (outcomes[2][0], "the scan measures" in outcomes[2][1]),
                 (1, True), say=True)
            test("a line-number key is a finding", (outcomes[3][0], "never a line number" in outcomes[3][1]),
                 (1, True), say=True)
            refusals = []
            for argv in ([str(reg), str(tree), "nosuch/"], [str(tree / "nosuch.txt"), str(tree)]):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    refusals.append(run_probe_scan(argv))
            test("an empty population and an unresolvable registry each refuse with 2", refusals, [2, 2],
                 say=True)
            (tree / ".git").rename(tree / "not-git")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                refusals = [run_probe_scan([str(reg), str(tree)])]
            test("a root that is no repository refuses with 2 rather than grading nothing", refusals, [2],
                 say=True)
    finally:
        os.environ.update(held)

    if n < FLOOR_ASSERTIONS:
        print(f"SELFTEST FAIL: {n} assertion(s) executed, under the floor of {FLOOR_ASSERTIONS} — an arm is stranded past an early exit, which is the one defect a printed count can see and a per-arm check cannot")
        ok = False
    print(f"PASS ({n} assertions)" if ok else f"sh-hygiene selftest: RED ({n} assertions)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return run_selftest()
    if "--location-probes" in argv:
        return run_probe_scan([arg for arg in argv[1:] if arg != "--location-probes"])
    args = argv[1:]
    root = pathlib.Path(args[1] if len(args) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"sh-hygiene: not a directory: {root}", file=sys.stderr)
        return 2
    try:
        declared, malformed = resolve_declaration(args[0] if args else None)
    except OSError as exc:
        print(f"sh-hygiene: {exc}", file=sys.stderr)
        return 2
    try:
        findings, scanned = scan_tree(root)
    except OSError as exc:
        print(f"sh-hygiene: {exc}", file=sys.stderr)
        return 2
    # AN EMPTY POPULATION IS A REFUSAL. A scan that graded nothing reports the same zero a clean
    # tree does, and the two are indistinguishable from outside.
    if scanned == 0:
        print("sh-hygiene: no tracked *.sh under the root, so this run graded NOTHING — that is a "
              "refusal and not a pass", file=sys.stderr)
        return 2
    print_populations(findings, scanned)
    problems = malformed + check_registry(build_measured(findings), declared)
    if not problems:
        # SITES, not ROWS, and the two are different numbers: a row keys on (file, delimiter)
        # and carries a COUNT, so one row can cover several sites. Printing the row count
        # beside a hit line that counts sites made one run report one population two ways.
        print(f"sh-hygiene: OK — {sum(declared.values())} declared site(s) in "
              f"{len(declared)} row(s), no undeclared loop fed by a command substitution")
        return 0
    print(f"sh-hygiene: {len(problems)} finding(s). A `while … done` fed by a heredoc or here-string "
          f"whose body holds a command substitution reads until EOF, and EOF can never arrive.")
    for problem in problems:
        print(f"  {problem}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
