"""coverage_join — the join factory: the both-ways coverage join (PLAY-dOrderedCharter-19 S9).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels INLINE,
byte-identical, in the memory-tree kit's `coverage_join.py`, which every consumer imports, and
`<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. It moved here from the
codebase-map kit's `map_lib.py` so that no core build imports an optional kit or reads its conf: the
block calls none of that kit's root or conf readers and raises none of its errors. The shrink-only
baseline's additions left the block when the map baseline became a ledger population: the memory-tree
kit's copy carries them as a thin adapter over the ledger factory, outside its block, since the
factory imports this block (TOOL-dWitnessedBar-16 §8 F8).
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
