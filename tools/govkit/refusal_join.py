#!/usr/bin/env python3
"""The refusal join — every refusal branch in the deployer is reached by an arm that asserts it.

WHY THIS IS NOT `check-arms.py`. That engine's population is tracked `*.sh`, repo-wide, and the
deployer unit resolved deliberately that it stays shell-only: admitting Python either demands an arm
from every tracked `*.py` or needs a scoping rule, and either is a change to a governance carrier.
The guarantee moved to the test layer instead, and this is it.

WHAT A REFUSAL BRANCH IS, stated rather than assumed. A call site of either of the engine's two
refusal channels — the exception it raises to abort a verb, and the finding it appends to a report.
Its ANCHOR is `(module, enclosing function, ordinal within that function)`, computed from the same
walk that finds it, so the engine gains no argument and no decoration and an anchor survives the file
being edited above it. A line number would not.

THE POPULATION IS DISCOVERED, never named: the tracked Python under the deployer's own directory,
minus the harness files. TWO shrink-only pins, because they catch different things and only one of
them survives the refactor this build makes likely — a branch moved into a NEW module makes the file
set GROW and leaves the branch count unchanged, so both pins pass and neither grades it. What grades
that is the enumerated anchor SET, which is a membership assertion rather than a count.

REUSE, and the correction it carries. `tools/memory-tree/corpus_ids.py` already walks a parsed Python
source for a statement shape, records which lines were REACHED at runtime with a trace hook, and
joins the two — AST enumeration plus an execution-observed join, both liveness halves, already on the
bar. This extends that doctrine: the matcher changes from one statement kind to two call shapes, and
the join key becomes the anchor rather than the line number.
"""

from __future__ import annotations

import ast
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
HARNESS = {"selftest.py", "refusal_join.py", "matrix.py"}

# Shrink-only. Both are DERIVED on a first run and written here; a move in the weakening direction
# must name both values beside it, which is the convention this repo already enforces on every pin.
BRANCH_PIN = 210    # DERIVED on the first run over the real engine, not guessed. Shrink-only.
# 208 -> 210 (DEPL-dCarriedReceipt-6). Its TWO new refusals: `apply`'s silenced-leg finding,
# and the gov-side `selfcheck` arm that catches the same class one side over, before any
# adopter can receive the descriptor. Both armed — the first by AC5's fixture, the second by a
# scratch gov whose descriptor declares a leg engine no rule ships, staged RED deliberately
# because an arm that has only ever been seen passing is an assertion about nothing. 2/2 armed.
# 197 -> 208 (DEPL-dCarriedReceipt-5). Its ELEVEN new refusals, all inside `decline_findings`: a row
# with no `kit` or no `dest`; a `kit` outside the run's selection; an empty `why`; more than one
# evidence field; the two STALENESS arms (the dest arrived, and gov withdrew it); a `taken_as` the
# target does not track; a `consumed_into` it does not track; a `discharge` with no command; a
# discharge argv carrying an unresolved token; and a discharge probe that cannot LAUNCH. The spec
# estimated "roughly seven" and asked for the figure to be RE-DERIVED at landing rather than pinned
# to a literal, which is what this is. ALL ELEVEN are armed by a named selftest arm — six by an
# acceptance criterion and five by arms written for the branches alone, because a branch serving no
# criterion is exactly the one that otherwise ships unasserted. 11/11 armed.
# 190 -> 197 (DEPL-dCarriedReceipt-13). Its SEVEN new refusals, all on the `adopt` path: `--pin`
# with no `=` (in `parse_args`, so it is the one reachable without a target), `--target` resolving
# to the gov checkout, an existing receipt without `--re-adopt`, a target index differing from HEAD,
# a `--to` that does not resolve, a `--pin` revision that does not resolve, and a `--pin` naming a
# revision where gov holds no blob for that source. ALL SEVEN are reached by a named selftest arm —
# the first four and the `--pin` grammar directly under AC7 and AC8, the last two through the same
# `--pin` fixture. 7/7 armed, which is rarer here than the two entries below and is stated rather
# than assumed.
# 185 -> 190 (DEPL-dCarriedReceipt-14). Its five new refusals, and this unit also RELOCATES four:
# `cmd_check`'s existing check-arm failures moved into the extracted `run_kit_check`, which changes
# their anchors and not their count. The five that are new: a check arm that cannot LAUNCH (armed by
# the no-such-binary fixture), the post-write rollback's own finding (armed by the roll fixture, and
# seen RED with it removed), and the rollback's THREE restore failures — `git rm --cached`,
# `git update-index --cacheinfo` and `git checkout-index`. Those three are NOT armed and say so in
# their own branches: reaching one needs the TARGET's git to refuse a plumbing call this suite
# manufactures no way to provoke, which is exactly where `-11` left `land_through_index`'s
# post-`git mv` failure. 2/5 armed, stated rather than rounded up.
# 180 -> 185 (DEPL-dCarriedReceipt-11). Its five new refusals: the escaping destination, the
# occupied destination, the failed move, the ambiguous destination and the out-of-kit source.
# FOUR of the five are reached by a named selftest arm; the fifth -- `land_through_index` failing
# AFTER a successful `git mv` -- is declared unarmed in its own branch, because reaching it needs
# the TARGET's git to refuse a blob write and this suite manufactures no such mode.
# 161 -> 180 (DEPL-dCarriedReceipt-7, -8, -10). Re-derived at the landing of the receipt build
# rather than guessed: -7's S9 integrity assertion and its land-failure reports, -8's cmd_check
# gov_oid mismatch and its verdict-grid cell arm, and -10's three `forked` rule refusals plus
# its FORKED-header arm. Both values named, per this file's own convention.
# 141 -> 161 (TOOL-dUnstalledConvoy-26). The pin had fallen 19 behind the population before
# this build and 20 by the end of it, which is the state this file's own convention forbids:
# `a floor that trails the population stops catching the matcher going blind`. Raised to the
# live count so the next blind matcher reds. NOTE what this does NOT buy: the JOIN half has
# never executed, because nothing in the tree passes a reached-set, so `enumeration only` is
# the whole of what runs. That is TOOL-dUnstalledConvoy-36, not this raise.
                    # 135 -> 141 at the origin/main reconcile: upstream's one plan/apply classifier
                    # adds refusal branches of its own. Raised rather than left slack, because a
                    # floor that trails the population stops catching the matcher going blind.
FILE_PIN = 1        # 1 -> current: the deployer is one module today; a refactor may only grow this


def population(root: pathlib.Path) -> list[pathlib.Path]:
    out = subprocess.run(["git", "-C", str(root), "ls-files", "tools/govkit/*.py"],
                         capture_output=True, text=True)
    return [root / p for p in out.stdout.split("\n")
            if p.strip() and pathlib.PurePosixPath(p).name not in HARNESS]


def _is_refusal(node: ast.AST) -> str | None:
    """The two channels, by call SHAPE. Named here so the matcher is a stated rule, not a guess."""
    if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call):
        f = node.exc.func
        if isinstance(f, ast.Name) and f.id == "Refusal":
            return "raise"
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        f = node.value.func
        if isinstance(f, ast.Attribute) and f.attr == "fail":
            return "fail"
    return None


def enumerate_branches(root: pathlib.Path) -> list[dict]:
    found: list[dict] = []
    for path in population(root):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for fn in [n for n in ast.walk(tree)
                   if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
            k = 0
            for node in ast.walk(fn):
                kind = _is_refusal(node)
                if kind:
                    k += 1
                    found.append({"module": path.name, "function": fn.name, "ordinal": k,
                                  "kind": kind, "line": getattr(node, "lineno", 0)})
    return found


def main(argv: list[str]) -> int:
    root = HERE.parents[1]
    branches = enumerate_branches(root)
    files = population(root)
    problems: list[str] = []

    # Both pins, shrink-only, and each with its own scenario. Reporting only one is what let a
    # single-pin design pass comfortably while grading a shrinking fraction of the engine.
    if len(branches) < BRANCH_PIN:
        problems.append(f"refusal branches: {len(branches)} < pin {BRANCH_PIN} — the matcher found "
                        f"fewer than the seeded population, so either branches were removed (lower "
                        f"the pin and say so) or the matcher stopped matching")
    if len(files) < FILE_PIN:
        problems.append(f"scanned files: {len(files)} < pin {FILE_PIN} — a module stopped being "
                        f"scanned, which no branch count can see: a branch moved into a new module "
                        f"leaves the count unchanged while the file set grows")

    reached_path = pathlib.Path(argv[0]) if argv else None
    if reached_path and reached_path.is_file():
        reached = {tuple(x) for x in json.loads(reached_path.read_text(encoding="utf-8"))}
        for b in branches:
            key = (b["module"], b["function"], b["ordinal"])
            if key not in reached:
                problems.append(f"refusal branch {b['module']}:{b['function']}#{b['ordinal']} "
                                f"({b['kind']}, line {b['line']}) was reached by NO arm")

    for p in problems:
        print(f"refusal-join: {p}")
    print(f"refusal-join: {len(branches)} branch(es) across {len(files)} module(s)"
          + ("" if reached_path else " — enumeration only; pass a reached-set to join"))
    if problems:
        print(f"refusal-join: {len(problems)} problem(s)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
