# **Serves:** research PLAY-dClosedLoop-1
"""Join the gap register's keys against the chain: every gap owned exactly once, every chain build owning at least
one. Reads its inputs; writes nothing. Ranges like `gap-test-01 to gap-test-09` are expanded.

Usage (every input a path, so it runs in any tree):
  python gap-join.py <register> <architecture>
      the owners are the chain table's rows of the architecture record (v1's chain table, v2's `[chain]`), each row's
      last cell the gaps that build owns
  python gap-join.py --readmes <register> <architecture> <builds dir>
      the owners are the opened READMEs: for each build of the architecture's chain table, the gaps the problem slot
      of `<builds dir>/<build>/README.md` lists as owned, the slot found by the heading the build index generator's
      canon declares (`tools/memory-tree/gen_build_index.py`, read from the working directory); a README that is
      absent or holds no such slot owns nothing
Exit 0 when every register gap is owned by exactly one build, no build owns a gap the register lacks, and every build
owns at least one; 1 when any of those fails; 2 on a usage error.

Promoted from the session's scratchpad (`join_canonical.py`) for the whole-design audit's Stage 0. The README mode is
the owner's opening-read answer 5, "Add it to P0.7 (Recommended)" (the execution record's `[phase0-answers-2]`), and
the chain-table mode's verdicts are its scratch original's.
"""
import importlib.util
import re
import sys

sys.dont_write_bytecode = True

RANGE = r"gap-[a-z]+-\d\d to gap-[a-z]+-\d\d"
ROW = r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| (.+) \|$"
GENERATOR = "tools/memory-tree/gen_build_index.py"


def extract_owned(cell):
    """The gap keys a cell or slot lists, each range expanded."""
    owned = set()
    for a, b in re.findall(r"(gap-[a-z]+-\d\d) to (gap-[a-z]+-\d\d)", cell):
        stem, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
        owned |= {f"{stem}-{i:02d}" for i in range(lo, hi + 1)}
    owned |= set(re.findall(r"gap-[a-z]+-\d\d", re.sub(RANGE, "", cell)))
    return owned


def read_chain_owners(arch):
    """{build: owned gaps} from the architecture record's chain-table rows."""
    owners = {}
    for line in arch.splitlines():
        m = re.match(ROW, line)
        if m:
            owners[m.group(1)] = extract_owned(m.group(2))
    return owners


def extract_slot(readme, heading):
    """The slot under `heading`, its lines joined by spaces so a range wrapped across two lines reads whole; None
    when the README holds no such heading."""
    lines = readme.splitlines()
    if heading not in lines:
        return None
    body = []
    for ln in lines[lines.index(heading) + 1:]:
        if re.match(r"#{1,6} |<!--", ln):
            break
        body.append(ln.strip())
    return " ".join(body)


def read_readme_owners(builds, root):
    """({build: the gaps its opened README's problem slot lists}, [builds whose README is absent or holds no slot])."""
    spec = importlib.util.spec_from_file_location("gen_build_index", GENERATOR)
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    heading = gen.SLOT_CANON[0][0]
    owners, unread = {}, []
    for b in builds:
        try:
            with open(f"{root}/{b}/README.md", encoding="utf-8") as fh:
                slot = extract_slot(fh.read(), heading)
        except FileNotFoundError:
            slot = None
        if slot is None:
            unread.append(b)
        owners[b] = extract_owned(slot or "")
    return owners, unread


def check_join(keys, owners):
    """Print the join's four findings and return 1 when any is non-empty, else 0."""
    count = {k: [b for b, s in owners.items() if k in s] for k in keys}
    unowned = [k for k, bs in count.items() if not bs]
    multi = {k: bs for k, bs in count.items() if len(bs) > 1}
    phantom = sorted({g for s in owners.values() for g in s} - set(keys))
    empty = [b for b, s in owners.items() if not s]
    print("unowned:", unowned or "none")
    print("owned twice or more:", multi or "none")
    print("owned but not in the register:", phantom or "none")
    print("builds owning nothing:", empty or "none")
    return 1 if (unowned or multi or phantom or empty) else 0


def main(argv):
    if len(argv) == 4 and argv[0] == "--readmes":
        reg_path, arch_path, root = argv[1:]
    elif len(argv) == 2 and not argv[0].startswith("-"):
        (reg_path, arch_path), root = argv, None
    else:
        print("usage: gap-join.py <register> <architecture> | --readmes <register> <architecture> <builds dir>")
        return 2
    with open(reg_path, encoding="utf-8") as fh:
        keys = [m.group(1) for m in re.finditer(r"^\| (gap-[a-z]+-\d\d) \|", fh.read(), flags=re.M)]
    with open(arch_path, encoding="utf-8") as fh:
        owners = read_chain_owners(fh.read())
    if root is None:
        print(f"register keys {len(keys)} · chain builds {len(owners)}")
    else:
        owners, unread = read_readme_owners(list(owners), root)
        print(f"register keys {len(keys)} · chain builds {len(owners)} · READMEs under {root}, "
              f"{len(owners) - len(unread)} read, absent or without the problem slot: {unread or 'none'}")
    return check_join(keys, owners)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
