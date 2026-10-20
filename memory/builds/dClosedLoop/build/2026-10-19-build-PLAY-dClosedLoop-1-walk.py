# **Serves:** research PLAY-dClosedLoop-1
"""The whole-design audit's walk: each walker's brief rendered from the round record, and each walk table checked
complete against its slice.

The round record, `2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, holds the scenarios (`[scenarios]`), the two
runs' slices (`[slicing]`), the table's grammar (`[walk-table]`) and the critical rubric (`[rubric]`). This script reads
them, so a brief and the check over its return share one source. The items are the design map's: the flow items by
step and the expansions' items, read through the atlas's derivation.

Usage (from the worktree root):
  python walk.py brief --run A|B --seeded <tree> --leads <file> --key-sha <hex> --out <dir> [--scratch <dir>]
                      [--walkers 1,3]
      writes the run's walker briefs into <dir>, all five or those --walkers names, each naming the sealed copy, the
      only places its walker may read, every item its table owes, Stage 0's leads and the sealed key's SHA-256, which
      no brief renders without.
  python walk.py check --run A|B --walker <n> <return.md> [--plant <case>]
      one walker's return: every cell of its slice, every build and principle it owes, each in the grammar.
  python walk.py check --run A|B --report <report.md> [--plant <case>]
      a run's joined report: every cell of every slice, all 22 builds and all 42 principles.
  cases: drop-cell, bad-verdict, ghost-finding, no-reason, drop-build, drop-principle, extra-cell, dup-cell
  python walk.py skeptic --run A|B --returns <dir> --seeded <tree> --out <dir> [--scratch <dir>]
      the run's four skeptic briefs: the walkers' findings sorted by address and cut into four batches, never
      splitting one address, each batch with eight clean cells to attack, drawn the same way on every render.
  python walk.py synth --run A|B|C --returns <dir> --verdicts <dir> --report <path> --subjects <file> --out <dir>
      the run's synthesis brief, naming the report's path and its Subjects line.
  python walk.py brief --run C ... and check --run C ... --seeded <copy> [--plant <case> | no-against]
      run C, the clause walk (`[walk-run-c]`): one row per clause of the slice's builds, read from the copy's
      `[chain]`, each read against a named record; its skeptic and synth commands take --run C as the others do.
  python walk.py recheck --run A|B|C --report <report> --returns <dir> --seeded <copy> --out <dir> [--scratch <dir>]
      the second look's brief: every finding the report refutes, as its walker or skeptic wrote it, without the
      refutation.
  python walk.py recheck-apply --run A|B|C --report <report> --verdicts <second look's return>
      a refutation both skeptics made stands; a split moves the finding to `## Unverified`; the shape line follows.
Exit 1 on any finding, 2 on a slice or a record this script cannot read.

What it does not check: whether a verdict is right, which the skeptics test on a sample of clean cells; whether a
finding's address is the defect's, which the scorer reads; and the brief's prose, which is the template below.
"""
import datetime
import importlib.util
import random
import re
import sys
from pathlib import Path

B = "memory/builds/dClosedLoop/build/"
ROUND = B + "2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md"
SCENARIOS = [f"S{i}" for i in range(1, 8)]
TODAY = datetime.date.today().isoformat()   # a brief is named for the day it is rendered
ROW = re.compile(r"^\| `?([a-z]+\.[a-z0-9-]+)`? \| (S[1-7]) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|\s*$")
ID = r"[ABC](?:[1-5]|S[1-4])-F\d+"   # a walker's finding, or a new one a skeptic batch raises
FINDING = re.compile(r"^### (" + ID + r")\b", re.M)
VERDICT = re.compile(r"^(holds|" + ID + r"(?:, " + ID + r")*|not on path: \S.*)$")
VERDICT_ROW = re.compile(r"^\| `?((?:d[A-Z]\w+)|(?:P\d+))`? \| ([^|]+) \|\s*$")
PLANTS = ("drop-cell", "bad-verdict", "ghost-finding", "no-reason", "drop-build", "drop-principle", "extra-cell",
          "dup-cell", "no-against")
# Run C's clause table: `| clause | build | read against | verdict |`.
CROW = re.compile(r"^\| `?(cl-dClosedLoop-\d{4})`? \| `?(d[A-Z]\w+)`? \| ([^|]*) \| ([^|]*) \|\s*$")
V2 = "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"


def fail(msg, code=2):
    print(f"walk: {msg}")
    sys.exit(code)


def section(text, tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\][^\n]*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not m:
        fail(f"the round record has no [{tag}]")
    return m.group(1)


def rows(block, first):
    out = []
    for ln in block.split("\n"):
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
        if c and c[0] not in (first, "") and not set(c[0]) <= set("-:"):
            out.append(c)
    return out


def load():
    text = Path(ROUND).read_text(encoding="utf-8")
    scen = {c[0]: c for c in rows(section(text, "scenarios"), "Scenario")}
    if sorted(scen) != SCENARIOS:
        fail(f"[scenarios] holds {sorted(scen)}, where the walk needs S1 to S7")
    slices = {}
    for c in rows(section(text, "slicing"), "Run"):
        run, walker, scenarios, steps, builds, principles = c[:6]
        slices[(run, int(walker))] = {
            "scenarios": SCENARIOS if scenarios == "all" else re.findall(r"S[1-7]", scenarios),
            "steps": steps.split(", ") if steps != "all" else ["all"],
            "builds": re.findall(r"d[A-Z]\w+", builds), "principles": re.findall(r"P\d+", principles)}
    return text, scen, slices


def derive_items():
    spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
    mp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mp)
    A, ns = mp.derive()
    by_step = {s["tag"]: [it["tag"] for it in s["items"]] for s in A["steps"]}
    flow = {t for ts in by_step.values() for t in ts}
    by_step["expansions"] = [n["key"] for n in ns["item"] if n["key"] not in flow]
    builds = [c["build"] for c in A["chain"]]
    principles = [f"P{p['n']}" for p in A["principles"]]
    return by_step, builds, principles


def cells_of(slice_, by_step):
    steps = list(by_step) if slice_["steps"] == ["all"] else slice_["steps"]
    unknown = [s for s in steps if s not in by_step]
    if unknown:
        fail(f"a slice names steps the items do not have: {unknown}")
    return [(item, s) for step in steps for item in by_step[step] for s in slice_["scenarios"]]


def check(run, walker, path, plant=None):
    text, _, slices = load()
    by_step, all_builds, all_principles = derive_items()
    if walker is None:
        mine = [k for k in slices if k[0] == run]
        if len(mine) != 5:
            fail(f"[slicing] holds {len(mine)} walkers for run {run}, where a run has five")
        want = sorted({c for k in mine for c in cells_of(slices[k], by_step)})
        builds, principles = all_builds, all_principles
        covered_b = sorted(b for k in mine for b in slices[k]["builds"])
        covered_p = sorted(p for k in mine for p in slices[k]["principles"])
        if covered_b != sorted(all_builds) or covered_p != sorted(all_principles, key=str):
            fail(f"run {run}'s slices do not give every build and principle exactly one verdict")
    else:
        if (run, walker) not in slices:
            fail(f"[slicing] has no walker {walker} in run {run}")
        want = cells_of(slices[(run, walker)], by_step)
        builds, principles = slices[(run, walker)]["builds"], slices[(run, walker)]["principles"]
    body = Path(path).read_text(encoding="utf-8")
    lines = body.split("\n")
    table = [m.groups() for m in (ROW.match(ln) for ln in lines) if m]
    if plant == "drop-cell":
        table = table[1:]
    elif plant == "bad-verdict":
        table[0] = table[0][:6] + ("fine",)
    elif plant == "ghost-finding":
        table[0] = table[0][:6] + (f"{run}1-F999",)   # in the grammar, and carried by no heading
    elif plant == "no-reason":
        table[0] = table[0][:6] + ("not on path: ",)
    elif plant == "extra-cell":
        table.append(("plan.no-such-item", "S1", "=", "=", "=", "=", "holds"))
    elif plant == "dup-cell":
        table.append(table[0])
    findings = set(FINDING.findall(body))
    verdicts = {m.group(1): m.group(2).strip() for m in (VERDICT_ROW.match(ln) for ln in lines) if m}
    if plant == "drop-build" and builds:
        verdicts.pop(builds[0], None)
    elif plant == "drop-principle" and principles:
        verdicts.pop(principles[0], None)
    out = []
    seen = {}
    for item, scen, actor, needs, witness, route, verdict in table:
        key = (item, scen)
        if key in seen:
            out.append(f"{item} {scen}: two rows")
        seen[key] = verdict.strip()
        if key not in set(want):
            out.append(f"{item} {scen}: a cell outside the slice")
        v = verdict.strip()
        if not VERDICT.match(v) or v == "not on path:" or v.endswith("not on path:"):
            out.append(f"{item} {scen}: verdict '{v}' is not holds, a finding id or 'not on path: <reason>'")
        for f in re.findall(ID, v):
            if f not in findings:
                out.append(f"{item} {scen}: names {f}, which no finding heading carries")
        if any(not x.strip() for x in (actor, needs, witness, route)):
            out.append(f"{item} {scen}: an empty actor, needs, witness or route cell")
    missing = [c for c in want if c not in seen]
    for item, scen in missing:
        out.append(f"{item} {scen}: no row")
    for b in builds:
        if b not in verdicts:
            out.append(f"{b}: no build verdict")
    for p in principles:
        if p not in verdicts:
            out.append(f"{p}: no principle verdict")
    for k, v in verdicts.items():
        if not VERDICT.match(v) or v.startswith("not on path"):
            out.append(f"{k}: verdict '{v}' is not holds or finding ids")
    who = f"run {run}" + (f", walker {walker}" if walker else ", joined")
    print(f"walk check, {who}: cells {len(want)}, rows {len(table)}, findings {len(findings)}, "
          f"builds {len(builds)}, principles {len(principles)} · problems {len(out)}" + (f" · plant {plant}" if plant else ""))
    for o in out[:60]:
        print(f"  {o}")
    if len(out) > 60:
        print(f"  ... and {len(out) - 60} more")
    return 1 if out else 0


def clauses_of(tree):
    """Each chain build's clause ids, in chain order, read from a tree's v2 `[chain]`: run C's from the sealed copy,
    since its clauses are the ones its walkers can read."""
    path = Path(tree) / B / V2
    m = re.search(r"^## \[chain\][^\n]*\n(.*?)(?=^## )", path.read_text(encoding="utf-8"), flags=re.M | re.S)
    if not m:
        fail(f"{path.as_posix()} has no [chain]")
    out = {}
    for ln in m.group(1).split("\n"):
        r = re.match(r"^\| (d[A-Z]\w+) \|", ln)
        if r:
            out[r.group(1)] = re.findall(r"cl-dClosedLoop-\d{4}", ln)
    return out


def check_c(walker, path, seeded, plant=None):
    """Run C's return or report: one row per clause of the slice's builds in the copy, each read against a named record
    and given `holds` or finding ids that headings carry, and a verdict for every build. A row for a clause the copy
    lacks is accepted when its verdict names a finding, since a walker may report a clause missing."""
    _, _, slices = load()
    by_build = clauses_of(seeded)
    mine = sorted(k for k in slices if k[0] == "C")
    if walker is None:
        if len(mine) != 5:
            fail(f"[slicing] holds {len(mine)} walkers for run C, where a run has five")
        builds = [b for k in mine for b in slices[k]["builds"]]
        if sorted(builds) != sorted(by_build):
            fail("run C's slices do not give every chain build exactly one verdict")
    else:
        if ("C", walker) not in slices:
            fail(f"[slicing] has no walker {walker} in run C")
        builds = slices[("C", walker)]["builds"]
    want = [c for b in builds for c in by_build.get(b, [])]
    body = Path(path).read_text(encoding="utf-8")
    lines = body.split("\n")
    table = [m.groups() for m in (CROW.match(ln) for ln in lines) if m]
    if plant == "drop-cell":
        table = table[1:]
    elif plant == "bad-verdict":
        table[0] = table[0][:3] + ("fine",)
    elif plant == "ghost-finding":
        table[0] = table[0][:3] + ("C1-F999",)
    elif plant == "extra-cell":
        table.append(("cl-dClosedLoop-9999", builds[0], "v2 [chain]", "holds"))
    elif plant == "dup-cell":
        table.append(table[0])
    elif plant == "no-against":
        table[0] = table[0][:2] + (" ",) + table[0][3:]
    findings = set(FINDING.findall(body))
    verdicts = {m.group(1): m.group(2).strip() for m in (VERDICT_ROW.match(ln) for ln in lines) if m}
    if plant == "drop-build" and builds:
        verdicts.pop(builds[0], None)
    out, seen = [], set()
    for clause, build, against, verdict in table:
        v = verdict.strip()
        if clause in seen:
            out.append(f"{clause}: two rows")
        seen.add(clause)
        named = re.findall(ID, v)
        if clause not in want and not named:
            out.append(f"{clause}: a row outside the slice")
        if v != "holds" and not re.fullmatch(ID + r"(?:, " + ID + r")*", v):
            out.append(f"{clause}: verdict '{v}' is not holds or finding ids")
        for f in named:
            if f not in findings:
                out.append(f"{clause}: names {f}, which no finding heading carries")
        if not against.strip():
            out.append(f"{clause}: read against nothing")
    for c in want:
        if c not in seen:
            out.append(f"{c}: no row")
    for b in builds:
        if b not in verdicts:
            out.append(f"{b}: no build verdict")
        elif not VERDICT.match(verdicts[b]) or verdicts[b].startswith("not on path"):
            out.append(f"{b}: verdict '{verdicts[b]}' is not holds or finding ids")
    who = f"run C, walker {walker}" if walker else "run C, joined"
    print(f"walk check, {who}: clauses {len(want)}, rows {len(table)}, findings {len(findings)}, builds {len(builds)} · "
          f"problems {len(out)}" + (f" · plant {plant}" if plant else ""))
    for o in out[:60]:
        print(f"  {o}")
    if len(out) > 60:
        print(f"  ... and {len(out) - 60} more")
    return 1 if out else 0


TEMPLATE = """# Walk brief: run {run}, walker {walker}

**Serves:** research PLAY-dClosedLoop-1

**Your task is to walk dClosedLoop's design and report its defects.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one line
at the end of your return, and nowhere else.

You are one of five walkers in run {run} of the whole-design audit. Walk the design in the sealed copy as the slice
below says, item by item, following the copy's round record (`{seeded}/{round}`, its `[scenarios]`, `[walk-table]` and
`[rubric]`), and report every defect you can show. A second run walks the same design sliced the other way.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `{seeded}/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`: the
   walk reads the design, never its review history.
2. **The design map,** `{seeded}/design-map.txt`, as your index, and **Stage 0's leads,** `{leads}`, its whole run on
   the working tree: take the leads your slice reaches.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `{scratch}`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `{key_sha}`. Look for every defect the same way, since a planted one is scored like any other finding.

Read `flow-steps` whole, then v2 (`architecture-v2`): the `[chain]` rows of your builds, the `[policies]` keys your
items read, and `[principles]` and `[enforcement]` for your principles. {extra}

## Your slice

- **Scenarios:** {scenarios}
- **Steps:** {steps}
- **Items, each a row in every scenario of your slice:** {items}
- **Builds you give a verdict:** {builds}
- **Principles you give a verdict:** {principles}

{scenario_text}

## How you walk

1. **Open with a pre-mortem line:** "The chain shipped and failed in this scenario because ...", your best guess.
2. **Walk every item of your steps through every scenario of your slice.** For each: who acts, what it needs, what
   witnesses it, and where it routes, against what the records declare. Where the scenario never reaches the item,
   say why in the verdict.
3. **On every item a failure can reach,** read its failure mode, its effect and how it is detected (the FMEA columns),
   and say where the failure routes.
4. **On S2's and S4's trust boundaries** (nodes, the remote, adopters' trees), read each data flow for spoofing,
   tampering, repudiation, disclosure, denial and elevation.
5. **Check every K1 to K10 class** of the rubric over your slice, and grade each finding by the rubric.
6. **For each build and each principle of your slice,** say whether what it owns holds in your scenarios.

## What you return

Your final message, in this order, nothing else:

1. **The pre-mortem line.**
2. **Findings,** each as `### {run}{walker}-F<n> — <title>` and then these lines:
   - `- **Address:** <record> [<section tag>]`, the record by its name after `PLAY-dClosedLoop-1-` (`architecture-v2`,
     `flow-steps`, `layer-runtime`), the tag of the section holding the defect, and the clause id
     (`cl-dClosedLoop-NNNN`) or item tag (`plan.record`) when one carries it;
   - `- **Class:** K<n>`, and `c<n>` when the consequence is critical (`[rubric]`);
   - `- **Severity:** blocker, high, medium or low`;
   - `- **Scenario:** S<n>`;
   - `- **Evidence:**` what you read, quoted short, with its address;
   - `- **Consequence:**` what goes wrong, in the scenario;
   - `- **Fix:**` the smallest change that closes it.
3. **The walk table,** one row per item and scenario of your slice, every cell filled, in `[walk-table]`'s grammar:
   `| item | S<n> | actor | needs | witness | route | verdict |`, a cell that reads as declared written `=`.
4. **Build verdicts,** `| <build> | holds |` or `| <build> | <finding ids> |`.
5. **Principle verdicts,** `| P<n> | holds |` or `| P<n> | <finding ids> |`.
6. **Read outside the list above:** `none`, or each path you read outside it and why.

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `{scratch}` only. Your effort is the owner's medium.
"""
EXTRA = {"S2": "For S2 read `layer-runtime`, `cloud-and-scale` and `stall-and-loop` too.",
         "S4": "For S4 read `adopter-instructions`, `flow-roles-adoption`, `fates` and `layer-expansions` too.",
         "expansions": "The expansions' items are the rows of `layer-expansions`' Item tables: read it for them."}


def brief(run, seeded, leads, out_dir, scratch, key_sha, walkers=None):
    if not key_sha or not re.fullmatch(r"[0-9a-f]{64}", key_sha):
        fail("--key-sha takes the sealed key's SHA-256, 64 hex digits, pinned before any brief is rendered")
    text, scen, slices = load()
    by_step, _, _ = derive_items()
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for (r, w), sl in sorted(slices.items()):
        if r != run or (walkers and w not in walkers):
            continue
        steps = list(by_step) if sl["steps"] == ["all"] else sl["steps"]
        extra = " ".join(EXTRA[s] for s in sl["scenarios"] + steps if s in EXTRA)
        scenario_text = "\n".join(f"- **{s}, {scen[s][1]}:** {scen[s][2]} Injected or probed: {scen[s][3]}"
                                  for s in sl["scenarios"])
        items = "; ".join(f"{s}: " + ", ".join(f"`{t}`" for t in by_step[s]) for s in steps)
        body = TEMPLATE.format(run=run, walker=w, round=ROUND, seeded=Path(seeded).as_posix(), leads=leads, key_sha=key_sha,
                               extra=extra, scenarios=", ".join(sl["scenarios"]), items=items,
                               steps=", ".join(f"{s} ({len(by_step[s])} items)" for s in steps),
                               builds=", ".join(sl["builds"]), principles=", ".join(sl["principles"]),
                               scenario_text=scenario_text, scratch=f"{Path(scratch).as_posix()}/walk-{run.lower()}{w}/")
        p = out / f"{TODAY}-build-PLAY-dClosedLoop-1-walk-brief-{run.lower()}{w}.md"
        p.write_text(body, encoding="utf-8", newline="\n")
        print(f"wrote {p.as_posix()}: cells {len(cells_of(sl, by_step))}")
    return 0


TEMPLATE_C = """# Clause walk brief: run C, walker {walker}

**Serves:** research PLAY-dClosedLoop-1

**Your task is to read dClosedLoop's chain clauses for your builds and report what each one omits or contradicts.**
This brief is your instructions, not the subject of your review: do not review it, the audit's seal or its
instruments. A defect you see in them goes in one line at the end of your return, and nowhere else.

You are one of five walkers in run C of the whole-design audit. Two runs walked the design's items through scenarios;
this run reads its clauses, the `[chain]` rows of v2 (`architecture-v2`) in the sealed copy, each against the records
that settle what it builds. Grade by the copy's round record's `[rubric]` (`{seeded}/{round}`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `{seeded}/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `{seeded}/design-map.txt`, as your index, and **Stage 0's leads,** `{leads}`.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `{scratch}`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `{key_sha}`. Look for every defect the same way, since a planted one is scored like any other finding.

## Your slice

- **Builds, each given a verdict:** {builds}
- **Clauses, each a row of your table:** {clauses}

## How you read

1. **Open with a pre-mortem line:** "The chain shipped and failed because one of these clauses ...", your best guess.
2. **For each build,** read its `[chain]` row whole: its parents, its planned units and the gaps it owns.
3. **For each clause,** find the records that settle what it builds: the gaps its row owns (`gap-register`), the
   sections of the layer, flow and expansion records that define its items, kinds, keys and routes, and the records
   it cites. Then check that it carries every rule they settle for it, contradicts none of them and no other clause,
   and names only what its build or an ancestor owns, or a stand-in. A rule settled elsewhere that no clause of the
   build carries is a finding at the clause that should carry it.
4. **Read each build's clauses against the principles it enforces** (v2 `[principles]` and `[enforcement]`) and
   every K1 to K10 class of the rubric, and grade each finding by the rubric.

## What you return

Your final message, in this order, nothing else:

1. **The pre-mortem line.**
2. **Findings,** each as `### C{walker}-F<n> — <title>` and then these lines:
   - `- **Address:** architecture-v2 [chain] <clause id>`, or another record and its section when the defect lies
     there;
   - `- **Class:** K<n>`, and `c<n>` when the consequence is critical (`[rubric]`);
   - `- **Severity:** blocker, high, medium or low`;
   - `- **Evidence:**` the settling record's words and the clause's, quoted short, each with its address;
   - `- **Consequence:**` what goes wrong when the build is built from the clause as written;
   - `- **Fix:**` the smallest change that closes it.
3. **The clause table,** one row per clause of your slice: `| clause | build | read against | verdict |`, the clause
   id, its build, the records and sections you read it against (never empty), and `holds` or its findings' ids.
4. **Build verdicts,** `| <build> | holds |` or `| <build> | <finding ids> |`.
5. **Read outside the list above:** `none`, or each path you read outside it and why.

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `{scratch}` only. Your effort is the owner's medium.
"""


def brief_c(seeded, leads, out_dir, scratch, key_sha, walkers=None):
    if not key_sha or not re.fullmatch(r"[0-9a-f]{64}", key_sha):
        fail("--key-sha takes the sealed key's SHA-256, 64 hex digits, pinned before any brief is rendered")
    _, _, slices = load()
    by_build = clauses_of(seeded)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for (r, w), sl in sorted(slices.items()):
        if r != "C" or (walkers and w not in walkers):
            continue
        unknown = [b for b in sl["builds"] if b not in by_build]
        if unknown:
            fail(f"run C's walker {w} names builds the copy's [chain] lacks: {unknown}")
        clauses = [c for b in sl["builds"] for c in by_build[b]]
        body = TEMPLATE_C.format(walker=w, round=ROUND, seeded=Path(seeded).as_posix(), leads=leads, key_sha=key_sha,
                                 builds=", ".join(sl["builds"]),
                                 clauses="; ".join(f"{b}: " + ", ".join(f"`{c}`" for c in by_build[b])
                                                   for b in sl["builds"]),
                                 scratch=f"{Path(scratch).as_posix()}/walk-c{w}/")
        p = out / f"{TODAY}-build-PLAY-dClosedLoop-1-walk-brief-c{w}.md"
        p.write_text(body, encoding="utf-8", newline="\n")
        print(f"wrote {p.as_posix()}: clauses {len(clauses)}, builds {len(sl['builds'])}")
    return 0


SKEPTIC = """# Skeptic brief: run {run}, batch {batch}

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run {run} of the whole-design audit (`{seeded}/{round}`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`{seeded}/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `{seeded}/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `{seeded}/design-map.txt`, as your index, and **Stage 0's leads,** `{seeded}/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `{scratch}`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

{findings}

## Clean cells to attack

{cells}

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- {cell_form}: holds`, or `- {cell_form}: defect` with the defect written as a new
  finding in the walkers' grammar, its id `{run}S{batch}-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `{scratch}` only. Your effort is the one the owner's
role definition sets.
"""
SYNTH = """# Synthesis brief: run {run}

**Serves:** research PLAY-dClosedLoop-1

**Your task is to merge run {run} of the whole-design audit into one report, written to `{report}`.** This brief is
your instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you
see in them goes in one line at the end of your return, and nowhere else.

## What you may read, and nothing else

1. **The round record's** `[walk-table]` and `[rubric]` (`{round}`).
2. **The five walker returns and the four skeptics' verdicts:**

{inputs}

3. **This brief.**

Read nothing else, and judge no finding against a design record: the skeptics judged each against the sealed copy,
and the report carries their verdicts as they gave them.

Write the report in this shape, and nothing else into the repository:
1. `**Serves:** spec-audit PLAY-dClosedLoop-1`, a blank line, and `# Whole-design walk, run {run}: <its slicing>`.
2. One paragraph: what the run walked, sliced how, by five walkers, four skeptics and you.
3. This line, verbatim: `{subjects}`
4. `## Verdict: CLEAN`, `CLEAN WITH FIXES` or `BLOCKED`, and a paragraph naming every critical finding by id.
5. `## Critical`, `## High`, `## Medium` and `## Low`: every confirmed finding once, under its own heading and id in the
   walkers' grammar, with the skeptic's reason added as `- **Skeptic:**`, and `- **Same as:** <ids>` where two walkers
   found one defect.
6. `## Refuted`: every refuted finding under its own heading and id, with the skeptic's reason.
7. `## Walk table`: the five walkers' tables joined, every item in every scenario, verdicts as the walkers gave them.
8. `## Build verdicts` and `## Principle verdicts`: every build and every principle, joined.
9. `review-shape kind=spec-audit round=1 intensity=full at=synth raw=<n> confirmed=<n> refuted=<n> unverified=0
   blocker=<n> high=<n> medium=<n> low=<n> agents=0 out-tokens=0`, on one line; the main loop fills `agents` and
   `out-tokens` from the run's returned lines, every dispatch of the run counted.

`walk.py check --run {run} --report` must pass on it: every cell, every build and principle, and every id a verdict
names carried by a heading. Return the report's path, the critical findings' ids and, last,
`**Read outside the list above:** none`, or each path you read outside it and why. Your effort is the one the owner's
role definition sets.
"""


def _swap(text, pairs):
    for old, new in pairs:
        if text.count(old) != 1:
            raise SystemExit(f"walk: the synthesis template no longer holds {old[:50]!r} once")
        text = text.replace(old, new)
    return text


# Run C's synthesis: the same report, its table the clauses' and its verdicts the builds' alone.
SYNTH_C = _swap(SYNTH, [
    ("7. `## Walk table`: the five walkers' tables joined, every item in every scenario, verdicts as the walkers gave them.",
     "7. `## Clause table`: the five walkers' clause tables joined, every clause once, in their grammar\n"
     "   `| clause | build | read against | verdict |`, verdicts as the walkers gave them."),
    ("8. `## Build verdicts` and `## Principle verdicts`: every build and every principle, joined.",
     "8. `## Build verdicts`: every build, joined."),
    ("`walk.py check --run {run} --report` must pass on it: every cell, every build and principle, and every id a verdict",
     "`walk.py check --run C --report <report> --seeded <copy>` must pass on it: every clause, every build, and every id a\n"
     "verdict"),
])

RECHECK = """# Second-look brief: run {run}

**Serves:** research PLAY-dClosedLoop-1

**Your task is to judge each finding below: confirm it or refute it.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one
line at the end of your return, and nowhere else.

Each finding below was returned by a walker reading the sealed copy of the design at
`{seeded}/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Grade a confirmed one by the copy's round record's
`[rubric]` (`{seeded}/{round}`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `{seeded}/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `{seeded}/design-map.txt`, as your index, and **Stage 0's leads,** `{seeded}/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `{scratch}`.

Read nothing else: not the working tree's other records, not the walkers' returns or the reports, not the session's
scratchpad or temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it
alone, since the working tree may differ from it.

## Findings to judge

{findings}

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `{scratch}` only. Your effort is the one the owner's
role definition sets.
"""


def report_sections(text):
    """A report's `### <id>` blocks by the `## ` section holding them, in order: {section: [(id, block)]}."""
    out, section = {}, None
    for block in re.split(r"(?m)^(?=## |### )", text):
        h2 = re.match(r"## (\w+)", block)
        if h2:
            section = h2.group(1)
            continue
        m = re.match(r"### (" + ID + r")\b", block)
        if m and section:
            out.setdefault(section, []).append((m.group(1), block))
    return out


def recheck(run, report, returns_dir, seeded, out_dir, scratch):
    """The second look's brief: every finding the report refutes, each as its walker or skeptic wrote it, without the
    refutation, for a second skeptic to judge alone."""
    refuted = [i for i, _ in report_sections(Path(report).read_text(encoding="utf-8")).get("Refuted", [])]
    if not refuted:
        fail(f"{report} refutes nothing, so a second look has nothing to judge")
    text = {}
    for f in returns_of(run, returns_dir):
        text.update((x["id"], x["text"]) for x in findings_of(f.read_text(encoding="utf-8")))
    for f in sorted(Path(returns_dir).glob(f"*-skeptic-return-{run.lower()}[1-4].md")):
        body = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^[ \t]*(### (" + ID + r")\b.*?)(?=^[ \t]*### |^- |\Z)", body, flags=re.M | re.S):
            text.setdefault(m.group(2), m.group(1).strip())
    missing = [i for i in refuted if i not in text]
    if missing:
        fail(f"no walker or skeptic return carries {missing}")
    body = RECHECK.format(run=run, seeded=Path(seeded).as_posix(), round=ROUND,
                          findings="\n\n".join(text[i] for i in refuted),
                          scratch=f"{Path(scratch).as_posix()}/recheck-{run.lower()}/")
    p = Path(out_dir) / f"{TODAY}-build-PLAY-dClosedLoop-1-recheck-brief-{run.lower()}.md"
    p.write_text(body, encoding="utf-8", newline="\n")
    print(f"wrote {p.as_posix()}: findings {len(refuted)}")
    return 0


def recheck_apply(run, report, verdicts_path):
    """The second look applied to a report: a refutation both skeptics made stands, with the second's reason added; a
    split moves the finding to `## Unverified`, before `## Refuted`, with the second skeptic's grade and reason; the
    shape line's refuted and unverified counts follow. Refuses a refuted finding the second look did not judge."""
    path = Path(report)
    text = path.read_text(encoding="utf-8")
    refuted = report_sections(text).get("Refuted", [])
    ret = Path(verdicts_path).read_text(encoding="utf-8")
    judged = {}
    for m in re.finditer(r"^- \**(" + ID + r")\**: (confirmed (?:blocker|high|medium|low)|refuted)\b([^\n]*)\n(.*?)(?=^- |\Z)",
                         ret, flags=re.M | re.S):
        judged[m.group(1)] = (m.group(2), " ".join((m.group(3).strip(" .") + " " + m.group(4)).split()))
    missing = [i for i, _ in refuted if i not in judged]
    if missing:
        fail(f"the second look judged none of {missing}")
    moved = []
    for fid, block in refuted:
        verdict, why = judged[fid]
        note = f"- **Second skeptic:** {verdict[0].upper() + verdict[1:]}. {why}\n"
        new = block.rstrip("\n") + "\n" + note + "\n"
        if verdict.startswith("confirmed"):
            text = text.replace(block, "", 1)
            moved.append(new)
        else:
            text = text.replace(block, new, 1)
    if moved:
        head = "## Unverified\n\nA skeptic refuted each finding below and a second confirmed it, so it stands unverified.\n\n"
        text = text.replace("## Refuted", head + "".join(moved) + "## Refuted", 1)
    shape = re.search(r"^review-shape [^\n]*$", text, flags=re.M).group(0)
    line = re.sub(r"refuted=\d+", f"refuted={len(refuted) - len(moved)}", shape)
    line = re.sub(r"unverified=\d+", f"unverified={len(moved)}", line)
    path.write_text(text.replace(shape, line, 1), encoding="utf-8", newline="\n")
    print(f"recheck applied to {path.name}: {len(refuted)} judged, {len(refuted) - len(moved)} refutations stand, "
          f"{len(moved)} unverified ({', '.join(i for i, _ in refuted if judged[i][0].startswith('confirmed')) or 'none'})")
    return 0


def findings_of(text):
    out = []
    # A finding ends at the next heading, at any table row, or at a numbered bold label such as `3. **The walk
    # table**`: a return that sets its table under no heading would otherwise hand its last finding's skeptic the
    # walker's whole table and verdicts.
    for m in re.finditer(r"^### (" + ID + r")\b[^\n]*\n(.*?)(?=^#{1,3} |^\||^\d+\. \*\*|\Z)", text, flags=re.M | re.S):
        addr = re.search(r"^- \*\*Address:\*\* (.+)$", m.group(2), flags=re.M)
        out.append({"id": m.group(1), "text": m.group(0).strip(), "address": addr.group(1).strip() if addr else ""})
    return out


def returns_of(run, folder):
    files = sorted(Path(folder).glob(f"*-walk-return-{run.lower()}[1-5].md"))
    if len(files) != 5:
        fail(f"{folder} holds {len(files)} walker returns for run {run}, where a run has five")
    return files


def skeptic(run, returns_dir, seeded, out_dir, scratch):
    files = returns_of(run, returns_dir)
    found, clean = [], []
    for f in files:
        text = f.read_text(encoding="utf-8")
        found += findings_of(text)
        if run == "C":
            clean += [(m.group(1), m.group(2)) for m in (CROW.match(ln) for ln in text.split("\n"))
                      if m and m.group(4).strip() == "holds"]
        else:
            clean += [(m.group(1), m.group(2)) for m in (ROW.match(ln) for ln in text.split("\n"))
                      if m and m.group(7).strip() == "holds"]
    key = lambda f: re.sub(r"`", "", f["address"])   # noqa: E731  record, tag, and the clause or item carrying it
    found.sort(key=lambda f: (key(f), f["id"]))
    groups = []
    for f in found:
        if groups and key(groups[-1][-1]) == key(f):
            groups[-1].append(f)
        else:
            groups.append([f])
    # Four contiguous batches in address order, the largest as small as whole addresses allow.
    def pack(cap):
        out, cur = [[]], 0
        for g in groups:
            if out[-1] and cur + len(g) > cap:
                out.append([])
                cur = 0
            out[-1] += g
            cur += len(g)
        return out

    lo, hi = max((len(g) for g in groups), default=0), len(found)
    while lo < hi:
        mid = (lo + hi) // 2
        lo, hi = (lo, mid) if len(pack(mid)) <= 4 else (mid + 1, hi)
    batches = pack(lo) if found else []
    batches += [[] for _ in range(4 - len(batches))]
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for n, batch in enumerate(batches, 1):
        rng = random.Random(f"{run}-{n}")
        cells = rng.sample(clean, min(8, len(clean)))
        body = SKEPTIC.format(run=run, batch=n, seeded=Path(seeded).as_posix(), round=ROUND,
                              findings="\n\n".join(f["text"] for f in batch) or "None in this batch.",
                              cells="\n".join(f"- `{c[0]}` in {c[1]}" for c in cells),
                              cell_form="<clause> <build>" if run == "C" else "<item> <scenario>",
                              scratch=f"{Path(scratch).as_posix()}/skeptic-{run.lower()}{n}/")
        p = out / f"{TODAY}-build-PLAY-dClosedLoop-1-skeptic-brief-{run.lower()}{n}.md"
        p.write_text(body, encoding="utf-8", newline="\n")
        print(f"wrote {p.as_posix()}: findings {len(batch)}, clean cells {len(cells)}")
    return 0


def synth(run, returns_dir, verdicts_dir, report, subjects, out_dir):
    files = returns_of(run, returns_dir)
    verdicts = sorted(Path(verdicts_dir).glob(f"*-skeptic-return-{run.lower()}[1-4].md"))
    if len(verdicts) != 4:
        fail(f"{verdicts_dir} holds {len(verdicts)} skeptic returns for run {run}, where a run has four")
    line = Path(subjects).read_text(encoding="utf-8").strip()
    if not line.startswith("Subjects (round 1): "):
        fail("the subjects file holds no 'Subjects (round 1): ' line")
    body = (SYNTH_C if run == "C" else SYNTH).format(run=run, report=report, round=ROUND, subjects=line,
                        inputs="\n".join(f"- `{p.as_posix()}`" for p in files + verdicts))
    p = Path(out_dir) / f"{TODAY}-build-PLAY-dClosedLoop-1-synth-brief-{run.lower()}.md"
    p.write_text(body, encoding="utf-8", newline="\n")
    print(f"wrote {p.as_posix()}")
    return 0


def opt(args, flag):
    return args[args.index(flag) + 1] if flag in args else None


def main(argv):
    if not argv or argv[0] not in ("brief", "check", "skeptic", "synth", "recheck", "recheck-apply"):
        fail(__doc__.split("\n\n")[2], 2)
    run = opt(argv, "--run")
    if run not in ("A", "B", "C"):
        fail("--run is A, B or C")
    if argv[0] == "brief":
        walkers = [int(w) for w in opt(argv, "--walkers").split(",")] if opt(argv, "--walkers") else None
        if run == "C":
            return brief_c(opt(argv, "--seeded"), opt(argv, "--leads"), opt(argv, "--out"),
                           opt(argv, "--scratch") or "<the session's scratchpad>", opt(argv, "--key-sha"), walkers)
        return brief(run, opt(argv, "--seeded"), opt(argv, "--leads"), opt(argv, "--out"),
                     opt(argv, "--scratch") or "<the session's scratchpad>", opt(argv, "--key-sha"), walkers)
    if argv[0] == "recheck":
        return recheck(run, opt(argv, "--report"), opt(argv, "--returns"), opt(argv, "--seeded"), opt(argv, "--out"),
                       opt(argv, "--scratch") or "<the session's scratchpad>")
    if argv[0] == "recheck-apply":
        return recheck_apply(run, opt(argv, "--report"), opt(argv, "--verdicts"))
    if argv[0] == "skeptic":
        return skeptic(run, opt(argv, "--returns"), opt(argv, "--seeded"), opt(argv, "--out"),
                       opt(argv, "--scratch") or "<the session's scratchpad>")
    if argv[0] == "synth":
        return synth(run, opt(argv, "--returns"), opt(argv, "--verdicts"), opt(argv, "--report"),
                     opt(argv, "--subjects"), opt(argv, "--out"))
    plant = opt(argv, "--plant")
    if plant and plant not in PLANTS:
        fail(f"no plant {plant}")
    walker = opt(argv, "--walker")
    flags = ("--run", "--walker", "--report", "--plant", "--seeded")
    positional = [a for i, a in enumerate(argv[1:], 1) if a not in flags and argv[i - 1] not in flags]
    path = opt(argv, "--report") or (positional[-1] if positional else None)
    if not path:
        fail("check needs a return file, or --report <file>")
    if run == "C":
        if not opt(argv, "--seeded"):
            fail("run C's check reads the clauses from the sealed copy: pass --seeded <copy>")
        return check_c(int(walker) if walker else None, path, opt(argv, "--seeded"), plant)
    return check(run, int(walker) if walker else None, path, plant)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
