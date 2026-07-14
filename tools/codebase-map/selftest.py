"""codebase-map kit self-test — exercises the pure engine with fixtures (stdlib only).

    python codebase-map/selftest.py        # exit 0 = the kit's contract holds

These are the red-path proofs: an unclaimed key, a stale claim, a stale/lazy baseline line,
and every malformed-dossier class must FAIL LOUD; multi-claim, case-sensitivity, and
backslash normalization must behave identically on every platform.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import map_lib as m  # noqa: E402

IDS = ("flags", "routes")
INV = {"flags": ["a_flag", "b_flag"], "routes": ["api/x/route.ts"]}
EMPTY_BASE: dict[str, tuple[str, ...]] = {k: () for k in IDS}

DOSSIER = """# x
```toml
feature = "x"
title = "X"
status = "shipped"
streams = ["core"]
decisions = ["REC-someSlug-1"]

[claims]
flags = ["a_flag"]
routes = []

[paths]
globs = ["src/x/**"]
```
"""


def claims(**over):
    return {k: () for k in IDS} | over


def check(name, fn):
    try:
        fn()
        print(f"ok   {name}")
        return 0
    except AssertionError as exc:
        print(f"FAIL {name}: {exc}")
        return 1


def expect_maperror(text_mutation, needle):
    try:
        m.parse_dossier(text_mutation, IDS, source="t")
    except m.MapError as exc:
        assert needle in str(exc), f"wrong error: {exc}"
        return
    raise AssertionError(f"parsed but should have failed ({needle!r})")


def t_coverage_directions():
    cov = m.compute_coverage(INV, {"x": claims(flags=("a_flag",))}, EMPTY_BASE)
    assert cov.unclaimed == {"flags": ["b_flag"], "routes": ["api/x/route.ts"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "dead"))},
        EMPTY_BASE | {"flags": ("b_flag",), "routes": ("api/x/route.ts",)},
    )
    assert cov.stale_claims == {"flags": ["x: dead"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "b_flag"), routes=("api/x/route.ts",))},
        EMPTY_BASE | {"flags": ("gone", "b_flag")},
    )
    assert cov.stale_baseline == {"flags": ["gone"]}
    assert cov.lazy_baseline == {"flags": ["b_flag"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "b_flag"), routes=("api/x/route.ts",)), "y": claims(flags=("a_flag",))},
        EMPTY_BASE,
    )
    assert cov.clean  # multi-claim legal


def t_parse_contract():
    d = m.parse_dossier(DOSSIER, IDS, source="t")
    assert d.feature == "x" and d.claims["flags"] == ("a_flag",)
    expect_maperror(DOSSIER.replace("```toml", "```"), "no ```toml fence")
    expect_maperror(DOSSIER.replace("routes = []", ""), "missing")
    expect_maperror(DOSSIER.replace("routes = []", "routes = []\nrouts = []"), "unknown")
    expect_maperror(DOSSIER.replace('status = "shipped"', 'status = "done"'), "status")
    expect_maperror(DOSSIER.replace('title = "X"', "title = 3"), "title")
    expect_maperror(DOSSIER.replace("REC-someSlug-1", "rec_bad"), "grammar")
    expect_maperror(DOSSIER.replace("src/x/**", "src\\\\x"), "forward-slash")


def t_attribution():
    d = m.parse_dossier(DOSSIER, IDS, source="t")
    f = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "foundation"').replace("src/x/**", "lib/**"),
        IDS,
        source="f",
    )
    tree = m.MapTree(foundation=f, dossiers=(d,), baseline=EMPTY_BASE)
    out = m.attribute_paths(["src\\x\\a.ts", "lib/b.ts", "Other/c.ts", "SRC/x/a.ts"], tree)
    assert out["x"] == ["src/x/a.ts"]  # backslash normalized
    assert out["foundation"] == ["lib/b.ts"]
    assert sorted(out["UNMAPPED"]) == ["Other/c.ts", "SRC/x/a.ts"]  # case-sensitive everywhere
    import re

    keyed = ((re.compile(r"^db/migrations/([0-9a-f]+)_"), "flags"),)
    d2 = m.parse_dossier(DOSSIER.replace('flags = ["a_flag"]', 'flags = ["abc123"]'), IDS, source="t")
    tree2 = m.MapTree(foundation=f, dossiers=(d2,), baseline=EMPTY_BASE)
    out2 = m.attribute_paths(["db/migrations/abc123_add.sql"], tree2, keyed_attributors=keyed)
    assert out2["x"] == ["db/migrations/abc123_add.sql"]  # keyed attribution wins


def t_renders_round_trip_and_determinism():
    text = m.render_baseline({"flags": ["b", "a"]}, IDS)
    parsed = m.parse_baseline(text, IDS)
    assert parsed["flags"] == ("a", "b") and parsed["routes"] == ()
    owners = {"x": claims(flags=("a_flag",)), "y": claims(flags=("b_flag",))}
    one = m.render_map_md(INV, IDS, owners, EMPTY_BASE)
    # a PERMUTED view must render byte-identically — reversed key lists AND reversed owner
    # insertion order, so this assert actually pins the renderer's own sorting
    permuted_inv = {k: list(reversed(v)) for k, v in INV.items()}
    permuted_owners = dict(reversed(list(owners.items())))
    two = m.render_map_md(permuted_inv, IDS, permuted_owners, EMPTY_BASE)
    assert one == two and "UNCLAIMED" in one and one.endswith("\n")
    j = m.render_inventories_json(permuted_inv, IDS)
    assert j == m.render_inventories_json(INV, IDS)
    assert '"a_flag"' in j and "claimant" not in j  # keys-only artifact
    # the version marker rides both generated artifacts so the deployer can grep the installed version
    marker = "codebase-map@" + m.KIT_CODEBASE_MAP_VERSION
    assert marker in one and marker in j


def t_conf_grammar(tmp: Path):
    (tmp / ".codebase-map.conf").write_text(
        '# c\nMAP_ROOT=docs/map\nGATE_FILE="tests/test map.py"\n'
        "export MAP_DIFF_CMD=python\nBAD=docs/map # inline\n",
        encoding="utf-8",
    )
    conf = m.load_conf(tmp)
    assert conf["MAP_ROOT"] == "docs/map"
    assert conf["GATE_FILE"] == "tests/test map.py"  # quoted value keeps its space
    assert conf["MAP_DIFF_CMD"] == "python"  # export prefix normalized
    assert conf["BAD"] == "docs/map"  # unquoted value ends at whitespace, comment can't leak


def t_glob_brackets_fail_loud_and_escape_works():
    bad = DOSSIER.replace("src/x/**", "src/app/[id]/**")
    try:
        m.parse_dossier(bad, IDS, source="t")
        raise AssertionError("unescaped [ in a glob must fail")
    except m.MapError as exc:
        assert "character class" in str(exc)
    d = m.parse_dossier(DOSSIER.replace("src/x/**", "src/app/[[]id[]]/*"), IDS, source="t")
    f = m.parse_dossier(DOSSIER.replace('feature = "x"', 'feature = "foundation"'), IDS, source="f")
    tree = m.MapTree(foundation=f, dossiers=(d,), baseline=EMPTY_BASE)
    out = m.attribute_paths(["src/app/[id]/page.tsx"], tree)
    assert out["x"] == ["src/app/[id]/page.tsx"]  # the escape matches the literal segment


def t_extractor_helpers_fail_closed(tmp: Path):
    (tmp / "flat").mkdir(parents=True)
    (tmp / "flat" / "a.py").write_text("x", encoding="utf-8")
    assert m.module_inventory(tmp / "flat", "t") == ["a"]
    (tmp / "flat" / "nested").mkdir()
    try:
        m.module_inventory(tmp / "flat", "t")
        raise AssertionError("subpackage escaped the flat walk")
    except m.MapError:
        pass
    try:
        m.json_artifact_inventory(tmp / "missing.json", "t", lambda d: d)
        raise AssertionError("missing artifact did not fail")
    except m.MapError:
        pass
    (tmp / "app" / "admin" / "x").mkdir(parents=True)
    (tmp / "app" / "admin" / "x" / "page.jsx").write_text("x", encoding="utf-8")
    (tmp / "app" / "api").mkdir(parents=True)
    (tmp / "app" / "api" / "route.tsx").write_text("x", encoding="utf-8")
    pages = frozenset({"page.tsx", "page.ts", "page.jsx", "page.js"})
    routes = frozenset({"route.ts", "route.tsx", "route.js", "route.jsx"})
    assert m.walk_dir_keys(tmp / "app" / "admin", pages, "t") == ["x"]  # extension variants seen
    assert m.walk_file_keys(tmp / "app", routes, "t") == ["api/route.tsx"]
    for key in m.walk_file_keys(tmp / "app", routes, "t"):
        assert "\\" not in key  # POSIX keys on every platform


def main() -> int:
    import tempfile

    failures = 0
    failures += check("coverage both directions + ratchet guards", t_coverage_directions)
    failures += check("dossier contract fails loud", t_parse_contract)
    failures += check("attribution: keyed > globs, posix, case-sensitive", t_attribution)
    failures += check("renders deterministic + keys-only + round-trip", t_renders_round_trip_and_determinism)
    failures += check("glob brackets fail loud; [[]-escape matches", t_glob_brackets_fail_loud_and_escape_works)
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "extractor helpers fail closed", lambda: t_extractor_helpers_fail_closed(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("conf restricted grammar", lambda: t_conf_grammar(Path(td)))
    print("PASS" if not failures else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
