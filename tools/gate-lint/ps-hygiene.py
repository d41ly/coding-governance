#!/usr/bin/env python3
"""PowerShell source-hygiene scans — two classes that make a script misbehave SILENTLY.

Project-agnostic. Run over any repo: `python <prefix>/gate-lint/ps-hygiene.py [root]`.
Exit 0 clean, 1 on findings, 2 on a refusal: a usage error, a `git ls-files` that failed, or no
tracked .ps1 at all. `--selftest` proves both scans, and the tracked population, can FAIL.

CLASS 1 — case-only identifier collisions. PowerShell variable names are case-INSENSITIVE, so
`$LEGS` and `$legs` are ONE variable. Upstream this bit the same file three times: `$LEGS =
@($legs.legs)` overwrote a parsed manifest with its own sub-array, and a `foreach ($sel in ...)`
clobbered a `$SEL` selection map — which also disabled the backstop that read `$SEL`, because a
guard sharing a variable with the thing it guards is not a guard.

CLASS 1 IS SCOPE-AWARE. PowerShell functions get their own scope: a parameter, and any name a
function body ASSIGNS, is function-local and cannot alias a script-level name. Comparing the two
in one flat namespace reported `function Recon($fa,$rid)` against a script-level `$FA` as a
collision — a name that PowerShell never merges, so the "finding" was unactionable and the only
remedy was to rename correct code. Collisions are therefore computed PER SCOPE: script level with
every function unit lifted out, then each function unit (its parameter list plus its body)
separately, recursively for nested functions. A name that a function only READS still resolves to
the script-level variable, but reading is not the clobber this class is about — the shape that bit
upstream was always an ASSIGNMENT, and an assignment inside a function is local by construction.
Brace matching runs on comment-stripped source; on unbalanced braces the scan falls back to
treating the remainder as one scope, preserving the pre-scope behaviour rather than losing text.

CLASS 2 — a BOM-less script containing non-ASCII. PowerShell 5.1 decodes it as CP1252, so an em
dash (E2 80 94) inside a double-quoted string becomes three chars ending in 0x94 = U+201D, which
PowerShell accepts as a STRING DELIMITER. It closes the string early and desynchronises the parser.
Every text-mode read hides this, so the check is byte-level.

Scans EVERY TRACKED .ps1 in the tree, not one file: gating a single instance while claiming the
class is itself the could-not-fail shape these scans exist to catch. TRACKED, not walked: the
question is about the commit, and a walk from the root also reads every untracked checkout parked
inside the tree, which is where some adopters keep their linked worktrees. No tracked .ps1 at all
is a refusal, because a dead `git ls-files` and an empty tree both yield zero files.

The listing takes no pathspec and filters the suffix case-insensitively. A pathspec glob is
case-sensitive even under `core.ignorecase`, so `*.ps1` dropped a tracked `Deploy.PS1` that the walk
it replaced had graded on Windows — a population narrower than the walk, certified clean.
"""
from __future__ import annotations

import collections
import contextlib
import io
import os
import pathlib
import re
import subprocess
import sys
import tempfile

_COMMENT = re.compile(r"^\s*#")
_BLOCK = re.compile(r"<#.*?#>", re.S)
_IDENT = re.compile(r"\$([A-Za-z_][A-Za-z0-9_]*)")
# `function Name` / `filter Name` — the scope-opening keywords. Hyphens are legal in PS verb-noun
# names (`Get-Thing`), and the lookbehind keeps `New-Function` from matching as a definition.
_FUNC_KW = re.compile(r"(?i)(?<![\w-])(?:function|filter)[ \t]+[A-Za-z_][\w-]*")


def _code(text: str) -> str:
    """Source with comments stripped — a collision in prose is not a collision.

    Strips block comments, whole-line comments AND trailing inline comments. The first cut kept
    trailing comments, so `$Foo = 1  # see $foo` reported a collision that does not exist. Naive on
    a `#` inside a string literal, which over-strips rather than over-reports — the safe direction
    for a gate: a missed collision surfaces on the next run, a false one blocks an innocent commit.
    """
    out = []
    for line in _BLOCK.sub("", text).splitlines():
        if _COMMENT.match(line):
            continue
        out.append(line.split("#", 1)[0] if "#" in line else line)
    return chr(10).join(out)


def _close_brace(code: str, open_at: int) -> int:
    """Index of the `}` matching the `{` at open_at, or -1 if the source is unbalanced."""
    depth = 0
    for i in range(open_at, len(code)):
        if code[i] == "{":
            depth += 1
        elif code[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return -1


def _scopes(code: str) -> list[str]:
    """Split comment-stripped source into [script level, *function scopes], recursively.

    Each function contributes ONE scope holding its parameter list and its body, and is removed
    from its parent's text — that is what stops a function parameter from being compared against a
    script-level name PowerShell would never merge with it. Unbalanced or unterminated definitions
    fall back to leaving the remaining text in the enclosing scope (over-group, never drop).
    """
    own: list[str] = []
    nested: list[str] = []
    i = 0
    while True:
        match = _FUNC_KW.search(code, i)
        if not match:
            own.append(code[i:])
            break
        body_open = code.find("{", match.end())
        if body_open < 0:
            own.append(code[i:])
            break
        body_close = _close_brace(code, body_open)
        if body_close < 0:
            own.append(code[i:])
            break
        own.append(code[i:match.start()])
        # The function's own scope: the parenthesised parameter list (if any) + the body. Dropping
        # the `function <Name>` keyword itself is what makes the recursion terminate.
        nested.extend(_scopes(code[match.end():body_open] + chr(10) + code[body_open + 1:body_close]))
        i = body_close + 1
    return ["".join(own)] + nested


def case_collisions(text: str) -> dict[str, list[str]]:
    collisions: dict[str, list[str]] = {}
    for scope in _scopes(_code(text)):
        seen: dict[str, set[str]] = collections.defaultdict(set)
        for ident in _IDENT.findall(scope):
            seen[ident.lower()].add(ident)
        for key, names in seen.items():
            if len(names) > 1:
                collisions.setdefault(key, sorted(names))
    return collisions


def missing_bom(raw: bytes) -> bool:
    return any(b > 127 for b in raw) and not raw.startswith(b"\xef\xbb\xbf")


def scan(root: pathlib.Path) -> tuple[list[str], int]:
    """Every tracked .ps1 under root, graded. Returns (findings, files scanned).

    A failed `git ls-files` raises rather than returning nothing: it is a dead probe, and spelling it
    the same way as an empty tree would grade nothing and pass. The set drops the repeat entries an
    unmerged path gets, one per stage. A listed path absent from disk (an unstaged deletion, a
    skip-worktree entry) is skipped and not counted.
    """
    listing = subprocess.run(["git", "ls-files", "-z"], cwd=str(root),
                             capture_output=True, text=True, encoding="utf-8")
    if listing.returncode != 0:
        raise OSError("git ls-files failed, so the population could not be derived at all: "
                      + (listing.stderr or "").strip())
    findings: list[str] = []
    scanned = 0
    for rel in sorted({p for p in listing.stdout.split("\0") if p.lower().endswith(".ps1")}):
        path = root / rel
        if not path.is_file():
            continue
        scanned += 1
        raw = path.read_bytes()
        if missing_bom(raw):
            findings.append(f"{rel}: non-ASCII with no UTF-8 BOM — PS 5.1 will read it as CP1252")
        for _, names in sorted(case_collisions(raw.decode("utf-8-sig", "replace")).items()):
            findings.append(f"{rel}: identifiers differ only by case, PowerShell sees ONE: {names}")
    return findings, scanned


def _selftest() -> int:
    """Stage the break, confirm RED. A gate whose failing case has never been observed is not a gate."""
    ok = True
    bad_case = '$Foo = 1\n$foo = 2\n'
    if not case_collisions(bad_case):
        print("SELFTEST FAIL: collision scan missed $Foo/$foo"); ok = False
    if case_collisions('$Foo = 1\n$Bar = 2\n'):
        print("SELFTEST FAIL: collision scan fired on clean source"); ok = False
    if case_collisions('# $Foo and $foo in a comment\n$Bar = 1\n'):
        print("SELFTEST FAIL: collision scan fired on comment prose"); ok = False
    # --- scope model: both directions, or the split is not a gate -------------------------------
    if case_collisions('$FA = 1\nfunction Recon($fa, $rid) { $fa.x }\n'):
        print("SELFTEST FAIL: collision scan fired on a function PARAM shadowing a script name"); ok = False
    if not case_collisions('function F($foo) { $Foo = 2 }\n'):
        print("SELFTEST FAIL: collision scan missed a collision INSIDE one function scope"); ok = False
    if not case_collisions('$Bar = 1\nfunction F($x) { $x }\n$bar = 2\n'):
        print("SELFTEST FAIL: lifting a function out lost script-level text"); ok = False
    if not case_collisions('function Outer($a) { function Inner($b) { $B = 1 } }\n'):
        print("SELFTEST FAIL: collision scan missed a collision in a NESTED function"); ok = False
    if case_collisions('function Outer($q) { function Inner($r) { $r } }\n'):
        print("SELFTEST FAIL: collision scan fired across two sibling nested scopes"); ok = False
    # Unbalanced braces must degrade to the flat pre-scope behaviour, never drop text.
    if not case_collisions('$Zed = 1\nfunction Broken($x) { if ($x) {\n$zed = 2\n'):
        print("SELFTEST FAIL: unbalanced braces dropped text instead of falling back"); ok = False
    if not missing_bom("Write-Host 'em dash —'".encode("utf-8")):
        print("SELFTEST FAIL: BOM scan missed a BOM-less non-ASCII file"); ok = False
    if missing_bom(b"\xef\xbb\xbf" + "Write-Host '—'".encode("utf-8")):
        print("SELFTEST FAIL: BOM scan fired on a file that has a BOM"); ok = False
    if missing_bom(b"Write-Host 'plain ascii'"):
        print("SELFTEST FAIL: BOM scan fired on pure ASCII"); ok = False
    # --- the population: TRACKED files, over a real scratch repository -------------------------
    # A git hook exports GIT_DIR, and this block runs git in a scratch repository, so the three are
    # held out of the environment for its length. The ceiling stops the not-a-repo arm from finding a
    # repository above the scratch directory, which would answer it with an empty listing instead.
    held = {name: os.environ.pop(name) for name in
            ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_CEILING_DIRECTORIES") if name in os.environ}
    bad = "Write-Host 'em dash —'\n".encode("utf-8")
    # `-f` because a node may ignore `.claude/` globally, and the autocrlf pair because a node's
    # safecrlf can refuse to stage an LF file: either would leave the control arm's fixture unstaged.
    git = ["git", "-c", "core.autocrlf=false", "-c", "core.safecrlf=false"]
    try:
        with tempfile.TemporaryDirectory() as scratch:
            base = pathlib.Path(scratch).resolve()
            os.environ["GIT_CEILING_DIRECTORIES"] = str(base)
            tree = base / "repo"
            nested = tree / ".claude" / "worktrees" / "x"
            nested.mkdir(parents=True)
            (tree / "a.ps1").write_bytes(bad)

            def run_quiet() -> tuple[int, str]:
                said = io.StringIO()
                with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
                    code = main(["ps-hygiene", str(tree)])
                return code, said.getvalue()

            # Each refusal is asserted by its REASON, not only its exit: both reasons exit 2.
            try:
                scan(tree)
                print("SELFTEST FAIL: a directory that is no repository did not raise"); ok = False
            except OSError:
                code, said = run_quiet()
                if code != 2 or "git ls-files failed" not in said or "graded NOTHING" in said:
                    print("SELFTEST FAIL: a directory that is no repository did not refuse with 2, "
                          "naming the dead listing"); ok = False
            subprocess.run(git + ["init", "-q", "."], cwd=str(tree), capture_output=True, check=True)
            # The one tracked .ps1 is then deleted from disk: listed, absent, and so not counted.
            (tree / "b.ps1").write_bytes(b"Write-Host 'plain ascii'\n")
            subprocess.run(git + ["add", "--", "b.ps1"], cwd=str(tree), capture_output=True, check=True)
            (tree / "b.ps1").unlink()
            code, said = run_quiet()
            if scan(tree)[1] != 0 or code != 2 or "graded NOTHING" not in said:
                print("SELFTEST FAIL: a repository whose one tracked .ps1 is gone from disk, beside an "
                      "untracked one, did not refuse as empty"); ok = False
            (tree / "a.ps1").write_bytes(b"Write-Host 'plain ascii'\n")
            (nested / "a.ps1").write_bytes(bad)
            subprocess.run(git + ["add", "--", "a.ps1"], cwd=str(tree), capture_output=True, check=True)
            code, said = run_quiet()
            if (code, scan(tree)[1]) != (0, 1) or "OK — 1 tracked .ps1 file(s)" not in said:
                print("SELFTEST FAIL: an untracked copy under .claude/worktrees/ was graded"); ok = False
            # The CONTROL: the same bytes, staged, red. Without it the arm above could pass on a
            # fixture that no scan would ever flag.
            subprocess.run(git + ["add", "-f", "--", ".claude/worktrees/x/a.ps1"], cwd=str(tree),
                           capture_output=True, check=True)
            code, said = run_quiet()
            if code != 1 or ".claude/worktrees/x/a.ps1: non-ASCII with no UTF-8 BOM" not in said:
                print("SELFTEST FAIL: the same copy, once tracked, did not red"); ok = False
            # An upper-case suffix under a non-ASCII name: a case-sensitive `*.ps1` pathspec drops it,
            # and a listing without -z quotes the name so it is no file. The walk graded it.
            (tree / "sub").mkdir()
            (tree / "sub" / "ü.PS1").write_bytes(bad)
            subprocess.run(git + ["add", "-f", "--", "sub/ü.PS1"], cwd=str(tree), capture_output=True,
                           check=True)
            code, said = run_quiet()
            if code != 1 or "sub/ü.PS1: non-ASCII with no UTF-8 BOM" not in said:
                print("SELFTEST FAIL: a tracked sub/ü.PS1 was not graded"); ok = False
    finally:
        os.environ.pop("GIT_CEILING_DIRECTORIES", None)
        os.environ.update(held)
    print("selftest: both scans and the tracked population observed failing and passing" if ok
          else "selftest: RED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return _selftest()
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"ps-hygiene: not a directory: {root}", file=sys.stderr)
        return 2
    try:
        findings, scanned = scan(root)
    except (OSError, ValueError) as exc:  # ValueError: a listing git wrote in no UTF-8 is a dead probe too
        print(f"ps-hygiene: {exc}", file=sys.stderr)
        return 2
    if scanned == 0:
        print(f"ps-hygiene: no tracked .ps1 under {root}, so this run graded NOTHING — that is a "
              f"refusal and not a pass", file=sys.stderr)
        return 2
    if not findings:
        print(f"ps-hygiene: OK — {scanned} tracked .ps1 file(s) clean under {root}")
        return 0
    print(f"ps-hygiene: {len(findings)} finding(s) across {scanned} tracked .ps1 file(s) under {root}")
    for f in findings:
        print(f"  {f}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
