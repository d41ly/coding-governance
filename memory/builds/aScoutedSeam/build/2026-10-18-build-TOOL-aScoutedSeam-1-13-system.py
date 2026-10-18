# **Serves:** research TOOL-aScoutedSeam-3 TOOL-aScoutedSeam-1
"""The system measurement: the pre-spec scout (M1c), then the diff check given the scout's `## reuse`
card, on the tuning corpus and the held-out set, plus the T2 diff variant. One judge pass grades all.

    python <this> orient-q   <corpus> <tree-root> <out-dir>              M1c question per case
    python <this> card       <results> <arm> <case-id> <out-file>        the `## reuse` card from an arm
    python <this> diff-q     <d1-root> <out-dir> <variant> [<results> <orient-arm>]
                             variant `t1`: the measured enumerated prompt; `t2`: T1 plus the house
                             index, the extended lister and the general rules. With an orient arm,
                             each question carries that arm's MUST/SHOULD seams as the wiring half.
    python <this> units-t2   <diff> <tree>                               the extended lister's units
    python <this> collect    <results> <arm> <case-id>=<reply>...        last ```json block per reply
    python <this> packets    <corpus> <results> <tree-root> <d1-root> <out-dir> <arm>...
    python <this> judge-collect <corpus> <results> <key.json> <short>=<reply>...
    python <this> system     <corpus> <results> <orient-arm> <diff-arm>...   judged union per case

Every prompt here is written for the general case. The held-out set is graded with them and is never
read to change them.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEM = "2026-10-11-build-TOOL-aScoutedSeam-1-"


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bench = load_module("bench", STEM + "4-bench.py")
TEMP = Path("C:/Users/daily-agent/AppData/Local/Temp")
# Where each set's host core tree sits: the tuning corpus under rsb/, the held-out set under rsh/.
CORE_SOURCES = [(TEMP / "rsb" / "cases.resolved.json", TEMP / "rsb"),
                (HERE / "2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json", TEMP / "rsh")]
d1v2 = load_module("d1v2", "2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py")

ORIENT_CONTRACT = (
    "RETURN CONTRACT. End your reply with ONE ```json block holding an object with keys: needs (list of "
    "strings), sketch (list of strings), census (list of strings), seams (list, at most 12, best first, each "
    "{repo, path, symbol, binding MUST|SHOULD, need, how, evidence, not}), constraints (at most 5, each "
    "{path, rule, how}), unmet (list of strings).")

ORIENT_STEPS = [
    "WORK THROUGH THIS CHECKLIST IN ORDER:",
    "0. HOUSE INDEX. Read {index} first. It was generated from the tree(s) before you started: shared "
    "libraries, canonical copies installed in many files, the most-reused symbols, the gate legs and lint "
    "rules that grade every change, the recorded bug classes, the dossiers' reuse affordances, the design "
    "tokens and the DSL node kinds. Every entry is a candidate seam or a house rule.",
    "1. ORIENT. Read AGENTS.md/CLAUDE.md and the codebase map index (memory/map/generated/CARDS.md or "
    "MAP.md, dossier titles) to learn this codebase's vocabulary and where things live.",
    "2. FRAME AND SKETCH. Write the request's needs, 3-10 of them, including implied ones (an image property "
    "implies choosing or uploading media; a new page implies layout, type and colour). Then sketch the "
    "implementation: every component a builder would have to write, 6-15 lines, each concrete - the "
    "function, constant, field, file, test, fixture, wiring or registration, config read, process or "
    "launcher call, status or phase decision, I/O format, UI element and style.",
    "3. ANCHORS AND CANONICAL. Resolve every page, route, block, component, command or feature the request "
    "names or implies to the code that implements it today. Find the existing implementations of the same "
    "KIND of thing being built, and identify the CANONICAL one: the shared generator, factory or base the "
    "others call, or the one a dossier or decision names.",
    "3b. CONVENTION CENSUS, whenever the request builds an instance of a kind that already has siblings. "
    "Open at least five siblings and tabulate how they set the shared choices. Bind the majority convention "
    "as MUST unless the request asks otherwise. Return one census line per choice: "
    "`<choice>: <majority> (<n> of <m>)`.",
    "4. SEARCH EVERY SKETCHED COMPONENT by concept across all file types, starting from the house index; "
    "run the tree's reuse_lookup and gotchas CLIs where present. A gate leg or lint rule that bans an idiom "
    "names the canonical helper. Verify reachability; a port plus a parity check counts as reuse across a "
    "kit or language boundary.",
    "5. DESIGN SYSTEM, when any need is visual: tokens and custom properties in BOTH trees, UI primitives "
    "and their props, DSL node kinds, and the existing visual pattern for the same kind of surface.",
    "6. RECORDS. Use the memory-recall CLI and grep memory/ and help/ for decisions, dossier reuse "
    "affordances and help pages that settle HOW this kind of thing is built here.",
    "7. SELF-REFUTE each candidate: does it provide the need, is it reachable, is it canonical, is it a lure "
    "for a different need? Drop any that fails.",
    "OUTPUT. seams: at most 12, best first, only EXISTING implementations of a need or a sketched component. "
    "MUST means writing new code for that need instead of using or extending this would be a defect a "
    "reviewer should reject; SHOULD is a strong default a spec may override with a stated reason. Files the "
    "build will merely edit and tests it must keep green are not seams.",
]

T2_RULES = (
    "GENERAL RULES THAT ALSO DECIDE A ROW:\n"
    "- VALUE TYPE. For every added field, prop, input or setting, name its value type (image or media, link "
    "or URL, colour, heading or rich text, date, enum, number, file) and find the field factory or primitive "
    "sibling code uses for that type. A plain text input for a typed value is at least `should-extend`.\n"
    "- SAME MODULE. For every function added to a module that already exists, read every function in that "
    "module whose name or docstring shares a noun with it. A variant doing the same walk with a small "
    "difference (fences, quotes, CRLF, a default) is the seam.\n"
    "- REACHABILITY. Never answer `new` because the existing seam sits in another kit, package or language. "
    "That is `should-extend` through the repo's sanctioned sharing mechanism: an inline copy under a parity "
    "gate, a shared library, or a port with a parity test.\n"
    "- DOSSIERS. A dossier reuse affordance, a generator or a canonical copy in the house index that covers "
    "a unit binds it: hand-writing what a generator emits is `duplicate`.\n"
    "- DO NOT TRUST the diff's own comments about what exists or is unreachable; verify in the tree.\n"
    "- A SPEC ITEM unit (a scope line of a spec the diff adds) is judged like code: does the design it "
    "commits to re-implement something the tree has?")

WIRING = (
    "THE ORIENTATION'S BINDING SEAMS. Before the spec was written, a reuse scout bound these seams for this "
    "work (the card's `## reuse`):\n{card}\nFor EACH MUST line, add a `wiring` row: {{seam, verdict "
    "used|bypassed|not-applicable, why}}. `bypassed` means the diff re-implements or ignores the seam where "
    "it applies. A bypassed MUST is reported as a `duplicate` seam too.")


def render_trees(case, tree_root):
    tree = (Path(tree_root) / case["short"] / case["repo"]).as_posix()
    text = f"PRIMARY TREE ({case['repo']}): {tree}"
    if case.get("core_point_sha"):
        text += ("\nHOST CORE TREE (incms, the platform this package installs into; its blocks, DSL, theme "
                 f"and UI primitives are available to the package): {(Path(tree_root) / case['short'] / 'incms').as_posix()}")
    return text


def render_orient_question(case, tree_root):
    index = (Path(tree_root) / case["short"] / "house-index.md").as_posix()
    return "\n\n".join([
        "You are the REUSE SCOUT for a request that has not been specced yet. Your output becomes binding "
        "instructions for whoever specs and builds it, so precision matters as much as recall. This task "
        "block OVERRIDES your role's pointer to reuse-lookup.agent.md.",
        render_trees(case, tree_root),
        "RULES: work ONLY inside the tree(s) above, read-only. Never read anything under C:/projects or any "
        "other checkout, and never consult git history beyond the tree HEAD: you stand at the moment the "
        "request arrived.",
        'THE REQUEST:\n"""' + case["prompt"] + '"""',
        *[s.replace("{index}", index) for s in ORIENT_STEPS],
        ORIENT_CONTRACT,
    ])


def render_card(seams):
    rows = [f"- {s.get('binding', 'SHOULD')} `{s.get('path')}` :: `{s.get('symbol')}` — {s.get('how', '')}"
            for s in seams or [] if s.get("binding") in ("MUST", "SHOULD")]
    return "\n".join(rows) or "(the scout bound no seam)"


SPEC_ITEM = re.compile(r"^\+\s*-\s+\*\*(S\d+)\*\*\s*(?:—|-)?\s*(.{0,80})")
CSS_VALUE = re.compile(r"(?<![\w.-])(\d+(?:\.\d+)?(?:px|rem|em)|#[0-9a-fA-F]{3,8})\b")
TOKEN_DEF = re.compile(r"(--[a-z][\w-]*)\s*:\s*([^;{}\"]+?)\s*[;}\"]")


def read_tokens(tree):
    """`--token: value` definitions across the tree's CSS and JSON, keyed by the literal value."""
    out = {}
    hits = bench.run_git(tree, "grep", "-h", "-o", "-E", "-e", r"--[a-z][a-zA-Z0-9_-]*\s*:\s*[^;{}\"]{1,40}[;}\"]",
                         "--", "*.css", "*.json", check=False)
    for m in TOKEN_DEF.finditer(hits):
        value = m.group(2).strip().lower()
        if CSS_VALUE.fullmatch(value):
            out.setdefault(value, set()).add(m.group(1))
    return out


def extract_units_t2(diff_text, tree):
    """T1's units, plus a spec diff's scope items and every added CSS literal equal to a token's value."""
    units = d1v2.extract_units(diff_text)
    path = None
    tokens = read_tokens(tree)
    literal = []
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
            continue
        if not path or not line.startswith("+"):
            continue
        m = SPEC_ITEM.match(line)
        if m and "/spec/" in path:
            units.append(("spec-item", f"{m.group(1)} {m.group(2).strip()}", path))
        for v in CSS_VALUE.findall(line):
            names = tokens.get(v.lower())
            if names and ("--" not in line.split(v)[0][-30:]):
                literal.append(("literal", f"{v} == {', '.join(sorted(names)[:3])}", path))
    seen, first = set(), []
    for u in literal:
        if (u[1], u[2]) not in seen and len(first) < 10:
            seen.add((u[1], u[2]))
            first.append(u)
    # The token matches lead the list, so the lister's cap never drops them behind a long code diff.
    return first + [u for u in units if u[0] == "spec-item"] + [u for u in units if u[0] != "spec-item"]


def render_diff_question(case, units, variant, card=None, index=None):
    question = d1v2.render_question(case, units)
    parts = question.split("\n\nFOR EACH LISTED UNIT", 1)
    extra = []
    if variant == "t2":
        if index:
            extra.append(f"HOUSE INDEX. Read {index} first: shared libraries, canonical copies, most-reused "
                         "symbols, gate legs, lint rules, dossier reuse affordances, design tokens and DSL node "
                         "kinds of the tree before the diff. Every entry is a candidate seam.")
        extra.append(T2_RULES)
    if card is not None:
        extra.append(WIRING.format(card=card))
    body = parts[0] + "".join("\n\n" + e for e in extra) + "\n\nFOR EACH LISTED UNIT" + parts[1]
    if card is not None:
        body = body.replace("keys: rows (every row above), seams, verdict.",
                            "keys: rows (every row above), seams, wiring, verdict.")
    return body


def run_diff_questions(d1_root, out_dir, variant, results=None, orient_arm=None):
    cases = bench.read_json(Path(d1_root) / "d1.cases.json")
    cores = {}
    for corpus, tree_root in CORE_SOURCES:
        if Path(corpus).exists():
            cores.update({r["id"]: (Path(tree_root) / r["short"] / "incms").as_posix()
                          for r in bench.read_json(corpus) if r.get("core_point_sha")})
    res = bench.read_json(results).get(orient_arm, {}) if results else {}
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for short, c in cases.items():
        if not c.get("core_tree") and c["id"] in cores:
            c = dict(c, core_tree=cores[c["id"]])
        diff = Path(c["diff"]).read_text(encoding="utf-8", errors="replace")
        units = extract_units_t2(diff, c["tree"]) if variant == "t2" else d1v2.extract_units(diff)
        index = None
        if variant == "t2":
            index = Path(d1_root) / short / "house-index.md"
            if not index.exists():
                index.write_text(bench.render_house_index(c["tree"], "pre-diff tree") + "\n",
                                 encoding="utf-8", newline="\n")
            index = index.as_posix()
        card = render_card((res.get(c["id"]) or {}).get("seams")) if results else None
        (out / f"{c['id']}.txt").write_text(render_diff_question(c, units, variant, card, index),
                                            encoding="utf-8")
        print(f"{c['id']:<36} units {len(units):>4}" + (f" card {card.count(chr(10)) + 1 if card else 0}" if results else ""))


def run_orient_questions(corpus, tree_root, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for c in bench.read_json(corpus):
        if not c.get("ground_truth"):
            continue
        (out / f"{c['id']}.txt").write_text(render_orient_question(c, tree_root), encoding="utf-8")
        print(c["id"])


JSON_BLOCK = re.compile(r"```json\s*(.*?)```", re.S)


def extract_reply(text):
    """The last ```json block. A reply may quote ``` inside a JSON string, so the fallback decodes one
    JSON value from the last fence instead of stopping at the first closing fence."""
    blocks = JSON_BLOCK.findall(text)
    try:
        return json.loads(blocks[-1]) if blocks else None
    except json.JSONDecodeError:
        start = text.rfind("```json")
        try:
            return json.JSONDecoder().raw_decode(text[start + 7:].lstrip())[0]
        except json.JSONDecodeError:
            return None


def run_collect(results, arm, reports):
    doc = bench.read_json(results) if Path(results).exists() else {}
    rows = doc.setdefault(arm, {})
    bad = 0
    for spec in reports:
        cid, _, f = spec.partition("=")
        rows[cid] = extract_reply(Path(f).read_text(encoding="utf-8", errors="replace"))
        bad += rows[cid] is None
    bench.write_json(results, doc)
    print(f"{arm}: {len(reports)} report(s), {bad} unparsed")


def run_packets(corpus, results, tree_root, d1_root, out_dir, arms):
    out = Path(out_dir)
    bench.cmd_judge_packets([corpus, results, str(out), tree_root] + arms)
    cases = bench.read_json(Path(d1_root) / "d1.cases.json")
    for short, c in cases.items():
        packet = out / f"{short}.md"
        if packet.exists():
            packet.write_text(packet.read_text(encoding="utf-8") + "\n## The diff under review (diff-time arms)\n\n"
                              f"- diff: {c['diff']} (commit subject: \"{c['subject']}\")\n"
                              f"- pre-diff tree: {c['tree']}\n", encoding="utf-8", newline="\n")
    keep = {c["short"] for c in bench.read_json(corpus) if c.get("ground_truth")}
    for p in out.glob("*.md"):
        if p.stem not in keep:
            p.unlink()
    print(f"{len(keep)} packets in {out}")


def run_judge_collect(corpus, results, key_file, reports):
    key = json.loads(Path(key_file).read_text(encoding="utf-8"))
    shorts = {c["short"]: c["id"] for c in bench.read_json(corpus)}
    doc = bench.read_json(results)
    verdicts = doc.setdefault("judge2", {})
    bad = 0
    for spec in reports:
        short, _, f = spec.partition("=")
        reply = extract_reply(Path(f).read_text(encoding="utf-8", errors="replace"))
        if not reply or "arms" not in reply:
            bad += 1
            continue
        for a in reply["arms"]:
            arm = key.get(short, {}).get(a.get("label"))
            if not arm:
                continue
            cell = {k: a.get(k) for k in ("covered", "primary", "wrong", "valid_extra", "score", "note")}
            if isinstance(cell["valid_extra"], dict):
                cell["valid_extra"] = sum(v for v in cell["valid_extra"].values() if isinstance(v, int))
            cell["primary"] = bool(cell["primary"]) and cell["primary"] not in ("false", "none", "None")
            verdicts.setdefault(arm, {})[shorts[short]] = cell
    bench.write_json(results, doc)
    print(f"judge2: {len(reports)} report(s), {bad} unparsed")


def run_system(corpus, results, arms):
    """Judged primary per case for each arm, then the union of the orient arm with each diff arm."""
    judge = bench.read_json(results).get("judge2", {})
    # A case no arm was judged on (a pre-spec case with no diff) is outside the population, not a miss.
    ids = [c["id"] for c in bench.read_json(corpus)
           if c.get("ground_truth") and any(judge.get(a, {}).get(c["id"]) for a in arms)]
    covered = lambda a, i: bool((judge.get(a, {}).get(i) or {}).get("primary"))
    print(f"{'case':<36}" + "".join(f"{a[:14]:>15}" for a in arms))
    for i in ids:
        print(f"{i:<36}" + "".join(f"{('P' if covered(a, i) else '.'):>15}" for a in arms))
    for a in arms:
        cells = [judge.get(a, {}).get(i) for i in ids if judge.get(a, {}).get(i)]
        wrong = sum(len(c.get("wrong") or []) for c in cells)
        print(f"# {a:<24} primary {sum(covered(a, i) for i in ids)}/{len(ids)} · judged {len(cells)} · wrong {wrong}")
    orient = arms[0]
    for a in arms[1:]:
        print(f"# system {orient} + {a}: {sum(covered(orient, i) or covered(a, i) for i in ids)}/{len(ids)}")


def main(argv):
    verb, rest = (argv[0], argv[1:]) if argv else ("", [])
    if verb == "orient-q" and len(rest) == 3:
        run_orient_questions(*rest)
    elif verb == "card" and len(rest) == 4:
        seams = (bench.read_json(rest[0]).get(rest[1], {}).get(rest[2]) or {}).get("seams")
        Path(rest[3]).write_text("# card\n\n## reuse\n\n" + render_card(seams) + "\n", encoding="utf-8")
    elif verb == "diff-q" and len(rest) in (3, 5):
        run_diff_questions(*rest)
    elif verb == "units-t2" and len(rest) == 2:
        for kind, name, path in extract_units_t2(Path(rest[0]).read_text(encoding="utf-8", errors="replace"), rest[1]):
            print(f"{kind}\t{name}\t{path}")
    elif verb == "collect" and len(rest) > 2:
        run_collect(rest[0], rest[1], rest[2:])
    elif verb == "packets" and len(rest) > 5:
        run_packets(rest[0], rest[1], rest[2], rest[3], rest[4], rest[5:])
    elif verb == "judge-collect" and len(rest) > 3:
        run_judge_collect(rest[0], rest[1], rest[2], rest[3:])
    elif verb == "system" and len(rest) > 3:
        run_system(rest[0], rest[1], rest[2:])
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
