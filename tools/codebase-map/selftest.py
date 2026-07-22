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
import reuse_lookup as rl  # noqa: E402

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


def t_symbols_render_deterministic_and_fail_closed():
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.ts"},
        {"id": "Button", "kind": "component", "file": "web/Button.tsx"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    one = m.render_symbols_json(syms)
    two = m.render_symbols_json(list(reversed(syms)))  # input order must not matter
    assert one == two, "symbols render depends on input order (not deterministic)"
    assert one.endswith("\n") and "\\" not in one  # LF-terminated, POSIX paths only
    marker = "codebase-map@" + m.KIT_CODEBASE_MAP_VERSION
    assert marker in one  # version marker rides the artifact
    # ids sorted (ascii: uppercase before lowercase) — the cross-platform byte-match guarantee
    assert one.index('"Button"') < one.index('"Cache"') < one.index('"slugify"')
    # fail-closed shape guards: the freshness gate runs the SAME renderer twice, so it cannot
    # see a fail-open producer — the shape is validated HERE, and every bad row must RAISE.
    for bad, needle in [
        ([{"id": "x", "kind": "widget", "file": "a.ts"}], "unknown kind"),
        ([{"id": "x", "kind": "function"}], "exactly id/kind/file"),
        ([{"id": "", "kind": "function", "file": "a.ts"}], "non-empty"),
        ([{"id": "x", "kind": "function", "file": "a\\b.ts"}], "POSIX"),
    ]:
        try:
            m.render_symbols_json(bad)
            raise AssertionError(f"render accepted a bad row (expected {needle!r})")
        except m.MapError as exc:
            assert needle in str(exc), f"wrong error: {exc}"


def t_symbol_extractors_fail_closed(tmp: Path):
    # --- python_symbols: real parser captures def/class/async/decorated + __all__ ----------
    pkg = tmp / "pkg"
    (pkg / "sub").mkdir(parents=True)
    (pkg / "mod.py").write_text(
        "import functools\n"
        "__all__ = ['slugify', 'CONST']\n"
        "CONST = 1\n"
        "def slugify(s):\n    return s\n"
        "async def fetch():\n    pass\n"
        "def _private():\n    pass\n"
        "@functools.total_ordering\n"
        "class Cache:\n    def method(self):\n        pass\n",
        encoding="utf-8",
    )
    (pkg / "sub" / "deep.py").write_text("def helper():\n    return 1\n", encoding="utf-8")
    syms = m.python_symbols(pkg, "py", root=tmp)
    got = {(s["id"], s["kind"], s["file"]) for s in syms}
    assert ("slugify", "function", "pkg/mod.py") in got
    assert ("fetch", "function", "pkg/mod.py") in got          # async def captured
    assert ("Cache", "class", "pkg/mod.py") in got             # decorated class captured (regex-hard)
    assert ("CONST", "const-export", "pkg/mod.py") in got      # __all__ const, not a def/class
    assert ("helper", "function", "pkg/sub/deep.py") in got    # nested dir walked, POSIX key
    assert not any(s["id"] == "_private" for s in syms)        # underscore = private, skipped
    assert not any(s["id"] == "method" for s in syms)          # a class method is not top-level
    assert all("\\" not in s["file"] for s in syms)            # POSIX keys on every platform
    (pkg / "broken.py").write_text("def broken(\n", encoding="utf-8")  # SyntaxError
    try:
        m.python_symbols(pkg, "py", root=tmp)
        raise AssertionError("python_symbols swallowed a parse error (fail-open)")
    except m.MapError as exc:
        assert "parse error" in str(exc)

    # --- enumerate_exports: the fail-closed JS/TS floor ------------------------------------
    web = tmp / "web"
    web.mkdir()
    (web / "ok.ts").write_text(
        "export function slugify(s) {}\n"
        "export async function load() {}\n"
        "export default class Panel {}\n"
        "export const RATE = 3;\n"
        "export type Foo = string;\n"            # recognized, not indexed (no runtime kind)
        "export interface Bar {}\n"              # recognized, not indexed
        "export { a, b as c } from './x';\n"     # recognized, not indexed (indexed at def site)
        "export * from './y';\n"                 # recognized, not indexed
        "// export function commented() {}\n"    # line comment ignored
        "/* export class Blocked {} */\n",       # block comment ignored
        encoding="utf-8",
    )
    jget = {(s["id"], s["kind"]) for s in m.enumerate_exports(web, "web", extensions=frozenset({".ts"}), root=tmp)}
    assert jget == {
        ("slugify", "function"),
        ("load", "function"),
        ("Panel", "class"),
        ("RATE", "const-export"),
    }, jget
    (web / "bad.ts").write_text("export abstract class Widget {}\n", encoding="utf-8")
    try:
        m.enumerate_exports(web, "web", extensions=frozenset({".ts"}), root=tmp)
        raise AssertionError("enumerate_exports silently skipped an unmodelled export form")
    except m.MapError as exc:
        assert "unmodelled" in str(exc)


def t_affordance_graced_presence(tmp: Path):
    # --- parse_affordance: leading seam block, none decl, delimiter-agnostic, presence-only ----
    seams = m.parse_affordance(
        "## Reuse affordance\n"
        "\n"
        "seam: slugify — reuse for name→slug; extend via the transform registry\n"
        "seam: Button - reuse for buttons; extend via the variant prop\n"  # plain hyphen delimiter
        "\n"
        "## Gaps\n"
    )
    assert seams.heading_present and seams.has_block
    assert seams.seams == ("slugify", "Button") and not seams.is_none  # id = first token, delim free
    none_aff = m.parse_affordance("## Reuse affordance\nnone — feature-specific glue, nothing reusable\n")
    assert none_aff.heading_present and none_aff.is_none and none_aff.has_block and none_aff.seams == ()
    bare = m.parse_affordance("## Reuse affordance\n\n## Gaps\n")
    assert bare.heading_present and not bare.has_block  # a bare heading dodges the decision → fails
    absent = m.parse_affordance("## Constraints & why\nx\n## Gaps\ny\n")
    assert not absent.heading_present and not absent.has_block
    # "leading CONSECUTIVE": prose ends the run — a `seam:` after prose is NOT in the block
    broken = m.parse_affordance("## Reuse affordance\nseam: a — x\nSee the notes.\nseam: b — y\n")
    assert broken.seams == ("a",)

    # --- affordance_offenders: graced skip, block passes, missing/bare fails --------------------
    texts = {
        "new_feat": "## Shared seams\n(no affordance section)\n",       # offender: no heading
        "graced_feat": "## Shared seams\n(predates the section)\n",     # exempt → not an offender
        "has_seams": "## Reuse affordance\nseam: slugify — reuse\n",    # ok
        "none_feat": "## Reuse affordance\nnone — nothing reusable\n",  # ok
        "bare": "## Reuse affordance\n\n## Gaps\n",                     # offender: no block
    }
    assert m.affordance_offenders(texts, frozenset({"graced_feat"})) == ["bare", "new_feat"]
    assert m.affordance_offenders(texts, frozenset()) == ["bare", "graced_feat", "new_feat"]

    # --- render → load round-trip + fail-closed on a malformed exempt file ----------------------
    map_dir = tmp / "memory" / "map"
    map_dir.mkdir(parents=True)
    assert m.load_affordance_exempt(tmp) == frozenset()  # absent file = no grace (fresh-repo default)
    rendered = m.render_affordance_exempt(["b", "a", "a"])  # unsorted + dup
    (map_dir / "affordance-exempt.toml").write_text(rendered, encoding="utf-8")
    assert m.load_affordance_exempt(tmp) == frozenset({"a", "b"})
    assert rendered.endswith("\n") and rendered.index('"a"') < rendered.index('"b"')  # sorted, deduped
    for bad, needle in [
        ("exempt = \"x\"\n", "exempt"),        # not a list
        ("exempt = [1]\n", "exempt"),          # non-string element
        ("exempt = [\"\"]\n", "exempt"),       # empty string
        ("other = []\n", "exempt"),            # unknown key / no exempt
        ("exempt = [\n", "toml parse error"),  # malformed toml
    ]:
        (map_dir / "affordance-exempt.toml").write_text(bad, encoding="utf-8")
        try:
            m.load_affordance_exempt(tmp)
            raise AssertionError(f"load accepted a malformed exempt file (expected {needle!r})")
        except m.MapError as exc:
            assert needle in str(exc), f"wrong error: {exc}"


def t_affordance_exemption_drop():
    """AC1 (U4 half): a dossier's affordance grace is dropped MECHANICALLY when a map_diff range
    touches its files (attribution owner), and it then fails the graced check until it carries a
    `seam:`/`none` block. An untouched graced dossier keeps its grace — no retro-red."""
    dx = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "touched"').replace("src/x/**", "src/touched/**"),
        IDS, source="touched",
    )
    dy = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "untouched"').replace("src/x/**", "src/untouched/**"),
        IDS, source="untouched",
    )
    f = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "foundation"').replace("src/x/**", "lib/**"),
        IDS, source="f",
    )
    tree = m.MapTree(foundation=f, dossiers=(dx, dy), baseline=EMPTY_BASE)

    attributed = m.attribute_paths(["src/touched/a.py"], tree)
    assert set(attributed) == {"touched"}, attributed  # only 'touched' was in the range
    exempt = frozenset({"touched", "untouched"})
    kept = m.drop_touched_exemptions(exempt, attributed)
    assert kept == frozenset({"untouched"}), kept  # touched loses grace, untouched keeps it
    # a range that hits nothing graced (foundation/UNMAPPED are never in the exempt list) is a no-op
    assert m.drop_touched_exemptions(exempt, {"UNMAPPED": ["z"], "foundation": ["lib/b.py"]}) == exempt

    # gate consequence: the un-graced 'touched' dossier (no affordance block yet) is now an offender
    texts = {
        "touched": "## Shared seams\n(no affordance yet)\n",
        "untouched": "## Shared seams\n(still graced)\n",
    }
    assert m.affordance_offenders(texts, exempt) == []          # both graced BEFORE the touch (no retro-red)
    assert m.affordance_offenders(texts, kept) == ["touched"]   # touch dropped grace -> must carry a block
    texts["touched"] = "## Reuse affordance\nseam: foo — reuse for bar; extend via baz\n"
    assert m.affordance_offenders(texts, kept) == []            # clears once it carries a seam:/none block


def t_seed_affordances(tmp: Path):
    """AC5: gen_map --seed-affordances --top N lists the N highest-fan-in seams no dossier yet
    declares, and NOTHING already declared. Pure core tested on a fixture repo (the CLI is thin
    glue over this + build_reference_index); ordering by fan-in desc and the --top cap verified."""
    import os

    (tmp / ".codebase-map.conf").write_text("MAP_ROOT=memory/map\nSEAM_FANIN_THRESHOLD=3\n", encoding="utf-8")
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},
        {"id": "titlecase", "kind": "function", "file": "src/text.py"},
        {"id": "truncate", "kind": "function", "file": "src/text.py"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    feats = tmp / "memory" / "map" / "features"
    feats.mkdir(parents=True)
    (feats / "text.md").write_text(  # slugify is ALREADY declared -> off the worklist despite top fan-in
        "## Reuse affordance\nseam: slugify — reuse for name→slug; extend via the registry\n",
        encoding="utf-8",
    )
    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text(
        "def slugify(s):\n    return s\n"
        "def titlecase(s):\n    return s\n"
        "def truncate(s, n):\n    return s[:n]\n",
        encoding="utf-8",
    )
    (src / "cache.py").write_text("class Cache:\n    pass\n", encoding="utf-8")
    # reference files planting a known fan-in: slugify 5, titlecase 4, truncate 3, Cache 1
    refs = {
        "a": "from text import slugify, titlecase, truncate\nfrom cache import Cache\nslugify(1); titlecase(2); truncate(3, 4); Cache()\n",
        "b": "from text import slugify, titlecase, truncate\nslugify(1); titlecase(2); truncate(3, 4)\n",
        "c": "from text import slugify, titlecase, truncate\nslugify(1); titlecase(2); truncate(3, 4)\n",
        "d": "from text import slugify, titlecase\nslugify(1); titlecase(2)\n",
        "e": "from text import slugify\nslugify(1)\n",
    }
    for name, body in refs.items():
        (src / f"{name}.py").write_text(body, encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)
        assert m.fan_in(ref, "slugify", "src/text.py") == 5
        assert m.fan_in(ref, "titlecase", "src/text.py") == 4
        assert m.fan_in(ref, "truncate", "src/text.py") == 3
        assert m.fan_in(ref, "Cache", "src/cache.py") == 1  # below the threshold -> not a seam

        worklist = rl.seed_affordances(corpus, ref, 10)
        # slugify EXCLUDED (already declares a seam) despite fan-in 5; Cache EXCLUDED (fan-in 1 < 3);
        # ranked by fan-in desc.
        assert [c.name for c, _ in worklist] == ["titlecase", "truncate"], worklist
        assert [fi for _, fi in worklist] == [4, 3]
        assert all(c.name != "slugify" for c, _ in worklist)  # nothing already declared
        # --top cap: only the single highest-fan-in undeclared seam
        assert [c.name for c, _ in rl.seed_affordances(corpus, ref, 1)] == ["titlecase"]
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def t_reuse_shared_primitives(tmp: Path):
    # --- tokenizer + crude stemmer: the one "shares a token stem" definition (S3 recall / S5 collision)
    assert m.subtokens("getUserID") == ["get", "user", "id"]
    assert m.subtokens("api/x/route.ts") == ["api", "x", "route", "ts"]
    assert m.subtokens("a_flag") == ["a", "flag"]
    assert m.subtokens("HTTPServer") == ["http", "server"]  # acronym run kept, not shredded
    assert m.stems("slugify") == frozenset({"slug"})        # `ify` stripped, NOT down to `y`
    assert m.stems("normalise a name to a slug") & m.stems("slugify") == {"slug"}
    assert not (m.stems("payment gateway") & m.stems("slugify"))  # unrelated -> no shared stem

    # --- fan-in: distinct referencing files minus the def file, comments/strings excluded ----
    src = tmp / "src"
    src.mkdir(parents=True)
    (src / "text.py").write_text("def slugify(s):\n    return s\n", encoding="utf-8")
    (src / "a.py").write_text("from text import slugify\n", encoding="utf-8")         # import ref
    (src / "b.py").write_text("x = slugify(1)  # slugify in a comment too\n", encoding="utf-8")
    (src / "c.py").write_text("s = 'slugify only inside a string'\n", encoding="utf-8")  # excluded
    (src / "d.py").write_text("# just slugify in a comment\ny = 1\n", encoding="utf-8")   # excluded
    idx = m.build_reference_index(["src/text.py"], root=tmp)
    refs = idx.get("slugify", set())
    assert "src/c.py" not in refs and "src/d.py" not in refs, refs  # string/comment-only dropped
    assert m.fan_in(idx, "slugify", "src/text.py") == 2  # a.py + b.py, minus the def file

    # --- seam threshold from conf: default, override, fail-closed on a non-int -----------------
    assert m.seam_fanin_threshold(tmp) == m.SEAM_FANIN_THRESHOLD_DEFAULT  # no conf -> default
    (tmp / ".codebase-map.conf").write_text("SEAM_FANIN_THRESHOLD=5\n", encoding="utf-8")
    assert m.seam_fanin_threshold(tmp) == 5
    (tmp / ".codebase-map.conf").write_text("SEAM_FANIN_THRESHOLD=nope\n", encoding="utf-8")
    try:
        m.seam_fanin_threshold(tmp)
        raise AssertionError("a non-int SEAM_FANIN_THRESHOLD must fail closed")
    except m.MapError:
        pass


def t_reuse_lookup(tmp: Path):
    """AC3 on a portable FIXTURE repo (no host-repo paths): a planted `slugify` seam is ranked
    above unrelated symbols for a behaviour query; a no-home query returns 'no seam fits'; and a
    recall-dark layer prints the partial-recall notice so an empty result is never falsely sure."""
    import os

    (tmp / ".codebase-map.conf").write_text(
        'MAP_ROOT=memory/map\nRECALL_DARK_LAYERS="web-ts"\nSEAM_FANIN_THRESHOLD=3\n', encoding="utf-8"
    )
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},
        {"id": "titlecase", "kind": "function", "file": "src/text.py"},
        {"id": "truncate", "kind": "function", "file": "src/text.py"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    (gen / "inventories.json").write_text(
        m.render_inventories_json({"flags": ["beta_flag"]}, ("flags",)), encoding="utf-8"
    )
    feats = tmp / "memory" / "map" / "features"
    feats.mkdir(parents=True)
    (feats / "text.md").write_text(
        "## Reuse affordance\n"
        "seam: slugify — reuse for name→slug; extend via the transform registry\n"
        "\n"
        "## Shared seams\n"
        "The text module normalises display names into url slugs.\n",
        encoding="utf-8",
    )
    (feats / "glue.md").write_text(  # prose-only feature: `none` affordance, no seam symbol
        "## Reuse affordance\nnone — feature-specific glue\n"
        "\n## Shared seams\nThe glue layer wires the webhook dispatcher.\n",
        encoding="utf-8",
    )
    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text(
        "def slugify(s):\n    return s\n"
        "def titlecase(s):\n    return s\n"
        "def truncate(s, n):\n    return s[:n]\n",
        encoding="utf-8",
    )
    for f in ("a", "b", "c"):
        (src / f"{f}.py").write_text(f"from text import slugify\nx = slugify('{f}')\n", encoding="utf-8")
    (src / "cache.py").write_text("class Cache:\n    pass\n", encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)

        # (a) a slug query ranks the planted seam FIRST and above unrelated same-file symbols
        sl = rl.assemble_shortlist("normalise a display name into a url slug", corpus, ref)
        names = [r.candidate.name for r in sl.ranked]
        assert names and names[0] == "slugify", names
        assert names.index("slugify") < names.index("titlecase"), names  # seed above neighbour
        top = sl.ranked[0]
        assert top.is_seed and top.is_seam and top.fanin == 3, top      # fan-in on demand, seam
        assert "affordance-seam" in corpus.candidates["slugify"].sources  # merged symbol + seam
        assert "Cache" not in names, names  # different kind AND file -> not a neighbour
        out = rl.render(sl, corpus)
        assert "recall partial: layers web-ts" in out                   # (c) recall-dark announced

        # (b) a no-home query returns "no seam fits" — and STILL flags the recall-dark gap
        sl2 = rl.assemble_shortlist("configure the payment gateway retry budget", corpus, ref)
        assert sl2.empty, [r.candidate.name for r in sl2.ranked]
        out2 = rl.render(sl2, corpus)
        assert "no seam fits" in out2
        assert "recall partial: layers web-ts" in out2  # never a falsely-confident "no seam"

        # `## Shared seams` prose recall: a seam-less feature surfaces via its prose (behavioural
        # recall beyond symbol names), and assembling is IDEMPOTENT (no synthetic leak into corpus).
        before = len(corpus.candidates)
        sl3 = rl.assemble_shortlist("dispatch a webhook", corpus, ref)
        names3 = [r.candidate.name for r in sl3.ranked]
        assert "glue (## Shared seams)" in names3, names3
        assert len(corpus.candidates) == before  # pool copy, not the caller's corpus
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def t_detect_collisions_and_backlog(tmp: Path):
    """AC4: on a range that adds `slugify2` (stem-colliding with the high-fan-in `slugify` seam,
    no new edge to it) the closing loop emits ONE collision_flag; a symbol that WIRES THROUGH its
    seam, one whose seam is below threshold, one of a different kind, and one unrelated do NOT
    flag; the backlog dedupes by (new, resembles); and new_clones is a clone-ratchet count, NOT
    dead_exports/affordance_coverage_%. Pure core — the git-range extraction is thin glue tested
    by the scratchpad fixture in the build report."""
    # base seams (present at range base). Constructed reference index -> exact fan-in per seam
    # (the fan_in math itself is proven in t_reuse_shared_primitives; this pins collision logic).
    base = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},        # reinvented (fan-in 3)
        {"id": "fetchGateway", "kind": "function", "file": "src/gw.py"},     # wired-through (fan-in 3)
        {"id": "parseThing", "kind": "function", "file": "src/parse.py"},    # below threshold (fan-in 1)
        {"id": "Money", "kind": "class", "file": "src/money.py"},            # a class (kind mismatch)
    ]
    ref = {
        "slugify": {"src/a.py", "src/b.py", "src/c.py", "src/text.py"},      # fan-in 3
        "fetchGateway": {"src/d.py", "src/e.py", "src/f.py", "src/gw.py"},   # fan-in 3
        "parseThing": {"src/g.py", "src/parse.py"},                          # fan-in 1 < threshold
        "Money": {"src/money.py"},                                           # fan-in 0
    }
    new = [
        {"id": "slugify2", "kind": "function", "file": "src/new1.py"},       # collides slugify, NOT wired -> FLAG
        {"id": "retryGateway", "kind": "function", "file": "src/new2.py"},   # collides fetchGateway, WIRES through
        {"id": "parseWidget", "kind": "function", "file": "src/new3.py"},    # collides parseThing, but it's < threshold
        {"id": "moneyBag", "kind": "function", "file": "src/new4.py"},       # stem 'money' but Money is a CLASS
        {"id": "helper", "kind": "function", "file": "src/new5.py"},         # unrelated -> no shared stem
    ]
    # the range wires through fetchGateway (new2 references it) — an edge added -> not reinvention;
    # slugify has NO edge added in the range -> slugify2 is reinvention.
    range_index = {"fetchGateway": {"src/new2.py"}}
    flags = m.detect_collisions(new, base, ref, range_index, threshold=3)
    assert [f.new for f in flags] == ["slugify2"], flags               # exactly one collision
    only = flags[0]
    assert only.resembles == "slugify" and only.file == "src/new1.py" and only.fanin == 3
    assert only.kind == "function" and only.confidence == "medium"     # no affordance declared -> medium
    # F8c: when the seam DECLARES an affordance, confidence rises to high.
    hi = m.detect_collisions(new, base, ref, range_index, threshold=3, affordance_seams=frozenset({"slugify"}))
    assert hi[0].confidence == "high"
    # retryGateway stays clean ONLY because the range wired through fetchGateway — drop that edge and
    # it flags, proving the reference-edge check is load-bearing (not dead code). parseWidget/moneyBag
    # stay clean regardless (below-threshold seam / kind mismatch).
    flagged_names = {f.new for f in m.detect_collisions(new, base, ref, {}, threshold=3)}
    assert flagged_names == {"slugify2", "retryGateway"}, flagged_names

    # --- backlog: seeded header, append, dedup by (new, resembles) --------------------------------
    text0, added0 = m.append_backlog("", flags)
    assert added0 and "| slugify2 | slugify |" in text0 and text0.startswith("# Reinvention backlog")
    assert m.backlog_keys(text0) == {("slugify2", "slugify")}
    text1, added1 = m.append_backlog(text0, flags)          # re-run same range -> nothing new
    assert added1 == [] and text1 == text0
    more = [m.CollisionFlag("slugify3", "slugify", "src/t3.py", 3, "function", "medium")]
    text2, added2 = m.append_backlog(text0, more)           # a different `new` -> a new row
    assert [a.new for a in added2] == ["slugify3"]
    assert m.backlog_keys(text2) == {("slugify2", "slugify"), ("slugify3", "slugify")}


def t_new_clones_reader(tmp: Path):
    """new_clones is the adopted clone-ratchet's count (int), null when no clone kit is wired, and
    folding a duplicate drops it — NEVER dead_exports/affordance_coverage_% (the demoted hints)."""
    import map_diff as md

    assert md._new_clones(tmp, {}) is None                                  # no CLONE_COUNT_FILE -> null
    conf = {"CLONE_COUNT_FILE": "clones.txt"}
    assert md._new_clones(tmp, conf) is None                                # configured but absent -> null
    (tmp / "clones.txt").write_text("7\n", encoding="utf-8")
    assert md._new_clones(tmp, conf) == 7
    (tmp / "clones.txt").write_text("4\n", encoding="utf-8")                # a fold drops the count
    assert md._new_clones(tmp, conf) == 4
    (tmp / "clones.txt").write_text("not-a-number\n", encoding="utf-8")     # garbage -> null, never a crash
    assert md._new_clones(tmp, conf) is None


def main() -> int:
    import tempfile

    failures = 0
    failures += check("coverage both directions + ratchet guards", t_coverage_directions)
    failures += check("dossier contract fails loud", t_parse_contract)
    failures += check("attribution: keyed > globs, posix, case-sensitive", t_attribution)
    failures += check("renders deterministic + keys-only + round-trip", t_renders_round_trip_and_determinism)
    failures += check("glob brackets fail loud; [[]-escape matches", t_glob_brackets_fail_loud_and_escape_works)
    failures += check(
        "symbols.json deterministic + fail-closed render", t_symbols_render_deterministic_and_fail_closed
    )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "extractor helpers fail closed", lambda: t_extractor_helpers_fail_closed(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "symbol extractors fail closed (ast + enum floor)", lambda: t_symbol_extractors_fail_closed(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("conf restricted grammar", lambda: t_conf_grammar(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "affordance graced presence + shrink-only exempt", lambda: t_affordance_graced_presence(Path(td))
        )
    failures += check("affordance exemption drop on touch (S4a / AC1)", t_affordance_exemption_drop)
    with tempfile.TemporaryDirectory() as td:
        failures += check("seed-affordances worklist (S4b / AC5)", lambda: t_seed_affordances(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "reuse-lookup shared primitives (stems + fan-in + threshold)", lambda: t_reuse_shared_primitives(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("reuse-lookup shortlist (AC3 fixture)", lambda: t_reuse_lookup(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "closing loop: collisions + backlog dedup (S5 / AC4)", lambda: t_detect_collisions_and_backlog(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("new_clones reader (S5 / AC4)", lambda: t_new_clones_reader(Path(td)))
    print("PASS" if not failures else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
