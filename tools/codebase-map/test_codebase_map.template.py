"""The codebase-map coverage + freshness gate (codebase-map kit).

Copied from codebase-map/test_codebase_map.template.py at adoption into the directory named by
`.codebase-map.conf` GATE_FILE — it must live where the project's EXISTING test suite collects
it (zero CI changes: a test file is its own deployment). Also runnable standalone in projects
without a test framework: `python <this file>`.

Remedies when this gate fails on your change:
- claim the new key in the owning `<MAP_ROOT>/features/<feature>.md` (create it from any
  existing dossier — headings are pinned, prose is free), or
- claim it in `<MAP_ROOT>/FOUNDATION.md` if it is shared substrate;
- `baseline.toml` additions are reserved for the initial backfill — do not add new keys;
- claim edits: regen artifacts via `python codebase-map/gen_map.py --write`.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _kit_dir() -> Path:
    """The kit dir — the directory holding map_lib.py — found from this gate file's own location,
    so the gate still needs no per-project placeholders.

    Two things vary independently. GATE_FILE points at whatever directory the project's test suite
    collects, which may be inside the kit dir or nowhere near it; and the kit dir may sit at any
    PREFIX under the repo root. So each ancestor of this file is probed in order: the ancestor
    itself (gate installed inside the kit dir), `<ancestor>/codebase-map` (the root convention),
    then `<ancestor>/*/codebase-map` (a one-segment prefix such as `tools/`). The walk stops after
    the ancestor holding `.git`, so it can never leave the repo into a neighbouring checkout.

    The kit dir's NAME is still the fixed convention — only its prefix is free. A prefix deeper
    than one segment is deliberately not searched: walking a whole repo downward is slow and
    ambiguous. The failure below names every path it probed, so a deeper install is TOLD what the
    gate looked for instead of being guessed at. `abspath`, not `resolve()`: a junctioned kit dir
    must anchor to the adopting repo, matching map_lib.resolve_root."""
    probed: list[str] = []
    here = Path(os.path.abspath(__file__))
    for parent in here.parents:
        candidates = [parent, parent / "codebase-map"]
        candidates += sorted(p for p in parent.glob("*/codebase-map") if p.is_dir())
        for candidate in candidates:
            if (candidate / "map_lib.py").is_file():
                return candidate
            probed.append(str(candidate))
        if (parent / ".git").exists():
            break
    raise RuntimeError(
        f"codebase-map kit dir (the directory holding map_lib.py) not found above {here}.\n"
        "Probed:\n  " + "\n  ".join(probed)
    )


sys.path.insert(0, str(_kit_dir()))

import map_extractors as ext  # noqa: E402
import map_lib as m  # noqa: E402

INVENTORY_IDS = ext.inventory_ids()
ID_RE = getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE)


# ======================================================================================
# Real-tree assertions
# ======================================================================================


def test_every_inventory_key_is_claimed_or_baselined() -> None:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    cov = m.compute_coverage(inventories, m.owners_of(tree), tree.baseline)
    assert cov.clean, (
        "codebase-map coverage violations.\n"
        f"UNCLAIMED (new key? claim it in a feature dossier, or FOUNDATION.md for shared "
        f"substrate; baseline.toml is reserved for the initial backfill): {cov.unclaimed}\n"
        f"STALE CLAIMS (a dossier names a key that no longer exists): {cov.stale_claims}\n"
        f"STALE BASELINE (delete the line — the item is gone): {cov.stale_baseline}\n"
        f"LAZY BASELINE (now claimed — delete its baseline line): {cov.lazy_baseline}"
    )


def test_dossier_prose_headings_pinned() -> None:
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    features_dir = m.map_root() / "features"
    for d in tree.dossiers:
        text = (features_dir / f"{d.feature}.md").read_text(encoding="utf-8")
        for heading in m.REQUIRED_HEADINGS:
            assert heading in text, f"{d.source}: required section missing: {heading}"


def test_dossier_affordance_present_or_graced() -> None:
    """GRACED presence of the `## Reuse affordance` section: every dossier NOT on the shrink-only
    affordance-exempt list must carry the heading with at least one `seam:` line or a `none`
    declaration. New dossiers are never exempt (the list only shrinks + drops on touch), so a new
    feature is forced to record its reuse decision; the exempt baseline keeps adoption from
    retro-redding the fleet. Content quality is the un-gatable ceiling — reported, never gated."""
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    features_dir = m.map_root() / "features"
    texts = {
        d.feature: (features_dir / f"{d.feature}.md").read_text(encoding="utf-8")
        for d in tree.dossiers
    }
    offenders = m.affordance_offenders(texts, m.load_affordance_exempt())
    assert not offenders, (
        f"dossiers missing the '{m.AFFORDANCE_HEADING}' section — add a `seam: <id> — reuse for "
        f"<need>; extend via <point>` line per reusable seam, or `none — <why feature-specific>`: "
        f"{offenders}"
    )


def test_path_derived_keys_are_posix() -> None:
    for inv_id, keys in ext.all_inventories().items():
        offenders = [k for k in keys if "\\" in k]
        assert not offenders, f"{inv_id}: non-POSIX keys {offenders}"


def test_generated_artifacts_are_fresh() -> None:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    owners = m.owners_of(tree)
    gen_dir = m.map_root() / "generated"
    fresh = {
        gen_dir / "inventories.json": m.render_inventories_json(inventories, INVENTORY_IDS),
        gen_dir / "MAP.md": m.render_map_md(inventories, INVENTORY_IDS, owners, tree.baseline),
    }
    # SYMBOL recall tier (optional): only gated when the project declares symbol extractors.
    # render_symbols_json is byte-deterministic (sorted ids, POSIX, LF), so this byte-compare
    # holds identically on Windows and Linux — the AC2 cross-platform claim.
    symbols = getattr(ext, "all_symbols", list)()
    if symbols:
        fresh[gen_dir / "symbols.json"] = m.render_symbols_json(symbols)
    for path, expected in fresh.items():
        assert path.is_file(), f"missing generated artifact {path} — regen: {m.REGEN_CMD}"
        committed = m.lf(path.read_text(encoding="utf-8"))
        assert committed == expected, f"STALE {path.name} — regen: {m.REGEN_CMD}"


# ======================================================================================
# Standalone runner (projects without a test framework)
# ======================================================================================

if __name__ == "__main__":
    failures = 0
    for fn in (
        test_every_inventory_key_is_claimed_or_baselined,
        test_dossier_prose_headings_pinned,
        test_dossier_affordance_present_or_graced,
        test_path_derived_keys_are_posix,
        test_generated_artifacts_are_fresh,
    ):
        try:
            fn()
            print(f"ok   {fn.__name__}")
        except AssertionError as exc:
            print(f"FAIL {fn.__name__}\n{exc}")
            failures += 1
    sys.exit(1 if failures else 0)
