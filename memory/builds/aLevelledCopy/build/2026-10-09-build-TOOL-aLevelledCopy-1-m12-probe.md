**Serves:** research TOOL-aLevelledCopy-1

# M12 probe — which normalization tells an eol-only working copy from drift

Run 2026-10-09 on node `a` (Git for Windows, system `core.autocrlf=true`), from the session
scratchpad, as `python m12_receipt.py <scratch dir>`. It builds throwaway repos and grades one file
with each candidate. Result rows, verbatim:

```text
case1 crlf-on-disk True status b''
case1 eol-only    A B C = ('GREEN', 'GREEN', 'GREEN')
case2 real edit   A B C = ('RED', 'RED', 'RED')
case3 no filter   A B C = ('RED', 'RED', 'GREEN')
case4 CRLF-box receipt on LF clone  A B = ('RED', 'RED')
```

Reading: C passes case 3, a CRLF copy no filter normalizes, which git would commit as CRLF, so C
loses. Case 4 reds under A and B alike (the tamper half fires because the raw bytes ARE the blob),
so it does not discriminate; it is a receipt-portability question and a non-goal. A and B survive;
A wins the tie-break as the seam `govkit cmd_check` already applies, at one spawn to B's two.

The instrument, verbatim:

```python
"""M12 probe for TOOL-aLevelledCopy-1: which normalization discriminates.

Candidates: A = clean-filter oid (git hash-object --path) vs row oid, tamper-guarded (govkit cmd_check's rule);
B = `git diff --quiet` then sha256 of the index blob vs row sha256; C = sha256 of bytes with CR stripped.
Cases: 1 eol-only (autocrlf=true, pin after checkout, CRLF copy) -> want GREEN;
2 real one-byte edit on that CRLF copy -> want RED;
3 CRLF copy with NO filter (autocrlf=false, no pin) -> want RED (git would commit CRLF).
"""
import hashlib, pathlib, subprocess, sys, tempfile

def git(t, *a, inp=None):
    return subprocess.run(["git", "-C", str(t), *a], input=inp, capture_output=True, check=False)

def blob_oid(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()

def make(base, name, autocrlf):
    t = base / name; t.mkdir()
    git(t, "init", "-q"); git(t, "config", "core.autocrlf", autocrlf)
    git(t, "config", "user.email", "x@x"); git(t, "config", "user.name", "x")
    body = b"line one\nline two\n"
    (t / "a.txt").write_bytes(body)
    git(t, "add", "a.txt"); git(t, "commit", "-qm", "c1")
    return t, body

def verdicts(t, body, path="a.txt"):
    want_sha, want_oid = hashlib.sha256(body).hexdigest(), blob_oid(body)
    raw = (t / path).read_bytes()
    if hashlib.sha256(raw).hexdigest() == want_sha:
        return "GREEN(raw)", "GREEN(raw)", "GREEN(raw)"
    cl = git(t, "hash-object", "--stdin-paths", inp=(path + "\n").encode()).stdout.decode().strip()
    A = "GREEN" if cl == want_oid and blob_oid(raw) != want_oid else "RED"
    quiet = git(t, "diff", "--quiet", "--", path).returncode == 0
    idx = git(t, "cat-file", "blob", ":" + path).stdout
    B = "GREEN" if quiet and hashlib.sha256(idx).hexdigest() == want_sha else "RED"
    C = "GREEN" if hashlib.sha256(raw.replace(b"\r", b"")).hexdigest() == want_sha else "RED"
    return A, B, C

with tempfile.TemporaryDirectory(dir=sys.argv[1]) as td:
    base = pathlib.Path(td)
    t, body = make(base, "case1", "true")
    (t / "a.txt").unlink(); git(t, "checkout", "--", "a.txt")          # autocrlf smudge -> CRLF copy
    (t / ".gitattributes").write_bytes(b"a.txt eol=lf\n")               # pin arrives after checkout
    git(t, "add", ".gitattributes"); git(t, "commit", "-qm", "pin")
    print("case1 crlf-on-disk", b"\r" in (t / "a.txt").read_bytes(), "status", git(t, "status", "--porcelain").stdout)
    print("case1 eol-only    A B C =", verdicts(t, body))
    (t / "a.txt").write_bytes((t / "a.txt").read_bytes().replace(b"one", b"onE"))
    print("case2 real edit   A B C =", verdicts(t, body))
    t, body = make(base, "case3", "false")
    (t / "a.txt").write_bytes(body.replace(b"\n", b"\r\n"))
    print("case3 no filter   A B C =", verdicts(t, body))

# case4: the receipt was written on a CRLF box (sha256 of CRLF worktree bytes, oid of the LF blob),
# and is graded on an LF clone. Want GREEN: the committed blob is gov's.
def verdicts_receipt(t, want_sha, want_oid, path="a.txt"):
    raw = (t / path).read_bytes()
    cl = git(t, "hash-object", "--stdin-paths", inp=(path + "\n").encode()).stdout.decode().strip()
    A = "GREEN" if hashlib.sha256(raw).hexdigest() == want_sha or (cl == want_oid and blob_oid(raw) != want_oid) else "RED"
    quiet = git(t, "diff", "--quiet", "--", path).returncode == 0
    idx = git(t, "cat-file", "blob", ":" + path).stdout
    B = "GREEN" if hashlib.sha256(raw).hexdigest() == want_sha or (quiet and hashlib.sha256(idx).hexdigest() == want_sha) else "RED"
    return A, B

with tempfile.TemporaryDirectory(dir=sys.argv[1]) as td:
    t, body = make(pathlib.Path(td), "case4", "false")
    print("case4 CRLF-box receipt on LF clone  A B =",
          verdicts_receipt(t, hashlib.sha256(body.replace(b"\n", b"\r\n")).hexdigest(), blob_oid(body)))
```
