# **Serves:** research PLAY-dClosedLoop-1
"""v2's clause ids (the owner's FQ-2): every clause of [chain] ends with its minted id, `cl-<minting-slug>-NNNN` in
backticks, never renumbered or reused; [clause-ids] states the grammar, the next free number and the retired ids.

Usage: python -X utf8 2026-10-19-build-PLAY-dClosedLoop-1-clause-ids.py [--mint] [--plant missing|duplicate|retired|next]
       (from the worktree root)
  (no flag)  check: exit 1 on a clause with no id or two, an id minted twice, a retired id in use, an id past the
             recorded next number, or no clause read; prints what it read
  --mint     appends an id to each clause that has none, numbered on from the highest in use, writes [clause-ids]
             (created on first use, before [planned]) with the next free number, then checks
  --plant    runs the check on an in-memory copy holding one planted defect, which must red
It reads only v2's [chain] rows, split on "; " as the clause scan splits them; it does not check that a spec carries a
clause (that is the carries join), nor that an id names the same clause it named before a rewrite.
"""
import pathlib
import re
import sys

V = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
SLUG = "dClosedLoop"
ID = re.compile(r"`(cl-d[A-Z]\w+-\d{4})`")
ROW = re.compile(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$")


def section(text, tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", text, flags=re.M | re.S)
    return m.group(0) if m else ""


def clauses(text):
    chain = section(text, "chain")
    out = []
    for ln in chain.split("\n"):
        m = ROW.match(ln)
        if m:
            out += [(m.group(1), c) for c in m.group(2).split("; ") if c.strip()]
    return out


def check(text):
    found, cl = [], clauses(text)
    if not cl:
        return ["read no clause"], cl
    seen = {}
    for build, c in cl:
        ids = ID.findall(c)
        if len(ids) != 1 or not c.rstrip().endswith(f"`{ids[0]}`" if ids else "\0"):
            found.append(f"{build}: a clause holds {len(ids)} ids or none at its end: {c[:70]}...")
            continue
        if ids[0] in seen:
            found.append(f"{ids[0]} minted twice: {seen[ids[0]]} and {build}")
        seen[ids[0]] = build
    sec = section(text, "clause-ids")
    retired = set(ID.findall(sec.split("Retired:", 1)[1])) if "Retired:" in sec else set()
    for r in sorted(retired & set(seen)):
        found.append(f"{r} is retired and in use on {seen[r]}")
    nxt = re.search(r"the next it mints is\s+`cl-" + SLUG + r"-(\d{4})`", sec)
    if sec and not nxt:
        found.append("[clause-ids] names no next free number")
    if nxt:
        top = max((int(i.rsplit("-", 1)[1]) for i in seen if i.startswith(f"cl-{SLUG}-")), default=0)
        if top >= int(nxt.group(1)):
            found.append(f"an id reaches {top}, past the recorded next number {int(nxt.group(1))}")
    if not sec:
        found.append("v2 holds no [clause-ids] section")
    return found, cl


def mint(text):
    lines = text.split("\n")
    top = max((int(i.rsplit("-", 1)[1]) for i in ID.findall(section(text, "chain"))), default=0)
    start = top + 1
    in_chain = False
    for k, ln in enumerate(lines):
        if ln.startswith("## [chain]"):
            in_chain = True
        elif ln.startswith("## [") and in_chain:
            break
        m = ROW.match(ln) if in_chain else None
        if not m:
            continue
        cells = ln.split(" | ")
        out = []
        for c in cells[3].split("; "):
            if not ID.search(c):
                top += 1
                c = f"{c} `cl-{SLUG}-{top:04d}`"
            out.append(c)
        cells[3] = "; ".join(out)
        lines[k] = " | ".join(cells)
    text = "\n".join(lines)
    minted = top - start + 1
    body = (f"Every clause of `[chain]` ends with its id, `cl-<minting-slug>-NNNN`, minted once by the session that adds the\n"
            "clause and never renumbered or reused (the charter's `[ids]` rule, the owner's FQ-2). A clause keeps its id\n"
            "through every amendment, its text's hash being its revision, and a spec that carries it pins both. A clause\n"
            "split across specs keeps its id, each carrier marking `part k/n`, a clause moved to another build keeps its id,\n"
            "and a retired clause's id is listed below and never minted again.\n"
            "`build/2026-10-19-build-PLAY-dClosedLoop-1-clause-ids.py` mints and checks them, and the next it mints is\n"
            f"`cl-{SLUG}-{top + 1:04d}`.\n\nRetired: none.\n")
    if section(text, "clause-ids"):
        text = re.sub(r"(the next it mints is\s+)`cl-" + SLUG + r"-\d{4}`", rf"\g<1>`cl-{SLUG}-{top + 1:04d}`",
                      text)
    else:
        anchor = "\n## [planned] "
        if text.count(anchor) != 1:
            sys.exit("v2's [planned] heading is not single")
        text = text.replace(anchor, "\n## [clause-ids] Clause ids\n\n" + body + anchor, 1)
    return text, minted


def plant(text, case):
    cl = [c for _, c in clauses(text)]
    if case == "missing":
        return text.replace(cl[0], re.sub(r" `cl-[^`]+`$", "", cl[0]), 1)
    if case == "duplicate":
        a, b = ID.findall(cl[0])[0], ID.findall(cl[1])[0]
        return text.replace(f"`{b}`", f"`{a}`", 1)
    if case == "retired":
        a = ID.findall(cl[0])[0]
        return text.replace("Retired: none.", f"Retired: `{a}`.", 1)
    if case == "next":
        return re.sub(r"(the next it mints is\s+)`cl-" + SLUG + r"-\d{4}`", rf"\g<1>`cl-{SLUG}-0001`", text)
    sys.exit(f"no plant {case}")


text = V.read_text(encoding="utf-8")
args = sys.argv[1:]
if args[:1] == ["--mint"]:
    text, n = mint(text)
    V.write_text(text, encoding="utf-8", newline="\n")
    print(f"minted {n} ids")
elif args[:1] == ["--plant"]:
    text = plant(text, args[1])
found, cl = check(text)
print(f"clause ids: read {len(cl)} clauses in {len({b for b, _ in cl})} builds; findings {len(found)}")
for f in found[:12]:
    print("  " + f)
if len(found) > 12:
    print(f"  ... and {len(found) - 12} more")
sys.exit(1 if found else 0)
