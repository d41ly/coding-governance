"""codebase-map kit — the portable engine (project-agnostic).

The self-verifying codebase map: per-feature DOSSIER files whose machine-readable claims are
CI-verified against live code inventories, a shrink-only BASELINE, deterministic GENERATED
artifacts with a byte-compare freshness gate, and a path->feature DIGEST for git ranges.

Two claim planes (the load-bearing design decision, learned the hard way):
- KEYED CLAIMS (the ratchet plane): dossiers claim EXACT KEYS from machine-enumerable
  inventories. The coverage gate operates ONLY here, both directions: a new unclaimed key
  fails, and a claim naming a dead key fails too — the map cannot rot into fiction.
- PATH GLOBS (the digest plane): used only by map_diff attribution; overlap legal, misses land
  in an explicit UNMAPPED bucket, NEVER gated.

This module is identical across repos. Project specifics live in TWO sibling files the adopting
repo owns: `.codebase-map.conf` at the repo root (paths) and `codebase-map/map_extractors.py`
(the EXTRACTORS dict — what is enumerable in THIS project). Everything here is stdlib-only,
Python >= 3.11 (tomllib).

Portability rules baked in (each was a review finding once — do not relax):
- every extractor FAILS CLOSED: a missing artifact or unexpected tree shape raises MapError,
  never returns a smaller inventory (the green-by-absence class);
- every path-derived key is POSIX-normalized (os.walk yields backslashes on Windows while CI
  renders on Linux — unnormalized keys flap the freshness gate per-platform);
- byte-compares are LF-normalized (CRLF checkouts);
- glob matching uses fnmatchcase (fnmatch normcases on Windows — attribution would diverge
  between platforms);
- file-kind inventories match EXTENSION SETS, not one literal filename (a `route.tsx` variant
  silently vanishing is the recurring "glob that skips a file class" bug).
"""

from __future__ import annotations

import json
import os
import re
import tomllib
from dataclasses import dataclass, field
from fnmatch import fnmatchcase
from pathlib import Path

STATUS_VALUES = frozenset({"shipped", "shipped-dark", "building", "deferred"})

#: Required prose sections in every feature dossier (headings pinned; content free).
REQUIRED_HEADINGS = ("## Constraints & why", "## Shared seams", "## Gaps")

#: Permissive default: PREFIX-anything id (override with a project grammar in map_extractors —
#: and if the project documents an id era as forward-only, keep the regex open there; a
#: validator hardcoding today's enum of node letters/prefixes blocks tomorrow's valid id.
DEFAULT_DECISION_ID_RE = re.compile(r"^[A-Z][A-Z0-9]{1,11}-[A-Za-z0-9][A-Za-z0-9-]*$")

_TOML_FENCE_RE = re.compile(r"^```toml[ \t]*\r?$(.*?)^```[ \t]*\r?$", re.MULTILINE | re.DOTALL)


class MapError(RuntimeError):
    """A codebase-map contract violation (malformed dossier, missing artifact, shape drift)."""


# ======================================================================================
# Repo root + conf
# ======================================================================================


def repo_root() -> Path:
    """The adopting repo's root. Convention: this kit dir lives AT the repo root as
    ``codebase-map/`` — so root is this file's grandparent. ``CODEBASE_MAP_ROOT`` overrides
    (tests, exotic layouts)."""
    override = os.environ.get("CODEBASE_MAP_ROOT")
    if override:
        return Path(override)
    return Path(__file__).resolve().parents[1]


def load_conf(root: Path | None = None) -> dict[str, str]:
    """Parse ``.codebase-map.conf`` (plain KEY=VALUE shell assignments, ``#`` comments) —
    the same one-conf-both-worlds format the memory-tree kit uses, readable by bash AND here."""
    path = (root or repo_root()) / ".codebase-map.conf"
    conf: dict[str, str] = {"MAP_ROOT": "memory/map"}
    if not path.is_file():
        return conf
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        conf[key.strip()] = value.strip().strip("\"'")
    return conf


def map_root(root: Path | None = None) -> Path:
    base = root or repo_root()
    return base / load_conf(base)["MAP_ROOT"]


# ======================================================================================
# Extractor helpers (the building blocks map_extractors.py composes)
# ======================================================================================


def no_subdirs(directory: Path, inventory: str, *, allow: frozenset[str] = frozenset({"__pycache__"})) -> None:
    """Fail-closed guard for deliberately-flat inventories: a future subdirectory must break
    the gate loudly, never escape a non-recursive walk silently."""
    if not directory.is_dir():
        raise MapError(f"{inventory}: expected directory missing: {directory}")
    unexpected = sorted(p.name for p in directory.iterdir() if p.is_dir() and p.name not in allow)
    if unexpected:
        raise MapError(
            f"{inventory}: unexpected subdirectories {unexpected} under {directory} — this "
            "inventory walks flat; extend the extractor before nesting the tree"
        )


def glob_inventory(directory: Path, pattern: str, inventory: str, *, exclude: frozenset[str] = frozenset(), flat: bool = True) -> list[str]:
    """Filenames matching ``pattern`` directly under ``directory`` (flat=True guards against
    nesting). Keys are bare filenames."""
    if flat:
        no_subdirs(directory, inventory)
    elif not directory.is_dir():
        raise MapError(f"{inventory}: expected directory missing: {directory}")
    return sorted(p.name for p in directory.glob(pattern) if p.name not in exclude)


def walk_file_keys(base: Path, filenames: frozenset[str], inventory: str, *, skip_top: frozenset[str] = frozenset()) -> list[str]:
    """POSIX-relative file paths for every file in ``filenames`` anywhere under ``base``.
    Pass the FULL extension set for a file kind (e.g. route.{ts,tsx,js,jsx}), never one
    literal name."""
    if not base.is_dir():
        raise MapError(f"{inventory}: expected directory missing: {base}")
    keys: list[str] = []
    for dirpath, dirnames, files in os.walk(base):
        rel = Path(dirpath).relative_to(base).as_posix()
        top = rel.split("/", 1)[0]
        if top in skip_top:
            dirnames[:] = []
            continue
        for name in files:
            if name in filenames:
                keys.append(name if rel == "." else f"{rel}/{name}")
    return sorted(keys)


def walk_dir_keys(base: Path, filenames: frozenset[str], inventory: str, *, root_key: str = "root") -> list[str]:
    """POSIX-relative DIRECTORY keys for every dir under ``base`` containing one of
    ``filenames`` (the screens-style inventory: the dir is the unit, e.g. Next.js pages)."""
    if not base.is_dir():
        raise MapError(f"{inventory}: expected directory missing: {base}")
    keys: list[str] = []
    for dirpath, _dirnames, files in os.walk(base):
        if filenames & set(files):
            rel = Path(dirpath).relative_to(base).as_posix()
            keys.append(root_key if rel == "." else rel)
    return sorted(keys)


def module_inventory(package_path: Path, inventory: str, *, prefix: str = "") -> list[str]:
    """Python module names directly under a package dir (flat; a subpackage fails loud)."""
    no_subdirs(package_path, inventory)
    return sorted(
        f"{prefix}{p.stem}" for p in package_path.glob("*.py") if p.stem != "__init__"
    )


def json_artifact_inventory(path: Path, inventory: str, extract) -> list[str]:
    """Keys from a generated JSON artifact — read DIRECTLY and fail-closed (runtime loaders
    are often fail-open by design; a coverage gate must not be)."""
    if not path.is_file():
        raise MapError(f"{inventory}: generated artifact missing: {path} (regenerate it)")
    try:
        keys = list(extract(json.loads(path.read_text(encoding="utf-8"))))
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise MapError(f"{inventory}: malformed {path}: {exc}") from exc
    if not keys:
        raise MapError(f"{inventory}: empty inventory from {path}")
    return sorted(keys)


# ======================================================================================
# Dossier / baseline contract
# ======================================================================================


@dataclass(frozen=True)
class Dossier:
    feature: str
    title: str
    status: str
    streams: tuple[str, ...]
    decisions: tuple[str, ...]
    claims: dict[str, tuple[str, ...]] = field(default_factory=dict)
    globs: tuple[str, ...] = ()
    source: str = "<dossier>"


def _require_str_list(value: object, what: str, source: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
        raise MapError(f"{source}: {what} must be a list of non-empty strings")
    return tuple(value)


def parse_dossier(
    text: str,
    inventory_ids: tuple[str, ...],
    *,
    decision_id_re: re.Pattern[str] = DEFAULT_DECISION_ID_RE,
    source: str = "<dossier>",
) -> Dossier:
    """Parse a dossier's machine half — the FIRST ```` ```toml ```` fence. Fails loud on:
    no fence, TOML errors, missing/unknown top or claim keys (claims must carry EXACTLY the
    project's inventory ids — typo protection), bad status, malformed decision ids, non-string
    title, backslashes in globs. A dossier that doesn't parse must break the gate, never be
    skipped."""
    match = _TOML_FENCE_RE.search(text)
    if match is None:
        raise MapError(f"{source}: no ```toml fence found (the machine half is required)")
    try:
        data = tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError as exc:
        raise MapError(f"{source}: toml parse error: {exc}") from exc

    required_top = {"feature", "title", "status", "streams", "decisions", "claims", "paths"}
    missing = required_top - set(data)
    unknown = set(data) - required_top
    if missing or unknown:
        raise MapError(
            f"{source}: top-level keys — missing {sorted(missing)}, unknown {sorted(unknown)}"
        )
    for key in ("feature", "title"):
        if not isinstance(data[key], str) or not data[key]:
            raise MapError(f"{source}: {key} must be a non-empty string")
    if data["status"] not in STATUS_VALUES:
        raise MapError(f"{source}: status {data['status']!r} not in {sorted(STATUS_VALUES)}")

    decisions = _require_str_list(data["decisions"], "decisions", source)
    bad_ids = [d for d in decisions if not decision_id_re.match(d)]
    if bad_ids:
        raise MapError(f"{source}: decision ids not matching the project grammar: {bad_ids}")

    claims_raw = data["claims"]
    if not isinstance(claims_raw, dict):
        raise MapError(f"{source}: [claims] must be a table")
    missing_c = set(inventory_ids) - set(claims_raw)
    unknown_c = set(claims_raw) - set(inventory_ids)
    if missing_c or unknown_c:
        raise MapError(
            f"{source}: [claims] keys — missing {sorted(missing_c)}, unknown {sorted(unknown_c)} "
            f"(exactly {list(inventory_ids)} required; empty lists are fine)"
        )
    claims = {k: _require_str_list(claims_raw[k], f"claims.{k}", source) for k in inventory_ids}

    paths = data["paths"]
    if not isinstance(paths, dict) or set(paths) != {"globs"}:
        raise MapError(f"{source}: [paths] must be a table with exactly one key: globs")
    globs = _require_str_list(paths["globs"], "paths.globs", source)
    with_backslash = [g for g in globs if "\\" in g]
    if with_backslash:
        raise MapError(f"{source}: globs must be forward-slash only: {with_backslash}")

    return Dossier(
        feature=data["feature"],
        title=data["title"],
        status=data["status"],
        streams=_require_str_list(data["streams"], "streams", source),
        decisions=decisions,
        claims=claims,
        globs=globs,
        source=source,
    )


@dataclass(frozen=True)
class MapTree:
    foundation: Dossier
    dossiers: tuple[Dossier, ...]
    baseline: dict[str, tuple[str, ...]]


def parse_baseline(
    text: str, inventory_ids: tuple[str, ...], *, source: str = "baseline.toml"
) -> dict[str, tuple[str, ...]]:
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        raise MapError(f"{source}: toml parse error: {exc}") from exc
    unknown = set(data) - set(inventory_ids)
    if unknown:
        raise MapError(f"{source}: unknown inventory keys {sorted(unknown)}")
    return {k: _require_str_list(data.get(k, []), k, source) for k in inventory_ids}


def load_map_tree(
    inventory_ids: tuple[str, ...],
    *,
    root: Path | None = None,
    decision_id_re: re.Pattern[str] = DEFAULT_DECISION_ID_RE,
) -> MapTree:
    map_dir = map_root(root)
    foundation_path = map_dir / "FOUNDATION.md"
    if not foundation_path.is_file():
        raise MapError(f"missing {foundation_path}")
    rel = map_dir.name
    foundation = parse_dossier(
        foundation_path.read_text(encoding="utf-8"),
        inventory_ids,
        decision_id_re=decision_id_re,
        source=f"{rel}/FOUNDATION.md",
    )
    if foundation.feature != "foundation":
        raise MapError('FOUNDATION.md must declare feature = "foundation"')

    dossiers: list[Dossier] = []
    features_dir = map_dir / "features"
    if features_dir.is_dir():
        for path in sorted(features_dir.glob("*.md")):
            d = parse_dossier(
                path.read_text(encoding="utf-8"),
                inventory_ids,
                decision_id_re=decision_id_re,
                source=f"{rel}/features/{path.name}",
            )
            if d.feature != path.stem:
                raise MapError(f"{d.source}: feature {d.feature!r} != filename stem {path.stem!r}")
            dossiers.append(d)
    names = [d.feature for d in dossiers]
    if len(names) != len(set(names)):
        raise MapError(f"duplicate feature names across dossiers: {names}")

    baseline_path = map_dir / "baseline.toml"
    baseline = (
        parse_baseline(baseline_path.read_text(encoding="utf-8"), inventory_ids)
        if baseline_path.is_file()
        else {k: () for k in inventory_ids}
    )
    return MapTree(foundation=foundation, dossiers=tuple(dossiers), baseline=baseline)


# ======================================================================================
# Coverage (pure)
# ======================================================================================


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


def owners_of(tree: MapTree) -> dict[str, dict[str, tuple[str, ...]]]:
    owners = {d.feature: d.claims for d in tree.dossiers}
    owners["foundation"] = tree.foundation.claims
    return owners


# ======================================================================================
# Generated artifacts (deterministic renders; byte-compared by the freshness gate)
# ======================================================================================

REGEN_CMD = "python codebase-map/gen_map.py --write"


def render_inventories_json(inventories: dict[str, list[str]], inventory_ids: tuple[str, ...]) -> str:
    # Keys-only on purpose: pure dossier/claim edits must never stale this artifact.
    doc = {
        "$comment": f"generated by codebase-map/gen_map.py — do not hand-edit; regen: {REGEN_CMD}",
        "inventories": {k: sorted(inventories[k]) for k in inventory_ids},
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def claimant_index(
    inventories: dict[str, list[str]],
    owners: dict[str, dict[str, tuple[str, ...]]],
    baseline: dict[str, tuple[str, ...]],
) -> dict[str, dict[str, list[str]]]:
    out: dict[str, dict[str, list[str]]] = {}
    for inv_id, keys in inventories.items():
        base = set(baseline.get(inv_id, ()))
        per_key: dict[str, list[str]] = {}
        for key in keys:
            who = sorted(o for o, claims in owners.items() if key in claims.get(inv_id, ()))
            if not who:
                who = ["baseline"] if key in base else ["UNCLAIMED"]
            per_key[key] = who
        out[inv_id] = per_key
    return out


def render_map_md(
    inventories: dict[str, list[str]],
    inventory_ids: tuple[str, ...],
    owners: dict[str, dict[str, tuple[str, ...]]],
    baseline: dict[str, tuple[str, ...]],
) -> str:
    """The human map: every inventory as a key -> claimant table. Deterministic: sorted inputs
    only, NO timestamps (determinism is what makes the freshness gate possible)."""
    idx = claimant_index(inventories, owners, baseline)
    counts = " · ".join(f"{k}: {len(inventories[k])}" for k in inventory_ids)
    lines: list[str] = [
        f"<!-- generated by codebase-map/gen_map.py — do not hand-edit; regen: {REGEN_CMD} -->",
        "",
        "# Codebase map — generated system inventory",
        "",
        "Every machine-enumerable moving part, annotated with its claimant "
        "(`<feature>` dossier · `foundation` · `baseline` · `UNCLAIMED`). Claims live in the "
        "map tree; this file just renders them.",
        "",
        f"Inventories: {counts}",
    ]
    for inv_id in inventory_ids:
        lines += ["", f"## {inv_id}", "", "| key | claimant |", "|---|---|"]
        lines += [f"| `{k}` | {', '.join(idx[inv_id][k])} |" for k in sorted(inventories[inv_id])]
    return "\n".join(lines) + "\n"


def render_baseline(baseline: dict[str, list[str]], inventory_ids: tuple[str, ...]) -> str:
    """Hand-rendered TOML (stdlib has no writer): sorted string arrays per inventory."""
    lines = [
        "# baseline.toml — the shrink-only ratchet baseline (codebase-map kit).",
        "# Items inventoried from code but not yet claimed by a dossier or FOUNDATION.md.",
        "# This file only SHRINKS: claim an item, delete its line. New keys belong in a",
        "# dossier, not here — additions are reserved for the initial backfill and reviewed.",
        "",
    ]
    for inv_id in inventory_ids:
        keys = sorted(baseline.get(inv_id, []))
        if not keys:
            lines.append(f"{inv_id} = []")
            continue
        lines.append(f"{inv_id} = [")
        lines.extend(f"  {json.dumps(k, ensure_ascii=False)}," for k in keys)
        lines.append("]")
    return "\n".join(lines) + "\n"


# ======================================================================================
# Map-diff attribution (pure)
# ======================================================================================


def attribute_paths(
    paths: list[str],
    tree: MapTree,
    *,
    keyed_attributors: tuple[tuple[re.Pattern[str], str], ...] = (),
) -> dict[str, list[str]]:
    """Attribute changed file paths to features: keyed attributors first (a regex whose
    group(1) is a claim key in the given inventory — e.g. a migration filename -> revision id),
    then dossier globs, then foundation globs, else UNMAPPED. Every claimant sees the path
    (multi-claim legal); nothing is silently dropped."""
    owners = [(d.feature, d) for d in tree.dossiers] + [("foundation", tree.foundation)]
    result: dict[str, list[str]] = {}
    for raw in paths:
        path = raw.replace("\\", "/")
        hits: list[str] = []
        for pattern, inv_id in keyed_attributors:
            m = pattern.match(path)
            if m:
                key = m.group(1)
                hits = [name for name, d in owners if key in d.claims.get(inv_id, ())]
                break
        if not hits:
            hits = [
                name
                for name, d in owners
                if any(
                    fnmatchcase(path, g) or fnmatchcase(path, g.rstrip("/") + "/*")
                    for g in d.globs
                )
            ]
        for owner in hits or ["UNMAPPED"]:
            result.setdefault(owner, []).append(path)
    return result


def lf(text: str) -> str:
    """LF-normalize before byte-comparing a committed artifact (CRLF-checkout defense)."""
    return text.replace("\r\n", "\n")
