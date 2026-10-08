#!/usr/bin/env python3
"""drift_report.py — does this repo's own RECORD of its state still describe reality?

gov:kit drift-audit@1.24

    python <prefix>/drift-audit/drift_report.py            # human table, always exits 0
    python <prefix>/drift-audit/drift_report.py --json     # machine-readable, always exits 0
    python <prefix>/drift-audit/drift_report.py --check    # exit 1 if a GATEABLE signal is over its pin
    python <prefix>/drift-audit/drift_report.py --escape-ratio 2026-09   # on demand, minutes, never the bar

WHY THIS KIT EXISTS. A governance repo gates its CODE contracts hard and its RECORD contracts not at
all: a memory-hygiene gate checks that a spec Status token is spelled legally, never that it is TRUE.
The upstream audit that produced this kit measured the consequence in a 121k-LOC adopter — 24 of 58
in-flight ledger rows contradicted git, and roughly half of all non-terminal spec headers said "not
built" about shipped work — with every hygiene check green throughout. Nothing was lost; the records
simply stopped being readable, and it took a human's hunch to notice.

THE DESIGN RULE, which is the whole point of the file. This is a REPORT, not a gate. But a report
whose numbers cannot move is worse than no report: the adopter's convergence tool shipped a
`collision_flags` signal that was structurally incapable of being non-zero and every reader took the
0 as "converged" for thirteen days. So every signal here carries a `live` field asserting the probe
can still move over a non-empty population, and a dead probe prints DEAD PROBE instead of a clean 0.

WHAT IS ENGINE AND WHAT IS PROJECT. The signal implementations are generic over any repo that
follows the governance playbook (a memory tree, TEMPLATE-SPEC status headers, a per-node in-flight
ledger, an agent auto-memory directory). Everything genuinely repo-shaped — which paths are product
source, which lists promise to shrink, which hand-kept inventories mirror a generated one, and the
PINS — lives in the project layer `drift_signals.py`, copied from `drift_signals.template.py` at
adoption. Same split as codebase-map's `map_extractors.py`.

NO SECOND CONF. The corpus root and disciplines are read from `.memory-tree.conf`, which the
memory-tree kit owns. This kit declares no conf of its own and takes no `--memory-root` flag: a
second way to state the same value is the hand-kept-second-copy defect the whole audit was about.

ponytail: stdlib + git only, no deps, no cache. It runs in seconds; there is nothing to invalidate.
"""

from __future__ import annotations

import argparse
import ast
import datetime
import hashlib
import json
import math
import os
import pathlib
import re
import subprocess
import sys

# The kit never leaves bytecode in the adopter's worktree (matching memory-recall's query.py).
sys.dont_write_bytecode = True

# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


KIT_DRIFT_AUDIT_VERSION = "1.24"

CONF_NAME = ".memory-tree.conf"


class DriftError(RuntimeError):
    """The project layer or the conf is missing/unusable. Always a refusal, never a default."""


# --------------------------------------------------------------------------------------------
# repo + conf
# --------------------------------------------------------------------------------------------


def repo_root() -> pathlib.Path:
    """The adopting repo's root, anchored on THIS FILE rather than on the cwd — so a throwaway-repo
    selftest that copies the kit in resolves to that repo, not to wherever the runner stood."""
    here = pathlib.Path(__file__).resolve().parent
    out = subprocess.run(
        ["git", "-C", str(here), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        raise DriftError("not inside a git work tree")
    return pathlib.Path(out.stdout.strip())


def load_conf(root: pathlib.Path) -> dict[str, str]:
    """Parse the memory-tree kit's KEY=VALUE conf.

    A deliberate COPY of codebase-map's `map_lib.load_conf`, not an import of it: kits are copied
    into adopters independently, and importing across kit directories would make drift-audit
    un-adoptable without codebase-map. The drift is gated by asserting this parser against BASH
    sourcing the same file in selftest.py, never against a second Python parser — two operands from
    one generator assert nothing (the adopter's own review-2 F5 lesson).

    TOOL-aScouredKit-5: for two years that gate had never observed a divergence, because its fixture
    covered four spellings and neither of the two that actually diverged. The copy had dropped
    `map_lib`'s `removeprefix("export ")` and its ends-at-whitespace rule, so `export K=v` parsed to
    no key at all and `K=v  # note` swallowed the comment. Both are now in the fixture and both were
    seen RED there before this function was touched. The one REMAINING divergence is deliberate and
    is named rather than left to be rediscovered: the `\\ufeff` strip below has no counterpart in
    `map_lib`, and it stays because a BOM-led conf is a real Windows artifact and dropping the strip
    would lose a behaviour rather than gain equivalence.
    """
    p = root / CONF_NAME
    if not p.exists():
        raise DriftError(
            f"{CONF_NAME} not found at {root}. It is owned by the memory-tree kit; adopt that first.\n"
            "Minimum stub:\n  MEMORY_ROOT=memory\n  DISCIPLINES=\"...\"\n"
        )
    return parse_conf_text(p.read_text(encoding="utf-8", errors="replace"))


def parse_conf_text(text: str) -> dict[str, str]:
    """`load_conf`'s grammar over a conf's TEXT, so every root conf this kit reads parses one way.

    Lifted out of `load_conf` unchanged twice over, on two branches: TOOL-aMendedFleet-21 S2 for
    `build_cutoff_keys_armed`, and TOOL-dUnstuckLanding-15 to read `.unattended.conf` as committed at
    HEAD from a BLOB. `load_conf` calls it too, so the bash-sourcing comparison in selftest.py keeps
    grading the one parser every caller uses. The grammar, and its one deliberate divergence from
    bash, is `load_conf`'s docstring.
    """
    conf: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip().lstrip("﻿")
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k = k.strip().removeprefix("export ").strip()
        # TOOL-aRepatriatedFork-38 rev-3 (the closing review's C4): whitespace right after `=`
        # ends the assignment, so `K=   # note` is empty in bash, not the word `#`.
        if v[:1].isspace():
            conf[k] = ""
            continue
        v = v.strip().strip("\r")
        # Bash sourcing semantics for the restricted grammar the conf documents: a quoted value
        # is the text up to its MATCHING quote, whatever follows it; an UNQUOTED value ends at
        # whitespace, so a trailing inline comment cannot leak into it. Both rules are
        # `map_lib.load_conf`'s and both were missing here — see the docstring. The quoted rule
        # first tested whether the value's first and last characters matched, so
        # `KEY="v"  # note` kept its quotes (TOOL-dLoggedFlight-13, closing review round 2 R2-L5).
        close = v.find(v[0], 1) if v[:1] in ("'", '"') else -1
        if close >= 0:
            v = v[1:close]
        else:
            v = v.split()[0] if v.split() else ""
        conf[k] = v
    return conf


def load_project_layer(root: pathlib.Path):
    """Import the adopter's `drift_signals.py` from beside this file. Absence is a refusal."""
    here = pathlib.Path(__file__).resolve().parent
    mod = here / "drift_signals.py"
    if not mod.exists():
        raise DriftError(
            f"drift_signals.py not found beside the kit at {here}.\n"
            "Copy drift_signals.template.py to drift_signals.py and fill it (see README.md)."
        )
    sys.path.insert(0, str(here))
    import drift_signals  # noqa: E402

    for attr in ("PRODUCT_GLOBS", "SHRINK_ONLY", "HANDKEPT", "PINS"):
        if not hasattr(drift_signals, attr):
            raise DriftError(f"drift_signals.py is missing required attribute {attr}")
    return drift_signals


# --------------------------------------------------------------------------------------------
# git helpers
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# RATCHET GUARD — a pin RAISE and a population DRAIN look identical to `value > pin`
# --------------------------------------------------------------------------------------------
# Reads each declared scalar at the BASE and at HEAD. A move in the weakening direction is refused
# unless a comment within the preceding few lines names both numbers as `<old> -> <new>`. That marker
# convention already existed in this repo's prose; this only makes it read.
#
# The base value is taken with `git show`, so this compares against the commit the branch forked
# from, not against a working copy the same run could have edited.
# The SHIPPED default. An adopter overrides it by declaring RATCHET_LOOKBACK in their project
# layer beside the ratchets it governs — NOT in a conf, because this module's own docstring commits
# to no second conf and a key in an unrelated kit's conf is the objection TOOL-aDeclaredCeiling-1
# ratified. The window's width is a statement about a repo's COMMENT DENSITY: too narrow and a
# justification written above the pin falls outside it, too wide and a justification for a
# DIFFERENT pin further up is read as this one's. This repo has two pins three lines apart at the
# same value, which is the case that makes the second half real.
DEFAULT_RATCHET_LOOKBACK = 14


def _read_lookback(proj) -> int:
    """The project layer's RATCHET_LOOKBACK, or the shipped default — a NAMED refusal otherwise.

    Absent is the default, so a layer written before this key keeps working and does not fail to
    import. Present-but-nonsense is a refusal on the same channel `load_project_layer` uses for a
    missing required attribute, rather than an arithmetic surprise two frames down inside a slice.
    """
    raw = getattr(proj, "RATCHET_LOOKBACK", None)
    if raw is None:
        return DEFAULT_RATCHET_LOOKBACK
    if not isinstance(raw, int) or isinstance(raw, bool) or raw < 1:
        raise DriftError(
            f"drift_signals.py declares RATCHET_LOOKBACK = {raw!r}; it must be a positive integer "
            f"number of lines, or absent to take the shipped {DEFAULT_RATCHET_LOOKBACK}"
        )
    return raw


def _scalar_at(text: str, key: str):
    """The integer bound to `key`, for the two shapes this repo pins numbers in.

    A shell conf writes `KEY="7"` or `KEY=7`; a python declaration writes `"key": 7,`. Comment lines
    are skipped, or the prose justification directly above a pin ("RAISED 2 -> 3") is itself matched
    and the guard reads the old value as the new one — silently passing every raise it exists to
    catch. Returns (value, line_index) or (None, None).
    """
    pats = (
        re.compile(r"^\s*" + re.escape(key) + r"\s*=\s*\"?(\d+)\"?\s*$"),
        re.compile(r"^\s*[\"']" + re.escape(key) + r"[\"']\s*:\s*(\d+)\s*,?\s*$"),
    )
    for i, line in enumerate(text.splitlines()):
        if line.lstrip().startswith("#"):
            continue
        for p in pats:
            m = p.match(line)
            if m:
                return int(m.group(1)), i
    return None, None


def _justified(text: str, at: int, old: int, new: int, lookback: int) -> bool:
    """A comment within `lookback` lines above the pin naming BOTH numbers, `<old> -> <new>`."""
    lines = text.splitlines()
    want = re.compile(r"\b" + str(old) + r"\b\s*(?:->|→|to)\s*\b" + str(new) + r"\b")
    for line in lines[max(0, at - lookback): at + 1]:
        if want.search(line):
            return True
    return False


def ratchet_findings(git: "Git", root: pathlib.Path, ratchets, lookback: int = DEFAULT_RATCHET_LOOKBACK) -> list[str]:
    out: list[str] = []
    for r in ratchets or ():
        path, key, weakens = r["file"], r["key"], r["weakens"]
        head_txt = (root / path).read_text(encoding="utf-8", errors="replace") \
            if (root / path).exists() else ""
        base = git.run("show", f"{git.base_ref}:{path}")
        if base.returncode != 0:
            continue                      # the file is new on this branch; nothing to compare
        now, at = _scalar_at(head_txt, key)
        was, _ = _scalar_at(base.stdout, key)
        if now is None or was is None or now == was:
            continue
        weaker = now > was if weakens == "up" else now < was
        if not weaker:
            continue                      # a tightening ratchet is always free
        if not _justified(head_txt, at, was, now, lookback):
            out.append(
                f"{path}: {key} moved {was} -> {now}, which WEAKENS it, with no justification "
                f"beside it. A raise and a drain are indistinguishable to the gate that owns this "
                f"number — write why, naming both values as '{was} -> {now}', within "
                f"{lookback} lines above it."
            )
    return out


# --------------------------------------------------------------------------------------------
# S5 of TOOL-dScaffoldedMirror-6 — the LANGS mode ratchet.
#
# BESIDE `RATCHETS`, NOT INSIDE IT, and the reason is shape rather than taste. `RATCHETS` compares
# one SCALAR per (file, key) and its whole grammar — `_scalar_at`, `_justified`, `weakens: up|down`
# — is built on a number. A `LANGS` declaration is a SET of (extension, mode) pairs inside one
# string, so a mode move is per-extension and ordinal rather than numeric, and widening the scalar
# ratchet to carry it would make one mechanism answer two questions. The spec's section 3 refuses
# that widening explicitly.
#
# WHY THIS EXISTS AT ALL: flipping an armed extension to `dark` is a ONE-STRING edit that empties a
# graded population and, before this, reddened nothing. Flip `py` from `parser` to `dark` and the
# armed share of definition-carrying files falls by tens of points with the gate still exiting 0.
# The two percentages this comment used to name were measured before the shell cell was armed and
# were wrong by the time anyone read them; `--check` prints the live share on every run.
#
# THE GAP IT DOES NOT CLOSE, said plainly. An extension ARRIVING already-dark is a rise from absent
# (-1) to dark (0), so it is not a weakening and nothing here fires — yet it lowers coverage exactly
# as a flip does. The spec's rev-1 gave that case to a `COVERAGE_FLOOR` that rev-2 cut, so it is
# currently VISIBLE (the fraction moves, and the lexicon gate prints it every run) and not gated.
LANG_MODE_RANK = {"parser": 2, "probe": 1, "dark": 0}


def read_lang_modes(text: str) -> dict:
    """`{ext: mode}` from a `LANGS="<ext>:<pset>:<mode> …"` declaration. Absent key gives {}."""
    m = re.search(r'^LANGS="([^"]*)"', text, re.M)
    if not m:
        return {}
    out = {}
    for tok in m.group(1).split():
        bits = tok.split(":")
        if len(bits) == 3 and bits[2]:
            out[bits[0]] = bits[2]
    return out


def _check_mode_justified(text: str, ext: str, old: str, new: str, lookback: int) -> bool:
    """A comment within `lookback` lines above the `LANGS` line naming `<ext>: <old> -> <new>`.

    The EXTENSION is required in the marker, unlike the scalar ratchet's, because one `LANGS` line
    carries every extension: a bare `parser -> dark` beside it would justify a move for whichever
    extension the reader guessed.
    """
    lines = text.splitlines()
    at = next((i for i, ln in enumerate(lines) if ln.startswith("LANGS=")), None)
    if at is None:
        return False
    # NEGATIVE WORD-CHARACTER LOOKAROUNDS around the EXTENSION -- a strict SUPERSET of the `\b` this
    # replaced, and that property is what took two rounds. `\b` is a word-character boundary, so for
    # `<none>` -- the extension this repo declares for a dotless basename -- it sat before a `<` and
    # after a `>` and could never match: the marker was unsatisfiable for exactly the extension whose
    # name is not a word, and a weakening move on it would have redded forever with a correct marker
    # sitting right above it. The round-1 fix demanded whitespace-or-start before the extension,
    # which fixed `<none>` and QUIETLY NARROWED everything else -- `#py:`, `# (py:` and `# js,py:`,
    # the natural way to justify one move for two extensions, all stopped matching, reintroducing the
    # same symptom for every shape that used to work. Asserting no word character on either side
    # admits all of those and still rejects `pyx`. Closing review M2, corrected by the round-2 review.
    want = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(ext) + r"(?![A-Za-z0-9_])"
                      + r"\s*:?\s*\b" + re.escape(old)
                      + r"\b\s*(?:->|\u2192|to)\s*\b" + re.escape(new) + r"\b")
    return any(want.search(ln) for ln in lines[max(0, at - lookback): at + 1])


def build_lang_mode_findings(git: "Git", root: pathlib.Path, path: str = ".lexicon.conf",
                             lookback: int = DEFAULT_RATCHET_LOOKBACK) -> list:
    """Extensions whose coverage mode WEAKENED between the base and HEAD, unjustified."""
    p = root / path
    if not p.exists():
        return []                          # the kit is not adopted here; nothing declared, nothing to rank
    head_txt = p.read_text(encoding="utf-8", errors="replace")
    base = git.run("show", f"{git.base_ref}:{path}")
    if base.returncode != 0:
        return []                          # the declaration is new on this branch; nothing to compare
    now, was = read_lang_modes(head_txt), read_lang_modes(base.stdout)
    out = []
    for ext, old in sorted(was.items()):
        new = now.get(ext)
        old_rank = LANG_MODE_RANK.get(old, -1)
        new_rank = LANG_MODE_RANK.get(new, -1) if new is not None else -1
        if new_rank >= old_rank:
            continue
        shown = new if new is not None else "absent"
        if not _check_mode_justified(head_txt, ext, old, shown, lookback):
            out.append(
                f"{path}: LANGS .{ext} moved {old} -> {shown}, which WEAKENS coverage, with no "
                f"justification beside it. Emptying a graded population is a one-string edit and "
                f"reds nothing else — write why, naming the move as '{ext}: {old} -> {shown}', "
                f"within {lookback} lines above the LANGS line."
            )
    return out



# --------------------------------------------------------------------------------------------
# TOOL-aMendedFleet-56 S6 — BASELINES is shrink-only, read at the base like the two guards above.
#
# A pin bounds a COUNT, so a drained offender and a new one at an equal count read as no change; an
# id set bounds the offenders themselves. This guard keeps the set from growing: an id the base's
# set did not carry is a finding, and a FIRST seed may not exceed the pin the base held for that
# signal. There is no escape: each signal has a remedy that is not an addition.
#
# TOOL-aMendedFleet-110: nor is MOVING a signal out of the set. Every signal the base's BASELINES
# held is graded, listed in the working set or not, so a signal leaving BASELINES for PINS may be
# pinned no higher than the size of the set the base held. Deleting the set and pinning it at any
# count used to pass, because only the working dict was walked and an empty one returned early.
# ponytail: the base layer is read with `ast.literal_eval`, so a non-literal BASELINES or PINS at the
# base is a finding rather than an evaluation; executing the base's code would be the upgrade.
def build_baseline_findings(git: "Git", path: str, baselines: dict, pins: dict) -> list:
    """Findings for every signal whose working `BASELINES` set is WEAKER than the base allows."""
    base = git.run("show", f"{git.base_ref}:{path}")
    if base.returncode != 0:
        return []                          # the layer is new on this branch; nothing to compare
    try:
        tree = ast.parse(base.stdout)
    except SyntaxError as exc:
        return [f"{path}: the project layer at {git.base_ref} does not parse ({exc.msg}, line "
                f"{exc.lineno}), so BASELINES cannot be compared against the base"]
    nodes = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value:
            names = [node.target.id]
        else:
            continue
        for n in names:
            if n in ("BASELINES", "PINS"):
                nodes[n] = node.value      # the last assignment wins, as it does on import
    was = {}
    for n, v in nodes.items():
        try:
            was[n] = ast.literal_eval(v)
        except ValueError:
            return [f"{path}: {n} at {git.base_ref} is not a literal, so BASELINES cannot be "
                    f"compared against the base"]
    old_sets, old_pins = was.get("BASELINES") or {}, was.get("PINS") or {}
    out = []
    for sig, ids in sorted(baselines.items()):
        if sig in old_sets:
            for i in sorted(set(ids) - set(old_sets[sig])):
                out.append(f"{path}: BASELINES[{sig!r}] gained {i} against {git.base_ref}, which "
                           f"WEAKENS it. The set is shrink-only and has no escape: remove the cause "
                           f"that makes {i} an offender instead of listing it.")
        elif len(set(ids)) > old_pins.get(sig, 0):
            out.append(f"{path}: BASELINES[{sig!r}] is seeded with {len(set(ids))} ids where the "
                       f"base pins it at {old_pins.get(sig, 0)} in PINS, which WEAKENS it. Seed only "
                       f"the offenders the base's pin already bounds.")
    for sig in sorted(set(old_sets) - set(baselines)):
        size = len(set(old_sets[sig]))
        if sig in pins and pins[sig] > size:
            out.append(f"{path}: {sig!r} moved from BASELINES to PINS at {pins[sig]} where the "
                       f"base's set held {size} ids at {git.base_ref}, which WEAKENS it. Pin it no "
                       f"higher than {size}, the set's size, and drain from there.")
    return out


class Git:
    def __init__(self, root: pathlib.Path, base_ref: str):
        self.root, self.base_ref = root, base_ref

    def run(self, *a: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["git", "-C", str(self.root), *a],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )

    def is_commit(self, sha: str) -> bool:
        return self.run("cat-file", "-e", sha + "^{commit}").returncode == 0

    def is_ancestor(self, sha: str) -> bool:
        return self.run("merge-base", "--is-ancestor", sha, self.base_ref).returncode == 0


# --------------------------------------------------------------------------------------------
# Signal 1 — in-flight ledger rows vs git ancestry
# --------------------------------------------------------------------------------------------

_OPEN_CLAIM = re.compile(r"not\s+merged|not\s+pushed|awaiting|in-flight|unpushed|blocked|merging", re.I)
# A row cites shas that are NOT its own work: its base ("off `X`"), and any reference point it
# compares against ("parity byte-identical vs `X`", "measured against `X`"). All of those are
# ancestors by construction and prove nothing about the row's own state, so they must be excluded or
# the signal fires on correct rows.
#
# The `vs|against|compared` arm was added after a FIELD false positive, not speculatively: a row
# reading "BUILT ... NOT merged. Parity byte-identical vs `e8d046cc`" was flagged, because the only
# sha it named was its comparison baseline. Widen this list when a real row is misjudged, never
# pre-emptively — every term here loses a little detection power.
_REFERENCE_SHA = re.compile(
    r"(?:off|base|base is|vs\.?|versus|against|compared\s+(?:to|with)|relative\s+to)"
    r"\s+`?([0-9a-f]{7,40})`?",
    re.I,
)
_SHA = re.compile(r"`([0-9a-f]{7,40})`")


# A row that has REACHED its terminal state still makes a claim about git: the ledger's own prune
# trigger says "prune once ancestor", so `merged:<sha>` for a sha that IS an ancestor is a row whose
# own written rule has fired and been ignored. Left unoracled, cleaning up the open-claim rows simply
# converts them into this blind class — which is what a hand cleanup would have done here.
_TERMINAL_SHA = re.compile(r"merged\s*:?\s*`?([0-9a-f]{7,40})`?", re.I)


def signal_ledger(ctx) -> dict:
    rows, contradicting, judgeable, unjudgeable = 0, [], 0, 0
    for f in sorted(ctx.ledger_dir.glob("*.md")) if ctx.ledger_dir.is_dir() else []:
        rel = str(f.relative_to(ctx.root)).replace("\\", "/")
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not line.startswith("|") or line.startswith("|--"):
                continue
            low = line.lower()
            if "| slug" in low or ("node" in low and "branch" in low and "stream" in low):
                continue  # header row
            rows += 1
            if not _OPEN_CLAIM.search(line):
                # TERMINAL rows are judged too — see _TERMINAL_SHA. A `merged:<sha>` row whose sha is
                # an ancestor is past the prune trigger the ledger index states in its own words.
                for s in _TERMINAL_SHA.findall(line):
                    if ctx.git.is_commit(s) and ctx.git.is_ancestor(s):
                        judgeable += 1
                        contradicting.append({"file": rel, "line": i, "shas": [s],
                                              "why": "terminal and landed — past its own prune trigger"})
                        break
                continue
            refs = set(_REFERENCE_SHA.findall(line))
            work = [s for s in _SHA.findall(line) if s not in refs]
            if not work:
                # An open claim naming no sha OF ITS OWN cannot be judged from git. Counted, never
                # scored clean — the same distinction `signal_spec_status` draws with `unkeyed`.
                unjudgeable += 1
                continue
            judgeable += 1
            landed = [s for s in work if ctx.git.is_commit(s) and ctx.git.is_ancestor(s)]
            if landed:
                contradicting.append({"file": rel, "line": i, "shas": landed[:4],
                                      "why": "open claim, but its own sha has landed"})
    return {
        "signal": "ledger_rows_contradicting_git",
        "value": len(contradicting),
        "of": rows,
        "tolerance": 0,
        "gateable": True,
        # LIVE IFF THE JUDGEABLE POPULATION IS NON-EMPTY — not iff rows exist. `live` used to be
        # asserted over the ambient population while `value` was drawn from a narrower one, so a
        # ledger of rows this probe cannot judge reported a confident 0. One prune away from
        # reachable, and `--check` scored it ok either way.
        "live": judgeable > 0,
        "unjudgeable": unjudgeable,
        "detail": contradicting,
    }


# --------------------------------------------------------------------------------------------
# Signal 2 — spec Status headers vs evidence the unit shipped
# --------------------------------------------------------------------------------------------

_STATUS = re.compile(r"^\*\*Status:\*\*\s*([A-Za-z]+)", re.M)
# The spec's OWN id, from its H1 (`# TOOL-cSightedPlumb-1 — title`). Keying on the SLUG instead was
# tried upstream and over-flagged 107/126: one shipped unit made all 14 siblings of its multi-spec
# build look stale, because every id of a build shares the slug. The seq is the discriminator.
#
# ONE GRAMMAR, AND IT IS THE RECALL EXTRACTOR'S. This was a hand-typed pattern of the shape
# family-dash-slug-dash-digits, which is a second spelling of a published alternation and had already
# diverged from it: the session era admits a trailing lowercase correction suffix that a
# digits-then-boundary form cannot match, so a correction-form spec scored UNKEYED and the probe
# silently declined to judge it rather than reporting anything.
#
# BOUND TO THE TREE BEING CLASSIFIED, never to the repo this kit is installed in. The extractor's
# module-level constants anchor on the extractor's own file, which is right for its own CLI and
# wrong for a caller classifying a different tree: a grammar that recognises nothing yields an empty
# classification, and an empty classification is exactly what a clean corpus yields. The recorded
# class is `memory/gotchas/grammar-bound-to-the-wrong-root.md`, which names the per-root accessor as
# the fix. This kit's own self-test copies the report into scratch trees carrying fixture ids and no
# memory-tree conf, which is precisely where the wrong binding reports a confident zero.
#
# IMPORTABLE OR NOT. drift-audit is copy-installed and must keep running in a tree that has no
# memory-recall, so the accessor answers when it imports and a LOCAL COPY answers when it does not.
# That copy is not a second grammar by stealth: the self-test asserts it still equals what the
# extractor produces whenever the extractor is present, so a divergence fails loudly here instead of
# silently in an adopter. This is unit 2's F1 resolution, and unit 3 adopts it by reference rather
# than deciding the same boundary twice.
_NODE_TAG_CLASS = "a-z"
_FAMILY_SHAPE = re.compile(r"^[A-Z][A-Z0-9]*$")


def _build_local_ident(families) -> str:
    """The LOCAL COPY of the shipped id alternation, for a tree with no recall kit.

    Byte-compared against the extractor's own output by this kit's self-test whenever that kit is
    present, which is what keeps "fallback" from meaning "second grammar".
    """
    node = _NODE_TAG_CLASS
    eras = (r"\d{3}", rf"[{node}]\d{{2,3}}", rf"[{node}][A-Za-z]{{2,}}-\d+[a-z]*")
    # A conf declaring NO families must not narrow the grammar to nothing: that is the blind
    # oracle this unit exists to remove, reintroduced through the fallback. The permissive form
    # below is what the hand-typed pattern did, so an undeclared tree keeps exactly the coverage
    # it had rather than silently losing all of it.
    fam = "|".join(families) if families else r"[A-Z]{2,6}"
    return r"(?:" + fam + r")-(?:" + "|".join(eras) + r")"


def _resolve_ident(root, families) -> str:
    """The shipped alternation for THIS tree, from the recall extractor where it is importable."""
    try:
        kit = resolve_kit_dir("memory-recall", "extract.py", pathlib.Path(__file__).resolve().parent)
    except LookupError:
        return _build_local_ident(families)
    added = str(kit)
    sys.path.insert(0, added)
    try:
        import extract  # type: ignore
        return extract.grammar_for(root).ID
    except Exception:
        # A present-but-unusable sibling is the fallback case, never a crash. Every signal is
        # evaluated in one unguarded comprehension, so a raise here takes the whole report down.
        return _build_local_ident(families)
    finally:
        try:
            sys.path.remove(added)
        except ValueError:
            pass



def _build_local_anchors(ident: str):
    """The LOCAL COPY of the four anchor shapes, for a tree with no recall kit.

    UNGUARDED, and said so rather than claimed otherwise. The sibling `_build_local_ident` IS
    byte-compared against the extractor by this kit's self-test; these anchor patterns are NOT.
    MEASURED, because this docstring has now been wrong twice: the flags are EQUAL on all four
    (`_resolve_anchors` re-compiles the extractor's with the same multiline flag), and two of the
    four `.pattern` strings are byte-identical. What differs on the other two is escape SPELLING of
    the same character classes. So a byte-compare would red today on a difference that is
    cosmetic, and an equivalence compare is a second grammar deciding what "equivalent" means. The
    first revision asserted a comparison nobody wrote; the second blamed a flag that matches. Both
    are the "assertion with no observation behind it" this build's own annotation guide bans, which
    is why this one carries the measurement instead of a reason. An anchor is a line that DEFINES a record, as
    opposed to one that merely cites it, and the distinction is the whole of the signal below — a
    head-anchored id is DEFINED, so a record complaining about a missing unit would silently create
    it. That class is `memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md`.
    """
    return (
        re.compile(r"^#{2,6}\s+[`*]*(" + ident + r")\b", re.M),
        re.compile(r"^\s*[-*]\s+[`*]*(" + ident + r")\b[`*]*\s*[-\u2014:\u00b7]", re.M),
        re.compile(r"^\|\s*[`*]*(" + ident + r")\b[^|]*\|", re.M),
        re.compile(r"^\s*[-*]\s+[`*]*(" + ident + r")\b[`*]*\s*[\u00b7|]", re.M),
    )


def _resolve_anchors(root, families):
    """The anchor patterns for THIS tree, from the recall extractor where it is importable."""
    try:
        kit = resolve_kit_dir("memory-recall", "extract.py", pathlib.Path(__file__).resolve().parent)
    except LookupError:
        return _build_local_anchors(_build_local_ident(families))
    added = str(kit)
    sys.path.insert(0, added)
    try:
        import extract  # type: ignore
        return tuple(re.compile(a.pattern, a.flags | re.M) for a in extract.grammar_for(root).anchors)
    except Exception:
        return _build_local_anchors(_build_local_ident(families))
    finally:
        try:
            sys.path.remove(added)
        except ValueError:
            pass


def _build_own_id_re(root, families):
    return re.compile(r"^#\s+(" + _resolve_ident(root, families) + r")\b", re.M)


def _read_families(conf) -> tuple:
    """The id FAMILY allowlist, from the memory-tree conf this kit already reads.

    Declared as `discipline:FAMILY` pairs; the uppercase half is the allowlist. Read rather
    than spelled, so a tree declaring a family this repo does not still classifies its own ids.
    """
    pairs = (conf.get("FAMILIES", "") or "").split()
    # DECLARATION ORDER, not sorted. The alternation must be byte-identical to the one the
    # extractor builds or the self-test that keeps this copy honest compares two spellings of
    # the same grammar and reports a divergence that is not one.
    # THE SAME RULE THE RECALL CONF USES, and it is not "split on a colon". That reader takes the
    # part after the LAST colon and keeps only tokens shaped like a family. A discipline-free entry
    # is therefore ADMITTED by both — `rpartition` returns the whole token when no colon is present
    # — and that is stated because an earlier revision of this comment claimed both readers dropped
    # it, which is the opposite of what the same hunk had just made true. What the shape filter
    # drops is a token that is not family-shaped, including one carrying a regex metacharacter,
    # which would otherwise reach `re.compile` below as a traceback rather than a named refusal.
    out = []
    for pair in pairs:
        fam = pair.rpartition(":")[2]
        if _FAMILY_SHAPE.match(fam) and fam not in out:
            out.append(fam)
    return tuple(out)


def _parse_slug(uid: str):
    """The slug PROJECTION of a matched id, or None for an era that has none.

    DERIVED, not captured. The shipped alternation carries no groups of its own and exposes no
    per-era parts, so a second capture group would mean re-deriving the session era's shape here —
    the second grammar the import above exists to remove.
    """
    parts = uid.split("-")
    return parts[1] if len(parts) == 3 else None
NON_TERMINAL = frozenset({"OPEN", "SPECCED", "BLOCKED", "INPROGRESS"})


def signal_spec_status(ctx) -> dict:
    suspect, checked, unkeyed = [], 0, 0
    # FLAT (memory-tree 1.5): `<memory_root>/builds/<slug>/spec/…`. This read
    # `{memory_root}/*/builds/…` — the discipline directory the flatten retired — and so matched 0
    # files while the flat form matched 39. The probe reported 0-of-0 DEAD PROBE, `--check` skipped
    # it for being dead, and the leg stayed green over a blind oracle for the whole of that session.
    for p in sorted(ctx.root.glob(f"{ctx.memory_root}/builds/*/spec/**/*.md")):
        head = p.read_text(encoding="utf-8", errors="replace")[:4000]
        m = _STATUS.search(head)
        if not m or m.group(1).upper() not in NON_TERMINAL:
            continue
        own = ctx.own_id_re.search(head)
        if not own:
            unkeyed += 1  # the probe cannot judge this spec. Counted, never guessed.
            continue
        checked += 1
        # The ORACLE: a non-terminal spec whose OWN id is cited by tracked PRODUCT source describes
        # work that demonstrably shipped. Product source only — keying a record's truth on another
        # record is circular, and upstream an id CATALOG (a recall alias file) certified all 110.
        #
        # `-w`, and it is load-bearing: without it `-F` matches a PREFIX, so `<slug>-1` hits
        # inside every `<slug>-1[0-9]` sibling. TOOL-aBoundedVerdict-30 measured the cost - id
        # `-1` was reported with three citations, all of them `-11`'s, on a build whose ids ran
        # past 10. The over-count GROWS with the build: a 30-unit build mis-attributes ids 1, 2
        # and 3 to twenty siblings, each reading as a stale status header nobody can find.
        # THE LAYER IS NOT EVIDENCE (TOOL-aMendedFleet-56 S10): a `BASELINES` list spelling this id
        # would otherwise cite it, and a listed id could then never drain.
        hit = ctx.git.run("grep", "-l", "-w", "-F", own.group(1), "--", *ctx.evidence_globs,
                          *([f":(exclude){ctx.layer_path}"] if ctx.layer_path else []))
        if hit.returncode == 0 and hit.stdout.strip():
            suspect.append({
                "file": str(p.relative_to(ctx.root)).replace("\\", "/"),
                "id": own.group(1),
                "status": m.group(1).upper(),
                "cited_in": hit.stdout.strip().splitlines()[:3],
            })
    # THE SECOND LIVENESS HALF, and the first one cannot substitute for it. `checked` counts
    # non-terminal keyed specs and is computed above before any glob is read, so an EVIDENCE_GLOBS
    # set that resolves to no tracked file leaves `live` True and `of` at full size while `value`
    # falls to 0 — the reassuring zero, wearing a live flag. This counts what the narrowed
    # declaration actually resolves to, which is the only number that moves when it collapses.
    seen = ctx.git.run("ls-files", "--", *ctx.evidence_globs)
    evidence_files = len(seen.stdout.split()) if seen.returncode == 0 else 0
    return {
        "signal": "non_terminal_specs_cited_by_product_source",
        "value": len(suspect),
        "of": checked,
        "evidence_files": evidence_files,
        "tolerance": 0,
        "gateable": True,
        "live": checked > 0 and evidence_files > 0,
        "unjudgeable": unkeyed,
        "detail": suspect,
    }


# --------------------------------------------------------------------------------------------
# Signal 3 — shrink-only lists that are not shrinking
# --------------------------------------------------------------------------------------------


def _entries(p: pathlib.Path) -> int:
    if not p.exists():
        return -1
    return sum(1 for ln in p.read_text(encoding="utf-8", errors="replace").splitlines()
               if ln.strip() and not ln.strip().startswith("#"))


def derive_low_waters(git: Git, paths: list) -> dict:
    """path -> the smallest count of `_entries`-style rows the file held after any commit on the
    first-parent line, from ONE patch walk over every path together; `None` where the path has no
    such history, or where the replay ever goes negative, which means a patch was misread and the
    row cannot be judged. `--no-renames`, so a rename shows as a whole add and the replay stays
    a count of the file's own lines, not a rename's delta."""
    out = {p: None for p in paths}
    if not paths:
        return out
    walk = git.run("log", "--first-parent", "--diff-merges=first-parent", "--no-renames", "-p",
                   "--reverse", "--format=%x01%H", "--", *paths)
    if walk.returncode != 0:
        return out
    headers = {f"diff --git a/{p} b/{p}": p for p in paths}
    count = {p: 0 for p in paths}
    broken: set = set()
    cur, in_hunk, touched = None, False, set()
    # A trailing commit marker settles the last commit the way every earlier marker does.
    for ln in walk.stdout.split("\n") + ["\x01"]:
        if ln.startswith("\x01"):
            for p in touched:
                if count[p] < 0:
                    broken.add(p)
                elif out[p] is None or count[p] < out[p]:
                    out[p] = count[p]
            touched.clear()
            cur, in_hunk = None, False
        elif ln.startswith("diff --git "):
            cur, in_hunk = headers.get(ln), False
            if cur is not None:
                touched.add(cur)
        elif ln.startswith("@@"):
            in_hunk = cur is not None
        elif in_hunk and ln[:1] in ("+", "-"):
            body = ln[1:].strip()
            if body and not body.startswith("#"):
                count[cur] += 1 if ln[0] == "+" else -1
    return {p: (None if p in broken else v) for p, v in out.items()}


def check_shrink_row(seed, low_water, entries):
    """Why a shrink-only row is an offender, or `None`. `regrown`: it holds more rows than the
    lowest count its history reached. `never drained`: it was seeded with rows and holds at least as
    many today. A list seeded empty and still empty is neither."""
    if low_water is not None and entries > low_water:
        return "regrown"
    if seed is not None and seed > 0 and entries >= seed:
        return "never drained"
    return None


def signal_shrink_only(ctx) -> dict:
    rows = []
    low_waters = derive_low_waters(ctx.git, list(ctx.shrink_only))
    for rel, what in ctx.shrink_only.items():
        p = ctx.root / rel
        now = _entries(p)
        adds = ctx.git.run("log", "--diff-filter=A", "--format=%H", "--", rel).stdout.strip().splitlines()
        seed = None
        if adds:
            blob = ctx.git.run("show", f"{adds[-1]}:{rel}")
            if blob.returncode == 0:
                seed = sum(1 for ln in blob.stdout.splitlines()
                           if ln.strip() and not ln.strip().startswith("#"))
        low = low_waters.get(rel)
        rows.append({"file": rel, "what": what, "entries": now, "seed": seed,
                     "shrunk_by": (seed - now) if seed is not None else None,
                     "low_water": low,
                     "reason": check_shrink_row(seed, low, now) if low is not None else None})
    # TOOL-aMendedFleet-57. Two reasons, from `check_shrink_row`. `regrown` grades a list against
    # its LOW-WATER MARK, the smallest count its first-parent history reached: the seed reading alone
    # let a list seeded at 9 that drained to 0 and grew back to 3 read "shrunk by 6", because 3 was
    # still under its seed. `never drained` is the seed reading's one surviving case, a list seeded
    # with rows that holds at least as many today.
    #
    # TOOL-aScouredKit-3's sibling finding still binds `never drained`: a list SEEDED EMPTY and
    # still empty has nothing to drain, so it is excluded by `seed > 0`. The obvious tightening of
    # the seed case to `entries > seed` is WRONG and is refused here rather than left for someone to
    # re-propose. It would drop the seed>0, now==seed case, which is a list nobody has drained since
    # the day it was written and is the case this signal first existed for. A predicate narrowed
    # past its own subject with no fixture to notice is this repo's own vacuous-selector class.
    #
    # A row whose low-water could not be replayed is UNJUDGEABLE: counted, and never an offender.
    stalled = [r for r in rows if r["reason"] is not None]
    return {
        "signal": "shrink_only_lists_not_shrinking",
        "value": len(stalled),
        "of": len(rows),
        "unjudgeable": sum(1 for r in rows if r["low_water"] is None),
        "tolerance": 0,
        # Report, never gate: a list can legitimately sit still for a week. What it must not do is
        # sit still for a quarter while its own header calls it shrink-only.
        "gateable": False,
        "live": any(r["seed"] is not None for r in rows),
        "detail": rows,
    }


# --------------------------------------------------------------------------------------------
# Signal 4 — hand-kept inventories vs their generated source
# --------------------------------------------------------------------------------------------


def signal_handkept(ctx) -> dict:
    rows = []
    for spec in ctx.handkept:
        try:
            claims, actual = spec["probe"](ctx)
        except Exception as exc:  # a broken probe is reported, never silently skipped
            rows.append({"record": spec["record"], "claims": None, "actual": None,
                         "agrees": False, "error": repr(exc)})
            continue
        if isinstance(claims, (set, frozenset)) and isinstance(actual, (set, frozenset)):
            # A NAME-SET pair (TOOL-aMendedFleet-52 S1): a count pair cannot see a stale row standing
            # in for a missing one, so the row names both halves and stores counts, which `--json`
            # serialises where a set would not.
            rows.append({"record": spec["record"], "source": spec.get("source", "?"),
                         "claims": len(claims), "actual": len(actual),
                         "missing": sorted(actual - claims), "extra": sorted(claims - actual),
                         "agrees": claims == actual})
            continue
        rows.append({"record": spec["record"], "source": spec.get("source", "?"),
                     "claims": claims, "actual": actual, "agrees": claims == actual})
    # A MAGNITUDE, not a per-row boolean. Scored as a boolean over a one-row population the value
    # lived in {0, 1} against a pin of 1, so `value > pin` needed 2 and the ceiling was 1: gateable
    # in name, unsatisfiable in fact. Counting the items that disagree gives a number that can DRAIN
    # — one charter bullet at a time — and a pin that means something.
    gap = 0
    pop = 0
    for r in rows:
        if "missing" in r:
            # Symmetric difference over union: the union is every actual name plus each stale one.
            gap += len(r["missing"]) + len(r["extra"])
            pop += r["actual"] + len(r["extra"])
        elif isinstance(r.get("claims"), int) and isinstance(r.get("actual"), int) and r["claims"] >= 0:
            gap += max(0, r["actual"] - r["claims"])
            pop += r["actual"]
        elif not r["agrees"]:
            gap += 1          # a probe that raised, or one that cannot count: one offender
            pop += 1
    return {
        "signal": "handkept_inventories_disagreeing_with_source",
        "value": gap,
        "of": pop,
        "tolerance": 0,
        "gateable": True,
        # Judgeable population, not row count: an inventory with nothing IN it proves nothing.
        "live": pop > 0,
        "detail": rows,
    }


# --------------------------------------------------------------------------------------------
# Signal 5 — this node's auto-memory notes naming repo paths the tracked tree no longer carries
# --------------------------------------------------------------------------------------------
#
# TOOL-aMendedFleet-53. The name is kept for its readers (the history rows among them); the
# per-node ledger shard it used to read retired with the authored session ledger. What it reads now
# is the agent's auto-memory, declared by the project layer as AUTO_MEMORY_DIR.

_BACKTICKED = re.compile(r"`([^`\n]+)`")
_NOT_A_PATH = set("<>{}*?$|\"'\\")
_LINE_SUFFIX = re.compile(r":\d+$")


def resolve_auto_memory_dir(root: pathlib.Path, declared: str) -> pathlib.Path | None:
    """Expand an AUTO_MEMORY_DIR declaration; None when it is blank (NOT ASKED).

    `~` is the user's home. `{checkout}` is the PRIMARY checkout's absolute path with every
    character outside `[A-Za-z0-9-]` turned into `-` — how Claude Code keys a project's
    auto-memory. The primary checkout is the parent of the common git dir, so every worktree of one
    clone reads the same directory. If git cannot answer, the token stays unexpanded and the path
    names no directory, which the signal reports as DEAD with the path it tried."""
    declared = (declared or "").strip()
    if not declared:
        return None
    if "{checkout}" in declared:
        out = subprocess.run(["git", "-C", str(root), "rev-parse", "--path-format=absolute",
                              "--git-common-dir"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        common = out.stdout.strip()
        if out.returncode == 0 and common:
            key = re.sub(r"[^A-Za-z0-9-]", "-", str(pathlib.Path(common).parent))
            declared = declared.replace("{checkout}", key)
    return root / pathlib.Path(declared).expanduser()


def signal_dangling_pointers(ctx) -> dict:
    """Node-scoped ON PURPOSE: the notes live on this machine, so the value is this machine's and
    the record never gates. Each backticked span carrying a `/`, no whitespace and none of
    `< > { } * ? $ | " ' \\` is judged — after a trailing `:<digits>` and a trailing `/` go — when its
    first segment is a top-level entry of `git ls-files`; it resolves when it equals a tracked file
    or a directory prefix of one. The tracked set is the oracle, not the disk: an untracked
    leftover would make a stale note read as true."""
    name = "dangling_pointers_in_own_ledger"
    d = resolve_auto_memory_dir(ctx.root, ctx.auto_memory_dir)
    if d is None:
        return _build_not_asked(name, "the project layer declares no AUTO_MEMORY_DIR, so there is no "
                                      "node-local memory to audit")
    dead = {"signal": name, "value": -1, "of": 0, "tolerance": None, "gateable": False,
            "live": False, "unjudgeable": 0}
    if not d.is_dir():
        return {**dead, "detail": [{"note": f"DEAD PROBE — AUTO_MEMORY_DIR resolves to {d}, "
                                            f"which is not a directory on this node"}]}
    files = [f for f in ctx.git.run("ls-files", "-z").stdout.split("\0") if f]
    dirs = {f[:i] for f in files for i, c in enumerate(f) if c == "/"}
    tops = {f.split("/", 1)[0] for f in files}
    tracked = set(files) | dirs
    judged, unreadable = set(), 0
    for note in sorted(d.glob("*.md")):
        try:
            text = note.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            unreadable += 1
            continue
        for tok in _BACKTICKED.findall(text):
            if "/" not in tok or any(c.isspace() or c in _NOT_A_PATH for c in tok):
                continue
            tok = _LINE_SUFFIX.sub("", tok).rstrip("/")
            if tok and tok.split("/", 1)[0] in tops:
                judged.add((note.name, tok))
    if not judged:
        return {**dead, "unjudgeable": unreadable,
                "detail": [{"note": f"DEAD PROBE — no note under {d} names a judgeable repo path"}]}
    gone = sorted(p for p in judged if p[1] not in tracked)
    return {
        "signal": name,
        "value": len(gone),
        "of": len(judged),
        # Pinless (TOOL-aMendedFleet-51): the value is one machine's notes, so a committed pin
        # would be another node's wrong answer.
        "tolerance": None,
        "gateable": False,
        "live": bool(judged),
        "unjudgeable": unreadable,
        "detail": [{"note_file": n, "path": p} for n, p in gone],
    }


# --------------------------------------------------------------------------------------------
# Signal 6 — CLOSED specs with no commit that both names them and changed the product
# --------------------------------------------------------------------------------------------

# The status header's date, which TEMPLATE-SPEC defines as the LAST-CHANGE date — so on a CLOSED
# spec it is the close date. Keyed on deliberately instead of the FILENAME date, which is the WRITE
# date: measured on the dogfood, a filename key exempted 18 specs still in flight, every one of which
# will close under the convention this signal judges. Both keys select the same population today.
_HEADER_DATE = re.compile(r"^\*\*Status:\*\*[^\n]*?(\d{4}-\d{2}-\d{2})", re.M)
# CLOSED only. WONTDO is terminal too and is deliberately NOT judged: an abandoned unit correctly has
# no product commit, so judging it would manufacture a permanent false positive out of a true record.
TERMINAL = frozenset({"CLOSED"})
# TOOL-aMendedFleet-91. A unit whose deliverable is records declares it in its OWN status header, at
# speccing time where its review reads it, as a whole `·`-separated tail field of exactly these bytes.
# Matched on the status line alone, so `records-only-ish` and a sentence in the body exempt nothing.
_RECORDS_ONLY = re.compile(r"·\s*records-only\s*(?:·|$)")


def signal_closed_specs_untraceable(ctx) -> dict:
    """The mirror of `signal_spec_status`. That one asks whether a spec claiming NOT-DONE is
    contradicted by product source; this one asks whether a spec claiming DONE is supported by any
    commit at all. Together they cover both ways a status can lie about git.

    WHAT THIS DOES NOT MEASURE, stated because a linkage signal is easy to read as a fidelity one: it
    proves a commit exists that names the unit and touched the product. It cannot tell whether that
    commit implemented the spec. A build that cites its unit correctly and builds something else
    passes. Fidelity is the spec audit and the closing review, and it stays there.
    """
    if not ctx.trace_cutoff:
        # UNSET is not "clean" and not "dead" — it is NOT ASKED. Returning gateable:False is what
        # makes that distinction reach `--check`, which reds a gateable signal whose population is
        # empty. Doing this in the ENGINE rather than through the project layer's DECLARED_EMPTY is
        # deliberate: that set lives in each adopter's own file, so it reaches neither this kit's
        # test fixture nor an adopter who has not edited theirs, which is exactly where the
        # dead-and-undeclared red would land on people who did nothing wrong.
        return {"signal": "closed_specs_with_no_product_commit", "value": 0, "of": 0,
                "tolerance": 0, "gateable": False, "live": False, "unjudgeable": 0,
                "detail": [{"note": "TRACE_CUTOFF is not set in the project layer; nothing judged"}]}

    # ONE walk, over BOTH tips. The spec population is read from the working tree, so the evidence
    # must be too — a unit that flips its own spec to CLOSED on its branch has its certifying commits
    # on that branch and nowhere else, and `base_ref` alone cannot see them. Measured on the dogfood:
    # replaying the judged specs at the commit the default branch sat on immediately before each
    # CLOSED flip landed, a base-only walk reds 2 of 13 CORRECT closes. The `drift-audit records` leg
    # carries an empty guard, so it runs on every branch-scoped bar — which is precisely when.
    #
    # `--full-history` because `--no-merges` does NOT defeat default history simplification: a
    # path-restricted walk drops a commit that is TREESAME with a parent, so a build's own
    # product commit can vanish behind an unrelated merge and score a false MISS. Reproduced in
    # a scratch repo with an `-s ours` merge. An earlier comment here claimed --no-merges
    # settled the traversal question; the selftest's merge arm said the opposite, and the
    # selftest was right.
    #
    # `--no-merges` because a reconcile merge's subject names the branch being merged INTO, so it
    # certifies whichever build it was merged into rather than the build that shipped. Measured: with
    # merges counted this signal read 0 on the dogfood and one of those greens rested entirely on two
    # merge subjects belonging to another build. Dropping them also removes the default
    # history-simplification ambiguity, which would otherwise decide the answer by accident.
    walk = ctx.git.run("log", ctx.git.base_ref, "HEAD", "--no-merges", "--full-history",
                       "--format=%s", "--", *ctx.trace_globs)
    subjects = walk.stdout if walk.returncode == 0 else ""

    # THE WAIVER, named by this signal's own spec BEFORE the first instance existed, so the first
    # occurrence could not be resolved by the ratchet it would defeat: a CLOSED unit that leaves no
    # TRACE_GLOBS subject naming it gets a per-spec row here, NEVER a raised pin. Two shapes reach
    # it — a unit whose deliverable is records-only, and a unit whose product landed BEFORE the
    # id-in-subject convention but whose header date crosses TRACE_CUTOFF when it finally closes.
    # The second is the residual the header-date key knowingly trades in, and this is where
    # cTracedPromise-1 §3 sends it, in writing, rather than to the pin.
    #
    # WHAT A ROW DOES NOT BUY: it asserts only that no subject CAN name this unit, never that the
    # unit was built or built faithfully. It suppresses one linkage finding and nothing else.
    #
    # The unused-row sweep below is what makes this an exemption rather than a hole. A row is
    # consumed only by a spec that is present, terminal and still untraceable; any row left over
    # becomes a finding in its own right, because a waiver outliving its subject silently widens
    # the surface it was written to narrow.
    waived: dict[str, str] = {}
    # THE PATH IS DECLARABLE (TOOL-dMuffledSentinel-2), and a DECLARED path must resolve. The default
    # may be absent, which is how an adopter with nothing to waive starts. A declared one may not: the
    # only reason to declare it is to use it, and one that does not resolve reads exactly like having
    # nothing waived. So it becomes a row of its own, carried the way a stale waiver is.
    declared = ctx.trace_waiver
    bad_declaration = ""
    if declared:
        posix = pathlib.PurePosixPath(declared.replace("\\", "/"))
        if posix.is_absolute() or pathlib.PureWindowsPath(declared).is_absolute() or ".." in posix.parts:
            bad_declaration = "is not a repo-relative path inside the tree"
        elif not (ctx.root / posix).is_file():
            bad_declaration = "names a file that is not there, so nothing it would waive is waived"
    wpath = ctx.root / (declared or f"{ctx.memory_root}/project/trace-waiver.txt")
    if not bad_declaration and wpath.is_file():
        for raw_row in wpath.read_text(encoding="utf-8", errors="replace").splitlines():
            if not raw_row.strip() or raw_row.lstrip().startswith("#"):
                continue
            cols = raw_row.split("\t")
            waived[cols[0].strip()] = cols[-1].strip() if len(cols) > 1 else ""
    used: set[str] = set()

    suspect, checked, unjudged, records_only = [], 0, 0, []
    for p in sorted(ctx.root.glob(f"{ctx.memory_root}/builds/*/spec/**/*.md")):
        head = p.read_text(encoding="utf-8", errors="replace")[:4000]
        m = _STATUS.search(head)
        if not m or m.group(1).upper() not in TERMINAL:
            continue
        own, when = ctx.own_id_re.search(head), _HEADER_DATE.search(head)
        if not own or not when:
            unjudged += 1  # no id or no header date: the probe cannot judge it. Counted, not guessed.
            continue
        if when.group(1) < ctx.trace_cutoff:
            unjudged += 1  # grandfathered: it closed before the convention it would be judged by.
            continue
        uid, slug = own.group(1), _parse_slug(own.group(1))
        if slug is None:
            unjudged += 1  # an era with no slug: this BUILD-level question has no key here.
            continue
        # AFTER the guard, never before it. The two earlier unjudged paths `continue` above this
        # line; the slug guard was added below it, so a pre-slug-era id landed in BOTH the judged
        # denominator and the unjudged count, and a corpus that was entirely pre-slug read as live.
        checked += 1
        rel = str(p.relative_to(ctx.root)).replace("\\", "/")
        # BEFORE the slug join, so no sibling's product commit, present or absent, moves the reading.
        # A waiver row naming this spec is then left unconsumed and the sweep below reports it: the
        # same fact declared in two places is a finding, not a silence.
        if _RECORDS_ONLY.search(head[m.start():].split("\n", 1)[0].rstrip()):
            records_only.append(rel)
            continue
        # SLUG ONLY, and that is not a narrowing: `\bslug\b` already matches inside
        # `FAMILY-slug-seq`, because the hyphens either side of the slug are non-word bytes.
        # An `id or slug` disjunct reads like a two-key oracle and is one unfalsifiable clause;
        # the id half could never decide a case the slug half did not already decide.
        if re.search(r"\b" + re.escape(slug) + r"\b", subjects):
            continue
        if rel in waived:
            used.add(rel)
            continue
        suspect.append({
            "file": rel, "id": uid, "slug": slug, "closed": when.group(1),
        })
    # A row left OVER is a finding, not a silence. Same shape as the append above so `--check`,
    # the gate leg and the JSON detail all carry it without a second code path.
    for rel in sorted(set(waived) - used):
        suspect.append({
            "file": rel, "id": "(stale waiver)", "slug": "(stale waiver)", "closed": "",
            "note": "waives a spec that is absent, not terminal, traceable again, or declaring "
                    "records-only in its own status header",
        })
    if bad_declaration:
        suspect.append({
            "file": declared, "id": "(declared TRACE_WAIVER)", "slug": "(declared TRACE_WAIVER)",
            "closed": "", "note": f"TRACE_WAIVER {bad_declaration}",
        })
    return {
        "signal": "closed_specs_with_no_product_commit",
        "value": len(suspect),
        "of": checked,
        "tolerance": 0,
        "gateable": True,
        "live": checked > 0,
        "unjudgeable": unjudged,
        "detail": suspect,
        "records_only": sorted(records_only),
    }


def _resolve_lexicon_conf(ctx):
    """The lexicon's declaration, or None. The two signals below are the ONLY place this shipped
    engine names an optional kit, and the guard is what makes that acceptable: an adopter without
    the lexicon gets `gateable: False`, never a raise and never a red."""
    p = ctx.root / ".lexicon.conf"
    return p if p.is_file() else None


def _load_lexicon(ctx):
    """`(VERBS, ratified, LANGS)` through the lexicon's own reader, or None if it is unreachable.

    RETURNS None RATHER THAN RAISING, and that is load-bearing. `main()` evaluates every signal in
    one unguarded comprehension, so an exception here does not degrade THIS signal — it kills all
    eight and takes the `--check` gate leg with it, on a repo that may not even use the lexicon.
    A conf can exist without the kit importable at this prefix in at least three real states: a
    root-prefix adopter, a mid-teardown tree, and a malformed conf (`ConfError`). The docstring above
    promised "never a raise and never a red"; this is what keeps that true.
    """
    import sys as _sys
    try:
        kit = str(resolve_kit_dir("lexicon", "lexicon_conf.py", pathlib.Path(__file__).resolve().parent))
    except LookupError:
        return None
    if kit not in _sys.path:
        _sys.path.insert(0, kit)
    try:
        from lexicon_conf import load_conf
        conf = load_conf(_resolve_lexicon_conf(ctx))
    except Exception:
        return None
    return (conf.get("VERBS") or {}), (conf.get("ratified") or "").strip(), (conf.get("LANGS") or "")


def _resolve_lexicon_sets(ctx, lex):
    """The lexicon's RESOLVED pattern sets — the shipped ones plus whatever `.lexicon.conf` declares.

    BOTH SIGNALS BELOW MUST READ THE RESOLUTION, never the shipped constant. They each tested
    `pset not in lex.PATTERN_SETS` and skipped, so a language armed only through a `PATTERNS:` row
    was passed over file by file while the signal reported a clean number with `live` still true off
    the Python half. That is green-by-absence on a GATEABLE signal, and it lands inside the one
    instrument whose whole value is that both of its operands come from one extractor.

    Falls back to the shipped constant on any failure, for the same reason `_load_lexicon` returns
    None rather than raising: `main()` evaluates every signal in one unguarded comprehension, and an
    adopter whose conf is momentarily unreadable must not lose the other seven. TOOL-aSurfacedLexicon-9.
    """
    try:
        from lexicon_conf import load_conf
        return lex.resolve_pattern_sets(load_conf(_resolve_lexicon_conf(ctx)))
    except Exception:
        return lex.PATTERN_SETS


def _build_not_asked(name, why):
    """NOT ASKED is neither clean nor dead — and it must not RENDER as dead either.

    `live: False` alone made the human table print "DEAD PROBE — signal cannot move" for every
    adopter who simply does not use the lexicon, which is a false alarm reported as a defect. The
    `not_asked` flag is what the renderer branches on so the three states stay three."""
    return {"signal": name, "value": 0, "of": 0, "tolerance": 0, "gateable": False,
            "live": False, "not_asked": True, "unjudgeable": 0, "detail": [{"note": why}]}


def signal_lexicon_verbs_unused(ctx) -> dict:
    """Verbs DECLARED in the table that no definition in the corpus leads with.

    The closure question from the OUTLIVING side: `codebase-map`'s ratchet catches the table growing,
    and nothing else catches a verb surviving the code that justified it. This is a
    record-versus-reality question, which is why it is a drift SIGNAL and not a gate predicate — a
    declared-but-unused verb violates nothing, and it is the sort of fact that is true for weeks
    before anyone should act on it.

    THE DAY-ONE SEED IS NOT ZERO, and that is correct rather than a failed build. `--scaffold` seeds a
    concept only when the corpus has a live site for it, but it spells that concept the CANON's way,
    and a human then curates -- and curation ADDS aspirational verbs the corpus does not use yet.
    Same shape as `non_terminal_specs_cited_by_product_source`, whose pin comment records a known
    residual rather than proven rot.
    """
    name = "lexicon_verbs_declared_but_unused"
    if not _resolve_lexicon_conf(ctx):
        return _build_not_asked(name, "no .lexicon.conf at the repo root; the lexicon kit is not adopted")
    loaded = _load_lexicon(ctx)
    if loaded is None:
        return _build_not_asked(name, ".lexicon.conf is present but its kit is not importable here "
                                      "(root-prefix install, mid-teardown, or an unparseable conf)")
    import sys as _sys
    try:
        kit = str(resolve_kit_dir("lexicon", "lexicon.py", pathlib.Path(__file__).resolve().parent))
    except LookupError as e:
        return _build_not_asked(name, str(e))
    if kit not in _sys.path:
        _sys.path.insert(0, kit)
    try:
        import lexicon as lex
        from lexicon_conf import langs as _langs
    except Exception:
        return _build_not_asked(name, "the lexicon engine is not importable here; nothing judged")

    verbs, _ratified, _l = loaded
    if not verbs:
        return _build_not_asked(name, ".lexicon.conf declares no VERBS; nothing to judge")

    # THE ARMED SET COMES FROM `_build_armed_exts` RATHER THAN FROM A SECOND COPY OF ITS CONDITION.
    # This loop re-derived "which extensions can actually be read" inline, which is how the H1 crash
    # reached two call sites from one defect: the sibling gained the unshipped-parser drop and this
    # one would not have. `KeyError` joins the `except` tuple as the belt to that braces — the
    # promise `_load_lexicon` makes is that a bad declaration never raises out of a signal, and a
    # promise carried by one guard is a promise one edit away from being false.
    sets = _resolve_lexicon_sets(ctx, lex)
    declared = _build_armed_exts(_l, lex, _langs, sets)
    used: set[str] = set()
    for rel in lex.tracked_files(ctx.root):
        ext = lex.ext_of(rel)
        if ext not in declared:
            continue
        pset, mode = declared[ext]
        try:
            got = lex.extract(ctx.root / rel, mode, pset, sets=sets)
        except (SyntaxError, OSError, KeyError):
            continue
        if not got:
            continue
        for nm, _ln in got[0]:
            v = lex.leading_verb(nm)
            if v:
                used.add(v)

    unused = sorted(v for v in verbs if v not in used)
    return {"signal": name, "value": len(unused), "of": len(verbs), "tolerance": 0,
            "gateable": True, "live": bool(used), "unjudgeable": 0,
            "detail": [{"verb": v, "note": "declared in VERBS, used by no definition"} for v in unused]}


def signal_lexicon_ratified_stale(ctx) -> dict:
    """Has the declared LANGUAGE SURFACE moved since a human last ratified the table?

    `ratified` is the checkable form of "a human curated this". It says nothing about WHEN, so a
    table ratified before a language was added is a curated vocabulary certifying a corpus it never
    saw. Compared by COMMIT DATE rather than by the stamp's own text: the stamp is authored and the
    thing it must outlive is not.
    """
    name = "lexicon_ratified_older_than_language_surface"
    conf = _resolve_lexicon_conf(ctx)
    if not conf:
        return _build_not_asked(name, "no .lexicon.conf at the repo root; the lexicon kit is not adopted")
    loaded = _load_lexicon(ctx)
    if loaded is None:
        return _build_not_asked(name, ".lexicon.conf is present but its kit is not importable here "
                                      "(root-prefix install, mid-teardown, or an unparseable conf)")
    _verbs, ratified, _l = loaded
    if not ratified:
        return _build_not_asked(name, ".lexicon.conf carries no ratified stamp; adopt-lexicon.sh --check owns that")

    stamp = ratified.split()[0]
    # `-G`, not `-S`. `-S` counts OCCURRENCES of the string: `LANGS=` appears exactly once before
    # and once after a value is widened, so an in-place edit is invisible and this lookup froze at the
    # adoption commit forever — a permanent, reassuring zero on a GATEABLE signal. Measured on a
    # two-commit fixture: -S sees only `add`, -G sees `widen` and `add`.
    found = ctx.git.run("log", "-1", "--format=%cI %H", "-G", "LANGS=", "--", ".lexicon.conf").stdout.strip()
    langs_at, _, langs_sha = found.partition(" ")
    if not langs_at:
        return _build_not_asked(name, "no commit yet touches the LANGS declaration; nothing to compare")
    stale = langs_at[:10] > stamp
    return {"signal": name, "value": 1 if stale else 0, "of": 1, "tolerance": 0,
            "gateable": True, "live": bool(langs_at and stamp), "unjudgeable": 0,
            "detail": ([{"ratified": stamp, "langs_changed": langs_at[:10], "langs_commit": langs_sha,
                         "note": "the declared language surface moved after the table was ratified"}]
                       if stale else []),
            "langs_commit": langs_sha}


def _build_armed_exts(langs_value, lex, _langs, sets):
    """`{ext: (pset, mode)}` for the extensions an extractor can actually READ. Dark and
    unknown-pattern-set extensions are dropped here, so both operands are derived over the same
    population and a `LANGS` edit moves both ends together rather than one.

    `sets` is the RESOLVED mapping and is required rather than defaulted: the shipped constant was
    what this test read before, and reading it silently narrowed the population to the languages the
    kit happens to ship. A default here would let a future caller re-earn that by omission.

    AN UNSHIPPED `parser` ID IS DROPPED HERE TOO, and that arm is closing review H1. This function
    dropped `dark` and unknown-`probe` rows and KEPT a `parser` row naming a pattern set the kit does
    not ship — the engine ships `python-ast` and `shell-tokens` only — so `extract_text` reached
    `PARSERS[pset]` and raised `KeyError`. Neither `except` tuple downstream covers that and
    `main()` evaluates every signal unguarded, so ONE legal-looking `LANGS` row cost all eight
    signals and a traceback, on a leg carrying no guard. `_load_lexicon`'s docstring promises "never
    a raise and never a red" for exactly this class, and the engine's own `scan_corpus` already
    refuses the same row by name — so the two readers of one declaration disagreed. The crash path
    is new: before TOOL-aSurfacedLexicon-14 the `parser` arm ignored its set id entirely.

    `lex.PARSERS` IS READ, NEVER RESTATED. A second copy of the shipped parser ids here is the
    two-carriers class inside the fix for two readers disagreeing."""
    out = {}
    for ext, pset, mode in _langs({"LANGS": langs_value}):
        if mode == "dark" or (mode == "probe" and pset not in sets):
            continue
        if mode == "parser" and pset not in lex.PARSERS:
            continue
        out[ext] = (pset, mode)
    return out


def _read_defs_at_sha(ctx, sha, armed, lex, sets):
    """`{(path, name)}` — every function definition an armed extractor sees in the tree at `sha`.

    ONE `git cat-file --batch` for the whole tree, not one read per file. Measured on node `d`: the
    per-file shape cost 2.774 s for both shas at 108 spawns, and this box taxes every exec by roughly
    0.022 s (`memory/gotchas/process-creation-is-the-suite-cost.md`), so 108 spawns IS 2.4 s of that.
    The cost here is spawn count rather than compute, and the batched read is what keeps it off the
    signal's budget.
    """
    listing = ctx.git.run("ls-tree", "-r", sha)
    if listing.returncode != 0:
        return None
    want = []
    for line in listing.stdout.splitlines():
        meta, _, path = line.partition("\t")
        bits = meta.split()
        if len(bits) < 3 or bits[1] != "blob" or lex.ext_of(path) not in armed:
            continue
        want.append((bits[2], path))
    if not want:
        return set()
    batch = subprocess.run(
        ["git", "-C", str(ctx.root), "cat-file", "--batch"],
        input="".join(b + "\n" for b, _ in want).encode(),
        capture_output=True,
    )
    if batch.returncode != 0:
        return None
    defs, buf, i = set(), batch.stdout, 0
    for _blob, path in want:
        nl = buf.find(b"\n", i)
        if nl < 0:
            return None
        header = buf[i:nl].split()
        if len(header) < 3:
            return None
        size = int(header[2])
        src = buf[nl + 1: nl + 1 + size].decode("utf-8", errors="replace")
        i = nl + 1 + size + 1
        pset, mode = armed[lex.ext_of(path)]
        try:
            got = lex.extract_text(src, mode, pset, sets=sets)
        except (SyntaxError, ValueError, KeyError):
            continue
        if got:
            for nm, _ln in got[0]:
                defs.add((path, nm))
    return defs


def build_lexicon_marginal_offense_rate(ctx) -> dict:
    """Offenders ADDED per definition ADDED, between the commit that adopted the declaration and HEAD.

    THE ONLY INSTRUMENT HERE THAT MEASURES THE THING THE KIT IS FOR: are new generations constrained.
    Both operands are DERIVED at both shas by the lexicon's own extractor, so there is nothing
    authored and nothing raisable — no pin, no threshold, no knob that shortens the window.

    WHAT KILLS THE PRESSURE CHAIN, stated here rather than in a spec nobody re-reads. If the rate over
    files written FRESH in the window stays at or below roughly 5% across two further readings, the
    pressure chain — `TOOL-dScaffoldedMirror-4`, `-9`, and `-11`'s cut fourth pin — should be
    ABANDONED rather than deferred: that reading says the declaration already constrains the
    generations and the enforcement half is buying nothing. A rate that CLIMBS in fresh files across
    two readings is the evidence `-9` was always missing, and promotes it from probation to scheduled.
    Either way the decision is a reading and not an argument, which is what the plan lacked.

    THE OPERANDS ARE PART OF THE CONTRACT, not an implementation detail (S3). A definition is a
    `(path, name)` pair from the armed extractors; ADDED is present at HEAD and absent at base; an
    OFFENDER is an added pair whose leading token is outside the table AT HEAD. Keying on `(path,
    name)` rather than the bare name is deliberate — a definition that moved file would otherwise read
    as deleted and re-added, inflating both operands.

    NOT the `assertion-between-two-derived-values` class, and the distinction is precise: the same
    code derives both operands from TWO DIFFERENT SOURCES — the tree at the base and the tree at HEAD
    — and a commit's content is exogenous to this checker. The comparison can disagree, and it did.

    NAMED `build_`, following `build_live_backlog_rows`, which already wrote this rule down: a new
    definition can be named right for free. Its spec's rev-1 argued the opposite and proposed raising
    `VERB_OFFENDER_PIN` to fit; the comment forty lines below refuted it before it was written.
    """
    name = "lexicon_marginal_offense_rate"
    if not _resolve_lexicon_conf(ctx):
        return _build_not_asked(name, "no .lexicon.conf at the repo root; the lexicon kit is not adopted")
    loaded = _load_lexicon(ctx)
    if loaded is None:
        return _build_not_asked(name, ".lexicon.conf is present but its kit is not importable here")
    import sys as _sys
    try:
        kit = str(resolve_kit_dir("lexicon", "lexicon.py", pathlib.Path(__file__).resolve().parent))
    except LookupError as e:
        return _build_not_asked(name, str(e))
    if kit not in _sys.path:
        _sys.path.insert(0, kit)
    try:
        import lexicon as lex
        from lexicon_conf import langs as _langs
    except Exception:
        return _build_not_asked(name, "the lexicon engine is not importable here; nothing judged")

    verbs, _ratified, langs_value = loaded
    if not verbs:
        return _build_not_asked(name, ".lexicon.conf declares no VERBS; nothing to judge")

    # S2 — the base is DERIVED, never declared. A knob that shortens the window hides the stretch it
    # removes, so the only base is the fact of when the declaration started existing.
    adopt = ctx.git.run("log", "--diff-filter=A", "--format=%H", "--", ".lexicon.conf")
    shas = [s for s in adopt.stdout.split() if s] if adopt.returncode == 0 else []
    base = shas[-1] if shas else ""
    head = ctx.git.run("rev-parse", "HEAD").stdout.strip()

    # L1 — the history is COMPLETE. Measured, and it corrects this unit's own spec: rev-2 asserted a
    # shallow clone makes the base unresolvable. It does not. `git log --diff-filter=A` there returns
    # the SHALLOW ROOT as the commit that "added" the file, and that sha resolves perfectly — so a
    # resolves-check is armed against a case it can never see, and the signal would report a rate over
    # a one-commit window as though it were the real one. Observed in a `--depth 1` clone: derived base
    # 37bfdd19, the only commit present, against a true adoption commit of b0626152.
    #
    # Asking whether the REPOSITORY is truncated is the assertion that actually fires. A derived base
    # is only as trustworthy as the history it was derived from.
    if ctx.git.run("rev-parse", "--is-shallow-repository").stdout.strip() == "true":
        return {"signal": name, "value": 0, "of": 0, "tolerance": None, "gateable": False,
                "live": False, "unjudgeable": 0,
                "detail": [{"note": "DEAD PROBE — this is a shallow clone, so the commit that added "
                                    ".lexicon.conf is not necessarily present and a derived base "
                                    "cannot be trusted; no rate is derived"}]}

    # L1b — and the base still has to resolve, for a grafted or otherwise mangled history.
    if not base or not ctx.git.is_commit(base):
        return {"signal": name, "value": 0, "of": 0, "tolerance": None, "gateable": False,
                "live": False, "unjudgeable": 0,
                "detail": [{"note": "DEAD PROBE — the commit that added .lexicon.conf does not "
                                    "resolve in this object store (a shallow or grafted clone); "
                                    "no rate is derived"}]}

    # NO CACHE, and that is a rev-4 cut with a measurement behind it. The spec asked for a per-sha
    # cache keyed on the table digest, sized against a per-file read costing 2.774 s for both shas.
    # The batched read below already costs 0.957 s cold inside a 3.7 s report that is not on the
    # merge bar, so the cache was specced against a cost that no longer exists — and an in-process
    # dict never survives to a second run anyway, which is a moving part with no consumer.
    sets = _resolve_lexicon_sets(ctx, lex)
    armed = _build_armed_exts(langs_value, lex, _langs, sets)
    at_base = _read_defs_at_sha(ctx, base, armed, lex, sets)
    at_head = _read_defs_at_sha(ctx, head, armed, lex, sets)
    # L2 and L3 — a population that is empty at either end means the extractor is not reading, which
    # is indistinguishable from a clean window unless it is said out loud.
    if at_base is None or at_head is None or not at_base or not at_head:
        return {"signal": name, "value": 0, "of": 0, "tolerance": None, "gateable": False,
                "live": False, "unjudgeable": 0,
                "detail": [{"note": "DEAD PROBE — the definition population is empty at the base or "
                                    "at HEAD, so the extractor is not reading this tree",
                            "at_base": len(at_base or ()), "at_head": len(at_head or ())}]}

    added = at_head - at_base
    # S6 — nobody added a definition is a REAL state (a records-only stretch) and is NOT a rate of 0.
    if not added:
        return _build_not_asked(name, "no definition was added between the declaration's adoption "
                                      "commit and HEAD; there is no marginal rate to report")

    # UNGRADEABLE NAMES LEAVE BOTH OPERANDS. `leading_verb` returns "" for an identifier with no word
    # characters, and `subtokens.py` says plainly that the caller must treat that as ungradeable
    # rather than as a violation -- but "" is not in `verbs`, so it counted as an offender AND stayed
    # in the denominator, inflating the rate at both ends. Closing review L4.
    gradeable = {(p, n) for p, n in added if lex.leading_verb(n)}
    if not gradeable:
        # THE EMPTINESS GUARD MOVED WITH THE OPERANDS. The round-1 L4 fix pointed every consumer at
        # `gradeable` and left the `if not added` guard above it reading `added`, so a window whose
        # every added definition was ungradeable fell through to the ordinary return with value 0,
        # of 0, live True and no `not_asked` -- and `0 > 0` is false, so it printed a plain `ok`.
        # That is this signal's own stated failure class handed back to it: the docstring says an
        # empty population at either end is indistinguishable from a clean window unless it is said
        # out loud. Found by the round-2 review, which built the window and observed the `ok`.
        return _build_not_asked(
            name, "every definition added since the declaration was adopted has a name with no word "
                  "characters, so this window holds nothing gradeable")
    offenders = {(p, n) for p, n in gradeable if lex.leading_verb(n) not in verbs}
    base_files = {p for p, _ in at_base}
    fresh = [x for x in gradeable if x[0] not in base_files]
    fresh_off = [x for x in fresh if x in offenders]
    pre = [x for x in gradeable if x[0] in base_files]
    pre_off = [x for x in pre if x in offenders]

    def _measure_pct(a, b):
        return round(100.0 * len(a) / len(b), 1) if b else 0.0

    return {"signal": name, "value": len(offenders), "of": len(gradeable), "tolerance": None,
            "gateable": False, "live": bool(at_base and at_head), "unjudgeable": 0,
            "detail": [
                {"note": "offenders added per definition added since the declaration was adopted",
                 "base": base[:8], "head": head[:8], "rate_pct": _measure_pct(offenders, gradeable)},
                {"note": "files written FRESH in the window — the reading the kill-rule watches",
                 "added": len(fresh), "offenders": len(fresh_off), "rate_pct": _measure_pct(fresh_off, fresh)},
                {"note": "files that predate the declaration",
                 "added": len(pre), "offenders": len(pre_off), "rate_pct": _measure_pct(pre_off, pre)},
            ]}


# --------------------------------------------------------------------------------------------
# Signal 9 — live backlog rows per shard (TOOL-aRelaxedShard-4)
#
# The bound that actually moves. Non-terminal rows survive a rotation under either declared
# ROTATION_MODE, so a shard's FLOOR is its live set: when nothing terminal is left, rotating is a no-op and the next row breaches the
# byte cap. That is how `TOOL-cSettledDocket-16` and `TOOL-aRelaxedShard-1` happened, twice, and
# neither the byte cap nor the map ratchet can see it coming.
#
# REPORT-ONLY, deliberately. `drift-audit records` is an unguarded merge-bar leg, so a pin set N days
# ahead of today's count becomes a scheduled refusal: the day the count crosses it every merge reds
# until someone raises the pin or closes rows, which is the refusal this signal exists to make
# unnecessary. `shrink_only_lists_not_shrinking` runs the same way for the same reason. If a later
# unit gates this, it must pin a MEASURED value with a movement rule AND give the record a numeric
# tolerance — a gateable record with a None one trips the engine's assertion in `main` — AND declare
# that pin in the shipped conf template.
#
# PINLESS since TOOL-aMendedFleet-51: `tolerance` is None and the status column prints `report only,
# no pin`. Under `BACKLOG_MODE="builds"` the reading is every live ask, which rises with every ask
# filed, and the shard-rotation floor the old watermark guarded no longer exists. A project that
# still wants a pin declares one in its PINS, and the status column then compares against it.
#
# The terminal set is SPELLED HERE. `.memory-tree.conf` declares no status vocabulary and no sibling
# module exposes one, so there is nothing to borrow; the engine already hardcodes the same tokens for
# hygiene check 8. Naming the duplication beats claiming a reuse that does not exist.
_TERMINAL_STATUSES = ("CLOSED", "WONTDO")


# NAMED `build_`, NOT `signal_`, deliberately. Its eight siblings in SIGNALS all lead with `signal`,
# which is a NOUN and not in `.lexicon.conf`'s VERBS table — they sit inside `VERB_OFFENDER_PIN` as
# grandfathered debt that `TOOL-aWiredReckoning-1` will curate. A new definition can be named right for
# free, and adding a ninth offender to spare a symmetry break would be paying the debt down in the wrong
# direction. `build` is the declared verb for "create a new value and return it", which is what this does.
def read_backlog_mode(ctx) -> str:
    """`BACKLOG_MODE` as the memory-tree kit reads it: blank or absent is `shards`."""
    return (ctx.conf.get("BACKLOG_MODE") or "").strip() or "shards"


def _resolve_index_generator():
    """The memory-tree kit's index generator, through `resolve_kit_dir` like every sibling lookup."""
    try:
        kit = resolve_kit_dir("memory-tree", "gen_build_index.py", pathlib.Path(__file__).resolve().parent)
    except LookupError:
        return None
    return kit / "gen_build_index.py"


def read_asks_projection(ctx, all_rows: bool):
    """`(rows, examined, note)` from `gen_build_index.py --asks [--all] --json`, run ONCE per shape.

    THE GENERATOR'S FOLD AND NOBODY ELSE'S (TOOL-dDerivedDocket-34 section 8 F14). Every builds-mode
    backlog signal reads this projection and implements no second liveness or status rule: the live
    shape is the generator's own filter, the `--all` shape its whole corpus. Cached on the context,
    because four signals read two shapes and each read is a process. `rows` is None when the
    projection could not be read, and `note` says why.
    """
    cache = ctx.__dict__.setdefault("_asks_projection", {})
    if all_rows in cache:
        return cache[all_rows]
    gen = _resolve_index_generator()
    if gen is None:
        cache[all_rows] = (None, 0, "the memory-tree kit is not installed beside this one")
        return cache[all_rows]
    argv = [sys.executable, str(gen), "--asks", "--json"] + (["--all"] if all_rows else [])
    try:
        out = subprocess.run(argv, cwd=str(ctx.root), capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=600)
        doc = json.loads(out.stdout) if out.returncode == 0 else None
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        cache[all_rows] = (None, 0, f"the ask projection could not be read: {exc}")
        return cache[all_rows]
    if not isinstance(doc, dict) or not isinstance(doc.get("asks"), list):
        said = ((out.stderr or "").strip().splitlines() or [f"exit {out.returncode}"])[-1]
        cache[all_rows] = (None, 0, f"the ask projection printed no ask list: {said[:240]}")
        return cache[all_rows]
    cache[all_rows] = (doc["asks"], int(doc.get("examined") or 0), "")
    return cache[all_rows]


def read_tracked_asks(ctx) -> list:
    """Every tracked per-build `BACKLOG.md`. None tracked is NOT ASKED, never a clean zero."""
    return [ln for ln in ctx.git.run("ls-files", f"{ctx.memory_root}/builds/*/BACKLOG.md")
            .stdout.splitlines() if ln.strip()]


def build_live_backlog_rows(ctx) -> dict:
    """Live asks: per backlog shard under `shards`, from the ask projection under `builds`.

    NEVER GATED either way. Under `builds` the reading is the length of `--asks --json`, the
    generator's LIVE projection, with no status filter of this kit's own: `_TERMINAL_STATUSES` below
    stays the shards reading's filter and is never applied to a derived status (section 8 F14 of
    TOOL-dDerivedDocket-34). The detail carries one row per family, so a total cannot hide one
    family growing inside another.
    """
    if read_backlog_mode(ctx) == "builds":
        rows, examined, note = read_asks_projection(ctx, all_rows=False)
        if rows is None:
            return {"signal": "live_backlog_rows_per_shard", "value": 0, "of": 0,
                    "tolerance": None,
                    "gateable": False, "live": False, "detail": [{"note": note}]}
        per: dict = {}
        for row in rows:
            fam = str(row.get("id", "")).split("-")[0]
            per[fam] = per.get(fam, 0) + 1
        return {
            "signal": "live_backlog_rows_per_shard",
            "value": len(rows),
            "of": examined,
            "tolerance": None,
            "gateable": False,
            # LIVENESS FROM THE FILES THE PROJECTION READ. A builds-mode tree whose projection
            # examined no ask file cannot move this count.
            "live": examined > 0,
            "detail": [{"family": f, "live": n} for f, n in sorted(per.items())],
        }
    shard_dir = f"{ctx.memory_root}/backlog"
    tracked = [ln for ln in ctx.git.run("ls-files", f"{shard_dir}/").stdout.splitlines() if ln.strip()]
    rows = []
    for rel in sorted(tracked):
        if not rel.endswith(".md"):
            continue
        try:
            text = (ctx.root / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            # Tracked but absent from the worktree. Distinguishable from an empty shard on purpose:
            # a missing file is a different fact from a drained one.
            rows.append({"shard": rel, "live": None, "total": None, "note": "tracked but not on disk"})
            continue
        entries = [ln for ln in text.splitlines() if ln.startswith("- ")]
        live = [ln for ln in entries
                if not any(f"· {t} ·" in ln or f"· {t}·" in ln for t in _TERMINAL_STATUSES)]
        rows.append({"shard": rel, "live": len(live), "total": len(entries)})
    judgeable = [r for r in rows if r["live"] is not None]
    return {
        "signal": "live_backlog_rows_per_shard",
        # The value is the LARGEST shard's live count, and `detail` carries every shard so a total can
        # never hide one growing inside another. A single aggregate is the mistake ARMS_FLOORS was
        # split per-gate to avoid.
        "value": max((r["live"] for r in judgeable), default=0),
        "of": len(rows),
        # NO PIN BY DESIGN: None, so the status column prints `report only, no pin` unless the
        # project's PINS declares one. A fallback of 0 printed `over pin 0` for every non-empty
        # shard, which trains a reader to ignore the line, the failure this signal is meant to cure.
        "tolerance": None,
        "gateable": False,
        # A tree with no backlog shards at all cannot move this signal, so it reports DEAD rather than
        # a reassuring 0 — the liveness assertion every signal here carries.
        "live": bool(judgeable),
        "detail": rows,
    }


# --------------------------------------------------------------------------------------------
# TOOL-dDerivedDocket-17 — `--close --override asks-disposed`, counted
#
# Owner ruling D12-b made the `asks-disposed` Definition-of-Done item OVERRIDABLE with a recorded
# reason, on the condition that the overrides are COUNTED. Without a count the ruling is an unbounded
# escape: each override is a legitimate, reasoned row in one record, and nothing anywhere reads the
# population. This is that reader, and it is REPORT-ONLY for `live_backlog_rows_per_shard`'s reason —
# `drift-audit records` is an unguarded merge-bar leg, so gating a count that legitimately rises
# turns a recorded owner decision into a scheduled refusal.
#
# NAMED `build_`, not `signal_`, for the reason its neighbour states: `signal` is a noun and not a
# declared verb, and a new definition can be named right for free.
_OVERRIDE_ASKS_ROW = re.compile(
    r"^[0-9][0-9:\-T]*Z override · item asks-disposed · reason ")


def build_asks_disposed_overrides(ctx) -> dict:
    """Recorded `--close --override asks-disposed` rows, per tracked run-state file."""
    tracked = [ln for ln in ctx.git.run(
        "ls-files", f"{ctx.memory_root}/builds/*/RUN.md").stdout.splitlines() if ln.strip()]
    rows = []
    for rel in sorted(tracked):
        try:
            text = (ctx.root / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            # Tracked and absent from the worktree is a DIFFERENT fact from a record holding no
            # override, so it is carried as its own row rather than counted as a clean zero.
            rows.append({"record": rel, "overrides": None, "note": "tracked but not on disk"})
            continue
        rows.append({"record": rel,
                     "overrides": sum(1 for ln in text.splitlines()
                                      if _OVERRIDE_ASKS_ROW.match(ln))})
    judgeable = [r for r in rows if r["overrides"] is not None]
    return {
        "signal": "asks_disposed_overrides",
        # THE ITEM'S OWN ROWS AND NOBODY ELSE'S. A count over every `override` row would rise on a
        # `gates-green` override and read as this item being bought, which is the one reading that
        # would make the number worse than none.
        "value": sum(r["overrides"] for r in judgeable),
        "of": len(rows),
        "tolerance": ctx.pins.get("asks_disposed_overrides", 0),
        "gateable": False,
        # A tree with no run-state file at all cannot move this signal, so it says DEAD PROBE rather
        # than printing the 0 that reads as "nobody has ever overridden it".
        "live": bool(judgeable),
        "detail": rows,
    }


# --------------------------------------------------------------------------------------------
# Signal 10 - a build README asserting a mechanism its own spec set has since revised
# (TOOL-dScriptedRepeat-14)
#
# A build README and that build's spec set are two records of one build and nothing compared them.
# Round 3 of `dScriptedRepeat` found the README saying `--counts` takes the recorded FACTS while spec
# 6 rev-8, written in the same fold, said it takes a pinned BASE sha and re-parses the blob - two
# answers to one question about the guard on the one Definition-of-Done item that takes no override.
# The README is the file a session opens first, so it is the copy that misleads. The instance was
# superseded in place; the CLASS had no reader until this.
#
# WHAT IT MATCHES, and it is deliberately narrow. A backticked MECHANISM token in the README's
# AUTHORED prose, where some entry in that build's spec revision logs is dated LATER than the git
# author-date of the README line carrying it, and names the same token. That is "the spec revised this
# mechanism after the README last said anything about it" - a review-me pointer, not a proven
# contradiction. Proving the contradiction needs a reader who can tell two English sentences apart,
# which is why this signal REPORTS and never gates.
#
# THE THREE NARROWINGS, each of which cut a false-positive population measured on this tree:
#   - AUTHORED REGION ONLY. Everything from the first `<!-- gen:` marker down is rendered by
#     gen_build_index.py from the specs themselves and cannot drift away from them.
#   - MECHANISM SHAPES ONLY: `--flag`, `name()`, `FOO_BAR`, `foo_bar`. The all-caps shape REQUIRES an
#     underscore, so status vocabulary (ABORTED, LANDED, INPROGRESS) is not a mechanism; the lowercase
#     shape forbids a dot, so `drift_report.py` is a FILE and not one either. Measured: the wide form
#     fired on 42% of the corpus, this one on 13%.
#   - THE README LINE'S OWN CLOCK, from `git blame`, not the file's. A typo fix elsewhere in a 280-line
#     README must not re-date every claim in it. The spec side uses its revision log read as DATA for
#     the mirror-image reason: a git mtime on a spec moves when someone fixes a comma.
#
# LIVENESS IS OVER THE TOKEN POPULATION, not over "did I find a build". The tree always has builds, so
# a liveness assertion watching them can never go false and is one in name only. What CAN empty is the
# set of README lines carrying a mechanism token, and the set of parseable revision entries to compare
# them against; both are required.
_MECH_RE = re.compile(r"^(--[a-z][a-z0-9-]{2,}"
                      r"|[a-z_][a-z0-9_]*\(\)"
                      r"|[A-Z][A-Z0-9]*_[A-Z0-9_]+"
                      r"|[a-z][a-z0-9]*_[a-z0-9_]+)$")
_TICK_RE = re.compile(r"`([^`]{2,60})`")
_REVLOG_RE = re.compile(r"^- rev-(\d+)\s*[\u00b7|-]\s*(\d{4}-\d{2}-\d{2})")
_GEN_MARK = "<!-- gen:"


def _build_blame_dates(ctx, rel: str, upto: int) -> dict:
    """line number -> author date, in the AUTHOR'S OWN timezone. Porcelain emits the header block ONCE
    per commit; every later line attributed to that commit carries the sha alone, so the date map is
    keyed on the sha.

    THE TIMEZONE IS NOT A DETAIL. The other side of this signal's comparison is a HAND-TYPED local date
    in a spec revision log, so reading `author-time` as UTC compares two different clocks. Measured on
    this repo: 11 of 31 rows were pure +0300 artifacts — every README line written between 00:00 and
    03:00 local was backdated a day, so a spec revision made the SAME day compared as later. This is
    what `git blame --date=short` prints and what a human types, which is the whole point."""
    out = ctx.git.run("blame", "--porcelain", "-L", f"1,{max(upto, 1)}", "--", rel).stdout
    dates: dict[int, str] = {}
    by_sha: dict[str, str] = {}
    sha = None
    lineno = None
    epoch = None
    for ln in out.splitlines():
        m = re.match(r"^([0-9a-f]{40}) \d+ (\d+)", ln)
        if m:
            sha, lineno = m.group(1), int(m.group(2))
            epoch = None
            if sha in by_sha:
                dates[lineno] = by_sha[sha]
            continue
        if ln.startswith("author-time ") and sha is not None:
            epoch = int(ln.split()[1])
            continue
        # `author-tz` FOLLOWS `author-time`, so the date is formatted here and not there.
        if ln.startswith("author-tz ") and epoch is not None and lineno is not None:
            tz = ln.split()[1]
            off = 0
            if len(tz) == 5 and tz[0] in "+-":
                off = (int(tz[1:3]) * 3600 + int(tz[3:5]) * 60) * (-1 if tz[0] == "-" else 1)
            d = datetime.datetime.fromtimestamp(
                epoch + off, datetime.timezone.utc).strftime("%Y-%m-%d")
            by_sha[sha] = d
            dates[lineno] = d
            epoch = None
    return dates


def _read(ctx, rel: str) -> str:
    try:
        return (ctx.root / rel).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


# NAMED `build_`, for the reason spelled above build_live_backlog_rows: `signal` is a noun and not in
# `.lexicon.conf`'s VERBS table, and a new definition can be named right for free.
def build_readme_mechanism_drift(ctx) -> dict:
    """README lines naming a mechanism the build's own spec set revised after that line was written."""
    readmes = [ln for ln in ctx.git.run(
        "ls-files", f"{ctx.memory_root}/builds/*/README.md").stdout.splitlines() if ln.strip()]
    specs_by_build: dict[str, list[str]] = {}
    for sp in ctx.git.run("ls-files", f"{ctx.memory_root}/builds/*/spec/*.md").stdout.splitlines():
        sp = sp.strip()
        if not sp:
            continue
        _pfx = f"{ctx.memory_root}/builds/"
        if sp.startswith(_pfx):
            specs_by_build.setdefault(sp[len(_pfx):].split("/")[0], []).append(sp)

    rows = []
    tok_pop = 0
    rev_pop = 0
    blamed = 0
    blame_blind = 0
    # NOT `rel.split("/")[2]`. `MEMORY_ROOT` is not constrained to one path segment and this repo's
    # own kickoff manifest records `docs/mem` as a real adopter value; at two segments the index lands
    # on the literal `builds` for every path, every README grades against every build's revision log,
    # and the rows name a build called `builds`. Every sibling signal here addresses the tree by glob
    # and is depth-agnostic.
    prefix = f"{ctx.memory_root}/builds/"

    def _extract_slug(path: str) -> str:
        return path[len(prefix):].split("/")[0] if path.startswith(prefix) else ""

    graded = 0
    for rel in sorted(readmes):
        build = _extract_slug(rel)
        if not build:
            continue
        # LIVE BUILDS ONLY (TOOL-aMendedFleet-51 S4). A build whose every spec is CLOSED or WONTDO is
        # a frozen record: 27 of the 31 rows this signal first reported sat in such builds and none
        # was worth acting on. Liveness is read from the `**Status:**` line of the spec text read
        # below for the revision log anyway, so no file is read twice.
        texts = [(sp, _read(ctx, sp)) for sp in specs_by_build.get(build, [])]
        if not any((m := _STATUS.search(t)) and m.group(1).upper() not in _TERMINAL_STATUSES
                   for _, t in texts):
            continue
        graded += 1
        lines = _read(ctx, rel).split("\n")
        cut = next((i for i, ln in enumerate(lines) if ln.startswith(_GEN_MARK)), len(lines))
        # THE REVISION ENTRIES, read as data. A continuation line is folded into the entry above it,
        # because a revision's reason routinely wraps and the token often sits in the wrap.
        revs = []
        for sp, text in texts:
            inlog = False
            for ln in text.split("\n"):
                if ln.startswith("## "):
                    inlog = "Revision log" in ln
                    continue
                if not inlog:
                    continue
                m = _REVLOG_RE.match(ln)
                if m:
                    revs.append([sp, m.group(2), ln])
                elif revs and revs[-1][0] == sp and ln.startswith("  "):
                    revs[-1][2] += " " + ln.strip()
        rev_pop += len(revs)
        # THE CANDIDATES FIRST, THE BLAME ONLY IF THERE ARE ANY. `git blame` is a process per README
        # and this audit is meant to run in seconds; a README whose tokens no revision entry mentions
        # cannot produce a row whatever its dates are.
        cand = []
        # ONE CANDIDATE PER (LINE, TOKEN), never one per occurrence. A README sentence naming a
        # mechanism twice is one sentence to re-read, and `value` is what the shipped pin ratchets
        # against - counting it twice inflates the drain list for no new work.
        seen = set()
        for i, ln in enumerate(lines[:cut], start=1):
            if ln.lstrip().startswith("#"):
                continue
            for tok in _TICK_RE.findall(ln):
                if not _MECH_RE.match(tok):
                    continue
                tok_pop += 1
                if (i, tok) in seen:
                    continue
                seen.add((i, tok))
                # THE BACKTICKED FORM, never a bare substring. `--check` is a prefix of
                # `--check-format` and every id ending in a 1-up sequence is a prefix of nine others -
                # this repo's own `id-matched-as-a-substring` class, and a revision log spells its
                # mechanisms in backticks anyway. Measured: identical rows on this corpus either way,
                # which is luck rather than equivalence.
                named = [r for r in revs if ("`" + tok + "`") in r[2]]
                if named:
                    cand.append((i, tok, named))
        if not cand:
            continue
        dates = _build_blame_dates(ctx, rel, cut)
        # A BLAME THAT ANSWERED NOTHING IS NOT A BUILD WITH NOTHING TO SAY. `Git.run` never raises and
        # that helper reads only stdout, so an unborn HEAD or any other blame failure yields {} and the
        # build contributes zero rows in silence. Counted here so `live` can watch the stage that
        # actually does the work, rather than only the two populations gathered before it.
        blamed += 1
        if not dates:
            blame_blind += 1
        for i, tok, named in cand:
            d = dates.get(i)
            if d is None:
                continue
            later = sorted((r for r in named if r[1] > d), key=lambda r: r[1])
            if not later:
                continue
            sp, rd, _ = later[-1]
            rows.append({"build": build, "readme": f"{rel}:{i}", "mechanism": tok,
                         "line_dated": d, "spec": sp, "revised": rd})
    return {
        "signal": "readme_mechanism_drift",
        "value": len(rows),
        "of": graded,
        "tolerance": ctx.pins.get("readme_mechanism_drift", 0),
        # REPORT ONLY. `drift-audit records` is an unguarded merge-bar leg, and this predicate reports
        # a POINTER rather than a proven contradiction - gating it would red a merge on a README
        # sentence that may well still be true.
        "gateable": False,
        # LIVENESS OVER THE STAGE THAT DOES THE WORK, not only over the two populations gathered
        # before it. `tok_pop` and `rev_pop` are both accumulated ahead of the blame call, so a signal
        # whose every blame failed used to report a clean `ok`. If any README reached the blame stage,
        # at least one of them has to have come back with dates.
        "live": bool(tok_pop and rev_pop and (blamed == 0 or blamed > blame_blind)),
        "detail": rows,
    }


# `backlog_rows_outliving_closed_specs` RETIRED at the backlog switch-over (TOOL-dDerivedDocket-34
# S10). It compared an AUTHORED shard row's token with its same-id spec's status, and under
# `BACKLOG_MODE="builds"` no status is authored: a signed `unit` ask derives its spec's status, and
# every other ask is a separate subject by ruling D2. The stance it counted — DEPL-dGaugedVintage-13,
# "COUNTED, NEVER REFUSED" — is superseded by the `unit` and `advances` model (design section 4.4),
# recorded in `memory/DECISIONS.md` under this unit's id. Its pin left `drift_signals.py` with it.


# --------------------------------------------------------------------------------------------
# Three builds-mode backlog signals (TOOL-dDerivedDocket-34 S10). REPORT-ONLY, each `gateable:
# False`: each counts a population a human reads and none is a merge refusal. Each reads the
# generator's ask projection and implements no second fold, and each is NOT ASKED under `shards`
# and while no per-build `BACKLOG.md` is tracked, which is the state right after an adopter sets
# the mode — three DEAD PROBE lines there would be alarms nobody staged.
#
# LIVENESS IS OVER THE FIELD, not the file: an ask row lacking the field a signal reads is not
# examined, so a projection that stopped emitting it reports DEAD PROBE rather than a clean zero.
# --------------------------------------------------------------------------------------------
def read_asks_or_skip(ctx, name: str, all_rows: bool):
    """`(rows, None)` for a builds-mode signal, or `(None, record)` naming why it cannot read."""
    if read_backlog_mode(ctx) != "builds":
        return None, _build_not_asked(name, "BACKLOG_MODE is shards: asks live in the authored "
                                            "shards and there is no ask projection to read")
    if not read_tracked_asks(ctx):
        return None, _build_not_asked(name, "BACKLOG_MODE is builds but no per-build BACKLOG.md "
                                            "is tracked yet; there is no ask to judge")
    rows, _examined, note = read_asks_projection(ctx, all_rows)
    if rows is None:
        return None, {"signal": name, "value": 0, "of": 0, "tolerance": ctx.pins.get(name, 0),
                      "gateable": False, "live": False, "detail": [{"note": note}]}
    return rows, None


def build_backlog_asks_contested(ctx) -> dict:
    """Asks with BOTH closing and declining evidence, and asks whose terminal evidence sits beside a
    LIVE spec — the two shapes in which the fold decided something a reader would dispute."""
    name = "backlog_asks_contested"
    rows, skip = read_asks_or_skip(ctx, name, all_rows=True)
    if skip:
        return skip
    fields = ("closing", "declining", "live_specs")
    judged = [r for r in rows if all(isinstance(r.get(f), list) for f in fields)]
    hits = [{"id": r.get("id"), "status": r.get("status"),
             "why": ("closing and declining" if r["closing"] and r["declining"]
                     else "terminal evidence beside a live spec")}
            for r in judged
            if (r["closing"] and r["declining"])
            or ((r["closing"] or r["declining"]) and r["live_specs"])]
    return {"signal": name, "value": len(hits), "of": len(judged),
            "tolerance": ctx.pins.get(name, 0), "gateable": False,
            "live": len(judged) > 0, "detail": hits[:20]}


def build_backlog_evidence_sha(ctx) -> dict:
    """`by <sha>` closing evidence the object database does not resolve to a commit."""
    name = "backlog_evidence_sha"
    rows, skip = read_asks_or_skip(ctx, name, all_rows=True)
    if skip:
        return skip
    shas: dict = {}
    for r in rows:
        if not isinstance(r.get("closing"), list):
            continue
        for value in r["closing"]:
            if re.fullmatch(r"[0-9a-f]{7,40}", str(value)):
                shas.setdefault(str(value), []).append(r.get("id"))
    missing = []
    ordered = sorted(shas)
    if ordered:
        # ONE process for every sha. `--batch-check` answers `<name> missing` for a name it cannot
        # resolve and a three-field object line for one it can, in input order.
        proc = subprocess.run(["git", "cat-file", "--batch-check"], cwd=str(ctx.root),
                              input="".join(sha + "^{commit}\n" for sha in ordered),
                              capture_output=True, text=True, encoding="utf-8", errors="replace")
        lines = (proc.stdout or "").splitlines()
        if len(lines) != len(ordered):
            return {"signal": name, "value": 0, "of": 0, "tolerance": ctx.pins.get(name, 0),
                    "gateable": False, "live": False,
                    "detail": [{"note": "git cat-file answered a different number of lines than "
                                        "it was asked, so no sha can be judged"}]}
        for sha, line in zip(ordered, lines):
            if len(line.split()) != 3:
                missing.append({"sha": sha, "asks": sorted(shas[sha])[:5]})
    return {"signal": name, "value": len(missing), "of": len(ordered),
            "tolerance": ctx.pins.get(name, 0), "gateable": False,
            "live": len(ordered) > 0, "detail": missing[:20]}


def build_backlog_asks_unlabelled(ctx) -> dict:
    """LIVE asks carrying no severity row. Read from the generator's live projection, so the kit
    applies no status filter of its own."""
    name = "backlog_asks_unlabelled"
    rows, skip = read_asks_or_skip(ctx, name, all_rows=False)
    if skip:
        return skip
    judged = [r for r in rows if isinstance(r.get("sev"), str)]
    hits = [r.get("id") for r in judged if r["sev"] == "unlabelled"]
    return {"signal": name, "value": len(hits), "of": len(judged),
            "tolerance": ctx.pins.get(name, 0), "gateable": False,
            "live": len(judged) > 0, "detail": [{"id": i} for i in hits[:20]]}


# Signal 2's sibling for asks (TOOL-aMendedFleet-55): a LIVE ask whose id tracked product source
# cites may describe work that already shipped. REPORT-ONLY and pinless, because source legitimately
# cites an ask it has not fixed yet — a forward reference reads exactly like a fix here — and no
# sampled precision exists to gate on. The population is the generator's live projection with no
# status rule of this kit's own; the citation test is signal 2's whole-word `-w -F` over
# EVIDENCE_GLOBS, run ONCE with the ids on stdin so the argument list does not grow with the backlog.
def build_open_asks_cited_by_source(ctx) -> dict:
    """Live asks whose id is cited by tracked product source, each with up to three citing paths."""
    name = "open_asks_cited_by_product_source"
    rows, skip = read_asks_or_skip(ctx, name, all_rows=False)
    if skip:
        return skip
    judged = [r for r in rows if isinstance(r.get("id"), str) and r["id"].strip()]
    ids = sorted({r["id"].strip() for r in judged})
    cited: dict = {}
    if ids:
        # `-z` so a path is split from its match by NUL, not by a ':' a path may hold. Exit 1 is
        # "no match", a clean zero; anything above it is git failing, which judges nothing.
        hit = subprocess.run(["git", "-C", str(ctx.root), "grep", "-o", "-z", "-w", "-F", "-f", "-",
                              "--", *ctx.evidence_globs],
                             input="".join(i + "\n" for i in ids), capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        if hit.returncode > 1:
            said = ((hit.stderr or "").strip().splitlines() or [f"exit {hit.returncode}"])[-1]
            return {"signal": name, "value": 0, "of": 0, "tolerance": None, "gateable": False,
                    "live": False, "detail": [{"note": f"git grep failed: {said[:240]}"}]}
        for line in hit.stdout.splitlines():
            path, _, match = line.partition("\0")
            cited.setdefault(match.strip(), set()).add(path)
    seen = ctx.git.run("ls-files", "--", *ctx.evidence_globs)
    evidence_files = len(seen.stdout.split()) if seen.returncode == 0 else 0
    detail = sorted(({"id": r["id"].strip(), "status": r.get("status"),
                      "cited_in": sorted(cited[r["id"].strip()])[:3]}
                     for r in judged if r["id"].strip() in cited), key=lambda d: d["id"])
    return {"signal": name, "value": len(detail), "of": len(judged),
            "evidence_files": evidence_files, "tolerance": None, "gateable": False,
            # Signal 2's two liveness halves: a population, AND evidence globs that resolve.
            "live": len(judged) > 0 and evidence_files > 0, "detail": detail}


# --------------------------------------------------------------------------------------------
# Signal — armed `*_CUTOFF` keys across the tracked root confs (TOOL-aMendedFleet-21)
#
# Every armed dated cutoff makes the required shape of a record depend on a filename date, and
# nothing priced adding one. This counts them: the population is every `_CUTOFF` assignment in a
# TRACKED root-level `.<name>.conf`, the value is the NON-BLANK ones. A blank key shapes nothing, so
# it is in `of` and not in `value`. Spellings in tool source are NOT counted: a comment edit must not
# move a budget.
#
# GATEABLE ONLY WHERE PINS DECLARES IT. The shipped example confs arm a key, so a default tolerance
# of 0 would red every adopter's first `--check`; a guessed shipped pin is what PINS forbids.
#
# What it cannot see: a key BLANKED to meet the pin disarms its rule exactly as making the rule
# unconditional does, and both read as one fewer. The README says so; the diff shows which.
# --------------------------------------------------------------------------------------------


def build_cutoff_keys_armed(ctx) -> dict:
    name = "cutoff_keys_armed"
    tracked = ctx.git.run("ls-files").stdout.splitlines()
    confs = sorted(f for f in tracked if re.fullmatch(r"\.[^/]+\.conf", f))
    armed, skipped, of = [], [], 0
    for f in confs:
        try:
            conf = parse_conf_text((ctx.root / f).read_text(encoding="utf-8", errors="replace"))
        except OSError as exc:
            skipped.append({"file": f, "note": f"unreadable, skipped: {exc.__class__.__name__}"})
            continue
        for k, v in conf.items():
            if k.endswith("_CUTOFF"):
                of += 1
                if v.strip():
                    armed.append({"file": f, "key": k, "value": v})
    gateable = name in ctx.pins
    note = [] if gateable else [{"note": "no budget declared: add a PINS entry"}]
    return {"signal": name, "value": len(armed), "of": of,
            "tolerance": ctx.pins.get(name, 0), "gateable": gateable,
            "live": of > 0, "detail": note + armed + skipped}



# --------------------------------------------------------------------------------------------
# Signal — a unit id cited by tracked SOURCE that no record defines
#
# THE HALF NOTHING HAD. The memory-tree orphan check counts ids cited-but-not-defined WITHIN the
# memory tree; its population is the memory tree by construction, so its honest zero says nothing
# about code. Product source cites unit ids densely and one of those pointers had resolved to no
# record for its entire life without anything noticing.
#
# THE DISCRIMINATOR IS SLUG-RESOLVABILITY, NOT A PATH PREDICATE, and that is measured rather than
# preferred. This repo puts self-test arms inside product modules and fixture ids inside test
# helpers, so a path split is wrong in whichever direction it is set. An id whose SLUG anchors at
# least one record is a real citation of a real build; an id whose slug anchors none is a fixture.
# The fixture ids in this tree are `tOne`, `tRun`, `tRos`, `zFix` and friends — slugs no record
# anchors — so they drop out with no waiver list at all, which is what makes this population small
# and every member actionable.
#
# REPORT-ONLY, and shrink-only through the ratchet row its pin carries. `gateable: False` means it
# can never enter the over-tolerance set, so the ONLY thing holding the pin is that raising it lands
# in RATCHETS and needs a reason written in place.
# --------------------------------------------------------------------------------------------


def build_source_cited_ids_with_no_record(ctx) -> dict:
    name = "source_cited_ids_resolving_to_no_record"
    grammar_re, anchors = ctx.id_re, ctx.anchors
    mem = ctx.memory_root + "/"

    tracked = ctx.git.run("ls-files")
    if tracked.returncode != 0:
        return _build_not_asked(name, "git could not list tracked files")
    paths = [p for p in tracked.stdout.splitlines() if p.strip()]

    # DEFINITIONS: an id on an anchor line anywhere under the memory root, PLUS a spec's own H1.
    # Anchors, not citations - the whole discriminator rests on the difference. The H1 half is
    # not optional and is easy to miss: the recall grammar's heading anchor deliberately starts
    # at two hashes, so a spec titling itself with its own id is NOT anchored by it. Without the
    # H1 pattern the memory-tree corpus checker also carries, every spec id in the tree reads as
    # undefined and this signal reports a hundred-odd phantom findings. Measured that way first.
    defined, slugs = set(), set()
    for rel in paths:
        if not rel.startswith(mem):
            continue
        try:
            text = (ctx.root / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for anchor in anchors + (ctx.own_id_re,):
            for m in anchor.finditer(text):
                uid = m.group(1)
                defined.add(uid)
                s = _parse_slug(uid)
                if s:
                    slugs.add(s)

    # CITATIONS: any id anywhere in tracked source OUTSIDE the memory root. Deliberately the whole
    # tracked non-memory population rather than the product globs: the question here is citation
    # integrity, and a dangling id in a test file is as wrong as one in a module.
    cited: dict[str, set] = {}
    scanned = 0
    for rel in paths:
        if rel.startswith(mem):
            continue
        try:
            text = (ctx.root / rel).read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeDecodeError):
            continue
        scanned += 1
        for m in grammar_re.finditer(text):
            cited.setdefault(m.group(0), set()).add(rel)

    findings = []
    for uid in sorted(cited):
        if uid in defined:
            continue
        s = _parse_slug(uid)
        if not s or s not in slugs:
            continue  # a slug no record anchors: a fixture, not a finding
        findings.append({"id": uid, "cited_in": sorted(cited[uid])[:3]})

    # LIVENESS, and the second half is NOT the one it looks like it should be. The obvious pair is
    # the slug set and the scanned-file count, and the file count is VACUOUS: this report is
    # itself a tracked non-memory file, so a tree with the kit installed always has source to
    # scan and that half can never read zero. Found by trying to observe it RED and failing,
    # which is the only way that class ever surfaces.
    #
    # What CAN collapse is the CITED set. A grammar bound to the wrong families matches nothing,
    # every file is still scanned, and the signal reports a confident zero over a corpus full of
    # ids it cannot see. So `live` keys on the slug set and the cited set; the file count stays
    # REPORTED, because it is the denominator a reader needs, but it decides nothing.
    return {
        "signal": name,
        "value": len(findings),
        "of": len(cited),
        "known_slugs": len(slugs),
        "scanned_source_files": scanned,
        "tolerance": 0,
        "gateable": False,
        "live": bool(slugs) and bool(cited),
        "unjudgeable": 0,
        "detail": findings[:20],
    }


# --------------------------------------------------------------------------------------------
# Signal - refs that still owe a backlog relocation (TOOL-dDerivedDocket-13)
#
# THE FLEET-WIDE HALF. The hooks beside `.githooks/` instruct a straggler at the moment its own node
# can see it, and `check-wiring.sh` names the LOCAL ones from a session tree. Neither reaches a
# branch pushed from another node, or a branch whose worktree runs its own pre-flip hook files. This
# walks the remote-tracking refs as well as the local ones, so a straggler is reported from ANY
# node's drift run until its changes are accounted on the default branch.
#
# REPORT-ONLY. `gateable: False`, so `--check` never reds on it: a straggler is a normal state of a
# transition and its remedy is a relocation somebody has to perform, not a merge to block. Before
# the flip it reports the whole migration inventory; after it, the stragglers left, until zero.
#
# IT DECIDES NOTHING. The judgement of what is accounted belongs to the relocation engine and the
# transition audit; this signal runs the engine's own `--stragglers` inventory and counts its rows.
# Two readers of one question would be two answers to it.
# --------------------------------------------------------------------------------------------


def _resolve_relocation_engine():
    """The memory-tree kit's relocation engine, through `resolve_kit_dir` like every sibling lookup.

    The resolution `_resolve_ident` makes for the recall kit, for the same reason: the kit that owns
    the answer is a sibling of this one at whatever prefix a tree installs them at, and the sibling
    is optional. Returns None rather than raising — `main()` evaluates every signal in one unguarded
    comprehension, so a raise here takes the whole report down. The receipt rung finds a kit an
    adopter RENAMED, which the old `parent.parent / <home>` probe could not (TOOL-aRepatriatedFork-2).
    """
    try:
        kit = resolve_kit_dir("memory-tree", "migrate_backlog.py", pathlib.Path(__file__).resolve().parent)
    except LookupError:
        return None
    return kit / "migrate_backlog.py"


def build_backlog_stragglers(ctx) -> dict:
    """Refs whose backlog row changes are unaccounted against the default branch."""
    name = "backlog_stragglers"
    engine = _resolve_relocation_engine()
    if engine is None:
        return _build_not_asked(name, "the memory-tree kit is not installed beside this one")
    try:
        source = engine.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return _build_not_asked(name, f"the relocation engine could not be read: {exc}")
    # THE MODE, not the module. A kit copy that predates the inventory answers a different question
    # or none at all, and running it would report a zero that means "this argument was rejected".
    if "--stragglers" not in source:
        return _build_not_asked(
            name, "the installed memory-tree kit predates the straggler inventory (--stragglers)")
    try:
        out = subprocess.run(
            [sys.executable, str(engine), "--stragglers", "--tsv"],
            cwd=str(ctx.root), capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=600)
    except (OSError, subprocess.SubprocessError) as exc:
        return _build_not_asked(name, f"the straggler inventory could not be run: {exc}")

    rows, examined = [], 0
    for line in (out.stdout or "").splitlines():
        bits = line.rstrip("\r").split("\t")
        if bits[0] == "straggler" and len(bits) >= 5:
            rows.append({"ref": bits[1], "tip": bits[2][:12],
                         "unaccounted": bits[3], "first_change": bits[4][:12]})
        elif bits[0] == "examined" and len(bits) >= 2 and bits[1].strip().isdigit():
            examined = int(bits[1].strip())
    detail = rows[:20]
    if out.returncode != 0:
        # The inventory refuses rather than guessing on a shallow clone or an empty ref set, and it
        # says which. Carried through as the DETAIL of a probe that reports itself not live, never
        # flattened into a reassuring zero.
        said = (out.stdout or "").strip() or (out.stderr or "").strip()
        detail = [{"note": said.splitlines()[0][:300] if said else
                   f"the straggler inventory exited {out.returncode} and printed nothing"}]
        examined = 0
    return {
        "signal": name,
        "value": len(rows),
        # LIVENESS FROM WHAT WAS EXAMINED. A repository whose ref walk examined nothing reports DEAD
        # rather than a clean 0 — a clone with no refs and a fleet with no stragglers are different
        # facts and only one of them is good news.
        "of": examined,
        "tolerance": 0,
        "gateable": False,
        "live": examined > 0,
        "unjudgeable": 0,
        "detail": detail,
    }


# --------------------------------------------------------------------------------------------
# Signal — run records left non-terminal after their build merged (TOOL-dLoggedFlight-13)
#
# THE HALF NOBODY READ. An unattended run's record keeps saying LANDING or BUILDING long after its
# work reached the default branch, so "did it land?" cannot be answered from the record, and every
# later run's concurrency report carries the stale ones as though they were live. When this signal
# was specced, several tracked records did exactly that and had been found by accident.
#
# REPORT-ONLY, because nobody is at fault. A sanctioned worktree landing moves the default branch
# past a run's witness before any verb can stamp the record terminal, so a gate here would red every
# bar on every node the moment such a landing merged. The project layer's pin makes a RISE visible in
# the table instead.
#
# WHAT IT COUNTS, from the record at HEAD and never from the working tree:
#   - its phase is not terminal, and it is not derived LANDED (below);
#   - its witness is an ancestor of the base ref;
#   - its witness is neither equal to nor an ancestor of the record's own `base:`.
# The third is the one that needs saying. The witness is HEAD at the last verb that writes one, and
# `--close` writes none, so a run that went from preflight to close leaves its witness AT its base
# even when its own commits merged. That record is UNJUDGEABLE: counted apart with its reason, never
# scored clean and never counted, because judging it needs the run's own commits, which these git
# calls do not read. The run model reads them.
#
# derived LANDED (owner ruling D12-i2, TOOL-aMendedFleet-47). A `LANDING` record whose landing
# commit is on the base ref IS landed, and the driver and its gate leg already read it so through
# `read_landing_commit` in the unattended kit's library. That rule is RE-SPELLED here, offline,
# because this kit is copy-installed without that one: the landing commit is the newest commit in
# HEAD's history that changed the record's path. Such a record is excluded BEFORE its witness is
# placed, so it is neither counted nor unjudgeable, and the detail's summary line counts it.
#
# FOUR GIT CALLS AT MOST, whatever the record count: one `ls-tree` to enumerate, one `rev-list
# --parents` of the base ref, one `cat-file --batch` HELD OPEN, because the witnesses are only known
# once the records it returns are read, and one `log --name-only` over every `LANDING` record's
# path, made only where such a record exists. `cat-file` flushes after every object, so one question
# and one answer at a time cannot deadlock on a buffer. The witness-to-base order is walked on the
# parent graph the rev-list printed: the SET of reachable commits alone cannot order two of its
# members. A landing commit is on the base ref exactly when it is a key of that same graph.
#
# WHAT IT DOES NOT SEE, said here because a structural count reads as a semantic one. A refused
# landing leaves no tracked row, so no sub-class can name one, and the detail says so on every run.
# A shallow clone truncates the rev-list, which can drop a record from the count and never add one.
# The batched `log` disagrees with the driver's per-record `git log -1` in one shape: a record whose
# newest change is a MERGE that resolved it, because a merge prints no names without `-m`. It then
# names an older commit on one side of that merge, which is still on any base ref holding the merge,
# so the disagreement can only leave a record counted, never derive one the driver would not.
# --------------------------------------------------------------------------------------------

# The driver's own declarations, SPELLED HERE because this kit is copy-installed and must run in a
# tree with no unattended kit. Not a second vocabulary by stealth: the self-test extracts the driver's
# PHASES_TERMINAL, PARK_KINDS, PARK_KINDS_OWED and PARK_ACTS_OWED wherever the driver is present and
# holds each set here to its source in both directions.
_RUN_PHASES_TERMINAL = frozenset({"LANDED", "ABORTED"})
_RUN_PARK_KINDS = frozenset({"decision", "abort", "override", "waiver", "proposal", "rescope",
                             "dispatch", "review", "brief", "hold", "resume", "handoff"})
# `hold` and `resume` joined the driver's PARK_KINDS in TOOL-dDerivedDocket-5 (auto-resume from
# HELD). Neither is owed, so a record whose last row is one reads `other`. `handoff` joined both sets
# in TOOL-dUnstuckLanding-13: its row is the landing recipe the owner is shown, so it is owed.
_RUN_PARK_KINDS_OWED = frozenset({"decision", "abort", "override", "waiver", "handoff"})
# `defer` joined the owed acts in TOOL-dUnstuckLanding-18, so a record whose last row defers a unit
# reads `retired-unit` beside a retirement: both set declared scope aside.
_RUN_PARK_ACTS_OWED = frozenset({"retire", "supersede", "defer"})
# A parked row as the driver's `park` appends it: `<utc> <kind> · item <item>[ · step <n>] · reason
# <why>`, the timestamp in the shape the driver's own counters grep for. The act of a `rescope` row is
# the FIRST word of its item and only the first, so an addition whose second word happens to be
# `retire` stays an addition.
_RUN_ROW = re.compile(r"^[0-9][0-9-]*T[0-9:]*Z ([a-z]+) \u00b7 item (\S*)")
# SHA-SHAPED before anything resolves it, for the reason the driver's own admission check gives: the
# run being graded authors its witness, and a witness reading `main` resolves and is an ancestor of the
# base ref by construction.
_RUN_SHA = re.compile(r"^[0-9a-f]{7,40}$")
_RUN_STALE = "witness not re-written since preflight"
_RUN_REFUSED_NOTE = ("note — a refused landing is not recorded in tracked bytes, so no sub-class here "
                     "can name one")


def _parse_run_record(text: str) -> dict:
    """The facts and the last parked row of one run-state file.

    Read the way the driver's `fact` reads them: the FIRST line starting `<key>:`, one trailing CR
    dropped, leading blanks trimmed. Split on LF alone, because `splitlines` also breaks on a lone CR
    and on form feeds, and either would end a row early inside a reason field. `halt-code` and
    `work-landed-at` joined the three in TOOL-dUnstuckLanding-15, for the ABORTED signals below; an
    absent one reads as the empty string, as the other three do.
    """
    facts: dict = {}
    last = None
    for line in text.split("\n"):
        if line.endswith("\r"):
            line = line[:-1]
        for key in ("phase", "witness", "base", "halt-code", "work-landed-at"):
            if key not in facts and line.startswith(key + ":"):
                facts[key] = line[len(key) + 1:].lstrip(" ")
        row = _RUN_ROW.match(line)
        # A row whose kind the driver does not declare is not a parked row, so it cannot be the last
        # one. That is what makes the PARK_KINDS comparison in the self-test load-bearing.
        if row and row.group(1) in _RUN_PARK_KINDS:
            last = (row.group(1), row.group(2))
    return {"phase": facts.get("phase", ""), "witness": facts.get("witness", ""),
            "base": facts.get("base", ""), "halt-code": facts.get("halt-code", ""),
            "work-landed-at": facts.get("work-landed-at", ""), "last": last}


def _derive_run_subclass(last) -> str:
    """Why a counted record stopped, from its LAST parked row: the table in TOOL-dLoggedFlight-13 S3,
    first match wins. Retirement is matched before the owed kinds because it is the more specific
    cause."""
    if last is None:
        return "no-rows"
    kind, act = last
    if kind == "rescope" and act in _RUN_PARK_ACTS_OWED:
        return "retired-unit"
    if kind in _RUN_PARK_KINDS_OWED:
        return "surfaced-park"
    return "other"


def _check_run_ancestor(parents: dict, older: str, newer: str) -> bool:
    """Is `older` reachable from `newer` through the parent graph `rev-list --parents` printed?"""
    seen, todo = set(), [newer]
    while todo:
        sha = todo.pop()
        if sha == older:
            return True
        if sha in seen:
            continue
        seen.add(sha)
        todo.extend(parents.get(sha, ()))
    return False


def _build_run_dead(name: str, of: int, note: str) -> dict:
    """DEAD with the stage that could not answer named, never a clean zero."""
    return {"signal": name, "value": 0, "of": of, "tolerance": 0, "gateable": False,
            "live": False, "unjudgeable": 0, "detail": [note]}


# NAMED `build_`, for the reason spelled above build_live_backlog_rows.
def build_nonterminal_merged_runs(ctx) -> dict:
    """Run records whose phase is still live although their witness is on the base ref."""
    name = "run_records_nonterminal_but_merged"
    builds = f"{ctx.memory_root}/builds/"

    # CALL 1 — the population, at HEAD. Both globs the driver's own single-live check reads: the live
    # `RUN.md` and every rotated `RUN.<phase>.<blob8>.md`, since an archive hand-edited back to a live
    # phase is the case that check exists for.
    listing = ctx.git.run("ls-tree", "-r", "-z", "HEAD", "--", builds)
    if listing.returncode != 0:
        return _build_run_dead(name, 0, "DEAD PROBE — `git ls-tree HEAD` failed, so no run record was read")
    shape = re.compile("^" + re.escape(builds) + r"[^/]+/RUN(?:\.[^/]+)?\.md$")
    records = []
    for entry in listing.stdout.split("\0"):
        meta, _, path = entry.partition("\t")
        bits = meta.split()
        if len(bits) >= 3 and bits[1] == "blob" and shape.match(path):
            records.append((path, bits[2]))
    if not records:
        # NOT ASKED where nothing here adopts what this reads, and DEAD where something does: a repo
        # carrying the kit's conf and no record is a repo whose population may have gone blind.
        if not (ctx.root / ".unattended.conf").exists():
            return _build_not_asked(name, "no tracked run-state file and no .unattended.conf at the repo "
                                          "root; the unattended kit is not adopted")
        return _build_run_dead(name, 0, "DEAD PROBE — .unattended.conf is present and no run-state file "
                                        "is tracked under the build folders")

    # CALL 2 — one conversation with one `cat-file --batch`: every record's blob first, then each
    # witness and base of a live record as `<sha>^{commit}`, which also expands an abbreviation.
    try:
        proc = subprocess.Popen(["git", "-C", str(ctx.root), "cat-file", "--batch"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL)
    except OSError:
        return _build_run_dead(name, len(records), "DEAD PROBE — `git cat-file --batch` did not start")

    def read_object(spec: str):
        proc.stdin.write(spec.encode("utf-8") + b"\n")
        proc.stdin.flush()
        head = proc.stdout.readline().split()
        if len(head) != 3:
            return None, b""                  # `<spec> missing` or `<spec> ambiguous`
        size = int(head[2])
        body = proc.stdout.read(size)
        proc.stdout.read(1)                   # the LF cat-file writes after every object
        return head[0].decode("ascii", errors="replace"), body

    parsed = []
    resolved: dict = {}
    try:
        for path, blob in records:
            got, body = read_object(blob)
            if got is None:
                raise ValueError(path)
            parsed.append((path, _parse_run_record(body.decode("utf-8", errors="replace"))))
        for _path, rec in parsed:
            if rec["phase"] in _RUN_PHASES_TERMINAL:
                continue
            for key in ("witness", "base"):
                val = rec[key]
                if val and _RUN_SHA.match(val) and val not in resolved:
                    resolved[val] = read_object(val + "^{commit}")[0]
        proc.stdin.close()
        proc.stdout.close()
        proc.wait()
    except (OSError, ValueError):
        proc.kill()
        proc.wait()
        return _build_run_dead(name, len(records), "DEAD PROBE — `git cat-file --batch` stopped "
                                                   "answering before every record was read")

    # CALL 3 — the base ref's history WITH its parent edges, which is what orders a witness against
    # the record's own base without a git call per record.
    walk = ctx.git.run("rev-list", "--parents", ctx.git.base_ref, "--")
    if walk.returncode != 0 or not walk.stdout.strip():
        return _build_run_dead(name, len(records), f"DEAD PROBE — `git rev-list {ctx.git.base_ref}` "
                                                   "returned nothing, so no witness could be placed")
    parents: dict = {}
    for line in walk.stdout.split("\n"):
        shas = line.split()
        if shas:
            parents[shas[0]] = shas[1:]

    # CALL 4 — derived LANDED: each `LANDING` record's landing commit, from ONE `log` over all their
    # paths. The first commit printed above a path is the newest that changed it.
    landing_paths = [path for path, rec in parsed if rec["phase"] == "LANDING"]
    landing: dict = {}
    if landing_paths:
        log = ctx.git.run("log", "--format=%x01%H", "--name-only", "--no-renames", "HEAD", "--",
                          *landing_paths)
        if log.returncode != 0:
            return _build_run_dead(name, len(records), "DEAD PROBE — `git log` of the LANDING records "
                                                       "failed, so no landing commit was read")
        want, sha = set(landing_paths), ""
        for line in log.stdout.split("\n"):
            if line.startswith("\x01"):
                sha = line[1:].strip()
            elif line in want and line not in landing:
                landing[line] = sha

    counted, stale, derived, detail = 0, 0, 0, []
    for path, rec in parsed:
        phase = rec["phase"]
        if phase in _RUN_PHASES_TERMINAL:
            continue
        if landing.get(path) in parents:
            derived += 1                      # derived LANDED: neither counted nor unjudgeable
            continue
        w_in, b_in = rec["witness"], rec["base"]
        why, rel = None, "unknown"
        # THE WITNESS IS READ FIRST: until it is placed, nothing says whether the record merged.
        if not phase:
            why = "no phase: fact"
        elif not w_in:
            why = "no witness: fact"
        elif not _RUN_SHA.match(w_in):
            why = "witness is not a sha"
        elif resolved.get(w_in) is None:
            why = "witness does not resolve in this object store"
        else:
            w = resolved[w_in]
            if w not in parents:
                continue                      # not merged: neither counted nor unjudgeable
            b = resolved.get(b_in) if (b_in and _RUN_SHA.match(b_in)) else None
            if not b_in:
                why = "no base: fact"
            elif b is None:
                why = "base does not resolve in this object store"
            elif b == w:
                rel, why = "equal", _RUN_STALE
            elif b not in parents:
                # Not reachable from the base ref while the witness is, so the witness cannot descend
                # from it — but whether it is BEHIND it needs the base's own history, which is outside
                # the one walk this signal takes.
                why = f"base is not on {ctx.git.base_ref}, so one rev-list cannot relate it to the witness"
            elif _check_run_ancestor(parents, w, b):
                rel, why = "behind", _RUN_STALE
            else:
                rel = "ahead"
        if why:
            stale += 1
            detail.append(f"{path} {phase or '-'} {w_in[:8] or '-'} {rel} unjudgeable — {why}")
            continue
        counted += 1
        detail.append(f"{path} {phase} {w_in[:8]} {rel} {_derive_run_subclass(rec['last'])}")
    # Printed at 0 too, so a drained value is told apart from a probe that stopped reading them.
    detail.append(f"derived — {derived} of {len(landing_paths)} LANDING records read LANDED: "
                  f"their landing commit is on {ctx.git.base_ref}")
    detail.append(_RUN_REFUSED_NOTE)
    return {
        "signal": name,
        "value": counted,
        "of": len(records),
        "tolerance": 0,
        # REPORT ONLY — see the head of this section. `--check` never reads a report-only signal.
        "gateable": False,
        # LIVE over the population the value is drawn from: every tracked record was read above, and
        # an empty population returned NOT ASKED or DEAD before reaching this line.
        "live": bool(parsed),
        "unjudgeable": stale,
        "derived_landed": derived,
        "detail": detail,
    }


# --------------------------------------------------------------------------------------------
# Signals - ABORTED run records whose work landed anyway (TOOL-dUnstuckLanding-15)
#
# The unattended kit's `--settle` writes `work-landed-at` onto a LEGACY ABORTED record - first
# committed before the project's HANDOFF_CUTOFF - whose work the content predicate reads landed.
# `aborted_work_landed` counts the LIVE legacy records still waiting for that write.
# `discarded_work_landed` counts the POST-CUTOFF records, live or archived, whose work landed
# although from that date ABORTED means discard; no verb clears that class, so it is counted whatever
# facts the record carries. A rotated legacy archive is LISTED with its verdict and counted in
# neither, because `--settle` never edits an archive and a count no verb can lower never reaches 0.
#
# THE PREDICATE IS THE KIT LIBRARY'S `check_work_landed`, consumed and never redefined: its three
# clauses, with this report's base ref standing for the tip the remote advertises. It is SPELLED here,
# as a pure function of gathered facts, because this kit is copy-installed and runs where the
# unattended kit does not; the self-test sources that library wherever it is present and holds every
# verdict and every first-commit date here to it, in both directions. The dating rule is ported the
# same way from the library's `read_first_commit_date`.
#
# LIVENESS is drawn from the population the predicate acts on: five record-shaped CONTROL fact sets,
# four that must read not-landed and one that must read landed, are run first on every report. Any
# other reading is a predicate that cannot say no, or cannot say yes, and both signals read DEAD
# naming the control. A signal is live only over a non-empty dated population as well.
#
# REPORT ONLY, both. A post-cutoff landed discard has no clearing verb, so a gate on it would be a
# permanent red, and a legacy record's work can land late through nobody's fault.
#
# WHAT IT DOES NOT SEE. The revert clause reads the base ref's FIRST-PARENT line only, so a revert
# landed on a side branch and merged in is not seen and its work reads landed - the library's
# clause, carried here unchanged. A revert naming a MERGE counts where that merge brought an
# attributable commit in, as the library's does (implementation review round 1, M4). Attribution by
# path reads `--name-only`, which lists no path for a merge commit, so a merge that alone touches the
# build folder is not attributable here where the library's path-limited log may keep it. The base
# ref is the remote-tracking ref, never a fresh `ls-remote`, so a stale clone judges against what it
# last fetched, and the header prints that ref. A record whose base is OFF the base ref's graph is
# placed by one `merge-base --is-ancestor`, as the library places every one (L4).
#
# UPHELD is read at the base ref, where the leg's check 15 grades `work-landed-at` at the tip the fact
# records (M9): both require the fact to name the record's witness and its tip to be on the base ref
# (L6), but a revert landing after a settle shows here as `fact-not-upheld` while check 15 only
# reports it. The self-test holds the two readings equal over records nothing reverted since.
# --------------------------------------------------------------------------------------------

_AWL_NAME = "aborted_work_landed"
_DWL_NAME = "discarded_work_landed"
_WL_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
# One revert per LINE, the last on it, which is what the library's greedy `sed` extracts.
_WL_REVERT = re.compile(r"This reverts commit ([0-9a-f]{7,40})")
_WL_CONTROL_SHA = "c0" * 20
# Record-shaped, never a free-standing sha: each is the fact set a real ABORTED record of that shape
# gathers. POSITIONAL against _WORK_LANDED_CONTROL_WANT, so replacing the facts cannot also replace
# what they must read.
_WORK_LANDED_CONTROLS = (
    ("witness-equals-base", {"witness_is_base_ancestor": True, "attributable": (), "on_base_ref": (),
                             "reverted": (), "why_unjudgeable": ""}),
    ("foreign-witness", {"witness_is_base_ancestor": False, "attributable": (), "on_base_ref": (),
                         "reverted": (), "why_unjudgeable": ""}),
    ("merged-then-reverted", {"witness_is_base_ancestor": False, "attributable": (_WL_CONTROL_SHA,),
                              "on_base_ref": (_WL_CONTROL_SHA,), "reverted": (_WL_CONTROL_SHA,),
                              "why_unjudgeable": ""}),
    ("merged-not-reverted", {"witness_is_base_ancestor": False, "attributable": (_WL_CONTROL_SHA,),
                             "on_base_ref": (_WL_CONTROL_SHA,), "reverted": (),
                             "why_unjudgeable": ""}),
    # Implementation review round 1, M11: the never-merged run, the one shape only clause (ii) decides.
    ("unmerged", {"witness_is_base_ancestor": False, "attributable": (_WL_CONTROL_SHA,),
                  "on_base_ref": (), "reverted": (), "why_unjudgeable": ""}),
)
_WORK_LANDED_CONTROL_WANT = ("not-landed", "not-landed", "not-landed", "landed", "not-landed")


def check_work_landed(facts: dict) -> tuple:
    """`(verdict, clause-or-reason)` from one record's gathered facts, and nothing else - no git call.

    The kit library's `check_work_landed`, clause for clause: `unjudgeable` with the reason wherever
    the library returns undecidable; `not-landed` naming the first clause that failed - (i) the
    witness is the base or behind it, or nothing in `base..witness` is attributable to the run; (ii)
    an attributable commit is not on the base ref; (iii) a first-parent revert names one - and
    `landed` with an empty second field otherwise.
    """
    why = facts.get("why_unjudgeable") or ""
    if why:
        return "unjudgeable", why
    if facts.get("witness_is_base_ancestor"):
        return "not-landed", "i"
    own = set(facts.get("attributable") or ())
    if not own:
        return "not-landed", "i"
    if own - set(facts.get("on_base_ref") or ()):
        return "not-landed", "ii"
    if own & set(facts.get("reverted") or ()):
        return "not-landed", "iii"
    return "landed", ""


def _check_work_landed_controls() -> str:
    """The first control that misreads, as a DEAD note, or "" when every control reads as stated."""
    controls = tuple(_WORK_LANDED_CONTROLS)
    if len(controls) != len(_WORK_LANDED_CONTROL_WANT):
        return (f"DEAD PROBE — {len(controls)} work-landed controls are declared and "
                f"{len(_WORK_LANDED_CONTROL_WANT)} readings are wanted, so no control can be judged")
    for (label, facts), want in zip(controls, _WORK_LANDED_CONTROL_WANT):
        got = check_work_landed(facts)[0]
        if got != want:
            return (f"DEAD PROBE — the control {label} reads {got} and must read {want}, so the content "
                    f"predicate cannot say {'no' if want != 'landed' else 'yes'} and no verdict below "
                    "means anything")
    return ""


def read_first_commit_date(ctx, path: str, siblings=()) -> str:
    """YYYY-MM-DD the record's own run began, or "" where the path has no committed history.

    The kit library's `read_first_commit_date`, ported: the OLDEST add along `--follow`, so a rotation
    does not re-date an archive; for a live `RUN.md`, floored at the newest FIRST TOUCH of an archived
    sibling in its folder, because the rotation recorded that path `M` and its tenancy began there.
    The caller passes the siblings for a live record and none for an archive.
    """
    out = ctx.git.run("log", "--follow", "--diff-filter=A", "--format=%cs", "--", path)
    days = [d.strip() for d in out.stdout.split("\n") if d.strip()] if out.returncode == 0 else []
    date = days[-1] if days else ""
    floor = ""
    for sib in siblings:
        touch = ctx.git.run("log", "--full-history", "--format=%cs", "--", sib)
        seen = [d.strip() for d in touch.stdout.split("\n") if d.strip()] if touch.returncode == 0 else []
        if seen and (not floor or seen[-1] > floor):
            floor = seen[-1]
    if floor and (not date or floor > date):
        date = floor
    return date


def read_aborted_verdicts(ctx) -> dict:
    """Every tracked ABORTED record at HEAD, dated, judged and classified - read ONCE per report.

    Returns `{"not_asked", "dead", "of", "cutoff", "rows"}`: a NOT ASKED reason, or a DEAD note, or
    the rows, one per ABORTED record, each carrying its rendered detail line, its dating class and the
    signal it counts in. Cached on the context, so both builders cost one read. The git calls: one
    `ls-tree`, one held-open `cat-file --batch`, one `rev-list --parents` and one first-parent revert
    `log` of the base ref, shared; per record a `--follow` dating walk and, where clause (i) needs it,
    one `log` of `base..witness`; one more per archived sibling of a live `RUN.md`; and a
    `merge-base --is-ancestor` only for a revert naming an attributable commit off the base ref's graph,
    or for a base off it.
    """
    cached = getattr(ctx, "_aborted_verdicts", None)
    if cached is not None:
        return cached
    got = {"not_asked": "", "dead": "", "of": 0, "cutoff": "", "rows": []}
    try:
        ctx._aborted_verdicts = got
    except AttributeError:
        pass

    note = _check_work_landed_controls()
    if note:
        got["dead"] = note
        return got

    builds = f"{ctx.memory_root}/builds/"
    conf_name = ".unattended.conf"
    listing = ctx.git.run("ls-tree", "-r", "-z", "HEAD", "--", builds, conf_name)
    if listing.returncode != 0:
        got["dead"] = "DEAD PROBE — `git ls-tree HEAD` failed, so no run record was read"
        return got
    shape = re.compile("^" + re.escape(builds) + r"[^/]+/RUN(?:\.[^/]+)?\.md$")
    records, conf_blob = [], None
    for entry in listing.stdout.split("\0"):
        meta, _, path = entry.partition("\t")
        bits = meta.split()
        if len(bits) < 3 or bits[1] != "blob":
            continue
        if path == conf_name:
            conf_blob = bits[2]
        elif shape.match(path):
            records.append((path, bits[2]))
    if not records and conf_blob is None:
        got["not_asked"] = ("no tracked run-state file and no .unattended.conf at HEAD; the unattended "
                            "kit is not adopted")
        return got

    try:
        proc = subprocess.Popen(["git", "-C", str(ctx.root), "cat-file", "--batch"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL)
    except OSError:
        got["dead"] = "DEAD PROBE — `git cat-file --batch` did not start"
        return got

    def read_object(spec: str):
        proc.stdin.write(spec.encode("utf-8") + b"\n")
        proc.stdin.flush()
        head = proc.stdout.readline().split()
        if len(head) != 3:
            return None, b""                  # `<spec> missing` or `<spec> ambiguous`
        body = proc.stdout.read(int(head[2]))
        proc.stdout.read(1)                   # the LF cat-file writes after every object
        return head[0].decode("ascii", errors="replace"), body

    conf, aborted, resolved = {}, [], {}
    try:
        if conf_blob is not None:
            sha, body = read_object(conf_blob)
            if sha is None:
                raise ValueError(conf_name)
            conf = parse_conf_text(body.decode("utf-8", errors="replace"))
        for path, blob in records:
            sha, body = read_object(blob)
            if sha is None:
                raise ValueError(path)
            rec = _parse_run_record(body.decode("utf-8", errors="replace"))
            if rec["phase"] == "ABORTED":
                aborted.append((path, rec))
        for _path, rec in aborted:
            wla_bits = rec["work-landed-at"].split()
            rec["wla-tip"] = wla_bits[1] if len(wla_bits) > 1 else ""
            for key in ("witness", "base", "wla-tip"):
                val = rec[key]
                # One object name per batch LINE: a value carrying whitespace is not one, and is
                # left unresolved rather than sent.
                if val and not re.search(r"\s", val) and val not in resolved:
                    resolved[val] = read_object(val + "^{commit}")[0]
        proc.stdin.close()
        proc.stdout.close()
        proc.wait()
    except (OSError, ValueError):
        proc.kill()
        proc.wait()
        got["dead"] = "DEAD PROBE — `git cat-file --batch` stopped answering before every record was read"
        return got

    got["of"] = len(aborted)
    got["cutoff"] = (conf.get("HANDOFF_CUTOFF") or "").strip()
    if not aborted:
        got["dead"] = ("DEAD PROBE — no tracked run-state file reads phase ABORTED, so the population "
                       "both signals count from is empty")
        return got

    base_ref = ctx.git.base_ref
    walk = ctx.git.run("rev-list", "--parents", base_ref, "--")
    if walk.returncode != 0 or not walk.stdout.strip():
        got["dead"] = (f"DEAD PROBE — `git rev-list {base_ref}` returned nothing, so no witness could "
                       "be placed")
        return got
    parents: dict = {}
    for line in walk.stdout.split("\n"):
        shas = line.split()
        if shas:
            parents[shas[0]] = shas[1:]
    revlog = ctx.git.run("log", "--first-parent", "--grep=This reverts commit",
                         "--format=%x1e%H%n%B", base_ref, "--")
    if revlog.returncode != 0:
        got["dead"] = (f"DEAD PROBE — the first-parent revert `log` of {base_ref} failed, so clause "
                       "(iii) cannot be read")
        return got
    reverts = []                              # (the reverting commit, the sha its line names)
    for chunk in revlog.stdout.split("\x1e")[1:]:
        sha, _, body = chunk.partition("\n")
        for line in body.split("\n"):
            hits = _WL_REVERT.findall(line)
            if hits:
                reverts.append((sha.strip(), hits[-1]))

    cutoff = got["cutoff"]
    dated = bool(_WL_DATE.match(cutoff))
    for path, rec in aborted:
        folder, _, leaf = path.rpartition("/")
        slug = folder.rpartition("/")[2]
        archived = leaf != "RUN.md"
        sibs = () if archived else tuple(p for p, _ in records
                                         if p.rpartition("/")[0] == folder and p != path)
        date = read_first_commit_date(ctx, path, sibs)
        # The library's test, `[ -z "$first" ] || ! [[ "$first" < "$cut" ]]`: undated is post-cutoff.
        legacy = (not dated) or (bool(date) and date < cutoff)

        facts = {"witness_is_base_ancestor": False, "attributable": (), "on_base_ref": (),
                 "reverted": (), "why_unjudgeable": ""}
        b_in, w_in = rec["base"], rec["witness"]
        b, w = resolved.get(b_in), resolved.get(w_in)
        if not b_in:
            facts["why_unjudgeable"] = "the record carries no base fact, so the run's own range cannot be opened"
        elif b is None:
            facts["why_unjudgeable"] = f"its base {b_in} does not resolve in this clone"
        elif w is None:
            facts["why_unjudgeable"] = f"its witness {w_in or 'none'} does not resolve in this clone"
        elif w == b or (w in parents and b in parents and _check_run_ancestor(parents, w, b)) \
                or (b not in parents and ctx.git.run("merge-base", "--is-ancestor", w, b).returncode == 0):
            # A base off the base ref's graph is placed by ONE call, as the library places it (L4).
            facts["witness_is_base_ancestor"] = True
        else:
            span = ctx.git.run("log", "--format=%x1e%H%x1f%s", "--name-only", f"{b}..{w}", "--")
            if span.returncode != 0:
                facts["why_unjudgeable"] = f"the range {b[:8]}..{w[:8]} cannot be read"
            else:
                word = re.compile(r"(?<![A-Za-z0-9])" + re.escape(slug) + r"(?![A-Za-z0-9])")
                own = []
                for chunk in span.stdout.split("\x1e")[1:]:
                    head, _, rest = chunk.partition("\n")
                    sha, _, subject = head.partition("\x1f")
                    touched = [p for p in rest.split("\n") if p.strip()]
                    if word.search(subject) or any(p.startswith(folder + "/") for p in touched):
                        own.append(sha.strip())
                hit = set()
                for rc, named in reverts:
                    named_own = [c for c in own if c.startswith(named)]
                    if not named_own:
                        # A `git revert -m 1 <merge>` names the MERGE: it reverts the run where that
                        # merge brought an attributable commit in, on its second parent's side and not
                        # already on its first (M4). The library's test, on the base ref's graph.
                        merge = named if named in parents else next(
                            (k for k in parents if k.startswith(named)), "")
                        sides = parents.get(merge, ())
                        if len(sides) >= 2:
                            named_own = [c for c in own if _check_run_ancestor(parents, c, sides[1])
                                         and not _check_run_ancestor(parents, c, sides[0])]
                    if not named_own:
                        continue
                    # The library walks `<tip> ^<witness>`, so a revert the witness already contains
                    # is not one. Placed on the graph where it can be, by one call where it cannot.
                    if w in parents:
                        behind = _check_run_ancestor(parents, rc, w)
                    else:
                        behind = ctx.git.run("merge-base", "--is-ancestor", rc, w).returncode == 0
                    if not behind:
                        hit.update(named_own)
                facts.update(attributable=tuple(own),
                             on_base_ref=tuple(c for c in own if c in parents),
                             reverted=tuple(sorted(hit)))
        verdict, clause = check_work_landed(facts)

        wla = rec["work-landed-at"]
        named = wla.split()[0] if wla.split() else ""
        # The fact names the record's witness and a tip the base ref carries (L6), and the work reads
        # landed - at the base ref here, at the recorded tip in check 15 (see the head of this section).
        upheld = (bool(named) and named in (w_in, w) and resolved.get(rec["wla-tip"]) in parents
                  and verdict == "landed")
        counts = ""
        if verdict == "unjudgeable":
            shown = f"unjudgeable — {clause}"
        elif verdict == "landed" and not legacy:
            shown, counts = "landed", _DWL_NAME
        elif verdict == "landed" and archived:
            shown = "landed (archived)"
        elif verdict == "landed":
            shown, counts = ("settled", "") if upheld else ("landed", _AWL_NAME)
        else:
            # Check 15 of the unattended leg grades this fact; shown here, never counted.
            shown = "fact-not-upheld" if wla else f"not-landed ({clause})"
        got["rows"].append({
            "path": path, "legacy": legacy, "verdict": verdict, "date": date, "counts": counts,
            "unjudgeable": verdict == "unjudgeable", "wla": bool(wla), "upheld": upheld,
            "row": (f"{path} {rec['halt-code'] or '-'} {(w_in or '-')[:8]} {date or '-'} "
                    f"{'legacy' if legacy else 'post-cutoff'} {shown}"),
        })
    return got


def _build_aborted_signal(name: str, rows: list, notes=()) -> dict:
    """One ABORTED signal over its dated population, which the caller has already found non-empty."""
    return {
        "signal": name,
        "value": sum(1 for r in rows if r["counts"] == name),
        "of": len(rows),
        "tolerance": 0,
        # REPORT ONLY - see the head of this section. `--check` never reads a report-only signal.
        "gateable": False,
        # LIVE over the population the value is drawn from: the controls read as stated before any
        # row was gathered, and an empty dated population returned DEAD before this was reached.
        "live": bool(rows),
        "unjudgeable": sum(1 for r in rows if r["unjudgeable"]),
        "detail": [r["row"] for r in rows] + list(notes),
    }


# NAMED `build_`, for the reason spelled above build_live_backlog_rows.
def build_aborted_work_landed(ctx) -> dict:
    """LIVE legacy ABORTED records whose work landed and which carry no upheld `work-landed-at`."""
    got = read_aborted_verdicts(ctx)
    if got["not_asked"]:
        return _build_not_asked(_AWL_NAME, got["not_asked"])
    if got["dead"]:
        return _build_run_dead(_AWL_NAME, got["of"], got["dead"])
    rows = [r for r in got["rows"] if r["legacy"]]
    if not rows:
        return _build_run_dead(_AWL_NAME, got["of"], "DEAD PROBE — every ABORTED record is dated on or "
                                                     "after HANDOFF_CUTOFF, so no LEGACY record exists "
                                                     "to count from")
    notes = ()
    if not _WL_DATE.match(got["cutoff"]):
        notes = (f"note — HANDOFF_CUTOFF is {'blank' if not got['cutoff'] else 'not a date: ' + got['cutoff']}"
                 " in .unattended.conf at HEAD, so every ABORTED record reads LEGACY, and --settle "
                 "refuses every ABORTED record until the key is dated",)
    return _build_aborted_signal(_AWL_NAME, rows, notes)


def build_discarded_work_landed(ctx) -> dict:
    """POST-CUTOFF ABORTED records, live or archived, whose work landed although ABORTED meant discard."""
    got = read_aborted_verdicts(ctx)
    if got["not_asked"]:
        return _build_not_asked(_DWL_NAME, got["not_asked"])
    if got["dead"]:
        return _build_run_dead(_DWL_NAME, got["of"], got["dead"])
    if not _WL_DATE.match(got["cutoff"]):
        return _build_not_asked(_DWL_NAME, f"HANDOFF_CUTOFF is "
                                f"{'blank' if not got['cutoff'] else 'not a date: ' + got['cutoff']} in "
                                ".unattended.conf at HEAD, so no ABORTED record is dated after the day "
                                "ABORTED came to mean discard")
    rows = [r for r in got["rows"] if not r["legacy"]]
    if not rows:
        return _build_run_dead(_DWL_NAME, got["of"], "DEAD PROBE — no ABORTED record is dated on or after "
                                                     f"HANDOFF_CUTOFF {got['cutoff']}, so the population "
                                                     "this counts from is empty")
    return _build_aborted_signal(_DWL_NAME, rows)


# --------------------------------------------------------------------------------------------
# Signal - legs the merge bar retried after a timeout (TOOL-dDerivedDocket-26 S7)
#
# The gate runner retries, once and alone, a leg whose own ceiling fired, and counts a pass on that
# retry as green. That is right for one bar and invisible across many: a leg that needs its retry on
# every bar is a leg whose ceiling no longer fits the box, and a green bar says nothing about it. Each
# run record's verdict file carries `retried <n>`, and this sums it over the records EVERY git dir
# of the clone still holds — the common dir and each linked worktree's under its `worktrees/` —
# because the runner writes into whichever git dir ran the bar (TOOL-aMendedFleet-59). The detail
# is one row per leg, named by the `<i>.retry.leg` rows beside the verdicts: how often it was
# retried, how often it failed even on its retry, and in how many git dirs.
#
# REPORT-ONLY, over a window nobody chose here: the runner keeps a handful of run directories per
# git dir and sweeps the rest, and `git worktree remove` deletes a worktree's git dir with its
# records, so the figure describes the last few bars of each git dir still present and is not a
# history. LIVENESS is a verdict file that carries the key at all. A clone with no run record, or
# only records from a runner that predates the retry, cannot move this signal, and it says DEAD
# PROBE rather than a reassuring 0.
#
# WHAT IT DOES NOT CHECK: whether a retry was a spinning leg or a starved one; a timeout verdict
# cannot tell them apart. `unattributed` is the verdict sum minus the retry rows read, nonzero when
# a counted retry names no leg.
_RUN_RECORD_DIR = "gate-run"


def read_git_dirs(ctx) -> list[pathlib.Path]:
    """The clone's common dir, then every directory under its `worktrees/` in sorted order; empty
    when git cannot name the common dir."""
    out = ctx.git.run("rev-parse", "--path-format=absolute", "--git-common-dir")
    common = out.stdout.strip() if out.returncode == 0 else ""
    if not common:
        return []
    base = pathlib.Path(common)
    linked = base / "worktrees"
    return [base] + (sorted(d for d in linked.iterdir() if d.is_dir()) if linked.is_dir() else [])


def measure_legs_retried_after_timeout(ctx) -> dict:
    """`retried` summed over every readable run-record verdict under every git dir of the clone,
    with one detail row per leg the `<i>.retry.leg` rows name."""
    name = "legs_retried_after_timeout"
    total, of, judged, rows_read = 0, 0, 0, 0
    holding = set()
    legs: dict[str, dict] = {}
    for base in read_git_dirs(ctx):
        for verdict in sorted((base / _RUN_RECORD_DIR).glob("*/verdict")):
            try:
                text = verdict.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            of += 1
            holding.add(base)
            for line in text.splitlines():
                key, _, val = line.rstrip("\r").partition("\t")
                if key == "retried" and val.strip().isdigit():
                    total += int(val.strip())
                    judged += 1
                    break
            for row in sorted(verdict.parent.glob("*.retry.leg")):
                try:
                    fields = row.read_text(encoding="utf-8", errors="replace").splitlines()[0].split("\t")
                except (OSError, IndexError):
                    continue
                leg = legs.setdefault(fields[0], {"leg": fields[0], "retried": 0,
                                                  "failed_after_retry": 0, "git_dirs": set()})
                leg["retried"] += 1
                leg["failed_after_retry"] += (fields[1:2] or [""])[0].strip() != "ok"
                leg["git_dirs"].add(base)
                rows_read += 1
    detail = [dict(r, git_dirs=len(r["git_dirs"]))
              for r in sorted(legs.values(), key=lambda r: (-r["retried"], r["leg"]))]
    return {
        "signal": name,
        "value": total,
        "of": of,
        "tolerance": ctx.pins.get(name, 0),
        "gateable": False,
        "live": bool(judged),
        "git_dirs": len(holding),
        "unattributed": total - rows_read,
        "detail": detail,
    }


# --------------------------------------------------------------------------------------------
# Signal - builds over their undeclared-write budget (TOOL-dUnstuckLanding-17 S10; ported ahead of
# that landing as TOOL-aMendedFleet-92, which reads every git dir of the clone)
#
# The unattended kit's check 23 judges each run record against a per-build budget and prints the
# whole fleet's count on one line that never fails a run:
#   unattended: check 23 fleet — <n> undeclared write(s) over <g> graded pass(es) in <r> record(s)
#     · budget <b> per build · over <slug>=<n>…|none · range …|whole (…) · at <head8>
# The port printed `budget 0 per run` and no `range` field; the reader takes only the `over` and `at`
# fields, by their leading word, so either shape parses.
# This signal READS THAT LINE out of the newest run record the merge bar persisted under any git dir
# of the clone, through `read_git_dirs` and the `_RUN_RECORD_DIR` constant above, and never
# re-implements check 23: a second copy of its pass-commit join, render skip, ABSORB classification
# and brief exclusion would be two answers to one question. Running the kit gate instead would cost
# the leg's whole wall clock against a report measured in seconds.
#
# REPORT-ONLY. Where the total should bind, it binds here and not in a closing run's bar, and it binds
# nowhere by default: `gateable: False`. NOT ASKED where the repo carries no `.unattended.conf`; DEAD
# PROBE where it does and no run record holds a fleet line, which is what a clone that never ran the
# bar, or ran it before the line existed, looks like, and DEAD PROBE where the newest line reads
# `over unjudged`. A line that does not parse is detail, never a count.
#
# WHAT IT DOES NOT CHECK: anything newer than the bar run it read. The `at` sha names the HEAD that
# bar graded, and the detail says when HEAD has moved past it.
_FLEET_HEAD = "unattended: check 23 fleet — "


def _parse_fleet_line(line: str):
    """The fleet line's `over` pairs, its record count and its `at` sha, or None when it does not parse.

    An `over` field holding anything but `none` or `<slug>=<n>` tokens - `unjudged` is what check 23
    prints when the budget is undeclared or malformed - parses with `over` None and `unjudged` naming
    it, so no reader can take it for zero builds over.
    """
    if not line.startswith(_FLEET_HEAD):
        return None
    fields = line[len(_FLEET_HEAD):].rstrip("\r\n").split(" · ")
    m = re.match(r"^(\d+) undeclared write\(s\) over (\d+) graded pass\(es\) in (\d+) record\(s\)$",
                 fields[0])
    if not m:
        return None
    over, at, unjudged = None, None, ""
    for fld in fields[1:]:
        word, _, rest = fld.partition(" ")
        if word == "over":
            over = []
            toks = rest.split()
            if toks == ["none"]:
                continue
            for tok in toks:
                slug, eq, n = tok.partition("=")
                if not (eq and slug and n.isdigit()):
                    # `over unjudged`, or any token that is neither `none` nor `<slug>=<n>`: check 23
                    # judged no budget, so the line carries no count (implementation review round 1,
                    # M10). The caller reads this as unjudgeable, never as zero builds over.
                    over = None
                    unjudged = rest.strip()
                    break
                over.append((slug, int(n)))
            if over is None:
                break
        elif word == "at":
            at = rest.strip()
    if unjudged:
        return {"over": None, "records": int(m.group(3)), "at": at or "", "unjudged": unjudged}
    if over is None or not at:
        return None
    return {"over": over, "records": int(m.group(3)), "at": at, "unjudged": ""}


def measure_fleet_over_budget(ctx) -> dict:
    """Builds over their undeclared-write budget, read from the newest bar run's check 23 fleet line."""
    name = "fleet_over_budget"
    if not (ctx.root / ".unattended.conf").exists():
        return _build_not_asked(name, "no .unattended.conf at the repo root; the unattended kit, whose "
                                      "check 23 prints the fleet line, is not adopted")
    runs = []
    for base in read_git_dirs(ctx):
        if not (base / _RUN_RECORD_DIR).is_dir():
            continue
        for d in (base / _RUN_RECORD_DIR).iterdir():
            if d.is_dir():
                try:
                    runs.append((d.stat().st_mtime, d.name, d))
                except OSError:
                    continue
    runs.sort(reverse=True)
    found, unparsed = None, []
    for _mtime, run_id, d in runs:
        for out in sorted(d.glob("*.out")):
            try:
                text = out.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for line in text.splitlines():
                if not line.startswith(_FLEET_HEAD):
                    continue
                got = _parse_fleet_line(line)
                if got is None:
                    unparsed.append(f"{run_id}/{out.name}: a fleet line that does not parse: {line[:160]}")
                    continue
                found = (run_id, got)
                break
            if found:
                break
        if found:
            break
    if found is None:
        return _build_run_dead(name, 0, "DEAD PROBE — .unattended.conf is present and no run record under "
                                        f"the git dir's {_RUN_RECORD_DIR}/ carries a check 23 fleet line"
                                        + (f"; {len(unparsed)} carried one that does not parse" if unparsed else ""))
    run_id, got = found
    if got.get("unjudged"):
        return _build_run_dead(name, got["records"], f"DEAD PROBE — the newest fleet line, in run record "
                                                     f"{run_id}, reads `over {got['unjudged']}`: check 23 "
                                                     "judged no per-build budget, which it does when "
                                                     "UNDECLARED_WRITE_BUDGET is undeclared or not an "
                                                     "integer, so no count of builds over it exists")
    head = ctx.git.run("rev-parse", "HEAD")
    head8 = head.stdout.strip()[:8] if head.returncode == 0 else ""
    moved = bool(head8) and not head8.startswith(got["at"][:8])
    detail = [f"{slug} {n} at {got['at']}" + (f" (HEAD has moved to {head8} since)" if moved else "")
              for slug, n in got["over"]]
    detail.append(f"read from run record {run_id}")
    detail.extend(unparsed)
    return {
        "signal": name,
        "value": len(got["over"]),
        "of": got["records"],
        "tolerance": ctx.pins.get(name, 0),
        # REPORT ONLY — a closing run's bar never fails on the fleet total (spec F4).
        "gateable": False,
        "live": bool(got),
        "unjudgeable": 0,
        "detail": detail,
    }


# --------------------------------------------------------------------------------------------
# Signal - consecutive red runs of the remote CI workflow on the default branch (TOOL-aMendedFleet-8)
#
# Every other signal reads the local clone, so a remote CI that has failed for a week was invisible
# to the one report that exists to say the record no longer matches reality. This reads the newest
# runs through `gh` and counts the leading reds over COMPLETED runs: `failure`, `timed_out` and
# `startup_failure` extend the streak, `success` ends it, and every other conclusion, or a run still
# in flight, carries no verdict and is passed over and listed. A cancelled run therefore cannot fake
# a green.
#
# REPORT-ONLY, and NOT ASKED in two cases: the project layer declares no `REMOTE_CI_WORKFLOW`, or
# the run is `--check` / `--offenders`, so the merge bar's leg never makes a network call for a value
# it does not grade. LIVENESS is a `gh` answer holding at least one verdict-bearing run; `gh` absent,
# failing, timing out, unparseable or empty is DEAD PROBE, never a reassuring 0.
#
# WHAT IT DOES NOT CHECK: why a run failed, or which job inside it. The detail names the run ids, and
# `gh run view <id>` answers the rest. A window that is all red reports its own length with `capped`
# set: the streak is AT LEAST that, and may be longer than the window shows.
REMOTE_CI_RUN_LIMIT = 30
REMOTE_CI_TIMEOUT_S = 20
_CI_RED = frozenset({"failure", "timed_out", "startup_failure"})
_CI_GREEN = frozenset({"success"})


def read_remote_ci_runs(root: pathlib.Path, workflow: str, branch: str):
    """`(rows, None)` from `gh run list`, newest first, or `(None, <why>)` when it could not answer."""
    argv = ["gh", "run", "list", "--workflow", workflow, "--branch", branch,
            "--limit", str(REMOTE_CI_RUN_LIMIT),
            "--json", "databaseId,status,conclusion,event,createdAt,headSha"]
    try:
        out = subprocess.run(argv, cwd=str(root), capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=REMOTE_CI_TIMEOUT_S)
    except FileNotFoundError:
        return None, "`gh` is not on PATH"
    except subprocess.TimeoutExpired:
        return None, f"`gh run list` did not answer within {REMOTE_CI_TIMEOUT_S} s"
    if out.returncode != 0:
        first = (out.stderr.strip().splitlines() or ["(no stderr)"])[0]
        return None, f"`gh run list` exited {out.returncode}: {first}"
    try:
        rows = json.loads(out.stdout)
    except ValueError:
        return None, "`gh run list` printed output that is not JSON"
    if not isinstance(rows, list) or not all(isinstance(x, dict) for x in rows):
        return None, "`gh run list` printed JSON that is not a list of runs"
    return rows, None


def measure_red_streak(rows: list) -> dict:
    """The leading red streak over verdict-bearing runs, newest first, overall and per event.

    `streak` is None when no run carries a verdict, which the caller reports DEAD. `capped` is true
    when every verdict-bearing run in the window is red, so the true streak may be longer."""
    verdicts, passed_over = [], []
    for x in rows:
        c = (x.get("conclusion") or "") if x.get("status") == "completed" else ""
        if c in _CI_RED or c in _CI_GREEN:
            verdicts.append((x, c in _CI_RED))
        else:
            passed_over.append({"run": x.get("databaseId"), "status": x.get("status"),
                                "conclusion": x.get("conclusion") or "", "event": x.get("event")})
    streak = next((i for i, (_, red) in enumerate(verdicts) if not red), len(verdicts))
    by_event = {}
    for ev in ("push", "schedule"):
        reds = [red for x, red in verdicts if x.get("event") == ev]
        by_event[ev] = next((i for i, red in enumerate(reds) if not red), len(reds))
    newest_red = next((x.get("databaseId") for x, red in verdicts if red), None)
    newest_green = next((x.get("databaseId") for x, red in verdicts if not red), None)
    return {"streak": streak if verdicts else None, "examined": len(verdicts),
            "capped": bool(verdicts) and streak == len(verdicts), "by_event": by_event,
            "newest_red": newest_red, "newest_green": newest_green, "passed_over": passed_over}


def build_remote_ci_red_streak(ctx) -> dict:
    """Consecutive failed runs of the declared remote CI workflow on the default branch."""
    name = "remote_ci_red_streak"
    workflow = getattr(ctx, "remote_ci_workflow", "")
    if not workflow:
        return _build_not_asked(name, "the project layer declares no REMOTE_CI_WORKFLOW, so there is no "
                                      "remote CI to read")
    if getattr(ctx, "offline", False):
        return _build_not_asked(name, "skipped under --check and --offenders: the merge bar's leg makes "
                                      "no network call for a value it does not grade")
    branch = re.sub(r"^refs/(?:remotes/[^/]+|heads)/", "", ctx.git.base_ref)
    rows, why = read_remote_ci_runs(ctx.root, workflow, branch)
    m = measure_red_streak(rows or [])
    if why is None and m["streak"] is None:
        why = f"`gh run list` returned {len(rows)} run(s) of {workflow} on {branch} and none carries a verdict"
    live = why is None
    if not live:
        return {"signal": name, "value": 0, "of": 0, "tolerance": 0, "gateable": False,
                "live": live, "detail": [{"note": f"DEAD PROBE — {why}"}]}
    summary = {"workflow": workflow, "branch": branch, "newest_red": m["newest_red"],
               "newest_green": m["newest_green"] if m["newest_green"] is not None else "none in window",
               "capped": m["capped"], "by_event": m["by_event"], "passed_over": len(m["passed_over"])}
    return {"signal": name, "value": m["streak"], "of": m["examined"], "tolerance": 0,
            "gateable": False, "live": live, "detail": [summary, *m["passed_over"]]}


# --------------------------------------------------------------------------------------------
# Signal - codebase-map dossiers older than their paths (TOOL-aMendedFleet-37)
#
# REPORT-ONLY, and IT DECIDES NOTHING. The rule — a commit touching a path a dossier claims is not
# an ancestor of the dossier's own last commit — is the codebase-map kit's, computed by its
# `map_diff.py --stale-dossiers --json` over its own glob attribution. Spelling the attribution a
# second time here would be two answers to "which feature owns this path", and they would drift.
# Three states: NOT ASKED where the map kit does not resolve or the root has not adopted it, DEAD
# PROBE where the history is shallow, nothing touched a claimed path, or the reader failed, and a
# count otherwise. The detail is the refresh worklist, most-behind first.
# --------------------------------------------------------------------------------------------


def read_stale_dossiers(ctx):
    """`(returncode, stdout, stderr)` of `map_diff.py --stale-dossiers --json` at this report's root,
    or None when the codebase-map kit does not resolve beside this one. `CODEBASE_MAP_ROOT` is
    pinned to the root this report grades, so the map answers about the same tree."""
    try:
        kit = resolve_kit_dir("codebase-map", "map_diff.py", pathlib.Path(__file__).resolve().parent)
    except LookupError:
        return None
    env = dict(os.environ, CODEBASE_MAP_ROOT=str(ctx.root))
    try:
        out = subprocess.run([sys.executable, str(kit / "map_diff.py"), "--stale-dossiers", "--json"],
                             cwd=str(ctx.root), env=env, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=600)
    except (OSError, subprocess.SubprocessError) as exc:
        return (None, "", f"map_diff.py did not run: {exc}")
    return (out.returncode, out.stdout, out.stderr)


def build_stale_dossiers(ctx) -> dict:
    name = "dossiers_older_than_their_paths"
    got = read_stale_dossiers(ctx)
    if got is None:
        return _build_not_asked(name, "the codebase-map kit is not installed beside this one")
    rc, stdout, stderr = got
    said = ((stderr or "").strip().splitlines() or [f"exit {rc}"])[0][:240]
    if rc == 2:
        # map_diff's refusal: the root carries no .codebase-map.conf, so there is no map to grade.
        return _build_not_asked(name, f"no codebase map is adopted at this root ({said})")
    try:
        doc = json.loads(stdout) if rc == 0 else None
    except ValueError:
        doc = None
    if not isinstance(doc, dict) or not isinstance(doc.get("dossiers"), list):
        live, detail = False, [{"note": f"DEAD PROBE — map_diff.py --stale-dossiers gave no answer: {said}"}]
    else:
        live = doc.get("live") is True
        detail = ([{"note": f"DEAD PROBE — {doc.get('note')}"}] if not live else
                  ([{"note": doc["note"]}] if doc.get("note") else [])
                  + [r for r in doc["dossiers"] if isinstance(r, dict) and r.get("stale")])
    return {"signal": name,
            "value": int(doc.get("stale") or 0) if live else 0,
            "of": int(doc.get("of") or 0) if live else 0,
            "tolerance": ctx.pins.get(name, 0), "gateable": False, "live": live,
            "unjudgeable": 0, "detail": detail}


# --------------------------------------------------------------------------------------------
# TOOL-aMendedFleet-54 — live builds nobody is working, read from the index generator's own render
#
# The dormancy RULE is the memory-tree generator's (`LIVE_DORMANT_DAYS`, its `Activity` column), and
# this signal defines none of its own: it counts the cells that render wrote, exactly as the backlog
# signals count the generator's ask projection. The column is found BY HEADER NAME, so a column
# appended after it moves nothing. REPORT-ONLY and pinless: a dormant build is a state to read, and a
# ceiling on a count that moves with the calendar would red a tree nobody touched.
# --------------------------------------------------------------------------------------------

def build_live_builds_without_activity(ctx) -> dict:
    """Dormant rows of `<memory root>/LIVE.md`'s table; a cell neither `active` nor `dormant` is
    UNJUDGEABLE, never active. No file, or a table with no `Activity` header, is NOT ASKED."""
    name = "live_builds_without_activity"
    rel = f"{ctx.memory_root}/LIVE.md"
    try:
        lines = (ctx.root / rel).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return _build_not_asked(name, f"no {rel}; the memory-tree index is not rendered here")
    start = next((i for i in range(len(lines) - 1) if lines[i].lstrip().startswith("|")
                  and re.fullmatch(r"\|?[\s:|-]+\|?", lines[i + 1].strip() or "x")), None)
    header = ([c.strip() for c in lines[start].strip().strip("|").split("|")]
              if start is not None else [])
    if "Activity" not in header:
        return _build_not_asked(name, f"{rel} carries no table with an Activity column; "
                                      "a blank LIVE_DORMANT_DAYS renders none, so dormancy is not asked")
    col, last = header.index("Activity"), (header.index("Last record") if "Last record" in header else None)
    dormant, active, unjudgeable, detail = 0, 0, 0, []
    for line in lines[start + 2:]:
        if not line.lstrip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        state = cells[col] if col < len(cells) else ""
        if state == "active":
            active += 1
        elif state == "dormant":
            dormant += 1
            link = re.search(r"\[([^\]]+)\]", cells[0])
            row = {"build": link.group(1) if link else cells[0]}
            if last is not None and last < len(cells):
                row["last_record"] = cells[last]
            detail.append(row)
        else:
            unjudgeable += 1
            detail.append({"note": f"unjudgeable Activity cell {state!r}: {line.strip()[:160]}"})
    return {"signal": name, "value": dormant, "of": dormant + active, "tolerance": None,
            "gateable": False,
            # A table with the column and no judgeable row cannot move this count.
            "live": dormant + active > 0,
            "unjudgeable": unjudgeable, "detail": detail}


SIGNALS = [build_lexicon_marginal_offense_rate,
           signal_ledger, signal_spec_status, signal_shrink_only, signal_handkept,
           signal_dangling_pointers, signal_closed_specs_untraceable,
           signal_lexicon_verbs_unused, signal_lexicon_ratified_stale,
           build_live_backlog_rows, build_asks_disposed_overrides,
           build_readme_mechanism_drift,
           build_backlog_asks_contested, build_backlog_evidence_sha,
           build_backlog_asks_unlabelled,
           build_open_asks_cited_by_source,
           build_cutoff_keys_armed,
           build_source_cited_ids_with_no_record,
           build_backlog_stragglers,
           build_nonterminal_merged_runs,
           build_aborted_work_landed, build_discarded_work_landed,
           measure_legs_retried_after_timeout, measure_fleet_over_budget,
           build_remote_ci_red_streak,
           build_stale_dossiers,
           build_live_builds_without_activity]


# --------------------------------------------------------------------------------------------
# context + main
# --------------------------------------------------------------------------------------------

_CHARTER_CANDIDATES = ("AGENTS.md", "CLAUDE.md")


class Ctx:
    def __init__(self, root: pathlib.Path, conf: dict[str, str], proj, base_ref: str):
        self.root = root
        self.conf = conf
        self.memory_root = conf.get("MEMORY_ROOT", "memory").strip("/")
        self.ledger_dir = root / self.memory_root / "project" / "in-flight"
        self.git = Git(root, base_ref)
        self.product_globs = list(proj.PRODUCT_GLOBS)
        # The cutoff and the evidence paths for signal 6. Both are repo-shaped, so both live in the
        # project layer; both are optional, so an adopter who has not filled them gets a signal that
        # says "not asked" rather than one that guesses. `TRACE_GLOBS` falls back to PRODUCT_GLOBS —
        # a usable default — but this repo narrows it, because PRODUCT_GLOBS holds `.claude/` and the
        # kickoff manifest, and a records commit touching those would certify the record.
        self.trace_cutoff = (getattr(proj, "TRACE_CUTOFF", "") or "").strip()
        self.trace_globs = list(getattr(proj, "TRACE_GLOBS", None) or proj.PRODUCT_GLOBS)
        # TOOL-dMuffledSentinel-2. Where signal 6's waiver registry lives, repo-relative. BLANK keeps
        # `<memory-root>/project/trace-waiver.txt`; an adopter whose memory tree has no `project/`
        # directory declares somewhere it does have. The same getattr-and-fallback as above, so a
        # project layer that never heard of the key keeps today's path.
        self.trace_waiver = (getattr(proj, "TRACE_WAIVER", "") or "").strip()
        # EVIDENCE_GLOBS — signal 2's own population, narrower than PRODUCT_GLOBS for the same
        # reason TRACE_GLOBS is: a citation from a test file is the house's own bookkeeping
        # certifying the bookkeeping. getattr-and-fallback, so an older adopter's project layer
        # — which declares neither name — keeps working instead of tripping a required-attribute
        # refusal, and visibly gets the old unnarrowed behaviour until they fill it.
        self.evidence_globs = list(getattr(proj, "EVIDENCE_GLOBS", None) or proj.PRODUCT_GLOBS)
        # TOOL-aMendedFleet-8. The remote CI workflow file the red-streak signal reads; BLANK or
        # undeclared is NOT ASKED. `offline` is set by `main` under --check / --offenders, so the
        # merge bar's leg never spawns `gh`.
        self.remote_ci_workflow = (getattr(proj, "REMOTE_CI_WORKFLOW", "") or "").strip()
        self.offline = False
        fams = _read_families(conf)
        self.own_id_re = _build_own_id_re(root, fams)
        # ONE accessor for both projections, so the citation scan and the definition scan
        # cannot drift apart into two spellings of the same grammar.
        self.id_re = re.compile(_resolve_ident(root, fams))
        self.anchors = _resolve_anchors(root, fams)
        self.shrink_only = dict(proj.SHRINK_ONLY)
        self.handkept = list(proj.HANDKEPT)
        self.pins = dict(proj.PINS)
        # The project layer itself, so a signal can ask for a declaration the kit does
        # not know about — e.g. DECLARED_EMPTY, which an older adopter will not have.
        self.proj = proj
        # The layer's repo-relative path, or None outside the tree: signal 2 excludes it from its
        # evidence and the BASELINES guard reads it at the base (TOOL-aMendedFleet-56).
        try:
            self.layer_path = pathlib.Path(proj.__file__).resolve().relative_to(
                root.resolve()).as_posix()
        except (AttributeError, TypeError, ValueError):
            self.layer_path = None
        self.charter = getattr(proj, "CHARTER", None) or self._find_charter()
        # TOOL-aMendedFleet-53. The auto-memory directory signal 5 audits; BLANK or undeclared is
        # NOT ASKED, so an older adopter's project layer keeps importing.
        self.auto_memory_dir = (getattr(proj, "AUTO_MEMORY_DIR", "") or "").strip()

    def _find_charter(self) -> str | None:
        for c in _CHARTER_CANDIDATES:
            if (self.root / c).exists():
                return c
        return None


# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test.
# >>> remote_ladder_py -- canonical copy: resolve_remote.py in the gov lib dir (byte-identical; gated)
def resolve_remote(root):
    """-> (remote, branch, observed, refusal) for the repository at <root>. Fetches nothing.

    remote    GOV_REMOTE, else branch.<current>.remote unless it is ".", else the ONLY remote.
              Several remotes and none chosen, or a chosen name that is not a remote here, is a
              REFUSAL naming GOV_REMOTE. No remote at all is remote "" and NO refusal: the caller
              keeps its own no-remote fallback.
    observed  the branch refs/remotes/<remote>/HEAD names, or "". A caller whose GOV_DEFAULT_BRANCH
              only CROSS-CHECKS the observation reads this one.
    branch    GOV_DEFAULT_BRANCH, else observed, else "".
    A refusal empties the other three, so no caller can pick a remote the ladder refused.
    """
    import os
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    names = read("remote").split()
    listed = " ".join(names) or "none"
    cur = read("symbolic-ref", "--quiet", "--short", "HEAD")
    remote, how = os.environ.get("GOV_REMOTE") or "", "GOV_REMOTE"
    if not remote and cur:
        remote, how = read("config", "branch." + cur + ".remote"), "branch." + cur + ".remote"
        if remote == ".":
            remote = ""
    if not remote and len(names) == 1:
        remote = names[0]
    if not remote and len(names) > 1:
        where = "branch " + cur if cur else "a detached HEAD"
        return "", "", "", ("cannot choose a remote: GOV_REMOTE is unset, %s has no configured remote, "
                            "and this repository has %d remotes (%s). Name it: export GOV_REMOTE=<remote>."
                            % (where, len(names), listed))
    if remote and remote not in names:
        return "", "", "", ("%s names %s, which is no remote of this repository (%s). Name one that is: "
                            "export GOV_REMOTE=<remote>." % (how, remote, listed))
    observed = ""
    if remote:
        head = read("symbolic-ref", "--quiet", "--short", "refs/remotes/" + remote + "/HEAD")
        if head.startswith(remote + "/") and len(head) > len(remote) + 1:
            observed = head[len(remote) + 1:]
    return remote, os.environ.get("GOV_DEFAULT_BRANCH") or observed, observed, ""
# <<< remote_ladder_py


def resolve_base_ref(root: pathlib.Path, explicit: str | None) -> str:
    """The ref "landed" means, resolved REMOTE-FIRST. TOOL-dDerivedDocket-21 S1 and S2.

    Every ancestry answer, every `git show <base>:<path>` a ratchet reads and the trace walk are
    measured against what this returns, so it is the one input to the report that is not the tree.
    It used to be the bare default-branch NAME, which git resolves to the LOCAL branch: the same
    commit then read differently on a node whose local main was stale. Measured, not supposed — an
    ORPHAN_ID_PIN signal read 0 against a stale local main and 5 against the remote, and a pin raise
    that had already landed there read as a WEAKENED RATCHET on the stale node alone.

    THE LADDER, one answer per rung:
      1. `--base-ref`, verbatim. The escape hatch for every rung below.
      2. The REMOTE and the NAME, from the remote ladder inlined above (TOOL-dLadderedRemote-2):
         `GOV_REMOTE`, else the branch's configured remote, else the only remote; then
         `GOV_DEFAULT_BRANCH`, else that remote's HEAD. Several remotes and none chosen is a
         refusal naming GOV_REMOTE, and so is a remote whose default branch nothing names. This is
         the lander's derivation, and it used to ask only about a remote called `origin`.
      3. `refs/remotes/<remote>/<name>`, whenever it resolves.
      4. A clone with NO remote at all: `refs/heads/<name>`, ANNOUNCED on stderr. There is no
         staler or fresher copy of the branch in such a clone, so local is the record.
      5. A clone that HAS the remote and has not fetched the branch: a refusal. It cannot say what
         landed, and falling back to local there is exactly the defect rung 3 removes.

    Returns the ref; raises DriftError carrying the refusal. It fetches nothing: a report that
    fetched would be a network call on a leg that must run offline, and would still grade a ref the
    run itself could move.
    """
    if explicit:
        return explicit
    remote, name, _observed, refusal = resolve_remote(root)
    if refusal:
        raise DriftError(refusal + " Or pass --base-ref. Refusing to guess: every ancestry answer "
                         "in this report is measured against it.")
    if not name:
        fix = (f"`git remote set-head {remote} -a`" if remote
               else "add the remote this repository lands on")
        raise DriftError(f"cannot resolve a default branch. Set GOV_DEFAULT_BRANCH, or pass "
                         f"--base-ref, or {fix}. Refusing to guess: every "
                         f"ancestry answer in this report is measured against it.")

    # `encoding="utf-8"` like every other probe in this file. `text=True` ALONE decodes with the
    # platform default, which on a cp125x Windows node mis-decodes a non-ASCII branch name and,
    # under a strict-encoding lint, is a finding in its own right. Reported by adopter ic, whose
    # encoding-posture leg requires it (ARCH-dReadoptedConvoy-1 S7).
    def read_sha8(ref: str) -> str:
        out = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet",
                              ref + "^{commit}"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        return out.stdout.strip()[:8] if out.returncode == 0 else ""

    if not remote:
        local = f"refs/heads/{name}"
        at = read_sha8(local)
        if at:
            # ANNOUNCED, because a reader must never mistake the fallback for the remote answer.
            # When `at` is empty the caller's resolution check refuses and names the ref.
            print(f"drift-report: this clone has no remote, so the base is local {name} "
                  f"@ {at}", file=sys.stderr)
        return local
    tracking = f"refs/remotes/{remote}/{name}"
    if read_sha8(tracking):
        return tracking
    raise DriftError(f"{remote} has no tracking ref for '{name}'; run `git fetch {remote} {name}`. "
                     f"Refusing to fall back to the local branch: a stale local {name} is the "
                     f"input this report used to grade instead of what landed.")


def extract_unlocated(v):
    """A detail row with its LINE LOCATORS dropped — the `line`/`lines` fields and a trailing
    `:<digits>` on any string. ONE spelling, shared by `--offenders` and the history's key hash."""
    if isinstance(v, str):
        return re.sub(r":\d+$", "", v)
    if isinstance(v, list):
        return [extract_unlocated(x) for x in v]
    if isinstance(v, dict):
        return {k: extract_unlocated(x) for k, x in v.items() if k not in ("line", "lines")}
    return v


def derive_row_identity(row) -> str:
    """A detail row's identity for `BASELINES` (TOOL-aMendedFleet-56 S2): its `id` when that is a
    string, else its unlocated `--offenders` key, so a row with no id is never silently matched."""
    if isinstance(row, dict) and isinstance(row.get("id"), str):
        return row["id"]
    return json.dumps(extract_unlocated(row), sort_keys=True, ensure_ascii=False)


# TOOL-aMendedFleet-48. Every `--check` appends one row per signal here, in the git COMMON dir so
# every worktree of a clone writes one history. Readers locate columns by the header, never by
# position: the header is the file's whole contract. Node-local, never pushed, never rotated.
HISTORY_FILE = "drift-history.tsv"
HISTORY_COLUMNS = ("#utc", "sha", "base_ref", "base_sha", "signal", "state", "value", "of", "key_hash")


def build_history_rows(out: list, declared: set, utc: str, sha: str, base_ref: str,
                       base_sha: str) -> list[str]:
    """One TSV row per record, in `SIGNALS` order. `key_hash` is the first 16 hex of the SHA-256 of
    the record's detail keys exactly as `--offenders` spells them, sorted and LF-joined, so a member
    swap at an equal count moves it and a moved line number does not; `-` for any state but live."""
    rows = []
    for s in out:
        if s.get("not_asked"):
            state = "not-asked"
        elif not s["live"]:
            state = "declared-empty" if s["signal"] in declared else "dead"
        else:
            state = "live"
        key_hash = "-"
        if state == "live":
            keys = render_drift_offenders([s], [], [])
            key_hash = hashlib.sha256("\n".join(sorted(keys)).encode("utf-8")).hexdigest()[:16]
        rows.append("\t".join((utc, sha, base_ref, base_sha, s["signal"], state,
                               str(s["value"]), str(s["of"]), key_hash)))
    return rows


def resolve_history_path(root: pathlib.Path) -> pathlib.Path | None:
    """`<git-common-dir>/drift-history.tsv`, the common dir resolved against the repo root; None
    when git cannot name one."""
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--git-common-dir"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    common = out.stdout.strip()
    if out.returncode != 0 or not common:
        return None
    return (root / common).resolve() / HISTORY_FILE


def write_drift_history(path: pathlib.Path | None, rows: list[str]) -> None:
    """Append `rows` in ONE binary write, the header first into an absent or empty file, so two bars
    on one node interleave whole groups at worst. A failure is one stderr line and never touches the
    exit status; a success is one stdout line, so a missing line is a visible miss."""
    try:
        if path is None:
            raise OSError("git rev-parse --git-common-dir named no directory")
        with open(path, "ab") as fh:
            head = "" if fh.tell() else "\t".join(HISTORY_COLUMNS) + "\n"
            fh.write((head + "".join(r + "\n" for r in rows)).encode("utf-8"))
    except OSError as exc:
        print(f"drift-report: history NOT written to {path}: {exc}", file=sys.stderr)
        return
    print(f"drift-report: {len(rows)} history rows appended to {path}")


# TOOL-aMendedFleet-49. `--delta <base> <head>`: the history's one reader, beside its writer so the two
# share HISTORY_COLUMNS. Every case that cannot produce a delta is ONE `skipped` line and exit 0 —
# never a zero delta, which would read as "nothing moved" when nothing was measured.
def read_history_groups(path: pathlib.Path | None) -> tuple[list[dict], str]:
    """The history's groups in append order, each `{utc, sha, rows: {signal: row}, order}`; or no
    groups and the skip reason. A group is the CONSECUTIVE rows of one write, keyed by utc and sha:
    the writer appends one group in one binary write, so its rows are never split."""
    if path is None or not path.is_file():
        return [], f"no drift history in this clone ({path or 'git named no common dir'})"
    lines = path.read_bytes().decode("utf-8", errors="replace").splitlines()
    head = lines[0].split("\t") if lines else []
    if not set(HISTORY_COLUMNS) <= set(head):
        return [], f"{path.name} opens with a header this engine does not write"
    col = {name: head.index(name) for name in HISTORY_COLUMNS}
    groups: list[dict] = []
    for ln in lines[1:]:
        f = ln.split("\t")
        if len(f) < len(head):
            continue
        row = {name: f[i] for name, i in col.items()}
        key = (row["#utc"], row["sha"])
        if not groups or groups[-1]["key"] != key:
            groups.append({"key": key, "sha": row["sha"], "rows": {}, "order": []})
        if row["signal"] not in groups[-1]["rows"]:
            groups[-1]["order"].append(row["signal"])
        groups[-1]["rows"][row["signal"]] = row
    return groups, ""


# TOOL-aMendedFleet-90. A report-only probe DEAD for this many recorded readings in a row stops
# printing "ignore its value" and names the two ways out. Report only: the history is node-local, so
# a verdict built on it would not reproduce at a sha.
DEFAULT_DEAD_READINGS_LIMIT = 10


def _read_dead_keys(proj) -> tuple[int, dict]:
    """(DEAD_READINGS_LIMIT, DEAD_FILED) from the project layer, each absent taking its default; a
    present-but-malformed one is a named refusal rather than a comparison failing mid-table."""
    limit = getattr(proj, "DEAD_READINGS_LIMIT", None)
    limit = DEFAULT_DEAD_READINGS_LIMIT if limit is None else limit
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        raise DriftError(f"drift_signals.py declares DEAD_READINGS_LIMIT = {limit!r}; it must be a "
                         f"positive integer, or absent to take the shipped {DEFAULT_DEAD_READINGS_LIMIT}")
    filed = getattr(proj, "DEAD_FILED", None) or {}
    if not isinstance(filed, dict) or not all(isinstance(k, str) and isinstance(v, str)
                                              for k, v in filed.items()):
        raise DriftError("drift_signals.py declares DEAD_FILED that is not a dict from a signal name "
                         "to the id of the ask filed for it")
    return limit, filed


def derive_dead_streaks(path: pathlib.Path | None) -> tuple[dict, int] | None:
    """({signal: trailing readings whose state is `dead`}, readings), or None when the history is
    missing, unreadable or headerless. A READING is the last group in a run of consecutive groups at
    one sha, so a bar re-run at one commit does not age a signal; absence ends a streak."""
    try:
        groups, why = read_history_groups(path)
    except OSError:
        return None
    if why:
        return None
    readings: list[dict] = []
    for g in groups:
        if readings and readings[-1]["sha"] == g["sha"]:
            readings[-1] = g
        else:
            readings.append(g)
    streaks = {}
    for sig in {s for g in readings for s in g["rows"]}:
        k = 0
        for g in reversed(readings):
            row = g["rows"].get(sig)
            if row is None or row["state"] != "dead":
                break
            k += 1
        streaks[sig] = k
    return streaks, len(readings)


def derive_drift_delta(root: pathlib.Path, base: str, head: str) -> tuple[int, list[str]]:
    """(exit, lines) for `--delta`. Exit 2 only when an argument is not a commit; every other miss is
    one `skipped` line at exit 0. Ancestry comes from ONE `rev-list --parents` over both ends."""
    shas = []
    for arg in (base, head):
        r = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet", arg + "^{commit}"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0 or not r.stdout.strip():
            return 2, [f"drift-report: --delta: '{arg}' does not resolve to a commit"]
        shas.append(r.stdout.strip())
    base_sha, head_sha = shas
    groups, why = read_history_groups(resolve_history_path(root))
    if why:
        return 0, [f"drift-delta: skipped — {why}"]
    graph = subprocess.run(["git", "-C", str(root), "rev-list", "--parents", head_sha, base_sha],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
    parents = {}
    for ln in graph.stdout.splitlines():
        f = ln.split()
        if f:
            parents[f[0]] = f[1:]

    def derive_ancestors(start: str) -> set:
        seen, todo = set(), [start]
        while todo:
            c = todo.pop()
            if c not in seen:
                seen.add(c)
                todo.extend(parents.get(c, ()))
        return seen

    at_base, at_head = derive_ancestors(base_sha), derive_ancestors(head_sha)
    b = next((g for g in reversed(groups) if g["sha"] in at_base), None)
    if b is None:
        return 0, [f"drift-delta: skipped — no reading at or before BASE {base_sha[:8]}"]
    h = next((g for g in reversed(groups) if g["sha"] in at_head and g["sha"] not in at_base), None)
    if h is None:
        return 0, [f"drift-delta: skipped — no reading inside BASE..HEAD "
                   f"({base_sha[:8]}..{head_sha[:8]})"]
    return 0, render_drift_delta(b, h, base_sha, head_sha)


def render_drift_delta(b: dict, h: dict, base_sha: str, head_sha: str) -> list[str]:
    """The two readings, then one line per signal that moved, in the HEAD group's order and then any
    signal only BASE carries. A non-live side prints its state; equal live values with a moved
    key_hash are `members changed`; a signal one group lacks is `absent`."""
    def render_side(row):
        if row is None:
            return "absent"
        return row["value"] if row["state"] == "live" else row["state"]

    def render_at(end, g):
        return f"{end[:8]} read at {g['sha'][:8]} ({'equal' if g['sha'] == end else 'an ancestor'})"

    out = [f"drift-delta: BASE {render_at(base_sha, b)} · HEAD {render_at(head_sha, h)}"]
    for sig in h["order"] + [s for s in b["order"] if s not in h["rows"]]:
        x, y = b["rows"].get(sig), h["rows"].get(sig)
        if x is not None and y is not None and x["state"] == y["state"]:
            if x["state"] != "live" or (x["value"] == y["value"] and x["key_hash"] == y["key_hash"]):
                continue
            tail = " (members changed)" if x["value"] == y["value"] else ""
            out.append(f"drift-delta:   {sig} {x['value']} -> {y['value']}{tail}")
            continue
        lhs, rhs = render_side(x), render_side(y)
        # A live side beside a non-live or absent one names its state too: `dead -> live 0`.
        if x is not None and x["state"] == "live":
            lhs = f"live {lhs}"
        if y is not None and y["state"] == "live":
            rhs = f"live {rhs}"
        out.append(f"drift-delta:   {sig} {lhs} -> {rhs}")
    if len(out) == 1:
        out.append("drift-delta:   no signal moved between the two readings")
    return out


def render_drift_offenders(over: list, dead: list, ratchets: list) -> list[str]:
    """`--offenders`: one `<signal>\t<detail key>` line per thing `--check` would red on.

    THE SIGNATURE THE MERGE BAR GRADES THIS LEG WITH (TOOL-dDerivedDocket-23 S3). The bar's red
    attribution asks whether every offender at the branch is an offender at the base, and only a SET
    answers that. So each line is a KEY: every detail row of every gateable signal over its pin, every
    gateable signal that is DEAD, and every weakened ratchet — the three things `--check` exits 1 on,
    and nothing else. No count, no header, no cut: `--check` shows ten detail rows per signal, and a
    set built from ten can hide the eleventh. A signal bounded by `BASELINES` keys only what moved:
    each of its `new` rows, and `{"stale": "<id>"}` per stale id, never a row its set lists.

    A detail row's key is its JSON with sorted keys and its LINE LOCATORS dropped — the `line` field,
    and a trailing `:<digits>` on any string — because an unrelated edit above a finding moves its
    line and would read as a new finding on every branch. A key repeating inside one signal carries
    `#<k>`, its occurrence ordinal, so two identical rows stay two.
    """
    rows = []
    for s in over:
        # A BASELINED record keys only what MOVED: each new row and each stale id (TOOL-aMendedFleet-56 S5).
        fresh = set(s["new"]) if "baseline" in s else None
        for d in s["detail"]:
            if fresh is None or derive_row_identity(d) in fresh:
                rows.append((s["signal"], json.dumps(extract_unlocated(d), sort_keys=True, ensure_ascii=False)))
        for i in (s["stale"] if fresh is not None else ()):
            rows.append((s["signal"], json.dumps({"stale": i}, ensure_ascii=False)))
    for s in dead:
        rows.append((s["signal"], "DEAD — gateable, and its judgeable population is empty"))
    for r in ratchets:
        rows.append(("ratchet", " ".join(str(r).split())))
    seen: dict[str, int] = {}
    out = []
    for sig, key in rows:
        line = f"{sig}\t{' '.join(key.split())}"
        seen[line] = seen.get(line, 0) + 1
        out.append(line if seen[line] == 1 else f"{line}#{seen[line]}")
    return out


# --------------------------------------------------------------------------------------------
# --escape-ratio <month> — an OUTCOME reading, on demand only (TOOL-aMendedFleet-50)
# --------------------------------------------------------------------------------------------
# Of one month's product fixes, the share that repaired code which had already reached the base.
# NOT a signal: it costs a blame per fix and file, so it is never on the bar, never on the card,
# and it prints no comparison between months — one repository's before and after is not evidence.

# A parent-side line matching one of these is a version or audit stamp, not code a fix repaired.
ESCAPE_STAMP_PATTERNS = (
    re.compile(r"gov:kit [A-Za-z0-9_.-]+@"),
    re.compile(r"\bKIT_[A-Z0-9_]+_VERSION\s*="),
    re.compile(r'^\s*version\s*=\s*"'),
    re.compile(r"\blast-(?:audit|body-change):"),
)
_FIX_SUBJECT = re.compile(r"fix(?:\([^)]*\))?!?(?:[:\s]|$)")
_FIX_GREP = r"^fix(\([^)]*\))?!?([:[:space:]]|$)"
_HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? ")
_BLAME_HEAD = re.compile(r"^([0-9a-f]{40}) \d+ \d+")
_WILSON_Z = 1.959963984540054
_ESCAPE_CAVEAT = ("caveat: a difference between two months of one repository is not evidence of "
                 "an effect")


def build_landing_index(git: Git, tip: str) -> tuple[list, dict, dict]:
    """(first-parent chain oldest first, commit -> landing commit, commit -> committer epoch), from
    ONE `rev-list --timestamp --parents`. Walking the chain oldest first, every commit newly reachable
    from a first-parent commit lands with it, so the landings partition the history and a commit's
    landing's chain index orders when it reached the base."""
    walk = git.run("rev-list", "--timestamp", "--parents", tip, "--")
    if walk.returncode != 0 or not walk.stdout.strip():
        raise DriftError(f"`git rev-list {tip}` returned nothing, so no landing can be placed")
    parents, stamp = {}, {}
    for line in walk.stdout.split("\n"):
        f = line.split()
        if len(f) >= 2:
            stamp[f[1]], parents[f[1]] = int(f[0]), f[2:]
    chain, at = [], tip
    while at in parents:
        chain.append(at)
        at = parents[at][0] if parents[at] else None
    chain.reverse()
    landing: dict = {}
    for f in chain:
        stack = [f]
        while stack:
            c = stack.pop()
            if c not in landing:
                landing[c] = f
                stack.extend(p for p in parents.get(c, ()) if p not in landing)
    return chain, landing, stamp


def read_month_fixes(git: Git, revs: list, globs: list) -> list[dict]:
    """Every non-merge `fix` commit in `revs` touching `globs`, with its PARENT-SIDE lines — the
    lines its diff takes out, numbered as they read in its parent — from ONE `git log -U0 -p`.
    `--full-history`, because default simplification drops a side branch whose merge is TREESAME to
    main for these paths, and that branch's fixes landed all the same."""
    log = git.run("-c", "core.quotePath=false", "log", "--no-merges", "--no-renames", "--full-history",
                  "--no-color", "--no-ext-diff", "--src-prefix=a/", "--dst-prefix=b/", "-U0", "-p",
                  "-E", f"--grep={_FIX_GREP}", "--format=%x01%H%x02%s", *revs, "--", *globs)
    if log.returncode != 0:
        raise DriftError(f"`git log` over the month's landings failed: {log.stderr.strip()[:200]}")
    fixes, cur, path, left, at = [], None, None, 0, 0
    for line in log.stdout.split("\n"):
        if line.startswith("\x01"):
            sha, _, subject = line[1:].partition("\x02")
            cur = {"sha": sha, "subject": subject, "lines": {}}
            path, left = None, 0
            if _FIX_SUBJECT.match(subject):  # `--grep` reads the body too; the subject decides
                fixes.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("diff --git "):
            path, left = None, 0
        elif left == 0 and line.startswith("--- "):
            p = line[4:].strip('"')
            path = p[2:] if p.startswith("a/") else None
        elif m := _HUNK.match(line):
            at, left = int(m.group(1)), int(m.group(2) or 1)
        elif left and line.startswith("-") and path:
            cur["lines"].setdefault(path, []).append((at, line[1:]))
            at, left = at + 1, left - 1
    return fixes


def check_stamp_line(text: str) -> bool:
    """True when a parent-side line is a version or audit stamp (`ESCAPE_STAMP_PATTERNS`)."""
    return any(p.search(text) for p in ESCAPE_STAMP_PATTERNS)


def derive_wilson_interval(k: int, n: int) -> tuple[float, float] | None:
    """The 95% Wilson score interval for k of n; None at n 0. Unlike the normal approximation it
    stays inside [0, 1] at k 0 and at small n."""
    if n <= 0:
        return None
    p, z2 = k / n, _WILSON_Z * _WILSON_Z
    mid = (p + z2 / (2 * n)) / (1 + z2 / n)
    half = _WILSON_Z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / (1 + z2 / n)
    return max(0.0, mid - half), min(1.0, mid + half)


def measure_escape_ratio(git: Git, base_ref: str, base_sha: str, month: str, globs: list) -> dict:
    """The `--escape-ratio` result for one `YYYY-MM` month, as the `--json` object.

    A fix is ESCAPED when any parent-side line, stamps filtered out, blames to a commit whose landing
    is earlier than the fix's own; a boundary or unplaced commit counts as earlier. DIRECT is a fix
    that is its own landing, made on the first-parent line, and escaped by construction once it blames
    anything — printed beside the ratio as the share that measures workflow rather than defects.
    ponytail: one blame per fix and file, about 300 spawns a month; never a signal for that reason."""
    chain, landing, stamp = build_landing_index(git, base_sha)
    index = {f: i for i, f in enumerate(chain)}
    picked = [i for i, f in enumerate(chain) if datetime.datetime.fromtimestamp(
        stamp[f], datetime.timezone.utc).strftime("%Y-%m") == month]
    res = {"month": month, "base_ref": base_ref, "base_sha": base_sha, "n": 0, "escaped": 0, "ratio": None, "interval": None, "direct": 0,
           "unclassified": {}, "fixes": []}
    if not picked:
        return res
    lo, hi = min(picked), max(picked)
    revs = [chain[hi]] + ([f"^{chain[lo - 1]}"] if lo else [])
    month_landings = {chain[i] for i in picked}
    for fx in reversed(read_month_fixes(git, revs, globs)):
        sha = fx["sha"]
        own = landing.get(sha)
        if own not in month_landings:
            continue
        row = {"sha": sha, "landing": own, "direct": own == sha, "class": "", "blamed_landings": []}
        res["fixes"].append(row)
        kept = {p: [n for n, t in ls if not check_stamp_line(t)] for p, ls in fx["lines"].items()}
        if not globs:
            row["class"] = "no-product-globs"
        elif not fx["lines"]:
            row["class"] = "addition-only"
        elif not any(kept.values()):
            row["class"] = "stamp-only"
        if row["class"]:
            res["unclassified"][row["class"]] = res["unclassified"].get(row["class"], 0) + 1
            continue
        blamed, bounds = set(), set()
        for path, nums in kept.items():
            spans = []
            for n in sorted(set(nums)):
                if spans and n == spans[-1][1] + 1:
                    spans[-1][1] = n
                else:
                    spans.append([n, n])
            args = [a for s, e in spans for a in ("-L", f"{s},{e}")]
            out = git.run("blame", "--porcelain", *args, f"{sha}^", "--", path)
            if out.returncode != 0:
                raise DriftError(f"`git blame` of {path} in {sha[:8]}^ failed: {out.stderr.strip()[:200]}")
            cur = None
            for ln in out.stdout.split("\n"):
                if m := _BLAME_HEAD.match(ln):
                    cur = m.group(1)
                    blamed.add(cur)
                elif ln == "boundary" and cur:
                    bounds.add(cur)
        mine = index[own]
        lands = {landing.get(b, b) for b in blamed}
        row["blamed_landings"] = sorted(lands, key=lambda f: index.get(f, -1))
        early = any(b in bounds or index.get(landing.get(b), -1) < mine for b in blamed)
        row["class"] = "escaped" if early else "contained"
        res["n"] += 1
        res["escaped"] += early
        res["direct"] += row["direct"]
    if res["n"]:
        res["ratio"] = res["escaped"] / res["n"]
        res["interval"] = list(derive_wilson_interval(res["escaped"], res["n"]))
    return res


def render_escape_ratio(res: dict) -> list[str]:
    """The human form of `measure_escape_ratio`: n, escaped, the ratio and its interval, the DIRECT
    share, the unclassified counts, then the caveat line, which is printed on every outcome."""
    out = [f"# escape-ratio {res['month']} (base {res['base_ref']} @ {res['base_sha'][:8]})"]
    if not res["fixes"]:
        out.append("n          0 — the month is empty: no product fix landed on the base in it")
    else:
        out.append(f"n          {res['n']} product fixes classified")
        out.append(f"escaped    {res['escaped']}")
        if res["n"]:
            lo, hi = res["interval"]
            out.append(f"ratio      {res['ratio']:.3f} (95% Wilson interval {lo:.3f} to {hi:.3f})")
            out.append(f"direct     {res['direct']} of {res['n']} ({res['direct'] / res['n']:.3f}) — "
                       "landed on the first-parent line, escaped by construction once it blames anything")
        else:
            out.append("ratio      none — no fix was classified, so there is nothing to divide")
        un = res["unclassified"]
        out.append("unclassified " + (", ".join(f"{k} {v}" for k, v in sorted(un.items())) or "0"))
    out.append(_ESCAPE_CAVEAT)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Report whether this repo's records still match reality.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if a GATEABLE signal is over its pin")
    ap.add_argument("--offenders", action="store_true",
                    help="print one <signal> TAB <detail key> per thing --check would red on, and "
                         "nothing else; exits as --check does")
    ap.add_argument("--base-ref", default=None,
                    help="ref that 'landed' means, verbatim (default: refs/remotes/<remote>/<the "
                         "default branch>, the remote being GOV_REMOTE, the branch's configured "
                         "remote or the only one; a clone with no remote uses the local branch, "
                         "announced)")
    ap.add_argument("--delta", nargs=2, metavar=("BASE", "HEAD"),
                    help="print what moved between the history readings at BASE and inside "
                         "BASE..HEAD; report only, exit 0 unless an argument is not a commit")
    ap.add_argument("--escape-ratio", metavar="YYYY-MM", default=None,
                    help="on demand, minutes: the share of that month's product fixes that repaired "
                         "code already on the base; never part of the report or the bar")
    args = ap.parse_args(argv)

    if args.escape_ratio is not None:
        # TOOL-aMendedFleet-50 S1: a mode of its own. Beside `--check` it would put a blame per fix
        # on the bar, and beside `--offenders` or `--delta` neither output would mean what it says.
        clash = [f for f, on in (("--check", args.check), ("--offenders", args.offenders),
                                 ("--delta", args.delta)) if on]
        if clash:
            print(f"drift-report: --escape-ratio is an on-demand mode and does not combine with "
                  f"{', '.join(clash)}", file=sys.stderr)
            return 2
        if not re.fullmatch(r"\d{4}-(?:0[1-9]|1[0-2])", args.escape_ratio):
            print(f"drift-report: --escape-ratio wants a month as YYYY-MM (four-digit year, hyphen, "
                  f"two-digit month), got '{args.escape_ratio}'", file=sys.stderr)
            return 2

    if args.delta:
        # Reads the history only: no conf, no signals, no base ladder (TOOL-aMendedFleet-49).
        try:
            rc, lines = derive_drift_delta(repo_root(), *args.delta)
        except DriftError as exc:
            print(f"drift-report: {exc}", file=sys.stderr)
            return 2
        for ln in lines:
            print(ln, file=sys.stderr if rc else sys.stdout)
        return rc

    try:
        root = repo_root()
        conf = load_conf(root)
        proj = load_project_layer(root)
        # RESOLVED HERE, beside the other project-layer reads, and not at the --check call site.
        # An unusable RATCHET_LOOKBACK raised DriftError out of main() from there: a raw traceback
        # and rc=1, which is the leg's "a gateable signal is over its pin" exit -- so a config error
        # reported itself as drift. The docstring promised a refusal on this channel; this is the
        # line that keeps it. It also means the key is validated on EVERY run, not only under
        # --check, which is the run an adopter is told to make first.
        lookback = _read_lookback(proj)
        # TOOL-aMendedFleet-56 S1 and S4: an optional id set per gateable signal, refused before any
        # signal runs when its shape is wrong or a PINS entry bounds the same signal.
        baselines = getattr(proj, "BASELINES", None) or {}
        if not isinstance(baselines, dict) or not all(
                isinstance(v, (list, tuple)) and all(isinstance(i, str) for i in v)
                for v in baselines.values()):
            raise DriftError("drift_signals.py declares BASELINES that is not a dict from a signal "
                             "name to a list of offender id strings")
        both = sorted(set(baselines) & set(proj.PINS))
        if both:
            raise DriftError(f"{', '.join(both)} is declared in both PINS and BASELINES; a signal "
                             f"takes ONE bound, a count or an id set, so delete one of the two")
        dead_limit, dead_filed = _read_dead_keys(proj)
    except DriftError as exc:
        print(f"drift-report: {exc}", file=sys.stderr)
        return 2

    # THE NAME comes from the ladder `push-main.sh`, `.githooks/pre-push` and `check-verdict-epoch.sh`
    # share; the BASE it names is the remote-tracking ref. `resolve_base_ref` carries both halves.
    try:
        base_ref = resolve_base_ref(root, args.base_ref)
    except DriftError as exc:
        print(f"drift-report: {exc}", file=sys.stderr)
        return 2
    base_sha = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet",
                               base_ref + "^{commit}"], capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
    if base_sha.returncode != 0:
        print(f"drift-report: base ref '{base_ref}' does not resolve in this clone — this report "
              f"cannot judge ancestry against it.", file=sys.stderr)
        return 2
    base_at = base_sha.stdout.strip()[:8]
    if args.escape_ratio is not None:
        try:
            res = measure_escape_ratio(Git(root, base_ref), base_ref, base_sha.stdout.strip(),
                                       args.escape_ratio, list(proj.PRODUCT_GLOBS))
        except DriftError as exc:
            print(f"drift-report: {exc}", file=sys.stderr)
            return 2
        print(json.dumps(res, indent=1) if args.json else "\n".join(render_escape_ratio(res)))
        return 0
    ctx = Ctx(root, conf, proj, base_ref)
    ctx.offline = bool(args.check or args.offenders)
    # The hand-kept signal runs LAST and is handed the names every other signal reported, so a
    # hand-kept list of signal names compares against the engine's own output (TOOL-aMendedFleet-52
    # S2); the records keep SIGNALS order. Running every signal twice would double the report.
    by_fn = {fn: fn(ctx) for fn in SIGNALS if fn is not signal_handkept}
    ctx.signal_names = {s["signal"] for s in by_fn.values()} | {"handkept_inventories_disagreeing_with_source"}
    out = [by_fn[fn] if fn in by_fn else fn(ctx) for fn in SIGNALS]
    for s in out:
        # A None tolerance is a report-only signal with NO PIN BY DESIGN (TOOL-aMendedFleet-51): its
        # pin stays None unless PINS declares one, and the table prints `report only, no pin`. A
        # gateable record never carries one, because `--check` compares its value against the pin.
        assert not (s["gateable"] and s["tolerance"] is None), f"{s['signal']}: gateable with no tolerance"
        s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])
    # TOOL-aMendedFleet-56 S4 and S3. A key naming no gateable record bounds nothing, so it is
    # refused here, before the table, the JSON, the offender keys and the history write. A baselined
    # record is then judged on its MEMBERS: `new` rows the set does not carry, `stale` ids no row
    # carries. A record that is not live judges nothing, so both stay empty and DEAD reports it.
    stray = sorted(set(baselines) - {s["signal"] for s in out if s["gateable"]})
    if stray:
        print(f"drift-report: BASELINES names {', '.join(stray)}, which this report does not "
              f"produce as a gateable signal; an id set bounds only a gateable one, so delete the "
              f"entry", file=sys.stderr)
        return 2
    for s in out:
        if s["signal"] in baselines:
            listed = set(baselines[s["signal"]])
            have = {derive_row_identity(d) for d in s["detail"]} if s["live"] else listed
            s["baseline"] = s["pin"] = len(listed)
            s["new"], s["stale"] = sorted(have - listed), sorted(listed - have)

    # THE THREE POPULATIONS `--check` reds on, computed ONCE for both modes that read them, so
    # `--offenders` cannot disagree with `--check` about what is red. Neither function prints, so
    # computing them above the table moves no line of `--check`'s output.
    #
    # A DEAD GATEABLE SIGNAL IS A FAILURE, not a skip. The old predicate required `live`, so a
    # probe that had gone blind scored exactly like a probe that had found nothing — which is how
    # a pre-flatten glob stayed green on the merge bar. This is the generic fix: it catches the
    # next blind probe without anyone having to notice the next layout change.
    #
    # Except when a signal is EMPTY BY DECLARATION. `SHRINK_ONLY` ships empty on purpose, and a
    # rule with no exception here would red every fresh adopter on their first run. The exception
    # is enumerated in the project layer, never inferred.
    ratchets, over, dead = [], [], []
    if args.check or args.offenders:
        declared = set(getattr(ctx.proj, "DECLARED_EMPTY", ()) or ())
        ratchets = ratchet_findings(ctx.git, root, getattr(ctx.proj, "RATCHETS", ()), lookback)
        ratchets += build_lang_mode_findings(ctx.git, root, lookback=lookback)
        if ctx.layer_path:
            ratchets += build_baseline_findings(ctx.git, ctx.layer_path, baselines, proj.PINS)
        over = [s for s in out if s["gateable"] and s["live"] and (
            bool(s["new"] or s["stale"]) if "baseline" in s else s["value"] > s["pin"])]
        dead = [s for s in out if s["gateable"] and not s["live"] and s["signal"] not in declared]

    if args.offenders:
        # Stdout is keys and nothing else, and the exit is `--check`'s.
        keys = render_drift_offenders(over, dead, ratchets)
        sys.stdout.buffer.write("".join(k + "\n" for k in keys).encode("utf-8"))
        return 1 if (over or dead or ratchets) else 0

    # TOOL-aMendedFleet-90: the history is read ONCE, here, before `--check` appends this run to it.
    history_path = resolve_history_path(root)
    streaks = derive_dead_streaks(history_path)
    for s in out:
        s["dead_readings"] = None if streaks is None else streaks[0].get(s["signal"], 0)

    if args.json:
        print(json.dumps(out, indent=1))
    else:
        # FULL, because the history row carries HEAD whole; the header shows eight, like base_at.
        head_sha = ctx.git.run("rev-parse", "HEAD").stdout.strip()
        head = head_sha[:8]
        # THE BASE IS A HEADER FACT, ref AND sha. Two nodes comparing reports can then see at once
        # whether they graded the same commit, which a bare branch name never told them.
        print(f"# drift-report at {head} (base {base_ref} @ {base_at}) · kit {KIT_DRIFT_AUDIT_VERSION}")
        # The reader's liveness line: a history it could not read says so, never the old status alone.
        where = history_path or "no git common dir"
        print(f"# dead-for-N: {streaks[1]} readings recorded at {where} · limit {dead_limit}"
              if streaks is not None else f"# dead-for-N: no history at {where}, nothing judged")
        # A filing must not outlive the death it filed.
        live_now = {s["signal"]: s["live"] and not s.get("not_asked") for s in out}
        for sig in sorted(dead_filed):
            if sig not in live_now or live_now[sig]:
                why = "is not a signal of this report" if sig not in live_now else "is live in this run"
                print(f"# dead-for-N: DEAD_FILED names {sig}, which {why}; take the entry out")
        print(f"# {'signal':<48} {'value':>7} {'of':>6}  status")
        for s in out:
            if s.get("not_asked"):
                # The record's own note where it carries one: a NOT ASKED that is a mode skip is not
                # a repo that "does not adopt" what the signal reads (TOOL-aMendedFleet-8 S5).
                note = next((d.get("note") for d in s["detail"][:1] if isinstance(d, dict)), None)
                status = f"not asked — {note or 'this repo does not adopt what the signal reads'}"
            elif not s["live"]:
                k = s["dead_readings"]
                if s["signal"] in set(getattr(ctx.proj, "DECLARED_EMPTY", ()) or ()):
                    status = "empty by declaration — nothing to measure here yet"
                elif not s["gateable"] and k is not None and k >= dead_limit:
                    # TOOL-aMendedFleet-90 S3. A gateable dead record keeps its status: `--check` reds it.
                    status = (f"DEAD PROBE for {k} readings — filed {dead_filed[s['signal']]}"
                              if s["signal"] in dead_filed else
                              f"DEAD PROBE for {k} readings — take it out of SIGNALS, or file an ask "
                              f"and declare it in DEAD_FILED")
                else:
                    status = "DEAD PROBE — signal cannot move, ignore its value"
            elif s["value"] < 0:
                status = "n/a"
            elif "baseline" in s:
                status = ("OVER BASELINE — gateable" if s["new"] or s["stale"]
                          else f"ok (baseline {s['baseline']})")
            elif s["pin"] is None:
                # NOT `over pin 0`: a signal with no pin by design has nothing to be over, and a
                # red-looking word nobody acts on trains the reader to skip the whole column.
                status = "report only, no pin"
            elif s["gateable"] and s["value"] > s["pin"]:
                status = f"OVER PIN {s['pin']} — gateable"
            elif s["gateable"]:
                status = f"ok (pin {s['pin']}" + (", drain it" if s["pin"] else ")") + (")" if s["pin"] else "")
            elif s["value"] > s["pin"]:
                # AGAINST THE PIN, not the bare tolerance. `pin` defaults to `tolerance` where PINS
                # declares none, so this changes nothing for a signal without one — but a
                # report-only signal WITH a pin could otherwise never print a calm status at its own
                # declared floor. A signal whose only product is its status line was reporting
                # "over" at exactly the value its pin ratifies, which trains a reader to ignore the
                # column. The two gateable branches above already compare against `pin`.
                status = f"over pin {s['pin']} (report only)"
            else:
                # NAMING THE PIN, like the gateable branch does. A bare `ok` beside a sibling that
                # prints its pin and a drain hint reads as "nothing declared here", which is the
                # opposite of true for a signal whose pin is the only thing holding it.
                status = (f"ok (pin {s['pin']}, drain it)" if s["pin"] else "ok")
            print(f"  {s['signal']:<48} {s['value']:>7} {s['of']:>6}  {status}")
        print("\n# detail: rerun with --json")

    if args.check:
        if not args.json:
            # TOOL-aMendedFleet-48: the bar's reading persists. `--json` never writes, even beside
            # `--check`, so its stdout stays one JSON document; the write never moves the verdict.
            utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            write_drift_history(resolve_history_path(root), build_history_rows(
                out, set(getattr(ctx.proj, "DECLARED_EMPTY", ()) or ()), utc, head_sha, base_ref,
                base_sha.stdout.strip()))
        # The populations are computed above, once, for this mode and `--offenders` alike.
        for r in ratchets:
            print(f"\ndrift-report: RATCHET WEAKENED — {r}", file=sys.stderr)
        for s in over:
            if "baseline" in s:
                print(f"\ndrift-report: {s['signal']} = {s['value']} against BASELINES "
                      f"({s['baseline']} listed in {ctx.layer_path}) — this set is shrink-only",
                      file=sys.stderr)
                for i in s["new"]:
                    print(f"  new   {i} — an offender the set does not list: remove its cause, "
                          f"never list it", file=sys.stderr)
                for i in s["stale"]:
                    print(f"  stale {i} — listed but no longer an offender: delete its line from "
                          f"BASELINES['{s['signal']}']", file=sys.stderr)
                continue
            print(f"\ndrift-report: {s['signal']} = {s['value']} (pin {s['pin']}) — this list is shrink-only",
                  file=sys.stderr)
            for d in s["detail"][:10]:
                print(f"  {d}", file=sys.stderr)
        for s in dead:
            print(f"\ndrift-report: {s['signal']} is DEAD — gateable, but its judgeable population is "
                  f"empty, so its value ({s['value']}) means nothing. Either its selector no longer "
                  f"matches this tree, or the signal is empty on purpose and belongs in "
                  f"DECLARED_EMPTY with the reason.", file=sys.stderr)
        return 1 if (over or dead or ratchets) else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
