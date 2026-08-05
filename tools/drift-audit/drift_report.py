#!/usr/bin/env python3
"""drift_report.py — does this repo's own RECORD of its state still describe reality?

gov:kit drift-audit@1.0

    python drift-audit/drift_report.py            # human table, always exits 0
    python drift-audit/drift_report.py --json     # machine-readable, always exits 0
    python drift-audit/drift_report.py --check    # exit 1 if a GATEABLE signal is over its pin

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

WHAT IS ENGINE AND WHAT IS PROJECT. The five signal implementations are generic over any repo that
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
import pathlib
import re
import subprocess
import sys

# The kit never leaves bytecode in the adopter's worktree (matching memory-recall's query.py).
sys.dont_write_bytecode = True

KIT_DRIFT_AUDIT_VERSION = "1.0"

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


def signal_ledger(ctx) -> dict:
    rows, contradicting = 0, []
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
                continue
            refs = set(_REFERENCE_SHA.findall(line))
            work = [s for s in _SHA.findall(line) if s not in refs]
            landed = [s for s in work if ctx.git.is_commit(s) and ctx.git.is_ancestor(s)]
            if landed:
                contradicting.append({"file": rel, "line": i, "shas": landed[:4]})
    return {
        "signal": "ledger_rows_contradicting_git",
        "value": len(contradicting),
        "of": rows,
        "tolerance": 0,
        "gateable": True,
        # Live iff there are rows to judge at all. A ledger with none would report a meaningless 0,
        # which is exactly the collision_flags failure mode this kit exists to refuse.
        "live": rows > 0,
        "detail": contradicting,
    }


# --------------------------------------------------------------------------------------------
# Signal 2 — spec Status headers vs evidence the unit shipped
# --------------------------------------------------------------------------------------------

_STATUS = re.compile(r"^\*\*Status:\*\*\s*([A-Za-z]+)", re.M)
# The spec's OWN id, from its H1 (`# TOOL-cSightedPlumb-1 — title`). Keying on the SLUG instead was
# tried upstream and over-flagged 107/126: one shipped unit made all 14 siblings of its multi-spec
# build look stale, because every id of a build shares the slug. The seq is the discriminator.
_OWN_ID = re.compile(r"^#\s+([A-Z]+-[a-zA-Z]+-\d+)\b", re.M)
NON_TERMINAL = frozenset({"OPEN", "SPECCED", "BLOCKED", "INPROGRESS"})


def signal_spec_status(ctx) -> dict:
    suspect, checked, unkeyed = [], 0, 0
    for p in sorted(ctx.root.glob(f"{ctx.memory_root}/*/builds/*/spec/**/*.md")):
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
        hit = ctx.git.run("grep", "-l", "-F", own.group(1), "--", *ctx.product_globs)
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
    return {
        "signal": "handkept_inventories_disagreeing_with_source",
        "value": sum(0 if r["agrees"] else 1 for r in rows),
        "of": len(rows),
        "tolerance": 0,
        "gateable": True,
        "live": len(rows) > 0,
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


SIGNALS = [signal_ledger, signal_spec_status, signal_shrink_only, signal_handkept,
           signal_dangling_pointers]


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
        self.shrink_only = dict(proj.SHRINK_ONLY)
        self.handkept = list(proj.HANDKEPT)
        self.pins = dict(proj.PINS)
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
    except DriftError as exc:
        print(f"drift-report: {exc}", file=sys.stderr)
        return 2

    base_ref = args.base_ref or conf.get("DEFAULT_BRANCH") or "main"
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
            if not s["live"]:
                status = "DEAD PROBE — signal cannot move, ignore its value"
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
        bad = [s for s in out if s["gateable"] and s["live"] and s["value"] > s["pin"]]
        for s in bad:
            print(f"\ndrift-report: {s['signal']} = {s['value']} (pin {s['pin']}) — this list is shrink-only",
                  file=sys.stderr)
            for d in s["detail"][:10]:
                print(f"  {d}", file=sys.stderr)
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
