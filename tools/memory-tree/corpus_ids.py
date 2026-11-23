#!/usr/bin/env python3
"""corpus_ids.py — the corpus's id and path classifier: one grammar, one walk, every consumer.

    python <kit>/corpus_ids.py --report             # the derived numbers
    python <kit>/corpus_ids.py --check              # checks 13-16 as a gate
    python <kit>/corpus_ids.py --measure            # the rows each waiver home would key
    python <kit>/corpus_ids.py --list-unbound       # the `unbound-records` seed, asked of the hygiene gate
    python <kit>/corpus_ids.py --print-defined-ids  # the id grammar, then every defined id
    python <kit>/corpus_ids.py --selftest           # fixtures

Every number a gate here quotes is DERIVED from one walk rather than written into a document. A
classifier that lives in prose is a classifier nobody can check.

NOTHING HERE DECLARES A GRAMMAR OR A SET IT DOES NOT OWN.
  * the id grammar and the four anchor shapes come from this kit's `id_grammar.py`, which
    already derives them from `.memory-tree.conf` (PLAY-dOrderedCharter-18). A second grammar is the catalogue-drift class:
    upstream re-typed one alternation with its branches reordered and would never have noticed.
  * the append-only areas and the byte-capped index set come from `check-memory-hygiene.sh`, which
    already owns both — asked for through its print modes, never transcribed. Upstream transcribed
    the index set and had to guard the transcription in BOTH directions, because a shell-side
    addition the Python side still excludes leaves a file under no cap at all. When the shell's own
    checks 1 to 5 ran clean it hands `--print-index-set`'s answer down on stdin under
    `GOV_INDEX_SET_STDIN=1` (TOOL-aHastenedSweep-3).

THE GRAMMAR MODULE IS A LATE IMPORT, and its two states are kept apart: with both waiver homes absent
the grammar module is never imported and checks 13-15 are simply off, while a home PRESENT with the
module absent is a NAMED error — you armed a check whose grammar is not installed. Never a traceback,
and never the silent pass a bare `try: import` would produce. A home arms its checks by being present,
in any state but absent under the ledger factory's `read_home_state`, so an empty zero-bound home arms
them too (TOOL-dWitnessedBar-17 S4): `id-orphan-waiver.txt` arms 14, `corpus-path-unresolved.txt` 15,
and either arms 13.

  13  id-definition collision   one id claimed by two different build folders
  14  orphan ids                cited in the present tense but never defined; keyed waiver + stale guard
  15  dead repo-path citations  keyed registry, both sides and the count, on (file, path), NEVER a line number
  16  read-path accounting      the charter's own read set: every member byte-capped, and present
"""
from __future__ import annotations

import copy
import io
import os
import posixpath
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
HYGIENE = HERE / "check-memory-hygiene.sh"

# The grammar is this kit's own `id_grammar.py` (PLAY-dOrderedCharter-18), a sibling imported late
# so a tree with both waiver homes absent never imports it. GRAMMAR_DIR is a module global so the selftest can
# point it at a directory holding an absent or an outdated grammar; GRAMMAR_WHERE is the file a
# refusal names.
GRAMMAR_DIR = HERE
GRAMMAR_WHERE = "%s/id_grammar.py" % GRAMMAR_DIR.as_posix()

# TOOL-aHastenedSweep-4 S1: walk()'s per-process memo, OFF (None) at import. Only
# `gotchas.py --check-with-ids` sets it to {}, so its two verbs walk one unchanged tree once; every
# caller gets its own deep copy, so neither verb sees what the other did to its result.
_WALK_MEMO = None

# TOOL-dSpentCeiling-1 — the two keys this engine no longer reads. A conf that still declares one
# is ANNOUNCED, never refused: the shipped example declared READ_PATH_CEILING blank, so refusing on
# presence would red every adopter for doing nothing. Presence is an EXACT test only because both
# names are absent from load_conf's defaults below — keep them out of it.
RETIRED_KEYS = ("READ_PATH_CEILING", "READ_PATH_HEADROOM")

# The charter every adopter's conf ships pointing at. Named once, because `load_conf`'s default and
# check 16's not-asked test must agree and two spellings of one value is how they stop agreeing.
DEFAULT_CHARTER = "AGENTS.md"

# Do check 16's rules 3 and 4 RED, or merely print? False = print and leave the exit code alone.
#
# The grace exists because arming used to be a MODULE-WIDE switch over three pins, so in any tree that
# never declared the retired ceiling these rules have never run at all — gating them the moment the
# kit upgrades would red an adopter for a pre-existing condition on their first upgraded bar. A tree
# that DID declare the ceiling is not graced at all: see `_resolve_sink`.
#
# IT IS A DELIBERATE FLIP, NOT A VERSION COMPARISON, and that is a correction. The first cut keyed on
# `KIT_MEMORY_TREE_VERSION >= (2, 44)`, reasoning that the grace should end one release after the one
# that ships the retirement. MEASURED against this repo's actual cadence, that cannot express what it
# says: the engine went 2.41 -> 2.46 in under two days across concurrent branches, for reasons having
# nothing to do with this check, so any pin is overtaken by unrelated work before an adopter sees a
# release. Worse, two branches minted identical version literals from one base, so the flip would
# have arrived by MERGE ORDER. A version-keyed grace in a repo whose version moves this way is a
# grace that ends when nobody decided it should. Keying it on the engine version also made the engine
# version readable through a print mode BELOW the conf source, which handed a project conf a one-line
# spoof of the constant its own comment promises cannot be spoofed. That print mode is gone with it.
#
# The obligation to flip this is a backlog row, not a memory: TOOL-dSpentCeiling-7. Until it flips,
# every run SAYS the rules are reporting rather than gating.
READ_PATH_RULES_GATE = False

REGISTRY = "project/corpus-path-unresolved.txt"
WAIVER = "project/id-orphan-waiver.txt"

# What counts as a repo PATH: rooted at a real top-level directory. That is the only class where
# "does it exist" is a well-posed question. A loose "backticked token with a slash" measures package
# specifiers, git refs and bare fragments as dead citations — upstream counted 13 085 of them.
BACKTICKED = re.compile(r"`([^`\s]+)`")
MD_LINK_TARGET = re.compile(r"\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")  # a Markdown code fence's opening or closing line
ELISION = ("...", "…", "<", ">", "*", "{{")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv: str, cwd=None) -> str:
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def read(path) -> str:
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8", "replace").replace("\r\n", "\n")


# TOOL-aRepatriatedFork-9 -- the kit's ONE conf parser moved to `tree_lib.py`, so the sibling engines
# that need it stop importing THIS module (an adopter's own `corpus_ids.py` killed them on import).
# Re-imported here so every caller reaching it as `corpus_ids.parse_conf` keeps working.
sys.path.insert(0, str(HERE))
from tree_lib import parse_conf, parse_conf_line  # noqa: E402,F401  the kit's ONE conf parser
from tree_lib import scan_missing_citations  # noqa: E402  the `missing:` citation form
from tree_lib import read_rows_at, render_leg_line  # noqa: E402  the leg rows (TOOL-dTotalRecall-23)


def load_conf(root: str) -> dict:
    conf = {
        "MEMORY_ROOT": "memory", "DISCIPLINES": "", "FAMILIES": "", "CHARTER": DEFAULT_CHARTER,
        "READ_PATH_WAIVER": "",
        "DEAD_PATH_EXCLUDE": ".claude/worktrees/",
    }
    p = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(p):
        parse_conf(read(p), conf)
    return conf


def read_declared_keys(root: str) -> set:
    """The keys the project's conf ACTUALLY writes, as against `load_conf`'s merged defaults.

    Two callers need the distinction and neither can get it from `conf`: a retired key is announced
    on PRESENCE, and a `CHARTER` the adopter never declared is a tree with no mandatory reading yet
    rather than a mis-set one. Re-parsing one small file is cheaper than threading a second return
    value through every caller of `load_conf`, and it cannot drift from it — same file, same rule.
    """
    out = set()
    p = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(p):
        # TOOL-aWeldedTribunal-5 S3b. THE SIXTH READER, and it must agree with `load_conf` on keys
        # or the retired-key and undeclared-CHARTER checks disagree with the parser inside one file.
        # The docstring above claims it "cannot drift from it — same file, same rule", which the
        # `export ` handling would have made false the moment only one of the two learned it.
        for line in read(p).split("\n"):
            kv = parse_conf_line(line)
            if kv is not None:
                out.add(kv[0])
    return out


def armed(root: str, conf: dict) -> frozenset:
    """-> the checks among 13-15 their waiver homes arm (TOOL-dWitnessedBar-17 S4): 14 where
    `id-orphan-waiver.txt` is present, 15 where `corpus-path-unresolved.txt` is, 13 where either is,
    present meaning any state but `absent` under the ledger factory's `read_home_state`. Both absent
    is off, and the grammar is never imported; an empty home arms its checks, as a zero pin did.

    Check 16 is NOT on this switch and has not been since TOOL-dSpentCeiling-1. It was, and that was
    the defect: a module-wide switch meant removing one setting silenced a structural citation check.
    WHAT IT DOES NOT CHECK: that a present home reads as a ledger; `checks` reads it through the
    factory and names a row it refuses.
    """
    import legacy_ledger as LL  # noqa: E402  (deliberately late, as the kit's other siblings are)
    m = conf["MEMORY_ROOT"]
    on = set()
    if LL.read_home_state(os.path.join(root, m, WAIVER)) != "absent":
        on |= {13, 14}
    if LL.read_home_state(os.path.join(root, m, REGISTRY)) != "absent":
        on |= {13, 15}
    return frozenset(on)


# ------------------------------------------------------ the sibling kit's grammar, and its refusal
# THE CAUSE AND THE CURE BELONG TO THE CALLER; the kit-state sentence belongs here. `grammar()`'s own
# pair is true for the callers the waiver homes gate and false for the anchor route, which no file of
# this kit turns off: a refusal that prescribes removing two homes the caller never wrote is a no-op
# wearing the shape of a remedy, and a reader asking only that A remedy be named certifies it as
# correct. Both of the module's refusal points take the pair, because re-causing only the first would
# leave the home cure alive on the second — the path a STALE sibling kit takes.
_PIN_WHY = "a waiver home that arms checks 13-15 is present"
_PIN_CURE_ABSENT = ("Either restore it from the memory-tree kit or remove project/id-orphan-waiver.txt "
                    "and project/corpus-path-unresolved.txt to turn checks 13-15 off.")
_PIN_CURE_OUTDATED = "update it, or remove the two waiver homes to turn checks 13-15 off"
_ROUTE_WHY = "the anchor route was asked for"
_ROUTE_CURE_ABSENT = ("Restore it from the memory-tree kit; no conf value of this kit turns "
                      "the anchor route off.")
_ROUTE_CURE_OUTDATED = ("update it from the memory-tree kit, because no conf value of this kit "
                        "turns the anchor route off")


def _check_grammar_installed(why: str, cure_absent: str, cure_outdated: str):
    """The module's ONE raise for an id grammar module that is absent or too old, and its import.

    Two refusal points and TWO remedies, because the remedies genuinely differ — restore the module
    versus update it — and one string reused at both would be wrong at one of them. The cause is the
    caller's at both.

    Returns the imported module, so exactly one site puts GRAMMAR_DIR on `sys.path` and a caller
    that needs `grammar_for` has it without a second import.
    """
    if not (GRAMMAR_DIR / "id_grammar.py").is_file():
        raise Problem(
            "corpus_ids: %s, but the id grammar lives in %s, which is not installed. %s"
            % (why, GRAMMAR_WHERE, cure_absent)
        )
    if str(GRAMMAR_DIR) not in sys.path:
        sys.path.insert(0, str(GRAMMAR_DIR))
    import id_grammar  # noqa: E402  (deliberately late: see the module docstring)

    if not hasattr(id_grammar, "grammar_for"):
        raise Problem("corpus_ids: %s, but the installed %s predates grammar_for(root); %s"
                      % (why, GRAMMAR_WHERE, cure_outdated))
    return id_grammar


def grammar(root: str, why: str = _PIN_WHY, cure_absent: str = _PIN_CURE_ABSENT,
            cure_outdated: str = _PIN_CURE_OUTDATED):
    """The kit's id + anchor grammar, BOUND TO THIS ROOT — or a named error naming its module.

    `id_grammar.repo_root()` anchors on the module's own file, so the module-level constants describe the
    repo the kit is installed in and no chdir can move them. That is right for its CLI and wrong for
    a caller classifying a different tree: the alternation would come from the wrong repo and every
    id in the target would fail to match — silently, since a grammar that recognises nothing yields
    an empty classification and an empty classification is what a CLEAN corpus yields. Measured: the
    first selftest run here reported a clean scratch corpus while using this repo's family list.
    `grammar_for(root)` is the accessor added to the grammar module for exactly this, so there is
    still only ONE grammar.

    The cause and the two cures DEFAULT to the ones the waiver homes make true, and a caller the homes
    do not gate passes its own — `resolve_anchor` below is that caller, and inheriting these would tell
    it to remove two homes it never wrote.
    """
    return _check_grammar_installed(why, cure_absent, cure_outdated).grammar_for(root)


def resolve_anchor(root: str, E=None):
    """The kit's ONE public route from a repository root to the anchor predicate.

    Returns a callable taking ONE line and answering the record id that line DEFINES, or `None`.
    Composed from the two accessors that already exist — `grammar(root)` for the bundle and
    `_anchor` for the call into the sibling kit's `anchor_at` — so this kit still declares no second
    grammar, and no caller has to import a private name or re-type the bundle-to-answer step.

    `root` is explicit and has no default. The sibling kit's module-level grammar binds to the repo
    the KIT is installed in, which is the measured wrong-root class both modules' docstrings record,
    and a default here would put it straight back.

    `E` is a bundle the caller has ALREADY resolved; omitted, the route resolves its own. It exists
    for the one in-kit caller that holds one: `grammar(root)` re-reads the conf at that root on
    every call, so a walk handing over no bundle would pay a second resolve per walk, and a resolve
    inside the returned callable would pay one per LINE of a README. The bundle IS the binding to a
    root — it records `families` and `memory_root`, never the root it came from — so `root` goes
    unused when one is passed, and a mismatch is not checkable here at any price this route will pay.

    THE SIBLING KIT'S OWN REFUSAL IS MAPPED, never leaked. `grammar_for(root)` resolves the conf AT
    THAT ROOT and raises `ConfError` — a `RuntimeError` subclass and NOT this kit's `Problem` — when
    the root carries no `.memory-tree.conf`, declares no `MEMORY_ROOT`, or declares no usable
    `FAMILIES`. None of this module's `except Problem` handlers catches that, so it escaped as a
    traceback out of a module whose own docstring forbids one. An arbitrary target root is the ONE
    input this route exists to accept, and those three declarations are exactly what a tree this kit
    did not write may lack.

    Never `None` for an absent kit: `None` is also what a line that anchors nothing returns, so
    every caller would read an uninstalled kit as a clean corpus. A caller that wants a SKIP rather
    than a refusal catches `Problem` and prints one naming the arm and the kit.
    """
    if E is None:
        try:
            E = grammar(root, why=_ROUTE_WHY, cure_absent=_ROUTE_CURE_ABSENT,
                        cure_outdated=_ROUTE_CURE_OUTDATED)
        except Problem:
            raise
        except RuntimeError as exc:
            # `ConfError` is matched BY NAME, and the obvious alternative was measured and rejected:
            # reaching the class through the grammar module in `sys.modules` raised KeyError when
            # that module refused DURING its own import, so the look-up that was supposed to catch
            # it became a second traceback. A RuntimeError that
            # is NOT that class is re-raised untouched rather than re-labelled with a cause it does
            # not have.
            if type(exc).__name__ != "ConfError":
                raise
            raise Problem(
                "corpus_ids: %s over %s, and the id grammar refused that root: %s"
                % (_ROUTE_WHY, root, str(exc).split("\n")[0])
            ) from None
    return lambda line: _anchor(E, line)


def load_backlog():
    """The parser kit-mate, imported LAZILY and for one reason: it owns the backlog layout.

    Lazy, and not a module-level import, because `row_grammar.py` imports `parse_conf` from THIS
    module and the parser module is where the two of them would meet — a module-level import each
    way is a cycle one edit away. Importing inside the accessor also keeps the cost off every caller
    that never asks: `--print-defined-ids` and check 16 do not read the backlog layout at all.

    `HERE` on the path rather than a package-relative import, because this kit is copy-installed as
    a flat directory and is run as a script from an arbitrary cwd.
    """
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import backlog  # noqa: E402  (deliberately late: see above)

    return backlog


def read_backlog_conf(conf: dict):
    """`BACKLOG_MODE` and `ASK_CUTOFF`, through the parser module's ONE reader.

    NOT a second reader. An unrecognised mode must RAISE on both sides — the shell engine aborts at
    exit 2 before it ever delegates here, and this module refuses the same value when it is run
    standalone, so a typo cannot half-migrate a tree by reaching one reader and not the other. The
    parser's own exception is re-raised as this module's, because `main()` promises a named line and
    never a traceback, and `except Problem` here would not catch a class from over there.
    """
    bk = load_backlog()
    try:
        return bk.read_conf(conf)
    except bk.Problem as exc:
        raise Problem(f"corpus_ids: {exc}") from None


# The `resolve_bash_py` block is carried once in `tree_lib.py` (TOOL-dWitnessedBar-57 S7), and
# `resolve_bash` below is this module's adapter over its `scan_bash`.
from tree_lib import scan_bash  # noqa: E402  the kit's one resolve_bash_py block


def resolve_bash() -> str:
    """The bash that shares THIS filesystem — not whatever the name `bash` resolves to.

    MEASURED on a Windows node: subprocess resolving the bare name `bash` goes through the Windows
    loader, which finds the System32 WSL launcher or the WindowsApps alias before git-bash. WSL then
    sees a DIFFERENT filesystem: the failure reads "/bin/bash: C:/a/b: No such file or directory"
    for a file that plainly exists, and a relative path resolves under /mnt/c/ instead. This is the
    documented trap — Python subprocess resolving a different bash on a Windows node — and the
    remedy is to name the EXECUTABLE rather than the command. GOV_BASH overrides.

    A candidate is accepted only if it RUNS. Existing on disk is not evidence — that is the same
    mistake one interpreter over that the python side made with the Microsoft Store `python3` stub,
    which answers `command -v` and exits 9009 without executing anything (see
    <prefix>/lib/resolve-python.sh). An override that is SET and unusable is a named failure here too,
    never a silent fall-through to something else. The rule is the one `resolve_bash_py` block, in
    `tree_lib.py` (TOOL-dWitnessedBar-26, -57 S7); its refusal is this module's Problem.
    """
    found, _tried, refusal = scan_bash()
    if not found:
        raise Problem("corpus_ids: " + refusal)
    return found


def ask_shell(flag: str, root: str) -> str:
    """Ask check-memory-hygiene.sh for a set IT owns. One direction only — the print modes return
    before check 1, so there is no recursion back into this module."""
    if not HYGIENE.is_file():
        raise Problem("corpus_ids: %s is missing — it owns the sets this module asks for" % HYGIENE)
    sh = resolve_bash()
    try:
        out = subprocess.run([sh, HYGIENE.as_posix(), flag], cwd=root, capture_output=True, text=True, encoding="utf-8")
    except OSError as exc:
        # A bash that cannot be LAUNCHED raises before any return code exists. Left unhandled this is
        # a traceback out of a hygiene gate — every failure here is named, including this one.
        raise Problem(f"corpus_ids: cannot run '{sh}' ({exc.strerror or exc}); set GOV_BASH to a bash "
                      f"that shares this filesystem") from None
    if out.returncode != 0:
        raise Problem("corpus_ids: `%s %s` failed: %s"
                      % (HYGIENE.name, flag, out.stderr.strip() or out.stdout.strip()))
    # A PRINT MODE THAT PRINTS FINDINGS ANSWERED THE WRONG QUESTION. `--print-index-set` is computed
    # below checks 1-5, so a structure failure earlier in that script lands on this stdout and every
    # line of it becomes a member of `capped` — which makes check 16 rule 3 pass by finding nothing.
    # A probe that cannot answer says so rather than returning a reassuring set.
    if any(l.startswith("HYGIENE ") for l in out.stdout.split("\n")):
        raise Problem("corpus_ids: `%s %s` answered with findings rather than a set, so the set it "
                      "returned cannot be trusted — fix the earlier check first"
                      % (HYGIENE.name, flag))
    return out.stdout


# ------------------------------------------------------------------------------------ the one walk
# A trailing `:12` or `:12-30` on a cited path. Cut ONLY for the advisory population below: cutting it
# inside check 15 proper would move a gated verdict, which is the open ask TOOL-aProbedToolkit-17.
LINE_LOCATOR = re.compile(r":\d+(?:-\d+)?$")


def read_live_readmes(root: str, m: str, tracked_set: set) -> tuple:
    """`(readmes, links)`: the tracked build READMEs `<m>/LIVE.md` links, resolved relative to that
    file exactly as walk() resolves its relative links, and how many build links it read.

    A build folder is a record of a moment and stays outside check 15, but a LIVE build's README is
    what sessions read to orient, so its dead citations are REPORTED, never gated (TOOL-aMendedFleet-24).
    An untracked `LIVE.md` is an adopter that renders no index: not asked, so `(set(), 0)`.
    """
    live = m + "/LIVE.md"
    if live not in tracked_set:
        return set(), 0
    build_link = re.compile(r"^" + re.escape(m) + r"/builds/([^/]+)/")
    readmes, links = set(), 0
    for tok in MD_LINK_TARGET.findall(read(os.path.join(root, live))):
        rel = posixpath.normpath(posixpath.join(m, tok))
        b = build_link.match(rel)
        if not b:
            continue
        links += 1
        if rel == f"{m}/builds/{b.group(1)}/README.md" and rel in tracked_set:
            readmes.add(rel)
    return readmes, links


def walk(root: str, conf: dict) -> dict:
    # The memo lives INSIDE walk, never as a wrapper round a renamed body: _walk_continues reads this
    # function's own source, and a wrapper would empty its population (TOOL-aHastenedSweep-4).
    memo_key = None
    if _WALK_MEMO is not None:
        memo_key = (root, tuple(sorted(conf.items())))
        if memo_key in _WALK_MEMO:
            return copy.deepcopy(_WALK_MEMO[memo_key])
    # The bundle, resolved ONCE: an undecodable or unreadable path is harvested from `read` with it below,
    # and `extract_ids` hands it to the kit's one anchor route.
    E = grammar(root)
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
    tracked_set = set(tracked)
    roots = _roots(tracked_set)   # once per walk: _roots is pure and the loop never changes tracked_set (TOOL-aHastenedSweep-2 S2)
    corpus = [p for p in tracked if p.startswith(m + "/")]
    build_re = re.compile(r"^" + re.escape(m) + r"/builds/([^/]+)/")

    append_only = re.compile(ask_shell("--print-append-only-ere", root).strip() or r"(?!)")
    excluded = tuple(x for x in conf.get("DEAD_PATH_EXCLUDE", "").split() if x)
    bconf = read_backlog_conf(conf)
    builds_mode = bconf.mode == "builds"
    # THE PRESENT-TENSE CORPUS, one list and one substitution. Under `builds` the file at
    # `backlog/<FAMILY>.md` is a GENERATED view whose every path token is derived text — grading it
    # would red a citation no author wrote and no author can repair — while the ask itself, with the
    # paths it cites, moves into `builds/<slug>/BACKLOG.md`. So the member is REPLACED IN PLACE
    # rather than dropped: dropping it alone would silently take every graded ask path token out of
    # check 15, which is a check losing its subject and reporting green (owner ruling D9).
    _present = [r"DECISIONS\.md", r"README\.md", r"HYGIENE\.md", r"TEMPLATE-SPEC\.md", r"LIVE\.md",
                "backlog/", "ledger/", "project/", "guides/"]
    if builds_mode:
        _present[_present.index("backlog/")] = r"builds/[^/]+/BACKLOG\.md"
    present = re.compile(r"^" + re.escape(m) + r"/(?:" + "|".join(_present) + r")")

    # CHECK 13's SKIP, armed only under `builds`. The grammar is the PARSER module's, built from the
    # family tokens the id grammar above already derived — never a second derivation, and never a
    # second spelling of the ask row.
    bk = load_backlog() if builds_mode else None
    ask_grammar = bk.build_grammar(E.families) if builds_mode else None
    cutoff_armed = bk.check_cutoff_armed(bconf) if builds_mode else False
    unarmed_asks = 0

    defs: dict = {}          # id -> set(paths)
    def_builds: dict = {}    # id -> set(build slugs)
    cites: dict = {}         # id -> set(paths)
    missing: dict = {}       # id -> set(paths) citing it in the `missing:` form, every file read
    missing_now: dict = {}   # the same, present-tense files only — check 14's stale clause
    dead: dict = {}        # (citing file, cited path) -> [count, first line]
    advisory: dict = {}      # the same shape, for live build READMEs — reported, never gated
    live_readmes, live_links = read_live_readmes(root, m, tracked_set)

    waiver = m + "/" + WAIVER
    # TOOL-dTotalRecall-23 S4: each file's path-independent harvest is its `id-harvest` leg row where the
    # index holds its unchanged blob, else `extract_ids` over its text; the classification by path stays here.
    harvests, legs = read_rows_at(root, corpus, "id-harvest")
    for p in corpus:
        harvest = harvests[p]
        if "lines" not in harvest:
            # undecodable or unreadable: read by `read` as before, which replaces a bad byte or raises
            harvest = extract_ids(read(os.path.join(root, p)), E)
        b = build_re.match(p)
        # A build's own ask file, and only under `builds`. Its rows are the one anchored line in this
        # corpus that is a FILING rather than a CLAIM, and the test is the whole path so a
        # `BACKLOG.md` somewhere else is untouched.
        asks_here = bool(b) and builds_mode and p.rsplit("/", 1)[-1] == "BACKLOG.md"
        # A citation is a claim about NOW only in the present-tense corpus. `builds/` is a record of
        # a moment — a spec proposing to write a file is a plan, not a broken pointer — and an
        # append-only area cannot legally be repaired anyway. ONE test, decided here once per file,
        # and read by BOTH check 14 (ids) and check 15 (paths): TOOL-aRepatriatedFork-39. Check 14
        # used to count ids cited anywhere, so an adopter's rotated archives and historical builds
        # produced 330 orphans where the present-tense corpus held 4 — two answers to one question.
        now = bool(present.match(p)) and not append_only.match(p)
        # A live build README is ADMITTED to the path harvest only: no id citation, no check 15 key.
        admitted = not now and p in live_readmes
        sink = dead if now else advisory
        for lineno, marked, anchor, line, ids, toks in harvest["lines"]:
            for i in marked:
                missing.setdefault(i, set()).add(p)
                if now:
                    missing_now.setdefault(i, set()).add(p)
            if anchor:
                defs.setdefault(anchor, set()).add(p)
                claims = bool(b)
                # AN ASK FILED BEFORE THE CUTOFF IS NOT ITS FOLDER'S CLAIM ON THE ID (owner ruling
                # D12-g). Migrated rows carry ids whose records already live in another build's
                # folder, so counting the ask as a second claim would red every one of them; an ask
                # filed on or after the cutoff DOES claim, so a new foreign anchor is still a
                # collision. The row stays in `defs` either way, so no legacy ask becomes an orphan
                # under check 14 — this touches `def_builds` and nothing else.
                if claims and asks_here:
                    row = bk.extract_row(line, ask_grammar)
                    if row is not None and row.cls == "ask":
                        if not cutoff_armed:
                            # V15 (blank) or V16 (not a DATE): a string compare against an unusable
                            # cutoff is not a date compare, so EVERY ask row is skipped and the note
                            # below names the verdict. Comparing anyway would read a blank cutoff as
                            # the empty string, under which every ask is "filed after it" and the
                            # legacy foreign anchors red for one misconfiguration that is already red.
                            claims = False
                            unarmed_asks += 1
                        elif row.value < bconf.cutoff:
                            claims = False
                if claims:
                    def_builds.setdefault(anchor, set()).add(b.group(1))
            if not now and not admitted:
                continue
            # The waiver is check 14's INPUT, not a citation: counted as one, every row kept its own
            # id alive and the stale guard could never fire for an id nothing else cites.
            if now and p != waiver:
                for i in ids:
                    cites.setdefault(i, set()).add(p)
            for tok in toks:
                cited = (LINE_LOCATOR.sub("", tok) if admitted else tok).rstrip("/")
                if any(e in cited for e in ELISION) or "/" not in cited:
                    continue
                # A token counts as a repo-path citation two ways. (1) Its first segment is a real
                # top-level directory — the ordinary case. (2) It is not, but the token is the TAIL of
                # a tracked path, which means it names a real file of this repo written at the WRONG
                # PREFIX. Case 2 exists because case 1 alone made this check structurally blind to
                # the failure it is most needed for: a kit installed at `<prefix>/<kit>/` scaffolds
                # documents citing `<kit>/…`, whose first segment is not a top-level directory, so
                # every one of those citations was skipped before it could be judged. Measured on a
                # `<prefix>/` install: seven dead kit paths in a scaffolded `HYGIENE.md` and the gate
                # exited 0. A tail match is deliberately narrow — an unresolvable token that matches
                # nothing tracked is still prose, not a finding.
                if cited.split("/", 1)[0] + "/" not in roots:
                    # RELATIVE TO THE CITING FILE first. Inside the memory tree the ordinary link
                    # shape is `builds/<slug>/README.md` written from `LIVE.md`, and it is correct.
                    # Measured on the first run of the tail rule below: 17 such links reported dead,
                    # 16 of them generated by this kit's own index writer. A rule that reds the
                    # artifact its own generator produces is wrong, not strict.
                    rel = posixpath.normpath(posixpath.join(posixpath.dirname(p), cited))
                    if rel in tracked_set or any(x.startswith(rel + "/") for x in tracked_set):
                        continue
                    tail = "/" + cited
                    if not any(x.endswith(tail) for x in tracked_set):
                        continue
                # NOT repo CONTENT. A checkout location is not a claim about what this repo holds,
                # and no resolution rule can express that: resolution here never touches the
                # filesystem — it is membership in `git ls-files` plus a prefix scan over the same
                # index — so such a path classifies as dead identically on every node. The question
                # is about meaning, not existence, so the answer is DECLARED in the conf.
                if any(cited.startswith(x) for x in excluded):
                    continue
                if cited in tracked_set or any(t.startswith(cited + "/") for t in tracked_set):
                    continue
                # NO SHAPE TEST. Every rooted, non-elided, unresolved token is a finding, file-shaped
                # or not: a citation naming a DIRECTORY is exactly as broken as one naming a file when
                # neither resolves — the flatten left four in the live ledger and the pre-V8 harvest
                # could not see one. What stood here was
                #     is_file_shaped = <B or something>;  is_dir_shaped = <not B or something>
                #     if not is_file_shaped and not is_dir_shaped: continue
                # with B = `"." in basename`, i.e. ¬(B ∨ ¬B) — identically False, filtering nothing.
                # Measured: 0 of 1550 exhaustively-generated token shapes reached the `continue`.
                # Deleted rather than kept as documentation, because executable dead code is plumbing
                # a later edit will trust; the reachability arm in the selftest is what stops it
                # coming back.
                key = (p, cited)
                if key in sink:
                    sink[key][0] += 1
                else:
                    sink[key] = [1, lineno]

    # ONE LINE, NAMING THE VERDICT, and only when the skip actually fired over a real population. A
    # gate that silently stops grading is the shape this kit refuses; a count of zero would be noise
    # on every `shards` tree, so the note exists exactly where coverage was lost.
    notes = []
    if unarmed_asks:
        v = bconf.verdicts[0]
        notes.append(f"corpus_ids: check 13 skipped {unarmed_asks} ask row(s) — V{v.code}: {v.text}")
    # Non-gating, and the shell's offender keying skips a line opening `HYGIENE advisory `
    # (TOOL-aMendedFleet-23). An EMPTY population announces itself rather than reading as clean.
    if live_links and not live_readmes:
        notes.append(f"advisory check 15: {m}/LIVE.md links {live_links} build(s) and none resolves to "
                     f"a tracked build README, so the live-README population is empty and graded nothing")
    elif advisory:
        held = len({f for f, _ in advisory})
        notes.append(f"advisory check 15: {len(advisory)} dead repo-path citation(s) in {held} of "
                     f"{len(live_readmes)} live build README(s) — corpus_ids.py --report lists them")
    w = {
        "tracked": tracked_set, "corpus": corpus, "defs": defs, "def_builds": def_builds,
        "cites": cites, "missing": missing, "missing_now": missing_now, "dead": dead, "advisory": advisory, "root": root, "conf": conf, "m": m,
        "notes": notes, "legs": legs,
    }
    if memo_key is None:
        return w
    _WALK_MEMO[memo_key] = w
    return copy.deepcopy(w)


def derive_id_params(root):
    """The `id-harvest` reader's params (TOOL-dTotalRecall-23 S2): `(key, bundle)`, the bundle `grammar`
    builds for `root` and, as the key, its `ID` pattern and its four anchor patterns, so every conf input
    the grammar folds in moves the reader's version."""
    E = grammar(root)
    return "\n".join([E.ID] + [a.pattern for a in E.anchors]), E


def extract_ids(text, grammar):
    """The `id-harvest` leg reader (TOOL-dTotalRecall-23 S4), `walk`'s per-line loop with nothing of a path:
    `{"lines": [[lineno, missing ids, anchor, line, cited ids, tokens], ...]}` for each line holding any,
    each read from the line with its `missing:` forms blanked: the ids it marks `missing:`, the id it
    defines with the line's text (check 13's ask row reads it), else None twice, the ids it cites, and its
    backticked and link-target tokens in order, repeats kept. `{"undecodable": true}` for no text."""
    if text is None:
        return {"undecodable": True}
    # The kit's one route from a bundle to an answer, HANDED the bundle: `resolve_anchor(root)` with no
    # bundle would re-resolve the conf a second time per walk, the cost the route's optional bundle avoids.
    anchor_of = resolve_anchor(None, grammar)
    h1_re = re.compile(r"^#\s+[`*]*(" + grammar.ID + r")\b")
    lines = []
    # A FENCED BLOCK HOLDS NO HEADING: a `#` comment line inside ``` or ~~~ is code, so it is never
    # an H1 anchor claiming an id for this folder; citations in it still count.
    fence = ""
    for lineno, line in enumerate(text.split("\n"), 1):
        opener = FENCE_RE.match(line)
        if opener and (not fence or (opener.group(1)[0] == fence[0] and len(opener.group(1)) >= len(fence))):
            fence = "" if fence else opener.group(1)
        # The `missing:` form (TOOL-aMendedFleet-26) is blanked out of the line before anything
        # reads it, so a marked id is neither a citation for check 14 nor an anchor.
        marked, line = scan_missing_citations(line, grammar.ID_RE)
        anchor = anchor_of(line)
        if anchor is None:
            h = h1_re.match(line) if not fence else None
            anchor = h.group(1) if h else None
        ids = list(dict.fromkeys(mm.group(0) for mm in grammar.ID_RE.finditer(line)))
        toks = BACKTICKED.findall(line) + MD_LINK_TARGET.findall(line)
        if marked or anchor or ids or toks:
            lines.append([lineno, list(marked), anchor, line if anchor else None, ids, toks])
    return {"lines": lines}


def _anchor(E, line):
    """The grammar bundle carries its own anchor patterns; `anchor_at` takes it as `g`."""
    import id_grammar

    return id_grammar.anchor_at(line, E)


def _roots(tracked_set) -> set:
    """Real top-level directories, derived — never a hardcoded list that an adopter has to edit."""
    return {p.split("/", 1)[0] + "/" for p in tracked_set if "/" in p}


# ------------------------------------------------------------------------------------- the read set
def read_set(w: dict) -> tuple:
    """Files the charter points a session at, DERIVED from the charter's own text through three
    independent token arms. Never enumerated: upstream hand-listed it five times and every revision
    missed something."""
    root, conf, tracked = w["root"], w["conf"], w["tracked"]
    charter = conf["CHARTER"]
    if charter not in tracked:
        raise Problem(f"corpus_ids: CHARTER '{charter}' is not a tracked file — check 16 has no source")
    text = read(os.path.join(root, charter))
    # READ_PATH_PREFIX: only charter citations INSIDE the memory root count. The charter also names
    # every gate script it runs, and those are code, not a read path — folding them in would make the
    # population 32 files of which 30 need waiving, and a rule whose whole population is waived is a
    # rule with no signal. The byte caps this check cross-references govern the memory tree, so the
    # memory tree is the population.
    prefix = conf["MEMORY_ROOT"].rstrip("/") + "/"
    bare = re.compile(r"(?<![`(\w./-])(" + re.escape(prefix) + r"[^\s`)\]]+)")
    members, absent = set(), set()
    for arm in (BACKTICKED, MD_LINK_TARGET, bare):
        for tok in arm.findall(text):
            cand = tok.rstrip("/").rstrip(".,;:")
            if not cand.startswith(prefix):
                continue
            if cand in tracked:
                if os.path.isfile(os.path.join(root, cand)):
                    members.add(cand)
                else:
                    absent.add(cand)          # tracked but missing: check 16 rule 4 owns this
    return sorted(members), sorted(absent)


def check_read_path(root: str, conf: dict) -> tuple:
    """Check 16 — the charter's read path. STRUCTURAL: it runs whenever the conf is loadable.

    Behind no pin, deliberately, and behind no NEW pin either: its population comes from `CHARTER`,
    which SHIPS WITH A VALUE, so a blank resolves FORWARD rather than off. That is the ratified
    pattern this tree already uses for `SPEC10_CUTOFF`, not a new convention, and minting a fourth
    blankable pin would be the defect TOOL-dSpentCeiling-1 exists to close, renamed.

    The BUDGET this check used to carry is gone. Check 6 already caps every member by class, so the
    sum was a second bound over an already-bounded population; it bound earlier only because it added
    six incommensurable things together, and across seventeen days and twenty-seven movements it
    never once caused a trim. The exhibit is in `memory/builds/dSpentCeiling/`.

    Calls neither `walk()` nor `grammar()`: `read_set` needs only root, conf and tracked, so the
    grammar module stays a CONDITIONAL import rather than one every run of check 16 pays for.

    Returns `(bad, notes)`. Notes print and do not touch the exit code.
    """
    bad, notes = [], []
    written = read_declared_keys(root)
    for k in RETIRED_KEYS:
        if k in written:
            notes.append(f"check 16: NOTE {k} is declared in .memory-tree.conf and is no longer "
                         f"read — the read-path budget was retired, and check 6's per-member byte "
                         f"caps are the bound. Delete the line.")

    charter = conf["CHARTER"]
    tracked = {p for p in run("git", "ls-files", cwd=root).split("\n") if p}
    found = []
    if charter not in tracked:
        # The shipped `.memory-tree.conf.example` DECLARES CHARTER="AGENTS.md" and the scaffolder
        # copies it verbatim without writing that file, so keying only on `not in written` never
        # fired for a real adopter — it fired only for a conf hand-edited into a state the installer
        # does not produce. The default value is therefore treated as undeclared: an adopter who
        # means something else says something else.
        if "CHARTER" not in written or charter == DEFAULT_CHARTER:
            # NOT ASKED, and it announces itself. A freshly scaffolded tree declares no CHARTER and
            # has no AGENTS.md yet: it has no mandatory reading, which is a REAL state rather than a
            # defect, and refusing it would red every adopter on the day they adopt. Measured — this
            # is exactly what `adopt-memory-tree.sh --scaffold` produces.
            notes.append(f"check 16: not asked — this tree declares no CHARTER and the default "
                         f"'{charter}' is not tracked, so there is no read path to grade yet")
            return bad, notes
        # A FINDING plus an early return, never a raise. Raising here escaped `checks()` and made
        # main() print one line, so a mis-set CHARTER replaced every check-13/14/15 finding in the
        # run with itself. This check owns its own failure and lets its siblings report.
        found.append(f"check 16: CHARTER '{charter}' is declared and is not a tracked file, so the "
                     f"read path has no source and rules 3 and 4 graded nothing")
        return _resolve_sink(written, bad, notes, found)

    members, absent = read_set({"root": root, "conf": conf, "tracked": tracked})
    # HANDED DOWN by check-memory-hygiene.sh when its own checks 1 to 5 ran clean, decoded and
    # newline-translated as the ask_shell capture is, so both routes parse to the same members.
    if os.environ.get("GOV_INDEX_SET_STDIN") == "1":   # handed down by check-memory-hygiene.sh
        raw = sys.stdin.buffer.read().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    else:
        raw = ask_shell("--print-index-set", root)
    capped = {l for l in raw.split("\n") if l.strip()}
    waived = set(conf["READ_PATH_WAIVER"].split())
    for p in members:                                                              # rule 3
        if p not in capped and p not in waived:
            found.append(f"check 16 rule 3: {charter} points a session at {p}, which is under "
                         f"no byte cap and not in READ_PATH_WAIVER — nothing watches it")
    for p in absent:                                                               # rule 4
        # NOT a duplicate of check 12, whatever this line used to claim. Check 12's tracked-but-absent
        # arm is built from a grep restricted to builds/*/spec/*.md, and `index_set()` filters absent
        # files out of check 6 before it measures. For a charter-cited guide or a generated index this
        # is the ONLY detector, and the comment that said otherwise was an invitation to delete it.
        found.append(f"check 16 rule 4: {p} is tracked but absent from the worktree, so the charter "
                     f"points a session at a file that is not there")

    return _resolve_sink(written, bad, notes, found)


def _resolve_sink(written: set, bad: list, notes: list, found: list) -> tuple:
    """Route this check's findings to the gating list or the reporting one. ONE decision, in one
    place, so the charter arm and the two rules cannot drift apart on whether the grace applies.

    THE GRACE DOES NOT REACH A TREE THAT DECLARED A RETIRED KEY. Declaring `READ_PATH_CEILING` is
    proof rules 3 and 4 were already armed and green there, so nothing in such a tree is
    pre-existing and gating it is honest. Without this the grace SUSPENDED a live check in every
    repo that had one — including the repo that wrote it — which is a coverage loss wearing a
    courtesy's clothes.
    """
    if found and not (written & set(RETIRED_KEYS)) and not READ_PATH_RULES_GATE:
        # THE GRACE ANNOUNCES ITSELF. A rule that is not gating and does not say so is
        # indistinguishable from a rule that found nothing.
        notes.append(f"check 16: the {len(found)} finding(s) below are REPORTED, not gated — this "
                     f"tree never declared the retired read-path ceiling, so these rules have never "
                     f"run here. They gate when READ_PATH_RULES_GATE flips. Fix them before then.")
        notes.extend(found)
    else:
        bad.extend(found)
    return bad, notes


# ----------------------------------------------------------------------------------------- registry
def parse_registry(root: str, m: str) -> dict:
    """-> {(citing file, cited path): (count, line)}: the `corpus-path-unresolved` ledger, keyed by
    `path` and `cited` (TOOL-dWitnessedBar-17 §4), read through the factory this kit carries at arity 2.
    A refused row, the factory's `duplicate` among them, is a Problem as `parse_waiver` raises one."""
    import legacy_ledger as LL  # noqa: E402  (deliberately late, as the kit's other siblings are)
    p = os.path.join(root, m, REGISTRY)
    if not os.path.isfile(p):
        return {}
    rows, bad = LL.read_rows(p, 2)
    if bad:
        raise Problem(f"{m}/{REGISTRY}: {LL.render_malformed(bad[0])}")
    return {key: (row[0], row[2]) for key, row in rows.items()}


def parse_waiver(root: str, m: str) -> list:
    """The waived ids: a ledger population keyed by `id` (TOOL-dWitnessedBar-16 S4), read through the
    factory this kit carries, each row's reason the conversion record's. A refused row is a Problem."""
    import legacy_ledger as LL  # noqa: E402  (deliberately late, as the kit's other siblings are)
    p = os.path.join(root, m, WAIVER)
    if not os.path.isfile(p):
        return []
    rows, bad = LL.read_rows(p, 1)
    if bad:
        raise Problem(f"{m}/{WAIVER}: {LL.render_malformed(bad[0])}")
    return [key[0] for key in rows]


# ------------------------------------------------------------------------------------------- checks
def checks(w: dict) -> list:
    conf, m, root = w["conf"], w["m"], w["root"]
    bad = []

    # 13 — one id claimed by two different BUILD FOLDERS. Deliberately NOT "defined twice": a
    # decision-log row and its spec's H1 both anchor the same id by design (the index points at the
    # record), and treating that as a collision would red 10 of this corpus's ids on day one.
    for i, slugs in sorted(w["def_builds"].items()):
        if len(slugs) > 1:
            bad.append(f"check 13: id {i} is claimed by {len(slugs)} build folders: {', '.join(sorted(slugs))}")

    # 14 — orphan ids, with a keyed waiver and a stale-entry guard. `cites` holds the PRESENT-tense
    # citations only, the population check 15 grades (walk()'s `now`), so this set, `--report`'s and the
    # rows `--measure` prints are one population. The waiver's shrink is `ratchet (never gains)`'s.
    on = armed(root, conf)
    if 14 in on:
        waived = parse_waiver(root, m)
        orphans = sorted(set(w["cites"]) - set(w["defs"]))
        for i in orphans:
            if i not in waived:
                bad.append(f"check 14: id {i} is cited but never defined, and is not in {m}/{WAIVER}")
        # The `missing:` form's stale clause: a present-tense file declaring a gap the corpus has
        # since filled. A record of a moment is not graded — the id was missing when it was written.
        for i, citers in sorted(w["missing_now"].items()):
            if i in w["defs"]:
                bad.append(f"check 14: id {i} is marked missing but defined — cited missing: in "
                           f"{', '.join(sorted(citers))}, defined in {', '.join(sorted(w['defs'][i]))}")
        for i in waived:
            if i in w["defs"]:
                bad.append(f"check 14: {m}/{WAIVER} waives {i}, which now resolves — stale row")
            elif i not in orphans:
                bad.append(f"check 14: {m}/{WAIVER} waives {i}, which no present-tense file cites — stale row")

    # 15 — dead repo-path citations, both sides and the count. The key is (citing file, cited path)
    # with a COUNT, never a line number: a line number moves whenever anything above the citation is
    # edited, so a line-keyed registry reds on edits that have nothing to do with it, and a gate whose
    # steady state is red gets bypassed. A duplicate row is the factory's refusal, raised by
    # `parse_registry`; the registry's shrink is `ratchet (never gains)`'s (TOOL-dWitnessedBar-17 §4).
    if 15 in on:
        rows = parse_registry(root, m)
        measured = {k: v for k, v in w["dead"].items()}
        for (f, cited), (count, ln) in sorted(rows.items()):
            if (f, cited) not in measured:
                bad.append(f"check 15: {m}/{REGISTRY}:{ln}: {f} -> {cited} no longer resolves to nothing — the citation was repaired; delete the row")
            elif measured[(f, cited)][0] != count:
                bad.append(f"check 15: {m}/{REGISTRY}:{ln}: {f} -> {cited} occurs {measured[(f, cited)][0]} time(s), row says {count}")
        for key, (count, ln) in sorted(measured.items()):
            if key not in rows:
                bad.append(f"check 15: {key[0]}:{ln} cites {key[1]}, which resolves to nothing and has no row in {m}/{REGISTRY}")
    # 16 lives in check_read_path(), OUTSIDE this function and outside armed(): it needs neither
    # walk() nor the grammar, and putting it here is what tied a structural check to a deletable pin.
    return bad


# ------------------------------------------------------------------------------------------- report
def cmd_report(root: str, conf: dict) -> int:
    w = walk(root, conf)
    orphans = sorted(set(w["cites"]) - set(w["defs"]))
    coll = {i: s for i, s in w["def_builds"].items() if len(s) > 1}
    print(f"ids defined      : {len(w['defs'])}")
    print(f"ids cited        : {len(w['cites'])}")
    print(f"orphan ids       : {len(orphans)}  {orphans}")
    print(f"missing-form ids : {len(w['missing'])}  {sorted(w['missing'])}")
    print(f"build collisions : {len(coll)}  {coll}")
    print(f"dead path cites  : {len(w['dead'])}")
    for note in w["notes"]:
        print(note)
    for k, v in sorted(w["dead"].items()):
        print(f"    {k[0]}:{v[1]} -> {k[1]} (x{v[0]})")
    print(f"advisory cites   : {len(w['advisory'])}  (live build READMEs, reported, never gated)")
    for k, v in sorted(w["advisory"].items()):
        print(f"    {k[0]}:{v[1]} -> {k[1]} (x{v[0]})")
    try:
        members, absent = read_set(w)
        total = sum(os.path.getsize(os.path.join(root, p)) for p in members)
        print(f"read path        : {len(members)} files, {total} B (tracked-but-absent: {len(absent)})")
        for p in members:
            print(f"    {os.path.getsize(os.path.join(root, p)):>7} B  {p}")
    except Problem as exc:
        print(f"read path        : {exc}")
    return 0


def _measure_lines(root: str, conf: dict) -> list:
    """The rows each waiver home would key, as strings: a `# <home>` line, then each orphan id and its
    count 1, then the second home's line and each dead citation's `<file> TAB <cited> TAB <count>`
    (TOOL-dWitnessedBar-17 S4). A `#` line is one the factory skips. Split out from the verb below so
    the selftest can ASSERT them: the arm helper compares a return value, and a verb that prints and
    returns 0 is unobservable to it — which is why nothing exercised this path for its whole life."""
    w = walk(root, conf)
    m = conf["MEMORY_ROOT"]
    orphans = sorted(set(w["cites"]) - set(w["defs"]))
    return ([f"# {m}/{WAIVER}"] + [f"{i}\t1" for i in orphans] + [f"# {m}/{REGISTRY}"]
            + [f"{f}\t{cited}\t{v[0]}" for (f, cited), v in sorted(w["dead"].items())])


def cmd_list_unbound(root: str) -> int:
    """`--list-unbound`: the `unbound-records` seed (TOOL-dWitnessedBar-17 §8 F6), one `<record> TAB 1` row
    per unbound record check 21 grades, the hygiene gate's own print mode returned through `ask_shell`,
    so check 21's population filter keeps its one shell definition and no seed carries a `bash` head."""
    sys.stdout.write(ask_shell("--list-unbound", root))
    return 0


def cmd_measure(root: str, conf: dict) -> int:
    """Print the rows each waiver home would key. Measured against THIS corpus — a row copied from
    another tree is either vacuous or permanently red."""
    for line in _measure_lines(root, conf):
        print(line)
    return 0


def _render_defined_ids(root: str, conf: dict) -> list:
    """The `--print-defined-ids` output as a list, so the selftest can assert it (the `_measure_lines`
    split, for the same reason). Line 0 is the id grammar as a POSIX ERE behind `# id-ere: `; every
    line after is one DEFINED id — anchored by a spec H1, a backlog row or a decision row — sorted.

    KICK-aReplayedCard-2. The kickoff checker's `--card --append` joins the ids a card cites against
    this set in ONE spawn, and it cannot extract id-shaped tokens from the card without the grammar;
    spelling the grammar in shell is the second-predicate class `TOOL-cSpliceWarden-6` closed, so the
    one spawn carries it. The translation covers exactly the two Python-only constructs the grammar
    builder in `id_grammar.py` uses — `(?:` and `\\d` — and refuses if either survives, because
    an ERE that `grep -E` reads differently from the reader would let the shell and the reader
    disagree about what an id is, silently.
    """
    w = walk(root, conf)
    ere = grammar(root).ID.replace("(?:", "(").replace(r"\d", "[0-9]")
    if "(?" in ere or "\\d" in ere:
        raise Problem("corpus_ids: the id grammar carries a construct this verb cannot translate to "
                      "POSIX ERE: %s" % ere)
    return ["# id-ere: " + ere] + sorted(w["defs"])


def print_defined_ids(root: str, conf: dict) -> int:
    """Print the id grammar, then every id this corpus DEFINES, one per line. Read-only; the pins do
    not gate it — it is a set for a caller, not a check.

    Exit 3 is a NAMED DEGRADATION, not a refusal: an install whose `id_grammar.py` is absent has no
    id set to print. The caller (`manifest-check.sh --card
    --append`) maps 3 onto its "id citations unchecked" branch and still judges paths; before this
    the grammar's Problem exited 1, the append refused every body, and the commit deny's printed
    remedy re-ran the refusing append — a lockout (the aReplayedCard closing review, F1)."""
    if not (GRAMMAR_DIR / "id_grammar.py").is_file():
        print("corpus_ids: no id set — the id grammar lives in %s, which is not installed; "
              "restore it to check id citations" % GRAMMAR_WHERE)
        return 3
    for line in _render_defined_ids(root, conf):
        print(line)
    return 0


# ----------------------------------------------------------------------------------------- selftest
# The two waiver homes as a scaffold of the landed tree holds them: the ledger header and the factory's
# empty-home line, so a fixture's homes arm checks 13-15 exactly as gov's do (TOOL-dWitnessedBar-17 S4).
_EMPTY_HOMES = {
    WAIVER: "# ledger · id-orphan-waiver · key record id · direction shrink-only · drain key\n"
            "# unarmed · dead probe · abcdef12\n",
    REGISTRY: "# ledger · corpus-path-unresolved · key site path,cited · direction shrink-only · drain hunk\n"
              "# unarmed · dead probe · abcdef12\n",
}


def _scratch(tmp: str, *, homes=True, extra=None):
    run("git", "init", "-q", "--template=", ".", cwd=tmp)
    conf = ['MEMORY_ROOT=memory', 'DISCIPLINES="arch"', 'FAMILIES="arch:ARCH"', 'CHARTER="AGENTS.md"']
    _w(tmp, ".memory-tree.conf", "\n".join(conf) + "\n")
    for rel, body in (_EMPTY_HOMES.items() if homes else ()):
        _w(tmp, "memory/" + rel, body)
    _w(tmp, "AGENTS.md", "# charter\n\nRead `memory/README.md` before touching code.\n")
    # A tracked `.claude/` path, so `.claude/` is a REAL top-level directory in the fixture. Without
    # it `_roots()` yields only {memory/} and a `.claude/worktrees/x` citation is never a candidate —
    # the exclusion arms below would pass while exercising nothing.
    _w(tmp, ".claude/settings.json", "{}\n")
    _w(tmp, "memory/README.md", "# r\n")
    _w(tmp, "memory/HYGIENE.md", "sentinel\n")
    _w(tmp, "memory/DECISIONS.md", "# d\n\n- ARCH-tOne-1 · a decision\n")
    _w(tmp, "memory/builds/tOne/README.md",
       "---\nslug: tOne\nnode: a\nopened: 2026-08-01\nstreams: arch\nroster: ARCH\nids: ARCH-tOne-1\nstatus: OPEN\n---\n\n# tOne\n")
    _w(tmp, "memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md", "# ARCH-tOne-1 — a unit\n\nbody\n")
    for rel, body in (extra or {}).items():
        _w(tmp, rel, body)
    run("git", "add", "-A", cwd=tmp)
    run("git", "commit", "-q", "-m", "f", "--no-verify", cwd=tmp)
    return load_conf(tmp)


def _w(root, rel, text):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(text.encode("utf-8"))


def _walk_continues() -> set:
    """Every `continue` statement inside walk(), by line, DERIVED from its own source.

    A written-down line list would rot at the first edit and then vouch for the wrong lines. The AST
    is asked instead, so adding a branch to walk() automatically adds an obligation to reach it.
    """
    import ast
    import inspect

    src, first = inspect.getsourcelines(walk)
    tree = ast.parse("".join(src).lstrip() if src[0][:1].isspace() else "".join(src))
    off = first - 1
    return {n.lineno + off for n in ast.walk(tree) if isinstance(n, ast.Continue)}


def check_leg_harvest(base) -> str:
    """TOOL-dTotalRecall-23 AC7, the selftest's leg arm: `--check` over the leg fixture reads alike from
    `id-harvest` rows and from text, and once FAMILIES gains a family every path is parsed, none answered from
    rows its old params wrote. Staged red by `derive_id_params` leaving the family list out of its key."""
    import tree_lib as tl
    t = os.path.join(base, "legs")
    tl.write_leg_fixture(t)
    for rel, body in _EMPTY_HOMES.items():
        _w(t, "memory/" + rel, body)
    run("git", "add", "-A", "--", "memory/project", cwd=t)
    run("git", "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-q", "-m", "homes",
        "--no-verify", cwd=t)
    n = len([p for p in run("git", "ls-files", "--", "memory/", cwd=t).split("\n") if p])
    db = str(tl.build_fixture_index(t))

    def read_leg_check():
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "--check"], cwd=t,
                           capture_output=True, text=True, encoding="utf-8")
        lines = p.stdout.splitlines()
        legs = [ln for ln in lines if "leg rows:" in ln]
        return p.returncode, [ln for ln in lines if ln not in legs], legs
    with_ix = read_leg_check()
    os.replace(db, db + ".aside")
    without = read_leg_check()
    os.replace(db + ".aside", db)
    _w(t, ".memory-tree.conf", read(os.path.join(t, ".memory-tree.conf")).replace(
        'FAMILIES="arch:ARCH"', 'FAMILIES="arch:ARCH arch:XTRA"'))
    flipped = read_leg_check()
    say = "HYGIENE advisory leg rows: id-harvest "
    return (f"same={with_ix[:2] == without[:2]} "
            f"with={with_ix[2] == [say + f'{n - 1} from the index, 1 parsed']} "
            f"without={without[2] == [say + f'index absent, {n} parsed']} "
            f"flipped={flipped[2] == [say + f'0 from the index, {n} parsed']} {with_ix[2]} {flipped[2]}")


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
    # EVERY `continue` IN walk() MUST BE REACHED BY A FIXTURE. This is the one arm that could catch
    # the tautological shape filter deleted in TOOL-aBatchedTribunal-4: that branch was
    # `not (B or not B)`, identically False, so no INPUT/OUTPUT arm could ever discriminate — a
    # behavioural fixture is green against the dead code and against its removal alike. A branch no
    # fixture reaches is a branch no arm covers, and the next person to edit around it will trust it.
    _hit = set()
    _walk_file = walk.__code__.co_filename

    def _tracer(frame, event, _arg):
        if frame.f_code is walk.__code__:
            return _liner
        return None

    def _liner(frame, event, _arg):
        if event == "line" and frame.f_code.co_filename == _walk_file:
            _hit.add(frame.f_lineno)
        return _liner

    def arm(label, want, fn):
        try:
            got = fn()
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        ok = (want in str(got)) if want else (str(got) in ("[]", ""))
        print(("arm ok    " if ok else "arm FAIL  ") + label + ("" if ok else f" — expected {want!r}, got: {got}"))
        if not ok:
            fails.append(label)

    sys.settrace(_tracer)
    with tempfile.TemporaryDirectory() as base:
        t = os.path.join(base, "clean"); os.makedirs(t)
        c = _scratch(t)
        arm("a clean corpus produces no finding", None, lambda: checks(walk(t, c)))

        # TOOL-aHastenedSweep-4 AC3: walk()'s memo is off at import, hands every caller its own deep
        # copy, really is hit, and keys on the conf as well as the root. RED against a walk returning
        # its stored object, a memo on at import, and a key on `root` alone.
        def check_walk_memo():
            said = [f"default {_WALK_MEMO}"]
            tm = os.path.join(base, "memo"); os.makedirs(tm)
            cm = _scratch(tm)
            globals()["_WALK_MEMO"] = {}
            try:
                walk(tm, cm)["defs"]["ARCH-tPlanted-1"] = "planted"
                said.append("frozen " + ("no" if "ARCH-tPlanted-1" in walk(tm, cm)["defs"] else "yes"))
                _w(tm, "memory/builds/tOne/spec/2026-08-02-spec-tOne-2.md", "# ARCH-tOne-2 — a unit\n\nbody\n")
                run("git", "add", "-A", cwd=tm)
                run("git", "commit", "-q", "-m", "g", "--no-verify", cwd=tm)
                said.append("hit " + ("no" if "ARCH-tOne-2" in walk(tm, cm)["defs"] else "yes"))
                globals()["_WALK_MEMO"] = None
                said.append("off " + ("sees new" if "ARCH-tOne-2" in walk(tm, cm)["defs"] else "misses it"))
                globals()["_WALK_MEMO"] = {}
                walk(tm, cm)
                cm2 = dict(cm, MEMO_PROBE="7")
                said.append("conf keyed " + ("yes" if walk(tm, cm2)["conf"].get("MEMO_PROBE") == "7" else "no"))
            finally:
                globals()["_WALK_MEMO"] = None
            return " · ".join(said)
        arm("walk()'s memo is off by default, frozen per caller, hit, and keyed on root and conf",
            "default None · frozen yes · hit yes · off sees new · conf keyed yes", check_walk_memo)
        # KICK-aReplayedCard-2: the grammar line is a POSIX ERE that still recognises a defined id
        # (it is valid Python too, which is what lets this arm run it), and the set follows it.
        arm("--print-defined-ids leads with the grammar as an ERE and lists the defined id", "ok",
            lambda: (lambda ls: "ok" if ls[0].startswith("# id-ere: ") and "(?" not in ls[0]
                     and r"\d" not in ls[0] and re.fullmatch(ls[0][len("# id-ere: "):], "ARCH-tOne-1")
                     and ls[1:] == ["ARCH-tOne-1"] else repr(ls))(_render_defined_ids(t, c)))
        # The aReplayedCard closing review, F1: with no id_grammar.py in the grammar dir the verb
        # DEGRADES — exit 3, one line naming the kit — instead of raising the grammar's Problem.
        # GRAMMAR_DIR is pointed at a directory that does not exist, then restored.

        def _check_degraded():
            import contextlib
            saved, buf = globals()["GRAMMAR_DIR"], io.StringIO()
            globals()["GRAMMAR_DIR"] = saved / "nowhere"
            try:
                with contextlib.redirect_stdout(buf):
                    rc = print_defined_ids(t, c)
            finally:
                globals()["GRAMMAR_DIR"] = saved
            return f"rc={rc} lines={len(buf.getvalue().splitlines())} {buf.getvalue().strip()}"
        arm("--print-defined-ids with no id_grammar.py exits 3 with one line naming it",
            "rc=3 lines=1 corpus_ids: no id set — the id grammar lives in ", _check_degraded)

        # ---- TOOL-dDerivedDocket-50: the kit's ONE public route to the anchor grammar.
        # ---- BOUND TO THE ROOT IT IS GIVEN, and the fixture's family (`arch:ARCH`) is one this
        # ---- repository does not declare — so a route bound to the repo the kit is INSTALLED in
        # ---- answers None on all three lines and this arm reds, which is the whole point of it.
        # ---- Without a discriminating family, an unrecognising grammar and a clean corpus are the
        # ---- same empty answer.
        _at = resolve_anchor(t)
        arm("resolve_anchor answers the GIVEN root's own id on a heading and a table row, None on a citation",
            "['ARCH-tOne-1', 'ARCH-tOne-1', None]",
            lambda: [_at("## ARCH-tOne-1 — a unit"),
                     _at("| ARCH-tOne-1 | a row |"),
                     _at("context lives in ARCH-tOne-1 upstream")])

        # ---- THE CALL GRAPH, derived from this module's own source in the idiom `_walk_continues`
        # ---- uses. A second bundle-to-answer site would take a change to the grammar's calling
        # ---- convention in one place and not the other; a `walk()` that reached the route with no
        # ---- bundle while keeping its own would resolve the conf at that root twice per walk, and
        # ---- both resolves would answer the same, so nothing behavioural could ever see it.
        def _graph():
            import ast as _ast
            _tree = _ast.parse(read(os.path.abspath(__file__)))
            _named, _callers, _in_walk, _route_args = 0, set(), 0, []
            for _fn in _tree.body:
                if not isinstance(_fn, _ast.FunctionDef):
                    continue
                for _n in _ast.walk(_fn):
                    if not isinstance(_n, _ast.Call):
                        continue
                    _f = _n.func
                    # `anchor_at` reached through ANY expression counts, not only through the name
                    # `extract`: measured, a staged break written as `__import__("extract").anchor_at`
                    # is invisible to a receiver-anchored test, which is the same could-not-fail
                    # shape this whole unit is about.
                    if isinstance(_f, _ast.Attribute) and _f.attr == "anchor_at":
                        _named += 1
                    if isinstance(_f, _ast.Name) and _f.id == "_anchor":
                        _callers.add(_fn.name)
                    if isinstance(_f, _ast.Name) and _f.id == "grammar" and _fn.name == "walk":
                        _in_walk += 1
                    # TOOL-dTotalRecall-23 S4: the per-line loop is `extract_ids`', which takes the bundle
                    # walk() resolved, or the reader's params resolved, and hands it to the route.
                    if (isinstance(_f, _ast.Name) and _f.id == "resolve_anchor"
                            and _fn.name in ("walk", "extract_ids")):
                        _route_args.append(f"{_fn.name}:{len(_n.args) + len(_n.keywords)}")
            return "anchor_at=%d _anchor callers=%r grammar( in walk=%d route args=%r" % (
                _named, sorted(_callers), _in_walk, _route_args)
        arm("anchor_at is named ONCE, _anchor's only caller is the route, walk() resolves one bundle "
            "and extract_ids hands it over",
            "anchor_at=1 _anchor callers=['resolve_anchor'] grammar( in walk=1 "
            "route args=['extract_ids:2']", _graph)

        # ---- THE ROUTE'S OWN REFUSAL, at BOTH of the installed-check's points, and `grammar()`'s
        # ---- beside it. The second fixture needs `id_grammar` out of sys.modules or the real module
        # ---- answers `hasattr(grammar_for)` and the outdated point is never reached — the arm would
        # ---- pass by exercising nothing.
        def _under_grammar_dir(d, fn):
            # GRAMMAR_WHERE is swapped beside GRAMMAR_DIR: the refusal reads it (TOOL-aRepatriatedFork-46 S4).
            saved_dir, saved_where = globals()["GRAMMAR_DIR"], globals()["GRAMMAR_WHERE"]
            saved_path = list(sys.path)
            saved_mod = sys.modules.pop("id_grammar", None)
            globals()["GRAMMAR_DIR"], globals()["GRAMMAR_WHERE"] = d, "%s/id_grammar.py" % d
            try:
                return fn()
            finally:
                globals()["GRAMMAR_DIR"], globals()["GRAMMAR_WHERE"] = saved_dir, saved_where
                sys.path[:] = saved_path
                sys.modules.pop("id_grammar", None)
                if saved_mod is not None:
                    sys.modules["id_grammar"] = saved_mod

        def _refusals(d):
            def _say(f):
                try:
                    f()
                    return "NO REFUSAL"
                except Problem as exc:
                    return str(exc)
                except Exception as exc:  # noqa: BLE001 — a foreign type escaping IS the finding
                    return f"UNEXPECTED {type(exc).__name__}: {exc}"
            return _under_grammar_dir(
                d, lambda: (_say(lambda: resolve_anchor(t)), _say(lambda: grammar(t))))

        for _sub, _body, _state, _cure, _pincure in (
            ("nowhere",
             None,
             "the id grammar lives in %s/id_grammar.py, which is not installed.",
             "Restore it from the memory-tree kit; no conf value of this kit turns the anchor route "
             "off.",
             "Either restore it from the memory-tree kit or remove project/id-orphan-waiver.txt and "
             "project/corpus-path-unresolved.txt to turn checks 13-15 off."),
            ("oldkit",
             "# an id_grammar.py that predates grammar_for(root)\n",
             "the installed %s/id_grammar.py predates grammar_for(root);",
             "update it from the memory-tree kit, because no conf value of this kit turns the anchor "
             "route off",
             "update it, or remove the two waiver homes to turn checks 13-15 off"),
        ):
            _d = pathlib.Path(base) / _sub
            if _body is not None:
                _w(base, _sub + "/id_grammar.py", _body)
            _state_text = _state % _d if "%s" in _state else _state
            _route, _pin = _refusals(_d)
            n_label = "the anchor route's refusal (%s) states ITS cause and ITS cure" % _sub
            arm(n_label, "corpus_ids: the anchor route was asked for, but " + _state_text + " " + _cure,
                lambda _r=_route: _r)
            arm("the anchor route's refusal (%s) names neither waiver home" % _sub, "clean",
                lambda _r=_route: "clean" if "id-orphan-waiver" not in _r and "corpus-path-unresolved" not in _r
                else _r)
            # The home caller's cure is re-typed here rather than read off the constant it grades.
            arm("grammar()'s own refusal (%s) keeps the home cause and its cure" % _sub,
                "corpus_ids: a waiver home that arms checks 13-15 is present, but " + _state_text + " " + _pincure,
                lambda _p=_pin: _p)

        # ---- THE TARGET ROOT'S OWN DECLARATIONS. `grammar_for(root)` refuses with the SIBLING
        # ---- kit's ConfError, a RuntimeError and not this kit's Problem, so before the route
        # ---- mapped it an arbitrary target root answered with a traceback past three
        # ---- `except Problem` handlers. Three roots, because the resolver distinguishes three and
        # ---- one collapsed sentence cannot tell an absent file from a conf declaring no families.
        for _sub, _confbody, _want in (
            ("root-noconf", None, "no .memory-tree.conf"),
            ("root-nomem", 'FAMILIES="arch:ARCH"\n', "declares no MEMORY_ROOT"),
            ("root-nofam", 'MEMORY_ROOT=memory\n', "declares no usable FAMILIES"),
        ):
            _r = os.path.join(base, _sub)
            os.makedirs(_r, exist_ok=True)
            if _confbody is not None:
                _w(_r, ".memory-tree.conf", _confbody)

            def _undeclared(_root=_r):
                try:
                    resolve_anchor(_root)
                    return "NO REFUSAL"
                except Problem as exc:
                    return str(exc)
                except Exception as exc:  # noqa: BLE001 — ConfError reaching here IS the finding
                    return f"UNEXPECTED {type(exc).__name__}: {exc}"
            arm("an undeclared target root (%s) raises this kit's Problem, naming the root" % _sub,
                "corpus_ids: the anchor route was asked for over %s, and the id grammar refused "
                "that root: refused: " % _r, _undeclared)
            arm("that refusal names WHICH declaration was missing (%s)" % _sub, _want, _undeclared)

        # ---- TOOL-aWeldedTribunal-5: the conf parser, graded against BASH rather than asserted.
        # ---- bash is the reference because bash is what the format IS; the python half is the copy,
        # ---- and six readers held an identical naive one. Each pair below was measured with
        # ---- `set -a; . conf` before it was written here.
        for _line, _want in [
            ("MEMORY_ROOT=memory   # note", ("MEMORY_ROOT", "memory")),
            ("export FAMILIES=\"TOOL DEPL\"", ("FAMILIES", "TOOL DEPL")),
            # THE TWO DIRECTIONS THIS PARSER HAS TO GET RIGHT AT ONCE, and the closing diff review
            # found the first cut got only one: a `#` INSIDE quotes is data, a `#` after the closing
            # quote is a comment. Getting the first alone kept a trailing comment and a stray quote,
            # live on five lines of this kit's own shipped conf example.
            ("Q=\"a # b\"", ("Q", "a # b")),
            ("R=\"v\"  # note", ("R", "v")),
            ("T=   # empty", ("T", "")),
            # TOOL-aRepatriatedFork-38 rev-3 (C4): a `#` OPENING the word is data, as bash reads it.
            ("H=#x", ("H", "#x")),
            ("S=plain", ("S", "plain")),
        ]:
            arm("conf parse agrees with bash: %s" % _line, repr(_want),
                (lambda ln=_line: repr(parse_conf_line(ln))))
        arm("a blank line declares nothing", "None", lambda: repr(parse_conf_line("   ")))
        arm("a full-line comment declares nothing", "None", lambda: repr(parse_conf_line("# x=1")))

        # 13 — two build folders claiming one id.
        t2 = os.path.join(base, "coll"); os.makedirs(t2)
        c2 = _scratch(t2, extra={
            "memory/builds/tTwo/README.md":
                "---\nslug: tTwo\nnode: a\nopened: 2026-08-01\nstreams: arch\nroster: ARCH\nids: ARCH-tOne-1\nstatus: OPEN\n---\n\n# tTwo\n",
            "memory/builds/tTwo/spec/2026-08-01-spec-tTwo-1.md": "# ARCH-tOne-1 — the same id\n\nbody\n"})
        arm("check 13 catches one id in two build folders", "claimed by 2 build folders",
            lambda: "\n".join(checks(walk(t2, c2))))
        # ...and its near miss: the same id on a `#` line inside a fenced block is code, no heading.
        t3 = os.path.join(base, "coll-fenced"); os.makedirs(t3)
        c3 = _scratch(t3, extra={
            "memory/builds/tTwo/README.md":
                "---\nslug: tTwo\nnode: a\nopened: 2026-08-01\nstreams: arch\nroster: ARCH\nids: ARCH-tTwo-1\nstatus: OPEN\n---\n\n# tTwo\n",
            "memory/builds/tTwo/spec/2026-08-01-spec-tTwo-1.md":
                "# ARCH-tTwo-1 — its own id\n\n```toml\n# ARCH-tOne-1 in a comment\n```\n"})
        arm("check 13 reads no heading inside a fenced block", "NONE",
            lambda: "\n".join(x for x in checks(walk(t3, c3)) if "check 13" in x) or "NONE")

        # ---- 13 and 15 UNDER `builds` (TOOL-dDerivedDocket-8). ONE corpus, five confs: an ask filed
        # ---- AFTER the cutoff and an ask filed BEFORE it, each anchored in a second build folder,
        # ---- plus a dead path cited from an ask and the same token cited from a family view. The
        # ---- one tree is what makes each verdict an observation: the pre-cutoff arm's silence is
        # ---- read beside the post-cutoff arm's finding over the same shape, so "raised nothing"
        # ---- cannot mean "found nothing to look at".
        tB = os.path.join(base, "bmode"); os.makedirs(tB)
        cB = _scratch(tB, extra={
            "memory/builds/tNew/BACKLOG.md":
                "# tNew\n\n## Asks\n\n"
                "- ARCH-tNew-1 · filed 2026-09-05 · an ask filed after the cutoff\n"
                "- ARCH-tOld-1 · filed 2026-08-05 · an ask migrated from the shard, filed before it\n"
                "- ARCH-tCite-1 · filed 2026-09-05 · cites `memory/gone/never-filed.md`, which is dead\n",
            # THE FOREIGN ANCHORS. Each id's records live in ANOTHER build's folder, which is what
            # every migrated legacy row looks like; the post-cutoff one is a collision and the
            # pre-cutoff one is the state D12-g exists to keep quiet.
            "memory/builds/tTwo/README.md":
                "---\nslug: tTwo\nnode: a\nopened: 2026-08-01\nstreams: arch\nroster: ARCH\n"
                "ids: ARCH-tNew-1\nstatus: OPEN\n---\n\n# tTwo\n",
            "memory/builds/tTwo/spec/2026-08-01-spec-tTwo-1.md":
                "# ARCH-tNew-1 — the foreign anchor of a post-cutoff ask\n\nbody\n",
            "memory/builds/tTwo/spec/2026-08-01-spec-tTwo-2.md":
                "# ARCH-tOld-1 — the foreign anchor of a pre-cutoff ask\n\nbody\n",
            # The SAME dead token, cited from the family view. Under `builds` that file is generated
            # text, so it leaves the present-tense corpus and its citation is not graded.
            "memory/backlog/ARCH.md":
                "# ARCH — live asks\n\nSee `memory/gone/never-viewed.md` for detail.\n",
        })
        cB["BACKLOG_MODE"] = "builds"
        cB["ASK_CUTOFF"] = "2026-09-01"
        arm("under `builds` an ask filed AFTER the cutoff still claims its id, so a foreign anchor "
            "is a check 13 collision", "ARCH-tNew-1 is claimed by 2 build folders",
            lambda: "\n".join(checks(walk(tB, cB))))
        arm("...and the SAME shape filed BEFORE the cutoff claims nothing, so the migrated legacy "
            "anchors stay quiet", "ABSENT",
            lambda: "PRESENT" if "ARCH-tOld-1 is claimed" in "\n".join(checks(walk(tB, cB)))
            else "ABSENT")
        # The row still DEFINES the id, so nothing the skip silences becomes an orphan one check
        # along. Without this arm the skip could have been written as "do not record it at all".
        arm("...and the pre-cutoff id is still DEFINED, so check 14 does not report it as an orphan",
            "ABSENT",
            lambda: "PRESENT" if "ARCH-tOld-1 is cited but never defined"
            in "\n".join(checks(walk(tB, cB))) else "ABSENT")
        # V16 — a cutoff that is not zero-padded. `"2026-10-01" < "2026-9-30"` is TRUE, so comparing
        # it as a raw string would silently pass every October ask through the skip.
        cB16 = dict(cB); cB16["ASK_CUTOFF"] = "2026-9-30"
        arm("a malformed cutoff skips EVERY ask row rather than comparing against it",
            "ABSENT",
            lambda: "PRESENT" if "ARCH-tNew-1 is claimed" in "\n".join(checks(walk(tB, cB16)))
            else "ABSENT")
        arm("...and says so once, naming V16", "V16: ASK_CUTOFF='2026-9-30' is not a zero-padded",
            lambda: "\n".join(walk(tB, cB16)["notes"]))
        # V15 — a blank cutoff. Compared as the empty string every ask reads as filed AFTER it, which
        # reds every migrated anchor at once: F2's rejected option (a).
        cB15 = dict(cB); cB15["ASK_CUTOFF"] = ""
        arm("a blank cutoff skips every ask row rather than reading as the empty string",
            "ABSENT",
            lambda: "PRESENT" if "ARCH-tNew-1 is claimed" in "\n".join(checks(walk(tB, cB15)))
            else "ABSENT")
        arm("...and says so once, naming V15", "V15: ASK_CUTOFF is blank while BACKLOG_MODE is",
            lambda: "\n".join(walk(tB, cB15)["notes"]))
        # 15 — the present-tense corpus swaps one member for another. BOTH halves, because dropping
        # `backlog/` without adding `BACKLOG.md` takes every graded ask path token out of the check
        # and reports green (owner ruling D9).
        arm("under `builds` a dead path cited from an ask IS graded",
            "memory/gone/never-filed.md", lambda: "\n".join(checks(walk(tB, cB))))
        arm("...and the same token cited from a generated family view is NOT", "ABSENT",
            lambda: "PRESENT" if "never-viewed.md" in "\n".join(checks(walk(tB, cB)))
            else "ABSENT")
        # THE SHARDS CONTROL, over the same tree: the view is an authored shard there and its dead
        # citation is named, while the build folder's file is a record of a moment and is not.
        cBs = dict(cB); cBs["BACKLOG_MODE"] = "shards"
        arm("under `shards` the dead path in the family shard is still named",
            "memory/gone/never-viewed.md", lambda: "\n".join(checks(walk(tB, cBs))))
        arm("...and under `shards` the build folder's own file is outside the present corpus",
            "ABSENT",
            lambda: "PRESENT" if "never-filed.md" in "\n".join(checks(walk(tB, cBs)))
            else "ABSENT")

        # 14 — orphan, keyed waiver, stale waiver.
        t3 = os.path.join(base, "orph"); os.makedirs(t3)
        # PROSE, not a list row: `- <id> ·` IS an anchor, so a backlog row DEFINES its id rather than
        # orphaning it. The first cut of this fixture used a backlog row, produced no orphan at all,
        # and the arm would have passed by finding nothing on a rule it never exercised.
        c3 = _scratch(t3, extra={"memory/README.md": "# r\n\nContext lives in ARCH-tGhost-9 upstream.\n"})
        arm("check 14 catches a cited-never-defined id", "ARCH-tGhost-9 is cited but never defined",
            lambda: "\n".join(checks(walk(t3, c3))))
        _w(t3, "memory/project/id-orphan-waiver.txt", "# waived\nARCH-tGhost-9\t1\tabcdef12\tseeded\n")
        run("git", "add", "-A", cwd=t3); run("git", "commit", "-q", "-m", "w", "--no-verify", cwd=t3)
        arm("a waived orphan passes", None, lambda: checks(walk(t3, c3)))
        t4 = os.path.join(base, "stale"); os.makedirs(t4)
        c4 = _scratch(t4, extra={"memory/project/id-orphan-waiver.txt": "ARCH-tOne-1\t1\tabcdef12\tseeded\n"})
        arm("a waiver row that now resolves is stale", "which now resolves — stale row",
            lambda: "\n".join(checks(walk(t4, c4))))

        # TOOL-aRepatriatedFork-39: check 14 grades the PRESENT-tense corpus only, check 15's
        # population. An archive and the append-only decision log each cite an undefined id AND a
        # dead path on one line; neither check may see either. The 869209ed engine reds both ids
        # here. The present-tense control is the README arm above, which reds on both engines.
        tN = os.path.join(base, "tense"); os.makedirs(tN)
        cN = _scratch(tN, extra={
            "memory/archive/DECISIONS.2026-08-01.md":
                "# rotated\n\nUpstream ARCH-tPast-7 lived at `memory/gone/archived.md`.\n",
            "memory/DECISIONS.md":
                "# d\n\n- ARCH-tOne-1 · a decision\n\nIt cites ARCH-tPast-8 at `memory/gone/logged.md`.\n"})
        arm("check 14 grades present-tense citations only, as check 15 does", None,
            lambda: checks(walk(tN, cN)))
        arm("...and the rows --measure prints are the orphans check 14 grades, none here",
            "# memory/project/corpus-path-unresolved.txt", lambda: _measure_lines(tN, cN)[1])
        # The waiver is not a citation: a row whose id only the waiver and an archive cite is stale.
        # The 869209ed engine read the waiver's own row as a citation and passed this.
        _w(tN, "memory/project/id-orphan-waiver.txt", "ARCH-tPast-7\t1\tabcdef12\tseeded\n")
        run("git", "add", "-A", cwd=tN); run("git", "commit", "-q", "-m", "w", "--no-verify", cwd=tN)
        arm("a waiver row no present-tense file cites is stale", "which no present-tense file cites — stale row",
            lambda: "\n".join(checks(walk(tN, cN))))
        # AC3's other half: one present-tense orphan beside one past-tense citation. The measured rows
        # and the graded count are both 1; the 869209ed engine made them both 2.
        tM = os.path.join(base, "tense-pin"); os.makedirs(tM)
        cM = _scratch(tM, extra={
            "memory/README.md": "# r\n\nContext lives in ARCH-tGhost-9 upstream.\n",
            "memory/archive/DECISIONS.2026-08-01.md": "# rotated\n\nUpstream ARCH-tPast-7.\n"})
        arm("--measure's orphan rows equal check 14's orphan count", "1 == 1",
            lambda: "%d == %d" % (_measure_lines(tM, cM).index("# memory/project/corpus-path-unresolved.txt") - 1,
                                  sum("never defined" in l for l in checks(walk(tM, cM)))))

        # TOOL-aMendedFleet-26 — the `missing:` form. The same undefined id as the orphan arm above,
        # written in the form, is no orphan and is counted on its own; the form naming an id the
        # corpus DEFINES reds in a present-tense file and is ignored in a record of a moment.
        tX = os.path.join(base, "missing-form"); os.makedirs(tX)
        cX = _scratch(tX, extra={
            "memory/README.md": "# r\n\nContext lives in missing:ARCH-tGhost-9 upstream.\n"})
        arm("a `missing:` id is not an orphan for check 14", None, lambda: checks(walk(tX, cX)))
        arm("...and the walk counts it on its own", "{'ARCH-tGhost-9': {'memory/README.md'}}",
            lambda: walk(tX, cX)["missing"])
        tY = os.path.join(base, "missing-defined"); os.makedirs(tY)
        cY = _scratch(tY, extra={
            "memory/README.md": "# r\n\nSee missing:ARCH-tOne-1 for now.\n",
            "memory/builds/tOne/spec/2026-08-02-spec-tOne-2.md": "# ARCH-tOne-2 — b\n\nmissing:ARCH-tOne-1\n"})
        arm("a `missing:` id the corpus defines reds check 14 in a present-tense file",
            "ARCH-tOne-1 is marked missing but defined — cited missing: in memory/README.md, defined in",
            lambda: "\n".join(checks(walk(tY, cY))))
        arm("...and only there: the spec's own marker is a record of a moment", "findings=1;",
            lambda: "findings=%d;" % sum("marked missing" in l for l in checks(walk(tY, cY))))

        # 15 — both sides and the count, the registry read through the ledger factory
        # (TOOL-dWitnessedBar-17 §4): rule 2 retired with the pin, rule 3 is the factory's duplicate
        # refusal, rule 4 and the state refusal retired with the `absent|moved:` column.
        DEAD = "# r\n\nSee `memory/gone/never-existed.md` for detail.\n"
        t5 = os.path.join(base, "dead"); os.makedirs(t5)
        c5 = _scratch(t5, extra={"memory/README.md": DEAD})
        arm("check 15 catches an unregistered dead citation", "has no row in",
            lambda: "\n".join(checks(walk(t5, c5))))
        reg = "memory/README.md\tmemory/gone/never-existed.md\t1\tabcdef12\tseeded\n"
        _w(t5, "memory/project/corpus-path-unresolved.txt", reg)
        run("git", "add", "-A", cwd=t5); run("git", "commit", "-q", "-m", "r", "--no-verify", cwd=t5)
        arm("a dead citation keyed in the registry passes, its row read through the factory", None,
            lambda: checks(walk(t5, c5)))
        _w(t5, "memory/project/corpus-path-unresolved.txt",
           "memory/README.md\tmemory/gone/never-existed.md\t2\tabcdef12\tseeded\n")
        run("git", "add", "-A", cwd=t5); run("git", "commit", "-q", "-m", "r1", "--no-verify", cwd=t5)
        arm("check 15 grades the count too", "occurs 1 time(s), row says 2",
            lambda: "\n".join(checks(walk(t5, c5))))
        _w(t5, "memory/project/corpus-path-unresolved.txt", reg + reg)
        run("git", "add", "-A", cwd=t5); run("git", "commit", "-q", "-m", "r2", "--no-verify", cwd=t5)
        arm("a duplicate row is the factory's refusal", "the key is declared twice",
            lambda: "\n".join(checks(walk(t5, c5))))
        # the OTHER direction: the source is repaired, the row survives.
        t6 = os.path.join(base, "repaired"); os.makedirs(t6)
        c6 = _scratch(t6, extra={
            "memory/project/corpus-path-unresolved.txt": "memory/README.md\tmemory/gone/x.md\t1\tabcdef12\tseeded\n"})
        arm("check 15 catches a row whose citation was repaired", "the citation was repaired",
            lambda: "\n".join(checks(walk(t6, c6))))

        # THE HOMES ARM THE CHECKS (TOOL-dWitnessedBar-17 S4, AC4). Each home holding its header and the
        # factory's empty-home line, with NO conf key at all, arms checks 13-15 through `--check`;
        # with both homes removed the same corpus names none of them. RED against an `armed` that
        # reads the home's seeded state, which an empty zero-bound home never reaches.
        tH = os.path.join(base, "homes"); os.makedirs(tH)
        _scratch(tH, extra={"memory/README.md": DEAD})

        def _check_rc(t):
            out = subprocess.run([sys.executable, os.path.abspath(__file__), "--check"], cwd=t,
                                 capture_output=True, text=True, encoding="utf-8")
            return "rc=%d %s" % (out.returncode, " | ".join(l for l in out.stdout.split("\n") if l))
        arm("an empty, unarmed home arms check 15 with no conf key", "rc=1 ",
            lambda: _check_rc(tH))
        arm("...naming check 15 and the dead path", "HYGIENE check 15: memory/README.md:3 cites memory/gone/never-existed.md",
            lambda: _check_rc(tH))
        for _rel in _EMPTY_HOMES:
            os.remove(os.path.join(tH, "memory", _rel))
        run("git", "add", "-A", cwd=tH); run("git", "commit", "-q", "-m", "no homes", "--no-verify", cwd=tH)
        arm("...and with both homes removed it names no check 13 to 15", "NONE",
            lambda: "NONE" if not any("check 1%d" % n in _check_rc(tH) for n in (3, 4, 5)) else _check_rc(tH))
        # Each home arms its own check: the orphan waiver alone arms 13 and 14, the registry alone 13 and 15.
        tW = os.path.join(base, "waiver-only"); os.makedirs(tW)
        cW = _scratch(tW, homes=False, extra={"memory/" + WAIVER: _EMPTY_HOMES[WAIVER]})
        tG = os.path.join(base, "registry-only"); os.makedirs(tG)
        cG = _scratch(tG, homes=False, extra={"memory/" + REGISTRY: _EMPTY_HOMES[REGISTRY]})
        arm("...and armed() reads each home on its own", "[13, 14] [13, 15]",
            lambda: "%s %s" % (sorted(armed(tW, cW)), sorted(armed(tG, cG))))

        # 15, DIRECTORY citations. The flatten moved every build folder and left four dead directory
        # citations in the live ledger, and the harvest could not see one of them because it required
        # a file extension. The RED and GREEN arms run over the SAME fixture, because the green half
        # alone passes on the un-widened code too: an unharvested token is silent for the wrong
        # reason.
        tD = os.path.join(base, "dirs"); os.makedirs(tD)
        cD = _scratch(tD, extra={
            # The four EXCLUSION branches of the harvest, each with a token that takes it. The
            # reachability arm at the end of this file is what demanded them: before it, three of
            # walk()'s `continue`s had never been executed by any fixture, so a change to the
            # append-only skip, the elision list or the top-level-root test could not have redded
            # anything. A branch no fixture reaches is a branch no arm covers.
            #   * `memory/DECISIONS.md` is APPEND-ONLY: a dead citation there is a historical
            #     record, not a repair, so the harvest must skip the file entirely.
            #   * `memory/builds/tOne/spec/…` is not in the PRESENT-tense corpus regex — same skip,
            #     the other half of the same `if`.
            #   * an ELIDED token (`<slug>`) and a slashless one (`README.md`) are not repo paths.
            #   * `nosuchroot/x.md` is rooted at no real top-level directory, so "does it exist" is
            #     not a well-posed question about this repo.
            "memory/DECISIONS.md": "# d\n\n- a decision citing `memory/gone/appendonly/`\n",
            "memory/builds/tOne/spec/2026-08-01-spec-tOne-9.md":
                "x\n\nnot present-tense: `memory/gone/notpresent/`\n",
            "memory/README.md": (
                "# r\n\nSee `memory/builds/tOne/` and `memory/gone/never/`.\n"
                "Elided: `memory/builds/<slug>/spec/`. Slashless: `README.md`.\n"
                "Unrooted: `nosuchroot/x.md`.\n"),
        })
        arm("check 15 catches a dead DIRECTORY citation", "memory/gone/never",
            lambda: "\n".join(checks(walk(tD, cD))))
        arm("...and is silent about a directory that resolves", "[nope]" if False else "",
            lambda: "" if not [l for l in checks(walk(tD, cD)) if "memory/builds/tOne" in l] else "FOUND")

        # THE WRONG-PREFIX CASE, both halves. A kit installed at `<prefix>/<kit>/` scaffolds documents
        # that cite `<kit>/…`, whose first segment is not a top-level directory. Before the tail rule
        # those citations were skipped unjudged: measured on a real `<prefix>/` install, seven dead kit
        # paths in a scaffolded HYGIENE.md and the gate exited 0. `_scratch` puts nothing under
        # `<prefix>/`, so the fixture supplies the whole shape — a real file at a prefix, and a citation
        # of it written WITHOUT that prefix.
        # The wrong citation is the ROOT-install spelling, built through a prefix variable set EMPTY.
        root_pfx = ""
        # At a root install PFX is empty, and the fixture still needs a prefixed shape to cite wrongly.
        fx_pfx = PFX or "scripts/"
        tP = os.path.join(base, "prefix"); os.makedirs(tP)
        cP = _scratch(tP, extra={
            f"{fx_pfx}{HERE.name}/check-memory-hygiene.sh": "#!/usr/bin/env bash\n",
            "memory/HYGIENE.md": f"sentinel\n\nRun `{root_pfx}{HERE.name}/check-memory-hygiene.sh` to lint.\n",
        })
        arm("check 15 catches a kit path written at the WRONG PREFIX",
            f"{root_pfx}{HERE.name}/check-memory-hygiene.sh",
            lambda: "\n".join(checks(walk(tP, cP))))
        # ...and the same citation spelled correctly is silent. Without this half the arm above would
        # also pass on a rule that reds every token whose first segment is not a top-level directory.
        tQ = os.path.join(base, "prefix-ok"); os.makedirs(tQ)
        cQ = _scratch(tQ, extra={
            f"{fx_pfx}{HERE.name}/check-memory-hygiene.sh": "#!/usr/bin/env bash\n",
            "memory/HYGIENE.md": f"sentinel\n\nRun `{fx_pfx}{HERE.name}/check-memory-hygiene.sh` to lint.\n",
        })
        arm("...and the correctly-prefixed spelling of it is silent", None,
            lambda: checks(walk(tQ, cQ)))
        # A link that resolves RELATIVE TO THE CITING FILE is correct and must stay silent. This is
        # the ordinary shape inside the memory tree (`builds/<slug>/README.md` from `LIVE.md`) and
        # the first cut of the tail rule reported 17 of them dead, 16 written by this kit's own
        # index generator.
        tR = os.path.join(base, "relative"); os.makedirs(tR)
        cR = _scratch(tR, extra={
            "memory/LIVE.md": "# live\n\n- [tOne](builds/tOne/README.md)\n"})
        arm("a link resolving relative to the citing file is not dead", None,
            lambda: checks(walk(tR, cR)))

        # the DECLARED exclusion. A checkout location is not repo CONTENT, and resolution here never
        # touches the filesystem, so it would otherwise classify as dead identically on every node.
        tX = os.path.join(base, "excl"); os.makedirs(tX)
        cX = _scratch(tX, extra={
            "memory/README.md": "# r\n\nThe worktree lives at `.claude/worktrees/whatever/`.\n"})
        arm("an excluded prefix is not classified", None, lambda: checks(walk(tX, cX)))
        cX2 = dict(cX); cX2["DEAD_PATH_EXCLUDE"] = ""
        arm("...and removing the prefix from the conf makes it classified again",
            ".claude/worktrees/whatever",
            lambda: "\n".join(checks(walk(tX, cX2))))

        # 15's ADVISORY population (TOOL-aMendedFleet-24): a build README `LIVE.md` links is read for
        # paths and REPORTED, never gated. The linked README cites one dead path and one tracked path
        # with a line locator; a second build absent from `LIVE.md` cites a dead path and is not read.
        # Routing admitted files into `dead` reds the first three arms below.
        tL = os.path.join(base, "live-readme"); os.makedirs(tL)
        cL = _scratch(tL, extra={
            "memory/LIVE.md": "# live\n\n- [tOne](builds/tOne/README.md)\n",
            "memory/builds/tOne/README.md":
                "# tOne\n\nGone: `memory/gone/livedead/`. Kept: `memory/HYGIENE.md:1-2`.\n",
            "memory/builds/tTwo/README.md": "# tTwo\n\nGone: `memory/gone/unlinked/`.\n"})
        wL = walk(tL, cL)

        def _check_in(t):
            out = subprocess.run([sys.executable, os.path.abspath(__file__), "--check"], cwd=t,
                                 capture_output=True, text=True, encoding="utf-8")
            adv = [l for l in out.stdout.split("\n") if l.startswith("HYGIENE advisory check 15:")]
            return f"rc={out.returncode} " + " | ".join(adv)

        arm("a live build README's dead citation is an advisory note, and --check still exits 0",
            "rc=0 HYGIENE advisory check 15: 1 dead repo-path citation(s) in 1 of 1 live build README(s)",
            lambda: _check_in(tL))
        arm("...and the advisory map holds exactly it, the line locator cut", "OK",
            lambda: "OK" if sorted(wL["advisory"]) == [("memory/builds/tOne/README.md", "memory/gone/livedead")]
            else str(sorted(wL["advisory"])))
        arm("...and check 15's dead map stays empty", None, lambda: str(sorted(wL["dead"])))
        arm("...and a build LIVE.md does not link is not read", None,
            lambda: str([k for k in wL["advisory"] if "tTwo" in k[0]]))
        tL0 = os.path.join(base, "live-empty"); os.makedirs(tL0)
        cL0 = _scratch(tL0, extra={"memory/LIVE.md": "# live\n\n- [tGhost](builds/tGhost/README.md)\n"})
        arm("a LIVE.md whose build links resolve to no tracked README says the population is empty",
            "the live-README population is empty", lambda: "\n".join(walk(tL0, cL0)["notes"]))

        # 16 — the charter's read path. STRUCTURAL since TOOL-dSpentCeiling-1: these arms call
        # check_read_path() directly, because it is deliberately NOT reachable from checks(walk(...))
        # any more. Every arm below rides ONE fixture whose charter cites a tracked, present file the
        # index set does not cap, so the only thing varying is the declaration under test.
        t7 = os.path.join(base, "readpath"); os.makedirs(t7)
        c7 = _scratch(t7, homes=False, extra={
            "AGENTS.md": "# charter\n\nRead `memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md` first.\n"})

        def _rp(root, conf):
            b, n = check_read_path(root, conf)
            return "BAD:" + " | ".join(b) + " NOTES:" + " | ".join(n)

        # THE DEFECT THIS UNIT CLOSES, as an arm. With every switch off the old engine returned 0 from
        # main() before check 16 could run, so this citation was invisible. `homes=False` is the whole
        # point of the fixture: an arm that writes a home would pass against the old code too.
        arm("rule 3 fires with NO waiver home at all — the silence this unit removes",
            "which is under", lambda: _rp(t7, c7))
        arm("...and armed() is empty on that same tree, so 13-15 stay off and the grammar unloaded",
            None, lambda: "" if not armed(t7, c7) else str(sorted(armed(t7, c7))))

        # THE GRACE. The comparison is the subject, so the arms vary the DECLARED threshold rather
        # than substituting a stand-in for the mechanism: below the flip a finding is a NOTE and the
        # gating list is empty, at or above it the finding is gating and the note is gone.
        # THE GRACE, BOTH SIDES. The constant is the subject, so the arms vary the DECLARED flip
        # rather than substituting a stand-in for the mechanism.
        _gate = READ_PATH_RULES_GATE
        try:
            globals()["READ_PATH_RULES_GATE"] = False
            arm("while the flip is off a rule-3 finding is REPORTED, never gated",
                "BAD: NOTES:", lambda: _rp(t7, c7))
            arm("...and the grace SAYS SO, rather than looking like a clean run",
                "are REPORTED, not gated", lambda: _rp(t7, c7))
            globals()["READ_PATH_RULES_GATE"] = True
            arm("once the flip is on the same finding GATES",
                "BAD:check 16 rule 3", lambda: _rp(t7, c7))

            # H1 — THE GRACE MUST NOT REACH A TREE THAT DECLARED THE RETIRED CEILING. Rules 3 and 4
            # were already armed and green there, so gracing them SUSPENDS a live check. This arm is
            # the one whose absence let that ship: every earlier grace arm tested the reporting side
            # only, and a grace nobody has watched decline to fire is not a grace, it is an off switch.
            globals()["READ_PATH_RULES_GATE"] = False
            tD = os.path.join(base, "declared-ceiling"); os.makedirs(tD)
            cD = _scratch(tD, homes=False, extra={
                "AGENTS.md": "# charter\n\nRead `memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md` first.\n"})
            _cp = os.path.join(tD, ".memory-tree.conf")
            with io.open(_cp, "a", encoding="utf-8", newline="") as fh:
                fh.write('READ_PATH_CEILING="135677"' + chr(10))
            run("git", "add", "-A", cwd=tD)
            run("git", "commit", "-q", "-m", "declared", "--no-verify", cwd=tD)
            cD = load_conf(tD)
            arm("a tree that DECLARED the retired ceiling is not graced — its finding GATES",
                "BAD:check 16 rule 3", lambda: _rp(tD, cD))
            arm("...and it is still told the key is dead", "is declared", lambda: _rp(tD, cD))
        finally:
            globals()["READ_PATH_RULES_GATE"] = _gate

        # THE VALVE, observed after the finding and never before.
        c7w = dict(c7)
        c7w["READ_PATH_WAIVER"] = "memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md"
        arm("READ_PATH_WAIVER silences rule 3, and is the only conf key check 16 still reads",
            None, lambda: _rp(t7, c7w).replace("BAD: NOTES:", ""))

        # A CLEAN CHARTER MUST BE SILENT, or every arm above passes by finding something unrelated.
        t7c = os.path.join(base, "readpath-clean"); os.makedirs(t7c)
        c7clean = _scratch(t7c, homes=False)
        arm("a charter citing only CAPPED files produces nothing",
            None, lambda: _rp(t7c, c7clean).replace("BAD: NOTES:", ""))

        # RULE 4 — tracked but absent. Its old comment claimed check 12 owned this finding; check 12's
        # arm is restricted to builds/*/spec/*.md and index_set() drops absent files before check 6
        # measures, so for a charter-cited guide this is the only detector there is.
        t7a = os.path.join(base, "readpath-absent"); os.makedirs(t7a)
        c7a = _scratch(t7a, homes=False, extra={
            "AGENTS.md": "# charter\n\nRead `memory/guides/g.md` first.\n",
            "memory/guides/g.md": "# g\n"})
        os.remove(os.path.join(t7a, "memory/guides/g.md"))
        arm("rule 4 fires on a charter citation that is tracked but not on disk",
            "check 16 rule 4", lambda: _rp(t7a, c7a))
        arm("...and its message no longer misattributes the finding to check 12",
            None, lambda: "x" if "check 12" in _rp(t7a, c7a) else "")

        # THE RETIRED KEYS — announced, never refused. The shipped example declared the ceiling
        # BLANK, so a rule that refused on presence would red every adopter for doing nothing.
        # The key must be written into the CONF FILE, not into the parsed dict: `read_declared_keys()`
        # re-reads the file precisely so a merged default cannot masquerade as a declaration, and an
        # arm that mutated the dict would pass against a version that never read the file at all.
        for _ki, _k in enumerate(RETIRED_KEYS):
            for _vi, _v in enumerate(('"161120"', '""')):
                tR = os.path.join(base, "retired%d%d" % (_ki, _vi)); os.makedirs(tR)
                cR = _scratch(tR, homes=False)
                _cp = os.path.join(tR, ".memory-tree.conf")
                with io.open(_cp, "a", encoding="utf-8", newline="") as fh:
                    fh.write("%s=%s\n" % (_k, _v))
                run("git", "add", "-A", cwd=tR)
                run("git", "commit", "-q", "-m", "retired", "--no-verify", cwd=tR)
                cR = load_conf(tR)
                how = "declared" if _vi == 0 else "declared BLANK"
                arm(f"a {how} {_k} in the conf FILE is announced and does NOT gate",
                    f"NOTES:check 16: NOTE {_k} is declared",
                    lambda t=tR, c=cR: _rp(t, c))
        arm("a retired key alone does not arm checks 13-15",
            None, lambda: "" if not armed(t7c, dict(c7clean, READ_PATH_CEILING="161120"))
            else str(sorted(armed(t7c, c7clean))))

        # A MIS-SET CHARTER IS THIS CHECK'S OWN FINDING, not a Problem that escapes checks() and
        # replaces every sibling finding in the run with one line.
        c7c = dict(c7); c7c["CHARTER"] = "NOPE.md"
        arm("a DECLARED charter that is not tracked is check 16's own finding",
            "check 16: CHARTER 'NOPE.md' is declared and is not a tracked file",
            lambda: _rp(t7, c7c))
        # A YOUNG TREE IS NOT A BROKEN ONE. `adopt-memory-tree.sh --scaffold` writes no CHARTER and
        # no AGENTS.md, so an unconditional check 16 refused every adopter on the day they adopted —
        # measured, as a RED on this repo's own scaffolder arm before this branch was corrected.
        t7y = os.path.join(base, "readpath-young"); os.makedirs(t7y)
        c7y = _scratch(t7y, homes=False)
        os.remove(os.path.join(t7y, "AGENTS.md"))
        run("git", "rm", "-q", "--cached", "AGENTS.md", cwd=t7y)
        run("git", "commit", "-q", "-m", "no charter", "--no-verify", cwd=t7y)
        _conf_no_charter = io.open(os.path.join(t7y, ".memory-tree.conf"),
                                   encoding="utf-8", newline="").read()
        io.open(os.path.join(t7y, ".memory-tree.conf"), "w", encoding="utf-8", newline="").write(
            "\n".join(l for l in _conf_no_charter.split("\n") if not l.startswith("CHARTER=")))
        c7yc = load_conf(t7y)
        arm("an undeclared CHARTER with no default file is NOT ASKED, and says so",
            "not asked", lambda: _rp(t7y, c7yc))
        arm("...and it does not gate", "BAD: NOTES:", lambda: _rp(t7y, c7yc))
        arm("...and read_set still RAISES for cmd_report, which catches it",
            "is not a tracked file",
            lambda: read_set({"root": t7, "conf": c7c, "tracked": set()}))

        # the off switch, and the armed-without-grammar error.
        t8 = os.path.join(base, "off"); os.makedirs(t8)
        c8 = _scratch(t8, homes=False)
        arm("absent waiver homes turn every check off", None,
            lambda: "" if not armed(t8, c8) else str(sorted(armed(t8, c8))))

        # resolve_bash accepts a candidate only if it RUNS. A launcher that exists on disk and cannot
        # execute is the same defect one interpreter over as the Microsoft Store `python3` stub, and
        # an override that is SET and unusable has to be a named failure rather than a fall-through
        # to whatever is next on PATH — otherwise the operator believes they chose, and did not.
        tB = os.path.join(base, "bashprobe"); os.makedirs(tB)
        dead = os.path.join(tB, "not-a-bash")
        with open(dead, "w", encoding="utf-8") as fh:
            fh.write("this file exists and is not an executable\n")

        def _with_gov_bash(value):
            old = os.environ.get("GOV_BASH")
            os.environ["GOV_BASH"] = value
            try:
                return resolve_bash()
            finally:
                if old is None:
                    os.environ.pop("GOV_BASH", None)
                else:
                    os.environ["GOV_BASH"] = old

        arm("an unusable GOV_BASH is a NAMED failure, not a fall-through",
            "is set to", lambda: _with_gov_bash(dead))
        # ...and the green half over the SAME mechanism: a real bash still comes back untouched, so
        # the arm above is not passing because resolve_bash rejects everything.
        arm("a working GOV_BASH is returned unchanged", "OK",
            lambda: "OK" if _with_gov_bash(resolve_bash()) else "")

        arm("TOOL-dTotalRecall-23 AC7 — the walk reads alike from rows and text, and a changed id grammar "
            "parses every path", "same=True with=True without=True flipped=True",
            lambda: check_leg_harvest(base))

    sys.settrace(None)
    want = _walk_continues()
    missed = sorted(want - _hit)
    arm("every `continue` in walk() is reached by a fixture", None,
        lambda: "" if not missed else
        "; ".join(f"corpus_ids.py:{n} is a `continue` no fixture reaches" for n in missed))
    # ...and the checker's own red half. The first cut re-typed the message over `want | {-1}` and so
    # held by construction — it asserted a formatting expression, not the checker. This runs the SAME
    # expression the arm above runs, against a population with one line the fixtures provably never
    # executed (line 0 does not exist), so a tracer that recorded nothing and a tracer that recorded
    # everything give different answers.
    def _missed(pop):
        return "; ".join(f"corpus_ids.py:{n} is a `continue` no fixture reaches"
                         for n in sorted(pop - _hit))
    arm("...and the reachability checker can name an unreached branch",
        "corpus_ids.py:0 is a `continue` no fixture reaches", lambda: _missed(want | {0}))
    arm("...and it is silent when every member was reached", None, lambda: _missed(want))
    arm("...and the population is derived, not listed", "True", lambda: str(len(want) >= 4))

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — corpus_ids: all arms held")
    return 0


def main(argv: list) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        # TOOL-aSparedSpawn-9 S1: the fixtures' identity and line endings, once for every git the
        # selftest runs, in place of two to four `git config` processes per fixture repository.
        os.environ.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t.test", GIT_COMMITTER_NAME="t",
                          GIT_COMMITTER_EMAIL="t@t.test", GIT_CONFIG_COUNT="1",
                          GIT_CONFIG_KEY_0="core.autocrlf", GIT_CONFIG_VALUE_0="false")
        return cmd_selftest()
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("corpus_ids: not a git repo")
        return 2
    conf = load_conf(root)
    try:
        if mode == "--report":
            return cmd_report(root, conf)
        if mode == "--measure":
            return cmd_measure(root, conf)
        if mode == "--print-defined-ids":
            return print_defined_ids(root, conf)
        if mode == "--list-unbound":
            return cmd_list_unbound(root)
        if mode != "--check":
            print("usage: corpus_ids.py [--check|--report|--measure|--print-defined-ids|--list-unbound|--selftest]")
            return 2
        # Check 16 runs ALWAYS. Checks 13-15 stay behind the waiver homes, and the grammar stays
        # unloaded when both are absent — the cross-kit dependency is still conditional.
        bad, notes = check_read_path(root, conf)
        if armed(root, conf):
            w = walk(root, conf)
            notes += w["notes"]     # non-gating, and printed through the same channel as check 16's
            # TOOL-dTotalRecall-23 S6: the announce line, non-gating, keyed by no offender as `advisory`
            notes.append("advisory " + render_leg_line("id-harvest", w["legs"]))
            bad += checks(w)
        for line in notes:
            print("HYGIENE " + line)
        for line in bad:
            print("HYGIENE " + line)
        return 1 if bad else 0
    except Problem as exc:
        print(f"HYGIENE {exc}")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main(sys.argv))
