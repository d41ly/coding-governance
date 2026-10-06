#!/usr/bin/env python3
# **Serves:** journal TOOL-aMendedFleet-93
#
# The instrument of the charter A/B: one tier2-review run with the default worker type (arm A) and one
# with `workerType: 'Plan'` (arm B), over one landed range. Four verbs; none spawns an agent.
#
#     python <this> --selftest [--scratch D]   # a fixture session tree, every verb asserted over it
#     python <this> tokens --session SID --arm-a WF --arm-b WF [--projects-root P]
#                                              # one row per workflow agent into the judges rows
#     python <this> arms                       # the two committed return objects, validity fields
#     python <this> aggregate                  # COMMITTED files only: the table, both medians,
#                                              # both precisions and ONE verdict word
#
# `WF` is a workflow run directory's name under `<session>/subagents/workflows/`. A judge is a finder
# (`find:` label) or a skeptic batch (`verify:` label); `synth` and `resume:probe` are orchestration;
# any other label, or none, is UNCLASSIFIED and makes its arm INVALID by name, never a zero.
# A judge's first-turn context is `in + cache_read + cache_write` of the FIRST `usage` event of a
# one-file runlog `SessionTree` over its transcript, built as `scan_owner_turns` builds one.
#
# WHAT THIS DOES NOT CHECK: that the committed return objects are the ones the Workflow tool returned,
# or that the judges' transcripts are whole. It reads what it is given; the run brief says how each
# file got here.
import argparse
import json
import pathlib
import re
import sys
import tempfile
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
STEM = "2026-10-06-build-TOOL-aMendedFleet-93-"
ARM_FILES = {"A": HERE / (STEM + "arm-a.json"), "B": HERE / (STEM + "arm-b.json")}
JUDGES = HERE / (STEM + "judges.tsv")
SUBJECT_RECORD = (REPO / "memory" / "builds" / "aWindowedPass" / "reviews"
                  / "2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md")
COLUMNS = ("arm", "agent", "label", "role", "agent_type", "first_turn", "out")
JUDGE_ROLES = ("finder", "skeptic")
VALID_FIELDS = (("exit", "complete"), ("lensesReused", 0), ("batchesReused", 0),
                ("lensesDead", 0), ("skepticsDead", 0))
PRECISION_SLACK = Fraction(5, 100)
CONTEXT_RATIO = Fraction(85, 100)
SUBJECT_RE = re.compile(r"raw \*\*(\d+)\*\* · confirmed \*\*(\d+)\*\* · refuted \*\*(\d+)\*\*"
                        r".*precision \*\*([0-9.]+)\*\*")


def load_extract():
    sys.path.insert(0, str(REPO / "tools" / "runlog"))
    import extract  # the transcript seam the spec reuses: SessionTree + extract_session
    return extract


def derive_role(label):
    if not label:
        return "unclassified"
    if label.startswith("find:"):
        return "finder"
    if label.startswith("verify:"):
        return "skeptic"
    if label in ("synth", "resume:probe"):
        return "orchestration"
    return "unclassified"


def derive_first_turn(extract, sid, path):
    """`(first-turn context, summed out)` of one agent transcript, or `(None, 0)` with no usage."""
    one = extract.SessionTree(sid=sid, main=path)
    uses = [e for e in extract.extract_session(one)["events"] if e["kind"] == "usage"]
    if not uses:
        return None, 0
    first = uses[0]
    return first["in"] + first["cache_read"] + first["cache_write"], sum(e["out"] for e in uses)


def scan_agents(projects_root, sid, runs):
    """One row per workflow agent of each arm's run, read from its transcript and its meta file."""
    extract = load_extract()
    tree = extract.resolve_session_tree(sid, projects_root)
    if tree.main is None:
        raise SystemExit(f"t93: no transcript for session {sid} under {projects_root}")
    rows = []
    for arm, run in runs.items():
        paths = [p for p in tree.workflow_agents if p.parent.name == run]
        if not paths:
            raise SystemExit(f"t93: DEAD PROBE: workflow run {run} (arm {arm}) holds no agent")
        for path in paths:
            meta_path = path.with_name(path.name[:-len(".jsonl")] + ".meta.json")
            meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
            label = meta.get("description") or ""
            first, out = derive_first_turn(extract, sid, path)
            rows.append({"arm": arm, "agent": path.stem, "label": label or "-",
                         "role": derive_role(label), "agent_type": meta.get("agentType") or "-",
                         "first_turn": "-" if first is None else str(first), "out": str(out)})
    rows.sort(key=lambda r: (r["arm"], r["label"], r["agent"]))
    return rows


def write_rows(path, rows):
    lines = ["\t".join(COLUMNS)] + ["\t".join(r[c] for c in COLUMNS) for r in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def read_rows(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != COLUMNS:
        raise SystemExit(f"t93: {path.name} does not open with the header {' '.join(COLUMNS)}")
    return [dict(zip(COLUMNS, line.split("\t"))) for line in lines[1:] if line]


def read_arm(path):
    if not path.exists():
        raise SystemExit(f"t93: {path.name} is not committed; the arms have not run")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise SystemExit(f"t93: {path.name} is not a JSON object")
    return obj


def check_arm(obj, rows):
    """The reasons an arm is NOT valid; empty when it is."""
    bad = [f"{k}={obj.get(k)!r}, not {want!r}" for k, want in VALID_FIELDS if obj.get(k) != want]
    roles = [r["role"] for r in rows]
    if not any(r in JUDGE_ROLES for r in roles):
        bad.append("no judge row")
    if "unclassified" in roles:
        bad.append(f"{roles.count('unclassified')} unclassified agent(s)")
    unmeasured = [r["label"] for r in rows if r["role"] in JUDGE_ROLES and r["first_turn"] == "-"]
    if unmeasured:
        bad.append(f"no first-turn figure for {', '.join(unmeasured)}")
    return bad


def derive_median(values):
    s = sorted(values)
    if not s:
        return None
    mid = len(s) // 2
    return Fraction(s[mid]) if len(s) % 2 else Fraction(s[mid - 1] + s[mid], 2)


def derive_verdict(arms, rows):
    """`(word, per-arm figures)` by the rule the run brief registered before either arm ran."""
    figures = {}
    for arm in ("A", "B"):
        mine = [r for r in rows if r["arm"] == arm]
        judges = [r for r in mine if r["role"] in JUDGE_ROLES]
        firsts = [int(r["first_turn"]) for r in judges if r["first_turn"] != "-"]
        figures[arm] = {
            "bad": check_arm(arms[arm], mine),
            "finders": sum(r["role"] == "finder" for r in judges),
            "skeptics": sum(r["role"] == "skeptic" for r in judges),
            "unclassified": sum(r["role"] == "unclassified" for r in mine),
            "median": derive_median(firsts),
            "judge_out": sum(int(r["out"]) for r in judges),
            "precision": Fraction(str(arms[arm].get("precision", 0))),
            "types": sorted({r["agent_type"] for r in judges}),
        }
    a, b = figures["A"], figures["B"]
    if a["bad"] or b["bad"]:
        return "INVALID", figures
    if b["precision"] >= a["precision"] - PRECISION_SLACK and b["median"] <= CONTEXT_RATIO * a["median"]:
        return "DEFAULT-PLAN", figures
    return "KEEP-DEFAULT", figures


def render_number(x):
    if x is None:
        return "-"
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}"


def render_table(arms, figures):
    head = ("| arm | finders | skeptics | unclassified | median first-turn | judge out | precision "
            "| confirmed | refuted | blockers | highs | judge types |")
    lines = [head, "|" + "---|" * 12]
    for arm in ("A", "B"):
        f, o = figures[arm], arms[arm]
        cells = [arm, f["finders"], f["skeptics"], f["unclassified"], render_number(f["median"]),
                 f["judge_out"], f"{float(f['precision']):.2f}", o.get("confirmed", "-"),
                 o.get("refuted", "-"), o.get("blockers", "-"), o.get("highs", "-"),
                 " ".join(f["types"]) or "-"]
        lines.append("| " + " | ".join(str(c) for c in cells) + " |")
    return lines


def render_reading(arms, rows):
    word, figures = derive_verdict(arms, rows)
    out = render_table(arms, figures)
    for arm in ("A", "B"):
        out.append(f"arm {arm}: " + ("VALID" if not figures[arm]["bad"]
                                     else "NOT VALID — " + "; ".join(figures[arm]["bad"])))
    b_types, a_types = figures["B"]["types"], figures["A"]["types"]
    out.append(f"types: arm-B judges {'all Plan' if b_types == ['Plan'] else 'NOT all Plan'}; "
               f"arm-A judges {'none Plan' if 'Plan' not in a_types else 'SOME Plan'}")
    if SUBJECT_RECORD.exists():
        m = SUBJECT_RE.search(SUBJECT_RECORD.read_text(encoding="utf-8"))
        if m:
            out.append(f"subject round 1, recorded, reported and never compared: raw {m.group(1)} · "
                       f"confirmed {m.group(2)} · refuted {m.group(3)} · precision {m.group(4)}")
    out.append(f"verdict: {word}")
    return word, out


def run_tokens(a):
    projects = pathlib.Path(a.projects_root) if a.projects_root else load_extract().resolve_projects_root()
    rows = scan_agents(projects, a.session, {"A": a.arm_a, "B": a.arm_b})
    write_rows(JUDGES, rows)
    for arm in ("A", "B"):
        mine = [r for r in rows if r["arm"] == arm]
        roles = {k: sum(r["role"] == k for r in mine) for k in JUDGE_ROLES + ("orchestration", "unclassified")}
        print(f"tokens: arm {arm} " + " ".join(f"{k}={v}" for k, v in roles.items()))
    print(f"tokens: {len(rows)} rows -> {JUDGES.name}")
    return 1 if any(r["role"] == "unclassified" for r in rows) else 0


def run_arms(_a):
    bad = 0
    for arm in ("A", "B"):
        obj = read_arm(ARM_FILES[arm])
        fails = [f"{k}={obj.get(k)!r}" for k, want in VALID_FIELDS if obj.get(k) != want]
        print(f"arms: {arm} " + " ".join(f"{k}={obj.get(k)!r}" for k, _ in VALID_FIELDS)
              + (" — OK" if not fails else " — FAILS " + " ".join(fails)))
        bad += bool(fails)
    return 1 if bad else 0


def run_aggregate(_a):
    arms = {arm: read_arm(path) for arm, path in ARM_FILES.items()}
    if not JUDGES.exists():
        raise SystemExit(f"t93: {JUDGES.name} is not committed; run `tokens` first")
    word, lines = render_reading(arms, read_rows(JUDGES))
    print("\n".join(lines))
    return 0


# ---------------------------------------------------------------------------------- selftest

def build_agent(wf_dir, name, label, agent_type, usages):
    """One fixture agent: a transcript with one assistant record per `(in, read, write, out)`."""
    wf_dir.mkdir(parents=True, exist_ok=True)
    recs = []
    for i, (tin, tcr, tcw, tout) in enumerate(usages):
        recs.append({"type": "assistant", "uuid": f"{name}-{i}", "isSidechain": True,
                     "timestamp": f"2026-10-06T10:00:0{i}Z", "requestId": f"req-{name}-{i}",
                     "message": {"id": f"msg-{name}-{i}", "model": "m", "content": [],
                                 "usage": {"input_tokens": tin, "cache_read_input_tokens": tcr,
                                           "cache_creation_input_tokens": tcw, "output_tokens": tout}}})
    (wf_dir / f"agent-{name}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs),
                                                encoding="utf-8", newline="\n")
    meta = {"agentType": agent_type, "spawnDepth": 1}
    if label:
        meta["description"] = label
    (wf_dir / f"agent-{name}.meta.json").write_text(json.dumps(meta), encoding="utf-8")


def check_selftest(scratch):
    sid = "93939393-0000-4000-8000-000000000093"
    arm_ok = {"exit": "complete", "lensesReused": 0, "batchesReused": 0, "lensesDead": 0,
              "skepticsDead": 0, "precision": 0.9, "confirmed": 9, "refuted": 1}
    with tempfile.TemporaryDirectory(dir=scratch) as tmp:
        projects = pathlib.Path(tmp) / "projects"
        sdir = projects / "p" / sid
        sdir.mkdir(parents=True)
        (projects / "p" / f"{sid}.jsonl").write_text(json.dumps(
            {"type": "user", "uuid": "u0", "timestamp": "2026-10-06T10:00:00Z",
             "message": {"role": "user", "content": "go"}}) + "\n", encoding="utf-8", newline="\n")
        wa, wb = sdir / "subagents" / "workflows" / "wf_a", sdir / "subagents" / "workflows" / "wf_b"
        build_agent(wa, "a1", "find:seams", "workflow-subagent", [(1000, 200, 300, 40), (5000, 0, 0, 60)])
        build_agent(wa, "a2", "verify:ids-1-2", "workflow-subagent", [(2000, 500, 500, 10), (9, 9, 9, 5)])
        build_agent(wa, "a3", "synth", "workflow-subagent", [(7000, 0, 0, 70)])
        build_agent(wa, "a4", "resume:probe", "workflow-subagent", [(100, 0, 0, 1)])
        build_agent(wa, "a5", "", "workflow-subagent", [(50, 0, 0, 2)])  # the unlabelled agent
        build_agent(wb, "b1", "find:seams", "Plan", [(600, 0, 0, 30), (1, 1, 1, 1)])
        build_agent(wb, "b2", "find:security", "Plan", [(400, 400, 0, 20)])
        build_agent(wb, "b3", "verify:ids-1-3", "Plan", [(900, 0, 100, 15)])
        build_agent(wb, "b4", "synth", "workflow-subagent", [(7000, 0, 0, 70)])
        rows = scan_agents(projects, sid, {"A": "wf_a", "B": "wf_b"})
        by = {(r["arm"], r["label"]): r for r in rows}
        checks = [
            ("finder first turn is in+read+write of the FIRST usage", by[("A", "find:seams")]["first_turn"] == "1500"),
            ("skeptic first turn", by[("A", "verify:ids-1-2")]["first_turn"] == "3000"),
            ("out is summed over every usage", by[("A", "find:seams")]["out"] == "100"),
            ("arm-B first turns", [by[("B", k)]["first_turn"] for k in ("find:seams", "find:security",
                                   "verify:ids-1-3")] == ["600", "800", "1000"]),
            ("the unlabelled agent is unclassified", by[("A", "-")]["role"] == "unclassified"),
            ("orchestration is no judge", by[("A", "synth")]["role"] == "orchestration"),
            ("every arm-B judge is Plan", all(r["agent_type"] == "Plan" for r in rows
                                              if r["arm"] == "B" and r["role"] in JUDGE_ROLES)),
        ]
        word, fig = derive_verdict({"A": arm_ok, "B": arm_ok}, rows)
        checks += [("arm-A median over its two judges", fig["A"]["median"] == 2250),
                   ("arm-B median over its three judges", fig["B"]["median"] == 800),
                   ("an unclassified agent makes its arm INVALID", word == "INVALID")]
        clean = [r for r in rows if r["role"] != "unclassified"]
        cases = [(0.86, {}, "DEFAULT-PLAN"), (0.84, {}, "KEEP-DEFAULT"),
                 (0.95, {"lensesReused": 1}, "INVALID"), (0.95, {"exit": "deferred-platform"}, "INVALID")]
        for prec, extra, want in cases:
            b = dict(arm_ok, precision=prec, **extra)
            checks.append((f"rule: B precision {prec} {extra or ''} -> {want}",
                           derive_verdict({"A": arm_ok, "B": b}, clean)[0] == want))
        slow = [dict(r, first_turn=str(int(r["first_turn"]) * 3)) if r["arm"] == "B" and r["role"] in
                JUDGE_ROLES else r for r in clean]
        checks.append(("rule: B context above 0.85 of A -> KEEP-DEFAULT",
                       derive_verdict({"A": arm_ok, "B": arm_ok}, slow)[0] == "KEEP-DEFAULT"))
        tsv = pathlib.Path(tmp) / "rows.tsv"
        write_rows(tsv, rows)
        checks.append(("rows round-trip through the TSV", read_rows(tsv) == rows))
    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"selftest: {'ok  ' if ok else 'FAIL'} {name}")
    print(f"selftest: {len(checks) - len(failed)}/{len(checks)} passed")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(prog="t93")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--scratch", default=None, help="the selftest's temporary-directory parent")
    sub = ap.add_subparsers(dest="verb")
    t = sub.add_parser("tokens")
    t.add_argument("--session", required=True)
    t.add_argument("--arm-a", required=True)
    t.add_argument("--arm-b", required=True)
    t.add_argument("--projects-root", default=None)
    sub.add_parser("arms")
    sub.add_parser("aggregate")
    s = sub.add_parser("selftest")
    s.add_argument("--scratch", default=None)
    a = ap.parse_args()
    if a.selftest or a.verb == "selftest":
        return check_selftest(a.scratch)
    verbs = {"tokens": run_tokens, "arms": run_arms, "aggregate": run_aggregate}
    if a.verb not in verbs:
        ap.error("a verb or --selftest is required")
    return verbs[a.verb](a)


if __name__ == "__main__":
    sys.exit(main())
