"""coverage_join — the join factory and the compare base, as the gate-lint kit carries them
(TOOL-dWitnessedBar-13).

`compute_coverage` with its `Coverage` and `drop_touched_exemptions`, then
`resolve_compare_base`, the merge bar's compare base, with the remote ladder it calls: the three names
this kit's `legacy_ledger.py` reaches. This kit requires no other kit, so it carries them itself rather
than importing memory-tree's `coverage_join.py`, whose shape this file copies.

Each block below is INLINED byte-identically from the canonical copy its marker line names, gov's lib
dir, which ships nothing; `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# >>> coverage_join -- canonical copy: coverage_join.py in the gov lib dir (byte-identical; gated)
def drop_touched_exemptions(exempt, touched) -> frozenset[str]:
    """S4a — the touch-triggered backfill rule: shrink the affordance-exempt set by every feature
    a `map_diff` range TOUCHED (i.e. every attribution owner). Touching a feature's files drops
    its grace MECHANICALLY, so the next gate run demands its `## Reuse affordance` block with no
    human remembering (review #5/#32). ``touched`` is a map_diff attribution result (owner ->
    paths) or any iterable of feature names; ``foundation``/``UNMAPPED`` are never in the exempt
    list, so passing the whole attribution dict is safe.

    ponytail: the S4a rule is exactly this set difference — the machinery is attribute_paths."""
    return frozenset(exempt) - set(touched)


@dataclass
class Coverage:
    unclaimed: dict[str, list[str]]
    stale_claims: dict[str, list[str]]  # inventory -> ["owner: key", ...]
    stale_baseline: dict[str, list[str]]
    lazy_baseline: dict[str, list[str]]

    @property
    def clean(self) -> bool:
        return not (
            self.unclaimed or self.stale_claims or self.stale_baseline or self.lazy_baseline
        )


def compute_coverage(
    inventories: dict[str, list[str]],
    owners: dict[str, dict[str, tuple[str, ...]]],
    baseline: dict[str, tuple[str, ...]],
) -> Coverage:
    """The four both-direction asserts. 1: inventory - (claims|baseline) = 0 (coverage).
    2: claims - inventory = 0 (no stale claim — dossiers can't rot into fiction).
    3: baseline - inventory = 0 (stale-line guard). 4: baseline & claims = 0 (a claimed key's
    baseline line must be deleted — mechanical shrink pressure)."""
    unclaimed: dict[str, list[str]] = {}
    stale_claims: dict[str, list[str]] = {}
    stale_baseline: dict[str, list[str]] = {}
    lazy_baseline: dict[str, list[str]] = {}
    for inv_id, keys in inventories.items():
        inv = set(keys)
        claimed: set[str] = set()
        for owner, claims in sorted(owners.items()):
            owned = set(claims.get(inv_id, ()))
            claimed |= owned
            for key in sorted(owned - inv):
                stale_claims.setdefault(inv_id, []).append(f"{owner}: {key}")
        base = set(baseline.get(inv_id, ()))
        if missing := sorted(inv - claimed - base):
            unclaimed[inv_id] = missing
        if stale := sorted(base - inv):
            stale_baseline[inv_id] = stale
        if lazy := sorted(base & claimed):
            lazy_baseline[inv_id] = lazy
    return Coverage(unclaimed, stale_claims, stale_baseline, lazy_baseline)
# <<< coverage_join


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
