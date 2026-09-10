#!/usr/bin/env python3
"""Shell source-hygiene scan — a loop reader fed by a command substitution, which can block forever.

Project-agnostic. Run over any repo:

    python <this file> <registry-path> [root]     # scan; exit 0 clean, 1 on an undeclared site
    python <this file> --selftest                 # prove the predicate in BOTH directions

THE CLASS. `while read … done <<TAG` with `$(cmd)` in the heredoc body, or `done <<< "$(cmd)"`.
The substitution reads until EOF, and EOF arrives when the LAST inherited write end of its pipe
closes — not when the direct child exits. Where the substituted command is a shell FUNCTION the
substitution forks a subshell which forks the real program, so the reader depends on a grandchild's
write end; under MSYS that is not reliably the one that closes. Measured in this repository on
2026-09-10: a merge-bar leg sat at zero CPU for 63 minutes with the forked subshell holding both
ends of its own pipe and no descendant alive. The remedy is a file — redirect the walk to a scratch
file and read the file — which keeps the loop in the current shell, so a `return` inside it still
returns from the enclosing function.

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

THE REGISTRY is a shrink-only declaration of the sites that predate the gate, one row per
`<path>\t<delimiter>\t<count>\t<reason>`, keyed on the delimiter and NEVER on a line number — a
line-keyed registry reds on unrelated edits, and a gate whose steady state is red gets bypassed.
Set equality in both directions: a measured site with no row fails, and a row the scan no longer
finds fails, so draining a site forces its row out instead of leaving a widened exemption behind.
"""
from __future__ import annotations

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

# The taxonomy, in report order. The first two are the failing population; the rest are printed so
# the reader can tell "no hits" from "nothing was looked at", and so the process-substitution count
# is never mistaken for coverage.
CLASSES = [
    ("loop-heredoc-sub", "loop fed by a heredoc holding a command substitution", True),
    ("loop-herestring-sub", "loop fed by a here-string holding a command substitution", True),
    ("loop-heredoc-plain", "loop fed by a heredoc with NO command substitution", False),
    ("heredoc-sub", "non-loop heredoc holding a command substitution", False),
    ("herestring-sub", "non-loop here-string holding a command substitution", False),
    ("procsub", "loop fed by a process substitution, `done < <(...)` — REPORTED, NOT GATED", False),
]
GATED = [key for key, _label, gated in CLASSES if gated]

#: The executed-assertion floor for `--selftest`, compared against the count it prints.
#: A printed count nothing reads is the same nothing as no count: this repository has shipped
#: nine arms stranded past an unconditional exit while the suite printed a total and every
#: other gate held. Raise it with the arms; it may never be lowered to fit a regression.
FLOOR_ASSERTIONS = 18


def check_substitution(text: str) -> bool:
    """True when the text holds a command substitution rather than a plain expansion."""
    return bool(SUBSTITUTION.search(text))


def extract_heredoc_body(lines: list[str], start: int, dash: str, tag: str) -> tuple[list[str], int]:
    """The body after line `start`, and the index of its terminator (or -1 when unterminated).

    An unterminated heredoc returns the rest of the file and -1. The caller must then NOT skip
    ahead: swallowing the remainder of a file on one malformed tag is how a scan goes dark over
    everything below it, which is worse than reporting the tail twice.
    """
    body = []
    for i in range(start + 1, len(lines)):
        probe = lines[i].lstrip("\t") if dash else lines[i]
        if probe.strip() == tag:
            return body, i
        body.append(lines[i])
    return body, -1


def scan_file(text: str) -> dict[str, list[tuple[int, str]]]:
    """Classify every heredoc, here-string and process substitution in one shell source.

    Returns `{class-key: [(1-based line, delimiter), ...]}`. A heredoc BODY is skipped once its
    terminator is known, so a fixture that writes a shell script through a heredoc is graded as the
    data it is rather than as code this repository runs.
    """
    lines = text.split("\n")
    found: dict[str, list[tuple[int, str]]] = {key: [] for key, _l, _g in CLASSES}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("#"):
            i += 1
            continue
        loop = bool(DONE.search(line))
        if loop and PROCESS_SUB.search(line):
            found["procsub"].append((i + 1, "<("))
        if HERESTRING in line:
            if check_substitution(line.split(HERESTRING, 1)[1]):
                found["loop-herestring-sub" if loop else "herestring-sub"].append((i + 1, HERESTRING))
            i += 1
            continue
        match = HEREDOC.search(line)
        if not match:
            i += 1
            continue
        dash, quote, tag = match.group(1), match.group(2), match.group(3)
        body, end = extract_heredoc_body(lines, i, dash, tag)
        carries = not quote and check_substitution("\n".join(body))
        if loop:
            found["loop-heredoc-sub" if carries else "loop-heredoc-plain"].append((i + 1, tag))
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
        cwd=str(root), capture_output=True, text=True,
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


def read_registry(path: pathlib.Path) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites, plus every malformed row. A row is `path TAB delim TAB count TAB reason`."""
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
        if not DELIMITER.match(delim):
            malformed.append(
                f"line {number}: {delim!r} is not a heredoc tag or `<<<` — the key is the DELIMITER, "
                f"never a line number, because a line number moves on an unrelated edit: {row}")
            continue
        if not count.isdigit() or int(count) < 1:
            malformed.append(f"line {number}: count {count!r} is not a positive integer: {row}")
            continue
        if (rel, delim) in declared:
            malformed.append(f"line {number}: ({rel}, {delim}) is declared twice: {row}")
            continue
        declared[(rel, delim)] = int(count)
    return declared, malformed


def check_registry(measured: dict[tuple[str, str], int],
                   declared: dict[tuple[str, str], int]) -> list[str]:
    """Set equality in both directions, with the counts. Returns one line per violation."""
    problems = []
    for key in sorted(set(measured) | set(declared)):
        rel, delim = key
        have, want = measured.get(key), declared.get(key)
        if want is None:
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


def run_selftest() -> int:
    """Stage the break, confirm RED. A gate whose failing case has never been observed is not one."""
    ok = True
    n = 0

    def test(claim: str, got: object, want: object) -> None:
        nonlocal ok, n
        n += 1
        if got != want:
            print(f"SELFTEST FAIL: {claim} — got {got!r}, wanted {want!r}")
            ok = False

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

    if n < FLOOR_ASSERTIONS:
        print(f"SELFTEST FAIL: {n} assertion(s) executed, under the floor of {FLOOR_ASSERTIONS} — an arm is stranded past an early exit, which is the one defect a printed count can see and a per-arm check cannot")
        ok = False
    print(f"PASS ({n} assertions)" if ok else f"sh-hygiene selftest: RED ({n} assertions)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return run_selftest()
    if len(argv) < 2:
        print("usage: sh_hygiene <registry-path> [root] | sh_hygiene --selftest", file=sys.stderr)
        return 2
    registry = pathlib.Path(argv[1])
    root = pathlib.Path(argv[2] if len(argv) > 2 else ".").resolve()
    if not root.is_dir():
        print(f"sh-hygiene: not a directory: {root}", file=sys.stderr)
        return 2
    if not registry.is_file():
        print(f"sh-hygiene: no registry at {registry} — a scan with no declaration to compare "
              f"would report the whole population as new, or nothing at all", file=sys.stderr)
        return 2
    try:
        declared, malformed = read_registry(registry)
    except OSError as exc:
        print(f"sh-hygiene: the registry is unreadable, which is a refusal: {exc}", file=sys.stderr)
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
        print(f"sh-hygiene: OK — {len(declared)} declared site(s), no undeclared loop fed by a "
              f"command substitution")
        return 0
    print(f"sh-hygiene: {len(problems)} finding(s). A `while … done` fed by a heredoc or here-string "
          f"whose body holds a command substitution reads until EOF, and EOF can never arrive.")
    for problem in problems:
        print(f"  {problem}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
