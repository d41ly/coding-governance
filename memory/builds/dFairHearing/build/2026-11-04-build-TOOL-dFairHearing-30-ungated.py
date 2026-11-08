# **Serves:** research TOOL-dFairHearing-30 TOOL-dFairHearing-15
# Spec 15 S5's `ungated` instrument (TOOL-dFairHearing-30): the `selected` arm's items as the clone's
# own checker prints them for the range, in their order, then every other class record of the clone
# that this repository's `check_ungated` (unit 23 S21) reads as ungated, by name.
# usage: python f30-ungated.py <orch repo> <clone> <base>..<head>   (stdout is the checklist)
import os, re, subprocess, sys

orch, clone, rng = sys.argv[1:4]
sys.path.insert(0, os.path.join(orch, "tools", "memory-tree"))
import gotchas as g  # noqa: E402 - this repository's reader, never the clone's

def check_tracked(path):
    return subprocess.run(["git", "-C", clone, "ls-files", "--error-unmatch", path],
                          capture_output=True).returncode == 0

checker = next((p for p in ("tools/memory-tree/gotchas.py", "tools/gotchas.py") if check_tracked(p)), None)
if checker is None:
    sys.exit("f30-ungated: no checker tracked in " + clone)
sel = subprocess.run([sys.executable, checker, "--for-diff", rng], cwd=clone, capture_output=True,
                     text=True, encoding="utf-8", timeout=120)
if sel.returncode != 0:
    sys.exit(f"f30-ungated: {checker} --for-diff {rng} exited {sel.returncode}: {sel.stderr.strip()}")
out = sel.stdout.replace("\r\n", "\n")
# The by-design block must stay last: the harness reads its entries up to the first non-item line,
# so an item appended after it would be read as a by-design entry.
cut = re.search(r"^# by design — \d+ invariant\(s\) this selection touches$", out, re.M)
head, tail = (out[:cut.start()], out[cut.start():]) if cut else (out, "")
chosen = set(re.findall(r"^- \[ \] (\S+) \(", head, re.M))
conf = g.load_conf(clone)
legs = g.load_leg_names(clone, conf)
files = set(p for p in subprocess.run(["git", "-C", clone, "ls-files"], capture_output=True, text=True,
                                      encoding="utf-8").stdout.split("\n") if p)
extra = [r for r in g.records(clone, conf["MEMORY_ROOT"])
         if r["kind"] == "class" and r["name"] not in chosen and g.check_ungated(r["text"], files, legs)]
items = "".join(f"\n- [ ] {r['name']} (ungated)\n      {r['description']}\n      {r['path']}\n" for r in extra)
sys.stdout.reconfigure(encoding="utf-8", newline="\n")
sys.stdout.write(head.rstrip("\n") + "\n" + items + ("\n" + tail if tail else ""))
print(f"f30-ungated: {len(chosen)} selected + {len(extra)} ungated, legs "
      f"{'blank' if legs is None else len(legs)}", file=sys.stderr)
