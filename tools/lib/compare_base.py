"""compare_base — the revision a shrink-only list is compared against (TOOL-dGroundRules-21 S7).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. The codebase map's baseline and the policy kit's two shrink-only lists read their
base through it, so a branch is graded on what it changed by one rule, never two.

The block calls `resolve_remote`, the remote ladder, which every consumer already carries inline
from `resolve_remote.py` beside this file; this module imports it from there. The block carries no
single quote, so a caller may embed it inside a single-quoted program.
"""
from resolve_remote import resolve_remote  # noqa: F401  (the block below calls it)


# >>> compare_base_py -- canonical copy: compare_base.py in the gov lib dir (byte-identical; gated)
def resolve_compare_base(root):
    """-> (sha or None, why): the revision a shrink-only list at <root> is compared against.

    The merge bar rule: the remote the inlined ladder resolves and the branch its HEAD names (`main`
    when none is named), its merge-base with HEAD where that is a PROPER ancestor of HEAD, else the
    remote tip. So a branch is graded on what IT changed, and a key the default branch deleted after
    the branch opened is not misread as one the branch added. Fetches nothing: no remote-tracking
    ref, no answer; a ladder refusal is no answer either, and says why. The OBSERVED branch, never
    GOV_DEFAULT_BRANCH: an environment value must not move the base a shrink-only assert grades.
    """
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    remote, _branch, observed, refusal = resolve_remote(root)
    if refusal:
        return None, refusal
    if not remote:
        return None, "no remote to compare against"
    branch = observed or "main"
    tip = read("rev-parse", "--verify", "-q", "refs/remotes/" + remote + "/" + branch + "^{commit}")
    if not tip:
        return None, "no %s/%s ref to compare against (never fetched)" % (remote, branch)
    head = read("rev-parse", "--verify", "-q", "HEAD")
    mb = read("merge-base", "HEAD", tip)
    if mb and mb != head:
        return mb, "merge-base of HEAD and %s/%s" % (remote, branch)
    return tip, "%s/%s tip" % (remote, branch)
# <<< compare_base_py
