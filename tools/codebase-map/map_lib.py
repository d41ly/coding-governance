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
repo owns: `.codebase-map.conf` at the repo root (paths) and `<kit-dir>/map_extractors.py`
(the EXTRACTORS dict — what is enumerable in THIS project). Everything here is stdlib-only,
Python >= 3.11 (tomllib).

The kit DIRECTORY is named `codebase-map` by convention (the gate resolves it by that name), but
its PREFIX under the repo root is free: `<repo-root>/codebase-map/` and
`<repo-root>/tools/codebase-map/` are both supported — see repo_root/resolve_root.

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

import ast
import json
import os
import re
import tomllib
from dataclasses import dataclass, field
from fnmatch import fnmatchcase
from pathlib import Path

#: gov:kit codebase-map — engine identity. Bump on any engine/render change; mirrored into the
#: generated artifacts as `codebase-map@<v>` so the deployer can grep the installed version.
KIT_CODEBASE_MAP_VERSION = "1.4"

#: The per-repo conf, at the adopting repo's ROOT. Also the MARKER resolve_root walks up for: a
#: repo that has adopted the kit has this file, and the kit needs no other declaration of where
#: the root is (a KIT_DIR key would be a second copy of what the filesystem already answers).
CONF_NAME = ".codebase-map.conf"

STATUS_VALUES = frozenset({"shipped", "shipped-dark", "building", "deferred"})

#: Required prose sections in every feature dossier (headings pinned; content free).
REQUIRED_HEADINGS = ("## Constraints & why", "## Shared seams", "## Gaps")

#: The forward reuse-menu heading. DELIBERATELY NOT in REQUIRED_HEADINGS: that tuple is looped
#: over every dossier with no exemption, so adding it there would retro-red the whole fleet.
#: Enforced instead by a GRACED check (affordance_offenders) that skips dossiers on a shrink-only
#: affordance-exempt list. Under it: leading `seam:` lines, or a single `none` line (parse_affordance).
AFFORDANCE_HEADING = "## Reuse affordance"

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


def resolve_root(kit_dir: Path) -> Path:
    """The adopting repo's root, as a PURE function of where the kit dir sits — so the selftest
    can drive both install shapes without copying this module around.

    Walk UP from ``kit_dir`` and return the nearest ancestor holding ``CONF_NAME``; stop after the
    ancestor holding ``.git``; otherwise fall back to ``kit_dir``'s parent. That fallback IS the
    kit's original convention (a kit dir at ``<repo-root>/codebase-map/`` makes the parent the
    root), so a root-installed adopter with a conf and one without both resolve exactly as before.
    The walk is what makes a PREFIXED install work: at ``<repo-root>/tools/codebase-map/`` the
    parent is ``tools/`` and every derived path was wrong by one segment.

    The ``.git`` stop is not decoration. Worktrees are commonly kept INSIDE the primary tree (this
    repo puts them under ``.claude/worktrees/``), so an unbounded walk from a worktree's kit dir
    reaches the PRIMARY tree's conf and resolves MAP_ROOT into a different checkout. ``.git`` is a
    FILE in a worktree and a directory in a primary tree, so one ``exists()`` covers both, and the
    conf is tested BEFORE it so an adopted root that also holds ``.git`` still wins.

    Pure path math on ``abspath``, never ``resolve()``: a symlinked/junctioned kit dir must anchor
    to the ADOPTING repo, not to the link target's parent (the gate's walk-up and the adopter both
    accept that layout — this must agree with them). That guarantee is also why the root is not
    taken from ``git rev-parse --show-toplevel``, which resolves the junction away."""
    kit_dir = Path(os.path.abspath(kit_dir))
    for ancestor in kit_dir.parents:
        if (ancestor / CONF_NAME).is_file():
            return ancestor
        if (ancestor / ".git").exists():
            break
    return kit_dir.parent


def repo_root() -> Path:
    """The adopting repo's root for THIS installed copy of the kit. ``CODEBASE_MAP_ROOT``
    overrides (tests, exotic layouts); otherwise ``resolve_root`` of this file's own directory."""
    override = os.environ.get("CODEBASE_MAP_ROOT")
    if override:
        return Path(os.path.abspath(override))
    return resolve_root(kit_dir())


def kit_dir() -> Path:
    """THIS installed copy of the kit — the directory holding this module."""
    return Path(os.path.abspath(__file__)).parent


def relative_kit(kit: Path, root: Path) -> str:
    """``kit`` as a POSIX path relative to ``root`` — how a HUMAN must spell the kit from the repo
    root, which is how every remedy line and usage line in this kit must spell it.

    Pure, so the selftest can drive every install shape. POSIX because these strings land in
    generated artifacts that are byte-compared across a Windows and a Linux render. Falls back to
    the kit dir's NAME when it is not under ``root`` — that happens under a ``CODEBASE_MAP_ROOT``
    pointed at a fixture tree, and a stable fallback keeps those renders deterministic instead of
    embedding an absolute temp path."""
    try:
        return Path(os.path.abspath(kit)).relative_to(Path(os.path.abspath(root))).as_posix()
    except ValueError:
        return Path(kit).name


def kit_rel(root: Path | None = None) -> str:
    """This install's kit dir, relative to the repo root (e.g. ``codebase-map`` or
    ``tools/codebase-map``)."""
    return relative_kit(kit_dir(), root or repo_root())


def regen_cmd(root: Path | None = None) -> str:
    """The regen command line, spelled for THIS install's prefix. Every remedy that tells a human
    to re-render must go through here: a remedy naming a path that does not exist is a dead end at
    exactly the moment someone is stuck, and the kit's whole convention is that its prefix is free."""
    return f"python {kit_rel(root)}/gen_map.py --write"


def require_adopted_root() -> Path:
    """The repo root, ASSERTED to carry the conf — for the entrypoints that read only committed
    artifacts and therefore have no project layer to fail closed for them (reuse_lookup, map_diff).

    Resolution answers WHERE the root is; this answers WHETHER anything was adopted there. They are
    deliberately separate: the library layer stays fail-open (a thin corpus is a thin shortlist, by
    design), while a CLI refuses. Without this, a mis-rooted lookup prints `corpus: 0 symbols` and
    `no seam fits`, and a mis-rooted `--converge` prints `collision_flags: 0` — both exit 0, and
    both read as real answers derived from a real population. That is the green-by-absence class
    the whole kit exists to prevent, so the kit must not ship it."""
    root = repo_root()
    if (root / CONF_NAME).is_file():
        return root
    override = os.environ.get("CODEBASE_MAP_ROOT")
    kit_dir = Path(os.path.abspath(__file__)).parent
    raise MapError(
        f"no {CONF_NAME} at the resolved repo root — refusing to answer from an empty corpus.\n"
        f"  resolved root: {root}\n"
        f"  kit dir:       {kit_dir}\n"
        f"  root came from: {'CODEBASE_MAP_ROOT=' + override if override else 'the walk up from the kit dir'}\n"
        f"If this repo has adopted the kit, {CONF_NAME} belongs at its ROOT (the kit dir may live at\n"
        f"any prefix under it). If it has not, run the adopter: <kit-dir>/adopt-codebase-map.sh --scaffold."
    )


def load_conf(root: Path | None = None) -> dict[str, str]:
    """Parse ``.codebase-map.conf`` (plain KEY=VALUE shell assignments, ``#`` comments) —
    the same one-conf-both-worlds format the memory-tree kit uses, readable by bash AND here."""
    path = (root or repo_root()) / CONF_NAME
    conf: dict[str, str] = {"MAP_ROOT": "memory/map"}
    if not path.is_file():
        return conf
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip().removeprefix("export ").strip()
        value = value.strip()
        # match bash sourcing semantics for the restricted grammar the conf documents:
        # quoted values keep everything inside the quotes; unquoted values end at whitespace
        # (so an inline " # comment" can't leak into the value and diverge from bash)
        if value[:1] in {'"', "'"} and value[-1:] == value[:1] and len(value) >= 2:
            value = value[1:-1]
        else:
            value = value.split()[0] if value.split() else ""
        conf[key] = value
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
# Symbol-tier extractors (the SYMBOL recall tier — feed render_symbols_json only)
# ======================================================================================
#
# These build the reuse recall index: every reusable symbol as {id, kind, file}. Unlike the
# keyed inventories they are NEVER a ratchet (a new symbol must never fail CI), so they render
# to symbols.json only. Same fail-closed law as every extractor: a real parser where one is
# available (python_symbols uses ast), and a raise-on-unmatched enumeration floor elsewhere
# (enumerate_exports) — NEVER a regex that silently skips export forms it forgot (the
# green-by-absence hole: export default / re-exports / type / decorated classes).

#: kind vocabulary for a symbol row. Frozen — render_symbols_json rejects any other kind.
SYMBOL_KINDS = frozenset({"function", "class", "component", "const-export"})

_SKIP_DIRS = frozenset({"__pycache__", "node_modules", ".git", ".venv"})


def python_symbols(
    base: Path,
    layer: str,
    *,
    root: Path | None = None,
    skip_dirs: frozenset[str] = _SKIP_DIRS,
) -> list[dict[str, str]]:
    """SYMBOL extractor for a Python layer, real-parser-backed (the F1a case). Every PUBLIC
    module-level ``def``/``async def`` -> function and ``class`` -> class under ``base``, plus
    statically-listed ``__all__`` names not already captured -> const-export. ``file`` is
    POSIX-relative to ``root`` (repo root by default) so a reference scan can open it.

    Fail-closed: an ``ast`` SyntaxError raises MapError (never a smaller index). Decorated and
    async defs are captured natively — the case a hand-rolled regex drops, and the whole reason
    to prefer a real parser. Leading-underscore names are private by Python convention (skipped)
    and only module-body nodes count (a def nested in a class/try is not a top-level seam)."""
    root = root or repo_root()
    if not base.is_dir():
        raise MapError(f"{layer}: expected directory missing: {base}")
    out: list[dict[str, str]] = []
    for dirpath, dirnames, files in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in sorted(files):
            if not name.endswith(".py"):
                continue
            path = Path(dirpath) / name
            rel = path.relative_to(root).as_posix()
            try:
                mod = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except SyntaxError as exc:
                raise MapError(f"{layer}: python parse error in {rel}: {exc}") from exc
            captured: set[str] = set()
            for node in mod.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
                    out.append({"id": node.name, "kind": "function", "file": rel})
                    captured.add(node.name)
                elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                    out.append({"id": node.name, "kind": "class", "file": rel})
                    captured.add(node.name)
            for exported in _static_all(mod):
                if exported not in captured and not exported.startswith("_"):
                    out.append({"id": exported, "kind": "const-export", "file": rel})
    return out


def _static_all(mod: ast.Module) -> list[str]:
    """``__all__`` entries when it is a plain list/tuple of string literals; [] otherwise.
    A dynamically-built ``__all__`` (concatenation, star-unpack) augments nothing — the
    def/class capture still stands (a documented recall floor, never a silent shrink)."""
    for node in mod.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        else:
            continue
        if not any(isinstance(t, ast.Name) and t.id == "__all__" for t in targets):
            continue
        value = node.value
        if isinstance(value, (ast.List, ast.Tuple)):
            names = [e.value for e in value.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
            if len(names) == len(value.elts):  # every element a string literal, else give up
                return names
        return []
    return []


#: Default JS/TS ``export`` rule set for enumerate_exports — the common floor. (regex, kind);
#: kind None = a recognized form with no runtime seam to index (types) or no name to recall by
#: (barrel re-exports, anonymous default). Order matters: default/async forms precede the bare
#: forms. Deliberately does NOT cover every TS form (e.g. `export abstract class`, `export
#: declare …`): an uncovered `export` RAISES, forcing the adopter to add a rule or use tsc,
#: rather than silently dropping the symbol. Extend it, or map a PascalCase const to
#: "component", in the project's map_extractors.py.
_JS_ID = r"(?P<id>[A-Za-z_$][\w$]*)"
JS_EXPORT_RULES: tuple[tuple[re.Pattern[str], str | None], ...] = (
    (re.compile(rf"export\s+default\s+async\s+function\s*\*?\s*{_JS_ID}"), "function"),
    (re.compile(rf"export\s+default\s+function\s*\*?\s*{_JS_ID}"), "function"),
    (re.compile(r"export\s+default\s+class\s+extends\b"), None),   # anonymous default class extending
    (re.compile(rf"export\s+default\s+class\s+{_JS_ID}"), "class"),
    (re.compile(rf"export\s+async\s+function\s*\*?\s*{_JS_ID}"), "function"),
    (re.compile(rf"export\s+function\s*\*?\s*{_JS_ID}"), "function"),
    (re.compile(rf"export\s+class\s+{_JS_ID}"), "class"),
    (re.compile(rf"export\s+(?:const|let|var)\s+{_JS_ID}"), "const-export"),
    (re.compile(r"export\s+type\s*\{"), None),               # type-only re-export
    (re.compile(rf"export\s+(?:type|interface|enum|namespace)\s+{_JS_ID}"), None),
    (re.compile(r"export\s*\{"), None),                       # named re-export (indexed at def site)
    (re.compile(r"export\s+\*"), None),                       # star re-export
    (re.compile(r"export\s+default\b"), None),                # anonymous default / default <expr>
)


#: Statement-leading DEFINITION forms for a JS/TS layer — the companion to JS_EXPORT_RULES, which
#: sees only what a file exports. (regex, kind). `export` prefixes are optional here: a form that is
#: both a definition and an export is emitted by both scans and deduped on `(id, file)`.
JS_DEFINITION_RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    # `function(?:\s*\*\s*|\s+)` and NOT `function\s*\*?\s*`: the permissive form lets the keyword
    # run straight into the name, so a line of prose beginning "functionality, duplicate or …"
    # inside a prompt string was indexed as a function named `ality`. Measured — it was the one row
    # by which this probe disagreed with the lexicon's independently-authored set.
    (re.compile(rf"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function(?:\s*\*\s*|\s+){_JS_ID}",
                re.M), "function"),
    (re.compile(rf"^\s*(?:export\s+)?(?:default\s+)?class\s+{_JS_ID}", re.M), "class"),
    (re.compile(rf"^\s*(?:export\s+)?(?:const|let|var)\s+{_JS_ID}\s*=\s*(?:async\s*)?"
                r"(?:function\b|\([^)]*\)\s*=>|[A-Za-z_$][\w$]*\s*=>)", re.M), "function"),
)


def render_comment_free(text: str) -> str:
    """The source with COMMENTS blanked and everything else byte-identical, line count preserved.

    `scan_js_definitions` used to strip block comments and THEN line comments, so a bare block
    opener written inside a `//` comment opened a `DOTALL` span that ran to the next closer and
    swallowed every definition between. Measured on the adopter corpus: 14 definitions lost across 9
    files. Swapping the two passes trades that for the mirror defect — a `//` inside a block comment
    truncates the line, the closer is lost, and the span runs on — because comments and strings
    EXCLUDE each other and no sequence of independent passes can say so.

    It TRACKS strings and templates so a marker inside one cannot open a comment, and it emits their
    contents UNCHANGED. That distinction is the whole safety argument: an earlier revision of this
    unit blanked string contents too, and since the pass models no regex literal, a stray delimiter
    blanked a live region — eight real definitions removed from this repo's own tracked JavaScript.
    The only bytes this function removes are inside a comment, so it cannot delete a definition.

    LINE COUNT IS PRESERVED because the caller reports `file:line` and `symbols.json` is committed;
    a pass that collapsed lines would move every definition and corrupt the artifact silently.
    """
    out: list[str] = []
    i, n = 0, len(text)
    while i < n:
        two = text[i : i + 2]
        if two == "//":
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if two == "/*":
            j = text.find("*/", i + 2)
            if j < 0:
                # Unterminated: abandon the opener rather than swallow the file, the rule
                # TOOL-aLexedStripper-1 S5 set for the token scan.
                out.append("  ")
                i += 2
                continue
            out.append("\n" * text.count("\n", i, j + 2))
            i = j + 2
            continue
        ch = text[i]
        if ch in ("'", '"', "`"):
            j = i + 1
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == ch:
                    break
                if text[j] == "\n" and ch != "`":
                    break  # an unterminated single-line literal ends at its line
                j += 1
            closed = j < n and text[j] == ch
            out.append(text[i : j + 1] if closed else ch)
            i = j + 1 if closed else i + 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def scan_js_definitions(
    base: Path,
    layer: str,
    *,
    extensions: frozenset[str] = frozenset({".js"}),
    rules: tuple[tuple[re.Pattern[str], str], ...] = JS_DEFINITION_RULES,
    root: Path | None = None,
    skip_dirs: frozenset[str] = _SKIP_DIRS,
) -> list[dict[str, str]]:
    """SYMBOL extractor for a JS layer's DEFINITIONS, not only its exports.

    WHY THIS EXISTS, MEASURED. ``enumerate_exports`` guarantees completeness over ``export`` FORMS —
    an unrecognised one raises. It guarantees nothing about a file with no ``export`` line at all,
    and that is the shape this repo's own kit hooks have. Measured on gov at ``b4f0cf1c``: the six
    tracked ``tools/**/*.js`` carry **30** top-level definitions and the recall index carried **3**
    rows for that layer — the three workflow ``meta`` blocks, which are objects and are DISJOINT from
    the 30. So the index carried none of the definitions, and ``reuse_lookup.py`` could not see
    ``boundedK`` (``tools/hooks/agent-cap.js``), the binder every fan-out consumer routes through.
    The comment that kept it that way read "accurate coverage of a layer with few exports, not a
    hole"; it was true about exports and false about the layer.

    Fail-closed, in the only direction available. There is no stdlib JS parser, so this is a probe
    and says so — its ceiling is a definition FORM the rule set forgot, and a definition spelled
    inside a template literal (the ceiling ``enumerate_exports`` documents for itself). What it does
    guarantee is a LIVENESS floor: a scanned file yielding ZERO symbols raises MapError naming it,
    because a probe that silently reads nothing is exactly how the hole above stayed invisible.
    Measured: every one of the six files under ``tools/`` yields at least one definition today
    (19, 4, 1, 2, 2, 2), so the floor is a measurement rather than an assumption.

    Comments are stripped the same way ``enumerate_exports`` strips them — block spans replaced by
    their own newline count so removing one never merges two statements onto one line.
    """
    root = root or repo_root()
    if not base.is_dir():
        raise MapError(f"{layer}: expected directory missing: {base}")
    out: list[dict[str, str]] = []
    for dirpath, dirnames, files in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in sorted(files):
            if not any(name.endswith(ext) for ext in extensions):
                continue
            path = Path(dirpath) / name
            rel = path.relative_to(root).as_posix()
            text = render_comment_free(path.read_text(encoding="utf-8"))
            seen: set[str] = set()
            for rx, kind in rules:
                for mm in rx.finditer(text):
                    sym = mm.group("id")
                    if sym in seen:
                        continue
                    seen.add(sym)
                    out.append({"id": sym, "kind": kind, "file": rel})
            if not seen:
                raise MapError(
                    f"{layer}: {rel} yielded NO definition. A JS file with no top-level function or "
                    f"class is either not what this layer is for, or a form these rules forgot — "
                    f"raising rather than indexing less, which is how this layer went 30-to-3 unseen"
                )
    return out


def _has_top_level_comma(s: str) -> bool:
    """True if ``s`` has a comma at bracket-depth 0 — for an ``export const/let/var`` line, a second
    declarator (``a = 1, b = 2``). A comma inside ``()``/``[]``/``{}``/``<>`` (an array/object/call
    initializer, or a TS generic like ``Record<string, string>`` / ``forwardRef<A, B>``) is NOT a
    declarator separator and must not trip this. Ceiling (documented, rare): a bare ``<``/``>``
    comparison or bit-shift appearing before a genuine second declarator can mask it — use a real
    parser for full fidelity. Tracking ``<>`` fixes the common false positive: a single-declarator
    ``export const x: Generic<A, B> = …`` is overwhelmingly more common than that comparison case."""
    depth = 0
    for ch in s:
        if ch in "([{<":
            depth += 1
        elif ch in ")]}>":
            depth = max(0, depth - 1)
        elif ch == "," and depth == 0:
            return True
    return False


def enumerate_exports(
    base: Path,
    layer: str,
    *,
    extensions: frozenset[str],
    rules: tuple[tuple[re.Pattern[str], str | None], ...] = JS_EXPORT_RULES,
    marker: str = "export",
    root: Path | None = None,
    skip_dirs: frozenset[str] = _SKIP_DIRS,
) -> list[dict[str, str]]:
    """SYMBOL extractor floor for a layer with no available parser (the F1b case). Walks
    ``extensions`` files under ``base``; for each statement-leading ``marker`` line the FIRST
    matching (regex, kind) rule emits {id: group('id'), kind, file}. kind None = recognized but
    not indexed. A ``marker`` line matching NO rule RAISES MapError — that raise IS the
    completeness guarantee: a form the rule set forgot fails the gate loudly instead of
    vanishing (stronger than a parsed-vs-keyword count check, which cannot name the offender).

    ``file`` is POSIX-relative to ``root``. Ceilings (documented, not silent): comments are
    stripped naively (``/* */`` spans and trailing ``//``), and only statement-leading markers
    are scanned — a ``marker`` inside a multi-line template literal would false-positive RAISE
    (fail-closed direction) and a multi-name ``export { a, b }`` is recognized-not-indexed
    (the names are indexed at their def sites). Use a real parser (tsc/tree-sitter) for full
    fidelity; this is the stdlib floor."""
    root = root or repo_root()
    if not base.is_dir():
        raise MapError(f"{layer}: expected directory missing: {base}")
    marker_re = re.compile(rf"^\s*{re.escape(marker)}\b")
    out: list[dict[str, str]] = []
    for dirpath, dirnames, files in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in sorted(files):
            if not any(name.endswith(ext) for ext in extensions):
                continue
            path = Path(dirpath) / name
            rel = path.relative_to(root).as_posix()
            # ONE pass, and the line count is preserved for the reason the old two-pass version
            # gave: removing a multi-line span must never MERGE two statements onto one line,
            # which would push a then-non-leading export out of the statement-leading scan.
            # The `//` split that used to live in the loop is GONE — comments are already blanked,
            # and splitting again would truncate at a `//` inside a string literal.
            text = render_comment_free(path.read_text(encoding="utf-8"))
            for raw in text.splitlines():
                line = raw
                if not marker_re.match(line):
                    continue
                stripped = line.strip()
                for pattern, kind in rules:
                    match = pattern.match(stripped)
                    if match:
                        if kind == "const-export" and _has_top_level_comma(stripped):
                            raise MapError(
                                f"{layer}: {rel}: unmodelled multi-declarator export (capturing only "
                                f"the first name is the green-by-absence hole — split it or use a real "
                                f"parser): {stripped!r}"
                            )
                        if kind is not None:
                            out.append({"id": match.group("id"), "kind": kind, "file": rel})
                        break
                else:
                    raise MapError(
                        f"{layer}: {rel}: unmodelled '{marker}' form (add a rule or use a real "
                        f"parser — a silent skip is the green-by-absence hole): {stripped!r}"
                    )
    return out


# ======================================================================================
# Reuse-convergence shared primitives (tokens · stems · fan-in)
# ======================================================================================
#
# The recall/collision math, written ONCE and shared by reuse_lookup.py (S3, behaviour->seam
# lookup) and map_diff --converge (S5, shipped-reinvention detector). If these lived in either
# CLI the other would reinvent them — the exact drift this whole tool exists to kill. Pure,
# stdlib, deterministic. NONE of this is committed to an artifact: fan-in restales a file on
# nearly every commit (that is why symbols.json is {id,kind,file}-only), so it is computed on
# demand OUTSIDE the freshness gate.

#: default fan-in at/above which a symbol counts as a reusable "seam" (referenced from >= this
#: many distinct files). Override per repo as SEAM_FANIN_THRESHOLD in .codebase-map.conf.
SEAM_FANIN_THRESHOLD_DEFAULT = 3

#: english glue dropped from a stem set so it never drives a match/collision.
_STOPWORDS = frozenset(
    {"a", "an", "the", "to", "of", "in", "on", "for", "and", "or", "is", "be", "as",
     "at", "by", "from", "into", "with", "it", "this", "that"}
)

#: crude single-strip suffixes, LONGEST-first (so `slugify` -> `slug` via `ify`, never via `y`).
#: A documented crude-stemmer ceiling: no external NLP, so it won't unify irregular plurals or
#: synonyms — that is the agent-read's job (S3), not this lexical shortlist's.
_STEM_SUFFIXES = tuple(
    sorted(
        {"ations", "ization", "isation", "ation", "izing", "ising", "ing", "ings",
         "able", "ible", "ment", "ness", "tion", "sion", "ize", "ise", "ify",
         "ers", "ors", "er", "or", "ed", "es", "s", "e"},
        key=len,
        reverse=True,
    )
)

#: camelCase / snake / kebab / path / digit boundary splitter — `getUserID` -> [get,user,id],
#: `api/x/route.ts` -> [api,x,route,ts], `slugify` -> [slugify]. `[A-Z]+(?![a-z])` keeps an
#: acronym run (`HTTPServer` -> [http, server]) instead of shredding it.
_SUBTOKEN_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z]*|[a-z]+|[0-9]+")


def subtokens(text: str) -> list[str]:
    """Lowercase word pieces of an identifier, key, or free-text phrase, split on camelCase,
    snake_case, kebab, path (`/` `.`), and digit boundaries. The single tokenizer behind both
    the recall corpus (S3) and the collision stem-compare (S5)."""
    return [t.lower() for t in _SUBTOKEN_RE.findall(text)]


def _stem(word: str) -> str:
    for suf in _STEM_SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[: -len(suf)]
    return word


def stems(text: str) -> frozenset[str]:
    """Stem set of any identifier, key, or behaviour query. Two strings SHARE A TOKEN STEM iff
    their stem sets intersect — the one definition of "lexically related" used by the lookup
    shortlist AND the --converge collision check, so a match means the same thing in both.
    Stopwords + 1-char tokens dropped; each subtoken crudely stemmed (see _STEM_SUFFIXES)."""
    return frozenset(
        _stem(t) for t in subtokens(text) if t not in _STOPWORDS and len(t) >= 2
    )


_IDENT_TOKEN_RE = re.compile(r"[A-Za-z_$][\w$]*")


#: Per-language lexical PROFILE — the sole declaration of the field set (TOOL-aLexedStripper-1 §4,
#: seventh field by TOOL-aLexedStripper-6). Fields, in order:
#:   line_markers             tokens opening a comment that runs to end of line
#:   marker_needs_word_start  whether a marker opens a comment ONLY at line start or after space
#:   block_pair               the block-comment open/close pair, or None
#:   quote_chars              characters opening a single-line string
#:   triple_quoted            whether ''' and \"\"\" open a multi-line string
#:   backtick_is_string       whether a backtick opens a string whose content is NOT code
#:   interpolation_pair       open/close tokens whose BODY is code, or None
#: `marker_needs_word_start` is shell-only: `$#` is the argument count and `${p#/opt/}` is a prefix
#: strip, and treating either as a comment deletes the rest of the line. Backtick is NOT a string in
#: shell, where it opens command substitution and the content IS code. `interpolation_pair` is what
#: lets one rule cover a JS template's `${…}` and a Python f-string's `{…}`; the Python row applies
#: it only inside a string whose prefix carries `f`.
_PROFILE_C = (("//",), False, ("/*", "*/"), ("'", '"'), False, True, ("${", "}"))
_PROFILE_PY = (("#",), False, None, ("'", '"'), True, False, ("{", "}"))
_PROFILE_SH = (("#",), True, None, ("'", '"'), False, False, None)

_LEX_PROFILES = {}
for _e in (".js .jsx .mjs .cjs .ts .tsx .c .h .cc .cpp .hpp .java .go .rs .cs .swift .kt "
           ".scala .php").split():
    _LEX_PROFILES[_e] = _PROFILE_C
for _e in (".py", ".pyi"):
    _LEX_PROFILES[_e] = _PROFILE_PY
for _e in ".sh .bash .zsh .toml .yaml .yml .cfg .ini .conf".split():
    _LEX_PROFILES[_e] = _PROFILE_SH

_TRIPLE_QUOTES = ('"""', "'''")
#: String prefix letters Python allows before a quote. Only `f` (any case) turns the
#: `interpolation_pair` on, but all of them have to be RECOGNISED so `rf"…"` is still seen as
#: f-prefixed and `b"…"` is not.
_PY_PREFIX_CHARS = "rRbBuUfF"


def _identifier_tokens(source: str, suffix: str = "") -> set[str]:
    """Distinct identifier tokens in a source file's CODE, with comments and string CONTENT removed
    by ONE left-to-right pass over the lexical profile for ``suffix``.

    A regex chain cannot express that comments and strings EXCLUDE each other, and whichever it
    strips first wins. The three regexes this replaced applied C syntax to every language, so a
    ``/*`` inside a Python docstring opened a comment running to the next ``*/`` (measured: 674
    lines swallowed, one file down to 18.8% recall against ``tokenize`` ground truth), a ``//``
    truncated a line of floor division, and a ``#`` truncated a line of TypeScript.

    An UNDECLARED suffix strips NOTHING and returns every token. Over-counting is this scan's
    documented fail-open direction — it feeds a RANKING and a WARN, never a gate — and guessing a
    comment syntax is exactly how the old chain got here.

    A multi-line construct left UNTERMINATED at EOF is ABANDONED, the pass resuming just after the
    opener, so an odd backtick cannot reproduce the same swallow this function exists to remove.
    """
    prof = _LEX_PROFILES.get(suffix)
    if prof is None:
        return set(_IDENT_TOKEN_RE.findall(source))
    markers, word_start, block, quotes, triple, backtick, interp = prof
    out: list[str] = []
    i, n = 0, len(source)

    def _string(start: int, delim: str, multiline: bool, interpolate: bool) -> int:
        """Consume a string opened at ``start`` by ``delim``. Text is blanked; an interpolation body
        is COPIED, because it holds real code. Returns the index just past the close, or past the
        opener when the literal is unterminated (the abandon rule)."""
        j = start + len(delim)
        while j < n:
            if source[j] == "\\":
                j += 2
                continue
            if interpolate and source.startswith(interp[0], j):
                if source.startswith(interp[0] * 2, j) and interp[0] == "{":
                    j += 2  # `{{` is a literal brace and opens nothing
                    continue
                k = j + len(interp[0])
                depth = 0
                body = []
                closed = False
                while k < n:
                    c = source[k]
                    # A brace inside a NESTED STRING is text, not structure. Counting it inflated the
                    # depth so the real closer never matched, and the walk ran on past the literal
                    # consuming comments and string bodies as code -- the over-capture direction of
                    # the same defect this scanner exists to remove. Measured: `{` inside a quoted
                    # argument leaked a following comment's prose into the index.
                    if c in quotes:
                        e = k + 1
                        while e < n and source[e] != c:
                            if source[e] == chr(92):
                                e += 2
                                continue
                            if source[e] == chr(10):
                                break
                            e += 1
                        if e < n and source[e] == c:
                            body.append(" " * (e - k + 1))
                            k = e + 1
                            continue
                    if c == interp[0][-1]:
                        depth += 1
                    elif c == interp[1]:
                        if depth == 0:
                            closed = True
                            break
                        depth -= 1
                    body.append(c)
                    k += 1
                # An interpolation that never closes is TEXT, not code. Emitting the body anyway
                # walked to EOF and leaked the whole rest of the file into the index as identifiers
                # -- the over-capture direction of the same defect this scanner exists to remove.
                out.append(" " + "".join(body) + " " if closed else " ")
                j = k + 1 if closed else k
                continue
            if not multiline and source[j] == "\n":
                return j  # a single-line literal never crosses its line
            if source.startswith(delim, j):
                return j + len(delim)
            j += 1
        return start + len(delim)  # unterminated: abandon, rescan from just after the opener

    while i < n:
        ch = source[i]
        if block and source.startswith(block[0], i):
            j = source.find(block[1], i + len(block[0]))
            i = i + len(block[0]) if j < 0 else j + len(block[1])
            out.append(" ")
            continue
        hit = next((m for m in markers if source.startswith(m, i)), None)
        if hit and (not word_start or i == 0 or source[i - 1].isspace()):
            j = source.find("\n", i)
            i = n if j < 0 else j
            out.append(" ")
            continue
        if ch in quotes or (backtick and ch == "`"):
            # Python string prefixes sit immediately before the quote; `f` (any case) turns on the
            # replacement field. A prefix run is at most a few letters and is already in ``out``.
            # The prefix run is a PYTHON construct, so it is read only for a profile that has
            # them. Running it for the C family cost nothing but said the opposite of what it meant.
            fstring = False
            if triple:
                k = i - 1
                pre = ""
                while k >= 0 and source[k] in _PY_PREFIX_CHARS:
                    pre = source[k] + pre
                    k -= 1
                fstring = "f" in pre.lower()
            if triple and any(source.startswith(d, i) for d in _TRIPLE_QUOTES):
                d = source[i : i + 3]
                i = _string(i, d, True, bool(interp) and fstring)
            elif ch == "`":
                i = _string(i, "`", True, bool(interp))
            else:
                i = _string(i, ch, False, bool(interp) and fstring)
            out.append(" ")
            continue
        out.append(ch)
        i += 1
    return set(_IDENT_TOKEN_RE.findall("".join(out)))


def build_reference_index(
    files: list[str], *, root: Path | None = None, skip_dirs: frozenset[str] = _SKIP_DIRS
) -> dict[str, set[str]]:
    """token -> {POSIX files mentioning it as an identifier}, scanned over the covered-layer
    source: the top-level dirs of ``files`` (a symbols.json file list), filtered to their
    extension set. This is the on-demand scan behind fan_in — NEVER committed. Fail-open by
    design on an unreadable file (skipped): this feeds a RANKING/WARN, not a gate, so a binary
    blob must not abort the lookup (the opposite of the extractor law, and deliberately so)."""
    root = root or repo_root()
    roots = sorted({f.split("/", 1)[0] for f in files if f})
    exts = frozenset(Path(f).suffix for f in files if Path(f).suffix)
    index: dict[str, set[str]] = {}
    for top in roots:
        base = root / top
        if not base.is_dir():
            continue
        for dirpath, dirnames, names in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in skip_dirs]
            for name in sorted(names):
                if exts and Path(name).suffix not in exts:
                    continue
                path = Path(dirpath) / name
                try:
                    text = path.read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue
                rel = path.relative_to(root).as_posix()
                for tok in _identifier_tokens(text, path.suffix):
                    index.setdefault(tok, set()).add(rel)
    return index


def fan_in(index: dict[str, set[str]], symbol_id: str, def_file: str) -> int:
    """Distinct files referencing ``symbol_id`` as an identifier, minus its own def file (the
    data-model definition). An import/identifier-scoped HEURISTIC, not a resolved call graph
    (§3 non-goal): over-counts a common id (`get`), under-counts registry/dynamic dispatch — a
    documented recall FLOOR used for ranking + a review WARN, never gated."""
    return len(index.get(symbol_id, set()) - {def_file})


def reference_index_for(
    files: list[str], *, root: Path | None = None, extensions: frozenset[str] | None = None
) -> dict[str, set[str]]:
    """Reference index (token -> {POSIX files}) over an EXACT file list, NOT their whole dirs.
    When ``extensions`` is given, only files with those suffixes are scanned (the covered code
    layers) — so a non-code file in the range (a .md that merely names a symbol) cannot register a
    spurious edge, mirroring build_reference_index's extension filter.
    build_reference_index walks a whole layer for corpus-wide fan-in; this indexes only the
    files given — the range-scoped scan behind --converge's "did the range wire through this
    seam?" test (fan_in over THIS index > 0 = an edge was added by the range). Same fail-open
    law: an unreadable/absent file (a deletion in the range) is skipped, never a crash — it
    feeds a WARN, not a gate."""
    root = root or repo_root()
    index: dict[str, set[str]] = {}
    for raw in files:
        rel = raw.replace("\\", "/")
        if extensions is not None and Path(rel).suffix not in extensions:
            continue
        try:
            text = (root / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for tok in _identifier_tokens(text, Path(rel).suffix):
            index.setdefault(tok, set()).add(rel)
    return index


def seam_fanin_threshold(root: Path | None = None) -> int:
    """The configured seam fan-in threshold (SEAM_FANIN_THRESHOLD in .codebase-map.conf),
    default SEAM_FANIN_THRESHOLD_DEFAULT. Shared by the lookup (hot-seam ranking) and --converge
    (collision detection) so the two agree on what "a seam" is."""
    raw = load_conf(root).get("SEAM_FANIN_THRESHOLD")
    if not raw:
        return SEAM_FANIN_THRESHOLD_DEFAULT
    try:
        n = int(raw)
    except ValueError as exc:
        raise MapError(f"SEAM_FANIN_THRESHOLD must be an integer, got {raw!r}") from exc
    if n < 1:
        raise MapError(f"SEAM_FANIN_THRESHOLD must be >= 1, got {n}")
    return n


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
    # fnmatch treats [] as a character class, so a literal Next-style segment like [id] NEVER
    # matches its own path — require the [[] escape (which fnmatch reads as a literal '[').
    bracketed = [g for g in globs if "[" in g.replace("[[]", "").replace("[]]", "")]
    if bracketed:
        raise MapError(
            f"{source}: '[' in a glob is an fnmatch character class, not a literal — escape "
            f"as [[]id[]] (or drop the segment for a broader glob): {bracketed}"
        )

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


def load_dossier_texts(map_dir: Path) -> dict[str, str]:
    """{feature -> raw dossier markdown} for FOUNDATION.md + every features/*.md — the prose half,
    read WITHOUT parsing the toml claims (so it needs no inventory_ids and survives a claim-shape
    error). The shared reader for the recall corpus (reuse_lookup S3) and the closing loop's
    affordance cross-check + coverage hint (map_diff --converge S5) — one loader, not two."""
    texts: dict[str, str] = {}
    foundation = map_dir / "FOUNDATION.md"
    if foundation.is_file():
        texts["foundation"] = foundation.read_text(encoding="utf-8")
    features = map_dir / "features"
    if features.is_dir():
        for path in sorted(features.glob("*.md")):
            texts[path.stem] = path.read_text(encoding="utf-8")
    return texts


# ======================================================================================
# Affordance — the forward reuse menu (graced presence check, NOT a keyed inventory)
# ======================================================================================
#
# Every non-exempt dossier must carry a `## Reuse affordance` section that forces the reuse
# decision: list the seams this feature is reused THROUGH, or state `none — <why>`. PRESENCE is
# gated here; content QUALITY (does the id resolve? is the reason sound?) is the un-gatable
# ceiling — reported later as affordance_coverage_% (S5), never a merge blocker. The delimiter
# (-/–/—) and every clause after the id are free: only the `seam:` prefix + first id token are
# load-bearing, so a graced dossier can't be gamed by a formatting nit yet a bare heading with no
# block still fails (a decision was dodged).


@dataclass(frozen=True)
class Affordance:
    seams: tuple[str, ...]      # seam ids, in document order (first token after `seam:`)
    is_none: bool               # an explicit `none — <why feature-specific>` declaration
    heading_present: bool       # the `## Reuse affordance` heading exists

    @property
    def has_block(self) -> bool:
        """A decision was recorded: at least one `seam:` line, or the `none` declaration."""
        return bool(self.seams) or self.is_none


_SEAM_RE = re.compile(r"^seam:\s*(?P<id>\S+)")
_NONE_RE = re.compile(r"^none\b")


def parse_affordance(text: str) -> Affordance:
    """Parse a dossier's `## Reuse affordance` section: ALL leading consecutive `seam:` lines
    (`seam: <id> — reuse for <need>; extend via <point>`) or the single `none — <why>` line. The
    block ends at the first blank/non-matching line (so trailing prose or the next heading stops
    it). Keys on the `seam:` prefix + first id token ONLY — delimiter and trailing clauses are
    free (review #20). A malformed block is still a block (a presence-pass, an
    affordance_coverage_% miss) — content is judged elsewhere, never here."""
    lines = text.splitlines()
    try:
        i = next(k for k, ln in enumerate(lines) if ln.strip() == AFFORDANCE_HEADING)
    except StopIteration:
        return Affordance(seams=(), is_none=False, heading_present=False)
    j = i + 1
    while j < len(lines) and not lines[j].strip():  # skip the blank line(s) after the heading
        j += 1
    seams: list[str] = []
    is_none = False
    while j < len(lines):
        s = lines[j].strip()
        if not s:
            break  # a blank line ends the leading run
        if m := _SEAM_RE.match(s):
            seams.append(m.group("id"))
        elif _NONE_RE.match(s):
            is_none = True
            break
        else:
            break  # any other prose ends the block
        j += 1
    return Affordance(seams=tuple(seams), is_none=is_none, heading_present=True)


def load_affordance_exempt(root: Path | None = None, *, source: str = "affordance-exempt.toml") -> frozenset[str]:
    """The shrink-only affordance grace list — feature names that predate the `## Reuse
    affordance` section and are skipped by the graced presence check. Absent file = no grace
    (every dossier must carry the section — the fresh-repo default). Fail-closed on a malformed
    file: a wrong shape must break the gate, never silently un-exempt (or over-exempt) the fleet."""
    path = map_root(root) / "affordance-exempt.toml"
    if not path.is_file():
        return frozenset()
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise MapError(f"{source}: toml parse error: {exc}") from exc
    names = data.get("exempt")
    if set(data) - {"exempt"} or not isinstance(names, list) or not all(isinstance(n, str) and n for n in names):
        raise MapError(f"{source}: expected exactly `exempt = [<feature>...]` of non-empty strings")
    return frozenset(names)


def render_affordance_exempt(names) -> str:
    """Hand-rendered TOML for the shrink-only affordance grace list (sorted, deduped) — the same
    stdlib-has-no-writer pattern as render_baseline. Seeded from existing dossiers at adoption
    (`gen_map.py --seed-affordance-baseline`); only shrinks thereafter."""
    lines = [
        "# affordance-exempt.toml — the shrink-only affordance grace list (codebase-map kit).",
        "# Dossiers here predate the '## Reuse affordance' section; the graced presence check skips",
        "# them. SHRINK-ONLY: a new dossier is NEVER added, a touch drops entries (map_diff",
        "# attribution), and a dossier that gains the section is removed. Seeded at adoption.",
        "",
    ]
    uniq = sorted(set(names))
    if not uniq:
        lines.append("exempt = []")
    else:
        lines.append("exempt = [")
        lines.extend(f"  {json.dumps(n, ensure_ascii=False)}," for n in uniq)
        lines.append("]")
    return "\n".join(lines) + "\n"


def affordance_offenders(dossier_texts: dict[str, str], exempt) -> list[str]:
    """Feature names whose dossier lacks a required affordance block. A dossier in the
    (shrink-only) exempt set is skipped; every other must carry AFFORDANCE_HEADING with at least
    one `seam:` line or a `none` declaration under it. Pure over {feature: text} so the gate and
    selftest drive it identically — the gate reads the tree off disk, this judges the texts."""
    return [
        feature
        for feature in sorted(dossier_texts)
        if feature not in exempt and not parse_affordance(dossier_texts[feature]).has_block
    ]


def drop_touched_exemptions(exempt, touched) -> frozenset[str]:
    """S4a — the touch-triggered backfill rule: shrink the affordance-exempt set by every feature
    a `map_diff` range TOUCHED (i.e. every attribution owner). Touching a feature's files drops
    its grace MECHANICALLY, so the next gate run demands its `## Reuse affordance` block with no
    human remembering (review #5/#32). ``touched`` is a map_diff attribution result (owner ->
    paths) or any iterable of feature names; ``foundation``/``UNMAPPED`` are never in the exempt
    list, so passing the whole attribution dict is safe.

    ponytail: the S4a rule is exactly this set difference — the machinery is attribute_paths."""
    return frozenset(exempt) - set(touched)


# ======================================================================================
# Closing loop — shipped-reinvention detector + backlog routing (S5, pure)
# ======================================================================================
#
# The other half of convergence: S1–S4 help new work FIND a seam; this catches reinvention that
# shipped anyway. A collision = a NEW exported symbol whose id shares a token stem with an
# EXISTING high-fan-in seam of the SAME kind that the range did NOT wire through (no reference
# edge added to it) — a machine proxy for "built new instead of reusing", computed over ALL new
# code so skipping the S3 lookup can't hide it. A soft force: a review WARN routed to the
# reinvention backlog, NEVER a hard gate (a token-stem collision has real false positives — a
# legitimately-new same-named symbol — and a hard gate on it trains --no-verify, §3).


@dataclass(frozen=True)
class CollisionFlag:
    new: str          # the new symbol id (S) — the shipped reinvention
    resembles: str    # the existing seam id (E) it collides with and did not wire through
    file: str         # S's def file — where the parallel implementation landed
    fanin: int        # E's fan-in — how reused the seam S ignored is
    kind: str         # the shared symbol kind (the F8b structural signal: same kind required)
    confidence: str   # "high" if E DECLARES a ## Reuse affordance seam (F8c), else "medium"


def detect_collisions(
    new_symbols: list[dict[str, str]],
    base_symbols: list[dict[str, str]],
    ref_index: dict[str, set[str]],
    range_index: dict[str, set[str]],
    *,
    threshold: int,
    affordance_seams: frozenset[str] = frozenset(),
) -> list[CollisionFlag]:
    """S5 closing loop (pure, deterministic). For each NEW symbol S, flag it iff it collides with
    some EXISTING seam E where: E is the SAME kind (F8b structural signal); stem(S) & stem(E) is
    non-empty (the one "shares a token stem" definition, shared with the S3 lookup); E's corpus
    fan-in >= threshold (E is a real seam — ``ref_index`` is the whole-corpus scan); and the range
    added NO reference edge to E (``fan_in(range_index, E) == 0`` — ``range_index`` is the
    range-scoped scan, so a range that DID wire through E is not a collision). One flag per new
    symbol, pointing at its strongest resemblance (highest fan-in; an affordance-declaring seam
    breaks ties and raises confidence). Sorted fan-in desc, then new/resembles id.

    ``base_symbols`` (present at range base) is the seam POOL: a seam must have existed to be
    reinvented. ``new_symbols`` = head rows absent from base (all public — the extractors already
    drop private names, so every kind here is an export). A malformed/empty stem yields no flag."""
    seams_by_kind: dict[str, list[dict[str, str]]] = {}
    for e in base_symbols:
        seams_by_kind.setdefault(e["kind"], []).append(e)

    flags: list[CollisionFlag] = []
    for s in new_symbols:
        s_stems = stems(s["id"])
        if not s_stems:
            continue
        best: tuple[int, bool, dict[str, str]] | None = None
        for e in seams_by_kind.get(s["kind"], ()):
            if e["id"] == s["id"] and e["file"] == s["file"]:
                continue  # an identical row is not "new vs existing"
            if not (s_stems & stems(e["id"])):
                continue
            fe = fan_in(ref_index, e["id"], e["file"])
            if fe < threshold:
                continue  # E is not a seam — below the reuse threshold
            # "Wired through" = the NEW symbol's OWN file references E — scoped to s["file"], not
            # the whole range (an unrelated changed file's edge to E must not mask S's reinvention),
            # and ONLY when the ids differ: a same-id row's occurrence in its own file is its
            # definition, never an edge to the same-named seam (else a verbatim same-name duplicate,
            # the most blatant reinvention, is silently not flagged).
            if s["id"] != e["id"] and s["file"] in range_index.get(e["id"], ()):
                continue  # S's file genuinely references E -> extension/wrap, not reinvention
            declared = e["id"] in affordance_seams
            if best is None or (fe, declared) > (best[0], best[1]):
                best = (fe, declared, e)
        if best is not None:
            fe, declared, e = best
            flags.append(
                CollisionFlag(
                    new=s["id"], resembles=e["id"], file=s["file"], fanin=fe,
                    kind=s["kind"], confidence="high" if declared else "medium",
                )
            )
    flags.sort(key=lambda f: (-f.fanin, f.new, f.resembles))
    return flags


_BACKLOG_PREAMBLE = (
    "# Reinvention backlog — codebase-map --converge (codebase-map kit)\n"
    "\n"
    "Shipped-reinvention WARNs from `map_diff --converge`: a NEW exported symbol whose id shares a\n"
    "token stem with an existing high-fan-in seam of the same kind that it did NOT wire through.\n"
    "Each row is a consolidation CANDIDATE, not a verdict — a token-stem collision has false\n"
    "positives (a legitimately-new same-named symbol). Burn down: fold `new` into `resembles`, or\n"
    "delete the row if the two are genuinely distinct. Append-only + deduped by (new, resembles);\n"
    "never a merge gate.\n"
    "\n"
    "| new | resembles | file | seam fan-in | kind | confidence |\n"
    "|---|---|---|---|---|---|\n"
)


def backlog_keys(text: str) -> set[tuple[str, str]]:
    """The (new, resembles) pairs already recorded in a reinvention-backlog file — its table rows,
    for append-time dedup. Tolerant of the header/separator/prose: a data row is a `| a | b | ...`
    line whose first cell is a real id (not `new`, not a `---` separator)."""
    keys: set[tuple[str, str]] = set()
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")][1:-1]  # drop the outer-pipe empties
        if len(cells) < 2 or not cells[0] or cells[0] == "new" or set(cells[0]) == {"-"}:
            continue
        keys.add((cells[0], cells[1]))
    return keys


def append_backlog(text: str, flags: list[CollisionFlag]) -> tuple[str, list[CollisionFlag]]:
    """F7: append each collision flag to the reinvention-backlog text, deduped by (new, resembles)
    — a durable, reviewable worklist. APPEND-ONLY: an existing row is never rewritten or removed
    (humans burn it down); a re-run of --converge on the same range adds nothing. Returns the new
    text and the flags actually appended (empty -> caller writes nothing). Seeds the header +
    table when the file is empty/new."""
    seen = backlog_keys(text)
    added: list[CollisionFlag] = []
    for f in flags:
        key = (f.new, f.resembles)
        if key in seen:
            continue
        seen.add(key)
        added.append(f)
    if not added:
        return text, []
    body = text if text.strip() else _BACKLOG_PREAMBLE
    if not body.endswith("\n"):
        body += "\n"
    rows = "".join(
        f"| {f.new} | {f.resembles} | {f.file} | {f.fanin} | {f.kind} | {f.confidence} |\n"
        for f in added
    )
    return body + rows, added


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

#: LEGACY, and the only hardcoded spelling left: the regen command for a ROOT install. Nothing in
#: this kit reads it — use ``regen_cmd()``, which is prefix-correct. It survives because a
#: ``GATE_FILE`` installed before 1.1 references ``m.REGEN_CMD``, and an installed gate is
#: project-owned: the maintenance rule overwrites ENGINE files, never GATE_FILE, so removing this
#: would break those gates on an ordinary engine update. The selftest pins it EQUAL to
#: ``regen_cmd()``'s root-install answer, so the two spellings cannot drift apart.
REGEN_CMD = "python codebase-map/gen_map.py --write"


def render_inventories_json(inventories: dict[str, list[str]], inventory_ids: tuple[str, ...]) -> str:
    # Keys-only on purpose: pure dossier/claim edits must never stale this artifact.
    doc = {
        "$generator": f"codebase-map@{KIT_CODEBASE_MAP_VERSION}",
        "$comment": f"generated by {kit_rel()}/gen_map.py — do not hand-edit; regen: {regen_cmd()}",
        "inventories": {k: sorted(inventories[k]) for k in inventory_ids},
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def render_symbols_json(symbols: list[dict[str, str]]) -> str:
    """The SYMBOL recall index: {id, kind, file} rows, ids sorted, POSIX paths, LF — so it is
    byte-deterministic across a Windows and a Linux run, exactly like inventories.json, and the
    freshness gate can byte-compare two renders. id/kind/file ONLY: NO fan-in (that would
    restale the artifact on nearly every commit — fan-in is computed on demand in the lookup /
    --converge). Fail-closed: a wrong-shape row, an unknown kind, or a backslash path RAISES —
    the byte-compare gate runs the SAME renderer twice so it cannot catch a fail-open producer;
    the shape is validated HERE."""
    rows: list[dict[str, str]] = []
    for s in symbols:
        if not isinstance(s, dict) or set(s) != {"id", "kind", "file"}:
            raise MapError(f"symbols.json: each symbol needs exactly id/kind/file: {s!r}")
        if not all(isinstance(s[k], str) and s[k] for k in ("id", "kind", "file")):
            raise MapError(f"symbols.json: id/kind/file must be non-empty strings: {s!r}")
        if s["kind"] not in SYMBOL_KINDS:
            raise MapError(f"symbols.json: unknown kind {s['kind']!r} (want {sorted(SYMBOL_KINDS)}): {s!r}")
        if "\\" in s["file"]:
            raise MapError(f"symbols.json: file must be POSIX (forward-slash): {s['file']!r}")
        rows.append({"id": s["id"], "kind": s["kind"], "file": s["file"]})
    rows.sort(key=lambda r: (r["id"], r["file"], r["kind"]))
    doc = {
        "$generator": f"codebase-map@{KIT_CODEBASE_MAP_VERSION}",
        "$comment": f"generated by {kit_rel()}/gen_map.py — do not hand-edit; regen: {regen_cmd()}",
        "symbols": rows,
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
    only, NO timestamps (determinism is what makes the freshness gate possible).

    The header's ``kit_rel()``/``regen_cmd()`` are NOT a timestamp-style input: the install prefix
    is a property of the repo being rendered, identical on every machine and both platforms
    (POSIX-joined), so the byte-compare still holds. A ``CODEBASE_MAP_ROOT`` pointing outside the
    kit falls back to the bare dir name, which is why fixture renders stay stable too."""
    idx = claimant_index(inventories, owners, baseline)
    counts = " · ".join(f"{k}: {len(inventories[k])}" for k in inventory_ids)
    lines: list[str] = [
        f"<!-- codebase-map@{KIT_CODEBASE_MAP_VERSION} · generated by {kit_rel()}/gen_map.py — do not hand-edit; regen: {regen_cmd()} -->",
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
