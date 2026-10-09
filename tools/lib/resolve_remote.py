"""resolve_remote — which remote "landed" is measured on, and its default branch (TOOL-dLadderedRemote-1).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. Its shell twin, with the same ladder and the same refusal text, is the
`resolve_remote_sh` block in `resolve-remote.sh` beside this file, and the same test's behaviour arm
runs both over one truth table.

The ladder is the lander's, from TOOL-aRepatriatedFork-8 S1. It used to live only in `push-main.sh`,
while every probe beside it read a literal `origin` — so a node whose remote is named after the
project refused, or graded a stale local branch, everywhere but the lander.

The block carries no single quote, so a caller may embed it inside a single-quoted program.
"""

# >>> remote_ladder_py -- canonical copy: resolve_remote.py in the gov lib dir (byte-identical; gated)
def resolve_remote(root):
    """-> (remote, branch, observed, refusal) for the repository at <root>. Fetches nothing.

    remote    GOV_REMOTE, else branch.<current>.remote unless it is ".", else the ONLY remote.
              Several remotes and none chosen, or a chosen name that is not a remote here, is a
              REFUSAL naming GOV_REMOTE. No remote at all is remote "" and NO refusal: the caller
              keeps its own no-remote fallback.
    observed  the branch refs/remotes/<remote>/HEAD names, or "". A caller whose GOV_DEFAULT_BRANCH
              only CROSS-CHECKS the observation reads this one.
    branch    GOV_DEFAULT_BRANCH, else observed, else "".
    A refusal empties the other three, so no caller can pick a remote the ladder refused.
    """
    import os
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    names = read("remote").split()
    listed = " ".join(names) or "none"
    # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous
    # (`heads/x`, `remotes/r/x`), and the prefix is stripped exactly instead.
    cur = read("symbolic-ref", "--quiet", "HEAD")
    cur = cur[len("refs/heads/"):] if cur.startswith("refs/heads/") else ""
    remote, how = os.environ.get("GOV_REMOTE") or "", "GOV_REMOTE"
    if not remote and cur:
        remote, how = read("config", "branch." + cur + ".remote"), "branch." + cur + ".remote"
        if remote == ".":
            remote = ""
    if not remote and len(names) == 1:
        remote = names[0]
    if not remote and len(names) > 1:
        where = "branch " + cur if cur else "a detached HEAD"
        return "", "", "", ("cannot choose a remote: GOV_REMOTE is unset, %s has no configured remote, "
                            "and this repository has %d remotes (%s). Name it: export GOV_REMOTE=<remote>."
                            % (where, len(names), listed))
    if remote and remote not in names:
        return "", "", "", ("%s names %s, which is no remote of this repository (%s). Name one that is: "
                            "export GOV_REMOTE=<remote>." % (how, remote, listed))
    observed = ""
    if remote:
        pre = "refs/remotes/" + remote + "/"
        head = read("symbolic-ref", "--quiet", pre + "HEAD")
        if head.startswith(pre) and len(head) > len(pre):
            observed = head[len(pre):]
    return remote, os.environ.get("GOV_DEFAULT_BRANCH") or observed, observed, ""
# <<< remote_ladder_py
