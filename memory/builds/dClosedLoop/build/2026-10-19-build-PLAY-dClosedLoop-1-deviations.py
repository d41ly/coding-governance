# **Serves:** research PLAY-dClosedLoop-1
"""The deviation population and its join: every departure from the frozen design, or from a spec once its code has
started, joined to a deviation record whose approver meets its risk (the owner's FQ-3, final-questions `[deviation]`,
dTrueNorth's clauses `cl-dClosedLoop-0004` and `cl-dClosedLoop-0005`). This is the bootstrap half, computed from
history here until dTrueNorth joins it at the commit and at the close.

A deviation record lives in the departing build's `build/` folder as `<date>-build-<unit>-deviation-<n>.md`, with:
  - **Departs from:** cl-dClosedLoop-NNNN@<hash8>, or <unit>@rev-N [<section tag>]
  - **Hand-off:** design-to-spec, design-revised, spec-revised, spec-to-code or code-to-record
  - **Before:** and **After:** the text departed from, and the text that replaced it
  - **Cause:** design defect, owner ruling, builder discovery, review finding or external
  - **Reason:** and **Evidence:**
  - **Risk:** editorial, additive, stricter, loosening or breaking
  - **Approver:** author, spec writer or owner, and where the approval is recorded
  - **Follow-through:** amends <clause-id>@<hash8>, supersedes <clause-id>@<hash8> by <clause-id>, new unit <id>,
    gap <id>, ask <id> or usage <key>
Approval by risk: an editorial change, its author or above; an additive or stricter one, the spec writer or above; a
loosening or a breaking one, the owner; and any change an owner's ruling causes, the owner.

The population, computed and never declared:
  - each clause of v2's `[chain]` whose hash moved since the baseline, or that was added or removed there, once v2's
    `[clause-ids]` records `Baseline:`; it joins a record departing from the clause at its baseline hash;
  - each chain build's spec revision after its unit's first attributed pass commit (a `Pass:` trailer naming the unit),
    a revision that changes only its `**Status:**` line excepted; it joins a record departing from `<unit>@rev-N`, the
    revision it changed;
  - each `AMENDED` acceptance line in a chain build's spec, which names its record as `(deviation <record>)`.
Divergence hand-backs and rescope rows join once the chain builds write them; none exists yet, and the summary says so.

Usage (from the worktree root):
  python deviations.py                              the population on the tree, joined to the records
  python deviations.py --fixture [--plant <case>]   a history built in memory, damaged one way: clause, pass-revision,
                                                    amended, pin, approver; and status, a status-only edit, green
Exit 0 when every member joins, 1 on an unjoined member or an approver below its risk, 2 when there is neither a
baseline nor a chain build's spec, so nothing is measured.

What it does not read: whether a record's reason is true, or its risk class honest, which the approver and the closing
review judge; and a departure in code that changes no spec, which Test's verdict and the closing review catch.
"""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

B = "memory/builds/dClosedLoop/build/"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
RANK = {"author": 0, "spec writer": 1, "owner": 2}
NEED = {"editorial": 0, "additive": 1, "stricter": 1, "loosening": 2, "breaking": 2}
FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$", re.M)
PLANTS = ("clause", "pass-revision", "amended", "pin", "approver", "status")

spec = importlib.util.spec_from_file_location("carries", B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py")
carries = importlib.util.module_from_spec(spec)
spec.loader.exec_module(carries)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8").stdout


def clauses_of(v2_text):
    chain = v2_text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    out = {}
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
        if m:
            for c in carries.split_clauses(m.group(2)):
                i = carries.CID.search(c)
                if i:
                    out[i.group(1)] = carries.clause_hash(c)
    return out


def record(path, text):
    f = dict(FIELD.findall(text))
    return {"id": Path(path).stem, "path": path, "departs": f.get("Departs from", ""), "risk": f.get("Risk", "").lower(),
            "cause": f.get("Cause", "").lower(), "approver": f.get("Approver", "").lower(),
            "follow": f.get("Follow-through", "")}


def approved(rec):
    who = next((r for r in sorted(RANK, key=len, reverse=True) if rec["approver"].startswith(r)), None)
    need = 2 if rec["cause"].startswith("owner ruling") else NEED.get(rec["risk"].split()[0] if rec["risk"] else "", None)
    if who is None or need is None:
        return f"approver '{rec['approver']}' or risk '{rec['risk']}' outside the grammar"
    return None if RANK[who] >= need else f"approved by the {who}, and a {rec['risk']} change needs the " + \
        {0: "author", 1: "spec writer", 2: "owner"}[need]


def join(members, records):
    """members: [(key, departs-from address or record id, what)]; each joins a record naming its address."""
    findings = []
    by_id = {r["id"]: r for r in records}
    for kind, address, what in members:
        if kind == "amended":
            rec = by_id.get(address)
        else:
            rec = next((r for r in records if r["departs"].split(" [")[0].strip("` ") == address), None)
        if rec is None:
            findings.append(f"{what}: joins no deviation record" + (f" departing from {address}" if kind != "amended" else
                                                                     f" (it names '{address or 'none'}')"))
            continue
        why = approved(rec)
        if why:
            findings.append(f"{what}: its record {rec['id']} is {why}")
    for r in records:
        if r["follow"].startswith(("amends", "supersedes")) and not re.search(r"cl-d[A-Z]\w+-\d{4}@[0-9a-f]{8}", r["follow"]):
            findings.append(f"{r['id']}: its follow-through names no clause at a hash")
    return findings


def population(baseline_v2, now_v2, revisions, amended):
    """revisions: [(unit, rev, after_pass, status_only)]; amended: [(unit, the record the line names)]."""
    members = []
    if baseline_v2 is not None:
        old, new = clauses_of(baseline_v2), clauses_of(now_v2)
        for cid in sorted(set(old) | set(new)):
            if cid not in new:
                members.append(("clause", f"{cid}@{old[cid]}", f"{cid} removed since the baseline"))
            elif cid not in old:
                members.append(("clause", f"{cid}@{new[cid]}", f"{cid} added since the baseline"))
            elif old[cid] != new[cid]:
                members.append(("clause", f"{cid}@{old[cid]}", f"{cid} moved from {old[cid]} to {new[cid]} since the baseline"))
    for unit, rev, after_pass, status_only in revisions:
        if after_pass and not status_only:
            members.append(("revision", f"{unit}@rev-{rev - 1}", f"{unit}'s spec revision rev-{rev}, after its first pass"))
    for unit, rec in amended:
        members.append(("amended", rec, f"an AMENDED acceptance line in {unit}'s spec"))
    return members


def real():
    v2 = Path(V2).read_text(encoding="utf-8")
    cid = v2.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0] if "\n## [clause-ids]" in v2 else ""
    m = re.search(r"^Baseline: `([0-9a-f]{7,40})`", cid, flags=re.M)
    baseline = git("show", f"{m.group(1)}:{V2}") if m else None
    chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    builds = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
    revisions, amended, specs = [], [], 0

    def descends(a, b):
        return a != b and subprocess.run(["git", "merge-base", "--is-ancestor", a, b]).returncode == 0

    for b in builds:
        for p in sorted(Path(f"memory/builds/{b}/spec").glob("*.md")):
            specs += 1
            text = p.read_text(encoding="utf-8")
            unit = re.search(r"\b([A-Z]+-" + b + r"-\d+)\b", text)
            unit = unit.group(1) if unit else p.stem
            passes = git("log", "--reverse", "--format=%H", f"--grep=^Pass: {unit}$").split()
            shas = git("log", "--reverse", "--format=%H", "--", p.as_posix()).split()
            first_pass = passes[0] if passes else None
            for n, sha in enumerate(shas, 1):
                after = bool(first_pass) and descends(first_pass, sha)
                prev = git("show", f"{shas[n - 2]}:{p.as_posix()}") if n > 1 else ""
                cur = git("show", f"{sha}:{p.as_posix()}")
                strip = lambda t: re.sub(r"(?m)^\*\*Status:\*\*.*$", "", t)   # noqa: E731
                revisions.append((unit, n, after and n > 1, strip(prev) == strip(cur)))
            for ln in text.split("\n"):
                if "AMENDED" in ln:
                    rec = re.search(r"\(deviation ([\w.-]+)\)", ln)
                    amended.append((unit, rec.group(1) if rec else ""))
    records = [record(p.as_posix(), p.read_text(encoding="utf-8"))
               for p in sorted(Path("memory/builds").glob("*/build/*-deviation-*.md"))]
    return baseline, v2, revisions, amended, records, specs


def fixture(plant):
    v2 = Path(V2).read_text(encoding="utf-8")
    ids = clauses_of(v2)
    first = sorted(ids)[6]
    m = re.search(r"(`" + re.escape(first) + r"`)", v2)
    now = v2[:m.start()] + "and a planted amendment " + v2[m.start():]
    old_hash, new_hash = ids[first], clauses_of(now)[first]
    records = [
        {"id": "fixture-deviation-1", "path": "fixture", "departs": f"{first}@{old_hash} [chain]", "risk": "stricter",
         "cause": "review finding", "approver": "owner, quoted in the round record", "follow": f"amends {first}@{old_hash}"},
        {"id": "fixture-deviation-2", "path": "fixture", "departs": "missing:PLAY-dTrueNorth-2@rev-2 [acceptance]",
         "risk": "additive", "cause": "builder discovery", "approver": "spec writer, re-audited at rev-3",
         "follow": "new unit missing:PLAY-dTrueNorth-7"},
        {"id": "fixture-deviation-3", "path": "fixture", "departs": "missing:PLAY-dTrueNorth-4@rev-1 [acceptance]",
         "risk": "editorial", "cause": "review finding", "approver": "author", "follow": "usage design.coverage"}]
    revisions = [("missing:PLAY-dTrueNorth-2", 1, False, False), ("missing:PLAY-dTrueNorth-2", 2, False, False),
                 ("missing:PLAY-dTrueNorth-2", 3, True, False), ("missing:PLAY-dTrueNorth-3", 2, True, True)]
    amended = [("missing:PLAY-dTrueNorth-4", "fixture-deviation-3")]
    if plant == "clause":
        records = records[1:]
    elif plant == "pass-revision":
        revisions.append(("missing:PLAY-dTrueNorth-5", 2, True, False))
    elif plant == "amended":
        amended.append(("missing:PLAY-dTrueNorth-5", ""))
    elif plant == "pin":
        records[1]["departs"] = "missing:PLAY-dTrueNorth-2@rev-1 [acceptance]"
    elif plant == "approver":
        records[0]["approver"] = "author"   # a stricter change needs the spec writer at least
    elif plant == "status":
        revisions.append(("missing:PLAY-dTrueNorth-6", 4, True, True))
    return v2, now, revisions, amended, records


def main(argv):
    plant = argv[argv.index("--plant") + 1] if "--plant" in argv else None
    if plant and plant not in PLANTS:
        sys.exit(f"deviations: no plant {plant}")
    if "--fixture" in argv:
        baseline, now, revisions, amended, records = fixture(plant)
        specs = len({r[0] for r in revisions})
    else:
        baseline, now, revisions, amended, records, specs = real()
    members = population(baseline, now, revisions, amended)
    findings = join(members, records)
    print(f"deviations: baseline {'read' if baseline is not None else 'none'}, chain-build specs {specs}, members "
          f"{len(members)}, records {len(records)} · findings {len(findings)}" + (" · fixture" if "--fixture" in argv else "")
          + (f" · plant {plant}" if plant else ""))
    print("  not read yet: divergence hand-backs and rescope rows, which no chain build has written")
    for f in findings:
        print(f"  {f}")
    if baseline is None and not specs:
        print("deviations: no baseline and no chain build's spec, so nothing is measured and the run is never green")
        return 2
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
