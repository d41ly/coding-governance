#!/usr/bin/env python3
"""drift_report.py — does this repo's own RECORD of its state still describe reality?

gov:kit drift-audit@1.4

    python tools/drift-audit/drift_report.py            # human table, always exits 0
    python tools/drift-audit/drift_report.py --json     # machine-readable, always exits 0
    python tools/drift-audit/drift_report.py --check    # exit 1 if a GATEABLE signal is over its pin

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
ledger, a node registry in the charter). Everything genuinely repo-shaped — which paths are product
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
import json
import os
import pathlib
import re
import subprocess
import sys

# The kit never leaves bytecode in the adopter's worktree (matching memory-recall's query.py).
sys.dont_write_bytecode = True

KIT_DRIFT_AUDIT_VERSION = "1.5"

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

    A deliberate COPY of the twenty lines in codebase-map's `map_lib.load_conf`, not an import of
    it: kits are copied into adopters independently, and importing across kit directories would make
    drift-audit un-adoptable without codebase-map. The drift is gated by asserting this parser
    against BASH sourcing the same file in selftest.py, never against a second Python parser — two
    operands from one generator assert nothing (the adopter's own review-2 F5 lesson).
    """
    p = root / CONF_NAME
    if not p.exists():
        raise DriftError(
            f"{CONF_NAME} not found at {root}. It is owned by the memory-tree kit; adopt that first.\n"
            "Minimum stub:\n  MEMORY_ROOT=memory\n  DISCIPLINES=\"...\"\n"
        )
    conf: dict[str, str] = {}
    for raw in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip().lstrip("﻿")
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        v = v.strip().strip("\r")
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        conf[k.strip()] = v
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
# Group 2 is the slug, for `signal_closed_specs_untraceable` — which asks a BUILD-level question the
# slug answers correctly. Group 1 is untouched, so `signal_spec_status` reads exactly what it did.
_OWN_ID = re.compile(r"^#\s+([A-Z]+-([a-zA-Z]+)-\d+)\b", re.M)
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
        own = _OWN_ID.search(head)
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
        hit = ctx.git.run("grep", "-l", "-w", "-F", own.group(1), "--", *ctx.product_globs)
        if hit.returncode == 0 and hit.stdout.strip():
            suspect.append({
                "file": str(p.relative_to(ctx.root)).replace("\\", "/"),
                "id": own.group(1),
                "status": m.group(1).upper(),
                "cited_in": hit.stdout.strip().splitlines()[:3],
            })
    return {
        "signal": "non_terminal_specs_cited_by_product_source",
        "value": len(suspect),
        "of": checked,
        "tolerance": 0,
        "gateable": True,
        "live": checked > 0,
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


def signal_shrink_only(ctx) -> dict:
    rows = []
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
        rows.append({"file": rel, "what": what, "entries": now, "seed": seed,
                     "shrunk_by": (seed - now) if seed is not None else None})
    stalled = [r for r in rows if r["shrunk_by"] is not None and r["shrunk_by"] <= 0]
    return {
        "signal": "shrink_only_lists_not_shrinking",
        "value": len(stalled),
        "of": len(rows),
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
        rows.append({"record": spec["record"], "source": spec.get("source", "?"),
                     "claims": claims, "actual": actual, "agrees": claims == actual})
    # A MAGNITUDE, not a per-row boolean. Scored as a boolean over a one-row population the value
    # lived in {0, 1} against a pin of 1, so `value > pin` needed 2 and the ceiling was 1: gateable
    # in name, unsatisfiable in fact. Counting the items that disagree gives a number that can DRAIN
    # — one charter bullet at a time — and a pin that means something.
    gap = 0
    pop = 0
    for r in rows:
        if isinstance(r.get("claims"), int) and isinstance(r.get("actual"), int) and r["claims"] >= 0:
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
# Signal 5 — this node's own ledger pointers that no longer resolve
# --------------------------------------------------------------------------------------------

_LOCAL_PATH = re.compile(r"(?:[A-Za-z]:[\\/]|/(?:home|Users)/)[A-Za-z0-9_\\/.-]+")


def signal_dangling_pointers(ctx) -> dict:
    """Node-scoped ON PURPOSE. Another node's paths live on another machine and are unknowable from
    this clone; reporting them missing would be the confidently-wrong-answer class. If the node tag
    cannot be resolved, the probe reports DEAD rather than guessing."""
    tag = ctx.node_tag
    if not tag:
        return {"signal": "dangling_pointers_in_own_ledger", "value": -1, "of": 0, "tolerance": 0,
                "gateable": False, "live": False,
                "detail": [{"note": "node tag not resolvable from the charter registry; skipped"}]}
    f = ctx.ledger_dir / f"{tag}.md"
    if not f.exists():
        return {"signal": "dangling_pointers_in_own_ledger", "value": -1, "of": 0, "tolerance": 0,
                "gateable": False, "live": False,
                "detail": [{"note": f"no ledger file for node {tag}"}]}
    txt = f.read_text(encoding="utf-8", errors="replace")
    paths = sorted({p.replace("\\", "/").rstrip("`,)./") for p in _LOCAL_PATH.findall(txt)})
    gone = [p for p in paths if not pathlib.Path(p).is_dir()]
    return {
        "signal": "dangling_pointers_in_own_ledger",
        "value": len(gone),
        "of": len(paths),
        "tolerance": 0,
        "gateable": False,
        "live": len(paths) > 0,
        "detail": [{"node": tag, "gone": gone}],
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
    wpath = ctx.root / ctx.memory_root / "project" / "trace-waiver.txt"
    if wpath.is_file():
        for raw_row in wpath.read_text(encoding="utf-8", errors="replace").splitlines():
            if not raw_row.strip() or raw_row.lstrip().startswith("#"):
                continue
            cols = raw_row.split("\t")
            waived[cols[0].strip()] = cols[-1].strip() if len(cols) > 1 else ""
    used: set[str] = set()

    suspect, checked, unjudged = [], 0, 0
    for p in sorted(ctx.root.glob(f"{ctx.memory_root}/builds/*/spec/**/*.md")):
        head = p.read_text(encoding="utf-8", errors="replace")[:4000]
        m = _STATUS.search(head)
        if not m or m.group(1).upper() not in TERMINAL:
            continue
        own, when = _OWN_ID.search(head), _HEADER_DATE.search(head)
        if not own or not when:
            unjudged += 1  # no id or no header date: the probe cannot judge it. Counted, not guessed.
            continue
        if when.group(1) < ctx.trace_cutoff:
            unjudged += 1  # grandfathered: it closed before the convention it would be judged by.
            continue
        checked += 1
        uid, slug = own.group(1), own.group(2)
        # SLUG ONLY, and that is not a narrowing: `\bslug\b` already matches inside
        # `FAMILY-slug-seq`, because the hyphens either side of the slug are non-word bytes.
        # An `id or slug` disjunct reads like a two-key oracle and is one unfalsifiable clause;
        # the id half could never decide a case the slug half did not already decide.
        if re.search(r"\b" + re.escape(slug) + r"\b", subjects):
            continue
        rel = str(p.relative_to(ctx.root)).replace("\\", "/")
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
            "note": "waives a spec that is absent, not terminal, or traceable again",
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
    kit = str(ctx.root / "tools" / "lexicon")
    if kit not in _sys.path:
        _sys.path.insert(0, kit)
    try:
        from lexicon_conf import load_conf
        conf = load_conf(_resolve_lexicon_conf(ctx))
    except Exception:
        return None
    return (conf.get("VERBS") or {}), (conf.get("ratified") or "").strip(), (conf.get("LANGS") or "")


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

    THE DAY-ONE SEED IS NOT ZERO, and that is correct rather than a failed build. `--scaffold` derives
    the table by frequency and a human then curates it; curation ADDS aspirational verbs the corpus
    does not use yet. Same shape as `non_terminal_specs_cited_by_product_source`, whose pin comment
    records a known residual rather than proven rot.
    """
    name = "lexicon_verbs_declared_but_unused"
    if not _resolve_lexicon_conf(ctx):
        return _build_not_asked(name, "no .lexicon.conf at the repo root; the lexicon kit is not adopted")
    loaded = _load_lexicon(ctx)
    if loaded is None:
        return _build_not_asked(name, ".lexicon.conf is present but its kit is not importable here "
                                      "(root-prefix install, mid-teardown, or an unparseable conf)")
    import sys as _sys
    kit = str(ctx.root / "tools" / "lexicon")
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

    declared = {ext: (pset, mode) for ext, pset, mode in _langs({"LANGS": _l})}
    used: set[str] = set()
    for rel in lex.tracked_files(ctx.root):
        ext = lex.ext_of(rel)
        if ext not in declared:
            continue
        pset, mode = declared[ext]
        if mode == "dark" or (mode == "probe" and pset not in lex.PATTERN_SETS):
            continue
        try:
            got = lex.extract(ctx.root / rel, mode, pset)
        except (SyntaxError, OSError):
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


# --------------------------------------------------------------------------------------------
# Signal 9 — live backlog rows per shard (TOOL-aRelaxedShard-4)
#
# The bound that actually moves. Rotation carries forward every non-terminal row, so a shard's FLOOR
# is its live set: when nothing terminal is left, rotating is a no-op and the next row breaches the
# byte cap. That is how `TOOL-cSettledDocket-16` and `TOOL-aRelaxedShard-1` happened, twice, and
# neither the byte cap nor the map ratchet can see it coming.
#
# REPORT-ONLY, deliberately. `drift-audit records` is an unguarded merge-bar leg, so a pin set N days
# ahead of today's count becomes a scheduled refusal: the day the count crosses it every merge reds
# until someone raises the pin or closes rows, which is the refusal this signal exists to make
# unnecessary. `shrink_only_lists_not_shrinking` runs the same way for the same reason. If a later
# unit gates this, it must pin a MEASURED value with a movement rule AND declare that pin in the
# shipped conf template — a signal absent from an adopter's PINS falls back to tolerance 0, so a
# gateable version would red their first run on one open row.
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
def build_live_backlog_rows(ctx) -> dict:
    """Live (non-terminal) rows per backlog shard, reported per shard and never gated."""
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
        # The threshold comes from the project layer, and for a NON-GATEABLE signal the status line
        # compares against `tolerance` rather than `pin` (see the report loop), so it is read here.
        # Absent, it is 0 and every non-empty shard reads "out of tolerance" — which trains a reader
        # to ignore the line, the failure mode this signal is supposed to cure.
        "tolerance": ctx.pins.get("live_backlog_rows_per_shard", 0),
        "gateable": False,
        # A tree with no backlog shards at all cannot move this signal, so it reports DEAD rather than
        # a reassuring 0 — the liveness assertion every signal here carries.
        "live": bool(judgeable),
        "detail": rows,
    }


SIGNALS = [signal_ledger, signal_spec_status, signal_shrink_only, signal_handkept,
           signal_dangling_pointers, signal_closed_specs_untraceable,
           signal_lexicon_verbs_unused, signal_lexicon_ratified_stale,
           build_live_backlog_rows]


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
        self.shrink_only = dict(proj.SHRINK_ONLY)
        self.handkept = list(proj.HANDKEPT)
        self.pins = dict(proj.PINS)
        # The project layer itself, so a signal can ask for a declaration the kit does
        # not know about — e.g. DECLARED_EMPTY, which an older adopter will not have.
        self.proj = proj
        self.charter = getattr(proj, "CHARTER", None) or self._find_charter()
        self.node_tag = self._resolve_node_tag()

    def _find_charter(self) -> str | None:
        for c in _CHARTER_CANDIDATES:
            if (self.root / c).exists():
                return c
        return None

    def _resolve_node_tag(self) -> str | None:
        """Match this machine's user against the charter's node-registry table."""
        import os

        if not self.charter:
            return None
        user = (os.environ.get("USERNAME") or os.environ.get("USER") or "").lower()
        if not user:
            return None
        text = (self.root / self.charter).read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            m = re.match(r"\|\s*`([a-z])`\s*\|\s*`?([A-Za-z0-9_@.-]+)`?", line.strip())
            if m and m.group(2).lower() in user:
                return m.group(1)
        return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Report whether this repo's records still match reality.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if a GATEABLE signal is over its pin")
    ap.add_argument("--base-ref", default=None,
                    help="ref that 'landed' means (default: the conf's DEFAULT_BRANCH, else main)")
    args = ap.parse_args(argv)

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
    except DriftError as exc:
        print(f"drift-report: {exc}", file=sys.stderr)
        return 2

    # THE LADDER THIS REPO ALREADY SHARES — `push-main.sh`, `.githooks/pre-push` and
    # `check-verdict-epoch.sh` all resolve the default branch this way. The old line was
    # `args.base_ref or conf["DEFAULT_BRANCH"] or "main"`: a fourth spelling, keyed on a conf key no
    # kit declares and no doc mentions, falling back to a literal that may not exist. On a repo whose
    # default is not `main`, every ancestry answer was silently wrong rather than refused.
    base_ref = args.base_ref or os.environ.get("GOV_DEFAULT_BRANCH") or ""
    if not base_ref:
        head = subprocess.run(["git", "-C", str(root), "symbolic-ref", "--quiet",
                               "refs/remotes/origin/HEAD"], capture_output=True, text=True)
        base_ref = head.stdout.strip().rpartition("/")[2] if head.returncode == 0 else ""
    if not base_ref:
        print("drift-report: cannot resolve a default branch. Set GOV_DEFAULT_BRANCH, or pass "
              "--base-ref, or `git remote set-head origin -a`. Refusing to guess: every ancestry "
              "answer in this report is measured against it.", file=sys.stderr)
        return 2
    if subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet", base_ref],
                      capture_output=True).returncode != 0:
        print(f"drift-report: base ref '{base_ref}' does not resolve in this clone — this report "
              f"cannot judge ancestry against it.", file=sys.stderr)
        return 2
    ctx = Ctx(root, conf, proj, base_ref)
    out = [s(ctx) for s in SIGNALS]
    for s in out:
        s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])

    if args.json:
        print(json.dumps(out, indent=1))
    else:
        head = ctx.git.run("rev-parse", "--short", "HEAD").stdout.strip()
        print(f"# drift-report at {head} (base {base_ref}) · kit {KIT_DRIFT_AUDIT_VERSION}")
        print(f"# {'signal':<48} {'value':>7} {'of':>6}  status")
        for s in out:
            if s.get("not_asked"):
                status = "not asked — this repo does not adopt what the signal reads"
            elif not s["live"]:
                status = ("empty by declaration — nothing to measure here yet"
                          if s["signal"] in set(getattr(ctx.proj, "DECLARED_EMPTY", ()) or ())
                          else "DEAD PROBE — signal cannot move, ignore its value")
            elif s["value"] < 0:
                status = "n/a"
            elif s["gateable"] and s["value"] > s["pin"]:
                status = f"OVER PIN {s['pin']} — gateable"
            elif s["gateable"]:
                status = f"ok (pin {s['pin']}" + (", drain it" if s["pin"] else ")") + (")" if s["pin"] else "")
            elif s["value"] > s["tolerance"]:
                status = "out of tolerance (report only)"
            else:
                status = "ok"
            print(f"  {s['signal']:<48} {s['value']:>7} {s['of']:>6}  {status}")
        print("\n# detail: rerun with --json")

    if args.check:
        # A DEAD GATEABLE SIGNAL IS A FAILURE, not a skip. The old predicate required `live`, so a
        # probe that had gone blind scored exactly like a probe that had found nothing — which is how
        # a pre-flatten glob stayed green on the merge bar. This is the generic fix: it catches the
        # next blind probe without anyone having to notice the next layout change.
        #
        # Except when a signal is EMPTY BY DECLARATION. `SHRINK_ONLY` ships empty on purpose, and a
        # rule with no exception here would red every fresh adopter on their first run. The exception
        # is enumerated in the project layer, never inferred.
        declared = set(getattr(ctx.proj, "DECLARED_EMPTY", ()) or ())
        ratchets = ratchet_findings(ctx.git, root, getattr(ctx.proj, "RATCHETS", ()), lookback)
        for r in ratchets:
            print(f"\ndrift-report: RATCHET WEAKENED — {r}", file=sys.stderr)
        over = [s for s in out if s["gateable"] and s["live"] and s["value"] > s["pin"]]
        dead = [s for s in out if s["gateable"] and not s["live"] and s["signal"] not in declared]
        for s in over:
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
