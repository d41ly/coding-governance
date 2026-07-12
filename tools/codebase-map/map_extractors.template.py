"""map_extractors.py — THIS PROJECT's inventory declarations (the only project-owned code).

Copied from codebase-map/map_extractors.template.py at adoption; fill it per
codebase-map/INVENTORY-DERIVATION.md, then run `python codebase-map/gen_map.py --scaffold`.

Rules (from the derivation checklist — each was a shipped bug once):
- Prefer IMPORT/REGISTRY reads over file globs where the code already exposes a registry
  (a flags list, a CLI command table, a migration chain walker).
- File-kind inventories: pass the FULL extension set (route.{ts,tsx,js,jsx}), never one name.
- Every extractor fails CLOSED — use the map_lib helpers; they raise MapError on a missing
  artifact or an unexpected subtree instead of returning fewer keys.
- Keys must be platform-stable: the helpers POSIX-normalize; keep it that way.
"""

from __future__ import annotations

import re

import map_lib as m

ROOT = m.repo_root()

# --------------------------------------------------------------------------------------
# EXTRACTORS — inventory id -> zero-arg callable returning sorted list[str] of keys.
# The dict's KEYS are the project's inventory ids: every dossier's [claims] table must
# carry exactly these keys, and baseline.toml may only use them.
#
# Delete the examples and declare your own. An EMPTY dict fails the gate on purpose —
# a map with no inventories enforces nothing.
# --------------------------------------------------------------------------------------

EXTRACTORS: dict[str, object] = {
    # --- file-glob examples (cheap, filesystem ground truth) --------------------------
    # "routes": lambda: m.walk_file_keys(
    #     ROOT / "src" / "app",
    #     frozenset({"route.ts", "route.tsx", "route.js", "route.jsx"}),
    #     "routes",
    # ),
    # "docs": lambda: m.glob_inventory(ROOT / "docs", "*.md", "docs", exclude=frozenset({"index.md"})),
    # "modules": lambda: m.module_inventory(ROOT / "app" / "services", "modules"),
    #
    # --- registry example (import the code's own source of truth) ---------------------
    # "cli": lambda: _cli_commands(),
    #
    # --- generated-artifact example (read the committed JSON, fail-closed) ------------
    # "components": lambda: m.json_artifact_inventory(
    #     ROOT / "packages" / "ui" / "manifest.json",
    #     "components",
    #     lambda doc: (entry["name"] for entry in doc["components"]),
    # ),
}


# def _cli_commands() -> list[str]:
#     import sys
#     sys.path.insert(0, str(ROOT / "src"))
#     from myproject.cli import app
#     names = [c.name for c in app.registered_commands]
#     if any(n is None for n in names):
#         raise m.MapError("cli: a command has no explicit name")
#     return sorted(names)


#: Optional: the project's decision/record id grammar (dossier `decisions` entries are
#: validated against it). Keep FORWARD-ONLY id schemes open — don't hardcode today's enum.
DECISION_ID_RE = m.DEFAULT_DECISION_ID_RE

#: Optional: keyed path attributors for map_diff — (regex, inventory_id) pairs where the
#: regex's group(1) IS a claim key, e.g. a migration file -> its revision id:
#:   (re.compile(r"^db/migrations/([0-9a-f]+)_"), "migrations"),
KEYED_ATTRIBUTORS: tuple[tuple[re.Pattern[str], str], ...] = ()


def inventory_ids() -> tuple[str, ...]:
    if not EXTRACTORS:
        raise m.MapError(
            "map_extractors.EXTRACTORS is empty — declare this project's inventories "
            "(see codebase-map/INVENTORY-DERIVATION.md); an inventory-less map enforces nothing"
        )
    return tuple(EXTRACTORS)


def all_inventories() -> dict[str, list[str]]:
    return {inv_id: fn() for inv_id, fn in EXTRACTORS.items()}  # type: ignore[operator]
