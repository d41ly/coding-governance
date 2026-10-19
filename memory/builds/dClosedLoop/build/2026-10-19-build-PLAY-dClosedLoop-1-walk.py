# **Serves:** research PLAY-dClosedLoop-1
"""The whole-design audit's walk: each walker's brief rendered from the round record, and each walk table checked
complete against its slice.

The round record, `2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, holds the scenarios (`[scenarios]`), the two
runs' slices (`[slicing]`), the table's grammar (`[walk-table]`) and the critical rubric (`[rubric]`). This script reads
them, so a brief and the check over its return share one source. The items are the design map's: the flow items by
step and the expansions' items, read through the atlas's derivation.

Usage (from the worktree root):
  python walk.py brief --run A|B --seeded <tree> --leads <file> --key-sha <hex> --out <dir> [--scratch <dir>]
      writes the run's five walker briefs into <dir>, each naming the sealed copy it reads, Stage 0's leads and the
      sealed key's SHA-256, which no brief renders without.
  python walk.py check --run A|B --walker <n> <return.md> [--plant <case>]
      one walker's return: every cell of its slice, every build and principle it owes, each in the grammar.
  python walk.py check --run A|B --report <report.md> [--plant <case>]
      a run's joined report: every cell of every slice, all 22 builds and all 42 principles.
  cases: drop-cell, bad-verdict, ghost-finding, no-reason, drop-build, drop-principle, extra-cell, dup-cell
  python walk.py skeptic --run A|B --returns <dir> --seeded <tree> --out <dir> [--scratch <dir>]
      the run's four skeptic briefs: the walkers' findings sorted by address and cut into four batches, never
      splitting one address, each batch with eight clean cells to attack, drawn the same way on every render.
  python walk.py synth --run A|B --returns <dir> --verdicts <dir> --report <path> --subjects <file> --out <dir>
      the run's synthesis brief, naming the report's path and its Subjects line.
Exit 1 on any finding, 2 on a slice or a record this script cannot read.

What it does not check: whether a verdict is right, which the skeptics test on a sample of clean cells; whether a
finding's address is the defect's, which the scorer reads; and the brief's prose, which is the template below.
"""
import importlib.util
import random
import re
import sys
from pathlib import Path

B = "memory/builds/dClosedLoop/build/"
ROUND = B + "2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md"
SCENARIOS = [f"S{i}" for i in range(1, 8)]
ROW = re.compile(r"^\| `?([a-z]+\.[a-z0-9-]+)`? \| (S[1-7]) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|\s*$")
ID = r"[AB](?:[1-5]|S[1-4])-F\d+"   # a walker's finding, or a new one a skeptic batch raises
FINDING = re.compile(r"^### (" + ID + r")\b", re.M)
VERDICT = re.compile(r"^(holds|" + ID + r"(?:, " + ID + r")*|not on path: \S.*)$")
VERDICT_ROW = re.compile(r"^\| `?((?:d[A-Z]\w+)|(?:P\d+))`? \| ([^|]+) \|\s*$")
PLANTS = ("drop-cell", "bad-verdict", "ghost-finding", "no-reason", "drop-build", "drop-principle", "extra-cell",
          "dup-cell")


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


TEMPLATE = """# Walk brief: run {run}, walker {walker}

**Serves:** research PLAY-dClosedLoop-1

You are one of five walkers in run {run} of the whole-design audit of dClosedLoop's design
(`{seeded}/{round}`, whose `[scenarios]`, `[walk-table]` and `[rubric]` you follow). Walk the design as the slice below says,
item by item, and report every defect you can show. A second run walks the same design sliced the other way; you
will not see its findings, and it will not see yours.

## Where you read

- **Every design record from the sealed copy only:** `{seeded}/memory/builds/dClosedLoop/build/`. The copy is the
  design under audit. Never read the design records in the working tree, never diff the copy against it, and never read
  git history for them: the copy differs on purpose, and a finding cited from anywhere else is not scored.
- **Code** under `tools/`, `skills/` and `.githooks/` from the working tree, to test a claim the design makes about
  today.
- **The design map at level 0:** `{seeded}/design-map.txt`, as your index.
- **Stage 0's leads for your slice:** `{leads}`, the mechanical checks' reds and what they do not read.

Known defects were planted in the copy before you started, and a sealed key lists them; its SHA-256, fixed before
launch, is `{key_sha}`. Look for every defect the same way: a planted one is scored like any other finding.

Read `flow-steps` whole, then v2 (`architecture-v2`): the `[chain]` rows of your builds, the `[policies]` keys your
items read, and `[principles]` and `[enforcement]` for your principles. {extra}

## Your slice

- **Scenarios:** {scenarios}
- **Steps:** {steps}
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

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `{scratch}` only. Your effort is the owner's medium.
"""
EXTRA = {"S2": "For S2 read `layer-runtime`, `cloud-and-scale` and `stall-and-loop` too.",
         "S4": "For S4 read `adopter-instructions`, `flow-roles-adoption`, `fates` and `layer-expansions` too."}


def brief(run, seeded, leads, out_dir, scratch, key_sha):
    if not key_sha or not re.fullmatch(r"[0-9a-f]{64}", key_sha):
        fail("--key-sha takes the sealed key's SHA-256, 64 hex digits, pinned before any brief is rendered")
    text, scen, slices = load()
    by_step, _, _ = derive_items()
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for (r, w), sl in sorted(slices.items()):
        if r != run:
            continue
        steps = list(by_step) if sl["steps"] == ["all"] else sl["steps"]
        extra = " ".join(EXTRA[s] for s in sl["scenarios"] if s in EXTRA)
        scenario_text = "\n".join(f"- **{s}, {scen[s][1]}:** {scen[s][2]} Injected or probed: {scen[s][3]}"
                                  for s in sl["scenarios"])
        body = TEMPLATE.format(run=run, walker=w, round=ROUND, seeded=Path(seeded).as_posix(), leads=leads, key_sha=key_sha,
                               extra=extra, scenarios=", ".join(sl["scenarios"]),
                               steps=", ".join(f"{s} ({len(by_step[s])} items)" for s in steps),
                               builds=", ".join(sl["builds"]), principles=", ".join(sl["principles"]),
                               scenario_text=scenario_text, scratch=f"{Path(scratch).as_posix()}/walk-{run.lower()}{w}/")
        p = out / f"2026-10-19-build-PLAY-dClosedLoop-1-walk-brief-{run.lower()}{w}.md"
        p.write_text(body, encoding="utf-8", newline="\n")
        print(f"wrote {p.as_posix()}: cells {len(cells_of(sl, by_step))}")
    return 0


SKEPTIC = """# Skeptic brief: run {run}, batch {batch}

**Serves:** research PLAY-dClosedLoop-1

You are one of four skeptics in run {run} of the whole-design audit (`{seeded}/{round}`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`{seeded}/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

Read the design only from the sealed copy, never from the working tree, and never diff the two; read code under
`tools/` from the working tree.

## Findings to refute

{findings}

## Clean cells to attack

{cells}

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `{run}S{batch}-F<n>`.

Write nothing to the repository; any probe you run writes under `{scratch}` only. Your effort is the owner's medium.
"""
SYNTH = """# Synthesis brief: run {run}

**Serves:** research PLAY-dClosedLoop-1

Merge run {run} of the whole-design audit into one report, written to `{report}`. Read the round record's
`[walk-table]` and `[rubric]` (`{round}`), the five walker returns and the four skeptics' verdicts:

{inputs}

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
   blocker=<n> high=<n> medium=<n> low=<n> agents=11 out-tokens=0`, on one line; the main loop fills `out-tokens` from
   the runs' returned lines.

`walk.py check --run {run} --report` must pass on it: every cell, every build and principle, and every id a verdict
names carried by a heading. Return the report's path and the critical findings' ids. Your effort is the owner's medium.
"""


def findings_of(text):
    out = []
    for m in re.finditer(r"^### (" + ID + r")\b[^\n]*\n(.*?)(?=^### |^\| Item |^## |\Z)", text, flags=re.M | re.S):
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
                              scratch=f"{Path(scratch).as_posix()}/skeptic-{run.lower()}{n}/")
        p = out / f"2026-10-19-build-PLAY-dClosedLoop-1-skeptic-brief-{run.lower()}{n}.md"
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
    body = SYNTH.format(run=run, report=report, round=ROUND, subjects=line,
                        inputs="\n".join(f"- `{p.as_posix()}`" for p in files + verdicts))
    p = Path(out_dir) / f"2026-10-19-build-PLAY-dClosedLoop-1-synth-brief-{run.lower()}.md"
    p.write_text(body, encoding="utf-8", newline="\n")
    print(f"wrote {p.as_posix()}")
    return 0


def opt(args, flag):
    return args[args.index(flag) + 1] if flag in args else None


def main(argv):
    if not argv or argv[0] not in ("brief", "check", "skeptic", "synth"):
        fail(__doc__.split("\n\n")[2], 2)
    run = opt(argv, "--run")
    if run not in ("A", "B"):
        fail("--run is A or B")
    if argv[0] == "brief":
        return brief(run, opt(argv, "--seeded"), opt(argv, "--leads"), opt(argv, "--out"),
                     opt(argv, "--scratch") or "<the session's scratchpad>", opt(argv, "--key-sha"))
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
    flags = ("--run", "--walker", "--report", "--plant")
    positional = [a for i, a in enumerate(argv[1:], 1) if a not in flags and argv[i - 1] not in flags]
    path = opt(argv, "--report") or (positional[-1] if positional else None)
    if not path:
        fail("check needs a return file, or --report <file>")
    return check(run, int(walker) if walker else None, path, plant)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
