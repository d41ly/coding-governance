# TOOL-dWitnessedBar-1 leg-tail 12 — remote literals (kit code names no remote) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** remote literals (kit code names no remote)
- **Hash:** da037ee5a471125a8a6db45cc020b930bb7d93f8
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg remote literals (kit code names no remote) | exit 1
tools/memory-tree/ratchet.py@8ee6db8a:789:    committed as the base on `main`, which `refs/remotes/origin/main` names."""
tools/memory-tree/ratchet.py@8ee6db8a:800:    run_git_in(top, "update-ref", "refs/remotes/origin/main", "HEAD")
tools/memory-tree/ratchet.py@8ee6db8a:996:    run_git_in(top, "update-ref", "-d", "refs/remotes/origin/main")
tools/memory-tree/ratchet.py@8ee6db8a:1147:    run_git_in(top, "update-ref", "refs/remotes/origin/main", "HEAD")
tools/run-gates/remote_verdict.py@f0aef65f:241:        rc, url = run_git(repo, "remote", "get-url", os.environ.get("GOV_REMOTE") or "origin")
tools/run-gates/verdict_backends.py@1dc655b3:549:    remote = os.environ.get("GOV_REMOTE") or "origin"
tools/run-gates/verdict_backends.py@1dc655b3:779:    this kit's readers under `tools/`; with `remote` pushed to the bare `top/remote.git`, origin/HEAD set."""
tools/run-gates/verdict_backends.py@1dc655b3:801:        run_fixture_git(work, "push", "-q", "--no-verify", "origin", "main")
tools/run-gates/verdict_backends.py@1dc655b3:802:        run_fixture_git(work, "remote", "set-head", "origin", "main")
tools/run-gates/verdict_backends.py@1dc655b3:1066:        run_fixture_git(work, "push", "-q", "--no-verify", "origin", "main")
tools/run-gates/verdict_backends.py@1dc655b3:1072:        why = (write_peer_tag if signed else write_unsigned_tag)(work, sha, rec, node_line, "origin")
tools/run-gates/verdict_backends.py@1dc655b3:1078:                     GOV_NODE="a", GOV_REMOTE="origin")
tools/run-gates/verdict_backends.py@1dc655b3:1101:                     ["verify-peer refused · user.signingkey"], GOV_NODE="b", GOV_REMOTE="origin")
tools/run-gates/verdict_backends.py@1dc655b3:1113:                      [said % "DEAD PROBE", f"git fetch origin {VERDICT_REF}{sha}"])
tools/run-gates/verdict_backends.py@1dc655b3:1138:        signed = run_fixture_git(work, "ls-remote", "origin", ref).split("\t")[0]
tools/run-gates/verdict_backends.py@1dc655b3:1145:        run_fixture_git(work, "push", "-q", "--force", "--no-verify", "origin", f"{edited}:{ref}")
tools/run-gates/verdict_backends.py@1dc655b3:1205:    run_fixture_git(work, "push", "-q", "--no-verify", "origin", f"{cand}:{CANDIDATE_REF}{cand}")
tools/run-gates/verdict_backends.py@1dc655b3:1214:    count = ("import subprocess, sys; p = subprocess.run(['git', 'ls-remote', 'origin', 'refs/gov/verdict/*'], "
tools/run-gates/verdict_backends.py@1dc655b3:1269:    run_fixture_git(work, "update-ref", "refs/remotes/origin/main", landed)
tools/run-gates/verdict_backends.py@1dc655b3:1270:    run_fixture_git(work, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
tools/run-gates/verdict_backends.py@1dc655b3:1296:        run_fixture_git(work, "update-ref", "refs/remotes/origin/main", run_fixture_git(work, "rev-parse", "HEAD"))
tools/run-gates/verdict_backends.py@1dc655b3:1385:    return run_verify_peer(args.remote or os.environ.get("GOV_REMOTE") or "origin")
tools/unattended/fix_keeps.py@196e3969:503:    run_fixture_git(repo, "push", "-q", "origin", "main")
remote-literals: FAILED — 23 line(s) in 292 file(s) name a remote by literal. Resolve it through the remote ladder (resolve_remote / resolve_remote_sh in the gov lib dir, inlined), never by name.
```
