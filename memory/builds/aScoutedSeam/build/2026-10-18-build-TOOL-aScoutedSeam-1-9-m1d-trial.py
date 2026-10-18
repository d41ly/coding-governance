# **Serves:** research TOOL-aScoutedSeam-1
"""The M1d trial: M1c's checklist plus a DRAFT of the code, an EXPANSION of every cited file into its
definitions, and an OWNER grep for every literal, regex and launcher in the draft (fork F3).

The spawn guard admits a `Workflow` call only for a listed harness, so the arm runs as typed
`gov-reuse-scout` agents, one per case and run, each spawned from a handoff `handoff.py render`
writes. The handoff is rendered against an EMPTY card, because the session card's task fields name the
benchmark's ground truth.

    python <this> questions <out-dir> <case-id>...      one question file per case
    python <this> collect <arm> <report>...             parse the agents' reports into the results file

What it does NOT do: grade (that is `-1-4-bench.py grade`), or enforce the return shape. A report
whose JSON block does not parse is filed as null and counted, never guessed at.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEM = "2026-10-11-build-TOOL-aScoutedSeam-1-"
_spec = importlib.util.spec_from_file_location("bench", str(HERE / (STEM + "4-bench.py")))
bench = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bench)
TREE_ROOT = Path("C:/Users/daily-agent/AppData/Local/Temp/rsb")
LISTER = (HERE / "2026-10-13-build-TOOL-aScoutedSeam-1-8-precision.py").as_posix()
JSON_BLOCK = re.compile(r"```json\s*(\{.*\})\s*```", re.S)


def render_question(case):
    tree = (TREE_ROOT / case["short"] / case["repo"]).as_posix()
    core = (TREE_ROOT / case["short"] / "incms").as_posix() if case.get("core_point_sha") else None
    index = (TREE_ROOT / case["short"] / "house-index.md").as_posix()
    trees = "PRIMARY TREE (" + case["repo"] + "): " + tree
    if core:
        trees += ("\nHOST CORE TREE (incms, the platform this package installs into; its blocks, DSL, theme "
                  "and UI primitives are available to the package): " + core)
    return "\n\n".join([
        "You are the REUSE SCOUT for a request that has not been specced yet. Your output becomes binding "
        "instructions for whoever specs and builds it, so precision matters as much as recall. This task block "
        "OVERRIDES your role's pointer to reuse-lookup.agent.md: follow the checklist below.",
        trees,
        "RULES: work ONLY inside the tree(s) above, read-only: no edit, stage or commit. Never read anything "
        "under C:/projects or any other checkout, and never consult git history beyond the tree HEAD: you stand "
        "at the moment the request arrived. The ONE exception is running the definitions lister named in step "
        "4c. You may run the tree's own read-only CLIs with cwd inside the tree (scripts/ or tools/ "
        "codebase-map/reuse_lookup.py \"<behaviour phrase>\"; memory-recall/query.py \"<question>\" --terms "
        "\"<8-14 words>\"), grep, glob and read.",
        "THE REQUEST:\n\"\"\"" + case["prompt"] + "\"\"\"",
        "WORK THROUGH THIS CHECKLIST IN ORDER:",
        "0. HOUSE INDEX. Read " + index + " first. It was generated from the tree(s) before you started: shared "
        "libraries, canonical copies installed in many files, the most-reused symbols, the gate legs and lint "
        "rules that grade every change, the recorded bug classes, the dossiers' reuse affordances, the design "
        "tokens and the DSL node kinds. Every entry is a candidate seam or a house rule.",
        "1. ORIENT. Read AGENTS.md/CLAUDE.md and the codebase map index (memory/map/generated/CARDS.md or MAP.md, "
        "dossier titles) to learn this codebase's vocabulary and where things live.",
        "2. FRAME AND SKETCH. Write the request's needs, 3-10 of them, including implied ones. Then list every "
        "component a builder would have to write, 6-15 lines, plumbing included: tests, wiring, config reads, "
        "launcher calls, phase or status decisions, I/O formats, UI elements and styles.",
        "3. ANCHORS AND CANONICAL. Resolve every page, route, block, component, command or feature the request "
        "names or implies to the code that implements it today. Find the existing implementations of the same "
        "KIND of thing. Where several exist, identify the CANONICAL one, the shared generator, factory or base "
        "the others call, or the one a dossier or decision names, and treat the rest as stale copies.",
        "3b. CONVENTION CENSUS, whenever the request builds an instance of a kind that already has siblings, or "
        "adds a prop, field or option siblings already have. Open at least five siblings and tabulate how they "
        "set the shared choices, INCLUDING how they declare the very prop or field the request adds. For a "
        "CHOICE (a prop, token, layout, test harness) bind the majority. For a HELPER (a reader, parser, "
        "launcher) bind the CANONICAL implementation and name the copies in `not`: a majority of local copies is "
        "a debt, never a convention to follow. One census line per choice: `<choice>: <majority> (<n> of <m>)`.",
        "4. SEARCH EVERY SKETCHED COMPONENT: start from the house index entries that match it, then search by "
        "CONCEPT across all file types, run the gotchas CLI for the paths you expect to touch, and run "
        "reuse_lookup with two or three phrasings. A gate leg or lint rule that bans an idiom names the canonical "
        "helper. Verify reachability; never trust a comment claiming something is unreachable.",
        "4b. DRAFT. Write the code a builder would actually TYPE for the core of the change, 30-120 lines in the "
        "house language: real function bodies, the literals and string sets, regexes, constants, interpreter "
        "and process launches, wall-clock or timeout handling, test fixture lines. Return it as `draft`. It is "
        "an instrument, never a file: write nothing.",
        "4c. EXPAND EVERY FILE YOU CITE OR ANCHOR ON. Run `python " + LISTER + " defs <absolute file>...` over "
        "every file you cite and every anchor file you opened. It prints each file's top-level definitions, "
        "constants included. Check every name against your draft: a definition that already does what a draft "
        "line does is a seam, and the draft line is the duplicate. Return `expanded`: the files you listed.",
        "4d. OWNERS. For every literal string set (phase or status names), regex or id pattern, interpreter "
        "launch (python3, python, node), path computation and timeout in the draft, grep the tree(s) for its "
        "existing owner, for example `grep -rn \"LANDED\"`, and bind the owner instead of the draft's copy.",
        "5. DESIGN SYSTEM, when any need is visual: tokens and CSS custom properties in BOTH trees, theme "
        "variables, UI primitives with their variants and props, DSL node kinds and recipes, and the existing "
        "visual pattern for the same kind of surface. Name exact tokens, props and variants.",
        "6. RECORDS. Use the memory-recall CLI and grep memory/ and help/ for decisions, dossier \"Reuse "
        "affordance\" lines and help pages that settle HOW this kind of thing is built here.",
        "7. SELF-REFUTE each candidate: does it provide the need, is it reachable, is it canonical, or is it a "
        "LURE for a different need? Drop any that fails.",
        "RETURN CONTRACT. End your reply with ONE ```json block holding an object with these keys: needs, sketch, "
        "census, draft (a string), expanded (file paths), seams, edits, constraints, unmet.",
        "- seams: at most 12, best first, ONLY EXISTING implementations. Each has repo, path (repo-relative), "
        "symbol (exact name), binding (MUST or SHOULD), need, how (the call, prop, token or extension point to "
        "build WITH), evidence (file:line you read), not (optional: the stale copy or lure to avoid).",
        "- MUST: an existing implementation the build would DUPLICATE or BYPASS if it ignored it; its `how` names "
        "that duplicate. At most 5 MUSTs, the strongest first. SHOULD: a strong default the spec may override "
        "with a reason.",
        "- edits: the files the build will merely edit, registrations, regenerations, tests to write or keep "
        "green, and docs to update. These are build work, NEVER seams.",
        "- constraints: at most 5 rules that constrain the build: path, rule, how to satisfy it. unmet: needs "
        "nothing fits, each with what you searched.",
    ])


def run_questions(out_dir, ids):
    corpus = {c["id"]: c for c in json.loads((TREE_ROOT / "cases.resolved.json").read_text(encoding="utf-8"))}
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for cid in ids:
        (out_dir / (cid + ".txt")).write_text(render_question(corpus[cid]), encoding="utf-8")
        print(cid, len(render_question(corpus[cid])))


def extract_report(text):
    """The last ```json block of a report, parsed; None when absent or malformed."""
    blocks = JSON_BLOCK.findall(text)
    if not blocks:
        return None
    try:
        return json.loads(blocks[-1])
    except json.JSONDecodeError:
        return None


def run_collect(arm, reports):
    """Each report path is `<case-id>=<file>`; the file holds the agent's final reply."""
    path = HERE / (STEM + "5-results.json")
    results = bench.read_json(str(path))
    rows = results.setdefault(arm, {})
    bad = 0
    for spec in reports:
        cid, _, f = spec.partition("=")
        rows[cid] = extract_report(Path(f).read_text(encoding="utf-8", errors="replace"))
        bad += rows[cid] is None
    bench.write_json(str(path), results)
    print(f"{arm}: {len(reports)} report(s), {bad} unparsed")


def main(argv):
    if argv[:1] == ["questions"] and len(argv) > 2:
        run_questions(argv[1], argv[2:])
    elif argv[:1] == ["collect"] and len(argv) > 2:
        run_collect(argv[1], argv[2:])
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
