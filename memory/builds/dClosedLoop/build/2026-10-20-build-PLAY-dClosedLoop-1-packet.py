# **Serves:** research PLAY-dClosedLoop-1
"""The packet instrument: one generated packet per chain build, the oriented handoff a session on any node reads
before it specs or builds that build (the execution plan's P0.3 and `[handoffs]`, built from the handoffs return's
probe, IR:197-283). A packet is written as `memory/builds/<slug>/prompts/<date>-prompt-<first unit>-packet.md`. It
carries `## The prompt` and `## The brief`, so `tools/roles/handoff.py render --build <slug> --unit <id> --input
prompt=<packet>` reads its `brief:*`: Goal, Items, Acceptance, Gates and Non-goals, then one sub-head per field.

Its twelve fields, derived and never typed:
  1  Pins: the baseline sha, `deviations.BASELINE` (P0.1 row 5) and never v2's `Baseline:` line, which
     `deviations.py` checks against it; the blobs at HEAD of v2 and of the as-built view; each instrument's pinned blob
     (`carries.py`, `deviations.py`, `asbuilt.py`, this file, the schedule script, the opening script and
     `bare-ids.py`, whose `read_roster` reads field 9's roster, those tracked at the first render); the HEAD it was
     rendered at; and the generator's version, this file's blob at HEAD.
  2  Items: each clause of the row, its id at its baseline hash, its hash now in the as-built view with the record
     behind any change, its tokens as `carries.py`'s token arm reads them (a clause that arm cannot see is flagged),
     and its text.
  3  Owned nodes, from `carries.py`'s `design()`.
  4  Parents: each one's state as the schedule script's `tree_state` reads HEAD, and each parent clause this build's
     clauses name, by a backticked name the two carry.
  5  Children: the chain builds whose Parents cell names this one.
  6  Gaps: each key of the row's Gaps cell, ranges expanded, with its severity, register line and text.
  7  Policy keys: the keys v2's `[policies]` gives this build, and the keys its clauses name that a later build (not
     an ancestor) owns.
  8  Later builds named: every mention of a non-ancestor chain build in a clause, verbatim, flagged when the clause
     matches the probe's stand-in pattern.
  9  Obligations: v2's `[owed]`, `[open]`, `[enforcement]` and `[policies]` lines naming the build; every unit of the
     opened README's `roster:units` pair as `bare-ids.py`'s `read_roster` reads it, `**Derived:**` ones included;
     for a build the schedule script's `EXTRA`
     names, its units beyond v2's row and the decision row they derive from (P0.8 row 1, written `missing:` until
     `memory/DECISIONS.md` holds it); and every open ask in dClosedLoop's `BACKLOG.md` naming a chain build, from the
     index generator's `--asks` (an absent file reads as none, never as an error). A unit or ask line opens with the
     word "id", since a list item led by an id defines it, and hygiene check 13 reds an id two build folders claim.
  10 Non-goals: what the build must not touch.
  11 Coverage: `carries.py --report <slug>`'s output.
  12 Reading order: the cold session's seven steps.

Usage (from the worktree root):
  python packet.py --write <slug> [--unit <first unit>]
      re-render the build's packet, keeping the instrument pins it carries; with none yet, render the first one,
      pinning every tracked instrument at HEAD, named for the opened README roster's first unit or else --unit
  python packet.py --check <slug>
      render it again and compare the bytes; the completeness arms (every clause id and hash of the row, every gap
      it owns, every parent, every `[owed]` line naming it, every roster unit, every open ask); and the pin arm,
      separate from the byte compare: each pinned instrument's blob against `git rev-parse HEAD:<path>`
  python packet.py --repin <instrument>
      the owner's re-pin: that instrument's pin set to its blob at HEAD in every chain build's packet, each re-rendered
  python packet.py --fixture [--build <slug>] [--plant <case>] [--control no-pin-arm|repin]
      the checks over a packet rendered in memory from the tree (default dTrueNorth), every arm's population seeded
      where the tree holds none, damaged one way: clause, gap, parent, owed, roster or ask (that item dropped from
      the renderer's input while the arms read the sources whole); hand-edit; pin (carries.py's blob moved by a
      one-byte edit, the packet made stale by a new `[owed]` line and re-rendered keeping its pins; the controls
      drop the pin arm, or re-pin on write); run-live and run-landed (a chain build's `RUN.md` at a live and at a
      terminal phase, read by the guard --repin and a first render share)
A first render and --repin refuse inside a chain run: a chain build's `RUN.md` whose phase is not terminal.
`render_packet(slug, first_unit=None)` returns the path and the text --write would write; the opening imports it.
Exit 0 green, 1 on a finding or a refusal, 2 when there is nothing to check.

What it does not check: whether a spec builds what a clause means, which the carries join and the semantic lens
read; a source-reading defect the renderer and the arms share, since both read the same tree; an instrument edited
and not committed, since the pin arm reads HEAD; whether v2's `Baseline:` line agrees with the pin, which
`deviations.py` lists as a member and `asbuilt.py --check` reports; and a hand edit of a pin line or of this file,
which only the owner's landing-diff check guards until a chain unit's merge-bar check (the execution plan's
`[cannot]`).
"""
import argparse
import copy
import datetime
import functools
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

B = "memory/builds/dClosedLoop/build/"
SELF = B + "2026-10-20-build-PLAY-dClosedLoop-1-packet.py"
INSTRUMENTS = (B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py",
               B + "2026-10-19-build-PLAY-dClosedLoop-1-deviations.py",
               B + "2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py", SELF,
               B + "2026-10-20-build-PLAY-dClosedLoop-1-schedule.py", B + "2026-10-20-build-PLAY-dClosedLoop-1-open.py",
               B + "2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py")
GR = B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"
DECISIONS = "memory/DECISIONS.md"
# P0.8 row 1's id, fixed for Phase 0 (dispatch 236's brief): the decision an EXTRA unit derives from. Written
# `missing:` here so the build-index generator joins nothing; a packet prints it bare once DECISIONS.md holds the row.
EXTRA_DECISION = "missing:PLAY-dClosedLoop-2"
TERMINAL = ("LANDED", "ABORTED")      # the run-state phases UNATTENDED-PROTOCOL §3 calls terminal
SECTIONS = ("owed", "open", "enforcement", "policies")
ROW = re.compile(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$")
STANDIN = r"stand(s|ing)?[- ]in|until {o}|before {o}|{o}'s [\w-]+ (lands|land)"     # the probe's pattern
PIN = re.compile(r"^- instrument: `([^`]+)` blob `([0-9a-f]{40,64})`$", re.M)
AT = re.compile(r"^- rendered at: `([0-9a-f]{40,64})`$", re.M)
PLANTS = ("clause", "gap", "parent", "owed", "roster", "ask", "hand-edit", "pin", "run-live", "run-landed")
CONTROLS = ("no-pin-arm", "repin")
UTF8 = dict(os.environ, PYTHONIOENCODING="utf-8")


class Refusal(Exception):
    """A refusal: exit 1, nothing written."""


class Unmeasured(Exception):
    """Nothing to check: exit 2."""


def load_instrument(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


carries = load_instrument("carries", INSTRUMENTS[0])
asbuilt = load_instrument("asbuilt", INSTRUMENTS[2])
deviations = asbuilt.deviations     # the module asbuilt.py loads: BASELINE, the pin the view and the packet render from
bareids = deviations.bareids        # the module deviations.py loads: `read_roster`, the roster:units pair's one reader
schedule = load_instrument("schedule", INSTRUMENTS[4])
handoff = load_instrument("handoff", "tools/roles/handoff.py")             # the reader `render` takes brief:* with
genindex = load_instrument("gen_build_index", "tools/memory-tree/gen_build_index.py")   # the conf and roster id grammar


def run_git(*args):
    done = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    if done.returncode:
        raise Refusal(f"git {' '.join(args)} failed: {done.stderr.strip()[:200]}")
    return done.stdout


def read_head_blob(path):
    done = subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"HEAD:{path}"], capture_output=True, text=True,
                          encoding="utf-8")
    return done.stdout.strip() if done.returncode == 0 else None


def derive_blob(data):
    """The git blob id of some bytes, as `git hash-object` gives it."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def read_file(path):
    return Path(path).read_text(encoding="utf-8") if Path(path).is_file() else None


def read_chain(v2):
    """{build: {stage, parents, gaps}} from v2's `[chain]` rows, the parents and gaps cells as written."""
    body = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    rows = {}
    for ln in body.split("\n"):
        m = ROW.match(ln)
        if m:
            rows[m.group(1)] = {"stage": m.group(2).strip(), "gaps": m.group(5).strip(),
                                "parents": [p.strip() for p in m.group(3).split(",") if p.strip()]}
    return rows


def read_section_lines(v2, tag):
    """[(line number, line)] of v2's `## [<tag>]` section."""
    lines = v2.split("\n")
    start = next((i for i, ln in enumerate(lines) if ln.startswith(f"## [{tag}]")), None)
    out = []
    for i in range(start + 1 if start is not None else len(lines), len(lines)):
        if lines[i].startswith("## "):
            break
        out.append((i + 1, lines[i]))
    return out


def extract_gaps(cell):
    """(keys, unparsed parts) of a Gaps cell, `gap-x-04 to gap-x-10` expanded (the probe's rule)."""
    keys, bad = [], []
    for part in [p.strip() for p in cell.split(",") if p.strip()]:
        m = re.fullmatch(r"(gap-[a-z]+-)(\d+) to (gap-[a-z]+-)(\d+)", part)
        if m and m.group(1) == m.group(3):
            keys += [f"{m.group(1)}{n:0{len(m.group(2))}d}" for n in range(int(m.group(2)), int(m.group(4)) + 1)]
        elif re.fullmatch(r"gap-[a-z]+-\d+", part):
            keys.append(part)
        else:
            bad.append(part)
    return keys, bad


def read_register():
    """{key: (line number, severity, gap)} from the gap register's rows."""
    out = {}
    for n, ln in enumerate(Path(GR).read_text(encoding="utf-8").split("\n"), 1):
        m = re.match(r"^\| (gap-[a-z]+-\d+) \| [^|]* \| ([^|]*) \| ([^|]*) \|", ln)
        if m:
            out[m.group(1)] = (n, m.group(2).strip(), m.group(3).strip())
    return out


def read_policy_owners(v2):
    """{key: owner} from v2's `[policies]` table, in its order."""
    out = {}
    for _, ln in read_section_lines(v2, "policies"):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if ln.startswith("| `") and len(cells) >= 5:
            out[cells[0].strip("`")] = cells[-1]
    return out


def derive_ancestors(slug, rows):
    seen, stack = set(), [p for p in rows[slug]["parents"] if p in rows]
    while stack:
        p = stack.pop()
        if p not in seen:
            seen.add(p)
            stack += [q for q in rows[p]["parents"] if q in rows]
    return seen


def read_roster(text, slug):
    """[(unit id, line number, row)] of the README's authored `roster:units` pair, in its order, the units of `slug`
    alone: `bareids.read_roster` over the tree's declared families. The opening imports this."""
    families = {p.split(":")[1] for p in genindex.load_conf(".")["FAMILIES"].split() if ":" in p}
    return bareids.read_roster(text, genindex.build_roster_id_re(families), slug)


@functools.lru_cache(maxsize=None)
def read_asks(chain):
    """The open asks dClosedLoop's BACKLOG.md files that name a chain build, from the index generator's `--asks`."""
    done = subprocess.run([sys.executable, "tools/memory-tree/gen_build_index.py", "--asks", "--build", "dClosedLoop",
                           "--json"], capture_output=True, text=True, encoding="utf-8", env=UTF8)
    if done.returncode:
        raise Refusal(f"gen_build_index.py --asks exited {done.returncode}, so the open asks cannot be read: "
                      f"{(done.stderr.strip().split(chr(10)) or [''])[-1][:200]}")
    out = []
    for a in json.loads(done.stdout)["asks"]:
        line = Path(a["file"]).read_text(encoding="utf-8").split("\n")[a["line"] - 1].strip()
        if any(re.search(r"\b" + b + r"\b", line) for b in chain):
            out.append({"id": a["id"], "status": a["status"], "where": f"{a['file']}:{a['line']}", "line": line})
    return tuple(out)


def derive_decision_id(marked):
    """The id bare once `memory/DECISIONS.md` holds its row, else in its `missing:` form."""
    bare = marked.split(":", 1)[1]
    return bare if re.search(r"^- " + re.escape(bare) + " · ", read_file(DECISIONS) or "", re.M) else marked


@functools.lru_cache(maxsize=None)
def read_tree():
    """The tree-wide reads every packet shares, read once."""
    builds, nodes, _retired = carries.design()
    v2 = Path(carries.V2).read_text(encoding="utf-8")
    rows = read_chain(v2)
    if list(rows) != list(builds):
        raise Refusal("v2's [chain] rows and carries.py's design() name different chain builds")
    sha = deviations.BASELINE
    base ={cid: h for _b, cid, _t, h in asbuilt.baseline_clauses(run_git("show", f"{sha}:{carries.V2}"))}
    view = {}
    for ln in (read_file(asbuilt.OUT) or "").split("\n"):
        r = asbuilt.ROW.match(ln)
        if r:
            view[r.group(2)] = (r.group(3), r.group(5))
    return {"builds": builds, "nodes": nodes, "rows": rows, "baseline": sha, "base": base, "view": view,
            "register": read_register(), "owners": read_policy_owners(v2),
            "lines": {tag: read_section_lines(v2, tag) for tag in SECTIONS},
            "v2_blob": read_head_blob(carries.V2), "view_blob": read_head_blob(asbuilt.OUT),
            "version": read_head_blob(SELF)}


def extract_excerpt(text, start, end):
    """A mention with up to 90 characters before and 60 after, cut at spaces."""
    a, b = max(0, start - 90), min(len(text), end + 60)
    if a:
        a = text.find(" ", a, start) + 1 or a
    if b < len(text):
        k = text.rfind(" ", end, b)
        b = k if k > end else b
    return ("…" if a else "") + text[a:b] + ("…" if b < len(text) else "")


def derive_sources(slug):
    """Everything one build's packet carries, from the tree."""
    t = read_tree()
    builds, rows = t["builds"], t["rows"]
    if slug not in rows:
        raise Unmeasured(f"{slug} is no build of v2's [chain]")
    chain = list(rows)
    anc = derive_ancestors(slug, rows)
    clauses = []
    for cid, (text, h, tokens) in builds[slug].items():
        vtext, rid = t["view"].get(cid, (None, None))
        clauses.append({"id": cid, "pin": t["base"].get(cid, h), "base": t["base"].get(cid), "row": h,
                        "now": carries.clause_hash(vtext) if vtext is not None else h, "record": rid,
                        "in_view": vtext is not None, "text": text if vtext is None else vtext, "tokens": tokens})
    mine = {tok for c in clauses for tok in c["tokens"]}
    states = schedule.tree_state("HEAD", {p: list(builds[p]) for p in rows[slug]["parents"] if p in builds})
    parents = []
    for p in rows[slug]["parents"]:
        named = [(y, h, sorted(set(toks) & mine)) for y, (_t, h, toks) in builds[p].items() if set(toks) & mine] \
            if p in builds else []
        parents.append({"name": p, "state": states.get(p), "named": named})
    keys, bad = extract_gaps(rows[slug]["gaps"])
    mentions = []
    for c in clauses:
        for o in chain:
            if o != slug and o not in anc:
                standin = bool(re.search(STANDIN.format(o=o), c["text"]))
                mentions += [(c["id"], o, standin, extract_excerpt(c["text"], m.start(), m.end()))
                             for m in re.finditer(r"\b" + o + r"\b", c["text"])]
    readme = read_file(f"memory/builds/{slug}/README.md")
    report = subprocess.run([sys.executable, INSTRUMENTS[0], "--report", slug], capture_output=True, text=True,
                            encoding="utf-8", env=UTF8)
    if report.returncode:
        raise Refusal(f"carries.py --report {slug} exited {report.returncode}: {report.stderr.strip()[:200]}")
    return {"slug": slug, "stage": rows[slug]["stage"], "chain": chain, "clauses": clauses,
            "nodes": sorted(t["nodes"][slug]), "parents": parents,
            "children": [b for b in chain if slug in rows[b]["parents"]],
            "gaps": [(k, t["register"].get(k)) for k in keys], "gaps_unparsed": bad,
            "owns": [k for k, o in t["owners"].items() if o == slug],
            "reads": [(k, o) for k, o in t["owners"].items() if k in mine and o in rows and o != slug and o not in anc],
            "mentions": mentions,
            "lines": [(tag, n, ln) for tag in SECTIONS for n, ln in t["lines"][tag]
                      if re.search(r"\b" + slug + r"\b", ln)],
            "roster": None if readme is None else read_roster(readme, slug),
            "extra": schedule.EXTRA.get(slug, 0), "decision": derive_decision_id(EXTRA_DECISION),
            "asks": [dict(a) for a in read_asks(tuple(chain))], "coverage": report.stdout.strip(),
            "others": sum(len(builds[b]) for b in chain if b != slug), "baseline": t["baseline"],
            "v2_blob": t["v2_blob"], "view_blob": t["view_blob"], "version": t["version"]}


def render_text(src, pins, at):
    """The packet's bytes, from its sources, the instrument pins it keeps and the HEAD it was rendered at."""
    s, stage = src["slug"], src["stage"]
    ticks = lambda xs: ", ".join(f"`{x}`" for x in xs)   # noqa: E731
    out = [f"# Packet — {s}: the {stage} build of the dClosedLoop chain", "",
           "**Serves:** research PLAY-dClosedLoop-1", "",
           f"Generated by `{SELF}`, never typed (the execution plan's P0.3 and `[handoffs]`). `packet.py --check {s}` "
           "renders it again and compares the bytes, reads it for every clause, gap, parent, `[owed]` line, roster "
           "unit and open ask it must carry, and compares each instrument pin with that instrument's blob at HEAD. "
           "Only `packet.py --repin <instrument>`, the owner's, moves a pin.", "",
           "## The prompt", "",
           f"Spec and build {s}, the {stage} build of the dClosedLoop chain, from its row of v2's `[chain]` at the "
           "baseline in Pins, under its README's build-level rules. Read this packet in the order Reading order gives.",
           "", "## The brief", "", "### Goal", "",
           f"Every unit of {s} specced and built, so that each of the {len(src['clauses'])} clauses of its row in v2's "
           f"`[chain]` (Items) is carried by a spec pinned to its hash and built, each of its {len(src['nodes'])} "
           f"owned nodes (Owned nodes) is built, and each of its {len(src['gaps'])} owned gaps (Gaps) is closed"
           + (f", with its {src['extra']} unit beyond the row (Obligations)." if src["extra"] else "."), "",
           "### Items", "",
           "Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with "
           "the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.", ""]
    for i, c in enumerate(src["clauses"], 1):
        now = f"now `{c['now']}`" + (", absent from the as-built view" if not c["in_view"] else
                                      f" by deviation `{c['record']}`" if c["record"] else
                                      ", as at the baseline" if c["now"] == c["pin"] else "")
        now += ", added since the baseline" if c["base"] is None else (
            f"; v2's text now hashes `{c['row']}`, a departure from the frozen design" if c["row"] != c["base"] else "")
        toks = ticks(c["tokens"]) or "none, so the token arm cannot see this clause"
        out.append(f"{i}. `{c['id']}@{c['pin']}` · {now} · tokens: {toks} — {c['text']}")
    standins = sorted({o for _c, o, si, _e in src["mentions"] if si}, key=src["chain"].index)
    out += ["", "### Acceptance", "",
            f"- At the Design exit, `carries.py --build {s} --exit` exits 0 over the build's specs: each clause in "
            "Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's "
            "tokens in its carriers.",
            "- Each clause's own seen-red cases, stated in its text, observed as it states them.",
            "- Every departure from a clause, or from a spec after its first pass, is a deviation record that "
            "`deviations.py` joins, and the build's departures report lists it (README rule 4).", "",
            "### Gates", "",
            f"- `packet.py --check {s}` green before the first pass. A red on a moved instrument blob is a stop, never "
            "re-rendered away (README rule 2).",
            f"- `carries.py --build {s} --exit` at the Design exit while it is in service (the execution plan's "
            "`[phase-1]` retirement table).",
            "- The close sequence of README rule 4, then the bar the driver owes at `--close`.", "",
            "### Non-goals", "",
            f"- v2, `{carries.V2}`: frozen at the baseline, so a change to a clause is a deviation record approved by "
            "its risk.",
            f"- The {src['others']} clauses of the other {len(src['chain']) - 1} chain builds' rows: carrying one "
            f"needs a `**Moved:** <clause id> to {s} by <decision>` line.",
            f"- Any path outside `memory/builds/{s}/`, but the product paths a build run's units record with "
            "`--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing "
            "re-renders (README rule 7).",
            f"- Another build's packet, the instruments under `{B}*.py`, and this packet's pin lines: only "
            "`packet.py --repin <instrument>`, the owner's, moves a pin."]
    if standins:
        out.append(f"- The surfaces of {', '.join(standins)}, which this build's clauses use as stand-ins only "
                   "(Later builds named).")
    order = {p: i for i, p in enumerate(INSTRUMENTS)}
    out += ["", "### Pins", "", f"- baseline: `{src['baseline']}`, the pin `deviations.py` carries (P0.1 row 5)",
            f"- v2: `{carries.V2}` " + (f"blob `{src['v2_blob']}`" if src["v2_blob"] else "absent at HEAD"),
            f"- as-built view: `{asbuilt.OUT}` "
            + (f"blob `{src['view_blob']}`" if src["view_blob"] else "absent at HEAD")]
    out += [f"- instrument: `{p}` blob `{pins[p]}`" for p in sorted(pins, key=lambda p: (order.get(p, len(order)), p))]
    out += [f"- rendered at: `{at}`", f"- generator: `{SELF}` " + (f"version `{src['version']}`, its blob at HEAD"
                                                                    if src["version"] else "untracked at HEAD"), "",
            "### Owned nodes", ""] + ([f"- `{n}`" for n in src["nodes"]] or ["- none"]) + ["", "### Parents", ""]
    for p in src["parents"]:
        if p["state"] is None:
            out.append(f"- {p['name']}: no chain build, so the schedule script derives no state for it, and it has no "
                       "clause in v2's `[chain]`")
            continue
        named = "; ".join(f"`{y}@{h}` ({ticks(toks)})" for y, h, toks in p["named"]) or "none"
        out.append(f"- {p['name']}: specs done {'yes' if p['state'][0] else 'no'}, build done "
                   f"{'yes' if p['state'][1] else 'no'}, as the schedule script's `tree_state` reads HEAD. Its clauses "
                   f"this build's clauses name, by a backticked name both carry: {named}")
    out += ["", "### Children", ""] + ([f"- {c}" for c in src["children"]] or ["- none"]) + ["", "### Gaps", ""]
    out += [f"- `{k}` · {reg[1]} · `{GR}:{reg[0]}` · {reg[2]}" if reg else f"- `{k}` · not in the gap register"
            for k, reg in src["gaps"]] or ["- none"]
    out += [f"- unparsed in the row's Gaps cell: {part}" for part in src["gaps_unparsed"]]
    out += ["", "### Policy keys", "", "- owns: " + (ticks(src["owns"]) or "none"),
            "- reads, owned by a later build: " + (", ".join(f"`{k}` ({o})" for k, o in src["reads"]) or "none"),
            "", "### Later builds named", ""]
    out += [f"- `{cid}` names {o}" + (", a stand-in" if si else "") + f': "{ex}"'
            for cid, o, si, ex in src["mentions"]] or ["- none"]
    out += ["", "### Obligations", "",
            f"v2's `[owed]`, `[open]`, `[enforcement]` and `[policies]` lines naming {s}:", ""]
    out += [f"- v2:{n} `[{tag}]` {ln.strip()}" for tag, n, ln in src["lines"]] or ["- none"]
    out += ["", "The opened README's roster, every unit with its row:", ""]
    if src["roster"] is None:
        out.append(f"- no opened README: `memory/builds/{s}/README.md` does not exist")
    else:
        out += [f"- unit id `{u}` · README:{n} {row}" for u, n, row in src["roster"]] or \
            ["- none: the opened README's `roster:units` pair names no unit"]
    if src["extra"]:
        out += ["", f"- {src['extra']} unit beyond v2's row, the schedule script's `EXTRA`, `**Derived:**` from "
                    f"`{src['decision']}`: the execution plan's P0.8 row 1, which approves it as a departure from v2. "
                    "The opening mints its id."]
    out += ["", "Open asks in dClosedLoop's `BACKLOG.md` naming a chain build:", ""]
    out += [f"- ask id `{a['id']}` · {a['status']} · `{a['where']}` · {a['line']}" for a in src["asks"]] or \
        ["- none: `memory/builds/dClosedLoop/BACKLOG.md` files no open ask naming one"]
    out += ["", "### Coverage", "", f"`carries.py --report {s}`:", "", src["coverage"], "", "### Reading order", "",
            f"1. Under a mandate, `bash tools/unattended/unattended.sh --status {s}`; otherwise "
            "`git log --oneline -5`.",
            f"2. `memory/builds/{s}/RUN.md` whole, when it exists.",
            "3. The README: its roster mapped to clause ids, its build-level rules, `parents:`, `may:` and "
            "`spec-audit:`.",
            f"4. This packet, with `packet.py --check {s}` green.",
            "5. `memory/guides/BUILD-METHOD.md` whole.",
            "6. The current spec whole.",
            "7. The recall probe, with the terms in that spec's §10."]
    return "\n".join(out) + "\n"


def read_pins(text):
    """({instrument: blob}, rendered-at sha) from a packet's Pins section."""
    sec = handoff.extract_brief_section(text, "pins") or ""
    m = AT.search(sec)
    return dict(PIN.findall(sec)), m.group(1) if m else None


def check_complete(text, src):
    """The completeness arms: each item the sources hold, looked for in its own section of the packet."""
    sec = {h: handoff.extract_brief_section(text, h) or "" for h in ("items", "gaps", "parents", "obligations")}
    s = src["slug"]
    out = [f"clause arm: `{c['id']}@{c['pin']}` of {s}'s row is not in Items" for c in src["clauses"]
           if f"`{c['id']}@{c['pin']}`" not in sec["items"]]
    out += [f"gap arm: `{k}`, which {s} owns, is not in Gaps" for k, _ in src["gaps"] if f"`{k}`" not in sec["gaps"]]
    out += [f"parent arm: {p['name']} is not in Parents" for p in src["parents"]
            if not re.search(r"^- " + re.escape(p["name"]) + ":", sec["parents"], re.M)]
    out += [f"owed arm: v2:{n} `[owed]`, naming {s}, is not in Obligations" for tag, n, ln in src["lines"]
            if tag == "owed" and f"- v2:{n} `[owed]` {ln.strip()}" not in sec["obligations"]]
    out += [f"roster arm: `{u}` of the opened README is not in Obligations" for u, _n, _r in src["roster"] or []
            if f"`{u}`" not in sec["obligations"]]
    out += [f"ask arm: `{a['id']}` ({a['where']}) is not in Obligations" for a in src["asks"]
            if f"`{a['id']}`" not in sec["obligations"]]
    return out


def check_pins(pins, blob_of):
    """The pin arm: each pinned instrument against its blob now, whatever the byte compare says."""
    if not pins:
        return ["pin arm: the packet pins no instrument, so the arm would read nothing"]
    return [f"pin arm: instrument {p} moved: pinned {b[:12]}, HEAD holds {(now or 'nothing')[:12]}"
            for p, b in pins.items() if (now := blob_of(p)) != b]


def check_text(text, rerendered, src, blob_of, pin_arm=True):
    """(findings, summary): the byte compare, the completeness arms and the pin arm over one packet."""
    findings = []
    if text != rerendered:
        a, b = text.split("\n"), rerendered.split("\n")
        n = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        findings.append(f"byte compare: the packet differs from its render from line {n + 1}: "
                        f"{a[n][:90] if n < len(a) else 'EOF'}")
    arms = check_complete(text, src)
    pins, _at = read_pins(text)
    moved = check_pins(pins, blob_of) if pin_arm else []
    roster = "none (no README)" if src["roster"] is None else len(src["roster"])
    summary = (f"byte compare {'green' if text == rerendered else 'red'} · completeness {len(arms)} findings over "
               f"clauses {len(src['clauses'])}, gaps {len(src['gaps'])}, parents {len(src['parents'])}, owed "
               f"{sum(1 for x in src['lines'] if x[0] == 'owed')}, roster {roster}, asks {len(src['asks'])} · "
               + (f"pin arm {len(pins)} instruments, {len(moved)} findings" if pin_arm else "pin arm removed"))
    return findings + arms + moved, summary


def scan_live_run(chain, read):
    """Each chain build's RUN.md whose phase is not terminal: a chain run in this tree."""
    live = []
    for b in chain:
        text = read(f"memory/builds/{b}/RUN.md")
        if text is not None:
            phases = re.findall(r"^phase: (\S+)", text, re.M)
            if not phases or phases[-1] not in TERMINAL:
                live.append(f"memory/builds/{b}/RUN.md (phase {phases[-1] if phases else 'unreadable'})")
    return live


def scan_packets(slug):
    return sorted(Path(f"memory/builds/{slug}/prompts").glob("*-prompt-*-packet.md"))


def resolve_instrument(name):
    hits = [p for p in INSTRUMENTS if name in (p, Path(p).name) or p.endswith("-" + name)]
    if len(hits) != 1:
        raise Refusal(f"--repin {name} names {len(hits)} of the instruments: {', '.join(INSTRUMENTS)}")
    return hits[0]


def render_packet(slug, first_unit=None):
    """(path, text) of the build's packet as --write would write it: the existing packet re-rendered keeping its
    instrument pins, or the first one, pinning every instrument tracked at HEAD. The opening imports this."""
    src = derive_sources(slug)
    found = scan_packets(slug)
    head = run_git("rev-parse", "HEAD").strip()
    if len(found) > 1:
        raise Refusal(f"{slug} has {len(found)} packets ({', '.join(p.name for p in found)}), and a build has one")
    if found:
        old = found[0].read_bytes().decode("utf-8")
        pins, at = read_pins(old)
        if not pins:
            raise Refusal(f"{found[0].as_posix()} carries no instrument pin, and only a first render or --repin pins")
        kept = render_text(src, pins, at or head)
        return found[0].as_posix(), old if kept == old else render_text(src, pins, head)
    live = scan_live_run(src["chain"], read_file)
    if live:
        raise Refusal("a first render pins every instrument, and a chain run never pins: " + "; ".join(live))
    units = [u for u, _n, _r in src["roster"] or []]
    if units and first_unit and first_unit != units[0]:
        raise Refusal(f"--unit {first_unit} is not {units[0]}, the opened README roster's first unit")
    unit = units[0] if units else first_unit
    if not unit or not re.fullmatch(r"[A-Z]+-" + slug + r"-\d+", unit):
        raise Refusal(f"no first unit of {slug}: no opened README roster names one, and --unit gave "
                      f"'{first_unit or ''}', not <FAMILY>-{slug}-<n>")
    pins = {p: b for p in INSTRUMENTS if (b := read_head_blob(p))}
    return (f"memory/builds/{slug}/prompts/{datetime.date.today().isoformat()}-prompt-{unit}-packet.md",
            render_text(src, pins, head))


def write_packet(path, text):
    folder = Path(path).parent
    if not folder.parent.is_dir():
        raise Refusal(f"{folder.parent.as_posix()} does not exist: the opening writes a chain build's folder")
    folder.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def cmd_write(slug, unit):
    path, text = render_packet(slug, unit)
    if Path(path).is_file() and Path(path).read_bytes() == text.encode("utf-8"):
        print(f"packet: {path} is current, nothing written")
        return 0
    write_packet(path, text)
    print(f"packet: wrote {path}")
    return 0


def cmd_check(slug):
    src = derive_sources(slug)
    found = scan_packets(slug)
    if not found:
        raise Unmeasured(f"{slug} has no packet under memory/builds/{slug}/prompts/, so there is nothing to check")
    if len(found) > 1:
        raise Refusal(f"{slug} has {len(found)} packets ({', '.join(p.name for p in found)}), and a build has one")
    try:
        text = found[0].read_bytes().decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refusal(f"{found[0].as_posix()} is not UTF-8: {e}")
    pins, at = read_pins(text)
    findings, summary = check_text(text, render_text(src, pins, at or ""), src, read_head_blob)
    print(f"packet: {slug} · {found[0].as_posix()} · {summary}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


def cmd_repin(name):
    chain = list(read_tree()["rows"])
    live = scan_live_run(chain, read_file)
    if live:
        raise Refusal("--repin is the owner's, and never runs inside a chain run: " + "; ".join(live))
    inst = resolve_instrument(name)
    blob = read_head_blob(inst)
    if not blob:
        raise Refusal(f"{inst} is not tracked at HEAD, so it has no blob to pin")
    packets = []
    for s in chain:
        found = scan_packets(s)
        if len(found) > 1:
            raise Refusal(f"{s} has {len(found)} packets, and a build has one")
        packets += [(s, found[0])] if found else []
    if not packets:
        raise Unmeasured("no chain build has a packet, so there is nothing to re-pin")
    head = run_git("rev-parse", "HEAD").strip()
    for s, path in packets:
        pins, _at = read_pins(path.read_bytes().decode("utf-8"))
        if not pins:
            raise Refusal(f"{path.as_posix()} carries no instrument pin to keep")
        old = pins.get(inst)
        pins[inst] = blob
        write_packet(path.as_posix(), render_text(derive_sources(s), pins, head))
        print(f"packet: {s} · {inst} pinned {(old or 'nothing')[:12]} -> {blob[:12]} · {path.as_posix()}")
    return 0


def seed_fixture(src):
    """The sources with every arm's population made non-empty: a population the tree leaves empty is seeded, with
    FIXTURE ids no family declares, so no arm reads an empty population as covered."""
    s, slug = copy.deepcopy(src), src["slug"]
    if not any(x[0] == "owed" for x in s["lines"]):
        s["lines"].append(("owed", "fixture",
                           f"- a fixture line owed to {slug}, seeded because v2's `[owed]` names none"))
    if not s["roster"]:
        s["roster"] = [(f"FIXTURE-{slug}-{i}", i, f"| {i} | `FIXTURE-{slug}-{i}` | `{c['id']}@{c['pin']}` |")
                       for i, c in enumerate(s["clauses"], 1)]
    if not s["asks"]:
        s["asks"] = [{"id": "FIXTURE-dClosedLoop-1", "status": "OPEN", "where": "fixture",
                      "line": f"- FIXTURE-dClosedLoop-1 · filed 2026-10-20 · a fixture ask naming {slug}"}]
    return s


def run_fixture(slug, plant, control):
    full = seed_fixture(derive_sources(slug))
    label = (f"packet: fixture {slug}" + (f" · plant {plant}" if plant else "")
             + (f" · control {control}" if control else ""))
    if plant in ("run-live", "run-landed"):
        phase = "BUILDING" if plant == "run-live" else "LANDED"
        tree = {f"memory/builds/{slug}/RUN.md": f"# {slug} - run state\n\n## Run facts\nphase: {phase}\n"}
        live = scan_live_run(full["chain"], tree.get)
        print(f"{label} · --repin " + (f"refused: {'; '.join(live)}" if live else "not refused: no live chain run"))
        return 1 if live else 0
    head = run_git("rev-parse", "HEAD").strip()
    pins = {p: b for p in INSTRUMENTS if (b := read_head_blob(p))}
    blob_of = read_head_blob
    stub = copy.deepcopy(full)
    if plant == "clause":
        stub["clauses"].pop(len(stub["clauses"]) // 2)
    elif plant in ("gap", "parent", "roster", "ask"):
        stub[{"gap": "gaps", "parent": "parents", "roster": "roster", "ask": "asks"}[plant]].pop()
    elif plant == "owed":
        stub["lines"].remove(next(x for x in stub["lines"] if x[0] == "owed"))
    written = render_text(stub, pins, head)
    if plant == "hand-edit":
        written = written.replace("### Goal\n\n", "### Goal\n\nA hand edit.\n", 1)
    if plant == "pin":
        head_bytes = subprocess.run(["git", "show", f"HEAD:{INSTRUMENTS[0]}"], capture_output=True).stdout
        moved = derive_blob(head_bytes + b"#")          # carries.py with one byte added, as a commit would hold it
        blob_of = lambda p: moved if p == INSTRUMENTS[0] else read_head_blob(p)   # noqa: E731
        stub = copy.deepcopy(full)
        stub["lines"].append(("owed", "fixture-2", f"- a second fixture line owed to {slug}, landed after the render"))
        kept = {p: blob_of(p) for p in read_pins(written)[0]} if control == "repin" else read_pins(written)[0]
        written, full = render_text(stub, kept, head), stub     # the re-render --write makes
    pins_w, at_w = read_pins(written)
    findings, summary = check_text(written, render_text(stub, pins_w, at_w), full, blob_of, control != "no-pin-arm")
    print(f"{label} · {summary}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="packet.py", description="Render and check each chain build's packet.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", metavar="SLUG")
    mode.add_argument("--check", metavar="SLUG")
    mode.add_argument("--repin", metavar="INSTRUMENT")
    mode.add_argument("--fixture", action="store_true")
    ap.add_argument("--unit")
    ap.add_argument("--build", default="dTrueNorth")
    ap.add_argument("--plant", choices=PLANTS)
    ap.add_argument("--control", choices=CONTROLS)
    a = ap.parse_args(argv)
    if (a.plant or a.control or a.build != "dTrueNorth") and not a.fixture:
        ap.error("--build, --plant and --control go with --fixture")
    if a.control and a.plant != "pin":
        ap.error("--control is a control of the pin plant: pass --plant pin")
    if a.unit and not a.write:
        ap.error("--unit names a first render's unit: pass --write")
    try:
        if a.write:
            return cmd_write(a.write, a.unit)
        if a.check:
            return cmd_check(a.check)
        if a.repin:
            return cmd_repin(a.repin)
        return run_fixture(a.build, a.plant, a.control)
    except Refusal as e:
        print(f"packet: refused: {e}")
        return 1
    except Unmeasured as e:
        print(f"packet: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
