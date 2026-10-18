# **Serves:** research TOOL-aScoutedSeam-3 TOOL-aScoutedSeam-1
"""T1: the diff-time duplicate check re-composed. A deterministic lister enumerates the units a diff
ADDS, and the reviewer must return one verdict row per listed unit, so the first duplicate found
cannot end the review. Tests the hypothesis that `medium` lost cases to an open-ended prompt with a
single verdict, not to effort.

    python <this> units <diff-file>                  the enumerated added units, one per line
    python <this> questions <d1-root> <out-dir>      one question file per diff case
    python <this> packets <out-dir> <arm>...         blind judge packets and tasks for the diff cases
    python <this> judge-collect <key.json> <short>=<reply>...   judge verdicts into the results

The replies are collected by `-1-9-m1d-trial.py collect d1v2@medium <case-id>=<file>...`.

What the lister does NOT see: a duplicated literal value inside an expression, a renamed copy of a
function body, or a JSON tree node with no `slug`, `part` or `name` key. The prompt asks the reviewer
to add such units itself, and every row it adds is marked as its own.
"""
import json
import re
import sys
from pathlib import Path

D1_ROOT = Path("C:/Users/daily-agent/AppData/Local/Temp/rsd")
SKIP_PATH = re.compile(r"(^|/)(memory|docs|help|tests?|__tests__|fixtures?)/|\.test\.|_test\.|\.md$|\.lock$|"
                       r"(^|/)(package-lock|pnpm-lock)\.|\.snap$|\.svg$|\.png$|\.webp$")
UNIT_PATTERNS = (
    ("def", re.compile(r"^\s*(?:export\s+)?(?:async\s+)?(?:def|function|class)\s+([A-Za-z_$][\w$]*)")),
    ("const", re.compile(r"^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=")),
    ("shell-fn", re.compile(r"^([A-Za-z_][\w]*)\s*\(\)\s*\{")),
    ("constant", re.compile(r"^(?:readonly\s+|declare\s+-[a-zA-Z]+\s+)?([A-Z][A-Z0-9_]{2,})=")),
    ("py-constant", re.compile(r"^([A-Z][A-Z0-9_]{2,})\s*[:=]")),
    ("css-prop", re.compile(r"^\s*(--[a-z][\w-]*)\s*:")),
    ("css-rule", re.compile(r"^\s*([.#\[][^{;]{1,80}?)\s*\{\s*$")),
    ("field", re.compile(r"^\s*([A-Za-z_]\w*)\s*:\s*(?:\{\s*type\s*:|[A-Za-z]+Field\()")),
    ("json-key", re.compile(r"\"(?:slug|part|descriptorSlug|name)\"\s*:\s*\"([^\"]{2,60})\"")),
)
UNIT_CAP = 60


STYLE_FILE = re.compile(r"\.(css|scss|less)$")
HUNK_MIN_ADDED = 4


def extract_units(diff_text):
    """[(kind, name, file)] the diff ADDS, in diff order, deduplicated, product files only. A hunk
    that adds HUNK_MIN_ADDED or more lines and holds no named unit becomes a `hunk` unit, so logic
    added inside an existing function is still listed."""
    units, seen, path, hunk = [], set(), None, None

    def add_hunk_unit():
        if hunk and not hunk["named"] and len(hunk["added"]) >= HUNK_MIN_ADDED:
            first = next((a.strip() for a in hunk["added"] if a.strip()), "")[:70]
            units.append(("hunk", f"{hunk['at']}: {first}", hunk["path"]))

    for line in diff_text.splitlines():
        if line.startswith("+++ ") or line.startswith("diff --git"):
            add_hunk_unit()
            hunk = None
            if line.startswith("+++ "):
                path = line[6:] if line.startswith("+++ b/") else None
            continue
        if line.startswith("@@"):
            add_hunk_unit()
            hunk = {"at": line.split("@@")[1].strip(), "added": [], "named": False, "path": path}
            continue
        if not path or SKIP_PATH.search(path) or not line.startswith("+"):
            continue
        body = line[1:]
        if hunk is not None:
            hunk["added"].append(body)
        for kind, pat in UNIT_PATTERNS:
            if kind.startswith("css") and not STYLE_FILE.search(path):
                continue
            for m in pat.finditer(body) if kind == "json-key" else [pat.match(body)]:
                if m and (path, m.group(1)) not in seen:
                    seen.add((path, m.group(1)))
                    units.append((kind, m.group(1).strip(), path))
                    if hunk is not None:
                        hunk["named"] = True
                    break
    add_hunk_unit()
    return units


def render_units(units):
    head = units[:UNIT_CAP]
    lines = [f"U{i + 1}. {name}  [{kind} · {path}]" for i, (kind, name, path) in enumerate(head)]
    if len(units) > UNIT_CAP:
        lines.append(f"... and {len(units) - UNIT_CAP} more units the lister found past its cap of "
                     f"{UNIT_CAP}; cover them as you read the diff.")
    return "\n".join(lines) or "(the lister found no added unit; enumerate them yourself from the hunks)"


def render_question(case, units):
    trees = "TREE (the parent revision, before the diff landed): " + case["tree"]
    if case.get("core_tree"):
        trees += "\nHOST CORE TREE (incms, the platform this package installs into): " + case["core_tree"]
    return "\n\n".join([
        "You are the REUSE REVIEWER for a diff about to land. This task block OVERRIDES your role's "
        "pointer to reuse-lookup.agent.md. Your job is a COVERAGE job: account for EVERY unit the diff "
        "adds, one verdict per unit, so that no duplicate goes unexamined because another was found first.",
        trees,
        "THE DIFF: " + case["diff"] + " (a unified diff with a --stat header; commit subject: \""
        + case["subject"] + "\"). Read the --stat first, then the hunks that add code or styles.",
        "RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or "
        "any other checkout, and never consult git history: the tree is the state before the diff.",
        "THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):\n"
        + render_units(units),
        "FOR EACH LISTED UNIT, in order, return one row:\n"
        "- unit: its U-number and name;\n"
        "- nearest: the closest EXISTING implementation in the tree of the same need, as path::symbol, "
        "found by searching the CONCEPT with synonyms across all file types, or `none` with what you searched;\n"
        "- verdict: `duplicate` (the existing one already covers the need and is reachable from the new "
        "code), `should-extend` (the existing one covers most of it and should have been extended), "
        "`new` (genuinely new capability) or `not-a-unit` (a lister artefact);\n"
        "- why: one line.\n"
        "Then ADD rows for duplicated units the lister cannot see: a repeated literal value, a hardcoded "
        "design value beside an existing token, a copied function body under a new name, a JSON tree node "
        "re-built beside an existing one. Mark each added row `added: true`.",
        "Do not stop at the first duplicate. A review that leaves a listed unit without a row is incomplete.",
        "RETURN CONTRACT. End your reply with ONE ```json block holding an object with keys: rows (every "
        "row above), seams, verdict. seams: one entry per `duplicate` or `should-extend` row, each with "
        "repo, path (repo-relative, the EXISTING seam), symbol, binding (MUST for duplicate, SHOULD for "
        "should-extend), new_code (what the diff added), how (how the diff should use the seam instead), "
        "evidence (file:line). verdict: `duplicates-found` or `clean`.",
    ])


def run_questions(d1_root, out_dir):
    cases = json.loads((Path(d1_root) / "d1.cases.json").read_text(encoding="utf-8"))
    resolved = {c["id"]: c for c in json.loads((Path("C:/Users/daily-agent/AppData/Local/Temp/rsb")
                                                / "cases.resolved.json").read_text(encoding="utf-8"))}
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for short, c in cases.items():
        rc = resolved.get(c["id"], {})
        if rc.get("core_point_sha"):
            c = dict(c, core_tree=(Path("C:/Users/daily-agent/AppData/Local/Temp/rsb") / rc["short"]
                                   / "incms").as_posix())
        units = extract_units(Path(c["diff"]).read_text(encoding="utf-8", errors="replace"))
        (out / (c["id"] + ".txt")).write_text(render_question(c, units), encoding="utf-8")
        print(f"{c['id']:<34} units {len(units):>4}")


HERE = Path(__file__).resolve().parent
STEM = "2026-10-11-build-TOOL-aScoutedSeam-1-"
RSB_ROOT = Path("C:/Users/daily-agent/AppData/Local/Temp/rsb")


def load_bench():
    import importlib.util
    spec = importlib.util.spec_from_file_location("bench", HERE / (STEM + "4-bench.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_packets(out_dir, arms):
    """Blind packets for the diff cases through the bench's own `judge-packets`, each extended with the
    diff under review and its pre-diff tree. The judge's instructions are `-1-10-judge-task.md`."""
    bench = load_bench()
    out = Path(out_dir)
    bench.cmd_judge_packets([str(HERE / (STEM + "3-cases.json")), str(HERE / (STEM + "5-results.json")),
                             str(out), str(RSB_ROOT)] + arms)
    cases = json.loads((D1_ROOT / "d1.cases.json").read_text(encoding="utf-8"))
    for short, c in cases.items():
        packet = out / f"{short}.md"
        packet.write_text(packet.read_text(encoding="utf-8") + "\n## The diff under review\n\n"
                          f"- diff: {c['diff']} (commit subject: \"{c['subject']}\")\n"
                          f"- pre-diff tree: {c['tree']}\n", encoding="utf-8", newline="\n")
    for p in out.glob("c*.md"):
        if p.stem not in cases:
            p.unlink()
    print(f"{len(cases)} diff packets in {out}")


def run_judge_collect(key_file, reports):
    """Each report is `<short>=<reply-file>`; the last ```json block's arms join back through the key and
    land under `judge` in the results, as the bench's own `judge-collect` files them."""
    import re as _re
    key = json.loads(Path(key_file).read_text(encoding="utf-8"))
    cases = json.loads((D1_ROOT / "d1.cases.json").read_text(encoding="utf-8"))
    bench = load_bench()
    path = HERE / (STEM + "5-results.json")
    results = bench.read_json(str(path))
    verdicts = results.setdefault("judge", {})
    bad = 0
    for spec in reports:
        short, _, f = spec.partition("=")
        blocks = _re.findall(r"```json\s*(.*?)```", Path(f).read_text(encoding="utf-8", errors="replace"), _re.S)
        try:
            arms_out = json.loads(blocks[-1])["arms"]
        except (IndexError, ValueError, KeyError, TypeError):
            bad += 1
            continue
        for a in arms_out:
            arm = key.get(short, {}).get(a.get("label"))
            if arm:
                cell = {k: a.get(k) for k in ("covered", "primary", "wrong", "valid_extra", "score", "note")}
                if isinstance(cell["valid_extra"], dict):  # one judge split it by binding; the rubric counts both
                    cell["valid_extra"] = sum(v for v in cell["valid_extra"].values() if isinstance(v, int))
                verdicts.setdefault(arm, {})[cases[short]["id"]] = cell
    bench.write_json(str(path), results)
    print(f"judge: {len(reports)} report(s), {bad} unparsed")


def main(argv):
    if argv[:1] == ["units"] and len(argv) == 2:
        for kind, name, path in extract_units(Path(argv[1]).read_text(encoding="utf-8", errors="replace")):
            print(f"{kind}\t{name}\t{path}")
    elif argv[:1] == ["questions"] and len(argv) == 3:
        run_questions(argv[1], argv[2])
    elif argv[:1] == ["packets"] and len(argv) > 2:
        run_packets(argv[1], argv[2:])
    elif argv[:1] == ["judge-collect"] and len(argv) > 2:
        run_judge_collect(argv[1], argv[2:])
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
