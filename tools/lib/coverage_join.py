"""coverage_join — the join factory: the both-ways coverage join and the shrink-only baseline's additions
(PLAY-dOrderedCharter-19 S9).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels INLINE,
byte-identical, in the memory-tree kit's `coverage_join.py`, which every consumer imports, and
`<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. It moved here from the
codebase-map kit's `map_lib.py` so that no core build imports an optional kit or reads its conf: the
block calls none of that kit's root or conf readers and raises none of its errors, and a working baseline that
does not parse propagates `tomllib.TOMLDecodeError` for its caller to name.
"""
from __future__ import annotations

import subprocess
import tomllib
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


def _read_git_text(root: Path, *args: str) -> str | None:
    """stdout of one `git -C root ...` call, or None when git is absent or the call fails."""
    try:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
    except (FileNotFoundError, OSError):
        return None
    return r.stdout if r.returncode == 0 else None


def derive_baseline_additions(root: Path, base: str, rel: str) -> tuple[dict[str, list[str]] | None, str]:
    """Per inventory id of the WORKING baseline at `root`/`rel` (a root-relative POSIX path), the keys
    `base`'s baseline did not carry — or None with the reason when there is no comparison to make. A
    baseline absent at `base`, or one that does not parse there, is NO comparison, never an empty one:
    read as empty, every key would read as added. An inventory id absent at `base` counts every key as
    added, so a new inventory cannot open with a baselined key. The note carries both sides' key counts,
    so a comparison over nothing is visible as such. A WORKING file that does not parse raises its
    `tomllib.TOMLDecodeError`, which the caller names in its own error."""
    path = Path(root) / rel
    text = _read_git_text(root, "show", f"{base}:./{rel}")  # `./`: relative to root, not the git top
    if text is None:
        return None, f"no {rel} at {base[:12]}"
    try:
        old = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        return None, f"{rel} does not parse at {base[:12]}: {exc}"
    new = tomllib.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    added = {inv: sorted(set(keys) - set(old.get(inv, ()))) for inv, keys in sorted(new.items())}
    note = (f"base carried {sum(len(v) for v in old.values())} key(s), "
            f"working carries {sum(len(v) for v in new.values())}")
    return {inv: keys for inv, keys in added.items() if keys}, note
# <<< coverage_join
