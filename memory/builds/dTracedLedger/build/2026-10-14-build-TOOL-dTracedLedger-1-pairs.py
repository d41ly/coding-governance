# **Serves:** research TOOL-dTracedLedger-1
"""Print, for each check-23 offender, the spec criterion's backticked tokens beside the ledger answer's.

Mirrors the two extractions in tools/memory-tree/check-memory-hygiene.sh check 23 (spec side: the
'## <n>. Acceptance criteria' section, label lines plus their continuation; ledger side: a journal
record's '**Evidences:** <id>' block, bullet-scoped tokens, first-line-scoped form). Read-only.
Usage: python c23_pairs.py <repo-root> <offender> [<offender> ...]   (offender = <unit>/<label>)
"""
import re
import subprocess
import sys

TOK = re.compile(r"`([^`]+)`")


def read_tracked(root, pat):
    out = subprocess.run(["git", "-C", root, "ls-files", pat], capture_output=True, text=True,
                         encoding="utf-8", check=True).stdout
    return [p for p in out.splitlines() if p]


def read(root, rel):
    with open(f"{root}/{rel}", encoding="utf-8", newline="") as fh:
        return [l.rstrip("\r\n") for l in fh]


def read_spec_side(root):
    res = {}
    lab_re = re.compile(r"^([ \t]*(-|\*)[ \t]*)?(\*\*)?AC[0-9]+[a-z]?(\*\*)?([^A-Za-z0-9]|$)")
    for rel in read_tracked(root, "memory/builds/*/spec/*.md"):
        uid, inac, cur = None, False, None
        for line in read(root, rel):
            if uid is None and re.match(r"^# [A-Z][A-Za-z0-9-]* ", line):
                uid = line[2:].split(" ")[0]
            if line.startswith("## "):
                inac = bool(re.match(r"^## [0-9]+[.] Acceptance criteria[ \t]*$", line))
                cur = None
                continue
            if not inac:
                continue
            if lab_re.match(line):
                lab = re.sub(r"^[ \t]*(-|\*)?[ \t]*(\*\*)?", "", line)
                lab = re.sub(r"[^A-Za-z0-9].*$", "", lab)
                cur = (uid, lab)
                res.setdefault(cur, {"file": rel, "text": [], "toks": []})
                res[cur]["text"].append(line)
                res[cur]["toks"] += TOK.findall(line)
            elif cur and line.strip():
                res[cur]["text"].append(line)
                res[cur]["toks"] += TOK.findall(line)
    return res


def read_ledger_side(root):
    res = {}
    pats = read_tracked(root, "memory/builds/*/build/*.md") + read_tracked(root, "memory/builds/*/reviews/*.md")
    for rel in pats:
        j, u, cur = False, "", None
        for line in read(root, rel):
            if line.startswith("**Serves:**"):
                j = bool(re.match(r"^\*\*Serves:\*\* *journal", line))
            if line.startswith("**Evidences:** "):
                cur = None
                u = line.split()[1] if j else ""
                continue
            if line.startswith("#"):
                cur, u = None, ""
                continue
            if u and re.match(r"^- *(\*\*)?AC[0-9]+", line):
                lab = re.sub(r"\*", "", line.split()[1])
                lab = re.sub(r"[^A-Za-z0-9].*$", "", lab)
                form = "obs" if TOK.search(line) else ("amd" if re.search(r"amended rev-[0-9]+", line) else "bad")
                cur = (u, lab)
                if cur not in res:  # first-wins, as the gate's map is
                    res[cur] = {"file": rel, "form": form, "text": [line], "toks": TOK.findall(line)}
                else:
                    cur = ("__dup__",) + cur
                continue
            if cur and cur[0] != "__dup__" and line.strip():
                res[cur]["text"].append(line)
                res[cur]["toks"] += TOK.findall(line)
    return res


def scan_join(st, lt):
    for a in st:
        for b in lt:
            if a.lower() in b.lower() or b.lower() in a.lower():
                return (a, b)
    return None


def main():
    root, offs = sys.argv[1], sys.argv[2:]
    sp, lg = read_spec_side(root), read_ledger_side(root)
    for o in offs:
        uid, lab = o.split("/")
        s, l = sp.get((uid, lab)), lg.get((uid, lab))
        print(f"=== {o}")
        if s:
            print(f"  spec   {s['file']}")
            print(f"  spec tokens   : {s['toks']}")
        else:
            print("  spec   (no criterion found)")
        if l:
            print(f"  ledger {l['file']}  form={l['form']}")
            print(f"  ledger tokens : {l['toks']}")
            print(f"  ledger line 1 : {l['text'][0][:220]}")
        else:
            print("  ledger (no answer found)")
        if s and l:
            print(f"  join          : {scan_join(s['toks'], l['toks'])}")


if __name__ == "__main__":
    main()
