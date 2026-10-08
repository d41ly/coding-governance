# Cross-site probe — the ladder at every consumer without an arm of its own

**Serves:** journal TOOL-dLadderedRemote-2

Node `d`, 2026-10-08, at `75a55242c`. The instrument is the program below, run as
`python site_probe.py <repo> <git-bash path>` from the repo root. It imports or extracts each
consumer from the working tree and runs it over three fixtures. Python consumers are imported. Shell
consumers are either run whole, as with both hooks, or have their own lines extracted by anchor and
run under Git-Bash, as with unattended's two functions and check-verdict-epoch's base block. Bare
`bash` from Python resolves to the WSL shim on this node, so the shell path is passed in.

The fixtures. `one` has `incms` as its ONLY remote; `incms/HEAD` names `incms/trunk`, and a local
`main` also exists. A site falling back to the local default therefore reads `main`, and one that
resolved the remote reads `trunk`. `two` adds an `origin` remote, the branch under test has no
upstream, and `GOV_REMOTE` is unset. `pick` is `two` with `GOV_REMOTE=incms`. Every ambient
`GOV_REMOTE` and `GOV_DEFAULT_BRANCH` is cleared first.

## Rows

| Site | one | two | pick |
|---|---|---|---|
| `render_playbook.derive_default_branch` | `trunk` | `main`, refusal on stderr | `trunk` |
| `govkit.resolve_measurer_currency` | unverified, `incms did not answer` | unverified, the refusal | unverified, `incms did not answer` |
| `migrate_backlog.resolve_default_tip` | `trunk` and its sha | `Refusal` naming `GOV_REMOTE` | `trunk` and its sha |
| `row_grammar.derive_relation_base` | merge-base with `incms/trunk` | `Problem` naming `GOV_REMOTE` | merge-base with `incms/trunk` |
| runlog `read_refs` `origin_head` | `refs/remotes/incms/trunk` | None, so local fallback | `refs/remotes/incms/trunk` |
| unattended `default_branch` | `trunk` | rc 1, the refusal on stderr | `trunk` |
| unattended `derive_liveness` ref | `refs/remotes/incms/trunk` | `unresolved` | `refs/remotes/incms/trunk` |
| `check-verdict-epoch.sh` base | merge-base with `incms/trunk` | rc 1 `FAILED` naming `GOV_REMOTE` | merge-base with `incms/trunk` |
| `.githooks/pre-commit` branch guard | default `trunk` | default `main` | default `trunk` |
| `.githooks/straggler-guard.sh` init | ready, ref `refs/remotes/incms/HEAD` | announced, NOTHING checked | ready, ref `refs/remotes/incms/HEAD` |

Every row reads `incms`, its refusal, or the fallback spec 2's site table declares for it. None reads
`origin`. The `two` column's local readings are the declared fallbacks of the render, the run log
and the pre-commit guard.

`govkit.cmd_epoch` refuses in a bare fixture before it reaches its base, because it needs a govkit
tool root. It was probed against this repository instead. `GOV_REMOTE=nosuch python
tools/govkit/govkit.py epoch` printed `epoch: FAILED · no base to compare against · GOV_REMOTE names
nosuch, which is no remote of this repository (origin).` With no environment set, it graded every
kit against the merge-base with `origin/main`.

## The instrument

```python
"""site_probe.py <repo> <bash> — TOOL-dLadderedRemote-2 AC5: run every ladder consumer that has no arm
of its own over three fixtures, and print one row per (site, fixture)."""
import contextlib
import importlib.util
import io
import os
import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(sys.argv[1]).resolve()
for k in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH", "GOVKIT_NO_REMOTE_PROBE"):
    os.environ.pop(k, None)
BASH = sys.argv[2]


def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout.strip()


def load(name, rel):
    sys.path.insert(0, str((REPO / rel).parent))
    spec = importlib.util.spec_from_file_location(name, REPO / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def build(base):
    r = base / "one"
    r.mkdir()
    git(r, "init", "-q", "-b", "main")
    git(r, "config", "user.email", "t@e")
    git(r, "config", "user.name", "t")
    (r / ".memory-tree.conf").write_text('BACKLOG_MODE="builds"\n', encoding="utf-8")
    git(r, "add", "-A")
    git(r, "commit", "-qm", "seed")
    git(r, "checkout", "-q", "-b", "feature")
    (r / "f.txt").write_text("x\n", encoding="utf-8")
    git(r, "add", "-A")
    git(r, "commit", "-qm", "feature")
    git(r, "remote", "add", "incms", "../incms.git")
    git(r, "update-ref", "refs/remotes/incms/trunk", "main")
    git(r, "symbolic-ref", "refs/remotes/incms/HEAD", "refs/remotes/incms/trunk")
    return r


def capture(fn):
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            val = fn()
    except Exception as exc:  # a refusal is an answer here
        val = f"{type(exc).__name__}: {exc}"
    return val, (out.getvalue() + err.getvalue()).strip().replace("\n", " | ")


def sh(cwd, script):
    f = pathlib.Path(cwd).parent / "probe.sh"
    f.write_text(script + "\n", encoding="utf-8", newline="\n")
    p = subprocess.run([BASH, str(f)], cwd=str(cwd), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return f"rc={p.returncode} {(p.stdout + p.stderr).strip()}".replace("\n", " | ")


def extract(rel, start, stop):
    lines = (REPO / rel).read_text(encoding="utf-8").split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith(start))
    j = next(k for k in range(i + 1, len(lines)) if lines[k].startswith(stop))
    return "\n".join(lines[i:j + 1])


rp = load("render_playbook", "tools/playbook/render_playbook.py")
gk = load("govkit", "tools/govkit/govkit.py")
mb = load("migrate_backlog", "tools/memory-tree/migrate_backlog.py")
rg = load("row_grammar", "tools/memory-tree/row_grammar.py")
rl = load("model", "tools/runlog/model.py")
LADDER = extract("tools/lib/resolve-remote.sh", "# >>> remote_ladder_sh", "# <<< remote_ladder_sh")
DEFBR = extract("tools/unattended/unattended.sh", "default_branch() {", "}")
LIVE = extract("tools/unattended/unattended.sh", "  dref=unresolved", "  fi")
EPOCH = extract("tools/memory-tree/check-verdict-epoch.sh", 'if [ -z "$BASE" ]; then', "fi")

with tempfile.TemporaryDirectory() as d:
    r = build(pathlib.Path(d))
    trunk = git(r, "rev-parse", "main")
    for label in ("one", "two", "pick"):
        if label == "two":
            git(r, "remote", "add", "origin", "../origin.git")
            git(r, "update-ref", "refs/remotes/origin/main", "main")
        if label == "pick":
            os.environ["GOV_REMOTE"] = "incms"
        rows = [
            ("render_playbook.derive_default_branch", capture(lambda: rp.derive_default_branch(r, {}))),
            ("govkit.resolve_measurer_currency", capture(lambda: gk.resolve_measurer_currency(r, trunk))),
            ("migrate_backlog.resolve_default_tip", capture(lambda: mb.resolve_default_tip(str(r)))),
            ("row_grammar.derive_relation_base", capture(lambda: rg.derive_relation_base(str(r)) == trunk and "merge-base with incms/trunk")),
            ("runlog model.read_refs origin_head", capture(lambda: rl.read_refs(r)["origin_head"])),
        ]
        if hasattr(gk.resolve_measurer_currency, "_memo"):
            gk.resolve_measurer_currency._memo.clear()
        for name, (val, noise) in rows:
            print(f"{label}\t{name}\t{val}\t{noise[:300]}")
        print(f"{label}\tunattended default_branch\t" + sh(r, LADDER + "\nGIT() { git \"$@\"; }; AREF=\"\"\n" + DEFBR + "\ndefault_branch"))
        print(f"{label}\tunattended derive_liveness dref\t" + sh(r, LADDER + "\nGIT() { git \"$@\"; }; AREF=\"\"\n" + DEFBR + "\n" + LIVE + "\necho \"$dref\""))
        print(f"{label}\tcheck-verdict-epoch base\t" + sh(r, LADDER + "\nBASE=\"\"\n" + EPOCH + "\n[ \"$BASE\" = \"" + trunk + "\" ] && echo \"BASE is the merge-base with incms/trunk\" || echo \"BASE=$BASE\""))
        print(f"{label}\tpre-commit branch guard\t" + sh(r, f"bash '{(REPO / '.githooks/pre-commit').as_posix()}' 2>&1 | grep -m1 'refusing a commit in the primary tree'"))
        print(f"{label}\tstraggler-guard init\t" + sh(r, f". '{(REPO / '.githooks/straggler-guard.sh').as_posix()}'; init_straggler_guard; echo \"ready=$STRAGGLER_READY ref=$STRAGGLER_DEF_REF\""))
```
