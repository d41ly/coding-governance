#!/usr/bin/env python3
"""check-arms.py — the harness meta-gate: every `fail` BRANCH is armed, or explicitly pinned.

    python <prefix>/memory-tree/check-arms.py --check        # the gate
    python <prefix>/memory-tree/check-arms.py --report       # what is armed, what is pinned, per gate
    python <prefix>/memory-tree/check-arms.py --emit-pin     # the pin file for the CURRENT unarmed set
    python <kit>/check-arms.py --emit-floors              # the ARMS_FLOORS line for the CURRENT census
    python <prefix>/memory-tree/check-arms.py --selftest

THE POPULATION IS DISCOVERED, never named. A gate is a tracked `*.sh` that DEFINES the helper
(`fail() {`) and has `fail <n> "` call sites; its test is the sibling `<stem>.test.sh`. A named pair
went stale the day a second gate landed — `manifest-check.sh` carried 16 branches behind six numbers
with no arm requirement at all — and that is the row this file drains.

WHY THE HELPER DEFINITION IS PART OF THE PREDICATE. With a call-site test alone, any `*.test.sh` that
QUOTES a fail line becomes a "gate" demanding a `<stem>.test.test.sh` that will never exist, and the
whole suite goes permanently red. `*.test.sh` is excluded outright as well: the fixture shape is one
heredoc away, and this module's own selftest already writes one.

WHY THE KEY CARRIES THE GATE. Not because one gate's arm could silence another's — it could not, the
arm scan reads each gate's own sibling test. Because the PIN's keys are global, and every discovered
gate numbers its checks from 1, so the same (number, ordinal) pair is claimed by several gates at
once — a two-field pin row raises false stale-signature reds against the other gate, or falsely
EXEMPTS it. The overlap COUNT is deliberately not written here: it moves with every gate that lands,
and the copy of it that used to sit in this docstring outlived the four-gate population by two.

WHY THE CAPTURE STOPS AT THE CLOSING QUOTE. `manifest-check.sh` writes five branches inline as
`{ fail 2 "…"; BLOCK_OK=0; }`. Capturing to end of line puts `"; BLOCK_OK=0; }` into the signature —
the gate's SOURCE, which no assertion can ever emit — so those rows would be permanently unarmable
inside a shrink-only pin, and `--check` would still pass because it compares the pin against a
signature from the same extractor. Measured: terminating at the first UNESCAPED closing quote changes
0 of 14 signatures in `check-memory-hygiene.sh` and exactly the 5 contaminated ones. A message with
no closing quote on its line is a run-on; it falls back to end-of-line.

WHAT COUNTS AS AN ARM. A POSITIVE assertion naming the branch's OWN failure text. A bare `check N`
mention, an ABSENCE assertion and a COMMENT all fail to arm: each is "something in the file mentions
it", which is not "something exercises it".

WHERE ARMS AND PINS ARE READ (TOOL-aRepatriatedFork-18). Arms come from `<stem>.test.sh` AND, when
it exists, `<stem>.local.test.sh`: a kit ships the first with its gate, so an adopter that forks the
gate arms its OWN branches in the second and the shipped suite stays gov's bytes. Pins come from
`<MEMORY_ROOT>/project/unarmed-branches.txt` AND every tracked `unarmed-branches.txt` elsewhere, a
SIDECAR whose gate column is relative to its own directory, so gov's pins for a shipped gate travel
with it at any prefix. A branch pinned in two files is refused. `--report` names the file that armed
or pinned each branch.

FLOORS ARE PER-GATE. An aggregate total lets one gate's DELETED guard be masked by another gate's
added one, and it goes slack by a whole gate's branch count the day a third gate lands — a guard that
gets quieter as the population grows.

AND THEY ARE REQUIRED, once a single gate is discovered (TOOL-aRepatriatedFork-9, ported from
adopter nc). `ARMS_FLOORS` defaulted to the empty string, so a tree that never declared it had both
floor arms iterating an EMPTY mapping and neither could ever fire — a guard whose population is
supplied by a key nobody set, which is the could-not-fail shape this file exists to detect, one level
up. `--check` refuses an empty or undeclared value while any gate is discovered, and `--emit-floors`
prints the declaration to paste. A tree with NO discovered gate is not refused. That is NOT the fresh
adopter of this kit, whatever the port's source said: installing the kit installs
`check-memory-hygiene.sh`, which defines the helper, so a fresh adopter has a gate on day one and is
refused on day one — owner-resolved (section 8 F2 of the unit), and `adopt-memory-tree.sh --scaffold`
prints the `--emit-floors` command in its next steps for that reason.

SIGNATURE 2 — A REFUSAL THAT IS NOT A FAIL CALL (TOOL-aGraftedHelix-47, closing TOOL-aDeferredBar-8).
An adopter's `--check` that prints a reason and exits 1, and a gate's delegated block that prints a
module's capture and sets `status=1`, were invisible to the predicate above. With
`ARMS_REFUSALS="graded"` in `.memory-tree.conf`, every tracked `*.sh` that is not `*.test.sh` and does
not sit under MEMORY_ROOT is read for REFUSAL SITES: a line whose code, with quoted spans, comments and
here-document bodies blanked, carries `exit 1` as a word or assigns `status=1`. A line holding a
`fail <n> "` call, and the helper's definition, stay signature 1's. A script holding a site is a gate
beside the helper-defined ones, with the same sibling-test rule. Its reason is decided in order:
  (a) the last `echo`/`printf` before the exit in the same statement — its first argument's literal,
      cut by `message_of`, signed by `signature` (a printf conversion counts as an interpolation); a
      signature under 12 characters makes the site DELEGATED instead;
  (b) that print carrying no literal (`printf '%s\n' "$capture"; status=1`): DELEGATED;
  (c) `<command> || exit 1` or `|| { …; exit 1; }` whose left side is not a `[`/`[[`/`test`
      condition: DELEGATED, because the callee prints the reason;
  (d) otherwise the BLOCK is walked upward — lines at the statement's indentation or deeper,
      comments, here-document bodies and quote-continuation lines skipped, stopping at the first
      blank or shallower line — and its TOPMOST print decides as in (a) or (b);
  (e) no print: UNREASONED, counted and listed, and not a site.
A DELEGATED site is signed by the nearest `# arm-signature: <text>` comment above it inside its
block (at least 12 characters, and no other site between them): the text its callee prints on that
refusal path. An arm asserting that text arms it. Unmarked, it cannot be armed and its pin key is its
own source line, whitespace-squeezed. A marker above a REASONED site is refused, because a declared
signature beside a derived one is two answers to one question, and a marker no delegated site reads
is refused, so a marker cannot outlive its site silently. A script this module's quote reader leaves
inside an unterminated quote or here-document is refused by name rather than read as clean.

Keys and pins. A site is keyed (gate, kind, occurrence, signature): kind `exit` or `status`, the
occurrence counting that gate's sites of that kind sharing that signature, so an inserted refusal
does not re-key the rows below it. Its pin row has FIVE tab-separated fields, the last its REASON:
`gate<TAB>kind<TAB>occurrence<TAB>signature<TAB>reason`. An empty reason or the placeholder
`REASON-OWED`, which `--emit-pin` writes, is refused, and every waived row prints
`check-arms: waived <gate>:<line> <kind> — <reason>` on every run. Every pin rule above holds for these
rows: shrink-only, a pinned site that is armed reds, a row naming no live site reds, and a site pinned
in two files is refused. A script found only by signature 2 with no sibling test is not an error while
every one of its sites is pinned.

THE SWITCH. Blank or absent is OFF, `graded` is ON, anything else is refused by name. It ships OFF,
because this file ships to every adopter as `engine` and turning it on reds their unarmed exits on
upgrade. Discovery runs in BOTH states, because the OFF line's count is that state's liveness
assertion: OFF prints how many sites go ungraded and how many exit/status pin rows were not read; ON
prints a census line (sites, scripts, armed, waived, unreasoned) on every run. Under ON the per-gate
floors count sites beside fail branches, so `--emit-floors` is re-run when the switch moves.

WHAT SIGNATURE 2 DOES NOT CHECK. A reason is prose and nothing checks that it is true. A marker's text
is trusted until the suite holding its arm runs. Python refusals, exit codes other than 1,
`return 1`, and hooks without a `.sh` suffix are outside the population. Unreasoned exits are listed
and never graded. The walk reads indentation, so a block indented against its own nesting can end
early or late, and a false association reads as a reasoned site with the wrong signature: `--report`
prints the line each signature was read from, and that column is the only defence.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PIN = "project/unarmed-branches.txt"

FAIL_RE = re.compile(r'\bfail (\d+) "(.*)$')
HELPER_RE = re.compile(r"^\s*fail\(\)\s*\{")
# A COMMAND SUBSTITUTION is an interpolation too (TOOL-aRepatriatedFork-18): `repair with
# $(derive_index_repair)` kept the call's SOURCE in the signature, which no run can ever print.
INTERP_RE = re.compile(r'\$\([^()]*\)|\$\{?[A-Za-z_][A-Za-z0-9_]*\}?')
# A NEGATIVE assertion. `miss` is this kit's absence helper; the `&&` form is the inline one.
NEGATIVE_RE = re.compile(r"^\s*(miss\b|.*grep -qF .* <<<.*\s&&\s)")
# A STRANDED prefix: an unarmed branch whose test holds a line carrying the signature's first
# STRAND_MIN characters but not the whole of it. It is a DIAGNOSIS beside the refusal, never an
# arm — a prefix that armed would let any fragment satisfy the leg. A shorter quote is
# indistinguishable from prose about the message, so below this bound nothing is named; a signature
# shorter than this cannot strand by prefix, because a line holding all of it arms the branch.
STRAND_MIN = 24
# Signature 2 (TOOL-aGraftedHelix-47). Every pattern below runs over a line's CODE, the text left
# once scan_shell_lines has blanked its quoted spans, comments and here-document bodies.
EXIT_RE = re.compile(r"(?<![\w$-])exit\s+1(?!\w)")
STATUS_RE = re.compile(r"(?<![\w$-])status=1(?!\w)")
PRINT_RE = re.compile(r"(?<![\w$./-])(echo|printf)(?![\w-])")
HEREDOC_RE = re.compile(r"<<(-?)\s*\\?(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\2")
MARKER_RE = re.compile(r"^\s*#\s*arm-signature:(.*)$")
TEST_COND_RE = re.compile(r"!?\s*(\[\[?|test)(\s|$)")
PRINTF_CONV_RE = re.compile(r"%[-+ #0-9.*]*[a-zA-Z%]|\\[a-z\\]")
REASON_OWED = "REASON-OWED"
REFUSAL_KINDS = ("exit", "status")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv, cwd=None):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def read(p):
    with open(p, "rb") as fh:
        return fh.read().decode("utf-8", "replace").replace("\r\n", "\n")


# TOOL-aWeldedTribunal-5 -- ONE `.memory-tree.conf` parser for the whole kit. Six readers held an
# identical naive body while the shell gate SOURCES the same file, so a legal spelling bash accepts
# and the python half mis-read REMOVED coverage with the gate still green. TOOL-aRepatriatedFork-9
# moved it into `tree_lib.py`: importing it from `corpus_ids.py` made that ENGINE a prerequisite of
# this one, and at an adopter whose `corpus_ids.py` is its own program this gate died on import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tree_lib import kit_rel, parse_conf  # noqa: E402  the kit's shared helpers

def load_conf(root):
    conf = {"MEMORY_ROOT": "memory", "ARMS_FLOORS": "", "ARMS_REFUSALS": ""}
    p = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(p):
        parse_conf(read(p), conf)
    return conf


def message_of(tail: str) -> str:
    """The message text, ending at the first UNESCAPED closing quote.

    Everything after that quote is shell, not output. A line with no closing quote is a run-on
    message that continues on the next line; the whole tail is the best available approximation and
    the signature is taken from it.
    """
    i = 0
    while i < len(tail):
        if tail[i] == "\\":
            i += 2
            continue
        if tail[i] == '"':
            return tail[:i]
        i += 1
    return tail


def signature(message: str) -> str:
    """A literal slice of the branch's own message that a test can assert on.

    Interpolations are dropped rather than guessed at, and the longest surviving literal run is the
    signature — short runs like ':' or ' — ' appear in every message and would arm every branch.

    FOR THE ARM AUTHOR: the run does not stop where the sentence does. A message ending
    `"... is not the remedy: refs/heads/$cur"` has the signature `... is not the remedy: refs/heads/`,
    trailing path fragment and all, because that text precedes the first interpolation. Only ':', '"'
    and spaces are trimmed. An arm that stops at the last WORD reads as UNARMED, and both --check's
    refusal and --report name it STRANDED at its test line; --report prints every row's signature
    WHOLE (it once cut rows at 72 characters, so the row it told the author to copy WAS the prefix
    that stranded the arm — TOOL-aWokenSentinel-25), so copy that row rather than the source.
    """
    parts = [p.strip() for p in INTERP_RE.split(message)]
    parts = [p.rstrip(':" ').strip() for p in parts]
    best = max(parts, key=len) if parts else ""
    return best


def discover(root: str) -> list:
    """Every (gate, test) pair in the tree. Derived, never listed."""
    tracked = [p for p in run("git", "ls-files", cwd=root).split("\n") if p.endswith(".sh")]
    pairs = []
    for rel in tracked:
        if rel.endswith(".test.sh"):
            continue                          # a fixture that quotes a fail line is not a gate
        try:
            text = read(os.path.join(root, rel))
        except OSError:
            continue
        if not any(HELPER_RE.match(l) for l in text.split("\n")):
            continue                          # quotes a fail line but does not own the protocol
        if not any(FAIL_RE.search(l) for l in text.split("\n")
                   if not l.lstrip().startswith("#") and "fail() {" not in l):
            continue
        pairs.append((rel, rel[:-3] + ".test.sh"))
    return sorted(pairs)


def branches(root: str, gate_rel: str) -> list:
    """Every `fail` call site in one gate, keyed on (number, ordinal-within-that-number)."""
    path = os.path.join(root, gate_rel)
    if not os.path.isfile(path):
        raise Problem(f"check-arms: {gate_rel} is missing — this meta-gate reads the gate's source, "
                      f"so a renamed or moved gate must be repointed here, not silently uncovered")
    seen = {}
    out = []
    for lineno, line in enumerate(read(path).split("\n"), 1):
        if line.lstrip().startswith("#") or "fail() {" in line:
            continue                          # a comment about a branch, and the helper's definition
        m = FAIL_RE.search(line)
        if not m:
            continue
        num = int(m.group(1))
        seen[num] = seen.get(num, 0) + 1
        sig = signature(message_of(m.group(2)))
        if len(sig) < 12:
            raise Problem(f"{gate_rel}:{lineno}: check {num} branch {seen[num]} has no literal run "
                          f"long enough to assert on ({sig!r}) — reword the message or the arm cannot "
                          f"name it")
        out.append({"gate": gate_rel, "num": num, "ord": seen[num], "line": lineno, "sig": sig})
    return out


def armed_signatures(root: str, test_rel: str) -> list:
    """(line number, text) for every line of the test file that could carry a POSITIVE assertion.

    A COMMENT is not an arm. The test file's prose explains what each arm covers and naturally quotes
    the messages, so a comment-blind scan would let a branch read as armed on the strength of a
    sentence describing it — the same shape as the bare-`check N` mention and the absence assertion
    this function already refuses. All three are "something mentions it", not "something exercises
    it". The numbers are kept so a STRANDED prefix can be named at its line, over EXACTLY the
    population the armed read walks: a comment quoting a message can no more be reported stranded
    than it can be counted as an arm.
    """
    path = os.path.join(root, test_rel)
    if not os.path.isfile(path):
        raise Problem(f"check-arms: {test_rel} is missing, but its gate has `fail` branches — with no "
                      f"test file EVERY branch is unarmed and there is nothing to arm them with")
    out = []
    for no, line in enumerate(read(path).split("\n"), 1):
        if line.lstrip().startswith("#"):
            continue
        if NEGATIVE_RE.match(line):
            continue
        out.append((no, line))
    return out


def check_refusal_switch(conf: dict) -> bool:
    """`ARMS_REFUSALS`: blank is OFF, `graded` is ON, and anything else is refused by name."""
    val = conf.get("ARMS_REFUSALS", "").strip()
    if val not in ("", "graded"):
        raise Problem(f"check-arms: ARMS_REFUSALS is {val!r} — only blank (signature 2 off) or `graded` "
                      f"is legal, and guessing which one was meant would grade a tree its owner did "
                      f"not ask for")
    return val == "graded"


def scan_shell_lines(text: str) -> list:
    """-> one (raw, code, continued, heredoc) per line of a shell script.

    `code` is `raw` with every quoted span, comment and `$'…'` blanked to spaces, so a pattern over it
    can only match shell. State carries ACROSS lines, because a message spanning two lines leaves its
    second line inside a quote (`continued`), and a here-document's body lines are `heredoc`. A
    command substitution inside double quotes is code again until its closing paren. A script that
    ENDS inside a quote or a here-document gets a trailing None row, which scan_refusal_sites refuses.
    """
    rows, stack, depth, queue, body = [], ["c"], [], [], None
    for raw in text.split("\n"):
        if body:
            rows.append((raw, " " * len(raw), False, True))
            if (raw.lstrip("\t") if body[0] else raw).strip() == body[1]:
                body = queue.pop(0) if queue else None
            continue
        continued, code, i, n = stack[-1] in "sad", list(raw), 0, len(raw)
        while i < n:
            ch, top = raw[i], stack[-1]
            if top in "sa":
                if top == "a" and ch == "\\":
                    code[i:i + 2] = " " * len(code[i:i + 2])
                    i += 2
                    continue
                if ch == "'":
                    stack.pop()
                code[i] = " "
                i += 1
                continue
            if top == "d":
                if ch == "\\":
                    code[i:i + 2] = " " * len(code[i:i + 2])
                    i += 2
                    continue
                if ch == '"':
                    stack.pop()
                elif raw.startswith("$(", i) and not raw.startswith("$((", i):
                    stack.append("p")
                    depth.append(0)
                    code[i:i + 2] = "  "
                    i += 2
                    continue
                code[i] = " "
                i += 1
                continue
            if ch == "\\":
                i += 2
                continue
            if ch == "#" and (i == 0 or raw[i - 1] in " \t;|&()"):
                code[i:] = " " * (n - i)
                break
            if raw.startswith("$'", i):
                stack.append("a")
                code[i:i + 2] = "  "
                i += 2
                continue
            if ch in "'\"":
                stack.append("s" if ch == "'" else "d")
                code[i] = " "
                i += 1
                continue
            if raw.startswith("$(", i) and not raw.startswith("$((", i):
                stack.append("p")
                depth.append(0)
                i += 2
                continue
            if raw.startswith("<<", i) and not raw.startswith("<<<", i):
                hm = HEREDOC_RE.match(raw, i)
                if hm:
                    queue.append((hm.group(1) == "-", hm.group(3)))
                    i = hm.end()
                    continue
            if top == "p":
                if ch == "(":
                    depth[-1] += 1
                elif ch == ")":
                    if depth[-1]:
                        depth[-1] -= 1
                    else:
                        stack.pop()
                        depth.pop()
            i += 1
        rows.append((raw, "".join(code), continued, False))
        if queue and body is None:
            body = queue.pop(0)
    if stack != ["c"] or body:
        rows.append(None)                     # unbalanced: the caller refuses the script by name
    return rows


def extract_print_message(raw: str, pm) -> str:
    """The signature a print at match `pm` of `raw` emits: its first argument's literal, or ''."""
    rest = raw[pm.end():].lstrip(" \t")
    while True:
        om = re.match(r"(-[neE]+|--|-v\s+\S+)\s+", rest)
        if not om:
            break
        rest = rest[om.end():]
    if rest.startswith('"'):
        msg = re.sub(r'\\([\\"`])', r"\1", message_of(rest[1:]))   # what the shell prints for \" \` \\
    elif rest.startswith("$'"):
        msg = rest[2:].split("'", 1)[0]
    elif rest.startswith("'"):
        msg = rest[1:].split("'", 1)[0]
    else:
        msg = re.split(r"[;|&<>)]", rest, 1)[0]
    # A positional or special parameter is an interpolation too: `run $0` prints the script's path,
    # never the two characters. INTERP_RE is signature 1's and stays as it is, so this is local.
    msg = re.sub(r"\$[0-9#?*@$!-]", "${_}", msg.split("\n", 1)[0])
    if pm.group(1) == "printf":
        msg = PRINTF_CONV_RE.sub("${_}", msg)     # a conversion is an interpolation: no run prints it
    return signature(msg)


def derive_refusal_reason(rows: list, start: int, k: int, pos: int, site_rows: set) -> tuple:
    """-> (class, signature, 1-based line it was read from) for the site at row `k`, offset `pos`.

    `start` is the row its statement began on (a site line that opens inside a quote belongs to the
    statement above it). Rules (a)-(e) of the module docstring, first match wins. The (d) walk also
    stops at another site, whose print is that site's reason and not this one's, and it prefers the
    topmost print at the statement's OWN indentation over one nested deeper in an earlier compound.
    """
    raw = "\n".join(r[0] for r in rows[start:k + 1])
    code = "\n".join(r[1] for r in rows[start:k + 1])
    off = sum(len(r[1]) + 1 for r in rows[start:k]) + pos

    def derive_from_print(text, pm, first_row):
        sig = extract_print_message(text, pm)
        line = first_row + text.count("\n", 0, pm.start()) + 1
        return ("reasoned", sig, line) if len(sig) >= 12 else ("delegated", None, line)

    prints = [pm for pm in PRINT_RE.finditer(code) if pm.start() < off]
    if prints:                                                        # (a), (b)
        return derive_from_print(raw, prints[-1], start)
    head = code[:off]
    bar = head.rfind("||")
    if bar >= 0 and re.fullmatch(r"\|\|\s*(\{[^{}]*)?", head[bar:]):  # (c)
        # Split on the CODE, read the RAW: a command whose words are all quoted is blank in `code`.
        cut = [sm.end() for sm in re.finditer(r"&&|\|\||;|\{|\(|\bthen\b|\bdo\b|\belse\b", head[:bar])]
        left = raw[cut[-1] if cut else 0:bar].strip()
        if left and not TEST_COND_RE.match(left):
            return ("delegated", None, k + 1)
    indent = len(rows[start][0]) - len(rows[start][0].lstrip())        # (d)
    top, deep = None, None
    for j in range(start - 1, -1, -1):
        r = rows[j]
        if r[3] or r[2]:
            continue
        if not r[0].strip() or j in site_rows:
            break
        if not r[1].strip() and r[0].lstrip().startswith("#"):
            continue
        ind = len(r[0]) - len(r[0].lstrip())
        if ind < indent:
            break
        if PRINT_RE.search(r[1]):
            if ind == indent:
                top = j
            else:
                deep = j
    top = deep if top is None else top
    if top is None:
        return ("unreasoned", None, None)                             # (e)
    end = top
    while end + 1 < len(rows) and rows[end + 1][2]:
        end += 1
    text = "\n".join(r[0] for r in rows[top:end + 1])
    codetext = "\n".join(r[1] for r in rows[top:end + 1])
    return derive_from_print(text, PRINT_RE.search(codetext), top)


def read_arm_marker(rows: list, start: int, site_rows: set):
    """-> (text, 1-based line) of the `# arm-signature:` comment nearest above a site, or None.

    The walk is the reason walk's — at the statement's indentation or deeper, stopping at a blank or
    shallower line — and it also stops at another site, so a marker belongs to exactly ONE site: the
    first one below it.
    """
    indent = len(rows[start][0]) - len(rows[start][0].lstrip())
    for j in range(start - 1, -1, -1):
        r = rows[j]
        if r[3] or r[2]:
            continue
        if not r[0].strip() or j in site_rows:
            return None
        mm = MARKER_RE.match(r[0])
        if mm and not r[1].strip():
            return (mm.group(1).strip(), j + 1)
        if r[0].lstrip().startswith("#"):
            continue
        if len(r[0]) - len(r[0].lstrip()) < indent:
            return None
    return None


def scan_refusal_sites(root: str, m: str) -> tuple:
    """Signature 2's population: ({gate: {"sites": [...], "unreasoned": [lines]}}, [errors]).

    Every tracked `*.sh` that is not `*.test.sh` and not under the memory root (a build record can hold
    a frozen repro script, which is no gate). Derived, never listed.
    """
    tracked = [p for p in run("git", "ls-files", cwd=root).split("\n")
               if p.endswith(".sh") and not p.endswith(".test.sh")
               and not p.startswith(m.rstrip("/") + "/")]
    out, errors = {}, []
    for rel in tracked:
        try:
            rows = scan_shell_lines(read(os.path.join(root, rel)))
        except OSError:
            continue
        if rows and rows[-1] is None:
            errors.append(f"check-arms: {rel} ends inside an unterminated quote or here-document by "
                          f"this module's reading, so its refusal sites cannot be read — bash and the "
                          f"reader disagree, and reading the rest as clean would hide every site in it")
            continue
        cands = []
        for k, (raw, code, _cont, here) in enumerate(rows):
            if here or "fail() {" in raw or HELPER_RE.match(raw) or FAIL_RE.search(raw):
                continue
            em, sm = EXIT_RE.search(code), STATUS_RE.search(code)
            if em or sm:
                cands.append((k, "exit" if em else "status", (em or sm).start()))
        site_rows = {k for k, _, _ in cands}
        sites, unreasoned, markers_read = [], [], set()
        for k, kind, pos in cands:
            start = k
            while start > 0 and rows[start][2]:
                start -= 1
            cls, sig, src = derive_refusal_reason(rows, start, k, pos, site_rows - {k})
            if cls == "unreasoned":
                unreasoned.append(k + 1)
                continue
            mk = read_arm_marker(rows, start, site_rows - {k})
            if mk:
                markers_read.add(mk[1])
                if cls == "reasoned":
                    errors.append(f"check-arms: {rel}:{mk[1]} carries an arm-signature marker above the "
                                  f"REASONED site at line {k + 1}, whose signature is derived from its "
                                  f"own message — a declared one beside it is two answers to one "
                                  f"question; delete the marker")
                elif len(mk[0]) < 12:
                    errors.append(f"check-arms: {rel}:{mk[1]} carries an arm-signature marker shorter "
                                  f"than 12 characters ({mk[0]!r}), too short to assert on")
                else:
                    sig, src = mk[0], mk[1]
            sites.append({"gate": rel, "kind": kind, "line": k + 1, "cls": cls, "sig": sig,
                          "src": src, "key_sig": sig or " ".join(rows[k][0].split())})
        for j, r in enumerate(rows):
            if not r[3] and MARKER_RE.match(r[0]) and not r[1].strip() and j + 1 not in markers_read:
                errors.append(f"check-arms: {rel}:{j + 1} carries an arm-signature marker no delegated "
                              f"site reads — its site was deleted or moved out of the block, and a "
                              f"marker that outlives its site would arm nothing; delete or re-place it")
        seen = {}
        for s in sites:
            key = (s["kind"], s["key_sig"])
            seen[key] = seen.get(key, 0) + 1
            s["occ"] = seen[key]
        if sites or unreasoned:
            out[rel] = {"sites": sites, "unreasoned": unreasoned}
    return out, errors


def parse_pin(root: str, m: str, graded: bool = False) -> tuple:
    """-> (fail rows, refusal rows, refusal rows not read), from the central file AND every SIDECAR.

    A fail row is (gate, check, ordinal, sig, line, file). A row whose second field is `exit` or
    `status` is signature 2's, carries a fifth field, its REASON, and is returned as a dict — or, with
    the switch off, is not read at all and only counted, which the OFF line reports.

    TOOL-aRepatriatedFork-18 S5. A pin for a SHIPPED gate is a fact about gov's bytes, so it travels
    with them: a tracked `unarmed-branches.txt` in any directory other than the central one pins the
    gates of THAT directory, and its gate column is relative to it. So `unattended.sh<TAB>9<TAB>1…`
    means the same branch at `<prefix>/unattended/` and at `scripts/unattended/`, and no adopter re-keys
    gov's rows by hand. The sidecar set is every tracked file of that name, not the discovered gates'
    directories, so a sidecar whose gate vanished is still read and still reds as stale.
    """
    central = f"{m}/{PIN}"
    sidecars = sorted(p for p in run("git", "ls-files", cwd=root).split("\n")
                      if os.path.basename(p) == os.path.basename(PIN) and p != central)
    rows, rrows, unread = [], [], 0
    for label in [central] + sidecars:
        p = os.path.join(root, label)
        if not os.path.isfile(p):
            continue
        base = "" if label == central else os.path.dirname(label)
        for i, line in enumerate(read(p).split("\n"), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) > 1 and parts[1].strip() in REFUSAL_KINDS:
                if not graded:
                    unread += 1
                    continue
                # The reason is the LAST field, so an empty one shifts nothing and is refused by name
                # in cmd_check rather than read as absent.
                if len(parts) != 5:
                    raise Problem(f"{label}:{i}: a `{parts[1].strip()}` row takes 5 tab-separated fields "
                                  f"(gate<TAB>kind<TAB>occurrence<TAB>signature<TAB>reason), got "
                                  f"{len(parts)}")
                gate = parts[0].strip()
                rrows.append({"gate": f"{base}/{gate}" if base else gate, "kind": parts[1].strip(),
                              "occ": parts[2].strip(), "sig": parts[3].strip(),
                              "reason": parts[4].strip(), "line": i, "file": label})
                continue
            if len(parts) != 4:
                raise Problem(f"{label}:{i}: expected 4 tab-separated fields "
                              f"(gate<TAB>check<TAB>ordinal<TAB>signature), got {len(parts)}")
            gate = parts[0].strip()
            gate = f"{base}/{gate}" if base else gate
            rows.append((gate, parts[1].strip(), parts[2].strip(), parts[3].strip(), i, label))
    return rows, rrows, unread


def parse_floors(conf: dict) -> dict:
    """`ARMS_FLOORS="<gate>:<branches>:<armed> …"` — per gate, both one-sided upward."""
    out = {}
    for tok in conf.get("ARMS_FLOORS", "").split():
        parts = tok.rsplit(":", 2)
        if len(parts) != 3 or not parts[1].isdigit() or not parts[2].isdigit():
            raise Problem(f"check-arms: ARMS_FLOORS entry {tok!r} is not <gate>:<branches>:<armed>")
        out[parts[0]] = (int(parts[1]), int(parts[2]))
    return out


def classify(root: str, conf: dict, pairs=None) -> dict:
    m = conf["MEMORY_ROOT"]
    graded = check_refusal_switch(conf)
    pairs = discover(root) if pairs is None else pairs
    brs, errors = [], []
    for gate_rel, test_rel in pairs:
        # A gate that raises does NOT abort the walk: for the duration of that red the gate would
        # otherwise enforce nothing else — every other gate's unarmed branches, every stale pin row
        # and both floors would go unchecked, and a second regression could land under cover.
        try:
            gb = branches(root, gate_rel)
            numbered = [(test_rel, no, l) for no, l in armed_signatures(root, test_rel)]
            # S6: an adopter that forks a gate arms ITS branches in `<stem>.local.test.sh`, which no
            # descriptor claims, so the shipped sibling stays byte-identical to gov's. Optional: an
            # absent or empty one arms nothing and is not an error.
            local_rel = test_rel[:-len(".test.sh")] + ".local.test.sh"
            if os.path.isfile(os.path.join(root, local_rel)):
                numbered += [(local_rel, no, l) for no, l in armed_signatures(root, local_rel)]
        except Problem as exc:
            errors.append(str(exc))
            continue
        lines = {l for _, _, l in numbered}
        for b in gb:
            b["armed"] = next((f for f, _, l in numbered if b["sig"] in l), None)
        # A STRANDED prefix: the first arm-shaped line holding the signature's opening run but not
        # the whole of it. Diagnosis only — the branch stays unarmed (TOOL-aWokenSentinel-25). A line
        # that arms SOME branch of this gate is that branch's arm, never a sibling's stranded prefix:
        # two messages of one gate opening with the same STRAND_MIN characters is a common shape, and
        # without this exclusion the row names a whole, working arm as the line to lengthen.
        arms = {l for l in lines if any(b["sig"] in l for b in gb)}
        for b in gb:
            b["stranded"] = None
            if not b["armed"] and len(b["sig"]) >= STRAND_MIN:
                head = b["sig"][:STRAND_MIN]
                for f, no, l in numbered:
                    if head in l and l not in arms:
                        b["stranded"] = (f, no)
                        break
        brs.extend(gb)
    pinned, rpinned, unread = parse_pin(root, m, graded)
    # SIGNATURE 2 is scanned in BOTH states: the OFF line's count is that state's liveness assertion.
    found, rerrors = scan_refusal_sites(root, m)
    sites = [s for g in sorted(found) for s in found[g]["sites"]]
    for gate_rel in sorted({s["gate"] for s in sites}):
        test_rel = gate_rel[:-3] + ".test.sh"
        numbered = []
        for rel in (test_rel, test_rel[:-len(".test.sh")] + ".local.test.sh"):
            if os.path.isfile(os.path.join(root, rel)):
                numbered += [(rel, l) for _, l in armed_signatures(root, rel)]
        for s in sites:
            if s["gate"] == gate_rel:
                s["test"] = test_rel
                s["test_missing"] = not os.path.isfile(os.path.join(root, test_rel))
                s["armed"] = next((f for f, l in numbered if s["sig"] and s["sig"] in l), None)
    if graded:
        errors.extend(rerrors)
    gates = sorted({g for g, _ in pairs} | ({s["gate"] for s in sites} if graded else set()))
    return {"branches": brs, "pinned": pinned, "errors": errors, "pairs": pairs, "m": m,
            "graded": graded, "sites": sites, "rpinned": rpinned, "unread": unread,
            "unreasoned": [(g, ln) for g in sorted(found) for ln in found[g]["unreasoned"]],
            "rerrors": rerrors, "gates": gates}


def check_refusal_sites(st: dict) -> tuple:
    """-> (problems, waived lines, census line) for signature 2, under the switch ON."""
    bad, waived, rkeys = [], [], {}
    for r in st["rpinned"]:
        key = (r["gate"], r["kind"], r["occ"], r["sig"])
        if key in rkeys:
            o = rkeys[key]
            bad.append(f"check-arms: {r['file']}:{r['line']} pins {r['gate']} {r['kind']} site "
                       f"{r['occ']}, which {o['file']}:{o['line']} already pins — a site is pinned in "
                       f"exactly one file; delete one of the two rows")
            continue
        rkeys[key] = r
        if r["reason"] in ("", REASON_OWED):
            what = "an EMPTY reason" if not r["reason"] else f"the placeholder {REASON_OWED}"
            bad.append(f"check-arms: {r['file']}:{r['line']} pins {r['gate']} {r['kind']} site "
                       f"{r['occ']} with {what} — a waiver that prints no reason is a silent one; "
                       f"write why no arm reaches it")
    armed = 0
    for s in st["sites"]:
        r = rkeys.get((s["gate"], s["kind"], str(s["occ"]), s["key_sig"]))
        if s["armed"]:
            armed += 1
            if r:
                bad.append(f"check-arms: {r['file']}:{r['line']} pins {s['gate']} {s['kind']} site "
                           f"{s['occ']}, which IS armed now — delete the row (the pin is shrink-only)")
            continue
        if r:
            waived.append(f"check-arms: waived {s['gate']}:{s['line']} {s['kind']} — {r['reason']}")
            continue
        why = (f" — and {s['test']} is missing, so nothing can arm it" if s["test_missing"]
               else " — an unmarked DELEGATED site: mark its block with `# arm-signature: <text its "
                    "callee prints>` and assert that text, or pin it" if not s["sig"] else "")
        bad.append(f"check-arms: {s['gate']}:{s['line']} {s['kind']} site ({s['cls']}) has no "
                   f"POSITIVE assertion naming its own failure text ({s['key_sig']!r}) and is not "
                   f"pinned in {st['m']}/{PIN} or a sidecar beside the gate{why}")
    live = {(s["gate"], s["kind"], str(s["occ"]), s["key_sig"]) for s in st["sites"]}
    for key, r in rkeys.items():
        if key not in live:
            bad.append(f"check-arms: {r['file']}:{r['line']} pins {r['gate']} {r['kind']} site "
                       f"{r['occ']} ({r['sig']!r}), which no live site carries — the refusal was "
                       f"deleted, reworded, or moved out of the population")
    census = (f"check-arms: refusal signature — {len(st['sites'])} site(s) in "
              f"{len({s['gate'] for s in st['sites']})} script(s): {armed} armed, {len(waived)} "
              f"waived; {len(st['unreasoned'])} unreasoned line(s) not graded")
    return bad, waived, census


def cmd_check(root: str, conf: dict) -> int:
    st = classify(root, conf)
    brs, pinned, m = st["branches"], st["pinned"], st["m"]
    bad = list(st["errors"])
    pin_keys = {}
    for r in pinned:
        key = (r[0], r[1], r[2])
        if key in pin_keys:
            # S5: ONE branch, ONE pin. Two rows for it means two files can disagree about its
            # signature and each shrink-only check would read only one of them.
            bad.append(f"check-arms: {r[5]}:{r[4]} pins {r[0]} check {r[1]} branch {r[2]}, which "
                       f"{pin_keys[key][5]}:{pin_keys[key][4]} already pins — a branch is pinned in "
                       f"exactly one file; delete one of the two rows")
            continue
        pin_keys[key] = r
    for b in brs:
        key = (b["gate"], str(b["num"]), str(b["ord"]))
        if b["armed"]:
            if key in pin_keys:
                bad.append(f"check-arms: {pin_keys[key][5]}:{pin_keys[key][4]} pins {b['gate']} check "
                           f"{b['num']} branch {b['ord']}, which IS armed now — delete the row "
                           f"(the pin is shrink-only)")
            continue
        if key not in pin_keys:
            hint = (f" — a STRANDED prefix at {b['stranded'][0]}:{b['stranded'][1]} stops short of "
                    f"the signature; copy the whole row --report prints") if b["stranded"] else ""
            bad.append(f"check-arms: {b['gate']}:{b['line']} check {b['num']} branch {b['ord']} has "
                       f"no POSITIVE assertion naming its own failure text ({b['sig']!r}) and is not "
                       f"pinned in {m}/{PIN} or a sidecar beside the gate{hint}")
        elif pin_keys[key][3] != b["sig"]:
            bad.append(f"check-arms: {pin_keys[key][5]}:{pin_keys[key][4]} pins {b['gate']} check "
                       f"{b['num']} branch {b['ord']} with a stale signature — the message was reworded")
    live = {(b["gate"], str(b["num"]), str(b["ord"])) for b in brs}
    scanned = {g for g, _ in st["pairs"]}
    graded = st["graded"]
    sites = st["sites"] if graded else []
    if graded:
        rbad, waived, census = check_refusal_sites(st)
        bad.extend(rbad)
        for line in waived:
            print(line)
        print(census)
    else:
        print(f"check-arms: refusal signature OFF — ARMS_REFUSALS is not `graded`, so "
              f"{len(st['sites'])} refusal site(s) outside fail() go ungraded and {st['unread']} pin "
              f"row(s) of kind exit or status were not read")
    for r in pin_keys.values():
        if (r[0], r[1], r[2]) not in live:
            why = ("the gate is no longer in the population" if r[0] not in scanned
                   else "the guard was deleted or renumbered")
            bad.append(f"check-arms: {r[5]}:{r[4]} pins {r[0]} check {r[1]} branch {r[2]}, which "
                       f"no longer exists — {why}")
    # PER-GATE floors. An aggregate would let one gate's deletion be masked by another's addition.
    floors = parse_floors(conf)
    # Under the switch ON a script holding a refusal site is a gate too, and its floor counts sites.
    floored = set(st["gates"])
    # NON-VACUITY. Both loops below draw their population from this mapping, so an empty or undeclared
    # `ARMS_FLOORS` leaves them iterating nothing and neither can fire. Refused ONLY when a gate is
    # actually discovered: a tree with no gate has nothing to floor. The remedy names this module by
    # its DERIVED path, never a literal prefix, because an adopter copies it verbatim.
    if not floors and floored:
        bad.append(f"check-arms: ARMS_FLOORS is empty or undeclared while {len(floored)} gate(s) are "
                   f"discovered, so both floor arms have an EMPTY population and neither can fire — a "
                   f"gate leaving discovery would be silent. Declare it in .memory-tree.conf, measured "
                   f"against this tree: `python {kit_rel()}/check-arms.py --emit-floors`. A tree with "
                   f"NO discovered gate is not refused")
    # A FLOOR NAMING A GATE THAT IS NOT IN THE POPULATION IS A FAILURE, not a skip. The count loop
    # further down walks the DISCOVERED gates and looks each floor up by key, so a floor whose gate
    # vanished was never consulted there at all: `cmd_check` returned 0 with no output. Measured —
    # reformatting one gate's helper from `fail() {` to `fail () {` drops it out of discovery
    # entirely, taking 14 branches and 14 arms with it, and every floor stayed green. The pin has
    # this guard already (above) but only for a gate some pin ROW names, so for every other
    # discovered gate the floors are the only backstop there is.
    for gate_rel in sorted(floors):
        if gate_rel not in floored:
            bad.append(f"check-arms: ARMS_FLOORS names {gate_rel}, which is NOT in the discovered "
                       f"population — the gate was renamed, moved, or stopped matching the "
                       f"`fail() {{` + call-site predicate. Its branches and arms are no longer "
                       f"counted by anything; fix the gate or remove the floor in a commit that "
                       f"says why")
    for gate_rel in sorted({b["gate"] for b in brs} | {s["gate"] for s in sites}):
        gb = [b for b in brs if b["gate"] == gate_rel] + [s for s in sites if s["gate"] == gate_rel]
        want = floors.get(gate_rel)
        if not want:
            continue
        got = (len(gb), sum(1 for b in gb if b["armed"]))
        for i, label in ((0, "fail branch(es) and refusal site(s)" if graded else "fail branch(es)"),
                         (1, "armed branch(es)")):
            if got[i] < want[i]:
                bad.append(f"check-arms: {gate_rel} has {got[i]} {label} against a floor of "
                           f"{want[i]} (ARMS_FLOORS) — a guard or an assertion was removed; lower "
                           f"the floor in a commit that says why")
    for line in bad:
        print("HYGIENE " + line)
    return 1 if bad else 0


def cmd_report(root: str, conf: dict) -> int:
    st = classify(root, conf)
    floors = parse_floors(conf)
    pinned = {(r[0], r[1], r[2]): r[5] for r in st["pinned"]}
    for gate_rel, test_rel in st["pairs"]:
        gb = [b for b in st["branches"] if b["gate"] == gate_rel]
        want = floors.get(gate_rel, ("unset", "unset"))
        print(f"{gate_rel}  ->  {test_rel}")
        print(f"    branches {len(gb):>3} (floor {want[0]})   armed "
              f"{sum(1 for b in gb if b['armed']):>3} (floor {want[1]})")
        for b in gb:
            # The signature prints WHOLE: this row is what the arm author copies, and a row cut at
            # 72 characters was itself the prefix that stranded every arm over a long message.
            # ...and the FILE that armed or pinned it follows, since S5 and S6 made that one of several.
            pin = pinned.get((b["gate"], str(b["num"]), str(b["ord"])))
            tail = f"  STRANDED {b['stranded'][0]}:{b['stranded'][1]}" if b["stranded"] else ""
            src = (f"  by {b['armed']}" if b["armed"] else f"  in {pin}" if pin else "")
            flag = "ARMED " if b["armed"] else "PINNED" if pin else "      "
            print(f"      check {b['num']:>2} branch {b['ord']}  line {b['line']:>4}  "
                  f"{flag} {b['sig']}{tail}{src}")
    print(f"pinned rows   : {len(st['pinned'])}")
    # SIGNATURE 2, in both states. `from` is the line the signature was READ from — a reasoned site's
    # print, a delegated site's marker — and is the only defence against a walk's false association.
    rpin = {(r["gate"], r["kind"], r["occ"], r["sig"]): r["file"] for r in st["rpinned"]}
    print(f"refusal signature {'graded' if st['graded'] else 'OFF'} — {len(st['sites'])} site(s)")
    for gate_rel in sorted({s["gate"] for s in st["sites"]}):
        gs = [s for s in st["sites"] if s["gate"] == gate_rel]
        print(f"{gate_rel}  ->  {gs[0]['test']}{'  (missing)' if gs[0]['test_missing'] else ''}")
        for s in gs:
            pin = rpin.get((s["gate"], s["kind"], str(s["occ"]), s["key_sig"]))
            flag = "ARMED " if s["armed"] else "WAIVED" if pin else "      "
            src = f"  by {s['armed']}" if s["armed"] else f"  in {pin}" if pin else ""
            print(f"      {s['kind']:<6} site {s['occ']}  line {s['line']:>5}  {flag} {s['cls']:<9} "
                  f"from {s['src']:>5}  {s['key_sig']}{src}")
    for gate_rel, ln in st["unreasoned"]:
        print(f"UNREASONED {gate_rel}:{ln}")
    print(f"refusal pin rows : {len(st['rpinned'])} read, {st['unread']} not read")
    for e in st["errors"] + ([] if st["graded"] else st["rerrors"]):
        print("ERROR " + e)
    return 0


def cmd_emit_pin(root: str, conf: dict) -> int:
    """Print the pin file for the CURRENT unarmed set — the measurement, not a guess."""
    st = classify(root, conf)
    print("# unarmed-branches.txt — `fail` branches with no positive assertion naming their own")
    print("# failure text. SHRINK-ONLY: a row leaves when its branch gains an arm, and check-arms")
    print("# reds if a pinned branch is armed, if a pinned branch or its gate disappears, or if a")
    print("# message is reworded out from under its signature.")
    print("# Fields: gate<TAB>check<TAB>ordinal<TAB>signature, and under ARMS_REFUSALS=\"graded\"")
    print("# gate<TAB>exit|status<TAB>occurrence<TAB>signature<TAB>reason for a refusal site.")
    for b in st["branches"]:
        if not b["armed"]:
            print(f"{b['gate']}\t{b['num']}\t{b['ord']}\t{b['sig']}")
    if st["graded"]:
        # The reason is OWED, never guessed: the gate refuses this placeholder until a person writes it.
        for s in st["sites"]:
            if not s["armed"]:
                print(f"{s['gate']}\t{s['kind']}\t{s['occ']}\t{s['key_sig']}\t{REASON_OWED}")
    return 0


def cmd_emit_floors(root: str, conf: dict) -> int:
    """Print the ARMS_FLOORS declaration for the CURRENT census — the measurement, not a guess.

    One token per DISCOVERED gate and never an aggregate, for the reason the module docstring gives.
    The declaration is the ONLY thing on stdout so it can be pasted into `.memory-tree.conf` verbatim;
    anything the walk could not measure goes to stderr, where a paste cannot swallow it.
    """
    st = classify(root, conf)
    toks = []
    sites = st["sites"] if st["graded"] else []
    for gate_rel in st["gates"]:
        gb = ([b for b in st["branches"] if b["gate"] == gate_rel]
              + [s for s in sites if s["gate"] == gate_rel])
        toks.append(f"{gate_rel}:{len(gb)}:{sum(1 for b in gb if b['armed'])}")
    print('ARMS_FLOORS="' + " ".join(toks) + '"')
    if not st["gates"]:
        # A skip announces itself: an empty emission is a declaration of nothing, and pasting it
        # would floor nothing while LOOKING like a declaration.
        print("check-arms: no gate is discovered in this tree, so the line above is EMPTY and floors "
              "nothing — re-emit once a gate lands", file=sys.stderr)
    for e in st["errors"]:
        print("ERROR " + e, file=sys.stderr)
    if st["errors"]:
        # An errored gate contributes no branches, so it would be emitted at 0:0 — a floor that can
        # never fire, declared under the name of a guard. Refuse rather than hand one over.
        print(f"check-arms: {len(st['errors'])} gate(s) errored above and are emitted at 0:0, which "
              f"is a floor that cannot fire — fix them and re-emit before declaring", file=sys.stderr)
        return 1
    return 0


# ----------------------------------------------------------------------------------------- selftest
def _w(path, text):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))


def derive_install_prefix() -> str:
    """The install prefix WITH its trailing slash, derived from where this file sits and empty at a
    root install. Every fixture and host path the self-test builds is spelled through it, never
    through a literal prefix (TOOL-aRepatriatedFork-28)."""
    import pathlib
    here = pathlib.Path(__file__).resolve().parent
    for anc in here.parents:
        if (anc / ".git").exists():
            rel = here.parent.relative_to(anc).as_posix()
            return "" if rel == "." else rel + "/"
    raise SystemExit(f"{pathlib.Path(__file__).name}: not inside a git repository, so there is no "
                     "install prefix to derive")


def cmd_selftest() -> int:
    PFX = derive_install_prefix()   # TOOL-aRepatriatedFork-28
    fails = []

    def arm(label, want, fn):
        import contextlib
        import io

        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = fn()
            got = buf.getvalue() + f"[rc={rc}]"
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        ok = (want in got) if want else ("[rc=0]" in got)
        print(("arm ok    " if ok else "arm FAIL  ") + label
              + ("" if ok else f" — expected {want!r}, got: {got.strip()}"))
        if not ok:
            fails.append(label)

    HELPER = 'fail() { echo "HYGIENE check $1 FAILED — $2"; status=1; }\n'
    GATE_A = HELPER + \
        '[ -n "$a" ] && fail 1 "alpha branch message here:\n"\n' \
        '[ -n "$b" ] && fail 1 "beta branch message here:\n"\n' \
        '[ -n "$c" ] && fail 2 "gamma branch message here:\n"\n'
    # The INLINE form: a message followed by more shell on the same line. Capturing to end of line
    # would put `"; BLOCK_OK=0; }` into the signature, which no assertion can ever emit.
    GATE_B = HELPER + '[ -n "$d" ] && { fail 1 "delta branch message here"; BLOCK_OK=0; }\n'

    with tempfile.TemporaryDirectory() as base:
        root = os.path.join(base, "repo")
        os.makedirs(root)
        run("git", "init", "-q", ".", cwd=root)
        run("git", "config", "user.email", "t@t.test", cwd=root)
        run("git", "config", "user.name", "t", cwd=root)
        _w(os.path.join(root, ".memory-tree.conf"),
           f'MEMORY_ROOT=memory\nARMS_FLOORS="{PFX}gate-a.sh:3:1"\n')
        _w(os.path.join(root, PFX, "gate-a.sh"), GATE_A)
        _w(os.path.join(root, PFX, "gate-a.test.sh"), "hit 'alpha branch message here'\n")
        _w(os.path.join(root, PFX, "gate-b.sh"), GATE_B)
        _w(os.path.join(root, PFX, "gate-b.test.sh"), "hit 'delta branch message here'\n")
        # A *.test.sh that QUOTES a fail line AND defines the helper — the shape that would make the
        # whole suite permanently red by demanding a <stem>.test.test.sh.
        _w(os.path.join(root, PFX, "decoy.test.sh"), HELPER + 'fail 1 "decoy message here"\n')
        _w(os.path.join(root, "memory", "project", ".keep"), "")
        run("git", "add", "-A", cwd=root)
        run("git", "commit", "-q", "-m", "f", "--no-verify", cwd=root)
        conf = load_conf(root)
        pin = os.path.join(root, "memory", "project", "unarmed-branches.txt")
        # A tracked tree with no `fail() {` gate at all: the non-vacuity refusal must stay silent
        # there, because an empty population has nothing to floor.
        empty = os.path.join(base, "empty")
        os.makedirs(empty)
        run("git", "init", "-q", ".", cwd=empty)
        run("git", "config", "user.email", "t@t.test", cwd=empty)
        run("git", "config", "user.name", "t", cwd=empty)
        _w(os.path.join(empty, "README.md"), "no gates here yet\n")
        run("git", "add", "-A", cwd=empty)
        run("git", "commit", "-q", "-m", "e", "--no-verify", cwd=empty)

        arm("two gates are discovered, the decoy test is not",
            "[rc=0]",
            lambda: 0 if [g for g, _ in discover(root)] == [f"{PFX}gate-a.sh", f"{PFX}gate-b.sh"] else 1)
        arm("branches are keyed on the call site, not the check number", "[rc=0]",
            lambda: 0 if [(b["num"], b["ord"]) for b in branches(root, f"{PFX}gate-a.sh")]
            == [(1, 1), (1, 2), (2, 1)] else 1)
        arm("a command substitution is dropped from the signature like a variable", "[rc=0]",
            lambda: 0 if signature(message_of('substituted message here; repair with $(derive_x)"'))
            == "substituted message here; repair with" else 1)
        arm("the capture stops at the closing quote, not end of line", "[rc=0]",
            lambda: 0 if branches(root, f"{PFX}gate-b.sh")[0]["sig"] == "delta branch message here" else 1)

        # the PIN key carries the gate: both gates have a (1,1)
        _w(pin, f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "p", "--no-verify", cwd=root)
        arm("a fully pinned + armed population passes", None, lambda: cmd_check(root, conf))
        # gate A's (1,1) pinned must NOT exempt gate B's (1,1)
        _w(os.path.join(root, PFX, "gate-b.test.sh"), "# no arm here\n")
        _w(pin, f"{PFX}gate-a.sh\t1\t1\talpha branch message here\n"
                f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "p2", "--no-verify", cwd=root)
        out = []
        arm("a pin for gate A does not exempt gate B's same key",
            f"{PFX}gate-b.sh:2 check 1 branch 1 has no POSITIVE",
            lambda: _capture(cmd_check, root, conf, out))
        arm("...and raises no stale-signature line against gate B", "[rc=0]",
            lambda: 0 if not any("gate-b" in l and "stale signature" in l for l in out) else 1)
        arm("...and gate A's own armed branch is reported as wrongly pinned",
            f"pins {PFX}gate-a.sh check 1 branch 1, which IS armed now",
            lambda: _capture(cmd_check, root, conf, []))

        # a missing sibling test is a NAMED failure, and it does not abort the other gate
        _w(pin, f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        os.remove(os.path.join(root, PFX, "gate-b.test.sh"))
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "rm", "--no-verify", cwd=root)
        arm("a gate with no sibling test is named", "gate-b.test.sh is missing, but its gate has",
            lambda: cmd_check(root, conf))
        out2 = []
        _w(pin, "")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "e", "--no-verify", cwd=root)
        # line-agnostic on purpose: the assertion is about WHICH gate still gets scanned, not about
        # where in that gate the branch happens to sit.
        arm("one gate's error does not hide the other gate's branches",
            f"{PFX}gate-a.sh:4 check 1 branch 2 has no POSITIVE",
            lambda: _capture(cmd_check, root, conf, out2))

        # restore gate B, then the per-gate floors
        _w(os.path.join(root, PFX, "gate-b.test.sh"), "hit 'delta branch message here'\n")
        _w(pin, f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "r", "--no-verify", cwd=root)
        arm("restored population passes", None, lambda: cmd_check(root, conf))
        confh = dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:4:1")
        arm("a per-gate branch floor catches a deleted guard",
            f"{PFX}gate-a.sh has 3 fail branch(es) against a floor of 4",
            lambda: cmd_check(root, confh))
        confa = dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:3:2")
        arm("a per-gate armed floor catches a dropped assertion",
            f"{PFX}gate-a.sh has 1 armed branch(es) against a floor of 2",
            lambda: cmd_check(root, confa))
        # CROSS-GATE COMPENSATION: an aggregate floor would be satisfied here; a per-gate one is not.
        confc = dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:4:1 {PFX}gate-b.sh:0:0")
        arm("a per-gate floor is not satisfied by another gate's growth",
            f"{PFX}gate-a.sh has 3 fail branch(es)",
            lambda: cmd_check(root, confc))

        # A FLOOR whose gate is gone. The floors loop walks the DISCOVERED gates and looks each floor
        # up by key, so before this guard a floor for a vanished gate was never consulted at all:
        # rc=0, no output, and a whole gate's branches and arms silently uncounted. The escape is not
        # hypothetical — reformatting `fail() {` to `fail () {` drops a gate out of discovery.
        confz = dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:3:1 {PFX}gate-gone.sh:9:9")
        arm("a floor naming a gate outside the population is a failure",
            "which is NOT in the discovered population", lambda: cmd_check(root, confz))
        # ...and the same floor set with the gate PRESENT is silent, so the arm above is not passing
        # because cmd_check reds on everything.
        arm("...and a floor whose gate IS discovered stays silent", "[rc=0]",
            lambda: cmd_check(root, dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:3:1")))

        # A GATE THAT LEAVES THE POPULATION — the measured escape itself, not a floor naming a gate
        # that never existed. Reformatting the helper from `fail() {` to `fail () {` drops a REAL
        # gate out of discovery, taking every branch and every arm with it. The PIN is emptied first
        # on purpose: a pinned gate is already covered by the vanished-gate arm above, and the gates
        # this escape actually threatens are the ones no pin row names, where the floor is the only
        # thing left watching.
        _w(pin, "")
        _w(os.path.join(root, PFX, "gate-a.sh"), GATE_A.replace("fail() {", "fail () {", 1))
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "s5", "--no-verify", cwd=root)
        arm("a gate whose helper is reformatted leaves the discovered population", "[rc=0]",
            lambda: 0 if [g for g, _ in discover(root)] == [f"{PFX}gate-b.sh"] else 1)
        arm("...and its floor is what catches that, with no pin row to help",
            f"ARMS_FLOORS names {PFX}gate-a.sh, which is NOT in the discovered population",
            lambda: cmd_check(root, dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:3:1 {PFX}gate-b.sh:1:1")))
        # AC6: ONE discovered gate and an empty declaration. The refusal names the module by the
        # path DERIVED for this install, so the arm asserts the derivation rather than a literal.
        arm("...and an empty ARMS_FLOORS is refused while a gate is discovered",
            "ARMS_FLOORS is empty or undeclared while 1 gate(s) are discovered",
            lambda: cmd_check(root, dict(conf, ARMS_FLOORS="")))
        arm("...and the refusal's remedy names this module at its derived kit path",
            f"`python {kit_rel()}/check-arms.py --emit-floors`",
            lambda: cmd_check(root, dict(conf, ARMS_FLOORS="")))
        arm("--emit-floors prints one token per discovered gate, measured",
            f'ARMS_FLOORS="{PFX}gate-b.sh:1:1"\n[rc=0]',
            lambda: cmd_emit_floors(root, dict(conf, ARMS_FLOORS="")))
        # ...and the SAME floor set over the restored gate is silent, so the arms above are not
        # passing because cmd_check reds on everything.
        _w(os.path.join(root, PFX, "gate-a.sh"), GATE_A)
        _w(pin, f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "s5r", "--no-verify", cwd=root)
        arm("...and the restored gate passes the same floor set", "[rc=0]",
            lambda: cmd_check(root, dict(conf, ARMS_FLOORS=f"{PFX}gate-a.sh:3:1 {PFX}gate-b.sh:1:1")))
        # An EMPTY population is not refused.
        arm("an empty ARMS_FLOORS over a tree with no discovered gate is not refused", "[rc=0]",
            lambda: cmd_check(empty, dict(conf, ARMS_FLOORS="")))

        # a pin whose GATE is gone names that, not "the guard was deleted"
        _w(pin, f"{PFX}gate-z.sh\t1\t1\tvanished gate message here\n"
                f"{PFX}gate-a.sh\t1\t2\tbeta branch message here\n"
                f"{PFX}gate-a.sh\t2\t1\tgamma branch message here\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "z", "--no-verify", cwd=root)
        arm("a pin for a gate outside the population says so",
            "the gate is no longer in the population", lambda: cmd_check(root, conf))

        # a signature present only in the PIN arms nothing
        arm("a signature present only in the PIN arms nothing", "[rc=0]",
            lambda: 0 if not [b for b in classify(root, conf)["branches"]
                              if (b["num"], b["ord"]) == (1, 2) and b["armed"]] else 1)

        # a comment and an absence assertion do not arm
        _w(os.path.join(root, PFX, "gate-a.test.sh"),
           "hit 'alpha branch message here'\n"
           "# this arm would cover: gamma branch message here\n"
           "miss 'beta branch message here'\n")
        _w(pin, "")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "c", "--no-verify", cwd=root)
        outc = []
        _capture(cmd_check, root, conf, outc)
        arm("a comment naming the message does not arm", "[rc=0]",
            lambda: 0 if any("check 2 branch 1 has no POSITIVE" in l for l in outc) else 1)
        arm("an absence assertion does not arm", "[rc=0]",
            lambda: 0 if any("check 1 branch 2 has no POSITIVE" in l for l in outc) else 1)

        # a message with no assertable literal run is a named error, not a silent skip
        _w(os.path.join(root, PFX, "gate-a.sh"), HELPER + '[ -n "$a" ] && fail 1 "$X:\n"\n')
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "x", "--no-verify", cwd=root)
        arm("a message with no literal run is named", "no literal run long enough",
            lambda: cmd_check(root, conf))

        # A STRANDED prefix. `signature()` runs past the sentence to the first interpolation, so a
        # test quoting the readable head of a long message reads UNARMED with nothing saying the
        # line is there and short; --check and --report now name that line. The verdict does not
        # move, and the report row holds the signature to its last character — a row cut at 72 was
        # the prefix the gotcha told the author to copy (TOOL-aWokenSentinel-25).
        LONG = ("epsilon branch message here runs long enough that a readable prefix of it "
                "strands its arms")
        # The second branch opens with the first's 40 characters: once the test arms branch 1 with
        # the whole signature, that line holds branch 2's opening run and is NOT its stranded prefix.
        _w(os.path.join(root, PFX, "gate-c.sh"),
           HELPER + f'[ -n "$e" ] && fail 1 "{LONG}: $x"\n'
           f'[ -n "$f" ] && fail 2 "{LONG[:40]} but this sibling ends another way: $y"\n')
        _w(os.path.join(root, PFX, "gate-c.test.sh"), f"hit '{LONG[:40]}'\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "s", "--no-verify", cwd=root)
        arm("a test quoting a prefix of a long message is named STRANDED at its line",
            f"STRANDED prefix at {PFX}gate-c.test.sh:1 stops short of the signature; copy the whole row",
            lambda: cmd_check(root, conf))
        arm("...and --report prints that row's signature whole, with the STRANDED line",
            f"{LONG}  STRANDED {PFX}gate-c.test.sh:1",
            lambda: cmd_report(root, conf))
        # the CONTROL: the same test quoting the whole signature arms it, and nothing says STRANDED
        _w(os.path.join(root, PFX, "gate-c.test.sh"), f"hit '{LONG}'\n")
        run("git", "add", "-A", cwd=root); run("git", "commit", "-q", "-m", "w", "--no-verify", cwd=root)
        outs = []
        _capture(cmd_report, root, conf, outs)
        arm("...and the same test quoting the whole signature reads ARMED with no STRANDED token",
            "[rc=0]",
            lambda: 0 if any("ARMED " in l and f"{LONG}  by {PFX}gate-c.test.sh" in l for l in outs)
            and not any("STRANDED" in l and "gate-c" in l for l in outs) else 1)

        # TOOL-aRepatriatedFork-18 S5 + S6, in a tree of their own: a SIDECAR pin beside the gate,
        # keyed relative to its directory, and an adopter's `<stem>.local.test.sh`. Both were
        # observed red against the a7c78ad2 reader, which read neither file.
        side = os.path.join(base, "side")
        os.makedirs(side)
        run("git", "init", "-q", ".", cwd=side)
        run("git", "config", "user.email", "t@t.test", cwd=side)
        run("git", "config", "user.name", "t", cwd=side)
        _w(os.path.join(side, ".memory-tree.conf"),
           f'MEMORY_ROOT=memory\nARMS_FLOORS="{PFX}kit/g.sh:2:1"\n')
        _w(os.path.join(side, PFX, "kit", "g.sh"),
           HELPER + '[ -n "$a" ] && fail 1 "sidecar pinned branch here"\n'
                    '[ -n "$b" ] && fail 2 "local arm branch message here"\n')
        _w(os.path.join(side, PFX, "kit", "g.test.sh"), "# the shipped suite arms neither\n")
        _w(os.path.join(side, PFX, "kit", "g.local.test.sh"), "hit 'local arm branch message here'\n")
        _w(os.path.join(side, PFX, "kit", "unarmed-branches.txt"),
           "g.sh\t1\t1\tsidecar pinned branch here\n")
        _w(os.path.join(side, "memory", "project", ".keep"), "")
        run("git", "add", "-A", cwd=side)
        run("git", "commit", "-q", "-m", "s", "--no-verify", cwd=side)
        sconf = load_conf(side)
        spin = os.path.join(side, "memory", "project", "unarmed-branches.txt")
        arm("S5+S6: a sidecar pin and a local-suite arm leave the gate green", None,
            lambda: cmd_check(side, sconf))
        arm("...and --report names the sidecar that pinned the branch",
            f"PINNED sidecar pinned branch here  in {PFX}kit/unarmed-branches.txt",
            lambda: cmd_report(side, sconf))
        arm("...and --report names the local suite that armed the other",
            f"ARMED  local arm branch message here  by {PFX}kit/g.local.test.sh",
            lambda: cmd_report(side, sconf))
        _w(spin, f"{PFX}kit/g.sh\t1\t1\tsidecar pinned branch here\n")
        run("git", "add", "-A", cwd=side); run("git", "commit", "-q", "-m", "d", "--no-verify", cwd=side)
        arm("S5: a branch pinned in the central file AND a sidecar is refused, naming both",
            f"{PFX}kit/unarmed-branches.txt:1 pins {PFX}kit/g.sh check 1 branch 1, which "
            "memory/project/unarmed-branches.txt:1 already pins",
            lambda: cmd_check(side, sconf))
        _w(spin, "")
        _w(os.path.join(side, PFX, "kit", "unarmed-branches.txt"),
           "g.sh\t1\t1\tsidecar pinned branch here\ngone.sh\t1\t1\tvanished sidecar gate here\n")
        run("git", "add", "-A", cwd=side); run("git", "commit", "-q", "-m", "g", "--no-verify", cwd=side)
        arm("S5: a sidecar row whose gate left its directory is stale, named at the sidecar",
            f"{PFX}kit/unarmed-branches.txt:2 pins {PFX}kit/gone.sh check 1 branch 1, which no longer "
            "exists — the gate is no longer in the population",
            lambda: cmd_check(side, sconf))
        _w(os.path.join(side, PFX, "kit", "unarmed-branches.txt"),
           "g.sh\t1\t1\tsidecar pinned branch here\n")
        os.remove(os.path.join(side, PFX, "kit", "g.local.test.sh"))
        run("git", "add", "-A", cwd=side); run("git", "commit", "-q", "-m", "l", "--no-verify", cwd=side)
        arm("S6: without the local suite the same branch is named unarmed",
            f"{PFX}kit/g.sh:3 check 2 branch 1 has no POSITIVE",
            lambda: cmd_check(side, sconf))

        # SIGNATURE 2 (TOOL-aGraftedHelix-47). Every arm builds its own tree, with the switch set as
        # its label says, so no arm can pass on a sibling's fixture.
        G, T = f"{PFX}kit/adopt.sh", f"{PFX}kit/adopt.test.sh"
        PINF = os.path.join("memory", "project", "unarmed-branches.txt")

        def build_refusal_tree(name, files, refusals="graded", floors=""):
            t = os.path.join(base, name)
            os.makedirs(t)
            run("git", "init", "-q", ".", cwd=t)
            run("git", "config", "user.email", "t@t.test", cwd=t)
            run("git", "config", "user.name", "t", cwd=t)
            _w(os.path.join(t, ".memory-tree.conf"), f'MEMORY_ROOT=memory\nARMS_REFUSALS="{refusals}"\n'
               f'ARMS_FLOORS="{floors}"\n')
            _w(os.path.join(t, "memory", "project", ".keep"), "")
            for rel, text in files.items():
                _w(os.path.join(t, rel), text)
            run("git", "add", "-A", cwd=t)
            run("git", "commit", "-q", "-m", "r", "--no-verify", cwd=t)
            return t, load_conf(t)

        def run_check_text(t, c):
            sink = []
            _capture(cmd_check, t, c, sink)
            return "\n".join(sink)

        def scan_one(t):
            return scan_refusal_sites(t, "memory")[0].get(G, {"sites": [], "unreasoned": []})

        one = '[ -n "$X" ] || { echo "adopt: a one-line refusal with its reason"; exit 1; }\n'
        t1, c1 = build_refusal_tree("r1", {G: one, T: 'hit "$o" "adopt: a one-line refusal with its reason"\n'},
                                    floors=f"{G}:1:1")
        arm("S1: a script with no fail() helper is discovered by a reasoned exit 1",
            "refusal signature — 1 site(s) in 1 script(s): 1 armed, 0 waived; 0 unreasoned line(s) "
            "not graded\n[rc=0]", lambda: cmd_check(t1, c1))
        t2, _c2 = build_refusal_tree("r2", {G: 'if [ ! -f "$CONF" ]; then\n'
                                            '  echo "adopt: the topmost line of the block is the reason"\n'
                                            '  echo "  remedy: a second line that is not the reason"\n'
                                            '  exit 1\nfi\n'})
        arm("S1: a multi-line block's reason is its topmost print", "[rc=0]",
            lambda: 0 if [(s["cls"], s["sig"], s["src"]) for s in scan_one(t2)["sites"]]
            == [("reasoned", "adopt: the topmost line of the block is the reason", 2)] else 1)
        cap3 = ('if ! out=$(python3 mod.py 2>&1); then\n  # arm-signature: and the module said no here\n'
                "  printf '%s\\n' \"$out\"; status=1\nfi\n")
        t3, c3 = build_refusal_tree("r3", {G: cap3, T: 'hit "$o" "and the module said no here"\n'},
                                    floors=f"{G}:1:1")
        arm("S1: a capture-print status=1 is a delegated site signed by its marker", "[rc=0]",
            lambda: 0 if [(s["kind"], s["cls"], s["sig"]) for s in scan_one(t3)["sites"]]
            == [("status", "delegated", "and the module said no here")]
            and "1 armed, 0 waived" in run_check_text(t3, c3) else 1)
        t4, _c4 = build_refusal_tree("r4", {G: '  echo "adopt: a message above the command here"\n'
                                            '  write_skill || exit 1\n'})
        arm("S1: a command-conditioned exit 1 is delegated, not reasoned", "[rc=0]",
            lambda: 0 if [(s["cls"], s["sig"], s["key_sig"]) for s in scan_one(t4)["sites"]]
            == [("delegated", None, "write_skill || exit 1")] else 1)
        t5, _c5 = build_refusal_tree("r5", {G: 'if [ -z "$X" ]; then\n  exit 1\nfi\n'})
        arm("S1: an exit 1 whose block prints nothing is counted unreasoned, not a site", "[rc=0]",
            lambda: 0 if scan_one(t5) == {"sites": [], "unreasoned": [2]} else 1)
        t6, _c6 = build_refusal_tree("r6", {G: 'echo "never exit 1 here, it is quoted"\n'
                                            "# exit 1 in a comment\ncat <<EOF\nexit 1\nstatus=1\nEOF\n"
                                            "x=1  # status=1 in a trailing comment\n"
                                            "msg='a single-quoted exit 1'\n"})
        arm("S1: exit 1 inside quotes, a comment or a here-document body is not a site", "[rc=0]",
            lambda: 0 if scan_one(t6) == {"sites": [], "unreasoned": []} else 1)
        t7, _c7 = build_refusal_tree("r7", {f"{PFX}kit/z.test.sh": one,
                                            os.path.join("memory", "builds", "x", "repro.sh"): one})
        arm("S1: a *.test.sh and a script under the memory root are not discovered", "[rc=0]",
            lambda: 0 if scan_refusal_sites(t7, "memory") == ({}, []) else 1)
        t8, _c8 = build_refusal_tree("r8", {G: HELPER + '[ -n "$a" ] && { fail 1 "alpha branch message '
                                            'here"; exit 1; }\n'})
        arm("S1: a line carrying a fail call is signature 1's alone", "[rc=0]",
            lambda: 0 if scan_one(t8) == {"sites": [], "unreasoned": []} else 1)
        t9, c9 = build_refusal_tree("r9", {G: "# arm-signature: a declared text beside a derived one\n"
                                           '[ -n "$X" ] || { echo "adopt: a reasoned refusal message here"; '
                                           "exit 1; }\n"})
        arm("S1: a marker on a reasoned site is refused",
            f"{G}:1 carries an arm-signature marker above the REASONED site at line 2",
            lambda: cmd_check(t9, c9))
        t10, c10 = build_refusal_tree("r10", {G: "# arm-signature: a marker with no site below it\n"
                                              'echo "nothing refuses here"\n'})
        arm("S1: a marker no delegated site reads is refused",
            f"{G}:1 carries an arm-signature marker no delegated site reads", lambda: cmd_check(t10, c10))

        lone = '[ -n "$X" ] || { echo "adopt: a refusal no fixture stages"; exit 1; }\n'
        row = f"{G}\texit\t1\tadopt: a refusal no fixture stages\t"
        t11, c11 = build_refusal_tree("r11", {G: lone, T: "# no arm\n", PINF: row + "no fixture stages X\n"},
                                      floors=f"{G}:1:0")
        arm("S2: a waived row prints its reason", "[rc=0]",
            lambda: 0 if f"check-arms: waived {G}:1 exit — no fixture stages X" in run_check_text(t11, c11)
            and cmd_check(t11, c11) == 0 else 1)
        t12, c12 = build_refusal_tree("r12", {G: lone, T: "# no arm\n", PINF: row + "\n"},
                                      floors=f"{G}:1:0")

        def check_owed_refused():
            first = "with an EMPTY reason" in run_check_text(t12, c12)
            _w(os.path.join(t12, PINF), row + REASON_OWED + "\n")
            return 0 if first and f"with the placeholder {REASON_OWED}" in run_check_text(t12, c12) else 1
        arm("S2: an exit row with an empty reason is refused, and so is REASON-OWED", "[rc=0]",
            check_owed_refused)
        t13, c13 = build_refusal_tree("r13", {G: lone, T: 'hit "$o" "adopt: an inserted armed refusal"\n',
                                              PINF: row + "no fixture stages X\n"}, floors=f"{G}:2:1")

        def check_insert_keeps_key():
            _w(os.path.join(t13, G), '[ -f "$Y" ] || { echo "adopt: an inserted armed refusal"; exit 1; }\n'
               + lone)
            return cmd_check(t13, c13)
        arm("S2: a refusal inserted above a pinned site does not re-key its row", None,
            check_insert_keeps_key)
        NT = f"{PFX}kit/notest.sh"
        t14, c14 = build_refusal_tree("r14", {NT: lone, PINF: row.replace(G, NT) + "no suite exists\n"},
                                      floors=f"{NT}:1:0")

        def check_testless():
            clean = cmd_check(t14, c14) == 0
            _w(os.path.join(t14, NT), lone + '[ -f "$Y" ] || { echo "adopt: a second refusal unpinned"; '
               "exit 1; }\n")
            return 0 if clean and f"{PFX}kit/notest.test.sh is missing, so nothing can arm it" \
                in run_check_text(t14, c14) else 1
        arm("S2: a test-less script passes with every site pinned, and one unpinned site names the "
            "missing test", "[rc=0]", check_testless)
        t15, c15 = build_refusal_tree("r15", {G: lone, PINF: f"{G}\texit\t1\tonly four fields\n"},
                                      refusals="")
        arm("S3: the switch off grades no site, reads no exit row, and prints the OFF line",
            "so 1 refusal site(s) outside fail() go ungraded and 1 pin row(s) of kind exit or status "
            "were not read\n[rc=0]", lambda: cmd_check(t15, c15))
        t16, c16 = build_refusal_tree("r16", {G: lone}, refusals="yes")
        arm("S7: a switch value other than blank or graded is refused by name",
            "ARMS_REFUSALS is 'yes'", lambda: cmd_check(t16, c16))

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — check-arms: all arms held")
    return 0


def _capture(fn, root, conf, sink):
    """Run a check, echo its output (so `arm` can match), and keep the lines for a second assertion."""
    import contextlib
    import io

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(root, conf)
    text = buf.getvalue()
    sink.extend(text.split("\n"))
    print(text, end="")
    return rc


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return cmd_selftest()
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("check-arms: not a git repo")
        return 2
    conf = load_conf(root)
    try:
        if mode == "--check":
            return cmd_check(root, conf)
        if mode == "--report":
            return cmd_report(root, conf)
        if mode == "--emit-pin":
            return cmd_emit_pin(root, conf)
        if mode == "--emit-floors":
            return cmd_emit_floors(root, conf)
        print("usage: check-arms.py [--check|--report|--emit-pin|--emit-floors|--selftest]")
        return 2
    except Problem as exc:
        print(f"HYGIENE {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
