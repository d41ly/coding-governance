#!/usr/bin/env python3
"""memory_retag.py — the upgrade step `memory-tree/legacy-anchors-retag` (TOOL-dTotalRecall-20 S5, S6).

    python <prefix>/govkit/steps/memory_retag.py plan|witness|down <target>
    python <prefix>/govkit/steps/memory_retag.py up <target> [--dry-run]

Its row is the memory-tree descriptor's `[[upgrade]]`. A record's untagged `##` heading is read under
an anchor derived from its text (TOOL-dTotalRecall-10, -19); the retag writes that anchor into the
record as the heading's authored tag, `## [section.<anchor>] <heading>` (TOOL-dTotalRecall-43 S6), the
grammar `record_extract.py`'s section extractor and `record_causes.py` read, and only where the adopter's own
committed `memory.legacy-anchors` is `retag`.

THE KEY. Each verb first reads the target's `memory.legacy-anchors` through govkit's
`read_policy_value`, the committed policy at its landed revision; a refused read exits 2 naming the
key and writes nothing. Under `derived` or `none` the verb writes nothing and exits 0.

THE POPULATION, under `retag`: every `.md` path an `S` or `U` row of the target's `gen_build_index.py
--print-bindings` names, the records `tree_lib.record_paths` selects, no spec among them. Each one's
untagged headings, outside fences and generated regions, and their anchors are what the playbook
kit's `gov_tag.py anchors <path>` prints, run with the target as its working directory; the derivation
is never copied here. Where the memory-tree or the playbook kit does not resolve, the verb exits 1
naming it, writing nothing.

THE VERBS, after `migrate_backlog.py`'s plan, dry-run and write. `plan` prints each heading to tag.
`up --dry-run` prints the plan and the conservation table and writes nothing; `up` writes the same
bytes through the before-image helpers, `write_before_image` then each file, so `down`
(`write_from_before_image`) restores every file byte-identical. `witness` exits 1 while an untagged
heading remains, so an adopter that sets `retag` after the walk applied the step gets it at its next
`update`.

THE CONSERVATION (S6), before the write and again after it: each rewritten record equals its earlier
bytes once every inserted `[section.<anchor>] ` is cut, every heading planned is then tagged, and no other
byte moves. A breach before the write exits 1 writing nothing; one after it exits 1 naming the file,
the before-image kept for `down`.

Exit 0 done, 1 refused (a breach, a kit that does not resolve, an edited file under `down`), 2 a usage
error or a refused policy read.
"""

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import govkit  # noqa: E402  the deployer beside this directory: its policy reader and before-image helpers

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from memory_journal_alias import run_index_mode  # noqa: E402  the steps' one reach of the index generator

STEP_ID = "memory-tree/legacy-anchors-retag"
KEY = "memory.legacy-anchors"
#: the namespace an authored section tag carries, `[section.<anchor>]` (TOOL-dTotalRecall-9 S1)
SECTION = "section."
VERBS = ("plan", "up", "down", "witness")


def read_retag_population(target: pathlib.Path) -> list[str]:
    """The `.md` records an `S` or `U` row of the target's `--print-bindings` names, in its order.
    RuntimeError where the run exits other than 0; LookupError where memory-tree does not resolve."""
    p = run_index_mode(target, "--print-bindings")
    if p.returncode != 0:
        said = (p.stdout + p.stderr).strip().splitlines()
        raise RuntimeError(f"gen_build_index.py --print-bindings exited {p.returncode}: {said[-1] if said else 'no output'}")
    rows = [ln.split("\t") for ln in p.stdout.splitlines()]
    return list(dict.fromkeys(r[1] for r in rows if r[0] in ("S", "U") and len(r) > 1 and r[1].endswith(".md")))


def read_heading_anchors(target: pathlib.Path, rel: str) -> list[tuple[int, str]]:
    """`(line, anchor)` per untagged heading of the record `rel`, as `gov_tag.py anchors` prints them.
    RuntimeError where the verb refuses; LookupError where the playbook kit does not resolve."""
    kit = govkit.resolve_kit_dir("playbook", "gov_tag.py", govkit.GOVKIT_DIR)
    p = subprocess.run([sys.executable, str(kit / "gov_tag.py"), "anchors", rel], cwd=str(target),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        raise RuntimeError(f"gov_tag.py anchors {rel} exited {p.returncode}: {p.stderr.strip()}")
    out = []
    for ln in p.stdout.splitlines():
        parts = ln.split()
        if parts[:2] == ["tags:", "anchor"] and len(parts) == 4 and parts[2].isdigit():
            out.append((int(parts[2]), parts[3]))
    return out


def derive_retag(text: str, tags: list[tuple[int, str]]) -> str:
    """`text` with `[section.<anchor>] ` inserted after the `## ` of each planned line, numbered as the anchors
    verb numbers them, through `str.splitlines`, every other character kept."""
    lines = text.splitlines(keepends=True)
    for n, anchor in tags:
        lines[n - 1] = lines[n - 1][:3] + f"[{SECTION}{anchor}] " + lines[n - 1][3:]
    return "".join(lines)


def check_conservation(before: str, after: str, tags: list[tuple[int, str]]) -> list[str]:
    """S6 over one record: each planned line of `after` holds its `## [section.<anchor>] ` at the heading's
    start, and cutting every inserted tag gives `before` back, no other character moved. One line per
    breach."""
    lines = after.splitlines(keepends=True)
    bad = []
    for n, anchor in tags:
        line = lines[n - 1] if n - 1 < len(lines) else ""
        if not line.startswith(f"## [{SECTION}{anchor}] "):
            bad.append(f"line {n} does not carry [{SECTION}{anchor}]")
        else:
            lines[n - 1] = line[:3] + line[3 + len(SECTION) + len(anchor) + 3:]
    if "".join(lines) != before:
        bad.append("its bytes with every inserted tag cut differ from its earlier bytes")
    return bad


def read_retag_plan(target: pathlib.Path) -> dict[str, tuple[bytes, str, str, list[tuple[int, str]]]]:
    """`{rel: (bytes on disk, text, retagged text, tags)}` for each record of the population holding an
    untagged heading."""
    plan = {}
    for rel in read_retag_population(target):
        tags = read_heading_anchors(target, rel)
        if not tags:
            continue
        data = (target / rel).read_bytes()
        text = data.decode("utf-8")
        plan[rel] = (data, text, derive_retag(text, tags), tags)
    return plan


def print_plan(plan: dict) -> None:
    """One line per heading to tag, its record, line and the tagged heading, then the count."""
    for rel, (_data, text, _after, tags) in plan.items():
        lines = text.splitlines()
        for n, anchor in tags:
            print(f"{STEP_ID}: plan · {rel}:{n} · ## [{SECTION}{anchor}] {lines[n - 1][3:].strip()}")
    print(f"{STEP_ID}: plan · {sum(len(v[3]) for v in plan.values())} heading(s) in {len(plan)} record(s)")


def check_retag_conservation(plan: dict, after_texts: dict) -> list[str]:
    """The breaches `check_conservation` finds in each record's `after_texts`, its conservation table
    printed on the way, one row per record."""
    breaches = []
    print(f"{STEP_ID}: conservation · record · tags inserted · bytes before -> after · cut equals before")
    for rel, (data, text, _after, tags) in plan.items():
        bad = check_conservation(text, after_texts[rel], tags)
        breaches += [f"{rel}: {b}" for b in bad]
        print(f"{STEP_ID}: conservation · {rel} · {len(tags)} · {len(data)} -> "
              f"{len(after_texts[rel].encode('utf-8'))} · {'no' if bad else 'yes'}")
    return breaches


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv[2:]
    if len(argv) < 2 or argv[0] not in VERBS or argv[2:] not in ([], ["--dry-run"]) or dry and argv[0] != "up":
        print("usage: memory_retag.py plan|witness|down <target> | up <target> [--dry-run]", file=sys.stderr)
        return 2
    verb, target = argv[0], pathlib.Path(argv[1]).resolve()
    try:
        value = govkit.read_policy_value("memory.legacy-anchors", target)[0]
    except (govkit.Refusal, LookupError) as exc:
        print(f"{STEP_ID}: {KEY} could not be read, so nothing is written: {exc}", file=sys.stderr)
        return 2
    if value != "retag":
        print(f"{STEP_ID}: {verb} · {KEY} is {value}, so no record is retagged and nothing is written")
        return 0
    try:
        if verb == "down":
            restored = govkit.upgrade_steps.write_from_before_image(target, STEP_ID)
            print(f"{STEP_ID}: down · {len(restored)} record(s) restored byte-identical")
            return 0
        plan = read_retag_plan(target)
    except LookupError as exc:
        print(f"{STEP_ID}: a kit the retag reads does not resolve, so nothing is written: {exc}", file=sys.stderr)
        return 1
    except (RuntimeError, govkit.Refusal, OSError, UnicodeDecodeError) as exc:
        print(f"{STEP_ID}: {verb} refused, nothing written: {exc}", file=sys.stderr)
        return 1
    if verb == "witness":
        left = sum(len(v[3]) for v in plan.values())
        print(f"{STEP_ID}: witness · {left} untagged heading(s) left in {len(plan)} record(s)")
        return 1 if left else 0
    print_plan(plan)
    if verb == "plan":
        return 0
    breaches = check_retag_conservation(plan, {rel: v[2] for rel, v in plan.items()})
    if breaches:
        for b in breaches:
            print(f"{STEP_ID}: conservation breach · {b}", file=sys.stderr)
        return 1
    if dry:
        print(f"{STEP_ID}: up --dry-run · nothing written")
        return 0
    if not plan:
        print(f"{STEP_ID}: up · no untagged heading, nothing written")
        return 0

    def derive_after(before):
        # A re-run over a killed up: a record already written holds no untagged heading and is its own after.
        rels = plan if before is None else before
        return {rel: plan[rel][2].encode("utf-8") if rel in plan else (target / rel).read_bytes() for rel in rels}

    try:
        after = govkit.upgrade_steps.write_before_image(target, STEP_ID, derive_after)
        for rel, data in after.items():
            (target / rel).write_bytes(data)
        again = {rel: (target / rel).read_bytes().decode("utf-8") for rel in plan}
        breaches = check_retag_conservation(plan, again)
        breaches += [f"{rel}: {n} heading(s) still untagged" for rel in plan
                     for n in [len(read_heading_anchors(target, rel))] if n]
    except (RuntimeError, govkit.Refusal, OSError, UnicodeDecodeError, LookupError) as exc:
        print(f"{STEP_ID}: up refused: {exc}", file=sys.stderr)
        return 1
    if breaches:
        for b in breaches:
            print(f"{STEP_ID}: conservation breach after the write · {b}; run down to restore", file=sys.stderr)
        return 1
    print(f"{STEP_ID}: up · {len(after)} record(s) retagged")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
