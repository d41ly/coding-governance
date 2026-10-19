# **Serves:** research PLAY-dClosedLoop-1
"""Print each progress row's review count and fold state, as the atlas derives them, and the pill the page draws.

Usage: python -X utf8 fold_state.py [<atlas.py>]   (from the worktree root; default: the build's generator)
Exit 1 when a row with reviews reads unfolded while one of its records holds a section whose tag ends in "fold".

Promoted from the session's scratchpad (`night/fold_state.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import importlib.util
import pathlib
import re
import sys

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                    "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py")
spec = importlib.util.spec_from_file_location("atlas", path)
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)
data = atlas.derive()
missed = 0
for p in data["progress"]:
    pill = ("reviewed x%d · folded" % len(p["reviews"]) if p["folded"]
            else "in review" if p["reviews"] else "review owed")
    marks = sorted({m for n in p["records"] for m in re.findall(r"^## \[([a-z0-9-]*fold)\]",
                                                              atlas.text(atlas.HERE / n), flags=re.M)})
    flag = ""
    if p["reviews"] and not p["folded"] and marks:
        flag = "  <- unfolded, yet it holds " + ", ".join("[%s]" % m for m in marks)
        missed += 1
    print("%-14s reviews %d  %-22s%s" % (p["layer"], len(p["reviews"]), pill, flag))
print("rows read unfolded despite a fold section: %d" % missed)
sys.exit(1 if missed else 0)
