#!/usr/bin/env python3
"""Runbook parity — the prose runbook and the registry describe the same population.

THE KEY IS THE ENTRY ID, carried as an HTML-comment anchor in the runbook. Keying on prose headings
is fragile in the wrong direction: a heading edited for readability reds a gate for nothing, and the
gate then gets waived. The entry id is stable, machine-comparable, and already the identifier both
sides use.

BOTH DIRECTIONS, and a LIVENESS half that is not presence. An anchor whose section body is EMPTY
satisfies a presence check and teaches nobody anything — it is worse than an absent one, because it
reads as covered. So the body is asserted non-empty, and that is the half this gate would be
pointless without.

WHAT IT DOES NOT DO: grade the prose. It cannot tell a correct sentence from a wrong one, and saying
so here is cheaper than letting a reader assume otherwise. What it asserts is that every deployable
has a section and every section names a deployable — which is the claim the runbook's demotion to
narrative actually rests on.

ITS GATE LEG CARRIES NO GUARD, deliberately. A guard scopes a run and would have to name BOTH the
registry and the runbook, since either side moving changes the verdict; the defect it exists to
catch is a new registry entry landing with no section, which is exactly the diff a too-narrow guard
would skip. It reads two files and costs a third of a second, so there is nothing to scope away.
"""

from __future__ import annotations

import pathlib
import re
import sys

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    sys.stderr.write("runbook-parity: needs tomllib (CPython 3.11+)\n")
    raise SystemExit(2)

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RUNBOOK = ROOT / "WIRE-INTO-PROJECT.md"
ANCHOR = re.compile(r"<!--\s*govkit:entry\s+([a-z0-9-]+)\s*-->")

# THE SHRINK-ONLY RATCHET, and it is an EQUALITY rather than a ceiling. `readme-contract.txt` under
# the memory tree's project registry carries the same shape as `exempt-pin:` and its header states
# why: a pin left ABOVE the count after a drain is permanent slack, which is how a shrink-only list
# stops shrinking without anyone noticing. So a DRAIN reds here too, and the remedy it prints is to
# lower this number in the same commit as the section that drained it. Raising it is not a remedy
# this gate ever prints, and there is nothing that writes it — a rise is a hand edit, in a diff.
#
# WHY A PIN AT ALL. This checker was tracked, correct and on NO bar: run by hand it exited 1, and a
# green bar had therefore never meant anything about runbook anchors. Landing it unpinned would
# block every push until the sections are written, which is a different build; landing it pinned
# binds it TODAY and lets the number only fall. TOOL-aHonedRuleset-9 costed exactly these three
# options and named this one as the repo's established answer.
#
# MEASURED 2026-09-20 on node `c` at 316978ec, five runs, before the pin existed: `18 problem(s)`
# over `8 anchored section(s)`, `26 registry entr(y|ies)`, `0 exempt`. Every one of the eighteen is
# a registry entry with no anchored runbook section. Writing those sections is a separate build.
PROBLEM_PIN = 18


def main() -> int:
    reg = tomllib.loads((ROOT / "tools" / "govkit" / "registry.toml").read_text(encoding="utf-8"))
    entries = {e["id"] for e in reg.get("entry", [])}
    exempt = {x.get("id") for x in reg.get("runbook_exempt", []) if x.get("id")}
    for x in reg.get("runbook_exempt", []):
        if not str(x.get("why", "")).strip():
            print(f"runbook-parity: runbook_exempt '{x.get('id')}' carries an empty reason")
            return 1
        if x.get("id") not in entries:
            print(f"runbook-parity: runbook_exempt '{x.get('id')}' names no registry entry — a "
                  f"stale exemption silently narrows what this gate covers")
            return 1

    if not RUNBOOK.is_file():
        print(f"runbook-parity: {RUNBOOK.name} is absent")
        return 1
    text = RUNBOOK.read_text(encoding="utf-8")
    lines = text.split("\n")

    anchored: dict[str, int] = {}
    problems: list[str] = []
    for i, ln in enumerate(lines):
        m = ANCHOR.search(ln)
        if m:
            if m.group(1) in anchored:
                problems.append(f"entry '{m.group(1)}' is anchored twice in the runbook")
            anchored[m.group(1)] = i

    for eid in sorted(entries - set(anchored) - exempt):
        problems.append(f"registry entry '{eid}' has no anchored runbook section")
    for eid in sorted(set(anchored) - entries):
        problems.append(f"runbook anchors '{eid}', which is not a registry entry")

    # The liveness half: an anchor whose body is empty reads as covered and is not.
    for eid, i in sorted(anchored.items()):
        body = []
        for ln in lines[i + 1:]:
            if ANCHOR.search(ln):
                break
            body.append(ln.strip())
        if not any(body):
            problems.append(f"the runbook section anchored '{eid}' has an EMPTY body — an anchor "
                            f"with nothing under it satisfies a presence check and is worse than "
                            f"an absent one, because it reads as covered")

    for p in problems:
        print(f"runbook-parity: {p}")
    print(f"runbook-parity: {len(anchored)} anchored section(s) · {len(entries)} registry "
          f"entr(y|ies) · {len(exempt)} exempt")
    if not anchored:
        print("runbook-parity: NO anchors at all — this gate would pass vacuously; the runbook has "
              "not been anchored yet")
        return 1
    n = len(problems)
    print(f"runbook-parity: {n} problem(s) · pin {PROBLEM_PIN}")
    if n > PROBLEM_PIN:
        print(f"runbook-parity: {n - PROBLEM_PIN} MORE than the pin — the list is shrink-only and "
              f"this grew it. Anchor a runbook section for the entr(y|ies) named above, or, if the "
              f"entry genuinely warrants none, give it a `runbook_exempt` row with a reason.")
        return 1
    if n < PROBLEM_PIN:
        print(f"runbook-parity: {PROBLEM_PIN - n} FEWER than the pin, which is not a pass either. "
              f"The pin is an EQUALITY: one left above the count is permanent slack, and slack is "
              f"how a shrink-only list stops shrinking. Lower PROBLEM_PIN to {n} in this commit.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
