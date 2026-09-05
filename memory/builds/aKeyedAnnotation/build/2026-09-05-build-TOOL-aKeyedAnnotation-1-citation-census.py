#!/usr/bin/env python3
# **Serves:** research TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4
#
# The census behind this build's design pass. It exists as a SCRIPT rather than as a table of
# numbers in the record, because a count typed beside the population it counts is wrong on the next
# commit and nobody notices. Re-run it; do not read a figure out of the prose.
#
#     python memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py
#
# WHAT IT ANSWERS, and why each half is here:
#   A. code -> memory. How many ids does product source cite, and how many of those resolve to an
#      anchored record? This is the population `tools/memory-tree/corpus_ids.py` check 14 has never
#      graded: its walk builds `corpus` as tracked files under MEMORY_ROOT, so a source citation is
#      outside its universe by construction and `orphan ids: 0` is true of memory and silent about
#      code.
#   B. memory -> code. How many anchored ids, and how many spec-defined UNITS, leave a trace in
#      product source at all? This is the reachability the reverse direction needs, and it is also
#      the live population of the drift-audit spec-status oracle at `drift_report.py:466`.
#   C. The false-positive class. Test files carry synthetic fixture ids (`zFixture`, `aFoo`, `tOne`)
#      that look exactly like real citations. Any source-side orphan gate that does not split them
#      out reds on fixtures forever, which is how a gate gets waived instead of drained.
#
# LIVENESS: every population is printed with its size. A zero that is not asserted to be a real zero
# is indistinguishable from a walk that matched nothing, which is the failure this repo has shipped
# twice (`drift_report.py:447` records one of them).
import glob
import os
import re
import subprocess
import sys

ROOT = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
).stdout.strip()
sys.path.insert(0, os.path.join(ROOT, "tools", "memory-tree"))
import corpus_ids as C  # noqa: E402

CONF = C.load_conf(ROOT)
MEM = CONF["MEMORY_ROOT"] + "/"
E = C.grammar(ROOT)
# The extensions a citation can live in. `.md` is included for the source side because a kit README
# is product documentation shipped to adopters, not a memory record.
SRC_EXT = (".py", ".sh", ".js", ".json", ".toml", ".txt", ".conf", ".md")


def is_test(p: str) -> bool:
    """A file whose ids are FIXTURES, not citations. Deliberately generous: a gate that mistakes a
    fixture for a dangling pointer is a gate nobody can drain, so the split errs toward test."""
    return (
        ".test." in p
        or "selftest" in p
        or "/fixtures/" in p
        or os.path.basename(p).startswith("test_")
    )


def main() -> int:
    walk = C.walk(ROOT, CONF)
    defined = set(walk["defs"])

    tracked = [p for p in C.run("git", "ls-files", cwd=ROOT).split("\n") if p]
    source = [p for p in tracked if not p.startswith(MEM) and p.endswith(SRC_EXT)]
    prod_files = [p for p in source if not is_test(p)]
    test_files = [p for p in source if is_test(p)]

    def cites(paths):
        by_id, by_file = {}, {}
        for p in paths:
            try:
                text = C.read(os.path.join(ROOT, p))
            except OSError:
                continue
            n = 0
            for m in E.ID_RE.finditer(text):
                by_id.setdefault(m.group(0), set()).add(p)
                n += 1
            if n:
                by_file[p] = n
        return by_id, by_file

    prod_ids, prod_by_file = cites(prod_files)
    test_ids, test_by_file = cites(test_files)

    spec_h1 = re.compile(r"^#\s+[`*]*(" + E.ID + r")\b", re.M)
    units = set()
    for p in glob.glob(os.path.join(ROOT, MEM, "builds", "*", "spec", "**", "*.md"), recursive=True):
        with open(p, encoding="utf-8", errors="replace") as fh:
            m = spec_h1.search(fh.read())
        if m:
            units.add(m.group(1))

    if not defined or not source or not units:
        print("DEAD PROBE — an input population is empty; every figure below would be a false zero")
        print(f"  anchored ids {len(defined)} · source files {len(source)} · spec units {len(units)}")
        return 1

    print("== populations (a zero here means the walk found nothing, not that nothing is wrong) ==")
    print(f"  ids anchored in {CONF['MEMORY_ROOT']}/            : {len(defined)}")
    print(f"  spec-defined units (H1)          : {len(units)}")
    print(f"  tracked source files             : {len(source)}  ({len(prod_files)} product, {len(test_files)} test)")
    print()
    print("== A. code -> memory ==")
    print(f"  product files carrying a citation: {len(prod_by_file)}")
    print(f"  citations in product source      : {sum(prod_by_file.values())}")
    print(f"  distinct ids cited (product)     : {len(prod_ids)}")
    dangling = sorted(set(prod_ids) - defined)
    print(f"  of those, UNRESOLVABLE           : {len(dangling)}")
    for i in dangling:
        print(f"      {i:32s} {', '.join(sorted(prod_ids[i]))}")
    print()
    print("== B. memory -> code ==")
    src_all = set(prod_ids)
    print(f"  anchored ids cited from source   : {len(defined & src_all)} of {len(defined)}"
          f"  ({100 * len(defined & src_all) / len(defined):.1f}%)")
    print(f"  spec UNITS cited from source     : {len(units & src_all)} of {len(units)}"
          f"  ({100 * len(units & src_all) / len(units):.1f}%)")
    print()
    print("== C. the fixture class (why a naive source-side orphan gate cannot be drained) ==")
    print(f"  distinct ids cited in test files : {len(test_ids)}")
    print(f"  of those, UNRESOLVABLE           : {len(set(test_ids) - defined)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
