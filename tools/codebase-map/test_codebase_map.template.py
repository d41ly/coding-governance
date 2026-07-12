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

import sys
from pathlib import Path


def _kit_dir() -> Path:
    """Walk up from this file to the repo root holding codebase-map/ (the kit dir name is a
    kit convention, so the gate needs no per-project placeholders)."""
    for parent in Path(__file__).resolve().parents:
        if (parent / "codebase-map" / "map_lib.py").is_file():
            return parent / "codebase-map"
    raise RuntimeError("codebase-map/ kit dir not found above the gate file")


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
